#!/usr/bin/env python3
"""DX.5 Obstacle biliaire extra-hépatique."""
from base_dx import P, W, construire, A
from moteur import S

ALAT = A("alanine aminotransférase", "ALAT")
ASAT = A("aspartate aminotransférase", "ASAT")
PAL = A("phosphatase alcaline", "PAL")
GGT = A("gamma-glutamyltransférase", "GGT")
LSN = A("limite supérieure de la normale", "LSN")
INR = A("international normalized ratio", "INR")
EASL = A("European Association for the Study of the Liver", "EASL")

def F(point, ident, titre, textes, *refs):
    return point, W(ident, titre, "\n".join(P(t, *refs) for t in textes))

fen = []
fen.append(F(1, "d5", "Ce que le nom recouvre", [
    f"L'obstacle extra-hépatique est une cholestase dont le blocage est dans la voie biliaire principale ou plus bas, pas dans le canalicule de l'hépatocyte. Calcul, sténose, tumeur de la tête du pancréas, compression, prothèse bouchée : la liste des causes reste ouverte, le mécanisme est le même.",
    f"Le profil biologique est cholestatique : R au plus égal à 2, ou une {PAL} au moins à deux fois la {LSN}. R = ({ALAT} / {LSN}) / ({PAL} / {LSN}), sur le premier bilan. R égal à 2 est déjà cholestatique. Le mixte commence au-dessus de 2.",
    "L'angiocholite est cet obstacle plus une infection. Elle ne se résume pas à la triade de Charcot. Tokyo 2018 demande une inflammation systémique, obligatoire, plus une cholestase, plus une image.",
], 2, 18))
fen.append(F(3, "ph5", "Physiopathologie", [
    f"La bile ne s'écoule plus. La pression monte dans les canaux. La {PAL} et la {GGT} montent, la bilirubine conjuguée ensuite. L'hépatocyte souffre en second : l'{ALAT} peut monter, mais R reste bas si la phosphatase monte davantage.",
    "L'infection vient quand le liquide stagnant se colonise. L'endotoxine passe dans le sang. La fièvre et le choc ne mesurent pas la taille du calcul, ils mesurent la réponse. Un petit calcul impacté peut donner un grade III.",
    "La levée de l'obstacle, par endoscopie le plus souvent, fait baisser la pression. L'antibiotique sans drainage laisse le foyer en place quand le grade l'exige. Le drainage sans antibiotique laisse l'infection.",
], 18))
fen.append(F(3, "et5", "Causes classées, aucune retirée", [
    "Lithiase de la voie biliaire principale, y compris le calcul qui est déjà passé et laisse une papillotomie à discuter. Sténose bénigne après chirurgie ou après pancréatite. Tumeur : tête du pancréas, cholangiocarcinome, ampullome. Compression ganglionnaire. Prothèse ou drain déjà en place, bouché ou migré.",
    "Ce qui n'est pas extra-hépatique et que l'on n'étiquette pas ainsi : cholangite biliaire primitive, cholangite sclérosante des petits canaux, cholestase médicamenteuse sans dilatation, sepsis sans obstacle. L'échographie ou le scanner tranche la dilatation. Sans image, on ne pose pas le nom.",
    f"Profil mixte, R entre 2 et 5 : l'obstacle reste possible, l'hépatite aussi. On ne classe pas « obstacle » sur une {ALAT} à dix fois la limite et une phosphatase normale.",
], 2, 18))
fen.append(F(8, "tg5", "Diagnostic Tokyo 2018, trois piliers", [
    "Inflammation systémique, obligatoire : fièvre au-dessus de 38 °C ou réponse inflammatoire. Sans elle, on n'a pas l'angiocholite, on a peut-être un obstacle froid.",
    "Cholestase : bilirubine au moins égale à 2 mg/dl, soit environ 34 µmol/l puisque 1 mg/dl vaut 17,1 µmol/l, ou bien phosphatase, gamma-glutamyltransférase ou aminotransférases au-dessus de 1,5 fois la norme.",
    "Image : dilatation, calcul, sténose ou prothèse. Les trois piliers se lisent ensemble. Deux sans le troisième ne portent pas le diagnostic d'angiocholite.",
    "Charcot. Des séries récentes donnent une sensibilité de 26,4 % et de 21,2 %. Les séries plus anciennes donnaient 50 à 70 %. L'absence de la triade n'écarte pas la maladie. Attendre le frisson, l'ictère et la douleur pour appeler le drainage fait perdre des grades II.",
    "Le taux de diagnostic de la version 2013 est de 90,0 % (5 454 sur 6 063), contre 79,4 % pour la version 2007. On enseigne 2018, qui reprend cette logique, pas un souvenir de la triade seule.",
], 18))
fen.append(F(8, "gr5", "Grades I, II et III, aucun en moins", [
    "Grade I : le patient ne remplit ni le grade II ni le grade III. Antibiotique. Drainage si l'évolution ne répond pas. Ce n'est pas « bénin, on verra demain » sans heure de réévaluation.",
    "Grade II : au moins deux items parmi les suivants. Leucocytes au-dessus de 12 000/mm³ ou en dessous de 4 000/mm³. Fièvre au moins égale à 39 °C. Âge au moins égal à 75 ans. Bilirubine au moins égale à 5 mg/dl. Hypoalbuminémie.",
    "5 mg/dl de bilirubine valent 85,5 µmol/l. On n'arrondit pas à 50 µmol/l : 50 µmol/l est un seuil du Child-Pugh, pas de Tokyo. Un ictère à 60 µmol/l ne coche pas cet item.",
    "L'hypoalbuminémie du grade II : le texte de Miura compare à 0,73 fois la limite inférieure du laboratoire. Le tableau lu imprime un facteur 0,7. On garde l'item. On cite les deux impressions. On ne retire pas l'albumine parce que le facteur hésite.",
    "Grade III : un seul organe suffit. Cardiovasculaire : dopamine d'au moins cinq microgrammes par kilogramme et par minute, ou n'importe quelle noradrénaline. Conscience altérée. Rapport PaO2/FiO2 inférieur à 300. Oligurie ou créatinine au-dessus de 2,0 mg/dl. INR au-dessus de 1,5. Plaquettes inférieures à 100 000/mm³.",
    "Créatinine 2,0 mg/dl vaut environ 177 µmol/l (facteur 88,4). Ce n'est pas le seuil de 300 µmol/l des critères de King pour l'antalgique. Un patient à 200 µmol/l peut être en grade III sans remplir la porte rénale de King.",
    "Les plaquettes inférieures à 100 000/mm³ sont lues. Elles suffisent, à elles seules, pour le grade III. On ne les remplace pas par un « bilan de coagulation global ».",
], 9, 18))
fen.append(F(4, "de5", "Démarche", [
    f"Premier geste : constantes, bilirubine, {PAL}, {GGT}, {ALAT}, leucocytes, albumine, créatinine, {INR}, plaquettes. On ne attend pas l'image pour prélever.",
    "R se calcule. S'il est au plus égal à 2, l'image est urgente. S'il est au moins égal à 5, on ne part pas au drainage pour une hépatite. Entre les deux, les deux bilans partent.",
    "Puis le grade. Grade I : antibiotique et réévaluation. Grade II : au moins deux items, drainage précoce. Grade III : un organe, réanimation et drainage. On n'inverse pas l'ordre en attendant une bilirubinémie « plus belle ».",
], 2, 18))
fen.append(F(5, "an5", "Anamnèse", [
    "Colique biliaire ancienne, cholécystectomie, prothèse déjà posée, amaigrissement, selles décolorées, urines foncées, prurit, fièvre à domicile. Chaque item change la cause, pas le grade : le grade se lit sur les organes.",
    "Médicament récent et R cholestatique : l'obstacle et le médicament coexistent jusqu'à l'image. Une image normale fait revenir au score de causalité. Une dilatation fait Tokyo.",
], 2, 18))
fen.append(F(6, "ex5", "Examen", [
    "Fièvre, ictère, douleur de l'hypocondre droit, défense, confusion, marbrures, pression artérielle. La triade complète est peu sensible. Un seul signe manque souvent. L'examen cherche le grade III : conscience, pression, diurèse, polypnée.",
    "Un Murphy et une fièvre sans ictère restent une cholécystite jusqu'à preuve d'une voie biliaire principale touchée. On ne les range pas d'office dans ce diagnostic.",
], 18))
fen.append(F(7, "sy5", "Syndromes", [
    "Obstacle froid : ictère, selles décolorées, R cholestatique, pas de fièvre. Angiocholite : inflammation obligatoire plus cholestase plus image. Pancréatite biliaire : lipase, douleur transfixiante, l'obstacle peut être le même calcul.",
    "Le sepsis d'une autre porte, poumon ou urine, peut élever les enzymes sans dilatation. L'image négative et une autre source arrêtent le drainage.",
], 18))
fen.append(F(9, "la5", "Examens", [
    f"Biologie du grade avant l'image : leucocytes, bilirubine en µmol/l avec la conversion si l'on compare à 2 ou 5 mg/dl, albumine, créatinine, {INR}, plaquettes, {PAL}, {GGT}, {ALAT}.",
    "Échographie en premier pour la dilatation et le calcul vésiculaire. Si elle ne voit pas la voie biliaire principale et que la clinique tient, scanner ou écho-endoscopie selon le plateau. On ne conclut pas « pas de calcul » sur une échographie non conclusive.",
    "Hémocultures avant l'antibiotique si le prélèvement ne retarde pas l'injection chez le grade III. Le germe ne change pas le grade déjà posé.",
], 18))
fen.append(F(10, "ar5", "Arbre", [
    "Pas de fièvre et pas de réponse inflammatoire : obstacle froid possible, drainage selon la cause, pas le circuit de l'angiocholite.",
    "Trois piliers réunis, aucun item de grade II, aucun organe de grade III : grade I. Antibiotique. Drainage seulement si ça ne répond pas.",
    "Au moins deux items de grade II, pas d'organe de grade III : grade II. Drainage précoce, pas après-demain.",
    "Un seul organe de grade III : réanimation et drainage. La noradrénaline, quelle que soit la dose, suffit pour l'item cardiovasculaire. La dopamine ne suffit qu'à partir de cinq microgrammes par kilogramme et par minute.",
], 18))
fen.append(F(11, "su5", "Prise en charge", [
    "Grade I : antibiotique adapté au germe biliaire du protocole local, boire si c'est possible, réévaluer à court terme. Si la fièvre et la bilirubine ne baissent pas, on passe au drainage : c'est la phrase du grade I, pas une option.",
    "Grade II et III : le drainage endoscopique est le geste qui lève l'obstacle. L'antibiotique commence tout de suite, il ne remplace pas le geste. Le choc se remplit et se soutient en parallèle.",
    "On ne donne pas l'acide ursodésoxycholique pour « fluidifier ». L'information 60812 le réserve à la cholangite biliaire primitive. Un calcul de la voie biliaire principale n'est pas cette indication.",
    f"Child-Pugh ne décide pas l'heure du drainage. Il décrit une cirrhose. Ici le score qui décide est Tokyo. L'{INR} au-dessus de 1,5 est un organe du grade III, pas un point de Child à commenter à la place.",
], 9, 12, 18))
fen.append(F(12, "pv5", "Prévention", [
    "Une vésicule lithiasique symptomatique se discute avant l'angiocholite, pas après la troisième. Une prothèse déjà en place a une date de changement. L'ictère qui revient chez un patient prothésé est une obstruction jusqu'à preuve du contraire.",
], 18))
fen.append(F(13, "cl5", "Points de la copie", [
    "Trois piliers. Trois grades. Grade II : au moins deux items, avec la bilirubine à 5 mg/dl soit 85,5 µmol/l, et l'albumine citée malgré les deux facteurs 0,73 et 0,7. Grade III : un organe, plaquettes inférieures à 100 000/mm³ comprises.",
    "Charcot peu sensible, 26,4 % et 21,2 % dans les séries récentes. R au plus égal à 2. Pas d'acide ursodésoxycholique à la place du drainage.",
], 12, 18))
fen.append(F(14, "pi5", "Pièges", [
    "Attendre la triade. Arrondir 5 mg/dl à 50 µmol/l. Oublier les plaquettes. Compter deux items de grade II et appeler ça un grade III, ou l'inverse. Mettre une noradrénaline et rester en grade II. Donner le schéma de l'antalgique ou l'acide ursodésoxycholique.",
    "Confondre 2 mg/dl (environ 34 µmol/l, pilier diagnostique) et 5 mg/dl (85,5 µmol/l, item de grade II). Les deux seuils coexistent.",
], 12, 18))
fen.append(F(14, "cas5", "Cas corrigé, grade I puis grade II", [
    "Homme de 60 ans. Fièvre à 38,4 °C, leucocytes à 9 000/mm³, bilirubine à 40 µmol/l (environ 2,3 mg/dl), phosphatase à 2 fois la limite, échographie avec voie biliaire dilatée et calcul du bas cholédoque. Albumine normale, créatinine normale, INR 1,1, plaquettes 180 000/mm³, conscience claire, pas d'amine.",
    "Diagnostic : les trois piliers sont là. Grade II ? Un seul item possible serait la bilirubine, mais 40 µmol/l n'atteint pas 85,5. L'âge est 60, pas 75. La fièvre est sous 39 °C. Les leucocytes sont entre 4 000 et 12 000. Aucun organe de grade III. Grade I. Antibiotique, et drainage si la réponse manque. On ne le classe pas II « parce qu'il y a un calcul ».",
    "Le lendemain, il a 78 ans dans une variante, ou bien c'est un autre patient de 78 ans, bilirubine à 100 µmol/l, même image, même absence d'organe défaillant. Âge au moins 75 et bilirubine au-dessus de 85,5 µmol/l : deux items. Grade II. Drainage précoce. La variante ne se traite pas comme le premier homme.",
    "Troisième patient. 70 ans, noradrénaline en cours, bilirubine à 30 µmol/l, image positive, fièvre. Un organe cardiovasculaire suffit : grade III, même si aucun item de grade II n'est complet. La dose d'amine n'a pas à dépasser un seuil chiffré : n'importe quelle noradrénaline coche.",
], 18))

