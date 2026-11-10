from rendu import outils

p,c,h,w,table,liste,save=outils(4)
a=w('Complication rénale ou électrique : priorité au patient',[
('La rhabdomyolyse peut provoquer une insuffisance rénale aiguë et une libération rapide de potassium ; ces complications peuvent menacer la vie.',['r01','s11']),
('Une diminution des urines, des constantes anormales ou une anomalie électrolytique impose une évaluation urgente, indépendamment du niveau initial de CK.',['e13','e09']),
('La kaliémie et la créatinine sont mesurées, tandis que l’électrocardiogramme recherche le retentissement électrique.',['s02','k01']),
('Une hyperkaliémie sévère ou rapidement évolutive déclenche un monitorage continu et un avis rénal ou de réanimation urgent.',['k01','k04']),
('Le rang E1 du LOT s’applique à ces formes compliquées ; il ne transforme pas chaque élévation enzymatique sportive en défaillance vitale.',['e13','e09'])])
b=w('Syndrome des loges aigu : douleur et étirement passif',[
('Une loge est un espace musculaire limité par les fascias ; la pression peut y augmenter jusqu’à compromettre la perfusion.',['b01']),
('La recherche porte sur une douleur disproportionnée et sur la douleur provoquée par la mobilisation passive des muscles concernés.',['b01']),
('Le mouvement passif est réalisé par l’examinateur, sans contraction volontaire du muscle exploré ; sa douleur est documentée avec les autres constatations.',['b01']),
('Une évaluation incomplète ou des signes équivoques justifient un avis chirurgical sénior, des examens répétés et une mesure de pression si nécessaire.',['b01']),
('Le diagnostic confirmé impose une décompression immédiate ; le bilan musculaire ou rénal ne doit pas retarder cette action.',['b01','s03'])])
d=w('Épisode inhabituel : effort déclencheur ou révélateur',[
('Une crise après un effort habituel, plusieurs crises ou une hyperCKémie durable évoquent une prédisposition neuromusculaire.',['e06']),
('Le second souffle décrit une amélioration après un début d’exercice difficile ou une courte pause ; il oriente vers certaines glycogénoses.',['d01','e03']),
('Des crises après un effort prolongé, un jeûne ou une maladie fébrile orientent vers des anomalies d’oxydation des acides gras.',['e04']),
('L’enquête réunit l’histoire, la biologie et la génétique ; une variante isolée n’est interprétée qu’en relation avec le phénotype.',['e03','e14']),
('Cette orientation se prépare après stabilisation ; elle ne remplace pas la prévention immédiate des complications rénales et métaboliques.',['e16','s03'])])
s=h('Les menaces changent le lieu et l’ordre des soins')
s+=p('La priorité porte sur la '+a+' : 🚩 E1 si une atteinte rénale sévère ou une perturbation électrolytique menace le pronostic vital.','r01','e13')
s+=p('Une anurie, une dégradation circulatoire ou une kaliémie menaçante nécessite un circuit hospitalier adapté, sans attendre la réunion de la triade musculaire classique.','e13','k04','r07')
s+=p('Le '+b+' représente une autre urgence : 🚩 E2 si une complication compartimentale est suspectée, avec chirurgie immédiate après diagnostic.','b01')
s+=p('Une anomalie des constantes dans un contexte de chaleur impose également une évaluation urgente des complications ; le seul diagnostic musculaire reste insuffisant.','e13','e15')
s+=p('La présence de symptômes sévères conserve cette priorité même si le prélèvement est précoce et que les CK n’ont pas atteint leur pic.','e12','e13')
s+=h('Les principaux concurrents sont distingués par leur contexte et leur évolution')
s+=table(['Hypothèse','Élément discriminant','Piège','Conduite si les arguments sont présents'],[
['Une réponse postexercice ou des courbatures accompagne l’entraînement.','Les symptômes restent limités et le bilan ne montre pas de retentissement systémique.'+c('e02','e13'),'Une CK isolée élevée ne prouve pas une rhabdomyolyse compliquée ; des urines claires ne l’excluent pas non plus.'+c('e02','r07'),'Le repos et une réévaluation adaptée sont organisés ; toute anomalie systémique ouvre la branche urgente.'+c('e13','e15')],
['Une myosite inflammatoire provoque une atteinte musculaire.','Une faiblesse persistante, des signes cutanés évocateurs ou un contexte auto-immun orientent les anticorps et le bilan spécialisé.'+c('d01','d03','e08'),'Un effort récent peut coexister ; il ne suffit pas à expliquer une faiblesse progressive ou durable.'+c('e14','e08'),'Le neurologue ou le spécialiste musculaire discute les anticorps et une biopsie selon la suspicion.'+c('e08','d03')],
['Une myopathie métabolique prédispose aux épisodes.','La récidive, le second souffle, le jeûne ou les antécédents familiaux orientent le phénotypage.'+c('d01','e03','e04','e06'),'Une activité habituelle peut devenir le déclencheur révélateur ; la condition physique n’écarte pas la prédisposition.'+c('e06','e16'),'Une consultation neuromusculaire organise biologie métabolique et analyse génétique après stabilisation.'+c('e03','e04','e14')],
['Une cause toxique ou médicamenteuse contribue à la lyse.','L’histoire recherche une exposition et les autres facteurs capables d’expliquer l’épisode.'+c('r06','e06'),'Une exposition et un effort peuvent agir ensemble ; la chronologie seule ne démontre pas une cause unique.'+c('r06','e06'),'Le facteur réversible est écarté avec l’équipe, puis la sévérité et la récupération sont réévaluées.'+c('s03','e14')]])
s+=p('La fenêtre '+d+' précise les éléments qui rendent l’enquête étiologique nécessaire malgré un contexte sportif vraisemblable.','e06','e14')
s+=p('L’imagerie musculaire peut localiser une anomalie, mais son signal ne distingue pas régulièrement à lui seul les différentes maladies musculaires.','d04')
s+=p('Une suspicion compartimentale se traite dans son circuit chirurgical ; une suspicion inflammatoire ou génétique relève d’un autre bilan spécialisé.','b01','e08','e14')
s+=p('L’absence d’urines brunes ou de douleur diffuse ne clôt jamais la démarche lorsque les autres signes suggèrent une destruction musculaire ou une complication.','r07','e13')
save(s)

