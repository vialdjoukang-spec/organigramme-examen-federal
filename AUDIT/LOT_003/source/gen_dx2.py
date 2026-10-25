# -*- coding: utf-8 -*-
"""DX.2 — Déshydratation intracellulaire hypernatrémique. LOT 3, V5 → V7 AUDITÉ."""
from lot3_commun import *
POINT = mkPOINT('dx2')
M = META('dx2', 'DX.2', 'Déshydratation hypernatrémique', 'Déshydratation intracellulaire hypernatrémique',
         'LOT_003_DX2_Deshydratation_hypernatremique_AUDITÉ.html',
         'Corrections majeures : chiffres non sourcés de l’original (15 % des soifs pathologiques, 1–3 % des personnes âgées hospitalisées, mortalité de 40 % « SSMIG ») remplacés par des données suisses et européennes publiées ; conduite en cas de correction trop rapide reformulée.')
ECT = T('eau corporelle totale', 'L’eau corporelle totale représente environ 60 % du poids chez l’homme jeune, 50 % chez la femme jeune et l’homme âgé, 45 % chez la femme âgée ; deux tiers sont dans les cellules.')
OSMI = T('osmoles idiogéniques', 'Les osmoles idiogéniques (myo-inositol, taurine, glutamine, bétaïne) sont des petites molécules que les neurones accumulent en 24–48 h pour retenir leur eau face à un plasma concentré.')
PTS = []
PTS.append(POINT(1, 'Définition et sémantique',
 P('La déshydratation intracellulaire est la perte d’eau des cellules provoquée par un plasma trop concentré. '
   'Elle se traduit par une hypernatrémie (natrémie > 145 mmol/L) et une hyperosmolalité plasmatique efficace. '
   'Elle signe toujours un manque d’eau libre par rapport au sodium de l’organisme.', 32, 33) +
 F('Terminologie',
   TAB(['Terme', 'Définition exacte', 'À ne pas confondre avec'], [
    ['Déshydratation intracellulaire', 'Diminution du volume des cellules par hypertonie plasmatique', 'Déshydratation extracellulaire (perte de sel et d’eau, hypovolémie)'],
    ['Hypernatrémie', 'Natrémie > 145 mmol/L ; sévère si > 155–160 mmol/L selon les auteurs', 'Excès de sodium total : il peut être bas, normal ou haut'],
    ['Eau libre', 'Eau sans soluté, celle qui modifie la natrémie', 'Volume perfusé total'],
    ['Hypernatrémie aiguë', 'Installée en < 48 h', 'Chronique (> 48 h ou durée inconnue)'],
    ['Hypodipsie', 'Soif diminuée ou absente malgré l’hyperosmolalité', 'Accès à l’eau impossible'],
   ]) + P('Le sodium mesuré reflète le rapport sodium/eau, pas la quantité de sodium. On parle donc le plus souvent de déficit en eau, et non d’excès de sel.', 32))))
PTS.append(POINT(2, 'Épidémiologie (Suisse, puis Europe)',
 P('Aux urgences de l’Hôpital de l’Île à Berne, une natrémie > 145 mmol/L touche 2 % des patients testés. '
   'Dans une réanimation médicale européenne (Vienne), une natrémie > 149 mmol/L touche 9 % des patients, le plus souvent pendant le séjour. '
   'La mortalité y atteint 39–43 %, contre 24 % sans hypernatrémie.', 34, 66) +
 F('Chiffres, terrain et histoire naturelle',
   TAB(['Donnée', 'Valeur', 'Portée'], [
    ['Hypernatrémie > 145 mmol/L aux urgences (Berne, 2008–2011)', '2 % des 43 911 patients avec natrémie mesurée', 'Donnée suisse monocentrique'],
    ['Hypernatrémie sévère > 149 mmol/L aux urgences (Berne)', '74 patients (≈ 0,2 %) ; 38 % avec symptômes neurologiques', 'Sujets âgés surtout'],
    ['Décès hospitaliers en cas d’hypernatrémie sévère (Berne)', '21 décès sur 74 (≈ 28 %)', 'Mortalité associée, non causale'],
    ['Hypernatrémie en réanimation médicale (Vienne)', '9 % (2 % à l’admission, 7 % acquise)', 'Composante iatrogène fréquente'],
    ['Mortalité à 28 jours en réanimation', '39–43 % contre 24 % ; risque relatif ajusté ≈ 2,1', 'Facteur de risque indépendant'],
    ['Terrain', 'Grand âge, démence, dépendance, nourrisson, patient intubé', 'Accès à l’eau ou soif défaillants'],
   ]) + P('Les chiffres non sourcés de l’original (15 % des soifs pathologiques, 1–3 % des personnes âgées hospitalisées, 40 % de mortalité attribuée à la Société suisse de médecine interne générale [SSMIG]) ont été remplacés.', 34, 66))))
