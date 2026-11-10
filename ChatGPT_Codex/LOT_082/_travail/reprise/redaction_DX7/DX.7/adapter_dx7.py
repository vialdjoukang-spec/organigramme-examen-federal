from pathlib import Path
import json,html,re,hashlib,copy
B=Path(__file__).resolve().parent
O=Path('ChatGPT_Codex/LOT_080/_travail/reprise/redaction_DX1_3/DX.1')
J=lambda p:json.loads(p.read_text())
pq=J(B/'paquet.json');sources={x['id']:x for x in pq['passages']}
def add(id,text,source,url,cache,year=None):
    if id in sources:return
    x={'id':id,'source':source,'url':url,'date':'2026-11-10','annee_edition':year,'texte':text,'cache':str(cache),'lecture':'Passage primaire contigu réellement lu,conservé sans ellipse de fusion.'}
    pq['passages'].append(x);sources[id]=x
def pick(id,result,start,end,cache,year=None):
    s=result.get('full_content') or '\n'.join(result.get('excerpts',[]));a=s.index(start);z=s.index(end,a)+len(end)
    add(id,s[a:z],result['title'].strip(),result['url'],cache,year)
ch=J(B/'cache/EXTRACTION_CHIRURGIE_CH.json')['results']
hug=next(x for x in ch if 'enfants-ados.hug' in x['url'])
pick('dx7-hug-chirurgie',hug,'Pour réaligner la colonne','les jeunes en croissance).',B/'cache/EXTRACTION_CHIRURGIE_CH.json',2023)
pick('dx7-hug-monitoring',hug,'L’intervention, pratiquée','pendant la chirurgie.',B/'cache/EXTRACTION_CHIRURGIE_CH.json',2023)
pick('dx7-hug-vbt',hug,'Et depuis 2020','(VBT))',B/'cache/EXTRACTION_CHIRURGIE_CH.json',2023)
pick('dx7-hug-date',hug,'Dernière mise à jour','21/04/2023',B/'cache/EXTRACTION_CHIRURGIE_CH.json',2023)
pr=next(x for x in ch if 'article-pro' in x['url'])
pick('dx7-hug-fusion',pr,'Un greffon osseux','vertèbres entre elles.',B/'cache/EXTRACTION_CHIRURGIE_CH.json',2021)
eu=J(B/'cache/EXTRACTION_SORTIE_SIA_EUROPE.json')['results']
ox=next(x for x in eu if 'ouh.nhs' in x['url'])
pick('dx7-oxford-sortie',ox,'## Goals for discharge',"following your surgery",B/'cache/EXTRACTION_SORTIE_SIA_EUROPE.json')
pick('dx7-oxford-progressivite',ox,'* Increase your activity level','gradual return to school or college',B/'cache/EXTRACTION_SORTIE_SIA_EUROPE.json')
nc=next(x for x in eu if 'northerncarealliance' in x['url'])
pick('dx7-nca-sortie',nc,'#### Going home','approximately 3 months post-surgery.',B/'cache/EXTRACTION_SORTIE_SIA_EUROPE.json',2026)
pick('dx7-nca-reeducation',nc,'Post-surgery you will be seen','encourage walking.',B/'cache/EXTRACTION_SORTIE_SIA_EUROPE.json',2026)
pick('dx7-nca-complications',nc,'There is a risk of surgical wound infections.','At worst this can be complete paralysis',B/'cache/EXTRACTION_SORTIE_SIA_EUROPE.json',2026)
pick('dx7-nca-alerte',nc,'**If any of these complications happen once discharged','please contact:**',B/'cache/EXTRACTION_SORTIE_SIA_EUROPE.json',2026)
sos=Path('ChatGPT_Codex/LOT_082/_travail/reprise/preparation_rachis/cache/SOSORT2018_ARCHIVE.txt');s=sos.read_text();a=s.index('# 2016 SOSORT guidelines:');z=s.index('Published: 10 January 2018',a)+len('Published: 10 January 2018');add('dx7-bib-sosort',s[a:z],'SOSORT — Identification éditoriale2016/2018','https://link.springer.com/article/10.1186/s13013-017-0145-8',sos,2018)
pdf=Path('ChatGPT_Codex/LOT_080/_travail/reprise/evidence/ch-scol-2023.txt');s=pdf.read_text();t='Vol. 34 | 4-2023';assert t in s;add('dx7-bib-paediatrica',t,'Paediatrica — Identification éditoriale2023','https://cdn.paediatrieschweiz.ch/production/uploads/2023/11/34_4_2023_FR_06.pdf',pdf,2023)
rev=Path('ChatGPT_Codex/LOT_082/_travail/reprise/preparation_rachis/cache/SUIVI2025_EXTRACTION.json');rr=J(rev)['results'][0];s=rr['full_content'];a=s.index('. 2025 Nov 5;5:105865.');z=s.index('\n\n',a);add('dx7-bib-cool2025',s[a:z],'Cool etal. — Identification éditoriale2025',rr['url'],rev,2025)
pa=Path('ChatGPT_Codex/LOT_082/_travail/reprise/EXTRACTION_SCOLIOSE_CH_URO81.json');rr=J(pa)['results'][0];pick('dx7-sia23-risser',rr,'Est généralement évaluée','stades de Risser (0-5) (15,16) .',pa,2023)
# Extrait européen pédiatrique lu pour la correction documentaireDX2.
ep=Path('ChatGPT_Codex/LOT_081/_travail/reprise/correction_DX2/paquet.json')
if ep.exists():d=J(ep)
else:
    import subprocess
    d=json.loads(subprocess.run(['git','show','codex/lot-081:'+str(ep)],check=True,capture_output=True,text=True).stdout)
