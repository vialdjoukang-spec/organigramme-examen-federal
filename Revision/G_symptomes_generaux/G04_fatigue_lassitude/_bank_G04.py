# -*- coding: utf-8 -*-
# Banque G4 — Fatigue, lassitude (LOT_004).
# Sources : exclusivement LOT_Claude_Finaux/LOT_004 (Phase A + Phase B DX.1–11, audités C7).
# Convention : opts[0] = bonne réponse (son « pourquoi pas » est ignoré) ; position finale fixée par build_ssp.py (seed).
# dx : le PREMIER DX.n cité = DX cible (couverture) ; les suivants = discrimination croisée.
R = "../../../repo/LOT_Claude_Finaux/LOT_004/"
def PA(sec, label): return (f"{R}LOT_004_Phase_A_V0.html#{sec}", f"Phase A {label}")
def B(n, p): return (f"{R}LOT_004_Phase_B_V0_DX.{n}.html#dx{n}-p{p}", f"Phase B DX.{n} §{p}")

# ═════════════ BLOC R · RAISONNER (avant de nommer le DX)
q("R","DX.5 · bilan sans signe d'appel","assessment_diagnosis","cabinet",
 "Une femme de 38 ans consulte pour une fatigue depuis 2 mois. Pas de perte de poids, pas de fièvre, pas de saignement. L'examen clinique complet est normal ; poids stable. Elle travaille à plein temps et dort 7 heures.",
 "Quelle est la conduite la plus appropriée ?",
 [("Bilan de base limité",""),
  ("TDM thoraco-abdominale pour exclure un cancer","Sans signe d'appel, l'imagerie large n'est pas indiquée : le cancer concerne 0,6 % des consultants fatigués."),
  ("Dosage des marqueurs tumoraux","Ils ne servent pas au dépistage et peuvent être normaux ou élevés sans cancer."),
  ("Polysomnographie d'emblée","Elle relève de la deuxième intention, devant ronflement, apnées ou somnolence."),
  ("Sérologies virales étendues et dépistage cœliaque","Examens de deuxième intention, après une hypothèse ou une première anomalie.")],
 "Sans drapeau rouge, on procède par étapes : anamnèse, examen de la tête aux pieds, puis un bilan de base limité (NFS, CRP, glycémie, TSH, ferritine, créatinine, ALAT). La méta-analyse de 26 études montre que le bilan étendu ne se justifie que devant un signe d'appel.",
 "Revoyez la patiente à 4 à 6 semaines ; la moitié des patients fatigués n'a aucun diagnostic explicatif dans l'année.",
 PA("ssp-p13","§13 Points clés"))

q("R","DX.1 · bilan normal","assessment_diagnosis","cabinet",
 "Un homme de 44 ans, comptable, est fatigué depuis 3 mois. Il dit « ne plus avoir goût à rien » depuis le décès de son père. Examen normal ; NFS, CRP, glycémie, TSH et ferritine normales.",
 "Quelle est la prochaine étape la plus appropriée ?",
 [("PHQ-2, puis PHQ-9 et entretien clinique",""),
  ("TDM cérébrale","Aucun déficit neurologique ni céphalée inhabituelle ne la justifie."),
  ("Dosage du cortisol à 9 h","Examen de deuxième intention devant une suspicion d'insuffisance surrénalienne (hypotension, hyperpigmentation)."),
  ("Polygraphie respiratoire nocturne","Sans ronflement ni somnolence, l'apnée du sommeil n'est pas évoquée."),
  ("Répéter le même bilan sanguin dans 1 mois","Le bilan en cascade n'apporte rien ; l'anhédonie oriente déjà vers l'humeur.")],
 "Devant une fatigue avec bilan de base normal, on cherche toujours la dépression et le trouble du sommeil avant de multiplier les examens. La dépression touche 18,5 % des consultants fatigués en premier recours (méta-analyse 2016). PHQ-2 ≥ 3 → PHQ-9 et entretien, avec évaluation du risque suicidaire.",
 "Un deuil récent n'exclut pas un épisode dépressif : il demande du discernement, pas une étiquette « réactionnelle ».",
 PA("ssp-p10","§10 Arbre décisionnel"))

q("R","DX.1 🚩E1 · idées suicidaires","management","cabinet",
 "Une femme de 51 ans, suivie pour fatigue, a un PHQ-9 à 21. À la question directe, elle dit avoir pensé à « en finir » et avoir mis de côté ses comprimés. Elle est venue seule.",
 "Quelle est la conduite immédiate la plus appropriée ?",
 [("Ne pas la laisser seule, avis psychiatrique urgent",""),
  ("Débuter sertraline 50 mg et la revoir dans 2 semaines","Un plan avec moyens = risque imminent : la sécurité passe avant le traitement."),
  ("Prescrire une psychothérapie et un arrêt de travail","Mesures utiles plus tard ; elles ne protègent pas aujourd'hui."),
  ("Compléter d'abord le bilan somatique de la fatigue","Le drapeau rouge E1 impose une action le jour même."),
  ("Lui demander de rappeler si les idées persistent","Laisser partir une patiente avec plan et moyens est une faute.")],
 "Idées suicidaires avec plan, moyens ou intention : risque de passage à l'acte imminent (🚩 E1, DX.1). On ne laisse pas la patiente seule, on écarte les moyens dangereux et on appelle le psychiatre de garde dans l'heure ; hospitalisation si nécessaire, au besoin sous placement à des fins d'assistance.",
 "Demander directement les idées suicidaires ne provoque pas le geste. Plan de sécurité écrit avant toute sortie.",
 B(1,11))

q("R","DX.4 🚩E2 · polyurie","assessment_diagnosis","cabinet",
 "Un homme de 29 ans se plaint d'une fatigue intense depuis 3 semaines. Il urine la nuit plusieurs fois, a très soif et a perdu 5 kg sans régime. Il a des nausées depuis hier.",
 "Quel examen faut-il réaliser en premier ?",
 [("Glycémie capillaire immédiate",""),
  ("TSH et fT4","Elles font partie du bilan de base, mais polyurie et polydipsie imposent d'abord la glycémie."),
  ("HbA1c au laboratoire dans la semaine","Utile pour confirmer plus tard ; elle ne dit rien de la décompensation aiguë."),
  ("Ferritine et NFS","Le tableau n'oriente pas vers une anémie."),
  ("Échelle d'Epworth","La somnolence n'est pas le problème ici.")],
 "Polyurie et polydipsie avec fatigue sont un drapeau rouge de diabète décompensé (🚩 E2, DX.4) : glycémie capillaire immédiate. Une glycémie très élevée avec nausées impose cétones et gaz du sang, puis avis en urgence.",
 "Nausées, vomissements, respiration ample : dosez les cétones même si la glycémie n'est que modérée.",
 PA("ssp-p4","§4 Démarche, drapeaux rouges"))

q("R","DX.11 🚩E5 · perte de poids","assessment_diagnosis","cabinet",
 "Un homme de 67 ans, ancien fumeur, est fatigué depuis 2 mois. Il a perdu 6 kg sans régime et transpire la nuit. L'examen trouve un ganglion sus-claviculaire dur de 2 cm. NFS, CRP et TSH normales.",
 "Quelle est la prochaine étape la plus appropriée ?",
 [("Imagerie ciblée et avis spécialisé rapide",""),
  ("Réévaluation clinique à 4 à 6 semaines","Le délai convient sans drapeau rouge ; ici, trois drapeaux rouges sont présents."),
  ("Dépistage de la dépression par PHQ-9","Utile en parallèle, mais il ne doit pas retarder la recherche d'une cause grave."),
  ("Antibiothérapie d'épreuve pour adénite","Une adénopathie dure, fixe et persistante oriente vers un lymphome ou un cancer."),
  ("Dosage des marqueurs tumoraux pour décider","Ils ne servent pas au diagnostic ; seule la biopsie prouve.")],
 "Perte de poids, sueurs nocturnes et adénopathie dure sont des drapeaux rouges de néoplasie (🚩 E5, DX.11) : imagerie ciblée et avis spécialisé sous quelques jours, puis biopsie. Un bilan de base normal n'exclut pas un cancer.",
 "Chez les 60 ans et plus, la VPP de la perte de poids pour un cancer dépasse 3 % ; sensibilité 2 à 47 %, spécificité 92 à 99 %.",
 B(11,4))

q("R","DX.6 · fer sans anémie","management","cabinet",
 "Une femme de 35 ans, réglée, se plaint de fatigue depuis 4 mois. Examen normal. Hb 132 g/L, ferritine 22 µg/L, CRP normale. TSH et glycémie normales.",
 "Quelle est la conduite la plus appropriée ?",
 [("Fer oral, contrôle à 6 semaines",""),
  ("Aucun traitement, car l'Hb est normale","Une Hb normale n'exclut pas un déficit en fer, qui peut expliquer la fatigue."),
  ("Carboxymaltose ferrique IV d'emblée","Le fer IV est réservé à l'échec, à l'intolérance ou à l'impossibilité du fer oral."),
  ("Transfusion d'un concentré érythrocytaire","Aucune anémie, a fortiori mal tolérée."),
  ("Gastroscopie et coloscopie avant tout traitement","Chez la femme réglée jeune, les règles expliquent la carence ; l'endoscopie vise l'homme ou la femme ménopausée.")],
 "Chez la femme réglée avec ferritine < 50 µg/L et Hb > 120 g/L, le fer oral réduit la fatigue de 18,9 points de pourcentage de plus que le placebo (Vaucher, CMAJ 2012). Une ferritine < 30 µg/L affirme le déficit en l'absence d'inflammation. Fer oral 50 à 100 mg/j, contrôle à 6 semaines.",
 "Interrogez les règles abondantes et l'alimentation pauvre en viande : elles épuisent les réserves.",
 PA("ssp-p14","§14 Pièges"))

q("R","DX.9 · TSH limite chez l'âgé","management","cabinet",
 "Un homme de 75 ans se plaint de fatigue. TSH 6 mU/L, fT4 normale. Pas de goitre, pas de cardiopathie. Le reste du bilan de base est normal.",
 "Quelle est la conduite la plus appropriée ?",
 [("Pas de traitement hormonal",""),
  ("Lévothyroxine 25 µg/j","L'essai TRUST ne montre aucun bénéfice sur la fatigue après 65 ans dans la forme infraclinique."),
  ("Lévothyroxine 100 µg/j","Dose d'entretien inadaptée, sans indication, et dangereuse chez l'âgé."),
  ("Échographie thyroïdienne urgente","Aucun nodule ni goitre ne la justifie."),
  ("Liothyronine en association","La liothyronine ne s'ajoute pas en routine.")],
 "TSH de 4,0 à 10,0 mU/L avec fT4 normale = hypothyroïdie infraclinique (DX.9). Chez les 65 ans et plus, TRUST (NEJM 2017) ne montre aucun bénéfice du traitement sur la fatigue ; la TSH augmente naturellement avec l'âge et se lit selon des normes adaptées.",
 "Un TSH légèrement élevé n'explique pas la fatigue : cherchez dépression, sommeil, médicaments.",
 PA("ssp-p8","§8 Diagnostic positif"))

q("R","DX.7 · 4 symptômes à 3 mois","assessment_diagnosis","cabinet",
 "Une femme de 34 ans, infirmière, est épuisée depuis 4 mois. Chaque effort (courses, garde) l'« écrase » le surlendemain pendant plusieurs jours. Sommeil non réparateur, difficultés à trouver ses mots. Humeur conservée, plaisir intact. Examen et bilan de base normaux.",
 "Quel est le diagnostic le plus probable ?",
 [("Syndrome de fatigue chronique",""),
  ("Épisode dépressif caractérisé","Ni humeur triste ni anhédonie : critère A (1 ou 2) absent."),
  ("Insomnie chronique","Elle n'explique pas le malaise post-effort retardé."),
  ("Fibromyalgie","Elle exige une douleur diffuse dans au moins 4 régions sur 5, absente ici."),
  ("Trouble anxieux généralisé","Aucune inquiétude excessive ni tension rapportée.")],
 "NICE 2021 : fatigue invalidante aggravée par l'activité, malaise post-effort, sommeil non réparateur et difficultés cognitives, tous présents, fonction nettement réduite, sans autre explication. Suspicion dès 6 semaines chez l'adulte, diagnostic à 3 mois (DX.7). Aucun test ne le confirme.",
 "Le malaise post-effort, retardé de 12 à 72 heures et disproportionné, est le symptôme cardinal ; son absence écarte le diagnostic.",
 PA("ssp-p8","§8 Diagnostic positif"))

q("R","DX.3 vs DX.7 · somnolence","assessment_diagnosis","cabinet",
 "Un homme de 52 ans, IMC 34, se dit « toujours fatigué ». Il s'endort en lisant et a failli s'assoupir au volant. Son épouse rapporte des ronflements et des pauses respiratoires. PA 152/94 mmHg.",
 "Quelle démarche est la plus appropriée ?",
 [("Interdire la conduite et demander une polysomnographie",""),
  ("Prescrire du zolpidem 10 mg pour améliorer le sommeil","Le SAOS suspecté contre-indique le zolpidem et le témazépam."),
  ("Bilan de base et réévaluation à 3 mois","La somnolence au volant est un drapeau rouge : on n'attend pas."),
  ("TCC-I en première intention","La TCC-I traite l'insomnie chronique, non les apnées."),
  ("Évoquer un syndrome de fatigue chronique","La somnolence et les apnées témoignées orientent ailleurs.")],
 "Somnolence diurne, ronflements et apnées témoignées chez un obèse hypertendu évoquent un SAOS (DX.3). La somnolence au volant impose l'arrêt de la conduite jusqu'au bilan ; STOP-Bang ≥ 3 ou apnées témoignées → polysomnographie, pas d'hypnotique ; PPC si IAH confirmé.",
 "Fatigue ≠ somnolence : demandez s'il s'endort en lisant ou au volant (échelle d'Epworth, seuil usuel 10).",
 B(3,10))

