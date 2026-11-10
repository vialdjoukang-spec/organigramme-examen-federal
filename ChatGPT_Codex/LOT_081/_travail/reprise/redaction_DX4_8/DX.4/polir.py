import json
from pathlib import Path
p=Path(__file__).with_name('contenu.json');d=json.loads(p.read_text())
rep={
'le type OF1 présente':'le type OF1 montre',
'L’ostéoporose désigne':'L’ostéoporose représente',
'Œdème STIR : signal permettant de reconnaître une lésion vertébrale récente dans le contexte approprié ; le nom de la séquence n’est ni un diagnostic étiologique autonome ni un score de stabilité.':'L’œdème STIR est un signal qui aide à reconnaître une lésion vertébrale récente. Cependant, la séquence ne constitue ni un diagnostic étiologique autonome ni un score de stabilité.',
'dépend du niveau de risque':'repose sur le niveau de risque',
'La classification OF relie ainsi':'La classification OF associe ainsi',
'HUG, stratégie de deux mille vingt-deux demande':'La stratégie HUG de deux mille vingt-deux recommande',
'Une douleur irradiée radiculaire demande':'Une douleur irradiée radiculaire nécessite',
'L’examen de la fracture documente':'L’examen de la fracture précise',
'Prendre les constantes, dont la température, puis observer':'On mesure les constantes, dont la température, puis on observe',
'Tester la flexion':'On recherche la force en flexion',
'Pour l’achilléen, percuter':'Pour l’achilléen, on percute',
'Examiner la sensibilité':'On recherche les anomalies de sensibilité',
'Terminer en documentant':'On précise finalement',
'n’est pas une description neurologique suffisante':'ne constitue pas une description neurologique suffisante',
'Leur association motive':'Leur association justifie',
'Cyphose postfracturaire : déformation sagittale pouvant résulter de la perte de hauteur.':'La cyphose postfracturaire correspond à une déformation sagittale liée à la perte de hauteur.',
'Anesthésie en selle : perte de sensation':'L’anesthésie en selle correspond à une perte de sensation',
'Fièvre nouvelle : température augmentée apparue avec l’épisode ou dans son évolution, à mesurer et à situer dans la chronologie.':'La fièvre nouvelle correspond à une température augmentée avec l’épisode ou dans son évolution. On la mesure et on précise sa chronologie.',
'Symptômes B : signes généraux évoqués dans l’alerte néoplasique du support HUG.':'Le support HUG indique des symptômes B parmi les alertes néoplasiques.',
'La directive suisse demande':'La directive suisse recommande',
'l’IRM explore':'l’IRM montre',
'Avant chaque dose, calculer la clairance selon Cockcroft-Gault, corriger l’hypocalcémie et assurer une hydratation convenable.':'Avant chaque dose, on calcule la clairance selon Cockcroft-Gault. On corrige aussi l’hypocalcémie et on assure une hydratation convenable.',
'L’AIPS ne demande pas':'L’AIPS ne recommande pas',
'Cette précision ne supprime pas':'Cette précision ne remplace pas',
'Le pronostic dépend de':'Le pronostic repose sur',
'D’abord, reconnaître et documenter':'D’abord, on recherche et on précise',
'Ne pas laisser une explication présumée ostéoporotique retarder cette première décision.':'Une explication présumée ostéoporotique ne doit pas retarder cette première décision.',
'Ensuite, déclencher':'Ensuite, on déclenche',
'Une augmentation cimentaire isolée n’est pas présentée comme réponse automatique à toute compression.':'Une augmentation cimentaire isolée ne constitue pas une réponse automatique à toute compression.',
'Une fois les urgences évaluées, stabiliser la stratégie symptomatique et vérifier la mobilisation sous antalgie.':'Une fois les urgences évaluées, on précise la stratégie symptomatique et on contrôle la mobilisation sous antalgie.',
'Enfin, engager':'Enfin, on organise',
'place les mesures de mode de vie':'recommande les mesures de mode de vie',
'Organisez la prévention secondaire pour chaque fracture de fragilité et adaptez l’intensité au risque de récidive.':'La prévention secondaire doit suivre chaque fracture de fragilité avec une intensité adaptée au risque de récidive.',
'Avant chaque Aclasta, calculez la clairance et respectez la contre-indication en dessous de 35 mL/min.':'Chaque Aclasta exige le calcul préalable de clairance et reste contre-indiqué en dessous de 35 mL/min.',
'« Avez-vous eu fièvre, frissons, infection urinaire ou cutanée, injection ou chirurgie récente du dos ?':'« Une fièvre, des frissons ou une infection ont-ils précédé cet épisode ? Une injection ou une chirurgie récente concerne-t-elle le dos ?',
'« Avez-vous été traité pour un cancer ?':'« Votre histoire comprend-elle un cancer traité ?',
' ; elles ne constituent pas':' . Elles ne constituent pas',
'La directive demande donc d’apprécier non seulement une intensité douloureuse, mais la mobilisation sous traitement :':'La directive recommande donc d’apprécier la mobilisation sous traitement au-delà de l’intensité douloureuse.',
'L’existence de séries favorables à l’augmentation vertébrale ne permet pas de promettre un bénéfice de survie individuel : les études et recommandations sont hétérogènes, et les comparaisons observationnelles restent exposées aux différences de sélection des patients.':'Les séries favorables à l’augmentation vertébrale ne permettent pas de promettre un bénéfice de survie individuel. En effet, les comparaisons observationnelles restent exposées aux différences de sélection des patients.',
'Leur présence conduit à préciser la plainte générale et son évolution puis à orienter le bilan ; ils ne sont pas un score de malignité et ne dispensent pas de l’histoire oncologique détaillée.':'Leur présence conduit à préciser la plainte générale puis à orienter le bilan. Toutefois, ils ne constituent pas un score de malignité et ne remplacent pas l’histoire oncologique.',
'Les critères suivants constituent une synthèse opérationnelle de sécurité à documenter pour envisager la sortie, fondée sur les domaines de décision de la directive ; ils ne sont pas présentés comme une grille suisse de sortie validée ou un score à additionner.':'Les critères suivants constituent une synthèse opérationnelle fondée sur les domaines de décision de la directive. Cependant, ils ne représentent ni une grille suisse de sortie validée ni un score à additionner.',
'La guérison clinique attendue associe amélioration de la douleur et récupération de mobilité, avec une évolution morphologique jugée satisfaisante par l’équipe ; un délai unique de guérison ne peut pas être promis à partir de ces sources.':'La guérison clinique attendue associe amélioration douloureuse, récupération de mobilité et évolution morphologique satisfaisante pour l’équipe. Toutefois, ces sources ne permettent pas de promettre un délai unique de guérison.',
'Cette démarche répond au défaut de prévention secondaire décrit en Suisse : le nombre important de fractures et leur retentissement justifient d’organiser le suivi dès l’épisode clinique, plutôt que de laisser au patient seul la tâche de rouvrir le dossier osseux.':'Le nombre important de fractures et leur retentissement justifient donc un suivi organisé dès l’épisode clinique. Cette démarche vise le défaut de prévention secondaire décrit en Suisse.'}
for point in d['points'].values():
 for items in [i for _,i in point['blocs']+point['fenetres']]+[r for _,_,rs in point['tableaux'] for r in rs]:
  for x in items:
   for a,b in rep.items():x[1]=x[1].replace(a,b)
p.write_text(json.dumps(d,ensure_ascii=False,indent=1)+'\n')
