#!/usr/bin/env python3
"""Phase A du LOT_159, F2.11 Enzymes hépatiques anormales."""
from moteur import A, B, P, S, W, ecrire, page, table

ALAT = A("alanine aminotransférase", "ALAT")
ASAT = A("aspartate aminotransférase", "ASAT")
PAL = A("phosphatase alcaline", "PAL")
GGT = A("gamma-glutamyltransférase", "GGT")
LSN = A("limite supérieure de la normale", "LSN")
INR = A("international normalized ratio", "INR")
EASL = A("European Association for the Study of the Liver", "EASL")
AIPS = A("information professionnelle", "AIPS")
MELD = A("model for end-stage liver disease", "MELD")
FIB = A("fibrosis-4 index", "FIB")
RUCAM = A("Roussel Uclaf causality assessment method", "RUCAM")
VHB = A("virus de l'hépatite B", "VHB")
VHC = A("virus de l'hépatite C", "VHC")
VHA = A("virus de l'hépatite A", "VHA")
VHE = A("virus de l'hépatite E", "VHE")
MASLD = A("metabolic dysfunction-associated steatotic liver disease", "MASLD")
IHA = A("insuffisance hépatique aiguë", "IHA")
CBP = A("cholangite biliaire primitive", "CBP")
HFE = A("gène HFE de l'hémochromatose", "HFE")
TIPS = A("transjugular intrahepatic portosystemic shunt", "TIPS")

essentiel = (
    P(
        f"Une enzyme hépatique anormale est un résultat, pas un diagnostic. Le médecin classe d'abord le profil avec le rapport R, "
        f"égal à ({ALAT} divisée par sa {LSN}) divisé par ({PAL} divisée par sa {LSN}). "
        f"R au moins égal à 5 est hépatocellulaire, R au plus égal à 2 est cholestatique, et R entre 2 et 5 est mixte. "
        f"Ce rapport se calcule sur le premier bilan disponible."
    , 2)
    + P(
        f"Trois situations ne se discutent pas au cabinet. L'intoxication au paracétamol reçoit l'acétylcystéine selon le schéma de Prescott "
        f"de l'{AIPS} Fluimucil 20 %, numéro 31954, dès que le nomogramme de Rumack-Matthew ou le tableau clinique l'exige. "
        f"L'{IHA}, coagulopathie et encéphalopathie sans cirrhose connue, se juge avec les critères de King's College et ceux de Clichy. "
        f"L'angiocholite sur obstacle se draine, elle ne se regarde pas."
    , 3, 10, 11)
    + P(
        f"Le reste se range par mécanisme. La {MASLD} est la maladie chronique du foie la plus fréquente dans la recommandation de 2024, "
        f"et le {FIB}-4 en trie la fibrose. L'hépatite alcoolique sévère se reconnaît à un score de Maddrey d'au moins 32. "
        f"La cirrhose déjà installée se classe en Child-Pugh A, B et C, puis en {MELD} et en {MELD}-Na. "
        f"Aucune de ces classifications ne se coupe : les classes absentes d'un résumé ne sont pas un résumé."
    , 4, 5, 8, 9)
)

sous = (
    f"Situation de départ {A('situation de départ F2.11 de PROFILES', 'F2.11')} "
    f"« Enzymes hépatiques anormales » de {A('Principal Relevant Objectives and Framework for Integrated Learning and Education in Switzerland', 'PROFILES')} 2023"
    f"{S(1)}. Leçon au format V8, texte du 31.10.2026. "
    f"Dix diagnostics : stéatose métabolique, hépatite alcoolique, hépatite virale, lésion médicamenteuse, obstacle biliaire, "
    f"hépatite auto-immune, cholangite biliaire primitive, hémochromatose, maladie de Wilson, insuffisance hépatique aiguë."
)

