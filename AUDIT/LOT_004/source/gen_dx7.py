# -*- coding: utf-8 -*-
"""DX.7 — Maladie rénale chronique. LOT 4, V5 → V7 AUDITÉ."""
from lot4_commun import *
POINT = mkPOINT('dx7')
M = META('dx7', 'DX.7', 'Maladie rénale chronique', 'Maladie rénale chronique (fatigue de l’insuffisance rénale)',
         'LOT_004_DX7_Maladie_renale_chronique_AUDITÉ.html',
         'Corrections majeures : seuils KDIGO restitués (DFGe < 60 mL/min/1,73 m², rapport albumine/créatinine ≥ 3 mg/mmol) ; prévalence suisse SKIPOGH 10,4 % au lieu de « 800 000 » non sourcé ; cible d’hémoglobine sous érythropoïétine ≤ 115 g/L ; le produit de contraste iodé n’est pas une contre-indication absolue ; xénotransplantation retirée faute de source.')
DFG = T('débit de filtration glomérulaire estimé (DFGe)', 'Le DFGe est le volume de sang que les reins filtrent par minute, calculé à partir de la créatinine ; il baisse quand les reins perdent leurs filtres (néphrons).')
RAC = T('rapport albumine/créatinine urinaire (RAC)', 'Le RAC mesure l’albumine qui fuit dans l’urine, rapportée à la créatinine urinaire ; une fuite traduit une lésion des filtres du rein.')
PTS = []
def ADD(*a): PTS.append(POINT(*a))
ADD(1, 'Définition et sémantique',
 P('La maladie rénale chronique (MRC) est une anomalie du rein qui dure plus de 3 mois et a des conséquences sur la santé. '
   'Elle se définit par un débit de filtration glomérulaire estimé (DFGe) < 60 mL/min/1,73 m² ou par un marqueur de lésion, surtout un rapport albumine/créatinine urinaire (RAC) ≥ 3 mg/mmol.', 27) +
 F('Terminologie (KDIGO 2024)',
   TAB(['Terme', 'Définition exacte', 'À ne pas confondre avec'], [
    ['Maladie rénale chronique', 'Anomalie > 3 mois : DFGe < 60 ou marqueur de lésion', 'Insuffisance rénale aiguë'],
    ['Stade G (G1–G5)', 'Classe selon le DFGe', 'Gravité des symptômes'],
    ['Stade A (A1–A3)', 'Classe selon le RAC', 'Protéinurie des 24 h seule'],
    ['Insuffisance rénale terminale', 'DFGe < 15 ou dialyse', 'MRC débutante'],
    ['Urémie', 'Syndrome toxique de l’insuffisance rénale avancée', 'Urée élevée seule'],
   ]) + P('La classification combine la cause, le stade G et le stade A (classement CGA).', 27)))
ADD(2, 'Épidémiologie (Suisse, puis Europe)',
 P('En Suisse, l’étude SKIPOGH estime la prévalence de la MRC à 10,4 % des adultes, surtout aux stades précoces. '
   'Le chiffre de « 800 000 personnes » de l’original n’est pas sourcé. Dans le monde, la MRC touche environ 10 % des adultes (KDIGO).', 28, 27) +
 F('Chiffres, terrain et histoire naturelle',
   TAB(['Donnée', 'Valeur', 'Portée'], [
    ['Prévalence suisse', '10,4 %', 'Étude SKIPOGH'],
    ['Prévalence mondiale', '≈ 10 %', 'KDIGO 2024'],
    ['Causes principales', 'Diabète de type 2, hypertension', 'Pays industrialisés'],
    ['MRC chez les personnes âgées', 'Prévalence croissante avec l’âge', 'Revue de Bowling'],
   ]) + P('Le terrain réunit le diabète, l’hypertension, l’âge, l’obésité, les maladies cardiovasculaires et les antécédents familiaux. '
          'Le pronostic dépend du stade G et du stade A ; le risque cardiovasculaire dépasse souvent le risque de dialyse.', 27, 54)))
