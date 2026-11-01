# -*- coding: utf-8 -*-
"""Pistes DX.2 à DX.10 de LOT_202. Les phrases courtes portent les critères lus."""
from contenu import DOSE_PAR, DOSE_IBU, DOSE_SALBU
from dx import DXS, T


def NV(cle, etq, rows):
    return {
        "cle": cle,
        "etiquette": etq,
        "structures": [
            {"nom": a, "cx": b, "cy": c, "rx": d, "ry": e, "definition": f}
            for a, b, c, d, e, f in rows
        ],
    }


def ajouter(titre, cle, ess, faits, algo, niveaux, question, reponse, modeles, teaser11=None):
    d = T(titre, f"Piste DX.{cle}. {titre}.", cle)
    if teaser11:
        d["teasers"][11] = teaser11
    d["ess"] = ess
    d["faits"] = faits
    d["algo"] = algo
    d["niveaux"] = niveaux
    d["question"] = question
    d["reponse"] = reponse
    d["modeles"] = modeles
    DXS.append(d)


def M(lignes):
    return [
        "Situation {k}. Chez une personne de {age} ans qui pratique {sport}, vue {lieu}, " + s
        for s in lignes
    ]


# --- DX.2 muscle ---
ajouter(
    "Lésion musculaire des ischio-jambiers",
    2,
    [
        "La lésion des ischio-jambiers va du trouble sans déchirure à l'arrachement.",
        "La classification de Munich, en 2013, sépare le fonctionnel du structural. [[3]]",
        "Le sprint reprend quand la course en ligne ne boite plus.",
    ],
    {
        1: [
            "Les ischio-jambiers sont souvent touchés parce qu'ils ont un long tendon intramusculaire. [[3]]",
            "Ce n'est pas toute douleur de cuisse, et ce n'est pas une crampe isolée du mollet.",
            "Le trouble fonctionnel limite le geste sans déchirure macroscopique. [[3]]",
            "La déchirure structurale montre un dommage macroscopique du muscle. [[3]]",
        ],
        2: [
            "Aucune incidence suisse de cette lésion n'a été lue pour ce lot.",
            "Le rang 2 est un rang d'enseignement, au cabinet de médecine du sport.",
            "Le consensus de 2013 a été écrit pour parler le même langage. [[3]]",
        ],
        3: [
            "L'étirement brusque pendant la contraction dépasse la limite du muscle. [[3]]",
            "La jonction entre muscle et tendon est un point faible de ce mécanisme. [[3]]",
            "Le type 1 est lié au surmenage : fatigue, ou courbatures différées. [[3]]",
            "Le type 2 est neuromusculaire, lié au rachis ou au muscle lui-même. [[3]]",
            "Le type 3 est une déchirure partielle, mineure en 3A et modérée en 3B. [[3]]",
            "Le type 3B a un diamètre supérieur à un faisceau. [[3]]",
            "Le type 4 est une déchirure subtotale, totale, ou un arrachement tendineux. [[3]]",
            "Les types 1 et 2 ne se voient pas comme une déchirure à l'imagerie standard. [[3]]",
        ],
        4: [
            "On écarte d'abord un membre froid, une peau ouverte et un genou bloqué.",
            "On demande si la douleur a été vive au sprint ou sourde le lendemain.",
            "On classe ensuite selon Munich, avant de promettre une date de course. [[3]]",
            "Un creux palpable ou un hématome large sort du trouble fonctionnel simple.",
            "On ne fait pas reprendre le sprint le jour du claquement.",
        ],
        5: [
            "On demande le geste : sprint, tir ou étirement en bout de course.",
            "On demande l'heure de la douleur et si un claquement a été entendu.",
            "On demande si la personne a fini la séance ou s'est arrêtée net.",
            "On demande les lésions anciennes du même muscle et le volume récent.",
            "On demande la date du prochain sprint ou du prochain match.",
        ],
        6: [
            "On regarde la marche, le bleu et un creux dans le ventre musculaire.",
            "On palpe le biceps fémoral, le semi-tendineux et le semi-membraneux.",
            "On cherche une douleur du tendon proximal, sous la fesse.",
            "On teste une contraction douce, sans forcer un muscle qui claque.",
            "Le dessin situe le ventre, le tendon et le creux. Ce n'est pas une image.",
        ],
        7: [
            "La crampe cède au repos et ne laisse pas de creux.",
            "La douleur du rachis peut donner un type 2, sans déchirure du ventre. [[3]]",
            "La sciatique descend plus bas que le ventre musculaire et suit le trajet nerveux.",
            "La rupture du tendon proximal se cherche si le creux est haut et la fesse est bleue.",
            "La fracture de fatigue du fémur n'a pas le claquement d'un sprint. [[11]]",
        ],
        8: [
            "On nomme le type de Munich, pas seulement le mot claquage. [[3]]",
            "Le type 1A est la fatigue, et le type 1B les courbatures différées. [[3]]",
            "Le type 2A est lié au rachis, et le type 2B au muscle. [[3]]",
            "Le type 3A est la déchirure partielle mineure. [[3]]",
            "Le type 3B est la déchirure partielle modérée, au-delà d'un faisceau. [[3]]",
            "Le type 4 comprend la déchirure totale et l'arrachement tendineux. [[3]]",
            "Une douleur en coup de poignard avec un défaut palpable oriente vers le structural. [[3]]",
        ],
        9: [
            "L'imagerie n'est pas le premier geste d'une tension sans creux. [[3]]",
            "Elle aide si le creux, le bleu large ou l'arrachement changent l'adresse.",
            "Elle ne remplace pas la classification clinique de 2013. [[3]]",
            "On ne répète pas l'image le lendemain si la marche s'améliore et le creux est absent.",
        ],
        10: [
            "Porte du danger : membre froid, peau ouverte, creux haut avec bleu massif.",
            "Porte de Munich : fonctionnel sans déchirure, ou structural avec dommage vu. [[3]]",
            "Porte de l'action : protection, charge relative, ou adresse si l'arrachement est probable.",
        ],
        11: list(DOSE_PAR) + list(DOSE_IBU) + [
            "Le comprimé soulage. Il ne recolle pas une déchirure.",
            "On protège la marche douloureuse et on évite le sprint tant que le creux tire.",
            "Un arrachement proximal douloureux s'adresse, il ne se traite pas seulement au cabinet.",
            "On revoit si le bleu s'étend, si le creux grandit, ou si la marche ne revient pas.",
        ],
        12: [
            "La course en ligne précède les accélérations.",
            "Les changements de direction viennent après la course sans boiterie.",
            "On ne raccourcit pas l'échauffement la semaine du retour.",
            "On corrige le bond de volume qui a précédé la douleur.",
        ],
        13: [
            "On dit le type de Munich, de 1A à 4. [[3]]",
            "L'absence de déchirure macroscopique définit le trouble fonctionnel. [[3]]",
            "Le type 3B dépasse un faisceau. [[3]]",
            "Le sprint du lendemain n'est pas un traitement.",
        ],
        14: [
            "Cas. Un sprinteur de 24 ans sent un coup de poignard, s'arrête, et un creux est palpable.",
            "Erreur. Le renvoyer au sprint du lendemain parce qu'il marche encore.",
            "Correction. Le claquement et le creux orientent vers une lésion structurale : pas de sprint, et on adresse si le tendon proximal lâche. [[3]]",
        ],
    },
    [
        ("alerte", "Écarter le danger", "Membre froid, peau ouverte ou bleu massif sous la fesse : on sort du soin simple."),
        ("bilan", "Classer selon Munich", "Fonctionnel sans déchirure vue, ou structural de type 3 ou 4. [[3]]"),
        ("age", "Protéger le sprint", "On soulage, on évite l'accélération, et on fixe une revue."),
    ],
    [
        NV("ventre", "Ventre", [
            ("Biceps fémoral", 340, 360, 80, 120, "Chef externe, souvent le siège du claquement."),
            ("Semi-tendineux", 500, 340, 60, 110, "Chef interne superficiel."),
            ("Semi-membraneux", 620, 400, 70, 100, "Chef interne profond."),
            ("Jonction", 480, 520, 90, 40, "Zone faible entre muscle et tendon."),
        ]),
        NV("tendon", "Tendon", [
            ("Tendon proximal", 480, 220, 70, 40, "Sous la fesse. Un creux ici fait adresser."),
            ("Tendon distal", 500, 600, 60, 36, "Vers le genou, moins souvent isolé."),
            ("Ischion", 470, 150, 50, 30, "L'arrachement osseux se cherche si le bleu est haut."),
            ("Repère", 700, 300, 30, 30, "La droite du patient reste à gauche de l'écran."),
        ]),
        NV("creux", "Creux", [
            ("Creux", 420, 400, 50, 36, "Un défaut palpable oriente vers le structural."),
            ("Bleu", 560, 430, 70, 50, "L'hématome large n'est pas une simple courbature."),
            ("Tension", 480, 300, 80, 36, "La tension sans creux peut rester fonctionnelle."),
            ("Marche", 500, 620, 90, 28, "La marche se regarde avant le sprint."),
        ]),
    ],
    "Quel plan ouvre une cuisse claquée ?",
    [
        "On ouvre le ventre pour nommer le muscle.",
        "On ouvre le tendon si la douleur est haute, sous la fesse.",
        "On ouvre le creux si un défaut ou un bleu large est là.",
    ],
    M([
        "on demande si la douleur a claqué pendant le sprint ou le lendemain.",
        "on ne promet pas l'accélération tant que la course en ligne boite.",
        "on palpe les trois chefs avant de dire que ce n'est qu'une crampe.",
        "on cherche un creux et un bleu, pas seulement une tension.",
        "on classe le type avant de choisir une image.",
        "on n'utilise pas le comprimé comme s'il recollait le muscle.",
        "on adresse un creux haut et bleu plutôt que d'attendre le match.",
        "on compare la cuisse blessée à la cuisse saine.",
        "on écrit la date où le sprint reste interdit.",
        "on relie la douleur au bond de volume de la semaine.",
    ]),
)

