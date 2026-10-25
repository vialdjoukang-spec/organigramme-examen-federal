from pathlib import Path
import json, html, textwrap
P=Path(__file__).parent
sources=json.loads((P/'evidence.json').read_text())['sources']
parts=[]
def p(s): return '<p>'+s+'</p>\n'
def d(title, definition, mechanism, example, trap, source):
 return '<details class="t" style="display:inline;">\n<summary>'+title+'</summary>\n<div class="window">\n'+p(definition)+p('<em>Le raisonnement se déroule ainsi.</em> '+mechanism)+p('<em>Un exemple pédagogique illustre la décision.</em> '+example)+p('<em>Le piège se corrige ainsi.</em> '+trap)+p('Les sources étayent les principes; le cas est construit pour l’enseignement. '+source)+'</div>\n</details>\n'
def t(headers,rows):
 return '<div style="overflow-x:auto;">\n<table><thead><tr>'+''.join('<th>'+x+'</th>' for x in headers)+'</tr></thead><tbody>\n'+''.join('<tr>'+''.join('<td>'+x+'</td>' for x in row)+'</tr>\n' for row in rows)+'</tbody></table>\n</div>\n'
def sec(n,title,body,*windows):
 parts.append('<section id="point-'+str(n)+'">\n'+p('<strong>'+str(n)+'. '+title+'</strong><br>'+body)+''.join(windows)+'</section>\n')

sec(1,'Le conseil articule santé, besoins et durabilité.',
"Le conseil diététique évalue les pratiques alimentaires, les besoins et les contraintes d’une personne pour construire des changements réalisables. L’Office fédéral de la sécurité alimentaire et des affaires vétérinaires (OSAV) et la Société Suisse de Nutrition (SSN) proposent des repères pour les adultes en bonne santé, que le médecin adapte en cas de maladie ou de besoins particuliers. Ce point de départ clinique de PROFILES, appelé Situation as Starting Point (SSP), associe explicitement alimentation saine et durable. [S1–S5]",
d('La pyramide et l’assiette remplissent des fonctions différentes.',
"La pyramide traduit des repères de consommation entre groupes d’aliments; l’assiette aide à composer un repas principal. La version courte consultée porte l’année2026, mais elle représente les recommandations établies en2024; l’assiette a été actualisée en2025.",
"Un repère quotidien sert à examiner l’ensemble des prises; un modèle de repas sert à vérifier la présence de plusieurs groupes. Ces deux échelles ne se remplacent pas. Le clinicien commence par le repas réellement accessible au patient avant de discuter l’équilibre global de la journée.",
"Une personne de35ans mange seulement un sandwich à midi et se demande si son dîner doit compenser. On examine la garniture, le pain, les légumes ou fruits et les boissons, puis le reste de sa journée; on n’impose pas une seconde portion arbitraire pour corriger une image d’assiette.",
"Un dessin ne constitue ni une prescription calorique personnelle ni un test diagnostique. Les dimensions imprimées de l’assiette ne définissent pas une quantité universelle.", '[S2–S5]'),
d('Une alimentation durable reste nutritionnellement adéquate.',
"La durabilité examine les effets de la consommation sur l’environnement et tient compte des conditions de production, du gaspillage et de l’accès aux aliments. Elle complète l’évaluation nutritionnelle; elle ne fournit pas, à elle seule, un diagnostic individuel.",
"Le choix d’aliments mobilise des ressources, leur production génère des impacts et leur élimination peut rendre ces impacts inutiles. Le conseil peut donc agir sur la composition des repas et sur les pertes évitables, tout en conservant une alimentation suffisante et acceptable.",
"Un ménage de2personnes jette régulièrement un paquet entier de légumes. Le travail porte sur la quantité achetée, la conservation et la préparation qu’il maîtrise; acheter davantage de légumes sans solution de consommation augmenterait les pertes.",
"Le mot«local» ne permet pas, seul, de calculer une empreinte complète. Le médecin ne transforme pas une origine géographique en score environnemental chiffré sans analyse correspondante.", '[S4,S9]'),
d('Le conseil se distingue du traitement d’une maladie.',
"L’éducation nutritionnelle transmet des repères; la prise en charge médicale d’une maladie associe un diagnostic, des objectifs personnalisés et une surveillance. La recommandation alimentaire destinée à une personne saine ne suffit pas pour traiter une dénutrition, un diabète ou un trouble du comportement alimentaire.",
"Une même modification peut être utile dans un contexte et inadaptée dans un autre. Réduire les apports chez une personne qui maigrit involontairement peut aggraver sa situation; l’étape de qualification clinique précède donc la discussion d’un régime.",
"Deux adultes de60ans souhaitent«manger mieux». Le premier garde un poids stable et cherche des repas variés; le second a perdu du poids et mange difficilement. Ils ne reçoivent pas la même intervention, même s’ils donnent le même motif de consultation.",
"L’absence de demande médicale explicite ne prouve pas l’absence de maladie. Le conseil ne doit pas devenir une voie de contournement de l’évaluation clinique.", '[S5,S16,S17]'))

