# -*- coding: utf-8 -*-
"""DX.1 — Diabète sucré décompensé : acidocétose (ACD) et état hyperosmolaire hyperglycémique (EHH). LOT 3, V5 → V7 AUDITÉ."""
from lot3_commun import *
POINT = mkPOINT('dx1')
M = META('dx1', 'DX.1', 'Diabète décompensé', 'Diabète sucré décompensé : acidocétose et état hyperosmolaire hyperglycémique',
         'LOT_003_DX1_Diabete_decompense_AUDITÉ.html',
         'Corrections majeures : seuil d’osmolalité efficace de l’EHH (> 300 mOsm/kg, et non > 320), critères de résolution et seuil du bicarbonate (pH < 7,0) alignés sur le consensus 2024 ; chiffre non sourcé « 60 % des consultations pour polydipsie » supprimé.')
TM = T('transport maximal du glucose', 'Le transport maximal du glucose est le débit au-delà duquel le tubule proximal ne peut plus réabsorber le glucose filtré ; le glucose apparaît alors dans l’urine, en général au-dessus de 10 mmol/L de glycémie.')
CET = T('corps cétoniques', 'Les corps cétoniques sont l’acétoacétate, le β-hydroxybutyrate et l’acétone ; le foie les fabrique à partir des acides gras quand l’insuline manque.')
TA = T('trou anionique', 'Le trou anionique est la différence Na⁺ − (Cl⁻ + HCO₃⁻) ; il estime les anions non dosés, normalement 8–12 mmol/L sans le potassium.')
PTS = []
PTS.append(POINT(1, 'Définition et sémantique',
 P('Le diabète décompensé désigne une hyperglycémie assez forte pour dépasser le ' + TM + ' : le glucose passe dans l’urine et entraîne l’eau. '
   'La soif et la polydipsie compensent cette perte d’eau. Deux urgences vitales en découlent : l’acidocétose diabétique (ACD) et l’état hyperosmolaire hyperglycémique (EHH).', 7, 19) +
 F('Terminologie',
   TAB(['Terme', 'Définition exacte', 'À ne pas confondre avec'], [
    ['Acidocétose diabétique (ACD)', 'Diabète connu ou glycémie ≥ 11,1 mmol/L, β-hydroxybutyrate ≥ 3,0 mmol/L et acidose (pH < 7,30 ou bicarbonates < 18 mmol/L)', 'Cétose de jeûne, sans acidose'],
    ['État hyperosmolaire hyperglycémique (EHH)', 'Glycémie ≥ 33,3 mmol/L, osmolalité efficace > 300 mOsm/kg, sans cétose ni acidose importantes', 'Ancien « coma hyperosmolaire » : le coma n’est pas obligatoire'],
    ['ACD euglycémique', 'ACD avec glycémie < 11,1 mmol/L, surtout sous gliflozine (inhibiteur du SGLT2)', 'Hypoglycémie ou cétose de jeûne'],
    ['Forme mixte ACD-EHH', 'Critères des deux entités réunis', 'Une ACD simple'],
    ['Diurèse osmotique', 'Perte d’eau entraînée par un soluté non réabsorbé (ici le glucose)', 'Diurèse aqueuse du déficit en vasopressine'],
   ]) + P('Le consensus 2024 a abaissé le seuil d’osmolalité de l’EHH à 300 mOsm/kg (osmolalité efficace calculée) ; le seuil de 320 mOsm/kg concerne l’osmolalité totale mesurée.', 7))))
PTS.append(POINT(2, 'Épidémiologie (Suisse, puis Europe)',
 P('En Suisse, 6,2 % des personnes de 15 ans et plus déclarent un diabète (Enquête suisse sur la santé 2022). '
   'En Europe, la Fédération internationale du diabète estime 61 millions d’adultes diabétiques en 2021. '
   'L’ACD révèle un diabète de type 1 chez ≈ 20–45 % des enfants selon les pays ; l’EHH touche surtout la personne âgée avec un diabète de type 2.', 2, 25, 24) +
 F('Chiffres, terrain et histoire naturelle',
   TAB(['Donnée', 'Valeur', 'Portée'], [
    ['Diabète déclaré, Suisse', '6,2 % des ≥ 15 ans (ESS 2022)', 'Autodéclaration : sous-estime le diabète non diagnostiqué'],
    ['Diabète, Europe', '≈ 61 millions d’adultes de 20–79 ans (2021)', 'Estimation modélisée de l’IDF'],
    ['ACD au diagnostic du type 1 (enfants)', '≈ 20–45 % selon les pays (2006–2016)', '13 pays, dont plusieurs pays européens'],
    ['Mortalité de l’ACD (adulte, pays à hauts revenus)', '< 1 %', 'Plus élevée chez la personne âgée et en cas de coma'],
    ['Mortalité de l’EHH', 'Nettement plus élevée que celle de l’ACD (≈ 5–20 % selon les séries)', 'Âge, comorbidités et retard au diagnostic'],
    ['Œdème cérébral de l’enfant en ACD', '≈ 0,5–0,9 % des épisodes', 'Première cause de décès de l’ACD pédiatrique'],
    ['Incidence suisse de l’ACD et de l’EHH', 'Non disponible', 'Aucune source suisse publiée trouvée'],
   ]) + P('Le chiffre « 60 % des consultations pour polydipsie » de l’original n’a pas de source et a été retiré. Le chiffre « ≈ 500 000 diabétiques » attribué à la SSED a été remplacé par la donnée Obsan.', 2, 7, 17))))
