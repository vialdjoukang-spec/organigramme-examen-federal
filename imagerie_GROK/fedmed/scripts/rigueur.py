#!/usr/bin/env python3
"""Normales adultes attestées, contours coupés à l'enveloppe du corps, texte nettoyé."""
import io
import re
import sys
import urllib.request
from pathlib import Path

import numpy as np
from PIL import Image
from scipy import ndimage
from skimage.draw import polygon as poly_draw
from skimage.measure import find_contours
from skimage.morphology import binary_dilation, disk

sys.path.insert(0, str(Path(__file__).resolve().parent))
import commun as C

RX_URL = "https://upload.wikimedia.org/wikipedia/commons/a/a1/Normal_posteroanterior_%28PA%29_chest_radiograph_%28X-ray%29.jpg"
RX_PAGE = "https://commons.wikimedia.org/wiki/File:Normal_posteroanterior_(PA)_chest_radiograph_(X-ray).jpg"
RX_NOM = "NORM-RX-THORAX-FACE.jpg"
RX_CREDIT = (
    "Mikael Häggström. Radiographie thoracique de face (postéro-antérieure) normale, "
    "sans lésion, chez une femme de 21 ans. CC0."
)
NEST = re.compile(r"\(([^()]*)\(([^()]*)\)([^()]*)\)")
AGE_N = re.compile(r"(\d{1,3})")


def age_nombre(texte):
    m = AGE_N.search(texte or "")
    return int(m.group(1)) if m else None


def radio_thorax_face(technique):
    t = (technique or "").lower()
    if any(k in t for k in ("tdm", "scanner", "irm", "échog", "echog", "ultrasound", "tep", "scintig")):
        return False
    if not any(k in t for k in ("radio", "cliché", "cliche", "radiograph")):
        return False
    if not any(k in t for k in ("thorax", "thorac", "poumon")):
        return False
    if "profil" in t and "face" not in t:
        return False
    return "face" in t or "postéro" in t or "postero" in t


def a_une_normale(fusion, fiche):
    g = (fusion.get("gabarit") or {}).get("normal") or {}
    if g.get("refus"):
        return False
    if fusion.get("normal_ajoute"):
        return True
    bloc = (fiche["enr"].get("images") or {}).get("normal")
    fichier = bloc.get("fichier") if isinstance(bloc, dict) else ""
    return isinstance(fichier, str) and fichier.startswith("images/")


def textes_normale(fusion, fiche):
    g = (fusion.get("gabarit") or {}).get("normal") or {}
    bloc = (fiche["enr"].get("images") or {}).get("normal")
    bloc = bloc if isinstance(bloc, dict) else {}
    ajout = fusion.get("normal_ajoute") or {}
    return " ".join([
        bloc.get("credit") or "",
        bloc.get("technique") or "",
        (g.get("source") or {}).get("credit") or "",
        (g.get("source") or {}).get("auteur") or "",
        ajout.get("credit") or "",
        ajout.get("technique") or "",
    ])


def adulte_atteste(fusion, fiche):
    g = (fusion.get("gabarit") or {}).get("normal") or {}
    n = age_nombre(g.get("age") or "")
    if n is None or n < 18 or n > 110:
        return False
    preuve = g.get("age_preuve") or ""
    if not preuve:
        return False
    if str(n) not in textes_normale(fusion, fiche) and str(n) not in (g.get("age") or ""):
        return False
    return True


def retirer(fusion, motif):
    fusion.setdefault("retraits", {})["normal"] = motif
    fusion["normal_ajoute"] = None
    g = fusion["gabarit"].setdefault("normal", {})
    g["refus"] = motif
    g["structures"] = []
    g["age"] = ""
    g["sexe"] = ""
    g.pop("age_preuve", None)
    fusion["signaux"] = [s for s in fusion.get("signaux") or [] if not s.startswith("Normale")]
    fusion["signaux"].append("Normale retirée : " + motif + ".")


def preparer_radio():
    dest = C.IMAGES / RX_NOM
    req = urllib.request.Request(RX_URL, headers={"User-Agent": "FedMedBot/1.0 (atlas pedagogique) python-urllib"})
    blob = urllib.request.urlopen(req, timeout=40).read()
    if C.donnees_patient(blob[:80000]):
        raise SystemExit("la radiographie de remplacement contient des métadonnées patient")
    im = Image.open(io.BytesIO(blob)).convert("RGB")
    im.thumbnail((1200, 1200))
    im.save(dest, "JPEG", quality=85)
    return dest


def remplacer_radio(fusion):
    fusion.get("retraits", {}).pop("normal", None)
    if not fusion.get("retraits"):
        fusion.pop("retraits", None)
    fusion["normal_ajoute"] = {
        "fichier": f"images/{RX_NOM}",
        "mime": "image/jpeg",
        "technique": "Radiographie du thorax de face, postéro-antérieure",
        "credit": "Mikael Häggström",
        "licence": "CC0",
        "url": RX_PAGE,
    }
    g = fusion["gabarit"].setdefault("normal", {})
    g["refus"] = ""
    g["structures"] = []
    g["age"] = "21 ans"
    g["sexe"] = "femme"
    g["age_preuve"] = "légende Commons"
    g["source"] = {
        "auteur": "Mikael Häggström",
        "licence": "CC0",
        "url": RX_PAGE,
        "credit": RX_CREDIT,
    }
    fusion["signaux"] = [s for s in fusion.get("signaux") or [] if not s.startswith("Normale")]
    fusion["signaux"].append(
        "Normale remplacée : radiographie thoracique de face, femme de 21 ans, CC0, Mikael Häggström."
    )


