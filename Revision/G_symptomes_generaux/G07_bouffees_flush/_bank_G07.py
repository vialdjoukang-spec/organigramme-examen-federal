# -*- coding: utf-8 -*-
# Banque G7 — Bouffées vasomotrices (flush) (LOT_007).
# Sources : exclusivement LOT_Claude_Finaux/LOT_007 (Phase A + Phase B DX.1–12, audités C7 : 0 critique sur 26 fichiers).
# Convention : opts[0] = bonne réponse (son « pourquoi pas » est ignoré) ; position finale fixée par build_ssp.py (seed).
# dx : le PREMIER DX.n cité = DX cible (couverture) ; les suivants = discrimination croisée.
R = "../../../repo/LOT_Claude_Finaux/LOT_007/"
def PA(sec, label): return (f"{R}LOT_007_Phase_A_V0.html#{sec}", f"Phase A {label}")
def B(n, p): return (f"{R}LOT_007_Phase_B_V0_DX.{n}.html#dx{n}-p{p}", f"Phase B DX.{n} §{p}")

# ═════════════ BLOC R · RAISONNER (danger d'abord, puis prochain pas)
q("R","DX.8 · flush et hypotension","management","urgences",
 "Une femme de 34 ans est amenée 10 minutes après avoir mangé un plat contenant des noix de cajou. Elle a un flush du visage et du thorax, une urticaire généralisée et une gêne respiratoire. PA 78/45 mmHg, FC 128/min, SpO2 91 %.",
 "Quelle est la première mesure la plus appropriée ?",
 [("Adrénaline 0,3 mg i.m. à la cuisse",""),
  ("Clémastine i.v. puis réévaluation","L'antihistaminique ne traite que la peau ; il est de seconde ligne."),
  ("Prélever la tryptase avant tout traitement","La tryptase se prélève dans les heures suivantes ; elle ne retarde jamais l'adrénaline."),
  ("Méthylprednisolone i.v. en bolus","Le corticoïde n'agit pas en minutes ; seconde ligne."),
  ("Salbutamol en aérosol seul","Il ne corrige ni l'hypotension ni l'œdème.")],
 "Peau atteinte avec atteinte respiratoire et hypotension après un allergène : anaphylaxie (DX.8, 🚩 E1). L'adrénaline intramusculaire à la face antérolatérale de la cuisse, 0,3 mg chez l'adulte, précède tout bilan ; on appelle le 144 et on couche la patiente.",
 "Deuxième dose possible 5 à 15 minutes plus tard si l'état ne s'améliore pas.",
 PA("ssp-p11","§11 Prise en charge (urgences)"))

q("R","DX.8 · position","management","domicile",
 "Un homme de 45 ans piqué par une guêpe il y a 5 minutes est pâle, couvert d'urticaire, et dit qu'il va s'évanouir. Il veut se lever pour aller aux toilettes. Il vient de recevoir 0,3 mg d'adrénaline i.m. de son autoinjecteur. Il respire sans difficulté.",
 "Quelle consigne est la plus appropriée ?",
 [("Rester couché, jambes surélevées",""),
  ("Marcher pour activer la circulation","Faire lever le patient expose à l'arrêt circulatoire, cœur vide."),
  ("Position assise, jambes pendantes","Elle est réservée à la détresse respiratoire dominante."),
  ("Debout, appuyé contre un mur","La position debout chute le retour veineux."),
  ("Position ventrale pour libérer les voies aériennes","Elle n'a aucun intérêt et gêne la surveillance.")],
 "Dans l'anaphylaxie, le décubitus jambes surélevées soutient le retour veineux et la tension (DX.8). On assoit seulement en cas de détresse respiratoire, on met en position latérale en cas de vomissements ou d'inconscience, en décubitus latéral gauche pendant la grossesse.",
 "Ne jamais faire lever un patient anaphylactique : risque d'arrêt « cœur vide ».",
 PA("ssp-p11","§11 Prise en charge (urgences)"))

q("R","DX.8 · surveillance","management","urgences",
 "Une femme de 28 ans a reçu de l'adrénaline i.m. pour une anaphylaxie alimentaire il y a 45 minutes. Elle va bien : PA 118/72 mmHg, plus d'urticaire, auscultation libre. Elle demande à rentrer chez elle.",
 "Quelle est la conduite la plus appropriée ?",
 [("Observation prolongée de plusieurs heures",""),
  ("Sortie immédiate avec antihistaminique","La réaction biphasique survient souvent dans les 6 à 12 heures."),
  ("Sortie après une dose de corticoïde oral unique","Le corticoïde ne prévient pas de façon fiable la réaction biphasique."),
  ("Hospitalisation de 7 jours en médecine interne","Durée sans justification si l'état est stable."),
  ("Test cutané immédiat à l'allergène","Le bilan allergologique se fait à distance.")],
 "La moitié des réactions biphasiques survient dans les 6 à 12 heures : l'observation prolongée est justifiée (DX.8). À la sortie : deux autoinjecteurs, un plan d'action écrit, l'enseignement du geste et une consultation d'allergologie.",
 "Tryptase de crise entre 15 minutes et 3 heures, puis tryptase basale après 24 heures.",
 B(8,11))

q("R","DX.10 vs DX.3 · crise paroxystique","assessment_diagnosis","cabinet",
 "Un homme de 41 ans décrit depuis 4 mois des crises brutales de céphalées, palpitations et sueurs, avec pâleur puis rougeur, de 20 minutes. On l'a étiqueté anxieux. PA mesurée pendant une crise : 210/115 mmHg ; 132/84 mmHg entre les crises.",
 "Quel examen est le plus approprié en premier ?",
 [("Métanéphrines plasmatiques libres",""),
  ("TDM des surrénales sans biologie","L'imagerie suit une biochimie positive."),
  ("5-HIAA urinaire des 24 heures","Il cible le syndrome carcinoïde, flush sec avec diarrhée."),
  ("Tryptase sérique basale","Elle cible la mastocytose."),
  ("Échelle d'anxiété et TCC d'emblée","Une hypertension paroxystique impose d'exclure le phéochromocytome avant la panique.")],
 "Triade céphalées, palpitations, sueurs avec hypertension paroxystique : phéochromocytome jusqu'à preuve du contraire (DX.10, 🚩 E3). Les métanéphrines plasmatiques libres sont le premier examen (CHUV, OPAS) ; la tension peut être normale entre les crises.",
 "Métanéphrines plasmatiques libres : sensibilité 99 %, spécificité 89 %.",
 B(10,9))

q("R","DX.10 · alpha avant bêta","management","urgences",
 "Une femme de 52 ans a des métanéphrines plasmatiques libres très élevées et une masse surrénalienne droite de 4 cm. Elle se présente pour palpitations : FC 124/min, PA 176/104 mmHg. L'interne propose du propranolol.",
 "Quelle est la conduite la plus appropriée ?",
 [("Alphabloquant d'abord, bêtabloquant ensuite",""),
  ("Propranolol seul pour ralentir le cœur","Le bêtabloquant seul laisse l'effet alpha sans opposition : crise hypertensive."),
  ("Glucagon pour soutenir le cœur","Le glucagon libère des catécholamines ; il est contre-indiqué."),
  ("Surrénalectomie en urgence sans préparation","L'opération se fait après le blocage alpha."),
  ("Diurétique de l'anse en bolus","La patiente a un volume plasmatique réduit.")],
 "Dans le phéochromocytome, l'alphabloquant précède toujours le bêtabloquant (DX.10). L'AIPS du propranolol précise « seulement en association avec un alphabloquant » ; le bêta-blocage seul peut aggraver la crise.",
 "Le bêtabloquant n'est ajouté que si la tachycardie persiste après l'alpha-blocage.",
 B(10,13))

q("R","DX.10 · crise hypertensive","management","urgences",
 "Un homme de 48 ans avec phéochromocytome connu, non encore opéré, arrive en crise : PA 220/125 mmHg, céphalée intense, sueurs. ECG sans signe d'ischémie, glycémie 6,1 mmol/L.",
 "Quel traitement immédiat est le plus approprié ?",
 [("Urapidil i.v. 10 à 50 mg, patient couché",""),
  ("Métoprolol i.v. en bolus","Aucun bêtabloquant avant l'alpha-blocage."),
  ("Nifédipine sublinguale et sortie","Une crise catécholaminergique se traite sous monitorage, à l'hôpital."),
  ("Glucagon 1 mg i.m.","Le glucagon déclenche une crise hypertensive dans le phéochromocytome."),
  ("Observation sans traitement pendant 2 heures","Risque d'accident vasculaire cérébral.")],
 "Crise catécholaminergique : patient couché, scope, voie veineuse, puis urapidil i.v. 10 à 50 mg ; la baisse de tension est attendue en 5 minutes (AIPS Ebrantil®) (DX.10). Si la tension reste élevée : perfusion d'urapidil ou nitroprussiate.",
 "Après la crise : doser les métanéphrines, débuter l'alpha-blocage oral, planifier l'imagerie.",
 B(10,11))

q("R","DX.7 · flush fébrile grave","management","urgences",
 "Une femme de 74 ans est amenée pour flush, frissons et confusion depuis ce matin. T 39,4 °C, FR 26/min, PA 92/55 mmHg. Elle a des brûlures mictionnelles depuis 3 jours.",
 "Quelle est la conduite la plus appropriée ?",
 [("Hémocultures et antibiotique dans l'heure",""),
  ("Paracétamol et contrôle de la température à 2 h","L'antipyrétique ne traite pas le sepsis."),
  ("5-HIAA urinaire pour flush avec frissons","Le flush accompagne ici une infection grave."),
  ("Uroculture puis attente du résultat","L'antibiotique ne doit pas attendre la culture."),
  ("Adrénaline i.m. pour hypotension avec flush","Pas d'urticaire ni d'allergène : rien n'évoque l'anaphylaxie.")],
 "Flush avec fièvre, confusion, polypnée et hypotension : qSOFA à 3, sepsis probable (DX.7, 🚩 E2). Hémocultures et lactate, antibiotique dans l'heure, remplissage vasculaire.",
 "Le qSOFA dépiste (FR ≥ 22/min, conscience altérée, PAS ≤ 100 mmHg) ; il ne pose pas le diagnostic.",
 B(7,13))

q("R","DX.7 · hyperthermie","management","urgences",
 "Un homme de 30 ans sous neuroleptique est amené par une chaude journée d'été : il est rouge, confus, la peau sèche. T rectale 40,6 °C. Il a reçu 1 g de paracétamol il y a 1 heure, sans effet.",
 "Quelle est la prochaine étape la plus appropriée ?",
 [("Refroidissement externe immédiat",""),
  ("Deuxième dose de paracétamol 1 g","La consigne hypothalamique est normale : l'antipyrétique n'agit pas."),
  ("Métamizole i.v.","Antipyrétique inefficace dans l'hyperthermie, et risque d'agranulocytose."),
  ("Attendre le résultat des hémocultures","Le refroidissement passe avant le bilan."),
  ("Ibuprofène 400 mg per os","Aucun antipyrétique n'agit sur une hyperthermie.")],
 "Température élevée sans réponse au paracétamol, avec chaleur et neuroleptique : hyperthermie non pyrogène, la consigne hypothalamique est normale (DX.7). On refroidit immédiatement et on cherche la cause.",
 "Fièvre = consigne relevée par la PGE2 ; hyperthermie = consigne normale débordée.",
 B(7,14))

q("R","DX.4 · orage thyréotoxique","management","urgences",
 "Une femme de 38 ans avec maladie de Basedow, qui a arrêté son traitement, est amenée agitée et confuse. T 39,8 °C, FC 168/min irrégulière, flush et sueurs profuses. TSH effondrée.",
 "Quelle est la conduite la plus appropriée ?",
 [("Soins intensifs, thyréostatique et bêtabloquant",""),
  ("Iode radioactif en urgence","Il ne s'utilise pas en phase aiguë."),
  ("Paracétamol et retour à domicile","Mortalité élevée sans soins intensifs."),
  ("Scintigraphie thyroïdienne avant tout traitement","Le traitement ne doit pas attendre l'imagerie."),
  ("Thyroïdectomie totale dans l'heure","Le traitement initial est médical.")],
 "Fièvre, agitation, tachycardie extrême chez une hyperthyroïdienne : crise thyrotoxique (DX.4, 🚩 E4). Soins intensifs, thyréostatique à forte dose, propranolol 10 à 40 mg 3 à 4 fois par jour en l'absence d'asthme.",
 "Le score de Burch et Wartofsky ou de la JTA aide à reconnaître la crise.",
 PA("ssp-p11","§11 Prise en charge (urgences)"))

q("R","DX.9 · flush sec et diarrhée","assessment_diagnosis","cabinet",
 "Un homme de 63 ans consulte pour des flushs secs, brefs, du visage et du thorax, et une diarrhée aqueuse de 6 selles par jour depuis 2 mois. Il siffle parfois. Le foie est palpable, nodulaire.",
 "Quel examen est le plus approprié pour confirmer le diagnostic ?",
 [("5-HIAA urinaire des 24 heures",""),
  ("Métanéphrines plasmatiques libres","Elles ciblent le phéochromocytome, flush humide avec hypertension."),
  ("Chromogranine A sérique seule","Elle est élevée dans les TNE avec ou sans syndrome."),
  ("Calcitonine sérique","Elle cible le carcinome médullaire, avec nodule thyroïdien."),
  ("FSH et estradiol","Hors sujet chez un homme ; flush sec avec diarrhée.")],
 "Flush sec avec diarrhée sécrétoire, sibilants et hépatomégalie nodulaire : syndrome carcinoïde (DX.9, 🚩 E5). Le 5-HIAA urinaire des 24 heures confirme, au-delà de 50 µmol/24 h, avec une tumeur identifiée.",
 "Le syndrome n'apparaît que lorsque les médiateurs échappent au foie, le plus souvent par des métastases hépatiques.",
 B(9,13))

