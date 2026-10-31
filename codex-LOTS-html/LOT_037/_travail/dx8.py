from format_lecon import Lesson, paras, table, steps, ABBR
from radioiode import radioiode

ABBR.update({'ETA':'Association européenne de la thyroïde','SFE':'Société française d’endocrinologie','EU-TIRADS':'système européen de classification échographique du risque des nodules thyroïdiens','T3':'triiodothyronine','OSAV':'Office fédéral de la sécurité alimentaire et des affaires vétérinaires','MBq':'mégabecquerels, unité d’activité radioactive','Gy':'grays, unité de dose absorbée'})
l=Lesson('Goitre',8)
l.add('Le goitre correspond à une {augmentation du volume de la thyroïde}. Il peut être diffus ou nodulaire. Son volume ne préjuge ni de la fonction hormonale ni de la bénignité de chaque nodule.',paras(
    'Les HUG décrivent le goitre comme une augmentation de la taille de la glande thyroïde. Le référentiel de la SFE distingue les formes diffuses et nodulaires. Une thyroïde augmentée peut fonctionner normalement, produire trop d’hormones ou en produire insuffisamment.',
    'Un nodule est une lésion individualisée au sein de la glande ; un goitre multinodulaire en contient plusieurs. Un nodule isolé peut exister sans augmentation globale du volume. Une masse latérale ganglionnaire ou salivaire n’est pas un goitre.',
    'Un goitre plongeant se prolonge sous le défilé cervico-thoracique. Sa portion visible au cou ne représente pas toujours tout son volume. L’extension et le retentissement sont des éléments distincts du bilan hormonal.'
),(46,47,48))
l.add('Le {contexte suisse de l’iode} aide à comprendre les causes sans déterminer seul le diagnostic. L’iodation du sel a réduit le goitre carentiel. Une tuméfaction actuelle demande néanmoins une évaluation individuelle.',paras(
    'Les HUG rappellent la diminution des goitres en Suisse grâce au sel iodé. Le goitre reste influencé par l’âge, des facteurs familiaux, des affections thyroïdiennes et la disponibilité en iode. Une histoire familiale n’établit pas à elle seule la nature bénigne d’une masse.',
    'Le monitorage OSAV 2020–2022 rapporte un statut iodé suffisant chez les écoliers étudiés et insuffisant chez les femmes enceintes étudiées. Ce constat de population ne signifie pas que chaque femme enceinte a un goitre, ni qu’une thyroïde de volume normal exclut un apport insuffisant.',
    'Aucune prévalence suisse contemporaine du goitre dans l’ensemble de la population n’a été identifiée dans ces lectures. Les chiffres de fréquence des nodules échographiques ne sont pas transposés à la fréquence des goitres palpables ni à celle des gonflements cervicaux symptomatiques.'
),(46,47,49))
l.add('La {croissance glandulaire et l’autonomie de certains nodules} expliquent les principaux profils. Le manque d’iode peut favoriser la stimulation et la croissance. Une compression peut apparaître même lorsque les hormones restent normales.',paras(
    'L’iode est nécessaire à la production des hormones thyroïdiennes. Une disponibilité insuffisante peut favoriser la sensibilité du tissu à l’effet trophique de la TSH et aux facteurs de croissance. Le volume peut donc augmenter sans qu’une hypothyroïdie manifeste soit présente.',
    'Au fil du temps, un goitre peut devenir hétérogène et nodulaire. Certaines zones acquièrent une production hormonale autonome, c’est-à-dire moins dépendante de la régulation habituelle. Le fonctionnement et l’aspect échographique répondent ainsi à deux questions différentes.',
    'L’augmentation de volume peut déplacer ou rétrécir la trachée et gêner l’œsophage ou le drainage veineux. Une déviation de la trachée n’est pas nécessairement un rétrécissement de son calibre. Le symptôme doit être rapproché de la cartographie anatomique.',
    'Une thyroïdite peut aussi augmenter le volume. Dans la forme subaiguë douloureuse, la libération d’hormones déjà stockées peut provoquer une thyrotoxicose transitoire. Ce mécanisme n’est pas identique à une production excessive autonome.'
)+table(['Perturbation','Exploration','Réponse adaptée'],[
    ['Croissance diffuse ou nodulaire','Palpation et échographie avec mesure du volume.','Surveillance ou traitement du volume selon gêne et risque.'],
    ['Production autonome','TSH puis hormones et scintigraphie selon le profil.','Prise en charge endocrinologique de l’autonomie.'],
    ['Compression des organes voisins','Évaluation des symptômes et imagerie de l’extension.','Avis chirurgical ou autre traitement du volume selon le contexte.'],
    ['Nodule morphologiquement suspect','Échographie classée et cytoponction si indiquée.','Parcours diagnostique puis thérapeutique adapté au résultat.'],
    ['Inflammation avec libération hormonale','Douleur, contexte, bilan biologique et échographique.','Traitement de la cause inflammatoire distinct d’un traitement d’autonomie.']
]),(46,47,48,49))
l.add('Le tri cherche d’abord une {compression menaçante ou une évolution suspecte}. Dyspnée, stridor et aggravation rapide imposent une évaluation urgente. Une fonction hormonale normale ne lève pas ce risque mécanique.',table(['Situation','Question discriminante','Conduite'],[
    ['Dyspnée, stridor ou gêne importante en position couchée','Le goitre comprime-t-il les voies aériennes ?','Appeler au 144 hors hôpital si menace respiratoire et organiser l’évaluation urgente.'],
    ['Gonflement brutal et douloureux','Existe-t-il une hémorragie dans un nodule ou une autre lésion aiguë ?','Évaluer rapidement le retentissement et la nécessité d’un geste.'],
    ['Croissance rapide, masse dure ou fixée, voix persistante modifiée','Existe-t-il une tumeur ou une atteinte laryngée ?','Orientation spécialisée rapide et exploration adaptée.'],
    ['Palpitations importantes ou décompensation cardiaque avec signes thyrotoxiques','Existe-t-il une complication de l’hyperthyroïdie ?','Évaluation urgente du retentissement et traitement de la cause.'],
    ['Masse stable sans gêne, fonction normale et bilan rassurant','La surveillance est-elle appropriée ?','Décider le suivi après caractérisation, sans chirurgie automatique.']
]),(46,47,48))
l.add('L’anamnèse précise les {symptômes mécaniques, hormonaux et les facteurs de risque}. Elle distingue une croissance lente d’un changement récent. Le projet de grossesse et les expositions iodées peuvent modifier la stratégie.',steps(
    'Dater la découverte et les changements de volume, de douleur ou de consistance afin d’identifier une évolution inhabituelle.',
    'Demander dyspnée, gêne couchée, dysphagie et changement de voix, car ils orientent vers une compression ou une atteinte locale.',
    'Rechercher signes d’excès ou de déficit hormonal et retentissement cardiaque afin d’orienter les dosages.',
    'Demander antécédents thyroïdiens familiaux, irradiation cervicale et examens ou prélèvements antérieurs pour apprécier le risque.',
    'Relever médicaments, compléments et examens récents avec contraste iodé, car ces expositions peuvent modifier la fonction ou le choix d’une exploration.',
    'Préciser grossesse, allaitement, âge, comorbidités et préférences avant de discuter surveillance ou traitement.'
),(47,48,50))
l.add('L’examen recherche une {masse thyroïdienne et ses effets}. La palpation apprécie symétrie, consistance et mouvement à la déglutition. Les ganglions et la voix doivent aussi être évalués.',paras(
    'Observer le cou au repos puis pendant une déglutition tolérée. Une thyroïde non augmentée ne crée normalement pas une tuméfaction cervicale évidente. Palper doucement les deux lobes et l’isthme en repérant la trachée, sans comprimer une masse symptomatique.',
    'Une masse thyroïdienne monte habituellement à la déglutition. Décrire volume apparent, régularité, nodules, douleur et mobilité. Une masse qui ne présente pas ce comportement demande de vérifier son origine plutôt que de forcer le diagnostic de goitre.',
    'Si le pôle inférieur n’est pas accessible à la palpation, une extension plongeante est possible. L’examen ne peut pas en mesurer l’étendue. Rechercher déviation trachéale, adénopathies et signes de compression, puis choisir l’imagerie.',
    'Apprécier fréquence cardiaque, tremblement et autres signes orientant la fonction selon le tableau. Une palpation souple ou une voix normale ne suffit pas à exclure un nodule suspect. Les signes biologiques et morphologiques restent complémentaires.'
),(46,47,48))
l.add('L’approche syndromique sépare {volume, fonction et risque tumoral}. Une même personne peut présenter plusieurs de ces dimensions. Le bilan doit répondre à chacune sans les confondre.',table(['Profil','Ce qui le soutient','Conséquence'],[
    ['7.1 — Goitre euthyroïdien non compressif','Le volume est augmenté, sans symptôme mécanique significatif ni dysfonction documentée.','Caractériser les nodules et discuter une surveillance.'],
    ['7.2 — Goitre hyperfonctionnel','Une TSH basse et des hormones adaptées au tableau orientent le bilan.','Rechercher l’étiologie, notamment autonomie nodulaire ou maladie de Basedow.'],
    ['7.3 — Goitre inflammatoire ou hypothyroïdien','Douleur, contexte auto-immun et bilan hormonal orientent selon le cas.','Ne pas traiter toutes les thyroïdites comme une autonomie.'],
    ['7.4 — Goitre compressif ou plongeant','Dyspnée, dysphagie, voix modifiée ou extension profonde sont présents.','Évaluer rapidement l’anatomie et la stratégie de réduction du volume.'],
    ['7.5 — Nodule ou ganglion suspect','Morphologie échographique, évolution ou examen sont inquiétants.','Organiser le diagnostic cytologique ou tissulaire approprié.']
]),(46,47,48))
l.add('Le {diagnostic positif} établit l’augmentation de volume et son origine thyroïdienne. L’échographie décrit le tissu et les nodules. Ni une TSH normale ni le mot goitre ne permettent de conclure à la bénignité.',paras(
    'Le diagnostic clinique repose sur une thyroïde augmentée ; l’échographie précise le volume et l’architecture. Les critères de volume dépendent notamment de l’âge et de la corpulence. Un seuil adulte n’est pas transposé à un enfant.',
    'Le référentiel SFE/CEEDMM publié en ligne en 2022 donne comme repères échographiques un volume supérieur à 18 ml chez la femme et à 20 ml chez l’homme, et supérieur à 16 ml chez l’adolescent. Ces repères ne déterminent pas à eux seuls l’urgence ou l’indication de traitement.',
    'Le diagnostic étiologique distingue goitre simple, autonomie nodulaire, maladie auto-immune, thyroïdite et autres causes. Le nodule suspect suit une stratification spécifique. La fonction normale ne dispense pas de cette analyse morphologique.'
),(47,48))

