from rendu import outils

p,c,h,w,table,liste,save=outils(6)
a=w('Comparer le normal et le déficit volontaire',[
('L’évaluation volontaire de force nécessite une personne stable et capable de comprendre les consignes ; un trouble de coopération limite son interprétation.',['m01']),
('Le mouvement attendu est d’abord montré puis demandé activement ; la même fonction est comparée des deux côtés avant de changer de groupe musculaire.',['m01']),
('Un mouvement contre la pesanteur est recherché avant une résistance ; le protocole poursuit vers une résistance ou vers une pesanteur éliminée.',['m01']),
('La cotation MRC décrit0pour une contraction absente,1pour une contraction sans mouvement et2pour un mouvement avec pesanteur éliminée.',['m01']),
('La cotation3correspond au mouvement contre la pesanteur,4au mouvement contre résistance et5à une puissance normale.',['m01']),
('La cotation décrit une fonction ; elle ne détermine pas à elle seule si la faiblesse vient d’une rhabdomyolyse ou d’une autre affection.',['m01','d01'])])
b=w('Palpation et comparaison des régions musculaires',[
('L’inspection situe la tuméfaction et la répartition des muscles atteints ; l’histoire de l’effort guide la comparaison des régions sollicitées.',['r01','e02']),
('La palpation recherche une douleur à la pression du corps musculaire ; la DGN recommande de la distinguer d’un point gâchette myofascial.',['d01']),
('La pression est appliquée sur les muscles concernés et comparée aux autres régions ; la localisation et la réponse sont consignées.',['d01']),
('Un gonflement important associé à une douleur excessive fait rechercher une complication compartimentale plutôt que de conclure à une simple sensibilité postexercice.',['b01','r04']),
('L’examen clinique sert donc à cartographier la lésion et à rechercher sa gravité, sans remplacer la confirmation biologique.',['r08','b01'])])
d=w('Recherche d’une douleur à la mobilisation passive',[
('La mobilisation passive signifie que l’examinateur déplace le segment pendant que la personne laisse les muscles se relâcher.',['b01']),
('Le geste met en tension les muscles de la loge concernée ; la douleur provoquée complète la recherche d’une douleur disproportionnée.',['b01']),
('Le résultat est documenté avec l’état neurologique, l’état vasculaire, la conscience et l’heure de l’examen.',['b01']),
('Une conclusion incertaine est réévaluée avec le chirurgien sénior ; l’instrumentation éventuelle de pression complète l’examen.',['b01']),
('La répétition horaire concerne les personnes à risque ou dont l’examen est incomplet, selon les standards BOASt2025.',['b01'])])
e=w('Constantes, volémie et tolérance du remplissage',[
('L’évaluation recherche d’abord une stabilité clinique et une diurèse conservée, puis les anomalies des constantes et les signes de complication.',['e13','s04']),
('Le poids, les apports, les urines et le contexte cardiorespiratoire sont rapprochés de la réponse aux apports hydriques.',['s04']),
('Un état circulatoire insuffisant peut accompagner la séquestration liquidienne dans les muscles ; une surcharge peut au contraire résulter d’apports excessifs.',['r04','aips-n6']),
('La surveillance clinique et biologique suit ces deux risques ; l’anurie ou la surcharge impose une adaptation des apports.',['s04','aips-n6']),
('Une perfusion n’est donc pas poursuivie mécaniquement sur la seule persistance d’une CK élevée.',['s04'])])
s=h('Le normal précède la recherche d’atteinte régionale')
s+=p('Une fonction musculaire normale permet les mouvements demandés et une résistance adaptée, chez une personne stable qui comprend l’examen.','m01')
s+=p('L’examinateur distingue la plainte de douleur, l’impression de fatigue et la faiblesse motrice observée, car elles ne décrivent pas le même phénomène.','d01','r01')
s+=p('La démarche '+a+' rend le déficit reproductible ; une cotation seule ne suffit pas à expliquer son mécanisme.','m01','d01')
s+=p('La stabilité générale est appréciée avant les tests de force : une urgence circulatoire ou métabolique est traitée dans son circuit prioritaire.','e13','k04','m01')
s+=h('Les membres supérieurs et inférieurs sont examinés de façon comparable')
s+=p('Aux membres supérieurs, l’examen volontaire compare l’abduction des épaules, la flexion des coudes et l’extension des poignets.','m01')
s+=p('Pour l’épaule, la personne élève le coude ; pour le coude, elle rapproche la main de l’épaule selon le mouvement montré.','m01')
s+=p('Pour le poignet, elle relève la main ; la résistance est appliquée seulement après observation du mouvement actif contre la pesanteur.','m01')
s+=p('Aux membres inférieurs, l’examen compare la flexion des hanches, l’extension des genoux et la dorsiflexion des chevilles.','m01')
s+=p('La flexion de hanche rapproche le genou du thorax ; l’extension du genou et le relevé des orteils explorent ensuite les autres groupes.','m01')
s+=p('La position est adaptée pour rendre le mouvement contre la pesanteur ou avec pesanteur éliminée comparable entre les côtés.','m01')
s+=p('Le protocole standardisé utilise un dossier à45°pour les mouvements contre la pesanteur et à10°pour les mouvements avec pesanteur éliminée.','m01')
s+=p('Les limitations de position, de coopération ou de mouvement sont consignées ; une fonction impossible à explorer n’est pas présentée comme normale.','m01')
s+=h('Les muscles douloureux et les loges sont évalués séparément')
s+=p('La '+b+' localise la sensibilité et la tuméfaction ; l’examen recherche aussi les signes cutanés évocateurs d’une autre maladie musculaire.','d01','r01')
s+=p('Une douleur du corps musculaire correspond à une constatation différente d’une douleur très localisée sur un point gâchette.','d01')
s+=p('La '+d+' est prioritaire devant une douleur croissante ou excessive ; l’état vasculaire et neurologique est documenté simultanément.','b01')
s+=p('L’analyse porte sur l’ensemble des constatations et leur évolution ; une seule observation rassurante ne remplace pas le réexamen d’un membre à risque.','b01')
s+=p('Après libération d’un pansement circulaire chez une personne symptomatique, le standard prévoit une réévaluation dans les30minutes.','b01')
s+=h('L’examen général apprécie les conséquences et la réponse aux soins')
s+=p('La fenêtre '+e+' relie la clinique, les urines et les paramètres cardiorespiratoires à la décision d’apport hydrique.','s04')
s+=p('L’heure des examens est conservée afin de comparer les douleurs, les constatations du membre et l’évolution après les premières mesures.','b01')
s+=p('La surveillance ne s’arrête pas à la disparition des urines foncées, car la fonction rénale et les électrolytes nécessitent leur propre évaluation.','s02','s04')
s+=p('Une faiblesse ou des manifestations musculaires persistantes à distance orientent vers le bilan neuromusculaire et le suivi de récupération.','e14','e16')
save(s)

