#!/usr/bin/env python3
"""DX.10 Insuffisance hépatique aiguë."""
from base_dx import P, W, construire, A
from moteur import S

EASL = A("European Association for the Study of the Liver", "EASL")
INR = A("international normalized ratio", "INR")
ALAT = A("alanine aminotransférase", "ALAT")
AIPS = A("information professionnelle", "AIPS")

def F(point, ident, titre, textes, *refs):
    return point, W(ident, titre, "\n".join(P(t, *refs) for t in textes))

fen = []
fen.append(F(1, "d10", "Définition", [
    f"L'insuffisance hépatique aiguë est une maladie du foie qui n'était pas cirrhotique, avec des enzymes aiguës, une coagulopathie en général un {INR} au-dessus de 1,5, et une encéphalopathie clinique.",
    f"Trois exceptions : une hépatite auto-immune, un Budd-Chiari, une maladie de Wilson peuvent se présenter ainsi alors que le foie était déjà malade. On ne les exclut pas de la définition.",
    f"Le nouveau-né et le très jeune enfant peuvent ne pas montrer d'encéphalopathie. La recommandation demande alors un {INR} au-dessus de 4. On ne exige pas le trouble de conscience à cet âge.",
], 3))
fen.append(F(3, "ph10", "Physiopathologie", [
    "Les hépatocytes meurent vite. Le foie ne fabrique plus les facteurs. L'INR s'allonge. L'ammoniaque et d'autres toxiques ne sont plus épurés : la vigilance baisse. Le rein et le poumon suivent souvent.",
    "La cause change le délai et le score de transplantation, pas le fait que l'on commence les mesures de soutien avant le nom de la cause. On n'attend pas la biopsie pour remplir, ventiler, appeler.",
], 3))
fen.append(F(3, "et10", "Causes, sans en retirer", [
    "Antalgique en dose toxique. Virus aigu. Médicament idiosyncrasique. Ischémie : enzymes très hautes, lacticodéshydrogénase, créatinine, chute si la pression revient. Hépatite auto-immune, Budd-Chiari, Wilson, les trois exceptions. Obstacle infecté si l'image le montre : alors Tokyo, pas seulement ce score. Grossesse : stéatose aiguë et hématome, à ne pas inventer ici au-delà du renvoi.",
    "Cause indéterminée : elle compte dans les critères hors antalgique, elle n'est pas un échec de copie si on l'a cherchée.",
], 3, 18))
fen.append(F(8, "k1", "Critères de King, forme avec antalgique", [
    "Trois portes, une seule suffit. Porte du pH : pH artériel inférieur à 7,3 après le remplissage, et plus de 24 heures après la prise. Un gaz trop tôt ne coche pas.",
    "Porte du lactate : au-dessus de 3 mmol/l. Elle ne demande pas le délai de 24 heures.",
    f"Porte des trois critères réunis, les trois, pas deux : encéphalopathie au-dessus du grade 3, créatinine au-dessus de 300 µmol/l, {INR} au-dessus de 6,5.",
    f"L'{INR} au-dessus de 6,5 ne suffit pas seul dans cette forme. Cette suffisance appartient à l'autre forme.",
], 3))
fen.append(F(8, "k2", "Critères de King, forme sans antalgique", [
    f"Soit l'{INR} dépasse 6,5 à lui seul. Soit trois critères parmi cinq : cause indéterminée ou médicament, âge inférieur à 10 ans ou supérieur à 40 ans, plus de 7 jours entre l'ictère et l'encéphalopathie, bilirubine au-dessus de 300 µmol/l, {INR} au-dessus de 3,5.",
    f"Deux critères sur cinq ne suffisent pas. L'{INR} au-dessus de 3,5 compte dans la liste. Il ne remplace pas le seuil de 6,5 qui, lui, suffit seul.",
    "L'âge de 38 ans n'est ni inférieur à 10 ni supérieur à 40. Il ne coche pas. 41 ans coche. 9 ans coche.",
], 3))
fen.append(F(8, "cl10", "Clichy, en plus, pas à la place", [
    "Encéphalopathie de stade 3 ou 4, et facteur V inférieur à 20 % si l'âge est inférieur à 30 ans, ou inférieur à 30 % si l'âge est supérieur à 30 ans.",
    "Avant 30 ans, 25 % est au-dessus de 20 % : le critère de facteur n'est pas rempli. Après 30 ans, 25 % est en dessous de 30 % : il est rempli. L'âge se calcule.",
    "La recommandation discute la transplantation si King ou Clichy est rempli. L'un n'efface pas l'autre.",
], 3))
fen.append(F(11, "nac10", "Acétylcystéine, information 31954, et la recommandation de 2017", [
    f"Quand la coagulopathie et les aminotransférases sont déjà là, la recommandation de 2017 donne l'acétylcystéine même si le dosage de l'antalgique est négatif. Un dosage négatif n'efface pas une prise ancienne.",
    f"{AIPS} Fluimucil 20 %, numéro 31954. Dose totale 300 mg/kg sur 21 heures. Bolus 150 mg/kg en 60 minutes dans du glucose à 5 % ou du chlorure de sodium à 0,9 %. Puis 50 mg/kg sur 4 heures, soit 12,5 mg/kg par heure. Puis 100 mg/kg sur 16 heures, soit 6,25 mg/kg par heure.",
    "Si l'encéphalopathie persiste, on poursuit la dernière perfusion, 150 mg/kg par 24 heures, jusqu'à ce qu'elle disparaisse. Ce n'est pas un second bolus d'une heure.",
    "Poids inférieur à 40 kg : surcharge liquidienne, on lit la notice. L'antidote lui-même peut allonger le temps de prothrombine. On ne conclut pas à l'aggravation sur ce seul chiffre.",
    "Ce schéma n'est pas celui de l'hépatite alcoolique ni celui d'une loi de Hy due à un antibiotique.",
], 3, 11))
fen.append(F(4, "de10", "Démarche", [
    f"Conscience, {INR}, créatinine, lactate, gaz du sang, bilirubine, âge, délai entre ictère et confusion, cause. Puis la bonne forme de King, puis Clichy si le facteur V est là.",
    "En même temps : remplir, glucose, appel du centre si une porte est ouverte ou si elle s'en rapproche. La cause se cherche sans retarder l'appel.",
], 3))
fen.append(F(5, "an10", "Anamnèse", [
    "Heure de la prise, médicaments, plantes, voyage, grossesse, douleur thoracique ou choc récent, jeune âge ou plus de 40 ans. L'heure manquante ne rassure pas : elle empêche le graphique, pas le traitement.",
], 3, 10))
fen.append(F(6, "ex10", "Examen", [
    "Vigilance, asterixis, ictère, pression, marbrures, diurèse. Le grade d'encéphalopathie se note. Au-dessus du grade 3, il entre dans la porte des trois critères de la forme avec antalgique, et le stade 3 ou 4 entre dans Clichy.",
], 3))
fen.append(F(7, "sy10", "Syndromes", [
    "Hyperaigu après un antalgique. Subaigu avec un long délai entre ictère et confusion, qui coche un critère hors antalgique si ce délai dépasse 7 jours. Ischémie avec chute rapide des enzymes. Wilson ou auto-immunité qui entrent dans la définition malgré le passé.",
], 3))
fen.append(F(9, "la10", "Examens", [
    f"{INR}, facteur V, créatinine, lactate artériel, gaz, bilirubine, enzymes, lacticodéshydrogénase, toxique, virus, échographie pour le flux et l'obstacle. Le facteur V sert à Clichy. L'{INR} sert à King. On ne les remplace pas l'un par l'autre.",
], 3))
fen.append(F(10, "ar10", "Arbre", [
    "Cause antalgique : trois portes, une suffit, l'INR seul ne suffit pas. Cause autre : INR au-dessus de 6,5 suffit, ou trois sur cinq. Clichy en parallèle selon l'âge et le facteur V.",
    "Image d'obstacle et fièvre : Tokyo, grades I à III, plaquettes comprises. Enzymes massives après un choc, sans encéphalopathie : traiter le choc, surveiller, ne pas appeler une transplantation sur l'enzyme seule.",
    "Nouveau-né, pas de trouble visible, INR au-dessus de 4 : la définition est remplie. On n'attend pas l'asterixis.",
], 3, 18))
fen.append(F(12, "pv10", "Après", [
    "Si le patient survit sans greffe, la cause se prévient : ordonnance de l'antalgique, plantes, suivi de l'auto-immunité. Ce fichier ne récite pas un calendrier de greffe qui n'a pas été extrait ligne à ligne.",
], 3))
fen.append(F(13, "cl10b", "Points de la copie", [
    "Définition avec les trois exceptions et l'INR au-dessus de 4 chez le tout-petit. Deux formes de King, toutes les portes. Clichy avec 20 % et 30 % selon l'âge. Schéma 31954 si coagulopathie et aminotransférases, même dosage négatif. Une porte ne se substitue pas à l'autre.",
], 3, 11))
fen.append(F(14, "pi10", "Pièges", [
    "Coter le pH avant 24 heures. Accepter deux critères sur trois. Utiliser l'INR au-dessus de 6,5 comme porte unique dans la forme avec antalgique. Oublier les trois exceptions. Exiger l'encéphalopathie chez le nouveau-né malgré un INR au-dessus de 4. Lire l'allongement du temps de prothrombine sous antidote comme un échec. Appliquer le schéma 31954 à une hépatite alcoolique.",
], 3, 4, 11))
fen.append(F(14, "cas10", "Cas corrigé", [
    f"Femme de 44 ans, pas d'antalgique en cause, médicament hépatotoxique, ictère depuis 10 jours, confusion depuis ce matin, bilirubine 320 µmol/l, {INR} 3,8, créatinine normale. Cause médicament : 1. Âge supérieur à 40 : 1. Délai au-dessus de 7 jours : 1. Bilirubine au-dessus de 300 : 1. {INR} au-dessus de 3,5 : 1. Cinq critères, il en fallait trois. King rempli. L'{INR} n'est pas au-dessus de 6,5, donc ce n'est pas la porte unique, c'est la liste. On appelle.",
    f"Homme de 26 ans, prise d'antalgique datée, 30 heures plus tard, après remplissage, pH artériel inférieur à 7,3. La porte du pH est ouverte : délai au-dessus de 24 heures et après remplissage. Une seule porte suffit. On appelle. On poursuit le schéma 31954.",
    "Même homme à la sixième heure, même pH. La porte du pH n'est pas ouverte. On remplit, on poursuit l'antidote, on ne coche pas. Si le lactate est déjà au-dessus de 3 mmol/l, cette autre porte, elle, est ouverte sans attendre 24 heures.",
    f"Femme de 22 ans, stade 4, facteur V 18 %. Avant 30 ans la barre est 20 %. 18 % est en dessous. Clichy rempli. À 42 ans, la même valeur serait aussi en dessous de 30 %. À 22 ans avec un facteur V à 25 %, la barre de 20 % n'est pas franchie : Clichy non rempli sur le facteur.",
    f"Nouveau-né, pas de trouble de vigilance perceptible, {INR} 4,5. Au-dessus de 4. La définition est remplie sans encéphalopathie visible. On n'écrit pas « pas d'insuffisance, il est calme ».",
], 3, 11))

