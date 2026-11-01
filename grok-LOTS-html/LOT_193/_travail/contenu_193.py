# -*- coding: utf-8 -*-
"""Noyaux cliniques LOT_193. Chaque phrase reste sous 32 mots. Les doses sont celles des extraits AIPS."""
from __future__ import annotations

import re

RX = re.compile(r"[\wÀ-ÿŒœ]+(?:['’\-][\wÀ-ÿŒœ]+)*")


def s(texte: str, src: int) -> tuple[str, int]:
    return (texte, src)


EXAMEN = [
    s("Le tonus de repos, le tonus passif et le tonus actif se jugent séparément.", 1),
    s("Le ballant teste la résistance à la mobilisation passive.", 1),
    s("Le tiré-assis, la suspension sous les aisselles et la suspension ventrale testent le tonus actif.", 1),
    s("La posture en jambe de grenouille montre des hanches en extension sur le plan du lit.", 1),
    s("L'hyperréflexie oriente vers le central, l'hypo ou l'aréflexie vers le neuromusculaire, sans être absolue.", 1),
    s("Des contractures chez un nouveau-né parlent pour une baisse des mouvements fœtaux.", 1),
    s("La faiblesse se voit par la baisse des mouvements contre gravité.", 1),
]
DIFF = [
    s("Au central, l'hypotonie axiale dépasse souvent celle des membres, et la force est préservée.", 1),
    s("Au périphérique, l'hypotonie est axiale et appendiculaire, avec faiblesse ou fatigabilité.", 1),
    s("Les réflexes centraux sont augmentés ou normaux. Les réflexes périphériques sont diminués ou normaux.", 1),
    s("Un trouble du périmètre crânien, des yeux, une épilepsie ou un retard global orientent vers le central.", 1),
    s("Des troubles alimentaires ou respiratoires néonataux, avec une cognition souvent normale, orientent vers le périphérique.", 1),
    s("Certaines leucodystrophies mêlent les deux étages.", 1),
]
GLU = [
    s("Le seuil lu de glycémie, à la maternité dès 35 semaines, est une valeur inférieure à 2,6 mmol/l.", 4),
    s("Ce seuil ne s'applique pas avant 35 semaines, ni au nouveau-né malade de soins intermédiaires ou intensifs.", 4),
    s("Il ne faut pas adopter un seuil de 2,0 mmol/l.", 4),
    s("Si la valeur est d'au moins 2,6 mmol/l, on la recontrôle avant les repas suivants.", 4),
]
BEIGHTON = [
    s("Après 5 ans, le score de Beighton lu compte cinq items, dont quatre sont bilatéraux.", 13),
    s("Le cinquième doigt est positif si la dorsiflexion passive atteint ou dépasse 90 degrés, des deux côtés.", 13),
    s("Le coude et le genou sont positifs si l'hyperextension passive atteint 10 degrés, des deux côtés.", 13),
    s("Le pouce est positif s'il touche toute la face fléchisse de l'avant-bras, des deux côtés.", 13),
    s("Le tronc est positif si les paumes reposent au sol, genoux tendus.", 13),
    s("Dans ce passage, un score total d'au moins 4 indique une laxité chez l'enfant de plus de 5 ans.", 13),
    s("De 12 mois à 4 ans et 11 mois, le dernier item devient la cheville, positive au-delà de 30 degrés.", 13),
    s("Pour cette version révisée, le score est indicatif s'il est supérieur à 4.", 13),
    s("La cohorte de l'article de 2023 n'est pas une norme suisse de cabinet.", 13),
]
SMA_DOSES = [
    s("Le nusinersen, autorisation 66495, est une solution pour injection intrathécale par ponction lombaire.", 6),
    s("Une dose de charge de 50 mg est administrée aux jours 0 et 14.", 6),
    s("La dose d'entretien de 28 mg est ensuite administrée une fois tous les 4 mois.", 6),
    s("Le schéma de 12 mg reste possible, aux jours 0, 14, 28 et 63, puis 12 mg tous les 4 mois.", 6),
    s("Des hydrocéphalies communicantes ont été rapportées chez des patients traités par le schéma de 12 mg.", 6),
    s("Le risdiplam, autorisation 67251, se prend une fois par jour, selon l'âge et le poids.", 7),
    s("Avant 2 mois, la dose lue est de 0,15 mg/kg, sur l'âge corrigé chez le prématuré.", 7),
    s("De 2 mois à moins de 2 ans, la dose lue est de 0,20 mg/kg.", 7),
    s("Dès 2 ans et moins de 20 kg, la dose lue est de 0,25 mg/kg.", 7),
    s("Dès 2 ans et au moins 20 kg, la dose lue est de 5 mg.", 7),
    s("Une dose quotidienne supérieure à 5 mg n'a pas été étudiée.", 7),
    s("Il n'y a pas de donnée clinique avant 16 jours de vie pour le risdiplam.", 7),
    s("L'onasemnogène abéparvovec, autorisation 67529, ne se donne que jusqu'à l'âge de deux ans.", 8),
    s("L'indication lue exige une mutation biallélique du gène de survie du motoneurone 1.", 8),
    s("Elle couvre un type 1 clinique, ou jusqu'à 3 copies du gène de survie du motoneurone 2.", 8),
    s("La prednisolone orale est de 1 mg/kg/jour, commencée 24 heures avant la perfusion.", 8),
    s("Elle est poursuivie 30 jours, jour de la perfusion inclus.", 8),
    s("Si le foie est rassurant, on peut descendre à 0,5 mg/kg/jour pendant 2 semaines.", 8),
    s("La seconde marche lue est de 0,25 mg/kg/jour pendant 2 semaines.", 8),
    s("Une insuffisance hépatique aiguë, parfois fatale, a été rapportée après la perfusion.", 8),
    s("Si 1 mg/kg/jour de prednisolone ne suffit pas, un hépatologue pédiatrique est consulté.", 8),
]
THYRO = [
    s("La lévothyroxine, autorisation 54949, est indiquée dans l'hypothyroïdie congénitale.", 11),
    s("On donne la dose tolérée la plus élevée possible, pour normaliser la thyréostimuline.", 11),
    s("De 0 à 6 mois, la table lit 25 à 75 µg, soit 10 µg/kg.", 11),
    s("De 6 à 12 mois, la table lit 50 à 75 µg, soit 8 µg/kg.", 11),
    s("De 1 à 5 ans, la table lit 75 à 100 µg, soit 5 à 6 µg/kg.", 11),
    s("De 6 à 12 ans, la table lit 100 à 150 µg, soit 4 à 5 µg/kg.", 11),
    s("Avant 12 ans, la dose reste individualisée.", 11),
    s("Aux doses thérapeutiques, l'allaitement reste possible selon le texte lu.", 11),
]
POMPE = [
    s("L'alpha alglucosidase, autorisation 58038, est recommandée à 20 mg/kg toutes les 2 semaines.", 9),
    s("On commence la perfusion à un débit maximal de 1 mg/kg/h.", 9),
    s("On augmente de 2 mg/kg/h toutes les 30 minutes, jusqu'à 7 mg/kg/h, sans réaction.", 9),
    s("La dose de 40 mg/kg a été étudiée sans différence claire de survie.", 9),
    s("La dose recommandée reste donc 20 mg/kg toutes les 2 semaines.", 9),
    s("La forme infantile charge le cœur et le muscle, avec cardiomyopathie et hypotonie.", 9),
    s("Le décès lu survient par arrêt cardiaque ou insuffisance respiratoire dans la première année.", 9),
]
JONCTION = [
    s("En myasthénie néonatale, autorisation 19943, on préfère en général la néostigmine.", 10),
    s("Si la néostigmine ne convient pas, la référence lue est de 5 mg par voie orale toutes les 4 à 6 heures.", 10),
    s("Cette prise est prévue 30 à 60 minutes avant les repas, puis on diminue jusqu'à l'arrêt.", 10),
    s("Le comprimé de 10 mg ne convient pas à la pédiatrie.", 10),
    s("La dragée de 60 mg est une forme adulte. Ce n'est pas la référence néonatale.", 10),
]
BOT = [
    s("Le botulisme n'est pas transmissible de personne à personne.", 5),
    s("La forme infantile vient de la colonisation du tube digestif. Le miel est en cause.", 5),
    s("On ne donne pas de miel avant l'âge d'un an.", 5),
    s("Après un aliment, la paralysie peut commencer par les yeux et la langue en 12 à 72 heures.", 5),
    s("La paralysie respiratoire peut tuer. La place est en soins intensifs.", 5),
    s("L'antitoxine est indiquée au stade précoce. La fiche d'avril 2023 ne donne aucun milligramme.", 5),
    s("En Suisse, l'antitoxine est disponible auprès de la pharmacie de l'armée.", 5),
    s("La mortalité de l'ensemble des cas se situe entre 5 et 10 pour cent.", 5),
    s("Avec un à deux cas par an, le botulisme reste très rare en Suisse.", 5),
    s("Une chaleur d'au moins 85 degrés pendant 15 minutes inactive la toxine.", 5),
    s("Aucun vaccin humain n'est disponible en Suisse.", 5),
]