x=next(x for x in d['passages'] if x['id']=='dx2corr-euneuro-modalite');x=copy.deepcopy(x);x['id']='dx7-euneuro-modalite'
if x['id'] not in sources:pq['passages'].append(x);sources[x['id']]=x

def C(*ids):
    assert all(i in sources for i in ids),[i for i in ids if i not in sources]
    return ''.join(f'<sup class="r"><a href="#sb-{i}">{i}</a></sup>' for i in ids)
def P(t,*ids):return '<div class="p">'+html.escape(t)+C(*ids)+'</div>\n'
def H(t):return '<h4><em>'+html.escape(t)+'</em></h4>\n'
def W(id,t,body):return f'<h4><button class="w" popovertarget="{id}">{html.escape(t)}</button></h4>\n<div id="{id}" popover class="fenetre"><h4>{html.escape(t)}</h4>\n'+body+'</div>\n'
def T(head,rows):
    z='<div class="t" style="overflow-x:auto"><table><thead><tr>'+''.join('<th>'+html.escape(x)+'</th>' for x in head)+'</tr></thead><tbody>\n'
    for row in rows:z+='<tr>'+''.join('<td>'+html.escape(x[0])+C(*x[1:])+'</td>' for x in row)+'</tr>\n'
    return z+'</tbody></table></div>\n'
def reprefix(s):return s.replace('id="dx1-','id="dx7-').replace('popovertarget="dx1-','popovertarget="dx7-')
fr={n:reprefix((O/'fragments'/f'p{n:02d}.html').read_text()) for n in range(1,15)}

