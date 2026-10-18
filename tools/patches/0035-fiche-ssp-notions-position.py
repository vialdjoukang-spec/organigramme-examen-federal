#!/usr/bin/env python3
"""Même monographie SSP depuis Notions ; fenêtre visible après chargement différé."""
import sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from _app import read,write
s=before=read()
replacements=[
 ("if(b[0]==='c'){ti=CLIN[i];", "if(b[0]==='c'){const MO=sspMonoGet(a,key);if(MO)return {hd:'Monographie SSP · '+a,ti:s[1],h:MO.h,src:MO.s};ti=CLIN[i];"),
 ("let left=Math.min(Math.max(8,r.left+Math.min(60,r.width/4)),vw-w-8);", "top=Math.max(8,Math.min(top,vh-hh-8));let left=Math.min(Math.max(8,r.left+Math.min(60,r.width/4)),vw-w-8);")]
for old,new in replacements:
 if s.count(old)==1:s=s.replace(old,new)
 elif new not in s:raise SystemExit('Ancrage absent ou ambigu : '+old[:60])
if s!=before:write(s);print('Fiche SSP commune depuis Notions ; position verticale bornée à la fenêtre.')
else:print('Correctif déjà appliqué.')