# --- DX.3 commotion ---
ajouter(
    "Commotion cérébrale liée au sport",
    3,
    [
        "La commotion liée au sport est un traumatisme cérébral par un coup transmis au cerveau. [[4]]",
        "Cette définition a obtenu 78,6 % des voix, sous la barre de 80 %. [[4]]",
        "Le joueur qui a ces signes ne reprend pas le match le jour même. [[4]]",
    ],
    {
        1: [
            "Le coup peut frapper la tête, le cou ou le corps, et l'onde arrive au cerveau. [[4]]",
            "Les signes peuvent être immédiats ou apparaître en minutes ou en heures. [[4]]",
            "La perte de connaissance n'est pas exigée. [[4]]",
            "L'image structurale standard ne montre pas la lésion. [[4]]",
            "Un médicament, l'alcool ou une lésion du cou peuvent accompagner le tableau. [[4]]",
            "Ce n'est pas un certificat, et ce n'est pas un mal de tête isolé sans choc.",
        ],
        2: [
            "Aucune incidence suisse de la commotion sportive n'a été lue pour ce lot.",
            "Le rang 3 est un rang d'enseignement, parce que le retard coûte des jours.",
            "La moyenne groupée du retour sans restriction est de 19,8 jours. [[4]]",
            "L'intervalle lu de cette moyenne va de 18,8 à 20,7 jours. [[4]]",
            "Ce regroupement porte sur 57 travaux. [[4]]",
            "Continuer à jouer et attendre pour voir un soignant allongent la récupération. [[4]]",
        ],
        3: [
            "Le coup déclenche une cascade de neurotransmetteurs et un trouble métabolique. [[4]]",
            "Un trouble du flux sanguin et une inflammation peuvent s'y ajouter. [[4]]",
            "Une lésion axonale est possible dans cette description. [[4]]",
            "Le cerveau n'est pas seulement un bleu du cuir chevelu.",
            "Les symptômes se prolongent parfois au-delà de quelques jours. [[4]]",
        ],
        4: [
            "Au moindre doute, on sort le joueur du terrain. [[4]]",
            "On protège le cou s'il est douloureux, et on arrête là l'examen sportif.",
            "On ne renvoie pas au match le jour des signes listés, sauf preuve que ce n'est pas une commotion. [[4]]",
            "Cette exception demande un soignant expérimenté et une évaluation multimodale. [[4]]",
            "Ensuite on ouvre les étapes, chacune d'au moins 24 heures. [[4]]",
            "On n'ordonne pas le repos absolu en chambre fermée. [[4]]",
        ],
        5: [
            "On demande le mécanisme, vu par le joueur, un partenaire ou la vidéo. [[4]]",
            "On demande la perte de connaissance, la crise, la confusion et l'amnésie. [[4]]",
            "On demande les commotions anciennes et le temps de chacune.",
            "On demande la migraine, l'anxiété et la dépression, qui modifient le tableau. [[4]]",
            "On demande l'école ou le travail du lendemain, pas seulement le match.",
        ],
        6: [
            "On regarde la vigilance, l'équilibre, la marche et le comportement. [[4]]",
            "Les signes de sortie immédiate comprennent la crise et la posture tonique. [[4]]",
            "Ils comprennent aussi l'ataxie, le mauvais équilibre, la confusion et l'amnésie. [[4]]",
            "Pour les plus de 12 ans, sans signe clair, des questions brèves orientent. [[4]]",
            "Une réponse fausse ouvre une évaluation plus complète, hors du jeu. [[4]]",
            "Le dessin situe la tête et le cou. Ce n'est pas un scanner.",
        ],
        7: [
            "Le saignement intracrânien se cherche si la vigilance chute ou le cou est raide.",
            "On n'enseigne pas ici un algorithme chiffré du rachis cervical.",
            "Un trouble vestibulaire ou du cou peut coexister avec la commotion. [[4]]",
            "L'intoxication peut brouiller les signes, elle ne les efface pas. [[4]]",
            "Le coup de chaleur donne aussi un trouble neurologique, avec une température haute. [[10]]",
        ],
        8: [
            "On retient la définition de 2022, y compris le vote à 78,6 %. [[4]]",
            "L'outil aigu discrimine surtout dans les 72 heures, et jusqu'à 5 à 7 jours. [[5]]",
            "Passé 7 jours, hors l'échelle des symptômes, il ne décide pas du retour. [[5]]",
            "De 8 à 12 ans, l'outil de l'enfant est celui qui est prévu. [[5]]",
            "Au-delà, l'outil de cabinet guide les évaluations répétées. [[4]]",
            "Une gêne brève est une hausse d'au plus 2 points sur 0 à 10, moins d'une heure. [[4]]",
        ],
        9: [
            "Le scanner ou l'imagerie structurale ne montre pas la commotion elle-même. [[4]]",
            "On image si un autre danger est plausible, pas pour prouver la commotion.",
            "L'outil de 2023 aide l'évaluation aiguë. Il ne remplace pas la surveillance. [[5]]",
            "On revoit dans les heures, parce que les signes peuvent encore apparaître. [[4]]",
        ],
        10: [
            "Porte du danger : vigilance, crise, cou douloureux, déficit qui s'aggrave.",
            "Porte des étapes : repos relatif, puis effort, puis geste, puis contact. [[4]]",
            "Porte de l'action : pas de jeu le jour même, et une date de revue. [[4]]",
        ],
        11: list(DOSE_PAR) + [
            "Le paracétamol soulage un mal de tête. Il n'autorise pas le retour au jeu.",
            "Le repos relatif dure environ 24 à 48 heures, avec les gestes de la vie. [[4]]",
            "L'étape 1, limitée par les symptômes, peut commencer dans les 24 heures. [[4]]",
            "L'étape 2 est un effort aérobie léger, puis un effort aérobie modéré. [[4]]",
            "L'étape 3 est un geste du sport, sans risque de nouveau coup à la tête. [[4]]",
            "Les étapes 4 à 6 attendent la fin des symptômes, y compris après l'effort. [[4]]",
            "Si la gêne dépasse la limite brève aux étapes 1 à 3, on arrête et on reprend le lendemain. [[4]]",
            "Si la gêne revient aux étapes 4 à 6, on revient à l'étape 3. [[4]]",
            "Au-delà de 4 semaines, l'évaluation devient multimodale. [[4]]",
        ],
        12: [
            "Le club sort le joueur au doute, sans attendre la fin de la mi-temps. [[4]]",
            "On limite les contacts à l'entraînement selon le sport, quand une règle existe. [[4]]",
            "Le protège-dents est soutenu au hockey sur glace des enfants et des adolescents. [[4]]",
            "On prévoit qui surveille les heures qui suivent le choc.",
        ],
        13: [
            "On sort du terrain au doute. [[4]]",
            "On ne rejoue pas le jour des signes de commotion. [[4]]",
            "Chaque étape demande au moins 24 heures. [[4]]",
            "La moyenne lue du retour sans restriction est de 19,8 jours. [[4]]",
            "Le vote de la définition est de 78,6 %, pas de 80 %. [[4]]",
        ],
        14: [
            "Cas. Un gardien de 17 ans veut jouer le lendemain d'un choc tête contre genou.",
            "Erreur. Autoriser le match parce qu'il sourit et connaît le résultat.",
            "Correction. On le retire, on protège le cou s'il est douloureux, et on ouvre les étapes. [[4]]",
        ],
    },
    [
        ("alerte", "Sortir du jeu", "Perte de connaissance, crise, confusion, ataxie ou cou douloureux : on arrête."),
        ("bilan", "Ouvrir les étapes", "Repos relatif, puis aérobie, puis geste sans contact, puis retour surveillé. [[4]]"),
        ("age", "Revoir les heures", "Les signes peuvent apparaître plus tard. On fixe une revue, pas un certificat."),
    ],
    [
        NV("tete", "Tête", [
            ("Cuir chevelu", 500, 260, 120, 80, "Zone du coup direct. Le dessin n'est pas un scanner."),
            ("Oreille", 680, 280, 36, 50, "Repère latéral."),
            ("Menton", 500, 360, 34, 24, "Le récit du choc passe par là."),
            ("Nuque haute", 500, 420, 70, 28, "Le cou douloureux arrête la mobilisation."),
        ]),
        NV("cou", "Cou", [
            ("Rachis", 500, 300, 40, 120, "On protège. On ne teste pas la mobilité au bord du terrain."),
            ("Muscle", 380, 340, 50, 70, "Une contracture peut accompagner le choc."),
            ("Trachée", 620, 360, 28, 50, "Repère médian du schéma, pas un diagnostic."),
            ("Base", 500, 520, 80, 30, "Le thorax commence plus bas."),
        ]),
        NV("etapes", "Étapes", [
            ("Étape 1", 220, 300, 70, 40, "Activité limitée par les symptômes."),
            ("Étape 2", 420, 300, 70, 40, "Effort aérobie léger puis modéré."),
            ("Étape 3", 620, 300, 70, 40, "Geste du sport sans risque de coup."),
            ("Étapes 4 à 6", 480, 480, 120, 40, "Après la fin des symptômes, y compris à l'effort."),
        ]),
    ],
    "Quel plan ouvre un choc à la tête ?",
    [
        "On ouvre la tête pour le récit du coup.",
        "On ouvre le cou si la nuque est douloureuse.",
        "On ouvre les étapes seulement quand le danger immédiat est écarté.",
    ],
    M([
        "on sort du terrain avant de discuter le certificat.",
        "on demande si la confusion est apparue tout de suite ou une heure après.",
        "on ne promet pas le match du soir.",
        "on surveille les heures qui suivent, parce que les signes bougent.",
        "on n'enferme pas la personne dans le noir.",
        "on sépare le retour à l'école du retour au contact.",
        "on note les commotions anciennes et leur durée.",
        "on protège la nuque douloureuse sans la manipuler.",
        "on n'utilise pas le mal de tête soulagé comme feu vert.",
        "on écrit la prochaine étape et la date, pas un adjectif vague.",
    ]),
)

