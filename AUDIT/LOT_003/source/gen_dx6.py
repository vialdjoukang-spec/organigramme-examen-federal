# -*- coding: utf-8 -*-
"""DX.6 — Soif non osmotique de l'insuffisance cardiaque et de la cirrhose. LOT 3, V5 → V7 AUDITÉ."""
from lot3_commun import *
POINT = mkPOINT('dx6')
M = META('dx6', 'DX.6', 'Insuffisance cardiaque et cirrhose', 'Soif non osmotique et hyponatrémie de dilution (insuffisance cardiaque, cirrhose)',
         'LOT_003_DX6_Insuffisance_cardiaque_cirrhose_AUDITÉ.html',
         'Corrections majeures : « 200 000 patients en Suisse », « 20–45 % de soif » et « 20 % d’hyponatrémie » remplacés par des données publiées (ESC 2021, OPTIMIZE-HF 2007, Angeli 2006) ; « les 4 piliers réduisent la mortalité de 60 % » corrigé (critère combiné, estimation inter-essais) ; affirmations non prouvées (gliflozine corrigeant l’hyponatrémie, sacubitril/valsartan « éteignant la soif ») retirées ; mention Swisstransplant non vérifiée retirée.')
VAE = T('volume artériel efficace', 'Le volume artériel efficace est la part du sang qui remplit réellement les artères et perfuse les organes ; il peut baisser alors que l’eau totale augmente.')
SAAG = T('SAAG', 'Le gradient d’albumine sérum-ascite (SAAG) est l’albumine sérique moins l’albumine de l’ascite ; ≥ 11 g/L signe une hypertension portale.')
PTS = []

p1 = (P('Dans l’insuffisance cardiaque (IC) et la cirrhose décompensée, le patient a soif alors qu’il a trop d’eau et de sel. '
        'Le ' + VAE + ' baisse ; le cerveau et le rein réagissent comme à une hémorragie. '
        'La soif et la vasopressine retiennent l’eau, d’où une hyponatrémie de dilution.', 40, 41) +
      F('Terminologie',
        TAB(['Terme', 'Définition exacte', 'À ne pas confondre avec'], [
         ['Soif non osmotique', 'Soif déclenchée par la baisse de pression ou de volume, sans hyperosmolalité', 'Soif osmotique (hypernatrémie)'],
         ['Hyponatrémie hypervolémique', 'Natrémie < 135 mmol/L avec œdèmes ou ascite', 'Hyponatrémie hypovolémique (diurétique, pertes digestives)'],
         ['IC à FEVG réduite', 'Fraction d’éjection ventriculaire gauche ≤ 40 %', 'IC à FEVG préservée (≥ 50 %)'],
         ['Ascite réfractaire', 'Ascite qui récidive ou résiste aux diurétiques à dose maximale', 'Ascite tendue simple'],
         ['Syndrome hépatorénal', 'Insuffisance rénale fonctionnelle de la cirrhose, sans réponse à l’albumine', 'Insuffisance rénale prérénale par diurétique'],
        ]), 40, 41))
PTS.append(POINT(1, 'Définition et sémantique', p1))

p2 = (P('Selon l’ESC, l’IC touche 1–2 % des adultes dans les pays européens ; aucune donnée suisse publiée récente n’a été trouvée. '
        'Dans un registre américain de 47 647 patients hospitalisés pour IC, 19,7 % ont une natrémie < 135 mmol/L. '
        'Dans une enquête européenne et mondiale chez 997 cirrhotiques avec ascite, 49,4 % ont une natrémie < 135 mmol/L.', 40, 81, 42) +
      F('Chiffres, terrain et histoire naturelle',
        TAB(['Donnée', 'Valeur', 'Portée'], [
         ['IC, adultes des pays européens', '1–2 %', 'Hausse avec l’âge'],
         ['Natrémie < 135 mmol/L à l’admission pour IC', '19,7 %', 'Registre OPTIMIZE-HF (États-Unis)'],
         ['Cirrhose avec ascite : natrémie < 135 / ≤ 130 / ≤ 125 mmol/L', '49,4 % / 21,6 % / 5,7 %', 'Enquête de 2006'],
         ['Soif gênante dans l’IC', 'Fréquente ; fréquence variable selon les études', 'Revue systématique de 2013'],
         ['Pronostic', 'L’hyponatrémie prédit la mortalité hospitalière et précoce', 'Facteur pronostique indépendant'],
        ]) + P('Le terrain à risque associe grand âge, IC avancée, cirrhose ascitique et diurétiques à forte dose ; la mortalité croît quand la natrémie baisse.', 81, 42), 43))
