# -*- coding: utf-8 -*-
"""Compléments sourcés pour atteindre un cours utilisable, sans remplissage vide."""
from gen_lot208_b import block, p, table, td


def windows(title, items):
    parts = [f"<div style='margin:16px 0 10px;'><strong>{title}</strong><br>"]
    for i, paras in enumerate(items, 1):
        parts.append(block(f"{title} — {i}", "".join(p(x) for x in paras)))
    parts.append("</div>")
    return "".join(parts)


def plus_dx5():
    items = []
    bandes = [
        ("moins de 50 ans", "moins de 2,5 %", "faible à modéré", "Le médicament n'est pas la règle, sauf modificateur ou bénéfice vie entière substantiel."),
        ("moins de 50 ans", "2,5 % à moins de 7,5 %", "élevé", "Le traitement des facteurs s'envisage avec les modificateurs, le bénéfice et la préférence."),
        ("moins de 50 ans", "au moins 7,5 %", "très élevé", "L'ESC recommande le traitement des facteurs, parce que ce chiffre annonce un risque vie entière haut."),
        ("50 à 69 ans", "moins de 5 %", "faible à modéré", "Le seuil de 2,5 % appartient à la tranche précédente. Il ne voyage pas avec l'âge."),
        ("50 à 69 ans", "5 % à moins de 10 %", "élevé", "La décision se prend près du seuil, avec les modificateurs."),
        ("50 à 69 ans", "au moins 10 %", "très élevé", "Le traitement des facteurs est recommandé dans cette catégorie."),
        ("70 ans et plus", "moins de 7,5 %", "faible à modéré", "SCORE2-OP remplace SCORE2, et AGLA le dit explicitement."),
        ("70 ans et plus", "7,5 % à moins de 15 %", "élevé", "La fragilité et les médicaments déjà présents pèsent autant que le pourcentage."),
        ("70 ans et plus", "au moins 15 %", "très élevé", "Même alors, l'hypolipémiant du sujet âgé apparemment sain reste, dans l'ESC, une recommandation de classe IIb que le médecin ne transforme pas en automatisme."),
    ]
    for age, band, cat, cond in bandes:
        items.append([
            f"La personne appartient à la tranche « {age} ».",
            f"L'outil valide pour la Suisse, pays à faible risque, rend un risque à dix ans {band}.",
            f"La page AGLA et le texte ESC placent alors la catégorie « {cat} ».",
            cond,
            "La tranche d'âge s'écrit à côté du pourcentage. Sans elle, le seuil est celui d'une autre vie.",
            "Ce pourcentage ne se calcule pas de tête lorsque les lipides ne sont pas sous les yeux.",
        ])
    outils = [
        ("AGLA, personnes saines", "L'âge va de 20 à 69 ans, et le diabète est absent.", "Le résultat est un événement coronarien fatal ou un infarctus non fatal à dix ans.", "Les champs lus sont la pression systolique, le LDL, le HDL et les triglycérides.", "À partir de 70 ans, la page renvoie vers SCORE2-OP."),
        ("SCORE2", "L'âge va de 40 à 69 ans chez une personne apparemment saine et non diabétique.", "Le résultat ajoute l'accident vasculaire cérébral et les événements non fatals.", "La Suisse se lit sur l'abaque à faible risque, avec la liste des pays que l'ESC publie.", "Un modèle d'une région à haut risque surestimerait le même profil."),
        ("SCORE2-OP", "Il commence à 70 ans.", "Il tient compte de la mortalité concurrente, ce que le score des adultes d'âge moyen ne fait pas.", "Les seuils montent : 7,5 % et 15 %.", "Le bénéfice en années sans événement se raccourcit."),
        ("SCORE2-Diabète", "Il concerne le diabète de type 2 de 40 à 69 ans, sans maladie athéromateuse établie ni atteinte d'organe qui classerait déjà.", "Le calculateur des personnes saines est alors une erreur.", "La page AGLA décrit l'atteinte sévère par le DFGe, l'albuminurie et l'atteinte microvasculaire multiple.", "Cette définition se lit avant toute reassurance."),
    ]
    for nom, a, b, c, d in outils:
        items.append([
            f"L'outil discuté est {nom}.",
            a, b, c, d,
            "Le nom de l'outil voyage avec le pourcentage, dans la même phrase.",
        ])
    pieges = [
        "Le candidat récite un risque relatif et oublie la base. La bonne copie dit que l'ESC refuse de traduire un risque relatif directement en décision.",
        "Le candidat rassure un fumeur de 38 ans. La bonne copie dit que, avant 40 ans, la prédiction est imprécise et que le mode de vie prime, sauf hypercholestérolémie familiale ou trouble tensionnel spécifique.",
        "Le candidat applique 10 % et 20 % à tout âge. La bonne copie ouvre la page AGLA du 24.10.2026 et lit les seuils par tranche.",
        "Le candidat multiplie par 1,3 parce que la personne est originaire d'Inde. La bonne copie rappelle que ces coefficients viennent de QRISK3 au Royaume-Uni et que l'ESC demande idéalement un rapport propre au pays.",
        "Le candidat demande un scanner pour préciser le risque vie entière. La bonne copie réserve le calcium au DX.6 et au voisinage d'un seuil.",
        "Le candidat calcule SCORE2 chez un patient déjà stenté. La bonne copie passe en prévention secondaire.",
        "Le candidat promet un nombre d'années gagnées sans avoir ouvert le calculateur. La bonne copie dit que l'ESC propose ces estimateurs, et que le chiffre individuel se lit dedans.",
        "Le candidat traite un LDL isolé chez une femme de 42 ans à bas risque. La bonne copie exige la catégorie et les modificateurs.",
        "Le candidat ignore une prééclampsie ancienne. La bonne copie la compte parmi les modificateurs que le score n'ingère pas.",
        "Le candidat donne une dose de statine. La bonne copie refuse, parce que l'information professionnelle n'est pas dans ce fichier.",
    ]
    for q in pieges:
        items.append([
            "Question de copie.",
            q,
            "La réponse cite la source lue, et elle distingue ce qui a été ouvert de ce qui ne l'a pas été.",
            "Une dose, un seuil Agatston de 100 ou un pourcentage non calculé font perdre les points.",
        ])
    return windows("Lecture appliquée du risque vie entière", items)