def defs(quoi: str, src: int) -> list:
    return [
        s("Le tonus est la tension du muscle en dehors de toute contraction volontaire.", 1),
        s("L'hypotonie, la faiblesse et l'hyperlaxité sont trois signes distincts, qui peuvent coexister.", 1),
        s("L'hyperlaxité augmente l'amplitude autour d'une articulation. Elle n'est pas un tonus bas.", 1),
        s(quoi, src),
    ]


def epi_commune() -> list:
    return [
        s("Les causes centrales représentent 66 à 88 pour cent des hypotonies du petit enfant.", 1),
        s("Aucune incidence suisse unique ne classe les dix diagnostics de ce motif.", 1),
        s("L'hyperlaxité est présente chez 4 à 13 pour cent des personnes saines.", 1),
    ]


def demarche() -> list:
    return [
        s("On commence par dire si le nourrisson est malade, avant de classer le tonus.", 1),
        s("On observe le repos, puis le ballant, puis le tiré-assis.", 1),
        s("On ajoute la suspension sous les aisselles et la suspension ventrale.", 1),
        s("On compare la force, les réflexes, la succion, le périmètre crânien et les yeux.", 1),
        s("Une hypotonie légère avec retard moteur isolé peut être revue pendant quelques mois.", 1),
        s("Un avis neuropédiatrique est indiqué si le tableau persiste ou si un autre signe apparaît.", 1),
        s("L'imagerie cérébrale attend une hypothèse. Une cause centrale n'est pas toujours visible.", 1),
        s("Les créatine kinases sont rarement pathologiques chez le nourrisson. Une valeur normale n'exclut pas le muscle.", 1),
        s("Les vitesses de conduction et l'électromyogramme sont rarement déterminants à cet âge.", 1),
    ]


def anamnese() -> list:
    return [
        s("Moins de mouvements fœtaux, un polyhydramnios ou une expulsion prolongée orientent vers le neuromusculaire.", 1),
        s("Une asphyxie peut être mise à tort sur la seule mauvaise adaptation et retarder le diagnostic.", 1),
        s("Un retard cognitif ou une épilepsie orientent vers le central. Un trouble de déglutition oriente vers le périphérique.", 1),
    ]


def prevention() -> list:
    return [
        s("On ne donne pas de miel avant un an.", 5),
        s("Le dépistage néonatal est, pour l'instant, le seul dépistage génétique autorisé en Suisse.", 3),
        s("L'attente de quelques mois ne concerne que l'hypotonie légère à retard moteur isolé.", 1),
        s("L'appellation hypotonie bénigne, venue des années 1950, est contestée.", 1),
    ]


def cles() -> list:
    return [
        s("Force gardée et réflexes vifs parlent pour le central. Faiblesse et aréflexie parlent pour le périphérique.", 1),
        s("Une créatine kinase normale n'exclut pas une maladie du muscle chez le nourrisson.", 1),
        s("Tout nourrisson malade peut être hypotone, quelle que soit la cause.", 1),
    ]


def cas_asphyxie() -> list:
    return [
        s("Cas corrigé. Un nouveau-né hypotone est étiqueté asphyxie, après une expulsion longue.", 1),
        s("Les mouvements fœtaux étaient déjà rares, et il y avait un polyhydramnios.", 1),
        s("La correction est de chercher une atteinte neuromusculaire, sans nier la mauvaise adaptation.", 1),
        s("Piège : appeler bénigne une hypotonie qui n'a pas été examinée ni suivie.", 1),
    ]


def pws() -> list:
    return [
        s("Le syndrome vient de l'absence d'expression des gènes paternels de la région 15q11-q13.", 12),
        s("Environ 70 pour cent des cas sont une délétion, environ 28 pour cent une disomie maternelle.", 12),
        s("Moins de 2 pour cent sont un défaut du centre d'empreinte.", 12),
        s("Sur 90 patients confirmés, 68 avaient une délétion, 21 une disomie, et 1 un défaut d'empreinte.", 12),
        s("L'hypotonie néonatale et le retard global dépassaient 97 pour cent.", 12),
        s("Les troubles alimentaires, la prise de poids après 1 an, l'hypogonadisme et l'hyperphagie atteignaient 93 pour cent ou plus.", 12),
        s("Quinze des 90 patients confirmés ne remplissaient pas les critères cliniques anciens.", 12),
        s("Les critères servent à demander le test. Ils ne remplacent pas le laboratoire.", 12),
        s("Le nourrisson hypotonique qui prend mal du poids n'est souvent pas testé.", 12),
    ]


def sma_epi() -> list:
    return [
        s("L'amyotrophie spinale est au dépistage depuis le 1.3.2024.", 3),
        s("En 2024, 80 509 dépistages ont été faits, et 6 nouveau-nés avec amyotrophie spinale ont été repérés.", 2),
        s("L'incidence lue est de 1 pour 11 500.", 2),
        s("La délétion homozygote a été cherchée chez 68 711 nouveau-nés.", 2),
        s("Un traitement présymptomatique a été donné aux nouveau-nés à haut risque de forme infantile.", 2),
        s("Devant une hypotonie récente, une faiblesse et une aréflexie, Jeannet fait chercher le gène.", 1),
    ]


def thyro_epi() -> list:
    return [
        s("L'incidence lue de l'hypothyroïdie primaire est de 1 pour 3 500.", 2),
        s("Vingt-huit cas ont été repérés en 2024, pour un total historique de 1 125.", 2),
        s("La thyréostimuline est dosée chez les 80 509 nouveau-nés du programme.", 2),
        s("L'hypothyroïdie peut accompagner une hypotonie.", 1),
    ]


def trisomie() -> list:
    return [
        s("Jeannet range les syndromes dysmorphiques parmi les causes centrales d'hypotonie.", 1),
        s("Une série de 124 enfants a mesuré l'adhésion au suivi publié en 2001.", 15),
        s("Le contrôle thyroïdien était suivi dans 61 pour cent des cas.", 15),
        s("Les radiographies du rachis cervical étaient faites dans 94 pour cent des cas, souvent avant une opération.", 15),
        s("Le passage lu ne liste pas les mesures du visage. On ne les recopie pas.", 15),
        s("L'adhésion cardiaque n'est pas un chiffre du passage lu. On garde seulement l'idée d'un suivi.", 15),
    ]


def steinert() -> list:
    return [
        s("La forme congénitale est la forme la plus sévère, présente à la naissance.", 14),
        s("L'atteinte motrice et cognitive peut être profonde.", 14),
        s("Les deux formes lues viennent d'une expansion de répétitions dans le gène de la protéine kinase.", 14),
        s("Un hydramnios, une microrétrognathie et un pied bot peuvent révéler une maladie maternelle non connue.", 14),
        s("Le cas cite une hypotonie légère, une alimentation lente et des scores d'Apgar bas, sans en faire un seuil.", 14),
        s("Ce récit est un cas de 2026, pas une série suisse.", 14),
    ]


def pompe_txt() -> list:
    return [
        s("L'information professionnelle estime une incidence globale de 1 pour 40 000 naissances.", 9),
        s("Le déficit empêche de dégrader le glycogène lysosomal, surtout dans le cœur et le muscle.", 9),
        s("La forme infantile progresse vite, en général dès la première année, avec une vie très courte sans traitement.", 9),
        s("Le développement moteur s'arrête, ou les progrès acquis sont perdus.", 9),
        s("Une forme infantile atypique a une cardiomyopathie moins sévère et une survie plus longue.", 9),
    ]


NOYAUX: dict = {}

