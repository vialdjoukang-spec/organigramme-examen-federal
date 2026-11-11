# -*- coding: utf-8 -*-
"""DX.4 — Polydipsie primaire. LOT 3, V5 → V7 AUDITÉ."""
from lot3_commun import *
POINT = mkPOINT('dx4')
M = META('dx4', 'DX.4', 'Polydipsie primaire', 'Polydipsie primaire (potomanie)',
         'LOT_003_DX4_Polydipsie_primaire_AUDITÉ.html',
         'Corrections majeures : « 5 % des consultations » retiré faute de source ; « consensus ESE » remplacé par les études de Bâle (NEJM 2018, Lancet 2019, NEJM 2023) ; bolus hypertonique aligné sur la recommandation européenne 2014 (150 mL en 20 min) ; clozapine présentée comme option et non comme seul traitement prouvé ; essai GLP-1 daté (2021) et chiffré.')
GRAD = T('gradient cortico-papillaire', 'Le gradient cortico-papillaire est la concentration croissante d’urée et de sel de la médullaire rénale ; il permet au rein de concentrer l’urine jusqu’à ≈ 1200 mOsm/kg.')
ODS = T('myélinolyse osmotique', 'La myélinolyse osmotique (démyélinisation osmotique) est une destruction de la myéline du tronc cérébral provoquée par une remontée trop rapide d’une hyponatrémie chronique.')
PTS = []

p1 = (P('La polydipsie primaire est un excès de boissons qui ne répond à aucun besoin de l’organisme. '
        'Le patient boit souvent plus de 3 L par jour ; la vasopressine (AVP) s’effondre et le rein élimine l’eau en surplus. '
        'La polyurie est donc la conséquence de la boisson, et non sa cause.', 31, 26) +
      F('Terminologie',
        TAB(['Terme', 'Définition exacte', 'À ne pas confondre avec'], [
         ['Polydipsie primaire', 'Apport d’eau excessif primitif, AVP freinée', 'Déficit en AVP (ancien diabète insipide central)'],
         ['Polydipsie psychogène', 'Forme liée à une maladie psychiatrique, surtout la schizophrénie', 'Potomanie à la bière (apport pauvre en solutés)'],
         ['Polydipsie « d’habitude »', 'Croyance qu’il faut boire beaucoup (sportifs, régimes)', 'Soif vraie'],
         ['Intoxication par l’eau', 'Hyponatrémie aiguë par apport supérieur à l’élimination rénale', 'Hyponatrémie chronique du syndrome de sécrétion inappropriée'],
         ['Polyurie hypotonique', 'Diurèse > 50 mL/kg/24 h et osmolalité urinaire < 800 mOsm/kg', 'Polyurie osmotique (glucose)'],
        ]), 26, 30))
PTS.append(POINT(1, 'Définition et sémantique', p1))

p2 = (P('Dans la cohorte internationale de 2018 (Suisse, Allemagne, Brésil), la polydipsie primaire représente 82 des 144 polyuries hypotoniques explorées (≈ 57 %). '
        'Elle est donc plus fréquente que le déficit en AVP dans les centres spécialisés. '
        'Chez les patients atteints de schizophrénie, une revue suisse rapporte 11–20 %.', 27, 31) +
      F('Chiffres, terrain et histoire naturelle',
        TAB(['Donnée', 'Valeur', 'Portée'], [
         ['Polyuries hypotoniques explorées (11 centres suisses, allemands et brésiliens, 2018)', 'Polydipsie primaire 57 %, déficit en AVP 41 %, résistance rénale 2 %', 'Population sélectionnée de centres experts'],
         ['Schizophrénie chronique', '11–20 %', 'Revue suisse 2017'],
         ['Autres terrains', 'Anxiété, troubles de la personnalité, sujets « adeptes de santé »', 'Fréquence non chiffrée'],
         ['Gravité', 'Intoxication par l’eau, parfois mortelle', 'Mortalité non chiffrée dans les sources'],
        ]) + P('Le facteur de risque principal est un trouble psychiatrique chronique ; le pronostic tient surtout aux épisodes d’hyponatrémie aiguë.', 31), 27))
