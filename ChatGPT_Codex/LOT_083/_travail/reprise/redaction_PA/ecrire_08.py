from rendu import Point
p=Point(8)
p.p('Le diagnostic de myalgie décrit une plainte musculaire ; il ne préjuge pas de la cause. Les critères utiles sont ensuite ceux du phénotype retenu, après la recherche des situations urgentes.', ['p83-definition','e13'])
p.h('Des critères cliniques propres à chaque constellation')
p.tableau(['Hypothèse','Éléments positifs','Ce qui reste insuffisant'],[
 [('Un syndrome myofascial est envisagé.', 'p83-myofascial-fibro'),('La DGN2025 décrit point douloureux dans une bande tendue, contraction locale à la palpation et douleur propagée.', 'p83-myofascial-fibro'),('Une douleur diffuse sans cette recherche clinique ne suffit pas à documenter un point gâchette.', 'p83-myofascial-fibro')],
 [('Des courbatures retardées suivent un effort inhabituel.', 'doms-definition'),('Le début est retardé de6–12heures, le maximum survient habituellement vers48–72heures selon la revue2024, dans une évolution généralement résolutive en une semaine.', 'doms-definition'),('Cette description ne remplace ni l’examen de gravité ni l’évaluation d’une douleur immédiatement liée à un choc.', ['doms-definition','p83-doms-contusion-clinique','e13'])],
 [('Une contusion survient après un impact direct.', 'p83-doms-contusion-clinique'),('La chronologie traumatique et les constatations locales guident le diagnostic.', ['p83-doms-contusion-clinique','rms-clinique']),('Le mécanisme ne dispense pas de rechercher une complication compartimentale.', 'p83-boast-loges-0')],
 [('Une PPR est plausible dans un tableau inflammatoire des ceintures.', 'p83-pmr'),('L’EULAR2025, publié en2026, retient la combinaison des symptômes et signes et l’exclusion des imitateurs.', 'p83-eular26-diagnostic'),('Les critères de classification destinés à la recherche ne doivent pas servir seuls de diagnostic individuel.', 'p83-eular26-diagnostic')]
])
p.h('Fibromyalgie : critères2016 repris dans le guide britannique2022')
p.p('Le Royal College of Physicians reprend les critères2016 : WPI au moins7 avec SSS au moins5, ou WPI de4 à6 avec SSS au moins9. Il faut aussi une douleur généralisée dans au moins4 des5régions et des symptômes présents à un niveau comparable depuis au moins3mois.', ['f83-rcp-criteres','f83-rcp-annexe2016'])
p.fenetre('Compter les sites et les régions sans confondre les deux',[
 ('Le WPI porte sur les sites douloureux de la dernière semaine et se cote sur19sites. Les régions sont supérieure gauche, supérieure droite, inférieure gauche, inférieure droite et axiale.', 'f83-rcp-annexe2016'),
 ('La mâchoire, le thorax et l’abdomen peuvent contribuer au comptage des sites, mais sont exclus de la définition de douleur généralisée utilisée pour la règle des4régions sur5. Le même récit doit donc être lu selon deux dénominateurs distincts.', 'f83-rcp-annexe2016'),
 ('Le SSS interroge la fatigue, les difficultés cognitives et le sommeil non réparateur, cotés de0 à3 sur la dernière semaine. La fiche recherche aussi céphalées, douleurs ou crampes du bas-ventre et dépression dans les6derniers mois.', 'f83-rcp-sss'),
 ('Une autre maladie n’invalide pas automatiquement une fibromyalgie ; réciproquement, la fibromyalgie n’exclut pas une maladie cliniquement importante associée. L’examen des anomalies objectives conserve donc sa place.', 'f83-rcp-coexistence')
])
p.h('Rhabdomyolyse : critères de consensus et priorité clinique')
p.p('Le consensus ENMC de l’atelier2024 publié en2025 propose une augmentation rapide des CK au-delà de10000UI/L après effort et au-delà de5000UI/L hors effort, accompagnée de gonflement, faiblesse ou douleur. Le pic survient approximativement entre1 et4jours, avec retour vers la valeur de base en1–2semaines de repos.', 'e12')
p.p('Chez un patient ayant une maladie neuromusculaire préexistante, le consensus considère une hausse de5 à10fois la valeur habituelle. La comparaison au niveau propre du patient évite de traiter une valeur chronique comme un événement entièrement nouveau.', 'e12')
p.fenetre('Critère diagnostique et seuil de sécurité ne sont pas interchangeables',[
 ('Le consensus ENMC associe le tableau clinique et l’évolution des CK ; la présence de myoglobinurie établit aussi une rhabdomyolyse dans ce cadre. Ces propositions sont attribuées à un atelier de consensus, sans les présenter comme un seuil universel de sortie.', 'e12'),
 ('La priorité aiguë repose sur les constantes, les urines foncées ou l’anurie, les complications de loges et les anomalies métaboliques. Une valeur inférieure au seuil de définition ne permet pas d’ignorer une de ces alarmes.', 'e13'),
 ('L’évaluation du risque rénal peut s’appuyer sur le score de McMahon. La stratégie de perfusion et de surveillance dépend du risque et des comorbidités, et non de la seule présence de myalgies après activité.', 'e13')
])
p.h('Les examens qui orientent sans constituer un verdict isolé')
p.p('Sous statine, une faiblesse proximale progressive, une dysphagie et des CK très élevées font envisager une forme nécrosante immunomédiée. Les anti-HMGCR soutiennent ce diagnostic ; l’absence d’amélioration après arrêt distingue cette branche d’une toxicité simple.', 'p83-statine-imnm')
p.p('Une CK normale ne ferme pas toutes les hypothèses inflammatoires ou endocriniennes. La DGN décrit cette possibilité dans certaines myosites et dans l’hypothyroïdie, ce qui impose une lecture conjointe de la force, des signes associés et du bilan ciblé.', ['pa83-biologie','p83-hypothyroidie'])
p.p('Une bonne réponse aux glucocorticoïdes ne doit pas servir de test diagnostique de PPR. L’EULAR déconseille l’essai diagnostique, car il peut masquer les informations nécessaires à la confirmation et compliquer l’évaluation spécialisée.', 'p83-eular26-pas-test-gc')
p.p('Pour l’artérite à cellules géantes, une forte probabilité clinique avec imagerie positive peut permettre de poser le diagnostic sans autre examen ; une faible probabilité avec imagerie négative le rend peu probable. Les configurations discordantes nécessitent un complément plutôt qu’une conclusion automatique.', 'p83-eular23-probabilite')
p.sauver()
