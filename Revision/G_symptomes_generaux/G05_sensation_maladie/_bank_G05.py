# -*- coding: utf-8 -*-
# Banque G5 — Sensation de maladie (LOT_005).
# Sources : exclusivement LOT_Claude_Finaux/LOT_005 (Phase A + Phase B DX.1–15, audités C7 : 0 critique).
# Convention : opts[0] = bonne réponse (son « pourquoi pas » est ignoré) ; position finale fixée par build_ssp.py (seed).
# dx : le PREMIER DX.n cité = DX cible (couverture) ; les suivants = discrimination croisée.
R = "../../../repo/LOT_Claude_Finaux/LOT_005/"
def PA(sec, label): return (f"{R}LOT_005_Phase_A_V0.html#{sec}", f"Phase A {label}")
def B(n, p): return (f"{R}LOT_005_Phase_B_V0_DX.{n}.html#dx{n}-p{p}", f"Phase B DX.{n} §{p}")

# ═════════════ BLOC R · RAISONNER (danger d'abord, puis prochain pas)
q("R","DX.7 · premier geste","assessment_diagnosis","urgences",
 "Une femme de 84 ans, vivant seule, est amenée aux urgences car elle « ne se sent pas bien » depuis 2 jours. Elle ne localise aucune plainte. Pas de douleur rapportée. Traitement : hydrochlorothiazide et sertraline.",
 "Quelle est la première étape la plus appropriée ?",
 [("Constantes complètes et glycémie capillaire",""),
  ("Bandelette urinaire systématique","Elle n'est indiquée qu'avec des symptômes urinaires ou sans autre source chez un patient fébrile."),
  ("PHQ-9 pour dépister une dépression","L'humeur s'évalue après l'exclusion des urgences vitales."),
  ("Scanner cérébral sans contraste","Sans déficit focal, l'imagerie ne précède pas les constantes."),
  ("Retour à domicile et contrôle chez le médecin de famille","À Bâle, 59 % de ces patients ont une maladie grave dans les 30 jours.")],
 "Une plainte non spécifique chez la personne âgée est une urgence présumée. En 10 minutes : température, FC, PA, FR, SpO2, conscience et glycémie capillaire. Ces mesures dépistent le choc, l'hypoxie et l'hypoglycémie avant toute hypothèse.",
 "Mortalité à 30 jours 6 % à Bâle ; mortalité hospitalière OR 2,50 par rapport aux plaintes spécifiques.",
 PA("ssp-p4","§4 Démarche diagnostique"))

q("R","DX.11 · afébrile et confuse","management","urgences",
 "Une femme de 86 ans, résidente d'EMS, est confuse depuis ce matin. T 36,4 °C, FC 108/min, PA 94/58 mmHg, FR 24/min, SpO2 93 %. Aucun foyer évident à l'examen.",
 "Quelle est la conduite la plus appropriée ?",
 [("Hémocultures, lactate, antibiotique i.v. dans l'heure",""),
  ("Attendre la fièvre avant tout antibiotique","La fièvre manque souvent chez le sujet âgé ; l'absence de fièvre n'exclut pas le sepsis."),
  ("Scanner cérébral avant toute autre mesure","Aucun déficit focal ; la confusion compte ici comme critère qSOFA."),
  ("Rechercher le foyer, puis décider de l'antibiotique","Avec qSOFA 3, l'antibiotique ne doit pas attendre l'identification du foyer."),
  ("Halopéridol pour la confusion et surveillance","Traiter le symptôme sans la cause retarde le traitement du sepsis.")],
 "qSOFA = 3 (FR ≥ 22/min, conscience altérée, PAS ≤ 100 mmHg) : risque de mort élevé en cas d'infection (DX.11). On prélève lactate et hémocultures sans retarder l'antibiotique, donné dans l'heure, puis remplissage si hypoperfusion.",
 "Chez les plaintes non spécifiques, l'antibiotique arrive plus tard (5 h 26 contre 3 h 56) : c'est ce retard qui tue.",
 B(11,14))

q("R","DX.12 · déficit brutal","assessment_diagnosis","domicile",
 "Un homme de 74 ans est trouvé par son épouse à 9 h, incapable de parler correctement, le bras droit faible. Elle l'avait vu normal la veille à 22 h. À l'arrivée de l'ambulance, il est somnolent.",
 "Quelle mesure doit précéder toutes les autres ?",
 [("Glycémie capillaire",""),
  ("Scanner cérébral sans contraste","Indispensable, mais l'hypoglycémie se corrige d'abord, car elle simule un AVC."),
  ("Altéplase 0,9 mg/kg","Jamais avant l'imagerie, et la fenêtre de 4,5 heures est dépassée ici."),
  ("Électroencéphalogramme","Il ne précède ni la glycémie ni l'imagerie."),
  ("Ponction lombaire","Elle n'a aucune place dans un déficit focal brutal.")],
 "Devant un déficit brutal, la glycémie capillaire vient en premier : l'hypoglycémie imite l'AVC et se corrige en minutes (DX.12). On note ensuite l'heure du dernier état normal, on appelle le 144 et on fait le scanner.",
 "L'heure retenue est celle du dernier état normal (ici 22 h), pas celle de la découverte.",
 B(12,14))

q("R","DX.12 · heure de référence","assessment_diagnosis","urgences",
 "Une femme de 79 ans se réveille à 7 h avec une hémiparésie gauche. Elle s'était couchée à 23 h sans plainte. Glycémie 6,1 mmol/L. Le scanner sans contraste ne montre pas d'hémorragie.",
 "Quelle heure de début faut-il retenir pour la décision de reperfusion ?",
 [("23 h, dernier état normal connu",""),
  ("7 h, heure du réveil","L'heure de la découverte n'est pas l'heure du début."),
  ("L'heure d'arrivée aux urgences","Elle ne reflète pas la durée de l'ischémie."),
  ("L'heure du scanner","Elle sert au délai porte-imagerie, non à la fenêtre thérapeutique."),
  ("Le milieu de la nuit, par convention","Aucune convention de ce type : on retient le dernier état normal.")],
 "La fenêtre de thrombolyse (4,5 heures) se compte depuis le dernier état asymptomatique connu (DX.12). Au réveil, l'heure est inconnue : l'ESO propose l'IRM diffusion-FLAIR pour décider.",
 "Si l'heure est inconnue, l'IRM diffusion-FLAIR peut encore ouvrir la thrombolyse.",
 B(12,10))

q("R","DX.13 · dyspnée du diabétique","assessment_diagnosis","urgences",
 "Un homme diabétique de 70 ans consulte pour un malaise et un essoufflement apparus il y a 2 heures. Il n'a aucune douleur thoracique. FC 96/min, PA 138/82 mmHg, SpO2 95 %.",
 "Quel examen faut-il réaliser en premier ?",
 [("ECG 12 dérivations dans les 10 minutes",""),
  ("Radiographie du thorax","Utile ensuite ; l'ECG passe avant devant un équivalent angineux."),
  ("D-dimères","Ils ne précèdent pas l'ECG et ne visent pas le SCA."),
  ("Spirométrie","Examen différé, sans place en urgence."),
  ("Échocardiographie transthoracique programmée","Le délai est incompatible avec un SCA possible.")],
 "Chez le sujet âgé, la femme et le diabétique, le SCA se manifeste souvent par un malaise ou une dyspnée sans douleur (DX.13). L'ECG se fait dans les 10 minutes, puis la troponine hs à 0 et 1 heure.",
 "La dyspnée peut être le seul équivalent angineux.",
 B(13,14))

q("R","DX.15 · choc et corticoïdes","management","urgences",
 "Un homme de 66 ans sous prednisone 20 mg/j depuis 6 mois pour une polymyalgie a arrêté son traitement il y a 4 jours. Il vomit, se sent très mal. PA 78/45 mmHg malgré 1 L de cristalloïde, Na 127 mmol/L, glycémie 3,9 mmol/L.",
 "Quelle est la conduite la plus appropriée ?",
 [("Hydrocortisone 100 mg i.v. immédiatement",""),
  ("Test à la corticotropine avant tout traitement","Le test confirme plus tard ; en crise, on traite sans attendre."),
  ("Noradrénaline seule","Le choc par déficit en cortisol reste réfractaire sans hydrocortisone."),
  ("Restriction hydrique pour l'hyponatrémie","Hypovolémique et en choc, il a besoin de volume, pas de restriction."),
  ("Reprendre la prednisone 20 mg par voie orale","La voie orale échoue chez un patient qui vomit.")],
 "Arrêt brutal d'une corticothérapie de plus de 2 semaines, vomissements, hypotension réfractaire et hyponatrémie : crise surrénalienne (DX.15). On prélève cortisol et ACTH, puis hydrocortisone 100 mg i.v. sans attendre le résultat, NaCl 0,9 % 1 L en 1 heure, et 200 mg/24 h ensuite.",
 "Le glucocorticoïde exogène freine l'axe après plus de 2 semaines : le stress ou l'arrêt déclenchent la crise.",
 PA("ssp-p14","§14 Pièges"))

q("R","DX.2 · hyponatrémie et convulsion","management","urgences",
 "Une femme de 78 ans, sous hydrochlorothiazide, est amenée après une crise convulsive. Elle vomit et reste somnolente. Na 116 mmol/L, glycémie 6,4 mmol/L.",
 "Quelle est la conduite immédiate la plus appropriée ?",
 [("Bolus de NaCl 3 % 100 à 150 mL en soins intensifs",""),
  ("Restriction hydrique à 500 mL par jour","Réservée à l'hyponatrémie chronique asymptomatique."),
  ("NaCl 0,9 % 2 L en 2 heures","Le soluté isotonique ne corrige pas une hyponatrémie profonde symptomatique."),
  ("Tolvaptan per os","Il n'a pas sa place dans l'urgence neurologique et est contre-indiqué en hypovolémie."),
  ("Attendre l'osmolalité urinaire avant toute correction","Les symptômes sévères imposent de traiter d'abord.")],
 "Natrémie < 125 mmol/L avec vomissements, somnolence ou convulsions : risque d'œdème cérébral (DX.2, 🚩 E5). Bolus de NaCl hypertonique 3 % en soins intensifs, puis correction lente (≤ 10 mmol/L le premier jour) ; arrêt du thiazide.",
 "Les symptômes sévères ne retardent pas l'hypertonique ; la surcorrection expose à la démyélinisation osmotique.",
 PA("ssp-p11","§11 Prise en charge"))

q("R","DX.14 · lombalgie nocturne","assessment_diagnosis","cabinet",
 "Un homme de 68 ans, traité il y a 2 ans pour un cancer de la prostate, se sent mal et souffre depuis 2 semaines d'une douleur dorsale qui le réveille la nuit. Force et sensibilité normales. Pas de trouble sphinctérien.",
 "Quel examen faut-il demander ?",
 [("IRM de tout le rachis en urgence",""),
  ("Radiographie lombaire standard","Elle manque une épidurite débutante."),
  ("Scintigraphie osseuse programmée","Le délai est incompatible avec une compression possible."),
  ("Dosage du PSA seul","Un marqueur sert au suivi ; il ne localise pas une lésion épidurale."),
  ("Physiothérapie et réévaluation à 6 semaines","Attendre le déficit fait perdre la marche.")],
 "Chez un patient avec antécédent de cancer, une douleur rachidienne nocturne peut être le premier signe d'une compression médullaire (DX.14). On demande une IRM de tout le rachis en urgence, avant l'apparition d'un déficit.",
 "Douleur dorsale avec déficit ou trouble sphinctérien : IRM du rachis entier et dexaméthasone en urgence.",
 B(14,14))

q("R","DX.11 · remplissage","management","urgences",
 "Un homme de 80 ans, 70 kg, a une pneumonie. PA 84/50 mmHg, lactate 4,1 mmol/L. Les hémocultures sont prélevées et la ceftriaxone est en cours.",
 "Quel remplissage est le plus approprié ?",
 [("Cristalloïde équilibré ≥ 30 mL/kg en 3 h",""),
  ("Glucose 5 % 1 L en 1 heure","Le glucose apporte de l'eau libre, sans effet volémique durable."),
  ("Albumine 20 % en première intention","Les cristalloïdes restent la première ligne."),
  ("500 mL de NaCl 0,9 % sur 24 heures","Volume très insuffisant dans l'hypoperfusion."),
  ("Pas de remplissage avant la noradrénaline","Le remplissage précède le vasopresseur.")],
 "Hypoperfusion (lactate > 2 mmol/L, PA basse) : au moins 30 mL/kg de cristalloïde, de préférence équilibré comme le Ringer-lactate, dans les 3 premières heures (DX.11), soit 2 100 mL pour 70 kg. Noradrénaline si la PAM reste < 65 mmHg.",
 "Surviving Sepsis Campaign 2021 : remplissage et antibiotique avancent ensemble, sans s'attendre.",
 B(11,14))

q("R","DX.13 · sus-décalage","management","urgences",
 "Une femme de 72 ans se plaint d'un malaise et de nausées depuis 1 heure. L'ECG montre un sus-décalage de ST de 2 mm en DII, DIII et aVF. La première troponine hs n'est pas encore revenue.",
 "Quelle est la conduite la plus appropriée ?",
 [("Reperfusion coronaire sans attendre la troponine",""),
  ("Attendre la troponine de 1 heure","Un STEMI se traite sans attendre la troponine ; elle peut rester normale au début."),
  ("Échocardiographie de stress","Elle n'a pas sa place en phase aiguë et retarde la reperfusion."),
  ("Antiémétique et ECG de contrôle à 6 heures","Chaque minute perdue détruit du myocarde."),
  ("Scanner thoracique injecté pour exclure d'abord une embolie","Le sus-décalage territorial impose la reperfusion.")],
 "Sus-décalage ST dans deux dérivations contiguës : STEMI (DX.13). AAS et héparine, reperfusion par angioplastie en moins de 120 minutes ; à défaut, fibrinolyse dans les 10 minutes. La troponine ne doit jamais retarder la reperfusion.",
 "Un premier dosage de troponine normal est attendu dans les premières heures d'un vrai STEMI.",
 B(13,13))

q("R","DX.10 · décompensation diabétique","management","urgences",
 "Un homme de 24 ans, diabétique de type 1, se sent mal depuis 2 jours. Il vomit et respire profondément. Glycémie 26 mmol/L.",
 "Quelle est la prochaine étape la plus appropriée ?",
 [("Cétonémie et gaz du sang, puis perfusion",""),
  ("Insuline glargine 20 U s.c.","Une insuline lente n'a pas sa place dans l'acidocétose ; on utilise une rapide i.v."),
  ("HbA1c pour juger du déséquilibre","Elle ne dit rien de la décompensation aiguë."),
  ("Insuline rapide i.v. en bolus avant tout bilan","La perfusion et le potassium précèdent l'insuline."),
  ("Métoclopramide et retour à domicile","Vomissements et respiration ample signent une urgence.")],
 "Vomissements, respiration profonde ou confusion chez un diabétique : cétones, gaz du sang et perfusion avant l'insuline (DX.10). Acidocétose : glycémie > 11 mmol/L, cétonémie ≥ 3 mmol/L, pH < 7,3.",
 "Insuline rapide i.v. ensuite, sous contrôle de la glycémie et du potassium.",
 B(10,13))