PTS.append(POINT(2, 'Épidémiologie (Suisse, puis Europe)', p2))

p3 = (P('Boire en excès abaisse l’osmolalité plasmatique. Les osmorécepteurs de l’hypothalamus arrêtent alors la sécrétion d’AVP ; le tube collecteur devient imperméable à l’eau et l’urine se dilue. '
        'À la longue, ce flux d’urine « lave » le ' + GRAD + '. '
        'Le rein ne concentre alors plus bien, même avec de l’AVP : c’est ce qui trompait l’ancien test de restriction.', 26, 31) +
      F('Chaîne logique : de l’anatomie au traitement',
        TAB(['Étape', 'Ce qu’il faut comprendre'], [
         ['Anatomie', 'Osmorécepteurs de la lame terminale, noyaux supraoptiques et paraventriculaires, post-hypophyse, tube collecteur rénal.'],
         ['Physiologie', 'Pourquoi on cesse d’uriner la nuit : l’AVP monte quand l’osmolalité dépasse ≈ 285 mOsm/kg ; en dessous, elle est freinée.'],
         ['Physiopathologie', 'L’apport d’eau dépasse les besoins ; l’AVP est freinée ; le gradient médullaire se lave.'],
         ['Clinique', 'D’où une polyurie diluée, une natrémie basse-normale et, si l’apport dépasse l’élimination, une intoxication par l’eau.'],
         ['Examens', 'On mesure la copeptine (reflet de l’AVP) après stimulation, ce qui ne dépend pas du rein.'],
         ['Traitement', 'On réduit progressivement les boissons ; la desmopressine est dangereuse, car le patient continue à boire.'],
        ]), 26) +
      F('Mécanisme, exploration et cible thérapeutique',
        TAB(['Mécanisme', 'Exploration', 'Cible thérapeutique'], [
         ['Apport d’eau excessif', 'Carnet de boissons, poids', 'Réduction par paliers'],
         ['Freinage de l’AVP', 'Copeptine stimulée > 4,9 pmol/L (NaCl 3 %)', 'Aucune : la réponse hypophysaire est normale'],
         ['Lavage du gradient médullaire', 'Osmolalité urinaire maximale réduite', 'Se corrige en quelques semaines de boissons normales'],
         ['Élimination d’eau limitée (solutés bas, médicaments)', 'Natrémie, osmolalité urinaire', 'Arrêt des médicaments en cause'],
        ]), 31))
PTS.append(POINT(3, 'Physiopathologie', p3))

p4 = (P('Le défi est de distinguer la polydipsie primaire d’un déficit partiel en AVP, car leurs traitements s’opposent. '
        'La desmopressine soigne le déficit en AVP, mais elle provoque une hyponatrémie grave dans la polydipsie primaire. '
        'Le médecin écarte d’abord une polyurie osmotique (glycémie) et une hypercalcémie.', 26, 27) +
      DIFF('pp') +
      F('Diagnostic différentiel des polyuries hypotoniques (probabilités en exposant rouge, même population)',
        TAB(['Diagnostic', 'Éléments d’orientation', 'Examen discriminant'], [
         ['Polydipsie primaire' + PR('57 %', 27), 'Natrémie basse-normale, boissons fluctuantes, terrain psychiatrique', 'Copeptine stimulée > 4,9 pmol/L'],
         ['Déficit en AVP (central)' + PR('41 %', 27), 'Natrémie haute-normale, nycturie constante, début brutal', 'Copeptine stimulée ≤ 4,9 pmol/L'],
         ['Résistance rénale à la vasopressine' + PR('2 %', 27), 'Lithium, hypercalcémie, hypokaliémie', 'Copeptine basale ≥ 21,4 pmol/L'],
        ]) + P('Ces pourcentages concernent 144 patients adressés à des centres experts pour polyurie hypotonique.', 27)))
