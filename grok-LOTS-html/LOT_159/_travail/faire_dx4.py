#!/usr/bin/env python3
"""DX.4 Lésion hépatique médicamenteuse et intoxication au paracétamol."""
from base_dx import P, W, construire, A
from moteur import S

ALAT = A("alanine aminotransférase", "ALAT")
ASAT = A("aspartate aminotransférase", "ASAT")
PAL = A("phosphatase alcaline", "PAL")
LSN = A("limite supérieure de la normale", "LSN")
INR = A("international normalized ratio", "INR")
EASL = A("European Association for the Study of the Liver", "EASL")
RUCAM = A("Roussel Uclaf causality assessment method", "RUCAM")
AIPS = A("information professionnelle", "AIPS")

def F(point, ident, titre, textes, *refs):
    return point, W(ident, titre, "\n".join(P(t, *refs) for t in textes))

fen = []
fen.append(F(1, "d4", "Deux mécanismes, un seul nom de liste", [
    f"Ce diagnostic couvre deux maladies que l'on ne traite pas de la même façon. La lésion idiosyncrasique survient chez peu de personnes exposées, sans lien simple avec la dose. L'intoxication est une toxicité de dose, prévisible, après une prise trop forte ou trop répétée.",
    f"La recommandation {EASL} de 2019 range les deux dans le même chapitre parce que le premier geste est le même : arrêter le suspect et classer le profil. Le second geste diverge. L'idiosyncrasie n'a pas d'antidote de dose. L'intoxication a un schéma d'acétylcystéine.",
    "On n'écrit pas « hépatite médicamenteuse » sans dire lequel des deux mécanismes on croit, ni sans le profil du premier bilan.",
], 2))
fen.append(F(3, "ph4", "Physiopathologie lue", [
    "Dans l'intoxication, la voie habituelle de conjugaison est débordée. Un métabolite réactif consomme le glutathion. Quand le stock est bas, ce métabolite se fixe aux protéines de l'hépatocyte et la nécrose commence, d'abord centrolobulaire.",
    "Le délai compte. Avant la quatrième heure, l'absorption n'est pas tenue pour complète et le graphique ne se lit pas. Après, la concentration guide. Une prise dont l'heure est inconnue ne se place pas sur une ligne au jugé.",
    "L'idiosyncrasie n'est pas ce débordement. Elle mêle une susceptibilité de l'hôte et, souvent, une réaction immune. La dose quotidienne peut être la dose habituelle du produit. Chercher une « erreur de posologie » dans ce cas fait manquer l'arrêt.",
    f"Les deux peuvent donner une nécrose, une cholestase, ou un mélange. Le rapport R du premier bilan dit lequel. Il ne dit pas le mécanisme. Une {ALAT} très haute se voit dans l'intoxication et dans certaines idiosyncrasies.",
], 2, 10))
fen.append(F(3, "et4", "Étiologies classées, sans en retirer une classe", [
    f"Profil hépatocellulaire : R au moins égal à 5. Le rapport est ({ALAT} divisée par sa {LSN}) divisé par ({PAL} divisée par sa {LSN}). On le calcule sur le premier jeu lié à l'événement, pas sur le pic le plus spectaculaire s'il est plus tardif.",
    f"Profil cholestatique : R au plus égal à 2. Profil mixte : R strictement au-dessus de 2 et strictement en dessous de 5. Les trois classes restent nommées. Dire « hépatite » pour un R à 1,5 est faux.",
    "Causes à séparer de l'idiosyncrasie : intoxication de dose, ischémie, virus aigu, obstacle, alcool aigu, auto-immunité, Wilson qui se présente comme une insuffisance. Le score de causalité baisse si ces causes n'ont pas été cherchées.",
    "Exposition : médicament à autorisation, plante, complément, produit en ligne, prise ponctuelle d'un antalgique. La recommandation de 2019 met ces expositions dans le même raisonnement.",
], 2))
fen.append(F(8, "r4", "Rapport R, trois exemples chiffrés", [
    f"Laboratoire de l'exemple : {LSN} de l'{ALAT} 40 U/l, {LSN} de la {PAL} 120 U/l. Ces bornes sont celles de l'exemple.",
    f"Exemple hépatocellulaire. {ALAT} 400 U/l, soit 10 fois sa limite. {PAL} 120 U/l, soit 1 fois sa limite. R = 10. C'est au moins 5 : hépatocellulaire.",
    f"Exemple cholestatique. {ALAT} 80 U/l, soit 2 fois. {PAL} 360 U/l, soit 3 fois. R = 2 divisé par 3, environ 0,7. Au plus égal à 2 : cholestatique. On cherche alors un obstacle, pas seulement un comprimé.",
    f"Exemple mixte. {ALAT} 200 U/l, soit 5 fois. {PAL} 240 U/l, soit 2 fois. R = 2,5. Au-dessus de 2 et en dessous de 5 : mixte. On ne le force ni dans l'une ni dans l'autre classe.",
    "R égal à 2 est cholestatique. R égal à 5 est hépatocellulaire. Le mixte est l'intervalle ouvert entre les deux. Arrondir 2,1 à 2 change la classe : on garde la décimale.",
], 2))
fen.append(F(8, "hy4", "Loi de Hy, les trois composantes", [
    f"La recommandation de 2019 écrit trois composantes. La première est collective, pour un essai : plus d'élévations de l'{ALAT} ou de l'{ASAT} d'au moins trois fois la {LSN} que dans le groupe témoin.",
    f"La deuxième est individuelle : {ALAT} ou {ASAT} au-dessus de trois fois la {LSN}, et bilirubine totale au-dessus de deux fois la {LSN}, sans cholestase initiale portée par la {PAL}.",
    "La troisième : pas d'autre cause. Virus A, B, C ou E, maladie de foie déjà connue, autre produit capable du même tableau. Sans cette exclusion, on n'a pas la loi.",
    "Au lit, le cas pratique réunit la deuxième et la troisième. On fractionne la bilirubine. Une hausse non conjuguée, Gilbert ou hémolyse, ne compte pas. La bilirubine peut monter jusqu'à quatre semaines après le pic des aminotransférases.",
    f"Une {PAL} au-dessus de deux fois la {LSN} au moment du pic n'exclut pas la loi si R reste au-dessus de 5. Le registre cité par la recommandation n'a pas vu cette {PAL} protéger de l'insuffisance.",
    "Au moins 10 % de ces atteintes, au sens de la loi, évoluent vers une insuffisance mortelle ou une transplantation. Ce n'est pas le risque d'une enzyme isolée à trois fois la limite.",
], 2))
fen.append(F(8, "ru4", "Score de causalité, sept domaines et cinq classes", [
    "Domaine du délai : le produit a commencé avant les enzymes, dans une fenêtre compatible. Un produit commencé après le pic n'est pas le coupable.",
    "Domaine de l'arrêt : la baisse après le retrait ajoute des points. L'aggravation malgré l'arrêt en retire. On date l'arrêt.",
    "Domaine des facteurs : âge au-dessus de 55 ans, alcool, grossesse. On les note. On ne les transforme pas en cause unique. Les grands registres ne font pas de l'âge un facteur général.",
    "Domaine des autres produits : chaque hépatotoxique concomitant retire des points. La liste de l'officine se reconstruit, y compris les prises ponctuelles.",
    "Domaine des causes non médicamenteuses : virus, obstacle, ischémie, auto-immunité, alcool. Moins on a cherché, plus le score baisse.",
    "Domaine de la connaissance antérieure : un produit déjà connu pour ce type de lésion marque plus. L'absence de publication baisse ce domaine, elle n'innocente pas.",
    "Domaine de la réintroduction : une reprise accidentelle qui reproduit la lésion pèse lourd. On ne la programme pas pour finir le score.",
    "Cinq classes, toutes affichées : hautement probable au-dessus de 8, probable de 6 à 8, possible de 3 à 5, improbable de 1 à 2, exclu à 0 ou en dessous. Un possible justifie l'arrêt et la surveillance, pas une certitude médico-légale.",
], 2))
fen.append(F(9, "no4", "Nomogramme : les deux lignes publiées", [
    "Le graphique commence à la quatrième heure. Avant, on note l'heure et l'on prélève au bon moment. On ne retarde pas l'antidote si l'histoire est déjà celle d'une intoxication grave, conscience altérée ou heure inconnue.",
    "Ligne de 1975, Rumack et Matthew, Pediatrics : elle part de 200 µg/ml à la quatrième heure.",
    "Ligne de traitement de 1981, Rumack et al., Archives of Internal Medicine : elle est abaissée d'un quart, à 150 µg/ml à la quatrième heure. Les deux lignes restent. On traite à partir de la ligne de 1981.",
    "150 µg/ml égalent 150 mg/l. Ils n'égalent pas une dose en milligrammes par kilogramme. Confondre la concentration et le bolus est une erreur d'unité, pas un détail.",
    "Le graphique ne se lit pas seul si la conscience est altérée ou si l'heure est inconnue. Une troisième ligne n'est pas enseignée : elle n'était pas sur la page lue.",
], 10))
fen.append(F(11, "pr4", "Acétylcystéine, schéma lu dans l'information 31954", [
    "Information suisse Fluimucil 20 %, numéro 31954. Dose totale : 300 mg/kg sur 21 heures.",
    "Bolus : 150 mg/kg dans du glucose à 5 % ou du chlorure de sodium à 0,9 %, en 60 minutes.",
    "Puis 50 mg/kg sur 4 heures, soit 12,5 mg/kg par heure.",
    "Puis 100 mg/kg sur 16 heures, soit 6,25 mg/kg par heure.",
    "Si l'encéphalopathie persiste après ces 21 heures, on poursuit la dernière perfusion, écrite comme 150 mg/kg par 24 heures, jusqu'à ce qu'elle disparaisse.",
    "Poids inférieur à 40 kg : l'information met en garde contre la surcharge liquidienne. On ne concentre pas le schéma au jugé.",
    "L'acétylcystéine elle-même peut allonger le temps de prothrombine. Un temps qui s'allonge sous perfusion ne se lit pas comme une aggravation sans regarder l'ensemble, conscience, lactate, créatinine.",
    "Ce schéma n'est pas celui de l'hépatite alcoolique. On ne le copie pas sur un ictère alcoolique. On ne le commence pas non plus pour une loi de Hy dont le produit n'est pas l'antalgique en cause.",
], 11))
fen.append(F(4, "de4", "Démarche, dans l'ordre", [
    "Heure de la prise, dose estimée, produits associés, vomissements, conscience. Si l'heure est connue et dépasse 4 heures, concentration et ligne de 1981. Si l'heure est inconnue ou la conscience altérée, on ne se rassure pas sur un graphique illisible.",
    f"Premier bilan : {ALAT}, {ASAT}, {PAL}, bilirubine totale et conjuguée, {INR}, créatinine, gaz du sang si le tableau est grave. R se calcule tout de suite.",
    "Chronologie du médicament idiosyncrasique : date de début, date d'arrêt, indication, plantes. Puis les sept domaines. On n'annonce pas la classe avant d'avoir cherché le virus et l'obstacle.",
    f"Surveillance de la loi de Hy : {INR} et bilirubine conjuguée deux à trois fois par semaine tant que les chiffres bougent. Hospitaliser si l'{INR} s'allonge, si la vigilance baisse, ou si le patient ne boit plus.",
], 2, 10, 11))
fen.append(F(5, "an4", "Anamnèse qui change la classe", [
    "La question n'est pas « prenez-vous des médicaments ? ». C'est la date, le nom, la raison de l'arrêt, et ce qui a été pris une seule fois. Un antibiotique arrêté depuis dix jours peut encore être le coupable.",
    "Alcool, grossesse, âge au-dessus de 55 ans : points du score, pas un diagnostic. Voyage et eau : virus A et E à écarter avant d'accuser le comprimé.",
    "Douleur, jeûne, prise répétée au-dessus de la journée habituelle : on pense à l'intoxication même sans une prise unique spectaculaire. On n'invente pas un grammage qui n'a pas été pesé.",
], 2))
fen.append(F(6, "ex4", "Examen", [
    f"Ictère, vigilance, asterixis, foie douloureux, signes de choc. L'examen ne distingue pas l'idiosyncrasie de l'intoxication. Il cherche l'insuffisance : encéphalopathie et {INR}.",
    "Un foie de choc, marbrures, hypotension récente, oriente vers l'ischémie. Les enzymes sont alors très hautes, avec lacticodéshydrogénase et créatinine, et elles chutent si la pression revient. Ce n'est pas un score de causalité.",
], 2, 3))
fen.append(F(7, "sy4", "Trois syndromes", [
    f"Hépatite aiguë médicamenteuse : {ALAT} haute, R au moins 5, délai compatible, autre cause écartée. Cholestase médicamenteuse : R au plus 2, prurit possible, sans calcul. Insuffisance : {INR} en général au-dessus de 1,5 et encéphalopathie, et l'on passe aux critères de King et à Clichy.",
    "Le syndrome mixte n'est pas un reste. R entre 2 et 5 a sa classe. Le traiter comme une hépatite pure ou comme un obstacle pur fait manquer l'un des deux bilans.",
], 2, 3))
fen.append(F(9, "la4", "Examens, et ce qu'ils ne remplacent pas", [
    f"Enzymes, bilirubine fractionnée, {INR}, créatinine, sérologies A, B, C, E, échographie si le profil est cholestatique ou mixte. Le score de causalité sans sérologie est incomplet.",
    "La concentration de l'antalgique se prélève à la quatrième heure ou après, pas avant. Elle se compare à la ligne de 1981. Elle ne remplace pas le schéma si l'heure est perdue et le tableau grave.",
    "La biopsie n'est pas le premier geste. Elle se discute si le diagnostic reste ouvert après l'arrêt et le bilan des autres causes.",
], 2, 10))
fen.append(F(10, "ar4", "Arbre", [
    "Prise datée, concentration au-dessus de la ligne de 1981 : schéma 31954, et l'on surveille la conscience. Prise dont l'heure est inconnue et vomissements ou confusion : même schéma, sans attendre un point sur le graphique.",
    f"Pas d'intoxication, R au moins 5, bilirubine au-dessus de deux fois la {LSN}, autre cause écartée : loi de Hy pratique. Arrêt, surveillance rapprochée de l'{INR}. Pas le bolus de l'information 31954.",
    "R au plus 2 : échographie et, s'il y a de la fièvre, critères de Tokyo. Le médicament peut être en cause, l'obstacle aussi. On ne choisit pas avant l'image.",
    "Score hautement probable, au-dessus de 8 : l'arrêt est déjà fait, on ne réintroduit pas. Score possible, de 3 à 5 : l'arrêt et la surveillance restent, la certitude non.",
], 2, 11, 18))
fen.append(F(12, "pv4", "Prévention", [
    "Écrire la dose et la durée sur l'ordonnance de l'antalgique. Demander les autres prises, y compris celles de la pharmacie familiale. Ne pas additionner deux produits qui contiennent la même molécule.",
    "Avant un médicament connu pour une atteinte hépatique, noter les enzymes de départ si le traitement sera long. La recommandation ne transforme pas ce geste en un calendrier unique pour tous les produits.",
], 2))
fen.append(F(13, "cl4", "Points que la copie doit contenir", [
    "Trois classes de R, avec 2 et 5. Trois composantes de la loi de Hy, et le cas pratique qui en garde deux. Cinq classes du score, de plus de 8 jusqu'à 0 ou moins. Deux lignes du nomogramme, 200 µg/ml et 150 µg/ml à la quatrième heure.",
    "Schéma 31954 en trois perfusions, total 300 mg/kg sur 21 heures, et la poursuite à 150 mg/kg par 24 heures si l'encéphalopathie reste. Ce schéma n'est pas celui d'une autre hépatite.",
], 2, 10, 11))
fen.append(F(14, "pi4", "Pièges", [
    "Calculer R sur un bilan tardif. Lire le graphique avant 4 heures. Traiter 150 µg/ml comme 150 mg/kg. Oublier la troisième composante de la loi de Hy. Citer une seule classe du score. Commencer le schéma 31954 pour un antibiotique. Allonger le temps de prothrombine et conclure que le foie s'aggrave, sans savoir que l'antidote lui-même l'allonge.",
    "Arrondir un R de 5,2 à « cholestase » parce que la phosphatase a un peu monté. La classe hépatocellulaire commence à 5 et s'y tient.",
], 2, 10, 11))
fen.append(F(14, "cas4", "Cas corrigé", [
    f"Femme de 46 ans, amoxicilline et acide clavulanique arrêtés il y a douze jours. {ALAT} 320 U/l, limite 40, soit 8 fois. {PAL} 130 U/l, limite 120, soit 1,1 fois. R environ 7,3. Bilirubine totale 2,4 fois la limite, conjuguée. {INR} 1,1. Sérologies A, B, C, E négatives. Échographie sans dilatation. Pas de plante nouvelle.",
    f"Profil hépatocellulaire, puisque R est au-dessus de 5. Loi de Hy pratique : aminotransférase au-dessus de trois fois, bilirubine au-dessus de deux fois, autre cause non trouvée. On arrête tout suspect restant. On surveille l'{INR} et la bilirubine conjuguée deux à trois fois par semaine. On n'ouvre pas le schéma 31954 : le produit n'est pas l'antalgique de cette information.",
    "Le score de causalité se complète avec les sept domaines. Le délai après l'arrêt est encore compatible pour cet antibiotique. On n'annonce pas « hautement probable » tant que les domaines ne sont pas cochés. On n'annonce pas non plus « exclu » parce que la boîte est déjà à la poubelle.",
    "Variante. La même femme a pris une dose unique dont elle ne sait plus l'heure, elle est confuse, l'INR est à 2,1. Ce n'est plus la loi de Hy de l'antibiotique. C'est l'insuffisance et le schéma 31954, sans attendre un point sur le graphique. Les critères de King viennent ensuite.",
    f"Variante de profil. {ALAT} 90 U/l (2,25 fois) et {PAL} 480 U/l (4 fois). R = 0,56. Cholestatique. L'échographie précède le score. Un calcul avec fièvre fait Tokyo, pas un {RUCAM} isolé.",
], 2, 3, 11))