q("R","DX.9 · bilan cardiaque","management","policlinique",
 "Un homme de 66 ans a un syndrome carcinoïde confirmé (5-HIAA 410 µmol/24 h) avec métastases hépatiques. Il n'a ni dyspnée ni œdème. L'auscultation est jugée normale.",
 "Quel examen est le plus approprié ensuite ?",
 [("NT-proBNP et échocardiographie",""),
  ("Aucun examen cardiaque si l'auscultation est normale","L'examen du cœur seul est peu fiable."),
  ("Coronarographie","La cardiopathie carcinoïde est valvulaire droite, pas coronarienne."),
  ("Holter de 24 heures seul","Il ne détecte pas l'atteinte valvulaire."),
  ("Épreuve d'effort","Elle ne montre pas la fibrose valvulaire.")],
 "Tout patient avec 5-HIAA élevé reçoit un NT-proBNP et une échocardiographie : l'examen du cœur seul est peu fiable (DX.9). Un 5-HIAA supérieur à 300 µmol/24 h impose l'échocardiographie d'emblée.",
 "NT-proBNP < 260 pg/mL : valeur prédictive négative de 97 % pour la cardiopathie.",
 B(9,10))

q("R","DX.9 · avant anesthésie","management","hôpital",
 "Une femme de 58 ans avec syndrome carcinoïde et métastases hépatiques doit subir une cholécystectomie. L'anesthésiste vous demande la préparation.",
 "Quelle préparation est la plus appropriée ?",
 [("Octréotide i.v. préparé, sans sympathomimétique",""),
  ("Adrénaline en prophylaxie systématique à l'induction","Les sympathomimétiques libèrent les médiateurs et aggravent la crise."),
  ("Alphabloquant 2 semaines avant","Préparation du phéochromocytome, pas du carcinoïde."),
  ("Aucune préparation particulière","La crise carcinoïde peut survenir au bloc."),
  ("Arrêt de l'analogue 1 semaine avant","On poursuit l'analogue sans interruption.")],
 "Avant une anesthésie ou un geste invasif, on prépare l'octréotide intraveineux et on évite les sympathomimétiques pour prévenir la crise carcinoïde (DX.9). Le protocole repose sur un consensus.",
 "La méta-analyse de 2022 ne montre pas de baisse nette de la crise sous octréotide (RC 0,73, IC 0,32–1,66) : rester vigilant.",
 B(9,13))

q("R","DX.12 · avant chirurgie","management","hôpital",
 "Un homme de 39 ans a un carcinome médullaire de la thyroïde confirmé par cytologie (calcitonine 820 ng/L). Le chirurgien planifie la thyroïdectomie.",
 "Quel examen faut-il obtenir avant l'opération ?",
 [("Métanéphrines plasmatiques libres",""),
  ("Scintigraphie à l'iode 131","Les cellules C ne fixent pas l'iode."),
  ("5-HIAA urinaire des 24 heures, sans banane","Il cible le syndrome carcinoïde."),
  ("Tryptase sérique basale","Elle cible la mastocytose."),
  ("FSH et LH","Sans intérêt préopératoire.")],
 "Avant toute chirurgie d'un carcinome médullaire, on exclut un phéochromocytome associé (néoplasie endocrinienne multiple de type 2) par les métanéphrines : l'anesthésie sans alpha-blocage peut déclencher une crise (DX.12).",
 "Ordre : métanéphrines → alpha-blocage et surrénalectomie si positives → thyroïdectomie.",
 B(12,13))

q("R","DX.12 · nodule avec diarrhée","assessment_diagnosis","cabinet",
 "Une femme de 47 ans consulte pour une diarrhée chronique et des flushs. Vous palpez un nodule thyroïdien dur de 2 cm avec une adénopathie cervicale. Sa mère a été opérée d'un « cancer de la thyroïde ».",
 "Quel dosage est le plus approprié ?",
 [("Calcitonine sérique",""),
  ("Thyroglobuline sérique","Marqueur des cancers différenciés, pas des cellules C."),
  ("5-HIAA urinaire des 24 heures","Le nodule thyroïdien oriente vers les cellules C."),
  ("Anticorps anti-TPO","Ils orientent vers une thyroïdite auto-immune."),
  ("Tryptase sérique basale","Elle cible la mastocytose.")],
 "Nodule dur, adénopathie, diarrhée, flush et antécédent familial : carcinome médullaire de la thyroïde (DX.12, 🚩 E7). On dose la calcitonine et on fait une échographie ; au-delà de 100 ng/L, le diagnostic est probable.",
 "Ne jamais opérer un nodule suspect sans calcitonine.",
 B(12,10))

q("R","DX.11 · anaphylaxie au venin","assessment_diagnosis","policlinique",
 "Un homme de 52 ans a fait deux chocs anaphylactiques après des piqûres de guêpe, sans urticaire. Il n'a aucune lésion cutanée. La tryptase prélevée 2 semaines après le dernier épisode est à 24 µg/L.",
 "Quelle est la prochaine étape la plus appropriée ?",
 [("Biopsie de moelle osseuse",""),
  ("Rassurer : tryptase élevée par la crise","Une tryptase basale à distance reflète la charge mastocytaire."),
  ("Antihistaminique seul au long cours","Il ne remplace pas le bilan ni l'adrénaline."),
  ("Échographie thyroïdienne","Aucun argument thyroïdien."),
  ("5-HIAA urinaire des 24 heures","Rien n'évoque un carcinoïde.")],
 "Anaphylaxie au venin sans urticaire avec tryptase basale ≥ 20 µg/L : mastocytose systémique à rechercher (DX.11, 🚩 E6). La biopsie de moelle osseuse, lue selon l'OMS 2022, est l'examen de référence.",
 "Tryptase basale ≥ 20 µg/L = critère mineur, pas un diagnostic.",
 B(11,10))

q("R","DX.11 · trousse d'urgence","management","cabinet",
 "Une femme de 44 ans a une mastocytose systémique indolente confirmée. Elle a des flushs et du prurit, contrôlés par la cétirizine. Elle n'a jamais fait d'anaphylaxie.",
 "Quel élément est le plus important à prescrire en plus ?",
 [("Deux autoinjecteurs d'adrénaline",""),
  ("Avapritinib 200 mg par jour","Dose de la forme avancée, sans indication ici."),
  ("Corticoïde oral au long cours","Aucune indication dans la forme indolente contrôlée."),
  ("Doublement de la dose sans autre mesure","L'antihistaminique ne prévient pas l'anaphylaxie."),
  ("Aucun traitement supplémentaire","La mastocytose expose à l'anaphylaxie.")],
 "Premier but dans la mastocytose : éviter toute nouvelle anaphylaxie, avec une trousse d'adrénaline toujours disponible (DX.11). L'antihistaminique H1 soulage la peau mais ne remplace jamais l'adrénaline.",
 "Prévenir le chirurgien et l'anesthésiste avant tout geste ; carte de patient.",
 B(11,11))

q("R","DX.1 vs DX.4 · TSH d'abord","assessment_diagnosis","cabinet",
 "Une femme de 49 ans consulte pour des bouffées de chaleur avec sueurs depuis 3 mois. Ses cycles sont irréguliers. Elle a perdu 4 kg, a des palpitations et un tremblement fin. T 37,1 °C.",
 "Quel examen est le plus approprié en premier ?",
 [("TSH",""),
  ("FSH sérique","La FSH varie en périménopause et ne pose pas le diagnostic."),
  ("Estradiol sérique","Il ne change pas la décision."),
  ("Métanéphrines plasmatiques libres","Pas d'hypertension paroxystique."),
  ("Échographie pelvienne","Aucun saignement post-ménopausique.")],
 "Amaigrissement, palpitations et tremblement : la TSH précède toute conclusion de ménopause (DX.1, DX.4). Une TSH normale est un critère d'exclusion du diagnostic de bouffées ménopausiques.",
 "Une sueur avec amaigrissement, fièvre ou hypertension paroxystique n'est pas la ménopause.",
 B(1,13))

q("R","DX.1 · forme modérée","management","cabinet",
 "Une femme de 52 ans, aménorrhée depuis 14 mois, a 8 bouffées de chaleur par jour qui perturbent son sommeil. Elle a un utérus. Pas d'antécédent de cancer du sein ni de thrombose. TSH normale.",
 "Quel traitement est le plus approprié ?",
 [("Estradiol transdermique plus progestatif",""),
  ("Estradiol transdermique seul","Avec un utérus, le progestatif protège l'endomètre."),
  ("Clonidine orale en première ligne, au long cours","Ni NICE ni l'AIPS ne la proposent d'emblée."),
  ("Gabapentine en première ligne","Usage hors AIPS, alternative au THM seulement."),
  ("Phyto-œstrogènes de soja","Efficacité non prouvée.")],
 "Bouffées modérées à sévères sans contre-indication : THM en première ligne, le plus efficace (DX.1). Estradiol (Oestrogel® 2 pressions par jour) ; utérus présent → progestatif 12 à 14 jours par mois ou en continu.",
 "Le THM réduit les bouffées d'environ 75 % par rapport au placebo.",
 B(1,11))

q("R","DX.1 · début précoce","assessment_diagnosis","cabinet",
 "Une femme de 32 ans consulte pour des bouffées de chaleur et une aménorrhée de 5 mois. Test de grossesse négatif. TSH normale.",
 "Quelle est la prochaine étape la plus appropriée ?",
 [("FSH et estradiol",""),
  ("THM sans bilan, comme une ménopause","On ne pose pas l'étiquette ménopause avant 40 ans sans bilan."),
  ("Fézolinétant 45 mg par jour","Indiqué chez la femme post-ménopausée, après le diagnostic."),
  ("Rassurer et revoir dans 1 an","Une insuffisance ovarienne prématurée se cherche maintenant."),
  ("Métanéphrines plasmatiques libres","Pas de triade adrénergique.")],
 "Avant 40 ans, on cherche une insuffisance ovarienne prématurée par la FSH et l'estradiol ; on ne conclut pas à une ménopause (DX.1).",
 "Après 45 ans, tableau typique : pas de dosage hormonal ; avant 40 ans : bilan obligatoire.",
 B(1,14))

q("R","DX.3 · douleur thoracique","management","urgences",
 "Une femme de 46 ans, connue pour un trouble panique, consulte pour une crise avec rougeur, sueurs, palpitations et douleur thoracique oppressive depuis 30 minutes. PA 148/90 mmHg, FC 104/min.",
 "Quelle est la prochaine étape la plus appropriée ?",
 [("ECG et troponine",""),
  ("Lorazépam et retour à domicile","On n'attribue pas la crise à la panique sans exclure l'infarctus."),
  ("Exercice de respiration lente seul","Ne ferme pas la branche cardiaque."),
  ("Augmenter l'escitalopram","Ne répond pas à la douleur thoracique aiguë."),
  ("Rendez-vous de psychothérapie","Différer l'évaluation cardiaque est dangereux.")],
 "Une douleur thoracique impose ECG et troponine avant tout autre examen, même chez une patiente anxieuse connue (DX.3). Le flush émotionnel est un diagnostic d'exclusion.",
 "Antécédent psychiatrique = piège d'attribution prématurée.",
 B(3,10))

q("R","DX.6 · red man","management","hôpital",
 "Un homme de 58 ans reçoit sa première dose de vancomycine 1 g i.v. en 15 minutes. Il présente une rougeur du visage et du torse avec prurit. PA 126/78 mmHg, pas de stridor, pas d'urticaire, auscultation libre.",
 "Quelle est la conduite la plus appropriée ?",
 [("Arrêter, puis reprendre à ≤ 10 mg/min",""),
  ("Adrénaline 0,3 mg i.m.","Pas de critère d'anaphylaxie : réaction liée au débit."),
  ("Contre-indication définitive à la vancomycine","Ce n'est pas une allergie vraie."),
  ("Poursuivre au même débit","Le débit trop rapide est la cause."),
  ("Remplacer par un dérivé nitré","Sans rapport avec la réaction.")],
 "Rougeur du torse pendant une perfusion rapide de vancomycine, sans signe d'anaphylaxie : « red man », libération d'histamine dépendante du débit (DX.6). On arrête, puis on reprend à 10 mg/min au plus, en 60 minutes au moins.",
 "La réaction régresse 20 minutes à 2 heures après l'arrêt de la perfusion.",
 B(6,10))

q("R","DX.6 · nitré et PDE5","management","urgences",
 "Un homme de 64 ans angineux prend de la nitroglycérine sublinguale pour une douleur thoracique. Il a pris du sildénafil 4 heures plus tôt. Il est rouge, vertigineux. PA 72/40 mmHg.",
 "Quelle est la conduite immédiate la plus appropriée ?",
 [("Allonger, remplir, surveiller monitoré",""),
  ("Nouvelle dose de nitroglycérine","Aggrave l'hypotension, potentiellement fatale."),
  ("Adrénaline i.m. pour flush avec hypotension","Pas de tableau allergique ; cause pharmacologique."),
  ("Retour à domicile après 30 minutes de repos","Hypotension sévère à surveiller."),
  ("Propranolol i.v.","Aggraverait l'hypotension.")],
 "Nitré et inhibiteur de la PDE5 pris ensemble avec hypotension : allonger, remplissage, surveillance monitorée, supprimer l'association (DX.6). L'association est contre-indiquée par l'AIPS.",
 "Ne jamais associer un nitré et un inhibiteur de la PDE5.",
 B(6,10))

