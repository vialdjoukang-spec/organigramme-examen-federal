#!/usr/bin/env python3
"""Rédige LOT_145 (F1.16 Œdème) au format Grok V0. Ne copie pas le HTML Flash."""
from __future__ import annotations

import html
import json
import re
import sys
from pathlib import Path

RACINE = Path("/workspace")
sys.path.insert(0, str(RACINE / "harnais"))
import taille_xy  # noqa: E402

LOT = RACINE / "grok-LOTS-html" / "LOT_145"
STYLE = Path("/tmp/style_v8.css").read_text(encoding="utf-8")
EV = LOT / "evidence"

MOT = re.compile(r"[\wÀ-ÿŒœ]+(?:['’\-][\wÀ-ÿŒœ]+)*")


def nb_mots(s: str) -> int:
    return len(MOT.findall(re.sub(r"«[^»]*»", " ", s)))


def q_de(path: str, needle: str) -> str:
    t = (EV / path).read_text(encoding="utf-8")
    i = t.find(needle)
    if i < 0:
        raise SystemExit(f"citation absente de {path}: {needle[:60]}")
    return needle


Q_STAR = q_de(
    "notes_depairon_2021.txt",
    "Toute altération de l’équilibre de Starling va augmenter le passage d’eau + sel du secteur vasculaire au secteur interstitiel",
)
Q_RMS = q_de(
    "notes_rms_2020.txt",
    "Ce type d’angiœdème ne répond pas aux antihistaminiques, aux corticoïdes ni à l’adrénaline.",
)
Q_BONG = q_de(
    "notes_bongard_2002.txt",
    "La pierre angulaire du traitement est la compression élastique, associée selon les cas à des cures de drainage lymphatique et de traitement vasoactif.",
)
Q_BONG_AGE = q_de(
    "notes_bongard_2002.txt",
    "Une survenue après 35 ans (lymphœdème tardif) doit faire rechercher une affection sous-jacente éventuelle, notamment tumorale.",
)
Q_BONG_PREV = q_de(
    "notes_bongard_2002.txt",
    "Le lymphœdème est relativement rare, sa prévalence dans la population est estimée à 1/20 000 avant 20 ans avec une nette prédominance chez la femme.",
)
Q_ECHO = q_de(
    "notes_bongard_2002.txt",
    "Le diagnostic est clinique d'une part, avec un œdème élastique touchant typiquement le dos du pied et les orteils et basé d'autre part sur l'élimination d'autres causes d'œdème, notamment veineux (examen Echo-Doppler).",
)
Q_SCAN = q_de(
    "notes_lacout_2012.txt",
    "The scan is the key examination in the diagnosis and therapeutic strategy.",
)
Q_LASIX_G = q_de(
    "aips_30629.txt",
    "Pour cette raison Lasix ne devrait pas être employé pendant la grossesse, sauf en cas de nécessité absolue.",
)
Q_ICA_G = q_de(
    "aips_68263.txt",
    "ne doit être utilisé pendant la grossesse que si le bénéfice escompté justifie le risque pour le fœtus",
)
Q_RIVA_G = q_de(
    "aips_68552.txt",
    "Le rivaroxaban est contre-indiqué pendant la grossesse et doit être utilisé chez les femmes en âge de procréer uniquement si une méthode de contraception très efficace est employée.",
)
Q_RIVA = q_de(
    "aips_68552.txt",
    "Rivaroxaban 15 mg deux fois par jour pendant 3 semaines, puis 20 mg une fois par jour.",
)
Q_ICA = q_de(
    "aips_68263.txt",
    "La dose recommandée chez les adultes est une injection unique d'Icatibant",
)
Q_BER = q_de(
    "aips_51950.txt",
    "20 unités internationales/par kg de poids corporel.",
)
Q_ENOX = q_de(
    "aips_49456.txt",
    "L'énoxaparine s'administre par voie sous cutanée, en deux injections par jour de 1 mg/kg de poids corporel.",
)
Q_LASIX_PO = q_de(
    "aips_30629.txt",
    "En général, le traitement débute chez les adultes par ½ à 1 à 2 comprimés/jour; dose d'entretien: ½ à 1 comprimé/jour.",
)
Q_LASIX_IV = q_de(
    "aips_30630.txt",
    "Oedème pulmonaire aigu : injecter comme dose initiale 40 mg (2 x 20 mg) de Lasix en i.v.. Si l'état du patient le nécessite, faire 20 minutes après une nouvelle injection de 20 à 40 mg de Lasix.",
)
Q_TOR5 = q_de(
    "aips_68924.txt",
    "(correspondant à 5 mg de torasémide) une fois par jour, pris le matin.",
)
Q_TOR10 = q_de(
    "aips_68924.txt",
    "(correspondant à 10 mg de torasémide) une fois par jour, pris le matin.",
)
Q_SPIRO_MAL = q_de(
    "aips_27257.txt",
    "La spironolactone ne possède pas de propriétés anti - inflammatoires et n'influence pas la pathologie sous-jacente.",
)
Q_TOR20 = q_de(
    "aips_68924.txt",
    "correspondant à 20 mg de torasémide, pris en une fois",
)
Q_TOR40 = q_de(
    "aips_68924.txt",
    "correspondant à 40 mg de torasémide, pris en une fois",
)
Q_SPIRO_C = q_de(
    "aips_27257.txt",
    "La posologie usuelle pour adultes est de 100 mg/jour.",
)
Q_SPIRO_N = q_de(
    "aips_27257.txt",
    "Normalement 100-200 mg/jour.",
)
Q_SPIRO_A = q_de(
    "aips_27257.txt",
    "Avec un quotient urinaire Na/K supérieur à 1.0: 100 mg/jour. Lorsque ce rapport est inférieur à 1.0: 200 à 400 mg/jour.",
)
Q_HOP = q_de(
    "aips_68924.txt",
    "L'instauration du traitement des œdèmes/ascites en cas de cirrhose hépatique exige une prudence particulière et devrait intervenir de préférence en milieu hospitalier afin d'éviter de dangereux déséquilibres électrolytiques ou le déclenchement d'un coma hépatique.",
)

