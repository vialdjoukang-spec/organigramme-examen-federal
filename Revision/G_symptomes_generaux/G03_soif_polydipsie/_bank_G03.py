# -*- coding: utf-8 -*-
# Banque G3 — Soif excessive, consommation excessive de liquides (polydipsie) (LOT_003).
# Sources : exclusivement LOT_Claude_Finaux/LOT_003 (Phase A + Phase B DX.1–13, audités C7).
# Convention : opts[0] = bonne réponse (son « pourquoi pas » est ignoré) ; position finale fixée par build_ssp.py (seed).
# dx : le PREMIER DX.n cité = DX cible (couverture) ; les suivants = discrimination croisée.
R = "../../../repo/LOT_Claude_Finaux/LOT_003/"
def PA(sec, label): return (f"{R}LOT_003_Phase_A_V0.html#{sec}", f"Phase A {label}")
def B(n, p): return (f"{R}LOT_003_Phase_B_V0_DX.{n}.html#dx{n}-p{p}", f"Phase B DX.{n} §{p}")

# ═════════════ BLOC R · RAISONNER (avant de nommer le DX)
q("R","DX.9 🚩E1 vs DX.12 · DX.2","assessment_diagnosis","urgences",
 "Un homme de 45 ans est amené aux urgences par son épouse : depuis 4 jours, il boit « sans arrêt » ; ce matin, il est somnolent et désorienté. PA 104/62 mmHg, FC 112/min, FR 28/min. Aucun antécédent connu ; ses médicaments ne sont pas connus.",
 "Quel examen faut-il obtenir en premier ?",
 [("Glycémie, cétones et natrémie",""),
  ("IRM cérébrale","L'imagerie ne passe pas avant le contrôle métabolique en une minute au lit du malade ; elle vient si céphalées ou trouble visuel (E5)."),
  ("Copeptine basale","La copeptine classe une polyurie hypotonique chez un patient stable, après avoir écarté glucose, calcium et rein."),
  ("Calcémie corrigée par l'albumine et PTH intacte","Indispensables plus tard (E4), mais un patient assoiffé et confus reçoit d'abord glycémie, cétones et natrémie."),
  ("Test de restriction hydrique","Dangereux chez un patient confus et hypovolémique ; sa précision n'est que de 70 à 77 %.")],
 "Point clé du cours : un patient assoiffé et confus reçoit d'abord une glycémie capillaire, des cétones et une natrémie. Elles orientent en minutes vers l'acidocétose (E1), le syndrome hyperosmolaire (E2), l'hypernatrémie (E3) ou l'hyponatrémie par potomanie.",
 "FR à 28/min chez un buveur confus : pensez respiration de Kussmaul et prélevez un gaz du sang veineux.",
 PA("ssp-p13","§13 Points clés"))

q("R","DX.1 · symptômes classiques","assessment_diagnosis","cabinet",
 "Un homme de 52 ans consulte pour une soif intense et des mictions fréquentes depuis 6 semaines ; il a perdu 4 kg sans régime. Glycémie veineuse aléatoire 14,2 mmol/L. Pas de vomissements, état général conservé.",
 "Quelle est la conclusion la plus appropriée ?",
 [("Le diabète est établi sans second test",""),
  ("Un second dosage à jeun est nécessaire avant de conclure","Avec des symptômes classiques, une glycémie aléatoire ≥ 11,1 mmol/L suffit seule ; la répétition vaut pour le patient asymptomatique."),
  ("Une HGPO de 75 g doit confirmer le diagnostic","Test long, utile en cas de doute ; ici le diagnostic est déjà posé."),
  ("Il s'agit d'un prédiabète à recontrôler","Le prédiabète correspond à une glycémie à jeun de 5,6 à 6,9 mmol/L ou une HbA1c de 5,7 à < 6,5 %."),
  ("Une glycosurie doit d'abord être documentée","Une glycosurie isolée ne suffit pas au diagnostic et n'ajoute rien à une glycémie diagnostique.")],
 "Critères ADA : une glycémie aléatoire ≥ 11,1 mmol/L avec symptômes classiques (soif, polyurie, perte de poids) pose seule le diagnostic ; sans symptôme, deux tests anormaux sont nécessaires. La soif vient de la diurèse osmotique par le glucose (DX.1).",
 "Avant de classer le type, écartez la crise : vomissements, Kussmaul ou confusion imposent cétones et gaz du sang.",
 B(1,14))

q("R","DX.4 vs DX.2 · prouver la polyurie","assessment_diagnosis","cabinet",
 "Une femme de 38 ans dit uriner « des litres » et boire 4 à 5 L par jour depuis 2 mois. Glycémie, HbA1c, créatinine et calcémie sont normales. Elle va bien par ailleurs.",
 "Quel examen faut-il demander d'abord ?",
 [("Diurèse de 24 h et osmolalité urinaire",""),
  ("IRM hypophysaire","L'IRM vient après avoir prouvé une polyurie hypotonique et orienté vers un déficit en AVP."),
  ("Copeptine stimulée par perfusion de NaCl 3 %","Test de deuxième intention : il faut d'abord prouver la polyurie et doser la copeptine basale."),
  ("Essai de desmopressine","Il ne distingue pas déficit en AVP et polydipsie primaire et expose à l'hyponatrémie."),
  ("Test de privation hydrique","Test historique, précision 70 à 77 % ; jamais en première intention.")],
 "Une polyurie se prouve par une diurèse de 24 heures supérieure à 3 litres (> 40–50 mL/kg/24 h) ; l'osmolalité urinaire sépare ensuite la diurèse osmotique (> 300 mOsm/kg) de la diurèse aqueuse (< 300 mOsm/kg : diabète insipide ou polydipsie primaire).",
 "Carnet mictionnel de 3 jours = alternative au recueil de 24 heures. Le volume avant le mécanisme.",
 PA("ssp-p7","§7.1 Syndrome polyuro-polydipsique"))

q("R","DX.2 vs DX.4 · anamnèse","assessment_diagnosis","cabinet",
 "Un homme de 30 ans boit environ 5 L par jour depuis plus d'un an ; le début a été insidieux. Il dort toute la nuit sans se lever pour boire ni uriner. Il est suivi pour un trouble anxieux. Glycémie, calcémie et créatinine normales ; natrémie 136 mmol/L.",
 "Quel diagnostic est le plus probable à ce stade ?",
 [("Polydipsie primaire",""),
  ("Diabète insipide central","Début plutôt brutal, et la polyurie persiste la nuit avec nycturie et soif nocturne."),
  ("Diabète insipide néphrogénique","On le cherche sous lithium, avec hypercalcémie ou hypokaliémie ; la nycturie persiste aussi."),
  ("Diabète sucré","La glycémie est normale."),
  ("Insuffisance rénale chronique","La créatinine est normale.")],
 "Début progressif, absence de nycturie et contexte psychiatrique orientent vers la polydipsie primaire (DX.2) : le polydipsique primaire dort souvent, alors que le diabète insipide persiste la nuit.",
 "Probable n'est pas prouvé : la copeptine (basale, puis stimulée) confirme avant toute étiquette et avant toute desmopressine.",
 PA("ssp-p5","§5 Anamnèse ciblée"))

q("R","DX.3 · chronicité","assessment_diagnosis","cabinet",
 "Une femme de 68 ans, hypertendue, a un DFGe à 55 mL/min/1,73 m² sur un bilan de routine ; c'est le premier dosage. Elle signale une nycturie. Aucune autre anomalie connue.",
 "Quelle est la conduite la plus appropriée ?",
 [("Répéter DFGe et RAC à 3 mois",""),
  ("Retenir d'emblée une IRC de stade G3a","Le diagnostic exige une persistance de plus de 3 mois."),
  ("Adresser d'emblée en néphrologie","L'adressage vise un DFGe < 30, une RAC > 30 mg/mmol ou un déclin rapide."),
  ("Débuter un inhibiteur du SGLT2 sans autre bilan","On confirme et on classe (G et A) avant de traiter."),
  ("Demander une biopsie rénale","Aucune indication sur un DFGe isolé.")],
 "KDIGO 2024 : IRC = DFGe < 60 mL/min/1,73 m² ou marqueur de lésion (albuminurie) pendant plus de 3 mois. Un DFGe bas isolé ne prouve pas l'IRC.",
 "Une créatinine normale n'exclut pas l'IRC chez la personne âgée à faible masse musculaire.",
 B(3,14))

q("R","DX.11 🚩E5 vs DX.2","assessment_diagnosis","cabinet",
 "Une femme de 41 ans a une polyurie de 6 L par jour apparue brutalement il y a 3 semaines. Elle a des céphalées et se cogne aux encadrements de porte ; vous notez une réduction du champ visuel. Glycémie et calcémie normales.",
 "Quelle est la prochaine étape la plus appropriée ?",
 [("IRM hypophysaire urgente et bilan hypophysaire",""),
  ("Essai de desmopressine à domicile","Il ne tranche pas et retarde le diagnostic d'une masse qui comprime le chiasma."),
  ("Test de privation hydrique ambulatoire","Peu précis et dangereux ; il ne répond pas à la question de la masse."),
  ("Carnet mictionnel de 3 jours et contrôle clinique dans 3 mois","Céphalées + déficit du champ visuel = drapeau rouge E5 : pas d'attente."),
  ("Échographie rénale","Le rein n'explique ni les céphalées ni le champ visuel.")],
 "Céphalées et déficit du champ visuel avec polyurie : une masse sellaire ou hypothalamique comprime le chiasma (DX.11, rang E5). IRM urgente, bilan hypophysaire complet, avis endocrinologique et neurochirurgical.",
 "Début brutal = déficit en AVP plutôt que polydipsie primaire. Cherchez aussi un panhypopituitarisme.",
 PA("ssp-p4","§4 Démarche, E5"))

q("R","DX.12 🚩E3 vs DX.8","management","urgences",
 "Un homme de 78 ans est retrouvé au sol chez lui après 2 jours sans boire. PA 78/45 mmHg, FC 124/min, extrémités froides, oligurie. Natrémie 162 mmol/L.",
 "Quelle est la première mesure thérapeutique ?",
 [("Cristalloïde isotonique en bolus",""),
  ("Glucose 5 % rapide pour abaisser la natrémie","L'eau libre vient après la restauration du volume ; elle ne corrige pas le choc."),
  ("Noradrénaline seule","Contre-indiquée seule dans l'hypotension par hypovolémie : remplir d'abord."),
  ("Eau par sonde gastrique","Trop lent pour un choc ; c'est une étape de correction du déficit en eau."),
  ("NaCl 0,45 % en perfusion lente","Le soluté hypotonique vient après la restauration du volume.")],
 "Le médecin traite le choc avant de corriger la natrémie : cristalloïde isotonique quelle que soit la natrémie, jusqu'à la restauration du volume (malgré la contre-indication de l'étiquette AIPS, à discuter) ; puis eau libre sur 48 à 72 heures (DX.12, E3).",
 "Une pression normale n'exclut pas le choc : la compensation retarde l'hypotension. Au-delà de 160 mmol/L, la mortalité de l'adulte atteint 75 %.",
 B(12,14))

q("R","DX.13 🚩E4 vs DX.5","management","hôpital",
 "Une femme de 67 ans traitée pour un cancer bronchique est confuse, constipée et très assoiffée. Calcémie corrigée 3,4 mmol/L ; PTH basse ; créatinine légèrement élevée. Pas d'insuffisance cardiaque.",
 "Quelle est la première mesure thérapeutique ?",
 [("Réhydratation par NaCl 0,9 %, puis antirésorptif IV",""),
  ("Zolédronate 4 mg IV immédiat, avant toute perfusion de sérum","L'AIPS exige de contrôler l'état d'hydratation avant le zolédronate."),
  ("Calcitonine seule","Effet court (48 à 72 h) ; elle complète l'antirésorptif dans les formes sévères."),
  ("Prednisone 60 mg/j","Réservée à l'hypercalcémie par calcitriol (lymphome, granulomatose)."),
  ("Parathyroïdectomie","PTH basse : la parathyroïde n'est pas en cause.")],
 "Calcémie corrigée > 3,0 mmol/L avec PTH basse chez un cancéreux = hypercalcémie maligne (DX.13, E4). Ordre : hydratation par sérum physiologique, puis bisphosphonate IV (zolédronate) ; calcitonine si sévère.",
 "Furosémide seulement en cas de surcharge, jamais en routine. Au-delà de 3,5 mmol/L : ajouter la calcitonine et surveiller l'ECG.",
 B(13,13))

q("R","DX.10 🚩E2 vs DX.9","assessment_diagnosis","EMS",
 "Une résidente d'EMS de 84 ans, diabétique de type 2, est de plus en plus confuse depuis 4 jours et boit peu. Glycémie 41 mmol/L, osmolalité 342 mOsm/kg, β-hydroxybutyrate 0,8 mmol/L, pH 7,37, bicarbonate 23 mmol/L. Muqueuses sèches, PA 98/60 mmHg.",
 "Quel est le diagnostic le plus probable ?",
 [("Syndrome hyperosmolaire hyperglycémique",""),
  ("Acidocétose diabétique","Exige β-hydroxybutyrate ≥ 3,0 mmol/L et pH < 7,30 ou bicarbonate < 18 mmol/L."),
  ("État mixte acidocétose et hyperosmolarité","Il faudrait une cétonémie > 3,0 mmol/L et une acidose."),
  ("Diabète insipide avec hypernatrémie","La glycémie de 41 mmol/L explique l'hyperosmolalité."),
  ("Démence évolutive avec déshydratation simple","Une confusion récente avec glycémie extrême n'est pas une démence.")],
 "Glycémie très élevée (≥ 30–33,3 mmol/L), osmolalité ≥ 320 mOsm/kg, hypovolémie, cétonémie < 3,0 mmol/L et pH ≥ 7,30 = syndrome hyperosmolaire hyperglycémique (DX.10, E2), typique du diabétique âgé, installé sur plusieurs jours.",
 "Le diagnostic n'est jamais biologique seul : l'hypovolémie clinique fait partie des critères.",
 B(10,13))