PTS.append(POINT(2, 'Épidémiologie (Suisse, puis Europe)', p2))

p3 = (P('Dans l’IC, le débit cardiaque baisse ; dans la cirrhose, les artères splanchniques se dilatent sous l’effet du monoxyde d’azote. '
        'Les barorécepteurs perçoivent une pression basse. Ils activent le système rénine-angiotensine-aldostérone, le sympathique et la vasopressine. '
        'L’angiotensine II stimule directement la soif ; la vasopressine retient l’eau ; l’aldostérone retient le sel.', 40, 41) +
      F('Chaîne logique : de l’anatomie au traitement',
        TAB(['Étape', 'Ce qu’il faut comprendre'], [
         ['Anatomie', 'Barorécepteurs du sinus carotidien, de la crosse aortique et de l’artériole afférente ; organe subfornical sans barrière hémato-encéphalique.'],
         ['Physiologie', 'Pourquoi on retient l’eau après une hémorragie : la baisse de pression active la soif et la vasopressine, même si l’osmolalité est normale.'],
         ['Physiopathologie', 'Dans l’IC et la cirrhose, ce réflexe persiste ; l’eau est retenue malgré l’hyponatrémie.'],
         ['Clinique', 'D’où les œdèmes, l’ascite, la soif et la prise de poids.'],
         ['Examens', 'On cherche la cause (échocardiographie, NT-proBNP, ponction d’ascite) et on mesure la natrémie.'],
         ['Traitement', 'On bloque le système rénine-angiotensine-aldostérone, on élimine le sel et on limite l’eau si l’hyponatrémie est marquée.'],
        ]), 40, 41) +
      F('Mécanisme, exploration et cible thérapeutique',
        TAB(['Mécanisme', 'Exploration', 'Cible thérapeutique'], [
         ['Baisse du débit cardiaque', 'Échocardiographie, NT-proBNP', 'Traitements de fond de l’IC'],
         ['Vasodilatation splanchnique (cirrhose)', 'Échographie Doppler hépatique, ponction d’ascite', 'Albumine, traitement de la cause'],
         ['Activation rénine-angiotensine-aldostérone', 'Natriurèse basse, kaliémie', 'Antagoniste des minéralocorticoïdes, sacubitril/valsartan'],
         ['Vasopressine non osmotique', 'Natrémie basse, urine concentrée', 'Restriction hydrique si natrémie < 125–130 mmol/L'],
         ['Rétention de sel', 'Poids, œdèmes', 'Diurétiques, sel modéré'],
        ]), 40, 41))
PTS.append(POINT(3, 'Physiopathologie', p3))

p4 = (P('Le clinicien vérifie d’abord l’urgence : œdème pulmonaire, encéphalopathie, natrémie < 125 mmol/L. '
        'Puis il classe l’hyponatrémie selon le volume : œdèmes ou ascite (dilution) contre hypotension orthostatique sans œdème (excès de diurétique). '
        'Enfin, chez le cirrhotique, il écarte le syndrome hépatorénal.', 41, 62) +
      DIFF('ic') +
      F('Hyponatrémie chez le cirrhotique avec ascite (même population, 997 patients ; probabilités en exposant rouge)',
        TAB(['Seuil de natrémie', 'Signification', 'Conduite'], [
         ['< 135 mmol/L' + PR('49,4 %', 42), 'Hyponatrémie fréquente', 'Surveillance, revue des diurétiques'],
         ['≤ 130 mmol/L' + PR('21,6 %', 42), 'Plus d’ascite réfractaire et d’encéphalopathie', 'Restriction hydrique selon EASL'],
         ['≤ 125 mmol/L' + PR('5,7 %', 42), 'Hyponatrémie sévère', 'Arrêt des diurétiques, avis spécialisé'],
        ]) + P('Les autres causes (excès de diurétique, syndrome hépatorénal) n’ont pas de prévalence publiée dans cette population.', 41)))