ADD(3, 'Physiopathologie',
 P('Le rein contient environ un million de filtres, les néphrons. Quand certains disparaissent, les autres filtrent plus (hyperfiltration). '
   'Cet effort, entretenu par l’angiotensine II sur l’artériole de sortie du glomérule, finit par les cicatriser (glomérulosclérose).', 27) +
 F('Chaîne logique : de l’anatomie au traitement',
   TAB(['Étape', 'Ce qu’il faut comprendre'], [
    ['Anatomie', 'Le néphron comprend le glomérule (filtre) et le tubule (réabsorption).'],
    ['Physiologie', 'Le rein élimine les déchets, l’acide et le potassium, produit l’érythropoïétine et active la vitamine D.'],
    ['Physiopathologie', 'La perte de néphrons réduit ces fonctions ; l’hyperfiltration accélère la perte.'],
    ['Clinique', 'D’où la fatigue (anémie, toxines urémiques, acidose), puis les nausées et le prurit.'],
    ['Examens', 'DFGe et RAC mesurent la fonction et la lésion.'],
    ['Traitement', 'Bloquer le SRAA et le cotransporteur SGLT2 réduit l’hyperfiltration.'],
   ]), 27) +
 F('Pourquoi la fatigue : quatre mécanismes',
   TAB(['Mécanisme', 'Lésion ou cause', 'Exploration', 'Cible thérapeutique'], [
    ['Toxines urémiques', 'Accumulation d’urée et d’autres déchets', 'Urée, DFGe', 'Dialyse si stade terminal'],
    ['Anémie', 'Manque d’érythropoïétine produite par les cellules interstitielles du rein', 'Hémogramme, ferritine', 'Fer, puis agent stimulant l’érythropoïèse'],
    ['Acidose métabolique', 'Le rein élimine moins d’acide', 'Bicarbonates', 'Bicarbonate de sodium'],
    ['Trouble minéral et osseux', 'Moins de calcitriol (perte de la 1α-hydroxylase), phosphate retenu', 'Calcium, phosphate, PTH, vitamine D', 'Régime, chélateurs, vitamine D'],
   ]) + P('Cette chaîne explique pourquoi la fatigue apparaît surtout aux stades G3b–G5.', 27, 64)) +
 F('Calculs utiles', P('Le DFGe se calcule par l’équation CKD-EPI 2021, sans facteur ethnique, à partir de la créatinine et parfois de la cystatine C.', 27) +
   P('Calcium corrigé (mmol/L) = calcium mesuré + 0,02 × (40 − albumine en g/L). Exemple : 2,02 + 0,02 × (40 − 30) = 2,22 mmol/L.', 27) +
   P('Cette correction est peu fiable dans la MRC ; on préfère le calcium ionisé.', 27)))
ADD(4, 'Raisonnement clinique et diagnostic différentiel',
 P('Devant une créatinine élevée chez un patient fatigué, le médecin cherche d’abord une urgence : hyperkaliémie, œdème pulmonaire, acidose. '
   'Puis il distingue une maladie chronique d’une insuffisance rénale aiguë, car celle-ci peut être réversible.', 27) +
 DIFF('mrc') + DIFF_FAT() +
 F('MRC ou insuffisance rénale aiguë',
   TAB(['Élément', 'Oriente vers la MRC', 'Oriente vers l’atteinte aiguë'], [
    ['Créatinine antérieure', 'Déjà élevée depuis > 3 mois', 'Normale récemment'],
    ['Taille des reins à l’échographie', 'Petits (souvent < 9–10 cm), cortex aminci', 'Normale ; dilatation si obstacle'],
    ['Anémie, hyperparathyroïdie', 'Présentes', 'Absentes'],
    ['Causes à chercher', 'Diabète, hypertension, polykystose', 'Obstacle, médicament, hypovolémie, glomérulonéphrite'],
   ]) + P('Le diabète, la polykystose et l’amylose peuvent garder des reins de taille normale ou grande.', 27)))
ADD(5, 'Anamnèse ciblée et drapeaux rouges',
 P('L’anamnèse cherche un diabète, une hypertension, des AINS, des inhibiteurs de la pompe à protons et des antécédents familiaux. '
   'Elle note les signes d’urémie : perte d’appétit, nausées, crampes, jambes sans repos et démangeaisons.', 27) +
 U('Drapeaux rouges (indications de dialyse en urgence, mnémonique AEIOU) : acidose sévère réfractaire, hyperkaliémie avec signes ECG, œdème pulmonaire résistant aux diurétiques, intoxication dialysable, complications urémiques (péricardite, encéphalopathie). Ils imposent une hospitalisation immédiate ou le 144.', 27) +
 F('Questions ciblées et leur raison',
   TAB(['Question', 'Pourquoi la poser'], [
    ['Avez-vous du diabète ou de l’hypertension ?', 'Causes principales.'],
    ['Prenez-vous des anti-inflammatoires ?', 'Néphrotoxiques.'],
    ['Urinez-vous moins, ou la nuit ?', 'Oligurie, perte du pouvoir de concentration.'],
    ['Vos urines sont-elles mousseuses ou rouges ?', 'Protéinurie, hématurie glomérulaire.'],
    ['Un parent a-t-il une maladie des reins ?', 'Polykystose, néphropathie héréditaire.'],
    ['Avez-vous des démangeaisons ou des nausées ?', 'Urémie avancée.'],
   ]), 27))
