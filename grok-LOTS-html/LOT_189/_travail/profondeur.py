"""Phrases d'application, une par situation, sans nouveau seuil ni dose hors AIPS."""
from __future__ import annotations

import re

NOMS = [
    "la restriction de croissance fœtale",
    "la macrosomie fœtale",
    "l'oligoamnios",
    "l'hydramnios",
    "le tracé cardiaque fœtal suspect",
    "l'anémie fœtale par allo-immunisation",
    "la malformation structurale fœtale",
    "l'arythmie fœtale",
    "le syndrome transfuseur-transfusé",
    "la mort fœtale in utero",
]

MOMENTS = [
    "À l'arrivée",
    "Au contrôle du lendemain",
    "Avant le retour à domicile",
    "Avec le pédiatre",
    "Pendant le travail",
    "À la visite du terme",
    "Si les mouvements baissent",
    "Avant toute prescription",
    "Dans le compte rendu",
    "Au conseil des parents",
    "Si la mère est hypertendue",
    "Si les fœtus sont deux",
    "En garde",
    "Avant le transfert",
    "Après le Doppler",
    "Au staff",
    "Si un saignement apparaît",
    "Si la fièvre est là",
    "Avant l'anesthésie",
    "À la sortie",
]

GESTES = [
    [
        "confirme l'âge avant de lire un percentile",
        "réserve la taille seule au fœtus sous le 3e percentile",
        "ne conclut pas sur un poids seulement sous le 10e percentile",
        "vérifie l'absence d'anomalie congénitale avant d'appliquer le guide",
        "sépare la forme avant 32 semaines et la forme dès 32 semaines",
        "cherche un flux diastolique ombilical absent avant 32 semaines",
        "joint le Doppler au-dessus du 95e percentile au fœtus sous le 10e percentile",
        "exige deux des trois signes tardifs à partir de 32 semaines",
        "ne fixe pas la naissance sur le seul Doppler cérébral avant 32 semaines",
        "personnalise la décision de 24 semaines et 0 jour à 25 semaines et 6 jours",
        "propose l'extraction dès 26 semaines si les ralentissements spontanés se répètent",
        "tient un profil biophysique à 4 ou moins comme motif dès 26 semaines",
        "lit la variation courte dans la bande d'âge réelle",
        "retient la césarienne si le flux diastolique ombilical est absent ou inversé",
        "laisse Angusta de côté quand le motif d'extraction est déjà écrit",
        "appelle le pédiatre pour un poids estimé sous le 3e percentile",
        "cherche l'hypertension maternelle dans la forme précoce",
        "rappelle une récidive lue de 20 à 30 pour cent sans schéma d'aspirine",
    ],
    [
        "date la grossesse avant d'annoncer un percentile",
        "décrit un poids de naissance au-dessus du 90e percentile selon la thèse de 2015",
        "cite 4000 grammes comme repère de naissance et non comme ordre opératoire",
        "cite 4500 grammes comme repère de dystocie possible si la mère est diabétique",
        "rappelle que la thèse n'est pas une directive suisse de césarienne",
        "distingue le poids estimé du poids de naissance",
        "cherche un diabète dans l'histoire sans écrire d'insuline",
        "ne convertit pas le percentile en voie d'accouchement",
        "revoit le poids et le liquide à 40 semaines et 0 jour",
        "ne déclenche pas une grossesse simple normale de 37 semaines et 0 jour à 39 semaines et 6 jours",
        "peut discuter un déclenchement dès 39 semaines et 0 jour si la mère a plus de 40 ans",
        "palpe la présentation sans inventer un chiffre de bassin",
        "cherche une malformation si le liquide est aussi augmenté",
        "explique aux parents la marge d'erreur de l'estimation",
        "laisse Angusta de côté si l'état fœtal est déjà inquiétant",
        "ne traite pas une dystocie des épaules par un schéma de déclenchement",
    ],
    [
        "retient après le terme une poche verticale maximale inférieure à 3 cm",
        "retient aussi un index amniotique inférieur à 5 cm",
        "mesure une poche sans cordon et sans membre",
        "additionne la poche la plus profonde de chaque quadrant",
        "rappelle la baisse d'environ 33 pour cent par semaine après 37 semaines et 0 jour",
        "fait un cardiotocogramme de repos sans épreuve à l'ocytocine",
        "ne s'inquiète d'une résistance cérébrale basse près du terme que sous le 10e percentile",
        "réserve la poche inférieure à 2 cm au jumeau donneur",
        "écarte une rupture des membranes avant d'appeler le liquide chronique",
        "n'invente aucun chiffre de poche pour la rupture",
        "ne déclenche pas entre 37 semaines et 0 jour et 39 semaines et 6 jours si tout est normal",
        "refait la mesure si le premier cliché est douteux",
        "cherche une restriction associée sans confondre les deux mots",
        "programme l'échographie de liquide et de poids à 40 semaines et 0 jour",
        "écrit les centimètres et l'heure",
        "ne rassure pas sur un index normal si la poche profonde contient le cordon",
    ],
    [
        "retient en Europe une poche d'au moins 8 cm jusqu'à 20 semaines incluses",
        "retient une poche d'au moins 10 cm après 20 semaines",
        "regarde la poche du donneur avant de conclure sur le receveur",
        "mesure sans cordon et sans membre",
        "cherche une malformation à la morphologie",
        "cherche un gros fœtus sans confondre le poids et le liquide",
        "ouvre le classement de Quintero si la grossesse est monochoriale",
        "n'invente ni drainage ni médicament du liquide",
        "ne pose pas la restriction sur le seul liquide augmenté",
        "répète les deux poches toutes les deux semaines dès 16 semaines chez les monochoriaux",
        "explique la différence entre le repère de 8 cm et celui de 10 cm",
        "note le col sans lui prêter un chiffre non lu",
        "ne rassure pas une poche large sans regarder le cœur et la paroi",
        "distingue l'hydramnios isolé du syndrome transfuseur-transfusé",
        "écrit la chorionicité avant le mot hydramnios",
        "compare avec l'examen précédent et non avec le souvenir",
    ],
    [
        "rappelle que les chiffres lus sont ceux du travail du 30 septembre 2015",
        "garde après le terme le cardiotocogramme de repos sans épreuve à l'ocytocine",
        "tient pour normale une ligne de base de 110 à 160 bpm",
        "appelle tachycardie une ligne au-dessus de 160 bpm pendant plus de 10 minutes",
        "appelle bradycardie une ligne sous 110 bpm pendant plus de 10 minutes",
        "sait que 100 à 110 bpm peut se voir après le terme",
        "classe pathologique une ligne de base inférieure à 100 bpm",
        "tient pour normale une bande de 5 à 25 bpm",
        "appelle réduite une bande sous 5 bpm pendant plus de 50 minutes",
        "appelle prolongé un ralentissement de plus de 3 minutes",
        "agit si le ralentissement dépasse 5 minutes avec un rythme sous 80 bpm et une bande réduite",
        "cherche une anémie devant une onde sinusoïdale lisse de plus de 30 minutes",
        "dit répétés les ralentissements qui suivent plus de la moitié des contractions",
        "relit le tracé au moins toutes les 30 minutes pendant le travail",
        "prend le pouls maternel pour ne pas enregistrer la mère",
        "extrait sans délai devant une procidence, une rupture utérine ou un décollement",
        "corrige une hypotension ou une hypercinésie si le tableau est seulement suspect",
        "laisse Angusta de côté si le test de réactivité est en échec",
    ],
    [
        "propose le génotype RhD entre 16 et 24 semaines à toute femme RhD négatif",
        "rappelle la sensibilité lue de 99,82 pour cent à partir de 16 semaines",
        "ne fait pas du test dès 12 semaines une recommandation de l'avis",
        "donne 300 µg entre 28 et 30 semaines si le fœtus est RhD positif et l'indication est retenue",
        "n'injecte pas d'anti-D systématique si le fœtus est RhD négatif",
        "ajoute 10 µg pour 0,5 ml d'érythrocytes fœtaux si l'hémorragie est excessive",
        "ajoute 300 µg si le test manque et qu'une hémorragie excessive n'est pas exclue",
        "compte les globules par Kleihauer ou par cytométrie",
        "recueille le consentement écrit avant le génotypage",
        "ne transforme pas le pic gémellaire de 1,5 multiples en calendrier de transfusion du singleton",
        "cherche une anémie si le tracé est sinusoïdal",
        "range la maladie hémolytique parmi les transferts relatifs du 23 février 2022",
        "sépare la prophylaxie et le traitement d'un fœtus déjà anémique",
        "vérifie le groupe avant un geste invasif",
        "injecte dès que possible si le besoin n'est vu qu'après 30 semaines",
        "écrit le résultat RhD à côté de la date d'injection",
    ],
    [
        "place l'échographie de 11 semaines et 0 jour à 14 semaines et 0 jour",
        "date avec la meilleure longueur cranio-caudale entre 45 et 84 mm",
        "oriente vers un prélèvement si la clarté nucale dépasse 3,5 mm",
        "cite une détection lue de 99,7 pour cent des trisomies 21",
        "cite 97,9 pour cent et 99,0 pour cent pour les trisomies 18 et 13",
        "regarde l'activité, le situs, l'axe de 30 à 60 degrés et les quatre cavités",
        "définit la régurgitation tricuspide par un flux au-dessus de 60 cm/s sur plus de la moitié du cycle",
        "sait la clarté nucale augmentée dans jusqu'à 40 pour cent des cardiopathies majeures",
        "programme la morphologie vers 20 semaines",
        "transfère si la malformation exige une prise en charge spécialisée",
        "n'applique pas la définition de restriction quand une anomalie congénitale est présente",
        "cite 3,8 pour cent et 3,1 pour cent comme ordres de perte après geste invasif gémellaire",
        "ne présente pas ces ordres comme le risque local du jour",
        "décrit la coupe obtenue et ce qui n'a pas été vu",
        "garde un conseil non directif",
        "n'invente pas de voie d'accouchement selon le seul type de malformation",
    ],
    [
        "type le rythme avant de parler de souffrance",
        "reconnaît une tachycardie au-dessus de 160 bpm pendant plus de 10 minutes",
        "reconnaît une bradycardie sous 110 bpm pendant plus de 10 minutes",
        "classe pathologique la ligne de base sous 100 bpm",
        "écarte la fièvre maternelle avant de conclure",
        "écarte l'effet d'un bêta-stimulant",
        "prend le pouls maternel en même temps que le tracé",
        "demande une coupe qui sépare oreillette et ventricule",
        "cite la tachycardie supraventriculaire et le flutter parmi les causes lues",
        "cite le bloc auriculo-ventriculaire parmi les causes de bradycardie",
        "range l'arythmie parmi les transferts relatifs du 23 février 2022",
        "n'écrit aucune dose d'antiarythmique",
        "fait monter l'urgence si un hydrops apparaît sans décompte d'épanchements inventé",
        "oriente un tracé sinusoïdal vers l'anémie",
        "n'administre pas Angusta si l'état fœtal est inquiétant",
        "hospitalise un rythme soutenu selon le transfert relatif déjà cité",
    ],
    [
        "exige une grossesse monochoriale avant de poser le syndrome",
        "retient une poche de donneur inférieure à 2 cm",
        "retient une poche de receveur supérieure à 8 cm",
        "ne rend pas la discordance de poids obligatoire",
        "décrit le stade 1 par la vessie du donneur encore visible",
        "décrit le stade 2 par la vessie du donneur absente",
        "décrit le stade 3 par le Doppler critique",
        "décrit le stade 4 par l'hydrops",
        "décrit le stade 5 par la mort d'un fœtus ou des deux",
        "retient le laser comme traitement de choix à partir du stade 2",
        "discute la surveillance ou le laser au stade 1",
        "n'accepte les drainages répétés après 26 semaines que si le laser manque",
        "rappelle une mortalité pouvant aller jusqu'à 90 pour cent sans traitement",
        "rappelle une survie des deux fœtus de 60 à 70 pour cent après laser",
        "commence la surveillance à 16 semaines puis toutes les deux semaines",
        "ne pose pas le diagnostic sur une grossesse bichoriale",
        "évalue le pic cérébral du survivant après la mort d'un jumeau",
        "ne fait pas naître d'emblée le survivant prématuré",
        "décrit le stade anténatal 1 de l'anémie-polyglobulie par un pic de donneur au-dessus de 1,5 multiples",
        "retient une différence d'hémoglobine supérieure à 8 g/dl comme stade postnatal 1",
        "retient une différence d'hémoglobine supérieure à 11 g/dl comme stade postnatal 2",
        "retient une différence d'hémoglobine supérieure à 14 g/dl comme stade postnatal 3",
        "retient une différence d'hémoglobine supérieure à 17 g/dl comme stade postnatal 4",
        "retient une différence d'hémoglobine supérieure à 20 g/dl comme stade postnatal 5",
    ],
    [
        "confirme l'absence d'activité cardiaque à l'échographie",
        "ne se fie pas au seul arrêt ressenti des mouvements",
        "cite la prévalence après 22 semaines entre 3,2 et 4,4 pour 1000",
        "respecte le souhait de la femme si elle est stable et sans coagulation disséminée",
        "autorise un retour à domicile dans ces mêmes conditions",
        "préfère la voie vaginale hors urgence vitale maternelle",
        "demande d'emblée le Kleihauer et les agglutinines irrégulières",
        "demande l'hémostase s'il y a un hématome rétroplacentaire, une hypertension ou un sepsis",
        "prélève la face fœtale du placenta après la naissance",
        "cite une anomalie génétique dans 7,2 à 18,5 pour cent des séries lues",
        "discute le cytomégalovirus et le parvovirus selon le contexte",
        "réserve 600 mg par jour pendant deux jours à l'indication suisse de Mifegyne",
        "ne recopie pas le schéma français qui n'est pas cette ligne",
        "rappelle qu'Angusta est contre-indiqué pour un fœtus vivant dont l'état inquiète",
        "limite un usage d'Angusta dans son indication à 25 µg toutes les 2 heures ou à 50 µg toutes les 4 heures",
        "attend 4 heures après Angusta avant une autre méthode et ne l'associe pas à l'ocytocine",
        "ne prescrit pas un tracé à la grossesse suivante au seul motif de l'antécédent",
        "vérifie le groupe RhD parce que la mort in utero peut relever de l'anti-D",
    ],
]