q("R","DX.6 · idées suicidaires","management","cabinet",
 "Une femme de 58 ans consulte pour un malaise diffus depuis 2 mois. Le bilan somatique est normal. PHQ-9 = 22. À la question directe, elle dit avoir prévu de prendre tous ses comprimés ce week-end.",
 "Quelle est la conduite la plus appropriée ?",
 [("Évaluation psychiatrique urgente le jour même",""),
  ("Sertraline 50 mg et contrôle dans 2 semaines","Avec un plan précis, la sécurité passe avant le traitement."),
  ("Psychothérapie programmée dans le mois","Délai incompatible avec un risque imminent."),
  ("Compléter d'abord le bilan endocrinien","Le bilan somatique est déjà normal ; le risque suicidaire prime."),
  ("Lui demander de rappeler si les idées persistent","Laisser partir une patiente avec plan et moyens est dangereux.")],
 "Idées suicidaires avec plan ou accès aux moyens : évaluation psychiatrique urgente ou hospitalisation (DX.6, nœud N0). Toute idée suicidaire se demande directement.",
 "Demander directement les idées suicidaires ne provoque pas le passage à l'acte.",
 B(6,10))

q("R","DX.8 · bradypnée et myosis","management","domicile",
 "Une femme de 81 ans sous patch de fentanyl est retrouvée somnolente. FR 7/min, pupilles en myosis serré, SpO2 86 %. Glycémie 6,0 mmol/L.",
 "Quelle est la conduite immédiate la plus appropriée ?",
 [("Naloxone 0,4 à 2 mg i.v. et oxygène",""),
  ("Flumazénil 0,3 mg i.v.","Il antagonise les benzodiazépines, pas les opioïdes."),
  ("Scanner cérébral avant tout traitement","Le tableau toxique se traite d'abord."),
  ("Acétylcystéine i.v.","C'est l'antidote du paracétamol."),
  ("Glucose 20 % i.v.","La glycémie est normale.")],
 "Respiration lente et myosis : surdosage opioïde probable (DX.8). Naloxone 0,4 à 2 mg i.v., i.m. ou s.c., répétable toutes les 2 à 3 minutes, oxygène et surveillance ; retirer le patch.",
 "Sans effet après 2 ou 3 injections, l'état n'est pas dû aux opioïdes seuls : chercher une autre cause.",
 B(8,14))

q("R","DX.1 · pyélonéphrite fébrile","assessment_diagnosis","urgences",
 "Une femme de 52 ans a de la fièvre à 39,2 °C, des frissons et une douleur lombaire droite depuis hier. PA 128/76 mmHg, FC 98/min. Bandelette : leucocytes et nitrites positifs.",
 "Quel examen faut-il ajouter avant le traitement ?",
 [("Échographie pour exclure un obstacle",""),
  ("Scintigraphie rénale","Sans place dans la prise en charge aiguë."),
  ("Cystoscopie","Examen invasif sans indication ici."),
  ("Urographie i.v.","Remplacée par l'échographie ; contraste inutile."),
  ("Aucun examen : fosfomycine en dose unique","La fosfomycine traite la cystite, pas la pyélonéphrite.")],
 "Fièvre avec douleur lombaire : pyélonéphrite (DX.1). L'ECBU confirme le germe ; l'échographie exclut un obstacle, car une pyélonéphrite obstructive exige un drainage urgent.",
 "Pyélonéphrite avec obstacle = drainage urgent ; l'antibiotique seul ne suffit pas.",
 B(1,10))

q("R","DX.4 · raideur de nuque","management","urgences",
 "Un homme de 71 ans est amené pour confusion et fièvre à 38,9 °C depuis 12 heures. Nuque raide. PA 132/80 mmHg. Pas de déficit focal.",
 "Quelle est la conduite la plus appropriée ?",
 [("Antibiotique sans attendre la ponction lombaire",""),
  ("Ponction lombaire, puis antibiotique selon le résultat","On ne retarde pas l'antibiotique pour la ponction."),
  ("IRM cérébrale avant tout antibiotique","L'imagerie ne doit pas retarder l'antibiothérapie."),
  ("Paracétamol et réévaluation à 6 heures","Une méningite bactérienne évolue en quelques heures."),
  ("Antiviral seul en attendant la PCR","Une méningite bactérienne doit être couverte d'emblée.")],
 "Fièvre, confusion et raideur de nuque : méningite à suspecter (DX.4). Antibiotique sans délai ; la ponction lombaire ne doit pas le retarder.",
 "Chez le sujet âgé, l'arthrose cervicale simule la raideur et le delirium peut la précéder.",
 B(4,10))

q("R","DX.14 · hypercalcémie","management","urgences",
 "Un homme de 74 ans, fumeur, est confus depuis une semaine, boit beaucoup et urine souvent. Calcémie corrigée 3,4 mmol/L, créatinine 118 µmol/L. Perte de 6 kg en 3 mois.",
 "Quelle est la première mesure thérapeutique ?",
 [("Hydratation i.v.",""),
  ("Zolédronate 4 mg d'emblée, sans perfusion préalable","L'AIPS impose de contrôler l'état hydrique avant le bisphosphonate."),
  ("Restriction hydrique","L'hypercalcémie empêche le rein de concentrer l'urine : le patient est déjà déshydraté."),
  ("Calcium et vitamine D","Ils aggravent l'hypercalcémie."),
  ("Biopsie avant tout traitement","La recherche du cancer suit la correction ; la confusion impose de traiter d'abord.")],
 "Calcémie corrigée ≥ 3,0 mmol/L : hypercalcémie, souvent maligne (DX.14, 🚩 E6). On hydrate d'abord, puis zolédronate 4 mg en au moins 15 minutes dans une voie séparée, et on cherche le cancer (scanner thoraco-abdominal, biopsie).",
 "Confusion avec polyurie : calcémie corrigée par l'albumine.",
 PA("ssp-p11","§11 Prise en charge"))

q("R","DX.9 · virose d'exclusion","assessment_diagnosis","cabinet",
 "Une femme de 76 ans consulte en saison grippale pour fièvre et malaise depuis hier. FR 23/min, PA 98/60 mmHg, elle est un peu ralentie. Elle souhaite « juste un médicament contre la grippe ».",
 "Quelle est la conduite la plus appropriée ?",
 [("Urgences : hémocultures et antibiotique",""),
  ("Oseltamivir 75 mg deux fois par jour à domicile","Le diagnostic viral ne se pose qu'après exclusion des drapeaux rouges."),
  ("Paracétamol et contrôle dans 48 heures","qSOFA à 3 : on ne temporise pas."),
  ("Test grippe puis décision selon le résultat","Un test positif n'exclut pas une surinfection ou un sepsis."),
  ("Vaccin contre la grippe le jour même","La vaccination prévient, elle ne traite pas un patient instable.")],
 "Le syndrome viral banal est un diagnostic d'exclusion (DX.9). FR ≥ 22/min, PAS ≤ 100 mmHg et conscience altérée = qSOFA 3 : urgences, hémocultures, antibiotique sans délai.",
 "Piège d'examen : poser « virose » avant d'avoir exclu les drapeaux rouges.",
 B(9,14))

# ═════════════ BLOC D · DISCRIMINER (les 15 DX face à face)
# ── DX.1 Infection urinaire
q("D","DX.1 · cystite simple","management","cabinet",
 "Une femme de 29 ans, non enceinte, sans antécédent, a depuis hier des brûlures mictionnelles, une pollakiurie et une douleur sus-pubienne. Pas de fièvre, pas de douleur lombaire, pas de pertes vaginales.",
 "Quelle est la conduite la plus appropriée ?",
 [("Fosfomycine 3 g per os en dose unique",""),
  ("ECBU et attendre le résultat avant de traiter","Chez la femme de moins de 65 ans avec ce tableau, aucun test n'est nécessaire."),
  ("Ceftriaxone 2 g i.v.","Réservée à la pyélonéphrite ou à l'infection sévère."),
  ("Échographie rénale urgente","Aucun signe de pyélonéphrite ni d'obstacle."),
  ("Amoxicilline-clavulanate 7 jours","Elle ne fait pas partie du traitement court de la cystite non compliquée.")],
 "Cystite non compliquée de la femme non enceinte de moins de 65 ans : dysurie, pollakiurie et douleur sus-pubienne suffisent, sans test (SSGO 2020) (DX.1). Monuril® 3 g en dose unique, à jeun, le soir, vessie vidée.",
 "Fosfomycine : femmes et adolescentes de plus de 12 ans ; pas chez l'homme.",
 B(1,8))

q("D","DX.1 · homme fébrile","management","cabinet",
 "Un homme de 67 ans a depuis 2 jours des brûlures mictionnelles et une fièvre à 38,3 °C. PA 136/82 mmHg, FC 92/min. Pas de sonde, pas d'antécédent urologique.",
 "Quelle est la conduite la plus appropriée ?",
 [("ECBU, puis traitement d'une infection compliquée",""),
  ("Fosfomycine 3 g en dose unique","L'AIPS limite l'indication curative à la femme et à l'adolescente."),
  ("Aucun antibiotique, boissons abondantes","Fièvre et symptômes chez l'homme imposent un traitement."),
  ("Bandelette seule et traitement de 3 jours","Chez l'homme, l'infection est toujours compliquée."),
  ("Antibiotique seulement après culture positive à 72 h","Le patient fébrile se traite dès l'ECBU prélevé.")],
 "Chez l'homme, l'infection urinaire se traite comme compliquée (DX.1) : ECBU d'abord, puis traitement plus long, adapté à la culture. Il en va de même en cas de grossesse, de sonde ou de comorbidité.",
 "Monuril® n'est pas une option chez l'homme.",
 B(1,13))

q("D","DX.1 vs DX.11 · urosepsis","management","urgences",
 "Une femme de 79 ans a des brûlures mictionnelles depuis 3 jours. Ce matin, elle est confuse. T 38,8 °C, PA 92/54 mmHg, FR 24/min.",
 "Quelle est la conduite la plus appropriée ?",
 [("Prélèvements, puis antibiotique i.v. immédiat",""),
  ("Fosfomycine 3 g et retour à domicile","Le traitement oral court ne s'applique pas à un urosepsis."),
  ("ECBU puis antibiotique adapté à l'antibiogramme","L'antibiotique ne doit pas attendre la culture."),
  ("Imagerie cérébrale pour la confusion","La confusion est ici un critère de sepsis, non un signe focal."),
  ("Hydratation orale et contrôle demain","Instabilité et confusion imposent une prise en charge immédiate.")],
 "Instabilité hémodynamique, confusion aiguë ou qSOFA ≥ 2 avec foyer urinaire : urosepsis (DX.1, DX.11). On prélève (hémocultures, ECBU), puis antibiotique i.v. immédiat, par exemple ceftriaxone, et remplissage.",
 "Un signe de sepsis impose l'antibiotique i.v. immédiat après les prélèvements.",
 B(1,10))

# ── DX.2 Troubles électrolytiques
q("D","DX.2 · hyponatrémie modérée","assessment_diagnosis","hôpital",
 "Une femme de 81 ans se sent faible et nauséeuse depuis une semaine. Elle est orientée, sans céphalée ni vomissement. Na 128 mmol/L. Traitement : hydrochlorothiazide et citalopram.",
 "Quelle est la prochaine étape la plus appropriée ?",
 [("Osmolalité, natriurèse et évaluation de la volémie",""),
  ("Bolus de NaCl 3 %","Réservé aux symptômes sévères ou à la natrémie profonde symptomatique."),
  ("Tolvaptan d'emblée","Contre-indiqué en cas d'hypovolémie, à exclure d'abord."),
  ("Imagerie cérébrale","Aucun signe neurologique focal."),
  ("Aucune mesure : valeur sans importance à cet âge","Une hyponatrémie modérée explique faiblesse et nausées.")],
 "Une natrémie basse seule ne donne pas la cause (DX.2) : on mesure l'osmolalité plasmatique et urinaire, la natriurèse et la volémie. On cherche thiazide, ISRS, insuffisance surrénalienne, SIADH.",
 "Thiazide et antidépresseur ensemble : contrôler la natrémie, surtout chez la personne âgée.",
 B(2,10))

q("D","DX.2 · hyperkaliémie et ECG","management","urgences",
 "Un homme de 76 ans en insuffisance rénale chronique se sent mal et faible. K 7,1 mmol/L sur un prélèvement non hémolysé. L'ECG montre des ondes T pointues et un QRS élargi.",
 "Quelle mesure est la plus urgente ?",
 [("Calcium i.v. immédiat",""),
  ("Chlorure de potassium i.v.","Il aggrave l'hyperkaliémie."),
  ("Restriction alimentaire en potassium","Mesure de fond, inefficace en urgence."),
  ("Dialyse programmée la semaine suivante","Le délai est incompatible avec un QRS large."),
  ("Répéter le dosage dans 24 heures","Avec un ECG anormal, on traite d'abord.")],
 "Hyperkaliémie avec modification ECG : calcium i.v. immédiat (DX.2), ECG en continu, puis traitement selon le protocole local ; évoquer une crise surrénalienne si le contexte s'y prête.",
 "Un prélèvement hémolysé augmente faussement le potassium : vérifier avant de conclure sans ECG anormal.",
 B(2,13))

q("D","DX.2 vs DX.14 · calcémie à corriger","assessment_diagnosis","hôpital",
 "Une femme de 83 ans dénutrie se sent mal. Calcémie totale 2,12 mmol/L, albumine 24 g/L. Elle n'a ni paresthésie ni crampe.",
 "Quelle est l'interprétation la plus appropriée ?",
 [("Calculer la calcémie corrigée par l'albumine",""),
  ("Hypocalcémie à substituer d'emblée","La calcémie brute est faussement basse quand l'albumine est basse."),
  ("Hypercalcémie maligne à traiter par zolédronate","La valeur brute est basse ; seule la valeur corrigée tranche."),
  ("Dosage de la PTH en urgence","Il vient après la calcémie corrigée."),
  ("Valeur normale pour l'âge, aucune suite","On ne conclut pas sans corriger par l'albumine.")],
 "Une calcémie brute sans albumine peut tromper (DX.2) : il faut la corriger par l'albumine avant de conclure. L'hypercalcémie maligne se définit par une calcémie corrigée ≥ 3,0 mmol/L.",
 "Corriger la calcémie par l'albumine avant toute décision.",
 B(2,8), niv="approfondissement")

