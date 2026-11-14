#!/usr/bin/env python3
"""Fusionne le texte du fichier Drive et l'apport local des manifestes."""
import argparse
import hashlib
import json
import re
import subprocess
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import commun as C

FIXES = {
    "paroi": "#00E5FF",
    "poumon-droit": "#7CFF4F",
    "poumon-gauche": "#4DFFDF",
    "coeur": "#FF4DFF",
    "diaphragme": "#FF9F1C",
}
CYCLE = ["#00E5FF", "#7CFF4F", "#4DFFDF", "#FF4DFF", "#FF9F1C", "#FFD400", "#B388FF", "#82B1FF", "#FF8A80", "#CCFF90"]
LESIONS = ["#FF1744", "#651FFF", "#2962FF", "#FF6D00", "#C51162", "#00B8D4", "#AA00FF", "#DD2C00"]
SENSIBLES = ("bassin", "sein", "génit", "genit", "pelvis", "utér", "uter", "prostat", "ovari")
ALIASES = {
    "rx": ("rx", "radio", "x-ray", "cliché", "cliche"),
    "tdm": ("tdm", "scanner", "ct"),
    "irm": ("irm", "mri"),
    "us": ("echo", "éch", "ech", "ultras"),
}
_MANIFESTES = {}
_OCTETS = {}


VERBES = re.compile(
    r"^(ne |n['’]|montre|caractérise|détecte|detecte|distingue|irradie|mesure|reste|manque|"
    r"date|explore|dépend|depend|voit|signe|permet|évite|evite|confirme|exclut|localise|"
    r"quantifie|différencie|differencie|se |sous-type|met|donne|apporte|guide|classe|"
    r"précise|precise|visualise|objective|retrouve|identifie|élimine|elimine|limite|"
    r"couvre|suit|repose|exige|nécessite|necessite|décrit|decrit|compare|grade)",
    re.I,
)


def net(s):
    s = re.sub(r"\s+", " ", (s or "").replace("\xa0", " ")).strip()
    return re.sub(r"\s+,", ",", s)


def verbaliser(fragment):
    f = net(fragment).rstrip(".")
    if not f:
        return ""
    if VERBES.match(f):
        return "elle " + f[0].lower() + f[1:]
    return f


def joindre(items):
    propres = [net(x).rstrip(" .;") for x in (items or []) if net(x)]
    if not propres:
        return ""
    texte = propres[0] if len(propres) == 1 else " ; ".join(propres)
    texte = texte[0].upper() + texte[1:]
    if texte[-1] not in ".!?":
        texte += "."
    return texte


def minuscule(phrase):
    if not phrase:
        return ""
    return phrase[0].lower() + phrase[1:]


def manifeste(ident):
    if ident in _MANIFESTES:
        return _MANIFESTES[ident]
    rel = f"imagerie_GROK/harnais/manifest/{ident}.json"
    obj = None
    try:
        brut = subprocess.check_output(
            ["git", "show", f"{C.REF_INTERFACE}:{rel}"],
            cwd=C.DEPOT,
            stderr=subprocess.DEVNULL,
        )
        obj = json.loads(brut)
    except (subprocess.CalledProcessError, json.JSONDecodeError):
        local = C.DEPOT / rel
        if local.is_file():
            obj = json.loads(local.read_text(encoding="utf-8"))
    _MANIFESTES[ident] = obj
    return obj


def octets_harnais(rel):
    if rel in _OCTETS:
        return _OCTETS[rel]
    chemin = f"imagerie_GROK/harnais/{rel}"
    blob = b""
    try:
        blob = subprocess.check_output(
            ["git", "show", f"{C.REF_INTERFACE}:{chemin}"],
            cwd=C.DEPOT,
            stderr=subprocess.DEVNULL,
        )
    except subprocess.CalledProcessError:
        local = C.DEPOT / "imagerie_GROK" / "harnais" / rel
        if local.is_file():
            blob = local.read_bytes()
    _OCTETS[rel] = blob
    return blob


def couleur_structure(sid):
    if sid in FIXES:
        return FIXES[sid]
    rang = int(hashlib.sha256(sid.encode("utf-8")).hexdigest()[:2], 16)
    return CYCLE[rang % len(CYCLE)]


def source_aspect(texte):
    brut = net(texte)
    if brut.lower() in {"", "à vérifier", "a vérifier"}:
        return C.PHRASE_NON_SOURCEE
    return brut


def xy_repere(valeur, echelle):
    x = float(valeur)
    if echelle:
        x = x / 100.0
    return round(x, 4)


