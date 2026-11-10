#!/usr/bin/env python3
"""GELER — porte P1 franchie : écrit LISTE_DX_CANONIQUE.md depuis audits/LISTE_DX.audit.json (liste_finale), signé SHA-256.
Usage (depuis le worktree) : python3 geler.py 043"""
import sys, json, hashlib, datetime
lot = f'{int(sys.argv[1]):03d}'
d = f'Claude/LOT_{lot}'
A = json.load(open(f'{d}/audits/LISTE_DX.audit.json'))
assert A['verdict'] == 'GEL' and A.get('finale') == 'oui', f"porte P1 non franchie : {A['verdict']} / {A.get('finale')}"
L = sorted(A['liste_finale'], key=lambda x: x['rang'])
assert len(L) == 10
lignes = [f"DX.{x['rang']} — {x['nom']}" + (f" 🚩 {x['E'] if str(x['E']).startswith('E') else 'E' + str(x['E'])}" if x.get('grave') or x.get('E') else '') for x in L]
corps = '\n'.join(lignes)
sha = hashlib.sha256(corps.encode()).hexdigest()
open(f'{d}/LISTE_DX_CANONIQUE.md', 'w').write(f"# LOT_{lot} — liste canonique gelée (porte P1)\n\n{corps}\n\nGel : {datetime.date.today()} · SHA-256 de la liste : {sha}\n")
open(f'{d}/JOURNAL.md', 'a').write(f"- {datetime.date.today()} · gel P1 de la liste DX (audit indépendant, verdict GEL) · sha {sha[:16]}\n")
print(corps)