PTS.append(POINT(3, 'Physiopathologie',
 P('Le glucose filtré est réabsorbé par les cotransporteurs SGLT2 (≈ 90 %) et SGLT1 (≈ 10 %) du tubule proximal. '
   'Au-delà d’une glycémie d’environ 10 mmol/L, le glucose reste dans la lumière tubulaire et retient l’eau, le sodium et le potassium. '
   'La déshydratation qui suit réduit le débit de filtration glomérulaire, ce qui élève encore la glycémie : c’est un cercle vicieux.', 7, 19) +
 F('Chaîne logique : de l’anatomie au traitement',
   TAB(['Étape', 'Ce qu’il faut comprendre'], [
    ['Anatomie', 'Le pancréas endocrine (cellules β) sécrète l’insuline ; le foie, le muscle et le tissu adipeux en sont les cibles ; le tubule proximal réabsorbe le glucose.'],
    ['Physiologie', 'Pourquoi l’insuline compte : elle fait entrer le glucose dans les cellules et freine la lipolyse et la fabrication des ' + CET + '.'],
    ['Physiopathologie', 'Sans insuline (ACD), les acides gras affluent au foie et deviennent des cétones acides. Avec un peu d’insuline (EHH), la lipolyse reste freinée, mais la glycémie monte très haut.'],
    ['Clinique', 'D’où la polyurie, la soif, l’amaigrissement, puis la respiration ample de Kussmaul (ACD) ou les troubles de conscience par hyperosmolalité (EHH).'],
    ['Examens', 'On mesure ce qui définit la crise : glycémie, β-hydroxybutyrate, gazométrie veineuse, ionogramme avec ' + TA + ' et osmolalité efficace.'],
    ['Traitement', 'On corrige dans l’ordre : le volume (perfusion), le potassium, puis l’insuline, qui arrête la cétogenèse ; on ajoute du glucose pour poursuivre l’insuline sans hypoglycémie.'],
   ]), 7, 16) +
 F('Mécanisme, exploration et cible thérapeutique',
   TAB(['Mécanisme', 'ACD', 'EHH', 'Cible thérapeutique'], [
    ['Insuline', 'Carence absolue (peptide C effondré) et excès de glucagon, cortisol, adrénaline', 'Insuline résiduelle suffisante pour freiner la lipolyse', 'Insuline IV à débit fixe'],
    ['Voie métabolique', 'Lipolyse → acides gras → β-oxydation hépatique → corps cétoniques', 'Néoglucogenèse sans cétogenèse importante', 'Insuline + glucose dès que la glycémie baisse'],
    ['Déficit en eau (ordre de grandeur)', '≈ 100 mL/kg, installé en 24–48 h', '≈ 100–220 mL/kg, installé en plusieurs jours', 'Cristalloïdes IV'],
    ['Potassium', 'Stock total effondré malgré une kaliémie souvent normale', 'Même mécanisme, moins marqué', 'KCl avant ou avec l’insuline'],
    ['Complication propre', 'Acidose, hypokaliémie sous insuline, œdème cérébral (enfant)', 'Thromboses, troubles de conscience, myélinolyse si correction trop rapide', 'Correction lente de l’osmolalité'],
   ]) + P('L’acidose déplace le potassium hors des cellules ; l’insuline le fait rentrer brutalement. C’est pourquoi une kaliémie < 3,5 mmol/L impose de différer l’insuline.', 7, 15, 16))))
PTS.append(POINT(4, 'Raisonnement clinique et diagnostic différentiel',
 P('Devant une polyurie avec soif, le médecin mesure d’abord la glycémie capillaire : elle confirme ou écarte en une minute la cause la plus fréquente. '
   'Si elle est élevée, la cétonémie et la gazométrie trient la simple hyperglycémie, l’ACD et l’EHH. '
   'Une ACD peut exister avec une glycémie normale sous gliflozine : on dose donc la cétonémie dès qu’il y a nausées ou dyspnée.', 7, 19) +
 DIFF('dm') +
 F('Diagnostic différentiel de l’acidose métabolique à trou anionique élevé',
   TAB(['Diagnostic et fréquence', 'Éléments d’orientation', 'Examen discriminant'], [
    ['ACD' + PR('fréquence suisse non publiée', 7), 'Diabète connu ou inaugural, β-hydroxybutyrate ≥ 3,0 mmol/L', 'Cétonémie, gazométrie'],
    ['ACD euglycémique sous gliflozine' + PR('fréquence non publiée en population générale', 7), 'Gliflozine, jeûne, chirurgie, glycémie < 11,1 mmol/L', 'Cétonémie malgré une glycémie normale'],
    ['Acidocétose alcoolique' + PR('fréquence non publiée en population générale', 16), 'Alcoolisme, vomissements, glycémie basse ou normale', 'Alcoolémie, cétonémie, glycémie'],
    ['Acidose lactique' + PR('fréquence non publiée en population générale', 16), 'Choc, sepsis, metformine avec insuffisance rénale', 'Lactate > 4 mmol/L'],
    ['Intoxication (méthanol, éthylène glycol, salicylés)' + PR('rare, fréquence non publiée', 16), 'Trou osmolaire élevé, troubles visuels, ingestion', 'Toxicologie, osmolalité mesurée'],
    ['Insuffisance rénale aiguë ou chronique sévère' + PR('fréquence non publiée en population générale', 44), 'Créatinine élevée, oligurie', 'Créatinine, urée'],
   ]) + P('Ces fréquences ne sont pas publiées sur une base commune ; le tableau sert à ordonner la recherche, non à estimer une probabilité.', 7, 16))))
