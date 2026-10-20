#!/usr/bin/env python3
"""Migration bornée et rejouable de TIP inline vers 248 sources JSON lisibles."""
import hashlib
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / 'tools'))
from _app import span
from tip_data import ASSET, TAG, SHARDS, build, compact, load, codes

# Tête du lot S1.5–S1.10 : deux URL primaires corrigées depuis l'audit initial.
# Les 3 472 textes et toutes les autres données sont identiques ; voir la preuve de reprise.
ORIGINAL_TIP_SHA256 = '2d9135a9340a942da3ebc24658cf0acd0aafb994426d56455c0b25c2bf1edc48'
ANCHOR = '<script>\nconst SSP='


def migrate(root=ROOT):
    root = Path(root)
    app_path = root / 'app_v2.html'
    app = app_path.read_text(encoding='utf-8')
    if TAG in app:
        load(root, app)
        print('TIP : déjà externalisé ; sources et asset conformes.')
        return
    if app.count(ANCHOR) != 1 or (root / ASSET).exists() or (root / SHARDS).exists():
        raise ValueError('Migration TIP : ancrage ambigu ou destination existante')
    a, b = span(app, 'TIP')
    literal = app[a:b]
    if hashlib.sha256(literal.encode()).hexdigest() != ORIGINAL_TIP_SHA256:
        raise ValueError('Migration TIP : contenu de départ inattendu')
    value = json.loads(literal)
    order = codes(app)
    if list(value) != order or len(order) != 248 or sum(len(x['c']) for x in value.values()) != 3472:
        raise ValueError('Migration TIP : catalogue ou 14 parties incohérents')
    if literal != compact(value):
        raise ValueError('Migration TIP : JSON initial non canonique')
    declaration = '\nconst TIP=' + literal + ';'
    if app.count(declaration) != 1 or app[b:b+1] != ';':
        raise ValueError('Migration TIP : déclaration ambiguë')
    after = app.replace(declaration, '', 1).replace(ANCHOR, TAG + '\n' + ANCHOR, 1)
    if after.replace(TAG + '\n', '', 1) != app.replace(declaration, '', 1):
        raise ValueError('Migration TIP : reconstruction HTML différente')
    directory = root / SHARDS
    directory.mkdir(parents=True)
    for code, item in value.items():
        (directory / (code + '.json')).write_text(json.dumps(item, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    size = build(root, app)
    asset = (root / ASSET).read_text(encoding='utf-8')
    if asset != '\nconst TIP=' + literal + ';\n':
        raise ValueError('Migration TIP : identité octet pour octet perdue')
    app_path.write_text(after, encoding='utf-8', newline='')
    if load(root, after) != value:
        raise ValueError('Migration TIP : identité sémantique perdue')
    print(f'TIP : {len(value)} SSP, 3472 parties ; asset {size} octets ; app -{len(declaration.encode())-len((TAG+chr(10)).encode())} octets.')


if __name__ == '__main__':
    migrate()
