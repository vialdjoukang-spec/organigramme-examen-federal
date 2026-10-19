#!/usr/bin/env python3
"""Appliquer le fond bleu ciel très pâle au thème clair, sans changer les blocs."""
import os
from pathlib import Path

def appliquer(css):
    ancres = [
        (':root{--bg:#fbfbf8;--paper:#ffffff;', ':root{--bg:#eaf7fd;--paper:#ffffff;'),
        (':root{--bg:#fbfbf8} ', ':root{--bg:#eaf7fd}'),
    ]
    for avant, _ in ancres:
        assert css.count(avant) == 1, 'Ancrage de fond unique attendu'
    for avant, apres in ancres:
        css = css.replace(avant, apres, 1)
    return css

if __name__ == '__main__':
    cible = Path(os.environ.get('STYLE_FILE', 'assets/style/app-2.css'))
    cible.write_text(appliquer(cible.read_text()))
