"""Source TIP par SSP et asset classique synchrone, avec contrôle strict de dérive.

Les fichiers data/tip/<code>.json sont la source éditable. L'asset est un produit
déterministe, obligatoire pour file:// et Pages ; les outils lisent le même corpus.
Les petites fixtures historiques avec TIP inline restent acceptées.
"""
import json
import re
from html.parser import HTMLParser
from pathlib import Path

try:
    from ._app import span
except ImportError:  # exécution directe de tools/*.py
    from _app import span

ASSET = 'assets/config/tip.js'
TAG = '<script src="' + ASSET + '"></script>'
SHARDS = 'data/tip'
MAX_ASSET_BYTES = 12 * 1024 * 1024


def compact(value):
    return json.dumps(value, ensure_ascii=False, separators=(',', ':'))


def from_js(text):
    try:
        a, b = span(text, 'TIP')
    except SystemExit as exc:
        raise ValueError('Asset TIP : déclaration absente ou ambiguë') from exc
    if text[:a] != '\nconst TIP=' or text[b:] != ';\n':
        raise ValueError('Asset TIP : déclaration unique attendue, sans autre code')
    value = json.loads(text[a:b])
    if not isinstance(value, dict):
        raise ValueError('TIP doit être un objet')
    return value


def render(value):
    return '\nconst TIP=' + compact(value) + ';\n'


def check_loading(app):
    """Valider les vrais scripts HTML, y compris pour une preuve historique Git."""
    class Scripts(HTMLParser):
        def __init__(self):
            super().__init__(); self.items = []; self.current = None

        def handle_starttag(self, tag, attrs):
            if tag == 'script':
                self.current = [attrs, '']; self.items.append(self.current)

        def handle_data(self, data):
            if self.current is not None:
                self.current[1] += data

        def handle_endtag(self, tag):
            if tag == 'script':
                self.current = None

    parser = Scripts(); parser.feed(app)
    tags = [i for i, (attrs, _) in enumerate(parser.items) if ('src', ASSET) in attrs]
    mains = [i for i, (_, body) in enumerate(parser.items) if body.startswith('\nconst SSP=')]
    if (app.count(TAG) != 1 or app.count(ASSET) != 1 or len(tags) != 1
            or parser.items[tags[0]][0] != [('src', ASSET)]):
        raise ValueError('Chargement TIP absent, asynchrone ou ambigu')
    if len(mains) != 1 or tags[0] >= mains[0]:
        raise ValueError('TIP doit être chargé avant le script principal')
    if any(re.search(r'\b(?:const|let|var)\s+TIP\s*[=;,]', body) for _, body in parser.items):
        raise ValueError('TIP déclaré deux fois : asset et HTML')


def codes(app):
    a, b = span(app, 'SSP')
    result = [row[0] for row in json.loads(app[a:b])]
    if len(result) != len(set(result)) or not result:
        raise ValueError('Catalogue SSP ambigu')
    return result


def shards(root, app):
    root = Path(root)
    order = codes(app)
    directory = root / SHARDS
    expected = {code + '.json' for code in order}
    found = {p.name for p in directory.glob('*.json')}
    if found != expected:
        raise ValueError(f'TIP : fichiers SSP manquants ou supplémentaires : {sorted(found ^ expected)}')
    out = {}
    for code in order:
        if not code.replace('.', '').isalnum() or '/' in code:
            raise ValueError('Code SSP non sûr : ' + code)
        value = json.loads((directory / (code + '.json')).read_text(encoding='utf-8'))
        if (not isinstance(value, dict) or not isinstance(value.get('c'), list)
                or len(value['c']) != 14 or not all(isinstance(part, str) for part in value['c'])):
            raise ValueError(code + ' : objet et 14 parties du cours attendus')
        out[code] = value
    return out


def load(root, app=None):
    root = Path(root)
    app = app if app is not None else (root / 'app_v2.html').read_text(encoding='utf-8')
    if ASSET not in app:
        a, b = span(app, 'TIP')
        return json.loads(app[a:b])
    check_loading(app)
    asset = (root / ASSET).read_text(encoding='utf-8')
    if len(asset.encode('utf-8')) > MAX_ASSET_BYTES:
        raise ValueError('Asset TIP au-delà de 12 Mio')
    value = shards(root, app)
    if asset != render(value):
        raise ValueError('TIP : divergence entre data/tip et asset JavaScript')
    return value


def build(root, app=None):
    root = Path(root)
    app = app if app is not None else (root / 'app_v2.html').read_text(encoding='utf-8')
    asset = render(shards(root, app))
    if len(asset.encode('utf-8')) > MAX_ASSET_BYTES:
        raise ValueError('Asset TIP au-delà de 12 Mio')
    (root / ASSET).write_text(asset, encoding='utf-8', newline='')
    return len(asset.encode('utf-8'))


if __name__ == '__main__':
    root = Path(__file__).resolve().parents[1]
    tip = load(root)
    print(f'TIP : {len(tip)} SSP, {sum(len(x["c"]) for x in tip.values())} parties, '
          f'{(root / ASSET).stat().st_size} octets d’asset identique aux sources.')
