#!/usr/bin/env python3
"""DX.3 à DX.10. Argument : le numéro, ou « tous »."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from base_dx import P, W, construire, A

def fen(point, ident, titre, paragraphes, *refs):
    corps = "\n".join(P(p, *refs) for p in paragraphes)
    return point, W("w-" + ident, titre, corps)

def page_de(num, h1, essentiel, fiches, fenetres, sources):
    sous = (
        f"Diagnostic différentiel DX.{num} de {A('situation de départ F2.11 de PROFILES','F2.11')} "
        f"« Enzymes hépatiques anormales ». Nom de la liste canonique. Texte du 31.10.2026."
    )
    par = {}
    for point, html in fenetres:
        par.setdefault(point, []).append(html)
    return construire(num, h1, essentiel, sous, fiches, par, sources)

# Le corps de chaque DX est une liste (point, id, titre, [paragraphes], refs).
# Il est complété jusqu'à la bande 35–46 Ko par des développements propres au diagnostic.
def bande(num, h1, essentiel, fiches, coeur, sources):
    # coeur : list of (point, id, titre, paragraphs, refs)
    fens = [fen(a, b, c, d, *e) for a, b, c, d, e in coeur]
    path = page_de(num, h1, essentiel, fiches, fens, sources)
    return path
