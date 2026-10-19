#!/usr/bin/env python3
"""Supprimer le blanc entre un sous-titre d’infobulle et sa liste, sans rapprocher les parties."""
import os
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from _app import read, write

path = os.environ.get('APP_FILE')
text = read(path) if path else read()
rule = '#tip .ck-b b+:is(ul,ol){margin-block-start:0}'
if rule not in text:
    # Le patch ordinal peut déjà précéder :root dans le premier style de head.
    start = text.index('<style>') + len('<style>')
    assert start < text.index('</head>'), 'Style de head introuvable'
    text = text[:start] + rule + '\n' + text[start:]
else:
    assert text.count(rule) == 1 and text.index(rule) < text.index('</head>')
write(text, path) if path else write(text)
print('Espaces sous-titre → liste supprimés ; séparation entre parties conservée. Script gratuit et rejouable.')
