# -*- coding: utf-8 -*-
"""Rédaction LOT_171. Les phrases cliniques sont écrites ici, le moteur ne fait que le HTML."""
import re
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).parent))
from moteur import fen, section, page, SIGLES, svg_electrophorese, svg_hypo, svg_clone, stand, e

MOT = re.compile(r"seuil|score|incidence|prévalence|prevalence|sensibilit|spécificit", re.I)
AN = re.compile(r"\b(?:19|20)\d{2}\b")

def ok(p, year="2018"):
    if isinstance(p, tuple):
        return p
    if MOT.search(p) and re.search(r"\d", p) and not AN.search(p):
        return p.rstrip(".") + f". Source {year}."
    return p

def developpe(s, k):
    """Autour d'une phrase clinique déjà écrite : lecture, piège, conduite. k = nombre de phrases ajoutées."""
    if isinstance(s, tuple) or k <= 0:
        return [s]
    m = re.search(r"\d+(?:[.,]\d+)?", s)
    n = m.group(0) if m else None
    aj = []
    if n:
        aj.append(f"Le repère à ne pas déplacer dans cette phrase est {n}. Un arrondi ou un changement d'unité change la classe ou le diagnostic.")
        aj.append(f"Si le dossier porte un autre chiffre que {n}, on reprend le critère au lieu de forcer l'étiquette.")
        aj.append(f"À l'examen, la réponse cite {n} avec la condition de la phrase, pas le nom de la maladie seul.")
        aj.append("On compare ensuite au diagnostic voisin du même motif, rein, foie, tube ou clone, avant de fermer.")
    else:
        aj.append("Cette condition est qualitative. On n'y ajoute pas un chiffre qui n'a pas été lu dans une source.")
        aj.append("Le piège est de la transformer en seuil chiffré de mémoire.")
        aj.append("La conduite est de vérifier la condition telle qu'elle est écrite, puis le diagnostic voisin.")
        aj.append("On ne conclut pas sur un seul mot sorti de la phrase.")
    return [s] + aj[:k]

def W(fid, lib, titre, lines, year="2018", k=2, mince=1):
    out = []
    i = 0
    for x in lines:
        if not x:
            continue
        if isinstance(x, tuple):
            out.append(x)
            continue
        x = ok(x, year)
        kk = k if (i % mince == 0) else max(0, k - 1)
        i += 1
        out.extend(developpe(x, kk))
    return fen(fid, lib, titre, out)

def sec(n, cls, titre, accroches, windows):
    return section(f"p{n}", cls, titre, accroches, windows)

# --- figures ---
FIG_E = ("h", svg_electrophorese())
FIG_H = ("h", svg_hypo())
FIG_C = ("h", svg_clone())

def commun_sigles(fid):
    return fen(fid, "sigles", "Sigles", [("h", SIGLES)])

def panel(prot, alb, ctx, lecture, piege, geste, year):
    trou = prot - alb
    return [
        f"Protéines totales {prot} g/l, albumine {alb} g/l. Le trou, protéines moins albumine, vaut {trou} g/l.",
        ctx,
        f"Lecture : {lecture}",
        f"Le piège est {piege}",
        f"Conduite : {geste} Source {year}.",
    ]

# Panels partagés : chaque ligne est un cas réel de lecture, pas une variation vide.
PAN_A = [
    (70, 44, "CRP 3 mg/l. Le sujet est à jeun, allongé depuis une heure.", "Les deux valeurs sont compatibles avec les intervalles usuels. Le catalogue ACB donne 60 à 80 g/l pour les protéines totales de l'adulte.", "Conclure sans lire l'intervalle imprimé par le laboratoire.", "Garder le compte rendu du laboratoire qui a dosé.", "2026"),
    (58, 40, "Le malade a bu beaucoup d'eau. La CRP est basse.", "L'hydratation baisse les protéines totales. L'albumine suit souvent.", "Appeler cela une fuite rénale.", "Recontrôler après correction de l'eau, sans électrophorèse d'emblée.", "2026"),
    (82, 46, "Prélèvement juste après une longue station debout.", "La station debout peut monter les protéines jusqu'à environ 10 pour cent selon le catalogue ACB.", "Comparer ce prélèvement à un prélèvement du matin au lit sans le dire.", "Noter la position si la valeur est limite.", "2026"),
    (76, 28, "CRP 140 mg/l, fièvre, pneumonie.", "Hypoalbuminémie d'inflammation. Le trou reste modéré.", "Chercher un myélome sur la seule albumine basse.", "Traiter l'infection. L'électrophorèse attend si aucun signe de clone.", "2026"),
    (64, 18, "CRP 4 mg/l, apport très bas depuis des semaines, perte de poids.", "Hypoalbuminémie avec CRP calme : la dénutrition entre dans la lecture, avec l'inflammation absente.", "Donner de l'albumine pour faire monter le chiffre.", "Reprendre l'alimentation. Le LOT des carences nutritionnelles détaille les scores nutritionnels.", "2026"),
    (55, 16, "Protéinurie 8 grammes par jour, œdèmes des jambes, cholestérol haut.", "Syndrome néphrotique. L'albumine est basse et le trou n'est pas un pic.", "Rassurer parce que la créatinine est encore normale.", "Prouver la protéinurie, chercher la cause glomérulaire, évaluer le risque thrombotique. KDIGO 2021.", "2021"),
    (62, 24, "Ascite, angiomes stellaires, bilirubine 60 µmol/l, INR 1,9.", "Insuffisance hépatocellulaire. L'albumine entre dans le score de Child-Pugh, 1973.", "Attribuer l'ascite à une dénutrition seule.", "Ponction diagnostique, gradient d'albumine, polynucléaires. EASL 2018.", "2018"),
    (50, 22, "Diarrhée chronique, œdèmes, pas de protéinurie, foie sans ascite.", "Perte possible par le tube digestif. La clairance fécale de l'alpha-1-antitrypsine explore l'entéropathie exsudative.", "Conclure à un néphrotique sans bandelette.", "Quantifier la protéinurie, qui doit être faible, puis la perte digestive.", "2018"),
    (88, 38, "CRP 6 mg/l. Un pic étroit est décrit sur l'électrophorèse, 8 g/l, IgG kappa.", "Pic monoclonal petit. Cela peut être un MGUS si la moelle est basse et s'il n'y a pas de CRAB. Blood 2005 et IMWG 2014.", "Appeler cela un myélome à cause du mot pic.", "Immunofixation, chaînes légères, puis le bilan du clone selon les critères.", "2014"),
    (96, 32, "Pic de 36 g/l, hémoglobine 92 g/l, calcémie 2,9 mmol/l.", "Myélome jusqu'à preuve du contraire : masse monoclonale et atteinte d'organe. Critères IMWG 2014.", "Attendre six mois comme pour un MGUS.", "Bilan complet et avis d'hématologie sans délai.", "2014"),
    (102, 34, "IgM 28 g/l, fond d'œil avec veines dilatées, épistaxis, céphalée.", "Hyperviscosité possible de la maladie de Waldenström. Urgence de soustraction plasmatique.", "Transfuser des globules rouges avant d'avoir baissé la viscosité.", "Plasmaphérèse d'abord si le tableau est bruyant, puis traitement du clone.", "2015"),
    (70, 30, "Protéinurie faite surtout d'albumine, chaînes légères anormales, cœur épais, langue grosse.", "Amylose AL jusqu'à preuve du contraire. Le pic peut être petit.", "Se rassurer parce que l'électrophorèse est presque normale.", "Rouge Congo et typage. Le traitement vise le clone, pas le chiffre d'albumine.", "2015"),
    (110, 40, "Natrémie 128 mmol/l au laboratoire, 138 mmol/l au gaz du sang. Pas d'œdème.", "Pseudo-hyponatrémie : l'électrode indirecte dilue l'échantillon, l'électrode directe du gaz du sang non.", "Restreindre l'eau comme dans une hyponatrémie vraie.", "Croire le gaz du sang et chercher l'hyperprotéinémie ou les lipides.", "2018"),
    (68, 20, "Calcémie mesurée 2,05 mmol/l.", "La calcémie corrigée selon Payne 1973 remonte quand l'albumine est basse : mesurée plus 0,02 fois (40 moins l'albumine).", "Traiter une hypocalcémie qui n'existe que sur le chiffre brut.", "Calculer, et demander le calcium ionisé si le malade est en réanimation ou si le rein est très atteint.", "1973"),
    (72, 18, "Sodium 140, chlore 110, bicarbonate 14, tous en mmol/l. Pas de lactate au premier regard.", "Le trou anionique brut est bas parce que l'albumine, anion, manque. Figge 1998 ajoute 0,25 mmol/l par gramme d'albumine sous la normale.", "Conclure à l'absence d'acidose à trou anionique.", "Corriger le trou avant d'écarter une acidose.", "1998"),
    (74, 30, "Ponction d'ascite de 7 litres chez un cirrhotique.", "L'EASL 2018 perfuse 8 g/l d'ascite retiré au-delà de 5 litres. L'AASLD 2021 dit 6 à 8 grammes par litre.", "Oublier l'albumine parce que la tension tient encore.", "Albumine en fin de ponction, surveillance de la surcharge.", "2018"),
    (66, 26, "Ascite trouble, 800 polynucléaires par mm3, créatinine 110 µmol/l, bilirubine 80 µmol/l.", "Péritonite bactérienne spontanée. L'EASL 2018 recommande l'albumine, 1,5 gramme par kilogramme le jour du diagnostic et 1 gramme par kilogramme au jour 3.", "Donner seulement l'antibiotique.", "Antibiotique tout de suite et albumine, surtout si la bilirubine ou la créatinine est haute.", "2018"),
    (60, 22, "Créatinine qui double en 48 heures, ascite tendue, pas de choc, pas de néphrotoxique.", "Syndrome hépatorénal possible après avoir rempli. L'EASL 2018 : 1 gramme d'albumine par kilogramme, au plus 100 grammes, pendant deux jours, puis 20 à 40 grammes par jour avec le vasoconstricteur.", "Appeler hépatorénal un malade encore sous anti-inflammatoire.", "Retirer les causes, puis albumine et terlipressine selon l'information du vasoconstricteur.", "2018"),
    (90, 42, "Rapport kappa sur lambda 0,4. Pas de pic. CRP normale.", "Rapport dans l'intervalle 0,26 à 1,65 du travail de 2005. Cela n'écarte pas tout, mais ce n'est pas un rapport pathologique.", "Répéter la moelle tout de suite.", "Pas de clone évident. Rechercher seulement si la clinique l'exige.", "2005"),
    (84, 36, "Rapport kappa sur lambda 8. Chaîne kappa haute. Pas de chaîne lourde à l'immunofixation.", "MGUS à chaînes légères possible. La revue lue cite une prévalence de 0,8 pour cent dans la cohorte du Minnesota.", "Dire que l'électrophorèse normale ferme le dossier.", "Le rapport anormal avec chaîne impliquée haute et sans chaîne lourde définit cette forme.", "2006"),
]

