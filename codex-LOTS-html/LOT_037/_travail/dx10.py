from format_lecon import Lesson, paras, table, steps, ABBR
from anticoagulation import enoxaparine

ABBR.update({'VCS':'veine cave supérieure','CIRSE':'Cardiovascular and Interventional Radiological Society of Europe, société européenne de radiologie cardiovasculaire et interventionnelle','GGC':'Greater Glasgow and Clyde, service de santé de la région de Glasgow','SC':'sous-cutané','HIT':'thrombopénie induite par l’héparine','TIH':'thrombopénie induite par l’héparine','STEMI':'infarctus du myocarde avec élévation du segment ST','Xa':'facteur dix activé de la coagulation','anti-Xa':'activité contre le facteur dix activé de la coagulation'})
l=Lesson('Syndrome de la veine cave supérieure',10)
anticoag=enoxaparine(l)
l.add('Le syndrome de la veine cave supérieure traduit un {obstacle au retour veineux du haut du corps}. Il associe notamment gonflement facial ou cervical et signes de congestion veineuse. La gravité dépend du retentissement et de la rapidité d’installation.',paras(
    'La veine cave supérieure conduit vers l’oreillette droite le sang provenant de la tête, du cou, des membres supérieurs et de la partie haute du thorax. Une obstruction ou un rétrécissement augmente la pression en amont. Le syndrome est une conséquence anatomique et fonctionnelle ; il ne désigne pas une cause unique.',
    'L’obstacle peut résulter d’une compression ou d’une invasion par une masse, d’un thrombus, ou de mécanismes associés. Un cancer n’est donc pas obligatoire. Inversement, un antécédent de cancer ne prouve pas que toute obstruction est une compression sans thrombose.',
    'Une évolution lente permet le développement de voies collatérales. Elles peuvent limiter les symptômes malgré une obstruction importante. Une aggravation rapide, une détresse respiratoire ou une atteinte neurologique impose une prise en charge immédiate.'
),(57,58,59))
l.add('Les {tumeurs thoraciques et dispositifs intravasculaires} sont des contextes majeurs à rechercher. Les causes bénignes existent. Aucun taux suisse actuel ne permet ici de classer ce diagnostic parmi toutes les tuméfactions du visage.',paras(
    'La CIRSE distingue les causes malignes et non malignes. Les cancers pulmonaires et les lymphomes font partie des causes de masse médiastinale ; des thromboses ou sténoses peuvent être associées aux cathéters centraux et aux sondes intravasculaires.',
    'Rechercher un dispositif actuel mais aussi ancien. L’article de Liège de 2024 montre l’intérêt d’un antécédent de cathéter même retiré depuis longtemps. Il s’agit d’un cas et d’une discussion, pas d’une mesure de fréquence applicable à tous les patients.',
    'Le contexte, la vitesse d’évolution et l’imagerie déterminent le bilan. L’absence de tumeur déjà connue ne rend pas la situation bénigne ; l’absence de cathéter actuel n’exclut pas une obstruction séquellaire.'
),(57,58,59,62))
l.add('L’{hypertension veineuse en amont} explique œdème et dilatation des veines. Les collatérales constituent un contournement parfois essentiel. Une masse peut aussi comprimer les voies aériennes ou d’autres structures thoraciques.',table(['Mécanisme','Signe ou examen','Conséquence pratique'],[
    ['Obstacle au drainage veineux','Œdème du visage, du cou ou des bras ; veines cervicales et thoraciques visibles.','Rechercher et cartographier l’obstacle central.'],
    ['Installation progressive','Réseau veineux collatéral développé ; symptômes parfois moins bruyants.','Ne pas conclure à une obstruction mineure sur la seule tolérance.'],
    ['Compression ou thrombose','Scanner thoracique injecté avec exploration veineuse.','Distinguer désobstruction, anticoagulation et traitement causal.'],
    ['Compression médiastinale associée','Intolérance au décubitus, stridor ou instabilité.','Anticiper le risque positionnel, de sédation et d’anesthésie.']
])+paras('Les collatérales ne sont pas de simples varices à supprimer. Avant un geste thoracique ou abdominal sur ces veines, vérifier leur rôle dans le drainage. La prise en charge de l’œdème seul ne résout pas l’obstacle.',
    'L’œdème laryngé ou les conséquences neurologiques d’une congestion importante peuvent menacer les fonctions vitales. Une masse médiastinale peut aussi comprimer directement trachée, bronches ou structures cardiovasculaires ; tous les symptômes ne proviennent donc pas de la veine seule.'),(57,58,59,63))