q("R","DX.10 · convalescence","management","cabinet",
 "Un homme de 27 ans a eu une infection virale des voies respiratoires il y a 3 semaines. La fièvre a disparu depuis 15 jours, mais il reste fatigué. Pas de dyspnée, pas de douleur thoracique. Examen et constantes normaux.",
 "Quelle est la conduite la plus appropriée ?",
 [("Rassurer, gérer l'énergie, revoir",""),
  ("Poser le diagnostic de syndrome de fatigue chronique","Le soupçon se pose seulement après 6 semaines chez l'adulte, le diagnostic à 3 mois."),
  ("Programme d'exercice gradué à paliers fixes","NICE déconseille l'exercice comme traitement de la fatigue post-infectieuse."),
  ("Sérologies EBV et CMV étendues","Une sérologie ne prouve pas la cause de la fatigue ; aucun test ne pose le diagnostic."),
  ("Arrêt de travail de 3 mois d'emblée","La capacité se juge selon la fonction ; on prévoit un retour adapté.")],
 "Avant 6 semaines, une fatigue après virose correspond le plus souvent à la convalescence : on rassure, on conseille de ne pas dépenser plus d'énergie qu'on en perçoit et on revoit le patient (DX.10). Après 6 semaines avec les 4 symptômes : soupçon de syndrome de fatigue chronique ; confirmation à 3 mois.",
 "Le facteur qui prédit la fatigue prolongée est la sévérité de l'infection aiguë, non les facteurs psychologiques.",
 B(10,10))

q("R","DX.2 · douleur des ceintures","assessment_diagnosis","cabinet",
 "Une femme de 72 ans est fatiguée depuis 6 semaines. Elle a des douleurs des deux épaules et des hanches, avec une raideur matinale d'environ 1 heure. Pas de céphalée, pas de trouble visuel. Pas de synovite périphérique.",
 "Quel examen faut-il demander en premier ?",
 [("CRP et vitesse de sédimentation",""),
  ("IRM des épaules","L'imagerie ne précède pas le marqueur inflammatoire dans ce tableau."),
  ("Critères ACR 2016 de fibromyalgie","Une douleur des ceintures après 50 ans impose d'abord de chercher l'inflammation."),
  ("Biopsie de l'artère temporale d'emblée","Sans céphalée temporale ni trouble visuel, l'artérite n'est pas au premier plan."),
  ("Électromyogramme","Une myopathie se cherche par la CK devant un déficit proximal.")],
 "Douleur bilatérale des épaules, plus de 50 ans, raideur matinale > 45 minutes : polymyalgie rhumatismale à évoquer (DX.2). CRP et VS d'abord, puis avis rhumatologique ; chercher aussi les signes d'artérite à cellules géantes.",
 "Les critères EULAR/ACR 2012 classent, ils ne posent pas le diagnostic. Un bilan normal n'exclut pas une polymyalgie débutante.",
 B(2,13))

q("R","DX.8 · palpitations","assessment_diagnosis","urgences",
 "Une femme de 31 ans arrive aux urgences pour des épisodes de palpitations, sueurs et peur de mourir. Elle est épuisée et dort mal depuis des semaines. FC 104/min, PA 128/80 mmHg. Pas de traitement connu.",
 "Quelle est la prochaine étape la plus appropriée ?",
 [("ECG, TSH, glycémie, électrolytes et hémogramme",""),
  ("Lorazépam 1 mg sublingual et retour à domicile","Le diagnostic de panique est d'exclusion : ECG et biologie d'abord."),
  ("Hospitalisation en psychiatrie","On n'hospitalise pas en psychiatrie avant d'avoir exclu une urgence somatique."),
  ("ISRS et TCC d'emblée","Le traitement suit le diagnostic, qui n'est pas encore posé."),
  ("Holter de 24 h en ambulatoire","Un ECG immédiat passe avant l'enregistrement ambulatoire.")],
 "Avant de conclure à une attaque de panique (DX.8), on exclut une arythmie, une thyrotoxicose, une hypoglycémie et un trouble électrolytique : ECG, TSH, glycémie, électrolytes, hémogramme. L'attaque de panique est un diagnostic d'exclusion.",
 "Une patiente jeune n'est pas à l'abri d'un trouble du rythme. Tachycardie, tremblement, perte de poids : la TSH tranche.",
 B(8,14))

q("R","DX.4 · confirmer","assessment_diagnosis","cabinet",
 "Un homme de 58 ans, asymptomatique, consulte pour une fatigue modérée. HbA1c 6,7 % sur un premier bilan. IMC 29 kg/m². Hb normale, DFGe 78.",
 "Quelle est la prochaine étape la plus appropriée ?",
 [("Confirmer par un second test un autre jour",""),
  ("Retenir le diabète et débuter la metformine","Sans symptôme d'hyperglycémie, deux tests anormaux sont nécessaires."),
  ("Classer d'emblée en diabète de type 1 par auto-anticorps","Le tableau (IMC 29, âge) oriente vers un type 2 ; le diagnostic n'est pas encore posé."),
  ("Mesure continue du glucose pour poser le diagnostic","Elle ne sert pas encore au diagnostic."),
  ("Conclure à un prédiabète","Le prédiabète correspond à une HbA1c de 5,7 à 6,4 %.")],
 "Diabète (DX.4) : HbA1c ≥ 6,5 %, glycémie à jeun ≥ 7,0 mmol/L, glycémie à 2 h de HGPO ≥ 11,1 mmol/L, ou glycémie aléatoire ≥ 11,1 mmol/L avec symptômes. Sans hyperglycémie symptomatique ni crise, un second test anormal un autre jour est requis.",
 "La carence en fer élève l'HbA1c ; l'anémie hémolytique la fausse : utilisez alors la glycémie.",
 B(4,8))

q("R","DX.6 vs DX.11 · homme ferriprive","assessment_diagnosis","cabinet",
 "Un homme de 62 ans se plaint de fatigue et d'essoufflement à l'effort. Hb 104 g/L, VGM 74 fL, ferritine 8 µg/L. Pas de saignement visible. Alimentation variée.",
 "Quelle est la prochaine étape la plus appropriée ?",
 [("Rechercher un saignement digestif",""),
  ("Fer oral seul et contrôle dans 3 mois","On ne traite pas à l'aveugle : la cause doit être cherchée."),
  ("Dosage de la B12 et des folates","Le VGM bas et la ferritine effondrée signent la carence en fer."),
  ("Frottis et ponction médullaire","Une seule lignée atteinte avec ferritine basse n'oriente pas vers la moelle."),
  ("Transfusion de 2 concentrés","Anémie tolérée, au-dessus du seuil restrictif de 70 à 80 g/L.")],
 "Une anémie ferriprive chez l'homme ou la femme ménopausée impose de chercher un saignement digestif ; le cancer colorectal est la cause à exclure (DX.6, DX.11). On ne traite pas à l'aveugle, car cela masque le diagnostic.",
 "Test immunologique des selles positif = coloscopie : il ne pose pas le diagnostic, la biopsie le pose.",
 B(6,13))

q("R","DX.11 🚩 · hypercalcémie maligne","management","urgences",
 "Une femme de 64 ans suivie pour un cancer du sein est confuse, très assoiffée et constipée depuis 5 jours. Calcium corrigé par l'albumine 3,4 mmol/L, créatinine en hausse. PA 102/64 mmHg.",
 "Quelle est la première mesure thérapeutique ?",
 [("Hydratation IV, puis acide zolédronique 4 mg",""),
  ("Acide zolédronique 4 mg IV immédiat, sans perfusion préalable","L'AIPS impose de contrôler l'état hydrique avant Zometa®."),
  ("Dexaméthasone à haute dose","Elle vise la compression médullaire, pas l'hypercalcémie."),
  ("Furosémide IV en première intention","Le patient est déshydraté : on hydrate d'abord."),
  ("Calcium total de contrôle avant toute décision","Le calcium total sous-estime l'hypercalcémie si l'albumine est basse ; le corrigé suffit.")],
 "Calcium corrigé > 3,0 mmol/L chez une patiente cancéreuse = hypercalcémie maligne, urgence oncologique (DX.11). Voie veineuse, ECG, hydratation, puis acide zolédronique 4 mg en perfusion unique d'au moins 15 minutes, sur une voie séparée sans calcium.",
 "Confusion + soif + polyurie + constipation chez un cancéreux : calcémie corrigée immédiate.",
 B(11,11))

q("R","DX.9 · TSH élevée isolée","assessment_diagnosis","cabinet",
 "Une femme de 40 ans, sans projet de grossesse, se plaint de fatigue. TSH 6,2 mU/L, fT4 normale. Pas de goitre. Le reste du bilan est normal.",
 "Quelle est la conduite la plus appropriée ?",
 [("Répéter TSH, fT4 et anti-TPO à 2–3 mois",""),
  ("Lévothyroxine 50 µg/j","Une TSH élevée isolée se confirme avant tout traitement ; le BMJ 2019 déconseille fortement de traiter."),
  ("Échographie thyroïdienne","Sans goitre ni nodule, elle n'est pas indiquée."),
  ("IRM hypophysaire","Une cause centrale se cherche devant une fT4 basse sans TSH élevée."),
  ("Conclure que la TSH explique la fatigue","Une TSH légèrement élevée n'explique pas la fatigue.")],
 "TSH 4,0 à 10,0 mU/L avec fT4 normale = hypothyroïdie infraclinique légère (DX.9, ETA 2013) : on répète après 2 à 3 mois avec les anticorps anti-TPO. On traite d'emblée si TSH > 10 mU/L avant 65 à 70 ans, ou en cas de grossesse ou de projet.",
 "Résultat discordant avec la clinique : pensez à une interférence de la biotine.",
 B(9,14))

q("R","DX.1 · avant l'antidépresseur","management","cabinet",
 "Un homme de 33 ans a un épisode dépressif caractérisé, PHQ-9 à 18. Il raconte qu'il y a 2 ans, il a dormi 3 heures par nuit pendant une semaine, « plein d'énergie », et a dépensé toutes ses économies.",
 "Quelle est la conduite la plus appropriée ?",
 [("Avis psychiatrique, pas d'antidépresseur seul",""),
  ("Sertraline 50 mg/j et contrôle à 2 semaines","Un antidépresseur seul peut induire un virage maniaque."),
  ("Escitalopram 10 mg/j","Même risque de virage, quel que soit l'ISRS."),
  ("Benzodiazépine au long cours","Non indiquée et source de dépendance."),
  ("Thérapie guidée seule, car la forme est légère","PHQ-9 de 16 ou plus = forme plus sévère.")],
 "L'épisode décrit évoque une hypomanie passée : le diagnostic devient un trouble bipolaire (DX.1, drapeau R3). On recherche systématiquement une manie ou une hypomanie avant tout antidépresseur, et on demande un avis psychiatrique.",
 "Trois questions avant l'ISRS : idées suicidaires, manie passée, substances.",
 B(1,10))

q("R","DX.3 · insomnie chronique","management","cabinet",
 "Une femme de 46 ans a du mal à s'endormir et se réveille à 4 h, 4 nuits par semaine depuis 5 mois. Elle est fatiguée et irritable au travail. Pas de ronflement ; humeur conservée ; PHQ-2 à 1. Elle a 8 heures pour dormir.",
 "Quel est le traitement de première intention ?",
 [("TCC-I, en personne ou en ligne",""),
  ("Zolpidem 10 mg pendant 3 mois","Un hypnotique classique ne dépasse pas 4 semaines et vient après la TCC-I."),
  ("Mélatonine Circadin® 2 mg","L'indication AIPS commence à 55 ans."),
  ("Témazépam 20 mg au long cours","Traitement court seulement, avec risque de dépendance."),
  ("Antihistaminique sédatif","Le guide européen le déconseille.")],
 "Insomnie chronique (DX.3) : difficulté d'endormissement ou de maintien ≥ 3 nuits/semaine, ≥ 3 mois, avec retentissement diurne et occasion de dormir adéquate. La TCC-I est le traitement de première ligne ; le médicament vient après son échec.",
 "La TCC-I améliore les symptômes dépressifs ; son effet sur la fatigue n'est pas établi.",
 B(3,13))

q("R","DX.2 🚩 · artérite","management","cabinet",
 "Un homme de 76 ans est fatigué depuis 1 mois. Il décrit une céphalée temporale nouvelle et une douleur de la mâchoire en mastiquant. Hier, il a vu flou de l'œil droit pendant quelques minutes. CRP 68 mg/L.",
 "Quelle est la conduite la plus appropriée ?",
 [("Glucocorticoïde à haute dose sans délai, avis dans les 24 h",""),
  ("Biopsie de l'artère temporale, puis traitement selon le résultat","On ne retarde pas le traitement : le risque est la cécité."),
  ("Prednisone 15 mg/j, comme pour une polymyalgie","Dose de la polymyalgie ; l'artérite demande 40 à 60 mg/j d'équivalent prednisone."),
  ("AINS et contrôle de la CRP à 1 semaine","Ne protège pas la vue."),
  ("IRM cérébrale avant tout traitement","Le tableau est typique ; le corticoïde ne doit pas attendre.")],
 "Céphalée temporale, claudication de la mâchoire et trouble visuel évoquent une artérite à cellules géantes (DX.2, drapeau R1) : glucocorticoïde à haute dose (EULAR : 40 à 60 mg/j d'équivalent prednisone) sans attendre la biopsie, avis rhumatologique et ophtalmologique dans les 24 heures.",
 "Une artère temporale normale à la palpation n'exclut pas l'artérite : l'imagerie ou la biopsie tranche.",
 B(2,10))

q("R","DX.10 🚩 · rate","management","urgences",
 "Un étudiant de 19 ans a une mononucléose diagnostiquée il y a 2 semaines. Il est fatigué et consulte pour une douleur brutale du flanc gauche, sans traumatisme. FC 118/min, PA 98/60 mmHg.",
 "Quelle est la conduite la plus appropriée ?",
 [("Appeler le 144, avis chirurgical",""),
  ("Antalgique et contrôle à 48 h","La douleur brutale du flanc gauche peut être une rupture de rate, urgence vitale."),
  ("Échographie abdominale ambulatoire dans la semaine","Le délai est inacceptable devant une tachycardie et une PA basse."),
  ("Sérologie EBV de contrôle","Elle n'apporte rien à l'urgence."),
  ("Rassurer : fatigue post-infectieuse","Le drapeau rouge impose d'exclure une complication.")],
 "Pendant une mononucléose, la rate est augmentée de volume ; une douleur brutale du flanc gauche évoque une rupture, souvent sans traumatisme (DX.10, drapeau rouge). La conduite (surveillance ou chirurgie) dépend de l'état hémodynamique.",
 "Environ 80 % des ruptures surviennent dans les 3 semaines suivant le début ; mortalité 4,8 %.",
 B(10,14))