def point(pair):
    if not isinstance(pair, (list, tuple)) or len(pair) < 2:
        return None
    try:
        x, y = float(pair[0]), float(pair[1])
    except (TypeError, ValueError):
        return None
    if x > 1 or y > 1:
        x, y = x / 100.0, y / 100.0
    if not (0 <= x <= 1 and 0 <= y <= 1):
        return None
    return [round(x, 4), round(y, 4)]


def contour_de(points):
    propre = []
    for p in points or []:
        q = point(p)
        if q:
            propre.append(q)
    if len(propre) >= 3 and propre[0] != propre[-1]:
        propre.append(propre[0])
    return propre if len(propre) >= 4 else []


def structures_de(cote, identique):
    if not identique or not isinstance(cote, dict):
        return []
    out = []
    for st in cote.get("anatomie") or []:
        if not isinstance(st, dict):
            continue
        sid = net(st.get("id") or st.get("nom") or "")
        if not sid:
            continue
        aspect = net(st.get("aspect") or st.get("description") or "")
        src = source_aspect(st.get("aspect_source") or st.get("source"))
        if aspect and src == C.PHRASE_NON_SOURCEE and not net(st.get("aspect")):
            aspect = net(st.get("description"))
        out.append({
            "id": sid,
            "nom": net(st.get("nom") or sid),
            "ordre": int(st.get("ordre") or 1),
            "couleur": couleur_structure(sid),
            "contour": contour_de(st.get("contour")),
            "aspect": aspect,
            "aspect_source": src if aspect else "",
        })
    out.sort(key=lambda s: s["ordre"])
    return out


def lesions_fichier(im):
    patho = im.get("patho") if isinstance(im.get("patho"), dict) else {}
    out = []
    for i, rep in enumerate(patho.get("reperes") or []):
        if not isinstance(rep, dict):
            continue
        try:
            brut = [float(rep[k]) for k in ("x", "y", "fx", "fy")]
            echelle = max(brut) > 1
            tip = [xy_repere(rep["x"], echelle), xy_repere(rep["y"], echelle)]
            depart = [xy_repere(rep["fx"], echelle), xy_repere(rep["fy"], echelle)]
        except (KeyError, TypeError, ValueError):
            continue
        out.append({
            "label": net(rep.get("lesion") or f"Lésion {i+1}"),
            "semio": net(rep.get("semio") or ""),
            "tip": tip,
            "from": depart,
            "contour": [],
            "couleur": LESIONS[i % len(LESIONS)],
            "role": "principale" if i == 0 else "associee",
        })
    return out


def lesions_manifeste(cote, de_base):
    fleches = (cote or {}).get("arrows") or []
    if not fleches:
        return de_base
    out = []
    for i, fleche in enumerate(fleches):
        if not isinstance(fleche, dict):
            continue
        tip = point(fleche.get("tip"))
        depart = point(fleche.get("from"))
        if not tip or not depart:
            continue
        semio = ""
        if i < len(de_base):
            semio = de_base[i].get("semio") or ""
        definition = net(fleche.get("definition") or "")
        src = source_aspect(fleche.get("definition_source"))
        if definition and src == C.PHRASE_NON_SOURCEE:
            semio = semio or definition
        out.append({
            "label": net(fleche.get("label") or f"Lésion {i+1}"),
            "semio": semio or (definition if src != C.PHRASE_NON_SOURCEE else definition),
            "tip": tip,
            "from": depart,
            "contour": contour_de(fleche.get("contour")),
            "couleur": LESIONS[i % len(LESIONS)],
            "role": fleche.get("role") or "principale",
            "definition_source": src,
        })
    return out or de_base


def carte_semio(lesions):
    morceaux = []
    for lesion in lesions:
        if lesion.get("label") and lesion.get("semio"):
            morceaux.append(f"{lesion['label']} : {lesion['semio'].rstrip('.')}")
        elif lesion.get("label") or lesion.get("semio"):
            morceaux.append(lesion.get("label") or lesion.get("semio"))
    return joindre(morceaux)


