#!/usr/bin/env python3
"""DX.1 Maladie de Basedow."""
from rendre_dx import rendre, P, S
from moteur import btn

ess = P(
    "La maladie de Basedow est une thyrotoxicose par fabrication : un anticorps stimule le récepteur de la thyréostimuline. "
    "Goitre diffus et orbitopathie rendent souvent la scintigraphie inutile. "
    "On traite par carbimazole dans la fourchette suisse, et par propranolol si le cœur va vite. "
    "On explique l'agranulocytose avant la première prise. Ce n'est pas une crise tant que le score reste bas.",
    S(2, 8, 10),
)

points = {
"p1": P("Basedow est une hyperthyroïdie auto-immune par stimulation du récepteur, pas une fuite de stock. Le ", btn("w-def", "nom et les frontières"), " évite de traiter une thyroïdite comme un Basedow.", S(2)),
"p2": P("Elle touche surtout des femmes jeunes. Les ", btn("w-epi", "chiffres"), " viennent de la revue lausannoise et ne classent pas ce diagnostic parmi les dix par une prévalence suisse.", S(1)),
"p3": P("L'anticorps anti-récepteur pousse la glande et peut pousser l'orbite. La ", btn("w-physio", "chaîne"), " va de l'anticorps au chiffre, puis au choix du thionamide.", S(2)),
"p4": P("La démarche confirme la thyrotoxicose, reconnaît le tableau, dose l'anticorps si le traitement médical est prévu, et écarte la crise. Les ", btn("w-dem", "sept pas"), " tiennent sur une page.", S(2)),
"p5": P("On cherche l'arrêt récent d'un thionamide, un contraste, une grossesse, une biotine. Les ", btn("w-ana", "questions"), " et ce ", btn("w-dire", "qu'on dit"), " changent l'ordonnance.", S(1, 7, 8)),
"p6": P("Goitre diffus, souffle, rétraction palpébrale, tremblement fin. L'", btn("w-ex", "examen"), " et l'", btn("w-oeil", "œil et la grossesse"), " suffisent souvent à orienter quand les hormones sont hautes.", S(2)),
"p7": P("Le syndrome est une thyrotoxicose de fabrication : thyréostimuline basse, thyroxine libre haute, parfois triiodothyronine libre haute alors que la thyroxine libre est encore limite. Le ", btn("w-syn", "profil"), " le distingue de la basse T3 et de la biotine.", S(1, 2, 7)),
"p8": P("Le diagnostic positif repose sur la clinique et l'anticorps. La sensibilité et la spécificité lues, et le ", btn("w-pos", "seuil de décision"), ", sont ceux de 2016.", S(2)),
"p9": P("L'anticorps anti-récepteur est l'examen de première ligne quand on veut un traitement médical. La scintigraphie reste pour le doute. Le ", btn("w-examens", "choix"), " est écrit.", S(2)),
"p10": P("On écarte d'abord la crise, puis on confirme Basedow plutôt qu'un nodule ou une thyroïdite. L'", btn("w-arbre", "arbre"), " et les ", btn("w-dd", "diagnostics voisins"), " ne commencent pas par l'iode radioactif."),
"p11": P("Carbimazole, numéro 21037, et propranolol, numéro 47025, sont les deux spécialités du début. Le ", btn("w-ttt", "schéma"), ", l'", btn("w-sang", "agranulocytose"), " et les ", btn("w-situ", "situations particulières"), " donnent les plafonds.", S(8, 10)),
"p12": P("On prévient la crise en ne stoppant pas le médicament d'un coup, et en évitant le contraste non préparé. La ", btn("w-prev", "prévention"), " et le ", btn("w-suivi-b", "calendrier"), " tiennent le suivi.", S(1, 2)),
"p13": P("Fabrication, pas fuite. Anticorps utile. Carbimazole plafonné. Fièvre égale arrêt. Durée citée sans la moyenner. Le ", btn("w-cles", "rappel"), " sert le jour de l'examen.", S(2, 8)),
"p14": P("Le piège est le thionamide dans une thyroïdite, ou l'iode nucléaire chez ce patient. Le ", btn("w-pieges", "liste"), ", le ", btn("w-cas", "cas de l'allaitement"), " et la ", btn("w-cas2", "rechute"), " ferment la leçon.", S(5, 12)),
}

fens = []

def add(pid, wid, titre, *paras):
    fens.append((pid, wid, titre, "".join(paras)))

add("p1", "w-def", "Définition et frontières",
P("La maladie de Basedow est la cause auto-immune la plus classique de thyrotoxicose par excès de fabrication. Un anticorps dirigé contre le récepteur de la thyréostimuline active la cellule thyroïdienne. La glande grossit de façon diffuse, le sang y circule fort, et les hormones libres montent. La thyréostimuline s'effondre par rétrocontrôle. Ce n'est pas une destruction : le stock n'est pas simplement lâché, il est renouvelé.", S(2)),
P("On la distingue de trois voisins qui donnent le même profil hormonal. Le nodule autonome et le goitre multinodulaire toxique fabriquent aussi, mais de façon focale, sans anticorps stimulant et sans orbitopathie. La thyroïdite destructrice lâche le stock, la fixation isotopique est basse, le cou est souvent douloureux au début, et le thionamide ne sert pas. La prise de lévothyroxine et la biotine imitent le chiffre. La première a une thyroïde petite et une fixation nulle. La seconde a une clinique pauvre et un contrôle normalisé après l'arrêt du complément.", S(2, 7)),
P("Le mot hyperthyroïdie, dans la revue de 2010, couvre l'excès d'hormone par production, par libération ou par apport exogène. Basedow n'occupe que la première case. Traiter les trois cases de la même façon est l'erreur que cette leçon corrige.", S(1)),
P("L'orbitopathie appartient à la même maladie autoimmune. Une rétraction palpébrale, une rougeur, une diplopie orientent. Une baisse de vision sort du cabinet. Ce cours ne récite pas un score d'activité orbitaire : le texte européen correspondant n'a pas été ouvert. Il dit seulement que l'œil menacé s'adresse, et que l'orbitopathie avec un goitre diffus rend le diagnostic de Basedow probable sans scintigraphie.", S(2)),
)

