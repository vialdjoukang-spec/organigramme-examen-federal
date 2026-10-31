#!/usr/bin/env python3
"""DX.1 approfondi : œdème veineux chronique. Sources lues le 31.10.2026."""
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import profond_lib as L

NOM = "Œdème veineux chronique des membres inférieurs"
FICHIER = "LOT_134_Phase_B_V0_DX.1.html"

STADES = [
    ("C0", "9,6 %", "13,6 %", "6,4 %", "l'absence de signe veineux visible"),
    ("C1", "59,1 %", "58,4 %", "59,5 %", "des télangiectasies ou des veines réticulaires seules"),
    ("C2", "14,3 %", "12,4 %", "15,8 %", "des varices sans œdème et sans atteinte de la peau"),
    ("C3", "13,4 %", "11,6 %", "14,9 %", "un godet des membres inférieurs au moment de l'examen"),
    ("C4", "2,9 %", "3,1 %", "2,7 %", "une atteinte de peau, eczéma, pigmentation ou lipodermatosclérose"),
    ("C5", "0,6 %", "la part globale lue", "la même revue", "un ulcère veineux cicatrisé"),
    ("C6", "0,1 %", "la part globale lue", "la même revue", "un ulcère veineux ouvert"),
]


def fen_stade(code, tot, hom, fem, sens):
    ph = [
        f"Le stade {code} correspond à {sens}.",
        f"Dans l'échantillon de Bonn, la part retenue pour {code} est {tot}.",
        f"La lecture par sexe, pour {code}, donne {hom} chez les hommes quand la revue le sépare.",
        f"La lecture par sexe, pour {code}, donne {fem} chez les femmes quand la revue le sépare.",
        f"Le dénominateur de {code} est 3072 adultes de 18 à 79 ans, tirés au sort, pas une file d'urgences.",
        f"On ne convertit pas la part {code} en risque de mourir dans l'année : la revue ne donne pas ce risque.",
        f"On ne convertit pas la part {code} en probabilité que le patient du jour ait une thrombose.",
        f"Le stade inscrit est le plus sévère vu chez la personne, donc {code} suppose qu'un stade au-dessus n'a pas été retenu.",
        f"La page ne fixe pas, pour {code}, une pression de bas en millimètres de mercure.",
        f"La page ne nomme pas, pour {code}, un diurétique comme le geste le plus fréquent.",
        f"Un godet d'un seul côté apparu en quelques heures ne se range pas d'emblée en {code} chronique.",
        f"La comparaison avec l'autre jambe reste obligatoire avant d'écrire {code} dans le dossier.",
        f"Le duplex faisait partie de l'enquête de Bonn, mais un délai suisse d'échodoppler pour {code} n'a pas été lu.",
        f"Les décimales anglaises de {code} sont citées dans les preuves, à côté de la forme française.",
    ]
    return L.W(f"w-dx1-{code.lower()}", f"Stade {code}", ph)


