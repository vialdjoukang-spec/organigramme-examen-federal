#!/usr/bin/env python3
"""Vérifie un lot en une commande ; une ligne par défaut, -v pour le détail. Code 1 si erreur.
  lot.py cours S4.10 [S4.11 …]   tools/cours/lots/<SSP>.json : 14 parties, références, lu_le daté
  lot.py mono <clé> [<clé> …]     monographie : rubriques, src + date de lecture, doses sans AIPS
  lot.py auto [base]              tout ce qui a changé depuis origin/main (lots + monographies)
Compte aussi les « À vérifier » (signalés, non bloquants).
"""
import json, os, re, subprocess, sys
from _c import ROOT, load, DOSE, DATE, SSP_RE, mono_key
REQ = ['def', 'epi', 'phy', 'cli', 'exp', 'dia', 'but', 'mes', 'pha', 'src', 'lu', 'n']
def cours(s, E, W):
    p = f'tools/cours/lots/{s}.json'
    if not os.path.exists(os.path.join(ROOT, p)): E.append(f'{s}: lot absent'); return
    d = load(p)
    if not isinstance(d, dict): return  # delta annexe, hors lot de cours
    if len(d.get('parties', [])) != 14: E.append(f'{s}: {len(d.get("parties", []))} parties ≠ 14')
    for i, r in enumerate(d.get('references_par_partie', []), 1):
        if not r: E.append(f'{s}.{i}: sans référence')
    if not DATE.search(str(d.get('lu_le', ''))): E.append(f'{s}: lu_le non daté')
    t = ' '.join(d.get('parties', []))
    W.append(t.count('À vérifier'))
    for m in set(DOSE.findall(t)):
        if 'AIPS' not in t: E.append(f'{s}: dose « {m} » sans extrait AIPS')
def mono(k, E, W):
    k = mono_key(k); d = load(f'data/ck/mono/{k[0] if k[0].isalpha() else "0"}.json').get(k)
    if d is None: E.append(f'{k}: absent'); return
    miss = [f for f in REQ if f not in d and not (f == 'exp' and 'exp_ref' in d)]
    if miss: E.append(f'{k}: rubriques manquantes {miss}')
    if not DATE.search(str(d.get('lu', '')) + str(d.get('src', ''))): E.append(f'{k}: source non datée')
    t = json.dumps(d, ensure_ascii=False); W.append(t.count('À vérifier'))
    pha = str(d.get('pha', ''))
    if DOSE.search(pha) and 'AIPS' not in pha + str(d.get('src', '')) and 'À vérifier' not in pha:
        E.append(f'{k}: dose sans extrait AIPS')
def auto(base):
    f = subprocess.run(['git', 'diff', '--name-only', f'{base}...HEAD'], cwd=ROOT, capture_output=True, text=True).stdout.split()
    c = [os.path.basename(x)[:-5] for x in f if x.startswith('tools/cours/lots/') and SSP_RE.match(os.path.basename(x)[:-5])]
    m = []
    for x in f:
        if x.startswith('data/ck/mono/') and x.endswith('.json'):
            old = subprocess.run(['git', 'show', f'{base}:{x}'], cwd=ROOT, capture_output=True, text=True).stdout
            o = json.loads(old) if old else {}; n = load(x)
            m += [k for k in n if n[k] != o.get(k)]
    return c, m
def main(a):
    v = '-v' in a; a = [x for x in a if x != '-v']
    if not a: sys.exit(__doc__)
    E, W = [], []
    if a[0] == 'auto': c, m = auto(a[1] if len(a) > 1 else 'origin/main')
    elif a[0] == 'cours': c, m = a[1:], []
    elif a[0] == 'mono': c, m = [], a[1:]
    else: sys.exit(__doc__)
    for s in c: cours(s, E, W)
    for k in m: mono(k, E, W)
    n = len(c) + len(m)
    print(f'{"OK" if not E else "ÉCHEC"} {n} élément(s) · {len(E)} erreur(s) · {sum(W)} « À vérifier »' + (f' · 1re : {E[0]}' if E and not v else ''))
    if v: print('\n'.join(E))
    sys.exit(1 if E else 0)
if __name__ == '__main__': main(sys.argv[1:])
