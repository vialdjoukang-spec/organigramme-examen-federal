#!/usr/bin/env python3
"""Assemble les 11 leçons V8 du LOT_139. Zéro réseau. Phrases courtes, doses AIPS."""
from __future__ import annotations

import html
import importlib.util
import re
import subprocess
import sys
from pathlib import Path

RACINE = Path(__file__).resolve().parents[3]
LOT = RACINE / "grok-LOTS-html" / "LOT_139"
sys.path.insert(0, str(RACINE / "harnais"))

spec = importlib.util.spec_from_file_location("moteur139", LOT / "_travail" / "moteur.py")
moteur = importlib.util.module_from_spec(spec)
spec.loader.exec_module(moteur)

CIBLES = {
    "A": (74800, 77800),
    "1": (37200, 39000),
    "2": (40200, 42000),
    "3": (42800, 44600),
    "4": (45000, 46800),
    "5": (46200, 48000),
    "6": (36600, 38400),
    "7": (41000, 42800),
    "8": (43600, 45400),
    "9": (45400, 47200),
    "10": (38800, 40600),
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
    1: "La définition sépare le bleu du sang et le bleu d'un pigment.",
    2: "Les fréquences lues concernent la dyspnée urgente, pas un rang des dix diagnostics.",
    3: "Cinq mécanismes d'hypoxémie et deux bleus, central ou périphérique, tiennent le fond.",
    4: "La démarche commence par les voies aériennes, le choc, puis la cible d'oxygène.",
    5: "L'anamnèse cherche le médicament, la douleur, le mollet et l'orthopnée.",
    6: "L'examen compare la langue, les lèvres, le lobule et le thorax.",
    7: "Dix lectures syndromiques se rangent sans classement de fréquence inventé.",
    8: "Le diagnostic positif s'appuie sur le gaz, la co-oxymétrie ou l'image, selon le mécanisme.",
    9: "Les examens gardent le saturomètre, le gaz, le tracé et l'image.",
    10: "L'arbre exclut d'abord ce qui tue, puis ce qui mime le bleu.",
    11: "La prise en charge cite l'oxygène et les trois autorisations lues, sans dose inventée.",
    12: "La prévention note la cible, le médicament oxydant et l'allaitement.",
    13: "Les points clés se redisent au lit, avec les deux bleus et les cibles côte à côte.",
    14: "Les pièges viennent d'une couleur crue, d'un saturomètre trompeur ou d'une dose hors texte.",
}

AIPS = '<abbr title="information professionnelle suisse">AIPS</abbr>'

