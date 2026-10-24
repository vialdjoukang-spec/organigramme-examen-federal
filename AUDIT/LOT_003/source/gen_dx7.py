# -*- coding: utf-8 -*-
"""DX.7 — Hypercalcémie et hypokaliémie : résistance rénale acquise à la vasopressine. LOT 3, V5 → V7 AUDITÉ."""
from lot3_commun import *
POINT = mkPOINT('dx7')
M = META('dx7', 'DX.7', 'Hypercalcémie et hypokaliémie', 'Hypercalcémie et hypokaliémie : résistance rénale acquise à la vasopressine',
         'LOT_003_DX7_Hypercalcemie_hypokaliemie_AUDITÉ.html',
         'Corrections : « seules anomalies électrolytiques » nuancé ; « 2 % des polyuries » et « 1 % après 55 ans » retirés (non sourcés) et remplacés par Yeh 2013 ; seuil de QTc < 340 ms retiré ; PTH normale face à une hypercalcémie : ajout de l’hypercalcémie hypocalciurique familiale et du lithium ; dénosumab suggéré avant le bisphosphonate (Endocrine Society 2023) ; seuil de l’os affamé corrigé (< 2,1 mmol/L).')
PAYNE = T('calcémie corrigée', 'La calcémie corrigée estime le calcium total qu’aurait le patient avec une albumine normale de 40 g/L.')
FHH = T('FHH', 'L’hypercalcémie hypocalciurique familiale (FHH) est une maladie héréditaire bénigne du récepteur sensible au calcium (CaSR) ; elle ne s’opère pas.')
PTS = []

p1 = (P('L’hypercalcémie et l’hypokaliémie chronique sont les deux principales anomalies électrolytiques qui rendent le rein résistant à la vasopressine. '
        'Le rein ne concentre plus l’urine ; il en résulte une polyurie hypotonique, réversible quand l’anomalie est corrigée.', 48, 51) +
      F('Terminologie',
        TAB(['Terme', 'Définition exacte', 'À ne pas confondre avec'], [
         ['Hypercalcémie', 'Calcémie corrigée > 2,55 mmol/L ou calcium ionisé élevé', 'Fausse hypercalcémie par hyperalbuminémie'],
         ['Hypokaliémie', 'Kaliémie < 3,5 mmol/L', 'Fausse hypokaliémie (leucocytose majeure)'],
         ['Hyperparathyroïdie primaire', 'Sécrétion autonome de PTH par une parathyroïde', 'Hyperparathyroïdie secondaire (carence en vitamine D, insuffisance rénale)'],
         ['Hypercalcémie maligne', 'Hypercalcémie due à un cancer (PTHrP, métastases, calcitriol)', 'Hyperparathyroïdie chez un patient cancéreux'],
         ['Résistance rénale acquise à la vasopressine', 'Polyurie hypotonique malgré une vasopressine élevée', 'Déficit en vasopressine (origine centrale)'],
        ]), 48))
PTS.append(POINT(1, 'Définition et sémantique', p1))

p2 = (P('Aucune donnée suisse publiée n’a été trouvée. '
        'Dans une étude américaine, la prévalence de l’hyperparathyroïdie primaire atteint 233 / 100 000 femmes et 85 / 100 000 hommes ; elle augmente avec l’âge. '
        'Selon les revues européennes et internationales, l’hyperparathyroïdie primaire et le cancer expliquent ≈ 90 % des hypercalcémies.', 49, 48) +
      F('Chiffres, terrain et histoire naturelle',
        TAB(['Donnée', 'Valeur', 'Population'], [
         ['Prévalence de l’hyperparathyroïdie primaire', '233 (femmes) et 85 (hommes) / 100 000', 'Population américaine, 2010'],
         ['Hyperparathyroïdie primaire + cancer', '≈ 90 % des hypercalcémies', 'Patients hypercalcémiques'],
         ['Adénome unique', '≈ 85 % des hyperparathyroïdies primaires', 'Patients opérés'],
         ['Pronostic de l’hypercalcémie maligne', 'Mauvais : elle survient souvent à un stade avancé', 'Patients cancéreux'],
        ]) + P('Le terrain typique est la femme ménopausée pour l’hyperparathyroïdie, le patient hospitalisé avec un cancer avancé pour l’hypercalcémie maligne ; dans ce cas, la mortalité est élevée.', 49, 50)))