LONGS = [
    "La définition demande une coagulopathie, en général un INR au-dessus de 1,5, et une encéphalopathie, et l'absence de cirrhose connue, sauf les trois exceptions. Une enzyme isolée, même à plusieurs milliers, n'est pas l'insuffisance.",
    "Hépatite auto-immune, Budd-Chiari, Wilson : on les nomme. Les retirer de la définition est une amputation. Un Wilson en coma est dans ce fichier et dans le fichier du cuivre.",
    "INR au-dessus de 4 chez le tout-petit remplace l'encéphalopathie que l'on ne voit pas. INR à 3,5 chez un nouveau-né ne remplit pas cette phrase. La borne est 4.",
    "Porte du pH. Inférieur à 7,3. Après remplissage. Plus de 24 heures après la prise. Trois conditions. En manquer une, c'est ne pas cocher. Un pH bas à la sixième heure est un malade grave, pas encore cette porte.",
    "Porte du lactate. Au-dessus de 3 mmol/l. Pas de délai de 24 heures. 3,0 pile n'est pas au-dessus. 3,1 l'est. On écrit le chiffre.",
    "Porte du trio. Grade d'encéphalopathie au-dessus de 3, créatinine au-dessus de 300 µmol/l, INR au-dessus de 6,5. Les trois. Encéphalopathie et INR sans le rein : non. Rein et INR sans le grade : non. Deux sur trois est la faute classique.",
    "Créatinine 300 µmol/l n'est pas la créatinine de Tokyo, environ 177 µmol/l. Un patient à 200 µmol/l peut être en grade III d'angiocholite sans remplir cette porte. Les deux seuils coexistent.",
    "Forme sans antalgique, INR 6,6. Seul, il suffit. On n'exige pas les trois sur cinq. On appelle.",
    "Forme sans antalgique, INR 4,0. Il est au-dessus de 3,5, donc il compte comme un des cinq, pas comme la porte unique. Il faut encore deux autres critères.",
    "Les cinq : cause indéterminée ou médicament, âge hors de 10 à 40 au sens strict inférieur à 10 ou supérieur à 40, délai ictère-confusion au-dessus de 7 jours, bilirubine au-dessus de 300 µmol/l, INR au-dessus de 3,5. On les compte sur les doigts. Trois.",
    "Âge 10 ans pile. Inférieur à 10 ne l'inclut pas. 40 ans pile : supérieur à 40 ne l'inclut pas. 9 ans et 41 ans cochent. On ne arrondit pas.",
    "Délai de 7 jours pile. Au-dessus de 7 est exigé. 7 ne coche pas. 8 coche. Le premier jour de l'ictère et le premier jour de la confusion se datent.",
    "Bilirubine 300 µmol/l pile. Au-dessus de 300. L'égalité ne coche pas. 310 coche. On ne convertit pas ce seuil : il est déjà en µmol/l. Le multiplier par 17,1 invente un chiffre absurde.",
    "Clichy, stade. 3 ou 4. Un stade 2 ne suffit pas, même avec un facteur V effondré. On note le stade, pas « un peu confus ».",
    "Clichy, 30 ans pile. La barre de 20 % est pour l'âge inférieur à 30. La barre de 30 % est pour l'âge supérieur à 30. À 30 ans, on dit la borne du texte sans inventer un troisième pourcentage. On calcule l'âge exact.",
    "Facteur V 20 % avant 30 ans. Inférieur à 20 est exigé. 20 % ne suffit pas. 19 % oui. Après 30 ans, inférieur à 30 : 30 % ne suffit pas, 29 % oui.",
    "King rempli et Clichy non, ou l'inverse. Une seule des deux discussions de transplantation suffit à appeler. On ne exige pas les deux.",
    "Schéma 31954. Trois temps, 60 minutes, 4 heures, 16 heures. Total 300 mg/kg sur 21 heures. Poursuite 150 mg/kg par 24 heures si la conscience ne revient pas. Solvants : glucose à 5 % ou chlorure de sodium à 0,9 %.",
    "Dosage négatif. On ne arrête pas l'antidote. La recommandation de 2017 le dit quand la coagulopathie et les aminotransférases sont là. La prise peut être ancienne.",
    "Allongement du temps de prothrombine par l'antidote. On prévient l'équipe. On suit la conscience, le lactate, la créatinine. On ne stoppe pas la perfusion sur ce seul temps.",
    "Poids 35 kg. La notice avertit la surcharge. On ne concentre pas au jugé. On ne diminue pas la dose d'antidote pour « faire moins de volume » sans lire.",
    "Antibiotique et loi de Hy, conscience claire, INR normal. Pas ce fichier. Pas le schéma 31954. L'antidote n'est pas un traitement de toute enzyme.",
    "Hépatite alcoolique. Maddrey, Glasgow, Lille. Pas le bolus de 150 mg/kg. Les deux maladies peuvent jaunir. Le score décide lequel.",
    "Ischémie. Enzymes très hautes, lacticodéshydrogénase, créatinine, chute après retour de la pression. Si l'INR reste normal et la conscience claire, ce n'est pas encore l'insuffisance. Si l'INR passe au-dessus de 1,5 et que la vigilance baisse, ce fichier s'ouvre.",
    "Obstacle. Fièvre, dilatation, plaquettes, Tokyo. Un grade III n'est pas automatiquement King. On draine. Si l'encéphalopathie et l'INR de King sont aussi là, on fait les deux raisonnements, on ne les fond pas.",
    "Auto-immune en insuffisance. Score de Hennes en parallèle, souvent incomplet le premier soir. King ne l'attend pas. Les exceptions de la définition sont faites pour ce cas.",
    "Wilson en insuffisance. Leipzig en parallèle. Anneau absent une fois sur deux dans la forme hépatique. On n'écarte pas. On appelle si King ou Clichy est là.",
    "Hémochromatose. Une ferritine haute de nécrose n'est pas une saignée d'urgence. La saturation du matin viendra plus tard. Ce fichier d'abord.",
    "Virus A ou E. Ils peuvent donner cette insuffisance. Pas d'analogue par principe. Soutien, King, Clichy. Le virus B se discute avec le centre, sans inventer une dose qui n'est pas l'objet de ce soir.",
    "Graphique. Il commence à 4 heures. Ligne de 1975 à 200 µg/ml, ligne de 1981 à 150 µg/ml. Avant 4 heures, on ne place pas le point. Conscience altérée ou heure inconnue : on ne se fie pas au graphique seul, on traite.",
    "150 µg/ml n'est pas 150 mg/kg. Concentration d'un côté, bolus de l'autre. La copie qui les égale a perdu l'unité.",
    "La copie minimale. Définition cochée, bonne forme de King, portes comptées, Clichy si le facteur est là, schéma 31954 oui ou non avec la raison, appel oui ou non. Cinq éléments.",
    "La copie qui perd les points. « INR haut, on greffe ». Sans le seuil. « pH bas » à la sixième heure coché. « Deux sur trois, ça suffit ». « Nouveau-né calme, pas d'insuffisance » avec un INR à 4,5. « Antidote pour l'alcool ». Chacune suffit à baisser la note.",
    "Lettre au centre. Âge, cause suspectée, heure de la prise si antalgique, INR, facteur V, créatinine, lactate, pH et son heure, bilirubine, délai ictère-confusion, stade de conscience, schéma commencé ou non. Une lettre sans INR n'est pas un appel.",
]

