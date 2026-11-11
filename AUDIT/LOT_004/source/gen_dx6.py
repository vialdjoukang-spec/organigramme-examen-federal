# -*- coding: utf-8 -*-
"""DX.6 — Insuffisance cardiaque chronique. LOT 4, V5 → V7 AUDITÉ."""
from lot4_commun import *
POINT = mkPOINT('dx6')
M = META('dx6', 'DX.6', 'Insuffisance cardiaque chronique', 'Insuffisance cardiaque chronique (fatigue d’effort)',
         'LOT_004_DX6_Insuffisance_cardiaque_AUDITÉ.html',
         'Corrections majeures : le B3 n’est pas pathognomonique ; CHAMPIT liste des facteurs de décompensation, pas des étiologies ; l’omecamtiv mécarbil n’est pas autorisé ; cible de fréquence cardiaque < 70/min (ESC) au lieu de 50–60 ; seuils d’arrêt du potassium complétés ; chiffre suisse « 200 000 » non sourcé retiré.')
SRAA = T('système rénine-angiotensine-aldostérone', 'Le système rénine-angiotensine-aldostérone (SRAA) est une cascade hormonale qui resserre les artères et fait retenir le sel et l’eau ; activé en permanence, il abîme le cœur.')
NP = T('peptides natriurétiques', 'Les peptides natriurétiques (BNP et son fragment NT-proBNP) sont libérés par le muscle cardiaque étiré ; ils font éliminer le sel et l’eau, et leur taux reflète la surcharge du cœur.')
PTS = []
def ADD(*a): PTS.append(POINT(*a))
ADD(1, 'Définition et sémantique',
 P('L’insuffisance cardiaque est un syndrome : des symptômes (essoufflement, fatigue, œdèmes) causés par une anomalie du cœur qui élève les pressions de remplissage ou abaisse le débit. '
   'La fatigue d’effort vient du manque de sang livré aux muscles et de leur déconditionnement.', 25) +
 F('Terminologie (ESC 2021)',
   TAB(['Terme', 'Définition exacte', 'À ne pas confondre avec'], [
    ['IC à fraction d’éjection réduite (ICFEr)', 'FEVG ≤ 40 %', 'Cardiomyopathie sans symptômes'],
    ['IC à FE légèrement réduite (ICFEm)', 'FEVG 41–49 %', 'ICFEr'],
    ['IC à FE préservée (ICFEp)', 'FEVG ≥ 50 % avec anomalies structurelles ou de remplissage et peptides élevés', 'Dyspnée d’obésité ou de déconditionnement'],
    ['IC aiguë', 'Aggravation rapide des symptômes nécessitant un traitement urgent', 'IC chronique stable'],
    ['Classe NYHA', 'Classement des symptômes de I (aucun) à IV (au repos)', 'Gravité de la FEVG'],
   ]) + P('La FEVG classe l’insuffisance cardiaque ; elle ne mesure pas les symptômes.', 25)))
ADD(2, 'Épidémiologie (Suisse, puis Europe)',
 P('En Europe, l’insuffisance cardiaque touche 1–2 % des adultes et plus de 10 % des personnes de plus de 70 ans. '
   'En Suisse, aucune prévalence nationale récente n’a été retrouvée ; le chiffre de « 200 000 personnes » de l’original n’est pas sourcé.', 25) +
 F('Chiffres, terrain et histoire naturelle',
   TAB(['Donnée', 'Valeur', 'Portée'], [
    ['Prévalence, adultes, pays développés', '1–2 %', 'ESC 2021'],
    ['Prévalence après 70 ans', '> 10 %', 'ESC 2021'],
    ['Carence en fer chez l’insuffisant cardiaque', '≈ 50 %', 'ESC 2021'],
    ['Fatigue liée à une maladie somatique grave en premier recours', '4,3 % (toutes causes)', 'Revue de Stadje'],
    ['Prévalence suisse', 'Non publiée de façon récente', 'Chiffre de l’original retiré'],
   ]) + P('Le terrain réunit l’âge, l’hypertension, la maladie coronarienne, le diabète, l’obésité et la fibrillation atriale. '
          'Le pronostic est sévère, avec une mortalité élevée et de nombreuses hospitalisations ; les quatre médicaments de base la réduisent nettement.', 25, 2)))
