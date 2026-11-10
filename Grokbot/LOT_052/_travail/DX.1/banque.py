#!/usr/bin/env python3
"""DX.1 Appendicite aiguë — phrases propres, distinctes de la Phase A."""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from moteur import Moteur

m = Moteur(os.path.join(os.path.dirname(__file__), 'paquet.json'))
S, W, H = m.S, m.W, m.HTML

# --- 1 ---
S(1, "La WSES met à jour en 2020 les [[dx1-p1-f1|recommandations de Jérusalem]] sur l'appendicite aiguë, car sept thèmes y sont traités.", "wses_app_2020-30")
S(1, "Ces thèmes couvrent donc le diagnostic, le traitement non opératoire, le délai opératoire, la chirurgie, le grade et l'antibiotique.", "wses_app_2020-30")
S(1, "L'appendicite aiguë compte parmi les causes fréquentes de douleur abdominale basse, car elle est le diagnostic le plus fréquent du jeune hospitalisé.", "wses_app_2020-31")
S(1, "Le grade 1 de la WSES correspond à un appendice inflammé, donc ce grade décrit la forme que le chirurgien rencontre le plus souvent.", "wses_app_2020-269")
S(1, "Le grade 0 est un appendice d'aspect normal, ce qui empêche de poser le diagnostic sur la seule vue opératoire.", "wses_app_2020-269")
S(1, "La forme compliquée, pour la plupart des chirurgiens cités, réunit donc perforation, abcès intra-abdominal ou péritonite purulente.", "wses_app_2020-267")
S(1, "Le phlegmon et l'abcès restent des formes compliquées à part, car le texte leur consacre un thème propre.", "wses_app_2020-30")
S(1, "Toute douleur de la fosse iliaque droite reste distincte d'une appendicite, puisque le grade 0 existe.", "wses_app_2020-269")
S(1, "La recherche a retenu 157 articles sur 984, afin de rédiger les énoncés de cette mise à jour.", "wses_app_2020-60")
S(1, "48 énoncés et 51 recommandations constituent ainsi la réponse à 30 questions de recherche dans cette mise à jour.", "wses_app_2020-60")

W(1, "dx1-p1-f1", "Ce que couvre la mise à jour de Jérusalem", [
    ("Le diagnostic constitue le premier thème, car la probabilité se stratifie avant l'imagerie.", "wses_app_2020-30"),
    ("Le traitement non opératoire de la forme non compliquée constitue ensuite le deuxième thème.", "wses_app_2020-30"),
    ("Le délai avant appendicectomie et le retard hospitalier constituent ensuite le troisième thème.", "wses_app_2020-30"),
    ("La chirurgie, le grade peropératoire, le phlegmon et l'antibiotique ferment enfin la liste des thèmes.", "wses_app_2020-30"),
    ("Le piège est de traiter la mise à jour comme un simple rappel, car le conseil de la WSES l'a convoquée.", "wses_app_2020-38"),
])

# --- 2 ---
S(2, "La douleur abdominale aiguë représente ainsi 7 à 10 % des passages aux urgences dans l'introduction de ces recommandations.", "wses_app_2020-31")
S(2, "Dans les pays développés, l'incidence va ainsi de 5,7 à 50 pour 100,000 habitants et par an, avec un pic entre 10 et 30 ans.", "wses_app_2020-31")
S(2, "Le risque au cours de la vie est ainsi de 9 % aux États-Unis, de 8 % en Europe et de 2 % en Afrique.", "wses_app_2020-32")
S(2, "La perforation survient dans 16 à 40 % des cas, alors qu'elle atteint 40 à 57 % chez les plus jeunes.", "wses_app_2020-32")
S(2, "Après 50 ans, cette perforation concerne 55 à 70 % des patients, donc l'âge change la gravité attendue.", "wses_app_2020-32")
S(2, "La mortalité reste inférieure à 0,1 % si l'appendicite n'est pas gangréneuse, et elle atteint 0,6 % si elle l'est.", "wses_app_2020-33")
S(2, "La forme perforée porte une mortalité d'environ 5 %, ce qui la sépare de la forme non perforée.", "wses_app_2020-33")
S(2, "Dans l'énumération de Sinz, cette cause représente 6,7 à 28,1 % des étiologies gastro-intestinales qu'il liste.", "sinz_fms_2021-5")
S(2, "Les complications globales atteignent 11,1 % après voie ouverte, tandis que la cœlioscopie affiche 8,7 % dans la synthèse citée.", "wses_app_2020-36")
S(2, "Une validation de 2018 a réuni 116 services dans 44 pays pendant 6 mois, afin de tester le grade opératoire.", "wses_app_2020-270")
S(2, "Dans cette validation, le grade 0 représente 3,8 %, alors que le grade 1 représente 50,4 % des patients inclus.", "wses_app_2020-270")
S(2, "Le grade 2a y représente 16,8 %, le grade 2b 3,4 %, et enfin le grade 3a 8,8 %.", "wses_app_2020-270")
S(2, "Le grade 3b représente 4,8 %, le grade 3c représente 1,9 %, et enfin le grade 4 atteint 10,0 %.", "wses_app_2020-270")
S(2, "L'enfant et l'adolescent, pour ce texte, ont entre 1 et 16 ans, car les nourrissons sont exclus de la revue.", "wses_app_2020-40")

H(2, '''<div class="t" style="overflow-x:auto"><table>
<caption>Chiffres recopiés depuis les passages cités.</caption>
<thead><tr><th>Indicateur</th><th>Valeur lue</th><th>Population</th><th>Source</th></tr></thead>
<tbody>
<tr><td>Passages aux urgences pour douleur abdominale</td><td>7 à 10 %</td><td>urgences</td><td>WSES, 2020</td></tr>
<tr><td>Incidence dans les pays développés</td><td>5,7 à 50 pour 100,000 par an</td><td>habitants</td><td>WSES, 2020</td></tr>
<tr><td>Risque au cours de la vie</td><td>9 % États-Unis, 8 % Europe, 2 % Afrique</td><td>population générale</td><td>WSES, 2020</td></tr>
<tr><td>Perforation</td><td>16 à 40 %, jusqu'à 55 à 70 % après 50 ans</td><td>appendicites</td><td>WSES, 2020</td></tr>
<tr><td>Place dans la liste de Sinz</td><td>6,7 à 28,1 %</td><td>causes gastro-intestinales citées</td><td>Sinz, 2021</td></tr>
</tbody></table></div>''')

W(2, "dx1-p2-f1", "Pourquoi les pourcentages ne se fusionnent pas", [
    ("L'incidence de 5,7 à 50 pour 100,000 est celle des pays développés, donc elle n'est pas un taux suisse séparé.", "wses_app_2020-31"),
    ("Le risque de 8 % en Europe est un risque au cours de la vie, ce qui n'est pas une incidence annuelle.", "wses_app_2020-32"),
    ("Sinz indique une fourchette de 6,7 à 28,1 % parmi des causes d'abdomen aigu, donc le dénominateur diffère.", "sinz_fms_2021-5"),
    ("La mortalité de 5 % concerne la forme perforée, alors qu'elle ne s'applique pas à la forme non gangréneuse.", "wses_app_2020-33"),
    ("Le piège est d'additionner 11,1 % et 8,7 %, car ce sont deux voies chirurgicales et non un même groupe.", "wses_app_2020-36"),
])