def carte_reference(gold):
    if not isinstance(gold, dict):
        return ""
    morceaux = []
    examen = net(gold.get("examen"))
    if examen:
        morceaux.append(examen if examen.endswith(".") else examen + ".")
    pourquoi = joindre(verbaliser(x) for x in (gold.get("pourquoi") or []))
    if pourquoi:
        morceaux.append("C'est l'examen de référence : " + minuscule(pourquoi))
    premiere = net(gold.get("premiere_intention"))
    if premiere:
        morceaux.append("En première intention : " + premiere.rstrip(".") + ".")
    quand = joindre(gold.get("quand") or [])
    if quand:
        morceaux.append("On la demande dans ces situations : " + minuscule(quand))
    montre = joindre(verbaliser(x) for x in (gold.get("montre") or []))
    if montre:
        morceaux.append(minuscule(montre) if montre.lower().startswith("elle ") else "Elle montre " + minuscule(montre))
    return " ".join(morceaux)


def carte_autres(autres):
    lignes = []
    for autre in autres or []:
        if not isinstance(autre, dict):
            continue
        nom = net(autre.get("examen"))
        if not nom:
            continue
        phrase = nom.rstrip(".") + "."
        pourquoi = joindre(verbaliser(x) for x in (autre.get("pourquoi_pas_gold") or []))
        if pourquoi:
            phrase += " Ce n'est pas la référence : " + minuscule(pourquoi)
        quand = joindre(autre.get("quand") or [])
        if quand:
            phrase += " On la demande quand même dans ces situations : " + minuscule(quand)
        montre = joindre(autre.get("montre") or [])
        if montre:
            phrase += " On y voit : " + minuscule(montre)
        lignes.append(phrase)
    return " ".join(lignes)


def carte_aspects(structures, lesions, technique):
    lignes = []
    for st in structures:
        if not st.get("aspect"):
            continue
        lignes.append(f"{st['nom']} : {st['aspect'].rstrip('.')} ({st['aspect_source']})")
    for lesion in lesions:
        if lesion.get("semio"):
            continue
        label = lesion.get("label") or "La lésion"
        tech = net(technique) or "ce cliché"
        lignes.append(f"{label} : on la reconnaît sur {tech} ({C.PHRASE_NON_SOURCEE})")
    return " ".join(lignes)


def source_de(bloc, cote_manifeste):
    bloc = bloc or {}
    man = cote_manifeste or {}
    return {
        "auteur": net(bloc.get("credit") or man.get("author") or ""),
        "licence": net(bloc.get("licence") or man.get("license") or ""),
        "url": net(bloc.get("url") or man.get("source_url") or ""),
        "credit": net(bloc.get("technique") or man.get("caption_source") or ""),
    }


def ages_proches(a, b):
    def n(v):
        m = re.search(r"\d+", v or "")
        return int(m.group(0)) if m else None
    na, nb = n(a), n(b)
    if na is None or nb is None:
        return True
    return abs(na - nb) <= 15


def modalite_ok(technique, modality):
    tech = (technique or "").lower()
    mod = (modality or "").lower()
    if not mod or not tech:
        return True
    for words in ALIASES.values():
        if any(w in mod for w in words):
            return any(w in tech for w in words)
    return True


def region_sensible(texte):
    t = (texte or "").lower()
    return any(m in t for m in SENSIBLES)


def controler_drive(cote, blob, man, meme):
    bloc = cote or {}
    licence = bloc.get("licence") or ""
    age, sexe = C.age_sexe_texte(" ".join([bloc.get("credit") or "", bloc.get("technique") or ""]))
    if meme:
        aa, ss = C.age_sexe_manifeste(man)
        age = age or aa
        sexe = sexe or ss
    blocage = []
    if not C.licence_ok(licence):
        blocage.append(f"licence hors liste blanche ({licence or 'absente'})")
    if C.donnees_patient(blob):
        blocage.append("données patient")
    signaux = []
    if not age or not sexe:
        signaux.append("âge ou sexe absent")
    return blocage, signaux, age, sexe


def controler_local(man, blob):
    raisons = []
    if not isinstance(man, dict):
        return ["manifeste absent"]
    if not C.licence_ok(man.get("license")):
        raisons.append(f"licence hors liste blanche ({man.get('license') or 'absente'})")
    age, sexe = C.age_sexe_manifeste(man)
    if not age:
        raisons.append("âge absent")
    if not sexe:
        raisons.append("sexe absent")
    if not (man.get("author") or "").strip() or not str(man.get("source_url") or "").startswith("http"):
        raisons.append("auteur ou URL absents")
    if C.donnees_patient(blob):
        raisons.append("données patient")
    return raisons