PTS.append(POINT(5, 'Anamnèse ciblée et drapeaux rouges',
 P('L’anamnèse cherche le facteur déclenchant : arrêt ou panne d’insuline (pompe), infection, infarctus indolore, corticoïdes, gliflozine, alcool, pancréatite. '
   'Elle date la polyurie, la soif et la perte de poids, et précise le type et le traitement du diabète.', 7, 16) +
 U('Drapeaux rouges : vomissements avec douleurs abdominales, respiration ample de Kussmaul, somnolence ou confusion, déshydratation avec hypotension, kaliémie < 3,5 mmol/L, enfant ou femme enceinte. Ils imposent une prise en charge hospitalière immédiate.', 7, 16, 17) +
 F('Questions ciblées et leur raison',
   TAB(['Question', 'Pourquoi la poser'], [
    ['Avez-vous oublié, réduit ou perdu votre insuline (pompe débranchée, cathéter bouché) ?', 'L’arrêt de l’insuline est le premier déclencheur de l’ACD.'],
    ['Avez-vous de la fièvre, une toux, des brûlures urinaires ?', 'Une infection déclenche une grande partie des crises.'],
    ['Prenez-vous une gliflozine (empagliflozine, dapagliflozine) ou des corticoïdes ?', 'La gliflozine favorise l’ACD euglycémique ; les corticoïdes élèvent la glycémie.'],
    ['Depuis quand urinez-vous et buvez-vous plus ? Combien de kilos avez-vous perdus ?', 'Quelques jours orientent vers l’ACD, une à deux semaines vers l’EHH.'],
    ['Avez-vous eu une douleur thoracique ou un malaise ?', 'Un infarctus peut être indolore chez le diabétique et déclencher la crise.'],
    ['Buvez-vous de l’alcool ? Consommez-vous de la cocaïne ?', 'Ils favorisent l’ACD et l’acidocétose alcoolique.'],
   ]), 7, 16)))
PTS.append(POINT(6, 'Examen clinique',
 P('L’examen mesure la gravité : fréquence respiratoire, pression artérielle, pouls, conscience (score de Glasgow), signes de déshydratation et température. '
   'Il cherche aussi un foyer infectieux et une douleur abdominale chirurgicale.', 7, 16) +
 P('On note d’abord les valeurs normales de l’adulte : fréquence respiratoire 12–20/min, pouls 60–100/min, Glasgow 15. '
   'Aucun signe isolé n’a de sensibilité ni de spécificité publiées suffisantes ; leur valeur vient de leur association et de la biologie.', 16) +
 F('Signes, technique et valeur',
   TAB(['Signe', 'Technique', 'Ce qu’il signifie'], [
    ['Respiration de Kussmaul', 'Observer une respiration ample, profonde et régulière', 'Compensation respiratoire d’une acidose métabolique, surtout si pH < 7,20'],
    ['Haleine « fruitée »', 'Sentir l’haleine près du visage', 'Acétone volatile ; signe inconstant'],
    ['Pli cutané, muqueuses sèches', 'Pincer la peau du sternum ; regarder la langue', 'Déshydratation ; peu fiable chez la personne âgée'],
    ['Tachycardie, hypotension orthostatique', 'Pouls et pression couché puis debout', 'Hypovolémie'],
    ['Troubles de conscience', 'Score de Glasgow', 'Hyperosmolalité (EHH) ou acidose sévère'],
    ['Défense abdominale', 'Palpation douce des quatre quadrants', 'Douleur de l’ACD ou vraie urgence chirurgicale : réévaluer après correction'],
    ['Fièvre ou hypothermie', 'Température centrale', 'Infection déclenchante ; l’hypothermie est de mauvais pronostic'],
   ]), 7, 16)))