PTS.append(POINT(3, 'Physiopathologie',
 P('Une perte d’eau libre (fièvre, polypnée, diarrhée osmotique, diurèse osmotique ou aqueuse) concentre le sodium extracellulaire. '
   'Par osmose, l’eau sort des cellules, qui contiennent deux tiers de l’' + ECT + ' ; les neurones se rétractent. '
   'La soif et la vasopressine corrigent normalement ce déséquilibre : l’hypernatrémie ne persiste donc que si la soif ou l’accès à l’eau manquent.', 32, 64) +
 F('Chaîne logique : de l’anatomie au traitement',
   TAB(['Étape', 'Ce qu’il faut comprendre'], [
    ['Anatomie', 'Les osmorécepteurs de l’hypothalamus antérieur (organe vasculaire de la lame terminale) captent la tonicité ; l’hypophyse postérieure libère la vasopressine ; le tube collecteur réabsorbe l’eau.'],
    ['Physiologie', 'Pourquoi on a soif : une hausse de 1–2 % de l’osmolalité déclenche la soif et la vasopressine, qui ramènent la natrémie vers 140 mmol/L.'],
    ['Physiopathologie', 'Si la personne ne peut pas boire, l’eau quitte les cellules ; en 24–48 h, les neurones fabriquent des ' + OSMI + ' pour se protéger.'],
    ['Clinique', 'D’où la soif, puis la somnolence, la confusion et les convulsions quand la rétraction cérébrale s’aggrave.'],
    ['Examens', 'On mesure la natrémie et l’osmolalité, puis l’osmolalité urinaire, qui dit si le rein économise l’eau.'],
    ['Traitement', 'On rend de l’eau libre lentement, car les osmoles idiogéniques attireraient l’eau trop vite dans les neurones (œdème cérébral).'],
   ]), 32, 33) +
 F('Mécanisme, exploration et cible thérapeutique',
   TAB(['Mécanisme', 'Exploration', 'Cible thérapeutique'], [
    ['Pertes extrarénales (sueur, fièvre, diarrhée)', 'Osmolalité urinaire > 600 mOsm/kg, natriurèse basse', 'Eau libre, traitement de la fièvre et de la diarrhée'],
    ['Diurèse osmotique (glucose, urée, mannitol)', 'Urines iso-osmotiques (300–600 mOsm/kg)', 'Équilibre glycémique, arrêt du mannitol'],
    ['Diurèse aqueuse (déficit ou résistance à la vasopressine)', 'Osmolalité urinaire < 300 mOsm/kg', 'Desmopressine (déficit) ou traitement de la cause (résistance)'],
    ['Apport excessif de sodium (bicarbonate, NaCl hypertonique)', 'Natriurèse élevée, bilan entrées-sorties', 'Arrêt de l’apport, diurétique et eau'],
    ['Soif défaillante (grand âge, démence, lésion hypothalamique)', 'Absence de soif malgré Na > 150 mmol/L', 'Hydratation programmée'],
   ]) + P('La rétraction cérébrale explique les symptômes neurologiques ; elle peut étirer les veines pontiques et provoquer un hématome sous-dural ou une hémorragie sous-arachnoïdienne.', 32))))
