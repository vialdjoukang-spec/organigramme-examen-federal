import json
def s(i): return f'<sup class="r"><a href="#sb-{i}">{i}</a></sup>'
C=[]
def c(a,b): C.append({"avant":a,"apres":b})
c("<tr><td>Paracétamol seul</td><td>Paracétamol</td><td>Voir l'information professionnelle de la préparation prescrite</td><td>Orale</td><td>Courte durée</td><td>Selon préparation</td></tr>",
  f"<tr><td>Dafalgan® comprimés 500 mg</td><td>Paracétamol</td><td>Adulte de plus de 40 kg : jusqu'à 4 x 1 à 2 comprimés par jour, maximum 4000 mg par jour, intervalle de 4 à 8 h entre les prises {s('aips-46206-3')}{s('aips-46206-4')}</td><td>Orale</td><td>Pas de durée fixée chez l'adulte ; 3 jours au plus sans avis médical chez l'enfant jusqu'à 12 ans {s('aips-46206-3')}</td><td>46206</td></tr>")
c("<tr><td>Décongestionnant nasal local</td><td>Xylométazoline ou autre</td><td>Voir l'information professionnelle de la préparation</td><td>Nasale</td><td>5 jours au plus</td><td>Selon préparation</td></tr>",
  f"<tr><td>Otrivin Rhume</td><td>Xylométazoline</td><td>Dès 12 ans : 1 pulvérisation dans chaque narine, à répéter si besoin, au plus 3 applications par jour ; préparation interdite avant 12 ans {s('aips-58857-2')}</td><td>Nasale</td><td>Pas plus d'une semaine, sinon rhinite médicamenteuse {s('aips-58857-2')}</td><td>58857</td></tr>")
c(" Un test négatif ne l'exclut pas si la clinique est évocatrice et si l'épidémie est en cours "+s('aips-55196-19')+".","")
c("Enfin, isoler le patient en cas de grippe ou de COVID suspecte et informer l'équipe, puisque la transmission est surtout hospitalière "+s('we19809-9'),
  "Enfin, isoler le patient en cas de grippe ou de COVID suspecte et informer l'équipe, car les hôpitaux et les institutions de soins sont des endroits à risque élevé de contagion "+s('we19809-9'))
c("Pour l'allaitement, on dispose de très peu d'informations sur les enfants allaités par une mère prenant de l'oseltamivir "+s('aips-55196-31')+".",
  "Pour l'allaitement, l'oseltamivir passe dans le lait maternel, et son emploi peut être envisagé seulement s'il apporte un effet bénéfique indiscutable à la femme allaitante "+s('aips-55196-31')+".")
c("<li>Si une méningite est suspectée, organiser un transfert hospitalier immédiat, car chaque délai aggrave le pronostic.</li>\n","")
c("La pneumonie communautaire constitue le premier piège.","La pneumonie communautaire (E2) constitue le piège le plus fréquent, mais l'embolie pulmonaire (E1) se cherche en premier.")
c("<tr><td>Pneumonie communautaire 🚩 E2</td><td>Foyer auscultatoire, dyspnée, fièvre persistante, radiographie</td><td>Signes discrets chez la personne âgée</td><td>Radiographie du thorax, antibiothérapie selon la gravité</td></tr>\n<tr><td>Embolie pulmonaire 🚩 E1</td><td>Probabilité clinique, D-dimères, angioscanner</td><td>Toux et fièvre modérée chez un patient avec rhume apparent</td><td>Anticoagulation immédiate si probabilité élevée</td></tr>",
  "<tr><td>Embolie pulmonaire 🚩 E1</td><td>Probabilité clinique, D-dimères, angioscanner</td><td>Toux et fièvre modérée chez un patient avec rhume apparent</td><td>Anticoagulation immédiate si probabilité élevée</td></tr>\n<tr><td>Pneumonie communautaire 🚩 E2</td><td>Foyer auscultatoire, dyspnée, fièvre persistante, radiographie</td><td>Signes discrets chez la personne âgée</td><td>Radiographie du thorax, antibiothérapie selon la gravité</td></tr>")
c("Entre 10 et 30 ml/min, la posologie recommandée est de 30 mg 1x par jour pendant 5 jours "+s('aips-55196-10')+".",
  "Entre 10 et 30 ml/min, la posologie recommandée est de 30 mg 1x par jour pendant 5 jours ; sous dialyse régulière, une dose de 30 mg se donne avant la dialyse puis après chaque séance "+s('aips-55196-10')+".")
c("<tr><td>D-dimères (&lt; 500 µg/l)</td><td>Normaux avec probabilité faible</td><td>Embolie exclue</td><td>Aucune imagerie</td></tr>","")
c("Le score de Centor modifié aide en revanche à décider du test streptococcique devant un mal de gorge, et les critères de gravité de la pneumonie guident l'hospitalisation. Ces scores répondent à d'autres questions que le diagnostic de rhume, mais ils servent à écarter un diagnostic alternatif.","")
c(" Par ailleurs, chez les patients immunodéprimés de 1 an ou plus, une prophylaxie pouvant aller jusqu'à 12 semaines est recommandée en cas de risque important de contagion "+s('aips-55196-13')+".","")
c(" Si une radiographie thoracique est nécessaire pour exclure une pneumonie, elle se pratique avec protection de l'abdomen, car le bénéfice diagnostique dépasse le risque.","")
json.dump(C,open('Claude/LOT_045/_travail/DX.1/corrections.json','w'),ensure_ascii=False,indent=1)
