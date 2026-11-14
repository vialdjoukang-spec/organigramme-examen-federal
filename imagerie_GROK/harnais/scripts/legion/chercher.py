"""Commons (imageinfo + extmetadata), Open-i et Europe PMC. Licence avant téléchargement."""
import os, re
import attestations as A
import europepmc
import fetch_commons as FC
import fetch_openi as FO
import licences as L
import portes
import socle
from _common import get

MAX_DL = 3


def interpreter(q):
    s = (q or "").strip()
    low = s.lower()
    if not s or "page d'erreur" in low or "rejetée" in low or "rejetee" in low:
        return None
    if low.startswith("commons cat"):
        cat = re.sub(r"(?i)^commons cat\s*:?\s*", "", s).strip(" :")
        return ("cat", cat) if cat else None
    if low.startswith("commons search"):
        rest = re.sub(r"(?i)^commons search\s*:?\s*", "", s).strip(" :")
        return ("search", rest) if rest else None
    if low.startswith("openi"):
        rest = re.sub(r"(?i)^openi\s*:?\s*", "", s)
        rest = rest.split("—")[0].strip(" :")
        return ("openi", rest) if rest else None
    return None


def plan(queries):
    actes, n_s, n_c, n_o = [], 0, 0, 0
    for q in queries or []:
        it = interpreter(q)
        if not it:
            continue
        kind, arg = it
        if kind == "search" and n_s < 2:
            actes.append(it)
            n_s += 1
        elif kind == "cat" and n_c < 1:
            actes.append(it)
            n_c += 1
        elif kind == "openi" and n_o < 1:
            actes.append(it)
            n_o += 1
    terme = ""
    for kind, arg in actes:
        if kind in ("search", "openi"):
            terme = re.sub(r"(?i)filetype:\S+", "", arg).strip()
            break
    if not terme and actes:
        terme = re.sub(r"(?i)filetype:\S+", "", actes[0][1]).strip()
    return actes, terme


def cote_suppose(caption):
    t = (caption or "").lower()
    if re.search(r"\b(normal|healthy|control|témoin|temoin)\b", t) and not re.search(
            r"\b(abnormal|patholog|lesion|lésion|fracture|mass)\b", t):
        return "normal"
    return ""


def _meta(origine, titre, source, lic, lic_url, author, caption, extra):
    age = A.age_ans(caption)
    sex = A.sexe(caption)
    return {
        "origine": origine,
        "titre": (titre or "")[:180],
        "source_url": source or "",
        "license": lic or "",
        "license_url": lic_url or "",
        "author": re.sub(r"\s+", " ", author or "")[:240],
        "age_ans": age,
        "sex": sex,
        "adulte": A.adulte_de(age),
        "cote": cote_suppose(caption),
        "preuve_age": A.phrase_age(caption),
        **extra,
    }


def _refus(liste, origine, porte, raison, url=""):
    liste.append({"origine": origine, "porte": porte, "raison": raison, "source_url": url or ""})