# ── DX.3 Pneumonie
q("D","DX.3 · CRB-65","management","cabinet",
 "Un homme de 84 ans est confus depuis hier. Toux, T 38,4 °C, FR 32/min, PA 86/54 mmHg. La radiographie montre un infiltrat lobaire droit nouveau.",
 "Quelle orientation est la plus appropriée ?",
 [("Hospitalisation urgente, soins intensifs à discuter",""),
  ("Amoxicilline à domicile","CRB-65 à 4 : le domicile est exclu."),
  ("Contrôle radiologique à 6 semaines","La gravité impose une décision immédiate."),
  ("Hospitalisation à envisager selon le contexte","Cette option vaut pour un score de 1 à 2."),
  ("Antibiotique si la CRP dépasse 100 mg/L","La CRP seule ne décide pas du lieu de soins.")],
 "CRB-65 : confusion, FR ≥ 30/min, PAS < 90 ou PAD ≤ 60 mmHg, âge ≥ 65 ans (DX.3). Score 4 : hospitalisation urgente, soins intensifs à discuter, hémocultures, bêta-lactamine i.v.",
 "Score 0 : domicile si le contexte le permet ; 1 à 2 : hospitalisation à envisager ; 3 à 4 : urgence.",
 B(3,8))

q("D","DX.3 · pneumonie simple","management","cabinet",
 "Un homme de 42 ans, sans comorbidité, a de la fièvre et une toux productive depuis 3 jours. FR 18/min, PA 128/80 mmHg, orienté. La radiographie montre un infiltrat nouveau du lobe inférieur gauche.",
 "Quel traitement est le plus approprié ?",
 [("Amoxicilline per os à domicile",""),
  ("Ceftriaxone i.v. à l'hôpital","CRB-65 à 0 : l'hospitalisation n'est pas nécessaire."),
  ("Aucun antibiotique, pneumonie probablement virale","Un infiltrat nouveau avec signes infectieux pose le diagnostic de pneumonie."),
  ("Oseltamivir seul","Rien n'oriente vers une grippe."),
  ("Macrolide seul d'emblée","Le macrolide s'ajoute en cas de gravité ou de légionellose.")],
 "CRB-65 à 0 et contexte stable : traitement ambulatoire par amoxicilline (DX.3). Le macrolide s'ajoute en cas de gravité ou de légionellose. Fièvre persistante après 72 heures : chercher un empyème ou un autre diagnostic.",
 "Dose AIPS dans l'infection légère à moyenne : 1 500 à 3 000 mg par jour en 3 à 4 prises.",
 B(3,13))

q("D","DX.3 · radiographie normale","assessment_diagnosis","urgences",
 "Une femme de 88 ans, en EMS, chute et se dit fatiguée. T 37,9 °C, FR 24/min, SpO2 90 %, crépitants de la base droite. La radiographie du thorax est normale.",
 "Quelle est la prochaine étape la plus appropriée ?",
 [("Échographie pulmonaire ou scanner thoracique",""),
  ("Exclure la pneumonie et chercher une autre cause","Une radiographie précoce normale n'exclut pas la pneumonie."),
  ("Répéter la radiographie dans 6 semaines","Le délai est inadapté à une infection aiguë."),
  ("Bronchoscopie","Examen invasif, non indiqué en première intention."),
  ("Procalcitonine unique pour décider","Elle sert surtout à arrêter l'antibiotique.")],
 "Une radiographie normale au début n'exclut pas la pneumonie (DX.3). Si la suspicion est forte, l'échographie ou le scanner tranche. Chez le sujet âgé, chute, confusion ou asthénie peuvent être la seule présentation.",
 "La pneumonie du sujet âgé peut être silencieuse à l'auscultation comme à la radiographie.",
 B(3,10))

# ── DX.4 Infections
q("D","DX.4 · abcès","management","hôpital",
 "Un homme de 63 ans, diabétique, se sent mal depuis une semaine. T 38,6 °C, CRP 210 mg/L. Le scanner montre un abcès hépatique de 6 cm. Il reçoit une antibiothérapie i.v. adaptée depuis 48 heures, sans amélioration.",
 "Quelle est la conduite la plus appropriée ?",
 [("Drainage de l'abcès",""),
  ("Doubler la dose d'antibiotique","Un abcès ne guérit pas par l'antibiotique seul."),
  ("Arrêter l'antibiotique et observer","Le foyer reste actif et non contrôlé."),
  ("Ajouter un antifongique empirique","Rien n'oriente vers un champignon."),
  ("Corticoïdes pour la fièvre","Ils masquent l'infection sans la traiter.")],
 "L'antibiotique seul échoue sur une collection : il faut drainer le pus ou retirer le matériel infecté (DX.4). Le contrôle de la source fait partie du traitement.",
 "Abcès = drainage ; matériel infecté = retrait.",
 B(4,14))

q("D","DX.4 · douleur disproportionnée","management","urgences",
 "Un homme de 58 ans se sent très mal depuis 12 heures. Il a une douleur intense de la cuisse droite, disproportionnée par rapport à un érythème discret. T 38,7 °C, FC 118/min, PA 102/64 mmHg.",
 "Quelle est la conduite la plus appropriée ?",
 [("Avis chirurgical urgent",""),
  ("Antibiotique oral et contrôle à 48 heures","La douleur disproportionnée évoque une infection nécrosante."),
  ("Doppler veineux et anticoagulation","Le tableau infectieux prime sur la thrombose."),
  ("Anti-inflammatoire et repos","Ils masquent l'évolution."),
  ("IRM programmée la semaine suivante","Délai incompatible avec une infection nécrosante.")],
 "Une douleur cutanée disproportionnée chez un patient fébrile impose d'appeler le chirurgien (DX.4). On traite comme un sepsis si la pression baisse : hémocultures, antibiotique dans l'heure.",
 "Chercher le foyer partout : poumon, voie urinaire, peau, abdomen, cœur, cathéter.",
 B(4,10))

q("D","DX.4 · pas de foyer","assessment_diagnosis","hôpital",
 "Une femme de 74 ans est hospitalisée pour malaise et fièvre. Constantes stables. Examen complet, radiographie du thorax, urine et hémocultures sans foyer après 72 heures.",
 "Quelle est la prochaine étape la plus appropriée ?",
 [("Scanner, puis cause non infectieuse",""),
  ("Antibiothérapie empirique au long cours","Sans foyer ni gravité, elle masque le diagnostic."),
  ("Conclure à une fièvre virale et la renvoyer","La recherche n'est pas terminée."),
  ("Sortie sans suivi","Fièvre sans foyer = recherche à poursuivre."),
  ("Répéter le même bilan chaque jour","Il n'apporte rien de nouveau.")],
 "Si aucun foyer n'apparaît après le bilan, on fait un scanner, puis on cherche une cause non infectieuse (DX.4) : inflammatoire, néoplasique, médicamenteuse.",
 "Piège : arrêter la recherche après une première infection trouvée, ou conclure trop tôt.",
 B(4,10))

# ── DX.5 Musculosquelettique
q("D","DX.5 · ceintures","assessment_diagnosis","cabinet",
 "Une femme de 73 ans se sent mal depuis 6 semaines. Elle a mal aux deux épaules et aux hanches, avec une raideur matinale de 90 minutes. CRP 48 mg/L. FR et ACPA négatifs. Pas de céphalée, pas de trouble visuel.",
 "Quel diagnostic est le plus probable ?",
 [("Polymyalgie rhumatismale",""),
  ("Fibromyalgie","Elle ne donne ni raideur matinale prolongée ni CRP élevée."),
  ("Polyarthrite rhumatoïde","FR et ACPA négatifs, pas de synovite des petites articulations."),
  ("Myopathie aux statines","Elle donne une faiblesse avec CK élevée, sans raideur des ceintures."),
  ("Dépression avec plaintes somatiques","La CRP élevée et la raideur orientent vers l'inflammation.")],
 "Après 50 ans, douleur bilatérale des épaules, raideur matinale > 45 minutes et CRP élevée évoquent une polymyalgie rhumatismale (DX.5). Il faut d'abord exclure infection et cancer, chercher une artérite à cellules géantes, puis demander l'avis de rhumatologie.",
 "Les critères EULAR/ACR 2012 classent, ils ne posent pas le diagnostic.",
 B(5,13))

q("D","DX.5 🚩 · trouble visuel","management","cabinet",
 "Un homme de 76 ans se sent mal depuis 3 semaines, avec céphalée temporale, douleur de la mâchoire en mastiquant et, ce matin, une vision floue de l'œil droit. CRP 92 mg/L.",
 "Quelle est la conduite la plus appropriée ?",
 [("Glucocorticoïde immédiat et avis spécialisé sous 24 h",""),
  ("Biopsie de l'artère temporale avant tout traitement","Attendre la biopsie expose à une cécité irréversible."),
  ("AINS et contrôle ophtalmologique à 2 semaines","Délai incompatible avec la menace visuelle."),
  ("IRM cérébrale programmée","Elle ne doit pas retarder le traitement."),
  ("Prednisone 15 mg par jour","Dose de la polymyalgie, insuffisante pour l'artérite.")],
 "Trouble visuel, claudication de la mâchoire et céphalée temporale : artérite à cellules géantes (DX.5). Glucocorticoïde sans attendre la biopsie et avis spécialisé sous 24 heures, car la cécité est irréversible.",
 "Une biopsie normale n'exclut pas l'artérite.",
 B(5,14))

q("D","DX.5 vs DX.8 · CK sous statine","management","cabinet",
 "Un homme de 69 ans se sent faible depuis 3 semaines et peine à se lever d'une chaise. Son atorvastatine a été augmentée il y a un mois. CK 4 200 U/L, créatinine normale.",
 "Quelle est la conduite la plus appropriée ?",
 [("Arrêter la statine, contrôler CK et créatinine",""),
  ("Poursuivre la statine et ajouter de la physiothérapie","La CK élevée sous médicament myotoxique peut annoncer une rhabdomyolyse."),
  ("Prednisone pour une polymyalgie","La faiblesse avec CK élevée n'est pas une polymyalgie."),
  ("Doubler la statine pour le risque cardiovasculaire","Elle aggraverait la myopathie."),
  ("Électromyogramme avant toute mesure","L'arrêt de la cause suspecte vient d'abord.")],
 "Faiblesse proximale avec CK élevée sous médicament myotoxique : arrêter le médicament suspect, puis contrôler CK et créatinine, car la CK élevée peut annoncer une rhabdomyolyse (DX.5, DX.8).",
 "L'amélioration à l'arrêt est le meilleur test diagnostique d'un effet indésirable.",
 B(5,13))

# ── DX.6 Psychologique
q("D","DX.6 · PHQ-9 positif","assessment_diagnosis","cabinet",
 "Un homme de 49 ans se sent « malade sans être malade » depuis 2 mois. Examen normal ; FSC, CRP, ionogramme, glycémie et TSH normaux. PHQ-9 = 14. Pas d'idée suicidaire.",
 "Quelle est la prochaine étape la plus appropriée ?",
 [("Entretien clinique selon les critères DSM-5",""),
  ("Diagnostic de dépression sur le seul PHQ-9","Le PHQ-9 est un outil de dépistage, pas un diagnostic."),
  ("Scanner thoraco-abdominal","Aucun signe d'appel de cancer."),
  ("Test à la corticotropine","Aucun argument pour une insuffisance surrénalienne."),
  ("Benzodiazépine au long cours","Elle ne traite pas la dépression et expose à la dépendance.")],
 "PHQ-9 ≥ 10 avec bilan normal : entretien clinique pour poser le diagnostic (DX.6). DSM-5 : au moins 5 symptômes sur 9 pendant 2 semaines, dont humeur dépressive ou perte d'intérêt, avec détresse ou handicap.",
 "Méta-analyse 2019 : seuil 10, sensibilité 0,88, spécificité 0,85.",
 B(6,14))

q("D","DX.6 vs DX.13 · anxiété et thorax","assessment_diagnosis","urgences",
 "Une femme de 61 ans, suivie pour trouble anxieux, se sent mal depuis 40 minutes avec oppression thoracique et dyspnée. Elle dit : « c'est encore mon angoisse ». FC 102/min, PA 148/90 mmHg.",
 "Quelle est la prochaine étape la plus appropriée ?",
 [("ECG et troponine hs",""),
  ("Lorazépam et observation","L'anxiété ne s'attribue qu'après exclusion du SCA."),
  ("Exercices respiratoires et retour à domicile","Attribution prématurée d'une douleur thoracique."),
  ("Sertraline à majorer","Le traitement de fond ne répond pas à une urgence possible."),
  ("Avis psychiatrique urgent","Le bilan organique précède l'avis psychiatrique.")],
 "L'anxiété ne doit jamais exclure un SCA, une infection ou une cause endocrinienne (DX.6, DX.13). L'ECG et la troponine précèdent tout diagnostic d'anxiété devant une douleur thoracique avec dyspnée.",
 "Fièvre, confusion, déficit ou douleur thoracique : bilan organique urgent avant d'attribuer à l'anxiété.",
 B(6,14))

# ── DX.7 Pathologie somatique claire
q("D","DX.7 · bilan de première intention","assessment_diagnosis","urgences",
 "Une femme de 82 ans se sent mal depuis 3 jours. Constantes stables, glycémie capillaire 6,2 mmol/L, pas de douleur thoracique ni de déficit. L'examen ne trouve pas de foyer.",
 "Quel bilan de première intention est le plus approprié ?",
 [("ECG, ionogramme, Ca, créatinine, glucose, FSC, CRP, TSH",""),
  ("Marqueurs tumoraux et scanner corps entier","Examens de deuxième intention, réservés à un signe d'appel."),
  ("IRM cérébrale, électroencéphalogramme et ponction lombaire","Sans signe neurologique, ils ne sont pas de première intention."),
  ("Test à la corticotropine et cortisol libre urinaire","Réservés à une suspicion d'insuffisance surrénalienne."),
  ("Copeptine et MR-proADM","Marqueurs de recherche, non validés en routine.")],
 "Sans urgence vitale, on va du général au particulier (DX.7) : anamnèse et médicaments, examen complet, puis ECG, ionogramme, calcémie, créatinine, glucose, hémogramme, CRP et TSH. Les examens ciblés suivent les signes.",
 "Un bilan de base normal n'exclut rien : réévaluer à 48–72 heures.",
 PA("ssp-p4","§4 Démarche diagnostique"))