PTS.append(POINT(4, 'Raisonnement clinique et diagnostic différentiel',
 P('Le médecin vérifie d’abord l’urgence : choc, coma ou convulsions imposent la réanimation. '
   'Il classe ensuite l’état du volume extracellulaire : hypovolémie (perte d’eau plus que de sel), euvolémie (perte d’eau pure) ou hypervolémie (apport de sodium). '
   'Puis l’osmolalité urinaire sépare les pertes extrarénales, osmotiques et aqueuses.', 32, 33) +
 DIFF('hyperna') +
 F('Diagnostic différentiel : causes de l’hypernatrémie acquise en réanimation (fréquences en exposant rouge, même unité)',
   TAB(['Cause et fréquence', 'Éléments d’orientation', 'Examen discriminant'], [
    ['Fièvre (pertes insensibles)' + PR('45 % des cas', 67), 'Température, sueurs, polypnée', 'Bilan hydrique'],
    ['Polyurie (osmotique ou aqueuse)' + PR('38 % des cas', 67), 'Diurèse > 3 L/24 h', 'Osmolalité urinaire'],
    ['Insuffisance rénale aiguë' + PR('35 % des cas', 67), 'Créatinine en hausse', 'Créatinine, urée'],
    ['Solutés hypertoniques administrés' + PR('27 % des cas', 67), 'Bicarbonate, NaCl hypertonique, antibiotiques sodés', 'Bilan des apports de sodium'],
    ['Diarrhée' + PR('18 % des cas', 67), 'Selles liquides, alimentation entérale', 'Bilan des pertes'],
   ]) + P('Ces fréquences proviennent de 45 patients d’une réanimation médicale ; plusieurs causes coexistent souvent, d’où une somme > 100 %.', 67))))
PTS.append(POINT(5, 'Anamnèse ciblée et drapeaux rouges',
 P('L’anamnèse, souvent obtenue auprès de l’entourage ou de l’établissement médico-social (EMS), cherche ce qui a empêché de boire et ce qui a fait perdre de l’eau. '
   'Elle reconstitue les apports, les pertes et les médicaments des derniers jours.', 32, 34) +
 U('Drapeaux rouges : somnolence ou confusion, convulsions, coma, natrémie > 160 mmol/L, signes de choc, céphalée brutale (hémorragie). Ils imposent une hospitalisation immédiate, souvent en soins intermédiaires.', 32, 34) +
 F('Questions ciblées et leur raison',
   TAB(['Question', 'Pourquoi la poser'], [
    ['La personne peut-elle se servir à boire seule ? A-t-elle soif ?', 'Dépendance et hypodipsie expliquent la plupart des hypernatrémies du sujet âgé.'],
    ['Y a-t-il eu de la fièvre, une canicule, des diarrhées, des vomissements ?', 'Ce sont les pertes d’eau les plus fréquentes.'],
    ['Quels médicaments : diurétique de l’anse (furosémide Lasix®), lactulose, lithium ?', 'Ils augmentent les pertes d’eau ou bloquent la concentration urinaire.'],
    ['Urine-t-elle beaucoup, même la nuit ?', 'Une polyurie oriente vers une diurèse osmotique ou aqueuse.'],
    ['A-t-on perfusé du bicarbonate ou du sel ?', 'Hypernatrémie par apport de sodium, souvent hospitalière.'],
    ['Depuis quand est-elle confuse ?', 'La durée (< ou > 48 h) fixe la vitesse de correction.'],
   ]), 32, 67)))
