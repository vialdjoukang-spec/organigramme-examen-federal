#!/usr/bin/env python3
"""APPLIQUER (D-7 sur fragments) — applique les corrections d'un audit P3 aux fragments d'une cible, par remplacement exact.
Usage (depuis le worktree) : python3 appliquer.py LOT CIBLE [--json corrections.json]
Par défaut : Claude/LOT_XXX/audits/<html>.audit.json (champ corrections[].avant/apres).
Chaque « avant » doit apparaître exactement une fois dans l'ensemble des fragments ; sinon : signalé, non appliqué."""
import sys, os, json, glob, html
lot, cible = f'{int(sys.argv[1]):03d}', sys.argv[2]
d = f'Claude/LOT_{lot}'
nom = f'LOT_{lot}_Phase_A_V0.html' if cible in ('A', 'PA') else f'LOT_{lot}_Phase_B_V0_{cible}.html'
src = sys.argv[sys.argv.index('--json') + 1] if '--json' in sys.argv else f'{d}/audits/{nom}.audit.json'
C = json.load(open(src))
C = C['corrections'] if isinstance(C, dict) else C
frs = sorted(glob.glob(f'{d}/_travail/{"PA" if cible in ("A","PA") else cible}/fragments/p*.html'))
T = {f: open(f, encoding='utf-8').read() for f in frs}
ok, ko = 0, []
for c in C:
    a, b = c.get('avant', ''), c.get('apres', '')
    if not a:
        continue
    cands = [a, html.unescape(a)]
    fait = False
    for v in cands:
        hits = [f for f in T if T[f].count(v) == 1]
        tot = sum(T[f].count(v) for f in T)
        if tot == 1:
            T[hits[0]] = T[hits[0]].replace(v, b)
            fait = True
            break
    if fait:
        ok += 1
    else:
        ko.append(a[:90])
for f, t in T.items():
    open(f, 'w', encoding='utf-8').write(t)
print(f'{nom} : {ok} corrections appliquées, {len(ko)} non trouvées')
for k in ko:
    print('  NON TROUVÉE :', k)