# sec|src|U|clause   U=1 : vrai dans tout contexte, donc répétable.
COMMUNE = r"""
1|1|1|la cyanose est une coloration bleuâtre de la peau ou des muqueuses
1|1|1|sa reconnaissance dépend de la pigmentation, de la lumière et de l'observateur
1|1|1|une langue bleue avec des lèvres bleues oriente vers une cyanose centrale
1|1|1|des lèvres bleues avec une langue rose orientent vers une cyanose périphérique
1|1|1|on réchauffe le lobule jusqu'au retour du pouls capillaire
1|1|1|si le bleu du lobule persiste au réchauffement, la cyanose est centrale
1|1|1|si le bleu du lobule disparaît au réchauffement, la cyanose est périphérique
1|1|1|la cyanose périphérique traduit une extraction accrue sur un sang artériel bien saturé
1|1|1|une cyanose limitée aux extrémités est périphérique
1|1|1|la couleur seule est peu fiable et appelle une mesure
1|1|1|le pigment d'argent, d'or, d'arsenic ou de plomb peut mimer le bleu
1|1|1|la phénothiazine, l'amiodarone et la chloroquine peuvent foncer la peau sans hypoxémie
3|1|1|l'oxygène pur, en cas de shunt, laisse la pression artérielle sous 500 mmHg
3|1|1|cette même limite de shunt se lit aussi sous 66 kPa
2|2|1|près de quatre pour cent des admissions urgentes le sont pour une dyspnée aiguë
2|2|1|en 2014, les urgences genevoises ont admis plus de 3000 patients pour dyspnée
2|2|1|six pour cent de ces patients genevois vont aux soins intensifs
2|2|1|près de deux pour cent décèdent pendant l'hospitalisation
2|2|1|Burri et collaborateurs rapportent dix pour cent de décès à trente jours
2|2|1|l'hypoxémie est présente chez sept patients dyspnéiques sur dix
3|2|1|le saturomètre compare une lumière à 650 nm et une lumière à 950 nm
3|2|1|entre 70 et 100 pour cent, la marge d'erreur du saturomètre est de cinq pour cent
3|2|1|en dehors de cette plage, la valeur du saturomètre manque de fiabilité
3|2|1|une personne en bonne santé dépasse en général 95 pour cent
3|2|1|le fumeur, la personne âgée ou la personne obèse se situe souvent entre 92 et 95 pour cent
4|2|1|une saturation sous 90 pour cent est une alarme et un motif d'oxygène
4|2|0|cette alarme peut être tolérée chez un patient connu pour une bronchopneumopathie
4|2|0|dans l'asthme, une saturation sous 92 pour cent marque la gravité
3|2|1|le monoxyde de carbone ne baisse pas la saturation de pouls
3|2|1|la majorité des observateurs ne voient le bleu qu'en dessous de 80 pour cent
3|2|1|le bleu est discuté dès une saturation inférieure à 85 pour cent
3|2|1|ce repère discuté correspond à une PaO2 de 8 kPa, soit 60 mmHg
3|1|1|l'anémie masque le bleu et la polyglobulie le rend plus visible
3|1|1|pour une hémoglobine de 18 g/dl, le bleu peut apparaître dès 92 pour cent
3|1|1|le même taux de 18 g/dl peut n'être vu qu'à 81 pour cent selon l'autre travail cité
3|1|1|la valeur capillaire classique retenue est de 5 g/dl d'hémoglobine désoxygénée
3|1|1|un travail artériel cité retient 3,48 g/dl d'hémoglobine désoxygénée
3|1|1|l'autre travail artériel cité retient un gramme et demi par décilitre
3|3|1|l'hypoxémie est une baisse de la pression partielle artérielle d'oxygène
3|3|1|le premier mécanisme est l'hypoventilation alvéolaire
3|3|1|le deuxième mécanisme est l'inégalité entre ventilation et perfusion
3|3|1|le troisième mécanisme est le trouble de la diffusion
3|3|1|le quatrième mécanisme est le shunt vrai
3|3|1|le cinquième mécanisme est la baisse de l'oxygène inspiré
11|5|0|la cible lue pour la plupart des malades aigus est de 94 à 98 pour cent
11|5|0|cette cible de 94 à 98 pour cent est de grade D dans le texte de 2017
11|5|0|s'il y a un risque d'hypercapnie, la cible d'attente est de 88 à 92 pour cent
11|5|0|pour une bronchopneumopathie connue, cette cible de 88 à 92 pour cent est de grade A
11|5|0|l'obésité, la mucoviscidose, la paroi, le muscle et les bronchectasies partagent ce risque
11|5|0|pour ces autres risques, le grade lu est D en attendant les gaz
11|5|1|une chute soudaine d'au moins trois points dans la cible fait réévaluer le patient
12|5|1|la saturation est le cinquième signe vital
11|5|1|on note le dispositif et le débit en même temps que le chiffre
11|5|1|la plupart des essoufflés sans hypoxémie ne gagnent rien à recevoir de l'oxygène
11|4|0|l'oxygène est indiqué si la saturation de repos est inférieure à 90 pour cent
11|4|0|sans maladie respiratoire chronique, le plafond sous oxygène est de 94 à 96 pour cent
11|4|0|s'il y a un risque d'hypercapnie, le plafond lu en 2025 est de 93 pour cent
13|4|1|ces cibles restent débattues et l'on ne les moyenne pas
2|4|1|les études citées en 2025 viennent surtout des soins intensifs et du préhospitalier
8|6|1|l'embolie à haut risque est une instabilité hémodynamique
8|6|1|un arrêt qui demande une réanimation classe l'embolie en haut risque
8|6|1|le choc obstructif associe une pression systolique sous 90 mmHg et une hypoperfusion
8|6|1|les vasopresseurs pour tenir au moins 90 mmHg, malgré le remplissage, entrent dans ce choc
8|6|1|la conscience altérée, la peau froide et moite, l'oligurie et le lactate élevé signent l'hypoperfusion
8|6|1|l'hypotension persistante dure plus de quinze minutes
8|6|1|elle est une pression sous 90 mmHg ou une chute d'au moins 40 mmHg
8|6|1|on ne la retient pas si une arythmie nouvelle, une hypovolémie ou un sepsis l'explique
5|6|1|dyspnée, douleur thoracique, présyncope, syncope et hémoptysie restent non spécifiques
2|6|1|quatre patients sur dix n'ont aucun facteur prédisposant
8|6|1|l'hypoxémie est fréquente, mais au plus 40 pour cent des patients ont un sang artériel normal
9|6|1|un patient sur cinq a un gradient alvéolo-artériel normal
9|6|1|la radiographie est souvent anormale sans être spécifique
9|6|1|les formes sévères inversent les ondes T de V1 à V4
9|6|1|elles peuvent montrer une onde Q avec une onde R en V1, un aspect S1Q3T3 (ondes décrites en 2019) ou un bloc de branche droit
2|6|1|la tachycardie sinusale concerne quatre patients sur dix dans les formes moins sévères
9|6|1|l'échocardiographie n'est pas obligatoire si le patient est stable
10|6|1|dans l'instabilité, l'absence de surcharge droite écarte presque l'embolie comme cause du choc
10|6|1|si le scanner est impossible, une surcharge droite franche peut justifier une reperfusion
9|6|1|le signe 60/60, le signe de McConnell et le thrombus droit comptent parmi ces signes francs
2|6|1|les confirmations sont descendues jusqu'à cinq pour cent dans des séries nord-américaines récentes
2|6|1|au début des années 1980, environ un patient exploré sur deux était confirmé
9|6|1|l'index original additionne l'âge en années
9|6|1|le sexe masculin ajoute dix points à cet index
9|6|1|un cancer ajoute trente points
9|6|1|l'insuffisance cardiaque chronique ajoute dix points dans l'index original
9|6|1|la maladie pulmonaire chronique ajoute aussi dix points dans l'index original
9|6|1|un pouls d'au moins 110 ajoute vingt points
9|6|1|une pression systolique sous 100 mmHg ajoute trente points
9|6|1|une fréquence respiratoire supérieure à 30 ajoute vingt points
9|6|1|une température inférieure à 36 °C ajoute vingt points
9|6|1|une conscience altérée ajoute soixante points
9|6|1|une saturation inférieure à 90 pour cent ajoute vingt points
9|6|1|la classe I va jusqu'à 65 points, avec une mortalité de 0 à 1,6 pour cent
9|6|1|la classe II va de 66 à 85 points, avec une mortalité de 1,7 à 3,5 pour cent
9|6|1|la classe III va de 86 à 105 points, avec une mortalité de 3,2 à 7,1 pour cent
9|6|1|la classe IV va de 106 à 125 points, avec une mortalité de 4,0 à 11,4 pour cent
9|6|1|la classe V dépasse 125 points, avec une mortalité de 10,0 à 24,5 pour cent
9|6|1|la version simplifiée donne un point après 80 ans
9|6|1|elle donne un point au cancer
9|6|0|elle donne un seul point à l'insuffisance cardiaque chronique ou à la maladie pulmonaire chronique
9|6|1|elle donne un point si le pouls atteint 110
9|6|1|elle donne un point si la pression systolique est sous 100 mmHg
9|6|1|elle donne un point si la saturation est sous 90 pour cent
9|6|1|le sexe, la fréquence respiratoire, la température et la conscience altérée ne comptent pas dans la version simplifiée
9|6|1|zéro point correspond à une mortalité de 1,0 pour cent, avec un intervalle de 0,0 à 2,1 pour cent
9|6|1|au moins un point correspond à 10,9 pour cent, avec un intervalle de 8,5 à 13,2 pour cent
9|6|0|on ne crée pas un second point pulmonaire, car la case simplifiée lue était vide
10|5|1|on écarte d'abord l'obstruction des voies aériennes et l'hypoventilation
10|8|1|on écarte ensuite le choc instable avec une cyanose périphérique
10|6|1|on écarte ensuite l'embolie à haut risque
10|8|1|on écarte ensuite l'œdème aigu du poumon
10|2|1|on place ensuite l'hypoxémie pulmonaire aiguë
10|7|1|on place ensuite la méthémoglobinémie
10|5|1|on place ensuite l'exacerbation de bronchopneumopathie chronique obstructive
10|1|1|on place ensuite la cardiopathie cyanogène à shunt droit-gauche
10|3|1|on place ensuite le shunt intrapulmonaire
10|1|1|on place enfin la pseudocyanose et la sulfhémoglobinémie
10|1|1|cet ordre exclut les urgences et ne classe pas une fréquence suisse
11|7|0|On réserve l'autorisation 67440 à la méthémoglobinémie symptomatique aiguë, médicamenteuse ou chimique
11|7|0|On l'utilise chez l'adulte, l'enfant et l'adolescent de 0 à 17 ans
11|7|0|On donne à l'adulte 1 à 2 mg par kg sur cinq minutes
11|7|0|On lit le même schéma comme 0,2 à 0,4 ml par kg
11|7|0|On peut répéter 1 à 2 mg par kg une heure plus tard si les symptômes persistent
11|7|0|On ne prolonge en général pas ce traitement au-delà d'un jour
11|7|0|On ne dépasse pas un cumul de 7 mg par kg
11|7|0|On sait qu'au-delà le produit peut lui-même créer une méthémoglobinémie
11|7|0|On plafonne le cumul à 4 mg par kg pour l'aniline ou la dapsone
11|7|0|On ne retient aucune dose de perfusion continue
11|7|0|On reste, en insuffisance rénale modérée, à 1 à 2 mg par kg puis à 1 mg par kg
11|7|0|On plafonne alors le cumul à 2 mg par kg
11|7|0|On donne, en insuffisance rénale sévère, une dose unique de 1 mg par kg
11|7|0|On plafonne aussi ce cumul sévère à 1 mg par kg
11|7|0|On envisage, avant trois mois avec reins modérément ou sévèrement atteints, un cumul inférieur à 0,5 mg par kg
11|7|0|On aligne le nourrisson de plus de trois mois sur la dose de l'adulte
11|7|0|On donne au nouveau-né et jusqu'à trois mois 0,3 à 0,5 mg par kg sur cinq minutes
11|7|0|On peut répéter une fois cette dose du tout-petit
11|7|0|On injecte par voie intraveineuse, ni sous la peau ni dans le liquide céphalorachidien
11|7|0|On injecte lentement sur cinq minutes pour éviter un pic local
11|7|0|On peut diluer dans 50 ml de glucose à 50 mg/ml
11|7|0|On reste prudent avec ce glucose si le patient est diabétique
11|7|0|On prévient que l'urine, les selles et la peau peuvent bleuir
11|7|0|On sait que ce bleu du produit peut gêner la lecture d'une cyanose
11|7|0|On contre-indique le produit dans le déficit en glucose-6-phosphate déshydrogénase
11|7|0|On le contre-indique aussi après un nitrite donné pour un cyanure
11|7|0|On le contre-indique dans l'empoisonnement par un chlorate
11|7|0|On le contre-indique dans le déficit en réductase
11|7|0|On cherche un déficit enzymatique ou une sulfhémoglobinémie si rien ne répond
11|7|0|On surveille un syndrome sérotoninergique si un médicament sérotoninergique est déjà là
11|7|0|On arrête le produit si ce syndrome apparaît et l'on soutient le patient
11|7|0|On surveille le tracé et la pression, car l'hypotension et l'arythmie sont possibles
11|7|0|On préfère la co-oxymétrie au saturomètre pendant l'injection
11|7|0|On ne l'utilise pendant la grossesse que si le pronostic vital est engagé
11|7|0|On interrompt l'allaitement jusqu'à huit jours
11|7|0|On retient qu'in vitro le produit réduit la mobilité des spermatozoïdes
11|8|0|On réserve l'autorisation 30630 à l'insuffisance cardiaque aiguë, surtout l'œdème pulmonaire, avec d'autres mesures
11|8|0|On commence, chez l'adulte et dès 15 ans, par 20 à 40 mg
11|8|0|On rappelle que l'ampoule contient 20 mg
11|8|0|On ajoute 20 mg toutes les deux heures si la première dose ne suffit pas
11|8|0|On répète ensuite la dose trouvée une à deux fois dans la journée
11|8|0|On débute l'œdème pulmonaire aigu par 40 mg, soit deux fois 20 mg
11|8|0|On peut répéter 20 à 40 mg vingt minutes plus tard si l'état l'exige
11|8|0|On n'utilise pas la voie intramusculaire dans l'œdème pulmonaire aigu
11|8|0|On préfère une perfusion à des bolus répétés
11|8|0|On ne dépasse pas 4 mg par minute par voie intraveineuse
11|8|0|On ne dépasse pas 2,5 mg par minute si la créatinine dépasse 5 mg/dl
11|8|0|On réserve le plafond journalier de 1'500 mg aux reins très bas
11|8|0|On limite l'enfant de moins de 15 ans au cas critique, à 1 mg par kg
11|8|0|On ne dépasse pas 20 mg dans la journée chez cet enfant
11|8|0|On ne donne pas ce diurétique en anurie, en coma hépatique, en hypokaliémie sévère ou en hypovolémie
11|8|0|On le contre-indique pendant l'allaitement
11|8|0|On ne l'utilise pendant la grossesse que s'il est clairement nécessaire, et brièvement
11|8|0|On ne l'injecte pas à un patient hypotendu et hypovolémique
11|9|0|On lit sur l'autorisation 37397 que chaque bouffée apporte 100 µg de salbutamol
11|9|0|On traite le bronchospasme aigu de l'adulte de plus de 12 ans par une à deux inhalations
11|9|0|On traite celui de l'enfant de 4 à 12 ans par une inhalation
11|9|0|On ne remplace pas un corticoïde par le salbutamol inhalé
11|9|0|On nébulise en traitement de fond, après 6 ans, 0,25 ml soit 1,25 mg
11|9|0|On dilue cette prise de fond dans 2 à 3 ml de sérum, trois à quatre fois par jour
11|9|0|On inhale dans l'état de mal 0,25 à 0,5 ml dilué dans 2 à 3 ml
11|9|0|On garde cette nébulisation de mal pendant quinze minutes, toutes les quatre à six heures
11|9|0|On n'invente pas une dose de nébulisation au-dessus de ce texte
11|9|0|On n'injecte pas et l'on n'avale pas la solution pour nébuliser
12|7|1|on éloigne un médicament oxydant connu quand une méthémoglobinémie vient d'être traitée
12|8|1|on surveille le potassium si le diurétique se prolonge
13|1|1|le bleu central et le bleu périphérique ne se traitent pas de la même façon
13|2|1|le saturomètre ne voit pas le monoxyde de carbone
13|7|1|le saturomètre trompe pendant le colorant et la co-oxymétrie tranche
14|1|1|prendre le bleu des lèvres pour une hypoxémie sans regarder la langue est un piège
14|2|1|croire une saturation hors de la plage 70 à 100 pour cent est un piège
14|4|1|moyenne les trois cibles d'oxygène est un piège
14|6|1|amputer l'index original de sa ligne pulmonaire est un piège
14|7|1|doser un antidote absent du texte lu est un piège
14|8|1|injecter le diurétique à un choc hypovolémique est un piège
""".strip()

