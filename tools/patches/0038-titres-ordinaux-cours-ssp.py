#!/usr/bin/env python3
"""Numéroter les 14 rubriques du cours, sans changer leurs clés mémorisées."""
import json
import os
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from _app import read, write, span

path = os.environ.get('APP_FILE')
s = read(path) if path else read()
a, b = span(s, 'CLIN')
old = s[a:b]
suffix = ".map((t,i)=>(i+1)+'- '+t+' :')"
# span délimite le tableau JSON avant le .map : ne pas doubler le suffixe.
if not s[b:].startswith(suffix):
    titles = json.loads(old)
    assert len(titles) == 14 and all(isinstance(t, str) for t in titles)
    assert not any(t[:1].isdigit() for t in titles), 'Titres déjà numérotés autrement'
    anchor = 'const CLIN=' + old + ';'
    assert s.count(anchor) == 1, 'Ancrage CLIN absent ou ambigu'
    s = s.replace(anchor, 'const CLIN=' + old + suffix + ';', 1)

anchor = '.nr.ok{background:'
rule = '.nr[data-k^="c"] .tw{font-weight:700}'
if rule not in s:
    assert s.count(anchor) == 1, 'Ancrage CSS absent ou ambigu'
    s = s.replace(anchor, rule + '\n' + anchor, 1)
else:
    assert s.count(rule) == 1

if path:
    write(s, path)
else:
    write(s)
print('Titres du cours 1–14 numérotés et en gras ; clés et différentiels conservés.')