# --- points ---
p1 = (
    P(
        f"Le cours appelle enzyme hépatique anormale une {ALAT}, une {ASAT}, une {PAL} ou une {GGT} au-dessus de la {LSN} du laboratoire, "
        f"ou une association de ces valeurs. La bilirubine et l'{INR} ne sont pas des enzymes : ils mesurent la fonction, et ils décident de la gravité."
    , 2)
    + P(
        f"La recommandation {EASL} de 2019 fixe trois définitions de cas pour une lésion attribuée à un médicament : "
        f"{ALAT} au moins cinq fois la {LSN}, ou {PAL} au moins deux fois la {LSN}, ou {ALAT} au moins trois fois la {LSN} avec une bilirubine totale au-dessus de deux fois la {LSN}. "
        f"Le {B('w-r','rapport R')} transforme ensuite ce couple en profil hépatocellulaire, cholestatique ou mixte."
    , 2)
)
p1w = W("w-r", "Rapport R : seuils 2 et 5", "\n".join([
    P(f"R se calcule ainsi : ({ALAT} du patient divisée par la {LSN} de l'{ALAT}) divisé par ({PAL} du patient divisée par la {LSN} de la {PAL}). "
      f"On prend le premier jeu de résultats lié à l'événement, pas le pic ultérieur.", 2),
    P(f"Le profil est hépatocellulaire si l'{ALAT} est seule au moins à cinq fois la {LSN}, ou si R est au moins égal à 5. "
      f"Il est cholestatique si la {PAL} est seule au moins à deux fois la {LSN}, ou si R est au plus égal à 2. "
      f"Il est mixte si R est strictement entre 2 et 5.", 2),
    P(f"Ces trois classes sont indissociables. Un compte rendu qui ne dit que « cytolyse » sans calculer R mélange l'hépatite, l'obstacle et la lésion mixte. "
      f"La {GGT} confirme l'origine hépatique d'une {PAL} élevée quand l'os est en cause, mais elle n'entre pas dans R.", 2),
    table("Les trois classes du rapport R", ["Classe", "Règle lue", "Ce que le médecin cherche"], [
        ["Hépatocellulaire", f"R au moins égal à 5, ou {ALAT} isolée au moins à cinq fois la {LSN}", "Virus, médicament, alcool aigu, ischémie, auto-immunité, Wilson"],
        ["Mixte", "R entre 2 et 5", "Médicament, hépatite avec cholestase, maladie de chevauchement"],
        ["Cholestatique", f"R au plus égal à 2, ou {PAL} isolée au moins à deux fois la {LSN}", "Obstacle, cholangite biliaire primitive, médicament cholestatique"],
    ]),
])) + W("w-noms", "Ce que chaque enzyme n'est pas", "\n".join([
    P(f"L'{ALAT} est surtout hépatocytaire. L'{ASAT} est aussi musculaire, cardiaque et érythrocytaire : une {ASAT} isolée fait doser la créatine kinase avant de conclure à une hépatite."),
    P(f"La {PAL} vient du foie, de l'os, du placenta et de l'intestin. Une {PAL} élevée avec une {GGT} normale oriente hors du foie. Une {GGT} isolée suit souvent l'alcool ou un inducteur enzymatique, sans prouver une hépatite."),
    P(f"La bilirubine conjuguée signe un problème hépatique ou biliaire. La bilirubine non conjuguée isolée, enzymes normales, fait chercher Gilbert ou une hémolyse, et elle ne réalise pas une loi de Hy.", 2),
]))

p2 = P(
    f"La {MASLD} est, dans la recommandation conjointe de 2024, la maladie chronique du foie la plus fréquente, liée au diabète de type 2, à l'obésité et aux autres facteurs cardiométaboliques. "
    f"Aucun texte lu ne classe les dix diagnostics de cette leçon dans une population suisse : l'ordre DX suit la fréquence décrite en Europe, et l'ordre E suit le danger.",
    5,
)
p2w = W("w-epi", "Ce que les registres permettent de dire", "\n".join([
    P(f"La lésion idiosyncrasique rend compte de 13 à 15 % des insuffisances hépatiques aiguës dans les séries des États-Unis et de Suède citées par l'{EASL} en 2019. "
      f"Environ 10 % des patients qui ont un ictère médicamenteux meurent d'insuffisance ou sont transplantés, et environ 90 % survivent.", 2),
    P(f"Le registre espagnol et les cohortes islandaises et américaines cités dans la même recommandation ne montrent pas un excès global de femmes, "
      f"sauf pour quelques médicaments. L'âge au-dessus de 55 ans donne un point dans le {RUCAM}, sans être à lui seul un facteur général.", 2),
    P(f"L'hépatite alcoolique survient en général après des décennies d'usage lourd. La recommandation de 2018 cite un seuil de suspicion à plus de vingt grammes par jour chez la femme et plus de trente grammes par jour chez l'homme, "
      f"tandis que la recommandation de 2024 réserve le nom de maladie alcoolique aux prises supérieures à cinquante grammes par jour chez la femme et à soixante grammes par jour chez l'homme. "
      f"Entre les deux se place la catégorie MetALD. Les deux textes sont gardés, ils ne disent pas la même chose.", 4, 5),
])) + W("w-qui", "Qui fait mesurer les enzymes", "\n".join([
    P(f"La recommandation de 2024 demande de chercher une {MASLD} avec fibrose chez la personne diabétique, chez la personne avec obésité abdominale et au moins un autre facteur cardiométabolique, "
      f"et chez celle dont les enzymes restent élevées.", 5),
    P("Le dépistage opportuniste d'une enzyme isolée, sans symptôme, n'a pas de seuil suisse unique dans les textes lus. Le médecin interprète le chiffre avec le profil, les médicaments et l'alcool, puis il répète avant d'empiler les sérologies."),
]))