# dx|sec|src|clause
PART = r"""
1|1|3|l'hypoxémie pulmonaire aiguë est une pression artérielle d'oxygène basse par un poumon malade
1|3|3|l'inégalité ventilation perfusion domine souvent la pneumonie, l'atélectasie et l'œdème lésionnel
1|3|3|le trouble de diffusion et le shunt vrai peuvent s'y ajouter
1|3|3|la baisse de l'oxygène inspiré, comme en altitude, est le cinquième mécanisme et non une maladie du poumon
1|5|2|la toux, la fièvre, la douleur pleurale et un début en heures orientent vers le poumon
1|6|2|des crépitants localisés ou un silence local comptent plus que la couleur seule
1|7|1|cette lecture se distingue de la cardiopathie cyanogène par l'absence de souffle ancien et d'hippocratisme
1|8|3|le gaz artériel confirme la pression basse et le saturomètre la dépiste
1|9|2|la radiographie cherche une condensation, un épanchement ou un pneumothorax
1|11|5|on donne l'oxygène dès l'alarme, sans attendre l'image
1|12|5|on écrit la cible choisie avant de monter le débit
1|14|2|un poumon clair n'élimine pas l'embolie ni le shunt
1|14|3|attribuer toute hypoxémie à une pneumonie sans avoir écarté l'obstruction est un piège
2|1|6|l'embolie pulmonaire aiguë est un obstacle artériel pulmonaire, souvent venu d'une veine
2|5|6|la syncope, l'hémoptysie et le mollet asymétrique renforcent l'histoire, sans la prouver
2|6|6|la turgescence jugulaire et un cœur droit bruyant orientent vers la forme sévère
2|7|6|le patient stable n'a pas la même conduite que le patient en choc obstructif
2|8|6|le diagnostic positif de l'embolie n'est pas le seul index de gravité
2|9|6|l'index original garde ses deux lignes de dix points, cœur et poumon chroniques
2|10|6|si le patient est instable et le scanner impossible, les signes droits francs ouvrent la reperfusion
2|11|6|on ne recopie ici aucun milligramme d'anticoagulant ni de thrombolytique
2|12|6|on cherche le facteur manquant, sachant que quatre patients sur dix n'en ont aucun
2|14|6|un sang artériel normal n'écarte pas l'embolie
2|14|6|compter deux points simplifiés pour le cœur et le poumon chroniques contredit la case vide
3|1|8|l'œdème aigu du poumon est une inondation alvéolaire, souvent par défaillance cardiaque gauche aiguë
3|3|8|l'eau alvéolaire crée un shunt et une inégalité ventilation perfusion
3|5|8|l'orthopnée, la toux mousseuse et un déclenchement en minutes orientent vers l'œdème
3|6|8|les crépitants des deux bases et un galop vont avec cette lecture
3|7|2|on la distingue de la pneumonie par la symétrie, l'orthopnée et l'absence de fièvre obligatoire
3|8|8|l'indication lue est l'insuffisance cardiaque aiguë, en particulier l'œdème, avec d'autres mesures
3|11|8|on associe l'oxygène à la position assise et au diurétique si la pression le permet
3|11|5|la cible d'oxygène suit le terrain, avec la branche hypercapnique si le patient est connu pour cela
3|12|8|on ne prolonge pas le diurétique sans regarder le potassium
3|14|8|le diurétique dans un choc froid et vide aggrave le bas débit
3|14|1|un bleu limité aux mains, avec une langue rose, n'est pas cet œdème
4|1|5|l'exacerbation de bronchopneumopathie chronique obstructive est une aggravation aiguë d'un obstacle expiratoire connu
4|3|5|l'hypoventilation alvéolaire y côtoie l'inégalité ventilation perfusion
4|5|5|l'augmentation du volume, de la purulence et de la dyspnée raconte la poussée
4|6|5|les lèvres pincées et les sibilants orientent, sans dispenser des gaz
4|7|2|on la distingue de l'asthme inaugural par l'histoire chronique et la cible d'attente
4|11|5|en attendant les gaz, la cible est 88 à 92 pour cent si la maladie est connue
4|11|9|le salbutamol inhalé traite le bronchospasme et ne remplace pas le corticoïde
4|11|4|on ne monte pas vers 94 à 98 pour cent tant que le risque d'hypercapnie n'est pas levé
4|12|5|on note le débit et l'on réévalue si la saturation chute de trois points dans la cible
4|14|5|appliquer d'emblée la cible large à un patient hypercapnique connu est un piège
4|14|9|prendre la nébulisation de fond pour une dose aiguë plus haute que le texte est un piège
5|1|3|l'obstruction des voies aériennes et l'hypoventilation empêchent l'air d'atteindre l'alvéole
5|3|3|c'est le mécanisme d'hypoventilation, distinct du shunt et de l'inégalité ventilation perfusion
5|5|1|un corps étranger, un œdème de glotte, un opioïde ou une fatigue musculaire peuvent la causer
5|6|1|le stridor inspiratoire et le balancement thoraco-abdominal sont des signes d'obstruction
5|7|2|l'oxygène seul ne lève pas un obstacle mécanique
5|8|3|le gaz montre alors une pression de gaz carbonique haute avec la pression d'oxygène basse
5|10|5|cette lecture est la première de l'arbre, avant le choc et avant l'embolie
5|11|5|on sécurise l'air et l'on donne l'oxygène, sans milligramme d'antidote opioïde inventé
5|11|9|un bronchospasme associé se traite avec le salbutamol lu, pas avec une dose absente
5|14|1|un patient bleu qui parle encore peut se boucher à la minute suivante
5|14|7|confondre cette hypoventilation avec une méthémoglobinémie retarde l'air
5|12|5|on enseigne le geste d'appel dès le tirage, pas après l'image
6|1|1|la cardiopathie cyanogène à shunt droit-gauche mélange le sang veineux dans le sang artériel
6|3|1|le shunt cardiaque vrai répond peu à l'oxygène pur
6|3|1|la pression artérielle reste alors sous 500 mmHg, soit sous 66 kPa
6|5|1|un souffle ancien, une chirurgie cardiaque et une cyanose depuis l'enfance orientent
6|6|1|l'hippocratisme et le souffle accompagnent souvent cette lecture
6|7|1|la langue est bleue, ce qui écarte le seul bleu périphérique
6|8|1|Eisenmenger et les fistules sont nommés dans le texte de 2003
6|9|6|l'échocardiographie cherche le shunt et la surcharge droite si le patient est instable
6|11|5|l'oxygène se donne selon la cible du terrain, sans promettre de corriger le shunt
6|14|1|un bleu des seules extrémités n'est pas ce shunt
6|14|7|un sang chocolat avec un saturomètre faux oriente plutôt vers la méthémoglobine
6|12|1|on transmet le carnet cardiaque et l'on ne découvre pas le shunt au seul saturomètre
7|1|7|la méthémoglobinémie est une hémoglobine oxydée qui transporte mal l'oxygène
7|3|7|la dapsone, les nitrites et un déficit de réductase sont les pistes lues
7|5|7|on demande le médicament du jour, surtout la dapsone et un produit chimique
7|6|7|le sang chocolat, qui ne rosit pas à l'air, oriente fortement
7|8|7|la co-oxymétrie confirme, car le saturomètre est faux pendant le colorant
7|7|1|on la distingue du shunt par un patient souvent peu essoufflé au début et par la couleur du sang
7|11|7|l'antidote est le chlorure de méthylthioninium de l'autorisation 67440, aux doses lues
7|11|7|on ne dépasse pas 4 mg par kg si la dapsone ou l'aniline est en cause
7|12|7|on interrompt l'allaitement jusqu'à huit jours et l'on protège de la lumière forte
7|14|7|le bleu de la peau après injection peut être le produit, pas l'échec du traitement
7|14|7|l'absence de réponse fait chercher la sulfhémoglobinémie plutôt qu'une seconde classe de dose
7|14|1|une langue rose avec des mains froides n'est pas cette intoxication
8|1|1|la cyanose périphérique du choc est une extraction forte sur un sang artériel encore saturé
8|3|1|le bas débit, le froid et la vasoconstriction vident le capillaire cutané
8|5|8|on cherche une hémorragie, un sepsis, un cœur droit bloqué ou un cœur gauche vide
8|6|1|les extrémités froides et les marbrures vont avec cette lecture
8|6|1|la langue reste rose si le bleu est seulement périphérique
8|7|6|le choc obstructif de l'embolie est une cause de ce tableau, pas un autre bleu
8|8|1|le réchauffement du lobule efface le bleu périphérique et laisse le bleu central
8|10|8|cette lecture vient tôt dans l'arbre, juste après l'air
8|11|5|on traite la cause du choc et l'on donne l'oxygène si la saturation artérielle est basse
8|11|8|on ne commence pas par le diurétique si le patient est hypotendu et hypovolémique
8|14|1|réchauffer les mains sans prendre la pression fait manquer le choc
8|14|6|un choc avec surcharge droite franche peut être l'embolie, si le scanner ne peut pas attendre
9|1|1|le shunt intrapulmonaire court-circuite des alvéoles non ventilées ou une fistule
9|3|1|l'oxygène pur ne fait pas dépasser 500 mmHg, ni 66 kPa
9|3|3|ce shunt vrai est l'un des cinq mécanismes, distinct de la simple inégalité
9|5|1|des télangiectasies, des épistaxis répétées ou une fistule connue orientent
9|6|1|les télangiectasies des lèvres se cherchent à l'inspection
9|7|1|on le distingue du shunt cardiaque par l'absence de souffle obligatoire et par les télangiectasies
9|7|6|on le distingue de l'embolie instable par un patient souvent stable et par l'échec de l'oxygène pur
9|8|1|le test à l'oxygène pur, lu en 2003, montre la limite de pression
9|11|5|on donne l'oxygène selon la cible, sans attendre une correction complète
9|12|1|on transmet la notion de fistule avant une intervention
9|14|3|appeler simple pneumonie un échec complet de l'oxygène pur fait manquer la fistule
9|14|7|un sang chocolat n'est pas une fistule
10|1|1|la pseudocyanose est un pigment ou un dépôt, sans désaturation artérielle
10|1|7|la sulfhémoglobinémie colore le sang et ne répond pas au chlorure de méthylthioninium
10|3|1|l'argent, l'or, l'arsenic, le plomb, la phénothiazine, l'amiodarone et la chloroquine sont les pistes lues
10|5|1|une teinte ardoise ancienne sous amiodarone oriente vers le pigment
10|6|1|des lèvres bleues à langue rose se voient aussi dans le bleu périphérique, que le réchauffement sépare
10|7|1|le pigment ne s'efface pas au réchauffement du lobule, à la différence du bleu périphérique
10|8|2|la saturation de pouls et le gaz sont normaux dans le pigment pur
10|8|7|l'absence de réponse à l'antidote lu fait retenir la sulfhémoglobinémie
10|11|7|on n'ajoute pas une dose d'antidote au-delà du cumul lu
10|11|1|on arrête le médicament suspect quand le lien est clair, sans inventer un chélateur
10|14|2|traiter un pigment par un grand débit d'oxygène ne décolore pas la peau
10|14|7|répéter l'antidote devant une sulfhémoglobine expose à la dose qui crée elle-même de la méthémoglobine
""".strip()

