#!/usr/bin/env python3
"""Fermer une bulle ne doit pas ouvrir au survol la ligne qu'elle recouvrait."""
from pathlib import Path
import sys
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from _app import read,write
s=read()
a="if(e.target.closest('#tip .h button')){hideTip(true);return}"
b="if(e.target.closest('#tip .h button')){clearTimeout(tipT);hideTip(true);const under=document.elementFromPoint(e.clientX,e.clientY);tipSup=under&&under.closest('[data-t]')?under.closest('[data-t]').dataset.t:null;return}"
if b in s:print('Correctif déjà appliqué.');raise SystemExit(0)
if s.count(a)!=1:raise SystemExit('Ancre absente ou ambiguë : aucun fichier modifié.')
write(s.replace(a,b));print('Fermeture : survol du contenu découvert neutralisé jusqu’à la sortie du pointeur.')