q("R","DX.9 🚩E1 · ordre","management","urgences",
 "Une femme de 19 ans, diabétique de type 1, arrive aux urgences : vomissements depuis 12 heures, respiration ample et profonde, haleine fruitée. Glycémie 24 mmol/L, β-hydroxybutyrate 5,1 mmol/L, pH 7,14, bicarbonate 12 mmol/L. La kaliémie est en cours d'analyse.",
 "Quelle est la première mesure thérapeutique ?",
 [("NaCl 0,9 % 500 à 1000 mL/h",""),
  ("Insuline IV 0,1 UI/kg/h immédiatement","La kaliémie doit être connue avant la première unité ; < 3,5 mmol/L, l'insuline se retarde."),
  ("Bicarbonate de sodium IV","Réservé au pH < 7,0."),
  ("Glucose 5 % IV","Il s'ajoute seulement quand la glycémie passe sous 13,9 mmol/L."),
  ("Insuline sous-cutanée et retour à domicile","Acidocétose modérée : hospitalisation et insuline IV.")],
 "Acidocétose (glycémie ≥ 11,1, β-hydroxybutyrate ≥ 3,0, pH < 7,30) : l'ordre est perfusion, potassium, insuline. Le remplissage (500–1000 mL/h pendant 2 à 4 h) débute d'emblée ; il restaure la volémie.",
 "Gravité : pH 7,0–7,25 = modérée (soins intermédiaires) ; pH < 7,0 = sévère. Cherchez le déclencheur : infection, oubli d'insuline.",
 B(9,13))

q("R","DX.5 vs DX.13 · confirmer","assessment_diagnosis","cabinet",
 "Une femme de 58 ans consulte pour une soif et une polyurie modérées ; elle a eu une colique néphrétique l'an dernier. Calcémie corrigée 2,78 mmol/L ; PTH élevée. Pas de cancer connu, pas de thiazidique ni de lithium.",
 "Quelle est l'étape suivante avant de retenir le diagnostic ?",
 [("Recontrôler calcémie et PTH à ≥ 2 semaines",""),
  ("Échographie cervicale de localisation des parathyroïdes","L'imagerie localise avant la chirurgie ; elle ne pose ni n'écarte le diagnostic."),
  ("Dosage de la PTHrP","La PTHrP cherche une hypercalcémie maligne, à PTH basse."),
  ("Parathyroïdectomie d'emblée","Le diagnostic biochimique doit d'abord être confirmé."),
  ("Zolédronate 4 mg IV","Réservé à l'hypercalcémie maligne (calcémie corrigée > 3,0 mmol/L).")],
 "Hyperparathyroïdie primaire (DX.5) : calcémie corrigée élevée avec PTH élevée ou inappropriée, sur deux mesures espacées d'au moins 2 semaines. L'hypercalcémie rend le tubule résistant à l'AVP : d'où la polyurie.",
 "Une PTH « normale » avec une calcémie haute est inappropriée : elle n'exclut pas la maladie.",
 B(5,14))

q("R","DX.6 vs DX.4 · soif sans polyurie","assessment_diagnosis","cabinet",
 "Une femme de 55 ans dit avoir « tout le temps soif » : elle doit boire pour avaler le pain. Ses yeux brûlent « comme du sable ». Diurèse de 24 h : 1,6 L. Glycémie et calcémie normales.",
 "Quelle démarche est la plus appropriée ?",
 [("Revoir les médicaments, puis anti-SSA et tests de sécheresse",""),
  ("Copeptine basale","Sans polyurie, il n'y a pas de diabète insipide à chercher."),
  ("Test de restriction hydrique pour exclure un diabète insipide","Il explore une polyurie hypotonique, absente ici."),
  ("IRM hypophysaire","Aucun signe de lésion sellaire ni de polyurie."),
  ("Essai de desmopressine","Aucune polyurie à traiter ; risque d'hyponatrémie.")],
 "La soif du syndrome sec naît de la bouche, pas de l'osmolalité : elle ne s'accompagne pas de polyurie. Un syndrome sec persistant impose d'abord la revue des médicaments (anticholinergiques), puis l'anti-SSA et les tests de sécheresse (DX.6).",
 "Seul le volume urinaire sépare la xérostomie du syndrome polyuro-polydipsique : mesurez-le.",
 B(6,13))

q("R","DX.7 vs DX.4 · lithium","assessment_diagnosis","cabinet",
 "Un homme de 44 ans, traité par lithium depuis 6 ans pour un trouble bipolaire, urine 5 L par jour et se lève deux fois la nuit pour boire. Il est bien orienté ; pas de tremblement. Glycémie normale.",
 "Quel examen faut-il demander en premier ?",
 [("Lithiémie, avec natrémie, calcémie et créatinine",""),
  ("IRM hypophysaire","Le lithium cause un diabète insipide néphrogénique, pas une lésion sellaire."),
  ("Test de restriction hydrique ambulatoire sur 24 heures","Pas de restriction thérapeutique sous lithium : la déshydratation pousse à l'intoxication."),
  ("Copeptine stimulée par NaCl 3 %","Le néphrogénique se signe par une copeptine basale élevée ; il faut d'abord la lithiémie."),
  ("Essai de desmopressine","Elle ne corrige pas le diabète insipide du lithium : le rein ne répond plus à l'ADH.")],
 "Un patient sous lithium qui boit et urine beaucoup a un diabète insipide néphrogénique jusqu'à preuve du contraire (DX.7). La lithiémie dit s'il existe un surdosage ; l'arrêt ou la substitution se discute avec le prescripteur.",
 "Lithiémie ≥ 1,5 mmol/L = arrêt immédiat. Prélèvement 12 h après la dernière prise.",
 B(7,13))

q("R","DX.8 · coup de chaleur","management","urgences",
 "Un ouvrier de 32 ans s'effondre sur un chantier en pleine canicule. Température centrale 40,8 °C ; il est confus et agité ; peau chaude ; FC 128/min ; PA 102/64 mmHg.",
 "Quelle est la mesure prioritaire ?",
 [("Refroidissement immédiat par immersion dans l'eau",""),
  ("Réhydratation orale et repos à l'ombre","Insuffisant : > 40 °C avec confusion définit un coup de chaleur."),
  ("Attendre la natrémie avant tout geste","Le refroidissement ne se retarde pas pour un résultat."),
  ("Glucose 5 % rapide en premier","L'eau libre ne refroidit pas ; le danger immédiat est la température."),
  ("Restriction hydrique","Contraire au besoin : il a perdu de l'eau.")],
 "Coup de chaleur = température centrale > 40 °C avec dysfonction du système nerveux central. Il impose le refroidissement immédiat ; l'immersion dans l'eau (1 à 17 °C) est la meilleure technique (DX.8).",
 "Soif + chaleur + urine concentrée = déshydratation ; ajoutez la confusion et la fièvre > 40 °C = coup de chaleur.",
 B(8,14))

q("R","DX.4 néphrogénique vs DX.2","assessment_diagnosis","hôpital",
 "Une femme de 47 ans a une polyurie de 5 L/24 h, une osmolalité urinaire de 180 mOsm/kg, une glycémie et une calcémie normales. La copeptine basale, prélevée sans restriction hydrique, est de 26 pmol/L.",
 "Quelle est la conduite la plus appropriée ?",
 [("Chercher lithium, hypercalcémie, hypokaliémie",""),
  ("Test de stimulation par NaCl 3 % pour confirmer le type","Inutile : une copeptine basale ≥ 21,4 pmol/L conclut déjà."),
  ("Test à l'arginine","Même raison : le test stimulé ne sert que si la basale est < 21,4 pmol/L."),
  ("IRM hypophysaire","Le néphrogénique est rénal ; l'IRM sert au déficit central."),
  ("Desmopressine sublinguale","Le rein résiste à l'AVP : la desmopressine ne corrige pas un néphrogénique.")],
 "Copeptine basale ≥ 21,4 pmol/L sans soif imposée (sensibilité et spécificité 100 %) = diabète insipide néphrogénique (DX.4). On recherche la cause : lithium, hypercalcémie, hypokaliémie.",
 "200 à 300 mL d'eau dans l'heure précédente suffisent à faire chuter la copeptine : pas de boisson avant le prélèvement.",
 PA("ssp-p9","§9.d Deuxième intention"))

# ═════════════ BLOC D · DISCRIMINER (DX face à face)
q("D","DX.1 · prédiabète","assessment_diagnosis","cabinet",
 "Un homme de 49 ans, en surpoids, sans symptôme, a une HbA1c à 6,0 % sur un bilan de routine. Glycémie à jeun 6,2 mmol/L.",
 "Comment interpréter ce bilan ?",
 [("Prédiabète",""),
  ("Diabète de type 2 confirmé","Il faut HbA1c ≥ 6,5 % ou glycémie à jeun ≥ 7,0 mmol/L."),
  ("Diabète à confirmer par une HGPO immédiate","Aucune valeur n'atteint un seuil diagnostique."),
  ("Bilan normal","HbA1c entre 5,7 et < 6,5 % et glycémie à jeun 5,6–6,9 mmol/L ne sont pas normales."),
  ("Diabète insipide débutant","Le diabète insipide ne touche pas la glycémie.")],
 "Prédiabète : HbA1c 5,7 à < 6,5 % ou glycémie à jeun 5,6 à 6,9 mmol/L. Une valeur isolée sans symptôme ne pose jamais le diagnostic de diabète (DX.1).",
 "Diabète : HbA1c ≥ 6,5 % (48 mmol/mol), glycémie à jeun ≥ 7,0 mmol/L, HGPO 2 h ≥ 11,1 mmol/L ; deux tests anormaux sans symptôme.",
 B(1,14))

q("D","DX.1 vs DX.3 · metformine","management","cabinet",
 "Une femme de 63 ans a un diabète de type 2 nouvellement diagnostiqué (HbA1c 7,4 %). Son DFGe est stable à 26 mL/min/1,73 m² depuis un an.",
 "Quelle affirmation est correcte concernant la metformine ?",
 [("Elle est contre-indiquée chez cette patiente",""),
  ("Elle se débute à 500 mg par jour","Contre-indiquée en dessous d'un DFGe de 30 mL/min/1,73 m²."),
  ("Elle est autorisée jusqu'à 1000 mg par jour","Ce plafond vaut pour un DFGe de 30 à 59."),
  ("Elle se donne à pleine dose, 3000 mg/j","Dose maximale hors insuffisance rénale."),
  ("Elle remplace l'insuline à jeun","Aucun rapport avec la question rénale.")],
 "AIPS Glucophage® : contre-indiquée si DFGe < 30 mL/min/1,73 m², en acidocétose ou en coma diabétique (DX.1). Les recommandations suisses (SSED) placent la metformine en premier, puis un inhibiteur du SGLT2 ou un agoniste du GLP-1.",
 "Les sulfonylurées ne sont plus recommandées par la SSED.",
 B(1,14))

q("D","DX.1 · DFGe 30–59","management","cabinet",
 "Un homme de 71 ans, diabétique de type 2, a un DFGe stable à 42 mL/min/1,73 m². Son médecin veut augmenter la metformine (actuellement 500 mg 2 fois par jour).",
 "Quelle dose quotidienne maximale l'AIPS autorise-t-elle ?",
 [("1000 mg",""),
  ("500 mg","Trop bas : le palier DFGe 30–59 autorise jusqu'à 1000 mg."),
  ("2000 mg","Dose d'entretien habituelle, hors insuffisance rénale."),
  ("3000 mg","Maximum hors insuffisance rénale."),
  ("Arrêt obligatoire","L'arrêt s'impose sous 30 mL/min/1,73 m².")],
 "AIPS Glucophage® : DFGe 30 à 59 → maximum 1000 mg par jour ; arrêt si < 30.",
 "Effet glycémique de l'empagliflozine réduit si DFGe < 45 : l'iSGLT2 garde surtout un bénéfice rénal et cardiaque.",
 B(1,11), niv="specialiste", spe="Endocrinologie")

q("D","DX.1 vs DX.9 · iSGLT2","assessment_diagnosis","cabinet",
 "Un homme de 57 ans, diabétique de type 2 sous empagliflozine (Jardiance®), vomit depuis la veille et se sent très faible. Glycémie capillaire 12 mmol/L.",
 "Quelle est la prochaine étape la plus appropriée ?",
 [("Doser les cétones (β-hydroxybutyrate) et le pH",""),
  ("Rassurer : une glycémie à 12 mmol/L exclut l'acidocétose","Sous iSGLT2, l'acidocétose survient avec une glycémie modérée."),
  ("Doubler l'empagliflozine","On l'arrête si l'acidocétose est suspectée."),
  ("Bandelette urinaire seule","Elle mesure l'acétoacétate et sous-estime la cétose au début."),
  ("Antiémétique et retour à domicile","Le tableau impose d'exclure une acidocétose.")],
 "AIPS Jardiance® : des nausées chez un diabétique imposent un test de cétones quelle que soit la glycémie, et l'arrêt si l'acidocétose est suspectée. Environ 10 % des acidocétoses sont euglycémiques (DX.9).",
 "Glycémie normale ≠ acidocétose exclue : β-hydroxybutyrate et gaz du sang.",
 B(1,14), niv="approfondissement")

