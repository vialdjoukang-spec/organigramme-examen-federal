from rendu import Point
p=Point(7)
p.h('7.1 — Douleur régionale provoquée par la charge ou le traumatisme')
p.p('Le premier regroupement associe une localisation musculaire, un événement mécanique identifiable et une modification de la fonction. La contusion suit un impact direct ; les courbatures retardées apparaissent après une sollicitation inhabituelle, notamment excentrique.', ['p83-doms-contusion-clinique','doms-definition'])
p.p('L’inspection et la comparaison des amplitudes permettent ensuite de confronter le récit à un hématome, une ecchymose, une déformation ou une douleur provoquée. L’étirement et la contraction interrogent la structure symptomatique sans donner, à eux seuls, la nature histologique de la lésion.', 'rms-clinique')
p.fenetre('Ecchymose, hématome et limitation mécanique',[
 ('Dans une lésion musculaire aiguë, le tableau clinique recherche une ecchymose ou un hématome à l’inspection et une douleur provoquée à la palpation. Leur absence ne remplace pas le testing passif et actif.', 'rms-clinique'),
 ('La contusion relève d’un mécanisme direct, tandis que les courbatures relèvent d’une perturbation après charge. L’interrogatoire sur le moment exact de la douleur est donc indispensable avant de lire les signes locaux.', ['p83-doms-contusion-clinique','doms-definition']),
 ('Les DOMS comportent des modifications ultrastructurales et une réponse inflammatoire ; elles ne sont pas définies par une rupture macroscopique recherchée systématiquement en imagerie.', ['doms-mecanisme','doms-biologie-imagerie'])
])
p.h('7.2 — Douleur myofasciale localisée')
p.p('Une bande musculaire tendue portant une zone de sensibilité maximale, une contraction locale déclenchée par la palpation et une douleur propagée constituent la constellation myofasciale décrite par la DGN 2025.', 'p83-myofascial-fibro')
p.p('Le geste consiste à identifier la zone douloureuse à la pression dans cette bande puis à demander où la douleur se propage. La contraction visible et la reproduction de la douleur sont des observations à consigner séparément.', 'p83-myofascial-fibro')
p.fenetre('Point gâchette et douleur propagée',[
 ('Le point gâchette correspond ici au maximum local de douleur à la pression situé dans un faisceau tendu. La réponse locale de contraction se recherche pendant la palpation ; la douleur propagée est ressentie à distance de cette pression.', 'p83-myofascial-fibro'),
 ('La surcharge et de probables microtraumatismes interviennent dans la forme primaire. Le mécanisme de la forme secondaire demeure moins bien établi, ce qui ne transforme pas le diagnostic clinique en une preuve d’une lésion anatomique unique.', 'p83-myofascial-fibro')
])
p.h('7.3 — Douleur diffuse persistante avec sommeil non réparateur')
p.p('Des douleurs dans plusieurs régions, une fatigue physique ou mentale et un sommeil non réparateur orientent vers le syndrome fibromyalgique. La recherche de cette constellation ne dispense pas de vérifier une parésie, une atrophie ou une anomalie biologique qui orienterait ailleurs.', 'p83-myofascial-fibro')
p.fenetre('Fatigue, faiblesse et sensibilisation',[
 ('La fatigue appartient au vécu d’épuisement ; une parésie correspond à une diminution de force vérifiée par l’examen. La DGN demande de confronter la faiblesse rapportée aux constatations cliniques.', ['p83-myofascial-fibro','p83-phenotype']),
 ('La sensibilisation centrale et des anomalies de nocicepteurs périphériques ont été décrites dans des sous-groupes fibromyalgiques. Elles ne constituent pas un biomarqueur diagnostique utilisable pour attribuer toutes les douleurs à cette entité.', 'p83-myofascial-fibro'),
 ('Le sommeil et la fatigue sont recherchés par l’entretien, alors que le testing vérifie la capacité à produire un mouvement contre la pesanteur et une résistance. Ces informations se complètent au lieu d’être traduites en un unique adjectif « faible ».', ['p83-myofascial-fibro','s103'])
])
p.h('7.4 — Syndrome de faiblesse proximale et atteinte cutanée')
p.p('La dermatomyosite peut réunir une atteinte bilatérale, proximale et symétrique et des lésions cutanées évocatrices. Demander comment le patient monte une marche, se relève du sol ou quitte sa chaise sans utiliser ses bras permet de préciser le handicap proximal.', 'dx10-pnds-examen')
p.fenetre('Héliotrope et Gottron : regarder la bonne région',[
 ('L’érythème héliotrope est rose-liliacé et symétrique ; l’œdème violacé des paupières, particulièrement supérieures, donne une distribution évocatrice autour des yeux. L’inspection recherche cette topographie plutôt qu’une rougeur faciale indifférenciée.', 'dx10-cedef-heliotrope'),
 ('Aux mains, le signe de Gottron comporte des macules érythémateuses parfois squameuses dans la distribution des extenseurs ; les papules sont des lésions plates, infiltrées et violines. Décrire le relief et le siège évite de confondre ces deux termes.', 'dx10-cedef-gottron'),
 ('La composante musculaire de la dermatomyosite s’inscrit dans une vasculopathie périmysiale avec inflammation et atrophie périfasciculaire. La peau suggère une famille diagnostique, tandis que le bilan musculaire et d’organes précise son retentissement.', ['p83-dermato-histologie','p83-myopathies-gravite'])
])
p.fenetre('Déglutition et respiration : mesurer la gravité au-delà des membres',[
 ('Une toux liée à l’alimentation, une voix modifiée ou nasonnée et une anomalie du voile orientent vers une atteinte de déglutition. L’examen respiratoire recherche notamment un tirage, une respiration paradoxale ou une orthopnée.', 'dx10-pnds-examen'),
 ('La dysphagie peut entraîner une pneumonie d’inhalation et ne suit pas nécessairement la sévérité de la faiblesse généralisée. Elle justifie une évaluation spécifique de déglutition et l’intervention des équipes compétentes.', 'dx10-bsr-xi'),
 ('Une atteinte pulmonaire interstitielle, une myocardite ou une dysphagie sévère figurent parmi les critères de prise en charge urgente du PNDS ; la seule présence de myalgies n’a pas cette signification.', 'dx10-pnds-severite')
])
p.h('7.5 — Ceintures douloureuses et raides, avec recherche d’artérite')
p.p('Une douleur inflammatoire avec raideur du cou et des ceintures scapulaire ou pelvienne, bilatérale, évoque une pseudopolyarthrite rhizomélique. L’état général, la perte de poids et les marqueurs inflammatoires complètent cette orientation.', 'p83-pmr')
p.fenetre('Les signes crâniens qui changent l’urgence',[
 ('Une céphalée, une sensibilité du cuir chevelu, un épaississement temporal, une claudication mandibulaire ou un trouble visuel augmentent la suspicion d’artérite à cellules géantes. Ils se recherchent explicitement lorsque les ceintures sont douloureuses.', 'p83-eular26-signes-urgence'),
 ('Le danger est une lésion ischémique irréversible, notamment visuelle ; les symptômes crâniens conduisent à une orientation immédiate. Une PPR sans cette complication ne doit pas être artificiellement classée dans la même urgence.', ['p83-eular26-orientation','p83-eular26-signes-urgence'])
])
p.h('7.6 — Souffrance musculaire aiguë avec menace systémique')
p.p('Douleur importante, gonflement ou faiblesse associés à une augmentation rapide des CK orientent vers une rhabdomyolyse. Les urines sombres, l’anurie, les constantes anormales et les troubles métaboliques déterminent la priorité de soins.', ['e12','e13'])
p.fenetre('Gonflement et douleur à la mobilisation passive',[
 ('Une douleur disproportionnée et une douleur lors de la mobilisation passive des muscles d’un compartiment constituent des signes d’alarme du syndrome compartimental aigu. La pression dans l’espace myofascial menace la perfusion tissulaire.', 'p83-boast-loges-0'),
 ('L’examen des loges est une recherche de complication et non une simple description de douleur post-effort ; le diagnostic établi impose une décompression chirurgicale immédiate.', 'p83-boast-loges-3'),
 ('Une rhabdomyolyse peut survenir sans tableau urinaire typique complet ; l’évolution biologique et le retentissement rénal ou électrolytique restent indispensables au raisonnement.', ['p83-rhabdo-clinique','e13'])
])
p.tableau(['Regroupement','Signes fonctionnels','Signes physiques ou orientation'],[
 [('La forme régionale mécanique est liée à la charge ou à un impact.', 'p83-doms-contusion-clinique'),('Le patient localise la gêne et décrit sa chronologie.', 'rms-clinique'),('Comparer mobilité, douleur provoquée et signes cutanés locaux.', 'rms-clinique')],
 [('La forme diffuse persistante associe plusieurs dimensions.', 'p83-myofascial-fibro'),('Douleur, épuisement et sommeil non réparateur sont recherchés.', 'p83-myofascial-fibro'),('Une faiblesse objective ou une atrophie modifie le bilan différentiel.', 'p83-myofascial-fibro')],
 [('La forme proximale peut être immunomédiée.', 'dx10-pnds-examen'),('Lever de chaise, escaliers et déglutition précisent la fonction.', 'dx10-pnds-examen'),('La peau et les signes d’organes orientent le recours spécialisé.', ['dx10-cedef-gottron','dx10-pnds-severite'])],
 [('La forme aiguë systémique fait rechercher une nécrose musculaire.', 'e12'),('La douleur ou la faiblesse s’accompagne parfois d’urines foncées.', ['e12','e13']),('Constantes, rein, métabolisme et loges déterminent l’urgence.', 'e13')]
])
p.sauver()
