"""Fenêtres supplémentaires de la Phase A : calculs, profils et conduite."""
from moteur import A, P, S, W, table

ALAT = A("alanine aminotransférase", "ALAT")
ASAT = A("aspartate aminotransférase", "ASAT")
PAL = A("phosphatase alcaline", "PAL")
GGT = A("gamma-glutamyltransférase", "GGT")
LSN = A("limite supérieure de la normale", "LSN")
INR = A("international normalized ratio", "INR")
FIB = A("fibrosis-4 index", "FIB")
MELD = A("model for end-stage liver disease", "MELD")

def bloc_profils():
    return W("w-profils", "Quatre profils chiffrés, même laboratoire", "\n".join([
        P(f"Le laboratoire de l'exemple a pour {LSN} 40 U/l d'{ALAT}, 40 U/l d'{ASAT}, 120 U/l de {PAL}. Ces bornes sont celles de l'exemple, pas une norme suisse unique.", 2),
        P(f"<b>Profil hépatocellulaire.</b> {ALAT} 800 U/l, {ASAT} 600 U/l, {PAL} 130 U/l. "
          f"{ALAT} vaut 20 fois la {LSN}, {PAL} vaut 1,08 fois la {LSN}. R égale 20 divisé par 1,08, soit environ 18. R est au-dessus de 5 : classe hépatocellulaire. "
          f"On cherche alors le paracétamol, le virus, l'ischémie, le médicament et l'auto-immunité.", 2),
        P(f"<b>Profil cholestatique.</b> {ALAT} 80 U/l (deux fois la {LSN}), {PAL} 600 U/l (cinq fois la {LSN}). R égale 2 divisé par 5, soit 0,4. R est en dessous de 2 : classe cholestatique. "
          f"L'échographie cherche une dilatation. Sans dilatation, on pense à la cholangite biliaire primitive, au médicament et à la stéatose avec inflammation.", 2),
        P(f"<b>Profil mixte.</b> {ALAT} 240 U/l (six fois la {LSN}), {PAL} 360 U/l (trois fois la {LSN}). R égale 6 divisé par 3, soit 2. "
          f"La recommandation dit cholestatique quand le rapport est de 2 ou moins, et mixte quand il est entre 2 et 5. "
          f"Un R exactement égal à 2 se range donc avec la cholestase. Un R à 2,1 serait mixte. La frontière se respecte.", 2),
        P(f"<b>Muscle, pas foie.</b> {ASAT} 400 U/l, {ALAT} 70 U/l, {PAL} normale, créatine kinase à plusieurs milliers. "
          f"Le rapport de De Ritis est haut, mais l'{ALAT} modeste et la kinase élevée sortent le patient de l'hépatite alcoolique. On ne calcule pas un Maddrey.", 4),
        P(f"<b>Alcool.</b> {ASAT} 180 U/l, {ALAT} 70 U/l, soit un rapport d'environ 2,6, au-dessus de la zone 1,5 à 2 lue pour l'hépatite alcoolique, "
          f"et une {ASAT} encore sous 300 U/l. La {GGT} est souvent haute. L'ictère et les neutrophiles décident si l'on calcule le Maddrey.", 4),
    ]))

def bloc_cas():
    return W("w-cas", "Cas ambulatoire : du chiffre au FIB-4", "\n".join([
        P(f"Une femme de 58 ans, diabétique, a une {ALAT} à 48 U/l, une {ASAT} à 62 U/l, des plaquettes à 160 milliards par litre, une {PAL} normale. "
          f"R n'est pas cholestatique. Le terrain est celui de la stéatose métabolique. On calcule le {FIB}-4 avant d'empiler les sérologies, sans oublier le médicament et l'alcool.", 5),
        P(f"Racine carrée de 48 : environ 6,9. Plaquettes fois cette racine : 160 fois 6,9, soit environ 1 110. "
          f"Âge fois {ASAT} : 58 fois 62, soit 3 596. {FIB}-4 environ 3,2. C'est au-dessus de 2,67 : la recommandation de 2024 envoie vers l'élastographie, pas vers un contrôle dans trois ans.", 5),
        P(f"Le même calcul à 32 ans est peu fiable : la recommandation dit que le {FIB}-4 marche mal avant 35 ans. "
          f"À 70 ans, le seuil bas qui déclenche la suite n'est plus 1,3 mais 2,0. Les trois âges ne se confondent pas.", 5),
        P("Ce cas est un exercice de calcul. Il n'est pas une série publiée. Les seuils, eux, viennent de la recommandation.", 5),
    ])) + W("w-child-ex", "Cas de cirrhose : Child-Pugh puis MELD", "\n".join([
        P("Un homme avec une cirrhose connue a une bilirubine à 40 µmol/l (2 points), une albumine à 3,0 g/dl (2 points), un INR à 1,9 (2 points), une ascite légère contrôlée par le diurétique (2 points) et pas d'encéphalopathie (1 point).", 9),
        P("Total : 9 points. La classe B couvre 7, 8 et 9. La classe A se serait arrêtée à 6, la classe C commence à 10. On nomme B, et l'on garde en tête que A et C existent.", 9),
        P(f"Le {MELD} se calcule à part, en mg/dl. Une créatinine de 1,2 mg/dl, une bilirubine de 2,3 mg/dl (proche de 40 µmol/l) et un INR de 1,9 ne donnent pas un Child-Pugh. "
          f"On applique 9,57 ln(1,2) + 3,78 ln(2,3) + 11,2 ln(1,9) + 6,43. "
          f"ln(1,2) vaut environ 0,18, ln(2,3) environ 0,83, ln(1,9) environ 0,64. "
          f"Le calcul dérivé donne environ 1,7 + 3,1 + 7,2 + 6,4, soit autour de 18. Ce n'est pas un pronostic publié, c'est l'application de la formule de 2010.", 8),
        P(f"Si le sodium est à 128 mmol/l, il est dans la borne 125 à 140. Le {MELD}-Na réécrit le score avec la formule lue. "
          f"Un sodium à 122 mmol/l se remplace par 125, et un sodium à 142 par 140. On ne laisse pas le sodium sortir de la borne.", 8),
    ]))

def bloc_heure():
    return W("w-heure", "Première heure d'une enzyme très élevée", "\n".join([
        P("Minute 0. Constantes, glycémie capillaire, conscience. Une hypoglycémie se corrige tout de suite. L'heure de la dernière prise de paracétamol se demande à la personne et à l'entourage."),
        P(f"Minute 10. Prélèvements : enzymes, bilirubine fractionnée, {INR}, numération, créatinine, gaz du sang si la vigilance baisse, paracétamolémie, hémocultures si fièvre. Le prélèvement ne retarde pas l'antidote quand l'histoire est claire."),
        P("Minute 20. Nomogramme si la prise a plus de 4 heures et que l'heure est sûre. Ligne de 1975 à 200 µg/ml, ligne de 1981 à 150 µg/ml. Au-dessus de la ligne de traitement : Prescott.", 10, 11),
        P("Minute 30. Échographie si douleur, fièvre ou profil cholestatique. Voie dilatée et sepsis : drainage, pas un bilan auto-immun.", 2),
        P(f"Heure 2. Si l'{INR} s'allonge et que la conscience baisse, on relit King's College et Clichy, et l'on appelle le centre qui transplante. "
          f"Le Child-Pugh attendra que l'on sache s'il existe une cirrhose.", 3, 9),
        P("Ce déroulement est une conduite d'enseignement. Il n'invente pas un délai suisse officiel absent des textes lus. Il empêche seulement d'attendre le lendemain pour un antidote ou un drainage."),
    ]))