q("D","DX.2 vs DX.4 · copeptine stimulée","assessment_diagnosis","hôpital",
 "Un homme de 34 ans a une polyurie hypotonique (6 L/24 h, osmolalité urinaire 120 mOsm/kg). Glycémie, calcémie et créatinine normales. Copeptine basale 3,1 pmol/L. Sous NaCl 3 %, la natrémie atteint 151 mmol/L ; la copeptine stimulée est de 9,8 pmol/L.",
 "Quel est le diagnostic ?",
 [("Polydipsie primaire",""),
  ("Diabète insipide central","Il faudrait une copeptine stimulée ≤ 4,9 pmol/L."),
  ("Diabète insipide néphrogénique","Il faudrait une copeptine basale ≥ 21,4 pmol/L."),
  ("Zone limite : répéter le test","La zone limite va de 4,9 à 6,5 pmol/L."),
  ("Insuffisance rénale chronique","La créatinine est normale.")],
 "Copeptine stimulée par NaCl 3 % (Na > 147 mmol/L) > 4,9 pmol/L = polydipsie primaire (sensibilité 93 %, spécificité 100 %, précision 97 %). ≤ 4,9 = diabète insipide central (DX.4).",
 "Entre 4,9 et 6,5 pmol/L (seuil post hoc 6,5) : avis endocrinologique, répéter ou croiser avec la clinique.",
 PA("ssp-p9","§9.d Interprétation de la copeptine"))

q("D","DX.2 · desmopressine","management","cabinet",
 "Une femme de 29 ans boit 6 L par jour ; une polydipsie primaire est confirmée par la copeptine stimulée. Elle demande « un médicament pour uriner moins ».",
 "Quelle attitude est correcte ?",
 [("Refuser la desmopressine : elle est contre-indiquée",""),
  ("Desmopressine sublinguale 60 µg 3 fois par jour","Dose du diabète insipide central ; contre-indiquée ici."),
  ("Hydrochlorothiazide 100 mg par jour","Traitement du diabète insipide néphrogénique."),
  ("Restriction hydrique stricte immédiate à 1 L","On réduit les apports progressivement."),
  ("Essai de desmopressine pour confirmer","Un essai ne distingue pas les deux entités et expose à l'hyponatrémie.")],
 "Dans la polydipsie primaire (DX.2), la desmopressine provoque une hyponatrémie : l'AIPS la contre-indique. Aucun traitement n'est validé : réduction progressive des apports, psychoéducation, TCC.",
 "Dire « boire à la soif », non « boire beaucoup » : c'est aussi la prévention primaire de la potomanie.",
 PA("ssp-p11","§11.B.2 Pharmacologique"))

q("D","DX.2 · faibles solutés","mechanisms","cabinet",
 "Un homme de 52 ans boit chaque jour 5 à 6 L de bière et mange très peu. Il est amené pour confusion ; natrémie 118 mmol/L.",
 "Quel mécanisme explique le mieux son hyponatrémie ?",
 [("L'apport faible de solutés réduit l'excrétion d'eau à environ 4 L/jour",""),
  ("La bière stimule directement la sécrétion d'AVP","Le facteur clé est la baisse de l'apport de solutés."),
  ("L'alcool provoque un diabète insipide néphrogénique","Ce n'est pas le mécanisme décrit."),
  ("Le rein normal ne peut pas excréter plus de 2 L d'eau par jour, quel que soit l'apport","Un rein normal excrète jusqu'à 15 à 18 L par jour."),
  ("La perte digestive de sodium domine","Aucune diarrhée n'est décrite.")],
 "Un rein normal excrète 15 à 18 L d'eau par jour ; quand l'apport de solutés baisse (malnutrition, bière), cette capacité tombe à 4 L par jour. Au-delà, l'eau s'accumule et la natrémie chute (DX.2, hors liste).",
 "Médicaments, infection et stress libèrent l'AVP et aggravent le risque.",
 PA("ssp-p3","§3 Complications"), niv="approfondissement")

q("D","DX.2 · correction prudente","management","hôpital",
 "Un homme de 41 ans, schizophrène, alcoolodépendant et dénutri, est hospitalisé pour une hyponatrémie à 116 mmol/L après une polydipsie massive. Il a eu une crise convulsive ; on débute du NaCl 3 %.",
 "Quelle hausse maximale de la natrémie sur 24 heures faut-il viser ?",
 [("8 mmol/L",""),
  ("10 mmol/L","Limite habituelle ; elle descend à 8 mmol/L si le risque de démyélinisation osmotique est élevé."),
  ("12 mmol/L","Limite citée pour la myélinolyse, trop haute chez ce patient à risque."),
  ("15 mmol/L","Expose à la démyélinisation osmotique."),
  ("Aucune limite tant que la convulsion persiste","Même en urgence, la correction reste limitée.")],
 "Hyponatrémie par potomanie : NaCl 3 % seulement si symptômes graves ; hausse ≤ 10 mmol/L en 24 h, 8 mmol/L si le risque de démyélinisation osmotique est élevé (alcool, dénutrition).",
 "Pesée quotidienne du polydipsique : une prise rapide signe la rétention d'eau.",
 PA("ssp-p11","§11.B.1 Hyponatrémie par potomanie"), niv="specialiste", spe="Psychiatrie")

q("D","DX.3 · hyperkaliémie","management","urgences",
 "Une femme de 74 ans en IRC stade G4 est adressée pour une faiblesse. Kaliémie 7,1 mmol/L ; l'ECG montre des ondes T pointues et un élargissement du QRS.",
 "Quelle est la première mesure ?",
 [("Gluconate de calcium IV",""),
  ("Furosémide IV","Il ne protège pas le myocarde dans l'immédiat."),
  ("Résine échangeuse orale seule","Trop lente devant un ECG anormal."),
  ("Contrôle de la kaliémie dans 2 heures","Un ECG anormal est une urgence immédiate."),
  ("Bicarbonate de sodium oral","Ne protège pas le myocarde.")],
 "Hyperkaliémie avec modifications ECG = urgence : le calcium IV vient d'abord, il protège le myocarde (DX.3). Les autres mesures suivent.",
 "Oligo-anurie, hyperkaliémie avec ECG ou œdème pulmonaire en IRC = traitement d'urgence.",
 B(3,13))

q("D","DX.3 · polyurie de l'IRC","mechanisms","cabinet",
 "Un homme de 66 ans en IRC stade G3b (DFGe 38) se plaint d'une nycturie et d'une soif modérée. Glycémie et calcémie normales.",
 "Quel mécanisme explique sa polyurie ?",
 [("Perte de la capacité tubulaire de concentrer l'urine",""),
  ("Diurèse osmotique par le glucose","La glycémie est normale."),
  ("Défaut de sécrétion d'AVP","Le défaut est rénal, pas hypophysaire."),
  ("Prise d'eau excessive primaire","Le mécanisme de l'IRC est tubulaire."),
  ("Hypercalcémie","La calcémie est normale.")],
 "Dans l'IRC (DX.3), les tubules perdent leur capacité de concentrer l'urine : polyurie modérée et nycturie.",
 "Une créatinine normale n'exclut pas l'IRC chez la personne âgée à faible masse musculaire.",
 B(3,13))

q("D","DX.3 · stade KDIGO","assessment_diagnosis","cabinet",
 "Un homme de 60 ans a, depuis 8 mois, un DFGe entre 48 et 52 mL/min/1,73 m² et une RAC entre 5 et 8 mg/mmol à chaque contrôle.",
 "Quelle classification KDIGO s'applique ?",
 [("G3a A2",""),
  ("G2 A1","DFGe 60–89 et RAC < 3."),
  ("G3b A2","G3b correspond à un DFGe de 30 à 44."),
  ("G3a A3","A3 correspond à une RAC > 30 mg/mmol."),
  ("Pas d'IRC : durée insuffisante","Plus de 3 mois de persistance : l'IRC est établie.")],
 "KDIGO 2024 : G3a = DFGe 45–59 ; A2 = RAC 3 à 30 mg/mmol. La combinaison G et A estime le risque (DX.3).",
 "Albuminurie seule (RAC ≥ 3 mg/mmol) persistante suffit au diagnostic, même avec un DFGe normal.",
 B(3,8), niv="approfondissement")

q("D","DX.3 · iSGLT2","management","cabinet",
 "Une femme de 70 ans a une IRC avec albuminurie ; DFGe 22 mL/min/1,73 m². Son néphrologue envisage un iSGLT2.",
 "Selon l'AIPS, quelle affirmation est correcte ?",
 [("La dapagliflozine ne s'instaure pas sous 25 mL/min/1,73 m²",""),
  ("Aucun iSGLT2 ne s'instaure sous 45","L'empagliflozine s'instaure dès 20, la dapagliflozine dès 25."),
  ("L'empagliflozine ne s'instaure pas sous 30","Son seuil d'instauration est 20 mL/min/1,73 m²."),
  ("La dapagliflozine s'instaure dès 15","Son seuil est 25 mL/min/1,73 m²."),
  ("Les iSGLT2 sont réservés au diabète","Ils ralentissent la progression de l'IRC avec albuminurie.")],
 "AIPS : instauration non recommandée si DFGe < 25 pour la dapagliflozine (Forxiga®), < 20 pour l'empagliflozine. Bloqueur du SRA + iSGLT2 ralentissent la progression en cas d'albuminurie (DX.3).",
 "IEC et statine sont contre-indiqués pendant la grossesse ; l'iSGLT2 s'arrête dès la grossesse constatée.",
 B(3,14), niv="approfondissement")

q("D","DX.3 · anémie rénale","management","hôpital",
 "Un homme de 68 ans en IRC non dialysée reçoit de la darbépoétine alfa (Aranesp®) pour une anémie. Son hémoglobine est passée de 98 à 121 g/L.",
 "Quelle limite d'hémoglobine l'AIPS fixe-t-elle ?",
 [("120 g/L au plus",""),
  ("100 g/L au plus","Trop bas : la limite AIPS est 120 g/L."),
  ("130 g/L au plus","Au-dessus de la limite AIPS."),
  ("140 g/L au plus","Au-dessus de la limite AIPS."),
  ("Aucune limite si bien toléré","L'AIPS fixe un plafond.")],
 "AIPS Aranesp® : hémoglobine maintenue à 120 g/L (12 g/dL) au plus ; baisse d'environ 25 % de la dose si elle monte de plus de 20 g/L en 4 semaines.",
 "Dose initiale 0,45 µg/kg par semaine, IV chez le dialysé, SC chez le non-dialysé.",
 B(3,11), niv="specialiste", spe="Néphrologie")

q("D","DX.4 vs DX.2 · natrémie","assessment_diagnosis","hôpital",
 "Une femme de 36 ans a une polyurie de 7 L/24 h. Osmolalité urinaire 110 mOsm/kg ; natrémie 152 mmol/L ; glycémie et calcémie normales.",
 "Quelle conclusion est la plus appropriée ?",
 [("Diabète insipide, sans test supplémentaire",""),
  ("Polydipsie primaire probable","La polydipsie primaire a une natrémie normale-basse."),
  ("Test de stimulation par NaCl 3 % indispensable","Inutile : Na ≥ 150 avec urine diluée confirme déjà le diabète insipide."),
  ("Test de restriction hydrique","Dangereux avec une natrémie déjà haute."),
  ("Diurèse osmotique","Une urine à 110 mOsm/kg est diluée, pas osmotique.")],
 "Un sodium ≥ 150 mmol/L avec urine diluée confirme le diabète insipide sans test supplémentaire (DX.4). Le test stimulé sert quand la natrémie est normale.",
 "Natrémie normale chez un diabète insipide qui a accès à l'eau ; haute seulement si adipsie ou eau inaccessible.",
 B(4,13))

q("D","DX.4 néphrogénique · traitement","management","cabinet",
 "Un homme de 50 ans a un diabète insipide néphrogénique sur hypokaliémie ancienne ; la kaliémie est corrigée mais la polyurie persiste. Pas de lithium.",
 "Quel traitement est indiqué ?",
 [("Hydrochlorothiazide",""),
  ("Desmopressine sublinguale","Le rein résiste à l'AVP : sans effet dans le néphrogénique."),
  ("Restriction hydrique stricte","Expose à la déshydratation et à l'hypernatrémie."),
  ("Furosémide","Diurétique de l'anse : pas l'indication AIPS du néphrogénique."),
  ("Pilocarpine","Traite la xérostomie, pas la polyurie.")],
 "Diabète insipide néphrogénique (DX.4) : supprimer la cause, corriger calcium et potassium, puis hydrochlorothiazide (100 mg/j en 2 à 4 prises, kaliémie étroitement surveillée). Paradoxe : le thiazide réduit le volume urinaire et augmente l'osmolalité urinaire.",
 "Sous lithium, le thiazide élève la lithiémie : choix discuté avec le prescripteur.",
 PA("ssp-p14","§14 Pièges"))

