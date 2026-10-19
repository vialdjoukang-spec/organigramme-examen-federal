#!/usr/bin/env python3
"""Appliquer un lot relu aux seules parties TIP.c ; préserver DD et fondamentaux."""
import argparse
import hashlib
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / 'tools'))
from _app import read, write, span


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


def appliquer(code):
    lot = json.loads((Path(__file__).with_name('lots') / (code + '.json')).read_text())
    assert lot['version'] == 1 and lot['ssp'] == code
    s = read(); a, b = span(s, 'TIP'); tip = json.loads(s[a:b])
    appliquer_au_cours(tip[code], lot)
    write(s[:a] + json.dumps(tip,ensure_ascii=False,separators=(',', ':')) + s[b:])
    print(code + ' : 14 parties du cours appliquées ; diagnostics différentiels conservés.')


if __name__ == '__main__':
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('ssp', choices=[x.stem for x in Path(__file__).with_name('lots').glob('*.json')])
    appliquer(p.parse_args().ssp)