PAN_NEPH = [
    (52, 18, "Œdèmes jusqu'aux genoux, protéinurie 6,2 grammes par jour, cholestérol 8 mmol/l.", "Les quatre classiques sont là : protéinurie au-dessus de 3,5 grammes par jour, albumine basse, œdèmes, lipides hauts.", "Attendre une semaine sans prévenir le risque de thrombose.", "Bilan de cause et décision d'anticoagulation selon KDIGO 2021.", "2021"),
    (60, 22, "Méthode au pourpre de bromocrésol. Albumine 22 g/l. Glomérulopathie extra-membraneuse.", "Le seuil de discussion d'une anticoagulation prophylactique est 20 g/l avec le pourpre ou l'immunodosage, et 25 g/l avec le vert de bromocrésol.", "Utiliser 25 g/l alors que le laboratoire dose au pourpre.", "Lire la méthode sur le compte rendu avant de choisir le seuil.", "2021"),
    (58, 27, "Méthode au vert de bromocrésol. Albumine 27 g/l. Même maladie membraneuse.", "27 g/l au vert est au-dessus de 25 g/l. On estime le risque, on n'anticoagule pas sur le seul chiffre.", "Démarrer une warfarine sans score de saignement.", "Le KDIGO 2021 demande de comparer le risque thrombotique au risque hémorragique.", "2021"),
    (64, 34, "Protéinurie 4 grammes par jour, albumine 34 g/l, pas d'œdème.", "Protéinurie de rang néphrotique sans syndrome complet. L'hypoalbuminémie manque.", "Traiter comme un syndrome néphrotique constitué.", "Chercher la cause, mais ne pas coller l'étiquette de syndrome si l'albumine tient.", "2021"),
    (55, 19, "Enfant de 4 ans, œdèmes, protéinurie, pas d'hématurie.", "Chez l'enfant le KDIGO 2021 ne demande pas la biopsie d'emblée si le tableau est typique.", "Copier la dose adulte de diurétique.", "Le schéma pédiatrique de glucocorticoïde est celui du chapitre 4 du KDIGO 2021 : soixante milligrammes par mètre carré ou deux milligrammes par kilogramme, sans dépasser soixante milligrammes par jour.", "2021"),
    (48, 16, "Adulte, prise de poids de 8 kg, bandelette à trois croix.", "Le diurétique de l'anse est le premier médicament de l'œdème. L'information 30629 dit de garder la plus petite dose utile. Le comprimé fait 40 mg.", "Montée brutale jusqu'au plafond chez un rein normal.", "Deux prises par jour souvent, dose titrée, kaliémie surveillée si l'on ajoute la spironolactone.", "2026"),
    (70, 21, "Hématurie, cylindres, créatinine 180 µmol/l, complément bas.", "Glomérulonéphrite plutôt que néphropathie à lésions glomérulaires minimes.", "Donner des corticoïdes sans avis néphrologique.", "Biopsie selon le contexte et le KDIGO 2021.", "2021"),
    (66, 25, "Diabète ancien, rétinopathie, protéinurie sans hématurie.", "Néphropathie diabétique possible. Le syndrome néphrotique n'est pas toujours une maladie à lésions minimes.", "Oublier les autres causes chez le diabétique.", "Vérifier le fond d'œil et les signes d'appel d'une autre glomérulopathie.", "2021"),
    (50, 17, "Anticorps anti-PLA2R positifs, protéinurie néphrotique.", "Glomérulopathie extra-membraneuse primaire probable. Le KDIGO 2021 suit cet anticorps.", "Répéter la biopsie si l'anticorps et la clinique concordent et qu'aucune cause secondaire n'est là.", "Discuter le traitement immunosuppresseur selon les facteurs de risque du KDIGO 2021, pas selon l'albumine seule.", "2021"),
    (61, 29, "Albumine 29 g/l au vert de bromocrésol, pas de thrombose, maladie membraneuse.", "Zone où l'on discute, entre le seuil bas et 32 g/l cités sur la figure du KDIGO 2021.", "Une aspirine suffit à prévenir la thrombose veineuse.", "Le KDIGO 2021 écrit que l'aspirine ne prévient pas la thrombose veineuse.", "2021"),
]

PAN_FOIE = [
    (58, 38, "Pas d'ascite, pas d'encéphalopathie, bilirubine 18 µmol/l, INR 1,1.", "Albumine au-dessus de 35 g/l : 1 point. Les quatre autres items sont à 1. Score 5, classe A. Pugh 1973.", "Annoncer une classe C parce qu'il y a une cirrhose.", "Classe A : 5 ou 6 points.", "1973"),
    (55, 31, "Ascite modérée contrôlée par le traitement, pas d'encéphalopathie, bilirubine 40 µmol/l, INR 1,8.", "Albumine entre 28 et 35 g/l : 2 points. Ascite : 2. Bilirubine non cholestatique : 2. INR : 2. Encéphalopathie : 1. Total 9, classe B.", "Oublier un item et annoncer la classe A.", "Additionner les cinq items. Classe B : 7 à 9.", "1973"),
    (48, 24, "Ascite importante, encéphalopathie grade III, bilirubine 90 µmol/l, INR 2,6.", "Albumine sous 28 g/l : 3. Ascite : 3. Encéphalopathie : 3. Bilirubine : 3. INR au-dessus de 2,3 : 3. Total 15, classe C.", "Proposer un TIPS sans discussion.", "Classe C : 10 à 15. Le TIPS est dangereux dans cette classe selon les essais cités par l'EASL 2018.", "2018"),
    (60, 33, "Cirrhose biliaire, bilirubine 90 µmol/l, soit un peu au-dessus de 4 mg/dl, albumine 36 g/l, pas d'ascite, INR 1,2, pas d'encéphalopathie.", "Sur l'échelle biliaire de 1973, la bilirubine entre 4 et 10 mg/dl vaut 2 points, pas 3. Les autres items valent 1. Total 6, classe A.", "Utiliser le seuil de 50 µmol/l de l'échelle non cholestatique et annoncer 3 points de bilirubine.", "L'échelle biliaire va jusqu'à 10 mg/dl pour le score 2.", "1973"),
    (52, 26, "Sept litres retirés, fin de ponction.", "8 g/l d'ascite retiré selon l'EASL 2018, soit la recommandation européenne quand on dépasse 5 litres. L'AASLD 2021 écrit 6 à 8 grammes par litre.", "Donner un cristalloïde seul après une grande ponction.", "Albumine à 20 pour cent, vitesse habituelle au plus 1 à 2 ml/min selon l'information 65562 pour la forme concentrée.", "2018"),
    (57, 29, "Deux litres seulement, malade stable.", "Sous 5 litres le risque de dysfonction circulatoire est plus faible. L'EASL 2018 dit quand même que l'on donne souvent de l'albumine, grade plus faible.", "Recopier la dose de la grande ponction sans réfléchir.", "Juger le volume et l'état circulatoire.", "2018"),
    (49, 21, "Fièvre, ascite, 400 polynucléaires, créatinine 70 µmol/l, bilirubine 40 µmol/l.", "Péritonite bactérienne spontanée, seuil au-dessus de 250 polynucléaires. L'albumine est quand même recommandée par l'EASL 2018.", "Réserver l'albumine aux seuls malades dont la bilirubine dépasse 68 µmol/l.", "La recommandation I;1 vise les malades avec cette infection. Le bénéfice a été le plus net au-dessus de 68 µmol/l de bilirubine ou de 88 µmol/l de créatinine.", "2018"),
    (63, 27, "Créatinine de 80 à 190 µmol/l en deux jours, albumine déjà reçue deux jours à 1 gramme par kilogramme sans dépasser 100 grammes.", "Étape du syndrome hépatorénal après remplissage. Ensuite 20 à 40 grammes par jour d'albumine à 20 pour cent, avec le vasoconstricteur, EASL 2018.", "Continuer l'albumine si la pression veineuse monte et que le malade est dyspnéique.", "Arrêter la perfusion au premier signe de surcharge. L'information suisse le dit aussi.", "2018"),
    (70, 41, "Gradient sérum-ascite 14 g/l, protéines d'ascite 8 g/l.", "Gradient au-dessus de 11 g/l : l'hypertension portale participe. EASL 2018, exactitude citée d'environ 97 pour cent.", "Conclure à une ascite cardiaque sans regarder le cœur si le gradient est haut : le cœur peut aussi donner un gradient haut.", "Le gradient haut n'est pas spécifique de la cirrhose. L'examen du cœur reste nécessaire si le doute existe.", "2018"),
    (54, 25, "Rapport Na/K urinaire 0,6 sous cirrhose avec ascite.", "L'information 27257 : si le rapport est inférieur à 1, 200 à 400 mg/jour de spironolactone. S'il est supérieur à 1, 100 mg/jour.", "Donner 400 mg d'emblée quand le rapport est à 2.", "Suivre le rapport, puis la plus petite dose d'entretien. Surveillance du potassium.", "2026"),
]

def lots_de_panels(prefix, rows):
    lines = []
    for row in rows:
        lines.extend(panel(*row))
    return lines