q("D","DX.4 · privation hydrique","assessment_diagnosis","hôpital",
 "Un interne propose un test de privation hydrique pour distinguer diabète insipide central et polydipsie primaire chez une patiente stable à natrémie normale.",
 "Quelle affirmation sur ce test est correcte ?",
 [("Sa précision n'est que de 41 % pour la polydipsie primaire",""),
  ("C'est l'étalon actuel, plus précis que la copeptine","La copeptine stimulée le surpasse : 96,5 % contre 76,6 %."),
  ("Sa précision globale dépasse 95 %","Elle est de 70 à 77 %."),
  ("Il est validé de façon prospective","Il ne l'est pas."),
  ("Il est sans danger dans le diabète insipide","Il expose à des complications graves dans le diabète insipide.")],
 "La privation hydrique (1964) reste un étalon historique : précision 70 à 77 %, et seulement 41 % pour la polydipsie primaire. La copeptine stimulée par NaCl 3 % atteint 96,5 % (DX.4 vs DX.2).",
 "Ce qui ne suffit pas : polyurie seule, urine diluée seule, essai de desmopressine.",
 PA("ssp-p14","§14 Pièges"), niv="approfondissement")

q("D","DX.4 · enfant","assessment_diagnosis","hôpital",
 "Un garçon de 8 ans a une polyurie hypotonique ; glycémie, calcémie et créatinine normales ; copeptine basale 2,4 pmol/L.",
 "Quel test de stimulation faut-il préférer ?",
 [("Test à l'arginine",""),
  ("Test au NaCl 3 %","Contre-indiqué chez l'enfant."),
  ("Test de privation hydrique","Moins précis et non validé de façon prospective."),
  ("Essai de desmopressine","Ne distingue pas central et polydipsie primaire."),
  ("Aucun : la basale suffit","Une basale < 21,4 pmol/L impose un test stimulé.")],
 "Chez l'enfant, le NaCl 3 % est contre-indiqué : on préfère l'arginine (seuil 3,8 pmol/L à 60 minutes). Le test à l'arginine dure 1 heure et demande moins de surveillance.",
 "Vomissements pendant l'arginine : test invalide, sauf si la copeptine reste basse.",
 PA("ssp-p9","§9.c Alternatives"), niv="approfondissement")

q("D","DX.4 · desmopressine du sujet âgé","management","cabinet",
 "Une femme de 72 ans débute de la desmopressine pour un diabète insipide central confirmé.",
 "Quand faut-il contrôler la natrémie ?",
 [("Avant le début et 3 jours après",""),
  ("Seulement à 3 mois","Trop tard : l'hyponatrémie survient tôt."),
  ("Aucun contrôle si la diurèse baisse","La natrémie reste obligatoire après 65 ans."),
  ("Une fois par an","Insuffisant au début."),
  ("Seulement en cas de convulsion","La surveillance prévient les symptômes.")],
 "Après 65 ans : natrémie avant le début, puis 3 jours après le début ou après chaque hausse de dose. Chez des adultes de 70 ans, la desmopressine multiplie par 13 le taux d'hyponatrémie (DX.4).",
 "Prise de poids ou signes d'hyponatrémie sous desmopressine : interrompre (AIPS).",
 B(4,14), niv="approfondissement")

q("D","DX.4 vs DX.11 · étiologie","assessment_diagnosis","hôpital",
 "Un garçon de 12 ans a un diabète insipide central isolé, sans céphalée ni trouble visuel. L'IRM est prévue.",
 "Quelles étiologies faut-il évoquer en priorité ?",
 [("Craniopharyngiome ou germinome",""),
  ("Adénome hypophysaire","L'adénome donne rarement un diabète insipide."),
  ("Hyperparathyroïdie primaire","Elle donne une polyurie néphrogénique, pas un déficit central."),
  ("Prise de lithium","Le lithium cause un néphrogénique."),
  ("Polydipsie primaire","Le déficit central est confirmé.")],
 "Un diabète insipide isolé ne fait pas suspecter un adénome hypophysaire, qui en donne rarement : on pense au craniopharyngiome ou au germinome (DX.11).",
 "Bilan hypophysaire complet : chaque lésion de l'axe peut toucher plusieurs hormones.",
 B(4,14), niv="specialiste", spe="Endocrinologie pédiatrique")

q("D","DX.5 · critère chirurgical","management","cabinet",
 "Une femme de 46 ans, asymptomatique, a une hyperparathyroïdie primaire confirmée : calcémie corrigée 2,70 mmol/L (norme supérieure 2,55), DFGe 85, T-score −1,8, pas de calcul.",
 "Quelle conduite est la plus appropriée ?",
 [("Parathyroïdectomie, car elle a moins de 50 ans",""),
  ("Surveillance annuelle : aucun critère chirurgical n'est rempli","L'âge < 50 ans suffit comme critère."),
  ("Cinacalcet au long cours","Réservé à l'hyperparathyroïdie non opérable."),
  ("Restriction du calcium alimentaire","On recommande 800 à 1000 mg par jour."),
  ("Zolédronate IV","Il traite l'hypercalcémie maligne.")],
 "Critères chirurgicaux chez l'asymptomatique (Ve atelier, 2022), un seul suffit : âge < 50 ans, calcémie > 0,25 mmol/L au-dessus de la norme, T-score ≤ −2,5 ou fracture vertébrale, DFGe < 60, calcul, hypercalciurie (DX.5).",
 "Signes neurocognitifs et qualité de vie ne sont pas des critères opératoires.",
 B(5,8))

q("D","DX.5 vs HHF · clairance","assessment_diagnosis","cabinet",
 "Un homme de 40 ans a une calcémie corrigée à 2,68 mmol/L et une PTH normale-haute. Le rapport de clairance calcium/créatinine est de 0,006.",
 "Quel diagnostic faut-il évoquer avant toute chirurgie ?",
 [("Hypercalcémie hypocalciurique familiale",""),
  ("Hyperparathyroïdie primaire typique","Un rapport > 0,02 l'évoque ; < 0,01 évoque l'HHF."),
  ("Hypercalcémie maligne","La PTH n'est pas basse."),
  ("Intoxication à la vitamine D","Elle donne une PTH basse."),
  ("Syndrome de Sjögren","Sans rapport avec la calcémie.")],
 "Rapport de clairance < 0,01 : hypercalcémie hypocalciurique familiale, où la chirurgie est contre-indiquée ; > 0,02 : forme primaire ; zone grise pour 40 % des patients (DX.5).",
 "Thiazidiques et lithium peuvent simuler ou aggraver une hyperparathyroïdie.",
 B(5,14), niv="approfondissement")

q("D","DX.5 · cinacalcet","management","hôpital",
 "Un homme de 82 ans, inopérable, a une hyperparathyroïdie primaire symptomatique ; on débute Cinacalcet-Mepha.",
 "Quel schéma correspond à l'AIPS ?",
 [("30 mg 2 fois par jour ; calcémie à 1 semaine",""),
  ("90 mg 4 fois par jour d'emblée","Dose maximale atteinte par paliers de 2 à 4 semaines."),
  ("30 mg 1 fois par semaine","Pas le schéma AIPS."),
  ("60 mg par jour sans contrôle","La calcémie se contrôle 1 semaine après le début."),
  ("30 mg 2 fois par jour ; calcémie à 6 mois","Contrôle trop tardif : 1 semaine, puis tous les 2 à 3 mois.")],
 "AIPS : 30 mg 2 fois par jour, paliers de 2 à 4 semaines jusqu'à 90 mg 3 à 4 fois par jour ; calcémie 1 semaine après le début puis tous les 2 à 3 mois. Contre-indication : hypocalcémie.",
 "Alerte : calcémie < 2,1 mmol/L ou symptômes d'hypocalcémie.",
 PA("ssp-p11","§11.C Surveillance"), niv="specialiste", spe="Endocrinologie")

q("D","DX.6 · score ACR/EULAR","assessment_diagnosis","cabinet",
 "Une femme de 52 ans a une sécheresse buccale et oculaire depuis 2 ans. Anti-SSA positifs ; test de Schirmer 4 mm en 5 minutes. Pas de biopsie. Aucun critère d'exclusion.",
 "Quel est le score ACR/EULAR 2016 et la conclusion ?",
 [("4 points : syndrome de Sjögren classé",""),
  ("3 points : non classé","Le Schirmer ≤ 5 mm ajoute 1 point aux 3 de l'anti-SSA."),
  ("6 points : classé","L'anti-SSA vaut 3, le Schirmer 1."),
  ("2 points : non classé","L'anti-SSA vaut à lui seul 3 points."),
  ("Biopsie indispensable pour conclure","Le seuil de 4 est atteint sans elle.")],
 "ACR/EULAR 2016 : anti-SSA 3 ; sialadénite focale 3 ; OSS ≥ 5 : 1 ; Schirmer ≤ 5 mm/5 min : 1 ; débit salivaire ≤ 0,1 mL/min : 1. Score ≥ 4 = classé (sensibilité 96 %, spécificité 95 %) (DX.6).",
 "Ce sont des critères de classification, non de diagnostic clinique.",
 B(6,8))

q("D","DX.6 · pilocarpine","management","cabinet",
 "Une femme de 60 ans a un syndrome de Sjögren primaire avec xérostomie gênante ; il reste des glandes fonctionnelles.",
 "Quelle posologie de pilocarpine (Salagen®) l'AIPS indique-t-elle ?",
 [("5 mg 4 fois par jour, pendant les repas",""),
  ("5 mg 1 fois par jour","Dose insuffisante selon l'AIPS."),
  ("30 mg 1 fois par jour","Dose maximale citée après radiothérapie, pas le schéma du Sjögren."),
  ("10 mg 4 fois par jour","Au-dessus du schéma AIPS."),
  ("5 mg 3 fois par jour","Schéma après radiothérapie ORL.")],
 "AIPS Salagen® (Sjögren) : 5 mg 4 fois par jour pendant les repas ; effet complet en 6 semaines ; arrêt sans amélioration après 2 à 3 mois ; sudation chez environ 50 % (DX.6).",
 "Soins buccodentaires et substituts salivaires complètent le traitement.",
 B(6,14))

q("D","DX.6 · anti-SSA seul","assessment_diagnosis","cabinet",
 "Une femme de 45 ans a une bouche sèche et des anti-SSA positifs. Schirmer 12 mm, débit salivaire 0,3 mL/min, coloration oculaire normale, pas de biopsie.",
 "Quelle conclusion est correcte ?",
 [("Score de 3 : critères non atteints",""),
  ("Score de 4 : Sjögren classé","Seul l'anti-SSA compte ici (3 points)."),
  ("Les anticorps antinucléaires suffiraient à conclure","Ils ne comptent pas dans le score."),
  ("Sjögren exclu définitivement","Une biopsie focale (3 points) pourrait compléter."),
  ("Diabète insipide associé","La bouche sèche ne crée pas de polyurie.")],
 "Un anti-SSA seul (3 points) ou une biopsie seule (3 points) n'atteint pas 4 ; les trois tests de sécheresse totalisent 3 points (DX.6).",
 "Exclusions : radiothérapie cervicale, hépatite C active, VIH avancé, sarcoïdose, amylose, GvH, maladie IgG4.",
 B(6,8), niv="approfondissement")

q("D","DX.6 · lymphome","assessment_diagnosis","cabinet",
 "Une femme de 63 ans, suivie pour un syndrome de Sjögren, signale depuis 2 mois une tuméfaction parotidienne dure et persistante ; vous palpez des adénopathies.",
 "Quel diagnostic faut-il rechercher ?",
 [("Lymphome",""),
  ("Poussée de sécheresse simple","Une parotide dure et persistante n'est pas une simple poussée."),
  ("Diabète insipide","Aucun lien avec une masse parotidienne."),
  ("Hyperparathyroïdie","Sans rapport."),
  ("Effet indésirable de la pilocarpine","Elle provoque une sudation, pas une masse.")],
 "Une tuméfaction parotidienne dure ou persistante, des adénopathies, des cryoglobulines ou un C4 bas font redouter un lymphome dans le Sjögren (DX.6).",
 "Un purpura impose aussi la recherche d'une vascularite.",
 B(6,14), niv="approfondissement")

q("D","DX.7 · lithiémie","management","cabinet",
 "Une femme de 39 ans débute du lithium (Lithiofor®) pour un trouble bipolaire. Elle demande quand faire la prise de sang de contrôle.",
 "Quelle cible et quel moment de prélèvement sont corrects ?",
 [("0,6 à 1,0 mmol/L, 12 heures après la dernière prise",""),
  ("0,6 à 1,0 mmol/L, 2 heures après la prise","Le prélèvement se fait 12 heures après la dernière prise."),
  ("1,5 à 2,0 mmol/L, à jeun","1,5 mmol/L est le seuil toxique."),
  ("0,2 à 0,4 mmol/L, au coucher","En dessous de la cible thérapeutique."),
  ("Aucune lithiémie si pas de symptôme","La lithiémie est hebdomadaire le premier mois.")],
 "AIPS Lithiofor® : lithiémie cible 0,6 à 1,0 mmol/L, prélevée 12 heures après la dernière prise ; hebdomadaire le 1er mois puis tous les 2 mois. Polyurie et soif chez 30 à 50 % au début (DX.7).",
 "Polydipsie ou polyurie sous lithium : arrêter et consulter (AIPS).",
 PA("ssp-p14","§14 Pièges"))