sec(2,'Les données suisses décrivent des populations distinctes.',
"L’Enquête suisse sur la santé (ESS) de2022 indique que43,0% des personnes de15ans ou plus vivant en ménage privé présentent un surpoids ou une obésité d’après leur taille et leur poids déclarés. L’étude suisse sur le sel2022–2023 estime la consommation moyenne adulte à8,7g/j, tandis que14% des personnes étudiées consomment moins de5g/j. Ces indicateurs ne mesurent pas la fréquence de chacun des dix scénarios de consultation; aucune distribution suisse homogène de ces scénarios n’a été trouvée. [S6,S7]",
t(['L’indicateur mesure…','Le résultat indique…','L’interprétation doit respecter…'],[
['L’ESS2022 classe le poids déclaré.','Le surpoids représente30,9% et l’obésité12,1%, soit43,0% au total. [S6]','L’enquête concerne les ménages privés et des données déclarées; elle ne remplace pas la mesure clinique.'],
['L’ESS2022 compare les sexes.','La proportion combinée atteint52,3% chez les hommes et33,8% chez les femmes. [S6]','Les écarts décrivent une distribution; ils ne justifient aucune présomption individuelle.'],
['L’étude suisse du sel compare les apports.','La moyenne atteint7,4g/j chez les femmes et9,9g/j chez les hommes. [S7]','Une moyenne populationnelle ne mesure pas l’apport d’un patient.'],
['L’enquête2010 estime la prévalence vie entière de l’anorexie.','La valeur est1,2% chez les femmes et0,2% chez les hommes. [S8]','Ces données anciennes ne mesurent ni l’incidence2026 ni la prévalence actuelle.'],
['L’OFEV étudie les pertes comestibles.','Environ un tiers se perd du champ à l’assiette. [S9]','L’indicateur concerne une chaîne alimentaire; il n’est pas une mesure des déchets d’un foyer donné.']]),
d('La prévalence ne permet pas de hiérarchiser seule les urgences.',
"La prévalence indique la proportion de personnes présentant un état dans une population et une période définies. Une prévalence vie entière exprime l’existence d’un épisode à un moment de la vie; elle ne décrit pas nécessairement la situation actuelle.",
"Le choix d’une action combine la probabilité et les conséquences d’un retard. Une situation peu fréquente mais dangereuse doit être recherchée tôt. C’est pourquoi la perte involontaire de poids et la restriction inquiétante apparaissent avant les branches cardiométaboliques dans l’algorithme.",
"Une patiente de25ans consulte pour des conseils de durabilité et décrit des vomissements répétés. Le médecin n’écarte pas un trouble alimentaire sous prétexte qu’il serait moins fréquent que le surpoids en population générale.",
"Comparer43,0% de surpoids/obésité actuelle avec1,2% d’anorexie vie entière additionne des objets statistiques différents. Le classement des scénarios reste pédagogique et sa fréquence n’est pas prétendue mesurée.", '[S6,S8,S24]'),
d('La distribution sociale guide les questions sans stigmatiser.',
"L’indicateur Obsan rapporte des différences selon le niveau de formation et rappelle que le poids dépend de facteurs multiples. Le conseil doit examiner ce qui rend les recommandations réalisables dans la vie quotidienne.",
"Un horaire, un budget ou une disponibilité limités peuvent empêcher une mise en pratique sans traduire un manque d’information. Le médecin recherche donc la contrainte précise et construit une option compatible, au lieu de répéter une recommandation que la personne connaît déjà.",
"Un travailleur de45ans n’a accès qu’à une petite supérette pendant son service. Le clinicien lui demande quels aliments et quels moyens de stockage sont disponibles; un exemple reposant sur une cuisine équipée ne répondrait pas à son problème.",
"La situation socioéconomique ne se déduit pas du poids, de l’apparence ou du niveau d’études. Les données collectives orientent une attention équitable; elles n’autorisent pas une conclusion personnelle sans entretien.", '[S6]'))

