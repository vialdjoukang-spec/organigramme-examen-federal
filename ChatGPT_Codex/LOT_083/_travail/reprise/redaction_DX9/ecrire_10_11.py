from rendu import outils

p,c,h,w,table,liste,save=outils(10)
a=w('L’orientation précède l’étiquette définitive',[
('Le premier embranchement identifie les personnes dont les constantes, la diurèse, le membre ou les électrolytes justifient des soins urgents.',['e13']),
('La deuxième décision porte sur l’admission et le niveau de surveillance ; le risque rénal est étudié avec la clinique et les résultats initiaux.',['e16','e09']),
('Le troisième temps organise le suivi de récupération et sélectionne les personnes nécessitant une recherche neuromusculaire.',['e14','e16']),
('La chronologie interdit de différer le traitement d’une complication au seul motif que la CK n’a pas encore atteint son maximum.',['e12','e13']),
('Chaque nouveau résultat est réinterprété si la douleur augmente, si les urines diminuent ou si le potassium progresse.',['b01','s04','s11'])])
s=h('Si un signe de danger est présent, la branche urgente s’ouvre')
s+=p('La fenêtre '+a+' ordonne le parcours d’un épisode après effort, depuis la menace immédiate jusqu’à l’enquête de susceptibilité.','e16','e13')
s+=liste([
'Si les constantes sont anormales, si une anurie apparaît ou si une complication métabolique est suspectée, alors la stabilisation et le bilan urgent commencent.'+c('e13','s02'),
'Si la kaliémie est sévère, s’il existe des signes électriques ou si une hausse rapide est attendue sur terrain malade, alors le monitorage et l’avis spécialisé sont organisés.'+c('k01','k04'),
'Si la douleur est disproportionnée ou s’aggrave à la mobilisation passive, alors le chirurgien sénior évalue la suspicion de loge et la nécessité d’une mesure de pression.'+c('b01'),
'Si la loge aiguë est confirmée, alors la décompression est immédiate ; la suite du bilan étiologique ne la retarde pas.'+c('b01','s03')])
s+=h('Si la situation est stable, la biologie confirme et stratifie')
s+=liste([
'Si les symptômes musculaires suivent un effort, alors les CK sont rapprochées de la chronologie, de la créatinine, des électrolytes et des urines.'+c('e12','s02','r08'),
'Si la CK seule est élevée sans symptôme systémique ni complication, alors une réponse postexercice reste possible et les interventions sont adaptées au risque.'+c('e02','e13'),
'Si la présentation et la cinétique répondent au consensus ENMC2025, alors le diagnostic d’épisode d’effort est retenu tout en recherchant ses complications.'+c('e12','e13'),
'Si le premier résultat est précoce ou si les manifestations évoluent, alors la réévaluation clinique et biologique tient compte du pic retardé.'+c('e12','s04'),
'Si la fonction rénale se dégrade ou si une surcharge apparaît pendant les apports, alors le remplissage est revu et l’indication d’épuration est discutée.'+c('s04','s09')])
s+=h('Si les facteurs réversibles sont identifiés, ils sont écartés')
s+=p('L’exercice est interrompu ; les médicaments, les toxiques et les autres circonstances sont analysés afin de supprimer l’agression lorsque cela est possible.','s03','e06')
s+=p('Si un déficit circulatoire nécessite une correction, les apports sont prescrits selon le terrain et la réponse, avec surveillance de la volémie et de la diurèse.','s04','aips-n4')
s+=p('Si le risque rénal est faible et la situation stable, l’intensité des soins est ajustée ; la seule CK ne justifie pas automatiquement un traitement agressif.','e13','e09')
s+=p('Si un trouble métabolique ou une complication rénale devient réfractaire, la néphrologie ou la réanimation détermine le recours à l’épuration.','s09','k04')
s+=h('Si la récupération est atypique, la branche étiologique reprend')
s+=liste([
'Si les crises se répètent, si l’effort était habituel ou si les proches sont atteints, alors une consultation neuromusculaire est organisée.'+c('e06','e14'),
'Si la CK reste élevée à8semaines, alors le critèreH de RHABDO participe à la sélection d’un bilan génétique ou métabolique.'+c('e06'),
'Si une faiblesse durable ou une constellation inflammatoire est observée, alors les anticorps et la biopsie sont discutés selon la suspicion.'+c('d03','e08'),
'Si les douleurs et la fonction se rétablissent, alors la reprise physique reste progressive et tient compte de la période recommandée après résolution des symptômes.'+c('e15')])
s+=p('Le relais comprend une explication des signes de nouvelle crise et une réévaluation du retentissement physique et psychologique de l’épisode.','e15','e16')
save(s)

