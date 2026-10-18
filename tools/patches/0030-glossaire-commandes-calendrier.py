#!/usr/bin/env python3
"""Ne pas imbriquer un bouton de glossaire dans les commandes du calendrier."""
from pathlib import Path
import sys
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from _app import read,write
s=read();a='nav,.tw,[contenteditable],[data-noglo],.blk,#grid,.ck-ctl,.ck-fil';b='nav,.tw,.it,.grp-h,[contenteditable],[data-noglo],.blk,#grid,.ck-ctl,.ck-fil'
if b in s:print('Correctif déjà appliqué.');raise SystemExit(0)
if s.count(a)!=1:raise SystemExit('Ancre absente ou ambiguë : aucun fichier modifié.')
write(s.replace(a,b));print('Calendrier : commandes laissées à leur action de sélection ou de repli ; aucun lien imbriqué.')