# --- 3 ---
S(3, "La perforation n'est pas l'aboutissement obligatoire d'une obstruction, car une résolution spontanée est aussi décrite.", "wses_app_2020-33")
S(3, "Tous les patients ne progressent donc pas vers la perforation, ce qui autorise à discuter une évolution favorable.", "wses_app_2020-33")
S(3, "La forme perforée augmente ainsi la morbidité et la mortalité par rapport à la forme non perforée.", "wses_app_2020-33")
S(3, "Le grade 2 correspond à la nécrose, le grade 3 à une tumeur inflammatoire, et enfin le grade 4 à la péritonite diffuse.", "wses_app_2020-269")
S(3, "Un coprolithe peut expliquer une douleur de fosse iliaque droite sans inflammation évidente, puisqu'une série de 203 pièces normales le discute.", "wses_app_2020-279")
S(3, "Dans cette série, retirer l'appendice d'aspect normal a semblé traiter des symptômes récidivants lorsqu'aucune autre cause n'était vue.", "wses_app_2020-279")
S(3, "Une autre étude a en effet trouvé des remaniements inflammatoires dans 90 % des appendices d'aspect normal retirés.", "wses_app_2020-279")
S(3, "L'infection compliquée justifie ainsi une couverture des gram négatifs digestifs et des anaérobies, dont Escherichia coli et Bacteroides.", "wses_app_2020-310")
S(3, "Le métronidazole n'est pas indiqué lorsque l'antibiotique large couvre déjà les anaérobies, car le texte le précise.", "wses_app_2020-310")
S(3, "La présentation, la gravité, l'imagerie et la chirurgie varient avec le revenu du pays, donc un protocole unique ne se transpose pas.", "wses_app_2020-32")

H(3, '''<div class="t" style="overflow-x:auto"><table>
<caption>Perturbation, ce qui la montre, ce qui la corrige.</caption>
<thead><tr><th>Perturbation</th><th>Ce qui la montre</th><th>Ce qui la corrige</th></tr></thead>
<tbody>
<tr><td>Appendice inflammé, grade 1</td><td>Score élevé et imagerie, ou vue opératoire</td><td>Appendicectomie cœlioscopique dans les 24 heures, ou traitement non opératoire sélectionné</td></tr>
<tr><td>Nécrose, grade 2</td><td>Grade opératoire</td><td>Chirurgie, car la nécrose sort de la forme simplement inflammée</td></tr>
<tr><td>Perforation, abcès ou péritonite purulente</td><td>Imagerie ou constat opératoire</td><td>Contrôle du foyer et antibiotique postopératoire</td></tr>
<tr><td>Péritonite diffuse, grade 4</td><td>Grade 4</td><td>Contrôle du foyer, sans traitement non opératoire</td></tr>
</tbody></table></div>''')

W(3, "dx1-p3-f1", "Obstruction et perforation", [
    ("L'obstruction n'entraîne pas forcément la perforation, car le texte décrit aussi une résolution.", "wses_app_2020-33"),
    ("La mortalité non gangréneuse reste sous 0,1 %, donc la perforation change l'ordre de grandeur.", "wses_app_2020-33"),
    ("La mortalité gangréneuse atteint 0,6 %, alors que la forme perforée avoisine 5 %.", "wses_app_2020-33"),
    ("Un coprolithe dans une pièce histologiquement normale a en effet été discuté sur 203 appendicectomies.", "wses_app_2020-279"),
    ("Le piège est de promettre que toute appendicite perforera, car le texte dit le contraire.", "wses_app_2020-33"),
])

# --- 4 ---
S(4, "La valeur de chaque signe isolé est faible, donc la démarche se taille selon l'âge, le sexe et la probabilité.", "wses_app_2020-61")
S(4, "La recommandation 1.1 est forte, avec une qualité de preuve modérée, car elle impose cette stratification.", "wses_app_2020-62")
S(4, "Les scores cliniques seuls, comme Alvarado, AIR et le score adulte, suffisent ainsi à exclure l'appendicite chez le patient à bas risque.", "wses_app_2020-62")
S(4, "La recommandation 1.2.1 est forte et de haute qualité, car elle retient les scores pour exclure et pour désigner le risque intermédiaire.", "wses_app_2020-63")
S(4, "Alvarado ne confirme pas l'appendicite de l'adulte, c'est pourquoi la recommandation 1.3 déconseille cet usage.", "wses_app_2020-64")
S(4, "AIR et AAS sont les scores les plus discriminants chez l'adulte, c'est pourquoi la recommandation 1.4 est forte, de classe 1A.", "wses_app_2020-65")
S(4, "Chez l'enfant, Alvarado et le score pédiatrique aident à exclure, cependant le diagnostic ne repose pas sur le score seul.", "wses_app_2020-66")
S(4, "La forme compliquée se recherche avant la forme fréquente, car la perforation change la mortalité et l'antibiotique.", "wses_app_2020-33")
S(4, "Un coprolithe écarte le traitement non opératoire, car la recommandation 2.1.1 le réserve à son absence.", "wses_app_2020-80")
S(4, "Pendant la grossesse, le traitement non opératoire est déconseillé, car des preuves de haut niveau manquent.", "wses_app_2020-80")

H(4, '''<div class="t" style="overflow-x:auto"><table>
<caption>Ce qui tranche, le piège, la conduite.</caption>
<thead><tr><th>Situation</th><th>Élément qui tranche</th><th>Piège</th><th>Conduite si le résultat est positif</th></tr></thead>
<tbody>
<tr><td>Bas risque selon AIR ou AAS</td><td>Le score exclut sans confirmer</td><td>Utiliser Alvarado pour affirmer chez l'adulte</td><td>L'imagerie n'est pas le premier geste</td></tr>
<tr><td>Risque intermédiaire</td><td>Imagerie systématique et rapide</td><td>Rester sur la clinique</td><td>Échographie, puis scanner à faible dose si besoin</td></tr>
<tr><td>Haut risque avant 40 ans, scores hauts</td><td>AIR 9 à 12, Alvarado 9 à 10, AAS au moins 16</td><td>Imposer un scanner à tous</td><td>Une cœlioscopie diagnostique peut précéder le scanner</td></tr>
<tr><td>Perforation, abcès ou péritonite</td><td>Imagerie ou grade opératoire</td><td>Proposer un traitement non opératoire</td><td>Contrôle du foyer et antibiotique</td></tr>
</tbody></table></div>''')

W(4, "dx1-p4-f1", "Scores : exclure n'est pas confirmer", [
    ("Alvarado, AIR et le score adulte identifient le bas risque et diminuent ainsi l'appendicectomie blanche.", "wses_app_2020-62"),
    ("AIR et AAS réduisent ainsi les admissions et les imageries dans les groupes bas et intermédiaires.", "wses_app_2020-65"),
    ("La recommandation contre Alvarado comme confirmation chez l'adulte est ainsi de force faible à modérée.", "wses_app_2020-64"),
    ("Chez l'enfant, le score seul ne pose pas le diagnostic, c'est pourquoi la recommandation 1.5 est faible, de classe 2C.", "wses_app_2020-66"),
    ("Le piège d'examen est donc d'hospitaliser ou d'opérer sur un Alvarado intermédiaire sans imagerie.", "wses_app_2020-63"),
])

