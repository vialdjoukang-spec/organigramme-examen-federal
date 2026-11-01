# Phrases courtes. Chaque tuple : (point, texte, référence INDEX).
from __future__ import annotations

UG = "µg"


def vides():
    return {i: [] for i in range(1, 15)}


def charger():
    D = {0: vides()}
    for n in range(1, 11):
        D[n] = vides()
    cas = {}
    leads = {0: {}, **{n: {} for n in range(1, 11)}}

    def a(n, pt, t, r):
        D[n][pt].append((t, r))

    # ----- Phase A -----
    L = leads[0]
    L[1] = "Un problème d'accouchement se nomme, puis se classe, puis se traite."
    L[2] = "On ne cite un taux que s'il a une année."
    L[3] = "Le muscle, le placenta, le cordon et le bassin ne se mélangent pas."
    L[4] = "On sécurise la mère et le fœtus avant de discuter la voie."
    L[5] = "L'entretien cherche la cicatrice, le saignement et la douleur."
    L[6] = "L'examen regarde le col, le tracé, le sang et le placenta."
    L[7] = "Dix branches. On n'en ferme pas une par habitude."
    L[8] = "Le diagnostic positif cite le critère lu, pas une impression."
    L[9] = "On mesure le sang. On ne se fie pas au seul regard."
    L[10] = "L'arbre part du danger immédiat."
    L[11] = "La dose suisse est celle de l'information professionnelle."
    L[12] = "Prévenir, c'est l'utérotonique et la protection du périnée."
    L[13] = "Les classifications se disent entières."
    L[14] = "Le piège habituel est de rassurer trop tôt."

    a(0, 1, "Le motif réunit les complications du travail et de la naissance.", 3)
    a(0, 1, "Il ne décrit pas l'accouchement normal sans complication.", 3)
    a(0, 1, "Chaque branche a son critère. On ne les fond pas.", 2)
    a(0, 1, "La déchirure périnéale et la lésion du sphincter anal est la première branche.", 4)
    a(0, 1, "Son nom exact est Déchirure périnéale et lésion du sphincter anal.", 4)
    a(0, 1, "Le tracé cardiaque fœtal suspect ou pathologique est la deuxième.", 1)
    a(0, 1, "La stagnation de la dilatation ou de la descente est la troisième.", 3)
    a(0, 1, "L'hémorragie du post-partum par atonie est la quatrième.", 2)
    a(0, 1, "La rétention placentaire est la cinquième.", 3)
    a(0, 1, "La présentation du siège pendant le travail est la sixième.", 3)
    a(0, 1, "L'hématome rétroplacentaire pendant le travail est la septième.", 12)
    a(0, 1, "La dystocie des épaules est la huitième.", 13)
    a(0, 1, "La procidence du cordon est la neuvième.", 1)
    a(0, 1, "La rupture utérine est la dixième.", 5)

    a(0, 2, "L'incidence lue de l'hémorragie du post-partum est de 1 à 3 pour cent.", 2)
    a(0, 2, "Avec une mesure quantitative, le texte de 2022 parle d'environ 10 pour cent.", 2)
    a(0, 2, "La forme qui menace la vie est d'environ 2 pour 1 000 naissances.", 2)
    a(0, 2, "Ce 2 pour 1 000 est celui des pays à haut revenu, texte de 2022.", 2)
    a(0, 2, "L'incidence lue de la dystocie des épaules va de 0,58 à 0,70 pour cent.", 13)
    a(0, 2, "Ces bornes viennent des grandes séries citées en mars 2012.", 13)
    a(0, 2, "Le rang des autres branches est pédagogique quand le taux suisse n'est pas lu.", 3)
    a(0, 2, "On ne transforme pas une absence de taux en zéro.", 3)

    a(0, 3, "L'utérus se contracte par le fond, puis le col s'ouvre.", 5)
    a(0, 3, "L'[[AIPS]] 22114 dit que les récepteurs augmentent en fin de grossesse.", 5)
    a(0, 3, "L'effet intraveineux commence en moins d'une minute.", 5)
    a(0, 3, "L'effet intramusculaire commence en 2 à 4 minutes.", 5)
    a(0, 3, "Après injection intramusculaire, l'effet dure environ 30 à 60 minutes.", 5)
    a(0, 3, "Un bolus intraveineux rapide peut faire chuter la tension.", 5)
    a(0, 3, "Le placenta qui ne se décolle pas laisse saigner la zone d'insertion.", 2)
    a(0, 3, "Le cordon comprimé baisse les échanges avant que le pH ne soit lu.", 1)
    a(0, 3, "L'épaule antérieure bute sur la symphyse.", 13)
    a(0, 3, "L'information 67580 interdit Angusta sur une cicatrice utérine.", 10)

    a(0, 4, "D'abord les voix, le sang, le tracé, puis le geste.", 1)
    a(0, 4, "Un tracé pathologique ne attend pas la fin d'un protocole lent.", 1)
    a(0, 4, "Une hémorragie ne attend pas le laboratoire pour l'utérotonique.", 2)
    a(0, 4, "On classe la déchirure avant de suturer.", 4)
    a(0, 4, "On dit la dystocie des épaules à voix haute.", 14)
    a(0, 4, "On ne pousse pas sur le fond utérin.", 13)

    a(0, 5, "On demande la cicatrice, le nombre de fœtus et le terme.", 5)
    a(0, 5, "On demande un utérus déjà opéré, y compris une césarienne.", 10)
    a(0, 5, "Angusta est contre-indiqué sur une cicatrice utérine.", 10)
    a(0, 5, "On demande le groupe sanguin et les saignements déjà vus.", 2)
    a(0, 5, "On demande si la tête est née et si les épaules suivent.", 13)
    a(0, 5, "On demande une douleur continue, différente de la contraction.", 12)

    a(0, 6, "Le toucher dit la dilatation, la hauteur et la présentation.", 3)
    a(0, 6, "Le toucher rectal fait partie de l'examen après une voie basse.", 4)
    a(0, 6, "Le [[CTG]] se lit par ligne de base, variabilité et décélérations.", 1)
    a(0, 6, "Le sang se mesure. Le regard sous-estime.", 2)
    a(0, 6, "Un utérus de bois et une douleur continue orientent vers le décollement.", 12)
    a(0, 6, "La tête née qui ne tourne pas oriente vers les épaules.", 13)

    a(0, 7, "Branche saignement : atonie, déchirure, placenta, coagulation.", 2)
    a(0, 7, "Branche tracé : suspect, puis pathologique, puis cause réversible.", 1)
    a(0, 7, "Branche mécanique : stagnation, siège, épaules, procidence.", 3)
    a(0, 7, "Branche paroi : rupture sur cicatrice ou sur hypertonie.", 5)
    a(0, 7, "Deux branches peuvent être vraies ensemble.", 2)
    a(0, 7, "L'atonie n'exclut pas une déchirure cachée.", 2)

    a(0, 8, "On nomme la classe [[FIGO]] entière du tracé.", 1)
    a(0, 8, "On nomme le degré entier de la déchirure, de 1 à 4.", 4)
    a(0, 8, "On nomme le volume, ou l'index de choc, pour l'hémorragie.", 2)
    a(0, 8, "On nomme la manœuvre qui a libéré l'épaule.", 13)
    a(0, 8, "On ne dit pas normal un tracé qui a perdu un critère.", 1)

    a(0, 9, "Le [[CTG]] est l'examen du rythme pendant le travail.", 1)
    a(0, 9, "La pesée des compresses vaut mieux que l'estimation visuelle.", 2)
    a(0, 9, "Le laboratoire vient avec le choc, il ne le précède pas toujours.", 2)
    a(0, 9, "On regarde si le placenta est entier. Le sang se pèse.", 2)
    a(0, 9, "Le toucher rectal vérifie le sphincter avant et après la suture.", 4)

    a(0, 10, "Branche A. Tracé pathologique : cause réversible, puis naître.", 1)
    a(0, 10, "Branche B. Avant 5 cm, mère et fœtus bien : pas d'accélération de routine.", 3)
    a(0, 10, "Branche C. Saignement : mesurer, utérotonique, quatre causes.", 2)
    a(0, 10, "Branche D. Tête née, épaules bloquées : McRoberts, pas le fond utérin.", 13)
    a(0, 10, "Branche E. Cordon devant la présentation : relever, naître.", 1)
    a(0, 10, "Branche F. Cicatrice et douleur continue avec tracé mauvais : laparotomie.", 5)

    a(0, 11, "L'information 22114 règle l'oxytocine injectable. Le spray nasal est une autre voie.", 5)
    a(0, 11, "Le spray nasal est contre-indiqué pendant la grossesse et l'accouchement.", 5)
    a(0, 11, "Pour prévenir le saignement après voie basse, 5 U.I. en perfusion sur 5 minutes.", 5)
    a(0, 11, "L'alternative lue est 5-10 U.I. en intramusculaire.", 5)
    a(0, 11, "Après césarienne, 5 U.I. en perfusion sur 5 minutes, juste après l'enfant.", 5)
    a(0, 11, "L'[[OMS]] 2018 écrit 10 unités internationales. On ne l'échange pas avec la phrase suisse.", 3)
    a(0, 11, "Pabal, numéro 58079 : une seule injection de 100 " + UG + ".", 6)
    a(0, 11, "Méthergin, numéro 12730 : 0,2 mg en intramusculaire, voie recommandée.", 7)
    a(0, 11, "Nalador, numéro 43642, est le relais de l'atonie, pas le premier geste.", 8)
    a(0, 11, "L'acide tranexamique, numéro 70581 : 1 g en intraveineuse lente si fibrinolyse générale.", 9)
    a(0, 11, "Angusta, numéro 67580, déclenche. Il ne traite pas l'hémorragie.", 10)
    a(0, 11, "Cytotec, numéro 46945, est contre-indiqué chez la femme enceinte.", 11)

    a(0, 12, "Un utérotonique préventif est recommandé pour toutes les naissances.", 3)
    a(0, 12, "La compression chaude au deuxième stade réduit le risque de lésion sphinctérienne.", 4)
    a(0, 12, "L'épisiotomie médio-latérale se pense surtout à l'instrumental.", 4)
    a(0, 12, "L'angle lu est de 60 degrés quand le périnée est distendu.", 4)
    a(0, 12, "On n'utilise pas le fond utérin pour finir une épaule.", 14)

    a(0, 13, "[[FIGO]] 2015 : normal, suspect, pathologique, avec toutes les bornes.", 1)
    a(0, 13, "[[OMS]] 2018 : phase active à partir de 5 cm.", 3)
    a(0, 13, "Ligne 2022 : 500 ml, 1000 ml, index de choc supérieur à 0,9.", 2)
    a(0, 13, "[[RCOG]] 2015 : degrés 1, 2, 3a, 3b, 3c et 4.", 4)
    a(0, 13, "[[RCOG]] 2012 : McRoberts d'abord, pression sus-pubienne, pas de fond utérin.", 13)

    a(0, 14, "Piège. Prendre un tracé suspect pour un tracé normal.", 1)
    a(0, 14, "Piège. Césariser pour une dilatation lente avant 5 cm, mère et fœtus bien.", 3)
    a(0, 14, "Piège. Estimer le sang à l'œil et attendre.", 2)
    a(0, 14, "Piège. Donner Cytotec à une femme enceinte.", 11)
    a(0, 14, "Piège. Pousser sur le fond pour dégager une épaule.", 13)
    a(0, 14, "Piège. Recopier la dose de misoprostol de la lettre suisse de 2012.", 12)

    # ----- DX.1 déchirure -----
    leads[1][1] = "On classe la déchirure avant de prendre l'aiguille."
    leads[1][2] = "Toute voie basse expose. Le taux suisse n'est pas dans le texte lu."
    leads[1][3] = "Le sphincter externe et le sphincter interne ne sont pas le même muscle."
    leads[1][4] = "Doute sur le degré : on classe plus haut."
    leads[1][5] = "L'instrumental et une expulsion très rapide comptent dans l'histoire."
    leads[1][6] = "Le doigt rectal fait partie de l'examen."
    leads[1][7] = "Une déchirure n'exclut pas une atonie."
    leads[1][8] = "Le degré se dit avec la structure atteinte."
    leads[1][9] = "Le bloc et la lumière manquent souvent en salle."
    leads[1][10] = "Peau, muscle, sphincter, muqueuse : quatre paliers."
    leads[1][11] = "La réparation du sphincter se fait au bloc."
    leads[1][12] = "La compresse chaude et l'angle de l'épisiotomie préviennent."
    leads[1][13] = "3a, 3b et 3c ne se résument pas à degré 3."
    leads[1][14] = "Suturer sans toucher rectal laisse passer un degré 3."

    a(1, 1, "Le degré 1 atteint la peau périnéale ou la muqueuse vaginale.", 4)
    a(1, 1, "Le degré 2 atteint les muscles, pas le sphincter anal.", 4)
    a(1, 1, "Le degré 3 atteint le complexe du sphincter anal.", 4)
    a(1, 1, "Le 3a déchire moins de 50 pour cent de l'épaisseur du sphincter externe.", 4)
    a(1, 1, "Le 3b déchire plus de 50 pour cent de cette épaisseur.", 4)
    a(1, 1, "Le 3c déchire le sphincter externe et le sphincter interne.", 4)
    a(1, 1, "Le degré 4 ajoute la muqueuse anorectale.", 4)
    a(1, 1, "Cette classification est celle de la ligne [[RCOG]] de juin 2015.", 4)
    a(1, 2, "Le texte dit que toute femme qui accouche par voie basse est exposée.", 4)
    a(1, 2, "Les facteurs de risque ne prédisent pas assez pour écarter l'examen.", 4)
    a(1, 2, "Après une dystocie des épaules, le texte de 2012 cite 3,8 pour cent de degrés 3 ou 4.", 13)
    a(1, 2, "Ce 3,8 pour cent ne se généralise pas à toutes les voies basses.", 13)
    a(1, 3, "Le sphincter externe ferme l'anus. Le sphincter interne est plus profond.", 4)
    a(1, 3, "Une boutonnière rectale isolée n'est pas un simple degré 2.", 4)
    a(1, 3, "Le muscle relevateur n'est pas le sphincter. On les nomme à part.", 4)
    a(1, 4, "Si le degré 3 est douteux, on classe au degré supérieur.", 4)
    a(1, 4, "On examine avant de suturer, pas après seulement.", 4)
    a(1, 4, "Un saignement abondant fait poser un tampon et monter au bloc.", 4)
    a(1, 5, "On demande l'instrument, l'épisiotomie et une expulsion très rapide.", 4)
    a(1, 5, "On demande un antécédent de lésion du sphincter.", 4)
    a(1, 5, "On demande la douleur anale et une perte de gaz.", 4)
    a(1, 6, "L'inspection écarte les grandes lèvres et regarde le vagin.", 4)
    a(1, 6, "Le toucher rectal teste le tonus et cherche une boutonnière.", 4)
    a(1, 6, "On le fait chez toutes les voies basses, pas seulement si ça saigne.", 4)
    a(1, 7, "Sang rouge qui continue avec un utérus dur : penser à la déchirure.", 2)
    a(1, 7, "Utérus mou : l'atonie peut coexister. On traite les deux.", 2)
    a(1, 7, "Un degré 4 n'est pas une hémorroïde.", 4)
    a(1, 8, "Le diagnostic positif nomme le degré et la structure.", 4)
    a(1, 8, "On écrit 3a, 3b ou 3c, pas seulement troisième degré.", 4)
    a(1, 8, "Le compte rendu dit la méthode et le fil.", 4)
    a(1, 9, "La réparation d'une lésion sphinctérienne se fait au bloc.", 4)
    a(1, 9, "Il faut une anesthésie régionale ou générale, et de la lumière.", 4)
    a(1, 9, "En salle, seulement après avis d'un senior, dit le texte de 2015.", 4)
    a(1, 10, "Palier 1. Degré 1 ou 2 : suture selon le protocole local, après toucher rectal.", 4)
    a(1, 10, "Palier 2. Degré 3 ou 4 : bloc, pas la salle par défaut.", 4)
    a(1, 10, "Palier 3. Après le fil : nouveau toucher rectal.", 4)
    a(1, 11, "Pas de point en huit sur le sphincter : il ischémie.", 4)
    a(1, 11, "Le sphincter interne, s'il est vu, se répare à part, sans chevauchement.", 4)
    a(1, 11, "Le sphincter externe en pleine épaisseur : chevauchement ou bout à bout.", 4)
    a(1, 11, "Un 3a, et une partie des 3b, se répare bout à bout.", 4)
    a(1, 11, "Le fil peut être un monofilament 3-0 ou un tressé 2-0.", 4)
    a(1, 11, "On enterre les nœuds sous les muscles superficiels.", 4)
    a(1, 11, "Un antibiotique à large spectre est recommandé après la réparation.", 4)
    a(1, 11, "La ligne de 2015 ne nomme pas la molécule suisse. On ne l'invente pas.", 4)
    a(1, 11, "Cas corrigé. Le toucher rectal trouve une perte de tonus. On dit 3b, on va au bloc.", 4)
    a(1, 12, "La compression chaude pendant la poussée réduit les lésions sphinctériennes.", 4)
    a(1, 12, "La protection manuelle au dégagement de la tête est citée comme protectrice.", 4)
    a(1, 12, "Si l'épisiotomie est décidée, elle est médio-latérale.", 4)
    a(1, 12, "L'angle est de 60 degrés par rapport à la ligne médiane, périnée distendu.", 4)
    a(1, 13, "Les six degrés se récitent : 1, 2, 3a, 3b, 3c, 4.", 4)
    a(1, 13, "Le toucher rectal se fait avant et après.", 4)
    a(1, 13, "Le doute classe vers le haut.", 4)
    a(1, 14, "Piège. Appeler degré 2 une atteinte du sphincter.", 4)
    a(1, 14, "Piège. Oublier le toucher rectal parce que le saignement est petit.", 4)
    a(1, 14, "Piège. Laisser un point qui traverse la muqueuse anale.", 4)
    a(1, 14, "Piège. Réparer un degré 3 en salle sans lumière, par habitude.", 4)

    # ----- DX.2 tracé -----
    leads[2][1] = "On classe le tracé en trois, pas en rassurant ou non."
    leads[2][2] = "La fréquence suisse du tracé pathologique n'est pas dans le texte lu."
    leads[2][3] = "La décélération variable et la tardive n'ont pas le même sens."
    leads[2][4] = "On corrige la cause réversible avant de conclure."
    leads[2][5] = "La fièvre maternelle et le bêta-mimétique montent la ligne de base."
    leads[2][6] = "On lit dix minutes, pas une seule case."
    leads[2][7] = "Un tracé mauvais avec un cordon visible change la branche."
    leads[2][8] = "La classe pathologique se dit avec le critère qui la fait."
    leads[2][9] = "Le chapitre relu ne donne pas de seuil de pH au scalp."
    leads[2][10] = "Normal, puis suspect, puis pathologique."
    leads[2][11] = "Pathologique : corriger, évaluer, ou faire naître."
    leads[2][12] = "On surveille avant que le tracé ne devienne pathologique."
    leads[2][13] = "110, 160, 5, 25, 50 minutes, 3 minutes : on les garde tous."
    leads[2][14] = "L'absence d'accélération, seule, ne prouve pas l'hypoxie."

    a(2, 1, "La ligne de base normale va de 110 à 160.", 1)
    a(2, 1, "La tachycardie est une ligne de base au-dessus de 160 pendant plus de 10 minutes.", 1)
    a(2, 1, "La bradycardie est une ligne de base au-dessous de 110 pendant plus de 10 minutes.", 1)
    a(2, 1, "Entre 100 et 110, un fœtus post-terme peut encore être normal.", 1)
    a(2, 1, "La variabilité normale est une bande de 5 à 25.", 1)
    a(2, 1, "Elle est réduite si la bande est sous 5 pendant plus de 50 minutes.", 1)
    a(2, 1, "Elle est aussi réduite si cela dure plus de 3 minutes pendant une décélération.", 1)
    a(2, 1, "L'aspect salé est une bande au-dessus de 25 pendant plus de 30 minutes.", 1)
    a(2, 1, "Le sinusoïdal dure plus de 30 minutes, amplitude 5 à 15, 3 à 5 cycles par minute.", 1)
    a(2, 1, "Il n'a pas d'accélération. Ce n'est pas un pseudo-sinusoïdal bref.", 1)
    a(2, 2, "Le texte de 2015 ne donne pas un taux suisse de tracés pathologiques.", 1)
    a(2, 2, "On ne fabrique pas ce taux.", 1)
    a(2, 2, "La fièvre maternelle est la cause la plus fréquente de tachycardie citée.", 1)
    a(2, 3, "Une accélération monte en moins de 30 secondes, de plus de 15.", 1)
    a(2, 3, "Elle dure plus de 15 secondes et moins de 10 minutes.", 1)
    a(2, 3, "Avant 32 semaines, 10 secondes et 10 peuvent suffire.", 1)
    a(2, 3, "Le sommeil profond peut durer jusqu'à 50 minutes, avec peu d'accélérations.", 1)
    a(2, 3, "Une décélération baisse de plus de 15 pendant plus de 15 secondes.", 1)
    a(2, 3, "La variable chute en moins de 30 secondes et garde de la variabilité.", 1)
    a(2, 3, "La tardive a un début progressif, plus de 30 secondes jusqu'au nadir.", 1)
    a(2, 3, "La prolongée dure plus de 3 minutes.", 1)
    a(2, 3, "Au-delà de 5 minutes, sous 80, avec variabilité faible : hypoxie aiguë fréquente.", 1)
    a(2, 4, "Classe normale : 110 à 160, variabilité 5 à 25, pas de décélérations répétitives.", 1)
    a(2, 4, "Répétitif veut dire lié à plus de 50 pour cent des contractions.", 1)
    a(2, 4, "Classe suspecte : il manque un critère normal, sans critère pathologique.", 1)
    a(2, 4, "Classe pathologique : ligne de base sous 100.", 1)
    a(2, 4, "Ou variabilité réduite plus de 50 minutes, ou salée plus de 30 minutes.", 1)
    a(2, 4, "Ou sinusoïdal plus de 30 minutes.", 1)
    a(2, 4, "Ou tardives ou prolongées répétitives plus de 30 minutes.", 1)
    a(2, 4, "Ce délai passe à 20 minutes si la variabilité est réduite.", 1)
    a(2, 4, "Ou une seule décélération prolongée de plus de 5 minutes.", 1)
    a(2, 5, "On demande la fièvre, l'épidurale et un médicament bêta-mimétique.", 1)
    a(2, 5, "On demande un bêtabloquant maternel devant une bradycardie.", 1)
    a(2, 5, "On demande la position, souvent un décubitus qui comprime la veine cave.", 1)
    a(2, 6, "On estime la ligne de base sur 10 minutes.", 1)
    a(2, 6, "Au deuxième stade, on vérifie que le capteur n'enregistre pas la mère.", 1)
    a(2, 6, "Une accélération synchrone de la poussée peut être le pouls maternel.", 1)
    a(2, 7, "Tachycardie et fièvre : penser à l'infection, pas seulement à l'hypoxie.", 1)
    a(2, 7, "Sinusoïdal : penser à l'anémie fœtale, dont le vasa praevia rompu.", 1)
    a(2, 7, "Décélération qui ne revient pas : penser procidence, rupture, décollement.", 1)
    a(2, 8, "On écrit la classe et le critère, avec l'heure.", 1)
    a(2, 8, "Un tracé normal n'a pas besoin d'un geste pour le rythme.", 1)
    a(2, 8, "L'absence d'accélération sur un tracé sinon normal est de sens incertain.", 1)
    a(2, 9, "Le chapitre [[FIGO]] de 2015 renvoie à d'autres méthodes d'oxygénation.", 1)
    a(2, 9, "Il ne fixe pas, dans les pages relues, un seuil de pH au scalp.", 1)
    a(2, 9, "On n'écrit donc pas ce seuil ici.", 1)
    a(2, 10, "Palier normal : pas d'intervention pour le rythme.", 1)
    a(2, 10, "Palier suspect : corriger ce qui est réversible et surveiller de près.", 1)
    a(2, 10, "Palier pathologique : action immédiate, puis faire naître si ça ne cède pas.", 1)
    a(2, 11, "On couche sur le côté, on arrête l'ocytocine si elle tourne.", 5)
    a(2, 11, "L'[[AIPS]] 22114 dit d'arrêter la perfusion dès l'hypertonie ou la souffrance.", 5)
    a(2, 11, "Le texte de 2015 ne prouve pas qu'un litre de sérum corrige un tracé chez une femme normotendue.", 1)
    a(2, 11, "Le texte ne prouve pas non plus qu'un masque d'oxygène, seul, le corrige.", 1)
    a(2, 11, "Cas corrigé. Décélération de 6 minutes, variabilité plate. On fait naître, on ne attend pas une heure.", 1)
    a(2, 12, "On relit le tracé avant qu'un critère suspect ne devienne pathologique.", 1)
    a(2, 12, "On évite l'hyperstimulation : la vitesse maximale lue est 20 milli-U.I. par minute.", 5)
    a(2, 13, "Normal : 110 à 160, bande 5 à 25, pas de décélérations répétitives.", 1)
    a(2, 13, "Pathologique : sous 100, ou les durées de 50, 30, 20 et 5 minutes.", 1)
    a(2, 13, "On ne résume pas la classe à un seul adjectif.", 1)
    a(2, 14, "Piège. Appeler rassurant un tracé seulement suspect.", 1)
    a(2, 14, "Piège. Rassurer parce qu'il n'y a pas d'accélération, et ignorer le reste.", 1)
    a(2, 14, "Piège. Continuer l'ocytocine pendant une hypertonie.", 5)
    a(2, 14, "Piège. Prendre le pouls maternel pour le fœtus au deuxième stade.", 1)

    # ----- DX.3 stagnation -----
    leads[3][1] = "La phase active commence à 5 cm dans le texte de 2018."
    leads[3][2] = "Le taux suisse de stagnation n'est pas lu. On ne l'invente pas."
    leads[3][3] = "Le col et la contraction ne sont pas la même panne."
    leads[3][4] = "Avant 5 cm, on n'accélère pas si tout va bien."
    leads[3][5] = "On demande la parité, la poche et l'heure du début."
    leads[3][6] = "On mesure le col deux fois, avec la hauteur de la tête."
    leads[3][7] = "Une présentation du front n'est pas une simple inertie."
    leads[3][8] = "On dit les centimètres et l'heure, pas le mot stagnation seul."
    leads[3][9] = "Le tracé décide si l'on a le temps."
    leads[3][10] = "Latence, puis phase active, puis descente."
    leads[3][11] = "L'ocytocine suit l'information 22114, pas une habitude."
    leads[3][12] = "On n'admet pas trop tôt une latence encore physiologique."
    leads[3][13] = "5 cm, 12 heures, 10 heures, 1 cm par heure : chacun a son sens."
    leads[3][14] = "La ligne d'alerte du partogramme n'est plus un motif de routine."

    a(3, 1, "La latence va jusqu'à 5 cm, avec des contractions douloureuses.", 3)
    a(3, 1, "La phase active part de 5 cm jusqu'à la dilatation complète.", 3)
    a(3, 1, "Cela vaut pour le premier accouchement et pour les suivants.", 3)
    a(3, 1, "La descente est l'autre temps : la tête doit progresser.", 3)
    a(3, 2, "La phase active ne dépasse en général pas 12 heures au premier enfant.", 3)
    a(3, 2, "Elle ne dépasse en général pas 10 heures ensuite.", 3)
    a(3, 2, "La durée type de la latence n'est pas fixée.", 3)
    a(3, 2, "Aucun taux suisse de dystocie n'est dans le texte relu.", 3)
    a(3, 3, "La contraction vient du fond. Le col cède si la tête applique.", 5)
    a(3, 3, "Une poche intacte ou une présentation haute changent la descente.", 3)
    a(3, 3, "L'utérus fatigué répond moins. Ce n'est pas toujours un bassin trop petit.", 5)
    a(3, 4, "Le seuil de 1 cm par heure n'identifie pas bien le mauvais pronostic.", 3)
    a(3, 4, "Il n'est pas recommandé pour cela.", 3)
    a(3, 4, "Une dilatation plus lente, seule, n'indique pas une intervention de routine.", 3)
    a(3, 4, "Avant 5 cm, si mère et fœtus vont bien, pas d'ocytocine pour accélérer.", 3)
    a(3, 4, "Pas de césarienne non plus, dans cette seule indication, avant 5 cm.", 3)
    a(3, 5, "On note l'heure des contractions régulières et de la rupture.", 3)
    a(3, 5, "On demande la parité : 12 heures et 10 heures ne se mélangent pas.", 3)
    a(3, 5, "On demande une cicatrice avant tout déclenchement par Angusta.", 10)
    a(3, 6, "Deux touchers, à distance, valent mieux qu'un chiffre isolé.", 3)
    a(3, 6, "On note dilatation, effacement, hauteur et variété.", 3)
    a(3, 6, "La grille en points de Bishop n'est pas dans les textes relus. On ne l'invente pas.", 3)
    a(3, 6, "On décrit quand même les cinq éléments : ouverture, longueur, hauteur, consistance, position.", 10)
    a(3, 7, "Front, face ou siège : ce n'est pas une inertie à perfuser d'abord.", 3)
    a(3, 7, "Un tracé pathologique change l'ordre : naître, pas accélérer.", 1)
    a(3, 7, "Une bosse séro-sanguine peut faire croire que la tête est descendue.", 3)
    a(3, 8, "On écrit les centimètres, l'heure et la parité.", 3)
    a(3, 8, "On ne dit pas stagnation avant 5 cm sur la seule lenteur.", 3)
    a(3, 8, "Après 5 cm, une lenteur isolée ne suffit toujours pas.", 3)
    a(3, 9, "Le [[CTG]] dit si l'on peut attendre la prochaine heure.", 1)
    a(3, 9, "Angusta demande une surveillance continue du tracé et des contractions.", 10)
    a(3, 9, "On évalue le col avant d'ouvrir le blister.", 10)
    a(3, 10, "Avant 5 cm et tout va bien : marche, soutien, pas d'utérotonique d'accélération.", 3)
    a(3, 10, "Phase active, tracé correct, contractions faibles : oxytocine selon 22114.", 5)
    a(3, 10, "Présentation incompatible ou tracé pathologique : ne pas accélérer.", 1)
    a(3, 11, "La perfusion lente commence à 1-2 milli-U.I. par minute.", 5)
    a(3, 11, "On augmente d'au plus 1-2 milli-U.I. par minute, pas avant 20 minutes.", 5)
    a(3, 11, "Souvent moins de 10 milli-U.I. par minute suffisent près du terme.", 5)
    a(3, 11, "On ne dépasse pas 20 milli-U.I. par minute, sauf exception écrite.", 5)
    a(3, 11, "La dilution lue : 5 U.I. dans 500 ml, soit 10 milli-U.I. par ml.", 5)
    a(3, 11, "Sans contraction après 5 U.I. au total, on arrête. On peut reprendre le lendemain.", 5)
    a(3, 11, "Hypertonie ou souffrance : arrêt immédiat.", 5)
    a(3, 11, "Angusta : 25 microgrammes toutes les 2 heures, ou 50 microgrammes toutes les 4 heures.", 10)
    a(3, 11, "Le maximum lu est 200 microgrammes en 24 heures.", 10)
    a(3, 11, "On attend 4 heures après Angusta avant l'ocytocine.", 10)
    a(3, 11, "Les deux ensemble sont contre-indiqués.", 10)
    a(3, 11, "Ces débits sont ceux de l'[[AIPS]] 22114.", 5)
    a(3, 11, "Cas corrigé. Col à 4 cm, tracé normal. On ne pose pas l'ocytocine pour aller plus vite.", 3)
    a(3, 12, "Le compagnon de naissance est recommandé pendant tout le travail.", 3)
    a(3, 12, "On informe que la latence n'a pas de durée standard.", 3)
    a(3, 13, "5 cm ouvre la phase active. 12 heures et 10 heures sont les durées usuelles citées.", 3)
    a(3, 13, "1 cm par heure n'est plus une ligne qui décide seule.", 3)
    a(3, 14, "Piège. Tracer une ligne d'alerte et césariser dessus.", 3)
    a(3, 14, "Piège. Mélanger Angusta et oxytocine.", 10)
    a(3, 14, "Piège. Dépasser 20 milli-U.I. par minute sans l'exception écrite.", 5)
    a(3, 14, "Piège. Donner Angusta sur un utérus cicatriciel.", 10)

    # ----- DX.4 hémorragie atonie -----
    leads[4][1] = "Cinq cents millilitres, ou le choc, suffisent à nommer l'hémorragie."
    leads[4][2] = "Les taux lus sont dans la fenêtre, avec l'année 2022."
    leads[4][3] = "L'atonie est un muscle qui ne ferme pas les vaisseaux du lit placentaire."
    leads[4][4] = "On cherche les quatre causes pendant qu'on traite."
    leads[4][5] = "Utérus surdistendu, travail long, fièvre : on les demande."
    leads[4][6] = "Un utérus mou au-dessus de l'ombilic est le signe classique."
    leads[4][7] = "Le sang peut être dans l'utérus, invisible dehors."
    leads[4][8] = "Le diagnostic joint le volume, ou l'index de choc, et le tonus."
    leads[4][9] = "On ne attend pas le fibrinogène pour la première dose."
    leads[4][10] = "Massage, oxytocine, puis relais, puis geste."
    leads[4][11] = "L'oxytocine est le premier médicament de l'hémorragie primaire."
    leads[4][12] = "La prévention est une injection pour chaque naissance."
    leads[4][13] = "500, 1000, 0,9, 80 pour cent : on les dit avec 2022."
    leads[4][14] = "L'œil sous-estime. C'est le piège le plus constant."

    a(4, 1, "Après voie basse, le seuil lu est une perte d'au moins 500 ml.", 2)
    a(4, 1, "Après césarienne, le seuil lu est d'au moins 1000 ml.", 2)
    a(4, 1, "Des signes de choc suffisent, même si le linge paraît moins plein.", 2)
    a(4, 1, "L'index de choc est la fréquence divisée par la pression systolique.", 2)
    a(4, 1, "Il est pathologique au-dessus de 0,9.", 2)
    a(4, 1, "L'atonie est la cause tonique, focale ou diffuse.", 2)
    a(4, 2, "L'incidence rapportée est de 1 à 3 pour cent des naissances.", 2)
    a(4, 2, "La mesure quantitative monte vers 10 pour cent dans le texte de 2022.", 2)
    a(4, 2, "La forme très grave est d'environ 2 pour 1 000.", 2)
    a(4, 2, "L'atonie représente au moins 80 pour cent des hémorragies.", 2)
    a(4, 2, "L'œil sous-estime de 30 à 50 pour cent.", 2)
    a(4, 3, "Après le placenta, les fibres compriment les artères du lit.", 2)
    a(4, 3, "Si le muscle reste mou, le lit saigne.", 2)
    a(4, 3, "Un travail long, une surdistension ou une infection favorisent cela.", 2)
    a(4, 3, "L'oxytocine longue peut épuiser la réponse, dit le texte de 2022.", 2)
    a(4, 3, "Entre 500 et 1500 ml, la femme tolère souvent encore, cliniquement.", 2)
    a(4, 4, "Les quatre causes se disent ensemble : tonus, traumatisme, tissu, thrombine.", 2)
    a(4, 4, "On les cherche en parallèle, pas l'une après l'échec complet de l'autre.", 2)
    a(4, 4, "Au-delà de 1000 ml, on envisage l'appel d'un expert.", 2)
    a(4, 4, "À 1500 ml qui continuent, l'appel est exigé.", 2)
    a(4, 5, "On demande la multiparité, l'hydramnios, un gros enfant, des jumeaux.", 2)
    a(4, 5, "On demande un travail très long ou très rapide.", 2)
    a(4, 5, "On demande une hémorragie déjà eue.", 2)
    a(4, 6, "L'utérus se palpe : mou, haut, mal rétracté.", 2)
    a(4, 6, "On regarde le col, le vagin et le périnée en même temps.", 4)
    a(4, 6, "Le pouls et la tension donnent l'index de choc.", 2)
    a(4, 7, "Utérus dur et sang qui continue : traumatisme ou tissu, pas seulement le tonus.", 2)
    a(4, 7, "Pas de caillot, saignement aux points de ponction : penser thrombine.", 2)
    a(4, 7, "Jusqu'à 500 à 1000 ml peuvent rester dans la cavité, dit le texte.", 2)
    a(4, 8, "On écrit le volume mesuré, ou l'index, et le tonus.", 2)
    a(4, 8, "On ne dit pas atonie si le placenta est incomplet, sans le dire.", 2)
    a(4, 8, "Le diagnostic de cause peut changer en quelques minutes.", 2)
    a(4, 9, "L'acide tranexamique se donne sans attendre le bilan de coagulation.", 2)
    a(4, 9, "L'information 70581 indique les hémorragies d'origine obstétricale.", 9)
    a(4, 9, "Pour une fibrinolyse générale, la dose lue est 1 g en intraveineuse lente.", 9)
    a(4, 9, "Cela équivaut à 15 mg par kilogramme, toutes les 6 à 8 heures.", 9)
    a(4, 9, "La voie est intraveineuse seulement. Jamais intrathécale.", 9)
    a(4, 9, "L'injection trop rapide a été liée à une bradycardie.", 9)
    a(4, 10, "Étape 1. Massage, mesure, voie veineuse, oxytocine.", 5)
    a(4, 10, "Étape 2. Si ça continue : sulprostone, pas une deuxième logique lente.", 8)
    a(4, 10, "Étape 3. Tissu resté ou déchirure : geste, pas seulement le médicament.", 2)
    a(4, 11, "Traitement lu : 5 U.I. en perfusion sur 5 minutes, ou 5-10 U.I. en intramusculaire.", 5)
    a(4, 11, "Dans les cas graves : ensuite 5-20 U.I. dans 500 ml, à la vitesse utile.", 5)
    a(4, 11, "On évite le bolus rapide.", 5)
    a(4, 11, "Pabal est une prévention, 100 " + UG + " une seule fois, pas un rappel.", 6)
    a(4, 11, "L'information dit qu'on n'a pas de donnée pour une dose supplémentaire.", 6)
    a(4, 11, "Le texte de 2022 dit l'usage curatif de la carbétocine hors indication.", 2)
    a(4, 11, "Méthergin : 1 ml, soit 0,2 mg, en intramusculaire.", 7)
    a(4, 11, "En intraveineuse, 0,1 à 0,2 mg, lentement, au moins 60 secondes.", 7)
    a(4, 11, "Pas pendant l'allaitement, et pas dans les 12 heures après la dernière dose.", 7)
    a(4, 11, "Au plus 5 injections en 24 heures pour le schéma répété lu.", 7)
    a(4, 11, "Nalador vient après l'oxytocine, quand l'atonie est confirmée.", 8)
    a(4, 11, "Dose initiale lue du tableau 2 : 1,7 " + UG + " par minute.", 8)
    a(4, 11, "Dose maximale lue : 8,3 " + UG + " par minute.", 8)
    a(4, 11, "La dose totale ne dépasse pas 1500 " + UG + ".", 8)
    a(4, 11, "Pas plus de 10 heures.", 8)
    a(4, 11, "Avec l'oxytocine, seulement utérus vidé, et avec prudence.", 8)
    a(4, 11, "Des troubles du rythme graves ont été rapportés avec l'association.", 5)
    a(4, 11, "Cas corrigé. 700 ml mesurés, utérus mou. Oxytocine tout de suite, et 1 g d'acide tranexamique.", 9)
    a(4, 12, "Prévention après voie basse : 5 U.I. en perfusion sur 5 minutes après le placenta.", 5)
    a(4, 12, "Ou 5-10 U.I. en intramusculaire.", 5)
    a(4, 12, "Si l'oxytocine tournait déjà, on monte à 20-40 milli-U.I. par minute un moment.", 5)
    a(4, 12, "Après césarienne : 5 U.I. sur 5 minutes dès l'enfant né.", 5)
    a(4, 12, "Pabal : 100 " + UG + " en intraveineuse, ou en intramusculaire après voie basse.", 6)
    a(4, 13, "Quatre T, index au-dessus de 0,9, oxytocine d'abord, acide tranexamique sans attendre.", 2)
    a(4, 13, "Les doses suisses restent celles de l'[[AIPS]], numéros 22114, 58079, 12730, 43642 et 70581.", 5)
    a(4, 14, "Piège. Croire le linge plutôt que la balance.", 2)
    a(4, 14, "Piège. Donner une deuxième ampoule de Pabal.", 6)
    a(4, 14, "Piège. Méthergin en bolus intraveineux rapide.", 7)
    a(4, 14, "Piège. Nalador et oxytocine ensemble sans surveillance du cœur.", 8)
    a(4, 14, "Piège. Injecter l'acide tranexamique dans le dos.", 9)
    a(4, 14, "Piège. Utiliser Cytotec, numéro 46945, chez une femme qui vient d'accoucher encore à risque.", 11)

    # ----- DX.5 rétention placentaire -----
    leads[5][1] = "Le placenta qui ne naît pas se nomme sans minute inventée."
    leads[5][2] = "Le taux suisse de cette rétention n'est pas dans le texte relu."
    leads[5][3] = "Le lit placentaire saigne tant que le muscle ne le ferme pas."
    leads[5][4] = "La traction contrôlée est le premier geste nommé, avec quelqu'un de qualifié."
    leads[5][5] = "On demande si le placenta est né et si l'oxytocine tourne."
    leads[5][6] = "On regarde le placenta, le tonus et le sang mesuré."
    leads[5][7] = "Un placenta incomplet est du tissu, pas seulement du tonus."
    leads[5][8] = "On écrit incomplet ou non né. On n'invente pas une minute."
    leads[5][9] = "Le saignement ne retarde pas le geste pour une image."
    leads[5][10] = "Utérus contracté, personne qualifiée, traction contrôlée."
    leads[5][11] = "La conduite du troisième stade est celle de l'information 22114."
    leads[5][12] = "L'utérotonique préventif concerne toutes les naissances."
    leads[5][13] = "Traction contrôlée, placenta complet, sang pesé."
    leads[5][14] = "Tirer fort sur un utérus mou n'est pas la traction contrôlée."

    a(5, 1, "La rétention placentaire est un placenta qui n'est pas né.", 3)
    a(5, 1, "Le texte de 2018 ne fixe pas, dans les pages relues, un nombre de minutes.", 3)
    a(5, 1, "On n'écrit donc pas ce nombre.", 3)
    a(5, 1, "La traction contrôlée du cordon est le premier geste cité.", 3)
    a(5, 1, "Elle suppose une personne qualifiée, présente.", 3)
    a(5, 2, "Aucun taux suisse n'est dans les textes relus pour cette branche.", 3)
    a(5, 2, "On ne fabrique pas ce taux.", 3)
    a(5, 2, "Le tissu est l'une des quatre causes de l'hémorragie, texte de 2022.", 2)
    a(5, 3, "Si le placenta ne se décolle pas, la zone d'insertion peut saigner.", 2)
    a(5, 3, "Un utérus mou ne ferme pas les vaisseaux du lit.", 2)
    a(5, 3, "La traction sur un utérus mou n'est pas le geste cité.", 3)
    a(5, 4, "On vérifie que le placenta est entier.", 2)
    a(5, 4, "On mesure le sang pendant cet examen.", 2)
    a(5, 4, "Un saignement qui continue se traite sans attendre, comme une hémorragie.", 2)
    a(5, 5, "On demande si le placenta est sorti.", 5)
    a(5, 5, "On demande si une perfusion d'oxytocine est en cours.", 5)
    a(5, 5, "On demande une cicatrice utérine avant tout déclenchement.", 10)
    a(5, 6, "On étale le placenta et l'on cherche une partie manquante.", 2)
    a(5, 6, "On palpe le tonus du fond utérin.", 2)
    a(5, 6, "Le sang sur le linge se pèse.", 2)
    a(5, 7, "Placenta incomplet : cause tissulaire, même si l'utérus est mou.", 2)
    a(5, 7, "Placenta complet et utérus mou : atonie, une autre branche.", 2)
    a(5, 7, "Utérus dur et sang qui continue : chercher une déchirure.", 4)
    a(5, 8, "Le diagnostic positif dit si le placenta est né et s'il est entier.", 3)
    a(5, 8, "Il ne cite pas une minute absente du texte de 2018.", 3)
    a(5, 8, "Le volume mesuré, s'il y a du sang, se note à part.", 2)
    a(5, 9, "On ne retarde pas l'utérotonique pour une image si le sang continue.", 2)
    a(5, 9, "L'information 22114 décrit la perfusion. Elle ne décrit pas une image.", 5)
    a(5, 10, "Palier 1. Utérus contracté et personne qualifiée : traction contrôlée du cordon.", 3)
    a(5, 10, "Palier 2. Sang qui continue : oxytocine selon l'information 22114.", 5)
    a(5, 10, "Palier 3. Placenta incomplet : le tissu se retire, pas seulement un médicament.", 2)
    a(5, 11, "Si la perfusion tourne déjà, on la monte à 20-40 milli-U.I. par minute.", 5)
    a(5, 11, "Ce débit couvre la période placentaire, dit l'information.", 5)
    a(5, 11, "Après l'expulsion, la prévention lue est 5 U.I. en perfusion sur 5 minutes.", 5)
    a(5, 11, "L'autre voie lue est 5-10 U.I. en intramusculaire.", 5)
    a(5, 11, "Méthergin, numéro 12730, peut être donné au passage de l'épaule antérieure.", 7)
    a(5, 11, "La dose lue est 0,2 mg en intramusculaire.", 7)
    a(5, 11, "L'information dit que le placenta suit souvent la contraction.", 7)
    a(5, 11, "Une pression manuelle sur le fond peut aider cette expulsion.", 7)
    a(5, 11, "Cette pression n'est pas le geste d'une épaule bloquée.", 13)
    a(5, 11, "Ces phrases viennent de l'[[AIPS]], numéros 22114 et 12730.", 5)
    a(5, 11, "Cas corrigé. Placenta non né, utérus dur, personne qualifiée. Traction contrôlée, sang pesé.", 3)
    a(5, 12, "Un utérotonique préventif est recommandé pour toutes les naissances.", 3)
    a(5, 12, "On ne mélange pas Angusta et oxytocine.", 10)
    a(5, 13, "Premier geste nommé : traction contrôlée, personne qualifiée.", 3)
    a(5, 13, "Pas de minute inventée. Sang pesé. Placenta entier ou non.", 3)
    a(5, 14, "Piège. Tirer sur le cordon alors que l'utérus est mou.", 3)
    a(5, 14, "Piège. Inventer une minute absente du texte de 2018.", 3)
    a(5, 14, "Piège. Appuyer sur le fond pour finir une épaule, en citant Méthergin.", 13)
    a(5, 14, "Piège. Oublier de regarder si le placenta est entier.", 2)

    # ----- DX.6 siège -----
    leads[6][1] = "On nomme le type de siège avant de choisir la voie."
    leads[6][2] = "Le taux suisse du siège en travail n'est pas lu."
    leads[6][3] = "Fesses seules, fesses et pieds, ou pieds : trois formes."
    leads[6][4] = "La voie se décide avec un senior. On n'invente pas un taux."
    leads[6][5] = "On demande le type de siège, la poche et une cicatrice."
    leads[6][6] = "Le toucher dit les pieds, les fesses ou le cordon."
    leads[6][7] = "Un pied et un cordon visible changent l'urgence."
    leads[6][8] = "On écrit le type de siège et la classe du tracé."
    leads[6][9] = "Le tracé se lit avec la classe entière."
    leads[6][10] = "Pied, cordon ou tracé pathologique : naître, ne pas accélérer."
    leads[6][11] = "Angusta est contre-indiqué si la présentation empêche la voie basse."
    leads[6][12] = "On ne déclenche pas un siège incompatible pour aller plus vite."
    leads[6][13] = "Trois formes. Un senior. Pas de taux inventé."
    leads[6][14] = "Perfuser pour forcer un siège qui ne progresse pas est un piège."

    a(6, 1, "Le siège décomplété présente les fesses, jambes relevées.", 3)
    a(6, 1, "Le siège complet présente les fesses et les pieds.", 3)
    a(6, 1, "Le siège avec un pied, ou les deux, est incomplet.", 3)
    a(6, 1, "Ces trois noms décrivent la présentation. Ils ne donnent pas un taux.", 3)
    a(6, 2, "Aucun taux suisse de présentation du siège n'est dans les textes relus.", 3)
    a(6, 2, "On ne transforme pas cette absence en zéro.", 3)
    a(6, 3, "Un pied descend plus tôt que des fesses seules.", 3)
    a(6, 3, "L'espace à côté du pied peut laisser passer le cordon.", 1)
    a(6, 3, "Le cordon comprimé se voit sur le tracé, pas sur un pourcentage.", 1)
    a(6, 4, "Si la présentation empêche la voie basse, on n'accélère pas le travail.", 3)
    a(6, 4, "Angusta est contre-indiqué dans ce cas, information 67580.", 10)
    a(6, 4, "La voie, basse ou césarienne, se décide avec un senior.", 3)
    a(6, 4, "Aucun essai chiffré de voie n'est archivé ici. On n'en invente pas.", 3)
    a(6, 5, "On demande le type de siège connu avant le travail.", 3)
    a(6, 5, "On demande la rupture de la poche et un cordon déjà vu.", 1)
    a(6, 5, "On demande une cicatrice utérine.", 10)
    a(6, 6, "Le toucher distingue fesses, pieds et cordon.", 1)
    a(6, 6, "On lit le [[CTG]] sur dix minutes, pas sur une case.", 1)
    a(6, 6, "On note la dilatation et la hauteur.", 3)
    a(6, 7, "Pied et cordon devant : ce n'est plus une simple attente.", 1)
    a(6, 7, "Tracé pathologique : la branche devient celle du rythme.", 1)
    a(6, 7, "Fesses seules, tracé normal, progression : le senior peut encore discuter la voie.", 3)
    a(6, 8, "On écrit le type de siège, la dilatation et la classe du tracé.", 1)
    a(6, 8, "On n'écrit pas un pourcentage de réussite absent du dossier.", 3)
    a(6, 9, "Le [[CTG]] suit les trois classes, normale, suspecte, pathologique.", 1)
    a(6, 9, "La surveillance continue du tracé est exigée si Angusta est en cours.", 10)
    a(6, 9, "On n'ajoute pas d'oxytocine sur un tracé pathologique.", 5)
    a(6, 10, "Palier 1. Mère et fœtus bien, avant 5 cm : pas d'accélération de routine.", 3)
    a(6, 10, "Palier 2. Présentation incompatible avec la voie basse : pas d'Angusta.", 10)
    a(6, 10, "Palier 3. Cordon ou tracé pathologique : faire naître.", 1)
    a(6, 11, "On n'utilise pas l'oxytocine pour forcer une voie basse impossible.", 5)
    a(6, 11, "Hypertonie ou souffrance : arrêt immédiat de la perfusion 22114.", 5)
    a(6, 11, "Cas corrigé. Pied et cordon au toucher. On relève la présentation et l'on fait naître.", 1)
    a(6, 12, "On confirme la présentation avant un déclenchement.", 10)
    a(6, 12, "Une présentation qui empêche la voie basse contre-indique Angusta.", 10)
    a(6, 13, "Trois formes : fesses seules, fesses et pieds, pieds.", 3)
    a(6, 13, "La voie est une décision de senior, sans taux inventé.", 3)
    a(6, 14, "Piège. Donner Angusta sur un siège qui ne peut pas naître par voie basse.", 10)
    a(6, 14, "Piège. Citer un pourcentage de voie basse absent du dossier.", 3)
    a(6, 14, "Piège. Accélérer alors que le tracé est pathologique.", 1)

    # ----- DX.7 hématome rétroplacentaire -----
    leads[7][1] = "Douleur continue, utérus de bois, sang, tracé qui change."
    leads[7][2] = "Le taux suisse du décollement en travail n'est pas lu."
    leads[7][3] = "Le placenta se sépare avant la naissance. Le lit saigne."
    leads[7][4] = "On fait naître. On ne classe pas cela comme une simple atonie."
    leads[7][5] = "On demande une douleur différente de la contraction."
    leads[7][6] = "L'utérus reste dur, parfois avec peu de sang dehors."
    leads[7][7] = "Le choc peut dépasser le sang vu."
    leads[7][8] = "On écrit la douleur, le tonus et la classe du tracé."
    leads[7][9] = "Le laboratoire vient avec le geste. Il ne le précède pas."
    leads[7][10] = "Naître, puis traiter le sang."
    leads[7][11] = "L'oxytocine ne remplace pas la naissance."
    leads[7][12] = "Une douleur qui change se dit tôt."
    leads[7][13] = "Bois, douleur continue, tracé, naissance."
    leads[7][14] = "Rassurer sur un petit saignement dehors est un piège."

    a(7, 1, "L'hématome rétroplacentaire pendant le travail est un décollement avant la naissance.", 12)
    a(7, 1, "La lettre suisse du 19 juillet 2012 le cite parmi les situations de coagulation.", 12)
    a(7, 1, "Cette lettre est archivée. On ne recopie pas sa dose de misoprostol.", 12)
    a(7, 1, "Le volume qui compte, après la naissance, reste celui de la ligne de 2022.", 2)
    a(7, 2, "Aucun taux suisse de décollement n'est dans les textes relus.", 12)
    a(7, 2, "On ne le fabrique pas.", 12)
    a(7, 2, "La forme d'hémorragie qui menace la vie est d'environ 2 pour 1 000.", 2)
    a(7, 3, "Le placenta quitte la paroi. Le sang s'accumule derrière lui.", 12)
    a(7, 3, "L'utérus peut devenir dur, en bois, et douloureux en continu.", 12)
    a(7, 3, "La coagulation peut se consommer. C'est l'association lue en 2012.", 12)
    a(7, 4, "Douleur continue, utérus de bois, tracé qui se dégrade : on fait naître.", 1)
    a(7, 4, "On ne remplace pas cette décision par un protocole d'atonie.", 2)
    a(7, 4, "Le sang dehors peut être moindre que le sang dedans.", 2)
    a(7, 5, "On demande une douleur qui ne cède pas entre les contractions.", 12)
    a(7, 5, "On demande un saignement, même petit, et l'heure du changement.", 12)
    a(7, 6, "L'utérus se palpe en permanence, pas seulement pendant la contraction.", 12)
    a(7, 6, "Un utérus de bois est dur et douloureux.", 12)
    a(7, 6, "Le [[CTG]] peut montrer une bradycardie ou une décélération prolongée.", 1)
    a(7, 7, "Peu de sang et un choc : le sang peut être caché.", 2)
    a(7, 7, "Le texte de 2022 dit que 500 à 1000 ml peuvent rester dans la cavité.", 2)
    a(7, 7, "L'index de choc au-dessus de 0,9 compte, même si le linge semble maigre.", 2)
    a(7, 8, "On écrit douleur continue, tonus de bois, volume et classe du tracé.", 1)
    a(7, 8, "On ne dit pas atonie seule si l'utérus est de bois.", 2)
    a(7, 9, "L'acide tranexamique, numéro 70581, accompagne l'hémorragie sans attendre le laboratoire.", 9)
    a(7, 9, "Pour une fibrinolyse générale, la dose lue est 1 g en intraveineuse lente.", 9)
    a(7, 9, "La voie est intraveineuse seulement. Jamais dans le dos.", 9)
    a(7, 9, "Conditions lues de l'hémostase : température au-dessus de 34 degrés.", 2)
    a(7, 9, "Calcium au-dessus de 0,9 mmol par litre, et pH au-dessus de 7,2.", 2)
    a(7, 9, "Le numéro 70581 est une information de l'[[AIPS]].", 9)
    a(7, 10, "Palier 1. Faire naître, par la voie la plus sûre décidée sur place.", 1)
    a(7, 10, "Palier 2. Après la naissance, oxytocine si le muscle saigne.", 5)
    a(7, 10, "Palier 3. Appel exigé si 1500 ml continuent.", 2)
    a(7, 11, "L'oxytocine 22114 traite le muscle après la naissance, pas le décollement lui-même.", 5)
    a(7, 11, "Si le muscle saigne : 5 U.I. en perfusion sur 5 minutes.", 5)
    a(7, 11, "Ou 5-10 U.I. en intramusculaire.", 5)
    a(7, 11, "On évite le bolus rapide.", 5)
    a(7, 11, "Cas corrigé. Douleur continue, utérus de bois, décélération de plus de 5 minutes. On fait naître.", 1)
    a(7, 12, "On dit tôt une douleur qui change et un saignement.", 12)
    a(7, 12, "On ne rassure pas sur un petit saignement si l'utérus est de bois.", 2)
    a(7, 13, "Bois, douleur continue, tracé pathologique, naissance.", 1)
    a(7, 13, "Lettre de 2012 pour l'association à la coagulation. Ligne de 2022 pour le volume.", 2)
    a(7, 14, "Piège. Attendre un laboratoire avant de faire naître.", 2)
    a(7, 14, "Piège. Masser comme une atonie sans décider la naissance.", 2)
    a(7, 14, "Piège. Recopier la dose de misoprostol de la lettre de 2012.", 12)
    a(7, 14, "Piège. Injecter l'acide tranexamique dans le dos.", 9)

    # ----- DX.8 dystocie des épaules -----
    leads[8][1] = "La tête est née. La traction douce ne sort pas l'épaule."
    leads[8][2] = "Le taux des grandes séries se lit dans la fenêtre, avec 2012."
    leads[8][3] = "L'épaule antérieure bute sur la symphyse."
    leads[8][4] = "On le dit à voix haute. On n'appuie pas sur le fond."
    leads[8][5] = "On demande si la tête est née et si la traction douce a échoué."
    leads[8][6] = "La tête ne tourne pas. On regarde si la main peut entrer."
    leads[8][7] = "Ce n'est pas un simple ralentissement de la poussée."
    leads[8][8] = "On écrit la manœuvre qui a libéré l'épaule."
    leads[8][9] = "Aucun bilan ne précède la flexion des hanches."
    leads[8][10] = "Hanches fléchies, pression sus-pubienne, puis bras postérieur."
    leads[8][11] = "On ne reste pas sur une manœuvre qui a déjà échoué."
    leads[8][12] = "Pas de pression sur le fond. On coupe seulement si la main n'entre pas."
    leads[8][13] = "Mars 2012 pour la définition. 2026 pour l'ordre des gestes."
    leads[8][14] = "Pousser sur le fond utérin est le piège le plus grave."

    a(8, 1, "La dystocie des épaules suit un accouchement céphalique par voie vaginale.", 13)
    a(8, 1, "La tête est née. La traction douce a échoué.", 13)
    a(8, 1, "Il faut des manœuvres supplémentaires pour sortir les épaules.", 13)
    a(8, 1, "Cette définition est celle de mars 2012.", 13)
    a(8, 2, "L'incidence lue dans les grandes séries va de 0,58 à 0,70 pour cent.", 13)
    a(8, 2, "Le texte de 2012 cite 11 pour cent d'hémorragies dans ces accouchements.", 13)
    a(8, 2, "Il cite 3,8 pour cent de déchirures de degré 3 ou 4.", 13)
    a(8, 2, "Ce 3,8 pour cent ne se généralise pas à toutes les voies basses.", 13)
    a(8, 2, "La lésion du plexus brachial va de 2,3 à 16 pour cent de ces accouchements.", 13)
    a(8, 3, "L'épaule antérieure reste derrière la symphyse.", 13)
    a(8, 3, "Pousser sur le fond l'y enfonce. Le texte l'interdit.", 13)
    a(8, 3, "La traction doit rester axiale, sans excès.", 13)
    a(8, 4, "On appelle de l'aide.", 14)
    a(8, 4, "On décourage la poussée.", 14)
    a(8, 4, "On dit à voix haute qu'il s'agit d'une dystocie des épaules.", 14)
    a(8, 4, "On ne garde pas une manœuvre déjà inefficace.", 14)
    a(8, 4, "Le texte de 2026 dit de ne pas y passer 30 secondes.", 14)
    a(8, 5, "On demande si la tête vient de naître.", 13)
    a(8, 5, "On demande si une traction douce a déjà été tentée.", 13)
    a(8, 5, "On note l'heure de la naissance de la tête.", 14)
    a(8, 6, "La tête est sortie et ne tourne pas.", 13)
    a(8, 6, "On cherche si la main peut entrer pour un bras postérieur.", 14)
    a(8, 6, "Après la sortie, on regarde le périnée pour une déchirure.", 4)
    a(8, 7, "Une épaule qui sort avec la traction douce n'est pas cette dystocie.", 13)
    a(8, 7, "Un tracé mauvais accélère la sortie. Il n'autorise pas le fond utérin.", 1)
    a(8, 8, "On nomme la manœuvre efficace et l'heure.", 14)
    a(8, 8, "On note une hémorragie et le degré d'une déchirure.", 13)
    a(8, 8, "On examine le bras de l'enfant après la naissance.", 13)
    a(8, 9, "Aucun examen ne précède la flexion des hanches.", 13)
    a(8, 9, "Le [[CTG]] se reprend dès que l'épaule est libre.", 1)
    a(8, 10, "Palier 1. Hanches fléchies, cuisses ramenées sur l'abdomen.", 13)
    a(8, 10, "Palier 2. Pression sus-pubienne, côté du dos fœtal, vers le bas et le côté.", 13)
    a(8, 10, "Palier 3. Si l'extérieur échoue : bras postérieur.", 14)
    a(8, 10, "On coupe le périnée seulement si la main ne peut pas entrer.", 14)
    a(8, 11, "La traction reste axiale, sans excès.", 13)
    a(8, 11, "On ne pousse jamais sur le fond utérin.", 13)
    a(8, 11, "On change de manœuvre dès qu'elle est inutile.", 14)
    a(8, 11, "Cas corrigé. Tête née, traction douce échouée. Hanches fléchies, puis pression. Pas le fond.", 13)
    a(8, 12, "Dire le nom à voix haute fait venir l'aide.", 14)
    a(8, 12, "On ne coupe pas si la main entre déjà.", 14)
    a(8, 13, "Définition et manœuvres externes : mars 2012.", 13)
    a(8, 13, "Ordre, voix haute, bras postérieur : texte de 2026.", 14)
    a(8, 13, "Incidence de 0,58 à 0,70 pour cent dans les grandes séries de 2012.", 13)
    a(8, 14, "Piège. Pousser sur le fond utérin.", 13)
    a(8, 14, "Piège. Tirer hors de l'axe.", 13)
    a(8, 14, "Piège. Rester sur la première manœuvre alors qu'elle a échoué.", 14)
    a(8, 14, "Piège. Couper le périnée alors que la main entre déjà.", 14)

    # ----- DX.9 procidence -----
    leads[9][1] = "Le cordon est devant la présentation. On fait naître."
    leads[9][2] = "Le taux suisse de la procidence n'est pas lu."
    leads[9][3] = "Le cordon comprimé se lit sur le tracé."
    leads[9][4] = "On relève la présentation. On ne repousse pas le cordon."
    leads[9][5] = "On demande l'heure de la rupture et si le cordon a été vu."
    leads[9][6] = "Le toucher sent le cordon. La main qui relève reste."
    leads[9][7] = "Un pied à côté du cordon change l'urgence, sans taux inventé."
    leads[9][8] = "On écrit cordon devant, classe du tracé, heure de l'appel."
    leads[9][9] = "Pas de volume vésical dans le dossier relu."
    leads[9][10] = "Relever, posture, arrêt de l'oxytocine, naissance."
    leads[9][11] = "On arrête l'oxytocine. On fait naître."
    leads[9][12] = "On dit le diagnostic à voix haute."
    leads[9][13] = "Relever, ne pas repousser, arrêter, faire naître."
    leads[9][14] = "Repousser le cordon est le piège."

    a(9, 1, "La procidence du cordon place le cordon devant la présentation, ou dans le vagin.", 1)
    a(9, 1, "Le cordon comprimé peut donner une décélération prolongée.", 1)
    a(9, 1, "Au-delà de 5 minutes, sous 80, avec variabilité faible, l'hypoxie aiguë est fréquente.", 1)
    a(9, 2, "Aucun taux suisse de procidence n'est dans les textes relus.", 1)
    a(9, 2, "On ne le fabrique pas.", 1)
    a(9, 3, "La compression baisse les échanges. Le tracé le montre.", 1)
    a(9, 3, "Relever la présentation diminue la compression en attendant la naissance.", 1)
    a(9, 3, "On ne repousse pas le cordon dans l'utérus.", 1)
    a(9, 4, "Dès le diagnostic, la main relève la présentation.", 1)
    a(9, 4, "La femme peut être mise en genu-pectorale ou en Trendelenburg.", 1)
    a(9, 4, "Ces postures ne remplacent pas la naissance.", 1)
    a(9, 4, "Aucun volume de liquide dans la vessie n'est archivé. On n'en écrit pas.", 1)
    a(9, 5, "On demande l'heure de la rupture.", 1)
    a(9, 5, "On demande si le cordon a été vu.", 1)
    a(9, 5, "On demande un siège ou un pied.", 3)
    a(9, 6, "Le toucher reconnaît le cordon, qu'il batte ou non.", 1)
    a(9, 6, "On laisse les doigts qui relèvent.", 1)
    a(9, 6, "On ne retire pas la main pour aller chercher un bilan.", 1)
    a(9, 6, "On vérifie que le capteur n'enregistre pas le pouls maternel.", 1)
    a(9, 7, "Même si le tracé est encore normal, on prépare la naissance.", 1)
    a(9, 7, "Une décélération prolongée impose la naissance immédiate.", 1)
    a(9, 7, "Un pied à côté du cordon confirme l'urgence, sans pourcentage.", 3)
    a(9, 8, "On écrit cordon devant la présentation, heure, et classe du tracé.", 1)
    a(9, 8, "On n'écrit pas un volume vésical.", 1)
    a(9, 9, "Le chapitre relu ne donne pas de volume à mettre dans la vessie.", 1)
    a(9, 9, "On n'en invente pas.", 1)
    a(9, 9, "Le [[CTG]] dit la gravité. Il ne retarde pas la main qui relève.", 1)
    a(9, 10, "Palier 1. Main qui relève la présentation.", 1)
    a(9, 10, "Palier 2. Genu-pectorale ou Trendelenburg, appel, arrêt de l'oxytocine.", 5)
    a(9, 10, "Palier 3. Naissance par la voie la plus rapide décidée sur place.", 1)
    a(9, 11, "L'information 22114 dit d'arrêter la perfusion dès la souffrance.", 5)
    a(9, 11, "On ne reprend pas l'oxytocine pour finir plus vite.", 5)
    a(9, 11, "Cas corrigé. Cordon au toucher après la rupture. Main qui relève, puis naissance.", 1)
    a(9, 12, "On dit le diagnostic à voix haute pour préparer la naissance.", 1)
    a(9, 12, "On ne pousse pas la présentation vers le bas.", 1)
    a(9, 13, "Relever, ne pas repousser, arrêter l'oxytocine, faire naître.", 5)
    a(9, 13, "Pas de volume vésical. Pas de taux inventé.", 1)
    a(9, 14, "Piège. Repousser le cordon.", 1)
    a(9, 14, "Piège. Retirer la main qui relève pour aller écrire.", 1)
    a(9, 14, "Piège. Continuer l'oxytocine.", 5)
    a(9, 14, "Piège. Remplir la vessie d'un volume absent du dossier.", 1)

    # ----- DX.10 rupture utérine -----
    leads[10][1] = "Douleur continue, contractions qui cessent, tracé mauvais, tête qui remonte."
    leads[10][2] = "Le taux suisse de la rupture n'est pas lu."
    leads[10][3] = "Angusta est contre-indiqué sur une cicatrice utérine."
    leads[10][4] = "On arrête l'oxytocine. On prépare la laparotomie."
    leads[10][5] = "On demande une césarienne et une douleur qui a changé."
    leads[10][6] = "Les contractions se perdent. La présentation peut remonter."
    leads[10][7] = "Une hypertonie qui cède n'est pas une rupture prouvée."
    leads[10][8] = "On écrit cicatrice, douleur, hauteur perdue, classe du tracé."
    leads[10][9] = "Un tracé pathologique ne se surveille pas une heure."
    leads[10][10] = "Arrêt de l'utérotonique, appel, laparotomie."
    leads[10][11] = "L'oxytocine s'arrête. Elle ne traite pas la rupture."
    leads[10][12] = "Pas d'Angusta sur un utérus déjà opéré."
    leads[10][13] = "Cicatrice, douleur continue, tête qui remonte, laparotomie."
    leads[10][14] = "Continuer la perfusion est le piège."

    a(10, 1, "La rupture utérine ouvre la paroi pendant le travail.", 5)
    a(10, 1, "Le texte relu ne donne pas un taux, même sur cicatrice.", 10)
    a(10, 1, "Angusta est contre-indiqué en cas de cicatrice utérine, information 67580.", 10)
    a(10, 1, "L'information 22114 dit d'arrêter la perfusion dès l'hypertonie ou la souffrance.", 5)
    a(10, 2, "Aucun taux suisse de rupture utérine n'est dans les textes relus.", 10)
    a(10, 2, "On ne le fabrique pas.", 10)
    a(10, 3, "La contraction pousse sur une zone déjà opérée.", 10)
    a(10, 3, "La douleur peut devenir continue, et les contractions cesser.", 5)
    a(10, 3, "La présentation peut remonter. Le tracé se dégrade.", 1)
    a(10, 4, "Douleur continue sur cicatrice, avec tracé pathologique : laparotomie.", 5)
    a(10, 4, "Arrêter la perfusion ne referme pas la paroi.", 5)
    a(10, 4, "Une décélération de plus de 5 minutes, sous 80, signe souvent l'hypoxie aiguë.", 1)
    a(10, 5, "On demande toute opération de l'utérus, dont la césarienne.", 10)
    a(10, 5, "On demande une douleur qui ne ressemble plus à la contraction.", 5)
    a(10, 5, "On demande si Angusta ou l'oxytocine sont en cours.", 10)
    a(10, 6, "L'utérus peut cesser de se contracter.", 5)
    a(10, 6, "La présentation peut remonter au toucher.", 1)
    a(10, 6, "Le saignement peut être interne, avec un choc.", 2)
    a(10, 6, "L'index de choc au-dessus de 0,9 se calcule si la tension est prise.", 2)
    a(10, 7, "Une hypertonie qui cède à l'arrêt de l'oxytocine n'est pas une rupture prouvée.", 5)
    a(10, 7, "Douleur continue et présentation qui remonte : on ne reste pas sur l'hypertonie.", 1)
    a(10, 7, "Un utérus de bois oriente vers le décollement. La cicatrice oriente vers la rupture.", 12)
    a(10, 8, "On écrit cicatrice, perte des contractions, hauteur perdue, classe du tracé.", 1)
    a(10, 8, "On n'écrit pas un pourcentage après césarienne, absent du dossier.", 10)
    a(10, 9, "Un [[CTG]] pathologique impose une action immédiate.", 1)
    a(10, 9, "Le chapitre relu ne donne pas une heure d'observation.", 1)
    a(10, 10, "Palier 1. Arrêt de l'oxytocine et de l'utérotonique en cours.", 5)
    a(10, 10, "Palier 2. Appel et laparotomie si la paroi est en cause.", 5)
    a(10, 10, "Palier 3. Après l'enfant, le saignement du muscle suit l'information 22114.", 5)
    a(10, 11, "On n'augmente pas l'oxytocine devant une douleur continue et un tracé mauvais.", 5)
    a(10, 11, "Hors exception écrite, on ne dépasse pas 20 milli-U.I. par minute.", 5)
    a(10, 11, "L'exception lue vise un fœtus mort ou un terme plus précoce.", 5)
    a(10, 11, "Elle ne décrit pas une douleur de cicatrice.", 5)
    a(10, 11, "Cas corrigé. Cicatrice, douleur continue, tête qui remonte, bradycardie. Arrêt, laparotomie.", 5)
    a(10, 12, "Angusta est contre-indiqué sur une cicatrice utérine.", 10)
    a(10, 12, "On le dit avant d'ouvrir le blister.", 10)
    a(10, 12, "On ne le remplace pas par Cytotec, numéro 46945, contre-indiqué pendant la grossesse.", 11)
    a(10, 13, "Cicatrice, douleur continue, contractions perdues, présentation qui remonte, laparotomie.", 5)
    a(10, 13, "L'[[AIPS]] 22114 ne sert pas à pousser sur une paroi douteuse.", 5)
    a(10, 14, "Piège. Continuer ou augmenter l'oxytocine.", 5)
    a(10, 14, "Piège. Donner Angusta sur un utérus cicatriciel.", 10)
    a(10, 14, "Piège. Attendre devant un tracé sous 80.", 1)
    a(10, 14, "Piège. Appeler hypertonie simple une présentation qui remonte.", 5)

    return D, leads