add("p2", "w-epi", "Qui est touché",
P("Dans l'enquête américaine citée par la revue lausannoise, les formes franches d'hypothyroïdie et d'hyperthyroïdie étaient chacune inférieures à 1 % chez des adultes sans maladie connue. Basedow, au sein de l'hyperthyroïdie, est plus fréquent chez les femmes de 20 à 40 ans. Le goitre multinodulaire et l'hyperthyroïdie en général augmentent avec l'âge, et le tabac renforce l'hyperthyroïdie. On ne déduit pas de ces phrases une part suisse de Basedow parmi les dix diagnostics de la leçon : aucun texte lu ne la donne.", S(1)),
P("La gravité ne vient pas de la fréquence. Elle vient de la crise si le médicament est arrêté, si un contraste est injecté, ou si une infection survient sur une thyrotoxicose non contrôlée. La mortalité des séries modernes de crise, 8 % à 25 %, ne s'applique pas à la femme jeune stable du cabinet. Elle rappelle pourquoi on ne banalise pas l'arrêt du carbimazole.", S(2)),
P("La rémission à long terme sous antithyroïdien est citée à 30 à 40 % par la revue, avec un suivi prolongé à cause des récidives, de l'hypothyroïdie secondaire et de l'orbitopathie qui peut bouger indépendamment des hormones. Ce n'est pas un échec de nommer une rechute. C'est l'histoire naturelle lue.", S(1)),
)

add("p3", "w-physio", "De l'anticorps à l'ordonnance",
P("L'anticorps anti-récepteur se lie au même récepteur que la thyréostimuline et l'active. La glande produit plus de thyroxine et de triiodothyronine. L'hypophyse freine. Le dosage montre une thyréostimuline basse et des hormones libres hautes. Parce que la glande hyperactive fabrique relativement plus de triiodothyronine, celle-ci peut dépasser sa borne alors que la thyroxine libre est encore proche de la sienne. C'est l'inverse d'une prise de lévothyroxine, où la thyroxine domine.", S(2)),
P("Le récepteur est aussi en cause dans l'orbite et parfois dans le derme prétibial. Le traitement qui baisse les hormones ne garantit pas que l'œil se calme. La revue le dit : l'orbitopathie a ses propres phases. On ne promet pas à la patiente que le carbimazole guérit les yeux.", S(1)),
P("Le carbimazole bloque la fabrication en amont, via son métabolite actif, le thiamazole. Il ne vide pas le stock déjà constitué. Les symptômes mettent donc des jours à céder, et le propranolol couvre le cœur pendant ce délai. Il ne bloque pas non plus une thyroïdite : il n'y a rien à empêcher de fabriquer si la glande fuit. D'où l'importance de nommer le mécanisme avant l'ordonnance.", S(8)),
P("L'iode minéral, donné à une glande de Basedow qui n'est pas bloquée par un thionamide, peut servir de substrat. C'est pourquoi, dans la crise, l'iode vient au moins une heure après le thionamide. Hors crise, on n'ajoute pas d'iode. Le comprimé nucléaire est contre-indiqué dans Basedow.", S(5, 12)),
)

add("p4", "w-dem", "Sept pas",
P("Pas 1. Constantes. Température, pouls, conscience, vomissements, ictère, crépitants. S'ils dessinent une défaillance, on quitte ce chapitre pour la crise et on calcule le score entier. Une femme jeune tachycarde mais lucide, apyrétique, sans vomissement, reste dans Basedow simple.", S(5)),
P("Pas 2. Profil. Thyréostimuline basse, thyroxine libre haute. Si la thyroxine libre est normale, on demande la triiodothyronine libre avant de conclure. On note les bornes du laboratoire.", S(1)),
P("Pas 3. Clinique de fabrication diffuse. Goitre homogène, souffle, yeux. Douleur vive du cou : on s'arrête, ce n'est pas le pas suivant.", S(2)),
P("Pas 4. Anticorps anti-récepteur si l'on envisage douze à dix-huit mois de traitement médical. Il servira de base et, à l'arrêt, de pronostic de rechute.", S(2)),
P("Pas 5. Scintigraphie seulement si le tableau n'est pas typique : pas d'orbitopathie, thyroïde nodulaire, anticorps négatif. Pas chez la femme enceinte ni allaitante.", S(2)),
P("Pas 6. Ordonnance. Propranolol si la fréquence gêne. Carbimazole dans la fourchette, avec la phrase sur la fièvre. Pas d'iode.", S(8, 10)),
P("Pas 7. Contrôle. Clinique rapprochée, formule selon l'âge et la dose, hormones pour baisser ensuite la dose par paliers. Date écrite avant le départ.", S(8)),
)