# --- 5 ---
S(5, "L'âge et le sexe entrent dans la probabilité, car la recommandation 1.1 les place au début du chemin diagnostique.", "wses_app_2020-62")
S(5, "Avant 40 ans, un score très haut peut conduire à la cœlioscopie sans scanner, ce qui ne vaut pas après cet âge.", "wses_app_2020-72")
S(5, "Après 50 ans, la perforation est plus fréquente, donc le récit d'une douleur brève ne rassure pas.", "wses_app_2020-32")
S(5, "Chez la femme enceinte, symptômes et signes seuls ne posent pas le diagnostic, c'est pourquoi la biologie est toujours demandée.", "wses_app_2020-63")
S(5, "La grossesse contre-indique le traitement non opératoire dans l'état actuel des preuves, puisque la recommandation 2.1.2 le dit.", "wses_app_2020-80")
S(5, "Un coprolithe connu ou vu à l'imagerie sort le patient du traitement non opératoire, car la sélection l'exige.", "wses_app_2020-80")
S(5, "Une douleur de fosse iliaque droite qui persiste malgré un bilan normal appelle donc une imagerie en coupe avant la chirurgie.", "wses_app_2020-75")
S(5, "Les médicaments et le VIH comptent, car Alvarado est moins sensible chez le patient vivant avec le VIH.", "wses_app_2020-64")
S(5, "Chez la personne âgée, Alvarado ne sépare en effet pas de façon fiable la forme compliquée de la forme simple.", "wses_app_2020-64")
S(5, "Le délai depuis l'admission se demande, car dépasser 24 heures augmente le risque d'issue défavorable.", "wses_app_2020-85")

H(5, '''<div class="t" style="overflow-x:auto"><table>
<caption>Drapeaux et action.</caption>
<thead><tr><th>Drapeau</th><th>Signification</th><th>Action</th></tr></thead>
<tbody>
<tr><td>Grossesse</td><td>Le diagnostic clinique seul est insuffisant</td><td>Biologie, échographie, puis IRM si l'échographie ne tranche pas</td></tr>
<tr><td>Coprolithe</td><td>Le traitement non opératoire n'est pas la sélection retenue</td><td>Discuter la chirurgie</td></tr>
<tr><td>Âge supérieur à 50 ans</td><td>Perforation plus fréquente, de 55 à 70 %</td><td>Ne pas différer l'imagerie au motif d'un tableau incomplet</td></tr>
<tr><td>Douleur persistante et bilan initial normal</td><td>La recommandation 1.12 est forte</td><td>Imagerie en coupe, puis cœlioscopie si la douleur progresse</td></tr>
</tbody></table></div>''')

W(5, "dx1-p5-f1", "Grossesse : ce que le récit ne suffit pas à dire", [
    ("Symptômes et signes seuls ne font pas le diagnostic pendant la grossesse, donc la biologie s'ajoute.", "wses_app_2020-63"),
    ("L'échographie par compression graduelle est ainsi l'imagerie initiale suggérée, avec une preuve très faible.", "wses_app_2020-76"),
    ("L'IRM vient ensuite si l'échographie ne conclut pas, et une IRM négative n'exclut pas l'appendicite.", "wses_app_2020-76"),
    ("Le traitement non opératoire est donc déconseillé pendant la grossesse jusqu'à de nouvelles preuves solides.", "wses_app_2020-80"),
    ("Le piège est de rassurer parce que l'IRM est normale, car la suspicion haute maintient l'indication opératoire.", "wses_app_2020-76"),
])

# --- 6 ---
S(6, "Le diagnostic clinique est souvent difficile, car il synthétise l'examen, la biologie et l'imagerie.", "wses_app_2020-34")
S(6, "Aucun score simple n'a été largement accepté, donc l'examen de la fosse iliaque droite ne se résume pas à un chiffre.", "wses_app_2020-34")
S(6, "L'échographie au lit du patient est un premier examen fiable lorsque l'opérateur est expérimenté, chez l'adulte comme chez l'enfant.", "wses_app_2020-72")
S(6, "La recommandation 1.10 place cette échographie en première ligne si l'imagerie est indiquée, et elle est forte.", "wses_app_2020-73")
S(6, "Chez l'enfant, l'échographie est en effet exacte et sûre quant aux perforations, aux retours aux urgences et aux appendicectomies blanches.", "wses_app_2020-77")
S(6, "Un score pédiatrique négatif aide à exclure, cependant la recommandation interdit de conclure sur ce seul score.", "wses_app_2020-66")
S(6, "La leucocytose et la protéine C réactive aident ainsi chez l'enfant, avec un seuil d'au moins 10 mg/L.", "wses_app_2020-67")
S(6, "Une leucocytose d'au moins 16,000 par millilitre est ainsi un facteur prédictif fort dans cette phrase pédiatrique.", "wses_app_2020-67")
S(6, "L'association de l'échographie et d'un score clinique peut ainsi remplacer le scanner chez l'adulte suspect.", "wses_app_2020-69")
S(6, "La palpation seule ne distingue pas la forme compliquée chez la personne âgée lorsque Alvarado est utilisé pour cela.", "wses_app_2020-64")

W(6, "dx1-p6-f1", "Échographie au lit du patient", [
    ("POCUS désigne l'échographie réalisée au lit, et le texte la juge fiable si l'opérateur est expérimenté.", "wses_app_2020-72"),
    ("Elle est proposée comme premier outil chez l'adulte et chez l'enfant lorsque l'imagerie est indiquée.", "wses_app_2020-73"),
    ("La recommandation correspondante est donc forte, avec une qualité de preuve modérée, de classe 1B.", "wses_app_2020-73"),
    ("Chez l'enfant, elle diminue le recours au scanner si un algorithme par étapes est suivi.", "wses_app_2020-77"),
    ("Le piège est donc de conclure que l'examen clinique chiffré remplace cette échographie.", "wses_app_2020-34"),
])

# --- 7 ---
H(7, '<h4><em>7.1 Forme non compliquée</em></h4>')
S(7, "La forme non compliquée est celle pour laquelle un traitement non opératoire sélectionné peut ainsi être discuté.", "wses_app_2020-79")
S(7, "L'absence de coprolithe fait partie de cette sélection, car la recommandation 2.1.1 l'écrit explicitement.", "wses_app_2020-80")
H(7, '<h4><em>7.2 Forme compliquée</em></h4>')
S(7, "La [[dx1-p7-f1|forme compliquée]] réunit, pour la plupart des chirurgiens du texte, perforation, abcès ou péritonite purulente.", "wses_app_2020-267")
S(7, "Le gangrène non perforé, le coprolithe et le pus élargissent encore la définition, puisque le passage cite ces auteurs.", "wses_app_2020-267")
H(7, '<h4><em>7.3 Grades opératoires</em></h4>')
S(7, "Le système comprend ainsi quatre grades principaux, de l'appendice normal jusqu'à la péritonite diffuse.", "wses_app_2020-269")
S(7, "Le grade 1, appendice inflammé, a ainsi représenté environ la moitié de la validation internationale.", "wses_app_2020-270")
H(7, '<h4><em>7.4 Phlegmon et abcès</em></h4>')
S(7, "Le phlegmon et l'abcès constituent ainsi un thème séparé de la simple appendicite inflammée.", "wses_app_2020-30")
S(7, "L'antibiotique postopératoire est indiqué pour la perforation, l'abcès ou la péritonite purulente, puisque le même passage l'indique.", "wses_app_2020-267")
H(7, '<h4><em>7.5 Grossesse</em></h4>')
S(7, "Pendant la grossesse, une IRM négative ou non conclusive n'exclut pas l'appendicite si la suspicion clinique reste haute.", "wses_app_2020-76")
H(7, '<h4><em>7.6 Enfant</em></h4>')
S(7, "L'enfant visé a de 1 à 16 ans, alors que le score seul ne suffit pas à affirmer le diagnostic.", "wses_app_2020-40")
H(7, '<h4><em>7.7 Douleur persistante à bilan normal</em></h4>')
S(7, "Si les examens sont normaux et que la douleur de fosse iliaque droite ne cède pas, l'imagerie en coupe précède la chirurgie.", "wses_app_2020-75")

