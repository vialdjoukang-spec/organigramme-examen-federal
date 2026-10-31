#!/usr/bin/env python3
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from construire import GLOSSAIRE, SOURCES, exp, meta_base, point
from moteur import ecrire

def L(*rows):
    return list(rows)

P = []

P.append(point(1, [
    "Le référentiel suisse validé le 1er novembre 2023 nomme cette situation, sans y classer dix maladies. {1}",
    "Dix troubles organisent la leçon : Hyponatrémie, Hypernatrémie, Hypokaliémie, Hyperkaliémie, Hypocalcémie, Hypercalcémie, Hypomagnésémie, Hypermagnésémie, Hypophosphatémie et Hyperphosphatémie.",
    "La recommandation européenne de 2014 définit l'hyponatrémie par un sodium inférieur à 135 mmol/l. {2}",
    "Le détail des bornes est dans [[a-p1|la fenêtre des définitions]].",
], L(
    ("La recommandation de 2014 appelle légère une natrémie de 130 à 135 mmol/l mesurée par électrode {2}", "ne pas confondre cette borne avec la gravité des symptômes", "ne pas dire sévère pour le seul chiffre bas", "classer les symptômes à part, dans la fenêtre dédiée"),
    ("Elle appelle modérée une natrémie de 125 à 129 mmol/l {2}", "surveiller de près sans attendre un coma", "ne pas rassurer sur le seul mot modérée", "chercher la cause et l'ancienneté"),
    ("Elle appelle profonde une natrémie inférieure à 125 mmol/l {2}", "la correction vers la normale se surveille de très près", "ne pas utiliser le mot sévère pour cette borne biochimique", "réserver sévère aux symptômes"),
    ("L'hyponatrémie aiguë est documentée depuis moins de 48 heures {2}", "traiter le risque d'œdème cérébral", "ne pas supposer l'ancienneté sans un dosage antérieur", "si l'ancienneté est inconnue, la tenir pour chronique sauf argument contraire"),
    ("L'hyponatrémie chronique existe depuis au moins 48 heures {2}", "limiter la vitesse de remontée du sodium", "ne pas corriger vite un trouble ancien", "viser les plafonds écrits plus bas"),
    ("L'hypernatrémie lue en 2023 est un sodium sanguin supérieur à 145 mmol/l {4}", "chercher l'accès à l'eau et la soif", "ne pas corriger trop vite", "suivre la natrémie de près"),
    ("L'hypokaliémie lue en 2007 est un potassium plasmatique inférieur à 3,5 mmol/l {5}", "séparer le transfert cellulaire et la perte", "ne pas oublier le magnésium si la kaliémie résiste", "doser le potassium urinaire si la cause n'est pas claire"),
    ("L'hyperkaliémie du guide de 2023 reprend le seuil du Conseil européen de réanimation, à partir de 5,5 mmol/l {3}", "grader légère, modérée ou sévère selon les bornes lues", "ne pas garder à domicile une forme sévère", "faire un électrocardiogramme s'il y a un doute clinique"),
    ("La forme légère va de 5,5 à 5,9 mmol/l, la modérée de 6,0 à 6,4, la sévère à partir de 6,5 {3}", "l'hôpital en urgence concerne surtout la forme sévère", "ne pas attendre une onde T pour appeler la forme sévère menaçante", "refaire le dosage si une pseudo-hyperkaliémie est plausible"),
    ("L'hypomagnésémie modérée est inférieure à 0,7 mmol/l et la sévère inférieure à 0,4 mmol/l, pour une zone usuelle de 0,7 à 1,1 {6}", "chercher une hypokaliémie ou une hypocalcémie associées", "ne pas traiter un chiffre sans le contexte", "revoir les médicaments qui font perdre le magnésium"),
    ("L'hypophosphatémie modérée va de 0,32 à 0,80 mmol/l et la sévère est inférieure à 0,32 mmol/l {7}", "substituer surtout la forme sévère ou symptomatique", "ne pas substituer tout transfert sans déplétion", "respecter la vitesse maximale lue de 20 mmol par heure"),
    ("Au-dessus de 3,5 mmol/l de calcium, le guide de 2016 demande une correction urgente {8}", "réhydrater et chercher la cause", "ne pas utiliser le diurétique de l'anse pour faire baisser le calcium", "corriger le calcium sur l'albumine"),
)))

P.append(point(2, [
    "Les fréquences lues décrivent des séries, pas un classement suisse des dix diagnostics.",
    "La prévalence hospitalière de l'hyponatrémie va jusqu'à 30 % dans le texte de 2014. {2}",
    "Les autres proportions sont dans [[a-p2|la fenêtre des fréquences]].",
], L(
    ("L'hypernatrémie concerne 1 à 3 % des patients hospitalisés et jusqu'à 11 % aux soins intensifs {4}", "prévenir le manque d'eau à l'hôpital", "ne pas prendre ces chiffres pour une incidence suisse nationale", "surveiller les patients qui ne boivent pas seuls"),
    ("L'hypokaliémie est présente chez 20 % des patients hospitalisés dans la revue de 2007 {5}", "revoir les diurétiques en premier", "ne pas appeler cela une incidence suisse", "chercher le magnésium si la correction échoue"),
    ("Sous thiazidique, la fourchette lue va de 10 à 40 % {5}", "surveiller le potassium après l'introduction", "ne pas croire le diurétique de l'anse plus hypokaliémiant que le thiazidique", "la revue dit l'inverse pour la sévérité"),
    ("Après 70 ans, sous diurétique de l'anse ou thiazidique, l'incidence lue va de 20 % à 40 % {5}", "contrôler la kaliémie chez la personne âgée traitée", "ne pas extrapoler à tout patient jeune sans diurétique", "relire la cause avant de substituer"),
    ("L'hypophosphatémie modérée touche 2 à 3 % des hospitalisés et la sévère 0,2 à 0,4 % {7}", "aux soins intensifs les chiffres lus montent à 65-80 % et 6 %", "ne pas dépister tout le monde hors risque", "suivre le facteur de risque"),
    ("L'hypomagnésémie touche jusqu'à 65 % des patients de soins intensifs dans la revue de 2016 {6}", "doser le magnésium devant une kaliémie ou une calcémie réfractaire", "ne pas traiter par habitude hors des indications lues", "la revue limite les usages recommandés"),
    ("Environ 20 à 30 % des insuffisances cardiaques chroniques avancées ont une hyponatrémie dans le texte de 2014 {2}", "relier le sodium bas à la sévérité de l'insuffisance cardiaque", "ne pas conclure que le sodium bas est la cause du décès", "le texte laisse ouverte la part de gravité et la part causale"),
    ("Aucune source lue ne donne la part suisse de chaque trouble", "ne pas numéroter les diagnostics selon une fréquence inventée", "ne pas écrire une prévalence manquante comme zéro", "garder le rang E comme ordre de gravité pratique"),
)))