q("D","DX.7 · bilan normal","management","cabinet",
 "Un homme de 79 ans consulte pour un malaise depuis 10 jours. Constantes, examen et bilan de base normaux. Il vit seul, avec une aide à domicile.",
 "Quelle est la conduite la plus appropriée ?",
 [("Revoir à 48 h et à une semaine",""),
  ("Rassurer et clore le dossier","Un bilan de base normal n'exclut pas une maladie."),
  ("Scanner thoraco-abdominal d'emblée","Sans signe d'appel, il n'est pas de première intention."),
  ("Antibiotique empirique","Sans foyer ni gravité, il n'est pas indiqué."),
  ("Hospitalisation systématique","Constantes stables et entourage présent permettent un suivi rapproché.")],
 "La plupart des diagnostics tombent après la première consultation (DX.7) : on revoit le patient à 48 heures et à une semaine, et on envisage la dépression (DX.6) et les médicaments (DX.8).",
 "Le diagnostic des urgences n'est correct que dans 46 % des cas.",
 B(7,10))

q("D","DX.7 · critères de sortie","management","hôpital",
 "Une femme de 85 ans, hospitalisée 4 jours pour une pneumonie traitée, se sent mieux. Constantes stables depuis 24 heures ; elle mange et boit seule. Sa fille demande si elle peut rentrer.",
 "Quel élément faut-il encore vérifier avant la sortie ?",
 [("Mobilité, cognition et médicaments revus",""),
  ("Normalisation complète de la CRP","Elle n'est pas un critère de sortie."),
  ("Radiographie du thorax normalisée","Le contrôle radiologique est différé."),
  ("Deux paires d'hémocultures de contrôle négatives","Pas exigées pour la sortie."),
  ("Absence de toute toux résiduelle","Une toux peut persister plusieurs semaines.")],
 "Critères de retour à domicile : constantes stables 24 heures, cause identifiée et traitée, boisson et alimentation suffisantes, mobilité et cognition évaluées, médicaments revus, entourage organisé, suivi à 48–72 heures (DX.7).",
 "Consultation de suivi à 48–72 heures après la sortie.",
 PA("ssp-p11","§11 Prise en charge"), niv="approfondissement")

# ── DX.8 Médicaments
q("D","DX.8 · thiazide et ISRS","management","cabinet",
 "Une femme de 80 ans se sent confuse et nauséeuse depuis 10 jours. On a ajouté de l'hydrochlorothiazide il y a 3 semaines ; elle prend de la sertraline. Na 126 mmol/L, sans symptôme sévère.",
 "Quelle est la conduite la plus appropriée ?",
 [("Arrêter le thiazide et surveiller la natrémie",""),
  ("Bolus de NaCl 3 %","Réservé aux symptômes sévères."),
  ("Augmenter la sertraline","L'ISRS contribue lui aussi à l'hyponatrémie."),
  ("Ajouter du furosémide","On ne traite pas un effet indésirable par un autre diurétique."),
  ("Poursuivre et refaire le dosage dans 3 mois","Un thiazide est incompatible avec une hyponatrémie symptomatique.")],
 "Malaise apparu après un changement de traitement : chronologie, natrémie, arrêt ou substitution avec le prescripteur (DX.8). Les thiazides provoquent ou aggravent l'hyponatrémie, surtout avec un antidépresseur.",
 "12,2 % des plaintes non spécifiques ont un problème médicamenteux ; 40 % seulement sont reconnus à l'accueil.",
 B(8,13))

q("D","DX.8 · paracétamol","management","urgences",
 "Une femme de 34 ans dit avoir avalé 12 g de paracétamol il y a 2 heures. Elle n'a aucun symptôme. Constantes normales.",
 "Quelle est la conduite la plus appropriée ?",
 [("Paracétamolémie à 4 h, antidote selon la courbe",""),
  ("Retour à domicile, car elle est asymptomatique","L'absence de symptôme ne protège pas."),
  ("Dosage immédiat pour décider","Avant 4 heures, la concentration n'est pas interprétable."),
  ("Naloxone i.v.","Elle antagonise les opioïdes, pas le paracétamol."),
  ("Flumazénil i.v.","Il antagonise les benzodiazépines.")],
 "Un surdosage en paracétamol impose une prise en charge même sans symptôme (DX.8). Concentration plasmatique au moins 4 heures après la prise, puis acétylcystéine selon la courbe ; seuil toxique chez l'adulte 7,5 à 10 g.",
 "Concentration > 200 µg/mL à 4 h : toxique.",
 B(8,13))

q("D","DX.8 vs DX.6 · liste complète","assessment_diagnosis","cabinet",
 "Un homme de 77 ans se sent mal et somnolent depuis 2 semaines. Il dit ne prendre « que ses comprimés pour la tension ». Bilan de base normal. PHQ-2 négatif.",
 "Quelle est la prochaine étape la plus appropriée ?",
 [("Liste complète, y compris sans ordonnance",""),
  ("Diagnostiquer une dépression masquée et traiter","Le PHQ-2 est négatif ; la piste médicamenteuse n'est pas explorée."),
  ("IRM cérébrale","Sans signe focal, elle n'est pas la première étape."),
  ("Polysomnographie","Prématurée avant d'avoir revu les médicaments."),
  ("Arrêter tous les antihypertenseurs","On arrête l'agent suspect identifié, pas tout le traitement.")],
 "Le médecin demande toujours la liste complète des médicaments, y compris sans ordonnance, avant de conclure à une cause non médicamenteuse (DX.8). Les critères STOPP/START repèrent les prescriptions inadaptées.",
 "Reconstituer la chronologie des prises avec l'ordonnance.",
 B(8,13))

# ── DX.9 Viral
q("D","DX.9 · rhinopharyngite","management","cabinet",
 "Un homme de 32 ans a depuis 2 jours de la fièvre à 38,2 °C, une rhinorrhée et un mal de gorge. Constantes normales, examen sans foyer bactérien. Il demande un antibiotique.",
 "Quelle est la conduite la plus appropriée ?",
 [("Paracétamol et consignes écrites",""),
  ("Amoxicilline 1 g trois fois par jour, 7 jours","Le virus ne répond pas à l'antibiotique."),
  ("Oseltamivir","Réservé à la grippe d'un patient à risque."),
  ("Radiographie du thorax","Aucun signe respiratoire bas."),
  ("Hémocultures","Aucun drapeau rouge.")],
 "Sans drapeau rouge ni foyer, le syndrome viral se traite symptomatiquement (DX.9) : paracétamol 500 mg à 1 g par prise, au plus 4 g par jour, consigne écrite de reconsulter.",
 "Un antibiotique ne se prescrit pas sans foyer bactérien prouvé.",
 B(9,13))

q("D","DX.9 · grippe à risque","management","cabinet",
 "Une femme de 71 ans, BPCO, a depuis ce matin une fièvre brutale à 39 °C, des myalgies et une toux sèche, en pleine saison grippale. FR 18/min, PA 132/78 mmHg, SpO2 95 %.",
 "Quelle est la conduite la plus appropriée ?",
 [("Test grippe et oseltamivir 75 mg deux fois par jour",""),
  ("Amoxicilline-clavulanate d'emblée","Aucun foyer bactérien n'est établi."),
  ("Paracétamol seul, sans test","Patiente à risque vue tôt : l'antiviral est indiqué."),
  ("Oseltamivir après 72 heures si persistance","Il se donne idéalement dans les 36 heures."),
  ("Hospitalisation en soins intensifs","Constantes stables : pas d'indication.")],
 "Début brutal en saison grippale chez une patiente à risque : test et antiviral (DX.9). Oseltamivir 75 mg deux fois par jour pendant 5 jours, dès le jour des symptômes ou le lendemain, idéalement dans les 36 heures.",
 "Clairance 30 à 60 mL/min : 30 mg deux fois par jour.",
 B(9,10))

q("D","DX.9 vs DX.10 · fatigue après fièvre","assessment_diagnosis","cabinet",
 "Une femme de 45 ans a eu un syndrome grippal il y a 5 semaines. La fièvre a disparu, mais elle se sent toujours mal et fatiguée. Examen normal.",
 "Quel bilan est le plus approprié ?",
 [("TSH, glycémie, FSC, ferritine",""),
  ("Sérologies virales étendues","Elles ne prouvent pas la cause de la fatigue."),
  ("Scanner thoraco-abdominal","Aucun signe d'appel de cancer."),
  ("Antibiotique d'épreuve","Aucun foyer bactérien."),
  ("Aucun examen, convalescence sans limite","Une fatigue persistante après la fièvre impose une recherche ciblée.")],
 "Une fatigue qui persiste après la fièvre impose de chercher une anémie, une hypothyroïdie ou un diabète (DX.9, DX.10) : TSH, glycémie, FSC, ferritine.",
 "Si fièvre prolongée, amaigrissement ou sueurs nocturnes : bilan élargi (DX.14).",
 B(9,14))

q("D","DX.9 · retour des tropiques","assessment_diagnosis","cabinet",
 "Un homme de 38 ans rentre du Cameroun depuis 9 jours. Il a de la fièvre à 39 °C, des frissons et se sent très mal. Constantes stables, examen sans foyer.",
 "Quel examen faut-il réaliser le jour même ?",
 [("Frottis et test rapide du paludisme",""),
  ("Sérologies virales de contrôle à 3 semaines","Le paludisme ne s'exclut pas en différé."),
  ("Test grippe seul","Un retour de zone tropicale impose d'exclure le paludisme."),
  ("Radiographie du thorax seule","Aucun signe respiratoire."),
  ("Aucun examen : virose probable","Le diagnostic viral est d'exclusion.")],
 "Fièvre au retour des tropiques : frottis et test rapide du paludisme le jour même (DX.9, arbre décisionnel). Le syndrome viral ne se pose qu'après exclusion des drapeaux rouges.",
 "Le frottis se fait le jour même, jamais en différé.",
 B(9,10))

# ── DX.10 Anémie, hypothyroïdie, diabète
q("D","DX.10 · anémie de l'homme","management","cabinet",
 "Un homme de 62 ans se sent mal et essoufflé à l'effort depuis 2 mois. Hb 98 g/L, VGM 72 fL, ferritine 9 µg/L, CRP normale. Pas de saignement visible.",
 "Quelle est la conduite la plus appropriée ?",
 [("Endoscopie digestive",""),
  ("Fer oral seul et contrôle à 3 mois","Il faut d'abord chercher la source digestive."),
  ("Transfusion de 2 concentrés","Anémie bien tolérée, sans signe de gravité."),
  ("Vitamine B12 i.m.","L'anémie est microcytaire avec ferritine basse."),
  ("Échographie pelvienne","Elle ne cherche pas la source chez l'homme.")],
 "Une anémie ferriprive inexpliquée chez l'homme ou la femme ménopausée impose une endoscopie digestive (DX.10) : un tiers ont une lésion. Le fer suit la recherche de la source.",
 "Carence en fer : ferritine < 30 µg/L sans inflammation.",
 B(10,14))

q("D","DX.10 · TSH modérée","management","cabinet",
 "Une femme de 36 ans se sent fatiguée. TSH 7 mU/L, fT4 normale. Pas de goitre. Elle n'a aucun autre symptôme.",
 "Quelle est la conduite la plus appropriée ?",
 [("Contrôle à 2–3 mois (anti-TPO, fT4)",""),
  ("Lévothyroxine 100 µg/j","Dose d'entretien sans indication confirmée."),
  ("Échographie thyroïdienne urgente avec Doppler","Aucun nodule ni goitre."),
  ("Scintigraphie thyroïdienne","Sans place dans l'hypothyroïdie subclinique."),
  ("Liothyronine","Pas de traitement sans confirmation.")],
 "TSH 4,0 à 10 mU/L avec fT4 normale : hypothyroïdie subclinique, à confirmer à 2–3 mois avec anti-TPO et fT4 (ETA 2013) (DX.10).",
 "TSH ≥ 10 mU/L confirmée avant 70 ans : traiter.",
 B(10,14))

q("D","DX.10 vs DX.4 · ferritine en inflammation","assessment_diagnosis","hôpital",
 "Une femme de 70 ans traitée pour une pneumonie a une anémie microcytaire (Hb 102 g/L). Ferritine 180 µg/L, CRP 95 mg/L.",
 "Quelle est l'interprétation la plus appropriée ?",
 [("Carence possible : doser la TSAT",""),
  ("Carence en fer exclue","La ferritine monte avec l'inflammation."),
  ("Anémie hémolytique","Aucun argument pour l'hémolyse."),
  ("Carence en vitamine B12","L'anémie est microcytaire."),
  ("Fer i.v. d'emblée sans autre examen","Aucune carence n'est encore prouvée.")],
 "La ferritine monte avec l'inflammation : une valeur normale n'exclut pas la carence en fer (DX.10). On associe CRP et saturation de la transferrine ; ferritine 30 à 50 µg/L avec TSAT < 20 % évoque la carence (consensus suisse 2019).",
 "Anémie microcytaire avec CRP et ferritine élevées : anémie inflammatoire probable, traiter la cause.",
 B(10,14), niv="approfondissement")

# ── DX.11 Sepsis
q("D","DX.11 · qSOFA à 1","assessment_diagnosis","urgences",
 "Un homme de 83 ans se sent mal depuis hier. T 37,6 °C, FR 20/min, PA 118/70 mmHg, orienté mais lent. Il a un cathéter veineux depuis 5 jours.",
 "Quelle est la prochaine étape la plus appropriée ?",
 [("Lactate et hémocultures",""),
  ("Exclure le sepsis, car le qSOFA est inférieur à 2","Le qSOFA est trop peu sensible pour exclure."),
  ("Retour à domicile avec paracétamol","Un foyer possible chez un patient fragile impose une évaluation."),
  ("Attendre la fièvre avant tout prélèvement","La fièvre peut manquer chez le sujet âgé."),
  ("Procalcitonine seule pour décider","Elle ne remplace ni le lactate ni le jugement clinique.")],
 "Un qSOFA < 2 n'exclut pas le sepsis : c'est un outil de pronostic, non de dépistage (DX.11). On mesure toutes les constantes et le lactate ; on cherche le foyer, ici le cathéter.",
 "La Surviving Sepsis Campaign déconseille le qSOFA comme outil unique de dépistage.",
 B(11,13))

q("D","DX.11 · PAM basse","management","urgences",
 "Une femme de 77 ans en choc septique d'origine urinaire a reçu 30 mL/kg de Ringer-lactate et de la ceftriaxone. PAM 58 mmHg, lactate 3,8 mmol/L.",
 "Quelle est la prochaine étape la plus appropriée ?",
 [("Noradrénaline et soins intensifs",""),
  ("Encore 3 L de cristalloïde","Le vasopresseur vient quand la PAM reste basse après le remplissage."),
  ("Dobutamine seule","La noradrénaline est le vasopresseur de première ligne."),
  ("Arrêter l'antibiotique en attendant la culture","Aucune raison d'interrompre le traitement."),
  ("Corticoïde oral","Pas de place ici en première ligne.")],
 "Si la PAM reste < 65 mmHg malgré le remplissage, noradrénaline en première ligne et soins intensifs (DX.11). Cible : PAM ≥ 65 mmHg.",
 "AIPS : 8 à 12 µg/min au départ chez l'adulte de 70 kg.",
 B(11,13))

