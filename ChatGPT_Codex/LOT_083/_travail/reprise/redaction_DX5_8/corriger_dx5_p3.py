from pathlib import Path
import json,re,hashlib,difflib,shutil
B=Path(__file__).resolve().parent;D=B/'DX.5';F=D/'fragments';BK=D/'avant_correction_P3';BK.mkdir(exist_ok=True)
for f in list(F.glob('*.html'))+[D/'paquet.json',D/'LOT_083_Phase_B_V0_DX.5.html']:
 if not (BK/f.name).exists():shutil.copyfile(f,BK/f.name)
pk=json.loads((D/'paquet.json').read_text())
def source(id,file,title,url,start,end):
 t=(B/file).read_text();a=t.index(start);b=t.index(end,a);s=t[a:b]
 pk['passages'].append(dict(id=id,source=title,url=url,date='2026-11-10',texte=s,archive=str(B/file),offset_debut=a,offset_fin=b,sha256=hashlib.sha256(s.encode()).hexdigest()))
source('f5-c1','DX5_CORRECTION_SOURCES_SEMIO_0.txt','UMVF/UNESS — Appareil respiratoire, 25 novembre 2013','https://archives.uness.fr/sites/campus-unf3s-2014/semiologie/enseignement/esemio9/site/html/cours.pdf','## **6\\. Auscultation**','### **6\\.1. Bruits normaux**')
source('f5-c2','DX5_CORRECTION_SOURCES_SEMIO_2.txt','Jordan, RMS des étudiants — Examen pulmonaire, 3 mai 2021','https://www.rmsetudiants.ch/content/download/976/9550','**On ausculte au niveau des premières divi- sions des bronches**','**FIG 12**')
source('f5-c3','DX5_CORRECTION_SOURCES_SEMIO_0.txt','UMVF/UNESS — Toux, expectoration et hémoptysie, 2013','https://archives.uness.fr/sites/campus-unf3s-2014/semiologie/enseignement/esemio9/site/html/cours.pdf','### **2\\.2. Toux**','### **2\\.5.')
source('f5-c4','DX5_CORRECTION_SOURCES_SEMIO_1.txt','HUG/CNRI — Prélèvement influenza Sentinella, formulaire 2017','https://www.hug.ch/sites/interhug/files/structures/laboratoire_de_virologie/documents/fichdema-fr_2017.pdf','**Prélèvements**','**Renseignements**')
source('f5-c5','DX5_CORRECTION_SOURCES_COMPLICATIONS_0.txt','ESC — Myocarditis and pericarditis, official slides, 2025','https://www.escardio.org/static-file/Escardio/Guidelines/Products/Slide%20sets/2025/2025%20official%20slides_MyoPeri.pdf','Recent or concomitant flu-like syndrome or','Recent or concomitant flu-like syndrome or\n\ngastroenteritis\n\nPleuritic')
source('f5-c6','DX5_CORRECTION_SOURCES_COMPLICATIONS_0.txt','ESC — Initial diagnostic assessment, 2025','https://www.escardio.org/static-file/Escardio/Guidelines/Products/Slide%20sets/2025/2025%20official%20slides_MyoPeri.pdf','Complete clinical evaluation, including history','Hospital admission is recommended for patients with high-risk')
source('f5-c7','DX5_CORRECTION_SPILF.txt','SPILF/Stahl — Infectious encephalitis guidelines, 2017','https://www.infectiologie.com/UserFiles/File/spilf/recos/2017-rfe-spilf-encephalite.pdf','_1\\.1._ _Clinical_','_1\\.2._ _Biological_')
source('f5-c8','DX5_CORRECTION_SPILF.txt','SPILF/Stahl — CSF and imaging, 2017','https://www.infectiologie.com/UserFiles/File/spilf/recos/2017-rfe-spilf-encephalite.pdf','_1\\.3._ _Cerebrospinal_','**2\\.** **Q2:**')
(D/'paquet.json').write_text(json.dumps(pk,ensure_ascii=False,indent=2))
nums={x['id']:str(i+1) for i,x in enumerate(pk['passages'])}
def refs(ids):return ''.join('<sup class="r"><a href="#sb-'+s+'">'+nums[s]+'</a></sup>' for s in ids.split())
def p(t,ids):return '<div class="p">'+t+refs(ids)+'. </div>\n'
def edit(n,fn):
 f=F/f'p{n:02}.html';f.write_text(fn(f.read_text()))