# --- DX.4 Achille ---
ajouter(
    "Tendinopathie du tendon d'Achille",
    4,
    [
        "La tendinopathie d'Achille est une douleur de charge du tendon, souvent raide le matin.",
        "Le tendon reste continu. La rupture se cherche à part, sans chiffre de sensibilité inventé.",
        "On garde une charge relative si la rupture n'est pas là.",
    ],
    {
        1: [
            "La douleur siège au corps du tendon ou à son insertion sur le calcanéus.",
            "Elle augmente avec la course, les sauts ou une montée brusque de volume.",
            "Ce n'est pas toute douleur de cheville, et ce n'est pas une entorse par inversion.",
            "La visite d'après blessure du motif ouvre cette piste quand le tendon est la plainte.",
        ],
        2: [
            "Aucune incidence suisse de cette tendinopathie n'a été lue pour ce lot.",
            "Le rang 4 est un rang d'enseignement, fréquent chez le coureur.",
            "Aucun protocole chiffré de répétitions n'a été relu : il n'est pas enseigné.",
        ],
        3: [
            "La charge répétée irrite le tendon plus qu'un seul faux pas.",
            "Le repos complet, s'il n'y a pas de rupture, affaiblit le tendon sans le soigner.",
            "Le matin raide correspond souvent à un tendon qui se réchauffe ensuite.",
            "Une rupture complète interrompt la continuité et la flexion plantaire au serrage du mollet.",
        ],
        4: [
            "On écarte d'abord une rupture, une peau ouverte et un pied froid.",
            "On demande si la douleur cède après l'échauffement ou si elle empire d'emblée.",
            "On palpe le corps du tendon et l'insertion.",
            "On serre le mollet, genou fléchi, et on regarde si le pied descend.",
            "Si le pied ne descend pas, on traite comme une rupture jusqu'à preuve du contraire.",
            "Sans rupture, on adapte la charge au lieu de tout arrêter.",
        ],
        5: [
            "On demande l'heure de la douleur, surtout les premiers pas du matin.",
            "On demande le volume de course des deux dernières semaines.",
            "On demande un claquement, une sensation de coup dans le mollet, et l'appui.",
            "On demande les fluoroquinolones récentes et les injections locales.",
            "On demande le sport de retour et la date de la prochaine course.",
        ],
        6: [
            "On regarde la marche, le gonflement du tendon et une fossette.",
            "On palpe le milieu du tendon et l'insertion sur le talon.",
            "On compare au tendon sain.",
            "Le serrage du mollet fait descendre le pied si le tendon est continu.",
            "Le dessin montre le tendon, l'insertion et le mollet. Ce n'est pas une échographie.",
        ],
        7: [
            "L'entorse latérale suit une inversion et fait mal en avant de la malléole. [[2]]",
            "La rupture complète enlève la descente du pied au serrage du mollet.",
            "La bursite rétrocalcanéenne fait mal à l'insertion, avec un tendon encore continu.",
            "La fracture de fatigue du calcanéus monte avec les semaines, sans claquement. [[11]]",
            "La lésion du mollet siège plus haut que le tendon.",
        ],
        8: [
            "On retient une douleur de charge, une raideur matinale, et un tendon continu.",
            "Le réchauffement qui améliore la douleur va dans ce sens.",
            "L'absence de descente du pied au serrage oriente vers la rupture complète.",
            "Aucun pourcentage de sensibilité de ce serrage n'a été relu.",
            "On ne pose pas un nombre de séries qui n'est pas dans les preuves du lot.",
        ],
        9: [
            "L'échographie ou l'imagerie attend un doute de rupture ou un échec de la charge.",
            "Elle n'est pas le premier geste d'une douleur matinale typique.",
            "Une image normale n'efface pas une rupture clinique évidente.",
            "On ne répète pas l'image chaque semaine si la charge progresse.",
        ],
        10: [
            "Porte du danger : rupture clinique, peau ouverte, pied froid.",
            "Porte du tendon : douleur de charge, matin raide, tendon continu.",
            "Porte de l'action : charge relative, soulagement, revue, ou adresse si rupture.",
        ],
        11: list(DOSE_PAR) + list(DOSE_IBU) + [
            "Le comprimé soulage la douleur. Il ne remplace pas la charge adaptée.",
            "On réduit le volume de course, on ne pose pas un plâtre de confort sans rupture.",
            "On adresse une rupture clinique le jour même.",
            "On revoit si la douleur de marche empire ou si une fossette apparaît.",
        ],
        12: [
            "La marche sans boiterie précède la course.",
            "La course en ligne précède les côtes et les sprints.",
            "On monte le volume par petits paliers, après une douleur de tendon calmée.",
            "On change les chaussures usées et le bond de séances.",
        ],
        13: [
            "Le matin raide qui se réchauffe oriente vers le tendon, pas vers l'entorse.",
            "On serre le mollet avant de rassurer.",
            "Sans rupture, la charge relative vaut mieux que le repos total.",
            "Aucun nombre de répétitions non relu n'est enseigné.",
        ],
        14: [
            "Cas. Une coureuse de 36 ans a mal au tendon le matin, puis la douleur cède en trottinant.",
            "Erreur. Interdire toute charge pendant un mois à cause de la raideur matinale.",
            "Correction. Le tendon est continu et le pied descend au serrage : on adapte la charge et on soulage.",
        ],
    },
    [
        ("alerte", "Chercher la rupture", "Pas de descente du pied au serrage du mollet : on adresse, on ne rassure pas."),
        ("bilan", "Confirmer le tendon", "Douleur de charge, matin raide, tendon continu : tendinopathie."),
        ("age", "Adapter la charge", "On baisse le volume, on garde une charge, on revoit."),
    ],
    [
        NV("tendon", "Tendon", [
            ("Corps", 520, 340, 28, 110, "Milieu du tendon, siège fréquent de la douleur de charge."),
            ("Insertion", 530, 520, 40, 30, "Sur le calcanéus."),
            ("Calcanéus", 540, 600, 70, 36, "Le talon porte l'appui."),
            ("Gaine", 430, 360, 24, 80, "Voisinage du tendon, à ne pas confondre avec une rupture."),
        ]),
        NV("mollet", "Mollet", [
            ("Mollet", 480, 240, 90, 70, "On le serre pour voir si le pied descend."),
            ("Jonction", 500, 360, 40, 30, "Entre muscle et tendon."),
            ("Pied", 620, 560, 70, 30, "La descente du pied signe la continuité."),
            ("Genou", 460, 120, 40, 28, "Le genou est fléchi pendant le serrage."),
        ]),
        NV("charge", "Charge", [
            ("Marche", 300, 400, 70, 36, "Premier palier."),
            ("Course", 520, 400, 70, 36, "Ensuite, en ligne."),
            ("Côte", 720, 400, 60, 36, "Plus tard, avec les sprints."),
            ("Volume", 500, 560, 100, 30, "On regarde les deux dernières semaines."),
        ]),
    ],
    "Quel plan ouvre un tendon douloureux ?",
    [
        "On ouvre le tendon pour le siège de la douleur.",
        "On ouvre le mollet pour le serrage.",
        "On ouvre la charge pour le retour.",
    ],
    M([
        "on demande si les premiers pas du matin sont les pires.",
        "on serre le mollet avant de parler de repos complet.",
        "on palpe le milieu du tendon et l'insertion.",
        "on ne promet pas la course en côte cette semaine.",
        "on relie la douleur au volume des quinze derniers jours.",
        "on compare les deux tendons.",
        "on n'immobilise pas un tendon continu.",
        "on adresse le jour même si le pied ne descend pas.",
        "on garde une marche indolore dans le plan.",
        "on écrit le palier interdit, pas seulement le mot repos.",
    ]),
)