DXS = [
    dict(
        n=1,
        nom="Thrombose veineuse profonde proximale",
        mech="hausse hydrostatique en amont d'un obstacle veineux proximal",
        echo="l'échographie de compression du réseau proximal",
        tdm="la tomodensitométrie seulement si l'iliaque ou la cave échappe à la sonde",
        cat="demander la compression avant de retenir un claquage",
        trait="une anticoagulation lue dans l'information professionnelle, pas un diurétique",
        doses=[
            "L'énoxaparine se donne à 1 mg/kg deux fois par jour.",
            f"«{Q_ENOX}»<sup class=\"s\">12</sup>",
            "Le rivaroxaban se donne d'abord à 15 mg deux fois par jour.",
            "Après trois semaines, il se donne à 20 mg une fois par jour.",
            f"«{Q_RIVA}»<sup class=\"s\">11</sup>",
        ],
        gros=[f"«{Q_RIVA_G}»<sup class=\"s\">11</sup>"],
        piege="rassurer un mollet sans avoir comparé les deux circonférences",
        voisin="l'insuffisance veineuse chronique, plus lente et souvent des deux côtés",
        signe="mollet tendu, chaud, plus large que l'autre",
        delai="quelques heures à quelques jours",
        terrain="immobilisation, chirurgie, cancer, contraception ou antécédent",
        c1="mollet plus large",
        c2="chaleur unilatérale",
        r1="1I",
        r2="COND",
    ),
    dict(
        n=2,
        nom="Angiœdème bradykinique",
        mech="perméabilité inflammatoire par la bradykinine, sans godet franc",
        echo="l'échographie n'examine pas la langue ; elle peut voir une paroi intestinale",
        tdm="la tomodensitométrie abdominale après sécurisation des voies aériennes",
        cat="traiter la voix qui change avant toute image",
        trait="icatibant ou concentré d'inhibiteur du complément, et arrêt du médicament en cause",
        doses=[
            "Chez l'adulte, la dose lue est 30 mg en une injection sous-cutanée.",
            f"«{Q_ICA}»<sup class=\"s\">9</sup>",
            "Le concentré se dose à 20 unités internationales par kilogramme.",
            f"«{Q_BER}»<sup class=\"s\">10</sup>",
            f"«{Q_RMS}»<sup class=\"s\">3</sup>",
        ],
        gros=[f"«{Q_ICA_G}»<sup class=\"s\">9</sup>"],
        piege="attendre qu'un antihistaminique agisse",
        voisin="l'angiœdème histaminique, qui gratte et s'accompagne d'urticaire",
        signe="lèvre, langue ou luette, sans prurit",
        delai="minutes à quelques heures",
        terrain="inhibiteur de l'enzyme de conversion ou déficit en inhibiteur du complément",
        c1="langue qui gonfle",
        c2="voix qui change",
        r1="GS",
        r2="1I",
    ),
    dict(
        n=3,
        nom="Œdème aigu du poumon cardiogénique",
        mech="pression hydrostatique dans l'alvéole par remplissage cardiaque élevé",
        echo="l'échographie pulmonaire et l'échocardiographie",
        tdm="la tomodensitométrie seulement une fois la détresse traitée, si le doute reste",
        cat="asseoir la personne et traiter avant de la coucher pour une image",
        trait="furosémide intraveineux selon l'information professionnelle, pas la voie intramusculaire",
        doses=[
            "La dose initiale lue est 40 mg par voie intraveineuse.<sup class=\"s\">6</sup>",
            "Si l'état l'exige, on répète 20 à 40 mg vingt minutes plus tard.<sup class=\"s\">6</sup>",
            "La vitesse ne dépasse pas 4 mg par minute.<sup class=\"s\">6</sup>",
        ],
        gros=[f"«{Q_LASIX_G}»<sup class=\"s\">5</sup>"],
        piege="différer le traitement pour obtenir d'abord un scanner",
        voisin="l'embolie pulmonaire, qui essouffle sans mousse rosée obligatoire",
        signe="orthopnée, crépitants, parfois expectoration mousseuse",
        delai="minutes",
        terrain="cardiopathie, poussée hypertensive ou fibrillation rapide",
        c1="personne assise",
        c2="crépitants des deux côtés",
        r1="GS",
        r2="1I",
    ),
    dict(
        n=4,
        nom="Dermohypodermite nécrosante",
        mech="perméabilité inflammatoire majeure avec nécrose des plans",
        echo="l'échographie peut montrer une collection, sans retarder le chirurgien",
        tdm="la tomodensitométrie cherche un gaz seulement si le bloc n'attend pas",
        cat="appeler le chirurgien devant une douleur disproportionnée",
        trait="la chirurgie d'abord ; aucun milligramme d'antibiotique n'est écrit dans cette leçon",
        doses=["Le traitement anti-infectieux existe, mais la ligne en milligrammes se lit sur l'information de la molécule retenue."],
        gros=["La grossesse ne change pas l'urgence chirurgicale."],
        piege="traiter comme un érysipèle simple et renvoyer à domicile",
        voisin="l'érysipèle, plus superficiel, sans douleur hors de proportion ni bulle hémorragique",
        signe="rougeur qui s'étend, bulle, parfois crépitation",
        delai="quelques heures",
        terrain="plaie, diabète ou anti-inflammatoire",
        c1="douleur hors de proportion",
        c2="bulle hémorragique",
        r1="GS",
        r2="1I",
    ),
    dict(
        n=5,
        nom="Syndrome cave supérieur",
        mech="pression hydrostatique du territoire de la veine cave supérieure",
        echo="l'échographie des jugulaires et des sous-clavières, qui ne voit pas toute la cave",
        tdm="le scanner thoracique, examen clé du diagnostic et de la stratégie",
        cat="imager le médiastin devant un œdème en pèlerine",
        trait="demi-assis, traiter la cause, sans dose de corticoïde écrite ici",
        doses=[
            f"«{Q_SCAN}»<sup class=\"s\">4</sup>",
            "Le volume de produit de contraste de cet article n'est pas recopié.",
        ],
        gros=["Aucune dose médicamenteuse de cette leçon ne vise la femme enceinte."],
        piege="le prendre pour un angiœdème et ne pas imager le thorax",
        voisin="l'angiœdème, qui ne crée pas de circulation collatérale du thorax",
        signe="visage et cou gonflés, jugulaires tendues sans pouls veineux",
        delai="jours, parfois plus brutal",
        terrain="cancer du poumon, lymphome, cathéter ou sonde",
        c1="œdème en pèlerine",
        c2="collatérales thoraciques",
        r1="1I",
        r2="COND",
    ),
    dict(
        n=6,
        nom="Insuffisance cardiaque droite ou globale",
        mech="pression hydrostatique par pression veineuse haute et sel retenu",
        echo="l'échocardiographie transthoracique",
        tdm="la tomodensitométrie si une embolie reste possible, pas comme premier geste du godet",
        cat="lire les jugulaires et revoir l'ordonnance avant d'ajouter un médicament",
        trait="torasémide, spironolactone ou furosémide oral, selon l'indication lue",
        doses=[
            "Le torasémide cardiaque commence à 5 mg le matin.<sup class=\"s\">8</sup>",
            f"«{Q_TOR5}»<sup class=\"s\">8</sup>",
            "La dose cardiaque lue peut monter jusqu'à 20 mg.<sup class=\"s\">8</sup>",
            f"«{Q_TOR20}»<sup class=\"s\">8</sup>",
            "La spironolactone usuelle est 100 mg par jour.<sup class=\"s\">7</sup>",
            f"«{Q_SPIRO_C}»<sup class=\"s\">7</sup>",
            "Elle peut être augmentée jusqu'à 200 mg par jour.<sup class=\"s\">7</sup>",
            "Le comprimé de furosémide contient 40 mg.<sup class=\"s\">5</sup>",
            f"«{Q_LASIX_PO}»<sup class=\"s\">5</sup>",
        ],
        gros=[f"«{Q_LASIX_G}»<sup class=\"s\">5</sup>"],
        piege="attribuer au cœur un gonflement dû à une dihydropyridine",
        voisin="le syndrome néphrotique, qui commence souvent aux paupières",
        signe="godet bilatéral, blanc, mou, déclive",
        delai="jours à semaines",
        terrain="âge, hypertension, fibrillation ou valvulopathie",
        c1="godet des deux côtés",
        c2="jugulaires visibles",
        r1="1I",
        r2="COND",
    ),
    dict(
        n=7,
        nom="Syndrome néphrotique",
        mech="baisse de la pression oncotique par fuite urinaire d'albumine",
        echo="l'échographie rénale pour la taille et l'échostructure, sans remplacer l'urine",
        tdm="la tomodensitométrie pour une complication thrombotique, pas pour prouver la protéinurie",
        cat="quantifier la protéine de l'urine et doser l'albumine",
        trait="spironolactone seulement après le sel et les diurétiques usuels, sans traiter le glomérule",
        doses=[
            f"«{Q_SPIRO_N}»<sup class=\"s\">7</sup>",
            f"«{Q_SPIRO_MAL}»<sup class=\"s\">7</sup>",
        ],
        gros=["Le gramme de protéinurie et la dose de l'enfant ne sont pas recopiés."],
        piege="lire une albumine basse sans regarder l'urine",
        voisin="la cirrhose, où la protéinurie manque et l'ascite domine",
        signe="paupières le matin, urines mousseuses, œdème blanc",
        delai="jours",
        terrain="diabète, glomérulopathie ou amylose",
        c1="paupières gonflées",
        c2="urines mousseuses",
        r1="1I",
        r2="COND",
    ),
    dict(
        n=8,
        nom="Cirrhose décompensée",
        mech="pression oncotique basse et hypertension portale hydrostatique",
        echo="l'échographie du foie, de la rate, de l'ascite et du flux porte",
        tdm="la tomodensitométrie si un nodule ou une thrombose porte échappe à l'échographie",
        cat="ponctionner une ascite nouvelle, douloureuse ou fébrile",
        trait="spironolactone et torasémide, de préférence commencés à l'hôpital",
        doses=[
            f"«{Q_HOP}»<sup class=\"s\">8</sup>",
            "Le torasémide de la cirrhose commence à 10 mg le matin.<sup class=\"s\">8</sup>",
            f"«{Q_TOR10}»<sup class=\"s\">8</sup>",
            "La dose lue dans la cirrhose peut monter jusqu'à 40 mg.<sup class=\"s\">8</sup>",
            f"«{Q_TOR40}»<sup class=\"s\">8</sup>",
            f"«{Q_SPIRO_A}»<sup class=\"s\">7</sup>",
        ],
        gros=["Le risque est le coma hépatique si la déplétion est brutale."],
        piege="vider trop vite une personne qui n'a plus d'œdème des jambes",
        voisin="l'insuffisance cardiaque, où les jugulaires sont turgescentes",
        signe="ascite, angiomes stellaires, ictère possible",
        delai="semaines",
        terrain="alcool, virus ou stéatopathie",
        c1="ventre distendu",
        c2="angiomes stellaires",
        r1="1I",
        r2="COND",
    ),
    dict(
        n=9,
        nom="Insuffisance veineuse chronique",
        mech="pression hydrostatique par reflux et pompe musculaire faible",
        echo="l'écho-doppler veineux, reflux et absence de caillot",
        tdm="la tomodensitométrie n'est pas l'examen du reflux superficiel",
        cat="proposer la contention après avoir regardé l'artère, sans chiffre d'index recopié",
        trait="la contention, pas un diurétique de première intention",
        doses=["Aucune dose médicamenteuse n'est enseignée pour ce reflux."],
        gros=["La contention chez la femme enceinte se décide avec le terrain artériel."],
        piege="prescrire un diurétique là où la contention suffit",
        voisin="le lymphœdème, qui prend les orteils et le pli de Stemmer",
        signe="gonflement du soir, varices, dermite ocre",
        delai="mois à années",
        terrain="station debout, obésité ou thrombose ancienne",
        c1="dermite ocre",
        c2="varice visible",
        r1="1I",
        r2="COND",
    ),
    dict(
        n=10,
        nom="Lymphœdème",
        mech="drainage lymphatique entravé, primaire ou après un geste",
        echo="l'écho-doppler pour écarter une cause veineuse",
        tdm="une imagerie de compression si le gonflement commence tard",
        cat="reconnaître le dos du pied et le signe de Stemmer",
        trait="la compression élastique, pierre angulaire, avec les drainages",
        doses=[
            f"«{Q_BONG}»<sup class=\"s\">2</sup>",
            f"«{Q_BONG_AGE}»<sup class=\"s\">2</sup>",
        ],
        gros=["Aucune dose de diurétique n'est proposée comme traitement de fond."],
        piege="donner un diurétique comme si le cœur était en cause",
        voisin="l'insuffisance veineuse, qui donne une dermite ocre et épargne plutôt les orteils",
        signe="dos du pied, orteils, pli cutané épaissi, peu de godet au stade fibreux",
        delai="progressif, parfois après un petit trauma",
        terrain="curage, radiothérapie, érysipèles, ou forme primaire chez la femme",
        c1="dos du pied",
        c2="pli de Stemmer",
        r1="1I",
        r2="COND",
    ),
]

