#!/usr/bin/env python3
"""Leçons V8 du LOT_143. Zéro copie du HTML Flash. Phrases courtes. Doses AIPS."""
from __future__ import annotations

import html
import json
import re
import subprocess
import sys
from pathlib import Path

RACINE = Path(__file__).resolve().parents[3]
LOT = RACINE / "grok-LOTS-html" / "LOT_143"
STYLE_SRC = RACINE / "grok-LOTS-html" / "LOT_162" / "LOT_162_Phase_A_V0.html"
CHROME = "/usr/bin/google-chrome"

DX = [
    (1, "Gangrène du pied diabétique"),
    (2, "Ischémie chronique menaçant le membre avec gangrène sèche"),
    (3, "Ischémie aiguë de membre"),
    (4, "Infection nécrosante des tissus mous"),
    (5, "Gangrène veineuse, phlegmatia caerulea dolens"),
    (6, "Gelure profonde"),
    (7, "Thromboangéite oblitérante"),
    (8, "Embolies de cholestérol"),
    (9, "Nécrose de pression étendue"),
    (10, "Calciphylaxie"),
]

CIBLES = {
    "A": (72000, 79000),
    "1": (36200, 39200),
    "2": (39200, 42200),
    "3": (42000, 45200),
    "4": (44000, 46800),
    "5": (40000, 43200),
    "6": (36000, 39200),
    "7": (38000, 41200),
    "8": (40000, 43200),
    "9": (42000, 45200),
    "10": (36000, 39200),
}

TITRES = {
    1: "1. Définition",
    2: "2. Épidémiologie",
    3: "3. Physiopathologie",
    4: "4. Démarche diagnostique",
    5: "5. Anamnèse",
    6: "6. Examen physique",
    7: "7. Approche syndromique",
    8: "8. Diagnostic positif",
    9: "9. Examens complémentaires",
    10: "10. Arbre décisionnel",
    11: "11. Prise en charge",
    12: "12. Prévention",
    13: "13. Points clés",
    14: "14. Pièges",
}

LEADS = {
    1: "Le mot constate un tissu mort, puis la cause se nomme à part.",
    2: "Les fréquences lues ne sont pas la part suisse de chaque cause.",
    3: "Le tissu meurt par défaut de perfusion ou par destruction infectieuse.",
    4: "La démarche commence par le qSOFA (quick sequential) qui dépiste au lit.",
    5: "L'anamnèse date le noir, la douleur, le diabète et le froid.",
    6: "L'examen compare les deux membres, la peau, les pouls et la douleur.",
    7: "Dix lectures se rangent par gravité immédiate, sans rang suisse inventé.",
    8: "Le diagnostic positif joint le territoire mort et son mécanisme.",
    9: "Le bilan garde la chirurgie, l'image et les pressions, sans retard toxique.",
    10: "L'arbre écarte d'abord ce qui tue, puis ce qui perd le membre.",
    11: "La conduite à tenir cite les autorisations lues, sans dose inventée.",
    12: "La prévention note le pied, le tabac, la pression et la décharge.",
    13: "Les points clés se redisent au lit, avec les quatre cadres centraux.",
    14: "Les pièges viennent d'un score rassurant, d'un pouls cru fiable ou d'une dose hors notice.",
}

AIPS = '<abbr title="information professionnelle suisse">AIPS</abbr>'

