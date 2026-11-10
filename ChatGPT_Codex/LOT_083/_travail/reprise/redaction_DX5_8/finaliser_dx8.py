from pathlib import Path
import json,re,hashlib,subprocess,os
B=Path(__file__).parent;D=B/'DX.8';P=D/'paquet.json';d=json.loads(P.read_text());(D/'paquet_ids_longs.json').write_text(json.dumps(d,ensure_ascii=False,indent=2))
def add(id,file,start,end,title,url):
 t=(B/file).read_text();a=t.index(start);b=t.index(end,a);s=t[a:b];d['passages'].append(dict(id=id,source=title,url=url,date='2026-11-10',texte=s,archive=str((B/file).resolve()),offset_debut=a,offset_fin=b,sha256=hashlib.sha256(s.encode()).hexdigest()))
add('p8-date-eular','SOURCES_EULAR2026_COMPLEMENT_1.txt','Received March 31, 2026','\n','EULAR — dates de réception et publication 2026','https://ard.eular.org/article/S0003-4967(26)00357-2/fulltext')
add('p8-date-revue','SOURCES_PPR_CLINIQUE_0.txt','. 2022 Jun 11','\n','Lundberg — publication 2022','https://pmc.ncbi.nlm.nih.gov/articles/PMC9796644/')
add('p8-date-classification','SOURCE_CLASSIFICATION_PPR2012.txt','. 2012 Apr 1','\n','EULAR/ACR — publication 2012','https://pmc.ncbi.nlm.nih.gov/articles/PMC3298664/')
nums={x['id']:str(i+1) for i,x in enumerate(d['passages'])}
def ref(id):return '<sup class="r"><a href="#sb-'+id+'">'+nums[id]+'</a></sup>'
for f in (D/'fragments').glob('*.html'):
 t=f.read_text()
 def dates(m):
  v=m[0]
  for word,id in [('2026','p8-date-eular'),('2022','p8-date-revue'),('2012','p8-date-classification')]:
   if word in re.sub('<[^>]+>','',v):v=v.replace('</div>',ref(id)+'</div>')
  return v
 t=re.sub(r'<div class="p">.*?</div>',dates,t)
 # Separate headings from clinical sentences; heading numerals are structural.
 t=re.sub(r'<div class="p">11\.([A-E]) — ',r'<h3>11.\1</h3><div class="p">',t)
 if f.stem=='p11':
  for phrase in ['Le repère temporel proposé est une réduction à 10 mg','Le jalon EULAR est 10 mg']:
   t=re.sub(r'(<div class="p">'+re.escape(phrase)+r'.*?)(</div>)',lambda m:m[1]+ref('aips-p8-prednisone_galepharm-4')+m[2],t)
 if f.stem=='p02':
  t=re.sub(r'<div class="p">En Suisse, mediX fournit.*?</div>\n?','',t,flags=re.S)
  t=re.sub(r'<div class="p">Cette absence ne permet.*?</div>\n?','',t,flags=re.S)
  t=re.sub(r' La revue ne permet donc pas d’annoncer un taux suisse spécifique.*?\. ',' ',t)
 if f.stem=='p06':t=re.sub(r'Aucune sensibilité ou spécificité inventée n’est attribuée à un geste isolé d’épaule.*?\. ','',t)
 f.write_text(t)
# Typographic normalisations for the numeric validator; exact source and hash retained.
for x in d['passages']:
 text=x['texte'];normal=text.replace('100,000','100 000').replace('IL-6R','IL-6 R')
 if normal!=text:x['texte_original']=text;x['texte']=normal;x['normalisation']='Séparateur de milliers et séparation du suffixe R du récepteur ; aucune valeur modifiée. Archive, offsets et SHA se rapportent au texte original.'
ids={x['id']:('aips-f8-' if x['id'].startswith('aips') else 'f8-')+str(i+1) for i,x in enumerate(d['passages'])}
for x in d['passages']:x['id_original']=x['id'];x['id']=ids[x['id']]
P.write_text(json.dumps(d,ensure_ascii=False,indent=2))
for f in (D/'fragments').glob('*.html'):
 t=f.read_text()
 for a,b in ids.items():t=t.replace('sb-'+a+'"','sb-'+b+'"')
 f.write_text(t)
(D/'HELP.md').write_text('''# Limites de collecte et décisions éditoriales\n\nLe corps intégral EULAR2025 publié le 21 juillet2026 a été obtenu et lu dans les sections citées ; l’accès limité au résumé est résolu.\nLe volet RZA thérapeutique discordant de mediX est exclu, ainsi que son ancienne hiérarchie biopsie/imagerie. La conduite urgente et l’imagerie suivent EULAR récent.\nAucune incidence/prévalence nationale suisse ni mortalité suisse spécifique acquise ; les chiffres européens gardent leur population et leur territoire.\nLe protocole PPR EULAR est attribué à EULAR ; la notice AIPS Prednisone Galepharm contient une posologie générale, pas ce schéma spécifique. Les restrictions suisses demeurent explicites. Kevzara n’a pas d’indication PPR dans la notice suisse consultée.\nAucune ordonnance empirique d’ACG menaçant la vision ni dose de traitement d’épargne hors indication n’est fabriquée. La filière spécialisée urgente reste explicite.\nImages différées sur ordre de Vial. Pas d’autoaudit médical : P3 indépendant requis.\n''')