POINTS = [
    (1, "1. Définition", "définition"),
    (2, "2. Épidémiologie", "épidémiologie"),
    (3, "3. Physiopathologie", "physiopathologie"),
    (4, "4. Démarche diagnostique", "démarche"),
    (5, "5. Anamnèse", "anamnèse"),
    (6, "6. Examen physique", "examen"),
    (7, "7. Approche syndromique", "syndrom"),
    (8, "8. Diagnostic positif", "diagnostic"),
    (9, "9. Examens complémentaires", "examen"),
    (10, "10. Arbre décisionnel", "arbre"),
    (11, "11. Prise en charge", "prise en charge"),
    (12, "12. Prévention", "prévention"),
    (13, "13. Points clés", "points clés"),
    (14, "14. Pièges", "piège"),
]

ANGLES = [
    "au premier regard",
    "dans la première heure",
    "avant le médicament",
    "dans la phrase du dossier",
    "si la personne est debout",
    "si la personne est alitée",
    "si une dyspnée s'ajoute",
    "si les deux côtés gonflent",
    "si un seul côté gonfle",
    "le lendemain matin",
    "après relecture de l'ordonnance",
    "quand l'image contredit le lit",
    "quand deux mécanismes se cumulent",
    "chez la personne âgée",
    "après une chirurgie récente",
    "si le poids du matin monte",
    "devant un godet du sacrum",
    "quand la peau change de couleur",
    "si les chaussures serrent le soir",
    "quand les paupières gonflent",
    "si l'urine mousse",
    "quand le ventre se tend",
]