H(7, '''<div class="t" style="overflow-x:auto"><table>
<caption>Syndromes de l'appendicite, d'après le grade WSES.</caption>
<thead><tr><th>Syndrome</th><th>Signes fonctionnels</th><th>Signes physiques ou grade</th></tr></thead>
<tbody>
<tr><td>7.1 Non compliquée</td><td>Douleur de fosse iliaque, sans critère de complication</td><td>Grade 1, appendice inflammé, sans coprolithe si un traitement non opératoire est discuté</td></tr>
<tr><td>7.2 Compliquée</td><td>Aggravation, défense plus étendue</td><td>Perforation, abcès ou péritonite purulente</td></tr>
<tr><td>7.3 Nécrose</td><td>Tableau appendiculaire qui se dégrade</td><td>Grade 2</td></tr>
<tr><td>7.4 Phlegmon ou abcès</td><td>Fièvre et douleur localisée persistante</td><td>Collection ou empâtement, thème propre du texte</td></tr>
<tr><td>7.5 Péritonite diffuse</td><td>Douleur généralisée</td><td>Grade 4</td></tr>
<tr><td>7.6 Grossesse</td><td>Douleur dont la clinique seule ne tranche pas</td><td>Échographie puis IRM</td></tr>
<tr><td>7.7 Enfant de 1 à 16 ans</td><td>Douleur et biologie inflammatoire</td><td>Échographie d'abord, score non conclusif seul</td></tr>
</tbody></table></div>''')

W(7, "dx1-p7-f1", "Les quatre grades", [
    ("Le grade 0 est un appendice d'aspect normal, tandis que le grade 1 est un appendice inflammé.", "wses_app_2020-269"),
    ("Le grade 2 est la nécrose, tandis que le grade 3 est une tumeur inflammatoire.", "wses_app_2020-269"),
    ("Le grade 4 est la péritonite diffuse, ce qui ferme l'échelle et termine la classification.", "wses_app_2020-269"),
    ("La validation a ainsi trouvé 50,4 % de grades 1 et 10,0 % de grades 4.", "wses_app_2020-270"),
    ("Le piège est donc de proposer le traitement non opératoire à une forme déjà compliquée, car la sélection ne le retient pas.", "wses_app_2020-80"),
])

# --- 8 ---
S(8, "Un Alvarado inférieur à 5 exclut ainsi l'appendicite avec une sensibilité de 99 %, sans pour autant la confirmer.", "wses_app_2020-117")
S(8, "Dans une cohorte rétrospective, 100 % des hommes avec un Alvarado d'au moins 9 avaient ainsi une appendicite à l'histologie.", "wses_app_2020-117")
S(8, "100 % des femmes avec un Alvarado de 10 avaient ainsi une appendicite confirmée par l'histologie dans cette cohorte.", "wses_app_2020-117")
S(8, "À l'inverse, 0 % des hommes avec un Alvarado de 1 ou moins avaient en effet une appendicite à l'opération.", "wses_app_2020-117")
S(8, "5 % ou moins des femmes avec un Alvarado de 2 ou moins étaient dans ce cas, donc le seuil bas sert à exclure.", "wses_app_2020-117")
S(8, "La recommandation 1.4 indique ainsi d'utiliser AIR et AAS comme prédicteurs, avec une preuve haute et une force forte.", "wses_app_2020-65")
S(8, "Pour un AIR de 9 à 12, un Alvarado de 9 à 10 et un AAS d'au moins 16, le scanner peut ainsi être évité avant 40 ans.", "wses_app_2020-72")
S(8, "Cette suggestion est faible, de classe 2B, donc elle ne devient pas une obligation de sauter l'imagerie.", "wses_app_2020-72")
S(8, "Le score RIPASA, au seuil de 7,5, a ainsi montré une sensibilité de 85,39 % et une spécificité de 69,86 % dans une série irlandaise.", "wses_app_2020-119")
S(8, "La même série indique ainsi une valeur prédictive positive de 84,06 % et une valeur prédictive négative de 72,86 %.", "wses_app_2020-119")
S(8, "L'exactitude diagnostique de ce seuil atteint 80 % dans la série irlandaise, donc le score ne se généralise pas seul.", "wses_app_2020-119")
S(8, "Ces chiffres ne remplacent pas AIR et AAS, car la recommandation forte porte sur ces deux scores.", "wses_app_2020-65")
S(8, "Le grade opératoire est ainsi suggéré en routine, par exemple le grade WSES de 2015 ou le grade AAST, avec une force faible.", "wses_app_2020-276")

H(8, '''<div class="t" style="overflow-x:auto"><table>
<caption>Ce qui suffit et ce qui ne suffit pas.</caption>
<thead><tr><th>Critère</th><th>Année et force</th><th>Ce qu'il permet</th><th>Ce qu'il ne permet pas</th></tr></thead>
<tbody>
<tr><td>Alvarado inférieur à 5</td><td>WSES 2020, sensibilité 99 % pour exclure</td><td>Réduire le séjour et l'irradiation</td><td>Confirmer l'appendicite de l'adulte</td></tr>
<tr><td>AIR et AAS</td><td>Recommandation 1.4, preuve haute, forte, 1A</td><td>Prédire et diminuer l'appendicectomie blanche</td><td>Remplacer l'imagerie du risque intermédiaire</td></tr>
<tr><td>AIR 9 à 12, Alvarado 9 à 10, AAS au moins 16, âge inférieur à 40 ans</td><td>Recommandation 1.9, faible, 2B</td><td>Envisager la cœlioscopie sans scanner</td><td>L'imposer après 40 ans</td></tr>
<tr><td>Grade WSES</td><td>Suggestion 5.2, preuve modérée, faible, 2B</td><td>Grouper les patients pour la suite opératoire</td><td>Remplacer l'histologie dans tous les débats</td></tr>
</tbody></table></div>''')

W(8, "dx1-p8-f1", "Alvarado inférieur à 5", [
    ("La spécificité d'Alvarado ne suffit pas à diagnostiquer, cependant un score sous 5 exclut avec une sensibilité de 99 %.", "wses_app_2020-117"),
    ("Ce seuil peut ainsi raccourcir le séjour aux urgences et diminuer l'irradiation des patients à bas risque.", "wses_app_2020-117"),
    ("Un homme avec un score de 9 ou plus était ainsi positif à 100 % dans la cohorte citée.", "wses_app_2020-117"),
    ("Une femme avec un score de 10 était ainsi positive à 100 % dans la même cohorte.", "wses_app_2020-117"),
    ("Le piège est donc de transformer ces 100 % rétrospectifs en règle pour opérer sans imagerie après 40 ans.", "wses_app_2020-117", "wses_app_2020-72"),
])

