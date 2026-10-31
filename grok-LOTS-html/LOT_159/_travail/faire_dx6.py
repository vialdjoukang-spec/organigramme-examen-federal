#!/usr/bin/env python3
"""DX.6 Hépatite auto-immune, score simplifié entier."""
from base_dx import P, W, construire, A
from moteur import S

ALAT = A("alanine aminotransférase", "ALAT")
LSN = A("limite supérieure de la normale", "LSN")
EASL = A("European Association for the Study of the Liver", "EASL")
AIPS = A("information professionnelle", "AIPS")
INR = A("international normalized ratio", "INR")
SLA = A("anticorps anti-antigène soluble du foie", "SLA")
PAL = A("phosphatase alcaline", "PAL")
GGT = A("gamma-glutamyltransférase", "GGT")

def sla(t):
    if "SLA</abbr>" in t:
        return t
    return t.replace("SLA", SLA)

def F(point, ident, titre, textes, *refs):
    return point, W(ident, titre, "\n".join(P(sla(t), *refs) for t in textes))

fen = []
fen.append(F(1, "d6", "Définition", [
    f"L'hépatite auto-immune est une inflammation du foie, à prédominance féminine dans les séries, où le système immunitaire entretient une hépatite. Le diagnostic ne se pose pas sur un anticorps isolé. Il se pose avec le score simplifié, ou avec un tableau aigu qui peut encore être négatif.",
    f"Le score de Hennes, Hepatology 2008, repris par l'{EASL} en 2015, a quatre domaines : autoanticorps, immunoglobuline G, histologie, absence d'hépatite virale. On ne retire aucun domaine.",
], 7, 22))
fen.append(F(8, "sc6", "Score simplifié, toutes les lignes", [
    "Autoanticorps, somme plafonnée à 2 points. Antinucléaires ou anti-muscle lisse d'au moins 1/40 : 1 point. Antinucléaires ou anti-muscle lisse d'au moins 1/80, ou anticorps anti-microsomes d'au moins 1/40, ou SLA positif : 2 points. On ne additionne pas 1 et 2 : le plafond est 2.",
    "Immunoglobuline G. Au-dessus de la limite supérieure : 1 point. Au-dessus de 1,10 fois cette limite, c'est-à-dire plus de 10 % au-dessus : 2 points. Une valeur normale vaut 0. Entre la limite et 1,10 fois, c'est 1, pas 2.",
    "Histologie, et une hépatite est nécessaire. Atypique, par exemple une stéatohépatite : 0 point. Compatible, hépatite chronique lymphocytaire sans tous les traits typiques : 1 point. Typique : 2 points. Typique veut dire hépatite d'interface, infiltrat lymphocytaire ou lymphoplasmocytaire portal étendu au lobule, empéripolèse et rosettes.",
    "Absence d'hépatite virale : 2 points. Si un virus explique l'hépatite, ce domaine vaut 0. On ne pose pas le score « quand même » sur un virus A en cours.",
    "Total au moins égal à 6 : probable. Total au moins égal à 7 : certaine. Le tableau et l'EASL 2015 disent au moins 6 et au moins 7. Une phrase de la conclusion de 2008 dit plus de 6 pour le probable et 7 ou plus pour le certain. On enseigne le tableau, et l'on ne cache pas la phrase.",
    "Jeu de validation : sensibilité 88 % et spécificité 97 % au seuil d'au moins 6. Sensibilité 81 % et spécificité 99 % au seuil d'au moins 7. Ce ne sont pas des prévalences suisses.",
], 7, 22))
fen.append(F(8, "ti6", "Titres et forme aiguë", [
    "Chez l'adulte, un titre d'immunofluorescence d'au moins 1/40 est significatif. C'est aussi le premier barreau du score, qui vaut 1 point, pas 2. Le barreau à 2 commence à 1/80 pour les antinucléaires ou le muscle lisse, ou à 1/40 pour les anti-microsomes, ou avec un SLA positif.",
    "Chez l'enfant, l'EASL 2015 retient 1/20 pour les antinucléaires ou le muscle lisse, et 1/10 pour les anti-microsomes, comme titres significatifs. On ne recalcule pas le tableau adulte avec ces titres. On les cite comme le seuil pédiatrique lu, à côté du score.",
    "Environ 85 % des patients ont une immunoglobuline G haute. Environ 25 % débutent de façon aiguë. Dans la forme aiguë, 25 à 39 % ont une immunoglobuline G normale et 9 à 17 % n'ont pas d'autoanticorps. Un bilan négatif n'écarte pas la maladie si le tableau est sévère.",
], 7, 22))
fen.append(F(8, "pa6", "Chevauchement, critères de Paris", [
    f"Avec la cholangite biliaire primitive, au moins deux critères sur trois de chaque maladie. Côté biliaire : {PAL} au moins deux fois la {LSN}, ou {GGT} au moins cinq fois ; anticorps antimitochondries ; lésion floride des canaux.",
    f"Côté hépatite : {ALAT} au moins cinq fois la {LSN} ; immunoglobuline G au moins deux fois la {LSN}, ou anti-muscle lisse ; nécrose parcellaire modérée ou sévère. Un seul côté ne fait pas le chevauchement.",
], 7))
fen.append(F(3, "ph6", "Physiopathologie", [
    "L'hépatocyte est attaqué par une réponse immune qui se perpétue. L'interface entre l'espace porte et le lobule est le lieu de cette attaque : c'est l'hépatite d'interface du score. Les plasmocytes dans l'infiltrat et les rosettes d'hépatocytes en sont les compagnons histologiques, pas des ornements.",
    "L'immunoglobuline G haute est le reflet soluble de cette réponse. Elle manque pourtant chez une minorité, surtout au début aigu. Le score donne alors moins de points, et la clinique garde la main.",
    "Sans traitement, la fibrose avance. Avec traitement, la cible lue est la normalisation de l'immunoglobuline G et de l'alanine aminotransférase. Une enzyme qui baisse à moitié n'est pas encore la cible.",
], 7))
fen.append(F(3, "et6", "Formes, sans en retirer", [
    "Forme classique, femme, enzymes hépatocellulaires, immunoglobuline haute, anticorps, histologie typique : le score dépasse souvent 7.",
    "Forme aiguë ou sévère : immunoglobuline normale dans 25 à 39 % des cas, anticorps absents dans 9 à 17 %. Le score peut rester sous 6 le premier jour. On n'écrit pas « écarté ».",
    "Chevauchement avec la cholangite biliaire primitive : critères de Paris, deux sur trois de chaque côté.",
    "Présentation comme une insuffisance aiguë : l'hépatite auto-immune est l'une des trois maladies chroniques que la recommandation de 2017 accepte dans cette définition, avec le Budd-Chiari et Wilson. L'INR et l'encéphalopathie font alors les critères de King et Clichy, en plus du score.",
], 3, 7, 22))
fen.append(F(4, "de6", "Démarche", [
    f"Enzymes, bilirubine, {INR}, immunoglobuline G avec la limite du laboratoire, antinucléaires, anti-muscle lisse, anti-microsomes, SLA. Sérologies virales, parce que l'absence de virus vaut 2 points et qu'un virus présent change le domaine.",
    "On additionne après, pas avant la biopsie si le score intermédiaire en dépend. Une histologie atypique de stéatohépatite vaut 0. Une hépatite est exigée pour que l'histologie compte.",
    "Au moins 6 : probable, on traite selon le spécialiste dans la fourchette suisse. Au moins 7 : certaine. Sous 6 et tableau aigu sévère : on ne clôt pas.",
], 7, 22))
fen.append(F(5, "an6", "Anamnèse", [
    "Autres maladies auto-immunes, thyroïde, traitement déjà en cours par corticoïde, médicament hépatotoxique à écarter, alcool en grammes dit avec des mots, virus ancien. Une femme jeune n'est pas un critère du score. C'est un contexte.",
    "Grossesse, désir de grossesse : le thiopurique et le corticoïde se discutent avec l'information du produit, pas avec une dose inventée.",
], 7))
fen.append(F(6, "ex6", "Examen", [
    f"Ictère, foie, rate, angiomes, ascite, confusion. Rien de tout cela ne donne de point au score. L'examen cherche la gravité, l'{INR} et la conscience cherchent l'insuffisance. Le score se lit au laboratoire et au microscope.",
], 7))
fen.append(F(7, "sy6", "Syndromes", [
    f"Hépatite chronique fluctuante. Hépatite aiguë à {ALAT} très haute. Insuffisance avec encéphalopathie. Chevauchement cholestatique si la phosphatase domine et que Paris est rempli. Quatre portes, un seul score pour la porte immune.",
], 7))
fen.append(F(9, "la6", "Examens", [
    "Immunoglobuline G quantitative, pas seulement l'électrophorèse qualitative. Titre exact, pas « positif ». Virus A, B, C, E écartés ou non. Biopsie sauf si l'insuffisance la rend dangereuse : on le dit, on ne invente pas un score histologique.",
    f"Échographie pour ne pas manquer un obstacle si R est cholestatique. Le score simplifié n'est pas un outil de dilatation.",
], 7, 22))
fen.append(F(10, "ar6", "Arbre", [
    "Virus présent qui explique le tableau : ce n'est pas ce diagnostic, le domaine viral vaut 0.",
    "Pas de virus, total au moins 7 : certaine. Traitement.",
    "Pas de virus, total 6 : probable. Traitement discuté, pas un refus.",
    "Pas de virus, total 5 ou moins, mais forme aiguë sévère avec les pourcentages lus de bilan négatif : on n'écarte pas. Avis spécialisé, parfois traitement d'épreuve, biopsie si elle est faisable.",
    f"INR au-dessus de 1,5 et encéphalopathie : filière d'insuffisance, critères de King et Clichy, en parallèle du score.",
], 3, 7, 22))
fen.append(F(11, "tx6", "Traitement suisse lu", [
    f"Prednisolone Streuli, {AIPS} 29348. La dose initiale habituelle est 5-60 mg/jour. Les comprimés sont à 5 mg, 20 mg et 50 mg. On ne sort pas un autre chiffre qui n'est pas dans cette information pour ce fichier. Le seuil de Cushing lu est au-dessus de 7,5 mg.",
    f"Imurek, {AIPS} 31887, indique l'hépatite chronique active auto-immune. Hors transplantation, la posologie initiale est généralement de 1 à 3 mg/kg par jour, en une prise ou en deux. En transplantation, le texte va jusqu'à 5 mg/kg puis un entretien de 1 à 3 mg/kg. On ne mélange pas les deux paragraphes.",
    f"La cible {EASL} est la normalisation de l'immunoglobuline G et de l'{ALAT}. Le thiopurique épargne le corticoïde. On ne s'arrête pas à une enzyme « améliorée ».",
    "Aucune dose de ce fichier n'est celle de l'hépatite alcoolique. On ne transporte pas ici une dose dite en toutes lettres pour une autre maladie.",
], 7, 13, 16))
fen.append(F(12, "pv6", "Prévention et suivi", [
    f"Vaccinations discutées avant l'immunosuppression. Surveillance de la numération sous thiopurine, comme l'information 31887 le demande. Contrôle de l'{ALAT} et de l'immunoglobuline G jusqu'à la cible, puis pour dépister la rechute. On ne donne pas de calendrier qui n'est pas dans l'extrait.",
], 7, 16))
fen.append(F(13, "cl6", "Points de la copie", [
    "Quatre domaines. Plafond 2 pour les anticorps. Immunoglobuline : 0, 1 ou 2 selon la limite et 1,10 fois. Histologie 0, 1 ou 2, hépatite exigée. Absence de virus : 2. Au moins 6 probable, au moins 7 certaine. Sensibilités 88 % et 81 %, spécificités 97 % et 99 %.",
    "Doses : 5-60 mg/jour, information 29348. 1 à 3 mg/kg par jour, information 31887. Cible : immunoglobuline et alanine normales.",
], 7, 13, 16, 22))
fen.append(F(14, "pi6", "Pièges", [
    "Additionner 1 et 2 sur les anticorps. Donner 2 points dès 1/40. Donner 2 points d'immunoglobuline dès qu'elle dépasse la limite, sans vérifier 1,10 fois. Oublier que la stéatohépatite vaut 0. Poser le diagnostic avec un virus actif. Écarter la forme aiguë parce que les anticorps manquent. Écrire une dose qui n'est pas dans 29348 ou 31887.",
    "Confondre au moins 6 et plus de 6. Le tableau enseigné est au moins 6. La phrase de conclusion qui dit plus de 6 se mentionne, elle ne remplace pas le tableau.",
], 13, 16, 22))
fen.append(F(14, "cas6", "Cas qui fait au moins 7", [
    f"Femme de 34 ans. {ALAT} à 12 fois la {LSN}, {INR} 1,1, conscience claire. Antinucléaires à 1/160. Immunoglobuline G à 1,4 fois la limite. Biopsie : hépatite d'interface, infiltrat lymphoplasmocytaire, rosettes. Virus A, B, C et E négatifs.",
    "Points. Anticorps : 1/160 est au moins 1/80, donc 2, et le plafond est déjà atteint. Immunoglobuline : 1,4 est au-dessus de 1,10, donc 2. Histologie typique : 2. Pas de virus : 2. Total 8. Au moins 7 : certaine.",
    "Traitement dans les textes suisses : prednisolone dans 5-60 mg/jour, information 29348, et azathioprine en général 1 à 3 mg/kg par jour, information 31887. Cible : immunoglobuline et alanine normales. On n'écrit pas une dose d'une autre maladie.",
    "Variante probable, pas certaine. Antinucléaires à 1/80 (2 points), immunoglobuline juste au-dessus de la limite mais pas au-dessus de 1,10 fois (1 point), histologie compatible sans tous les traits typiques (1 point), pas de virus (2). Total 6. Probable. On ne le reclasse pas en certain pour faire une phrase plus forte.",
    "Variante qui ne ferme pas le dossier. Homme de 28 ans, ALAT à 20 fois la limite, INR 1,8, immunoglobuline normale, aucun anticorps, virus négatifs, biopsie non faite ce soir-là. Le score sérologique est bas : 0 + 0 + histologie inconnue + 2. La forme aiguë autorise 25 à 39 % d'immunoglobuline normale et 9 à 17 % sans anticorps. On n'écrit pas écarté. On appelle, on surveille l'INR, on discute la biopsie.",
], 3, 7, 13, 16, 22))

