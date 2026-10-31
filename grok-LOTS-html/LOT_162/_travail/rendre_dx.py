#!/usr/bin/env python3
"""Rend un DX. Le corps long est une liste de fenêtres (id, titre, html)."""
from moteur import fen, btn
from dx_lib import ecrire, SOURCES

def P(*a):
    return "<p>" + "".join(a) + "</p>"

def S(*n):
    return "".join(f'<sup class="s">{i}</sup>' for i in n)

def rendre(numero, titre, essentiel, points, fenetres):
    """points: dict pid -> phrase courte qui contient des btn.
    fenetres: list of (pid, wid, titre_fen, html) attachées au point.
    """
    ilots = {}
    for i in range(1, 15):
        pid = f"p{i}"
        ilots[pid] = (points[pid], [])
    for pid, wid, titre_fen, html in fenetres:
        ile, fens = ilots[pid]
        fens.append(fen(wid, titre_fen, html))
        ilots[pid] = (ile, fens)
    return ecrire(numero, titre, titre, essentiel, ilots, SOURCES)