def fenetres_enseignement():
    w = []
    for row in STADES:
        w.append(fen_stade(*row))
    w.append(L.W("w-dx1-methode", "Comment Bonn a compté", [
        "L'enquête a couru du 13 novembre 2000 au 15 mars 2002.",
        "Elle a été menée à Bonn et dans deux communes rurales, avec le ministère de la santé.",
        "Les personnes venaient d'un tirage au sort sur les registres de population.",
        "L'effectif lu est 3072, dont 1722 femmes et 1350 hommes.",
        "L'âge va de 18 à 79 ans.",
        "Chaque personne a répondu à un questionnaire et a été examinée.",
        "Le duplex veineux faisait partie de l'examen, pas seulement le regard.",
        "Le stade clinique retenu est le plus sévère, selon la classification complète.",
        "La revue dit que la façon de vérifier le godet n'est détaillée que dans cette enquête.",
        "C'est pour cela que comparer 13,4 % à 1,1 % sans parler de méthode est une faute d'examen.",
        "Le chiffre suisse équivalent, sur un tirage national, n'est pas dans cette page.",
        "Cette leçon ne crée pas un dépistage de population pour la Suisse.",
    ]))
    w.append(L.W("w-dx1-plaintes", "Plaintes et godet", [
        "Avoir une plainte de jambe n'est pas avoir un godet.",
        "Dans les quatre semaines précédentes, 49,1 % des hommes et 62,1 % des femmes signalaient des plaintes veineuses.",
        "Un gonflement de jambe sur cette période concernait 14,8 % de l'échantillon.",
        "Ce gonflement anamnestique touchait 7,9 % des hommes et 20,2 % des femmes.",
        "Le godet C3, lui, est constaté le jour de l'examen, pas seulement raconté.",
        "On peut donc se plaindre d'une lourdeur sans être au stade C3.",
        "On peut avoir un godet sans que la plainte des quatre semaines ait été le motif de consultation.",
        "À l'examen fédéral, la question qui sépare les deux est : le signe est-il vu, ou seulement dit ?",
        "La revue ne donne pas la sensibilité du seul interrogatoire pour prédire le stade C3.",
        "Inventer cette sensibilité serait une faute.",
        "Le questionnaire incluait une qualité de vie en 36 items, sans seuil décisionnel recopié ici.",
        "Les symptômes augmentaient avec l'âge, dit la revue, sans que je recalcule une pente.",
    ]))
    w.append(L.W("w-dx1-france", "Pourquoi 13,4 % et 1,1 %", [
        "L'étude française citée par la même revue trouve un stade C3 chez 1,1 % des hommes.",
        "Elle le trouve chez 2,2 % des femmes.",
        "Cette étude porte sur 409 personnes, 277 hommes et 132 femmes.",
        "Les auteurs de Bonn écrivent que le stade C3 varie de 1,1 % à 14,9 % selon la méthode.",
        "Le 14,9 % de cette fourchette est aussi la part féminine de Bonn, pas un troisième pays.",
        "La Pologne, toujours selon cette revue, trouve un C3 à 4,5 % sur 40 095 adultes vus en soins.",
        "Ce n'est pas un tirage au sort sur registres, donc le dénominateur n'est pas celui de Bonn.",
        "Édimbourg, selon la même revue, a examiné 1566 adultes de 18 à 64 ans.",
        "On n'aligne pas Édimbourg sur Bonn sans dire que l'âge s'arrête à 64 ans.",
        "Framingham, cité dans la revue, donne une incidence de varices de 2,6 % par an chez les femmes et 1,9 % chez les hommes.",
        "Une incidence annuelle n'est pas la prévalence d'un godet un jour donné.",
        "Le piège d'examen est de réciter un seul pourcentage sans le pays, l'âge et le geste qui l'a produit.",
    ]))
    w.append(L.W("w-dx1-peau", "Peau et ulcère", [
        "Le stade C4 de Bonn regroupe eczéma, pigmentation et lipodermatosclérose, à 2,9 %.",
        "Les hommes y sont à 3,1 % et les femmes à 2,7 %.",
        "L'ulcère cicatrisé, stade C5, est à 0,6 %.",
        "L'ulcère ouvert, stade C6, est à 0,1 %.",
        "La revue dit que les formes sévères de C4 à C6 représentaient 3,6 % à Bonn.",
        "Elle compare ce poids à des enquêtes plus anciennes, où la part grave était plus haute.",
        "Elle avance que le recours plus fréquent au diagnostic et au traitement a pu faire baisser ces formes.",
        "Cette phrase est une hypothèse d'auteurs, pas un essai qui prouve la cause.",
        "La part d'ulcères cicatrisés et ouverts est donnée à 0,7 % pour Bonn dans le résumé comparatif.",
        "On ne soigne pas un C6 avec le seul conseil donné pour un C1.",
        "La page ne détaille pas un pansement, ni une greffe, ni une dose.",
        "Le geste suisse devant un ulcère ouvert se lit dans un protocole local : À vérifier.",
    ]))
    w.append(L.W("w-dx1-soin", "Ce qui a été fait aux veines", [
        "22,9 % de l'échantillon avait déjà eu un geste thérapeutique veineux.",
        "C'était 12,7 % des hommes et 31,0 % des femmes.",
        "Le traitement le plus fréquent était les bas de contention.",
        "Venait ensuite la chirurgie veineuse, puis le médicament.",
        "L'ordre est une fréquence observée, pas une ligne de recommandation graduée.",
        "Aucun nom commercial suisse n'est écrit dans cette revue.",
        "Aucun milligramme n'est écrit dans cette revue.",
        "Un diurétique donné à la place du bas n'est pas le traitement le plus fréquent de cette page.",
        "Une interdiction formelle suisse du diurétique dans l'œdème veineux n'a pas été lue.",
        "Si un médicament est choisi, sa dose se lit dans l'information professionnelle suisse du produit.",
        "Le paracétamol de la Phase A ne traite pas la maladie veineuse.",
        "La chirurgie veineuse n'est pas décidée sur la seule photo d'un godet.",
    ]))
    w.append(L.W("w-dx1-main", "Ce que la main fait", [
        "On regarde les deux jambes, du pied à l'aine, avant d'appuyer.",
        "On presse devant le tibia et derrière la malléole, puis on compare.",
        "Le godet se juge des deux côtés, pas sur une seule photo.",
        "On note la chaleur, un cordon douloureux et l'état de la peau.",
        "La revue ne donne pas le nombre de secondes d'appui ni la profondeur en millimètres.",
        "Ces deux précisions de geste sont donc À vérifier dans un manuel suisse non ouvert ici.",
        "Un œdème dur qui ne prend pas le godet ne se range pas au stade C3.",
        "La part du lymphœdème parmi ces œdèmes n'est pas chiffrée dans la revue.",
        "Une chaleur vive et un cordon font quitter la voie du simple stade C3.",
        "La température cutanée fait partie des anomalies de palpation du cours, sans seuil en degrés ici.",
        "On écrit le côté, le délai et le stade, avant de nommer une maladie de cœur ou de rein.",
        "La Phase A décrit la palpation abdominale. Cette leçon ne la répète pas.",
    ]))
    w.append(L.W("w-dx1-thrombose", "Une jambe, pas les deux", [
        "Le stade C3 de Bonn est une prévalence de population, souvent un tableau bilatéral chronique.",
        "Une seule jambe, gonflée en quelques heures, n'est pas le tableau que ce pourcentage décrit.",
        "Ce profil fait chercher une thrombose veineuse avant d'accepter le diagnostic chronique.",
        "Le score clinique de cette thrombose n'a pas été relu dans cette session.",
        "Le nom du score, ses items et ses seuils sont donc À vérifier.",
        "On ne remplace pas ce score manquant par le pourcentage de Bonn.",
        "L'échodoppler veineux tranche si le doute clinique reste.",
        "Le délai suisse pour obtenir cet échodoppler n'a pas été lu.",
        "En attendant, on ne rassure pas avec la phrase « c'est veineux chronique ».",
        "La contention peut être le traitement d'un stade chronique, pas le premier mot d'une jambe aiguë.",
        "Une douleur thoracique ou un essoufflement brutal sortent du cadre de cette leçon et relèvent d'une filière d'urgence.",
        "Aucun chiffre de cette revue ne quantifie ce risque thoracique.",
    ]))
    w.append(L.W("w-dx1-autres", "Ce que Bonn ne classe pas", [
        "Un œdème des chevilles peut aussi mener à chercher une ascite, dit la Revue Médicale Suisse dans un autre chapitre.",
        "La prévalence de 5 % lue dans cet article est celle de l'ascite en premier recours, pas celle du stade C3.",
        "Mélanger 5 % et 13,4 % est un piège, parce que les dénominateurs ne sont pas les mêmes.",
        "L'insuffisance cardiaque, le syndrome néphrotique et le médicament ne sont pas des stades de la classification veineuse.",
        "La revue de Bonn ne donne pas leur part parmi les godets.",
        "Les marquer À vérifier n'est pas les déclarer rares.",
        "L'examen cherche alors une dyspnée, une prise de poids rapide, une oligurie et une liste de médicaments.",
        "Aucun de ces signes n'a de sensibilité chiffrée dans les pages veineuses lues.",
        "On n'invente pas un rapport de vraisemblance pour combler le trou.",
        "Si le foie est dur ou la rate palpable, on quitte cette leçon vers le diagnostic du foie.",
        "Si la peau crépite ou la douleur dépasse la rougeur, on quitte cette leçon vers l'infection nécrosante.",
        "Le rang d'exclusion E10 signifie : ce diagnostic se pose après les urgences, pas avant.",
    ]))
    w.append(L.W("w-dx1-suisse", "Suisse, sans dose inventée", [
        "Aucune spécialité veineuse n'a été ouverte dans l'information professionnelle suisse pour cette leçon.",
        "Il n'y a donc aucun milligramme, aucun schéma et aucune contre-indication recopiée.",
        "Le seul antalgique dont la dose est écrite dans le lot est le paracétamol de la Phase A.",
        "Cette dose ne devient pas le traitement de l'œdème.",
        "Les bas restent, dans la revue allemande, le geste le plus fréquent.",
        "La classe de compression, la durée quotidienne et le remboursement suisse sont À vérifier.",
        "La marche est cohérente avec une maladie de station debout, sans protocole chiffré lu.",
        "On ne promet pas la disparition du godet après une semaine.",
        "On revoit le patient si la peau change, si la douleur devient unilatérale, ou si le godet s'aggrave.",
        "Le délai de cette revue n'est pas écrit.",
        "Un geste chirurgical se discute avec le spécialiste, pas sur le seul stade C3.",
        "Le dossier garde le stade, le côté et la date, pour que le prochain examen ait une comparaison.",
    ]))
    return "\n".join(w)


