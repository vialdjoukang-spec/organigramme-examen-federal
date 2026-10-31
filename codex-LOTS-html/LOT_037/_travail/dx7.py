from format_lecon import Lesson, paras, table, steps, ABBR
from antibiotiques_oraux import coamoxi_oral, coamoxi_enfant
from antibiotiques_parenteraux import coamoxi, clindamycine
from medicaments import paracetamol

ABBR.update({'AMX':'amoxicilline','CLV':'acide clavulanique','BSAC':'Société britannique de chimiothérapie antimicrobienne'})
l=Lesson('Adénite cervicale infectieuse',7)
l.add('L’adénite cervicale infectieuse est une {inflammation ganglionnaire liée à une infection}. Elle se distingue d’un simple ganglion palpable et d’une masse non ganglionnaire. Une origine virale, bactérienne commune ou plus spécifique change la conduite.',paras(
    'Le terme adénopathie décrit une anomalie d’un ganglion, quelle qu’en soit la cause. Le terme adénite met l’accent sur l’inflammation. Le portail genevois Mon enfant est malade explique cette distinction et la possibilité de suppuration dans une infection bactérienne.',
    'Les ganglions reçoivent la lymphe des territoires voisins et participent à la réponse immunitaire. Une infection du pharynx, des dents, de la face ou du cuir chevelu peut donc entraîner une tuméfaction cervicale. La localisation du ganglion aide à rechercher le foyer initial.',
    'Une adénite suppurée contient une collection de pus. Elle n’équivaut pas à une simple réaction ganglionnaire après un rhume. Inversement, une masse salivaire, un kyste ou une tumeur ne doit pas être appelé adénite sans vérifier sa nature.'
),(40,42,34))
l.add('Le {contexte épidémiologique et les expositions} orientent le diagnostic. Les petites réactions ganglionnaires sont fréquentes chez l’enfant. Elles ne prouvent pas à elles seules une infection bactérienne à traiter.',paras(
    'Les enfants ont souvent plusieurs petits ganglions palpables au cou lors des infections courantes. Une atteinte aiguë, unilatérale, chaude et douloureuse fait davantage rechercher une adénite à pyogènes, sans constituer une preuve absolue.',
    'L’âge, une porte d’entrée cutanée ou dentaire, un contact avec un chat, un contexte tuberculeux et l’immunité du patient modifient les hypothèses. Une adénopathie chronique peu douloureuse ne suit pas nécessairement le même mécanisme qu’une adénite bactérienne aiguë.',
    'Aucune incidence nationale suisse actuelle, ni comparaison quantitative européenne homogène entre les dix causes de gonflement, n’a été établie dans les documents consultés. La fréquence des ganglions palpables ne se confond pas avec celle des adénites suppurées.'
),(40,41,42))
l.add('Le {drainage lymphatique et la réaction immunitaire} expliquent le gonflement. L’inflammation peut provoquer douleur et rougeur. Une collection ou une autre cause persistante demande une réponse spécifique.',paras(
    'La réponse au foyer drainé active les cellules immunitaires du ganglion et augmente son volume. Cette réaction peut accompagner une infection virale et régresser avec elle. Un antibiotique ne corrige pas ce mécanisme lorsqu’aucune infection bactérienne sensible n’est en cause.',
    'Lors d’une infection bactérienne, l’afflux inflammatoire peut s’accompagner de destruction tissulaire et de pus. La collection devient parfois fluctuante, mais l’absence de fluctuation ne l’exclut pas. L’échographie peut aider à l’identifier.',
    'Une infection inhabituelle, une anomalie congénitale infectée ou une tumeur peut expliquer un ganglion qui persiste ou revient. Répéter le même antibiotique ne corrige pas toutes ces causes.'
)+table(['Mécanisme','Exploration utile','Réponse'],[
    ['Activation immunitaire après infection virale','Contexte clinique et suivi de la régression.','Soins symptomatiques et surveillance lorsque le tableau est rassurant.'],
    ['Infection bactérienne d’un territoire drainé','Examen de la porte d’entrée et prélèvement si indiqué.','Traitement du foyer et antibiotique adapté.'],
    ['Suppuration ganglionnaire','Examen puis échographie selon le tableau.','Ponction ou drainage spécialisé lorsque nécessaire, avec bactériologie.'],
    ['Processus persistant atypique','Bilan ciblé et prélèvement tissulaire décidé en milieu spécialisé.','Traitement étiologique après identification.']
]),(40,41,42))
l.add('La démarche exclut d’abord une {compression, une infection profonde ou un sepsis}. Une adénite douloureuse reste une hypothèse, pas une garantie de bénignité. Les signes généraux et la durée comptent autant que la palpation.',table(['Signe ou contexte','Ce qu’il faut rechercher','Décision'],[
    ['Dyspnée, stridor, salive mal déglutie, voix étouffée','Compression ou infection profonde.','Évaluation urgente ; appel au 144 hors hôpital si menace respiratoire.'],
    ['Torticolis fébrile ou trismus récent','Extension rétro- ou parapharyngée.','Avis spécialisé et imagerie adaptée à la suspicion.'],
    ['Mauvais état général, hypotension ou dégradation rapide','Sepsis ou foyer mal contrôlé.','Prise en charge hospitalière immédiate.'],
    ['Masse dure, fixée, sus-claviculaire, ou signes généraux durables','Cause tumorale ou autre maladie systémique.','Bilan spécialisé sans répétition empirique indéfinie d’antibiotiques.'],
    ['Fièvre persistante chez l’enfant avec signes inhabituels ou cutanéomuqueux','Infection spécifique ou maladie inflammatoire, notamment Kawasaki.','Réévaluation pédiatrique plutôt qu’une simple prolongation d’antibiotique.']
]),(3,34,41,42))
l.add('L’anamnèse précise la {porte d’entrée et l’évolution}. Elle recherche symptômes associés, contacts et traitements. Chaque réponse doit modifier une hypothèse ou le degré d’urgence.',steps(
    'Dater le début, la douleur et la croissance afin de distinguer une réaction récente d’une évolution persistante.',
    'Demander douleur pharyngée ou dentaire et lésions de la peau ou du cuir chevelu, car ces territoires peuvent drainer vers les ganglions cervicaux.',
    'Rechercher gêne respiratoire, dysphagie, salive mal déglutie et torticolis, car ils imposent de chercher une extension profonde.',
    'Demander contact avec des animaux, griffure, voyage et exposition tuberculeuse afin de choisir des tests ciblés.',
    'Relever fièvre prolongée, sueurs nocturnes, amaigrissement, fatigue, douleurs osseuses ou saignement inhabituel pour élargir l’enquête.',
    'Noter antibiotiques, observance, évolution sous traitement, allergies, poids, fonction rénale et immunodépression avant de modifier une prescription.'
),(40,41,42,44,45))
l.add('L’examen décrit le {ganglion et son territoire de drainage}. Il compare les deux côtés et recherche d’autres aires atteintes. Une observation datée facilite l’évaluation de la réponse.',paras(
    'Un enfant peut avoir de petits ganglions mobiles sans rougeur ni altération générale. Inspecter puis palper doucement le cou, sans massage agressif. Décrire siège, dimensions, douleur, consistance, mobilité, chaleur et aspect cutané.',
    'Une tuméfaction chaude, sensible et rouge soutient une inflammation. Une fluctuation évoque du liquide ; une peau violacée, une fistule ou une évolution indolente demande un diagnostic plus spécifique. Aucun de ces signes ne prouve seul le germe.',
    'Inspecter pharynx, dents, oreilles, face et cuir chevelu selon les symptômes. Rechercher d’autres ganglions et, si le tableau le justifie, une augmentation du foie ou de la rate. Vérifier l’état général, la respiration, la déglutition et l’hydratation avant de prolonger l’examen.',
    'Reporter les constatations sur un schéma ou dans le dossier avec date et côté. L’impression du patient que la masse a changé peut alors être confrontée à des mesures comparables.'
),(40,41,42))
l.add('L’approche syndromique distingue {forme aiguë localisée, atteinte disséminée et évolution chronique}. Ces profils orientent les tests et le traitement. L’étiquette infectieuse reste révisable.',table(['Profil','Signes utiles et sens','Conduite'],[
    ['7.1 — Adénite aiguë à pyogènes possible','Une masse récente, douloureuse et chaude peut suivre un foyer ORL, dentaire ou cutané.','Chercher la porte d’entrée et la suppuration ; traiter selon gravité.'],
    ['7.2 — Réaction virale ou infection systémique possible','Plusieurs ganglions et des symptômes généraux ou pharyngés peuvent accompagner une infection virale.','Vérifier les signes de gravité ; réserver les tests à une question clinique.'],
    ['7.3 — Infection spécifique ou masse atypique','Une évolution indolente, une fistule ou des expositions particulières modifie les hypothèses.','Avis spécialisé et tests ciblés ; ne pas inciser une lésion atypique sans diagnostic.'],
    ['7.4 — Cause non infectieuse possible','Une masse dure, fixée ou persistante et des signes généraux durables peuvent orienter vers une autre cause.','Bilan tissulaire et systémique selon les spécialistes.']
]),(34,40,41,42))
l.add('Le {diagnostic positif} est d’abord clinique dans une forme simple. L’étiologie bactérienne n’est pas établie par la seule taille. Une évolution atypique ou défavorable impose de vérifier le diagnostic.',paras(
    'Un tableau aigu inflammatoire dans un territoire drainant une porte d’entrée infectieuse soutient l’adénite. Le diagnostic de suppuration demande une évaluation adaptée, parfois une échographie et un prélèvement du pus.',
    'Il n’existe pas ici de score unique permettant de décider automatiquement du germe ou de l’antibiotique. Le référentiel pédiatrique et la recommandation SFORL2024 distinguent les profils cliniques et leur gravité. Un frottis pharyngé positif peut documenter une infection pharyngée associée sans prouver que toute masse est causée par ce germe.',
    'La recommandation suisse sur l’angine simple vise à restreindre des prescriptions inutiles. Elle ne signifie pas qu’une adénite suppurée ou une infection profonde doive rester sans traitement. Il faut nommer la complication et traiter la situation réellement présente.',
    'Une réponse partielle à l’antibiotique ne suffit pas à exclure une tumeur ou une infection atypique. La disparition des signes inflammatoires et l’évolution de la masse sont évaluées séparément.'
),(34,35,42,43))
l.add('Les {examens complémentaires} dépendent de la gravité et de l’incertitude. Une adénite simple n’exige pas un bilan exhaustif systématique. L’échographie et les prélèvements répondent à des questions différentes.',
    '<h3>9.a — Référence étiologique</h3>'+paras('Le prélèvement d’une collection pour culture et antibiogramme peut établir l’agent d’une adénite suppurée. Il ne faut pas ponctionner systématiquement toute forme simple. Une suspicion tumorale ou de mycobactérie peut nécessiter un prélèvement tissulaire organisé avec les analyses appropriées.')+
    '<h3>9.b — Première intention</h3>'+paras('La forme simple repose surtout sur l’examen clinique. Une échographie est utile si la nature ganglionnaire est incertaine, si une collection est suspectée ou si l’évolution est défavorable. Hémogramme, marqueurs inflammatoires et hémocultures sont adaptés au retentissement et à la gravité.')+
    table(['Résultat','Signification','Suite'],[
        ['Ganglion sans collection et évolution favorable','Une suppuration drainable n’est pas mise en évidence.','Poursuivre le plan clinique et la surveillance adaptés.'],
        ['Collection accessible','Une suppuration est possible.','Avis pour ponction ou drainage avec bactériologie.'],
        ['Atteinte profonde suspectée','Le problème dépasse une adénite superficielle.','Avis urgent et scanner adapté après sécurité respiratoire.'],
        ['Cytopénies ou cellules sanguines anormales','Une hémopathie ou un autre processus systémique est possible.','Bilan spécialisé sans attribuer automatiquement le résultat à une infection banale.']
    ])+
    '<h3>9.c — Examens ciblés alternatifs</h3>'+paras('Choisir les sérologies ou tests de tuberculose selon les contacts, symptômes et risques. Une recherche de Bartonella est discutée après exposition compatible ; un ensemble de sérologies non orientées peut produire des résultats difficiles à interpréter.')+
    '<h3>9.d — Seconde intention</h3>'+paras('Devant échec, persistance ou signes suspects, discuter une cytoponction ou une biopsie dans le parcours spécialisé. La suspicion de lymphome demande un prélèvement qui préserve les informations histologiques nécessaires. Une imagerie thoracique ou d’autres territoires répond à la recherche d’une atteinte profonde.'),(34,35,41,42))