PTS.append(POINT(4, 'Raisonnement clinique et diagnostic différentiel', p4))

p5 = (P('L’anamnèse quantifie les boissons sur plusieurs jours. Elle cherche des volumes qui varient d’un jour à l’autre, une soif surtout diurne et un terrain psychiatrique. '
        'Un déficit en AVP réveille au contraire le patient chaque nuit.', 31, 26) +
      U('Drapeaux rouges : céphalées, nausées, vomissements, confusion, convulsions ou coma chez un grand buveur. Ils signent une intoxication par l’eau (natrémie souvent < 125 mmol/L) et imposent une hospitalisation immédiate.', 62, 31) +
      F('Questions ciblées et leur raison',
        TAB(['Question', 'Pourquoi la poser'], [
         ['Combien buvez-vous par jour, et cela varie-t-il ?', 'Des volumes fluctuants orientent vers une polydipsie primaire.'],
         ['Vous levez-vous la nuit pour boire ?', 'Une soif nocturne impérieuse évoque un déficit en AVP.'],
         ['Le début a-t-il été brutal ?', 'Un début brutal évoque une lésion hypophysaire.'],
         ['Avez-vous un suivi psychiatrique ?', 'La schizophrénie est le terrain principal.'],
         ['Prenez-vous un antidépresseur, de la carbamazépine, un thiazide ?', 'Ils limitent l’élimination d’eau et favorisent l’intoxication par l’eau.'],
         ['Avez-vous pris du poids dans la journée ?', 'Une prise de poids rapide signale une rétention d’eau.'],
        ]), 31, 62))
PTS.append(POINT(5, 'Anamnèse ciblée et drapeaux rouges', p5))

p6 = (P('Le patient est en général euvolémique. À l’état normal, la pression est stable, les muqueuses humides et il n’y a pas d’œdème. '
        'Les signes neurologiques ont une sensibilité faible pour une hyponatrémie légère ; seule la natrémie tranche.', 62, 31) +
      F('Signes, technique et valeur',
        TAB(['Signe', 'Technique', 'Ce qu’il signifie'], [
         ['Poids matin et soir', 'Même balance, même tenue', 'Gain > 2–3 kg dans la journée : rétention d’eau (seuil empirique)'],
         ['Pression et pouls couché puis debout', 'Mesure après 3 minutes', 'Normaux : euvolémie'],
         ['Vigilance, orientation', 'Score de Glasgow', 'Encéphalopathie hyponatrémique'],
         ['Démarche, équilibre', 'Marche en tandem', 'Ataxie de l’hyponatrémie'],
         ['Champ visuel', 'Confrontation', 'Lésion hypophysaire (diagnostic différentiel)'],
        ]), 62, 31))
PTS.append(POINT(6, 'Examen clinique', p6))

p7 = (P('Deux syndromes se suivent. Le syndrome polyuro-polydipsique hypotonique est chronique et bien toléré. '
        'Le syndrome d’intoxication par l’eau est aigu ; il menace la vie par œdème cérébral.', 31, 62) +
      F('Signes fonctionnels (symptômes rapportés)', UL(['Soif et boissons abondantes, surtout le jour', 'Mictions fréquentes et abondantes', 'Céphalées, nausées (hyponatrémie)', 'Crampes, fatigue']), 31) +
      F('Signes physiques (constatés à l’examen)', UL(['Euvolémie', 'Prise de poids rapide', 'Confusion, ataxie', 'Convulsions, coma (formes graves)']), 62) +
      F('Syndrome polyuro-polydipsique hypotonique',
        TAB(['Signe', 'Mécanisme', 'Valeur'], [
         ['Polyurie diluée', 'AVP freinée', 'Commune aux trois causes'],
         ['Natrémie basse-normale', 'Excès relatif d’eau', 'Oriente vers la polydipsie primaire'],
         ['Nycturie modérée', 'Moins de boissons la nuit', 'Peu spécifique'],
        ]), 26) +
      F('Syndrome d’intoxication par l’eau (encéphalopathie hyponatrémique)',
        TAB(['Signe', 'Mécanisme', 'Valeur'], [
         ['Céphalées, vomissements', 'Œdème cérébral', 'Signes précoces'],
         ['Confusion, convulsions', 'Hypertension intracrânienne', 'Urgence vitale'],
         ['Natrémie < 125 mmol/L en < 48 h', 'Apport > élimination rénale', 'Confirme l’intoxication'],
        ]), 62))
