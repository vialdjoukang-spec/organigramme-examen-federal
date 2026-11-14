#!/usr/bin/env python3
"""Restaure les normales d'aspect adulte, trace les quatre thorax, injecte les partiels."""
import html
import json
import re
import subprocess
import sys
import unicodedata
from pathlib import Path

from PIL import Image

sys.path.insert(0, str(Path(__file__).resolve().parent))
import commun as C
import age_documenter as AD
import plausibilite as P
import rigueur as R
import segmenter_fenetres as SEG

BRANCHE = "origin/cursor/interface-didactique-ffbc"
MANIFEST = f"{BRANCHE}:imagerie_GROK/harnais/manifest"
IMAGES = f"{BRANCHE}:imagerie_GROK/harnais"
ANCIEN = "e7fa72cd5"
COULEURS = {
    "poumon-droit": "#7CFF4F",
    "poumon-gauche": "#4DFFDF",
    "mediastin": "#B388FF",
    "coeur": "#FF4DFF",
    "coupole-droite": "#FF9F1C",
    "coupole-gauche": "#FFD400",
}
PLAN_THORAX = [
    ("poumon-droit", 2, "Poumon droit", "air", 0.32, 0.42),
    ("poumon-gauche", 2, "Poumon gauche", "air", 0.68, 0.42),
    ("mediastin", 3, "Médiastin", "eau", 0.50, 0.40),
]
REGIONS = (
    (("encéph", "enceph", "cerveau", "crân", "cran", "tête", "tete", "eeg", "orbit", "sinus", "cou"), "TC", "Tête et cou"),
    (("thorax", "poumon", "plevr", "cœur", "coeur", "médiast", "mediast", "sein"), "TH", "Thorax"),
    (("abdomen", "foie", "hépat", "hepat", "rein", "pancré", "pancre", "rate"), "AB", "Abdomen"),
    (("pelv", "utér", "uter", "prostat", "vessie", "bassin"), "PE", "Pelvis"),
    (("main", "épaule", "epaule", "bras", "poignet"), "MS", "Membres supérieurs"),
    (("genou", "cheville", "hanche", "pied", "jambe", "fémur", "femur"), "MI", "Membres inférieurs"),
    (("rachis", "vertéb", "verteb"), "RA", "Rachis"),
)


def git_show(spec):
    return subprocess.check_output(["git", "show", spec], cwd=C.DEPOT)


def norm(texte):
    texte = unicodedata.normalize("NFKD", texte or "")
    texte = "".join(c for c in texte if not unicodedata.combining(c))
    texte = texte.lower()
    texte = re.sub(r"[^a-z0-9]+", " ", texte)
    return re.sub(r"\s+", " ", texte).strip()


def region_de(texte):
    t = norm(texte)
    for mots, code, nom in REGIONS:
        if any(norm(m) in t for m in mots):
            return code, nom
    return "TR", "Transversal et systémique"


def lettre_de(texte):
    t = norm(texte)
    if any(m in t for m in ("infect", "abses", "abscess", "pneumonie")):
        return "I"
    if any(m in t for m in ("tumeur", "cancer", "tumoral", "masse")):
        return "T"
    if any(m in t for m in ("trauma", "fracture")):
        return "Tr"
    if any(m in t for m in ("vascul", "arter", "thromb", "embolie")):
        return "V"
    if any(m in t for m in ("degener", "arthrose")):
        return "D"
    return "F"


def manifeste(nom):
    return json.loads(git_show(f"{MANIFEST}/{nom}"))


def lister_manifestes():
    noms = git_show(MANIFEST).decode().splitlines()
    return [n for n in noms if n.endswith(".json")]


