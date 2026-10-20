#!/usr/bin/env python3
"""Vue de code sans données (skill ssp-extrait-cible).

Remplace les valeurs de TIP, NOT et GES par un repère qui donne leur taille, puis
écrit la vue dans .cache/app_v2.slim.html (ignoré par git). L'agent lit cette vue
au lieu du fichier complet ; il n'édite jamais la vue.
"""
import os, sys
from _app import ROOT, read, span
from tip_data import TAG
NAMES = sys.argv[1:] or ['TIP', 'NOT', 'GES']
s = read()
total = len(s)
for name in NAMES:
    if name == 'TIP' and TAG in s:
        continue  # La source lisible réside déjà dans data/tip/.
    a, b = span(s, name)
    s = s[:a] + f'/*[{name} : {b - a} caractères retirés ; voir data/{name}.json ou tools/json_inject.py]*/null' + s[b:]
out = os.path.join(ROOT, '.cache', 'app_v2.slim.html')
os.makedirs(os.path.dirname(out), exist_ok=True)
open(out, 'w', encoding='utf-8').write(s)
print(f'{out} : {len(s)} caractères sur {total} ({100 * len(s) / total:.2f} %).')