PTS.append(POINT(6, 'Examen clinique',
 P('L’examen estime le volume extracellulaire et cherche les signes neurologiques. '
   'À l’état normal, l’adulte a des muqueuses humides, un pouls < 100/min et une pression stable en position debout. '
   'La sécheresse buccale a une sensibilité et une spécificité faibles chez la personne âgée, qui respire souvent bouche ouverte.', 32) +
 F('Signes, technique et valeur',
   TAB(['Signe', 'Technique', 'Ce qu’il signifie'], [
    ['Poids', 'Peser sur la même balance que la dernière mesure', 'La perte aiguë de poids estime la perte d’eau (1 kg ≈ 1 L)'],
    ['Sécheresse de la face inférieure de la langue et du sillon gingivo-jugal', 'Inspecter avec une lampe', 'Déshydratation intracellulaire ; peu spécifique'],
    ['Hypotension orthostatique', 'Pression couché puis après 1 et 3 minutes debout', 'Hypovolémie associée'],
    ['Veines jugulaires plates', 'Patient à 45°', 'Hypovolémie'],
    ['Œdèmes', 'Pression sur la face antérieure du tibia', 'Hypernatrémie par surcharge sodée'],
    ['Vigilance, orientation, signes focaux', 'Score de Glasgow, examen neurologique', 'Gravité ; un signe focal fait chercher un hématome'],
   ]), 32)))
PTS.append(POINT(7, 'Syndromes et signes cliniques',
 P('Le syndrome de déshydratation intracellulaire associe soif, sécheresse des muqueuses, perte de poids et troubles de la vigilance. '
   'La déshydratation globale y ajoute l’hypovolémie : hypotension, tachycardie, oligurie. '
   'Les symptômes dépendent du niveau de natrémie et de la vitesse d’installation.', 32, 34) +
 F('Signes fonctionnels (symptômes rapportés)', UL(['Soif intense (souvent absente chez la personne âgée)', 'Faiblesse, irritabilité', 'Somnolence et désorientation (premiers symptômes à Berne)', 'Céphalées', 'Nausées']), 34) +
 F('Signes physiques (constatés à l’examen)', UL(['Muqueuses sèches, perte de poids', 'Fièvre fréquente (cause ou conséquence)', 'Hypotension et tachycardie si hypovolémie', 'Hyperréflexie, myoclonies, convulsions', 'Coma dans les formes sévères']), 32) +
 F('Syndrome de déshydratation intracellulaire pure',
   TAB(['Signe', 'Mécanisme', 'Valeur'], [
    ['Soif', 'Stimulation des osmorécepteurs', 'Absente si hypodipsie'],
    ['Troubles de la vigilance', 'Rétraction neuronale', 'Corrélés au niveau de natrémie'],
    ['Diurèse faible et concentrée', 'Vasopressine maximale', 'Absente si cause rénale'],
   ]), 32) +
 F('Syndrome de déshydratation globale',
   TAB(['Signe', 'Mécanisme', 'Valeur'], [
    ['Hypotension, tachycardie', 'Perte de sodium et d’eau', 'Impose de restaurer le volume d’abord'],
    ['Pli cutané', 'Perte de liquide interstitiel', 'Peu fiable chez la personne âgée'],
    ['Oligurie, natriurèse < 20 mmol/L', 'Rétention rénale du sodium', 'Perte extrarénale'],
   ]), 32) +
 F('Syndrome d’hypernatrémie par surcharge sodée',
   TAB(['Signe', 'Mécanisme', 'Valeur'], [
    ['Œdèmes, prise de poids', 'Excès de sodium et d’eau', 'Contexte hospitalier'],
    ['Natriurèse élevée', 'Le rein élimine l’excès de sel', 'Confirme l’apport'],
   ]), 32)))
PTS.append(POINT(8, 'Critères diagnostiques',
 P('Le diagnostic biologique repose sur une natrémie > 145 mmol/L, qui implique une osmolalité plasmatique efficace > 295 mOsm/kg. '
   'Ce critère fait consensus dans les revues de référence de 2000 et de 2015, mais aucune société savante n’a publié de critères plus détaillés. '
   'La classification par volume et par osmolalité urinaire sert ensuite à trouver la cause. '
   'La clinique seule ne suffit pas : seul l’ionogramme pose le diagnostic.', 32, 33) +
 F('Gravité de l’hypernatrémie (repères usuels)',
   TAB(['Natrémie (mmol/L)', 'Repère', 'Conduite'], [
    ['146–150', 'Légère', 'Eau orale, cause à traiter'],
    ['151–160', 'Modérée', 'Hospitalisation souvent nécessaire'],
    ['> 160', 'Sévère', 'Surveillance rapprochée, voie IV'],
   ]) + P('Ces bornes sont des repères d’enseignement ; elles ne proviennent pas d’un consensus publié.', 32))))