P.append(point(3, [
    "L'hyponatrémie est d'abord un excès d'eau par rapport au sodium et au potassium. {2}",
    "Le potassium, le calcium, le magnésium et le phosphate ont chacun un stock et un transfert.",
    "Les mécanismes lus sont dans [[a-p3|la fenêtre de physiologie]].",
], L(
    ("Le cerveau extrude des osmoles en 24 à 48 heures pour retrouver son volume {2}", "distinguer l'aigu du chronique avant une correction rapide", "ne pas remonter vite un cerveau déjà adapté", "le dépassement expose à la démyélinisation osmotique"),
    ("Une osmolalité mesurée inférieure à 275 mOsm/kg signe une hyponatrémie hypotonique {2}", "cette mesure précède le classement volémique", "ne pas calculer seulement si un osmole non mesuré est possible", "l'osmolalité calculée basse ne tranche pas à elle seule"),
    ("Une osmolalité urinaire d'au plus 100 mOsm/kg fait retenir un excès d'eau relatif {2}", "chercher la polydipsie et les apports hypotoniques", "ne pas conclure à un SIAD si l'urine est aussi diluée", "le SIAD garde en général une urine trop concentrée"),
    ("Le guide de 2014 utilise le mot SIAD, car la conduite rejoint celle du SIADH {2}", "traiter l'antidiurèse inappropriée sans exiger la preuve d'une sécrétion", "ne pas opposer les deux sigles pour changer la conduite", "chercher les causes connues"),
    ("L'hypokaliémie de transfert ne diminue pas le stock total {5}", "ne pas charger en potassium un simple transfert bref", "ne pas oublier l'insuline, le bêta-2-mimétique et l'alcalose", "la revue cite aussi la théophylline et la caféine"),
    ("L'hypomagnésémie augmente la kaliurèse et stimule le SRAA {5}", "corriger le magnésium quand le potassium ne remonte pas", "ne pas augmenter seulement le potassium", "doser le magnésium"),
    ("Le magnésium augmente la libération de PTH et participe à l'hydroxylation de la vitamine D {6}", "une magnésémie basse peut entraîner une calcémie basse", "ne pas conclure à une hypoparathyroïdie sans magnésium", "doser les deux"),
    ("La PTH et le FGF23 diminuent la réabsorption proximale du phosphate et abaissent sa concentration {7}", "une filtration basse laisse le phosphate s'accumuler", "ne pas inventer une borne d'hyperphosphatémie", "le texte de 2019 ne la donne pas"),
    ("L'insuline et l'alcalose respiratoire font entrer le phosphate dans les cellules {7}", "ne pas substituer un pur transfert comme une déplétion", "l'exemple lu est la correction d'une acidocétose", "réévaluer après le traitement de la cause"),
    ("Le calcium sanguin est lié à l'albumine et se corrige sur l'albumine {8}", "interpréter le calcium corrigé", "ne pas traiter un calcium total bas seulement parce que l'albumine est basse", "doser l'albumine"),
)))

P.append(point(4, [
    "On classe d'abord le danger, puis le mécanisme, puis la cause.",
    "Le volume clinique seul est peu fiable pour l'hyponatrémie. {2}",
    "La séquence lue est dans [[a-p4|la fenêtre de démarche]].",
], L(
    ("Devant des symptômes sévères d'hyponatrémie, le risque d'œdème cérébral l'emporte sur celui de démyélinisation {2}", "perfuser le salé hypertonique sans attendre la preuve de l'ancienneté", "ne pas retarder pour un scanner si les signes sont ceux du guide", "contrôler le sodium après 20 minutes"),
    ("Sans symptôme sévère ni moyennement sévère, il y a le temps du diagnostic {2}", "traiter selon la cause", "ne pas lancer d'emblée le salé hypertonique", "mesurer l'osmolalité et les urines"),
    ("Le guide de 2023 organise l'hyperkaliémie hospitalière en cinq temps {3}", "protéger le cœur s'il y a des signes électriques, puis faire entrer le potassium, puis le retirer", "ne pas commencer par une résine si le tracé est menaçant", "surveiller le rebond"),
    ("Une pseudo-hyperkaliémie se discute sur des prélèvements appariés {3}", "éviter de traiter un artefact", "ne pas ignorer un vrai potassium haut pendant la vérification", "en urgence, un gaz du sang peut donner une première valeur"),
    ("Pour le calcium, le guide de 2016 demande l'histoire, l'examen, le tracé et la PTH {8}", "séparer PTH haute et PTH basse", "ne pas opérer une hypercalcémie hypocalciurique familiale prise pour une hyperparathyroïdie", "doser la PTH avant de conclure"),
    ("Pour le potassium bas, la revue de 2007 commence par les médicaments et le volume {5}", "puis l'urine et l'équilibre acido-basique", "ne pas multiplier les dosages rares d'emblée", "un potassium urinaire bas oriente hors du rein"),
    ("Pour le magnésium, une fraction excrétée inférieure à 2 % exclut une perte rénale selon la revue de 2016 {6}", "chercher alors l'absorption", "ne pas affirmer une perte rénale sur ce seul résultat bas", "revoir les IPP et les thiazidiques"),
    ("Hors soins intensifs, le phosphate se cherche s'il y a un facteur de risque {7}", "ne pas le doser sans raison chez tout hospitalisé", "aux soins intensifs le dépistage est plus large", "la revue le dit explicitement"),
)))

P.append(point(5, [
    "Les médicaments, l'accès à l'eau, les pertes digestives et le cancer orientent vite.",
    "Un symptôme sévère d'hyponatrémie ne se discute pas longtemps. {2}",
    "Les drapeaux lus sont dans [[a-p5|la fenêtre d'anamnèse]].",
], L(
    ("Les vomissements, la détresse cardiorespiratoire, la somnolence profonde, les crises et le coma définissent les symptômes sévères {2}", "traiter en urgence si le lien avec l'hyponatrémie est crédible", "ne pas attribuer ces signes à une hyponatrémie légère sans argument fort", "le guide demande cette prudence"),
    ("Nausée sans vomissement, confusion et céphalée sont les symptômes moyennement sévères lus {2}", "ne pas laisser descendre le sodium", "ne pas les appeler anodins", "réévaluer très tôt"),
    ("La soif abolie ou l'eau inaccessible explique la plupart des hypernatrémies lues en 2023 {4}", "demander qui apporte à boire", "ne pas supposer que le patient boit parce qu'une carafe est là", "prévenir dès l'admission"),
    ("Les diurétiques sont la cause la plus fréquente d'hypokaliémie dans la revue de 2007 {5}", "nommer la molécule et la date de début", "ne pas oublier les laxatifs et les vomissements", "les vomissements agissent surtout par le rein"),
    ("Une diarrhée abondante perd du potassium dans les selles {5}", "le stock fécal lu est élevé quand le volume augmente", "ne pas attribuer toute diarrhée à une perte rénale", "le potassium urinaire aide"),
    ("Une faiblesse qui monte, une douleur musculaire ou une urine sombre font craindre une kaliémie très basse {5}", "sous 2,0 mmol/l la revue décrit rhabdomyolyse et arrêt respiratoire possible", "ne pas laisser partir un tel patient", "surveiller le rythme"),
    ("Soif, polyurie, constipation, confusion et douleurs orientent vers l'hypercalcémie {8}", "chercher un cancer et une hyperparathyroïdie, qui font 90 % des causes lues", "ne pas oublier le lithium, le thiazidique et la vitamine D", "demander le poids et les sueurs"),
    ("Une hypocalcémie symptomatique ou un calcium corrigé inférieur à 1,9 mmol/l est une urgence dans le guide de 2016 {9}", "préparer le calcium intraveineux", "ne pas attendre un dosage de confirmation si les signes sont là et le chiffre déjà bas", "surveiller le tracé"),
)))

neuro = [
    "On cherche les signes lus du tableau de 2014, pas un score inventé.",
    "Vomissement, détresse cardiorespiratoire, somnolence profonde, crise et coma sont les symptômes sévères. {2}",
    "Nausée sans vomissement, confusion et céphalée sont moyennement sévères. {2}",
    "Même une hyponatrémie légère peut s'accompagner d'un déficit d'attention. {2}",
    "Le guide dit qu'un patient n'est probablement jamais vraiment asymptomatique. {2}",
    "Si l'hyponatrémie est peu profonde et les signes graves, le lien causal est exceptionnel. {2}",
    "L'hypernatrémie va du tableau pauvre au coma dans le résumé de 2023. {4}",
    "On ne conclut pas le lien neurologique sans le contexte.",
]
vol = [
    "Le volume clinique est en général peu exact pour classer l'hyponatrémie. {2}",
    "On note les œdèmes, la turgescence et la perte de poids sans en faire une preuve.",
    "Un sodium urinaire d'au plus 30 mmol/l suggère un volume artériel efficace bas. {2}",
    "Au-dessus, on écarte d'autres causes avant de retenir un SIAD. {2}",
    "L'hypernatrémie s'accompagne souvent d'un manque d'eau. {4}",
    "L'hypercalcémie demande le bilan hydrique du guide de 2016. {8}",
    "On pèse si un poids antérieur est connu.",
    "On ne décide pas la perfusion sur la seule impression visuelle.",
]
musc = [
    "Sous 2,0 mmol/l de potassium, la revue décrit une atteinte musculaire grave. {5}",
    "La rhabdomyolyse, la tétraparésie, l'iléus et la rétention urinaire sont écrites. {5}",
    "L'hypercalcémie donne une faiblesse musculaire dans le guide de 2016. {8}",
    "L'hypophosphatémie sévère touche le muscle respiratoire et le cœur selon la revue de 2019. {7}",
    "L'hypomagnésémie est aspécifique. {6}",
    "Une crampe isolée ne prouve pas le diagnostic.",
    "On cherche les signes associés, pas un réflexe dont la leçon n'a pas lu la description.",
    "Le signe de Chvostek n'est pas affirmé ici.",
]
elec = [
    "L'hypokaliémie peut montrer une onde U, puis des arythmies graves. {5}",
    "La torsade de pointes et la fibrillation ventriculaire sont citées par la revue de 2007. {5}",
    "L'hyperkaliémie montre souvent une onde T pointue, qui seule menace rarement la vie. {3}",
    "Les signes électriques ne suivent pas toujours un ordre fixe. {3}",
    "L'hypercalcémie raccourcit l'intervalle QT. {8}",
    "L'hypocalcémie se surveille sur le tracé pendant le calcium intraveineux. {9}",
    "On compare le tracé au potassium du laboratoire et, en urgence, au gaz du sang. {3}",
    "Un tracé normal n'exclut pas une kaliémie haute. {3}",
]