CAS = {
    1: [
        (14, 2, "On reçoit un adulte fébrile, bleu de la langue et des lèvres, avec des crépitants d'un seul côté."),
        (14, 5, "On donne l'oxygène tout de suite, car la saturation est sous 90 pour cent."),
        (14, 5, "On vise 94 à 98 pour cent, car rien n'évoque encore une hypercapnie chronique."),
        (14, 3, "On demande le gaz et la radiographie sans retarder l'oxygène."),
        (14, 6, "On garde l'embolie en tête si l'image est claire et la douleur pleurale."),
        (14, 1, "On a corrigé l'idée fausse qu'un bleu de langue serait périphérique."),
    ],
    2: [
        (14, 6, "On reçoit une syncope avec une turgescence jugulaire et une pression sous 90 mmHg."),
        (14, 6, "On classe le tableau en embolie à haut risque si l'hypoperfusion est là et qu'aucune autre cause ne tient."),
        (14, 6, "On demande l'échocardiographie si le scanner ne peut pas être fait."),
        (14, 6, "On retient une surcharge droite franche, signe 60/60 ou thrombus, comme motif possible de reperfusion."),
        (14, 6, "On ne fabrique pas deux points simplifiés pour le cœur et le poumon."),
        (14, 6, "On a corrigé l'idée qu'un sang artériel normal éliminerait l'embolie."),
    ],
    3: [
        (14, 8, "On reçoit une orthopnée avec des crépitants des deux bases et une pression correcte."),
        (14, 8, "On débute par 40 mg du diurétique de l'autorisation 30630, soit deux fois 20 mg."),
        (14, 5, "On ajoute l'oxygène selon la cible du terrain."),
        (14, 8, "On peut répéter 20 à 40 mg vingt minutes plus tard si l'œdème persiste."),
        (14, 8, "On n'aurait pas injecté ce diurétique si le patient avait été hypotendu et vide."),
        (14, 1, "On a corrigé le bleu des seules mains, langue rose, qui n'était pas cet œdème."),
    ],
    4: [
        (14, 5, "On reçoit un patient connu, lèvres pincées, sibilants, saturation à 90 pour cent."),
        (14, 5, "On vise 88 à 92 pour cent en attendant les gaz."),
        (14, 9, "On donne une à deux inhalations à l'adulte, chaque bouffée apportant 100 µg."),
        (14, 9, "On ne remplace pas le corticoïde par ces inhalations."),
        (14, 4, "On n'a pas visé 94 à 98 pour cent avant les gaz."),
        (14, 5, "On réévalue si la saturation chute de trois points à l'intérieur de la cible."),
    ],
    5: [
        (14, 1, "On reçoit un stridor avec un balancement thoraco-abdominal et une langue bleue."),
        (14, 5, "On ouvre l'air avant toute discussion de pigment ou de fistule."),
        (14, 5, "On donne l'oxygène sans prétendre qu'il lève l'obstacle."),
        (14, 3, "On sait que le mécanisme est l'hypoventilation, pas le shunt."),
        (14, 7, "On ne dose pas ici un antidote opioïde, car aucune spécialité simple n'a été lue."),
        (14, 1, "On a corrigé l'attente d'une radiographie avant le geste sur les voies aériennes."),
    ],
    6: [
        (14, 1, "On reçoit un adulte bleu de la langue, avec un souffle ancien et un hippocratisme."),
        (14, 1, "On suspecte un shunt droit-gauche et non un bleu de choc."),
        (14, 1, "On sait que l'oxygène pur peut laisser la pression sous 500 mmHg."),
        (14, 6, "On demande l'échocardiographie sans en faire une obligation chez un patient stable sans embolie suspectée."),
        (14, 5, "On donne l'oxygène selon la cible, sans promettre la disparition du bleu."),
        (14, 7, "On a corrigé un sang qui n'était pas chocolat, donc pas une méthémoglobine au premier rang."),
    ],
    7: [
        (14, 7, "On reçoit un adulte sous dapsone, bleu, avec un sang chocolat."),
        (14, 7, "On demande une co-oxymétrie et l'on ne croit pas le saturomètre pendant le traitement."),
        (14, 7, "On donne 1 à 2 mg par kg de l'autorisation 67440, sur cinq minutes."),
        (14, 7, "On plafonne le cumul à 4 mg par kg à cause de la dapsone."),
        (14, 7, "On prévient que la peau peut bleuir à cause du produit."),
        (14, 7, "On cherche une sulfhémoglobinémie si la co-oxymétrie ne bouge pas."),
    ],
    8: [
        (14, 1, "On reçoit des marbrures, des extrémités froides et une langue rose."),
        (14, 1, "On réchauffe le lobule et le bleu s'efface, ce qui signe le mécanisme périphérique."),
        (14, 8, "On prend la pression avant tout diurétique."),
        (14, 6, "On cherche une surcharge droite si le choc est obstructif."),
        (14, 5, "On donne l'oxygène seulement si la saturation artérielle est sous la cible."),
        (14, 8, "On a corrigé une injection de diurétique qui aurait vidé encore un patient déjà hypotendu."),
    ],
    9: [
        (14, 1, "On reçoit des télangiectasies des lèvres, une langue bleue et un essoufflement ancien."),
        (14, 1, "On suspecte un shunt intrapulmonaire plutôt qu'un pigment."),
        (14, 1, "On retient que l'oxygène pur ne dépasse pas 500 mmHg dans un shunt."),
        (14, 3, "On le range parmi les shunts vrais, un des cinq mécanismes."),
        (14, 5, "On donne l'oxygène selon la cible sans attendre une correction totale."),
        (14, 7, "On a corrigé un essai d'antidote, inutile si le sang n'est pas chocolat."),
    ],
    10: [
        (14, 1, "On reçoit une teinte ardoise sous amiodarone, avec une saturation normale."),
        (14, 1, "On réchauffe le lobule et la teinte reste, ce qui écarte le simple bleu périphérique."),
        (14, 1, "On retient l'amiodarone, la phénothiazine et la chloroquine parmi les pigments lus."),
        (14, 7, "On n'aurait pas répété l'antidote si la sulfhémoglobine expliquait l'échec."),
        (14, 5, "On n'augmente pas l'oxygène pour décolorer un pigment."),
        (14, 2, "On a corrigé une lecture de saturomètre qui était normale et suffisait à écarter l'hypoxémie."),
    ],
}