PTS.append(POINT(4, 'Raisonnement clinique et diagnostic différentiel', p4))

p5 = (P('L’anamnèse évalue la dyspnée selon la classe NYHA (New York Heart Association, I à IV) et l’orthopnée. '
        'Elle relève la prise de poids, les boissons, le sel et les médicaments, surtout les anti-inflammatoires.', 40, 41) +
      U('Drapeaux rouges : œdème aigu du poumon, encéphalopathie hépatique (astérixis), fièvre avec ascite (infection), hémorragie digestive, natrémie < 125 mmol/L. Ils imposent une hospitalisation immédiate.', 40, 41) +
      F('Questions ciblées et leur raison',
        TAB(['Question', 'Pourquoi la poser'], [
         ['Combien d’oreillers utilisez-vous pour dormir ?', 'L’orthopnée signe une congestion pulmonaire.'],
         ['Avez-vous pris plus de 2 kg en 3 jours ?', 'C’est un signe précoce de décompensation.'],
         ['Combien buvez-vous, avez-vous très soif ?', 'La soif non osmotique augmente les apports.'],
         ['Prenez-vous un anti-inflammatoire (ibuprofène Irfen®, diclofénac Voltaren®) ?', 'Il bloque les prostaglandines rénales et précipite l’insuffisance rénale.'],
         ['Êtes-vous confus, somnolent ?', 'Encéphalopathie hépatique ou hyponatrémie.'],
         ['Avez-vous de la fièvre ou mal au ventre ?', 'Infection spontanée du liquide d’ascite.'],
        ]), 40, 41))
PTS.append(POINT(5, 'Anamnèse ciblée et drapeaux rouges', p5))

p6 = (P('L’examen cherche l’excès de liquide extracellulaire. À l’état normal, les veines jugulaires ne sont pas visibles à 45° et il n’y a ni œdème ni matité des flancs. '
        'La turgescence jugulaire a une bonne spécificité mais une sensibilité modeste pour la congestion.', 40) +
      F('Signes, technique et valeur',
        TAB(['Signe', 'Technique', 'Ce qu’il signifie'], [
         ['Œdèmes prenant le godet', 'Pression de 5 secondes sur le tibia', 'Excès de sel et d’eau'],
         ['Turgescence jugulaire, reflux hépato-jugulaire', 'Patient à 45°, pression abdominale', 'Pression veineuse élevée (IC droite)'],
         ['Crépitants, galop B3', 'Auscultation', 'Congestion gauche'],
         ['Matité déclive des flancs', 'Percussion, changement de position', 'Ascite (> 1,5 L environ)'],
         ['Ictère, angiomes stellaires, circulation collatérale', 'Inspection', 'Cirrhose'],
         ['Astérixis', 'Bras tendus, poignets en extension', 'Encéphalopathie hépatique'],
        ]), 40, 41))
PTS.append(POINT(6, 'Examen clinique', p6))

p7 = (P('Deux syndromes se combinent. Le syndrome d’hyperhydratation extracellulaire avec hyponatrémie de dilution associe œdèmes, soif et natrémie basse. '
        'Le syndrome d’IC congestive associe signes gauches et droits.', 40, 41) +
      F('Signes fonctionnels (symptômes rapportés)', UL(['Soif persistante', 'Dyspnée d’effort, orthopnée', 'Prise de poids, gonflement des jambes', 'Ventre qui gonfle (ascite)', 'Fatigue, confusion']), 43) +
      F('Signes physiques (constatés à l’examen)', UL(['Œdèmes, ascite', 'Turgescence jugulaire', 'Crépitants, galop', 'Ictère, astérixis (cirrhose)']), 40) +
      F('Syndrome d’hyperhydratation extracellulaire avec hyponatrémie de dilution',
        TAB(['Signe', 'Mécanisme', 'Valeur'], [
         ['Œdèmes, ascite', 'Rétention de sel par l’aldostérone', 'Hypervolémie'],
         ['Natriurèse < 20 mmol/L (sans diurétique)', 'Rein qui retient le sel', 'Confirme la rétention'],
         ['Natrémie < 135 mmol/L', 'Vasopressine non osmotique', 'Pronostic défavorable'],
        ]), 41, 81) +
      F('Syndrome d’IC congestive globale',
        TAB(['Signe', 'Mécanisme', 'Valeur'], [
         ['Orthopnée, crépitants', 'Congestion pulmonaire', 'IC gauche'],
         ['Turgescence jugulaire, hépatalgie', 'Congestion veineuse systémique', 'IC droite'],
         ['NT-proBNP élevé', 'Étirement des cardiomyocytes', 'Confirme l’IC'],
        ]), 40))
