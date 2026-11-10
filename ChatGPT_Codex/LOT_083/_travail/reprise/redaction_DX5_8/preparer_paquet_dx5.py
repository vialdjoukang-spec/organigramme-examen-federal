from pathlib import Path
import json,hashlib
B=Path(__file__).parent;R=B.parent;rows=[]
def add(id,t,a,b,fn,title,url):
 start=t.index(a) if a else 0;end=t.index(b,start) if b else len(t);s=t[start:end].strip();start=t.index(s,start)
 rows.append(dict(id=id,source=title,url=url,date='2026-11-10',texte=s,archive=str(fn),offset_debut=start,offset_fin=start+len(s),sha256=hashlib.sha256(s.encode()).hexdigest()))
f=R/'sources/source_04.txt';t=f.read_text();print(t[:800])
# Source OFSP intégralement lue ; paragraphes séparés pour garder la traçabilité clinique.
for k,s in enumerate(t.split('\n\n')):
 if len(s)>110:add(f'flu-ofsp-{k}',t,s,None if s==t else s+'\0',f,'OFSP — Grippe saisonnière, page courante consultée 2026','https://www.bag.admin.ch/fr/grippe-saisonniere-influenza') if False else None
# Enregistrement exact de la page pour découpage par paragraphes.
pos=0
for k,s in enumerate(t.split('\n\n')):
 if len(s)>110:
  rows.append(dict(id=f'flu-ofsp-{k}',source='OFSP — Grippe saisonnière, page courante ; année de publication non indiquée',url='https://www.bag.admin.ch/fr/grippe-saisonniere-influenza',date='2026-11-10',texte=s,archive=str(f),offset_debut=pos,offset_fin=pos+len(s),sha256=hashlib.sha256(s.encode()).hexdigest()))
 pos+=len(s)+2
for med,stamp in [('tamiflu','janvier 2026 ; autorisations 55196/56176'),('xofluza','juillet 2026 ; autorisations 67426/68068')]:
 f=B/f'AIPS_{med}_texte.json';d=json.loads(f.read_text())
 for n in [2,3,4,5,6,7,8,16,19]:
  s=d['sections'][n];v=s['texte'];v=v.split('Remarques concernant la manipulation')[0].strip() if n==19 else v
  rows.append(dict(id=f'flu-aips-{med}-{n}',source=f'AIPS Swissmedic {med} — {stamp} — '+s['titre'],url=d['url_api'],date='2026-11-10',texte=v,archive=str(f),section=n,sha256=hashlib.sha256(v.encode()).hexdigest()))
 s=d['sections'][12]['texte'];v=s[:s.index('Pharmacodynamique')]
 rows.append(dict(id=f'flu-aips-{med}-mecanisme',source=f'AIPS Swissmedic {med} — {stamp} — mécanisme',url=d['url_api'],date='2026-11-10',texte=v,archive=str(f),section=12,offset_debut=0,offset_fin=len(v),sha256=hashlib.sha256(v.encode()).hexdigest()))
f=B/'SOURCES_SSI2026_COMPLEMENT_0.txt';t=f.read_text();u='https://ssi.guidelines.ch/guideline/5082/en';title='SSI — Acute respiratory infection and/or influenza-like illness in adults — validation 01.09.2026'
for id,a,b in [('definition','## Definition and disease spectrum','## Severity'),('alarmes','## Severity criteria','## Tests'),('tests','## Tests','## Treatment'),('symptomatique','### **Symptomatic treatment**','### **Empirical antibiotics**'),('antibiotiques-non','Antibiotic therapy is not recommended','### **Influenza'),('decision-antiviraux','Expert opinion from the SSI','## Prevention'),('vaccins','## Prevention','### **Prevention/Chemoprophylaxis**')]:add('flu-ssi-'+id,t,a,b,f,title,u)
f=B/'SOURCES_FLU_COMPLEMENT_1.txt';t=f.read_text();add('flu-hoch2026',t,None,None,f,'HOCH — Influenza — validation 15 janvier 2026','https://ssi.guidelines.ch/guideline/1727')
f=B/'SOURCES_FLU_COMPLEMENT_2.txt';t=f.read_text();u='https://www.bmj.com/content/392/bmj-2025-087397';title='BMJ 2026 — résumé recommandations OMS du 12 septembre 2024'
for id,a,b in [('cadre','This guideline applies to adults','### How to identify'),('diagnostic','* _For adjunctive therapies_','The full guideline provides complete'),('principes','**Recommendations** apply','**The evidence**')]:add('flu-oms-'+id,t,a,b,f,title,u)
f=B/'SOURCES_FLU_COMPLEMENT_0.txt';t=f.read_text();u='https://www.hug.ch/sites/interhug/files/structures/maladies_infectieuses/documents/S%C3%A9minaire%20infectio/03_la_grippe_dre_vetter_05.12.2024.pdf';title='HUG Pauline Vetter — La grippe : comment utiliser les antiviraux ? — 05.12.2024'
for id,a,b in [('virus','# Le(s) virus de la grippe','# Options disponibles'),('resistance','# Grippe, antiviraux et résistance','# 12 Septembre'),('non-severe','# Nouvelles recommandations','# Traitement de première'),('tester','# Tester avant de traiter','# Recommandations pour les patients')]:add('flu-hug-'+id,t,a,b,f,title,u)
D=B/'DX.5';(D/'paquet.json').write_text(json.dumps({'LOT':'083','DX':5,'entite':'Grippe saisonnière','passages':rows},ensure_ascii=False,indent=2))
print(len(rows),'passages');print([(x['id'],x['texte'][:90]) for x in rows if x['id'].startswith('flu-ofsp')])