NOYAUX["A"] = {
    1: defs("Ce motif rassemble le tonus bas du nourrisson et de l'enfant, du cerveau jusqu'au muscle.", 1),
    2: epi_commune() + sma_epi() + thyro_epi() + [
        s("Le botulisme compte un à deux cas par an en Suisse, toutes formes confondues.", 5),
        s("La mortalité de l'ensemble des cas de botulisme se situe entre 5 et 10 pour cent.", 5),
    ],
    3: [
        s("L'étage central comprend le cerveau, le cervelet ou la moelle.", 1),
        s("L'étage périphérique comprend le motoneurone inférieur, le nerf, la jonction ou le muscle.", 1),
        s("Une affection centrale peut devenir plus tard une infirmité motrice cérébrale spastique, ataxique ou dyskinétique.", 1),
        s("L'amyotrophie spinale détruit le motoneurone de la corne antérieure.", 1),
        s("La maladie de Pompe infantile dépose le glycogène dans le cœur et le muscle.", 9),
        s("Le botulisme bloque la transmission par une neurotoxine.", 5),
    ] + pws()[:3] + steinert()[:3],
    4: demarche() + GLU,
    5: anamnese() + [
        s("On demande le miel, l'alimentation, la succion et la couleur pendant les repas.", 5),
        s("On demande l'hydramnios, la mâchoire et les pieds, et la force de la mère.", 14),
        s("On demande la prise de poids, la faim après un an, et les organes génitaux.", 12),
    ],
    6: EXAMEN + BEIGHTON[:5],
    7: DIFF + [
        s("Les maladies du collagène et l'hypothyroïdie peuvent accompagner une hypotonie.", 1),
        s("L'hyperlaxité et la faiblesse coexistent dans certaines myopathies, dont la maladie d'Ullrich.", 1),
    ],
    8: [
        s("Le diagnostic positif suit l'étage clinique, puis un test ciblé.", 1),
        s("Le laboratoire confirme le syndrome de Prader-Willi. Les critères anciens ne suffisent pas.", 12),
        s("La délétion homozygote du gène de survie du motoneurone est le test du dépistage.", 2),
        s("L'hypotonie bénigne n'est pas un diagnostic de repos.", 1),
    ] + trisomie()[:2],
    9: [
        s("Le prélèvement du dépistage se fait au talon et part vers l'hôpital des enfants de Zurich.", 3),
        s("La liste fédérale du 28 janvier 2025 comprend l'hypothyroïdie et l'amyotrophie spinale.", 3),
    ] + thyro_epi() + sma_epi()[:3],
    10: [
        s("Si le nourrisson est malade, on traite la cause avant de conclure à une maladie du tonus.", 1),
        s("Si la force chute et les réflexes disparaissent, on pense corne, nerf, jonction ou muscle.", 1),
        s("Si la glycémie de maternité est inférieure à 2,6 mmol/l, le passage lu parle d'hypoglycémie, dans ce cadre seul.", 4),
        s("Si les yeux et la langue se paralysent après un aliment, on pense au botulisme et aux soins intensifs.", 5),
    ],
    11: SMA_DOSES + THYRO + POMPE + JONCTION + BOT[:6],
    12: prevention() + [
        s("Une chaleur d'au moins 85 degrés pendant 15 minutes inactive la toxine botulique.", 5),
    ],
    13: cles() + [
        s("Les dix noms du motif restent dans l'ordre de fréquence habituelle, et l'exclusion suit le danger.", 1),
        s("Le score de Beighton lu a deux totaux, au moins 4 et supérieur à 4, selon la version.", 13),
    ],
    14: cas_asphyxie() + [
        s("Piège : appliquer le seuil de 2,6 mmol/l à un nouveau-né de soins intensifs.", 4),
        s("Piège : donner la dragée adulte de 60 mg comme référence du nouveau-né.", 10),
        s("Piège : croire qu'une créatine kinase normale écarte la maladie de Pompe ou une autre myopathie.", 1),
    ],
}

NOYAUX[1] = {
    1: defs("L'hypotonie d'origine centrale part du cerveau, du cervelet ou de la moelle.", 1),
    2: [
        s("Les causes centrales représentent 66 à 88 pour cent des hypotonies du petit enfant.", 1),
        s("Ce chiffre vient d'une revue de 2006, pas d'un registre suisse de l'année en cours.", 1),
    ] + epi_commune()[1:],
    3: [
        s("Le cortex, les noyaux, le cervelet ou la moelle peuvent baisser le tonus.", 1),
        s("La force est souvent gardée, parce que le motoneurone inférieur et le muscle sont intacts.", 1),
        s("Plus tard, le tableau peut devenir spastique, ataxique ou dyskinétique.", 1),
        s("La moelle est rangée par Jeannet parmi les causes centrales au sens large.", 1),
    ],
    4: demarche() + GLU[:2],
    5: anamnese() + [
        s("On cherche un retard des acquisitions, des crises, un périmètre qui s'écarte et une dysmorphie.", 1),
    ],
    6: EXAMEN + [
        s("On regarde les yeux, la succion, la langue et le contact, pas seulement les membres.", 1),
    ],
    7: DIFF + [
        s("La trisomie 21 et d'autres syndromes dysmorphiques entrent dans ce groupe central.", 1),
        s("Une leucodystrophie peut brouiller la frontière avec le périphérique.", 1),
    ],
    8: [
        s("Le diagnostic positif est clinique d'abord : axial, force gardée, réflexes vifs, tête ou crises.", 1),
        s("L'imagerie ne confirme pas toujours. Elle se demande après une hypothèse.", 1),
        s("On n'écrit pas hypotonie bénigne pour fermer le dossier.", 1),
    ],
    9: [
        s("L'imagerie cérébrale vient après l'hypothèse, pas à la place de l'examen.", 1),
        s("Une créatine kinase est utile pour ne pas manquer le muscle, même si elle est souvent normale.", 1),
        s("Le dépistage de l'hypothyroïdie et de l'amyotrophie spinale est déjà fait au talon, ou à rattraper.", 3),
    ],
    10: [
        s("Si les réflexes sont vifs et la force gardée, on reste sur l'étage central.", 1),
        s("Si une faiblesse et une aréflexie apparaissent, on quitte ce diagnostic et on cherche le périphérique.", 1),
        s("Si l'enfant est aigu, on traite comme un nourrisson malade avant l'étiquette centrale.", 1),
    ],
    11: [
        s("Il n'y a pas de milligramme propre à l'hypotonie centrale dans les sources lues.", 1),
        s("On protège la respiration et la succion, et on traite la cause quand elle est connue.", 1),
        s("L'avis neuropédiatrique ne se diffère pas si un signe neurologique s'ajoute.", 1),
    ],
    12: prevention(),
    13: cles() + [
        s("Le central est fréquent, de 66 à 88 pour cent, mais ce n'est pas une raison pour oublier le muscle.", 1),
    ],
    14: cas_asphyxie() + [
        s("Cas corrigé. Une hypotonie axiale avec crises est appelée périphérique à cause du tonus bas.", 1),
        s("La force est gardée et les réflexes sont vifs. La correction est de revenir au central et à l'imagerie raisonnée.", 1),
    ],
}

NOYAUX[2] = {
    1: defs("L'hypotonie du nourrisson malade est celle de tout enfant aigu, avant toute maladie du tonus.", 1),
    2: [
        s("Jeannet écrit que tout nourrisson malade pourra être hypotone, quelle que soit la cause.", 1),
        s("Ce n'est pas une incidence chiffrée. C'est une règle d'examen.", 1),
    ] + epi_commune(),
    3: [
        s("L'infection, le manque d'oxygène, le froid ou une glycémie basse peuvent éteindre le tonus.", 1),
        s("Le cerveau et le muscle ne sont pas malades au départ. Ils manquent d'énergie ou d'apport.", 4),
        s("Le botulisme intestinal est une cause aiguë, par colonisation et toxine.", 5),
    ],
    4: demarche()[:4] + GLU + [
        s("On sécurise l'air et la respiration avant le classement central ou périphérique.", 1),
    ],
    5: anamnese() + [
        s("On demande la fièvre, l'alimentation, le miel, les vomissements et la couleur.", 5),
        s("On demande l'âge gestationnel, pour savoir si le cadre de 35 semaines s'applique.", 4),
    ],
    6: EXAMEN + [
        s("Un enfant gris, chaud, ou en pause respiratoire n'est pas un simple bilan de tonus.", 1),
    ],
    7: DIFF + [
        s("Le sepsis, l'hypoglycémie de maternité et le botulisme se ressemblent au premier regard par le tonus.", 5),
        s("On ne range pas d'emblée cet enfant dans l'hyperlaxité ni dans une trisomie.", 1),
    ],
    8: [
        s("Le diagnostic positif est celui de la maladie aiguë, pas celui d'un syndrome du tonus.", 1),
        s("L'hypoglycémie de la page suisse est une glycémie inférieure à 2,6 mmol/l, dans son cadre seulement.", 4),
        s("Le botulisme se reconnaît au contexte et à la paralysie descendante, puis aux soins intensifs.", 5),
    ],
    9: GLU + [
        s("On ne copie pas ici un volume de gel de glucose. La page lue n'est pas réécrite en millilitres.", 4),
        s("Le dépistage au talon ne remplace pas la glycémie du jour.", 2),
    ],
    10: [
        s("Air, respiration, puis cause aiguë. Le classement du tonus vient après.", 1),
        s("À la maternité, dès 35 semaines, une valeur sous 2,6 mmol/l est le seuil lu.", 4),
        s("En soins intensifs, ce seuil n'est pas la définition à utiliser.", 4),
        s("Paralysie des yeux et de la langue après miel ou aliment : soins intensifs et antitoxine précoce.", 5),
    ],
    11: BOT + [
        s("Aucune dose de glucose en millilitres n'est écrite, faute de l'avoir recopiée comme conduite.", 4),
        s("Aucune dose d'antitoxine en milligrammes n'est écrite, faute de chiffre dans la fiche.", 5),
    ],
    12: prevention() + BOT[-2:],
    13: cles() + [
        s("Le nourrisson malade passe avant les neuf autres noms, dans l'ordre d'exclusion.", 1),
    ],
    14: [
        s("Cas corrigé. Un nouveau-né de 36 semaines, en maternité, a une glycémie à 2,1 mmol/l.", 4),
        s("On avait proposé d'attendre un seuil de 2,0 mmol/l. La page suisse le déconseille.", 4),
        s("La correction est de traiter selon le cadre lu, puis de recontrôler, sans transporter ce chiffre en soins intensifs.", 4),
        s("Piège : oublier le miel chez un nourrisson brusquement faible.", 5),
    ],
}

