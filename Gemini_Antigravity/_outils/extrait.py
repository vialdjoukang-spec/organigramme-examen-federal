#!/usr/bin/env python3
"""EXTRAIT — lire un cours par morceaux (zéro modèle) au lieu de le lire en entier (Le_Gaspillon G3/G5 :
la lecture intégrale des HTML de 80–150 Ko pèse à chaque tour suivant ; c'est la première fuite mesurée).

  plan <cours.html>                    → table : points (id, titre, Ko) et fenêtres (id, titre, Ko)
  point <cours.html> N[,N…] [--texte]  → HTML (ou texte) des points demandés, fenêtres de ces points comprises
  fenetre <cours.html> <id>            → une fenêtre seule
  cherche <cours.html> <motif>         → lignes de texte contenant le motif (≤ 20), avec le point d'appartenance
Repère : points <h3 id="…-pN">, fenêtres <section class="fenetre" id="f-…-pN-…">.
"""
import re, sys, html

def lire(f): return open(f, encoding='utf-8').read()
def texte(h): return re.sub(r'\s+', ' ', html.unescape(re.sub(r'<[^>]+>', ' ', re.sub(r'<(script|style)\b.*?</\1>', ' ', h, flags=re.S)))).strip()

def points(h):
    m = list(re.finditer(r'<h3 id="([a-z0-9]+-p(\d+))"[^>]*>(.*?)</h3>', h, re.S))
    fin = [x.start() for x in m[1:]] + [len(h)]
    return [(int(x.group(2)), x.group(1), texte(x.group(3)), h[x.start():e]) for x, e in zip(m, fin)]

def fenetres(h):
    return [(x.group(1), x.group(2), x.group(0)) for x in re.finditer(
        r'<section class="fenetre" id="([^"]+)"[^>]*?aria-label="([^"]*)".*?</section>', h, re.S)]

if __name__ == '__main__':
    if len(sys.argv) < 3: print(__doc__); sys.exit(0)
    a, f = sys.argv[1], sys.argv[2]; h = lire(f); F = fenetres(h)
    if a == 'plan':
        print(f'{len(h.encode())//1000} Ko · {len(F)} fenêtres')
        for n, i, t, b in points(h):
            fw = [x for x in F if re.search(rf'-p{n}-', x[0])]
            print(f'p{n:<2} {len(b.encode())//1000:>3} Ko  {t[:70]}  [{len(fw)} fen., {sum(len(x[2].encode()) for x in fw)//1000} Ko]')
    elif a == 'point':
        voulus = {int(x) for x in sys.argv[3].split(',')}
        for n, i, t, b in points(h):
            if n in voulus:
                fw = ''.join(x[2] for x in F if re.search(rf'-p{n}-', x[0]) and x[2] not in b)
                print(texte(b + fw) if '--texte' in sys.argv else b + fw)
    elif a == 'fenetre':
        print(next((x[2] for x in F if x[0] == sys.argv[3]), 'fenêtre absente'))
    elif a == 'cherche':
        P = points(h); k = 0
        for n, i, t, b in P:
            for s in re.split(r'(?<=[.!?;])\s+', texte(b)):
                if re.search(sys.argv[3], s, re.I) and k < 20: print(f'p{n}: {s[:240]}'); k += 1