q("D","DX.11 vs DX.15 · choc réfractaire","assessment_diagnosis","urgences",
 "Un homme de 70 ans, sous prednisone 10 mg/j depuis 2 ans, est en choc avec fièvre. Malgré remplissage et noradrénaline, la PA reste basse. Na 128, K 5,4 mmol/L.",
 "Quel geste faut-il ajouter ?",
 [("Hydrocortisone 100 mg i.v.",""),
  ("Restriction hydrique","Le patient est en choc."),
  ("Arrêt de la noradrénaline","Elle reste nécessaire."),
  ("Test à la corticotropine avant décision","Le test confirme plus tard ; on ne retarde pas la dose."),
  ("Fludrocortisone per os seule","Elle ne remplace pas le cortisol en urgence.")],
 "Un choc réfractaire chez un patient sous glucocorticoïde au long cours fait suspecter une crise surrénalienne (DX.11, DX.15) : hydrocortisone 100 mg i.v. sans attendre le résultat.",
 "Un déficit en cortisol évolue vers un choc réfractaire aux liquides.",
 PA("ssp-p3","§3 Physiopathologie"), niv="approfondissement")

# ── DX.12 AVC
q("D","DX.12 · vertige continu","assessment_diagnosis","urgences",
 "Un homme de 75 ans a depuis 5 heures un vertige continu, des vomissements et ne peut plus marcher. Nystagmus présent. Pas de déficit moteur. Glycémie normale. Le scanner sans contraste est normal.",
 "Quelle est la prochaine étape la plus appropriée ?",
 [("Test HINTS par un clinicien formé ou IRM",""),
  ("Diagnostic de névrite vestibulaire et retour à domicile","Le tronc cérébral et le cervelet donnent ce tableau."),
  ("Antivertigineux et contrôle chez l'ORL","Le vertige central doit être exclu d'abord."),
  ("Manœuvre de repositionnement d'emblée","Elle vise un vertige positionnel bref, non un vertige continu."),
  ("Conclure à l'absence d'AVC sur le scanner normal","Un scanner normal n'exclut pas un infarctus du tronc cérébral.")],
 "Un vertige continu avec nystagmus et marche impossible n'est pas une névrite avant le test HINTS ou l'IRM (DX.12). Impulsion normale, nystagmus changeant ou skew : cause centrale, IRM.",
 "HINTS : 100 % de sensibilité dans l'étude initiale, chez des cliniciens formés seulement.",
 B(12,14))

q("D","DX.12 · scanner normal","assessment_diagnosis","urgences",
 "Une femme de 81 ans a depuis 2 heures une confusion et une chute avec faiblesse de la main gauche. Glycémie 5,8 mmol/L. Le scanner cérébral sans contraste est normal.",
 "Quelle est l'interprétation la plus appropriée ?",
 [("Infarctus possible malgré le scanner",""),
  ("AVC exclu, chercher une cause métabolique","Le scanner précoce ne montre pas l'infarctus récent."),
  ("Hémorragie probable","Le scanner sans contraste exclut justement l'hémorragie."),
  ("Accès de panique","Diagnostic d'exclusion, inadapté devant un déficit focal."),
  ("Delirium sur infection urinaire","Un déficit focal ne s'explique pas par un delirium.")],
 "Le scanner sans contraste distingue hémorragie et infarctus, mais un scanner normal à la phase aiguë n'exclut pas l'infarctus (DX.12). L'IRM de diffusion est plus sensible ; la décision de thrombolyse se prend dans la fenêtre de 4,5 heures.",
 "AVC manqué dans 64 % des présentations non spécifiques contre 15,3 % en général.",
 B(12,8))

# ── DX.13 SCA
q("D","DX.13 · ECG normal","assessment_diagnosis","urgences",
 "Une femme de 60 ans se sent mal depuis 2 heures, avec une gêne thoracique qui persiste. Le premier ECG est normal.",
 "Quelle est la conduite la plus appropriée ?",
 [("ECG répété avec V7–V9, troponine 0/1 h",""),
  ("Exclure le SCA sur l'ECG normal","Un ECG normal n'exclut pas un SCA."),
  ("Test d'effort immédiat","Contre-indiqué tant que le SCA n'est pas exclu."),
  ("Retour à domicile et contrôle chez le médecin demain","La douleur persiste : le doute impose la surveillance."),
  ("Coronarographie immédiate","Réservée au STEMI ou au très haut risque.")],
 "Un ECG normal n'exclut pas un SCA (DX.13) : l'occlusion de la circonflexe est souvent silencieuse sur 12 dérivations. On répète l'ECG à 15–30 minutes, on ajoute V7–V9 et on dose la troponine hs à 0 et 1 heure.",
 "La troponine hs à 0 et 1 heure tranche ; chaque test a ses propres seuils.",
 B(13,14))

q("D","DX.13 vs DX.11 · troponine isolée","assessment_diagnosis","hôpital",
 "Un homme de 84 ans est hospitalisé pour un sepsis pulmonaire. Il n'a aucune douleur. Troponine hs élevée, stable sur deux dosages. ECG sans modification ischémique.",
 "Quelle est l'interprétation la plus appropriée ?",
 [("Lésion myocardique sans preuve d'infarctus",""),
  ("Infarctus de type 1 à traiter par coronarographie","Une troponine élevée seule n'est pas un infarctus."),
  ("STEMI","Pas de sus-décalage ST."),
  ("Erreur de laboratoire à ignorer","Une lésion myocardique se surveille ; elle n'est pas une erreur."),
  ("Dissection aortique","Rien n'oriente vers une dissection.")],
 "L'infarctus exige une troponine > 99e percentile avec montée ou baisse et un contexte d'ischémie (4e définition universelle, 2018) (DX.13). Sepsis, insuffisance rénale, embolie et myocardite élèvent aussi la troponine.",
 "Seul le profil dynamique avec contexte ischémique compte.",
 B(13,8))

# ── DX.14 Cancer
q("D","DX.14 · adénopathie","assessment_diagnosis","cabinet",
 "Un homme de 66 ans se sent mal depuis 2 mois. Il a perdu 7 kg et transpire la nuit. Ganglion sus-claviculaire gauche dur, fixe, de 2 cm. ACE élevé.",
 "Quel examen pose le diagnostic ?",
 [("Biopsie avec histologie",""),
  ("Répétition de l'ACE à 1 mois","Un marqueur sert au suivi, pas au diagnostic."),
  ("Scanner seul","L'imagerie évoque, elle n'affirme pas."),
  ("TEP-scanner seul","Il oriente la biopsie mais ne prouve pas le cancer."),
  ("Ponction-aspiration cytologique de contrôle à 3 mois","Le délai est inadapté et l'histologie prime.")],
 "Le cancer se prouve par l'histologie, jamais par l'imagerie ou un marqueur seul (DX.14). Masse palpable ou adénopathie : biopsie. Un ganglion sus-claviculaire gauche peut signaler une tumeur abdominale.",
 "Imagerie et avis spécialisé sous 1 à 2 semaines devant perte de poids, adénopathie, sueurs nocturnes.",
 B(14,8))

q("D","DX.14 · syndrome constitutionnel","assessment_diagnosis","cabinet",
 "Une femme de 71 ans se sent mal depuis 3 mois. Elle a perdu 6 kg, n'a plus d'appétit. Hb 104 g/L sans cause trouvée. Examen sans masse ni adénopathie.",
 "Quel examen est le plus approprié ?",
 [("TDM thoraco-abdomino-pelvienne",""),
  ("Panel étendu de marqueurs tumoraux sériques","Ils ne posent pas le diagnostic."),
  ("Réévaluation dans 6 mois","Le délai est incompatible avec un cancer possible."),
  ("Scintigraphie osseuse","Pas d'orientation osseuse."),
  ("PHQ-9 seul","La dépression ne s'envisage qu'après exclusion de la cause organique.")],
 "Syndrome constitutionnel ou anémie sans cause : TDM thoraco-abdomino-pelvienne, puis biopsie du site accessible (DX.14). Si l'imagerie n'est pas conclusive : TEP et avis d'oncologie.",
 "Un patient cancéreux sur dix reçoit son diagnostic aux urgences.",
 B(14,10))

# ── DX.15 Insuffisance surrénalienne
q("D","DX.15 · soluté","management","urgences",
 "Une femme de 45 ans, suivie pour maladie d'Addison, vomit depuis 24 heures. PA 82/50 mmHg, Na 124 mmol/L. Elle vient de recevoir 100 mg d'hydrocortisone i.v.",
 "Quel soluté est le plus approprié ?",
 [("NaCl 0,9 % 1 L en 1 heure",""),
  ("Glucose 5 % seul","Il apporte de l'eau libre et peut aggraver l'hyponatrémie."),
  ("NaCl 3 % en bolus","Réservé à l'hyponatrémie profonde avec symptômes neurologiques."),
  ("Restriction hydrique à 500 mL par jour","Elle est en choc hypovolémique."),
  ("Albumine 20 %","Le cristalloïde isotonique est la première ligne.")],
 "Crise surrénalienne : hydrocortisone 100 mg i.v., puis NaCl 0,9 % 1 L dans la première heure, puis selon les besoins (DX.15). Pas de soluté glucosé seul.",
 "Mesurer la glycémie et le potassium : hypoglycémie et hyperkaliémie menacent la vie.",
 B(15,14))

q("D","DX.15 · substitué qui vomit","management","domicile",
 "Un homme de 52 ans, substitué par hydrocortisone pour une insuffisance surrénalienne primaire, a une gastro-entérite. Il vomit chaque prise depuis ce matin et se sent de plus en plus faible.",
 "Quelle est la conduite la plus appropriée ?",
 [("Hydrocortisone par voie parentérale",""),
  ("Doubler la dose orale","La voie orale échoue chez un patient qui vomit."),
  ("Suspendre l'hydrocortisone jusqu'à la fin des vomissements","L'arrêt déclenche la crise."),
  ("Ajouter de la fludrocortisone seule","Elle ne remplace pas le cortisol."),
  ("Antiémétique et attendre 24 heures","Le délai expose à la crise.")],
 "Un patient substitué qui vomit doit recevoir l'hydrocortisone par voie parentérale (DX.15), car la voie orale échoue. D'où la carte d'urgence, la trousse d'hydrocortisone injectable et la formation aux doses de stress.",
 "Maladie générale sous corticoïde : doubler ou tripler la dose, et passer à l'injection si vomissements.",
 B(15,14))

q("D","DX.15 vs DX.2 · hyponatrémie trompeuse","assessment_diagnosis","hôpital",
 "Une femme de 58 ans se sent mal et a perdu 4 kg. PA 96/60 mmHg couchée, 78/50 debout. Na 129, K 5,6 mmol/L. Pigmentation des plis palmaires et des gencives. On évoque un SIADH.",
 "Quel diagnostic faut-il évoquer en priorité ?",
 [("Insuffisance surrénalienne primaire",""),
  ("SIADH","Le SIADH ne donne ni hypotension orthostatique ni hyperkaliémie."),
  ("Hyponatrémie induite par un thiazide","Elle ne donne pas d'hyperkaliémie ni d'hyperpigmentation."),
  ("Hypothyroïdie","Elle n'explique pas l'hyperkaliémie et la pigmentation."),
  ("Potomanie avec apport hydrique excessif","Elle ne donne pas d'hypotension ni d'hyperkaliémie.")],
 "Hypotension, hyponatrémie et hyperkaliémie : triade de la crise surrénalienne, par déficit en cortisol et en aldostérone (DX.15). L'hyperpigmentation des plis et des gencives signe la forme primaire (excès d'ACTH).",
 "Piège : attribuer l'hyponatrémie à un SIADH ou à un diurétique.",
 PA("ssp-p4","§4 Démarche diagnostique"))

# ═════════════ BLOC R (suite) · MÉCANISMES (AP) et DÉCISIONS DE 2e LIGNE (SPE)
q("R","DX.7 · comportement de maladie","mechanisms","hôpital",
 "Un étudiant demande pourquoi une femme de 80 ans avec une infection débutante se dit « malade » sans fièvre, sans toux ni signe d'organe, avec fatigue, anorexie et retrait.",
 "Quel mécanisme explique le mieux cette sensation de maladie ?",
 [("Cytokines relayées au cerveau par la microglie",""),
  ("Lésion directe des neurones par les bactéries","Il n'y a pas d'infection cérébrale ; le signal est humoral et nerveux."),
  ("Hypoglycémie réactionnelle","Elle donne une confusion aiguë, pas un comportement de retrait."),
  ("Déficit primaire en sérotonine","C'est un mécanisme invoqué pour la dépression, non pour l'infection."),
  ("Hyperthermie centrale","La patiente n'a pas de fièvre.")],
 "Les macrophages libèrent IL-1, IL-6 et TNF ; ces cytokines atteignent le cerveau par le nerf vague et les cellules endothéliales, la microglie les relaie et déclenche le comportement de maladie : fatigue, anorexie, somnolence, retrait (DX.7, Phase A §3).",
 "La réserve du sujet âgé est réduite : une maladie aiguë se résume souvent à la plainte générale.",
 PA("ssp-p3","§3 Physiopathologie"), niv="approfondissement")

q("R","DX.2 · correction trop rapide","mechanisms","hôpital",
 "Une femme de 72 ans, alcoolique, admise avec Na 112 mmol/L, a reçu des perfusions : Na 129 mmol/L 24 heures plus tard. Au 3e jour, elle devient dysarthrique, tétraparétique et somnolente.",
 "Quel mécanisme est le plus probable ?",
 [("Démyélinisation osmotique du tronc cérébral",""),
  ("Œdème cérébral par hyponatrémie persistante","La natrémie a été corrigée, et trop vite."),
  ("AVC hémorragique","Rien n'oriente vers une hémorragie ; la chronologie suit la correction."),
  ("Encéphalopathie hypoglycémique","Le tableau suit l'élévation rapide de la natrémie."),
  ("Méningite","Pas de fièvre ni de raideur.")],
 "Une élévation trop rapide de la natrémie lèse le tronc cérébral : démyélinisation osmotique, avec tétraparésie, dysarthrie et troubles de conscience (DX.2). Ici + 17 mmol/L en 24 heures, au-delà de la limite de 10 mmol/L le premier jour.",
 "Hausse > 10 mmol/L par 24 heures : arrêter et abaisser.",
 PA("ssp-p3","§3 Physiopathologie"), niv="approfondissement")