sec(3,'Les mécanismes relient les contraintes aux cibles du conseil.',
"Le SSP est transversal: il n’a pas de physiopathologie unique. L’analyse relie les apports, les besoins, l’assimilation et les conditions de vie aux difficultés observées, puis choisit une action qui agit sur le mécanisme identifié. Le tableau remplace la fausse cascade physiopathologique par une corrélation clinique explicite. [S16–S19]",
t(['La perturbation survient lorsque…','L’exploration recherche…','L’action corrige…'],[
['Les prises ne couvrent plus les besoins ou l’assimilation devient insuffisante.','L’entretien documente les repas, les difficultés digestives et la trajectoire pondérale; l’évaluation de dénutrition complète le dépistage. [S17]','L’équipe restaure un apport adapté et traite la cause; elle ne se limite pas à conseiller de«manger plus».'],
['Les difficultés buccales ou de déglutition empêchent l’alimentation.','Le clinicien examine la bouche et oriente l’évaluation de déglutition selon les signes. [S16]','Les soins buccaux et l’adaptation des prises répondent à l’obstacle identifié.'],
['Une restriction élimine les sources fiables de vitamineB12.','L’entretien précise les aliments enrichis, les compléments et le suivi médical. [S10]','Le plan assure une source fiable de vitamineB12 et un accompagnement adapté.'],
['Les facteurs cardiométaboliques se cumulent.','Le bilan considère le poids, la pression artérielle et les données métaboliques pertinentes. [S18,S19]','Une prise en charge globale associe alimentation, activité et traitements indiqués.'],
['Les aliments achetés ne sont pas consommés.','Le ménage décrit les pertes et leur cause concrète. [S9]','La planification et les pratiques domestiques ciblent la perte évitable identifiée.']]),
d('Le poids résulte d’une histoire et ne prouve pas une cause.',
"Le poids mesuré est un état à un moment donné. Son évolution apporte des informations que la valeur isolée ne donne pas, et la composition corporelle ainsi que les mouvements hydriques peuvent modifier son interprétation.",
"Une diminution involontaire attire l’attention sur une insuffisance d’apport, une mauvaise assimilation ou une maladie associée. Un excès pondéral n’empêche pas la diminution de la masse musculaire. Une rétention liquidienne peut masquer une perte de tissu et nécessite de rapprocher l’examen de l’histoire.",
"Une personne de72ans garde un poids identique après l’apparition d’œdèmes et explique qu’elle mange moins. Le clinicien ne conclut pas que son état nutritionnel est stable uniquement parce que la balance affiche la même valeur.",
"L’indice de masse corporelle ne mesure ni les muscles ni l’adéquation des micronutriments. Une valeur élevée ne permet donc pas d’exclure la dénutrition ou une carence.", '[S17]'),
d('Une exclusion alimentaire impose de vérifier la fonction supprimée.',
"Une substitution alimentaire est utile lorsque le repas conserve les fonctions nutritionnelles nécessaires. Le nom commercial ou l’aspect du produit ne garantit pas qu’il apporte les mêmes nutriments que l’aliment remplacé.",
"La suppression d’un groupe réduit certaines sources habituelles; le remplacement doit donc être évalué sur sa composition et sur le reste du régime. Dans un régime végétalien, la vitamineB12 nécessite une source fiable; l’évaluation doit aussi considérer les autres apports critiques.",
"Un adulte de30ans remplace tous les laitages par une boisson végétale. Le médecin demande le produit exact, vérifie les informations nutritionnelles et recherche comment la personne couvre les fonctions auparavant assurées par les laitages; il n’évalue pas seulement la couleur de la boisson.",
"«Végétal» n’équivaut pas automatiquement à«complet». Le conseil ne prescrit pas une dose de complément sur le seul récit d’un remplacement sans examen de la situation.", '[S4,S10,S23]'))