add("p5", "w-ana", "Anamnèse",
P("Début en semaines ou mois, amaigrissement avec appétit conservé, chaleur, tremblement, irritabilité, selles fréquentes, palpitations, règles irrégulières. Un début en quatre jours avec douleur d'oreille fait chercher De Quervain, pas Basedow.", S(1)),
P("Médicaments. Un complément pour les cheveux peut fausser le tube en plus d'un vrai Basedow : on le fait arrêter, on ne retarde pas le traitement si la clinique est riche. Un produit de contraste récent est un facteur de crise. Une lévothyroxine déjà prescrite fait vérifier qu'il n'y a pas un double apport.", S(2, 7)),
P("Grossesse et allaitement avant toute chose. Avis spécialisé si la patiente est enceinte. Allaitement : plafond 20 mg par jour de carbimazole, prises après la tétée. Projet de grossesse : on le dit, parce que le médicament passe le placenta.", S(1, 8)),
P("Antécédent d'agranulocytose, de pancréatite après thionamide, d'hépatite sévère, de compression trachéale : contre-indications lues. On ne réintroduit pas le carbimazole dans ces cas.", S(8)),
)

add("p6", "w-oeil", "Œil, grossesse, et ce qu'on n'invente pas",
P("L'orbitopathie se cherche à chaque visite, pas seulement au diagnostic. On demande la douleur à l'orbite, la rougeur, la diplopie, la vision des couleurs, une baisse récente. Une rétraction isolée sans baisse de vision se note et se revoit. Une baisse de vision, un œil figé, une cornée exposée : adressage ophtalmologique le jour même. On ne donne pas de sélénium ni une dose de corticoïde orbitaire : ces schémas n'ont pas été lus dans cette session. On ne les fabrique pas pour avoir l'air complet."),
P("Le tabac aggrave l'hyperthyroïdie dans la phrase de la revue et il est raisonnable de le faire arrêter, surtout si l'œil est atteint. On le dit sans attribuer à la revue un pourcentage de risque oculaire qu'elle n'a pas écrit dans l'extrait lu.", S(1)),
P("Grossesse. On confirme ou on exclut une grossesse avant la scintigraphie et avant de parler d'iode radioactif. Le carbimazole traverse le placenta. Une posologie inadaptée peut entraîner un goitre et une hypothyroïdie chez l'enfant à naître, et un faible poids de naissance. La phrase est celle de l'information professionnelle. Toute atteinte thyroïdienne chez une femme enceinte justifie un avis spécialisé. Le dépistage de toutes les femmes n'est pas la règle : seulement en début de grossesse si le risque est augmenté, antécédent, maladie autoimmune, irradiation, fausses couches, infertilité.", S(1, 8)),
P("Sans borne locale, l'ATA de 2017 retient environ 4,0 mU/l et l'ETA de 2014 retient 2,5 mU/l, 3,0 mU/l et 3,5 mU/l selon le trimestre. La revue de 2010 demande en outre un avis spécialisé.", S(1)),
P("Après l'accouchement, une thyrotoxicose peut être un Basedow ou une thyroïdite du post-partum. La douleur absente et la fixation basse orientent vers la thyroïdite. L'anticorps anti-récepteur et l'œil orientent vers Basedow. On ne reprend pas automatiquement l'ancien carbimazole le jour de la sortie de maternité sans ce tri, et on respecte le plafond de 20 mg si l'allaitement continue.", S(2, 8)),
P("Enfant qui accompagne une mère traitée. On ne donne pas au enfant le comprimé de la mère. Si l'enfant lui-même a un Basedow, avant 12 ans le plafond est 30 mg, avant 3 ans le spécialiste décide. Ce n'est pas le dossier de la mère.", S(8)),
)

add("p6", "w-ex", "Examen",
P("Pouls et pression. La tachycardie sinusale est habituelle. Une fibrillation fait monter la vigilance, surtout après 60 ans, et justifie le propranolol si la pression le permet. Une température fait calculer le score, pas augmenter le carbimazole de mémoire.", S(10, 5)),
P("Cou. Volume diffus, consistance souple, thrill ou souffle. Un nodule dominant change le plan : échographie classée et souvent scintigraphie. Une douleur à la palpation n'appartient pas à Basedow.", S(2, 6)),
P("Yeux. Rétraction, asynergie oculo-palpébrale, rougeur conjonctivale, diplopie, baisse d'acuité. On demande à la patiente si les couleurs ont changé ou si la vision a chuté. Au moindre doute visuel, adressage le jour même. On ne classe pas l'œil avec un score non lu."),
P("Mains. Tremblement fin, paumes chaudes. Peau. Parfois myxœdème prétibial, rare, à ne pas prendre pour une insuffisance cardiaque. Réflexes vifs. On pèse le patient : le poids de départ sert de contrôle."),
)

add("p7", "w-syn", "Profil et syndromes voisins",
P("Profil de Basedow non compliqué : thyréostimuline basse ou indétectable, thyroxine libre haute, triiodothyronine libre haute. Au Centre hospitalier universitaire vaudois en 2010, la thyroxine libre de référence allait de 8 à 22 pmol/l et la thyréostimuline de 0,2 à 3,5 mU/l. Une valeur au-dessus de la borne locale est haute, même si un autre laboratoire aurait dit autrement. On écrit la borne à côté du chiffre.", S(1)),
P("Thyroxine libre normale et triiodothyronine libre haute, thyréostimuline basse : thyrotoxicose à T3, encore compatible avec Basedow. On ne rassure pas sur la seule thyroxine libre.", S(2)),
P("Hormones très hautes et clinique vide : biotine jusqu'à preuve du contraire. On arrête le complément et on recontrôle au moins deux jours plus tard, le texte australien disant 72 heures. On ne commence pas le carbimazole sur ce seul décalage.", S(7)),
P("Thyroxine libre haute, thyréostimuline normale, patient sous amiodarone sans amaigrissement : ce n'est pas Basedow. C'est l'effet du médicament. Basedow sous amiodarone existe, mais la thyréostimuline est alors effondrée et la triiodothyronine libre monte, sur un terrain qui peut être un Basedow latent : c'est le type 1, traité ailleurs dans la leçon.", S(4)),
P("Triiodothyronine basse en réanimation : syndrome de basse T3, pas Basedow. On ne donne pas de carbimazole pour une triiodothyronine basse.", S(3)),
)