PTS.append(POINT(7, 'Syndromes et signes cliniques', p7))

p8 = (P('Aucune société savante n’a publié de critère formel. Le critère de référence vient de l’étude de 2018 : copeptine > 4,9 pmol/L quand la natrémie atteint ≥ 150 mmol/L sous NaCl 3 % (précision 96,5 %). '
        'Une recommandation de l’étude de 2019 propose, après arginine, un seuil > 3,8 pmol/L. '
        'Une natrémie basse ne suffit pas à elle seule.', 27, 29) +
      F('Seuils de copeptine (polyurie hypotonique)',
        TAB(['Test', 'Seuil', 'Interprétation'], [
         ['Copeptine basale', '≥ 21,4 pmol/L', 'Résistance rénale à l’AVP'],
         ['Après NaCl 3 % (natrémie ≥ 150 mmol/L)', '> 4,9 pmol/L', 'Polydipsie primaire'],
         ['Après NaCl 3 %', '≤ 4,9 pmol/L', 'Déficit en AVP'],
         ['Après arginine (60 min)', '> 3,8 pmol/L', 'Polydipsie primaire (moins précis)'],
        ]) + P('En comparaison directe, le test au NaCl 3 % est plus précis que l’arginine (96 % contre 74 %).', 4)))
PTS.append(POINT(8, 'Critères diagnostiques', p8))

p9 = (H4('9.a Examen de référence') +
      P('Le test au NaCl 3 % avec copeptine est la référence. Contre le déficit partiel en AVP, sa précision atteint 95 % contre 73 % pour l’épreuve de restriction hydrique. '
        'Sa sensibilité et sa spécificité dépassent 90 % dans l’étude de 2018.', 27) +
      H4('9.b Examens de première et de deuxième intention') +
      P('En première intention : diurèse des 24 heures, natrémie, osmolalités plasmatique et urinaire, glycémie, calcémie, kaliémie, créatinine et copeptine basale. '
        'En deuxième intention : test au NaCl 3 % (ou arginine), puis IRM hypophysaire si le déficit en AVP est retenu.', 26, 27) +
      TAB(['Intention', 'Examen', 'Pourquoi'], [
       ['1re', 'Diurèse des 24 heures et osmolalité urinaire', 'Confirme une polyurie hypotonique'],
       ['1re', 'Ionogramme et osmolalité plasmatique', 'Natrémie basse-normale en faveur de la polydipsie primaire'],
       ['1re', 'Glycémie, calcémie, kaliémie, créatinine', 'Écartent les polyuries osmotiques et rénales'],
       ['1re', 'Copeptine basale', 'Résistance rénale si ≥ 21,4 pmol/L'],
       ['2e', 'Test au NaCl 3 % avec copeptine', 'Sépare polydipsie primaire et déficit en AVP'],
       ['2e', 'IRM hypophysaire', 'Seulement si déficit en AVP'],
      ]) +
      H4('9.c Protocole du test au NaCl 3 %') +
      P('Indication : polyurie hypotonique avec copeptine basale < 21,4 pmol/L. Moment : le matin, en hôpital de jour, avec un médecin présent. '
        'Préparation : boissons libres la veille, puis à jeun ; pose de deux voies veineuses.', 27) +
      TAB(['Étape', 'Réalisation'], [
       ['Bolus', '250 mL de NaCl 3 % (513 mmol/L de sodium) en 15 minutes'],
       ['Perfusion', '0,15 mL/kg/min de NaCl 3 %'],
       ['Contrôle', 'Natrémie toutes les 30 minutes'],
       ['Prélèvement', 'Copeptine dès que la natrémie atteint ≥ 150 mmol/L'],
       ['Fin', 'Boire 30 mL/kg d’eau en 30 minutes et perfuser du glucose 5 % ; natrémie de contrôle'],
      ]) +
      H4('9.d Interprétation : positif, négatif, limite, discordant') +
      TAB(['Résultat', 'Signification', 'Conduite'], [
       ['Positif : copeptine > 4,9 pmol/L', 'Hypophyse normale : polydipsie primaire', 'Réduction des boissons, pas de desmopressine'],
       ['Négatif : copeptine ≤ 4,9 pmol/L', 'Déficit en AVP', 'IRM hypophysaire, voir DX.9'],
       ['Limite : copeptine proche de 4,9 pmol/L', 'Zone d’incertitude', 'Répéter ou compléter par l’arginine'],
       ['Discordant : natrémie basse et copeptine basse', 'Test interrompu avant la cible', 'Refaire le test jusqu’à la cible de natrémie'],
      ]) +
      H4('9.e Alternatives') +
      P('Grossesse : test au NaCl 3 % déconseillé, avis spécialisé. Enfant : test à l’arginine plus utilisé en pédiatrie. '
        'DFGe < 30 : interprétation difficile, avis néphrologique. L’IRM se fait sans produit iodé ; le gadolinium n’est pas nécessaire pour la post-hypophyse.', 29, 26))