p,c,h,w,table,liste,save=outils(7)
a=w('Myalgie : symptôme recherché et limites',[
('La myalgie correspond à la douleur ressentie dans le muscle ; sa présence est recherchée par localisation et relation temporelle à l’effort.',['r01','e02']),
('La palpation du corps musculaire teste la sensibilité provoquée, tandis que l’interrogatoire décrit la douleur spontanée et le retentissement fonctionnel.',['d01']),
('La douleur sévère peut accompagner la destruction musculaire ; elle n’est cependant pas indispensable à toutes les présentations.',['r07','e12']),
('Une augmentation disproportionnée ou une douleur à l’étirement passif fait rechercher une loge aiguë et modifie immédiatement l’orientation.',['b01'])])
b=w('Faiblesse : signe fonctionnel et constat moteur',[
('La plainte de faiblesse décrit une difficulté à produire le mouvement attendu ; elle est vérifiée avec des gestes volontaires comparables.',['d01','m01']),
('La personne reproduit le mouvement montré, puis l’examinateur observe le mouvement contre la pesanteur et la résistance lorsque cela est possible.',['m01']),
('Une diminution reproductible distingue le constat moteur d’un simple récit de fatigue ; la coopération et les contraintes d’examen restent documentées.',['m01']),
('La destruction des fibres peut réduire la fonction, mais une faiblesse durable après la crise appelle l’étude d’une maladie sous-jacente.',['r01','e14'])])
d=w('Gonflement musculaire et menace compartimentale',[
('Le gonflement est une augmentation du volume musculaire, visible ou appréciée à l’examen comparatif des régions symptomatiques.',['r01','r04']),
('Il peut traduire un œdème consécutif à la lyse ; l’accumulation de liquide participe aussi à la réduction du volume circulant efficace.',['r04']),
('Une douleur disproportionnée ou déclenchée par l’étirement passif augmente la suspicion de pression dangereuse dans une loge.',['b01']),
('La surveillance répétée et la mesure de pression, selon l’incertitude clinique, précèdent la décision chirurgicale spécialisée.',['b01']),
('La décompression est immédiate lorsque le diagnostic est retenu ; la simple baisse de CK n’est pas un traitement local.',['b01','s03'])])
e=w('Pigmenturie et oligo-anurie : deux informations différentes',[
('La pigmenturie correspond à une coloration des urines par un pigment ; la myoglobine musculaire constitue une explication dans la rhabdomyolyse.',['r08']),
('Une bandelette positive pour le sang est confrontée au sédiment, car la bandelette ne distingue pas myoglobine et hémoglobine.',['r08']),
('L’oligurie désigne une diminution des urines, tandis que l’anurie correspond à leur cessation ; les quantités sont suivies avec le contexte clinique.',['s02','e13']),
('La couleur renseigne sur le pigment ; le volume et la créatinine renseignent sur une conséquence rénale qui peut devenir urgente.',['r08','s02','e13']),
('Des urines claires ne constituent donc pas un critère d’exclusion d’une atteinte musculaire ou d’une complication biologique.',['r07','s02'])])
f=w('Syndrome électrolytique : menace indépendante de la douleur',[
('Une libération musculaire de potassium peut modifier le risque électrique cardiaque avant une amélioration rénale suffisante.',['s11']),
('La recherche comprend une kaliémie, un électrocardiogramme et la surveillance de la tendance des valeurs.',['k01','k03']),
('Le monitorage continu est indiqué pour une kaliémie≥6,5mmol/L ou des signes électriques d’hyperkaliémie.',['k01']),
('Il est aussi recommandé entre6,0et6,4mmol/L si la personne est cliniquement malade ou si une augmentation rapide est attendue.',['k01']),
('Le traitement et l’orientation sont adaptés à cette menace, même si les manifestations musculaires sont peu marquées.',['k04','r07'])])
s=h('7.1 Un syndrome de lésion musculaire associe plusieurs constatations')
s+=p('La '+a+', la '+b+' et le '+d+' décrivent les manifestations locales possibles d’un épisode aigu.','r01','e12')
s+=p('Les signes fonctionnels correspondent aux douleurs et aux difficultés motrices rapportées ; les signes physiques viennent de l’examen de force et de la tuméfaction.','d01','m01','r01')
s+=p('La biologie complète cette description, car la présentation clinique peut être incomplète ou peu symptomatique dans certaines formes non traumatiques.','r07','r08')
s+=h('7.2 Un syndrome rénal ou pigmentaire recherche la conséquence systémique')
s+=p('La fenêtre '+e+' sépare le marqueur urinaire du pigment et la diminution de la fonction d’excrétion.','r08','s02')
s+=p('Le récit d’urines brunes constitue un signe fonctionnel ; la couleur observée, le sédiment et la diurèse mesurée sont des constatations complémentaires.','r08','s04')
s+=p('La créatinine et les électrolytes sont interprétés avec ces signes afin de décider du niveau de surveillance et d’une éventuelle épuration.','s02','s09')
s+=h('7.3 Un syndrome compartimental aigu menace le muscle lui-même')
s+=p('L’association d’un gonflement avec une douleur excessive ou provoquée passivement fait rechercher une ischémie locale par pression.','b01','r04')
s+=p('La douleur est décrite puis reproduite à la mobilisation passive ; la fonction neurologique et la perfusion sont consignées lors des examens successifs.','b01')
s+=p('Une évaluation clinique incomplète conserve la suspicion et mène à la discussion d’une mesure de pression avec le chirurgien.','b01')
s+=h('7.4 Un syndrome métabolique peut déterminer la priorité vitale')
s+=p('Le '+f+' relie les concentrations sanguines à leur retentissement cardiaque et à leur vitesse d’aggravation.','s11','k01')
s+=p('Le calcium et le phosphate complètent l’analyse, car les déplacements et les dépôts tissulaires changent selon la phase de récupération.','s08')
s+=table(['Syndrome','Signes fonctionnels recherchés','Signes physiques ou constatations mesurées'],[
['La lésion musculaire domine.','La personne rapporte douleur ou perte de fonction après l’effort.'+c('r01','e12'),'L’examen retrouve éventuellement une tuméfaction et une diminution de force.'+c('r01','m01')],
['Le retentissement rénal est suspecté.','La personne décrit une réduction des urines ou une coloration foncée.'+c('r08','s02'),'La diurèse, la créatinine et les électrolytes documentent la conséquence systémique.'+c('s02','s04')],
['Une loge aiguë est envisagée.','La douleur paraît excessive ou s’aggrave.'+c('b01'),'La mobilisation passive et l’évaluation répétée orientent la décision chirurgicale.'+c('b01')],
['Une complication électrolytique est détectée.','Les symptômes musculaires peuvent être incomplets malgré le risque biologique.'+c('r07','s11'),'Les dosages et l’électrocardiogramme déterminent le monitorage et le traitement urgent.'+c('k01','k04')]])
s+=p('Ces syndromes peuvent coexister ; la complication la plus menaçante fixe l’ordre des mesures sans attendre une présentation complète.','e13','s03')
save(s)
