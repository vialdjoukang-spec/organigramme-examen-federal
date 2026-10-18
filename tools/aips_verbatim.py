#!/usr/bin/env python3
"""Compare les extraits aux textes officiels Refdata ; ne valide aucune dose clinique.

Usage : aips_verbatim.py [table.json] --cache prive/aips [--hors-ligne]
Les documents restent hors git. Chaque ligne non vide d'extrait doit exister dans
le texte officiel (espaces normalisés). Les caractères de la police Symbol sont
décodés explicitement : m → µ, ³ → ≥. Les unités nécessitent toujours une relecture.
"""
import argparse
import hashlib
from html.parser import HTMLParser
import json
from pathlib import Path
import re
import unicodedata
from urllib.parse import urlparse
from urllib.request import urlopen


class OfficialText(HTMLParser):
    def __init__(self, symbol_classes):
        super().__init__()
        self.symbol_classes = symbol_classes
        self.stack = []
        self.parts = []

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag in {'p', 'div', 'br', 'tr', 'td', 'li', 'h1', 'h2', 'h3'}:
            self.parts.append('\n')
        if tag not in {'br', 'img', 'meta', 'link', 'hr', 'input'}:
            symbolic = bool(set(attrs.get('class', '').split()) & self.symbol_classes)
            symbolic |= 'symbol' in (attrs.get('style', '') + attrs.get('face', '')).lower()
            self.stack.append((tag, symbolic))

    def handle_endtag(self, tag):
        for i in range(len(self.stack)-1, -1, -1):
            if self.stack[i][0] == tag:
                self.stack = self.stack[:i]
                break

    def handle_data(self, data):
        if any(tag in {'style', 'script'} for tag, _ in self.stack):
            return
        if any(symbolic for _, symbolic in self.stack):
            data = data.translate(str.maketrans({'m': 'µ', '³': '≥'}))
        self.parts.append(data)


def decode(html):
    classes = {name for name, _ in re.findall(r'\.([\w-]+)\{([^}]*Symbol[^}]*)\}', html, re.I)}
    parser = OfficialText(classes)
    parser.feed(html)
    return ''.join(parser.parts)


def normalize(text):
    return ' '.join(unicodedata.normalize('NFC', text).split())


def missing_lines(row, official):
    official = normalize(official)
    return [line for excerpt in row.get('aips_extrait', [])
            for line in excerpt['texte'].splitlines()
            if line.strip() and normalize(line) not in official]


def main():
    args = argparse.ArgumentParser(description=__doc__)
    args.add_argument('table', nargs='?', default='data/ck/doses_ch.json')
    args.add_argument('--cache', type=Path, default=Path('prive/aips'))
    args.add_argument('--hors-ligne', action='store_true')
    opts = args.parse_args()
    rows = json.loads(Path(opts.table).read_text())
    opts.cache.mkdir(parents=True, exist_ok=True)
    documents, failures, hashes = {}, [], {}
    for row in rows:
        url = row.get('url_texte', '')
        if urlparse(url).scheme != 'https' or urlparse(url).hostname != 'files.refdata.ch':
            failures.append(f"{row['id']} : URL officielle Refdata manquante")
            continue
        if url not in documents:
            path = opts.cache / (hashlib.sha256(url.encode()).hexdigest()[:16]+'.html')
            try:
                if not path.exists():
                    if opts.hors_ligne:
                        raise ValueError('document absent du cache')
                    with urlopen(url, timeout=30) as response:
                        if urlparse(response.url).hostname != 'files.refdata.ch':
                            raise ValueError('redirection hors Refdata')
                        path.write_bytes(response.read())
                raw = path.read_bytes()
                documents[url] = decode(raw.decode('utf-8-sig'))
                hashes[url] = hashlib.sha256(raw).hexdigest()
            except Exception as exc:
                failures.append(f"{row['id']} : {exc}")
                continue
        for line in missing_lines(row, documents[url]):
            failures.append(f"{row['id']} : ligne non retrouvée : {line}")
    (opts.cache/'empreintes.json').write_text(json.dumps(hashes, ensure_ascii=False, indent=1)+'\n')
    for failure in failures:
        print('ÉCHEC', failure)
    print(f'{len(rows)} lignes de doses, {len(documents)} documents, {len(failures)} écarts ; conformité des extraits seulement, aucune validation clinique.')
    return bool(failures)


if __name__ == '__main__':
    raise SystemExit(main())
