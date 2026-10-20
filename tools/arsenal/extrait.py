#!/usr/bin/env python3
"""Sort UNIQUEMENT le bloc à traiter, en JSON compact (jamais app_v2.html entier).
  extrait.py ssp S4.10 [--partie N]   cours TIP (c = 14 parties) depuis data/tip/
  extrait.py mono <clé|libellé> [--champ f]  monographie DD depuis data/ck/mono/
  extrait.py region <id> [--k peau_0]       région CS (GES) depuis app_v2.html
  extrait.py liste <ssp|mono|region>        identifiants seulement
"""
import os, sys
from _c import ROOT, load, out, mono_key
def opt(a, n):
    return a[a.index(n) + 1] if n in a else None
def main(a):
    if len(a) < 2: sys.exit(__doc__)
    kind, ident = a[0], a[1]
    if kind == 'liste':
        if ident == 'ssp': out(sorted(f[:-5] for f in os.listdir(os.path.join(ROOT, 'data/tip'))))
        elif ident == 'mono':
            out(sum((list(load(f'data/ck/mono/{f}')) for f in sorted(os.listdir(os.path.join(ROOT, 'data/ck/mono')))), []))
        else: out([r['id'] for r in ges()])
        return
    if kind == 'ssp':
        d = load(f'data/tip/{ident}.json'); p = opt(a, '--partie')
        out({'ssp': ident, 'partie': int(p), 'c': d['c'][int(p) - 1]} if p else {'ssp': ident, 'c': d['c'], 'fs': d.get('fs')})
    elif kind == 'mono':
        k = mono_key(ident); d = load(f'data/ck/mono/{k[0] if k[0].isalpha() else "0"}.json')
        if k not in d: sys.exit(f'absent : {k}')
        f = opt(a, '--champ'); out({k: d[k][f] if f else d[k]})
    elif kind == 'region':
        r = next((x for x in ges() if x['id'] == ident), None) or sys.exit(f'absent : {ident}')
        k = opt(a, '--k')
        out(next(i for i in r['items'] if i['k'] == k) if k else r)
    else: sys.exit(__doc__)
def ges():
    import json
    from _app import read, span
    s = read(); x, y = span(s, 'GES'); return json.loads(s[x:y])
if __name__ == '__main__': main(sys.argv[1:])