def bloc_med():
    return W("w-medic", "Médicaments : chronologie avant le score", "\n".join([
        P("On écrit la date de début, la date d'arrêt, la dose et l'indication. Un antibiotique arrêté depuis dix jours peut encore être le coupable : le score regarde le délai, il ne se contente pas de la boîte du jour.", 2),
        P("Les plantes, les compléments et les produits achetés en ligne comptent comme des expositions. La recommandation de 2019 les place dans le même raisonnement que les médicaments à autorisation.", 2),
        P("On n'additionne pas deux suspects sans les noter séparément. Le domaine « autres médicaments » du score retire des points quand un autre produit hépatotoxique est présent. Oublier ce domaine gonfle le total.", 2),
        P("La réintroduction volontaire pour « voir » n'est pas un geste de cabinet. Le domaine de réintroduction du score décrit ce qui a déjà été observé, il ne prescrit pas un test dangereux.", 2),
    ]))

def bloc_dxnoms():
    rows = [
        ["DX.1", "Stéatose hépatique liée à un dysfonctionnement métabolique", "La plus fréquente des maladies chroniques du foie dans le texte de 2024. Fibrose triée par le FIB-4."],
        ["DX.2", "Hépatite alcoolique", "Ictère récent, rapport ASAT/ALAT souvent au-dessus de 1,5 à 2, Maddrey à 32, Glasgow, Lille."],
        ["DX.3", "Hépatite virale", "A, E, B et C selon la durée. L'aigu se distingue du portage."],
        ["DX.4", "Lésion hépatique médicamenteuse et intoxication au paracétamol", "R, RUCAM, loi de Hy, nomogramme et Prescott. Les deux mécanismes ne se traitent pas de la même façon."],
        ["DX.5", "Obstacle biliaire extra-hépatique", "R au plus égal à 2 et dilatation. L'infection change l'heure du drainage."],
        ["DX.6", "Hépatite auto-immune", "Score simplifié : probable dès 6, certaine dès 7. Quatre domaines."],
        ["DX.7", "Cholangite biliaire primitive", "Femme, prurit, phosphatase, anticorps antimitochondries, acide ursodésoxycholique selon l'information 60812."],
        ["DX.8", "Hémochromatose héréditaire", "Saturation et ferritine, puis homozygotie p.Cys282Tyr. Saignées selon les cibles de 2022."],
        ["DX.9", "Maladie de Wilson", "Score de Leipzig entier : 4 ou plus établi, 3 possible, 2 ou moins très improbable."],
        ["DX.10", "Insuffisance hépatique aiguë", "Enzymes aiguës, INR habituellement au-dessus de 1,5, encéphalopathie, sans cirrhose connue. King's College et Clichy."],
    ]
    return W("w-dix", "Les dix noms, tels que la liste les fige", "\n".join([
        P("Chaque nom ci-dessous est celui de la liste canonique. Le détail est dans le fichier du diagnostic. La Phase A ne les réduit pas à un mot."),
        table("Liste de la leçon", ["N°", "Nom", "Repère"], rows),
    ]))

def bloc_hy_long():
    return W("w-hy-long", "Lire une loi de Hy sans la raccourcir", "\n".join([
        P(f"La loi n'est pas « transaminases plus ictère ». La recommandation de 2019 écrit trois composantes, et le signal d'un essai les exige toutes. "
          f"La première est collective : plus d'élévations de l'{ALAT} ou de l'{ASAT} d'au moins trois fois la {LSN} que dans le groupe témoin. "
          f"La deuxième est individuelle : la même élévation, plus une bilirubine totale au-dessus de deux fois la {LSN}, sans cholestase initiale portée par la {PAL}. "
          f"La troisième est l'absence d'autre cause : virus A, B, C ou E, maladie de foie déjà là, autre médicament capable du même tableau.", 2),
        P(f"Au lit, on appelle cas de loi de Hy le patient qui réunit la deuxième et la troisième composante. "
          f"On fractionne la bilirubine. Une hausse non conjuguée, Gilbert ou hémolyse, ne compte pas. "
          f"La bilirubine peut monter jusqu'à quatre semaines après le pic des aminotransférases : un bilan unique le jour du pic ne clôt pas l'affaire.", 2),
        P(f"Une {PAL} qui dépasse deux fois la {LSN} au moment du pic ne suffit pas à classer le cas en cholestase si R reste au-dessus de 5. "
          f"Le registre espagnol cité par la recommandation n'a pas vu la {PAL} protéger de l'insuffisance dans ce cas. On garde le patient dans la loi de Hy et on le surveille comme tel.", 2),
        P("Le chiffre lu est celui-ci : au moins 10 % de ces atteintes évoluent vers une insuffisance mortelle ou une transplantation. "
          "Ce n'est pas le risque de chaque enzyme isolée à trois fois la limite. L'enzyme seule, sans bilirubine et sans exclusion des autres causes, n'est pas la loi.", 2),
        P(f"Conséquence pratique. On arrête le suspect. On dose l'{INR} et la bilirubine conjuguée deux à trois fois par semaine tant que les chiffres bougent. "
          f"On hospitalise si l'{INR} s'allonge, si la vigilance baisse, ou si les vomissements empêchent de boire. "
          f"On ne commence pas l'acétylcystéine de Prescott pour une loi de Hy sans paracétamol : ce schéma est celui de l'intoxication, information 31954.", 2, 11),
    ]))

def bloc_rucam_long():
    return W("w-rucam-long", "Les sept domaines, un par un", "\n".join([
        P("Domaine 1, le délai. Le médicament doit avoir commencé avant les enzymes, dans une fenêtre compatible avec une réaction idiosyncrasique ou, pour le paracétamol, avec une toxicité de dose. Un produit commencé après le pic n'est pas le coupable.", 2),
        P("Domaine 2, l'arrêt. La baisse des enzymes après le retrait ajoute des points. Une aggravation malgré l'arrêt en retire. On date l'arrêt, on ne se contente pas de dire « le patient ne le prend plus ».", 2),
        P("Domaine 3, les facteurs de risque. L'âge au-dessus de 55 ans, l'alcool et la grossesse donnent des points dans l'échelle, même si les grands registres ne font pas de l'âge un facteur général. On les note, on ne les transforme pas en cause.", 2),
        P("Domaine 4, les autres médicaments. Chaque hépatotoxique concomitant retire des points. La liste de l'officine, y compris les prises ponctuelles, se reconstruit.", 2),
        P("Domaine 5, les causes non médicamenteuses. Virus, obstruction, ischémie, auto-immunité, alcool. Moins on a cherché, plus le score baisse. Un score haut sans sérologie est un score incomplet.", 2),
        P("Domaine 6, la connaissance antérieure. Un médicament déjà connu pour ce type de lésion marque plus qu'un produit jamais décrit. L'absence de publication ne l'innocente pas : elle baisse seulement ce domaine.", 2),
        P("Domaine 7, la réintroduction. Une reprise accidentelle qui reproduit la lésion pèse lourd. Elle ne se programme pas pour terminer le score.", 2),
        P("Les cinq classes restent affichées ensemble : hautement probable au-dessus de 8, probable de 6 à 8, possible de 3 à 5, improbable de 1 à 2, exclu à 0 ou moins. "
          "Un possible justifie l'arrêt et la surveillance, pas une certitude médico-légale.", 2),
    ]))