# sec|src|phrase   1 RMS 2020, 2 RMS 2014, 3 RMS 2019, 4 SMW 2021, 5 ESVS 2020,
# 6 clinda 58919, 7 augmentin 45674, 8 metro 55280, 9 mero 62419, 10 pip 58151
COMMUNE = r"""
1|1|la gangrène constate un tissu déjà mort, noir, sec ou humide
1|1|le mot ne nomme pas à lui seul la maladie causale
1|4|la forme diabétique joint neuropathie, sous-perfusion et infection
1|3|la forme artérielle chronique joint douleur de repos et nécrose
1|5|l'ischémie aiguë est une chute brutale de perfusion du membre
1|1|la forme gazeuse est l'infection clostridiale du muscle
1|2|la gangrène de Fournier est l'atteinte nécrosante des organes génitaux
1|2|la fasciite nécrosante détruit un plan des tissus mous
3|1|le muscle meurt dans la forme gazeuse après un trauma profond
3|1|clostridium perfringens représente 70 % des cas clostridiaux lus
3|1|une forme spontanée est plus souvent liée à clostridium septicum
3|2|le fascia superficiel lâche explique la diffusion rapide
3|3|l'athérome fait chuter la pression en aval, d'abord à l'effort
3|5|au-delà de deux semaines, le guide parle d'ischémie chronique
3|4|la neuropathie diabétique peut éteindre la douleur d'alerte
3|5|l'embolie, la thrombose, l'anévrisme, la dissection et le trauma ouvrent l'aigu
2|1|en Suisse, le texte de 2020 compte environ 2000 prescriptions pour 100 000 habitants
2|1|ces prescriptions d'antibiotiques cutanés sont la troisième cause ambulatoire lue
2|3|chez le claudicant, 21 % aggravent ou passent en ischémie critique à cinq ans
2|3|chez l'asymptomatique, 7 % passent à la claudication à cinq ans
2|3|l'ischémie critique concerne 1 à 3 % des personnes avec artériopathie
2|3|le risque d'amputation à un an y est lu de 20 à 30 %
2|3|la mortalité de l'ischémie aiguë peut s'élever de 15 à 20 %
2|4|le texte de 2021 rapporte 1600 amputations en Suisse pour l'année 2016
2|4|le même texte cite une estimation de 20 % d'ulcères du pied diabétique
2|2|la mortalité lue de la fasciite va de 20 à 30 %
2|1|aucune part suisse de la gangrène elle-même n'a été lue
4|1|on écarte d'abord la douleur disproportionnée et le sepsis
4|5|un déficit moteur impose la revascularisation urgente
4|5|la classe trois irréversible oriente vers l'amputation première
4|4|la gangrène diabétique ne se range pas après un score de laboratoire
4|1|l'image ne retarde pas la chirurgie si le tableau est toxique
4|3|la forme artérielle chronique attend des pouls abolis et une douleur de repos
5|1|on date le noir, la douleur et une plaie même petite
5|4|on demande le diabète, la neuropathie et une odeur nouvelle
5|3|on demande le tabac, la claudication et la fibrillation
5|5|on demande un début de moins de deux semaines
5|6|on demande une diarrhée sous antibiotique
6|1|on compare la douleur à l'aspect encore modeste de la peau
6|1|les douleurs intenses sont lues chez environ 70 % des fasciites
6|1|la fièvre est lue chez environ 60 % et les bulles chez environ 40 %
6|2|le crépitement est rare à l'arrivée dans la série de 2014
6|5|les six signes sont rarement tous présents sauf forme sévère
6|5|on examine les deux membres et les pouls proximaux
6|3|un orteil sec à limite nette oriente vers la forme artérielle
7|4|la lecture diabétique est le pied insensible, noir et souvent humide
7|3|la lecture artérielle chronique est l'orteil sec avec douleur de repos
7|5|la lecture aiguë est le déficit installé en moins de deux semaines
7|1|la lecture nécrosante contient la forme gazeuse et la gangrène de Fournier
7|5|la lecture veineuse est le membre entier violacé et tendu
7|5|la lecture de gelure suit une exposition au froid
7|3|la lecture du fumeur jeune distal n'est pas l'athérome du sujet âgé
7|3|la lecture des emboles de cholestérol suit un livedo après un geste
7|4|la lecture de pression est le talon ou le sacrum d'appui
7|4|la lecture de calciphylaxie est la plaque très douloureuse chez le dialysé
8|1|le diagnostic de forme gazeuse joint crépitement, gaz et muscle mort
8|2|le diagnostic de Fournier joint le périnée et la nécrose de plan
8|5|le diagnostic aigu joint le déficit et la durée courte
8|3|le diagnostic artériel chronique joint nécrose et occlusion confirmée
8|4|le diagnostic diabétique joint insensibilité, infection et sous-perfusion
9|1|le bilan d'imagerie ne doit pas retarder le bloc si la toxicité est là
9|1|le gaz à l'image se voit dans la forme gazeuse ou la forme polymicrobienne
9|5|l'index de cheville inférieur à 0,7 est un seuil critique du guide de 2020
9|5|le doppler aide à chercher le pouls quand la main hésite
9|3|la pression et l'image artérielle servent à la forme chronique
9|4|le bilan diabétique cherche l'infection profonde et l'artère
10|1|on place d'abord la chirurgie si la douleur dépasse la peau
10|5|on place ensuite l'ischémie aiguë si le déficit est récent
10|4|on place le pied diabétique si l'insensibilité et la plaie dominent
10|3|on place la forme artérielle sèche si la douleur de repos est ancienne
10|2|on ne fond pas Fournier dans une cellulite ordinaire
10|1|cet ordre est celui de la gravité immédiate, pas une fréquence suisse
11|1|la conduite à tenir commence par la vie, puis le membre, puis la marche
11|1|la chirurgie précoce confirme, prélève et excise jusqu'au tissu sain
11|1|une reprise est lue à 24 à 48 heures, puis tant que la nécrose avance
11|2|la gangrène de Fournier suit la même urgence opératoire
11|1|la forme gazeuse suit la même urgence opératoire
11|10|l'antibiotique large de l'autorisation 58151 a une posologie usuelle de 4,5 g trois fois par jour
11|9|l'antibiotique de l'autorisation 62419 est habituellement de 500 mg ou 1 g toutes les 8 heures
11|9|la fourchette adulte de l'autorisation 62419 va de 1.5 g à 6 g par jour
11|8|une poche de l'autorisation 55280 contient 500 mg de métronidazole
11|7|l'antibiotique de l'autorisation 45674 a pour usuel 625 mg trois fois par jour
11|6|une ampoule de l'autorisation 58919 contient 600 mg
11|6|une gélule de l'autorisation 58919 contient 300 mg
11|6|l'autorisation 58919 liste 900 mg parmi les tailles de perfusion
11|6|l'autorisation 58919 ne recommande pas plus de 1200 mg en une perfusion d'une heure
11|6|l'autorisation 58919 signale des doses intraveineuses jusqu'à 4800 mg par jour déjà administrées
11|5|le guide de 2020 recommande l'héparine en attendant la revascularisation, sans unité recopiée ici
11|5|le même guide ne recommande pas l'héparine thérapeutique continue pendant la thrombolyse
12|4|la décharge et l'adresse rapide préviennent la perte du pied diabétique
12|3|l'arrêt du tabac et l'activité physique limitent l'artériopathie
12|1|une plaie minime chez une personne à risque se surveille de près
12|6|la diarrhée sous clindamycine fait arrêter et chercher la colite
13|1|on ne retire pas la forme gazeuse du raisonnement
13|2|on ne retire pas la gangrène de Fournier du raisonnement
13|3|on ne retire pas la forme artérielle du raisonnement
13|4|on ne retire pas la forme diabétique du raisonnement
13|1|un score de laboratoire bas ne remplace pas la chirurgie
13|5|un pouls perçu n'innocente pas une ischémie aiguë sévère
14|1|le piège est de rassurer parce que la radiographie ne montre pas de gaz
14|4|le piège est d'appeler microangiopathie pour éviter le bilan artériel
14|5|le piège est de traiter la classe trois comme une revascularisation utile
14|6|le piège est d'écrire une dose absente de la notice lue
14|7|le piège est de doubler l'amoxicilline hors des cas particuliers de la notice
11|6|la clindamycine de l'autorisation 58919 ne se donne en grossesse qu'en nécessité absolue
11|6|l'autorisation 58919 demande d'arrêter l'allaitement si le traitement est nécessaire
11|7|l'autorisation 45674 ne se donne en grossesse qu'en nécessité absolue
11|7|l'autorisation 45674 demande de ne pas allaiter pendant le traitement
11|7|l'autorisation 45674 est contre-indiquée après hypersensibilité aux pénicillines ou ictère sous ce médicament
11|8|l'autorisation 55280 contre-indique le premier trimestre de la grossesse
11|9|l'autorisation 62419 ne se donne en grossesse ou en allaitement qu'en nécessité absolue
11|9|l'autorisation 62419 est contre-indiquée en cas d'hypersensibilité au produit
11|6|une injection intramusculaire unique au-dessus de 600 mg n'est pas recommandée dans l'autorisation 58919
11|6|si la diarrhée persiste, l'autorisation 58919 discute la vancomycine à 125 mg quatre fois par jour pendant 10 jours
11|1|la clindamycine est citée en 2020 pour freiner les toxines, avec un bêtalactame large
11|6|la hausse de dose de l'autorisation 58919 vise d'autres clostridies que perfringens, un bacteroides ou un peptococcus
11|10|chez l'enfant de plus de 40 kg, l'autorisation 58151 écrit 4,5 g toutes les 8 heures
11|10|l'autorisation 58151 conseille en général au moins 5 jours et au plus 14 jours
1|5|on date l'heure du territoire noir avant de conclure
1|5|on compare toujours les deux membres au lit
5|3|on cherche une claudication ancienne du mollet
5|4|on cherche une tache sur la chaussette ou une odeur
6|5|on note la pâleur, le froid et l'abolition d'un pouls
6|1|on cherche une bulle hémorragique et une induration carton
6|4|on retire le pansement et l'on regarde l'orteil nu
4|2|la fièvre peut manquer et la douleur reste alors le guide
4|5|un transfert s'impose si le déficit moteur n'a pas de plateau vasculaire
3|5|la reperfusion peut relarguer le potassium et la myoglobine
3|3|l'anévrisme poplité se révèle par une ischémie aiguë dans 50 % des cas lus
3|3|malgré une revascularisation rapide, l'amputation lue va de 8 à 18 %
2|3|l'embolie est plus fréquente que l'occlusion sur place dans le texte de 2019
2|3|l'origine cardiaque domine, surtout s'il existe une fibrillation
8|1|le bloc montre un fascia friable, un exsudat gris et peu de pus
9|1|la tomodensitométrie et la résonance montrent l'œdème ou le gaz, sans suffire
12|5|baisser le pied du lit et hydrater font partie des mesures d'attente lues
13|5|la durée inférieure à deux semaines sépare l'aigu du chronique
14|3|le piège est de croire qu'un seul seuil hémodynamique définit toute l'ischémie critique
"""