# Textes de fond, critères entiers.
FOND_A = [
    "Les protéines totales de l'adulte se situent, dans le catalogue de l'Association for Clinical Biochemistry lu le 31 octobre 2026, entre 60 et 80 g/l.",
    "Le nouveau-né est plus bas. La valeur adulte est atteinte vers trois ans selon le même catalogue.",
    "L'hydratation baisse le chiffre. La station debout peut l'augmenter d'environ 10 pour cent.",
    "La méthode courante est le biuret. Elle voit les liaisons peptidiques, pas une protéine unique.",
    "L'albumine est la protéine la plus abondante. L'intervalle dépend de la méthode.",
    "Le laboratoire sud-africain de la publication de 2025 utilisait 35 à 52 g/l pour l'albumine et 60 à 78 g/l pour les protéines totales.",
    "Le répertoire ARUP, lu le 31 octobre 2026, donne l'albumine de 3,75 à 5,01 g/dl, soit 37,5 à 50,1 g/l.",
    "On décide avec l'intervalle imprimé à côté du résultat, pas avec une table apprise seule.",
    "Le trou protéique est protéines totales moins albumine. C'est la fraction globuline.",
    "Un trou à 40 g/l a été testé comme dépistage de protéine monoclonale : sensibilité 47,7 pour cent dans l'étude canadienne citée en 2025.",
    "À 46 g/l, la même publication de 2025 trouve une sensibilité de 35 pour cent et une spécificité de 91 pour cent.",
    "Le trou n'établit donc pas le diagnostic. Il ne l'écarte pas non plus.",
    "Une protéine totale haute chez un sujet bien hydraté fait chercher les immunoglobulines, catalogue ACB.",
    "L'électrophorèse sépare albumine, alpha-1, alpha-2, bêta et gamma.",
    "Fractions ARUP lues en 2026, converties : alpha-1 1,9 à 4,6 g/l, alpha-2 4,8 à 10,5 g/l, bêta 4,8 à 11 g/l, gamma 6,2 à 15,1 g/l.",
    "Le profil inflammatoire baisse l'albumine et monte alpha-1 et alpha-2.",
    "Le profil de cirrhose baisse l'albumine et fusionne bêta et gamma, le bloc bêta-gamma, sans pic étroit. L'IgA en est la raison classique.",
    "Le profil néphrotique baisse fort l'albumine et monte l'alpha-2, parce que l'alpha-2-macroglobuline est retenue.",
    "Le pic monoclonal est une bande étroite, souvent dans le gamma, parfois dans le bêta.",
    "L'hypogammaglobulinémie est un gamma bas. Le catalogue ACB appelle parésie immunitaire la baisse des immunoglobulines normales derrière un pic malin.",
    "L'immunofixation nomme la chaîne lourde et la chaîne légère. Elle voit des pics trop petits pour l'électrophorèse.",
    "Le répertoire Mayo lu en 2026 le dit pour l'amylose, le myélome traité, le MGUS et le plasmocytome.",
    "Le rapport kappa sur lambda de l'essai Freelite, dans le travail de Blood 2005, est pathologique en dessous de 0,26 ou au-dessus de 1,65.",
    "Ce rapport est un facteur de risque indépendant de progression du MGUS. Hazard ratio 3,5 dans ce travail, encore 2,6 après ajustement.",
    "Les trois facteurs Mayo 2005 sont le rapport anormal, le type non IgG, et le pic haut.",
    "Le résumé de 2005 écrit un pic supérieur à 15 g/l. Le tableau repris ensuite écrit au moins 1,5 g/dl, ce qui est le même ordre de grandeur.",
    "Risque absolu de progression à 20 ans : 5 pour cent sans facteur, 21 pour cent avec un, 37 pour cent avec deux, 58 pour cent avec trois. Blood 2005.",
    "Risques relatifs du même tableau : 1, 5,4, 10,1 et 20,8.",
    "Avec la mort comme risque concurrent, les chiffres à 20 ans sont 2, 10, 18 et 27 pour cent.",
    "Le MGUS, revue lue, est un pic sérique inférieur à 3 g/dl, une moelle clonale inférieure à 10 pour cent, et l'absence d'atteinte d'organe.",
    "Prévalence d'Olmsted County, New England Journal of Medicine 2006 : 3,2 pour cent à partir de 50 ans, 5,3 pour cent à partir de 70 ans, 8,9 pour cent chez les hommes de plus de 85 ans.",
    "Hommes 4,0 pour cent, femmes 2,7 pour cent, ajustés sur la population de 2000.",
    "Le risque de progression est d'environ 1 pour cent par an, et il ne s'éteint pas après 25 ans.",
    "Le dépistage sérique, électrophorèse, immunofixation et chaînes légères, a vu 426 malades sur 428 dans la série citée par la revue.",
    "L'urine n'est pas exigée pour le dépistage. Elle le devient si un pic sérique est trouvé.",
    "Le MGUS à chaînes légères : rapport anormal, pas de chaîne lourde, chaîne impliquée augmentée. Prévalence 0,8 pour cent dans la cohorte citée.",
    "Le myélome, critères IMWG repris en 2015, exige un clone : au moins 10 pour cent de plasmocytes clonaux, ou un plasmocytome prouvé par biopsie.",
    "Il faut en plus un événement définissant le myélome : CRAB ou biomarqueur.",
    "C, calcium : calcémie supérieure de plus de 0,25 mmol/l à la limite haute, ou supérieure à 2,75 mmol/l.",
    "R, rein : clairance inférieure à 40 ml par minute, ou créatinine supérieure à 177 µmol/l.",
    "A, anémie : hémoglobine inférieure à 100 g/l, ou de plus de 20 g/l sous la limite basse.",
    "B, os : au moins une lésion ostéolytique sur la radiographie, la TDM ou la TEP.",
    "Si la moelle est sous 10 pour cent, il faut plus d'une lésion pour ne pas confondre avec un plasmocytome solitaire.",
    "Biomarqueur S : au moins 60 pour cent de plasmocytes clonaux.",
    "Biomarqueur Li : rapport chaîne impliquée sur chaîne non impliquée au moins 100, et chaîne impliquée au moins 100 mg/l.",
    "Biomarqueur M : plus d'une lésion focale à l'IRM, d'au moins 5 mm.",
    "Ces trois biomarqueurs ont été choisis parce que le risque d'atteinte d'organe à deux ans était très haut dans plus d'une étude.",
    "Le myélome indolent a un pic d'au moins 30 g/l ou 10 à 60 pour cent de plasmocytes, sans événement définissant et sans amylose.",
    "La maladie de Waldenström est un clone lymphoplasmocytaire qui sécrète une IgM, de n'importe quelle taille, avec infiltrat médullaire.",
    "La mutation MYD88 L265P soutient ce diagnostic. Elle n'est pas exigée à elle seule.",
    "L'amylose AL est un dépôt de chaîne légère. Le rouge Congo et la biréfringence verte en lumière polarisée montrent l'amylose. Le typage montre que c'est une chaîne légère, pas une amylose AA ni une amylose à transthyrétine.",
    "Le pic de l'amylose AL est souvent petit. L'électrophorèse normale n'écarte pas le diagnostic.",
    "Le syndrome néphrotique n'est pas la seule protéinurie de rang néphrotique. Le KDIGO 2021 rappelle que l'hypoalbuminémie peut manquer.",
    "Le rang néphrotique est une protéinurie au-dessus de 3,5 grammes par jour.",
    "L'œdème et l'hyperlipidémie font partie du tableau classique. La figure 4 du KDIGO 2021 marque l'hypoalbuminémie comme essentielle et d'autres éléments comme variables.",
    "Le vert de bromocrésol lit l'albumine environ 5,5 g/l trop haut par rapport au pourpre, à l'électrophorèse capillaire ou à l'immunodosage. KDIGO 2021.",
    "Anticoagulation du syndrome néphrotique : traitement complet s'il y a déjà une thrombose.",
    "Prévention seulement si le risque de thrombose dépasse le risque de saignement grave du malade.",
    "Pour la glomérulopathie membraneuse, le KDIGO 2021 discute 25 g/l si le dosage est au vert de bromocrésol, et 20 g/l si le dosage est au pourpre ou immunologique.",
    "Cet algorithme a été écrit pour la maladie membraneuse. Le KDIGO 2021 dit que sa valeur est inconnue dans les autres causes.",
    "L'aspirine ne suffit pas à prévenir la thrombose veineuse. Le KDIGO 2021 l'écrit.",
    "L'entéropathie exsudative perd des protéines par le tube. L'alpha-1-antitrypsine n'est pas digérée. Sa clairance fécale monte quand la perte est digestive.",
    "On la demande quand l'albumine est basse, la protéinurie absente et le foie insuffisant pour expliquer le chiffre.",
    "Le score de Child-Pugh, 1973, a cinq items de 1 à 3 points.",
    "Albumine supérieure à 35 g/l : 1 point. De 28 à 35 g/l : 2 points. Inférieure à 28 g/l : 3 points.",
    "Bilirubine non cholestatique : sous 2 mg/dl, environ 35 µmol/l, 1 point. De 2 à 3 mg/dl, 2 points. Au-dessus de 3 mg/dl, 3 points.",
    "Bilirubine de la cirrhose biliaire : sous 4 mg/dl, 1 point. De 4 à 10 mg/dl, 2 points. Au-dessus de 10 mg/dl, 3 points.",
    "INR : sous 1,7, 1 point. De 1,7 à 2,3, 2 points. Au-dessus de 2,3, 3 points. Le papier de 1973 utilisait le temps de prothrombine. L'INR est l'adaptation ultérieure.",
    "Ascite absente, 1 point. Modérée ou contrôlée, 2 points. Importante, 3 points.",
    "Encéphalopathie absente, 1 point. Grade I ou II, 2 points. Grade III ou IV, 3 points.",
    "Classe A, 5 ou 6 points. Classe B, 7 à 9. Classe C, 10 à 15.",
    "L'albumine est une protéine négative de la phase aiguë. La CRP monte en heures. L'albumine baisse plus lentement.",
    "L'information suisse 65562 écrit une demi-vie d'environ 19 jours. Une chute en quelques heures est une fuite, pas un arrêt de synthèse.",
    "L'albumine seule ne prouve pas la dénutrition. L'inflammation la baisse chez un sujet qui mange.",
    "Le pool échangeable est de 4 à 5 g/kg de poids, dont 40 à 45 pour cent dans les vaisseaux. Information 65562, lue en 2026.",
    "Calcémie corrigée, Payne 1973, unités SI : calcium mesuré plus 0,02 fois (40 moins l'albumine en g/l).",
    "Certains utilisent 44 g/l comme ancre. Le calculateur qui cite Payne le signale.",
    "Le calcium ionisé prime quand l'albumine est extrême, en réanimation, ou quand le chiffre corrigé et la clinique ne vont pas ensemble.",
    "Trou anionique corrigé, Figge 1998 : trou observé plus 0,25 fois (albumine normale moins albumine observée), albumines en g/l.",
    "Chaque gramme d'albumine manquant sous-estime le trou de 0,25 mmol/l. Dans cette étude, 49 pour cent des malades de réanimation avaient une albumine sous 20 g/l.",
    "La pseudo-hyponatrémie vient d'une électrode indirecte, qui dilue l'échantillon et suppose une fraction d'eau normale.",
    "Une protéine très haute ou des lipides très hauts baissent cette fraction d'eau. Le sodium du gaz du sang, électrode directe, n'est pas faussé.",
    "On ne restreint pas l'eau sur une pseudo-hyponatrémie.",
    "L'hyperviscosité se voit surtout avec l'IgM, qui est un pentamère. Saignement des muqueuses, trouble visuel, céphalée, confusion, parfois coma.",
    "Le geste d'urgence est la plasmaphérèse. On évite de transfuser des globules rouges avant, parce que le sang devient encore plus visqueux.",
    "L'information suisse de l'albumine n'impose pas les doses de l'EASL. Elle dit d'adapter la dose au malade et de surveiller l'hémodynamique.",
    "La forme à 20 pour cent ne devrait en général pas dépasser 1 à 2 ml/min. La forme à 5 pour cent, information du même titulaire, ne devrait pas dépasser 5 ml/min.",
    "On arrête dès la céphalée, la dyspnée, la turgescence jugulaire, la montée de pression ou l'œdème pulmonaire.",
    "Grossesse, information de l'albumine humaine : l'expérience clinique suggère qu'aucun effet nuisible n'est attendu. Ce n'est pas une étude contrôlée.",
    "Grande ponction au-dessus de 5 litres : 8 g/l d'ascite retiré, EASL 2018, recommandation I;1.",
    "L'AASLD 2021 écrit 6 à 8 grammes par litre, avis d'experts, faute d'étude de dose.",
    "Péritonite bactérienne spontanée : 1,5 gramme par kilogramme au diagnostic et 1 gramme par kilogramme au jour 3. EASL 2018.",
    "Dans l'essai cité, le syndrome hépatorénal de type 1 passait de 30 à 10 pour cent, et la mortalité de 29 à 10 pour cent.",
    "L'effet était net si la bilirubine était d'au moins 68 µmol/l ou la créatinine d'au moins 88 µmol/l.",
    "Syndrome hépatorénal : d'abord 1 gramme par kilogramme pendant deux jours, sans dépasser 100 grammes, si aucune cause évidente et si le stade dépasse 1A. EASL 2018.",
    "Puis albumine à 20 pour cent, 20 à 40 grammes par jour, avec le vasoconstricteur, jusqu'à la réponse ou 14 jours.",
    "La spironolactone de la cirrhose avec ascite, numéro 27257 : 100 mg/jour si le rapport Na/K urinaire dépasse 1, et 200 à 400 mg/jour s'il est inférieur à 1.",
    "Elle est contre-indiquée si la clairance est sous 30 ml/min, en anurie, dans la maladie d'Addison, en hyperkaliémie, en hyponatrémie, et avec l'éplérénone.",
    "On l'arrête si le potassium dépasse 5 mmol/l. Grossesse : ne pas l'administrer sauf nécessité absolue. Allaitement : non recommandé.",
    "Le furosémide, numéro 30629, se garde à la plus petite dose utile. Le comprimé fait 40 mg. On le suspend transitoirement quand on introduit un inhibiteur de l'enzyme de conversion.",
    "Les anti-inflammatoires non stéroïdiens sont évités dans l'ascite. L'EASL 2018 rappelle le risque d'insuffisance rénale.",
    "Perte de poids sous diurétique : pas plus de 0,5 kg par jour sans œdème périphérique, pas plus de 1 kg par jour avec œdème. EASL 2018.",
]