RECITS = [
    [
        "Cas corrigé. Une femme à 29 semaines a un poids estimé au 8e percentile et un Doppler encore normal.",
        "On ne nomme pas encore la restriction, parce que le 3e percentile est respecté et qu'un second critère manque.",
        "Le contrôle écrit la bande d'âge et ne lui emprunte pas le seuil d'une bande plus tardive.",
        "Deux semaines plus tard, le flux diastolique ombilical disparaît.",
        "Le dossier retient alors le critère solitaire d'avant 32 semaines et appelle le niveau de néonatologie.",
        "On n'écrit pas Angusta, parce que l'état fœtal a déjà fourni un motif de surveillance hospitalière.",
        "La variation courte est lue avec le chiffre de la bande 29 à 31 semaines, soit 3,0 ms.",
        "La mère est prise la tension, car la forme précoce s'associe souvent à une pré-éclampsie.",
        "Le compte rendu sépare le percentile, le Doppler et l'heure prévue de la prochaine lecture.",
    ],
    [
        "Cas corrigé. L'estimation à 38 semaines annonce un poids au-dessus du 90e percentile.",
        "On date d'abord la grossesse et l'on dit que l'estimation n'est pas le poids de naissance.",
        "Le repère de 4000 grammes est expliqué comme un chiffre de la thèse de 2015, pas comme une césarienne obligatoire.",
        "On cherche un diabète dans l'histoire sans recopier une insuline qui n'est pas dans les textes ouverts.",
        "La présentation est palpée et le liquide est mesuré à part.",
        "Aucun déclenchement n'est posé pour une grossesse simple encore normale avant 39 semaines et 6 jours.",
        "Si la mère a plus de 40 ans, la directive de 2014 permet d'en parler dès 39 semaines et 0 jour.",
        "Le compte rendu refuse de transformer 4500 grammes en ordre opératoire.",
    ],
    [
        "Cas corrigé. À 41 semaines, la poche verticale maximale mesure moins de 3 cm et ne contient ni cordon ni membre.",
        "L'index est aussi inférieur à 5 cm, donc les deux définitions suisses de 2014 sont réunies.",
        "On écarte d'abord une rupture des membranes par l'histoire et l'examen, sans inventer un chiffre de rupture.",
        "Le cardiotocogramme est un tracé de repos, sans épreuve à l'ocytocine.",
        "On ne rassure pas en disant que la baisse de liquide après 37 semaines est toujours anodine.",
        "La poche de 2 cm du jumeau donneur n'est pas utilisée pour ce singleton.",
        "Le poids est revu en même temps, parce que l'échographie de 40 semaines et 0 jour cherche aussi un retard.",
        "La suite est datée par écrit.",
    ],
    [
        "Cas corrigé. À 22 semaines, une poche mesure 11 cm.",
        "Le seuil européen après 20 semaines est atteint, donc on ne parle pas d'un liquide simplement confortable.",
        "On cherche une malformation, un gros fœtus et, s'ils sont deux, la poche de l'autre.",
        "La grossesse est bichoriale, donc on ne pose pas le syndrome transfuseur-transfusé.",
        "Aucun drainage n'est inventé.",
        "Le contrôle suivant a une date, et la morphologie est relue si elle est incomplète.",
        "On explique aux parents la différence avec le repère de 8 cm d'avant 20 semaines.",
    ],
    [
        "Cas corrigé. En travail, la ligne de base est à 170 bpm depuis 20 minutes et la mère a 38,6 degrés.",
        "On prend d'abord le pouls maternel, puis on traite la fièvre, cause la plus fréquente.",
        "Le tableau n'est pas appelé pathologique sur la seule tachycardie si la variabilité reste entre 5 et 25 bpm.",
        "On relit au plus tard 30 minutes plus tard.",
        "Un ralentissement qui dépasse 5 minutes, avec un rythme sous 80 bpm et une bande réduite, ferait agir tout de suite.",
        "Angusta n'est pas donné, le test de réactivité n'étant plus rassurant.",
        "Une procidence, une rupture utérine ou un décollement ne se surveillent pas.",
    ],
    [
        "Cas corrigé. Une femme RhD négatif est vue à 17 semaines.",
        "On propose le génotype fœtal, avec information et consentement écrit, et non un test dès 12 semaines.",
        "Le résultat est RhD positif.",
        "Entre 28 et 30 semaines, la prophylaxie lue est 300 µg si l'indication est retenue.",
        "Un saignement plus tard fait demander un Kleihauer avant d'ajouter 10 µg par 0,5 ml d'érythrocytes.",
        "On n'écrit pas un calendrier de transfusion à partir du seul pic gémellaire de 1,5 multiples.",
        "Un tracé sinusoïdal ferait chercher l'anémie et le transfert, pas une simple surveillance de cabinet.",
    ],
    [
        "Cas corrigé. À 12 semaines et 4 jours, la longueur cranio-caudale est de 62 mm et la clarté nucale de 4 mm.",
        "La clarté au-dessus de 3,5 mm ouvre le parcours de prélèvement décrit avant l'acide nucléique libre.",
        "Le cœur est regardé, activité, situs, axe et quatre cavités, et non déclaré normal par défaut.",
        "On ne range pas cette grossesse dans les critères de restriction, qui supposent l'absence d'anomalie.",
        "Le conseil dit ce qui est vu et ne choisit pas à la place des parents.",
        "Une malformation qui exige un plateau spécialisé est une indication absolue de transfert selon le texte du 23 février 2022.",
        "Aucun chiffre de césarienne lié au type de malformation n'est ajouté.",
    ],
    [
        "Cas corrigé. Le tracé montre 180 bpm depuis 15 minutes.",
        "On prend le pouls maternel et la température avant de parler de flutter.",
        "L'échographie sépare oreillette et ventricule.",
        "Aucune dose d'antiarythmique n'est écrite.",
        "Le transfert relatif du 23 février 2022 est cité.",
        "Un hydrops ferait monter l'urgence sans qu'on invente un nombre d'épanchements.",
        "Le comprimé Angusta est écarté tant que l'état fœtal inquiète.",
    ],
    [
        "Cas corrigé. À 18 semaines, deux fœtus monochoriaux ont des poches de 1 cm et de 9 cm.",
        "La vessie du donneur est encore vue, donc le stade 1 est écrit, avec les deux mesures.",
        "On ne saute pas au stade 5, même si le guide rappelle qu'un stade peut sauter.",
        "La surveillance rapprochée ou le laser se discutent, et le drainage ne remplace pas le laser disponible.",
        "Le pic cérébral est noté, parce que la séquence anémie-polyglobulie se cherche à part.",
        "Une grossesse bichoriale avec les mêmes poches n'aurait pas reçu ce nom.",
        "Les parents entendent les ordres de survie après laser, 60 à 70 pour cent pour les deux, sans promesse.",
    ],
    [
        "Cas corrigé. Les mouvements ont cessé depuis la veille.",
        "L'échographie confirme l'absence d'activité cardiaque, et l'annonce attend cette image.",
        "La mère est stable, sans saignement ni signe de coagulation disséminée.",
        "Le moment de l'induction suit son souhait, et un retour à domicile est possible.",
        "Le Kleihauer et les agglutinines sont demandés d'emblée.",
        "Mifegyne à 600 mg par jour pendant deux jours n'est écrit que dans l'indication où les prostaglandines ou l'ocytocine sont contre-indiquées.",
        "On ne promet pas un examen de la grossesse suivante réduit à un tracé systématique.",
    ],
]