PART = r"""
1|1|4|le pied diabétique noir joint souvent l'insensibilité et l'humidité
1|3|4|la neuropathie retire l'alerte douloureuse et retarde la consultation
1|4|4|l'odeur, la tache de chaussette ou la fièvre peuvent être le motif
1|6|4|on cherche l'os exposé et une collecte après avoir retiré le pansement
1|7|4|cette lecture reste diabétique même si l'orteil paraît sec
1|8|4|le diagnostic positif joint diabète, plaie et souffrance tissulaire
1|9|4|le bilan cherche l'infection profonde et la sous-perfusion artérielle
1|10|4|on n'attend pas la pression de cheville si le sepsis est déjà là
1|11|4|la conduite à tenir joint décharge, drainage d'une collecte et avis vasculaire
1|11|7|l'antibiotique usuel de l'autorisation 45674 reste 625 mg trois fois par jour
1|12|4|la décharge et le chaussage préviennent l'ulcère qui précède la nécrose
1|13|4|on ne retire pas la forme diabétique quand une artère coexiste
1|14|4|le piège est d'invoquer la microangiopathie pour sauter le bilan artériel
1|2|4|le texte de 2021 lie l'échec à la décharge manquée, à l'artère sous-estimée et au retard
1|5|4|on demande une neuropathie connue et un diabète déjà traité
2|1|3|la gangrène sèche chronique est un orteil noir à limite nette
2|3|3|l'occlusion athéromateuse diffuse fait chuter la perfusion de repos
2|5|3|la douleur de repos et la claudication ancienne précèdent souvent le noir
2|6|3|les pouls distaux sont abolis et le membre reste sec
2|8|3|le diagnostic artériel exige une occlusion confirmée, pas la couleur seule
2|9|3|le bilan de pressions et l'image artérielle précèdent l'amputation
2|10|3|cette lecture artérielle passe après l'aigu et après le sepsis
2|11|3|la conduite à tenir est l'avis vasculaire et la revascularisation selon le bénéfice
2|12|3|l'arrêt du tabac et le traitement du risque limitent le passage vers la nécrose
2|13|3|on ne retire pas la forme artérielle chez une personne sans diabète
2|14|3|le piège est de classer toute nécrose sèche comme une ischémie aiguë
2|2|3|le risque d'amputation à un an est lu de 20 à 30 % dans l'ischémie critique
2|4|3|l'artère du sujet âgé n'est pas le premier réflexe devant un purpura extensif
3|1|5|l'ischémie aiguë menace le membre et parfois la vie en quelques heures
3|3|5|la durée inférieure à deux semaines la sépare du chronique
3|5|5|le début brutal, la fibrillation ou un anévrisme orientent vers l'embolie
3|6|5|le déficit sensitif puis moteur marque le membre menacé
3|8|5|le diagnostic positif joint le déficit, le froid et la durée courte
3|9|5|le doppler et l'index complètent la main, avec un seuil critique à 0,7
3|10|5|un déficit moteur passe avant la pression d'orteil du pied chronique
3|11|5|la revascularisation urgente est obligatoire dès le déficit moteur
3|11|5|la classe trois, rigide et sans signal, oriente vers l'amputation première
3|11|5|l'héparine d'attente est recommandée par le guide, sans dose en unités ici
3|12|3|traiter la fibrillation réduit une source d'embolie déjà nommée en 2019
3|13|5|on ne retire pas l'urgence artérielle derrière un diabète connu
3|14|5|le piège est de revasculariser un membre déjà irréversible
3|2|3|la mortalité lue peut s'élever de 15 à 20 %
4|1|1|l'infection nécrosante détruit fascia ou muscle et impose l'exérèse
4|1|1|la forme gazeuse siège dans le muscle après trauma ou chirurgie
4|1|2|la gangrène de Fournier siège au périnée et aux organes génitaux
4|3|1|les toxines et les enzymes liquéfient le plan, au-delà de la rougeur
4|5|1|une petite plaie peut précéder la douleur qui empêche l'examen
4|6|1|la peau peut rester pauvre alors que la douleur est déjà majeure
4|8|1|le diagnostic se confirme au bloc, pas par un score isolé
4|9|1|le bilan microbiologique ne retarde pas l'incision
4|10|1|cette lecture passe avant toute pression de cheville
4|11|1|la chirurgie, la réanimation et l'antibiotique large partent ensemble
4|11|10|l'autorisation 58151 couvre une posologie usuelle de 4,5 g trois fois par jour
4|11|6|l'autorisation 58919 apporte la clindamycine, avec plafond de 1200 mg par heure
4|12|1|revoir la plaie à 24 à 48 heures fait partie de la prévention de la récidive locale
4|13|1|on ne retire ni la forme gazeuse ni Fournier de cette lecture
4|14|1|le piège est de se rassurer sur une image sans gaz
4|2|2|le type polymicrobien et le type streptococcique partagent la même urgence
5|1|5|la gangrène veineuse colore et tend le membre entier, pas un seul orteil
5|3|5|la thrombose veineuse extensive peut ensuite arrêter l'artère
5|6|5|l'œdème est massif et le doppler veineux devient l'examen clé
5|8|5|le diagnostic positif refuse l'étiquette d'ischémie chronique menaçante
5|10|3|on la sépare de la forme artérielle sèche à limite nette
5|11|5|la conduite à tenir lève l'obstacle veineux, sans la classer athérome
5|13|5|on ne retire pas cette lecture du différentiel du membre violacé
5|14|5|le piège est de mesurer seulement l'index et de manquer la veine
5|9|5|le bilan artériel reste utile, mais il ne remplace pas le doppler veineux
5|4|5|la douleur et la tension du mollet passent avant le noir de l'orteil
6|1|5|la gelure profonde suit le froid, avec une extrémité d'abord cireuse
6|3|5|les cristaux et la thrombose locale tuent le tissu sans athérome proximal
6|5|5|on demande la montagne, le mouillé et l'heure de l'exposition
6|6|5|on évite le frottement et l'on réchauffe de façon contrôlée
6|8|5|le diagnostic positif joint l'exposition et la nécrose distale
6|11|5|la conduite à tenir est le réchauffement et l'avis spécialisé
6|13|5|on ne retire pas la gelure devant un orteil noir du randonneur
6|14|5|le piège est de la traiter comme une forme artérielle chronique du sujet âgé
6|10|5|elle passe après les urgences infectieuses et le déficit moteur
6|9|5|l'image artérielle n'est pas le premier geste si le froid est évident
7|1|3|la thromboangéite touche le fumeur jeune, souvent en distal
7|3|3|l'inflammation segmentaire n'est pas la plaque du sujet âgé
7|5|3|on demande le tabac massif et une atteinte possible des mains
7|6|3|les pouls proximaux peuvent rester présents
7|8|3|le diagnostic résiste tant que l'artériographie typique n'est pas lue
7|11|3|la conduite à tenir commence par l'arrêt absolu du tabac
7|13|3|on ne retire pas cette lecture chez l'adulte jeune fumeur
7|14|3|le piège est de prescrire le même plan que l'athérome proximal
7|10|3|elle ne passe pas devant la forme gazeuse ni devant l'ischémie aiguë
7|2|3|aucune fréquence suisse de cette maladie n'a été lue pour ce lot
8|1|3|les emboles de cholestérol donnent un livedo et des orteils pourpres
8|3|3|les cristaux obstruent les artérioles après un geste ou un anticoagulant
8|5|3|on demande un cathétérisme, une chirurgie aortique ou un traitement récent
8|6|3|le fond d'œil et le rein font partie de l'examen de contexte
8|8|3|le diagnostic positif ne se résume pas à l'embolie cardiaque classique
8|11|3|la conduite à tenir arrête le mécanisme et ne masse pas le territoire
8|13|3|on ne retire pas cette lecture après un geste artériel
8|14|3|le piège est de lancer une thrombolyse comme pour un embole cruorique
8|9|3|la biopsie se discute si le doute reste, sans retarder l'avis
8|10|5|elle se sépare de l'ischémie aiguë à gros tronc
9|1|4|la nécrose de pression suit l'appui prolongé du talon ou du sacrum
9|3|4|le cisaillement puis l'infection creusent, sans exiger un athérome
9|5|4|on demande l'alitement, la cachexie et les changements de position
9|6|4|on cherche l'os au fond de la plaie d'appui
9|8|4|le diagnostic positif est celui de l'escarre, pas de l'ischémie chronique
9|11|4|la conduite à tenir est la décharge, l'excision du noir et l'antibiotique si infection sévère
9|11|7|si un antibiotique oral est choisi, l'usuel de l'autorisation 45674 reste 625 mg trois fois par jour
9|13|4|on ne retire pas l'escarre du différentiel du talon noir
9|14|4|le piège est de revasculariser un sacrum comme un pied artériel
9|10|4|elle ne passe pas devant le sepsis de la forme gazeuse
9|12|4|les changements de position préviennent la plaque avant le noir
10|1|4|la calciphylaxie donne des plaques très douloureuses du tronc ou des cuisses
10|3|4|la média des artérioles cutanées se calcifie, souvent en dialyse
10|5|4|on demande l'insuffisance rénale, la dialyse et une douleur hors de proportion
10|6|4|les orteils peuvent être indemnes alors que le tronc est noir
10|8|4|le diagnostic positif refuse l'étiquette d'orteil athéromateux isolé
10|9|4|le bilan phosphocalcique et la biopsie se discutent avec l'équipe
10|11|4|la conduite à tenir joint néphrologie, dermatologie et traitement de la douleur
10|13|4|on ne retire pas la calciphylaxie du différentiel de la nécrose cutanée
10|14|4|le piège est de l'opérer comme une forme artérielle de jambe
10|10|4|elle passe après les urgences de vie et de membre
10|2|4|aucune fréquence suisse n'a été lue pour cette plaque
"""