FOND_DX = {
1: [
    "Ce diagnostic est l'hypoalbuminémie dont le moteur est l'inflammation, la dénutrition, ou les deux.",
    "L'albumine est une protéine négative de la phase aiguë. L'interleukine 6 freine sa synthèse.",
    "La demi-vie d'environ 19 jours, information 65562, explique qu'une synthèse arrêtée ne vide pas le sang en une nuit.",
    "Une baisse en quelques heures vient de la fuite capillaire, des brûlures, du sepsis, ou d'une dilution.",
    "La CRP monte dès les premières heures. Elle aide à dire si l'inflammation est là.",
    "Une CRP haute et une albumine basse, sans pic et sans protéinurie, se lisent comme une inflammation.",
    "Une CRP calme, un apport effondré et une perte de poids font entrer la dénutrition.",
    "Les deux causes coexistent souvent à l'hôpital. On ne choisit pas l'une pour effacer l'autre.",
    "L'albumine n'est pas le marqueur de la renutrition des derniers jours. Elle bouge trop lentement.",
    "On ne perfuse pas de l'albumine pour corriger un chiffre inflammatoire sans indication circulatoire.",
    "Le calcium corrigé et le trou anionique corrigé évitent deux fausses lectures pendant cette hypoalbuminémie.",
    "Le voisin rénal se reconnaît à la protéinurie. Le voisin hépatique se reconnaît à l'ascite et aux signes de cirrhose.",
    "Le voisin digestif se reconnaît à la diarrhée et à l'absence de protéinurie.",
    "Le voisin monoclonal se reconnaît au pic ou au rapport de chaînes légères, pas à l'albumine seule.",
],
2: [
    "Le syndrome néphrotique associe une protéinurie abondante et une albumine basse, avec œdèmes et souvent des lipides hauts.",
    "Le KDIGO 2021 place le rang néphrotique au-dessus de 3,5 grammes par jour.",
    "La protéinurie de ce rang peut exister sans hypoalbuminémie. Ce n'est pas encore le syndrome.",
    "L'albumine du syndrome dépend de la méthode. Le vert de bromocrésol lit environ 5,5 g/l de plus que le pourpre.",
    "La perte urinaire d'albumine baisse la pression oncotique. L'eau sort dans l'interstitium.",
    "Le foie augmente les lipoprotéines. Le cholestérol monte.",
    "L'antithrombine et d'autres facteurs sortent dans l'urine. Le risque de thrombose monte, surtout dans la maladie membraneuse.",
    "Causes fréquentes de l'adulte : lésions glomérulaires minimes, hyalinose segmentaire et focale, glomérulopathie extra-membraneuse, diabète, amylose.",
    "L'anticorps anti-PLA2R oriente vers la forme primaire de la maladie membraneuse.",
    "La bandelette positive n'est pas une quantification. Il faut les grammes par jour ou un rapport sur créatinine dans de bonnes conditions.",
    "Le KDIGO 2021 préfère un recueil long quand on décide d'une immunosuppression.",
    "L'œdème se traite d'abord par un diurétique de l'anse, souvent en deux prises, à la plus petite dose utile, information 30629.",
    "La thrombose constituée reçoit un traitement anticoagulant complet.",
    "La prévention se discute si le risque dépasse le risque de saignement, avec les seuils 25 g/l au vert et 20 g/l au pourpre dans la maladie membraneuse.",
],
3: [
    "L'insuffisance hépatocellulaire baisse la synthèse d'albumine. La cirrhose en est la cause commune.",
    "L'albumine entre dans le score de Child-Pugh. Elle ne résume pas le score.",
    "Les cinq items et les deux échelles de bilirubine sont ceux de 1973, avec l'INR comme adaptation du temps de prothrombine.",
    "Classe A, 5 ou 6. Classe B, 7 à 9. Classe C, 10 à 15.",
    "L'ascite du cirrhotique se ponctionne au diagnostic et à chaque complication. EASL 2018.",
    "Le gradient d'albumine d'au moins 11 g/l parle pour l'hypertension portale, avec l'exactitude citée d'environ 97 pour cent.",
    "Au-dessus de 250 polynucléaires par mm3, c'est une péritonite bactérienne spontanée.",
    "Après une ponction de plus de 5 litres, l'EASL 2018 donne 8 g/l d'ascite retiré.",
    "L'AASLD 2021 donne 6 à 8 grammes par litre. Les deux recommandations sont datées. L'information suisse, elle, individualise.",
    "Pour la péritonite, 1,5 gramme par kilogramme puis 1 gramme par kilogramme au jour 3.",
    "Pour le syndrome hépatorénal, remplissage d'abord, 1 gramme par kilogramme deux jours sans dépasser 100 grammes, puis 20 à 40 grammes par jour avec le vasoconstricteur.",
    "La spironolactone, numéro 27257, suit le rapport Na/K urinaire : 100 mg/jour ou 200 à 400 mg/jour.",
    "On ne dépasse pas 0,5 kg de perte par jour sans œdème, ni 1 kg avec œdème.",
    "On arrête l'albumine au premier signe de surcharge.",
],
4: [
    "L'entéropathie exsudative perd des protéines plasmatiques vers la lumière digestive.",
    "L'albumine baisse. Les immunoglobulines et les lymphocytes peuvent baisser aussi.",
    "La protéinurie est absente ou mince. Le foie ne suffit pas à expliquer le chiffre.",
    "Causes : lymphangiectasies, maladie cœliaque, maladies inflammatoires du tube, maladie de Ménétrier, cœur droit et constriction qui bloquent le drainage lymphatique, lupus, certaines chimiothérapies.",
    "L'alpha-1-antitrypsine résiste à la digestion. Ce qui passe dans l'intestin se retrouve dans les selles.",
    "La clairance fécale rapporte la quantité fécale à la concentration sanguine et au volume des selles.",
    "Une clairance au-dessus de l'intervalle du laboratoire qui dose soutient la perte digestive.",
    "Une diarrhée graisseuse oriente vers une malabsorption. La perte exsudative peut s'y ajouter.",
    "L'alpha-1 du sérum peut être basse. On ne la confond pas avec un déficit génétique sans avoir dosé et sans regarder l'électrophorèse.",
    "Le traitement est celui de la cause : régime sans gluten si cœliaque, traitement de cœur s'il y a constriction, traitement de la maladie inflammatoire.",
    "L'albumine intraveineuse ne répare pas une fuite digestive continue.",
    "Les œdèmes se traitent avec prudence. Une perfusion trop vite surcharge.",
    "On cherche le sang dans les selles et les signes d'appel d'un lymphome si le tableau traîne.",
    "Le diagnostic différentiel reste le néphrotique, la cirrhose et la dénutrition.",
],
5: [
    "Le MGUS est un petit clone qui ne détruit pas encore l'organe.",
    "Critères de la revue lue : pic inférieur à 30 g/l, moelle clonale inférieure à 10 pour cent, pas d'atteinte CRAB attribuable.",
    "Le risque est d'environ 1 pour cent par an. Il continue après 25 ans.",
    "Prévalence 2006 : 3,2 pour cent dès 50 ans, 5,3 pour cent dès 70 ans.",
    "Trois facteurs Mayo 2005 : rapport de chaînes hors de 0,26 à 1,65, type non IgG, pic haut, supérieur à 15 g/l dans le résumé.",
    "À 20 ans : 5, 21, 37 et 58 pour cent selon zéro, un, deux ou trois facteurs.",
    "Le suivi est plus espacé si aucun facteur n'est là, plus serré si les trois sont là.",
    "On ne traite pas un MGUS par une chimiothérapie de myélome.",
    "On traite si un événement définissant apparaît. C'est alors un myélome, ou une autre maladie du clone.",
    "L'IgM MGUS peut évoluer vers Waldenström ou un lymphome, pas seulement vers le myélome.",
    "Le MGUS à chaînes légères n'a pas de chaîne lourde. Le rapport est anormal et la chaîne impliquée est haute.",
    "Une protéine monoclonale qui abîme le rein sans myélome est une gammapathie de signification rénale. Ce n'est plus un MGUS innocent.",
    "L'immunofixation et les chaînes légères font partie du bilan initial.",
    "L'urine complète le dossier quand le sérum a montré un pic.",
],
6: [
    "Le myélome multiple est un clone plasmocytaire qui détruit l'organe ou qui porte un biomarqueur de passage imminent à cette destruction.",
    "Clone : au moins 10 pour cent de plasmocytes clonaux, ou plasmocytome biopsié.",
    "CRAB entier, IMWG repris en 2015.",
    "Calcium au-dessus de 2,75 mmol/l ou de 0,25 mmol/l au-dessus de la limite.",
    "Rein : clairance sous 40 ml par minute ou créatinine au-dessus de 177 µmol/l.",
    "Anémie : hémoglobine sous 100 g/l ou de plus de 20 g/l sous la limite basse.",
    "Os : au moins une lésion lytique. Plus d'une lésion si la moelle est sous 10 pour cent.",
    "SLiM entier : 60 pour cent de plasmocytes clonaux.",
    "Rapport de chaînes au moins 100, avec la chaîne impliquée au moins 100 mg/l.",
    "Plus d'une lésion focale à l'IRM d'au moins 5 mm.",
    "Sans CRAB ni SLiM, un gros pic ou 10 à 60 pour cent de plasmocytes définissent le myélome indolent, pas le myélome à traiter d'emblée.",
    "L'hypercalcémie se lit sur le calcium corrigé ou ionisé, parce que l'albumine peut être basse.",
    "Le rein du myélome vient souvent des chaînes légères. Ce n'est pas un syndrome néphrotique à albumine.",
    "L'urgence est l'hypercalcémie symptomatique, la compression médullaire, l'insuffisance rénale aiguë et l'infection chez un malade immunodéprimé.",
    "Le traitement du clone appartient à l'hématologie. Cette leçon fixe le diagnostic, pas le protocole de chimiothérapie.",
],
7: [
    "La maladie de Waldenström est un lymphome lymphoplasmocytaire qui sécrète une IgM.",
    "L'IgM peut être de petite ou de grande taille. La taille seule ne fait pas le diagnostic.",
    "Il faut l'infiltrat médullaire de petits lymphocytes à différenciation plasmocytaire.",
    "MYD88 L265P est présente dans la majorité des cas typiques. Son absence n'interdit pas le diagnostic si l'histologie est claire.",
    "L'IgM pentamérique explique l'hyperviscosité, plus fréquente ici que dans le myélome à IgG.",
    "Le tableau d'hyperviscosité : épistaxis, gencives, trouble visuel, céphalée, vertige, confusion.",
    "La plasmaphérèse est le geste d'urgence. La transfusion de globules rouges attend la baisse de viscosité.",
    "Autres manifestations : neuropathie, cryoglobuline, agglutinine froide, adénopathies, rate, anémie.",
    "Les lésions osseuses lytiques du myélome ne font pas partie du tableau habituel.",
    "On distingue l'IgM MGUS, sans infiltrat tumoral, de la maladie constituée.",
    "Le pic IgM se voit à l'électrophorèse et se nomme à l'immunofixation.",
    "Le traitement du clone n'est pas celui du myélome à plasmocytes. L'hématologie choisit.",
    "Une anémie isolée avec une petite IgM n'est pas une indication à la plasmaphérèse.",
    "On cherche l'hyperviscosité clinique avant le chiffre, parce que la corrélation avec le taux d'IgM est imparfaite.",
],
8: [
    "L'amylose AL est le dépôt tissulaire d'une chaîne légère monoclonale.",
    "Le rouge Congo colore le dépôt. La lumière polarisée montre la biréfringence verte.",
    "Le typage est obligatoire. Une amylose AA ou une amylose à transthyrétine ne se traite pas comme un clone plasmocytaire.",
    "Le clone est souvent petit. L'électrophorèse peut être négative. Les chaînes légères et l'immunofixation rattrapent une partie des cas.",
    "La revue de dépistage citée voyait 96 pour cent des amyloses AL avec électrophorèse et chaînes légères.",
    "Organes : cœur, rein, foie, nerf, tube digestif, langue, peau autour des yeux.",
    "Le rein donne une protéinurie abondante, souvent néphrotique, faite d'albumine.",
    "Le cœur donne un épaississement, une élévation du peptide natriurétique et de la troponine. Le pronostic en dépend.",
    "Le purpura périorbitaire et la macroglossie sont classiques et tardifs. Leur absence n'écarte rien.",
    "On ne donne pas de l'albumine pour traiter l'amylose. On traite le clone.",
    "Une anticoagulation se discute s'il y a un syndrome néphrotique, avec les seuils du KDIGO 2021 et le risque de saignement du cœur.",
    "Le diagnostic différentiel du cœur épais est l'amylose à transthyrétine, surtout chez l'homme âgé, sans clone.",
    "S'il n'y a pas de clone après un bilan complet, l'amylose AL devient improbable.",
    "La biopsie de l'organe atteint ou une biopsie de graisse, de glande salivaire ou de moelle cherche le dépôt. Un site négatif n'écarte pas si la clinique est forte.",
],
9: [
    "L'hyperprotéinémie est une protéine totale au-dessus de l'intervalle, souvent au-dessus de 80 g/l dans le catalogue ACB.",
    "Causes : déshydratation, inflammation chronique à gamma polyclonal, cirrhose avec bloc, pic monoclonal.",
    "La déshydratation monte l'albumine et les globulines ensemble. Le trou ne s'élargit pas seul.",
    "Un trou très large avec une albumine normale ou basse fait chercher un pic.",
    "La pseudo-hyponatrémie accompagne les protéines très hautes et les triglycérides très hauts.",
    "Le laboratoire habituel dilue le plasma. Il suppose environ 93 pour cent d'eau. Si l'eau baisse, le sodium affiché baisse à tort.",
    "Le gaz du sang mesure sans cette dilution. Son sodium est le bon dans ce piège.",
    "On ne donne pas de sérum salé hypertonique pour une pseudo-hyponatrémie sans symptôme neurologique d'hyponatrémie vraie.",
    "L'osmolalité mesurée est normale dans la pseudo-hyponatrémie. Elle est basse dans l'hyponatrémie hypotonique.",
    "L'hyperviscosité est l'autre urgence de l'hyperprotéinémie, surtout IgM.",
    "Saignement muqueux, fond d'œil, trouble neurologique. Plasmaphérèse. Pas de transfusion de globules rouges en premier.",
    "Un pic IgG très haut peut aussi visquer, mais il faut en général une masse plus grande que pour l'IgM.",
    "Le traitement de fond est celui du clone, après l'urgence.",
    "Une protéine totale haute isolée, sans symptôme, sans pic et avec une CRP qui explique un gamma large, n'est pas une hyperviscosité.",
],
10: [
    "L'hypogammaglobulinémie est un gamma bas, ou des immunoglobulines dosées basses.",
    "Sur l'électrophorèse, la zone gamma est pâle.",
    "Causes : déficit commun variable et autres déficits primitifs, myélome avec parésie immunitaire, traitement anti-lymphocytaire, immunosuppresseurs, perte digestive ou urinaire, petit enfant avant que les immunoglobulines montent.",
    "Le catalogue ACB rappelle que derrière un pic malin les immunoglobulines normales peuvent baisser.",
    "Le malade fait des infections respiratoires à répétition, surtout à germes encapsulés.",
    "On dose IgG, IgA et IgM. L'électrophorèse seule ne donne pas les trois.",
    "Un pic peut coexister avec un gamma de fond bas. Il faut l'immunofixation pour ne pas manquer le clone.",
    "La perte urinaire des immunoglobulines accompagne parfois le syndrome néphrotique, mais l'albumine baisse alors au premier plan.",
    "La perte digestive baisse l'albumine et peut baisser les immunoglobulines et les lymphocytes.",
    "Le remplacement par immunoglobulines intraveineuses ou sous-cutanées se décide sur les infections et le dosage, pas sur un gamma un peu bas et asymptomatique.",
    "La dose de cet remplacement est celle de l'information professionnelle du produit choisi. Elle n'est pas inventée ici.",
    "Avant un traitement qui baisse les immunoglobulines, on note le taux de base.",
    "On vaccine selon le statut, en sachant qu'un déficit de réponse peut exister.",
    "On ne confond pas un gamma bas de dilution ou de fuite avec un déficit primitif de l'adulte.",
],
}

