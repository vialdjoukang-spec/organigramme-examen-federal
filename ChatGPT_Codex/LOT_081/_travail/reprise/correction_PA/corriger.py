from pathlib import Path
import json,html,shutil
R=Path(__file__).resolve().parent; O=R.parent/'redaction_PA'
for f in (O/'fragments').glob('*.html'):shutil.copyfile(f,R/'fragments'/f.name)
shutil.copyfile(O/'contrat.json',R/'contrat.json')
packet=json.loads((O/'paquet.json').read_text());ids={x['id'] for x in packet['passages']}
for d, wanted in [('redaction_DX2_3/DX.3',['n81-cen-force','n81-cen-reflexes-mi','n81-cen-reflexes-normalite','n81-cen-sensibilite','pa814-esur-allergie','pa814-esur-renal','pa814-esur-alternative']),('redaction_DX5_6/DX.5',['c-enfant','c-metabolique'])]:
 q=json.loads((R.parent/d/'paquet.json').read_text())
 for x in q['passages']:
  if x['id'] in wanted and x['id'] not in ids:packet['passages'].append(x);ids.add(x['id'])
(R/'paquet.json').write_text(json.dumps(packet,ensure_ascii=False,indent=2)+'\n')
def p(t,*refs):
 assert all(i in ids for i in refs)
 return '<div class="p">'+html.escape(t)+''.join('<sup class="r"><a href="#sb-'+i+'">'+i+'</a></sup>' for i in refs)+'</div>\n'
def w(key,title,body):
 return '<button class="w" popovertarget="'+key+'">'+html.escape(title)+'</button><div id="'+key+'" class="fenetre" popover><h4><em>'+html.escape(title)+'</em></h4>'+body+'</div>\n'