crit=l.subwindow('nodules','Nodules : cytoponction et interprétation',paras('La recommandation ETA 2023 utilise EU-TIRADS pour le risque échographique et Bethesda pour le résultat cytologique. Leurs numéros ne décrivent pas la même chose. La décision intègre aussi symptômes, ganglions, extension et préférence du patient.')+table(['Classe échographique','Seuil usuel de cytoponction ETA 2023','Limite'],[
    ['EU-TIRADS 3','Nodule de plus de 20 mm.','Le contexte clinique reste intégré.'],
    ['EU-TIRADS 4','Nodule de plus de 15 mm.','Une taille inférieure ne remplace pas le suivi adapté.'],
    ['EU-TIRADS 5','Nodule de plus de 10 mm.','Une adénopathie suspecte ou une extension peut modifier la décision.']
])+paras('Ces seuils concernent le parcours adulte décrit par la recommandation. Ils ne s’appliquent pas automatiquement à la pédiatrie. Les nodules réellement hyperfonctionnels à la scintigraphie suivent un parcours différent ; la scintigraphie peut éviter une ponction inappropriée.',
    'Une cytologie non diagnostique n’est pas une cytologie bénigne. Une cytologie indéterminée nécessite discussion, parfois nouvelle ponction, examens complémentaires ou chirurgie selon le risque. Une cytologie bénigne discordante avec une échographie très suspecte appelle une réévaluation.',
    'L’ETA 2023 recommande notamment un suivi à un an pour un nodule EU-TIRADS 4 sous 15 mm et tous les 6 à 12 mois pour un EU-TIRADS 5 sous 10 mm non ponctionné. Le suivi se raccourcit si des symptômes ou des signes suspects apparaissent. Les intervalles ne sont pas présentés comme des garanties de bénignité.'),(48,))