ADD(3, 'Physiopathologie',
 P('Après une lésion du cœur, le débit baisse. Le corps compense en activant le système nerveux sympathique et le ' + SRAA + '. '
   'Ces systèmes soutiennent la pression à court terme, mais retiennent l’eau et abîment le myocarde à long terme. Le cœur étiré libère des ' + NP + '.', 25) +
 F('Chaîne logique : de l’anatomie au traitement',
   TAB(['Étape', 'Ce qu’il faut comprendre'], [
    ['Anatomie', 'Le ventricule gauche pompe le sang vers le corps ; les oreillettes et les veines pulmonaires reçoivent le sang en amont.'],
    ['Physiologie', 'Le débit dépend de la contraction, du remplissage et de la fréquence.'],
    ['Physiopathologie', 'La lésion baisse le débit ; les systèmes neuro-hormonaux retiennent l’eau ; la pression monte en amont (congestion).'],
    ['Clinique', 'D’où la fatigue (bas débit), l’essoufflement et les œdèmes (congestion).'],
    ['Examens', 'Le NT-proBNP mesure l’étirement ; l’échocardiographie mesure la FEVG.'],
    ['Traitement', 'Les quatre médicaments bloquent les systèmes neuro-hormonaux ; les diurétiques enlèvent l’eau.'],
   ]), 25) +
 F('Mécanisme, exploration et cible thérapeutique',
   TAB(['Mécanisme', 'Lésion ou cause', 'Exploration', 'Cible thérapeutique'], [
    ['Perte de muscle cardiaque', 'Infarctus, cardiomyopathie', 'Échocardiographie, coronarographie', 'Quadrithérapie, revascularisation'],
    ['Surcharge de pression', 'Hypertension, sténose aortique', 'Pression artérielle, échocardiographie', 'Antihypertenseurs, valve'],
    ['Activation neuro-hormonale', 'Sympathique, SRAA', 'Fréquence cardiaque, potassium', 'Bêtabloquant, ARNI, ARM'],
    ['Congestion', 'Rétention d’eau et de sel', 'Poids, œdèmes, NT-proBNP', 'Diurétique de l’anse'],
    ['Muscle squelettique', 'Perte des fibres oxydatives, carence en fer', 'Ferritine, saturation de la transferrine', 'Réadaptation, fer IV'],
   ]) + P('La fatigue d’effort est expliquée autant par le muscle squelettique que par le cœur ; c’est pourquoi la réadaptation améliore les symptômes.', 25)) +
 F('FEVG : calcul', P('FEVG (%) = (volume télédiastolique − volume télésystolique) / volume télédiastolique × 100.', 25) +
   P('Exemple : 180 mL et 117 mL donnent (180 − 117) / 180 × 100 = 35 %, soit une ICFEr.', 25)))
ADD(4, 'Raisonnement clinique et diagnostic différentiel',
 P('Devant une fatigue d’effort avec essoufflement, le médecin cherche d’abord une urgence : œdème pulmonaire, choc, syncope. '
   'Puis il dose le NT-proBNP et fait un ECG ; s’ils sont anormaux, l’échocardiographie confirme et classe. '
   'Ensuite, il cherche la cause et les facteurs de décompensation.', 25) +
 DIFF('ic') + DIFF_FAT() +
 F('Diagnostics voisins et facteurs de décompensation',
   TAB(['Diagnostic ou facteur', 'Élément distinctif', 'Examen discriminant'], [
    ['BPCO', 'Tabac, sifflements, toux', 'Spirométrie'],
    ['Anémie', 'Pâleur, hémoglobine basse', 'Hémogramme'],
    ['Embolie pulmonaire chronique', 'Dyspnée progressive après une embolie', 'Scintigraphie de ventilation-perfusion'],
    ['Déconditionnement, obésité', 'NT-proBNP normal', 'Test d’effort'],
    ['Facteurs de décompensation (CHAMPIT)', 'Syndrome coronarien, hypertension, arythmie, cause mécanique, embolie, infection, tamponnade ou toxiques', 'Selon le contexte'],
   ]) + P('CHAMPIT liste des facteurs qui déclenchent une décompensation ; l’original l’utilisait à tort pour l’étiologie de l’insuffisance chronique.', 25)))
