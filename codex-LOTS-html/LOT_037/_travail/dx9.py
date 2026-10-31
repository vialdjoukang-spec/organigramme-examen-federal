from format_lecon import Lesson, paras, table, steps, ABBR

ABBR.update({'EBV':'virus Epstein–Barr','p16':'protéine utilisée comme marqueur dans certains carcinomes associés au papillomavirus','TEP':'tomographie par émission de positons','TNM':'classification de la tumeur, des ganglions régionaux et des métastases à distance'})
l=Lesson('Adénopathie cervicale maligne',9)
l.add('Une adénopathie cervicale maligne correspond à un {ganglion atteint par une tumeur maligne}. Elle peut révéler une métastase d’une tumeur voisine ou un lymphome. Le diagnostic exige un prélèvement adapté, pas une conclusion fondée sur la palpation seule.',paras(
    'Dans une métastase ganglionnaire, des cellules provenant d’une autre tumeur colonisent le ganglion. Dans un lymphome, la maladie concerne des cellules du système lymphatique et doit être précisément typée. Ces mécanismes ne conduisent pas aux mêmes bilans ni aux mêmes traitements.',
    'Une métastase cervicale peut provenir notamment d’une tumeur des voies aérodigestives supérieures, de la thyroïde ou de la peau. Le siège ganglionnaire et les caractéristiques anatomopathologiques orientent la recherche. Une lésion primitive peut être petite ou non visible au premier examen.',
    'La formule sans primitif retrouvé s’applique après un bilan approprié, pas après un simple examen de la bouche. Une atteinte ganglionnaire régionale ne signifie pas automatiquement une maladie métastatique à distance ou un stade terminal.'
),(52,55,56))
l.add('Le {terrain et la nature de la tumeur} orientent le risque. Une masse persistante chez l’adulte doit faire rechercher une cause tumorale. L’absence de tabagisme n’exclut pas un cancer.',paras(
    'Les HUG décrivent les carcinomes épidermoïdes associés au tabac et ceux associés au papillomavirus parmi les cancers de la tête et du cou. Une présentation ganglionnaire peut donc survenir sans les facteurs de risque classiques attendus.',
    'L’âge, les expositions, les antécédents de cancer et les symptômes du territoire drainé contribuent à l’évaluation. Chez l’enfant, une cause infectieuse est fréquente, mais un ganglion suspect, une atteinte disséminée ou des anomalies générales nécessitent un parcours pédiatrique adapté.',
    'Les proportions de types de cancers de la tête et du cou ne représentent pas la probabilité de malignité de toute masse cervicale. Aucun taux suisse actuel ni classement comparatif des dix diagnostics de gonflement n’a été établi dans ces lectures.'
),(42,52,54,56))
l.add('L’{infiltration tumorale du ganglion} explique sa croissance et certains changements de structure. Une nécrose peut donner un aspect kystique trompeur. Le prélèvement doit fournir l’information nécessaire au type de tumeur suspecté.',paras(
    'Une prolifération ou une infiltration tumorale modifie la structure normale du ganglion. Le volume, la consistance et la mobilité peuvent évoluer. Cependant, une petite taille ou une mobilité conservée ne suffisent pas à prouver la bénignité.',
    'Une métastase peut comporter des zones liquides ou nécrotiques. L’aspect kystique d’une masse adulte n’autorise donc pas le diagnostic automatique de kyste congénital. Le prélèvement doit cibler une zone informative et un résultat insuffisant reste à réévaluer.',
    'Un examen de cellules et une analyse d’un fragment tissulaire n’apportent pas exactement la même information. La suspicion de lymphome nécessite notamment un matériel permettant le typage. Une ponction pauvre ne remplace pas un diagnostic anatomopathologique complet.'
)+table(['Mécanisme ou question','Exploration','Conséquence thérapeutique'],[
    ['Métastase d’une tumeur de proximité','Imagerie, examen du territoire et prélèvement ganglionnaire.','Traiter le cancer et son extension régionale dans une stratégie coordonnée.'],
    ['Maladie lymphomateuse','Prélèvement tissulaire suffisant et analyses spécialisées.','Choisir un traitement propre au sous-type ; l’ablation d’un seul ganglion ne suffit pas comme règle générale.'],
    ['Zone kystique ou nécrotique','Échographie et prélèvement ciblé selon le contexte.','Ne pas déclarer la masse bénigne sur son seul contenu liquide.'],
    ['Compression ou atteinte fonctionnelle','Évaluation respiratoire, laryngée et anatomique adaptée.','Stabiliser les fonctions menacées avec les spécialistes.']
]),(6,52,53,55,56))
l.add('Le tri cherche d’abord une {menace respiratoire, une complication ou un retard diagnostique}. Une masse peu douloureuse peut être importante. La prise en charge rapide ne signifie pas un geste non planifié sur le ganglion.',table(['Situation','Interprétation possible','Conduite'],[
    ['Dyspnée, stridor ou déglutition très altérée','Compression ou atteinte des voies aériennes.','Évaluation hospitalière urgente ; appel au 144 hors hôpital si détresse.'],
    ['Gonflement facial avec signes veineux thoraciques ou symptômes neurologiques','Obstacle veineux central ou autre complication.','Évaluation urgente de la cause et du retentissement.'],
    ['Masse adulte persistante, dure, fixée, kystique ou sans foyer infectieux convaincant','Origine tumorale à exclure.','Orientation rapide pour imagerie et prélèvement adaptés.'],
    ['Adénopathies multiples avec pâleur, saignement inhabituel ou altération générale','Hémopathie ou autre maladie systémique possible.','Bilan sanguin et avis spécialisé rapides selon retentissement.'],
    ['Masse pulsatile ou suspicion de lésion vasculaire','La ponction peut être dangereuse.','Caractériser la lésion avant tout prélèvement.']
]),(3,42,52,54,56))
l.add('L’anamnèse reconstitue la {durée, le territoire et les symptômes associés}. Elle recherche des indices de tumeur primitive ou de maladie systémique. Un traitement antibiotique antérieur n’établit pas le diagnostic.',steps(
    'Dater la découverte et la croissance ; noter si la masse a réellement régressé ou seulement cessé d’être douloureuse.',
    'Rechercher dysphagie, changement de voix, douleur pharyngée, lésion buccale ou douleur irradiée dans l’oreille pour orienter le territoire ORL.',
    'Demander lésion cutanée de la face, du cuir chevelu ou de l’oreille et antécédents thyroïdiens ou tumoraux.',
    'Relever tabac, alcool et facteurs de risque sans exclure un cancer en leur absence.',
    'Rechercher fièvre persistante, sueurs nocturnes, amaigrissement et autres aires ganglionnaires ou symptômes généraux.',
    'Préciser antibiotiques, corticoïdes, anticoagulants, biopsies et imageries déjà effectués afin de préparer la suite sans répéter inutilement les actes.'
),(3,42,52,53,55,56))
l.add('L’examen décrit la {masse et les territoires potentiellement en cause}. Il doit aussi apprécier voix, respiration et alimentation. Une palpation rassurante ne remplace pas le prélèvement lorsqu’il est indiqué.',paras(
    'Inspecter et palper doucement les chaînes ganglionnaires des deux côtés. Décrire localisation, nombre, dimensions, consistance, mobilité, douleur et peau. Le repère attendu est l’absence de masse pathologique ; de petits ganglions réactionnels peuvent toutefois être palpables.',
    'Examiner cavité buccale, langue, oropharynx et peau de la face, des oreilles et du cuir chevelu. L’examen des voies aérodigestives supérieures peut nécessiter une nasofibroscopie réalisée par le spécialiste. Une bouche sans lésion évidente ne clôt pas la recherche.',
    'Rechercher une autre masse cervicale, notamment thyroïdienne ou salivaire, et d’autres aires ganglionnaires. L’examen général et le bilan sanguin orientent une maladie lymphomateuse ou une autre cause systémique.',
    'Apprécier l’état nutritionnel et les possibilités de boire ou de s’alimenter. Ces données participent immédiatement à l’organisation des soins, même avant le nom définitif de la tumeur.'
),(42,52,54,55,56))
l.add('L’approche syndromique distingue {métastase probable, lymphome possible et autre masse}. Les signes orientent le prélèvement et le bilan. Ils ne permettent pas de choisir une chimiothérapie.',table(['Profil','Indices','Suite'],[
    ['7.1 — Métastase cervicale possible','Masse localisée avec symptômes ORL, cutanés ou thyroïdiens, parfois sans primitif évident.','Examiner les territoires, cartographier et prélever.'],
    ['7.2 — Lymphome ou hémopathie possible','Plusieurs aires atteintes, signes généraux ou anomalies du sang peuvent être présents.','Préparer un prélèvement tissulaire suffisant et un bilan hématologique.'],
    ['7.3 — Masse kystique adulte','Une métastase nécrotique peut imiter une lésion congénitale.','Ne pas conclure à la bénignité ; organiser le parcours spécialisé.'],
    ['7.4 — Adénite ou autre lésion','Contexte inflammatoire, salivaire, thyroïdien ou vasculaire possible.','Vérifier la nature de la masse et réévaluer une évolution atypique.']
]),(6,42,52,53,54,56))
l.add('Le {diagnostic positif de malignité} repose sur la preuve anatomopathologique. L’examen et l’imagerie désignent ce qu’il faut prélever. Le résultat doit être suffisamment précis pour guider le traitement.',paras(
    'L’échographie peut confirmer le caractère ganglionnaire et guider une cytoponction. Celle-ci prélève des cellules ; une microbiopsie prélève davantage de tissu. Le choix dépend de la lésion et des analyses nécessaires.',
    'Pour un lymphome, la Ligue suisse contre le cancer souligne la nécessité d’un échantillon tissulaire et le rôle de la biopsie ganglionnaire. Une excision ou une autre technique de prélèvement se discute avec les spécialistes selon accessibilité, risques et rendement attendu.',
    'Un prélèvement non contributif n’est pas un résultat bénin. Le clinicien confronte le compte rendu à la persistance de la masse et aux images. Une discordance appelle un nouvel examen ou un nouveau prélèvement ciblé.',
    'Les marqueurs complémentaires peuvent orienter le primitif et le type de maladie. Dans les carcinomes épidermoïdes sans porte d’entrée, le statut viral et les examens anatomopathologiques sont interprétés dans le parcours spécialisé. Le stade utilise la classification actuellement applicable au cancer identifié.'
),(52,53,55,56))
l.add('Les {examens complémentaires} précisent nature, primitif et extension. L’imagerie ne remplace pas le tissu. Le bilan doit aussi préserver les informations nécessaires aux étapes suivantes.',
    '<h3>9.a — Examen de référence</h3>'+paras('La preuve anatomopathologique fonde le diagnostic de malignité et son type. Prévenir l’équipe de prélèvement et le laboratoire lorsqu’un lymphome ou une infection spécifique est possible, pour organiser les échantillons et leurs analyses. Un fragment mal choisi ou insuffisant peut imposer de répéter le geste.')+
    '<h3>9.b — Première intention</h3>'+paras('L’échographie caractérise les masses superficielles et guide le prélèvement. Pour une masse adulte suspecte ou persistante sans cause infectieuse évidente, l’ADERIM recommande d’emblée une imagerie en coupe adaptée. Un scanner cervical ou cervico-thoracique injecté recherche notamment le primitif et l’extension selon le siège.',
    'L’hémogramme et les examens biologiques sont choisis selon les signes généraux et l’hypothèse. Un hémogramme normal n’exclut pas un lymphome ni une métastase ganglionnaire.')+
    table(['Résultat','Interprétation','Conduite'],[
        ['Carcinome au prélèvement','Une tumeur épithéliale est identifiée.','Orienter la recherche du primitif et le bilan d’extension selon son profil.'],
        ['Prolifération lymphoïde nécessitant typage','La classification précise reste indispensable.','Compléter le matériel et les analyses avec hématologie et pathologie.'],
        ['Prélèvement pauvre ou non diagnostique','La cause de la masse n’est pas établie.','Reprendre le ciblage ou la technique si la suspicion persiste.'],
        ['Image kystique chez l’adulte','Le contenu liquide ne prouve pas une lésion congénitale bénigne.','Poursuivre le bilan étiologique.'],
        ['Anomalie potentiellement vasculaire','Un geste aveugle peut être dangereux.','Caractériser avant ponction et solliciter les spécialistes.']
    ])+
    '<h3>9.c — Alternatives ciblées</h3>'+paras('Une imagerie par résonance magnétique peut être choisie selon le territoire ou les contre-indications. Une microbiopsie ou une biopsie-exérèse remplace ou complète une cytoponction lorsqu’elle ne fournit pas l’information nécessaire. Chez l’enfant, l’échographie est privilégiée initialement selon le contexte.')+
    '<h3>9.d — Seconde intention et extension</h3>'+paras('La tomographie par émission de positons associée au scanner, l’endoscopie et d’autres examens sont discutés selon histologie et recherche du primitif. Le prélèvement médullaire n’est pas un examen automatique de toute masse cervicale. Le programme d’examens évite les gestes qui pourraient compliquer inutilement la suite.'),(52,53,54,55,56))