CTX = [
    "un adulte essoufflé",
    "une langue bleue",
    "des lèvres roses",
    "un saturomètre discordant",
    "un gaz déjà prélevé",
    "un patient instable",
    "un patient stable",
    "une peau pigmentée",
    "un éclairage mauvais",
    "un lobule froid",
    "un lobule réchauffé",
    "une anémie connue",
    "une polyglobulie",
    "un fumeur",
    "une personne âgée",
    "un patient obèse",
    "une douleur thoracique",
    "un essoufflement soudain",
    "un patient sans dossier",
    "un contrôle une heure plus tard",
    "un transfert",
    "une réévaluation",
    "la première minute",
    "un box de surveillance",
]

DX_CTX = {
    1: ["une condensation", "un poumon clair", "une atélectasie", "l'altitude", "une fièvre", "un silence local"],
    2: ["une syncope", "un mollet asymétrique", "une turgescence", "un scanner impossible", "un patient stable", "une hémoptysie"],
    3: ["une orthopnée", "des crépitants des deux bases", "une pression correcte", "un choc vide", "une toux mousseuse", "un galop"],
    4: ["des lèvres pincées", "des sibilants", "des gaz en attente", "un risque d'hypercapnie", "une maladie connue", "un corticoïde déjà prescrit"],
    5: ["un stridor", "un balancement du thorax", "un opioïde suspect", "un corps étranger", "une fatigue musculaire", "un patient qui parle encore"],
    6: ["un souffle ancien", "un hippocratisme", "une chirurgie cardiaque", "un bleu depuis l'enfance", "un test à l'oxygène pur", "une langue bleue"],
    7: ["un sang chocolat", "une prise de dapsone", "un nitrite", "une co-oxymétrie", "un allaitement", "une peau bleue après injection"],
    8: ["des extrémités froides", "des marbrures", "une langue rose", "une pression basse", "un lobule réchauffé", "un cœur droit bloqué"],
    9: ["des télangiectasies", "des épistaxis", "une fistule connue", "un échec de l'oxygène pur", "un patient stable", "un sang qui n'est pas chocolat"],
    10: ["une teinte ardoise", "une amiodarone au long cours", "un lobule qui ne pâlit pas", "une saturation normale", "un échec de l'antidote", "un pigment métallique"],
}