NOYAUX[3] = {
    1: defs("L'hyperlaxité ligamentaire est une amplitude trop grande. Ce n'est pas, à elle seule, une hypotonie.", 1),
    2: [
        s("Elle est présente chez 4 à 13 pour cent des personnes saines.", 1),
        s("L'article de 2023 sépare l'hypermobilité locale, en général sous cinq sites, et la forme généralisée.", 13),
        s("La forme généralisée touche en général cinq sites ou plus.", 13),
    ] + epi_commune()[:2],
    3: [
        s("Le collagène et les ligaments laissent l'articulation dépasser l'amplitude attendue.", 13),
        s("Le muscle peut être fort. Le tonus de repos peut rester normal.", 1),
        s("Dans la maladie d'Ullrich, l'hyperlaxité coexiste avec une vraie faiblesse.", 1),
        s("Les maladies du collagène peuvent accompagner une hypotonie.", 1),
    ],
    4: demarche()[:6] + BEIGHTON,
    5: anamnese()[:1] + [
        s("On demande les entorses, la douleur, la famille, et si l'enfant se tient contre la gravité.", 13),
        s("Une faiblesse vraie ou une aréflexie font quitter l'hyperlaxité isolée.", 1),
    ],
    6: EXAMEN + BEIGHTON,
    7: DIFF + [
        s("On distingue l'amplitude, le tonus et la force, dans cet ordre, à chaque articulation utile.", 1),
        s("Une trisomie, une myopathie ou un nourrisson malade peuvent montrer une amplitude large sans être ce diagnostic.", 1),
    ],
    8: [
        s("Le diagnostic positif d'une laxité, dans le passage de 2023, repose sur le score lu et l'examen.", 13),
        s("Deux formulations coexistent : au moins 4 après 5 ans, et supérieur à 4 dans la version du jeune enfant.", 13),
        s("On ne transforme pas ces cinq items en un total sur neuf qui n'est pas celui du texte lu.", 13),
    ],
    9: [
        s("Aucun laboratoire n'est exigé par le seul score, si la force et les réflexes sont normaux.", 13),
        s("Une créatine kinase se discute si une faiblesse s'ajoute, parce qu'une valeur normale n'exclut pas le muscle.", 1),
        s("Ce score n'est pas un seuil suisse officiel.", 13),
    ],
    10: [
        s("Si l'amplitude est large et la force normale, on explique, on surveille, on ne médicalise pas à l'excès.", 1),
        s("Si la force baisse, on sort de ce diagnostic et on reprend l'étage périphérique.", 1),
        s("Si l'enfant est aigu, l'hyperlaxité n'explique pas la détresse.", 1),
    ],
    11: [
        s("Aucune dose médicamenteuse n'est liée à l'hyperlaxité dans les sources lues.", 13),
        s("On protège les articulations douloureuses et on adresse si la faiblesse apparaît.", 1),
    ],
    12: prevention() + [
        s("On explique aux parents que 4 à 13 pour cent des personnes saines sont hyperlaxes.", 1),
    ],
    13: cles() + [
        s("Le score révisé remplace le tronc par la cheville, positive si l'angle dépasse 30 degrés.", 13),
    ],
    14: [
        s("Cas corrigé. Un enfant de 6 ans touche le sol avec les paumes et on conclut à une myopathie.", 13),
        s("La force est normale, les réflexes sont présents, le score atteint 4.", 13),
        s("La correction est de parler de laxité, et de ne chercher le muscle que si la force chute.", 1),
        s("Piège : inverser les deux totaux, au moins 4 et supérieur à 4.", 13),
    ],
}

NOYAUX[4] = {
    1: defs("La trisomie 21 est un syndrome dysmorphique que Jeannet range parmi les hypotonies centrales.", 1),
    2: trisomie() + epi_commune()[:1],
    3: [
        s("Le tonus bas est central : la force peut être relativement gardée au début.", 1),
        s("L'hypothyroïdie, plus fréquente dans ce syndrome, peut aggraver le tonus.", 1),
        s("Le passage de suivi ne décrit pas la mécanique du chromosome. On ne l'invente pas.", 15),
    ],
    4: demarche() + [
        s("On vérifie que le dépistage thyroïdien néonatal a été fait, puis le suivi.", 2),
    ],
    5: anamnese() + [
        s("On demande le diagnostic déjà connu, le cœur, la thyroïde, le sommeil et le rachis.", 15),
    ],
    6: EXAMEN + [
        s("On examine le tonus axial, la succion et les réflexes, sans substituer une liste de mesures du visage.", 15),
    ],
    7: DIFF + [
        s("Le syndrome de Prader-Willi et l'hypothyroïdie partagent l'hypotonie et la mauvaise prise de poids.", 12),
        s("L'hyperlaxité peut s'y ajouter sans résumer l'enfant.", 1),
    ],
    8: [
        s("Le diagnostic positif de la trisomie est génétique. L'hypotonie ne le prouve pas à elle seule.", 1),
        s("Le suivi lu comprend la thyroïde et le rachis cervical, avec les taux d'adhésion cités.", 15),
    ] + trisomie()[2:4],
    9: thyro_epi()[:3] + [
        s("Le rachis cervical était radiographié dans 94 pour cent des cas de la série, souvent avant une opération.", 15),
        s("On ne crée pas un pourcentage d'échocardiographie qui n'est pas dans le passage.", 15),
    ],
    10: [
        s("Si le diagnostic est connu, on surveille la thyroïde et le rachis, et on traite une autre cause si le tonus change.", 15),
        s("Si l'enfant devient faible et aréflexique, on ne met pas tout sur la trisomie.", 1),
        s("Si l'enfant est aigu, on le traite comme un nourrisson malade.", 1),
    ],
    11: [
        s("La lévothyroxine de l'hypothyroïdie congénitale, autorisation 54949, n'est pas automatique chez tout enfant avec trisomie.", 11),
        s("On ne la commence que si l'hypothyroïdie est là, à la dose de la table, par exemple 25 à 75 µg de 0 à 6 mois.", 11),
        s("Le reste de la table, 8 µg/kg puis 5 à 6 µg/kg puis 4 à 5 µg/kg, suit l'âge si le traitement est indiqué.", 11),
    ],
    12: prevention() + [
        s("Le contrôle thyroïdien manquait chez une part importante de la série, puisque l'adhésion était de 61 pour cent.", 15),
    ],
    13: cles() + trisomie()[4:],
    14: [
        s("Cas corrigé. Un nourrisson avec trisomie, très hypotone, n'a pas eu de contrôle de thyréostimuline après la naissance.", 15),
        s("On avait conclu que le tonus bas faisait partie du syndrome, et rien d'autre.", 1),
        s("La correction est de vérifier la thyroïde, parce que l'hypothyroïdie peut accompagner l'hypotonie.", 1),
        s("Piège : recopier des mesures de visage qui ne sont pas dans le résumé lu.", 15),
    ],
}

