#!/usr/bin/env python3
"""Vérifie les octets et la navigation d'un LOT, sans attribuer de score médical."""
import argparse
import hashlib
import json
from collections import Counter
from html.parser import HTMLParser
from pathlib import Path


class Navigation(HTMLParser):
    def __init__(self):
        super().__init__()
        self.ids = []
        self.targets = []
        self.sections = []

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if a.get('id'):
            self.ids.append(a['id'])
            if tag == 'section':
                self.sections.append(a['id'])
        if a.get('href', '').startswith('#'):
            self.targets.append(a['href'][1:])
        if a.get('popovertarget'):
            self.targets.append(a['popovertarget'])


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('dossier', type=Path)
    ap.add_argument('--sortie', type=Path, required=True)
    args = ap.parse_args()
    root = args.dossier
    lot = root.name
    expected = [f'{lot}_Phase_A_V0.html'] + [f'{lot}_Phase_B_V0_DX.{n}.html' for n in range(1, 11)]
    manifest = json.loads((root / 'MANIFESTE.json').read_text())
    rows = []
    for name in expected:
        p = root / name
        row = {'fichier': name, 'erreurs': []}
        if not p.exists():
            row['erreurs'].append('Fichier absent')
            rows.append(row)
            continue
        raw = p.read_bytes()
        row.update(octets=len(raw), sha256=hashlib.sha256(raw).hexdigest())
        if not 100000 <= len(raw) <= 200000:
            row['erreurs'].append('Taille hors bande 100000–200000 octets')
        if manifest.get(name) != {k: row[k] for k in ('octets', 'sha256')}:
            row['erreurs'].append('Manifeste différent des octets courants')
        text = raw.decode('utf-8')
        nav = Navigation()
        nav.feed(text)
        duplicates = [key for key, n in Counter(nav.ids).items() if n > 1]
        missing = sorted(set(nav.targets) - set(nav.ids))
        if duplicates:
            row['erreurs'].append({'ids_dupliques': duplicates})
        if missing:
            row['erreurs'].append({'renvois_absents': missing})
        points = [i for i in nav.sections if i.rsplit('-p', 1)[-1].isdigit()]
        if len(points) != 14 or {int(i.rsplit('-p', 1)[-1]) for i in points} != set(range(1, 15)):
            row['erreurs'].append('Les quatorze sections ne sont pas identifiées')
        if f'<!-- FIN_FICHIER {p.stem} -->' not in text:
            row['erreurs'].append('Marqueur FIN_FICHIER absent ou incohérent')
        rows.append(row)
    report = {'lot': lot, 'controle': 'Octets, manifeste, structure et renvois seulement ; P2, P3 et CI restent distincts.',
              'fichiers': rows, 'valide': not any(r['erreurs'] for r in rows)}
    args.sortie.write_text(json.dumps(report, ensure_ascii=False, indent=2) + '\n')
    print(json.dumps({'valide': report['valide'], 'fichiers_presents': sum('sha256' in r for r in rows),
                      'erreurs': {r['fichier']: r['erreurs'] for r in rows if r['erreurs']}}, ensure_ascii=False))
    return 0 if report['valide'] else 1


if __name__ == '__main__':
    raise SystemExit(main())
