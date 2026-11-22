#!/usr/bin/env python3
"""Contrôle portable en lecture seule. Python 3 stdlib ; aucune requête réseau."""
from pathlib import Path
import re,json,hashlib
P=Path(__file__).resolve().parent;H=lambda b:hashlib.sha256(b).hexdigest()
for line in (P/'MANIFESTE_SHA256.txt').read_text().splitlines():
 h,name=line.split('  ',1);assert H((P/name).read_bytes())==h,('manifest',name)
j=json.loads((P/'COUVERTURE.json').read_text());m=(P/'NEO_DISCIPLINES_ALLIEES_SUISSE.md').read_text();assert H(m.encode())==j['markdown_sha256']
groups=[];rows=[];cur=None
for line in m.splitlines():
 h=re.match(r'^### (\d{2})\. (.*)$',line)
 if h:cur=(int(h[1]),h[2]);groups.append(cur)
 r=re.match(r'^- \*\*(.*?)\*\* — (.*)$',line)
 if r:rows.append((*cur,r[1],r[2]))
assert groups==[(g['n'],g['name']) for g in j['groups']]
assert len(groups)==45 and len(rows)==len(j['couverture'])==137
for out,r in zip(rows,j['couverture']):
 assert out==(r['n'],r['specialite'],r['discipline'],r['sortie']),r['id']
 assert H(r['source'].encode())==r['source_sha256'] and H(r['sortie'].encode())==r['sortie_sha256']
 # Reconstruct changed text from exact source ranges and replacement fragments.
 chunks=[];end=0
 for c in r['transformations']:
  a,b=c['source_offsets'];assert a>=end and r['source'][a:b]==c['avant'];chunks.extend([r['source'][end:a],c['apres']]);end=b
 chunks.append(r['source'][end:]);assert ''.join(chunks)==r['sortie']
 for name,patt in [('nombres',r'\d+(?:[.,]\d+)?'),('comparateurs',r'[<>≤≥]'),('grades_romains',r'\b[IVX]{1,5}\b'),('negations',r'\b(?:sans|non)\b')]:
  assert re.findall(patt,r['source'])==re.findall(patt,r['sortie']),r['id']
  assert r['controles'][name]['source']==re.findall(patt,r['source'])
  assert r['controles'][name]['sortie']==re.findall(patt,r['sortie'])
assert 'siwf.ch' in m and not re.search(r'https?://|mailto:|cid:',m)
assert 'non validés cliniquement ni juridiquement' in m
assert sum(len(r['discipline'].encode())+len(r['source'].encode()) for r in j['couverture'])==j['metrics']['source_body_bytes']
assert sum(len(r['discipline'].encode())+len(r['sortie'].encode()) for r in j['couverture'])==j['metrics']['v5_body_bytes']
print('PAQUET OK : manifeste, 45 spécialités, 137 couples, mapping réversible, nombres/comparateurs/grades/négations. NON VALIDE CLINIQUEMENT/JURIDIQUEMENT.')