def plus_dx6():
    items = []
    scenes = [
        ("Le risque calculé est déjà très élevé.", "Le scanner ne change pas la décision de traiter les facteurs.", "Ce refus s'explique. On ne cède pas à l'image."),
        ("Le risque calculé est clairement bas, sans modificateur.", "Un calcium inattendu pourrait théoriquement monter le risque, mais l'ESC concentre l'examen autour des seuils, pour des raisons de faisabilité.", "On ne dépiste pas toute la patientèle."),
        ("Le risque est au seuil et la personne ne veut pas de rayons.", "Le refus s'accepte, et la décision se prend avec les données cliniques.", "La plaque carotidienne peut s'envisager si elle change encore quelque chose."),
        ("Le score revient plus haut que l'attendu pour l'âge.", "Le risque calculé augmente.", "La discussion du traitement des facteurs reprend, sans dose inventée."),
        ("Le score revient nul chez un fumeur de 52 ans.", "L'ESC rappelle qu'une plaque molle peut exister malgré ce zéro.", "Aucun certificat de cœur sain ne sort de ce zéro."),
        ("La personne décrit une oppression à la marche.", "Ce n'est plus un examen de prévention.", "La filière de la douleur s'ouvre le jour même."),
        ("La personne a un diabète de type 2.", "La page AGLA dit que la preuve est insuffisante pour utiliser le score calcique afin de classer ce diabète.", "On ne s'appuie pas dessus."),
        ("La personne est enceinte.", "Tout scanner se diffère.", "Le risque vie entière se commente sans image."),
        ("Le radiologue rend seulement un nombre d'Agatston.", "On redemande la comparaison à l'âge et au sexe, parce que l'ESC lit le résultat ainsi.", "Le seuil américain de 100 ne se plaque pas."),
        ("La page EAS affiche une classe IIa.", "Le guide de prévention 2021, ouvert en texte, dit IIb.", "Le cours ne fait pas passer la page web pour une abrogation du guide tant qu'une mise à jour complète n'a pas été lue."),
    ]
    for a, b, c in scenes:
        items.append([a, b, c, "La phrase de conclusion est écrite dans le dossier, avec le nom de l'examen et la décision qu'il change ou qu'il ne change pas.", "Source de raisonnement : [S501] et, pour le diabète, [S505]."])
    return windows("Décisions autour du score calcique", items)


def plus_dx7():
    # calculs dérivés : 1 verre = 10 g, lu dans Obsan (20 g = 2 verres).
    cas = [
        ("Une femme boit 3 verres standard chaque jour.", "3 fois 10 g font 30 g.", "30 g se situent dans la bande 20 à 40 g, donc dans le risque chronique moyen d'Obsan.", "Ce n'est pas une quantité que l'OFSP présente comme protectrice."),
        ("Une femme boit 5 verres standard chaque jour.", "5 fois 10 g font 50 g.", "50 g dépassent 40 g, donc le risque chronique est élevé.", "L'intervention ne se limite pas à un conseil vague."),
        ("Un homme boit 5 verres standard chaque jour.", "5 fois 10 g font 50 g.", "50 g se situent dans la bande 40 à 60 g, donc dans le risque chronique moyen masculin.", "La même quantité chez une femme serait déjà un risque élevé."),
        ("Un homme boit 7 verres standard chaque jour.", "7 fois 10 g font 70 g.", "70 g dépassent 60 g, donc le risque chronique masculin est élevé.", "Les signes de dépendance se cherchent dans la même consultation."),
        ("Un homme de 22 ans boit 6 verres un samedi et rien en semaine.", "Six verres dépassent le seuil épisodique masculin de 5 verres.", "L'OFSP demande au moins une fois par mois pour qualifier l'épisode à risque.", "S'il le fait chaque samedi, le critère est rempli, et 35 % des hommes de 20 à 24 ans sont dans cette zone."),
        ("Une femme boit 4 verres lors d'un dîner mensuel.", "Quatre verres atteignent le seuil épisodique féminin.", "Le risque chronique peut rester bas si les autres jours sont à zéro.", "Les deux risques se documentent séparément."),
        ("Une personne de 70 ans boit un verre chaque soir et dit que c'est bon pour le cœur.", "21,4 % des plus de 65 ans boivent chaque jour.", "L'OFSP ne retient pas le bénéfice cardiovasculaire des études anciennes.", "Les chutes et les médicaments sédatifs se cherchent avant le discours."),
        ("Une femme enceinte a bu deux verres avant de savoir.", "L'OFSP place la grossesse parmi les situations inappropriées.", "On n'accuse pas. On ouvre l'accompagnement et l'arrêt.", "Aucun seuil résiduel « sans danger » ne s'invente."),
    ]
    items = []
    for a, b, c, d in cas:
        items.append([
            a,
            b + " Ce produit est un calcul dérivé de l'équivalence Obsan, 20 g pour 2 verres.",
            c,
            d,
            "Le calcul se refait si le verre réel n'est pas un verre standard. On fait alors estimer le volume.",
        ])
    items.append([
        "Repère de mortalité à ne pas moderniser sans source.",
        "L'OFSP attribue 1 553 décès en 2017, entre 15 et 74 ans, et non un chiffre de 2026.",
        "Parmi ces décès, 36 % sont des cancers, 21 % des troubles digestifs et hépatiques, et 21 % des blessures.",
        "Environ 10 % des décès masculins et environ 5 % des décès féminins de la période sont liés à l'alcool, selon la même page.",
        "Le candidat qui invente une baisse linéaire jusqu'en 2026 perd les points.",
    ])
    items.append([
        "Repère de coût.",
        "Les coûts directs de santé cités sont 447 millions de francs en 2017 et 513 millions dans l'étude 2022 que l'OFSP mentionne.",
        "Le coût social d'environ 2,8 milliards inclut 2,1 milliards de productivité et 215 millions de poursuites.",
        "Ces sommes décrivent le pays. Elles ne se divisent pas par le patient assis en face du médecin.",
        "Source : [S507].",
    ])
    return windows("Calculs dérivés et repères OFSP sur l'alcool", items)


