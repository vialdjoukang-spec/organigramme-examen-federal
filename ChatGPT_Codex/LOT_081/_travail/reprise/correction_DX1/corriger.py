import argparse
import hashlib
import html
import json
from pathlib import Path
import re
import shutil
import subprocess
import sys

B=Path(__file__).resolve().parent
LOT=B.parents[2]
SRC=B.parent/'redaction_DX1'
OUTILS=LOT.parent/'_outils'
CANON=LOT/'LOT_081_Phase_B_V0_DX.1.html'
EXPECTED='a72d5182dd593ead6af7681f8c1574346056dbcf4a4d20ded1973e7ff3823b63'
assert hashlib.sha256(CANON.read_bytes()).hexdigest()==EXPECTED
(B/'fragments').mkdir(parents=True,exist_ok=True)
for n in range(1,15):shutil.copy2(SRC/'fragments'/f'p{n:02d}.html',B/'fragments'/f'p{n:02d}.html')
shutil.copy2(SRC/'contrat.json',B/'contrat.json')
packet=json.loads((SRC/'paquet.json').read_text())
changes=[]
new_ids=[]

def cite(*ids):
 return ''.join('<sup class="r"><a href="#sb-'+i+'">'+i+'</a></sup>' for i in ids)
def para(ident,text,*ids):
 return '<div class="p" id="'+ident+'">'+html.escape(text)+cite(*ids)+'</div>\n'
def window(n,ident,title,rows):
 return '<h4><button class="w" popovertarget="'+ident+'">'+html.escape(title)+'</button></h4>\n<div id="'+ident+'" popover class="fenetre"><h4>'+html.escape(title)+'</h4>\n'+''.join(para(ident+'-fait'+str(j),text,*ids) for j,(text,ids) in enumerate(rows,1))+'</div>\n'
def modify(n,label,old,new,refs,items):
 p=B/'fragments'/f'p{n:02d}.html';s=p.read_text();assert s.count(old)==1,(label,s.count(old));s=s.replace(old,new,1);p.write_text(s)
 changes.append({'id':label,'point':n,'items_du_rapport':items,'avant':old,'apres':new,'references':refs})
def append(n,label,block,refs,items):
 p=B/'fragments'/f'p{n:02d}.html';p.write_text(p.read_text()+block)
 changes.append({'id':label,'point':n,'items_du_rapport':items,'operation':'ajout_en_fin_de_point','avant':'','apres':block,'references':refs})
def proof(ident,source,url,path,start,end=None,edition=None):
 t=path.read_text();a=t.index(start);z=t.index(end,a)+len(end) if end else a+len(start);text=t[a:z]
 packet['passages'].append({'id':ident,'source':source,'url':url,'date':'2026-11-10','annee_edition':edition,'texte':text,'cache_primaire':str(path.relative_to(LOT)),'sha256_cache':hashlib.sha256(path.read_bytes()).hexdigest(),'verification':'Sous-chaîne exacte et contiguë du cache primaire réellement relu ; aucun assemblage ni ellipse.'});new_ids.append(ident)

