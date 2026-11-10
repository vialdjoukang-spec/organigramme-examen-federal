from rendu import Point

p = Point(3)
p.h('Une forme visible peut résulter de mécanismes très différents')
p.p('La croissance modifie normalement l’axe des membres inférieurs ; une déviation observée pendant l’enfance ne traduit donc pas nécessairement une destruction tissulaire.', 'p82-genou')
p.p('À l’inverse, l’arthrose de la main associe une atteinte du cartilage, une inflammation et des changements articulaires pouvant déformer les doigts.', 'p82-arthrose')
p.p('Dans le pied neuropathique, le processus inflammatoire de Charcot lèse les structures et peut entraîner des fractures ou des luxations progressives.', 'p82-charcot')
p.p('Une rétraction palmaire peut provenir d’un épaississement cellulaire de l’aponévrose, alors qu’un défaut d’extension terminale peut résulter d’une rupture tendineuse.', ['p82-dupuytren', 'p82-maillet'])
p.fenetre('De PHEX au déficit de minéralisation : la chaîne métabolique de l’XLH', [
    ('Une mutation inactivante de PHEX est à l’origine de l’hypophosphatémie liée à l’X, ce qui définit une cause génétique précise.', 'p82-xlh-definition'),
    ('Cette anomalie entraîne une libération excessive de facteur de croissance fibroblastique 23, ou FGF23, par les ostéocytes.', 'p82-xlh-mecanisme-bilan'),
    ('Au tubule proximal rénal, le FGF23 réduit l’activité des cotransporteurs sodium-phosphate NPT2a et NPT2c, donc la réabsorption du phosphate diminue.', 'p82-xlh-mecanisme-bilan'),
    ('Le phosphate est alors davantage éliminé dans les urines, ce qui contribue à une hypophosphatémie chronique.', 'p82-xlh-mecanisme-bilan'),
    ('Le FGF23 inhibe également l’activité de l’1α-hydroxylase, donc la production de calcitriol, forme active de vitamine D, diminue.', 'p82-xlh-mecanisme-bilan'),
    ('Cette disponibilité réduite du calcitriol diminue l’absorption intestinale du phosphate, ce qui renforce les conséquences des pertes rénales.', 'p82-xlh-mecanisme-bilan'),
    ('Le déficit chronique perturbe ensuite le squelette en croissance ; les os longs des membres inférieurs peuvent développer des déformations progressives.', 'p82-xlh-clinique'),
    ('La croissance du tronc reste relativement conservée tandis que celle des extrémités est entravée, ce qui produit une petite taille disproportionnée.', 'p82-xlh-clinique'),
])
p.h('Du tissu palmaire au défaut d’extension')
p.p('Dans Dupuytren, la prolifération de myofibroblastes produit un épaississement nodulaire ou cordonal de l’aponévrose palmaire située sous la peau.', 'p82-dupuytren')
p.p('Les cordes peuvent s’étendre vers les articulations digitales puis se raccourcir, ce qui maintient progressivement les doigts en flexion.', 'p82-dupuytren')
p.p('Cette rétraction ne régresse pas spontanément ; l’évolution fonctionnelle dépend donc notamment de la perte d’extension.', 'p82-dupuytren')
p.p('Dans le doigt en maillet, la lésion concerne au contraire le tendon extenseur terminal, avec perte de l’extension active de la dernière phalange.', 'p82-maillet')
p.p('La présence d’une plaie ou d’un fragment osseux change l’évaluation de cette rupture ; elle ne transforme pas la lésion en maladie aponévrotique.', ['p82-maillet', 'p82-dupuytren'])
p.fenetre('Souplesse, charge et formation de la voûte plantaire', [
    ('À la naissance, le pied est décrit comme mou, trapu et sans voûte visible, avec un coussinet graisseux marqué.', 'p82-plat-physio'),
    ('Pendant la croissance, l’architecture se développe progressivement ; une voûte peut apparaître hors charge avant d’être pleinement visible en position debout.', 'p82-plat-physio'),
    ('Dans le pied flexible, la voûte est présente assis et s’efface debout, ce qui relie l’aspect à la mise en charge.', 'p82-plat-examen'),
    ('Le passage sur la pointe des pieds redresse normalement le talon et reforme l’arche, ce qui permet d’apprécier la réductibilité.', 'p82-plat-examen'),
    ('L’extension dorsale du gros orteil tend passivement le fascia plantaire et peut reformer la voûte lors du test de Jack.', 'p82-plat-examen'),
    ('Si le talon ne se redresse pas et que la voûte reste effacée, la rigidité fait rechercher une autre cause, notamment une coalition.', 'p82-plat-examen'),
])
p.h('La géométrie et la résistance osseuses orientent les explorations')
p.p('Dans l’hallux valgus, les déplacements opposés du gros orteil et du premier métatarsien créent une saillie médiale exposée aux frottements.', 'p82-hallux')
p.p('Les contraintes de chaussage participent à la gêne, tandis que l’hérédité et le sexe figurent parmi les facteurs associés décrits.', 'p82-hallux')
p.p('Dans la scoliose, les composantes tridimensionnelles nécessitent une appréciation frontale, rotationnelle et sagittale, au lieu d’une seule mesure visuelle.', ['p82-scoliose-definition', 'p82-scoliose-clinique', 'p82-scoliose-radio'])
p.p('Dans une fracture distale du radius, la fragilité osseuse ou l’énergie traumatique contribue au contexte de rupture et de déplacement.', 'p82-radius')
p.p('Une déformation après fracture peut menacer les tissus voisins ; l’analyse mécanique doit donc rester associée à l’examen cutané et vasculo-nerveux.', 'p82-radius')
p.tableau(['Perturbation et conséquence', 'Exploration qui la précise', 'Conduite reliée au mécanisme'], [
    [('La perte rénale de phosphate et l’absorption intestinale réduite produisent une hypophosphatémie dans l’XLH.', 'p82-xlh-mecanisme-bilan'), ('Le phosphate sanguin, les pertes urinaires et la réabsorption tubulaire précisent ce mécanisme.', 'p82-xlh-mecanisme-bilan'), ('Le diagnostic précoce permet d’organiser un traitement métabolique destiné à limiter les conséquences squelettiques.', 'p82-xlh-clinique')],
    [('La rétraction des cordes palmaires limite progressivement l’extension dans Dupuytren.', 'p82-dupuytren'), ('La localisation des cordes et l’amplitude d’extension documentent le retentissement sur la main.', 'p82-dupuytren'), ('La stratégie thérapeutique cherche à améliorer l’extension et la fonction, en tenant compte de cette rétraction.', 'p82-dupuytren')],
    [('La rupture de l’extenseur terminal explique le déficit d’extension dans le doigt en maillet.', 'p82-maillet'), ('La recherche d’une plaie et d’une composante osseuse distingue les présentations de cette lésion.', 'p82-maillet'), ('La protection par attelle ou le traitement spécialisé vise la continuité et la fonction de l’appareil extenseur.', 'p82-maillet')],
    [('La souplesse permet à une arche plantaire aplatie en charge de se reconstituer hors charge.', 'p82-plat-examen'), ('Le passage sur la pointe des pieds et le test de Jack confrontent l’aspect statique à la réductibilité.', 'p82-plat-examen'), ('Lorsque le pied est indolore et fonctionnel, l’observation évite de traiter inutilement une variante physiologique.', 'p82-plat-examen')],
    [('L’inflammation neuropathique peut désorganiser les os et articulations du pied dans le Charcot actif.', 'p82-charcot'), ('Les signes inflammatoires et l’imagerie recherchent cette activité et ses conséquences structurelles.', 'p82-charcot'), ('L’immobilisation et la décharge débutent précocement pour promouvoir la rémission et prévenir une aggravation de la déformation.', 'p82-charcot')],
    [('Le déplacement fracturaire modifie la géométrie du radius et peut menacer les tissus voisins.', 'p82-radius'), ('Les radiographies complètent le bilan de la peau, des nerfs et de la perfusion.', 'p82-radius'), ('Le réalignement spécialisé répond notamment aux déplacements importants et aux menaces cutanées ou vasculo-nerveuses.', 'p82-radius')],
])
p.sauver()