def plus_dx8():
    items = [
        [
            "La question d'entretien se pose avec des verbes, pas avec une liste morte.",
            "On demande si le travail, l'argent, la famille, la solitude ou un événement récent pèsent.",
            "On demande ensuite si l'humeur a baissé et si des idées de mort sont présentes.",
            "On demande enfin si les médicaments vasculaires sont encore pris, parce que le stress casse l'observance.",
            "Source de la question : [S501].",
        ],
        [
            "Le risque relatif ne se transforme pas en destin.",
            "Un risque relatif entre 1,2 et 2,0 décrit des groupes, dans les travaux que l'ESC résume.",
            "Le bas revenu est associé à la mortalité cardiovasculaire avec un risque relatif de 1,76, intervalle 1,45 à 2,14.",
            "On dit « association ». On ne dit pas « vous avez 76 % de risque en plus » comme si c'était son SCORE2.",
            "Près d'un seuil seulement, il en tient compte dans la décision partagée.",
        ],
        [
            "L'épuisement vital n'est pas chaque fatigue.",
            "L'ESC dit que, parmi les marqueurs psychosociaux, seul l'épuisement vital a amélioré la reclassification.",
            "Une contrariété ponctuelle ne reçoit donc pas le même statut mathématique.",
            "Elle peut quand même justifier une aide, parce que le soin ne se limite pas à la reclassification.",
            "Les deux phrases restent séparées : l'aide d'un côté, la reclassification de l'autre.",
        ],
        [
            "Oppression thoracique : les deux hypothèses restent ouvertes.",
            "Au moins une personne sur cinq, dit l'ESC, porte un trouble psychique souvent exprimé par le corps.",
            "Ce fait ne blanchit pas une douleur d'effort.",
            "L'électrocardiogramme et la filière habituelle restent indiqués lorsque la clinique est évocatrice.",
            "Le candidat qui choisit un seul des deux diagnostics échoue.",
        ],
        [
            "Aucune dose psychotrope n'est licite dans ce fichier.",
            "Un antidépresseur peut être le bon moyen plus tard.",
            "Son choix dépend de la grossesse, du cœur, du foie et du rein.",
            "Ces adaptations se lisent dans l'information professionnelle suisse, que cette rédaction n'a pas ouverte.",
            "La copie qui invente une dose est fausse, même si la classe est juste.",
        ],
    ]
    return windows("Entretien psychosocial utilisable en consultation", items)


def plus_dx9():
    items = [
        [
            "Le niveau de 300 Bq/m³ se traduit en décision, pas en slogan.",
            "Le niveau s'applique au local où l'on séjourne au moins quinze heures par semaine.",
            "Une buanderie traversée dix minutes par jour ne déclenche pas le même devoir qu'une chambre.",
            "Si cette buanderie devient une chambre, les délais du séjour prolongé s'appliquent.",
            "Source : lignes directrices du 2 février 2023 [S510].",
        ],
        [
            "Bande 300 à 600 Bq/m³, seule ligne du tableau 4 recopiée sans ambiguïté.",
            "Le séjour prolongé, au-delà de trente heures par semaine, laisse au plus dix ans.",
            "Le séjour court, de quinze à trente heures, laisse au plus trente ans.",
            "En dessous de quinze heures, les lignes directrices n'exigent pas de mesure pour ce local.",
            "Si une transformation majeure survient avant l'échéance, l'assainissement radon se fait en même temps.",
        ],
        [
            "Les autres cellules ne se récitent pas.",
            "Le PDF lu mélange, dans l'extraction, les délais au-dessus de 600 Bq/m³.",
            "Plutôt que d'inventer « un an » ou « trois ans » pour une cellule douteuse, il ouvre le tableau 4 officiel.",
            "Cette honnêteté est elle-même une réponse d'examen.",
            "Le dépassement de 1 000 Bq/m³ au poste de travail, lui, est clair : le poste est exposé, article 167.",
        ],
        [
            "Qui fait quoi, selon les articles cités par l'OFSP.",
            "L'article 155 fixe le cadre du niveau de référence dans les locaux occupés.",
            "L'article 158 confie en général l'exécution aux cantons.",
            "L'article 163 oblige le propriétaire ou le maître d'ouvrage du neuf et du transformé à viser moins de 300 Bq/m³ selon l'état de la technique.",
            "L'article 166 met l'assainissement à la charge du propriétaire, et permet au canton de l'ordonner.",
        ],
        [
            "Cancer du poumon et radon se disent dans le même entretien que le tabac.",
            "L'OFSP compte environ 3 200 décès par cancer du poumon, source OFS 2023, dont 200 à 300 imputés au radon par Menzler, 2005.",
            "200 à 300 ne se présentent pas comme une statistique de l'année 2026.",
            "Il dit la latence : des années ou des décennies.",
            "Il n'existe pas, dans les pages lues, de comprimé qui lave le radon.",
        ],
        [
            "Mesure ancienne.",
            "Une mesure d'avant 2018 peut rester dans la base et dépasser 300 Bq/m³.",
            "Si le séjour atteint quinze heures, les lignes directrices recommandent vivement une nouvelle mesure, ou un assainissement décidé par le propriétaire.",
            "On ne dit pas que l'ancienne limite de 1 000 Bq/m³ protège encore un logement.",
            "Source : [S510] et [S511].",
        ],
    ]
    return windows("Décisions radon que l'on peut défendre", items)