q("R","DX.5 vs DX.8 · alcool et stridor","management","urgences",
 "Un homme de 35 ans développe, 20 minutes après deux verres de vin au restaurant, un flush, une urticaire, un stridor et une PA à 84/50 mmHg.",
 "Quel est le premier geste le plus approprié ?",
 [("Adrénaline i.m.",""),
  ("Disulfirame pour bloquer l'acétaldéhyde","Le disulfirame provoque le flush ; il ne le traite pas."),
  ("Rassurer : flush alcoolique bénin","Stridor et hypotension imposent l'urgence."),
  ("Antihistaminique oral et observation","Seconde ligne ; ne traite pas l'obstruction."),
  ("Test génétique ALDH2","Sans place en urgence.")],
 "Un flush avec urticaire, stridor et hypotension est une anaphylaxie, quel que soit le déclencheur : adrénaline i.m. 0,3 mg, puis surveillance (DX.5, DX.8).",
 "Tout stridor ou hypotension pendant un flush est une urgence.",
 B(5,14))

q("R","DX.4 · agranulocytose","management","cabinet",
 "Une femme de 36 ans prend du carbimazole 30 mg par jour depuis 5 semaines pour une maladie de Basedow. Elle appelle pour une fièvre à 39 °C et une angine.",
 "Quelle est la conduite la plus appropriée ?",
 [("Arrêter et faire une formule sanguine",""),
  ("Amoxicilline et poursuite du carbimazole","Ne pas méconnaître une agranulocytose."),
  ("Augmenter le carbimazole","Aggraverait une agranulocytose."),
  ("Paracétamol et contrôle dans 1 semaine","Délai dangereux."),
  ("Passer à l'iode radioactif dans la semaine","Ne répond pas à l'urgence.")],
 "Fièvre, angine ou aphtes sous thionamide évoquent une agranulocytose : arrêt du médicament et formule sanguine en urgence (AIPS Néo-Mercazole®) (DX.4).",
 "Formule sanguine avant, puis chaque semaine pendant 6 semaines après 40 ans, surtout au-delà de 40 mg par jour.",
 B(4,14))

q("R","DX.2 · œil douloureux","management","cabinet",
 "Un homme de 55 ans suivi pour une rosacée consulte pour un œil droit rouge et douloureux, avec photophobie et baisse de vision depuis la veille.",
 "Quelle est la conduite la plus appropriée ?",
 [("Avis ophtalmologique urgent",""),
  ("Larmes artificielles et contrôle dans 1 mois","Une kératite menace la vue."),
  ("Brimonidine gel autour de l'œil","Topique de l'érythème facial, pas de l'œil."),
  ("Collyre corticoïde sans examen","Ne jamais prescrire avant l'examen ophtalmologique."),
  ("Ivermectine crème sur les paupières","Sans effet sur l'atteinte oculaire.")],
 "Un œil rouge douloureux chez un rosacéen impose un avis ophtalmologique urgent : la kératite menace la vue (DX.2).",
 "L'atteinte oculaire est un phénotype majeur de la rosacée.",
 B(2,13))

q("R","DX.10 · crise peropératoire","management","hôpital",
 "Pendant une surrénalectomie laparoscopique pour phéochromocytome, préparée par alpha-blocage, la PA monte à 230/120 mmHg lors de la manipulation de la tumeur.",
 "Quelle est la conduite la plus appropriée ?",
 [("Nitroprussiate i.v. à 0,2 µg/kg/min",""),
  ("Propranolol i.v. en premier","Bêtabloquant seulement si la tachycardie persiste après l'alpha-blocage."),
  ("Glucagon i.v.","Contre-indiqué : libère des catécholamines."),
  ("Noradrénaline en perfusion","Vasopresseur : aggrave l'hypertension."),
  ("Arrêt définitif de l'intervention chirurgicale","On arrête la manipulation et on traite le pic.")],
 "Pic hypertensif peropératoire : arrêter la manipulation si possible, puis vasodilatateur de courte durée, nitroprussiate débuté à 0,2 µg/kg/min et doublé toutes les 3 à 5 minutes, ou urapidil en injection (DX.10).",
 "Après la ligature de la veine surrénalienne, le risque devient l'hypotension (volume plasmatique réduit).",
 B(10,11), niv="specialiste", spe="Anesthésiologie")

q("R","DX.9 · hypotension au bloc","management","hôpital",
 "Pendant une résection de métastases hépatiques chez un patient carcinoïde, un flush brutal apparaît avec PA 70/40 mmHg et bronchospasme, malgré le remplissage et l'octréotide i.v.",
 "Quel vasopresseur est le plus approprié ?",
 [("Phényléphrine ou vasopressine",""),
  ("Adrénaline en bolus répétés","Les sympathomimétiques classiques libèrent les médiateurs."),
  ("Éphédrine i.v. en bolus","Sympathomimétique : aggrave la crise."),
  ("Dobutamine en perfusion continue","Sympathomimétique, sans effet vasoconstricteur utile."),
  ("Isoprénaline","Sympathomimétique bêta : vasodilatation.")],
 "Crise carcinoïde avec hypotension persistante : phényléphrine ou vasopressine, car les sympathomimétiques classiques aggravent la libération des médiateurs (DX.9). L'octréotide i.v. est poursuivi.",
 "Bronchospasme carcinoïde : éviter aussi les sympathomimétiques ; traitement guidé par l'anesthésiste.",
 B(9,14), niv="specialiste", spe="Anesthésiologie")

q("R","DX.12 · hypocalcémie postopératoire","management","hôpital",
 "Le lendemain d'une thyroïdectomie totale avec curage central pour carcinome médullaire, une femme de 50 ans a des paresthésies péribuccales et des crampes. Signe de Chvostek positif.",
 "Quelle est la conduite immédiate la plus appropriée ?",
 [("Calcium i.v. lent sous scope",""),
  ("Lévothyroxine à dose suppressive","Sans rapport avec la tétanie."),
  ("Calcitriol seul et contrôle dans 1 mois","Le relais oral suit le calcium i.v."),
  ("Furosémide i.v.","Aggraverait l'hypocalcémie."),
  ("Reprise chirurgicale immédiate","L'hypocalcémie se corrige médicalement.")],
 "Hypocalcémie aiguë après thyroïdectomie : ECG, scope, voie veineuse, calcémie ionisée, magnésium et PTH, puis calcium i.v. lent (DX.12). Relais : calcitriol 0,25 µg par jour et calcium oral.",
 "Calcémie deux fois par semaine au début sous calcitriol ; arrêt si dépassement de la norme.",
 B(12,11), niv="specialiste", spe="Endocrinologie")

q("R","DX.7 · fièvre inexpliquée","assessment_diagnosis","policlinique",
 "Un homme de 55 ans, immunocompétent, a une fièvre à 38,6 °C mesurée à plusieurs reprises depuis 5 semaines, avec bouffées de chaleur nocturnes. Le bilan minimal standard (examen, formule, CRP, hémocultures, urines, radiographie du thorax) n'a rien trouvé.",
 "Quel examen est le plus approprié ensuite ?",
 [("PET-TDM",""),
  ("Antibiotique d'épreuve","Masque le diagnostic d'une FPI."),
  ("Corticoïde d'épreuve","Peut masquer un lymphome ou une infection."),
  ("FSH et estradiol","Hors sujet chez un homme fébrile."),
  ("Répéter le même bilan dans 6 mois","Retard diagnostique.")],
 "Fièvre ≥ 38,3 °C à plus de 3 reprises pendant plus de 3 semaines, sans explication après un bilan minimal : fièvre prolongée inexpliquée (Delphi 2024) (DX.7). Le PET-TDM suit, puis la biopsie du site actif.",
 "Une fièvre objective exclut le diagnostic de bouffées ménopausiques.",
 B(7,10), niv="approfondissement")

q("R","DX.8 · choc réfractaire","management","urgences",
 "Une femme de 60 ans en anaphylaxie a reçu deux doses d'adrénaline i.m., de l'oxygène et 2 L de cristalloïde. PA 70/40 mmHg persistante.",
 "Quelle est la prochaine étape la plus appropriée ?",
 [("Adrénaline i.v. titrée en soins monitorés",""),
  ("Troisième dose d'antihistaminique H1 par voie i.v.","Seconde ligne, sans effet hémodynamique."),
  ("Corticoïde i.v. seul","N'agit pas en minutes."),
  ("Attendre la tryptase","Ne guide pas l'urgence."),
  ("Retour à la position assise","Aggrave le retour veineux.")],
 "Choc anaphylactique réfractaire à l'adrénaline i.m. : adrénaline intraveineuse en soins monitorés, 0,05 à 0,1 mg répétable toutes les 3 à 5 minutes (DX.8).",
 "Le glucagon est cité sous bêtabloquant, avec des preuves très limitées.",
 B(8,11), niv="specialiste", spe="Médecine intensive")

# ═════════════ BLOC D · DISCRIMINER (les DX face à face)
q("D","DX.1 · diagnostic clinique","assessment_diagnosis","cabinet",
 "Une femme de 51 ans a depuis 6 mois des accès de chaleur du visage et du thorax suivis de sueurs, de 2 à 3 minutes, et des sueurs nocturnes. Cycles irréguliers. Examen normal, T 36,8 °C. TSH normale.",
 "Quelle est la conduite diagnostique la plus appropriée ?",
 [("Diagnostic clinique, sans dosage",""),
  ("FSH sérique pour confirmer le diagnostic","La FSH varie d'un jour à l'autre en périménopause."),
  ("Estradiol et LH sériques","Aucun dosage ne pose le diagnostic."),
  ("5-HIAA urinaire des 24 heures","Flush humide, sans diarrhée."),
  ("Tryptase sérique basale","Sans urticaire ni anaphylaxie.")],
 "Femme de 40 à 65 ans, bouffées humides récurrentes, température et TSH normales, sans drapeau rouge : bouffées de la ménopause, diagnostic clinique (NAMS 2022–2023) (DX.1).",
 "Après 45 ans, tableau typique : pas de FSH.",
 B(1,8))

q("D","DX.1 · voie non hormonale","management","cabinet",
 "Une femme de 56 ans, traitée il y a 3 ans pour un cancer du sein, a des bouffées sévères. Bilan hépatique normal, DFGe 82 mL/min/1,73 m². Elle ne prend aucun médicament.",
 "Quel traitement est le plus approprié ?",
 [("Fézolinétant 45 mg par jour",""),
  ("Estradiol transdermique","Contre-indiqué après cancer du sein."),
  ("Tibolone 2,5 mg par jour","Récidive accrue après cancer du sein."),
  ("Estradiol plus dydrogestérone","THM contre-indiqué après cancer du sein."),
  ("Clonidine en première ligne","Non proposée d'emblée ; hors AIPS.")],
 "Après cancer du sein, le THM est contre-indiqué : option non hormonale, fézolinétant (VEOZA™) 45 mg une fois par jour, antagoniste NK3 (DX.1).",
 "Bilan hépatique avant, puis chaque mois pendant 3 mois ; réévaluation à 12 mois.",
 B(1,10))

q("D","DX.1 · surveillance VEOZA","management","cabinet",
 "Une femme de 54 ans va débuter le fézolinétant pour des bouffées modérées. Elle demande quel suivi est nécessaire.",
 "Quel suivi est le plus approprié ?",
 [("Bilan hépatique avant, puis mensuel",""),
  ("ECG avant le début, puis à 1 mois","Le suivi AIPS est hépatique."),
  ("FSH tous les 3 mois","Inutile."),
  ("Formule sanguine hebdomadaire 6 semaines","Suivi du carbimazole, pas du fézolinétant."),
  ("Mammographie mensuelle","Sans rapport avec ce médicament.")],
 "VEOZA™ exige ALAT, ASAT, PAL et bilirubine avant le début, puis chaque mois pendant 3 mois (AIPS) (DX.1). On ne débute pas si ALAT ou ASAT > 2 × LSN.",
 "Arrêt si transaminases > 5 × LSN, ou > 3 × LSN avec bilirubine > 2 × LSN.",
 B(1,14))

q("D","DX.2 vs DX.1 · rougeur persistante","assessment_diagnosis","cabinet",
 "Une femme de 48 ans consulte pour des rougeurs du visage déclenchées par la chaleur, l'alcool et les épices. Entre les épisodes persistent un érythème centrofacial, des télangiectasies et quelques papulopustules, sans comédons. Cycles réguliers.",
 "Quel est le diagnostic le plus probable ?",
 [("Rosacée",""),
  ("Bouffées de la ménopause","L'examen est normal entre les épisodes dans la ménopause."),
  ("Acné vulgaire","Les comédons manquent."),
  ("Mastocytose systémique","Pas de signe de Darier ni d'urticaire."),
  ("Syndrome carcinoïde","Pas de diarrhée ; rougeur persistante.")],
 "Rougeur centrofaciale persistante avec poussées : phénotype diagnostique de rosacée, qui suffit seul (NRS 2017, ROSCO 2019) (DX.2). Les comédons orientent vers l'acné.",
 "Rosacée : 5,46 % en population générale (méta-analyse 2018).",
 B(2,8))

q("D","DX.2 · papulopustules","management","cabinet",
 "Un homme de 52 ans a une rosacée avec de nombreuses papulopustules des joues et du menton (IGA 3). Pas d'atteinte oculaire.",
 "Quel traitement est le plus approprié ?",
 [("Ivermectine crème 1 g par jour",""),
  ("Brimonidine gel seul","Elle traite l'érythème, pas les lésions inflammatoires."),
  ("Dermocorticoïde puissant","Il provoque une dermatose rosacéiforme."),
  ("Isotrétinoïne orale","La rosacée n'est pas une indication AIPS."),
  ("Acide azélaïque, indication AIPS rosacée","L'AIPS ne retient que l'acné.")],
 "Rosacée papulopustuleuse moyennement sévère à sévère : ivermectine (Soolantra®) 1 g de crème une fois par jour, jusqu'à 3 mois (AIPS) (DX.2). Évaluation à 3 mois ; arrêt sans amélioration.",
 "Soolantra® pour les papulopustules, Mirvaso® pour l'érythème.",
 B(2,14))