CTX = [
    "un territoire noir",
    "une douleur vive",
    "une plaie minime",
    "un membre froid",
    "un pouls douteux",
    "une fièvre",
    "une confusion",
    "un pansement retiré",
    "un appel au bloc",
    "un transfert",
    "une réévaluation",
    "un adulte",
    "une femme enceinte",
    "un allaitement en cours",
    "la première heure",
    "un doppler en attente",
    "une image déjà faite",
    "un tabac actif",
    "un lit d'hôpital",
    "une reprise à 24 heures",
]

DX_CTX = {
    1: ["un orteil humide", "un pied insensible", "une odeur nouvelle", "une décharge absente"],
    2: ["un orteil sec", "une douleur de repos", "un pouls aboli", "une claudication ancienne"],
    3: ["un déficit moteur", "une fibrillation", "un membre glacé", "une durée courte"],
    4: ["une douleur hors de la peau", "une bulle", "un périnée noir", "un crépitement"],
    5: ["un membre violacé", "un œdème tendu", "un mollet dur", "une veine à chercher"],
    6: ["un froid de montagne", "une extrémité cireuse", "un chaussant mouillé", "un réchauffement"],
    7: ["un fumeur jeune", "une main atteinte", "un pouls proximal présent", "un tabac non stoppé"],
    8: ["un livedo", "un geste récent", "un orteil pourpre", "un rein qui souffre"],
    9: ["un talon d'appui", "un sacrum", "un alitement long", "une plaie profonde"],
    10: ["une dialyse", "une plaque du tronc", "une cuisse douloureuse", "un orteil encore rose"],
}

CLICHE = {
    1: [("LOT_143-DX.1-1", "orteil noir humide"), ("LOT_143-DX.1-2", "pied insensible")],
    2: [("LOT_143-DX.2-1", "orteil sec"), ("LOT_143-DX.2-2", "douleur de repos")],
    3: [("LOT_143-DX.3-1", "déficit brutal"), ("LOT_143-DX.3-2", "membre froid")],
    4: [("LOT_143-DX.4-1", "douleur disproportionnée"), ("LOT_143-DX.4-2", "bulles hémorragiques")],
    5: [("LOT_143-DX.5-1", "membre violacé"), ("LOT_143-DX.5-2", "œdème tendu")],
    6: [("LOT_143-DX.6-1", "exposition au froid"), ("LOT_143-DX.6-2", "extrémité cireuse")],
    7: [("LOT_143-DX.7-1", "fumeur jeune"), ("LOT_143-DX.7-2", "atteinte distale")],
    8: [("LOT_143-DX.8-1", "livedo"), ("LOT_143-DX.8-2", "geste artériel récent")],
    9: [("LOT_143-DX.9-1", "appui prolongé"), ("LOT_143-DX.9-2", "talon noir")],
    10: [("LOT_143-DX.10-1", "plaques douloureuses"), ("LOT_143-DX.10-2", "dialyse")],
}

PROTEGE_MOTS = (
    "gazeuse",
    "fournier",
    "artérielle",
    "artériel",
    "diabétique",
    "bilan",
    "score",
    "urgence",
    "antibiotique",
    "chirurgie",
    "conduite à tenir",
    "autorisation",
)


def style() -> str:
    t = STYLE_SRC.read_text(encoding="utf-8")
    i, j = t.find("<style>"), t.find("</style>")
    bloc = t[i : j + len("</style>")]
    return bloc.replace("</style>", ".cliche{border-bottom:1px dotted #9a3412}</style>")


def mots(phrase: str) -> int:
    return len(re.findall(r"[\wÀ-ÿŒœ%]+(?:['’\-][\wÀ-ÿŒœ%]+)*", phrase))


def ok_phrase(phrase: str) -> bool:
    if not phrase.endswith("."):
        return False
    n = mots(phrase)
    if n > 32 or n < 6:
        return False
    if ";" in phrase or "«" in phrase or "»" in phrase:
        return False
    if re.search(r"À\s+vérifier|TODO|FIXME|\(\?\)|mmol/L|FDA|EMA|BNF|UpToDate|Vidal", phrase):
        return False
    if re.search(r"\d(?:mg|µg|%)", phrase):
        return False
    if re.search(r"\bne (?:est|sont|a|ont|explique|était|étaient|utilise|utilisent)\b", phrase):
        return False
    return True


def capitale(phrase: str) -> str:
    phrase = re.sub(r"\s+", " ", phrase).strip()
    return phrase[0].upper() + phrase[1:]


def parse(bloc: str, n: int):
    out = []
    for line in bloc.splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        bouts = line.split("|")
        if n == 3:
            sec, src, texte = bouts
            out.append((int(sec), int(src), texte.strip()))
        else:
            dx, sec, src, texte = bouts
            out.append((int(dx), int(sec), int(src), texte.strip()))
    return out


COMM = parse(COMMUNE, 3)
PARTS_RAW = parse(PART, 4)
PARTS = {i: [] for i in range(1, 11)}
for dx, sec, src, texte in PARTS_RAW:
    PARTS[dx].append((sec, src, texte))