# --- 9 ---
H(9, '<h4><em>9.a Gold standard</em></h4>')
S(9, "Aucun examen unique ne reste l'étalon de toutes les appendicites, car le chemin dépend du risque clinique.", "wses_app_2020-62")
S(9, "L'histologie confirme des cas de la cohorte d'Alvarado, cependant elle arrive après la décision opératoire.", "wses_app_2020-117")
H(9, '<h4><em>9.b Première intention</em></h4>')
S(9, "Après le score, l'imagerie est recommandée, et l'échographie au lit est le premier outil s'il faut une image.", "wses_app_2020-73")
S(9, "La combinaison du score et de l'échographie est recommandée pour améliorer la sensibilité et réduire le scanner.", "wses_app_2020-70")
S(9, "Chez l'enfant, la biologie inflammatoire est demandée de routine, avec une recommandation forte malgré une preuve très faible.", "wses_app_2020-68")
H(9, '<h4><em>9.c Alternatives</em></h4>')
S(9, "Pendant la grossesse, l'échographie par compression graduelle vient en premier, puis l'IRM si elle ne conclut pas.", "wses_app_2020-76")
S(9, "Chez l'enfant, si l'échographie ne conclut pas, le deuxième examen reste choisi selon les moyens locaux.", "wses_app_2020-78")
S(9, "L'IRM de l'enfant a au moins la sensibilité et la spécificité du scanner, donc elle est préférée en deuxième ligne malgré son coût.", "wses_app_2020-77")
H(9, '<h4><em>9.d Deuxième intention</em></h4>')
S(9, "Lorsque le scanner est indiqué, la faible dose avec injection n'est pas inférieure à la dose standard pour distinguer la forme compliquée.", "wses_app_2020-73")
S(9, "La recommandation 1.11 est forte, de classe 1A, et elle vise l'adolescent et le jeune adulte dont l'échographie est négative.", "wses_app_2020-74")
S(9, "Au risque intermédiaire, l'imagerie est suggérée de façon systématique, avec une recommandation faible de classe 2B.", "wses_app_2020-71")
S(9, "Si l'imagerie est négative et que la douleur progresse, la cœlioscopie exploratrice est recommandée, et cette recommandation est forte.", "wses_app_2020-75")

H(9, '''<div class="t" style="overflow-x:auto"><table>
<caption>Résultat, signification, conduite.</caption>
<thead><tr><th>Résultat</th><th>Signification</th><th>Conduite</th></tr></thead>
<tbody>
<tr><td>Score inférieur au seuil d'exclusion</td><td>Appendicite peu probable</td><td>Ne pas enchaîner un scanner pour confirmer</td></tr>
<tr><td>Échographie non conclusive</td><td>Le premier outil n'a pas tranché</td><td>Scanner à faible dose chez l'adolescent et le jeune adulte, ou IRM chez l'enfant et la femme enceinte</td></tr>
<tr><td>Scanner positif d'une forme compliquée</td><td>Perforation, abcès ou péritonite à prendre en charge</td><td>Contrôle du foyer, pas de traitement non opératoire</td></tr>
<tr><td>IRM négative pendant la grossesse</td><td>L'appendicite n'est pas exclue</td><td>Maintenir la discussion opératoire si la suspicion reste haute</td></tr>
</tbody></table></div>''')

H(9, '''<figure>
<img src="images/ee303acdbc1c4096.jpg" alt="Coupe axiale de tomodensitométrie déjà légendée par l'auteur : appendice, caecum, graisse, ganglions, artère iliaque.">
<figcaption>Cliché brut, pixels d'origine non modifiés. Cerevisae, CC BY-SA 4.0, Wikimedia Commons, fichier « CT scan of the abdomen showing acute appendicitis.jpg », consulté le 2026-11-10. L'auteur a écrit Enlarged appendix, caecum, Fat stranding, Subcentimeter lymph nodes et Left common iliac artery. Aucun millimètre n'est ajouté au mot subcentimeter.</figcaption>
</figure>
<figure>
<div style="position:relative;max-width:36rem">
<img src="images/ee303acdbc1c4096.jpg" alt="Même coupe, cinq repères numérotés sur les légendes de l'auteur." style="width:100%;height:auto;display:block">
<svg viewBox="0,0,512,512" style="position:absolute;left:0;top:0;width:100%;height:100%">
<circle cx="250" cy="78" r="16" fill="none" stroke="#7a1020" stroke-width="3"/>
<text x="244" y="84" fill="#7a1020" font-size="18" font-family="Verdana,sans-serif">1</text>
<circle cx="78" cy="150" r="16" fill="none" stroke="#7a1020" stroke-width="3"/>
<text x="72" y="156" fill="#7a1020" font-size="18" font-family="Verdana,sans-serif">2</text>
<circle cx="70" cy="430" r="16" fill="none" stroke="#7a1020" stroke-width="3"/>
<text x="64" y="436" fill="#7a1020" font-size="18" font-family="Verdana,sans-serif">3</text>
<circle cx="300" cy="455" r="16" fill="none" stroke="#7a1020" stroke-width="3"/>
<text x="294" y="461" fill="#7a1020" font-size="18" font-family="Verdana,sans-serif">4</text>
<circle cx="400" cy="95" r="16" fill="none" stroke="#7a1020" stroke-width="3"/>
<text x="394" y="101" fill="#7a1020" font-size="18" font-family="Verdana,sans-serif">5</text>
</svg>
</div>
<figcaption>Œuvre dérivée sous la même licence. Le repère 1 numérote la mention Enlarged appendix. Le repère 2 numérote caecum. Le repère 3 numérote Fat stranding. Le repère 4 numérote Subcentimeter lymph nodes. Le repère 5 numérote Left common iliac artery. Ces numéros ne mesurent pas l'appendice.</figcaption>
</figure>''')

S(9, "Le cliché retenu est une coupe axiale déjà légendée, et il illustre la modalité que la recommandation place après l'échographie négative.", "wses_app_2020-74")
S(9, "La graisse infiltrée et l'appendice augmenté, tels que l'auteur les a nommés, vont dans le sens d'une inflammation, sans donner un diamètre.", "wses_app_2020-269")
S(9, "Un appendice d'aspect normal sur une vue ne ferme pas le sujet, car le grade 0 existe et l'histologie peut encore montrer une inflammation.", "wses_app_2020-279")
S(9, "La conduite, si la clinique concorde avec une forme compliquée, est le contrôle du foyer plutôt qu'un nouvel examen sans enjeu.", "wses_app_2020-267")

W(9, "dx1-p9-f1", "Scanner à faible dose", [
    ("La faible dose avec injection reste non inférieure à la dose standard pour diagnostiquer et séparer la forme compliquée.", "wses_app_2020-73"),
    ("Elle réduit l'irradiation, ce qui justifie la préférence écrite dans l'énoncé 1.12.", "wses_app_2020-73"),
    ("La recommandation 1.11 vise l'adolescent et le jeune adulte après une échographie négative, et elle est de classe 1A.", "wses_app_2020-74"),
    ("Avant 40 ans, avec des scores très hauts, le scanner peut être sauté au profit de la cœlioscopie, suggestion faible.", "wses_app_2020-72"),
    ("Le piège est de répéter un scanner standard après une faible dose déjà conclusive.", "wses_app_2020-73"),
])

W(9, "dx1-p9-f2", "Lecture de la coupe", [
    ("On regarde d'abord les mentions déjà imprimées, car elles nomment l'appendice, le caecum et la graisse.", "wses_app_2020-269"),
    ("Le mot subcentimeter est celui de l'auteur pour les ganglions, donc aucun millimètre n'est inventé.", "wses_app_2020-269"),
    ("L'artère iliaque commune gauche est une légende d'orientation, et elle n'est pas le diagnostic.", "wses_app_2020-269"),
    ("Le grade 1 reste un appendice inflammé, ce que l'image suggère sans le prouver à elle seule.", "wses_app_2020-269"),
    ("Le piège est de conclure à une perforation parce que la graisse est infiltrée, car l'image ne date pas la perforation.", "wses_app_2020-33"),
])

