#!/usr/bin/env python3
"""Segmente les images du fichier avec segment.py (scikit-image).

Les graines sont des positions types. Un contour n'est gardé que si l'algorithme
en produit un, fermé, ni minuscule ni collé au cadre. Il est marqué approximatif.
"""
import argparse
import gc
import importlib.util
import json
import subprocess
import sys
from pathlib import Path

import numpy as np
from PIL import Image

sys.path.insert(0, str(Path(__file__).resolve().parent))
import commun as C

REF = "origin/cursor/interface-didactique-ffbc:imagerie_GROK/harnais/scripts/segment.py"
CACHE = Path("/tmp/fedmed-seg/segment.py")
PHRASE = "Contour approximatif (segmentation automatique, non relu)"


def module_segment():
    CACHE.parent.mkdir(parents=True, exist_ok=True)
    if not CACHE.is_file():
        brut = subprocess.check_output(["git", "show", REF], cwd=C.DEPOT)
        CACHE.write_bytes(brut)
    spec = importlib.util.spec_from_file_location("segment_harnais", CACHE)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def gris(path):
    im = Image.open(path).convert("L")
    im.thumbnail((480, 480))
    return np.asarray(im)


def famille(tech, region):
    t = f"{tech or ''} {region or ''}".lower()
    radio = any(k in t for k in ("radio", "cliché", "cliche", "rx "))
    coupe = any(k in t for k in ("tdm", "scanner", "tomodensit", "irm", "mri", "coupe axial"))
    echo = any(k in t for k in ("échog", "echog", "ultras", "écho", "echo "))
    if radio and any(k in t for k in ("thorax", "poumon", "plevr", "médiast", "mediast", "pneumo")):
        return "rx-thorax"
    if echo:
        return "us"
    if coupe and any(k in t for k in ("tête", "tete", "céréb", "cereb", "encéph", "enceph", "crân", "cran")):
        return "coupe-tete"
    if coupe and any(k in t for k in ("thorax", "poumon", "plevr")):
        return "coupe-thorax"
    if coupe and any(k in t for k in ("abdomen", "hépat", "hepat", "foie", "rein", "pelv", "bassin")):
        return "coupe-abdomen"
    if coupe:
        return "coupe"
    if radio:
        return "rx"
    return "generique"


PLANS = {
    "rx-thorax": [
        ("paroi", 1, "Paroi", "enveloppe", 0.10, 0.42),
        ("poumon-droit", 2, "Poumon droit", "air", 0.32, 0.40),
        ("poumon-gauche", 2, "Poumon gauche", "air", 0.68, 0.40),
        ("coeur", 3, "Cœur", "eau", 0.56, 0.56),
    ],
    "coupe-thorax": [
        ("paroi", 1, "Paroi", "enveloppe", 0.50, 0.16),
        ("poumon-droit", 2, "Poumon droit", "air", 0.34, 0.46),
        ("poumon-gauche", 2, "Poumon gauche", "air", 0.66, 0.46),
        ("mediastin", 3, "Médiastin", "foyer", 0.50, 0.50),
    ],
    "coupe-tete": [
        ("crane", 1, "Enveloppe crânienne", "os", 0.50, 0.16),
        ("parenchyme", 2, "Parenchyme", "foyer", 0.50, 0.48),
    ],
    "coupe-abdomen": [
        ("paroi", 1, "Paroi", "enveloppe", 0.50, 0.14),
        ("contenu", 2, "Contenu abdominal", "foyer", 0.42, 0.48),
    ],
    "coupe": [
        ("enveloppe", 1, "Enveloppe", "enveloppe", 0.50, 0.16),
        ("contenu", 2, "Contenu de la coupe", "foyer", 0.50, 0.48),
    ],
    "us": [
        ("champ", 1, "Champ échographique", "enveloppe", 0.50, 0.28),
        ("organe", 2, "Structure centrale", "foyer", 0.50, 0.52),
    ],
    "rx": [
        ("enveloppe", 1, "Enveloppe", "enveloppe", 0.50, 0.20),
        ("contenu", 2, "Structure centrale", "foyer", 0.50, 0.50),
    ],
    "generique": [
        ("enveloppe", 1, "Enveloppe", "enveloppe", 0.50, 0.22),
    ],
}


def acceptable(contour):
    if not contour or len(contour) < 13:
        return False
    xs = [p[0] for p in contour]
    ys = [p[1] for p in contour]
    aire = (max(xs) - min(xs)) * (max(ys) - min(ys))
    if aire < 0.012 or aire > 0.72:
        return False
    if max(xs) > 0.98 and min(xs) < 0.02 and max(ys) > 0.98 and min(ys) < 0.02:
        return False
    bord = sum(1 for x, y in contour if x < 0.025 or x > 0.975 or y < 0.025 or y > 0.975)
    if bord / len(contour) > 0.12:
        return False
    return True


