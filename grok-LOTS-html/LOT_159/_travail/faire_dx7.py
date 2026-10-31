#!/usr/bin/env python3
"""DX.7 Cholangite biliaire primitive."""
from base_dx import P, W, construire, A
from moteur import S

ALAT = A("alanine aminotransférase", "ALAT")
PAL = A("phosphatase alcaline", "PAL")
GGT = A("gamma-glutamyltransférase", "GGT")
LSN = A("limite supérieure de la normale", "LSN")
EASL = A("European Association for the Study of the Liver", "EASL")
AIPS = A("information professionnelle", "AIPS")
INR = A("international normalized ratio", "INR")

def sla(t):
    return t

def F(point, ident, titre, textes, *refs):
    return point, W(ident, titre, "\n".join(P(t, *refs) for t in textes))

fen = []
fen.append(F(1, "d7", "Définition", [
    "La cholangite biliaire primitive est une maladie des petits canaux biliaires, chronique, souvent chez la femme, avec prurit, phosphatase haute et anticorps antimitochondries. Le nom ancien de cirrhose n'est plus juste au début : beaucoup de patientes n'ont pas de cirrhose le jour du diagnostic.",
    "L'information suisse Ursofalk, numéro 60812, l'indique aux stades I à III. Ce n'est pas le traitement d'un calcul, ni d'une hépatite auto-immune pure, ni d'une autre cholestase intrahépatique hors étude.",
], 12))
fen.append(F(3, "ph7", "Physiopathologie", [
    "Les petits canaux sont détruits. La bile des canalicules s'évacue mal. La phosphatase et la gamma-glutamyltransférase montent avant l'ictère. Le prurit peut précéder l'ictère de mois. La bilirubine haute est un signe plus tardif.",
    "L'acide ursodésoxycholique remplace des acides biliaires plus toxiques et fait régresser les enzymes et la bilirubine dans les études citées par l'information. L'information dit aussi que l'amélioration histologique est peu documentée et qu'aucune affirmation n'est faite sur la survie. On ne promet pas les deux.",
], 12))
fen.append(F(3, "et7", "Ce que ce n'est pas", [
    "Obstacle extra-hépatique : dilatation, calcul, Tokyo. Ici les voies principales sont fines. Une dilatation fait quitter ce fichier.",
    "Hépatite auto-immune pure : score de Hennes, pas d'acide biliaire comme seul traitement. Chevauchement : critères de Paris, au moins deux sur trois de chaque côté, et alors les deux traitements se discutent sans se confondre.",
    "Cholangite sclérosante : autre maladie. L'information 60812 dit que l'usage prolongé de 28 à 30 mg/kg/jour a été associé à des effets indésirables sévères dans la cholangite sclérosante primitive, hors indication. On n'emporte pas cette dose.",
    "Autre cholestase intrahépatique : l'information limite l'usage à une étude contrôlée. On ne généralise pas.",
], 7, 12, 18))
fen.append(F(8, "dg7", "Diagnostic positif", [
    f"Phosphatase haute, souvent au moins deux fois la {LSN} quand on parle du critère de Paris côté biliaire, ou gamma-glutamyltransférase au moins cinq fois. Anticorps antimitochondries. Échographie sans obstacle. Biopsie si les anticorps manquent : lésion floride des canaux, pas obligatoire si les anticorps et le profil concordent et que l'image est normale.",
    "On ne pose pas le nom sur un prurit isolé sans enzyme, ni sur une phosphatase isolée sans avoir cherché l'obstacle.",
], 7, 12))
fen.append(F(8, "cp7", "Child-Pugh, bilirubine décalée", [
    "Le barème habituel de la bilirubine, lu avec Child et Pugh, est inférieur à 34 µmol/l, de 34 à 50, au-dessus de 50. Pour la cholangite biliaire primitive et la cholangite sclérosante, la page lue décale ces seuils : 68 µmol/l et 170 µmol/l.",
    "Albumine, INR, ascite et encéphalopathie ne changent pas de barème. Seule la bilirubine se décale. Utiliser 50 µmol/l chez une patiente qui a cette maladie sous-cote ou surcote le point. A reste 5 ou 6, B 7 à 9, C 10 à 15. Les trois classes restent.",
    "Ce score décrit la cirrhose. Il ne remplace pas la décision de commencer l'acide aux stades I à III, ni la surveillance d'un stade avancé.",
], 9))
fen.append(F(11, "ud7", "Dose lue, information 60812", [
    "Environ 10 mg par kilogramme de poids. La dose journalière est comprise entre un comprimé et demi et trois comprimés et demi, soit 14 ± 2 mg par kilogramme. Les comprimés sont à 500 mg. En dessous de 47 kg, ou si la patiente ne peut pas avaler le comprimé, il existe des capsules et une suspension, dont la capsule à 250 mg est citée pour réduire la dose en cas de prurit aggravé au début.",
    "Les trois premiers mois, on répartit la dose dans la journée. Après amélioration des paramètres, la dose du jour peut se prendre le soir. Sauf la prise du soir, on prend le comprimé avec les repas, sans le croquer, avec du liquide.",
    "Le traitement des stades I à III n'est pas limité dans le temps par l'information. L'usage chez l'enfant et l'adolescent n'a pas été étudié.",
    "Au début, le prurit peut s'aggraver. On réduit alors à un demi-comprimé de 500 mg ou à une capsule de 250 mg par jour, puis on remonte. On n'arrête pas au premier prurit sans cette étape.",
    "Stade avancé : une décompensation de cirrhose a été observée, très rare, et elle a régressé à l'arrêt. On surveille la fonction hépatique. On ne commence pas « pour voir » chez un ictère déjà compliqué sans cette surveillance.",
    "28 à 30 mg/kg/jour, usage prolongé, cholangite sclérosante, hors indication : effets indésirables sévères. Cette phrase interdit d'augmenter au-delà de 14 ± 2 mg par kilogramme pour « faire plus fort ».",
], 12))
fen.append(F(4, "de7", "Démarche", [
    f"Phosphatase et gamma-glutamyltransférase, bilirubine, {ALAT}, {INR}, albumine, échographie, anticorps antimitochondries. R se calcule : il est en général au plus égal à 2. S'il est au moins égal à 5, on cherche une hépatite, pas seulement cette maladie.",
    "Image normale et anticorps présents : le diagnostic est tenu. Image anormale : Tokyo ou tumeur, pas l'acide seul. Anticorps absents et image normale : biopsie avant de poser le nom.",
], 2, 12))
fen.append(F(5, "an7", "Anamnèse", [
    "Prurit, surtout le soir, fatigue, sécheresse, autre maladie immune, thyroïde, ostéoporose déjà là. Médicaments cholestatiques à écarter. Pas de colique, pas de fièvre : sinon l'obstacle infecté passe devant.",
], 12, 18))
fen.append(F(6, "ex7", "Examen", [
    "Griffures, ictère, xanthélasmas, foie, rate, ascite. L'examen peut être normal au début. Le prurit sans lésion cutanée primitive se distingue d'une dermatose. L'ascite et la confusion font compter Child-Pugh avec la bilirubine décalée.",
], 9))
fen.append(F(7, "sy7", "Syndromes", [
    "Cholestase chronique sans dilatation. Poussée de prurit au début du traitement. Décompensation rare du stade avancé. Chevauchement si Paris est rempli. Angiocholite si la fièvre et la dilatation apparaissent : on change de fichier.",
], 7, 12, 18))
fen.append(F(9, "la7", "Examens", [
    f"Phosphatase, gamma-glutamyltransférase, bilirubine, anticorps, échographie, numération et coagulation pour le stade. Élastographie si l'on cherche la fibrose, sans inventer un seuil en kilopascals qui n'a pas été lu. Biopsie ciblée.",
], 12))
fen.append(F(10, "ar7", "Arbre", [
    "Obstacle à l'image : quitter ce fichier. Anticorps et profil cholestatique et image normale : commencer selon 60812, stades I à III. Stade avancé : surveillance renforcée, savoir arrêter si décompensation. Chevauchement : Paris, puis les deux traitements dans leurs informations.",
    "Autre cholestase intrahépatique sans cette maladie : pas d'acide hors étude. Cholangite sclérosante : pas la dose de 28 à 30 mg/kg/jour.",
], 12))
fen.append(F(12, "pv7", "Suivi", [
    "Enzymes et bilirubine pour voir la réponse et pour voir une décompensation. Os et vitamines selon le spécialiste, sans dose inventée ici. Le traitement n'a pas de date de fin écrite pour les stades I à III. Un contrôle unique le premier mois ne suffit pas.",
], 12))
fen.append(F(13, "cl7", "Points de la copie", [
    "Stades I à III. Environ 10 mg par kilogramme, et 14 ± 2 mg par kilogramme, comprimés à 500 mg, information 60812. Pas pour les autres cholestases hors étude. Pas 28 à 30 mg/kg/jour dans la sclérosante. Bilirubine de Child-Pugh décalée à 68 et 170 µmol/l. Décompensation rare du stade avancé, réversible à l'arrêt.",
], 9, 12))
fen.append(F(14, "pi7", "Pièges", [
    "Traiter un calcul avec cet acide. Traiter toute cholestase. Monter à 28-30 mg/kg. Utiliser le seuil de bilirubine à 50 µmol/l pour le Child-Pugh de cette maladie. Promettre un gain de survie que l'information ne promet pas. Oublier la réduction de dose si le prurit s'aggrave au début.",
], 9, 12))
fen.append(F(14, "cas7", "Cas corrigé", [
    "Femme de 52 ans, prurit vespéral, phosphatase à 3 fois la limite, gamma-glutamyltransférase haute, alanine à 1,4 fois, bilirubine normale, anticorps antimitochondries positifs, échographie sans dilatation, pas de fièvre. R cholestatique. Pas de Tokyo. Diagnostic tenu sans biopsie obligatoire.",
    "Poids 70 kg. Dose dans 14 ± 2 mg par kilogramme, soit la zone de l'information, comprimés à 500 mg, numéro 60812. Répartie dans la journée les trois premiers mois, avec les repas, sauf si l'on regroupe le soir après amélioration. On ne promet pas la survie.",
    "Le prurit augmente à la deuxième semaine. On baisse à un demi-comprimé de 500 mg ou une capsule de 250 mg par jour, puis on remonte. On n'arrête pas net et on ne monte pas la dose.",
    "Variante. La même femme a une ascite et une bilirubine à 80 µmol/l. Child-Pugh : la bilirubine se compare à 68 et à 170, pas à 50. 80 est au-dessus de 68 et en dessous de 170 : 2 points de bilirubine, pas 3. On ajoute albumine, INR, ascite, encéphalopathie. Stade avancé : surveillance, et l'on sait qu'une décompensation sous traitement a été vue et a régressé à l'arrêt.",
    "Variante obstacle. Fièvre 38,8 °C et voie biliaire dilatée. On quitte l'acide comme sujet principal. Tokyo. Le prurit chronique ne fait pas ignorer la fièvre.",
], 9, 12, 18))