ADD(5, 'Anamnèse ciblée et drapeaux rouges',
 P('L’anamnèse classe la gêne selon la NYHA et cherche l’orthopnée, la dyspnée nocturne, la prise de poids rapide (> 2 kg en 3 jours) et la nycturie. '
   'Elle note les médicaments, notamment les AINS, et l’observance du sel et des diurétiques.', 25) +
 U('Drapeaux rouges : œdème aigu du poumon (orthopnée immédiate, crachats mousseux), syncope d’effort, marbrures avec urine rare (choc cardiogénique), douleur thoracique. Ils imposent l’appel au 144 et une hospitalisation urgente.', 25) +
 F('Questions ciblées et leur raison',
   TAB(['Question', 'Pourquoi la poser'], [
    ['Combien d’étages montez-vous sans vous arrêter ?', 'Classe NYHA.'],
    ['Dormez-vous avec plusieurs oreillers ?', 'Orthopnée.'],
    ['Avez-vous pris du poids rapidement ?', 'Rétention d’eau.'],
    ['Prenez-vous des anti-inflammatoires ?', 'Ils retiennent le sel et aggravent la fonction rénale.'],
    ['Avez-vous eu une douleur thoracique ou des palpitations ?', 'Ischémie, fibrillation atriale.'],
    ['Avez-vous été traité par chimiothérapie ?', 'Cardiotoxicité (anthracyclines, trastuzumab).'],
   ]), 25))
ADD(6, 'Examen clinique',
 P('L’examen mesure la pression, le pouls et le poids. Il cherche une turgescence jugulaire, un reflux hépato-jugulaire, un galop, des râles crépitants et des œdèmes.', 25) +
 P('Valeurs normales : veine jugulaire non visible à 45°, pas de B3 après 40 ans. Le B3 a une spécificité élevée mais une sensibilité faible ; il n’est pas pathognomonique, contrairement à ce qu’affirmait l’original.', 25) +
 F('Signes, technique et valeur',
   TAB(['Signe', 'Technique', 'Ce qu’il signifie'], [
    ['Turgescence jugulaire', 'Patient à 45°, tête tournée', 'Pression veineuse élevée'],
    ['Reflux hépato-jugulaire', 'Pression sur le foie 10 s', 'Congestion droite'],
    ['Galop B3', 'Auscultation avec la cloche à la pointe, décubitus latéral gauche', 'Remplissage rapide d’un ventricule dilaté'],
    ['Râles crépitants', 'Auscultation des bases', 'Congestion pulmonaire'],
    ['Œdèmes prenant le godet', 'Pression 5 s sur la cheville', 'Rétention d’eau'],
    ['Choc de pointe dévié', 'Palpation', 'Ventricule dilaté'],
   ]), 25))