l.add('Les {examens complémentaires} évaluent fonction, structure et extension. Le premier bilan repose sur la TSH et l’échographie dans le contexte approprié. Une ponction est ciblée par le risque, pas par le seul mot goitre.',
    '<h3>9.a — Référence selon la question</h3>'+paras('L’échographie mesure le volume et caractérise les nodules ; elle ne prouve pas à elle seule une malignité. La cytoponction échoguidée apporte une information cytologique lorsqu’elle est indiquée. L’histologie peut rester nécessaire pour certains diagnostics : '+crit+'.')+
    '<h3>9.b — Première intention</h3>'+paras('Doser la TSH et réaliser une échographie thyroïdienne avec examen des compartiments ganglionnaires quand une maladie nodulaire est suspectée. Si la TSH est anormale, compléter par les hormones libres et les examens étiologiques adaptés. Les limites du laboratoire et le contexte physiologique sont pris en compte.')+
    table(['Résultat','Signification','Décision'],[
        ['TSH normale','Une euthyroïdie est compatible avec un goitre.','Poursuivre l’analyse anatomique et du risque nodulaire.'],
        ['TSH basse','Une production autonome ou une autre cause de thyrotoxicose est possible.','Préciser les hormones et discuter anticorps ou scintigraphie selon le tableau.'],
        ['TSH élevée','Un déficit hormonal ou un autre contexte doit être caractérisé.','Compléter notamment par thyroxine libre et recherche étiologique appropriée.'],
        ['Nodule ou ganglion suspect à l’échographie','La fonction hormonale ne suffit pas à conclure.','Discuter un prélèvement ciblé dans le parcours spécialisé.']
    ])+
    '<h3>9.c — Alternatives et limites</h3>'+paras('La scintigraphie recherche notamment les zones hyperfonctionnelles quand la TSH est basse. Elle ne remplace pas l’échographie morphologique. La décision de dosage de calcitonine dépend du contexte et du parcours spécialisé ; l’ETA 2023 ne fixe pas une recommandation universelle pour ou contre son dosage systématique initial.')+
    '<h3>9.d — Seconde intention et compression</h3>'+paras('Un scanner ou une imagerie par résonance magnétique précise une extension rétrosternale ou une compression. Le protocole, notamment la nécessité de contraste iodé, est discuté avec radiologue et endocrinologue car une exposition iodée peut modifier la fonction. L’examen laryngé est adapté à la dysphonie et au projet opératoire.'),(47,48))