LONGS = [
    "Le pilier inflammatoire est obligatoire. Une dilatation sans fièvre et sans syndrome inflammatoire est un obstacle, pas une angiocholite. Le mot du diagnostic change le délai du drainage.",
    "La fièvre au-dessus de 38 °C coche le pilier. La fièvre au moins égale à 39 °C coche un item du grade II. 38,5 °C fait le diagnostic possible, pas le grade II. On ne confond pas les deux thermomètres.",
    "Les leucocytes du grade II sont au-dessus de 12 000 ou en dessous de 4 000 par mm³. 11 000 ne coche pas. 3 500 coche. Une leucopénie est un item, pas un argument pour récuser l'infection.",
    "L'âge d'au moins 75 ans est un item, pas une décoration. À 74 ans révolus, l'item n'est pas là. On calcule, on n'écrit pas « sujet âgé ».",
    "La bilirubine diagnostique, 2 mg/dl, et la bilirubine de gravité, 5 mg/dl, ne se remplacent pas. 34 µmol/l ouvre le pilier. 85,5 µmol/l ouvre l'item de grade II. Entre les deux, le diagnostic peut être posé sans que le grade II le soit.",
    "Convertir avec 17,1. 2 fois 17,1 font 34,2, que l'on enseigne comme environ 34. 5 fois 17,1 font 85,5. L'arrondi à 50 µmol/l est une confusion avec le Child-Pugh, dont la bilirubine à 2 points commence au-dessus de 50 µmol/l dans le barème habituel, et à 68 puis 170 dans la cholangite biliaire primitive.",
    "L'albumine de Tokyo n'est pas l'albumine de Child-Pugh. Child : plus de 3,5 g/dl, de 2,8 à 3,5, moins de 2,8. En g/l, facteur dix : plus de 35, de 28 à 35, moins de 28. Tokyo : 0,73 fois la limite basse du laboratoire selon Miura, 0,7 sur le tableau lu. Mélanger 28 g/l et ce facteur classe mal.",
    "Les plaquettes inférieures à 100 000/mm³ sont un organe hématologique du grade III. 120 000 ne coche pas. 90 000 coche, même si l'INR est normal et la conscience claire. Un seul organe suffit.",
    "L'INR au-dessus de 1,5 est un autre organe du grade III. Il ne double pas l'item des plaquettes : chacun suffit seul. Les deux ensemble restent un grade III, pas un grade « IV » qui n'existe pas.",
    "La créatinine au-dessus de 2,0 mg/dl, environ 177 µmol/l, est l'item rénal, au même titre que l'oligurie. L'un ou l'autre coche. 150 µmol/l sans oligurie ne coche pas. 200 µmol/l coche, et pourtant reste sous les 300 µmol/l de King.",
    "Le rapport PaO2/FiO2 inférieur à 300 est l'item respiratoire. On ne le remplace pas par « le patient est essoufflé ». Si le gaz n'est pas fait, on ne l'invente pas. On dit que l'item n'est pas mesuré.",
    "La conscience altérée coche, sans score de Glasgow imposé par le texte lu. Une confusion nouvelle chez un ictérique fébrile est un grade III jusqu'à ce qu'une autre cause soit prouvée, et le drainage ne se diffère pas pour un scanner cérébral si le ventre est le foyer.",
    "Dopamine : le seuil se dit en toutes lettres, au moins cinq microgrammes par kilogramme et par minute. En dessous, l'item cardiovasculaire n'est pas coché par la dopamine. La noradrénaline, elle, coche dès qu'elle est perfusée.",
    "Grade I n'est pas l'absence de maladie. C'est l'angiocholite qui n'a ni deux items de II ni un organe de III. L'antibiotique est là. Le drainage arrive si la réponse manque. Oublier cette deuxième phrase transforme le grade I en abstention.",
    "Grade II exige au moins deux items. Un seul, même spectaculaire comme une fièvre à 39,5 °C, ne suffit pas si l'âge, les leucocytes, la bilirubine et l'albumine ne suivent pas. On compte sur les doigts.",
    "Grade III n'exige pas les items du grade II. Un jeune adulte en choc, sans bilirubine à 5 mg/dl, est en grade III. Attendre qu'il « mérite » aussi le grade II retarde le drainage.",
    "La sensibilité de Charcot à 26,4 % et 21,2 % interdit d'écrire « pas d'angiocholite, la triade est incomplète ». Les séries anciennes à 50-70 % ne restaurent pas cette exigence.",
    "Le taux diagnostique de 90,0 % contre 79,4 % se cite avec les versions 2013 et 2007. Il ne se transforme pas en sensibilité de l'échographie.",
    "R se calcule avant de parler de drainage. R à 8 est hépatocellulaire. Une voie biliaire fine et une alanine très haute orientent vers une hépatite, pas vers une sphinctérotomie.",
    "R à 1,2 avec fièvre et dilatation : le profil et l'image concordent. On ne perd pas de temps à chercher d'abord une hépatite auto-immune.",
    "R à 3, mixte : image et sérologies partent ensemble. Le grade ne se pose que si les trois piliers de l'angiocholite sont réunis. Un R mixte sans fièvre n'est pas une angiocholite.",
    "La prothèse bouchée est une cause d'obstacle au même titre que le calcul. L'image le dit. Le grade se calcule de la même façon. On ne crée pas un grade spécial « prothèse ».",
    "La tumeur de la tête du pancréas donne souvent un obstacle froid, sans fièvre. Le drainage est celui de la décompression et du diagnostic, pas le circuit du grade II infecté. Si la fièvre s'y ajoute, Tokyo reprend ses droits.",
    "La cholécystite sans dilatation de la voie principale n'est pas ce diagnostic. Douleur, Murphy, vésicule lithiasique, voies fines : autre filière. On ne la « surclasse » pas en angiocholite pour obtenir une endoscopie.",
    "La pancréatite biliaire partage le calcul et pas toujours le grade. La lipase haute se note. Le grade de Tokyo ne se remplace pas par un score de pancréatite, et l'inverse non plus.",
    "L'acide ursodésoxycholique, information 60812, est indiqué dans la cholangite biliaire primitive aux stades I à III. Il est déconseillé dans les autres cholestases intrahépatiques hors étude. Il n'est pas le traitement d'un calcul du cholédoque.",
    "Une décompensation de cirrhose a été observée, très rare, sous cet acide dans la cholangite biliaire primitive avancée. Raison de plus pour ne pas le poser sur un ictère obstructif non caractérisé.",
    "Child-Pugh A, B et C restent 5-6, 7-9 et 10-15, avec les cinq items, mais ils ne datent pas l'endoscopie. Les citer à la place du grade est une copie hors sujet.",
    "L'insuffisance aiguë, INR en général au-dessus de 1,5 et encéphalopathie sans cirrhose, peut croiser un grade III. Si l'image montre l'obstacle, on draine. Si l'image est vide et que les enzymes sont massives, on pense ischémie, antalgique, virus, et aux critères de King.",
    "Ischémie : enzymes très hautes, lacticodéshydrogénase, créatinine, chute après stabilisation. Pas de dilatation. Pas de drainage.",
    "Médicament : R hépatocellulaire, pas de fièvre, image normale. Score de causalité, pas Tokyo.",
    "Hépatite auto-immune aiguë : elle peut manquer d'anticorps. Elle n'élargit pas la voie biliaire. L'image normale fait quitter ce fichier.",
    "Virus A ou E : tableau aigu, parfois cholestatique en queue d'évolution, image sans obstacle. On ne sphinctérotomise pas une hépatite A.",
    "Alcool : profil avec ASAT rarement au-dessus de 300 U/l, pas une dilatation. Maddrey n'est pas Tokyo.",
    "La copie minimale : trois piliers oui ou non, grade avec les items comptés, conversion de la bilirubine montrée, geste (antibiotique seul avec réévaluation, ou drainage précoce, ou réanimation). Sans le compte des items, le nom du grade est une étiquette.",
    "La copie qui perd les points : « ictère fébrile, antibiotique ». Il manque l'image et le grade. « Charcot incomplet, ce n'est pas ça ». Faux à cause de la sensibilité. « Bilirubine 60 µmol/l, grade II ». Faux, le seuil est 85,5. « Plaquettes à 80 000, on surveille ». Faux, c'est un grade III.",
    "Lettre à l'endoscopiste : âge, fièvre exacte, leucocytes, bilirubine en µmol/l et en mg/dl, albumine, créatinine, INR, plaquettes, amines oui ou non, image, grade conclu. Une lettre sans plaquettes ni INR peut cacher un grade III.",
    "Retour de salle : heure de l'antibiotique, heure du drainage, grade écrit dans le dossier, consigne de réévaluation si l'on était en grade I. Le patient de grade I sans heure de revue est un grade I abandonné.",
]