q("D","DX.2 · érythème","management","cabinet",
 "Une femme de 46 ans a une rosacée érythémateuse sans papules. Elle souhaite atténuer la rougeur avant des réunions.",
 "Quel traitement est le plus approprié ?",
 [("Brimonidine gel une fois par jour",""),
  ("Ivermectine crème","Cible les papulopustules."),
  ("Dermocorticoïde de classe III","Induit une dermatose rosacéiforme."),
  ("Propranolol 40 mg","Sans indication dans l'érythème rosacéen."),
  ("Doxycycline 200 mg par jour pendant 3 mois","Dose antibiotique, sans intérêt pour l'érythème seul.")],
 "Érythème facial de la rosacée : brimonidine (Mirvaso®), un petit pois sur chacune des 5 zones du visage, une fois par jour, maximum 1 g (AIPS) (DX.2).",
 "Rebond de l'érythème possible, plus sévère, surtout les 2 premières semaines.",
 B(2,14))

q("D","DX.3 · diagnostic d'exclusion","assessment_diagnosis","cabinet",
 "Un étudiant de 23 ans rougit et transpire dès qu'il doit parler en public, depuis plusieurs années. Il évite les présentations. Examen normal, PA 122/76 mmHg, TSH normale.",
 "Quel est le diagnostic le plus probable ?",
 [("Flush émotionnel",""),
  ("Phéochromocytome","Pas d'hypertension paroxystique ni de céphalées."),
  ("Hyperthyroïdie","TSH normale."),
  ("Syndrome carcinoïde","Pas de diarrhée ni de sifflements."),
  ("Rosacée","Pas de rougeur persistante ni de papulopustules.")],
 "Rougeur liée à la peur du jugement avec évitement, examen et TSH normaux : flush émotionnel sur anxiété sociale (DX.3), diagnostic d'exclusion après élimination des causes organiques.",
 "Anxiété : 14,0 % sur 12 mois en Europe (UE-27, Suisse, 2011).",
 B(3,8))

q("D","DX.3 · traitement de fond","management","cabinet",
 "Une femme de 31 ans a un trouble anxieux généralisé avec épisodes de rougeur et sueurs. Bilan somatique et TSH normaux. Elle souhaite un traitement durable.",
 "Quel traitement de fond est le plus approprié en première intention ?",
 [("Psychothérapie cognitivo-comportementale",""),
  ("Lorazépam 1 mg trois fois par jour au long cours","Les benzodiazépines servent brièvement, pas en fond."),
  ("Propranolol au long cours seul","Il ne traite que les symptômes somatiques."),
  ("Fézolinétant","Indiqué dans les bouffées de la ménopause."),
  ("Brimonidine gel","Traitement de la rosacée.")],
 "La TCC est le traitement de première intention des troubles anxieux (DX.3) ; l'escitalopram (Cipralex®) 10 mg par jour peut s'y ajouter.",
 "Lorazépam : durée la plus brève possible, généralement pas plus de 2 à 3 mois (AIPS).",
 B(3,13))

q("D","DX.3 vs DX.4 · anxieux avec TSH basse","assessment_diagnosis","cabinet",
 "Une femme de 29 ans se dit anxieuse depuis 2 mois : flushs, palpitations, insomnie, perte de 3 kg. FC 112/min. TSH < 0,01 mUI/L, fT4 élevée.",
 "Quel est le diagnostic le plus probable ?",
 [("Hyperthyroïdie",""),
  ("Trouble anxieux généralisé","L'anxiété est ici un symptôme de thyrotoxicose."),
  ("Trouble panique","La TSH basse oriente vers une cause organique."),
  ("Bouffées de la ménopause","Âge et biologie incompatibles."),
  ("Flush médicamenteux","Aucun médicament en cause.")],
 "TSH supprimée avec fT4 élevée : hyperthyroïdie franche (DX.3, DX.4). L'anxiété est un symptôme de thyrotoxicose, non une cause à traiter seule.",
 "Toujours doser TSH et fT4 chez un patient qui rougit et qui est anxieux.",
 B(3,14))

q("D","DX.4 · diagnostic biologique","assessment_diagnosis","cabinet",
 "Un homme de 44 ans a une thermophobie, des sueurs, des flushs humides et un tremblement fin. FC 108/min. TSH 0,02 mUI/L.",
 "Quel examen est le plus approprié pour confirmer l'hyperthyroïdie franche ?",
 [("fT4 et T3",""),
  ("Scintigraphie en premier","Elle cherche la cause, après la confirmation."),
  ("Anticorps anti-TPO","Ils ne confirment pas l'hyperthyroïdie."),
  ("Calcitonine sérique","Elle cible le carcinome médullaire."),
  ("Répéter la TSH dans 6 mois","Retard ; on complète d'emblée par fT4 et T3.")],
 "Une TSH basse isolée ne suffit pas : la fT4 et la T3 élevées posent l'hyperthyroïdie franche ; fT4 et T3 normales définissent la forme subclinique (DX.4).",
 "Ensuite : TSH-R-Ab, échographie, scintigraphie pour la cause.",
 B(4,8))

q("D","DX.4 · grossesse","management","hôpital",
 "Une femme de 30 ans enceinte de 8 semaines a une maladie de Basedow active : TSH supprimée, fT4 élevée, TSH-R-Ab positifs.",
 "Quel thyréostatique est le plus approprié ?",
 [("Propylthiouracile",""),
  ("Carbimazole","Plus tératogène au 1er trimestre."),
  ("Iode radioactif","Contre-indiqué pendant la grossesse."),
  ("Propranolol seul au long cours","Ne traite pas la cause."),
  ("Lévothyroxine","Aggraverait la thyrotoxicose.")],
 "Au 1er trimestre, le propylthiouracile est préféré, car le carbimazole est plus tératogène ; ensuite on revient au carbimazole, car le propylthiouracile est hépatotoxique (DX.4).",
 "Avis d'endocrinologie ; contraception fiable sous carbimazole.",
 B(4,14))

q("D","DX.4 · TSH normale","assessment_diagnosis","cabinet",
 "Une femme de 50 ans a des bouffées humides et des palpitations. TSH 1,8 mUI/L. PA 124/78 mmHg, sans crise hypertensive. Aménorrhée depuis 8 mois.",
 "Quelle conclusion est la plus appropriée concernant la thyroïde ?",
 [("Hyperthyroïdie exclue",""),
  ("Doser fT3 pour exclure une T3-toxicose","TSH normale : hyperthyroïdie exclue."),
  ("Scintigraphie thyroïdienne","Sans indication."),
  ("Thyréostatique d'épreuve","Aucune base biologique."),
  ("Anticorps anti-récepteur de la TSH","Sans indication.")],
 "Une TSH normale exclut l'hyperthyroïdie ; on cherche alors DX.1 à DX.3 et les autres causes de flush (DX.4).",
 "TSH normale = critère d'exclusion respecté pour poser le diagnostic de ménopause.",
 B(4,10))

q("D","DX.5 · déficit en ALDH2","assessment_diagnosis","cabinet",
 "Un homme de 26 ans d'origine japonaise rougit intensément 5 à 10 minutes après chaque verre d'alcool, quelle que soit la boisson. Il n'a jamais de flush sans alcool. Il ne prend aucun médicament.",
 "Quel est le diagnostic le plus probable ?",
 [("Déficit en ALDH2",""),
  ("Syndrome carcinoïde","Il donne des flushs spontanés avec diarrhée."),
  ("Mastocytose systémique","Flushs aussi sans alcool, prurit."),
  ("Rosacée","Rougeur persistante entre les épisodes."),
  ("Phéochromocytome","Crises hypertensives sans lien avec l'alcool.")],
 "Flush reproductible 5 à 10 minutes après l'alcool, origine d'Asie de l'Est, sans flush spontané : déficit en ALDH2 (DX.5). L'acétaldéhyde s'accumule.",
 "Questionnaire à deux questions : environ 90 % de sensibilité et de spécificité.",
 B(5,8))

q("D","DX.5 · métronidazole","management","cabinet",
 "Une femme de 38 ans débute du métronidazole pour une vaginite à Gardnerella. Elle demande si elle peut boire du vin au mariage de sa sœur dans 3 jours.",
 "Quel conseil est le plus approprié ?",
 [("Aucun alcool pendant et le jour suivant",""),
  ("Alcool permis en petite quantité","Une réaction de type disulfirame est possible."),
  ("Alcool permis après la première dose","La consigne couvre tout le traitement."),
  ("Arrêter le métronidazole le jour du mariage","Interrompre le traitement est inutile."),
  ("Prendre un antihistaminique avant de boire","Ne prévient pas la réaction.")],
 "Sous métronidazole, aucun alcool pendant le traitement et le jour suivant (AIPS Flagyl®) (DX.5).",
 "Disulfirame et métronidazole bloquent la dégradation de l'acétaldéhyde.",
 B(5,13))

q("D","DX.5 · sous disulfirame","management","cabinet",
 "Un homme de 49 ans a arrêté le disulfirame il y a 10 jours. Il demande s'il peut boire une bière.",
 "Quel conseil est le plus approprié ?",
 [("Réaction possible jusqu'à 3 semaines",""),
  ("Aucun risque après 48 heures","L'enzyme repousse en une semaine ou plus."),
  ("Aucun risque après 7 jours","La réaction reste possible plus longtemps."),
  ("Risque seulement avec les alcools forts","Toute quantité peut déclencher la réaction."),
  ("Risque seulement s'il reprend le disulfirame","Le risque persiste après l'arrêt.")],
 "Après l'arrêt d'Antabus®, la réaction reste possible jusqu'à trois semaines ; l'enzyme repousse en une semaine ou plus (DX.5).",
 "Sous disulfirame, même l'alcool caché (médicaments, aliments) provoque un flush.",
 B(5,14))

q("D","DX.6 · inhibiteur calcique","assessment_diagnosis","cabinet",
 "Une femme de 61 ans hypertendue a débuté l'amlodipine 5 mg il y a 10 jours. Elle a depuis des rougeurs du visage, bien tolérées. PA 136/82 mmHg. Examen normal.",
 "Quel est le diagnostic le plus probable ?",
 [("Flush médicamenteux",""),
  ("Bouffées de la ménopause","Le lien chronologique avec le médicament prime."),
  ("Phéochromocytome","PA contrôlée, sans triade."),
  ("Rosacée","Pas de rougeur persistante ni de papules."),
  ("Anaphylaxie","Ni urticaire ni hypotension.")],
 "Flush apparu après l'introduction d'un vasodilatateur : flush médicamenteux ; la rougeur du visage est un effet indésirable fréquent de l'amlodipine (AIPS) (DX.6).",
 "Le flush s'atténue souvent en quelques semaines ; ne pas arrêter un inhibiteur calcique sans avis.",
 B(6,8))

q("D","DX.6 · persistance","assessment_diagnosis","cabinet",
 "Un homme de 57 ans a arrêté la niacine il y a 4 semaines, mais ses flushs secs persistent et s'accompagnent de selles liquides.",
 "Quelle est la prochaine étape la plus appropriée ?",
 [("5-HIAA urinaire des 24 heures",""),
  ("Rassurer : effet résiduel de la niacine","Un flush persistant à l'arrêt fait chercher une autre cause."),
  ("Reprendre la niacine avec aspirine","Ne traite pas un flush d'autre cause."),
  ("Aucun examen, contrôle dans 1 an","Retard d'un carcinoïde possible."),
  ("FSH sérique","Hors sujet.")],
 "Un flush qui persiste à l'arrêt du médicament impose de chercher carcinoïde, mastocytose ou phéochromocytome (DX.6, DX.9) ; avec des selles liquides, le 5-HIAA des 24 h.",
 "La régression à l'arrêt est le critère d'imputabilité le plus fort.",
 B(6,13))

q("D","DX.7 · seuil de fièvre","assessment_diagnosis","cabinet",
 "Une femme de 47 ans dit avoir « de la fièvre » avec ses bouffées de chaleur. Elle se sent chaude, sans frissons. T tympanique 37,2 °C au cabinet.",
 "Quel élément est le plus approprié pour affirmer une fièvre ?",
 [("Température centrale mesurée ≥ 38,0 °C",""),
  ("Sensation de chaleur rapportée","Le flush seul ne suffit pas à poser la fièvre."),
  ("Rougeur du visage","Signe de flush, non de fièvre."),
  ("Sueurs nocturnes","Nombreuses causes."),
  ("Mesure axillaire isolée à 37,9 °C, au domicile","Mesure périphérique peu fiable.")],
 "La fièvre se prouve par la température centrale mesurée (≥ 38,3 °C selon les sociétés, 38,0 °C en usage clinique) ; le flush seul ne suffit pas (DX.7).",
 "Piège : confondre fièvre et bouffée ménopausique.",
 B(7,8))

q("D","DX.7 · dose de paracétamol","management","cabinet",
 "Un homme de 70 kg a une grippe avec fièvre à 38,9 °C et frissons. Fonction rénale et hépatique normales.",
 "Quelle posologie de paracétamol est la plus appropriée ?",
 [("1 g toutes les 6 h, max 4 g/j",""),
  ("2 g toutes les 6 h","Dépasse la dose maximale."),
  ("1 g toutes les 2 h","Intervalle trop court."),
  ("500 mg une fois par jour","Sous-dosé."),
  ("1 g toutes les 4 h, max 6 g/j","Dépasse 4 g par jour.")],
 "Paracétamol (Dafalgan®) adulte > 40 kg : 500 à 1 000 mg par prise, intervalle de 4 à 8 heures, maximum 4 g par jour (AIPS) (DX.7).",
 "3 g/j si clairance 10–50 mL/min ; 2 g/j si < 10 mL/min.",
 B(7,14))