l.add('L’{arbre décisionnel} part de la gravité puis analyse fonction et morphologie. La surveillance est une décision après bilan. Une indication de traitement ne signifie pas une technique unique pour tous.',steps(
    'Si une menace respiratoire ou une compression aiguë est suspectée, alors organiser l’évaluation urgente des voies aériennes et de l’anatomie.',
    'Si le patient est stable, alors préciser origine thyroïdienne, fonction et morphologie par examen, TSH et échographie.',
    'Si la TSH est basse, alors caractériser la thyrotoxicose et rechercher notamment une autonomie avant de décider une ponction ou un traitement.',
    'Si un nodule ou un ganglion est suspect, alors organiser le prélèvement adapté et sa confrontation à l’imagerie.',
    'Si le goitre est bénin, euthyroïdien et peu symptomatique, alors discuter une surveillance structurée.',
    'Si le volume gêne, comprime, s’étend ou s’accompagne d’une maladie nécessitant un traitement, alors comparer les options spécialisées et organiser le suivi.'
),(46,47,48))
r=radioiode(l)
l.add('La {prise en charge en Suisse} dépend de la cause, de la compression et du risque nodulaire. Un goitre bénin peu gênant peut être surveillé. La chirurgie ou une autre technique spécialisée est discutée lorsque le bénéfice attendu justifie l’intervention.',
    '<h3>11.A — But</h3>'+paras('Soulager ou prévenir une compression significative, traiter une dysfonction identifiée et établir la nature des lésions suspectes. Éviter en parallèle une intervention inutile sur une maladie stable et bénigne. Le choix intègre symptômes, comorbidités et souhaits du patient.')+
    '<h3>11.B — Moyens</h3>'+paras('Devant une menace respiratoire, commencer par l’équipe d’urgence et les voies aériennes. Dans les situations stables, organiser la caractérisation endocrinologique et échographique avant de choisir un traitement du volume.',
    'Les HUG décrivent la surveillance pour les goitres restreints, non compressifs et sans trouble fonctionnel. Pour les goitres gênants, volumineux ou plongeants, une thyroïdectomie partielle ou totale est discutée. La voie opératoire dépend de l’extension ; une extension thoracique ne signifie pas automatiquement une ouverture du sternum.',
    'La recommandation ETA 2023 prévoit un traitement en médecine nucléaire pour certaines autonomies ou certains goitres multinodulaires bénins. Elle prévoit aussi une destruction thermique pour certains nodules solides bénins symptomatiques et un traitement par éthanol pour des lésions kystiques sélectionnées. Confirmer la nature bénigne et les critères de sélection avant une réduction locale.',
    'Ces techniques ne traitent pas instantanément une urgence compressive. Leur disponibilité et leur indication sont appréciées par l’équipe. La fonction des cordes vocales, le risque hémorragique, les rapports anatomiques et les contre-indications sont évalués avant un geste. L’information professionnelle suisse de la capsule thérapeutique est détaillée ici : '+r+'.',
    'Un traitement hormonal visant à réduire la TSH n’est pas indiqué de routine chez une personne euthyroïdienne avec maladie nodulaire. Une dysfonction réelle suit son traitement étiologique, distinct d’un simple traitement du volume. Aucune dose universelle d’hormone, d’antithyroïdien ou de radiopharmaceutique n’est prescrite à partir du seul diagnostic de goitre.',
    'L’iode alimentaire et une supplémentation ciblée ne sont pas un traitement empirique de toute masse. L’OSAV recommande aux femmes envisageant une grossesse, enceintes ou allaitantes de discuter les compléments avec leur gynécologue. Une maladie thyroïdienne préexistante demande une coordination endocrinologique.',
    'Le parcours adulte ETA 2023 ne remplace pas une décision pédiatrique ou obstétricale. Les examens nucléaires et les traitements radioactifs nécessitent notamment la vérification des contre-indications liées à la grossesse ou à l’allaitement. L’activité et la spécialité exactes d’un traitement nucléaire sont arrêtées dans le service compétent, pas par transposition d’un exemple étranger.')+
    '<h3>11.C — Surveillance</h3>'+paras('Contrôler symptômes, volume, fonction et nodules selon leur risque. Une croissance récente, une nouvelle dysphonie ou une gêne respiratoire fait avancer la réévaluation. Une cytologie bénigne ne dispense pas d’examiner une discordance clinique ou échographique.',
    'Après un geste, suivre les consignes de l’équipe et l’évolution de la fonction thyroïdienne. Une dyspnée ou un gonflement cervical rapidement croissant impose une évaluation urgente. Les contrôles biologiques et l’éventuelle substitution sont adaptés à l’étendue du geste et aux résultats.')+
    '<h3>11.D — Pronostic et suivi durable</h3>'+paras('Le pronostic est généralement favorable pour un goitre bénin correctement surveillé ou traité, mais dépend de sa cause et de ses complications. La fin d’une intervention ne clôt pas nécessairement le suivi hormonal. Le patient doit disposer d’un plan écrit précisant qui contrôle la fonction, les nodules résiduels et les symptômes.'),(46,47,48,49,50,51))