PTS.append(POINT(2, 'Épidémiologie (Suisse, puis Europe)', p2))

p3 = (P('Le calcium sanguin active le récepteur sensible au calcium (CaSR) de la branche ascendante de Henlé. '
        'Ce récepteur freine la réabsorption de sel ; le gradient de la médullaire diminue, comme sous furosémide. '
        'Dans le tube collecteur, l’hypercalcémie et l’hypokaliémie font baisser l’aquaporine 2 ; le tube devient moins perméable à l’eau.', 48, 51) +
      F('Chaîne logique : de l’anatomie au traitement',
        TAB(['Étape', 'Ce qu’il faut comprendre'], [
         ['Anatomie', 'Quatre parathyroïdes derrière la thyroïde ; néphron avec branche de Henlé et tube collecteur.'],
         ['Physiologie', 'Pourquoi la calcémie reste stable : le CaSR parathyroïdien freine la PTH quand le calcium monte.'],
         ['Physiopathologie', 'Excès de PTH, de PTHrP ou de calcitriol ; le calcium élevé bloque la concentration de l’urine.'],
         ['Clinique', 'D’où la polyurie, la soif, la déshydratation, la constipation et la confusion.'],
         ['Examens', 'On confirme la calcémie, puis la PTH sépare les causes dépendantes et indépendantes de la PTH.'],
         ['Traitement', 'On réhydrate, on bloque l’ostéoclaste, puis on traite la cause.'],
        ]), 48) +
      F('Mécanisme, exploration et cible thérapeutique',
        TAB(['Mécanisme', 'Exploration', 'Cible thérapeutique'], [
         ['Excès de PTH', 'PTH, calciurie', 'Parathyroïdectomie, cinacalcet'],
         ['Sécrétion tumorale de PTHrP', 'PTHrP', 'Dénosumab ou acide zolédronique, traitement du cancer'],
         ['Lyse osseuse (myélome, métastases)', 'Électrophorèse des protéines, chaînes légères', 'Antirésorptif, traitement du cancer'],
         ['Excès de calcitriol (granulome, lymphome)', 'Calcitriol', 'Glucocorticoïde'],
         ['Baisse de l’aquaporine 2', 'Osmolalité urinaire basse', 'Correction de la calcémie et de la kaliémie'],
        ]), 48, 85))
PTS.append(POINT(3, 'Physiopathologie', p3))

p4 = (P('Le clinicien traite d’abord l’urgence : calcémie ≥ 3,5 mmol/L, confusion, insuffisance rénale aiguë, troubles du rythme. '
        'Puis il dose la PTH intacte ; elle sépare les causes dépendantes de la PTH des causes indépendantes.', 48, 85) +
      DIFF('hpt') +
      F('Causes d’hypercalcémie (même population : patients hypercalcémiques ; probabilités en exposant rouge)',
        TAB(['Cause', 'PTH', 'Indice décisif'], [
         ['Hyperparathyroïdie primaire ou cancer (à eux deux)' + PR('≈ 90 %', 48), 'Élevée ou normale (hyperparathyroïdie) ; basse (cancer)', 'PTH, puis PTHrP'],
         ['Hypercalcémie hypocalciurique familiale (' + FHH + ')' + PR('non chiffrée', 48), 'Normale ou un peu élevée', 'Rapport de clairance calcium/créatinine < 0,01'],
         ['Excès de vitamine D, granulomatose' + PR('non chiffrée', 48), 'Basse', 'Calcidiol (intoxication) ou calcitriol (granulome)'],
         ['Médicaments : thiazide, lithium' + PR('non chiffrée', 48), 'Normale ou élevée (lithium)', 'Chronologie'],
        ]) + P('Pour l’hypokaliémie, la cause habituelle est un diurétique, des vomissements ou un hyperaldostéronisme.', 48)))
