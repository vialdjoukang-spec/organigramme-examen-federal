#!/usr/bin/env python3
"""GELER — porte P1 franchie : écrit LISTE_DX_CANONIQUE.md depuis audits/LISTE_DX.audit.json (liste_finale), signé SHA-256.
Usage (depuis le worktree) : python3 geler.py 043"""
import sys, json, hashlib, datetime
lot = f'{int(sys.argv[1]):03d}'
d = f'Claude/LOT_{lot}'
A = json.load(open(f'{d}/audits/LISTE_DX.audit.json'))
corr = '--corrections-appliquees' in sys.argv
assert A['verdict'] == 'GEL' or corr, f"porte P1 non franchie : {A['verdict']} / {A.get('finale')}"
if corr:  # verdict CORRIGER : la liste_finale de l'auditeur EST la correction ; elle est appliquée telle quelle
    open(f'{d}/CORRECTIONS_AUDIT.md', 'a').write('# Corrections de l\'audit P1 (à appliquer par les rédacteurs)\n\n' + ''.join(
        f"- [{c.get('gravite')}] {c.get('objet')} → {c.get('correction')} ({c.get('source')})\n" for c in A.get('corrections', [])))
L = sorted(A['liste_finale'], key=lambda x: x['rang'])
assert len(L) == 10
lignes = [f"DX.{x['rang']} — {x['nom']}" + (f" 🚩 {x['E'] if str(x['E']).startswith('E') else 'E' + str(x['E'])}" if x.get('grave') or x.get('E') else '') for x in L]
corps = '\n'.join(lignes)
sha = hashlib.sha256(corps.encode()).hexdigest()
open(f'{d}/LISTE_DX_CANONIQUE.md', 'w').write(f"# LOT_{lot} — liste canonique gelée (porte P1)\n\n{corps}\n\nGel : {datetime.date.today()} · SHA-256 de la liste : {sha}\n")
statut = A['verdict'] + (", liste corrigée de l'auditeur appliquée" if corr else '')
open(f'{d}/JOURNAL.md', 'a').write(f"- {datetime.date.today()} · gel P1 de la liste DX (audit indépendant, verdict {statut}) · sha {sha[:16]}\n")
print(corps)