PTS.append(POINT(7, 'Syndromes et signes cliniques', p7))

p8 = (P('Le critère ESC 2021 de l’IC associe symptômes, signes et preuve objective : FEVG mesurée et NT-proBNP ≥ 125 pg/mL en ambulatoire. '
        'Pour l’ascite, la recommandation EASL 2018 retient un SAAG ≥ 11 g/L comme signe d’hypertension portale. '
        'Un œdème isolé ne suffit pas.', 40, 41) +
      F('Phénotypes de l’IC et seuils de NT-proBNP (ESC 2021)',
        TAB(['Phénotype', 'FEVG', 'Remarque'], [
         ['IC à FEVG réduite', '≤ 40 %', 'Quatre classes de traitement de fond'],
         ['IC à FEVG modérément réduite', '41–49 %', 'Traitement proche de l’IC réduite'],
         ['IC à FEVG préservée', '≥ 50 % avec anomalie structurelle ou pressions élevées', 'Gliflozine, diurétiques'],
         ['NT-proBNP en ambulatoire', '≥ 125 pg/mL (BNP ≥ 35)', '< 125 pg/mL rend l’IC peu probable'],
         ['NT-proBNP en aigu', '≥ 300 pg/mL (BNP ≥ 100)', 'Seuils selon l’âge : 450, 900, 1800 pg/mL (< 50, 50–75, > 75 ans)'],
        ]) + P('Ces seuils proviennent des recommandations ESC 2021 et de leur mise à jour 2023.', 40)))
PTS.append(POINT(8, 'Critères diagnostiques', p8))