NOYAUX[5] = {
    1: defs("L'hypothyroïdie congénitale est un déficit thyroïdien présent dès la naissance, qui peut baisser le tonus.", 11),
    2: thyro_epi() + epi_commune()[:1],
    3: [
        s("L'hormone manque au cerveau et au muscle en croissance.", 11),
        s("Jeannet cite l'hypothyroïdie parmi les accompagnements possibles de l'hypotonie.", 1),
        s("Sans traitement, le texte lu parle de prophylaxie du crétinisme par la dose la plus haute tolérée.", 11),
    ],
    4: demarche()[:4] + [
        s("On retrouve le résultat de thyréostimuline du talon avant d'ajouter des examens lourds.", 2),
        s("On contrôle ensuite la thyréostimuline pour ajuster, pas pour retarder la première dose indiquée.", 11),
    ],
    5: anamnese() + [
        s("On demande le dépistage, l'ictère prolongé, la hernie, la langue large et la prise de poids.", 1),
        s("Ces signes classiques ne sont pas une liste chiffrée dans Jeannet. On les tient pour l'orientation, sans score.", 1),
    ],
    6: EXAMEN + [
        s("Le tonus axial bas avec une fontanelle large et une mauvaise succion fait vérifier la thyroïde.", 1),
    ],
    7: DIFF + [
        s("La trisomie 21 et le syndrome de Prader-Willi partagent l'hypotonie. Le talon les sépare de cette cause.", 2),
        s("Un nourrisson malade peut être hypotone sans hypothyroïdie.", 1),
    ],
    8: [
        s("Le diagnostic positif repose sur la thyréostimuline du programme et la confirmation, pas sur le tonus seul.", 2),
        s("Vingt-huit cas en 2024 montrent que le motif reste réel en Suisse.", 2),
    ],
    9: thyro_epi() + [
        s("Le prélèvement part au laboratoire de Zurich avec le reste du carton.", 3),
    ],
    10: [
        s("Résultat au-dessus de la norme du programme : on confirme et on traite, sans attendre une faiblesse.", 2),
        s("Enfant déjà traité : on ajuste pour normaliser la thyréostimuline.", 11),
        s("Détresse aiguë : on traite le nourrisson malade en même temps, pas à la place.", 1),
    ],
    11: THYRO + [
        s("On ne commence pas par la dose basse du sujet âgé, qui est un autre passage du même texte.", 11),
        s("La dose de 25 µg citée pour le sujet âgé ou la maladie cardiaque n'est pas le schéma du nourrisson.", 11),
    ],
    12: prevention() + [
        s("Le dépistage de la thyréostimuline concerne tous les nouveau-nés du programme, 80 509 en 2024.", 2),
    ],
    13: cles() + [
        s("L'incidence lue reste 1 pour 3 500, avec 28 cas sur l'année 2024.", 2),
    ],
    14: [
        s("Cas corrigé. Un nourrisson hypotone de 3 semaines n'a pas de résultat de talon dans le dossier.", 2),
        s("On avait demandé une imagerie cérébrale en premier.", 1),
        s("La correction est de retrouver ou de refaire la thyréostimuline, puis de traiter si le diagnostic se confirme.", 11),
        s("La dose de départ lue, de 0 à 6 mois, est 25 à 75 µg, soit 10 µg/kg, autorisation 54949.", 11),
    ],
}

NOYAUX[6] = {
    1: defs("L'amyotrophie spinale liée au chromosome cinq détruit le motoneurone de la corne antérieure.", 1),
    2: sma_epi() + [
        s("Les causes centrales restent plus fréquentes, de 66 à 88 pour cent, ce qui ne doit pas faire rater celle-ci.", 1),
    ],
    3: [
        s("Le gène de survie du motoneurone manque. La corne antérieure dégénère.", 8),
        s("La langue peut fasciculer. Les réflexes tombent. La force tombe.", 1),
        s("Le cerveau, lui, n'explique pas l'aréflexie.", 1),
    ],
    4: demarche() + [
        s("Une hypotonie récente avec faiblesse et aréflexie fait chercher ce gène, même si le talon est déjà passé.", 1),
    ],
    5: anamnese() + [
        s("On demande le résultat du dépistage, les copies, la date du talon et la respiration.", 2),
        s("On demande si un traitement a déjà été commencé, et lequel.", 6),
    ],
    6: EXAMEN + [
        s("On cherche l'aréflexie, la faiblesse antigravitaire, la langue et la respiration paradoxale.", 1),
    ],
    7: DIFF + [
        s("La maladie de Pompe partage la faiblesse, mais elle charge le cœur.", 9),
        s("La jonction partage l'aréflexie possible et la fatigabilité, avec un contexte de toxine ou de mère myasthénique.", 5),
        s("Le central garde en général la force et les réflexes.", 1),
    ],
    8: [
        s("Le diagnostic positif est génétique : délétion ou mutation du gène, pas le seul examen.", 2),
        s("Le dépistage cherche la délétion homozygote.", 2),
        s("Jeannet nomme encore la forme de Werdnig-Hoffmann, ou type 1, devant ce tableau.", 1),
    ],
    9: sma_epi() + [
        s("Le rapport ne dit pas le nombre de copies qui déclenche le traitement. Cela se lit dans les informations professionnelles.", 2),
    ],
    10: [
        s("Dépistage positif et haut risque de forme infantile : le rapport décrit un traitement présymptomatique.", 2),
        s("Enfant symptomatique, faible et aréflexique : on confirme le gène et on adresse sans attendre l'imagerie.", 1),
        s("Détresse respiratoire : on sécurise l'air pendant que le traitement de fond se décide.", 5),
    ],
    11: SMA_DOSES,
    12: prevention() + [
        s("Le prélèvement au talon, envoyé à Zurich, est le filet suisse depuis le 1.3.2024.", 3),
    ],
    13: cles() + [
        s("Trois médicaments lus ont des schémas différents : 50 mg puis 28 mg, 12 mg, et les doses de risdiplam selon l'âge.", 6),
        s("L'onasemnogène s'arrête à l'âge de deux ans dans l'indication lue, autorisation 67529.", 8),
    ],
    14: [
        s("Cas corrigé. Un nourrisson de deux mois, faible, sans réflexes, a une créatine kinase normale.", 1),
        s("On avait exclu une maladie neuromusculaire à cause de ce dosage.", 1),
        s("La correction est de chercher le gène, parce qu'une créatine kinase normale n'exclut pas l'atteinte.", 1),
        s("Piège : utiliser le schéma de 12 mg sans connaître le risque d'hydrocéphalie rapporté.", 6),
    ],
}

NOYAUX[7] = {
    1: defs("Le syndrome de Prader-Willi est l'absence d'expression des gènes paternels en 15q11-q13.", 12),
    2: pws()[:4] + [
        s("Les causes centrales restent majoritaires, de 66 à 88 pour cent, et ce syndrome en est une cause précise.", 1),
    ],
    3: pws()[:3] + [
        s("L'hypotonie néonatale est presque constante, au-dessus de 97 pour cent dans la série lue.", 12),
        s("La mauvaise succion précède l'hyperphagie, qui vient plus tard.", 12),
    ],
    4: demarche() + [
        s("Un nourrisson hypotonique qui ne prend pas de poids doit faire demander le test, même s'il manque d'autres signes.", 12),
    ],
    5: anamnese() + [
        s("On demande la succion, la sonde, le gain de poids après 1 an, et l'hypogonadisme.", 12),
    ],
    6: EXAMEN + [
        s("On note l'axe, la succion, les organes génitaux et le contact, sans exiger tout le tableau ancien.", 12),
    ],
    7: DIFF + [
        s("L'hypothyroïdie et la trisomie 21 partagent l'hypotonie. Le test génétique les sépare.", 2),
        s("L'amyotrophie spinale partage la faiblesse néonatale, mais les réflexes et le gène diffèrent.", 1),
    ],
    8: pws()[4:],
    9: [
        s("Le test de laboratoire est la confirmation. Les critères cliniques ne le remplacent pas.", 12),
        s("Quinze patients sur 90 auraient été manqués par les anciens critères.", 12),
        s("Le dépistage au talon suisse, dans la fiche lue, ne cite pas ce syndrome parmi les maladies du carton.", 3),
    ],
    10: [
        s("Hypotonie et mauvaise prise de poids : on demande le test, sans attendre l'hyperphagie.", 12),
        s("Test positif : le diagnostic est posé. Le suivi nutritionnel change avec l'âge.", 12),
        s("Détresse : on traite le nourrisson malade en parallèle.", 1),
    ],
    11: [
        s("Aucune dose d'hormone de croissance n'est écrite : elle n'est pas dans les sources lues de ce lot.", 12),
        s("On protège la succion et la respiration, et on confirme par le laboratoire.", 12),
        s("On ne commence pas une lévothyroxine sans hypothyroïdie démontrée.", 11),
    ],
    12: prevention() + [
        s("Le piège de prévention est de ne pas tester l'enfant encore maigre.", 12),
    ],
    13: cles() + [
        s("Plus de 97 pour cent avaient l'hypotonie néonatale et le retard global dans la série de 90 patients.", 12),
    ],
    14: [
        s("Cas corrigé. Un nourrisson hypotone, nourri par sonde, n'est pas testé parce qu'il n'a pas encore d'hyperphagie.", 12),
        s("Les anciens critères ne sont pas au complet. La série dit que c'est fréquent.", 12),
        s("La correction est de demander le test génétique maintenant.", 12),
        s("Piège : annoncer le diagnostic sur les seuls critères, sans laboratoire.", 12),
    ],
}

