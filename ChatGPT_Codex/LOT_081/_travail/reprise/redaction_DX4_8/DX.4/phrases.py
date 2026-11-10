import json,re
from pathlib import Path
p=Path(__file__).with_name('contenu.json');d=json.loads(p.read_text())
rep={
'L’âge augmente nettement cette incidence : les valeurs rapportées chez les femmes passent de 121 pour cent mille à 50 ans à mille cinq cent trente-sept pour cent mille entre 80 et 85 ans.':'L’incidence rapportée chez les femmes est de 121 pour cent mille à 50 ans. Elle atteint mille cinq cent trente-sept pour cent mille entre 80 et 85 ans.',
'douloureuse. un patient':'douloureuse. Un patient',
'Cette conciliation est nécessaire avant Aclasta : la déshydratation et les associations susceptibles d’altérer le rein augmentent le risque, et le même principe actif ne doit pas être administré sous deux spécialités simultanément.':'Cette conciliation est nécessaire avant Aclasta, car la déshydratation et certaines associations augmentent le risque rénal. En outre, le même principe actif ne doit pas être administré sous deux spécialités simultanément.',
'Une anamnèse néoplasique et des symptômes B doivent être signalés au radiologue et au spécialiste : une compression ou une fracture tumorale ne suit pas le même parcours qu’une fracture de fragilité habituelle.':'Une anamnèse néoplasique et des symptômes B doivent être signalés au radiologue et au spécialiste. En effet, une fracture tumorale ne suit pas le même parcours qu’une fracture de fragilité habituelle.',
' ; dans cette situation clinique,':' . Dans cette situation clinique,',
' ; ce test fonctionnel n’est pas une preuve spécifique de fracture.':'. Toutefois, ce test fonctionnel ne constitue pas une preuve spécifique de fracture.',
' ; la sensibilité profonde':'. La sensibilité profonde',
'→ rechercher immédiatement une compression neurologique, documenter l’examen, obtenir une IRM si possible ou au minimum un scanner et un avis neurochirurgical.':'→ rechercher immédiatement une compression neurologique. On documente l’examen, puis on organise l’IRM si possible ou au minimum un scanner et un avis neurochirurgical.',
' ; si l’IRM manque,':'. Si l’IRM manque,',
' ; discuter la stratégie avec le patient.':'. On discute ensuite la stratégie avec le patient.',
' ; une intervention locale réussie':'. Une intervention locale réussie',
' ; SI autre catégorie de risque':'. SI autre catégorie de risque',
'Le but osseux de long terme est distinct : SVGO 2026 propose au minimum un T-score de hanche supérieur à −2,5 lorsque la densité initiale pertinente est au plus −2,5, et préfère une cible supérieure à −2,0 chez certains patients à haut risque persistant.':'Le but osseux de long terme est distinct. SVGO 2026 propose un T-score de hanche supérieur à −2,5 lorsque la densité initiale pertinente est au plus −2,5. Une cible supérieure à −2,0 est préférée chez certains patients à haut risque persistant.',
'ont une orientation effective : une neurocompression':'ont une orientation effective. Ainsi, une neurocompression',
' ; le seul chiffre de VAS':'. Le seul chiffre de VAS',
' ; le patient sait':'. Le patient sait',
'la directive suisse demande de traiter':'la directive suisse recommande de traiter'}
for point in d['points'].values():
 for items in [i for _,i in point['blocs']+point['fenetres']]+[r for _,_,rs in point['tableaux']for r in rs]:
  for x in items:
   for a,b in rep.items():x[1]=x[1].replace(a,b)
   x[1]=x[1].replace(' . ','. ')
p.write_text(json.dumps(d,ensure_ascii=False,indent=1)+'\n')
p=Path(__file__).parents[1]/'rendre.py';s=p.read_text().replace("sentences=re.split(r'(?<=[.!?])\\s+(?=[A-ZÀ-Ý«])',item[1])", "sentences=re.findall(r'.+?(?:[.!?](?:\\s*»)?(?=\\s+[A-ZÀ-Ý«])|$)',item[1])")
p.write_text(s)