PTS.append(POINT(9, 'Examens complémentaires',
 H4('9.a Examen de référence') +
 P('L’ionogramme sanguin avec osmolalité plasmatique est l’examen de référence ; l’osmolalité urinaire donne le mécanisme. '
   'Sensibilité et spécificité ne s’appliquent pas : la natrémie définit la maladie.', 32) +
 H4('9.b Examens de première et de deuxième intention') +
 P('En première intention : ionogramme sanguin, osmolalités plasmatique et urinaire, créatinine, urée, glycémie et calcémie. '
   'En deuxième intention : scanner cérébral si un signe focal ou un coma persiste ; copeptine et avis endocrinologique si l’osmolalité urinaire reste < 300 mOsm/kg.', 32, 3) +
 TAB(['Intention', 'Examen', 'Pourquoi'], [
  ['1re', 'Ionogramme sanguin (sodium, potassium, chlore)', 'Diagnostic et suivi toutes les 2–6 heures'],
  ['1re', 'Osmolalité urinaire', 'Sépare pertes extrarénales, diurèse osmotique et diurèse aqueuse'],
  ['1re', 'Créatinine et urée', 'Insuffisance rénale fonctionnelle (urée élevée)'],
  ['1re', 'Glycémie', 'Diurèse osmotique par hyperglycémie'],
  ['1re', 'Ionogramme urinaire (sodium)', 'Natriurèse < 20 mmol/L : perte extrarénale ; élevée : apport de sel ou diurétique'],
  ['2e', 'Scanner cérébral sans injection', 'Hématome sous-dural en cas de signe focal'],
  ['2e', 'Copeptine', 'Déficit ou résistance à la vasopressine si urines diluées'],
 ]) +
 H4('9.c Prescription et calculs') +
 P('Indication : toute confusion du sujet âgé, toute fièvre prolongée chez une personne dépendante. Moment : à l’arrivée, puis à 2, 4 et 6 heures pendant la correction. '
   'Préparation : aucune ; l’échantillon urinaire se prélève avant toute perfusion.', 32) +
 F('Déficit en eau libre et formule d’Adrogué-Madias',
   TAB(['Calcul', 'Formule', 'Exemple : homme âgé de 70 kg, Na⁺ 160 mmol/L'], [
    ['Eau corporelle totale', '0,6 × poids (homme jeune) ; 0,5 (femme jeune, homme âgé) ; 0,45 (femme âgée)', '0,5 × 70 = 35 L'],
    ['Déficit en eau libre', 'Eau corporelle × (Na⁺ / 140 − 1)', '35 × (160/140 − 1) ≈ 5 L, plus ≈ 1 L de pertes insensibles par jour'],
    ['Variation de natrémie par litre perfusé', '(Na⁺ + K⁺ du soluté − Na⁺ du patient) / (eau corporelle + 1)', 'Effet chiffré par soluté ci-dessous'],
   ]) +
   TAB(['Soluté', 'Sodium du soluté', 'Effet attendu par litre (patient de l’exemple)', 'Indication'], [
    ['Eau orale ou par sonde, glucose 5 % IV', '0 mmol/L', '≈ −4,4 mmol/L', 'Déshydratation intracellulaire sans choc'],
    ['NaCl 0,45 %', '77 mmol/L', '≈ −2,3 mmol/L', 'Déshydratation mixte modérée'],
    ['NaCl 0,9 %', '154 mmol/L', '≈ −0,2 mmol/L', 'Seulement en cas de choc, avant de passer à l’eau libre'],
   ]) + P('La formule suppose qu’il n’y a pas d’autres pertes ; on la recalcule après chaque ionogramme.', 32)) +
 H4('9.d Interprétation : positif, négatif, limite, discordant') +
 TAB(['Situation', 'Interprétation', 'Conduite'], [
  ['Positif : Na⁺ > 145 et osmolalité urinaire > 600 mOsm/kg', 'Le rein économise l’eau : perte extrarénale ou apport insuffisant', 'Eau libre'],
  ['Négatif : Na⁺ 135–145 mmol/L', 'Pas d’hypernatrémie', 'Chercher une autre cause de confusion'],
  ['Limite : osmolalité urinaire 300–600 mOsm/kg', 'Diurèse osmotique ou déficit partiel en vasopressine', 'Glycémie, urée ; copeptine'],
  ['Discordant : Na⁺ élevé et urines < 300 mOsm/kg', 'Le rein perd de l’eau malgré l’hyperosmolalité', 'Déficit ou résistance à la vasopressine : test à la desmopressine'],
 ]) +
 H4('9.e Alternatives') +
 P('Grossesse : mêmes examens. Enfant et nourrisson : volumes adaptés au poids et avis pédiatrique. '
   'DFGe < 30 : le calcul reste valable, mais les apports se réévaluent plus souvent. Le scanner se fait sans produit iodé ; l’IRM sert si le scanner est normal et le déficit persiste.', 32)))