def plus_dx10():
    items = [
        [
            "Article 5, consentement.",
            "L'analyse n'a lieu que si la personne concernée a consenti de façon libre et expresse, après information suffisante.",
            "Elle peut révoquer ce consentement à tout moment.",
            "Si elle est incapable de discernement, le représentant consent, et elle est associée autant que possible.",
            "Un prélèvement « pendant qu'elle réfléchit » viole cet article.",
        ],
        [
            "Article 6, information minimale.",
            "Le but, le type et la pertinence de l'analyse s'expliquent avant le reste.",
            "Il explique les risques physiques et psychiques, le sort des échantillons et des données, et la possibilité d'informations excédentaires.",
            "Il dit dans quels cas ces informations ne peuvent pas être communiquées.",
            "Il dit l'importance possible pour la famille, le droit familial de ne pas savoir, et les droits de consentir, de savoir et de refuser.",
        ],
        [
            "Articles 7, 8 et 9.",
            "Le résultat revient à la personne, et à personne d'autre sans son accord.",
            "Elle peut refuser tout ou partie des informations sur son patrimoine génétique, sans se justifier.",
            "Le PDF de l'OFSP de février 2025 ajoute que ce refus peut ne porter que sur les informations excédentaires, et que la famille a le même droit.",
            "L'article 9 demande d'éviter autant que possible de produire ces informations excédentaires.",
        ],
        [
            "Article 20, qui a le droit de prescrire.",
            "Le prescripteur est un médecin habilité à exercer sous sa propre responsabilité.",
            "Il possède un titre postgrade fédéral dans le domaine de l'analyse, ou une qualification particulière en génétique humaine.",
            "Le Conseil fédéral peut restreindre ou élargir ce droit. Le cours ne devine pas les exceptions non lues.",
            "Un test commandé sur internet par le patient ne devient pas légitime parce que le médecin le commente après coup sans cadre.",
        ],
        [
            "Article 21, le cœur de l'examen.",
            "Pour une analyse diagnostique, la personne doit pouvoir bénéficier d'un conseil avant et après.",
            "Pour une analyse présymptomatique, prénatale ou de planning familial, elle bénéficie de ce conseil. La différence de verbe compte.",
            "Le conseil est non directif, qualifié, individuel et familial, consigné, et il ignore l'intérêt général de la société.",
            "Un délai adéquat sépare le conseil du prélèvement.",
        ],
        [
            "Contenu obligatoire du conseil, alinéa 3.",
            "Le conseiller dit la fréquence et la nature de l'anomalie.",
            "Il dit les conséquences médicales, psychiques et sociales du test et du refus.",
            "Il dit les coûts, l'importance de l'anomalie, les mesures possibles et les soutiens.",
            "Il dit dans quelles conditions les assurances peuvent demander les données.",
        ],
        [
            "Article 22 et grossesse.",
            "La femme est informée de son autodétermination avant et après l'analyse prénatale.",
            "S'il est probable qu'aucun traitement ne suivra, elle en est avertie.",
            "Si elle envisage une interruption, elle entend aussi les autres issues et l'existence d'associations.",
            "Le partenaire est associé si c'est possible. La note Fedlex date une modification au 1er août 2025.",
        ],
        [
            "Ce que l'histoire familiale ne fait pas.",
            "Avant 55 ans chez l'homme et avant 60 ans chez la femme, la page EAS déclenche l'évaluation.",
            "L'ESC dit que cette histoire n'améliore que marginalement la prédiction au-delà des facteurs classiques.",
            "Elle ne justifie pas un score polygénique de routine, classe III dans le tableau de prévention 2021.",
            "Elle ne justifie pas non plus de sauter le conseil lorsque le test devient présymptomatique.",
        ],
        [
            "Hypercholestérolémie familiale, pont avec AGLA.",
            "Sans facteur majeur additionnel, la page AGLA la place en risque élevé.",
            "Avec un facteur majeur additionnel, elle la place en risque très élevé.",
            "Le calculateur des personnes saines ne sert pas à adoucir ce classement.",
            "La dose du médicament se lira plus tard dans l'information professionnelle.",
        ],
    ]
    return windows("LAGH article par article, telle que lue le 24.10.2026", items)