AJOUTS = [
    "On écrit les unités à chaque item. Par mm³ pour les leucocytes et les plaquettes. mg/dl et µmol/l pour la bilirubine, les deux, avec 17,1. mg/dl et µmol/l pour la créatinine, avec 88,4. g/dl ou le facteur du laboratoire pour l'albumine, jamais le barème de Child à la place.",
    "Un patient peut cumuler un item de grade II et un organe de grade III. Le grade retenu est III. Le plus grave l'emporte. On ne fait pas la moyenne.",
    "Deux items de grade II plus un INR à 1,6 : grade III à cause de l'INR, pas « II fort ». L'organe suffit.",
    "Fièvre à 39 °C et leucocytes à 13 000, âge 50 ans, bilirubine 40 µmol/l, albumine normale, aucun organe : deux items, grade II. Le drainage est précoce même si le patient « a l'air bien ».",
    "Fièvre à 38,2 °C seule, tout le reste normal, image positive : grade I. On n'emprunte pas l'âge ou la bilirubine du voisin de chambre.",
    "Hypoalbuminémie isolée plus âge de 80 ans, sans fièvre haute ni leucocytes extrêmes ni bilirubine à 5 mg/dl : deux items si l'albumine est vraiment sous le facteur lu. On cite 0,73 et 0,7 plutôt que d'effacer l'item.",
    "Plaquettes à 95 000/mm³, tout le reste rassurant, trois piliers présents : grade III hématologique. Le drainage et la réanimation selon l'état, pas un simple contrôle de numération le lendemain comme seule réponse.",
    "Noradrénaline à petite dose : l'item est coché. On ne demande pas un débit minimal. La phrase lue est : n'importe quelle noradrénaline.",
    "Dopamine en dessous du seuil de cinq microgrammes par kilogramme et par minute : l'item n'est pas coché par cette amine. S'il n'y a pas d'autre organe, on ne fabrique pas un grade III.",
    "PaO2/FiO2 à 280 : item respiratoire, grade III. À 350 : pas cet item. On ne l'estime pas au lit sans le gaz.",
    "Oligurie : l'item rénal est coché même si la créatinine n'a pas encore atteint 2,0 mg/dl. La créatinine monte en retard. Attendre le chiffre de 177 µmol/l chez un anurique est une faute.",
    "Image douteuse et grade III clinique : on ne renvoie pas le patient au lit « en attendant une meilleure échographie demain ». On poursuit l'imagerie tout de suite.",
    "Hémocultures négatives : elles n'annulent pas un grade déjà posé sur les trois piliers. Le germe manque souvent. Le drainage ne dépend pas du nom du germe.",
    "Antibiotique commencé aux urgences avant l'appel : on note l'heure, on ne recommence pas la dose, on ne retarde pas le drainage pour « laisser l'antibiotique agir » quand le grade est II ou III.",
    "Grade I qui ne répond pas : la définition elle-même dit de drainer. La copie qui laisse le grade I sans cette phrase est incomplète.",
    "Obstacle froid chez un patient de 80 ans, bilirubine à 200 µmol/l, pas de fièvre, pas de syndrome inflammatoire : pas d'angiocholite. La bilirubine haute ne fabrique pas le grade II sans le pilier inflammatoire. On décomprime selon la cause tumorale ou lithiasique, avec un autre raisonnement.",
    "Selles toujours colorées et voie biliaire fine : l'obstacle complet est peu probable. On retourne au profil R et aux autres diagnostics du chapitre.",
    "Prurit isolé, phosphatase haute, femme, anticorps antimitochondries : on quitte ce fichier pour la cholangite biliaire primitive. Pas de calcul, pas de Tokyo.",
    "Le schéma 31954 de l'acétylcystéine n'a pas sa place ici. Ni Maddrey. Ni le score simplifié d'hépatite auto-immune, sauf si l'image est normale et que le profil redevient hépatocellulaire.",
    "La prévalence suisse de l'obstacle parmi les dix diagnostics n'a pas été lue. On ne l'invente pas. Le rang d'urgence de l'algorithme place l'obstacle infecté haut, parce qu'il tue vite, pas parce qu'un pourcentage suisse a été publié dans ce lot.",
]