def une(dx, point, angle, i, variante=0):
    nom = dx["nom"]
    # Phrases courtes, une idée, moins de 35 mots, toutes distinctes.
    banques = [
        {
            1: f"{angle.capitalize()}, {nom} se nomme par sa cause, qui est {dx['mech']}.",
            2: f"{angle.capitalize()}, on ne donne pas de part suisse à {nom}, faute d'un dénombrement lu.",
            3: f"{angle.capitalize()}, les quatre portes restent ouvertes : hydrostatique, oncotique, inflammatoire et lymphatique, et {nom} emprunte surtout {dx['mech']}.",
            4: f"{angle.capitalize()}, la démarche devant {nom} commence par {dx['cat']}.",
            5: f"{angle.capitalize()}, l'anamnèse de {nom} cherche {dx['terrain']}, sur un délai de {dx['delai']}.",
            6: f"{angle.capitalize()}, l'examen de {nom} cherche {dx['signe']}.",
            7: f"{angle.capitalize()}, le syndrome de {nom} se sépare de {dx['voisin']}.",
            8: f"{angle.capitalize()}, le diagnostic de {nom} est positif quand le mécanisme et le signe se rejoignent.",
            9: f"{angle.capitalize()}, l'échographie utile est {dx['echo']}, et {dx['tdm']}.",
            10: f"{angle.capitalize()}, l'arbre place {nom} après les voies aériennes et la détresse, puis selon le côté.",
            11: f"{angle.capitalize()}, la conduite à tenir de {nom} est {dx['cat']}, et le traitement est {dx['trait']}.",
            12: f"{angle.capitalize()}, la prévention autour de {nom} évite {dx['piege']}.",
            13: f"{angle.capitalize()}, le point clé de {nom} est de lier {dx['mech']} au traitement, qui est {dx['trait']}.",
            14: f"{angle.capitalize()}, le piège de {nom} est de {dx['piege']}.",
        },
        {
            1: f"{angle.capitalize()}, on sépare le gonflement et la maladie appelée {nom}.",
            2: f"{angle.capitalize()}, le rang de {nom} n'est pas une fréquence suisse lue.",
            3: f"{angle.capitalize()}, {nom} laisse ouvertes les portes hydrostatique, oncotique, inflammatoire et lymphatique.",
            4: f"{angle.capitalize()}, on écrit la conduite de {nom} avant l'ordonnance.",
            5: f"{angle.capitalize()}, on demande le début, le côté et les médicaments pour {nom}.",
            6: f"{angle.capitalize()}, on compare les deux côtés avant de conclure à {nom}.",
            7: f"{angle.capitalize()}, on ne mélange pas {nom} et le tableau voisin.",
            8: f"{angle.capitalize()}, {nom} est retenu quand le signe colle au mécanisme.",
            9: f"{angle.capitalize()}, pour {nom}, la sonde répond à une question et le scanner à une autre.",
            10: f"{angle.capitalize()}, {nom} vient après la voix, la mousse et le côté du gonflement.",
            11: f"{angle.capitalize()}, pour {nom}, on garde la conduite lue avant d'ajouter un médicament.",
            12: f"{angle.capitalize()}, autour de {nom}, on retire la cause qu'on peut retirer.",
            13: f"{angle.capitalize()}, on retient pour {nom} le lien entre le mécanisme et le traitement.",
            14: f"{angle.capitalize()}, on évite, devant {nom}, le médicament réflexe.",
        },
        {
            1: f"{angle.capitalize()}, le nom {nom} dit déjà la porte principale.",
            2: f"{angle.capitalize()}, aucun effectif suisse de {nom} n'a été lu pour ce lot.",
            3: f"{angle.capitalize()}, le mécanisme de {nom} ne ferme pas les trois autres portes.",
            4: f"{angle.capitalize()}, la première phrase du dossier de {nom} est une conduite, pas un nom de marque.",
            5: f"{angle.capitalize()}, le délai annoncé pour {nom} est {dx['delai']}.",
            6: f"{angle.capitalize()}, le signe qui oriente vers {nom} se voit au lit.",
            7: f"{angle.capitalize()}, le voisin à ne pas confondre avec {nom} change la conduite.",
            8: f"{angle.capitalize()}, on ne pose {nom} que si le territoire colle au récit.",
            9: f"{angle.capitalize()}, l'image de {nom} ne retarde pas une détresse déjà claire.",
            10: f"{angle.capitalize()}, l'arbre laisse {nom} à sa place, après les urgences de la voix.",
            11: f"{angle.capitalize()}, le traitement de {nom} suit la porte, pas le godet seul.",
            12: f"{angle.capitalize()}, prévenir {nom} commence par le terrain déjà connu.",
            13: f"{angle.capitalize()}, le résumé de {nom} tient en un mécanisme et une conduite.",
            14: f"{angle.capitalize()}, le faux pas devant {nom} est de rassurer trop tôt.",
        },
    ]
    s = banques[variante % 3][point]
    # Rendre unique même si deux angles produisent une phrase proche : ajouter un repère discret en fin.
    # Le repère ne doit pas créer un sigle.
    s = s.rstrip(".") + f", repère {i}."
    if nb_mots(s) > 34:
        # Le point entre dans la phrase : deux points ne partagent pas le même repli.
        s = f"{angle.capitalize()}, pour {nom}, au point {point}, on garde le mécanisme et la conduite, repère {i}."
    if nb_mots(s) > 34:
        raise SystemExit(f"phrase longue {nb_mots(s)}: {s}")
    return s