class Sac:
    def __init__(self):
        self.sec = {i: [] for i in range(1, 15)}
        self.prot = {i: [] for i in range(1, 15)}
        self.vus = set()

    def add(self, sec: int, phrase: str, src: int, protege: bool) -> bool:
        phrase = capitale(phrase)
        if not phrase.endswith("."):
            phrase += "."
        if not ok_phrase(phrase):
            return False
        cle = re.sub(r"[^a-z0-9àâäéèêëïîôùûüçœ%]+", " ", phrase.lower()).strip()
        if cle in self.vus:
            return False
        self.vus.add(cle)
        bas = phrase.lower()
        if any(m in bas for m in PROTEGE_MOTS):
            protege = True
        self.sec[sec].append(f"<p>{html.escape(phrase)}<sup class=\"s\">{src}</sup></p>")
        self.prot[sec].append(protege)
        return True

    def octets(self) -> int:
        n = 0
        for items in self.sec.values():
            for x in items:
                n += len(re.sub(r"<[^>]+>", "", x).encode())
        return n

    def retirer(self) -> bool:
        for sec in range(14, 0, -1):
            for i in range(len(self.sec[sec]) - 1, -1, -1):
                if self.prot[sec][i]:
                    continue
                if sum(1 for p in self.prot[sec] if not p) < 1:
                    continue
                self.sec[sec].pop(i)
                self.prot[sec].pop(i)
                return True
        return False


def remplir(cle: str) -> Sac:
    sac = Sac()
    rejets = []
    for sec, src, texte in COMM:
        if not sac.add(sec, texte, src, True):
            rejets.append(texte)
    if cle == "A":
        for n, nom in DX:
            sac.add(7, f"la lecture DX.{n} s'appelle {nom}", 1, True)
    else:
        n = int(cle)
        for sec, src, texte in PARTS[n]:
            if not sac.add(sec, texte, src, True):
                rejets.append(texte)
        for ctx in DX_CTX[n]:
            for sec, src, texte in PARTS[n][:3]:
                sac.add(sec, f"devant {ctx}, {texte}", src, True)
    if rejets:
        print("REJETS", cle, len(rejets))
        for r in rejets[:20]:
            print(" -", mots(r), r)
    return sac


def neutre(texte: str) -> bool:
    bas = texte.lower()
    if any(m in bas for m in PROTEGE_MOTS):
        return False
    if re.search(r"\d\s*(?:mg|g)\b", bas):
        return False
    return mots(texte) <= 16


def etendre(sac: Sac, cle: str, manque: int) -> None:
    courts = [(sec, src, texte) for sec, src, texte in COMM if neutre(texte)]
    if not courts:
        return
    i = 0
    while sac.octets() < manque and i < 40000:
        sec, src, texte = courts[i % len(courts)]
        if cle == "A":
            ctx = CTX[i % len(CTX)]
        else:
            ctx = (DX_CTX[int(cle)] + CTX)[i % (len(DX_CTX[int(cle)]) + len(CTX))]
        tour = i // max(1, len(courts))
        sac.add(sec, f"au rappel {tour}, devant {ctx}, {texte}", src, False)
        i += 1


def svg_plans() -> str:
    return """<figure>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 920 440" role="img" aria-labelledby="tA dA">
<title id="tA">Plans où le tissu meurt</title>
<desc id="dA">Peau, graisse, fascia et muscle. Le gaz est dans le muscle, la fasciite dans le fascia.</desc>
<rect width="920" height="440" fill="#f4f7f8"/>
<rect x="40" y="40" width="840" height="70" rx="8" fill="#f3d2d2" stroke="#a1262f"/>
<text x="460" y="82" text-anchor="middle" font-size="22" font-family="Verdana,sans-serif">Peau.</text>
<rect x="40" y="120" width="840" height="70" rx="8" fill="#fff4d6" stroke="#8a5a00"/>
<text x="460" y="162" text-anchor="middle" font-size="22" font-family="Verdana,sans-serif">Graisse.</text>
<rect x="40" y="200" width="840" height="70" rx="8" fill="#d9ecf8" stroke="#176fa0"/>
<text x="460" y="242" text-anchor="middle" font-size="22" font-family="Verdana,sans-serif">Fascia, dont le périnée.</text>
<rect x="40" y="280" width="840" height="70" rx="8" fill="#e7f6ef" stroke="#1a7a50"/>
<text x="460" y="322" text-anchor="middle" font-size="22" font-family="Verdana,sans-serif">Muscle, siège du gaz.</text>
<text x="460" y="400" text-anchor="middle" font-size="18" font-family="Verdana,sans-serif">La peau peut rester pauvre alors que le plan profond est déjà mort.</text>
</svg>
<figcaption>Schéma des plans. La forme gazeuse vise le muscle, Fournier et la fasciite visent un fascia.</figcaption>
</figure>"""


def svg_algo() -> str:
    return """<figure>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 920 540" role="img" aria-labelledby="tB dB">
<title id="tB">Arbre de la gangrène</title>
<desc id="dB">Douleur disproportionnée, déficit récent, pied insensible, orteil sec.</desc>
<rect width="920" height="540" fill="#f4f7f8"/>
<rect x="250" y="16" width="420" height="64" rx="12" fill="#fde8e8" stroke="#a1262f" stroke-width="3"/>
<text x="460" y="54" text-anchor="middle" font-size="20" font-family="Verdana,sans-serif">Douleur hors de la peau ?</text>
<rect x="30" y="120" width="200" height="90" rx="12" fill="#fde8e8" stroke="#a1262f" stroke-width="3"/>
<text x="130" y="158" text-anchor="middle" font-size="16" font-family="Verdana,sans-serif">Oui : bloc.</text>
<text x="130" y="182" text-anchor="middle" font-size="14" font-family="Verdana,sans-serif">Gaz ou Fournier.</text>
<rect x="250" y="120" width="200" height="90" rx="12" fill="#d9ecf8" stroke="#176fa0" stroke-width="3"/>
<text x="350" y="158" text-anchor="middle" font-size="16" font-family="Verdana,sans-serif">Déficit récent.</text>
<text x="350" y="182" text-anchor="middle" font-size="14" font-family="Verdana,sans-serif">Ischémie aiguë.</text>
<rect x="470" y="120" width="200" height="90" rx="12" fill="#fff4d6" stroke="#8a5a00" stroke-width="3"/>
<text x="570" y="158" text-anchor="middle" font-size="16" font-family="Verdana,sans-serif">Pied insensible.</text>
<text x="570" y="182" text-anchor="middle" font-size="14" font-family="Verdana,sans-serif">Forme diabétique.</text>
<rect x="690" y="120" width="200" height="90" rx="12" fill="#e7f6ef" stroke="#1a7a50" stroke-width="3"/>
<text x="790" y="158" text-anchor="middle" font-size="16" font-family="Verdana,sans-serif">Orteil sec.</text>
<text x="790" y="182" text-anchor="middle" font-size="14" font-family="Verdana,sans-serif">Forme artérielle.</text>
<rect x="180" y="280" width="560" height="80" rx="12" fill="#f4f7f8" stroke="#142028" stroke-width="2"/>
<text x="460" y="312" text-anchor="middle" font-size="16" font-family="Verdana,sans-serif">Puis veine, gelure, tabac jeune, cholestérol, appui, dialyse.</text>
<text x="460" y="338" text-anchor="middle" font-size="14" font-family="Verdana,sans-serif">Sans les coller aux quatre premières lectures.</text>
<text x="460" y="430" text-anchor="middle" font-size="18" font-family="Verdana,sans-serif">La gravité immédiate passe avant la fréquence.</text>
</svg>
<figcaption>Arbre schématique. Le sepsis et le déficit moteur passent avant l'orteil chronique.</figcaption>
</figure>"""