PTS.append(POINT(4, 'Raisonnement clinique et diagnostic différentiel', p4))

p5 = (P('L’anamnèse cherche les signes osseux, rénaux, digestifs et psychiques : douleurs osseuses, coliques néphrétiques, constipation, fatigue. '
        'Elle relève les médicaments : thiazide, lithium, vitamine D, calcium.', 48, 47) +
      U('Drapeaux rouges : calcémie ≥ 3,5 mmol/L, confusion ou coma, insuffisance rénale aiguë, arythmie, vomissements incoercibles. Ils imposent une hospitalisation immédiate.', 85) +
      F('Questions ciblées et leur raison',
        TAB(['Question', 'Pourquoi la poser'], [
         ['Avez-vous eu des calculs rénaux ?', 'La lithiase oriente vers l’hyperparathyroïdie.'],
         ['Avez-vous perdu du poids, toussez-vous, avez-vous une masse au sein ?', 'Cherche un cancer.'],
         ['Prenez-vous de la vitamine D, du calcium, un thiazide ou du lithium ?', 'Ces produits élèvent la calcémie.'],
         ['Un parent a-t-il une calcémie élevée ?', 'Évoque une hypercalcémie hypocalciurique familiale.'],
         ['Êtes-vous constipé, nauséeux, confus ?', 'Mesure le retentissement.'],
         ['Vomissez-vous ou prenez-vous des laxatifs ?', 'Cause d’hypokaliémie.'],
        ]), 48))
PTS.append(POINT(5, 'Anamnèse ciblée et drapeaux rouges', p5))

p6 = (P('L’examen évalue la déshydratation : à l’état normal, la muqueuse buccale est humide et la pression ne baisse pas en position debout. '
        'Il teste les réflexes ostéo-tendineux, souvent diminués, et la force musculaire. '
        'Il cherche une masse tumorale ; la palpation d’un adénome parathyroïdien a une faible sensibilité.', 48) +
      F('Signes, technique et valeur',
        TAB(['Signe', 'Technique', 'Ce qu’il signifie'], [
         ['Hypotension orthostatique', 'Pression couchée puis debout à 1 et 3 min', 'Déshydratation extracellulaire'],
         ['Muqueuses sèches, poids en baisse', 'Inspection, pesée', 'Perte d’eau'],
         ['Réflexes diminués, hypotonie', 'Marteau réflexe', 'Hypercalcémie ou hypokaliémie'],
         ['Masse mammaire, adénopathie', 'Palpation des seins et des aires ganglionnaires', 'Cancer'],
         ['Confusion', 'Orientation, attention', 'Hypercalcémie sévère'],
        ]), 48))
PTS.append(POINT(6, 'Examen clinique', p6))