q("R","DX.8 · TAG","assessment_diagnosis","cabinet",
 "Une femme de 39 ans se dit épuisée depuis 8 mois. Elle s'inquiète « de tout » (travail, enfants, argent) sans pouvoir s'arrêter, se sent tendue, irritable, dort mal et se concentre difficilement. Humeur et plaisir conservés. TSH et glycémie normales.",
 "Quel est le diagnostic le plus probable ?",
 [("Trouble anxieux généralisé",""),
  ("Trouble panique","Il exige des attaques inattendues et récurrentes, absentes ici."),
  ("Épisode dépressif caractérisé","Humeur et intérêt conservés : critère A (1 ou 2) absent."),
  ("Syndrome de fatigue chronique","Pas de malaise post-effort décrit."),
  ("Phobie sociale","Pas de peur du jugement d'autrui ni d'évitement ciblé.")],
 "TAG (DX.8, DSM-5-TR) : inquiétude excessive sur plusieurs domaines, difficile à contrôler, plus de jours qu'autrement depuis au moins 6 mois, avec au moins 3 symptômes sur 6 (agitation, fatigabilité, concentration, irritabilité, tension musculaire, sommeil), après exclusion d'une cause somatique ou toxique.",
 "L'anxiété perturbe le sommeil, ce qui entretient la fatigue. Le GAD-2 dépiste, l'entretien diagnostique.",
 B(8,8))

q("R","DX.4 · mécanisme","mechanisms","cabinet",
 "Une femme de 49 ans a un diabète de type 2 nouvellement découvert, glycémie à jeun 9,8 mmol/L. Elle demande pourquoi elle est si fatiguée alors que « son sang est plein de sucre ».",
 "Quel mécanisme explique le mieux sa fatigue ?",
 [("Les cellules manquent de glucose malgré l'hyperglycémie",""),
  ("Les cytokines inflammatoires induisent un comportement de maladie","Mécanisme de l'infection ou du cancer."),
  ("Le transport d'oxygène est réduit","Mécanisme de l'anémie ou de la carence en fer."),
  ("Le métabolisme basal est ralenti par déficit hormonal","Mécanisme de l'hypothyroïdie."),
  ("La neurotransmission sérotoninergique est déréglée","Mécanisme de la dépression.")],
 "La fatigue est une voie finale commune. Dans le diabète (DX.4), l'hyperglycémie avec carence d'effet de l'insuline prive les cellules de glucose ; s'y ajoutent la diurèse osmotique par glycosurie (polyurie, polydipsie) et la perte de glucose et d'eau.",
 "Une cause corrigée (glycémie, fer, thyroxine) guérit souvent la fatigue ; une cause psychique ou post-effort demande un suivi.",
 PA("ssp-p3","§3 Physiopathologie"), niv="approfondissement")

q("R","DX.5 · interpréter la fréquence","mechanisms","cabinet",
 "Un médecin de famille lit que 4,3 % des consultants pour fatigue ont une maladie somatique grave. Il hésite à prescrire une imagerie large à tous ses patients fatigués sans signe d'appel.",
 "Quelle interprétation de cette donnée est la plus juste ?",
 [("La fréquence est identique chez les patients non fatigués",""),
  ("La fatigue multiplie par 4 le risque de maladie grave","Les études avec témoins montrent une prévalence identique."),
  ("Un bilan large systématique est donc recommandé","Il ne se justifie que devant un signe d'appel."),
  ("La dépression est plus rare que la maladie grave","La dépression touche 18,5 % des consultants fatigués."),
  ("Un bilan de routine normal exclut une maladie grave","La plupart des diagnostics se posent plus tard.")],
 "Méta-analyse de Stadje (2016) : maladie somatique grave chez 4,3 % (IC 2,7 à 6,7) des consultants fatigués, mais la fréquence est identique chez les patients sans fatigue ; l'association n'est pas forcément causale (DX.5). D'où le bilan limité et la réévaluation à intervalle court.",
 "Un pourcentage décrit sa population, pas une probabilité chez le patient devant vous.",
 B(5,14), niv="approfondissement")

q("R","DX.5 🚩E3 · surrénale","management","urgences",
 "Une femme de 45 ans est amenée aux urgences pour fatigue extrême, vomissements et malaise debout. PA 82/50 mmHg, FC 120/min. Natrémie 128 mmol/L, kaliémie 5,8 mmol/L. Peau hyperpigmentée.",
 "Quelle est la conduite la plus appropriée ?",
 [("Hydrocortisone IV sans attendre le cortisol",""),
  ("Attendre le résultat du cortisol avant tout traitement","Le délai tue : on prélève, puis on traite sans attendre le résultat."),
  ("Cortisol à 9 h en ambulatoire, puis décision","Examen de deuxième intention chez le patient stable ; ici, la crise se traite d'emblée."),
  ("Restriction hydrique pour l'hyponatrémie","La patiente est hypovolémique : il faut au contraire du NaCl 0,9 %."),
  ("Méthylprednisolone en premier choix","L'AIPS désigne l'hydrocortisone comme médicament de choix.")],
 "Hypotension, sodium bas et potassium haut évoquent une crise surrénalienne (DX.5, 🚩 E3), mortelle sans traitement. Voie veineuse, prélèvement de cortisol, ACTH et ionogramme sans retarder le traitement, hydrocortisone IV (Solu-Cortef®) et NaCl 0,9 % (1000 mL la première heure).",
 "Piège : attribuer le malaise à la dépression. Pigmentation des plis palmaires et chute tensionnelle debout orientent vers l'insuffisance surrénalienne.",
 B(5,13))

# ═════════════ BLOC D · DISCRIMINER (DX face à face)
# ── DX.1 Dépression
q("D","DX.1 vs DX.8 · DX.7","assessment_diagnosis","cabinet",
 "Une femme de 47 ans est fatiguée depuis 3 semaines. Elle est triste presque chaque jour, ne prend plus plaisir à rien, dort mal, se sent coupable et ne se concentre plus ; elle a réduit son temps de travail. TSH, NFS et ferritine normales.",
 "Quel est le diagnostic le plus probable ?",
 [("Épisode dépressif caractérisé",""),
  ("Trouble anxieux généralisé","Il exige au moins 6 mois d'inquiétude excessive."),
  ("Syndrome de fatigue chronique","Il exige un malaise post-effort et au moins 3 mois (NICE)."),
  ("Insomnie chronique","L'humeur triste et l'anhédonie dominent ; la durée de 3 mois manque."),
  ("Fatigue post-infectieuse","Aucune infection récente.")],
 "DSM-5-TR : au moins 5 des 9 symptômes, presque chaque jour depuis au moins 2 semaines, dont l'humeur dépressive ou la perte d'intérêt, avec retentissement fonctionnel (DX.1). Ici : humeur triste, anhédonie, insomnie, fatigue, culpabilité, trouble de concentration.",
 "Un PHQ-9 positif dépiste ; seul l'entretien pose le diagnostic.",
 B(1,8))

q("D","DX.1 · forme moins sévère","management","cabinet",
 "Un homme de 36 ans a un épisode dépressif caractérisé, PHQ-9 à 12. Pas d'idée suicidaire, pas d'antécédent de manie, pas de substance. Il préfère éviter les médicaments.",
 "Quelle prise en charge est la plus appropriée ?",
 [("Thérapie guidée, activité physique et réévaluation à 2 semaines",""),
  ("ISRS d'emblée, car toute dépression se traite par médicament","NICE ne propose pas l'antidépresseur en routine dans la forme moins sévère."),
  ("Hospitalisation psychiatrique","Aucun drapeau rouge."),
  ("Benzodiazépine pour améliorer le sommeil","Non indiquée ; ne traite pas la dépression."),
  ("Électroconvulsivothérapie","Réservée à la dépression psychotique ou à la stupeur, sur décision du psychiatre.")],
 "PHQ-9 < 16 = forme moins sévère (NICE 2022) : soutien, activité physique, thérapie guidée ou TCC ; antidépresseur seulement sur choix éclairé. Réévaluation à 2 semaines ; l'effet attendu apparaît en 4 semaines (DX.1).",
 "PHQ-9 ≥ 16 = forme plus sévère : TCC individuelle avec antidépresseur.",
 B(1,10))

q("D","DX.1 · ISRS","management","cabinet",
 "Une femme de 42 ans a un épisode dépressif, PHQ-9 à 19, sans idée suicidaire ni antécédent de manie. Elle accepte une TCC et un antidépresseur ; vous choisissez la sertraline (Zoloft®). Fonction hépatique normale.",
 "Quel schéma correspond à l'AIPS ?",
 [("50 mg/j ; +50 mg/semaine au plus ; maximum 200 mg",""),
  ("25 mg/j, augmenter de 25 mg tous les 2 jours","Paliers trop rapides : la demi-vie d'environ 24 h impose au plus une modification par semaine."),
  ("100 mg/j d'emblée, maximum 400 mg","La dose maximale AIPS est 200 mg/j."),
  ("50 mg/j pendant 4 semaines, puis arrêt brutal du traitement","Le traitement se poursuit au moins 6 mois après la rémission, avec arrêt progressif."),
  ("200 mg/j d'emblée pour un effet plus rapide","On débute à 50 mg ; l'effet apparaît en 2 à 4 semaines quelle que soit la dose.")],
 "Sertraline (Zoloft®) dans la dépression : 50 mg/j en une prise, dose usuelle et initiale ; paliers de 50 mg par semaine au plus ; maximum 200 mg/j ; effet maximal en 2 à 4 semaines (AIPS). Child-Pugh A ou B : dose réduite d'au moins 50 % ; contre-indiquée en Child-Pugh C.",
 "Sertraline + tramadol, triptan ou linézolide : pensez au syndrome sérotoninergique.",
 PA("ssp-p11","§11.B Pharmacologie"), niv="approfondissement")

q("D","DX.1 · durée et suivi","management","cabinet",
 "Un homme de 22 ans débute un ISRS pour un épisode dépressif modéré. Il n'a pas de plan suicidaire mais des pensées de mort passives.",
 "Quand faut-il le revoir pour la première réévaluation ?",
 [("Dans 1 semaine",""),
  ("Dans 2 semaines, comme tout patient","Entre 18 et 25 ans ou en cas de risque suicidaire, la première réévaluation se fait à 1 semaine."),
  ("Dans 4 semaines, quand l'effet apparaît","Délai trop long pour un jeune patient à risque."),
  ("Dans 3 mois","Inadapté au début du traitement."),
  ("Seulement en cas d'aggravation","Le suivi actif est la règle.")],
 "Après un antidépresseur, première réévaluation à 2 semaines, ou à 1 semaine si 18 à 25 ans ou risque suicidaire ; PHQ-9 et risque suicidaire à chaque visite. Poursuite au moins 6 mois après la rémission, arrêt progressif (DX.1).",
 "Les moins de 30 ans ont plus de pensées suicidaires au début d'un antidépresseur.",
 B(1,14), niv="specialiste", spe="Psychiatrie")

q("D","DX.1 · sujet âgé","management","EMS",
 "Une résidente d'EMS de 78 ans, fatiguée et triste depuis 2 mois, a un épisode dépressif modéré. Le psychiatre de liaison propose l'escitalopram (Cipralex®).",
 "Quel schéma et quelle surveillance correspondent à l'AIPS ?",
 [("5 mg au départ, maximum 10 mg ; natrémie au début",""),
  ("10 mg au départ, maximum 20 mg ; pas de contrôle","Au-delà de 65 ans : 5 mg au départ, 10 mg au maximum."),
  ("20 mg d'emblée ; ECG annuel","Dose trop élevée pour l'âge."),
  ("5 mg au départ ; arrêt brutal dès l'amélioration","L'arrêt est progressif, sur au moins 1 à 2 semaines."),
  ("Dose adulte ; surveiller le poids à chaque visite","La surveillance du poids concerne surtout la mirtazapine (Remeron®).")],
 "Chez le sujet âgé, Cipralex® débute à 5 mg, maximum 10 mg ; on surveille la natrémie (femmes âgées à risque d'hyponatrémie) et le risque de fracture. ECG si risque de QT long (DX.1).",
 "Confusion, chutes, nausées sous ISRS chez l'âgé : dosez le sodium.",
 B(1,11), niv="specialiste", spe="Psychogériatrie")

# ── DX.2 Problèmes musculo-squelettiques
q("D","DX.2 vs DX.1 · fibromyalgie","assessment_diagnosis","cabinet",
 "Une femme de 45 ans a des douleurs diffuses dans les 4 membres et le rachis depuis 8 mois, avec fatigue et sommeil non réparateur. Examen articulaire sans synovite. NFS, CRP, VS, CK et TSH normales. Humeur conservée.",
 "Sur quoi repose le diagnostic de fibromyalgie ?",
 [("Indice de douleur diffuse et score de sévérité",""),
  ("Nombre de points douloureux à la pression digitale","Les critères de 2016 ne requièrent plus les points douloureux."),
  ("Un bilan biologique normal suffit","Un bilan normal oriente ; il ne pose pas le diagnostic."),
  ("Une CRP élevée","Elle oriente vers une maladie inflammatoire, non vers la fibromyalgie."),
  ("L'absence de toute autre maladie","Le diagnostic reste valable en présence d'autres maladies.")],
 "Fibromyalgie (ACR 2016, DX.2) : indice de douleur diffuse ≥ 7 avec échelle de sévérité ≥ 5, ou indice 4 à 6 avec échelle ≥ 9 ; douleur dans au moins 4 des 5 régions ; durée ≥ 3 mois. Critères valides pour le diagnostic individuel.",
 "Un bilan normal ne suffit pas : cherchez aussi dépression, trouble du sommeil et hypothyroïdie.",
 B(2,8))

q("D","DX.2 · fibromyalgie, traitement","management","cabinet",
 "La même patiente de 45 ans a une fibromyalgie confirmée. Elle demande « le médicament le plus efficace » pour sa fatigue et ses douleurs.",
 "Quelle mesure a le niveau de recommandation le plus fort ?",
 [("Exercice aérobie régulier",""),
  ("Prégabaline (Lyrica®)","Elle n'a pas l'indication fibromyalgie dans l'AIPS suisse."),
  ("Glucocorticoïde à faible dose","Il traite la polymyalgie, pas la fibromyalgie."),
  ("Repos prolongé","L'inactivité entretient la douleur et la fatigue."),
  ("AINS au long cours","Réservés à la douleur inflammatoire ; risque rénal.")],
 "Dans la fibromyalgie, l'éducation est la première étape et l'exercice est la seule recommandation forte de l'EULAR (2017) ; l'effet des médicaments est modeste (DX.2). TCC si l'humeur est touchée, réadaptation multimodale si handicap sévère.",
 "Lyrica® et la duloxétine ne sont pas indiqués dans la fibromyalgie selon l'AIPS suisse.",
 B(2,14))