PTS.append(POINT(9, 'Examens complémentaires', p9))

p10 = (P('Si la copeptine stimulée dépasse 4,9 pmol/L, le diagnostic est la polydipsie primaire. '
         'Le médecin explique alors que le rein et l’hypophyse fonctionnent, il proscrit la desmopressine et il oriente vers une réduction progressive des boissons.', 27, 31) +
       F('Arbre décisionnel : polyurie hypotonique',
         OL(['Natrémie < 125 mmol/L avec symptômes : urgence, NaCl 3 % (voir 11.B).',
             'Glycémie, calcémie, kaliémie anormales : traiter la cause.',
             'Copeptine basale ≥ 21,4 pmol/L : résistance rénale à l’AVP.',
             'Sinon, test au NaCl 3 % : > 4,9 pmol/L → polydipsie primaire ; ≤ 4,9 → déficit en AVP.',
             'Polydipsie primaire : réduction des boissons, avis psychiatrique si besoin, pas de desmopressine.']), 27, 62))
PTS.append(POINT(10, 'Arbre décisionnel', p10))

fiche = FICHE([
  ['Antipsychotique atypique : clozapine (Leponex®)', 'Antagoniste des récepteurs dopaminergiques D4 et sérotoninergiques de type 2A', 'Demi-vie ≈ 12 h ; métabolisme hépatique (cytochrome 1A2)', 'Titration progressive jusqu’à 200–450 mg/j ; durée prolongée', 'Agranulocytose, myocardite, constipation, sédation', 'Antécédent d’agranulocytose, myélosuppression', 'Fluvoxamine et ciprofloxacine (hausse), tabac (baisse)'],
  ['Soluté salé hypertonique : NaCl 3 %', 'Hausse rapide de l’osmolalité plasmatique', 'Effet immédiat', '150 mL IV en 20 min, à répéter 2 fois si besoin', 'Correction trop rapide, surcharge', 'Hyponatrémie chronique asymptomatique', 'Diurétiques (effet additif)'],
 ], 62, 31)
