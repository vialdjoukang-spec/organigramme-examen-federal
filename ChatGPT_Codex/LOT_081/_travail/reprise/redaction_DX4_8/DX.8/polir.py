import json
from pathlib import Path
p=Path(__file__).with_name('contenu.json');d=json.loads(p.read_text());r={
'La forme radiographique signifie qu’une sacro-iliite structurale répond au cadre radiographique retenu.':'La forme radiographique correspond à une sacro-iliite structurale qui satisfait le cadre radiographique retenu.',
'Le diagnostic demande':'Le diagnostic exige',
'présente une prévalence':'indique une prévalence',
'HUG présente un délai':'HUG indique un délai',
'Le support HUG relie':'Le support HUG associe',
'Cette réponse implique':'Cette réponse comprend',
'La douleur n’est donc pas un marqueur pur d’inflammation.':'La douleur ne représente donc pas un marqueur pur d’inflammation.',
'La fonction réclame':'La fonction nécessite',
'ASAS–EULAR demande':'ASAS–EULAR recommande',
'Une uvéite nouvelle réclame':'Une uvéite nouvelle exige',
'La sécurité prime sur une augmentation de dose automatique.':'La sécurité doit guider toute décision d’augmentation de dose.',
'La liste médicamenteuse inclut':'La liste médicamenteuse comprend',
'L’inspection compare posture habituelle, courbures, aisance de transfert et marche.':'L’inspection permet de comparer posture habituelle, courbures, aisance de transfert et marche.',
'Le manuel ASAS présente':'Le manuel ASAS décrit et recommande',
'Cette démarche s’intègre à la filière urgente':'Cette démarche relève de la filière urgente',
'Leur concordance au calcanéum, à l’insertion achilléenne ou plantaire, complète l’argumentaire clinique.':'Leur concordance au calcanéum, à l’insertion achilléenne ou plantaire, constitue un argument clinique complémentaire.',
'La douleur fessière alternante change de côté au cours de l’histoire.':'La douleur fessière alternante est une douleur qui change de côté au cours de l’histoire.',
'La recommandation actuelle insiste sur':'La recommandation actuelle rappelle',
'L’échec conventionnel inclut':'L’échec conventionnel comprend',
'Le spectre inclut':'Le spectre comprend',
'La répétition routinière de l’IRM n’est pas recommandée pour surveiller tous les patients.':'La surveillance ne doit pas comporter systématiquement une IRM répétée chez tous les patients.',
'Un HLA positif ou un œdème isolé ne clôt pas cette étape.':'Un HLA positif ou un œdème isolé ne suffit pas pour clore cette étape.',
'la décision inclut':'la décision comprend',
'Leur usage continu dépend du besoin symptomatique.':'Leur usage continu repose sur le besoin symptomatique.',
'l’AIPS demande':'l’AIPS recommande',
'Sous Celebrex, surveiller la tolérance digestive et éviter l’association avec un autre AINS.':'Sous Celebrex, on surveille la tolérance digestive et on évite l’association avec un autre AINS.',
'Le suivi apprécie':'Le suivi contrôle',
'L’arrêt complet systématique n’est pas recommandé en raison du risque de rechute.':'Le risque de rechute ne justifie pas un arrêt complet systématique.',
'Un test isolé n’est pas présenté comme verdict définitif.':'Un test isolé ne constitue pas un verdict définitif.',
'La décision d’IRM et/ou de scanner répond au risque mécanique actuel.':'La décision d’IRM et/ou de scanner vise le risque mécanique actuel.',
'Une fois ces problèmes évalués, le parcours de fond reprend sur diagnostic vérifié, activité documentée et moyens conventionnels adaptés.':'Une fois ces problèmes évalués, le parcours de fond repose sur un diagnostic vérifié, une activité documentée et des moyens conventionnels adaptés.',
'La surveillance intègre':'La surveillance comprend',
'La prévention médicamenteuse inclut':'La prévention médicamenteuse comprend'}
for point in d['points'].values():
 for items in [i for _,i in point['blocs']+point['fenetres']]+[row for _,_,rows in point['tableaux']for row in rows]:
  for x in items:
   for a,b in r.items():x[1]=x[1].replace(a,b)
   if x[1].startswith('Les traitements ciblant TNF'):x[0]+='+b1'
d['points']['1']['blocs'][0][0]='Définition ASAS–EULAR 2022 : spectre axial sans ankylose obligatoire'
d['points']['2']['blocs'][0][0]='Repères HUG 2023 et limites épidémiologiques'
d['points']['11']['blocs'][0][0]='11.A — Objectifs ASAS–EULAR 2022, précisés par BSR 2025'
d['points']['11']['blocs'][-2][0]='11.C — Surveillance AIPS et recommandations BSR 2025'
p.write_text(json.dumps(d,ensure_ascii=False,indent=1)+'\n')
