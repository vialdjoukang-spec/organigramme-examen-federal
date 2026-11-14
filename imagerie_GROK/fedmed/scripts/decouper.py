#!/usr/bin/env python3
"""Extrait chaque fenêtre d'imagerie et laisse un squelette réversible."""
import hashlib
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import commun as C


def contexte_lignes(obj):
    reg = obj.get("reg") or {}
    letn = obj.get("letn") or {}
    out = {}
    for famille, rows in (obj.get("lignes") or {}).items():
        for row in rows:
            ident = row.get("id")
            if not ident:
                continue
            c = row.get("c") or {}
            out[ident] = {
                "id": ident,
                "famille": famille,
                "dx": C.plain(row.get("dxt") or c.get("dx") or ""),
                "region": C.plain(str(reg.get(row.get("r"), ""))),
                "systeme": C.plain(row.get("sh") or ""),
                "lettre": C.plain(str(letn.get(row.get("l"), ""))),
                "niveau": "Minimum indispensable" if row.get("n") == "M" else "Cible complète",
                "signe": C.plain(c.get("sg") or ""),
            }
    return out


def extraire_images(ident, enr):
    im = enr.get("images") or {}
    mime = {}
    sha = {}
    for cote in ("patho", "normal"):
        bloc = im.get(cote)
        if not isinstance(bloc, dict):
            continue
        fichier = bloc.get("fichier")
        if not isinstance(fichier, str) or not fichier.startswith("data:image"):
            continue
        type_mime, brut = C.scinder_data_uri(fichier)
        ext = "jpg" if type_mime == "image/jpeg" else type_mime.split("/")[-1]
        nom = f"{ident}_{cote}.{ext}"
        dest = C.IMAGES / nom
        dest.parent.mkdir(parents=True, exist_ok=True)
        if not dest.exists() or dest.read_bytes() != brut:
            dest.write_bytes(brut)
        bloc["fichier"] = f"images/{nom}"
        mime[cote] = type_mime
        sha[cote] = hashlib.sha256(brut).hexdigest()
    return mime, sha


def decouper():
    data = C.lire_original()
    m, page, d, obj = C.ouvrir_rts(data)
    ctx = contexte_lignes(obj)
    ids = []
    sans = []
    for ident, enr in obj["enr"].items():
        im = enr.get("images") or {}
        patho = im.get("patho") if isinstance(im.get("patho"), dict) else {}
        fichier = patho.get("fichier") if isinstance(patho, dict) else ""
        if not (isinstance(fichier, str) and fichier.startswith("data:image")):
            continue
        normal = im.get("normal") if isinstance(im.get("normal"), dict) else {}
        a_normal = isinstance(normal.get("fichier"), str) and normal.get("fichier", "").startswith("data:image")
        mime, sha = extraire_images(ident, enr)
        fiche = {
            "id": ident,
            "contexte": ctx.get(ident) or {"id": ident},
            "manque_normal": (not a_normal) or bool(im.get("manque_normal")),
            "mime": mime,
            "sha256": sha,
            "enr": enr,
        }
        C.ecrire_json(C.FENETRES / f"{ident}.json", fiche)
        obj["enr"][ident] = {"__fenetre__": ident}
        ids.append(ident)
        if not a_normal:
            sans.append(ident)
    squelette = C.refermer(data, m, page, d, obj)
    C.SQUELETTE.parent.mkdir(parents=True, exist_ok=True)
    C.SQUELETTE.write_text(squelette, encoding="utf-8")
    index = {
        "n": len(ids),
        "sans_normale": sans,
        "ids": ids,
        "sha256_original": C.SHA256_ATTENDU,
    }
    C.ecrire_json(C.FENETRES / "index.json", index)
    print(f"fenêtres {len(ids)} ; sans normale {len(sans)} ; squelette {len(squelette)} caractères")
    return index


def main():
    decouper()


if __name__ == "__main__":
    main()