def segmenter_plan(seg, im, plan):
    out = []
    for sid, ordre, nom, mode, x, y in plan:
        if mode == "base":
            continue
        try:
            contour, how, _ = seg.contour_from_seed(im, x, y, mode, n=28)
        except Exception:
            contour, how = None, "échec"
        if not acceptable(contour):
            continue
        out.append({
            "id": sid,
            "nom": nom,
            "ordre": ordre,
            "couleur": "",
            "contour": contour,
            "aspect": "Contour approximatif, non relu.",
            "aspect_source": PHRASE,
            "approximatif": True,
            "methode": how,
        })
    return out


def couleur(sid):
    from fusionner import couleur_structure
    return couleur_structure(sid)


def lesion_contours(seg, im, lesions):
    n = 0
    for lesion in lesions or []:
        tip = lesion.get("tip")
        if not tip:
            continue
        h, w = im.shape
        sx = min(max(int(round(float(tip[0]) * (w - 1))), 1), w - 2)
        sy = min(max(int(round(float(tip[1]) * (h - 1))), 1), h - 2)
        try:
            contour, how = seg.polygon(im, sx, sy, 28)
        except Exception:
            continue
        if not acceptable(contour):
            continue
        lesion["contour"] = contour
        lesion["approximatif"] = True
        lesion["contour_source"] = PHRASE
        n += 1
    return n


def chemin_image(fiche, fusion, cote):
    if cote in (fusion.get("retraits") or {}):
        return None
    if cote == "normal" and fusion.get("normal_ajoute"):
        return C.FENETRES / fusion["normal_ajoute"]["fichier"]
    bloc = ((fiche["enr"].get("images") or {}).get(cote) or {})
    fichier = bloc.get("fichier") if isinstance(bloc, dict) else ""
    if isinstance(fichier, str) and fichier.startswith("images/"):
        path = C.FENETRES / fichier
        return path if path.is_file() else None
    return None


def appliquer(seg, ident):
    fiche = C.lire_json(C.FENETRES / f"{ident}.json")
    dest = C.FUSION / f"{ident}.json"
    if not dest.is_file():
        return "sans fusion"
    fusion = C.lire_json(dest)
    if fusion.get("segmentation") and not appliquer.force:
        return "déjà"
    tech = ((fiche["enr"].get("images") or {}).get("patho") or {}).get("technique") or ""
    region = (fiche.get("contexte") or {}).get("region") or ""
    plan = PLANS[famille(tech, region)]
    g = fusion["gabarit"]
    comptes = {}
    for cote in ("normal", "patho"):
        path = chemin_image(fiche, fusion, cote)
        info = g.get(cote) or {}
        gardes = [s for s in (info.get("structures") or []) if s.get("contour") and not s.get("approximatif")]
        neufs = []
        if path:
            im = gris(path)
            neufs = segmenter_plan(seg, im, plan)
            for st in neufs:
                st["couleur"] = couleur(st["id"])
            if cote == "patho":
                comptes["lesions"] = lesion_contours(seg, im, info.get("lesions") or [])
        ids = {s["id"] for s in neufs}
        info["structures"] = neufs + [s for s in gardes if s.get("id") not in ids]
        info["structures"].sort(key=lambda s: (s.get("ordre") or 9, s.get("id") or ""))
        g[cote] = info
        comptes[cote] = len(neufs)
    fusion["gabarit"] = g
    fusion["segmentation"] = {"famille": famille(tech, region), **comptes}
    C.ecrire_json(dest, fusion)
    return f"{famille(tech, region)} N{comptes.get('normal',0)} P{comptes.get('patho',0)} L{comptes.get('lesions',0)}"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--limite", type=int, default=0)
    ap.add_argument("--ids", default="")
    ap.add_argument("--force", action="store_true")
    args = ap.parse_args()
    appliquer.force = args.force
    seg = module_segment()
    index = C.lire_json(C.FENETRES / "index.json")
    if args.ids:
        cibles = [i.strip() for i in args.ids.split(",") if i.strip()]
    else:
        cibles = []
        for ident in index["ids"]:
            doc = C.lire_json(C.FUSION / f"{ident}.json")
            if args.force or not doc.get("segmentation"):
                cibles.append(ident)
            if args.limite and len(cibles) >= args.limite:
                break
    for ident in cibles:
        try:
            print(ident, appliquer(seg, ident), flush=True)
        except Exception as exc:
            print(ident, "ERREUR", type(exc).__name__, flush=True)
        gc.collect()


if __name__ == "__main__":
    main()
