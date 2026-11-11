#!/usr/bin/env python3
"""Contrôles déterministes V7 (§2, §10, §11, §16) — zéro jeton. Usage : controle_v7.py fichier.html LOT_X_PARTIE"""
import re, sys
from html.parser import HTMLParser

def main(path, etiquette):
    raw = open(path, 'rb').read(); txt = raw.decode('utf-8')
    err = []
    taille = len(raw)
    if not 90_000 <= taille <= 200_000: err.append(f"taille {taille} o hors 90–200 Ko (découper en _a/_b si > 200 Ko)")
    if not txt.lstrip().lower().startswith('<!doctype html>'): err.append("DOCTYPE absent")
    fin = f"<!-- FIN_FICHIER {etiquette} -->"
    if not txt.rstrip().endswith(fin): err.append(f"balise finale attendue : {fin}")
    if '</html>' not in txt.lower(): err.append("</html> absent")
    if re.search(r'\stitle\s*=', txt, re.I): err.append("attribut title= interdit")
    for motif, nom in [(r'<script\b', 'script'), (r'<img\b', 'image'), (r'<link\b[^>]*stylesheet', 'feuille externe')]:
        if re.search(motif, txt, re.I): err.append(f"{nom} interdit")
    longues = [i + 1 for i, l in enumerate(txt.splitlines()) if len(l) > 3000]
    if longues: err.append(f"lignes > 3000 car. : {longues[:10]}")
    for m in re.finditer(r'<table\b', txt, re.I):
        avant = txt[max(0, m.start() - 300):m.start()]
        if 'overflow-x:auto' not in avant.replace(' ', ''): err.append(f"tableau non enveloppé vers l'octet {m.start()}"); break
    class P(HTMLParser):
        vides = {'br','hr','meta','link','img','input','col','wbr','source','area','base','embed','param','track'}
        def __init__(s): super().__init__(); s.pile = []; s.err = []
        def handle_starttag(s, t, a):
            if t not in s.vides: s.pile.append(t)
        def handle_endtag(s, t):
            if t in s.vides: return
            if s.pile and s.pile[-1] == t: s.pile.pop()
            else: s.err.append(f"fermeture </{t}> inattendue ligne {s.getpos()[0]}")
    p = P(); p.feed(txt)
    if p.err: err.append(p.err[0])
    if p.pile: err.append(f"balises non fermées : {p.pile[-5:]}")
    if not re.search(r'Sources', txt): err.append("section Sources absente")
    if 'non validé cliniquement par un médecin' not in txt: err.append("mention de non-validation absente")
    print(f"{path} · {taille} o · " + ("OK" if not err else "ÉCHEC"))
    for e in err: print("  -", e)
    return 0 if not err else 1

if __name__ == '__main__':
    sys.exit(main(sys.argv[1], sys.argv[2]))