PTS.append(POINT(7, 'Syndromes et signes cliniques',
 F('Signes fonctionnels (symptômes rapportés)', UL(['Soif intense et polyurie, y compris la nuit', 'Fatigue, faiblesse, crampes', 'Nausées, vomissements, douleurs abdominales', 'Vision floue (variation osmotique du cristallin)', 'Somnolence rapportée par l’entourage']), 16) +
 F('Signes physiques (constatés à l’examen)', UL(['Respiration ample de Kussmaul', 'Haleine à l’odeur d’acétone', 'Tachycardie, hypotension, pli cutané', 'Troubles de conscience, parfois signes focaux', 'Amaigrissement mesuré sur la balance']), 16, 15) +
 P('Le syndrome cardinal réunit polyurie, polydipsie, amaigrissement et polyphagie : il traduit la fuite urinaire du glucose. '
   'Le syndrome d’acidocétose y ajoute nausées, vomissements, douleurs abdominales et respiration de Kussmaul. '
   'Le syndrome hyperosmolaire associe déshydratation majeure et troubles neurologiques, parfois focaux.', 7, 15, 16) +
 F('Syndrome cardinal diabétique',
   TAB(['Signe', 'Mécanisme', 'Valeur'], [
    ['Polyurie (> 3 L/24 h chez l’adulte)', 'Diurèse osmotique par la glycosurie', 'Constante quand la glycémie dépasse le seuil rénal'],
    ['Polydipsie', 'Soif déclenchée par l’hyperosmolalité et l’hypovolémie', 'Compense la perte ; manque chez la personne âgée'],
    ['Amaigrissement', 'Perte calorique urinaire et catabolisme', 'Rapide dans le type 1'],
    ['Polyphagie', 'Faim cellulaire malgré l’hyperglycémie', 'Inconstante'],
   ]), 7) +
 F('Syndrome d’acidocétose',
   TAB(['Signe', 'Mécanisme', 'Valeur'], [
    ['Nausées, vomissements', 'Cétose et acidose', 'Fréquents ; ils aggravent la déshydratation'],
    ['Douleurs abdominales', 'Acidose, iléus, distension', 'Disparaissent avec la correction ; sinon chercher une cause chirurgicale'],
    ['Respiration de Kussmaul', 'Élimination du CO₂', 'Signe d’acidose marquée'],
   ]), 16) +
 F('Syndrome hyperosmolaire',
   TAB(['Signe', 'Mécanisme', 'Valeur'], [
    ['Obnubilation, coma', 'Déshydratation cellulaire cérébrale', 'Corrélé à l’osmolalité'],
    ['Signes focaux, convulsions', 'Hyperosmolalité', 'Peuvent simuler un accident vasculaire cérébral'],
    ['Thrombose veineuse ou artérielle', 'Hyperviscosité et hypovolémie', 'Justifie la prophylaxie anticoagulante'],
   ]), 15)))
PTS.append(POINT(8, 'Critères diagnostiques',
 P('Le diagnostic de diabète repose sur la glycémie ou l’HbA1c ; celui de l’ACD et de l’EHH sur les critères du consensus 2024. '
   'Les trois lettres de l’ACD résument ses critères : D pour diabète ou glycémie ≥ 11,1 mmol/L, K pour cétose, A pour acidose. '
   'Une HbA1c élevée ne suffit pas à poser une ACD, et une cétonurie isolée ne suffit pas non plus.', 7, 19) +
 F('Critères du diabète sucré (ADA 2025)',
   TAB(['Critère', 'Seuil'], [
    ['Glycémie à jeun (≥ 8 h)', '≥ 7,0 mmol/L'],
    ['Glycémie 2 h après 75 g de glucose', '≥ 11,1 mmol/L'],
    ['HbA1c', '≥ 6,5 % (48 mmol/mol)'],
    ['Glycémie aléatoire avec symptômes', '≥ 11,1 mmol/L'],
   ]) + P('Sans symptômes, un résultat anormal doit être confirmé par un second test.', 19)) +
 F('Critères de l’ACD et de l’EHH (consensus ADA/EASD/JBDS 2024)',
   TAB(['Paramètre', 'ACD', 'EHH'], [
    ['Glycémie', '≥ 11,1 mmol/L ou diabète connu', '≥ 33,3 mmol/L'],
    ['β-hydroxybutyrate', '≥ 3,0 mmol/L (ou cétonurie ≥ 2+)', '< 3,0 mmol/L'],
    ['pH veineux', '< 7,30', '≥ 7,30'],
    ['Bicarbonates', '< 18 mmol/L', '≥ 15 mmol/L'],
    ['Osmolalité', 'Variable', 'Efficace calculée > 300 mOsm/kg ou totale > 320 mOsm/kg'],
   ]) + P('Les formes mixtes sont fréquentes ; on traite alors l’acidose et l’hyperosmolalité.', 7)) +
 F('Gravité de l’ACD',
   TAB(['Grade', 'pH', 'Bicarbonates (mmol/L)'], [
    ['Légère', '7,25–7,30', '15–18'],
    ['Modérée', '7,00–7,24', '10–14,9'],
    ['Sévère', '< 7,00', '< 10'],
   ]) + P('La sévérité s’aggrave aussi si la kaliémie est < 3,5 mmol/L, si la conscience est altérée ou si la pression systolique est < 90 mmHg.', 7, 16))))
