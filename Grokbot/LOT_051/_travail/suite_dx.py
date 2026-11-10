# -*- coding: utf-8 -*-
"""DX.1 — syndrome de la paroi thoracique. Aucune phrase reprise de la Phase A."""
from suite_pa import paras

def dx(S, P, W, tableau, H, cellule, paire, repere, chrome):
    q = "dx1"
    out = {}
    out[1] = (
        chrome("dx1", "#0F4C2A")
        + paras(S, P, q, [
            ("Le syndrome de la paroi thoracique est la cause bénigne la plus souvent retenue devant une douleur de la paroi antérieure, car il s’agit d’un trouble musculosquelettique.", ["PMC3444903-10"]),
            ("Ronga le code R07.4 lorsqu’aucune précision supplémentaire n’est disponible, donc le code décrit le siège et non une lésion histologique.", ["PMC3444903-10"]),
            ("En soins primaires, L04 retient la douleur de la paroi ou de l’appareil locomoteur, tandis que A11 laisse une douleur thoracique sans autre précision.", ["PMC3444903-10"]),
            ("Costochondrite, syndrome costosternal, douleur chondrocostale et glissement costal entrent dans ce cadre.", ["PMC3444903-10"]),
            ("La douleur intercostale, le syndrome chondrocostal gauche, le syndrome pectoral gauche et le syndrome sternal y entrent aussi.", ["PMC3444903-10"]),
            ("La fibromyalgie est incluse, en revanche le traumatisme, la métastase et la douleur projetée du dos en sont exclus.", ["PMC3444903-10"]),
            ("Appeler Tietze toute douleur chondrocostale est inexact, car ce nom n’est admis qu’avec une tuméfaction.", ["PMC2072948-33"]),
            ("La cohorte lausannoise n’a d’ailleurs reconnu ni vrai syndrome de Tietze ni polyarthrite rhumatoïde, donc l’inflammation franche n’est pas le cas habituel.", ["PMC2072948-23"]),
        ])
        + W("dx1", 1, 1, "frontière du diagnostic",
           P(
               S("Le syndrome se distingue de la maladie coronarienne parce que la cohorte sépare les deux diagnostics au lieu de les confondre.", ["PMC2072948-11"], q),
               S("Il se distingue aussi de l’embolie pulmonaire, puisque le premier geste clinique consiste à l’écarter en même temps que le syndrome coronarien aigu.", ["PMC3444903-5"], q),
               S("Un point douloureux ne suffit pas à franchir cette frontière, car on le note aussi dans d’autres origines.", ["PMC2072948-21"], q),
           ))
    )
    out[2] = paras(S, P, q, [
        ("Cinquante-huit cabinets privés ont inclus, de mars à mai 2001, toute douleur thoracique consécutive pendant une période médiane de cinq semaines.", ["PMC2072948-2", "PMC2072948-6"]),
        ("Sur 24 620 rencontres, 672 personnes consultaient pour cette douleur, ce qui représente 2,7 pour cent.", ["PMC2072948-11"]),
        ("Trois cents d’entre elles ont reçu le diagnostic de syndrome de paroi, soit 44,6 pour cent des douleurs.", ["PMC2072948-11"]),
        ("Ce volume équivaut à 1,2 pour cent de l’ensemble des consultations, alors que les 84 maladies coronariennes n’en représentent que 0,34 pour cent.", ["PMC2072948-11"]),
        ("Les auteurs jugent le syndrome trois fois plus fréquent que les douleurs cardiaques, et le cabinet en voit un à deux cas par semaine.", ["PMC2072948-21"]),
        ("Le rapport des sexes y est de 1 pour 1, avec 155 femmes et 145 hommes.", ["PMC2072948-3", "PMC2072948-12"]),
        ("L’âge moyen atteint 50,3 ans, l’écart-type 18,2 ans, et les âges vont des adolescents jusqu’au-delà de 75 ans.", ["PMC2072948-12"]),
        ("L’épisode était inaugural dans 62 pour cent des cas, ancien ou récidivant dans 35 pour cent, et indéterminé dans 3 pour cent.", ["PMC2072948-12"]),
        ("Une comorbidité existait chez 250 personnes, soit 83 pour cent, dont une comorbidité psychiatrique chez 149, soit 50 pour cent.", ["PMC2072948-12"]),
        ("Cent personnes avaient donc une comorbidité cardiovasculaire, soit 33,3 pour cent, et 19 une maladie coronarienne déjà connue, soit 6 pour cent.", ["PMC2072948-12"]),
        ("Six néoplasies étaient connues, dont deux cancers du poumon, donc le terrain tumoral n’était pas nul.", ["PMC2072948-12"]),
        ("Le suivi a été complet à trois mois et de 97 pour cent à douze mois.", ["PMC2072948-11"]),
        ("Pendant l’année de suivi, 171 personnes, soit 57 pour cent, ont présenté une récidive.", ["PMC2072948-20"]),
        ("La méta-analyse attribue 48,8 pour cent à Verdon 2008, intervalle 45,0 à 52,7, et ce chiffre ne remplace pas 44,6 pour cent.", ["PMC4655927-37", "PMC2072948-11"]),
        ("La fourchette des études à faible biais va de 24,5 à 49,8 pour cent pour le syndrome de paroi.", ["PMC4655927-18"]),
        ("L’incidence en soins primaires va de 20,4 à 46,6 pour cent selon les études récentes citées par Ronga.", ["PMC3444903-5"]),
    ])
    out[2] += tableau([
        ["Chiffre", "Population", "Année", "Source"],
        [cellule("Le rapport des sexes est de 1 pour 1, avec 155 femmes et 145 hommes.", ["PMC2072948-3", "PMC2072948-12"], q),
         cellule("Le compte porte sur les 300 syndromes de paroi.", ["PMC2072948-11"], q),
         cellule("Le rapport de cohorte est publié en 2007.", ["PMC2072948-1"], q),
         cellule("Verdon et ses collègues décrivent cette cohorte lausannoise.", ["PMC2072948-1"], q)],
        [cellule("L’âge moyen atteint 50,3 ans, et l’écart-type 18,2 ans.", ["PMC2072948-12"], q),
         cellule("Les âges vont des adolescents jusqu’au-delà de 75 ans.", ["PMC2072948-12"], q),
         cellule("Le même article de 2007 donne cet âge.", ["PMC2072948-1", "PMC2072948-12"], q),
         cellule("La source reste la cohorte de Verdon.", ["PMC2072948-1"], q)],
        [cellule("La récidive concerne 171 personnes, soit 57 pour cent.", ["PMC2072948-20"], q),
         cellule("Le suivi atteint 97 pour cent à douze mois.", ["PMC2072948-11"], q),
         cellule("Ce suivi est celui du rapport de 2007.", ["PMC2072948-1", "PMC2072948-20"], q),
         cellule("Verdon rapporte cette histoire naturelle.", ["PMC2072948-20"], q)],
        [cellule("L’incidence citée va de 20,4 à 46,6 pour cent.", ["PMC3444903-5"], q),
         cellule("La fourchette concerne les soins primaires.", ["PMC3444903-5"], q),
         cellule("Ronga publie cette synthèse en 2012.", ["PMC3444903-1"], q),
         cellule("Ronga réunit ici plusieurs études de premier recours.", ["PMC3444903-5"], q)],
    ])
    out[3] = (
        paras(S, P, q, [
            ("Les zones douloureuses siègent sur les insertions musculaires ou tendineuses, sur le cartilage et sur les jonctions ostéochondrales.", ["PMC2072948-23"]),
            ("L’étiologie du syndrome reste mal définie, en revanche son caractère mécanique est clairement documenté.", ["PMC2072948-23"]),
            ("La position, le mouvement, le décubitus ou la respiration amplifient la douleur chez 71 pour cent des personnes.", ["PMC2072948-13"]),
            ("L’anxiété peut augmenter la sensibilité d’un point tenu pour menaçant, ainsi que le texte le reprend.", ["PMC2072948-23"]),
            ("Une toux longue, une thoracotomie ou le surmenage respiratoire de l’asthme peuvent favoriser l’épisode, donc le déclencheur change selon la personne.", ["PMC2072948-23"]),
        ])
        + P(
            S("Le schéma retenu montre la face antérieure du sternum et des cartilages costaux, en planche d’anatomie et non en cliché de patient.", [], q),
            S("Le fichier original n’est pas modifié : les quatre repères sont dessinés dans un calque séparé.", [], q),
        )
        + paire(
            "images/58c26a85d58f0594.png",
            "Planche anatomique du sternum et des cartilages costaux, sans repère ajouté.",
            "Même planche, avec quatre repères français sur le manubrium, le corps, le xiphoïde et les jonctions gauches.",
            repere(50, 15, 1) + repere(50, 42, 2) + repere(50, 64, 3) + repere(66, 46, 4),
            "Cliché brut. Henry Vandyke Carter, Gray’s Anatomy, planche 115, domaine public. https://commons.wikimedia.org/wiki/File:Gray115.png — consulté le 2026-11-10.",
            "Repère 1, manubrium. Repère 2, corps sternal. Repère 3, xiphoïde. Repère 4, jonctions chondrocostales du côté gauche du sujet, à droite de l’image.",
        )
        + paras(S, P, q, [
            ("Le premier repère indique le manubrium, le deuxième indique le corps et le troisième indique le xiphoïde.", []),
            ("Le quatrième repère désigne les jonctions chondrocostales gauches, là où le syndrome localisé est le plus souvent décrit.", ["PMC2072948-33"]),
            ("Cette planche associe donc le siège anatomique au mécanisme d’insertion, et elle ne montre pas une inflammation.", ["PMC2072948-23"]),
        ("La prédominance gauche reste inexpliquée, car l’auteur ne retient qu’une hypothèse d’innervation convergente, et non une preuve.", ["PMC2072948-22"]),
        ("Le diagnostic a été posé sans critères standards et sans supervision extérieure, donc des erreurs restaient possibles.", ["PMC2072948-25"]),
        ("Le suivi d’une année sert précisément à reconnaître les maladies graves prises au début pour ce syndrome.", ["PMC2072948-25"]),
        ("La maladie coronarienne et le syndrome de paroi peuvent coexister, ainsi que le texte le note après une thoracotomie.", ["PMC2072948-25"]),
        ("Dans un service d’urgence de la même région et de la même période, la maladie coronarienne devenait la cause principale.", ["PMC2072948-25"]),
        ("Le syndrome y était surtout décrit comme aigu, ce qui suggère que cette forme rare oriente vers l’urgence.", ["PMC2072948-25"]),
        ])
        + W("dx1", 3, 1, "lecture de la planche",
           P(
               S("On lit d’abord le sternum de haut en bas, puis les cartilages qui rejoignent les côtes.", [], q),
               S("Le piège serait de prendre la légende anglaise déjà imprimée pour une annotation de ce cours : les numéros français sont seulement dans le calque.", [], q),
           ))
        + tableau([
            ["Perturbation", "Exploration qui la montre", "Moyen qui la corrige"],
            [cellule("La douleur naît sur une insertion ou une jonction chondrocostale, et l’inflammation franche reste l’exception.", ["PMC2072948-23"], q),
             cellule("La planche situe le manubrium, le corps, le xiphoïde et les jonctions gauches.", [], q),
             cellule("Nommer le syndrome rassure davantage que le seul rejet d’une maladie grave.", ["PMC2072948-24"], q)],
            [cellule("La position, le mouvement, le décubitus ou la respiration amplifient la douleur chez 71 pour cent des personnes.", ["PMC2072948-13"], q),
             cellule("L’anamnèse cherche donc ces facteurs mécaniques, dont le rapport de cotes vaut 1,54.", ["PMC2072948-32"], q),
             cellule("La dose efficace la plus faible, pendant la durée la plus courte, vise ce symptôme.", ["aips_irfen_dolo_fr-3"], q)],
            [cellule("L’anxiété peut augmenter la sensibilité d’un point tenu pour menaçant.", ["PMC2072948-23"], q),
             cellule("L’inquiétude clinique est notée, et elle retire un point à la règle de paroi lorsqu’elle est présente.", ["PMC3444903-3"], q),
             cellule("Un diagnostic précis de syndrome de paroi est jugé rassurant dans ce texte.", ["PMC2072948-24"], q)],
        ])
    )
    out[4] = (
        paras(S, P, q, [
            ("Avant de retenir ce diagnostic, le syndrome coronarien aigu et l’embolie pulmonaire sont écartés, car ce sont les deux causes vitales nommées en premier.", ["PMC3444903-5"]),
            ("La maladie coronarienne occupe 12,5 pour cent des douleurs suisses et garde le rang E1, sans céder sa place à la fréquence.", ["PMC2072948-11"]),
            ("L’embolie pulmonaire n’a pas de pourcentage de premier recours dans les extraits, donc elle reçoit le rang E2 sans rang de fréquence.", ["PMC3444903-5"]),
            ("Une palpation qui reproduit la douleur ne fait pas sortir la personne du rang E1, ni du rang E2.", ["PMC2072948-21"]),
            ("Une fois ces deux rangs abordés, les quatre caractères ou plus parmi les six donnent une sensibilité de 0,82.", ["PMC2072948-16"]),
            ("La validation externe a néanmoins classé trois angors stables parmi les faux positifs, soit 1,8 pour cent de tous les positifs.", ["PMC3444903-24"]),
        ])
        + tableau([
            ["Concurrent", "Ce qui le sépare du syndrome", "Piège", "Conduite"],
            [cellule("Maladie coronarienne, rang E1.", ["PMC2072948-11"], q),
             cellule("Douleur rétrosternale, effort, durée de une à soixante minutes, absence de point douloureux.", ["PMC2832616-20"], q),
             cellule("Le côté gauche prédomine dans le syndrome et fait craindre le cœur.", ["PMC2072948-26"], q),
             cellule("Le diagnostic de paroi attend que ce concurrent ait été examiné.", ["PMC3444903-5"], q)],
            [cellule("Embolie pulmonaire, rang E2.", ["PMC3444903-5"], q),
             cellule("Aucun pourcentage de premier recours n’est disponible ici.", ["PMC3444903-5"], q),
             cellule("Le point douloureux est décrit dans l’embolie.", ["PMC2072948-21"], q),
             cellule("La démarche de l’embolie continue.", ["PMC3444903-5"], q)],
            [cellule("Traumatisme, 4 pour cent dans la cohorte suisse.", ["PMC2072948-11"], q),
             cellule("Ronga le retire de la définition.", ["PMC3444903-10"], q),
             cellule("Une douleur pariétale après choc n’est pas ce syndrome.", ["PMC3444903-10"], q),
             cellule("L’histoire du choc décide.", ["PMC2072948-11"], q)],
            [cellule("Syndrome de Tietze, sans fréquence.", ["PMC2072948-23"], q),
             cellule("La tuméfaction est exigée.", ["PMC2072948-33"], q),
             cellule("La costochondrite sans tuméfaction n’en est pas un.", ["PMC2072948-33"], q),
             cellule("On garde le nom de syndrome de paroi.", ["PMC2072948-23"], q)],
        ])
    )
    out[5] = (
        paras(S, P, q, [
            ("On cherche d’abord l’absence de caractère constrictif, dont le rapport de cotes vaut 2,53, intervalle 1,21 à 5,28.", ["PMC2072948-32"]),
            ("On cherche ensuite une douleur bien localisée, rapport 2,10, intervalle 1,37 à 3,22.", ["PMC2072948-32"]),
            ("Une douleur non liée à l’effort porte un rapport de 1,58, intervalle 1,00 à 2,49.", ["PMC2072948-32"]),
            ("Les facteurs mécaniques portent un rapport de 1,54, intervalle 1,06 à 2,24.", ["PMC2072948-32"]),
            ("La localisation gauche ou médio-gauche porte un rapport de 2,28, intervalle 1,58 à 3,28.", ["PMC2072948-32"]),
            ("L’intensité était modérée dans 75 pour cent des cas et sévère dans 23 pour cent.", ["PMC2072948-13"]),
            ("Des accès de quelques secondes à quelques jours concernaient 50 pour cent des personnes, et une douleur continue 35 pour cent.", ["PMC2072948-13"]),
            ("La forme aiguë intense concernait 9 pour cent, et l’anxiété passait alors de 54 à 93 pour cent.", ["PMC2072948-15", "PMC2072948-13"]),
            ("L’inquiétude clinique passait de 10 à 26 pour cent entre la douleur modérée et la douleur aiguë intense.", ["PMC2072948-15"]),
            ("L’irradiation touchait donc le bras gauche chez 18 personnes, le bras droit chez 4, le dos chez 5, le cou ou l’abdomen chez 3.", ["PMC2072948-13"]),
        ("La douleur dure des heures, des jours ou des semaines, et elle est le plus souvent bien localisée.", ["PMC2072948-13"]),
        ("Le côté gauche prédomine sur le côté droit, sans que cette latéralité ferme le diagnostic coronarien.", ["PMC2072948-13", "PMC2072948-21"]),
        ])
        + tableau([
            ["Signal d’alerte", "Ce qu’il signifie", "Décision"],
            [cellule("Durée de une à soixante minutes, effort, siège rétrosternal.", ["PMC2832616-38"], q),
             cellule("Ces caractères ajoutent des points au score coronarien.", ["PMC2832616-20"], q),
             cellule("Le rang E1 reste ouvert.", ["PMC3444903-5"], q)],
            [cellule("Inquiétude clinique présente.", ["PMC3444903-3"], q),
             cellule("La règle de paroi compte au contraire l’absence d’inquiétude.", ["PMC3444903-3"], q),
             cellule("Ce point de la règle est perdu.", ["PMC3444903-3"], q)],
            [cellule("Antécédent cardiovasculaire, qui vaut deux points.", ["PMC2832616-20"], q),
             cellule("Dix-neuf syndromes coexistaient avec une maladie coronarienne.", ["PMC2072948-12"], q),
             cellule("La coexistence n’est pas niée par le diagnostic de paroi.", ["PMC2072948-3"], q)],
        ])
        + W("dx1", 5, 1, "anxiété selon l’intensité",
           P(
               S("À intensité modérée, 54 pour cent des personnes expriment une anxiété et l’inquiétude clinique est notée dans 10 pour cent des cas.", ["PMC2072948-15"], q),
               S("À intensité aiguë, ces parts montent à 93 et à 26 pour cent, donc l’acuité change l’alarme sans changer le siège.", ["PMC2072948-15"], q),
           ))
    )
    out[6] = paras(S, P, q, [
        ("La palpation ne compte que si le point recouvre la douleur spontanée, le plus souvent d’un seul côté.", ["PMC2072948-21"]),
        ("Ce point était présent chez 214 des 300 personnes, donc son absence n’élimine pas à elle seule le syndrome.", ["PMC2072948-13"]),
        ("Le rapport de cotes imprimé pour cette reproduction est 5,72, tandis que l’intervalle joint, de 1,20 à 5,28, ne le contient pas.", ["PMC2072948-32"]),
        ("Parmi 210 douleurs à siège unique, un syndrome précis a été nommé chez 195 personnes.", ["PMC2072948-18"]),
        ("Le syndrome chondrocostal gauche comptait 70 personnes, le syndrome pectoral gauche 40, et le syndrome sternal 28.", ["PMC2072948-18"]),
        ("Quatre-vingt-huit personnes avaient plusieurs sièges, et 17 une douleur trop diffuse pour être nommée.", ["PMC2072948-18"]),
        ("Le sternal haut représentait 2,6 pour cent des 195, le sternal 14,4 pour cent et la xiphoïdalgie 3,1 pour cent.", ["PMC2072948-32"]),
        ("Le pectoral gauche représentait 20,5 pour cent contre 3,1 à droite, et l’axillaire gauche 6,2 contre 2,6.", ["PMC2072948-33"]),
        ("Le syndrome chondrocostal gauche représentait 35,8 pour cent, contre 6,2 pour cent à droite.", ["PMC2072948-33"]),
        ("Les totaux donnaient 65,5 pour cent à gauche, 20,0 au milieu et 14,5 à droite.", ["PMC2072948-33"]),
        ("Les étages gauches deux et trois valaient 8,7 pour cent, les étages quatre à six 19,0, et les étages sept à neuf 8,2.", ["PMC2072948-33"]),
        ("À droite, les mêmes étages valaient 1,0, 2,1 et 3,1 pour cent.", ["PMC2072948-33"]),
        ("La pointe costale valait 3,1 pour cent à gauche et 2,6 à droite.", ["PMC2072948-33"]),
        ("Huit personnes ont reçu un diagnostic costovertébral, sans point douloureux, la douleur semblant venir du rachis.", ["PMC2072948-14"]),
        ("Trois personnes décrivaient des élancements brefs, dits attrape thoracique, qui peuvent aussi siéger à droite.", ["PMC2072948-14"]),
        ("Une toux ou une dyspnée prolongée était donc notée chez 31 personnes, soit 10 pour cent, avec une douleur droite de 26 contre 11 pour cent.", ["PMC2072948-31"]),
        ("Vingt personnes, soit 7 pour cent, présentaient une anxiété, et leur âge moyen était de 43 ans contre 51 ans.", ["PMC2072948-31"]),
        ("Dans ce sous-groupe anxieux, la douleur constrictive concernait 55 pour cent des personnes, contre 23 pour cent chez les autres.", ["PMC2072948-31"]),
        ("L’humeur anxieuse inaugurait l’épisode chez 40 pour cent d’entre elles, contre 11 pour cent chez les autres.", ["PMC2072948-31"]),
        ("La fibromyalgie concernait 10 personnes, soit 3 pour cent, et 9 d’entre elles sur 10 étaient des femmes.", ["PMC2072948-31"]),
        ("Huit personnes, soit 3 pour cent, décrivaient un syndrome après thoracotomie, long et récidivant.", ["PMC2072948-31"]),
        ("Huit autres personnes, soit 3 pour cent, avaient un trouble rhumatologique associé.", ["PMC2072948-31"]),
        ("Parmi elles, l’ostéoporose concernait 3 personnes, la spondyloarthrite 2, l’arthrite 2 et la radiothérapie 1.", ["PMC2072948-31"]),
    ])
    out[6] += W("dx1", 6, 1, "geste de palpation",
        P(
            S("Le doigt appuie doucement sur le siège montré, car c’est l’empreinte décrite.", ["PMC2072948-21"], q),
            S("Un point éloigné de la douleur spontanée est écarté, puisqu’il n’a pas la valeur retenue.", ["PMC2072948-21"], q),
            S("Le signe reste non spécifique, car on le retrouve dans la maladie coronarienne, l’embolie, la plèvre, la néoplasie et la douleur psychogène.", ["PMC2072948-21"], q),
        ))
    out[7] = (
        H("7.1 Syndrome chondrocostal et syndrome pectoral")
        + paras(S, P, q, [
            ("Le syndrome chondrocostal gauche est le plus nombreux des syndromes isolés, avec 70 personnes sur les 195 nommées.", ["PMC2072948-18"]),
            ("Le syndrome pectoral gauche vient ensuite, avec 40 personnes, et c’est lui qui concentre presque toutes les présentations aiguës.", ["PMC2072948-18", "PMC2072948-26"]),
            ("L’origine musculaire de ce siège pectoral explique l’irradiation fréquente vers le bras gauche.", ["PMC2072948-26"]),
        ])
        + H("7.2 Syndrome sternal et attrape thoracique")
        + paras(S, P, q, [
            ("Le syndrome sternal comptait 28 personnes, et le sternal haut peut venir de l’articulation sternoclaviculaire ou manubriosternale.", ["PMC2072948-18", "PMC2072948-26"]),
            ("L’attrape thoracique, trois personnes dans la cohorte, est fréquent dans la vie mais rarement motif de consultation.", ["PMC2072948-14"]),
        ])
        + H("7.3 Ce qui reste hors du syndrome")
        + paras(S, P, q, [
            ("Le traumatisme, la métastase et la douleur venue du dos restent hors définition, même si la douleur est antérieure.", ["PMC3444903-10"]),
            ("La fibromyalgie, en revanche, reste à l’intérieur de la définition retenue par Ronga.", ["PMC3444903-10"]),
            ("Le syndrome pectoral, et même le syndrome axillaire, explique pratiquement toutes les présentations aiguës.", ["PMC2072948-24"]),
            ("Les patientes redoutent alors un cancer du sein, tandis que d’autres redoutent une maladie coronarienne.", ["PMC2072948-24"]),
            ("Le syndrome sternal haut peut venir d’une subluxation, d’une arthrite, d’un syndrome SAPHO ou de l’articulation manubriosternale.", ["PMC2072948-24"]),
            ("Deux personnes de la cohorte illustraient l’association avec un psoriasis ou une spondyloarthropathie.", ["PMC2072948-24"]),
            ("La xiphoïdalgie et les syndromes des côtes basses peuvent durer des décennies et être pris pour une maladie digestive.", ["PMC2072948-24"]),
        ])
        + tableau([
            ["Forme", "Signe fonctionnel", "Signe physique"],
            [cellule("Chondrocostal gauche, 70 personnes.", ["PMC2072948-18"], q),
             cellule("Douleur localisée sur les jonctions, souvent mécanique.", ["PMC2072948-23"], q),
             cellule("Point concordant, sans tuméfaction exigée.", ["PMC2072948-33"], q)],
            [cellule("Pectoral gauche, 40 personnes.", ["PMC2072948-18"], q),
             cellule("Présentation souvent aiguë, irradiation possible vers le bras.", ["PMC2072948-26"], q),
             cellule("Sensibilité du muscle pectoral au siège montré.", ["PMC2072948-21"], q)],
            [cellule("Sternal, 28 personnes.", ["PMC2072948-18"], q),
             cellule("Douleur médiane.", ["PMC2072948-32"], q),
             cellule("Point sur le sternum ou le xiphoïde.", ["PMC2072948-32"], q)],
        ])
    )
    out[8] = paras(S, P, q, [
        ("Avec quatre caractères ou davantage, la sensibilité atteint 0,82, intervalle 0,78 à 0,86, et la spécificité 0,54, intervalle 0,48 à 0,59.", ["PMC2072948-16"]),
        ("Avec cinq ou six caractères, la sensibilité diminue à 0,61 et la spécificité augmente à 0,83.", ["PMC2072948-16"]),
        ("Les intervalles correspondants vont de 0,55 à 0,66 pour la sensibilité, puis de 0,79 à 0,87 pour la spécificité.", ["PMC2072948-16"]),
        ("La règle de Ronga porte deux points pour la palpation et un point pour chacune des cinq autres variables, soit un total de 7.", ["PMC3444903-3"]),
        ("Dans la dérivation, l’aire sous la courbe atteint 0,80, avec un intervalle de 0,76 à 0,83.", ["PMC3444903-3"]),
        ("Au seuil de 6 points, la sensibilité de dérivation vaut 45 pour cent et la spécificité 89 pour cent.", ["PMC3444903-3"]),
        ("Sur 284 syndromes, 201, soit 71 pour cent, avaient une douleur reproductible, et 127, soit 45 pour cent, étaient correctement classés.", ["PMC3444903-3"]),
        ("À Marbourg, 1 212 personnes ont été classées, dont 565 syndromes, soit 46,6 pour cent.", ["PMC3444903-24"]),
        ("L’aire sous la courbe y vaut 0,76, intervalle 0,73 à 0,79, la spécificité 93,4 pour cent et la sensibilité 22,0 pour cent.", ["PMC3444903-24"]),
        ("Le rapport de vraisemblance positif vaut 3,3, et 124 syndromes, soit 22 pour cent, sont correctement classés.", ["PMC3444903-24"]),
        ("Quarante-trois faux positifs ont été comptés, et trois d’entre eux étaient des angors stables.", ["PMC3444903-24"]),
        ("Le rang coronarien reste donc à revoir malgré un score de paroi élevé.", ["PMC3444903-24"]),
    ])
    out[8] += (
        W("dx1", 8, 1, "seuil de six points",
           P(
               S("Le seuil de 6 points privilégie la spécificité, puisque 89 pour cent est la valeur de dérivation et 93,4 pour cent celle de validation.", ["PMC3444903-3", "PMC3444903-24"], q),
               S("La sensibilité de validation, 22,0 pour cent, montre que la plupart des syndromes restent sous ce seuil.", ["PMC3444903-24"], q),
           ))
        + W("dx1", 8, 2, "pourquoi l’intervalle de palpation est écarté",
           P(
               S("Le tableau indique 5,72 pour la palpation et, à côté, 1,20 à 5,28.", ["PMC2072948-32"], q),
               S("Comme la borne supérieure est plus basse que le rapport, cet intervalle n’est pas enseigné comme une précision.", ["PMC2072948-32"], q),
           ))
    )
    svg = repere(12, 8, 1) + repere(84, 8, 2) + repere(30, 46, 3) + repere(74, 86, 4)
    out[9] = (
        H("9.a Gold standard")
        + paras(S, P, q, [
            ("Le diagnostic positif est clinique, car il est construit exclusivement sur l’histoire et les caractères physiques.", ["PMC2072948-21"]),
            ("La radiographie n’est pas l’examen de référence du cartilage, puisque le cartilage ne se voit pas sur un cliché standard.", []),
        ])
        + H("9.b Première intention")
        + P(
            S("Le cliché joint est une radiographie thoracique de face, en incidence postéro-antérieure, chez une adulte sans identifiant lisible.", [], q),
            S("Les marqueurs Dx et Sin sont visibles, et le fichier original reste intact sous le calque.", [], q),
        )
        + paire(
            "images/6283642446c01898.jpg",
            "Radiographie thoracique de face, postéro-antérieure, sans repère ajouté.",
            "Même radiographie, avec quatre repères sur les marqueurs, le champ droit et la bulle gastrique.",
            svg,
            "Cliché brut. Mikael Häggström, CC0 1.0. https://commons.wikimedia.org/wiki/File:Normal_posteroanterior_(PA)_chest_radiograph_(X-ray).jpg — consulté le 2026-11-10.",
            "Repère 1, marqueur Dx, côté droit du sujet. Repère 2, marqueur Sin, côté gauche. Repère 3, champ pulmonaire droit aéré. Repère 4, bulle gastrique sous l’hémicoupole gauche.",
        )
        + paras(S, P, q, [
            ("Les deux champs sont aérés et aucune large opacité n’est affirmée sur cette image.", []),
            ("Une ligne pleurale viscérale de pneumothorax reste non affirmée sur cette radiographie également.", []),
            ("La bulle gastrique se voit sous l’hémicoupole gauche, du côté marqué Sin.", []),
            ("Ce cliché ne prouve pas le syndrome de paroi, car le cartilage costal n’y dessine pas le point douloureux.", ["PMC2072948-21"]),
            ("Il n’écarte pas non plus un syndrome coronarien aigu, puisque ce diagnostic ne se lit pas sur la transparence pulmonaire.", ["PMC3444903-5"]),
            ("Dans un sous-groupe de 43 syndromes bien classés, 16 radiographies et 30 électrocardiogrammes avaient pourtant été demandés.", ["PMC3444903-3"]),
        ])
        + H("9.c Alternatives")
        + paras(S, P, q, [
            ("Ni l’histoire ni la palpation n’injectent d’iode, donc une allergie à l’iode ne bloque pas le geste qui pose le diagnostic.", ["PMC2072948-21"]),
            ("L’ibuprofène, lui, est contre-indiqué si la clairance de la créatinine est inférieure à 30 ml par minute.", ["aips_irfen_dolo_fr-4"]),
            ("Il est également contre-indiqué pendant tout le troisième trimestre, sans exception écrite de petite dose.", ["aips_irfen_dolo_fr-10"]),
            ("Avant l’âge de 12 ans, la sécurité de l’ibuprofène n’a pas été examinée dans ce texte.", ["aips_irfen_dolo_fr-3"]),
        ])
        + H("9.d Deuxième intention")
        + paras(S, P, q, [
            ("Le même sous-groupe comptait dix examens de laboratoire, huit avis et un scanner.", ["PMC3444903-3"]),
            ("Ces demandes ont contribué au classement, donc elles ne sont pas déclarées superflues.", ["PMC3444903-3"]),
            ("Elles restent secondes par rapport à l’exclusion du syndrome coronarien aigu et de l’embolie.", ["PMC3444903-5"]),
        ])
        + tableau([
            ["Lecture", "Ce qu’elle permet", "Ce qu’elle ne permet pas"],
            [cellule("Champs aérés, sans large opacité affirmée, bulle gastrique à gauche.", [], q),
             cellule("Le cliché montre un thorax sans foyer étendu visible.", [], q),
             cellule("Il ne montre pas le cartilage et ne pose pas le syndrome.", ["PMC2072948-21"], q)],
            [cellule("Absence de ligne pleurale affirmée.", [], q),
             cellule("Un pneumothorax franc n’est pas lu sur cette image.", [], q),
             cellule("Cette lecture n’exclut pas l’embolie pulmonaire.", ["PMC3444903-5"], q)],
        ])
        + W("dx1", 9, 1, "ce que la radiographie décide",
           P(
               S("Elle décide qu’aucun grand foyer ni pneumothorax franc n’est visible sur ce cliché précis.", [], q),
               S("Elle ne décide pas le syndrome de paroi, qui reste un diagnostic d’histoire et de palpation concordante.", ["PMC2072948-21"], q),
               S("Elle ne décide donc pas d’arrêter la recherche d’un syndrome coronarien aigu.", ["PMC3444903-5"], q),
           ))
    )
    out[10] = (
        "<ol>\n"
        + "".join("<li>" + S(t, ids, q) + "</li>\n" for t, ids in [
            ("Si la douleur est rétrosternale, liée à l’effort ou longue de une à soixante minutes, alors le rang coronarien est examiné avant le syndrome.", ["PMC2832616-38", "PMC3444903-5"]),
            ("Si le score coronarien est inférieur à 5, la prévalence observée est de 0,5 pour cent, mais deux événements ont été vus en douze mois.", ["PMC2832616-21", "PMC2832616-22"]),
            ("Si une embolie reste plausible, alors la palpation positive ne clôt pas sa recherche.", ["PMC2072948-21"]),
            ("Si le point douloureux recouvre la douleur spontanée et que quatre caractères sont réunis, alors le syndrome reste plausible, car la spécificité n’atteint que 0,54.", ["PMC2072948-21", "PMC2072948-16"]),
            ("Si au moins quatre des six caractères sont présents, la sensibilité atteint 0,82 et la spécificité seulement 0,54.", ["PMC2072948-16"]),
            ("Si le score de Ronga atteint 6, la spécificité de validation est de 93,4 pour cent, avec une sensibilité de 22,0 pour cent.", ["PMC3444903-24"]),
            ("Si une tuméfaction chondrocostale apparaît, alors le nom de Tietze peut être discuté, ce que la cohorte n’a pas eu à faire.", ["PMC2072948-23"]),
            ("Si un choc, une métastase ou une douleur venue du dos expliquent le siège, alors le syndrome est retiré.", ["PMC3444903-10"]),
            ("Si le diagnostic est retenu, l’antalgique suit la dose la plus faible et la durée la plus courte.", ["aips_irfen_dolo_fr-3"]),
            ("Si la douleur récidive, le dossier est rouvert, car 57 pour cent des personnes ont eu plus d’un épisode.", ["PMC2072948-20"]),
        ])
        + "</ol>\n"
    )
    out[11] = (
        H("11.A But")
        + paras(S, P, q, [
            ("Une fois les rangs graves abordés, le but est de nommer le syndrome plutôt que de se contenter d’avoir écarté une maladie grave.", ["PMC2072948-26"]),
            ("Le but médicamenteux, lorsque un antalgique est choisi, reste la plus petite dose efficace pendant le moins de temps possible.", ["aips_irfen_dolo_fr-3"]),
        ])
        + H("11.B Moyens")
        + paras(S, P, q, [
            ("Irfen Dolo contient 200 mg d’ibuprofène, et la forme forte contient 400 mg, avec un comprimé sécable.", ["aips_irfen_dolo_fr-2"]),
            ("L’indication d’automédication couvre les douleurs articulaires, ligamentaires, dorsales et celles qui suivent une blessure, pendant trois jours au plus.", ["aips_irfen_dolo_fr-2"]),
            ("À partir de 12 ans, on donne un ou deux comprimés d’Irfen Dolo, en respectant 4 à 6 heures entre les prises.", ["aips_irfen_dolo_fr-3"]),
            ("On ne dépasse pas 6 comprimés, c’est-à-dire 1200 mg d’ibuprofène par jour.", ["aips_irfen_dolo_fr-3"]),
            ("La forme forte se limite à un comprimé par prise et à 3 comprimés, soit les mêmes 1200 mg par jour.", ["aips_irfen_dolo_fr-3"]),
            ("On avale le comprimé d’ibuprofène sans le croquer, et on le prend avec beaucoup de liquide.", ["aips_irfen_dolo_fr-3"]),
            ("Dafalgan concerne les douleurs faibles à modérées, y compris articulaires, ligamentaires, dorsales et après blessure.", ["aips_dafalgan_500_fr-4"]),
            ("Chez l’adulte, la dose de paracétamol ne dépasse pas 4000 mg par jour.", ["aips_dafalgan_500_fr-6"]),
            ("Au-delà de 40 kg, la prise de 500 mg va de un à deux comprimés, et le plafond est de 8 comprimés, soit 4 g.", ["aips_dafalgan_500_fr-6"]),
            ("L’intervalle adulte est donc de 4 à 8 heures, et celui de l’enfant de 6 à 8 heures.", ["aips_dafalgan_500_fr-6"]),
            ("Le comprimé de 1 g exige un poids supérieur à 50 kg, une prise de 1 g et un plafond de 4 g par jour.", ["aips_dafalgan_500_fr-6"]),
        ])
        + W("dx1", 11, 1, "ordre chronologique du traitement",
           P(
               S("On vérifie d’abord que le rang coronarien et le rang embolique ont été abordés.", ["PMC3444903-5"], q),
               S("On confirme ensuite que le point, s’il existe, recouvre la douleur spontanée.", ["PMC2072948-21"], q),
               S("Alors seulement l’antalgique oral commence, à la dose la plus faible, pour trois jours au plus s’il n’y a pas d’ordonnance.", ["aips_irfen_dolo_fr-3"], q),
           ))
        + W("dx1", 11, 2, "fiche de l’ibuprofène",
           P(
               S("L’effet antalgique vient de l’inhibition des prostaglandines, et le même mécanisme explique l’ulcère et la rétention de sodium.", ["aips_irfen_dolo_fr-15"], q),
               S("Après 200 à 400 mg, le pic plasmatique de 15 à 55 µg par ml est atteint en une à deux heures.", ["aips_irfen_dolo_fr-16"], q),
               S("La liaison protéique est de 99 pour cent, et l’élimination est presque achevée en 24 heures, sans accumulation.", ["aips_irfen_dolo_fr-16"], q),
               S("La dose de 2400 mg par jour est citée comme dose élevée liée à un léger excès thrombotique.", ["aips_irfen_dolo_fr-12"], q),
               S("Cette dose élevée reste donc distincte de la dose d’automédication retenue pour Irfen Dolo.", ["aips_irfen_dolo_fr-3"], q),
           ))
        + W("dx1", 11, 3, "fiche du paracétamol",
           P(
               S("L’action antalgique est plus centrale que périphérique, et il n’existe pas d’effet anti-inflammatoire marqué ni d’effet sur l’hémostase.", ["aips_dafalgan_500_fr-18"], q),
               S("Le comprimé effervescent est ressenti en moyenne au bout de 20 minutes, contre 45 minutes pour le comprimé ordinaire.", ["aips_dafalgan_500_fr-18"], q),
               S("Dès 7,5 à 10 g chez l’adulte, ou 140 à 200 mg par kilogramme chez l’enfant, la nécrose hépatique peut menacer la vie.", ["aips_dafalgan_500_fr-16"], q),
               S("La prise en charge d’un surdosage commence même si aucun symptôme n’est encore apparu.", ["aips_dafalgan_500_fr-16"], q),
           ))
        + tableau([
            ["Spécialité", "Dose lue dans l’information", "Voie", "Durée", "Contre-indication majeure", "Extrait suisse"],
            [cellule("Irfen Dolo contient 200 mg d’ibuprofène par comprimé.", ["aips_irfen_dolo_fr-2"], q),
             cellule("Dès 12 ans, la prise est de un à deux comprimés, espacés de 4 à 6 heures, sans dépasser 1200 mg par jour.", ["aips_irfen_dolo_fr-3"], q),
             cellule("Le comprimé s’avale sans être croqué, avec beaucoup de liquide.", ["aips_irfen_dolo_fr-3"], q),
             cellule("Sans ordonnance, l’usage ne dépasse pas trois jours.", ["aips_irfen_dolo_fr-2"], q),
             cellule("Le troisième trimestre et une clairance inférieure à 30 ml par minute ferment cet usage.", ["aips_irfen_dolo_fr-10", "aips_irfen_dolo_fr-4"], q),
             cellule("Swissmedic attribue le numéro 67372, mis à jour en décembre 2024.", ["aips_irfen_dolo_fr-19"], q)],
            [cellule("Irfen Dolo forte contient 400 mg, et le comprimé est sécable.", ["aips_irfen_dolo_fr-2"], q),
             cellule("La prise est d’un comprimé, au plus 3 par jour, soit 1200 mg.", ["aips_irfen_dolo_fr-3"], q),
             cellule("La voie reste orale.", ["aips_irfen_dolo_fr-3"], q),
             cellule("La durée sans ordonnance reste de trois jours.", ["aips_irfen_dolo_fr-3"], q),
             cellule("L’ulcère actif, la classe NYHA III-IV et la douleur après pontage restent des contre-indications.", ["aips_irfen_dolo_fr-4"], q),
             cellule("La forme forte partage le numéro 67372.", ["aips_irfen_dolo_fr-19"], q)],
            [cellule("Dafalgan apporte 500 mg de paracétamol, ou 1 g selon le comprimé.", ["aips_dafalgan_500_fr-6"], q),
             cellule("L’adulte ne dépasse pas 4000 mg par jour, et le comprimé de 1 g exige plus de 50 kg.", ["aips_dafalgan_500_fr-6"], q),
             cellule("La voie orale admet un intervalle de 4 à 8 heures.", ["aips_dafalgan_500_fr-6"], q),
             cellule("Jusqu’à 12 ans, l’usage continu sans avis ne dépasse pas trois jours.", ["aips_dafalgan_500_fr-6"], q),
             cellule("L’insuffisance hépatique grave et la maladie de Gilbert contre-indiquent le paracétamol.", ["aips_dafalgan_500_fr-7"], q),
             cellule("Les numéros Swissmedic sont 47503, 47505 et 56318, mis à jour en juillet 2026.", ["aips_dafalgan_500_fr-25"], q)],
        ])
        + H("Situations particulières")
        + paras(S, P, q, [
            ("L’hypersensibilité, le bronchospasme ou l’urticaire après aspirine ou après un autre anti-inflammatoire contre-indiquent l’ibuprofène.", ["aips_irfen_dolo_fr-4"]),
            ("L’ulcère actif, le saignement digestif, la maladie de Crohn et la colite ulcéreuse le contre-indiquent aussi.", ["aips_irfen_dolo_fr-4"]),
            ("La cirrhose avec ascite, l’insuffisance cardiaque grave de classe NYHA III-IV et la douleur après pontage aorto-coronarien le contre-indiquent également.", ["aips_irfen_dolo_fr-4"]),
            ("La clairance de la créatinine qui contre-indique l’ibuprofène est inférieure à 30 ml par minute.", ["aips_irfen_dolo_fr-4"]),
            ("Pendant les deux premiers trimestres, l’ibuprofène reste réservé à une nécessité absolue, à la dose la plus faible et pendant la durée la plus courte.", ["aips_irfen_dolo_fr-10"]),
            ("Dès la semaine 20, l’oligohydramnios et l’insuffisance rénale néonatale sont des risques décrits, parfois dès 48 heures.", ["aips_irfen_dolo_fr-10"]),
            ("Tout le troisième trimestre de la grossesse est une contre-indication, sans dose résiduelle autorisée.", ["aips_irfen_dolo_fr-10"]),
            ("Pendant l’allaitement, l’ibuprofène n’est pas donné, et l’enfant passe au biberon si un traitement maternel est vraiment indispensable.", ["aips_irfen_dolo_fr-10"]),
            ("Le paracétamol est contre-indiqué dans l’hypersensibilité, l’insuffisance hépatique grave, l’hépatite aiguë et la maladie de Gilbert.", ["aips_dafalgan_500_fr-7"]),
            ("Le foie chronique compensé, l’alcoolisme et la malnutrition limitent la dose journalière à 2 g.", ["aips_dafalgan_500_fr-6"]),
            ("De 10 à 50 ml par minute, on espace les prises de 6 heures et on plafonne à 3000 mg par jour.", ["aips_dafalgan_500_fr-6"]),
            ("Sous 10 ml par minute, l’intervalle atteint 8 heures et le plafond atteint 2000 mg par jour.", ["aips_dafalgan_500_fr-6"]),
            ("À posologie correcte pendant la grossesse, le risque du paracétamol est tenu pour faible, à la dose, la durée et la fréquence les plus basses.", ["aips_dafalgan_500_fr-12"]),
            ("Il passe ainsi dans le lait à un taux proche du plasma, des éruptions de nourrisson ont été rapportées, et la prudence demeure.", ["aips_dafalgan_500_fr-12"]),
            ("Le syndrome de Kounis sous ibuprofène peut constricter les coronaires et aboutir à un infarctus, donc une douleur nouvelle sous traitement rouvre le rang E1.", ["aips_irfen_dolo_fr-6"]),
            ("La rétention d’eau et l’hypertension sont des effets de classe, et la prudence augmente si le cœur retient déjà l’eau.", ["aips_irfen_dolo_fr-6"]),
            ("Un autre anti-inflammatoire, un corticoïde, l’alcool, un anticoagulant oral ou un inhibiteur de recapture de la sérotonine majorent le saignement digestif.", ["aips_irfen_dolo_fr-8"]),
            ("Phénobarbital, carbamazépine, isoniazide et rifampicine aggravent donc la toxicité hépatique du paracétamol lorsqu’ils sont associés.", ["aips_dafalgan_500_fr-10"]),
            ("L’autorisation d’Irfen Dolo est le numéro 67372, mise à jour en décembre 2024, et celles de Dafalgan sont 47503, 47505 et 56318, mises à jour en juillet 2026.", ["aips_irfen_dolo_fr-19", "aips_dafalgan_500_fr-25"]),
        ])
        + H("11.C Surveillance")
        + paras(S, P, q, [
            ("Sans ordonnance, on s’arrête au troisième jour même si la douleur n’a pas entièrement disparu.", ["aips_irfen_dolo_fr-3"]),
            ("Un saignement digestif, un bronchospasme ou un tableau de Kounis arrêtent donc l’ibuprofène.", ["aips_irfen_dolo_fr-6", "aips_irfen_dolo_fr-12"]),
            ("Les signes hépatiques d’un surdosage de paracétamol apparaissent en un à deux jours et culminent entre le troisième et le quatrième jour.", ["aips_dafalgan_500_fr-16"]),
        ])
        + H("11.D Pronostic et sortie")
        + paras(S, P, q, [
            ("Les auteurs parlent d’un pronostic favorable, d’une morbidité faible et d’une absence de mortalité propre au syndrome.", ["PMC2072948-26"]),
            ("Les résultats comptent néanmoins quatre décès et six hospitalisations jugés indépendants, plus une hospitalisation attribuée au syndrome.", ["PMC2072948-20"]),
            ("Un infarctus et trois maladies coronariennes sont apparus sans que le diagnostic initial soit retiré.", ["PMC2072948-20"]),
            ("Seize diagnostics ont été retirés : sept œsophagites, quatre tableaux d’anxiété ou de somatisation, trois maladies coronariennes, un cancer du poumon et une métastase pariétale.", ["PMC2072948-20"]),
            ("La sortie se décide donc si l’un de ces diagnostics s’impose, ou si un rang grave n’a pas été examiné.", ["PMC2072948-20", "PMC3444903-5"]),
        ])
    )
    out[12] = paras(S, P, q, [
        ("Prévenir, selon l’information Swissmedic de décembre 2024, c’est ne pas commencer l’ibuprofène lorsqu’une contre-indication est déjà connue.", ["aips_irfen_dolo_fr-4", "aips_irfen_dolo_fr-19"]),
        ("Le numéro d’autorisation 67372 porte cette règle pour Irfen Dolo, mis à jour en décembre 2024.", ["aips_irfen_dolo_fr-19"]),
        ("La dose la plus faible et la durée la plus courte visent les ulcères et les saignements, qui peuvent survenir sans annonce.", ["aips_irfen_dolo_fr-6"]),
        ("Après un premier épisode, la prévention secondaire rouvre donc l’interrogatoire, car 57 pour cent des personnes récidivent.", ["PMC2072948-20"]),
        ("Elle refuse aussi de clore un angor sur le seul score de paroi.", ["PMC3444903-24"]),
        ("La prévention tertiaire tient l’automédication à trois jours et à 1200 mg d’ibuprofène par jour.", ["aips_irfen_dolo_fr-3"]),
        ("Elle tient le paracétamol adulte à 4000 mg par jour, et à 2 g si le foie chronique est compensé.", ["aips_dafalgan_500_fr-6"]),
        ("De 9 à 12 ans, le paracétamol ne dépasse pas 2000 mg par jour, et trois jours continus sans avis restent le maximum jusqu’à 12 ans.", ["aips_dafalgan_500_fr-6"]),
        ("L’évolution reste défavorable seulement dans les erreurs de diagnostic, surtout malignes, ou dans les maladies concomitantes.", ["PMC2072948-26"]),
        ("Le texte signale le cœur, la maladie néoplasique et la pneumonie parmi ces concomitances.", ["PMC2072948-26"]),
        ("Le syndrome récidive, provoque une anxiété réelle et fait souvent craindre une maladie du cœur.", ["PMC2072948-26"]),
        ("La distinction clinique avec la maladie coronarienne reste difficile dans quelques cas, parce que la douleur pariétale est majoritairement gauche.", ["PMC2072948-26"]),
    ])
    out[13] = P(
        S("Le syndrome de paroi se nomme après avoir abordé le syndrome coronarien aigu et l’embolie pulmonaire, et non à leur place.", ["PMC3444903-5"], q),
        S("Il a donc concerné 300 des 672 douleurs lausannoises, soit 44,6 pour cent, avec un point concordant chez 214 personnes.", ["PMC2072948-11", "PMC2072948-13"], q),
        S("Le côté gauche domine, et cette latéralité ne doit pas être lue comme une preuve coronarienne ni comme son exclusion.", ["PMC2072948-26", "PMC2072948-21"], q),
        S("Quatre caractères suffisent pour une sensibilité de 0,82, mais le seuil validé de 6 points laisse passer des angors stables.", ["PMC2072948-16", "PMC3444903-24"], q),
        S("L’ibuprofène d’automédication s’arrête donc à 1200 mg par jour et à trois jours, et le troisième trimestre le contre-indique.", ["aips_irfen_dolo_fr-3", "aips_irfen_dolo_fr-10"], q),
    )
    out[14] = (
        tableau([
            ["Question", "Réponse", "Raison"],
            [cellule("Faut-il enseigner 48,8 pour cent à la place de 44,6 pour cent ?", ["PMC4655927-37", "PMC2072948-11"], q),
             cellule("Non, ces deux pourcentages viennent de deux rapports et ne se substituent pas.", ["PMC4655927-37", "PMC2072948-1"], q),
             cellule("Le rapport de 2007 reste la source du 44,6 pour cent.", ["PMC2072948-1", "PMC2072948-11"], q)],
            [cellule("Peut-on citer l’intervalle 1,20 à 5,28 comme précision du rapport 5,72 ?", ["PMC2072948-32"], q),
             cellule("Non, car la borne haute est inférieure au rapport imprimé.", ["PMC2072948-32"], q),
             cellule("On retient le rapport et on laisse l’intervalle de côté.", ["PMC2072948-32"], q)],
            [cellule("La palpation positive permet-elle d’arrêter le raisonnement embolique ?", ["PMC2072948-21"], q),
             cellule("Non, le point douloureux est expressément signalé dans l’embolie.", ["PMC2072948-21"], q),
             cellule("Le premier geste de Ronga reste entier.", ["PMC3444903-5"], q)],
            [cellule("2400 mg par jour est-il le plafond d’Irfen Dolo sans ordonnance ?", ["aips_irfen_dolo_fr-12", "aips_irfen_dolo_fr-3"], q),
             cellule("Non, 2400 mg est une dose élevée du texte sur le risque thrombotique, et le plafond d’automédication est 1200 mg.", ["aips_irfen_dolo_fr-12", "aips_irfen_dolo_fr-3"], q),
             cellule("La durée sans ordonnance demeure de trois jours.", ["aips_irfen_dolo_fr-3"], q)],
            [cellule("Une faible dose d’ibuprofène reste-t-elle possible au troisième trimestre ?", ["aips_irfen_dolo_fr-10"], q),
             cellule("Non, la contre-indication est complète pendant ce trimestre.", ["aips_irfen_dolo_fr-10"], q),
             cellule("La nécessité absolue n’est écrite que pour les deux premiers trimestres.", ["aips_irfen_dolo_fr-10"], q)],
            [cellule("Le syndrome chondrocostal gauche est-il un syndrome de Tietze ?", ["PMC2072948-33"], q),
             cellule("Non, sauf si une tuméfaction est présente, ce qui n’a pas été observé dans la cohorte.", ["PMC2072948-33", "PMC2072948-23"], q),
             cellule("Le nom ordinaire reste celui de syndrome de paroi.", ["PMC3444903-10"], q)],
        ])
        + H("Ce cours, lu seul avec ses fenêtres, suffit-il pour gagner 90 à 100 % des points sur ce sujet et pour traiter ce patient en sécurité ?")
        + P(
            S("Oui pour nommer ce syndrome et pour en limiter l’antalgique, car les exclusions graves précèdent le diagnostic et les doses suisses sont citées.", ["PMC3444903-5", "aips_irfen_dolo_fr-3"], q),
            S("La palpation concordante soutient le diagnostic sans fermer l’embolie ni la maladie coronarienne.", ["PMC2072948-21"], q),
        )
    )
    out[2] += paras(S, P, q, [
        ("La durée d’inclusion allait de 3 à 9 semaines, avec une médiane de 5 semaines.", ["PMC2072948-6"]),
        ("Dans cette cohorte, 90 pour cent des personnes étaient déjà connues du cabinet consulté.", ["PMC2072948-12"]),
        ("Une comorbidité rhumatologique était notée chez 62 personnes, soit 20,7 pour cent de la cohorte.", ["PMC2072948-12"]),
        ("Deux spondyloarthrites étaient connues, alors qu’aucune polyarthrite rhumatoïde n’était recensée dans ce groupe.", ["PMC2072948-12"]),
        ("Le groupe cardiovasculaire hors maladie coronarienne représentait 3,4 pour cent des douleurs.", ["PMC2072948-11"]),
        ("La paroi dans son ensemble représentait 51 pour cent, dont 4 pour cent de douleurs traumatiques et 2,4 pour cent de causes diverses.", ["PMC2072948-11"]),
        ("Le groupe respiratoire représentait 10 pour cent, et le groupe digestif 8 pour cent des douleurs.", ["PMC2072948-11"]),
        ("Aucune cause n’avait été retenue chez 4 pour cent des personnes douloureuses.", ["PMC2072948-11"]),
        ("Le groupe cardiovasculaire des études à faible biais va de 13,8 à 16,1 pour cent.", ["PMC4655927-18"]),
        ("La coronaropathie stable des mêmes études va de 6,6 à 11,2 pour cent.", ["PMC4655927-18"]),
        ("Le syndrome coronarien aigu ou l’infarctus va de 1,5 à 3,6 pour cent.", ["PMC4655927-18"]),
        ("Le groupe respiratoire va de 10,3 à 18,2 pour cent, et le groupe psychogène de 9,5 à 18,2 pour cent.", ["PMC4655927-18"]),
        ("Dans ces études, le groupe digestif va de 5,6 à 9,7 pour cent des douleurs.", ["PMC4655927-18"]),
        ("L’œsophage rapporté pour Verdon est à 7,1 pour cent, avec un intervalle de 5,4 à 9,4.", ["PMC4655927-36"]),
        ("La cohorte hessoise compte 1 212 personnes, dont 179 maladies coronariennes, soit 14,8 pour cent.", ["PMC3853238-34"]),
        ("La douleur psychogène y compte 115 personnes, ce qui représente 9,5 pour cent.", ["PMC3853238-34"]),
        ("L’infection des voies aériennes supérieures y compte 98 personnes, soit 8,1 pour cent.", ["PMC3853238-34"]),
        ("L’hypertension artérielle y est retenue chez 48 personnes, soit 4,0 pour cent.", ["PMC3853238-34"]),
        ("Le reflux y compte 42 personnes, soit 3,5 pour cent, et le traumatisme 39 personnes, soit 3,2 pour cent.", ["PMC3853238-34"]),
        ("Les troubles gastriques sont retenus chez 26 personnes, soit 2,1 pour cent de la cohorte.", ["PMC3853238-34"]),
        ("La pleuropneumonie est retenue chez 25 personnes, soit 2,1 pour cent de la cohorte.", ["PMC3853238-34"]),
        ("La bronchopneumopathie ou l’asthme sont retenus chez 23 personnes, soit 1,9 pour cent.", ["PMC3853238-34"]),
        ("Les autres diagnostics regroupent 52 personnes, ce qui représente 4,3 pour cent.", ["PMC3853238-34"]),
    ])
    out[8] += paras(S, P, q, [
        ("Le score coronarien attribue deux points lorsqu’un risque cardiovasculaire est déjà connu.", ["PMC2832616-20"]),
        ("Il attribue aussi deux points à l’homme de plus de 55 ans, ou à la femme de plus de 65 ans.", ["PMC2832616-20"]),
        ("L’antécédent cardiovasculaire personnel et la douleur rétrosternale valent également deux points chacun.", ["PMC2832616-20"]),
        ("La durée de une à soixante minutes, l’effort et l’absence de sensibilité valent un point chacun.", ["PMC2832616-20"]),
        ("L’aire sous la courbe de ce score vaut 0,946, avec un intervalle de 0,924 à 0,968.", ["PMC2832616-21"]),
        ("Dans la cohorte de dérivation, le coefficient de détermination de ce modèle vaut 0,538.", ["PMC2832616-21"]),
        ("Sous le score de 5, on compte 413 personnes, soit 62,5 pour cent.", ["PMC2832616-21"]),
        ("La sensibilité y atteint 97,6 pour cent, soit 83 cas sur 85.", ["PMC2832616-21"]),
        ("La spécificité y atteint 71,3 pour cent, soit 411 cas sur 576.", ["PMC2832616-21"]),
        ("À ce seuil bas, le rapport de vraisemblance négatif descend à 0,033.", ["PMC2832616-21"]),
        ("La valeur prédictive négative atteint 99,5 pour cent, soit 411 personnes sur 413.", ["PMC2832616-21"]),
        ("Au-dessus du score de 7, on compte 87 personnes, soit 13,2 pour cent.", ["PMC2832616-22"]),
        ("La zone intermédiaire du score compte 161 personnes, soit 24,4 pour cent.", ["PMC2832616-22"]),
        ("Les prévalences coronariennes observées sont de 0,5 pour cent, puis de 12,4 pour cent, puis de 72,4 pour cent.", ["PMC2832616-22"]),
        ("Un angor stable et un infarctus ont été observés dans les douze mois du groupe à score bas.", ["PMC2832616-21"]),
        ("Vingt-quatre décès ont été recensés pendant le suivi, dont quatre dans le groupe à score bas, sans maladie coronarienne.", ["PMC2832616-23"]),
        ("Soixante-douze électrocardiogrammes du groupe à bas risque représentaient 50,3 pour cent de tous les tracés.", ["PMC2832616-23"]),
        ("Moins d’un tiers des personnes à haut risque avaient reçu un électrocardiogramme.", ["PMC2832616-23"]),
        ("L’antécédent cardiovasculaire ajuste un rapport de 6,7, intervalle 3,2 à 13,8, et vaut deux points.", ["PMC2832616-38"]),
        ("La durée de une à soixante minutes porte un rapport ajusté de 3,0, intervalle 1,4 à 6,2.", ["PMC2832616-38"]),
        ("La douleur rétrosternale porte un rapport ajusté de 5,2, intervalle 2,5 à 10,9.", ["PMC2832616-38"]),
        ("L’augmentation à l’effort porte un rapport ajusté de 2,1, intervalle 1,0 à 4,3.", ["PMC2832616-38"]),
        ("L’absence de sensibilité à la palpation porte un rapport ajusté de 3,4, intervalle 1,5 à 8,0.", ["PMC2832616-38"]),
    ])
    out[9] += paras(S, P, q, [
        ("Dans ce sous-groupe de 43 personnes bien classées, trente électrocardiogrammes avaient été demandés.", ["PMC3444903-3"]),
        ("Seize radiographies de thorax avaient été demandées dans le même sous-groupe de 43 personnes.", ["PMC3444903-3"]),
    ])
    out[11] += paras(S, P, q, [
        ("La concentration synoviale atteint 8 à 13 µg par ml, six heures après une prise de 400 mg.", ["aips_irfen_dolo_fr-16"]),
        ("Le métabolisme hépatique concerne 50 à 60 pour cent de la dose.", ["aips_irfen_dolo_fr-16"]),
        ("La demi-vie plasmatique est de l’ordre de deux heures, selon la formulation retenue dans le texte.", ["aips_irfen_dolo_fr-16"]),
        ("Une concentration supérieure à 200 µg par ml à 4 heures annonce une lésion hépatique qui peut être fatale.", ["aips_dafalgan_500_fr-16"]),
        ("Le seuil atteint ensuite 100 µg par ml, à 8 heures après la prise.", ["aips_dafalgan_500_fr-16"]),
        ("Il passe encore à 50 µg par ml à 12 heures, puis à 30 µg par ml à 15 heures.", ["aips_dafalgan_500_fr-16"]),
        ("La toxicité de l’ibuprofène est rarement observée en dessous de 100 mg par kilogramme.", ["aips_irfen_dolo_fr-14"]),
        ("Chez l’enfant, des signes de surdosage peuvent apparaître dès 400 mg par kilogramme.", ["aips_irfen_dolo_fr-14"]),
        ("Les symptômes d’un surdosage d’ibuprofène surviennent habituellement en 4 à 6 heures.", ["aips_irfen_dolo_fr-14"]),
        ("Le texte ne fournit aucune donnée d’efficacité clinique pour le syndrome de paroi lui-même.", ["aips_irfen_dolo_fr-15"]),
        ("L’association à un autre anti-inflammatoire, y compris un coxib, est donc à éviter.", ["aips_irfen_dolo_fr-8"]),
        ("Les diurétiques, les inhibiteurs de l’enzyme de conversion et les bêtabloquants voient leur effet réduit, et le risque rénal augmente.", ["aips_irfen_dolo_fr-8"]),
        ("De 9 à 12 ans, le paracétamol ne dépasse pas 2000 mg par jour.", ["aips_dafalgan_500_fr-6"]),
        ("En pédiatrie, le plafond usuel du paracétamol est de 75 mg par kilogramme.", ["aips_dafalgan_500_fr-6"]),
        ("Les suppositoires de paracétamol ne sont pas répétés plus de quatre fois par jour.", ["aips_dafalgan_500_fr-6"]),
        ("La phénytoïne réduit l’effet antalgique et augmente les métabolites toxiques du paracétamol.", ["aips_dafalgan_500_fr-10"]),
        ("De 22 à 30 kg, soit de 6 à 9 ans, la prise va de 300 à 500 mg et le plafond journalier atteint 1,5 g.", ["aips_dafalgan_500_fr-6"]),
        ("De 30 à 40 kg, soit de 9 à 12 ans, la prise va donc de 400 à 600 mg et le plafond atteint 2 g.", ["aips_dafalgan_500_fr-6"]),
        ("Un comprimé effervescent de Dafalgan à 500 mg contient ainsi 197 mg de sodium.", ["aips_dafalgan_500_fr-2"]),
        ("Un comprimé effervescent de Dafalgan à 1 g contient ainsi 394 mg de sodium.", ["aips_dafalgan_500_fr-2"]),
        ("Le paracétamol prolonge donc par un facteur cinq la demi-vie d’élimination du chloramphénicol associé.", ["aips_dafalgan_500_fr-10"]),
        ("Un déficit en glucose-6-phosphate déshydrogénase peut entraîner une anémie hémolytique, donc un avis précède le paracétamol.", ["aips_dafalgan_500_fr-8"]),
        ("Une aggravation des infections cutanées, par exemple une fasciite nécrosante, a été décrite avec les anti-inflammatoires.", ["aips_irfen_dolo_fr-12"]),
        ("Si l’ibuprofène est pris après un repas, l’absorption devient plus lente et le pic plasmatique plus faible.", ["aips_irfen_dolo_fr-16"]),
        ("L’absorption orale du paracétamol est rapide, entre 10 et 60 minutes, et presque complète.", ["aips_dafalgan_500_fr-20"]),
        ("La biodisponibilité rectale est inférieure de 20 à 30 pour cent à celle de la voie orale.", ["aips_dafalgan_500_fr-20"]),
        ("Après 600 mg par voie rectale, le pic atteint 2,8 µg par ml en 2,9 heures.", ["aips_dafalgan_500_fr-20"]),
        ("Le comprimé effervescent de 500 mg atteint 6,4 µg par ml en 27 minutes.", ["aips_dafalgan_500_fr-20"]),
    ])
    return out