q("D","DX.8 · hypotension sans peau","assessment_diagnosis","domicile",
 "Une femme de 57 ans, connue pour une allergie au venin de guêpe, est piquée au jardin. Quelques minutes plus tard, elle est vertigineuse, PA 76/44 mmHg. Aucune urticaire, aucun prurit.",
 "Quel est le diagnostic le plus probable ?",
 [("Anaphylaxie",""),
  ("Malaise vagal simple","Hypotension après un allergène connu : anaphylaxie jusqu'à preuve du contraire."),
  ("Urticaire aiguë","Absente."),
  ("Flush émotionnel","Diagnostic d'exclusion."),
  ("Réaction locale étendue","N'explique pas l'hypotension.")],
 "L'hypotension après un allergène connu suffit à poser l'anaphylaxie, même sans atteinte cutanée (critère 2, WAO 2020) (DX.8).",
 "Hypotension adulte : PAS < 90 mmHg ou baisse > 30 %.",
 B(8,14))

q("D","DX.8 · urticaire chronique","management","cabinet",
 "Une femme de 35 ans a des papules urticariennes prurigineuses fugaces presque chaque jour depuis 3 mois, sans angio-œdème ni déclencheur physique. Hémogramme et CRP normaux.",
 "Quel traitement est le plus approprié en première ligne ?",
 [("Antihistaminique H1 de 2e génération",""),
  ("Corticoïde oral au long cours, à dose dégressive","Seulement en cure courte pour une poussée."),
  ("Omalizumab d'emblée","Après échec des antihistaminiques."),
  ("Antihistaminique à la demande","Il se prend chaque jour."),
  ("Adrénaline autoinjectable seule","Sans anaphylaxie, ne traite pas l'urticaire.")],
 "Urticaire chronique spontanée (> 6 semaines) : antihistaminique H1 de 2e génération pris chaque jour, augmentable jusqu'à 4 fois la dose, puis omalizumab (DX.8).",
 "Une papule dure de 30 minutes à 24 heures ; au-delà, penser vasculite urticarienne.",
 B(8,13))

q("D","DX.9 vs DX.1 · sec ou humide","assessment_diagnosis","cabinet",
 "Une femme de 53 ans décrit des flushs brefs du visage et du thorax, sans aucune sueur, avec des selles liquides 5 fois par jour et un sifflement à l'effort. Ménopausée depuis 2 ans.",
 "Quel diagnostic faut-il évoquer en premier ?",
 [("Syndrome carcinoïde",""),
  ("Bouffées de la ménopause","Bouffée humide sans diarrhée."),
  ("Flush émotionnel","Diagnostic d'exclusion."),
  ("Rosacée","Ne donne ni diarrhée ni sifflements."),
  ("Flush lié à l'alcool","Pas de lien avec l'alcool rapporté.")],
 "Le flush carcinoïde est sec, bref, au visage et au thorax ; associé à une diarrhée et des sifflements, il impose le 5-HIAA (DX.9). Un flush avec sueurs profuses évoque plutôt la ménopause.",
 "Humide : ménopause, catécholamines, fièvre ; sec : carcinoïde, mastocytose, médicaments.",
 B(9,14))

q("D","DX.9 · première ligne","management","policlinique",
 "Un homme de 61 ans a un syndrome carcinoïde (TNE iléale G1, métastases hépatiques, récepteurs de la somatostatine positifs). Flushs et diarrhée quotidiens.",
 "Quel traitement est le plus approprié en première ligne ?",
 [("Analogue de la somatostatine",""),
  ("Évérolimus","Effet antisécrétoire faible ; tumeur progressive."),
  ("Lutécium-177 d'emblée","Réservé à la tumeur progressive avec récepteurs."),
  ("Télotristat seul","S'ajoute à l'analogue, ne le remplace pas."),
  ("Lopéramide seul, à dose maximale quotidienne","Symptomatique, ne contrôle pas la sécrétion.")],
 "Les analogues de la somatostatine sont la première ligne : octréotide LAR 20 mg i.m. toutes les 4 semaines ou lanréotide 60 à 120 mg tous les 28 jours (DX.9).",
 "Ils améliorent les symptômes chez jusqu'à 70 % des patients.",
 B(9,11))

q("D","DX.10 · biologie avant imagerie","assessment_diagnosis","hôpital",
 "Un scanner fait pour des douleurs lombaires découvre une masse surrénalienne gauche de 3 cm chez un homme de 58 ans hypertendu. Le radiologue propose une biopsie.",
 "Quelle est la prochaine étape la plus appropriée ?",
 [("Métanéphrines avant tout geste",""),
  ("Biopsie scanoguidée","Une biopsie peut déclencher une crise."),
  ("Surrénalectomie sans bilan","Le blocage alpha précède l'opération si phéochromocytome."),
  ("Scintigraphie MIBG d'emblée","La biochimie précède l'imagerie fonctionnelle."),
  ("Surveillance par scanner à 1 an","Sans avoir exclu une tumeur sécrétante.")],
 "Avant toute biopsie ou chirurgie d'une masse surrénalienne, on dose les métanéphrines : une biopsie peut déclencher une crise (DX.10).",
 "L'imagerie seule ne distingue pas le phéochromocytome d'un adénome.",
 B(10,14))

q("D","DX.10 · glucagon","management","urgences",
 "Un homme diabétique insulinotraité de 56 ans, avec phéochromocytome suspecté, est trouvé hypoglycémique (2,4 mmol/L), conscient, avec une voie veineuse.",
 "Quel traitement est le plus approprié ?",
 [("Glucose i.v.",""),
  ("Glucagon 1 mg i.m.","Contre-indiqué : libère des catécholamines."),
  ("Adrénaline s.c.","Sympathomimétique : risque de crise."),
  ("Attendre la glycémie de contrôle","L'hypoglycémie se corrige sans délai."),
  ("Octréotide s.c.","Hors sujet.")],
 "Chez un diabétique hypoglycémique avec phéochromocytome suspecté, on donne du glucose et on évite le glucagon, contre-indiqué par l'AIPS (crise hypertensive) (DX.10).",
 "Autres déclencheurs à éviter : sympathomimétiques, efforts de poussée, palpation profonde.",
 B(10,10))

q("D","DX.11 vs DX.8 · signe de Darier","assessment_diagnosis","cabinet",
 "Une femme de 39 ans a des flushs, du prurit et des macules brunâtres du tronc. Le frottement doux d'une macule fait apparaître une papule urticarienne en quelques minutes.",
 "Quel diagnostic ce signe évoque-t-il le plus ?",
 [("Mastocytose",""),
  ("Urticaire chronique inductible","Le dermographisme se teste en peau saine par un trait ferme."),
  ("Rosacée","Atteinte faciale persistante."),
  ("Syndrome carcinoïde","Pas de macules urticariennes."),
  ("Flush médicamenteux","Pas de lésion cutanée fixe.")],
 "Le signe de Darier (papule urticarienne en minutes après frottement d'une macule brunâtre) est spécifique de la mastocytose cutanée, peu sensible (DX.11, DX.8).",
 "Frotter peu pour éviter une réaction étendue.",
 PA("ssp-p6","§6 Examen physique"))

q("D","DX.11 · tryptase","assessment_diagnosis","policlinique",
 "Un homme de 47 ans a des flushs secs récurrents et une hépatosplénomégalie. Tryptase basale hors crise : 38 µg/L.",
 "Quel examen est le plus approprié ensuite ?",
 [("Biopsie de moelle osseuse",""),
  ("Métanéphrines plasmatiques libres","Pas d'hypertension paroxystique."),
  ("Calcitonine sérique","Pas de nodule thyroïdien."),
  ("Répéter la tryptase dans 2 ans","Retard diagnostique."),
  ("Test cutané aux pneumallergènes","Sans rapport.")],
 "Tryptase basale ≥ 20 µg/L : critère mineur de mastocytose ; on demande la biopsie de moelle, avec recherche de KIT D816V (DX.11).",
 "Tryptase basale normale < 11,4 µg/L.",
 B(11,10))

q("D","DX.12 · RET","management","policlinique",
 "Un homme de 42 ans a un carcinome médullaire de la thyroïde opéré. Il a deux enfants de 8 et 12 ans.",
 "Quelle mesure est la plus appropriée ?",
 [("Test RET du patient puis des apparentés",""),
  ("Test génétique seulement si antécédent familial","On le propose à tous les patients."),
  ("Calcitonine annuelle des enfants sans génétique","La génétique guide le dépistage."),
  ("Thyroïdectomie prophylactique sans test","Le test RET guide l'indication et la date."),
  ("Aucune mesure familiale","Forme héréditaire possible.")],
 "Test génétique RET à tous les patients atteints de carcinome médullaire, puis dépistage des apparentés du 1er degré (DX.12). Chez l'enfant, le risque de la mutation guide la date de la thyroïdectomie.",
 "Mutation germinale = forme héréditaire (NEM 2) ; somatique = sporadique.",
 B(12,13))

q("D","DX.12 · traitement curatif","management","hôpital",
 "Une femme de 45 ans a un carcinome médullaire de 1,8 cm avec adénopathie centrale, métanéphrines normales.",
 "Quel traitement est le plus approprié ?",
 [("Thyroïdectomie totale avec curage central",""),
  ("Iode radioactif après lobectomie","Les cellules C ne fixent pas l'iode."),
  ("Lobectomie seule","Insuffisante."),
  ("Sélpercatinib en première ligne","Réservé à la maladie avancée avec mutation RET."),
  ("Surveillance semestrielle de la calcitonine et de l'ACE","Le traitement curatif est chirurgical.")],
 "Le traitement curatif est la thyroïdectomie totale avec curage central, en centre spécialisé, après exclusion du phéochromocytome (DX.12).",
 "Suivi : calcémie, TSH, calcitonine et ACE.",
 B(12,13))

# ─── D · approfondissement (mécanismes) et spécialiste
q("D","DX.1 · mécanisme KNDy","mechanisms","cabinet",
 "Une femme de 53 ans sous fézolinétant pour des bouffées sévères demande comment agit ce médicament non hormonal.",
 "Quel mécanisme explique le mieux son effet ?",
 [("Blocage du récepteur NK3 hypothalamique",""),
  ("Agonisme des récepteurs aux œstrogènes","Ce n'est pas une hormone."),
  ("Inhibition de la recapture de la sérotonine","Mécanisme des ISRS, hors AIPS pour les bouffées."),
  ("Agonisme alpha-2 central","Mécanisme de la clonidine."),
  ("Inhibition de la COX","Mécanisme de l'aspirine.")],
 "Les œstrogènes freinent les neurones KNDy (kisspeptine, neurokinine B, dynorphine) de l'hypothalamus ; à la ménopause, ce frein disparaît et la zone thermoneutre se rétrécit. Le fézolinétant bloque le récepteur NK3 de la neurokinine B (DX.1).",
 "Contre-indiqué avec un inhibiteur du CYP1A2 comme la fluvoxamine.",
 B(1,3), niv="approfondissement")

q("D","DX.1 · CYP1A2","management","cabinet",
 "Une femme de 55 ans souhaite le fézolinétant pour des bouffées modérées. Elle prend de la fluvoxamine pour un trouble obsessionnel. Bilan hépatique et DFGe normaux.",
 "Quelle conduite est la plus appropriée ?",
 [("Ne pas prescrire le fézolinétant",""),
  ("Fézolinétant 45 mg, dose habituelle","Interaction contre-indiquée."),
  ("Fézolinétant 90 mg par jour","Maximum 45 mg."),
  ("Fézolinétant un jour sur deux","Pas d'adaptation prévue : contre-indication."),
  ("Fézolinétant après dosage de la FSH","La FSH n'a pas de rôle ici.")],
 "Le fézolinétant est contre-indiqué avec un inhibiteur du CYP1A2 comme la fluvoxamine (AIPS VEOZA™) (DX.1). On discute un THM ou une autre option.",
 "Autres contre-indications : Child-Pugh B ou C, DFGe < 30 mL/min/1,73 m².",
 B(1,13), niv="approfondissement")

q("D","DX.2 · dermocorticoïde","assessment_diagnosis","cabinet",
 "Une femme de 40 ans applique depuis 4 mois un dermocorticoïde puissant sur une rougeur du visage. La rougeur s'aggrave, avec papules et télangiectasies.",
 "Quelle conduite est la plus appropriée ?",
 [("Sevrage progressif du dermocorticoïde",""),
  ("Augmenter la puissance du dermocorticoïde","Entretient la dermatose rosacéiforme."),
  ("Arrêt brutal et isotrétinoïne","La rosacée n'est pas une indication AIPS de l'isotrétinoïne."),
  ("Ajouter la brimonidine et poursuivre","Le dermocorticoïde est la cause."),
  ("Biopsie cutanée immédiate","Diagnostic clinique.")],
 "Un dermocorticoïde sur le visage provoque une dermatose rosacéiforme, à sevrer progressivement ; elle est un critère d'exclusion de la rosacée (DX.2).",
 "Les télangiectasies peuvent aussi être produites par la corticothérapie locale.",
 B(2,14), niv="approfondissement")

q("D","DX.3 · propranolol et asthme","management","cabinet",
 "Un homme de 34 ans asthmatique demande du propranolol pour son trac avec rougeur et tachycardie avant ses concerts.",
 "Quelle réponse est la plus appropriée ?",
 [("Propranolol contre-indiqué : asthme",""),
  ("Propranolol 40 mg avant chaque concert","Contre-indiqué par l'AIPS en cas d'asthme."),
  ("Propranolol avec salbutamol en prévention","L'association ne lève pas la contre-indication."),
  ("Propranolol à demi-dose","La contre-indication ne dépend pas de la dose."),
  ("Propranolol en patch","Pas de forme cutanée ; même contre-indication.")],
 "L'AIPS d'Inderal® contre-indique le propranolol en cas d'asthme ou de bronchospasme (DX.3). On privilégie la TCC.",
 "Autres contre-indications : bradycardie, BAV 2–3, phéochromocytome non traité.",
 B(3,14), niv="approfondissement")