PTS.append(POINT(9, 'Examens complémentaires',
 H4('9.a Examen de référence') +
 P('Aucun examen isolé ne suffit : le diagnostic associe la glycémie veineuse, le β-hydroxybutyrate capillaire ou sanguin, la gazométrie veineuse et l’ionogramme. '
   'La cétonémie remplace la cétonurie, car la bandelette ne détecte pas le β-hydroxybutyrate. '
   'Le consensus ne publie pas de sensibilité ni de spécificité chiffrées pour cet ensemble ; la cétonurie est moins spécifique, car le jeûne la rend positive.', 7, 16) +
 H4('9.b Examens de première et de deuxième intention') +
 P('En première intention, on prélève tout le bilan de crise avant l’insuline. En deuxième intention, on cherche le déclencheur si le tableau l’évoque : fièvre, douleur thoracique ou abdominale.', 7, 16) +
 TAB(['Intention', 'Examen', 'Pourquoi'], [
  ['1re', 'Glycémie veineuse et capillaire', 'Confirme l’hyperglycémie et suit la correction'],
  ['1re', 'Cétonémie (β-hydroxybutyrate)', 'Définit l’ACD et sa résolution'],
  ['1re', 'Gazométrie veineuse', 'pH et bicarbonates ; la voie veineuse suffit'],
  ['1re', 'Ionogramme, créatinine, urée', 'Kaliémie avant l’insuline, trou anionique, insuffisance rénale'],
  ['1re', 'Osmolalité plasmatique calculée ou mesurée', 'Définit l’EHH et guide la vitesse de correction'],
  ['1re', 'ECG', 'Signes de dyskaliémie, infarctus déclenchant'],
  ['1re', 'Hémogramme, lactate, analyse d’urine', 'Infection, hypoperfusion'],
  ['2e', 'Hémocultures, radiographie du thorax, troponine, lipase', 'Selon le facteur déclenchant suspecté'],
  ['2e', 'HbA1c', 'Ancienneté du déséquilibre'],
  ['2e', 'Auto-anticorps (anti-GAD, anti-IA2, anti-ZnT8) et peptide C', 'Type de diabète, à distance de la crise pour le peptide C'],
 ]) +
 H4('9.c Prescription et formules') +
 P('Indication : toute glycémie > 11,1 mmol/L avec malaise, ou tout patient sous gliflozine avec nausées. Moment : avant la première dose d’insuline, puis toutes les 2–4 heures. '
   'Préparation : aucune ; on ne fait pas attendre un patient à jeun, et la gazométrie veineuse évite la ponction artérielle.', 7, 16) +
 TAB(['Grandeur', 'Formule', 'Repère'], [
  ['Trou anionique', 'Na⁺ − (Cl⁻ + HCO₃⁻)', 'Normal 8–12 mmol/L ; > 12 = acides non dosés'],
  ['Natrémie corrigée', 'Na⁺ mesuré + 0,3 × (glycémie − 5,5) [Katz] ; 0,4 avec le facteur de Hillier', 'Une valeur corrigée > 145 mmol/L signe un déficit en eau libre'],
  ['Osmolalité efficace', '2 × Na⁺ + glycémie (mmol/L)', 'Normale 275–295 mOsm/kg ; EHH > 300 mOsm/kg'],
  ['Compensation respiratoire (Winter)', 'pCO₂ attendue = 1,5 × HCO₃⁻ + 8 (± 2) mmHg', 'pCO₂ plus haute : trouble respiratoire associé'],
 ]) + P('Exemple : Na⁺ 128 mmol/L et glycémie 35,5 mmol/L donnent une natrémie corrigée de 128 + 0,3 × 30 = 137 mmol/L ; il n’y a pas de vraie hyponatrémie.', 61, 7) +
 H4('9.d Interprétation : positif, négatif, limite, discordant') +
 TAB(['Situation', 'Interprétation', 'Conduite'], [
  ['Positif : β-hydroxybutyrate ≥ 3,0, pH < 7,30', 'ACD confirmée', 'Protocole ACD'],
  ['Négatif : cétonémie < 0,6 et pH normal', 'Pas d’ACD ; vérifier l’osmolalité', 'Hyperglycémie simple ou EHH'],
  ['Limite : cétonémie 1,5–3,0 mmol/L', 'Cétose sans critère d’ACD', 'Insuline, contrôle à 1–2 h'],
  ['Discordant : cétonurie négative et ACD clinique', 'La bandelette ignore le β-hydroxybutyrate', 'Doser la cétonémie'],
  ['Discordant : kaliémie normale et ACD', 'Le stock de potassium est pourtant bas', 'Prévoir le potassium dès l’insuline'],
 ]) +
 H4('9.e Alternatives') +
 P('Grossesse : mêmes examens, avec surveillance fœtale. Enfant : gazométrie veineuse et cétonémie capillaire, sans ponction artérielle. '
   'DFGe < 30 ou déshydratation : éviter le produit de contraste iodé tant que la perfusion n’a pas corrigé l’hypovolémie ; l’IRM n’a pas de place dans la crise.', 7, 17) +
 P('Si la cétonémie n’est pas disponible, une cétonurie ≥ 2+ est acceptée pour le diagnostic, mais pas pour suivre la résolution. Le peptide C se dose à distance de la crise, car la glucotoxicité l’abaisse transitoirement.', 7, 18) +
 F('Auto-anticorps et peptide C : lecture', TAB(['Marqueur', 'Ce qu’il montre'], [
  ['Anti-GAD65', 'Attaque auto-immune ; positif chez la majorité des patients de type 1 et dans le LADA'],
  ['Anti-IA2, anti-ZnT8, anti-insuline', 'Augmentent la probabilité d’un type 1 ; l’anti-insuline perd sa valeur après le début de l’insuline'],
  ['Peptide C < 200 pmol/L', 'Carence sévère en insuline, compatible avec un type 1 et nécessitant une insuline à vie'],
  ['Peptide C > 600 pmol/L (à jeun, à distance)', 'Réserve conservée ; type 2 ou diabète monogénique plus probable'],
 ]), 18)))