LONGS = [
    "Le stade I à III est l'indication écrite. On ne commence pas l'information en disant « toute cholangite ». Le stade se discute avec l'histologie ou le tableau. Un stade avancé n'est pas une interdiction sèche : c'est une surveillance, à cause de la décompensation rare.",
    "Environ 10 mg par kilogramme est la première phrase de l'information. 14 ± 2 mg par kilogramme est la phrase de la dose journalière en comprimés. Les deux se citent. On n'en fabrique pas une troisième, par exemple 20, qui n'est pas le texte.",
    "Un comprimé et demi à trois comprimés et demi de 500 mg : c'est la même dose, dite en comprimés. Pour un poids hors de la zone où ce nombre de comprimés tombe juste, on revient au milligramme par kilogramme, on ne force pas un comprimé de plus.",
    "En dessous de 47 kg, le comprimé de 500 mg est malcommode. Capsules et suspension existent. On ne casse pas au jugé sans lire cette phrase.",
    "Prurit aggravé : demi-comprimé de 500 mg ou capsule de 250 mg, puis remontée. La baisse est temporaire. L'abandonner définitivement au premier prurit prive la patiente du traitement.",
    "Trois mois de doses réparties, puis possibilité du soir. Avant l'amélioration des enzymes, tout mettre le soir n'est pas la phrase. Après, c'est permis.",
    "Avec les repas, sans croquer, avec un liquide. La prise du soir avant le coucher est l'exception écrite. On ne invente pas un jeûne.",
    "Pas de date de fin pour les stades I à III. Un « essai de trois mois puis stop » n'est pas l'information. Trois mois est le délai de la répartition, pas de l'arrêt.",
    "Enfant et adolescent : usage non étudié. On ne calque pas la dose adulte. On adresse.",
    "Régression des enzymes et de la bilirubine : oui, les études citées. Histologie : données rares. Survie : aucune affirmation. Trois phrases, trois niveaux de preuve. Les aligner est une faute.",
    "Décompensation très rare au stade avancé, régressive à l'arrêt. On prévient. On surveille. On n'en fait pas une contre-indication absolue de la première ligne, et on ne l'oublie pas non plus.",
    "Surveillance : détection précoce d'une altération de la fonction, surtout au stade avancé, et jugement de la réponse. Un bilan annuel unique chez une ictérique n'est pas cette phrase.",
    "28 à 30 mg/kg/jour et cholangite sclérosante : hors indication, effets sévères. La copie qui propose cette dose « comme dans les études » a mal lu. La dose de la primitive reste 14 ± 2 mg par kilogramme.",
    "Autre cholestase intrahépatique : étude contrôlée seulement. Grossesse cholestatique, médicament, sepsis : pas une ordonnance d'Ursofalk par analogie.",
    "Calcul du cholédoque : Tokyo ou endoscopie, pas cet acide. La dissolution des calculs de cholestérol est une autre rubrique de la même information, avec une contraception non hormonale. On ne la colle pas sur la cholangite biliaire primitive, et on ne l'utilise pas comme traitement d'un calcul obstructif fébrile.",
    "Contraception : la rubrique des calculs de cholestérol demande une contraception non hormonale ou un œstrogène faible, parce que les hormones favorisent les calculs. On ne transporte pas cette phrase comme une interdiction générale sans dire de quelle rubrique elle vient.",
    "Child-Pugh, bilirubine. Habituel : 34 et 50 µmol/l. Cette maladie et la sclérosante : 68 et 170. Albumine inchangée : plus de 3,5 g/dl, 2,8 à 3,5, moins de 2,8. INR inchangé : inférieur à 1,7, 1,7 à 2,3, supérieur à 2,3. Ascite et encéphalopathie inchangées. Cinq items, une seule bilirubine décalée.",
    "Classe A 5 ou 6, B 7 à 9, C 10 à 15. Citer seulement B n'est plus le score. Chez cette patiente, un total se calcule avec 68 et 170, puis on nomme A, B ou C.",
    "Exemple. Bilirubine 60 µmol/l. Barème habituel : au-dessus de 50, 3 points. Barème décalé : en dessous de 68, 1 point. La classe peut changer. La copie doit dire quel barème.",
    "Exemple. Bilirubine 100 µmol/l. Décalé : au-dessus de 68 et en dessous de 170, 2 points. Habituel : 3 points. Encore un écart. On montre 100, 68 et 170.",
    "Exemple. Bilirubine 200 µmol/l. Au-dessus de 170 : 3 points, même dans le barème décalé. Là, les deux barèmes se rejoignent sur 3. On le dit, on ne suppose pas que le décalage annule toujours le point fort.",
    "R au plus égal à 2 confirme le profil. R à 6 doit faire chercher une hépatite, un médicament, une ischémie, pas augmenter l'acide.",
    "Paris, côté biliaire : phosphatase au moins deux fois ou gamma-glutamyltransférase au moins cinq fois, anticorps antimitochondries, lésion floride. Deux sur trois. Un seul ne fait pas le chevauchement, mais les anticorps plus la phosphatase font déjà le diagnostic de la cholangite elle-même, qui n'exige pas Paris.",
    "Paris, côté hépatite : alanine au moins cinq fois, immunoglobuline au moins deux fois ou muscle lisse, nécrose parcellaire. Deux sur trois. Alors le score de Hennes et l'acide coexistent, chacun dans son fichier, doses non additionnées.",
    "Hennes ne se substitue pas aux anticorps antimitochondries. Un score à 8 sans phosphatase haute n'est pas cette maladie. Une phosphatase haute sans score n'est pas une hépatite auto-immune.",
    "Fièvre et dilatation : grade de Tokyo, pas une poussée de la maladie chronique. L'acide ne draine pas un calcul.",
    "Médicament cholestatique : on l'arrête et l'on recalcule. Un antibiotique récent peut imiter le profil. Les anticorps antimitochondries, eux, ne se positivent pas en une semaine de médicament.",
    "Alcool : pas le profil de cette maladie. Une stéatose ne se traite pas par 60812. L'information n'a pas cette indication.",
    "Virus : une hépatite C ne se traite pas par l'acide biliaire. On confirme ou l'on écarte le virus avant d'attribuer toute la phosphatase à la cholangite.",
    "La copie minimale : diagnostic (anticorps, phosphatase, image normale), dose avec 14 ± 2 mg par kilogramme et le numéro 60812, ce que l'on ne fait pas (pas 28 à 30, pas un calcul), et le barème de bilirubine si la cirrhose est là. Quatre éléments.",
    "La copie qui perd les points. « Prurit, Ursofalk ». Il manque la dose et l'image. « 30 mg par kilogramme ». C'est la dose interdite de la sclérosante, pas celle-ci. « Child-Pugh C parce que la bilirubine est à 60 ». Faux si l'on a utilisé 50 au lieu de 68. « Survie améliorée ». L'information ne le dit pas.",
    "Lettre. Poids, nombre de comprimés, répartition ou prise du soir, numéro 60812, prochaine phosphatase, échographie déjà normale, stade si on le connaît, prurit expliqué. Une lettre sans poids ne permet pas de vérifier 14 ± 2 mg par kilogramme.",
    "Ordonnance de ville. Comprimés à 500 mg, avec les repas, sans croquer. Consigne écrite : si le prurit explose, baisser à un demi-comprimé ou une capsule de 250 mg et appeler, ne pas doubler. Pas d'autre cholestase ajoutée sur la même ordonnance.",
]