def bloc_kings_long():
    return W("w-kings-long", "Appliquer King's College sans en oublier une ligne", "\n".join([
        P(f"Définition d'abord. Enzymes aiguës, coagulopathie d'origine hépatique, en général un {INR} supérieur à 1,5, et une encéphalopathie clinique, chez quelqu'un sans cirrhose connue. "
          f"Le nouveau-né et le très jeune enfant peuvent ne pas avoir d'encéphalopathie visible : la recommandation demande alors un {INR} supérieur à 4. "
          f"Trois maladies chroniques peuvent se présenter comme une insuffisance aiguë : hépatite auto-immune, Budd-Chiari, Wilson.", 3),
        P(f"Paracétamol, trois portes, une seule suffit. Porte du pH : pH artériel inférieur à 7,3 après le remplissage, et plus de 24 heures après la prise. "
          f"Porte du lactate : supérieur à 3 mmol/l. Porte des trois critères réunis : encéphalopathie au-dessus du grade 3, créatinine supérieure à 300 µmol/l, {INR} supérieur à 6,5. "
          f"Réunir deux critères sur trois de cette porte ne suffit pas. Oublier le délai de 24 heures sur le pH non plus.", 3),
        P(f"Hors paracétamol. Soit l'{INR} dépasse 6,5 à lui seul. Soit trois critères parmi cinq : cause indéterminée ou médicament, âge inférieur à 10 ans ou supérieur à 40 ans, "
          f"plus de 7 jours entre l'ictère et l'encéphalopathie, bilirubine supérieure à 300 µmol/l, {INR} supérieur à 3,5. "
          f"Deux critères ne remplissent pas la règle des trois. L'{INR} supérieur à 3,5 compte dans la liste, il ne remplace pas le seuil de 6,5 qui, lui, suffit seul.", 3),
        P("Clichy s'ajoute, il ne se substitue pas. Encéphalopathie de stade 3 ou 4, et facteur V inférieur à 20 % avant 30 ans, ou inférieur à 30 % après 30 ans. "
          "La recommandation discute la transplantation si King's College ou Clichy est rempli.", 3),
        P(f"Pendant ce temps, l'acétylcystéine de l'intoxication suit Prescott, et la recommandation de 2017 la donne aussi quand la coagulopathie et les aminotransférases sont déjà là, "
          f"même si le dosage de paracétamol est négatif. Le dosage négatif n'efface pas une prise ancienne.", 3, 11),
    ]))

def bloc_alcool_long():
    return W("w-alcool-long", "Hépatite alcoolique : scores entiers", "\n".join([
        P("Le syndrome est un ictère récent, avec ou sans ascite et sans encéphalopathie obligatoire, chez quelqu'un qui boit encore ou qui s'est arrêté depuis des jours ou des semaines. "
          "La biopsie montre une stéatose, des ballonisations et des polynucléaires, mais le diagnostic de départ est clinique et biologique.", 4),
        P(f"Biologie lue : polynucléose, bilirubine au-dessus de 50 µmol/l, {ASAT} au-dessus de deux fois la {LSN} et au-dessus de 50 U/l, rarement au-dessus de 300 U/l, "
          f"rapport {ASAT} sur {ALAT} en général supérieur à 1,5 jusqu'à 2. Au stade de cirrhose, le même rapport, simplement supérieur à 1, n'est ni sensible ni spécifique.", 4),
        P("Maddrey, formule entière. En 1978 : 4,6 fois le temps de prothrombine en secondes, plus la bilirubine en mg/dl. Les décès de cette série survenaient au-dessus de 93. "
          "Forme modifiée de 1989, celle du seuil 32 : 4,6 fois (temps de prothrombine du patient moins le temps témoin), plus la bilirubine en mg/dl. "
          "Le rapport STOPAH écrit la même chose avec la bilirubine en µmol/l divisée par 17,1. Maladie sévère si le résultat est au moins 32, ou s'il y a une encéphalopathie. "
          "En dessous de 32, le risque de décès à un mois lu dans l'EASL 2018 est inférieur à 10 %.", 4, 20),
        P("Glasgow, Forrest, Hepatology 2005, toutes les cases. Âge : moins de 50 ans vaut 1, 50 ans ou plus vaut 2. "
          "Leucocytes : moins de 15 milliards par litre vaut 1, 15 ou plus vaut 2. Urée : moins de 5 mmol/l vaut 1, 5 ou plus vaut 2. "
          "Rapport de prothrombine ou INR : moins de 1,5 vaut 1, de 1,5 à 2,0 vaut 2, plus de 2,0 vaut 3. "
          "Bilirubine : moins de 125 µmol/l vaut 1, de 125 à 250 vaut 2, plus de 250 vaut 3. "
          "Total de 5 à 12. Au moins 9 : mauvais pronostic. Avec un Maddrey d'au moins 32, c'est aussi le groupe où le corticoïde a montré un bénéfice à 84 jours dans l'EASL 2018.", 4, 19),
        P("Lille, de 0 à 1, au septième jour de corticoïde. Au moins 0,45 : non-réponse. Trois classes, toutes gardées : réponse complète jusqu'à 0,16, réponse partielle de 0,16 à 0,56, réponse nulle à partir de 0,56. "
          "La recommandation arrête le corticoïde chez le non-répondeur nul.", 4),
        P("Le corticoïde lu est la prednisolone à quarante milligrammes par jour, ou la méthylprednisolone à trente-deux milligrammes par jour, s'il n'y a pas d'infection. "
          "L'information 29348 autorise habituellement 5-60 mg/jour de prednisolone : la fourchette suisse contient la dose européenne, le comprimé de quarante milligrammes n'y est pas écrit. "
          "L'essai britannique n'a pas montré de bénéfice au-delà d'un mois. L'abstinence reste la mesure qui décide du long terme.", 4, 13),
        P(f"Nutrition citée via l'{A('European Society for Clinical Nutrition and Metabolism','ESPEN')} : 35 à 40 kcal par kilogramme et de un gramme deux dixièmes à un gramme et demi de protéines par kilogramme. "
          "Les vitamines du groupe B précèdent le glucose abondant, à cause de Gayet-Wernicke. L'infection se cherche avant le corticoïde, pendant, et après.", 4),
    ]))

def bloc_masld_long():
    return W("w-masld-long", "Stéatose métabolique : définition et deux chemins", "\n".join([
        P("La maladie se définit par une stéatose, au moins un facteur cardiométabolique, et l'absence d'un usage d'alcool considéré comme nocif. "
          "Elle remplace l'ancienne maladie appelée non alcoolique. Le spectre va de la stéatose isolée à l'hépatite métabolique, à la fibrose, à la cirrhose et au carcinome.", 5),
        P("La recommandation de 2024 sépare trois usages d'alcool, en grammes par jour. "
          "Maladie alcoolique : plus de cinquante chez la femme, plus de soixante chez l'homme. "
          "Zone intermédiaire, dite MetALD : de vingt à cinquante chez la femme, de trente à soixante chez l'homme. "
          "La recommandation de 2018, elle, suspecte une maladie alcoolique dès plus de vingt grammes chez la femme et plus de trente chez l'homme quand les enzymes ou la clinique sont anormales. "
          "On cite les deux seuils avec leur texte, on n'en fabrique pas un troisième.", 4, 5),
        P(f"Le {FIB}-4 est le premier tri chez l'adulte à risque : diabète, obésité abdominale avec un autre facteur, ou enzymes qui restent hautes. "
          f"Sous 1,3 : risque bas, nouveau calcul dans un à trois ans, en sachant qu'environ 10 % des fibroses avancées manquent. "
          f"Après 65 ans, ce seuil bas passe à 2,0. Avant 35 ans, on ne se fie pas au chiffre.", 5),
        P(f"Entre 1,3 et 2,67, deux chemins sont écrits, pas un seul. "
          f"Chemin immédiat : élastographie, surtout si le score est proche de 2,67 ou si le risque est haut. "
          f"Chemin différé : un an de poids, de diabète et de tension, puis un second {FIB}-4, et l'élastographie s'il reste haut. "
          f"Au-dessus de 2,67, le second examen ne se reporte pas. L'aire sous la courbe lue pour la fibrose avancée est d'environ 0,77.", 5),
        P("Le risque qui tue le plus souvent ces patients est cardiovasculaire, rénal et tumoral, pas seulement hépatique. "
          "Le tri fibreux sert à trouver ceux dont le foie va décompenser. Il ne remplace pas le traitement du diabète.", 5),
    ]))

