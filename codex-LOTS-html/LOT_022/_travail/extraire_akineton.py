"""Extraction reproductible sans ajouter d'espaces entre les spans d'un mot."""
from html.parser import HTMLParser
from pathlib import Path
import gzip,hashlib,json
D=Path(__file__).resolve().parents[1]
p=D/'evidence/AKINETON_24035_officiel.html'
class P(HTMLParser):
 def __init__(self):super().__init__();self.t=[];self.skip=0
 def handle_starttag(self,t,a):
  if t in ('style','script'):self.skip+=1
 def handle_data(self,s):
  if not self.skip:self.t.append(s)
 def handle_endtag(self,t):
  if t in ('style','script'):self.skip-=1
  if t in ('p','div','br','li','h1','h2','h3'):self.t.append('\n')
s=P();s.feed(p.read_text());t='\n'.join(x.strip() for x in ''.join(s.t).splitlines() if x.strip())
p.with_suffix('.txt').write_text(t)
g=p.with_suffix('.txt.gz');g.write_bytes(gzip.compress(t.encode(),mtime=0))
(D/'evidence/AIPS_24035_officiel.json').write_text(json.dumps({'source':str(g.relative_to(D.parents[1])),'sha256':hashlib.sha256(g.read_bytes()).hexdigest(),'html_sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'url':'https://files.refdata.ch/simis-public-prod/MedicinalDocuments/ca5967db8afc43e59a26069f7ac30bea-fr.html','consultation':'2026-10-31','methode':'HTML officiel conservé ; texte des spans concaténé sans ajout artificiel d’espaces ; script extraire_akineton.py. Source commune inchangée.','rubriques':'Composition, indications, posologie, sécurité, interactions, grossesse/allaitement ; fiche mai 2022.'},ensure_ascii=False,indent=2)+'\n')