LONGS = [
    "Le plafond de 2 sur les anticorps se vérifie avec un exemple. Antinucléaires à 1/160 (ce serait 2) et anti-microsomes à 1/80 (ce serait aussi 2) ne font pas 4. Le domaine vaut 2. L'addition naïve est la faute la plus simple.",
    "1/40 d'antinucléaires vaut 1, pas 2. Le saut à 2 se fait à 1/80. Un titre « positif » sans chiffre ne se cote pas. On redemande le titre.",
    "1/40 d'anti-microsomes vaut déjà 2. Ce n'est pas le même barreau que les antinucléaires. Copier 1/80 sur les anti-microsomes sous-cote le patient.",
    "SLA positif vaut 2, sans titre d'immunofluorescence. Un SLA positif et des antinucléaires à 1/40 ne font pas 3. Le plafond reste 2.",
    "Immunoglobuline exactement à la limite : le texte dit au-dessus de la limite pour 1 point. L'égalité n'est pas au-dessus. On ne offre pas le point.",
    "Immunoglobuline à 1,05 fois la limite : 1 point. Il faut dépasser 1,10 fois pour le second point. 10 % au-dessus, pas 5 %.",
    "Immunoglobuline à 1,10 fois pile. Le texte dit au-dessus de 1,10 fois. L'égalité avec 1,10 n'est pas au-dessus. On cote 1, sauf si le laboratoire montre un dépassement. On ne arrondit pas vers 2.",
    "Immunoglobuline à 2 fois la limite : 2 points au score simplifié. Le critère de Paris, lui, parle de deux fois la limite comme item du chevauchement. Même chiffre, deux usages. On dit lequel on coche.",
    "Histologie sans hépatite : le domaine ne s'ouvre pas. Une fibrose isolée ou une stéatose sans hépatite n'est pas « compatible ». Compatible veut une hépatite chronique lymphocytaire.",
    "Stéatohépatite : atypique, 0 point. On ne la fait pas monter à 1 parce qu'il y a des lymphocytes quelque part. L'exemple du tableau est précisément celui-là.",
    "Typique exige l'interface, l'infiltrat qui entre dans le lobule, l'empéripolèse, les rosettes. S'il manque ces traits et qu'il y a quand même une hépatite lymphocytaire, c'est compatible, 1 point, pas 2.",
    "Absence de virus : 2 points, pas 1. C'est le domaine le plus lourd après un histologie typique. L'oublier fait rater le seuil de 6 chez un patient qui aurait 4 plus 2.",
    "Virus B avec ADN élevé et ALAT haute : le domaine vaut 0. Le score ne se bricole pas. On traite le virus selon ses indications, pas avec 1 à 3 mg/kg d'azathioprine.",
    "Total 5 : sous le probable. On ne dit pas « presque ». On regarde si la forme est aiguë et si la biopsie peut encore ajouter 1 ou 2.",
    "Total 6 : probable. La conclusion de 2008 qui dit plus de 6 ne fait pas tomber ce 6. Le tableau et l'EASL 2015 le gardent. On écrit la tension entre les deux phrases et l'on suit le tableau.",
    "Total 7 : certaine. La sensibilité de validation est 81 %, la spécificité 99 %. Un certain n'est pas une preuve à 100 %. Il se traite.",
    "Total 8, comme le cas de 1/160, immunoglobuline à 1,4 fois, histologie typique et virus négatifs : 2+2+2+2. Au-dessus de 7. On ne cherche pas un neuvième point.",
    "Total 4 : anticorps 2 et virus 0 et le reste vide, par exemple. Très en dessous. Si l'histoire est chronique et calme, on cherche une autre maladie. Si l'histoire est fulminante, les 9 à 17 % sans anticorps empêchent l'exclusion sèche.",
    "Sensibilité 88 % au seuil d'au moins 6 : environ un patient sur dix avec la maladie peut être manqué par ce seuil. C'est cohérent avec la forme aiguë séronégative. La spécificité de 97 % dit que peu de gens sans la maladie passent le seuil.",
    "Au seuil d'au moins 7, la sensibilité baisse à 81 % et la spécificité monte à 99 %. Exiger 7 pour commencer à y penser fait manquer des probables à 6. Les deux seuils restent.",
    "Titre pédiatrique 1/20 et 1/10 : significatif selon l'EASL 2015, pas une ligne du tableau de Hennes. On ne donne pas 1 point adulte à un 1/20. On le signale au spécialiste comme titre significatif de l'enfant.",
    "85 % d'immunoglobuline haute : 15 % ne l'ont pas. Le score prévoit le 0. On ne récite pas 85 % comme si c'était obligatoire.",
    "25 % de début aigu. La majorité est plus lente. Un début aigu n'est pas un argument contre.",
    "Paris, côté biliaire, au moins deux sur trois. Phosphatase deux fois ou gamma-glutamyltransférase cinq fois, ce n'est pas « un peu cholestatique ». Anticorps antimitochondries. Lésion floride. Un seul de ces trois ne suffit pas.",
    "Paris, côté hépatite, au moins deux sur trois. Alanine cinq fois. Immunoglobuline deux fois ou muscle lisse. Nécrose parcellaire modérée ou sévère. Le score simplifié peut être haut sans que Paris soit rempli, et l'inverse se discute : on ne les fusionne pas en un seul nombre.",
    "Insuffisance. L'hépatite auto-immune peut se présenter ainsi malgré son caractère chronique. INR et encéphalopathie ouvrent King et Clichy. Le score ne retarde pas l'appel au centre.",
    "King hors antalgique : INR au-dessus de 6,5 seul, ou trois critères parmi cinq. Une hépatite auto-immune avec INR à 7 est déjà dans la porte qui suffit seule. On ne demande pas le score à 7 pour téléphoner.",
    "Clichy reste disponible : stade 3 ou 4 et facteur V selon l'âge, 20 % avant 30 ans, 30 % après. Il ne remplace pas le score, il décide de la greffe.",
    "Prednisolone, 5-60 mg/jour, information 29348. C'est la fourchette habituelle. Dire un nombre hors de cette information, pour ce lot, serait une dose non lue. Les comprimés existent à 5, 20 et 50 mg.",
    "Cushing au-dessus de 7,5 mg dans la même information. Un entretien prolongé au-dessus de ce seuil se justifie et se surveille. On ne le confond pas avec la dose d'attaque.",
    "Azathioprine, 1 à 3 mg/kg par jour, information 31887, hors greffe. C'est la phrase de l'hépatite chronique active auto-immune et des autres indications non transplantées. On pèse le patient. On ne donne pas une dose fixe de mémoire.",
    "Transplantation, même information : jusqu'à 5 mg/kg puis entretien 1 à 3 mg/kg. Un patient non greffé n'hérite pas du 5 mg/kg de départ. On cite le bon paragraphe.",
    "Comprimés d'Imurek à 25 mg et 50 mg. Ils servent à arrondir la dose au poids. Ils ne définissent pas la cible en mg/kg, qui reste 1 à 3.",
    "Cible : immunoglobuline G normale et alanine normale. Une alanine à deux fois la limite est encore un échec de cible, même si elle est « mieux ». On le dit au patient.",
    "Le thiopurine épargne le corticoïde. Commencer les deux se discute. Laisser le corticoïde seul des mois sans épargne, alors que l'information décrit l'azathioprine dans cette maladie, se justifie seulement par une contre-indication, pas par l'oubli.",
    "Numération sous azathioprine. L'information ajuste sur les paramètres hématologiques. Une neutropénie se voit, la dose baisse ou s'arrête selon le texte suisse, pas selon un seuil inventé ici.",
    "On ne pose pas l'acide ursodésoxycholique de l'information 60812 comme traitement de l'hépatite auto-immune pure. S'il y a un chevauchement et une cholangite biliaire primitive, c'est l'autre fichier qui porte cette dose, pas celui-ci en mélange.",
    "On ne pose pas le schéma d'acétylcystéine. Ce n'est pas une intoxication. Sauf si une prise d'antalgique coexiste, et alors c'est l'autre diagnostic qui commande l'antidote.",
    "Obstacle : une dilatation fait quitter le score pour Tokyo. Une hépatite auto-immune ne dilate pas la voie biliaire principale.",
    "Alcool : le score n'a pas de domaine pour les grammes. Une stéatohépatite vaut 0 à l'histologie. On ne cote pas « typique » un foie alcoolique.",
    "Wilson et l'insuffisance : les deux peuvent donner une hépatite aiguë sévère. L'anneau, la céruléoplasmine et le score de Leipzig se cherchent si l'âge et l'hémolyse y font penser. Un score simplifié bas ne les remplace pas.",
    "Hémochromatose : ferritine haute d'inflammation, pas une saturation. On ne cote pas le fer dans le score simplifié.",
    "La copie minimale : quatre domaines chiffrés, total, seuil 6 ou 7, conduite avec les numéros 29348 et 31887 si l'on traite, ou la phrase « non écarté » si la forme est aiguë et le score bas. Moins que ça, la longueur ne sert à rien.",
    "La copie qui perd les points. « Hépatite auto-immune, corticoïde ». Il manque le score. « Score à 6, donc certaine ». Faux, 6 est probable. « Immunoglobuline normale, donc non ». Faux dans la forme aiguë. « 1/40 égale 2 points ». Faux pour les antinucléaires.",
]