q("D","DX.7 vs DX.4 · desmopressine","management","cabinet",
 "Un homme de 55 ans a un diabète insipide néphrogénique dû au lithium, prouvé par une copeptine basale élevée. Un collègue propose de la desmopressine.",
 "Quelle réponse est correcte ?",
 [("Inefficace : le rein ne répond plus à l'ADH",""),
  ("Indiquée à 60 µg 3 fois par jour","C'est le schéma du diabète insipide central."),
  ("Indiquée si la natrémie est basse","L'hyponatrémie contre-indique la desmopressine."),
  ("Plus efficace que le thiazide","Le rein résiste à l'AVP : elle n'agit pas."),
  ("Indiquée, à associer à une restriction hydrique stricte","Pas de restriction thérapeutique sous lithium.")],
 "La desmopressine ne corrige pas le diabète insipide du lithium, car le rein ne répond plus à l'ADH (DX.7). Le thiazide a l'indication AIPS du néphrogénique, mais il élève la lithiémie.",
 "Sous lithium : bouche sèche + natrémie normale = soif anticholinergique, pas diabète insipide.",
 B(7,14))

q("D","DX.7 · interactions","management","cabinet",
 "Un homme de 62 ans sous lithium, lithiémie stable à 0,8 mmol/L, se voit prescrire de l'ibuprofène pour une lombalgie et du lisinopril pour une hypertension.",
 "Quel est le risque principal ?",
 [("Hausse de la lithiémie",""),
  ("Baisse de la lithiémie","AINS et IEC la font monter."),
  ("Diabète insipide central","Le lithium agit sur le rein, pas sur l'hypophyse."),
  ("Hypercalcémie maligne","Sans rapport avec ces médicaments."),
  ("Aucun : ces associations sont neutres","AINS, IEC, sartans et diurétiques élèvent la lithiémie.")],
 "AINS, IEC, sartans, diurétiques de l'anse, épargneurs de potassium et thiazidiques font monter la lithiémie : contrôle rapproché ou alternative avec le prescripteur (DX.7).",
 "Toxicité attendue dès 1,5 mmol/L, parfois plus bas chez le sujet sensible.",
 B(7,14), niv="specialiste", spe="Psychiatrie")

q("D","DX.7 · dialyse","management","hôpital",
 "Une femme de 70 ans sous lithium est hospitalisée pour confusion après une gastro-entérite. Lithiémie 4,4 mEq/L ; créatinine nettement élevée.",
 "Quelle mesure faut-il envisager ?",
 [("Dialyse",""),
  ("Réduction de moitié de la dose de lithium","Le lithium s'arrête ; le taux et l'insuffisance rénale imposent la dialyse."),
  ("Hydrochlorothiazide","Il élève la lithiémie."),
  ("Desmopressine","Sans effet sur l'intoxication."),
  ("Contrôle de la lithiémie dans une semaine","Urgence immédiate.")],
 "La dialyse est recommandée si la lithiémie dépasse 4,0 mEq/L avec insuffisance rénale, ou si la conscience baisse, quel que soit le taux (DX.7).",
 "La déshydratation pousse à l'intoxication au lithium : pas de restriction hydrique.",
 B(7,11), niv="specialiste", spe="Néphrologie")

q("D","DX.7 · anticholinergique","assessment_diagnosis","cabinet",
 "Un homme de 76 ans se plaint d'une bouche sèche et boit beaucoup depuis l'introduction d'un médicament anticholinergique pour une vessie hyperactive. Diurèse 1,5 L/24 h ; natrémie 139 mmol/L.",
 "Quelle est l'explication la plus probable ?",
 [("Bouche sèche médicamenteuse",""),
  ("Diabète insipide néphrogénique","Sans polyurie, pas de diabète insipide."),
  ("Polydipsie primaire","La chronologie médicamenteuse et l'absence de polyurie orientent ailleurs."),
  ("Syndrome hyperosmolaire","Aucune hyperglycémie décrite."),
  ("Hypernatrémie","La natrémie est normale.")],
 "Les anticholinergiques assèchent la bouche : la soif naît de la bouche, sans polyurie (DX.7). Critères d'imputabilité : chronologie, mécanisme connu, régression à l'arrêt, autres causes écartées.",
 "Arrêt ou substitution avec le prescripteur.",
 B(7,8), niv="approfondissement")

q("D","DX.8 · enfant déshydraté","management","cabinet",
 "Un garçon de 3 ans, 14 kg, a une gastro-entérite depuis 2 jours ; il a perdu 7 % de son poids. Il boit, n'a pas de sang dans les selles et reste réactif.",
 "Quelle réhydratation est appropriée ?",
 [("Solution orale hypoosmolaire, 100 mL/kg en 6 heures",""),
  ("Solution orale, 50 mL/kg en 6 heures","Volume de la perte < 5 %."),
  ("Perfusion de NaCl 0,9 % en bolus","Le choc n'est pas présent ; l'oral est la première intention."),
  ("Eau plate à volonté","Sans sels : pas une réhydratation adaptée."),
  ("Lopéramide","Pas de traitement de la déshydratation.")],
 "Solution de réhydratation orale hypoosmolaire en première intention : 50 mL/kg en 6 h si perte < 5 %, 100 mL/kg en 6 h si 5 à 10 % (DX.8).",
 "Perte de poids de l'enfant : < 5 % légère, 5 à 10 % moyenne.",
 B(8,11))

q("D","DX.8 · définition","assessment_diagnosis","EMS",
 "Une résidente d'EMS de 88 ans a la bouche sèche et dit avoir soif. Natrémie 146 mmol/L ; urée élevée ; osmolalité sérique 302 mOsm/kg.",
 "Quelle conclusion est la plus appropriée ?",
 [("Déshydratation par perte d'eau établie",""),
  ("Déshydratation exclue : la soif suffit à l'écarter","Aucun signe clinique isolé n'est fiable chez le sujet âgé."),
  ("Déshydratation imminente seulement","295 à 300 = imminente ; > 300 = établie."),
  ("Polydipsie primaire","Le tableau est une perte d'eau."),
  ("Syndrome de Sjögren","La bouche sèche s'explique par la déshydratation biologique.")],
 "Déshydratation par perte d'eau : osmolalité sérique ≥ 295 mOsm/kg (Cochrane 2015) ; 295–300 = imminente, > 300 = établie (DX.8).",
 "Couleur des urines, bouche sèche et soif n'atteignent pas le seuil d'utilité chez les ≥ 65 ans (sensibilité 60 %, spécificité 75 %).",
 B(8,8), niv="approfondissement")

q("D","DX.8 · signe isolé","assessment_diagnosis","EMS",
 "Une infirmière d'EMS demande si une bouche sèche suffit à affirmer la déshydratation d'un résident de 85 ans.",
 "Quelle réponse est correcte ?",
 [("Non, aucun signe clinique isolé n'est fiable",""),
  ("Oui, la bouche sèche est un signe spécifique chez le sujet âgé","Sensibilité 60 %, spécificité 75 % au mieux."),
  ("Oui, si la soif est présente","La soif est aussi peu fiable chez le sujet âgé."),
  ("Oui, si les urines sont foncées","La couleur des urines n'atteint pas le seuil d'utilité."),
  ("Non, seule l'IRM tranche","On mesure l'osmolalité sérique.")],
 "Chez les 65 ans et plus, aucun signe isolé (couleur, densité et volume urinaires, FC, bouche sèche, soif) n'atteint le seuil d'utilité : on mesure l'osmolalité sérique (DX.8).",
 "Prévention : proposer des boissons régulières aux personnes âgées en cas de chaleur.",
 B(8,14), niv="approfondissement")

q("D","DX.9 · potassium","management","urgences",
 "Une femme de 24 ans, diabétique de type 1, est en acidocétose (pH 7,12, β-hydroxybutyrate 4,8 mmol/L). Elle reçoit du NaCl 0,9 % depuis 30 minutes. Kaliémie 3,0 mmol/L.",
 "Quelle est la conduite correcte ?",
 [("Potassium 10 mmol/h ; retarder l'insuline jusqu'à K > 3,5",""),
  ("Insuline 0,1 UI/kg/h immédiatement","Sous 3,5 mmol/L de kaliémie, l'insuline se retarde : le potassium d'abord."),
  ("Bicarbonate de sodium IV","Réservé au pH < 7,0."),
  ("Arrêter la perfusion","Le remplissage se poursuit."),
  ("Insuline et potassium simultanés à pleine dose","Sous 3,5 mmol/L, le potassium vient d'abord.")],
 "Acidocétose (DX.9) : potassium mesuré avant l'insuline ; < 3,5 mmol/L retarde l'insuline et impose du chlorure de potassium à 10 mmol/h ; entre 3,5 et 5,0, ajouter 20 à 30 mmol par litre.",
 "AIPS du KCl : max 10 mmol/h, 40 mmol/L, 200 mmol/j si K > 2,5 mmol/L.",
 B(9,14))

q("D","DX.9 · glucose","management","urgences",
 "Un homme de 30 ans en acidocétose reçoit de l'insuline IV à 0,1 UI/kg/h. Après 5 heures, glycémie 12,8 mmol/L ; pH 7,24 ; β-hydroxybutyrate 2,1 mmol/L.",
 "Quelle est la prochaine étape ?",
 [("Ajouter glucose 5–10 % et réduire l'insuline à 0,05 UI/kg/h",""),
  ("Arrêter l'insuline : la glycémie est presque normale","La cétose persiste ; l'insuline continue avec du glucose."),
  ("Relais sous-cutané immédiat","Les critères de résolution ne sont pas atteints."),
  ("Augmenter l'insuline à 0,2 UI/kg/h","Risque d'hypoglycémie ; la cible est la cétose."),
  ("Bicarbonate IV","pH > 7,0.")],
 "Sous 13,9 mmol/L de glycémie : ajouter glucose 5–10 % et réduire l'insuline à 0,05 UI/kg/h pour continuer à éteindre la cétose (DX.9).",
 "La guérison se juge sur le β-hydroxybutyrate et le pH, pas sur la glycémie.",
 B(9,13))

q("D","DX.9 · résolution","management","hôpital",
 "Une femme de 22 ans traitée pour acidocétose a, au matin : β-hydroxybutyrate 0,4 mmol/L, pH 7,33, bicarbonate 19 mmol/L. Elle mange.",
 "Quelle est l'étape suivante ?",
 [("Relais sous-cutané avec chevauchement de 1 à 2 heures",""),
  ("Poursuivre l'insuline IV 24 heures","L'acidocétose est résolue."),
  ("Arrêter l'insuline IV puis attendre la glycémie du lendemain avant tout relais","Sans chevauchement, la cétose récidive."),
  ("Contrôler la cétonurie avant de décider","La bandelette urinaire mesure l'acétoacétate et trompe."),
  ("Attendre la normalisation du trou anionique","Il n'est pas un critère de guérison.")],
 "Résolution : β-hydroxybutyrate < 0,6 mmol/L et pH ≥ 7,30 ou bicarbonate ≥ 18 mmol/L. Relais sous-cutané avec chevauchement de 1 à 2 heures (DX.9).",
 "Sortie : relais établi, alimentation reprise, cause traitée, éducation et suivi planifiés.",
 B(9,14))

q("D","DX.9 · œdème cérébral de l'enfant","management","hôpital",
 "Un garçon de 9 ans traité pour acidocétose devient, à la 6e heure, céphalalgique, bradycarde et somnolent.",
 "Quelle est la conduite immédiate ?",
 [("Mannitol IV 0,5 à 1 g/kg",""),
  ("Scanner cérébral d'abord","L'imagerie ne doit jamais retarder le traitement."),
  ("Augmenter le débit de perfusion","On réduit le débit, sans hypotension."),
  ("Bicarbonate IV","Pas le traitement de l'œdème cérébral."),
  ("Insuline en bolus","Sans effet sur l'œdème.")],
 "L'œdème cérébral tue l'enfant en acidocétose (0,4 % en Suisse) : mannitol 0,5 à 1 g/kg en 10 à 15 minutes dès la suspicion (ou NaCl 3 % 2,5 à 5 mL/kg), puis imagerie.",
 "Réduire le débit de perfusion, intuber si défaillance respiratoire.",
 B(9,11), niv="specialiste", spe="Pédiatrie")

q("D","DX.10 · insuline","management","urgences",
 "Un homme de 79 ans a un syndrome hyperosmolaire pur (glycémie 45 mmol/L, osmolalité 350 mOsm/kg, β-hydroxybutyrate 0,5 mmol/L, pH 7,38). Il reçoit du NaCl 0,9 % ; la glycémie baisse régulièrement.",
 "Quand faut-il débuter l'insuline ?",
 [("Quand la glycémie cesse de baisser sous perfusion",""),
  ("Immédiatement à 0,1 UI/kg/h","Débit de l'acidocétose ; l'insuline précoce fait chuter volume et osmolalité."),
  ("Immédiatement en bolus de 10 UI","Pas de bolus : l'hydratation prime."),
  ("Jamais","Elle devient nécessaire quand la glycémie ne baisse plus."),
  ("Après normalisation de l'osmolalité","Trop tard : elle démarre quand la glycémie stagne.")],
 "SHH pur (DX.10) : le remplissage vient avant l'insuline ; l'hydratation abaisse déjà la glycémie. L'insuline à 0,05 UI/kg/h démarre quand la glycémie cesse de baisser, d'emblée si β-hydroxybutyrate 1,0 à 3,0 mmol/L.",
 "β-hydroxybutyrate > 3,0 mmol/L ou pH < 7,3 : état mixte → protocole de l'acidocétose (0,1 UI/kg/h).",
 B(10,14))

