#!/usr/bin/env python3
"""Conserve le bloc de texte anonyme quand le glossaire le lie dans une grille ou un flex."""
from pathlib import Path
import sys
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from _app import read,write
s=read()
a='if(k){f.append(txt.slice(at));t.replaceWith(f);n+=k}'
b="if(k){f.append(txt.slice(at));if(['grid','inline-grid','flex','inline-flex'].includes(getComputedStyle(p).display)){const flow=document.createElement('span');flow.append(f);t.replaceWith(flow)}else t.replaceWith(f);n+=k}"
if b in s:print('Correctif déjà appliqué.');raise SystemExit(0)
if s.count(a)!=1:raise SystemExit('Ancre absente ou ambiguë : aucun fichier modifié.')
write(s.replace(a,b));print('Glossaire : texte lié conservé dans un seul élément de grille ou de flex.')