q("R","DX.15 · pigmentation","mechanisms","cabinet",
 "Une femme de 44 ans se sent mal depuis des mois. Elle a une hyperpigmentation des plis palmaires et des gencives, une hypotension orthostatique et une kaliémie à 5,5 mmol/L.",
 "Quel mécanisme explique l'hyperpigmentation ?",
 [("Excès d'ACTH stimulant les mélanocytes",""),
  ("Déficit en aldostérone","Il explique l'hyperkaliémie et l'hypovolémie, pas la pigmentation."),
  ("Excès de cortisol","Le cortisol manque dans ce tableau."),
  ("Hémochromatose associée","Rien ne l'évoque."),
  ("Photosensibilisation médicamenteuse","Les gencives et les plis ne sont pas exposés au soleil.")],
 "Dans l'insuffisance surrénalienne primaire, le cortisol bas lève le frein sur l'hypophyse : l'ACTH en excès stimule les mélanocytes (DX.15). L'aldostérone manque aussi : hyponatrémie, hyperkaliémie, hypotension.",
 "Pas d'hyperpigmentation dans la forme secondaire, notamment après des corticoïdes.",
 PA("ssp-p7","§7 Approche syndromique"), niv="approfondissement")

q("R","DX.11 · définition Sepsis-3","assessment_diagnosis","hôpital",
 "Un homme de 75 ans a une pneumonie. Ses plaquettes passent de 220 à 95 G/L et sa créatinine de 85 à 190 µmol/L en 24 heures. Il reste normotendu.",
 "Quelle est la classification la plus appropriée ?",
 [("Sepsis",""),
  ("Pneumonie simple","Une dysfonction d'organe nouvelle est présente."),
  ("Choc septique","Il exige un vasopresseur et un lactate > 2 mmol/L malgré le remplissage."),
  ("SIRS","Le SIRS seul ne définit plus le sepsis."),
  ("Bactériémie","Elle n'est ni nécessaire ni suffisante.")],
 "Sepsis-3 (2016) : infection suspectée ou prouvée avec hausse du SOFA ≥ 2 points (DX.11). Ici coagulation et rein ajoutent chacun des points. Cette hausse s'associe à une mortalité hospitalière > 10 %.",
 "La fièvre seule, le SIRS, un qSOFA < 2 ou une CRP élevée ne suffisent pas.",
 B(11,8), niv="approfondissement")

q("R","DX.4 · pourquoi pas de fièvre","mechanisms","EMS",
 "Une infirmière d'EMS s'étonne qu'une résidente de 91 ans avec une pneumonie radiologique n'ait jamais eu de fièvre.",
 "Quelle explication est la plus juste ?",
 [("Réponse inflammatoire atténuée avec l'âge",""),
  ("Absence probable d'infection bactérienne active","L'absence de fièvre n'exclut pas l'infection."),
  ("Prise cachée d'antipyrétique","Hypothèse sans argument."),
  ("Hypothermie de l'EMS","Ce n'est pas l'explication habituelle."),
  ("Infection purement virale","La fièvre ne distingue pas le virus de la bactérie.")],
 "Chez le sujet âgé, la réponse inflammatoire est atténuée : la fièvre peut manquer et la plainte reste isolée (DX.4). Les infections sont la catégorie de diagnostics la plus représentée dans les plaintes non spécifiques.",
 "82 ans, se sent mal, pas de fièvre : l'infection n'est pas exclue.",
 B(4,14), niv="approfondissement")

q("R","DX.9 · procalcitonine","management","cabinet",
 "Une femme de 39 ans a une toux fébrile depuis 3 jours, sans signe de gravité ni foyer à l'auscultation. Procalcitonine 0,08 µg/L.",
 "Quelle décision est la plus appropriée ?",
 [("Pas d'antibiotique",""),
  ("Amoxicilline 7 jours","PCT ≤ 0,1 µg/L : antibiotique fortement déconseillé."),
  ("Lévofloxacine 7 jours","Aucune indication."),
  ("Hospitalisation pour antibiotique i.v.","Aucun signe de gravité."),
  ("Doxycycline en réserve","La PCT très basse ne justifie aucun antibiotique.")],
 "Étude suisse de premier recours : PCT ≤ 0,1 µg/L antibiotique fortement déconseillé ; ≤ 0,25 déconseillé ; > 0,25 recommandé (DX.9). La stratégie réduit les prescriptions de 72 % sans nuire à l'évolution.",
 "La PCT guide ; elle ne remplace pas la recherche des drapeaux rouges.",
 B(9,8), niv="approfondissement")

q("R","DX.13 · infarctus de type 2","mechanisms","hôpital",
 "Un homme de 79 ans hospitalisé pour méléna a une Hb à 62 g/L. Il se sent mal, avec une oppression thoracique. Troponine hs en montée, sous-décalage ST diffus.",
 "Quel mécanisme est le plus probable ?",
 [("Déséquilibre apport-besoin (type 2)",""),
  ("Rupture de plaque avec thrombus (type 1)","Le contexte d'anémie aiguë sévère oriente vers un déséquilibre, sans rupture."),
  ("Infarctus lié à une angioplastie","Aucun geste coronaire récent."),
  ("Mort cardiaque avant prélèvement (type 3)","Le patient est vivant et la troponine est dosée."),
  ("Myocardite virale","Le contexte hémorragique explique l'ischémie.")],
 "4e définition universelle : le type 2 relève d'un déséquilibre entre apport et besoins en oxygène, sans rupture de plaque, par exemple anémie sévère, tachyarythmie ou hypotension (DX.13).",
 "On traite d'abord la cause du déséquilibre (ici le saignement), pas une plaque.",
 B(13,8), niv="approfondissement")

q("R","DX.6 · délai de l'antidépresseur","management","cabinet",
 "Une femme de 54 ans a débuté la sertraline 50 mg pour une dépression il y a 10 jours. Elle est déçue : « je ne sens encore rien ».",
 "Quelle information est la plus juste ?",
 [("Effet attendu en 2 à 4 semaines",""),
  ("Échec : changer de molécule maintenant","Le délai d'action n'est pas encore écoulé."),
  ("Arrêter brutalement et réévaluer","Un arrêt brutal est à éviter."),
  ("Doubler aussitôt à 200 mg","Les paliers sont d'au plus 50 mg par semaine."),
  ("Ajouter une benzodiazépine au long cours","Elle ne traite pas la dépression.")],
 "La sertraline agit en 2 à 4 semaines (DX.6). Paliers de 50 mg par semaine, maximum 200 mg ; poursuite au moins 6 mois après la rémission. Réévaluer le PHQ-9 à 2–4 semaines.",
 "Pas de baisse du PHQ-9 à 2–4 semaines : changer de stratégie.",
 B(6,13), niv="approfondissement")

q("R","DX.11 · choc septique","assessment_diagnosis","urgences",
 "Une femme de 68 ans a une péritonite. Après 30 mL/kg de cristalloïde, il faut de la noradrénaline pour maintenir une PAM ≥ 65 mmHg ; lactate 3,2 mmol/L.",
 "Quelle est la classification la plus appropriée ?",
 [("Choc septique",""),
  ("Sepsis sans choc","Le vasopresseur et le lactate élevé malgré le remplissage définissent le choc."),
  ("Choc hypovolémique pur","Le remplissage adéquat n'a pas corrigé la pression."),
  ("Choc cardiogénique","Le contexte est infectieux."),
  ("Bactériémie isolée","Elle ne décrit pas la défaillance circulatoire.")],
 "Choc septique (Sepsis-3) : vasopresseur nécessaire pour une PAM ≥ 65 mmHg et lactate > 2 mmol/L malgré un remplissage adéquat (DX.11). Mortalité hospitalière > 40 %.",
 "Contrôler la source (ici chirurgie) dès que possible ; réévaluer l'antibiotique à 48–72 heures.",
 B(11,8), niv="specialiste", spe="Médecine intensive")

q("R","DX.12 · occlusion de gros vaisseau","management","urgences",
 "Une femme de 70 ans a une hémiplégie droite et une aphasie depuis 2 heures. Scanner sans hémorragie ; altéplase débutée. L'angio-scanner montre une occlusion de l'artère cérébrale moyenne proximale.",
 "Quelle est la prochaine étape la plus appropriée ?",
 [("Thrombectomie et transfert immédiat",""),
  ("Attendre l'effet de l'altéplase 24 heures","La thrombectomie s'ajoute à la thrombolyse."),
  ("Aspirine 300 mg immédiatement","Ni aspirine ni anticoagulant parentéral dans les 24 heures suivant la thrombolyse."),
  ("IRM de contrôle à 48 heures","Elle ne traite pas l'occlusion."),
  ("Héparine i.v. à dose curative","Contre-indiquée après thrombolyse.")],
 "Occlusion d'un gros vaisseau : thrombectomie, même après thrombolyse, avec transfert immédiat (DX.12). Recommandée jusqu'à 6 heures (preuve élevée), puis de 6 à 24 heures selon les critères des essais.",
 "Pas d'aspirine ni d'anticoagulant parentéral dans les 24 heures après altéplase.",
 B(12,10), niv="specialiste", spe="Neurologie")

q("R","DX.15 · confirmer le diagnostic","assessment_diagnosis","hôpital",
 "Un homme de 49 ans stabilisé après une crise surrénalienne présumée doit être exploré. Il ne reçoit plus d'hydrocortisone depuis la veille, sur avis endocrinologique.",
 "Quel examen est la référence pour poser le diagnostic ?",
 [("Test à la corticotropine 250 µg",""),
  ("Cortisol plasmatique aléatoire en soirée","Un cortisol isolé ne conclut pas."),
  ("Natrémie et kaliémie","Elles orientent sans prouver."),
  ("Scanner des surrénales","Il cherche la cause une fois le diagnostic posé."),
  ("Anticorps anti-TPO","Ils concernent la thyroïde.")],
 "Le test à la corticotropine de 250 µg est l'examen de référence (Endocrine Society 2016) (DX.15). Cortisol à 30 minutes > 500 nmol/L : fonction normale ; < 500 nmol/L : insuffisance. ACTH élevée : forme primaire.",
 "Forme primaire : hydrocortisone et fludrocortisone ; forme centrale : hydrocortisone seule.",
 B(15,8), niv="specialiste", spe="Endocrinologie")

q("R","DX.13 · score GRACE","management","hôpital",
 "Un homme de 78 ans a un NSTEMI confirmé (troponine hs dynamique). Il est stable, sans douleur réfractaire ni arythmie. Score GRACE 156.",
 "Quel délai de coronarographie est le plus approprié ?",
 [("Sous 24 heures",""),
  ("Sous 2 heures","Réservé au très haut risque : choc, douleur réfractaire, arythmie, œdème."),
  ("Programmée à 3 mois","Un GRACE > 140 impose un délai court."),
  ("Aucune, traitement médical seul","L'infarctus confirmé relève d'une stratégie invasive."),
  ("Après un test d'effort","Le test d'effort n'a pas sa place dans un NSTEMI confirmé.")],
 "NSTE-ACS à haut risque (infarctus confirmé, ST dynamique ou GRACE > 140) : coronarographie sous 24 heures ; très haut risque : sous 2 heures (DX.13, ESC 2023).",
 "GRACE : âge, FC, PA, créatinine, Killip, arrêt cardiaque, ST, troponine.",
 B(13,14), niv="specialiste", spe="Cardiologie")

q("R","DX.7 · confusion fluctuante","assessment_diagnosis","EMS",
 "Une résidente d'EMS de 87 ans est apathique depuis 2 jours, avec des moments de lucidité. Elle ne peut pas compter de 20 à 1 et son discours est décousu. Constantes et glycémie normales.",
 "Quelle démarche est la plus appropriée ?",
 [("CAM, puis cause du delirium",""),
  ("Diagnostic de démence évolutive","Le début aigu et la fluctuation orientent vers un delirium."),
  ("Dépression : PHQ-9 et antidépresseur","Le delirium hypoactif imite l'apathie dépressive."),
  ("Neuroleptique et observation","Le traitement vise d'abord la cause."),
  ("Scanner cérébral seul","Sans signe focal, on cherche d'abord les causes fréquentes.")],
 "CAM : début aigu, fluctuation, inattention, avec pensée désorganisée ou conscience altérée (sensibilité 94–100 %, spécificité 90–95 %) (DX.7). Delirium : chercher infection, trouble ionique, médicament, rétention urinaire.",
 "Le delirium hypoactif passe inaperçu ; il précède souvent la fièvre.",
 PA("ssp-p6","§6 Examen physique"), niv="specialiste", spe="Gériatrie")

q("R","DX.14 · neutropénie fébrile","management","urgences",
 "Une femme de 59 ans, sous chimiothérapie pour un cancer du sein, se sent mal depuis ce matin. T 38,7 °C. PNN 0,3 G/L. PA 112/70 mmHg.",
 "Quelle est la conduite la plus appropriée ?",
 [("Hémocultures et antibiotique dans l'heure",""),
  ("Attendre le résultat des cultures","On ne retarde pas l'antibiotique."),
  ("Antipyrétique et contrôle le lendemain","La neutropénie fébrile évolue en quelques heures."),
  ("Chercher d'abord un foyer par scanner thoraco-abdominal","L'antibiotique ne doit pas attendre le foyer."),
  ("Facteur de croissance seul","Il ne remplace pas l'antibiotique.")],
 "Neutropénie fébrile (ESMO 2016) : PNN < 0,5 G/L et T > 38,5 °C, ou > 38,0 °C à deux reprises sur 2 heures (DX.14). Antibiotique à large spectre dans l'heure, sans attendre les résultats.",
 "Fièvre sous chimiothérapie : neutropénie fébrile jusqu'à preuve du contraire.",
 B(14,14), niv="specialiste", spe="Oncologie")

# ═════════════ BLOC D (suite) · SPE
q("D","DX.5 · dose de prednisone","management","policlinique",
 "Une femme de 74 ans a une polymyalgie rhumatismale confirmée. Infection et cancer ont été exclus. Elle n'a ni céphalée, ni trouble visuel, ni claudication de la mâchoire.",
 "Quelle dose initiale de prednisone est la plus appropriée ?",
 [("15 à 25 mg par jour",""),
  ("40 à 60 mg par jour","Dose de l'artérite à cellules géantes."),
  ("5 mg par jour","Dose insuffisante pour contrôler l'inflammation."),
  ("Bolus de 1 g de méthylprednisolone","Aucune menace visuelle."),
  ("Aucun corticoïde, AINS seuls","La polymyalgie relève du glucocorticoïde.")],
 "Polymyalgie rhumatismale : équivalent prednisone 15 à 25 mg par jour ; artérite à cellules géantes : 40 à 60 mg (DX.5). On exclut d'abord infection et cancer.",
 "Toute apparition de trouble visuel sous traitement impose un avis sous 24 heures.",
 B(5,14), niv="specialiste", spe="Rhumatologie")

