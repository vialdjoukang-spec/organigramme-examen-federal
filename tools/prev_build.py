#!/usr/bin/env python3
"""Compile data/ck/prev.json : constante PRV de app_v2.html (ordre et chiffres) et assets/ck/prev.js (cadre, source).
  python3 tools/prev_build.py           # contrôle (tools/audit/prevalence.py), puis écrit
  python3 tools/prev_build.py --check   # échoue si PRV ou assets/ck/prev.js ne sont pas à jour (CI)
ck_build.py inclut prev.js dans ses sorties ; ne retouchez jamais PRV à la main."""
import json, os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(HERE, 'audit'))
from _app import ROOT, APP, read, write, span  # noqa: E402
import prevalence as P  # noqa: E402


def prev_js(root=ROOT):
    from ck_build import js
    return js('prev', P.detail(P.charger(root)))


def main(argv):
    err = P.controler()
    for c, i, r, m in err:
        print(f'ÉCHEC {r} {c}|{i} : {m}')
    if err:
        return 1
    D = P.charger()
    v = json.dumps(P.prv(D), ensure_ascii=False, separators=(',', ':'), sort_keys=True)
    s = read(); a, b = span(s, 'PRV')
    jsf = os.path.join(ROOT, 'assets', 'ck', 'prev.js'); jc = prev_js()
    if '--check' in argv:
        bad = []
        if s[a:b] != v: bad.append('PRV de app_v2.html')
        if not os.path.exists(jsf) or open(jsf, encoding='utf-8').read() != jc: bad.append('assets/ck/prev.js')
        for x in bad: print(f'ÉCHEC {x} n’est pas à jour : lancez python3 tools/prev_build.py')
        if bad: return 1
        print('prev_build : à jour.'); return 0
    if s[a:b] != v: write(s[:a] + v + s[b:])
    open(jsf, 'w', encoding='utf-8', newline='\n').write(jc)
    print(f'prev_build : PRV {len(v)} octets, prev.js {len(jc.encode())} octets.')
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