sec(4,'La démarche trie les dangers avant les habitudes modifiables.',
"Le premier tri recherche une perte pondérale involontaire, une restriction préoccupante, une difficulté à boire ou manger et des symptômes d’instabilité. Il distingue ensuite les besoins liés à l’âge ou à la grossesse, les exclusions alimentaires et les facteurs cardiométaboliques. Les dix scénarios peuvent coexister; leur liste ne forme pas dix diagnostics mutuellement exclusifs. [S11,S14,S16–S19,S24]",
d('Une perte involontaire conduit à évaluer la dénutrition.',
"La perte involontaire constitue un critère phénotypique de l’approche Global Leadership Initiative on Malnutrition (GLIM), consensus diagnostique international incluant la Société européenne de nutrition clinique et métabolisme (ESPEN). Le diagnostic demande aussi un critère étiologique.",
"On confirme d’abord l’histoire, puis on recherche les apports diminués, les difficultés d’assimilation et une charge inflammatoire ou morbide. La perte de poids n’identifie pas à elle seule la cause; le bilan médical reste nécessaire.",
"Un patient de68ans rapporte une perte de6kg sur un poids antérieur de80kg en4mois. La perte relative calculée est7,5%; cette constatation justifie une évaluation, mais ne prouve pas à elle seule une dénutrition GLIM complète ni sa cause.",
"Attribuer la perte à un régime«plus sain» sans vérifier qu’elle était voulue peut retarder la reconnaissance d’une maladie ou d’un trouble alimentaire.", '[S17]'),
d('Une restriction avec peur de grossir change le cadre du conseil.',
"Une restriction alimentaire préoccupante peut relever d’un trouble du comportement alimentaire, appelé TCA. L’évaluation associe la santé somatique et les dimensions psychiques; la discussion alimentaire ne suffit pas à les séparer.",
"Les conduites restrictives ou compensatoires peuvent s’accompagner de désordres électrolytiques et de complications cardiaques. Le clinicien questionne les comportements puis recherche leur retentissement; une apparence rassurante ne clôt pas cette analyse.",
"Une personne de22ans explique qu’elle supprime toujours plus d’aliments pour obtenir une alimentation«pure» et qu’elle vomit après certains repas. Le médecin interrompt la proposition d’une nouvelle restriction et organise une évaluation spécialisée adaptée au retentissement.",
"Un intérêt pour la durabilité ne définit pas un TCA, mais il n’exclut pas non plus une restriction pathologique. La distinction repose sur l’entretien, la souffrance, le fonctionnement et l’examen.", '[S8,S24]'),
d('Une maladie rénale ou hépatique empêche la prescription automatique.',
"Les repères pour adultes sains ne constituent pas des prescriptions de protéines, de boissons ou de minéraux adaptées à toutes les maladies. L’insuffisance rénale, les complications hépatiques et les restrictions déjà prescrites demandent une coordination médicale.",
"Le même aliment apporte plusieurs nutriments et peut modifier plusieurs objectifs. Une modification isolée peut contredire un autre traitement; le clinicien vérifie donc le diagnostic, les prescriptions existantes et les données nécessaires avant de fixer une cible.",
"Un patient de70ans suivi pour une maladie rénale demande s’il doit remplacer son sel par un produit enrichi en potassium. Il apporte l’emballage et ses médicaments; le conseil est coordonné avec son équipe plutôt que validé par une règle générale sur les fruits et légumes.",
"L’absence de cible chiffrée dans cette vue d’ensemble ne signifie pas que l’adaptation est inutile. Les paliers détaillés non vérifiés sont signalés dans HELP et ne sont pas inventés.", '[S5,S16,S18,S19]'))