q("D","DX.2 · doses EULAR","management","cabinet",
 "Une femme de 70 ans a une polymyalgie rhumatismale typique, sans céphalée ni trouble visuel. CRP 42 mg/L. Le rhumatologue confirme et vous demande de débuter le traitement.",
 "Quelle dose initiale de glucocorticoïde l'EULAR propose-t-elle ?",
 [("15 à 25 mg/j, puis décroissance",""),
  ("40 à 60 mg/j d'équivalent prednisone","Dose de l'artérite à cellules géantes."),
  ("5 mg/j au long cours sans décroissance","Insuffisant au départ ; la décroissance est la règle."),
  ("Paracétamol seul, sans glucocorticoïde","L'antalgique soulage mais ne traite pas l'inflammation de la polymyalgie."),
  ("AINS seuls","Ils ne remplacent pas le glucocorticoïde, auquel la polymyalgie répond vite ; risque rénal.")],
 "EULAR 2025 : polymyalgie 15 à 25 mg/j d'équivalent prednisone, puis décroissance prudente ; artérite 40 à 60 mg/j. Surveillance : CRP, douleur, raideur, et au long cours glycémie, tension, poids, densité osseuse (DX.2).",
 "Tout trouble visuel sous traitement d'une polymyalgie = urgence (artérite).",
 B(2,14), niv="specialiste", spe="Rhumatologie")

q("D","DX.2 · classification","assessment_diagnosis","cabinet",
 "Un médecin assistant calcule un score EULAR/ACR 2012 de 5 chez une patiente de 68 ans avec douleur des épaules et CRP élevée, et conclut : « diagnostic posé ».",
 "Quelle remarque est la plus juste ?",
 [("Ils classent, sans poser le diagnostic",""),
  ("Le diagnostic exige un score de 8","Le seuil de classification est un score d'au moins 4."),
  ("Le score exige une biopsie temporale positive","La biopsie concerne l'artérite."),
  ("Un facteur rhumatoïde positif est requis","L'absence de facteur rhumatoïde et d'ACPA rapporte 2 points."),
  ("La raideur matinale ne compte pas","Une raideur de plus de 45 minutes rapporte 2 points.")],
 "Critères EULAR/ACR 2012 de polymyalgie : âge ≥ 50 ans, douleur bilatérale des épaules, CRP ou VS augmentée ; score ≥ 4 : sensibilité 68 %, spécificité 78 %. Ce sont des critères de classification, non diagnostiques (DX.2).",
 "Raideur > 45 min (2 points), hanche (1), absence de FR et d'ACPA (2), absence de douleur périphérique (1).",
 B(2,8), niv="approfondissement")

# ── DX.3 Troubles du sommeil
q("D","DX.3 · sommeil insuffisant","assessment_diagnosis","cabinet",
 "Un homme de 30 ans, développeur, se dit fatigué. Son agenda du sommeil montre 5 heures par nuit par choix (séries tardives), sans difficulté à s'endormir. Le week-end, il dort 9 heures et va mieux.",
 "Quel est le diagnostic le plus probable ?",
 [("Sommeil insuffisant",""),
  ("Insomnie chronique","L'insomnie exige une difficulté à dormir malgré une occasion adéquate."),
  ("Syndrome d'apnées obstructives du sommeil","Rien n'évoque des apnées, et la récupération le week-end est nette."),
  ("Épisode dépressif caractérisé","Aucun symptôme thymique."),
  ("Syndrome de fatigue chronique","Le repos soulage clairement la fatigue.")],
 "Sommeil insuffisant (DX.3) : durée courte (< 7 heures chez l'adulte) avec fatigue, amélioration quand le sommeil s'allonge. Conduite : allonger le temps au lit, cible ≥ 7 heures.",
 "Agenda du sommeil de 2 semaines : distinguer insomnie, sommeil insuffisant, apnées, jambes sans repos et décalage circadien.",
 B(3,8))

q("D","DX.3 · hypnotique","management","cabinet",
 "Une femme de 72 ans souffre d'insomnie malgré une TCC-I bien conduite. Vous envisagez un hypnotique à court terme. Pas d'apnées.",
 "Quel schéma correspond à l'AIPS ?",
 [("Zolpidem 5 mg, 4 semaines au plus",""),
  ("Zolpidem 10 mg pendant 3 mois","Sujet âgé : 5 mg ; durée maximale 4 semaines."),
  ("Témazépam 20 mg en continu","Sujet âgé : 10 mg ; traitement court seulement."),
  ("Mélatonine à libération rapide","Le guide européen la déconseille."),
  ("Antipsychotique sédatif à faible dose","Le guide européen le déconseille dans l'insomnie.")],
 "Un hypnotique classique ne dépasse pas 4 semaines, arrêt progressif compris (AIPS) ; zolpidem 10 mg/j au maximum, 5 mg chez le sujet âgé ; témazépam 10 mg chez l'âgé. On réduit progressivement pour éviter le sevrage (DX.3).",
 "Zolpidem et témazépam sont contre-indiqués en cas d'apnées du sommeil.",
 B(3,14), niv="approfondissement")

q("D","DX.3 · daridorexant","management","cabinet",
 "Un homme de 54 ans a une insomnie chronique depuis 1 an, échec d'une TCC-I. Le spécialiste du sommeil propose le daridorexant (Quviviq®). Pas d'insuffisance hépatique.",
 "Quel schéma correspond à l'AIPS ?",
 [("50 mg le soir ; revoir dans 3 mois",""),
  ("10 mg le soir, maximum 4 semaines","Schéma du zolpidem."),
  ("2 mg dès 55 ans","Schéma de la mélatonine Circadin®."),
  ("25 mg trois fois par jour pendant les repas","Une seule prise le soir, maximum 50 mg/j."),
  ("50 mg le matin au réveil","La prise se fait dans les 30 minutes avant le coucher.")],
 "Daridorexant (Quviviq®) : insomnie chronique de l'adulte (≥ 3 mois, impact diurne) ; 50 mg le soir dans les 30 minutes avant le coucher, 25 mg possible, maximum 50 mg/j ; 25 mg si insuffisance hépatique modérée. Réévaluer dans les 3 mois. Contre-indiqué en cas de narcolepsie et avec les inhibiteurs puissants du CYP3A4 (DX.3).",
 "Les antagonistes de l'orexine peuvent aussi provoquer un comportement complexe du sommeil.",
 B(3,11), niv="specialiste", spe="Médecine du sommeil")

q("D","DX.3 · SAOS, sévérité","assessment_diagnosis","policlinique",
 "La polysomnographie d'un homme de 58 ans, somnolent, montre un IAH de 34 événements par heure.",
 "Comment classer ce résultat ?",
 [("SAOS sévère",""),
  ("SAOS léger","Léger à modéré : IAH de 5 à moins de 30."),
  ("Examen normal","Un IAH ≥ 5 avec symptômes définit le SAOS."),
  ("Insomnie chronique","L'insomnie est un diagnostic clinique."),
  ("SAOS modéré","IAH ≥ 30 = sévère.")],
 "SAOS (DX.3) : polysomnographie avec IAH ≥ 5 et symptômes ; léger à modéré de 5 à < 30, sévère ≥ 30. Traitement : PPC.",
 "STOP-Bang ≥ 3 : sensibilité 90 % pour un SAOS en clinique du sommeil ; avec un score de 3, probabilité d'un SAOS sévère de 25 %.",
 B(3,8), niv="approfondissement")

# ── DX.4 Diabète
q("D","DX.4 · metformine et rein","management","cabinet",
 "Un homme de 71 ans a un diabète de type 2 nouvellement confirmé. DFGe 26 mL/min/1,73 m². Il n'a pas de maladie cardiovasculaire connue.",
 "Quelle affirmation sur la metformine est juste ?",
 [("Elle est contre-indiquée à ce DFGe",""),
  ("Elle débute à 500 mg/j et monte jusqu'à 3000 mg","Le DFGe < 30 la contre-indique."),
  ("Elle est possible à 1000 mg/j au maximum","Ce plafond vaut pour un DFGe de 30 à 59."),
  ("Elle se contrôle simplement tous les 6 mois","Le contrôle trimestriel vaut pour 30 à 44 ; sous 30, on l'arrête."),
  ("Elle remplace l'insuline dans le type 1","La metformine est le traitement du type 2.")],
 "Metformine (Glucophage®) : contre-indiquée si DFGe < 30 mL/min/1,73 m², acidose métabolique, déshydratation, infection grave, produit de contraste iodé IV. DFGe 30 à 59 : 500 ou 850 mg au départ, maximum 1000 mg/j (DX.4).",
 "Arrêt 48 h avant un produit de contraste iodé si le DFGe est < 60.",
 PA("ssp-p11","§11.B Pharmacologie"))

q("D","DX.4 · HbA1c faussée","assessment_diagnosis","cabinet",
 "Une femme de 39 ans, fatiguée, a une anémie hémolytique connue. Son HbA1c est de 5,1 %, mais elle a soif et urine beaucoup depuis 2 semaines.",
 "Quel examen faut-il utiliser pour le diagnostic ?",
 [("La glycémie veineuse",""),
  ("Une nouvelle HbA1c dans 3 mois","Elle restera faussée par l'hémolyse."),
  ("Une glycémie capillaire isolée","Une glycémie capillaire ne suffit pas au diagnostic."),
  ("La mesure continue du glucose","Elle ne sert pas encore au diagnostic."),
  ("Le peptide C","Il n'est utile que chez les patients sous insuline.")],
 "L'HbA1c n'est pas fiable en cas d'anémie hémolytique, d'hémoglobinopathie, d'insuffisance rénale sévère ou de grossesse : on utilise la glycémie (DX.4). Avec des symptômes, une glycémie aléatoire ≥ 11,1 mmol/L suffit.",
 "La carence en fer, elle, élève l'HbA1c.",
 PA("ssp-p14","§14 Pièges"))

q("D","DX.4 · SGLT2","assessment_diagnosis","urgences",
 "Un homme de 56 ans, diabétique de type 2 sous empagliflozine (Jardiance®), vomit depuis 24 heures. Il est épuisé et respire amplement. Glycémie 12 mmol/L.",
 "Quel diagnostic faut-il évoquer en premier ?",
 [("Acidocétose euglycémique",""),
  ("Gastro-entérite virale simple","Vomissements et respiration ample imposent les cétones."),
  ("État hyperosmolaire hyperglycémique","La glycémie est trop basse pour ce diagnostic."),
  ("Hypoglycémie sévère","La glycémie est à 12 mmol/L."),
  ("Diabète bien équilibré","La glycémie modérée ne rassure pas sous inhibiteur du SGLT2.")],
 "Sous inhibiteur du SGLT2, l'acidocétose peut survenir avec une glycémie modérée, parfois < 14 mmol/L : on dose les cétones (β-OHB), le gaz du sang, et on arrête l'empagliflozine (DX.4).",
 "Résolution de l'acidocétose : cétones < 0,6 mmol/L et pH ≥ 7,3 (ou bicarbonate ≥ 18 mmol/L).",
 B(4,14), niv="specialiste", spe="Endocrinologie")

q("D","DX.4 · acidocétose, potassium","management","urgences",
 "Une femme de 23 ans, diabétique de type 1, est en acidocétose : β-OHB 4,8 mmol/L, pH 7,18. Le remplissage par NaCl 0,9 % a débuté. Kaliémie 3,1 mmol/L.",
 "Quelle est la conduite la plus appropriée pour l'insuline ?",
 [("Retarder l'insuline et donner du potassium",""),
  ("Débuter l'insuline IV immédiatement","L'insuline fait baisser la kaliémie : sous 3,5 mmol/L, on la retarde."),
  ("Bicarbonate IV avant l'insuline","Pas de bicarbonate en routine."),
  ("Insuline sous-cutanée et retour à domicile","L'acidocétose exige une hospitalisation."),
  ("Ajouter du glucose 5 % d'emblée","Le glucose s'ajoute quand la glycémie passe sous 13,9 mmol/L.")],
 "Acidocétose : remplissage par NaCl 0,9 %, puis insuline IV avec potassium. L'insuline n'est retardée que si K+ < 3,5 mmol/L, jusqu'à ce qu'il remonte ; sinon on ajoute le potassium dès que K+ < 5,0 mmol/L (consensus 2024, DX.4).",
 "Quand la glycémie passe sous 13,9 mmol/L : glucose 5 à 10 % et insuline réduite à 0,05 UI/kg/h.",
 B(4,13), niv="specialiste", spe="Médecine intensive")

q("D","DX.4 · hypoglycémie","management","domicile",
 "Un homme de 66 ans, diabétique sous insuline, est retrouvé inconscient par son épouse. Glycémie capillaire 1,9 mmol/L. Pas d'accès veineux disponible.",
 "Quelle est la première mesure ?",
 [("Glucagon 1 mg SC ou IM",""),
  ("Sucre par voie orale","Contre-indiqué chez un patient inconscient (risque de fausse route)."),
  ("Attendre l'ambulance sans traitement","L'hypoglycémie sévère se corrige vite et doit être traitée immédiatement."),
  ("Insuline rapide","Elle aggrave l'hypoglycémie."),
  ("Metformine 500 mg","Sans effet sur l'hypoglycémie aiguë.")],
 "Hypoglycémie sévère inconsciente (DX.4) : glucagon 1 mg SC ou IM ; sans réponse en 10 minutes, glucose 40 % IV ; dès le réveil, hydrates de carbone par voie orale pour reconstituer le glycogène et éviter la rechute.",
 "Prévenez le patient du risque d'hypoglycémie au volant sous insuline ou sulfamide.",
 B(4,13), niv="approfondissement")

# ── DX.5 Maladie somatique grave
q("D","DX.5 · insuffisance cardiaque","assessment_diagnosis","EMS",
 "Un résident d'EMS de 83 ans est de plus en plus fatigué depuis 1 mois. Il dort avec 3 oreillers. Œdèmes des chevilles, crépitants aux deux bases, galop à l'auscultation.",
 "Quel examen confirme le mieux l'hypothèse principale ?",
 [("NT-proBNP et échocardiographie",""),
  ("TSH et fT4","Un examen d'organe ciblé passe avant le bilan de base devant ces signes cardiaques."),
  ("PHQ-9","Les signes d'organe orientent vers une cause somatique, pas thymique."),
  ("Ferritine et NFS, puis réévaluation","Elles n'expliquent ni les œdèmes ni les crépitants."),
  ("Polysomnographie","L'orthopnée n'est pas une apnée du sommeil.")],
 "Orthopnée, œdèmes, crépitants et galop orientent vers une insuffisance cardiaque (DX.5) : NT-proBNP et échocardiographie. On cherche un signe d'organe ciblé, puis le bilan de l'organe.",
 "Chez la personne âgée, la fatigue seule peut être la seule plainte d'une insuffisance cardiaque.",
 B(5,4))

