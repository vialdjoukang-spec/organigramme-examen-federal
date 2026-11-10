from rendu import Point
p=Point(2)
p.h('Lire la fréquence avec sa population de référence')
p.p('En Suisse, les syndromes grippaux constituent un contexte courant de douleurs musculaires pendant la saison froide ; leur poids varie avec les vagues épidémiques.', 'p83-grippe')
p.p('L’OFSP estime que la grippe entraîne chaque année entre 50 000 et 250 000 consultations médicales en Suisse, selon la surveillance Sentinella.', 'p83-grippe')
p.p('Ce volume décrit le recours aux soins pour la grippe ; il situe cette infection dans son contexte saisonnier.', 'p83-grippe')
p.p('La DGN décrit le syndrome myofascial comme la forme la plus fréquente de douleur musculaire localisée, et la fibromyalgie comme la plus fréquente dans le cadre généralisé.', 'p83-myofascial-fibro')
p.p('La distinction entre ces cadres s’appuie donc sur la répartition et la durée des symptômes avant de rechercher leur étiologie.', ['pa83-anamnese','p83-myofascial-fibro'])
p.tableau(['Situation et population','Repère de fréquence','Portée clinique'],[
 [('La grippe est surveillée dans la population suisse.', 'p83-grippe'),('Elle motive environ 50 000 à 250 000 consultations annuelles.', 'p83-grippe'),('La vague hivernale replace les myalgies fébriles dans un contexte épidémique.', 'p83-grippe')],
 [('La Ligue suisse contre le rhumatisme présente une estimation mondiale de fibromyalgie.', 'p83-fibro-frequence'),('Cette estimation concerne entre 2 et 4 % de la population mondiale.', 'p83-fibro-frequence'),('Le tableau concerne surtout les adultes jeunes et d’âge moyen.', 'p83-fibro-frequence')],
 [('Les douleurs localisées et généralisées forment deux cadres cliniques distincts.', 'p83-myofascial-fibro'),('Le myofascial domine le premier cadre et la fibromyalgie le second dans la recommandation DGN.', 'p83-myofascial-fibro'),('La description du patient choisit le cadre de comparaison.', ['pa83-anamnese','p83-myofascial-fibro'])],
 [('Les effets musculaires médicamenteux forment un autre groupe de comparaison.', 'p83-statine-frequence'),('Les statines occupent la première place dans ce groupe selon la DGN.', 'p83-statine-frequence'),('L’exposition et les symptômes orientent l’évaluation de causalité.', 'p83-statine-frequence')]
])
p.fenetre('Âge, sexe et terrain : modifier la vigilance',[
 ('La fibromyalgie est plus souvent rapportée chez les femmes ; la Ligue suisse indique une fréquence deux à cinq fois supérieure à celle des hommes.', 'p83-fibro-frequence'),
 ('Elle peut aussi survenir chez l’enfant ou l’adolescent, mais ces cas sont décrits comme rares dans cette même source.', 'p83-fibro-frequence'),
 ('La pseudopolyarthrite rhizomélique concerne surtout les personnes plus âgées et touche préférentiellement les femmes.', 'p83-pmr'),
 ('Une douleur inflammatoire des ceintures dans ce terrain appelle une enquête spécifique, notamment sur les symptômes crâniens et visuels.', ['p83-pmr','p83-eular26-signes-urgence']),
 ('La grossesse, la prématurité, l’âge avancé et certaines maladies chroniques augmentent le risque de complications de la grippe.', 'p83-grippe'),
 ('Les personnes âgées peuvent présenter une grippe sans fièvre ; la température isolée ne décrit donc pas toute leur présentation.', 'p83-grippe')
])
p.h('Effort et évolution : interpréter la chronologie')
p.p('Les efforts inhabituels, notamment excentriques, sont associés aux courbatures retardées ; la douleur survient après un intervalle initial peu symptomatique.', 'doms-mecanisme')
p.p('La revue européenne sur les courbatures décrit un début entre 6 et 12 heures après l’exercice et un maximum entre 48 et 72 heures.', 'doms-mecanisme')
p.p('La guérison habituelle intervient dans la semaine, tandis que la charge doit rester adaptée à l’état fonctionnel et au niveau d’entraînement.', ['doms-mecanisme','doms-prevention'])
p.p('L’effort est aussi un déclencheur de rhabdomyolyse chez des personnes jusque-là en bonne santé, notamment après une reprise d’activité intense.', 'e02')
p.p('La présentation et les complications différencient alors l’adaptation à l’effort d’un épisode pathologique ; le taux de CK s’interprète dans cet ensemble.', 'e13')
p.fenetre('Une histoire naturelle ne remplace pas le triage',[
 ('L’apparition de douleurs après le sport ne suffit pas à classer l’épisode parmi les courbatures lorsque des signes généraux ou une complication sont présents.', ['p83-doms-contusion-clinique','e13']),
 ('Dans la rhabdomyolyse, le risque rénal et les perturbations métaboliques donnent leur importance immédiate à l’évaluation.', ['p83-rhabdo-menace','e13']),
 ('Des épisodes répétés ou inexpliqués orientent vers une recherche génétique ou neuromusculaire, afin d’adapter la prise en charge et la prévention.', 'e14'),
 ('La fibromyalgie suit au contraire une évolution douloureuse chronique qui justifie une stratégie individuelle et multimodale.', ['p83-myofascial-fibro','pa83-fibro-soins']),
 ('Une faiblesse objectivée, une atrophie ou une élévation des CK conduit à rechercher une autre atteinte ou une affection associée.', 'p83-myofascial-fibro')
])
p.h('Conséquences pour la santé et les soins')
p.p('Les complications grippales causent en Suisse plusieurs milliers d’hospitalisations et fréquemment plusieurs centaines de décès, surtout sur les terrains les plus exposés.', 'p83-grippe')
p.p('Les myopathies inflammatoires immunomédiées sont rares ; leur pronostic dépend notamment des atteintes respiratoires, cardiaques, œsophagiennes et néoplasiques associées.', ['p83-myopathies-inflammatoires','p83-myopathies-gravite'])
p.p('La douleur chronique diffuse nécessite un accompagnement centré sur les ressources de la personne et sur l’autogestion, avec des soins adaptés à son retentissement.', 'pa83-fibro-soins')
p.p('Après une rhabdomyolyse, le suivi doit également prendre en compte les séquelles physiques et psychologiques et organiser la réadaptation.', 'e15')
p.sauver()
