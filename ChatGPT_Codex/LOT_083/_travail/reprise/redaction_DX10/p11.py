def rediger(c):
 c.block(11,'11.A Le but est une rémission clinique avec récupération fonctionnelle documentée',[
 ('Le traitement vise la rémission musculaire, cutanée et viscérale, tout en prévenant les complications et les effets indésirables.','pnds-objectif+bsr-i'),
 ('La force initiale est documentée groupe par groupe, puis comparée aux examens ultérieurs avec le même outil.','pnds-mmt+bsr-i'),
 ('Le grade 5 de la cotation MRC sert de comparateur normal, sans devenir un seuil universel de sortie ou d’arrêt thérapeutique.','mrc-test+rms-fonction'),
 ('L’objectif fonctionnel tient compte des tâches antérieures et des séquelles éventuelles ; une baisse de CK seule ne démontre pas sa réalisation.','rms-bilan+rms-fonction+bsr-xii'),
 ('Le projet associe donc le contrôle de maladie, la sécurité de déglutition, la fonction respiratoire et les activités quotidiennes.','bsr-i+bsr-xi+ers-cadence+bsr-xii'),
 ('La stratégie est réévaluée lorsque les domaines cliniques évoluent différemment, afin de ne pas augmenter l’immunosuppression sur un chiffre isolé.','rms-bilan+bsr-i')])
 c.fen(11,'Urgence — conduite chronologique',[
 ('D’abord, une menace respiratoire, une déglutition dangereuse ou une suspicion de myocardite fait organiser une prise en charge hospitalière urgente.','pnds-severite+pnds-hospitalisation'),
 ('L’évaluation immédiate décrit la respiration, les symptômes de déglutition, les signes cardiaques et la sévérité de la faiblesse.','pnds-examen'),
 ('Si les fausses routes ou la dysphagie compromettent l’alimentation, l’équipe précise la sécurité nutritionnelle et le besoin d’une prise en charge spécialisée.','pnds-severite+bsr-xi'),
 ('L’atteinte cardiaque est explorée par les moyens adaptés, avec préférence pour la troponine I parmi les marqueurs cités.','bsr-x'),
 ('La menace pulmonaire est caractérisée avec les spécialistes respiratoires, sans attendre que la faiblesse périphérique soit nécessairement importante.','bsr-iii+fr-mda5'),
 ('Ensuite, l’équipe spécialisée articule le traitement de maladie et les mesures propres à l’organe atteint.','bsr-i+bsr-iii+bsr-xi'),
 ('L’induction immunosuppressive tient compte des causes concurrentes et des infections pertinentes, sans retarder une prise en charge d’organe menaçante.','rms-bilan+pnds-severite'),
 ('La planification de la surveillance et du relais commence dès cette prise en charge, selon le traitement réellement retenu.','bsr-i+im-warn+oc-dose')])
 c.block(11,'11.B La séquence thérapeutique est adaptée aux domaines atteints',[
 ('La BSR recommande un glucocorticoïde à dose élevée pour l’induction d’une inflammation musculaire active.','bsr-i'),
 ('Elle recommande aussi une stratégie d’épargne pour contrôler l’inflammation et diminuer la charge de corticoïdes.','bsr-i'),
 ('Chez l’adulte, les options considérées comprennent notamment l’azathioprine, le méthotrexate et d’autres immunosuppresseurs choisis avec l’équipe spécialisée.','bsr-i'),
 ('Cette recommandation ne hiérarchise pas uniformément les traitements conventionnels en première, deuxième et troisième lignes pour tous les adultes.','bsr-i'),
 ('Le choix tient donc compte du phénotype, des organes, des contre-indications et de la tolérance attendue.','bsr-i+bsr-vi'),
 ('Des immunoglobulines intraveineuses sont considérées devant une inflammation musculaire sévère ou réfractaire.','bsr-i'),
 ('La BSR les considère également dans certaines atteintes cutanées réfractaires et dans une dysphagie résistante à d’autres traitements.','bsr-ii+bsr-xi'),
 ('Le rituximab et le cyclophosphamide figurent parmi les autres possibilités spécialisées pour certaines formes réfractaires ou sévères.','bsr-i'),
 ('Leur mention dans une recommandation européenne ne constitue pas une affirmation d’indication suisse pour chaque spécialité et chaque schéma.','bsr-i+sp-ind+im-ind+oc-ind'),
 ('Les posologies détaillées ci-dessous concernent uniquement les spécialités dont la notice suisse a été consultée pour ce cours.','sp-dose+im-dose+oc-dose')])
 c.tab(11,'Médicaments : cadre de prescription des trois spécialités suisses retenues',['Spécialité et indication','Dose et voie de la notice','Durée et réévaluation','Précaution majeure'],[
  [('Spiricort® contient de la prednisolone et cite la dermatomyosite systémique parmi ses indications.','sp-ind+sp-meca'),('Son cadre initial général est de 5 à 60 mg par jour par voie orale, avec adaptation à la maladie et à la réponse.','sp-dose'),('La notice ne définit pas une durée fixe propre à la dermatomyosite ; la réduction est individualisée.','sp-dose'),('Le terrain infectieux et les contre-indications d’un usage prolongé doivent être examinés.','sp-ci+sp-warn')],
  [('Imurek® contient de l’azathioprine et cite la dermatomyosite/polymyosite.','im-ind+im-meca'),('Pour les autres affections, l’AIPS donne initialement 1 à 3 mg/kg par jour, en prise unique ou en 2 prises.','im-dose'),('L’absence d’amélioration dans les 3 mois fait réévaluer l’intérêt de poursuivre.','im-dose'),('Une surveillance hématologique adéquate est indispensable ; l’hypersensibilité est une contre-indication.','im-warn+im-ci')],
  [('Octagam® 10 % cite la dermatomyosite active de l’adulte dans les conditions décrites par sa notice.','oc-ind+oc-dose'),('Le schéma est de 2 g/kg par voie intraveineuse, répartis sur 2 à 5 jours consécutifs toutes les 4 semaines.','oc-dose'),('L’effet est évalué après chaque cycle ; sans effet à 6 mois, le traitement doit être arrêté.','oc-dose'),('Le débit en dermatomyosite ne dépasse pas 0,04 mL/kg/min et le risque thromboembolique impose une surveillance.','oc-dose+oc-warn')]
 ])
 c.fen(11,'Prednisolone : distinguer le cadre AIPS du protocole individuel d’induction',[
 ('L’AIPS de Spiricort porte le numéro Swissmedic 38840 et sa mise à jour est de juin 2026.','sp-num+sp-date'),
 ('Elle demande de déterminer la dose selon la nature, la gravité et l’évolution de l’affection ainsi que la réponse du patient.','sp-dose'),
 ('La fourchette initiale générale de 5 à 60 mg par jour n’est pas présentée comme un algorithme pondéral spécifique de dermatomyosite.','sp-dose'),
 ('La BSR précise l’objectif d’induction à dose élevée ; l’équipe spécialisée fixe le schéma individuel dans ce contexte.','bsr-i+sp-dose'),
 ('Une administration intraveineuse éventuelle fait appel à une préparation soluble appropriée, et non aux comprimés de Spiricort.','sp-dose'),
 ('Aucun schéma de bolus n’est déduit ici de la présentation orale, puisque la notice renvoie aux préparations adéquates.','sp-dose'),
 ('Une exposition prolongée nécessite la dose efficace la plus faible possible et une surveillance clinique et biologique régulière.','sp-dose'),
 ('Lorsque le traitement dépasse 8 à 10 jours, la notice demande une diminution lente et progressive plutôt qu’un arrêt brutal.','sp-dose'),
 ('La réduction doit également tenir compte du risque de récidive de maladie et d’insuffisance corticosurrénale.','sp-dose'),
 ])
 c.fen(11,'Azathioprine : indication, administration et contrôle de toxicité',[
 ('L’AIPS d’Imurek porte le numéro Swissmedic 31887 et mentionne une mise à jour d’avril 2026.','im-num+im-date'),
 ('La posologie initiale de 1 à 3 mg/kg par jour relève de la rubrique des autres affections, distincte du schéma de transplantation.','im-dose'),
 ('La dose est ajustée selon l’état clinique et les paramètres hématologiques, dont l’évaluation accompagne l’introduction.','im-dose+im-warn'),
 ('Dès qu’un bénéfice clinique devient visible, la notice prévoit une réduction par paliers de 0,5 mg/kg vers la dose minimale efficace.','im-dose'),
 ('La notice ne fixe pas un intervalle universel entre ces paliers ; le suivi détermine leur mise en œuvre.','im-dose'),
 ('Les comprimés sont pris après le repas avec du liquide pour réduire les effets gastro-intestinaux.','im-dose'),
 ('Ils ne doivent être ni divisés ni écrasés ; les consignes de manipulation réduisent le contact avec des particules de produit.','im-dose'),
 ('Les variants NUDT15 et le déficit en thiopurine méthyltransférase peuvent augmenter le risque de toxicité hématologique.','im-dose+im-warn'),
 ('Une recherche génétique ou enzymatique ne remplace cependant pas la surveillance des cellules sanguines.','im-warn'),
 ('Un bénéfice retardé est possible ; l’absence d’amélioration dans les 3 mois impose de reconsidérer l’intérêt de poursuivre.','im-dose')])
 c.fen(11,'Immunoglobulines : le schéma de dermatomyosite reste spécifique à l’adulte',[
 ('L’AIPS d’Octagam 10 % porte le numéro Swissmedic 60323 et une mise à jour de juillet 2022.','oc-num+oc-date+oc-dose'),
 ('L’indication concerne une dermatomyosite adulte active déjà traitée par immunosuppresseurs, y compris corticoïdes, ou une intolérance ou contre-indication à ces médicaments.','oc-ind'),
 ('La dose totale de 2 g/kg est répartie à parts égales sur 2 à 5 jours consécutifs, avec répétition toutes les 4 semaines.','oc-dose'),
 ('La perfusion commence selon le cadre de la notice à 0,01 à 0,02 mL/kg/min pendant 30 minutes.','oc-dose'),
 ('Dans la dermatomyosite, le débit ne dépasse ensuite jamais 0,04 mL/kg/min, même si d’autres indications ont un plafond différent.','oc-dose'),
 ('Ce plafond spécifique répond au risque thromboembolique reconnu dans cette population.','oc-dose+oc-warn'),
 ('L’effet thérapeutique est évalué après chaque cycle et l’absence d’effet après 6 mois impose l’arrêt.','oc-dose'),
 ('Si le traitement est efficace, sa poursuite et l’adaptation ultérieure de la dose ou des intervalles reposent sur la réponse individuelle.','oc-dose'),
 ('L’indication adulte de cette spécialité n’est pas transposée automatiquement à une dermatomyosite juvénile.','oc-ind+bsr-v')])
 c.tab(11,'Situations particulières : la notice de chaque produit reste déterminante',['Situation','Prednisolone Spiricort','Azathioprine Imurek','Immunoglobulines Octagam'],[
  [('Un projet de grossesse nécessite une discussion spécialisée.','bsr-viii'),('La notice réserve la grossesse à une nécessité absolue et décrit les risques d’une exposition prolongée.','sp-gross'),('Il ne faut pas instaurer Imurek lors d’une grossesse planifiée ou avérée ; une poursuite éventuelle demande une balance bénéfice-risque.','im-gross'),('L’administration pendant la grossesse demande de la prudence, faute d’études contrôlées de sécurité.','oc-gross')],
  [('L’allaitement impose une vérification propre au produit.','sp-gross+im-gross+oc-gross'),('La notice demande l’arrêt de l’allaitement lors de l’utilisation systémique de corticostéroïdes.','sp-gross'),('L’AIPS demande de ne pas allaiter pendant le traitement par azathioprine.','im-gross'),('Les immunoglobulines passent dans le lait et la notice conserve une administration prudente.','oc-gross')],
  [('L’âge avancé et les comorbidités modifient la surveillance.','im-dose+oc-warn'),('La dose et la durée sont réévaluées selon la maladie et les effets indésirables.','sp-dose'),('La dose la plus faible possible est retenue et les paramètres hématologiques sont suivis.','im-dose'),('Le terrain thrombotique, l’hydratation et la fonction rénale sont appréciés.','oc-warn')],
  [('Une atteinte rénale ou hépatique demande une individualisation.','im-dose+oc-warn'),('Les contre-indications et précautions de l’utilisation prolongée sont examinées avant de retenir la stratégie.','sp-ci+sp-warn'),('La notice ne donne pas de table universelle fondée sur le taux plasmatique ; elle recommande une faible dose et la surveillance sanguine.','im-dose'),('Le risque rénal impose une surveillance, un faible débit et la discussion d’une interruption si une insuffisance rénale apparaît.','oc-warn')],
  [('La forme juvénile relève d’une équipe pédiatrique.','bsr-v'),('Les consignes pédiatriques de la notice ne sont pas remplacées par une dose adulte supposée.','sp-dose'),('L’expérience chez l’enfant et l’adolescent est décrite comme limitée.','im-dose'),('L’indication de dermatomyosite citée dans cette notice est celle de l’adulte.','oc-ind')]
 ])
 c.block(11,'Les formes pulmonaires, cutanées et bulbaires ont des décisions propres',[
 ('Pour une myosite avec pneumopathie interstitielle, ERS/EULAR recommande une immunosuppression et considère les associations selon la présentation.','ers-traitement+ers-association'),
 ('La BSR distingue une atteinte interstitielle rapidement progressive d’une atteinte chronique et demande une prise en charge respiratoire spécialisée.','bsr-iii'),
 ('Une forme rapidement progressive peut conduire à une induction et à une escalade précoces décidées avec cette équipe.','bsr-iii'),
 ('Le choix d’une molécule et d’une voie dans cette situation n’est pas déduit d’une posologie orale destinée à un autre contexte.','bsr-iii+sp-dose'),
 ('La photoprotection et les soins dermatologiques accompagnent la stratégie cutanée, même lorsqu’un traitement systémique est nécessaire.','bsr-ii'),
 ('Une atteinte cutanée réfractaire peut faire discuter les immunoglobulines ou le rituximab dans le cadre spécialisé décrit par la BSR.','bsr-ii'),
 ('La dysphagie demande parallèlement un bilan de déglutition et l’intervention de professionnels adaptés.','bsr-xi'),
 ('La réponse musculaire périphérique ne remplace pas l’appréciation de la sécurité de déglutition.','bsr-xi')])
 c.block(11,'La réadaptation et les moyens sociaux font partie du traitement',[
 ('Un programme d’exercice sûr et approprié est conduit avec des physiothérapeutes ou des ergothérapeutes expérimentés.','bsr-i'),
 ('L’exercice adapté est recommandé à travers les différents niveaux d’activité de maladie, avec une individualisation du programme.','bsr-xii'),
 ('Les objectifs comprennent la force utile, les gestes quotidiens et la qualité de vie, plutôt qu’une immobilisation prolongée systématique.','bsr-i+bsr-xii'),
 ('Le prurit, la douleur, les troubles du sommeil et le retentissement psychologique sont recherchés afin de traiter ce qui limite la participation.','bsr-xii'),
 ('Les activités professionnelles ou scolaires sont aménagées selon les manifestations et la récupération.','pnds-education+pnds-objectif'),
 ('En Suisse, la détection précoce de l’assurance-invalidité vise le contact rapide des personnes en incapacité de travail ou menacées de l’être.','ai-reintegration'),
 ('L’office AI apprécie avec l’assuré et les partenaires les mesures permettant un maintien de l’emploi ou une réinsertion.','ai-reintegration'),
 ('Cette démarche de réadaptation ne constitue pas une promesse automatique de prestation ou de rente.','ai-reintegration'),
 ])
 c.block(11,'11.C La surveillance donne à chaque effet indésirable une conduite',[
 ('Sous Imurek, la formule sanguine complète et les plaquettes sont contrôlées chaque semaine pendant les 8 premières semaines.','im-warn'),
 ('La notice demande ensuite un contrôle au moins tous les 3 mois, avec une fréquence accrue dans certaines situations à risque.','im-warn'),
 ('Une baisse anormale de numération impose une interruption immédiate, car les cellules peuvent encore diminuer après l’arrêt.','im-warn'),
 ('Une infection, des hématomes ou des saignements conduisent le patient à consulter immédiatement.','im-warn'),
 ('Le bilan hépatique est surveillé et le patient doit interrompre l’azathioprine dès les premiers signes de jaunisse.','im-warn'),
 ('Une hypersensibilité ou une cholestase attribuée à l’azathioprine impose l’arrêt selon les consignes de la notice.','im-warn'),
 ('L’association avec l’allopurinol nécessite une réduction majeure de dose et une supervision ; celle avec le fébuxostat n’est pas recommandée.','im-inter'),
 ('L’ensemble des traitements associés est donc revu avant l’introduction et lors de toute modification.','im-inter+sp-inter+oc-inter')])
 c.tab(11,'Surveillance : constater, interpréter et agir',['Ce qui est observé','Risque ou signification','Conduite associée'],[
  [('La force et les gestes fonctionnels sont réévalués.','bsr-i+pnds-mmt'),('Une limitation persistante peut refléter activité ou séquelles.','rms-fonction'),('Le traitement et la réadaptation sont réexaminés avec la clinique globale.','bsr-i+bsr-xii')],
  [('La déglutition est interrogée au cours du suivi.','bsr-xi'),('Une aggravation peut exposer à la dénutrition ou à l’inhalation.','bsr-xi'),('Le bilan spécialisé est renouvelé et la sécurité des apports est appréciée.','bsr-xi')],
  [('La numération sanguine est suivie sous azathioprine.','im-warn'),('Une baisse anormale peut annoncer une toxicité médullaire.','im-warn'),('Le traitement est interrompu immédiatement selon l’AIPS.','im-warn')],
  [('La diurèse et la créatinine sont contrôlées pendant le traitement par immunoglobulines.','oc-warn'),('Une atteinte rénale peut compliquer l’exposition, particulièrement sur terrain à risque.','oc-warn'),('Une interruption est envisagée si une insuffisance rénale survient.','oc-warn')],
  [('La tolérance de perfusion est observée chez le patient traité par Octagam.','oc-warn'),('Une réaction peut imposer une réduction de vitesse ou un arrêt.','oc-warn'),('La conduite dépend de sa nature et de sa sévérité ; un choc nécessite le traitement médical adapté.','oc-warn')],
  [('La pression artérielle, le poids, la glycémie et les électrolytes pertinents sont surveillés sous corticoïde.','sp-dose'),('L’exposition prolongée peut entraîner des complications métaboliques et autres effets indésirables.','sp-dose+sp-meca'),('La dose et la poursuite sont réévaluées avec une diminution supervisée si indiquée.','sp-dose')]
 ])
 c.fen(11,'Surveillance pulmonaire : un calendrier ne remplace pas une réévaluation clinique',[
 ('ERS/EULAR suggère des explorations fonctionnelles répétées tous les 3 à 6 mois pendant les premières années d’atteinte interstitielle.','ers-cadence'),
 ('Le suivi est ensuite poursuivi au moins tous les 6 à 12 mois selon cette proposition générale.','ers-cadence'),
 ('Pour une myosite à risque d’atteinte interstitielle sévère ou rapidement progressive, le scanner peut être répété après 3 à 6 mois.','ers-suivi'),
 ('Le guide propose ensuite un scanner annuel pendant les 2 premières années et lors d’une suspicion de progression.','ers-suivi'),
 ('Ces propositions sont conditionnelles et reposent sur un faible niveau de preuve ; le contexte clinique guide leur application.','ers-suivi+ers-cadence'),
 ('Une aggravation respiratoire avant l’échéance fait réévaluer immédiatement la situation clinique et les explorations nécessaires.','ers-cadence+pnds-severite')])
 c.block(11,'11.D Le relais est fondé sur les domaines évalués et les consignes comprises',[
 ('Le pronostic dépend de l’entité précise, du délai de prise en charge, des organes associés et de l’évolution sous traitement.','rms-conclusion'),
 ('Une CK diminuée ne suffit pas à conclure à la guérison fonctionnelle ni à autoriser un arrêt de toute surveillance.','rms-bilan+rms-fonction'),
 ('Avant un passage au suivi ambulatoire, l’équipe documente les problèmes d’organes et le plan adapté à leur degré de stabilité.','pnds-hospitalisation+bsr-iii+bsr-x+bsr-xi'),
 ('Le relais explicite également les prescriptions, les contrôles de toxicité et les personnes à contacter si un symptôme change.','im-warn+oc-dose+pnds-suivi'),
 ('La surveillance spécialisée et les évaluations fonctionnelles se poursuivent même lorsque l’activité inflammatoire diminue.','pnds-suivi+rms-fonction'),
 ('L’organisation du retour tient enfin compte des besoins de réadaptation et de l’environnement quotidien.','bsr-xii+ai-reintegration')])
 c.tab(11,'Vérifications individualisées avant un relais à domicile',['Domaine vérifié','Ce qui est documenté','Action ou relais prévu'],[
  [('La respiration a été évaluée.','pnds-examen'),('Le bilan décrit l’atteinte musculaire ou interstitielle et sa prise en charge.','ers-depistage+pnds-examen'),('Le suivi respiratoire et les signes imposant une réévaluation sont expliqués.','ers-cadence+ers-suivi')],
  [('La déglutition et les besoins nutritionnels ont été appréciés.','bsr-xi'),('Les difficultés et les moyens de réduire le risque d’inhalation sont identifiés.','bsr-xi'),('Le suivi des professionnels de déglutition est organisé si nécessaire.','bsr-xi')],
  [('L’évaluation cardiaque a répondu aux signes ou au risque suspecté.','bsr-x'),('Les résultats et le besoin d’exploration supplémentaire sont transmis.','bsr-x'),('La filière cardiaque est poursuivie selon les anomalies identifiées.','bsr-x+rms-conclusion')],
  [('Le patient comprend la prescription retenue.','sp-dose+im-dose+oc-dose'),('Les doses, la voie et les règles de réduction ou de contrôle sont écrites selon les produits prescrits.','sp-dose+im-dose+oc-dose'),('Les examens de surveillance et les conduites devant infection, jaunisse ou réaction sont explicités.','im-warn+oc-warn')],
  [('La force et les besoins d’aide sont documentés.','pnds-mmt+bsr-xii'),('Le retentissement dans les activités quotidiennes accompagne la cotation musculaire.','bsr-xii'),('La physiothérapie, l’ergothérapie et les démarches sociales sont coordonnées.','bsr-i+ai-reintegration')],
  [('La surveillance de maladie et du risque tumoral a été planifiée.','pnds-suivi+imacs-screen'),('Le niveau de risque et les examens déjà effectués sont transmis.','imacs-risk+imacs-screen'),('Le médecin traitant et l’équipe spécialisée se partagent le suivi prévu.','pnds-suivi+pnds-objectif')]
 ])