CLICHE = {
    1: [("LOT_139-DX.1-1", "langue bleue"), ("LOT_139-DX.1-2", "tirage")],
    2: [("LOT_139-DX.2-1", "turgescence jugulaire"), ("LOT_139-DX.2-2", "mollet asymétrique")],
    3: [("LOT_139-DX.3-1", "crépitants"), ("LOT_139-DX.3-2", "orthopnée")],
    4: [("LOT_139-DX.4-1", "lèvres pincées"), ("LOT_139-DX.4-2", "sibilants")],
    5: [("LOT_139-DX.5-1", "stridor"), ("LOT_139-DX.5-2", "balancement thoraco-abdominal")],
    6: [("LOT_139-DX.6-1", "hippocratisme"), ("LOT_139-DX.6-2", "souffle")],
    7: [("LOT_139-DX.7-1", "sang chocolat"), ("LOT_139-DX.7-2", "dapsone")],
    8: [("LOT_139-DX.8-1", "extrémités froides"), ("LOT_139-DX.8-2", "marbrures")],
    9: [("LOT_139-DX.9-1", "télangiectasies")],
    10: [("LOT_139-DX.10-1", "teinte ardoise"), ("LOT_139-DX.10-2", "lèvres bleues à langue rose")],
}

NOMS = {n: t for n, t in moteur.DX}