p7 = (P('Deux syndromes se distinguent. Le syndrome d’hypercalcémie associe polyurie, troubles digestifs et confusion. '
        'Le syndrome d’hypokaliémie chronique associe polyurie, faiblesse musculaire et anomalies de l’ECG.', 48) +
      F('Signes fonctionnels (symptômes rapportés)', UL(['Soif, polyurie', 'Constipation, nausées, douleurs abdominales', 'Fatigue, troubles de l’humeur', 'Crampes, faiblesse']), 48) +
      F('Signes physiques (constatés à l’examen)', UL(['Déshydratation', 'Réflexes diminués', 'Confusion', 'Masse tumorale éventuelle']), 48) +
      F('Syndrome d’hypercalcémie',
        TAB(['Signe', 'Mécanisme', 'Valeur'], [
         ['Polyurie hypotonique', 'CaSR rénal activé, aquaporine 2 diminuée', 'Déshydratation qui aggrave la calcémie'],
         ['Constipation, pancréatite, ulcère', 'Baisse de l’excitabilité, sécrétion de gastrine', 'Hypercalcémie prolongée'],
         ['Intervalle QT raccourci', 'Repolarisation accélérée', 'Risque de trouble du rythme'],
        ]), 48) +
      F('Syndrome d’hypokaliémie chronique',
        TAB(['Signe', 'Mécanisme', 'Valeur'], [
         ['Polyurie', 'Baisse de l’aquaporine 2', 'Réversible'],
         ['Faiblesse proximale, crampes', 'Hyperpolarisation musculaire', 'Hypokaliémie marquée'],
         ['Onde T aplatie, onde U', 'Repolarisation ralentie', 'Risque d’arythmie'],
        ]), 48))
PTS.append(POINT(7, 'Syndromes et signes cliniques', p7))

p8 = (P('Le critère biologique repose sur le calcium ionisé ou la ' + PAYNE + ' > 2,55 mmol/L, contrôlée sur un second prélèvement. '
        'Selon la recommandation de l’atelier international de 2022, l’hyperparathyroïdie primaire associe hypercalcémie et PTH élevée ou normale non freinée. '
        'Une calcémie élevée isolée ne suffit pas.', 48, 47) +
      F('Gravité de l’hypercalcémie',
        TAB(['Stade', 'Calcémie corrigée', 'Conduite'], [
         ['Légère', '2,60–2,99 mmol/L', 'Bilan ambulatoire si pas de symptôme'],
         ['Modérée', '3,00–3,49 mmol/L', 'Traitement selon les symptômes'],
         ['Sévère', '≥ 3,50 mmol/L', 'Hospitalisation, traitement immédiat'],
        ]) + P('Ces seuils sont ceux des revues de référence ; ils varient de ± 0,05 mmol/L selon les laboratoires.', 48)))
PTS.append(POINT(8, 'Critères diagnostiques', p8))