# --- DX.5 LCA ---
ajouter(
    "Rupture du ligament croisé antérieur",
    5,
    [
        "La rupture du ligament croisé antérieur suit souvent un pivot, avec un craquement.",
        "Le genou lâche, gonfle tôt, et le test de Lachman est mou vers 20 degrés.",
        "On n'autorise pas le sport de pivot tant que le genou lâche.",
    ],
    {
        1: [
            "Le ligament croisé antérieur retient le tibia qui part en avant sous le fémur.",
            "La rupture est une perte de cette retenue, pas une simple contusion.",
            "Ce n'est pas toute douleur de genou, et ce n'est pas une entorse bénigne du doigt.",
            "La radiographie normale ne montre pas ce ligament.",
        ],
        2: [
            "Aucune incidence suisse de cette rupture n'a été lue pour ce lot.",
            "Le rang 5 est un rang d'enseignement, parce que le pivot non protégé récidive.",
            "Aucun pourcentage de sensibilité du Lachman n'a été relu.",
        ],
        3: [
            "Le pivot ou la réception en valgus et rotation tend le ligament jusqu'à le rompre.",
            "Le craquement entendu par la personne correspond souvent à cet instant.",
            "Le sang intra-articulaire gonfle le genou dans les premières heures.",
            "Le Lachman se fait genou fléchi d'environ 20 degrés, en comparant l'autre genou.",
            "Un arrêt mou, sans butée, oriente vers la rupture.",
            "La règle du genou dite d'Ottawa n'a pas été relue : elle n'est pas enseignée.",
        ],
        4: [
            "On écarte un genou déformé, une peau ouverte et un pied froid.",
            "On ne force pas l'extension d'un genou vraiment bloqué.",
            "On demande le pivot, le craquement et l'heure du gonflement.",
            "On fait le Lachman des deux côtés, sans chercher un chiffre absent des preuves.",
            "On interdit le sport de pivot tant que le lâchage persiste.",
            "On adresse pour confirmer et discuter la suite, sans inventer un délai opératoire.",
        ],
        5: [
            "On demande le geste : changement de direction, réception, contact.",
            "On demande si un craquement a été senti ou entendu.",
            "On demande si le genou a gonflé dans l'heure ou le lendemain seulement.",
            "On demande les épisodes de lâchage depuis, même courts.",
            "On demande le sport visé, surtout s'il comporte des pivots.",
        ],
        6: [
            "On regarde la marche, le gonflement et un flessum vrai.",
            "On compare le tiroir mou au genou sain, vers 20 degrés de flexion.",
            "On cherche un épanchement précoce.",
            "On ne pousse pas un genou bloqué vers l'extension.",
            "Le dessin situe le genou, le pivot et le blocage. Ce n'est pas une radiographie.",
        ],
        7: [
            "L'entorse du ligament collatéral fait mal sur le côté, sans le même lâchage rotatoire.",
            "La lésion méniscale peut bloquer le genou. On ne force pas l'extension.",
            "La rupture du tendon rotulien empêche l'extension active contre pesanteur.",
            "La contusion osseuse gonfle, sans arrêt mou au Lachman.",
            "La fracture du plateau se cherche s'il y a déformation ou impossibilité d'appui.",
        ],
        8: [
            "On retient le pivot, le craquement, le gonflement précoce et le Lachman mou.",
            "Le genou sain sert de comparaison.",
            "La radiographie normale n'écarte pas la rupture.",
            "Le sport de pivot est contre-indiqué tant que le genou lâche.",
            "Aucun délai opératoire chiffré n'a été relu : on ne l'invente pas.",
        ],
        9: [
            "La radiographie cherche une fracture ou une déformation, pas le ligament.",
            "L'imagerie du ligament vient ensuite, quand elle change l'adresse ou le plan.",
            "On ne la fait pas pour autoriser le match du week-end.",
            "Un genou bloqué non réductible s'adresse, il ne s'image pas seulement au cabinet.",
        ],
        10: [
            "Porte du danger : déformation, peau ouverte, pied froid, blocage vrai.",
            "Porte du croisé : pivot, craquement, gonflement tôt, Lachman mou.",
            "Porte de l'action : pas de pivot, soulagement, adresse, date de revue.",
        ],
        11: list(DOSE_PAR) + list(DOSE_IBU) + [
            "Le comprimé calme la douleur en attendant l'avis spécialisé.",
            "On protège l'appui et on évite le pivot.",
            "On n'autorise pas le football, le ski ou le handball tant que le genou lâche.",
            "On revoit tôt si le blocage, le bleu massif ou l'instabilité s'aggravent.",
        ],
        12: [
            "La marche sans lâchage précède toute course.",
            "La course en ligne précède les appuis latéraux.",
            "Le sport de pivot attend un genou stable et un avis tracé.",
            "On explique au club que la radiographie normale ne vaut pas un feu vert.",
        ],
        13: [
            "Pivot, craquement, gonflement de la première heure, Lachman mou.",
            "On compare toujours à l'autre genou.",
            "On ne force pas un genou bloqué.",
            "On ne signe pas le retour au pivot sur une radiographie normale.",
        ],
        14: [
            "Cas. Une joueuse de 21 ans pivote, entend un craquement, et le genou gonfle dans l'heure.",
            "Erreur. Autoriser le match parce que la radiographie ne montre pas de fracture.",
            "Correction. Le Lachman est mou par rapport à l'autre genou : pas de pivot, et on adresse.",
        ],
    },
    [
        ("alerte", "Écarter le danger", "Déformation, peau ouverte, pied froid ou genou bloqué : on n'étend pas de force."),
        ("bilan", "Tester le croisé", "Pivot, craquement, gonflement tôt, arrêt mou vers 20 degrés."),
        ("age", "Interdire le pivot", "On soulage, on adresse, on ne signe pas le match."),
    ],
    [
        NV("genou", "Genou", [
            ("Fémur", 500, 240, 70, 80, "Partie haute du schéma."),
            ("Tibia", 500, 480, 60, 80, "Part en avant si le croisé lâche."),
            ("Rotule", 500, 360, 36, 28, "Repère antérieur."),
            ("Creux", 640, 400, 40, 36, "Creux poplité, arrière du genou."),
        ]),
        NV("pivot", "Pivot", [
            ("Pied planté", 420, 560, 70, 30, "Le pied reste au sol pendant la rotation."),
            ("Valgus", 560, 400, 50, 40, "Le genou part en dedans dans le mécanisme fréquent."),
            ("Rotation", 500, 300, 80, 36, "Le tronc tourne sur le genou."),
            ("Craquement", 700, 260, 40, 30, "Souvent senti à l'instant de la rupture."),
        ]),
        NV("test", "Test", [
            ("Flexion", 360, 360, 70, 40, "Environ 20 degrés pour le Lachman."),
            ("Arrêt mou", 560, 360, 70, 40, "Pas de butée franche, comparée à l'autre genou."),
            ("Gonflement", 500, 500, 80, 36, "Dans la première heure, on y pense."),
            ("Blocage", 680, 480, 50, 30, "On ne force pas l'extension."),
        ]),
    ],
    "Quel plan ouvre un genou qui lâche ?",
    [
        "On ouvre le genou pour situer le tibia et le fémur.",
        "On ouvre le pivot pour le mécanisme.",
        "On ouvre le test pour le Lachman et le blocage.",
    ],
    M([
        "on demande l'heure du gonflement, pas seulement la douleur.",
        "on compare le Lachman au genou sain.",
        "on n'autorise pas le changement de direction.",
        "on ne force pas l'extension si le genou bloque.",
        "on explique qu'une radiographie normale laisse le ligament invisible.",
        "on protège l'appui douloureux.",
        "on écrit l'interdiction de pivot avec une date de revue.",
        "on cherche un craquement dans le récit.",
        "on ne promet pas une date d'opération.",
        "on adresse plutôt que de signer le prochain match.",
    ]),
)

# --- DX.6 fatigue ---
ajouter(
    "Fracture de fatigue du membre inférieur",
    6,
    [
        "La fracture de fatigue est une douleur d'os qui monte avec les semaines de charge.",
        "Le site change le délai de retour et le risque de complication. [[11]]",
        "On arrête l'impact sur un site à complication haute.",
    ],
    {
        1: [
            "L'os se fissure sous la répétition, pas sous un seul choc.",
            "La douleur est focale, osseuse, et augmente avec la charge.",
            "Ce n'est pas une courbature diffuse du lendemain.",
            "Le membre inférieur regroupe le col fémoral, le tibia, le naviculaire et le métatarse.",
        ],
        2: [
            "Aucune incidence suisse n'a été lue pour ce lot.",
            "Le rang 6 est un rang d'enseignement, parce que le retard complique le col et le naviculaire.",
            "Le retour global lu dépasse 90 % des athlètes. [[11]]",
            "Ce chiffre global n'est pas celui du col fémoral. [[11]]",
        ],
        3: [
            "La charge répétée dépasse la réparation de l'os.",
            "Un bond de volume, un changement de surface ou un déficit d'apports favorisent la fissure.",
            "Le col fémoral et le naviculaire ont les délais groupés les plus longs. [[11]]",
            "Le tibia postéro-médial et la fibula ont les délais les plus courts dans la même revue. [[11]]",
        ],
        4: [
            "On écarte une douleur thoracique, une fièvre et un membre froid.",
            "On demande depuis combien de semaines la douleur d'os monte.",
            "On demande si le saut sur place réveille exactement le même point.",
            "On arrête l'impact si le site est le col, le naviculaire, le tibia antérieur ou le cinquième métatarsien. [[11]]",
            "On demande les apports, le poids et les règles, parce que l'énergie basse fragilise l'os. [[7]]",
            "On n'autorise pas la course en attendant une image parfaite.",
        ],
        5: [
            "On demande le volume des semaines récentes et le changement de chaussures ou de sol.",
            "On demande le point exact, pas une zone floue de toute la jambe.",
            "On demande les fractures de fatigue anciennes.",
            "On demande les règles absentes, la restriction alimentaire et la perte de poids. [[7]]",
            "On demande le prochain départ, pour écrire une interdiction datée.",
        ],
        6: [
            "On palpe l'os, un doigt sur le point douloureux.",
            "On demande un saut sur place si l'appui simple est encore possible.",
            "On regarde la marche et une boiterie d'impact.",
            "Le dessin situe le col, le tibia et le pied. Ce n'est pas une scintigraphie.",
            "Une douleur de hanche ou d'aine chez un coureur fait penser au col.",
        ],
        7: [
            "La périostite ou l'attelle tibiale est plus étendue que le point d'un doigt.",
            "L'entorse a un début brutal en inversion. [[2]]",
            "La tendinopathie d'Achille siège sur le tendon, pas dans l'os.",
            "Le déficit énergétique peut accompagner la fissure. Il se cherche en même temps. [[7]]",
            "Une tumeur ou une infection se discutent si la douleur nocturne ou la fièvre dominent.",
        ],
        8: [
            "Le délai groupé lu du naviculaire est de 127 jours, intervalle 102 à 151. [[11]]",
            "Le délai groupé lu du col fémoral est de 107 jours, intervalle 79 à 135. [[11]]",
            "Le tibia postéro-médial est à 44 jours, intervalle 27 à 61. [[11]]",
            "La fibula est à 56 jours, intervalle 13 à 100. [[11]]",
            "Les complications les plus hautes concernent le col, le naviculaire, le tibia antérieur et le cinquième métatarsien. [[11]]",
            "Le taux de retour lu du col fémoral est de 55,3 %, pas le taux global. [[11]]",
            "Aucune indication opératoire chiffrée n'est transformée en obligation.",
        ],
        9: [
            "La radiographie précoce peut être insuffisante. L'imagerie suit si elle change la conduite.",
            "On n'attend pas une image pour arrêter l'impact sur un site à haut risque. [[11]]",
            "Le choix entre appui protégé et avis chirurgical dépend du site et du déplacement, pas d'une règle unique.",
            "On revoit tôt un col fémoral douloureux.",
        ],
        10: [
            "Porte du danger : col fémoral, douleur nocturne avec fièvre, membre froid.",
            "Porte du site : haut risque de complication ou site à délai plus court. [[11]]",
            "Porte de l'action : arrêt de l'impact, bilan d'apports, image utile, revue.",
        ],
        11: list(DOSE_PAR) + list(DOSE_IBU) + [
            "Le comprimé calme. Il ne répare pas l'os et il n'autorise pas la course.",
            "On arrête les sauts et la course sur un site à complication haute. [[11]]",
            "On adresse le col fémoral et le naviculaire sans attendre la fin de saison.",
            "On corrige les apports si le récit alimentaire est bas. [[7]]",
            "On revoit si la douleur d'appui empire ou si la fièvre apparaît.",
        ],
        12: [
            "L'impact ne reprend qu'après une marche indolore.",
            "On allonge le calendrier sur le naviculaire et le col, selon les délais lus. [[11]]",
            "On monte ensuite par petits paliers, pas par un semi-marathon test.",
            "On surveille les règles et les apports pendant la montée de charge. [[7]]",
        ],
        13: [
            "Douleur d'os focale, semaines de charge, saut douloureux.",
            "Col, naviculaire, tibia antérieur et cinquième métatarsien : on arrête l'impact. [[11]]",
            "Le retour global au-dessus de 90 % ne s'applique pas au col. [[11]]",
            "On demande l'énergie, pas seulement la chaussure. [[7]]",
        ],
        14: [
            "Cas. Un coureur de 28 ans a une douleur du naviculaire depuis quatre semaines, et le saut la réveille.",
            "Erreur. Le laisser finir la course parce que la première radiographie ne montre rien.",
            "Correction. Site à complication haute : on arrête l'impact et on adresse, sans attendre une image rassurante. [[11]]",
        ],
    },
    [
        ("alerte", "Arrêter l'impact", "Col, naviculaire, tibia antérieur ou cinquième métatarsien : plus de sauts. [[11]]"),
        ("bilan", "Nommer le site", "Le délai lu dépend du site. Le col n'a pas le taux de retour global. [[11]]"),
        ("age", "Revoir et nourrir", "On adresse le haut risque, on demande les apports, on date la revue."),
    ],
    [
        NV("hanche", "Hanche", [
            ("Col", 420, 360, 70, 36, "Douleur d'aine à la charge. Délai long, retour moins fréquent."),
            ("Tête", 520, 300, 46, 46, "Voisine du col sur le schéma."),
            ("Aine", 360, 460, 50, 30, "Siège de plainte fréquent."),
            ("Appui", 500, 600, 80, 24, "L'impact se retire."),
        ]),
        NV("tibia", "Tibia", [
            ("Bord antérieur", 460, 320, 28, 120, "Site à complication haute."),
            ("Bord interne", 560, 360, 28, 110, "Postéro-médial, délai plus court dans la revue."),
            ("Fibula", 660, 400, 22, 90, "Délai court, complication plus basse."),
            ("Genou", 500, 160, 40, 24, "Repère haut."),
        ]),
        NV("pied", "Pied", [
            ("Naviculaire", 460, 340, 46, 32, "Délai groupé le plus long de la revue."),
            ("Cinquième", 300, 460, 70, 24, "Base et diaphyse : complication haute."),
            ("Calcanéus", 560, 520, 50, 30, "Douleur de talon à distinguer du tendon."),
            ("Saut", 480, 620, 80, 24, "Le saut sur place réveille le point."),
        ]),
    ],
    "Quel plan ouvre une douleur d'os ?",
    [
        "On ouvre la hanche si l'aine ou le col est en cause.",
        "On ouvre le tibia si la jambe est le siège.",
        "On ouvre le pied si le médio-pied ou le métatarse est douloureux.",
    ],
    M([
        "on palpe un seul point d'os, pas toute la jambe.",
        "on demande si le saut réveille exactement ce point.",
        "on arrête la course quand le site est à complication haute.",
        "on ne rassure pas avec une radiographie précoce normale.",
        "on demande les apports et les règles.",
        "on sépare le délai du naviculaire de celui de la fibula.",
        "on n'applique pas le retour global au col fémoral.",
        "on écrit l'interdiction d'impact avec une date.",
        "on adresse le col sans finir la saison.",
        "on ne promet pas un délai opératoire chiffré.",
    ]),
)