PIEGES = [
    ("Un godet d'hier, sur une seule jambe, est-il un stade C3 ?",
     "Non comme premier nom. Ce profil fait chercher une thrombose. Le score de cette thrombose est À vérifier."),
    ("13,4 % est-il le risque du patient assis en face ?",
     "Non. C'est la part de godet chez 3072 adultes de 18 à 79 ans examinés à Bonn."),
    ("1,1 % contredit-il 13,4 % ?",
     "Non. L'étude française n'a pas la même méthode. La revue dit que le stade C3 varie de 1,1 % à 14,9 %."),
    ("Le diurétique est-il le traitement le plus fréquent de la revue ?",
     "Non. Les bas de contention venaient en tête, puis la chirurgie, puis le médicament."),
    ("Une plainte de lourdeur suffit-elle au stade C3 ?",
     "Non. Le godet doit être constaté. Les plaintes des quatre semaines étaient plus fréquentes que le godet du jour."),
    ("C1 est-il un ulcère ?",
     "Non. C1 est la télangiectasie ou la veine réticulaire. L'ulcère ouvert est C6, à 0,1 % dans l'échantillon."),
    ("C6 se soigne-t-il comme C3 ?",
     "La page ne le dit pas. Elle sépare les stades. Le pansement suisse de l'ulcère ouvert est À vérifier."),
    ("Le duplex était-il facultatif à Bonn ?",
     "Non. L'examen clinique et le duplex faisaient partie de l'enquête."),
    ("22,9 % est-il la part de personnes sous diurétique ?",
     "Non. C'est la part qui avait déjà eu un geste veineux, 12,7 % des hommes et 31,0 % des femmes."),
    ("Le chiffre polonais de 4,5 % a-t-il le même dénominateur ?",
     "Non. La revue parle de 40 095 adultes vus en soins, pas d'un tirage sur registres."),
    ("Framingham mesure-t-il le godet ?",
     "La revue y cite une incidence de varices, 2,6 % par an chez les femmes et 1,9 % chez les hommes, pas le stade C3."),
    ("Peut-on écrire une dose de médicament veineux de mémoire ?",
     "Non. Aucun milligramme n'a été lu. La dose se prend dans l'information professionnelle suisse du produit choisi."),
    ("E10 veut-il dire que l'œdème est une urgence maximale ?",
     "Non. E10 est le rang d'exclusion le plus tardif de ce lot. Les urgences passent avant."),
    ("La Phase A doit-elle être recopiée ici ?",
     "Non. La palpation générale est dans le cours. Ici, on ne reprend que ce qui change le godet."),
]


