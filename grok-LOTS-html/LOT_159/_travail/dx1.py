#!/usr/bin/env python3
"""DX.1 — stéatose métabolique, profondeur V8."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from moteur import A, B, P, S, W, ecrire, page, table

ALAT = A("alanine aminotransférase", "ALAT")
ASAT = A("aspartate aminotransférase", "ASAT")
PAL = A("phosphatase alcaline", "PAL")
GGT = A("gamma-glutamyltransférase", "GGT")
LSN = A("limite supérieure de la normale", "LSN")
EASL = A("European Association for the Study of the Liver", "EASL")
FIB = A("fibrosis-4 index", "FIB")
MASLD = A("metabolic dysfunction-associated steatotic liver disease", "MASLD")
MASH = A("metabolic dysfunction-associated steatohepatitis", "MASH")
SLD = A("steatotic liver disease", "SLD")
IMC = A("indice de masse corporelle", "IMC")
HDL = A("high-density lipoprotein", "HDL")

essentiel = (
    P(f"La {MASLD} est une stéatose du foie avec au moins un facteur cardiométabolique, sans usage d'alcool considéré comme nocif. "
      f"Elle remplace l'ancienne maladie dite non alcoolique. Le spectre va de la stéatose isolée à l'hépatite métabolique ({MASH}), à la fibrose, à la cirrhose et au carcinome.", 5)
    + P(f"Le danger n'est pas le chiffre d'{ALAT}. C'est la fibrose. Le premier tri chez l'adulte est le {FIB}-4 : sous 1,3 le risque est bas, "
      f"entre 1,3 et 2,67 deux chemins sont licites, au-dessus de 2,67 on passe au second test. Après 65 ans le seuil bas est 2,0. Avant 35 ans le score est peu fiable.", 5)
    + P("On ne dépiste pas toute la population. On cherche la fibrose chez le diabétique, chez la personne avec obésité abdominale et un autre facteur, et chez celle dont les enzymes restent hautes.", 5)
)

sous = (
    f"Diagnostic différentiel DX.1 de {A('situation de départ F2.11 de PROFILES','F2.11')} "
    f"« Enzymes hépatiques anormales », {A('Principal Relevant Objectives and Framework for Integrated Learning and Education in Switzerland','PROFILES')} 2023{S(1)}. "
    f"Nom exact de la liste canonique. Texte du 31.10.2026."
)

p1 = P(f"La {MASLD} exige une stéatose documentée, par l'image ou l'histologie, et au moins un des facteurs du tableau lu en 2024, "
       f"sans autre cause discernable. L'hépatite métabolique, ou {MASH}, ajoute en histologie le ballonnement hépatocytaire et l'inflammation lobulaire.", 5)
p1w = W("w-classes", "Toutes les sous-classes de stéatose lues", "\n".join([
    P(f"La {SLD} est le genre. La recommandation de 2024 en nomme plusieurs espèces, et aucune ne se substitue aux autres.", 5),
    table("Sous-classes, toutes gardées", ["Nom", "Ce qui la définit", "Conséquence"], [
        [f"{MASLD}", "Stéatose et au moins un facteur cardiométabolique, sans alcool nocif", "Le tri par FIB-4 s'applique"],
        ["MetALD", "Même terrain, alcool de vingt à cinquante grammes par jour chez la femme et de trente à soixante chez l'homme", "Mortalité toutes causes plus haute ; les conseils de la MASLD ne s'y étendent pas"],
        ["Maladie alcoolique", "Plus de cinquante grammes par jour chez la femme, plus de soixante chez l'homme", "Autre diagnostic de la leçon, DX.2 si l'hépatite alcoolique est là"],
        ["Cause spécifique", "Médicament, maladie monogénique", "On la cherche quand le terrain habituel manque"],
        ["Stéatose cryptogénique", "Pas de facteur, pas de cause connue", "Ce n'est pas une MASLD prouvée"],
        ["Possible MASLD", "Stéatose sans facteur cardiométabolique", "Il faut encore chercher une insulinorésistance"],
    ]),
    P("Retirer MetALD ou la forme cryptogénique pour « simplifier » laisse un trou dans la classification de 2024. Les deux restent.", 5),
    P(f"L'ancienne cohorte dite non alcoolique recouvre presque la {MASLD} : 99,8 % de concordance dans une cohorte de soins tertiaires, "
      f"et seulement 5,3 % des personnes de la cohorte de population NHANES III ne remplissaient pas les critères nouveaux. "
      f"Les tests non invasifs se transposent. Ce n'est pas une permission d'employer l'ancien nom comme s'il était identique dans chaque phrase.", 5),
])) + W("w-cm", "Les facteurs cardiométaboliques, tableau entier", "\n".join([
    P("Un seul suffit. Le tableau de 2024 en compte plusieurs familles. On ne garde pas seulement le diabète.", 5),
    table("Critères de l'adulte", ["Famille", "Seuil lu"], [
        ["Corpulence", f"{IMC} au moins 25 kg/m², ou 23 kg/m² si origine asiatique"],
        ["Tour de taille, Europe", "Au moins 94 cm chez l'homme, 80 cm chez la femme"],
        ["Tour de taille, Asie du Sud et Chine", "Au moins 90 cm chez l'homme, 80 cm chez la femme"],
        ["Tour de taille, Japon", "Au moins 85 cm chez l'homme, 90 cm chez la femme"],
        ["Prédiabète", "Hémoglobine glyquée 39 à 47 mmol/mol, ou glycémie à jeun 5,6 à 6,9 mmol/l, ou glycémie à 2 heures 7,8 à 11 mmol/l"],
        ["Diabète de type 2", "Hémoglobine glyquée au moins 48 mmol/mol, ou glycémie à jeun au moins 7,0 mmol/l, ou glycémie à 2 heures au moins 11,1 mmol/l, ou déjà traité"],
        ["Triglycérides", "Au moins 1,7 mmol/l, ou traitement hypolipémiant"],
        [f"{HDL}", "Au plus 1,0 mmol/l chez l'homme, 1,3 mmol/l chez la femme, ou traitement hypolipémiant"],
        ["Pression", "Au moins 130/85 mmHg, ou traitement antihypertenseur"],
    ]),
    P("Le traitement d'un diabète, d'un lipide ou d'une hypertension compte comme le facteur, même si le chiffre du jour est revenu dans la cible. "
      "Oublier la ligne « ou traitement » sous-estime le terrain.", 5),
]))

p2 = P(f"C'est la maladie chronique du foie la plus fréquente dans le texte de 2024, et elle va encore augmenter. "
       f"Elle est liée au diabète de type 2, à l'obésité et aux autres facteurs. Le dépistage de toute la population n'est pas recommandé.", 5)
p2w = W("w-qui", "Qui progresse", "\n".join([
    P("La stéatose dans la population générale n'est pas, à elle seule, liée aux événements hépatiques. "
      "La fibrose, et des enzymes qui restent hautes, le sont. C'est pour cela que le tri porte sur la fibrose, pas sur le fait d'avoir un foie brillant.", 5),
    P("Les hommes de plus de 50 ans, les femmes après la ménopause, et les personnes qui cumulent les facteurs cardiométaboliques ont un risque plus haut de fibrose qui progresse, de cirrhose et de complications.", 5),
    P(f"La {MASLD} s'associe à des événements hors du foie : cardiovasculaires, rein chronique, cancers. "
      f"Le texte cite des hazard ratios lus, dont 1,43 pour la maladie rénale chronique et 2,19 pour le diabète incident dans les études qu'il résume. "
      f"Ces chiffres décrivent des cohortes, pas le risque personnel calculé au lit sans le reste du dossier.", 5),
    P("Aucun texte lu ne donne la part suisse de ce diagnostic parmi les dix de la leçon. Le rang DX.1 dit la fréquence européenne décrite, pas un registre fédéral.", 5),
]))

p3 = P(f"Le triglycéride s'accumule dans l'hépatocyte quand les apports et l'insuline dépassent ce que le foie exporte. "
       f"L'inflammation et le ballonnement font l'hépatite métabolique. La fibrose décide du pronostic hépatique. "
       f"L'{ALAT} peut rester presque normale malgré une fibrose avancée : le chiffre n'est pas un thermomètre de la cicatrice.", 5)
p3w = W("w-physio", "De la graisse à la cicatrice", "\n".join([
    P("L'insuline haute pousse le foie à fabriquer des triglycérides et freine leur combustion. Le tissu adipeux, surtout viscéral, envoie des acides gras. "
      "La stéatose est ce stock. Elle est visible en échographie quand elle est suffisante, et certaine en histologie.", 5),
    P(f"Le passage à l'hépatite métabolique n'est pas une {ALAT} au-dessus d'un seuil unique. "
      f"C'est, en histologie, le ballonnement et l'inflammation lobulaire. Une enzyme normale n'exclut pas cette étape. Une enzyme haute ne la prouve pas.", 5),
    P("La fibrose part des zones de nécrose et d'inflammation répétées. Elle peut aller jusqu'à la cirrhose et au carcinome sans que le patient ait été ictérique. "
      "D'où le {FIB}-4, qui mélange âge, {ASAT}, {ALAT} et plaquettes : les plaquettes basses et l'{ASAT} qui dépasse l'{ALAT} tirent le score vers le haut.", 5),
    P(f"Formule relue : {FIB}-4 = âge en années × {ASAT} en U/l / (plaquettes en milliards par litre × racine carrée de l'{ALAT} en U/l).", 5),
    P("L'alcool dans la zone MetALD ajoute un risque de mortalité toutes causes alors que les facteurs cardiométaboliques sont les mêmes. "
      "Le mécanisme n'est donc pas « un peu plus de la même graisse ». La recommandation refuse d'y appliquer tels quels les conseils écrits pour la MASLD.", 5),
]))

p4 = P(f"On confirme la stéatose, on compte les facteurs, on quantifie l'alcool en grammes, on écarte le médicament et le virus, puis on trie la fibrose. "
       f"Le {B('w-dd','différentiel')} reprend les autres diagnostics de la leçon qui imitent une enzyme modérée.", 5)
p4w = W("w-dd", "Ce qui n'est pas une stéatose métabolique simple", "\n".join([
    table("Diagnostics à ne pas coller sur un foie brillant", ["Hypothèse", "Ce qui tranche", "Piège"], [
        ["Hépatite alcoolique", "Ictère, rapport ASAT/ALAT souvent au-dessus de 1,5, Maddrey", "Un verre le dimanche n'est pas une hépatite alcoolique"],
        ["Hépatite virale", "Antigène ou ARN, cinq phases pour le virus B", "Un porteur inactif peut avoir en plus une stéatose"],
        ["Médicament", "Chronologie et score de causalité", "Le méthotrexate, le tamoxifène, l'amiodarone font partie des stéatoses médicamenteuses citées"],
        ["Obstacle", "Rapport R au plus égal à 2 et dilatation", "Une stéatose ne dilate pas la voie"],
        ["Hépatite auto-immune", "Score simplifié au moins 6", "Les deux maladies peuvent coexister"],
        ["Hémochromatose", "Saturation et ferritine, puis gène", "La ferritine monte aussi avec la stéatose"],
        ["Wilson", "Cinq piliers du résumé lu", "Y penser chez le jeune"],
        ["Insuffisance aiguë", "INR et encéphalopathie", "Une ALAT à 60 ne l'est pas"],
    ]),
    P("La stéatose du virus C de génotype 3 est une cause spécifique dans le tableau des autres stéatoses : triglycérides plutôt bas, génotype 3. On ne l'appelle pas métabolique par défaut.", 5),
]))

p5 = P("On demande le diabète, les traitements, le tour de taille, la tension, les triglycérides, et l'alcool sur une semaine type, pas sur « je ne bois pas ».", 5)
p5w = W("w-quest", "Questions", "\n".join([
    table("Ce que la réponse change", ["Question", "Réponse", "Effet"], [
        ["Verres par semaine, et lesquels", "Au-dessus de vingt à cinquante grammes par jour chez la femme", "Ce n'est plus la MASLD pure, c'est MetALD ou la maladie alcoolique"],
        ["Médicaments", "Tamoxifène, amiodarone, méthotrexate, valproate, corticoïde au long cours", "Cause spécifique de stéatose, listée en 2024"],
        ["Famille, foie jeune", "Plusieurs apparentés, début précoce", "Maladie monogénique possible, dont le déficit en lipase acide lysosomale"],
        ["Diabète déjà traité", "Oui, même si la glycémie du jour est bonne", "Le facteur compte"],
    ]),
    P("L'histoire d'alcool compte autant que la semaine en cours : un sevrage récent ne transforme pas une maladie alcoolique en stéatose métabolique.", 5),
]))

p6 = P(f"L'examen cherche le tour de taille, la tension, les signes de cirrhose et l'hépatomégalie molle. "
       f"Il n'y a pas de signe cutané propre à la {MASLD}. L'angiome et l'ascite disent que la fibrose est déjà là, et le {FIB}-4 ne sert plus à rassurer.", 5)
p6w = W("w-exam", "Gestes", "\n".join([
    P(f"<b>Tour de taille.</b> En Europe, 94 cm chez l'homme et 80 cm chez la femme suffisent comme facteur, même si l'{IMC} est sous 25. "
      f"Les seuils asiatiques et japonais ne sont pas les mêmes : on n'applique pas 94 cm à un patient dont la recommandation cite un autre seuil ethnique.", 5),
    P("<b>Pression.</b> 130/85 mmHg, ou un traitement déjà commencé. Une mesure unique au stress ne remplace pas le dossier, mais un traitement antihypertenseur compte."),
    P("<b>Foie.</b> Bord mou, régulier, parfois bas. Un bord dur et nodulaire sort de la stéatose simple et fait chercher la cirrhose ou une autre maladie."),
    P("<b>Ce que l'examen ne fait pas.</b> Il ne donne pas le stade de fibrose. Il ne remplace pas les plaquettes dans le FIB-4."),
]))

p7 = P(f"Le syndrome est une enzyme souvent modeste, une {GGT} parfois isolée, un foie hyperéchogène, un terrain métabolique. "
       f"Le {B('w-fib','FIB-4')} classe le risque de fibrose avancée, pas la cause.", 5)
p7w = W("w-fib", "FIB-4, zones entières", "\n".join([
    P(f"Sous 1,3 : risque bas de fibrose avancée. Nouveau calcul dans un à trois ans. Environ 10 % des fibroses avancées manquent malgré tout. "
      f"Après 65 ans, ce seuil bas passe à 2,0. Avant 35 ans, on ne se fie pas au nombre.", 5),
    P(f"De 1,3 à 2,67 inclus dans la zone intermédiaire : deux chemins, pas un. "
      f"Élastographie d'emblée, surtout près de 2,67 ou si le risque est haut. "
      f"Ou un an de poids, de diabète et de tension, puis un second {FIB}-4, et l'élastographie s'il reste haut.", 5),
    P(f"Au-dessus de 2,67 : le second test ne se reporte pas. L'aire sous la courbe lue pour le stade de fibrose au moins F3 est d'environ 0,77. "
      f"Ce n'est pas une biopsie. C'est un tri.", 5),
    P(f"Exemple. 52 ans, {ASAT} 48, {ALAT} 55, plaquettes 220. Racine de 55 environ 7,4. Dénominateur environ 1 630. Numérateur 2 496. Score environ 1,5. "
      f"Zone intermédiaire. Un contrôle dans trois ans serait la conduite du score sous 1,3, pas de celui-ci.", 5),
    P("Plaquettes : 220 milliards par litre, pas 220 000. La mauvaise unité annule le score.", 5),
]))

p8 = P(f"Le diagnostic positif est : stéatose, au moins un facteur du tableau, alcool en dessous du seuil de la maladie alcoolique, autre cause écartée. "
       f"L'hépatite métabolique, elle, se prouve en histologie. Le {FIB}-4 ne la nomme pas.", 5)
p8w = W("w-pos", "Ce qui est prouvé et ce qui ne l'est pas", "\n".join([
    P(f"Prouvé par l'image et le tableau : la {MASLD}, si l'alcool et les autres causes sont écartés.", 5),
    P(f"Non prouvé par l'{ALAT} : le {MASH}. Il faut le ballonnement et l'inflammation lobulaire.", 5),
    P("Non prouvé par le FIB-4 : le stade exact. Il oriente vers l'élastographie ou vers l'attente active d'un an.", 5),
    P("Stéatose sans aucun facteur : « possible MASLD » si l'on cherche encore l'insulinorésistance, ou cryptogénique si aucune cause n'apparaît. Ce n'est pas le même mot.", 5),
]))

p9 = P(f"Échographie ou autre image de stéatose, bilan lipidique, glycémie ou hémoglobine glyquée, tension, numération pour les plaquettes, enzymes. "
       f"La sérologie virale et la saturation du fer viennent si le profil ou la ferritine l'exigent, pas en paquet systématique chez un {FIB}-4 très bas sans autre alerte.", 5)
p9w = W("w-exa", "Examens et ce qu'ils ne disent pas", "\n".join([
    P("L'échographie montre la stéatose quand elle est assez abondante. Elle rate les stéatoses légères. Elle ne stade pas la fibrose."),
    P(f"L'élastographie est le second pas quand le {FIB}-4 le demande. Une hépatite alcoolique surajoutée, une cholestase ou une congestion cardiaque faussent la dureté : "
      f"la recommandation alcool de 2018 le dit pour une {ASAT} au-dessus de 100 U/l. On ne transpose pas un chiffre de dureté au milieu d'une cytolyse aiguë.", 4, 5),
    P("La biopsie reste l'outil quand le non-invasif ne tranche pas, ou quand une autre maladie est plausible. Elle n'est pas le premier geste d'une enzyme à une fois et demie la limite."),
    P("Le dépistage du carcinome concerne la fibrose avancée et la cirrhose, pas toute stéatose de découverte fortuite.", 5),
]))

p10 = P(f"Stable et métabolique : facteurs, alcool, {FIB}-4, puis le chemin qui correspond à la zone. "
        f"Instable, ictère ou pic d'enzymes : on quitte ce diagnostic et l'on reprend l'arbre de la Phase A.", 5)
p10w = W("w-algo", "Pas à pas", "\n".join([
    P("1. Le patient est-il instable, ictérique, fébrile, ou avec un INR qui bouge ? Si oui, ce n'est pas le moment du FIB-4."),
    P("2. Y a-t-il une stéatose, ou seulement une enzyme ? Sans stéatose documentée, on ne pose pas le nom."),
    P("3. Combien de grammes d'alcool, vraiment ? Sous le seuil, au-dessus du seuil MetALD, ou dans la maladie alcoolique. Trois cases.", 5),
    P("4. Au moins un facteur du tableau, en comptant les traitements en cours.", 5),
    P("5. FIB-4. Sous 1,3 ou sous 2,0 après 65 ans : contrôle dans un à trois ans. Entre les deux seuils : deux chemins. Au-dessus de 2,67 : second test maintenant.", 5),
    P("6. Autre cause si le terrain est pauvre, si le patient est jeune, ou si les enzymes sont disproportionnées.", 5),
]))

p11 = P(f"En Suisse, il n'y a pas dans les informations lues de ce lot une spécialité dont la dose traiterait la {MASLD}. "
        f"La conduite lue est le poids, le diabète, la tension et les lipides, pendant l'année d'observation quand le {FIB}-4 est intermédiaire, et l'adressage si le score est haut. "
        f"On ne recopie pas une dose de médicament métabolique qui n'a pas été lue.", 5)
p11w = W("w-pec", "Prise en charge sans dose inventée", "\n".join([
    P("Perte de poids et activité : c'est le fond du texte de 2024 pour le terrain, pas un médicament nommé avec des milligrammes dans l'extrait lu.", 5),
    P("Diabète, tension au moins 130/85 ou déjà traitée, triglycérides au moins 1,7 mmol/l, HDL bas : on traite ces cibles pour elles-mêmes. "
      "Le bénéfice cardiovasculaire dépasse souvent le bénéfice hépatique. Les doses des antidiabétiques et des statines sont celles de leur information suisse le jour de la prescription, pas une dose de ce cours.", 5),
    P(f"L'acide ursodésoxycholique, {A('information professionnelle','AIPS')} Ursofalk numéro 60812, n'a pas la {MASLD} comme indication. On ne l'ajoute pas pour faire baisser une {GGT}.", 12),
    P(f"Si une cirrhose est déjà là, le Child-Pugh A, B et C et le score de maladie hépatique terminale reprennent leurs droits, comme dans la Phase A. "
      f"La {MASLD} n'a pas son propre Child-Pugh.", 8, 9),
    P("MetALD : les recommandations de prise en charge de la MASLD ne s'étendent pas à cette sous-classe. On le dit au patient, on ne fait pas semblant.", 5),
]))

p12 = P("Pas de dépistage de population. On profite du diabète, de l'obésité et de l'enzyme déjà prescrite pour calculer le FIB-4, pas pour multiplier les échographies de confort.", 5)
p12w = W("w-prev", "Prévention", "\n".join([
    P("Le texte de 2024 déconseille le dépistage de la stéatose dans la population générale.", 5),
    P("Il recommande le repérage de la fibrose dans trois groupes : diabète de type 2 ; obésité abdominale plus un autre facteur ; enzymes qui restent hautes.", 5),
    P("L'alcool se quantifie à chaque visite. Franchir vingt à cinquante grammes chez la femme change le nom de la maladie.", 5),
    P("Les médicaments stéatogènes cités se relisent : corticoïdes, tamoxifène, amiodarone, irinotécan, méthotrexate, lomitapide, valproate, fluorouracil.", 5),
]))

p13 = P(f"Stéatose plus un facteur, alcool quantifié, cinq familles de facteurs, trois zones de {FIB}-4, MetALD à part, pas de dose inventée.", 5)
p13w = W("w-cles", "À pouvoir réciter", "\n".join([
    P(f"{FIB}-4 = âge × {ASAT} / (plaquettes × racine de l'{ALAT}). Seuils 1,3 et 2,67, et 2,0 après 65 ans.", 5),
    P("Alcool : MetALD de vingt à cinquante grammes par jour chez la femme et de trente à soixante chez l'homme. Maladie alcoolique au-dessus de cinquante et de soixante.", 5),
    P(f"{IMC} 25, ou 23 si origine asiatique. Tour de taille européen 94 et 80. Pression 130/85. Triglycérides 1,7 mmol/l. {HDL} 1,0 et 1,3.", 5),
    P("Le MASH est histologique. L'enzyme ne le prouve pas.", 5),
]))

p14 = P("Les pièges sont le mauvais seuil d'âge, la mauvaise unité des plaquettes, le MetALD traité comme une MASLD, et le FIB-4 au milieu d'une hépatite aiguë.", 5)
p14w = W("w-pieges", "Pièges d'examen", "\n".join([
    P("Dire « normal » un FIB-4 à 1,5 chez un adulte de 50 ans. C'est la zone du milieu.", 5),
    P("Dire « pathologique » un FIB-4 à 1,8 chez un adulte de 70 ans. Le seuil bas est alors 2,0.", 5),
    P("Calculer le score à 28 ans et rassurer. Avant 35 ans il est peu fiable.", 5),
    P("Oublier « ou traitement » et conclure qu'un diabétique équilibré n'a pas de facteur.", 5),
    P("Appeler MASLD une consommation de quarante grammes par jour chez une femme. C'est MetALD. Les conseils ne se copient pas.", 5),
    P(f"Rassurer sur une {ALAT} normale alors que les plaquettes sont à 90. Le score peut être haut. L'enzyme n'est pas la fibrose.", 5),
])) + W("w-cas", "Cas d'examen fédéral, corrigé", "\n".join([
    P(f"<b>Énoncé.</b> Femme de 58 ans, ménopausée, indice de masse corporelle à 31, tour de taille 96 cm, pression 138/88 mmHg sans traitement, "
      f"hémoglobine glyquée à 44 mmol/mol, triglycérides 2,1 mmol/l, {HDL} 1,1 mmol/l. "
      f"Elle boit deux verres de vin par jour, qu'elle estime à environ vingt grammes. "
      f"{ALAT} 46 U/l ({LSN} 35), {ASAT} 52 U/l, plaquettes 150 milliards par litre, phosphatase normale, échographie stéatosique. "
      f"Pas de médicament nouveau. Que nommez-vous, que calculez-vous, que faites-vous dans l'année ?"),
    P(f"<b>Nom.</b> Stéatose : oui. Facteurs : corpulence, tour de taille européen au-dessus de 80 cm, pression au-dessus de 130/85, prédiabète "
      f"(44 mmol/mol est entre 39 et 47), triglycérides au-dessus de 1,7. Le {HDL} à 1,1 mmol/l n'est pas sous 1,3 : ce facteur-là manque, les autres suffisent. "
      f"Alcool estimé à vingt grammes par jour : c'est la borne basse de MetALD chez la femme (vingt à cinquante grammes), pas encore la maladie alcoolique (plus de cinquante). "
      f"La copie juste dit MetALD, ou au minimum « à la frontière, ne pas appliquer tels quels les conseils de la {MASLD} ». "
      f"Appeler cela une simple {MASLD} perd le sur-risque lu.", 5),
    P(f"<b>Score.</b> 58 × 52 / (150 × racine de 46). Racine de 46 environ 6,8. Dénominateur environ 1 020. Numérateur 3 016. Score environ 3,0. "
      f"Au-dessus de 2,67. Le second test, élastographie, ne s'attend pas un an. Elle a moins de 65 ans : le seuil 2,0 ne la concerne pas. "
      f"Elle a plus de 50 ans et elle est ménopausée : le texte la place dans le groupe à risque de fibrose progressive, ce qui renforce l'adressage, il ne change pas la formule.", 5),
    P("<b>Ce qui ferait perdre les points.</b> Proposer un dépistage de population à partir de ce cas. Prescrire l'acide ursodésoxycholique pour la GGT. "
      "Calculer un Maddrey. Donner le grade III de Tokyo. Oublier l'alcool parce que « deux verres, ce n'est rien ».", 5, 12),
    P("<b>Conduite de l'année.</b> Poids, glycémie, tension, lipides, arrêt ou forte baisse de l'alcool, élastographie maintenant, puis suivi selon le stade. "
      "Pas de milligrammes de médicament hépatique inventés.", 5),
]))

from profondeur_dx1 import fenetres
p14w = p14w + fenetres()

sources = [
    f"PROFILES 2023, F2.11.{S(1)}",
    f"{EASL}, {A('European Association for the Study of Diabetes','EASD')} et {A('European Association for the Study of Obesity','EASO')}, MASLD, 2024 : définition, facteurs, FIB-4, sous-classes.{S(5)}",
    f"{EASL}, maladie alcoolique, 2018 : dureté du foie faussée si l'ASAT dépasse 100 U/l.{S(4)}",
    f"Ursofalk, information 60812 : pas l'indication de cette stéatose.{S(12)}",
    f"Formules de MELD, 2010, seulement si la cirrhose est déjà là.{S(8)}",
    f"Child-Pugh, 1964 et 1973, seulement si la cirrhose est déjà là.{S(9)}",
]

sections = [
    ("c", "Définition", p1, p1w),
    ("v", "Épidémiologie", p2, p2w),
    ("c", "Physiopathologie", p3, p3w),
    ("v", "Démarche diagnostique", p4, p4w),
    ("c", "Anamnèse et drapeaux rouges", p5, p5w),
    ("v", "Examen physique", p6, p6w),
    ("c", "Approche syndromique", p7, p7w),
    ("v", "Diagnostic positif", p8, p8w),
    ("c", "Examens complémentaires", p9, p9w),
    ("v", "Arbre décisionnel", p10, p10w),
    ("c", "Prise en charge en Suisse", p11, p11w),
    ("v", "Prévention", p12, p12w),
    ("c", "Points clés", p13, p13w),
    ("v", "Pièges d'examen", p14, p14w),
]
html = page(
    "LOT_159_Phase_B_V0_DX.1",
    "Stéatose hépatique liée à un dysfonctionnement métabolique",
    sous, essentiel, sections, sources,
)
p = ecrire("LOT_159_Phase_B_V0_DX.1.html", html)
print(p, p.stat().st_size)