p,c,h,w,table,liste,save=outils(5)
a=w('Chronologie exacte de l’effort et des symptômes',[
('L’histoire précise l’heure de l’effort, sa durée, son caractère habituel ou nouveau et le délai avant les premières manifestations.',['e02','e12']),
('La douleur, le gonflement et la faiblesse sont situés par rapport aux groupes musculaires réellement sollicités.',['r01','e02']),
('Le pic de CK survient après le déclenchement ; une analyse très précoce ne remplace donc pas la surveillance de l’évolution.',['e12']),
('La reprise après une interruption et les séances inhabituelles constituent des circonstances fréquentes dans les descriptions européennes.',['e02']),
('Une crise après une charge ordinaire conduit à rechercher une explication supplémentaire plutôt qu’à attribuer tout épisode à un excès d’entraînement.',['e06'])])
b=w('Urines, apports et facteurs de vulnérabilité rénale',[
('L’interrogatoire demande la fréquence et la quantité des urines ainsi que l’apparition d’une coloration inhabituelle.',['r08','e13']),
('La diminution de diurèse renseigne sur une complication possible ; elle est rapprochée des apports, des pertes et de l’état circulatoire.',['r04','s04']),
('Les vomissements et la baisse des apports peuvent compliquer la possibilité d’un traitement oral et la restauration d’une volémie adaptée.',['r07','s04']),
('Les maladies rénales, cardiaques et les autres comorbidités modifient la prudence nécessaire lors de la surveillance et du remplissage.',['e13','s04']),
('Les apports et les sorties sont suivis ensemble afin de reconnaître aussi une surcharge provoquée par le traitement.',['s04','aips-n6'])])
d=w('Questions RHABDO : identifier une susceptibilité',[
('R recherche des épisodes récurrents de rhabdomyolyse d’effort ; une nouvelle crise augmente l’intérêt d’une évaluation spécialisée.',['e06']),
('H recherche une hyperCKémie persistante8semaines après l’événement, en tenant compte de la valeur habituelle connue.',['e06']),
('A recherche une crise après un exercice habituel dont l’intensité n’explique pas la sévérité de la lyse.',['e06']),
('B retient une élévation sanguine des CK supérieure à50fois la limite supérieure normale comme élément d’orientation génétique.',['e06']),
('D demande si les médicaments, suppléments ou autres facteurs expliquent suffisamment la sévérité ; O recherche les proches atteints et les symptômes d’effort.',['e06']),
('La présence d’une caractéristique RHABDO motive la discussion génétique ; elle ne constitue pas à elle seule un diagnostic moléculaire.',['e06','e14'])])
s=h('Les questions reconstituent le mécanisme et la gravité')
s+=p('La '+a+' distingue une séance réellement inhabituelle d’un effort ordinaire qui révèle une susceptibilité musculaire.','e02','e06')
s+=p('Le programme est décrit concrètement : reprise récente, exercice excentrique, nouvelle intensité et pression éventuelle du groupe ou de l’encadrement.','e02','e15')
s+=p('La chaleur, l’humidité et une infection récente sont recherchées, car ces facteurs peuvent réduire la tolérance à l’exercice.','e15')
s+=p('L’histoire précise aussi l’alcool, les substances, les médicaments et les compléments ; plusieurs déclencheurs peuvent contribuer au même événement.','r06','e06')
s+=p('La liste réelle des produits est reconstruite avec le patient et l’entourage ; les facteurs réversibles sont ensuite discutés avec l’équipe soignante.','e06','s03')
s+=p('Les '+b+' déterminent la possibilité d’une surveillance sûre et la tolérance attendue des apports hydriques.','s04','e13')
s+=h('Les drapeaux rouges indiquent une action')
s+=table(['Constat recherché','Signification','Action immédiate'],[
['La quantité des urines diminue fortement ou les urines cessent.','Une complication rénale peut évoluer malgré la stabilisation apparente de la douleur.'+c('e13','s02'),'Le bilan rénal et électrolytique est urgent ; l’orientation hospitalière et l’avis spécialisé sont organisés.'+c('e13','s09')],
['Les urines deviennent foncées après l’effort.','Une pigmenturie peut accompagner la libération de myoglobine.'+c('r08'),'Les CK, la créatinine, les électrolytes et le sédiment urinaire sont contrôlés.'+c('r08','s02')],
['La douleur locale devient disproportionnée ou augmente à l’étirement passif.','La pression intracompartimentale peut menacer la perfusion du muscle.'+c('b01'),'Le chirurgien est alerté ; la réévaluation et la pression de loge sont discutées sans attendre une CK supplémentaire.'+c('b01')],
['Les constantes sont anormales ou la situation clinique se dégrade.','Une forme systémique ou une autre affection associée doit être identifiée.'+c('e13'),'La stabilisation, le bilan urgent et le niveau de surveillance sont déterminés à l’hôpital.'+c('e13','k04')],
['Une hyperkaliémie est sévère ou sa progression paraît rapide.','La libération musculaire et l’insuffisance rénale peuvent compromettre le rythme cardiaque.'+c('s11'),'Un électrocardiogramme et un monitorage continu sont réalisés selon les critères de risque, avec avis urgent.'+c('k01','k04')],
['Une réaction apparaît pendant la perfusion.','Une hypersensibilité ou une réaction à la perfusion est possible.'+c('aips-n6'),'La perfusion est immédiatement interrompue et une prise en charge clinique appropriée débute.'+c('aips-n6')]])
s+=h('Le terrain et les antécédents rendent l’épisode intelligible')
s+=p('Les '+d+' recherchent les indices d’une cause métabolique, génétique ou neuromusculaire sans attendre plusieurs épisodes identiques.','e06','e14')
s+=p('Des crampes précoces avec second souffle orientent vers une glycogénose ; des crises après jeûne ou effort prolongé orientent vers une anomalie lipidique.','d01','e03','e04')
s+=p('Les antécédents familiaux de symptômes musculaires ou de réactions anesthésiques sont transmis au spécialiste, notamment lorsque RYR1 est envisagé.','e05')
s+=p('Une faiblesse persistante, des manifestations cutanées ou d’autres signes généraux font rechercher une maladie inflammatoire au-delà de l’épisode aigu.','d01','d03','e08')
s+=p('Les contraintes de domicile, de déplacement, de travail et d’entraînement sont précisées, car la surveillance et la reprise nécessitent un relais réellement réalisable.','e15','e16')
s+=p('La discussion inclut le retentissement psychologique et les attentes de récupération ; des symptômes tardifs sont décrits après les épisodes d’effort.','e11')
save(s)