p,c,h,w,table,liste,save=outils(11)
a=w('Urgence — conduite chronologique',[
('Au premier contact, l’activité est interrompue et les constantes, les urines et la gravité locale sont évaluées afin de choisir le circuit de soins.',['e13','s03']),
('Dès la suspicion de complication, le bilan musculaire, rénal et métabolique est prélevé ; une hyperkaliémie possible impose aussi son évaluation électrique.',['s02','k01']),
('Si la kaliémie est≥6,5mmol/L, ou si les autres critères électriques et cliniques l’exigent, le monitorage continu accompagne le traitement hospitalier.',['k01','k04']),
('Le traitement urgent de l’hyperkaliémie combine la protection cardiaque, le transfert du potassium vers les cellules et son élimination selon le protocole hospitalier.',['k02','k04']),
('Après traitement d’une hyperkaliémie modérée ou sévère, UKKA propose des dosages au moins à1,2,4,6et24heures pour rechercher réponse et rebond.',['k03']),
('Si une suspicion compartimentale existe, les pansements circulaires sont libérés ; la réévaluation suit dans les30minutes selon BOASt2025.',['b01']),
('Un membre à risque ou une conclusion incertaine reçoit une évaluation documentée horaire et un avis chirurgical sénior ; une loge confirmée est décomprimée immédiatement.',['b01']),
('Les apports nécessaires sont ensuite ajustés avec réévaluations répétées ; une anurie persistante ou une surcharge fait reconsidérer le remplissage et l’épuration.',['s04','s09'])])
b=w('Cristalloïde isotonique : Chlorure de sodium0,9%Baxter®',[
('Cette solution stérile apporte de l’eau, du sodium et du chlorure ; elle sert notamment au remplacement liquidien isotonique et aux déshydratations adaptées à son indication.',['aips-n3','aips-n12']),
('La notice porte le numéro d’autorisation Swissmedic41181 et sa mise à jour est datée de février2022.',['aips-n16','aips-n19']),
('Un litre contient9,0g de chlorure de sodium, avec154mmol/L de sodium et154mmol/L de chlorure.',['aips-n2']),
('L’administration est intraveineuse ; la posologie, la vitesse et la durée sont personnalisées selon indication, âge, poids, état clinique et résultats.',['aips-n4']),
('La distribution se fait dans l’espace extracellulaire et l’élimination dépend essentiellement du rein.',['aips-n13']),
('Chez le sujet sain, la notice décrit une rééquilibration extracellulaire en20–30minutes ; la fraction intravasculaire varie selon le contexte critique.',['aips-n13']),
('La solution peut entraîner une surcharge, une hypernatrémie, des troubles acido-basiques ou une réaction à la perfusion.',['aips-n6','aips-n10']),
('Une hypersensibilité suspectée impose l’interruption immédiate ; les symptômes de surdosage imposent aussi l’arrêt et une prise en charge appropriée.',['aips-n6','aips-n11'])])
d=w('Réhydratation individualisée : besoin et tolérance',[
('La correction d’une hypovolémie vise une perfusion rénale adéquate et une diminution de la concentration tubulaire des pigments.',['s03','s04']),
('Le volume est ajusté aux données cliniques, au poids, aux antécédents cardiorespiratoires, à la diurèse et à l’évolution biologique.',['s04']),
('La revue SRLF2026 souligne le risque de surcharge lorsque la perfusion est poursuivie seulement jusqu’à une CK inférieure à5000UI/L.',['s04']),
('Une anurie persistante ou des signes de surcharge conduisent à reconsidérer les apports et l’indication d’épuration plutôt qu’à augmenter mécaniquement le débit.',['s04']),
('Les cristalloïdes balancés et le NaCl0,9% appartiennent aux possibilités décrites par la revue ; le choix tient compte du bilan et de la tolérance.',['s05']),
('Le chlorure apporté en quantité peut contribuer à une acidose hyperchlorémique ; l’équilibre acido-basique est donc surveillé.',['s05','aips-n6'])])
e=w('Alcalinisation, diurétiques et calcium : éviter la routine',[
('Le consensus ENMC2025 ne trouve pas de preuve pour l’infusion de bicarbonate visant seulement à alcaliniser les urines.',['e10']),
('La revue SRLF2026 souligne les risques d’aggravation de l’hypocalcémie et de dépôts phosphocalciques, notamment lors d’une atteinte rénale sévère ou oligo-anurique.',['s06']),
('Le mannitol n’est pas recommandé ; les diurétiques de l’anse se discutent pour une surcharge et non pour traiter systématiquement la lyse.',['s07']),
('L’hypocalcémie initiale asymptomatique est respectée ; sa correction est réservée aux symptômes ou à une indication liée à l’hyperkaliémie menaçante.',['s08']),
('Le retour du calcium vers la circulation pendant la récupération expose à une hypercalcémie, particulièrement après des apports excessifs.',['s08']),
('Ces règles distinguent la prévention de complication d’une correction biologique automatique sans bénéfice clinique démontré.',['s06','s07','s08'])])
f=w('Épuration : traiter la complication réfractaire',[
('Une hyperkaliémie menaçante, une acidose profonde ou un œdème pulmonaire réfractaire peut imposer une épuration rénale.',['s09']),
('La décision intègre la vitesse d’augmentation du potassium, l’acidose, la diurèse et l’intensité de la rhabdomyolyse.',['s09']),
('La néphrologie ou la réanimation détermine urgemment la modalité et le moment du traitement en présence d’une menace vitale.',['k04']),
('L’extraction de myoglobine seule n’est pas une indication de dialyse prophylactique ; les membranes spécialisées ne remplacent pas l’évaluation clinique.',['s09']),
('Une indication chirurgicale étiologique reste prioritaire lorsqu’elle traite la source de lésion, sous réserve de la stabilisation d’une urgence vitale.',['s09','b01'])])
g=w('Terrains particuliers et sécurité de la perfusion',[
('Chez la personne insuffisante rénale, la rétention sodique et la tolérance aux volumes imposent une prudence particulière et une surveillance rapprochée.',['aips-n6']),
('L’insuffisance cardiaque ou pulmonaire et les affections hépatiques avec rétention hydrosodée modifient le choix du volume et du débit.',['aips-n6']),
('Chez la personne âgée, les maladies cardiaques, rénales, hépatiques et les médicaments associés participent au choix de prescription.',['aips-n6']),
('Chez l’enfant, les concentrations électrolytiques sont suivies étroitement ; les doses sont déterminées selon l’âge, le poids et le contexte pédiatrique.',['aips-n4','aips-n6']),
('Pendant la grossesse ou l’allaitement, le médecin compare attentivement les risques et les bénéfices de Chlorure de sodium0,9%Baxter avant administration.',['aips-n8']),
('Les médicaments favorisant la rétention ou l’action de la vasopressine sont examinés ; les interactions peuvent aggraver un trouble hydrique ou sodique.',['aips-n7'])])
s=h('11.A Les buts portent sur les complications et la récupération')
s+=p('La prise en charge suisse initiale vise la prévention des complications rénales et électrolytiques ; l’actualisation européenne précise une intensité adaptée au risque.','r01','e13')
s+=p('Le traitement corrige le déficit circulatoire, sécurise les électrolytes et écarte le facteur déclenchant, tout en surveillant la fonction rénale.','s03')
s+=p('La trajectoire enzymatique attendue au cours d’un épisode se rapproche du niveau de base après1–2semaines de repos selon ENMC2025.','e12')
s+=p('Ce repère ne constitue pas une cible de perfusion ; la clinique, la diurèse et l’équilibre métabolique déterminent les apports nécessaires.','s04')
s+=p('Le retour de la force et de la fonction accompagne la récupération ; l’évaluation volontaire peut être comparée à la cotation normale5de MRC.','m01','e16')
s+=h('11.B L’ordre des moyens suit la menace réellement présente')
s+=p('La fenêtre '+a+' distingue la stabilisation, les décisions rénales et les délais de réexamen documentés pour les complications.','e13','k03','b01')
s+=p('L’effort est interrompu et les facteurs réversibles sont supprimés avec l’équipe, car la poursuite de l’agression entretient la libération musculaire.','s03','e06')
s+=p('Une forme à faible risque ne reçoit pas automatiquement un traitement agressif sur sa seule CK ; les comorbidités et les signes rouges modifient cette décision.','e13')
s+=p('La '+d+' est prescrite lorsqu’elle est nécessaire ; une surveillance médicale empêche de transformer cette correction en surcharge.','s04','aips-n6')
s+=h('La spécialité documentée précise la prescription de remplissage')
s+=p('Le '+b+' possède une information professionnelle suisse utilisée pour la voie, les quantités, les précautions et les modalités d’arrêt.','aips-n4','aips-n6')
s+=table(['Spécialité et indication de notice','Dose, voie et durée','Restriction majeure et surveillance'],[
['Chlorure de sodium0,9%Baxter® apporte une solution de remplacement isotonique dans les indications de sa notice.'+c('aips-n3'),'Pour une déshydratation extracellulaire isotonique ou une déplétion sodique adulte, la dose recommandée est500mLà3litres/24h, par voie intraveineuse.'+c('aips-n4'),'Le volume, la vitesse et la durée sont personnalisés ; ce cadre général n’est pas un débit automatique de rhabdomyolyse.'+c('aips-n4','s04')],
['La même notice décrit les situations extrêmes et les états de choc.'+c('aips-n4'),'Dans ce contexte, elle autorise une augmentation selon le déficit, pouvant atteindre un maximum de2000mL/heure.'+c('aips-n4'),'Cette disposition de choc exige son indication et sa surveillance ; elle ne s’applique pas à une CK isolément élevée.'+c('aips-n4','e13')],
['La composition comprend154mmol/L de sodium et154mmol/L de chlorure.'+c('aips-n2'),'L’administration et la durée sont adaptées à la réponse clinique et aux analyses.'+c('aips-n4'),'La surveillance suit le bilan hydrique, les électrolytes et l’équilibre acido-basique.'+c('aips-n6')],
['Une réaction d’hypersensibilité ou un surdosage est suspecté.'+c('aips-n6','aips-n11'),'La perfusion est immédiatement interrompue puis la situation clinique est prise en charge.'+c('aips-n6','aips-n11'),'Le sodium, la surcharge, le contexte cardiorespiratoire et les paramètres physiologiques sont évalués.'+c('aips-n6','aips-n11')]])
s+=p('Les contre-indications de la spécialité comprennent l’hypervolémie, l’hypernatrémie, l’hyperchlorémie et la déshydratation hypertonique.','aips-n5')
s+=p('La présence d’une de ces contre-indications impose un autre choix thérapeutique ; le bilan initial et les réévaluations préviennent son emploi inadapté.','aips-n5','aips-n6')
s+=p('La notice précise les besoins pédiatriques selon le poids ; le volume de traitement d’une complication reste individualisé avec l’équipe pédiatrique.','aips-n4','aips-n6')
s+=p('Les autres cristalloïdes font l’objet d’un choix selon leur composition et le contexte ; aucune supériorité universelle n’est retenue pour toute rhabdomyolyse.','s05')
s+=h('Les autres moyens traitent une indication précise')
s+=p('La fenêtre '+e+' explique pourquoi le bicarbonate, le mannitol et la correction calcique ne sont pas ajoutés systématiquement à chaque perfusion.','e10','s06','s07','s08')
s+=p('La complication hyperkaliémique reçoit immédiatement le protocole de traitement et de monitorage du service ; une menace persistante mène à une décision d’épuration spécialisée.','k02','k04','s09')
s+=p('La fenêtre '+f+' relie la dialyse à la complication clinique et métabolique, plutôt qu’à la seule volonté d’extraire un pigment.','s09')
s+=p('Le syndrome des loges confirmé impose sa décompression, car les apports hydriques ne corrigent pas l’ischémie entretenue par la pression.','b01','s03')
s+=p('La reprise physique et la réhabilitation sont progressives ; les douleurs persistantes, la fatigue ou les difficultés psychologiques nécessitent un relais adapté.','e15','e16')
s+=h('Les situations particulières modifient le plan')
s+=p('La fenêtre '+g+' rassemble les risques documentés de la spécialité selon l’âge, le rein, le cœur, le foie et la maternité.','aips-n4','aips-n6','aips-n8')
s+=table(['Terrain','Adaptation concrète','Point de surveillance'],[
['Une insuffisance rénale est connue ou apparaît.','Les apports sont ajustés à la diurèse et au bilan clinique ; la notice requiert une prudence particulière.'+c('aips-n6','s04'),'La créatinine, le potassium, l’acidose et la surcharge guident l’escalade spécialisée.'+c('s04','s09')],
['Une maladie cardiaque, pulmonaire ou hépatique expose à la rétention.','Le volume et le débit tiennent compte du risque de congestion et des autres traitements.'+c('aips-n6'),'Les constatations cliniques et le bilan hydro-électrolytique sont répétés.'+c('aips-n6')],
['La personne est âgée.','Les comorbidités et les médicaments concomitants participent à la prescription.'+c('aips-n6'),'Le choix est réévalué selon la réponse et les analyses, sans appliquer un volume standard à tout âge.'+c('aips-n4','aips-n6')],
['La personne est un enfant ou un adolescent.','Le bilan et les apports suivent l’âge, le poids et l’expertise pédiatrique.'+c('aips-n4','aips-n6'),'La régulation des liquides et des électrolytes nécessite une vigilance spécifique.'+c('aips-n6')],
['Une grossesse ou un allaitement est en cours.','La comparaison individuelle des bénéfices et risques précède l’administration de la spécialité.'+c('aips-n8'),'La fonction rénale et la tolérance clinique restent incluses dans le suivi.'+c('aips-n6','aips-n8')],
['Les contraintes sociales ou professionnelles entravent le repos ou le suivi.','Le plan prévoit les contacts de soins, la limitation temporaire des charges et le relais de réhabilitation.'+c('e15','e16'),'L’équipe clarifie l’organisation des contrôles et des démarches nécessaires au retour fonctionnel.'+c('e15','e16')]])
s+=p('La coordination sociale et les questions d’assurance sont traitées avec l’équipe selon le contexte ; le plan précise les soins et les adaptations nécessaires.','e15','e16')
s+=h('11.C La surveillance évalue la réponse et les seuils d’action')
s+=table(['Élément suivi','Moment ou condition','Résultat qui modifie la conduite'],[
['La douleur, l’état neurologique et vasculaire du membre sont suivis.'+c('b01'),'L’évaluation est horaire chez les personnes à risque ou lorsque l’examen reste incomplet.'+c('b01'),'Une aggravation ou une suspicion persistante conduit à l’avis chirurgical et à la pression de loge.'+c('b01')],
['La kaliémie et l’ECG évaluent la complication électrique.'+c('k01'),'Après traitement d’une hyperkaliémie modérée ou sévère, les contrôles proposés sont au moinsà1,2,4,6et24heures.'+c('k03'),'La réponse insuffisante, le rebond ou la progression rapide déclenche une réévaluation urgente.'+c('k03','k04','s11')],
['La glycémie est suivie si le protocole d’hyperkaliémie utilise un transfert insulinique.'+c('k03'),'Le guide propose des contrôlesà0,30,60,90,120,180,240,300et360minutes après le traitement insulinoglucosé.'+c('k03'),'Une anomalie glycémique reçoit une prise en charge et le plan de surveillance est adapté.'+c('k03')],
['Les apports, les urines, le poids et les constantes guident la perfusion.'+c('s04'),'La réponse est réévaluée régulièrement et après adaptation des apports.'+c('s04'),'L’anurie persistante ou la surcharge fait revoir les apports et discuter l’épuration.'+c('s04')],
['Les électrolytes et l’équilibre acido-basique suivent la tolérance au NaCl.'+c('aips-n6'),'Les analyses sont périodiques ou adaptées à l’état clinique et au débit.'+c('aips-n6'),'Une réaction à la perfusion ou des signes de surdosage imposent son interruption immédiate.'+c('aips-n6','aips-n11')],
['La CK, la fonction et les symptômes suivent la récupération.'+c('e12','e16'),'La trajectoire est comparée au niveau de base et à la reprise fonctionnelle.'+c('e12','e16'),'Une hyperCKémie persistanteà8semaines ou des épisodes répétés ouvre le bilan de susceptibilité.'+c('e06','e14')]])
s+=h('11.D Le relais et la guérison se décident sur plusieurs critères')
s+=p('La récupération habituelle d’un épisode traité est favorable, mais les complications rénales sévères nécessitent un suivi de fonction à distance.','s10')
s+=p('Une fatigue, une douleur à l’effort ou des symptômes psychologiques persistants justifient également une prise en charge après la résolution biologique.','e11','e16')
s+=p('La décision de sortie ou de suivi hors hospitalisation réunit les éléments cliniques, biologiques et organisationnels suivants, adaptés au risque individuel.','e13','e16','s04')
s+=liste([
'La personne présente une stabilité clinique compatible avec le niveau de soins prévu et les signes rouges ont été réévalués.'+c('e13'),
'La complication électrique est contrôlée et le plan de surveillance du potassium tient compte du risque de rebond.'+c('k03','k04'),
'La diurèse, la fonction rénale et les apports sont compatibles avec le relais prévu, sans surcharge ou complication réfractaire en attente de traitement.'+c('s04','s09'),
'Une suspicion de loge aiguë a reçu sa décision spécialisée et les besoins de surveillance du membre sont précisés.'+c('b01'),
'La douleur, la force et la tendance des CK sont intégrées à l’évaluation de récupération plutôt qu’à une cible enzymatique isolée de perfusion.'+c('e12','s04','e16'),
'Le suivi des analyses et des symptômes, l’arrêt des facteurs réversibles et le contact en cas d’aggravation sont organisés.'+c('e15','e16','k04'),
'La recherche étiologique est programmée lorsque RHABDO, la faiblesse persistante ou les récidives la justifient.'+c('e06','e14')])
s+=p('Le retour progressif à l’activité est proposé au moins4semaines après résolution des symptômes dans les recommandations ENMC2025.','e15')
s+=p('La reprise tient compte du terrain, des complications, des contraintes de l’activité et du besoin éventuel de réhabilitation spécialisée.','e15','e16')
save(s)