PROF = [
    "Le nom de l'antalgique de ce chapitre est le paracétamol. On le dit. Le graphique et le schéma ne se confondent pas pour autant : l'un est une concentration à partir de la quatrième heure, l'autre est une perfusion. Les écrire dans la même phrase sans unité est la faute.",
    "Heure connue, au-delà de 4 heures, concentration au-dessus de la ligne de traitement de 1981, à 150 µg/ml à la quatrième heure : on perfuse. La ligne de 1975, à 200 µg/ml, reste citée. On ne traite pas seulement ceux qui dépassent 200.",
    "Heure inconnue et confusion : le graphique ne se lit pas seul. On perfuse. On date. On ne rassure pas la famille avec un prélèvement trop tôt.",
    "Conscience claire, heure connue, concentration sous la ligne de 1981, INR normal : on ne perfuse pas « par précaution » au-delà de ce que l'information indique pour une concentration sous la ligne. On surveille. Si l'INR s'allonge ensuite et que les enzymes sont hautes, la recommandation de 2017 rouvre la perfusion même si un dosage tardif est négatif.",
    "Porte du pH, récit. Prise à 8 heures, gaz à 15 heures, pH artériel inférieur à 7,3, remplissage pas encore fait. Deux conditions manquent : le délai de 24 heures et le remplissage. On remplit. On ne coche pas. On refait le gaz demain matin.",
    "Même patient, lendemain 10 heures, remplissage fait, pH artériel toujours inférieur à 7,3. Plus de 24 heures. Porte ouverte. Appel. Une seule porte suffit dans la forme liée au paracétamol.",
    "Lactate à 2,8 mmol/l. Pas au-dessus de 3. Porte fermée. On ne l'arrondit pas à 3. On le redose. S'il passe à 3,2, la porte s'ouvre sans regarder l'heure de la prise.",
    "Trio incomplet, récit. Grade 4, INR 8, créatinine 140 µmol/l, paracétamol en cause. Il manque la créatinine au-dessus de 300 µmol/l. Le trio est fermé. L'INR à 8 ne suffit pas dans cette forme. S'il n'y a ni pH ni lactate au-dessus du seuil, King n'est pas rempli. On continue le soutien et on surveille le rein : il peut encore monter.",
    "Trio complet, récit. Grade 4, créatinine 420 µmol/l, INR 7,2. Les trois sont là. Ouvert. On appelle. On ne demande pas en plus le pH.",
    "Forme sans paracétamol, récit d'INR. INR 7,1, hépatite aiguë virale, confusion. La porte unique est ouverte. On n'exige pas l'âge ni la bilirubine. On appelle.",
    "Forme sans paracétamol, récit de liste courte. Âge 28 ans, délai 2 jours, bilirubine 80 µmol/l, INR 2,0, cause virus. Aucun des cinq n'est là : l'âge est entre 10 et 40, le délai est court, la bilirubine est sous 300, l'INR est sous 3,5, la cause n'est ni indéterminée ni médicamenteuse. King non rempli. On surveille de très près, on ne dit pas « pas grave » : la définition d'insuffisance peut être là sans que la porte de greffe le soit.",
    "Liste qui se complète dans la nuit. Le matin, seulement la cause médicamenteuse. Le soir, la bilirubine passe à 340 µmol/l et l'âge est 46 ans. Trois critères. La porte s'ouvre en cours de séjour. On rappelle le centre. Le premier appel négatif n'est pas un acquis.",
    "Clichy, récit jeune. 19 ans, stade 4, facteur V 15 %. Inférieur à 20 %. Ouvert. On appelle même si King de la forme sans antalgique n'est pas encore complet.",
    "Clichy, récit qui rate d'un point. 19 ans, stade 4, facteur V 22 %. 22 n'est pas inférieur à 20. Fermé. On ne l'appelle pas ouvert « parce que c'est proche ». On surveille le facteur, il peut encore baisser.",
    "Clichy, récit adulte. 55 ans, stade 3, facteur V 27 %. Inférieur à 30 %. Ouvert. Le même 27 % à 19 ans n'aurait pas suffi. L'âge est le premier mot de la phrase.",
    "Exceptions, récit auto-immun. Jeune femme, INR 6,9, confusion, pas de cirrhose connue au dossier, anticorps en cours. La porte unique hors paracétamol est ouverte par l'INR. L'hépatite auto-immune reste dans la définition. On appelle et l'on cote Hennes quand les résultats arrivent, pas avant.",
    "Exceptions, récit Wilson. Homme de 18 ans, hémolyse, INR 3,2, stade 4, facteur V 12 %. Clichy ouvert avant 30 ans. L'anneau peut manquer. On ne retient pas l'appel pour chercher l'anneau.",
    "Exceptions, récit Budd-Chiari. Douleur, ascite aiguë, veines sus-hépatiques thrombosées, INR au-dessus de 1,5, confusion. La définition l'accepte. L'imagerie fait le diagnostic de cause. King se calcule sur la forme sans antalgique.",
    "Ischémie, récit. Hypotension documentée, alanine à plusieurs milliers, lacticodéshydrogénase haute, créatinine doublée, INR 1,0, réveil normal, enzymes en chute à H12. Pas la définition. Pas d'appel de greffe. On traite le choc. Si l'INR passe à 2 et que la vigilance baisse, on reprend ce fichier.",
    "Obstacle, récit. Angiocholite grade III sur les plaquettes à 80 000/mm³, INR 1,4, conscience claire. Tokyo oui, King non : l'INR n'est pas au-dessus de 1,5 pour la définition, et aucune porte de King n'est là. On draine. On ne dit pas insuffisance aiguë pour obtenir un lit de réanimation hépatique.",
    "Alcool, récit. Ictère, Maddrey au-dessus de 32, Glasgow haut, pas de confusion, pas d'INR à 6,5. Fichier de l'hépatite alcoolique. Le schéma en trois perfusions n'est pas le corticoïde. On ne les échange pas.",
    "Tout-petit, récit. Nourrisson, INR 5, pas d'asterixis perceptible. Au-dessus de 4. Définition remplie. On n'écrit pas « vigilance normale, donc pas d'insuffisance ». On appelle la filière pédiatrique.",
    "Tout-petit, INR 3,6. Pas au-dessus de 4. Cette phrase de la définition ne suffit pas. S'il n'y a pas d'encéphalopathie visible, on ne force pas le diagnostic sur ce seul chiffre. On surveille d'heure en heure.",
    "Lettre modèle. « Femme de 44 ans, cause médicamenteuse, pas de paracétamol, délai 10 jours, âge supérieur à 40, bilirubine 320 µmol/l, INR 3,8 : au moins trois des cinq, King rempli, Clichy en attente du facteur V, appel maintenant. » Une phrase, la décision dedans.",
    "Lettre modèle antalgique. « Homme, prise datée, H30, pH artériel inférieur à 7,3 après remplissage : porte ouverte, perfusion selon 31954 en cours, appel. » On ne demande pas le trio en plus.",
    "Ce que l'on ne retire pas. Les trois exceptions. L'INR au-dessus de 4 du tout-petit. Les trois portes de la forme avec paracétamol, y compris l'exigence des trois critères du trio. Les cinq items de l'autre forme et le trois sur cinq. L'INR au-dessus de 6,5 seul dans cette autre forme seulement. Clichy, 20 % et 30 %. Le schéma même si le dosage est négatif. En retirer un change la greffe.",
    "Ordre de la copie quand tout est vrai en même temps. D'abord la porte qui décide de l'appel : pH, lactate, trio, ou INR au-dessus de 6,5, ou trois sur cinq, ou Clichy. Ensuite la cause. Ensuite le schéma de perfusion s'il s'agit du paracétamol ou d'une coagulopathie avec enzymes hautes. Mettre le nom de la cause avant de dire si l'on appelle est une copie qui décrit sans décider.",
    "Deux patients, même INR à 4. Le premier a pris du paracétamol : 4 n'ouvre ni le trio ni une porte unique, il faut le pH, le lactate ou les trois critères. Le second n'en a pas pris : 4 est au-dessus de 3,5, donc un item de la liste, pas une porte seule. Le même chiffre, deux grammaires. On nomme la forme avant de conclure.",
    "Deux patients, même facteur V à 25 %. 19 ans : pas inférieur à 20 %, Clichy fermé. 45 ans : inférieur à 30 %, Clichy ouvert si le stade est 3 ou 4. L'âge n'est pas une décoration du dossier.",
    "Deux patients, même lactate à 3,6 mmol/l. S'il y a du paracétamol, la porte est ouverte quelle que soit l'heure. S'il n'y en a pas, le lactate n'est pas une porte de King de cette forme. On ne transporte pas la porte.",
    "Dosage tardif négatif, enzymes encore hautes, INR 2,4, confusion légère. On perfuse selon l'information 31954. On ne dit pas « trop tard, le dosage est vide ». La recommandation de 2017 a prévu ce cas. L'heure de début de la perfusion se note.",
    "Temps de prothrombine qui s'allonge sous perfusion, conscience qui s'améliore, lactate qui baisse. On continue. L'antidote peut allonger le temps. L'amélioration clinique prime sur ce chiffre isolé. L'équipe de nuit est prévenue pour ne pas arrêter.",
    "Temps de prothrombine qui s'allonge, conscience qui s'aggrave, lactate qui monte. Là, on ne met pas tout sur l'antidote. On refait King. Une porte peut s'ouvrir pendant la perfusion. L'appel part.",
    "Cause encore inconnue à la sixième heure, INR 7, confusion. La cause inconnue est un des cinq, et l'INR au-dessus de 6,5 suffit déjà seul dans la forme sans paracétamol. On n'attend pas le nom du virus pour appeler. On prie les sérologies en parallèle.",
    "Grossesse. Une insuffisance au troisième trimestre a ses causes propres. Ce fichier ne les détaille pas au-delà du renvoi, parce que l'extrait lu ne les chiffre pas. On appelle la filière obstétricale et hépatique. On ne pose pas un score de King « comme chez l'adulte de ville » sans le dire.",
    "Après la greffe ou la survie. La cause se écrit dans le courrier de sortie. Paracétamol : éducation sur les boîtes cumulées. Auto-immunité : le score et le traitement de son fichier. Wilson : traitement à vie. On ne ferme pas le dossier le jour où l'INR revient à 1.",
    "Ce que la copie finale doit pouvoir être lue à voix haute en trente secondes. Forme. Porte ouverte ou fermée, avec le chiffre. Clichy oui, non, ou en attente du facteur. Perfusion oui ou non, et pourquoi. Appel oui ou non. Cinq mots de décision. Le reste est le commentaire.",
    "Grade d'encéphalopathie. Au-dessus du grade 3 veut dire 4 dans l'échelle habituelle, pas « plutôt agité ». On nomme le grade. Un grade 3 pile n'est pas au-dessus de 3 : le trio de la forme avec paracétamol n'est pas coché par ce seul mot. Clichy, lui, accepte le stade 3 ou 4. Les deux phrases ne disent pas la même borne. On ne les fond pas.",
    "Créatinine 300 µmol/l pile. Au-dessus de 300 est exigé pour le trio. 300 ne suffit pas. 310 suffit. On ne convertit pas ce seuil en mg/dl pour le comparer à Tokyo sans le dire : 300 µmol/l ne sont pas 2,0 mg/dl. 2,0 mg/dl valent environ 177 µmol/l. Un patient à 200 µmol/l a passé Tokyo et pas King.",
    "Bilirubine 300 µmol/l, déjà dans la bonne unité. On ne la multiplie pas. On ne la compare pas aux 34 µmol/l de Tokyo ni aux 68 et 170 du Child-Pugh de la cholangite biliaire primitive. Quatre usages de la bilirubine, quatre seuils. La copie dit lequel.",
    "INR, quatre usages déjà vus dans le chapitre, rappel pour cette porte. Définition : en général au-dessus de 1,5. Tout-petit : au-dessus de 4. Forme sans paracétamol : au-dessus de 6,5 seul, ou au-dessus de 3,5 dans la liste. Trio : au-dessus de 6,5 mais avec les deux autres critères. Child-Pugh n'est pas l'outil du jour, sauf cirrhose déjà connue, ce que la définition exclut hors les trois exceptions.",
    "pH, trois conditions rappel. Inférieur à 7,3. Après remplissage. Plus de 24 heures après la prise. Un pH normal n'élimine pas les autres portes. Un pH bas trop tôt n'ouvre pas celle-ci. On écrit l'heure du gaz à côté du chiffre.",
    "Facteur V et INR ne se remplacent pas. Clichy veut le facteur et le stade. King veut l'INR. Un INR à 7 avec un facteur V non dosé : King peut être ouvert, Clichy est en attente. On ne invente pas le facteur. On le demande.",
    "Appel même si une seule porte est ouverte. Attendre « d'être sûr des cinq » quand l'INR est déjà au-dessus de 6,5 dans la forme sans paracétamol fait perdre des heures. La recommandation discute la transplantation dès que King ou Clichy est rempli. Discuter n'est pas greffer dans le couloir. C'est téléphoner.",
    "Soutien en attendant le centre. Remplissage, glycémie, protection des voies aériennes si le grade monte, pas de sédation qui masque la conscience. Ce fichier ne donne pas une dose de sédatif. Il dit de ne pas en mettre une qui empêche de coter le stade.",
    "Sortie de la définition. INR revenu sous 1,5, conscience claire, cause identifiée, enzymes en baisse. On quitte l'alerte. On garde la cause : éducation si c'était le paracétamol, autre fichier si c'était Wilson, l'auto-immunité ou l'obstacle. L'alerte finie n'efface pas le diagnostic de cause.",
    "Compte des cinq, à voix haute. Un : cause indéterminée ou médicament. Deux : âge inférieur à 10 ans ou supérieur à 40 ans. Trois : plus de 7 jours entre l'ictère et l'encéphalopathie. Quatre : bilirubine au-dessus de 300 µmol/l. Cinq : INR au-dessus de 3,5. Il en faut trois, ou bien l'INR au-dessus de 6,5 tout seul. Cette liste n'est pas celle de la forme avec paracétamol.",
    "Compte du trio, à voix haute. Encéphalopathie au-dessus du grade 3. Créatinine au-dessus de 300 µmol/l. INR au-dessus de 6,5. Les trois ensemble, dans la forme avec paracétamol. À côté, et suffisantes seules : pH artériel inférieur à 7,3 après remplissage et après 24 heures, ou lactate au-dessus de 3 mmol/l. On ne mélange pas le trio avec ces portes en exigeant les trois plus le pH.",
    "Compte de Clichy, à voix haute. Stade 3 ou 4. Facteur V inférieur à 20 % si l'âge est inférieur à 30 ans, inférieur à 30 % s'il est supérieur à 30 ans. Pas d'INR dans cette phrase. Pas de bilirubine. Le facteur manquant se demande, il ne se devine pas.",
    "Fermeture du fichier. Définition avec trois exceptions et le tout-petit. Deux formes de King, portes entières. Clichy entier. Perfusion 31954 si la coagulopathie et les enzymes sont là, dosage négatif inclus. Appel dès qu'une porte est ouverte. Cinq lignes. La copie qui n'en a que trois a laissé une amputation.",
    "Mémo avant de rendre. Forme avec paracétamol : pH artériel inférieur à 7,3 après remplissage et après 24 heures, ou lactate au-dessus de 3 mmol/l, ou les trois critères ensemble. Forme sans paracétamol : INR au-dessus de 6,5 seul, ou trois critères parmi les cinq. Clichy : stade 3 ou 4 et facteur V selon l'âge, 20 % puis 30 %. Tout-petit : INR au-dessus de 4 même sans trouble visible. Exceptions : hépatite auto-immune, Budd-Chiari, Wilson. Perfusion selon 31954, y compris dosage négatif. Rien de cette liste ne se retire.",
    "Dernière phrase. Une enzyme isolée n'est pas une insuffisance. Une porte incomplète n'est pas un appel. Une porte complète est un appel. Le schéma de perfusion n'est pas un corticoïde. Ces trois négations ferment la copie.",
]
def main():
    fen.append((8, W("w-long10", "Portes, une par une", "\n".join(P(p, 3, 10, 11) for p in LONGS))))
    fen.append((4, W("w-prof10", "Récits de porte", "\n".join(P(p, 3, 4, 11) for p in PROF))))
    rows = [
        ("pH à H30 après remplissage, inférieur à 7,3, antalgique", "porte du pH ouverte", "une suffit"),
        ("pH à H6, inférieur à 7,3, antalgique", "porte du pH fermée", "délai non atteint"),
        ("lactate 3,4 mmol/l, antalgique, H8", "porte du lactate ouverte", "pas de délai de 24 heures"),
        ("lactate 3,0 mmol/l", "non au-dessus de 3", "porte fermée"),
        ("encéphalopathie grade 4, créatinine 310, INR 7, antalgique", "trio complet", "ouvert"),
        ("encéphalopathie grade 4, créatinine 220, INR 7, antalgique", "il manque le rein au-dessus de 300", "trio fermé"),
        ("INR 6,8, pas d'antalgique", "porte unique ouverte", "pas besoin des cinq"),
        ("INR 4,2, âge 50, cause médicament, délai 3 jours, bilirubine 100, pas d'antalgique", "deux critères seulement : médicament et INR au-dessus de 3,5", "il en faut trois"),
        ("âge 41, cause inconnue, délai 9 jours, INR 2, pas d'antalgique", "trois : âge, cause, délai", "ouvert même si l'INR n'est pas au-dessus de 3,5"),
        ("âge 40 pile, pas d'antalgique", "supérieur à 40 non inclus", "cet item tombe"),
        ("âge 10 pile", "inférieur à 10 non inclus", "cet item tombe"),
        ("délai 7 jours pile", "au-dessus de 7 non inclus", "item tombe"),
        ("bilirubine 300 pile", "au-dessus de 300 non inclus", "item tombe"),
        ("22 ans, stade 4, facteur V 18 %", "inférieur à 20", "Clichy ouvert"),
        ("22 ans, stade 4, facteur V 25 %", "25 n'est pas inférieur à 20", "Clichy fermé sur le facteur"),
        ("42 ans, stade 3, facteur V 25 %", "inférieur à 30", "Clichy ouvert"),
        ("42 ans, stade 2, facteur V 10 %", "stade insuffisant", "Clichy fermé"),
        ("nouveau-né, INR 4,5, éveillé", "définition remplie", "pas d'exigence d'encéphalopathie"),
        ("nouveau-né, INR 3,2", "pas au-dessus de 4", "cette phrase ne suffit pas"),
        ("dosage négatif, INR 2,2, ALAT très haute, confusion", "schéma 31954 quand même", "2017"),
        ("INR 1,2, ALAT 4 000, conscience claire", "pas la définition", "pas d'appel de greffe sur l'enzyme"),
        ("choc, enzymes en chute, INR 1,1", "ischémie", "pas King"),
        ("fièvre, dilatation, INR 1,6, plaquettes 90 000", "Tokyo grade III", "drainage, et King seulement si ses portes sont là"),
        ("alcool, Maddrey haut, pas de confusion", "fichier de l'hépatite alcoolique", "pas le bolus"),
    ]
    extra = []
    for titre, lecture, suite in rows:
        extra.append(
            f"{titre}. Lecture : {lecture}. Conséquence : {suite}. "
            f"On nomme la forme, antalgique ou non, avant de compter. "
            f"Une porte de l'autre forme ne se recopie pas."
        )
    fen.append((14, W("w-extra10", "Vingt-quatre lectures de porte", "\n".join(P(p, 3, 11, 18) for p in extra))))
    essentiel = (
        P(f"Définition : enzymes, {INR} en général au-dessus de 1,5, encéphalopathie, pas de cirrhose connue, sauf hépatite auto-immune, Budd-Chiari et Wilson. Tout-petit : {INR} au-dessus de 4 peut suffire.", 3)
        + P("King, deux formes entières. Clichy : 20 % avant 30 ans, 30 % après, avec un stade 3 ou 4. Schéma 31954 si coagulopathie et aminotransférases.", 3, 11)
    )
    phrases = {
        1: "Coagulopathie et encéphalopathie, foie auparavant non cirrhotique, trois exceptions.",
        2: "Pas de prévalence suisse. Au moins 10 % concerne la loi de Hy, pas ce fichier.",
        3: "Nécrose, facteurs qui manquent, vigilance qui baisse. La cause vient en même temps que le soutien.",
        4: "Conscience, INR, lactate, pH daté, créatinine, bilirubine, âge, délai, cause.",
        5: "Heure de la prise, plantes, choc, grossesse. L'heure inconnue ne retarde pas l'antidote.",
        6: "Le stade se note. Il entre dans le trio et dans Clichy.",
        7: "Hyperaigu, délai long, ischémie, ou exception de la définition.",
        8: "Deux formes de King. Une porte suffit dans la sienne. Clichy s'ajoute.",
        9: "Facteur V pour Clichy, INR pour King. Gaz et lactate pour le pH et la deuxième porte.",
        10: "Antalgique : pas d'INR seul. Autre cause : INR au-dessus de 6,5 seul, ou trois sur cinq.",
        11: "31954 en trois temps, poursuite si la conscience reste, même si le dosage est négatif.",
        12: "Prévenir la cause chez celui qui survit. Pas de calendrier inventé.",
        13: "Exceptions, deux formes, 20 et 30 %, schéma même dosage négatif.",
        14: "Deux sur trois ne suffit pas. Le pH de la sixième heure ne coche pas.",
    }
    fiches = {n: P(phrases[n], 3) for n in phrases}
    sources = [
        f"{EASL}, insuffisance hépatique aiguë, Journal of Hepatology, 2017.{S(3)}",
        f"{AIPS} Fluimucil 20 %, Swissmedic 31954.{S(11)}",
        f"Rumack, lignes de 1975 et de 1981, si l'heure de la prise est connue.{S(10)}",
        f"Tokyo Guidelines 2018, si l'image montre un obstacle infecté.{S(18)}",
        f"{EASL}, maladie alcoolique, 2018, pour ne pas y coller le schéma 31954.{S(4)}",
    ]
    sous = (
        f"Diagnostic différentiel DX.10 de {A('situation de départ F2.11 de PROFILES','F2.11')} "
        f"« Enzymes hépatiques anormales ». Texte du 31.10.2026."
    )
    par = {}
    for point, html in fen:
        par.setdefault(point, []).append(html)
    path = construire(10, "Insuffisance hépatique aiguë", essentiel, sous, fiches, par, sources)
    print(path)

if __name__ == "__main__":
    main()