add("p8", "w-pos", "Diagnostic positif",
P("Devant une thyrotoxicose franche, un goitre diffus et une orbitopathie, la recommandation de 2016 juge le diagnostic de Basedow probable et l'enquête étiologique supplémentaire inutile. L'anticorps anti-récepteur confirme et sert de ligne de base.", S(2)),
P("Les dosages récents cités ont une sensibilité de 96 à 97 % et une spécificité de 99 % pour Basedow dans la thyrotoxicose franche. Un dosage négatif dans un tableau typique est rare. Un dosage négatif sans orbitopathie et avec des nodules n'élimine pas un nodule toxique : il rend Basedow moins probable.", S(2)),
P("À la fin d'un traitement de 12 à 18 mois, un anticorps encore haut annonce une rechute dans 80 à 100 % des cas selon les séries citées. Un anticorps bas ou indétectable laisse une rechute de l'ordre de 20 à 30 %. On ne promet pas la guérison. On planifie le contrôle après l'arrêt, plus rapproché les premiers mois.", S(2)),
P("La revue suisse parle d'une rémission à long terme chez 30 à 40 % des patients. Les deux chiffres ne se contredisent pas : l'un décrit le taux de rémission globale, l'autre le risque selon l'anticorps à l'arrêt. On les cite tous les deux.", S(1, 2)),
)

add("p9", "w-examens", "Examens",
P("Premier examen utile après les hormones : l'anticorps anti-récepteur, quand le traitement médical est le plan. Il coûte moins et répond plus vite qu'une scintigraphie dans l'étude de modélisation citée en 2016, sans que ce cours en fasse une obligation comptable. Si le dosage n'est pas disponible, la scintigraphie reprend la place.", S(2)),
P("Scintigraphie. Basedow : fixation diffuse. Nodule toxique : un foyer et le reste éteint. Goitre multinodulaire : plusieurs foyers. Thyroïdite : fixation basse. On ne la demande pas si l'œil et le goitre diffus ont déjà nommé la maladie. On ne l'injecte pas à une femme enceinte.", S(2)),
P("Échographie. Elle n'est pas nécessaire pour nommer Basedow typique. Elle le devient s'il y a un nodule. On le classe alors de TR1 à TR5, toutes catégories gardées, avec les seuils de cytoponction de 2017 : 2,5 cm pour TR3, 1,5 cm pour TR4, 1,0 cm pour TR5. Un nodule dans un Basedow peut être un cancer. L'autonomie et la malignité sont deux questions.", S(6)),
P("Formule sanguine avant le carbimazole, surtout si la dose dépassera 40 mg par jour et si le patient a plus de 40 ans : contrôle hebdomadaire six semaines. Tout patient, même jeune, est instruit d'arrêter devant fièvre, angine ou aphtes, sans attendre le rendez-vous.", S(8)),
P("Bilan hépatique si le contexte le suggère. L'insuffisance hépatique sévère contre-indique le carbimazole. On ne demande pas un bilan exhaustif à une femme jeune par réflexe, mais on ne rate pas un ictère.", S(8)),
)

add("p10", "w-arbre", "Arbre",
P("Entrée : thyrotoxicose clinique et biologique. Sortie immédiate vers la crise si le score atteint 45 ou si le critère japonais TS1 ou TS2 est rempli, ou si le jugement clinique dit défaillance même entre 25 et 44.", S(5)),
P("Sinon : yeux et goitre diffus. Oui : Basedow, anticorps, traitement médical ou discussion d'un traitement radical avec le spécialiste. Non : palpation nodulaire ou douleur. Nodule : scintigraphie et échographie classée. Douleur et vitesse de sédimentation haute : thyroïdite, pas de carbimazole. Clinique pauvre et hormones extrêmes : biotine, recontrôle.", S(1, 2, 6, 7)),
P("Basedow retenu : bêtabloquant si besoin, carbimazole, éducation, contrôle. À 12-18 mois, on regarde l'anticorps et la thyréostimuline. Négatifs et hormones normales : on peut arrêter et surveiller. Anticorps haut : on discute la poursuite, l'iode radioactif ou la chirurgie. La recommandation ne force pas un seul chemin.", S(2)),
P("Rechute après arrêt. L'information professionnelle dit que l'on peut reprendre le carbimazole, mais qu'il faut envisager un autre traitement, en particulier la chirurgie. On ne présente pas la reprise comme le seul choix, ni la chirurgie comme obligatoire le jour de la rechute.", S(8)),
)