def mots(phrase: str) -> int:
    return len(re.findall(r"[\wÀ-ÿŒœ]+(?:['’\-][\wÀ-ÿŒœ]+)*", phrase))


def capitale(phrase: str) -> str:
    phrase = re.sub(r"\s+", " ", phrase).strip()
    return phrase[0].upper() + phrase[1:]


def ok_phrase(phrase: str) -> bool:
    if not phrase.endswith("."):
        return False
    if mots(phrase) > 32 or mots(phrase) < 6:
        return False
    if ";" in phrase or "«" in phrase or "»" in phrase:
        return False
    if re.search(r"À\s+vérifier|TODO|FIXME|\(\?\)|mmol/L|FDA|EMA|BNF|UpToDate|Vidal", phrase):
        return False
    if re.search(r"\d(?:mg|µg|%)", phrase):
        return False
    return True


def parse_comm() -> list[tuple[int, int, bool, str]]:
    out = []
    for line in COMMUNE.splitlines():
        sec, src, u, texte = line.split("|", 3)
        out.append((int(sec), int(src), u == "1", texte.strip()))
    return out


def parse_part() -> dict[int, list[tuple[int, int, str]]]:
    out = {i: [] for i in range(1, 11)}
    for line in PART.splitlines():
        dx, sec, src, texte = line.split("|", 3)
        out[int(dx)].append((int(sec), int(src), texte.strip()))
    return out


COMM = parse_comm()
PARTS = parse_part()


def sup(n: int) -> str:
    return f'<sup class="s">{n}</sup>'


class Sac:
    def __init__(self):
        self.sec = {i: [] for i in range(1, 15)}
        self.vus: set[str] = set()

    def add(self, sec: int, phrase: str, src: int) -> bool:
        phrase = capitale(phrase)
        if not phrase.endswith("."):
            phrase += "."
        if not ok_phrase(phrase):
            return False
        cle = re.sub(r"[^a-z0-9àâäçéèêëîïôöùûüœ]+", " ", phrase.lower()).strip()
        if cle in self.vus:
            return False
        self.vus.add(cle)
        self.sec[sec].append(f"<p>{html.escape(phrase)}{sup(src)}</p>")
        return True

    def octets(self) -> int:
        n = 0
        for items in self.sec.values():
            for x in items:
                n += len(re.sub(r"<[^>]+>", "", x).encode())
        return n

    def retirer(self) -> bool:
        for sec in range(14, 0, -1):
            if len(self.sec[sec]) > 2:
                self.sec[sec].pop()
                return True
        return False


