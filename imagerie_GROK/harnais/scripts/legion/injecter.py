"""Dépôt entrant/ : métadonnées, quatre portes, manifeste, page. Un refus explique."""
import hashlib, os, re, shutil
import attestations as A
import portes
import socle
import validate as V

ID_RE = re.compile(r"^(IMG-\d{3}|EXP-\d{3}|FTE-\d{2}|TEST-[A-Za-z0-9_-]+)$")
COTE = {"normal": "normal", "normale": "normal", "n": "normal",
        "pathologique": "patho", "patho": "patho", "p": "patho"}


def _sha(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for bloc in iter(lambda: f.read(1 << 16), b""):
            h.update(bloc)
    return h.hexdigest()


def _meta(path):
    brut = socle.lire_json(path, None)
    if not isinstance(brut, dict):
        return None, ["métadonnées illisibles"]
    alias = {
        "id": "id", "cote": "cote", "côté": "cote", "source": "source", "source_url": "source",
        "licence": "licence", "license": "licence", "auteur": "auteur", "author": "auteur",
        "age": "age", "âge": "age", "age_ans": "age", "sexe": "sexe", "sex": "sexe",
        "license_url": "license_url", "test_of": "test_of", "fantome": "fantome",
        "graine": "graine", "note": "note",
    }
    out = {}
    for k, v in brut.items():
        cle = alias.get(k, k)
        out[cle] = v
    return out, []


def _refus(image, lignes):
    dest = os.path.splitext(image)[0] + ".refus.md"
    corps = ["# Refus", "", f"Fichier : `{os.path.basename(image)}`", ""]
    corps += [f"- {l}" for l in lignes]
    corps += ["", "Aucune donnée patient n'est recopiée ici.", ""]
    with open(dest, "w", encoding="utf-8") as f:
        f.write("\n".join(corps))
    socle.journal("entrant_refus", fichier=os.path.basename(image), n=len(lignes))
    return dest


def _ecraser_masque(src, propre):
    if propre and os.path.isfile(propre) and os.path.abspath(propre) != os.path.abspath(src):
        shutil.copyfile(propre, src)


def traiter(dossier=None, racine=None, construire_page=False):
    racine = racine or socle.ROOT
    dossier = dossier or os.path.join(racine, "entrant")
    os.makedirs(dossier, exist_ok=True)
    resultats = []
    images = [f for f in sorted(os.listdir(dossier)) if f.lower().endswith((".jpg", ".jpeg", ".png", ".webp"))]
    ids_page = []
    for nom in images:
        image = os.path.join(dossier, nom)
        meta_path = os.path.splitext(image)[0] + ".json"
        recu_path = os.path.splitext(image)[0] + ".recu.json"
        if not os.path.isfile(meta_path):
            _refus(image, ["fichier de métadonnées absent (id, côté, source, licence, auteur, âge, sexe)"])
            resultats.append({"fichier": nom, "ok": False})
            continue
        meta, err = _meta(meta_path)
        if err:
            _refus(image, err)
            resultats.append({"fichier": nom, "ok": False})
            continue
        manques = [k for k in ("id", "cote", "source", "licence", "auteur", "age", "sexe") if meta.get(k) in (None, "")]
        if manques:
            _refus(image, ["champ absent : " + ", ".join(manques)])
            resultats.append({"fichier": nom, "ok": False})
            continue
        mid = str(meta["id"]).strip()
        if not ID_RE.match(mid):
            _refus(image, [f"identifiant refusé ({mid}) : attendu IMG, EXP, FTE ou TEST-"])
            resultats.append({"fichier": nom, "ok": False})
            continue
        fantome = bool(meta.get("fantome"))
        if mid.startswith("TEST-") and not fantome:
            _refus(image, ["un identifiant TEST exige fantome: true et l'absence de patient"])
            resultats.append({"fichier": nom, "ok": False})
            continue
        if fantome and not mid.startswith("TEST-"):
            _refus(image, ["un fantôme ne s'inscrit pas sur un identifiant clinique"])
            resultats.append({"fichier": nom, "ok": False})
            continue
        cote = COTE.get(str(meta["cote"]).strip().lower())
        if not cote:
            _refus(image, ["côté illisible : normal ou pathologique"])
            resultats.append({"fichier": nom, "ok": False})
            continue
        try:
            age = int(meta["age"])
        except (TypeError, ValueError):
            _refus(image, ["âge illisible"])
            resultats.append({"fichier": nom, "ok": False})
            continue
        sex = V.sex_code(meta.get("sexe"))
        if sex not in ("M", "F"):
            _refus(image, ["sexe non attesté (M ou F)"])
            resultats.append({"fichier": nom, "ok": False})
            continue
        sha = _sha(image)
        recu = socle.lire_json(recu_path, {})
        if recu.get("sha") == sha and recu.get("ok"):
            socle.journal("entrant_reprise", id=mid, fichier=nom)
            resultats.append({"fichier": nom, "ok": True, "reprise": True, "id": mid})
            if recu.get("test_of"):
                ids_page.append(recu["test_of"])
            elif not mid.startswith("TEST-"):
                ids_page.append(mid)
            continue
        dx = _dx(racine, meta, mid)
        if mid.startswith("TEST-") and (not meta.get("test_of") or not dx):
            _refus(image, ["TEST sans test_of connu dans diagnostics.json"])
            resultats.append({"fichier": nom, "ok": False})
            continue
        if not mid.startswith("TEST-") and racine == socle.ROOT and not dx:
            _refus(image, ["identifiant absent de diagnostics.json"])
            resultats.append({"fichier": nom, "ok": False})
            continue
        m = _charger_manifeste(racine, mid, meta, dx)
        if m.get("statut") == "complet":
            _refus(image, ["le manifeste est déjà complet : la légion n'y touche pas"])
            resultats.append({"fichier": nom, "ok": False, "id": mid})
            continue
        autre_nom = "normal" if cote == "patho" else "patho"
        autre = m.get(autre_nom) or {}
        vis = {"sex": autre.get("sex")} if autre.get("file") else None
        candidat = {
            "license": meta["licence"], "author": meta["auteur"], "source_url": meta["source"],
            "license_url": meta.get("license_url") or "",
            "age_ans": age, "sex": sex, "adulte": A.adulte_de(age),
            "preuve_age": f"{age} ans", "fichier": image,
            "dx": dx.get("dx") or "", "cliche": dx.get("cliche") or "",
            "origine": "entrant", "cle_dl": nom,
        }
        dest = os.path.join(os.path.dirname(image), "." + os.path.splitext(nom)[0] + ".masque.jpg")
        ok = portes.evaluer(candidat, dx, dest, vis_a_vis=vis)
        if candidat.get("fichier") and os.path.isfile(candidat["fichier"]) and candidat["fichier"] != image:
            _ecraser_masque(image, candidat["fichier"])
        if os.path.isfile(dest) and os.path.abspath(dest) != os.path.abspath(image):
            os.remove(dest)
        if not ok:
            r = candidat.get("refus") or {"porte": "?", "raison": "refusée"}
            _refus(image, [f"Porte {r['porte']} : {r['raison']}"])
            resultats.append({"fichier": nom, "ok": False, "id": mid})
            continue
        if autre.get("age_ans") is not None and not A.ages_comparables(age, autre.get("age_ans")):
            _refus(image, ["Porte paire : tranche d'âge non comparable avec le vis-à-vis"])
            resultats.append({"fichier": nom, "ok": False, "id": mid})
            continue
        if autre.get("file"):
            try:
                from PIL import Image
                with Image.open(image) as im1, Image.open(os.path.join(racine, autre["file"])) as im2:
                    from apparier import taille_comparable
                    if not taille_comparable(im1.size, im2.size):
                        _refus(image, ["Porte paire : tailles non comparables"])
                        resultats.append({"fichier": nom, "ok": False, "id": mid})
                        continue
            except Exception as e:
                _refus(image, [f"Porte paire : vis-à-vis illisible ({type(e).__name__})"])
                resultats.append({"fichier": nom, "ok": False, "id": mid})
                continue
        rel = _copier(racine, mid, cote, image)
        _ecrire_manifeste(racine, m, mid, cote, rel, candidat, meta, dx)
        sha2 = _sha(image)
        socle.ecrire_json(recu_path, {
            "ok": True, "id": mid, "cote": cote, "sha": sha2,
            "manifeste": os.path.basename(_chemin_manifeste(racine, mid)),
            "fichier": rel, "masques": candidat.get("masques") or 0,
            "test_of": meta.get("test_of") or "",
            "statut": "partiel",
        })
        refus_md = os.path.splitext(image)[0] + ".refus.md"
        if os.path.isfile(refus_md):
            os.remove(refus_md)
        etat = socle.charger(mid) if racine == socle.ROOT else {"id": mid}
        etat["graine"] = meta.get("graine")
        etat["fichier_segment"] = os.path.join(racine, rel)
        etat["insertion"] = "partiel"
        etat["statut_pose"] = "partiel"
        etat["dx"] = dx.get("dx") or etat.get("dx") or ""
        etat["cliche"] = dx.get("cliche") or etat.get("cliche") or ""
        etat["acceptes"] = [{
            "origine": "entrant",
            "source_url": meta.get("source") or "",
            "license": candidat.get("license") or "",
            "age_ans": age,
            "sex": sex,
            "adulte": A.adulte_de(age),
            "masques": candidat.get("masques") or 0,
            "cote": cote,
        }]
        if racine == socle.ROOT:
            socle.sauver(etat)
        socle.journal("entrant_ok", id=mid, fichier=nom, masques=candidat.get("masques") or 0)
        resultats.append({"fichier": nom, "ok": True, "id": mid, "fichier_manifeste": rel})
        ids_page.append(meta.get("test_of") or mid)
    page = ""
    if construire_page and ids_page and racine == socle.ROOT:
        page = _page(sorted(set(ids_page)))
    if racine == socle.ROOT:
        page_rel = os.path.relpath(page, socle.ROOT) if page else ""
        socle.ecrire_json(os.path.join(socle.RAPPORTS, "ENTRANT.json"),
                          {"resultats": resultats, "page": page_rel})
    return {"resultats": resultats, "page": page}


def _chemin_manifeste(racine, mid):
    return os.path.join(racine, "manifest", mid + ".json")


def _dx(racine, meta, mid):
    if racine == socle.ROOT:
        table = socle.diagnostics()
    else:
        brut = socle.lire_json(os.path.join(racine, "diagnostics.json"), [])
        table = {d["id"]: d for d in brut} if isinstance(brut, list) else (brut or {})
    cle = meta.get("test_of") if mid.startswith("TEST-") else mid
    return table.get(cle, {})


def _charger_manifeste(racine, mid, meta, dx):
    path = _chemin_manifeste(racine, mid)
    m = socle.lire_json(path, None)
    if m:
        return m
    m = {
        "id": mid,
        "dx": dx.get("dx") or "",
        "cliche": dx.get("cliche") or "",
        "statut": "partiel",
        "a_verifier": [],
        "queries": ["entrant"],
    }
    if mid.startswith("TEST-"):
        m["test_of"] = meta.get("test_of")
        m["a_verifier"] = ["Fantôme synthétique, aucun patient. Contour non promu."]
    return m


def _copier(racine, mid, cote, src):
    if mid.startswith("TEST-"):
        rel = f"legion/demo/images/{mid}_{cote}.jpg"
    else:
        rel = f"images/{'normal' if cote == 'normal' else 'patho'}/{mid}_{'normal' if cote == 'normal' else 'patho'}.jpg"
    dest = os.path.join(racine, rel)
    os.makedirs(os.path.dirname(dest), exist_ok=True)
    shutil.copyfile(src, dest)
    return rel


def _ecrire_manifeste(racine, m, mid, cote, rel, candidat, meta, dx):
    if m.get("statut") == "complet":
        return
    bloc = {
        "file": rel,
        "source_url": candidat.get("source_url") or "",
        "license": candidat.get("license") or "",
        "license_url": candidat.get("license_url") or "",
        "author": candidat.get("author") or "",
        "sex": candidat.get("sex") or "",
        "adulte": candidat.get("adulte") or "",
        "adulte_preuve": meta.get("note") or f"Métadonnée déposée : {candidat.get('age_ans')} ans, sexe {candidat.get('sex')}.",
        "age_ans": candidat.get("age_ans"),
        "anonymisation_verifiee": "oui" if candidat.get("anonymisation_verifiee") == "oui" else "non",
        "caption_source": meta.get("note") or "Dépôt entrant. Légende clinique non inventée.",
        "note": "Déposé dans entrant/. Statut partiel : aucun complet forcé.",
    }
    cle = "normal" if cote == "normal" else "patho"
    m[cle] = bloc
    m["statut"] = "partiel"
    m["dx"] = m.get("dx") or dx.get("dx") or ""
    m["cliche"] = m.get("cliche") or dx.get("cliche") or ""
    vis = "présente" if (m.get("normal") if cle == "patho" else m.get("patho")) else "absente"
    m["pair_match"] = (
        f"Image {cle} déposée et passée par les quatre portes. Vis-à-vis {vis}. "
        "Pas de définition sourcée ni de flèche relue : le statut reste partiel."
    )
    path = _chemin_manifeste(racine, mid)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    socle.ecrire_json(path, m)


def _page(ids):
    import subprocess, sys
    out = os.path.join(socle.DEMO, "Radio_Paires.html")
    cmd = [sys.executable, os.path.join(socle.SCRIPTS, "build_app.py"),
           "--external", "--include-test", "--only", ",".join(ids), "--out", out]
    r = subprocess.run(cmd, cwd=socle.ROOT)
    return out if r.returncode == 0 else ""
