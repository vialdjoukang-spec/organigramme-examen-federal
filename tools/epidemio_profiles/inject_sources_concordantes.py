#!/usr/bin/env python3
"""Reporte dans les cours sources (main) le même encadré que celui injecté dans FedMed_Progression.html,
pour qu'une reconstruction par outils/injecter_cours_fedmed.py le conserve. Sortie : out/stage_concordant/<chemin>."""
import json, os, sys, subprocess, re
ICI = os.path.dirname(os.path.abspath(__file__)); OUT = os.path.join(os.path.dirname(ICI), 'out'); sys.path.insert(0, ICI)
import inject as I
sys.argv = ['x', '/dev/null', '/dev/null']
src = open(f'{ICI}/inject_progression.py').read()
bloc_src = src[src.index('def bloc('):src.index('journal = []')]
ref = {x['n']: x for x in json.load(open(f'{OUT}/referentiel.json'))}
import html as H
exec(bloc_src)
carte = json.load(open(f'{I.BRIEF}/carte_lots.json'))['lecons']
conc = {x['n']: x for x in json.load(open(f'{OUT}/concordance.json')) if x['statut'] == 'concordant'}
jr = json.load(open(f'{OUT}/inject_progression_journal.json'))
arbre = dict(l.split('\t')[::-1] for l in subprocess.run(['git', '-C', I.REPO, 'ls-tree', '-r', 'origin/main'], capture_output=True, text=True).stdout.splitlines())
for j in jr:
    if j['statut'] not in ('injecte', 'regenere'): continue
    v = carte[f"{j['lot']:03d}:{j['dx']}"]; n = int(j['dx'][2:])
    assert v['ref'] == 'origin/main' and v['chemin'] in arbre and arbre[v['chemin']].split()[2] == v['blob'], v['chemin']
    h0 = subprocess.run(['git', '-C', I.REPO, 'cat-file', 'blob', v['blob']], capture_output=True).stdout.decode('utf-8')
    nouveau = bloc(n, [conc[k] for k in sorted(j['valeurs'])])
    deb, fin = I.DEB.format(n=n), I.FIN.format(n=n)
    if deb in h0: h = h0[:h0.index(deb)] + nouveau + h0[h0.index(fin) + len(fin):]
    else:
        loc, _ = I.localiser(h0, n); h = h0[:loc[1]] + nouveau + '\n' + h0[loc[1]:]
    assert len(h.encode()) < I.MAX and (I.equilibre(h) == I.equilibre(h0) or not I.equilibre(h))
    p = f"{OUT}/stage_concordant/{v['chemin']}"; os.makedirs(os.path.dirname(p), exist_ok=True)
    open(p, 'w', encoding='utf-8').write(h); print(v['chemin'], len(h0.encode()), '→', len(h.encode()))
