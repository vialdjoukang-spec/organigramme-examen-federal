from pathlib import Path
import json,hashlib
B=Path(__file__).parent;R=B.parent;rows=[]
def add(id,f,a,b,title,url):
 t=f.read_text();x=t.index(a);z=t.index(b,x) if b else len(t);s=t[x:z].strip();rows.append(dict(id=id,source=title,url=url,date='2026-11-10',texte=s,archive=str(f),offset_debut=x,offset_fin=x+len(s),sha256=hashlib.sha256(s.encode()).hexdigest()))
f=B/'SOURCES_PPR_CLINIQUE_0.txt';u='https://pmc.ncbi.nlm.nih.gov/articles/PMC9796644/';title='Lundberg, Sharma, Turesson, Mohammad — An update on polymyalgia rheumatica — J Intern Med 2022'
for id,a,b in [('epi','## Epidemiology','### Fig. 1.'),('mecanisme','## Pathogenesis and pathophysiology','### Fig. 2.'),('cellules','Perturbations of circulating T','## Clinical presentation'),('clinique','## Clinical presentation','## Association'),('acg','## Association with temporal','## Diagnostic and classification'),('diagnostic','## Diagnosis','## Imaging studies'),('imagerie','## Imaging studies','### Fig. 3.'),('radio','### Other imaging studies','## Laboratory'),('bio','## Laboratory findings','## Differential'),('dd-pr','### Rheumatoid arthritis','### Myositis'),('dd-myosite','### Myositis','### Pain syndromes'),('dd-fibro','### Pain syndromes','### Malignancy'),('dd-cancer','### Malignancy','### Others'),('dd-autres','### Others','## PMR as an'),('mortalite','## Mortality','## Conclusion')]:add('p8-'+id,f,a,b,title,u)
f=R/'sources/source_08.txt';u='https://www.medix.ch/wissen/guidelines/kurzversion/bewegungsapparat/polymyalgia-rheumatica-riesenzellarteriitis/';title='mediX Suisse — version septembre 2024'
for id,a,b in [('ch-date','**Erstellt von:','* [Vollversion]'),('ch-clinique','### Polymyalgia rheumatica','Diagnostik'),('ch-bilan','**Labor**','Überweisung an Rheumatologen'),('ch-orientation','Überweisung an Rheumatologen','Therapie'),('ch-prevention','Begleittherapie','Kontrollen'),('ch-suivi','Kontrollen','### Riesenzellarteriitis'),('ch-acg','### Riesenzellarteriitis','Ausserdem')]:add('p8-'+id,f,a,b,title,u)
f=R/'sources/source_01.txt';u='https://register.awmf.org/assets/guidelines/030-051l_S1_Diagnostik-Differentialdiagnose-Myalgien_2025-04.pdf';title='DGN — Diagnostik und Differenzialdiagnose bei Myalgien — 2025'
add('p8-dgn-clinique',f,'### **3\\.2.7** **Polymyalgia rheumatica**','Bisher existieren',title,u)
add('p8-dgn-ck',f,'Laborchemisch fehlen spezifische Veränderungen.','Myalgien – Leitlinien',title,u)
f=B/'SOURCE_CLASSIFICATION_PPR2012.txt';u='https://pmc.ncbi.nlm.nih.gov/articles/PMC3298664/';title='Dasgupta et al. — EULAR/ACR classification criteria — 2012'
add('p8-classification',f,'The objective of this study was','\n\n',title,u)
# Tables et texte entier du score, repérables dans le cache ; lecture ciblée à compléter avant citations des détails échographiques.
f=B/'SOURCES_EULAR2026_COMPLEMENT_1.txt';u='https://ard.eular.org/article/S0003-4967(26)00357-2/fulltext';title='EULAR recommandations 2025 — publication 21 juillet 2026'
for n in [1,2,3,6,9,10,12]:
 a='#### Recommendation '+str(n)+'\n';t=f.read_text();x=t.index(a);z=t.index('\n\n',t.index('**',x)+2)+2
 # heading and complete bold recommendation
 start=t.index('**',x);end=t.index('**',start+2)+2
 add('p8-eular-r'+str(n),f,t[start:end],t[end:end+15],title,u)
for id,a,b in [('eular-remission','After confirming the diagnosis of PMR','  [38'),('eular-taper','Patients with persistent or recurring symptoms','\n\n#### Recommendation 4'),('eular-il6-ch','This recommendation is based on available evidence','Sarilumab 200 mg'),('eular-rechute','We recommend that the diagnosis of relapse in PMR','#### Recommendation 10'),('eular-no-test','Therapy with oral GC remains the mainstay','  [35')]:add('p8-'+id,f,a,b,title,u)
for x in json.loads((B/'EXTRAITS_PA_EULAR.json').read_text())['passages']:
 y=dict(x);y['source']='EULAR — '+x['annee'];y['date']=y.pop('date_consultation');rows.append(y)
for med,stamp in [('prednisone_galepharm','Prednisone Galepharm — mars2026 ; autorisation69640'),('kevzara','Kevzara — juillet2025 ; autorisations66424/66425')]:
 f=B/f'AIPS_{med}_texte.json';d=json.loads(f.read_text())
 for n in [2,3,4,5,6,7,8,12,16,19]:
  s=d['sections'][n];v=s['texte'];rows.append(dict(id=f'aips-p8-{med}-{n}',source='AIPS Swissmedic — '+stamp+' — '+s['titre'],url=d['url_api'],date='2026-11-10',texte=v,archive=str(f),section=n,sha256=hashlib.sha256(v.encode()).hexdigest()))
D=B/'DX.8';(D/'paquet.json').write_text(json.dumps({'LOT':'083','DX':8,'entite':'Pseudopolyarthrite rhizomélique','passages':rows},ensure_ascii=False,indent=2));print(len(rows),'passages')