l.add('L’{arbre décisionnel} sépare l’urgence de la forme simple. Le traitement est ensuite réévalué sur une évolution observée. Une absence de réponse déclenche une enquête, pas seulement une nouvelle ordonnance.',steps(
    'Si des signes respiratoires, de sepsis ou d’extension profonde sont présents, alors adresser immédiatement au niveau hospitalier adapté.',
    'Si le tableau est viral et rassurant, alors proposer soins symptomatiques et suivi, avec consignes précises de retour.',
    'Si une adénite bactérienne simple est probable et la prise orale fiable, alors traiter le foyer et choisir une antibiothérapie adaptée au patient.',
    'Si une collection est possible, alors demander une échographie et un avis pour prélèvement ou drainage selon gravité et évolution.',
    'Si aucune amélioration n’apparaît après un traitement correctement pris ou si l’état se dégrade, alors vérifier le diagnostic, la dose, l’observance, la sensibilité et le contrôle du foyer.',
    'Si la masse persiste ou présente des caractères suspects, alors organiser le bilan spécialisé sans répéter indéfiniment les traitements empiriques.'
),(34,35,40,41,42))

o=coamoxi_oral(l);e=coamoxi_enfant(l);v=coamoxi(l);k=clindamycine(l);p=paracetamol(l,contexte='au soulagement et à la réévaluation')
l.add('La {prise en charge en Suisse} traite la cause et soulage le patient. Une forme bactérienne simple peut relever de la voie orale, tandis qu’une forme grave ou une prise orale impossible impose une autre organisation. La réponse et les signes d’alarme sont vérifiés rapidement.',
    '<h3>11.A — But</h3>'+paras('Traiter une infection bactérienne lorsqu’elle est probable ou documentée, prévenir l’extension et contrôler une éventuelle collection. Le soulagement doit s’accompagner d’une évolution générale et locale favorable. Une réaction virale ne nécessite pas un antibiotique.')+
    '<h3>11.B — Moyens</h3>'+paras('Commencer par les fonctions vitales et l’orientation en cas de gravité. Dans la forme stable, assurer une hydratation tolérée et une antalgie adaptée : '+p+'. La porte d’entrée dentaire, cutanée ou pharyngée doit être traitée.',
    'L’amoxicilline–acide clavulanique est une option probabiliste décrite pour l’adénite à pyogènes. Les doses générales de la spécialité suisse sont détaillées séparément pour '+o+' et pour '+e+'. Les rapports, concentrations, poids et reins doivent être vérifiés avant toute prescription.',
    'Une impossibilité de prendre le traitement oral, une dégradation ou une infection compliquée nécessite une évaluation hospitalière. La fenêtre '+v+' décrit les doses suisses de la spécialité parentérale ; elles ne s’obtiennent pas en convertissant directement les millilitres de suspension.',
    'En allergie, identifier le type de réaction et les produits en cause. La fenêtre '+k+' décrit une option parentérale lorsque sa place et la sensibilité sont établies. Elle ne vaut pas une alternative pédiatrique orale universelle ni une ordonnance pour toute infection résistante. Une allergie grave ou une situation complexe nécessite le schéma complet du spécialiste.',
    'Une collection peut être évacuée par ponction ou drainage selon le contexte ; le pus est prélevé pour analyse. Une masse chronique atypique ne doit pas être incisée comme un abcès banal. Une mycobactériose, une bartonellose ou une tuberculose relève de son propre traitement.',
    'Chez le jeune nourrisson, la personne immunodéprimée ou le patient avec défaillance d’organe, abaisser le seuil d’avis spécialisé. Grossesse, allaitement et insuffisances suivent les restrictions des notices de la spécialité choisie. Une corticothérapie empirique d’une adénopathie non élucidée peut masquer un lymphome et doit être évitée.')+
    '<h3>11.C — Surveillance</h3>'+paras('Réévaluer la forme ambulatoire dans les 48 à 72 heures selon le tableau, plus tôt devant toute aggravation. Contrôler fièvre, douleur, volume, peau, déglutition, hydratation et observance. Une fièvre qui persiste après deux jours de traitement ou une masse qui continue de grossir justifie un nouvel avis.',
    'Vérifier dose et concentration réellement reçues, résultat microbiologique et besoin d’un geste. La disparition de la douleur ne signifie pas nécessairement la disparition du ganglion. La durée dépend de la cause, du drainage, du guide local et de l’évolution ; les différences entre recommandations sont détaillées dans les fenêtres de prescription.')+
    '<h3>11.D — Pronostic et sortie</h3>'+paras('La plupart des formes simples évoluent favorablement, mais un ganglion résiduel peut rester palpable. Une sortie ou un maintien à domicile exige un état général satisfaisant, une prise orale fiable, l’absence de signe de gravité et un suivi réalisable. Une masse qui ne régresse pas, une récidive au même endroit ou de nouveaux signes généraux demande une nouvelle enquête.'),(34,35,40,41,42,44,45,38,39,27))