def bloc_fer_cuivre_hai():
    return W("w-fer-cuivre", "Fer, cuivre, auto-immunité : ce qui a été lu", "\n".join([
        P("Hémochromatose, 2022. Premier geste : saturation de la transferrine et ferritine, le matin, le jeûne n'améliore pas le rendement. "
          "Saturation élevée : au-dessus de 50 % chez l'homme, au-dessus de 45 % chez la femme.", 6),
        P("Homozygote p.Cys282Tyr : le diagnostic provisoire est biologique. Femme : saturation au-dessus de 45 % et ferritine au-dessus de 200 µg/l. "
          "Homme ou femme ménopausée : saturation au-dessus de 50 % et ferritine au-dessus de 300 µg/l. "
          "Autre génotype : il faut le fer du foie à l'imagerie ou à la biopsie. On ne pose pas le nom sur une ferritine isolée d'inflammation.", 6),
        P("Saignées : ferritine sous 50 µg/l en induction, sous 100 µg/l en entretien. La fibrose avancée entre dans un dépistage du carcinome hépatocellulaire. L'hepcidine ne se dose pas.", 6),
        P("Wilson, score de Leipzig entier, EASL 2012. Anneaux de Kayser-Fleischer : 2 si présents, 0 si absents. "
          "Neurologie : 2 si sévère, 1 si légère, 0 si absente. Céruléoplasmine : 0 au-dessus de 0,2 g/l, 1 entre 0,1 et 0,2 g/l, 2 en dessous de 0,1 g/l. "
          "Hémolyse à Coombs négatif : 1 ou 0. Cuivre hépatique : 2 au-dessus de 4 µmol/g, 1 entre 0,8 et 4, moins 1 si normal. "
          "Rhodanine : 1 point si le dosage quantitatif manque. Cuivre urinaire : 0, 1 ou 2 selon la limite, ou 2 si la pénicillamine fait dépasser cinq fois la limite. "
          "Mutations : 4 sur les deux chromosomes, 1 sur un seul, 0 si aucune. "
          "Quatre ou plus : diagnostic établi. Trois : possible. Deux ou moins : très improbable. "
          "L'anneau manque dans jusqu'à la moitié des formes hépatiques. L'association anneau plus céruléoplasmine sous 0,1 g/l suffit souvent.", 21),
        P("Hépatite auto-immune. Score simplifié de Hennes, Hepatology 2008, tableau 2, repris par l'EASL 2015. "
          "Autoanticorps, somme plafonnée à 2 : antinucléaires ou anti-muscle lisse d'au moins 1/40 = 1 point ; "
          "antinucléaires ou anti-muscle lisse d'au moins 1/80, ou anticorps anti-microsomes d'au moins 1/40, ou anticorps anti-SLA positifs = 2 points. "
          "Immunoglobuline G au-dessus de la limite supérieure = 1 point ; au-dessus de 1,10 fois cette limite = 2 points. "
          "Histologie, une hépatite est nécessaire : atypique = 0 (par exemple une stéatohépatite), compatible = 1 (hépatite chronique lymphocytaire sans tous les traits typiques), "
          "typique = 2 (hépatite d'interface, infiltrat lymphocytaire ou lymphoplasmocytaire portal étendu au lobule, empéripolèse, rosettes). "
          "Absence d'hépatite virale = 2 points. Au moins 6 : probable. Au moins 7 : certaine. "
          "Jeu de validation : sensibilité 88 % et spécificité 97 % au seuil d'au moins 6 ; sensibilité 81 % et spécificité 99 % au seuil d'au moins 7. "
          "Une phrase de la conclusion de 2008 dit plus de 6 pour le probable et 7 ou plus pour le certain. Le tableau et l'EASL 2015 disent au moins 6 et au moins 7 : c'est ce tableau que l'on enseigne, sans cacher la variante de la conclusion.", 7, 22),
        P("Chez l'adulte, un titre d'immunofluorescence d'au moins 1/40 est significatif. "
          "Chez l'enfant, 1/20 pour les antinucléaires ou le muscle lisse, 1/10 pour les anticorps anti-microsomes de foie et de rein.", 7),
        P("Environ 85 % des patients ont une immunoglobuline G haute. Environ 25 % débutent de façon aiguë. "
          "Dans la forme aiguë, 25 à 39 % ont une immunoglobuline G normale et 9 à 17 % n'ont pas d'autoanticorps : un bilan négatif n'écarte pas la maladie si le tableau est fulminant.", 7),
        P(f"Chevauchement avec la cholangite biliaire primitive, critères de Paris, au moins deux critères sur trois de chaque maladie. "
          f"Côté biliaire : {PAL} au moins deux fois la {LSN} ou {GGT} au moins cinq fois, anticorps antimitochondries, lésion floride des canaux. "
          f"Côté hépatite : {ALAT} au moins cinq fois la {LSN}, immunoglobuline G au moins deux fois la {LSN} ou anticorps anti-muscle lisse, nécrose parcellaire modérée ou sévère.", 7),
        P(f"Traitement lu : le corticoïde induit, le thiopurique épargne le corticoïde, la cible est la normalisation de l'immunoglobuline G et de l'{ALAT}. "
          f"Imurek 31887 indique l'hépatite chronique active auto-immune et, hors transplantation, commence en général à 1 à 3 mg/kg par jour. "
          f"La prednisolone suisse se tient dans 5-60 mg/jour.", 7, 13, 16),
    ]))

def bloc_obstacle():
    return W("w-obstacle", "Cholestase : ce qui est dans le canal et ce qui n'y est pas", "\n".join([
        P(f"R au plus égal à 2, ou {PAL} au moins à deux fois la {LSN}, définit le profil cholestatique. "
          f"La {GGT} haute soutient l'origine hépatobiliaire. Une {PAL} haute et une {GGT} normale font regarder l'os, le placenta et l'intestin avant le foie.", 2),
        P("L'échographie répond à une question : les voies sont-elles dilatées ? Dilatées et douloureuses avec de la fièvre : obstacle infecté, drainage. "
          "Fines, avec prurit et anticorps antimitochondries : cholangite biliaire primitive, pas une pierre oubliée.", 2),
        P("L'acide ursodésoxycholique de l'information 60812 est indiqué dans la cholangite biliaire primitive aux stades I à III. "
          "La dose journalière suit le poids, autour de douze à seize milligrammes par kilogramme, d'abord répartie, puis le soir quand les enzymes baissent. "
          "Au stade avancé, le même produit peut décompenser la cirrhose : on surveille, on n'augmente pas dans le brouillard.", 12),
        P("Une cholestase intrahépatique qui n'est pas une cholangite biliaire primitive ne reçoit pas cet acide hors étude, dit l'information. "
          "On ne l'étend pas à tout prurit.", 12),
        P("Le Child-Pugh de ces maladies cholestatiques utilise, sur la page lue, une bilirubine décalée : 68 µmol/l pour rester à 1 point, 170 µmol/l comme borne haute de 2 points. "
          "Les classes A, B et C et les autres items ne changent pas.", 9),
    ]))

