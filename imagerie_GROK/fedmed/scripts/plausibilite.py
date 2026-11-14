#!/usr/bin/env python3
"""Masque les contours invraisemblables. Un faux contour disparaît."""
import json
import sys
from pathlib import Path

import numpy as np
from PIL import Image

sys.path.insert(0, str(Path(__file__).resolve().parent))
import commun as C

ATTENDU = {
    "poumon-droit": {"cx": (0.10, 0.48), "cy": (0.20, 0.80), "aire": (0.08, 0.45), "ratio": (0.50, 2.5)},
    "poumon-gauche": {"cx": (0.52, 0.92), "cy": (0.20, 0.80), "aire": (0.08, 0.45), "ratio": (0.50, 2.5)},
    "coeur": {"cx": (0.30, 0.74), "cy": (0.30, 0.80), "aire": (0.045, 0.34), "ratio": (0.40, 2.3)},
    "paroi": {"aire": (0.12, 0.82), "ratio": (0.28, 3.6)},
    "mediastin": {"cx": (0.28, 0.72), "aire": (0.04, 0.40), "ratio": (0.35, 2.8)},
    "crane": {"aire": (0.10, 0.78), "ratio": (0.30, 3.2)},
    "parenchyme": {"cx": (0.22, 0.78), "cy": (0.22, 0.78), "aire": (0.06, 0.58)},
    "contenu": {"aire": (0.05, 0.62)},
    "enveloppe": {"aire": (0.10, 0.82)},
    "organe": {"aire": (0.05, 0.58)},
    "champ": {"aire": (0.08, 0.72)},
}
PAIRES = (("poumon-droit", "poumon-gauche"),)


def boite(contour):
    xs = [p[0] for p in contour]
    ys = [p[1] for p in contour]
    x0, x1, y0, y1 = min(xs), max(xs), min(ys), max(ys)
    w, h = max(x1 - x0, 1e-6), y1 - y0
    return {
        "aire": (x1 - x0) * h,
        "cx": (x0 + x1) / 2,
        "cy": (y0 + y1) / 2,
        "ratio": h / w,
    }


def individuel(st):
    contour = st.get("contour") or []
    if len(contour) < 8:
        return "contour trop court"
    b = boite(contour)
    if b["aire"] < 0.04:
        return "aire trop petite"
    if b["aire"] > 0.78:
        return "aire trop grande"
    if b["ratio"] > 3.6 or b["ratio"] < 0.22:
        return "rapport hauteur/largeur invraisemblable"
    att = ATTENDU.get(st.get("id") or "")
    if not att:
        return ""
    if "cx" in att and not (att["cx"][0] <= b["cx"] <= att["cx"][1]):
        return "position horizontale inattendue"
    if "cy" in att and not (att["cy"][0] <= b["cy"] <= att["cy"][1]):
        return "position verticale inattendue"
    if "aire" in att and not (att["aire"][0] <= b["aire"] <= att["aire"][1]):
        return "aire hors de la plage attendue"
    if "ratio" in att and not (att["ratio"][0] <= b["ratio"] <= att["ratio"][1]):
        return "rapport hauteur/largeur hors de la plage attendue"
    return ""


def symetrie(gauche, droite):
    if not gauche or not droite:
        return ""
    a, b = boite(gauche["contour"]), boite(droite["contour"])
    petit, grand = min(a["aire"], b["aire"]), max(a["aire"], b["aire"])
    if petit <= 0 or grand / petit > 2.8:
        return "aires gauche et droite trop différentes"
    if abs(a["cy"] - b["cy"]) > 0.18:
        return "centres verticaux trop éloignés"
    if not (a["cx"] < 0.5 < b["cx"] or b["cx"] < 0.5 < a["cx"]):
        return "les contours pairs ne sont pas de part et d'autre de la ligne médiane"
    rp, rg = min(a["ratio"], b["ratio"]), max(a["ratio"], b["ratio"])
    if rp <= 0 or rg / rp > 2.2:
        return "formes gauche et droite trop différentes"
    return ""


def coherence(a, b):
    if not a or not b:
        return ""
    ba, bb = boite(a["contour"]), boite(b["contour"])
    petit, grand = min(ba["aire"], bb["aire"]), max(ba["aire"], bb["aire"])
    if petit <= 0 or grand / petit > 3.0:
        return "aire incohérente avec l'autre côté, à échelle près"
    rp, rg = min(ba["ratio"], bb["ratio"]), max(ba["ratio"], bb["ratio"])
    if rp <= 0 or rg / rp > 2.2:
        return "forme incohérente avec l'autre côté"
    if abs(ba["cx"] - bb["cx"]) > 0.22 or abs(ba["cy"] - bb["cy"]) > 0.22:
        return "position incohérente avec l'autre côté"
    return ""


def outlier(a, b):
    ba, bb = boite(a["contour"]), boite(b["contour"])
    if ba["aire"] < bb["aire"] * 0.5:
        return "normal"
    if bb["aire"] < ba["aire"] * 0.5:
        return "patho"
    return "les deux"


def nettoyer_aspect(st):
    st["aspect"] = ""
    st["aspect_source"] = ""
    st["approximatif"] = True
    st["mention"] = "contour automatique approximatif"