P.append(point(6, [
    "L'examen cherche le danger neurologique, le volume, le muscle et le tracé.",
    "Le détail neurologique est dans [[w-neuro|la fenêtre neurologique]].",
    "Le volume est dans [[w-volume|la fenêtre du volume]], le muscle dans [[w-muscle|la fenêtre musculaire]] et le tracé dans [[w-trace|la fenêtre du tracé]].",
], L(
    ("On chronomètre l'examen quand un symptôme sévère est déjà là", "le traitement de l'hyponatrémie symptomatique sévère ne attend pas la fin du bilan", "ne pas enchaîner les examens avant le salé hypertonique", "rester auprès du patient"),
    ("On ausculte le poumon si une perfusion massive est prévue", "4 à 6 litres de salé isotonique en 24 heures exposent à la surcharge {8}", "ne pas oublier le sujet âgé et l'insuffisance rénale", "le guide de 2016 le dit"),
    ("On palpe le cou, les seins, l'abdomen et les aires ganglionnaires si le calcium est haut {8}", "chercher une tumeur", "ne pas limiter l'examen au pli cutané", "la cause maligne est l'une des deux grandes causes"),
    ("On évalue la cognition {8}", "une confusion peut être le calcium, le sodium ou le potassium", "ne pas l'attribuer d'office à l'âge", "refaire l'examen après correction"),
    ("On cherche les œdèmes avant un chélateur de potassium riche en sodium", "Lokelma apporte du sodium et des œdèmes sont décrits {11}", "ne pas l'utiliser comme médicament d'urgence vitale", "le texte suisse le dit"),
    ("On note la diurèse avant une perfusion de potassium {14}", "le produit est contre-indiqué si l'urine est rare", "ne jamais injecter le concentré sans dilution", "surveiller le cœur"),
    ("On regarde la force des membres et la respiration si le phosphate ou le potassium est très bas", "une faiblesse respiratoire change le lieu de soin", "ne pas se fier au seul chiffre", "répéter l'examen clinique"),
    ("On prend la pression et le pouls", "une arythmie impose le tracé immédiat", "ne pas ranger l'électrocardiogramme après tous les bilans", "le guide de 2023 protège le cœur tôt"),
), [
    {"id": "w-neuro", "titre": "Examen neurologique", "phrases": neuro},
    {"id": "w-volume", "titre": "Examen du volume", "phrases": vol},
    {"id": "w-muscle", "titre": "Examen musculaire", "phrases": musc},
    {"id": "w-trace", "titre": "Examen du tracé", "phrases": elec},
]))

P.append(point(7, [
    "Les syndromes se lisent par couples de chiffres et de contexte, pas par une liste plate.",
    "Hyponatrémie avec urine très diluée n'est pas un SIAD. {2}",
    "Le tableau comparatif est dans [[a-p7|la fenêtre syndromique]].",
], L(
    ("Hyponatrémie, urine concentrée et volume non augmenté orientent vers le SIAD après exclusion {2}", "écarter l'insuffisance surrénale et la thyroïde selon le guide", "ne pas commencer le tolvaptan avant cette lecture", "Samsca vise l'hyponatrémie du SIADH chez l'adulte {10}"),
    ("Hyponatrémie et sodium urinaire bas orientent vers un volume efficace diminué {2}", "traiter la cause hémodynamique", "ne pas restreindre l'eau comme dans un SIAD", "répéter le sodium urinaire si le tableau change"),
    ("Hypernatrémie et soif impossible orientent vers un déficit d'eau {4}", "donner de l'eau et traiter la cause", "ne pas corriger plus vite que le cerveau ne le supporte", "le résumé de 2023 redoute hémorragie et démyélinisation"),
    ("Hypokaliémie et hypertension font chercher un excès de minéralocorticoïde {5}", "ne pas se contenter d'un comprimé de potassium", "le chlore urinaire aide à séparer les situations", "la revue décrit le syndrome de Conn et la sténose artérielle"),
    ("Hyperkaliémie et rein qui filtre mal est le couple le plus lu en 2023 {3}", "revoir les médicaments du SRAA", "ne pas arrêter tout traitement sans stratégie", "un chélateur d'entretien peut aider hors urgence vitale"),
    ("Calcium haut et PTH haute orientent vers l'hyperparathyroïdie primaire ou tertiaire {8}", "écarter l'hypercalcémie hypocalciurique familiale", "ne pas envoyer au chirurgien sur la PTH seule", "le guide le signale"),
    ("Calcium haut et PTH basse orientent vers une tumeur ou une cause plus rare {8}", "chercher la tumeur et la vitamine D", "ne pas doser seulement la PTH", "phosphate et fonction rénale font partie du bilan lu"),
    ("Hypokaliémie réfractaire et magnésium bas forment un couple {5}", "corriger le magnésium", "ne pas monter indéfiniment le potassium", "la revue de 2007 explique la kaliurèse"),
)))

P.append(point(8, [
    "Le diagnostic positif est un chiffre défini par la source, plus le mécanisme.",
    "Le mot sévère n'a pas le même sens pour le sodium et pour le potassium.",
    "Les critères sont dans [[a-p8|la fenêtre des critères]].",
], L(
    ("Le diagnostic d'hyponatrémie hypotonique utilise l'osmolalité mesurée {2}", "en dessous de 275 mOsm/kg elle est hypotonique", "ne pas traiter une pseudo-hyponatrémie comme un manque de sodium", "le guide sépare ces situations"),
    ("Le diagnostic de SIAD n'est retenu qu'après exclusion si le sodium urinaire dépasse 30 mmol/l et que le volume n'est pas franchement augmenté {2}", "utiliser les critères du tableau du guide", "ne pas poser le nom sur une insuffisance cardiaque évidente", "l'insuffisance cardiaque avancée a sa propre logique"),
    ("Le diagnostic d'hyperkaliémie sévère est un potassium d'au moins 6,5 mmol/l {3}", "l'hôpital est indiqué", "ne pas la réduire à l'onde T", "l'onde T pointue isolée menace rarement la vie"),
    ("Le diagnostic d'hypercalcémie urgente est un calcium au-dessus de 3,5 mmol/l {8}", "corriger sans attendre", "entre 3,0 et 3,5 le traitement prompt est en général indiqué", "sous 3,0 le guide dit souvent l'absence de symptôme et l'absence d'urgence"),
    ("Le diagnostic d'hypocalcémie sévère est un calcium inférieur à 1,9 mmol/l ou un symptôme sous la zone de référence {9}", "c'est une urgence médicale dans le texte lu", "le seuil varie avec la vitesse de baisse", "ne pas rassurer sur un chiffre seul si les signes sont là"),
    ("Le diagnostic d'hypophosphatémie sévère est un phosphate inférieur à 0,32 mmol/l {7}", "la substitution est logique", "la preuve d'un gain de survie n'est pas démontrée dans la revue", "on substitue quand même les formes profondes"),
    ("Le diagnostic d'hypomagnésémie sévère est un magnésium inférieur à 0,4 mmol/l {6}", "ne pas se limiter à l'oral de 12 à 15 mmol si d'autres troubles sont sévères", "la revue réserve cet oral aux formes non sévères", "surveiller le rein"),
    ("Le produit Zometa définit l'hypercalcémie maligne par un calcium corrigé supérieur à 3,0 mmol/l {15}", "ce n'est pas la même borne que l'urgence à 3,5 mmol/l du guide de 2016", "les deux textes se lisent ensemble", "la dose suisse est celle de l'information professionnelle"),
)))