# --- DX.7 bronches ---
ajouter(
    "Bronchoconstriction induite par l'exercice",
    7,
    [
        "La bronchoconstriction d'effort se prouve par le souffle, pas par la toux seule. [[8]]",
        "Le critère lu est une baisse du volume expiratoire d'au moins 10 %. [[8]]",
        "La prévention lue chez l'adulte est de 2 inhalations avant l'activité. [[14]]",
    ],
    {
        1: [
            "C'est un rétrécissement des bronches déclenché par l'effort, mesuré par le souffle. [[8]]",
            "La toux, le sifflement ou la gêne ne suffisent ni à affirmer ni à écarter le diagnostic. [[8]]",
            "Ce n'est pas une douleur d'os, et ce n'est pas une douleur thoracique constrictive.",
            "Le code de la situation reste celui de la visite d'avant ou d'après l'effort.",
        ],
        2: [
            "Aucune prévalence suisse n'a été lue pour ce lot.",
            "Le rang 7 est un rang d'enseignement, fréquent à l'air froid.",
            "Le critère de 10 % vient de la recommandation de 2013. [[8]]",
        ],
        3: [
            "L'hyperventilation d'air sec refroidit et assèche les bronches. [[8]]",
            "Le muscle lisse se contracte, et le volume expiratoire chute après l'effort. [[8]]",
            "La mesure utile est le plus bas volume dans les 30 minutes, comparé à l'avant. [[8]]",
            "Des épreuves de remplacement existent : hyperpnée, sérum salé à 4,5 %, mannitol. [[8]]",
        ],
        4: [
            "On écarte d'abord une détresse, une douleur thoracique et une syncope.",
            "On ne conclut pas sur la toux. On prévoit une mesure. [[8]]",
            "En attendant, un essoufflement au repos ou une parole impossible font sortir de la piste simple.",
            "Si le diagnostic est déjà connu, on vérifie la prise avant l'effort et le besoin du jour. [[14]]",
            "On n'augmente pas seul le nombre de prises au-delà de l'autorisation.",
        ],
        5: [
            "On demande la toux, le sifflement et la gêne à l'air froid ou après l'arrêt.",
            "On demande si cela cède au repos en moins d'une heure.",
            "On demande les traitements déjà pris et le nombre de prises du jour.",
            "On demande les allergies et les crises nocturnes.",
            "On demande le sport, surtout la course et le ski.",
        ],
        6: [
            "On écoute le souffle au repos et on regarde la parole.",
            "On ne fait pas courir une personne déjà en détresse pour prouver la piste.",
            "Le VEMS (volume expiratoire maximal seconde) se mesure avant, puis dans les 30 minutes. [[8]]",
            "Le dessin situe la bronche, l'effort et l'inhalateur. Ce n'est pas une radiographie.",
        ],
        7: [
            "La cardiopathie donne une douleur, une syncope ou une palpitation, pas seulement une toux. [[6]]",
            "Le déconditionnement essouffle sans la chute mesurée du volume.",
            "L'hyperventilation sans rétrécissement ne baisse pas le volume de 10 %. [[8]]",
            "Une infection aiguë se cherche si la fièvre et les crachats dominent.",
            "Le coup de chaleur associe un trouble neurologique et une température haute. [[10]]",
        ],
        8: [
            "La baisse d'au moins 10 % du volume, dans les 30 minutes, pose le diagnostic. [[8]]",
            "La forme légère va de 10 % inclus à moins de 25 %. [[8]]",
            "La forme modérée va de 25 % inclus à moins de 50 %. [[8]]",
            "La forme sévère atteint ou dépasse 50 %. [[8]]",
            "Beaucoup de laboratoires retiennent 15 % pour une spécificité plus grande. [[8]]",
            "Les symptômes seuls ne sont ni sensibles ni spécifiques. [[8]]",
        ],
        9: [
            "On mesure le volume. On ne se fie pas au seul débit de pointe si le volume est disponible. [[8]]",
            "L'épreuve d'effort ventilatoire suit les conditions lues de 2013, en laboratoire. [[8]]",
            "Le sérum salé à 4,5 % ou le mannitol remplacent l'effort si besoin. [[8]]",
            "On n'ordonne pas une course test au bord du terrain chez une personne en détresse.",
        ],
        10: [
            "Porte du danger : détresse, douleur thoracique, syncope, parole impossible.",
            "Porte de la mesure : baisse d'au moins 10 % dans les 30 minutes. [[8]]",
            "Porte de l'action : inhalation avant l'effort selon l'autorisation, et revue si le jour dépasse le plafond lu.",
        ],
        11: list(DOSE_SALBU) + [
            "Cette prévention est celle du nébuliseur-doseur de l'autorisation 37397, pas d'un autre dispositif.",
            "On n'écrit pas ici un plafond d'agence antidopage. L'ordonnance reste l'autorisation suisse.",
            "Si le besoin dépasse la ligne lue, la personne voit son médecin. [[14]]",
            "Un échauffement peut diminuer la gêne. Il ne remplace pas la mesure. [[8]]",
            "On revoit si les prises deviennent quotidiennes ou si la détresse apparaît.",
        ],
        12: [
            "On évite l'air le plus froid et le plus sec au début du plan, sans prétendre guérir.",
            "L'échauffement progressif précède l'effort intense. [[8]]",
            "On vérifie la technique d'inhalation à chaque visite.",
            "On ne signe pas un sport en salle fermée si la détresse au repos persiste.",
        ],
        13: [
            "On mesure, on ne devine pas sur la toux. [[8]]",
            "Au moins 10 % de baisse dans les 30 minutes. [[8]]",
            "15 % est un critère de laboratoire pour plus de spécificité, pas une autre maladie. [[8]]",
            "Adulte : 2 inhalations avant l'activité. De 4 à 12 ans : 1 inhalation sur ce dispositif. [[14]]",
        ],
        14: [
            "Cas. Une skieuse de 19 ans tousse à l'air froid et demande un certificat sur ce seul récit.",
            "Erreur. Affirmer la bronchoconstriction sans mesure du volume.",
            "Correction. On mesure la baisse dans les 30 minutes, et on n'utilise l'inhalateur préventif que selon l'autorisation. [[8]]",
        ],
    },
    [
        ("alerte", "Écarter la détresse", "Douleur thoracique, syncope ou parole impossible : on quitte la piste simple."),
        ("bilan", "Mesurer le volume", "Baisse d'au moins 10 % dans les 30 minutes, sinon on ne conclut pas. [[8]]"),
        ("age", "Prévenir selon l'autorisation", "2 inhalations adultes avant l'activité sur le nébuliseur-doseur lu. [[14]]"),
    ],
    [
        NV("bronche", "Bronche", [
            ("Trachée", 500, 220, 28, 50, "Repère haut."),
            ("Bronche", 420, 360, 80, 28, "Le calibre chute après l'effort sec."),
            ("Poumon", 620, 400, 90, 80, "Le volume se mesure, il ne se devine pas."),
            ("Air froid", 300, 300, 40, 30, "Déclencheur fréquent du récit."),
        ]),
        NV("mesure", "Mesure", [
            ("Avant", 280, 360, 70, 40, "Volume de départ."),
            ("Effort", 500, 360, 70, 40, "Hyperventilation d'air sec."),
            ("Après", 720, 360, 70, 40, "Plus bas volume dans les 30 minutes."),
            ("Dix", 500, 520, 60, 30, "La baisse d'au moins 10 % est le critère lu."),
        ]),
        NV("prise", "Prise", [
            ("Inhalateur", 420, 360, 80, 36, "Nébuliseur-doseur de l'autorisation lue."),
            ("Adulte", 640, 300, 60, 30, "Deux inhalations avant l'activité."),
            ("Enfant", 640, 420, 60, 30, "Une inhalation de 4 à 12 ans sur ce dispositif."),
            ("Plafond", 480, 540, 80, 28, "Au-delà de 800 microgrammes du jour, prévenir le médecin."),
        ]),
    ],
    "Quel plan ouvre une gêne d'effort ?",
    [
        "On ouvre la bronche pour le mécanisme.",
        "On ouvre la mesure avant de conclure.",
        "On ouvre la prise seulement si l'autorisation correspond.",
    ],
    M([
        "on ne conclut pas sur une toux à l'air froid.",
        "on prévoit la mesure du volume avant et après l'effort.",
        "on sépare une gêne bronchique d'une douleur d'os.",
        "on vérifie le dispositif avant de dire le nombre d'inhalations.",
        "on demande combien de prises ont déjà eu lieu aujourd'hui.",
        "on n'envoie pas courir une personne qui ne peut plus parler.",
        "on écrit la prévention avant l'activité, pas un traitement au long cours inventé.",
        "on revoit si le besoin devient quotidien.",
        "on rappelle que 15 % est un critère de laboratoire.",
        "on n'ajoute pas un plafond antidopage à l'ordonnance.",
    ]),
    teaser11="L'inhalation vient de l'autorisation suisse.",
)