NOYAUX[8] = {
    1: defs("La dystrophie myotonique congénitale est la forme la plus sévère, présente dès la naissance.", 14),
    2: steinert() + epi_commune()[:1],
    3: [
        s("Une expansion de répétitions dans le gène de la protéine kinase explique les formes lues.", 14),
        s("Le muscle et le cerveau sont touchés. L'atteinte cognitive peut être profonde.", 14),
        s("La mère peut être malade sans le savoir.", 14),
    ],
    4: demarche() + [
        s("Hydramnios, microrétrognathie et pied bot font chercher cette maladie chez l'enfant et chez la mère.", 14),
    ],
    5: anamnese() + steinert()[3:],
    6: EXAMEN + [
        s("On regarde la mâchoire, les pieds, la succion, la respiration et la force de la mère.", 14),
        s("On ne transforme pas un score d'Apgar bas en seuil de cette maladie.", 14),
    ],
    7: DIFF + [
        s("L'amyotrophie spinale et la maladie de Pompe partagent la faiblesse néonatale, pas le visage ni l'histoire maternelle.", 9),
        s("Le central pur n'explique pas à lui seul l'hydramnios avec pied bot.", 14),
    ],
    8: steinert() + [
        s("Le diagnostic positif est génétique. Le cas de 2026 ne donne pas un score diagnostique.", 14),
    ],
    9: [
        s("On demande l'analyse du gène chez l'enfant, et on examine la mère.", 14),
        s("La créatine kinase peut être normale dans une maladie musculaire du nourrisson. Elle n'exclut pas celle-ci.", 1),
        s("L'imagerie cérébrale ne remplace pas l'histoire obstétricale.", 1),
    ],
    10: [
        s("Signes anténataux et hypotonie : on pense à cette maladie et on protège la respiration.", 14),
        s("Mère symptomatique : on ne sépare pas son diagnostic de celui de l'enfant.", 14),
        s("Absence de ces signes : on revient à l'arbre général, sans forcer ce nom.", 1),
    ],
    11: [
        s("Aucune dose médicamenteuse de cette maladie n'est dans les sources lues. On n'en invente pas.", 14),
        s("On traite la respiration, l'alimentation et on confirme le gène.", 14),
        s("On ne donne pas les schémas de l'amyotrophie spinale sans le gène correspondant.", 6),
    ],
    12: prevention() + [
        s("Reconnaître l'hydramnios et le pied bot peut révéler la maladie de la mère avant la naissance suivante.", 14),
    ],
    13: cles() + [
        s("Un seul cas publié en 2026 ne fixe pas un seuil suisse.", 14),
    ],
    14: [
        s("Cas corrigé. Un deuxième enfant naît hypotone après un hydramnios, une petite mâchoire et un pied bot.", 14),
        s("L'aîné avait eu une hypotonie légère et une alimentation lente, classées banales.", 14),
        s("La correction est de chercher la dystrophie chez l'enfant et chez la mère.", 14),
        s("Piège : prendre l'Apgar bas pour un critère chiffré. Le texte ne le fait pas.", 14),
    ],
}

NOYAUX[9] = {
    1: defs("La maladie de Pompe à début infantile est une surcharge de glycogène du cœur et du muscle.", 9),
    2: pompe_txt()[:2] + [
        s("L'incidence globale estimée dans l'information professionnelle est de 1 pour 40 000 naissances.", 9),
        s("Ce n'est pas le registre suisse du dépistage. L'amyotrophie spinale, elle, est au carton depuis le 1.3.2024.", 3),
    ],
    3: pompe_txt()[1:],
    4: demarche() + [
        s("Une hypotonie avec grosse langue, foie, ou cœur large fait chercher cette maladie sans attendre.", 9),
    ],
    5: anamnese() + [
        s("On demande la fatigue au biberon, la sueur, la respiration et les antécédents familiaux.", 9),
    ],
    6: EXAMEN + [
        s("On écoute le cœur, on regarde la respiration et la force, pas seulement le tiré-assis.", 9),
    ],
    7: DIFF + [
        s("L'amyotrophie spinale n'élargit pas le cœur de cette façon.", 9),
        s("Une myocardite ou un nourrisson malade peuvent élargir le cœur : on ne pose pas Pompe sur le seul tonus.", 1),
    ],
    8: pompe_txt() + [
        s("Le diagnostic positif relie le déficit enzymatique au tableau. Le tonus seul ne suffit pas.", 9),
    ],
    9: [
        s("L'enzyme et le cœur se demandent quand le tableau est là. La créatine kinase normale n'écarte pas le muscle.", 1),
        s("Le dépistage suisse lu en 2025 ne met pas cette maladie sur le carton du talon.", 3),
    ],
    10: [
        s("Cardiomyopathie et hypotonie du nourrisson : on confirme et on traite, la mortalité naturelle est précoce.", 9),
        s("Forme atypique, cœur moins atteint : on ne promet pas le même rythme, le texte la distingue.", 9),
        s("Choc ou pause : on réanime d'abord, le classement vient avec.", 1),
    ],
    11: POMPE + [
        s("On surveille les anticorps et les réactions de perfusion, décrites dans le même texte.", 9),
        s("On ne choisit pas 40 mg/kg comme dose de routine.", 9),
    ],
    12: prevention() + [
        s("Repérer tôt la cardiomyopathie est la prévention de l'arrêt, dans la limite de ce que le texte décrit.", 9),
    ],
    13: cles() + [
        s("La dose qui reste recommandée est 20 mg/kg toutes les 2 semaines, autorisation 58038.", 9),
    ],
    14: [
        s("Cas corrigé. Un nourrisson hypotone a un cœur large. On avait conclu à une asphyxie ancienne.", 1),
        s("La créatine kinase était normale, ce qui avait faussement rassuré.", 1),
        s("La correction est de chercher la maladie de Pompe et, si elle est confirmée, de perfuser 20 mg/kg.", 9),
        s("Piège : monter d'emblée à 40 mg/kg parce que la maladie est grave. L'essai n'a pas montré ce gain.", 9),
    ],
}

NOYAUX[10] = {
    1: defs("L'atteinte de la jonction neuromusculaire bloque la transmission, sans détruire d'abord la corne.", 1),
    2: [
        s("Jeannet place les syndromes myasthéniques à la jonction, à côté du nerf et du muscle.", 1),
        s("Le botulisme reste rare, un à deux cas par an en Suisse, mortalité de 5 à 10 pour cent.", 5),
    ] + epi_commune()[:1],
    3: [
        s("La toxine botulique empêche la libération à la jonction.", 5),
        s("La myasthénie néonatale vient du passage d'anticorps maternels, dans le cadre lu de l'autorisation 19943.", 10),
        s("La corne antérieure et le muscle peuvent être structurellement intacts au début.", 1),
    ],
    4: demarche() + BOT[:4],
    5: anamnese() + [
        s("On demande le miel, les conserves, la faiblesse de la mère, et les paupières.", 5),
        s("La paralysie alimentaire commence entre 12 et 72 heures, par les yeux et la langue.", 5),
    ],
    6: EXAMEN + [
        s("On regarde les paupières, la succion, la voix faible et la fatigue au fil de l'examen.", 1),
        s("La pupille et la respiration font partie de l'examen quand on pense au botulisme.", 5),
    ],
    7: DIFF + [
        s("L'amyotrophie spinale dure et progresse. Le botulisme alimentaire est aigu, après un repas.", 5),
        s("Le central donne plutôt des réflexes vifs et parfois des crises.", 1),
        s("La maladie de Pompe met le cœur au premier plan.", 9),
    ],
    8: [
        s("Le diagnostic positif du botulisme est clinique et toxicologique. La fiche ne donne pas un score.", 5),
        s("La myasthénie néonatale se discute devant la mère et le nouveau-né faible, selon le texte de l'autorisation 19943.", 10),
        s("On ne confirme pas la jonction sur le seul tonus bas.", 1),
    ],
    9: [
        s("L'électromyogramme est difficile chez le petit enfant et rarement déterminant.", 1),
        s("On ne retarde pas les soins intensifs pour un tracé.", 5),
        s("La créatine kinase normale n'exclut pas, en parallèle, une maladie du muscle.", 1),
    ],
    10: [
        s("Paralysie descendante, yeux et langue, aliment ou miel : soins intensifs immédiatement.", 5),
        s("Antitoxine au stade précoce, sans inventer un milligramme.", 5),
        s("Nouveau-né d'une mère myasthénique : on suit la succion et la respiration, et on lit l'autorisation 19943.", 10),
    ],
    11: JONCTION + BOT,
    12: prevention(),
    13: cles() + [
        s("La référence néonatale lue est 5 mg par voie orale, pas la dragée de 60 mg, autorisation 19943.", 10),
        s("L'antitoxine n'a pas de dose en milligrammes dans la fiche d'avril 2023.", 5),
    ],
    14: [
        s("Cas corrigé. Un nourrisson de 4 mois, nourri au miel, devient faible, les paupières tombent.", 5),
        s("On avait proposé un avis dans quelques mois, comme pour une hypotonie légère isolée.", 1),
        s("La correction est les soins intensifs et l'antitoxine précoce, pas l'attente.", 5),
        s("Piège : donner 60 mg de pyridostigmine parce que c'est la dragée adulte.", 10),
    ],
}