LONGS = [
    "Le premier jeu de résultats est celui qui est lié à l'événement, pas le contrôle de confort fait trois semaines plus tard. Une phosphatase qui monte ensuite peut faire croire à une cholestase alors que R était hépatocellulaire. On archive le premier R.",
    "R se calcule avec les limites du laboratoire du jour. Emprunter la limite d'un autre hôpital change la classe. On recopie les deux limites à côté des deux enzymes.",
    "Une ALAT à 39 U/l pour une limite à 40 n'est pas une hépatite. Elle ne lance ni le score ni la loi de Hy. Elle se recontrôle si le contexte est bruyant, elle ne se traite pas.",
    "L'enzyme à trois fois la limite, seule, sans bilirubine et sans exclusion des autres causes, n'est pas la loi de Hy. Le risque d'au moins 10 % ne s'applique pas à cette enzyme isolée. L'écrire sur la copie est une faute de définition.",
    "La bilirubine non conjuguée ne remplit pas la composante individuelle. On demande le conjugué. Gilbert, découvert le jour de l'ictère, ne se décrète pas sans le fractionnement.",
    "Le décalage de quatre semaines autorise un second dosage de bilirubine après le pic des aminotransférases. Un bilan unique le jour du pic, avec une bilirubine encore normale, ne clôt pas la loi.",
    "R au-dessus de 5 garde le patient dans la logique hépatocellulaire même si la phosphatase dépasse deux fois sa limite. On ne le « reclasse » pas en cholestase pour cette seule phosphatase.",
    "Les cinq classes du score se citent ensemble. Répondre « probable » sans dire que probable est 6 à 8, et sans dire ce que sont les quatre autres classes, est une copie incomplète.",
    "Un score à 4 est possible, pas probable. L'arrêt est déjà indiqué par la clinique. Le chiffre ne sert pas à négocier la reprise du produit.",
    "Un score à 9 est hautement probable. Il n'autorise pas une réintroduction « sous surveillance » pour confirmer. Le domaine de réintroduction décrit un accident déjà vu.",
    "Un score à 0 ou négatif est la classe exclu. Il suppose que les autres causes ont été cherchées. Un zéro avec une sérologie non faite n'est pas un zéro.",
    "L'âge au-dessus de 55 ans est un item du domaine des facteurs, pas une cause. Un patient de 70 ans avec un virus A a une hépatite A, pas une lésion médicamenteuse « parce qu'il a plus de 55 ans ».",
    "La grossesse est un item du même domaine. Elle ne dispense pas de chercher l'intoxication si une prise est racontée, ni l'obstacle si R est cholestatique.",
    "Deux médicaments hépatotoxiques en même temps : on les note séparément. Le domaine des autres produits retire des points. Additionner les soupçons en un seul nom gonfle la certitude.",
    "La plante et le complément comptent. « Je ne prends rien, seulement des gélules » n'est pas une anamnèse négative. La recommandation de 2019 le dit.",
    "La ligne de 1975 à 200 µg/ml n'est pas abandonnée par la ligne de 1981. On enseigne les deux. Traiter dès 200 µg/ml en ignorant la ligne abaissée à 150 µg/ml retarde l'antidote.",
    "La ligne de 1981 n'efface pas la publication de 1975. Une copie qui ne cite qu'une année est incomplète.",
    "Avant la quatrième heure, placer un point est une erreur de méthode. Noter l'heure et prélever ensuite est la méthode. Si la personne est déjà inconsciente, on ne diffère pas l'antidote pour respecter le graphique.",
    "Heure inconnue : le graphique ne se lit pas seul. La conscience et l'INR décident. Attendre « de savoir l'heure » chez un patient confus est une perte de temps.",
    "150 µg/ml est une concentration. Le bolus de 150 mg/kg est une dose d'acétylcystéine, information 31954. Les deux nombres 150 ne se convertissent pas l'un en l'autre.",
    "La perfusion se fait dans du glucose à 5 % ou du chlorure de sodium à 0,9 %. Choisir un autre soluté n'est pas dans le schéma lu.",
    "Les trois temps sont 60 minutes, puis 4 heures, puis 16 heures. Les comprimer « pour aller plus vite » n'est pas l'information. La surcharge, surtout sous 40 kg, est le risque inverse.",
    "12,5 mg/kg par heure est la même perfusion que 50 mg/kg sur 4 heures. 6,25 mg/kg par heure est la même que 100 mg/kg sur 16 heures. Écrire les deux évite l'erreur de pompe.",
    "Après 21 heures, si la conscience n'est pas revenue, on ne s'arrête pas. La dernière perfusion se poursuit, 150 mg/kg par 24 heures, jusqu'à la disparition de l'encéphalopathie. Ce n'est pas un second bolus de 60 minutes.",
    "L'allongement du temps de prothrombine par l'antidote se dit à l'équipe de nuit. Sinon quelqu'un conclut à une aggravation et quelqu'un d'autre arrête la perfusion. Les deux se trompent si ils n'ont pas lu l'information.",
    "King et Clichy ne se calculent pas sur une enzyme isolée. Ils attendent la coagulopathie et l'encéphalopathie, ou le facteur V avec le stade. Une ALAT à 8 000 U/l avec un INR normal n'est pas encore cette porte.",
    "Le pH artériel inférieur à 7,3 ne compte pour King qu'après le remplissage et plus de 24 heures après la prise. Un gaz précoce ne coche pas cette porte. Le lactate au-dessus de 3 mmol/l est une autre porte, qui ne demande pas le même délai.",
    "La porte des trois critères réunis, encéphalopathie au-dessus du grade 3, créatinine au-dessus de 300 µmol/l, INR au-dessus de 6,5, exige les trois. Deux sur trois ne suffisent pas.",
    "Hors antalgique, un INR au-dessus de 6,5 suffit seul. Trois critères parmi cinq suffisent aussi : cause indéterminée ou médicament, âge inférieur à 10 ans ou supérieur à 40, délai ictère-encéphalopathie au-dessus de 7 jours, bilirubine au-dessus de 300 µmol/l, INR au-dessus de 3,5.",
    "Clichy : encéphalopathie de stade 3 ou 4, et facteur V inférieur à 20 % avant 30 ans, ou inférieur à 30 % après 30 ans. Il s'ajoute à King, il ne le remplace pas.",
    "Ischémie : enzymes très hautes, lacticodéshydrogénase, créatinine, chute rapide si l'hémodynamique revient. On traite le choc. On n'ouvre pas un score de causalité comme premier geste.",
    "Obstacle infecté : fièvre et R cholestatique mènent à Tokyo, grades I, II et III, pas à un arrêt de médicament isolé. Le drainage a son heure selon le grade.",
    "Alcool aigu : ASAT rarement au-dessus de 300 U/l dans l'hépatite alcoolique lue. Une ASAT à 3 000 U/l n'est pas ce profil. On cherche l'ischémie et l'intoxication.",
    "Auto-immunité : un tableau aigu peut manquer d'anticorps. Ce n'est pas une raison pour oublier l'arrêt du médicament suspect. Les deux bilans coexistent.",
    "Virus : une sérologie positive ancienne n'explique pas le pic d'aujourd'hui à elle seule. Une IgM ou une virémie manquante laisse le score incomplet.",
    "La copie minimale : mécanisme soupçonné, R avec sa classe, conduite (schéma 31954 ou arrêt et surveillance), ce que l'on ne fait pas. Sans ces quatre éléments, la longueur ne rachète rien.",
    "La copie qui perd les points : « hépatite médicamenteuse, on arrête ». Il manque R, la loi de Hy, et la distinction avec l'antidote. « Enzymes hautes, nomogramme ». Il manque l'heure et la ligne. « RUCAM probable ». Il manque les cinq classes et les sept domaines.",
]