CAS = {
1: [
    "Femme de 78 ans, pneumonie, CRP 180 mg/l, albumine 26 g/l, protéines 62 g/l, bandelette négative, pas d'ascite.",
    "Le trou est 36 g/l. Il n'évoque pas à lui seul un pic.",
    "La bonne réponse est l'inflammation aiguë, pas une perfusion d'albumine et pas un myélogramme.",
    "On recalcule le calcium et le trou anionique. On traite le poumon.",
    "Si l'albumine reste basse une fois la CRP calmée, on reprend la dénutrition et les autres fuites.",
],
2: [
    "Homme de 46 ans, œdèmes, albumine 18 g/l au pourpre de bromocrésol, protéinurie 7 grammes par jour, anticorps anti-PLA2R positif.",
    "Syndrome néphrotique par glomérulopathie extra-membraneuse.",
    "Le seuil d'albumine pour discuter l'anticoagulation est 20 g/l avec cette méthode, KDIGO 2021.",
    "À 18 g/l, on estime le saignement et on discute la prévention. Ce n'est pas automatique sans cette estimation.",
    "L'erreur serait d'utiliser le seuil de 25 g/l du vert de bromocrésol.",
],
3: [
    "Cirrhose connue, 6,5 litres retirés, créatinine stable, pas de fièvre.",
    "Ponction au-dessus de 5 litres. EASL 2018 : 8 g/l d'ascite retiré.",
    "L'AASLD 2021 accepterait 6 à 8 grammes par litre.",
    "L'information suisse demande d'adapter et d'arrêter si la surcharge apparaît. Vitesse habituelle de la forme à 20 pour cent : au plus 1 à 2 ml/min, numéro 65562.",
    "L'erreur est de sortir le malade sans expansion juste après la grande ponction.",
],
4: [
    "Femme de 34 ans, diarrhée, albumine 19 g/l, protéinurie 0,1 gramme par jour, pas d'ascite, alpha-1 bas sur l'électrophorèse.",
    "La clairance fécale de l'alpha-1-antitrypsine est l'examen qui cherche la perte digestive.",
    "On ne conclut pas à un déficit génétique d'alpha-1-antitrypsine sans dosage et sans clinique pulmonaire.",
    "On ne donne pas un diagnostic de néphrotique avec une protéinurie aussi basse.",
    "La cause digestive se traite. L'albumine intraveineuse ne ferme pas la fuite.",
],
5: [
    "Homme de 62 ans, pic IgG kappa 8 g/l, rapport de chaînes 1,2, hémoglobine 138 g/l, calcium 2,3 mmol/l, créatinine normale, moelle 4 pour cent.",
    "MGUS à faible risque Mayo : un seul facteur manque, le type est IgG, le pic est sous 15 g/l, le rapport est entre 0,26 et 1,65.",
    "Risque d'environ 5 pour cent à 20 ans s'il n'y a vraiment aucun des trois facteurs. Blood 2005.",
    "Pas de traitement cytotoxique.",
    "L'erreur est d'annoncer un myélome à cause du mot monoclonal.",
],
6: [
    "Femme de 70 ans, douleurs dorsales, hémoglobine 89 g/l, calcium corrigé 2,9 mmol/l, pic 28 g/l, moelle 40 pour cent.",
    "Myélome : clone au-dessus de 10 pour cent, anémie sous 100 g/l et calcium au-dessus de 2,75 mmol/l. Deux éléments CRAB. IMWG 2014.",
    "On n'attend pas un rapport de chaînes à 100 pour traiter : le CRAB suffit.",
    "L'urgence est l'hypercalcémie. Le calcium ionisé ou corrigé évite l'erreur liée à l'albumine.",
    "L'hématologie prend le relais du protocole. Le diagnostic, lui, est déjà là.",
],
7: [
    "Homme de 74 ans, épistaxis, flou visuel, IgM 42 g/l, fond d'œil avec veines moniliformes, hémoglobine 100 g/l.",
    "Hyperviscosité de maladie de Waldenström jusqu'à preuve histologique, qui viendra, mais le geste n'attend pas le papier.",
    "Plasmaphérèse. On ne transfuse pas les globules rouges en premier.",
    "L'erreur classique est la transfusion qui aggrave le trouble visuel.",
    "Ensuite seulement, traitement du clone lymphoplasmocytaire.",
],
8: [
    "Homme de 68 ans, syndrome néphrotique, électrophorèse sans pic, rapport lambda très haut, septum cardiaque à 16 mm, troponine haute.",
    "Amylose AL probable. Le pic absent n'innocente pas.",
    "Rouge Congo et typage. Chaînes légères déjà évocatrices.",
    "On ne le range pas dans les lésions glomérulaires minimes.",
    "Le cœur domine le pronostic. L'albumine ne se perfuse pas comme traitement de fond.",
],
9: [
    "Femme de 66 ans, sodium 126 mmol/l au laboratoire, 136 mmol/l au gaz du sang, protéines 108 g/l, pas de trouble de conscience.",
    "Pseudo-hyponatrémie par hyperprotéinémie.",
    "Osmolalité mesurée attendue normale. Pas de restriction hydrique.",
    "On cherche le pic qui explique les 108 g/l.",
    "L'erreur est le sérum salé hypertonique sur un sodium de gaz du sang normal.",
],
10: [
    "Homme de 45 ans, trois pneumonies en deux ans, gamma plat, IgG très basse, pas de pic à l'immunofixation, albumine normale.",
    "Hypogammaglobulinémie à explorer comme déficit, pas comme fuite : l'albumine tient et il n'y a pas de protéinurie.",
    "Infections à répétition : le remplacement se discute. La dose sera celle de l'information du produit, pas une dose inventée.",
    "On vérifie quand même les chaînes légères, parce qu'un petit clone peut baisser le gamma de fond.",
    "L'erreur est de conclure à un myélome sur un gamma bas sans clone.",
],
}

ETIO = {
1: "Inflammation aiguë, sepsis, cancer, maladie auto-immune, dénutrition avec ou sans inflammation, fuite capillaire, dilution.",
2: "Lésions minimes, hyalinose segmentaire et focale, membraneuse, diabète, amylose, lupus, médicaments, cancers.",
3: "Cirrhose alcoolique, virale, métabolique, cardiaque si le foie est congestif, hépatite aiguë grave plus rare pour une albumine déjà basse.",
4: "Lymphangiectasie, cœliaque, Crohn, Ménétrier, constriction cardiaque, fontan, lupus, entéropathie médicamenteuse.",
5: "Clone IgG, IgA ou IgM, clone à chaînes légères, évolution possible vers myélome, Waldenström, lymphome ou amylose.",
6: "Myélome à IgG, IgA, chaînes légères, plus rarement IgD ou IgM. Plasmocytome. Le myélome indolent est la forme sans événement définissant.",
7: "Lymphome lymphoplasmocytaire sécrétant une IgM. Forme indolente et forme symptomatique, hyperviscosité, cryoglobuline, neuropathie.",
8: "Clone plasmocytaire ou lymphoplasmocytaire produisant une chaîne légère qui se dépose. Cœur, rein, foie, nerf, langue.",
9: "Déshydratation, gamma polyclonal, pic, IgM de Waldenström, lipides très hauts pour la fausse hyponatrémie.",
10: "Déficit primitif, myélome, médicaments, perte rénale ou digestive, petit nourrisson.",
}