def _act(verbes: list[str]) -> list[str]:
    return verbes


ACTIONS = {
    "A": _act([
        "refaire le tiré-assis et noter la chute de la tête",
        "comparer la force des membres à la tenue de l'axe",
        "chercher la posture en jambe de grenouille",
        "tester le ballant des quatre membres",
        "noter les réflexes et la succion",
        "demander les mouvements fœtaux et l'hydramnios",
        "vérifier le résultat du talon",
        "séparer tonus, force et amplitude",
        "protéger la respiration avant le classement",
        "relire la glycémie seulement dans son cadre",
        "chercher le miel si la faiblesse est aiguë",
        "écrire l'étage retenu et celui écarté",
        "peser l'enfant et noter la courbe",
        "regarder les yeux et le périmètre crânien",
        "ne pas fermer le dossier sur une créatine kinase normale",
        "prévoir l'avis neuropédiatrique si le tableau dure",
    ]),
    1: _act([
        "noter si la force est gardée",
        "comparer les réflexes au tonus axial",
        "chercher une crise ou un trouble des yeux",
        "mesurer le périmètre crânien",
        "demander le développement global",
        "différer l'imagerie tant que l'hypothèse manque",
        "écarter l'attente si un signe neurologique s'ajoute",
        "rechercher une dysmorphie sans inventer de mesure",
        "vérifier que le nourrisson n'est pas aigu",
        "écrire pourquoi l'étage central est retenu",
        "recontrôler la succion",
        "surveiller l'évolution vers une spasticité",
        "laisser le périphérique ouvert si l'aréflexie apparaît",
        "expliquer l'incertitude du terme bénin",
        "revoir dans un délai court si l'axe reste faible",
        "noter le contact et l'éveil",
    ]),
    2: _act([
        "sécuriser l'air et la respiration",
        "prendre la température et la couleur",
        "lire l'âge gestationnel avant tout chiffre de glycémie",
        "recontrôler la glycémie dans le cadre de la maternité",
        "ne pas utiliser le cadre de maternité en soins intensifs",
        "demander le miel et les repas",
        "chercher une paralysie des yeux et de la langue",
        "appeler les soins intensifs si la respiration chute",
        "traiter la cause aiguë avant l'étiquette de tonus",
        "noter l'heure du dernier repas",
        "éviter d'inventer un volume de gel",
        "écrire que l'antitoxine n'a pas de milligramme lu",
        "surveiller la reprise du tonus après le traitement de la cause",
        "ne pas classer hyperlaxe un enfant gris",
        "refaire l'examen quand la fièvre tombe",
        "transmettre le cadre de 35 semaines à l'équipe",
    ]),
    3: _act([
        "mesurer l'amplitude sans la confondre avec le tonus",
        "tester le pouce, le coude et le genou",
        "demander si les paumes touchent le sol",
        "noter l'âge avant de choisir la version du score",
        "garder les deux totaux lus, sans les fusionner",
        "vérifier la force contre gravité",
        "chercher une aréflexie qui ferait quitter ce diagnostic",
        "expliquer la fréquence chez les personnes saines",
        "ne pas promettre un seuil suisse officiel",
        "adresser si la faiblesse s'installe",
        "protéger l'articulation douloureuse",
        "relire les cinq items avant de conclure",
        "distinguer laxité locale et forme généralisée",
        "noter la cheville seulement chez le jeune enfant",
        "écrire que la cohorte n'est pas un standard de cabinet",
        "revoir si une douleur ou une entorse se répète",
    ]),
    4: _act([
        "vérifier le contrôle de thyréostimuline",
        "noter le suivi du rachis sans inventer un pourcentage cardiaque",
        "examiner l'axe et la succion",
        "ne pas recopier de mesure du visage",
        "chercher une faiblesse nouvelle qui dépasse le syndrome",
        "traiter une détresse comme chez tout nourrisson malade",
        "expliquer que l'hypotonie est centrale dans ce classement",
        "demander le sommeil et l'alimentation",
        "revoir la courbe de poids",
        "laisser ouvert le diagnostic de Prader-Willi si le test manque",
        "ne pas attribuer toute hypotonie au chromosome",
        "rappeler le contrôle thyroïdien manquant",
        "vérifier le résultat du talon",
        "regarder les réflexes",
        "planifier le contrôle manquant",
        "décrire le tonus aux parents avec des mots simples",
    ]),
    5: _act([
        "retrouver le résultat de thyréostimuline",
        "ne pas commencer par l'imagerie",
        "écrire la dose selon l'âge, autorisation 54949",
        "viser la dose haute tolérée dans la forme congénitale",
        "contrôler ensuite la thyréostimuline",
        "distinguer la table de l'enfant de la dose basse du sujet âgé",
        "autoriser l'allaitement aux doses thérapeutiques lues",
        "noter les 28 cas de 2024 comme rappel, pas comme pronostic individuel",
        "vérifier l'ictère et la prise de poids",
        "examiner la succion et l'axe",
        "ne pas attendre une faiblesse pour traiter un résultat confirmé",
        "expliquer la prophylaxie du crétinisme avec les mots du texte",
        "adapter la dose à la réponse",
        "séparer ce diagnostic d'une trisomie non hypothyréoïdienne",
        "transmettre la table d'âge à l'équipe",
        "revoir après l'ajustement",
    ]),
    6: _act([
        "lire le résultat du dépistage au talon",
        "chercher faiblesse, aréflexie et langue",
        "ne pas rassurer sur une créatine kinase normale",
        "adresser sans attendre une imagerie non indiquée",
        "protéger la respiration",
        "citer l'autorisation avant toute dose",
        "distinguer le schéma de charge du schéma d'entretien",
        "rappeler l'hydrocéphalie rapportée avec le schéma ancien",
        "choisir la dose de risdiplam selon l'âge et le poids",
        "respecter la limite d'âge lue pour l'onasemnogène",
        "prévoir le corticoïde avant la perfusion si elle est décidée",
        "surveiller le foie après la perfusion",
        "ne pas promettre un nombre de copies absent du rapport de dépistage",
        "noter les 6 cas de 2024 sans en faire un taux local",
        "écrire le centre et le médecin qui suivent",
        "recontrôler la succion et la toux",
    ]),
    7: _act([
        "demander le test devant hypotonie et mauvaise prise de poids",
        "ne pas attendre l'hyperphagie",
        "expliquer que les critères ne remplacent pas le laboratoire",
        "noter la succion et le recours à la sonde",
        "regarder les organes génitaux sans conclure seul",
        "distinguer ce syndrome de l'hypothyroïdie par le talon",
        "protéger l'alimentation",
        "ne pas inventer une dose d'hormone de croissance",
        "écrire les proportions lues, délétion et disomie, comme repères",
        "rappeler que 15 patients sur 90 échappaient aux anciens critères",
        "surveiller le virage de poids après 1 an",
        "laisser le neuropédiatre confirmer le suivi",
        "ne pas classer bénigne cette hypotonie",
        "vérifier la respiration pendant les repas",
        "informer les deux parents du sens du test",
        "revoir la courbe à la visite suivante",
    ]),
    8: _act([
        "demander l'hydramnios, la mâchoire et les pieds",
        "examiner la mère",
        "ne pas transformer l'Apgar en seuil",
        "protéger la respiration et la succion",
        "demander le test génétique sans l'inventer dans le détail technique",
        "rappeler qu'il s'agit d'un cas publié, pas d'une série suisse",
        "distinguer cette maladie de l'amyotrophie spinale",
        "ne pas donner un médicament de l'amyotrophie sans le gène",
        "noter l'alimentation lente",
        "chercher une faiblesse maternelle passée inaperçue",
        "expliquer l'expansion de répétitions avec des mots simples",
        "laisser ouvert le central si les signes anténataux manquent",
        "revoir la fratrie",
        "écrire ce qui a été vu et ce qui ne l'a pas été",
        "surveiller le contact, l'atteinte cognitive étant possible",
        "adresser en neuromusculaire",
    ]),
    9: _act([
        "écouter le cœur et regarder la respiration",
        "ne pas conclure à une asphyxie seule",
        "ne pas rassurer sur une créatine kinase normale",
        "confirmer avant de citer la dose lue",
        "commencer la perfusion au débit bas si le traitement est décidé",
        "monter le débit par paliers si aucune réaction",
        "ne pas choisir la dose haute étudiée comme routine",
        "surveiller une réaction de perfusion",
        "expliquer la mortalité naturelle de la première année",
        "distinguer la forme atypique, au cœur moins atteint",
        "adresser sans perdre de jours",
        "noter le foie et la langue si on les a vus",
        "séparer ce diagnostic de l'amyotrophie spinale",
        "écrire l'autorisation 58038 à côté de la dose",
        "recontrôler le poids pour la dose",
        "prévoir le prélèvement d'anticorps décrit dans le texte",
    ]),
    10: _act([
        "demander le miel et l'heure du repas",
        "examiner les paupières, la langue et la respiration",
        "envoyer en soins intensifs si la paralysie descend",
        "ne pas inventer un milligramme d'antitoxine",
        "citer la pharmacie de l'armée comme source lue de l'antitoxine",
        "préférer la néostigmine dans la myasthénie néonatale",
        "réserver la pyridostigmine au cas où la néostigmine ne convient pas",
        "ne pas donner la dragée adulte au nouveau-né",
        "rappeler que le petit comprimé ne convient pas à la pédiatrie",
        "ne pas attendre quelques mois devant une faiblesse aiguë",
        "distinguer la jonction de la corne antérieure",
        "protéger la toux et la déglutition",
        "rappeler le délai alimentaire lu",
        "rappeler l'absence de vaccin humain en Suisse",
        "expliquer l'interdiction du miel avant un an",
        "revoir la mère si une myasthénie est possible",
    ]),
}

