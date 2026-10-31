#!/usr/bin/env python3
"""Dix monographies DX de LOT_155. Les faits viennent des preuves du 31.10.2026."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from construire import GLOSSAIRE, SOURCES, exp, meta_base, point
from moteur import ecrire

def Q(e, c, p, k):
    return (e, c, p, k)

def S(lignes):
    out = []
    for ligne in lignes:
        bas = ligne[0].lower() + ligne[1:]
        out.append(Q(
            ligne,
            f"la conduite retenue part de là : {bas}",
            f"le piège serait d'oublier ceci : {bas}",
            f"le contrôle suivant porte sur ceci : {bas}",
        ))
    return out

def lecon(n, nom, fiches, items, sous=None):
    points = []
    for i in range(1, 15):
        points.append(point(i, fiches[i - 1], items[i - 1], sous if i == 6 else None))
    meta = meta_base(
        h1=nom,
        h2=f"DX.{n} — {nom}",
        sous=f"DX.{n} du cours des électrolytes anormaux. Le rang d'exclusion n'est pas le numéro. Texte du 31 octobre 2026.",
        essentiel=[
            "Le cours des électrolytes anormaux pose le cadre et l'ordre E.",
            "Les doses chiffrées en milligrammes, grammes ou microgrammes viennent de l'information professionnelle nommée.",
            "Les sigles s'ouvrent dans [[w-glossaire|la fenêtre des sigles]].",
        ],
        points=points,
        fichier=f"LOT_155_Phase_B_V0_DX.{n}.html",
        fin=f"FIN_FICHIER LOT_155_Phase_B_V0_DX.{n}",
    )
    return ecrire(meta)

# Chaque entrée de ITEMS[dx] est une liste de 14 listes de tuples.
# On construit DX.1 d'abord de façon complète, puis les autres sur le même moule.