q("D","DX.10 vs DX.9 · état mixte","management","urgences",
 "Une femme de 68 ans, diabétique de type 2, est confuse et hypovolémique. Glycémie 38 mmol/L, osmolalité 334 mOsm/kg, β-hydroxybutyrate 4,2 mmol/L, pH 7,18, bicarbonate 12 mmol/L.",
 "Quel protocole d'insuline appliquer ?",
 [("Protocole de l'acidocétose, 0,1 UI/kg/h",""),
  ("SHH pur : insuline retardée","La cétonémie > 3,0 et l'acidose imposent le protocole de l'acidocétose."),
  ("Insuline 0,05 UI/kg/h d'emblée","Débit du SHH avec cétose légère (BHB 1,0 à < 3,0)."),
  ("Insuline sous-cutanée basale","Pas dans une crise hyperglycémique."),
  ("Pas d'insuline avant 24 h","Retard dangereux.")],
 "État mixte : hypovolémie, osmolalité ≥ 320, pH < 7,3, bicarbonate < 15, β-hydroxybutyrate > 3,0 mmol/L → protocole de l'acidocétose à 0,1 UI/kg/h. Un tiers des crises chevauchent acidocétose et SHH (DX.10, DX.9).",
 "Toujours : kaliémie avant insuline.",
 B(10,8))

q("D","DX.10 · vitesse","management","hôpital",
 "Chez un homme de 81 ans traité pour SHH, l'osmolalité passe de 352 à 330 mOsm/kg en 2 heures.",
 "Comment interpréter cette évolution ?",
 [("Trop rapide : la cible est 3 à 8 mOsm/kg par heure",""),
  ("Idéale : plus vite, c'est mieux","Une baisse rapide augmente le risque d'œdème cérébral."),
  ("Trop lente","11 mOsm/kg/h dépasse la cible."),
  ("Sans importance si la glycémie baisse","La vitesse d'osmolalité compte en elle-même."),
  ("Signe de guérison","La guérison est une osmolalité < 300 mOsm/kg.")],
 "Dans le SHH (DX.10) : osmolalité ↓ 3 à 8 mOsm/kg/h, glycémie ↓ 5 mmol/L/h au plus (5–6,7 selon les sources), natrémie ↓ ≤ 10 mmol/L en 24 h, pour éviter l'œdème cérébral.",
 "Une natrémie qui monte sous NaCl 0,9 % est attendue : soluté à 0,45 % seulement si l'osmolalité ne baisse plus.",
 B(10,14), niv="approfondissement")

q("D","DX.10 · natrémie qui monte","management","hôpital",
 "Chez une femme de 77 ans traitée pour SHH par NaCl 0,9 %, la natrémie monte de 134 à 140 mmol/L tandis que la glycémie baisse ; l'osmolalité diminue de 4 mOsm/kg/h.",
 "Quelle est la conduite appropriée ?",
 [("Poursuivre le NaCl 0,9 %",""),
  ("Passer immédiatement au NaCl 0,45 %","Seulement si l'osmolalité ne baisse plus."),
  ("Arrêter toute perfusion","Le volume n'est pas restauré."),
  ("Glucose 5 % en remplacement","Il s'ajoute sous 14 mmol/L de glycémie, pas pour la natrémie."),
  ("Desmopressine","Sans indication.")],
 "L'hyperglycémie abaisse la natrémie mesurée ; quand la glycémie baisse, la natrémie remonte. Cette hausse est attendue : on passe au NaCl 0,45 % seulement si l'osmolalité ne baisse plus (DX.10).",
 "Natrémie corrigée de Hillier : + 0,024 × (glycémie mg/dL − 100).",
 B(10,14), niv="approfondissement")

q("D","DX.10 · thromboprophylaxie","management","hôpital",
 "Un homme de 83 ans hospitalisé pour SHH a une clairance de la créatinine à 25 mL/min.",
 "Quelle prophylaxie antithrombotique l'AIPS prévoit-elle ?",
 [("Énoxaparine 20 mg par jour",""),
  ("Énoxaparine 40 mg par jour","Dose standard ; 20 mg si clairance < 30 mL/min."),
  ("Aucune prophylaxie","Elle s'applique pendant tout le séjour."),
  ("Énoxaparine 1 mg/kg 2 fois par jour","Dose curative."),
  ("Aspirine 100 mg","Pas la prophylaxie décrite.")],
 "SHH (DX.10) : prophylaxie antithrombotique pendant tout le séjour ; Clexane® 40 mg par jour (AIPS), 20 mg si clairance < 30 mL/min.",
 "Examiner les pieds chaque jour : le SHH expose aux ulcères de pression.",
 B(10,14), niv="specialiste", spe="Médecine intensive")

q("D","DX.11 · ordre de substitution","management","hôpital",
 "Une femme de 45 ans a un diabète insipide central après la découverte d'une masse sellaire ; le bilan montre aussi une insuffisance corticotrope et thyréotrope.",
 "Quel ordre de substitution faut-il suivre ?",
 [("Glucocorticoïde avant lévothyroxine",""),
  ("Lévothyroxine avant glucocorticoïde","L'insuffisance surrénalienne se traite d'abord."),
  ("Desmopressine seule, sans autre hormone","Le panhypopituitarisme impose la substitution complète."),
  ("Lévothyroxine et glucocorticoïde le même jour, à doses pleines","Le glucocorticoïde vient en premier."),
  ("Aucune substitution avant la chirurgie","L'insuffisance corticotrope se traite sans attendre.")],
 "En cas d'hypopituitarisme, l'insuffisance surrénalienne est exclue ou traitée avant de débuter la thyroxine (DX.11).",
 "Prévenir le patient : le cortisol peut démasquer ou aggraver la polyurie du déficit en AVP.",
 B(11,13))

q("D","DX.11 · après chirurgie hypophysaire","management","hôpital",
 "Un homme de 52 ans a été opéré d'une lésion hypophysaire il y a 2 jours. Il urine abondamment et a soif.",
 "Quelle surveillance s'impose ?",
 [("Natrémie et diurèse au moins quotidiennes",""),
  ("Natrémie à 1 mois seulement","Le diabète insipide postopératoire s'installe vite."),
  ("Restriction hydrique stricte","Expose à l'hypernatrémie."),
  ("IRM quotidienne","La surveillance est biologique et clinique."),
  ("Lithiémie","Sans rapport.")],
 "Après chirurgie hypophysaire : natrémie et diurèse au moins chaque jour (DX.11). Le déficit en AVP s'installe brutalement après chirurgie ou traumatisme.",
 "Score bâlois : antécédent de chirurgie hypophysaire = +50 en faveur du déficit en AVP.",
 PA("ssp-p11","§11.B.1 Lésion hypothalamo-hypophysaire"))

q("D","DX.11 vs DX.2 · natrémie de base","assessment_diagnosis","hôpital",
 "Deux patients ont une polyurie hypotonique avec glycémie et calcémie normales. Le premier a une natrémie de base à 147 mmol/L ; le second à 133 mmol/L.",
 "Quelle orientation est correcte ?",
 [("Premier : déficit en AVP ; second : polydipsie primaire",""),
  ("Premier : polydipsie primaire ; second : déficit en AVP","C'est l'inverse."),
  ("Les deux : polydipsie primaire","Na > 145 désigne le déficit en AVP."),
  ("Les deux : déficit en AVP","Na < 135 désigne la polydipsie primaire."),
  ("La natrémie n'oriente pas","Elle a une spécificité de 100 % à ces seuils.")],
 "Cohorte bâloise (2025) : natrémie de base > 145 mmol/L → déficit en AVP (spécificité 100 %) ; < 135 mmol/L ou copeptine de base > 5,6 pmol/L → polydipsie primaire (spécificité 100 %) (DX.11, DX.2).",
 "Cette approche par étapes conclut chez 75 % des patients sans test dynamique.",
 B(11,8), niv="approfondissement")

q("D","DX.11 · cortisol et polyurie","mechanisms","hôpital",
 "Une femme de 39 ans, avec masse hypothalamique, reçoit de l'hydrocortisone pour une insuffisance corticotrope. Deux jours plus tard, sa polyurie passe de 3 à 7 L.",
 "Quelle explication est la plus probable ?",
 [("Le cortisol démasque un déficit en AVP",""),
  ("Surdosage en hydrocortisone provoquant un diabète sucré","La glycémie n'est pas en cause dans cette chronologie."),
  ("Polydipsie primaire déclenchée par le traitement","Le mécanisme connu est le démasquage du déficit en AVP."),
  ("Diabète insipide néphrogénique iatrogène","Le cortisol n'induit pas de résistance rénale à l'AVP."),
  ("Hypercalcémie","Aucun argument.")],
 "La substitution en cortisol peut démasquer ou aggraver la polyurie du déficit en AVP : il faut en prévenir le patient (DX.11).",
 "Glucocorticoïde avant lévothyroxine.",
 B(11,14), niv="specialiste", spe="Endocrinologie")

q("D","DX.11 · desmopressine et vomissements","management","cabinet",
 "Un homme de 48 ans sous desmopressine pour un déficit en AVP a une gastro-entérite fébrile avec vomissements.",
 "Quelle conduite est appropriée ?",
 [("Suspendre la desmopressine",""),
  ("Doubler la desmopressine","Risque d'hyponatrémie en cas de déséquilibre hydrique."),
  ("Restriction hydrique stricte","Il perd déjà de l'eau."),
  ("Passer à l'hydrochlorothiazide","Traitement du néphrogénique."),
  ("Poursuivre sans changement","La règle est de suspendre.")],
 "Patient sous desmopressine qui vomit ou a de la fièvre : suspendre jusqu'au retour de l'équilibre hydrique (DX.11).",
 "Desmopressine orale contre-indiquée si clairance < 50 mL/min.",
 B(11,14), niv="approfondissement")

q("D","DX.12 · déficit en eau","management","hôpital",
 "Un homme de 78 ans, 70 kg, a une hypernatrémie à 154 mmol/L, sans choc.",
 "Quel est son déficit en eau estimé ?",
 [("Environ 3,5 L",""),
  ("Environ 4,2 L","Calcul avec 0,6 × poids (homme jeune) ; chez l'homme âgé, 0,5."),
  ("Environ 1,5 L","Sous-estimation : 0,5 × 70 × (154/140 − 1)."),
  ("Environ 7 L","Calcul erroné."),
  ("Impossible à estimer","La formule eau totale × (Na/140 − 1) s'applique.")],
 "Déficit en eau = eau totale × (Na/140 − 1). Eau totale : 0,6 × poids (homme jeune), 0,5 (femme jeune, homme âgé), 0,45 (femme âgée). Ici 0,5 × 70 × 0,1 = 3,5 L (DX.12).",
 "Remplacer sur 48 à 72 h par eau libre, orale ou glucose 5 %.",
 B(12,11))

q("D","DX.12 · vitesse de correction","management","hôpital",
 "Un homme de 84 ans a une hypernatrémie à 158 mmol/L de durée inconnue ; il est hémodynamiquement stable.",
 "Quelle vitesse de baisse de la natrémie viser ?",
 [("Moins de 0,5 mmol/L/h, soit 12 mmol/L par jour",""),
  ("1 à 2 mmol/L/h pendant 24 h","Admis seulement dans les 48 premières heures d'une forme aiguë, sur 6 à 8 h."),
  ("Normalisation en 6 heures","Trop rapide pour une forme chronique."),
  ("Moins de 0,1 mmol/L/h","Trop lente : la correction trop lente aggrave le pronostic."),
  ("Aucune limite","La forme chronique impose une limite.")],
 "Hypernatrémie chronique (> 48 h) ou de durée inconnue : baisse < 0,5 mmol/L/h, soit 12 mmol/L par jour (DX.12).",
 "Natrémie toutes les 2 à 4 h au début.",
 B(12,14))

q("D","DX.12 · noradrénaline","management","urgences",
 "Une femme de 75 ans est en choc hypovolémique après une diarrhée profuse ; PA 70/40 mmHg ; natrémie 153 mmol/L. L'interne propose de débuter la noradrénaline.",
 "Quelle réponse est correcte ?",
 [("Remplir d'abord : la noradrénaline seule est contre-indiquée",""),
  ("Noradrénaline seule, sans remplissage préalable, pour gagner du temps","Contre-indiquée seule dans l'hypotension par hypovolémie."),
  ("Glucose 5 % rapide","L'eau libre vient après la restauration du volume."),
  ("Restriction hydrique","Contraire au besoin."),
  ("Desmopressine","Sans indication.")],
 "La noradrénaline ne remplace jamais le remplissage chez un patient hypovolémique : cristalloïde isotonique d'abord (DX.12).",
 "Dose initiale de noradrénaline, avec remplissage : 8 à 12 µg/min.",
 B(12,13))

q("D","DX.12 · correction trop lente","management","soins intensifs",
 "Aux soins intensifs, un patient a une natrémie de 160 mmol/L. L'équipe hésite à accélérer la correction au-delà de 0,5 mmol/L/h.",
 "Que montre la cohorte de 4265 patients citée par le cours ?",
 [("Baisse lente (≤ 0,5 mmol/L/h) : mortalité à 30 jours 50,7 % vs 31,8 %",""),
  ("Baisse rapide : mortalité 50,7 % vs 31,8 %","C'est l'inverse."),
  ("Aucune différence de mortalité","La baisse lente s'associe à une mortalité plus élevée."),
  ("Baisse rapide : œdème cérébral chez 50 %","Pas le résultat rapporté."),
  ("La cohorte portait sur l'hyponatrémie","Elle portait sur une natrémie ≥ 155 mmol/L.")],
 "Cohorte de 4265 patients avec natrémie ≥ 155 mmol/L : baisse ≤ 0,5 mmol/L/h → mortalité à 30 jours 50,7 % ; baisse plus rapide → 31,8 %. Chez l'adulte hospitalisé, la correction rapide n'augmente pas la mortalité (DX.12).",
 "Ne pas corriger trop lentement non plus.",
 B(12,11), niv="specialiste", spe="Médecine intensive")