q("D","DX.4 · TSH-R-Ab","assessment_diagnosis","policlinique",
 "Une femme de 33 ans a une TSH supprimée et une fT4 élevée. Elle a une exophtalmie et un goitre diffus.",
 "Quel examen confirme le plus directement la cause ?",
 [("Anticorps anti-récepteur de la TSH",""),
  ("Calcitonine sérique","Cible les cellules C."),
  ("Thyroglobuline","Marqueur de suivi des cancers différenciés."),
  ("Cytoponction échoguidée du goitre diffus","Sans nodule suspect."),
  ("TDM cervicale injectée","L'iode peut aggraver la thyrotoxicose.")],
 "Thyrotoxicose confirmée avec TSH-R-Ab positifs, thyroïde hypervascularisée et orbitopathie : diagnostic direct de maladie de Basedow (ETA 2018) (DX.4). Thionamide en première intention, 12 à 18 mois.",
 "Un goitre diffus évoque Basedow ; un nodule dur évoque le carcinome médullaire.",
 B(4,8), niv="approfondissement")

q("D","DX.4 · propranolol masque","mechanisms","cabinet",
 "Un homme de 40 ans en thyrotoxicose reçoit du propranolol. Ses palpitations et son tremblement disparaissent ; il veut arrêter le reste du bilan.",
 "Quelle explication est la plus appropriée ?",
 [("Le propranolol soulage sans traiter la cause",""),
  ("Le propranolol normalise la fT4","Il n'agit pas sur la sécrétion."),
  ("Le propranolol guérit la maladie de Basedow","Effet symptomatique seulement."),
  ("Le propranolol remplace le thyréostatique à long terme","Il s'ajoute au thyréostatique."),
  ("Le propranolol bloque les TSH-R-Ab","Aucune action immunologique.")],
 "L'Inderal® soulage seulement les symptômes adrénergiques ; il ne traite pas la cause et peut masquer la thyrotoxicose (AIPS) (DX.4).",
 "Excès d'hormones thyroïdiennes = chaleur produite, puis vasodilatation de dissipation.",
 B(4,14), niv="approfondissement")

q("D","DX.5 · acétaldéhyde","mechanisms","cabinet",
 "Un étudiant de 22 ans demande pourquoi il devient rouge après un seul verre de bière alors que ses amis non.",
 "Quel mécanisme explique le mieux ce flush ?",
 [("Accumulation d'acétaldéhyde vasodilatateur",""),
  ("Libération de sérotonine tumorale","Mécanisme carcinoïde."),
  ("Dégranulation mastocytaire clonale","Mécanisme de la mastocytose."),
  ("Excès de catécholamines","Mécanisme du phéochromocytome."),
  ("Libération de prostaglandine D2 par la niacine","Mécanisme médicamenteux.")],
 "L'alcool est oxydé en acétaldéhyde, dégradé par l'ALDH2 ; un déficit en ALDH2 fait s'accumuler l'acétaldéhyde, vasodilatateur (DX.5). Le disulfirame reproduit ce blocage.",
 "Flush dans les minutes après l'alcool : déficit en ALDH2 ou interaction médicamenteuse.",
 B(5,13), niv="approfondissement")

q("D","DX.5 · risque œsophagien","management","cabinet",
 "Un homme de 30 ans d'origine coréenne, avec déficit en ALDH2 probable, boit 3 bières par soir « pour s'habituer » au flush.",
 "Quel conseil est le plus approprié ?",
 [("Abstinence : risque de cancer de l'œsophage",""),
  ("Continuer pour induire une tolérance","Le risque de cancer augmente."),
  ("Antihistaminique H1 pris une heure avant de boire","Masque le flush sans réduire le risque."),
  ("Disulfirame pour réduire le flush","Le disulfirame provoque le flush."),
  ("Aucune mesure : flush bénin","Le flush signale un risque de cancer.")],
 "Le déficit en ALDH2 expose au cancer de l'œsophage : on conseille l'abstinence (Brooks 2009) (DX.5). Le flush à l'alcool n'est pas toujours bénin.",
 "Antihistaminique avant l'alcool : masque l'alarme, ne protège pas.",
 B(5,14), niv="approfondissement")

q("D","DX.6 · niacine et PGD2","mechanisms","cabinet",
 "Un homme de 59 ans qui prend de la niacine pour une dyslipidémie a un flush 30 minutes après chaque dose.",
 "Quel mécanisme explique le mieux ce flush ?",
 [("PGD2 sur le récepteur DP1 cutané",""),
  ("Accumulation d'acétaldéhyde","Mécanisme du flush à l'alcool."),
  ("Libération d'histamine dépendante du débit","Mécanisme du red man à la vancomycine."),
  ("Blocage des canaux calciques","Mécanisme de l'amlodipine."),
  ("Sérotonine d'origine tumorale","Mécanisme carcinoïde.")],
 "La niacine libère la prostaglandine D2, qui active le récepteur DP1 des vaisseaux cutanés (DX.6). L'aspirine prise avant la dose en réduit l'effet en bloquant la COX.",
 "L'usage préventif de l'aspirine est hors AIPS (recommandation internationale).",
 B(6,13), niv="approfondissement")

q("D","DX.6 · red man non allergique","mechanisms","hôpital",
 "Une infirmière demande si un patient ayant eu un « red man » sous vancomycine doit être étiqueté allergique.",
 "Quelle réponse est la plus appropriée ?",
 [("Non : histamine liée au débit",""),
  ("Oui : allergie IgE vraie","Ce n'est pas une allergie vraie."),
  ("Oui : contre-indication définitive","Reprise possible à débit lent."),
  ("Non : réaction à l'excipient","Le mécanisme est la libération d'histamine."),
  ("Oui : désensibilisation obligatoire","Inutile.")],
 "Le red man est une libération d'histamine dépendante du débit, qui régresse à l'arrêt : ce n'est pas une allergie vraie (DX.6). Débit maximal 10 mg/min, au moins 60 minutes.",
 "Urticaire, stridor ou hypotension changent la donne : arrêt et adrénaline i.m.",
 B(6,14), niv="approfondissement")

q("D","DX.8 · tryptase normale","assessment_diagnosis","urgences",
 "Une femme de 41 ans a eu une urticaire généralisée avec bronchospasme et hypotension après une crevette, corrigés par l'adrénaline. La tryptase prélevée à 1 heure est à 9 µg/L.",
 "Quelle conclusion est la plus appropriée ?",
 [("L'anaphylaxie reste le diagnostic",""),
  ("Anaphylaxie exclue par la tryptase","La tryptase normale n'exclut pas l'anaphylaxie."),
  ("Réaction vagale","Urticaire et bronchospasme : non."),
  ("Flush émotionnel","Diagnostic d'exclusion."),
  ("Asthme isolé","N'explique pas l'urticaire ni l'hypotension.")],
 "L'anaphylaxie est un diagnostic clinique ; une tryptase normale ne l'exclut pas : 36 à 40 % des patients restent sous 11,4 µg/L (DX.8). On dose aussi la tryptase basale après 24 heures.",
 "36 à 40 % des anaphylaxies ont une tryptase normale.",
 B(8,14), niv="approfondissement")

q("D","DX.8 · angio-œdème sous IEC","mechanisms","urgences",
 "Un homme de 66 ans sous lisinopril a un gonflement de la lèvre et de la langue, sans urticaire ni prurit. Il respire bien, SpO2 97 %, PA 148/88 mmHg.",
 "Quel mécanisme explique le mieux ce tableau ?",
 [("Bradykinine",""),
  ("Histamine mastocytaire","L'antihistaminique serait efficace ; ici il ne l'est pas."),
  ("Acétaldéhyde","Mécanisme du flush à l'alcool."),
  ("Sérotonine","Mécanisme carcinoïde."),
  ("Catécholamines","Mécanisme du phéochromocytome.")],
 "Un angio-œdème sans papules ni prurit sous IEC est médié par la bradykinine : l'antihistaminique n'agit pas, l'adrénaline peu (DX.8). En cas de doute avec une anaphylaxie ou d'obstruction, on injecte l'adrénaline et on sécurise les voies aériennes.",
 "Bilan : C4 et C1-INH si histoire familiale.",
 B(8,14), niv="approfondissement")

q("D","DX.9 · métastases hépatiques","mechanisms","policlinique",
 "Un étudiant demande pourquoi une tumeur neuroendocrine de l'iléon sans métastase ne donne habituellement pas de flush.",
 "Quel mécanisme explique le mieux cette observation ?",
 [("Le foie inactive les médiateurs portaux",""),
  ("La tumeur iléale ne sécrète pas de sérotonine","Elle sécrète, mais le foie inactive."),
  ("Le rein élimine toute la sérotonine","Le premier filtre est hépatique."),
  ("Les plaquettes détruisent la sérotonine","Elles la stockent, elles ne la détruisent pas."),
  ("Le poumon capte toute la bradykinine","Le foie est le filtre principal.")],
 "Les médiateurs libérés dans la veine porte sont inactivés par le foie ; le syndrome carcinoïde n'apparaît que lorsqu'ils y échappent, le plus souvent par des métastases hépatiques (DX.9).",
 "Les médiateurs : tachykinines, kinines et sérotonine.",
 B(9,13), niv="approfondissement")

q("D","DX.9 · chromogranine A","assessment_diagnosis","policlinique",
 "Un homme de 64 ans a une TNE pancréatique non fonctionnelle. Sa chromogranine A est élevée. Il n'a ni flush ni diarrhée.",
 "Quelle conclusion est la plus appropriée ?",
 [("Pas de syndrome carcinoïde",""),
  ("Syndrome carcinoïde confirmé","La chromogranine A ne distingue pas les patients avec ou sans syndrome."),
  ("Phéochromocytome associé","Aucun argument."),
  ("Mastocytose associée","Aucun argument."),
  ("Carcinome médullaire associé","Aucun argument.")],
 "Le syndrome carcinoïde associe un symptôme (diarrhée chronique ou flush) et une sérotonine ou un 5-HIAA élevé (ENETS 2022). La chromogranine A, marqueur général des TNE, ne pose pas le syndrome (DX.9).",
 "Ni le symptôme seul, ni le 5-HIAA seul, ni l'imagerie seule ne suffisent.",
 B(9,8), niv="approfondissement")

q("D","DX.10 · faux positif","assessment_diagnosis","policlinique",
 "Un homme de 50 ans a des métanéphrines plasmatiques libres légèrement au-dessus de la norme, prélevées assis, après un café, sans crise ni hypertension.",
 "Quelle est la prochaine étape la plus appropriée ?",
 [("Refaire le dosage, couché 30 min, à jeun",""),
  ("TDM des surrénales avec injection d'emblée","Un résultat limite impose d'abord de contrôler les interférences."),
  ("Alpha-blocage et chirurgie","Diagnostic non établi."),
  ("Scintigraphie à la MIBG","Réservée aux métastases suspectées."),
  ("Conclure au phéochromocytome","Faux positif possible.")],
 "Métanéphrines légèrement élevées : possible faux positif (médicament, stress, prélèvement) ; on refait le dosage dans de bonnes conditions, couché 30 minutes, à jeun depuis la veille (DX.10).",
 "Spécificité 89 % : les faux positifs existent.",
 B(10,9), niv="approfondissement")

q("D","DX.10 · régime salé","mechanisms","hôpital",
 "Une femme de 45 ans est préparée à une surrénalectomie pour phéochromocytome. On lui prescrit un alphabloquant et un régime riche en sodium.",
 "Quel est le but principal du régime salé ?",
 [("Prévenir l'hypotension postopératoire",""),
  ("Prévenir l'hypokaliémie liée à l'alpha-blocage","Ce n'est pas le but."),
  ("Réduire la sécrétion tumorale","Aucun effet sur la tumeur."),
  ("Prévenir l'hypoglycémie","Sans rapport."),
  ("Améliorer la cicatrisation","Sans rapport.")],
 "La vasoconstriction chronique réduit le volume plasmatique ; le régime salé et les apports hydriques préviennent l'hypotension après l'exérèse (DX.10).",
 "Après l'exérèse : remplissage abondant, surveillance glycémique 48 h (hypoglycémie possible).",
 B(10,14), niv="approfondissement")

q("D","DX.11 · critères OMS","assessment_diagnosis","hôpital",
 "La biopsie de moelle d'un homme de 50 ans montre des agrégats multifocaux denses de plus de 15 mastocytes. La mutation KIT D816V est présente.",
 "Quelle conclusion est la plus appropriée ?",
 [("Mastocytose systémique confirmée",""),
  ("Il faut trois critères mineurs en plus","Un majeur et un mineur suffisent."),
  ("Diagnostic exclu sans lésion cutanée","La peau n'est pas nécessaire."),
  ("Une tryptase ≥ 20 µg/L est obligatoire","Ce n'est qu'un critère mineur parmi d'autres."),
  ("Leucémie à mastocytes d'emblée","Classification selon l'OMS ensuite.")],
 "Critère majeur (agrégats ≥ 15 mastocytes) plus un critère mineur (KIT D816V) : diagnostic de mastocytose systémique (OMS 2022) (DX.11). Trois critères mineurs suffisent aussi.",
 "Mineurs : > 25 % mastocytes atypiques, KIT D816V, CD25/CD2/CD30, tryptase ≥ 20.",
 B(11,8), niv="approfondissement")

q("D","DX.11 · tryptase sous 20","assessment_diagnosis","policlinique",
 "Une femme de 49 ans a fait une anaphylaxie sévère au venin d'abeille, sans urticaire. Tryptase basale : 9 µg/L. Aucune lésion cutanée.",
 "Quelle est la prochaine étape la plus appropriée ?",
 [("KIT D816V dans le sang",""),
  ("Mastocytose exclue","Une tryptase < 20 µg/L ne l'exclut pas."),
  ("Biopsie cutanée","Pas de lésion cutanée."),
  ("5-HIAA urinaire","Sans argument carcinoïde."),
  ("Aucun bilan, trousse seule","Le bilan clonal est indiqué.")],
 "Après une anaphylaxie au venin, même avec une tryptase sous 11,5 µg/L, on cherche KIT D816V dans le sang (DX.11) : 13 patients sur 48 avaient une tryptase ≤ 20 sans lésion cutanée.",
 "KIT D816V sanguin négatif n'exclut pas : la moelle reste obligatoire si la suspicion est forte.",
 B(11,14), niv="approfondissement")

