# -*- coding: utf-8 -*-
"""Compléments sourcés du DX.2, phrases nouvelles."""
from dx_lib import b, w, tableau

def extra() -> dict[int, str]:
    return {
1: f"""
<p>Le plexus pampiniforme est le réseau veineux du cordon, et non une artère ni un lymphatique. Quand ce réseau se dilate à cause du reflux, on parle de varicocèle. Quand il est simplement vu au Doppler, sans dilatation palpable, le chapitre refuse de le mettre dans le même panier opératoire. [S1]</p>
<p>Trois mots voisins prêtent à confusion et doivent rester séparés. « Varice » tout court ne dit pas le lieu. « Varicocèle secondaire » ajoute une obstruction, souvent rénale gauche. « Récidive » suppose qu’une cure a déjà eu lieu et qu’une branche veineuse a été oubliée. Aucun de ces mots n’est un synonyme interchangeable. [S1] [S2]</p>
{w('dx2-p1-plexus',
'Le plexus tire son nom de sa forme en vrille autour du canal déférent et de l’artère.',
'Le sang testiculaire y ralentit, échange de la chaleur, puis remonte par la veine spermatique interne.',
'Exemple : à gauche, cette veine entre dans la veine rénale, ce qui allonge la colonne de sang et favorise le reflux. [S1]',
'Le piège de vocabulaire est d’appeler varicocèle toute grosse bourse, y compris une hydrocèle.',
'Source [S1].')}
<p>La définition de l’EAU est fonctionnelle. Elle exige deux éléments ensemble : la dilatation anormale et le reflux. Une grosse veine sans reflux démontré, ou un reflux sans conséquence clinique, ne remplissent pas à eux seuls le cadre de la forme que l’on opère. [S1]</p>
""",
2: f"""
<p>Il faut lire ensemble deux dénominateurs qui ne se recouvrent pas. La revue romande parle d’environ 15 % dans la population générale et d’un doublement chez les hommes déjà infertiles. L’EAU parle de 14 à 20 % des adolescents, avec une incidence semblable chez l’adulte. Le doublement chez les infertiles ne veut pas dire que 30 % des adolescents sont infertiles : calcul dérivé, si 15 % doublent, on obtient 30 % parmi les hommes infertiles, pas dans la cour de récréation. [S1] [S2]</p>
<p>La géographie suisse chiffrée manque. Ni l’OFS, ni l’Obsan, ni un registre cantonal n’ont été ouverts pour cette entité le 9 novembre 2026. On ne fabrique donc pas un taux genevois ou zurichois. Le seul ancrage suisse lu est la synthèse romande de 2015. [S2]</p>
{w('dx2-p2-temps',
'L’effet défavorable augmente avec la durée d’exposition au reflux.',
'Plus l’adolescent garde un grade II ou III, plus le volume et, plus tard, le sperme ont le temps de se dégrader. Environ 20 % auront un problème de fertilité, pas 100 %. [S1]',
'Exemple : un garçon de treize ans vu tôt n’a pas, pour cette seule raison, une indication plus pressante qu’un jeune de dix-sept ans. Le chapitre le dit explicitement. [S1]',
'Le piège de santé publique est de transformer un dépistage en file opératoire.',
'Source [S1].')}
<p>La mortalité n’est pas l’enjeu lu. Le coût discuté est celui des cures inutiles, des hydrocèles postopératoires et des consultations de fertilité plus tard. Le dépistage pubertaire avec traitement systématique reste controversé quant à la paternité finale. [S1]</p>
""",
3: f"""
<p>On peut suivre la cascade sans sauter d’étage. D’abord l’anatomie : la veine gauche s’abouche haut, dans la veine rénale, et la colonne sanguine est longue. Ensuite la puberté augmente le débit. Puis le reflux s’installe et le plexus se dilate. Enfin la chaleur, le manque d’androgènes locaux et les métabolites entretiennent l’apoptose, le volume baisse, FSH et LH montent, l’inhibine B baisse. [S1] [S2]</p>
<p>Le lien avec le geste est direct. On ne refroidit pas le scrotum avec un médicament dans le chapitre lu. On coupe le reflux, par ligature ou par occlusion, pour retirer la cause de la chaleur et de la stase. L’artère, elle, mesure environ 0,5 mm à l’anneau : elle n’est pas la cible, et c’est pourquoi le grossissement fait partie de la correction, non de l’esthétique. [S1]</p>
{w('dx2-p3-apoptose',
'L’apoptose est une mort cellulaire programmée, ici déclenchée dans le tube séminifère.',
'Le sang refluxé chauffe le testicule, prive localement d’androgènes et apporte des métabolites. Les cellules germinales meurent, le volume clinique diminue.',
'Exemple histologique cité : dégâts sévères chez 20 % des adolescents atteints, anomalies chez 46 %, aspect proche de celui des hommes infertiles. [S1]',
'Le piège est d’invoquer une liste de gènes que la page ne nomme pas.',
'Source [S1].')}
<p>La revue ajoute l’hypoxie de stase et les métabolites rénaux, ce qui rejoint le trajet anatomique gauche sans contredire l’EAU. Quand le mécanisme est un thrombus tumoral, la cascade commence par l’obstacle, pas par une valve pubertaire, et la thérapeutique qui corrige est celle de la tumeur. [S2] [S1]</p>
""",
4: f"""
<p>Après les deux urgences, masse rétro-péritonéale et bourse aiguë, la démarche revient aux formes fréquentes. La varicocèle pubertaire gauche est la plus commune. L’hydrocèle et la spermatocèle sont nommées par la revue comme tuméfactions fréquentes, mais le signe lu qui appartient en propre à la varicocèle reste le paquet veineux qui roule et qui s’efface allongé. [S2]</p>
<p>Un quatrième piège est quantitatif. Une asymétrie unique, même supérieure à 2 mL et à 20 %, peut être une puberté décalée. La conduite n’est pas le bloc : c’est la seconde mesure à six mois. Confondre ce délai avec de la négligence, c’est inventer une urgence que le chapitre ne écrit pas. [S1]</p>
{w('dx2-p4-ordre',
'L’ordre annoncé est la gravité d’abord, la fréquence ensuite.',
'On ne commence pas par le grade cosmétique. On commence par ce qui peut cacher une tumeur ou une ischémie.',
'Exemple : varicocèle droit isolé chez un garçon de seize ans, par ailleurs typique. L’échographie abdominale passe avant la discussion microchirurgicale. [S1]',
'Le piège est de sauter l’imagerie parce que le patient a l’âge habituel.',
'Source [S1].')}
""",
5: f"""
<p>D’autres questions changent encore la décision. On demande s’il existe déjà une maladie de l’autre testicule, parce qu’une atteinte controlatérale fait partie des situations où le traitement peut se discuter au cas par cas. On demande si les deux côtés sont palpables, pour la même raison. On demande ce que la famille a compris du chiffre de 20 % : la majorité des adolescents porteurs n’auront pas de problème de fertilité. [S1]</p>
<p>Le contexte suisse lu ne comporte pas de formulaire d’assurance spécifique. On explique néanmoins que la cure n’est pas un vaccin contre l’infertilité et qu’un refus de chirurgie, quand l’indication n’est que faible, reste compatible avec le chapitre. [S1]</p>
{w('dx2-p5-questions',
'Chaque question est là pour une bifurcation, pas pour remplir un dossier.',
'L’âge sépare primaire et secondaire. Le côté sépare le trajet rénal gauche et l’obstacle. L’horaire sépare le reflux et l’inflammation. Le projet de paternité n’existe que chez le plus grand.',
'Exemple : gêne uniquement le soir, disparition allongé, garçon de quinze ans, côté gauche. Le récit colle à la forme primaire. [S2] [S1]',
'Le piège est une check-list sans conséquence sur le geste.',
'Source [S1] [S2].')}
<p>Le drapeau rouge de la douleur brutale impose le 144 si le garçon n’est pas déjà aux urgences, parce qu’on ne traite pas ce récit comme les 2 à 10 % de douleurs de varicocèle. Le drapeau du prépubère impose l’image abdominale le jour même, pas un contrôle dans six mois. [S1]</p>
""",
6: f"""
<p>La manœuvre se détaille. Le garçon est debout, les deux pieds stables. L’examinateur réchauffe ses mains, regarde d’abord sans toucher pour ne pas manquer un grade III visible à distance, puis palpe le cordon au repos, puis pendant un Valsalva vrai, bouche et nez fermés, poussée abdominale. On compare ensuite les volumes, droit puis gauche, avec le même orchidomètre. Allongé, on revérifie que le paquet diminue : s’il reste dur et fixé, on ne conclut pas à un simple reflux. [S1] [S2]</p>
{w('dx2-p6-valsalva',
'La manœuvre de Valsalva augmente la pression dans le thorax et l’abdomen.',
'Cette pression pousse le sang vers le plexus si les valvules cèdent. Sous les doigts, le cordon s’épaissit pendant l’effort et se relâche après.',
'Exemple : palpable seulement pendant cet effort, c’est un grade I. Palpable déjà avant l’effort, c’est un grade II. Visible sans doigt, c’est un grade III. [S1]',
'Le piège est de faire tousser légèrement et d’appeler cela un Valsalva, puis de sous-grader.',
'Source [S1].')}
<p>La valeur diagnostique chiffrée de la palpation n’est pas dans le chapitre. Ce qui est chiffré, c’est le seuil d’hypotrophie, supérieur à 2 mL ou à 20 %, et la nécessité de deux visites. Un orchidomètre et une échographie peuvent différer de quelques millilitres : le chapitre accepte les deux méthodes, sans donner un coefficient de conversion. On ne moyenne pas deux techniques incompatibles pour franchir le seuil de justesse. [S1]</p>
""",
7: f"""
<p><em>7.1 suite</em> Le geste de recherche de la lourdeur est l’interrogatoire minute par minute sur une journée d’école : sac à dos, sport, soirée au lit. Le mécanisme reste la pression hydrostatique. Un signe fonctionnel absent n’innocente pas un grade III vu à l’inspection. [S1] [S2]</p>
<p><em>7.2 suite</em> Pour le volume, le geste est bilatéral et chiffré. On écrit les deux chiffres et la date, parce qu’une phrase « testicule un peu petit » ne permet pas de calculer 20 %. Le mécanisme apoptotique explique pourquoi le côté du reflux est le côté petit, presque toujours le gauche. [S1]</p>
{w('dx2-p7-volume',
'Le volume orchidomètrique est une estimation tactile, l’échographie une mesure d’image.',
'On compare le côté du reflux au côté sain. Au-delà de 2 mL ou de 20 %, et seulement si le constat se répète six mois plus tard, l’hypotrophie devient un critère d’offre opératoire.',
'Exemple déjà calculé : 12 mL contre 8 mL franchit les deux seuils, mais une seule fois ne suffit pas. [S1]',
'Le piège est de déclarer l’hypotrophie sur une photo ou sur le souvenir parental.',
'Source [S1].')}
<p><em>7.3 suite</em> Le syndrome secondaire se reconnaît d’abord par l’âge ou par le côté, pas par un symptôme rénal que la page n’a pas listé. La revue dit seulement qu’un thrombus tumoral venu d’un cancer du rein gauche peut boucher la veine spermatique. L’échographie abdominale part donc de cette possibilité, sans exiger une hématurie pour être prescrite. [S2] [S1]</p>
""",
8: f"""
<p>On peut donc écrire deux portes, et non une seule. La porte « diagnostic » s’ouvre sur la palpation ou la visibilité debout. La porte « traitement fort » s’ouvre seulement sur l’hypotrophie persistante. Mélanger les portes fait échouer la question d’examen la plus classique de ce sujet. [S1]</p>
<p>Ce qui ne suffit toujours pas, même répété : la gêne esthétique seule, la bilatéralité seule, un spermogramme unique chez un garçon trop jeune, une réponse hormonale sans seuil lu. Ces éléments peuvent ouvrir une discussion faible, jamais une obligation. Le panel le formule par « can be considered », ce qui n’est pas la recommandation forte réservée au petit testicule persistant. [S1]</p>
{w('dx2-p8-fort',
'La force de la recommandation fait partie du critère.',
'Forte : informer et offrir la chirurgie pour une hypotrophie de plus de 2 mL ou de 20 % confirmée deux fois. Faible : douleur, autre maladie testiculaire, forme bilatérale palpable, sperme pathologique du plus grand, raison esthétique. [S1]',
'Exemple : grade III bilatéral, volumes égaux, aucune douleur. On peut discuter, on ne doit pas présenter l’opération comme obligatoire.',
'Le piège est de citer « l’EAU recommande d’opérer les grades III » : cette phrase n’est pas dans le chapitre.',
'Source [S1].')}
<p>La page de Dubin et Amelar n’ayant pas livré son tableau dans l’extrait lu, on n’ajoute pas de stade 0 ni de diamètre veineux en millimètres. Si une autre source, plus tard, donne ces seuils, elle devra être lue avant d’être enseignée. [S2]</p>
""",
9: f"""
<p>Prescrire l’échographie se fait en toutes lettres : scrotum, deux volumes, Doppler couleur, trois conditions (couché, debout, Valsalva), et abdomen si l’âge ou le côté l’exigent. On ne écrit pas « écho des bourses » sans la manœuvre, parce que le reflux peut manquer sur un cliché couché. [S1]</p>
<p>Le terme {b('dx2-p9-reflux','reflux')} appartient au Doppler. Il ne se remplace pas par « flux bizarre ». La sévérité de ce reflux a été corrélée aux dégâts testiculaires dans les travaux cités par le chapitre, sans qu’un grade doppler numéroté ne soit reproduit dans la page ouverte. On ne plaque donc pas une classification de Sarteschi ou d’un autre auteur non lu. [S1]</p>
{w('dx2-p9-reflux',
'Le reflux est un sang qui redescend dans le plexus au lieu de monter.',
'Le Doppler couleur le montre quand la manœuvre pousse le flux vers le testicule. Couché, il peut disparaître, d’où les trois positions.',
'Exemple : reflux isolé, palpation vide. Le chapitre classe cela en forme infraclinique, pas en grade I. [S1]',
'Le piège de compte rendu est une conclusion « varicocèle significative » sans dire si la veine était palpable.',
'Source [S1].')}
<p>Cas discordant : la clinique voit un grade II, l’échographie ne retrouve pas de reflux ce jour-là. On ne nie pas l’examen debout, qui reste le gold standard clinique, et on peut répéter le Doppler dans de bonnes conditions plutôt que d’annuler le diagnostic palpé. Cas limite : volumes à 1 mL près du seuil, une seule fois. On attend six mois. Cas concordant : grade III, différence confirmée, reflux net. L’offre opératoire devient cohérente. [S1]</p>
<p>Aucune image de patient sous licence CC0, CC BY ou CC BY-SA n’a été téléchargée ni annotée le 9 novembre 2026. Le schéma du point 9 reste didactique. L’IRM et le scanner ne sont pas les examens de la varicocèle primitive dans le chapitre. [S1]</p>
""",
10: f"""
<p>On peut réécrire l’arbre avec des chiffres, pour qu’il soit utilisable un soir de garde. Si la douleur a commencé net et s’accompagne de nausée, alors ce n’est pas cet arbre. Si l’âge est inférieur à dix ans ou si seul le côté droit est pris, alors échographie abdominale d’abord. Si la palpation debout est négative, alors pas de cure pour un reflux d’image. Si deux mesures à six mois montrent plus de 2 mL ou plus de 20 % d’écart, alors offre de cure avec loupe ou microscope et épargne lymphatique. Si aucune de ces branches n’est vraie, alors surveillance, et spermogramme seulement chez le plus grand. [S1]</p>
{w('dx2-p10-cas',
'Un cas tient l’arbre entier.',
'Garçon de quatorze ans, grade II gauche, droite 14 mL, gauche 9 mL aujourd hui. Écart de 5 mL et de 5/14, soit environ 36 %, calcul dérivé. Une seule visite : on ne opère pas. On revoit à six mois. Si l’écart reste au-dessus des deux seuils, on offre la cure.',
'Le piège est d’additionner le grade II et le premier écart pour « faire une indication forte » le jour même.',
'Source [S1].')}
<p>La branche faible ne se dessine pas comme une obligation. Douleur, bilatéralité palpable, testicule controlatéral malade, sperme altéré du grand adolescent, gêne visible : chacune peut justifier une discussion, et le patient doit entendre que la recommandation est faible. [S1]</p>
""",
11: f"""
<p>Le conseil avant une cure tient en quelques phrases que l’on peut dire aux parents. Le volume peut rattraper, en moyenne 76,4 % des séries de la méta-analyse citée, entre 52,6 % et 93,8 %, mais une part de ce gonflement est parfois de l'œdème. La concentration spermatique s’améliore dans les essais contre l’observation, sans que la paternité soit un acquis. La varicocèle disparaît dans 85,1 % à 100 % des études retenues. Une hydrocèle est la complication la plus citée, et elle devient rare si les lymphatiques sont respectés. La douleur, si elle existait, peut rester dans un cas sur cinq. [S1]</p>
<p>Le choix du niveau de ligature se justifie à voix haute. Sous l’anneau, au microscope, on voit mieux l’artère de 0,5 mm et les lymphatiques, au prix de plus de veines à lier. Au-dessus, en cœlioscopie ou à ciel ouvert, les veines sont moins nombreuses, et sacrifier l’artère n’améliore pas le rattrapage tout en augmentant la récidive si l’on s’obstine à l’épargner sans raison. Le panel ne couronne aucune des deux. L’injection de bleu isosulfan dans le scrotum ou le testicule a été proposée pour colorer les lymphatiques lors des abords hauts. [S1]</p>
{w('dx2-p11-radio',
'L’occlusion radiologique bouche la veine spermatique de l’intérieur, par sclérose.',
'La voie rétrograde descend depuis une veine centrale. La voie antérograde pique plus près du scrotum. Les deux épargnent en principe les lymphatiques et peuvent éviter une anesthésie générale.',
'Exemple de limite : l’irradiation est moins contrôlable dans la technique antérograde, ce qui compte chez un adolescent. [S1]',
'Le piège est de présenter la radio comme sans conséquence parce qu’elle évite la cicatrice.',
'Source [S1].')}
<p>Forme compliquée locale : l’hydrocèle après section lymphatique. Elle n’est pas une urgence minute, mais elle se cherche à la visite de contrôle, parce qu’elle concerne jusqu’à 40 % des cures qui ne respectent pas les lymphatiques. On n’y répond pas par un nouvel anti-reflux aveugle. [S1]</p>
<p>Forme non compliquée : mesures générales d’abord, c’est-à-dire l’explication et la surveillance, parce que la plupart des garçons n’ont pas d’indication forte. Ensuite seulement, si les critères sont là, la ligature dans l’ordre anatomique : voir l’artère, voir les lymphatiques, lier les veines. Cet ordre protège la fonction que l’on prétend sauver. [S1]</p>
<p>Aucun antalgique, aucune héparine, aucune veino-active n’a de dose dans cette monographie. Le corpus AIPS local manquait le 9 novembre 2026, et les pages swissmedicinfo ouvertes ce jour-là concernaient d’autres molécules, sans lien avec la varicocèle. Écrire un nom de marque serait inventer. [S1]</p>
<p>La sortie de l’hôpital, pour une cure élective, n’a pas de critère chiffré dans le chapitre. On peut au moins exiger, un par un : réveil sans douleur scrotale aiguë inexpliquée, pansement sec, consignes de consultation si la bourse regonfle ou si la douleur devient brutale, et rendez-vous de contrôle du volume. Le sport et la date de retour en classe ne sont pas fixés par la page lue. [S1]</p>
<p>Surveillance chiffrée : à six mois pour une asymétrie douteuse ; après cure, recherche clinique de disparition et d’hydrocèle ; réintervention seulement si la récidive est palpable et que l’asymétrie stagne ou que la plainte continue. Le seuil d’arrêt n’est pas une toxicité médicamenteuse, puisqu’il n’y a pas de médicament de fond. [S1]</p>
""",
12: f"""
<p>Au niveau primaire, on peut dire aux familles ce que l’on ne fera pas : pas de suspension scrotale préventive chez l’enfant sain, pas de dépistage scolaire suivi d’une opération automatique, pas d’échographie « pour voir » chez un garçon sans bourse anormale. Ces non-gestes découlent du caractère controversé du dépistage avec traitement. [S1]</p>
<p>Au niveau secondaire, le seuil d’action est concret. Devant un paquet veineux, on grade debout. Devant un écart de volume, on mesure deux fois à six mois. Devant un âge inférieur à dix ans ou un côté droit seul, on échographie l’abdomen. Ces trois seuils évitent autant l’excès que l’oubli. [S1]</p>
<p>Au niveau tertiaire, après la cure, prévenir l’hydrocèle c’est avoir choisi l’épargne lymphatique, et prévenir l’angoisse c’est avoir annoncé les 20 % de douleurs qui peuvent rester et l’inconnu sur la paternité. Aucun calendrier vaccinal ne s’y rattache. [S1]</p>
{w('dx2-p12-depist',
'Un dépistage n’a de sens que si le traitement des cas trouvés améliore un résultat qui compte.',
'Ici, le résultat qui compterait est la paternité. Le chapitre dit que ce bénéfice est controversé et que l’effet ultime est inconnu. [S1]',
'Exemple : découvrir un grade I à une visite de treize ans ne déclenche pas une cure. Cela déclenche, au plus, une surveillance.',
'Le piège est de confondre « fréquent » et « à opérer ».',
'Source [S1].')}
""",
13: f"""
<p>On peut répéter la décision sans ouvrir de fenêtre. Debout d’abord. Abdomen si l’âge ou le côté déraillent. Deux mesures avant de parler d’hypotrophie. Lymphatiques respectés si l’on coupe. Paternité non promise.</p>
<p>Le chiffre 14 à 20 % décrit les adolescents, pas les garçons de huit ans. Le chiffre 20 % de problèmes de fertilité n’est pas un risque vital. Le chiffre 40 % d’hydrocèles punit la section des lymphatiques, pas la maladie elle-même.</p>
""",
14: f"""
<p>Question : un grade III à volumes égaux chez un garçon de quinze ans est-il une indication forte ? Réponse : non. Le grade visible pose le diagnostic, pas l’obligation d’opérer. [S1]</p>
<p>Question : quelle est la différence entre 76,4 % et 20 % dans ce chapitre ? Réponse : 76,4 % est la proportion moyenne de rattrapage de croissance après cure dans une méta-analyse, fourchette 52,6 à 93,8 %. Vingt pour cent est la part des adolescents porteurs qui auront un problème de fertilité, et c’est aussi, dans une autre phrase, la part des douleurs qui persistent après cure. Il ne faut pas additionner ces 20 %. [S1]</p>
<p>Question : l’odds ratio de 0,08 concerne quoi ? Réponse : la baisse d’hydrocèle quand la chirurgie épargne les lymphatiques, avec un intervalle de confiance à 95 % de 0,01 à 0,67. [S1]</p>
<p>Question : pourquoi l’intervalle de confiance de la comparaison ouvert contre cœlioscopie va-t-il de 0,13 à 2,84 ? Réponse : parce qu’aucune des deux techniques n’a montré de supériorité stable. [S1]</p>
<p>Question : peut-on promettre la disparition de la douleur parce que certaines séries dépassent 90 % de soulagement ? Réponse : non, pas sans citer aussi les 20 % de persistance. Les deux données sont dans le même chapitre et ne sélectionnent pas les mêmes patients. [S1]</p>
<p>Question : une récidive doppler sans paquet palpable et avec un volume qui a rattrapé se réopère-t-elle ? Réponse : non. On ne traite la récidive que si elle est clinique et que l’asymétrie ne bouge pas, ou que les symptômes restent. On change alors de technique. [S1]</p>
<p>Question : le bleu isosulfan sert-il à colorer l’artère ? Réponse : non, il a été proposé pour voir les lymphatiques lors des abords supra-inguinaux. [S1]</p>
<p>Question : la varicocèle de l’homme infertile dans la revue romande autorise-t-elle à opérer tout adolescent ? Réponse : non. Le doublement de fréquence chez les infertiles décrit une association, pas une indication pédiatrique automatique. [S2] [S1]</p>
<p>Question : où est le numéro Swissmedic du traitement ? Réponse : il n’y en a pas dans cette monographie, parce qu’aucun médicament de fond n’a été relu dans une information professionnelle suisse. La correction est mécanique. [S1]</p>
""",
    }