p9 = (H4('9.a Examen de référence') +
      P('Pour l’IC, la référence est l’échocardiographie transthoracique, complétée par le NT-proBNP. Un NT-proBNP < 125 pg/mL a une sensibilité élevée et une valeur prédictive négative forte ; sa spécificité est faible. '
        'Pour l’ascite, la référence est la ponction avec ' + SAAG + ' ; un SAAG ≥ 11 g/L a une précision ≈ 97 %, avec une bonne sensibilité et spécificité.', 40, 41) +
      H4('9.b Examens de première et de deuxième intention') +
      P('En première intention : ionogramme sanguin et urinaire, créatinine et DFGe, NT-proBNP, ECG, bilan hépatique avec albumine et INR. '
        'En deuxième intention : échocardiographie, échographie Doppler du foie, ponction d’ascite.', 40, 41) +
      TAB(['Intention', 'Examen', 'Pourquoi'], [
       ['1re', 'Ionogramme et natriurèse', 'Hyponatrémie de dilution, rétention de sel'],
       ['1re', 'Créatinine, kaliémie', 'Fonction rénale avant les bloqueurs du système rénine-angiotensine'],
       ['1re', 'NT-proBNP et ECG', 'Probabilité d’IC'],
       ['1re', 'Bilirubine, albumine, INR', 'Scores de Child-Pugh et MELD-Na'],
       ['2e', 'Échocardiographie', 'FEVG et phénotype'],
       ['2e', 'Ponction d’ascite', 'SAAG, protéines, polynucléaires (infection si ≥ 250/mm³)'],
      ]) +
      H4('9.c Prescription et calculs') +
      P('Indication : toute ascite nouvelle ou toute décompensation (ponction systématique). Moment : à l’admission, avant les antibiotiques. '
        'Préparation : pas de correction systématique de l’INR ou des plaquettes avant la ponction selon l’EASL.', 41) +
      TAB(['Calcul', 'Formule', 'Seuil'], [
       ['SAAG', 'Albumine sérique − albumine de l’ascite', '≥ 11 g/L : hypertension portale'],
       ['Protéines de l’ascite', 'Dosage direct', '> 25 g/L avec SAAG ≥ 11 : origine cardiaque probable'],
       ['MELD-Na', 'Bilirubine, INR, créatinine et natrémie (bornée entre 125 et 137 mmol/L)', 'Plus la natrémie baisse, plus le score monte'],
      ]) +
      H4('9.d Interprétation : positif, négatif, limite, discordant') +
      TAB(['Résultat', 'Signification', 'Conduite'], [
       ['Positif : NT-proBNP ≥ 125 pg/mL', 'IC possible', 'Échocardiographie'],
       ['Négatif : NT-proBNP < 125 pg/mL', 'IC peu probable', 'Chercher une autre cause'],
       ['Limite : NT-proBNP modéré chez l’obèse', 'Valeurs plus basses dans l’obésité', 'Échocardiographie quand même'],
       ['Discordant : NT-proBNP élevé, FEVG normale', 'IC à FEVG préservée, insuffisance rénale, fibrillation auriculaire', 'Recherche des anomalies diastoliques'],
      ]) +
      H4('9.e Alternatives') +
      P('Grossesse : NT-proBNP et échocardiographie utilisables. Enfant : causes congénitales, avis spécialisé. '
        'DFGe < 30 : NT-proBNP plus élevé, interpréter avec prudence. L’IRM cardiaque ou le scanner avec produit iodé servent seulement si l’échocardiographie ne suffit pas.', 40))
PTS.append(POINT(9, 'Examens complémentaires', p9))

p10 = (P('Si le patient œdémateux a une hyponatrémie, le médecin ne perfuse pas de NaCl 0,9 %, car il aggrave l’œdème sans corriger la natrémie. '
         'Il oriente plutôt vers le traitement de la cause, les diurétiques et une restriction hydrique si la natrémie est basse.', 40, 41) +
       F('Arbre décisionnel : soif et hyponatrémie chez un patient œdémateux',
         OL(['Œdème pulmonaire, encéphalopathie, hémorragie : urgence.',
             'Œdèmes ou ascite : hyponatrémie de dilution → traitement de la cause, diurétiques, restriction hydrique si natrémie < 125–130 mmol/L.',
             'Pas d’œdème, hypotension orthostatique : excès de diurétique → réduire, réhydrater prudemment.',
             'Cirrhose et créatinine en hausse : arrêt des diurétiques, albumine 1 g/kg ; si pas de réponse, syndrome hépatorénal.',
             'IC à FEVG réduite : instaurer les quatre classes de traitement de fond.']), 40, 41))
PTS.append(POINT(10, 'Arbre décisionnel', p10))

fiche = FICHE([
  ['Inhibiteur de l’angiotensine et de la néprilysine : sacubitril/valsartan (Entresto®)', 'Bloque le récepteur AT1 et freine la dégradation des peptides natriurétiques', 'Demi-vie ≈ 1,4 h (sacubitril) et ≈ 10 h (valsartan)', '24/26 mg 2 fois/j, cible 97/103 mg 2 fois/j ; au long cours', 'Hypotension, hyperkaliémie, angiœdème', 'Inhibiteur de l’enzyme de conversion dans les 36 h, angiœdème', 'Potassium, épargneurs de potassium'],
  ['Antagoniste des minéralocorticoïdes : spironolactone (Aldactone®)', 'Bloque le récepteur de l’aldostérone', 'Métabolites actifs, demi-vie > 12 h', 'IC : 25–50 mg/j ; ascite : 100–400 mg/j', 'Hyperkaliémie, gynécomastie', 'Kaliémie > 5,0 mmol/L, DFGe < 30', 'Sacubitril/valsartan, triméthoprime'],
  ['Bêtabloquant : bisoprolol (Concor®)', 'Bloque les récepteurs β1', 'Demi-vie ≈ 10–12 h', '1,25 mg/j, cible 10 mg/j', 'Bradycardie, fatigue', 'Bloc auriculo-ventriculaire de haut degré', 'Vérapamil, diltiazem'],
 ], 40, 41)