CAS = [
    "Femme de 82 ans, fièvre 38,3 °C, leucocytes 8 000/mm³, bilirubine 90 µmol/l, albumine normale, image de calcul du cholédoque. Items de grade II : âge au moins 75, et bilirubine au-dessus de 85,5 µmol/l. Deux items. Pas d'organe. Grade II. Drainage précoce. La fièvre sous 39 °C n'enlève pas les deux items déjà là.",
    "Homme de 44 ans, fièvre 39,6 °C, leucocytes 14 000/mm³, bilirubine 36 µmol/l, âge loin de 75, albumine normale. Deux items : fièvre et leucocytes. Bilirubine diagnostique seulement, pas l'item de gravité. Grade II quand même. On ne dit pas grade I parce que l'ictère est modeste.",
    "Femme de 50 ans, fièvre 38,1 °C, leucocytes 3 200/mm³, tout le reste du grade II normal, image positive, pression normale. Un seul item, la leucopénie. Grade I, pas II. Antibiotique et heure de réévaluation. On n'emprunte pas un second item.",
    "Homme de 76 ans, pas de fièvre, leucocytes normaux, bilirubine 20 µmol/l, albumine basse sous le facteur du laboratoire, image douteuse, pas de syndrome inflammatoire. Le pilier inflammatoire manque. On ne pose pas l'angiocholite. L'âge et l'albumine ne créent pas la maladie.",
    "Femme de 33 ans, pression maintenue par noradrénaline, fièvre 38,7 °C, bilirubine 50 µmol/l, voie biliaire dilatée. Grade III cardiovasculaire. La bilirubine à 50 µmol/l n'est même pas l'item des 85,5. Le grade III n'en a pas besoin.",
    "Homme de 68 ans, plaquettes 88 000/mm³, INR 1,2, conscience claire, fièvre 38,5 °C, calcul du cholédoque. L'item plaquettaire suffit au grade III. On ne le laisse pas en grade I sous prétexte que le reste est calme.",
    "Femme de 71 ans, INR 1,7, plaquettes 210 000/mm³, pas d'amine, fièvre et dilatation. L'INR au-dessus de 1,5 suffit au grade III. Ce n'est pas un point de Child-Pugh à commenter à la place du drainage.",
    "Homme de 59 ans, créatinine 190 µmol/l, diurèse conservée, fièvre, image positive. 190 est au-dessus d'environ 177. Item rénal. Grade III. On ne le compare pas aux 300 µmol/l de King : autre score, autre maladie.",
    "Femme de 63 ans, anurie depuis huit heures, créatinine encore à 110 µmol/l, angiocholite par ailleurs diagnostiquée. L'oligurie coche sans attendre la créatinine. Grade III rénal.",
    "Homme de 57 ans, PaO2/FiO2 à 250 sous oxygène, foie obstructif infecté. Item respiratoire. Grade III. À 320, cet item tomberait. On écrit le rapport, pas le mot détresse.",
    "Femme de 48 ans, confusion nouvelle, pas de focalité, ictère fébrile, dilatation. Conscience altérée : grade III. Le scanner cérébral ne se substitue pas au drainage si le ventre est le foyer évident.",
    "Homme de 80 ans, dopamine en dessous de cinq microgrammes par kilogramme et par minute, pas d'autre organe, un seul item de grade II. Pas de grade III. On ne gonfle pas l'amine. S'il faut une noradrénaline, le grade change à ce moment-là, pas avant.",
    "Femme de 77 ans, fièvre 37,8 °C, leucocytes 11 500, bilirubine 70 µmol/l, albumine normale. Âge seul au-dessus de 75. Fièvre sous 38 °C : le pilier fièvre manque, sauf si une autre réponse inflammatoire est écrite. Sans elle, pas d'angiocholite. 70 µmol/l n'aurait de toute façon pas coché l'item des 85,5.",
    "Homme de 61 ans, fièvre 38,6 °C, leucocytes 15 000, bilirubine 120 µmol/l, âge sous 75, albumine basse, INR 1,0, plaquettes normales. Grade II largement, plusieurs items, pas d'organe. Drainage précoce. Ajouter un organe imaginaire pour « faire plus grave » est une faute.",
    "Femme de 69 ans, trois piliers, aucun item II, aucun organe, antibiotique à la sixième heure, fièvre qui tombe, bilirubine qui baisse. Grade I qui répond. On n'impose pas l'endoscopie du seul fait qu'un calcul a été vu, si la définition autorise d'attendre la réponse. On écrit l'heure de la revue : si la réponse s'arrête, on draine.",
    "Le même tableau à la vingt-quatrième heure, fièvre revenue, bilirubine plus haute. La phrase du grade I est atteinte : drainage. Rester sur l'antibiotique seul contredit Tokyo.",
    "Obstacle tumoral froid, homme de 79 ans, bilirubine 280 µmol/l, pas de fièvre, leucocytes normaux, voie biliaire très dilatée. Pas d'angiocholite. Décompression selon la filière tumorale. On ne coche pas le grade II avec l'âge et la bilirubine si le pilier inflammatoire est absent.",
    "Prothèse datant de quatre mois, fièvre 39,2 °C, leucocytes 13 500, ictère qui revient. Deux items au moins, image de prothèse. Grade II. Changement de prothèse, pas un nouvel acide biliaire.",
    "Cholécystite, femme de 40 ans, Murphy, fièvre 38,4 °C, voies biliaires fines, bilirubine normale. Ce n'est pas l'obstacle extra-hépatique de ce fichier. Autre prise en charge. L'endoscopie ne se justifie pas par la fièvre seule.",
    "Pancréatite et calcul. Lipase haute, fièvre, dilatation, deux items de grade II. On note les deux maladies. Le grade de Tokyo décide de l'angiocholite. Le score de pancréatite ne le remplace pas.",
    f"R à 0,8, {PAL} à 4 fois la limite, {ALAT} à 1,5 fois. Cholestatique, concordant. L'image est le prochain geste, pas une sérologie seule.",
    f"R à 9, {ALAT} à 12 fois, {PAL} normale, fièvre absente. Hépatocellulaire. Pas de drainage. On quitte ce fichier.",
    f"R à 2,6, fièvre 38,8 °C, échographie non conclusive. Mixte. On complète l'image. On ne pose pas le grade sur une image non faite.",
    "Albumine à 28 g/l. En Child-Pugh, 28 g/l est la borne basse de la classe moyenne, 2,8 g/dl. En Tokyo, on compare au facteur 0,73 ou 0,7 de la limite du laboratoire, qui peut ne pas être 35 g/l. On écrit la limite du jour. On ne recopie pas 28 g/l comme si c'était le seuil de Tokyo.",
    "Bilirubine 86 µmol/l. Juste au-dessus de 85,5. L'item est coché. À 80 µmol/l, il ne l'est pas. Le calcul avec 17,1 se montre sur la copie, il ne se fait de tête en arrondissant à 50.",
    "Bilirubine 34 µmol/l exactement autour du pilier. Le diagnostic de cholestase biologique peut s'ouvrir. L'item de grade II, lui, reste loin. Une copie qui met « grade II » à 34 µmol/l a confondu les deux seuils.",
    "Lettre type grade II. Âge, deux items nommés avec leurs chiffres, image, heure de l'antibiotique, demande de drainage précoce, organes absents nommés pour montrer qu'on les a cherchés. Une lettre qui dit seulement « angiocholite » renvoie le correspondant au début.",
    "Lettre type grade III. L'organe responsable est nommé : plaquettes, ou INR, ou amine, ou rein, ou poumon, ou conscience. Le drainage et la réanimation sont demandés ensemble. On ne demande pas un avis « dans la semaine ».",
    "Sortie après grade I répondu. Ordonnance d'antibiotique selon le protocole, date de contrôle de la bilirubine, consigne si la fièvre revient. Pas d'Ursofalk. Pas de schéma d'acétylcystéine.",
    "Ce que la copie perd. Un grade sans compte. Une bilirubine en µmol/l comparée au seuil en mg/dl sans conversion. Charcot utilisé comme test obligatoire. Plaquettes oubliées. Acide ursodésoxycholique à la place de l'endoscopie. Chacune suffit à baisser la note.",
    "Cas des deux bilirubines sur la même copie. On écrit 40 µmol/l = environ 2,3 mg/dl, au-dessus du pilier de 2 mg/dl, en dessous de l'item de 5 mg/dl. Le diagnostic d'angiocholite peut être posé si les deux autres piliers sont là. Le grade II ne l'est pas par cette bilirubine. La copie qui ne donne qu'un des deux seuils est ambiguë.",
    "Cas des plaquettes à 100 000/mm³ pile. Le texte lu dit inférieures à 100 000. À 100 000, l'item n'est pas coché. À 99 000, il l'est. La borne est stricte. On ne l'arrondit pas « dans le doute » vers le grade III ni vers le grade I.",
    "Cas de l'INR à 1,5 pile. Le grade III dit au-dessus de 1,5. 1,5 ne coche pas. 1,6 coche. Même discipline que pour les plaquettes : la copie montre l'inégalité, pas un « environ ».",
    "Cas de la créatinine à 2,0 mg/dl pile, soit le chiffre du seuil, pas au-dessus. L'item dit au-dessus de 2,0 mg/dl. L'égalité ne suffit pas. L'oligurie, si elle est là, coche par l'autre branche. Sans oligurie, on ne force pas.",
    "Cas du leucocyte à 12 000 pile. L'item dit au-dessus de 12 000 ou en dessous de 4 000. 12 000 ne coche pas. 12 100 coche. 4 000 ne coche pas la leucopénie. 3 900 coche. Les bornes se lisent comme elles sont écrites.",
    "Cas de l'âge à 75 ans jour pour jour. L'item dit au moins 75 ans. Le jour anniversaire coche. 74 ans et 11 mois ne coche pas. On demande la date de naissance si la décision en dépend.",
    "Cas de la fièvre à 39,0 °C. L'item de grade II dit au moins 39 °C. 39,0 coche. 38,9 ne coche pas cet item, mais 38,9 reste au-dessus de 38 °C et peut remplir le pilier diagnostique. Deux phrases, deux seuils.",
    "Réanimation et drainage en parallèle au grade III. Remplir, amine s'il le faut, antibiotique, appel de l'endoscopiste dans le même temps. Attendre la stabilisation complète pour téléphoner n'est pas le texte : le foyer est le canal.",
    "Antibiotique du grade I. On suit le protocole du service pour les germes biliaires. Ce fichier ne invente pas une dose d'antibiotique qui n'a pas été extraite. La dose sera celle de l'information suisse du produit choisi ce jour-là.",
    "Contrôle après drainage. La bilirubine doit redescendre, la fièvre tomber, les leucocytes revenir. Si rien ne bouge, on cherche un autre obstacle, une prothèse mal placée, un abcès. On ne se contente pas du compte rendu « sphinctérotomie faite ».",
    "Grossesse et obstacle. Le grade se calcule pareil. L'image tient compte du terme. On ne reporte pas un grade III au prétexte de la grossesse. On ne pose pas non plus un acide ursodésoxycholique « parce que c'est une cholestase » : l'information 60812 n'est pas cette indication.",
    "Enfant. Les seuils de Tokyo lus sont ceux de l'adulte du texte. On ne les réduit pas au jugé. Un enfant fébrile et ictérique va au spécialiste avec les trois piliers écrits, pas avec une triade exigée.",
    "Deux patients, même calcul, deux grades. Le premier a 60 ans, fièvre 38,4 °C, bilirubine 40 µmol/l, aucun item de grade II, aucun organe : grade I. Le second a 78 ans et 100 µmol/l de bilirubine : deux items, grade II. Le compte rendu d'échographie identique ne donne pas le même horaire de drainage. La copie qui traite les deux pareil n'a pas lu le grade.",
    "Sepsis urinaire et enzymes un peu hautes, voie biliaire fine, pas de calcul. Le pilier image manque. On traite l'urine. On ne titre pas une angiocholite pour utiliser une salle d'endoscopie. R se calcule quand même, pour ne pas manquer une hépatite à côté.",
    "Après le drainage, INR qui était à 1,8 et qui revient à 1,2, plaquettes qui remontent. Le grade III du jour de l'admission ne se réécrit pas. Il explique pourquoi on a drainé la nuit. Le lendemain n'efface pas l'indication.",
    "Copie modèle. Piliers : fièvre 38,6 °C, bilirubine 40 µmol/l soit environ 2,3 mg/dl, dilatation avec calcul. Grade : aucun des cinq items de II, aucun des organes de III, donc I. Conduite : antibiotique maintenant, revue datée, drainage si la réponse manque. Ce paragraphe tient en une minute et contient la décision.",
    "Copie modèle du grade III plaquettaire. Piliers présents. Plaquettes 72 000/mm³. Un organe. Conduite : réanimation selon l'hémodynamique et drainage sans attendre un autre item. On cite 100 000/mm³ pour montrer que 72 000 est en dessous. On ne parle pas d'une « coagulopathie vague ».",
]

