#!/usr/bin/env python3
"""Taille d'une leçon selon la règle de Vial : T = x Ko (+ y Ko), zéro jeton.

x = texte visible de la fiche (lue d'un trait) ; y = texte visible de toutes les fenêtres (popover) et de tous les dépliants (<details>).
Usage : python3 harnais/taille_xy.py <fichier.html> [--inscrire]
--inscrire remplace le contenu de l'élément id="taille" par « Taille : T = x Ko (+ y Ko) · lecture de la fiche ≈ n min ».
"""
import re, sys
from html.parser import HTMLParser


class Mesure(HTMLParser):
    def __init__(s):
        super().__init__(convert_charrefs=True)
        s.pile = []; s.dans = 0; s.cache = 0; s.x = [0, 0]; s.y = [0, 0]; s.fen = 0; s.dep = 0

    def handle_starttag(s, t, a):
        a = dict(a); pop = "popover" in a; det = t == "details"; cach = t in ("style", "script", "title", "head") or a.get("id") == "taille"
        s.pile.append((t, pop or det, cach))
        if pop or det: s.dans += 1
        if pop: s.fen += 1
        if det: s.dep += 1
        if cach: s.cache += 1

    def handle_endtag(s, t):
        while s.pile:
            tt, d, c = s.pile.pop()
            if d: s.dans -= 1
            if c: s.cache -= 1
            if tt == t: break

    def handle_data(s, d):
        if s.cache: return
        cible = s.y if s.dans else s.x
        cible[0] += len(d.split()); cible[1] += len(d.encode())


def mesurer(h):
    m = Mesure(); m.feed(h); return m


def main(a):
    f = a[0]; h = open(f, encoding="utf-8").read(); m = mesurer(h)
    lib = f"Taille : T = {m.x[1]/1000:.1f} Ko (+ {m.y[1]/1000:.1f} Ko) · lecture de la fiche ≈ {round(m.x[0]/180)} min · {m.fen} fenêtres, {m.dep} dépliants"
    print(f"{f} : {lib} · fichier {len(h.encode())} octets")
    if "--inscrire" in a:
        h2, n = re.subn(r'(<[^>]*id="taille"[^>]*>).*?(</[a-z]+>)', lambda g: g.group(1) + lib + g.group(2), h, count=1, flags=re.S)
        if n: open(f, "w", encoding="utf-8").write(h2)
        else: print("élément id=\"taille\" absent")


if __name__ == "__main__":
    main(sys.argv[1:])