q("D","DX.5 · endocardite","assessment_diagnosis","cabinet",
 "Un homme de 54 ans, porteur d'une valve aortique mécanique, est fatigué depuis 3 semaines, avec une fébricule le soir. Vous entendez un souffle nouveau.",
 "Quelle est la prochaine étape la plus appropriée ?",
 [("Hémocultures, puis échocardiographie",""),
  ("Antibiothérapie orale d'épreuve pendant 7 jours","Les hémocultures doivent précéder tout antibiotique."),
  ("Réévaluation dans 4 à 6 semaines","Fièvre et souffle nouveau sont des drapeaux rouges."),
  ("Sérologies virales","Elles ne répondent pas à la question de l'endocardite."),
  ("PHQ-9 et entretien","La cause somatique est au premier plan.")],
 "Une fièvre avec souffle nouveau impose des hémocultures puis une échocardiographie (DX.5). Piège : ne pas penser à l'endocardite sans fièvre franche.",
 "Fièvre prolongée ou sueurs nocturnes : infection chronique (tuberculose, endocardite, VIH) ou lymphome.",
 B(5,10))

q("D","DX.5 · résultat isolé","assessment_diagnosis","cabinet",
 "Une femme de 41 ans, fatiguée depuis 6 semaines, sans signe d'appel, a un bilan de base normal sauf une CRP à 7 mg/L (norme < 5). Examen normal.",
 "Quelle interprétation est la plus appropriée ?",
 [("Répéter et corréler à la clinique",""),
  ("La CRP élevée explique à elle seule la fatigue","Un résultat isolé légèrement anormal ne suffit pas à expliquer la fatigue."),
  ("TDM thoraco-abdominale pour exclure un cancer","Elle relève d'un signe d'appel (perte de poids, adénopathie)."),
  ("Biopsie ostéomédullaire","Aucune cytopénie ni signe hématologique."),
  ("Antibiothérapie empirique","Aucun foyer infectieux.")],
 "Un résultat discordant ou limite a une valeur peu spécifique : on le répète, on le corrèle à la clinique et on évite le bilan en cascade (DX.5). Réévaluer à intervalle court.",
 "Une maladie grave peut coexister avec une dépression, fréquente.",
 B(5,8), niv="approfondissement")

q("D","DX.5 · relais oral","management","hôpital",
 "Une femme de 45 ans a été traitée pour une crise surrénalienne par hydrocortisone IV. Elle est stable. L'endocrinologue organise le relais pour une insuffisance surrénale chronique.",
 "Quel schéma oral correspond à l'AIPS ?",
 [("Hydrocortisone orale 10 à 20 mg/j",""),
  ("Méthylprednisolone en premier choix","L'AIPS désigne l'hydrocortisone ou la cortisone comme médicaments de choix."),
  ("Hydrocortisone 100 mg/j au long cours","Dose de crise, pas de substitution."),
  ("Aucun traitement une fois la crise passée","L'insuffisance surrénale chronique demande une substitution."),
  ("Hydrocortisone IV à haute dose prolongée","Le traitement parentéral à hautes doses se limite en général à 48–72 heures (AIPS).")],
 "Relais oral de la substitution (AIPS Hydrocortison Galepharm) : insuffisance surrénale chronique 10 à 20 mg/j, parfois davantage, avec 4 à 6 g de chlorure de sodium ou un minéralocorticoïde (DX.5).",
 "Une corticothérapie prolongée supprime la surrénale : l'arrêt est progressif.",
 B(5,11), niv="specialiste", spe="Endocrinologie")

# ── DX.6 Anémie
q("D","DX.6 · macrocytaire","management","cabinet",
 "Une femme de 70 ans, fatiguée, a des paresthésies des pieds et une marche instable. Hb 98 g/L, VGM 112 fL.",
 "Quelle est la conduite la plus appropriée ?",
 [("Doser B12, folates et MMA",""),
  ("Acide folique seul d'emblée","Il laisse progresser l'atteinte neurologique d'une carence en B12."),
  ("Fer oral","Le VGM haut n'oriente pas vers une carence en fer."),
  ("Transfusion","Anémie tolérée."),
  ("Agent stimulant l'érythropoïèse","Réservé à l'anémie rénale ou chimio-induite.")],
 "Anémie macrocytaire avec troubles neurologiques : carence en B12 à évoquer (DX.6). On dose B12, folates et MMA ; on exclut une carence en B12 avant l'acide folique, car l'atteinte neurologique peut devenir irréversible.",
 "Un VGM normal n'exclut pas une carence mixte : fer et B12 s'annulent.",
 B(6,10))

q("D","DX.6 · hémolyse","assessment_diagnosis","hôpital",
 "Un homme de 34 ans est fatigué depuis 10 jours, avec un ictère et des urines foncées. Hb 96 g/L, VGM 92 fL, réticulocytes élevés. Pas de saignement.",
 "Quels examens confirment le mieux l'hypothèse principale ?",
 [("LDH, haptoglobine, frottis",""),
  ("Ferritine et TSAT","Le tableau n'est pas celui d'une carence en fer."),
  ("Endoscopie digestive haute","Aucun saignement ; ictère et réticulocytes orientent vers l'hémolyse."),
  ("B12 et folates","Le VGM est normal."),
  ("Ponction médullaire d'emblée","Les réticulocytes hauts montrent une moelle qui produit.")],
 "Ictère avec urines foncées = drapeau rouge d'hémolyse (DX.6). VGM normal et réticulocytes hauts : chercher d'abord un saignement, puis une hémolyse (LDH, haptoglobine, frottis).",
 "Piège : donner du fer à une anémie non ferriprive.",
 B(6,4), niv="specialiste", spe="Hématologie")

q("D","DX.6 · Ferinject®","management","policlinique",
 "Une femme de 28 ans, enceinte de 9 semaines, a une anémie ferriprive avec intolérance digestive au fer oral.",
 "Quelle affirmation sur le carboxymaltose ferrique (Ferinject®) est juste ?",
 [("Il est contre-indiqué au 1er trimestre",""),
  ("Il est indiqué en première intention au 1er trimestre","L'AIPS le contre-indique au 1er trimestre."),
  ("La dose maximale est de 2000 mg par semaine","Au plus 1000 mg de fer par semaine."),
  ("Il s'associe utilement au fer oral","L'association est déconseillée (AIPS)."),
  ("Aucune surveillance n'est nécessaire après la dose","Surveillance de 30 minutes après la dose.")],
 "Ferinject® : contre-indiqué au 1er trimestre ; au 2e et 3e trimestre, seulement en indication stricte. Dose unique au plus 15 mg/kg en injection ou 20 mg/kg en perfusion, sans dépasser 1000 mg ; maximum 1000 mg par semaine ; Hb au plus tôt 4 semaines après (DX.6).",
 "Doses répétées de Ferinject® avec facteurs de risque : surveiller le phosphate (hypophosphatémie).",
 B(6,14), niv="approfondissement")

q("D","DX.6 · transfusion","management","hôpital",
 "Un homme de 68 ans, hospitalisé et stable, sans cardiopathie, a une Hb de 76 g/L après un saignement digestif contrôlé par endoscopie. Il est asymptomatique au repos.",
 "Quel seuil guide la décision transfusionnelle ?",
 [("Seuil restrictif de 70 à 80 g/L",""),
  ("Transfuser dès que l'Hb est sous 120 g/L","Le seuil OMS définit l'anémie, pas l'indication transfusionnelle."),
  ("Transfuser seulement sous 50 g/L","Trop bas chez un patient hospitalisé."),
  ("Transfuser jusqu'à 130 g/L","Aucune justification."),
  ("Fer IV à la place de toute transfusion","Le fer agit en semaines ; ce n'est pas la question du seuil.")],
 "Choosing Wisely : seuil restrictif d'Hb de 70 à 80 g/L chez le patient hospitalisé stable ; on adapte chez le cardiaque ou l'instable (DX.6). Prélever NFS, groupe, coagulation, ferritine, B12 et folates avant toute transfusion.",
 "La transfusion se réserve aux anémies mal tolérées.",
 B(6,11), niv="approfondissement")

# ── DX.7 Syndrome de fatigue chronique
q("D","DX.7 vs DX.1 · PEM","assessment_diagnosis","cabinet",
 "Un homme de 41 ans est fatigué depuis 5 mois. Il dit ne plus avoir envie de rien et se sentir sans valeur ; un effort ne l'épuise pas davantage les jours suivants. Sommeil perturbé. Bilan de base normal.",
 "Quel diagnostic est le plus probable ?",
 [("Épisode dépressif caractérisé",""),
  ("Syndrome de fatigue chronique","L'absence de malaise post-effort écarte le diagnostic."),
  ("Fatigue post-infectieuse","Aucune infection récente."),
  ("Fibromyalgie","Aucune douleur diffuse."),
  ("Hypothyroïdie","Le bilan de base, TSH comprise, est normal.")],
 "Le malaise post-effort est le symptôme cardinal du syndrome de fatigue chronique ; son absence l'écarte (DX.7). Anhédonie et dévalorisation orientent vers la dépression (DX.1). Les deux peuvent coexister.",
 "PEM absent → chercher dépression, apnée, carence, endocrinopathie.",
 B(7,10))

q("D","DX.7 · référentiels","assessment_diagnosis","cabinet",
 "Une patiente a les 4 symptômes NICE depuis 4 mois. Le consensus D-A-CH (2024) recommande les critères canadiens pour la suite de la prise en charge.",
 "Quelle durée minimale ces critères canadiens exigent-ils chez l'adulte ?",
 [("6 mois",""),
  ("6 semaines","C'est le seuil de suspicion de NICE chez l'adulte."),
  ("3 mois","C'est la durée de diagnostic de NICE, et celle des critères canadiens chez l'enfant."),
  ("2 semaines","Durée de l'épisode dépressif (DSM-5-TR)."),
  ("12 mois","Aucun référentiel ne l'exige.")],
 "Trois référentiels : IOM 2015 (> 6 mois, 3 symptômes obligatoires + 1), NICE 2021 (suspicion 6 semaines, diagnostic 3 mois), critères canadiens (5 critères majeurs + 2 mineurs sur 3 ; 6 mois chez l'adulte, 3 mois chez l'enfant), recommandés par le consensus D-A-CH (DX.7).",
 "Le D-A-CH juge les critères de l'IOM suffisants pour le soupçon, non pour la suite.",
 B(7,8), niv="approfondissement")

q("D","DX.7 · orthostatisme","assessment_diagnosis","cabinet",
 "Une femme de 26 ans avec syndrome de fatigue chronique se plaint d'étourdissements debout. Vous réalisez un test debout de 10 minutes : la FC passe de 72 à 108/min, sans hypotension.",
 "Comment interpréter ce test ?",
 [("Tachycardie orthostatique posturale (POTS)",""),
  ("Test normal","Une hausse d'au moins 30/min chez l'adulte est pathologique."),
  ("Hypotension orthostatique","La pression ne chute pas."),
  ("Insuffisance surrénalienne","Elle se teste par le cortisol à 9 h."),
  ("Arythmie à explorer d'abord par un Holter de 24 h","Syncope ou douleur thoracique imposeraient d'abord un ECG ; ici la réponse est posturale.")],
 "Test debout de 10 minutes : POTS si la FC monte d'au moins 30/min (40 avant 20 ans). L'intolérance orthostatique renforce le diagnostic de syndrome de fatigue chronique (DX.7). Mesures : hydratation, sel, bas de contention, éviter la station debout prolongée.",
 "Les médicaments de l'orthostatisme sévère sont hors indication et réservés à un expert.",
 B(7,14), niv="specialiste", spe="Médecine interne")

q("D","DX.7 · pharmacologie","management","domicile",
 "Une femme de 37 ans avec syndrome de fatigue chronique modéré a des douleurs musculaires. Elle a déjà mal toléré plusieurs médicaments.",
 "Quel principe de prescription est le plus approprié ?",
 [("Commencer à faible dose et augmenter lentement",""),
  ("Débuter à pleine dose pour un effet rapide","Ces patients tolèrent mal : on commence bas."),
  ("Prescrire un traitement curatif du syndrome","Aucun médicament ne guérit le syndrome."),
  ("Suppléments à haute dose","À éviter sans indication."),
  ("Méthylphénidate contre la fatigue","Non recommandé ; il ne guérit pas.")],
 "Aucun médicament ne guérit le syndrome de fatigue chronique ; on traite les symptômes. Le consensus D-A-CH cite des doses de départ de 1/10 à 1/4 de la dose usuelle chez les patients sensibles (DX.7). Paracétamol en première ligne pour la douleur.",
 "Métamizole : agranulocytose possible, indépendante de la dose ; arrêt si fièvre, angine ou aphtes.",
 B(7,11), niv="approfondissement")

# ── DX.8 Troubles anxieux
q("D","DX.8 · trouble panique","assessment_diagnosis","cabinet",
 "Un homme de 28 ans a eu 4 attaques brutales en 2 mois (palpitations, sueurs, tremblements, peur de mourir), sans déclencheur. Depuis, il craint la prochaine et évite les transports. ECG, TSH, glycémie et électrolytes normaux.",
 "Quel est le diagnostic le plus probable ?",
 [("Trouble panique",""),
  ("Trouble anxieux généralisé","Il exige une inquiétude diffuse depuis au moins 6 mois."),
  ("Attaque de panique isolée","Les attaques sont récurrentes, avec inquiétude persistante."),
  ("Phobie spécifique","Les attaques sont inattendues, non liées à un objet précis."),
  ("Épisode dépressif caractérisé","Aucun symptôme thymique décrit.")],
 "Trouble panique (DX.8, DSM-5-TR) : attaques inattendues et récurrentes avec au moins 4 symptômes, suivies d'au moins 1 mois d'inquiétude persistante ou de changement de comportement, après exclusion d'une cause somatique ou toxique.",
 "Une attaque de panique isolée ne suffit pas.",
 B(8,10))

q("D","DX.8 · TAG, première ligne","management","cabinet",
 "Une femme de 39 ans a un TAG avec retentissement marqué, sans amélioration après auto-aide guidée. Elle demande « un calmant ».",
 "Quelle prise en charge est la plus appropriée ?",
 [("TCC ou ISRS/IRSN",""),
  ("Lorazépam au long cours","Les benzodiazépines ne sont pas recommandées dans le TAG."),
  ("Antipsychotique à faible dose","À éviter en soins primaires."),
  ("Hydroxyzine en traitement de fond","Pas de première ligne."),
  ("Simple suivi sans traitement","Retentissement marqué : échelon 3 (TCC ou médicament).")],
 "TAG (DX.8) : TCC (12 à 15 séances hebdomadaires d'une heure) en première intention, ou ISRS/IRSN selon la préférence ; les benzodiazépines ne sont pas recommandées. Le traitement efficace se poursuit au moins un an.",
 "La psychothérapie par psychologue-psychothérapeute sur prescription médicale est remboursée par l'AOS depuis juillet 2022.",
 B(8,13))

