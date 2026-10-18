#!/usr/bin/env python3
"""Dimensionne les cibles à leur création, sans ajouter de règle au style hérité du corps."""
from pathlib import Path
import sys
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from _app import read,write
before=s=read()
css='.nr .glo{display:inline-flex;align-items:center;min-width:24px;min-height:24px}.nr .ti{width:24px;height:24px;min-width:24px;min-height:24px}'
s=s.replace(css+'\n','')
a="s.className='tw glo';s.dataset.t='glo|'+id;"
b="s.className='tw glo';if(p.closest('.nr'))s.style.cssText='display:inline-flex;align-items:center;min-width:24px;min-height:24px';s.dataset.t='glo|'+id;"
c='<button class="ti" aria-label="L’essentiel pour 100 % des points">'
d='<button class="ti" style="width:24px;height:24px;min-width:24px;min-height:24px" aria-label="L’essentiel pour 100 % des points">'
for old,new in [(a,b),(c,d)]:
 if new in s:continue
 if s.count(old)!=1:raise SystemExit('Ancre absente ou ambiguë : aucun fichier modifié.')
 s=s.replace(old,new)
if s==before:print('Correctif déjà appliqué.');raise SystemExit(0)
write(s);print('Notions : mêmes cibles de 24 px, dimensions portées par leurs éléments.')