def echantillon(index):
    ids = index["ids"]
    present = set(ids)
    sans = set(index["sans_normale"])
    choix = []

    def add(seq):
        for ident in seq:
            if ident in present and ident not in choix:
                choix.append(ident)

    add(["IMG-134", "IMG-001", "IMG-136", "IMG-267"])
    exp = [i for i in ids if i.startswith("EXP-")]
    add([i for i in exp if i not in sans][:2])
    add([i for i in exp if i in sans][:2])
    add([i for i in ids if i in sans and i.startswith("IMG-")][:2])
    return choix[:10]


def fusionner_une(fiche):
    ident = fiche["id"]
    enr = fiche["enr"]
    im = enr.get("images") or {}
    man = manifeste(ident) or {}
    ctx = fiche.get("contexte") or {}
    signaux = []
    retraits = {}
    normal_ajoute = None
    sha = fiche.get("sha256") or {}

    def cote_local(nom):
        bloc = man.get(nom) if isinstance(man.get(nom), dict) else {}
        rel = bloc.get("file") or ""
        blob = octets_harnais(rel) if rel else b""
        meme = bool(blob) and hashlib.sha256(blob).hexdigest() == sha.get(nom)
        return bloc, blob, meme, rel

    patho_m, patho_blob_local, patho_meme, _ = cote_local("patho")
    normal_m, normal_blob_local, normal_meme, normal_rel = cote_local("normal")
    patho = im.get("patho") if isinstance(im.get("patho"), dict) else {}
    normal = im.get("normal") if isinstance(im.get("normal"), dict) else {}
    patho_bytes = b""
    if sha.get("patho"):
        chemin = C.FENETRES / (patho.get("fichier") or "")
        if chemin.is_file():
            patho_bytes = chemin.read_bytes()
    blocage, alerte, age_p, sexe_p = controler_drive(patho, patho_bytes, patho_m, patho_meme)
    if blocage:
        retraits["patho"] = " ; ".join(blocage)
        signaux.append("Pathologique retirée : " + retraits["patho"] + ".")
    elif alerte:
        signaux.append("Pathologique signalée : " + " ; ".join(alerte) + ".")

    a_normal = isinstance(normal.get("fichier"), str) and normal.get("fichier", "").startswith("images/")
    age_n, sexe_n = "", ""
    if a_normal:
        normal_bytes = (C.FENETRES / normal["fichier"]).read_bytes()
        blocage_n, alerte_n, age_n, sexe_n = controler_drive(normal, normal_bytes, normal_m, normal_meme)
        if blocage_n:
            retraits["normal"] = " ; ".join(blocage_n)
            signaux.append("Normale retirée : " + retraits["normal"] + ".")
            a_normal = False
        elif alerte_n:
            signaux.append("Normale signalée : " + " ; ".join(alerte_n) + ".")
    if not a_normal and normal_rel:
        raisons = controler_local(normal_m, normal_blob_local)
        technique = patho.get("technique") or ""
        if raisons:
            signaux.append("Normale locale non ajoutée (" + " ; ".join(raisons) + ").")
        elif not modalite_ok(technique, normal_m.get("modality")):
            signaux.append("Normale locale non ajoutée : modalité différente du cliché pathologique.")
        elif not ages_proches(age_p, C.age_sexe_manifeste(normal_m)[0]):
            signaux.append("Normale locale non ajoutée : écart d'âge supérieur à 15 ans.")
        elif region_sensible(ctx.get("region")) and sexe_p and C.age_sexe_manifeste(normal_m)[1] not in {"", sexe_p}:
            signaux.append("Normale locale non ajoutée : sexe discordant sur une région où il change l'anatomie.")
        else:
            ext = "jpg" if (normal_m.get("file") or "").endswith(".jpg") else Path(normal_rel).suffix.lstrip(".") or "jpg"
            nom = f"{ident}_normal.{ext if ext != 'jpeg' else 'jpg'}"
            dest = C.IMAGES / nom
            dest.write_bytes(normal_blob_local)
            age_n, sexe_n = C.age_sexe_manifeste(normal_m)
            normal_ajoute = {
                "fichier": f"images/{nom}",
                "mime": "image/jpeg" if nom.endswith(".jpg") else "image/" + ext,
                "technique": " ".join(x for x in (normal_m.get("modality"), normal_m.get("sequence"), normal_m.get("plane")) if x),
                "credit": net(normal_m.get("author") or ""),
                "licence": net(normal_m.get("license") or ""),
                "url": net(normal_m.get("source_url") or ""),
            }
            normal = {
                "credit": normal_ajoute["credit"],
                "licence": normal_ajoute["licence"],
                "url": normal_ajoute["url"],
                "technique": normal_ajoute["technique"],
            }
            normal_meme = True
            signaux.append("Normale locale ajoutée.")

    structures_n = structures_de(normal_m, normal_meme or bool(normal_ajoute))
    structures_p = structures_de(patho_m, patho_meme and "patho" not in retraits)
    lesions = lesions_fichier(im)
    if patho_meme and "patho" not in retraits:
        lesions = lesions_manifeste(patho_m, lesions)
    for lesion in lesions:
        if not lesion.get("semio"):
            lesion["semio_source"] = C.PHRASE_NON_SOURCEE

    cartes = []
    semio = carte_semio(lesions)
    if semio:
        cartes.append({"titre": "Sémiologie", "texte": semio})
    reference = carte_reference(enr.get("gold"))
    if reference:
        cartes.append({"titre": "Examen de référence", "texte": reference})
    autres = carte_autres(enr.get("autres"))
    if autres:
        cartes.append({"titre": "Pourquoi pas l'examen de référence", "texte": autres})
    aspects = carte_aspects(structures_n + structures_p, lesions, patho.get("technique"))
    if aspects:
        cartes.append({"titre": "Aspects", "texte": aspects})

    indices = []
    if ctx.get("dx"):
        indices.append("Diagnostic : " + ctx["dx"])
    if ctx.get("region"):
        indices.append("Région : " + ctx["region"])
    signe = lesions[0]["label"] if lesions else ctx.get("signe")
    if signe:
        indices.append("Signe : " + signe)

    def cote_gabarit(info_drive, structures, age, sexe, refus):
        return {
            "age": age,
            "sexe": sexe,
            "source": source_de(info_drive, None),
            "refus": refus,
            "structures": structures,
        }

    gabarit = {
        "normal": cote_gabarit(normal, structures_n, age_n, sexe_n, retraits.get("normal", "")),
        "patho": cote_gabarit(patho, structures_p, age_p, sexe_p, retraits.get("patho", "")),
        "cartes": cartes,
        "indices": indices,
        "signaux": signaux,
    }
    gabarit["patho"]["lesions"] = [] if retraits.get("patho") else lesions
    return {
        "id": ident,
        "retraits": retraits,
        "normal_ajoute": normal_ajoute,
        "gabarit": gabarit,
        "signaux": signaux,
    }


