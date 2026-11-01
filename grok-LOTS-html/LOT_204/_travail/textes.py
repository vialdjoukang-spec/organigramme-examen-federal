# -*- coding: utf-8 -*-
"""Phrases cliniques de LOT_204. Une phrase, au plus 34 mots, sans point-virgule. [[n]] = INDEX."""

def N(cle, etiquette, items):
    pos = [(280, 230, 130, 80), (720, 240, 120, 75), (300, 540, 110, 85), (710, 530, 115, 70)]
    structures = []
    for (nom, defin), (cx, cy, rx, ry) in zip(items, pos):
        structures.append({"nom": nom, "cx": cx, "cy": cy, "rx": rx, "ry": ry, "definition": defin})
    return {"cle": cle, "etiquette": etiquette, "structures": structures}


def Q(queues):
    base = "Situation {k}. Chez une personne de {age} ans qui pratique {sport}, vue {lieu}, "
    return [base + q for q in queues]


TEASERS = {
    1: "Un comportement choisi, pas un discours général.",
    2: "Les parts lues classent, elles ne jugent pas la personne.",
    3: "Le plaisir immédiat gagne souvent contre le risque lointain.",
    4: "Le danger du jour passe avant le conseil.",
    5: "On demande la permission, puis un seul sujet.",
    6: "Le schéma montre trois plans, pas une radiographie.",
    7: "Dix pistes, une seule travaillée à la fois.",
    8: "Le critère lu tranche, pas l'impression.",
    9: "L'examen ne motive pas à lui seul.",
    10: "Trois portes : urgence, conseil, stade.",
    11: "Le milligramme vient de l'information suisse.",
    12: "Le cadre collectif compte autant que la phrase.",
    13: "Peu de règles, toutes actionnables.",
    14: "Le cas montre l'erreur, puis la correction.",
}