p3 = P(
    f"L'hépatocyte lâche l'{ALAT} et l'{ASAT} quand sa membrane cède. Le cholangiocyte et la pression biliaire élèvent la {PAL} et la {GGT}. "
    f"Le {B('w-axe','passage de la lésion au chiffre')} explique pourquoi une même enzyme n'a pas le même sens selon le mécanisme.",
    2,
)
p3w = W("w-axe", "De la lésion au chiffre", "\n".join([
    P(f"Nécrose et apoptose hépatocytaires libèrent les aminotransférases. L'ischémie et le paracétamol donnent des pics très hauts, souvent au-delà de vingt-cinq fois la {LSN}, qui chutent vite si la perfusion revient ou si l'antidote est donné."),
    P(f"La rétention des sels biliaires et la lésion des petits canaux élèvent la {PAL}. L'obstacle extra-hépatique ajoute une dilatation des voies, visible en échographie, que la cholestase intrahépatique n'a pas."),
    P(f"L'alcool, le fer, le cuivre et la graisse n'élèvent pas les enzymes par le même chemin. L'alcool favorise un rapport {ASAT} sur {ALAT} supérieur à 1, souvent entre 1,5 et 2, avec une {ASAT} qui dépasse rarement 300 U/l.", 4),
    P(f"Le paracétamol épuise le glutathion par son métabolite toxique. L'acétylcystéine restaure ce glutathion ou le remplace comme substrat, ce que dit l'{AIPS} du Fluimucil 20 %.", 11),
])) + W("w-gravite", "Fonction, pas seulement enzymes", "\n".join([
    P(f"Une {ALAT} à dix fois la {LSN} avec un {INR} normal et une bilirubine normale peut être une hépatite qui guérit. "
      f"Une {ALAT} à trois fois la {LSN} avec une bilirubine qui monte et un {INR} qui s'allonge est plus grave : c'est le sens de la loi de Hy et de la définition de l'{IHA}.", 2, 3),
    P(f"La loi de Hy, dans la recommandation de 2019, a trois composantes, toutes requises pour le signal d'un essai. "
      f"D'abord un excès d'élévations de l'{ALAT} ou de l'{ASAT} d'au moins trois fois la {LSN} par rapport au groupe témoin. "
      f"Ensuite des personnes qui cumulent cette élévation et une bilirubine totale au-dessus de deux fois la {LSN}, sans cholestase initiale marquée par la {PAL}. "
      f"Enfin l'absence d'autre cause. En pratique, un patient qui réunit les deux dernières composantes est un cas de loi de Hy.", 2),
    P(f"La recommandation attend alors une insuffisance mortelle ou une transplantation chez au moins 10 % de ces patients. "
      f"La bilirubine qui compte est la bilirubine conjuguée. Le décalage peut atteindre quatre semaines après le pic des aminotransférases. "
      f"Une {PAL} secondaire ne suffit pas à écarter la loi si R reste au-dessus de 5.", 2),
]))

p4 = P(
    f"Le médecin écarte d'abord ce qui se traite dans l'heure, puis il nomme le profil, puis il choisit parmi les {B('w-dd','dix diagnostics')}. "
    f"L'ordre E n'est pas l'ordre de fréquence.",
    3,
)
p4w = W("w-dd", "Dix diagnostics, graves d'abord dans l'algorithme", "\n".join([
    P("Le numéro DX suit l'enseignement, du mécanisme le plus souvent rencontré au plus rare. Le rang E dit qui passe en premier quand le patient est devant le médecin."),
    table("Ordre E de l'algorithme", ["Rang", "Diagnostic", "Ce qui tranche"], [
        ["E1", "Insuffisance hépatique aiguë et intoxication au paracétamol", f"{INR} allongé et encéphalopathie, ou nomogramme positif"],
        ["E2", "Obstacle biliaire extra-hépatique infecté", "Fièvre, douleur, ictère, dilatation des voies"],
        ["E3", "Hépatite alcoolique sévère", "Ictère récent et Maddrey au moins égal à 32"],
        ["E4", "Hépatite virale", f"{VHA}, {VHE}, {VHB} selon le contexte"],
        ["E5", "Lésion hépatique médicamenteuse et intoxication au paracétamol", f"Chronologie et score {RUCAM}"],
        ["E6", "Hépatite auto-immune", "Score simplifié au moins égal à 6"],
        ["E7", "Maladie de Wilson révélée par une forme aiguë", "Jeune adulte, hémolyse, phosphatase basse"],
        ["E8", "Hémochromatose héréditaire", f"Saturation de la transferrine et ferritine, puis {HFE}"],
        ["E9", "Cholangite biliaire primitive", "Anticorps antimitochondries et profil cholestatique"],
        ["E10", f"Stéatose hépatique liée à un dysfonctionnement métabolique", f"{FIB}-4 puis élastographie si le score dépasse le seuil bas"],
    ]),
])) + W("w-pas", "Trois questions avant tout bilan large", "\n".join([
    P("Le patient peut-il avoir pris du paracétamol, y compris en association, dans les dernières vingt-quatre heures, et l'heure est-elle connue ?"),
    P(f"A-t-il un trouble de conscience, un {INR} qui s'allonge, ou une hypoglycémie ? Ce trio fait appeler le centre d'hépatologie, pas attendre la sérologie."),
    P("A-t-il de la fièvre et une douleur de l'hypocondre droit avec un ictère ? L'échographie et les hémocultures passent avant le bilan auto-immun."),
]))

p5 = P(
    f"L'anamnèse cherche le médicament nouveau, l'alcool quantifié, les facteurs cardiométaboliques, le voyage, le rapport sexuel, la perfusion, et les signes qui datent l'ictère. "
    f"Les {B('w-drapeaux','drapeaux rouges')} changent le lieu de la prise en charge.",
    2, 4,
)
p5w = W("w-questions", "Questions dont la réponse change la conduite", "\n".join([
    table("Anamnèse ciblée", ["Question", "Réponse qui oriente", "Conduite"], [
        ["Heure et dose de paracétamol", "Prise datée, concentration disponible", "Nomogramme, puis schéma de Prescott si la ligne est franchie"],
        ["Médicament commencé dans les trois derniers mois", "Chronologie compatible", f"Arrêt du suspect et score {RUCAM}"],
        ["Alcool", "Usage quotidien quantifié", "Maddrey si ictère récent"],
        ["Diabète, tour de taille, tension", "Au moins un facteur cardiométabolique", f"{FIB}-4"],
        ["Voyage, eau, porc peu cuit", "Tableau aigu", f"{VHA} et {VHE}"],
        ["Antécédent familial de foie ou de diabète bronzé", "Apparentés atteints", f"Saturation de la transferrine et {HFE}"],
        ["Jeune adulte, trouble neurologique", "Mouvements anormaux, baisse scolaire", "Bilan du cuivre"],
    ]),
])) + W("w-drapeaux", "Drapeaux rouges", "\n".join([
    P(f"Confusion, astérixis, inversion du sommeil ou agitation : encéphalopathie. Avec un {INR} habituellement supérieur à 1,5 et des enzymes aiguës, sans cirrhose connue, c'est la définition de l'{IHA} lue en 2017.", 3),
    P("Vomissements incoercibles, hypoglycémie, acidose, oligurie : le foie ne tient plus la glycémie ni le pH. Le lactate artériel entre dans les critères du paracétamol.", 3),
    P("Fièvre et frissons avec ictère et douleur : angiocholite jusqu'à preuve du contraire. Le choc ne se traite pas par une consultation d'hépatologie élective."),
    P(f"Femme enceinte au troisième trimestre, vomissements, hypoglycémie et enzymes élevées : stéatose aiguë gravidique ou syndrome associé à la prééclampsie. Ce cours ne détaille pas l'obstétrique, mais il ne retient pas ces patientes au cabinet."),
]))