def row(cells,ids):return '<tr>'+''.join('<td>'+p(c,ids)+'</td>' for c in cells)+'</tr>\n'
def c4(t):
 pat=r'<tr><td><div class="p">Une complication cardiaque ou neurologique.*?</tr>'
 a=row(['Une myocardite peut compliquer un syndrome grippal','Une douleur thoracique pseudo-infarctus, des palpitations, une syncope ou une instabilité circulatoire alertent','La présence d’influenza ne prouve pas la cause de la douleur thoracique','Une suspicion impose ECG, biomarqueurs myocardiques et échocardiographie ; l’instabilité nécessite une évaluation hospitalière urgente'],'f5-c5 f5-c6 flu-ssi-alarmes')
 a+=row(['Une encéphalite infectieuse doit être envisagée devant une atteinte neurologique fébrile','Confusion, changement du comportement, crise épileptique ou déficit focal orientent','Les signes méningés peuvent manquer ; la fièvre peut être masquée par un antipyrétique','Une évaluation hospitalière urgente recherche notamment une indication d’imagerie cérébrale et de ponction lombaire selon les conditions de sécurité détaillées au point 9'],'f5-c7 f5-c8')
 return re.sub(pat,a,t,flags=re.S)
edit(4,c4)
edit(6,lambda t:t.replace('Le stéthoscope est déplacé sur des zones correspondantes afin de rechercher une anomalie localisée'+refs('flu-ssi-tests'),'Le stéthoscope est posé sur la peau, dans le calme ; le patient respire par la bouche et les zones correspondantes sont comparées de haut en bas'+refs('f5-c1'))+p('Le repère normal des plages pulmonaires est un murmure vésiculaire doux, plus long à l’inspiration ; chaque site est écouté pendant un cycle complet. La comparaison droite-gauche couvre les faces antérieure, latérale et postérieure','f5-c2')+p('Des sibilances expiratoires suggèrent une obstruction des voies inférieures ; des ronchis graves aux deux temps évoquent des sécrétions. Des crépitants fins inspiratoires traduisent l’ouverture de petites voies remplies d’exsudat ou de transsudat : pneumonie, œdème et fibrose restent à distinguer','f5-c2')+p('Un souffle tubaire entendu sur une plage pulmonaire suggère une condensation. La modification des bruits après la toux aide à distinguer les sécrétions et certains crépitants d’ouverture ; un bruit isolé ne désigne donc pas à lui seul une pneumonie bactérienne','f5-c1 f5-c2'))
def c7(t):
 # Attach acquired definitions to existing windows, without changing safety thresholds.
 t=re.sub(r'(<div class="p">L’hémoptysie correspond.*?</div>)',lambda m:m[0].replace(refs('flu-ssi-alarmes'),refs('f5-c3')),t)
 t=re.sub(r'(<div class="p">Le stridor est.*?</div>)',lambda m:m[0].replace(refs('flu-ssi-alarmes'),refs('f5-c2')),t)
 t=t.replace('La fièvre est une élévation mesurée de la température corporelle ; les frissons sont une sensation accompagnée de contractions musculaires involontaires','L’OFSP décrit une fièvre supérieure à 38 °C et des frissons parmi les symptômes typiques de la grippe')
 return t+p('La toux est un phénomène expulsif réflexe qui participe au drainage bronchique. Une expectoration purulente peut accompagner une infection virale : son aspect ne suffit pas à établir une surinfection bactérienne','f5-c3')