p = Point(5)
p.h('L’entretien commence par le contexte et la chronologie utiles au triage')
p.p('Un traumatisme récent oriente vers la branche fracturaire, tandis que le mécanisme de haute énergie ou la fragilité osseuse précise son contexte.', 'p82-radius')
p.p('Chez une personne diabétique neuropathique, une rougeur et un gonflement récents du pied font rechercher une activité de Charcot.', 'p82-charcot')
p.p('Chez l’enfant, la douleur nocturne persistante, la fièvre ou la raideur empêchent de conclure trop vite à une variante de développement.', 'p82-plat-examen')
p.tableau(['Question clinique', 'Raison et conséquence pour la démarche'], [
    [('Le changement de forme est-il apparu après un traumatisme, et quel en était le mécanisme ?', 'p82-radius'), ('La haute énergie et la fragilité du sujet âgé définissent des contextes différents de fracture distale du radius.', 'p82-radius')],
    [('La personne utilise-t-elle des moyens auxiliaires, reçoit-elle une anticoagulation et quel est son niveau d’autonomie ?', 'p82-radius'), ('Les HUG intègrent ces éléments à l’anamnèse traumatique, car ils participent à la préparation de la prise en charge.', 'p82-radius')],
    [('La douleur de la main augmente-t-elle pendant les activités puis diminue-t-elle au repos ?', 'p82-arthrose'), ('Ce profil décrit le retentissement mécanique de l’arthrose et permet de cibler les activités devenues difficiles.', 'p82-arthrose')],
    [('Le pied fait-il surtout mal dans les chaussures, et d’autres orteils se déforment-ils ?', 'p82-hallux'), ('Le frottement de la saillie et les déformations associées font partie des manifestations de l’hallux valgus.', 'p82-hallux')],
    [('L’enfant rapporte-t-il des douleurs, une fatigabilité, une instabilité de marche ou une malposition inhabituelle du pied ?', 'p82-plat-examen'), ('Ces éléments font discuter une consultation spécialisée plutôt que la seule observation d’un pied souple indolore.', 'p82-plat-examen')],
    [('L’axe des jambes évolue-t-il avec la croissance et existe-t-il un retentissement fonctionnel ?', 'p82-genou'), ('Une évolution non spontanément résolutive doit être reconnue, afin de ne pas laisser progresser un trouble pathologique.', 'p82-genou')],
    [('Le doigt ne s’étend-il plus à son extrémité, et existe-t-il une plaie associée ?', 'p82-maillet'), ('Le défaut terminal et l’ouverture distinguent les présentations de lésion de l’appareil extenseur.', 'p82-maillet')],
    [('Des nodules ou cordes sont-ils apparus dans la paume, et la difficulté d’extension progresse-t-elle ?', 'p82-dupuytren'), ('Dupuytren se manifeste souvent par ces épaississements et par une gêne croissante malgré une douleur habituellement faible.', 'p82-dupuytren')],
    [('La rétraction est-elle bilatérale, familiale ou associée à des nodules plantaires ?', 'p82-dupuytren'), ('Ces associations contribuent à caractériser le terrain et certaines évolutions plus agressives de Dupuytren.', 'p82-dupuytren')],
    [('L’adolescent présente-t-il des douleurs, des symptômes neurologiques ou une poussée de croissance récente ?', 'p82-scoliose-clinique'), ('Ces renseignements orientent l’examen d’une scoliose et la recherche d’une cause secondaire.', 'p82-scoliose-clinique')],
    [('Quand les premières règles sont-elles survenues, et quelle est l’évolution de la taille ?', 'p82-scoliose-clinique'), ('La maturation et la croissance permettent d’apprécier le besoin d’évaluation de l’âge osseux dans le contexte de scoliose.', 'p82-scoliose-clinique')],
    [('Les jambes se déforment-elles progressivement avec une croissance disproportionnée ou des abcès dentaires ?', 'p82-xlh-clinique'), ('Ces associations renforcent une hypothèse métabolique telle que l’XLH, au lieu d’une variation isolée de l’axe.', 'p82-xlh-clinique')],
])
p.fenetre('Une histoire familiale utile ne remplace pas les signes cliniques', [
    ('Les antécédents familiaux contribuent à l’évaluation d’une scoliose, bien que son mode précis de transmission reste non établi dans la synthèse suisse.', ['p82-scoliose-definition', 'p82-scoliose-clinique']),
    ('Une agrégation familiale est décrite dans Dupuytren, ainsi qu’une association avec le diabète, ce qui oriente l’entretien ciblé.', 'p82-dupuytren'),
    ('Dans l’XLH, des mutations spontanées peuvent retarder la reconnaissance ; une absence d’antécédent familial ne doit donc pas interrompre un bilan motivé.', 'p82-xlh-definition'),
    ('Les anomalies de croissance et les manifestations dentaires restent ainsi des éléments à rechercher même lorsque la famille ne rapporte pas de diagnostic connu.', 'p82-xlh-clinique'),
])
p.h('Drapeaux rouges et décisions associées')
p.tableau(['Drapeau rouge', 'Signification clinique', 'Action imposée'], [
    [('Une fracture du poignet est ouverte ou menace les tissus cutanés et vasculo-nerveux.', 'p82-radius'), ('Le déplacement peut compromettre la peau, les nerfs ou la perfusion, ce qui active la priorité 🚩 E1.', 'p82-radius'), ('La garde de chirurgie de la main est appelée et la prise en charge urgente du bilan et du réalignement est organisée.', 'p82-radius')],
    [('Un pied diabétique neuropathique devient rouge, chaud et gonflé.', 'p82-charcot'), ('Un Charcot actif doit être considéré avant même que la déformation soit fixée, ce qui active la priorité 🚩 E2.', 'p82-charcot'), ('La décharge et l’immobilisation commencent dès la suspicion, avec exploration et suivi rapproché.', 'p82-charcot')],
    [('L’enfant présente des douleurs nocturnes tenaces ou des douleurs associées à un état fébrile.', 'p82-plat-examen'), ('Une infection ou une maladie tumorale doit être envisagée au lieu d’une variante physiologique.', 'p82-plat-examen'), ('Des investigations sont engagées sans délai pour préciser cette cause potentiellement grave.', 'p82-plat-examen')],
    [('Le pied est rigide ou s’inscrit dans une maladie neuromusculaire.', 'p82-plat-examen'), ('La mobilité réduite ou le contexte neurologique indique une situation différente du pied plat souple indolore.', 'p82-plat-examen'), ('Une évaluation orthopédique pédiatrique spécialisée est organisée pour préciser le diagnostic et les besoins thérapeutiques.', 'p82-plat-examen')],
    [('La scoliose s’accompagne de symptômes neurologiques ou d’une courbure atypique.', 'p82-scoliose-irm'), ('Une anomalie secondaire intrarachidienne doit être recherchée avant de maintenir le diagnostic idiopathique.', 'p82-scoliose-irm'), ('L’imagerie par résonance magnétique est discutée dans le bilan spécialisé selon ces indices.', 'p82-scoliose-irm')],
    [('La déformation des jambes progresse avec une croissance disproportionnée et d’autres manifestations osseuses ou dentaires.', 'p82-xlh-clinique'), ('Le tableau peut traduire une maladie métabolique dont les conséquences dépassent le seul alignement des membres.', 'p82-xlh-clinique'), ('Le bilan étiologique et l’orientation spécialisée sont organisés précocement, sans confondre cette priorité avec une réanimation urgente.', ['p82-xlh-clinique', 'p82-xlh-mecanisme-bilan'])],
])
p.sauver()