def main():
    fen.append((11, W("w-long5", "Items qui changent le grade", "\n".join(P(p, 9, 18) for p in LONGS))))
    fen.append((14, W("w-cas5b", "Vingt situations de grade", "\n".join(P(p, 9, 12, 18) for p in CAS))))
    fen.append((14, W("w-aj5", "Cas limites du grade", "\n".join(P(p, 9, 12, 18) for p in AJOUTS))))
    essentiel = (
        P("Trois piliers, obligatoirement l'inflammation. Grades I, II (au moins deux items) et III (un organe, plaquettes comprises).", 18)
        + P("Bilirubine diagnostique environ 34 µmol/l. Item de grade II : 85,5 µmol/l. Pas 50.", 9, 18)
    )
    phrases = {
        1: "Obstacle de la voie biliaire principale, froid ou infecté. L'angiocholite est Tokyo, pas la triade seule.",
        2: "Pas de prévalence suisse lue. La sensibilité récente de Charcot est basse, 26,4 % et 21,2 %.",
        3: "Pression dans le canal, puis infection du liquide stagnant. La taille du calcul ne donne pas le grade.",
        4: "Biologie du grade, R, image, puis le compte des items.",
        5: "Chirurgie, prothèse, amaigrissement, fièvre à la maison. La cause change, le grade se calcule pareil.",
        6: "Chercher le choc et la confusion, pas une triade complète.",
        7: "Froid, angiocholite, ou autre foyer. L'image sépare.",
        8: "Trois piliers. Grade II à deux items. Grade III à un organe.",
        9: "Leucocytes, bilirubine convertie, albumine, rein, INR, plaquettes, échographie.",
        10: "I : antibiotique et réévaluation. II : drainage précoce. III : réanimation et drainage.",
        11: "Pas d'acide ursodésoxycholique à la place de l'endoscopie. Information 60812, autre maladie.",
        12: "Traiter la lithiase symptomatique avant la troisième angiocholite. Surveiller la prothèse.",
        13: "34 contre 85,5 µmol/l. Plaquettes sous 100 000/mm³. Deux facteurs d'albumine cités.",
        14: "Charcot incomplet n'innocente pas. 60 µmol/l n'est pas le grade II.",
    }
    fiches = {n: P(phrases[n], 18) for n in phrases}
    sources = [
        f"Tokyo Guidelines 2018, grades I, II et III, plaquettes inférieures à 100 000/mm³.{S(18)}",
        f"Child-Pugh, bilirubine, pour ne pas confondre 50 µmol/l et 85,5 µmol/l.{S(9)}",
        f"{EASL}, lésion médicamenteuse, 2019, rapport R.{S(2)}",
        f"Information Ursofalk, Swissmedic 60812, qui n'est pas le traitement de l'obstacle.{S(12)}",
    ]
    sous = (
        f"Diagnostic différentiel DX.5 de {A('situation de départ F2.11 de PROFILES','F2.11')} "
        f"« Enzymes hépatiques anormales ». Texte du 31.10.2026."
    )
    par = {}
    for point, html in fen:
        par.setdefault(point, []).append(html)
    path = construire(5, "Obstacle biliaire extra-hépatique", essentiel, sous, fiches, par, sources)
    print(path)

if __name__ == "__main__":
    main()