def selection(args, index, faits):
    if args.ids:
        return [i.strip() for i in args.ids.split(",") if i.strip()]
    pool = echantillon(index) if args.echantillon else list(index["ids"])
    reste = [i for i in pool if i not in faits or args.force]
    if args.limite:
        reste = reste[: args.limite]
    return reste


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--limite", type=int, default=0)
    ap.add_argument("--ids", default="")
    ap.add_argument("--echantillon", action="store_true")
    ap.add_argument("--force", action="store_true")
    args = ap.parse_args()
    index = C.lire_json(C.FENETRES / "index.json")
    etat_chemin = C.FUSION / "etat.json"
    etat = C.lire_json(etat_chemin) if etat_chemin.is_file() else {"faits": [], "echantillon": echantillon(index)}
    faits = set(etat.get("faits") or [])
    if args.echantillon:
        etat["echantillon"] = echantillon(index)
    cibles = selection(args, index, faits)
    if not cibles:
        print("rien à fusionner")
        return
    C.FUSION.mkdir(parents=True, exist_ok=True)
    C.SIGNAUX.mkdir(parents=True, exist_ok=True)
    for ident in cibles:
        fiche = C.lire_json(C.FENETRES / f"{ident}.json")
        resultat = fusionner_une(fiche)
        C.ecrire_json(C.FUSION / f"{ident}.json", resultat)
        faits.add(ident)
        print(ident, "signaux", len(resultat["signaux"]), "normale+", bool(resultat["normal_ajoute"]))
    etat["faits"] = sorted(faits, key=lambda i: index["ids"].index(i) if i in index["ids"] else 9999)
    C.ecrire_json(etat_chemin, etat)
    signaux = []
    ajoutees = 0
    for ident in etat["faits"]:
        doc = C.lire_json(C.FUSION / f"{ident}.json")
        if doc.get("normal_ajoute"):
            ajoutees += 1
        for ligne in doc.get("signaux") or []:
            signaux.append({"id": ident, "texte": ligne})
    C.ecrire_json(C.SIGNAUX / "images_signalees.json", {"n": len(signaux), "lignes": signaux, "normales_ajoutees": ajoutees})
    print(f"faits {len(etat['faits'])} ; normales ajoutées {ajoutees} ; signalements {len(signaux)}")


if __name__ == "__main__":
    main()