P.append(point(9, [
    "Le laboratoire confirme le chiffre, l'urine oriente le mécanisme, le tracé juge le danger.",
    "En urgence potassique, le gaz du sang précède le rendu du laboratoire. {3}",
    "Le choix des examens est dans [[a-p9|la fenêtre des examens]].",
], L(
    ("Un prélèvement sur héparinate de lithium est préféré pour un ionogramme rapide {3}", "réduire le délai", "ne pas crier à la pseudo-hyperkaliémie sans prélèvements appariés", "le guide de 2023 décrit cette paire"),
    ("L'osmolalité sanguine et urinaire vient tôt dans l'hyponatrémie {2}", "une urine à 100 mOsm/kg ou moins change la cause", "ne pas attendre le lendemain si le patient est symptomatique", "le traitement sévère ne dépend pas de ce résultat"),
    ("Le sodium urinaire se lit avec le volume et les diurétiques {2}", "la borne suggérée de 30 mmol/l n'est pas une loi isolée {2}", "les diurétiques brouillent le sodium urinaire", "le guide demande d'en tenir compte"),
    ("Le potassium et le chlore urinaires classent l'hypokaliémie {5}", "sous 20 mmol/l de potassium urinaire, la perte est plutôt extrarénale ou un transfert", "au-dessus de 25 mmol/l, deux chemins restent ouverts", "le chlore urinaire les sépare"),
    ("La PTH, le phosphate et la fonction rénale accompagnent le calcium corrigé {8}", "PTH haute et calcium haut ne ferment pas le diagnostic", "l'hypercalcémie hypocalciurique familiale imite l'hyperparathyroïdie", "ne pas l'opérer par erreur"),
    ("La créatinine se mesure avant Zometa {15}", "une clairance basse change la décision", "le texte déconseille le produit si la clairance est inférieure à 30 ml par minute dans certaines indications", "lire l'indication exacte"),
    ("Le magnésium se dose devant une hypokaliémie sévère {5}", "la correction potassique échoue souvent sinon", "ne pas l'oublier devant une hypocalcémie", "la revue de 2016 le recommande"),
    ("Le phosphate varie dans la journée jusqu'à 40 % {7}", "noter l'heure du prélèvement", "ne pas comparer un matin et une nuit sans cette réserve", "le pic lu est entre minuit et 4 heures"),
)))

P.append(point(10, [
    "L'algorithme suit le danger, pas le numéro du diagnostic.",
    "E1 est l'hyperkaliémie sévère ou électrique, E2 l'hyponatrémie à symptômes sévères.",
    "La suite E3 à E10 est dans [[a-p10|la fenêtre de l'algorithme]].",
], L(
    ("E1 protège le cœur si le tracé de l'hyperkaliémie est anormal, puis fait entrer le potassium dans les cellules {3}", "le calcium intraveineux est le premier temps lu", "ne pas débuter par Lokelma ou Veltassa dans l'urgence vitale", "les deux informations professionnelles l'interdisent"),
    ("E2 perfuse 150 ml de salé à 3 % en 20 minutes si les symptômes sont sévères {2}", "contrôler le sodium et répéter si besoin jusqu'à une hausse d'environ 5 mmol/l", "ne pas dépasser 10 mmol/l le premier jour ni 8 mmol/l chaque jour suivant jusqu'à 130 mmol/l", "arrêter la perfusion si les symptômes cèdent après 5 mmol/l"),
    ("E3 réhydrate un calcium au-dessus de 3,5 mmol/l {8}", "le salé à 0,9 % se lit à 4 à 6 litres en 24 heures", "le diurétique de l'anse n'est pas un traitement du calcium", "puis le bisphosphonate selon l'information suisse si l'indication est là"),
    ("E4 traite une kaliémie inférieure à 2,0 mmol/l ou symptomatique {5}", "la voie intraveineuse se surveille", "ne jamais pousser le concentré pur", "l'information 29552 donne des plafonds indicatifs"),
    ("E5 traite l'hypocalcémie sévère ou symptomatique par le calcium intraveineux {9}", "10 à 20 ml de gluconate à 10 % dans 50 à 100 ml de glucose à 5 %, en 10 minutes, sous tracé", "répéter jusqu'à la disparition des symptômes", "puis relais par perfusion diluée"),
    ("E6 corrige l'hypernatrémie en traitant la cause et l'hyperosmolarité {4}", "ne pas aller trop vite", "le résumé redoute l'hémorragie cérébrale et la démyélinisation", "suivre la natrémie"),
    ("E7 substitue l'hypophosphatémie sévère ou symptomatique {7}", "préférer la voie orale si elle suffit", "ne pas dépasser 20 mmol par heure en intraveineux", "surveiller le calcium"),
    ("E8 à E10 viennent après les menaces immédiates", "E8 est l'hypomagnésémie sévère, E9 l'hypermagnésémie iatrogène si le rein filtre mal, E10 l'hyperphosphatémie par baisse de filtration", "cet ordre n'est pas une prévalence", "aucun texte lu ne classe les dix troubles dans la population suisse"),
)))

P.append(point(11, [
    "Les milligrammes et les grammes cités viennent de l'information professionnelle du produit nommé.",
    "Samsca, numéro 66962, débute à 15 mg de tolvaptan une fois par jour chez l'adulte. {10}",
    "Les autres produits sont dans [[a-p11|la fenêtre des traitements]].",
], L(
    ("La dose de Samsca peut monter jusqu'à 60 mg par jour en une prise {10}", "l'instauration et la reprise se font à l'hôpital", "la dose de 7,5 mg s'envisage si la natrémie risque de monter trop vite", "surveiller le sodium et le volume"),
    ("Samsca est indiqué chez l'adulte dans l'hyponatrémie secondaire au SIADH {10}", "la grossesse et l'allaitement figurent aux contre-indications lues", "ne pas le donner dans l'hypovolémie, également contre-indiquée", "ne pas le prendre avec du jus de pamplemousse"),
    ("Lokelma, numéro 67851, n'est pas un médicament de l'hyperkaliémie vitale {11}", "au-dessus de 5,0 mmol/l la dose initiale lue est 10 g trois fois par jour", "l'entretien usuel est 5 g par jour, jusqu'à 10 g, sans dépasser 10 g une fois par jour", "éviter le produit pendant la grossesse par précaution lue"),
    ("Veltassa, numéro 66411, débute à au moins 8,4 g de patiromer une fois par jour {12}", "le maximum lu est 25,2 g par jour", "il ne remplace pas le traitement d'urgence vitale", "écarter les autres médicaments oraux de 3 heures en général"),
    ("Resonium A, numéro 33379, se donne souvent par 15 g trois à quatre fois par jour par la bouche {13}", "par voie rectale, 30 g une à deux fois par jour sont écrits", "ne pas l'associer au sorbitol", "l'interrompre quand la kaliémie revient vers 5 mmol/l ou au-dessous"),
    ("Le chlorure de potassium B. Braun, numéro 29552, ne s'injecte jamais sans dilution {14}", "les valeurs sont indicatives", "sous 2,0 mmol/l la vitesse maximale écrite est 40 mmol par litre et par heure, et l'apport quotidien maximal indicatif est 400 mmol", "au-dessus de 2,5 mmol/l ces plafonds indicatifs passent à 10 mmol par litre et par heure et 200 mmol par jour"),
    ("Zometa, numéro 56257, se dose à 4 mg d'acide zolédronique en au moins 15 minutes pour l'hypercalcémie maligne {15}", "l'indication lue est un calcium corrigé supérieur à 3,0 mmol/l", "le produit est contre-indiqué pendant la grossesse et l'allaitement", "Aclasta, numéro 57363, est un autre produit, à 5 mg, pour l'os et non pour cette indication"),
    ("Minirin injectable, numéro 43585, est indiqué dans le diabète insipide central {17}", "chez l'adulte la dose lue va de 1 à 4 µg une à deux fois par jour", "l'hyponatrémie est une contre-indication", "un excès d'eau sous desmopressine peut donner des crises et un coma"),
)))