add("p11", "w-ttt", "Traitement et doses",
P("Propranolol Zentiva, numéro 47025. Indication lue : hyperthyroïdie et crises thyréotoxiques. Dose : 10-40 mg, 3 à 4 fois par jour. On ne prend pas la ligne de l'hypertension, dont le plafond est bien plus haut. On baisse ou on arrête quand la fréquence et les hormones se calment. Un asthme sévère fait demander un avis avant un bêtabloquant non sélectif : ce cours ne choisit pas une autre molécule dont la dose thyroïdienne n'a pas été lue.", S(10)),
P("Néo-Mercazole, numéro 21037. On ne le donne qu'après confirmation biologique. Dose initiale 20 à 60 mg par jour selon l'ampleur, en deux ou trois prises, titrée jusqu'à l'euthyroïdie. Puis baisse par paliers de 5 à 15 mg par jour tous les 10 jours, jusqu'à 5 à 20 mg par jour. Plafond adulte et adolescent dès 12 ans : 60 mg par jour. Avant 12 ans : 0,7 à 0,8 mg par kilogramme, plafond 30 mg par jour, et avant 3 ans un spécialiste habitué à cet âge. Durée habituelle écrite : 6 à 18 mois.", S(8)),
P("La revue et la recommandation de 2016 parlent, pour Basedow, de douze à dix-huit mois. On dit au patient les deux formulations. On n'invente pas une durée de neuf mois pour les réconcilier. L'arrêt se tente si les hormones et, pour la recommandation, l'anticorps sont revenus. Après l'arrêt, surveillance : les rechutes à anticorps négatif viennent plutôt plus tard, d'où des contrôles les premiers mois puis plus espacés.", S(1, 2)),
P("Iode préopératoire. La recommandation de 2016 décrit, avant une thyroïdectomie pour Basedow, cinq à sept gouttes de solution de Lugol ou une à deux gouttes de solution saturée, trois fois par jour, une dizaine de jours. Ce n'est pas le comprimé d'iodure de potassium axapharm, numéro 67017, dosé à 130.0 mg pour un accident nucléaire et contre-indiqué dans Basedow. On ne confond pas la préparation opératoire et le blocage nucléaire. Hors bloc et hors crise, pas d'iode.", S(2, 12)),
P("Iode radioactif et chirurgie sont les traitements définitifs cités par la revue quand l'hyperthyroïdie persiste ou quand le thionamide est mal supporté. Ce cours ne donne pas une activité en becquerels : elle n'a pas été lue dans une information professionnelle suisse ouverte pour cette leçon. L'arrêt du carbimazole deux à trois jours avant l'iode radioactif est discuté dans les remarques de 2016. On adresse pour le calcul.", S(1, 2)),
P("Grossesse. Le carbimazole passe le placenta. Une dose inadaptée peut donner un goitre, une hypothyroïdie fœtale et un petit poids de naissance. Toute atteinte chez une femme enceinte va au spécialiste. On cite les seuils de 2014 et de 2017, et le laboratoire prime s'il a les siens.", S(1, 8)),
P("Allaitement. Dose au plus 20 mg par jour, en plusieurs prises, juste après la tétée, information du risque pour l'enfant. Au-dessus, on n'allaite pas sous ce médicament selon la phrase lue.", S(8)),
)

add("p11", "w-sang", "Agranulocytose et autres alertes",
P("L'agranulocytose et l'aplasie peuvent survenir en quelques heures à quelques jours. Des décès sont rapportés. Le pronostic dépend de l'arrêt précoce. Le patient arrête Néo-Mercazole et consulte devant fièvre, malaise, hématomes, saignements, aphtes, angine ou autre infection. On contrôle la formule. L'arrêt précoce peut rendre l'aplasie réversible.", S(8)),
P("La surveillance chiffrée la plus explicite vise les deux premiers mois, les doses au-dessus de 40 mg par jour, et les patients de plus de 40 ans : formule avant traitement, puis chaque semaine pendant six semaines. Elle ne dispense pas le patient jeune d'arrêter devant une angine. Une formule normale la veille n'autorise pas à continuer si la fièvre est là le matin.", S(8)),
P("Autres alertes lues. Vascularite à ANCA, plus classique du propylthiouracile mais décrite aussi sous carbimazole : peau, articulations, rein, poumon, fièvre. Pancréatite aiguë après carbimazole ou thiamazole : contre-indication définitive. Hépatite sévère : contre-indication. Goitre simple, compression trachéale, cancer dépendant de la thyréostimuline, granulopénie déjà sévère : on ne commence pas.", S(8)),
P("Un surdosage prolongé fait l'inverse de Basedow : thyréostimuline haute, goitre qui grossit. On baisse la dose. On ne l'augmente pas en croyant à une résistance.", S(8)),
)

add("p11", "w-situ", "Enfant, sujet âgé, foie",
P("Dès 12 ans, le plafond reste 60 mg par jour, avec une dose de départ au poids, 0,7 à 0,8 mg par kilogramme. Avant 12 ans le plafond tombe à 30 mg, et les données sont dites extrêmement limitées. Avant 3 ans, spécialiste. On n'écrit pas une dose d'adulte sur une ordonnance pédiatrique.", S(8)),
P("Sujet âgé. Aucune adaptation chiffrée obligatoire du carbimazole n'est écrite, mais le cœur dicte le propranolol et la vitesse de la descente. Une fibrillation sur Basedow n'est pas une hyperthyroïdie infraclinique : les hormones libres sont hautes, on traite.", S(8)),
P("Foie léger ou modéré : prudence, demi-vie plus longue. Foie sévère : contre-indication. Rein : prudence et contrôles, sans chiffre d'adaptation lu. On ne divise pas la dose par deux faute d'une phrase qui le dirait.", S(8)),
)