fr[1]=P('Dans ses recommandations de 2016 publiées en 2018, SOSORT reprend le critère diagnostique de la Scoliosis Research Society.','dx7-bib-sosort','pa17-sosort-cobb')+fr[1]
fr[2]=H('2.0 La source suisse décrit une population adolescente précise')+P('L’article de Paediatrica publié en 2023 décrit la SIA comme la forme la plus fréquente de scoliose dès l’âge de 10 ans.','p82-scoliose-definition','dx7-bib-paediatrica')+P('Il rapporte davantage de filles et des courbures plus marquées dans cette population, sans comparer les causes de toutes les déformations squelettiques.','p82-scoliose-definition')+P('Le rapport filles-garçons décrit est de 1.4:1 pour les formes bénignes inférieures à 20°, puis de 7:1 au-dessus de 30°.','p82-scoliose-definition')+P('Les estimations de la synthèse internationale sont présentées séparément, car leurs populations et leurs définitions conditionnent les valeurs rapportées.','eu-sosort-2018-5','pa17-sosort-sexe')+fr[2]
fr[6]=H('6.0 La référence rassurante précède la recherche d’une asymétrie')+P('Dans le consensus de radioprotection SOSORT, un examen physique et un scoliomètre normaux ne justifient pas une radiographie initiale de dépistage.','sia82-sos12-normalite')+P('Le clinicien compare d’abord les repères des deux côtés, puis recherche gibbosité, bascule pelvienne, défaut de mobilité et anomalie neurologique.','pa17-ped23-inspection','pa17-ped23-adams','pa17-ped23-mobilite','pa17-ped23-neuro')+fr[6]
fr[6]+=W('dx7-p6-installation','Installer le test d’Adams et conserver le sens de la mesure',P('L’enfant se place de dos, pieds joints et bras ballants, puis se penche en avant avec jambes tendues et mains jointes.','sia82-hug23-geste')+P('Le clinicien observe depuis l’arrière la symétrie, la gibbosité thoracique et le bourrelet lombaire pendant cette flexion active.','pa17-ped23-adams')+P('Le scoliomètre objective un angle de tronc ; cette mesure ne devient donc pas un angle radiographique de Cobb.','prep-dx1-scoliometre','pa17-sosort-cobb'))
fr[6]+=W('dx7-p6-reference-force','Décrire la force avant de nommer un déficit',P('La cotation musculaire situe la force de 0 à 5 ; le niveau 5 représente la force normale dans cette échelle.','oa82-hug-force')+P('Une baisse de force peut accompagner une atteinte musculo-tendineuse, radiculaire ou neuropathique ; sa présence demande donc une interprétation clinique.','oa82-hug-force')+P('Chez l’adolescent scoliotique, la recherche de parésie complète sensibilité, marche et réflexes abdominaux dans l’examen standard.','pa17-ped23-neuro'))
fr[7]+=W('dx7-p7-neurologie','Une parésie ou une anomalie sensitive change la recherche étiologique',P('La parésie correspond à une diminution de force objectivée ; la cotation distingue contraction, mouvement et résistance avant la référence normale.','oa82-hug-force')+P('L’examen de SIA recherche aussi sensibilité, marche, réflexes abdominaux et myoclonies afin de repérer une possible cause secondaire.','pa17-ped23-neuro','prep-sia23-irm')+P('Un trouble sphinctérien nouveau ou un déficit d’alarme ne suit pas le calendrier habituel de surveillance de la courbure.','pa17-lomb22-queue','pa17-lomb22-urgence'))
fr[8]+=W('dx7-p8-risser','Le stade de Risser renseigne une maturité, pas la totalité du risque',P('Le signe de Risser évalue l’ossification de l’apophyse de la crête iliaque sur la radiographie, selon des stades de 0 à 5.','dx7-sia23-risser')+P('La ménarche et les autres paramètres de croissance complètent cette lecture, car le risque évolutif ne dépend pas d’un seul âge civil.','eu-sosort-2018-221','eu-sosort-2018-155'))

altern=H('9.c.1 La modalité et le produit de contraste sont deux décisions distinctes')+T(['Situation','Adaptation de la demande','Condition à conserver'],[
 [('Une exploration intrarachidienne est indiquée chez l’enfant de plus d’un an.','dx7-euneuro-modalite'),('Le consensus européen privilégie l’IRM pour les structures intrarachidiennes.','dx7-euneuro-modalite'),('La radiographie reste initiale pour certaines questions de scoliose, de douleur persistante ou de stabilité.','dx7-euneuro-modalite')],
 [('Une grossesse est connue et une IRM injectée est envisagée.','pa82-esur-gadolinium-grossesse'),('Une indication très forte est nécessaire pour la plus faible dose possible d’un agent macrocyclique.','pa82-esur-gadolinium-grossesse'),('Chez une mère enceinte ou allaitante avec atteinte rénale, ESUR demande de ne pas administrer de produit gadoliné.','pa82-esur-mere-renale')],
 [('Un contraste iodé intravasculaire est envisagé avec un DFGe inférieur à 30 mL/min/1,73 m².','pa82-esur-renal'),('Une méthode sans produit iodé peut être discutée selon la question clinique.','pa82-esur-alternative'),('Ce repère concerne cette exposition au contraste ; il ne devient pas une contre-indication à toute imagerie.','pa82-esur-renal','pa82-esur-alternative')],
 [('Une hypersensibilité antérieure à un produit de contraste est connue.','pa82-esur-hypersensibilite'),('Une modalité alternative ou un examen sans injection peut être retenu si le rendement suffit à la conduite.','pa82-esur-hypersensibilite'),('Le produit responsable et la question clinique sont explicités dans la demande.','pa82-esur-hypersensibilite')],
 [('L’IRM est impossible alors que des signaux neurologiques imposent une exploration urgente.','pa17-lomb22-urgence'),('HUG prévoit au minimum une tomodensitométrie avec avis neurochirurgical sans attendre.','pa17-lomb22-urgence'),('Cette branche urgente ne transforme pas le CT en examen habituel de suivi de SIA.','pa17-lomb22-urgence','prep-dx1-tdm')]
])
fr[9]=fr[9].replace('<h4><em>9.d',altern+'<h4><em>9.d',1)
fr[9]+=H('9.e La synthèse récente sur le suivi reste conditionnelle')+P('La synthèse de 2025 porte sur des SIA suivies par observation radiologique seule ; elle distingue la croissance de la maturité approchée.','dx7-bib-cool2025','sia82-suivi25-resultats')+P('Elle suggère un suivi radiographique tous les six mois jusqu’à l’approche de la maturité, puis un suivi annuel.','sia82-suivi25-conclusion')+P('Cependant, le risque de biais et l’hétérogénéité empêchent une conclusion définitive ; ce calendrier ne remplace pas une adaptation clinique individuelle.','sia82-suivi25-conclusion')