p6 = P(
    f"L'examen cherche l'ictère, les signes d'hépatopathie chronique, la douleur vésiculaire et l'encéphalopathie. "
    f"Chaque geste s'ouvre dans la {B('w-exam','fenêtre d’examen')}. Aucune sensibilité chiffrée n'est donnée pour un signe dont le texte lu n'en fournit pas.",
)
p6w = W("w-exam", "Examen physique, geste par geste", "\n".join([
    P("<b>Conjonctives et frein de la langue.</b> L'ictère y apparaît avant la peau. Il date le début de la cholestase ou de l'hépatite, ce dont les scores de King's College et de Lille ont besoin."),
    P("<b>Mains.</b> Astérixis : le patient tend les poignets, doigts écartés, et l'on compte les battements. Érythème palmaire, ongles blancs et angiomes stellaires parlent pour une maladie chronique, pas pour une hépatite aiguë de trois jours."),
    P("<b>Abdomen.</b> Matité déclive et onde ascitique. Bord hépatique : mou et douloureux dans l'hépatite, dur et nodulaire dans la cirrhose ou la tumeur. Rate : hypertension portale ou hémolyse."),
    P("<b>Signe de Murphy.</b> La palpation sous le rebord costal droit bloque l'inspiration. Il oriente vers une vésicule inflammatoire, donc vers l'obstacle ou l'angiocholite, pas vers une stéatose."),
    P("<b>Peau.</b> Lésions de grattage dans la cholestase prolongée. Mélanodermie et arthropathie dans l'hémochromatose avancée. Aucun de ces signes ne remplace le laboratoire."),
    P("<b>Neurologie.</b> Tremblement, dystonie, baisse de la vigilance chez un jeune adulte : le bilan du cuivre ne se reporte pas. L'examen à la lampe à fente relève du spécialiste ; les seuils de l'anneau cornéen ne sont pas dans l'extrait lu."),
])) + W("w-chronique", "Signes qui disent que le foie est déjà chronique", "\n".join([
    P(f"Circulation collatérale, ascite, splénomégalie et angiomes ne sont pas une {IHA} « pure ». La recommandation de 2017 exclut la cirrhose connue, avec trois exceptions où la maladie chronique peut se révéler d'un coup : hépatite auto-immune, syndrome de Budd-Chiari et maladie de Wilson.", 3),
    P("Ces trois exceptions gardent la même urgence qu'une insuffisance aiguë : coagulopathie, encéphalopathie, appel du centre de transplantation.", 3),
]))

p7 = P(
    f"Le profil syndromique tient en une phrase : hépatocellulaire, mixte ou cholestatique, selon R, puis aigu ou chronique selon la durée et les signes. "
    f"Le {B('w-synd','tableau des syndromes')} évite d'appliquer un score de fibrose à une hépatite de quatre jours.",
    2,
)
p7w = W("w-synd", "Syndromes et scores qui leur appartiennent", "\n".join([
    table("Quel score pour quel syndrome", ["Syndrome", "Outil", "Ce qu'il ne fait pas"], [
        ["Enzymes élevées, malade ambulatoire, stéatose", f"{FIB}-4", "Il ne diagnostique pas la cause"],
        ["Ictère et usage d'alcool", "Maddrey, Glasgow, Lille", "Il ne remplace pas l'arrêt de l'alcool"],
        ["Médicament suspect", f"{RUCAM} et loi de Hy", "Il ne donne pas la dose de l'antidote"],
        ["Paracétamol daté", "Nomogramme de Rumack-Matthew", "Il ne s'applique pas si l'heure est inconnue"],
        ["Coagulopathie et confusion, foie auparavant sain", "King's College et Clichy", "Le Child-Pugh n'est pas l'outil de cette heure"],
        ["Cirrhose connue", "Child-Pugh A, B, C, puis MELD et MELD-Na", "Il ne classe pas une hépatite aiguë sans cirrhose"],
    ]),
    P(f"Le rapport de De Ritis est {ASAT} divisée par {ALAT}. Dans l'hépatite alcoolique, la recommandation de 2018 le trouve en général supérieur à 1, et dans le profil biologique typique supérieur à 1,5 jusqu'à 2. "
      f"Il n'est ni sensible ni spécifique au stade de cirrhose. Le seuil 2 n'est donc pas une porte qui ferme le diagnostic.", 4),
])) + W("w-fib", "FIB-4, seuils lus en 2024", "\n".join([
    P(f"{FIB}-4 égale l'âge en années, multiplié par l'{ASAT} en U/l, divisé par le produit du nombre de plaquettes en milliards par litre et de la racine carrée de l'{ALAT} en U/l.", 5),
    P(f"En dessous de 1,3, le risque de fibrose avancée est bas et le contrôle peut revenir dans un à trois ans. Le score manque environ 10 % des fibroses avancées. "
      f"Au-dessus de 1,3, ou au-dessus de 2,0 après 65 ans, le risque augmente. Entre 1,3 et 2,67, la recommandation propose l'élastographie ou une année de traitement des facteurs métaboliques puis un second {FIB}-4. "
      f"Au-dessus de 2,67, le second test ne se discute plus. En dessous de 35 ans, le score est peu fiable.", 5),
    P("Ces trois zones, basse, intermédiaire et haute, restent ensemble. Retirer la zone intermédiaire transformerait un outil de tri en un oui ou un non qu'il n'est pas.", 5),
]))