PTS.append(POINT(10, 'Arbre décisionnel',
 P('Si le patient est en choc, on restaure d’abord la pression avec du NaCl 0,9 %. Ensuite, on passe à l’eau libre, par la bouche ou par sonde si possible, sinon en glucose 5 % IV.', 32, 33) +
 F('Arbre décisionnel : natrémie > 145 mmol/L',
   OL(['Choc, coma ou convulsions : réanimation ; NaCl 0,9 % jusqu’à stabilisation de la pression.',
       'Évaluer le volume : hypovolémie → eau et sel ; euvolémie → eau ; hypervolémie → arrêt du sel, diurétique de l’anse et eau.',
       'Osmolalité urinaire > 600 mOsm/kg : perte extrarénale ou apport insuffisant → eau libre et cause.',
       'Osmolalité urinaire 300–600 : diurèse osmotique → glycémie, urée, mannitol.',
       'Osmolalité urinaire < 300 : déficit ou résistance à la vasopressine → test à la desmopressine, avis endocrinologique.',
       'Durée > 48 h ou inconnue : baisse ≤ 10 mmol/L par 24 h ; < 48 h : correction plus rapide possible.']), 32, 3)))
PTS.append(POINT(11, 'Prise en charge',
 H4('11.A Buts : d’abord l’urgence (choc, convulsions), car elle menace la vie avant l’hypernatrémie elle-même') +
 P('Le traitement rend l’eau libre manquante, corrige le volume et traite la cause, sans provoquer d’œdème cérébral.', 32) +
 TAB(['But', 'Cible chiffrée'], [
  ['Vitesse de baisse (hypernatrémie chronique)', '≤ 0,5 mmol/L par heure, ≤ 10 mmol/L par 24 h (recommandation classique)'],
  ['Hypernatrémie aiguë (< 48 h)', 'Correction possible de ≈ 1 mmol/L par heure'],
  ['Natrémie finale', '≈ 140 mmol/L en 48–72 h'],
 ]) + P('Chez l’adulte en réanimation, une correction plus rapide n’a pas été associée à plus de décès ni d’œdèmes cérébraux dans une étude rétrospective ; la règle prudente reste celle de 10 mmol/L par 24 h.', 32, 65) +
 H4('11.B Moyens et méthodes : forme compliquée en urgence, forme non compliquée en ambulatoire ou en EMS') +
 P('Les mesures générales passent avant les perfusions : eau plate par la bouche ou par sonde nasogastrique, arrêt des médicaments en cause, traitement de la fièvre et éducation de l’entourage.', 32) +
 F('Solutés et leur usage',
   TAB(['Situation', 'Soluté', 'Débit indicatif', 'Pourquoi'], [
    ['Choc hypovolémique', 'NaCl 0,9 %', '500–1000 mL en 30–60 min, à répéter selon la pression', 'Le volume prime sur la natrémie'],
    ['Déshydratation intracellulaire pure', 'Eau orale ou glucose 5 % IV', 'Débit calculé par la formule d’Adrogué-Madias', 'Apporte de l’eau libre'],
    ['Déshydratation mixte', 'NaCl 0,45 %', 'Selon la formule', 'Apporte eau et sel'],
    ['Surcharge sodée', 'Furosémide (Lasix®) + glucose 5 %', 'Dose selon la fonction rénale', 'Élimine le sodium et rend l’eau'],
    ['Déficit en vasopressine', 'Desmopressine (Minirin®)', 'Voir DX.9', 'Arrête la fuite d’eau rénale'],
   ]) + P('Un débit élevé de glucose 5 % peut provoquer une hyperglycémie, puis une diurèse osmotique qui aggrave la déshydratation ; on surveille la glycémie.', 32, 55)) +
 FICHE([
  ['Glucose 5 % (soluté d’eau libre)', 'Le glucose est métabolisé ; il reste de l’eau libre', 'Captation cellulaire par l’insuline', 'Débit selon le déficit, sur 48–72 h', 'Hyperglycémie, hypokaliémie, œdème cérébral si trop rapide', 'Hyperglycémie non contrôlée', 'Insuline (à adapter)'],
  ['Diurétique de l’anse : furosémide (Lasix®)', 'Bloque le cotransporteur Na-K-2Cl de l’anse de Henle', 'Demi-vie ≈ 1–2 h ; élimination rénale', '20–40 mg IV, à répéter selon la diurèse', 'Hypokaliémie, hypovolémie, ototoxicité', 'Hypovolémie, anurie', 'Aminosides (ototoxicité), lithium (lithémie accrue)'],
 ], 32) +
 F('Situations particulières',
   TAB(['Situation', 'Particularité'], [
    ['Enfant et nourrisson', 'Œdème cérébral plus fréquent : correction lente, avis pédiatrique'],
    ['Personne âgée', 'Hypodipsie : hydratation programmée et surveillance du poids'],
    ['Grossesse', 'Mêmes principes ; surveiller la glycémie sous glucose'],
    ['Insuffisance cardiaque', 'Volumes réduits, eau par voie orale de préférence'],
    ['Insuffisance rénale (DFGe < 30)', 'Réponse aux diurétiques réduite, contrôles rapprochés'],
    ['Insuffisance hépatique', 'Éviter l’excès de sel ; la lactulose favorise la perte d’eau'],
   ]), 32) +
 SOCIAL('Un arrêt de travail n’est en général nécessaire que pendant l’hospitalisation et la convalescence (durée non chiffrée dans les sources).',
        'La conduite est contre-indiquée tant qu’il existe des troubles de la vigilance ou de l’orientation (OAC, annexe 1).',
        'Chez la personne âgée dépendante, l’enjeu est surtout l’organisation des soins à domicile ou en EMS, remboursés en partie par la LAMal.') +
 H4('11.C Surveillance et critères de sortie') +
 TAB(['Quand', 'Quoi'], [
  ['À 2, 4 et 6 heures, puis toutes les 4–6 heures', 'Natrémie, glycémie ; arrêt de la perfusion si la baisse dépasse 10 mmol/L par 24 h'],
  ['Toutes les heures', 'Diurèse, conscience'],
  ['Chaque jour', 'Poids, bilan entrées-sorties'],
  ['Critères de sortie', 'Natrémie stable 135–145 mmol/L, conscience revenue à l’état antérieur, boissons assurées par la personne ou l’entourage'],
 ]) + P('La guérison se définit par une natrémie normale et stable avec retour à l’état cognitif de base.', 32) +
 H4('11.D Pronostic et recherche 2026') +
 P('Le pronostic dépend surtout de la maladie sous-jacente : l’hypernatrémie en réanimation double environ le risque de décès. '
   'La recherche actuelle porte sur la vitesse optimale de correction chez l’adulte, que les essais n’ont pas encore fixée.', 66, 65)))