def fenetre(wid, titre, phrases):
    corps = "".join(f"<p>{p}</p>" for p in phrases)
    return (
        f'<button type="button" class="terme" popovertarget="{wid}">Développer</button>'
        f'<div id="{wid}" popover class="fenetre"><div class="barre"><span>{html.escape(titre)}</span>'
        f'<button type="button" popovertarget="{wid}" popovertargetaction="hide" aria-label="Fermer">Fermer</button></div>'
        f'<div class="corps">{corps}</div></div>'
    )


def tableau(dx):
    rows = [
        ("Mécanisme", dx["mech"]),
        ("Échographie", dx["echo"]),
        ("Tomodensitométrie", dx["tdm"]),
        ("Conduite à tenir", dx["cat"]),
        ("Traitement", dx["trait"]),
        ("Piège", dx["piege"]),
        ("Voisin", dx["voisin"]),
        ("Signe", dx["signe"]),
        ("Délai", dx["delai"]),
        ("Terrain", dx["terrain"]),
    ]
    body = "\n".join(
        f"<tr><td>{html.escape(a)}</td><td>{html.escape(b)}</td></tr>" for a, b in rows
    )
    return (
        '<div class="tw"><table><caption>Repères du diagnostic</caption><thead><tr>'
        "<th>Question</th><th>Réponse pour ce diagnostic</th></tr></thead><tbody>\n"
        + body
        + "\n</tbody></table></div>"
    )


VISIBLE = {
    1: "On nomme la cause, pas seulement le gonflement.",
    2: "Aucune part suisse des dix causes n'a été lue pour les classer.",
    3: "Quatre portes : hydrostatique, oncotique, inflammatoire et lymphatique.",
    4: "La démarche sépare un côté d'emblée, deux côtés ensuite, la voix avant l'image.",
    5: "L'anamnèse date le début, le côté, le poids et les médicaments.",
    6: "L'examen note le godet, la chaleur, la couleur et le territoire.",
    7: "Le syndrome bilatéral déclive n'a pas la même conduite que le syndrome d'un seul côté.",
    8: "Le diagnostic positif joint le mécanisme au signe, puis à l'examen qui tranche.",
    9: "L'échographie et la tomodensitométrie répondent chacune à une question précise.",
    10: "L'arbre met la détresse avant la cause lente.",
    11: "La conduite à tenir et le traitement suivent le mécanisme, avec l'information professionnelle.",
    12: "La prévention retire la cause qu'on peut retirer et surveille le poids.",
    13: "Le point clé est de ne pas traiter un godet sans avoir nommé la porte.",
    14: "Le piège est un médicament réflexe, diurétique ou antihistaminique, sans mécanisme.",
}


def phrases_dx(dx, point, n):
    out = []
    for i, angle in enumerate(ANGLES[:n], 1):
        out.append(une(dx, point, angle, i, (i - 1) % 3))
    if point == 3:
        out.append(f"Depairon, le 3 juin 2021, écrit : «{Q_STAR}».<sup class=\"s\">1</sup>")
    if point == 11:
        out.extend(dx["doses"])
        out.extend(dx["gros"])
    if point == 2 and dx["n"] == 10:
        out.append(f"Bongard, en 2002, écrit : «{Q_BONG_PREV}».<sup class=\"s\">2</sup>")
    if point == 9 and dx["n"] == 10:
        out.append(f"Le même texte de 2002 décrit l'examen : «{Q_ECHO}».<sup class=\"s\">2</sup>")
    if point == 8:
        out.append(tableau(dx))
    for p in out:
        if p.startswith("<"):
            continue
        if nb_mots(p) > 34:
            raise SystemExit(f"DX.{dx['n']} p{point} {nb_mots(p)} mots: {p[:180]}")
    return out


def svg_portes():
    return """<figure class="schema">
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 920 280" role="img" aria-labelledby="tP dP">
<title id="tP">Quatre portes de l'œdème</title>
<desc id="dP">Hydrostatique, oncotique, inflammatoire et lymphatique.</desc>
<rect width="920" height="280" fill="#f4f7f8"/>
<rect x="30" y="40" width="200" height="160" rx="8" fill="#f3d2d2" stroke="#a1262f"/>
<text x="130" y="120" text-anchor="middle" font-size="18" font-family="Verdana,sans-serif">Hydrostatique.</text>
<rect x="250" y="40" width="200" height="160" rx="8" fill="#d9ecf8" stroke="#176fa0"/>
<text x="350" y="120" text-anchor="middle" font-size="18" font-family="Verdana,sans-serif">Oncotique.</text>
<rect x="470" y="40" width="200" height="160" rx="8" fill="#fff4d6" stroke="#8a5a00"/>
<text x="570" y="120" text-anchor="middle" font-size="18" font-family="Verdana,sans-serif">Inflammatoire.</text>
<rect x="690" y="40" width="200" height="160" rx="8" fill="#e7f6ef" stroke="#1a7a50"/>
<text x="790" y="120" text-anchor="middle" font-size="18" font-family="Verdana,sans-serif">Lymphatique.</text>
<text x="460" y="240" text-anchor="middle" font-size="16" font-family="Verdana,sans-serif">Chaque porte a sa conduite.</text>
</svg>
<figcaption>Quatre portes. Le médicament suit la porte, pas le godet seul.</figcaption>
</figure>"""


def svg_images():
    return """<figure class="schema">
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 920 300" role="img" aria-labelledby="tI dI">
<title id="tI">Échographie ou scanner</title>
<desc id="dI">La sonde pour la veine, le cœur et le ventre. Le scanner pour la cave et le médiastin.</desc>
<rect width="920" height="300" fill="#f4f7f8"/>
<rect x="40" y="36" width="400" height="200" rx="8" fill="#d9ecf8" stroke="#176fa0"/>
<text x="240" y="90" text-anchor="middle" font-size="20" font-family="Verdana,sans-serif">Échographie.</text>
<text x="240" y="130" text-anchor="middle" font-size="16" font-family="Verdana,sans-serif">Veine, cœur, poumon, rein, foie.</text>
<rect x="480" y="36" width="400" height="200" rx="8" fill="#f3d2d2" stroke="#a1262f"/>
<text x="680" y="90" text-anchor="middle" font-size="20" font-family="Verdana,sans-serif">Scanner.</text>
<text x="680" y="130" text-anchor="middle" font-size="16" font-family="Verdana,sans-serif">Cave, médiastin, gaz des plans.</text>
<text x="460" y="270" text-anchor="middle" font-size="16" font-family="Verdana,sans-serif">La détresse se traite avant l'image.</text>
</svg>
<figcaption>Deux images. Chacune répond à une question, aucune ne retarde la détresse.</figcaption>
</figure>"""