p8 = P(
    f"Le diagnostic positif de la situation est le profil, pas le nom de la maladie. La maladie se prouve ensuite : virus, médicament par le {RUCAM}, alcool par le tableau et le Maddrey, "
    f"auto-immunité par le score simplifié, fer par la saturation, cuivre par les cinq piliers, obstacle par l'image.",
    2, 6, 7,
)
p8w = W("w-rucam", "RUCAM, toutes les classes", "\n".join([
    P(f"Le {RUCAM}, aussi appelé échelle du {A('Council for International Organizations of Medical Sciences','CIOMS')}, note sept domaines : délai d'apparition, évolution à l'arrêt, facteurs de risque, médicaments concomitants, exclusion des causes non médicamenteuses, "
      f"connaissance antérieure du médicament, et réintroduction.", 2),
    P("Le total classe l'événement en cinq catégories, toutes conservées : hautement probable au-dessus de 8, probable de 6 à 8, possible de 3 à 5, improbable de 1 à 2, exclu à 0 ou en dessous.", 2),
    P("Un score possible n'est pas une preuve, et un score exclu ne disparaît pas du dossier : il documente pourquoi le médicament a été innocenté.", 2),
])) + W("w-child", "Child-Pugh A, B et C", "\n".join([
    P("Cinq mesures, chacune de 1 à 3 points. On n'additionne pas à la fois le temps de prothrombine et l'INR : l'un ou l'autre.", 9),
    table("Points du Child-Pugh", ["Mesure", "1 point", "2 points", "3 points"], [
        ["Bilirubine", "moins de 34 µmol/l", "34 à 50 µmol/l", "plus de 50 µmol/l"],
        ["Albumine", "plus de 3,5 g/dl", "2,8 à 3,5 g/dl", "moins de 2,8 g/dl"],
        ["INR", "inférieur à 1,7", "1,7 à 2,3", "supérieur à 2,3"],
        ["Ascite", "absente", "légère ou contrôlée", "modérée, sévère ou réfractaire"],
        ["Encéphalopathie", "absente", "grade I ou II", "grade III ou IV"],
    ]),
    P("Classe A : 5 ou 6 points. Classe B : 7, 8 ou 9 points. Classe C : de 10 à 15 points. Les trois classes font la classification. Pour la cholangite biliaire primitive et la cholangite sclérosante, la page lue déplace la bilirubine : 68 µmol/l reste à 1 point, et 170 µmol/l sépare 2 et 3 points.", 9),
    P(f"Le {MELD} lu en 2010 vaut 9,57 fois le logarithme népérien de la créatinine en mg/dl, plus 3,78 fois celui de la bilirubine en mg/dl, plus 11,2 fois celui de l'{INR}, plus 6,43. "
      f"Chaque terme est au moins égal à 1, et la créatinine est plafonnée à 4 mg/dl. "
      f"Le {MELD}-Na égale {MELD} moins le sodium, moins 0,025 fois {MELD} fois (140 moins le sodium), plus 140. Le sodium est borné entre 125 et 140 mmol/l.", 8),
]))