def oraux(title, pairs):
    facons = [
        "Au milieu de la consultation, presque en passant, quelqu'un glisse : « {q} ».",
        "L'examinateur pose cela comme une évidence, et c'est là que la phrase dérape : « {q} ».",
        "Le patient arrive avec son chiffre déjà fait, convaincu d'avoir compris : « {q} ».",
        "Entre deux portes, là où les raccourcis font le plus de mal, on entend : « {q} ».",
        "La question a l'air pratique. Elle économise une minute. La voici : « {q} ».",
    ]
    clotures = [
        (
            "On répond avec le texte lu le 24 octobre 2026, et la phrase s'arrête net où la page s'arrête.",
            "Une dose, un seuil venu d'ailleurs ou un pourcentage deviné ne viennent pas combler le blanc.",
            "Si la personne souffre, saigne, tient encore un volant ou parle de mourir, cette conversation cède aussitôt la place.",
        ),
        (
            "La réponse tient dans ce qui a été ouvert ce jour-là. Au-delà, on dit simplement qu'on ne sait pas.",
            "On ne bouche pas l'incertitude avec un chiffre appris dans un autre pays ou dans une autre année.",
            "La douleur, le sang, la route ou l'idée de mort interrompent la leçon avant qu'elle ne devienne un retard.",
        ),
        (
            "On rend la phrase au document, pas à la mémoire flatteuse.",
            "Rien ne s'invente pour faire joli : ni milligramme, ni coefficient importé, ni part de population absente de la source.",
            "Dès qu'un signe d'alarme apparaît, le commentaire se tait et les gestes de protection commencent.",
        ),
        (
            "Ce qui n'a pas été lu ne se récite pas. Le silence, ici, est une réponse juste.",
            "Le candidat qui complète le trou par une dose ou par un seuil célèbre perd la question, même si le début était bon.",
            "Une personne instable ne reste pas dans cet exercice : on la met en sécurité d'abord.",
        ),
        (
            "La copie s'arrête sur la dernière ligne réellement ouverte le 24 octobre 2026.",
            "Elle ne déguise pas une ignorance en précision, et elle ne transforme pas un risque de groupe en destin individuel.",
            "Souffrance actuelle, saignement, conduite imminente ou parole de mort : la consultation change de registre sans discuter.",
        ),
    ]
    items = []
    for i, (question, answer) in enumerate(pairs):
        phrase = answer if answer.endswith(".") else answer + "."
        a, b, c = clotures[i % len(clotures)]
        items.append([
            facons[i % len(facons)].format(q=question),
            phrase,
            a,
            b,
            c,
        ])
    return windows(title, items)