urg=W('dx7-p11-urgence','Urgence — conduite chronologique',P('D’abord, le clinicien identifie déficit d’alarme, rétention, anesthésie en selle ou autres signes neurologiques nouveaux.','pa17-lomb22-queue','pa17-lomb22-urgence')+P('Ensuite, l’équipe organise sans attendre l’imagerie, si possible une IRM, avec avis neurochirurgical ; HUG prévoit au minimum un CT.','pa17-lomb22-urgence')+P('Si le contexte évoque une spondylodiscite ou un abcès épidural, l’IRM suit aussi une filière urgente.','pa17-lomb22-infection','pa17-lomb22-irm-infection')+P('Le suivi morphologique programmé ne retarde aucune de ces actions, car la nouvelle question est neurologique ou infectieuse.','pa17-lomb22-urgence','pa17-lomb22-irm-infection'))
fr[11]=fr[11].replace('<h4><em>11.C',urg+'<h4><em>11.C',1)
fr[11]+=H('11.E La chirurgie est discutée pour certaines courbures majeures')+P('Les HUG décrivent une option chirurgicale pour réaligner le rachis et arrêter la progression de courbures majeures dépassant 40° chez des jeunes en croissance.','dx7-hug-chirurgie')+P('Cette formulation décrit une possibilité de prise en charge spécialisée ; elle ne transforme pas chaque mesure isolée en indication opératoire automatique.','dx7-hug-chirurgie','eu-sosort-2018-155')+P('La fusion utilise notamment un greffon osseux pour réunir des vertèbres dans un angle corrigé.','dx7-hug-fusion')+P('Les HUG proposent aussi, pour certains patients, une modulation de croissance sans fusion vertébrale préservant la mobilité.','dx7-hug-vbt')+P('Pendant l’intervention, le contrôle électrophysiologique surveille la fonction de la moelle épinière et accompagne la correction.','dx7-hug-monitoring')
fr[11]+=W('dx7-p11-complications','Complications opératoires : ce qui doit être signalé',P('Le parcours adolescent décrit un risque d’infection de plaie, de retard de cicatrisation et de douleur supplémentaire persistante.','dx7-nca-complications')+P('Une atteinte nerveuse peut provoquer faiblesse, paresthésies, modification de température ou diminution de sensibilité dans les jambes.','dx7-nca-complications')+P('Une complication apparaissant après la sortie demande un contact avec l’équipe, plutôt qu’une simple attente du rendez-vous prévu.','dx7-nca-alerte'))
fr[11]+=H('11.F Les critères de retour après chirurgie sont vérifiés séparément')+P('Le parcours adolescent britannique conditionne le retour à l’accord de l’équipe, au contrôle de la douleur par voie orale et à une mobilité autonome.','dx7-nca-sortie')+P('Oxford détaille des objectifs fonctionnels avant le départ ; ces repères décrivent ce parcours postopératoire et non chaque SIA observée sans chirurgie.','dx7-oxford-sortie')
fr[11]+=T(['Vérification avant le retour','Constat attendu dans le parcours cité','Interprétation'],[
 [('L’équipe vérifie la douleur.','dx7-nca-sortie'),('Elle est contrôlée par les médicaments oraux prescrits.','dx7-nca-sortie'),('L’accord médical reste une condition distincte de la durée de séjour.','dx7-nca-sortie')],
 [('La marche et les transferts sont testés avec l’entourage.','dx7-oxford-sortie'),('Le jeune peut marcher et utiliser lit, chaise et toilettes avec confiance.','dx7-oxford-sortie'),('La mobilité indépendante peut nécessiter une aide adaptée dans le parcours spécialisé.','dx7-nca-reeducation','dx7-nca-sortie')],
 [('Oxford évalue une marche d’au moins 10 mètres.','dx7-oxford-sortie'),('Le kinésithérapeute contrôle aussi la capacité à monter les escaliers.','dx7-oxford-sortie'),('Cet objectif ne définit pas un seuil universel de guérison radiographique.','dx7-oxford-sortie','eu-sosort-2018-111')],
 [('Le jeune tolère une position assise confortable.','dx7-oxford-sortie'),('Le parcours Oxford demande au moins 30 minutes dans une chaise.','dx7-oxford-sortie'),('Cette tolérance est un objectif fonctionnel après opération.','dx7-oxford-sortie')],
 [('Les consignes sont comprises avec les parents ou aidants.','dx7-oxford-sortie'),('Ils connaissent ce qui est permis ou déconseillé après l’intervention.','dx7-oxford-sortie'),('La préparation du domicile accompagne la récupération.','dx7-oxford-sortie')],
 [('Le suivi est organisé avant de clore l’épisode hospitalier.','dx7-nca-sortie'),('Le parcours cité prévoit une consultation spécialisée après le départ.','dx7-nca-sortie'),('Une nouvelle alarme justifie toutefois un contact avant ce rendez-vous.','dx7-nca-alerte')]
])
fr[11]+=P('Après le retour, l’activité augmente selon douleur et fatigue ; la réhabilitation accompagne la reprise progressive de l’école ou des études.','dx7-oxford-progressivite')
fr[12]=fr[12].replace('12.a La détection précoce conserve une démarche de sélection','12.a La prévention primaire ne se confond pas avec une explication posturale').replace('12.b Le suivi vise la prévention de progression évitable','12.b La prévention secondaire vise détection et progression').replace("12.c L'exposition radiologique est limitée à ce qui aide la décision","12.c La prévention tertiaire limite le retentissement et les risques du suivi")
# Préserver le questionnement sourceM1.3 après les questions complémentaires.
q=re.search(r'<div\b[^>]*id="dx7-question-finale"[^>]*>.*?</div>',fr[14],re.S);assert q
extra=H('14.c Les calendriers et les critères postopératoires gardent leur contexte')+T(['Question','Réponse','Raison'],[
 [('Un contrôle clinique de corset impose-t-il une radiographie à chaque consultation ?','dx1-sia23-corset-controle','eu-sosort-2018-45'),('Non, le suivi clinique et l’acquisition radiographique répondent à des étapes distinctes.','eu-sosort-2018-45','audit-dx1-sia23-radio-corset'),('La croissance, le risque et la question de correction déterminent l’examen utile.','eu-sosort-2018-155','audit-dx1-sia23-radio-corset')],
 [('Le calendrier proposé en 2025 annule-t-il l’adaptation individuelle ?','dx7-bib-cool2025','sia82-suivi25-conclusion'),('Non, la synthèse souligne un risque de biais et une preuve limitée.','sia82-suivi25-conclusion'),('Ses intervalles concernent des patients observés sans autre traitement.','sia82-suivi25-resultats')],
 [('Les objectifs Oxford de sortie s’appliquent-ils à toute SIA dépistée ?','dx7-oxford-sortie'),('Non, ils décrivent le retour après une chirurgie dans ce parcours pédiatrique.','dx7-oxford-sortie'),('Ils ne remplacent pas les indications propres à observation, corset ou chirurgie.','dx7-oxford-sortie','prep-sia23-corset','prep-dx1-observation')]
])
fr[14]=fr[14][:q.start()]+extra+fr[14][q.start():]

c=J(B/'contrat.json')
assert 'dx7-euneuro-modalite' in fr[9]
assert 'id="dx7-p11-urgence"' in fr[11]
for n,s in fr.items():
    ids=sorted(set(re.findall(r'href="#sb-([\w.\-:]+)"',s)));assert set(ids)<=set(sources),(n,set(ids)-set(sources))
    (B/'fragments'/f'p{n:02}.html').write_text(s)
    c['points'][str(n)]['citations_autorisees']=ids
    pq['points'][str(n)]=ids
(B/'contrat.json').write_text(json.dumps(c,ensure_ascii=False,indent=2)+'\n')
(B/'paquet.json').write_text(json.dumps(pq,ensure_ascii=False,indent=2)+'\n')
print('Fragments14 rédigés ; extraits',len(pq['passages']))