q("D","DX.8 · prégabaline","management","cabinet",
 "Un homme de 50 ans a un TAG ; il n'a toléré ni l'escitalopram ni la venlafaxine. Clairance de la créatinine 90 mL/min. Le psychiatre propose la prégabaline (Lyrica®).",
 "Quel schéma correspond à l'AIPS ?",
 [("150 mg/j, jusqu'à 600 mg",""),
  ("10 mg/j, maximum 20 mg","Schéma de l'escitalopram."),
  ("75 mg/j au départ, maximum 225 mg/j","Schéma de la venlafaxine."),
  ("50 mg/j, maximum 100 mg","Schéma de l'hydroxyzine."),
  ("1 mg 2 à 3 fois/j","Schéma du lorazépam.")],
 "Prégabaline (Lyrica®) dans le TAG : 150 mg/j, jusqu'à 600 mg ; réservée si ISRS et IRSN ne sont pas tolérés ; arrêt progressif sur plusieurs semaines ; risque d'abus. Dose réduite si clairance < 60 mL/min (DX.8).",
 "Clairance 30 à 60 : 75 mg/j au départ, 300 mg au plus.",
 B(8,11), niv="specialiste", spe="Psychiatrie")

q("D","DX.8 · grossesse","management","cabinet",
 "Une femme de 31 ans, anxieuse, envisage une grossesse. Elle prend de la paroxétine (Deroxat®) depuis peu et demande si elle peut continuer ou passer à l'hydroxyzine (Atarax®).",
 "Quelle affirmation correspond à l'AIPS ?",
 [("Atarax® est contre-indiqué pendant la grossesse",""),
  ("Deroxat® est le premier choix chez la femme qui envisage une grossesse","Ne pas le débuter : malformations cardiovasculaires au 1er trimestre."),
  ("Atarax® est le premier choix pendant l'allaitement","Il est contre-indiqué pendant la grossesse et l'allaitement."),
  ("Temesta® est sûr au 1er trimestre","Risque de malformations au 1er trimestre."),
  ("Les ISRS n'ont aucun risque après 20 semaines","HPPN : 6 à 12 cas pour 1000, contre 1 à 2.")],
 "AIPS : Atarax® contre-indiqué pendant la grossesse et l'allaitement ; Deroxat® à ne pas débuter chez la femme enceinte ou qui envisage une grossesse (malformation cardiovasculaire environ 1/50 contre 1/100) ; Temesta® à éviter (malformations au 1er trimestre) (DX.8).",
 "Chez l'enfant, la TCC est le premier choix.",
 B(8,11), niv="specialiste", spe="Psychiatrie")

# ── DX.9 Hypothyroïdie
q("D","DX.9 · forme manifeste","management","cabinet",
 "Une femme de 52 ans, frileuse, constipée, fatiguée, a une peau sèche et des réflexes lents. TSH 38 mU/L, fT4 basse. Pas de cardiopathie.",
 "Quelle conduite est la plus appropriée ?",
 [("Lévothyroxine 25 à 50 µg/j, TSH à 2 mois",""),
  ("Répéter la TSH dans 2 à 3 mois avant de traiter","Une TSH élevée avec fT4 basse définit la forme manifeste : traitement indiqué."),
  ("Lévothyroxine 200 µg/j d'emblée","On débute bas et on augmente par paliers de 25 à 50 µg toutes les 2 à 4 semaines."),
  ("Liothyronine en association","La lévothyroxine seule reste la référence."),
  ("IRM hypophysaire","La TSH élevée signe une origine primaire.")],
 "Hypothyroïdie primaire manifeste (DX.9) : TSH élevée et fT4 basse. Lévothyroxine (Euthyrox®) 25 à 50 µg/j le matin à jeun, au moins une demi-heure avant le petit-déjeuner, paliers de 25 à 50 µg toutes les 2 à 4 semaines ; entretien 100 à 200 µg/j ; TSH à 2 mois. Cible TSH 0,4 à 2,5 mU/L.",
 "Âgé ou cardiaque : débuter à 25 µg, ECG avant.",
 B(9,13))

q("D","DX.9 · TSH > 10","management","cabinet",
 "Un homme de 48 ans, peu symptomatique, a une TSH de 13 mU/L contrôlée à 3 mois, fT4 normale, anti-TPO positifs. Pas de cardiopathie.",
 "Quelle conduite l'ETA 2013 recommande-t-elle ?",
 [("Traiter par lévothyroxine",""),
  ("Surveiller sans traiter, car il est peu symptomatique","Avant 65 à 70 ans, une TSH > 10 mU/L se traite même sans symptôme (ETA 2013)."),
  ("Traiter seulement si la TSH dépasse 20 mU/L","C'est le seuil du BMJ 2019, plus restrictif."),
  ("Ajouter la liothyronine","Pas en routine."),
  ("Répéter tous les 2 à 3 mois indéfiniment","La confirmation est faite ; la décision est due.")],
 "Hypothyroïdie infraclinique marquée (TSH > 10 mU/L, fT4 normale) : l'ETA 2013 recommande de traiter avant 65 à 70 ans, même sans symptôme (DX.9). Après 80 à 85 ans, une TSH ≤ 10 se surveille.",
 "Les anticorps anti-TPO signent l'auto-immunité, non le déficit.",
 B(9,14))

q("D","DX.9 · interactions","management","cabinet",
 "Une femme de 60 ans sous lévothyroxine prend aussi du carbonate de calcium et du fer. Sa TSH remonte malgré une bonne observance.",
 "Quel conseil est le plus approprié ?",
 [("Prendre la lévothyroxine au moins 2 h avant fer et calcium",""),
  ("Prendre la lévothyroxine au repas avec le calcium","Un repas réduit l'absorption jusqu'à 20 %."),
  ("Doubler la dose de lévothyroxine sans autre changement","On corrige d'abord l'interaction."),
  ("Arrêter définitivement le calcium","Il suffit de décaler les prises."),
  ("Prendre la lévothyroxine le soir avec le fer","Fer et calcium réduisent l'absorption.")],
 "La lévothyroxine se prend le matin à jeun, au moins une demi-heure avant le petit-déjeuner et au moins 2 heures avant les sels de fer, de calcium et d'aluminium ; 4 à 5 heures avant les résines. IPP, soja et orlistat réduisent aussi l'absorption (DX.9).",
 "Demi-vie d'environ 7 jours : l'équilibre exige plusieurs semaines, d'où la TSH à 2 mois.",
 B(9,11), niv="approfondissement")

q("D","DX.9 · hypothyroïdie centrale","assessment_diagnosis","policlinique",
 "Une femme de 44 ans, fatiguée, a des céphalées et une hypotension orthostatique. fT4 basse, TSH 1,2 mU/L (normale).",
 "Quelle est la prochaine étape la plus appropriée ?",
 [("Cortisol et IRM hypophysaire",""),
  ("Lévothyroxine 50 µg/j immédiatement","Seule, elle peut déclencher une crise surrénalienne : traiter la surrénale d'abord."),
  ("Conclure à un bilan thyroïdien normal","Une fT4 basse sans TSH élevée signe une atteinte hypophysaire."),
  ("Répéter la TSH seule dans 3 mois","Doser seulement la TSH fait manquer la forme centrale."),
  ("Anti-TPO","Ils signent une auto-immunité thyroïdienne, sans lien avec la forme centrale.")],
 "Hypothyroïdie centrale (DX.9) : fT4 basse avec TSH basse ou normale. On cherche une cause hypophysaire (cortisol, IRM, avis endocrinologique) avant la lévothyroxine ; l'AIPS impose de traiter la surrénale d'abord.",
 "Une TSH normale n'exclut pas une dysfonction hypophysaire.",
 B(9,10), niv="specialiste", spe="Endocrinologie")

q("D","DX.9 · coma myxœdémateux","management","urgences",
 "Une femme de 81 ans, hypothyroïdienne non suivie, est retrouvée somnolente en hiver. Température 33,8 °C, FC 46/min, natrémie 126 mmol/L.",
 "Quel est l'ordre thérapeutique correct ?",
 [("Hydrocortisone IV avant ou avec la lévothyroxine IV",""),
  ("Lévothyroxine orale 25 µg/j et retour à domicile le jour même","Urgence vitale de soins intensifs."),
  ("Lévothyroxine IV seule, sans corticoïde","Un déficit surrénalien associé se démasque quand le métabolisme accélère."),
  ("Réchauffement actif rapide seul","On réchauffe passivement ; le traitement hormonal est indispensable."),
  ("Restriction hydrique stricte d'abord","Elle ne traite pas la cause.")],
 "Coma myxœdémateux (DX.9) : soins intensifs ; prélever TSH, fT4, cortisol ; réchauffer passivement ; hydrocortisone (Solu-Cortef®, jusqu'à 100 mg IV) avant ou avec la lévothyroxine IV ; chercher et traiter le facteur déclenchant (froid, infection, sédatif).",
 "Piège : attribuer la somnolence à l'âge ou à la dépression.",
 B(9,14), niv="specialiste", spe="Médecine intensive")

q("D","DX.9 · biotine","assessment_diagnosis","cabinet",
 "Un homme de 39 ans asymptomatique a un bilan thyroïdien discordant avec la clinique. Il prend un complément « cheveux et ongles ».",
 "Quelle hypothèse faut-il évoquer avant de conclure ?",
 [("Interférence de la biotine avec le dosage",""),
  ("Hypothyroïdie centrale","Rien ne l'évoque cliniquement."),
  ("Hypothyroïdie infraclinique à traiter","On ne traite pas un résultat discordant avant d'avoir exclu une interférence."),
  ("Thyroïdite auto-immune","Elle ne donne pas de dosage discordant isolé."),
  ("Effet de l'âge sur la TSH","Le patient a 39 ans.")],
 "Un résultat thyroïdien discordant avec la clinique doit faire penser à une interférence de la biotine avant de conclure (DX.9). Le patient signale la biotine au laboratoire.",
 "Symptômes seuls ou anti-TPO seuls ne suffisent pas : la biologie tranche.",
 B(9,8), niv="approfondissement")

# ── DX.10 Fatigue post-infectieuse
q("D","DX.10 vs DX.7 · 8 semaines","management","cabinet",
 "Une femme de 32 ans est épuisée depuis 8 semaines, après une COVID-19. Elle décrit un malaise post-effort, un sommeil non réparateur et un brouillard cognitif. Bilan de base normal ; pas de drapeau rouge.",
 "Quelle conduite est la plus appropriée ?",
 [("Soupçon de SFC ; revoir à 3 mois",""),
  ("Poser d'emblée le diagnostic de SFC","Le diagnostic se confirme à 3 mois."),
  ("Programme d'exercice progressif forcé","NICE le déconseille, surtout avec malaise post-effort."),
  ("Rassurer : simple convalescence","Après 6 semaines avec les 4 symptômes, on pose le soupçon."),
  ("Sérologies étendues pour trouver la cause","Aucun test ne pose le diagnostic.")],
 "Après une infection, 4 symptômes NICE persistant ≥ 6 semaines chez l'adulte avec activité nettement réduite = soupçon de syndrome de fatigue chronique : gestion de l'énergie, pas d'exercice forcé, réévaluation à 3 mois (DX.10, DX.7).",
 "Environ la moitié des patients post-COVID avec PEM remplit les critères de SFC.",
 B(10,10))

q("D","DX.10 · définition OMS","assessment_diagnosis","cabinet",
 "Un homme de 45 ans a eu une COVID-19 confirmée il y a 4 mois. Fatigue et troubles de concentration depuis 10 semaines, apparus après l'infection, sans autre explication.",
 "Selon l'OMS, ce tableau remplit-il la définition de l'affection post-COVID-19 ?",
 [("Oui, la définition est remplie",""),
  ("Non : il faut 6 mois de symptômes","C'est le délai de l'IOM pour le SFC."),
  ("Non : il faut une sérologie positive","L'infection probable ou confirmée suffit."),
  ("Non : la fatigue n'en fait pas partie","La fatigue en est un symptôme fréquent."),
  ("Oui, dès 4 semaines après l'infection","Le cadre OMS se pose à 3 mois.")],
 "OMS 2022 : infection par le SARS-CoV-2 probable ou confirmée, symptômes habituellement à 3 mois du début, durant au moins 2 mois, non expliqués par un autre diagnostic (DX.10).",
 "Une cohorte suisse : arrêts de travail ≥ 1 mois chez 11,5 % des personnes avec séquelles de COVID-19, contre 4,0 %.",
 B(10,14), niv="approfondissement")

q("D","DX.10 · sérologie","assessment_diagnosis","cabinet",
 "Une femme de 30 ans est fatiguée depuis 5 semaines. Une sérologie montre des IgG anti-EBV positives (contact ancien). Elle demande si « c'est le virus ».",
 "Quelle interprétation est la plus juste ?",
 [("Elle prouve un contact ancien seulement",""),
  ("Elle confirme une fatigue post-infectieuse","Une sérologie ancienne ne prouve pas la cause."),
  ("Elle impose un antiviral","Aucun traitement ne guérit cette fatigue."),
  ("Elle confirme un SFC","Aucun test ne confirme le SFC."),
  ("Elle impose une sérologie de contrôle mensuelle","Aucune utilité.")],
 "Une sérologie EBV ancienne positive prouve un contact ancien, non la cause de la fatigue actuelle (DX.10). Le diagnostic est clinique et d'exclusion ; le bilan de base sert à exclure une autre cause.",
 "Après mononucléose, 13 %, 7 % et 4 % des adolescents ont encore un SFC à 6, 12 et 24 mois.",
 B(10,8), niv="approfondissement")

q("D","DX.10 · enfant","management","cabinet",
 "Une adolescente de 14 ans est épuisée depuis 5 semaines après une mononucléose, avec malaise post-effort et absences scolaires.",
 "Quelle conduite est la plus appropriée ?",
 [("Soupçon de SFC ; avis pédiatrique",""),
  ("Attendre 6 mois avant toute évaluation","Chez l'enfant, le soupçon se pose dès 4 semaines."),
  ("Programme sportif scolaire intensif","L'exercice forcé est déconseillé."),
  ("Antidépresseur d'emblée","Aucune dépression décrite."),
  ("Rassurer sans suivi","Le suivi est nécessaire ; revue tous les 6 mois.")],
 "Chez l'enfant, NICE pose le soupçon de SFC après 4 semaines (6 chez l'adulte) et le confirme à 3 mois ; évaluation par un pédiatre dès 4 semaines ; revue tous les 6 mois (DX.10, DX.7).",
 "Les enfants et adolescents ont de meilleures chances de récupération.",
 B(10,11), niv="specialiste", spe="Pédiatrie")