PTS.append(POINT(10, 'Arbre décisionnel',
 P('L’ordre des priorités ne change pas : perfuser, vérifier la kaliémie, puis débuter l’insuline. On ne commence jamais l’insuline si la kaliémie est < 3,5 mmol/L.', 7, 16) +
 F('Arbre décisionnel : polyurie, soif et glycémie élevée',
   OL(['Glycémie capillaire > 11,1 mmol/L, ou patient sous gliflozine avec malaise : doser cétonémie, gazométrie veineuse, ionogramme, créatinine.',
       'β-hydroxybutyrate ≥ 3,0 et pH < 7,30 ou bicarbonates < 18 : ACD ; classer la gravité.',
       'Glycémie ≥ 33,3, osmolalité efficace > 300, pas d’acidose : EHH.',
       'Ni l’une ni l’autre : hyperglycémie simple ; insuline sous-cutanée et recherche du déclencheur.',
       'Dans l’ACD et l’EHH : 1 L de cristalloïde la première heure, puis kaliémie ; si < 3,5 mmol/L, potassium d’abord et insuline différée.',
       'Signes de gravité (pH < 7,0, coma, choc, kaliémie < 3,5) : soins intermédiaires ou intensifs.']), 7, 15, 16)))
PTS.append(POINT(11, 'Prise en charge',
 H4('11.A Buts : d’abord l’urgence vitale (ACD, EHH), car elle tue en quelques heures') +
 P('Le traitement restaure le volume circulant, arrête la cétogenèse et corrige le potassium. Il abaisse l’osmolalité lentement pour éviter l’œdème cérébral, puis traite la cause.', 7) +
 TAB(['But', 'Cible chiffrée'], [
  ['Baisse de la glycémie', '≈ 3–4 mmol/L par heure (ACD) ; ≤ 5 mmol/L par heure (EHH)'],
  ['Baisse de l’osmolalité (EHH)', '3–8 mOsm/kg par heure'],
  ['Kaliémie', '4,0–5,0 mmol/L'],
  ['Glycémie pendant l’insuline IV', '8,3–13,9 mmol/L jusqu’à la résolution'],
 ]) + P('Ces cibles proviennent du consensus 2024 et du guide britannique de l’EHH.', 7, 15) +
 H4('11.B Moyens et méthodes : forme compliquée en urgence, puis forme non compliquée en ambulatoire') +
 P('Les moyens non médicamenteux sont la surveillance continue, deux voies veineuses, le bilan entrées-sorties horaire et l’éducation thérapeutique avant la sortie.', 16) +
 F('Protocole de l’ACD et de l’EHH aux urgences (consensus 2024)',
   TAB(['Pilier', 'Produit', 'Posologie et seuils', 'Pourquoi'], [
    ['1. Volume', 'NaCl 0,9 % ou cristalloïde équilibré (Ringer lactate)', '1–1,5 L la 1re heure (15–20 mL/kg), puis 250–500 mL/h selon l’état hémodynamique', 'Restaure la perfusion rénale et l’élimination du glucose'],
    ['2. Glucose', 'Glucose 5 % (ou 10 %)', 'Dès glycémie < 13,9 mmol/L, en maintenant l’insuline', 'La cétose disparaît après la glycémie ; il faut poursuivre l’insuline'],
    ['3. Potassium', 'KCl IV dilué', 'K⁺ < 3,5 : 10–20 mmol/h et insuline différée ; 3,5–5,0 : 20–30 mmol par litre ; > 5,0 : pas de K⁺, contrôle toutes les 2 h', 'L’insuline fait entrer le potassium dans les cellules'],
    ['4. Insuline', 'Insuline humaine rapide (Actrapid®) IV au pousse-seringue', '0,1 U/kg/h à débit fixe (bolus de 0,1 U/kg facultatif) ; 0,05 U/kg/h dès glycémie < 13,9 mmol/L', 'Bloque la lipolyse et la cétogenèse'],
    ['EHH', 'Même produit', 'Liquides d’abord ; insuline 0,05 U/kg/h si la glycémie ne baisse plus ou si β-hydroxybutyrate > 1,0 mmol/L', 'Éviter une chute trop rapide de l’osmolalité'],
    ['5. Relais', 'Insuline basale sous-cutanée + rapide', 'Injecter la basale 1–2 h avant d’arrêter la pompe IV', 'La demi-vie de l’insuline IV est de quelques minutes : sans chevauchement, la cétose récidive'],
    ['Bicarbonate', 'Bicarbonate de sodium', 'Seulement si pH < 7,0', 'Aggrave l’hypokaliémie ; aucun bénéfice prouvé au-dessus'],
    ['Phosphate', 'Phosphate de potassium', 'Si phosphatémie < 0,32 mmol/L, insuffisance cardiaque ou respiratoire', 'Évite l’hémolyse et la faiblesse musculaire'],
   ]) + P('Doses hors AIPS : elles proviennent des recommandations internationales et doivent être vérifiées avant prescription. Dans la forme compliquée, la première heure est consacrée au volume, car l’insuline sans volume aggrave le collapsus.', 7, 15, 16, 55)) +
 FICHE([
  ['Insuline humaine rapide (Actrapid®)', 'Agoniste du récepteur de l’insuline : entrée du glucose, arrêt de la lipolyse', 'Demi-vie IV ≈ 5 min ; élimination rénale et hépatique', '0,1 U/kg/h IV jusqu’à la résolution (en général 12–24 h)', 'Hypoglycémie, hypokaliémie', 'Kaliémie < 3,5 mmol/L (différer)', 'Corticoïdes (besoins accrus), bêtabloquants (masquent l’hypoglycémie)'],
  ['Metformine (biguanide)', 'Inhibe la néoglucogenèse hépatique', 'Non métabolisée, élimination rénale', '500 mg 1–2 ×/j, au long cours', 'Troubles digestifs, carence en B12, acidose lactique rare', 'DFGe < 30, hypoxie, produit de contraste iodé avec DFGe bas', 'Produits iodés, alcool'],
  ['Gliflozine : empagliflozine (Jardiance®)', 'Inhibe le SGLT2 : glycosurie', 'Demi-vie ≈ 12 h ; métabolisme hépatique', '10 mg 1 ×/j, au long cours', 'ACD euglycémique, mycoses génitales, déshydratation', 'Type 1 (hors indication), jeûne, chirurgie', 'Diurétiques (hypovolémie), insuline (hypoglycémie)'],
 ], 7, 19) +
 F('Traitement de fond (ambulatoire, Suisse)',
   TAB(['Situation', 'Classe et molécule', 'Repère posologique', 'Précaution'], [
    ['Type 1', 'Insuline basale (dégludec Tresiba®, glargine U300 Toujeo®) + analogue rapide aux repas (asparte NovoRapid® ou Fiasp®, lispro Humalog®)', 'Dose totale de départ ≈ 0,4–0,5 U/kg/j, dont environ la moitié en basale', 'Pompe ou boucle fermée hybride si disponible'],
    ['Type 2, première ligne', 'Metformine (biguanide)', '500 mg 1–2 ×/j, à augmenter progressivement', 'Réduire si DFGe 30–45 ; contre-indiquée si DFGe < 30 mL/min/1,73 m²'],
    ['Type 2 avec maladie cardiovasculaire, rénale ou insuffisance cardiaque', 'Gliflozine : empagliflozine (Jardiance®) ou dapagliflozine (Forxiga®)', '10 mg 1 ×/j', 'Suspendre lors d’une maladie aiguë, d’un jeûne ou 3 jours avant une chirurgie'],
    ['Type 2, poids ou risque cardiovasculaire', 'Agoniste du GLP-1 (sémaglutide Ozempic®) ou double agoniste GIP/GLP-1 (tirzépatide Mounjaro®)', 'Sémaglutide 0,25 → 1 mg/semaine ; tirzépatide 2,5 → 15 mg/semaine', 'Nausées ; arrêter en cas de pancréatite'],
   ]) + P('Les posologies proviennent de l’original et des recommandations ADA 2025 ; elles restent à vérifier dans l’AIPS.', 19, 55)) +
 F('Situations particulières',
   TAB(['Situation', 'Particularité'], [
    ['Enfant et adolescent', 'Perfusion plus lente, sans bolus d’insuline ; surveillance neurologique pour l’œdème cérébral'],
    ['Grossesse', 'L’ACD survient à des glycémies plus basses et menace le fœtus : avis obstétrical immédiat'],
    ['Insuffisance cardiaque ou rénale', 'Volumes réduits et réévalués toutes les heures'],
    ['Gliflozine', 'Arrêter la molécule ; l’ACD euglycémique demande du glucose dès le début de l’insuline'],
    ['Personne âgée (EHH)', 'Prophylaxie de la thrombose par héparine de bas poids moléculaire, sauf contre-indication'],
   ]), 7, 15, 17) +
 SOCIAL('Un arrêt de quelques jours suit l’hospitalisation ; sa durée dépend du déclencheur (ordre de grandeur, non chiffré dans les sources).',
        'Après une hypoglycémie sévère ou une décompensation, la conduite reste suspendue jusqu’à l’équilibre ; les recommandations de la SSED 2025 et l’annexe 1 de l’OAC s’appliquent.') +
 H4('11.C Surveillance et critères de sortie') +
 TAB(['Quand', 'Quoi'], [
  ['Toutes les heures', 'Glycémie capillaire, cétonémie, conscience, diurèse'],
  ['Toutes les 2–4 heures', 'Gazométrie veineuse, ionogramme, trou anionique, osmolalité'],
  ['Résolution de l’ACD', 'β-hydroxybutyrate < 0,6 mmol/L et pH ≥ 7,30 ou bicarbonates ≥ 18 mmol/L'],
  ['Résolution de l’EHH', 'Osmolalité < 300 mOsm/kg, conscience normale, glycémie < 13,9 mmol/L'],
  ['Sortie', 'Alimentation orale, insuline sous-cutanée réglée, patient formé aux jours de maladie, suivi fixé'],
  ['Suivi chronique', 'HbA1c tous les 3 mois (cible usuelle < 7 %) ; temps dans la cible 3,9–10,0 mmol/L > 70 % au capteur ; albuminurie et fond d’œil chaque année'],
 ]) + P('Les critères de résolution et de suivi proviennent du consensus 2024 et du consensus sur le temps dans la cible.', 7, 23, 19) +
 H4('11.D Pronostic et recherche 2026') +
 P('Le diabète de type 1 reste incurable ; le type 2 peut entrer en rémission (HbA1c < 6,5 % au moins 3 mois sans traitement) après une forte perte de poids. '
   'Le téplizumab, un anticorps anti-CD3, a retardé d’environ 2 ans le passage au type 1 clinique chez des apparentés à risque.', 22, 21) +
 P('Des îlots dérivés de cellules souches (zimislécel) ont rendu des patients indépendants de l’insuline dans un essai précoce ; leur statut suisse reste à vérifier. Les insulines basales hebdomadaires (icodec) sont autorisées dans l’Union européenne depuis 2024.', 63, 55)))