p9 = P(
    f"Le premier tube comprend {ALAT}, {ASAT}, {PAL}, {GGT}, bilirubine totale et conjuguée, albumine, {INR}, numération et créatinine. "
    f"Le paracétamol sérique et le gaz du sang artériel s'ajoutent si l'histoire ou la vigilance l'exigent. L'échographie vient tôt dès que R est cholestatique ou que la fièvre est là.",
    2, 3,
)
p9w = W("w-labo", "Ce que chaque examen ajoute", "\n".join([
    table("Bilan de première ligne", ["Examen", "Question", "Piège"], [
        [f"{ALAT}, {ASAT}, {PAL}, {GGT}", "Calculer R et le rapport de De Ritis", "Comparer à la LSN du laboratoire, pas à une norme de mémoire"],
        ["Bilirubine fractionnée", "Conjuguée ou non", "Gilbert et hémolyse faussent la loi de Hy"],
        [f"{INR}, facteur V", "Fonction de synthèse", "L'acétylcystéine elle-même peut allonger le temps de prothrombine"],
        ["Paracétamol sérique et heure de prise", "Placer le point sur le nomogramme", "Inutile si la prise est trop récente pour que l'absorption soit complète, soit avant 4 heures"],
        ["Saturation de la transferrine, ferritine", "Hémochromatose", "La ferritine monte aussi dans l'inflammation et l'alcool"],
        ["Sérologies virales", f"{VHA}, {VHB}, {VHC}, {VHE} selon le tableau", "Un {VHC} positif ne date pas l'élévation d'aujourd'hui"],
        ["Échographie", "Dilatation, stéatose, ascite, thrombose", "Une voie fine n'exclut pas une cholestase intrahépatique"],
    ]),
    P(f"Pour l'hémochromatose, la recommandation de 2022 pose d'abord la saturation et la ferritine, le matin, sans exiger le jeûne. "
      f"Chez un homozygote p.Cys282Tyr, une saturation supérieure à 45 % et une ferritine supérieure à 200 µg/l chez la femme, "
      f"ou une saturation supérieure à 50 % et une ferritine supérieure à 300 µg/l chez l'homme et la femme ménopausée, suffisent au diagnostic provisoire. "
      f"Les autres génotypes exigent le fer hépatique à l'imagerie ou à la biopsie.", 6),
])) + W("w-nom", "Nomogramme de Rumack-Matthew", "\n".join([
    P("Le graphique place la concentration de paracétamol en ordonnée logarithmique et les heures depuis l'ingestion en abscisse. Il commence à 4 heures, quand l'absorption est tenue pour complète.", 10),
    P("La ligne publiée en 1975 part de 200 µg/ml à 4 heures. La ligne de traitement publiée en 1981, abaissée d'un quart, part de 150 µg/ml à 4 heures. "
      "Une concentration de 140 à 150 µg/ml à 4 heures indique en général le traitement par acétylcystéine. Les deux lignes sont enseignées. Une troisième ligne, non lue, n'est pas ajoutée.", 10),
    P("Si la conscience est altérée ou si l'heure est inconnue, le nomogramme ne décide pas seul. La recommandation de 2017 demande un dosage et une recherche toxicologique chez tout patient en insuffisance aiguë, même si le dosage revient négatif.", 3, 10),
]))

p10 = P(
    f"L'arbre tient en quatre branches : urgence vitale, profil cholestatique fébrile, hépatite alcoolique ictérique, puis bilan ambulatoire. "
    f"Le {B('w-algo','détail')} et les {B('w-kings','critères de King')} sont dans les fenêtres.",
    3,
)
p10w = W("w-algo", "Arbre décisionnel", "\n".join([
    P("<b>Branche 1.</b> Trouble de conscience, INR allongé, hypoglycémie ou prise de paracétamol datée : prélèvements, nomogramme, acétylcystéine si indiqué, appel du centre. On ne calcule pas le FIB-4 à cette heure."),
    P("<b>Branche 2.</b> Fièvre, douleur, ictère, R cholestatique : échographie en urgence, hémocultures, antibiothérapie selon le sepsis, drainage si la voie est dilatée et infectée."),
    P("<b>Branche 3.</b> Ictère récent et alcool : numération, INR, bilirubine, Maddrey. Au moins 32 : discuter le corticoïde après avoir écarté l'infection. Moins de 32 : sevrage, nutrition, surveillance."),
    P("<b>Branche 4.</b> Patient stable, enzymes découvertes : répéter, calculer R, relire les médicaments, quantifier l'alcool, puis FIB-4 si le terrain est métabolique, sérologies si le profil est hépatocellulaire et inexpliqué."),
])) + W("w-kings", "King's College et Clichy, critères complets", "\n".join([
    P(f"Pour le paracétamol, un seul des trois blocs suffit. Bloc A : pH artériel inférieur à 7,3 après remplissage, plus de 24 heures après l'ingestion. "
      f"Bloc B : lactate supérieur à 3 mmol/l. Bloc C, les trois ensemble : encéphalopathie au-dessus du grade 3, créatinine supérieure à 300 µmol/l, {INR} supérieur à 6,5.", 3),
    P(f"Hors paracétamol : {INR} supérieur à 6,5, ou trois des cinq critères suivants. Étiologie indéterminée ou hépatite médicamenteuse. Âge inférieur à 10 ans ou supérieur à 40 ans. "
      f"Délai entre l'ictère et l'encéphalopathie supérieur à 7 jours. Bilirubine supérieure à 300 µmol/l. {INR} supérieur à 3,5.", 3),
    P("Clichy, dits critères de Beaujon-Paul Brousse : confusion ou coma, soit une encéphalopathie de stade 3 ou 4, et un facteur V inférieur à 20 % de la normale si l'âge est inférieur à 30 ans, ou inférieur à 30 % si l'âge est supérieur à 30 ans.", 3),
    P("La recommandation dit de discuter la transplantation quand l'un ou l'autre système est rempli. Elle ne demande pas de choisir un seul des deux et d'oublier l'autre.", 3),
]))