AJOUTS = [
    "On date chaque enzyme sur une ligne du temps. Le premier R est entouré. Les bilans suivants servent à la cinétique, pas à recalculer la classe initiale.",
    "On écrit la bilirubine en µmol/l si le laboratoire suisse la rend ainsi, et l'on convertit seulement quand le seuil lu est en mg/dl. Un mg/dl de bilirubine vaut 17,1 µmol/l. On le montre.",
    "La créatinine de King, 300 µmol/l, n'est pas la créatinine du grade III de Tokyo, environ 177 µmol/l. Un patient peut remplir l'une sans l'autre.",
    "L'INR de l'insuffisance, en général au-dessus de 1,5, n'est pas l'INR de King hors antalgique, au-dessus de 6,5, ni celui de la liste des cinq, au-dessus de 3,5. Quatre usages, quatre seuils.",
    "Le Child-Pugh ne classe pas cette hépatite aiguë sans cirrhose. A, B et C décrivent une maladie chronique. L'aiguë se juge par King et Clichy.",
    "Le FIB-4 ne se calcule pas aux urgences devant un INR qui bouge. Il trie une fibrose chez un patient stable. Mettre les deux outils dans le même paragraphe sans dire lequel décide est le défaut le plus fréquent.",
    "Maddrey ne se calcule pas sur une idiosyncrasie. Il appartient à l'hépatite alcoolique. Un ictère médicamenteux n'a pas de fonction discriminante.",
    "Glasgow, avec l'urée et non la créatinine, ne se transporte pas ici. Lille non plus. Ces scores ont leur maladie.",
    "Le nomogramme ne se transporte pas vers un antibiotique. Il n'existe pas de ligne de traitement pour l'amoxicilline. L'arrêt et la loi de Hy sont les outils.",
    "La réintroduction diagnostique n'est pas un exercice d'examen à proposer. La copie juste dit qu'on ne la programme pas.",
    "Un possible, score de 3 à 5, se surveille. Il ne se rassure pas. L'insuffisance peut encore venir si la bilirubine monte dans les quatre semaines.",
    "Un improbable, 1 ou 2, fait chercher plus fort l'autre cause. Il ne fait pas reprendre le produit le soir même si la clinique est encore bruyante.",
    "L'exclu, 0 ou moins, se justifie. On écrit ce qui a été écarté : virus, image, ischémie, alcool, auto-immunité.",
    "La dose totale de 300 mg/kg n'est pas une perfusion unique. Elle est la somme des trois temps. Écrire « 300 mg/kg en une heure » est une faute de schéma.",
    "Le bolus de 60 minutes n'est pas le débit des 16 heures suivantes. La pompe change trois fois. La feuille de prescription le montre.",
    "Le glucose à 5 % et le chlorure de sodium à 0,9 % sont les deux solvants lus. On n'en ajoute pas un troisième.",
    "Sous 40 kg, le volume du solvant se discute avec la notice, à cause de la surcharge. On ne divise pas la dose d'antidote pour « faire moins de liquide » sans lire l'information.",
    "L'antidote allonge le temps de Quick. On prévient. On suit la conscience et le lactate en parallèle, pas le temps de Quick seul.",
    "Une réaction pendant la perfusion, maîtrisée par un antihistaminique, permet de reprendre, selon l'information, à la vitesse de 50 mg/kg en 4 heures puis, si c'est toléré, la perfusion de 16 heures. On ne jette pas le schéma au premier prurit.",
    "Le cas de l'antibiotique et le cas de l'heure inconnue ne se corrigent pas avec le même paragraphe. La copie qui mélange les deux perd les points des deux.",
    "On dit le numéro 31954 à côté du schéma, et le nom de l'information. Une dose sans numéro, dans ce lot, n'est pas une dose suisse montrée.",
    "On ne cite pas une troisième ligne du graphique. Le trou est dans le fichier d'incertitudes. Le combler par mémoire serait une invention.",
    "On ne classe pas les dix diagnostics du chapitre par une prévalence suisse. Ce chiffre n'a pas été lu. Le rang de l'algorithme est l'urgence, pas la fréquence.",
    "La lettre au spécialiste, si l'INR bouge : heure de la prise ou date du médicament, R, bilirubine conjuguée, INR, conscience, schéma commencé ou non, sérologies. Une lettre sans heure et sans INR n'est pas un appel, c'est une demande de refaire le bilan.",
]