# --- DX.8 cœur ---
ajouter(
    "Cardiopathie à risque pendant l'effort",
    8,
    [
        "Cette piste cherche une maladie qui rend l'effort dangereux.",
        "Chez le jeune compétiteur, on associe l'histoire, l'examen et le tracé. [[6]]",
        "Une syncope, une douleur thoracique ou une palpitation d'effort arrêtent le certificat.",
    ],
    {
        1: [
            "C'est une maladie cardiaque qui peut tuer ou défaillir pendant l'effort.",
            "Chez le jeune, on pense aux cardiomyopathies, aux canalopathies et aux anomalies coronaires. [[6]]",
            "Plus tard, la maladie coronaire athéroscléreuse devient la cause dominante. [[6]]",
            "Ce n'est pas un test de performance, et ce n'est pas une aptitude signée sur un sourire.",
        ],
        2: [
            "Aucune incidence suisse de mort subite du sport n'a été lue pour ce lot.",
            "Le rang 8 est un rang d'enseignement : rare, et décisif pour l'aptitude.",
            "Le tracé, lu avec les standards actuels, fait mieux que l'histoire et l'examen seuls. [[6]]",
        ],
        3: [
            "L'effort augmente le débit, la pression et le risque d'un trouble du rythme.",
            "Une coronaire anormale ou un muscle malade supporte mal cette hausse.",
            "Après 35 ans, la plaque coronaire explique davantage les accidents. [[6]]",
            "Une hypertension mal contrôlée fait reporter l'effort maximal. [[6]]",
        ],
        4: [
            "On demande d'abord la syncope, la douleur de poitrine, la palpitation et l'essoufflement hors proportion. [[6]]",
            "Si l'un de ces signes existe à l'effort, on ne signe pas l'aptitude.",
            "Chez le compétiteur jeune, on ajoute l'examen et le tracé à 12 dérivations. [[6]]",
            "On ne demande pas une échographie de routine. [[6]]",
            "Après 35 ans, on ne demande pas une épreuve d'effort de routine chez l'asymptomatique. [[6]]",
            "On la réserve à la personne symptomatique ou à haut risque coronaire. [[6]]",
        ],
        5: [
            "On demande les morts subites et les maladies cardiaques de la famille proche. [[6]]",
            "On demande les syncopes pendant ou juste après l'effort.",
            "On demande les douleurs de poitrine à l'effort, même brèves.",
            "On demande les palpitations et l'essoufflement sans rapport avec l'intensité. [[6]]",
            "On demande les médicaments et la pression connue.",
        ],
        6: [
            "On ausculte le cœur, on prend la pression au repos et on cherche un souffle. [[6]]",
            "L'ECG (électrocardiogramme) à 12 dérivations se lit avec les standards actuels. [[6]]",
            "On cherche des signes de tissu fragile et des pouls fémoraux faibles. [[6]]",
            "Au moins 2 extrasystoles au repos, ou au moins 1 chez l'endurant de haut niveau, ouvrent un bilan. [[6]]",
            "Le dessin situe le cœur et les portes du récit. Ce n'est pas un tracé réel.",
        ],
        7: [
            "La bronchoconstriction se mesure par le volume, et elle ne fait pas syncope. [[8]]",
            "Le déconditionnement essouffle en proportion de l'effort, sans douleur constrictive.",
            "La commotion donne un trouble neurologique après un choc, pas une douleur d'effort. [[4]]",
            "Le coup de chaleur associe la chaleur et le trouble neurologique. [[10]]",
            "Une douleur pariétale est reproduite à la palpation, sans syncope.",
        ],
        8: [
            "On ne signe pas si la syncope, la douleur thoracique, la palpitation ou la dyspnée disproportionnée existent. [[6]]",
            "Le dépistage du jeune compétiteur n'est pas l'examen seul. [[6]]",
            "L'échographie n'est pas recommandée en routine. [[6]]",
            "L'épreuve d'effort de routine n'est pas recommandée chez l'asymptomatique de plus de 35 ans. [[6]]",
            "Si la pression systolique au repos dépasse 160 mmHg, on reporte l'effort maximal. [[6]]",
            "Le bilan des extrasystoles suit le nombre lu sur le tracé de repos. [[6]]",
        ],
        9: [
            "Le tracé de repos précède l'épreuve d'effort. [[6]]",
            "L'épreuve d'effort attend un symptôme ou un risque coronaire élevé. [[6]]",
            "L'échographie attend une raison, pas un certificat de routine. [[6]]",
            "On n'invente pas une liste de 14 questions qui n'a pas été relue.",
        ],
        10: [
            "Porte du danger : syncope, douleur thoracique, palpitation, essoufflement hors proportion.",
            "Porte du tracé : histoire, examen, électrocardiogramme chez le jeune compétiteur. [[6]]",
            "Porte de l'action : on ne signe pas, on traite la pression, ou on adresse.",
        ],
        11: [
            "Aucune dose médicamenteuse n'est enseignée pour signer ou pour lever cette interdiction.",
            "On reporte l'effort maximal tant que la pression systolique de repos dépasse 160 mmHg. [[6]]",
            "On adresse la syncope d'effort et le tracé anormal.",
            "On écrit l'inaptitude provisoire avec le motif et la date de revue.",
            "On ne rassure pas avec un examen normal si le récit d'effort est parlant. [[6]]",
        ],
        12: [
            "Le compétiteur jeune a une histoire, un examen et un tracé avant la saison. [[6]]",
            "On redemande les symptômes à chaque renouvellement.",
            "On traite la pression avant un test maximal. [[6]]",
            "Le club ne fait pas courir un joueur syncope en attendant le papier.",
        ],
        13: [
            "Symptôme d'effort : pas de certificat. [[6]]",
            "Tracé meilleur que l'histoire seule chez le jeune, avec les standards actuels. [[6]]",
            "Pas d'échographie de routine. [[6]]",
            "Pas d'épreuve d'effort de routine après 35 ans sans symptôme. [[6]]",
            "Pression systolique au-dessus de 160 mmHg : on reporte l'effort maximal. [[6]]",
        ],
        14: [
            "Cas. Un compétiteur de 16 ans a perdu connaissance à la fin d'un sprint et veut son papier.",
            "Erreur. Signer parce que l'auscultation du jour est brève et qu'il va bien assis.",
            "Correction. La syncope d'effort arrête l'aptitude. On complète l'histoire, l'examen et le tracé, puis on adresse. [[6]]",
        ],
    },
    [
        ("alerte", "Arrêter le certificat", "Syncope, douleur thoracique, palpitation ou essoufflement hors proportion."),
        ("bilan", "Lire le tracé", "Histoire, examen et électrocardiogramme chez le jeune compétiteur. [[6]]"),
        ("age", "Reporter l'effort maximal", "Pression systolique de repos au-dessus de 160 mmHg : on contrôle d'abord. [[6]]"),
    ],
    [
        NV("coeur", "Cœur", [
            ("Cœur", 430, 390, 70, 55, "On ausculte avant de signer."),
            ("Aorte", 500, 250, 24, 50, "Repère du schéma, pas une mesure."),
            ("Poumon", 650, 380, 70, 60, "L'essoufflement hors proportion s'y raconte."),
            ("Sternum", 520, 300, 20, 60, "Repère médian."),
        ]),
        NV("recit", "Récit", [
            ("Syncope", 260, 320, 70, 36, "Pendant ou juste après l'effort : on ne signe pas."),
            ("Douleur", 480, 320, 70, 36, "Poitrine à l'effort."),
            ("Palpitation", 700, 320, 70, 36, "Battements anormaux ressentis à l'effort."),
            ("Famille", 480, 500, 90, 30, "Morts subites et maladies cardiaques proches."),
        ]),
        NV("trace", "Tracé", [
            ("Repos", 300, 360, 70, 36, "Tracé à 12 dérivations."),
            ("Extrasystoles", 560, 360, 80, 36, "Au moins deux au repos ouvrent un bilan."),
            ("Pression", 420, 520, 70, 30, "Au-dessus de 160 au repos, on reporte le test maximal."),
            ("Épreuve", 680, 520, 70, 30, "Pas en routine si la personne de plus de 35 ans est asymptomatique."),
        ]),
    ],
    "Quel plan ouvre une aptitude ?",
    [
        "On ouvre le cœur pour l'examen.",
        "On ouvre le récit avant le papier.",
        "On ouvre le tracé si le compétiteur est jeune ou si un signe existe.",
    ],
    M([
        "on demande la syncope avant de prendre le stylo.",
        "on demande les morts subites dans la famille proche.",
        "on ne commande pas une échographie par habitude.",
        "on ne commande pas une épreuve d'effort chez l'asymptomatique plus âgé.",
        "on mesure la pression au repos avant un test maximal.",
        "on compte les extrasystoles du tracé de repos.",
        "on écrit une inaptitude provisoire plutôt qu'un feu vert gêné.",
        "on sépare un essoufflement proportionné d'une dyspnée anormale.",
        "on ausculte vraiment, on ne coche pas la case de loin.",
        "on adresse un tracé anormal au lieu de le commenter seul.",
    ]),
    teaser11="Aucune dose ne signe l'aptitude.",
)