def chemin_image(ident, cote, fusion, fiche):
    if cote == "normal" and fusion.get("normal_ajoute") and not (fusion["gabarit"].get("normal") or {}).get("refus"):
        return C.FENETRES / fusion["normal_ajoute"]["fichier"]
    if cote == "normal" and (fusion.get("retraits") or {}).get("normal"):
        return None
    if cote == "normal" and (fusion["gabarit"].get("normal") or {}).get("refus"):
        return None
    bloc = (fiche["enr"].get("images") or {}).get(cote)
    fichier = bloc.get("fichier") if isinstance(bloc, dict) else ""
    if isinstance(fichier, str) and fichier.startswith("images/"):
        p = C.FENETRES / fichier
        return p if p.is_file() else None
    return None


def masque_corps(im):
    gris = im.convert("L")
    gris.thumbnail((240, 240))
    g = np.asarray(gris)
    fond = (g < 24) | (g > 244)
    labels, n = ndimage.label(fond)
    if n == 0:
        return None
    bord = np.unique(np.concatenate([labels[0], labels[-1], labels[:, 0], labels[:, -1]]))
    fond_bord = np.isin(labels, bord[bord > 0])
    corps = ~fond_bord
    if corps.mean() < 0.08 or corps.mean() > 0.98:
        return None
    return binary_dilation(corps, disk(2))


def hors_corps(contour, corps):
    h, w = corps.shape
    xs = np.clip(np.array([p[0] for p in contour], float), -0.05, 1.05) * (w - 1)
    ys = np.clip(np.array([p[1] for p in contour], float), -0.05, 1.05) * (h - 1)
    if np.any(np.array([p[0] for p in contour]) < -0.01) or np.any(np.array([p[0] for p in contour]) > 1.01):
        return 1.0, None
    if np.any(np.array([p[1] for p in contour]) < -0.01) or np.any(np.array([p[1] for p in contour]) > 1.01):
        return 1.0, None
    rr, cc = poly_draw(ys, xs, shape=corps.shape)
    if len(rr) < 8:
        return 1.0, None
    return float((~corps[rr, cc]).mean()), (rr, cc)


def rogner(contour, corps):
    frac, _ = hors_corps(contour, corps)
    if frac >= 0.12:
        return None, "masqué"
    if frac < 0.02:
        return contour, ""
    h, w = corps.shape
    xs = np.clip(np.array([p[0] for p in contour], float), 0, 1) * (w - 1)
    ys = np.clip(np.array([p[1] for p in contour], float), 0, 1) * (h - 1)
    rr, cc = poly_draw(ys, xs, shape=corps.shape)
    zone = np.zeros(corps.shape, bool)
    zone[rr, cc] = True
    inter = zone & corps
    if inter.sum() < 20:
        return None, "masqué"
    traces = find_contours(inter.astype(float), 0.5)
    if not traces:
        return None, "masqué"
    trace = max(traces, key=len)
    idx = np.linspace(0, len(trace) - 1, min(28, len(trace))).astype(int)
    pts = [[round(float(trace[i, 1] / (w - 1)), 4), round(float(trace[i, 0] / (h - 1)), 4)] for i in idx]
    return pts, "rogne"


def appliquer_enveloppe(fusion, fiche):
    masques = []
    rognes = 0
    for cote in ("normal", "patho"):
        path = chemin_image(fusion["id"] if "id" in fusion else fiche["id"], cote, fusion, fiche)
        info = (fusion.get("gabarit") or {}).get(cote) or {}
        contours = []
        for st in info.get("structures") or []:
            if st.get("contour"):
                contours.append(("structure", st.get("nom") or st.get("id"), st))
        for i, le in enumerate(info.get("lesions") or []):
            if le.get("contour"):
                contours.append(("lésion", le.get("label") or str(i + 1), le))
        if not contours or path is None or not path.is_file():
            continue
        try:
            corps = masque_corps(Image.open(path))
        except Exception:
            corps = None
        if corps is None:
            continue
        garder_s = []
        for st in info.get("structures") or []:
            if not st.get("contour"):
                garder_s.append(st)
                continue
            neuf, etat = rogner(st["contour"], corps)
            if etat == "masqué" or neuf is None:
                masques.append(f"{st.get('nom') or st.get('id')} ({cote})")
                continue
            if etat == "rogne":
                st["contour"] = neuf
                rognes += 1
            garder_s.append(st)
        info["structures"] = garder_s
        garder_l = []
        for le in info.get("lesions") or []:
            if not le.get("contour"):
                garder_l.append(le)
                continue
            neuf, etat = rogner(le["contour"], corps)
            if etat == "masqué" or neuf is None:
                masques.append(f"{le.get('label') or 'lésion'} ({cote})")
                continue
            if etat == "rogne":
                le["contour"] = neuf
                rognes += 1
            garder_l.append(le)
        info["lesions"] = garder_l
        fusion["gabarit"][cote] = info
    if masques:
        fusion.setdefault("signaux", []).append(
            "Contours masqués, hors de l'enveloppe du corps : " + " ; ".join(masques) + "."
        )
    return masques, rognes