sec(5,'L’entretien explique les prises et recherche les drapeaux rouges.',
"L’anamnèse part d’une journée réellement vécue, puis explore la variabilité, les exclusions, les difficultés matérielles et la trajectoire pondérale. Chaque question vise une décision: évaluer un danger, identifier un apport manquant ou rendre l’objectif réalisable. Les vomissements, la restriction inquiétante et les difficultés de déglutition imposent un examen médical et une orientation selon leur retentissement. [S16,S17,S24]",
t(['Le clinicien pose cette question.','La réponse permet cette analyse.','La décision reste concrète.'],[
['«Qu’avez-vous mangé et bu hier, depuis votre réveil jusqu’au coucher?»','La personne décrit des prises réelles plutôt qu’un régime idéal.','Le clinicien demande ensuite si cette journée ressemble aux autres.'],
['«Votre poids a-t-il changé, depuis quand et était-ce volontaire?»','La trajectoire distingue une intention de perte d’une évolution inexpliquée. [S17]','Le clinicien vérifie les mesures disponibles et l’état hydrique.'],
['«Qu’est-ce qui vous empêche de manger ou boire comme vous le souhaitez?»','La réponse peut révéler une douleur buccale, une gêne à avaler ou une contrainte matérielle. [S16]','La prise en charge cible l’obstacle au lieu de répéter des repères.'],
['«Quels aliments avez-vous supprimés et par quoi les remplacez-vous?»','La réponse situe le risque de couverture insuffisante des besoins. [S10,S15]','Le plan examine les sources fiables et les situations particulières.'],
['«Avez-vous des vomissements, des comportements compensatoires ou une peur de certains aliments?»','La réponse ouvre une évaluation de TCA et de ses complications. [S24]','Le médecin évalue le retentissement sans proposer un régime plus strict.'],
['«Qui achète, cuisine et partage vos repas?»','La réponse identifie les personnes et les moyens utiles au changement.','Le patient choisit les aides qu’il souhaite mobiliser.']]),
d('Le relevé alimentaire sert à comprendre, sans juger.',
"Le relevé alimentaire est un support descriptif: il précise les aliments, les boissons, les horaires et les circonstances. Il ne constitue pas une preuve morale de bonne ou de mauvaise conduite.",
"Une différence entre intention et réalité peut montrer une difficulté pratique. Le dialogue confronte les informations avec bienveillance et cherche ce qui rendrait le prochain repas plus simple. Le relevé ne doit pas renforcer une surveillance obsessionnelle chez une personne en difficulté avec l’alimentation.",
"Un patient de50ans affirme ne jamais boire de boissons sucrées, puis décrit une boisson énergisante pendant ses services. Le clinicien clarifie ce qu’il entendait par«boisson sucrée» et examine l’étiquette avec lui; il ne présente pas cette découverte comme un mensonge.",
"Une seule journée ne représente pas automatiquement une semaine entière. Les exemples du week-end, du travail et des jours difficiles servent à vérifier cette variabilité.", '[S2,S5,S24]'),
d('Le récit du poids doit être daté et contextualisé.',
"La trajectoire pondérale décrit un poids de référence, un poids actuel, une durée et le caractère voulu ou non de l’évolution. Sans ces éléments, une affirmation comme«j’ai beaucoup maigri» reste difficile à interpréter.",
"La durée distingue une évolution récente d’un changement ancien; l’intention distingue un objectif annoncé d’une perte subie. L’état hydrique, les vêtements et les conditions de mesure peuvent aussi modifier la comparaison, ce qui impose de vérifier les données sans retarder l’évaluation d’une situation inquiétante.",
"Une femme de75ans indique60kg aujourd’hui et65kg il y a5mois, d’après deux mesures médicales. Le calcul dérivé donne7,7% de perte; le médecin recherche les apports réduits et la maladie associée plutôt que de se limiter à une valeur isolée d’indice de masse corporelle.",
"Une perte volontaire n’est pas automatiquement sans risque; son contexte et son retentissement comptent. Une dénutrition peut aussi apparaître chez une personne auparavant en surpoids.", '[S17]'))