A = {
    "cle": "a",
    "titre": "Promotion d'un mode de vie sain",
    "sous": "Code O4.3. Situation de départ du référentiel du 1er novembre 2023.",
    "fin": "LOT_204_Phase_A_V0.html",
    "teasers": TEASERS,
    "ess": [
        "Informer ne suffit pas. On cherche un motif, une marche possible et un cadre qui ne s'y oppose pas.",
        "Le référentiel suisse validé le 1er novembre 2023 nomme cette situation O4.3. [[1]]",
        "On travaille un seul comportement par rencontre, choisi avec la personne.",
        "Le danger immédiat, thoracique, de sevrage ou de restriction, passe avant le conseil.",
    ],
    "faits": {
        1: [
            "La promotion d'un mode de vie sain est une situation de prévention, pas un organe malade. [[1]]",
            "Elle vise le tabac, l'alcool, le mouvement, l'assiette, le temps assis, le sommeil et le cannabis.",
            "Le bilan de santé et le dépistage appartiennent à d'autres situations du même chapitre. [[1]]",
            "La santé sexuelle et la fertilité ne sont pas traitées ici. [[1]]",
            "Le succès se juge à un geste tenu, pas à une phrase entendue.",
        ],
        2: [
            "La prévalence lue de fumeurs en 2022 est de 24 % après 15 ans. [[5]]",
            "La page lue attribue 9500 décès par an au tabac. [[5]]",
            "En 2022, 75,7 % respectaient les recommandations d'activité, et 8,3 % étaient inactifs. [[4]]",
            "La moyenne lue de sel est de 8,7 g de sel par jour, pour un repère de 5 g de sel. [[8]]",
            "Dans l'étude du sel, 34 % étaient en surpoids et 12 % étaient obèses. [[8]]",
            "En 2022, 8,6 % buvaient de l'alcool au moins une fois par jour. [[6]]",
            "Ces parts classent l'enseignement. Elles ne sont pas un registre du cabinet.",
        ],
        3: [
            "Le comportement oppose un gain proche et certain à un risque lointain et probable.",
            "La nicotine lève le manque en quelques minutes, et le cancer se compte en années.",
            "L'alcool lève l'anxiété le soir, et le foie se plaint plus tard.",
            "Le sucre et le gras donnent un rassasiement rapide, au-delà de la faim.",
            "Rester assis économise l'effort, et le muscle se déshabitue.",
            "Le sommeil trop court laisse le jour entier plus irritable et plus affamé.",
            "Sans motif personnel, la connaissance du risque ne déplace pas cet équilibre.",
        ],
        4: [
            "On écarte d'abord la douleur thoracique, la syncope d'effort et la dyspnée récente.",
            "On écarte un sevrage d'alcool si le verre est matinal, si ça tremble, ou s'il y a eu une crise.",
            "On n'écrit pas de restriction devant une perte de poids involontaire.",
            "On demande la permission, puis la personne choisit un seul sujet.",
            "On situe le stade : pas d'intention, ambivalence, envie dans le mois, geste en cours, maintien.",
            "On écrit une marche que la personne cote au moins capable, avec un jour et un lieu.",
            "On fixe la revue. Un conseil sans date ne se mesure pas.",
        ],
        5: [
            "L'anamnèse balaye tabac, alcool, mouvement, assiette, temps assis, sommeil et cannabis.",
            "Pour le tabac, on demande l'heure de la première cigarette et le nombre du jour.",
            "Pour l'alcool, on demande la fréquence, la quantité d'un jour type et les soirs de dépassement.",
            "Pour le mouvement, on demande les minutes de la semaine et les jours de force.",
            "On demande qui achète, qui cuisine, et ce que le budget permet.",
            "On demande le sommeil réel, les ronflements et la somnolence au volant.",
            "Un refus d'aborder un sujet se respecte, et la porte reste ouverte.",
        ],
        6: [
            "L'examen quantifie un risque et vérifie qu'un effort plus intense est supportable.",
            "On mesure la pression, le pouls, le poids, la taille et le tour de taille.",
            "On ausculte le cœur et les poumons si l'on va prescrire un effort.",
            "On cherche un tremblement, une conjonctive jaune ou un foie dur si l'alcool est au premier plan.",
            "On ne commente pas le corps comme un échec moral.",
            "Le schéma pédagogique sépare le danger, le geste et le stade.",
        ],
        7: [
            "Tabagisme quotidien de l'adulte : nicotine, décès fréquents, sevrage planifié.",
            "Alimentation éloignée de la pyramide suisse : sel, fibres, boissons sucrées, portions.",
            "Inactivité physique de l'adulte : minutes et renforcement sous les fourchettes lues.",
            "Excès pondéral de l'adulte : indice au moins à 25, geste sur les comportements.",
            "Usage d'alcool à risque : au-dessus des verres lus, sans dépendance constituée.",
            "Sédentarité avec temps assis prolongé : longues périodes assises, même si l'on bouge ailleurs.",
            "Durée de sommeil insuffisante : nuits trop courtes pour l'âge, hors maladie du sommeil.",
            "Usage de cannabis à problème : retentissement, conduite, jeune âge ou mélange au tabac.",
            "Dépendance à l'alcool et sevrage : critères lus et risque si l'arrêt est brutal.",
            "Demande de régime et trouble alimentaire : restriction demandée, signes de trouble.",
        ],
        8: [
            "Le score court d'alcool devient problématique à 5 points chez l'homme et à 4 chez la femme. [[9]]",
            "Le score long va de 0 à 40, et 8 points, ou 5 chez les femmes, ouvrent un problème. [[9]]",
            "Cinq points ou plus au test de nicotine, avec plus de 20 cigarettes, orientent le patch fort. [[14]]",
            "Le seuil lu du surpoids commence à un indice de 25, et celui de l'obésité à 30. [[8]]",
            "Le seuil lu de sel est de 5 g de sel par jour. [[8]]",
            "La dépendance lue à l'alcool demande au moins trois critères sur l'année. [[11]]",
            "La durée de sommeil lue est de 7 à 9 heures de 18 à 64 ans, et de 7 à 8 heures après. [[12]]",
        ],
        9: [
            "On ne demande pas un scanner entier pour faire peur ou pour motiver.",
            "La pression confirme un risque déjà connu, elle ne remplace pas le geste.",
            "La glycémie ou l'hémoglobine glyquée se discute si le risque métabolique est déjà là.",
            "On ne fait pas d'épreuve d'effort chez un adulte asymptomatique qui veut seulement marcher.",
            "Un monoxyde expiré, si on le dispose, objective l'arrêt du tabac sans inventer un seuil ici.",
            "Devant un sevrage alcoolique bruyant, le laboratoire ne retarde pas la protection.",
        ],
        10: [
            "La porte urgence arrête le conseil ordinaire.",
            "La porte conseil écrit un seul geste daté.",
            "La porte stade adapte la phrase au degré d'intention.",
            "On ne mélange pas les trois portes dans la même minute.",
        ],
        11: [
            "Les milligrammes du tabac et de l'alcool viennent des autorisations 70067, 50582, 54064, 55263, 53090, 15104, 32497 et 10989.",
            "Sans dépendance, on commence par le geste, pas par le comprimé.",
            "Avec dépendance nicotinique, un substitut ou un médicament lu augmente la chance d'arrêter.",
            "Avec dépendance alcoolique, on ne laisse pas arrêter seul si le sevrage a déjà été bruyant.",
            "La revue est rapprochée au début, puis espacée si le geste tient.",
            "Un écart isolé ne se traite pas comme une rechute complète.",
        ],
        12: [
            "La page du tabac rappelle un volet personnel et un volet de cadre, prix, lieux et vente. [[5]]",
            "Chaque mouvement compte, même sous la fourchette, selon la page du 21 janvier 2025. [[2]]",
            "L'assiette du 11 septembre 2024 est le repère collectif, pas un régime du mois. [[7]]",
            "On oriente vers les offres du canton quand le cabinet ne peut pas porter le suivi seul.",
            "Chez l'adolescent, la prévention du premier produit passe avant le sevrage d'un adulte.",
        ],
        13: [
            "Un sujet, une permission, une marche écrite, une date.",
            "Le tabac tue beaucoup, et la page lue donne 9500 décès par an. [[5]]",
            "Le mouvement utile commence bien avant la performance.",
            "L'alcool à risque n'est pas encore la dépendance, et les conduites diffèrent.",
            "On ne prescrit pas l'inaccessible.",
            "On ne pèse pas pour faire honte.",
        ],
        14: [
            "Erreur : répéter le risque que la personne connaît déjà, jusqu'à la dispute.",
            "Correction : on reflète l'ambivalence et on laisse la personne dire son motif.",
            "Erreur : dix conseils le même jour.",
            "Correction : un seul geste, revu à une date écrite.",
            "Cas. Une personne de 52 ans veut tout changer lundi. On lui fait choisir le tabac, et le reste attend.",
        ],
    },
    "niveaux": [
        N("danger", "Danger", [
            ("Poitrine", "Douleur, syncope ou dyspnée récente : on n'augmente pas l'effort."),
            ("Sevrage", "Tremblement, verre matinal ou crise : l'arrêt d'alcool ne se fait pas seul."),
            ("Poids perdu", "Une perte involontaire se comprend avant toute restriction."),
            ("Conduite", "Somnolence au volant ou alcool encore présent : on ne reprend pas la route."),
        ]),
        N("geste", "Geste", [
            ("Tabac", "Première cigarette et nombre du jour orientent le substitut."),
            ("Assiette", "La pyramide du 11 septembre 2024 remplace le régime miracle."),
            ("Mouvement", "Minutes modérées ou soutenues, plus deux jours de force."),
            ("Sommeil", "Heure du coucher et du lever, avant tout comprimé."),
        ]),
        N("stade", "Stade", [
            ("Pas prêt", "On ne fixe pas de date. On laisse une porte."),
            ("Ambivalent", "On fait dire les deux plateaux, sans argumenter."),
            ("Ce mois", "Date, marche écrite, et revue rapprochée."),
            ("Tient", "On valorise, et on prépare l'écart sans humilier."),
        ]),
    ],
    "question": "Quelle porte ouvre-t-on en premier ?",
    "reponse": [
        "On ouvre la porte du danger si la poitrine, le sevrage ou la route sont en jeu.",
        "Sinon on ouvre le geste que la personne a choisi.",
        "Le stade dit comment parler, il ne remplace pas le danger.",
    ],
    "algo": [
        ("alerte", "Urgence", "Douleur thoracique, sevrage bruyant, route ou perte de poids involontaire : le conseil attend."),
        ("bilan", "Conseil", "Un seul geste écrit, avec quantité, jour et lieu, puis une date de revue."),
        ("age", "Stade", "Pas d'intention : porte ouverte. Ambivalence : reflet. Dans le mois : date. Maintien : écart prévu."),
    ],
    "modeles": Q([
        "on demande d'abord si quelque chose fait mal à la poitrine à l'effort.",
        "on ne parle pas de dix sujets, on en fait choisir un.",
        "on écrit le geste avec un jour, un lieu et une durée.",
        "on ne dispute pas quand la personne dit qu'elle sait déjà.",
        "on respecte un refus et on propose de rouvrir plus tard.",
        "on sépare un verre de trop et une dépendance déjà bruyante.",
        "on ne donne pas un régime chiffré si le rapport à l'assiette est déjà malade.",
        "on vérifie le budget avant de prescrire une salle.",
        "on date la revue au lieu de dire de faire attention.",
        "on ne félicite pas une perte de poids dont on ignore la cause.",
        "on demande l'heure de la première cigarette avant le choix du patch.",
        "on demande les minutes réellement bougées, pas l'intention.",
        "on demande les jours sans alcool de la semaine.",
        "on demande l'heure du coucher et celle du lever.",
        "on ne promet pas un résultat que la page lue ne chiffre pas.",
        "on laisse le cadre, prix et lieux, à côté du conseil personnel.",
    ]),
}