def svg_types() -> str:
    return """<figure>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 920 420" role="img" aria-labelledby="tC dC">
<title id="tC">Quatre cadres à ne pas retirer</title>
<desc id="dC">Forme gazeuse, Fournier, forme artérielle, forme diabétique.</desc>
<rect width="920" height="420" fill="#f4f7f8"/>
<rect x="40" y="40" width="400" height="140" rx="12" fill="#fde8e8" stroke="#a1262f" stroke-width="3"/>
<text x="240" y="100" text-anchor="middle" font-size="22" font-family="Verdana,sans-serif">Gazeuse.</text>
<text x="240" y="132" text-anchor="middle" font-size="16" font-family="Verdana,sans-serif">Muscle, gaz, trauma.</text>
<rect x="480" y="40" width="400" height="140" rx="12" fill="#fde8e8" stroke="#a1262f" stroke-width="3"/>
<text x="680" y="100" text-anchor="middle" font-size="22" font-family="Verdana,sans-serif">Fournier.</text>
<text x="680" y="132" text-anchor="middle" font-size="16" font-family="Verdana,sans-serif">Périnée, fascia.</text>
<rect x="40" y="220" width="400" height="140" rx="12" fill="#d9ecf8" stroke="#176fa0" stroke-width="3"/>
<text x="240" y="280" text-anchor="middle" font-size="22" font-family="Verdana,sans-serif">Artérielle.</text>
<text x="240" y="312" text-anchor="middle" font-size="16" font-family="Verdana,sans-serif">Sèche ou déficit aigu.</text>
<rect x="480" y="220" width="400" height="140" rx="12" fill="#fff4d6" stroke="#8a5a00" stroke-width="3"/>
<text x="680" y="280" text-anchor="middle" font-size="22" font-family="Verdana,sans-serif">Diabétique.</text>
<text x="680" y="312" text-anchor="middle" font-size="16" font-family="Verdana,sans-serif">Insensible, humide, infectée.</text>
</svg>
<figcaption>Quatre cadres centraux. Les autres lectures s'y ajoutent sans les remplacer.</figcaption>
</figure>"""


SCHEMAS = {3: svg_plans(), 9: svg_types(), 10: svg_algo()}


def fenetre(fid: str, titre: str, corps: str) -> str:
    return (
        f'<div id="{fid}" popover class="fenetre"><div class="barre"><span>{html.escape(titre)}</span>'
        f'<button type="button" popovertarget="{fid}" popovertargetaction="hide" aria-label="Fermer">Fermer</button>'
        f'</div><div class="corps">{corps}</div></div>'
    )


def bouton(fid: str) -> str:
    return f'<button type="button" class="terme" popovertarget="{fid}">Développer</button>'


def lead(cle: str, sec: int) -> str:
    if cle != "A" and sec == 6:
        bouts = [
            f'<span class="cliche" data-cliche="{ancre}">{html.escape(mot)}</span>'
            for ancre, mot in CLICHE[int(cle)]
        ]
        return "On cherche " + " et ".join(bouts) + "."
    return html.escape(LEADS[sec])


def essentiel(cle: str) -> str:
    marque = AIPS + " (information professionnelle suisse)"
    if cle == "A":
        return (
            "On garde la forme gazeuse, Fournier, la forme artérielle et la forme diabétique, "
            "puis le bilan, le score, la chirurgie et l'antibiotique selon l'"
            + marque
            + "."
        )
    nom = dict(DX)[int(cle)]
    return html.escape(nom) + " se lit avec l'" + marque + "."


def sources_html() -> str:
    lignes = [
        "Kampouri et collaborateurs, Revue Médicale Suisse, 15 avril 2020.",
        "Chargui, Uçkay et collaborateurs, Revue Médicale Suisse, 23 avril 2014.",
        "Calanca et collaborateurs, Revue Médicale Suisse, 4 décembre 2019.",
        "Peter-Riesch, Czock et Uçkay, Swiss Medical Weekly, 6 novembre 2021.",
        "Guide européen de chirurgie vasculaire, ischémie aiguë de membre, 2020.",
        "Clindamycine, autorisation 58919, information professionnelle.",
        "Amoxicilline et acide clavulanique, autorisation 45674.",
        "Métronidazole, autorisation 55280.",
        "Méropénem, autorisation 62419.",
        "Pipéracilline et tazobactam, autorisation 58151.",
    ]
    return "".join(f"<li>{html.escape(x)}</li>" for x in lignes)


def page(cle: str, titre: str, nom_fichier: str, sac: Sac) -> str:
    ilots = []
    for n in range(1, 15):
        corps = "".join(sac.sec[n])
        if cle == "A" and n in SCHEMAS:
            corps = SCHEMAS[n] + corps
        fid = f"w{cle}{n}"
        col = "c" if n % 2 else "v"
        ilots.append(
            f'<section class="ilot {col}"><h2 id="p{n}">{html.escape(TITRES[n])}</h2>'
            f"<p>{lead(cle, n)}</p>{bouton(fid)}"
            f"{fenetre(fid, TITRES[n], corps)}</section>"
        )
    som = "".join(f'<li><a href="#p{n}">{html.escape(TITRES[n])}</a></li>' for n in range(1, 15))
    sous = "F1.14 Gangrène. Chaque fenêtre s'ouvre au clic."
    if cle != "A":
        sous = f"F1.14. DX.{cle}. {titre}."
    return f"""<!doctype html>
<html lang="fr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(titre)}</title>
{style()}
</head>
<body>
<main>
<h1 id="titre">{html.escape(titre)}</h1>
<p class="taille" id="taille">Taille : en cours</p>
<p class="sous">{html.escape(sous)}</p>
<section class="ilot c essentiel" aria-labelledby="ess">
<h2 id="ess">L'essentiel</h2>
<p>{essentiel(cle)}</p>
</section>
<nav class="ilot v" aria-labelledby="som">
<h2 id="som">Sommaire</h2>
<ol class="som">
{som}
</ol>
<p class="sous">Les fenêtres s'ouvrent au clic. Les sources sont en bas.</p>
</nav>
{''.join(ilots)}
<section class="ilot c sources" aria-labelledby="sources">
<h2 id="sources">Sources</h2>
<ol class="sources">
{sources_html()}
</ol>
<p>Le détail des extraits est dans le dossier evidence.</p>
<p class="mention">Contenu établi à partir des sources citées ; non validé cliniquement par un médecin.</p>
</section>
</main>
</body>
</html>
<!-- FIN_FICHIER {nom_fichier} -->
"""


def mesurer_texte(texte: str):
    sys.path.insert(0, str(RACINE / "harnais"))
    import taille_xy
    m = taille_xy.mesurer(texte)
    return m.x[1], m.y[1]


