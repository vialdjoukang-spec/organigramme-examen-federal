#!/usr/bin/env python3
"""Rétablit uniquement la balise ouvrante de l'alerte des DD (rejouable)."""
import json
from pathlib import Path
import sys
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from _app import read,span,write
s=read();a,b=span(s,'TIP');tip=json.loads(s[a:b]);count=0
for bloc in tip.values():
 for i,text in enumerate(bloc.get('d',[])):
  if text.startswith('À ne pas manquer.</b>'):
   bloc['d'][i]='<b style="color:var(--bad)">'+text;count+=1
out=s[:a]+json.dumps(tip,ensure_ascii=False,separators=(',',':'))+s[b:] if count else s
out=out.replace('#tip .mono-r{color:#b3261e}', '#tip .mono-r{color:var(--bad)}')
if out!=s:write(out)
print(f'{count} balises ouvrantes restaurées ; aucun texte clinique réécrit.')