def cote_image(bloc, ident, cote):
    """Retourne le bloc fichier ou un refus."""
    if not isinstance(bloc, dict) or not bloc.get("file"):
        return None
    licence = bloc.get("license") or ""
    if not C.licence_ok(licence):
        return {"refus": f"licence hors liste blanche ({licence or 'absente'})"}
    try:
        brut = git_show(f"{IMAGES}/{bloc['file']}")
    except subprocess.CalledProcessError:
        return {"refus": "fichier image absent du manifeste"}
    if C.donnees_patient(brut[:80000]):
        return {"refus": "données patient dans le fichier"}
    texte = " ".join(str(bloc.get(k) or "") for k in ("note", "caption_source", "author", "sex"))
    age, sexe_txt = AD.depuis_texte(texte)
    sexe = C._sexe(bloc.get("sex") or "") or sexe_txt
    n = R.age_nombre(age)
    if n is not None and n < 18:
        return {"refus": f"non adulte ({n} ans)"}
    dest = C.IMAGES / f"{ident}_{cote}.jpg"
    im = Image.open(__import__("io").BytesIO(brut)).convert("RGB")
    im.thumbnail((1200, 1200))
    im.save(dest, "JPEG", quality=85)
    info = {
        "fichier": f"images/{ident}_{cote}.jpg",
        "mime": "image/jpeg",
        "technique": " ".join(x for x in (bloc.get("modality"), bloc.get("plane"), bloc.get("sequence")) if x),
        "credit": re.sub(r"\s+", " ", bloc.get("author") or "")[:180],
        "licence": licence,
        "url": bloc.get("source_url") or "",
        "note": re.sub(r"\s+", " ", bloc.get("note") or "")[:500],
        "age": age if n is not None and n >= 18 else "",
        "sexe": sexe,
        "aspect_adulte": not (n is not None and n >= 18),
        "age_preuve": "légende du manifeste" if n is not None and n >= 18 else "",
    }
    return info


def ligne_de(ident, doc, famille):
    dx = doc.get("dx") or ident
    code, reg = region_de(f"{dx} {doc.get('cliche') or ''}")
    titre = html.escape(dx)
    return {
        "id": ident,
        "r": code,
        "s": reg,
        "l": lettre_de(dx),
        "n": "C",
        "t": (doc.get("cliche") or "")[:80],
        "q": norm(dx),
        "sh": reg,
        "dxt": titre,
        "c": {
            "dx": (
                f'<button type="button" class="dxb" data-p="{famille}" data-dx="{ident}" '
                f'aria-haspopup="dialog">{titre}</button>'
            ),
            "niv": '<span class="niv c" title="Cible complète">cible</span>',
            "ex": "",
            "sg": html.escape((doc.get("cliche") or "")[:220]),
            "exi": "",
            "fct": html.escape((doc.get("cliche") or "")[:120]),
        },
    }


def restaurer():
    rapport = C.lire_json(C.SIGNAUX / "rigueur.json")
    rendues, enfants = [], []
    for ligne in rapport["retires"]:
        ident, motif = ligne.split(" — ", 1)
        if motif.startswith("non adulte"):
            enfants.append(ligne)
            continue
        ancien = json.loads(git_show(f"{ANCIEN}:imagerie_GROK/fedmed/fusion/{ident}.json"))
        fusion = C.lire_json(C.FUSION / f"{ident}.json")
        src = ancien["gabarit"]["normal"]
        g = fusion["gabarit"].setdefault("normal", {})
        g["structures"] = src.get("structures") or []
        g["refus"] = ""
        g["age"] = ""
        g["sexe"] = src.get("sexe") or ""
        g["aspect_adulte"] = True
        g.pop("age_preuve", None)
        if src.get("source"):
            g["source"] = src["source"]
        retraits = fusion.get("retraits") or {}
        retraits.pop("normal", None)
        if retraits:
            fusion["retraits"] = retraits
        else:
            fusion.pop("retraits", None)
        fusion["normal_ajoute"] = ancien.get("normal_ajoute")
        fusion["signaux"] = [
            s for s in fusion.get("signaux") or []
            if not s.startswith("Normale retirée") and "hors de l'enveloppe" not in s
        ]
        fusion["id"] = ident
        masques, _ = R.appliquer_enveloppe(fusion, C.lire_json(C.FENETRES / f"{ident}.json"))
        C.ecrire_json(C.FUSION / f"{ident}.json", fusion)
        rendues.append(ident)
    return rendues, enfants


