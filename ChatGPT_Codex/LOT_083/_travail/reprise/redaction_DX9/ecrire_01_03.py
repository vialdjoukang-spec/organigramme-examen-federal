from rendu import outils

p,c,h,w,table,liste,save=outils(1)
a=w('Rhabdomyolyse d’effort : syndrome et cinétique',[
('Le consensus du 276e atelier ENMC, publié en2025, associe des symptômes musculaires sévères et une élévation aiguë de la créatine kinase.',['e01','e12']),
('Dans la forme d’effort, la créatine kinase dépasse 10000UI/L ; les symptômes comprennent gonflement, faiblesse ou douleur musculaire.',['e12']),
('Le pic survient environ1–4jours après le facteur déclenchant et les valeurs reviennent vers leur niveau de base après1–2semaines de repos.',['e12']),
('Cette cinétique décrit l’épisode ; une menace clinique ou métabolique déclenche les soins avant que son évolution complète soit connue.',['e13']),
('Chez une personne atteinte d’une maladie neuromusculaire, le consensus retient une élévation supérieure à5–10fois sa valeur de base.',['e01','e12'])])
b=w('CK élevée après sport : réponse biologique et maladie',[
('La créatine kinase est une enzyme musculaire dont la concentration peut augmenter après un travail musculaire important.',['d02']),
('Une élévation après exercice ne démontre donc pas à elle seule une atteinte rénale ni un épisode pathologique symptomatique.',['e02','e09']),
('Le consensus décrit499recrues en bonne santé ; certaines avaient des CK très élevées sans relation constante avec les symptômes.',['e02']),
('Le résultat est confronté à l’intensité inhabituelle de l’effort, aux manifestations cliniques, aux électrolytes et à la fonction rénale.',['e02','e13']),
('Une douleur sévère, une tuméfaction ou une réduction des urines fait sortir de la simple interprétation d’un chiffre postexercice.',['e13'])])
d=w('Myoglobinurie, pigmenturie et urines foncées',[
('La myoglobine est une protéine du muscle libérée lors de la destruction des fibres ; son passage urinaire peut colorer les urines.',['r02','r04']),
('Une pigmenturie désigne cette coloration ; l’aspect brun ne distingue pas à lui seul la myoglobine d’un autre pigment sanguin.',['r08']),
('Une bandelette positive pour le sang sans érythrocytes au sédiment oriente vers un pigment libre dans le contexte musculaire.',['r08']),
('La bandelette reconnaît aussi l’hémoglobine ; sa positivité doit donc être rapprochée de la microscopie et de l’histoire clinique.',['r08']),
('Les urines peuvent rester claires malgré la maladie ; la triade classique est inconstante dans les formes non traumatiques.',['r07'])])
s=h('Une destruction musculaire, puis un risque systémique')
s+=p('Le texte suisse du CHUV, publié dans la Revue médicale suisse le25novembre2020, définit la rhabdomyolyse comme les conséquences de la destruction musculaire striée.','r01')
s+=p('L’effort constitue un déclencheur fréquent, mais sa présence ne prouve pas qu’il explique seul l’ensemble de la destruction musculaire.','r06','e06')
s+=p('Le European Neuromuscular Centre (ENMC) précise en2025 le cadre de la '+a+', fondé sur la clinique et la variation des CK.','e01','e12')
s+=p('La créatine kinase (CK) renseigne sur l’atteinte musculaire ; la créatinine renseigne sur la fonction rénale dans le bilan des complications.','r08','e09')
s+=p('Ces marqueurs répondent à des questions différentes, car une importante libération enzymatique après sport peut survenir sans insuffisance rénale aiguë.','e09')
s+=h('Les mots décrivent des phénomènes différents')
s+=p('Une '+b+' appartient au diagnostic différentiel biologique ; elle ne devient pas automatiquement une indication de traitement intensif.','e02','e13')
s+=p('Une myalgie signifie une douleur musculaire ; une faiblesse décrit une diminution de capacité motrice, qui doit être recherchée à l’examen.','r01','d01')
s+=p('Un myo-œdème correspond au gonflement du muscle ; sa progression peut augmenter la pression dans une loge limitée par les fascias.','r04')
s+=p('La '+d+' suggère la libération de protéines musculaires ; son absence conserve cependant la nécessité du bilan en présence d’autres arguments.','r07','r08')
s+=p('Les courbatures et la rhabdomyolyse partagent le contexte d’exercice, mais une atteinte sévère ou systémique impose une autre conduite que le simple repos sportif.','e02','e13')
s+=h('Le nom de l’épisode ne clôt pas l’enquête')
s+=p('Une rhabdomyolyse peut compliquer une myopathie métabolique, une exposition toxique ou une maladie inflammatoire, même après un effort apparemment explicatif.','r06','e03','e04')
s+=p('La récidive, les épisodes après un effort habituel et les antécédents familiaux orientent vers une prédisposition à explorer après la prise en charge aiguë.','e06','e14')
s+=p('Le diagnostic désigne donc un épisode de destruction musculaire ; son étiologie et ses complications font l’objet de décisions distinctes.','r02','e16')
save(s)