l.add('Le tri identifie une {menace respiratoire, neurologique ou circulatoire}. Appeler le 144 en cas de détresse hors hôpital. L’œdème facial isolé et stable reste à explorer rapidement, sans imposer le même geste immédiat à tous.',table(['Signe','Risque','Conduite'],[
    ['Stridor, dyspnée sévère, hypoxémie ou incapacité à rester allongé','Obstruction respiratoire ou compression médiastinale.','Urgence hospitalière avec réanimation et spécialistes ; conserver la position tolérée.'],
    ['Confusion, trouble de conscience ou aggravation neurologique','Retentissement cérébral ou autre cause grave.','Évaluation et stabilisation immédiates, sans attendre un bilan ambulatoire.'],
    ['Syncope, hypotension ou instabilité','Retentissement circulatoire ou complication associée.','Réanimation et recherche urgente des mécanismes.'],
    ['Œdème cervico-facial, bras gonflés et collatérales thoraciques','Obstacle veineux central probable.','Imagerie et avis spécialisé rapides, même si le patient paraît stable.'],
    ['Douleur thoracique ou dyspnée aiguë dans un contexte thrombotique','Embolie ou autre complication possible.','Évaluer l’urgence et adapter le protocole d’imagerie.']
]),(57,58,62,63))
l.add('L’anamnèse précise la {chronologie, la tolérance et les facteurs de cause}. L’incapacité à s’allonger doit être transmise avant le scanner ou un prélèvement. Ne pas oublier un cathéter retiré.',steps(
    'Dater début, progression et caractère positionnel du gonflement ; demander dyspnée, toux, modification de voix, céphalées et malaise.',
    'Rechercher intolérance au décubitus, stridor, syncope ou modification de vigilance pour organiser immédiatement le lieu de soins.',
    'Recenser cathéters, chambres implantables et sondes intravasculaires actuels ou anciens, avec leur côté et leur histoire si connus.',
    'Demander cancer connu, symptômes thoraciques, amaigrissement, sueurs nocturnes et autres masses ; ces signes orientent sans établir l’histologie.',
    'Relever antécédents thrombotiques, traitements anticoagulants, saignements, thrombopénie liée à l’héparine, fonction rénale et gestes récents.',
    'Préciser grossesse éventuelle et limitations fonctionnelles ; transmettre les images ou comptes rendus déjà disponibles.'
),(57,58,59,61,62))
l.add('L’examen cherche la {congestion du haut du corps et son retentissement}. Comparer les deux bras et examiner le thorax. Une saturation normale n’écarte pas un obstacle important.',paras(
    'Observer d’abord respiration, fréquence respiratoire, saturation en oxygène, pression artérielle, pouls et vigilance dans la position tolérée. Rechercher bruit inspiratoire, difficulté à parler et signes de lutte. Ne pas allonger de force un patient qui respire mieux assis.',
    'Inspecter visage, cou, bras et partie haute du thorax : œdème, coloration anormale et veines dilatées. Comparer les membres supérieurs et noter l’existence d’une circulation collatérale. Le repère normal attendu est l’absence d’œdème inhabituel et de réseau veineux collatéral pathologique.',
    'Rechercher une masse ou des ganglions accessibles, ainsi qu’un dispositif veineux et des signes d’infection associés. Ausculter le thorax et évaluer les autres signes cardiorespiratoires selon la situation. Aucun signe isolé de palpation ne localise complètement l’obstacle.',
    'Un réseau abdominal peut correspondre à un drainage collatéral venu du thorax. Il doit être interprété avec l’imagerie avant un geste. Une présentation asymétrique n’exclut pas une obstruction centrale ou associée aux veines afférentes.'
),(57,58,59,63))
l.add('L’approche distingue {obstacle tumoral, thrombose et diagnostics concurrents}. Plusieurs mécanismes peuvent coexister. Le gonflement facial ne doit pas être automatiquement assimilé à un angio-œdème.',table(['Profil','Orientation','Vérification'],[
    ['7.1 — Congestion veineuse centrale','Œdème du haut du corps avec veines dilatées, parfois positionnel.','Scanner thoracique veineux et recherche de cause.'],
    ['7.2 — Thrombose liée à un dispositif','Dispositif actuel ou ancien, gonflement d’un bras ou du cou.','Examiner les veines accessibles et surtout l’extension centrale.'],
    ['7.3 — Masse médiastinale','Symptômes thoraciques ou ganglions, compression possible.','Imagerie et prélèvement planifiés après évaluation de sécurité.'],
    ['7.4 — Autre tuméfaction','Angio-œdème, infection locale, masse thyroïdienne ou autre cause systémique.','Rechercher les signes propres ; ne pas omettre l’urgence respiratoire commune à plusieurs causes.']
]),(57,58,59,62,63))
l.add('Le diagnostic positif relie {syndrome clinique et obstacle veineux objectivé}. Le scanner précise siège, extension et mécanisme probable. L’imagerie d’une masse ne fournit pas à elle seule son type tumoral.',paras(
    'Le tableau clinique évocateur doit conduire à une imagerie adaptée. Le scanner thoracique injecté avec phase veineuse visualise la veine cave supérieure, les voies afférentes, les collatérales et une éventuelle masse. Informer le radiologue de l’hypothèse pour choisir le protocole.',
    'Décrire compression extrinsèque, invasion suspectée, thrombus et obstacles associés. Les mécanismes mixtes sont possibles. L’importance de l’obstruction anatomique doit être confrontée à la tolérance, à la rapidité d’installation et aux complications.',
    'Si un cancer est suspecté sans preuve, choisir un prélèvement adapté avec l’équipe. Un ganglion accessible peut permettre une voie plus sûre qu’un geste médiastinal. La recherche de tissu ne doit pas retarder une stabilisation vitale, mais le patient stable bénéficie d’une preuve avant traitement antitumoral.'
),(57,58,59,62,63))
l.add('Les {examens complémentaires} cartographient l’obstacle et préparent un soin sûr. Le protocole dépend de la question clinique et de la tolérance. L’échographie du cou seule n’exclut pas une obstruction intrathoracique.',
    '<h3>9.a — Examen de référence</h3>'+paras('Le scanner thoracique injecté avec temps veineux est l’examen de référence pratique de la cartographie initiale dans le guide GGC. Il recherche obstruction, thrombus, collatérales et cause thoracique. Une suspicion d’embolie pulmonaire exige une question et un protocole adaptés, pas l’affirmation qu’un temps veineux quelconque l’exclut.')+
    '<h3>9.b — Première intention</h3>'+paras('Évaluer immédiatement les fonctions vitales et les conditions de transport. Vérifier fonction rénale, hémogramme et plaquettes, ainsi que les éléments d’hémostase utiles à un traitement ou une procédure. Ces résultats ne prouvent ni n’excluent seuls le syndrome. L’urgence vitale et le risque du contraste sont discutés avec l’équipe, sans retard automatique.')+
    table(['Constat','Interprétation','Conduite'],[
        ['Compression sans thrombus démontré','L’obstacle peut être mécanique.','Discuter désobstruction et traitement causal ; pas d’anticoagulation curative automatique.'],
        ['Thrombus central','Composante thrombotique documentée.','Évaluer anticoagulation et éventuelle intervention selon risque.'],
        ['Masse et compression aérienne','Risque thoracique dépassant l’obstruction veineuse.','Avis spécialisé urgent et plan de prélèvement/anesthésie.'],
        ['Créatinine ou plaquettes anormales','Imagerie, geste ou traitement peuvent nécessiter adaptation.','Vérifier les risques et le choix thérapeutique.']
    ])+
    '<h3>9.c — Alternatives ciblées</h3>'+paras('L’imagerie par résonance magnétique peut caractériser les veines et les tissus dans des situations choisies. L’échographie Doppler est utile pour certaines veines cervicales ou des bras, mais sa fenêtre ne couvre pas toute la veine cave supérieure. Une radiographie thoracique peut montrer une masse sans suffire à cartographier l’obstacle.')+
    '<h3>9.d — Seconde intention et cause</h3>'+paras('La phlébographie sert notamment à préparer ou réaliser une recanalisation endovasculaire. Le bilan tumoral et le prélèvement sont adaptés à la lésion et à l’état du patient. Bronchoscopie, biopsie guidée ou prélèvement ganglionnaire ne sont pas interchangeables ; une suspicion de lymphome nécessite un matériel permettant son typage.'),(57,58,59,61,62,63))