PTS.append(POINT(12, 'Prévention',
 P('Les règles des jours de maladie réduisent le risque d’ACD. Le patient n’arrête jamais l’insuline basale, mesure glycémie et cétonémie toutes les 2–4 heures et boit régulièrement. '
   'Il appelle si la cétonémie dépasse 1,5 mmol/L. '
   'Lors d’une maladie aiguë, d’un jeûne ou d’une chirurgie, on suspend temporairement la gliflozine et la metformine.', 7, 16) +
 F('Prévention primaire, secondaire et tertiaire',
   TAB(['Niveau', 'Mesure'], [
    ['Primaire', 'Dépister le type 2 chez les personnes à risque ; dépistage du type 1 présymptomatique par auto-anticorps chez les apparentés'],
    ['Secondaire', 'Éducation aux jours de maladie, lecteur de cétonémie à domicile pour le type 1 et les patients sous gliflozine'],
    ['Tertiaire', 'Analyser chaque épisode : panne de pompe, difficultés financières, troubles du comportement alimentaire'],
   ]) + P('En Suisse, la SSED publie les recommandations de prise en charge et d’aptitude à la conduite ; l’éducation thérapeutique est remboursée par l’assurance de base sur prescription.', 8, 13, 56), 19, 20)))
PTS.append(POINT(13, 'Points clés',
 P('La polyurie du diabète est osmotique : le glucose entraîne l’eau, d’où la soif. '
   'L’ACD se définit par la cétonémie ≥ 3,0 mmol/L et l’acidose, l’EHH par l’hyperglycémie majeure et l’osmolalité efficace > 300 mOsm/kg. '
   'On perfuse d’abord, on vérifie la kaliémie, puis on donne l’insuline. '
   'La résolution se juge sur la cétonémie et le pH, jamais sur la cétonurie.', 7, 16)))