p9 = (H4('9.a Examen de référence') +
      P('La référence est le calcium ionisé ; la calcémie corrigée suffit si l’albumine est normale. '
        'La PTH intacte est l’examen d’orientation clé : sa sensibilité et sa spécificité sont élevées pour séparer les causes dépendantes de la PTH, sans valeur chiffrée unique publiée.', 48) +
      H4('9.b Examens de première et de deuxième intention') +
      P('En première intention : calcium, albumine, phosphate, PTH intacte, créatinine, kaliémie, magnésium, calcidiol et ECG. '
        'En deuxième intention, selon la PTH : calciurie et localisation de l’adénome, ou PTHrP, électrophorèse des protéines et imagerie.', 48, 47) +
      TAB(['Intention', 'Examen', 'Pourquoi'], [
       ['1re', 'PTH intacte', 'Sépare les causes dépendantes et indépendantes'],
       ['1re', 'Phosphate', 'Bas si PTH ou PTHrP en excès'],
       ['1re', 'Créatinine, kaliémie, magnésium', 'Retentissement rénal, hypokaliémie associée'],
       ['1re', 'ECG', 'QT court, arythmie'],
       ['2e, PTH élevée', 'Calciurie des 24 h ; échographie cervicale et scintigraphie au MIBI', 'Exclure la FHH, localiser l’adénome avant chirurgie'],
       ['2e, PTH basse', 'PTHrP, électrophorèse, chaînes légères, calcitriol, scanner', 'Cancer, myélome, granulomatose'],
      ]) +
      H4('9.c Prescription et calculs') +
      P('Indication : toute calcémie élevée confirmée. Moment : prélèvement sans garrot prolongé, PTH sur le même échantillon. '
        'Préparation : arrêt du thiazide si possible avant la calciurie.', 48, 47) +
      TAB(['Calcul', 'Formule', 'Seuil'], [
       ['Calcémie corrigée', 'Calcium total + 0,02 × (40 − albumine en g/L)', 'Normale 2,15–2,55 mmol/L'],
       ['Rapport de clairance calcium/créatinine', '(calcium urinaire × créatinine plasmatique) / (calcium plasmatique × créatinine urinaire)', '< 0,01 : FHH probable ; > 0,02 : hyperparathyroïdie'],
       ['Calciurie des 24 h', 'Dosage direct', '> 10 mmol/24 h : critère opératoire'],
      ]) +
      H4('9.d Interprétation : positif, négatif, limite, discordant') +
      TAB(['Résultat', 'Signification', 'Conduite'], [
       ['Positif : PTH élevée, phosphate bas', 'Hyperparathyroïdie primaire', 'Calciurie, localisation'],
       ['Négatif : PTH < 20 pg/mL', 'Cause indépendante de la PTH', 'PTHrP, électrophorèse, calcitriol'],
       ['Limite : PTH dans la norme haute', 'Non freinée, donc anormale face à une hypercalcémie', 'Calciurie pour exclure la FHH'],
       ['Discordant : rapport de clairance entre 0,01 et 0,02', 'Zone grise', 'Génétique CASR ou avis spécialisé'],
      ]) +
      H4('9.e Alternatives') +
      P('Grossesse : échographie cervicale, pas de scintigraphie. Enfant : penser aux formes génétiques. '
        'DFGe < 30 : la calciurie perd sa valeur. La TEP à la choline ou l’IRM cervicale servent si l’échographie et la scintigraphie sont négatives ; le scanner avec iode n’est pas nécessaire en première intention.', 47))
PTS.append(POINT(9, 'Examens complémentaires', p9))

p10 = (P('Si la calcémie est ≥ 3,5 mmol/L ou symptomatique, alors le médecin réhydrate d’abord par NaCl 0,9 % ; la perfusion corrige la déshydratation et relance l’élimination du calcium. '
         'La PTH oriente ensuite vers la cause.', 85, 48) +
       F('Arbre décisionnel devant une hypercalcémie',
         OL(['Confirmer la calcémie corrigée ou le calcium ionisé.',
             'Sévère ou symptomatique : hospitalisation, NaCl 0,9 %, antirésorptif.',
             'PTH élevée ou normale : calciurie ; rapport < 0,01 → FHH ; sinon hyperparathyroïdie.',
             'PTH basse : PTHrP, électrophorèse, calcidiol et calcitriol.',
             'Toujours : arrêter le thiazide, le calcium et la vitamine D ; corriger la kaliémie.']), 48, 85))
PTS.append(POINT(10, 'Arbre décisionnel', p10))

fiche = FICHE([
  ['Anticorps anti-RANKL : dénosumab (Xgeva®)', 'Bloque le RANKL et donc la formation des ostéoclastes', 'Pas d’élimination rénale ; demi-vie ≈ 4 semaines', '120 mg SC ; schéma selon l’AIPS', 'Hypocalcémie (surtout si DFGe bas), ostéonécrose de la mâchoire', 'Hypocalcémie non corrigée', 'Aucune majeure'],
  ['Bisphosphonate : acide zolédronique (Zometa®)', 'Inhibe la farnésyl-pyrophosphate synthase ; l’ostéoclaste meurt', 'Élimination rénale', '4 mg IV en ≥ 15 min ; effet en 2–4 jours, durée 3–4 semaines', 'Fièvre, insuffisance rénale, ostéonécrose de la mâchoire', 'Insuffisance rénale sévère', 'Aminosides, diurétiques de l’anse'],
  ['Calcimimétique : cinacalcet (Mimpara®)', 'Rend le CaSR plus sensible ; la PTH baisse', 'Métabolisme hépatique (CYP3A4)', '30 mg 2 fois/j, à adapter', 'Nausées, hypocalcémie', 'Hypocalcémie', 'Inhibiteurs du CYP2D6 et du CYP3A4'],
 ], 85, 55, 47)
