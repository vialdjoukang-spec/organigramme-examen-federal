#!/usr/bin/env python3
"""Audit indépendant source, lecture seule. Usage: python audit_source.py SOURCE.pdf ; PyMuPDF requis."""
from pathlib import Path
import sys
import pymupdf,json,re,hashlib
P=Path(__file__).resolve().parent;S=Path(sys.argv[1]);D=pymupdf.open(S)
coverage=json.loads((P/'COUVERTURE.json').read_text());assert hashlib.sha256(S.read_bytes()).hexdigest()==coverage['source_sha256']
N=lambda s:re.sub(r'\s+',' ',s).strip();rows=[];groups=[];issues=[]
for pn,p in enumerate(D,1):
 t=p.find_tables().tables[0];xleft=(t.rows[0].cells[0][0]+t.rows[0].cells[0][2])/2
 lines=[ln for b in p.get_text('rawdict')['blocks'] if 'lines' in b for ln in b['lines']]
 chars=[c for ln in lines for sp in ln['spans'] for c in sp['chars']]
 def text(rect):
  r=pymupdf.Rect(rect);return N(' '.join(''.join(c['c'] for sp in ln['spans'] for c in sp['chars'] if pymupdf.Point((c['bbox'][0]+c['bbox'][2])/2,(c['bbox'][1]+c['bbox'][3])/2) in r) for ln in lines))
 # Merged-cell bounds are actual horizontal strokes crossing the NUMBER-column centre.
 # No forward fill of arbitrary names; no reliance on detected fake split cells there.
 bounds=[]
 for d in p.get_drawings():
  if d['type'] not in ('s','fs'):continue
  for it in d['items']:
   if it[0]=='l':
    a,b=it[1:3]
    if abs(a.y-b.y)<.05 and min(a.x,b.x)<xleft<max(a.x,b.x):bounds.append(round(a.y,3))
 bounds=sorted(set(bounds))
 for top,bottom in zip(bounds,bounds[1:]):
  if top<t.rows[0].bbox[3]-.1:continue
  n=text((t.bbox[0],top,t.rows[0].cells[0][2],bottom))
  if not n.isdigit():raise ValueError((pn,top,bottom,n))
  name=text((t.rows[0].cells[1][0],top,t.rows[0].cells[1][2],bottom))
  g=dict(n=int(n),name=name,page=pn,bounds=[top,bottom],rows=[])
  for ri,r in enumerate(t.rows[1:],1):
   c=pymupdf.Rect(r.cells[2]);cy=(c.y0+c.y1)/2
   if top<cy<bottom:
    item=dict(id=f'{int(n):02d}.{len(g["rows"])+1}',n=int(n),specialite=name,page=pn,row=ri,discipline=text(c),source=text(r.cells[3]),discipline_rect=list(c),source_rect=list(r.cells[3]),group_bounds=[top,bottom])
    rows.append(item);g['rows'].append(item['id'])
  groups.append(g)
assert len(rows)==137 and [g['n'] for g in groups]==list(range(1,46))
prod=coverage['couverture']
for a,b in zip(rows,prod):
 for k in ['id','n','specialite','page','row','discipline','source']:
  if a[k]!=b[k]:issues.append(dict(id=a['id'],key=k,independent=a[k],package=b[k]))
 assert hashlib.sha256(a['source'].encode()).hexdigest()==b['source_sha256']
alltext='\n'.join(p.get_text() for p in D)
links=[l for p in D for l in p.get_links()]
uris=[i for i in range(1,D.xref_length()) if '/URI' in D.xref_object(i)]
urls=re.findall(r'(?:https?://|mailto:|cid:)\S+',alltext)
domains=set(re.findall(r'(?<![\w@/])(?:[A-Za-z0-9-]+\.)+[A-Za-z]{2,}(?!\w)',alltext))
assert not issues and not links and not uris and not urls and domains=={'siwf.ch'}
assert D.embfile_count()==0
assert [(g['n'],g['name'],g['rows']) for g in groups]==[(g['n'],g['name'],g['rows']) for g in coverage['groups']]
assert hashlib.sha256(S.read_bytes()).hexdigest()==coverage['source_sha256']
print(json.dumps(dict(verdict='CONFORME_DOCUMENTAIRE_GEOMETRIQUE_NON_METIER',pages=len(D),specialites=len(groups),pairs=len(rows),mapping_differences=issues,link_annotations=len(links),uri_objects=len(uris),explicit_urls=urls,domains=sorted(domains),source_sha256=coverage['source_sha256']),ensure_ascii=False,indent=2))