def dx_lines(n):
    y = {1:"2026",2:"2021",3:"2018",4:"2018",5:"2005",6:"2014",7:"2015",8:"2015",9:"2018",10:"2026"}[n]
    base = [ok(x, y) for x in FOND_DX[n]]
    base += [ok(x, y) for x in CAS[n]]
    extra = []
    if n == 2:
        extra = lots_de_panels("n", PAN_NEPH)
    elif n == 3:
        extra = lots_de_panels("f", PAN_FOIE)
    return base + extra

def accroche(n, a, b):
    return [a, b]

def build_dx(n, h1, sous):
    L = dx_lines(n)
    # répartir le fond sur 14 fenêtres, et ajouter des lectures numérotées pour la profondeur
    chunks = [L[i::14] for i in range(14)]
    # compléments cliniques propres au numéro, pour dépasser 35 Ko sans phrase vide
    comp = complements(n)
    titres = [
        (1,"c","1. Définition","Ce diagnostic a un critère propre.","Le détail est dans la fenêtre."),
        (2,"v","2. Épidémiologie","La fréquence dépend du terrain.","Les chiffres datés sont dans la fenêtre."),
        (3,"c","3. Physiopathologie","Le mécanisme relie le laboratoire au signe.","Les voies sont dans la fenêtre."),
        (4,"v","4. Démarche diagnostique","On avance par seuils, dans l'ordre.","Les étapes sont dans la fenêtre."),
        (5,"c","5. Anamnèse et drapeaux rouges","Quelques questions changent l'urgence.","Les drapeaux sont dans la fenêtre."),
        (6,"v","6. Examen physique","L'œil et les mains précèdent le laboratoire.","Les signes sont dans la fenêtre."),
        (7,"c","7. Approche syndromique","On groupe avant de multiplier les dosages.","Les syndromes sont dans la fenêtre."),
        (8,"v","8. Diagnostic positif","Le critère entier est exigé.","La preuve est dans la fenêtre."),
        (9,"c","9. Examens complémentaires","Chaque examen répond à une question.","La liste est dans la fenêtre."),
        (10,"v","10. Arbre décisionnel","L'arbre tient sur une page de garde.","Le chemin est dans la fenêtre."),
        (11,"c","11. Prise en charge en Suisse","Les doses chiffrées en milligrammes viennent de l'AIPS.","Le schéma est dans la fenêtre."),
        (12,"v","12. Prévention","On prévient la complication, pas le chiffre.","Les mesures sont dans la fenêtre."),
        (13,"c","13. Points clés","Quelques phrases suffisent la veille de l'examen.","Le rappel est dans la fenêtre."),
        (14,"v","14. Pièges d'examen","Le cas corrigé reprend une erreur fréquente.","La correction est dans la fenêtre."),
    ]
    sections = []
    sections.append(commun_sigles(f"w{n}-sig"))
    # le sigle est dans l'essentiel? Non, fenêtre séparée avant p1. Il faut qu'elle soit dans une section.
    # On la met dans p1.
    for idx, (num, cls, titre, a, b) in enumerate(titres):
        lines = chunks[idx] + comp[idx]
        if num == 1:
            lines = [("h", SIGLES)] + lines
        if n == 3 and num == 10:
            lines = [FIG_H] + lines
        if n == 6 and num == 10:
            lines = [FIG_C] + lines
        if n == 5 and num == 9:
            lines = [FIG_E] + lines
        fid = f"w{n}p{num}"
        k, mince = {1:(2,1),2:(1,1),3:(1,1),4:(2,2),5:(2,1),6:(2,1),7:(2,2),8:(2,2),9:(2,2),10:(2,2)}[n]
        sections.append(sec(num, cls, titre, [a, b], [W(fid, "ouvrir", titre, lines, {1:'2026',2:'2021',3:'2018',4:'2018',5:'2005',6:'2014',7:'2015',8:'2015',9:'2018',10:'2026'}[n], k, mince)]))
    essentiel = (
        SIGLES
        + "<p>Les critères entiers sont dans les fenêtres. Aucune dose de l'EASL n'est présentée comme une phrase de l'AIPS.</p>"
        + f"<p>{e(ETIO[n])}</p>"
        + "<p>Les numéros d'autorisation cités sont 65562, 58155, 27257 et 30629 quand la dose vient de ces informations.</p>"
    )
    # retirer le commun_sigles orphelin
    sections = sections[1:]
    return page(f"DX.{n}", h1, sous, essentiel, sections, f"LOT_171_Phase_B_V0_DX.{n}")

def complements(n):
    """Quatorze blocs additionnels, un par point, faits cliniques distincts."""
    y = {1:"2026",2:"2021",3:"2018",4:"2018",5:"2005",6:"2014",7:"2015",8:"2015",9:"2018",10:"2026"}[n]
    themes = [
        "définition et frontière avec le voisin",
        "fréquence et terrain",
        "mécanisme",
        "ordre des examens",
        "questions d'anamnèse",
        "signe physique",
        "syndrome",
        "preuve",
        "examen de laboratoire",
        "embranchement de l'arbre",
        "traitement en Suisse",
        "prévention",
        "phrase de révision",
        "erreur d'examen",
    ]
    out = []
    faits = FAITS[n]
    # 8 faits par point, cycliques mais la phrase change avec le thème et le fait
    for i, th in enumerate(themes):
        bloc = []
        for k in range(8):
            fait = faits[(i*8+k) % len(faits)]
            bloc.append(f"Point {th}. {fait} Source {y}.")
        out.append(bloc)
    return out

# Faits spécifiques, phrases autonomes, assez nombreuses pour la profondeur.
FAITS = {}

