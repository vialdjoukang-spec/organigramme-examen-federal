#!/usr/bin/env python3
"""Extrait ou réinjecte une constante JSON de app_v2.html (skill ssp-json-data).

  json_inject.py extract NAME   → écrit data/NAME.json (indenté, lisible en diff)
  json_inject.py inject  NAME   → valide data/NAME.json puis le réinjecte, compacté
  json_inject.py check   NAME   → vérifie que l'aller-retour est identique à l'octet

Seules les constantes en JSON strict sont acceptées (SSP, TIP, NOT, GES, PHT).
SESSION, EXI et ATT résident désormais dans assets/config/interface.js ; les mêmes commandes y sont routées.
CLIN utilise des identifiants JS : on le modifie par ssp-patch.
"""
import hashlib, json, os, sys
from pathlib import Path
from _app import ROOT, read, write, span
from tip_data import TAG as TIP_TAG, ASSET as TIP_ASSET, SHARDS, load as load_tip, render as render_tip, compact as tip_compact, MAX_ASSET_BYTES


EXTERNES = {name: "assets/config/interface.js" for name in ("SESSION", "EXI", "ATT")}


def compact(v):
    return json.dumps(v, ensure_ascii=False, separators=(',', ':'))


def main(cmd, name):
    s = read()
    if name == 'TIP' and TIP_TAG in s:
        path = os.path.join(ROOT, 'data', 'TIP.json')
        baseline = os.path.join(ROOT, 'data', 'TIP.base.json')
        current = load_tip(ROOT, s)
        hashes = {k: hashlib.sha256(tip_compact(v).encode()).hexdigest() for k, v in current.items()}
        if cmd == 'check':
            print('TIP : 248 sources JSON et asset identiques.')
            return
        if cmd == 'extract':
            with open(path, 'w', encoding='utf-8') as f:
                json.dump(current, f, ensure_ascii=False, indent=1)
            with open(baseline, 'w', encoding='utf-8') as f:
                json.dump(hashes, f, indent=1)
            print('data/TIP.json extrait ; empreintes de base enregistrées.')
            return
        if cmd == 'inject':
            proposed = json.loads(Path(path).read_text(encoding='utf-8'))
            base = json.loads(Path(baseline).read_text(encoding='utf-8'))
            if list(proposed) != list(current) or set(base) != set(current):
                raise ValueError('TIP : codes ajoutés, supprimés ou réordonnés')
            changed = []
            for code, value in proposed.items():
                if (not isinstance(value, dict) or not isinstance(value.get('c'), list)
                        or len(value['c']) != 14 or not all(isinstance(part, str) for part in value['c'])):
                    raise ValueError(code + ' : 14 parties attendues')
                digest = hashlib.sha256(tip_compact(value).encode()).hexdigest()
                if digest != base[code]:
                    if hashes[code] not in (base[code], digest):
                        raise ValueError('TIP : conflit de modification sur ' + code)
                    changed.append(code)
                    current[code] = value
            asset = render_tip(current)
            if len(asset.encode()) > MAX_ASSET_BYTES:
                raise ValueError('Asset TIP au-delà de 12 Mio')
            for code in changed:
                with open(os.path.join(ROOT, SHARDS, code + '.json'), 'w', encoding='utf-8') as f:
                    json.dump(current[code], f, ensure_ascii=False, indent=1)
                    f.write('\n')
            with open(os.path.join(ROOT, TIP_ASSET), 'w', encoding='utf-8', newline='') as f:
                f.write(asset)
            load_tip(ROOT, s)
            print(f'TIP : {len(changed)} SSP réinjectés sans conflit.')
            return
        sys.exit(__doc__)
    destination = None
    asset = EXTERNES.get(name)
    if asset and s.count('<script src="' + asset + '"></script>') == 1:
        destination = os.path.join(ROOT, asset)
        s = read(destination)
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
        result = s[:a] + compact(val) + s[b:]
        if destination:
            write(result, destination)
        else:
            write(result)
        print(f'{name} réinjecté ({len(compact(val))} caractères). Lancez ensuite tests/run_tests.py.')
    else:
        sys.exit(__doc__)


if __name__ == '__main__':
    if len(sys.argv) != 3:
        sys.exit(__doc__)
    main(sys.argv[1], sys.argv[2])
