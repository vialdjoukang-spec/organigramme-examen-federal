#!/usr/bin/env python3
"""Extrait ou réinjecte une constante JSON de app_v2.html (skill ssp-json-data).

  json_inject.py extract NAME   → écrit data/NAME.json (indenté, lisible en diff)
  json_inject.py inject  NAME   → valide data/NAME.json puis le réinjecte, compacté
  json_inject.py check   NAME   → vérifie que l'aller-retour est identique à l'octet

Seules les constantes en JSON strict sont acceptées (SSP, TIP, NOT, GES, PHT).
EXI, ATT ou CLIN utilisent des identifiants JS : on les modifie par ssp-patch.
"""
import json, os, sys
from _app import ROOT, read, write, span


def compact(v):
    return json.dumps(v, ensure_ascii=False, separators=(',', ':'))


def main(cmd, name):
    s = read()
    a, b = span(s, name)
    path = os.path.join(ROOT, 'data', f'{name}.json')
    if cmd in ('extract', 'check'):
        try:
            val = json.loads(s[a:b])
        except json.JSONDecodeError as e:
            sys.exit(f'{name} n’est pas du JSON strict ({e}) ; utilisez ssp-patch.')
        same = compact(val) == s[a:b]
        if cmd == 'check':
            print(f'{name} : aller-retour {"identique" if same else "DIFFÉRENT"}.')
            sys.exit(0 if same else 1)
        if not same:
            print(f'Attention : la réinjection de {name} changera la mise en forme.')
        os.makedirs(os.path.dirname(path), exist_ok=True)
        json.dump(val, open(path, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
        print(f'data/{name}.json écrit.')
    elif cmd == 'inject':
        val = json.load(open(path, encoding='utf-8'))
        write(s[:a] + compact(val) + s[b:])
        print(f'{name} réinjecté ({len(compact(val))} caractères). Lancez ensuite tests/run_tests.py.')
    else:
        sys.exit(__doc__)


if __name__ == '__main__':
    if len(sys.argv) != 3:
        sys.exit(__doc__)
    main(sys.argv[1], sys.argv[2])