# ── DX.11 Néoplasie maligne
q("D","DX.11 · histologie","assessment_diagnosis","hôpital",
 "Un homme de 66 ans, fatigué et amaigri, a une masse pulmonaire spiculée au TDM et un CEA élevé. Il demande si « le diagnostic est posé ».",
 "Quel élément pose le diagnostic de cancer ?",
 [("Une biopsie avec histologie",""),
  ("L'image TDM typique","L'image oriente et stadifie ; seule la biopsie prouve."),
  ("Le marqueur tumoral élevé","Il peut être élevé sans cancer ; il sert au suivi."),
  ("La TEP au FDG","Elle stadifie, elle ne prouve pas."),
  ("La perte de poids associée","Elle oriente, elle ne prouve pas.")],
 "Le diagnostic de néoplasie maligne repose sur l'histologie : biopsie examinée par le pathologiste, avec immunohistochimie, qui définit type, grade et cible thérapeutique (DX.11).",
 "Un test immunologique des selles positif impose une coloscopie, qui prélève la lésion.",
 B(11,8))

q("D","DX.11 🚩 · compression médullaire","management","urgences",
 "Un homme de 71 ans avec cancer de la prostate métastatique a une dorsalgie nocturne depuis 2 semaines ; depuis hier, ses jambes sont faibles et il urine mal.",
 "Quelle conduite est la plus appropriée ?",
 [("IRM du rachis entier et dexaméthasone",""),
  ("Radiographie lombaire et antalgiques, puis revoir","Elle ne montre pas la compression ; l'urgence est l'IRM."),
  ("IRM programmée dans la semaine","Le déficit devient irréversible sans traitement rapide."),
  ("Acide zolédronique 4 mg","Il traite l'hypercalcémie maligne."),
  ("Kinésithérapie de renforcement","Le déficit est neurologique.")],
 "Dorsalgie avec faiblesse des jambes ou rétention urinaire chez un cancéreux = compression médullaire (DX.11, E2) : IRM totale du rachis en urgence, corticoïde dès la suspicion, avis de radio-oncologie et de neurochirurgie.",
 "La dorsalgie isolée précède le déficit : elle impose déjà l'IRM chez un patient cancéreux.",
 B(11,10))

q("D","DX.11 vs DX.10 · lymphome","assessment_diagnosis","cabinet",
 "Une femme de 29 ans est fatiguée depuis 2 mois. Fièvre le soir, sueurs nocturnes, perte de 4 kg, adénopathies cervicales indolores de 3 cm. Pas d'infection récente.",
 "Quelle est la démarche la plus appropriée ?",
 [("NFS, LDH, TDM ou TEP, puis biopsie ganglionnaire",""),
  ("Diagnostic de fatigue post-virale et revoir à 3 mois","Le trio fièvre, sueurs, adénopathies ne s'explique pas par une virose bénigne."),
  ("Antibiotique d'épreuve 10 jours","Ne remplace pas l'exploration."),
  ("Ponction à l'aiguille fine seule","La biopsie ganglionnaire envoie un échantillon frais en histologie et en microbiologie."),
  ("Marqueurs tumoraux sériques","Ils ne servent pas au diagnostic.")],
 "Fièvre, sueurs nocturnes et adénopathies indolores évoquent un lymphome (DX.11) : NFS, LDH, imagerie (TDM ou TEP), puis biopsie ganglionnaire, avec échantillon frais en microbiologie et en histologie (un lymphome et une tuberculose donnent le même tableau).",
 "Les symptômes B ne qualifient plus le stade que dans le lymphome de Hodgkin (Lugano 2014).",
 B(11,10))

q("D","DX.11 · neutropénie fébrile","management","urgences",
 "Une femme de 58 ans sous chimiothérapie pour un cancer du sein est fatiguée et a 38,6 °C. Aucun foyer à l'examen. FC 108/min.",
 "Quelle est la conduite la plus appropriée ?",
 [("Hémocultures puis antibiotiques IV",""),
  ("Attendre la NFS pour décider","Les antibiotiques ne doivent pas attendre les résultats."),
  ("Antipyrétique et contrôle le lendemain","La neutropénie fébrile tue en quelques heures."),
  ("Antibiotique oral et retour à domicile","Hospitalisation et voie IV."),
  ("Rechercher d'abord un foyer par imagerie","Un neutropénique peut n'avoir aucun signe localisé.")],
 "Fièvre sous chimiothérapie = neutropénie fébrile jusqu'à preuve du contraire (DX.11, E4) : constantes, voie veineuse, hémocultures, NFS, CRP, lactate, créatinine, puis antibiothérapie IV à large spectre sans délai selon le protocole local ; hospitalisation, isolement, oncologue.",
 "Œdème du visage, dyspnée et veines du cou dilatées : obstruction de la veine cave supérieure.",
 B(11,11), niv="specialiste", spe="Oncologie")

q("D","DX.11 · lyse tumorale","management","hôpital",
 "Un homme de 45 ans avec lymphome à forte charge tumorale va débuter une chimiothérapie. Il a un déficit connu en G6PD.",
 "Quelle mesure est contre-indiquée chez lui ?",
 [("La rasburicase",""),
  ("L'hydratation abondante","Mesure de base de la prévention."),
  ("La surveillance du potassium et du phosphate","Surveillance indispensable pendant les premiers jours."),
  ("L'avis néphrologique si la diurèse chute","Conduite recommandée."),
  ("L'allopurinol à risque intermédiaire","Utilisé pour prévenir la néphropathie urique.")],
 "Prévention de la lyse tumorale (DX.11) : repérer le risque, perfuser abondamment, pas d'alcalinisation, rasburicase avant la chimiothérapie (0,20 mg/kg/j en 30 minutes, jusqu'à 7 jours), surveillance de K+, phosphate, calcium, acide urique et créatinine. La rasburicase est contre-indiquée en cas de déficit en G6PD.",
 "Allopurinol : toute éruption impose l'arrêt immédiat.",
 B(11,14), pol="negative", niv="specialiste", spe="Hématologie")

q("D","DX.11 · fatigue liée au cancer","management","policlinique",
 "Une femme de 55 ans en cours de radiothérapie pour un cancer du sein se plaint d'une fatigue intense. Hb, TSH et glycémie normales ; pas de dépression.",
 "Quelle mesure a le meilleur niveau de preuve contre sa fatigue ?",
 [("Exercice et soutien psychologique",""),
  ("Méthylphénidate","Il n'améliore pas plus la fatigue que le placebo."),
  ("Corticoïde au long cours à faible dose","Preuve de très faible certitude."),
  ("Repos strict au lit","Il aggrave le déconditionnement et la fonction."),
  ("Fer IV systématique","Sans carence prouvée, aucune indication.")],
 "La fatigue liée au cancer touche jusqu'à 52 % des patients. Exercice, interventions psychologiques et leur association l'améliorent pendant et après le traitement, mieux que les médicaments ; on corrige d'abord les facteurs réversibles (anémie, hypothyroïdie, dépression, insomnie, douleur) (DX.11).",
 "Méta-analyse en réseau 2025 : bénéfice de l'exercice de résistance et du yoga.",
 B(11,14), niv="approfondissement")

# ═════════════ BLOC P · PIÈGES & ALARMES
q("P","DX.3 · SAOS et zolpidem","management","cabinet",
 "Un homme de 49 ans ronfle fort, se réveille fatigué et somnole en réunion. Il demande « un somnifère comme celui de sa femme », du zolpidem.",
 "Quelle est la conduite la plus appropriée ?",
 [("Polysomnographie, sans hypnotique",""),
  ("Zolpidem 10 mg pendant 4 semaines au plus","Le SAOS suspecté est une contre-indication."),
  ("Témazépam 10 mg","Également contre-indiqué en cas d'apnées."),
  ("Mélatonine Circadin® 2 mg","Indication AIPS dès 55 ans, et elle ne traite pas un SAOS."),
  ("TCC-I seule sans autre examen","Il faut d'abord exclure les apnées.")],
 "Ronflement, réveil non reposé et somnolence évoquent un SAOS (DX.3) : zolpidem et témazépam sont contre-indiqués ; on demande une polysomnographie, puis PPC si le SAOS est confirmé.",
 "Prescrire un hypnotique avant d'exclure un SAOS est le piège classique.",
 B(3,14))

q("P","DX.7 · exercice gradué","management","cabinet",
 "Une femme de 36 ans a un syndrome de fatigue chronique confirmé. Son employeur suggère un programme de « remise en forme » avec augmentation fixe de l'effort chaque semaine.",
 "Quelle recommandation est la plus appropriée ?",
 [("Gestion de l'énergie (pacing)",""),
  ("Exercice gradué à paliers fixes","NICE le déconseille : il peut aggraver l'état."),
  ("Salle de sport trois fois par semaine","À éviter ; l'activité physique est individuelle et supervisée, si la patiente le souhaite."),
  ("TCC à visée curative","La TCC aide à gérer les symptômes, jamais curative."),
  ("Lightning Process","Déconseillé par NICE.")],
 "Dans le syndrome de fatigue chronique (DX.7), le pacing est le pilier : rester sous sa limite, alterner activité et repos, fractionner les tâches. NICE ne recommande pas l'exercice gradué à augmentation fixe ; le déconditionnement n'est pas retenu comme cause.",
 "Crash : réduire l'activité sous la limite et ne reprendre qu'après stabilisation.",
 B(7,13))

q("P","DX.7 · symptôme nouveau","assessment_diagnosis","cabinet",
 "Un homme de 44 ans a un syndrome de fatigue chronique depuis 2 ans. Il signale depuis 1 mois une faiblesse de la jambe droite et une vision floue d'un œil.",
 "Quelle est la conduite la plus appropriée ?",
 [("Examen neurologique et IRM cérébrale",""),
  ("Attribuer ces signes au syndrome de fatigue chronique","Un nouveau signe n'est jamais attribué d'emblée au SFC."),
  ("Renforcer le pacing et revoir dans 1 an","La revue annuelle ne vaut pas pour un symptôme nouveau."),
  ("Physiothérapie de renforcement","Un déficit focal impose une imagerie."),
  ("Augmenter l'antalgique","Ne répond pas à la question diagnostique.")],
 "Déficit neurologique focal ou trouble visuel : drapeau rouge (DX.7) ; ils évoquent une sclérose en plaques, une tumeur ou une cause vasculaire. Examen neurologique, IRM, avis neurologique. Un symptôme nouveau déclenche une enquête, jamais une attribution automatique au SFC.",
 "La fatigue de la sclérose en plaques ressemble à celle du SFC, mais sans PEM marqué.",
 B(7,4))

q("P","DX.6 · inflammation","assessment_diagnosis","hôpital",
 "Un homme de 63 ans hospitalisé pour une polyarthrite active est fatigué. Hb 108 g/L, CRP 64 mg/L, ferritine 180 µg/L, TSAT 12 %.",
 "Quelle conclusion est la plus juste ?",
 [("Un déficit en fer reste possible",""),
  ("La ferritine normale exclut un déficit en fer","L'inflammation relève la ferritine."),
  ("Il faut une gastroscopie urgente","Aucun signe de saignement aigu."),
  ("Il s'agit d'une carence en B12","Rien n'évoque une macrocytose."),
  ("L'anémie est hémolytique","Ni ictère ni réticulocytes élevés.")],
 "L'inflammation augmente la ferritine : une ferritine normale ou haute n'exclut pas un déficit en fer (DX.6). On s'aide de la TSAT (basse ici) ou du sTfR ; en inflammation hospitalière, index sTfR/log ferritine ≥ 1,5.",
 "Maladie de Crohn : ni ferritine ni TSAT ne sont fiables, utiliser le sTfR.",
 B(6,14))

q("P","DX.4 · HbA1c et fer","assessment_diagnosis","cabinet",
 "Une femme de 44 ans, asymptomatique, a une HbA1c à 6,6 % et une carence en fer marquée (ferritine 6 µg/L). Glycémie à jeun 5,4 mmol/L.",
 "Quelle conclusion est la plus appropriée ?",
 [("Se fier aux glycémies",""),
  ("Le diabète est établi par l'HbA1c","Une seule valeur sans symptôme ne suffit pas, et la carence en fer élève l'HbA1c."),
  ("Débuter la metformine","Aucun diagnostic posé."),
  ("Prédiabète certain","La glycémie à jeun est normale."),
  ("HGPO inutile dans ce cas","Elle est au contraire une option pour trancher.")],
 "La carence en fer élève l'HbA1c ; anémie, hémoglobinopathie, insuffisance rénale ou grossesse la faussent (DX.4). Sans symptôme, il faut deux tests anormaux ; ici la glycémie à jeun est normale.",
 "Traitez la carence et cherchez sa cause ; recontrôlez ensuite.",
 B(4,8), niv="approfondissement")

q("P","DX.8 · hypoglycémie","assessment_diagnosis","cabinet",
 "Une femme de 58 ans, diabétique sous insuline, décrit des « crises d'angoisse » en fin de matinée : sueurs, tremblements, palpitations. Elle saute souvent le petit-déjeuner.",
 "Quel examen faut-il réaliser en premier ?",
 [("Glycémie pendant un épisode",""),
  ("GAD-2 et entretien psychiatrique","Le diagnostic d'anxiété est d'exclusion."),
  ("Holter de 24 h en ambulatoire","L'horaire à jeun sous insuline oriente vers l'hypoglycémie."),
  ("TSH seule","Utile, mais le contexte impose d'abord la glycémie."),
  ("Essai de sertraline","Traiter sans diagnostic expose au piège.")],
 "Sueurs, tremblements, palpitations à jeun ou après l'insuline : hypoglycémie jusqu'à preuve du contraire ; la glycémie pendant l'épisode tranche. Étiqueter « panique » un épisode hypoglycémique est un piège classique (DX.8).",
 "Un épisode isolé peut être manqué : apprenez à la patiente à mesurer pendant la crise.",
 B(8,4))

q("P","DX.1 · bilan normal ne clôt pas","assessment_diagnosis","cabinet",
 "Un homme de 69 ans a un épisode dépressif depuis 2 mois, de début récent. Il a perdu 7 kg et transpire la nuit. Le bilan de base est normal.",
 "Quelle est la conduite la plus appropriée ?",
 [("Examen complet et bilan somatique ciblé",""),
  ("Débuter un ISRS et revoir à 2 semaines","Perte de poids et sueurs nocturnes orientent vers une cause organique (drapeau R4)."),
  ("Psychothérapie seule","Elle ne répond pas aux drapeaux rouges."),
  ("Rassurer : le bilan est normal","Un bilan de base normal n'exclut pas un cancer."),
  ("Hospitalisation psychiatrique","Aucun risque suicidaire ni psychose décrits.")],
 "Perte de poids involontaire, fièvre, sueurs nocturnes ou adénopathies orientent vers un cancer, une infection ou une maladie systémique, non vers la dépression (DX.1, DX.11) : examen complet et bilan ciblé. Début après 60 ans : la dépression tardive peut cacher une maladie organique.",
 "Un cancer peut aussi causer une dépression réactive.",
 B(1,4))