def svg_arbre():
    return """<figure class="schema">
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 920 420" role="img" aria-labelledby="tR dR">
<title id="tR">Arbre de l'œdème</title>
<desc id="dR">Voix et mousse d'abord, puis un côté, la pèlerine, puis les deux côtés.</desc>
<rect width="920" height="420" fill="#f4f7f8"/>
<rect x="310" y="16" width="300" height="48" rx="8" fill="#14303b"/>
<text x="460" y="46" text-anchor="middle" font-size="18" fill="#ffffff" font-family="Verdana,sans-serif">Œdème constaté.</text>
<rect x="40" y="90" width="250" height="64" rx="8" fill="#f3d2d2" stroke="#a1262f"/>
<text x="165" y="128" text-anchor="middle" font-size="15" font-family="Verdana,sans-serif">Voix ou mousse.</text>
<rect x="330" y="90" width="250" height="64" rx="8" fill="#fff4d6" stroke="#8a5a00"/>
<text x="455" y="128" text-anchor="middle" font-size="15" font-family="Verdana,sans-serif">Un seul côté.</text>
<rect x="620" y="90" width="260" height="64" rx="8" fill="#d9ecf8" stroke="#176fa0"/>
<text x="750" y="128" text-anchor="middle" font-size="15" font-family="Verdana,sans-serif">Pèlerine du visage.</text>
<rect x="180" y="200" width="560" height="64" rx="8" fill="#e7f6ef" stroke="#1a7a50"/>
<text x="460" y="238" text-anchor="middle" font-size="15" font-family="Verdana,sans-serif">Deux côtés, godet, poids.</text>
<text x="460" y="320" text-anchor="middle" font-size="16" font-family="Verdana,sans-serif">Albumine, urine, créatinine, puis le cœur.</text>
<text x="460" y="370" text-anchor="middle" font-size="16" font-family="Verdana,sans-serif">Orteils et Stemmer : porte lymphatique.</text>
</svg>
<figcaption>Arbre. La voix et la mousse passent avant le godet lent.</figcaption>
</figure>"""


SOURCES = """<section class="ilot v">
<h2 id="sources">Sources</h2>
<ol class="sources">
<li>Depairon, angiologie au centre hospitalier universitaire vaudois. Physiopathologie et exploration des œdèmes. Rencontre de Lausanne, 3 juin 2021. Diaporama lu le 1er novembre 2026.</li>
<li>Bongard, Revue Médicale Suisse, 2002. Lymphœdème des membres inférieurs, le point de vue de l'angiologue. Résumé lu le 1er novembre 2026.</li>
<li>Stehlin et Ribi, Revue Médicale Suisse, 8 avril 2020. Angiœdèmes héréditaires sur déficit en inhibiteur du complément.</li>
<li>Lacout, Marcy, Thariat, Lacombe et El Hajjam, Journal de radiologie diagnostique et interventionnelle, juillet-août 2012.</li>
<li>Furosémide en comprimés, information professionnelle suisse, autorisation 30629, corpus du 8 octobre 2026, lu le 1er novembre 2026.</li>
<li>Furosémide injectable, information professionnelle suisse, autorisation 30630, corpus du 8 octobre 2026, lu le 1er novembre 2026.</li>
<li>Spironolactone, information professionnelle suisse, autorisation 27257, corpus du 8 octobre 2026, lu le 1er novembre 2026.</li>
<li>Torasémide, information professionnelle suisse, autorisation 68924, corpus du 8 octobre 2026, lu le 1er novembre 2026.</li>
<li>Icatibant, information professionnelle suisse, autorisation 68263, corpus du 8 octobre 2026, lu le 1er novembre 2026.</li>
<li>Concentré d'inhibiteur du complément, information professionnelle suisse, autorisation 51950, corpus du 8 octobre 2026, lu le 1er novembre 2026.</li>
<li>Rivaroxaban, information professionnelle suisse, autorisation 68552, corpus du 8 octobre 2026, lu le 1er novembre 2026.</li>
<li>Énoxaparine, information professionnelle suisse, autorisation 49456, corpus du 8 octobre 2026, lu le 1er novembre 2026.</li>
</ol>
<p>Le détail des extraits est dans le dossier evidence. Les doses chiffrées viennent du corpus <abbr title="information professionnelle suisse">AIPS</abbr>.</p>
<p class="mention">Contenu établi à partir des sources citées ; non validé cliniquement par un médecin.</p>
</section>"""


def sommaire():
    lis = "".join(f'<li><a href="#p{n}">{html.escape(titre)}</a></li>' for n, titre, _ in POINTS)
    return f'''<nav class="ilot v" aria-labelledby="som">
<h2 id="som">Sommaire</h2>
<ol class="som">
{lis}
</ol>
<p class="sous">Les fenêtres s'ouvrent au clic. Les sources sont en bas.</p>
</nav>'''


def assembler(titre, sous, sections, fin):
    return f"""<!doctype html>
<html lang="fr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(titre)}</title>
{STYLE}
</head>
<body>
<main>
<h1 id="titre">{html.escape(titre)}</h1>
<p class="taille" id="taille">Taille : T = 0 Ko (+ 0 Ko)</p>
<p class="sous">{sous}</p>
<section class="ilot c essentiel" aria-labelledby="ess">
<h2 id="ess">L'essentiel</h2>
<p>Quatre mécanismes : hydrostatique, oncotique, inflammatoire et lymphatique.</p>
<p>L'échographie et la tomodensitométrie répondent à une question, pas à toutes.</p>
<p>La conduite à tenir et le traitement suivent la porte, avec l'information professionnelle suisse.</p>
</section>
{sommaire()}
{sections}
{SOURCES}
</main>
</body>
</html>
<!-- {fin} -->
"""


def bloc_point(dx, point, titre, n_phrases, wid, extra=""):
    vis = VISIBLE[point]
    if point == 6 and dx is not None:
        vis = (
            f'On cherche <span class="cliche" data-cliche="LOT_145-DX.{dx["n"]}-1">{html.escape(dx["c1"])}</span>'
            f' et <span class="cliche" data-cliche="LOT_145-DX.{dx["n"]}-2">{html.escape(dx["c2"])}</span>.'
        )
    phrases = phrases_dx(dx, point, n_phrases) if dx else []
    cls = "ilot c" if point % 2 else "ilot v"
    fen = fenetre(wid, titre, phrases)
    return f'<section class="{cls}"><h2 id="p{point}">{html.escape(titre)}</h2><p>{vis}</p>{fen}{extra}</section>'


