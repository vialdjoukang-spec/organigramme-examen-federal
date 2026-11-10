from rendu import Point
p=Point(12)
p.h('Prévention primaire : agir sur les déclencheurs évitables')
p.p('Une progression lente de la charge selon le niveau d’entraînement limite le risque de courbatures après effort inhabituel. La revue2024 souligne l’adaptation du muscle ; une séance brutalement intensifiée ne devient pas sûre par l’ajout d’une intervention de récupération.', 'doms-prevention')
p.p('Le consensus ENMC2025 conseille hydratation et nutrition appropriées et maîtrise des facteurs favorisant la rhabdomyolyse : efforts non habituels, contractions excentriques exigeantes, chaleur et humidité, infection précédant l’exercice et médicaments modifiant la thermorégulation. L’information doit porter sur la combinaison réelle de ces facteurs.', 'e15')
p.p('La prévention de la grippe contribue à prévenir une cause infectieuse de myalgies. L’OFSP2026 recommande la vaccination à partir de la mi-octobre jusqu’au début de la vague et maintient les groupes cibles des années précédentes.', ['f5-9','f5-12'])
p.fenetre('Groupes suisses de vaccination et protection de l’entourage',[
 ('La page OFSP cite les personnes de plus de65ans, les femmes enceintes, les prématurés jusqu’à2ans et les personnes atteintes de maladies chroniques. Les contacts réguliers, les proches et le personnel soignant contribuent aussi à leur protection par la vaccination.', 'f5-10'),
 ('Pour les personnes d’au moins75ans, ainsi que celles d’au moins65ans ayant un facteur supplémentaire, l’OFSP privilégie un vaccin à haute dose. Le produit et sa prescription relèvent de son indication propre, pas d’une dose déduite de la plainte musculaire.', 'f5-13'),
 ('La recommandation2026 inclut aussi les personnes en contact régulier avec les volailles ou les oiseaux sauvages. La vaccination influenza ne protège ni contre le COVID-19 ni contre l’ensemble des refroidissements.', 'f5-12')
])
p.h('Prévention secondaire : reconnaître une évolution qui change la conduite')
p.p('Une surveillance précoce évite de banaliser les urines sombres ou l’anurie, la douleur disproportionnée d’une loge et les manifestations crâniennes associées aux douleurs de ceinture. Chacune ouvre une filière urgente différente plutôt qu’une simple augmentation d’antalgique.', ['e13','p83-boast-loges-0','p83-eular26-orientation'])
p.p('Sous statine, l’apparition de crampes, faiblesse ou douleurs impose une mesure des CPK selon la notice Sortis. L’arrêt demandé au-delà de5fois la limite normale s’inscrit dans cette stratégie de détection, avec une attention aussi aux symptômes importants malgré un chiffre inférieur.', 'aips-sortis-surveillance')
p.p('Une douleur persistante attribuée à la fibromyalgie ne doit pas faire perdre une nouvelle maladie associée. Le guide RCP2022 précise que les diagnostics peuvent coexister ; une anomalie objective nouvelle conserve sa valeur d’orientation.', 'f83-rcp-coexistence')
p.h('Prévention tertiaire : récupérer et prévenir les récidives')
p.p('La Ligue suisse contre le rhumatisme place l’éducation et l’autogestion au centre de la stratégie fibromyalgique. L’activité régulière adaptée et le pacing permettent de répartir l’effort et la récupération, en tenant compte de la fatigue physique et cognitive.', ['pa83-fibro-soins','pa83-fibro-activite'])
p.p('Après rhabdomyolyse, la réadaptation prend en compte les séquelles physiques et psychologiques. Des épisodes répétés ou inexpliqués justifient une investigation étiologique afin de prévenir une récidive plutôt que de répéter seulement les mêmes conseils généraux.', ['e15','e14'])
p.p('Dans une myopathie inflammatoire, le suivi ne porte pas uniquement sur les CK : les atteintes œsophagienne, cardiaque et pulmonaire et la recherche d’une néoplasie selon le contexte influencent le pronostic. La prévention de leur retentissement dépend de la filière spécialisée.', 'p83-myopathies-gravite')
p.tableau(['Niveau','Geste concret','Population concernée'],[
 [('La prévention primaire adapte l’exposition.', 'doms-prevention'),('Éviter l’augmentation brutale d’une charge non habituelle.', 'doms-prevention'),('Les personnes débutant ou reprenant une activité ajustent la charge à leur entraînement.', 'doms-prevention')],
 [('La prévention secondaire repère les complications.', 'e13'),('Faire réévaluer rapidement une anomalie urinaire, générale ou métabolique.', 'e13'),('Les personnes présentant une souffrance musculaire aiguë sont évaluées selon les signes et comorbidités.', 'e13')],
 [('La prévention tertiaire rend l’activité soutenable.', 'pa83-fibro-activite'),('Planifier effort, pauses et récupération plutôt que dépasser les réserves.', 'pa83-fibro-activite'),('Les personnes ayant un syndrome fibromyalgique construisent un programme individualisé.', 'pa83-fibro-soins')]
])
p.sauver()