ADD(7, 'Syndromes et signes cliniques',
 F('Signes fonctionnels (symptômes rapportés)', UL(['Essoufflement d’effort', 'Fatigue, faiblesse', 'Orthopnée', 'Dyspnée paroxystique nocturne', 'Nycturie']), 25) +
 F('Signes physiques (constatés à l’examen)', UL(['Turgescence jugulaire', 'Galop B3', 'Râles crépitants', 'Œdèmes des jambes', 'Hépatomégalie']), 25) +
 P('Le syndrome de bas débit réunit fatigue, extrémités froides, pression basse et urine rare : il traduit le manque de débit. '
   'Le syndrome congestif réunit essoufflement, orthopnée, œdèmes et gros foie : il traduit la pression élevée en amont du cœur.', 25) +
 F('Syndrome de bas débit', TAB(['Signe', 'Mécanisme', 'Valeur'], [
    ['Fatigue', 'Muscles moins perfusés', 'Fréquente, peu spécifique'],
    ['Extrémités froides', 'Vasoconstriction', 'Gravité'],
    ['Oligurie', 'Rein moins perfusé', 'Choc si marquée'],
   ]), 25) +
 F('Syndrome congestif', TAB(['Signe', 'Mécanisme', 'Valeur'], [
    ['Orthopnée', 'Retour veineux accru couché', 'Évocatrice'],
    ['Œdèmes', 'Pression veineuse élevée', 'Peu spécifiques'],
    ['Hépatalgie d’effort', 'Foie congestif', 'Congestion droite'],
   ]), 25))
ADD(8, 'Critères diagnostiques',
 P('Le diagnostic exige des symptômes ou des signes et une preuve objective d’anomalie cardiaque. Un œdème seul ne suffit pas.', 25) +
 F('Critères (ESC 2021)',
   TAB(['Critère', 'Seuil'], [
    ['NT-proBNP ambulatoire', '≥ 125 ng/L : échocardiographie ; < 125 ng/L : IC improbable'],
    ['NT-proBNP en contexte aigu', '< 300 ng/L (= pg/mL) : IC aiguë improbable, valeur prédictive négative ≈ 98–99 %'],
    ['NT-proBNP aigu, seuils d’inclusion selon l’âge', '> 450 ng/L avant 50 ans, > 900 de 50 à 75 ans, > 1800 après 75 ans'],
    ['ICFEr', 'FEVG ≤ 40 %'],
    ['ICFEm', 'FEVG 41–49 %'],
    ['ICFEp', 'FEVG ≥ 50 % avec anomalie structurelle ou de remplissage et peptides élevés'],
   ]) + P('La Société suisse de cardiologie applique les recommandations de l’ESC.', 25)))
ADD(9, 'Examens complémentaires',
 H4('9.a Examen de référence') +
 P('L’examen de référence est l’échocardiographie transthoracique, après un NT-proBNP. '
   'Au seuil de 125 ng/L, le NT-proBNP a une sensibilité élevée et une valeur prédictive négative de 94–98 % ; sa spécificité est faible (âge, fibrillation atriale, insuffisance rénale).', 25) +
 H4('9.b Examens de première et de deuxième intention') +
 P('En première intention, on fait ECG, NT-proBNP et biologie. En deuxième intention, on fait l’échocardiographie, puis les examens de la cause.', 25) +
 TAB(['Intention', 'Examen', 'Pourquoi'], [
  ['1re', 'ECG', 'Un ECG normal rend l’IC improbable'],
  ['1re', 'NT-proBNP', 'Exclure ou orienter'],
  ['1re', 'Hémogramme, ferritine, saturation de la transferrine', 'Anémie et carence en fer'],
  ['1re', 'Créatinine, DFGe, potassium, sodium, TSH', 'Bilan avant traitement et cause'],
  ['1re', 'Radiographie du thorax', 'Congestion, autre cause de dyspnée'],
  ['2e', 'Échocardiographie', 'FEVG, valves, pressions'],
  ['2e', 'Coronarographie ou scanner coronaire', 'Cause ischémique'],
  ['2e', 'IRM cardiaque', 'Mauvaise fenêtre d’échographie, myocardite, amylose'],
 ]) +
 H4('9.c Prescription et formules') +
 P('Indication : fatigue et dyspnée d’effort, œdèmes, cardiopathie connue. Moment : à distance d’un effort intense ; l’échocardiographie dans les semaines qui suivent un NT-proBNP élevé. '
   'Préparation : aucune ; noter les médicaments et le rythme cardiaque.', 25) +
 TAB(['Grandeur', 'Formule', 'Repère'], [['FEVG', '(VTD − VTS) / VTD × 100', 'Normale ≈ 52–72 % (homme), 54–74 % (femme)'], ['Saturation de la transferrine', 'Fer / capacité de fixation × 100', '< 20 % : carence']]) +
 H4('9.d Interprétation : positif, négatif, limite, discordant') +
 TAB(['Situation', 'Interprétation', 'Conduite'], [
  ['Positif : NT-proBNP ≥ 125 ng/L', 'IC possible', 'Échocardiographie'],
  ['Négatif : NT-proBNP < 125 ng/L, ECG normal', 'IC improbable', 'Autre cause de fatigue'],
  ['Limite : NT-proBNP élevé chez un insuffisant rénal âgé', 'Spécificité réduite', 'Échocardiographie quand même'],
  ['Discordant : NT-proBNP bas chez un obèse symptomatique', 'L’obésité abaisse les peptides', 'Échocardiographie si suspicion forte'],
 ]) +
 H4('9.e Alternatives') +
 P('Grossesse : échocardiographie sans risque ; penser à la cardiomyopathie du péripartum. Enfant : avis cardiopédiatrique. '
   'DFGe < 30 : coronarographie avec prudence pour l’iode. L’IRM cardiaque est possible avec la plupart des pacemakers récents, selon le modèle.', 25))