ADD(6, 'Examen clinique',
 P('L’examen mesure la pression artérielle, le poids et cherche des œdèmes. Il note la pâleur, le teint terreux et les lésions de grattage.', 27) +
 P('Valeurs normales : pression < 140/90 mmHg au cabinet. Il cherche aussi un globe vésical, un frottement péricardique et un souffle abdominal.', 27) +
 F('Signes, technique et valeur',
   TAB(['Signe', 'Technique', 'Ce qu’il signifie'], [
    ['Pression artérielle élevée', 'Mesure assise après 5 min', 'Cause et conséquence'],
    ['Œdèmes', 'Pression 5 s sur la cheville', 'Rétention de sel'],
    ['Teint terreux, pâleur', 'Inspection', 'Anémie, rétention de pigments'],
    ['Globe vésical', 'Palpation et percussion sus-pubienne', 'Obstacle'],
    ['Frottement péricardique', 'Auscultation penché en avant', 'Urémie grave'],
    ['Astérixis', 'Bras tendus, poignets en extension', 'Encéphalopathie urémique'],
   ]), 27))
ADD(7, 'Syndromes et signes cliniques',
 F('Signes fonctionnels (symptômes rapportés)', UL(['Fatigue', 'Perte d’appétit, nausées', 'Démangeaisons', 'Crampes, jambes sans repos', 'Nycturie']), 27) +
 F('Signes physiques (constatés à l’examen)', UL(['Hypertension', 'Œdèmes', 'Pâleur', 'Astérixis au stade terminal', 'Frottement péricardique au stade terminal']), 27) +
 P('Le syndrome urémique réunit fatigue profonde, nausées, haleine d’urine, neuropathie et saignements : il traduit l’accumulation des toxines. '
   'Le trouble minéral et osseux réunit phosphate élevé, calcium bas, vitamine D active basse et PTH élevée : il fragilise l’os et calcifie les vaisseaux.', 27) +
 F('Syndrome urémique', TAB(['Signe', 'Mécanisme', 'Valeur'], [
    ['Nausées, anorexie', 'Toxines urémiques', 'Stade G5'],
    ['Saignements', 'Plaquettes moins efficaces', 'Gravité'],
    ['Astérixis', 'Encéphalopathie', 'Dialyse urgente'],
   ]), 27) +
 F('Trouble minéral et osseux', TAB(['Signe', 'Mécanisme', 'Valeur'], [
    ['Phosphate > 1,5 mmol/L', 'Moins d’élimination', 'Calcifications'],
    ['PTH élevée', 'Hyperparathyroïdie secondaire', 'Douleurs osseuses'],
    ['Vitamine D active basse', 'Moins de 1α-hydroxylase', 'Calcium bas'],
   ]), 27))
ADD(8, 'Critères diagnostiques',
 P('Le diagnostic exige une anomalie confirmée sur plus de 3 mois. Une seule créatinine élevée ne suffit pas.', 27) +
 F('Critères (KDIGO 2024)',
   TAB(['Critère', 'Seuil'], [
    ['DFGe', '< 60 mL/min/1,73 m² > 3 mois'],
    ['RAC', '≥ 3 mg/mmol (≥ 30 mg/g) > 3 mois'],
    ['Autres marqueurs', 'Sédiment anormal, anomalie tubulaire, histologique ou d’imagerie, greffe'],
    ['Stades G', 'G1 ≥ 90 ; G2 60–89 ; G3a 45–59 ; G3b 30–44 ; G4 15–29 ; G5 < 15'],
    ['Stades A', 'A1 < 3 ; A2 3–30 ; A3 > 30 mg/mmol'],
   ]) + P('Ces seuils sont ceux de la recommandation internationale KDIGO 2024.', 27)))