add("p12", "w-prev", "Prévention",
P("Ne pas arrêter le carbimazole parce que les boîtes sont finies ou parce qu'une angine banale a été prise pour une allergie sans formule. L'arrêt brutal est un précipitant de crise. Une vraie angine fébrile, elle, impose l'arrêt et la formule : les deux consignes tiennent ensemble si l'on explique la différence.", S(2, 8)),
P("Produit de contraste et amiodarone chez un Basedow non contrôlé : risque de crise, signalé par la revue pour le goitre multinodulaire et valable ici par le même mécanisme d'iode sur une glande qui fabrique. On prévient le radiologue et le cardiologue.", S(1)),
P("Carte ou consigne écrite : fièvre, angine, aphtes, arrêt, consultation. Proche informé. Femme en âge de procréer : contraception le temps de stabiliser, ou avis immédiat si grossesse.", S(8)),
P("Après rémission, on ne disparaît pas. Contrôles, et retour si les palpitations reviennent. L'œil se surveille même si les hormones sont normales.", S(1)),
)

add("p5", "w-dire", "Ce qu'on dit à la patiente",
P("Votre glande fabrique trop d'hormone parce qu'un anticorps la stimule. Ce n'est pas un cancer du fait de ce diagnostic, et ce n'est pas une infection. Le médicament bloque la fabrication. Il ne vide pas ce qui est déjà dans le sang : les palpitations mettent plusieurs jours à céder. Le propranolol calme le cœur en attendant."),
P("Vous prenez le carbimazole en deux ou trois fois, pas toute la boîte d'un coup. On commencera entre 20 et 60 mg par jour, puis on baissera par paliers de 5 à 15 mg tous les dix jours, jusqu'à une petite dose de 5 à 20 mg. Le plafond est 60 mg par jour. On ne monte pas au-dessus parce qu'un voisin a eu une dose plus haute dans un autre pays.", S(8)),
P("Si vous avez de la fièvre, une angine, des aphtes ou des bleus, vous arrêtez le soir même et vous consultez. Vous ne finissez pas la plaquette. Cet arrêt-là protège. Un arrêt parce que vous vous sentez mieux, sans avis, peut au contraire déclencher une crise. Les deux phrases sont vraies ensemble.", S(8)),
P("Le traitement dure souvent de nombreux mois. L'information professionnelle parle de 6 à 18 mois. Les textes sur Basedow parlent de douze à dix-huit mois. Environ un tiers à quatre dixièmes des patients restent en rémission ensuite, et l'anticorps à l'arrêt aide à prévoir la rechute. Ce n'est pas une note personnelle. On recontrôlera.", S(1, 2)),
P("Si vous allaitez, la dose ne peut pas dépasser 20 mg par jour, prise juste après la tétée. Si la maladie est trop forte pour cette dose, on suspend l'allaitement ou on change de stratégie avec un spécialiste. Si vous êtes enceinte, on ne garde pas le schéma du cabinet : avis spécialisé. Le médicament passe au fœtus.", S(1, 8)),
P("Les yeux peuvent rester gênants même quand les hormones rentrent dans l'ordre. Une baisse de vision, c'est le jour même. Un nodule qu'on découvre se décrit à part, avec une classification échographique complète, pas un mot vague de kyste."),
P("Vous prenez le propranolol trois ou quatre fois par jour, 10 à 40 mg, tant que le cœur va vite. Vous ne le confondez pas avec un traitement de la tension à plus forte dose. Vous ne conduisez pas si vous êtes très ralentie au début. Vous dites si vous avez de l'asthme.", S(10)),
)

add("p14", "w-cas2", "Rechute, deuxième cas",
P("Énoncé. Homme de 46 ans, Basedow traité 14 mois par carbimazole, arrêté il y a quatre mois parce que l'anticorps était devenu indétectable et la thyréostimuline normale. Il revient pour des palpitations. Pouls 104, régulier, pas de fièvre, pas de vomissement. Thyroxine libre de nouveau haute, thyréostimuline basse, anticorps de nouveau présent. Il demande si l'on réopère demain. Il a un nodule de 1,8 cm, solide, hypoéchogène, marge lisse, sans foyer échogène, plus large que haut, déjà vu stable."),
P("Correction. C'est une rechute de fabrication, pas une crise. Fréquence 104 : classe 90 à 109, 5 points. Pas de fièvre utile au score, pas de signe digestif. Total très bas. On ne déclenche pas l'iode de la crise.", S(5)),
P("L'information professionnelle permet de reprendre le carbimazole et demande d'envisager un autre traitement, en particulier la chirurgie. La recommandation de 2016 offre aussi un nouveau cours de thionamide, l'iode radioactif ou la chirurgie. On n'opère pas le lendemain sans préparation et sans discussion. On explique les trois voies. On reprend un bêtabloquant si la fréquence gêne, dans la fourchette 10-40 mg trois à quatre fois.", S(2, 8, 10)),
P("Le nodule. Solide 2 points, hypoéchogène 2, marge lisse 0, pas de foyer 0, plus large que haut 0. Total 4 : TR4. La cytoponction se discute à partir de 1,5 cm. À 1,8 cm, elle est dans la zone. On ne la remplace pas par la scintigraphie, et on ne dit pas que tout nodule de Basedow est bénin. On programme la ponction selon le texte de 2017, en parallèle du traitement de la rechute.", S(6)),
P("On ne donne pas d'iodure nucléaire. On ne promet pas que la reprise du carbimazole évitera une troisième poussée. On fixe un rendez-vous spécialisé pour le choix définitif, et une consigne d'agranulocytose renouvelée : une deuxième exposition peut donner une agranulocytose même si la première cure a été simple. La recommandation de 2016 le signale.", S(2, 8, 12)),
)