def filtrer(fusion):
    g = fusion["gabarit"]
    masques = []
    gardes = {"normal": {}, "patho": {}}
    for cote in ("normal", "patho"):
        info = g.get(cote) or {}
        retenus = []
        for st in info.get("structures") or []:
            if not st.get("contour"):
                continue
            raison = individuel(st)
            if raison:
                masques.append(f"Contour masqué : {st.get('nom') or st.get('id')} ({cote}) — {raison}.")
                continue
            nettoyer_aspect(st)
            retenus.append(st)
        gardes[cote] = {st["id"]: st for st in retenus if st.get("id")}
        info["structures"] = retenus
        g[cote] = info
    for cote in ("normal", "patho"):
        info = g[cote]
        raison = symetrie(gardes[cote].get("poumon-droit"), gardes[cote].get("poumon-gauche"))
        if not raison:
            continue
        for sid in ("poumon-droit", "poumon-gauche"):
            st = gardes[cote].pop(sid, None)
            if not st:
                continue
            info["structures"] = [s for s in info["structures"] if s.get("id") != sid]
            masques.append(f"Contour masqué : {st.get('nom')} ({cote}) — {raison}.")
    ids = set(gardes["normal"]) | set(gardes["patho"])
    for sid in ids:
        a, b = gardes["normal"].get(sid), gardes["patho"].get(sid)
        raison = coherence(a, b)
        if not raison:
            continue
        qui = outlier(a, b) if a and b else "les deux"
        cotes = ("normal", "patho") if qui == "les deux" else (qui,)
        for cote in cotes:
            st = gardes[cote].pop(sid, None)
            if not st:
                continue
            g[cote]["structures"] = [s for s in g[cote]["structures"] if s.get("id") != sid]
            masques.append(f"Contour masqué : {st.get('nom')} ({cote}) — {raison}.")
    fusion["gabarit"] = g
    anciens = [s for s in fusion.get("signaux") or [] if not s.startswith("Contour masqué")]
    fusion["signaux"] = anciens + masques
    fusion["contours"] = {
        "conserves": sum(len(g[c].get("structures") or []) for c in ("normal", "patho")),
        "masques": len(masques),
    }
    return fusion


def montage_coupe(path):
    """Si deux vues sont séparées par une bande noire, garde la vue de gauche."""
    im = Image.open(path).convert("RGB")
    arr = np.asarray(im)
    h, w, _ = arr.shape
    if w < h * 1.25:
        return None
    noir = arr.mean(axis=2) < 18
    colonne = noir.mean(axis=0)
    milieu = colonne[int(w * 0.35) : int(w * 0.75)]
    if milieu.size == 0 or milieu.max() < 0.45:
        return None
    i = int(np.argmax(milieu)) + int(w * 0.35)
    gauche = im.crop((0, 0, max(i - 4, 1), h))
    if gauche.size[0] < 40:
        return None
    return gauche


def retirer_normale(d, motif):
    d.pop("normal_ajoute", None)
    g = d["gabarit"].setdefault("normal", {})
    for cle in ("age", "sexe", "age_preuve"):
        g.pop(cle, None)
    g["source"] = {"auteur": "", "licence": "", "url": "", "credit": ""}
    g["structures"] = []
    g["refus"] = motif
    d["signaux"] = [s for s in d.get("signaux") or [] if "Normale" not in s]
    d["signaux"].append("Normale retirée : " + motif + ".")
    d["recherche_normale"] = {"ajoutee": False, "refus": [motif]}


def revoir_normales():
    decisions = {
        "IMG-157": "recadrer",
        "IMG-257": "garder",
        "IMG-159": "retirer",
        "IMG-209": "retirer",
        "IMG-216": "retirer",
        "IMG-219": "retirer",
        "IMG-220": "retirer",
        "IMG-221": "retirer",
    }
    for ident, action in decisions.items():
        fusion = C.lire_json(C.FUSION / f"{ident}.json")
        image = C.FENETRES / "images" / f"{ident}_normal.jpg"
        if action == "garder":
            continue
        if action == "recadrer" and image.is_file():
            vue = montage_coupe(image)
            if vue is None:
                retirer_normale(fusion, "montage sans vue unique au bon niveau")
            else:
                vue.save(image, "JPEG", quality=85)
                fusion.setdefault("signaux", []).append(
                    "Normale recadrée : une seule vue axiale, au niveau de l'aorte thoracique."
                )
            C.ecrire_json(C.FUSION / f"{ident}.json", fusion)
            if action != "recadrer" or not image.is_file() or fusion.get("normal_ajoute") is None and action == "retirer":
                pass
            continue
        if image.is_file():
            image.unlink()
        retirer_normale(fusion, "montage ou niveau de coupe différent de la pathologique")
        C.ecrire_json(C.FUSION / f"{ident}.json", fusion)
        print(ident, action)


def main():
    revoir_normales()
    total_c = total_m = 0
    for path in sorted(C.FUSION.glob("*.json")):
        if path.name == "etat.json":
            continue
        doc = filtrer(C.lire_json(path))
        C.ecrire_json(path, doc)
        total_c += doc["contours"]["conserves"]
        total_m += doc["contours"]["masques"]
    print(f"conservés {total_c} ; masqués {total_m}")


if __name__ == "__main__":
    main()