SCHEMAS = {
    "A": ("Orientation du tonus bas", [
        ("Repos", ["Membres étendus sur le lit", "Hanches en grenouille", "Force encore à juger"]),
        ("Actif", ["Tiré-assis, tête en arrière", "Aisselles, l'enfant glisse", "Ventral, le corps pend"]),
        ("Étage", ["Central : force gardée", "Périphérique : faiblesse", "Malade : traiter d'abord"]),
    ]),
    1: ("Hypotonie centrale", [
        ("Signes", ["Axe plus faible que membres", "Réflexes vifs ou normaux", "Crises ou tête anormale"]),
        ("Suite", ["Imagerie après hypothèse", "Image parfois normale", "Avis si le tableau dure"]),
        ("Écarter", ["Aréflexie et faiblesse", "Cœur large type Pompe", "Miel et paralysie aiguë"]),
    ]),
    2: ("Nourrisson malade", [
        ("D'abord", ["Air et respiration", "Couleur et chaleur", "Cause aiguë"]),
        ("Maternité", ["Dès 35 semaines", "Sous 2,6 mmol/l", "Pas le seuil de 2,0"]),
        ("Hors cadre", ["Pas avant 35 semaines", "Pas les soins intensifs", "Miel : soins intensifs"]),
    ]),
    3: ("Hyperlaxité", [
        ("Après 5 ans", ["Cinq items bilatéraux", "Total lu : au moins 4", "Paumes au sol"]),
        ("Avant 5 ans", ["Cheville au-delà de 30 degrés", "Total lu : supérieur à 4", "Pas une norme suisse"]),
        ("Force", ["Amplitude n'est pas tonus", "Faiblesse : quitter ce nom", "Ullrich : les deux"]),
    ]),
    4: ("Trisomie 21", [
        ("Classement", ["Syndrome dysmorphique", "Hypotonie centrale", "Force souvent gardée"]),
        ("Suivi lu", ["Thyroïde : 61 pour cent", "Rachis : 94 pour cent", "Visage non recopié"]),
        ("Alerte", ["Faiblesse nouvelle", "Talon à relire", "Détresse : traiter"]),
    ]),
    5: ("Hypothyroïdie", [
        ("Talon", ["Thyréostimuline pour tous", "28 cas en 2024", "1 pour 3 500"]),
        ("Dose", ["0 à 6 mois : 25 à 75 µg", "Puis selon la table d'âge", "Autorisation 54949"]),
        ("But", ["Dose haute tolérée", "Normaliser la thyréostimuline", "Allaitement possible"]),
    ]),
    6: ("Amyotrophie spinale", [
        ("Dépistage", ["Depuis le 1.3.2024", "6 cas en 2024", "1 pour 11 500"]),
        ("Clinique", ["Faiblesse et aréflexie", "Langue à regarder", "Kinase souvent normale"]),
        ("Traitements", ["50 mg puis 28 mg", "Ou schéma 12 mg", "Jusqu'à deux ans : gène"]),
    ]),
    7: ("Prader-Willi", [
        ("Presque constant", ["Hypotonie néonatale", "Plus de 97 pour cent", "Retard global aussi"]),
        ("Plus tard", ["Poids excessif après 1 an", "Hyperphagie", "Hypogonadisme"]),
        ("Test", ["Critères = demander", "Laboratoire = confirmer", "15 sur 90 manqués"]),
    ]),
    8: ("Myotonie congénitale", [
        ("Avant la naissance", ["Hydramnios", "Petite mâchoire", "Pied bot"]),
        ("À la naissance", ["Forme la plus sévère", "Succion et respiration", "Mère parfois non connue"]),
        ("Limite", ["Un cas de 2026", "Apgar : pas un seuil", "Pas une série suisse"]),
    ]),
    9: ("Pompe infantile", [
        ("Cœur", ["Glycogène massif", "Cardiomyopathie rapide", "Mort dans la première année"]),
        ("Muscle", ["Hypotonie généralisée", "Progrès perdus", "Kinase non décisive"]),
        ("Perfusion", ["20 mg/kg / 2 semaines", "Départ 1 mg/kg/h", "Pas 40 mg/kg d'emblée"]),
    ]),
    10: ("Jonction", [
        ("Botulisme", ["Yeux et langue", "12 à 72 heures", "Soins intensifs"]),
        ("Antitoxine", ["Stade précoce", "Aucun milligramme lu", "Pharmacie de l'armée"]),
        ("Myasthénie", ["Néostigmine d'abord", "Sinon 5 mg oral", "Pas la dragée de 60 mg"]),
    ]),
}


def _controle() -> None:
    cles_ok = ["A", *range(1, 11)]
    for cle in cles_ok:
        if set(NOYAUX[cle]) != set(range(1, 15)):
            raise SystemExit(f"points manquants {cle}")
        if cle not in ACTIONS or cle not in SCHEMAS:
            raise SystemExit(f"action ou schéma manquant {cle}")
        for n, lignes in NOYAUX[cle].items():
            for texte, _src in lignes:
                if RX.findall(texte) and len(RX.findall(texte)) > 32:
                    raise SystemExit(f"phrase longue {cle} p{n} ({len(RX.findall(texte))}) : {texte}")
                if "mmol/L" in texte or "À vérifier" in texte or "(?)" in texte:
                    raise SystemExit(texte)
        for v in ACTIONS[cle]:
            if len(RX.findall(v)) > 14:
                raise SystemExit(f"action longue {cle}: {v}")
        _titre, niveaux = SCHEMAS[cle]
        if len(niveaux) != 3:
            raise SystemExit(f"schéma {cle}")
        for _nom, lignes in niveaux:
            if len(lignes) != 3:
                raise SystemExit(f"lignes {_nom}")
            for ligne in lignes:
                if len(ligne) > 42:
                    raise SystemExit(f"ligne svg longue : {ligne}")


_controle()