P.append(point(12, [
    "Prévenir, c'est surveiller l'eau, les diurétiques et les médicaments qui montent le potassium.",
    "L'hypernatrémie hospitalière se prévient. {4}",
    "Les mesures lues sont dans [[a-p12|la fenêtre de prévention]].",
], L(
    ("Donner accès à l'eau aux patients qui ne boivent pas seuls {4}", "la soif abolie ne protège pas", "ne pas attendre la natrémie du lendemain", "peser et noter les boissons"),
    ("Contrôler le potassium après un diurétique, surtout chez la personne âgée {5}", "les thiazidiques baissent souvent plus fort le potassium que les diurétiques de l'anse", "ne pas renouveler l'ordonnance sans un ionogramme", "chercher le magnésium si la baisse résiste"),
    ("Revoir les inhibiteurs du SRAA quand le potassium dépasse 5,5 mmol/l {3}", "le guide institue alors une action pour baisser le potassium", "ne pas ajouter un chélateur pour masquer une urgence vitale", "Lokelma et Veltassa ne sont pas ce traitement d'urgence"),
    ("Limiter l'eau libre sous desmopressine {17}", "l'information décrit l'hyponatrémie, les crises et le coma", "contrôler le sodium chez la personne de plus de 65 ans", "arrêter devant céphalée ou nausée"),
    ("Ne pas corriger une hyponatrémie chronique au-delà des plafonds de 2014 {2}", "10 mmol/l le premier jour et 8 mmol/l les jours suivants jusqu'à 130 mmol/l", "dépasser expose à la démyélinisation", "arrêter le salé hypertonique dès que le but symptomatique est atteint"),
    ("Chercher le phosphate seulement avec un facteur de risque hors soins intensifs {7}", "éviter les dosages inutiles", "aux soins intensifs la revue est plus large", "substituer la forme sévère"),
    ("Corriger le magnésium bas avant qu'il n'entretienne l'hypokaliémie {6}", "revoir les IPP et les thiazidiques", "ne pas prescrire le magnésium pour une crampe sans autre argument lu", "la revue ne recommande pas cet usage"),
    ("Avant Zometa, hydrater et mesurer le rein {15}", "une perfusion trop courte double le risque de hausse de créatinine selon l'information", "au moins 15 minutes", "le produit est exclu pendant la grossesse"),
)))

P.append(point(13, [
    "Le danger passe avant le mécanisme, et le mécanisme avant le nom de la maladie.",
    "Sévère veut dire le symptôme pour le sodium, et le chiffre pour le potassium dans les textes lus.",
    "Les repères sont dans [[a-p13|la fenêtre des repères]].",
], L(
    ("Sodium inférieur à 135 mmol/l, potassium inférieur à 3,5 ou à partir de 5,5, calcium corrigé, magnésium, phosphate {2}", "ces bornes viennent des textes de 2014, 2007, 2023, 2016 et 2019", "ne pas les mélanger", "chaque fenêtre de diagnostic les reprend"),
    ("150 ml de salé à 3 % en 20 minutes, puis plafond de 10 puis 8 mmol/l {2}", "c'est la conduite des symptômes sévères", "sans ces symptômes, diagnostiquer d'abord", "le volume clinique ne suffit pas"),
    ("Protéger le cœur de l'hyperkaliémie par le calcium si le tracé change {3}", "30 ml de gluconate à 10 % en 10 minutes, ou 10 ml de chlorure à 10 % en 5 minutes", "le chlorure est préféré dans l'arrêt ou la péri-arrêt", "puis déplacer le potassium, sans recopier ici les unités d'insuline"),
    ("Les chélateurs oraux ont une action trop lente pour l'urgence vitale {11}", "Lokelma et Veltassa le disent", "Resonium non plus n'est pas le premier geste si le tracé est menaçant", "on les discute après la protection cardiaque"),
    ("4 mg de Zometa ne sont pas 5 mg d'Aclasta {15}", "l'un traite l'hypercalcémie maligne, l'autre l'os", "les deux sont contre-indiqués pendant la grossesse dans les textes lus", "lire le numéro Swissmedic"),
    ("Le potassium intraveineux est dilué, avec une diurèse et un tracé {14}", "les plafonds 29552 sont indicatifs", "la revue de 2007 écrit aussi 20 mmol par heure", "les deux sources restent attribuées"),
    ("Le magnésium oral de 12 à 15 mmol par jour n'est pas la conduite d'une forme sévère {6}", "la revue le réserve aux formes non sévères", "surveiller l'hypermagnésémie si le rein est faible", "corriger aussi le potassium et le calcium associés"),
    ("Aucune prévalence suisse des dix diagnostics n'a été lue", "le rang E n'est pas une fréquence", "ne pas combler le trou par un chiffre", "le trou est consigné hors du cours"),
)))

P.append(point(14, [
    "Les pièges d'examen confondent un mot, un produit ou une vitesse.",
    "Le mot profonde n'est pas le mot sévère dans le guide de 2014. {2}",
    "Les questions sont dans [[a-p14|la fenêtre des pièges]].",
], L(
    ("Appeler sévère une natrémie inférieure à 125 mmol/l contredit le vocabulaire de 2014 {2}", "dire profonde pour le chiffre et sévère pour le symptôme", "le coma et la crise sont sévères", "la borne 125 ne l'est pas par elle-même"),
    ("Croire le pli cutané pour classer l'hyponatrémie est fragile {2}", "le guide dit le volume clinique peu exact", "passer par l'osmolalité et le sodium urinaire", "les diurétiques troublent la lecture"),
    ("Donner Lokelma ou Veltassa devant un tracé menaçant retarde le geste utile {11}", "les deux textes refusent l'usage d'urgence vitale", "le calcium et le transfert cellulaire viennent avant", "les unités d'insuline ne sont pas recopiées faute d'AIPS lue"),
    ("Mélanger Aclasta et Zometa change la dose et l'indication {16}", "5 mg une fois par an n'est pas le traitement de l'hypercalcémie maligne", "4 mg de Zometa suivent l'information 56257", "les deux sont distincts"),
    ("Pousser le chlorure de potassium pur est interdit par l'information 29552 {14}", "toujours diluer", "contrôler la diurèse et le cœur", "l'anurie et l'insuffisance surrénale non traitée sont des contre-indications"),
    ("Attribuer une crise à l'hyponatrémie alors que la desmopressine et l'eau libre en sont la cause {17}", "Minirin est contre-indiqué si le sodium est déjà bas", "limiter les boissons", "arrêter si la tête tourne ou si le patient vomit"),
    ("Chercher un signe de Chvostek que la leçon n'a pas lu", "l'extrait de 2016 sur l'hypocalcémie ne le décrit pas", "ne pas l'inventer à l'examen", "s'en tenir au calcium, aux symptômes et au tracé"),
    ("Classer les dix troubles par fréquence suisse", "aucune source lue ne le permet", "le rang E est un ordre d'algorithme", "Hyponatrémie et Hyperkaliémie ne sont pas numérotées selon une prévalence"),
)))

FICHES = [
    "On ne mélange pas la borne biochimique et le mot qui décrit le symptôme.",
    "Une série hospitalière ne devient pas un taux national.",
    "Le transfert cellulaire et la perte de stock ne se traitent pas de la même façon.",
    "Le premier geste dépend du danger immédiat, pas du nom final.",
    "La date de début d'un médicament compte autant que son nom.",
    "On répète l'examen après le premier geste, pas seulement avant.",
    "Deux chiffres concordants valent mieux qu'un seul symptôme vague.",
    "Le critère positif reste celui du texte cité, pas une habitude locale.",
    "Un examen qui ne change pas la conduite peut attendre.",
    "On suit l'ordre E1 à E10 sans le prendre pour une fréquence.",
    "Chaque produit garde son numéro Swissmedic à côté de sa dose.",
    "La prévention se joue souvent sur l'ordonnance et l'accès à l'eau.",
    "Retenir peu de bornes, mais les attribuer au bon texte.",
    "Un piège d'examen est une confusion de mots, pas un détail rare.",
]
for i, ph in enumerate(FICHES):
    P[i]["fiche"].insert(0, ph)