sec(6,'L’examen ciblé interprète les mesures avec le contexte.',
"L’examen vérifie les mesures anthropométriques et les signes suggérés par l’histoire. Il examine notamment l’état buccal, l’hydratation et le retentissement fonctionnel lorsque des difficultés alimentaires sont présentes; devant un TCA possible, la pression artérielle, le pouls et les signes d’atteinte somatique complètent l’évaluation. Un aspect normal ne suffit pas à exclure un déficit nutritionnel. [S16,S17,S24]",
d('La mesure anthropométrique répond à une question précise.',
"L’anthropométrie décrit les dimensions corporelles; l’indice de masse corporelle (IMC) rapporte le poids à la taille au carré. Le recueil doit préciser la mesure utilisée et la date, afin de rendre la comparaison interprétable.",
"On mesure le poids et la taille avec un matériel adapté et on consigne les conditions qui peuvent fausser la comparaison. L’IMC fournit une classification pondérale; le clinicien la rapproche de l’histoire, des comorbidités et des éléments de composition corporelle.",
"Un adulte mesure1,75m et pèse92kg: son IMC calculé est30,0kg/m² après arrondi à une décimale. Cette valeur appelle une évaluation clinique, mais ne quantifie ni sa masse musculaire ni la qualité de son alimentation.",
"Les seuils adultes ne s’appliquent pas comme tels aux enfants, qui nécessitent des références de croissance. Pendant la grossesse, le poids actuel doit être replacé dans la situation obstétricale.", '[S6,S14,S24]'),
d('L’examen de la bouche cherche un obstacle aux prises.',
"L’examen buccal observe la dentition, les prothèses et les muqueuses en lien avec les symptômes. Il recherche un obstacle fonctionnel qui explique une difficulté à mâcher ou une diminution des prises.",
"Une douleur ou une prothèse mal tolérée peut entraîner l’abandon d’aliments puis une réduction de la variété ou de l’apport. Le clinicien demande à la personne ce qu’elle n’arrive plus à manger, examine avec son accord et adresse pour une prise en charge adaptée.",
"Une personne de82ans laisse les aliments solides parce que sa prothèse la blesse. La proposition immédiate porte sur des prises compatibles avec ses possibilités et sur la correction de la cause; l’éducation à la pyramide ne résout pas à elle seule la douleur.",
"Une texture modifiée ne garantit pas une déglutition sûre. Une toux ou une gêne à avaler demande une évaluation spécifique; on ne déduit pas sa sécurité d’une inspection de la bouche.", '[S16]'),
d('Les œdèmes rendent le poids plus difficile à interpréter.',
"Les œdèmes correspondent à une accumulation liquidienne dans les tissus. Dans l’évaluation nutritionnelle, leur présence peut masquer une diminution du poids tissulaire et doit conduire à examiner la maladie sous-jacente.",
"Le clinicien observe les régions concernées et documente les signes dans leur contexte, puis rapproche la mesure du poids de l’histoire et des données médicales. Il ne convertit pas arbitrairement un œdème en kilogrammes de poids«sec».",
"Un patient de78ans a des chevilles gonflées et mange la moitié de ses repas habituels. Même si son poids ne baisse pas, l’évaluation des apports et de la masse musculaire reste pertinente; le bilan de l’œdème suit sa propre logique clinique.",
"L’œdème n’est pas un signe spécifique de dénutrition. Il peut accompagner plusieurs maladies et ne suffit pas à poser un diagnostic nutritionnel.", '[S17]'))

