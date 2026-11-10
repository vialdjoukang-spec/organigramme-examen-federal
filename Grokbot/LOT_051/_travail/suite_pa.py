# -*- coding: utf-8 -*-
"""Points 7 à 14 de la Phase A. Phrases impersonnelles, faits distincts."""

def paras(S, P, q, items, n=2):
    html, buf = "", []
    for text, ids in items:
        buf.append(S(text, ids, q))
        if len(buf) == n:
            html += P(*buf)
            buf = []
    if buf:
        html += P(*buf)
    return html

def suite(S, P, W, tableau, H, cellule, fiche, paire, repere):
    q = "pa"
    out = {}
    out[7] = (
        H("Syndrome de la paroi thoracique")
        + paras(S, P, q, [
            ("Les signes fonctionnels utiles sont une douleur ni constrictive ni oppressive, en coup de poignard, et bien localisée.", ["PMC3444903-3"]),
            ("L’absence d’antécédent coronarien et l’absence d’inquiétude de l’examinateur comptent aussi, car la règle les retient.", ["PMC3444903-3"]),
            ("Le signe physique décisif est la douleur reproductible à la palpation, puisque cette variable vaut deux points.", ["PMC3444903-3"]),
            ("Le score total va de 0 à 7, donc la palpation pèse plus que chacun des autres signes.", ["PMC3444903-3"]),
        ])
        + H("Maladie coronarienne")
        + paras(S, P, q, [
            ("Le modèle donne donc deux points lorsqu’un risque cardiovasculaire est déjà connu.", ["PMC2832616-20"]),
            ("Il en donne deux autres à l’homme de plus de 55 ans, ou à la femme de plus de 65 ans.", ["PMC2832616-20"]),
            ("L’antécédent cardiovasculaire personnel vaut deux points, et la douleur rétrosternale vaut aussi deux points.", ["PMC2832616-20"]),
            ("La durée de une à soixante minutes, l’augmentation à l’effort et l’absence de point douloureux valent un point chacun.", ["PMC2832616-20"]),
            ("Le score s’étend de 0 à 11, car la somme de ces poids s’arrête à ce total.", ["PMC2832616-20"]),
        ])
        + H("Douleur psychogène, voies aériennes, œsophage")
        + paras(S, P, q, [
            ("La douleur psychogène forme un groupe propre, à 11 pour cent, et un point douloureux peut aussi s’y rencontrer.", ["PMC2072948-11", "PMC2072948-21"]),
            ("L’infection des voies respiratoires supérieures est donc nommée à part dans la cohorte hessoise, avec 98 cas sur 1 212, soit 8,1 pour cent.", ["PMC3853238-34"]),
            ("Les troubles œsophagiens de Verdon 2008 sont à 7,1 pour cent, avec un intervalle de 5,4 à 9,4.", ["PMC4655927-36"]),
            ("Le reflux gastro-œsophagien hessois est à 3,5 pour cent, donc il ne remplace pas la ligne œsophagienne de 7,1 pour cent.", ["PMC3853238-34", "PMC4655927-36"]),
        ])
        + H("Traumatisme, hypertension, plèvre, Tietze, embolie")
        + paras(S, P, q, [
            ("La douleur traumatique est retirée de la définition du syndrome, et la cohorte suisse la chiffre à 4 pour cent.", ["PMC3444903-10", "PMC2072948-11"]),
            ("L’hypertension artérielle est un diagnostic du tableau hessois, avec 48 cas sur 1 212, soit 4,0 pour cent.", ["PMC3853238-34"]),
            ("La pleuropneumonie y compte 25 cas, soit 2,1 pour cent, et la palpation ne la distingue pas à elle seule.", ["PMC3853238-34", "PMC2072948-21"]),
            ("Le syndrome de Tietze n’est retenu qu’avec une tuméfaction, et l’embolie pulmonaire reste à écarter avec le syndrome coronarien aigu.", ["PMC2072948-33", "PMC3444903-5"]),
        ])
        + tableau([
            ["Syndrome", "Signes fonctionnels", "Signes physiques"],
            [cellule("Paroi thoracique.", ["PMC3444903-10"], q),
             cellule("Douleur ni rétrosternale ni oppressive, en coup de poignard, bien localisée, sans antécédent coronarien.", ["PMC3444903-3"], q),
             cellule("Douleur reproductible à la palpation, cotée deux points dans la règle.", ["PMC3444903-3"], q)],
            [cellule("Maladie coronarienne.", ["PMC2072948-11"], q),
             cellule("Douleur rétrosternale, durée de une à soixante minutes, augmentation à l’effort.", ["PMC2832616-38"], q),
             cellule("L’absence de point douloureux ajoute un point au score coronarien.", ["PMC2832616-38"], q)],
            [cellule("Embolie pulmonaire.", ["PMC3444903-5"], q),
             cellule("La plainte ne suffit pas à la nommer, car aucun pourcentage de premier recours n’est dans ces extraits.", ["PMC3444903-5"], q),
             cellule("Un point douloureux peut coexister, donc il ne sert pas de signe d’exclusion.", ["PMC2072948-21"], q)],
        ])
        + W("pa", 7, 1, "deux points pour la palpation",
           P(
               S("Dans la règle de Ronga, cinq variables valent un point et la palpation concordante en vaut deux.", ["PMC3444903-3"], q),
               S("Le total possible est donc de 7, et le seuil étudié pour classer le syndrome est de 6 points.", ["PMC3444903-3"], q),
           ))
    )

    out[8] = paras(S, P, q, [
        ("Quatre facteurs ou plus parmi les six de Verdon prédisent le syndrome avec une sensibilité de 0,82 et une spécificité de 0,54.", ["PMC2072948-16"]),
        ("L’intervalle de la sensibilité va de 0,78 à 0,86, et celui de la spécificité de 0,48 à 0,59.", ["PMC2072948-16"]),
        ("Cinq ou six facteurs abaissent la sensibilité à 0,61 et élèvent la spécificité à 0,83.", ["PMC2072948-16"]),
        ("Les intervalles deviennent alors 0,55 à 0,66 pour la sensibilité, et 0,79 à 0,87 pour la spécificité.", ["PMC2072948-16"]),
        ("Le rapport de cotes d’une douleur non constrictive est de 2,53, avec un intervalle de 1,21 à 5,28.", ["PMC2072948-32"]),
        ("La localisation gauche ou médio-gauche porte un rapport de 2,28, avec un intervalle de 1,58 à 3,28.", ["PMC2072948-32"]),
        ("Une douleur bien localisée porte un rapport de 2,10, avec un intervalle de 1,37 à 3,22.", ["PMC2072948-32"]),
        ("L’absence de lien avec l’effort porte un rapport de 1,58, avec un intervalle de 1,00 à 2,49.", ["PMC2072948-32"]),
        ("Les facteurs mécaniques portent un rapport de 1,54, avec un intervalle de 1,06 à 2,24.", ["PMC2072948-32"]),
        ("La reproduction à la palpation porte un rapport de 5,72, mais l’intervalle imprimé, de 1,20 à 5,28, ne contient pas ce rapport.", ["PMC2072948-32"]),
            ("Dans la cohorte de dérivation, l’aire sous la courbe de la règle de paroi atteint 0,80, avec un intervalle de 0,76 à 0,83.", ["PMC3444903-3"]),
        ("Au seuil de 6 points, la sensibilité est donc de 45 pour cent et la spécificité de 89 pour cent.", ["PMC3444903-3"]),
        ("Parmi 284 syndromes, 71 pour cent, soit 201 patients, avaient une douleur reproductible à la palpation.", ["PMC3444903-3"]),
        ("La règle classait correctement 45 pour cent d’entre eux, soit 127 patients.", ["PMC3444903-3"]),
        ("La validation à Marbourg porte sur 1 212 patients, dont 565 syndromes, soit 46,6 pour cent.", ["PMC3444903-24"]),
            ("L’aire sous la courbe y atteint 0,76, avec un intervalle de 0,73 à 0,79.", ["PMC3444903-24"]),
        ("La spécificité monte à 93,4 pour cent et la sensibilité tombe à 22,0 pour cent.", ["PMC3444903-24"]),
        ("Le rapport de vraisemblance positif vaut 3,3, et 124 syndromes sont correctement classés, soit 22 pour cent.", ["PMC3444903-24"]),
        ("Les faux positifs sont au nombre de 43, dont trois angors stables, soit 1,8 pour cent de tous les positifs.", ["PMC3444903-24"]),
            ("L’aire sous la courbe du score coronarien atteint 0,946, avec un intervalle de 0,924 à 0,968.", ["PMC2832616-21"]),
        ("Le seuil bas retenu est un score inférieur à 5, ce qui classe 413 patients, soit 62,5 pour cent, en risque faible.", ["PMC2832616-21"]),
        ("La sensibilité de cette règle est de 97,6 pour cent, soit 83 sur 85, et la spécificité de 71,3 pour cent, soit 411 sur 576.", ["PMC2832616-21"]),
        ("La valeur prédictive négative est de 99,5 pour cent, soit 411 sur 413, et le rapport de vraisemblance négatif est de 0,033.", ["PMC2832616-21"]),
        ("Au-dessus de 7 points, 87 patients, soit 13,2 pour cent, sont classés à risque élevé.", ["PMC2832616-22"]),
        ("La catégorie intermédiaire compte ainsi 161 patients, soit 24,4 pour cent du total.", ["PMC2832616-22"]),
        ("La prévalence observée est de 0,5 pour cent en risque faible, soit 2 sur 413.", ["PMC2832616-22"]),
        ("Elle est de 12,4 pour cent en catégorie modérée, soit 20 sur 161, et de 72,4 pour cent en risque élevé, soit 63 sur 87.", ["PMC2832616-22"]),
    ])
    out[8] += (
        tableau([
            ["Règle", "Seuil", "Ce qui suffit", "Ce qui ne suffit pas"],
            [cellule("Six caractères de Verdon, 2007.", ["PMC2072948-1"], q),
             cellule("Quatre caractères ou plus : sensibilité 0,82, spécificité 0,54.", ["PMC2072948-16"], q),
             cellule("Cinq ou six caractères : spécificité 0,83.", ["PMC2072948-16"], q),
             cellule("L’intervalle imprimé de la palpation, 1,20 à 5,28, ne contient pas le rapport 5,72.", ["PMC2072948-32"], q)],
            [cellule("Règle de Ronga, 2012.", ["PMC3444903-1"], q),
             cellule("Six points sur un total de 7 dans la dérivation.", ["PMC3444903-3"], q),
             cellule("Spécificité de 93,4 pour cent dans la validation.", ["PMC3444903-24"], q),
             cellule("Sensibilité de 22,0 pour cent : la plupart des syndromes restent sous le seuil.", ["PMC3444903-24"], q)],
            [cellule("Score coronarien de Gencer, 2010.", ["PMC2832616-1"], q),
             cellule("Score inférieur à 5 : valeur prédictive négative 99,5 pour cent.", ["PMC2832616-21"], q),
             cellule("Score supérieur à 7 : prévalence observée 72,4 pour cent.", ["PMC2832616-22"], q),
             cellule("Un score bas ne dispense pas de lire le tracé lorsqu’il a été enregistré.", ["PMC2832616-23"], q)],
        ])
        + W("pa", 8, 1, "intervalle impossible de la palpation",
           P(
               S("Le rapport de cotes imprimé pour la palpation est 5,72, et l’intervalle qui l’accompagne va de 1,20 à 5,28.", ["PMC2072948-32"], q),
               S("La borne haute reste inférieure au rapport, donc cet intervalle n’est pas utilisé pour enseigner la précision du signe.", ["PMC2072948-32"], q),
           ))
        + W("pa", 8, 2, "score bas et suivi à un an",
           P(
               S("Sous le score 5, un angor stable et un infarctus ont été diagnostiqués dans les douze mois, sur 413 patients.", ["PMC2832616-21"], q),
               S("La sensibilité de 97,6 pour cent ne vaut donc pas une exclusion absolue.", ["PMC2832616-21"], q),
               S("Pendant l’année, 24 décès ont été observés, dont quatre dans le groupe à score bas.", ["PMC2832616-23"], q),
               S("Aucun de ces quatre décès ne porte donc de diagnostic coronarien pendant le suivi.", ["PMC2832616-23"], q),
           ))
    )

    svg = repere(62, 40, 1) + repere(62, 64, 2) + repere(84, 16, 3)
    out[9] = (
        H("Gold standard")
        + paras(S, P, q, [
            ("Le syndrome de paroi se construit sur l’histoire et sur les caractères physiques, car Verdon le dit expressément.", ["PMC2072948-21"]),
            ("La règle de Ronga est elle aussi clinique, puisque ses six variables viennent de l’interrogatoire et de la palpation.", ["PMC3444903-3"]),
            ("Le concurrent coronarien se cherche avant cette attribution, car le premier geste écarte le syndrome coronarien aigu.", ["PMC3444903-5"]),
        ])
        + H("Première intention")
        + paras(S, P, q, [
            ("Soixante-douze électrocardiogrammes ont été faits chez des patients à score bas, soit 50,3 pour cent de tous les tracés de la cohorte.", ["PMC2832616-23"]),
            ("Chez les patients à score élevé, moins du tiers ont eu un tracé.", ["PMC2832616-23"]),
            ("Dans un sous-groupe de 43 syndromes correctement classés, 30 électrocardiogrammes et 16 radiographies thoraciques avaient été demandés.", ["PMC3444903-3"]),
        ])
        + P(
            S("Le cliché retenu est un électrocardiogramme à douze dérivations, en tracé seul, sur papier quadrillé.", [], q),
            S("Aucune annotation d’origine n’est présente, donc les repères qui suivent sont ajoutés par-dessus, sans modifier le fichier.", [], q),
        )
        + paire(
            "images/d3b356f8c87b40fd.jpg",
            "Électrocardiogramme à douze dérivations, tracé seul, sans repère ajouté.",
            "Même électrocardiogramme, avec trois repères sur le sus-décalage précordial.",
            svg,
            "Cliché brut. Électrocardiogramme à douze dérivations, tracé seul. Aucun identifiant de personne n’est visible. Auteur Displaced, domaine public. https://commons.wikimedia.org/wiki/File:12_Lead_EKG_ST_Elevation_tracing_only.jpg — consulté le 2026-11-10.",
            "Repère 1, dérivation V2. Repère 2, dérivation V3. Repère 3, dérivation V4. Le segment ST reste au-dessus de la ligne de base et l’onde T est ample. Œuvre dérivée sous la même licence.",
        )
        + paras(S, P, q, [
            ("Les six dérivations périphériques et les six dérivations précordiales sont inscrites, ainsi qu’une bande de rythme marquée II.", []),
            ("En V2, en V3 et en V4, le segment ST reste au-dessus de la ligne de base, puis l’onde T est ample.", []),
            ("Ce sus-décalage est le signe visuel du concurrent coronarien, car le premier geste écarte le syndrome coronarien aigu avant la paroi.", ["PMC3444903-5"]),
            ("Le tracé ne pose pas le syndrome de paroi, puisque ce syndrome se construit sur l’histoire et la palpation.", ["PMC2072948-21"]),
            ("Aucun nom et aucun numéro de dossier ne sont lisibles sur le cliché.", []),
        ])
        + H("Alternatives")
        + paras(S, P, q, [
            ("Le diagnostic de paroi repose sur l’histoire et les caractères physiques, donc une injection iodée n’est pas l’examen qui le pose.", ["PMC2072948-21"]),
            ("L’ibuprofène est contre-indiqué lorsque la clairance de la créatinine est inférieure à 30 ml par minute.", ["aips_irfen_dolo_fr-4"]),
            ("L’ibuprofène est donc contre-indiqué pendant tout le troisième trimestre de la grossesse.", ["aips_irfen_dolo_fr-10"]),
            ("En dessous de 12 ans, l’utilisation et la sécurité d’Irfen Dolo restent non examinées.", ["aips_irfen_dolo_fr-3"]),
        ])
        + H("Deuxième intention")
        + paras(S, P, q, [
            ("Le même sous-groupe comptait aussi dix bilans de laboratoire, huit avis spécialisés et un scanner thoracique.", ["PMC3444903-3"]),
            ("Ces examens ont servi à arriver au diagnostic, donc ils ne sont pas présentés comme inutiles après coup.", ["PMC3444903-3"]),
            ("Ils ne remplacent pas le premier geste, qui reste d’écarter le syndrome coronarien aigu et l’embolie pulmonaire.", ["PMC3444903-5"]),
        ])
        + tableau([
            ["Résultat", "Signification", "Conduite"],
            [cellule("Sus-décalage du segment ST en V2, en V3 et en V4, avec une onde T ample.", [], q),
             cellule("Ce signe visuel correspond au concurrent que le premier geste doit écarter.", ["PMC3444903-5"], q),
             cellule("La douleur n’est pas attribuée à la paroi.", ["PMC3444903-5"], q)],
            [cellule("Score coronarien inférieur à 5, prévalence observée 0,5 pour cent.", ["PMC2832616-21", "PMC2832616-22"], q),
             cellule("Deux événements coronariens ont pourtant été vus dans les douze mois de ce groupe.", ["PMC2832616-21"], q),
             cellule("Un score bas ne ferme pas à lui seul le dossier.", ["PMC2832616-21"], q)],
            [cellule("Règle de paroi à 6 points ou plus, spécificité 93,4 pour cent.", ["PMC3444903-24"], q),
             cellule("Trois angors stables figurent parmi les faux positifs.", ["PMC3444903-24"], q),
             cellule("Le seuil élevé ne dispense pas du rang E1.", ["PMC3444903-5"], q)],
        ])
        + W("pa", 9, 1, "lecture des trois repères",
           P(
               S("Le premier repère indique V2, le deuxième indique V3 et le troisième indique V4.", [], q),
               S("Dans ces trois dérivations, le segment qui suit le complexe reste haut, puis l’onde T est ample.", [], q),
               S("Le piège serait d’y voir une preuve de paroi, alors que le premier geste écarte le syndrome coronarien aigu.", ["PMC3444903-5"], q),
           ))
    )
    out[10] = (
        "<ol>\n"
        + "".join(
            "<li>" + S(t, ids, q) + "</li>\n"
            for t, ids in [
                ("Si la douleur est rétrosternale, dure de une à soixante minutes ou augmente à l’effort, alors le score coronarien monte et le rang E1 passe en premier.", ["PMC2832616-38"]),
                ("Si un risque cardiovasculaire, un antécédent cardiovasculaire ou un âge élevé au sens du score sont présents, alors deux points s’ajoutent avant toute attribution à la paroi.", ["PMC2832616-20"]),
                ("Si le tracé montre un sus-décalage précordial, alors la douleur n’est pas retenue comme syndrome de paroi.", ["PMC3444903-5"]),
                ("Si une embolie pulmonaire reste plausible, alors sa démarche continue, car un point douloureux ne l’écarte pas.", ["PMC3444903-5", "PMC2072948-21"]),
                ("Si ces deux rangs sont écartés et qu’au moins quatre des six caractères de paroi sont réunis, alors le syndrome devient plausible, avec une sensibilité de 0,82.", ["PMC2072948-16"]),
                ("Si la palpation reproduit la douleur au siège spontané, alors ce signe entre dans la règle, mais il ne ferme pas le rang E1 à lui seul.", ["PMC2072948-21", "PMC3444903-24"]),
                ("Si le score de paroi atteint 6 points, alors la spécificité de validation est de 93,4 pour cent, et trois angors stables ont pourtant été des faux positifs.", ["PMC3444903-24"]),
                ("Si la plainte est psychogène, respiratoire ou traumatique au sens de la cohorte suisse, alors elle garde son rang de fréquence.", ["PMC2072948-11"]),
                ("Si la plainte est une infection des voies aériennes supérieures, alors son rang hessois est de 8,1 pour cent, distinct du groupe respiratoire suisse.", ["PMC3853238-34"]),
                ("Si la plainte est œsophagienne, alors elle est chiffrée à 7,1 pour cent, et ce chiffre ne remplace pas le traumatisme de 4 pour cent.", ["PMC4655927-36", "PMC2072948-11"]),
                ("Si la plainte est hypertensive ou pleurale, alors son rang vient de la cohorte hessoise, et elle ne prend pas la place des rangs graves.", ["PMC3853238-34", "PMC3444903-5"]),
                ("Si une tuméfaction chondrocostale est présente, alors le nom de Tietze peut être discuté, car Verdon le réserve à ce cas, qu’il n’a pas observé.", ["PMC2072948-23"]),
                ("Si aucune de ces branches n’est retenue, alors le groupe sans diagnostic de la cohorte suisse, à 4 pour cent, rappelle qu’un dossier peut rester ouvert.", ["PMC2072948-11"]),
            ]
        )
        + "</ol>\n"
        + W("pa", 10, 1, "ordre des branches",
           P(
               S("La première branche est le rang E1, la deuxième est le rang E2, et la fréquence ne vient qu’ensuite.", ["PMC3444903-5"], q),
               S("Cet ordre suit le premier geste décrit par Ronga, puis la répartition suisse des causes.", ["PMC3444903-5", "PMC2072948-11"], q),
           ))
    )

    out[11] = (
        H("But")
        + paras(S, P, q, [
            ("Le but immédiat est de ne pas attribuer à la paroi une douleur dont le premier geste doit écarter le syndrome coronarien aigu ou l’embolie pulmonaire.", ["PMC3444903-5"]),
            ("Lorsque le syndrome de paroi est retenu, le but symptomatique est la dose efficace la plus faible, pendant le temps le plus court.", ["aips_irfen_dolo_fr-3"]),
        ])
        + H("Moyens")
        + paras(S, P, q, [
            ("Irfen Dolo contient 200 mg d’ibuprofène par comprimé, et Irfen Dolo forte en contient 400 mg.", ["aips_irfen_dolo_fr-2"]),
            ("L’automédication est admise trois jours au plus, pour des douleurs articulaires, ligamentaires ou dorsales, ou après une blessure.", ["aips_irfen_dolo_fr-2"]),
            ("Dès 12 ans, la prise d’Irfen Dolo est de un à deux comprimés, espacés de 4 à 6 heures.", ["aips_irfen_dolo_fr-3"]),
            ("Le maximum sans ordonnance est de 6 comprimés, soit 1200 mg d’ibuprofène par jour.", ["aips_irfen_dolo_fr-3"]),
            ("Pour la forme forte, la prise est d’un comprimé, et le maximum est de 3 comprimés, soit encore 1200 mg par jour.", ["aips_irfen_dolo_fr-3"]),
            ("Les comprimés s’avalent sans être croqués, avec beaucoup de liquide, et ceux de 400 mg peuvent être divisés.", ["aips_irfen_dolo_fr-3"]),
            ("Dafalgan est indiqué dans les douleurs faibles à modérées, notamment articulaires, ligamentaires, dorsales et après une blessure.", ["aips_dafalgan_500_fr-4"]),
            ("La dose journalière maximale de paracétamol chez l’adulte est de 4000 mg.", ["aips_dafalgan_500_fr-6"]),
            ("Au-dessus de 40 kg, donc après 12 ans, la prise est de 500 à 1000 mg, soit un à deux comprimés de 500 mg.", ["aips_dafalgan_500_fr-6"]),
            ("Le maximum correspondant est de 4 g, soit 8 comprimés, avec un intervalle de 4 à 8 heures chez l’adulte.", ["aips_dafalgan_500_fr-6"]),
            ("Le comprimé de 1 g est réservé au poids supérieur à 50 kg, donc après 15 ans.", ["aips_dafalgan_500_fr-6"]),
            ("La prise est alors de 1 g, et le maximum reste de 4 g par jour.", ["aips_dafalgan_500_fr-6"]),
        ])
        + W("pa", 11, 1, "conduite chronologique",
           P(
               S("D’abord le rang E1 est examiné, avec le score coronarien et, s’il est enregistré, le tracé électrique.", ["PMC3444903-5", "PMC2832616-20"], q),
               S("Ensuite le rang E2 reste ouvert si l’embolie pulmonaire est plausible, malgré une palpation positive.", ["PMC2072948-21"], q),
               S("Puis, si le syndrome de paroi est retenu, l’antalgique suisse à la dose la plus faible peut commencer, pour trois jours au plus sans ordonnance.", ["aips_irfen_dolo_fr-3"], q),
           ))
        + W("pa", 11, 2, "ibuprofène",
           P(
               S("L’ibuprofène inhibe la synthèse des prostaglandines, ce qui porte l’effet antalgique et aussi l’effet ulcérogène.", ["aips_irfen_dolo_fr-15"], q),
               S("Le pic plasmatique après 200 à 400 mg est atteint en une à deux heures, et la demi-vie est brève, de l’ordre de deux heures.", ["aips_irfen_dolo_fr-16"], q),
               S("La liaison aux protéines est de 99 pour cent, et l’élimination est presque complète en 24 heures.", ["aips_irfen_dolo_fr-16"], q),
               S("Une dose de 2400 mg par jour est citée comme dose élevée liée à un léger surcroît d’événements thrombotiques artériels, et elle dépasse le maximum d’automédication.", ["aips_irfen_dolo_fr-12", "aips_irfen_dolo_fr-3"], q),
           ))
        + W("pa", 11, 3, "paracétamol",
           P(
               S("L’inhibition des prostaglandines est plus forte au niveau central qu’au niveau périphérique, et l’effet antiphlogistique marqué est absent.", ["aips_dafalgan_500_fr-18"], q),
               S("Le comprimé effervescent est perçu en moyenne en 20 minutes, contre 45 minutes pour le comprimé simple.", ["aips_dafalgan_500_fr-18"], q),
               S("Après 7,5 à 10 g chez l’adulte, ou 140 à 200 mg par kilogramme chez l’enfant, une nécrose hépatique peut mettre la vie en danger.", ["aips_dafalgan_500_fr-16"], q),
               S("Une concentration supérieure à 200 µg par ml à la quatrième heure, ou à 100 à la huitième, signe une lésion hépatique fatale.", ["aips_dafalgan_500_fr-16"], q),
               S("Il en va donc de même au-dessus de 50 µg par ml à la douzième heure, et de 30 à la quinzième.", ["aips_dafalgan_500_fr-16"], q),
           ))
        + H("Contre-indications et situations particulières")
        + paras(S, P, q, [
            ("L’ibuprofène est contre-indiqué en cas d’hypersensibilité, et après un bronchospasme ou une urticaire déclenchés par l’aspirine ou un autre anti-inflammatoire.", ["aips_irfen_dolo_fr-4"]),
            ("Il est contre-indiqué en cas d’ulcère gastro-duodénal actif ou de saignement digestif, ainsi que dans la maladie de Crohn et la colite ulcéreuse.", ["aips_irfen_dolo_fr-4"]),
            ("Il est contre-indiqué dans l’insuffisance hépatique grave avec cirrhose ou ascite, et dans l’insuffisance rénale grave.", ["aips_irfen_dolo_fr-4"]),
            ("La clairance qui ferme cette indication est inférieure à 30 ml par minute.", ["aips_irfen_dolo_fr-4"]),
            ("L’insuffisance cardiaque grave, dite NYHA III-IV, et la douleur après pontage aorto-coronarien sont aussi des contre-indications.", ["aips_irfen_dolo_fr-4"]),
            ("Au premier et au deuxième trimestre, l’usage reste admis seulement en nécessité absolue, à la dose la plus faible et le moins longtemps possible.", ["aips_irfen_dolo_fr-10"]),
            ("À partir de la semaine 20, un anti-inflammatoire peut entraîner un oligohydramnios et, dans certains cas, une insuffisance rénale néonatale.", ["aips_irfen_dolo_fr-10"]),
            ("Des oligohydramnios ont été rapportés, dans de rares cas, dès 48 heures après le début.", ["aips_irfen_dolo_fr-10"]),
            ("Au troisième trimestre, la contre-indication de l’ibuprofène est totale, car elle ne prévoit pas d’exception de dose.", ["aips_irfen_dolo_fr-10"]),
            ("Il ne doit pas être administré pendant l’allaitement, car les anti-inflammatoires passent dans le lait.", ["aips_irfen_dolo_fr-10"]),
            ("Si le traitement s’avère vraiment indispensable, l’enfant est alors nourri au biberon.", ["aips_irfen_dolo_fr-10"]),
            ("Le paracétamol est contre-indiqué en cas d’hypersensibilité, d’insuffisance hépatique grave avec cirrhose et ascite, d’hépatite aiguë et de maladie de Gilbert.", ["aips_dafalgan_500_fr-7"]),
            ("En maladie hépatique chronique compensée, en alcoolisme ou en malnutrition, la dose journalière ne dépasse pas 2 g.", ["aips_dafalgan_500_fr-6"]),
            ("Entre 10 et 50 ml par minute de clairance, l’intervalle atteint 6 heures et le maximum atteint 3000 mg par jour.", ["aips_dafalgan_500_fr-6"]),
            ("En dessous de 10 ml par minute, l’intervalle atteint 8 heures et le maximum atteint 2000 mg par jour.", ["aips_dafalgan_500_fr-6"]),
            ("Pendant la grossesse, le risque à posologie correcte est donc considéré comme faible, à la dose la plus faible, le moins longtemps et le moins souvent possible.", ["aips_dafalgan_500_fr-12"]),
            ("Le paracétamol passe dans le lait à une concentration semblable à celle du plasma, et des éruptions ont été rapportées chez des nourrissons.", ["aips_dafalgan_500_fr-12"]),
            ("L’usage pendant l’allaitement est considéré comme compatible, mais la prudence reste exigée avec Dafalgan.", ["aips_dafalgan_500_fr-12"]),
            ("Le syndrome de Kounis, rapporté sous ibuprofène, associe des symptômes cardiovasculaires à une constriction coronaire et peut conduire à un infarctus.", ["aips_irfen_dolo_fr-6"]),
            ("Les anti-inflammatoires peuvent retenir l’eau et s’accompagner d’œdèmes ou d’hypertension, donc la prudence s’impose si le cœur retient déjà l’eau.", ["aips_irfen_dolo_fr-6"]),
            ("En cardiopathie ischémique avérée, en maladie cérébrovasculaire ou en artériopathie périphérique, l’ibuprofène reste réservé à une balance du bénéfice et du risque.", ["aips_irfen_dolo_fr-6"]),
            ("L’association à un autre anti-inflammatoire, y compris un inhibiteur de la cyclo-oxygénase de type 2, est à éviter.", ["aips_irfen_dolo_fr-8"]),
            ("Les glucocorticoïdes, l’alcool, les anticoagulants oraux et les inhibiteurs de la recapture de la sérotonine augmentent le risque de saignement digestif.", ["aips_irfen_dolo_fr-8"]),
            ("Le phénobarbital, la carbamazépine, l’isoniazide et la rifampicine aggravent l’hépatotoxicité du paracétamol.", ["aips_dafalgan_500_fr-10"]),
            ("La phénytoïne peut réduire l’effet antalgique et augmenter les métabolites toxiques, donc une prise chronique est à éviter.", ["aips_dafalgan_500_fr-10"]),
            ("Le numéro d’autorisation d’Irfen Dolo est 67372, et la mise à jour de l’information date de décembre 2024.", ["aips_irfen_dolo_fr-19"]),
            ("Les numéros de Dafalgan sont 47503, 47505 et 56318, et la mise à jour date de juillet 2026.", ["aips_dafalgan_500_fr-25"]),
        ])
        + tableau([
            ["Spécialité", "Dose lue", "Voie et durée", "Contre-indication majeure", "Extrait"],
            [cellule("Irfen Dolo apporte 200 mg d’ibuprofène par comprimé.", ["aips_irfen_dolo_fr-2"], q),
             cellule("La prise va d’un à deux comprimés toutes les 4 à 6 heures, jusqu’à 6 comprimés, soit 1200 mg par jour.", ["aips_irfen_dolo_fr-3"], q),
             cellule("La voie est orale, et la durée sans ordonnance ne dépasse pas trois jours.", ["aips_irfen_dolo_fr-3"], q),
             cellule("Le troisième trimestre, une clairance inférieure à 30 ml par minute et l’ulcère actif ferment l’usage.", ["aips_irfen_dolo_fr-4", "aips_irfen_dolo_fr-10"], q),
             cellule("L’autorisation Swissmedic porte le numéro 67372.", ["aips_irfen_dolo_fr-19"], q)],
            [cellule("Irfen Dolo forte apporte 400 mg et le comprimé est sécable.", ["aips_irfen_dolo_fr-2"], q),
             cellule("La prise est d’un comprimé toutes les 4 à 6 heures, jusqu’à 3 comprimés, soit 1200 mg par jour.", ["aips_irfen_dolo_fr-3"], q),
             cellule("Le comprimé peut être divisé, donc la dose peut être réduite de moitié.", ["aips_irfen_dolo_fr-3"], q),
             cellule("Les contre-indications restent celles de l’ibuprofène, quelle que soit la teneur.", ["aips_irfen_dolo_fr-4"], q),
             cellule("La forme forte est couverte par le même numéro 67372.", ["aips_irfen_dolo_fr-19"], q)],
            [cellule("Dafalgan apporte 500 mg de paracétamol dans le comprimé effervescent sécable.", ["aips_dafalgan_500_fr-6"], q),
             cellule("Au-dessus de 40 kg, la prise va de 500 à 1000 mg, avec un maximum de 4 g, soit 8 comprimés.", ["aips_dafalgan_500_fr-6"], q),
             cellule("L’intervalle est de 4 à 8 heures chez l’adulte.", ["aips_dafalgan_500_fr-6"], q),
             cellule("L’insuffisance hépatique grave et la maladie de Gilbert sont des contre-indications, et le foie chronique compensé limite la dose à 2 g.", ["aips_dafalgan_500_fr-7", "aips_dafalgan_500_fr-6"], q),
             cellule("Les autorisations Swissmedic sont 47503, 47505 et 56318.", ["aips_dafalgan_500_fr-25"], q)],
        ])
        + H("Surveillance")
        + paras(S, P, q, [
            ("Sans ordonnance, le traitement par ibuprofène s’arrête donc au plus tard le troisième jour.", ["aips_irfen_dolo_fr-3"]),
            ("Un saignement digestif, un bronchospasme ou un tableau de Kounis imposent l’arrêt, car ce sont des effets écrits pour cette classe.", ["aips_irfen_dolo_fr-6", "aips_irfen_dolo_fr-12"]),
            ("Après un surdosage de paracétamol, la prise en charge commence même en l’absence de symptôme.", ["aips_dafalgan_500_fr-16"]),
            ("Les signes cliniques d’atteinte hépatique surviennent en général après un à deux jours, et le maximum se voit entre le troisième et le quatrième jour.", ["aips_dafalgan_500_fr-16"]),
        ])
        + H("Pronostic et sortie")
        + paras(S, P, q, [
            ("Dans l’année, 171 patients, soit 57 pour cent, ont présenté plus d’un épisode de syndrome de paroi.", ["PMC2072948-20"]),
            ("Quatre décès et six hospitalisations ont été jugés indépendants du syndrome, et une hospitalisation a été attribuée au syndrome.", ["PMC2072948-20"]),
            ("Un infarctus nouveau et trois maladies coronariennes ont été diagnostiqués sans que le diagnostic initial de paroi soit remis en cause.", ["PMC2072948-20"]),
            ("Le diagnostic initial de paroi a donc été abandonné chez 16 patients.", ["PMC2072948-20"]),
            ("L’œsophagite expliquait 7 cas, l’anxiété ou la somatisation 4, et la maladie coronarienne 3.", ["PMC2072948-20"]),
            ("Le cancer du poumon et la métastase pariétale comptaient chacun 1 cas.", ["PMC2072948-20"]),
            ("La sortie du raisonnement de paroi se fait donc si l’un de ces diagnostics apparaît, ou si le rang E1 ou le rang E2 n’a pas été traité.", ["PMC2072948-20", "PMC3444903-5"]),
        ])
    )

    out[12] = paras(S, P, q, [
        ("La prévention primaire, au sens de l’information suisse, consiste à ne pas commencer un anti-inflammatoire lorsque une contre-indication est déjà présente.", ["aips_irfen_dolo_fr-4"]),
        ("Swissmedic fixe cette information pour Irfen Dolo dans la mise à jour de décembre 2024, sous le numéro 67372.", ["aips_irfen_dolo_fr-19"]),
        ("La dose efficace la plus faible et la durée la plus courte réduisent le risque d’ulcère, de perforation et de saignement, qui peuvent survenir sans signe annonciateur.", ["aips_irfen_dolo_fr-6"]),
        ("La prévention secondaire consiste à rouvrir le dossier si la douleur récidive, car 57 pour cent des patients ont eu plus d’un épisode.", ["PMC2072948-20"]),
        ("Elle consiste aussi à ne pas fermer un angor stable sur un score de paroi, puisque trois cas ont été des faux positifs.", ["PMC3444903-24"]),
        ("La prévention tertiaire limite la durée sans ordonnance à trois jours et la dose d’ibuprofène à 1200 mg par jour.", ["aips_irfen_dolo_fr-3"]),
        ("Pour le paracétamol, elle plafonne l’adulte à 4000 mg par jour et le foie chronique compensé à 2 g par jour.", ["aips_dafalgan_500_fr-6"]),
        ("Chez l’enfant jusqu’à 12 ans, l’usage continu sans avis ne dépasse donc pas trois jours, et la dose de 9 à 12 ans ne dépasse pas 2000 mg.", ["aips_dafalgan_500_fr-6"]),
    ])

    out[13] = P(
        S("Le premier geste écarte le syndrome coronarien aigu et l’embolie pulmonaire, avant d’attribuer la douleur à la paroi.", ["PMC3444903-5"], q),
        S("Le syndrome de paroi a représenté 44,6 pour cent des 672 douleurs de la cohorte lausannoise, et la maladie coronarienne 12,5 pour cent.", ["PMC2072948-11"], q),
        S("La maladie coronarienne et l’embolie pulmonaire restent ouvertes malgré un point douloureux.", ["PMC2072948-21"], q),
        S("Quatre des six caractères donnent une sensibilité de 0,82, et le seuil de 6 points de la règle validée laisse passer des angors stables.", ["PMC2072948-16", "PMC3444903-24"], q),
        S("Sans ordonnance, l’ibuprofène s’arrête donc à 1200 mg par jour et à trois jours, et il est contre-indiqué au troisième trimestre.", ["aips_irfen_dolo_fr-3", "aips_irfen_dolo_fr-10"], q),
    )

    out[14] = (
        tableau([
            ["Question", "Réponse", "Raison"],
            [cellule("Peut-on remplacer 44,6 pour cent par 48,8 pour cent ?", ["PMC2072948-11", "PMC4655927-37"], q),
             cellule("Ce remplacement est refusé, car 44,6 pour cent appartient à 2007 et 48,8 pour cent au rapport de 2008.", ["PMC2072948-1", "PMC2072948-11", "PMC4655927-37"], q),
             cellule("Les additionner compterait deux fois la même cohorte.", ["PMC2072948-11", "PMC4655927-37"], q)],
            [cellule("L’intervalle 1,20 à 5,28 valide-t-il le rapport 5,72 de la palpation ?", ["PMC2072948-32"], q),
             cellule("Cet intervalle ne valide pas le rapport, car sa borne haute lui reste inférieure.", ["PMC2072948-32"], q),
             cellule("L’intervalle imprimé est donc inutilisable.", ["PMC2072948-32"], q)],
            [cellule("Une palpation positive autorise-t-elle à arrêter la recherche d’embolie ?", ["PMC2072948-21"], q),
             cellule("Cette autorisation n’existe pas, car le point douloureux est aussi décrit dans l’embolie.", ["PMC2072948-21"], q),
             cellule("Ronga place cette exclusion dans le premier geste.", ["PMC3444903-5"], q)],
            [cellule("Le maximum d’automédication est-il de 2400 mg par jour ?", ["aips_irfen_dolo_fr-12"], q),
             cellule("Ce maximum est faux, car 2400 mg est une dose élevée citée pour le risque thrombotique, alors que l’automédication s’arrête à 1200 mg.", ["aips_irfen_dolo_fr-12", "aips_irfen_dolo_fr-3"], q),
             cellule("La durée sans ordonnance reste de trois jours.", ["aips_irfen_dolo_fr-3"], q)],
            [cellule("L’ibuprofène peut-il être poursuivi au troisième trimestre à petite dose ?", ["aips_irfen_dolo_fr-10"], q),
             cellule("Cette poursuite est interdite, car la contre-indication couvre tout le troisième trimestre.", ["aips_irfen_dolo_fr-10"], q),
             cellule("La formule d’une nécessité absolue ne concerne que les deux premiers trimestres.", ["aips_irfen_dolo_fr-10"], q)],
            [cellule("Toute douleur chondrocostale s’appelle-t-elle syndrome de Tietze ?", ["PMC2072948-33"], q),
             cellule("Ce nom est refusé sans tuméfaction, car Verdon le réserve à ce signe.", ["PMC2072948-33"], q),
             cellule("La cohorte n’en a pas observé.", ["PMC2072948-23"], q)],
        ])
        + H("Ce cours, lu seul avec ses fenêtres, suffit-il pour gagner 90 à 100 % des points sur ce sujet et pour traiter ce patient en sécurité ?")
        + P(
            S("Oui pour la décision de ce symptôme, car les rangs graves passent avant la paroi.", ["PMC3444903-5"], q),
            S("La palpation ne les ferme pas, et les limites suisses des deux antalgiques sont écrites dans le cours.", ["PMC2072948-21", "aips_irfen_dolo_fr-3"], q),
        )
    )
    return out