p11 = (H4('11.A Buts : d’abord l’urgence (intoxication par l’eau), car l’œdème cérébral tue en quelques heures') +
       P('Le traitement réduit les boissons à un volume normal, prévient les hyponatrémies et traite le trouble psychiatrique.', 31) +
       TAB(['But', 'Cible chiffrée'], [
        ['Boissons', '≈ 1,5–2,5 L/j, atteint par paliers'],
        ['Hausse de natrémie en urgence', '+5 mmol/L dans la première heure, ≤ 10 mmol/L par 24 h'],
        ['Natrémie de fond', '135–145 mmol/L'],
       ]) +
       H4('11.B Moyens et méthodes : forme compliquée en urgence, forme non compliquée en ambulatoire') +
       P('L’intoxication par l’eau compliquée (convulsions, coma) relève de l’urgence : 150 mL de NaCl 3 % IV en 20 minutes. '
         'On contrôle la natrémie et on répète le bolus jusqu’à un gain de 5 mmol par litre. '
         'Dès l’arrêt des boissons, le rein élimine beaucoup d’eau ; la natrémie peut alors remonter trop vite.', 62) +
       P('Si la natrémie monte de plus de 10 mmol/L en 24 heures, on donne de l’eau ou du glucose 5 % et parfois de la desmopressine, pour éviter une ' + ODS + '.', 62) +
       P('En ambulatoire, l’éducation est le premier traitement : carnet de boissons, bouteille graduée, réduction par paliers, glaçons ou bonbons sans sucre contre la bouche sèche, thérapie cognitivo-comportementale.', 31) +
       F('Traitements selon la situation',
         TAB(['Situation', 'Traitement', 'Pourquoi'], [
          ['Intoxication par l’eau grave', 'NaCl 3 % en bolus', 'Réduit l’œdème cérébral'],
          ['Intoxication par l’eau légère', 'Restriction des boissons, surveillance', 'Le rein élimine l’excès'],
          ['Polydipsie d’habitude', 'Éducation, réduction progressive', 'La croyance est la cause'],
          ['Schizophrénie avec polydipsie', 'Revoir l’antipsychotique ; clozapine possible', 'Séries de cas favorables'],
         ]), 31, 62) +
       fiche +
       F('Situations particulières',
         TAB(['Situation', 'Particularité'], [
          ['Grossesse', 'Natrémie physiologiquement plus basse (≈ 4–5 mmol/L) ; avis spécialisé'],
          ['Personne âgée', 'Capacité d’élimination d’eau réduite : intoxication plus facile'],
          ['Enfant', 'Polydipsie d’habitude fréquente ; même démarche'],
          ['Insuffisance rénale (DFGe < 30)', 'Élimination d’eau limitée : risque accru'],
          ['Insuffisance hépatique', 'Clozapine à éviter ou à doser prudemment'],
         ]), 31, 55) +
       SOCIAL('Un arrêt de travail est surtout nécessaire après une intoxication par l’eau (quelques jours, durée non chiffrée dans les sources).',
              'La conduite est contre-indiquée après des convulsions, selon les règles de l’OAC (annexe 1).',
              'La prise en charge psychiatrique est couverte par la LAMal ; l’assurance-invalidité (AI) intervient seulement si la maladie psychiatrique limite durablement la capacité de travail.') +
       H4('11.C Surveillance et critères de sortie') +
       TAB(['Quand', 'Quoi'], [
        ['Toutes les 2–4 heures après une intoxication par l’eau', 'Natrémie et diurèse ; arrêt du NaCl 3 % dès +5 mmol/L ou disparition des symptômes'],
        ['Chaque jour, matin et soir', 'Poids (patients psychiatriques à risque)'],
        ['À 1 mois', 'Natrémie, osmolalité urinaire (le gradient se reconstitue)'],
        ['Critères de sortie', 'Natrémie stable > 130 mmol/L, conscience normale, plan de boissons écrit, suivi psychiatrique organisé'],
       ]) +
       H4('11.D Pronostic et recherche 2026') +
       P('Le pronostic rénal est bon dès que les boissons redeviennent normales. Le risque vital tient aux intoxications par l’eau. '
         'Dans un essai bâlois de 2021, le dulaglutide (Trulicity®) a réduit les boissons de 490 mL sur 8 heures (−17 %) ; ce traitement reste expérimental.', 31, 77))