ADD(9, 'Examens complémentaires',
 H4('9.a Examen de référence') +
 P('La mesure du DFG par un traceur (iohexol) est la référence ; elle est réservée à des cas choisis. En pratique, on combine le DFGe (créatinine, avec ou sans cystatine C) et le RAC sur l’urine du matin. Le DFGe a une sensibilité correcte mais une spécificité limitée chez la personne âgée ; le RAC est plus sensible que la bandelette urinaire.', 27) +
 H4('9.b Examens de première et de deuxième intention') +
 P('En première intention, on fait créatinine, RAC, sédiment urinaire, électrolytes, hémogramme et échographie rénale. En deuxième intention, on cherche une cause rare ou une gammapathie.', 27) +
 TAB(['Intention', 'Examen', 'Pourquoi'], [
  ['1re', 'Créatinine et DFGe', 'Stade G'],
  ['1re', 'Rapport albumine/créatinine', 'Stade A'],
  ['1re', 'Sédiment urinaire (ECBU)', 'Hématurie glomérulaire'],
  ['1re', 'Ionogramme, bicarbonates', 'Potassium, acidose'],
  ['1re', 'Hémogramme, ferritine', 'Anémie, carence en fer'],
  ['1re', 'Calcium, phosphate, PTH, vitamine D', 'Trouble minéral et osseux (dès G3a)'],
  ['1re', 'Échographie rénale', 'Taille, obstacle, kystes'],
  ['1re', 'Cystatine C', 'Muscle faible : la créatinine surestime le DFG'],
  ['2e', 'Électrophorèse des protéines, chaînes légères libres', 'Myélome'],
  ['2e', 'Biopsie rénale', 'Glomérulopathie suspectée'],
 ]) +
 H4('9.c Prescription et formules') +
 P('Indication : diabète, hypertension, maladie cardiovasculaire, antécédent familial, fatigue inexpliquée. Moment : RAC sur la première urine du matin. '
   'Préparation : pas d’effort intense ni d’infection urinaire la veille, car ils augmentent l’albumine urinaire.', 27) +
 TAB(['Grandeur', 'Formule', 'Repère'], [['RAC', 'Albumine urinaire (mg/L) / créatinine urinaire (mmol/L)', '< 3 mg/mmol normal'], ['Calcium corrigé', 'Ca + 0,02 × (40 − albumine)', '2,15–2,55 mmol/L']]) +
 H4('9.d Interprétation : positif, négatif, limite, discordant') +
 TAB(['Situation', 'Interprétation', 'Conduite'], [
  ['Positif : DFGe < 60 sur deux mesures à 3 mois', 'MRC', 'Stadifier, chercher la cause'],
  ['Négatif : DFGe ≥ 60 et RAC < 3', 'Pas de MRC', 'Recontrôle selon le risque'],
  ['Limite : DFGe 55–60 chez une personne âgée', 'MRC G3a possible', 'Cystatine C, RAC'],
  ['Discordant : créatinine normale chez un patient très maigre', 'DFG surestimé', 'Cystatine C'],
 ]) +
 H4('9.e Alternatives') +
 P('Grossesse : créatinine plus basse qu’hors grossesse ; avis néphrologique. Enfant : formule pédiatrique. '
   'DFGe < 30 : le produit de contraste iodé n’est pas contre-indiqué, mais il impose hydratation et pesée du bénéfice ; on évite les gadolinium à risque élevé.', 27))
ADD(10, 'Arbre décisionnel',
 P('Si le DFGe baisse vite, alors on cherche une atteinte aiguë. Sinon, on stadifie et on protège le rein.', 27) +
 F('Arbre décisionnel : fonction rénale diminuée chez un patient fatigué',
   OL(['Hyperkaliémie, acidose, œdème pulmonaire : urgence.',
       'Comparer aux valeurs antérieures ; refaire à 3 mois si nouveau.',
       'Échographie et sédiment : obstacle, glomérulopathie.',
       'Stadifier G et A.',
       'Bloqueur du SRAA, gliflozine, contrôle de la pression.',
       'Adresser au néphrologue si DFGe < 30, RAC > 30 mg/mmol, baisse rapide ou hématurie glomérulaire.',
       'Au stade G4, préparer la dialyse ou la greffe et protéger les veines du bras.']), 27))