# --- 10 ---
S(10, "L'arbre commence par la forme grave, car une péritonite purulente ou une perforation impose le contrôle du foyer.", "wses_app_2020-267")
S(10, "Si un coprolithe est présent, alors le traitement non opératoire n'est pas l'option retenue par la recommandation 2.1.1.", "wses_app_2020-80")
S(10, "Si la patiente est enceinte, alors le traitement non opératoire est déconseillé et l'imagerie commence par l'échographie.", "wses_app_2020-80")
S(10, "Si le score est bas, alors l'appendicite s'exclut et l'imagerie n'est pas demandée pour la confirmer.", "wses_app_2020-62")
S(10, "Si le risque est intermédiaire, alors l'imagerie est systématique, avant de choisir entre surveillance et chirurgie.", "wses_app_2020-71")
S(10, "Si le patient a moins de 40 ans et des scores très hauts, alors la cœlioscopie peut précéder le scanner.", "wses_app_2020-72")
S(10, "Si la forme est non compliquée et sans coprolithe, alors l'appendicectomie cœlioscopique se planifie dans les 24 heures.", "wses_app_2020-85")
S(10, "Attendre jusqu'à 24 heures après l'admission reste sans effet propre sur la complication, l'infection de site ou la morbidité.", "wses_app_2020-85")
S(10, "Au-delà de 24 heures après l'admission, le risque d'issue défavorable augmente, donc le créneau suivant ne se laisse pas passer.", "wses_app_2020-85")
S(10, "Si la douleur persiste après une imagerie négative, alors la cœlioscopie exploratrice cherche l'appendicite ou une autre cause.", "wses_app_2020-75")
S(10, "Chez l'enfant, la cœlioscopie est préférée à la voie ouverte lorsque le matériel et l'expérience existent.", "wses_app_2020-88")
S(10, "Cette préférence pédiatrique reste liée à moins de douleur, à moins d'infection de site et à une meilleure qualité de vie.", "wses_app_2020-88")

H(10, '''<div class="t" style="overflow-x:auto"><table>
<caption>Arbre, la forme grave d'abord.</caption>
<thead><tr><th>Si</th><th>Alors</th></tr></thead>
<tbody>
<tr><td>Perforation, abcès ou péritonite purulente</td><td>Le foyer se contrôle et l'antibiotique postopératoire est indiqué</td></tr>
<tr><td>Coprolithe</td><td>Le traitement non opératoire n'est pas retenu</td></tr>
<tr><td>Grossesse</td><td>Pas de traitement non opératoire ; échographie puis IRM</td></tr>
<tr><td>Score bas</td><td>L'appendicite s'exclut sans scanner de confirmation</td></tr>
<tr><td>Risque intermédiaire</td><td>Imagerie systématique</td></tr>
<tr><td>Moins de 40 ans et scores très hauts</td><td>La cœlioscopie peut précéder le scanner</td></tr>
<tr><td>Forme non compliquée sans coprolithe</td><td>Cœlioscopie sur la prochaine liste, dans les 24 heures</td></tr>
<tr><td>Douleur qui progresse après imagerie négative</td><td>Cœlioscopie exploratrice</td></tr>
</tbody></table></div>''')

W(10, "dx1-p10-f1", "Les 24 heures", [
    ("La recommandation 3.1 indique la cœlioscopie sur la prochaine liste, dans les 24 heures, pour la forme non compliquée.", "wses_app_2020-85"),
    ("La qualité de preuve est modérée et la force est forte, de classe 1B.", "wses_app_2020-85"),
    ("Un délai jusqu'à 24 heures après l'admission reste sans rôle propre de facteur de complication.", "wses_app_2020-85"),
    ("Après ce délai, les issues défavorables augmentent, donc le report au lendemain suivant n'est pas neutre.", "wses_app_2020-85"),
    ("Le piège est de confondre ce délai hospitalier avec la durée des symptômes avant l'arrivée.", "wses_app_2020-85"),
])

# --- 11 ---
H(11, '<h4><em>11.A But</em></h4>')
S(11, "Le but immédiat est de traiter dans les 24 heures une forme non compliquée, car la recommandation 3.1 fixe ce créneau.", "wses_app_2020-85")
S(11, "Pour la forme compliquée, le but est le contrôle du foyer, car l'antibiotique ne le remplace pas.", "wses_app_2020-111")
H(11, '<h4><em>11.B Moyens</em></h4>')
S(11, "Une dose unique d'antibiotique à large spectre, donnée de 0 à 60 minutes avant l'incision, diminue l'infection de paroi et l'abcès.", "wses_app_2020-110")
S(11, "La recommandation 7.1 est forte, de classe 1A, et elle déconseille l'antibiotique postopératoire si la forme est non compliquée.", "wses_app_2020-110")
S(11, "Cette dose préopératoire est efficace quel que soit le degré d'inflammation de l'appendice retiré.", "wses_app_2020-110")
S(11, "Si la forme est compliquée et que le foyer est contrôlé, 3 à 5 jours d'antibiotique donnent des résultats semblables à une cure plus longue.", "wses_app_2020-111")
S(11, "L'arrêt après 24 heures, lorsque l'adulte en a besoin, paraît sûr et raccourcit le séjour dans l'énoncé 7.2.", "wses_app_2020-111")
S(11, "L'essai STOP-IT a inclus 518 patients, et environ 4 jours ont donné des résultats semblables à environ 8 jours.", "wses_app_2020-307")
S(11, "Aucun milligramme suisse n'est écrit pour ces antibiotiques, car leur information professionnelle n'a pas été ouverte pour cette leçon.", "wses_app_2020-310")
S(11, "La WSES nomme la pipéracilline-tazobactam, l'ampicilline-sulbactam et l'imipénem, sans que ces noms deviennent une dose.", "wses_app_2020-310")
S(11, "Le [[dx1-p11-f4|traitement non opératoire]] par antibiotique est sûr chez des patients sélectionnés, sans coprolithe, avec une récidive jusqu'à 39 % à 5 ans.", "wses_app_2020-79")
S(11, "La recommandation 2.1.1 est forte et de haute qualité, et elle avertit du risque d'échec et de forme compliquée méconnue.", "wses_app_2020-80")
S(11, "Les méta-analyses citées trouvent moins de complications à 5 ans et un arrêt de travail plus court qu'avec la chirurgie.", "wses_app_2020-79")
S(11, "[[dx1-p11-f2|Dafalgan]] oral est indiqué pour une douleur faible à modérée, ce qui ne constitue pas le traitement complet d'une appendicite compliquée.", "aips-47503-2")
S(11, "Le plafond journalier lu chez l'adulte est de 4000 mg, et il reste de 2000 mg entre 9 et 12 ans.", "aips-47503-2")
S(11, "Dès 40 kg, la prise orale va de 500 à 1000 mg, tandis que le maximum indiqué atteint 4 g.", "aips-47503-3")
S(11, "L'écart entre deux prises orales de l'adulte va de 4 à 8 heures, selon le même passage de posologie.", "aips-47503-3")
S(11, "Le comprimé de 1 g exige un poids supérieur à 50 kg, car le texte relie ce dosage au risque de surdosage.", "aips-47503-4")
S(11, "Si la voie orale est impossible, la forme intraveineuse se perfuse en 15 minutes pour une douleur légère à modérée de courte durée.", "aips-66702-2")
S(11, "Au-dessus de 50 kg, la dose intraveineuse est de 1 g, jusqu'à 4 fois par jour, sans dépasser 4 g en 24 heures.", "aips-66702-2")
S(11, "De 33 à 50 kg, la dose est de 15 mg par kg, au plus 4 fois par jour.", "aips-66702-2")
S(11, "Le plafond sur 24 heures, dans cette tranche, est de 60 mg par kg, et l'intervalle minimal est de 4 heures.", "aips-66702-2")
S(11, "Si la clairance est d'au plus 30 ml par minute, l'intervalle intraveineux minimal atteint 6 heures.", "aips-66702-2")
S(11, "Sous 10 ml par minute, la forme intraveineuse ne s'utilise pas, faute de données dans le texte.", "aips-66702-2")
S(11, "Au-dessus de 33 kg, en maladie hépatique chronique compensée, le plafond quotidien reste de 2 g.", "aips-66702-2")
S(11, "La durée maximale de ce traitement intraveineux est de 2 jours chez l'adulte et chez l'enfant.", "aips-66702-2")
S(11, "[[dx1-p11-f3|Algifor]] Liquid Caps 400 n'a pas l'appendicite parmi ses indications d'automédication, donc il ne constitue pas l'antalgie de cette leçon.", "aips-65372-2")
S(11, "Son plafond d'automédication est de 1200 mg par jour pendant 3 jours au plus, ce qui n'est pas un schéma d'appendicite.", "aips-65372-2")
S(11, "L'ulcère, l'hémorragie et la maladie inflammatoire intestinale contre-indiquent cet ibuprofène, ainsi que le troisième trimestre.", "aips-65372-2")
S(11, "La cœlioscopie de l'adulte, lorsque le matériel existe, diminue la morbidité par rapport à la voie ouverte dans la synthèse initiale.", "wses_app_2020-35")
S(11, "Chez l'enfant, la recommandation 4.2 indique la cœlioscopie, avec une preuve haute et une force forte.", "wses_app_2020-88")

