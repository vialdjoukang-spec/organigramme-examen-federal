#!/usr/bin/env python3
"""Initialise le lot G5 sans inventer de chiffre ; ne remplace aucun lot existant."""
import json
from pathlib import Path
import sys
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from _app import read,span
s=read();a,b=span(s,'NOT');notions=json.loads(s[a:b])
p=Path('data/ck/prev.json');d=json.loads(p.read_text())
for c in ['S7.5','S2.6','S5.2']:
 if c not in d:
  d[c]={'cadre':'Médecine de premier recours ou urgences, Suisse ou Europe : cadre et chiffres à établir par diagnostic.','items':[{'i':i,'nom':n,'prev_pct':None,'statut':'À vérifier','rang':i+1,'note':'Aucun chiffre de source adapté à ce libellé précis n’a encore été validé.'} for i,n in enumerate(notions[c][0])]}
p.write_text(json.dumps(d,ensure_ascii=False,indent=1)+'\n')