PTS.append(POINT(11, 'Prise en charge', p11))

p12 = (P('La prévention protège la capacité du rein à éliminer l’eau. Chez un patient connu, on évite si possible les thiazides, les antidépresseurs inhibiteurs sélectifs de la recapture de la sérotonine (ISRS), la carbamazépine (Tegretol®) et l’ecstasy (MDMA, méthylène-dioxy-métamphétamine). '
         'Une pesée quotidienne repère tôt la rétention d’eau.', 31, 62) +
       F('Prévention primaire, secondaire et tertiaire',
         TAB(['Niveau', 'Mesure'], [
          ['Primaire', 'Information sur les volumes de boissons utiles, notamment chez les sportifs'],
          ['Secondaire', 'Natrémie lors de toute confusion chez un patient psychiatrique ; test à la copeptine avant toute desmopressine'],
          ['Tertiaire', 'Plan de boissons, pesée, revue des médicaments, suivi psychiatrique'],
         ]) + P('En Suisse, les recommandations de l’étude bâloise ont fait du test au NaCl 3 % la référence avant de traiter une polyurie.', 27, 4)))
PTS.append(POINT(12, 'Prévention', p12))

PTS.append(POINT(13, 'Points clés',
 P('La polydipsie primaire est la cause la plus fréquente de polyurie hypotonique en centre expert. '
   'Une copeptine > 4,9 pmol/L sous NaCl 3 % la confirme. '
   'La desmopressine y est dangereuse, car le patient continue à boire. '
   'L’intoxication par l’eau grave se traite par 150 mL de NaCl 3 % en 20 minutes.', 27, 62)))

PTS.append(POINT(14, 'Pièges d’examen',
 TAB(['Piège', 'Ce qu’il faut répondre'], [
  ['Donner de la desmopressine « à l’essai »', 'Faute grave : hyponatrémie et coma en 24 heures si le patient continue à boire'],
  ['Conclure à un déficit partiel en AVP sur une épreuve de restriction', 'Le lavage du gradient fausse ce test ; faire le test au NaCl 3 %'],
  ['Oublier la remontée trop rapide après arrêt des boissons', 'Surveiller la natrémie toutes les 2–4 heures ; freiner si > 10 mmol/L par 24 h'],
  ['Natrémie basse = déficit en AVP', 'Non : elle oriente vers la polydipsie primaire'],
 ]) + P('Une natrémie de base > 143 mmol/L oriente plutôt vers un déficit en AVP, mais ce repère ne remplace pas la copeptine.', 26, 27)))

CTX = {'_prefixe': 'Dans la polydipsie primaire',
 'copeptine': 'Une copeptine > 4,9 pmol/L sous NaCl 3 % (natrémie ≥ 150 mmol/L) confirme la polydipsie primaire.',
 'restriction': 'L’épreuve de restriction hydrique se trompe souvent ici, car le gradient médullaire est lavé.',
 'osmo': 'Une osmolalité urinaire basse avec osmolalité plasmatique basse-normale oriente vers la polydipsie primaire.',
 'iono': 'Une natrémie basse-normale oriente vers la polydipsie primaire ; < 125 mmol/L avec symptômes impose l’urgence.',
 'gly': 'Une glycémie normale écarte une polyurie osmotique.',
 'creat': 'Une créatinine normale écarte une polyurie d’origine rénale.',
 'irm': 'L’IRM hypophysaire ne se fait que si le test conclut à un déficit en AVP.',
 'nfs': 'Sous clozapine, la formule sanguine se contrôle chaque semaine les 18 premières semaines.'}
if __name__ == '__main__':
    produire(M, PTS, SOURCES, CTX)