def mots(texte: str) -> int:
    return len(re.findall(r"\b[\w'’]+\b", texte, re.U))


def completer(sac, n: int, cible: int) -> int:
    """Ajoute des applications jusqu'au budget, puis le cas. Retourne le nombre de phrases trop longues sautées."""
    refuses = 0
    nom = NOMS[n - 1]
    reserve = sum(len(t) for t in RECITS[n - 1]) + 400
    for moment in MOMENTS:
        for geste in GESTES[n - 1]:
            if sac.chars() >= cible - reserve:
                break
            phrase = f"{moment}, pour {nom}, on {geste}."
            if mots(phrase) > 34:
                refuses += 1
                continue
            sac.add(phrase, [1, 11, 6, 4, 3, 5, 8, 3, 4, 7][n - 1])
        if sac.chars() >= cible - reserve:
            break
    for phrase in RECITS[n - 1]:
        if mots(phrase) > 34:
            refuses += 1
            continue
        sac.add(phrase, [1, 11, 6, 4, 3, 5, 8, 3, 4, 7][n - 1])
    return refuses


def completer_phase(sac, cible: int) -> int:
    refuses = 0
    refs = [1, 11, 6, 4, 3, 5, 8, 3, 4, 7]
    cadres = [
        "Au tri, {moment}, pour {nom}, on {geste}",
        "Le dossier d'orientation, {moment}, pour {nom}, montre qu'on {geste}",
        "On explique, {moment}, que pour {nom} l'équipe {geste}",
    ]
    index = [(0, c, m, g) for c in range(3) for m in range(len(MOMENTS)) for g in range(18)]
    # round-robin sur les dix tableaux
    curseurs = [0] * 10
    progres = True
    while sac.chars() < cible and progres:
        progres = False
        for i in range(10):
            if sac.chars() >= cible:
                break
            gestes = GESTES[i]
            while curseurs[i] < len(cadres) * len(MOMENTS) * len(gestes):
                k = curseurs[i]
                curseurs[i] += 1
                n_g = len(gestes)
                n_m = len(MOMENTS)
                g = k % n_g
                m = (k // n_g) % n_m
                c = (k // (n_g * n_m)) % len(cadres)
                if c > 2:
                    break
                phrase = cadres[c].format(moment=MOMENTS[m].lower(), nom=NOMS[i], geste=gestes[g])
                if mots(phrase) > 34:
                    refuses += 1
                    continue
                sac.add(phrase, refs[i])
                progres = True
                break
    return refuses