q("D","DX.12 · pseudo-normonatrémie","assessment_diagnosis","urgences",
 "Un homme de 70 ans diabétique a une natrémie mesurée de 136 mmol/L et une glycémie de 33 mmol/L (≈ 600 mg/dL).",
 "Quelle est sa natrémie corrigée selon Hillier ?",
 [("Environ 148 mmol/L",""),
  ("136 mmol/L : pas de correction","L'hyperglycémie abaisse la natrémie mesurée."),
  ("Environ 128 mmol/L","La correction s'ajoute."),
  ("Environ 160 mmol/L","Calcul erroné."),
  ("Environ 141 mmol/L","Correction insuffisante.")],
 "Hillier : Na corrigée = Na + 0,024 × (glycémie mg/dL − 100) ; 136 + 0,024 × 500 = 148 mmol/L. Une hyperglycémie masque une hypernatrémie (DX.12).",
 "Glycémie en mmol/L × 18 = mg/dL.",
 B(12,8), niv="approfondissement")

q("D","DX.13 vs DX.5 · PTH haute","assessment_diagnosis","hôpital",
 "Une femme de 64 ans traitée pour un cancer du sein a une calcémie corrigée à 3,1 mmol/L et une PTH élevée.",
 "Quel diagnostic faut-il retenir en premier ?",
 [("Hyperparathyroïdie primaire",""),
  ("Hypercalcémie maligne humorale","Elle s'accompagne d'une PTH basse."),
  ("Métastases ostéolytiques","PTH basse attendue."),
  ("Lymphome à calcitriol","PTH basse attendue."),
  ("Intoxication à la vitamine D","PTH basse attendue.")],
 "Une PTH élevée chez un cancéreux hypercalcémique oriente vers l'hyperparathyroïdie primaire (ou un cancer parathyroïdien), pas vers l'hypercalcémie maligne : un cancer connu n'exclut pas une hyperparathyroïdie (DX.13, DX.5).",
 "PTH basse = cause non parathyroïdienne : PTHrP, vitamine D, calcitriol, protéines.",
 B(13,14))

q("D","DX.13 · zolédronate","management","hôpital",
 "Un homme de 71 ans avec métastases osseuses a une calcémie corrigée à 3,3 mmol/L ; il a été réhydraté ; DFGe 65.",
 "Quel schéma de zolédronate (Zometa®) l'AIPS prévoit-il ?",
 [("4 mg IV unique, sur au moins 15 minutes",""),
  ("4 mg IV en bolus de 1 minute","Durée minimale de 15 minutes."),
  ("8 mg IV unique","Dose AIPS : 4 mg."),
  ("4 mg par voie orale chaque jour","Voie et rythme erronés."),
  ("120 mg SC","Dose du dénosumab.")],
 "AIPS Zometa® (hypercalcémie maligne, calcémie corrigée > 3,0 mmol/L) : 4 mg en perfusion IV unique dans 100 mL de NaCl 0,9 % ou glucose 5 %, sur au moins 15 minutes, après contrôle de l'hydratation (DX.13).",
 "Contre-indiqué pendant la grossesse et l'allaitement ; séparé des solutions calciques.",
 B(13,14))

q("D","DX.13 · insuffisance rénale","management","hôpital",
 "Une femme de 76 ans avec cancer pulmonaire a une hypercalcémie maligne à 3,4 mmol/L ; DFGe 24 mL/min après réhydratation.",
 "Quel antirésorptif faut-il préférer ?",
 [("Dénosumab, en surveillant l'hypocalcémie",""),
  ("Zolédronate 4 mg sans précaution","Déconseillé si DFGe < 30 mL/min (AIPS)."),
  ("Calcitonine seule au long cours","Tachyphylaxie en 48 à 72 h."),
  ("Prednisone","Réservée à l'hypercalcémie par calcitriol."),
  ("Furosémide à haute dose","Seulement en cas de surcharge.")],
 "Zolédronate déconseillé si DFGe < 30 mL/min ; le dénosumab reste possible en insuffisance rénale (hors AMM pour cette indication), avec un risque d'hypocalcémie : calcémie dans les 2 semaines (DX.13).",
 "Calcium oral et vitamine D requis sous dénosumab, sauf en cas d'hypercalcémie.",
 B(13,14), niv="specialiste", spe="Oncologie")

q("D","DX.13 · calcitriol","management","hôpital",
 "Un homme de 66 ans atteint d'un lymphome a une calcémie corrigée à 3,2 mmol/L ; PTH basse, PTHrP basse, calcitriol élevé.",
 "Quel traitement spécifique est indiqué après la réhydratation ?",
 [("Glucocorticoïde",""),
  ("Parathyroïdectomie","PTH basse : la parathyroïde n'est pas en cause."),
  ("Cinacalcet","Indiqué dans l'hyperparathyroïdie."),
  ("Vitamine D","Aggraverait l'hypercalcémie."),
  ("Hydrochlorothiazide","Les thiazidiques élèvent la calcémie.")],
 "Hypercalcémie par calcitriol (lymphome, granulomatose) : glucocorticoïde, car les antirésorptifs agissent mal (DX.13).",
 "PTHrP élevée = cause humorale (80 %) ; ostéolyse locale = 20 %.",
 B(13,10), niv="specialiste", spe="Hématologie")

q("D","DX.13 · calcitonine","management","hôpital",
 "Une femme de 59 ans a une hypercalcémie maligne à 3,7 mmol/L ; on ajoute de la calcitonine au zolédronate.",
 "Quelle est la limite principale de la calcitonine ?",
 [("Tachyphylaxie : effet de 48 à 72 heures",""),
  ("Délai d'action de 5 jours","C'est le délai du bisphosphonate ; la calcitonine agit vite."),
  ("Contre-indiquée en cas de calcémie > 3,5 mmol/L","Elle est justement ajoutée dans les formes sévères."),
  ("Elle provoque une hypercalcémie de rebond immédiate","Pas la limite décrite."),
  ("Elle remplace l'hydratation","L'hydratation vient d'abord.")],
 "La calcitonine n'agit que quelques jours (48 à 72 h) à cause de la tachyphylaxie : elle complète l'antirésorptif dans les formes sévères (> 3,5 mmol/L) (DX.13).",
 "Miacalcic® en crise : 5 à 10 UI/kg sur au moins 6 heures.",
 B(13,14), niv="approfondissement")

q("D","DX.13 · mécanisme","mechanisms","hôpital",
 "Un homme de 61 ans avec carcinome épidermoïde pulmonaire, sans métastase osseuse, a une calcémie corrigée à 3,4 mmol/L et une PTH basse.",
 "Quel est le mécanisme le plus probable ?",
 [("Sécrétion de PTHrP",""),
  ("Ostéolyse métastatique locale","Pas de métastase osseuse ; l'ostéolyse explique 20 % des cas."),
  ("Excès de calcitriol","Surtout lymphome et granulomatose."),
  ("Hyperparathyroïdie primaire","PTH basse."),
  ("Insuffisance rénale chronique","Elle n'élève pas la calcémie ainsi.")],
 "La PTHrP explique 80 % des hypercalcémies malignes ; l'ostéolyse locale 20 % (DX.13).",
 "Survie médiane : 52 jours dans les tumeurs solides — discuter tôt les soins palliatifs.",
 B(13,14), niv="approfondissement")

# ═════════════ BLOC P · PIÈGES & ALARMES
q("P","DX.2 🚩hors liste · convulsion","management","urgences",
 "Un homme de 33 ans, schizophrène, connu pour boire « des seaux d'eau », est amené après une crise convulsive. Il est confus ; pas de fièvre. Glycémie capillaire normale.",
 "Quel examen faut-il obtenir immédiatement ?",
 [("Natrémie",""),
  ("IRM cérébrale","L'hyponatrémie se cherche en minutes ; l'imagerie après."),
  ("Électroencéphalogramme","Ne change pas la conduite immédiate."),
  ("Copeptine stimulée","Test de la polyurie stable, jamais en urgence."),
  ("Lithiémie","Utile s'il prend du lithium, mais la natrémie prime.")],
 "Convulsion ou confusion chez un grand buveur d'eau : natrémie immédiate (hors liste, avant E1). Puis restriction hydrique ; NaCl 3 % si symptômes graves (DX.2).",
 "Donner de l'eau ou de la desmopressine aggrave l'hyponatrémie.",
 PA("algo","Algorithme, étape 0"))

q("P","DX.4 vs DX.2 · point brillant","assessment_diagnosis","hôpital",
 "L'IRM d'une patiente polyurique montre l'absence du point brillant de la posthypophyse. L'interne conclut à un diabète insipide central.",
 "Quelle affirmation est correcte ?",
 [("Il manque aussi dans 39 % des polydipsies primaires",""),
  ("Son absence prouve le diabète insipide central","Il manque aussi dans 39 % des polydipsies primaires."),
  ("Il est toujours absent dans le diabète insipide central","Il manque chez 70 % seulement."),
  ("Sa présence exclut le diabète insipide central","Il reste présent chez 30 % des centraux."),
  ("Il distingue central et néphrogénique","Ce n'est pas un test diagnostique fiable.")],
 "Le point brillant manque chez 70 % des diabètes insipides centraux et 39 % des polydipsies primaires : il ne tranche pas. La copeptine stimulée tranche (DX.4, DX.2).",
 "L'IRM cherche une lésion (E5), pas un diagnostic fonctionnel.",
 PA("ssp-p14","§14 Pièges"))

q("P","DX.9 · bicarbonate","management","urgences",
 "Un homme de 27 ans en acidocétose a un pH de 7,08 et un bicarbonate de 8 mmol/L. L'interne veut perfuser du bicarbonate.",
 "Quelle réponse est correcte ?",
 [("Non : le bicarbonate est réservé au pH < 7,0",""),
  ("Oui : bicarbonate < 10 mmol/L","Le critère est le pH < 7,0."),
  ("Oui, systématiquement en acidocétose sévère","Seulement si pH < 7,0."),
  ("Oui, à la place de l'insuline","L'insuline éteint la cétogenèse."),
  ("Oui, avant le remplissage","Le remplissage vient d'abord.")],
 "Acidocétose (DX.9) : bicarbonate seulement si pH < 7,0 (100 mmol dans 400 mL d'eau stérile toutes les 2 h). Perfusion, potassium, insuline restent l'ordre.",
 "Phosphate : seulement si phosphatémie < 1,0 mmol/L avec faiblesse.",
 B(9,14))

q("P","DX.9 · euglycémique","assessment_diagnosis","urgences",
 "Une femme de 31 ans, diabétique de type 1, enceinte de 30 semaines, vomit depuis 24 h. Glycémie 9 mmol/L ; β-hydroxybutyrate 4,0 mmol/L ; pH 7,21.",
 "Quel est le diagnostic ?",
 [("Acidocétose euglycémique",""),
  ("Gastro-entérite simple : glycémie presque normale","La glycémie normale n'exclut pas l'acidocétose."),
  ("Cétose de jeûne sans gravité","pH 7,21 et BHB ≥ 3,0 : acidocétose."),
  ("Syndrome hyperosmolaire","Glycémie basse, cétose forte."),
  ("Acidose lactique","La cétonémie explique l'acidose.")],
 "Environ 10 % des acidocétoses sont euglycémiques (jeûne, grossesse, inhibiteurs du SGLT2). Le diabète connu remplace le critère glycémique (DX.9).",
 "Mesurer cétones et pH même si la glycémie est normale.",
 PA("ssp-p4","§4 Drapeaux rouges, E1"))

q("P","DX.9 · bandelette","assessment_diagnosis","hôpital",
 "Au cours du traitement d'une acidocétose, la cétonurie à la bandelette augmente alors que le patient s'améliore.",
 "Comment interpréter ce résultat ?",
 [("Bandelette trompeuse : suivre le BHB sanguin",""),
  ("Échec du traitement : augmenter le débit d'insuline IV","La bandelette surestime la cétose en phase de guérison."),
  ("Signe d'acidocétose euglycémique","Sans rapport."),
  ("Indication au bicarbonate","Seul un pH < 7,0 l'indique."),
  ("Critère de sortie atteint","La sortie se juge sur BHB < 0,6 et pH ≥ 7,3.")],
 "La bandelette urinaire mesure l'acétoacétate, pas le β-hydroxybutyrate : elle sous-estime la cétose au début et la surestime ensuite. On suit le BHB sanguin (DX.9).",
 "Le trou anionique ne sert ni au diagnostic ni à la guérison.",
 B(9,8), niv="approfondissement")

q("P","DX.8 · lopéramide","management","cabinet",
 "Un homme de 35 ans a une diarrhée sanglante depuis 2 jours avec 39,5 °C ; il a soif et la bouche sèche, sans signe de choc.",
 "Toutes les mesures suivantes sont appropriées, SAUF une. Laquelle ?",
 [("Lopéramide",""),
  ("Réhydratation orale","Appropriée : première intention sans choc."),
  ("Coproculture","Appropriée devant une diarrhée sanglante fébrile."),
  ("Avis infectiologique","Approprié devant une dysenterie."),
  ("Surveillance de la natrémie","Appropriée en cas de déshydratation.")],
 "Le lopéramide est contre-indiqué en cas de diarrhée sanglante avec fièvre (dysenterie) : il aggrave la colite (DX.8).",
 "Drapeau rouge : sang dans les selles + fièvre élevée.",
 B(8,13), pol="negative")