ADD(11, 'Prise en charge',
 H4('11.A Buts : d’abord l’urgence (hyperkaliémie, acidose), car elle peut tuer en quelques heures') +
 P('Le traitement ralentit la perte de fonction, réduit le risque cardiovasculaire, corrige les complications et prépare la suppléance.', 27) +
 TAB(['But', 'Cible chiffrée'], [['Pression systolique', '< 120 mmHg si tolérée (KDIGO 2021)'], ['RAC', 'Baisse ≥ 30 %'], ['Hémoglobine sous agent stimulant', '100–115 g/L, jamais volontairement > 130 g/L'], ['Bicarbonates', 'Traitement si < 18 mmol/L']]) +
 H4('11.B Moyens et méthodes : forme compliquée en urgence, puis forme non compliquée en ambulatoire') +
 P('La forme compliquée (potassium > 6,5 mmol/L, œdème pulmonaire, péricardite) se traite en urgence : gluconate de calcium, insuline-glucose, dialyse dans les heures qui suivent. '
   'La forme non compliquée se traite en ambulatoire, avec des mesures générales : sel < 5 g/j, protéines 0,8 g/kg/j aux stades G3–G5 et arrêt des néphrotoxiques.', 27) +
 P('La metformine se réduit à DFGe 30–44 et s’arrête sous 30.', 27) +
 FICHE([
  ['Sartan : irbésartan (Aprovel®) ; ou IEC : lisinopril (Zestril®)', 'Bloque l’angiotensine II ; baisse la pression dans le glomérule', 'Demi-vie ≈ 11–15 h (irbésartan)', '150–300 mg/j, dose maximale tolérée', 'Hyperkaliémie, hausse de créatinine', 'Grossesse, sténose bilatérale des artères rénales', 'AINS, ARM, potassium'],
  ['Gliflozine : dapagliflozine (Forxiga®)', 'Bloque le cotransporteur SGLT2 ; réduit l’hyperfiltration', 'Demi-vie ≈ 13 h', '10 mg/j ; début si DFGe ≥ 20, poursuivi jusqu’à la dialyse', 'Infection génitale, déshydratation', 'Diabète de type 1, dialyse', 'Diurétiques'],
  ['Antagoniste non stéroïdien du récepteur minéralocorticoïde : finérénone (Kerendia®)', 'Bloque l’aldostérone, effet anti-fibrose', 'Métabolisme hépatique (CYP3A4)', 'Départ 10 mg/j si DFGe 25–59, 20 mg/j si ≥ 60, quand K⁺ ≤ 4,8 ; cible 20 mg/j ; dans l’insuffisance cardiaque à fraction d’éjection ≥ 40 % (indication 2026), cible 40 mg/j si DFGe ≥ 60', 'Hyperkaliémie', 'DFGe < 25, inhibiteurs puissants du CYP3A4', 'Kétoconazole, clarithromycine'],
  ['Agent stimulant l’érythropoïèse : darbépoétine alfa (Aranesp®)', 'Remplace l’érythropoïétine', 'Sous-cutanée, demi-vie ≈ 70 h', 'Selon le poids, toutes les 1–4 semaines', 'Hypertension, thrombose, AVC si Hb trop haute', 'Hypertension non contrôlée', 'Aucune majeure'],
  ['Bicarbonate de sodium (Nephrotrans®)', 'Apporte une base', 'Absorption orale', '500 mg 2–6 capsules/j', 'Ballonnements, charge en sodium', 'Œdèmes sévères', 'Absorption de certains médicaments'],
 ], 27, 64, 65, 66, 80) +
 P('Corriger d’abord la carence en fer, puis débuter l’agent stimulant si l’hémoglobine reste < 100 g/L.', 64) +
 F('Situations particulières',
   TAB(['Situation', 'Particularité'], [
    ['Grossesse', 'IEC, sartans, gliflozines et finérénone contre-indiqués ; grossesse à haut risque'],
    ['Personne âgée', 'DFGe souvent 45–60 ; ne pas surtraiter, adapter les doses'],
    ['Enfant', 'Causes congénitales ; avis néphropédiatrique'],
    ['Insuffisance hépatique', 'Créatinine faussement basse ; cystatine C'],
    ['Insuffisance rénale avancée (DFGe < 30)', 'Adapter toutes les doses ; éviter les AINS'],
   ]), 27) +
 SOCIAL('Un arrêt de travail est souvent nécessaire au début de la dialyse ; les horaires peuvent ensuite s’adapter.',
        'La MRC n’interdit pas la conduite ; une hypoglycémie ou une encéphalopathie l’interdit temporairement.') +
 H4('11.C Surveillance et critères de sortie') +
 TAB(['Quand', 'Quoi'], [
  ['1–2 semaines après un sartan, un IEC ou la finérénone', 'Créatinine, potassium'],
  ['Selon le stade (1–4 fois par an)', 'DFGe, RAC, hémogramme, phosphate, PTH'],
  ['Hausse de créatinine > 30 %', 'Chercher une hypovolémie ou une sténose ; réduire la dose'],
  ['Au stade G4', 'Information sur dialyse, greffe et soins conservateurs ; fistule artério-veineuse'],
  ['Critères de sortie d’hospitalisation', 'Potassium et créatinine stables, volume équilibré, suivi néphrologique planifié'],
 ]) + P('Une baisse initiale du DFGe jusqu’à 30 % sous ces médicaments est attendue.', 27) +
 H4('11.D Pronostic et recherche 2026') +
 P('La MRC est le plus souvent irréversible. La greffe rénale, si possible avec donneur vivant, offre la meilleure survie au stade terminal.', 27) +
 P('Le roxadustat, un inhibiteur oral de l’enzyme qui dégrade le facteur induit par l’hypoxie, est autorisé dans l’Union européenne ; son statut en Suisse est à vérifier.', 27))