p,c,h,w,table,liste,save=outils(2)
a=w('Cadre suisse : effort et causes associées',[
('La revue du CHUV présente l’effort, les causes traumatiques et les toxiques parmi les étiologies fréquentes de rhabdomyolyse chez l’adulte.',['r06']),
('Elle rapporte que deux étiologies coexistent dans plus de la moitié des cas de rhabdomyolyse de sa synthèse.',['r06']),
('Ce constat motive la recherche de médicaments, alcool, chaleur et autres facteurs plutôt qu’une attribution automatique à la séance sportive.',['r06','e06']),
('La mortalité inférieure à2% citée pour la rhabdomyolyse d’effort appartient à cette revue de2020 ; elle ne définit pas un risque individuel.',['r03'])])
b=w('Effort inhabituel et population exposée',[
('Le consensus européen souligne les reprises d’exercice intense après une interruption et les entraînements inhabituels chez des personnes auparavant en bonne santé.',['e02']),
('Une bonne condition physique ne supprime pas le risque lorsque l’intensité, les contractions ou les conditions environnementales changent brutalement.',['e16','e15']),
('La pression exercée par un groupe ou un entraîneur peut conduire à dépasser les limites habituelles de l’entraînement.',['e02']),
('La prévention doit donc considérer le programme collectif et la possibilité de signaler des symptômes, autant que les caractéristiques individuelles.',['e02','e15'])])
d=w('Séquelles : cohorte néerlandaise, périmètre exact',[
('Le rapport ENMC présente une étude néerlandaise portant sur des sportifs et des militaires ayant subi une rhabdomyolyse ou un coup de chaleur d’effort.',['e11']),
('Les événements étudiés se situent entre2010et2020 ; les symptômes sont évalués à6et12mois après l’épisode.',['e11']),
('Les pourcentages de fatigue, douleur et manifestations psychologiques décrivent cette population mixte, et non toutes les rhabdomyolyses d’effort.',['e11']),
('Leur intérêt clinique est de programmer un suivi de récupération et de fonction, même lorsque l’urgence biologique est résolue.',['e11','e16'])])
s=h('La référence suisse situe le problème clinique')
s+=p('La revue suisse du CHUV de2020 décrit la rhabdomyolyse d’effort parmi les causes usuelles de destruction musculaire aiguë chez l’adulte.','r06')
s+=p('Son '+a+' associe la reconnaissance de l’effort à la recherche de cofacteurs, car plusieurs mécanismes peuvent contribuer au même épisode.','r06')
s+=p('La mortalité liée à l’effort est décrite comme faible dans cette synthèse ; le pronostic dépend toutefois des complications rénales et électrolytiques.','r03','r01')
s+=p('Les données de réanimation concernent une population différente, car le choc, le sepsis, les traumatismes et les défaillances associées aggravent le risque.','s10')
s+=h('Les synthèses européennes décrivent des groupes et des expositions')
s+=p('Le '+b+' explique pourquoi un épisode peut survenir lors d’une reprise ou d’un entraînement collectif, sans maladie musculaire préalablement connue.','e02','e16')
s+=p('La synthèse de772patients citée par ENMC retrouve surtout des hommes jeunes, avec la course et l’haltérophilie comme activités fréquemment représentées.','e02')
s+=p('Ces séries sélectionnent des personnes atteintes ; elles ne mesurent pas la probabilité de maladie chez toute personne qui court ou soulève des charges.','e02')
s+=table(['Observation chiffrée','Population et période','Portée clinique'],[
['La revue rapporte une mortalité inférieure à2%.','Elle concerne la rhabdomyolyse d’effort dans la synthèse suisse publiée en2020.'+c('r03'),'Ce chiffre décrit un ensemble et ne rassure pas face à une complication aiguë.'+c('r01','e13')],
['La course représente54% et l’haltérophilie15% des activités rapportées.','Ces proportions proviennent d’une revue de772patients citée par ENMC2025.'+c('e02'),'Le dénominateur est constitué de cas publiés, pas des participants à ces sports.'+c('e02')],
['Les symptômes musculaires touchent26% au repos et28% pendant l’exercice.','Ces données concernent la cohorte néerlandaise mixte2010–2020, évaluée à6et12mois.'+c('e11'),'La récupération fonctionnelle mérite une évaluation après la phase aiguë.'+c('e11')],
['Une fatigue sévère est rapportée chez30% et des troubles de l’humeur ou anxieux chez11%.','Les résultats viennent de la même population mixte de rhabdomyolyse ou de coup de chaleur.'+c('e11'),'Le suivi associe symptômes physiques et retentissement psychologique.'+c('e11','e16')]])
s+=h('L’histoire naturelle dépend de la gravité et du terrain')
s+=p('La CK augmente puis décroît après l’arrêt du facteur déclenchant ; le consensus européen décrit un retour au niveau de base après repos.','e12')
s+=p('Une hyperCKémie durable, des douleurs persistantes ou une nouvelle crise déplacent l’évaluation vers une cause musculaire sous-jacente.','e06','e14')
s+=p('La '+d+' montre également que les symptômes tardifs ne se réduisent pas à une anomalie de laboratoire.','e11')
s+=p('Après une atteinte rénale sévère, la fonction rénale est suivie à distance, car une récupération incomplète peut persister au-delà de l’hospitalisation.','s10')
s+=p('La prévention de santé publique porte sur la progressivité des charges, l’exposition à la chaleur et la reconnaissance précoce des symptômes préoccupants.','e15')
s+=p('Le retour au sport et au travail physique se prépare avec l’équipe, car leurs contraintes peuvent reproduire les facteurs de l’épisode initial.','e15','e16')
save(s)