p11 = (H4('11.A Buts : d’abord l’urgence (calcémie ≥ 3,5 mmol/L, confusion), car elle menace le cœur et le rein') +
       P('Le traitement baisse la calcémie, restaure la concentration urinaire et traite la cause.', 85) +
       TAB(['But', 'Cible chiffrée'], [
        ['Diurèse', '100–150 mL/h sous perfusion'],
        ['Calcémie corrigée', 'Retour < 2,6 mmol/L'],
        ['Kaliémie', '> 3,5 mmol/L'],
       ]) +
       H4('11.B Moyens et méthodes : forme compliquée en urgence, forme non compliquée en ambulatoire') +
       P('La forme compliquée se traite en urgence : NaCl 0,9 % à 200–300 mL/h dans les premières heures, puis un antirésorptif. '
         'Le furosémide ne sert qu’en cas de surcharge, après réhydratation. '
         'La calcitonine agit en 4–6 h ; on l’arrête après 48–72 h, car son effet s’épuise.', 85) +
       P('En ambulatoire, l’éducation porte sur l’hydratation et l’arrêt du thiazide et des suppléments.', 48) +
       F('Traitements selon la cause',
         TAB(['Situation', 'Traitement', 'Pourquoi'], [
          ['Hypercalcémie maligne', 'Dénosumab, suggéré avant l’acide zolédronique (Endocrine Society 2023)', 'Efficace même si le rein est altéré'],
          ['Calcémie > 3,5 mmol/L', 'Calcitonine 4 UI/kg SC toutes les 12 h, en plus', 'Effet rapide, transitoire'],
          ['Granulome, lymphome, intoxication à la vitamine D', 'Prednisone 40–60 mg/j', 'Freine la production de calcitriol'],
          ['Hyperparathyroïdie primaire symptomatique', 'Parathyroïdectomie', 'Seul traitement curatif'],
          ['Hyperparathyroïdie asymptomatique', 'Chirurgie si : âge < 50 ans, calcémie > 0,25 mmol/L au-dessus de la norme, DFGe < 60, calciurie > 10 mmol/24 h ou lithiase, T-score ≤ −2,5 ou fracture vertébrale', 'Critères de 2022'],
          ['Hypokaliémie', 'Chlorure de potassium oral ; spironolactone si hyperaldostéronisme', 'Restaure l’aquaporine 2'],
         ]), 85, 47) +
       fiche +
       F('Situations particulières',
         TAB(['Situation', 'Particularité'], [
          ['Grossesse', 'Chirurgie au 2e trimestre si nécessaire ; dénosumab et bisphosphonates déconseillés'],
          ['Personne âgée', 'Réhydratation prudente (cœur)'],
          ['Enfant', 'Formes génétiques ; avis spécialisé'],
          ['Insuffisance rénale (DFGe < 30)', 'Préférer le dénosumab ; surveiller l’hypocalcémie'],
          ['Insuffisance hépatique', 'Cinacalcet avec prudence'],
         ]), 85, 47, 55) +
       SOCIAL('Un arrêt de travail est souvent nécessaire pendant l’hospitalisation et la convalescence (durée non chiffrée dans les sources).',
              'La conduite est déconseillée en cas de confusion ou de faiblesse (OAC, annexe 1).') +
       H4('11.C Surveillance et critères de sortie') +
       TAB(['Quand', 'Quoi'], [
        ['Toutes les 12–24 h en aigu', 'Calcémie, kaliémie, phosphate, créatinine, bilan entrées-sorties'],
        ['J1–J3 après parathyroïdectomie', 'Calcémie ; chercher un syndrome de l’os affamé'],
        ['Chaque année (surveillance)', 'Calcémie, créatinine, densitométrie selon le cas'],
        ['Critères de sortie', 'Calcémie < 3 mmol/L stable, prise orale, patient lucide, suivi organisé'],
       ]) +
       H4('11.D Pronostic et recherche 2026') +
       P('La polyurie guérit en quelques jours à semaines après correction de la calcémie et de la kaliémie. '
         'Le pronostic de l’hypercalcémie maligne dépend du cancer. En 2026, la recherche porte sur la chirurgie précoce de l’hyperparathyroïdie asymptomatique.', 48, 50, 47))