EXTRAS = [
L(
    ("Si l'hyponatrémie ne peut pas être datée, le guide de 2014 la tient pour chronique sauf argument contraire {2}", "corriger comme un trouble ancien", "ne pas la déclarer aiguë par défaut", "chercher un dosage antérieur"),
    ("Le guide de 2014 ne couvre pas l'enfant {2}", "ne pas lui appliquer ces bornes d'adulte", "les doses pédiatriques ne sont pas celles de cette leçon", "demander un texte d'enfant"),
    ("Une composition corporelle très éloignée de l'ordinaire peut faire préférer 2 ml par kilogramme de salé à 3 % plutôt que 150 ml fixes {2}", "le guide le suggère seulement", "ne pas en faire la dose de tous", "rester sur 150 ml dans le cas ordinaire"),
    ("Le sodium se contrôle à 6 heures, à 12 heures, puis chaque jour tant que le traitement n'est pas stable {2}", "attraper un dépassement tôt", "ne pas se contenter du dosage de la première heure", "le plafond de 24 heures reste valide"),
),
L(
    ("Les causes aiguës lues comprennent la phase postopératoire, la polydipsie, l'exercice et un thiazidique récent {2}", "demander ces contextes des dernières 48 heures", "ne pas les classer chroniques d'emblée", "la préparation de coloscopie figure aussi"),
    ("L'ocytocine, le cyclophosphamide intraveineux et une desmopressine récente figurent dans le même tableau {2}", "les chercher à l'anamnèse", "ne pas oublier la terlipressine et la vasopressine lues à côté", "dater le début"),
    ("L'insuffisance hépatique s'associe à une hyponatrémie de moins bon pronostic dans le texte de 2014 {2}", "le texte ne tranche pas la part causale", "ne pas attribuer la mort au sodium seul", "chercher la vasodilatation et les diurétiques"),
    ("Le syndrome néphrotique peut stimuler la vasopressine si le volume baisse {2}", "les diurétiques s'y ajoutent souvent", "ne pas le confondre avec un SIAD pur", "regarder la pression, surtout chez l'enfant cité par le guide"),
),
L(
    ("Dans l'insuffisance surrénale secondaire, le cortisol bas ne freine plus la vasopressine {2}", "l'hyponatrémie ressemble alors à un SIAD", "l'aldostérone est moins touchée que dans la forme primaire", "ne pas oublier le cortisol avant de conclure"),
    ("Le rein de l'insuffisance cardiaque garde le sodium mais l'eau est retenue par la vasopressine {2}", "le volume efficace est bas malgré les œdèmes", "ne pas restreindre seulement le sel", "les diurétiques de l'anse font moins d'hyponatrémie que les thiazidiques selon le guide"),
    ("L'échappement à la vasopressine limite la baisse du sodium dans le SIAD {2}", "la descente n'est pas infinie", "ne pas attendre cet échappement pour traiter un symptôme sévère", "le mécanisme est une baisse des canaux à eau"),
    ("Le potassium fécal lu est d'environ 80 à 100 mmol/l, pour une perte quotidienne d'environ 10 mmol {5}", "une diarrhée augmente cette perte", "les vomissements baissent le potassium surtout par le rein", "alcalose de contraction et aldostérone sont le mécanisme lu"),
),
L(
    ("Un potassium urinaire inférieur à 20 mmol/l oriente vers une perte extrarénale, un transfert ou un faible apport {5}", "ne pas lancer un bilan de tubulopathie", "au-dessus de 25 mmol/l le rein participe", "le chlore urinaire sépare alors l'hypovolémie"),
    ("La paralysie périodique hypokaliémique est rare et survient en fin d'effort ou après un repas riche en glucides {5}", "demander les antécédents familiaux", "ne pas la mettre en tête de liste", "les diurétiques restent la cause fréquente"),
    ("L'amphotéricine augmente la perméabilité au potassium et baisse aussi le magnésium {5}", "surveiller les deux", "les fortes doses de pénicilline intraveineuse sont aussi citées", "ce ne sont pas des causes de premier recours"),
    ("Bartter, Gitelman, Liddle et l'acidose tubulaire sont des causes rares lues en 2007 {5}", "y penser si le tableau est ancien et inexpliqué", "ne pas les chercher avant les médicaments", "le volume et la pression orientent"),
),
L(
    ("Une soif intense avec un calcium haut fait partie des signes lus en 2016 {8}", "demander la quantité bue", "la polyurie suit", "ne pas la mettre sur le compte du diabète sans dosage"),
    ("Lithium, immobilisation, lait-alcalin, thyrotoxicose et granulomatose figurent parmi les causes moins fréquentes {8}", "les interroger une à une", "la vitamine D et la vitamine A sont aussi écrites", "théophylline et phéochromocytome ferment la liste lue"),
    ("Une pancréatite, un ulcère, une lithiase ou une kératite en bande accompagnent parfois le calcium haut {8}", "les chercher si le chiffre est élevé", "ils ne remplacent pas la PTH", "le raccourcissement de QT reste électrique"),
    ("La dialyse se discute si l'insuffisance rénale est sévère et le calcium très haut {8}", "le guide de 2016 le mentionne", "ce n'est pas le premier geste", "la réhydratation vient avant"),
),
L(
    ("On palpe les mollets et on demande une douleur si le potassium est très bas {5}", "la rhabdomyolyse est écrite sous 2,0 mmol/l", "ne pas attendre l'enzyme pour protéger le rein", "hydrater selon la cause"),
    ("On écoute le cœur avant de quitter la pièce {3}", "une bradycardie ou un élargissement change l'urgence", "le tracé peut être en retard sur le chiffre", "on le répète après le calcium"),
    ("On cherche les œdèmes des membres si un chélateur sodé est envisagé {11}", "Lokelma décrit des œdèmes", "chez l'insuffisant cardiaque le texte signale une dégradation dans une analyse groupée", "peser le patient"),
    ("On évalue la déglutition et la vigilance avant un traitement oral {13}", "Resonium par la bouche suppose une déglutition sûre", "la voie rectale agit plus vite mais moins fort selon l'information", "ne pas utiliser de sorbitol"),
),
L(
    ("Calcium haut avec soif et constipation forme un syndrome du guide de 2016 {8}", "corriger l'albumine", "90 % des causes lues sont l'hyperparathyroïdie primaire ou une tumeur", "le reste est une liste courte à parcourir"),
    ("Potassium bas avec vomissements est souvent une perte rénale secondaire {5}", "chercher l'alcalose", "ne pas compter seulement le potassium du liquide gastrique", "la revue insiste sur l'aldostérone"),
    ("Magnésium bas avec potassium bas forme le couple de 2007 et de 2016 {6}", "traiter les deux", "une fraction excrétée de magnésium sous 2 % écarte la perte rénale", "regarder l'intestin"),
    ("Phosphate bas après correction d'une acidocétose peut n'être qu'un transfert {7}", "ne pas substituer d'office", "s'il y a une perte digestive ou rénale, substituer", "la forme sévère se substitue"),
),
L(
    ("Le diagnostic de forme légère de l'hyperkaliémie va de 5,5 à 5,9 mmol/l {3}", "beaucoup de ces cas communautaires ne vont pas à l'hôpital si le patient va bien", "la forme sévère, elle, y va", "le guide de 2023 sépare les deux"),
    ("Entre 3,0 et 3,5 mmol/l de calcium, le traitement prompt est en général indiqué {8}", "une hausse lente peut être tolérée", "au-dessus de 3,5 l'urgence est écrite", "sous 3,0 l'urgence est rare"),
    ("L'hypocalcémie dépend aussi de la vitesse de baisse, pas seulement du chiffre 1,9 {9}", "un symptôme sous la zone de référence suffit à l'urgence lue", "ne pas attendre 1,9 si le patient crampe ou convulse", "le guide le dit"),
    ("L'hyperphosphatémie n'a pas de borne chiffrée dans le texte de 2019 {7}", "on décrit la rétention quand la filtration baisse", "ne pas inventer un seuil", "la PTH et le FGF23 abaissent le phosphate quand le rein répond"),
),
L(
    ("Le potassium se recontrôle au moins à 1 heure, 2 heures, 4 heures, 6 heures et 24 heures après une hyperkaliémie modérée ou sévère {3}", "guetter le rebond", "ne pas croire le premier chiffre bas définitif", "le guide de 2023 le suggère"),
    ("La glycémie se surveille après l'insuline donnée pour faire entrer le potassium {3}", "les heures précises sont celles du guide", "les unités d'insuline ne sont pas recopiées", "elles ne figuraient pas dans l'AIPS lue"),
    ("La créatinine de Zometa se relit avant chaque dose dans les indications répétées {15}", "une hausse fait suspendre", "l'hypercalcémie maligne est en général une dose unique", "la perfusion dure au moins 15 minutes"),
    ("L'osmolalité urinaire de concentration sous Minirin se compare à la valeur avant le test {17}", "chez l'adulte le texte cite 800 à 1000 mOsm/kg comme repère d'âge", "une faible hausse signe un défaut de concentration", "ce test n'est pas le traitement de l'hyponatrémie"),
),
L(
    ("E1 reste prioritaire même si le numéro de leçon de l'hyperkaliémie n'est pas le premier", "le tracé et le chiffre 6,5 mmol/l décident {3}", "ne pas finir l'interrogatoire avant le calcium si le tracé est pathologique", "les chélateurs viennent après"),
    ("E2 s'arrête à 130 mmol/l de sodium même si les symptômes n'ont pas toutes disparu {2}", "au-delà, le symptôme a une autre cause probable", "ne pas poursuivre le salé à 3 % pour forcer le réveil", "chercher une autre lésion"),
    ("E5 utilise le chlorure de calcium seulement par voie centrale selon le guide de 2016 {9}", "il irrite les veines", "le gluconate est le sel du premier schéma lu", "surveiller le tracé pendant l'injection"),
    ("E9 surveille l'hypermagnésémie iatrogène surtout si le rein chronique filtre mal {6}", "la revue de 2016 le demande", "elle ne détaille pas un score de gravité", "on s'arrête sur les apports et la filtration"),
),
L(
    ("La séparation des médicaments oraux et de Resonium est d'au moins 3 heures, et de 6 heures si l'estomac se vide mal {13}", "écrire l'heure sur la feuille", "ne pas donner le comprimé dans la même gorgée", "le nouveau-né ne reçoit pas la résine par la bouche"),
    ("Lokelma en dialyse se prend les jours sans dialyse, en commençant à 5 g {11}", "la hausse se fait par paliers de 5 g jusqu'à 15 g", "la cible prédialyse lue va de 4,0 à 5,0 mmol/l", "ce n'est pas le schéma de l'urgence vitale"),
    ("Veltassa se titre par paliers de 8,4 g, au plus une fois par semaine {12}", "on baisse ou on arrête si le potassium passe sous la cible", "le maximum reste 25,2 g par jour", "l'oubli se rattrape le jour même, sans doubler le lendemain"),
    ("Le gluconate de calcium du guide de 2016 se répète jusqu'à la fin des symptômes {9}", "puis 100 ml de solution à 10 % dans un litre, à raison de 50 à 100 ml par heure", "le chlorure reste une alternative centrale", "on traite la cause pendant la perfusion"),
),
L(
    ("Tenir une carafe hors de portée ne compte pas comme un accès à l'eau {4}", "la prévention de l'hypernatrémie est hospitalière", "demander à l'équipe qui fait boire", "peser"),
    ("Un inhibiteur de l'enzyme de conversion peut monter le potassium selon l'information 29552 {14}", "l'énalapril et le captopril sont cités", "les épargneurs de potassium aussi", "surveiller la kaliémie"),
    ("Sous Minirin, le sodium se contrôle avant et trois jours après le début chez la personne de plus de 65 ans {17}", "ou après chaque hausse de dose", "céphalée ou nausée font arrêter", "l'eau libre est le cofacteur"),
    ("Après Zometa, calcium, phosphate, magnésium et créatinine se surveillent {15}", "une hypocalcémie peut suivre", "la grossesse est une contre-indication", "Aclasta n'est pas le substitut de cette indication"),
),
L(
    ("La revue de 2007 estime environ 100 mmol de chlorure de potassium pour une hausse d'environ 0,3 mmol/l {5}", "c'est une estimation de revue, pas une posologie AIPS", "l'information 29552 reste le plafond du produit nommé", "ne pas les additionner sans lire les deux"),
    ("La voie périphérique de la revue de 2007 ne dépasse pas 40 mmol par litre de solution {5}", "et 20 mmol par heure sous surveillance du rythme", "l'information 29552 écrit d'autres plafonds indicatifs", "on cite les deux sans les fusionner"),
    ("Le magnésium corporel est surtout osseux, environ 60 %, puis musculaire, environ 25 % {6}", "le sang n'en montre qu'environ 1 %", "un chiffre normal n'exclut pas un stock bas", "on le dose quand même devant le couple potassium-calcium"),
    ("Le phosphate alimentaire est absorbé à 55-70 %, et 80 à 90 % du filtrat est réabsorbé {7}", "la PTH et le FGF23 freinent cette réabsorption", "une filtration basse inverse le bilan", "la leçon ne chiffre pas l'hyperphosphatémie"),
),
L(
    ("Confondre 4 mg de Zometa et 5 mg d'Aclasta est le piège de produit {15}", "les numéros 56257 et 57363 ne sont pas interchangeables", "l'un vise l'hypercalcémie maligne, l'autre l'os", "la grossesse contre-indique les deux dans les textes lus"),
    ("Oublier que le salbutamol nébulisé du guide de 2023 n'a pas de milligrammes recopiés ici {3}", "la conduite adjuvante est nommée", "la dose chiffrée est hors de l'AIPS lue", "elle reste dans les incertitudes"),
    ("Prendre l'estimation de 100 mmol de la revue pour une ordre AIPS {5}", "la revue n'est pas l'information 29552", "on dit d'où vient chaque plafond", "on ne les additionne pas"),
    ("Traiter une hyperphosphatémie avec un seuil inventé {7}", "le texte de 2019 n'en donne pas", "on raisonne sur la filtration et la PTH", "on ne fabrique pas une borne"),
),
]
for i, items in enumerate(EXTRAS):
    P[i]["fenetre"].extend(exp(items))

