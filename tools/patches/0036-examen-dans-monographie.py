#!/usr/bin/env python3
"""Conserver les régions et renvois de l'examen dans la rubrique clinique du SSP."""
import sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from _app import read,write
s=before=read()
old="if(MO)return {hd:'Monographie SSP · '+a,ti:s[1],h:MO.h,src:MO.s};ti=CLIN[i];"
new="if(MO){const exam=i===5?exFmt(T.c[i]).replace(/<\\/?(?:b|strong)\\b[^>]*>/gi,''):'';return {hd:'Monographie SSP · '+a,ti:s[1],h:exam?MO.h.replace('<b>5. Sémiologie aux explorations</b>','<br><b>Examen physique par région :</b>'+exam+'<br><b>5. Sémiologie aux explorations</b>'):MO.h,src:exam?MO.s+' · Examen physique : '+T.s:MO.s}}ti=CLIN[i];"
if s.count(old)==1:s=s.replace(old,new)
elif new not in s:raise SystemExit('Ancrage absent ou ambigu')
if s!=before:write(s);print('Examen régional et renvois conservés dans la rubrique 4.')
else:print('Correctif déjà appliqué.')
