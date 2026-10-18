#!/usr/bin/env python3
"""Garantit la taille des cibles des liens de glossaire et boutons d'information des notions."""
from pathlib import Path
import sys
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from _app import read,write
s=read();css='.nr .glo{display:inline-flex;align-items:center;min-width:24px;min-height:24px}.nr .ti{width:24px;height:24px;min-width:24px;min-height:24px}'
if css in s:print('Correctif déjà appliqué.');raise SystemExit(0)
anchor='.ti:hover,.ti:focus-visible{'
if s.count(anchor)!=1:raise SystemExit('Ancre absente ou ambiguë : aucun fichier modifié.')
write(s.replace(anchor,css+'\n'+anchor));print('Notions : cibles de glossaire et d’information au minimum à 24 px.')