q("D","DX.6 · escitalopram âgé","management","cabinet",
 "Un homme de 78 ans a une dépression confirmée. Son ECG ne montre pas d'allongement du QT. On choisit l'escitalopram.",
 "Quelle dose maximale est la plus appropriée ?",
 [("10 mg par jour",""),
  ("20 mg par jour","Dose maximale de l'adulte de moins de 65 ans."),
  ("40 mg par jour","Au-delà de toute dose autorisée."),
  ("5 mg une fois par semaine","Schéma sans fondement."),
  ("Même dose que l'adulte jeune, sans limite","L'AIPS limite la dose après 65 ans.")],
 "Escitalopram : maximum 20 mg par jour, 10 mg chez le sujet de plus de 65 ans ; contre-indiqué en cas d'allongement du QT connu (AIPS Cipralex®) (DX.6).",
 "ECG avant un ISRS à risque de QT chez le sujet âgé.",
 B(6,14), niv="specialiste", spe="Psychogériatrie")

q("D","DX.9 · mononucléose précoce","assessment_diagnosis","cabinet",
 "Une étudiante de 19 ans a depuis 4 jours une fièvre, une angine et des adénopathies cervicales postérieures. Rate palpable. Le test hétérophile est négatif.",
 "Quelle est la conduite la plus appropriée ?",
 [("Répéter le test ou sérologie VCA",""),
  ("Exclure la mononucléose","Le test est faussement négatif en première semaine."),
  ("Amoxicilline pour angine bactérienne","La rate palpable et les adénopathies postérieures orientent vers la mononucléose."),
  ("Corticoïde systématique","Traitement symptomatique dans la forme simple."),
  ("Reprise du sport de contact","La rate peut se rompre : pas de sport pendant 3 semaines.")],
 "Test hétérophile : sensibilité 87 %, spécificité 91 %, mais faux négatif en première semaine (DX.9). On répète ou on fait la sérologie VCA. Traitement symptomatique ; pas de sport pendant 3 semaines.",
 "FSC : lymphocytes > 40 % et atypiques > 10 % ; ALAT élevées si le test est négatif.",
 B(9,14), niv="specialiste", spe="Infectiologie")

q("D","DX.3 · légionellose","management","hôpital",
 "Un homme de 57 ans, fumeur, revient d'un hôtel. Pneumonie bilatérale, confusion, hyponatrémie, CRB-65 à 2. L'antigène urinaire de légionelle est négatif.",
 "Quelle est la conduite la plus appropriée ?",
 [("Bêta-lactamine plus macrolide",""),
  ("Exclure la légionellose","L'antigène urinaire ne détecte que le sérogroupe 1."),
  ("Amoxicilline seule à domicile","Gravité et suspicion de légionelle imposent un macrolide et l'hôpital."),
  ("Oseltamivir seul","Rien n'oriente vers une grippe isolée."),
  ("Pas d'antibiotique avant la culture","On ne retarde pas le traitement.")],
 "L'antigène urinaire ne détecte que le sérogroupe 1 : un test négatif n'exclut pas la légionellose (DX.3). Le macrolide s'ajoute en cas de gravité ou de légionellose.",
 "Fièvre persistante après 72 heures : chercher empyème, résistance ou autre diagnostic.",
 B(3,14), niv="specialiste", spe="Infectiologie")

# ═════════════ BLOC P · PIÈGES & ALARMES
q("P","DX.1 · bactériurie asymptomatique","management","EMS",
 "Une résidente d'EMS de 86 ans est confuse depuis 2 jours. Pas de brûlure, pas de fièvre, pas de douleur lombaire. Constantes stables. La bandelette urinaire montre leucocytes et nitrites positifs.",
 "Quelle est la conduite la plus appropriée ?",
 [("Chercher une autre cause, sans antibiotique",""),
  ("Fosfomycine 3 g en dose unique","Une bandelette positive sans symptôme est une bactériurie asymptomatique."),
  ("Ceftriaxone i.v. pour un urosepsis présumé","Constantes stables, pas de signe de sepsis."),
  ("ECBU de contrôle chaque semaine jusqu'à négativation","Le dépistage de la bactériurie asymptomatique n'est pas recommandé."),
  ("Sonde urinaire à demeure","Geste sans indication, source d'infection.")],
 "Chez le sujet âgé confus sans symptôme local, une bandelette positive ne prouve pas la cause (DX.1). La bactériurie asymptomatique ne se traite pas, sauf avant un geste urologique invasif avec saignement muqueux (IDSA 2019). Chercher infection d'un autre site, trouble ionique, médicament, rétention urinaire.",
 "Traiter une bactériurie asymptomatique est le piège classique de l'examen.",
 PA("ssp-p14","§14 Pièges"))

q("P","DX.1 · nitrofurantoïne et rein","management","cabinet",
 "Une femme de 76 ans a une cystite simple. DFGe 40 mL/min. Elle est allergique à la fosfomycine. On envisage la nitrofurantoïne.",
 "Quelle est la conduite la plus appropriée pour la nitrofurantoïne ?",
 [("Ne pas la prescrire à ce DFGe",""),
  ("La prescrire à dose habituelle","L'AIPS la contre-indique sous 45 mL/min."),
  ("La prescrire à demi-dose","Une réduction de dose ne lève pas la contre-indication."),
  ("La prescrire si la culture est sensible","La sensibilité du germe ne change pas la contre-indication rénale."),
  ("La prescrire en dose unique","Aucun schéma ne la rend acceptable sous 45 mL/min.")],
 "L'AIPS contre-indique la nitrofurantoïne quand le DFGe est inférieur à 45 mL/min (DX.1). On choisit un autre antibiotique adapté à la fonction rénale.",
 "Bactrim® est contre-indiqué au 3e trimestre de grossesse (ictère nucléaire) et élève la kaliémie.",
 B(1,14), niv="approfondissement")

q("P","DX.2 · perfusion de potassium","management","hôpital",
 "Un homme de 71 ans, après une diarrhée, se sent faible. K 2,9 mmol/L, créatinine normale. On prescrit du chlorure de potassium i.v.",
 "Quelle modalité est la plus appropriée ?",
 [("Dilué, au plus 10 mmol/h, sous ECG",""),
  ("Bolus i.v. direct de 20 mmol en 5 minutes","Un bolus non dilué expose à l'arrêt cardiaque."),
  ("40 mmol/h par voie périphérique","Débit très supérieur à la limite AIPS."),
  ("Sans surveillance ECG","L'ECG est nécessaire pendant la perfusion."),
  ("Concentré non dilué en seringue","Le potassium se donne toujours dilué.")],
 "Chlorure de potassium : toujours dilué ; si K > 2,5 mmol/L, au plus 10 mmol/h et 200 mmol par jour, 40 mmol/L de solution, avec ECG (DX.2).",
 "L'AIPS contre-indique le potassium en insuffisance rénale.",
 PA("ssp-p14","§14 Pièges"), niv="approfondissement")

q("P","DX.2 · tolvaptan","management","hôpital",
 "Une femme de 79 ans a vomi pendant 3 jours. Muqueuses sèches, hypotension orthostatique. Na 127 mmol/L, sans symptôme neurologique.",
 "Quelle mesure est contre-indiquée ?",
 [("Tolvaptan",""),
  ("Soluté isotonique","Traitement adapté à l'hypovolémie."),
  ("Mesure de l'osmolalité et de la natriurèse","Bilan étiologique recommandé."),
  ("Arrêt d'un éventuel thiazide","Mesure utile."),
  ("Contrôle répété de la natrémie","Surveillance indispensable.")],
 "Hyponatrémie hypovolémique : remplir par soluté isotonique (DX.2). Le tolvaptan est contre-indiqué en cas d'hypovolémie (AIPS Samsca®).",
 "Limite de correction : moins de 10 à 12 mmol/L en 24 heures.",
 B(2,14), pol="negative", niv="specialiste", spe="Néphrologie")

q("P","DX.13 · sildénafil","management","urgences",
 "Un homme de 64 ans se sent mal avec une oppression thoracique. ECG : sous-décalage ST. Il a pris du sildénafil il y a 6 heures. PA 128/78 mmHg.",
 "Quel médicament est contre-indiqué chez lui ?",
 [("Nitroglycérine",""),
  ("Acide acétylsalicylique","Indiqué dans le SCA sans contre-indication ici."),
  ("Énoxaparine","Utilisée dans le NSTE-ACS."),
  ("Oxygène si SpO2 < 90 %","Indication correcte."),
  ("Atorvastatine","Indiquée après un SCA.")],
 "L'AIPS contre-indique les nitrés avec les inhibiteurs de la PDE5 : hypotension sévère (DX.13).",
 "Toujours demander la prise de sildénafil ou tadalafil avant un nitré.",
 B(13,14), pol="negative", niv="approfondissement")

q("P","DX.13 · oxygène","management","urgences",
 "Une femme de 74 ans a un NSTEMI. Elle n'est pas dyspnéique. SpO2 96 % à l'air ambiant.",
 "Quelle conduite pour l'oxygène est la plus appropriée ?",
 [("Pas d'oxygène",""),
  ("Oxygène 6 L/min systématique","L'oxygène se donne seulement si la SpO2 est < 90 %."),
  ("Masque à haute concentration","Sans indication."),
  ("Oxygène pour une SpO2 cible de 100 %","Aucun bénéfice démontré."),
  ("Ventilation non invasive","Sans indication.")],
 "Dans le SCA, l'oxygène se donne seulement si la SpO2 est inférieure à 90 % (DX.13).",
 "Objectif LDL après SCA : < 1,4 mmol/L et baisse ≥ 50 %.",
 B(13,14), niv="approfondissement")

q("P","DX.12 · AVK et thrombolyse","management","urgences",
 "Un homme de 73 ans sous acénocoumarol a une hémiparésie depuis 90 minutes. Scanner sans hémorragie. INR 1,6. Plaquettes 210 G/L. PA 170/95 mmHg.",
 "Quelle est l'interprétation la plus appropriée ?",
 [("Altéplase contre-indiquée par l'INR",""),
  ("Altéplase possible, l'INR est sous 2","Le seuil est un INR supérieur à 1,3."),
  ("Baisser d'abord la PA sous 140/90 mmHg","On traite la PA si elle dépasse 185/110 mmHg."),
  ("Altéplase après une dose de vitamine K","La correction ne lève pas la contre-indication dans la fenêtre."),
  ("Plaquettes insuffisantes","Le seuil est 100 G/L ; elles sont normales.")],
 "INR > 1,3 : contre-indication à l'altéplase (AIPS) (DX.12). Plaquettes < 100 000/mm³ : contre-indication ; PA > 185/110 mmHg à traiter avant thrombolyse.",
 "Une occlusion de gros vaisseau reste accessible à la thrombectomie.",
 B(12,14), niv="approfondissement")

q("P","DX.14 · zolédronate et Ringer","management","hôpital",
 "Une femme de 70 ans a une hypercalcémie maligne (calcémie corrigée 3,3 mmol/L). Elle est hydratée par Ringer-lactate. On prescrit 4 mg de zolédronate.",
 "Quelle modalité de perfusion est la plus appropriée ?",
 [("Voie séparée, NaCl 0,9 %, ≥ 15 min",""),
  ("Dans la même poche de Ringer-lactate","Aucune solution contenant du calcium ne doit être mélangée."),
  ("En bolus i.v. de 1 minute","La perfusion dure au moins 15 minutes."),
  ("Par voie sous-cutanée","Voie non prévue."),
  ("Avant toute hydratation","L'état hydrique se contrôle avant la perfusion.")],
 "Zolédronate 4 mg dans 100 mL de NaCl 0,9 % ou de glucose 5 %, en au moins 15 minutes, voie séparée ; jamais avec du Ringer-lactate, qui contient du calcium (DX.14).",
 "Contrôler calcémie et créatinine avant et après.",
 PA("ssp-p14","§14 Pièges"), niv="approfondissement")

q("P","DX.10 vs DX.15 · thyroïde et surrénale","management","hôpital",
 "Une femme de 51 ans a une hypothyroïdie manifeste (TSH 38 mU/L, fT4 basse). Elle a aussi une hypotension, une hyponatrémie et un cortisol du matin bas avec ACTH élevée.",
 "Quel est l'ordre de traitement le plus approprié ?",
 [("Hydrocortisone d'abord, puis lévothyroxine",""),
  ("Lévothyroxine d'abord","Contre-indiquée en cas d'insuffisance surrénalienne non traitée."),
  ("Les deux à pleine dose le même jour","Le cortisol doit être substitué d'abord."),
  ("Lévothyroxine seule, car la TSH est très élevée","Elle peut précipiter une crise surrénalienne."),
  ("Fludrocortisone seule","Elle ne remplace pas le cortisol.")],
 "La lévothyroxine est contre-indiquée en cas d'insuffisance surrénalienne non traitée : il faut d'abord substituer le cortisol (DX.10, DX.15).",
 "Lévothyroxine à jeun, 2 heures avant le fer et le calcium ; 25 µg au départ chez le sujet âgé.",
 PA("ssp-p14","§14 Pièges"), niv="specialiste", spe="Endocrinologie")

q("P","DX.10 · HbA1c et anémie","assessment_diagnosis","cabinet",
 "Un homme de 67 ans se sent mal et urine beaucoup. Hb 84 g/L. HbA1c 5,4 %. Glycémies capillaires répétées à 14–17 mmol/L.",
 "Quelle est l'interprétation la plus appropriée ?",
 [("HbA1c faussée : se fier aux glycémies",""),
  ("Diabète exclu, car l'HbA1c est normale","L'anémie fausse l'HbA1c."),
  ("Hypercalcémie seule en cause","Les glycémies élevées expliquent la polyurie."),
  ("Erreur de glucomètre","Les mesures sont répétées et concordantes."),
  ("Potomanie","Elle n'élève pas la glycémie.")],
 "Une anémie fausse l'HbA1c : on se fie aux glycémies (DX.10). Glycémie ≥ 11,1 mmol/L avec symptômes = diabète (ADA).",
 "Polyurie et soif : hyperglycémie ou hypercalcémie.",
 B(10,14), niv="approfondissement")

q("P","DX.15 · cortisol normal en choc","assessment_diagnosis","urgences",
 "Une femme de 62 ans, sous prednisone au long cours arrêtée il y a 1 semaine, est en choc. Son cortisol plasmatique aléatoire revient « dans la norme du laboratoire ».",
 "Quelle est l'interprétation la plus appropriée ?",
 [("Crise non exclue : on poursuit",""),
  ("Crise exclue, arrêter l'hydrocortisone","Un cortisol normal est insuffisant en situation de choc."),
  ("Diagnostic de choc septique certain","Le cortisol ne permet pas cette conclusion."),
  ("Répéter le dosage avant tout traitement","On traite sans attendre."),
  ("Test à la corticotropine immédiat en choc","Le test se fait après stabilisation.")],
 "Un cortisol aléatoire « normal » en plein choc n'exclut pas la crise surrénalienne : il est insuffisant pour le stress (DX.15). On traite, puis on confirme par le test à la corticotropine après récupération.",
 "Un cortisol bas sous glucocorticoïde n'a pas de valeur non plus.",
 B(15,14), niv="approfondissement")