p11 = P(
    f"En Suisse, la dose chiffrée vient de l'{AIPS}. L'acétylcystéine de l'intoxication est celle du Fluimucil 20 %, numéro 31954. "
    f"Le {B('w-nac','schéma de Prescott')} est intégral. Les autres doses de cette leçon sont soit dans une information suisse, soit écrites en toutes lettres quand seule la recommandation européenne les porte.",
    11, 13,
)
p11w = W("w-nac", "Schéma de Prescott, information 31954", "\n".join([
    P("L'information professionnelle indique l'antidote de l'intoxication aiguë au paracétamol et la défaillance hépatique qui la suit. La perfusion se fait sous surveillance, lentement : une perfusion trop rapide favorise la réaction anaphylactoïde.", 11),
    P("Dose totale : 300 mg/kg sur 21 heures. Bolus initial de 150 mg/kg dans du glucose à 5 % ou du chlorure de sodium à 0,9 %, en 60 minutes. "
      "Puis 50 mg/kg sur 4 heures, soit 12,5 mg/kg/h. Puis 100 mg/kg sur 16 heures, soit 6,25 mg/kg/h.", 11),
    P("Si l'encéphalopathie persiste après ces 21 heures, la dernière perfusion, écrite dans l'information comme 150 mg/kg par 24 heures, est poursuivie jusqu'à sa disparition. "
      "En dessous de 40 kg, le volume est surveillé à cause du risque d'hypervolémie.", 11),
    P("L'information précise que l'acétylcystéine peut elle-même allonger le temps de prothrombine, en plus de la toxicité du paracétamol. Un INR qui bouge ne se lit donc pas seul.", 11),
    P(f"Pour l'hépatite alcoolique sévère, la recommandation de 2018 retient la prednisolone à quarante milligrammes par jour, ou la méthylprednisolone à trente-deux milligrammes par jour, en l'absence d'infection active. "
      f"L'{AIPS} Prednisolone Streuli, numéro 29348, écrit une posologie initiale habituellement de 5-60 mg/jour. Le chiffre quarante n'y figure pas : il reste celui de la recommandation, en toutes lettres. "
      f"L'association à cinq jours d'acétylcystéine est proposée par la même recommandation ; le schéma milligrammé de cet essai n'est pas recopié sur Prescott.", 4, 13),
])) + W("w-suite", "Autres traitements dont la dose suisse a été lue", "\n".join([
    P(f"Hépatite B chronique : Ténofovir Sandoz, numéro 66282, 245 mg de ténofovir disoproxil une fois par jour avec un repas. "
      f"Entécavir, Baraclude, numéro 57435, dose usuelle 0,5 mg par jour chez le patient naïf de nucléoside. L'ajustement rénal est celui de l'information, pas une règle improvisée.", 14, 15),
    P(f"Cholangite biliaire primitive : Ursofalk 500 mg, numéro 60812, dose journalière selon le poids, de l'ordre de douze à seize milligrammes par kilogramme, répartie dans la journée puis le soir quand les enzymes s'améliorent. "
      f"Le stade avancé peut se décompenser sous acide ursodésoxycholique : l'information le dit.", 12),
    P(f"Hépatite auto-immune : Imurek, numéro 31887, a l'hépatite chronique active auto-immune parmi ses indications. Pour les affections autres que la transplantation, la posologie initiale est généralement de 1 à 3 mg/kg par jour. "
      f"Le corticoïde d'induction reste dans la fourchette de l'information 29348. La recommandation de 2015 ajoute le thiopurique pour épargner le stéroïde, et elle vise la normalisation de l'immunoglobuline G et de l'{ALAT}.", 7, 13, 16),
    P(f"Hémochromatose : saignées jusqu'à une ferritine inférieure à 50 µg/l en induction, puis inférieure à 100 µg/l en entretien, selon la recommandation de 2022. Ce ne sont pas des doses médicamenteuses.", 6),
]))

p12 = P(
    f"La prévention tient à la dose de paracétamol, à l'alcool, au poids et aux médicaments surveillés. "
    f"Un médicament connu pour léser le foie se surveille selon son information, pas selon une calendrier inventé.",
    2, 5,
)
p12w = W("w-prev", "Ce qui évite le prochain dosage catastrophique", "\n".join([
    P("Relire les boîtes combinées : plusieurs spécialités contiennent du paracétamol. L'heure de la dernière prise se note avant que la famille parte."),
    P(f"Chez la personne avec une {MASLD}, traiter le diabète, le poids et la tension change le risque cardiovasculaire, qui dépasse souvent le risque hépatique. Le {FIB}-4 répété repère ceux qui doivent voir un hépatologue.", 5),
    P("L'abstinence est la mesure de fond de la maladie alcoolique, quel que soit le Maddrey. Les vitamines du groupe B sont recommandées à cause du risque d'encéphalopathie de Gayet-Wernicke.", 4),
    P(f"Un patient sous hépatite auto-immune ou sous azathioprine ne stoppe pas seul : la numération surveille la moelle, et l'{ALAT} surveille la reprise.", 7, 16),
]))

p13 = P(
    "Six phrases suffisent à l'examen. R aux seuils 2 et 5. Loi de Hy en trois composantes. Prescott en trois perfusions et nomogramme en deux lignes. "
    "King's College complet, paracétamol et hors paracétamol, plus Clichy. Child-Pugh A, B et C, MELD et MELD-Na. FIB-4 à 1,3, à 2,0 après 65 ans, et à 2,67."
, 2, 3, 5, 8, 9, 10, 11)
p13w = W("w-cles", "Formules à pouvoir réécrire", "\n".join([
    P(f"R = ({ALAT}/{LSN}) / ({PAL}/{LSN}).", 2),
    P(f"De Ritis = {ASAT}/{ALAT}. Typiquement supérieur à 1, et dans l'hépatite alcoolique souvent supérieur à 1,5 jusqu'à 2, {ASAT} rarement au-dessus de 300 U/l.", 4),
    P(f"{FIB}-4 = âge × {ASAT} / (plaquettes × racine carrée de l'{ALAT}).", 5),
    P(f"{MELD} = 9,57 ln(créatinine) + 3,78 ln(bilirubine) + 11,2 ln({INR}) + 6,43, unités mg/dl pour la créatinine et la bilirubine.", 8),
    P(f"{MELD}-Na = {MELD} − Na − [0,025 × {MELD} × (140 − Na)] + 140, sodium entre 125 et 140 mmol/l.", 8),
    P("Maddrey modifié : seuil 32. Glasgow : 5 à 12, mauvais pronostic à partir de 9 si le Maddrey est déjà au moins à 32. Lille : de 0 à 1, non-réponse à partir de 0,45 ; réponse complète jusqu'à 0,16, partielle de 0,16 à 0,56, nulle à partir de 0,56.", 4),
]))