CAS = [
    "Cas 2+2+2+2. Anticorps 2, immunoglobuline 2, histologie typique 2, pas de virus 2. Total 8. Certaine. C'est le cas de la femme de 34 ans. On le refait sans regarder le texte, de mémoire de tableau.",
    "Cas 2+1+1+2. Anticorps au moins 1/80, immunoglobuline entre la limite et 1,10 fois, histologie compatible, pas de virus. Total 6. Probable. Pas certaine.",
    "Cas 1+2+1+2. Antinucléaires à 1/40 seulement, immunoglobuline au-dessus de 1,10 fois, histologie compatible, pas de virus. Total 6. Le 1 de l'anticorps faible est compensé par le 2 de l'immunoglobuline. On ne refuse pas le probable.",
    "Cas 2+2+0+2. Anticorps forts, immunoglobuline haute, mais stéatohépatite, pas de virus. Histologie 0. Total 6. Probable malgré l'histologie atypique, si l'on accepte que le tableau cote ainsi. On dit que l'histologie ne soutient pas, et que le spécialiste tranchera : le cours ne transforme pas un 0 histologique en 1.",
    "Cas 2+2+2+0. Tout est typique mais un virus B actif explique l'hépatite. Le domaine viral vaut 0. Total 6 si les trois autres sont à 2, ce qui ferait 6, mais on ne l'utilise pas pour traiter comme une auto-immune : le virus commande. Le score n'est pas une autorisation à ignorer l'ADN.",
    "Cas 1+1+1+2. Anticorps 1/40, immunoglobuline juste haute, histologie compatible, pas de virus. Total 5. Sous 6. Pas probable. Si la maladie est chronique et calme, on cherche autre chose ou l'on complète. Si elle est aiguë et grave, on n'écrit pas écarté.",
    "Cas 0+0+0+2. Rien que l'absence de virus. Total 2. Le tableau dit très en dessous. La seule raison de ne pas clore est le pourcentage de forme aiguë sans anticorps et sans immunoglobuline haute, 9 à 17 % et 25 à 39 %. On le réserve au malade sévère, pas à une enzyme à 1,2 fois la limite.",
    "Cas enfant. Antinucléaires à 1/20, enfant, titre significatif pour l'EASL 2015, pas 1 point du tableau adulte. On téléphone. On ne fabrique pas un total.",
    "Cas SLA seul. SLA positif, immunoglobuline normale, histologie pas encore faite, virus négatifs. Anticorps 2, immunoglobuline 0, histologie en attente, virus 2. Déjà 4, plus ce que dira le foie. On ne commence pas à coter 0 parce que les antinucléaires sont négatifs : le SLA suffit pour le 2.",
    "Cas d'interface incomplète. Le compte rendu dit hépatite lymphocytaire chronique sans rosettes ni empéripolèse. Compatible, 1, pas typique. Le total change d'un point. Ce point fait passer de 6 à 5 ou de 7 à 6. On lit les mots du pathologiste, on ne les embellit pas.",
    "Cas de chevauchement incomplet. Phosphatase à trois fois la limite, pas d'anticorps antimitochondries, pas de biopsie des canaux. Un seul critère biliaire. Paris n'est pas rempli. On ne dit pas chevauchement. On cote le score simplifié de l'hépatite si les domaines y sont.",
    "Cas de chevauchement tenu. Phosphatase à deux fois, anticorps antimitochondries, alanine à six fois, immunoglobuline à deux fois. Deux et deux. Paris est rempli. Le traitement de la cholangite biliaire primitive et celui de l'hépatite se discutent ensemble, chacun dans son information, 60812 d'un côté, 29348 et 31887 de l'autre. On ne additionne pas les doses.",
    "Cas d'insuffisance. INR 6,8, confusion, pas de cirrhose connue par ailleurs, anticorps en cours. King hors antalgique est rempli par l'INR seul au-dessus de 6,5. L'appel part avant le retour du titre. Le score complètera le dossier, il ne retient pas le téléphone.",
    "Cas de cible. Sous traitement, alanine encore à 1,8 fois la limite, immunoglobuline encore à 1,3 fois. Ni l'une ni l'autre n'est normale. La cible n'est pas atteinte. On ne parle pas de rémission.",
    "Cas de Cushing. Entretien prolongé au-dessus de 7,5 mg de prednisolone, information 29348. On cherche l'épargne par le thiopurine si la numération le permet, dans 1 à 3 mg/kg. On ne laisse pas la dose haute par habitude.",
    "Cas de greffe. Le paragraphe jusqu'à 5 mg/kg ne s'applique pas à la patiente de 34 ans jamais greffée. Elle reste dans 1 à 3 mg/kg. Écrire 5 mg/kg sur son ordonnance est une mauvaise lecture de l'information.",
    "Cas de poids. 60 kg, 2 mg/kg font la zone du milieu de 1 à 3. On montre le calcul. On arrondit au comprimé de 25 mg ou de 50 mg disponible. On ne invente pas un comprimé intermédiaire.",
    "Lettre. Âge, ALAT et sa limite, titre de chaque anticorps, immunoglobuline et sa limite, résultat viral, compte rendu histologique mot à mot, total du score, seuil retenu, proposition dans la fourchette 29348 et 31887. Une lettre sans total n'est pas une demande d'avis, c'est un paquet de bilans.",
    "Ce que l'on retire encore, hors de ce score. Une prévalence suisse. Une troisième ligne de nomogramme. Pas le tableau de Hennes : il est entier. Pas Leipzig, pas Tokyo, pas Maddrey : ils vivent dans leurs fichiers.",
    "Phrase de conclusion contre tableau. Si un correcteur attend plus de 6, on montre la phrase de 2008 et le tableau. La réponse enseignée ici est celle du tableau et de l'EASL 2015 : au moins 6 probable, au moins 7 certaine. On ne fait pas comme si la phrase n'existait pas.",
    "Addition lente. On écrit quatre lignes avant le total. Ligne anticorps, avec le titre et le plafond. Ligne immunoglobuline, avec le rapport à la limite. Ligne histologie, avec le mot du pathologiste : atypique, compatible ou typique. Ligne virus, 2 ou 0. Puis seulement le total. Une copie qui donne le total sans les lignes ne se corrige pas.",
    "Erreur de plafond, chiffrée. Antinucléaires 1/320 et anti-microsomes 1/160. Un étudiant écrit 4. La réponse est 2. Le domaine est plafonné. Le second anticorps confirme, il n'ajoute pas.",
    "Erreur de barreau, chiffrée. Antinucléaires 1/40, l'étudiant met 2 parce que « c'est positif ». La réponse est 1. Le 2 commence à 1/80 pour ces anticorps-là. Les anti-microsomes, eux, valent 2 dès 1/40. Le barreau dépend de l'anticorps.",
    "Erreur d'immunoglobuline. Rapport 1,08. L'étudiant met 2 parce que « c'est au-dessus ». La réponse est 1. Le 2 commence au-dessus de 1,10 fois. 1,08 est au-dessus de la limite et en dessous du second seuil.",
    "Erreur d'histologie. Le compte rendu dit stéatohépatite. L'étudiant met 1, compatible, parce qu'il y a de l'inflammation. La réponse est 0, atypique. L'exemple du tableau est celui-ci.",
    "Erreur de virus. IgM du virus A positive, antinucléaires 1/160, immunoglobuline haute, histologie pas faite. On ne commence pas l'azathioprine. Le virus aigu commande. Le domaine viral ne vaut pas 2.",
    "Forme aiguë chiffrée. ALAT à 25 fois la limite, INR 2,0, immunoglobuline à 0,9 fois la limite, aucun anticorps, virus négatifs. Points sérologiques : 0 et 0, plus 2 pour le virus absent, histologie absente. Total provisoire 2. Les 25 à 39 % et les 9 à 17 % interdisent d'écrire écarté. INR à 2,0 est déjà au-dessus de 1,5 : on regarde la conscience pour l'insuffisance.",
    "Forme certaine minimale. Il faut au moins 7, donc par exemple 2+2+1+2 = 7. Anticorps forts, immunoglobuline au-dessus de 1,10 fois, histologie seulement compatible, pas de virus. Certaine sans histologie typique. Le 2 histologique n'est pas obligatoire si le reste compense.",
    "Forme probable minimale autre chemin. 2+2+2+0 ne se traite pas comme auto-immune si le 0 est un virus actif. Le chemin propre du probable est 2+1+1+2 ou 1+2+1+2, sans virus. On le réécrit.",
    "Enfant et adulte sur la même feuille. La mère a des antinucléaires à 1/40, soit 1 point adulte. L'enfant a des antinucléaires à 1/20, titre significatif pédiatrique, pas un point du tableau. Deux phrases, deux âges. On ne copie pas le 1 de la mère sur l'enfant.",
    "Cible non atteinte, chiffres. Alanine encore à 2 fois la limite, immunoglobuline encore à 1,2 fois. Aucune des deux n'est normale. On continue. On ne déclare pas la rémission sur une baisse de moitié.",
    "Ordonnance. Prednisolone dans la fourchette 5-60 mg/jour, numéro 29348. Azathioprine 1 à 3 mg/kg par jour, numéro 31887, poids écrit à côté. Numération de contrôle. Pas de dose d'une autre hépatite. Pas de 5 mg/kg, réservé au paragraphe de la greffe.",
    "Greffe, le bon paragraphe. Jusqu'à 5 mg/kg puis entretien 1 à 3 mg/kg, même information 31887, autre section. Le patient du cas de 34 ans n'y est pas. Le patient greffé n'est pas dans la phrase « généralement 1 à 3 » comme dose de départ unique : le texte de greffe autorise d'aller jusqu'à 5 mg/kg au début.",
    "Chevauchement et doses séparées. Paris rempli. L'acide de l'information 60812 se décide dans le fichier de la cholangite biliaire primitive. Le corticoïde et le thiopurine se décident ici. Une ordonnance qui mélange les deux sans dire quel critère de Paris est coché est illisible.",
    "Suivi. On reprend l'alanine et l'immunoglobuline, pas seulement l'une. Une alanine normale avec une immunoglobuline encore haute n'est pas la cible. L'inverse non plus. Les deux lignes du dossier bougent ensemble.",
    "Ce que le score ne fait pas. Il ne donne pas le grade de Tokyo. Il ne donne pas le rapport R, même s'il est en général hépatocellulaire. Il ne donne pas Child-Pugh. Il ne donne pas la fonction discriminante de l'hépatite alcoolique. Un malade peut avoir besoin d'un de ces outils en plus, jamais à la place des quatre domaines.",
    "Lettre de sortie après le diagnostic certain. Total 8, domaines écrits, prednisolone commencée dans la fourchette suisse, azathioprine prévue ou différée avec la raison, prochaine prise de sang, numéro des deux informations. Le patient repart avec une cible dite en mots : immunoglobuline normale et alanine normale.",
    "Relecture du tableau avant de rendre la copie. Autoanticorps plafonnés à 2. Immunoglobuline : 1 au-dessus de la limite, 2 au-dessus de 1,10 fois. Histologie : 0 atypique, 1 compatible, 2 typique, et une hépatite est nécessaire. Absence de virus : 2. Au moins 6 probable. Au moins 7 certaine. Si une ligne manque, le total est un guess.",
    "Validation à citer avec le seuil, pas toute seule. Au moins 6 : sensibilité 88 %, spécificité 97 %. Au moins 7 : sensibilité 81 %, spécificité 99 %. Inverser les paires est une faute. Attribuer 99 % de sensibilité est une faute.",
    "Interface, infiltrat lymphocytaire ou lymphoplasmocytaire étendu au lobule, empéripolèse, rosettes : les quatre traits du typique. En manquer et appeler ça typique vole un point. Les avoir tous et appeler ça compatible en vole un dans l'autre sens.",
    "Empéripolèse se définit comme une cellule intacte à l'intérieur d'une autre. On ne la confond pas avec une nécrose. Le cours la cite parce que le tableau de 2008 la met dans le typique, pas pour orner la phrase.",
    "Rosettes : hépatocytes arrangés autour d'une lumière. Elles comptent pour le typique. Une biopsie qui ne les mentionne pas n'est pas automatiquement atypique : elle peut rester compatible s'il y a une hépatite lymphocytaire.",
    "Médicament et auto-immunité. Un antibiotique peut accompagner le début. On date les deux. Si les virus sont négatifs et que le score atteint 7, on ne réduit pas le diagnostic à l'antibiotique. Si le score est à 3 et que l'antibiotique a un délai net, le fichier de la lésion médicamenteuse reprend la main, avec ses cinq classes.",
    "Grossesse. On ne invente pas une dose. On lit 29348 et 31887 avec le spécialiste. Le score, lui, se calcule pareil. Une immunoglobuline haute de la grossesse ne se décrète pas : on compare à la limite du laboratoire du jour.",
    "Homme de 55 ans, même score à 8 qu'une femme de 34 ans. Le sexe ne retire pas de point et n'en ajoute pas. Écrire « peu probable parce que c'est un homme » contredit le tableau, qui n'a pas de ligne sexe.",
    "Rechute. Alanine qui était normale et qui repasse à trois fois la limite, immunoglobuline qui remonte, observance douteuse. On ne refait pas tout le score comme un premier diagnostic. On reprend la cible. On vérifie les comprimés pris. Une nouvelle biopsie se discute, elle ne se pose pas le jour même par réflexe.",
    "Arrêt du traitement. L'information 31887 dit, pour la greffe, que l'arrêt expose au rejet. Pour l'hépatite, le cours ne invente pas une durée minimale qui n'a pas été extraite. L'arrêt se décide avec le spécialiste après une cible tenue, pas au premier mois normal.",
    "Biopsie impossible, INR à 2,4, ascite. L'histologie manque. On additionne ce que l'on a et l'on écrit « histologie non faite, total incomplet ». On ne met pas 2 points « parce que c'est sûrement typique ». L'insuffisance, elle, se gère tout de suite.",
    "Contrôle de la numération avant d'augmenter l'azathioprine dans la fourchette 1 à 3 mg/kg. L'information ajuste sur l'hématologie. Monter le poids théorique sans regarder les leucocytes n'est pas le texte suisse.",
    "Phrase finale de la copie type. Quatre domaines, total, comparaison à 6 et à 7, mention que la conclusion de 2008 dit aussi plus de 6, conduite avec 29348 et 31887 ou non-exclusion si la forme est aiguë. Cinq éléments. Le correcteur les cherche dans cet ordre.",
    "Cas limite 6 contre 7. Immunoglobuline à 1,10 fois pile : on cote 1, pas 2, parce que le tableau dit au-dessus de 1,10 fois. Si le reste est 2+1+2, le total est 6, probable. Si le laboratoire rend 1,15 fois, le point d'immunoglobuline passe à 2 et le total passe à 7, certaine. Le chiffre après la virgule décide. On le recopie, on ne le estime pas.",
    "Cas limite histologique. Compte rendu : hépatite d'interface et infiltrat lymphoplasmocytaire, sans mention de rosette ni d'empéripolèse. On ne complète pas les traits absents. Compatible, 1 point, tant que le pathologiste n'a pas écrit les quatre traits du typique. Ce point manquant sépare un 7 d'un 6.",
    "Cas de double seuil viral. Antigène HBs positif, ADN indétectable, ALAT à 8 fois, score immunitaire par ailleurs à 6 sans compter le virus. Un ADN indétectable ne veut pas dire absence d'hépatite virale si l'antigène est là et que l'enzyme est haute : on en discute avec le spécialiste du virus, on ne coche pas 2 points « virus absent » par confort. Le domaine veut l'absence d'hépatite virale, pas l'absence d'un papier de sérologie.",
    "Ordre du traitement le premier jour d'une forme certaine sans insuffisance. Expliquer le score. Commencer dans 5-60 mg/jour de prednisolone, information 29348. Prévoir l'azathioprine dans 1 à 3 mg/kg, information 31887, après la numération. Donner la cible. Fixer la date du prochain bilan. Cinq phrases, aucune dose venue d'une autre maladie.",
    "Mémo des deux seuils, dans cet ordre. D'abord au moins 6, probable. Ensuite au moins 7, certaine. Ensuite seulement la phrase de conclusion qui dit plus de 6. Le tableau gagne. Le candidat qui inverse 6 et 7 inverse la maladie.",
]