f=R/'fragments/p06.html';s=f.read_text()
anchor=p('La force normale correspond au grade M5 dans l’échelle décrite par HUG ; ce repère précède l’identification des déficits.','hug22-neurologie');assert anchor in s
normal=p('L’examen neurologique confronte les deux côtés avant de qualifier une faiblesse, une asymétrie réflexe ou une perte de sensibilité.','n81-cen-force','n81-cen-sensibilite','n81-cen-reflexes-normalite')
normal+=p('Pour le réflexe rotulien, la réponse attendue associe contraction du quadriceps et extension du genou ; pour le réflexe achilléen, elle associe contraction du triceps sural et flexion plantaire.','n81-cen-reflexes-mi')
normal+=p('La perception tactile est comparée entre droite et gauche, entre segments proximaux et distaux, puis entre membres supérieurs et inférieurs lorsque la topographie le demande.','n81-cen-sensibilite')
normal+=p('Une vivacité réflexe isolée peut s’observer chez un sujet tendu ou anxieux ; certains sujets ont aussi des réflexes constitutionnellement faibles ou absents sans maladie.','n81-cen-reflexes-normalite')
normal+=p('Ainsi, la valeur d’une réponse réflexe dépend de son association aux autres signes et de sa concordance topographique.','n81-cen-reflexes-normalite','hug22-neurologie')
s=s.replace(anchor,anchor+normal)
old=p('L’indice de Schobert modifié et la distance doigt-sol reflètent des dimensions différentes de la mobilité ; ils sont particulièrement utiles au suivi.','hug22-dynamique');assert old in s
s=s.replace(old,p('Pour apprécier la mobilité, l’examinateur demande au patient une flexion antérieure, une extension puis des inclinaisons latérales du tronc et observe le mouvement obtenu.','hug22-dynamique'))
old=p('Les réflexes rotuliens et achilléens complètent l’examen moteur ; la sensibilité est explorée sur les cuisses, les mollets et les pieds.','hug22-neurologie');assert old in s
body=p('Le réflexe rotulien se recherche par percussion du tendon rotulien, chez le patient assis avec les jambes pendantes ou couché avec la jambe semi-fléchie soutenue par l’examinateur.','n81-cen-reflexes-mi')
body+=p('L’examinateur observe la contraction du quadriceps et l’extension du genou ; l’arc décrit par le CEN correspond à L4 et au nerf fémoral.','n81-cen-reflexes-mi')
body+=p('Le réflexe achilléen est déclenché en percutant le tendon d’Achille, puis en observant la contraction du triceps sural et la flexion plantaire du pied.','n81-cen-reflexes-mi')
body+=p('L’arc achilléen correspond à S1 et au nerf tibial ; l’interprétation est rapprochée de la force et du territoire sensitif.','n81-cen-reflexes-mi','hug22-neurologie')
body+=p('Pour le tact, le clinicien passe un doigt ou un coton sur la peau et compare les perceptions de façon systématique entre côtés et segments.','n81-cen-sensibilite')
body+=p('Les résultats sont consignés sur un schéma corporel daté avec le nom du patient et de l’examinateur ; l’examen est répété si nécessaire.','n81-cen-sensibilite')
body+=p('Une compréhension insuffisante limite l’interprétation des réponses sensitives ; l’examen requiert du temps et de la patience.','n81-cen-sensibilite')
s=s.replace(old,old+w('pa81-p6-correction-rot','Réaliser les réflexes et le tact comparatif',body));f.write_text(s)
f=R/'fragments/p09.html';s=f.read_text();anchor='<h4><em>9.d — Organiser la seconde intention et son délai</em></h4>\n';assert anchor in s
body=p('Chez l’enfant avec suspicion de calcul, l’EAU recommande d’abord une échographie incluant les reins, la vessie remplie et les segments urétéraux accessibles près du rein et de la vessie.','c-enfant')
body+=p('Si cette échographie ne fournit pas l’information requise, l’EAU prévoit une radiographie réno-urétéro-vésicale ou un scanner sans contraste à faible dose.','c-enfant')
body+=p('L’uro-IRM peut préciser l’anatomie et le siège d’un obstacle, mais elle n’est généralement pas fiable pour détecter les calculs eux-mêmes.','c-enfant')
body+=p('Un antécédent de réaction d’hypersensibilité à un produit iodé ou gadoliné conduit à envisager une autre modalité, ou un examen sans injection si son rendement suffit à la prise en charge.','pa814-esur-allergie')
body+=p('L’ESUR identifie le DFGe inférieur à 30 ml/min/1.73 m² comme facteur de risque avant contraste intraveineux ou intra-artériel avec exposition rénale de second passage.','pa814-esur-renal')
body+=p('Une méthode n’utilisant pas de contraste iodé est alors à envisager ; ce seuil ne signifie pas que toute imagerie urgente devient interdite.','pa814-esur-alternative','l81-hug-urgent-neuro','l81-nice-aaa-urgence')
body+=p('L’alternative doit continuer à répondre à la question clinique : le bilan d’une compression ou d’une suspicion aortique urgente demeure organisé avec l’équipe concernée.','l81-hug-urgent-neuro','l81-nice-aaa-urgence')
extra=w('pa81-p9-correction-alternatives','Enfant, réaction au contraste et risque rénal',body)
body=p('Les valeurs ci-dessous appartiennent au bilan métabolique lithiasique de l’adulte présenté par l’EAU, et ne constituent pas un bilan systématique de toute lombalgie.','c-metabolique','hug22-diagnostic-imagerie')
body+=p('Le tableau EAU donne une créatininémie de référence de 50–100 μmol/L, une calcémie totale de 2.0–2.5 mmol/L et une calcémie ionisée de 1.12–1.32 mmol/L.','c-metabolique')
body+=p('Il indique également une natrémie de 135–145 mmol/L et une kaliémie de 3.5–5.5 mmol/L ; ces intervalles sont présentés avec leur source et leur population adulte.','c-metabolique')
body+=p('Le bilan métabolique spécifique concerne les patients à haut risque lithiasique, tandis que l’analyse fiable du calcul et une évaluation métabolique de base sont demandées chez tout patient formant un calcul.','c-metabolique')
body+=p('Après l’épisode aigu, l’EAU situe le bilan métabolique au plus tôt à 20 jours et de préférence vers trois mois, une fois le patient stable, sans infection et sous ses apports habituels.','c-metabolique')
extra+=w('pa81-p9-correction-si','Repères biologiques en unités SI dans la branche lithiasique',body)
s=s.replace(anchor,extra+anchor);f.write_text(s)
(R/'CORRECTIONS.json').write_text(json.dumps({'audit':'audits/PA_P3.audit.json','portee':['PA-C1 normalité comparative au point6','PA-C2 gestes ROT et tact au point6 ; retrait des deux noms de tests sans technique dans le paquet initial','PA-C3 alternatives pédiatriques lithiasiques, hypersensibilité et risque rénal au point9 ; repères SI EAU contextualisés','PA-C4 retours entre balises lors de l’assemblage'],'autres_points':'Fragments1–5,7–8,10–14 identiques au manuscrit initial.'},ensure_ascii=False,indent=2)+'\n')