CEN=B.parent/'preparation_neuro/sources/eu-cen-examen-neurologique.txt'
U='https://www.cen-neurologie.fr/premier-cycle/examen-neurologique'
S='Collège des enseignants de neurologie — Examen neurologique, version consultée le10novembre2026 ; millésime non indiqué'
proof('dx1c-cen-rotulien',S,U,CEN,"Percussion du tendon rotulien chez un patient assis jambes pendantes",'Niveau de l\'arc réflexe : L4, nerf fémoral')
proof('dx1c-cen-achilleen',S,U,CEN,"Percussion du tendon d'Achille",'Niveau de l\'arc réflexe : S1, nerf tibial')
proof('dx1c-cen-reflexes-piege',S,U,CEN,'Les ROT peuvent être présents et normaux','sans que cela soit pathologique.')
proof('dx1c-cen-comparaison',S,U,CEN,"L'examen est conduit de façon comparative entre le côté droit",'comparant également les membres inférieurs et les membres supérieurs')
proof('dx1c-cen-tact',S,U,CEN,"La sensibilité au tact au doigt ou à l'aide d'un coton qu'on promène sur la peau.")
proof('dx1c-cen-force',S,U,CEN,'Tout examen doit être comparatif droite/gauche.')
HERNIE=B.parent/'preparation_neuro/sources/ch-hug-hernie-definition-2025.txt'
HURL='https://www.hug.ch/neurochirurgie/hernie-discale-lombaire'
idx=json.loads((B.parent/'preparation_neuro/INDEX_SOURCES.json').read_text())
# L’URL est reprise du paquet documentaire existant et non déduite d’un titre.
rp=json.loads((B.parent/'preparation_neuro/acquisition_primaire.json').read_text())
hp=next(q for q in rp['results'] if q['url']==HURL)
HURL=hp['url']
proof('dx1c-hug-racines','HUG — Neurochirurgie, hernie discale lombaire, mise à jour2025',HURL,HERNIE,'Elle peut alors entraîner une compression et une inflammation des nerfs lombaires.','(syndrome de la queue de cheval).',2025)
DP=B.parent/'preparation_neuro/sources/eu-dgou-2024.txt'
DU='https://register.awmf.org/assets/guidelines/187-059l_S2k_Spezifischer-Kreuzschmerz_2024-08.pdf'
proof('dx1c-dgou-flexion','DGOU — S2k Spezifischer Kreuzschmerz,2024,§2.5.4',DU,DP,'Der Durchmesser des\n\nZentralkanals nimmt unter axialer Belastung und Extension weiter ab','Flexion führen zur relativen Zunahme des Spinalkanaldurchmessers [217].',2024)

# Q1a : attribution institutionnelle explicite, sans inventer une société savante.
old='La lombalgie désigne une douleur située entre la douzième côte et le pli fessier, souvent associée à une raideur ou une mobilité réduite.'
new='Dans leur stratégie de 2022, les Hôpitaux universitaires de Genève (HUG) définissent une douleur entre la douzième côte et le pli fessier.'
p=B/'fragments/p01.html';s=p.read_text();m=re.search(r'<div class="p" id="dx1-p1-fait1">.*?</div>\n',s);assert old in html.unescape(re.sub('<[^>]+>','',m[0]))
modify(1,'DX1-C01',m[0],para('dx1-p1-fait1',new,'hug22-definition','hug22-classification')+para('dx1-p1-corr-definition','Cette douleur lombaire s’accompagne généralement d’une raideur ou d’une limitation de la mobilité du rachis.','hug22-definition'),['hug22-definition','hug22-classification'],['Q1a'])