def chercher(mid, force=False):
    m, _ = socle.manifeste(mid)
    if not m:
        raise SystemExit("manifeste absent : " + mid)
    dx = socle.diagnostics().get(mid, {})
    actes, terme = plan(m.get("queries"))
    cle = socle.cle("fetch", socle.VERSION, mid, actes, terme)
    etat = socle.charger(mid)
    if not force and etat.get("cle_fetch") == cle and "candidats" in etat:
        socle.journal("fetch_reprise", id=mid, n=len(etat.get("candidats") or []))
        return etat
    dossier = os.path.join(socle.TRAVAIL, mid)
    os.makedirs(dossier, exist_ok=True)
    refus, bruts, faites = [], [], []

    for kind, arg in actes:
        faites.append(f"{kind}: {arg}")
        try:
            if kind == "search":
                recs = FC.search(arg, 6)
            elif kind == "cat":
                recs = FC.category(arg, 8)
            else:
                recs = FO.search(arg, 5)
        except Exception as e:
            _refus(refus, kind, "reseau", f"source injoignable ({type(e).__name__})")
            continue
        for r in recs:
            url = r.get("source_url") or ""
            if not L.licence_ok(r.get("license")):
                _refus(refus, kind, "licence",
                       f"licence hors liste blanche ({L.normaliser(r.get('license')) or 'absente'})", url)
                continue
            if not L.auteur_ok(r.get("author")):
                _refus(refus, kind, "licence", "auteur absent", url)
                continue
            if not L.url_ok(url):
                _refus(refus, kind, "licence", "URL de source absente", url)
                continue
            caption = r.get("description") or ""
            if A.age_ans(caption) is None or A.sexe(caption) not in ("M", "F"):
                _refus(refus, kind, "age_sexe", "âge ou sexe non attesté dans la légende", url)
                continue
            extra = {"img_url": r.get("img_url") or r.get("thumb_url") or r.get("orig_url") or ""}
            if kind == "openi":
                extra["cle_dl"] = r.get("key") or url
            else:
                extra["cle_dl"] = r.get("title") or url
                extra["img_url"] = r.get("thumb_url") or r.get("orig_url") or ""
            bruts.append(_meta("openi" if kind == "openi" else "commons",
                               r.get("title") or r.get("key"), url, r.get("license"),
                               r.get("license_url"), r.get("author"), caption, extra))

    if terme:
        faites.append("europepmc: " + terme)
        socle.ajouter_requete(mid, "europepmc: " + terme)
        try:
            arts = europepmc.articles(terme, n=3, max_figures=2)
        except Exception as e:
            _refus(refus, "europepmc", "reseau", f"source injoignable ({type(e).__name__})")
            arts = []
        for art in arts:
            if not art.get("accepte_licence"):
                _refus(refus, "europepmc", "licence", art.get("raison") or "licence refusée",
                       art.get("source_url") or "")
                continue
            utiles = []
            for fig in art.get("figures") or []:
                cap = fig.get("caption") or ""
                if A.age_ans(cap) is None or A.sexe(cap) not in ("M", "F"):
                    _refus(refus, "europepmc", "age_sexe", "âge ou sexe non attesté dans la légende",
                           art.get("source_url") or "")
                    continue
                utiles.append(fig)
            if not utiles:
                continue
            try:
                europepmc.charger_figures(art)
            except Exception as e:
                _refus(refus, "europepmc", "reseau", f"archive injoignable ({type(e).__name__})",
                       art.get("source_url") or "")
                continue
            for fig in utiles:
                if not fig.get("octets"):
                    _refus(refus, "europepmc", "figure", "figure absente de l'archive", art.get("source_url") or "")
                    continue
                extra = {"cle_dl": (art.get("pmcid") or "") + ":" + fig["href"], "octets": fig.get("octets")}
                bruts.append(_meta("europepmc", fig["href"], art.get("source_url"), art.get("license"),
                                   art.get("license_url"), art.get("author"), fig.get("caption") or "", extra))
                fig["octets"] = None
                fig["caption"] = ""

    vus, uniques = set(), []
    for c in bruts:
        k = c.get("cle_dl") or c.get("source_url")
        if k in vus:
            continue
        vus.add(k)
        uniques.append(c)
    uniques.sort(key=A.priorite)
    candidats = []
    for i, c in enumerate(uniques):
        if len(candidats) >= MAX_DL:
            _refus(refus, c["origine"], "quota", "quota de téléchargement atteint", c.get("source_url") or "")
            continue
        dest = os.path.join(dossier, f"{len(candidats)}.src")
        try:
            if c.get("octets"):
                open(dest, "wb").write(c["octets"])
                c["octets"] = None
            elif c.get("img_url"):
                open(dest, "wb").write(get(c["img_url"], binary=True))
            else:
                _refus(refus, c["origine"], "reseau", "URL d'image absente", c.get("source_url") or "")
                continue
        except Exception as e:
            _refus(refus, c["origine"], "reseau", f"téléchargement impossible ({type(e).__name__})",
                   c.get("source_url") or "")
            continue
        meta = {k: v for k, v in c.items() if k != "octets"}
        meta["fichier"] = dest
        candidats.append(meta)
        socle.journal("fetch", id=mid, origine=c["origine"], source_url=c.get("source_url") or "")

    etat.update({
        "cle_fetch": cle,
        "requetes": faites,
        "refus_fetch": refus,
        "candidats": candidats,
        "dx": dx.get("dx") or m.get("dx") or "",
        "cliche": dx.get("cliche") or m.get("cliche") or "",
        "region": dx.get("region") or "",
        "systeme": dx.get("systeme") or "",
    })
    socle.sauver(etat)
    socle.journal("fetch_fin", id=mid, candidats=len(candidats), refus=len(refus))
    return etat


def filtrer(mid, force=False):
    """Porte sur les fichiers déjà téléchargés. Reprise si la clé n'a pas changé."""
    etat = socle.charger(mid)
    if not etat.get("candidats") and "cle_fetch" not in etat:
        etat = chercher(mid, force=force)
    cle = socle.cle("gate", socle.VERSION, etat.get("cle_fetch"),
                    [c.get("cle_dl") for c in etat.get("candidats") or []])
    if not force and etat.get("cle_gate") == cle:
        socle.journal("gate_reprise", id=mid)
        return etat
    dx = {"id": mid, "dx": etat.get("dx"), "cliche": etat.get("cliche"),
          "region": etat.get("region"), "systeme": etat.get("systeme")}
    refus = []
    acceptes = []
    for c in etat.get("candidats") or []:
        brut = c.get("fichier") or ""
        dest = os.path.splitext(brut)[0] + ".jpg" if brut else ""
        if not brut:
            refus.append({"origine": c.get("origine"), "porte": "anonymisation",
                          "raison": "fichier absent", "source_url": c.get("source_url") or ""})
            continue
        portes.evaluer(c, dx, dest)
        if c.get("portes_ok"):
            if brut != c.get("fichier") and os.path.isfile(brut):
                os.remove(brut)
            acceptes.append(c)
            socle.journal("gate_ok", id=mid, origine=c.get("origine"), source_url=c.get("source_url") or "",
                          masques=c.get("masques") or 0)
        else:
            r = c.get("refus") or {"porte": "?", "raison": "refusée"}
            refus.append({"origine": c.get("origine"), "porte": r["porte"], "raison": r["raison"],
                          "source_url": c.get("source_url") or ""})
            for p in (brut, dest):
                if p and os.path.isfile(p):
                    os.remove(p)
            c["fichier"] = ""
            socle.journal("gate_refus", id=mid, porte=r["porte"], raison=r["raison"],
                          source_url=c.get("source_url") or "")
    etat["cle_gate"] = cle
    etat["refus_gate"] = refus
    etat["acceptes"] = [{k: v for k, v in c.items() if k != "octets"} for c in acceptes]
    socle.sauver(etat)
    return etat