p,c,h,w,table,liste,save=outils(3)
a=w('De la demande énergétique à la lyse de la fibre',[
('L’adénosine triphosphate, ou ATP, fournit l’énergie nécessaire au fonctionnement des pompes ioniques du muscle.',['r04','s01']),
('Un effort intense peut épuiser les ressources énergétiques ; les gradients membranaires deviennent alors difficiles à maintenir.',['s01']),
('Le sodium et le calcium intracellulaires augmentent ; le calcium entretient la contraction et active des enzymes qui dégradent les structures cellulaires.',['s01']),
('Les phospholipases et les protéases participent aux lésions membranaires ; le contenu de la fibre passe alors dans la circulation.',['s01']),
('La recherche de CK, de potassium et de troubles de la fonction rénale explore donc des conséquences différentes du même événement musculaire.',['r04','s02'])])
b=w('Œdème musculaire, hypovolémie et loge fermée',[
('L’inflammation locale et les lésions musculaires provoquent une accumulation liquidienne dans le muscle lésé.',['r04','s01']),
('Une partie du liquide est ainsi soustraite à la circulation efficace ; une hypovolémie peut apparaître lorsque plusieurs groupes musculaires sont atteints.',['r04']),
('Dans un espace limité par les fascias, l’augmentation de volume accroît la pression et peut compromettre la perfusion tissulaire.',['r04','b01']),
('La douleur disproportionnée et sa majoration à l’étirement passif orientent vers cette complication ; la confirmation impose une décompression chirurgicale immédiate.',['b01']),
('La correction d’un déficit circulatoire ne remplace donc pas le traitement d’une loge devenue ischémique.',['s03','b01'])])
d=w('Myoglobine et agression rénale',[
('La libération de myoglobine expose le rein à une charge pigmentaire qui peut participer à des lésions tubulaires.',['r04','s01']),
('Sa précipitation avec les protéines tubulaires favorise l’obstruction ; l’urine concentrée et acide accentue ce mécanisme.',['r04','s01']),
('Les produits de dégradation de l’hème induisent un stress oxydatif qui altère les cellules tubulaires.',['s01']),
('La vasoconstriction et l’hypovolémie réduisent simultanément la perfusion rénale, ce qui associe plusieurs mécanismes d’insuffisance rénale aiguë.',['r04','s01']),
('Le traitement restaure une perfusion adaptée et corrige les complications ; la plausibilité d’un mécanisme ne suffit pas à justifier une alcalinisation systématique.',['s03','s06','e10'])])
e=w('Potassium, phosphate et calcium : phases différentes',[
('Le potassium et le phosphate quittent les cellules musculaires détruites ; leur accumulation est aggravée si le rein les élimine moins bien.',['r04','s02']),
('L’hyperkaliémie peut survenir tôt et menacer le rythme cardiaque ; sa cinétique impose une surveillance rapprochée.',['s11']),
('L’hypocalcémie initiale est liée notamment aux dépôts phosphocalciques ; sa correction systématique peut favoriser des dépôts tissulaires.',['r04','s08']),
('Le calcium peut remonter lors de la récupération, en particulier après une supplémentation excessive pendant la phase initiale.',['s08']),
('L’interprétation des électrolytes conserve donc la chronologie de la maladie au lieu d’appliquer une correction identique à chaque phase.',['s08','s11'])])
s=h('Une perte d’intégrité musculaire entraîne plusieurs voies de complication')
s+=p('Le muscle normal adapte sa production énergétique à l’activité ; une demande excessive ou une prédisposition métabolique peut dépasser cette adaptation.','e03','e04','s01')
s+=p('La chaîne '+a+' relie l’effort aux perturbations ioniques, puis aux manifestations locales et aux marqueurs biologiques.','r04','s01')
s+=p('L’élévation de CK marque la libération cellulaire ; cette enzyme ne représente pas directement la quantité de myoglobine encore présente dans la circulation.','r08','e09')
s+=p('Le risque rénal résulte de la charge pigmentaire et du contexte hémodynamique ; il ne dépend donc pas d’une valeur unique de CK.','e09','s04')
s+=p('L’'+b+' explique l’association possible d’une tuméfaction importante avec une hypovolémie et une menace locale.','r04','b01')
s+=h('Chaque mécanisme oriente un examen et une décision')
s+=table(['Perturbation','Exploration correspondante','Conduite et mécanisme recherché'],[
['Le déficit énergétique dérègle les pompes et favorise la destruction des fibres.'+c('s01'),'Les CK répétées et les symptômes documentent la lésion et sa cinétique.'+c('e12'),'L’effort est interrompu et le facteur déclenchant est écarté pour stopper l’agression.'+c('s03','e15')],
['Le liquide se séquestre dans les muscles lésés.'+c('r04'),'Les constantes, la volémie, le poids et la diurèse évaluent son retentissement.'+c('s04'),'Le déficit circulatoire est corrigé avec des apports réévalués selon la réponse.'+c('s04')],
['La myoglobine contribue à l’obstruction et à la toxicité tubulaires.'+c('s01'),'La créatinine, la diurèse et les urines recherchent une atteinte rénale.'+c('r08','s02'),'La perfusion rénale est préservée ; une complication réfractaire conduit à discuter l’épuration.'+c('s03','s09')],
['La lyse libère du potassium et du phosphate.'+c('r04'),'Le bilan électrolytique, l’électrocardiogramme et les contrôles répétés évaluent la menace.'+c('s02','k01'),'La complication métabolique est traitée sous monitorage, avec avis spécialisé urgent si elle menace le pronostic.'+c('s11','k04')],
['Le calcium peut être bas au début puis augmenter à la récupération.'+c('s08'),'Le calcium et les symptômes sont suivis en tenant compte de la phase clinique.'+c('s08'),'Une hypocalcémie asymptomatique ne déclenche pas de supplémentation automatique.'+c('s08')],
['La pression intracompartimentale peut compromettre la perfusion.'+c('b01'),'La douleur, l’étirement passif et, si nécessaire, la pression de loge sont évalués.'+c('b01'),'Une loge confirmée nécessite une décompression immédiate de tous les compartiments impliqués.'+c('b01')]])
s+=p('La '+d+' justifie une surveillance rénale même lorsque les manifestations musculaires semblent s’améliorer.','s01','s02')
s+=p('Les '+e+' expliquent pourquoi le traitement vise la sécurité métabolique et la fonction, plutôt qu’une normalisation simultanée de tous les chiffres.','s08','s11')
s+=h('La prédisposition modifie le seuil de tolérance à l’effort')
s+=p('Les glycogénoses limitent l’utilisation des glucides musculaires ; des symptômes précoces à l’effort et un second souffle peuvent orienter leur recherche.','e03','d01')
s+=p('Les défauts d’oxydation des acides gras exposent plutôt lors d’efforts prolongés, du jeûne ou d’une maladie fébrile.','e04')
s+=p('Les anomalies du couplage excitation-contraction, notamment liées à RYR1, peuvent rendre le muscle sensible à la chaleur et à d’autres déclencheurs.','e05')
s+=p('L’existence d’un effort récent n’écarte donc pas une maladie sous-jacente lorsque l’intensité de cet effort explique mal la crise.','e06')
s+=p('L’enquête spécialisée recherche cette interaction entre constitution et environnement après avoir traité les conséquences aiguës de la lyse musculaire.','e14','e16')
save(s)