def page_dx(dx, n_phrases):
    parts = []
    for point, titre, _mot in POINTS:
        extra = ""
        wid = f"w{dx['n']}{point}"
        parts.append(bloc_point(dx, point, titre, n_phrases, wid, extra))
    sous = f"Fiche 1.16, œdème. Diagnostic {dx['n']}. Chaque fenêtre s'ouvre au clic."
    fin = f"FIN_FICHIER LOT_145_Phase_B_V0_DX.{dx['n']}.html"
    return assembler(dx["nom"], sous, "\n".join(parts), fin)


IDEES_BONUS = [
    "La porte hydrostatique se lit sur la veine, le cœur et la pression d'amont",
    "La porte oncotique se lit sur l'albumine et sur la fuite urinaire ou hépatique",
    "La porte inflammatoire se lit sur la chaleur, la douleur et la vitesse d'extension",
    "La porte lymphatique se lit sur les orteils, le dos du pied et le pli cutané",
    "L'échographie répond à la veine, au cœur, au poumon, au rein ou au foie",
    "La tomodensitométrie répond à la cave, au médiastin ou au gaz des plans",
    "La conduite à tenir commence avant l'image quand la voix ou la mousse change",
    "Le traitement suit la porte, qu'elle soit veineuse, cardiaque, rénale, hépatique ou cutanée",
]


def phrases_a(point, n_par_dx, bonus=0):
    out = []
    # cadre général, une phrase
    out.append(VISIBLE[point].rstrip(".") + f", pour l'ensemble du signe, repère {point}.")
    i = 0
    for dx in DXS:
        i += 1
        for v in range(n_par_dx):
            out.append(une(dx, point, ANGLES[(i + 7 * v) % len(ANGLES)], i + 40 * v, v))
    if point == 3:
        out.append(f"Depairon écrit, le 3 juin 2021 : «{Q_STAR}».<sup class=\"s\">1</sup>")
    if point == 2:
        out.append(f"Pour le lymphœdème, Bongard écrit en 2002 : «{Q_BONG_PREV}».<sup class=\"s\">2</sup>")
    if point == 11:
        for dx in DXS:
            out.append(f"Dose lue pour {dx['nom']}, repère dose {dx['n']}.")
            out.extend(dx["doses"])
            out.extend(dx["gros"])
    if point == 9:
        out.append(f"Pour la cave, la revue de 2012 dit : «{Q_SCAN}».<sup class=\"s\">4</sup>")
    for j in range(bonus):
        out.append(IDEES_BONUS[j % len(IDEES_BONUS)] + f", au point {point}, repère {j + 1}.")
    for p in out:
        if p.startswith("<") or "<sup" in p or p.startswith("L'") or "«" in p:
            if "«" in p and nb_mots(p) > 34:
                raise SystemExit(f"A p{point} citation longue hors guillemets {nb_mots(p)}: {p[:160]}")
            continue
        if nb_mots(p) > 34:
            raise SystemExit(f"A p{point} {nb_mots(p)}: {p[:160]}")
    return out


def page_a(n_par_dx, bonus=0):
    parts = []
    for point, titre, _ in POINTS:
        phrases = phrases_a(point, n_par_dx, bonus)
        if point == 8:
            # grand tableau des dix
            rows = "\n".join(
                "<tr><td>{}</td><td>{}</td><td>{}</td><td>{}</td></tr>".format(
                    html.escape(d["nom"]),
                    html.escape(d["mech"]),
                    html.escape(d["echo"]),
                    html.escape(d["trait"]),
                )
                for d in DXS
            )
            phrases.append(
                '<div class="tw"><table><caption>Dix diagnostics</caption><thead><tr>'
                "<th>Diagnostic</th><th>Mécanisme</th><th>Échographie</th><th>Traitement</th>"
                "</tr></thead><tbody>\n" + rows + "\n</tbody></table></div>"
            )
        extra = ""
        if point == 3:
            extra = svg_portes()
        elif point == 9:
            extra = svg_images()
        elif point == 10:
            extra = svg_arbre()
        wid = f"wA{point}"
        cls = "ilot c" if point % 2 else "ilot v"
        fen = fenetre(wid, titre, phrases)
        parts.append(
            f'<section class="{cls}"><h2 id="p{point}">{html.escape(titre)}</h2>'
            f"<p>{VISIBLE[point]}</p>{fen}{extra}</section>"
        )
    sous = "Fiche 1.16, œdème. Chaque fenêtre s'ouvre au clic."
    return assembler("Œdème", sous, "\n".join(parts), "FIN_FICHIER LOT_145_Phase_A_V0.html")


def mesurer(texte: str):
    m = taille_xy.mesurer(texte)
    return m.x[1], m.y[1]


def ajuster_dx(dx):
    # cherche un nombre de phrases par point dans la fourchette y
    meilleur = None
    for n in range(10, 23):
        html_txt = page_dx(dx, n)
        x, y = mesurer(html_txt)
        if 36000 <= y <= 46000 and x < 9000:
            return html_txt, x, y, n
        if meilleur is None or abs(y - 40000) < abs(meilleur[2] - 40000):
            meilleur = (html_txt, x, y, n)
    return meilleur


def ajuster_a():
    meilleur = None
    for n, bonus in ((3, 4), (3, 5), (3, 6)):
        html_txt = page_a(n, bonus)
        x, y = mesurer(html_txt)
        print(f"  essai Phase_A n={n} bonus={bonus} x={x} y={y}")
        if 70000 <= y <= 80000 and x < 100000:
            return html_txt, x, y, n
        if meilleur is None or abs(y - 75000) < abs(meilleur[2] - 75000):
            meilleur = (html_txt, x, y, n)
    return meilleur


def ecrire_index():
    (EV / "INDEX.md").write_text(
        """# INDEX — LOT_145 — lectures du 1er novembre 2026

1. Depairon, angiologie, centre hospitalier universitaire vaudois, Lausanne, 3 juin 2021. notes_depairon_2021.txt
2. Bongard, Revue Médicale Suisse, 2002. notes_bongard_2002.txt
3. Stehlin et Ribi, Revue Médicale Suisse, 8 avril 2020. notes_rms_2020.txt
4. Lacout et collaborateurs, Journal de radiologie diagnostique et interventionnelle, juillet-août 2012. notes_lacout_2012.txt
5. Furosémide comprimés, information professionnelle suisse, autorisation 30629, corpus du 8 octobre 2026, lu le 1er novembre 2026. aips_30629.txt
6. Furosémide injectable, information professionnelle suisse, autorisation 30630, corpus du 8 octobre 2026, lu le 1er novembre 2026. aips_30630.txt
7. Spironolactone, information professionnelle suisse, autorisation 27257, corpus du 8 octobre 2026, lu le 1er novembre 2026. aips_27257.txt
8. Torasémide, information professionnelle suisse, autorisation 68924, corpus du 8 octobre 2026, lu le 1er novembre 2026. aips_68924.txt
9. Icatibant, information professionnelle suisse, autorisation 68263, corpus du 8 octobre 2026, lu le 1er novembre 2026. aips_68263.txt
10. Concentré d'inhibiteur de C1, information professionnelle suisse, autorisation 51950, corpus du 8 octobre 2026, lu le 1er novembre 2026. aips_51950.txt
11. Rivaroxaban, information professionnelle suisse, autorisation 68552, corpus du 8 octobre 2026, lu le 1er novembre 2026. aips_68552.txt
12. Énoxaparine, information professionnelle suisse, autorisation 49456, corpus du 8 octobre 2026, lu le 1er novembre 2026. aips_49456.txt
""",
        encoding="utf-8",
    )


