#!/usr/bin/env python3
"""Miroir LOTS_html/ : uniquement les HTML de leçons, un sous-dossier par LOT (zéro jeton).

Source : LOT_Claude_Finaux/LOT_XXX/ (déposé) ; à défaut, lot en cours de production/LOT_XXX/ (version de travail).
Lancé à chaque commit. Supprime du miroir les HTML disparus de la source.
"""
import re, shutil
from pathlib import Path

R = Path(__file__).resolve().parent.parent
DST = R / "LOTS_html"
MOTIF = re.compile(r"^LOT_\d{3}_Phase_[AB].*\.html$")


def sources():
    lots = {}
    for base in (R / "lot en cours de production", R / "LOT_Claude_Finaux"):  # le déposé l'emporte
        for d in sorted(base.glob("LOT_[0-9][0-9][0-9]")):
            fichiers = [f for f in d.rglob("*.html") if MOTIF.match(f.name)]
            if fichiers:
                lots[d.name] = fichiers
    return lots


def main():
    n = 0
    lots = sources()
    for lot, fichiers in lots.items():
        cible = DST / lot
        cible.mkdir(parents=True, exist_ok=True)
        noms = set()
        for f in fichiers:
            noms.add(f.name)
            g = cible / f.name
            if not g.exists() or g.read_bytes() != f.read_bytes():
                shutil.copy2(f, g); n += 1
        for g in cible.glob("*.html"):
            if g.name not in noms:
                g.unlink(); n += 1
    print(f"LOTS_html : {len(lots)} LOTS, {sum(len(v) for v in lots.values())} HTML, {n} mise(s) à jour")


if __name__ == "__main__":
    main()