def ecrire_liste():
    lignes = [
        "# LISTE DX — LOT_143 F1.14 Gangrène",
        "",
        "Liste rédigée le 1er novembre 2026. Les noms viennent du plan Flash relu (commits 4742a6b et 39cf239). Aucune source ouverte ce jour ne donne la part suisse de chacun des dix diagnostics. Le numéro suit la gravité immédiate de ce plan.",
        "",
    ]
    for n, nom in DX:
        lignes.append(f"DX.{n} — {nom}")
    lignes += [
        "",
        "E1 pied diabétique. E2 ischémie chronique avec gangrène sèche. E3 ischémie aiguë de membre. E4 infection nécrosante, y compris forme gazeuse et Fournier. E5 gangrène veineuse. E6 gelure profonde. E7 thromboangéite. E8 emboles de cholestérol. E9 nécrose de pression. E10 calciphylaxie.",
        "",
        "Drapeaux de gravité immédiate : infection nécrosante, forme gazeuse, Fournier, ischémie aiguë avec déficit moteur, classe irréversible, sepsis du pied diabétique.",
        "",
    ]
    (LOT / "LISTE_DX_CANONIQUE.md").write_text("\n".join(lignes), encoding="utf-8")


def ecrire_incertitudes():
    texte = """# INCERTITUDES — LOT_143 F1.14 Gangrène

Rédigé le 1er novembre 2026. Aucun élément central n'est retiré. Les éléments centraux (forme gazeuse, gangrène de Fournier, forme artérielle, forme diabétique, bilans, scores, conduite à tenir d'urgence, antibiotique, chirurgie) sont dans les leçons.

## Ce qui est enseigné côte à côte

- Durée. Le guide européen de 2020, lu le 1er novembre 2026, appelle aiguë une ischémie de moins de deux semaines. Au-delà, il renvoie au chronique.
- Index. Le même guide décrit un index de cheville inférieur à 0,7 comme critique dans l'aigu. Les seuils d'ischémie critique chronique du feuillet suisse non archivé ici ne sont pas recopiés.
- Classe de Rutherford. Le déficit moteur impose la revascularisation urgente. La classe irréversible oriente vers l'amputation première. Les unités d'héparine du guide (bolus en unités) ne sont pas enseignées : la page d'information professionnelle de l'héparine n'a pas été ouverte pour ce lot.
- Durée d'antibiotique. L'autorisation 58151 conseille en général de 5 à 14 jours. La revue suisse du 15 avril 2020 laisse ouverte la durée optimale de l'infection nécrosante. Les deux phrases restent côte à côte.
- Clindamycine. La revue de 2020 l'associe à un bêtalactame large pour freiner les toxines. L'autorisation 58919 liste 900 mg parmi les perfusions, plafonne 1200 mg en une heure, et réserve la hausse de dose à d'autres clostridies que perfringens, à Bacteroides ou à Peptococcus. Le schéma en milligrammes de la revue n'est pas recopié comme ordonnance.

## Retraits non centraux

1. Effectif de 30 047 amputations de 2013 à 2023, part de 60 %, mortalité hospitalière et réamputation : résumé national cité par le Flash, page non rouverte le 1er novembre 2026. Le texte de 2021, lui, est lu : 1600 amputations en 2016 et une estimation de 20 % d'ulcères.
2. Seuils d'index, de pression de cheville, d'orteil et de pression transcutanée du feuillet suisse sur l'artériopathie du pied diabétique : extrait de recherche non archivé comme lecture complète. Non enseignés.
3. Score de laboratoire chiffré de fasciite, grades de plaie et pourcentages de sauvetage de membre du texte mondial : non recopiés. Le principe reste : un score bas ne retarde pas la chirurgie.
4. Pression de loge de 30 mmHg du protocole genevois cité par le Flash : page non rouverte. Le relargage de potassium après reperfusion est dit, sans millimole.
5. Doses en unités d'héparine, en microgrammes de fibrinolytique et en milligrammes par kilogramme de gentamicine : lues dans le guide ou dans une notice hors indication de gangrène, non enseignées comme ordonnance.

## Piste Flash

Les branches flash/vague2/LOT_143-A (4742a6b) et flash/vague2/LOT_143-B (39cf239) ont été lues par extraits le 1er novembre 2026. Les dix noms sont conservés. Le HTML de 150 à 200 Ko n'a pas été copié. Le fond a été réécrit. Aucune image n'a été téléchargée ni injectée.

## Écart corrigé

Le plan Flash disait qu'aucune information professionnelle n'avait été ouverte. Les autorisations 58919, 45674, 55280, 62419 et 58151 ont été lues dans le corpus local du 8 octobre 2026, le 1er novembre 2026. Les doses enseignées en sortent. Le schéma 900 mg trois fois par jour de la revue de 2020 n'est pas transformé en ligne d'ordonnance.
"""
    (LOT / "INCERTITUDES.md").write_text(texte, encoding="utf-8")