q("P","DX.5 vs DX.13 · furosémide","management","hôpital",
 "Une femme de 70 ans a une crise hypercalcémique (3,6 mmol/L) ; pas de surcharge. Un collègue propose du furosémide IV d'emblée.",
 "Quelle réponse est correcte ?",
 [("Non : réhydrater d'abord ; furosémide seulement si surcharge",""),
  ("Oui : il élimine le calcium urinaire et passe avant toute hydratation","La réhydratation salée vient d'abord."),
  ("Oui, avec une restriction hydrique","Le patient hypercalcémique est déshydraté."),
  ("Oui, à la place du bisphosphonate","Il ne freine pas la résorption osseuse."),
  ("Oui, avec un thiazidique","Les thiazidiques élèvent la calcémie.")],
 "La crise hypercalcémique se traite d'abord par la réhydratation salée ; le furosémide vient seulement en cas de surcharge cardiaque ou rénale (DX.5, DX.13).",
 "L'hypercalcémie rend le tubule résistant à l'AVP : le patient est polyurique et déshydraté.",
 B(5,14))

q("P","DX.7 · restriction sous lithium","management","cabinet",
 "Un patient de 58 ans sous lithium a une polyurie de 6 L. Son médecin envisage de lui demander de boire 1,5 L par jour au maximum.",
 "Quelle est la meilleure réponse ?",
 [("Non : la déshydratation pousse à l'intoxication au lithium",""),
  ("Oui : la restriction corrige le diabète insipide","Elle ne corrige pas la résistance rénale."),
  ("Oui, si la lithiémie est normale","Pas de restriction thérapeutique sous lithium."),
  ("Oui, associée à la desmopressine","La desmopressine est inefficace ici."),
  ("Oui, pour poser le diagnostic à domicile","Seul un test hospitalier surveillé reste possible.")],
 "Un patient sous lithium ne subit pas de restriction hydrique thérapeutique : la déshydratation pousse à l'intoxication. Seul un test diagnostique hospitalier surveillé reste possible (DX.7).",
 "Lithiémie ≥ 1,5 mmol/L : arrêt immédiat.",
 B(7,13))

q("P","DX.13 · calcium total","assessment_diagnosis","hôpital",
 "Un homme de 74 ans dénutri, avec myélome, a un calcium total de 2,5 mmol/L et une albumine très basse ; il est confus et constipé.",
 "Quelle est la prochaine étape ?",
 [("Calcémie corrigée ou calcium ionisé",""),
  ("Conclure à une normocalcémie et chercher une autre cause","Le calcium total trompe si l'albumine est basse."),
  ("IRM hypophysaire","Sans rapport."),
  ("Restriction hydrique","Contre-indiquée en cas d'hypercalcémie."),
  ("Supplément de vitamine D","Dangereux si l'hypercalcémie est confirmée.")],
 "Le calcium total trompe si l'albumine est basse (myélome, dénutrition) : utiliser la calcémie corrigée par l'albumine ou le calcium ionisé (DX.13).",
 "38 % des sorties ne mentionnent pas une hypercalcémie : elle échappe au diagnostic.",
 B(13,14))

q("P","DX.12 · glucose 5 %","management","hôpital",
 "Pour corriger une hypernatrémie, un interne prescrit uniquement du glucose 5 % comme seul apport liquidien pendant 3 jours.",
 "Quel est le problème selon l'AIPS ?",
 [("Le glucose 5 % ne doit jamais être le seul apport liquidien",""),
  ("Le glucose 5 % est contre-indiqué en hypernatrémie","Il apporte l'eau libre ; il n'est simplement jamais seul."),
  ("Il faut du NaCl 3 %","Aggraverait l'hypernatrémie."),
  ("Le glucose 5 % n'apporte pas d'eau libre","Il en apporte après métabolisation."),
  ("Aucun problème","L'AIPS le contre-indique comme seul apport.")],
 "AIPS glucose 5 % : maximum 40 mL/kg/j et 5 mL/kg/h ; contre-indiqué comme seul apport liquidien journalier ; prudence si la fonction rénale est altérée (DX.12).",
 "Choc d'abord (cristalloïde isotonique), eau libre ensuite.",
 B(12,14), niv="approfondissement")

q("P","DX.1 · HbA1c trompeuse","assessment_diagnosis","cabinet",
 "Une femme de 40 ans avec une hémoglobinopathie connue a une soif et une polyurie ; son HbA1c est de 5,8 %.",
 "Quelle conduite est la plus appropriée ?",
 [("Doser la glycémie veineuse",""),
  ("Exclure le diabète sur l'HbA1c","Non fiable en cas d'anémie ou d'hémoglobinopathie."),
  ("Conclure à un prédiabète","Le chiffre n'est pas interprétable."),
  ("Test de privation hydrique","On écarte d'abord un soluté par la glycémie."),
  ("Copeptine basale","Après avoir écarté glucose, calcium et rein.")],
 "L'HbA1c n'est pas fiable en cas d'anémie ou d'hémoglobinopathie ; les critères glycémiques (à jeun ≥ 7,0, aléatoire ≥ 11,1 avec symptômes, HGPO) prennent le relais (DX.1).",
 "Seule la glycémie sépare le diabète insipide du diabète sucré.",
 B(1,8), niv="approfondissement")

# ───────────── META (rendu)
_P = "../../../repo/LOT_Claude_Finaux/LOT_003/LOT_003_Phase_A_V0.html"
META = dict(
 code="G3", lot="LOT_003", version="1.0.0", seed=10, date="2026-11-01",
 titre="Soif excessive, consommation excessive de liquides (polydipsie)",
 titre_court="Soif excessive, polydipsie", n_dx=13,
 note_version="v1 : gabarit Revision (EX/AP/SPE, 💡 fermé) — 1re production G3",
 note_media="Aucune image clinique dans les HTML LOT_003 (Phase A + DX.1–13) : media = null partout, bouton 🖼 absent.",
 intro_R="Assoiffé et confus ? Glycémie, cétones, natrémie d'abord. Stable ? Prouver la polyurie, écarter un soluté, puis l'osmolalité urinaire.",
 intro_D="Les 13 DX du LOT face à face : un signe, un examen qui tranche, une conduite. Les questions AP (bleu) et SPE (violet) sont mêlées aux EX : filtrez par niveau en haut.",
 intro_P="Point brillant, privation hydrique, desmopressine en polydipsie primaire, bicarbonate, bandelette urinaire, lithium et restriction, furosémide, calcium total.",
 verdict_label="Réflexe G3",
 footer="LOT_003 · G3 · Banque « Temps 1 » v1 · Faits issus exclusivement des leçons auditées LOT_003 (Phase A + Phase B DX.1–13) · Type A, une seule meilleure réponse (règles IML) · Aucun cliché dans les sources LOT_003 : aucune image affichée.",
 carte_html="""<div class="reflex"><b>Les 3 questions réflexes devant toute soif excessive</b><ol>
<li><b>Danger maintenant ?</b> Confusion, convulsion, vomissements, Kussmaul, hypotension → <b>glycémie capillaire, cétones, natrémie, gaz du sang</b>.</li>
<li><b>Vraie polyurie ?</b> Diurèse de 24 h &gt; 3 L (&gt; 40–50 mL/kg). Sans polyurie : bouche sèche (Sjögren, anticholinergiques).</li>
<li><b>Soluté ou eau ?</b> Glycémie, calcémie, créatinine ; puis osmolalité urinaire &lt; 300 → <b>copeptine</b>.</li></ol></div>
<div class="map" style="margin-top:10px">
<div class="ax"><h3>🍬 Glucose</h3><ul>
<li>Aléatoire ≥ 11,1 + symptômes → diabète (DX.1), sans 2e test</li>
<li>BHB ≥ 3,0 + pH &lt; 7,30 → acidocétose (DX.9) ; ≈ 10 % euglycémiques</li>
<li>Glycémie très haute, osmolalité ≥ 320, BHB &lt; 3,0 → SHH (DX.10)</li></ul></div>
<div class="ax"><h3>💧 Axe AVP</h3><ul>
<li>Copeptine basale ≥ 21,4 → néphrogénique (DX.4, DX.7)</li>
<li>Stimulée NaCl 3 % &gt; 4,9 (arginine &gt; 3,8) → polydipsie primaire (DX.2)</li>
<li>≤ 4,9 → central (DX.4, DX.11) : IRM</li>
<li>Na ≥ 150 + urine diluée → diabète insipide sans test</li></ul></div>
<div class="ax"><h3>🦴 Calcium · rein</h3><ul>
<li>Ca corrigé haut + PTH haute ×2 → hyperparathyroïdie (DX.5)</li>
<li>Ca corrigé &gt; 3,0 + PTH basse + cancer → maligne (DX.13)</li>
<li>DFGe &lt; 60 ou RAC ≥ 3 &gt; 3 mois → IRC (DX.3)</li></ul></div>
<div class="ax"><h3>🏜 Pertes · sécheresse</h3><ul>
<li>Chaleur, fièvre, diarrhée, osmolalité ≥ 295 → déshydratation (DX.8)</li>
<li>Na &gt; 145, hypotension → E3 (DX.12) : isotonique d'abord</li>
<li>Bouche et yeux secs sans polyurie, anti-SSA → Sjögren (DX.6)</li>
<li>Lithium, diurétique, anticholinergique → DX.7</li></ul></div>
<div class="ax rf"><h3>🚩 Ordre d'exclusion</h3><ol>
<li>0 · <b>Hyponatrémie symptomatique</b> (grand buveur confus ou convulsif)</li><li>E1 Acidocétose (DX.9)</li>
<li>E2 SHH (DX.10)</li><li>E3 Hypernatrémie, choc hypovolémique (DX.12)</li>
<li>E4 Hypercalcémie maligne (DX.13)</li><li>E5 Lésion hypothalamo-hypophysaire (DX.11)</li>
<li>Puis : hyperparathyroïdie, diabète, IRC, médicaments, diabète insipide, polydipsie primaire, Sjögren, déshydratation</li></ol>
<p class="red" style="margin:6px 0 0">Jamais de desmopressine « pour tester » : hyponatrémie en polydipsie primaire.</p></div>
</div>""",
 algo_html=f"""<table class="algo"><tr><th>Si…</th><th>Alors…</th></tr>
<tr class="e"><td>0 · Convulsion ou confusion avec boisson excessive</td><td>Natrémie immédiate ; restriction hydrique ; NaCl 3 % si symptômes graves</td></tr>
<tr class="e"><td>E1 · Glycémie ≥ 11,1 ou diabète connu, vomissements, Kussmaul</td><td>DX.9 : BHB, gaz du sang ; perfusion, potassium, insuline IV</td></tr>
<tr class="e"><td>E2 · Glycémie très haute, osmolalité &gt; 320, cétonémie &lt; 3,0</td><td>DX.10 : hydratation, insuline 0,05 UI/kg/h</td></tr>
<tr class="e"><td>E3 · Hypotension, tachycardie ou Na &gt; 145</td><td>DX.12 : NaCl 0,9 % si choc ; puis eau libre ; correction lente</td></tr>
<tr class="e"><td>E4 · Ca corrigé &gt; 3,0 et PTH basse</td><td>DX.13 : hydratation, bisphosphonate IV, calcitonine</td></tr>
<tr class="e"><td>E5 · Céphalées, trouble visuel, chirurgie hypophysaire</td><td>DX.11 : IRM de la selle, bilan hypophysaire, avis spécialisé</td></tr>
<tr><td>Ca corrigé élevé, PTH haute ou inappropriée</td><td>DX.5 : critères chirurgicaux (âge &lt; 50 ans, T-score ≤ −2,5…)</td></tr>
<tr><td>Glycémie à jeun ≥ 7,0 ou HbA1c ≥ 6,5 %, sans crise</td><td>DX.1 : metformine et mode de vie</td></tr>
<tr><td>DFGe &lt; 60 depuis &gt; 3 mois</td><td>DX.3 : néphrologie, albuminurie</td></tr>
<tr><td>Lithium, diurétique ou anticholinergique récent</td><td>DX.7 : lithiémie ; arrêt ou substitution avec le prescripteur</td></tr>
<tr><td>Urine &lt; 300 mOsm/kg ; copeptine basale ≥ 21,4</td><td>DX.4 néphrogénique : traiter la cause ; thiazide</td></tr>
<tr><td>Basale &lt; 21,4 puis stimulée ≤ 4,9 (arginine ≤ 3,8)</td><td>DX.4 / DX.11 central : IRM ; desmopressine</td></tr>
<tr><td>Stimulée &gt; 4,9 (arginine &gt; 3,8)</td><td>DX.2 : restriction progressive ; TCC ; pas de desmopressine</td></tr>
<tr><td>Bouche et yeux secs sans polyurie, anti-SSA</td><td>DX.6 : score ACR/EULAR ; pilocarpine</td></tr>
<tr><td>Chaleur, fièvre ou diarrhée, urine concentrée</td><td>DX.8 : réhydratation ; surveiller la natrémie</td></tr>
</table>
<p class="intro">Source : <a href="{_P}#algo">Phase A · Algorithme discriminant</a> et <a href="{_P}#ssp-p10">§10 Arbre décisionnel</a>.</p>""",
)