def main():
    fen.append((8, W("w-long6", "Chaque point, avec l'erreur qui le perd", "\n".join(P(sla(p), 3, 7, 13, 16, 22) for p in LONGS))))
    fen.append((14, W("w-cas6b", "Additions", "\n".join(P(sla(p), 7, 13, 16, 22) for p in CAS))))
    essentiel = (
        P("Hennes 2008 et EASL 2015 : anticorps plafonnés à 2, immunoglobuline 1 ou 2, histologie 0 à 2, absence de virus 2. Au moins 6 probable, au moins 7 certaine.", 22)
        + P("Prednisolone 5-60 mg/jour, information 29348. Azathioprine 1 à 3 mg/kg par jour hors greffe, information 31887.", 13, 16)
    )
    phrases = {
        1: "Hépatite immune. Le nom ne se pose pas sur un anticorps isolé.",
        2: "Pas de prévalence suisse. Sensibilité 88 % et 81 %, spécificité 97 % et 99 %, jeu de validation.",
        3: "L'interface est le lieu de l'attaque. L'immunoglobuline en est le reflet, absent chez une minorité aiguë.",
        4: "Titrer, doser l'immunoglobuline, écarter le virus, puis l'histologie.",
        5: "Autres maladies immunes, médicaments, alcool. Le sexe n'est pas un point du score.",
        6: "L'examen cherche l'insuffisance, pas les points.",
        7: "Chronique, aiguë, insuffisance, ou chevauchement. Quatre portes.",
        8: "Quatre domaines, seuils 6 et 7, phrase de conclusion citée sans remplacer le tableau.",
        9: "Titre chiffré, immunoglobuline quantitative, virus, biopsie si elle est faisable.",
        10: "7 certaine, 6 probable, sous 6 et tableau aigu : non écarté.",
        11: "5-60 mg/jour et 1 à 3 mg/kg par jour. Cible : deux normalisations.",
        12: "Numération sous thiopurine. Vaccinations avant l'immunosuppression.",
        13: "Plafond 2. 1,10 fois. Histologie avec hépatite. Virus 2 points.",
        14: "1/40 n'est pas 2 points pour les antinucléaires. 6 n'est pas certaine.",
    }
    fiches = {n: P(phrases[n], 22) for n in phrases}
    sources = [
        f"Hennes et al., Hepatology, 2008, score simplifié, tableau 2.{S(22)}",
        f"{EASL}, hépatite auto-immune, 2015, mêmes domaines et mêmes seuils.{S(7)}",
        f"{AIPS} Prednisolone Streuli, Swissmedic 29348.{S(13)}",
        f"{AIPS} Imurek, Swissmedic 31887.{S(16)}",
        f"{EASL}, insuffisance hépatique aiguë, 2017, si le tableau décompense.{S(3)}",
    ]
    sous = (
        f"Diagnostic différentiel DX.6 de {A('situation de départ F2.11 de PROFILES','F2.11')} "
        f"« Enzymes hépatiques anormales ». Texte du 31.10.2026."
    )
    par = {}
    for point, html in fen:
        par.setdefault(point, []).append(html)
    path = construire(6, "Hépatite auto-immune", essentiel, sous, fiches, par, sources)
    print(path)

if __name__ == "__main__":
    main()