l.add('L’{arbre décisionnel} commence par l’urgence, puis organise la preuve. Le parcours dépend de la suspicion anatomopathologique. Une attente sans suivi ou des traitements empiriques répétés peuvent retarder le diagnostic.',steps(
    'Si respiration, déglutition ou circulation sont menacées, alors organiser la stabilisation hospitalière avec les équipes capables de traiter la complication.',
    'Si la masse reste suspecte ou persistante sans cause infectieuse claire, alors adresser rapidement pour examen spécialisé et imagerie appropriée.',
    'Si une origine ganglionnaire tumorale est possible, alors choisir un prélèvement avec le spécialiste et le pathologiste selon les analyses attendues.',
    'Si le résultat est non contributif ou discordant, alors poursuivre le bilan plutôt que déclarer la masse bénigne.',
    'Si un carcinome est identifié, alors rechercher le primitif et l’extension ; si un lymphome est identifié, alors préciser le sous-type et son bilan propre.',
    'Si les données sont réunies, alors discuter la stratégie multidisciplinaire et les besoins de soutien avec le patient.'
),(52,53,54,55,56))
l.add('La {prise en charge en Suisse} associe diagnostic rapide, discussion spécialisée et soutien du patient. Le traitement dépend du type et du stade réels. Une adénopathie maligne n’a pas un protocole anticancéreux unique.',
    '<h3>11.A — But</h3>'+paras('Sécuriser les fonctions menacées, obtenir un diagnostic exploitable et proposer une stratégie adaptée au cancer et au patient. Préserver nutrition, déglutition, communication et qualité de vie fait partie du traitement. Les objectifs curatifs ou de contrôle sont expliqués après le bilan.')+
    '<h3>11.B — Moyens</h3>'+paras('Commencer par les complications nécessitant un soin urgent. Ensuite, organiser l’examen ORL ou hématologique et le prélèvement. L’ablation ouverte d’un ganglion cervical ne doit pas être un geste isolé non coordonné lorsqu’une métastase ORL est suspectée ; une biopsie-exérèse peut au contraire être choisie pour établir certains lymphomes.',
    'Le plan des cancers de la tête et du cou est discuté en réunion multidisciplinaire aux HUG. Selon les données, il peut associer chirurgie du primitif et des territoires ganglionnaires, radiothérapie et traitements systémiques. Les indications varient selon localisation, extension, marqueurs et état général.',
    'Un lymphome suit son propre parcours hématologique. La chirurgie d’un ganglion peut établir le diagnostic sans constituer le traitement complet. Certains sous-types relèvent d’un traitement rapide, d’autres d’une stratégie différente après typage ; aucune conduite ne se déduit du seul mot lymphome.',
    'Les anticancéreux, doses et associations sont choisis après identification du cancer, bilan et vérification de leurs informations professionnelles suisses. Il serait inapproprié de prescrire un schéma unique à une masse dont la nature n’est pas connue. Cette monographie décrit le parcours initial et ne vaut pas un protocole oncologique exhaustif.',
    'Éviter antibiotiques répétés sans argument infectieux et corticoïdes empiriques devant une suspicion de lymphome, car ils peuvent perturber le diagnostic. Une nécessité vitale éventuelle de traitement avant la preuve complète est décidée avec les spécialistes, sans retarder les gestes de stabilisation.',
    'Préparer le prélèvement en relevant anticoagulants, troubles de l’hémostase et autres médicaments ; les interruptions sont décidées par le prescripteur. Pendant grossesse, allaitement, en pédiatrie ou sur terrain fragile, coordonner examens et traitement avec les équipes concernées.',
    'Évaluer la douleur, l’alimentation, l’hydratation et les besoins psychosociaux. Les soins dentaires, la nutrition et la rééducation de la déglutition sont intégrés au projet de traitement lorsqu’ils sont indiqués. L’annonce se fait avec une information claire et un interlocuteur identifié.')+
    '<h3>11.C — Surveillance</h3>'+paras('S’assurer que les rendez-vous, le prélèvement et le retour du résultat sont effectivement organisés. Une masse persistante ne doit pas se perdre entre deux consultations. Le médecin responsable vérifie la concordance du diagnostic et la réalisation du bilan d’extension.',
    'Pendant le traitement, les contrôles de réponse et de toxicité dépendent du protocole. Dans le parcours initial, toute nouvelle dyspnée, dysphagie importante, hémorragie ou altération rapide impose un contact urgent. Un résultat négatif mais non contributif ne ferme pas le dossier.')+
    '<h3>11.D — Pronostic et suivi</h3>'+paras('Le pronostic varie fortement selon origine, histologie, extension et réponse. Aucun taux unique ne peut être attribué à toutes les adénopathies malignes. Le suivi comprend contrôle de la maladie et des fonctions, soutien du patient et prise en charge des séquelles ; ses modalités sont définies par l’équipe.'),(42,52,53,55,56))