add("p13", "w-cles", "Points d'examen",
P("Basedow fabrique. L'anticorps stimule. Le goitre est diffus. L'œil oriente. La scintigraphie est diffuse si on la fait, et souvent inutile si l'œil et le goitre parlent.", S(2)),
P("Carbimazole 20 à 60 mg puis 5 à 20 mg, plafond 60 mg, 30 mg avant 12 ans, 20 mg si allaitement. Propranolol 10-40 mg trois à quatre fois. Fièvre : arrêt. Durée 6 à 18 mois sur l'information professionnelle, douze à dix-huit mois dans la revue et la recommandation. On cite, on ne moyenne pas.", S(1, 2, 8, 10)),
P("Pas d'iode nucléaire. Iode de préparation opératoire seulement en gouttes, avant le bloc, pas au cabinet. Pas de thionamide si le cou est une thyroïdite. Pas de score de crise si le patient va bien, mais on sait le calculer.", S(5, 12)),
P("Sensibilité 96 à 97 %, spécificité 99 % de l'anticorps dans la thyrotoxicose franche. Rechute 80 à 100 % si l'anticorps reste haut, 20 à 30 % s'il est bas. Rémission globale citée 30 à 40 %.", S(1, 2)),
)

add("p14", "w-pieges", "Pièges",
P("Appeler Basedow toute thyréostimuline basse. La maladie grave, le corticoïde, l'amiodarone et la biotine abaissent la thyréostimuline sans cette maladie.", S(1, 4, 7)),
P("Donner le carbimazole à une thyroïdite douloureuse. Le médicament ne stoppe pas la fuite et peut donner une agranulocytose inutile.", S(8)),
P("Donner 130.0 mg d'iodure nucléaire. Contre-indiqué dans Basedow.", S(12)),
P("Commencer l'iode de la crise avant le thionamide. L'ordre lu est l'inverse.", S(5)),
P("Oublier la formule devant une angine parce que le patient a 25 ans. La consigne d'arrêt vaut à tout âge.", S(8)),
P("Promettre que les yeux guérissent avec les hormones. L'orbitopathie suit son cours.", S(1)),
P("Moyenner 6 à 18 mois et 12 à 18 mois en une durée unique. On rapporte les sources."),
P("Calculer une activité d'iode radioactif sans l'avoir lue. On adresse."),
)

add("p10", "w-dd", "Cinq diagnostics que Basedow n'est pas",
P("Nodule autonome. La thyréostimuline est basse, souvent la triiodothyronine libre d'abord. La thyroïde n'est pas diffuse et soufflante : un nodule domine. La scintigraphie montre un foyer chaud et le reste éteint. L'anticorps anti-récepteur est négatif. L'œil est calme. Le carbimazole peut préparer une chirurgie ou un iode radioactif, il ne fait pas disparaître le nodule. L'échographie classe le nodule de TR1 à TR5 pour la question du cancer, qui est distincte de la toxicité.", S(2, 6)),
P("Goitre multinodulaire toxique. Patient plus âgé, souvent. Plusieurs nodules, plusieurs foyers chauds. Le tabac et l'âge augmentent cette hyperthyroïdie dans la revue. Un contraste iodé peut la faire basculer en crise. On ne l'appelle pas Basedow parce que les deux fabriquent. Le traitement radical est plus souvent discuté d'emblée, parce que la rémission médicamenteuse du Basedow ne s'applique pas à une autonomie nodulaire.", S(1, 2)),
P("Thyroïdite de De Quervain. Douleur, fièvre modérée, vitesse de sédimentation haute, fixation basse. Phase haute puis phase basse. Prednisone dans la fourchette 15 à 30 mg par jour de l'information professionnelle pour une maladie aiguë, pas un carbimazole. Confondre les deux expose à une agranulocytose sans bénéfice.", S(1, 8, 13)),
P("Thyroïdite silencieuse ou du post-partum. Pas de douleur, fixation basse, évolution vers une phase basse puis souvent la guérison. L'anticorps anti-thyroperoxydase peut être présent sans que ce soit un Basedow. On ne lance pas douze mois de carbimazole. On surveille, on traite le cœur s'il va vite, on explique la phase basse.", S(1, 2)),
P("Biotine. Hormones libres très hautes, thyréostimuline effondrée, pouls calme, pas de goitre. Arrêt du complément, contrôle après au moins deux jours. Pas de thionamide. Si la patiente a en plus un vrai Basedow, la clinique reste riche après l'arrêt de la biotine : c'est alors les deux, et l'on traite la maladie.", S(7)),
P("Prise cachée de lévothyroxine. Thyroxine très haute, triiodothyronine moins haute, thyroïde petite, fixation nulle, pas de douleur. On cherche l'apport. On n'irradie pas. On n'opère pas.", S(2)),
P("Crise. Même maladie, autre chapitre. Score à 45 ou plus, ou TS1, ou TS2, ou jugement clinique entre 25 et 44. Là, l'iode minéral vient après le thionamide, l'hydrocortisone de stress entre, et le propranolol est celui de la crise, toujours 10-40 mg trois à quatre fois dans l'information professionnelle lue, pas une dose inventée.", S(5, 10, 11)),
P("Amiodarone de type 1. Basedow latent réveillé par l'iode du médicament. Le Doppler est riche. On traite par thionamide. On ne retire pas l'amiodarone seul. La décision est conjointe avec le cardiologue. Ce n'est pas le Basedow de la femme jeune sans cœur, mais le mécanisme de fabrication est le même.", S(4)),
)