PTS.append(POINT(12, 'Prévention',
 P('La prévention vise les personnes qui ne peuvent pas boire seules : hydratation programmée sans attendre la soif, et surveillance accrue lors de fièvre, diarrhée ou canicule. '
   'Les diurétiques se suspendent temporairement en cas de diarrhée ou de fièvre, sur avis médical.', 68, 32) +
 F('Prévention primaire, secondaire et tertiaire',
   TAB(['Niveau', 'Mesure'], [
    ['Primaire', 'Plans canicule de l’OFSP et des cantons : boissons proposées régulièrement en EMS et à domicile, pièces fraîches'],
    ['Secondaire', 'Natrémie lors de toute confusion d’une personne âgée ; bilan hydrique quotidien à l’hôpital et en réanimation'],
    ['Tertiaire', 'Revoir les médicaments et l’aide à domicile après un épisode'],
   ]) + P('En Suisse, l’OFSP publie des recommandations de protection contre la chaleur pour les personnes âgées et leurs soignants.', 68), 66)))
PTS.append(POINT(13, 'Points clés',
 P('L’hypernatrémie traduit un manque d’eau libre, presque toujours chez une personne qui ne peut pas boire. '
   'On restaure d’abord le volume en cas de choc, puis on rend l’eau libre par la bouche ou en glucose 5 %. '
   'En hypernatrémie chronique, la natrémie ne doit pas baisser de plus de 10 mmol/L par 24 h. '
   'L’osmolalité urinaire dit si le rein économise l’eau ou la perd.', 32, 33)))