H(11, '<h4><em>11.C Surveillance</em></h4>')
S(11, "Après un traitement non opératoire, la récidive peut atteindre 39 % à 5 ans, donc la surveillance ne s'arrête pas à la sortie.", "wses_app_2020-79")
S(11, "L'arrêt de l'antibiotique de la forme compliquée reste guidé par la clinique et la biologie, en général après 3 à 5 jours.", "wses_app_2020-307")
S(11, "Un délai opératoire au-delà de 24 heures reste un risque d'issue défavorable, et non une attente neutre.", "wses_app_2020-85")
S(11, "Chez la femme enceinte, une échographie répétée a augmenté le rendement diagnostique sans hausse des perforations dans une série citée.", "wses_app_2020-204")

H(11, '<h4><em>11.D Pronostic et sortie</em></h4>')
S(11, "La mortalité non gangréneuse reste sous 0,1 %, la mortalité gangréneuse atteint 0,6 %, et la forme perforée avoisine 5 %.", "wses_app_2020-33")
S(11, "La sortie après une forme non compliquée suppose le geste fait dans le créneau de 24 heures, ou un plan explicite de traitement non opératoire.", "wses_app_2020-85")
S(11, "La guérison du traitement non opératoire ne se décrète pas à la sortie, car l'échec et la récidive à 5 ans sont annoncés.", "wses_app_2020-79")
S(11, "Dans une série de femmes enceintes, l'appendice était normal dans 17,6 % des cas et l'appendicectomie blanche atteignait 17,7 %.", "wses_app_2020-204")
S(11, "L'échographie initiale était diagnostique dans 57,9 % de cette série, et 55,8 % ont eu un examen répété.", "wses_app_2020-204")
S(11, "75,9 % des appendicites de cette série de grossesse étaient non compliquées, et 6,5 % étaient compliquées.", "wses_app_2020-204")

H(11, '''<div class="t" style="overflow-x:auto"><table>
<caption>Médicaments dont le texte suisse a été lu.</caption>
<thead><tr><th>Spécialité</th><th>Dose lue</th><th>Voie et durée</th><th>Limite lue</th><th>Extrait</th></tr></thead>
<tbody>
<tr><td>Dafalgan, paracétamol, n° 47503<sup class="r"><a href="#sb-aips-47503-2">aips-47503-2</a></sup></td><td>Plafond adulte 4000 mg par jour ; de 9 à 12 ans, 2000 mg ; dès 40 kg, 500 à 1000 mg par prise<sup class="r"><a href="#sb-aips-47503-2">aips-47503-2</a></sup><sup class="r"><a href="#sb-aips-47503-3">aips-47503-3</a></sup></td><td>Orale, écart de 4 à 8 heures<sup class="r"><a href="#sb-aips-47503-3">aips-47503-3</a></sup></td><td>Douleur faible à modérée, pas le traitement d'une appendicite compliquée</td><td>aips-47503</td></tr>
<tr><td>Dafalgan intraveineux, n° 66702<sup class="r"><a href="#sb-aips-66702-2">aips-66702-2</a></sup></td><td>Au-dessus de 50 kg : 1 g jusqu'à 4 fois, maximum 4 g ; de 33 à 50 kg : 15 mg par kg, maximum 60 mg par kg<sup class="r"><a href="#sb-aips-66702-2">aips-66702-2</a></sup></td><td>Perfusion de 15 minutes, écart minimal de 4 heures, durée maximale de 2 jours<sup class="r"><a href="#sb-aips-66702-2">aips-66702-2</a></sup></td><td>Clairance inférieure à 10 ml par minute : ne pas utiliser</td><td>aips-66702</td></tr>
<tr><td>Algifor Liquid Caps 400, n° 65372<sup class="r"><a href="#sb-aips-65372-2">aips-65372-2</a></sup></td><td>Plafond d'automédication 1200 mg par jour<sup class="r"><a href="#sb-aips-65372-2">aips-65372-2</a></sup></td><td>Au plus 3 jours<sup class="r"><a href="#sb-aips-65372-2">aips-65372-2</a></sup></td><td>Pas d'indication lue pour l'appendicite ; ulcère et troisième trimestre contre-indiqués</td><td>aips-65372</td></tr>
</tbody></table></div>''')

W(11, "dx1-p11-f1", "Urgence — conduite chronologique", [
    ("Dès que la forme compliquée est reconnue, l'antibiotique à spectre digestif commence, sans attendre la fin du bilan de confort.", "wses_app_2020-310"),
    ("De 0 à 60 minutes avant l'incision, une dose unique à large spectre est recommandée, quelle que soit l'inflammation.", "wses_app_2020-110"),
    ("Si la forme est non compliquée, cette dose préopératoire ne se prolonge pas après l'opération.", "wses_app_2020-110"),
    ("La cœlioscopie de la forme non compliquée reste prévue sur la prochaine liste, dans les 24 heures.", "wses_app_2020-85"),
    ("Si le foyer compliqué est contrôlé, la durée usuelle reste de 3 à 5 jours, et l'essai cité compare environ 4 jours à environ 8 jours.", "wses_app_2020-307"),
    ("Le piège est d'ajouter des jours d'antibiotique à une forme non compliquée déjà opérée.", "wses_app_2020-110"),
])

W(11, "dx1-p11-f2", "Paracétamol lu pour cette leçon", [
    ("L'indication orale est la douleur faible à modérée et la fièvre, donc l'appendicite compliquée dépasse ce cadre.", "aips-47503-2"),
    ("Le plafond est de 4000 mg par jour chez l'adulte et de 2000 mg entre 9 et 12 ans.", "aips-47503-2"),
    ("Dès 40 kg, la prise orale va de 500 à 1000 mg, et le maximum lu est de 4 g.", "aips-47503-3"),
    ("Au-dessus de 50 kg, la perfusion est de 1 g jusqu'à 4 fois par jour, sans dépasser 4 g.", "aips-66702-2"),
    ("De 33 à 50 kg, la perfusion est de 15 mg par kg, avec un plafond de 60 mg par kg en 24 heures.", "aips-66702-2"),
    ("Le déficit en glucose-6-phosphate déshydrogénase contre-indique la forme intraveineuse, car une anémie hémolytique est possible.", "aips-66702-2"),
])