def aplatir(texte):
    if not isinstance(texte, str) or "(" not in texte:
        return texte, False
    origine = texte
    for _ in range(8):
        neuf = NEST.sub(lambda m: "(" + m.group(1) + m.group(2) + m.group(3) + ")", texte)
        if neuf == texte:
            break
        texte = neuf
    texte = re.sub(r"\s+", " ", texte).strip()
    return texte, texte != origine


def dedoublonner(texte):
    if not isinstance(texte, str):
        return texte, False
    origine = texte
    texte = re.sub(
        r"(?i)(contour approximatif(?:[^()]{0,60})?)\s*\(\1\)",
        r"\1",
        texte,
    )
    morceaux = re.split(r"(?<=[.!?])\s+", texte)
    vus = []
    for morceau in morceaux:
        if vus and vus[-1].strip().lower() == morceau.strip().lower():
            continue
        vus.append(morceau)
    texte = " ".join(vus)
    return texte, texte != origine


def nettoyer_texte(fusion):
    change = False

    def touche(valeur):
        nonlocal change
        if not isinstance(valeur, str):
            return valeur
        a, c1 = aplatir(valeur)
        b, c2 = dedoublonner(a)
        change = change or c1 or c2
        return b

    g = fusion.get("gabarit") or {}
    for carte in g.get("cartes") or []:
        carte["titre"] = touche(carte.get("titre") or "")
        carte["texte"] = touche(carte.get("texte") or "")
    fusion["signaux"] = [touche(s) for s in fusion.get("signaux") or []]
    for cote in ("normal", "patho"):
        info = g.get(cote) or {}
        for st in info.get("structures") or []:
            st["aspect"] = re.sub(r"(?i)\(?\s*contour approximatif[\s\S]*", "", st.get("aspect") or "").strip()
            st["nom"] = touche(st.get("nom") or "")
        for le in info.get("lesions") or []:
            le["label"] = touche(le.get("label") or "")
            le["semio"] = touche(le.get("semio") or "")
        src = info.get("source") or {}
        if src:
            src["credit"] = touche(src.get("credit") or "")
            info["source"] = src
        g[cote] = info
    fusion["gabarit"] = g
    return change


def main():
    preparer_radio()
    index = C.lire_json(C.FENETRES / "index.json")
    remplaces, retires = [], []
    for ident in index["ids"]:
        fusion = C.lire_json(C.FUSION / f"{ident}.json")
        fiche = C.lire_json(C.FENETRES / f"{ident}.json")
        fusion["id"] = ident
        if not a_une_normale(fusion, fiche):
            continue
        if adulte_atteste(fusion, fiche):
            continue
        tech = ((fiche["enr"].get("images") or {}).get("patho") or {}).get("technique") or ""
        g = fusion["gabarit"].get("normal") or {}
        if radio_thorax_face(tech):
            remplacer_radio(fusion)
            remplaces.append(ident + " — " + (g.get("age") or "âge absent"))
        else:
            n = age_nombre(g.get("age") or "")
            motif = f"non adulte ({n} ans)" if n is not None and n < 18 else "âge adulte non attesté"
            retirer(fusion, motif)
            retires.append(ident + " — " + motif)
        C.ecrire_json(C.FUSION / f"{ident}.json", fusion)

    masques_n = rognes_n = 0
    fenetres_contour = []
    textes = []
    for ident in index["ids"]:
        fusion = C.lire_json(C.FUSION / f"{ident}.json")
        fiche = C.lire_json(C.FENETRES / f"{ident}.json")
        fusion["id"] = ident
        masques, rognes = appliquer_enveloppe(fusion, fiche)
        if nettoyer_texte(fusion) or masques or rognes:
            C.ecrire_json(C.FUSION / f"{ident}.json", fusion)
        if masques or rognes:
            fenetres_contour.append(f"{ident} : {len(masques)} masqués, {rognes} rognés")
            masques_n += len(masques)
            rognes_n += rognes
        if ident in ("IMG-134", "IMG-157"):
            textes.append(ident)

    rapport = {
        "remplaces": remplaces,
        "retires": retires,
        "contours": fenetres_contour,
        "masques": masques_n,
        "rognes": rognes_n,
    }
    C.ecrire_json(C.RACINE / "signaux" / "rigueur.json", rapport)
    print("remplacées", len(remplaces))
    print("retirées", len(retires))
    print("contours masqués", masques_n, "rognés", rognes_n)
    print("IMG-134", "remplacée" if any(x.startswith("IMG-134") for x in remplaces) else "autre")
    print("IMG-157 contours", next((x for x in fenetres_contour if x.startswith("IMG-157")), "aucun"))


if __name__ == "__main__":
    main()