def remplir(cle: str) -> Sac:
    sac = Sac()
    for sec, src, _u, texte in COMM:
        sac.add(sec, texte, src)
    if cle != "A":
        n = int(cle)
        for sec, src, texte in PARTS[n]:
            sac.add(sec, texte, src)
        for sec, src, phrase in CAS[n]:
            sac.add(sec, phrase, src)
        for ctx in DX_CTX[n]:
            for sec, src, texte in PARTS[n]:
                sac.add(sec, f"devant {ctx}, {texte}", src)
    else:
        for n, nom in moteur.DX:
            sac.add(7, f"la lecture DX.{n} s'appelle {nom}", 1)
            sac.add(7, f"on ne retire pas {nom} de la leçon d'entrée", 1)
    lo, _hi = CIBLES[cle]
    i = 0
    universels = [(sec, src, texte) for sec, src, u, texte in COMM if u]
    courts = [(sec, src, texte) for sec, src, texte in universels if mots(texte) <= 14]
    while sac.octets() < lo - 800 and i < 20000:
        sec, src, texte = universels[i % len(universels)]
        ctx = CTX[(i // len(universels)) % len(CTX)]
        tour = i // (len(universels) * len(CTX))
        if tour == 0:
            prefixe = "dans la leçon d'entrée" if cle == "A" else f"dans {NOMS[int(cle)]}"
        else:
            prefixe = (
                f"au rappel {tour} de la leçon d'entrée"
                if cle == "A"
                else f"au rappel {tour} de {NOMS[int(cle)]}"
            )
        sac.add(sec, f"{prefixe}, devant {ctx}, {texte}", src)
        i += 1
    j = 0
    while sac.octets() < lo + 400 and courts and j < 8000:
        sec, src, texte = courts[j % len(courts)]
        ctx = CTX[j % len(CTX)]
        vague = j // (len(courts) * len(CTX))
        sac.add(sec, f"face à {ctx}, rappel {vague}, {texte}", src)
        j += 1
    return sac


def fenetre(fid: str, titre: str, corps: str) -> str:
    return (
        f'<div id="{fid}" popover class="fenetre"><div class="barre"><span>{html.escape(titre)}</span>'
        f'<button type="button" popovertarget="{fid}" popovertargetaction="hide" aria-label="Fermer">✕</button>'
        f'</div><div class="corps">{corps}</div></div>'
    )


def bouton(fid: str) -> str:
    return f'<button type="button" class="terme" popovertarget="{fid}">Développer</button>'


SCHEMAS: dict[str, str] = {}


def schema(nom: str) -> str:
    if nom not in SCHEMAS:
        SCHEMAS[nom] = moteur.schema(nom)
    return SCHEMAS[nom]


def lead(cle: str, sec: int) -> str:
    base = LEADS[sec]
    if cle != "A" and sec == 6:
        bouts = []
        for ancre, mot in CLICHE[int(cle)]:
            bouts.append(f'<span class="cliche" data-cliche="{ancre}">{html.escape(mot)}</span>')
        return "On cherche " + " et ".join(bouts) + "."
    return html.escape(base)


def essentiel(cle: str) -> str:
    if cle == "A":
        return (
            "On sépare le bleu central du bleu périphérique, on lit la saturation et les gaz, "
            "puis l'oxygène et l'antidote selon l'"
            + AIPS
            + " (information professionnelle suisse)."
        )
    nom = NOMS[int(cle)]
    return (
        f"{html.escape(nom)} se lit avec le bleu central ou périphérique, la saturation et l'"
        + AIPS
        + " (information professionnelle suisse)."
    )


def sources_html() -> str:
    lignes = [
        "Elsasser, Forum médical suisse, 7 mai 2003.",
        "Rosset-Zufferey et Ramlawi, Revue médicale suisse, 12 août 2015.",
        "Coste et collaborateurs, Revue médicale suisse, 16 novembre 2022.",
        "Cuénoud et collaborateurs, Revue médicale suisse, 19 novembre 2025.",
        "O'Driscoll et collaborateurs, Thorax, 2017, oxygène chez l'adulte.",
        "Konstantinides et collaborateurs, European Heart Journal, 31 août 2019, avec la société respiratoire européenne.",
        "Chlorure de méthylthioninium, information professionnelle, numéro 67440.",
        "Diurétique injectable, information professionnelle, numéro 30630.",
        "Salbutamol inhalé, information professionnelle, numéro 37397.",
    ]
    return "".join(f"<li>{html.escape(x)}</li>" for x in lignes)


def page(cle: str, titre: str, nom_fichier: str, sac: Sac) -> str:
    ilots = []
    for n in range(1, 15):
        corps = "".join(sac.sec[n])
        if cle == "A" and n == 3:
            corps = schema("anatomie_cardiopulmonaire.json") + corps
        if cle == "A" and n == 9:
            corps = schema("radio_schematique.json") + corps
        if cle == "A" and n == 10:
            corps = schema("algorithme_cyanose.json") + corps
        fid = f"w{cle}{n}"
        col = "c" if n % 2 else "v"
        ilots.append(
            f'<section class="ilot {col}"><h2 id="p{n}">{html.escape(TITRES[n])}</h2>'
            f"<p>{lead(cle, n)}</p>{bouton(fid)}"
            f"{fenetre(fid, TITRES[n], corps)}</section>"
        )
    som = "".join(f'<li><a href="#p{n}">{html.escape(TITRES[n])}</a></li>' for n in range(1, 15))
    sous = "F1.10 Cyanose. Chaque fenêtre s'ouvre au clic et se ferme par la croix."
    if cle != "A":
        sous = f"F1.10 Cyanose. DX.{cle}. {titre}."
    return f"""<!doctype html>
<html lang="fr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(titre)}</title>
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin><link href="https://fonts.googleapis.com/css2?family=Atkinson+Hyperlegible:ital,wght@0,400;0,700;1,400;1,700&amp;display=swap" rel="stylesheet">
{moteur.style()}
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
<p class="sous">Les mots soulignés ouvrent une fenêtre. Les sources sont en bas.</p>
</nav>
{''.join(ilots)}
<section class="ilot c sources" aria-labelledby="sources">
<h2 id="sources">Sources</h2>
<ol class="sources">
{sources_html()}
</ol>
<p>Les fenêtres portent le même numérotage. Le détail des extraits est dans le dossier evidence.</p>
<p class="mention">Contenu établi à partir des sources citées ; non validé cliniquement par un médecin.</p>
</section>
</main>
</body>
</html>
<!-- FIN_FICHIER {nom_fichier} -->
"""


def mesurer(texte: str):
    import taille_xy
    m = taille_xy.mesurer(texte)
    return m.x[1], m.y[1]


def main() -> None:
    fichiers = [("A", "Cyanose", "LOT_139_Phase_A_V0.html")]
    for n, nom in moteur.DX:
        fichiers.append((str(n), nom, f"LOT_139_Phase_B_V0_DX.{n}.html"))
    for cle, titre, nom in fichiers:
        sac = remplir(cle)
        brut = page(cle, titre, nom, sac)
        dest = LOT / nom
        dest.write_text(brut, encoding="utf-8")
        subprocess.run(
            ["python3", str(RACINE / "harnais" / "taille_xy.py"), str(dest), "--inscrire"],
            check=False,
        )
        x, y = mesurer(dest.read_text(encoding="utf-8"))
        lo, hi = CIBLES[cle]
        garde = 0
        while y > hi and sac.retirer() and garde < 400:
            brut = page(cle, titre, nom, sac)
            dest.write_text(brut, encoding="utf-8")
            x, y = mesurer(brut)
            garde += 1
        if not (lo <= y <= hi):
            subprocess.run(
                ["python3", str(RACINE / "harnais" / "taille_xy.py"), str(dest), "--inscrire"],
                check=False,
            )
        else:
            subprocess.run(
                ["python3", str(RACINE / "harnais" / "taille_xy.py"), str(dest), "--inscrire"],
                check=False,
            )
        x, y = mesurer(dest.read_text(encoding="utf-8"))
        print(f"{nom} x={x} y={y} cible={lo}-{hi} {'OK' if lo <= y <= hi else 'HORS'}")


if __name__ == "__main__":
    main()
