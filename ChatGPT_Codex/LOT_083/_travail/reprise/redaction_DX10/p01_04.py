def rediger(c):
 c.block(1,'Une maladie auto-immune définie par sa constellation cutanée et musculaire',[
 ('Dans sa recommandation de 2022, la Deutsche Gesellschaft für Neurologie décrit la dermatomyosite par une atteinte de la peau et des muscles, avec participation viscérale variable.','dgn-definition'),
 ('La vasculopathie et la signature des interférons contribuent à distinguer cette maladie des autres myosites inflammatoires.','dgn-definition+cedef-meca'),
 ('Les manifestations caractéristiques peuvent concerner les paupières, les surfaces articulaires des doigts et les régions photosensibles.','cedef-heliotrope+cedef-gottron+cedef-tronc'),
 ('Une faiblesse proximale objectivée renforce la constellation, tandis que la douleur musculaire est possible sans constituer une condition indispensable.','rms-clin+pnds-examen'),
 ('La dermatomyosite amyopathique conserve une atteinte cutanée évocatrice sans faiblesse musculaire manifeste ; elle demande cependant une évaluation des organes associés.','fr-definition+fr-mda5'),
 ('La forme juvénile appartient au même ensemble, mais son évaluation, ses complications et sa prise en charge nécessitent une expertise pédiatrique.','dgn-definition+bsr-v'),
 ])
 c.fen(1,'Dermatomyosite, myosite, myopathie et forme amyopathique',[
 ('Une myopathie désigne une affection musculaire ; les causes explorées comprennent les maladies inflammatoires, endocriniennes, toxiques, infectieuses et génétiques.','rms-clin+rms-hist'),
 ('Les myopathies inflammatoires auto-immunes forment un groupe hétérogène, dont la dermatomyosite est une entité clinique et histologique.','rms-hist+dgn-definition'),
 ('Le mot amyopathique décrit ici la présentation musculaire et ne garantit pas l’absence de pneumopathie ou d’autre atteinte systémique.','fr-mda5+ers-depistage'),
 ('Une créatine kinase normale ne rend pas les lésions cutanées spécifiques anodines, notamment dans le phénotype associé aux anticorps anti-MDA5.','fr-mda5'),
 ('Le syndrome des antisynthétases et la myopathie nécrosante immunomédiée restent des diagnostics distincts, même lorsque leur présentation comporte une faiblesse proximale.','rms-hist+fr-definition'),
 ('La présence d’un cancer modifie le bilan et le pronostic d’une dermatomyosite adulte, sans définir à elle seule la maladie musculaire.','imacs-risk+rms-conclusion')])
 c.tab(1,'Les mots orientent des décisions différentes',['Terme utilisé','Ce que le terme apporte','Limite à conserver'],[
  [('La dermatomyosite associe une constellation cutanée et une atteinte musculaire variable.','dgn-definition+fr-definition'),('Elle impose de rechercher les autres atteintes d’organes.','rms-conclusion'),('La douleur et la CK ne résument pas le diagnostic.','rms-bilan')],
  [('La forme amyopathique exprime une présentation sans faiblesse musculaire manifeste.','fr-mda5'),('Elle conduit notamment à évaluer le risque pulmonaire.','ers-depistage'),('Le qualificatif ne signifie pas une maladie bénigne.','fr-mda5')],
  [('La myosite nécrosante immunomédiée possède une histologie différente.','rms-hist'),('Les anticorps anti-HMGCR ou anti-SRP orientent cette autre branche.','fr-autres'),('Une exposition aux statines ne remplace pas la caractérisation de la myopathie.','rms-clin+rms-hist')],
  [('La classification EULAR/ACR décrit une probabilité de myopathie inflammatoire.','rms-class+crit-cutoffs'),('Elle facilite une définition homogène des groupes étudiés.','crit-cutoffs'),('Elle ne remplace pas le diagnostic clinique individuel.','rms-class')]
 ])
 c.block(1,'Les références thérapeutiques ont des périmètres définis',[
 ('La British Society for Rheumatology maintient sa recommandation de 2022 dans son annuaire actuel pour les myosites de l’enfant, de l’adolescent et de l’adulte.','bsr-actualite'),
 ('Cette recommandation organise le traitement musculaire, cutané et systémique ; elle distingue les propositions adultes des propositions pédiatriques.','bsr-i+bsr-v'),
 ('Les recommandations ERS/EULAR complètent la stratégie lorsqu’une pneumopathie interstitielle accompagne la myosite.','ers-traitement+ers-association'),
 ('Les spécialités suisses retenues plus loin possèdent des notices propres ; leur indication et leurs précautions sont vérifiées séparément.','sp-ind+im-ind+oc-ind')])

 c.block(2,'La rareté suisse ne se transforme pas en chiffre national supposé',[
 ('La revue des HUG décrit les myopathies inflammatoires comme un ensemble hétérogène, dont le diagnostic différentiel et le pronostic nécessitent une caractérisation précise.','rms-conclusion'),
 ('Les estimations portant sur toutes les myopathies inflammatoires ne donnent pas directement la prévalence de la dermatomyosite en Suisse.','rms-class+rms-hist'),
 ('Pour disposer d’un repère européen explicitement défini, on peut examiner la cohorte populationnelle de Cantabrie publiée en 2025.','esp-provenance+esp-methodes'),
 ('Cette étude a recherché les cas diagnostiqués pendant la période 2000–2022 et a appliqué des critères de classification aux sous-groupes étudiés.','esp-methodes'),
 ('Dans son sous-groupe adulte de dermatomyosite, les auteurs rapportent une incidence de 0,36 cas pour cent mille personnes-années.','esp-adulte'),
 ('Ils rapportent une prévalence de 9 cas pour cent mille habitants ; cette mesure décrit leur territoire et leur méthode de repérage.','esp-adulte+esp-methodes'),
 ('Ces valeurs européennes constituent un repère local et ne sont pas converties en nombre attendu de cas suisses.','esp-methodes+esp-adulte')])
 c.tab(2,'Repères européens et dénominateurs à conserver',['Mesure rapportée','Population et période','Interprétation permise'],[
  [('L’incidence adulte rapportée est de 0,36 cas pour cent mille personnes-années.','esp-adulte'),('L’étude cantabre couvre les diagnostics de2000–2022.','esp-methodes'),('Elle décrit de nouveaux diagnostics dans une population définie.','esp-methodes')],
  [('La prévalence adulte rapportée est de 9 cas pour cent mille habitants.','esp-adulte'),('Les auteurs identifient 27 adultes atteints de dermatomyosite.','esp-adulte+esp-effectif'),('La prévalence locale ne représente pas une estimation nationale suisse.','esp-methodes')],
  [('L’âge moyen adulte au diagnostic est de 55,2 ans.','esp-adulte'),('Le sous-groupe compte 23 femmes parmi 27 adultes.','esp-adulte+esp-effectif'),('Cette composition décrit la série et ne définit pas une condition diagnostique.','esp-adulte+crit-table')]
 ])
 c.fen(2,'Incidence, prévalence et composition d’une série répondent à des questions différentes',[
 ('L’incidence de l’étude est exprimée en cas par personnes-années, alors que sa prévalence est exprimée par population.','esp-methodes+esp-adulte'),
 ('La proportion de femmes ou d’un sous-type dans une cohorte ne peut donc pas être utilisée comme prévalence de dermatomyosite.','esp-methodes+esp-adulte'),
 ('Le diagnostic peut survenir chez l’enfant comme chez l’adulte, et l’âge module le phénotype et les complications recherchées.','fr-definition+bsr-v'),
 ('Le risque tumoral adulte se raisonne selon le sous-type, les anticorps et la clinique ; il n’est pas transposé automatiquement à l’enfant.','imacs-risk+bsr-vii'),
 ('L’existence de formes amyopathiques explique également pourquoi un recrutement fondé uniquement sur la faiblesse manquerait une partie du spectre.','fr-definition+fr-mda5')])
 c.block(2,'L’histoire naturelle dépend des organes et du retentissement',[
 ('Une atteinte pulmonaire interstitielle peut dominer la gravité, notamment dans le phénotype anti-MDA5, malgré une atteinte musculaire discrète.','fr-mda5'),
 ('La dysphagie expose à une perte de poids et à une pneumopathie d’inhalation, indépendamment de l’intensité apparente de la faiblesse globale.','bsr-xi'),
 ('Une participation cardiaque augmente également la morbidité et demande une évaluation dédiée.','bsr-x'),
 ('Chez l’adulte, la présence d’un cancer modifie le parcours diagnostique et la stratégie de surveillance.','imacs-risk+imacs-screen'),
 ('La rémission inflammatoire et la récupération fonctionnelle ne sont pas interchangeables, car un handicap peut persister après la diminution de l’activité.','rms-fonction'),
 ('Le suivi doit donc considérer la force, les activités quotidiennes, les symptômes cutanés et les complications du traitement.','bsr-i+bsr-xii'),
 ('Chez l’enfant, la calcinose et les conséquences du retard diagnostique justifient une orientation et une surveillance adaptées.','bsr-v'),

 ])
 c.block(3,'L’amorce associe susceptibilité et réponse immunitaire anormale',[
 ('La dermatomyosite associe une inflammation auto-immune et une atteinte de la microvascularisation musculaire.','pnds-definition+cedef-meca'),
 ('Le modèle présenté par le CEDEF relie une susceptibilité génétique à des facteurs environnementaux, dont les ultraviolets.','cedef-meca'),
 ('Ces associations n’établissent cependant pas un déclencheur unique chez chaque patient ; le phénotype reste hétérogène.','cedef-meca+fr-definition'),
 ('Les cellules dendritiques plasmacytoïdes participent à une production d’interférons de type I dans ce modèle inflammatoire.','cedef-meca'),
 ('La signature des interférons représente une caractéristique moléculaire importante de la dermatomyosite dans la description de la DGN.','dgn-definition'),
 ('La réponse immunitaire comporte aussi une activation du complément et un recrutement de cellules inflammatoires autour des petits vaisseaux.','cedef-meca+rms-hist')])
 c.fen(3,'Du capillaire à la faiblesse proximale',[
 ('L’activation du complément s’accompagne d’une lésion de l’endothélium capillaire et d’une atteinte ischémique musculaire dans le modèle décrit.','cedef-meca'),
 ('L’expression de molécules d’adhésion favorise l’arrivée de cellules inflammatoires, ce qui entretient l’atteinte tissulaire.','cedef-meca'),
 ('L’histologie de dermatomyosite peut montrer une inflammation périmysiale avec atrophie périfasciculaire.','rms-hist'),
 ('Cette localisation aide à distinguer la dermatomyosite d’une nécrose diffuse de fibres ou d’une myosite à inclusions.','rms-hist'),
 ('La perte de fonction devient cliniquement visible lors des mouvements des ceintures, comme le lever d’une chaise.','pnds-examen'),
 ('Le lien entre lésion musculaire et faiblesse doit néanmoins être exploré, car les causes neurologiques et le déconditionnement peuvent produire des difficultés proches.','rms-clin')])
 c.block(3,'Les examens montrent des dimensions différentes de la lésion',[
 ('La créatine kinase renseigne sur une atteinte musculaire, mais son niveau ne mesure pas à lui seul la sévérité de la maladie.','rms-bilan'),
 ('L’imagerie musculaire en séquences sensibles à l’eau peut montrer un œdème et guider le choix d’un site de biopsie.','cedef-irm+rms-bilan'),
 ('Un hypersignal musculaire est cependant non spécifique ; il ne suffit pas à attribuer l’anomalie à une dermatomyosite.','cedef-irm'),
 ('L’électroneuromyographie étudie le fonctionnement neuromusculaire et aide à écarter des causes neurologiques ou jonctionnelles.','rms-bilan'),
 ('La biopsie complète cette exploration lorsque la constellation clinique et biologique ne permet pas de caractériser suffisamment la myopathie.','rms-hist'),
 ('Les anticorps précisent des associations phénotypiques, mais un résultat de panel doit être interprété avec la présentation clinique.','fr-anticorps+bsr-vi')])
 c.tab(3,'Corrélation : perturbation, exploration et mécanisme thérapeutique',['Perturbation','Exploration qui la documente','Réponse thérapeutique expliquée'],[
  [('L’inflammation musculaire altère la force des ceintures.','pnds-examen'),('Le testing objectivé et son suivi décrivent le déficit.','pnds-mmt+bsr-i'),('Les glucocorticoïdes participent à l’induction du contrôle inflammatoire.','bsr-i+sp-meca')],
  [('La vasculopathie et l’inflammation produisent une atteinte périfasciculaire.','rms-hist+cedef-meca'),('La biopsie recherche la distribution des lésions et les diagnostics voisins.','rms-hist'),('L’immunosuppression vise l’activité de maladie plutôt qu’un simple chiffre enzymatique.','bsr-i+rms-bilan')],
  [('L’atteinte cutanée spécifique intéresse notamment les régions articulaires et photosensibles.','cedef-gottron+cedef-tronc'),('L’inspection topographique et la documentation cutanée suivent son évolution.','pnds-examen+bsr-ii'),('La photoprotection et le contrôle de la maladie réduisent les poussées cutanées.','bsr-ii')],
  [('La participation pharyngée perturbe une déglutition sûre.','pnds-examen+bsr-xi'),('Les symptômes et une évaluation spécialisée de déglutition précisent le risque.','bsr-xi'),('La stratégie associe traitement de maladie et intervention des professionnels de déglutition.','bsr-xi')],
  [('La pneumopathie interstitielle peut évoluer indépendamment d’une faiblesse musculaire importante.','fr-mda5'),('Le scanner thoracique de haute résolution complète les explorations fonctionnelles respiratoires.','ers-depistage+ers-hrct'),('Une immunosuppression spécialisée et parfois combinée est recommandée dans les myosites avec atteinte interstitielle.','ers-traitement+ers-association')],
  [('Les lésions et l’inactivité peuvent laisser un retentissement fonctionnel durable.','rms-fonction'),('Les activités quotidiennes et la force sont réévaluées au cours du suivi.','bsr-xii+bsr-i'),('La physiothérapie et l’ergothérapie accompagnent la récupération dans un programme adapté.','bsr-i+bsr-xii')]
 ])
 c.fen(3,'Ce que les traitements modifient et ce qu’ils ne démontrent pas',[
 ('La prednisolone stimule la synthèse de protéines responsables d’effets anti-inflammatoires et immunosuppresseurs.','sp-meca'),
 ('L’azathioprine est un dérivé de la mercaptopurine dont l’effet immunosuppresseur comporte une action antimétabolite proposée par l’AIPS.','im-meca'),
 ('Son mécanisme exact reste incomplètement élucidé ; l’AIPS précise néanmoins qu’elle permet une épargne des corticoïdes associés.','im-meca'),
 ('Les immunoglobulines intraveineuses ont une action immunomodulatrice dont le mécanisme hors substitution n’est pas entièrement élucidé.','oc-meca'),
 ('La poursuite d’une faiblesse demande de distinguer activité inflammatoire, séquelles et complications du traitement avant une nouvelle escalade.','rms-fonction+bsr-i')])

 c.block(4,'Les menaces d’organes précèdent la recherche d’une étiquette',[
 ('🚩E1 conditionnelle : une menace respiratoire, bulbaire ou cardiaque ouvre une filière urgente, plutôt qu’un bilan ambulatoire différé.','pnds-severite+bsr-x+bsr-xi'),
 ('Une dyspnée, une orthopnée ou une respiration paradoxale demandent de préciser rapidement une faiblesse respiratoire et une atteinte pulmonaire associée.','pnds-examen+ers-depistage'),
 ('Une fausse route, une voix modifiée ou une dysphagie importante imposent une appréciation de la sécurité de déglutition.','pnds-examen+bsr-xi'),
 ('Des palpitations, une douleur cardiaque ou des signes d’insuffisance ventriculaire justifient une évaluation cardiaque dédiée.','pnds-examen+bsr-x'),
 ('Les manifestations cutanées évocatrices et la faiblesse stable justifient également une orientation spécialisée, sans transformer toute dermatomyosite en urgence vitale.','pnds-severite+pnds-hospitalisation'),
 ('Le choix de la filière dépend donc de l’état clinique et des organes menacés, puis de la caractérisation de la myopathie.','rms-clin+pnds-severite')])
 c.tab(4,'Diagnostics discriminants : les situations graves sont examinées en premier',['Diagnostic ou branche','Élément qui discrimine','Piège à éviter','Conduite si l’argument est positif'],[
  [('Une atteinte respiratoire ou bulbaire sévère complique la myosite.','pnds-severite'),('L’examen cherche détresse, orthopnée, fausses routes et défaut de protection de la déglutition.','pnds-examen+bsr-xi'),('Une CK peu élevée ou une faible douleur ne rassurent pas sur ces organes.','rms-bilan+fr-mda5'),('La prise en charge hospitalière urgente mobilise les spécialistes concernés.','pnds-severite+pnds-hospitalisation')],
  [('Une participation cardiaque constitue une autre menace conditionnelle.','bsr-x'),('L’ECG, la troponine I et les explorations cardiaques orientées précisent la suspicion.','bsr-x'),('La troponine T peut provenir aussi du muscle squelettique en régénération.','bsr-x'),('L’évaluation cardiologique est organisée et le traitement est adapté à la situation clinique.','bsr-x+rms-conclusion')],
  [('Une myopathie nécrosante immunomédiée peut produire une faiblesse proximale importante.','rms-hist'),('La biopsie et les anticorps anti-HMGCR ou anti-SRP caractérisent cette autre forme.','fr-autres+rms-hist'),('Une prise de statine n’autorise pas à nommer toutes les faiblesses de simples myalgies médicamenteuses.','rms-clin+rms-hist'),('Le bilan neuromusculaire spécialisé est poursuivi afin d’adapter la prise en charge à l’entité.','rms-conclusion')],
  [('Une myopathie hypothyroïdienne entre dans le diagnostic différentiel.','rms-clin'),('Le bilan thyroïdien et l’examen des autres signes endocriniens orientent.','rms-bilan+rms-clin'),('Une faiblesse proximale avec enzymes élevées n’est pas spécifique d’une myosite auto-immune.','rms-bilan'),('La cause endocrinienne est explorée avant d’attribuer le déficit à une dermatomyosite.','rms-clin+rms-conclusion')],
  [('Une atteinte neurologique ou jonctionnelle peut imiter un déficit musculaire.','rms-clin'),('La localisation neurologique et l’électroneuromyographie restreignent le diagnostic différentiel.','rms-clin+rms-bilan'),('La fatigue ressentie et la faiblesse objectivée ne sont pas confondues.','rms-clin'),('La filière neurologique précise la localisation et les explorations nécessaires.','rms-clin+rms-conclusion')]
 ])
 c.fen(4,'Caractériser une faiblesse avant d’interpréter un panel d’anticorps',[
 ('Le déficit est décrit selon sa distribution proximale ou distale et son caractère symétrique ou asymétrique.','rms-clin'),
 ('La dermatomyosite habituelle intéresse surtout les ceintures, tandis qu’une prédominance distale isolée exige d’examiner d’autres causes.','pnds-examen'),
 ('Une arthropathie ou un déconditionnement peut limiter les mouvements sans représenter la même lésion musculaire.','rms-clin'),
 ('Un panel d’anticorps positif doit donc rester cohérent avec cette localisation clinique et les autres examens.','fr-anticorps+bsr-vi'),
 ('Les résultats d’immunoblot peuvent être trompeurs ; leur interprétation associe le contexte et les manifestations d’organes.','fr-anticorps+bsr-vi'),
 ('L’absence d’anticorps détectés ne termine pas le bilan lorsque la constellation clinique demeure évocatrice.','rms-bilan')])
 c.block(4,'Le diagnostic associé modifie la stratégie',[
 ('La recherche de cancer suit une appréciation de risque chez l’adulte, au-delà des dépistages usuels adaptés à l’âge et au sexe.','imacs-risk+imacs-screen'),
 ('Le sous-type dermatomyosite, certains anticorps et une dysphagie importante comptent dans cette stratification.','imacs-risk'),
 ('Une forme cliniquement amyopathique peut au contraire conduire d’abord à approfondir le bilan pulmonaire.','fr-mda5+ers-depistage'),
 ('Les causes infectieuses et médicamenteuses doivent également être considérées avant d’instaurer une immunosuppression.','rms-clin+rms-conclusion'),
 ])