add("p12", "w-suivi-b", "Les dix premiers jours, puis les mois",
P("Jour 0. On a confirmé les hormones. On a écarté la crise. On a parlé de la fièvre. On démarre, par exemple, dans le haut ou le milieu de la fourchette selon l'ampleur : la phrase autorise 20 à 60 mg par jour. On choisit une dose, on l'écrit en milligrammes par jour, en deux ou trois prises. On ajoute le propranolol si la fréquence est gênante. On donne la date du premier contrôle, sous une à deux semaines pour la clinique, pas pour juger déjà la thyréostimuline.", S(8, 10)),
P("Tous les dix jours, si l'on descend. L'information professionnelle dit de réduire par paliers de 5 à 15 mg par jour tous les dix jours jusqu'à une dose de 5 à 20 mg. On ne descend pas si la patiente est encore très thyrotoxique. On ne reste pas à la dose initiale trois mois par inertie : le surdosage fait monter la thyréostimuline et le goitre. Le palier se décide sur la clinique et les hormones libres, pas sur une thyréostimuline qui met plus longtemps à revenir.", S(8)),
P("Six premières semaines si la dose dépasse 40 mg et si la patiente a plus de 40 ans : formule avant, puis chaque semaine. Les autres patients n'ont pas cette grille hebdomadaire écrite, mais tous ont la consigne d'arrêt immédiat. On ne transforme pas la grille en une prise de sang inutile chez une femme de 25 ans à 20 mg, et on ne s'en sert pas pour rassurer celle qui a 39 °C de fièvre.", S(8)),
P("Mois 2 à 12. Dose d'entretien 5 à 20 mg. Contrôle clinique et biologique selon l'évolution. On cherche l'effet indésirable à chaque visite, comme la revue le demande. On parle de l'œil. On parle d'un projet de grossesse. On ne change pas de marque de lévothyroxine : elle n'est pas encore indiquée. Basedow traité ne reçoit pas d'Euthyrox tant que la thyréostimuline n'a pas monté par excès de thionamide ou après un traitement radical.", S(1, 8, 9)),
P("Mois 12 à 18. On regarde la thyréostimuline et l'anticorps. Si les deux sont revenus, on peut arrêter. Si l'anticorps est haut, on discute la poursuite, parfois encore douze à dix-huit mois, ou un traitement définitif. Après l'arrêt, contrôles rapprochés les premiers mois, parce qu'une rechute précoce existe, puis plus espacés. La patiente sait revenir si les palpitations reviennent, sans attendre la date.", S(2)),
P("Après chirurgie ou iode radioactif, l'hypothyroïdie est attendue. Là, Euthyrox entre : début selon l'âge et le cœur, entretien dans la zone 100 à 200 µg, à jeun, contrôle à quatre à six semaines après chaque changement. Ce n'est plus le chapitre du carbimazole. On ne mélange pas les deux ordonnances le même matin sans une raison lue. L'association lévothyroxine plus thionamide existe dans le tableau d'Euthyrox, 25 à 100 µg, comme traitement associé : on ne l'emploie que si le schéma de blocage-substitution a été choisi, pas par automatisme.", S(9)),
)

add("p14", "w-cas", "Cas corrigé",
P("Énoncé. Femme de 29 ans, 4 kg perdus en six semaines, pouls 112 régulier, température 37,0 °C, tremblement, goitre diffus soufflant, rétraction palpébrale, pas de diplopie, pas de vomissement. Thyroxine libre 41 pmol/l pour une borne haute à 22, thyréostimuline indétectable. Elle prend une gélule pour les ongles. Elle allaite un enfant de quatre mois. Que prescrivez-vous, et que refusez-vous ?"),
P("Correction. Clinique et biologie concordent : Basedow probable. La gélule peut fausser en plus le tube. On l'arrête. On ne diffère pas le traitement, parce que la clinique est riche, contrairement au piège de la biotine isolée. Score de crise : fréquence 112 vaut 10 points, température 37,0 °C est sous la première classe qui commence à 37,2 °C, pas de signe digestif ni neurologique de crise. Total bas. Pas de protocole de crise.", S(5, 7)),
P("Allaitement. Carbimazole possible seulement si la dose reste au plus de 20 mg par jour, en plusieurs prises, juste après la tétée, avec information du risque. Une thyrotoxicose à 41 pmol/l demanderait souvent une dose initiale plus haute, jusqu'à 60 mg, incompatible avec l'allaitement selon la phrase lue. On ne garde pas les deux : soit on suspend l'allaitement le temps d'une dose pleine et on l'explique, soit on adresse dans la journée pour un choix qui respecte le plafond. On n'écrit pas 40 mg en disant que l'allaitement continuera.", S(8)),
P("Propranolol 10-40 mg trois à quatre fois par jour, numéro 47025, si l'on retient le bêtabloquant pour la fréquence, en vérifiant l'asthme et l'effet sur l'enfant allaité : l'information professionnelle du propranolol doit être relue pour l'allaitement avant l'ordonnance, et si la phrase n'est pas sous les yeux on n'invente pas une compatibilité. Dans cette correction, on pose l'indication cardiaque et on exige la lecture de la rubrique allaitement du propranolol, numéro 47025, plutôt qu'une affirmation absente du passage déjà extrait.", S(10)),
P("Anticorps anti-récepteur en ligne de base. Pas de scintigraphie pendant l'allaitement. Pas d'iode. Consigne d'agranulocytose même à 29 ans. Contrôle clinique sous une semaine. Avis spécialisé parce que l'allaitement et la dose se contraignent. On ne promet pas les 30 à 40 % de rémission comme une garantie personnelle.", S(1, 2, 8)),
)

if __name__ == "__main__":
    p = rendre(1, "Maladie de Basedow", ess, points, fens)
    print(p)