def bloc_questions():
    paires = [
        ("Pourquoi le premier bilan, et pas le pic ?",
         f"Parce que la recommandation de 2019 fixe le profil sur le premier jeu de résultats lié à l'événement. Une {PAL} qui monte ensuite peut faire croire à une cholestase alors que R était hépatocellulaire."),
        ("R égal à 2, de quel côté ?",
         "Du côté cholestatique. Le mixte commence au-dessus de 2 et s'arrête avant 5. Les trois classes restent nommées."),
        ("Une ALAT à dix fois la limite et un INR normal, est-ce une insuffisance aiguë ?",
         f"Non. L'{A('insuffisance hépatique aiguë','IHA')} demande une coagulopathie, en général un {A('international normalized ratio','INR')} supérieur à 1,5, et une encéphalopathie, sans cirrhose connue."),
        ("Le nomogramme avant 4 heures ?",
         "Il ne se lit pas. L'absorption n'est pas tenue pour complète. On note l'heure et on prélève au bon moment, sans retarder l'antidote si l'histoire est déjà celle d'une intoxication grave."),
        ("150 µg/ml et 150 mg/kg, même chose ?",
         "Non. 150 µg/ml est un point de la ligne de traitement de 1981. 150 mg/kg est le bolus d'acétylcystéine de l'information 31954."),
        ("Child-Pugh sur une hépatite aiguë sans cirrhose ?",
         "Non. A, B et C décrivent une maladie chronique. L'aiguë se juge par King's College et Clichy."),
        ("Peut-on ne citer que la classe B ?",
         "Non. A est 5 ou 6, B est 7 à 9, C est 10 à 15. Une classe isolée n'est plus le score."),
        ("Maddrey à 28, corticoïde ?",
         "Le seuil lu de l'hépatite alcoolique sévère est 32. En dessous, le risque de décès à un mois cité est inférieur à 10 %, et le corticoïde n'est pas l'indication de ce seuil."),
        ("Lille à 0,60 au jour 7 ?",
         "C'est une réponse nulle, au-dessus de 0,56. Le corticoïde s'arrête. La classe partielle s'arrêtait à 0,56, la complète à 0,16."),
        ("FIB-4 à 1,8 chez un adulte de 50 ans ?",
         f"Zone intermédiaire, entre 1,3 et 2,67. Deux chemins : élastographie, ou un an de traitement métabolique puis un second {A('fibrosis-4 index','FIB')}-4. On ne choisit pas un troisième chemin."),
        ("FIB-4 à 1,8 chez un adulte de 70 ans ?",
         "Le seuil bas après 65 ans est 2,0. 1,8 reste sous ce seuil. Avant 35 ans, le même outil est peu fiable."),
        ("Ferritine haute, saturation normale ?",
         "Ce n'est pas le diagnostic provisoire d'hémochromatose. La saturation fait partie du premier pas. L'inflammation et l'alcool élèvent la ferritine seule."),
        ("Homozygote C282Y, saturation et ferritine dans les zones lues ?",
         "Le diagnostic provisoire est posé sans biopsie. Un autre génotype exige le fer hépatique en image ou en histologie."),
        ("Immunoglobuline G normale et pas d'anticorps, hépatite aiguë sévère ?",
         "La forme aiguë de l'hépatite auto-immune peut être dans ce cas : 25 à 39 % ont une immunoglobuline normale, 9 à 17 % n'ont pas d'anticorps. On n'écarte pas la maladie sur ce seul négatif."),
        ("Score simplifié à 6, probable ou certain ?",
         "Tableau de Hennes 2008 et EASL 2015 : au moins 6 probable, au moins 7 certaine. Autoanticorps plafonnés à 2, immunoglobuline G (1 au-dessus de la limite, 2 au-dessus de 1,10 fois), histologie 0, 1 ou 2, absence de virus = 2. Une phrase de conclusion dit plus de 6 ; on enseigne le tableau."),
        ("Quelle cible sous traitement auto-immun ?",
         f"Normaliser l'immunoglobuline G et l'{A('alanine aminotransférase','ALAT')}. Le thiopurique épargne le corticoïde. L'azathioprine suisse, hors greffe, commence en général entre 1 et 3 mg/kg par jour."),
        ("Acide ursodésoxycholique pour tout prurit ?",
         "Non. L'information 60812 le réserve à la cholangite biliaire primitive, et elle déconseille de l'étendre aux autres cholestases intrahépatiques hors étude."),
        ("ASAT 500, ALAT 80, kinase normale, alcool ?",
         f"L'{A('aspartate aminotransférase','ASAT')} de l'hépatite alcoolique dépasse rarement 300 U/l. À 500 avec une kinase normale, on cherche une autre nécrose, dont l'ischémie et le paracétamol."),
        ("pH à 7,25 à la sixième heure après le paracétamol ?",
         "La porte du pH de King's College demande plus de 24 heures après la prise, après remplissage. Un pH bas trop tôt ne coche pas cette porte. Le lactate et le tableau clinique restent lus."),
        ("Facteur V à 25 % à 40 ans, encéphalopathie stade 3 ?",
         "Clichy demande moins de 30 % après 30 ans, avec une encéphalopathie de stade 3 ou 4. 25 % est en dessous de 30 %. Le critère est rempli. Avant 30 ans, la barre serait 20 %."),
        ("Sodium à 122 dans le MELD-Na ?",
         f"La formule de 2010 borne le sodium entre 125 et 140 mmol/l. 122 devient 125. Au-dessus de 140, on prend 140. Puis {A('model for end-stage liver disease','MELD')}-Na = {A('model for end-stage liver disease','MELD')} − Na − [0,025 × {A('model for end-stage liver disease','MELD')} × (140 − Na)] + 140."),
    ]
    corps = []
    for q, r in paires:
        corps.append(f"<p><b>{q}</b> {r}{S(2,3,4,5,6,7,8,9,10,11)}</p>")
    corps.append(P("Ces questions reprennent les seuils déjà cités. Elles ne créent pas un chiffre nouveau.", 2))
    return W("w-questions", "Questions d'examen sur les seuils entiers", "\n".join(corps))