p11 = (H4('11.A Buts : d’abord l’urgence (œdème pulmonaire, encéphalopathie), car elle menace la vie en quelques heures') +
       P('Le traitement corrige la cause, élimine l’excès de sel et d’eau, et limite l’hyponatrémie.', 40, 41) +
       TAB(['But', 'Cible chiffrée'], [
        ['Perte de poids sous diurétiques (cirrhose)', '≤ 0,5 kg/j sans œdèmes, ≤ 1 kg/j avec œdèmes'],
        ['Sel', 'IC : < 5 g/j ; ascite : 80–120 mmol de sodium par jour (≈ 4,6–6,9 g de sel)'],
        ['Restriction hydrique', '1–1,5 L/j seulement si hyponatrémie (cirrhose < 125 mmol/L)'],
        ['Kaliémie', '< 5,5 mmol/L'],
       ]) +
       H4('11.B Moyens et méthodes : forme compliquée en urgence, forme non compliquée en ambulatoire') +
       P('L’œdème pulmonaire compliqué relève de l’urgence : diurétique de l’anse IV dans l’heure, oxygène, ventilation non invasive si besoin. '
         'Dans l’ascite tendue, la ponction évacuatrice soulage ; au-delà de 5 L, on perfuse 8 g d’albumine par litre retiré.', 40, 41) +
       P('En ambulatoire, l’éducation porte sur le poids quotidien, le sel et la soif ; sucer des glaçons limite le volume bu.', 43) +
       F('Traitements de fond selon la situation',
         TAB(['Situation', 'Traitement', 'Pourquoi'], [
          ['IC à FEVG réduite', 'Sacubitril/valsartan, bêtabloquant, antagoniste des minéralocorticoïdes, gliflozine', 'Ensemble, ils réduisent d’≈ 62 % le risque combiné de décès cardiovasculaire ou d’hospitalisation (estimation inter-essais)'],
          ['Congestion dans l’IC', 'Torasémide (Torem®) 10–40 mg/j ou furosémide (Lasix®)', 'Élimine le sel'],
          ['Ascite de la cirrhose', 'Spironolactone 100 mg + furosémide 40 mg, jusqu’à 400/160 mg/j', 'L’aldostérone est le moteur de la rétention'],
          ['IC à FEVG modérément réduite ou préservée', 'Gliflozine ; finérénone (essai de 2024) ; tirzépatide si obésité (essai de 2025)', 'Moins d’hospitalisations'],
         ]), 82, 59, 41, 83, 84) +
       fiche +
       F('Situations particulières',
         TAB(['Situation', 'Particularité'], [
          ['Grossesse', 'Sacubitril/valsartan et antagonistes des minéralocorticoïdes contre-indiqués'],
          ['Personne âgée', 'Hypotension et hyperkaliémie plus fréquentes : titration lente'],
          ['Enfant', 'Causes congénitales ; avis cardiopédiatrique'],
          ['Insuffisance rénale (DFGe < 30)', 'Spironolactone à éviter ; surveillance du potassium'],
          ['Insuffisance hépatique', 'Pas de tolvaptan dans la cirrhose (toxicité hépatique, saignements)'],
         ]), 40, 41, 55) +
       SOCIAL('Un arrêt de travail est souvent nécessaire en phase de décompensation (durée non chiffrée dans les sources).',
              'La conduite est déconseillée en IC de classe NYHA IV ou en encéphalopathie hépatique (OAC, annexe 1).',
              'L’AI peut intervenir si l’IC ou la cirrhose limitent durablement la capacité de travail.') +
       H4('11.C Surveillance et critères de sortie') +
       TAB(['Quand', 'Quoi'], [
        ['Chaque jour, à jeun', 'Poids ; consulter si +2 kg en 3 jours'],
        ['1–2 semaines après chaque palier', 'Créatinine, kaliémie, natrémie ; arrêt de la spironolactone si kaliémie > 6 mmol/L'],
        ['Tous les 6 mois (cirrhose)', 'Échographie hépatique (carcinome hépatocellulaire)'],
        ['Critères de sortie', 'Poids sec atteint, natrémie stable, diurétique oral efficace, éducation faite'],
       ]) +
       H4('11.D Pronostic et recherche 2026') +
       P('Le pronostic dépend de la cause : l’hyponatrémie prédit la mortalité dans l’IC et la cirrhose. '
         'En 2026, la recherche porte sur la finérénone et les agonistes du GLP-1 dans l’IC à FEVG préservée ; leur autorisation suisse dans cette indication reste à vérifier.', 81, 42, 83, 84))