CAS = [
    "Cas 60 kg. La ligne lue est 14 ± 2 mg par kilogramme, pas une autre ligne inventée. On traduit en comprimés de 500 mg, entre un et demi et trois et demi, et l'on vérifie que le nombre de comprimés reste dans cette zone. On montre le produit et le poids. On ne sort pas de la fourchette.",
    "Cas 90 kg. La fourchette 14 ± 2 mg par kilogramme se recalcule. On compte les comprimés de 500 mg. On reste entre un et demi et trois et demi. Si le calcul sort de 14 ± 2, on ne rajoute pas un comprimé de plus pour arrondir.",
    "Cas 45 kg. Sous 47 kg. On n'impose pas le comprimé de 500 mg. Capsule ou suspension. La phrase est dans l'information. L'ignorer fait une ordonnance que la patiente ne prend pas.",
    "Cas prurit à J10. Dose pleine, prurit pire. Conduite : demi-comprimé de 500 mg ou capsule de 250 mg, puis remontée progressive. Pas d'arrêt définitif. Pas d'ajout d'antihistaminique comme seul geste si l'on n'a pas baissé l'acide.",
    "Cas enzymes améliorées à trois mois. On peut regrouper le soir. On continue. On ne stoppe pas parce que « trois mois sont passés ». Trois mois ne sont pas une durée de cure.",
    "Cas sans amélioration à six mois. On vérifie la prise, le poids, l'obstacle oublié, le chevauchement. On ne passe pas à 28 à 30 mg/kg/jour. Cette zone est celle qui a posé problème dans la sclérosante.",
    "Cas sclérosante par erreur d'étiquette. Homme, maladies inflammatoires de l'intestin, voies irrégulières à l'image. Ce n'est pas la primitive. Surtout pas 28 à 30 mg/kg/jour. On adresse. On ne recopie pas l'ordonnance de la voisine.",
    "Cas Child-Pugh. Bilirubine 90 µmol/l, albumine 3,0 g/dl, INR 1,5, ascite absente, pas d'encéphalopathie. Bilirubine décalée : 90 est entre 68 et 170, 2 points. Albumine entre 2,8 et 3,5 : 2 points. INR inférieur à 1,7 : 1 point. Pas d'ascite : 1. Pas d'encéphalopathie : 1. Total 7. Classe B. Avec le barème non décalé, la bilirubine à 90 serait à 3 points et le total à 8, toujours B, mais le point est faux. On exige le bon point même si la classe ne bouge pas.",
    "Cas où la classe bouge. Bilirubine 60, albumine 3,6 g/dl (1 point), INR 1,2 (1), pas d'ascite (1), pas d'encéphalopathie (1). Décalé : bilirubine sous 68, 1 point, total 5, classe A. Non décalé : bilirubine au-dessus de 50, 3 points, total 7, classe B. Le barème change la classe. C'est pour ce cas que le décalage existe.",
    "Cas 200 µmol/l. Au-dessus de 170, 3 points de bilirubine, décalé ou non. On ne dit pas que le décalage « protège » toujours.",
    "Cas décompensation. Ictère qui s'aggrave, ascite nouvelle, sous acide, stade déjà avancé. L'information a vu cela, très rare, régressif à l'arrêt. On arrête et l'on hospitalise. On ne double pas la dose.",
    "Cas fièvre. 39 °C, dilatation, bilirubine 100 µmol/l. Tokyo, grade à compter, pas une adaptation d'Ursofalk. L'acide chronique peut être suspendu le temps du sepsis. Il ne traite pas l'angiocholite.",
    "Cas chevauchement. Phosphatase 2,5 fois, anticorps antimitochondries, alanine 6 fois, immunoglobuline 2 fois. Paris des deux côtés. Acide selon 60812 et traitement de l'hépatite selon 29348 et 31887. Deux ordonnances lisibles, pas une dose hybride.",
    "Cas hépatite auto-immune seule. Score de Hennes à 8, phosphatase normale, pas d'anticorps antimitochondries. Pas d'Ursofalk. Le corticoïde et le thiopurine suffisent comme sujet. Ajouter l'acide « pour le foie » contredit l'information.",
    "Cas enzyme médicamenteuse. Antibiotique depuis trois semaines, phosphatase haute, anticorps négatifs, image normale. On arrête l'antibiotique. On ne pose pas la maladie chronique sur un mois. Les anticorps antimitochondries ne sont pas un détail.",
    "Cas de promesse. La patiente demande si elle vivra plus longtemps. Réponse selon l'information : les enzymes et la bilirubine peuvent régresser, l'histologie est peu prouvée, la survie n'est pas affirmée. On ne invente pas un pourcentage.",
    "Cas d'observance. Elle croque le comprimé. L'information dit sans croquer. On corrige. Ce n'est pas une subtilité : c'est la phrase du mode d'emploi.",
    "Lettre au spécialiste si la bilirubine monte sous traitement bien pris, image toujours normale, pas de fièvre. Question : stade avancé et décompensation, ou chevauchement, ou autre maladie. On joint le poids, la dose, les dates d'enzymes.",
    "Sortie. Ordonnance 60812, poids, répartition, consigne du prurit, date de bilan. Pas de 28 à 30. Pas de promesse de survie. Child-Pugh seulement si la cirrhose est là, avec 68 et 170.",
    "Ce que l'on ne retire pas. La dose 14 ± 2. Les stades I à III. L'avertissement 28 à 30. Le décalage 68 et 170. La décompensation rare. Les retirer pour raccourcir la copie la rend fausse.",
    "Phosphatase à 1,3 fois la limite, prurit, anticorps négatifs, image normale. On ne pose pas le nom. On recontrôle. On cherche une autre cause de prurit, peau, médicament, thyroïde. La maladie des petits canaux se construit sur un profil plus net ou sur une biopsie.",
    "Phosphatase à 4 fois, anticorps fortement positifs, femme de 48 ans, échographie normale, alanine normale. Le diagnostic est tenu. La biopsie n'est pas exigée pour commencer. La dose est celle de 60812, pas une dose d'attente « en attendant la biopsie ».",
    "Anticorps positifs et phosphatase normale. On ne traite pas une sérologie isolée. On surveille l'enzyme. L'information traite une maladie, pas un titre.",
    "Anticorps négatifs, phosphatase à 3 fois, image normale, femme de 55 ans. La biopsie cherche la lésion floride. Sans elle, le nom reste provisoire. On ne commence pas l'acide « au cas où » le jour de la prise de sang si le spécialiste veut d'abord le tissu.",
    "Homme de 60 ans, même biologie, anticorps positifs, image normale. Le sexe ne retire pas le diagnostic. Il le rend seulement moins habituel. La dose ne change pas. On ne dit pas « ce n'est pas ça, c'est un homme ».",
    "Fatigue seule, enzymes normales, anticorps négatifs. Ce n'est pas le fichier. On ne prescrit pas 500 mg « pour l'énergie ».",
    "Xanthélasmas et cholestérol haut. Ils accompagnent la cholestase chronique. Ils ne dosent pas l'acide. Le traitement lipidique, s'il existe, se lit dans sa propre information, pas ici.",
    "Ostéoporose. La cholestase chronique expose l'os. Ce fichier ne donne pas de dose de vitamine ni de calcium : elles n'ont pas été extraites. On le dit au spécialiste. On ne invente pas un comprimé.",
    "Grossesse. L'information se lit avec le spécialiste pour la conduite. Le cours ne fabrique pas une dose de grossesse. Le diagnostic, lui, reste le même si les anticorps et la phosphatase étaient déjà là avant.",
    "Jeune femme et contraceptif. La rubrique des calculs de cholestérol parle de contraception. La rubrique de la cholangite biliaire primitive ne se résume pas à cette phrase. On ne interdit pas toute contraception sur une mauvaise rubrique, et on ne l'autorise pas non plus sans lire l'information du contraceptif.",
    "Interaction. L'acide peut induire le cytochrome qui dégrade d'autres médicaments, dit l'information. Un traitement associé dont le métabolisme passe par là se surveille. On ne cite pas une liste de noms qui n'est pas dans l'extrait.",
    "Alcool dit en mots, au-dessus du seuil de suspicion de la maladie alcoolique. On ne met pas les deux maladies sur la même ordonnance sans les séparer. L'acide n'est pas le traitement de l'alcool. L'arrêt de l'alcool n'est pas le traitement des petits canaux.",
    "Stéatose métabolique et phosphatase haute. La stéatose n'élève pas volontiers la phosphatase autant qu'une cholangite. On dose les anticorps avant d'attribuer tout au diabète. L'acide n'est pas le traitement de la stéatose.",
    "Hémochromatose et phosphatase. La saturation et la ferritine d'abord. Une ferritine haute d'inflammation ne se saigne pas. L'acide ne traite pas le fer.",
    "Wilson. Rare à l'âge habituel de cette maladie, mais un jeune avec une hémolyse n'est pas une cholangite biliaire primitive. Leipzig se calcule dans son fichier.",
    "Insuffisance aiguë. Cette maladie chronique ne se présente pas comme une insuffisance en quelques jours, sauf décompensation. INR et confusion : Child-Pugh avec bilirubine décalée, et l'on cherche une complication, pas un premier diagnostic de petits canaux posé aux urgences.",
    "Ascite nouvelle sous traitement bien dosé. On pense à la décompensation rare. On arrête. On cherche aussi une thrombose, une infection du liquide, un carcinome. L'arrêt de l'acide n'est pas le seul geste.",
    "Carcinome. La cirrhose biliaire avancée entre dans un dépistage, comme les autres cirrhoses. Ce fichier ne donne pas un intervalle d'échographie qui n'a pas été extrait de 60812. On ne l'invente pas. On ne l'oublie pas non plus comme question au spécialiste.",
    "Réponse partielle. Phosphatase encore à 1,8 fois après un an de prise correcte, image toujours normale. On ne monte pas à 28 à 30 mg/kg/jour. On vérifie le poids, l'observance, le chevauchement. Le deuxième traitement, s'il existe, n'est pas dans l'extrait de 60812 : on ne le nomme pas.",
    "Réponse complète biologique. Phosphatase normale, bilirubine normale, prurit absent. On continue. L'information ne donne pas de date d'arrêt. Arrêter parce que « c'est normal » n'est pas écrit.",
    "Oubli d'une semaine. On reprend la dose habituelle. On ne double pas le lendemain. 14 ± 2 mg par kilogramme est une dose du jour, pas une dose à rattraper.",
    "Deux boîtes. Comprimés à 500 mg et capsules à 250 mg à la maison. On écrit laquelle est le traitement de fond et laquelle est la baisse en cas de prurit. Sinon la patiente additionne.",
    "Soir uniquement dès le jour 1. Ce n'est pas la phrase. Les trois premiers mois se répartissent. Le soir vient après l'amélioration. Inverser fait une ordonnance hors texte.",
    "Croquer. Interdit par le mode d'emploi. On le dit. Un comprimé croqué n'est pas « presque pareil ».",
    "Enfant de 12 ans, prurit, phosphatase haute, mère malade. On n'ouvre pas 60812 comme chez l'adulte : l'usage pédiatrique n'est pas étudié. On adresse. On ne rassure pas avec le comprimé de la mère.",
    "Homme avec intestin inflammatoire et image de voies irrégulières. Étiquette fausse si l'on écrit primitive. La dose de 28 à 30 mg/kg/jour est précisément celle qu'il ne faut pas lui donner. On nomme la sclérosante comme hypothèse et l'on arrête là.",
    "Bilirubine 68 µmol/l pile. Le décalage dit 68 pour le changement de point. On lit la page : 68 µmol/l pour 1 point et 170 pour 2 points. À 68, on applique la borne comme elle est écrite, sans inventer un « strictement supérieur » qui n'est pas sur la page si elle ne le dit pas. On cite 68 et 170. On ne revient pas à 50.",
    "Albumine 2,8 g/dl pile, soit 28 g/l. Borne du barème lu : 2,8 à 3,5 est la classe du milieu. On ne la mélange pas avec le facteur 0,73 de Tokyo, qui n'a rien à faire ici sans fièvre ni dilatation.",
    "INR 1,7 pile. Le barème dit inférieur à 1,7, puis 1,7 à 2,3, puis supérieur à 2,3. 1,7 entre dans la classe du milieu, pas dans la classe basse. Le point change. On ne écrit pas « INR normal ».",
    "Encéphalopathie légère et ascite modérée. Ce sont deux items distincts de Child-Pugh. Les additionner en un seul « il va mal » perd des points. Chacun a son score. Avec la bilirubine décalée, le total se refait.",
    "Classe C, 10 à 15. Une patiente à 11 n'est pas « presque B ». B s'arrête à 9. La conduite du stade avancé, surveillance et risque de décompensation sous acide, est déjà là. On ne commence pas une forte dose pour compenser la classe.",
    "Lettre de décompensation. Poids, dose exacte, date de début, bilirubine d'aujourd'hui comparée à 68 et 170, ascite oui ou non, INR, conscience, décision d'arrêt. Le correspondant doit voir que l'on a reconnu l'effet rare, pas une simple fatigue.",
    "Copie modèle. Femme, prurit, phosphatase haute, anticorps, image normale, poids, 14 ± 2 mg par kilogramme, comprimés 500 mg, numéro 60812, trois mois répartis, pas de promesse de survie, pas de 28 à 30. Huit éléments. Le grade de Tokyo n'y est pas, parce qu'il n'y a pas de fièvre.",
    "Copie modèle du piège. On montre 60 µmol/l de bilirubine, on refuse 3 points, on donne 1 point parce que 60 est sous 68, on recalcule la classe. Une ligne de calcul vaut plus qu'un paragraphe de définition.",
    "Quatre patientes, une seule dose. Toutes sont aux stades I à III, image normale, anticorps positifs. Les poids diffèrent. Chacune a 14 ± 2 mg par kilogramme, pas la même boîte copiée. Le numéro 60812 est le même. Le nombre de comprimés de 500 mg change. Écrire « deux comprimés pour tout le monde » est faux.",
    "Prurit avant toute enzyme. On cherche d'abord la phosphatase. Si elle est normale et les anticorps négatifs, on ne pose pas le diagnostic ce jour-là. Le prurit a d'autres causes. L'acide n'est pas un antiprurigineux général.",
    "Ictère sans prurit, phosphatase à 5 fois, anticorps positifs, voies fines. Le prurit n'est pas obligatoire. Le diagnostic tient. On ne l'écarte pas parce que la patiente ne se gratte pas.",
    "Phosphatase normale, gamma-glutamyltransférase à 6 fois, anticorps positifs, image normale. La gamma-glutamyltransférase peut porter le profil. On ne exige pas que les deux enzymes soient hautes. On écarte quand même l'alcool et le médicament, qui montent volontiers cette enzyme.",
    "Alanine à 2 fois, phosphatase à 3 fois. R se calcule. Si R reste au plus égal à 2, le profil reste cholestatique et ce fichier reste ouvert. Si R passe au-dessus de 5, on ouvre Hennes en parallèle. Les deux scores ne se remplacent pas.",
    "Biopsie : lésion floride, anticorps négatifs, image normale. Le troisième critère de Paris côté biliaire est là, et le diagnostic de la maladie peut se tenir sans l'anticorps. On le dit avec le compte rendu, pas avec une impression.",
    "Biopsie non floride, anticorps négatifs, phosphatase haute. On ne force pas le nom. On reprend l'obstacle, le médicament, l'infiltration. L'acide n'est pas un test thérapeutique autorisé hors étude dans une cholestase non caractérisée.",
    "Suivi à un mois. Phosphatase encore haute, prurit stable, pas de fièvre, pas d'ictère nouveau. On continue. Un mois n'est pas un échec. Les trois mois de répartition ne sont pas non plus le jury de la réponse.",
    "Suivi à un an, tout est normal, elle veut arrêter. L'information ne limite pas la durée aux stades I à III. On explique. L'arrêt, s'il se discute, n'est pas une phrase de ce fichier. On ne l'invente pas pour faire plaisir.",
    "Erreur de solvant. Elle prend le comprimé sans eau, croqué. On corrige les deux : liquide, et ne pas croquer. La dose chiffrée était juste, la prise était fausse. Les deux comptent.",
    "Erreur de soir précoce. Jour 4, toute la dose au coucher, enzymes pas encore améliorées. On revient à la répartition diurne. Le soir est une récompense de l'amélioration, pas une préférence.",
    "Association avec le corticoïde. Seulement si Paris est rempli et que l'hépatite a son indication, informations 29348 et 31887. Sinon le corticoïde n'est pas le traitement des petits canaux. On ne l'ajoute pas « pour la fatigue ».",
    "Ce que la page de Child-Pugh change et ne change pas. Elle change 34 et 50 en 68 et 170 pour la bilirubine de cette maladie et de la sclérosante. Elle ne change pas l'albumine, l'INR, l'ascite, l'encéphalopathie, ni les bornes 5, 7 et 10 des classes. Une copie qui décale aussi l'albumine a trop lu.",
    "Dernière ligne. Stades I à III, 14 ± 2 mg par kilogramme, 500 mg, 60812, pas 28 à 30 mg/kg/jour, pas d'autre cholestase hors étude, bilirubine 68 et 170 si cirrhose, décompensation rare réversible à l'arrêt, pas de promesse de survie. Si une de ces lignes manque, la copie est incomplète même si elle est longue.",
    "Cas 34 µmol/l de bilirubine. Dans le barème habituel, c'est la borne. Dans le barème décalé de cette maladie, 34 est très en dessous de 68 : 1 point, pas 2. On ne importe pas le 34 de Tokyo ni le 34 de Child habituel comme si c'était le seuil de gravité ici.",
    "Cas 170 µmol/l. C'est la borne lue pour 2 points dans le barème décalé. Au-dessus, 3 points. On écrit 170 à côté du résultat. On ne le remplace pas par 300, qui est un seuil de King, ni par 85,5, qui est un item de Tokyo.",
    "Cas d'ascite cotée à part. Ascite contrôlée par le traitement et ascite tendue ne valent pas le même item dans le barème classique, mais ce fichier ne réécrit pas les sous-scores d'ascite au-delà de ce qui a été lu : on cote l'ascite présente ou absente selon la page, et l'on ne invente pas un troisième niveau.",
    "Encéphalopathie. Absente : le point bas. Présente : on ne la confond pas avec la fatigue de la maladie. Une confusion nouvelle sous acide, au stade avancé, fait partie du tableau de décompensation. On arrête et l'on hospitalise, on ne donne pas un somnifère.",
    "Image de contrôle. Une échographie normale au diagnostic ne dispense pas de la refaire si l'ictère apparaît ou si la fièvre vient. L'obstacle peut s'ajouter à la maladie chronique. Tokyo reprend alors la main, l'acide ne la garde pas.",
    "Numéro sur l'ordonnance. 60812 à côté du nom Ursofalk et de 500 mg. Sans le numéro, la dose n'est pas montrée comme suisse dans ce lot. Avec le numéro et hors de 14 ± 2 mg par kilogramme, la dose est suisse mais fausse. Les deux conditions.",
    "Comparaison finale des trois acides qu'il ne faut pas mélanger. L'acide de 60812 pour les stades I à III. Le corticoïde de 29348 et le thiopurine de 31887 pour l'hépatite, pas pour les petits canaux seuls. L'antidote de 31954 pour l'intoxication, jamais ici. Trois informations, trois maladies.",
    "Mémo chiffré à recopier en bas de copie. Indication : stades I à III. Dose : environ 10 mg par kilogramme, précisée en 14 ± 2 mg par kilogramme, comprimés de 500 mg, capsules de 250 mg si l'on baisse pour un prurit ou si le poids est sous 47 kg. Interdit : 28 à 30 mg/kg/jour, et toute autre cholestase hors étude. Child-Pugh : bilirubine 68 puis 170 µmol/l, classes A B et C entières. Surveillance du stade avancé parce qu'une décompensation rare régresse à l'arrêt. Survie : non affirmée. Ce bloc suffit à ne rien amputer.",
    "On relit enfin l'unité. La bilirubine suisse est en µmol/l. 68 et 170 sont déjà en µmol/l. Les y convertir une seconde fois les multiplie par 17,1 et invente un score impossible. On convertit seulement ce qui était en mg/dl, pas ce qui est déjà en µmol/l.",
]