p14 = P(
    "Les pièges d'examen consistent à appliquer le bon score au mauvais malade, à couper une classification, ou à retarder l'antidote pour un dosage."
)
p14w = W("w-pieges", "Erreurs qui changent la note et le patient", "\n".join([
    P("Calculer R sur le bilan du lendemain au lieu du premier bilan : le profil glisse vers la cholestase quand la PAL monte en second, et la loi de Hy peut être écartée à tort.", 2),
    P("Dire Child-Pugh B sans avoir écrit A et C, ou donner le FIB-4 sans la zone entre 1,3 et 2,67. Une classe manquante n'est plus la classification.", 5, 9),
    P("Traiter une hépatite alcoolique à Maddrey inférieur à 32 par corticoïde, ou continuer le corticoïde chez un non-répondeur de Lille au-delà du seuil nul.", 4),
    P(f"Attribuer une {ASAT} isolée au foie sans créatine kinase. Oublier que l'acétylcystéine allonge le temps de prothrombine.", 11),
    P("Placer un point sur le nomogramme avant 4 heures, ou refuser l'antidote parce que le nomogramme est illisible alors que l'insuffisance est déjà là.", 3, 10),
    P(f"Commencer une lévothyroxine ou un autre médicament hépatotoxique sans avoir vu l'{INR} et la bilirubine. Confondre une ferritine d'inflammation avec une hémochromatose sans saturation de la transferrine.", 6),
])) + W("w-pieges2", "Unités et dénominateurs", "\n".join([
    P(f"Le {MELD} historique est en mg/dl, pas en µmol/l. Convertir sans le dire change le score. Le cours garde l'unité de la formule lue.", 8),
    P("L'albumine du barème lu est en g/dl : 3,5 g/dl valent 35 g/l, 2,8 g/dl valent 28 g/l. Le facteur dix est une conversion, pas un second barème.", 9),
    P("Le nomogramme se lit en µg/ml. 150 µg/ml et 150 mg/l sont la même concentration. 150 mg/kg est une dose d'acétylcystéine, pas un point du graphique.", 10, 11),
]))

sources = [
    f"PROFILES 2023, situation F2.11, validé le 1er novembre 2023.{S(1)}",
    f"{EASL}, lésion hépatique médicamenteuse, Journal of Hepatology, 2019 : rapport R, loi de Hy, {RUCAM}.{S(2)}",
    f"{EASL}, insuffisance hépatique aiguë, Journal of Hepatology, 2017 : King's College et Clichy.{S(3)}",
    f"{EASL}, maladie alcoolique, Journal of Hepatology, 2018 : De Ritis, Maddrey, Glasgow, Lille.{S(4)}",
    f"{EASL}, {A('European Association for the Study of Diabetes','EASD')} et {A('European Association for the Study of Obesity','EASO')}, stéatose métabolique, 2024 : {FIB}-4.{S(5)}",
    f"{EASL}, hémochromatose, 2022.{S(6)}",
    f"{EASL}, hépatite auto-immune, 2015.{S(7)}",
    f"Asrani et Kim, Current Opinion in Gastroenterology, mai 2010 : {MELD} et {MELD}-Na.{S(8)}",
    f"Child et Turcotte, 1964 ; Pugh et al., British Journal of Surgery, 1973.{S(9)}",
    f"Rumack et Matthew, Pediatrics, 1975 ; Rumack et al., Archives of Internal Medicine, 1981.{S(10)}",
    f"{AIPS} Fluimucil 20 %, Swissmedic 31954.{S(11)}",
    f"{AIPS} Ursofalk, Swissmedic 60812.{S(12)}",
    f"{AIPS} Prednisolone Streuli, Swissmedic 29348.{S(13)}",
    f"{AIPS} Ténofovir Sandoz, Swissmedic 66282.{S(14)}",
    f"{AIPS} Baraclude, Swissmedic 57435.{S(15)}",
    f"{AIPS} Imurek, Swissmedic 31887.{S(16)}",
    f"{EASL} 2017, hépatite B, cinq phases et indications de traitement.{S(17)}",
    f"Tokyo Guidelines 2018, angiocholite aiguë, grades I, II et III.{S(18)}",
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

from plus_fenetres import EXTRA
sections = [
    (c, t, f, w + EXTRA.get(i, ""))
    for i, (c, t, f, w) in enumerate(sections)
]

html = page(
    "LOT_159_Phase_A_V0",
    "Enzymes hépatiques anormales",
    sous,
    essentiel,
    sections,
    sources,
)
path = ecrire("LOT_159_Phase_A_V0.html", html)
print(path, path.stat().st_size)