CAS = [
    f"Cas limite de R. {ALAT} 200 U/l, limite 40, soit exactement 5. {PAL} 120 U/l, limite 120, soit 1. R = 5. La classe hépatocellulaire commence à 5, elle inclut 5. On n'écrit pas « mixte » par prudence. Le mixte s'arrête avant 5.",
    f"Autre limite. {ALAT} 80 U/l, limite 40, soit 2. {PAL} 240 U/l, limite 120, soit 2. R = 1, qui est au plus égal à 2 : cholestatique. La classe mixte commence au-dessus de 2. R = 2 n'y entre pas.",
    f"Cas de décalage. Jour du pic : {ALAT} 12 fois la limite, bilirubine totale encore à 1,2 fois la limite, conjuguée normale. Jour 18 : aminotransférases en baisse, bilirubine totale à 3 fois la limite, conjuguée. La loi de Hy pratique peut se remplir jusqu'à quatre semaines après le pic. Le premier bilan rassurant sur la bilirubine n'a pas clos le dossier.",
    "Cas de Gilbert. Bilirubine totale à 2,5 fois la limite, presque toute non conjuguée, enzymes à peine au-dessus de trois fois, hémolyse absente. La composante individuelle veut une bilirubine qui compte, pas un Gilbert. On fractionne avant d'écrire la loi. On n'arrête pas le raisonnement sur le total seul.",
    f"Cas de phosphatase haute et de R encore hépatocellulaire. {ALAT} 600 U/l, limite 40, soit 15. {PAL} 300 U/l, limite 120, soit 2,5. R = 6. La phosphatase dépasse deux fois sa limite, et pourtant R reste au-dessus de 5. On ne sort pas le patient de la loi de Hy pour cette phosphatase. La recommandation de 2019 le dit.",
    "Frontières du score de causalité. 9 est hautement probable, puisque la classe commence au-dessus de 8. 8 est encore probable, la classe probable va de 6 à 8. 5 est possible, la classe possible va de 3 à 5. 2 est improbable. 0 est exclu. Glisser 8 dans « hautement probable » ou 5 dans « probable » change la phrase de la copie.",
    "Nomogramme à la quatrième heure pile. La concentration est à 150 µg/ml. Elle est sur la ligne de traitement de 1981. On commence le schéma 31954. La ligne de 1975, à 200 µg/ml, est au-dessus : le patient n'a pas besoin d'atteindre 200 pour être traité. Les deux lignes sont citées, la décision suit 1981.",
    "Nomogramme à la troisième heure. On ne place pas le point. On note l'heure de la prise, on prélève à la quatrième, et l'on ne rassure pas la famille avec un chiffre précoce. Si la conscience est déjà altérée, ce respect du graphique ne retarde pas l'antidote.",
    "Conscience altérée, heure perdue, concentration non faite. Le graphique ne se lit pas seul. Le schéma 31954 commence. On prévient que l'antidote peut allonger le temps de prothrombine. On suit la vigilance, le lactate et la créatinine, pas un seul temps de coagulation.",
    "Feuille de pompe. Première ligne : 150 mg/kg en 60 minutes. Deuxième ligne : 50 mg/kg en 4 heures, débit 12,5 mg/kg par heure. Troisième ligne : 100 mg/kg en 16 heures, débit 6,25 mg/kg par heure. Total 300 mg/kg, durée 21 heures. Une seule ligne sur la feuille est un schéma faux.",
    "Poids de 35 kg. L'information 31954 avertit la surcharge liquidienne en dessous de 40 kg. La dose d'antidote reste celle du schéma. Le volume du soluté se lit dans la notice, il ne se devine pas en concentrant « à l'œil ». Glucose à 5 % ou chlorure de sodium à 0,9 % restent les deux solvants.",
    "Temps de prothrombine qui passe de 13 à 17 secondes pendant la deuxième perfusion, conscience claire, lactate normal. On n'arrête pas l'antidote pour ce seul allongement : l'information dit qu'il peut l'allonger. On le répète à la relève. On n'écrit pas « insuffisance » sur ce seul chiffre.",
    "Antibiotique et loi de Hy pratique, INR normal, conscience claire. On arrête le produit. On surveille. On n'ouvre pas le schéma 31954. L'antidote de l'information n'est pas un traitement général de toute enzyme médicamenteuse.",
    f"Imitation ischémique. {ALAT} 4 200 U/l, {ASAT} 5 100 U/l, lacticodéshydrogénase haute, créatinine qui a doublé, hypotension documentée il y a six heures. On traite le choc. Les enzymes doivent chuter si la pression tient. Un score de causalité vient après, pas avant la restauration hémodynamique.",
    "Imitation virale. Retour de voyage, fièvre, enzymes hépatocellulaires, antibiotique commencé hier pour la fièvre. La sérologie A et E se fait avant d'accuser l'antibiotique. Un score sans ces sérologies est incomplet, même si le délai du médicament est joli.",
    f"Imitation biliaire. R à 1,4, fièvre à 38,6 °C, bilirubine à 40 µmol/l. L'image cherche la dilatation. Tokyo s'ouvre si l'inflammation, la cholestase et l'image se réunissent. Le médicament du mois ne remplace pas l'échographie.",
    "Porte du pH. Gaz artériel avec un pH artériel inférieur à 7,3 à la sixième heure, avant le remplissage. Cette porte de King ne s'ouvre qu'après le remplissage et plus de 24 heures après la prise. On ne coche pas. On remplit, on poursuit l'antidote, on refera le gaz.",
    "Porte des trois critères. Encéphalopathie au-dessus du grade 3, créatinine à 240 µmol/l, INR à 7. La créatinine n'est pas au-dessus de 300 µmol/l. Deux critères sur trois ne suffisent pas. L'INR au-dessus de 6,5 ne suffit pas non plus dans la forme liée à l'antalgique : cette porte-là est réservée à la forme sans antalgique, ou elle entre dans le trio mais ne le remplace pas.",
    "Forme sans antalgique. INR à 6,8, encéphalopathie, pas de cirrhose connue. L'INR au-dessus de 6,5 suffit seul pour les critères de King de cette forme. On appelle le centre. On ne demande pas les trois critères de l'autre porte.",
    "Clichy. Patient de 42 ans, encéphalopathie de stade 3, facteur V à 25 %. Après 30 ans, la barre est 30 %. 25 % est en dessous. Le critère est rempli. Avant 30 ans, la même valeur de 25 % serait au-dessus de la barre de 20 % et ne suffirait pas. L'âge se calcule.",
    "Lettre. Heure ou date, produit, R avec les deux limites, bilirubine conjuguée, INR, conscience, schéma 31954 commencé ou non et à quelle heure, sérologies demandées. Le correspondant doit pouvoir continuer sans refaire l'anamnèse.",
    "Ce que la copie perd. Un seul profil au lieu de trois. Une seule ligne de nomogramme. Une seule perfusion au lieu de trois. Une classe de score sans les quatre autres. L'antidote posé sur un antibiotique. Le graphique lu à la deuxième heure. Chacune de ces phrases suffit à baisser la note, même si le reste est long.",
    f"Cas mixte chiffré. {ALAT} 160 U/l, limite 40, soit 4. {PAL} 200 U/l, limite 120, soit 1,67. R environ 2,4. Mixte. On ne choisit pas le camp. Sérologie et échographie partent ensemble. Le score de causalité attend les deux.",
    "Cas d'exclusion. Virus A avec IgM, médicament commencé après le début des symptômes. Le domaine du délai est contre le médicament. Le score ne se force pas au-dessus de 8 pour « faire propre ». La maladie est l'hépatite A. Le médicament s'arrête seulement s'il n'est plus utile, pas parce qu'il est le coupable.",
    "Cas de reprise accidentelle. Le patient a repris trois comprimés, les enzymes remontent dans la même fenêtre. Le domaine de réintroduction se coche comme un fait déjà arrivé. On ne propose pas une nouvelle reprise pour « être sûr ». On interdit le produit.",
    "Ordonnance de sortie après une loi de Hy sans insuffisance. Liste des produits arrêtés, date du prochain INR, date de la prochaine bilirubine conjuguée, consigne de revenir si la vigilance baisse ou si les vomissements empêchent de boire. Pas de schéma 31954 sur l'ordonnance de ville.",
    f"Cas à deux bilans. Premier jour : {ALAT} 10 fois la limite, {PAL} à sa limite, R = 10, hépatocellulaire. Dix jours plus tard la phosphatase a triplé et l'alanine a baissé. On ne recalcule pas la classe sur le second bilan pour réécrire l'histoire. Le premier R reste celui de la recommandation de 2019. Le second bilan sert à voir si la bilirubine monte.",
    "Cas du lactate. Lactate artériel à 3,4 mmol/l après le début de la prise en charge, conscience qui baisse, prise datée. La porte du lactate de King est au-dessus de 3 mmol/l. Elle ne demande pas d'attendre 24 heures, contrairement à la porte du pH. Une seule porte suffit dans la forme liée à l'antalgique. On appelle le centre et l'on poursuit le schéma 31954.",
    "Cas incomplet du trio. Encéphalopathie au-dessus du grade 3 et INR à 7,1, créatinine à 110 µmol/l. Il manque la créatinine au-dessus de 300 µmol/l. Le trio n'est pas réuni. S'il n'y a pas non plus la porte du pH ni celle du lactate, King n'est pas rempli. On ne « complète » pas avec l'INR seul : ce raccourci appartient à l'autre forme, sans antalgique.",
    "Cas d'âge aux critères sans antalgique. Patient de 38 ans, cause médicamenteuse, ictère depuis 10 jours avant la confusion, bilirubine à 320 µmol/l, INR à 3,8. Trois critères parmi cinq : cause médicament, délai au-dessus de 7 jours, bilirubine au-dessus de 300 µmol/l. L'âge de 38 ans n'est ni inférieur à 10 ni supérieur à 40, il ne compte pas. L'INR à 3,8 est au-dessus de 3,5, ce serait un quatrième, mais trois suffisent déjà. On appelle. L'INR n'est pas au-dessus de 6,5, donc ce n'est pas la porte qui suffit seule.",
    "Stéatose médicamenteuse, classe à part. La recommandation de stéatose de 2024 cite, parmi les produits qui peuvent graisser le foie, les corticoïdes, le tamoxifène, l'amiodarone, l'irinotécan, le méthotrexate, le lomitapide, le valproate et le fluoro-uracile. Ce n'est pas une loi de Hy aiguë. On ne leur applique pas le schéma 31954. On les retire du différentiel de la stéatose métabolique quand l'exposition est là.",
]

