#!/usr/bin/env python3
"""RESTAURER_FOND — ordre de Vial du 13.11.2026 : retire le fond « vivant » injecté par le designer
(bloc /*fm-palette*/…/*fin*/ et body{background:var(--fm-a-doux…)}) pour revenir au fond blanc de forme.css.
Usage : python3 Claude/_outils/restaurer_fond.py Claude/LOT_0NN/*.html   (idempotent ; --verifier : code 1 si un fond coloré reste)"""
import re, sys
BLOC = re.compile(r'/\*fm-palette\*/.*?/\*fin\*/', re.S)
CORPS = re.compile(r'body\{background:var\(--fm-a-doux[^}]*\}')
FOND = re.compile(r'--fm-fond:\s*#(?!fff\b|ffffff\b)[0-9a-fA-F]{3,6}')
verif = '--verifier' in sys.argv
reste = 0
for f in [a for a in sys.argv[1:] if not a.startswith('--')]:
    h = open(f, encoding='utf-8').read()
    n = BLOC.sub('', CORPS.sub('', h))
    if verif:
        if FOND.search(n if False else h) or BLOC.search(h) or CORPS.search(h):
            reste += 1; print('fond coloré :', f)
        continue
    if n != h:
        open(f, 'w', encoding='utf-8').write(n); print('restauré :', f)
sys.exit(1 if reste else 0)