def plus_oraux():
    dx5 = [
        ("Mon application dit 3 %, je suis tranquille ?", "Trois pour cent ne veulent rien dire sans l'outil, l'âge et la région. Avant 50 ans, 2,5 à moins de 7,5 % est déjà un risque élevé."),
        ("Je n'ai que 36 ans, le cœur peut attendre.", "Avant 40 ans le chiffre à dix ans est imprécis. Le mode de vie compte maintenant, et une hypercholestérolémie familiale reste une exception."),
        ("Donnez-moi la statine de mon voisin.", "La catégorie se calcule d'abord. La dose se lira dans l'information professionnelle, qui n'est pas dans ce cours."),
        ("Je multiplie par 1,7 parce que mon père est pakistanais.", "Ce coefficient vient de données britanniques citées par l'ESC. Il ne se plaque pas sur un SCORE2 suisse sans rapport propre au pays."),
        ("Mon risque vie entière est un diagnostic.", "Non. C'est un horizon de communication. Le diagnostic, s'il existe, est celui de la maladie ou du facteur."),
        ("Depuis ma prééclampsie je suis comme avant.", "Le score ignore souvent cet antécédent. L'ESC le compte parmi les modificateurs, surtout près d'un seuil."),
        ("Je veux le scanner pour voir mon risque vie entière.", "Le scanner ne mesure pas cet horizon. Le calcium se discute seulement près d'un seuil de décision, au DX.6."),
        ("AGLA et SCORE2, c'est le même pourcentage.", "Non. AGLA prédit un événement coronarien fatal ou un infarctus non fatal. SCORE2 ajoute l'accident vasculaire et les événements non fatals."),
        ("La Suisse est un pays à haut risque européen.", "Non. L'ESC la liste parmi les pays à faible risque des abaques SCORE2."),
        ("À 72 ans je garde le même seuil que mon fils de 48 ans.", "Non. À partir de 70 ans, SCORE2-OP s'applique, et le risque très élevé commence à 15 %."),
        ("Mon diabète est léger, calculez comme si je n'en avais pas.", "Le calculateur des personnes saines exclut le diabète. La page AGLA ouvre une autre voie."),
        ("Mon DFGe est à 25, faites un score pour me rassurer.", "La page AGLA classe déjà cette fonction rénale en risque très élevé. Le score de personne saine ne l'adoucit pas."),
    ]
    dx6 = [
        ("Faites un score calcique à tous mes patients de 50 ans.", "Non. L'ESC le réserve au voisinage d'un seuil, en classe IIb."),
        ("Mon score est à 0, je peux fumer tranquille.", "Non. Une plaque molle peut exister, et le tabac reste un levier majeur."),
        ("Mon score est à 80, donc inférieur à 100, je suis bas risque.", "Le seuil de 100 n'est pas celui de l'ESC 2021. On compare à l'âge et au sexe."),
        ("J'ai mal à la marche, le score suffira.", "Non. Une douleur d'effort quitte la prévention et entre dans une filière diagnostique."),
        ("Mesurez mon intima-média pour décider.", "L'ESC ne recommande pas cette mesure isolée. La plaque carotidienne a une définition précise."),
        ("La page EAS dit IIa, donc oubliez le IIb.", "Les deux textes ont été lus. Le guide de prévention 2021 dit IIb. Une page web ne l'abroge pas sans mise à jour complète."),
        ("Je suis enceinte, faites le scanner quand même.", "Non. La décision préventive attend, et l'irradiation ne se justifie pas."),
        ("J'ai un diabète, le calcium classera mon risque.", "La page AGLA dit que la preuve est insuffisante pour cet usage dans le diabète de type 2."),
    ]
    dx7 = [
        ("Un verre de rouge protège mon cœur.", "L'OFSP ne retient pas ce bénéfice. Les anciennes études comparaient souvent à d'anciens buveurs déjà malades."),
        ("Je bois trois verres par jour, je suis une femme, est-ce haut ?", "Trois verres font environ 30 g, calcul dérivé. C'est un risque chronique moyen, entre 20 et 40 g, pas une zone sans danger."),
        ("Comme mon mari, cinq verres par jour, c'est pareil.", "Non. Chez lui, 50 g restent dans le risque moyen masculin. Chez vous, 50 g dépassent 40 g et le risque est élevé."),
        ("Je ne bois que le samedi, six verres.", "Chez un homme, cinq verres ou plus sur une occasion, au moins une fois par mois, définissent l'épisode à risque."),
        ("Mes gamma-GT sont normaux, donc tout va bien.", "Non. L'anamnèse en verres tranche. La biologie normale ne blanchit pas la quantité."),
        ("Donnez-moi la dose de naltrexone.", "Elle se lit dans l'information professionnelle suisse, qui n'a pas été ouverte pour ce fichier."),
        ("Combien de décès cette année ?", "La page OFSP donne 1 553 décès en 2017, entre 15 et 74 ans. Elle ne donne pas un chiffre 2026."),
        ("Je conduis après deux verres, la limite est connue de tous.", "La limite légale n'a pas été relue sur Fedlex aujourd'hui. Elle ne sera pas inventée. En attendant, ne pas conduire après avoir bu est la conduite sûre."),
    ]
    dx8 = [
        ("C'est le stress, ne faites pas d'électrocardiogramme.", "Une oppression d'effort peut être les deux. Le cœur ne se conclut pas par le stress."),
        ("Ajoutez 50 % à mon SCORE2 parce que je suis stressé.", "Le risque relatif de groupe, entre 1,2 et 2,0, ne se multiplie pas ainsi au pourcentage individuel."),
        ("Le bas revenu double le risque, donc je suis perdu.", "Le risque relatif publié est 1,76, intervalle 1,45 à 2,14. C'est une association de population, pas votre destin."),
        ("Toute contrariété reclasse comme l'épuisement vital.", "Non. L'ESC limite cette preuve de reclassification à l'épuisement vital."),
        ("Posez-moi la question utile.", "Le travail, l'argent, la famille, la solitude et les événements récents ouvrent l'entretien, puis l'humeur et les idées de mort."),
        ("Prescrivez l'antidépresseur standard.", "La classe peut être juste plus tard. La dose attend l'information professionnelle et le contexte rénal, hépatique et obstétrical."),
    ]
    dx9 = [
        ("Je ne fume pas, le radon ne me concerne pas.", "Le radon est la cause de cancer du poumon qui vient après le tabac, y compris chez des non-fumeurs. Il tue 200 à 300 personnes par an."),
        ("Ma commune est orange, je n'ai pas besoin de mesurer.", "La carte priorise. Seule la mesure du local occupé dit la concentration."),
        ("1 000 becquerels restent la limite de ma chambre.", "Depuis 2018, la référence des locaux occupés est 300 Bq/m³. 1 000 Bq/m³ est le seuil du poste de travail exposé."),
        ("Je passe dix minutes au sous-sol, dois-je assainir ?", "En dessous de quinze heures par semaine, ce local n'exige en principe pas de mesure. La décision change s'il devient une chambre."),
        ("Qui paie les travaux ?", "En principe le propriétaire, article 166 de l'ordonnance, et le canton peut ordonner l'assainissement."),
        ("Donnez-moi tous les délais du tableau 4.", "La bande 300 à 600 Bq/m³ est claire : dix ans si le séjour est prolongé, trente ans s'il est court. Au-dessus, le médecin ouvre le tableau plutôt que de réciter une cellule mal lue."),
        ("Quel comprimé baisse le radon ?", "Aucun. Le bâtiment et l'arrêt du tabac sont les leviers."),
    ]
    dx10 = [
        ("Mon père est mort à 78 ans, c'est précoce.", "Non. La page EAS retient avant 55 ans chez l'homme et avant 60 ans chez la femme."),
        ("Prélevez aujourd'hui, je veux savoir.", "Pour un test présymptomatique, le conseil vient avant, puis un délai, article 21. Le prélèvement immédiat ne respecte pas la loi."),
        ("Dites le résultat à ma sœur, elle angoisse.", "L'article 7 interdit cette communication sans votre consentement. Elle a aussi le droit de ne pas savoir."),
        ("Un score polygénique vendu en ligne suffit.", "L'ESC ne recommande pas la collecte routinière de ces scores, classe III. Ce n'est pas un conseil LAGH."),
        ("Mon LDL est très élevé mais mon SCORE2 est bas, ignorez la famille.", "L'hypercholestérolémie familiale se classe sur la page AGLA, sans score de personne saine pour l'adoucir."),
        ("Testez mon enfant pour me rassurer.", "Le représentant consent si l'enfant est incapable de discernement, et l'enfant est associé. Un test de curiosité n'est pas une indication."),
        ("Que doit contenir le conseil ?", "Fréquence et nature, conséquences du test et du refus, coûts, mesures, soutien, et ce que les assurances peuvent demander."),
    ]
    return {
        "dx5": oraux("Réponses orales — risque vie entière", dx5),
        "dx6": oraux("Réponses orales — score calcique", dx6),
        "dx7": oraux("Réponses orales — alcool", dx7),
        "dx8": oraux("Réponses orales — stress psychosocial", dx8),
        "dx9": oraux("Réponses orales — radon", dx9),
        "dx10": oraux("Réponses orales — histoire familiale et LAGH", dx10),
    }


def suite_courte(title, rows):
    items = []
    for row in rows:
        items.append(list(row))
    return windows(title, items)