q("D","DX.12 · calcitonine faussement élevée","assessment_diagnosis","cabinet",
 "Une femme de 68 ans sous IPP au long cours, DFGe 35 mL/min/1,73 m², a une calcitonine légèrement élevée découverte lors d'un bilan. Pas de nodule palpable.",
 "Quelle conduite est la plus appropriée ?",
 [("Refaire et chercher une cause non tumorale",""),
  ("Thyroïdectomie totale","Une élévation légère isolée ne suffit pas."),
  ("Sélpercatinib","Réservé à la maladie avancée confirmée."),
  ("Iode radioactif","Les cellules C ne fixent pas l'iode."),
  ("Conclure au carcinome médullaire et adresser au chirurgien","L'insuffisance rénale et les IPP élèvent la calcitonine.")],
 "Une calcitonine légèrement élevée seule ne suffit pas : l'insuffisance rénale, les IPP et d'autres TNE peuvent l'élever (DX.12). On la refait et on cherche une cause non tumorale.",
 "Calcitonine > 100 ng/L : carcinome médullaire probable.",
 B(12,8), niv="approfondissement")

q("D","DX.12 · lévothyroxine","management","policlinique",
 "Après thyroïdectomie totale pour carcinome médullaire, un homme de 44 ans reçoit de la lévothyroxine. L'interne propose une dose suppressive.",
 "Quelle cible est la plus appropriée ?",
 [("TSH normale",""),
  ("TSH supprimée","Les cellules C ne dépendent pas de la TSH."),
  ("TSH > 10 mUI/L","Hypothyroïdie inutile."),
  ("fT4 au double de la norme","Thyrotoxicose iatrogène."),
  ("Aucune substitution","Substitution à vie après thyroïdectomie totale.")],
 "Après thyroïdectomie pour carcinome médullaire, la substitution vise une TSH normale : les cellules C ne dépendent pas de la TSH (ATA 2015, hors AIPS) (DX.12).",
 "La fourchette AIPS 150–300 µg vise la suppression des cancers différenciés.",
 B(12,14), niv="approfondissement")

q("D","DX.7 · consigne hypothalamique","mechanisms","cabinet",
 "Une étudiante demande pourquoi la rougeur et la chaleur apparaissent quand la fièvre « tombe ».",
 "Quel mécanisme explique le mieux ce flush ?",
 [("Vasodilatation pour dissiper la chaleur",""),
  ("Libération d'histamine par les mastocytes cutanés","Mécanisme allergique."),
  ("Excès de catécholamines","Mécanisme adrénergique."),
  ("Accumulation d'acétaldéhyde","Mécanisme alcoolique."),
  ("Sécrétion de calcitonine","Mécanisme du carcinome médullaire.")],
 "Pyrogènes et PGE2 relèvent la consigne hypothalamique (frissons) ; quand elle redescend, la vasodilatation cutanée dissipe la chaleur, d'où flush et sueurs (DX.7).",
 "Un antipyrétique agit sur la consigne ; il n'agit pas sur l'hyperthermie.",
 PA("ssp-p7","§7 Approche syndromique"), niv="approfondissement")

# ═════════════ BLOC P · PIÈGES & ALARMES
q("P","DX.8 · attendre la tryptase","management","urgences",
 "Une femme de 22 ans a une urticaire, un œdème de la langue et une PA à 82/50 mmHg après un antibiotique. L'interne veut prélever la tryptase avant d'injecter.",
 "Quelle est la conduite la plus appropriée ?",
 [("Adrénaline i.m. immédiate, tryptase ensuite",""),
  ("Tryptase, puis adrénaline selon le résultat","Le résultat ne doit jamais retarder l'adrénaline."),
  ("Antihistaminique d'abord, adrénaline si échec","L'adrénaline est la première ligne."),
  ("Corticoïde i.v. et observation","Seconde ligne."),
  ("Test de provocation","Dangereux et hors sujet.")],
 "La tryptase se prélève dans les heures suivantes (15 minutes à 3 heures) ; elle ne retarde jamais l'adrénaline (DX.8).",
 "Œdème de la langue ou de la gorge : l'obstruction laryngée tue en minutes.",
 PA("ssp-p14","§14 Pièges"))

q("P","DX.10 · bêtabloquant seul","management","cabinet",
 "Un homme de 39 ans a des crises de palpitations, sueurs et céphalées avec PA à 200/110 mmHg pendant les crises. Les métanéphrines sont en cours.",
 "Quel médicament est contre-indiqué en monothérapie ?",
 [("Propranolol",""),
  ("Urapidil","Alphabloquant : possible en crise."),
  ("Doxazosine","Alphabloquant : utilisé en préparation (hors AIPS)."),
  ("Nitroprussiate","Vasodilatateur de crise."),
  ("Soluté salé isotonique","Sans danger.")],
 "Le bêtabloquant seul laisse l'effet alpha sans opposition et peut provoquer une crise hypertensive (DX.10). L'alpha-blocage vient toujours d'abord.",
 "AIPS du propranolol : phéochromocytome « seulement en association avec un alphabloquant ».",
 B(10,14), pol="negative")

q("P","DX.1 · FSH piège","assessment_diagnosis","cabinet",
 "Une femme de 50 ans a des bouffées typiques. Sa FSH, dosée par un autre médecin, est normale. TSH normale, examen normal.",
 "Quelle conclusion est la plus appropriée ?",
 [("Bouffées de la ménopause probables",""),
  ("Ménopause exclue par la FSH normale","La FSH varie d'un jour à l'autre en périménopause."),
  ("Phéochromocytome à rechercher","Aucune triade."),
  ("Carcinoïde à rechercher","Bouffées humides, pas de diarrhée."),
  ("Répéter la FSH chaque semaine","Inutile : diagnostic clinique.")],
 "La FSH varie d'un jour à l'autre en périménopause : une valeur isolée ne pose ni n'exclut le diagnostic, qui est clinique (DX.1).",
 "Ne pas doser les hormones chez une femme de plus de 45 ans avec bouffées humides.",
 B(1,8), niv="approfondissement")

q("P","DX.9 · banane et noix","assessment_diagnosis","cabinet",
 "Un homme de 60 ans doit recueillir ses urines de 24 heures pour un 5-HIAA. Il mange chaque jour des bananes et des noix.",
 "Quelle consigne est la plus appropriée ?",
 [("Régime sans sérotonine 72 h avant",""),
  ("Aucune consigne alimentaire","La sérotonine alimentaire fausse le dosage."),
  ("Jeûne complet de 24 heures","Inutile."),
  ("Arrêt des bananes seulement le jour même","Préparation de 72 heures."),
  ("Doubler les noix pour stimuler la sécrétion","Faux positif garanti.")],
 "Le 5-HIAA urinaire des 24 heures exige un régime de 72 heures sans aliments riches en sérotonine (banane, noix), et si possible deux collectes (DX.9).",
 "Seuil ENETS : > 50 µmol/24 h compatible avec le syndrome.",
 B(9,14))

q("P","DX.5 · disulfirame contre le flush","management","cabinet",
 "Un homme de 36 ans avec flush à l'alcool demande un médicament pour « bloquer » le flush.",
 "Quel médicament est contre-indiqué dans ce but ?",
 [("Disulfirame",""),
  ("Paracétamol","Sans lien, sans danger particulier."),
  ("Cétirizine","Sans effet sur le risque, mais pas contre-indiquée."),
  ("Oméprazole","Sans lien."),
  ("Vitamine B1","Sans lien.")],
 "Le disulfirame inhibe l'aldéhyde-déshydrogénase et provoque le flush : il sert au sevrage, jamais au traitement du flush (DX.5). Le traitement du flush à l'alcool est d'éviter l'alcool.",
 "Antabus® : sevrage préalable d'environ 3 jours ; toute prise d'alcool provoque un flush.",
 PA("ssp-p11","§11 Prise en charge"), pol="negative")

q("P","DX.12 · iode radioactif","management","policlinique",
 "Après thyroïdectomie pour carcinome médullaire, la calcitonine reste élevée. Un médecin propose de l'iode radioactif.",
 "Quel est l'argument le plus juste ?",
 [("Les cellules C ne fixent pas l'iode",""),
  ("L'iode est réservé aux femmes","Argument faux."),
  ("L'iode est efficace après un curage ganglionnaire central","Inefficace dans ce cancer."),
  ("L'iode remplace la chirurgie","Faux."),
  ("L'iode guérit la forme héréditaire","Faux.")],
 "L'iode radioactif ne traite pas le carcinome médullaire : les cellules C ne fixent pas l'iode, contrairement aux cellules folliculaires (DX.12).",
 "Maladie avancée avec mutation RET : sélpercatinib ou vandétanib.",
 B(12,14), niv="approfondissement")

q("P","DX.1 · tibolone","management","cabinet",
 "Une femme de 57 ans traitée pour un cancer du sein il y a 5 ans demande la tibolone pour des bouffées sévères.",
 "Quelle réponse est la plus appropriée ?",
 [("Non : récidive accrue",""),
  ("Oui, sans progestatif","Contre-indiquée après cancer du sein."),
  ("Oui, à demi-dose","La contre-indication ne dépend pas de la dose."),
  ("Oui, si la FSH est élevée","Sans rapport."),
  ("Oui, après 5 ans de rémission","Le risque persiste.")],
 "La tibolone (Livial®) est contre-indiquée après cancer du sein : récidive accrue (HR 1,40, IC 1,14–1,70, étude LIBERATE) (DX.1).",
 "Livial® : au plus tôt 12 mois après les dernières règles, sans progestatif.",
 B(1,11), niv="specialiste", spe="Gynécologie")

q("P","DX.2 · doxycycline 40 mg","mechanisms","cabinet",
 "Une femme de 50 ans avec rosacée papulopustuleuse reçoit de la doxycycline 40 mg à libération modifiée. Elle craint une résistance bactérienne.",
 "Quelle explication est la plus appropriée ?",
 [("Dose anti-inflammatoire, sous le seuil antimicrobien",""),
  ("Dose antibiotique pleine","40 mg est sous le seuil antimicrobien."),
  ("Action antiparasitaire sur les acariens Demodex de la peau","C'est le mécanisme de l'ivermectine."),
  ("Agonisme alpha-2 vasoconstricteur","Mécanisme de la brimonidine."),
  ("Action rétinoïde","Mécanisme de l'isotrétinoïne.")],
 "Oracea® 40 mg agit par effet anti-inflammatoire et non antibiotique : la dose est inférieure au seuil antimicrobien (DX.2). Contre-indiqué aux 2e et 3e trimestres de grossesse.",
 "Oracea® : sinon seulement en cas de nécessité absolue pendant la grossesse.",
 B(2,14), niv="specialiste", spe="Dermatologie")

q("P","DX.3 · escitalopram","management","cabinet",
 "Un homme de 32 ans a un trouble panique avec bouffées de chaleur, après bilan somatique normal. Vous débutez l'escitalopram en plus de la TCC.",
 "Quelle posologie de départ est la plus appropriée ?",
 [("5 mg la 1re semaine, puis 10 mg",""),
  ("20 mg dès le premier jour","Démarrer bas : risque d'aggravation initiale."),
  ("40 mg par jour","Dépasse le maximum de 20 mg."),
  ("10 mg un jour sur deux","Schéma non prévu."),
  ("Lorazépam à la place, au long cours","Les benzodiazépines ne se prescrivent pas en fond.")],
 "Dans le trouble panique, Cipralex® débute à 5 mg par jour la première semaine, puis 10 mg ; maximum 20 mg par jour (DX.3). Arrêt progressif sur 1 à 2 semaines au moins.",
 "Ne jamais arrêter brutalement un ISRS.",
 B(3,13), niv="specialiste", spe="Psychiatrie")

q("P","DX.4 · iode et orbitopathie","management","policlinique",
 "Une femme de 45 ans a une maladie de Basedow avec orbitopathie active modérée, après rechute sous thionamide. On discute le traitement définitif.",
 "Quelle option est contre-indiquée ?",
 [("Iode radioactif",""),
  ("Thyroïdectomie totale","Option définitive possible."),
  ("Reprise du thionamide","Option possible."),
  ("Avis ophtalmologique spécialisé","Recommandé."),
  ("Arrêt du tabac","Recommandé.")],
 "L'iode radioactif est contre-indiqué en cas d'orbitopathie active ou sévère (ETA 2018) (DX.4).",
 "Thionamide 12 à 18 mois dans la maladie de Basedow.",
 B(4,14), pol="negative", niv="specialiste", spe="Endocrinologie")

q("P","DX.5 · douleur à l'alcool","assessment_diagnosis","cabinet",
 "Un homme de 28 ans décrit une douleur dans les ganglions du cou après chaque verre d'alcool, sans flush. Il a des adénopathies cervicales de 2 cm.",
 "Quelle est la conduite la plus appropriée ?",
 [("Imagerie et avis hématologique",""),
  ("Test génétique ALDH2","Il s'agit d'une douleur, pas d'un flush."),
  ("Rassurer : intolérance à l'alcool","Risque de méconnaître un lymphome."),
  ("Antihistaminique avant l'alcool","Sans rapport."),
  ("Disulfirame","Sans rapport.")],
 "Une douleur déclenchée par l'alcool avec adénopathies oriente vers un lymphome de Hodgkin ; ce n'est pas un flush (DX.5). Imagerie et avis hématologique.",
 "Toute douleur provoquée par l'alcool avec adénopathie impose une imagerie.",
 B(5,10), niv="specialiste", spe="Hématologie")