PLUS = [
    "On relit la borne avant de la citer à l'oral.",
    "Une proportion lue dans une revue reste datée et située.",
    "Le stock total et le chiffre sanguin ne racontent pas la même chose.",
    "Nommer le danger prend une phrase, nommer la cause en prend une autre.",
    "On fait répéter le nom du médicament et l'heure de la dernière prise.",
    "Un second passage clinique après le geste vérifie qu'on a visé juste.",
    "Le syndrome se confirme par un deuxième chiffre concordant.",
    "On écrit le critère avec sa source, pas de mémoire.",
    "L'examen qui oriente le mécanisme passe avant l'examen de confort.",
    "On dit à voix haute le rang E avant de choisir le flacon.",
    "On lit l'indication du produit, pas seulement la ligne de dose.",
    "La prévention se note dans le plan de sortie.",
    "Trois bornes bien sues valent mieux qu'une liste floue.",
    "Le piège se récite avec la phrase qui le défait.",
]
for i, ph in enumerate(PLUS):
    P[i]["fiche"].append(ph)

DEUX = [
L(
    ("Le coma du tableau de 2014 correspond à une échelle de Glasgow à 8 ou en dessous {2}", "le tenir pour un symptôme sévère", "ne pas attendre un chiffre plus bas pour commencer", "répéter le sodium après le premier bolus"),
    ("Les déficits d'attention existent déjà dans l'hyponatrémie légère {2}", "ne pas exiger un coma pour admettre un effet cérébral", "ne pas appeler cela un score validé de la leçon", "le guide refuse le mot asymptomatique au sens strict"),
),
L(
    ("La préparation de coloscopie et l'exercice figurent parmi les contextes aigus {2}", "demander les 48 dernières heures", "ne pas les ranger avec les causes chroniques", "dater le début des symptômes"),
    ("Une hyponatrémie de ville sans symptôme sévère laisse le temps du diagnostic {2}", "mesurer l'osmolalité", "ne pas perfuser d'emblée le salé à 3 %", "réserver ce geste aux symptômes sévères"),
),
L(
    ("Le thiazidique favorise plus l'hyponatrémie que le diurétique de l'anse selon le guide de 2014 {2}", "nommer la classe", "ne pas les traiter comme équivalents", "la revue de 2007 dit la même chose pour la profondeur de l'hypokaliémie"),
    ("Un apport potassique sous 25 mmol par jour peut baisser le potassium le temps que le rein s'adapte {5}", "chercher l'anorexie et l'alcool", "ce n'est pas la cause la plus fréquente", "les diurétiques le restent"),
),
L(
    ("L'hyperaldostéronisme primaire se cherche si le potassium est bas et la pression haute {5}", "le volume n'est pas diminué", "le chlore urinaire n'est pas celui de la déshydratation", "traiter la cause, pas seulement le comprimé"),
    ("Une sonde gastrique ou des vomissements répétés miment une perte digestive alors que le rein perd le potassium {5}", "chercher l'alcalose", "ne pas compter seulement le liquide aspiré", "la revue décrit ce piège"),
),
L(
    ("Une faiblesse qui s'aggrave en quelques heures avec un potassium très bas fait craindre l'arrêt respiratoire {5}", "surveiller la force inspiratoire", "ne pas laisser le patient seul", "préparer la voie veineuse diluée"),
    ("Une confusion récente avec un calcium au-dessus de 3,5 mmol/l est une urgence du guide de 2016 {8}", "réhydrater", "ne pas attendre la PTH pour le premier litre", "la PTH oriente ensuite"),
),
L(
    ("On compte la fréquence respiratoire si le phosphate est inférieur à 0,32 mmol/l {7}", "la revue cite l'atteinte respiratoire", "ne pas se limiter au muscle des membres", "substituer quand le phosphate est dans la zone sévère"),
    ("On cherche une bande kératique seulement si l'œil est douloureux et le calcium haut {8}", "c'est un signe lu, pas constant", "il ne remplace pas le dosage", "le raccourcissement de QT est plus directement électrique"),
),
L(
    ("Potassium haut et médicaments du SRAA forment le couple le plus modifié en ville {3}", "revoir la dose ou ajouter un chélateur d'entretien si ce n'est pas une urgence", "ne pas utiliser ce chélateur pour un tracé menaçant", "l'hôpital reste la règle de la forme sévère"),
    ("Calcium bas et magnésium bas se corrigent ensemble {6}", "le magnésium participe à la libération de PTH", "ne pas conclure trop vite à une hypoparathyroïdie", "doser le magnésium avant de nommer la parathyroïde"),
),
L(
    ("Une urine très diluée, à 100 mOsm/kg ou moins, fait retenir l'excès d'eau {2}", "ce n'est pas le profil du SIAD", "le SIAD concentre en général trop l'urine", "chercher la polydipsie"),
    ("Zometa parle d'hypercalcémie maligne au-dessus de 3,0 mmol/l de calcium corrigé {15}", "le guide de 2016 parle d'urgence au-dessus de 3,5", "les deux seuils ne se remplacent pas", "on cite chacun"),
),
L(
    ("Le gaz du sang donne un potassium d'attente pendant que le laboratoire tourne {3}", "ne pas traiter un artefact évident", "ne pas ignorer un chiffre haut concordant", "le prélèvement sur héparinate de lithium est préféré pour aller vite"),
    ("Le phosphate du matin n'est pas celui de la nuit {7}", "la variation lue atteint 40 %", "noter l'heure", "ne pas crier à la guérison sur un seul matin"),
),
L(
    ("Si les symptômes d'hyponatrémie ne bougent pas après 10 mmol/l de hausse, chercher une autre cause {2}", "ne pas dépasser ce plafond le premier jour", "le guide le dit même sans amélioration", "l'imagerie se discute alors"),
    ("Le salbutamol nébulisé est un adjuvant de l'hyperkaliémie sévère dans le guide de 2023 {3}", "on ne recopie pas ses milligrammes", "ils ne sont pas dans l'AIPS lue", "l'insuline non plus, pour la même raison"),
),
L(
    ("Resonium par voie rectale utilise 30 g, à retenir le plus longtemps possible {13}", "l'information parle de 4 à 10 heures si le patient y arrive", "la bouche reste plus efficace, le rectum plus rapide", "pas de sorbitol"),
    ("La dose diagnostique adulte de Minirin injectable lue pour le test de concentration est de 4 µg {17}", "ce n'est pas le traitement d'une hyponatrémie", "l'hyponatrémie contre-indique le produit", "on jette la première heure d'urine du test"),
),
L(
    ("Montrer au patient comment atteindre la carafe fait partie de la prévention {4}", "l'hypernatrémie hospitalière est souvent un défaut d'accès", "ne pas s'arrêter à la prescription d'eau", "vérifier que la gorgée a lieu"),
    ("Séparer Veltassa des autres comprimés d'environ 3 heures {12}", "certains médicaments n'exigent pas cet intervalle selon l'information", "en pratique on vérifie la liste", "on ne le donne pas à la place du geste d'urgence"),
),
L(
    ("Aclasta à 5 mg est annuel dans l'ostéoporose, pas dans l'hypercalcémie maligne {16}", "une clairance sous 35 ml par minute le contre-indique", "Zometa a sa propre lecture rénale", "on ne les substitue pas"),
    ("Le magnésium oral de 12 à 15 mmol par jour s'arrête si un autre trouble est sévère {6}", "la revue le dit", "la forme sévère n'est pas ce schéma", "on surveille l'excès si le rein est faible"),
),
L(
    ("Dire que tout calcium haut se traite par le diurétique de l'anse contredit le guide de 2016 {8}", "ce diurétique ne fait pas baisser le calcium de façon utile", "on ne l'ajoute que si la surcharge apparaît", "la réhydratation est le premier temps"),
    ("Oublier la contre-indication de grossesse de Zometa {15}", "le texte l'écrit", "Aclasta l'écrit aussi", "on le dit avant la perfusion"),
),
]
for i, items in enumerate(DEUX):
    P[i]["fenetre"].extend(exp(items))

