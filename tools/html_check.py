#!/usr/bin/env python3
"""Validation HTML par cliquet : le validateur Nu ne doit signaler aucune erreur nouvelle.

Usage : html_check.py <sortie-json-de-vnu> [--update]
La référence qa/html-baseline.json compte les erreurs par message (sans numéro de
ligne). Une PR échoue si un message apparaît plus souvent que dans la référence.
"""
import collections, json, os, re, sys
from _app import ROOT
BASE = os.path.join(ROOT, 'qa', 'html-baseline.json')


def norm(m):
    return re.sub(r'\s+', ' ', m.get('message', '')).strip()


data = json.load(open(sys.argv[1], encoding='utf-8'))
cur = collections.Counter(norm(m) for m in data.get('messages', []) if m.get('type') == 'error')
if '--update' in sys.argv:
    json.dump(dict(sorted(cur.items())), open(BASE, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    print(f'Référence mise à jour : {sum(cur.values())} erreurs connues.')
    sys.exit(0)
base = collections.Counter(json.load(open(BASE, encoding='utf-8')))
new = {k: v - base.get(k, 0) for k, v in cur.items() if v > base.get(k, 0)}
print(f'Erreurs HTML : {sum(cur.values())} (référence {sum(base.values())}) ; nouvelles : {sum(new.values())}.')
for k, v in new.items():
    print(f'  NOUVELLE ×{v} : {k[:200]}')
sys.exit(1 if new else 0)