ADD(10, 'Arbre décisionnel',
 P('Si le NT-proBNP est < 125 ng/L, alors l’IC est improbable. S’il est plus élevé, alors l’échocardiographie classe la maladie.', 25) +
 F('Arbre décisionnel : fatigue et dyspnée d’effort',
   OL(['Signes de gravité : urgence, 144.',
       'ECG et NT-proBNP.',
       'NT-proBNP < 125 ng/L et ECG normal : chercher une autre cause.',
       'NT-proBNP ≥ 125 ng/L : échocardiographie.',
       'FEVG ≤ 40 % : quadrithérapie ; chercher une cause ischémique.',
       'FEVG 41–49 % ou ≥ 50 % : gliflozine, diurétique si congestion, traitement des comorbidités.',
       'Carence en fer : fer IV selon les critères ci-dessous.']), 25, 26))
ADD(11, 'Prise en charge',
 H4('11.A Buts : d’abord l’urgence (œdème pulmonaire, choc), car elle peut tuer en quelques heures') +
 P('Le traitement réduit la mortalité et les hospitalisations, améliore la capacité d’effort et supprime la congestion.', 25) +
 TAB(['But', 'Cible chiffrée'], [['Fréquence cardiaque (rythme sinusal)', '< 70/min'], ['Poids', 'Stable, sans prise > 2 kg en 3 jours'], ['Doses', 'Doses cibles des quatre médicaments en quelques semaines']]) +
 H4('11.B Moyens et méthodes : forme compliquée en urgence, puis forme non compliquée en ambulatoire') +
 P('La forme compliquée (œdème pulmonaire, choc cardiogénique) se traite en urgence à l’hôpital : oxygène, diurétique IV, ventilation non invasive dans la première heure. '
   'La forme non compliquée se traite en ambulatoire, avec des mesures générales : pesée quotidienne, sel < 5 g/j, vaccins contre la grippe et le pneumocoque, et une éducation du patient.', 25) +
 P('Moyens non médicamenteux : réadaptation cardiaque supervisée ; défibrillateur implantable si FEVG ≤ 35 % après 3 mois de traitement optimal ; resynchronisation si bloc de branche gauche large.', 25) +
 FICHE([
  ['ARNI : sacubitril/valsartan (Entresto®)', 'Bloque le récepteur de l’angiotensine et la néprilysine', 'Demi-vies ≈ 1–10 h', 'Départ 24/26 ou 49/51 mg 2×/j, cible 97/103 mg 2×/j', 'Hypotension, hyperkaliémie, angio-œdème', 'Angio-œdème, IEC dans les 36 h', 'IEC, ARM, potassium'],
  ['Bêtabloquant : bisoprolol (Concor®)', 'Bloque les récepteurs β1', 'Demi-vie ≈ 10–12 h', '1,25 mg/j, paliers toutes les 2 semaines jusqu’à 10 mg/j', 'Bradycardie, fatigue initiale', 'Bloc atrio-ventriculaire de haut degré, IC aiguë congestive', 'Vérapamil, diltiazem'],
  ['ARM : spironolactone (Aldactone®)', 'Antagoniste de l’aldostérone', 'Métabolites actifs, longue demi-vie', '25–50 mg/j', 'Hyperkaliémie, gynécomastie', 'K⁺ > 5,0 mmol/L, DFGe < 30', 'IEC, ARNI, AINS'],
  ['Gliflozine : dapagliflozine (Forxiga®), empagliflozine (Jardiance®)', 'Inhibe le cotransporteur SGLT2 du rein', 'Demi-vie ≈ 12 h', '10 mg 1×/j, durée illimitée', 'Infection génitale, acidocétose rare', 'Diabète de type 1, DFGe très bas', 'Diurétiques (déshydratation)'],
  ['Diurétique de l’anse : torasémide (Torem®)', 'Bloque le cotransporteur Na-K-2Cl de l’anse', 'Demi-vie ≈ 3–4 h', '10–40 mg/j, dose minimale efficace', 'Hypokaliémie, insuffisance rénale', 'Anurie', 'AINS, lithium'],
 ], 25, 26) +
 P('Fer IV (Ferinject®) : l’ESC 2023 le propose si ferritine < 100 µg/L ou 100–299 µg/L avec saturation < 20 %, pour réduire les symptômes et les hospitalisations. '
   'L’essai HEART-FID (2023) n’a pas montré de bénéfice net sur son critère principal ; l’essai AFFIRM-AHF a réduit les réhospitalisations après une décompensation.', 26, 52, 53) +
 F('Situations particulières',
   TAB(['Situation', 'Particularité'], [
    ['Grossesse', 'ARNI, IEC, ARM et gliflozines contre-indiqués ; avis cardiologique'],
    ['Personne âgée', 'Titration lente, hypotension orthostatique et chutes'],
    ['Enfant', 'Cardiopathie congénitale ou myocardite : avis spécialisé'],
    ['Insuffisance hépatique', 'Prudence avec ARNI et bêtabloquants'],
    ['Insuffisance rénale (DFGe bas)', 'Hausse de créatinine ≤ 30 % tolérée ; ARM évité si DFGe < 30'],
    ['Hyperkaliémie', 'K⁺ > 5,5 : réduire l’ARM ; K⁺ > 6,0 : l’arrêter'],
   ]), 25) +
 SOCIAL('Un arrêt de travail est fréquent après une décompensation ; un poste adapté est souvent possible en classe NYHA I–II.',
        'L’insuffisance cardiaque stable n’interdit pas la conduite ; une syncope, une classe NYHA IV ou un défibrillateur récemment posé l’interdisent temporairement.') +
 H4('11.C Surveillance et critères de sortie') +
 TAB(['Quand', 'Quoi'], [
  ['Chaque jour', 'Poids : appeler si + 2 kg en 3 jours'],
  ['1–2 semaines après chaque palier', 'Créatinine, DFGe, potassium'],
  ['Après 3–6 mois de doses cibles', 'Échocardiographie : FEVG et indication au défibrillateur'],
  ['Arrêt d’un médicament', 'ARM si K⁺ > 6,0 ; bêtabloquant réduit (pas arrêté) si décompensation modérée'],
  ['Critères de sortie d’hospitalisation', 'Euvolémie, diurétique oral stable 24 h, créatinine stable, rendez-vous dans les 1–2 semaines'],
 ]) + P('La surveillance rapprochée après la sortie réduit les réhospitalisations précoces.', 25) +
 H4('11.D Pronostic et recherche 2026') +
 P('Le pronostic reste sévère ; il s’améliore avec la quadrithérapie, la réadaptation et le défibrillateur chez les patients choisis.', 25) +
 P('Le vériciguat est utilisé après une décompensation chez certains patients ICFEr. L’omecamtiv mécarbil, cité par l’original, n’est pas autorisé : il reste un médicament de recherche.', 25, 40))