l.add('La {prévention} vise un apport iodé adapté et une surveillance proportionnée. Elle n’impose pas une supplémentation systématique à toute personne. Les besoins et les risques sont appréciés selon le terrain.',paras(
    'En Suisse, le sel iodé fait partie de la prévention de la carence. L’OSAV encourage une alimentation riche en iode et une attention particulière aux groupes vulnérables. Cela n’est pas une consigne d’augmenter sa consommation globale de sel.',
    'Une personne enceinte ou allaitante, ou préparant une grossesse, discute d’un éventuel complément avec son gynécologue. Un apport excessif n’est pas la réponse automatique à un goitre déjà constitué. Les médicaments, compléments et expositions iodées doivent être signalés au prescripteur.',
    'La prévention secondaire repose sur le contrôle des nodules réellement identifiés et des changements de symptômes. Un dépistage échographique systématique des adultes asymptomatiques n’est pas recommandé par l’ETA 2023. Un antécédent familial particulier peut toutefois relever d’un parcours ciblé.'
),(48,49,50))
l.add('Les {points clés} sont le volume, la fonction et les nodules. Chacun demande une réponse propre. Une thyroïde qui fonctionne normalement peut néanmoins comprimer ou contenir une lésion suspecte.',steps(
    'Confirmer l’origine thyroïdienne de la masse et rechercher les symptômes compressifs.',
    'Doser la TSH et caractériser la morphologie, sans confondre ces deux axes.',
    'Adapter la ponction au risque du nodule et au contexte fonctionnel.',
    'Cartographier l’extension profonde si elle est suspectée.',
    'Discuter surveillance et traitements spécialisés avec des objectifs explicites.',
    'Organiser le suivi hormonal et morphologique après la décision.'
),(46,47,48))
l.quiz([
    ('Le goitre signifie-t-il hyperthyroïdie ?','Non. Il décrit une augmentation de volume ; la fonction peut être normale, excessive ou insuffisante.'),
    ('Une TSH normale exclut-elle un nodule malin ?','Non. Le risque morphologique et cytologique est évalué séparément.'),
    ('La taille visible au cou montre-t-elle tout le goitre ?','Non. Une portion peut descendre dans le thorax et nécessiter une cartographie adaptée.'),
    ('Une gêne respiratoire doit-elle attendre le rendez-vous d’échographie ?','Non. Une menace des voies aériennes impose une évaluation urgente.'),
    ('Quel est le premier dosage hormonal orientant le bilan ?','La TSH, complétée selon le résultat et le contexte.'),
    ('Une trachée déviée est-elle forcément rétrécie ?','Non. L’imagerie distingue déplacement et diminution du calibre.'),
    ('Faut-il ponctionner automatiquement le plus gros nodule ?','Non. Le choix intègre les signes de risque échographique, le contexte clinique et la fonction.'),
    ('Quels seuils usuels de ponction donne l’ETA 2023 ?','Plus de 20 mm pour EU-TIRADS 3, plus de 15 mm pour EU-TIRADS 4, plus de 10 mm pour EU-TIRADS 5, avec les exceptions et le contexte clinique.'),
    ('Bethesda et EU-TIRADS sont-ils la même classification ?','Non. Bethesda classe le résultat cytologique ; EU-TIRADS classe le risque échographique.'),
    ('Faut-il prescrire des hormones pour faire diminuer tout goitre euthyroïdien nodulaire ?','Non. Ce traitement n’est pas recommandé de routine ; une véritable dysfonction nécessite son propre diagnostic et traitement.'),
    ('Un goitre bénin impose-t-il toujours une chirurgie ?','Non. Une surveillance ou une autre technique sélectionnée peut être appropriée selon gêne, fonction et risque.'),
    ('Une cytologie non diagnostique est-elle rassurante comme une cytologie bénigne ?','Non. Le prélèvement peut être insuffisant et doit être réévalué selon le contexte.'),
    ('Les seuils adultes s’appliquent-ils directement à l’enfant ?','Non. La pédiatrie nécessite ses critères et une expertise adaptée.'),
    ('Faut-il augmenter spontanément les compléments iodés devant un goitre ?','Non. L’apport et les éventuels compléments sont appréciés selon le terrain ; un excès peut aussi poser problème.')
],(46,47,48,49,50))
l.write()
