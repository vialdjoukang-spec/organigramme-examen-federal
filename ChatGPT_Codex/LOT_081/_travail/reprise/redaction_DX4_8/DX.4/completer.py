import json,re
from pathlib import Path
D=Path(__file__).parent;B=D.parents[1];p=json.loads((D/'paquet.json').read_text());general=json.loads((B/'AIPS_HUG2022/PAQUET_AIPS_CONDITIONNEL.json').read_text());old=json.loads(Path('ChatGPT_Codex/LOT_080/_travail/reprise/redaction_DX4_7/DX.6/paquet.json').read_text());ids={x['id']for x in p['passages']}
selected=[x for x in general['passages']if x['id'].startswith('aips81-tramal') or x['id'].startswith('aips81-dafalgan')]+[x for x in old['passages']if x['id'] in ['ch-fracture-2023-detail-1','ch-svgo-2026-detail-1']]
for x in selected:
 if x['id']not in ids:p['passages'].append(x)
(D/'paquet.json').write_text(json.dumps(p,ensure_ascii=False,indent=1)+'\n')
c=json.loads((D/'contenu.json').read_text());R=c['references'];R.update({'f1':'ch-fracture-2023-detail-1','v1':'ch-svgo-2026-detail-1'})
def block(title,txt):return [title,[x.split('|',1)for x in txt.strip().splitlines()]]
c['points']['11']['blocs'].insert(3,block('Antalgie de la fracture : options adultes et surveillance AIPS', '''f2+f31|La directive suisse prévoit une antalgie graduée et une mobilisation adaptée. L’effet recherché est une reprise fonctionnelle sûre ; une douleur persistante malgré traitement impose aussi de réexaminer la fracture.
aips81-dafalgan-4+aips81-dafalgan-17+aips81-dafalgan-20|Dafalgan® est documenté pour les douleurs faibles à modérées, notamment dorsales ou après blessure. L’AIPS de juillet 2026 porte les autorisations Swissmedic 47503, 47505 et 56318 selon présentation.
aips81-dafalgan-5|Pour les comprimés effervescents à 500 mg, l’AIPS indique chez l’adulte de plus de 40 kg une prise de 500 à 1'000 mg. L’intervalle entre prises est de 4 à 8 heures chez l’adulte ; le maximum quotidien est de 4 g.
aips81-dafalgan-5|Ce maximum concerne le paracétamol total de toutes les préparations prises. Il faut donc rechercher les associations qui contiennent déjà cette molécule avant de rédiger une nouvelle ordonnance.
aips81-dafalgan-5|En cas de maladie hépatique chronique ou compensée active, d’alcoolisme chronique, de déficit alimentaire, de déshydratation ou de cachexie, l’AIPS demande une adaptation. La dose quotidienne ne doit alors pas dépasser 2 g.
aips81-dafalgan-5|Pour une clairance de 10 à 50 mL/min, l’intervalle est de 6 heures et le maximum de 3000 mg/jour. En dessous de 10 mL/min, l’intervalle est de 8 heures et le maximum de 2000 mg/jour.
aips81-dafalgan-6|Dafalgan est contre-indiqué notamment en cas de trouble hépatique grave, hépatite aiguë, maladie hépatique décompensée active ou maladie de Gilbert. Ces restrictions doivent être vérifiées avant de présenter le paracétamol comme anodin.
aips81-dafalgan-7-p8+aips81-dafalgan-7-p13|Un surdosage expose à une lésion hépatique grave, parfois initialement peu symptomatique. Il faut agir dès la suspicion et éviter l’alcool pendant le traitement, particulièrement si le patient est dénutri.
aips81-dafalgan-9|Pendant la grossesse, le paracétamol peut être utilisé en cas de nécessité clinique, à dose minimale efficace, durée la plus courte et fréquence la plus basse. Son utilisation est considérée compatible avec l’allaitement, avec prudence.
aips81-tramal-5+aips81-tramal-18+aips81-tramal-21|Tramal® peut être envisagé pour une douleur moyenne à forte ou si les non-opioïdes sont insuffisants. L’AIPS d’avril 2025 porte les autorisations 40858, 40859, 43787 et 43788 selon présentation.
aips81-tramal-6|Pour les capsules de Tramal à 50 mg, l’AIPS adulte indique 50 à 100 mg par voie orale toutes les 4 à 6 heures. La dose efficace la plus faible est choisie ; le total de 400 mg par jour ne doit pas être dépassé hors circonstances particulières.
aips81-tramal-6|La durée et les objectifs sont convenus avant traitement, puis réévalués par des contacts réguliers. Tramal n’est pas utilisé plus longtemps qu’absolument nécessaire ; une diminution progressive peut éviter le sevrage lors de l’arrêt.
aips81-tramal-6|L’insuffisance rénale ou hépatique ralentit l’élimination ; l’intervalle entre doses peut devoir être prolongé. Après 75 ans, l’élimination peut aussi ralentir même sans insuffisance rénale ou hépatique cliniquement manifeste.
aips81-tramal-7|Tramal est contre-indiqué avec un inhibiteur de la MAO actuel ou reçu dans les 14 jours précédents. Il est aussi contre-indiqué en cas d’épilepsie insuffisamment contrôlée ou d’intoxication aiguë par alcool et autres dépresseurs cités dans l’AIPS.
aips81-tramal-8-p5+aips81-tramal-8-p9|La surveillance recherche particulièrement sédation et dépression respiratoire, surtout à l’instauration ou après augmentation. Les benzodiazépines et autres dépresseurs centraux majorent le risque ; une association demande une justification et une surveillance étroite.
aips81-tramal-8-p26+aips81-tramal-8-p28+aips81-tramal-8-p31|Le tramadol expose aussi aux convulsions et au syndrome sérotoninergique, notamment avec des traitements associés. Devant une suspicion de syndrome sérotoninergique, réduire ou arrêter selon la gravité et organiser la prise en charge appropriée.
aips81-tramal-10|Tramal ne doit pas être utilisé pendant la grossesse sauf nécessité absolue. Il ne doit pas être administré pendant l’allaitement ; l’AIPS précise toutefois qu’une administration unique n’impose généralement pas d’interrompre celui-ci.
aips81-tramal-6+f31|Si l’escalade antalgique ne permet pas la mobilisation, rechercher une progression de la maladie ou une complication mécanique. Augmenter l’opioïde sans réexaminer la fracture peut retarder la décision utile.'''))
c['points']['11']['tableaux'].append(['Antalgiques : ne pas confondre dose maximale et dose à viser',['Spécialité','Posologie AIPS adulte','Durée et sécurité'],[
[['aips81-dafalgan-17+aips81-dafalgan-20','Dafalgan® ; Swissmedic 47503/47505/56318, AIPS juillet 2026.'],['aips81-dafalgan-5','Effervescent 500 mg, adulte de plus de 40 kg : 500 à 1\'000 mg par prise, intervalle 4 à 8 h, maximum 4 g/jour hors adaptations.'],['aips81-dafalgan-5+aips81-dafalgan-6','Réévaluer selon évolution et terrain ; réduire selon facteurs hépatiques ou rénaux, éviter tout cumul de paracétamol.']],
[['aips81-tramal-18+aips81-tramal-21','Tramal® ; Swissmedic 40858/40859/43787/43788, AIPS avril 2025.'],['aips81-tramal-6','Capsules : 50–100 mg PO toutes les 4–6 h ; dose efficace minimale, maximum habituel 400 mg/jour.'],['aips81-tramal-6+aips81-tramal-8-p5','Durée minimale nécessaire, objectifs convenus, réévaluation régulière ; surveiller sédation et respiration.']]]])
for point in c['points'].values():
 groups=[items for _,items in point['blocs']+point['fenetres']]+[row for _,_,rows in point['tableaux'] for row in rows]
 for items in groups:
  for item in items:
   item[1]=item[1].replace('1 537','mille cinq cent trente-sept')
   if '2026' in item[1] and 'SVGO' in item[1]:item[0]+='+v1'
   if '2023' in item[1]:item[1]=item[1].replace('2023','deux mille vingt-trois')
   if 'version 1.1 du 12 juin' in item[1]:item[1]=item[1].replace('version 1.1 du 12 juin deux mille vingt-trois','version 1.1 du 12.06.2023');item[0]+='+f1'
(D/'contenu.json').write_text(json.dumps(c,ensure_ascii=False,indent=1)+'\n')