def suite_dx5():
    rows = [
        ("Le médecin écrit la phrase de sortie d'une consultation de prévention.", "Il nomme l'outil, la tranche d'âge, la catégorie, les modificateurs cherchés et la date de revue.", "Il n'écrit pas une dose.", "La personne repart avec un seul plan, limité aux leviers qu'elle peut tenir.", "Un symptôme d'alerte annule cette sortie et ouvre l'urgence."),
        ("Le bénéfice vie entière se dit en années, pas en pourcentage relatif.", "L'ESC le définit comme la différence d'âge auquel le risque cumulé atteint 50 %, avec et sans le traitement envisagé.", "Aucun seuil formel n'accompagne cette différence.", "Le médecin ne promet pas un nombre d'années s'il n'a pas ouvert le calculateur.", "La durée du traitement est plus longue chez le jeune, donc le retour se juge aussi sur cette durée."),
        ("La randomisation mendélienne est citée par l'ESC pour une seule idée.", "De petites différences de LDL ou de pression, maintenues toute la vie, pèsent lourd.", "Ce n'est pas une autorisation à traiter tout adolescent.", "Avant 40 ans, le médicament reste l'exception familiale ou tensionnelle.", "Le mode de vie est le moyen qui peut durer des décennies."),
        ("Une personne originaire de l'étranger consulte en Suisse.", "La page AGLA du calculateur SCORE2 demande d'envisager le pays d'origine si le séjour est court ou si le mode de vie d'origine persiste.", "Cette phrase ne donne pas un coefficient chiffré suisse.", "Le médecin le note comme une limite, pas comme une multiplication automatique.", "Il recalcule lorsque le mode de vie a convergé vers celui du pays de résidence."),
        ("Le candidat confond prévention primaire et dépistage organisé.", "L'ESC distingue le repérage opportuniste, efficace pour découvrir une pression ou un lipide, du dépistage systématique, qui améliore les facteurs sans avoir montré d'effet sur les événements.", "Ce DX est une consultation, pas un programme national de scores.", "Le médecin saisit l'occasion d'une visite pour autre chose.", "Il n'en déduit pas un scanner de masse."),
        ("La symétrie des modificateurs s'examine sur un cas.", "Un modificateur défavorable peut monter le risque près d'un seuil.", "Un profil plus favorable que prévu doit pouvoir le baisser.", "L'ESC dit que l'effet sur le risque absolu est en général bien plus petit que le risque relatif publié.", "Le médecin ne collectionne donc pas les modificateurs loin de tout seuil."),
        ("Femme de moins de 50 ans et homme de moins de 40 ans.", "L'ESC dit que leur risque à dix ans est presque toujours bas.", "Leurs facteurs modifiables peuvent néanmoins rendre le risque lointain très haut.", "La copie qui s'arrête à « bas risque » est incomplète.", "La copie qui médicalise d'emblée avant 40 ans l'est aussi."),
        ("Le dossier de sortie nomme ce qui n'a pas été fait.", "Aucune information professionnelle n'a été ouverte, donc aucune dose.", "Aucun pourcentage individuel n'a été inventé lorsque les lipides manquaient.", "La Suisse a été lue comme pays à faible risque.", "Le prochain rendez-vous sert à saisir l'outil, pas à répéter le cours."),
        ("Le médecin ferme par trois phrases que la personne peut répéter.", "Il dit quel outil sera utilisé, parce que l'autre ne mesure pas le même événement.", "Il dit dans quelle tranche d'âge les seuils changent.", "Il dit ce qui ferait revenir avant la date : une douleur, un déficit, ou un LDL déjà connu comme très élevé.", "Il n'ajoute pas une ordonnance pour meubler le silence."),
        ("Le pays à faible risque change le bénéfice absolu, pas la biologie de la plaque.", "La même pression et le même LDL produisent moins d'événements en Suisse que dans une région à très haut risque des abaques SCORE2.", "Le médecin le dit pour ne pas importer un protocole étranger.", "Il ne dit pas que le risque est nul.", "Il envisage le pays d'origine si le séjour est court ou si le mode de vie d'origine persiste, comme la page AGLA du calculateur SCORE2 le demande."),
    ]
    return suite_courte("Clôture de consultation — risque vie entière", rows)


def suite_dx6():
    rows = [
        ("Le compte rendu d'imagerie doit être traduit.", "Le médecin écrit si le calcium est absent, plus bas ou plus haut que l'attendu pour l'âge et le sexe.", "Il écrit si ce résultat change la catégorie.", "Il écrit si une douleur existait, auquel cas le compte rendu de prévention ne suffit pas.", "Il ne recopie pas un seuil de 100 unités."),
        ("Refus d'examen.", "La personne peut refuser le rayonnement.", "Le médecin documente le refus et décide avec le calculateur et les modificateurs.", "Il ne punit pas le refus par une menace chiffrée inventée.", "Il propose la plaque carotidienne seulement si elle peut encore changer la décision."),
        ("Disponibilité et coût.", "L'ESC conditionne le déploiement du score à la faisabilité locale.", "Un examen excellent sur le papier et inaccessible ne devient pas un standard suisse par cette phrase.", "Le médecin dit ce qui est faisable ici.", "Il n'envoie pas à l'étranger pour un score de routine."),
        ("Scanner injecté.", "L'ESC dit qu'il voit les sténoses et que l'étude SCOT-HEART concerne des douleurs stables, pas le dépistage.", "On ne sait pas, dans le texte lu, s'il classe le risque mieux que le calcium seul.", "Il ne devient donc pas l'examen de première intention de ce DX.", "L'allergie à l'iode le concerne, lui, et non le score sans injection."),
        ("Répétition.", "Le texte ESC ouvert ne fixe pas un intervalle suisse de nouveau score.", "Le médecin ne le reprend pas chaque année par habitude.", "Il le reprend seulement si une nouvelle décision dépend du résultat.", "Il le dit à la personne pour éviter la course à l'image."),
        ("Phrase de remise du résultat.", "Le médecin dit d'abord si le calcium est au-dessus, au niveau ou en dessous de l'attendu pour l'âge et le sexe.", "Il dit ensuite si la catégorie de risque change.", "Il dit enfin ce qui reste vrai même si le score est nul : le tabac, la pression et le LDL.", "Il ne remet pas un chiffre d'Agatston isolé comme un diplôme."),
        ("Ce que le score ne remplace pas.", "Il ne remplace pas l'arrêt du tabac.", "Il ne remplace pas la confirmation de la pression hors du cabinet.", "Il ne remplace pas la recherche d'une hypercholestérolémie familiale.", "Il ne remplace pas l'information professionnelle le jour où un médicament devient indiqué."),
        ("Le médecin note enfin la limite du zéro.", "Un score nul abaisse le risque calculé seulement s'il est lu avec l'âge et le sexe.", "Il ne voit pas la plaque molle.", "Il ne clôt pas une douleur d'effort.", "La personne repart avec cette phrase, pas avec une certitude absolue."),
    ]
    return suite_courte("Clôture de consultation — score calcique", rows)