edit(7,c7)
edit(9,lambda t:t+p('Le formulaire HUG/CNRI Sentinella de 2017 décrit un frottis nasal profond associé à un frottis de gorge : les deux écouvillons sont placés ensemble dans un tube de milieu de transport, puis leurs tiges sont cassées. Ce protocole identifié ne remplace pas les instructions du laboratoire pour le dispositif et la méthode actuellement utilisés','f5-c4')+p('Si une myocardite est suspectée, l’ESC 2025 recommande anamnèse, examen, radiographie thoracique, biomarqueurs, ECG et échocardiographie. La troponine ultrasensible documente la lésion myocardique ; l’IRM cardiaque recherche l’inflammation dans la filière spécialisée','f5-c5 f5-c6')+p('Pour une suspicion d’encéphalite, la SPILF 2017 privilégie l’IRM cérébrale urgente lorsqu’elle est réalisable ; à défaut, un scanner est réalisé. En cas de trouble de vigilance, déficit focal ou crise, une imagerie précède la ponction lombaire pour rechercher une contre-indication ; la ponction reste urgente dès qu’elle est possible','f5-c8')+p('Le liquide céphalorachidien est examiné pour sa cytologie, ses protéines, glucose et lactate, avec glycémie concomitante, examen bactériologique et PCR HSV, VZV et entérovirus. Un EEG aide à rechercher une crise ou un état de mal ; une PCR respiratoire influenza positive ne dispense pas de ce bilan neurologique','f5-c8')+p('Si la ponction lombaire est impossible, la SPILF prévoit une prise en charge empirique hospitalière couvrant méningite bactérienne et encéphalite infectieuse sans attendre sa réalisation. Les produits de contraste éventuels sont choisis après vérification du terrain et des contre-indications','f5-c8'))
edit(12,lambda t:t.replace('aux personnes âgées, aux femmes enceintes, aux prématurés dans le cadre précisé par l’OFSP','aux personnes de plus de 65 ans, aux femmes enceintes, aux prématurés jusqu’à 2 ans')+p('L’OFSP privilégie un vaccin antigrippal à dose élevée chez les personnes de 75 ans et plus, ainsi que dès 65 ans avec un facteur de risque supplémentaire. Cette recommandation de produit n’est pas une dose vaccinale à improviser','f5-13'))
removed=[]
for n,starts in {2:['Une incidence suisse chiffrée','Les sources utilisées ne donnent'],8:['Il n’existe pas, dans les sources acquises'],11:['Les sources acquises ne fixent']}.items():
 f=F/f'p{n:02}.html';t=f.read_text()
 for start in starts:
  pat=r'<div class="p">'+re.escape(start)+r'.*?</div>\n?'
  for m in re.finditer(pat,t):removed.append(dict(point=n,raison='LV7 : constat de collecte déplacé dans HELP',html=m[0]))
  t=re.sub(pat,'',t,flags=re.S)
 f.write_text(t)
with (D/'HELP.md').open('a') as f:f.write('\n## Correction P3 — lacunes de collecte\n'+ '\n'.join(re.sub('<[^>]+>','',x['html']) for x in removed)+'\nQ11a : aucune cible individuelle universelle documentée ; le point partiel peut être conservé. Aucun seuil de triage ne devient un objectif thérapeutique.\n')
# Existing redundant reminders in point4 repeat the triage/test/safety messages preserved in points8–11.
f=F/'p04.html';t=f.read_text()
for start in ['Le choix d’un test doit tenir compte du délai','La consultation évite un bilan identique','Cette économie d’examens reste conditionnée']:
 pat=r'<div class="p">'+re.escape(start)+r'.*?</div>\n?'
 for m in re.finditer(pat,t):removed.append(dict(point=4,raison='Rappel conservé dans points8–11 ; place nécessaire aux corrections',html=m[0]))
 t=re.sub(pat,'',t,flags=re.S)
f.write_text(t)
(D/'CORRECTIONS_P3.json').write_text(json.dumps(dict(version_avant_sha256='77657f8d7ca96b2c67775efd39632958f43c38158442b180bf49f88720797716',questions=['Q4b','Q6b','Q7','Q9b','Q12'],Q11a='Limite conservée conformément à C3 ; pas de cible inventée',retraits=removed,nouveaux_passages=[x['id'] for x in pk['passages'] if x['id'].startswith('f5-c')]),ensure_ascii=False,indent=2))
(D/'CORRECTIONS_P3.diff').write_text(''.join(''.join(difflib.unified_diff((BK/f.name).read_text().splitlines(True),f.read_text().splitlines(True),fromfile='avant/'+f.name,tofile='apres/'+f.name)) for f in sorted(F.glob('*.html'))))