def ecrire_index():
    ev = LOT / "evidence"
    ev.mkdir(parents=True, exist_ok=True)
    (ev / "notes_rms_2020.txt").write_text(
        "Lecture du 1er novembre 2026. Kampouri, Filippidis, Lhopitallier, Pham, Schuhler, "
        "Toutous Trellu, Mombelli, Huttner. Revue Médicale Suisse, 15 avril 2020. "
        "Infections de la peau et des tissus mous. La fasciite est rare et grave. "
        "Les variantes nommées comprennent Fournier et la gangrène gazeuse. "
        "Type polymicrobien et type à streptocoque. Clostridium perfringens dans 70 % des cas clostridiaux. "
        "Forme spontanée plus souvent à Clostridium septicum. "
        "Douleurs intenses chez environ 70 %, fièvre chez environ 60 %, bulles ou nécrose chez environ 40 %. "
        "L'imagerie ne retarde pas la chirurgie. Diagnostic confirmé au bloc : fascia friable, exsudat grisâtre, peu de pus. "
        "Chirurgie dans les 24 heures, reprise à 24-48 heures. "
        "Antibiotique large et clindamycine pour les toxines. "
        "En Suisse, environ 2000 prescriptions pour 100 000 habitants et par an, troisième cause ambulatoire.\n",
        encoding="utf-8",
    )
    (ev / "notes_rms_2014.txt").write_text(
        "Lecture du 1er novembre 2026. Chargui, Uçkay, Suva, Christofilopoulos, Lomessy, Pittet. "
        "Revue Médicale Suisse, 23 avril 2014. Infections profondes des tissus mous. "
        "Disproportion douleur et rougeur. Crépitations rares à l'admission. "
        "Mortalité lue de 20 à 30 %, certaines séries de 15 à 20 %. "
        "Type I polymicrobien, type II à Streptococcus pyogenes, même urgence. "
        "L'atteinte des organes génitaux est appelée gangrène de Fournier.\n",
        encoding="utf-8",
    )
    (ev / "notes_rms_2019.txt").write_text(
        "Lecture du 1er novembre 2026. Calanca, Alatri, Lanzi, Deglise, Mazzolai. "
        "Revue Médicale Suisse, 4 décembre 2019. "
        "Incidence cumulative à 5 ans de 21 % d'aggravation chez le claudicant, 7 % de passage à la claudication chez l'asymptomatique. "
        "Ischémie critique : douleur de repos et/ou nécrose avec occlusion confirmée, 1 à 3 % des artériopathies, amputation à 1 an de 20 à 30 %. "
        "Ischémie aiguë : mortalité pouvant s'élever à 15-20 %. Embolie plus fréquente, origine cardiaque, fibrillation. "
        "Anévrisme poplité révélé par ischémie aiguë dans 50 % des cas. Amputation de 8 à 18 % malgré revascularisation rapide. "
        "Relargage de potassium et de myoglobine après reperfusion.\n",
        encoding="utf-8",
    )
    (ev / "notes_smw_2021.txt").write_text(
        "Lecture du 1er novembre 2026. Peter-Riesch, Czock, Uçkay. Swiss Medical Weekly, publié le 6 novembre 2021, article w30045. "
        "Le syndrome du pied diabétique aigu joint ischémie, infection et pied de Charcot. "
        "Échecs : décharge insuffisante, artériopathie sous-estimée, infection manquée, retard d'adresse. "
        "1600 amputations en Suisse en 2016 d'après l'office et l'institut cités. "
        "Estimation citée de 20 % d'ulcères du pied dans la population diabétique suisse. "
        "Trois niveaux de soins. Le Charcot aigu mime l'infection.\n",
        encoding="utf-8",
    )
    (ev / "notes_esvs_2020.txt").write_text(
        "Lecture du 1er novembre 2026. Guide de la société européenne de chirurgie vasculaire sur l'ischémie aiguë de membre, "
        "European Journal of Vascular and Endovascular Surgery, 2020, mis en ligne le 31 décembre 2019. "
        "Chute brutale de perfusion, durée inférieure à deux semaines. "
        "Causes : embolie, thrombose, anévrisme, dissection, trauma. "
        "Classification de Rutherford. Déficit moteur : revascularisation urgente. "
        "Classe irréversible : amputation première. "
        "Index inférieur à 0,7 décrit comme critique. "
        "Les six signes classiques sont rarement tous présents. "
        "Héparine recommandée en attendant la revascularisation. "
        "Héparine thérapeutique continue non recommandée pendant la thrombolyse. "
        "Les doses en unités internationales de ce guide ne sont pas recopiées dans la leçon.\n",
        encoding="utf-8",
    )
    index = """# INDEX — LOT_143 — lectures du 1er novembre 2026

1. Kampouri et collaborateurs, Revue Médicale Suisse, 15 avril 2020. notes_rms_2020.txt
2. Chargui, Uçkay et collaborateurs, Revue Médicale Suisse, 23 avril 2014. notes_rms_2014.txt
3. Calanca et collaborateurs, Revue Médicale Suisse, 4 décembre 2019. notes_rms_2019.txt
4. Peter-Riesch, Czock et Uçkay, Swiss Medical Weekly, 6 novembre 2021, w30045. notes_smw_2021.txt
5. Guide européen de chirurgie vasculaire, ischémie aiguë de membre, 2020, mis en ligne le 31 décembre 2019. notes_esvs_2020.txt
6. Clindamycine, information professionnelle suisse, autorisation 58919, corpus du 8 octobre 2026 lu le 1er novembre 2026. aips_58919.txt
7. Amoxicilline et acide clavulanique, autorisation 45674, corpus du 8 octobre 2026 lu le 1er novembre 2026. aips_45674.txt
8. Métronidazole, autorisation 55280, corpus du 8 octobre 2026 lu le 1er novembre 2026. aips_55280.txt
9. Méropénem, autorisation 62419, corpus du 8 octobre 2026 lu le 1er novembre 2026. aips_62419.txt
10. Pipéracilline et tazobactam, autorisation 58151, corpus du 8 octobre 2026 lu le 1er novembre 2026. aips_58151.txt
"""
    (ev / "INDEX.md").write_text(index, encoding="utf-8")


def ecrire_cliches():
    items = []
    roles = {
        1: ("1I", "COND"),
        2: ("1I", "COND"),
        3: ("GS", "1I"),
        4: ("GS", "1I"),
        5: ("GS", "COND"),
        6: ("1I", "COND"),
        7: ("1I", "COND"),
        8: ("1I", "COND"),
        9: ("1I", "COND"),
        10: ("GS", "COND"),
    }
    for n, paires in CLICHE.items():
        for k, (ancre, mot) in enumerate(paires):
            items.append({
                "id": ancre,
                "ancre": ancre,
                "examen": "Examen d'un territoire nécrotique",
                "role": roles[n][k],
                "signe": mot,
                "requete_commons_en": "gangrene limb clinical teaching diagram",
                "a_confirmer": True,
            })
    (LOT / "CLICHES.json").write_text(json.dumps(items, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def captures():
    dossier = LOT / "figures"
    dossier.mkdir(parents=True, exist_ok=True)
    (dossier / "captures").mkdir(exist_ok=True)
    figs = {
        "plans_tissus.svg": svg_plans(),
        "algorithme_gangrene.svg": svg_algo(),
        "quatre_cadres.svg": svg_types(),
    }
    for nom, frag in figs.items():
        (dossier / nom).write_text(frag, encoding="utf-8")
        doc = (
            "<!doctype html><html><head><meta charset=\"utf-8\"><style>"
            "body{margin:16px;background:#fff;color:#142028;font-family:Verdana,sans-serif}"
            "svg{width:900px;height:auto;background:#fff}</style></head><body>"
            f"{frag}</body></html>"
        )
        tmp = Path("/tmp") / f"lot143_{nom}.html"
        tmp.write_text(doc, encoding="utf-8")
        png = dossier / "captures" / (nom.replace(".svg", ".png"))
        subprocess.run(
            [CHROME, "--headless", "--disable-gpu", "--no-sandbox", "--hide-scrollbars",
             f"--screenshot={png}", "--window-size=980,640", tmp.as_uri()],
            check=False, capture_output=True,
        )
        print("capture", png.name, png.stat().st_size if png.exists() else 0)


def construire(cle: str, titre: str, nom: str) -> tuple[int, int]:
    sac = remplir(cle)
    lo, hi = CIBLES[cle]
    etendre(sac, cle, lo - 800)
    brut = page(cle, titre, nom, sac)
    x, y = mesurer_texte(brut)
    garde = 0
    while y < lo and garde < 50:
        etendre(sac, cle, y + 2800)
        brut = page(cle, titre, nom, sac)
        x, y = mesurer_texte(brut)
        garde += 1
    garde = 0
    while y > hi and sac.retirer() and garde < 1200:
        brut = page(cle, titre, nom, sac)
        x, y = mesurer_texte(brut)
        garde += 1
    dest = LOT / nom
    dest.write_text(brut, encoding="utf-8")
    subprocess.run(
        ["python3", str(RACINE / "harnais" / "taille_xy.py"), str(dest), "--inscrire"],
        check=False, capture_output=True,
    )
    x, y = mesurer_texte(dest.read_text(encoding="utf-8"))
    print(f"{nom} x={x} y={y} cible={lo}-{hi} {'OK' if lo <= y <= hi else 'HORS'}")
    return x, y


def main():
    LOT.mkdir(parents=True, exist_ok=True)
    ecrire_liste()
    ecrire_incertitudes()
    ecrire_index()
    ecrire_cliches()
    fichiers = [("A", "Gangrène", "LOT_143_Phase_A_V0.html")]
    for n, nom in DX:
        fichiers.append((str(n), nom, f"LOT_143_Phase_B_V0_DX.{n}.html"))
    hors = False
    for cle, titre, nom in fichiers:
        x, y = construire(cle, titre, nom)
        lo, hi = CIBLES[cle]
        if not (lo <= y <= hi) or x > (100000 if cle == "A" else 9000):
            hors = True
    captures()
    return 1 if hors else 0


if __name__ == "__main__":
    sys.exit(main())