def bande_basse(contour, cote):
    """Bord inférieur du poumon : la coupole, en bande étroite."""
    bas = [p for p in contour if p[1] >= 0.52 and (p[0] < 0.48 if cote == "droite" else p[0] > 0.52)]
    if len(bas) < 4:
        return None
    bas = sorted(bas, key=lambda p: p[0])
    haut = [[p[0], round(p[1] - 0.03, 4)] for p in bas]
    return bas + haut[::-1]


def partie_basse(contour):
    """Moitié inférieure du médiastin : le cœur, sans dupliquer le contour entier."""
    ys = [p[1] for p in contour]
    seuil = min(ys) + (max(ys) - min(ys)) * 0.42
    bas = [p for p in contour if p[1] >= seuil - 0.01]
    if len(bas) < 6:
        return None
    return bas


def tracer_thorax():
    seg = SEG.module_segment()
    gardes = {}
    for ident in ("IMG-118", "IMG-123", "IMG-134", "IMG-153"):
        fusion = C.lire_json(C.FUSION / f"{ident}.json")
        fusion["signaux"] = [
            s for s in fusion.get("signaux") or []
            if "hors de l'enveloppe" not in s and "(normal)" not in s
        ]
        path = C.FENETRES / fusion["normal_ajoute"]["fichier"]
        im = SEG.gris(path)
        bruts = {}
        for sid, ordre, nom, mode, x, y in PLAN_THORAX:
            try:
                contour, _, _ = seg.contour_from_seed(im, x, y, mode, n=28)
            except Exception:
                contour = None
            if contour:
                bruts[sid] = contour
        structures = []

        def ajouter(sid, nom, ordre, contour):
            if not contour or len(contour) < 8:
                return
            st = {
                "id": sid, "nom": nom, "ordre": ordre, "couleur": COULEURS[sid],
                "contour": contour, "aspect": "", "aspect_source": "", "approximatif": True,
            }
            raison = P.individuel(st)
            if sid.startswith("coupole"):
                b = P.boite(contour)
                ymin = min(p[1] for p in contour)
                if not (0.004 <= b["aire"] <= 0.12 and b["cy"] >= 0.58 and ymin >= 0.50):
                    raison = raison or "position de coupole invraisemblable"
                else:
                    raison = ""
            if raison:
                fusion.setdefault("signaux", []).append(f"Contour masqué : {nom} (normal) — {raison}.")
                return
            structures.append(st)

        for sid in ("poumon-droit", "poumon-gauche"):
            ajouter(sid, "Poumon droit" if sid.endswith("droit") else "Poumon gauche", 2, bruts.get(sid))
        ajouter("mediastin", "Médiastin", 3, bruts.get("mediastin"))
        ajouter("coeur", "Cœur", 3, partie_basse(bruts.get("mediastin") or []))
        ajouter("coupole-droite", "Coupole diaphragmatique droite", 4, bande_basse(bruts.get("poumon-droit") or [], "droite"))
        ajouter("coupole-gauche", "Coupole diaphragmatique gauche", 4, bande_basse(bruts.get("poumon-gauche") or [], "gauche"))
        fusion["gabarit"]["normal"]["structures"] = structures
        fusion["id"] = ident
        R.appliquer_enveloppe(fusion, C.lire_json(C.FENETRES / f"{ident}.json"))
        C.ecrire_json(C.FUSION / f"{ident}.json", fusion)
        gardes[ident] = [s["nom"] for s in fusion["gabarit"]["normal"]["structures"]]
    return gardes