PTS.append(POINT(14, 'Pièges d’examen',
 TAB(['Piège', 'Ce qu’il faut répondre'], [
  ['Démarrer l’insuline avec une kaliémie < 3,5 mmol/L', 'Non : potassium d’abord, insuline différée'],
  ['Arrêter l’insuline quand la glycémie se normalise', 'Non : on ajoute du glucose et on poursuit jusqu’à la résolution de la cétose'],
  ['Suivre la guérison sur la cétonurie', 'Non : la bandelette reste positive ; suivre le β-hydroxybutyrate'],
  ['Donner du bicarbonate dès pH < 7,10', 'Non : seulement si pH < 7,0'],
  ['Exclure une ACD parce que la glycémie est normale', 'Non : ACD euglycémique sous gliflozine'],
  ['Retenir 320 mOsm/kg d’osmolalité efficace pour l’EHH', 'Le seuil 2024 est > 300 mOsm/kg (efficace) ou > 320 mOsm/kg (totale)'],
  ['Corriger rapidement une hyperosmolalité', 'Non : 3–8 mOsm/kg par heure au maximum'],
 ]) + P('Ces pièges reprennent les erreurs les plus fréquentes signalées par les consensus.', 7, 15)))
CTX = {'_prefixe': 'Dans le diabète décompensé',
 'gly': 'La glycémie capillaire trie en une minute ; la glycémie veineuse confirme et sert aux formules.',
 'cetone': 'Le β-hydroxybutyrate ≥ 3,0 mmol/L définit l’ACD ; < 0,6 mmol/L signe sa résolution.',
 'gds': 'La gazométrie veineuse suffit pour le pH et les bicarbonates ; on la répète toutes les 2–4 heures.',
 'iono': 'La kaliémie décide du moment de l’insuline ; la natrémie se corrige pour la glycémie.',
 'osmo': 'Une osmolalité efficace > 300 mOsm/kg définit l’EHH ; elle doit baisser de 3–8 mOsm/kg par heure.',
 'creat': 'Une créatinine élevée traduit souvent l’hypovolémie et se corrige avec la perfusion.',
 'ecg': 'L’ECG cherche une hypo- ou hyperkaliémie et un infarctus déclenchant.',
 'hba1c': 'Une HbA1c élevée indique un déséquilibre ancien ; normale, elle oriente vers une ACD inaugurale rapide.',
 'peptc': 'Le peptide C se dose à distance de la crise : < 200 pmol/L confirme une carence sévère en insuline.',
 'autoac': 'Les auto-anticorps confirment un type 1 ou un LADA quand le type est incertain.',
 'lact': 'Un lactate élevé fait chercher un choc, un sepsis ou une acidose sous metformine.'}
if __name__ == '__main__':
    produire(M, PTS, SOURCES, CTX)