PTS.append(POINT(11, 'Prise en charge', p11))

p12 = (P('Avant le dénosumab ou l’acide zolédronique au long cours, un bilan dentaire réduit le risque d’ostéonécrose de la mâchoire. '
         'Après le dénosumab, la calcémie doit être surveillée, car l’hypocalcémie rebond est possible.', 85, 55) +
       F('Prévention primaire, secondaire et tertiaire',
         TAB(['Niveau', 'Mesure'], [
          ['Primaire', 'Ne pas surdoser la vitamine D et le calcium'],
          ['Secondaire', 'Calcémie devant une lithiase, une ostéoporose ou une polyurie'],
          ['Tertiaire', 'Bilan dentaire avant antirésorptif, suivi osseux et rénal'],
         ]) + P('En Suisse, l’OFSP et la SSED ne publient pas de dépistage systématique de la calcémie.', 47)))
PTS.append(POINT(12, 'Prévention', p12))

PTS.append(POINT(13, 'Points clés',
 P('Une PTH normale face à une hypercalcémie est anormale : elle évoque une hyperparathyroïdie primaire. '
   'Avant d’opérer, la calciurie exclut une hypercalcémie hypocalciurique familiale. '
   'L’urgence se traite d’abord par la réhydratation. '
   'La polyurie guérit quand la calcémie et la kaliémie se normalisent.', 48, 47)))

PTS.append(POINT(14, 'Pièges d’examen',
 TAB(['Piège', 'Ce qu’il faut répondre'], [
  ['Croire qu’une PTH normale exclut l’hyperparathyroïdie', 'Face à une hypercalcémie, la PTH devrait être freinée'],
  ['Opérer une FHH', 'Rapport de clairance < 0,01 : génétique, pas de chirurgie'],
  ['Donner du furosémide avant la réhydratation', 'Aggrave la déshydratation'],
  ['Confondre os affamé et hypoparathyroïdie après chirurgie', 'Os affamé : calcium < 2,1 mmol/L avec phosphate bas ; hypoparathyroïdie : phosphate élevé'],
 ]) + P('Le syndrome de l’os affamé se traite par calcium et calcitriol (Rocaltrol®) à forte dose.', 86)))

CTX = {'_prefixe': 'Devant une hypercalcémie',
 'pth': 'Une PTH élevée ou normale non freinée signe une hyperparathyroïdie primaire ; < 20 pg/mL oriente vers une cause indépendante.',
 'pthrp': 'Une PTHrP élevée avec PTH basse signe une hypercalcémie humorale maligne.',
 'calciurie': 'Un rapport de clairance calcium/créatinine < 0,01 évoque une FHH.',
 'vitd': 'Un calcidiol très élevé signe une intoxication ; un calcitriol élevé une granulomatose.',
 'iono': 'La kaliémie et la calcémie corrigée se suivent toutes les 12–24 h en aigu.',
 'creat': 'Le DFGe guide le choix de l’antirésorptif.',
 'ecg': 'L’ECG cherche un QT court ou des ondes U.',
 'mibi': 'La scintigraphie localise l’adénome avant chirurgie, jamais pour poser le diagnostic.',
 'epp': 'Un pic monoclonal oriente vers un myélome.'}
if __name__ == '__main__':
    produire(M, PTS, SOURCES, CTX)