def construire():
    c = L.Corpus()
    bonn = Path("/tmp/bonn_texte.txt").read_text(encoding="utf-8").split("REFERENCES")[0]
    c.texts["BONN"] = bonn
    extraits = L.choisir(bonn, None, 80)
    # Phrase courte des bas, souvent sous le seuil ou collée à un tableau.
    courte = "The most frequent therapy was compression stockings followed by venous surgery and drug treatment."
    if courte not in extraits and courte in " ".join(bonn.split()):
        extraits.append(courte)
    preuves = L.preuves(c, "BONN", "w-dx1b", "la revue de Bonn", "la revue de Bonn", extraits)
    index_ph = ["Les boutons ouvrent les phrases de la revue, sans ajouter un chiffre."]
    for i in range(1, len(extraits) + 1):
        index_ph.append(f"Phrase citée numéro {i}. " + L.B(f"w-dx1b-q{i}", f"citation {i}"))
    index = L.W("w-dx1-index", "Citations de la revue de Bonn", index_ph)
    enseignement = fenetres_enseignement()
    pieges = L.quiz("w-dx1-pieges", PIEGES)
    # Répartition des fenêtres sur les 14 points. Le texte de fiche reste court.
    wins = [""] * 14
    wins[0] = fen_stade(*STADES[3])  # C3 aussi au point définition? déjà dans enseignement. éviter id double
    # fen_stade C3 id w-dx1-c3 est déjà dans enseignement. Ne pas le dupliquer.
    wins[0] = L.W("w-dx1-def", "Ce que le godet veut dire", [
        "Prendre le godet veut dire que le liquide sous-cutané se déplace encore sous le doigt.",
        "Le stade C3 de la revue est ce godet, constaté à l'examen.",
        "Un ulcère n'est pas exigé pour écrire C3.",
        "Une définition de société suisse distincte n'a pas été ouverte.",
        "Les caractères de la palpation du cours, chaleur et limites, complètent le godet sans devenir un stade.",
        "On décrit avant de nommer une insuffisance cardiaque.",
    ])
    wins[1] = "\n".join(fen_stade(*row) for row in STADES) + "\n" + index + "\n" + preuves
    wins[2] = L.W("w-dx1-physio", "Pression et godet", [
        "La revue ne décrit pas la cascade moléculaire de la paroi veineuse.",
        "Elle constate un liquide qui prend le godet, donc encore mobile.",
        "Un œdème fixé, qui ne prend plus le godet, n'est pas le signe qu'elle a compté comme C3.",
        "Le détail biochimique est À vérifier dans un traité non lu ici.",
        "On n'invente pas un chiffre de pression veineuse en millimètres de mercure.",
        "Le duplex de l'enquête voyait le reflux, sans seuil de seconde recopié dans le résumé lu.",
    ])
    wins[3] = L.W("w-dx1-demarche", "Fréquence et gravité", [
        "Ce diagnostic est DX.1 parce que le godet est le signe de population le plus répandu des dix.",
        "Son rang d'exclusion est E10, donc il ne se pose pas avant les urgences du lot.",
        "La prévalence ne dit pas l'ordre de gravité.",
        "Une jambe aiguë quitte cette voie même si le stade C3 est fréquent dans la population.",
        "Le tableau des dix est dans la Phase A.",
        "Ici, on ne refait pas l'algorithme entier.",
    ])
    wins[4] = "\n".join([
        L.W("w-dx1-thrombose2", "Drapeaux", [
            "On date le début en heures ou en mois.",
            "On demande le côté, la station debout, la chaleur et l'essoufflement.",
            "Quelques heures et un seul côté orientent vers une thrombose.",
            "Des mois et les deux côtés rapprochent du tableau chronique de la revue.",
            "Une dyspnée nouvelle n'est pas un symptôme de stade C3.",
            "Le score de thrombose reste À vérifier, items compris.",
        ]),
    ])
    wins[5] = L.W("w-dx1-examen2", "Examen des deux jambes", [
        "L'inspection précède la pression.",
        "On cherche une télangiectasie, une varice, une tache, un ulcère, puis le godet.",
        "On compare le côté opposé avant de conclure.",
        "La chaleur et un cordon se notent en toutes lettres.",
        "Le nombre de secondes d'appui n'est pas dans la revue.",
        "L'examen de Bonn ajoutait un duplex, pas seulement le doigt.",
    ])
    wins[6] = L.W("w-dx1-synd", "Syndrome des parties molles", [
        "Le syndrome est celui des parties molles, pas une masse abdominale.",
        "Ce n'est pas une défense, ni une détente.",
        "Un lymphœdème dur ne donne pas le même godet.",
        "Sa part n'est pas chiffrée ici.",
        "Une crépitation ou une douleur hors de proportion font sortir de ce syndrome.",
        "Ces signes appartiennent à l'infection nécrosante du lot, pas au stade C3.",
    ])
    wins[7] = L.W("w-dx1-positif", "Diagnostic positif", [
        "Le diagnostic positif est un godet bilatéral et chronique, une fois la thrombose écartée.",
        "Il ne se pose pas sur un seul mollet.",
        "Il ne se pose pas sur une photo sans examen.",
        "Le stade le plus sévère est celui qu'on écrit.",
        "Un C4 ou un C6, s'il est présent, passe devant le simple godet.",
        "L'échodoppler reste indiqué si le clinique ne tranche pas.",
    ])
    wins[8] = L.W("w-dx1-bilan", "Bilan", [
        "Il n'y a pas de prise de sang unique pour affirmer le stade C3.",
        "L'échodoppler se discute si l'œdème est unilatéral, aigu, ou si la contention ne suffit pas.",
        "Le délai suisse de cet examen n'a pas été lu.",
        "Une albuminémie se discute si l'on cherche une autre cause, sans seuil veineux dans cette revue.",
        "On ne demande pas un angioscanner pour un godet bilatéral chronique isolé.",
        "L'imagerie d'une jambe aiguë suit la suspicion de thrombose, score À vérifier.",
    ])
    wins[9] = L.W("w-dx1-arbre", "Arbre court", [
        "D'abord le côté et le délai.",
        "Unilatéral et aigu : thrombose jusqu'à preuve du contraire.",
        "Bilatéral, chronique, avec godet : stade veineux, puis contention, puis nouvelle évaluation.",
        "Peau ulcérée : ne pas s'arrêter au mot œdème.",
        "Essoufflement ou douleur thoracique : filière d'urgence, hors pourcentage de Bonn.",
        "Le détail des urgences E1 à E4 est dans la Phase A.",
    ])
    wins[10] = L.W("w-dx1-pec", "Prise en charge", [
        "Aucune dose en milligrammes n'est écrite pour cet œdème.",
        "À Bonn, la contention était le traitement le plus fréquent.",
        "La chirurgie venait ensuite, puis le médicament.",
        "Un diurétique de remplacement n'est pas décrit.",
        "L'interdiction formelle suisse de ce diurétique est À vérifier.",
        "Le produit choisi, s'il y en a un, se lit dans son information professionnelle.",
    ])
    wins[11] = L.W("w-dx1-prev", "Prévention", [
        "La revue ne décrit pas un programme national suisse.",
        "Elle observe que les formes graves de peau ont diminué sur vingt ans, comme une hypothèse.",
        "La marche et la contention concernent une personne déjà classée, pas un dépistage.",
        "Aucun âge de dépistage n'est fixé ici.",
        "On ne palpe pas les jambes d'une population saine sur la foi du seul 13,4 %.",
        "La prévention de la thrombose aiguë est un autre chapitre, non chiffré ici.",
    ])
    wins[12] = L.W("w-dx1-cles", "À retenir", [
        "Godet bilatéral et chronique : penser contention, après avoir écarté l'urgence.",
        "Un seul côté, en heures : penser thrombose.",
        "13,4 % et 1,1 % ne se contredisent pas : la méthode change.",
        "La plainte n'est pas le godet.",
        "Pas de milligramme dans cette leçon.",
        "E10 n'est pas le rang de la plus grande urgence.",
    ])
    wins[13] = pieges
    # Fenêtres longues restantes (méthode, plaintes, france, peau, soin, main, autres, suisse)
    wins[1] += "\n" + enseignement
    points = []
    paras = [
        "Le godet bilatéral chronique est le stade C3 de la classification clinique, étiologique, anatomique et physiopathologique. "
        + L.B("w-dx1-def", "godet") + " Une définition suisse séparée n'a pas été lue. Une seule jambe, en quelques heures, quitte ce nom.",
        "À Bonn, 3072 adultes de 18 à 79 ans ont été examinés, et 13,4 % avaient un godet. "
        + L.B("w-dx1-c3", "stades") + " L'étude française citée est beaucoup plus basse. La méthode fait partie du résultat.",
        "Le liquide qui prend le godet est encore mobile sous le doigt. " + L.B("w-dx1-physio", "mécanisme")
        + " La revue ne donne pas la cascade moléculaire. On n'invente pas une pression chiffrée.",
        "DX.1 est le signe de population le plus fréquent des dix, et E10 est son rang d'exclusion. "
        + L.B("w-dx1-demarche", "ordre") + " La fréquence ne passe pas devant une jambe aiguë. Le cours général reste dans la Phase A.",
        "On date le début, le côté, la station debout et l'essoufflement. " + L.B("w-dx1-thrombose2", "drapeaux")
        + " Une seule jambe, aiguë, oriente vers une thrombose. Les items du score ne sont pas dans cette leçon.",
        "On presse le tibia et la malléole, puis on compare les deux jambes. " + L.B("w-dx1-examen2", "geste")
        + " On note la chaleur, un cordon et la peau. Le temps d'appui en secondes n'est pas dans la revue.",
        "Le syndrome est celui des parties molles. " + L.B("w-dx1-synd", "syndrome")
        + " Ce n'est ni une masse ni une défense. Une crépitation fait sortir de cette leçon.",
        "Le diagnostic positif est un godet bilatéral et chronique, thrombose écartée. " + L.B("w-dx1-positif", "positif")
        + " Un stade de peau plus sévère passe devant. La photo seule ne suffit pas.",
        "Il n'y a pas de prise de sang qui affirme le stade C3. " + L.B("w-dx1-bilan", "bilan")
        + " L'échodoppler se discute si le tableau est unilatéral ou aigu. Son délai suisse est À vérifier.",
        "Le côté et le délai décident. " + L.B("w-dx1-arbre", "arbre")
        + " Aigu et unilatéral : thrombose d'abord. Chronique et bilatéral : contention, puis contrôle.",
        "Aucune dose en milligrammes n'est écrite ici. " + L.B("w-dx1-pec", "soins")
        + " À Bonn, la contention venait en tête. Un diurétique de remplacement n'est pas décrit.",
        "La revue ne fixe pas un dépistage suisse. " + L.B("w-dx1-prev", "prévention")
        + " La baisse des formes graves est une hypothèse d'auteurs. On ne palpe pas une population entière sur un seul pourcentage.",
        "Décrire le godet, le côté et le délai avant de nommer la maladie. " + L.B("w-dx1-cles", "clés")
        + " Ne pas transporter 13,4 % sans son dénominateur. Ne pas inventer un milligramme.",
        "Quatorze questions ferment la leçon. " + L.B("w-dx1-pieges", "pièges")
        + " Répondez avant d'ouvrir. Les preuves anglaises sont à part, dans les citations.",
    ]
    if len(paras) != 14 or len(wins) != 14:
        raise SystemExit("compte points")
    # Éviter un double id : fen_stade C3 est dans wins[1] via enseignement ET via la boucle STADES.
    # enseignement inclut déjà tous les stades. La boucle dans wins[1] les répète. Retirer le doublon.
    wins[1] = index + "\n" + preuves + "\n" + enseignement
    sources = L.sources_section([
        "<sup class=\"s\">2</sup> Piqueres S, Staeger P, Pasche O. Revue Médicale Suisse 2016;537, 2 novembre 2016.",
        "<sup class=\"s\">3</sup> Rabe E, Pannier F. What have we learned from the Bonn Vein Study? Phlebolymphology. Texte complet lu le 31.10.2026. Enquête du 13 novembre 2000 au 15 mars 2002.",
        "<sup class=\"s\">4</sup> Wanhainen A et al. Société européenne de chirurgie vasculaire, anévrismes aorto-iliaques, 2024.",
        "<sup class=\"s\">5</sup> Björck M et al. Maladies des artères et veines mésentériques. Publié le 29.3.2017.",
        "<sup class=\"s\">6</sup> Sartelli M et al. Consensus du 14 décembre 2018 sur les infections de la peau et des parties molles.",
        "<sup class=\"s\">7</sup> Couderc M, Bart G, Coiffier G et al. Recommandations françaises, arthrite septique native de l'adulte, 3 août 2020.",
        "<sup class=\"s\">8</sup> Swissmedic, Dafalgan comprimés, numéro 69266. Texte hors ligne lu le 31.10.2026.",
    ], "La Phase A porte la ligne du catalogue et les adresses complètes. Ce diagnostic ne les recopie pas.")
    html = L.assembler(
        f"DX.1 — {NOM}", NOM,
        "DX.1 du cours F1.5. Le rang d'exclusion n'est pas le numéro DX. Texte du 31.10.2026.",
        f"<h2>DX.1 — {NOM}</h2>",
        "L'œdème veineux chronique est un godet des jambes, souvent bilatéral, dans une maladie veineuse. Un début aigu sur une seule jambe fait chercher une thrombose avant d'accepter ce diagnostic. À Bonn, le traitement le plus fréquent était la contention.",
        list(zip(paras, wins)),
        sources,
        "FIN_FICHIER LOT_134_Phase_B_DX.1",
        FICHIER,
        40000,
    )
    # ids dupliqués ? fen_stade est appelé dans fenetres_enseignement seulement.
    L.ecrire(FICHIER, html)
    c.ecrire_preuves()
    return extraits


if __name__ == "__main__":
    construire()