ADD(12, 'Prévention',
 P('La prévention traite le diabète et l’hypertension, et dépiste chaque année le DFGe et le RAC chez les patients à risque.', 27) +
 F('Prévention primaire, secondaire et tertiaire',
   TAB(['Niveau', 'Mesure'], [
    ['Primaire', 'Pression, glycémie, poids, tabac ; éviter les AINS au long cours'],
    ['Secondaire', 'DFGe et RAC annuels chez le diabétique et l’hypertendu'],
    ['Tertiaire', 'Sartan ou IEC, gliflozine, finérénone, vaccins (hépatite B avant dialyse)'],
   ]) + P('En Suisse, la Société suisse de néphrologie applique les recommandations KDIGO.', 27, 28)))
ADD(13, 'Points clés',
 P('La MRC se définit par un DFGe < 60 ou un RAC ≥ 3 mg/mmol pendant plus de 3 mois. '
   'La fatigue vient de l’anémie, des toxines et de l’acidose. '
   'Sartan et gliflozine protègent le rein. '
   'Une baisse initiale du DFGe jusqu’à 30 % ne justifie pas l’arrêt.', 27, 65))
ADD(14, 'Pièges d’examen',
 TAB(['Piège', 'Ce qu’il faut répondre'], [
  ['Viser une hémoglobine > 130 g/L sous érythropoïétine', 'Non : plus d’AVC et de thromboses'],
  ['Piquer les veines du bras non dominant au stade G4–G5', 'Non : elles servent à la fistule'],
  ['Arrêter un sartan pour une hausse de créatinine de 15 %', 'Non : effet attendu'],
  ['Diagnostiquer une MRC sur une seule créatinine', 'Non : confirmer à 3 mois'],
  ['Dire que l’iode est contre-indiqué de façon absolue', 'Non : il impose des précautions'],
 ]) + P('Ces pièges reprennent KDIGO.', 27, 64))
CTX = {'_prefixe': 'Dans la maladie rénale chronique',
 'creat': 'Un DFGe < 60 mL/min/1,73 m² pendant plus de 3 mois définit la MRC.',
 'albu': 'Un RAC ≥ 3 mg/mmol pendant plus de 3 mois définit aussi la MRC.',
 'uree': 'L’urée monte avec l’urémie, mais dépend aussi des protéines et de l’hydratation.',
 'iono': 'Un K⁺ > 6,5 mmol/L avec signes ECG impose une prise en charge urgente.',
 'nfs': 'L’anémie de la MRC est normocytaire, par manque d’érythropoïétine.',
 'ferritine': 'Corriger la carence en fer avant un agent stimulant l’érythropoïèse.',
 'pth': 'Une PTH élevée traduit une hyperparathyroïdie secondaire.',
 'vitd': 'Une carence en 25-OH vitamine D est fréquente et se corrige.',
 'echo': 'Des reins petits orientent vers une maladie ancienne ; une dilatation vers un obstacle.',
 'ecbu': 'Des globules rouges déformés orientent vers une glomérulopathie.',
 'epp': 'Elle cherche un pic monoclonal (myélome).',
 'flc': 'Le rapport kappa/lambda s’interprète avec une plage propre à la MRC.',
 'biopsie': 'Elle précise une glomérulopathie quand le traitement en dépend.',
 'ecg': 'Des ondes T pointues ou des QRS larges signent une hyperkaliémie grave.'}
if __name__ == '__main__':
    produire(M, PTS, SOURCES, CTX)