l.add('La {prévention} repose sur les soins du foyer et un suivi compréhensible. Les mesures doivent correspondre à l’agent en cause. Il n’existe pas un traitement préventif unique de toute adénite.',paras(
    'Traiter les lésions dentaires et cutanées identifiées, préserver l’hygiène buccale et éviter de manipuler une masse inflammatoire. La prévention d’une infection spécifique dépend de ses voies de transmission et des recommandations correspondantes.',
    'Expliquer comment prendre le médicament prescrit et mesurer une suspension. Fournir les signes de retour urgent et un rendez-vous de contrôle. Une ordonnance sans possibilité de réévaluation est insuffisante pour une masse évolutive.',
    'En cas de récidive au même siège, rechercher avec le spécialiste une anomalie congénitale ou un foyer persistant. L’imagerie à distance de l’épisode peut être utile. Une suspicion de tuberculose ou d’une autre infection particulière nécessite aussi les mesures de santé publique appropriées.'
),(34,40,42,44,45))
l.add('Les {points clés} relient le ganglion à son contexte. L’antibiotique est réservé à une indication bactérienne. La surveillance vérifie autant l’évolution de la masse que celle de la fièvre.',steps(
    'Distinguer adénite inflammatoire, réaction ganglionnaire et masse non ganglionnaire.',
    'Examiner les territoires de drainage et rechercher les signes de gravité.',
    'Adapter les tests à la suspicion de collection, d’agent spécifique ou de cause non infectieuse.',
    'Choisir la présentation et la dose d’antibiotique sans confondre adulte, suspension et voie parentérale.',
    'Réévaluer rapidement une réponse insuffisante et contrôler une collection si nécessaire.',
    'Organiser l’exploration d’une masse persistante ou suspecte.'
),(34,35,40,41,42,44,45))
l.quiz([
    ('Un ganglion palpable chez l’enfant impose-t-il un antibiotique ?','Non. De petits ganglions réactionnels sont fréquents ; l’indication dépend de l’origine probable et du retentissement.'),
    ('Quelle différence y a-t-il entre adénopathie et adénite ?','L’adénopathie décrit une anomalie ganglionnaire ; l’adénite décrit une inflammation. Les causes ne sont pas toutes bactériennes.'),
    ('Que faut-il examiner près d’une adénite cervicale ?','Les territoires drainés : pharynx, dents, oreilles, face et cuir chevelu selon les symptômes.'),
    ('Un torticolis fébrile est-il toujours une simple contracture ?','Non. Il peut révéler une infection profonde et nécessite une évaluation adaptée.'),
    ('La taille seule permet-elle de distinguer bactérie, virus et cancer ?','Non. Le siège, l’évolution, les signes inflammatoires et l’état général sont indispensables.'),
    ('Quand l’échographie est-elle utile ?','En cas de doute sur la nature de la masse, de suspicion de collection ou d’évolution défavorable. Une extension profonde peut demander une autre imagerie.'),
    ('Pourquoi analyser le pus prélevé ?','Pour documenter le germe et sa sensibilité, puis adapter le traitement.'),
    ('Les suspensions à 156,25 et 457 mg se prennent-elles au même rythme ?','Non. Elles ont des concentrations, rapports et indications différents. La notice décrit trois prises pour les formes 156,25/312,5 et deux pour la forme 457.'),
    ('Une dose en mg/kg/jour est-elle une dose par prise ?','Non. C’est une dose quotidienne à répartir selon la notice ; il faut vérifier si elle désigne l’association ou une seule composante.'),
    ('Un traitement de dix jours est-il sans réserve avec la suspension chez le moins de trois ans ?','Non. Sa notice contient une restriction au-delà d’une semaine liée à l’alcool benzylique, sauf avis médical ou pharmaceutique ; la durée doit être explicitement vérifiée.'),
    ('Que faire si la fièvre persiste ou si le ganglion grossit malgré le traitement ?','Réévaluer sans prolonger automatiquement : diagnostic, dose, observance, résistance, collection et extension doivent être vérifiés.'),
    ('Faut-il inciser une masse chronique peu inflammatoire sans autre bilan ?','Non. Une infection atypique ou une autre lésion peut nécessiter un prélèvement et une stratégie spécialisés.'),
    ('Pourquoi éviter les corticoïdes empiriques devant une adénopathie inexpliquée ?','Ils peuvent masquer ou modifier un lymphome et compromettre le diagnostic.'),
    ('Une amélioration partielle élimine-t-elle une cause tumorale ?','Non. La masse résiduelle, sa trajectoire et les signes associés restent à contrôler.')
],(34,35,40,41,42,43,44,45))
l.write()