P[5]["sous"][0]["phrases"] += [
    "On note l'heure du premier signe neurologique pour juger l'ancienneté.",
    "Une crise fait commencer le geste sans attendre le scanner si le sodium est très bas et le lien crédible. {2}",
    "On réévalue la vigilance après chaque bolus de salé à 3 %.",
    "Un déficit d'attention isolé ne déclenche pas le schéma des symptômes sévères.",
]
P[5]["sous"][1]["phrases"] += [
    "On compare le poids du jour au poids connu.",
    "Les œdèmes n'excluent pas un volume efficace bas dans l'insuffisance cardiaque. {2}",
    "On note les plis seulement comme un indice faible.",
    "La soif exprimée oriente vers l'hypernatrémie ou l'hypercalcémie selon le chiffre.",
]
P[5]["sous"][2]["phrases"] += [
    "On demande au patient de compter jusqu'à vingt d'une traite si le phosphate est très bas.",
    "Une voix faible peut précéder l'atteinte respiratoire.",
    "On palpe les loges musculaires si la kaliémie est inférieure à 2,0 mmol/l. {5}",
    "Une crampe isolée sans chiffre ne ferme aucun diagnostic de cette leçon.",
]
P[5]["sous"][3]["phrases"] += [
    "On mesure l'intervalle QT et on le compare au calcium. {8}",
    "Une onde U se cherche dans l'hypokaliémie, sans se substituer au dosage. {5}",
    "On répète le tracé après le calcium intraveineux de l'hyperkaliémie. {3}",
    "Un tracé plat n'autorise pas à renvoyer une kaliémie à 6,5 mmol/l. {3}",
]

meta = meta_base(
    h1="Électrolytes anormaux",
    sous="F2.7. Électrolytes anormaux. Texte du 31 octobre 2026.",
    essentiel=[
        "Dix diagnostics organisent la leçon. Le rang E est l'ordre de l'algorithme, pas un classement de fréquence suisse.",
        "Les milligrammes, grammes et microgrammes écrits viennent de l'information professionnelle du produit nommé.",
        "Les sigles s'ouvrent dans [[w-glossaire|la fenêtre des sigles]].",
    ],
    points=P,
    fichier="LOT_155_Phase_A_V0.html",
    fin="FIN_FICHIER LOT_155_Phase_A_V0",
)
p = ecrire(meta)
print(p)