ADD(12, 'Prévention',
 P('La prévention traite l’hypertension, le diabète, les lipides et le tabac, et revascularise vite les syndromes coronariens.', 25) +
 F('Prévention primaire, secondaire et tertiaire',
   TAB(['Niveau', 'Mesure'], [
    ['Primaire', 'Pression artérielle, statines si indiquées, arrêt du tabac, gliflozine chez le diabétique à risque'],
    ['Secondaire', 'NT-proBNP et ECG chez le patient à risque essoufflé'],
    ['Tertiaire', 'Quadrithérapie, réadaptation, éducation, vaccins'],
   ]) + P('En Suisse, la Société suisse de cardiologie applique les recommandations de l’ESC ; la réadaptation cardiaque ambulatoire est remboursée sur prescription.', 25, 16)))
ADD(13, 'Points clés',
 P('Un NT-proBNP < 125 ng/L rend l’insuffisance cardiaque improbable en ambulatoire. '
   'L’échocardiographie classe la maladie selon la FEVG. '
   'L’ICFEr se traite par quatre médicaments introduits vite. '
   'Les AINS sont à éviter, car ils retiennent le sel et abîment le rein.', 25))
ADD(14, 'Pièges d’examen',
 TAB(['Piège', 'Ce qu’il faut répondre'], [
  ['Introduire un bêtabloquant en pleine décompensation congestive', 'Non : stabiliser d’abord, puis l’introduire'],
  ['Prescrire un AINS sous IEC et diurétique', 'Non : risque d’insuffisance rénale aiguë et de décompensation'],
  ['Dire que le B3 est pathognomonique', 'Non : il est spécifique mais peu sensible'],
  ['Utiliser CHAMPIT pour la cause de l’IC chronique', 'Non : il liste les facteurs de décompensation'],
  ['Associer IEC et ARNI', 'Non : délai de 36 h obligatoire'],
  ['Arrêter l’ARM pour un potassium à 5,3 mmol/L', 'Non : surveiller ; réduire au-delà de 5,5'],
 ]) + P('Ces pièges reprennent les recommandations de l’ESC.', 25))