def injecter_partiels():
    fed = set(C.lire_json(C.FENETRES / "index.json")["ids"])
    injectes, ecartes, introuvables, sans_statut = [], [], [], []
    for nom in lister_manifestes():
        ident = nom[:-5]
        doc = manifeste(nom)
        statut = doc.get("statut") or ""
        if ident in fed:
            continue
        if statut == "introuvable":
            introuvables.append(ident + " — " + (doc.get("dx") or ""))
            continue
        if statut != "partiel":
            sans_statut.append(ident + " — " + (doc.get("dx") or "sans titre"))
            continue
        normal = cote_image(doc.get("normal") or {}, ident, "normal")
        patho = cote_image(doc.get("patho") or {}, ident, "patho")
        images = {}
        mime = {}
        gabarit = {"normal": {}, "patho": {}, "cartes": [], "signaux": [], "indices": []}
        utile = False
        for cote, info in (("normal", normal), ("patho", patho)):
            g = {"structures": [], "lesions": [], "source": {}, "age": "", "sexe": "", "refus": ""}
            if not info:
                g["refus"] = "image absente"
            elif info.get("refus"):
                g["refus"] = info["refus"]
                gabarit["signaux"].append(f"{cote} : {info['refus']}.")
            else:
                utile = True
                images[cote] = {
                    "fichier": info["fichier"],
                    "technique": info["technique"],
                    "credit": info["credit"],
                    "licence": info["licence"],
                    "url": info["url"],
                }
                mime[cote] = "image/jpeg"
                g["age"] = info["age"]
                g["sexe"] = info["sexe"]
                g["aspect_adulte"] = info["aspect_adulte"]
                if info["age_preuve"]:
                    g["age_preuve"] = info["age_preuve"]
                g["source"] = {
                    "auteur": info["credit"],
                    "licence": info["licence"],
                    "url": info["url"],
                    "credit": info["note"],
                }
            gabarit[cote] = g
        if not utile:
            ecartes.append(ident + " — " + (doc.get("dx") or "") + " — aucune image admissible")
            continue
        if patho and not patho.get("refus"):
            lesions = []
            for fleche in (doc.get("patho") or {}).get("arrows") or []:
                contour = fleche.get("contour") or []
                if len(contour) < 3:
                    continue
                lesions.append({
                    "label": fleche.get("label") or "Repère",
                    "semio": R.aplatir(fleche.get("definition") or "")[0],
                    "contour": contour,
                    "couleur": "#FF1744",
                    "approximatif": False,
                })
            gabarit["patho"]["lesions"] = lesions
        note = R.aplatir((doc.get("pair_match") or "")[:700])[0]
        if note:
            gabarit["cartes"].append({"titre": "Lecture", "texte": note})
        famille = "exp" if ident.startswith("EXP-") else "img"
        fusion = {
            "id": ident,
            "complement": True,
            "famille": famille,
            "ligne": ligne_de(ident, doc, famille),
            "placement_dx": doc.get("dx") or ident,
            "gabarit": gabarit,
            "signaux": gabarit["signaux"],
        }
        fiche = {
            "id": ident,
            "contexte": {"id": ident, "dx": doc.get("dx") or "", "region": region_de(doc.get("dx") or "")[1]},
            "mime": mime,
            "enr": {"images": images},
        }
        fusion["id"] = ident
        R.appliquer_enveloppe(fusion, fiche)
        gabarit["signaux"] = fusion.get("signaux") or []
        C.ecrire_json(C.FENETRES / f"{ident}.json", fiche)
        C.ecrire_json(C.FUSION / f"{ident}.json", fusion)
        injectes.append(ident + " — " + (doc.get("dx") or ""))
    index = C.lire_json(C.FENETRES / "index.json")
    for ligne in injectes:
        ident = ligne.split(" — ", 1)[0]
        if ident not in index["ids"]:
            index["ids"].append(ident)
    C.ecrire_json(C.FENETRES / "index.json", index)
    etat = {"injectes": injectes, "ecartes": ecartes, "introuvables": introuvables, "sans_statut": sans_statut}
    C.ecrire_json(C.SIGNAUX / "partiels.json", etat)
    return etat


def main():
    rendues, enfants = restaurer()
    thorax = tracer_thorax()
    etat = injecter_partiels()
    print("restaurées", len(rendues))
    print("enfants laissés retirés", len(enfants))
    for ident, noms in thorax.items():
        print(ident, ", ".join(noms) or "aucun contour")
    print("partiels injectés", len(etat["injectes"]), "écartés", len(etat["ecartes"]))
    print("introuvables", len(etat["introuvables"]), "sans statut", len(etat["sans_statut"]))


if __name__ == "__main__":
    main()
