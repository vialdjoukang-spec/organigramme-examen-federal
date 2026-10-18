#!/usr/bin/env python3
"""Ordre de Vial : aucune infobulle au survol, ouverture par activation seulement."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from _app import read, write

s=before=read()
lines=s.splitlines(keepends=True)
prefixes=("const fine=matchMedia(", "document.addEventListener('mouseover',",
          "document.addEventListener('pointerdown',e=>{lpFired=",
          "['pointerup','pointercancel'].forEach(",
          "document.addEventListener('pointermove',e=>{if(lpXY",
          "document.addEventListener('contextmenu',e=>{if(lpFired",
          "TIPEL.addEventListener('pointerover',", "TIPEL.addEventListener('pointerout',",
          "TIPEL.addEventListener('focusin',")
s=''.join(line for line in lines if not line.startswith(prefixes)
          and not line.startswith('/* Appui long (tactile)'))
# Les gestes du calendrier n'ont plus de temporisateur d'infobulle à annuler.
s=s.replace('if(rz)clearTimeout(lpT);','').replace('clearTimeout(lpT);','')
s=s.replace('au survol, au clic ou au toucher','au clic ou au toucher')
s=s.replace('survolez ou touchez le pourcentage','cliquez ou touchez le pourcentage')
s=s.replace('bulle « n · nom » au survol, au focus et au toucher',
            'bulle « n · nom » après clic, toucher ou activation clavier')

def replace(old,new):
    global s
    if s.count(old)==1:
        s=s.replace(old,new)
    elif old in s or new not in s:
        raise SystemExit('Ancrage absent ou ambigu : '+old[:70])

replace("document.addEventListener('click',e=>{if(lpFired){lpFired=false;e.preventDefault();e.stopPropagation();return}",
        "document.addEventListener('click',e=>{")
replace("tipSup=null,lpT=null,lpFired=false,lpXY=null;const TIPEL=", "tipSup=null;const TIPEL=")
replace("if(inTip||inT){const d=gloShort(id);if(d)s.title=d}s.textContent=", "s.textContent=")
old='aria-haspopup="dialog"${ti?` title="${esc(ti)}"`:\'\'}>${esc(t)}</span>`}'
new='aria-haspopup="dialog">${esc(t)}</span>`}'
replace(old,new)
replace("(e.key==='Enter'||e.key===' ')&&t.classList.contains('tw')",
        "(e.key==='Enter'||e.key===' ')&&t.matches('.tw,.pv[data-t][role=\"button\"]')")

if s!=before:
    write(s)
    print('Infobulles : clic, toucher et clavier ; aucun survol ni appui long automatique.')
else:print('Correctif déjà appliqué.')