q("P","DX.8 · flumazénil et épilepsie","management","urgences",
 "Une femme de 45 ans, épileptique traitée au long cours par clonazépam, est somnolente après une prise excessive. FR 12/min, SpO2 95 %.",
 "Quelle conduite est la plus appropriée ?",
 [("Soutien et surveillance",""),
  ("Flumazénil 0,3 mg i.v.","Déconseillé chez l'épileptique sous benzodiazépines : risque de convulsions."),
  ("Naloxone 2 mg","Elle cible les opioïdes."),
  ("Intubation orotrachéale immédiate","La ventilation est conservée."),
  ("Acétylcystéine","Antidote du paracétamol.")],
 "Coma sans myosis après sédatif : benzodiazépine possible ; soutien, flumazénil seulement si indiqué (DX.8). Chez l'épileptique traité par benzodiazépines, il est déconseillé, car il peut déclencher des convulsions.",
 "Flumazénil en soins intensifs : 0,3 mg i.v., jusqu'à 2 mg au total.",
 B(8,14), niv="specialiste", spe="Toxicologie clinique")

q("P","DX.8 · syndrome sérotoninergique","assessment_diagnosis","urgences",
 "Une femme de 70 ans sous sertraline a reçu du tramadol il y a 2 jours. Elle est agitée, en sueur, T 38,6 °C, FC 118/min, avec un clonus des membres inférieurs.",
 "Quel diagnostic est le plus probable ?",
 [("Syndrome sérotoninergique",""),
  ("Sepsis urinaire","Le clonus après un nouvel agent sérotoninergique oriente ailleurs."),
  ("Surdosage en tramadol (opioïde)","Il donne myosis et bradypnée, non clonus et agitation."),
  ("Crise d'anxiété","Fièvre et clonus ne sont pas anxieux."),
  ("Hypoglycémie","Elle ne donne pas de clonus ni de fièvre.")],
 "Excitation neuromusculaire, dysautonomie et conscience altérée après un traitement sérotoninergique nouveau ou modifié : syndrome sérotoninergique (critères de Hunter) (DX.8). Arrêt, soutien, avis spécialisé.",
 "Une fièvre isolée ne suffit pas ; c'est le clonus qui oriente.",
 B(8,10), niv="approfondissement")

q("P","DX.14 · lyse tumorale","management","hôpital",
 "Un homme de 46 ans avec un lymphome à forte charge tumorale a, 48 heures après le début de la chimiothérapie, une oligurie, K 6,1 mmol/L et une hyperuricémie.",
 "Quelle mesure est la plus appropriée ?",
 [("Hydratation et rasburicase",""),
  ("Alcalinisation des urines","Elle n'est pas recommandée."),
  ("Restriction hydrique","L'hydratation est la base du traitement."),
  ("Poursuivre sans changement","Une lyse tumorale clinique impose d'agir."),
  ("Allopurinol seul à forte dose","La rasburicase est le traitement de l'hyperuricémie aiguë ici.")],
 "Lyse tumorale (Cairo-Bishop) : hyperuricémie, hyperkaliémie, hyperphosphatémie, hypocalcémie, avec atteinte rénale pour la forme clinique (DX.14). Hydratation et rasburicase 0,20 mg/kg/j, ECG ; pas d'alcalinisation.",
 "Rasburicase : jusqu'à 7 jours, sous surveillance d'un hématologue expérimenté.",
 B(14,14), niv="specialiste", spe="Oncologie")

q("P","DX.13 · dissection","assessment_diagnosis","urgences",
 "Un homme de 69 ans se sent mal avec une douleur thoracique « déchirante » irradiant dans le dos. PA 168/90 mmHg au bras droit, 128/70 mmHg au gauche. ECG : sus-décalage discret en DIII.",
 "Quelle est la prochaine étape la plus appropriée ?",
 [("Angio-CT avant tout antithrombotique",""),
  ("Aspirine 300 mg et héparine","Les antithrombotiques sont dangereux dans une dissection."),
  ("Fibrinolyse dans les 10 minutes","Elle est dangereuse dans une dissection."),
  ("Troponine à 1 heure et observation en box","Le tableau impose une imagerie urgente."),
  ("Test d'effort","Contre-indiqué en urgence.")],
 "Douleur déchirante, pouls asymétriques ou différence de PA entre les bras : suspecter une dissection aortique et faire un angio-CT avant tout antithrombotique (DX.13).",
 "Un sus-décalage avec troponine restée normale sur des dosages répétés doit aussi faire chercher une dissection.",
 B(13,13), niv="specialiste", spe="Cardiologie")

q("P","DX.4 · matériel infecté","management","hôpital",
 "Une femme de 67 ans en hémodialyse par cathéter veineux central a une fièvre et des frissons au branchement. Les hémocultures poussent à Staphylococcus aureus. Antibiotique i.v. débuté.",
 "Quelle mesure est indispensable ?",
 [("Retirer le cathéter",""),
  ("Verrou antibiotique en gardant le cathéter","L'antibiotique seul échoue sur le matériel infecté."),
  ("Antibiothérapie orale de 5 jours","Insuffisante pour une bactériémie sur matériel."),
  ("Arrêter l'antibiotique si la fièvre cède","La source reste en place."),
  ("Hémocultures à répéter avant de décider","Elles n'autorisent pas à retarder le contrôle de la source.")],
 "On draine ou on retire le matériel infecté, car l'antibiotique seul échoue (DX.4). Le contrôle de la source fait partie du traitement de l'infection.",
 "Toujours chercher le foyer : poumon, voie urinaire, peau, abdomen, cœur, cathéter.",
 B(4,13), niv="specialiste", spe="Infectiologie")

q("P","DX.6 · PHQ-9 chez le grand malade","assessment_diagnosis","hôpital",
 "Une femme de 73 ans, hospitalisée depuis 3 jours, se sent mal, mange peu et pleure. PHQ-9 = 17. On n'a pas encore les résultats du bilan biologique.",
 "Quelle est la conduite la plus appropriée ?",
 [("Rechercher d'abord une cause somatique",""),
  ("Débuter la sertraline sur le score","Un score élevé chez un patient très malade ne dispense pas du bilan."),
  ("Conclure à une dépression réactionnelle","Attribution prématurée."),
  ("Avis psychiatrique avant le bilan","Le bilan somatique vient d'abord, sauf idée suicidaire avec plan."),
  ("Répéter le PHQ-9 dans 3 mois","Délai inadapté.")],
 "Un score PHQ-9 élevé chez un patient très malade impose de rechercher d'abord la cause somatique (DX.6). Une maladie somatique ou un médicament produisent les mêmes symptômes ; bilan anormal (TSH, anémie, glycémie, sodium) : traiter la cause et réévaluer l'humeur.",
 "Le PHQ-9 dépiste, il ne diagnostique pas.",
 PA("ssp-p8","§8 Diagnostic positif"), niv="approfondissement")

META = dict(
 code="G5", lot="LOT_005", version="1.0.0", seed=16, date="2026-11-01",
 titre="Sensation de maladie",
 titre_court="Sensation de maladie", n_dx=15,
 note_version="v1 : gabarit Revision (EX/AP/SPE, 💡 fermé) — 1re production G5",
 note_media="Aucune image clinique dans les HTML LOT_005 (Phase A + DX.1–15) : media = null partout, bouton 🖼 absent.",
 intro_R="Plainte non spécifique de la personne âgée = urgence présumée. Constantes et glycémie capillaire d'abord ; puis sepsis, AVC, SCA, crise surrénalienne, trouble ionique, cancer, avant la cause banale.",
 intro_D="Les 15 DX du LOT face à face : un signe, un examen qui tranche, une conduite. Les questions AP (bleu) et SPE (violet) sont mêlées aux EX : filtrez par niveau en haut.",
 intro_P="Bactériurie asymptomatique, qSOFA rassurant à tort, cortisol « normal » en choc, correction trop rapide du sodium, nitrés et PDE5, Ringer et zolédronate, HbA1c faussée, flumazénil.",
 verdict_label="Réflexe G5",
 footer="LOT_005 · G5 · Banque « Temps 1 » v1 · Faits issus exclusivement des leçons auditées LOT_005 (Phase A + Phase B DX.1–15) · Type A, une seule meilleure réponse (règles IML) · Aucun cliché dans les sources LOT_005 : aucune image affichée.",
 carte_html="""<div class="reflex"><b>Les 3 questions réflexes devant « je ne me sens pas bien »</b><ol>
<li><b>Danger maintenant ?</b> Constantes complètes et <b>glycémie capillaire en 10 minutes</b> : choc, qSOFA ≥ 2, lactate, déficit focal, douleur thoracique ou dyspnée, hypotension avec Na bas et K haut.</li>
<li><b>Foyer ou signe d'appel ?</b> Urine, poumon, peau, abdomen, cathéter ; perte de poids, sueurs, adénopathie ; changement de médicament.</li>
<li><b>Sinon :</b> anamnèse avec un proche et <b>liste complète des médicaments</b>, examen de la tête aux pieds, bilan de base (ECG, ionogramme, calcium, créatinine, glucose, FSC, CRP, TSH), PHQ-2 ; <b>réévaluer à 48–72 h</b>.</li></ol></div>
<div class="map" style="margin-top:10px">
<div class="ax"><h3>🦠 Infection</h3><ul>
<li>Pas de fièvre ≠ pas d'infection chez le sujet âgé (DX.4)</li>
<li>Bandelette positive sans symptôme = ne pas traiter (DX.1)</li>
<li>CRB-65 : 0 domicile, 3–4 hôpital en urgence (DX.3)</li>
<li>Virose = diagnostic d'exclusion (DX.9)</li></ul></div>
<div class="ax"><h3>⚗️ Ions · métabolisme</h3><ul>
<li>Na &lt; 125 + symptômes → NaCl 3 % ; ≤ 10 mmol/L le 1er jour (DX.2)</li>
<li>K élevé + ECG anormal → calcium i.v. (DX.2)</li>
<li>Glycémie &lt; 4,0 ou &gt; 11 mmol/L ; Hb, TSH (DX.10)</li></ul></div>
<div class="ax"><h3>💊 Médicaments · psyché</h3><ul>
<li>12,2 % des plaintes non spécifiques, 40 % reconnus (DX.8)</li>
<li>Thiazide + ISRS → natrémie ; myosis + bradypnée → naloxone</li>
<li>PHQ-9 ≥ 10 → entretien ; somatique d'abord (DX.6)</li></ul></div>
<div class="ax"><h3>🦴 Ceintures · organe</h3><ul>
<li>&gt; 50 ans, raideur &gt; 45 min, CRP ↑ → PMR ; exclure infection et cancer (DX.5)</li>
<li>Trouble visuel, mâchoire → corticoïde sans attendre la biopsie</li>
<li>Aucune orientation → évaluation gériatrique, suivi (DX.7)</li></ul></div>
<div class="ax rf"><h3>🚩 Ordre d'exclusion</h3><ol>
<li>E1 Sepsis (DX.11)</li><li>E2 AVC (DX.12)</li><li>E3 SCA atypique (DX.13)</li>
<li>E4 Crise surrénalienne (DX.15)</li><li>E5 Trouble ionique sévère (DX.2)</li><li>E6 Cancer (DX.14)</li></ol>
<p class="red" style="margin:6px 0 0">Bâle : maladie grave à 30 jours chez 59 % ; diagnostic des urgences correct dans 46 % ; AVC manqué dans 64 % des présentations non spécifiques.</p></div>
</div>""",
 algo_html=f"""<table class="algo"><tr><th>Si…</th><th>Alors…</th></tr>
<tr class="e"><td>Choc, qSOFA ≥ 2, lactate &gt; 2 mmol/L</td><td>DX.11 : hémocultures, antibiotique dans l'heure, cristalloïde 30 mL/kg, noradrénaline si PAM &lt; 65</td></tr>
<tr class="e"><td>Déficit focal ou trouble de la parole</td><td>DX.12 : glycémie, 144, scanner, altéplase avant 4,5 h, thrombectomie si gros vaisseau</td></tr>
<tr class="e"><td>Douleur thoracique, dyspnée, ECG anormal</td><td>DX.13 : ECG en 10 min, troponine hs 0/1 h, aspirine</td></tr>
<tr class="e"><td>Hypotension réfractaire, Na bas, K haut, corticoïdes</td><td>DX.15 : hydrocortisone 100 mg i.v. sans attendre, NaCl 0,9 % 1 L</td></tr>
<tr class="e"><td>Na &lt; 125 mmol/L avec symptômes</td><td>DX.2 : NaCl 3 % en bolus, ≤ 10 mmol/L le 1er jour</td></tr>
<tr class="e"><td>Perte de poids, adénopathie, sueurs, Ca ≥ 3,0</td><td>DX.14 : scanner, biopsie ; hydratation puis zolédronate</td></tr>
<tr><td>Glycémie &lt; 4,0 ou &gt; 11 mmol/L</td><td>DX.10 : glucose, ou cétones et gaz du sang</td></tr>
<tr><td>Symptômes urinaires, fièvre, douleur lombaire</td><td>DX.1 : culture ; fosfomycine (cystite), ceftriaxone (pyélonéphrite)</td></tr>
<tr><td>Toux, fièvre, opacité</td><td>DX.3 : CRB-65, amoxicilline ou hôpital</td></tr>
<tr><td>Autre foyer infectieux</td><td>DX.4 : traiter et contrôler la source</td></tr>
<tr><td>Médicament récent ou augmenté</td><td>DX.8 : arrêt ou substitution, natrémie</td></tr>
<tr><td>Humeur basse, PHQ-9 ≥ 10</td><td>DX.6 : risque suicidaire, entretien, psychothérapie, sertraline</td></tr>
<tr><td>Ceintures et CRP élevée</td><td>DX.5 : exclure infection et cancer, rhumatologie</td></tr>
<tr><td>Contexte épidémique, bilan normal</td><td>DX.9 : symptomatique, réévaluer à 48–72 h</td></tr>
<tr><td>Aucune orientation</td><td>DX.7 : évaluation gériatrique, suivi programmé</td></tr>
</table>
<p class="intro">Source : <a href="{R}LOT_005_Phase_A_V0.html#algo">Phase A · Algorithme discriminant</a> et <a href="{R}LOT_005_Phase_A_V0.html#ssp-p10">§10 Arbre décisionnel</a>.</p>""",
)