sec(7,'Les profils cliniques associent plaintes et signes observés.',
"L’approche syndromique sépare ce que la personne ressent de ce que le clinicien mesure ou observe. Elle rassemble ces informations sans faire d’un profil alimentaire un diagnostic automatique. Les profils ci-dessous déterminent surtout le type d’évaluation à approfondir. [S16–S19,S24]",
d('7.1 Le profil d’apports insuffisants exige une recherche de cause.',
"Le profil associe des prises diminuées, une perte pondérale ou un retentissement fonctionnel. Les plaintes peuvent porter sur l’appétit, la mastication, la déglutition ou la tolérance digestive; les constatations peuvent inclure une trajectoire pondérale défavorable et une diminution musculaire.",
"Une difficulté d’accès, une gêne à manger ou une maladie réduit les apports; la persistance de cette situation expose à une perte de tissu et de fonction. L’entretien précise le premier maillon et l’examen vérifie le retentissement, ce qui permet de choisir une intervention ciblée.",
"Une personne de80ans dit ne plus faire les courses depuis une hospitalisation. Les repas manquants expliquent une partie de la situation; l’équipe examine aussi ses capacités physiques, sa bouche et les aides disponibles, car plusieurs causes peuvent se cumuler.",
"Une albumine isolée ou une silhouette maigre ne remplace pas l’approche diagnostique GLIM. Une personne en surpoids peut également présenter ce profil.", '[S16,S17]'),
d('7.2 Le profil cardiométabolique demande une évaluation globale.',
"Le profil peut associer un excès pondéral, une pression artérielle élevée, une anomalie glycémique, une dyslipidémie ou une stéatose hépatique métabolique. Certaines de ces affections sont peu symptomatiques et se révèlent par les mesures ou le bilan.",
"Les facteurs peuvent se renforcer et partagent des axes de prise en charge, mais chacun conserve ses critères diagnostiques. Le médecin examine les risques et les comorbidités plutôt que d’attribuer tous les résultats à une seule habitude alimentaire.",
"Une personne de58ans a une obésité et un diabète connu; l’identification d’une stéatose ne clôt pas l’évaluation hépatique. On recherche le risque de fibrose selon une démarche dédiée, en parallèle de la prise en charge cardiométabolique.",
"Une recommandation alimentaire utile ne remplace pas les traitements nécessaires. Un patient ne doit pas attendre de«réussir son régime» pour recevoir une prise en charge médicalement indiquée.", '[S18,S19]'),
d('7.3 Le profil restrictif exige une lecture somatique et psychique.',
"Les plaintes peuvent concerner la peur de grossir, des règles alimentaires envahissantes ou une souffrance autour des repas. L’examen recherche le retentissement du poids bas, des vomissements ou des autres comportements décrits, y compris cardiovasculaire et électrolytique.",
"Une restriction ou une compensation persistante peut altérer les apports et l’équilibre physiologique; les conséquences physiques peuvent entretenir les difficultés de fonctionnement. Le clinicien organise une évaluation conjointe plutôt que de réduire le problème à une préférence alimentaire.",
"Un étudiant de21ans consulte pour«optimiser» son alimentation; il décrit une restriction croissante et des malaises. La question immédiate devient la sécurité et le retentissement somatique; une liste supplémentaire d’aliments interdits serait inadaptée.",
"Les hommes peuvent également présenter un TCA. Une prévalence différente entre sexes ne justifie pas l’absence de recherche chez un patient masculin.", '[S8,S24]'))