CTX = {'_prefixe': 'Dans l’insuffisance cardiaque',
 'bnp': 'Un NT-proBNP < 125 ng/L rend l’IC improbable ; au-delà, une échocardiographie est nécessaire.',
 'echocoeur': 'La FEVG classe l’IC : ≤ 40 % réduite, 41–49 % légèrement réduite, ≥ 50 % préservée.',
 'ecg': 'Un ECG normal rend l’IC improbable ; une fibrillation atriale est une cause et un facteur de décompensation.',
 'radio': 'Elle montre une congestion ou une autre cause de dyspnée.',
 'nfs': 'Une anémie aggrave la fatigue et la dyspnée.',
 'ferritine': 'Une ferritine < 100 µg/L définit une carence en fer selon l’ESC.',
 'tsat': 'Une TSAT < 20 % avec ferritine 100–299 µg/L définit aussi une carence en fer.',
 'creat': 'Une hausse de créatinine ≤ 30 % est tolérée sous IEC ou ARNI.',
 'iono': 'Un K⁺ > 5,5 mmol/L impose de réduire l’ARM.',
 'irmcard': 'Elle précise la cause : cicatrice, myocardite, amylose.',
 'coro': 'Elle cherche une cause ischémique revascularisable.',
 'tsh': 'Une dysthyroïdie peut causer ou aggraver l’IC.',
 'cpet': 'Une VO₂ pic < 14 mL/kg/min signe une IC avancée.'}
if __name__ == '__main__':
    produire(M, PTS, SOURCES, CTX)