def main():
    fen.append((11, W("w-long4", "Ce que la copie développe", "\n".join(P(p, 2, 3, 10, 11) for p in LONGS))))
    fen.append((14, W("w-cas4b", "Cas limites, un seuil à la fois", "\n".join(P(p, 2, 3, 5, 10, 11) for p in CAS))))
    fen.append((14, W("w-aj4", "Erreurs qui changent la note", "\n".join(P(p, 2, 10, 11) for p in AJOUTS))))
    essentiel = (
        P(f"R en trois classes, loi de Hy en trois composantes, {RUCAM} en cinq classes, nomogramme en deux lignes, schéma 31954 en trois perfusions.", 2, 10, 11)
        + P("L'idiosyncrasie s'arrête et se surveille. L'intoxication reçoit l'acétylcystéine. On ne mélange pas les deux schémas.", 11)
    )
    phrases = {
        1: "Deux mécanismes sous le même nom de liste : idiosyncrasie et toxicité de dose.",
        2: "Aucune prévalence suisse des dix diagnostics n'a été lue. Le risque d'au moins 10 % concerne la loi de Hy, pas toute enzyme.",
        3: "Glutathion débordé d'un côté, réaction d'hôte de l'autre. R ne distingue pas les mécanismes, il distingue les profils.",
        4: "Heure, premier bilan, R, puis soit le graphique soit les sept domaines.",
        5: "Dates, plantes, prise unique, alcool, grossesse. Chaque réponse change un domaine du score.",
        6: "L'examen cherche l'encéphalopathie et le choc, pas le nom du comprimé.",
        7: "Hépatocellulaire, cholestatique, mixte, ou déjà l'insuffisance. Quatre portes.",
        8: "R, loi de Hy, cinq classes. Les trois outils se citent en entier.",
        9: "Enzymes, bilirubine conjuguée, INR, sérologies, concentration après 4 heures, échographie si R est bas.",
        10: "Ligne de 1981 ou arrêt. Graphique illisible et conscience altérée : antidote quand même.",
        11: "300 mg/kg sur 21 heures, information 31954. Pas pour un antibiotique.",
        12: "Ne pas additionner deux boîtes qui contiennent la même molécule.",
        13: "Deux lignes, trois composantes, cinq classes, trois perfusions.",
        14: "150 µg/ml n'est pas 150 mg/kg. Le premier bilan n'est pas le pic tardif.",
    }
    fiches = {n: P(phrases[n], 2) for n in phrases}
    sources = [
        f"{EASL}, lésion hépatique médicamenteuse, Journal of Hepatology, 2019.{S(2)}",
        f"Rumack et Matthew, Pediatrics, 1975 ; Rumack et al., Archives of Internal Medicine, 1981.{S(10)}",
        f"{AIPS} Fluimucil 20 %, Swissmedic 31954.{S(11)}",
        f"{EASL}, insuffisance hépatique aiguë, 2017, si la coagulopathie et l'encéphalopathie sont là.{S(3)}",
    ]
    sous = (
        f"Diagnostic différentiel DX.4 de {A('situation de départ F2.11 de PROFILES','F2.11')} "
        f"« Enzymes hépatiques anormales ». Texte du 31.10.2026."
    )
    par = {}
    for point, html in fen:
        par.setdefault(point, []).append(html)
    path = construire(4, "Lésion hépatique médicamenteuse et intoxication au paracétamol", essentiel, sous, fiches, par, sources)
    print(path)

if __name__ == "__main__":
    main()
