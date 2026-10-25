#!/usr/bin/env python3
"""build_extra.py — fragments d'examens propres au LOT (même format que bibliotheque_examens/fragments), chargés en plus de la bibliothèque commune."""
import os, sys, json
D = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, '/workspace/audit_1_10/bibliotheque_examens'); sys.path.insert(0, D)
from build_bibliotheque import fragment
from donnees_extra import EXTRA
os.makedirs(os.path.join(D, 'fragments'), exist_ok=True)
idx = {}
for k, e in sorted(EXTRA.items()):
    fr = fragment(k, e); open(os.path.join(D, 'fragments', k + '.html'), 'w').write(fr + '\n')
    idx[k] = {'lex': e['lex'], 'cat': e['cat'], 'titre': e['titre'], 'fragment': f'fragments/{k}.html', 'octets': len(fr.encode())}
json.dump(idx, open(os.path.join(D, 'index.json'), 'w'), ensure_ascii=False, indent=1)
print(len(idx), 'fragments supplémentaires')