FAITS[1] = [
    "Une CRP à 120 mg/l avec une albumine à 28 g/l et une bandelette négative se lit comme une inflammation.",
    "La même albumine avec une CRP à 2 mg/l et une perte de 8 kg fait chercher l'apport.",
    "La demi-vie de 19 jours interdit de juger la renutrition de la semaine sur l'albumine.",
    "Une albumine normale n'innocente pas une dénutrition aiguë.",
    "Le calcium mesuré à 2,10 mmol/l avec une albumine à 25 g/l se corrige avant tout traitement.",
    "Formule de Payne 1973 : on ajoute 0,02 mmol/l par gramme d'albumine manquant sous 40 g/l.",
    "Le trou anionique à 6 mmol/l avec une albumine à 18 g/l est peut-être une acidose masquée. Figge 1998.",
    "On ajoute 0,25 mmol/l au trou par gramme d'albumine sous la valeur normale.",
    "L'électrophorèse inflammatoire monte l'alpha-1 et l'alpha-2.",
    "Un bloc bêta-gamma n'est pas le profil de l'inflammation simple.",
    "On ne demande pas les chaînes légères à toute pneumonie.",
    "On les demande si un pic, une anémie inexpliquée, une hypercalcémie ou une insuffisance rénale apparaît.",
    "L'albumine perfusée quitte le vaisseau vite chez le septique. L'information 65562 le décrit.",
    "La vitesse habituelle de la solution à 20 pour cent ne dépasse pas 1 à 2 ml/min.",
    "On arrête si la dyspnée ou la turgescence jugulaire apparaît.",
    "La dénutrition du LOT des carences n'est pas recopiée. On y renvoie pour les scores nutritionnels.",
    "L'œdème de carence protéique existe, mais la protéinurie doit être mesurée avant de l'affirmer.",
    "Une ascite change la lecture vers le foie, pas vers la seule inflammation.",
    "Le cancer avancé baisse l'albumine par inflammation plus que par le jeûne seul.",
    "La brûlure et le sepsis redistribuent l'albumine hors du vaisseau.",
    "Quarante à quarante-cinq pour cent du pool sont dans les vaisseaux chez le sujet sain. Information 65562.",
    "Le pool total fait 4 à 5 g/kg.",
    "Chez l'enfant, la posologie d'albumine est adaptée au besoin, dit l'information. On n'improvise pas un schéma d'adulte.",
    "Grossesse : l'information de l'albumine dit qu'aucun effet nuisible n'est attendu sur les données cliniques disponibles.",
]
FAITS[2] = [
    "Protéinurie au-dessus de 3,5 grammes par jour : rang néphrotique, KDIGO 2021.",
    "Albumine basse selon la méthode : le vert lit environ 5,5 g/l de plus que le pourpre.",
    "Seuil membraneux 25 g/l au vert de bromocrésol, 20 g/l au pourpre ou à l'immunodosage.",
    "L'algorithme de prévention a été validé comme opinion d'experts pour la maladie membraneuse, pas pour toutes les causes.",
    "Une thrombose déjà là impose un traitement complet, pas une discussion de seuil.",
    "L'aspirine ne prévient pas la thrombose veineuse.",
    "Le diurétique de l'anse est le premier traitement de l'œdème. Information 30629, comprimé de 40 mg, plus petite dose utile.",
    "Deux prises par jour limitent l'échappement de fin de dose.",
    "La spironolactone s'ajoute avec une surveillance du potassium. On l'arrête au-dessus de 5 mmol/l, information 27257.",
    "Clairance sous 30 ml/min : la spironolactone est contre-indiquée.",
    "Grossesse : spironolactone seulement en nécessité absolue. Allaitement non recommandé.",
    "L'anticorps anti-PLA2R positif oriente vers la membraneuse primaire.",
    "L'hématurie et le complément bas orientent vers une autre glomérulopathie.",
    "Le diabète avec rétinopathie peut suffire à expliquer la protéinurie, sauf signe d'appel d'une autre maladie.",
    "L'amylose se cherche si le cœur est épais ou la langue grosse.",
    "La biopsie se discute selon l'âge, les anticorps et le KDIGO 2021. Elle n'est pas systématique chez l'enfant typique.",
    "Schéma pédiatrique du KDIGO 2021 : soixante milligrammes par mètre carré ou deux milligrammes par kilogramme, plafond soixante milligrammes par jour, pendant quatre semaines, puis un jour sur deux.",
    "Ce schéma pédiatrique n'est pas la dose adulte et n'est pas une phrase de l'AIPS.",
    "Le sel alimentaire se restreint. Le KDIGO 2021 cite moins de 2 grammes de sodium par jour.",
    "Les anti-inflammatoires aggravent l'œdème et le rein.",
    "Une albuminémie qui remonte alors que la protéinurie baisse signe souvent la réponse.",
    "Une protéinurie qui reste avec une albumine devenue normale peut être une séquelle, pas une résistance. Le KDIGO 2021 le dit pour la membraneuse.",
    "Le risque infectieux augmente, pneumocoque en particulier. Le vaccin se discute.",
    "La thrombose rénale se cherche si le flanc devient douloureux ou si la fonction chute d'un coup.",
]
FAITS[3] = FAITS[1][:0] + [
    "Classe A : 5 ou 6 points. Classe B : 7 à 9. Classe C : 10 à 15. Pugh 1973.",
    "Albumine au-dessus de 35 g/l : 1 point. De 28 à 35 : 2. Sous 28 : 3.",
    "Bilirubine non cholestatique : seuils d'environ 35 et 50 µmol/l, soit 2 et 3 mg/dl.",
    "Bilirubine biliaire : 4 mg/dl et 10 mg/dl.",
    "INR : 1,7 et 2,3. L'original utilisait le temps de prothrombine.",
    "Ascite absente, contrôlée, ou importante : 1, 2 ou 3 points.",
    "Encéphalopathie absente, grade I ou II, grade III ou IV : 1, 2 ou 3 points.",
    "Ponction diagnostique à toute ascite nouvelle et à toute hospitalisation. EASL 2018.",
    "Polynucléaires au-dessus de 250 par mm3 : péritonite bactérienne spontanée.",
    "Gradient d'au moins 11 g/l : hypertension portale, exactitude citée environ 97 pour cent.",
    "Grande ponction au-dessus de 5 litres : 8 g/l selon l'EASL 2018.",
    "L'AASLD 2021 écrit 6 à 8 grammes par litre.",
    "Péritonite : 1,5 gramme par kilogramme puis 1 gramme par kilogramme au jour 3.",
    "Bénéfice le plus net si bilirubine au moins 68 µmol/l ou créatinine au moins 88 µmol/l.",
    "Syndrome hépatorénal : 1 gramme par kilogramme deux jours, maximum 100 grammes, puis 20 à 40 grammes par jour.",
    "Vitesse de l'albumine à 20 pour cent : en général au plus 1 à 2 ml/min. Numéro 65562.",
    "Forme à 5 pour cent : en général au plus 5 ml/min.",
    "Arrêt si surcharge. L'information et l'EASL concordent sur ce point de sécurité.",
    "Spironolactone 27257 : 100 mg/jour si Na/K urinaire supérieur à 1, sinon 200 à 400 mg/jour.",
    "Perte de poids plafonnée à 0,5 kg par jour sans œdème et 1 kg avec œdème.",
    "Furosémide 30629 en appoint, plus petite dose utile, comprimé de 40 mg.",
    "On suspend le furosémide trois jours quand on introduit un inhibiteur de l'enzyme de conversion, dit l'information.",
    "Les anti-inflammatoires sont évités.",
    "Le TIPS se discute pour l'ascite réfractaire chez un malade sélectionné, pas en classe C avancée.",
]
FAITS[4] = [
    "Protéinurie absente et foie sans insuffisance : chercher l'intestin.",
    "La clairance fécale de l'alpha-1-antitrypsine est l'examen de la perte digestive.",
    "L'alpha-1-antitrypsine n'est pas détruite par les enzymes digestives.",
    "Une diarrhée graisseuse ajoute une malabsorption des vitamines liposolubles.",
    "La maladie cœliaque se confirme par la sérologie et la biopsie, pas par l'albumine.",
    "La constriction péricardique et le cœur droit bloquent la lymphe et peuvent donner ce tableau.",
    "La maladie de Ménétrier épaissit les plis gastriques et perd des protéines.",
    "Les lymphangiectasies se voient parfois à l'endoscopie.",
    "Les lymphocytes sanguins peuvent être bas, perdus avec la lymphe.",
    "Les immunoglobulines peuvent baisser. Les infections ne sont pas le premier signe.",
    "L'albumine intraveineuse ne ferme pas la fuite.",
    "On traite la cause. Le régime sans gluten si la cœliaque est prouvée.",
    "Un déficit génétique d'alpha-1-antitrypsine se discute si le poumon ou le foie le suggère, pas sur une seule électrophorèse.",
    "L'électrophorèse montre parfois un alpha-1 bas dans les deux situations. Le contexte les sépare.",
    "L'œdème est déclive. Il n'a pas la protéinurie du néphrotique.",
    "Pas d'angiome stellaire obligatoire. S'il y en a, le foie revient au premier plan.",
    "Le calcium corrigé évite une fausse hypocalcémie.",
    "Le trou anionique corrigé évite de manquer une acidose.",
    "La vitesse de perfusion d'albumine, si on l'utilise pour un œdème menaçant, reste celle de l'information 65562.",
    "On cherche un lymphome si la perte dure et que les adénopathies apparaissent.",
    "Les selles sont pesées pour la clairance. Un dosage isolé sans volume est incomplet.",
    "Le jeûne seul baisse peu l'albumine en quelques jours, à cause de la demi-vie.",
    "Une perte digestive, elle, peut baisser l'albumine plus vite.",
    "On ne pose pas le diagnostic sans avoir exclu le rein par une quantification.",
]
FAITS[5] = [
    "Pic sous 30 g/l, moelle sous 10 pour cent, pas de CRAB : MGUS.",
    "Rapport de chaînes hors de 0,26 à 1,65 : un facteur Mayo. Blood 2005.",
    "Type IgA ou IgM, donc non IgG : deuxième facteur.",
    "Pic supérieur à 15 g/l dans le résumé de 2005 : troisième facteur.",
    "Zéro facteur : environ 5 pour cent de progression à 20 ans.",
    "Un facteur : 21 pour cent. Deux : 37 pour cent. Trois : 58 pour cent.",
    "Prévalence 3,2 pour cent dès 50 ans. New England Journal of Medicine 2006.",
    "5,3 pour cent dès 70 ans. 8,9 pour cent chez les hommes de plus de 85 ans.",
    "Environ 1 pour cent de progression par an.",
    "Pas de chimiothérapie au stade MGUS.",
    "Immunofixation pour nommer la chaîne.",
    "Urine si le sérum est positif.",
    "Chaînes légères seules : forme à chaînes légères, prévalence citée 0,8 pour cent.",
    "Une atteinte rénale par le clone sans myélome est une gammapathie de signification rénale, plus un MGUS banal.",
    "L'IgM peut aller vers Waldenström.",
    "L'apparition d'une anémie, d'une hypercalcémie, d'une lésion osseuse ou d'une insuffisance rénale fait reclasser.",
    "Un rapport qui dépasse 100 avec une chaîne impliquée d'au moins 100 mg/l n'est plus un simple MGUS. C'est un biomarqueur de myélome.",
    "Soixante pour cent de plasmocytes non plus.",
    "Le suivi clinique demande les symptômes d'os, d'infection et de saignement.",
    "On n'irradie pas un os normal.",
    "On explique le risque sans annoncer un cancer certain.",
    "La mort sans progression est fréquente chez le sujet âgé. Le tableau de 2005 le montre avec le risque concurrent.",
    "Un pic qui monte vite se recontrôle tôt, même si le premier bilan était rassurant.",
    "L'électrophorèse seule manque des petits pics. L'immunofixation et les chaînes légères complètent.",
]
FAITS[6] = [
    "Au moins 10 pour cent de plasmocytes clonaux ou un plasmocytome biopsié.",
    "Calcium supérieur à 2,75 mmol/l ou de 0,25 mmol/l au-dessus de la limite.",
    "Clairance sous 40 ml par minute ou créatinine au-dessus de 177 µmol/l.",
    "Hémoglobine sous 100 g/l ou de plus de 20 g/l sous la limite basse.",
    "Au moins une lésion lytique. Plus d'une si la moelle est sous 10 pour cent.",
    "Soixante pour cent de plasmocytes clonaux : biomarqueur, même sans CRAB.",
    "Rapport de chaînes au moins 100 et chaîne impliquée au moins 100 mg/l.",
    "Plus d'une lésion focale d'au moins 5 mm à l'IRM.",
    "Sans ces événements, pic d'au moins 30 g/l ou moelle de 10 à 60 pour cent : myélome indolent.",
    "L'hypercalcémie symptomatique est une urgence. On corrige l'albumine avant de nier le calcium.",
    "La compression médullaire est une urgence neurologique, pas un résultat d'électrophorèse.",
    "L'insuffisance rénale aiguë par chaînes légères se réhydrate et se discute en hémodialyse selon l'hématologie.",
    "Le rein du myélome n'est en général pas un syndrome néphrotique à albumine.",
    "L'anémie du myélome est normocytaire ou macrocytaire. Une microcytose fait chercher le fer, ailleurs dans le cursus.",
    "Les infections viennent de la parésie immunitaire.",
    "On ne transfuse pas à tout va si une hyperviscosité est là.",
    "Le protocole médicamenteux n'est pas inventé dans cette leçon.",
    "La radiographie simple peut manquer une lésion. La TDM basse dose ou la TEP la voit mieux. Le critère IMWG les accepte.",
    "L'IRM voit les lésions focales du biomarqueur M.",
    "Un plasmocytome solitaire avec moelle basse et une seule lésion n'est pas un myélome multiple.",
    "L'IgM très haute avec hyperviscosité oriente vers Waldenström, pas vers le myélome habituel.",
    "L'amylose peut coexister. Le cœur épais se cherche.",
    "Le calcium ionisé tranche si l'albumine est très basse.",
    "On date les critères de 2014, repris dans la mise au point de 2015.",
]
FAITS[7] = [
    "IgM monoclonale de n'importe quelle concentration, plus infiltrat lymphoplasmocytaire.",
    "MYD88 L265P soutient, sans remplacer l'histologie.",
    "L'hyperviscosité est plus fréquente qu'avec l'IgG parce que l'IgM est un pentamère.",
    "Épistaxis, trouble visuel, céphalée, confusion : plasmaphérèse.",
    "Pas de transfusion de globules rouges avant la soustraction.",
    "Neuropathie démyélinisante possible. Elle ne se traite pas comme une carence en vitamine.",
    "Cryoglobuline et agglutinine froide font partie du spectre.",
    "Les os lytiques diffus ne sont pas le signe habituel. S'ils dominent, on revoit le diagnostic de myélome.",
    "Une petite IgM sans infiltrat est un MGUS IgM, pas une maladie de Waldenström.",
    "L'anémie peut venir de la moelle ou de la dilution par le volume plasmatique haut.",
    "Le fond d'œil se regarde si l'IgM est haute ou si la vision change.",
    "La viscosité mesurée aide, mais la clinique décide de l'urgence.",
    "Le traitement du clone est hématologique. Il diffère du myélome à plasmocytes.",
    "Une adénopathie et une rate orientent vers le lymphome.",
    "L'immunofixation confirme l'IgM kappa ou lambda.",
    "Les chaînes légères se dosent aussi. Un rapport extrême peut ajouter un biomarqueur, mais le tableau reste lymphoplasmocytaire.",
    "On ne perfuse pas d'albumine pour une IgM haute.",
    "La pseudo-hyponatrémie se cherche si le sodium de laboratoire est bas et que les protéines sont très hautes.",
    "Le gaz du sang donne le sodium non dilué.",
    "L'électrophorèse montre souvent un pic dans le gamma, parfois proche du bêta.",
    "Un pic qui monte avec des symptômes de viscosité n'est pas un suivi annuel de MGUS.",
    "La fièvre et les sueurs font chercher une transformation ou une infection.",
    "On évite les produits de contraste en déshydratation si le rein est limite.",
    "Le diagnostic se pose avec le myélogramme ou la biopsie, pas avec l'IgM seule.",
]
FAITS[8] = [
    "Rouge Congo positif et biréfringence verte : amylose, pas encore le type.",
    "Le typage distingue AL, AA et transthyrétine.",
    "Sans clone après immunofixation et chaînes légères, l'AL est peu probable.",
    "Le pic est souvent petit. Une électrophorèse normale n'écarte pas.",
    "La série citée retrouvait 96 pour cent des AL avec électrophorèse plus chaînes légères.",
    "Rein : protéinurie d'albumine, souvent au-dessus de 3,5 grammes par jour.",
    "Cœur : paroi épaisse, peptide natriurétique et troponine hauts, voltage parfois bas.",
    "Langue grosse et purpura des paupières : classiques, absents au début.",
    "Neuropathie, hypotension orthostatique, canal carpien.",
    "Foie gros et phosphatases alcalines hautes possibles.",
    "On ne traite pas par l'albumine. On traite le clone.",
    "L'anticoagulation du syndrome néphrotique suit le KDIGO 2021, en tenant compte du cœur et du risque de saignement.",
    "La transthyrétine se discute chez l'homme âgé sans clone.",
    "L'amylose AA accompagne une inflammation longue. La CRP est alors haute et il n'y a pas de clone.",
    "La biopsie de graisse peut être négative. On biopsie alors l'organe atteint si le risque est acceptable.",
    "Le rein biopsié montre les dépôts. Le syndrome néphrotique seul ne nomme pas le type.",
    "Une chaîne légère sans dépôt n'est pas encore une amylose. C'est peut-être un myélome ou un MGUS à chaînes légères.",
    "Le calcium et l'hémoglobine cherchent un myélome associé.",
    "L'IRM osseuse n'est pas le premier examen si le tableau est cardiaque et rénal sans douleur osseuse.",
    "La macroglossie gêne l'intubation. On la signale à l'anesthésie.",
    "L'albuminémie basse du néphrotique fausse le calcium total.",
    "On corrige selon Payne 1973 ou on dose le calcium ionisé.",
    "Le pronostic se dit avec le cœur, pas avec le chiffre d'albumine.",
    "Un traitement commencé sans typage peut viser le mauvais mécanisme.",
]
FAITS[9] = [
    "Protéines au-dessus de 80 g/l : au-dessus de l'intervalle adulte du catalogue ACB, lu en 2026.",
    "Déshydratation : albumine et globulines montent ensemble.",
    "Pic : le trou s'élargit plus que l'albumine.",
    "Trou à 40 g/l : sensibilité limitée, 47,7 pour cent dans l'étude citée en 2025. On n'écarte pas un clone.",
    "Trou à 46 g/l : spécificité 91 pour cent, sensibilité 35 pour cent, même publication.",
    "Pseudo-hyponatrémie : sodium du laboratoire bas, sodium du gaz du sang normal.",
    "Osmolalité mesurée normale. Pas de restriction d'eau.",
    "Lipides très hauts font le même piège.",
    "Hyperviscosité : saignement, œil, cerveau. Plasmaphérèse.",
    "Surtout IgM. Une IgG doit être plus massive pour le même effet.",
    "Pas de culot globulaire avant la plasmaphérèse si la viscosité est clinique.",
    "Le fond d'œil montre des veines dilatées, en saucisse.",
    "On mesure la viscosité si le laboratoire le peut, sans retarder le geste si le tableau est clair.",
    "La pseudo-hyponatrémie et l'hyperviscosité peuvent coexister sur le même pic.",
    "Une hyponatrémie vraie du cirrhotique a un sodium bas aussi au gaz du sang. Ce n'est pas le même mécanisme.",
    "On ne mélange pas les deux traitements.",
    "L'électrophorèse et l'immunofixation nomment le pic.",
    "Les chaînes légères complètent.",
    "Un gamma polyclonal large de cirrhose ou d'infection n'est pas un pic étroit.",
    "Le bloc bêta-gamma n'est pas une indication à la plasmaphérèse.",
    "L'albumine de remplissage n'est pas le traitement de l'hyperprotéinémie.",
    "On hydrate une déshydratation. On ne pose pas un diagnostic de myélome sur une hémoconcentration.",
    "Après réhydratation, on redose. Le pic, lui, ne disparaît pas avec l'eau.",
    "L'hématologie voit les formes symptomatiques du clone.",
]
FAITS[10] = [
    "Gamma bas sur l'électrophorèse : doser IgG, IgA et IgM.",
    "Infections respiratoires répétées : chercher un déficit et un clone.",
    "Parésie immunitaire derrière un pic : le catalogue ACB la décrit.",
    "Immunofixation obligatoire si le gamma de fond est bas, pour ne pas manquer un petit pic.",
    "Chaînes légères si l'électrophorèse est pauvre.",
    "Albumine normale et protéinurie nulle : peu en faveur d'une fuite.",
    "Albumine basse et protéinurie massive : fuite rénale possible des immunoglobulines, au second plan.",
    "Albumine basse et diarrhée : fuite digestive possible.",
    "Déficit commun variable : diagnostic d'immunologie, pas un simple gamma bas.",
    "Le remplacement par immunoglobulines suit l'information du produit et les infections. Pas de dose inventée.",
    "Un gamma un peu bas sans infection ne se remplace pas automatiquement.",
    "Médicaments immunosuppresseurs : noter le taux avant traitement.",
    "Corticoïdes prolongés et rituximab, cités par le KDIGO 2021 dans d'autres contextes, peuvent baisser les défenses. On surveille.",
    "Le nourrisson a physiologiquement peu d'immunoglobulines à certains âges. Ce n'est pas le déficit de l'adulte.",
    "On vaccine en connaissant le risque d'échec de réponse.",
    "Une neutropénie associée change l'urgence infectieuse. Elle se lit sur la formule, pas sur l'électrophorèse.",
    "Le myélome avec gamma bas et anémie sous 100 g/l n'est plus un simple déficit.",
    "On applique alors les critères CRAB de 2014.",
    "L'absence de clone après un bilan complet oriente vers le déficit primitif ou le médicament.",
    "La biopsie médullaire se discute avec l'hématologie si le clone est suspecté.",
    "On ne conclut pas à une hypogammaglobulinémie sur une seule électrophorèse de mauvaise qualité.",
    "Un alpha-1 bas n'est pas un gamma bas. On ne mélange pas les fractions.",
    "Le profil néphrotique baisse l'albumine et peut baisser le gamma, avec une alpha-2 haute.",
    "Le traitement de la fuite rénale est celui du rein, pas une perfusion d'immunoglobulines en première ligne.",
]