q("P","DX.5 · fatigue récente après 50 ans","assessment_diagnosis","cabinet",
 "Une femme de 63 ans consulte pour une fatigue d'installation récente, progressive depuis 5 semaines. Elle a des selles noires depuis 10 jours.",
 "Quelle est la prochaine étape la plus appropriée ?",
 [("NFS, ferritine et avis gastro-entérologique",""),
  ("PHQ-9 et réévaluation à 4 à 6 semaines","Le méléna est un drapeau rouge à explorer sans attendre."),
  ("Fer oral et contrôle dans 3 mois","On ne traite pas sans chercher la source."),
  ("TSH et glycémie seules","Elles n'explorent pas le saignement."),
  ("Polysomnographie","Aucun trouble du sommeil décrit.")],
 "Saignement digestif ou changement du transit après 50 ans, et fatigue récente progressive après 50 ans sont des drapeaux rouges de maladie somatique grave (DX.5) : NFS, ferritine, recherche de la source et avis gastro-entérologique.",
 "Instabilité ou douleur thoracique avec méléna : 144 et hospitalisation.",
 B(5,4))

q("P","DX.2 · artère normale","assessment_diagnosis","cabinet",
 "Une femme de 74 ans a une céphalée temporale nouvelle, une claudication de la mâchoire et une CRP à 55 mg/L. Le pouls temporal est bien perçu et l'artère est souple.",
 "Quelle conclusion est la plus appropriée ?",
 [("L'artère normale n'exclut pas l'artérite",""),
  ("L'artérite est exclue par l'artère souple","L'imagerie ou la biopsie tranche."),
  ("Il s'agit d'une polymyalgie isolée","Céphalée et claudication orientent vers l'artérite."),
  ("Attendre la biopsie avant tout corticoïde","On traite sans attendre."),
  ("La CRP élevée suffit à poser le diagnostic","L'imagerie ou la biopsie confirment.")],
 "Une artère temporale normale à la palpation n'exclut pas l'artérite à cellules géantes : l'imagerie ou la biopsie tranche, et le glucocorticoïde ne doit pas attendre (DX.2).",
 "Risque : cécité par occlusion artérielle.",
 B(2,14))

q("P","DX.10 · fièvre persistante","assessment_diagnosis","cabinet",
 "Un homme de 38 ans est fatigué depuis 5 semaines après une « grippe ». Il garde une fièvre à 38,3 °C le soir et des frissons. Pas de toux.",
 "Quelle est la conduite la plus appropriée ?",
 [("Bilan infectieux avec hémocultures",""),
  ("Rassurer : séquelle virale banale","Une fièvre persistante évoque une infection non guérie ou une complication."),
  ("Gestion de l'énergie seule","Le drapeau rouge doit être exploré d'abord."),
  ("Soupçonner un SFC à 6 semaines","On exclut d'abord une infection active."),
  ("Ibuprofène en automédication prolongée","Au plus 3 jours en automédication ; il masque la fièvre.")],
 "Après une virose, une fièvre qui persiste, des frissons ou un foyer évoquent une infection non guérie ou une complication (endocardite, sepsis) : bilan infectieux, hospitalisation si instabilité (DX.10).",
 "Prendre la fièvre pour une séquelle virale est le piège.",
 B(10,4))

q("P","DX.11 · marqueur normal","assessment_diagnosis","cabinet",
 "Un homme de 61 ans, fatigué, a perdu 8 kg en 3 mois et a du sang dans les selles. Son CEA est normal. Il est soulagé.",
 "Quelle conduite est la plus appropriée ?",
 [("Coloscopie malgré le marqueur normal",""),
  ("Rassurer : le CEA normal exclut un cancer","Les marqueurs servent au suivi, non au dépistage."),
  ("Répéter le CEA dans 3 mois","Le délai fait perdre une chance."),
  ("Fer oral et contrôle","On ne traite pas sans chercher la source."),
  ("PHQ-9 d'abord","Les drapeaux rouges imposent l'exploration.")],
 "Un marqueur tumoral normal n'exclut pas un cancer ; il sert au suivi d'un cancer connu (DX.11). Perte de poids et sang dans les selles imposent l'endoscopie, puis biopsie.",
 "Dépistage organisé du côlon en Suisse : 50 à 69 ans, coloscopie tous les 10 ans ou test immunologique tous les 2 ans.",
 B(11,14))

q("P","DX.3 · comportement complexe","management","cabinet",
 "Une femme de 61 ans sous hypnotique depuis 3 semaines a été retrouvée par son mari en train de cuisiner la nuit, sans aucun souvenir le matin. Elle souhaite continuer, car « il aide à dormir ».",
 "Quelle est la conduite la plus appropriée ?",
 [("Arrêt immédiat de l'hypnotique",""),
  ("Poursuivre à la même dose","Un comportement complexe du sommeil impose l'arrêt."),
  ("Réduire la dose de moitié","L'arrêt doit être immédiat."),
  ("Ajouter un second hypnotique","Aggrave le risque."),
  ("Remplacer par un antagoniste de l'orexine","Il peut aussi provoquer des comportements complexes.")],
 "Somnambulisme, conduite ou repas au cours du sommeil sans souvenir : comportement complexe du sommeil, possible avec les hypnotiques, y compris les antagonistes de l'orexine (DX.3). Arrêt immédiat de l'hypnotique et avis neurologique.",
 "Le piège : poursuivre le médicament « parce qu'il aide à dormir ».",
 B(3,4), niv="approfondissement")

q("P","DX.6 · femme ménopausée","assessment_diagnosis","cabinet",
 "Une femme de 64 ans, ménopausée depuis 12 ans, est fatiguée. Hb 106 g/L, VGM 76 fL, ferritine 9 µg/L. Elle attribue sa fatigue à « des règles abondantes autrefois ».",
 "Quelle est la prochaine étape la plus appropriée ?",
 [("Rechercher une perte de sang digestive",""),
  ("Attribuer la carence aux règles passées","Les règles ne l'expliquent pas après la ménopause."),
  ("Fer IV d'emblée sans autre bilan","On cherche la cause avant de traiter."),
  ("Dosage B12 et folates","Le VGM bas oriente vers le fer."),
  ("Réévaluation à 6 mois","Le délai fait manquer un cancer digestif.")],
 "Anémie chez l'homme ou la femme ménopausée sans cause évidente : la perte de sang digestive doit être cherchée (DX.6). Attribuer l'anémie aux règles chez une femme ménopausée est un piège classique.",
 "Déficit en fer fréquent chez l'âgé (26,8 % dans DO-HEALTH) : cherchez une cause digestive.",
 B(6,4))

q("P","DX.9 · amaigrissement","management","cabinet",
 "Une femme de 34 ans euthyroïdienne, IMC 27, demande de la lévothyroxine « pour maigrir et avoir plus d'énergie », comme une amie.",
 "Quelle réponse est la plus appropriée ?",
 [("Refuser la prescription",""),
  ("Prescrire 25 µg/j à l'essai","Aucune indication chez l'euthyroïdien."),
  ("Prescrire 100 µg/j avec contrôle de TSH","Abus : risque vital selon l'AIPS."),
  ("Ajouter la liothyronine pour l'énergie","Pas en routine, et sans indication ici."),
  ("Doser les anti-TPO pour décider","Ils ne posent pas d'indication de traitement.")],
 "Le traitement par lévothyroxine n'a aucune indication de perte de poids ; l'AIPS l'interdit et signale un risque vital en cas d'abus (DX.9). Un surdosage donne tachycardie, arythmie, tremblement, insomnie, perte de poids.",
 "Postménopause : un surdosage chronique expose à l'ostéoporose.",
 B(9,14), niv="approfondissement")

META = dict(
 code="G4", lot="LOT_004", version="1.0.0", seed=13, date="2026-11-01",
 titre="Fatigue, lassitude",
 titre_court="Fatigue, lassitude", n_dx=11,
 note_version="v1 : gabarit Revision (EX/AP/SPE, 💡 fermé) — 1re production G4",
 note_media="Aucune image clinique dans les HTML LOT_004 (Phase A + DX.1–11) : media = null partout, bouton 🖼 absent.",
 intro_R="Drapeau rouge d'abord (suicide, glycémie, perte de poids, saignement, instabilité). Sinon : anamnèse, examen, bilan de base limité, puis humeur et sommeil.",
 intro_D="Les 11 DX du LOT face à face : un signe, un examen qui tranche, une conduite. Les questions AP (bleu) et SPE (violet) sont mêlées aux EX : filtrez par niveau en haut.",
 intro_P="Bilan normal qui rassure à tort, ferritine en inflammation, HbA1c faussée, zolpidem et apnées, exercice gradué, marqueur tumoral, attribution prématurée.",
 verdict_label="Réflexe G4",
 footer="LOT_004 · G4 · Banque « Temps 1 » v1 · Faits issus exclusivement des leçons auditées LOT_004 (Phase A + Phase B DX.1–11) · Type A, une seule meilleure réponse (règles IML) · Aucun cliché dans les sources LOT_004 : aucune image affichée.",
 carte_html="""<div class="reflex"><b>Les 3 questions réflexes devant toute fatigue</b><ol>
<li><b>Danger maintenant ?</b> Idées suicidaires, douleur thoracique, syncope, instabilité, polyurie-polydipsie → <b>urgence, glycémie capillaire, ECG</b>.</li>
<li><b>Signe d'appel ?</b> Perte de poids, fièvre, sueurs, adénopathie, saignement, déficit neurologique → <b>bilan ciblé, imagerie, avis</b>.</li>
<li><b>Sinon :</b> anamnèse (humeur, sommeil, médicaments), examen complet, <b>bilan de base limité</b> (NFS, CRP, glycémie, TSH, ferritine, créatinine, ALAT) ; revoir à 4–6 semaines.</li></ol></div>
<div class="map" style="margin-top:10px">
<div class="ax"><h3>🧠 Psychique · sommeil</h3><ul>
<li>PHQ-2 ≥ 3 → PHQ-9 ; ≥ 10 dépiste, ≥ 16 forme plus sévère (DX.1)</li>
<li>TAG : ≥ 6 mois, ≥ 3/6 symptômes ; panique : attaques récurrentes + 1 mois (DX.8)</li>
<li>Epworth, STOP-Bang ≥ 3 → polysomnographie ; TCC-I d'abord (DX.3)</li></ul></div>
<div class="ax"><h3>🩸 Biologie de base</h3><ul>
<li>Hb &lt; 120 (F) / &lt; 130 (H) → VGM, ferritine (DX.6) ; ferritine &lt; 50 + Hb normale chez la femme réglée → fer oral</li>
<li>HbA1c ≥ 6,5 % ou GAJ ≥ 7,0 → 2e test (DX.4)</li>
<li>TSH 4–10 → répéter 2–3 mois ; &gt; 10 → traiter avant 65–70 ans (DX.9)</li></ul></div>
<div class="ax"><h3>⏳ Durée · effort</h3><ul>
<li>Après infection : &lt; 6 sem = convalescence (DX.10)</li>
<li>≥ 6 sem + PEM, sommeil non réparateur, cognition → soupçon SFC ; 3 mois → diagnostic (DX.7)</li>
<li>Pacing ; jamais d'exercice gradué fixe</li></ul></div>
<div class="ax"><h3>🦴 Locomoteur · organe</h3><ul>
<li>Ceintures &gt; 50 ans, raideur &gt; 45 min → CRP, VS (DX.2)</li>
<li>Céphalée temporale, trouble visuel → corticoïde immédiat</li>
<li>Signe d'organe → bilan de l'organe (DX.5) ; histologie pour le cancer (DX.11)</li></ul></div>
<div class="ax rf"><h3>🚩 Ordre d'exclusion</h3><ol>
<li>E1 Dépression avec risque suicidaire (DX.1)</li><li>E2 Diabète décompensé (DX.4)</li>
<li>E3 Maladie somatique grave (DX.5)</li><li>E4 Anémie sévère (DX.6)</li>
<li>E5 Néoplasie maligne (DX.11)</li>
<li>Puis : sommeil, musculo-squelettique, anxiété, hypothyroïdie, post-infectieux, SFC</li></ol>
<p class="red" style="margin:6px 0 0">Bilan de base normal ≠ cancer exclu. Méta-analyse : dépression 18,5 %, maladie grave 4,3 %, anémie 2,8 %, cancer 0,6 %.</p></div>
</div>""",
 algo_html=f"""<table class="algo"><tr><th>Si…</th><th>Alors…</th></tr>
<tr class="e"><td>Instabilité, douleur thoracique, syncope ou idées suicidaires</td><td>Urgence : signes vitaux, ECG ; ne pas laisser seul, avis psychiatrique</td></tr>
<tr class="e"><td>Glycémie capillaire très élevée ou diabète décompensé</td><td>DX.4 : urgence, cétones, puis HbA1c</td></tr>
<tr class="e"><td>Perte de poids, fièvre, sueurs nocturnes, adénopathie</td><td>DX.11, DX.5 : imagerie ciblée et avis spécialisé</td></tr>
<tr class="e"><td>Saignement ou pâleur</td><td>DX.6 : NFS, ferritine, source du saignement</td></tr>
<tr><td>PHQ-2 ≥ 3</td><td>DX.1, DX.8 : PHQ-9, entretien, risque suicidaire</td></tr>
<tr><td>Somnolence, ronflement, sommeil court</td><td>DX.3 : Epworth, polygraphie</td></tr>
<tr><td>Douleur diffuse ou articulaire</td><td>DX.2 : examen locomoteur, CRP ou VS</td></tr>
<tr><td>TSH élevée</td><td>DX.9 : fT4, contrôle à 2–3 mois</td></tr>
<tr><td>Infection récente</td><td>DX.10 : cadre post-infectieux, OMS à 3 mois</td></tr>
<tr><td>Malaise post-effort après 3 mois</td><td>DX.7 : SFC, centre spécialisé</td></tr>
<tr><td>Bilan normal, fatigue stable</td><td>Hygiène du sommeil, TCC, revue à 4–6 semaines</td></tr>
</table>
<p class="intro">Source : <a href="{R}LOT_004_Phase_A_V0.html#algo">Phase A · Algorithme discriminant</a> et <a href="{R}LOT_004_Phase_A_V0.html#ssp-p10">§10 Arbre décisionnel</a>.</p>""",
)