l.add('La {prévention et la limitation des retards} reposent sur les facteurs de risque et le suivi. Elles ne permettent pas d’exclure un cancer chez une personne sans exposition connue. Une masse inexpliquée nécessite une réponse documentée.',paras(
    'Aider le patient à réduire les expositions évitables, notamment le tabac, dans le parcours de soins. Les mesures de prévention spécifiques, dont la vaccination selon les recommandations suisses applicables, sont discutées dans leur contexte et ne remplacent pas le bilan d’une masse existante.',
    'La prévention secondaire consiste ici à identifier les signes suspects et à organiser le diagnostic. Ne pas rassurer uniquement parce que la masse est kystique, mobile ou peu douloureuse. Fixer qui vérifie sa régression ou le résultat du prélèvement.',
    'Après traitement, le suivi cherche aussi les troubles de déglutition, nutrition, voix et autres séquelles. Le patient doit connaître les changements nécessitant un nouvel avis et disposer d’un accès à l’équipe.'
),(6,52,53,56))
l.add('Les {points clés} relient suspicion, preuve et stratégie. L’anatomopathologie prime sur une impression de palpation. Un diagnostic précis permet d’éviter un traitement inadapté et des gestes qui compliquent le parcours.',steps(
    'Considérer une masse adulte persistante sans cause claire comme une situation à explorer.',
    'Rechercher le primitif et les complications sans présumer une origine unique.',
    'Adapter le prélèvement à la suspicion de carcinome ou de lymphome.',
    'Réévaluer tout résultat non contributif ou discordant.',
    'Distinguer atteinte ganglionnaire régionale et métastase à distance.',
    'Coordonner traitement multidisciplinaire, soutien et suivi du résultat.'
),(52,53,54,55,56))
l.quiz([
    ('Une masse kystique cervicale chez l’adulte est-elle présumée congénitale bénigne ?','Non. Une métastase peut être kystique ou nécrotique ; le bilan étiologique doit être poursuivi.'),
    ('L’absence de tabagisme exclut-elle un cancer ORL ?','Non. D’autres profils existent, notamment les cancers associés au papillomavirus.'),
    ('Une atteinte ganglionnaire régionale signifie-t-elle forcément une métastase à distance ?','Non. Le territoire régional et les métastases à distance sont des dimensions distinctes de la classification.'),
    ('Une bouche sans lésion visible exclut-elle un primitif ORL ?','Non. L’examen spécialisé, l’imagerie et parfois l’endoscopie complètent la recherche.'),
    ('Quel examen établit la nature maligne ?','Un prélèvement anatomopathologique adapté, avec les analyses nécessaires au type de tumeur.'),
    ('Une cytoponction non contributive équivaut-elle à une cytologie bénigne ?','Non. Elle peut manquer de cellules ou ne pas fournir l’information nécessaire.'),
    ('Pourquoi une suspicion de lymphome doit-elle être signalée avant le prélèvement ?','Pour choisir une technique et un matériel permettant le typage et les analyses nécessaires.'),
    ('Faut-il toujours enlever d’emblée la masse du cou ?','Non. Le geste se coordonne avec le parcours diagnostique. Une biopsie-exérèse peut être appropriée pour un lymphome, mais n’est pas un geste systématique pour toute masse.'),
    ('Une échographie seule suffit-elle toujours devant une masse adulte suspecte ?','Non. Une imagerie en coupe adaptée peut être nécessaire d’emblée pour rechercher primitif et extension.'),
    ('Pourquoi éviter des cures répétées d’antibiotiques sans signe infectieux ?','Elles peuvent retarder le diagnostic sans traiter la cause tumorale.'),
    ('Les corticoïdes empiriques sont-ils anodins avant le diagnostic de lymphome ?','Non. Ils peuvent modifier la maladie et le prélèvement ; une éventuelle urgence doit être discutée avec les spécialistes.'),
    ('L’ablation d’un ganglion atteint de lymphome constitue-t-elle toujours le traitement complet ?','Non. Elle peut servir au diagnostic ; le traitement dépend du sous-type et de son extension.'),
    ('Quel symptôme impose de faire passer la stabilisation avant le bilan programmé ?','Une détresse respiratoire, une déglutition gravement altérée ou une autre complication menaçante.'),
    ('Qui doit vérifier qu’un résultat de biopsie revient et conduit à une décision ?','Un professionnel responsable clairement identifié, avec un rendez-vous ou une modalité de retour organisée avec le patient.')
],(6,42,52,53,54,55,56))
l.write()