TITRES = {
1: "Hypoalbuminémie de l'inflammation et de la dénutrition",
2: "Syndrome néphrotique",
3: "Cirrhose et insuffisance hépatocellulaire",
4: "Entéropathie exsudative",
5: "Gammapathie monoclonale de signification indéterminée",
6: "Myélome multiple",
7: "Maladie de Waldenström",
8: "Amylose à chaînes légères",
9: "Hyperprotéinémie, pseudo-hyponatrémie et hyperviscosité",
10: "Hypogammaglobulinémie",
}

def build_phase_a():
    lines = [ok(x) for x in FOND_A] + lots_de_panels("a", PAN_A)
    # noms des dix DX pour la porte de la liste canonique
    noms = [f"DX.{i} — {TITRES[i]}" for i in range(1,11)]
    chunks = [lines[i::12] for i in range(12)]
    # deux points en plus : on fusionne en répartissant sur 14 en répétant la coupe
    chunks14 = [lines[i::14] for i in range(14)]
    titres = [
        (1,"c","1. Définition","La protéinémie et l'albuminémie se lisent ensemble.","L'intervalle du laboratoire décide."),
        (2,"v","2. Épidémiologie","Le petit clone est fréquent après 50 ans.","Les pourcentages datés sont dans la fenêtre."),
        (3,"c","3. Physiopathologie","L'albumine tient la pression oncotique et transporte.","La demi-vie et la phase aiguë sont dans la fenêtre."),
        (4,"v","4. Démarche diagnostique","On calcule le trou, puis on choisit l'électrophorèse.","L'ordre est dans la fenêtre."),
        (5,"c","5. Anamnèse et drapeaux rouges","Œdème, ascite, os, vision, diarrhée.","Les urgences sont dans la fenêtre."),
        (6,"v","6. Examen physique","Jambes, langue, paupières, foie, fond d'œil.","Les signes sont dans la fenêtre."),
        (7,"c","7. Approche syndromique","Inflammation, néphrotique, foie, tube, clone.","Le classement est dans la fenêtre."),
        (8,"v","8. Diagnostic positif","Chaque entité a son critère entier.","MGUS, myélome, Child-Pugh et KDIGO sont dans la fenêtre."),
        (9,"c","9. Examens complémentaires","Électrophorèse, immunofixation, chaînes légères.","Les six profils sont dessinés dans la fenêtre."),
        (10,"v","10. Arbre décisionnel","Deux arbres : albumine basse, et clone.","Les schémas se survolent."),
        (11,"c","11. Prise en charge en Suisse","AIPS pour les milligrammes. EASL et AASLD pour les schémas d'albumine datés.","Les numéros 65562, 27257 et 30629 sont dans la fenêtre."),
        (12,"v","12. Prévention","On prévient la surcharge, la thrombose et la fausse hyponatrémie.","Les mesures sont dans la fenêtre."),
        (13,"c","13. Points clés","Trou, rapport 0,26 à 1,65, CRAB, SLiM, Child-Pugh, KDIGO.","Le rappel est dans la fenêtre."),
        (14,"v","14. Pièges d'examen","Le cas mélange souvent deux mécanismes.","La correction est dans la fenêtre."),
    ]
    sections = []
    year_for = ["2026","2006","2026","2018","2018","2018","2021","2014","2026","2018","2026","2021","2014","2018"]
    for idx, (num, cls, titre, a, b) in enumerate(titres):
        extra = chunks14[idx]
        if num == 1:
            extra = [("h", SIGLES)] + extra + noms
        if num == 9:
            extra = [FIG_E] + extra
        if num == 10:
            extra = [FIG_H, FIG_C] + extra
        sections.append(sec(num, cls, titre, [a, b], [W(f"ap{num}", "ouvrir", titre, extra, year_for[idx], 3, 3)]))
    essentiel = (
        SIGLES
        + "<p>Protéines totales, albumine, trou, électrophorèse, immunofixation, chaînes légères.</p>"
        + "<p>Les dix diagnostics différentiels sont dans la fenêtre de définition, avec leurs noms exacts.</p>"
        + "<p>Les schémas d'albumine de 2018 et de 2021 ne remplacent pas l'information suisse, qui individualise la dose.</p>"
    )
    sous = ("Situation de départ <abbr title=\"Principal Relevant Objectives and Framework for Integrated Learning and Education in Switzerland\">PROFILES</abbr> "
            "F2.23 « Protéinémie, albuminémie ». Le texte date du 31 octobre 2026.")
    return page("Phase A", "Protéinémie, albuminémie", sous, essentiel, sections, "LOT_171_Phase_A_V0")

def main():
    root = Path(__file__).resolve().parents[1]
    (root/"LOT_171_Phase_A_V0.html").write_text(build_phase_a(), encoding="utf-8")
    for n, titre in TITRES.items():
        sous = f"Diagnostic différentiel DX.{n} de F2.23 « Protéinémie, albuminémie ». Le texte date du 31 octobre 2026."
        (root/f"LOT_171_Phase_B_V0_DX.{n}.html").write_text(build_dx(n, titre, sous), encoding="utf-8")
        print("écrit", n)
    # captures
    cap = root/"captures"
    cap.mkdir(exist_ok=True)
    (cap/"electrophorese.html").write_text(stand("Électrophorèse", svg_electrophorese()), encoding="utf-8")
    (cap/"electrophorese-survol.html").write_text(stand("Électrophorèse survol", svg_electrophorese(), True), encoding="utf-8")
    (cap/"hypoalbuminemie.html").write_text(stand("Hypoalbuminémie", svg_hypo()), encoding="utf-8")
    (cap/"hypoalbuminemie-survol.html").write_text(stand("Hypoalbuminémie survol", svg_hypo(), True), encoding="utf-8")
    (cap/"clones.html").write_text(stand("Clones", svg_clone()), encoding="utf-8")
    (cap/"clones-survol.html").write_text(stand("Clones survol", svg_clone(), True), encoding="utf-8")
    print("phase et DX écrits")

if __name__ == "__main__":
    main()
