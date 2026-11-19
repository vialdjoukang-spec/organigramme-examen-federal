#!/usr/bin/env python3
"""ABRÉVIATIONS — porte avant audit inspirée de Lyncée (tools/lyncee.py, contrôle G4), adaptée aux cours LOT (zéro modèle).
Signale tout sigle (2 à 6 majuscules) dont la PREMIÈRE occurrence dans le corps du cours n'est ni précédée ni suivie
de sa forme développée entre parenthèses. Les audits B relèvent ce défaut à chaque LOT ; le script le trouve en 0,1 s.
Usage : python3 Claude/_harnais/abreviations.py Claude/LOT_0NN/*.html     (code 1 si un sigle n'est pas développé)
"""
import re, sys, html

ADMIS = set('DX SSP LOT PDF HTML URL CC BY SA AIPS ORL OMS CHUV HUG SSI OFS ADN ARN IRM UI SRC ERC ESC ESO ESGE UEG ESNM'.split()) - {'AIPS', 'ORL', 'HUG', 'CHUV', 'SSI', 'IRM', 'OFS', 'ESO', 'ESGE', 'UEG', 'ESNM', 'SRC', 'ERC'}
SIGLE = re.compile(r'(?<![\w-])([A-Z][A-Z0-9]{1,5})(?![\w-])')


def corps(h):
    h = re.sub(r'<section class="bloc" id="sources">.*', ' ', h, flags=re.S)
    h = re.sub(r'<li id="sb-.*?</li>', ' ', h, flags=re.S)
    h = re.sub(r'<(nav|header|script|style|title)\b.*?</\1>', ' ', h, flags=re.S)
    h = re.sub(r'<svg\b.*?</svg>', ' ', h, flags=re.S)
    return re.sub(r'\s+', ' ', html.unescape(re.sub(r'<[^>]+>', ' ', h)))


def verifier(f):
    t = corps(open(f, encoding='utf-8').read()); vus = set(); out = []
    for m in SIGLE.finditer(t):
        s = m.group(1)
        if s in vus or s in ADMIS or re.fullmatch(r'[IVX]+|S\d+|E\d|DX\d*', s):
            continue
        vus.add(s)
        avant, apres = t[max(0, m.start() - 90):m.start()], t[m.end():m.end() + 90]
        if not (re.match(r'\s*\(', apres) or re.search(r'\(\s*$', avant)):
            out.append((s, t[max(0, m.start() - 40):m.end() + 40]))
    return out


if __name__ == '__main__':
    n = 0
    for f in sys.argv[1:]:
        for s, ctx in verifier(f):
            n += 1; print(f'{f.split("/")[-1]} · {s} · …{ctx}…')
    print(f'{n} sigle(s) non développé(s) à la première occurrence'); sys.exit(1 if n else 0)