q("P","DX.6 · tamoxifène et paroxétine","management","policlinique",
 "Une femme de 47 ans sous tamoxifène adjuvant a des bouffées gênantes. Son médecin propose la paroxétine.",
 "Quelle réponse est la plus appropriée ?",
 [("Éviter : baisse de l'endoxifène",""),
  ("Paroxétine 20 mg le matin, sans réserve","Interaction CYP2D6."),
  ("Arrêter le tamoxifène","Avis oncologique avant toute modification."),
  ("Ajouter un estradiol","Contre-indiqué dans un cancer hormonosensible."),
  ("Doubler le tamoxifène","Sans fondement.")],
 "La paroxétine inhibe le CYP2D6, abaisse l'endoxifène et réduit l'efficacité du tamoxifène (AIPS) (DX.6). Les bouffées sous tamoxifène touchent 37,8 % des patientes.",
 "Flush de type ménopausique sous tamoxifène : rassurer et demander l'avis oncologique.",
 B(6,14), niv="specialiste", spe="Oncologie")

q("P","DX.7 · métamizole","management","hôpital",
 "Un homme de 70 ans fébrile reçoit du métamizole depuis 10 jours. Il a une nouvelle angine et une fièvre persistante.",
 "Quel examen est le plus approprié en urgence ?",
 [("Formule sanguine",""),
  ("Radiographie du thorax seule","Ne cherche pas l'agranulocytose."),
  ("Hémocultures seules, métamizole poursuivi","Le médicament doit être suspecté."),
  ("CRP seule","Ne montre pas les neutrophiles."),
  ("Échocardiographie","Pas d'argument endocarditique.")],
 "Le métamizole expose à une agranulocytose idiosyncrasique, possible à tout moment ; la fièvre en masque les signes (DX.7). Formule sanguine en urgence et arrêt du médicament.",
 "Métamizole = dernier recours antipyrétique.",
 B(7,13), niv="specialiste", spe="Médecine interne")

q("P","DX.9 · vésicule","management","policlinique",
 "Un homme de 62 ans va débuter un analogue de la somatostatine pour un syndrome carcinoïde.",
 "Quel examen faut-il avant le début ?",
 [("Échographie de la vésicule biliaire",""),
  ("Scintigraphie à l'iode 131","Sans rapport."),
  ("Spirométrie","Sans rapport."),
  ("Densitométrie osseuse de la hanche et du rachis","Sans rapport."),
  ("EEG","Sans rapport.")],
 "Les analogues de la somatostatine favorisent la lithiase biliaire : échographie de la vésicule avant, puis tous les 6 à 12 mois (AIPS) (DX.9).",
 "Aussi : allongement du QT, stéatorrhée (enzymes pancréatiques).",
 B(9,14), niv="specialiste", spe="Oncologie")

q("P","DX.10 · génétique","management","policlinique",
 "Un homme de 34 ans est opéré d'un phéochromocytome sporadique apparent, sans antécédent familial.",
 "Quelle mesure est la plus appropriée ?",
 [("Test génétique proposé",""),
  ("Aucun test sans antécédent familial","Tous les patients reçoivent un test."),
  ("Test seulement en cas de récidive","Trop tard pour le dépistage familial."),
  ("Surveillance de 1 an puis arrêt","Suivi à long terme."),
  ("Scanner annuel des apparentés","Sans génétique préalable.")],
 "Tous les patients avec phéochromocytome reçoivent un test génétique ; SDHx si paragangliome, SDHB si métastases (DX.10). Suivi à vie si risque élevé.",
 "Facteurs de risque de récidive : jeune âge, paragangliome, mutation, tumeur ≥ 5 cm.",
 B(10,14), niv="specialiste", spe="Endocrinologie")

q("P","DX.11 · avapritinib indolent","management","hôpital",
 "Une femme de 51 ans a une mastocytose systémique indolente avec symptômes sévères non contrôlés malgré antihistaminiques. Plaquettes 210 G/L.",
 "Quelle posologie d'avapritinib est la plus appropriée ?",
 [("25 mg par jour, à jeun",""),
  ("200 mg par jour","Dose de la forme avancée."),
  ("300 mg par jour","Dose du GIST."),
  ("100 mg deux fois par jour","Posologie de la midostaurine."),
  ("25 mg deux fois par jour","Dépasse le maximum de la forme indolente.")],
 "Forme indolente symptomatique malgré le traitement : avapritinib (Ayvakyt®) 25 mg par voie orale à jeun, une fois par jour, dose maximale (AIPS) (DX.11).",
 "Avapritinib déconseillé si plaquettes < 50 G/L.",
 B(11,14), niv="specialiste", spe="Hématologie")

q("P","DX.11 · midostaurine","management","hôpital",
 "Un homme de 66 ans a une mastocytose systémique agressive avec cytopénies. L'hématologue choisit la midostaurine.",
 "Quelle posologie est la plus appropriée ?",
 [("100 mg deux fois par jour",""),
  ("25 mg une fois par jour","Posologie de l'avapritinib indolent."),
  ("50 mg deux fois par jour","Posologie de la leucémie aiguë myéloïde."),
  ("200 mg une fois par jour","Posologie de l'avapritinib avancé."),
  ("300 mg une fois par jour, à jeun le matin","Sans fondement.")],
 "Mastocytose avancée : midostaurine (Rydapt®) 100 mg deux fois par jour (AIPS) ; interrompre si neutrophiles < 1,0 G/L (DX.11).",
 "Formes avancées : agressive, avec néoplasie hématologique associée, leucémie à mastocytes.",
 B(11,14), niv="specialiste", spe="Hématologie")

q("P","DX.12 · sélpercatinib","management","hôpital",
 "Un homme de 58 ans, 72 kg, a un carcinome médullaire métastatique progressif avec mutation RET.",
 "Quelle posologie de sélpercatinib est la plus appropriée ?",
 [("160 mg deux fois par jour",""),
  ("120 mg deux fois par jour","Dose sous 50 kg."),
  ("300 mg une fois par jour","Posologie du vandétanib."),
  ("25 mg une fois par jour","Sans fondement."),
  ("160 mg une fois par semaine","Schéma faux.")],
 "Sélpercatinib (Retsevmo®) : 160 mg deux fois par jour dès 50 kg, 120 mg en dessous (AIPS) (DX.12). LIBRETTO-531 : survie sans progression prolongée (HR 0,28).",
 "Vandétanib : 300 mg/j, ECG (QT) à 2–4 semaines puis 8–12 semaines.",
 B(12,14), niv="specialiste", spe="Oncologie")

META = dict(
 code="G7", lot="LOT_007", version="1.0.0", seed=22, date="2026-11-02",
 titre="Bouffées vasomotrices (flush)",
 titre_court="Bouffées vasomotrices (flush)", n_dx=12,
 note_version="v1 : gabarit Revision (EX/AP/SPE, 💡 fermé) — 1re production G7",
 note_media="Aucune image clinique dans les HTML LOT_007 (Phase A + DX.1–12) : media = null partout, bouton 🖼 absent.",
 intro_R="Devant un flush : signes vitaux d'abord. Hypotension ou œdème laryngé → adrénaline i.m. ; hypertension paroxystique → alphabloquant avant bêtabloquant ; fièvre avec confusion → antibiotique en 1 h ; tachycardie fébrile → soins intensifs. Puis sec ou humide, déclencheur, médicaments.",
 intro_D="Les 12 DX du LOT face à face : un signe, un examen qui tranche, une conduite. Les questions AP (bleu) et SPE (violet) sont mêlées aux EX : filtrez par niveau en haut.",
 intro_P="Tryptase avant l'adrénaline, bêtabloquant seul, FSH isolée, banane et noix avant le 5-HIAA, disulfirame contre le flush, iode radioactif dans le carcinome médullaire, tibolone après cancer du sein, paroxétine sous tamoxifène, métamizole, doses spécialisées.",
 verdict_label="Réflexe G7",
 footer="LOT_007 · G7 · Banque « Temps 1 » v1 · Faits issus exclusivement des leçons auditées LOT_007 (Phase A + Phase B DX.1–12) · Type A, une seule meilleure réponse (règles IML) · Aucun cliché dans les sources LOT_007 : aucune image affichée.",
 carte_html="""<div class="reflex"><b>Les 3 questions réflexes devant un flush</b><ol>
<li><b>Drapeau rouge ?</b> Hypotension, œdème de la langue ou de la gorge ; hypertension sévère paroxystique avec céphalées ; diarrhée avec sifflements ; souffle droit ; fièvre avec frissons ou confusion ; tachycardie majeure fébrile ; masse cervicale dure avec diarrhée.</li>
<li><b>Sec ou humide ?</b> Humide (sueurs) : ménopause, catécholamines, fièvre, thyrotoxicose ; sec : carcinoïde, mastocytose, médicaments.</li>
<li><b>Quel déclencheur, quel terrain ?</b> Alcool (minutes), médicament récent, chaleur et épices, peur ; âge, cycle, dernières règles ; goitre, nodule, antécédent familial de tumeur endocrine.</li></ol></div>
<div class="map" style="margin-top:10px">
<div class="ax"><h3>🌡️ Causes courantes</h3><ul>
<li>Femme &gt; 45 ans, bouffées humides, TSH normale → clinique, pas de FSH (DX.1)</li>
<li>Rougeur centrofaciale persistante, sans comédons → rosacée (DX.2)</li>
<li>Peur, examen et TSH normaux → exclusion, TCC (DX.3)</li></ul></div>
<div class="ax"><h3>💊 Réactionnel</h3><ul>
<li>Minutes après l'alcool, Asie de l'Est → ALDH2 ; abstinence (DX.5)</li>
<li>Amlodipine, niacine (PGD2), vancomycine ≤ 10 mg/min (DX.6)</li>
<li>Persiste à l'arrêt → chercher DX.9–11</li></ul></div>
<div class="ax"><h3>🧪 Examen qui tranche</h3><ul>
<li>TSH puis fT4/T3 (DX.4)</li>
<li>Métanéphrines plasmatiques libres (DX.10)</li>
<li>5-HIAA urinaire 24 h, sans banane ni noix (DX.9)</li>
<li>Tryptase basale &gt; 20 µg/L → moelle (DX.11)</li>
<li>Calcitonine devant un nodule (DX.12)</li></ul></div>
<div class="ax rf"><h3>🚩 Ordre d'exclusion</h3><ol>
<li>E1 Anaphylaxie (DX.8)</li><li>E2 Fièvre avec sepsis (DX.7)</li><li>E3 Phéochromocytome (DX.10)</li>
<li>E4 Thyrotoxicose décompensée (DX.4)</li><li>E5 Syndrome carcinoïde (DX.9)</li><li>E6 Mastocytose systémique (DX.11)</li><li>E7 Carcinome médullaire (DX.12)</li></ol>
<p class="red" style="margin:6px 0 0">Métanéphrines libres : sensibilité 99 %, spécificité 89 % ; 36 à 40 % des anaphylaxies ont une tryptase normale ; NT-proBNP &lt; 260 pg/mL : VPN 97 % pour la cardiopathie carcinoïde.</p></div>
</div>""",
 algo_html=f"""<table class="algo"><tr><th>Si…</th><th>Alors…</th></tr>
<tr class="e"><td>Hypotension, œdème laryngé, urticaire après exposition</td><td>DX.8 : adrénaline 0,3 mg i.m. à la cuisse, 144, tryptase ensuite, observation (biphasique)</td></tr>
<tr class="e"><td>Hypertension paroxystique, céphalées, sueurs</td><td>DX.10 : métanéphrines plasmatiques libres ; alphabloquant avant bêtabloquant ; pas de glucagon</td></tr>
<tr class="e"><td>Flush sec, diarrhée aqueuse, sifflements</td><td>DX.9 : 5-HIAA urinaire 24 h, imagerie ; NT-proBNP et échocardiographie</td></tr>
<tr class="e"><td>Fièvre avec frissons ou confusion</td><td>DX.7 : hémocultures, antibiotiques en 1 h</td></tr>
<tr class="e"><td>Tachycardie, thermophobie, goitre, TSH basse</td><td>DX.4 : fT4, fT3, thyréostatique ; orage → soins intensifs</td></tr>
<tr class="e"><td>Masse cervicale dure, diarrhée, calcitonine élevée</td><td>DX.12 : échographie, test RET, métanéphrines avant chirurgie</td></tr>
<tr class="e"><td>Flush sec, urticaire pigmentaire, tryptase &gt; 20 µg/L</td><td>DX.11 : biopsie de moelle, KIT D816V ; deux autoinjecteurs</td></tr>
<tr><td>Flush à la prise d'un médicament</td><td>DX.6 : réduire ou arrêter ; red man → débit ≤ 10 mg/min</td></tr>
<tr><td>Flush quelques minutes après l'alcool</td><td>DX.5 : éviter l'alcool ; disulfirame et métronidazole en cause ?</td></tr>
<tr><td>Flush humide, femme 45–55 ans, cycles irréguliers</td><td>DX.1 : clinique sans dosage ; THM ou fézolinétant ; &lt; 40 ans → FSH et estradiol</td></tr>
<tr><td>Érythème centrofacial persistant, papulopustules</td><td>DX.2 : brimonidine (érythème), ivermectine (papulopustules) ; œil douloureux → ophtalmologue</td></tr>
<tr><td>Épisodes liés à la peur, examen et bilan normaux</td><td>DX.3 : TCC ; ECG et troponine si douleur thoracique</td></tr>
</table>
<p class="intro">Source : <a href="{R}LOT_007_Phase_A_V0.html#ssp-p10">Phase A · §10 Arbre décisionnel</a> et <a href="{R}LOT_007_Phase_A_V0.html#ssp-p4">§4 Démarche diagnostique</a>.</p>""",
)