def main():
    fen.append((11, W("w-long7", "Chaque phrase de l'information", "\n".join(P(p, 9, 12) for p in LONGS))))
    fen.append((14, W("w-cas7b", "Poids, barème, erreurs", "\n".join(P(p, 9, 12, 16, 18) for p in CAS))))
    essentiel = (
        P("Ursofalk 60812, stades I à III, environ 10 mg/kg et 14 ± 2 mg/kg, comprimés à 500 mg. Pas 28 à 30 mg/kg/jour.", 12)
        + P("Child-Pugh : bilirubine décalée à 68 et 170 µmol/l. Décompensation rare du stade avancé, réversible à l'arrêt.", 9, 12)
    )
    phrases = {
        1: "Petits canaux, pas un calcul. Stades I à III pour l'acide.",
        2: "Pas de prévalence suisse lue. L'information ne promet pas la survie.",
        3: "Destruction des petits canaux, enzymes d'abord, ictère ensuite.",
        4: "Anticorps, phosphatase, image normale. R en général cholestatique.",
        5: "Prurit, fatigue, maladies immunes. La fièvre fait changer de fichier.",
        6: "Souvent normal au début. Ascite et confusion : Child-Pugh décalé.",
        7: "Chronique, prurit de début de traitement, décompensation rare, chevauchement.",
        8: "Antimitochondries et profil. Biopsie si les anticorps manquent.",
        9: "Enzymes, anticorps, échographie. Pas de seuil d'élastographie inventé.",
        10: "Image anormale : sortir. Image normale : 60812. Sclérosante : pas 28 à 30.",
        11: "14 ± 2 mg par kilogramme. Demi-comprimé si le prurit explose. Pas de date de fin.",
        12: "Surveiller la fonction, surtout au stade avancé. Pas un seul contrôle.",
        13: "Trois phrases de preuve : enzymes oui, histologie peu, survie non affirmée.",
        14: "50 µmol/l n'est pas le seuil de bilirubine de cette maladie dans le Child-Pugh.",
    }
    fiches = {n: P(phrases[n], 12) for n in phrases}
    sources = [
        f"{AIPS} Ursofalk, Swissmedic 60812.{S(12)}",
        f"Child-Pugh, bilirubine décalée à 68 et 170 µmol/l pour cette maladie.{S(9)}",
        f"{EASL}, hépatite auto-immune, 2015, critères de Paris si chevauchement.{S(7)}",
        f"Tokyo Guidelines 2018, si fièvre et dilatation.{S(18)}",
    ]
    sous = (
        f"Diagnostic différentiel DX.7 de {A('situation de départ F2.11 de PROFILES','F2.11')} "
        f"« Enzymes hépatiques anormales ». Texte du 31.10.2026."
    )
    par = {}
    for point, html in fen:
        par.setdefault(point, []).append(html)
    path = construire(7, "Cholangite biliaire primitive", essentiel, sous, fiches, par, sources)
    print(path)

if __name__ == "__main__":
    main()
