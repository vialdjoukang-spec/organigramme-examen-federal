#!/usr/bin/env python3
"""Appliquer un lot relu aux seules parties TIP.c ; préserver DD et fondamentaux."""
import argparse
import hashlib
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / 'tools'))
from _app import span
from tip_data import TAG, SHARDS, compact, render, load, MAX_ASSET_BYTES, ASSET


def appliquer_au_cours(item, lot):
    """Annoter le cours sans attribuer une relecture aux DD hérités."""
    assert len(lot['parties']) == len(lot['avant_sha256']) == len(lot['references_par_partie']) == 14
    current = [hashlib.sha256(text.encode()).hexdigest() for text in item['c']]
    assert item['c'] == lot['parties'] or current == lot['avant_sha256'], 'Le cours a changé : nouvelle relecture requise'
    assert all(isinstance(text, str) and text.strip() for text in lot['parties'])
    if 'v' not in item:
        item['v'] = {'S': [], 'c': [], 'd': [None] * len(item.get('d', []))}
    for source in lot['sources_ajoutees']:
        matches = [x for x in item['v']['S'] if x['id'] == source['id']]
        assert not matches or matches == [source], 'Collision dans les identifiants de source'
        if not matches:
            item['v']['S'].append(source)
    source_ids = {x['id'] for x in item['v']['S']}
    assert all(refs and all(n in source_ids for n in refs) for refs in lot['references_par_partie'])
    item['c'] = list(lot['parties'])
    item['v']['c'] = [['réorganisé', list(refs)] for refs in lot['references_par_partie']]


def appliquer(code, root=ROOT):
    root = Path(root)
    lot = json.loads((root / 'tools/cours/lots' / (code + '.json')).read_text())
    assert lot['version'] == 1 and lot['ssp'] == code
    app_path = root / 'app_v2.html'
    s = app_path.read_text(encoding='utf-8'); tip = load(root, s)
    appliquer_au_cours(tip[code], lot)
    if TAG in s:
        asset = render(tip)
        if len(asset.encode()) > MAX_ASSET_BYTES:
            raise ValueError('Asset TIP au-delà de 12 Mio')
        (root / SHARDS / (code + '.json')).write_text(json.dumps(tip[code], ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
        (root / ASSET).write_text(asset, encoding='utf-8', newline='')
        load(root, s)
    else:
        a, b = span(s, 'TIP')
        app_path.write_text(s[:a] + compact(tip) + s[b:], encoding='utf-8')
    print(code + ' : 14 parties du cours appliquées ; diagnostics différentiels conservés.')


if __name__ == '__main__':
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('ssp', choices=[x.stem for x in Path(__file__).with_name('lots').glob('*.json')])
    appliquer(p.parse_args().ssp)