def bloc_suivi():
    ALAT = A("alanine aminotransférase", "ALAT")
    LSN = A("limite supérieure de la normale", "LSN")
    VHB = A("virus de l'hépatite B", "VHB")
    FIB = A("fibrosis-4 index", "FIB")
    return W("w-suivi", "Surveillance : ce que la recommandation de 2017 écrit vraiment", "\n".join([
        P(f"Phase III avec ADN du {VHB} sous 2 000 UI/ml : {ALAT} tous les 6 à 12 mois, ADN et fibrose de temps en temps, par exemple tous les 2 à 3 ans. "
          f"Si l'antigène HBs est sous 1 000 UI/ml, l'{ALAT} peut n'être revue qu'une fois par an, l'ADN et la fibrose tous les 3 ans. "
          f"S'il est au-dessus de 1 000 UI/ml, l'{ALAT} revient tous les 6 mois, l'ADN et la fibrose au moins tous les 2 ans.", 17),
        P(f"Phase III avec ADN au-dessus de 2 000 UI/ml, sans critère de traitement : {ALAT} au moins tous les 3 mois la première année, puis tous les 6 mois, "
          f"et ADN plus fibrose non invasive chaque année pendant au moins 3 ans. Un rythme unique pour tous les porteurs n'existe pas dans le texte.", 17),
        P(f"Le carcinome reste le souci principal même sous traitement. L'échographie abdominale est recommandée chez tout patient. "
          f"La sévérité se juge sur l'examen, les enzymes, la bilirubine, l'albumine, la numération et le temps de prothrombine. "
          f"Si les marqueurs ne tranchent pas, biopsie ou test non invasif. L'élastographie est surtout utile pour écarter la cirrhose, moins pour l'affirmer.", 17),
        P(f"Sous interféron pégylé, les contrôles lus sont à 3, 6 et 12 mois de traitement, puis 6 et 12 mois après. "
          f"La réponse souhaitée est un ADN durablement sous 2 000 UI/ml, mieux une perte de l'antigène HBs, avec une {ALAT} normale, "
          f"et une séroconversion HBe si l'antigène HBe était positif. Après l'arrêt, la rechute existe : le suivi ne s'arrête pas au dernier comprimé.", 17),
        P(f"Réactivation. Un antigène HBs positif qui reçoit un antiviral de l'hépatite C est candidat à une prophylaxie par analogue jusqu'à la semaine 12 après ce traitement, avec une surveillance étroite. "
          f"Un antigène HBs négatif mais anti-HBc positif se surveille, et l'on cherche la réactivation si l'{ALAT} monte. "
          f"Ce n'est pas la même conduite. La phase V n'est pas un dossier clos.", 17),
        P("Liste d'attente de greffe pour une maladie liée au virus : analogue pour tout candidat, afin d'arriver à un ADN indétectable. "
          "Après la greffe, l'immunoglobuline anti-HBs plus un analogue puissant est la combinaison recommandée. "
          "Les patients à bas risque peuvent arrêter l'immunoglobuline et garder l'analogue. "
          "Un receveur antigène HBs négatif qui reçoit un foie anti-HBc positif a besoin d'une prophylaxie par analogue.", 17),
        P(f"Cinq ans d'entécavir dans l'hépatite antigène HBe positif : probabilité cumulée de réponse virologique de 99 %, perte de l'antigène HBe de 53 %. "
          f"Cinq ans de ténofovir disoproxil dans la même situation, parmi les patients encore sous traitement : réponse virologique 97 %, {ALAT} normale 73 %, "
          f"perte de l'antigène HBe 49 %, séroconversion 40 %, perte de l'antigène HBs 10 %, séroconversion HBs 8 %. "
          f"Ces pourcentages décrivent des essais, pas la promesse faite à un patient au cabinet.", 17),
    ])) + W("w-cas-ambu", "Cas d'examen : enzyme de ville, corrigé pas à pas", "\n".join([
        P(f"<b>Énoncé.</b> Homme de 52 ans, diabète de type 2, tour de taille augmenté, pression artérielle traitée. "
          f"Pas d'alcool au-delà d'un verre le dimanche, pas de nouveau médicament. "
          f"{ALAT} 55 U/l pour une {LSN} à 40, {A('aspartate aminotransférase','ASAT')} 48 U/l, phosphatase alcaline normale, plaquettes 220 milliards par litre, "
          f"bilirubine normale, INR normal. L'échographie montre un foie hyperéchogène. Que fait-on, et que ne fait-on pas ?"),
        P(f"Étape 1, le profil. L'{ALAT} est à 1,4 fois la {LSN}, la phosphatase est normale : R n'est pas cholestatique. "
          f"On ne lance pas un drainage. On ne calcule pas un Maddrey : il n'y a pas d'ictère ni d'usage lourd d'alcool.", 2, 4),
        P(f"Étape 2, le terrain. Au moins un facteur cardiométabolique, en réalité trois, et une stéatose à l'image : c'est le champ de la stéatose liée à un dysfonctionnement métabolique, "
          f"tant que l'alcool nocif est écarté. Vingt grammes par jour chez la femme et trente chez l'homme sont le seuil de suspicion de 2018 ; "
          f"cinquante et soixante grammes sont le seuil de maladie alcoolique de 2024. Un verre le dimanche n'atteint aucun des deux.", 4, 5),
        P(f"Étape 3, le {FIB}-4. Âge 52, {A('aspartate aminotransférase','ASAT')} 48, {ALAT} 55, plaquettes 220. "
          f"Racine carrée de 55 : environ 7,4. Plaquettes fois cette racine : environ 1 630. Âge fois {A('aspartate aminotransférase','ASAT')} : 2 496. "
          f"Score environ 1,5. C'est au-dessus de 1,3 et en dessous de 2,67, et l'homme a moins de 65 ans donc le seuil bas n'est pas 2,0. "
          f"Zone intermédiaire : élastographie, ou un an de traitement du diabète, du poids et de la tension puis un second score. Les deux chemins sont licites. Un contrôle dans trois ans ne l'est pas.", 5),
        P(f"Étape 4, ce qu'il ne faut pas oublier quand même. Un médicament hépatotoxique, une sérologie si le profil devenait franchement hépatocellulaire, "
          f"une saturation de la transferrine si la ferritine est haute. Ici la ferritine n'est pas donnée : on ne pose pas une hémochromatose sur une stéatose.", 6),
        P(f"<b>Variante.</b> Le même homme revient avec une {ALAT} à 900 U/l, une {A('aspartate aminotransférase','ASAT')} à 1 100 U/l, une créatinine qui a doublé, "
          f"après un épisode d'hypotension aux urgences. La lacticodéshydrogénase est haute. "
          f"Ce n'est plus le {FIB}-4. C'est le profil ischémique lu en 2017 : enzymes très hautes, lacticodéshydrogénase et créatinine, puis chute rapide si la pression revient. "
          f"On cherche la cause hémodynamique. Si l'INR s'allonge et que la vigilance baisse, King's College et Clichy prennent la suite, pas le score de fibrose.", 3),
        P(f"<b>Variante médicamenteuse.</b> Trois semaines après un antibiotique, {ALAT} à six fois la {LSN}, bilirubine à trois fois la {LSN}, phosphatase à 1,2 fois la {LSN}, pas d'autre cause. "
          f"R est très au-dessus de 5. Les composantes individuelles de la loi de Hy sont là si aucune autre cause ne tient : aminotransférase au-dessus de trois fois et bilirubine au-dessus de deux fois, sans cholestase initiale. "
          f"On arrête l'antibiotique. On ne donne pas le bolus de 150 mg/kg, réservé au paracétamol. On surveille l'INR. "
          f"Le score de causalité se complète ensuite, avec ses cinq classes, il ne se devine pas.", 2, 11),
        P("Barème de correction. Profil juste et seuil juste : les points. Appliquer un score d'une autre maladie : les points tombent. "
          "Citer une classe sans les autres : les points tombent. Inventer une dose absente de l'information suisse et de la recommandation lue : les points tombent.", 2, 5),
    ])) + W("w-unites", "Unités suisses et seuils publiés en mg/dl", "\n".join([
        P("Plusieurs seuils lus sont en mg/dl. Le laboratoire suisse rend souvent la bilirubine en µmol/l et l'albumine en g/l. "
          "La conversion se montre, elle ne se cache pas. Un mg/dl de bilirubine vaut 17,1 µmol/l. "
          "Donc 2 mg/dl, seuil diagnostique de l'ictère dans Tokyo 2018, valent 34 µmol/l. "
          "5 mg/dl, seuil de gravité du grade II, valent 85,5 µmol/l. "
          "On n'arrondit pas 5 mg/dl à 50 µmol/l : ce serait un autre seuil, celui du Child-Pugh, qui n'a pas le même usage.", 9, 18),
        P("L'albumine du Child-Pugh est lue en g/dl : plus de 3,5, de 2,8 à 3,5, moins de 2,8. "
          "En g/l, le facteur dix donne plus de 35, de 28 à 35, moins de 28. "
          "Le grade II de Tokyo compare l'albumine à 0,73 fois la limite inférieure de la normale du laboratoire, pas à 28 g/l. "
          "Mélanger ces deux règles classe mal un patient.", 9, 18),
        P(f"Le {A('model for end-stage liver disease','MELD')} de 2010 prend la créatinine et la bilirubine en mg/dl. "
          f"Une bilirubine à 85 µmol/l vaut environ 5 mg/dl, pas 85. Entrer 85 dans le logarithme invente un score incompatible avec la vie. "
          f"La créatinine est plafonnée à 4 mg/dl. Le sodium du {A('model for end-stage liver disease','MELD')}-Na reste en mmol/l, borné de 125 à 140.", 8),
        P("Le nomogramme se lit en µg/ml. 150 µg/ml égalent 150 mg/l, et n'égalent pas 150 mg/kg. "
          "150 mg/kg est le bolus d'acétylcystéine sur 60 minutes, information 31954, suivi de 50 mg/kg sur 4 heures et de 100 mg/kg sur 16 heures. "
          "La ligne de 1975 est à 200 µg/ml à la quatrième heure. La ligne de traitement de 1981 est à 150 µg/ml. Les deux restent.", 10, 11),
        P(f"Le {A('fibrosis-4 index','FIB')}-4 veut les aminotransférases en U/l et les plaquettes en milliards par litre. "
          f"Des plaquettes écrites 220 000 par mm³ sont 220 milliards par litre. Entrer 220 000 dans le dénominateur écrase le score vers zéro et rassure à tort. "
          f"Les seuils 1,3, 2,0 après 65 ans et 2,67 ne changent pas avec cette conversion : seule l'unité des plaquettes change.", 5),
        P(f"Créatinine du grade III de Tokyo : au-dessus de 2,0 mg/dl, soit environ 177 µmol/l si l'on multiplie par 88,4. "
          f"Le critère de King's College pour le paracétamol est une créatinine au-dessus de 300 µmol/l, ce qui est plus haut. "
          f"Un patient à 200 µmol/l peut être en grade III d'angiocholite sans remplir la porte rénale de King's College. Les deux seuils coexistent, ils ne se remplacent pas.", 3, 18),
        P(f"INR. Tokyo grade III : au-dessus de 1,5, un seul organe suffit à la gravité. "
          f"Définition de l'insuffisance aiguë : en général au-dessus de 1,5, avec encéphalopathie. "
          f"King's College hors paracétamol : au-dessus de 6,5 seul, ou au-dessus de 3,5 dans la liste des cinq. "
          f"Child-Pugh : inférieur à 1,7, de 1,7 à 2,3, supérieur à 2,3. "
          f"Quatre usages, quatre seuils. Répondre « INR élevé » sans le chiffre et sans le score est une copie incomplète.", 3, 9, 18),
        P(f"Ordre de la copie quand plusieurs seuils sont vrais en même temps. On écrit d'abord le danger immédiat : nomogramme et Prescott, ou grade de Tokyo, ou King's College. "
          f"On écrit ensuite le profil R avec ses trois classes. On n'ouvre le {A('fibrosis-4 index','FIB')}-4 que si le patient est stable et que la question est la fibrose. "
          f"On n'ouvre le Child-Pugh, avec A, B et C, que si la cirrhose est déjà connue. "
          f"Mettre les quatre outils dans le même paragraphe sans dire lequel décide aujourd'hui est le défaut le plus fréquent.", 3, 5, 9, 11, 18),
        P("Ce que l'on retire encore, parce que la page ne le donnait pas. "
          "Une troisième ligne de nomogramme. Un classement suisse des dix diagnostics par prévalence. "
          "Le score simplifié d'hépatite auto-immune n'est plus dans cette liste : autoanticorps, immunoglobuline G, histologie et absence de virus sont écrits, avec les seuils 6 et 7. "
          "On ne retire pas Maddrey, ni Glasgow, ni les plaquettes de Tokyo, ni Leipzig, ni Hennes : ils sont écrits en entier. "
          "Les deux trous restants sont dans le fichier d'incertitudes du lot. Ils ne sont pas comblés par une moyenne de mémoire. "
          "En revanche, tout ce qui a été lu reste dans la copie : les trois classes de R, les trois classes de Child-Pugh, les cinq classes du score de causalité, "
          "les cinq phases du virus B, les trois grades de Tokyo, les deux lignes du nomogramme, les trois perfusions de Prescott, "
          "les seuils du score de fibrose, les seuils de Maddrey, de Glasgow et de Lille, les quatre domaines du score simplifié, et les deux systèmes de transplantation, King's College et Clichy. "
          "La copie qui ne garde qu'une classe, qu'une phase ou qu'une ligne est incomplète, même si le reste de la phrase est juste. "
          "On relit enfin les unités : mg/dl contre µmol/l, µg/ml contre mg/kg, plaquettes par mm³ contre milliards par litre. "
          "Une conversion fausse fait échouer un seuil juste. On refait le calcul sur le brouillon avant de cocher la case. Le seuil juste dans la mauvaise unité est une mauvaise réponse.", 4, 10, 18),
    ]))

