#!/usr/bin/env python3
"""Inventorie les champs À vérifier d'un instantané Git, sans modifier le contenu clinique."""
import argparse
import collections
import datetime
from html.parser import HTMLParser
import json
from pathlib import Path
import re
import subprocess
import unicodedata

ROOT = Path(__file__).resolve().parents[1]


def git(*args):
    return subprocess.check_output(['git', '-C', str(ROOT), *args], text=True)


class Text(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.parts = []

    def handle_data(self, data):
        self.parts.append(data)


def occurrences(value):
    parser = Text()
    parser.feed(value)
    plain = ''.join(c for c in unicodedata.normalize('NFD', ' '.join(parser.parts).casefold())
                    if not unicodedata.combining(c))
    return len(re.findall(r'\ba\s+verifier\b', plain))


def walk(value, pointer='', context=None):
    if isinstance(value, dict):
        context = next((value[k] for k in ('id', 'k', 'dci', 'nom', 'label')
                        if isinstance(value.get(k), str)), context)
        for key, child in value.items():
            escaped = key.replace('~', '~0').replace('/', '~1')
            yield from walk(child, pointer + '/' + escaped, context)
    elif isinstance(value, list):
        for i, child in enumerate(value):
            yield from walk(child, pointer + '/' + str(i), context)
    elif isinstance(value, str):
        count = occurrences(value)
        if count:
            yield {'pointeur': pointer or '/', 'contexte': context,
                   'occurrences': count}


def inventory(ref):
    sha = git('rev-parse', ref).strip()
    paths = git('ls-tree', '-r', '--name-only', sha, 'data/ck', 'data/cs').splitlines()
    entries = []
    for path in paths:
        if not path.endswith('.json') or '/schema/' in path or path.endswith('.schema.json'):
            continue
        if path in {'data/cs/format.json'}:
            continue
        for row in walk(json.loads(git('show', sha + ':' + path))):
            entries.append({'fichier': path, **row})
    app = git('show', sha + ':app_v2.html')
    for name in ('TIP', 'NOT', 'GES'):
        if name == 'TIP' and '<script src="assets/config/tip.js"></script>' in app:
            from tip_data import from_js
            data = from_js(git('show', sha + ':assets/config/tip.js'))
            fichier = 'assets/config/tip.js'
        else:
            marker = '\nconst ' + name + '='
            if app.count(marker) != 1:
                raise ValueError('Ancre clinique absente ou ambiguë : ' + name)
            data = json.JSONDecoder().raw_decode(app.split(marker, 1)[1])[0]
            fichier = 'app_v2.html'
        for row in walk(data, '/' + name):
            entries.append({'fichier': fichier, **row})
    counts = collections.Counter(row['fichier'] for row in entries)
    return {
        'date_generation': datetime.datetime.now(datetime.timezone.utc).isoformat(),
        'ref': ref, 'sha': sha,
        'perimetre': 'Données CK/CS et constantes cliniques TIP/NOT/GES ; schémas et format CS exclus.',
        'limite': 'Champs marqués explicitement, pas un audit médical ni une liste exhaustive des erreurs. '
                  'Branches non fusionnées exclues : voir ETAT.json.en_attente.',
        'champs': len(entries),
        'occurrences': sum(row['occurrences'] for row in entries),
        'par_fichier': dict(sorted(counts.items())),
        'elements': entries,
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--ref', default='origin/main')
    parser.add_argument('--sortie', type=Path, required=True)
    args = parser.parse_args()
    report = inventory(args.ref)
    args.sortie.parent.mkdir(parents=True, exist_ok=True)
    args.sortie.write_text(json.dumps(report, ensure_ascii=False, indent=1) + '\n')
    print(f"{report['champs']} champs, {report['occurrences']} occurrences, "
          f"{len(report['par_fichier'])} fichiers ; instantané {report['sha'][:7]}")


if __name__ == '__main__':
    main()