PTS.append(POINT(14, 'Pièges d’examen',
 TAB(['Piège', 'Ce qu’il faut répondre'], [
  ['Corriger avec du NaCl 0,9 % une hypernatrémie sans choc', 'Non : il n’apporte presque pas d’eau libre ; utiliser l’eau ou le glucose 5 %'],
  ['Corriger de 20 mmol/L en 24 h une hypernatrémie ancienne', 'Non : ≤ 10 mmol/L par 24 h, sauf hypernatrémie aiguë'],
  ['Conclure à un « excès de sel »', 'En réalité, il s’agit le plus souvent d’un manque d’eau'],
  ['Attendre que la personne âgée ait soif', 'Non : sa soif est émoussée ; hydratation programmée'],
  ['Natriurèse et osmolalité urinaire oubliées', 'Il faut les prélever avant la perfusion, car elles donnent la cause'],
  ['Correction trop rapide avec céphalée ou aggravation neurologique', 'Arrêter les apports hypotoniques, contrôler la natrémie et demander un avis de réanimation'],
 ]) + P('Ces erreurs sont décrites dans les revues de référence.', 32, 33)))
CTX = {'_prefixe': 'Dans l’hypernatrémie',
 'iono': 'La natrémie se contrôle à 2, 4 et 6 heures ; la baisse ne doit pas dépasser 10 mmol/L par 24 h en forme chronique.',
 'osmo': 'L’osmolalité urinaire > 600 mOsm/kg montre que le rein économise l’eau ; < 300 mOsm/kg, il la perd.',
 'natriurese': 'Une natriurèse < 20 mmol/L oriente vers une perte extrarénale ; élevée, vers un apport de sel ou un diurétique.',
 'creat': 'Une créatinine élevée traduit souvent une insuffisance rénale fonctionnelle par hypovolémie.',
 'uree': 'L’urée élevée peut aussi provoquer une diurèse osmotique (alimentation hyperprotéinée, catabolisme).',
 'gly': 'Une hyperglycémie provoque une diurèse osmotique qui entretient l’hypernatrémie.',
 'tdm': 'Le scanner cérébral sans injection cherche un hématome sous-dural en cas de signe focal.',
 'copeptine': 'La copeptine se demande si les urines restent diluées malgré l’hyperosmolalité.'}
if __name__ == '__main__':
    produire(M, PTS, SOURCES, CTX)