# Q6b : gestes, réponses, localisations et pièges, sans nouvelles valeurs normales.
append(6,'DX1-C02',window(6,'dx1-p6-corr-reflexes','Réflexes des membres inférieurs : exécution et portée',[
 ('Pour rechercher le réflexe rotulien, le patient est assis jambes pendantes, ou couché avec la jambe semi-fléchie soutenue.', ['dx1c-cen-rotulien']),
 ('La percussion du tendon rotulien déclenche une contraction du quadriceps et une extension du genou ; cet arc correspond à L4.', ['dx1c-cen-rotulien']),
 ('Le tendon d’Achille est percuté pour rechercher la contraction du triceps sural et la flexion plantaire, correspondant à S1.', ['dx1c-cen-achilleen']),
 ('Ces réponses doivent être confrontées aux mouvements testés : extension du genou pour L3–L4 et flexion plantaire de cheville pour S1.', ['hug22-neurologie']),
 ('Une interruption de l’arc réflexe, notamment par une atteinte de racine postérieure, peut expliquer une aréflexie ostéotendineuse.', ['dx1c-cen-reflexes-piege']),
 ('Cependant, des réflexes constitutionnellement très faibles ou absents peuvent exister sans maladie ; une vivacité isolée peut aussi être non pathologique.', ['dx1c-cen-reflexes-piege']),
 ('Le résultat est donc interprété avec les signes sensitifs et moteurs, au lieu de conclure sur un réflexe isolé.', ['hug22-neurologie','dx1c-cen-reflexes-piege'])
]),['dx1c-cen-rotulien','dx1c-cen-achilleen','dx1c-cen-reflexes-piege','hug22-neurologie'],['Q6b'])
append(6,'DX1-C03',window(6,'dx1-p6-corr-sensibilite','Sensibilité et force : comparaison segmentaire',[
 ('Le tact est exploré au doigt ou avec un coton parcourant la peau, afin de préciser une anomalie sensitive rapportée.', ['dx1c-cen-tact','hug22-neurologie']),
 ('La comparaison porte sur les côtés droit et gauche, puis sur les segments distaux et proximaux.', ['dx1c-cen-comparaison']),
 ('Dans le bilan lombaire HUG, les territoires explorés comprennent les cuisses, les mollets et les pieds.', ['hug22-neurologie']),
 ('La force est également comparée des deux côtés ; la flexion de hanche explore L1–L2 et l’extension du genou L3–L4.', ['dx1c-cen-force','hug22-neurologie']),
 ('Pour L5, l’extension du gros orteil et la flexion dorsale de cheville sont recherchées séparément de la marche globale.', ['hug22-neurologie']),
 ('Pour S1, la flexion plantaire de cheville est confrontée au réflexe achilléen et aux résultats sensitifs.', ['hug22-neurologie']),
 ('La cotation M5 à M0 précise ensuite le déficit ; une marche conservée sur talons ou pointes ne suffit pas à exclure une atteinte discrète.', ['hug22-neurologie'])
]),['dx1c-cen-tact','dx1c-cen-comparaison','dx1c-cen-force','hug22-neurologie'],['Q6b'])