# --- DX.9 énergie ---
ajouter(
    "Déficit énergétique relatif dans le sport",
    9,
    [
        "Le déficit énergétique relatif touche les femmes et les hommes. [[7]]",
        "Il vient d'apports trop bas, trop longtemps ou trop fort, pour la charge. [[7]]",
        "Il n'existe pas un seul test. Les indicateurs graves font protéger. [[7]]",
    ],
    {
        1: [
            "C'est un trouble physiologique ou psychologique lié à une disponibilité énergétique trop basse. [[7]]",
            "Le mot problématique veut dire prolongé, sévère, ou les deux. [[7]]",
            "Les suites touchent le métabolisme, les règles, l'os, l'immunité et le cœur. [[7]]",
            "Ce n'est pas une simple volonté de maigrir sans conséquence.",
        ],
        2: [
            "Aucune prévalence suisse n'a été lue pour ce lot.",
            "Le rang 9 est un rang d'enseignement, parce que la charge monte souvent sans qu'on demande les apports.",
            "Le consensus a été accepté le 20 août 2023. [[7]]",
        ],
        3: [
            "La disponibilité énergétique est ce qui reste pour la santé après la dépense d'exercice. [[7]]",
            "Une baisse brève peut être adaptable. La forme problématique casse des fonctions. [[7]]",
            "L'os, les règles, l'humeur et la performance peuvent tomber ensemble. [[7]]",
            "Chaque indicateur a d'autres causes : on les cherche avant de tout attribuer à l'énergie. [[7]]",
        ],
        4: [
            "On demande les apports, la charge, le poids et les règles ou la libido.",
            "On classe ensuite selon quatre couleurs, pas selon une impression. [[7]]",
            "Le vert autorise l'entraînement et la compétition. [[7]]",
            "Le jaune poursuit la surveillance. [[7]]",
            "L'orange intensifie le soin et la surveillance. [[7]]",
            "Le rouge fait envisager le retrait de la compétition et de l'entraînement. [[7]]",
        ],
        5: [
            "On demande si les apports ont baissé pendant que le volume montait.",
            "On demande les règles absentes, la fatigue, les fractures de fatigue et l'humeur. [[7]]",
            "On demande les malaises, les syncopes et les vomissements.",
            "On demande qui pèse, qui commente le corps, et si la personne mange seule.",
            "On demande les deux sexes le même récit. [[7]]",
        ],
        6: [
            "On pèse, on mesure, et on calcule l'IMC (indice de masse corporelle).",
            "On prend la pression couchée puis debout.",
            "On prend le pouls et on lit un tracé si le pouls est très bas ou si un malaise existe. [[7]]",
            "On cherche les signes graves avant de parler de volume d'entraînement.",
            "Le dessin situe l'énergie, l'os et les quatre couleurs. Ce n'est pas une balance connectée.",
        ],
        7: [
            "Une maladie digestive, une infection ou une dépression peuvent baisser les apports sans ce cadre.",
            "La fracture de fatigue peut être le premier signe osseux. [[11]]",
            "La cardiomyopathie se cherche si le tracé ou la syncope ne collent pas au seul déficit. [[6]]",
            "Une grossesse se discute devant un retard de règles, avant d'attribuer tout à la charge.",
            "L'hyperthyroïdie maigrit avec d'autres signes. Elle n'est pas ce consensus.",
        ],
        8: [
            "Aucun test unique ne pose le diagnostic. [[7]]",
            "L'IMC à 75 % de la médiane d'âge et de sexe, ou en dessous, est un indicateur grave. [[7]]",
            "Un trouble des électrolytes est un indicateur grave. [[7]]",
            "Un tracé anormal ou un pouls très bas sont des indicateurs graves. [[7]]",
            "Chez l'adulte, un pouls de 30 battements ou moins entre dans ce cadre. [[7]]",
            "Chez l'adolescent, le chiffre lu est de 45 battements ou moins. [[7]]",
            "Une pression à 90/45 mmHg ou en dessous est un indicateur grave. [[7]]",
            "La chute au lever dépasse 20 mmHg pour la systolique et 10 mmHg pour la diastolique. [[7]]",
        ],
        9: [
            "Le bilan sanguin cherche les électrolytes et les autres causes, il ne remplace pas le récit.",
            "Le tracé cherche la bradycardie sévère et un allongement dangereux. [[7]]",
            "L'os s'image si une douleur osseuse ou une fracture de fatigue est là. [[11]]",
            "On n'utilise pas un seul questionnaire comme diagnostic. [[7]]",
        ],
        10: [
            "Porte du danger : indicateur grave, syncope, trouble ionique, tracé anormal.",
            "Porte des couleurs : vert, jaune, orange, rouge. [[7]]",
            "Porte de l'action : manger plus, charger moins, surveiller, ou retirer du jeu.",
        ],
        11: [
            "Aucune dose de ce lot ne traite le déficit. Le premier geste est de restaurer l'énergie. [[7]]",
            "On augmente les apports et on baisse la charge, avec un suivi.",
            "Un indicateur grave fait envisager l'hôpital et le retrait de l'entraînement. [[7]]",
            "L'échec d'un soin ambulatoire du trouble alimentaire est un indicateur grave. [[7]]",
            "On n'écrit pas un patch hormonal : ce n'est pas l'autorisation recopiée ici.",
            "On revoit le poids, les règles ou la libido, et l'humeur.",
        ],
        12: [
            "On demande les apports avant d'augmenter le volume. [[7]]",
            "Le club ne commente pas le corps comme une consigne d'entraînement.",
            "On surveille l'os chez la personne qui a déjà fissuré. [[11]]",
            "Les deux sexes reçoivent la même question. [[7]]",
        ],
        13: [
            "Prolongé ou sévère : disponibilité énergétique trop basse. [[7]]",
            "Quatre couleurs, du jeu complet au retrait envisagé. [[7]]",
            "Pas de test unique. [[7]]",
            "Indicateurs graves : médiane d'IMC, ions, tracé, pression, lever. [[7]]",
            "On nourrit et on allège la charge avant d'ajouter un médicament.",
        ],
        14: [
            "Cas. Une coureuse de 19 ans n'a plus de règles, mange peu, et le volume a doublé.",
            "Erreur. Lui dire de s'entraîner plus pour rester légère.",
            "Correction. On cherche les indicateurs graves, on remonte les apports et on baisse la charge. [[7]]",
        ],
    },
    [
        ("alerte", "Repérer le grave", "Syncope, ions anormaux, tracé anormal ou pression très basse : on protège. [[7]]"),
        ("bilan", "Choisir la couleur", "Vert, jaune, orange ou rouge, après avoir écarté les autres causes. [[7]]"),
        ("age", "Restaurer l'énergie", "Plus d'apports, moins de charge, et une revue. Pas un médicament de ce lot."),
    ],
    [
        NV("energie", "Énergie", [
            ("Apports", 320, 360, 70, 40, "Ce qui est mangé."),
            ("Charge", 560, 360, 70, 40, "Ce qui est dépensé à l'entraînement."),
            ("Reste", 440, 500, 80, 36, "Ce qui devrait nourrir la santé."),
            ("Durée", 640, 500, 60, 30, "Prolongé ou sévère : forme problématique."),
        ]),
        NV("os", "Os", [
            ("Os", 480, 400, 80, 50, "Les fissures répétées font chercher l'énergie."),
            ("Règles", 300, 300, 60, 30, "Un arrêt de règles entre dans le récit."),
            ("Humeur", 660, 300, 60, 30, "Peut précéder ou suivre le déficit."),
            ("Poids", 480, 560, 70, 28, "On le mesure, on ne le commente pas comme un objectif de maigreur."),
        ]),
        NV("couleur", "Couleur", [
            ("Vert", 220, 360, 50, 36, "Entraînement et compétition."),
            ("Jaune", 400, 360, 50, 36, "Surveillance."),
            ("Orange", 580, 360, 50, 36, "Soin intensif et surveillance."),
            ("Rouge", 740, 360, 50, 36, "Retrait envisagé de la compétition et de l'entraînement."),
        ]),
    ],
    "Quel plan ouvre un récit d'apports bas ?",
    [
        "On ouvre l'énergie pour le déséquilibre.",
        "On ouvre l'os si une fissure ou un arrêt de règles existe.",
        "On ouvre la couleur pour la décision de jeu.",
    ],
    M([
        "on demande les apports avant d'augmenter les séances.",
        "on pose la même question aux deux sexes.",
        "on cherche une autre cause à chaque indicateur.",
        "on pèse et on mesure avant de commenter.",
        "on prend la pression couchée puis debout.",
        "on ne promet pas une performance par une restriction.",
        "on envisage le retrait si un indicateur grave est là.",
        "on relie une fissure d'os au récit alimentaire.",
        "on n'ajoute pas un médicament à la place du repas.",
        "on fixe une revue du poids et des règles ou de la libido.",
    ]),
    teaser11="On restaure l'énergie, sans dose de ce lot.",
)

