#!/usr/bin/env python3
"""APPLIQUER_HTML — applique les corrections d'un audit (avant/apres exacts) directement à un HTML renforcé (sans fragments).
Usage : appliquer_html.py fichier.html audit.json"""
import sys, json
f, a = sys.argv[1], json.load(open(sys.argv[2]))
t = open(f, encoding='utf-8').read()
ok = ko = 0
for c in a.get('corrections', []) + a.get('restants', []):
    av, ap = c.get('avant', ''), c.get('apres', '')
    if av and t.count(av) == 1:
        t = t.replace(av, ap); ok += 1
    else:
        ko += 1; print('NON APPLIQUÉE :', av[:90].replace('\n', ' '))
open(f, 'w', encoding='utf-8').write(t)
print(f.split('/')[-1], ok, 'appliquées,', ko, 'non trouvées')