W(11, "dx1-p11-f3", "Ibuprofène d'automédication", [
    ("Algifor Liquid Caps 400 vise des douleurs articulaires, dorsales, dentaires ou menstruelles, et la fièvre grippale.", "aips-65372-2"),
    ("L'appendicite n'est pas dans cette liste, donc l'indication ne se déduit pas du symptôme abdominal.", "aips-65372-2"),
    ("Le plafond lu est de 1200 mg par jour pendant 3 jours au plus.", "aips-65372-2"),
    ("L'ulcère, l'hémorragie digestive et la maladie inflammatoire intestinale contre-indiquent cet ibuprofène, car le texte les liste.", "aips-65372-2"),
    ("Le troisième trimestre contre-indique aussi la molécule, ce qui croise la grossesse déjà hors traitement non opératoire.", "aips-65372-2"),
])

W(11, "dx1-p11-f4", "Traitement non opératoire", [
    ("Il se discute pour une forme non compliquée sans coprolithe, et la recommandation est forte, de classe 1A.", "wses_app_2020-80"),
    ("La récidive peut atteindre 39 % à 5 ans, ce qui se dit avant le choix.", "wses_app_2020-79"),
    ("Les complications globales à 5 ans sont moindres qu'avec la chirurgie dans les méta-analyses citées, et l'arrêt de travail est plus court.", "wses_app_2020-79"),
    ("L'échec et une forme compliquée méconnue font partie de l'avertissement obligatoire avant le choix.", "wses_app_2020-80"),
    ("Pendant la grossesse, cette voie est déconseillée, avec une preuve très faible et une suggestion faible.", "wses_app_2020-80"),
])

# --- 12 ---
S(12, "La prévention primaire passe par ne pas confirmer l'appendicite sur Alvarado chez l'adulte, car cela évite une opération inutile.", "wses_app_2020-64")
S(12, "Utiliser AIR et AAS dans le groupe à bas risque diminue l'appendicectomie blanche, ce qui est une prévention de geste inutile.", "wses_app_2020-65")
S(12, "La prévention secondaire reconnaît tôt la récidive après traitement non opératoire, puisque le risque atteint 39 % à 5 ans.", "wses_app_2020-79")
S(12, "Revoir une douleur qui persiste après une imagerie négative relève de cette prévention, car la cœlioscopie reste recommandée.", "wses_app_2020-75")
S(12, "La prévention tertiaire limite l'infection de paroi par la dose unique donnée de 0 à 60 minutes avant l'incision.", "wses_app_2020-110")
S(12, "Préférer la cœlioscopie chez l'enfant diminue l'infection de site, donc cette voie fait partie de la prévention des suites.", "wses_app_2020-88")
S(12, "Ne pas prolonger l'antibiotique après une forme non compliquée évite une exposition inutile, selon la recommandation 7.1.", "wses_app_2020-110")
S(12, "Aucune de ces mesures ne reste un substitut au contrôle d'un foyer déjà perforé, car la source doit être traitée.", "wses_app_2020-111")

# --- 13 ---
S(13, "AIR et AAS excluent et stratifient, tandis qu'Alvarado ne confirme pas l'appendicite de l'adulte.", "wses_app_2020-65")
S(13, "L'échographie au lit vient en premier si une image est nécessaire, et le scanner à faible dose suit l'échographie négative du jeune.", "wses_app_2020-73")
S(13, "La forme non compliquée sans coprolithe s'opère dans les 24 heures, ou se traite sans opération après un avertissement de récidive.", "wses_app_2020-85")
S(13, "La dose antibiotique unique se donne de 0 à 60 minutes avant l'incision, et elle ne se poursuit pas si la forme est simple.", "wses_app_2020-110")
S(13, "Le paracétamol oral a un plafond lu de 4000 mg par jour, car l'information professionnelle interdit de le dépasser.", "aips-47503-2")
S(13, "La perforation, l'abcès ou la péritonite purulente imposent le contrôle du foyer, car le traitement non opératoire ne les couvre pas.", "wses_app_2020-267")

# --- 14 ---
S(14, "Peut-on confirmer l'appendicite de l'adulte avec Alvarado, puisque le score existe ?", "wses_app_2020-64")
S(14, "La recommandation 1.3 indique de ne pas confirmer l'appendicite de l'adulte avec Alvarado.", "wses_app_2020-64")
S(14, "La réponse reste non, car un score sous 5 sert à exclure sans confirmer l'appendicite de l'adulte.", "wses_app_2020-117")
S(14, "Faut-il poursuivre un antibiotique après l'appendicectomie d'une forme non compliquée déjà opérée ?", "wses_app_2020-110")
S(14, "La réponse est non, car la recommandation 7.1 s'y oppose, alors que la dose unique préopératoire reste indiquée.", "wses_app_2020-110")
S(14, "Quel plafond journalier de Dafalgan oral le texte fixe-t-il chez l'adulte ?", "aips-47503-2")
S(14, "La réponse est 4000 mg, car l'information professionnelle écrit ce plafond et non un arrondi supérieur.", "aips-47503-2")
S(14, "Pourquoi Algifor Liquid Caps 400 n'est-il pas l'antalgique choisi devant une appendicite aiguë ?", "aips-65372-2")
S(14, "La réponse est que l'indication lue ne contient pas ce diagnostic, et que l'ulcère contre-indique la spécialité.", "aips-65372-2")
S(14, "Un traitement non opératoire se propose-t-il en cas de coprolithe ou de grossesse ?", "wses_app_2020-80")
S(14, "La réponse est non, car la sélection exige l'absence de coprolithe, et la grossesse fait l'objet d'une suggestion contraire.", "wses_app_2020-80")
S(14, "Que reste une attente de plus de 24 heures après l'admission pour une forme non compliquée ?", "wses_app_2020-85")
S(14, "La réponse est un risque accru d'issue défavorable, car le texte sépare le délai jusqu'à 24 heures du délai qui le dépasse.", "wses_app_2020-85")

H(14, '''<div class="t" style="overflow-x:auto"><table>
<caption>Question, réponse, raison.</caption>
<thead><tr><th>Question</th><th>Réponse</th><th>Raison</th></tr></thead>
<tbody>
<tr><td>Alvarado confirme-t-il l'adulte ?</td><td>Non, il ne confirme pas l'adulte.</td><td>Il sert à exclure sous le seuil de 5, avec une sensibilité de 99 %.</td></tr>
<tr><td>Antibiotique après une forme simple opérée ?</td><td>Non, il ne se poursuit pas.</td><td>Une seule dose reste indiquée, de 0 à 60 minutes avant l'incision.</td></tr>
<tr><td>Plafond oral de paracétamol chez l'adulte ?</td><td>Le plafond lu est de 4000 mg par jour<sup class="r"><a href="#sb-aips-47503-2">aips-47503-2</a></sup>.</td><td>Le chiffre est repris tel quel, sans arrondi.</td></tr>
<tr><td>Traitement non opératoire si coprolithe ?</td><td>Non, cette voie est écartée.</td><td>La recommandation 2.1.1 exige l'absence de coprolithe, et annonce jusqu'à 39 % de récidive à 5 ans.</td></tr>
</tbody></table></div>''')

H(14, '<div class="finale">Ce cours, lu seul avec ses fenêtres, suffit-il pour gagner 90 à 100 % des points sur ce sujet et pour traiter ce patient en sécurité ? La réponse est réservée à l’audit de Bitunder.</div>')

out = os.path.join(os.path.dirname(__file__), 'fragments')
m.ecrire(out)
print('fenêtres', m.fen)