PTS.append(POINT(11, 'Prise en charge', p11))

p12 = (P('Dans la cirrhose ascitique, les anti-inflammatoires sont à éviter, car ils bloquent les prostaglandines rénales et précipitent l’insuffisance rénale. '
         'Dans l’IC, la vaccination et le traitement de fond préviennent les décompensations.', 41, 40) +
       F('Prévention primaire, secondaire et tertiaire',
         TAB(['Niveau', 'Mesure'], [
          ['Primaire', 'Contrôle de la pression, du diabète et de l’alcool (OFSP, stratégie MNT)'],
          ['Secondaire', 'NT-proBNP et échocardiographie devant une dyspnée ; échographie hépatique chez le buveur'],
          ['Tertiaire', 'Éducation, poids quotidien, réadaptation cardiaque, abstinence d’alcool'],
         ]) + P('En Suisse, la réadaptation cardiaque ambulatoire est remboursée par la LAMal sur prescription.', 56)))
PTS.append(POINT(12, 'Prévention', p12))

PTS.append(POINT(13, 'Points clés',
 P('Le patient œdémateux a soif parce que son volume artériel efficace est bas. '
   'L’hyponatrémie de dilution ne se traite pas par du NaCl 0,9 %. '
   'Dans l’ascite, la spironolactone est le diurétique de première intention. '
   'Une natrémie basse est un marqueur pronostique défavorable.', 41, 81)))

PTS.append(POINT(14, 'Pièges d’examen',
 TAB(['Piège', 'Ce qu’il faut répondre'], [
  ['Perfuser du NaCl 0,9 % chez un cirrhotique hyponatrémique', 'Aggrave l’ascite sans corriger la natrémie'],
  ['Utiliser le tolvaptan dans la cirrhose', 'À éviter : toxicité hépatique et saignements digestifs'],
  ['Donner un anti-inflammatoire à un cirrhotique', 'Risque d’insuffisance rénale aiguë'],
  ['Restreindre l’eau chez tous les insuffisants cardiaques', 'Seulement si hyponatrémie ou congestion sévère'],
 ]) + P('Ces règles suivent les recommandations EASL 2018 et ESC 2021.', 41, 40)))

CTX = {'_prefixe': 'Chez le patient œdémateux',
 'iono': 'Une natrémie < 135 mmol/L avec œdèmes signe une hyponatrémie de dilution ; < 125 mmol/L, elle impose un avis spécialisé.',
 'natriurese': 'Sans diurétique, une natriurèse < 20 mmol/L confirme la rétention de sel.',
 'creat': 'La créatinine se contrôle 1–2 semaines après chaque palier de bloqueur du système rénine-angiotensine.',
 'bnp': 'Un NT-proBNP < 125 pg/mL en ambulatoire rend l’IC peu probable (ESC 2021).',
 'echocoeur': 'L’échocardiographie mesure la FEVG et classe l’IC.',
 'ascite': 'Un SAAG ≥ 11 g/L signe une hypertension portale ; ≥ 250 polynucléaires/mm³ une infection.',
 'ecg': 'L’ECG cherche une fibrillation auriculaire ou une séquelle d’infarctus.',
 'hep': 'La bilirubine, l’albumine et l’INR calculent les scores de Child-Pugh et MELD-Na.'}
if __name__ == '__main__':
    produire(M, PTS, SOURCES, CTX)