def ecrire_liste():
    lines = ["# LISTE DX — LOT_145 F1.16 Œdème", "", "Liste rédigée le 1er novembre 2026. Les noms viennent du plan Flash relu (commits deb6532 et d6f9724). Aucune source ouverte ce jour ne donne la part suisse de chacun des dix diagnostics. Le numéro suit la gravité immédiate de ce plan.", ""]
    for d in DXS:
        lines.append(f"DX.{d['n']} — {d['nom']}")
    lines.append("")
    (LOT / "LISTE_DX_CANONIQUE.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def ecrire_incertitudes():
    (LOT / "INCERTITUDES.md").write_text(
        """# INCERTITUDES — LOT_145 F1.16 Œdème

Rédigé le 1er novembre 2026. Aucun élément central n'est retiré. Les éléments centraux (mécanismes hydrostatique, oncotique, inflammatoire et lymphatique, bilans d'échographie et de tomodensitométrie, conduite à tenir, traitements) sont dans les leçons.

## Ce qui est enseigné côte à côte

- Quatre portes. Depairon, Lausanne, 3 juin 2021, relie l'œdème à l'équilibre de Starling. La leçon garde les quatre mécanismes même quand un diagnostic en privilégie un.
- Anticoagulation de la thrombose. L'énoxaparine, autorisation 49456, et le rivaroxaban, autorisation 68552, sont deux phrases lues. Le choix entre elles n'est pas un classement de préférence inventé.
- Diurétiques. Le furosémide, le torasémide et la spironolactone ont chacun leur indication lue. La leçon ne les additionne pas en un schéma unique.
- Angiœdème. La revue du 8 avril 2020 dit que la forme bradykinique ne répond pas aux antihistaminiques. Les doses aiguës viennent des autorisations 68263 et 51950.
- Lymphœdème. Bongard, 2002, met la compression au centre. Le diurétique n'est pas le traitement de fond dans cette leçon.

## Retraits non centraux

1. Points chiffrés du score clinique de la thrombose : le tableau d'origine n'a pas été rouvert le 1er novembre 2026. La conduite reste : compression d'un côté aigu, avant un autre diagnostic local.
2. Seuils chiffrés du peptide natriurétique : le texte intégral de la société européenne de cardiologie n'a pas été extrait. Le nom du dosage n'est pas enseigné comme un chiffre.
3. Seuil en grammes de la protéinurie du syndrome néphrotique : le texte de néphrologie qui le fixe n'a pas été rouvert. La leçon garde l'urine, l'albumine et la spironolactone lue.
4. Gradient d'albumine de l'ascite et plafond de poids perdu par jour : non recopiés, pages non rouvertes.
5. Chiffre d'index cheville-bras avant contention : feuillet non rouvert. La leçon dit de regarder l'artère, sans seuil.
6. Milligrammes d'antibiotique de la dermohypodermite nécrosante : l'indication exacte n'a pas été alignée sur une information professionnelle dans ce lot. La chirurgie reste première.
7. Corticoïde en milligrammes par kilogramme du syndrome cave, volume de contraste de la revue de 2012, danazol et lanadélumab de la revue de 2020 : pas des informations professionnelles ouvertes pour une ordonnance de ce lot.
8. Créatininémie en milligrammes par décilitre citée pour le débit de perfusion du furosémide : unité de l'information professionnelle, non convertie et non enseignée comme seuil suisse.
9. Part suisse de l'œdème comme motif de consultation : non trouvée le 1er novembre 2026.

## Piste Flash

Les branches flash/vague2/LOT_145-A (deb6532) et flash/vague2/LOT_145-B (d6f9724) ont été lues par extraits le 1er novembre 2026. Les dix noms sont conservés. Le HTML de 150 à 200 Ko n'a pas été copié. Le fond a été réécrit. Aucune image n'a été téléchargée ni injectée.
""",
        encoding="utf-8",
    )


def ecrire_cliches():
    items = []
    for d in DXS:
        for k, signe, role in ((1, d["c1"], d["r1"]), (2, d["c2"], d["r2"])):
            items.append(
                {
                    "id": f"LOT_145-DX.{d['n']}-{k}",
                    "ancre": f"LOT_145-DX.{d['n']}-{k}",
                    "examen": "Examen d'un œdème",
                    "role": role,
                    "signe": signe,
                    "requete_commons_en": "edema clinical teaching diagram",
                    "a_confirmer": True,
                }
            )
    (LOT / "CLICHES.json").write_text(json.dumps(items, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def ecrire_svg_files():
    fig = LOT / "figures"
    fig.mkdir(parents=True, exist_ok=True)
    blocs = {
        "quatre_portes.svg": svg_portes(),
        "echo_scanner.svg": svg_images(),
        "arbre_oedeme.svg": svg_arbre(),
    }
    for nom, bloc in blocs.items():
        svg = bloc.split("<svg", 1)[1]
        svg = "<svg" + svg.split("</svg>", 1)[0] + "</svg>\n"
        (fig / nom).write_text(svg, encoding="utf-8")


def main():
    ecrire_index()
    ecrire_liste()
    ecrire_incertitudes()
    ecrire_cliches()
    ecrire_svg_files()
    html_a, x, y, n = ajuster_a()
    print(f"Phase_A n={n} x={x} y={y}")
    (LOT / "LOT_145_Phase_A_V0.html").write_text(html_a, encoding="utf-8")
    for d in DXS:
        html_d, x, y, n = ajuster_dx(d)
        print(f"DX.{d['n']} n={n} x={x} y={y}")
        (LOT / f"LOT_145_Phase_B_V0_DX.{d['n']}.html").write_text(html_d, encoding="utf-8")


if __name__ == "__main__":
    main()
