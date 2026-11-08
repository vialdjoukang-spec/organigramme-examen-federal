"""Vérification portable locale, sans réseau ni dépendance externe."""
import re,json,hashlib
from pathlib import Path
P=Path(__file__).resolve().parent
for l in (P/'MANIFESTE_SHA256.txt').read_text().splitlines():
 s,n=l.split('  ',1);assert hashlib.sha256((P/n).read_bytes()).hexdigest()==s,n
m=(P/'NEO_REFERENTIEL_SUISSE_2026.md').read_text();j=json.loads((P/'NEO_REFERENTIEL_SUISSE_2026_LIENS.json').read_text())
defs=dict(re.findall(r'^\[(R\d{3})\]: <([^>]+)>$',m,re.M))
assert len(defs)==238
assert all(a['uri'] in defs.values() for a in j['annotations'])
assert len(j['annotations'])==458
assert all(u in m for u in j['displayed_urls'])
content=m.split('\n## 5. Cibles exactes des liens (références Markdown)\n\n',1)[0]
it=iter(j['markdown_compaction']['occurrences']);seen=[]
def restore(z):
 a=next(it);assert z[1]==a['label'] and z[2]==a['reference'];assert defs[z[2]]==a['target'];seen.append(a);return a['original_syntax']
expanded=re.sub(r'\[((?:\\.|[^\]])*)\]\[(R\d{3})\]',restore,content)
assert not list(it) and len(seen)==497
assert hashlib.sha256(expanded.encode()).hexdigest()==j['markdown_compaction']['expanded_sha256']
assert hashlib.sha256(m.encode()).hexdigest()==j['markdown_compaction']['compact_sha256']
assert len(re.findall(r'^\| \d+ \|',m,re.M))==45
assert all('### 2.'+str(i)+' ' in m for i in range(1,6))
citations=re.findall(r'^(\d+)\. (.*?) — \[URL\]\[(R\d{3})\]$',m,re.M)
assert len(citations)==52
for (n,t,r),c in zip(citations,j['citations']):assert int(n)==c['n'] and t==c['title'] and defs[r]==c['url']
print('PAQUET OK : SHA, 458 annotations, 84 URLs affichées, 497 liens/238 références, 45 spécialités, 52 citations, aller-retour exact. NON VALIDE METIER.')