def bloc_vhb_tokyo():
    ALAT = A("alanine aminotransférase", "ALAT")
    ASAT = A("aspartate aminotransférase", "ASAT")
    PAL = A("phosphatase alcaline", "PAL")
    GGT = A("gamma-glutamyltransférase", "GGT")
    LSN = A("limite supérieure de la normale", "LSN")
    INR = A("international normalized ratio", "INR")
    VHB = A("virus de l'hépatite B", "VHB")
    return W("w-vhb", "Hépatite B : les cinq phases, sans en retirer une", "\n".join([
        P(f"La recommandation {A('European Association for the Study of the Liver','EASL')} de 2017 divise l'infection chronique par le {VHB} en cinq phases. "
          f"Une seule mesure d'ADN et d'{ALAT} ne classe pas toujours : il faut des contrôles répétés. Certains patients restent dans une zone grise.", 17),
        P(f"Phase I, autrefois dite de tolérance immunitaire : antigène HBe présent, ADN très élevé, {ALAT} durablement normale. "
          f"La limite supérieure traditionnelle citée est d'environ 40 UI/l. Le foie a peu ou pas de nécrose, mais l'ADN viral s'intègre déjà : le carcinome peut se préparer. "
          f"Cette phase dure plus longtemps après une contamination à la naissance. Ces patients sont très contagieux. La perte spontanée de l'antigène HBe est rare.", 17),
        P(f"Phase II, hépatite chronique antigène HBe positif : antigène HBe, ADN haut, {ALAT} élevée, nécrose modérée ou sévère, fibrose qui s'accélère. "
          f"Elle vient souvent après des années de phase I, plus vite si l'infection a été acquise à l'âge adulte. "
          f"Beaucoup font une séroconversion HBe et passent en phase III. D'autres n'arrêtent pas le virus et glissent vers la phase IV.", 17),
        P(f"Phase III, autrefois porteurs inactifs : anticorps anti-HBe, ADN indétectable ou bas, sous 2 000 UI/ml, {ALAT} normale. "
          f"Certains ont un ADN au-dessus de 2 000 UI/ml, en général sous 20 000 UI/ml, avec une {ALAT} qui reste normale et une histologie presque calme. "
          f"Le risque de cirrhose est alors bas, tant qu'ils ne repartent pas en hépatite. La perte spontanée de l'antigène HBs atteint 1 à 3 % par an, souvent quand l'antigène HBs est sous 1 000 UI/ml.", 17),
        P(f"Phase IV, hépatite chronique antigène HBe négatif : plus d'antigène HBe, en général des anti-HBe, ADN moyen ou haut qui fluctue, {ALAT} élevée. "
          f"C'est une vraie hépatite, pas un portage. La traiter comme une phase III parce que l'antigène HBe est négatif est une erreur de nom.", 17),
        P(f"Phase V, infection occulte : antigène HBs négatif, anti-HBc positif, avec ou sans anti-HBs. "
          f"L'{ALAT} est en général normale, l'ADN sérique souvent indétectable, mais l'ADN circulaire fermé reste souvent dans le foie. "
          f"La perte de l'antigène HBs avant la cirrhose abaisse beaucoup le risque de décompensation et de carcinome. Si la cirrhose est déjà là, ce bénéfice n'est plus le même.", 17),
        P(f"Qui traiter. ADN au-dessus de 2 000 UI/ml et {ALAT} au-dessus de la {LSN}, et/ou une histologie au moins modérée : traiter. "
          f"Cirrhose compensée ou décompensée : tout ADN détectable, quelle que soit l'{ALAT}. "
          f"ADN au-dessus de 20 000 UI/ml et {ALAT} au-dessus de deux fois la {LSN} : traiter sans exiger de biopsie. "
          f"Phase I qui dure, patient de plus de 30 ans : le traitement peut se discuter même si l'{ALAT} est normale. "
          f"Antécédent familial de carcinome ou de cirrhose, ou manifestation extra-hépatique : on peut traiter hors du schéma habituel. Ces indications se lisent ensemble.", 17),
        P(f"Le traitement de fond nommé par la recommandation est un analogue puissant à barrière de résistance haute : entécavir, ténofovir disoproxil ou ténofovir alafénamide. "
          f"En Suisse, les doses lues sont celles des informations : Ténofovir Sandoz 66282, 245 mg une fois par jour avec un repas ; Baraclude 57435, 0,5 mg par jour chez le naïf de nucléoside. "
          f"La dose suisse du ténofovir alafénamide n'est pas dans les extraits de ce lot : elle n'est pas inventée. "
          f"La cible principale est la suppression durable de l'ADN. La perte de l'antigène HBs est la cible optimale, pas le seul succès acceptable.", 14, 15, 17),
    ])) + W("w-tokyo", "Angiocholite : diagnostic et grades I, II et III", "\n".join([
        P("La triade de Charcot, douleur, fièvre et ictère, est très spécifique et peu sensible. "
          "Des séries multicentriques récentes la retrouvent chez 26,4 % et chez 21,2 % des patients. Des séries plus anciennes citaient une sensibilité de l'ordre de 50 à 70 %. "
          "On ne peut donc pas attendre la triade complète pour diagnostiquer.", 18),
        P(f"Les critères de Tokyo 2018 reprennent ceux de 2013. Le diagnostic exige trois volets, et l'inflammation systémique est obligatoire. "
          f"Volet A, inflammation : fièvre au-dessus de 38 °C, ou réponse inflammatoire (leucocytes inférieurs à 4 ou supérieurs à 10 dans l'unité du tableau, protéine C réactive d'au moins 1 mg/dl). "
          f"Volet B, cholestase : ictère avec bilirubine totale d'au moins 2 mg/dl, ou enzymes au-dessus de 1,5 fois la référence ({PAL}, {GGT}, {ASAT}, {ALAT}). "
          f"Volet C, image : dilatation, calcul, sténose ou prothèse. Sans inflammation, ce n'est pas une angiocholite de ces critères, même si la voie est dilatée.", 18),
        P("Appliqués après coup à 6 063 patients traités comme une angiocholite, ces critères en reconnaissaient 5 454, soit 90,0 %, contre 79,4 % pour les critères de 2007. "
          "La sensibilité compte ici plus que la spécificité : la maladie tue si on la rate.", 18),
        P("Grade I, léger : ne remplit ni le grade II ni le grade III. L'antibiotique suffit le plus souvent. Le drainage vient si le patient ne répond pas. "
          "Grade II, modéré : drainage biliaire précoce. Il faut au moins deux des cinq critères : leucocytes d'au moins 12 000 ou inférieurs à 4 000, température d'au moins 39 °C, "
          "âge d'au moins 75 ans, bilirubine totale d'au moins 5 mg/dl, albumine inférieure à 0,73 fois la limite inférieure de la normale. Un seul de ces cinq ne fait pas un grade II.", 18),
        P(f"Grade III, sévère : un seul dysfonctionnement d'organe suffit. Cardiovasculaire : dopamine d'au moins cinq microgrammes par kilogramme par minute, ou noradrénaline. "
          f"Neurologique : trouble de conscience. Respiratoire : rapport de la pression artérielle d'oxygène sur la fraction inspirée inférieur à 300. "
          f"Rénal : oligurie ou créatinine sérique au-dessus de 2,0 mg/dl. Hépatique : {INR} au-dessus de 1,5. "
          f"Hématologique : plaquettes inférieures à 100 000/mm³. Les trois grades et les six défaillances du grade III sont enseignés ensemble.", 18),
        P("Le drainage du grade III est urgent, avec le soutien des organes. Le grade II se draine tôt, sans attendre la défaillance. Le grade I se surveille sous antibiotique. "
          "Confondre ces trois tempos est la faute. La bilirubine de 2 mg/dl sert au diagnostic, celle de 5 mg/dl sert à la gravité : ce ne sont pas le même seuil.", 18),
    ])) + W("w-ischemie", "Ischémie et cas d'examen corrigé", "\n".join([
        P(f"La recommandation de 2017 sur l'insuffisance aiguë décrit la lésion ischémique ainsi : aminotransférases très élevées, lacticodéshydrogénase et créatinine hautes, "
          f"puis normalisation rapide dès que l'hémodynamique est rétablie. Ce n'est pas une hépatite virale qui met des semaines à descendre, ni une {ALAT} chronique de stéatose.", 3),
        P(f"Devant un pic d'{ASAT} et d'{ALAT} au-delà de ce que l'alcool explique (l'{ASAT} alcoolique dépasse rarement 300 U/l), on cherche l'hypotension, l'hypoxie, la défaillance cardiaque droite et la thrombose vasculaire. "
          f"Le Child-Pugh ne se calcule pas sur ce pic. Si l'{INR} s'allonge et que la conscience baisse, on passe aux critères de King's College.", 3, 4),
        P("<b>Cas.</b> Homme de 62 ans. Douleur de l'hypocondre droit, température à 38,5 °C, leucocytes à 13 000, protéine C réactive haute, "
          "bilirubine à 3 mg/dl, phosphatase à trois fois la référence, échographie : calcul de la voie principale et dilatation. Pas de trouble de conscience, créatinine normale, INR normal, albumine normale.", 18),
        P("Correction, diagnostic. Inflammation (fièvre au-dessus de 38 °C et leucocytes hauts), cholestase (bilirubine au-dessus de 2 mg/dl et enzymes hautes), image de calcul : les trois volets de Tokyo 2018 sont là. "
          "La triade de Charcot est présente, mais elle n'était pas exigée.", 18),
        P("Correction, grade. Pour le grade II il faut deux critères parmi cinq. Les leucocytes à 13 000 en remplissent un. "
          "38,5 °C n'atteint pas 39 °C. 62 ans n'atteint pas 75 ans. 3 mg/dl n'atteint pas 5 mg/dl. L'albumine est normale. "
          "Un seul critère : ce n'est pas un grade II, et aucun organe n'est en grade III. C'est un grade I : antibiotique, drainage seulement s'il ne répond pas.", 18),
        P("Le lendemain, la température passe à 39,2 °C et la bilirubine à 6 mg/dl, le reste inchangé. "
          "Deux critères du grade II sont maintenant réunis (température et bilirubine), en plus des leucocytes. Le grade devient II : drainage biliaire précoce, sans attendre un INR au-dessus de 1,5.", 18),
        P(f"<b>Second cas, même semaine de révision.</b> Femme de 35 ans, antigène HBe positif, ADN du {VHB} très élevé, {ALAT} normale à deux reprises sur un an, pas de cirrhose. "
          f"C'est une phase I. Le traitement n'est pas automatique. Comme elle a plus de 30 ans, la recommandation de 2017 permet de le discuter malgré l'{ALAT} normale. "
          f"Ce n'est pas une phase II : l'{ALAT} n'est pas élevée. Si l'{ALAT} dépassait deux fois la {LSN} avec un ADN au-dessus de 20 000 UI/ml, la biopsie ne serait plus exigée.", 17),
        P(f"Ce que l'examen retire des points. Oublier la phase V et rassurer un anti-HBc isolé qui reçoit une chimiothérapie. "
          f"Appeler grade III une angiocholite dès que l'{INR} dépasse 1,5, oui, c'est le critère hépatique, mais appeler grade III une simple fièvre, non. "
          f"Donner le schéma de Prescott, 150 mg/kg puis 50 mg/kg puis 100 mg/kg, à l'angiocholite : ce schéma est celui du paracétamol, information 31954, pas celui du calcul.", 11, 17, 18),
    ]))

EXTRA = {
    0: "",
    1: bloc_masld_long() + bloc_suivi(),
    2: bloc_profils() + bloc_hy_long(),
    3: bloc_dxnoms() + bloc_rucam_long(),
    4: bloc_med(),
    5: "",
    6: bloc_cas() + bloc_alcool_long(),
    7: bloc_fer_cuivre_hai(),
    8: bloc_obstacle() + bloc_vhb_tokyo(),
    9: bloc_heure() + bloc_kings_long(),
    10: "",
    11: "",
    12: bloc_questions(),
    13: "",
}
