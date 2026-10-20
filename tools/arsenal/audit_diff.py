#!/usr/bin/env python3
"""Pour l'auditeur : seules les valeurs modifiées (base...HEAD) avec leurs sources, en JSON lignes.
  audit_diff.py [base=origin/main] [--max 400]   (troncature par valeur)
Couvre data/tip/*.json (parties c), data/ck/mono/*.json (rubriques), tools/cours/lots/*.json.
Autres fichiers : nom + nombre de lignes +/-. Ne relit jamais la PR entière.
"""
import json, subprocess, sys
from _c import ROOT
def git(*a): return subprocess.run(['git', *a], cwd=ROOT, capture_output=True, text=True).stdout
def j(ref, p):
    t = git('show', f'{ref}:{p}'); return json.loads(t) if t.strip() else {}
def cut(x, n): x = x if isinstance(x, str) else json.dumps(x, ensure_ascii=False); return x if len(x) <= n else x[:n] + '…'
def main(a):
    n = int(a[a.index('--max') + 1]) if '--max' in a else 400
    a = [x for i, x in enumerate(a) if x != '--max' and (i == 0 or a[i - 1] != '--max')]
    base = git('merge-base', a[0] if a else 'origin/main', 'HEAD').strip()
    for line in git('diff', '--numstat', base, 'HEAD').splitlines():
        ad, de, p = line.split('\t')
        if p.startswith('data/ck/mono/') and p.endswith('.json'):
            o, h = j(base, p), j('HEAD', p)
            for k in h:
                if h[k] == o.get(k): continue
                ch = {f: cut(h[k][f], n) for f in h[k] if h[k].get(f) != (o.get(k) or {}).get(f)}
                print(json.dumps({'mono': k, 'src': h[k].get('src'), 'lu': h[k].get('lu'), 'modif': ch}, ensure_ascii=False))
        elif p.startswith('data/tip/') and p.endswith('.json'):
            o, h = j(base, p), j('HEAD', p)
            for i, c in enumerate(h.get('c', []), 1):
                if c != (o.get('c') or [None] * 14)[i - 1:i][0:1] and (len(o.get('c', [])) < i or o['c'][i - 1] != c):
                    print(json.dumps({'ssp': p[9:-5], 'partie': i, 'txt': cut(c, n)}, ensure_ascii=False))
        elif p.startswith('tools/cours/lots/'):
            h = j('HEAD', p)
            print(json.dumps({'lot': p, 'lu_le': h.get('lu_le'), 'sources': h.get('sources_ajoutees'), 'refs': h.get('references_par_partie')}, ensure_ascii=False))
        else:
            print(json.dumps({'fichier': p, '+': ad, '-': de}))
if __name__ == '__main__': main(sys.argv[1:])