def suite_dx7():
    rows = [
        ("Semaine type d'une femme : deux verres le vendredi et deux le samedi, rien d'autre.", "Quatre verres sur la semaine font 40 g au total, soit environ 6 g par jour en moyenne, calcul dérivé.", "La moyenne quotidienne reste sous 20 g, donc hors risque chronique moyen.", "Deux verres ne constituent pas non plus un épisode féminin, dont le seuil est de quatre verres.", "Le médecin le dit, sans appeler cette consommation protectrice."),
        ("Semaine type d'un homme : cinq verres chaque samedi.", "Cinq verres atteignent le seuil épisodique masculin.", "S'il le fait au moins une fois par mois, l'OFSP qualifie l'épisode à risque.", "La moyenne sur sept jours peut rester sous le seuil chronique.", "Les deux lignes figurent dans le dossier."),
        ("Adolescent de 16 ans.", "En 2022, 22 % des 15 à 19 ans déclarent un excès au moins une fois par mois.", "La réponse n'est pas un score d'adulte.", "Le médecin protège, informe et cherche l'entourage.", "Il ne prescrit pas un médicament de l'alcoolodépendance de l'adulte sans cadre."),
        ("Coûts et travail.", "L'OFSP relie 2,1 milliards de francs à la productivité perdue.", "Cela ne fixe pas la durée d'un arrêt de ce patient.", "L'incapacité se juge sur ce qu'il peut faire, ce jour-là.", "L'alcool au travail à risque se traite comme une situation inappropriée, selon la page OFSP."),
        ("Hôpital.", "La page prévention de l'OFSP, citée par la recherche puis recoupée par les faits, parle d'hospitalisations.", "Le chiffre précis d'hospitalisations n'est pas recopié ici s'il n'a pas été relu sur MonAM dans le fichier ouvert.", "Le médecin hospitalise selon la clinique du sevrage, du trauma ou de l'hépatopathie, pas selon un quota.", "Il ne donne pas un schéma de benzodiazépine dans ce cours."),
        ("Cancer et alcool.", "Parmi les 1 553 décès de 2017, 36 % sont des cancers.", "L'OFSP ajoute qu'aucune quantité sans effet sur les cancers n'a été établie.", "Le médecin le dit sans listing inventé d'organes au-delà de ce qui est écrit.", "L'arrêt reste utile après le diagnostic."),
        ("Entourage.", "Environ un tiers de la population a, autour d'elle, au moins une personne en difficulté avec l'alcool, selon la page OFSP qui cite Marmet et Gmel, 2015.", "Le médecin peut ouvrir cette porte si le patient consulte pour un proche.", "Il ne soigne pas le proche absent sans le voir.", "Il oriente vers les offres cantonales plutôt que d'inventer un dispositif."),
        ("Phrase de fin pour une consommation au-dessus du seuil, sans dépendance ni urgence.", "Le médecin répète le nombre de verres standard et la bande Obsan qui correspond.", "Il fixe un objectif chiffré et une date de revue.", "Il rappelle qu'aucune quantité n'est présentée comme sans effet sur les cancers.", "Il vérifie que la personne ne va pas conduire si elle a bu."),
        ("Ce qui reste hors de ce fichier.", "Les doses de médicaments du sevrage et du maintien de l'abstinence.", "Le seuil légal d'alcool au volant, non relu sur Fedlex.", "Le seuil chiffré d'un questionnaire AUDIT, non relu dans une recommandation suisse.", "Le médecin le dit, et il ouvre ces textes au moment du soin réel."),
        ("Dernière vérification avant de laisser partir une personne stable.", "Le médecin a séparé l'épisode, la moyenne quotidienne et la dépendance.", "Il a converti les verres en grammes avec l'équivalence de 10 g, marquée comme lecture d'Obsan.", "Il a écarté la grossesse, la conduite immédiate et l'idée suicidaire.", "Il a fixé la revue, et il n'a signé aucune dose."),
    ]
    return suite_courte("Clôture de consultation — alcool", rows)


def plus_map():
    base = {
        "dx5": plus_dx5() + suite_dx5(),
        "dx6": plus_dx6() + suite_dx6(),
        "dx7": plus_dx7() + suite_dx7(),
        "dx8": plus_dx8(),
        "dx9": plus_dx9(),
        "dx10": plus_dx10(),
    }
    extra = plus_oraux()
    return {k: base[k] + extra[k] for k in base}