l.add('L’{arbre décisionnel} associe stabilisation et identification du mécanisme. L’urgence du drainage ne se déduit pas du mot cancer seul. La stratégie est coordonnée avec les équipes thoraciques, oncologiques et interventionnelles.',steps(
    'Si détresse respiratoire, atteinte neurologique ou instabilité, alors transférer et stabiliser immédiatement dans un environnement capable de traiter la compression.',
    'Si le décubitus aggrave les symptômes, alors conserver la position tolérée et anticiper les risques de transport, imagerie, sédation et anesthésie.',
    'Si la situation le permet, alors réaliser rapidement la cartographie thoracique injectée avec question veineuse précise.',
    'Si une désobstruction urgente est nécessaire et réalisable, alors discuter une recanalisation et un stent avec l’équipe interventionnelle.',
    'Si un thrombus est documenté, alors choisir l’anticoagulation ou un geste après évaluation des contre-indications et du programme de prélèvement.',
    'Si une cause tumorale est suspectée et que le patient est stable, alors obtenir le diagnostic tissulaire avant le traitement spécifique ; en menace vitale, la stabilisation et la décision spécialisée priment.'
),(57,58,60,62,63))
l.add('La {prise en charge en Suisse} dépend du retentissement et de la cause. Le stent peut soulager rapidement une obstruction sélectionnée. Anticoagulants, corticoïdes et traitements anticancéreux ont chacun des indications distinctes.',
    '<h3>11.A — But</h3>'+paras('Préserver respiration, fonctions neurologiques et circulation, réduire la congestion puis traiter l’obstacle et sa cause. Le soulagement veineux n’équivaut pas à la guérison d’une tumeur. La décision tient compte de l’état général, des objectifs du patient et des possibilités techniques.')+
    '<h3>11.B — Moyens</h3>'+paras('Installer le patient avec le haut du corps relevé si cette position est mieux tolérée, surveiller et donner de l’oxygène en cas d’hypoxémie selon le contexte. Appeler rapidement les spécialistes. Une masse médiastinale compressive impose un plan spécifique pour toute sédation ou anesthésie ; même une sédation peut aggraver la compression, notamment chez l’enfant.',
    'Une recanalisation avec endoprothèse veineuse, parfois associée à une dilatation, peut rétablir le drainage. La CIRSE décrit souvent un soulagement en vingt-quatre à quarante-huit heures après stent ; ce délai n’est ni garanti ni une autorisation d’attendre devant une détresse. La faisabilité, les risques et la nécessité d’une thrombectomie sont appréciés individuellement.',
    'Une thrombose documentée conduit à discuter un traitement anticoagulant si son bénéfice dépasse le risque hémorragique. Un exemple suisse de traitement adulte par énoxaparine est détaillé dans la sous-fenêtre. Il ne vaut pas obligation de cette molécule pour tous les patients ou toutes les procédures. Une compression sans thrombus n’impose pas d’anticoagulation curative.',
    'Le devenir d’un cathéter ou d’une sonde est décidé selon utilité, fonctionnement, infection éventuelle, thrombus et projet de traitement. Ne pas retirer automatiquement tout dispositif ni supposer que son retrait résout une sténose ancienne. Les gestes sont coordonnés avec l’équipe qui traite l’obstacle.')+anticoag+paras(
    'Une cause tumorale exige un traitement adapté à l’histologie et à l’extension : traitement systémique, radiothérapie ou autre stratégie discutée en concertation. Le patient stable doit autant que possible avoir une preuve tissulaire avant traitement. Une menace vitale peut nécessiter un traitement urgent décidé avec oncologie, hématologie et réanimation.',
    'Les corticoïdes ne constituent pas une désobstruction universelle. Ils peuvent être discutés dans certaines compressions tumorales, mais peuvent aussi altérer le rendement d’une biopsie de lymphome et provoquer une lyse tumorale. Les schémas britanniques ne sont pas transposés en prescription suisse ; indication, molécule et dose nécessitent une décision spécialisée et une notice applicable.',
    'Grossesse et allaitement nécessitent une coordination spécialisée des examens et traitements. En pédiatrie, une masse médiastinale impose une équipe expérimentée et un plan de sécurité ; ne pas extrapoler les doses adultes ni programmer une anesthésie banale. Les traitements antitumoraux ne sont pas détaillés ici comme un protocole exhaustif.')+
    '<h3>11.C — Surveillance</h3>'+paras('Réévaluer respiration, voix, vigilance, pression, œdème et tolérance positionnelle. Après recanalisation, surveiller le point d’accès, le saignement, la thrombose et les signes de migration ou de réobstruction. Une aggravation respiratoire, un malaise ou une douleur thoracique après le geste exige une évaluation immédiate.',
    'Le traitement antithrombotique après stent dépend du thrombus, du dispositif, du risque hémorragique et du protocole de l’équipe. La durée courte mentionnée dans une page générale de procédure ne fixe pas la durée de toute thrombose cave ni de tout stent. Sous anticoagulation, suivre notamment saignement, plaquettes et reins selon la molécule.')+
    '<h3>11.D — Pronostic et suivi</h3>'+paras('Le pronostic dépend de la cause et du retentissement, pas seulement de l’aspect du visage. Un stent peut améliorer les symptômes sans traiter le cancer. Organiser le suivi clinique, l’évaluation de la perméabilité si indiquée, le diagnostic causal et la durée des traitements. Une récidive de gonflement ou de dyspnée doit être signalée rapidement.'),(57,58,59,60,61,62,63))