# Q7a : fenêtres des signes déjà présents dans les syndromes ; pas de nouvelle entité.
append(7,'DX1-C04',window(7,'dx1-p7-corr-lombovertebral','Douleur, raideur et limitation lombovertébrale',[
 ('La douleur lombaire est localisée entre la douzième côte et le pli fessier ; raideur et limitation de mobilité peuvent l’accompagner.', ['hug22-definition']),
 ('Les flexions antéropostérieure et latérale recherchent le retentissement lombovertébral, tandis que la distance doigts-sol sert surtout de repère de suivi.', ['hug22-dynamique']),
 ('La contracture est recherchée par la palpation lombaire chez une personne couchée sur le ventre, plutôt qu’en position debout.', ['hug22-palpation']),
 ('Une forte douleur et la peur du mouvement sont recherchées ensemble, car les HUG les retiennent parmi les facteurs de chronicisation.', ['hug22-risque-chronicite']),
 ('Ces constatations décrivent le retentissement douloureux ; elles ne désignent pas à elles seules une lésion pathoanatomique causale.', ['hug22-diagnostic-imagerie','l81-de-nonspecifique'])
]),['hug22-definition','hug22-dynamique','hug22-palpation','hug22-risque-chronicite','l81-de-nonspecifique'],['Q7a'])
append(7,'DX1-C05',window(7,'dx1-p7-corr-radiculaire','Irradiation et irritation radiculaire : le signe et son contexte',[
 ('L’irradiation dépasse le pli fessier dans une lombo-sciatalgie ; la concordance d’un territoire et de signes irritatifs précise une atteinte radiculaire.', ['hug22-classification']),
 ('Le Lasègue recherche une douleur dans le trajet radiculaire pendant l’élévation de jambe, avec une positivité décrite entre 30° et 70°.', ['hug22-neurologie']),
 ('Si seule la région lombaire est douloureuse pendant cette élévation, le signe radiculaire n’est pas positif selon cette définition.', ['hug22-neurologie']),
 ('Une extension passive de hanche en décubitus ventral ou latéral recherche la douleur antérieure de cuisse du rétro-Lasègue.', ['hug22-neurologie']),
 ('Cette douleur antérieure oriente vers L2, L3 ou L4 ; les signes ne sont donc pas tous attribués au nerf sciatique.', ['hug22-neurologie','hug22-classification']),
 ('Lorsqu’une hernie discale en est la cause, une compression et une inflammation des nerfs lombaires peuvent expliquer la douleur et les déficits.', ['dx1c-hug-racines']),
 ('Ce mécanisme appartient à une cause spécifique à rechercher ; il n’est pas attribué à toute lombalgie non spécifique.', ['dx1c-hug-racines','l81-de-nonspecifique'])
]),['hug22-classification','hug22-neurologie','dx1c-hug-racines','l81-de-nonspecifique'],['Q7a'])
append(7,'DX1-C06',window(7,'dx1-p7-corr-deficit','Déficit moteur, trouble sensitif et signe sacré',[
 ('Un déficit moteur est décrit par le mouvement atteint et sa cotation, depuis M5 normal jusqu’à M0 sans contraction visible.', ['hug22-neurologie']),
 ('L’examen recherche les mouvements contre résistance, contre gravité ou dans le plan du lit, puis confronte les deux côtés.', ['hug22-neurologie','dx1c-cen-force']),
 ('Une perte de sensibilité dans la jambe ou le pied peut accompagner une atteinte des nerfs lombaires par une hernie.', ['dx1c-hug-racines']),
 ('Le tact comparatif permet de préciser cette plainte, tandis que les réflexes et la force documentent les autres composantes neurologiques.', ['dx1c-cen-tact','dx1c-cen-comparaison','hug22-neurologie']),
 ('La queue de cheval correspond ici à une compression des racines sacrées ; troubles sphinctériens et anesthésie en selle changent la priorité.', ['hug22-neurologie','pa17-lomb22-queue']),
 ('La sensibilité péri-anale et glutéale et le tonus anal sont alors recherchés, mais cet examen ne retarde pas l’imagerie urgente.', ['hug22-neurologie','hug22-diagnostic-imagerie'])
]),['hug22-neurologie','dx1c-cen-force','dx1c-hug-racines','dx1c-cen-tact','dx1c-cen-comparaison','pa17-lomb22-queue','hug22-diagnostic-imagerie'],['Q7a'])
append(7,'DX1-C07',window(7,'dx1-p7-corr-posture','Claudication : relier la posture au mécanisme',[
 ('La douleur de marche soulagée en position assise et par diminution de la lordose oriente vers une claudication neurogène.', ['l81-hug-stenose']),
 ('Dans la sténose lombaire dégénérative, la charge axiale et l’extension rétrécissent davantage le canal, tandis que la flexion augmente relativement son diamètre.', ['dx1c-dgou-flexion']),
 ('Le profil postural est donc recherché à l’entretien et confronté à l’examen neurologique, au lieu de conclure sur la localisation lombaire seule.', ['l81-hug-stenose','hug22-diagnostic-imagerie'])
]),['l81-hug-stenose','dx1c-dgou-flexion','hug22-diagnostic-imagerie'],['Q7a'])

# Q8a : les bornes sont reprises dans le point qui porte le diagnostic positif.
old='La durée précise une phase aiguë, subaiguë ou chronique.'
p=B/'fragments/p08.html';s=p.read_text();m=next(x for x in re.findall(r'<td>.*?</td>',s,re.S) if old in x)
new='<td>'+html.escape('Le cadre HUG de 2022 distingue un épisode aigu inférieur à quatre semaines d’une persistance chronique dépassant trois mois.')+cite('hug22-classification')+' '+html.escape('Entre quatre et douze semaines, la durée appartient à la catégorie subaiguë de cette classification.')+cite('hug22-classification')+'</td>'
modify(8,'DX1-C08',m,new,['hug22-classification'],['Q8a'])