# --- DX.10 chaleur ---
ajouter(
    "Coup de chaleur d'effort",
    10,
    [
        "Le coup de chaleur grave associe un trouble neurologique et une température centrale haute. [[9]]",
        "On refroidit sur place avant de transporter. [[9]]",
        "La cible des Jeux descend sous 39,0 °C. [[9]]",
        "La fourchette lue en 2024 va de 38,5 à 39,0 °C. [[10]]",
    ],
    {
        1: [
            "C'est une urgence de thermorégulation pendant ou juste après l'effort. [[10]]",
            "La forme sévère comporte un trouble du système nerveux et une température souvent au-dessus de 40,0 °C. [[10]]",
            "La forme légère empêche de continuer, sans ce trouble neurologique. [[10]]",
            "Ce n'est pas une fièvre infectieuse isolée, et ce n'est pas une crampe de mollet.",
        ],
        2: [
            "Aucune incidence suisse n'a été lue pour ce lot.",
            "Le rang 10 est un rang d'enseignement : moins fréquent, et immédiatement grave.",
            "Le temps passé à température haute aggrave les dégâts. [[10]]",
        ],
        3: [
            "Le muscle produit plus de chaleur que la peau n'en évacue. [[9]]",
            "L'air chaud, l'humidité, les vêtements et l'équipement réduisent cette évacuation.",
            "Le cerveau dysfonctionne quand la température centrale reste trop haute. [[10]]",
            "Une température rectale est la mesure pratique retenue sur le terrain. [[9]]",
        ],
        4: [
            "On reconnaît tôt : confusion, agressivité, chute, crise ou perte de connaissance. [[9]]",
            "On mesure la température centrale si on le peut, sans retarder le refroidissement sinon. [[10]]",
            "On refroidit sur place, avant le transport. [[9]]",
            "L'immersion dans l'eau froide, jusqu'au cou, est le moyen préféré de la forme sévère. [[10]]",
            "On surveille la température pendant l'immersion. [[10]]",
            "Les troubles du rythme et le choc cardiogénique sont des contre-indications relatives. [[10]]",
        ],
        5: [
            "On demande l'effort, la chaleur du lieu, l'équipement et l'heure de la confusion.",
            "On demande les vomissements, la soif et les urines.",
            "On demande une crise, une chute et un comportement bizarre. [[9]]",
            "On demande les maladies et les médicaments, sans retarder le bain.",
            "Un témoin raconte si la personne ne peut plus parler.",
        ],
        6: [
            "On regarde la vigilance, la peau, la marche et la température centrale. [[10]]",
            "La forme légère a souvent une température entre 38,5 et 40,0 °C, sans trouble neurologique. [[10]]",
            "La forme sévère a souvent une température au-dessus de 40,0 °C avec ce trouble. [[10]]",
            "On ne se fie pas au thermomètre buccal ou cutané pour trancher. [[10]]",
            "Le dessin situe la chaleur, le bain et le transport. Ce n'est pas une courbe réelle.",
        ],
        7: [
            "La commotion suit un choc et n'a pas cette température. [[4]]",
            "L'hypoglycémie et l'hyponatrémie d'effort se cherchent si le prélèvement n'interrompt pas le bain. [[9]]",
            "Une infection fébrile n'a pas le même contexte d'effort maximal en chaleur.",
            "Un arrêt cardiaque se réanime d'abord. L'immersion a ses contre-indications relatives. [[10]]",
            "La crise peut venir de la chaleur elle-même. [[10]]",
        ],
        8: [
            "Le texte des Jeux arrête l'immersion quand la température rectale passe sous 39,0 °C. [[9]]",
            "Le consensus de 2024 arrête l'immersion entre 38,5 et 39,0 °C. [[10]]",
            "Ces deux cibles sont citées séparément. On n'en fabrique pas une troisième.",
            "La forme légère se décrit entre 38,5 et 40,0 °C sans trouble neurologique. [[10]]",
            "La forme sévère se décrit au-dessus de 40,0 °C avec trouble neurologique. [[10]]",
            "Les antipyrétiques ne sont pas recommandés dans ce consensus. [[10]]",
            "Les solutés froids ne sont pas le premier refroidissement. [[10]]",
        ],
        9: [
            "La température rectale confirme et guide l'arrêt du bain. [[9]]",
            "Un prélèvement de sodium ou de glucose n'interrompt pas un bain encore nécessaire. [[9]]",
            "On continue de surveiller après la sortie du bain, au moins le temps lu de 30 minutes. [[10]]",
            "Si la température remonte, on reprend le refroidissement. [[10]]",
        ],
        10: [
            "Porte du danger : trouble neurologique, température haute, arrêt circulatoire.",
            "Porte du bain : immersion jusqu'au cou, ou ombre et ventilation si elle est impossible. [[10]]",
            "Porte de l'action : refroidir d'abord, transporter ensuite, surveiller. [[9]]",
        ],
        11: [
            "Aucun comprimé ne remplace le bain. [[10]]",
            "On déshabille, on retire l'équipement, et on immerge jusqu'au cou si c'est possible. [[9]]",
            "Selon les Jeux, on sort du bain sous 39,0 °C et on surveille. [[9]]",
            "Selon le consensus de 2024, on arrête entre 38,5 et 39,0 °C. [[10]]",
            "Si l'immersion est impossible, on met à l'ombre, on découvre, on vaporise et on ventile. [[10]]",
            "On transporte après le refroidissement, pas avant. [[10]]",
            "On ne donne pas un antipyrétique pour faire baisser ce chiffre. [[10]]",
        ],
        12: [
            "Le club prévoit l'eau, l'ombre et un bain froid les jours de chaleur. [[10]]",
            "On reconnaît la confusion comme une urgence, pas comme un manque de volonté. [[9]]",
            "On entraîne les soignants du site à mesurer la température centrale. [[10]]",
            "On arrête l'épreuve si la chaleur et les signes neurologiques commencent.",
        ],
        13: [
            "Trouble neurologique plus température haute : on refroidit tout de suite. [[10]]",
            "Le transport vient après le bain, pas avant. [[9]]",
            "Cible des Jeux : sous 39,0 °C. [[9]]",
            "Cible de 2024 : arrêt entre 38,5 et 39,0 °C. [[10]]",
            "Pas d'antipyrétique à la place de l'eau froide. [[10]]",
        ],
        14: [
            "Cas. Un coureur de 31 ans devient confus à l'arrivée, et la température rectale est à 40,8 °C.",
            "Erreur. L'asseoir dans l'ambulance et partir avant le bain.",
            "Correction. On immerge sur place, on suit la cible de la source utilisée, puis on transporte. [[9]]",
        ],
    },
    [
        ("alerte", "Reconnaître", "Confusion, crise ou chute en chaleur : on mesure et on refroidit. [[10]]"),
        ("bilan", "Choisir la cible", "Sous 39,0 °C pour les Jeux. Entre 38,5 et 39,0 °C pour arrêter selon 2024. [[9]]"),
        ("age", "Transporter après", "Le bain d'abord. L'ambulance ensuite. Pas d'antipyrétique à la place. [[10]]"),
    ],
    [
        NV("corps", "Corps", [
            ("Tête", 500, 180, 50, 40, "Le trouble neurologique se voit ici."),
            ("Tronc", 500, 360, 90, 80, "La chaleur vient surtout du muscle."),
            ("Peau", 680, 340, 40, 60, "Voie d'évacuation, souvent dépassée."),
            ("Rectum", 500, 520, 30, 24, "Siège de la mesure pratique."),
        ]),
        NV("bain", "Bain", [
            ("Cuve", 480, 420, 140, 70, "Immersion jusqu'au cou si possible."),
            ("Cou", 480, 300, 70, 24, "Limite haute de l'immersion lue."),
            ("Sonde", 650, 460, 30, 20, "Surveillance continue de la température."),
            ("Ombre", 250, 240, 50, 30, "Si le bain est impossible : ombre, découverte, vaporisation, ventilation."),
        ]),
        NV("cible", "Cible", [
            ("Jeux", 300, 360, 80, 40, "On descend sous 39,0 degrés."),
            ("Consensus", 620, 360, 90, 40, "On arrête entre 38,5 et 39,0 degrés."),
            ("Sévère", 460, 500, 80, 30, "Souvent au-dessus de 40,0 degrés avec trouble neurologique."),
            ("Transport", 460, 600, 90, 24, "Après le refroidissement, pas avant."),
        ]),
    ],
    "Quel plan ouvre un coureur confus en chaleur ?",
    [
        "On ouvre le corps pour le trouble neurologique.",
        "On ouvre le bain pour le geste immédiat.",
        "On ouvre la cible pour ne pas mélanger les deux textes.",
    ],
    M([
        "on traite la confusion en chaleur comme une urgence de refroidissement.",
        "on mesure la température centrale plutôt que le front.",
        "on ne retarde pas le bain pour un prélèvement.",
        "on immerge jusqu'au cou quand c'est possible.",
        "on cite la cible des Jeux et celle de 2024 sans les fusionner.",
        "on surveille encore après la sortie de l'eau.",
        "on met à l'ombre si aucune cuve n'est là.",
        "on ne donne pas un antipyrétique à la place de l'eau.",
        "on transporte une fois la température redescendue.",
        "on prévoit la cuve avant le jour de chaleur.",
    ]),
    teaser11="Le bain précède l'ambulance. Pas de dose à la place.",
)