l.add('La {prévention vise les risques et la détection précoce}. Un dispositif veineux mérite une indication et un suivi adaptés. Une anticoagulation préventive systématique pour tous les dispositifs ne se déduit pas de ce diagnostic.',paras(
    'Évaluer régulièrement l’utilité des dispositifs et appliquer leur protocole de soin. Une complication infectieuse ou thrombotique nécessite une décision clinique ; le patient ne manipule ni ne retire lui-même son dispositif. Les mesures médicamenteuses préventives relèvent de leurs indications propres.',
    'Informer le patient porteur d’un dispositif ou traité pour une masse thoracique de signaler gonflement inhabituel de la face, du cou ou d’un bras, dyspnée et apparition de veines collatérales. Un antécédent ancien reste utile à transmettre.',
    'Après intervention, remettre des consignes de suivi et d’alerte ainsi qu’un interlocuteur. Avant toute nouvelle opération sur un réseau veineux collatéral, transmettre les antécédents et l’imagerie. La prévention des retards passe aussi par un responsable clairement identifié du résultat de biopsie.'
),(57,59,60))
l.add('Les {points clés} sont congestion, cartographie et traitement causal. L’urgence vitale précède le programme diagnostique. Le patient stable bénéficie d’un parcours qui préserve la preuve tissulaire.',steps(
    'Associer un œdème cervico-facial avec veines thoraciques visibles à l’hypothèse d’obstacle central.',
    'Rechercher la menace respiratoire, neurologique ou circulatoire et l’intolérance au décubitus.',
    'Demander une imagerie thoracique adaptée à l’exploration veineuse.',
    'Distinguer compression, thrombose et mécanismes associés.',
    'Discuter stent, anticoagulation et traitement tumoral selon leurs indications respectives.',
    'Préserver le diagnostic tissulaire quand possible et organiser la surveillance des complications et des résultats.'
),(57,58,60,62,63))
l.quiz([
    ('Quel territoire est drainé par la veine cave supérieure ?','La tête, le cou, les membres supérieurs et la partie haute du thorax vers l’oreillette droite.'),
    ('Le syndrome implique-t-il obligatoirement un cancer ?','Non. Une thrombose ou une sténose liée à un dispositif, notamment, peut en être la cause.'),
    ('Pourquoi une obstruction importante peut-elle rester relativement bien tolérée ?','Une installation progressive peut permettre un drainage par des veines collatérales.'),
    ('Quels signes imposent une stabilisation urgente ?','Détresse respiratoire, stridor, hypoxémie, atteinte neurologique ou instabilité circulatoire.'),
    ('Faut-il allonger de force un patient qui devient très dyspnéique en décubitus ?','Non. Conserver la position tolérée et alerter les équipes avant transport, scanner ou anesthésie.'),
    ('Un cathéter retiré depuis longtemps est-il sans intérêt dans l’anamnèse ?','Non. Une obstruction séquellaire peut se manifester tardivement.'),
    ('Quel examen cartographie habituellement l’obstacle et sa cause thoracique ?','Un scanner thoracique injecté avec protocole et temps veineux adaptés.'),
    ('Une échographie cervicale négative exclut-elle une obstruction cave ?','Non. Elle ne visualise pas l’ensemble des veines intrathoraciques.'),
    ('Une masse au scanner établit-elle le type de cancer ?','Non. Le traitement spécifique nécessite autant que possible une preuve tissulaire adaptée.'),
    ('Une compression sans thrombus impose-t-elle une anticoagulation curative ?','Non. L’indication dépend du mécanisme, du bénéfice et du risque hémorragique.'),
    ('Quel schéma adulte Clexane est cité pour une thrombose retenue chez un patient cancéreux avec reins compatibles ?','La notice privilégie 1 mg/kg sous-cutané par injection, deux fois par jour ; le choix doit être validé et adapté au terrain et aux gestes prévus.'),
    ('Que devient ce schéma de traitement dans le tableau de la notice pour une clairance inférieure à 30 ml/min ?','Le tableau indique 1 mg/kg sous-cutané une fois par jour ; la situation rénale sévère et le choix de molécule exigent une validation spécialisée.'),
    ('Pourquoi ne pas donner automatiquement un corticoïde avant une biopsie de lymphome ?','Il peut modifier le tissu et réduire le rendement diagnostique ; une menace vitale éventuelle est décidée avec les spécialistes.'),
    ('Un stent traite-t-il nécessairement la cause tumorale ?','Non. Il peut améliorer le drainage et les symptômes ; le traitement de la cause et le suivi restent nécessaires.')
],(57,58,59,60,61,62,63))
l.write()