# Q11f : conserver exactement la condition AIPS, sans arrêt systématique inventé.
append(11,'DX1-C09',window(11,'dx1-p11-corr-tramal','Tramadol : reconnaître une complication et agir',[
 ('Un syndrome sérotoninergique peut associer des modifications mentales, une instabilité autonome, des anomalies neuromusculaires ou des symptômes gastro-intestinaux.', ['aips81-tramal-8-p30']),
 ('Si ce syndrome est suspecté, une réduction de dose ou un arrêt du traitement est envisagé selon la gravité des symptômes.', ['aips81-tramal-8-p31']),
 ('Le retrait des médicaments sérotoninergiques apporte généralement une amélioration rapide ; la conduite dépend donc du tableau clinique.', ['aips81-tramal-8-p31']),
 ('Quand une association sérotoninergique est cliniquement justifiée, la surveillance est particulièrement attentive à l’instauration et aux augmentations de dose.', ['aips81-tramal-8-p29']),
 ('Une dépression respiratoire doit être reconnue et traitée rapidement, car elle peut évoluer vers un arrêt respiratoire et la mort.', ['aips81-tramal-8-p5']),
 ('Selon l’état clinique, son traitement comporte une surveillance étroite, des mesures de soutien et l’administration d’antagonistes opioïdes.', ['aips81-tramal-8-p5']),
 ('Des convulsions peuvent également survenir aux doses recommandées ; les médicaments abaissant le seuil convulsif renforcent ce risque.', ['aips81-tramal-8-p26'])
]),['aips81-tramal-8-p30','aips81-tramal-8-p31','aips81-tramal-8-p29','aips81-tramal-8-p5','aips81-tramal-8-p26'],['Q11f'])

packet['statut']='Copie privée corrigée après audit P3 ; aucune autoévaluation P3 ; contrelecture indépendante attendue.'
packet['correction_DX1']={'audit_entree':'audits/DX1_P3.audit.json','sha256_entree':EXPECTED,'extraits_ajoutes':new_ids}
(B/'paquet.json').write_text(json.dumps(packet,ensure_ascii=False,indent=2)+'\n')
(B/'CHANGEMENTS_EXACTS.json').write_text(json.dumps({'base_sha256':EXPECTED,'changements':changes,'portee':'Seuls les points1,6,7,8,11 sont modifiés ; aucun autre point clinique ni canonique modifié.'},ensure_ascii=False,indent=2)+'\n')
(B/'HELP.json').write_text(json.dumps({'date':'2026-11-10','lacunes_non_comblees':[{'item':'Q1a','point':1,'constat':'Attribution institutionnelle HUG2022 explicitée ; aucune définition nouvelle de société savante n’a été acquise. HUG ne devient pas une société savante.'},{'item':'Q3a','point':3,'constat':'Chaîne cellulaire/tissulaire spécifique au phénomène douloureux non complétée par une source déjà acquise. Aucune lésion causale unique attribuée à la lombalgie commune.'},{'item':'Q11a','point':11,'constat':'Objectif fonctionnel individualisé conservé ; aucun but chiffré inventé et pronostic à six semaines non transformé en objectif.'}],'sources_deja_lues':['HUG2022','NICE NG59 actualisation2026','CEN examen neurologique','HUG hernie2025','DGOU2024 §2.5.4','AIPS Tramal avril2025']},ensure_ascii=False,indent=2)+'\n')
target=B/CANON.name
subprocess.run([sys.executable,str(OUTILS/'assembler.py'),'--fragments',str(B/'fragments'),'--paquet',str(B/'paquet.json'),'--contrat',str(B/'contrat.json'),'--titre','DX.1 — Lombalgie commune non spécifique','--sortie',str(target)],check=True)
# Même mise en lignes des sources que la version d’entrée ; aucun texte clinique changé ici.
target.write_text(target.read_text().replace('</li>','</li>\n'))
control=subprocess.run([sys.executable,str(OUTILS/'controle3.py'),str(target),'--paquet',str(B/'paquet.json'),'--ex','12'],capture_output=True,text=True)
(B/'controle.json').write_text(control.stdout)
final=target.read_bytes()
(B/'MANIFESTE.json').write_text(json.dumps({target.name:{'octets':len(final),'sha256':hashlib.sha256(final).hexdigest()}},ensure_ascii=False,indent=2)+'\n')
assert hashlib.sha256(CANON.read_bytes()).hexdigest()==EXPECTED
print(control.stdout)
print('SHA256',hashlib.sha256(final).hexdigest(),'OCTETS',len(final),'CANONIQUE_INCHANGE',True)
