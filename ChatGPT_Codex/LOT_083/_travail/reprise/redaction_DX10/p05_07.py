def rediger(c):
 c.block(5,'L’entretien distingue la chronologie musculaire des manifestations d’organes',[
 ('Le patient décrit le début de la faiblesse et les tâches devenues difficiles, notamment les escaliers, le lever du siège et les activités des bras.','pnds-anamnese+pnds-examen'),
 ('Une installation en semaines ou en mois oriente vers une myopathie acquise, tandis que les antécédents familiaux et développementaux éclairent d’autres causes.','pnds-anamnese'),
 ('Les lésions cutanées sont recherchées dans l’histoire même si elles semblent discrètes le jour de l’examen.','pnds-examen+fr-definition'),
 ('La date des symptômes cutanés et celle des difficultés musculaires sont distinguées, puisque les phénotypes ne sont pas uniformes.','fr-definition'),
 ('L’entretien demande aussi les médicaments, les toxiques et les infections récentes avant de retenir une cause auto-immune.','pnds-anamnese'),
 ('La prise de statines, de corticoïdes et d’autres médicaments myotoxiques guide ainsi le diagnostic différentiel et la discussion spécialisée.','pnds-anamnese+rms-clin'),
 ('Les symptômes respiratoires, de déglutition et cardiaques sont recherchés directement, car ils modifient la gravité et la filière de soins.','pnds-examen+bsr-x+bsr-xi')])
 c.tab(5,'Questions ciblées : raison et conséquence',['Question posée','Pourquoi la question est utile','Conséquence si le symptôme est présent'],[
  [('Avez-vous besoin des bras pour quitter une chaise ?','pnds-examen'),('La manœuvre sollicite les muscles proximaux de la ceinture pelvienne.','pnds-examen'),('Le déficit est recherché et objectivé lors du testing.','pnds-examen+pnds-mmt')],
  [('Les aliments déclenchent-ils une toux ou une impression de fausse route ?','pnds-examen'),('La déglutition peut être atteinte et exposer à une inhalation.','bsr-xi'),('Une évaluation de sécurité et un avis spécialisé de déglutition sont organisés.','bsr-xi+pnds-severite')],
  [('Votre voix est-elle devenue différente ou nasonnée ?','pnds-examen'),('La modification peut accompagner une participation pharyngée.','pnds-examen'),('L’examen bulbaire et les autres symptômes de déglutition sont approfondis.','pnds-examen+bsr-xi')],
  [('Avez-vous une gêne respiratoire, y compris dans certaines positions ?','pnds-examen'),('Une atteinte musculaire respiratoire ou pulmonaire peut accompagner la maladie.','pnds-examen+ers-depistage'),('La sévérité clinique et le bilan respiratoire sont évalués sans attendre le panel d’anticorps.','pnds-severite+ers-depistage')],
  [('Ressentez-vous des palpitations ou une douleur évoquant une atteinte cardiaque ?','pnds-examen'),('La participation myocardique constitue une complication à identifier.','bsr-x'),('L’évaluation cardiaque associe la clinique et les explorations adaptées.','bsr-x')],
  [('Une éruption concerne-t-elle les paupières, les doigts ou le décolleté ?','cedef-heliotrope+cedef-gottron+cedef-tronc'),('La distribution cutanée peut orienter vers la dermatomyosite.','pnds-examen'),('Les zones sont inspectées et la constellation est documentée.','pnds-examen')],
  [('Avez-vous perdu du poids ou une maladie tumorale a-t-elle été évoquée ?','bsr-xi+imacs-screen'),('Une perte pondérale peut accompagner une dysphagie et le contexte tumoral demande aussi une exploration.','bsr-xi+imacs-screen'),('La déglutition, la nutrition et la stratification du risque de cancer sont examinées.','bsr-xi+imacs-risk')],
  [('Quels traitements et quelles activités précédaient la faiblesse ?','pnds-anamnese'),('Les causes médicamenteuses et les autres contextes musculaires doivent être considérés.','rms-clin+pnds-anamnese'),('Le traitement antérieur est confronté au bilan clinique avant une décision d’immunosuppression.','rms-clin+rms-conclusion')]
 ])
 c.fen(5,'Drapeaux rouges : le signe ouvre une action',[
 ('Une détresse respiratoire ou une faiblesse respiratoire importante conduit à une prise en charge urgente et à une évaluation des organes.','pnds-severite+pnds-examen'),
 ('Une dysphagie importante avec fausses routes fait apprécier immédiatement la sécurité de l’alimentation et le besoin de soins hospitaliers.','pnds-severite+bsr-xi'),
 ('Une suspicion de myocardite ou des signes cardiaques préoccupants nécessitent une évaluation cardiaque urgente selon l’état clinique.','pnds-severite+bsr-x'),
 ('Une faiblesse très sévère avec confinement au lit figure aussi parmi les situations de gravité du protocole français.','pnds-severite'),
 ('Des ulcérations cutanées sévères demandent une évaluation spécialisée et renforcent certains risques systémiques ou tumoraux.','pnds-severite+imacs-risk'),
 ('L’apparition d’une infection sous immunosuppresseur change la conduite et justifie un contact médical rapide.','im-warn+pnds-hospitalisation'),
 ('Ces signaux ne signifient pas que tous les patients présentant un érythème de Gottron doivent être traités comme une urgence vitale.','pnds-severite+pnds-hospitalisation')])
 c.block(5,'Le terrain prépare une prescription et un suivi sûrs',[
 ('La discussion porte sur un projet de grossesse et sur les médicaments déjà pris, car les notices des immunothérapies imposent des précautions différentes.','sp-gross+im-gross+oc-gross'),
 ('Les antécédents infectieux et les traitements associés orientent également les investigations réalisées avant une immunosuppression.','rms-bilan+im-warn'),
 ('Les fonctions rénale et hépatique sont prises en compte avant de choisir et de surveiller l’azathioprine ou les immunoglobulines.','im-dose+im-warn+oc-warn'),
 ('La capacité à se déplacer, à s’habiller et à travailler complète l’évaluation de la force afin de fixer des objectifs de réadaptation.','bsr-xii+ai-reintegration'),
 ('Chez l’enfant, la croissance, les étapes du développement et la scolarité sont intégrées au parcours spécialisé.','pnds-anamnese+pnds-objectif')])

 c.block(6,'Le comparateur normal précède la recherche d’une faiblesse',[
 ('La référence du testing est la force maximale attendue pour le muscle examiné, selon l’échelle du Medical Research Council.','mrc-echelle'),
 ('Le grade 5 correspond à une force normale ; le grade 3 correspond à un mouvement contre la gravité.','mrc-test'),
 ('Le grade 4 décrit un mouvement contre une résistance modérée, ce qui demande de distinguer résistance appliquée et simple déplacement du segment.','mrc-test'),
 ('L’examinateur explique le mouvement, peut le montrer passivement, puis demande sa réalisation active avant d’interpréter la réponse.','mrc-test'),
 ('Les deux côtés d’un même groupe musculaire sont examinés avant de passer au groupe suivant afin de rendre la comparaison cohérente.','mrc-test'),
 ('La capacité à participer et les limitations de l’examen sont prises en compte ; un groupe non testable ne reçoit pas une force normale supposée.','mrc-test'),
 ('La cotation d’un muscle ne doit pas être confondue avec une somme de groupes ou un score de myosite complet.','mrc-echelle+pnds-mmt')])
 c.fen(6,'Geste de testing : ce qui est demandé et ce qui est observé',[
 ('Pour l’abduction de l’épaule, le patient reçoit une consigne de déplacement du coude vers le haut.','mrc-test'),
 ('Le mouvement actif est observé, puis la capacité à lutter contre la gravité et la résistance est appréciée selon la cotation.','mrc-test'),
 ('Pour la flexion du coude, la consigne rapproche la main de l’épaule, en examinant les deux côtés du même groupe.','mrc-test'),
 ('Pour la flexion de hanche, le patient rapproche le genou du thorax ; cette tâche explore un groupe proximal utile dans le tableau myogène.','mrc-test+pnds-mmt'),
 ('L’extension du genou et la dorsiflexion de cheville complètent la description de la distribution plutôt que de présumer une atteinte purement proximale.','mrc-test+rms-clin'),
 ('Le résultat est décrit avec le geste réellement possible et ses limitations, afin que l’examen suivant puisse être comparé.','mrc-test+bsr-i')])
 c.block(6,'La région pelvienne est évaluée par la force et la fonction',[
 ('Le tableau habituel comporte une faiblesse bilatérale et proximale des ceintures ; la distribution exacte reste à vérifier chez chaque patient.','pnds-examen'),
 ('Le lever d’une chaise est observé en demandant au patient de se redresser sans l’aide des bras lorsque la tâche est réalisable.','pnds-examen'),
 ('Une difficulté dans ce geste correspond au signe du tabouret décrit dans le protocole, puis le testing précise les groupes concernés.','pnds-examen+pnds-mmt'),
 ('Le relevé du sol et les difficultés à monter une marche renseignent également sur le retentissement du déficit proximal.','pnds-examen'),
 ('Le patient qui ne peut pas réaliser une tâche n’est pas décrit uniquement par une douleur ; la force et la sécurité fonctionnelle sont évaluées séparément.','rms-clin+pnds-examen'),
 ('L’inspection recherche une éventuelle amyotrophie et la palpation peut retrouver une douleur des masses musculaires.','pnds-examen')])
 c.block(6,'L’étage scapulaire et axial complète la topographie',[
 ('Les muscles proximaux des membres supérieurs et les muscles du cou sont intégrés à l’examen standardisé.','pnds-mmt'),
 ('L’évaluation associe les deltoïdes, les biceps et les fléchisseurs du cou aux groupes pelviens, selon le protocole choisi.','pnds-mmt'),
 ('La faiblesse des fléchisseurs du cou relativement aux extenseurs constitue aussi une variable des critères de classification.','crit-table'),
 ('Une atteinte distale isolée ou prédominante ne correspond pas à la distribution habituelle décrite pour la dermatomyosite.','pnds-examen'),
 ('L’examen neurologique sert alors à localiser la lésion et à discuter une cause périphérique, centrale ou jonctionnelle.','rms-clin'),
 ])
 c.fen(6,'Inspection cutanée : le geste cible des régions précises',[
 ('Les paupières sont inspectées pour une coloration érythémateuse ou violacée et un œdème périoculaire compatible avec un érythème héliotrope.','cedef-heliotrope+crit-table'),
 ('Le dos des doigts est regardé sur les surfaces d’extension articulaires pour distinguer les papules de Gottron des macules non palpables.','crit-table'),
 ('Le repli unguéal est examiné pour un érythème, des anomalies des cuticules et des capillaires visibles.','cedef-ongles'),
 ('La partie haute du dos, les épaules et le décolleté sont inspectés pour un érythème en châle ou en V.','cedef-tronc'),
 ('Les reliefs périarticulaires sont examinés pour une éventuelle calcinose, particulièrement dans les formes juvéniles.','cedef-calcinose+bsr-v'),
 ('Une lésion discrète reste recherchée attentivement devant un déficit musculaire, car les signes cutanés peuvent être peu intenses.','pnds-examen')])
 c.fen(6,'Examen des organes : chercher les manifestations qui changent la filière',[
 ('L’examinateur note la fréquence respiratoire et recherche un tirage ou une respiration paradoxale dans le bilan clinique respiratoire.','pnds-examen'),
 ('La voix et la contraction du voile du palais sont observées avec les symptômes de déglutition.','pnds-examen'),
 ('La recherche de dysphagie ne dépend pas uniquement de la force globale, car les deux atteintes ne sont pas toujours parallèles.','bsr-xi'),
 ('La fréquence cardiaque, la pression artérielle et les signes d’insuffisance ventriculaire complètent l’appréciation clinique.','pnds-examen'),
 ('Une anomalie préoccupante conduit à l’évaluation adaptée de l’organe avant de poursuivre un programme de suivi ordinaire.','pnds-severite+bsr-x+bsr-xi'),
 ('Les manœuvres de déglutition sont intégrées à l’évaluation professionnelle lorsque la sécurité est incertaine, plutôt qu’à un exercice autonome.','bsr-xi+pnds-severite')])

 c.tab(7,'Ensembles syndromiques numérotés',['Syndrome','Signes fonctionnels','Signes physiques et exploration'],[
  [('Le syndrome myogène proximal organise la plainte motrice.','pnds-examen'),('Le patient décrit des difficultés au lever, dans les escaliers ou lors d’activités des ceintures.','pnds-examen'),('Le testing documente une faiblesse surtout proximale et symétrique.','pnds-examen+pnds-mmt')],
  [('Le syndrome cutané caractéristique oriente vers la dermatomyosite.','cedef-heliotrope+cedef-gottron'),('Le patient peut signaler une éruption et un prurit qui modifient sa qualité de vie.','cedef-mecaniciens+bsr-xii'),('L’inspection cherche un héliotrope et des lésions de Gottron.','crit-table')],
  [('Le syndrome bulbaire et respiratoire fait rechercher une menace fonctionnelle.','pnds-examen+pnds-severite'),('La déglutition, la voix et la respiration deviennent difficiles.','pnds-examen'),('L’examen et les explorations spécialisées caractérisent la gravité et le mécanisme.','bsr-xi+ers-depistage')],
  [('Le syndrome systémique associé relie peau, organes et contexte immunologique.','fr-definition+imacs-risk'),('Les manifestations articulaires, pulmonaires ou générales peuvent dominer certains phénotypes.','fr-mda5'),('Le bilan d’organes et les anticorps sont interprétés dans leur constellation clinique.','bsr-vi+ers-depistage')]
 ])
 c.fen(7,'7.1 Définir le déficit myogène et ses signes fonctionnels',[
 ('Le déficit myogène de ce tableau est une diminution objectivée de la force, à prédominance proximale et généralement symétrique.','pnds-examen+crit-table'),
 ('Le signe du tabouret désigne la difficulté à se lever d’un siège sans utiliser les bras pour aider le redressement.','pnds-examen'),
 ('Sa recherche consiste à observer ce mouvement et à préciser ensuite la force des groupes proximaux concernés.','pnds-examen+pnds-mmt'),
 ('Le signe de Gowers est recherché dans la difficulté au relevé du sol décrite par le protocole.','pnds-examen'),
 ('Ces difficultés traduisent le retentissement de l’atteinte des ceintures, mais leur cause doit être confrontée à l’examen neurologique et articulaire.','pnds-examen+rms-clin'),
 ('Une myalgie correspond ici à une douleur musculaire possible, parfois déclenchée par la pression des masses musculaires.','pnds-examen'),
 ('La douleur ne remplace donc ni la démonstration du déficit ni la description de sa distribution.','rms-clin+pnds-examen')])
 c.fen(7,'7.2 Définir l’héliotrope et les lésions de Gottron',[
 ('L’érythème héliotrope est une coloration rose, liliacée ou violacée des paupières, souvent associée à un œdème périoculaire.','cedef-heliotrope+crit-table'),
 ('Il est recherché par l’inspection du pourtour des yeux, en décrivant la topographie et l’éventuel œdème.','cedef-heliotrope'),
 ('Les papules de Gottron sont des lésions érythémateuses à violacées en relief sur les surfaces d’extension des articulations.','crit-table'),
 ('Le signe de Gottron correspond au contraire à des macules de même distribution qui ne sont pas palpables.','crit-table'),
 ('L’inspection du dos des articulations des doigts et l’appréciation du relief permettent donc de décrire ces deux morphologies.','crit-table+cedef-gottron'),
 ('Les lésions spécifiques cutanées sont reliées à une atteinte de l’interface dermoépidermique dans la présentation du CEDEF.','cedef-interface'),
 ('Leur valeur tient à la constellation cutanée et musculaire, sans supprimer la recherche d’autres causes devant une éruption atypique.','fr-definition+rms-clin')])
 c.fen(7,'7.2 Définir les autres signes cutanés utiles au suivi',[
 ('Le signe du châle décrit des macules érythémateuses et violacées sur la nuque, les épaules et la racine des membres supérieurs.','cedef-tronc'),
 ('L’érythème en V intéresse la région antérieure du cou et la partie haute du thorax.','cedef-tronc'),
 ('La poïkilodermie associe une atrophie, des télangiectasies et des modifications de pigmentation au cours d’une évolution cutanée chronique.','cedef-tronc'),
 ('L’inspection des régions concernées permet de documenter ces aspects et leur évolution.','cedef-tronc+bsr-ii'),
 ('Le signe de la manucure comporte un repli unguéal congestif et douloureux à la pression, avec des anomalies cuticulaires possibles.','cedef-ongles'),
 ('La calcinose correspond à des dépôts calciques tissulaires, parfois responsables d’un blindage, d’une ulcération ou d’une fistulisation cutanée.','cedef-calcinose'),
 ('La recherche clinique de calcinose est particulièrement pertinente chez l’enfant et peut être complétée par une radiographie selon la situation.','bsr-v')])
 c.fen(7,'7.3 Définir la dysphagie et distinguer les mécanismes respiratoires',[
 ('La dysphagie est une difficulté à avaler ; elle fait partie des manifestations cliniques retenues dans les critères de classification.','crit-table'),
 ('Une toux pendant l’alimentation, une fausse route ou une voix nasonnée orientent l’examen vers la participation pharyngée.','pnds-examen'),
 ('Le mécanisme musculaire de la déglutition explique le recours à une évaluation spécialisée et aux professionnels de la parole et de la déglutition.','pnds-examen+bsr-xi'),
 ('Le risque concerne notamment la nutrition et l’inhalation ; il peut être important malgré une faiblesse générale apparemment modérée.','bsr-xi'),
 ('La dyspnée peut accompagner une atteinte des muscles respiratoires ou une pneumopathie interstitielle, qui ne sont pas le même mécanisme.','pnds-examen+rms-conclusion+ers-depistage'),
 ('L’examen respiratoire, les explorations fonctionnelles et le scanner thoracique ont ainsi des rôles complémentaires.','pnds-examen+ers-hrct+ers-depistage')])
 c.fen(7,'7.4 Le phénotype anti-MDA5 illustre les limites d’une lecture uniquement musculaire',[
 ('MDA5 appartient à une famille de protéines de l’immunité antivirale impliquée notamment dans la voie des interférons.','fr-mda5'),
 ('Les anticorps associés peuvent accompagner une présentation cutanée ulcérée et une atteinte musculaire faible ou absente.','fr-mda5'),
 ('Les mains de mécanicien décrivent une hyperkératose fissuraire des doigts dans l’enseignement clinique cité.','cedef-mecaniciens'),
 ('Ce signe n’est pas une preuve isolée de dermatomyosite ; il contribue à une constellation qui inclut d’autres myosites et le risque pulmonaire.','ers-depistage+bsr-vi'),
 ('Le caractère amyopathique ne supprime donc pas la recherche d’une atteinte interstitielle potentiellement grave.','fr-mda5+ers-depistage'),
 ])
