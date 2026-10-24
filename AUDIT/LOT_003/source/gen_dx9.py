# -*- coding: utf-8 -*-
"""DX.9 — Déficit en arginine-vasopressine (AVP-D, ancien diabète insipide central). LOT 3, V5 → V7 AUDITÉ."""
from lot3_commun import *
POINT = mkPOINT('dx9')
M = META('dx9', 'DX.9', 'Déficit en vasopressine (AVP-D)', 'Déficit en arginine-vasopressine (AVP-D, ancien diabète insipide central)',
         'LOT_003_DX9_Deficit_vasopressine_AVP_D_AUDITÉ.html',
         'Corrections : prévalence « en Suisse » requalifiée (donnée internationale) ; mécanisme du masquage par le déficit en cortisol corrigé ; volumes « 6–10 L » et prolactine « 30–150 µg/L » retirés (non sourcés) ; seuil de copeptine < 2,6 pmol/L retiré de l’algorithme ; Nocutil® retiré ; hyponatrémie sous desmopressine sourcée (27 %, 2015) ; travaux sur l’ocytocine datés de 2023 et non de 2026 ; délai « choc mortel en 12–24 h » retiré.')
COP = T('copeptine', 'La copeptine est le fragment terminal du précurseur de la vasopressine ; elle est libérée en quantité égale et reste stable dans le tube.')
PTS = []

p1 = (P('Le déficit en arginine-vasopressine (AVP-D), ancien diabète insipide central, est un manque de sécrétion de vasopressine par l’hypothalamus ou la post-hypophyse. '
        'Le rein ne retient plus l’eau, ce qui entraîne une polyurie hypotonique et une soif intense. '
        'Le nom a changé en 2022 pour éviter la confusion avec le diabète sucré.', 30, 26) +
      F('Terminologie',
        TAB(['Terme', 'Définition exacte', 'À ne pas confondre avec'], [
         ['AVP-D', 'Déficit de sécrétion de vasopressine, complet ou partiel', 'AVP-R : résistance rénale à la vasopressine'],
         ['Polydipsie primaire', 'Apport d’eau excessif, vasopressine freinée', 'AVP-D partiel'],
         ['Forme adipsique', 'AVP-D avec perte de la soif', 'AVP-D simple (soif conservée)'],
         ['Réponse triphasique', 'Polyurie, puis antidiurèse, puis polyurie après chirurgie de la tige', 'Polyurie postopératoire banale (perfusions)'],
        ]), 30, 26))
PTS.append(POINT(1, 'Définition et sémantique', p1))

p2 = (P('Aucune donnée suisse publiée n’a été trouvée. '
        'Selon les revues européennes et internationales, la prévalence de l’AVP-D est ≈ 1 / 25 000, soit ≈ 4 / 100 000 ; les deux sexes sont touchés à tout âge. '
        'Dans l’étude multicentrique de 2018 (Suisse, Allemagne, Brésil), l’AVP-D représente 41 % (59/144) des patients polyuriques explorés, contre 57 % pour la polydipsie primaire.', 26, 27) +
      F('Chiffres, terrain et histoire naturelle',
        TAB(['Donnée', 'Valeur', 'Population'], [
         ['Prévalence de l’AVP-D', '≈ 4 / 100 000', 'Population générale'],
         ['AVP-D parmi les polyuries explorées', '41 % (59/144)', 'Patients adressés en centre'],
         ['Hyponatrémie ≤ 134 mmol/L sous desmopressine', '27 %', 'Patients traités suivis au long cours'],
         ['Hyponatrémie signalée par les patients', '22 %', 'Enquête internationale de 2022'],
        ]) + P('Le terrain comprend la chirurgie hypophysaire, le traumatisme crânien et les maladies infiltratives ; la mortalité vient surtout des dysnatrémies et du déficit corticotrope associé.', 26, 91, 92)))
PTS.append(POINT(2, 'Épidémiologie (Suisse, puis Europe)', p2))

p3 = (P('Les neurones des noyaux supra-optiques et paraventriculaires fabriquent la vasopressine ; elle descend dans la tige et se stocke dans la post-hypophyse. '
        'La vasopressine se fixe au récepteur V2 du tube collecteur ; l’aquaporine 2 s’insère alors dans la membrane apicale. '
        'Leur perte entraîne la polyurie ; il faut perdre ≈ 80 % de ces neurones pour qu’un AVP-D permanent apparaisse.', 26) +
      F('Chaîne logique : de l’anatomie au traitement',
        TAB(['Étape', 'Ce qu’il faut comprendre'], [
         ['Anatomie', 'Noyaux supra-optiques et paraventriculaires, tige pituitaire, post-hypophyse, chiasma juste au-dessus.'],
         ['Physiologie', 'Pourquoi l’urine se concentre la nuit : la vasopressine ouvre les aquaporines 2.'],
         ['Physiopathologie', 'Sans vasopressine, le tube collecteur reste imperméable ; l’eau part dans l’urine.'],
         ['Clinique', 'D’où la polyurie hypotonique, la nycturie et la soif d’eau froide.'],
         ['Examens', 'On mesure la copeptine stimulée, puis l’IRM cherche la cause.'],
         ['Traitement', 'On remplace l’hormone par la desmopressine et on traite la cause.'],
        ]), 26) +
      F('Réponse triphasique et masquage par le déficit en cortisol',
        TAB(['Phase', 'Mécanisme', 'Danger'], [
         ['1. Polyurie (premiers jours)', 'Sidération des axones', 'Hypernatrémie si la soif ou l’accès à l’eau manquent'],
         ['2. Antidiurèse (vers la 2e semaine)', 'Les terminaisons lésées libèrent leur stock', 'Hyponatrémie si la desmopressine continue'],
         ['3. Polyurie permanente', 'Perte définitive des neurones', 'Traitement à vie'],
         ['Déficit en cortisol associé', 'Le déficit en cortisol réduit l’excrétion de l’eau libre', 'La polyurie apparaît sous hydrocortisone'],
        ]) + P('La réponse triphasique complète est rare ; sa fréquence varie selon les séries.', 5, 26)) +
      F('Mécanisme, exploration et cible thérapeutique',
        TAB(['Mécanisme', 'Exploration', 'Cible thérapeutique'], [
         ['Déficit de vasopressine', 'Copeptine stimulée', 'Desmopressine'],
         ['Lésion de la tige ou de l’hypothalamus', 'IRM hypothalamo-hypophysaire', 'Traitement de la cause'],
         ['Déficit antéhypophysaire', 'Cortisol, TSH et T4 libre, gonadotrophines', 'Hydrocortisone d’abord, puis lévothyroxine'],
         ['Déficit en ocytocine possible', 'Recherche (test à la MDMA)', 'Essais en cours'],
        ]), 26, 93))
PTS.append(POINT(3, 'Physiopathologie', p3))

p4 = (P('Le clinicien cherche d’abord l’urgence : hypernatrémie, perte de la soif, accès à l’eau impossible. '
        'Puis il confirme l’AVP-D par la copeptine et le distingue de la polydipsie primaire et de l’AVP-R. '
        'Enfin, l’IRM cherche la cause.', 26, 27) +
      DIFF('avpd') +
      F('Polyurie hypotonique explorée (même population : 144 patients de l’étude de 2018 ; probabilités en exposant rouge)',
        TAB(['Diagnostic', 'Copeptine', 'Indice décisif'], [
         ['AVP-D' + PR('41 %', 27), 'Stimulée ≤ 4,9 pmol/L', 'IRM : hypersignal post-hypophysaire absent'],
         ['Polydipsie primaire' + PR('57 %', 27), 'Stimulée > 4,9 pmol/L', 'Trouble psychiatrique fréquent'],
         ['AVP-R' + PR('2 %', 27), 'Basale ≥ 21,4 pmol/L', 'Lithium, hypercalcémie'],
        ]) + P('Les causes d’AVP-D comprennent chirurgie, traumatisme, craniopharyngiome, germinome, métastase, histiocytose, sarcoïdose et hypophysite.', 26)))
PTS.append(POINT(4, 'Raisonnement clinique et diagnostic différentiel', p4))

p5 = (P('L’anamnèse retrouve un début brutal, une préférence pour l’eau froide et une nycturie fréquente.', 26) +
      U('Drapeaux rouges : céphalées et baisse du champ visuel, signes d’insuffisance antéhypophysaire, hypernatrémie, perte de la soif, patient sans accès à l’eau. Ils imposent une hospitalisation immédiate.', 26, 5) +
      F('Questions ciblées et leur raison',
        TAB(['Question', 'Pourquoi la poser'], [
         ['Vous souvenez-vous du jour où cela a commencé ?', 'Un début net évoque un AVP-D.'],
         ['Préférez-vous l’eau très froide ?', 'Signe fréquent de l’AVP-D.'],
         ['Avez-vous des maux de tête ou voyez-vous moins sur les côtés ?', 'Lésion proche du chiasma.'],
         ['Êtes-vous très fatigué, frileux, vos règles ont-elles cessé ?', 'Déficit antéhypophysaire.'],
         ['Avez-vous eu une opération ou un choc à la tête ?', 'Cause fréquente.'],
         ['Recevez-vous une immunothérapie contre un cancer ?', 'Hypophysite, rarement avec AVP-D.'],
        ]), 26))
PTS.append(POINT(5, 'Anamnèse ciblée et drapeaux rouges', p5))

p6 = (P('L’examen teste le champ visuel par confrontation ; à l’état normal, les deux hémichamps temporaux sont vus. '
        'La confrontation a une sensibilité faible ; la périmétrie automatisée la complète. '
        'Il cherche aussi des signes de déficit antéhypophysaire et d’histiocytose.', 26) +
      F('Signes, technique et valeur',
        TAB(['Signe', 'Technique', 'Ce qu’il signifie'], [
         ['Hémianopsie bitemporale', 'Confrontation, puis périmétrie', 'Compression du chiasma'],
         ['Paralysie des nerfs III, IV, VI', 'Oculomotricité', 'Atteinte du sinus caverneux'],
         ['Pâleur, dépilation, hypotension orthostatique', 'Inspection, pression debout', 'Déficit antéhypophysaire'],
         ['Lésions cutanées ou osseuses', 'Inspection, palpation du crâne', 'Histiocytose langerhansienne'],
         ['Muqueuses sèches', 'Inspection', 'Déshydratation'],
        ]), 26))
PTS.append(POINT(6, 'Examen clinique', p6))

p7 = (P('Deux syndromes coexistent souvent. Le syndrome polyuro-polydipsique hypotonique traduit le déficit en vasopressine. '
        'Le syndrome de la région hypothalamo-hypophysaire traduit la lésion qui l’a causé.', 26) +
      F('Signes fonctionnels (symptômes rapportés)', UL(['Polyurie, nycturie', 'Soif d’eau froide', 'Céphalées', 'Fatigue, frilosité']), 26) +
      F('Signes physiques (constatés à l’examen)', UL(['Hémianopsie bitemporale', 'Signes de déshydratation', 'Signes de déficit antéhypophysaire']), 26) +
      F('Syndrome polyuro-polydipsique hypotonique',
        TAB(['Signe', 'Mécanisme', 'Valeur'], [
         ['Diurèse > 50 mL/kg/24 h', 'Absence de vasopressine', 'Définit la polyurie'],
         ['Osmolalité urinaire < 300 mOsm/kg', 'Urine non concentrée', 'Hypotonique'],
         ['Natrémie haute-normale', 'Perte d’eau compensée par la soif', 'Oriente vers l’AVP-D'],
        ]), 26, 3) +
      F('Syndrome de la région hypothalamo-hypophysaire',
        TAB(['Signe', 'Mécanisme', 'Valeur'], [
         ['Hémianopsie bitemporale', 'Compression du chiasma', 'Masse suprasellaire'],
         ['Prolactine modérément élevée', 'Section du frein dopaminergique par la lésion de la tige', 'Atteinte de la tige'],
         ['Déficits antéhypophysaires', 'Lésion de l’hypophyse ou de la tige', 'Bilan hormonal'],
        ]), 26))
PTS.append(POINT(7, 'Syndromes et signes cliniques', p7))

p8 = (P('Le critère repose sur la copeptine, selon la recommandation européenne et les études de Bâle. '
        'Après NaCl 3 % jusqu’à une natrémie ≥ 150 mmol/L, une copeptine ≤ 4,9 pmol/L signe l’AVP-D. '
        'Une polyurie seule ne suffit pas : il faut prouver qu’elle est hypotonique.', 27, 3) +
      F('Seuils de copeptine (consensus de 2025 et études de 2015–2023)',
        TAB(['Situation', 'Seuil', 'Diagnostic et performance'], [
         ['Hypernatrémie spontanée (≥ 147 mmol/L), urine hypotonique', 'Copeptine ≤ 4,9 pmol/L', 'AVP-D, sans test de stimulation'],
         ['Copeptine basale', '≥ 21,4 pmol/L', 'AVP-R ; sensibilité et spécificité 100 % (2015)'],
         ['NaCl 3 %, natrémie ≥ 150 mmol/L', '≤ 4,9 pmol/L', 'AVP-D ; précision 96,5 % (2018)'],
         ['Arginine 0,5 g/kg en 30 min, dosage à 60 min', '≤ 3,8 pmol/L', 'AVP-D ; précision 93 % (2019)'],
        ]) + P('En 2023, la précision de l’arginine est inférieure à celle du NaCl 3 % (74 % contre 96 %).', 28, 27, 29, 4)))
PTS.append(POINT(8, 'Critères diagnostiques', p8))

p9 = (H4('9.a Examen de référence') +
      P('La référence biologique est la ' + COP + ' après NaCl 3 % ; au seuil de 4,9 pmol/L, sa sensibilité et sa spécificité dépassent 90 %. '
        'La référence étiologique est l’IRM hypothalamo-hypophysaire en coupes fines, avant et après gadolinium.', 27, 26) +
      H4('9.b Examens de première et de deuxième intention') +
      P('En première intention : natrémie, osmolalités plasmatique et urinaire, glycémie, calcium, potassium et créatinine. '
        'En deuxième intention : copeptine stimulée, puis IRM et bilan antéhypophysaire à 8 h.', 3, 26) +
      TAB(['Intention', 'Examen', 'Pourquoi'], [
       ['1re', 'Natrémie, osmolalités', 'Polyurie hypotonique'],
       ['1re', 'Glycémie, calcium, potassium', 'Exclure une diurèse osmotique ou une AVP-R'],
       ['2e', 'Copeptine stimulée', 'Distinguer AVP-D et polydipsie primaire'],
       ['2e', 'IRM', 'Cause : tige épaissie, masse'],
       ['2e', 'Cortisol à 8 h, TSH avec T4 libre, LH, FSH, prolactine, IGF-1', 'Déficits associés ; la TSH seule est trompeuse'],
       ['2e, tige épaissie avant 35 ans', 'Alpha-fœtoprotéine et hCG (sang, liquide céphalorachidien)', 'Germinome'],
      ]) +
      H4('9.c Prescription et calculs') +
      P('Indication : polyurie hypotonique > 50 mL/kg/24 h. Moment : test le matin, à l’hôpital, natrémie toutes les 30 min. '
        'Préparation : arrêt de la desmopressine 24 h avant ; pas de NaCl 3 % si épilepsie ou insuffisance cardiaque.', 27, 3) +
      TAB(['Calcul', 'Formule', 'Seuil'], [
       ['Débit de NaCl 3 %', 'Bolus 250 mL, puis 0,15 mL/kg/min', 'Arrêt quand la natrémie est ≥ 150 mmol/L'],
       ['Polyurie', 'Diurèse / poids', '> 50 mL/kg/24 h'],
       ['Osmolalité urinaire', 'Mesurée', '< 300 mOsm/kg : hypotonique'],
      ]) +
      H4('9.d Interprétation : positif, négatif, limite, discordant') +
      TAB(['Résultat', 'Signification', 'Conduite'], [
       ['Positif : copeptine stimulée ≤ 4,9 pmol/L', 'AVP-D', 'IRM, bilan hormonal, desmopressine'],
       ['Négatif : > 4,9 pmol/L', 'Polydipsie primaire', 'Réduction des apports'],
       ['Limite : 4–6 pmol/L', 'Zone d’incertitude', 'Répéter ou essai thérapeutique encadré'],
       ['Discordant : copeptine basse, IRM normale', 'AVP-D idiopathique possible', 'IRM de contrôle'],
      ]) +
      H4('9.e Alternatives') +
      P('Grossesse : la vasopressinase placentaire peut causer un AVP-D transitoire ; IRM sans gadolinium. Enfant : test de restriction hydrique encadré. '
        'DFGe bas : interpréter la copeptine avec prudence. Le scanner avec iode ne sert que si l’IRM est impossible.', 26))
PTS.append(POINT(9, 'Examens complémentaires', p9))

p10 = (P('Si la copeptine confirme l’AVP-D, alors le médecin dose le cortisol avant tout, car l’hormone thyroïdienne seule peut déclencher une insuffisance surrénalienne aiguë. '
         'L’IRM oriente ensuite vers la cause.', 26) +
       F('Arbre décisionnel de l’AVP-D',
         OL(['Hypernatrémie, perte de la soif : urgence, hospitalisation.',
             'Polyurie hypotonique confirmée : copeptine (basale, puis stimulée).',
             'AVP-D : bilan antéhypophysaire ; hydrocortisone d’abord si déficit.',
             'IRM : masse, tige épaissie ou normale ; marqueurs du germinome si tige épaissie chez le jeune.',
             'Desmopressine le soir, titrée sur la nycturie et la natrémie.']), 26, 27))
PTS.append(POINT(10, 'Arbre décisionnel', p10))

fiche = FICHE([
  ['Analogue V2 : desmopressine (Minirin®, Minirin® Melt)', 'Agoniste sélectif du récepteur V2 ; pas d’effet vasoconstricteur', 'Demi-vie ≈ 2–3 h ; action 6–12 h', 'Melt 60–120 µg au coucher, puis 2–3 prises/j ; comprimés 0,1–0,2 mg 2–3 fois/j ; injectable selon l’AIPS ; à vie si permanent', 'Hyponatrémie, céphalées', 'Polydipsie primaire, hyponatrémie', 'AINS, carbamazépine, ISRS (hyponatrémie)'],
  ['Glucocorticoïde : hydrocortisone', 'Remplace le cortisol', 'Demi-vie ≈ 1,5 h', '15–25 mg/j en 2–3 prises si déficit corticotrope', 'Prise de poids, glycémie haute', 'Aucune en substitution', 'Inducteurs du CYP3A4'],
 ], 26, 55)
p11 = (H4('11.A Buts : d’abord l’urgence (hypernatrémie, patient sans accès à l’eau), car elle menace le cerveau en quelques heures') +
       P('Le traitement supprime la nycturie, garde une diurèse de 1,5–2,5 L/24 h et évite l’hyponatrémie.', 26) +
       TAB(['But', 'Cible chiffrée'], [
        ['Natrémie', '135–145 mmol/L'],
        ['Diurèse', '1,5–2,5 L/24 h'],
        ['Nycturie', '0–1 lever'],
       ]) +
       H4('11.B Moyens et méthodes : forme compliquée en urgence, forme non compliquée en ambulatoire') +
       P('La forme compliquée relève de l’urgence : desmopressine parentérale, natrémie toutes les 4–6 h, bilan entrées-sorties. '
         'À l’hôpital, la desmopressine ne doit jamais être omise chez un patient à jeun.', 5) +
       P('En ambulatoire, l’éducation enseigne à boire selon la soif et à retarder une prise 1 fois par semaine pour laisser une diurèse libre ; cet échappement réduit l’hyponatrémie.', 26, 92) +
       F('Traitements selon la situation',
         TAB(['Situation', 'Traitement', 'Pourquoi'], [
          ['AVP-D permanent', 'Desmopressine', 'Remplace l’hormone'],
          ['Déficit corticotrope associé', 'Hydrocortisone avant toute lévothyroxine', 'Évite une crise surrénalienne'],
          ['Après chirurgie hypophysaire', 'Desmopressine à la demande, pas à heure fixe', 'Risque de la phase 2'],
          ['Forme adipsique', 'Apport d’eau fixe, pesée quotidienne', 'La soif ne protège plus'],
          ['Germinome, histiocytose', 'Traitement oncologique', 'La cause est traitable'],
         ]), 26, 5) +
       fiche +
       F('Situations particulières',
         TAB(['Situation', 'Particularité'], [
          ['Grossesse', 'Desmopressine possible ; elle résiste à la vasopressinase'],
          ['Personne âgée', 'Doses plus faibles ; hyponatrémie plus fréquente'],
          ['Enfant', 'Surveillance du poids et de la natrémie'],
          ['Insuffisance rénale (DFGe < 50)', 'Desmopressine éliminée par le rein : doses réduites'],
          ['Insuffisance hépatique', 'Pas d’adaptation connue'],
         ]), 26, 55) +
       SOCIAL('Un arrêt de travail court suffit souvent après l’ajustement du traitement (durée non chiffrée dans les sources).',
              'La conduite est possible si le traitement est stable et le champ visuel normal (OAC, annexe 1).') +
       H4('11.C Surveillance et critères de sortie') +
       TAB(['Quand', 'Quoi'], [
        ['J3, J7, puis 1 mois', 'Natrémie après l’instauration'],
        ['Tous les 3–6 mois', 'Natrémie, symptômes'],
        ['Tous les 3–6 mois pendant 2–3 ans', 'IRM si tige épaissie isolée chez le jeune'],
        ['Critères de sortie', 'Natrémie stable, nycturie contrôlée, carte d’urgence remise, éducation faite'],
       ]) +
       H4('11.D Pronostic et recherche 2026') +
       P('L’AVP-D permanent ne guérit pas, mais la desmopressine le contrôle. '
         'En 2023, l’équipe de Bâle a montré un déficit en ocytocine chez les patients AVP-D ; en 2026, des essais évaluent l’ocytocine, sans bénéfice établi.', 26, 93))
PTS.append(POINT(11, 'Prise en charge', p11))

p12 = (P('À l’hôpital, la desmopressine est maintenue, avec bilan entrées-sorties et natrémie toutes les 4–6 h, car son omission provoque une hypernatrémie grave. '
         'Une carte d’urgence aide le personnel.', 5, 92) +
       F('Prévention primaire, secondaire et tertiaire',
         TAB(['Niveau', 'Mesure'], [
          ['Primaire', 'Surveiller la diurèse après chirurgie hypophysaire ou traumatisme crânien'],
          ['Secondaire', 'Copeptine devant une polyurie hypotonique'],
          ['Tertiaire', 'Échappement hebdomadaire, natrémie régulière, carte d’urgence'],
         ]) + P('En Suisse, l’OFSP et la SSED n’ont pas de programme dédié ; le centre de Bâle est une référence pour le test à la copeptine.', 27)))
PTS.append(POINT(12, 'Prévention', p12))

PTS.append(POINT(13, 'Points clés',
 P('L’AVP-D est l’ancien diabète insipide central. '
   'La copeptine stimulée par NaCl 3 % pose le diagnostic. '
   'Le cortisol se remplace avant l’hormone thyroïdienne. '
   'La desmopressine expose à l’hyponatrémie ; l’échappement hebdomadaire la prévient.', 30, 27, 91)))

PTS.append(POINT(14, 'Pièges d’examen',
 TAB(['Piège', 'Ce qu’il faut répondre'], [
  ['Attribuer un AVP-D à un adénome hypophysaire non opéré', 'Rare : penser craniopharyngiome, germinome, métastase, hypophysite'],
  ['Donner la desmopressine à heure fixe après chirurgie', 'Risque d’hyponatrémie en phase 2'],
  ['Confondre diabète insipide et diabète sucré', 'D’où le nouveau nom AVP-D'],
  ['Bloquer les urines en permanence', 'Laisser un échappement hebdomadaire'],
 ]) + P('Ces réponses suivent la revue de 2019 et la prise de position de 2022.', 26, 30)))

CTX = {'_prefixe': 'Devant une polyurie hypotonique',
 'copeptine': 'Une copeptine stimulée ≤ 4,9 pmol/L après NaCl 3 % signe l’AVP-D (précision 96,5 %).',
 'osmo': 'Une osmolalité urinaire < 300 mOsm/kg confirme la polyurie hypotonique.',
 'iono': 'La natrémie se contrôle à J3, J7 et 1 mois après le début de la desmopressine.',
 'irm': 'L’IRM cherche l’absence d’hypersignal post-hypophysaire et un épaississement de la tige.',
 'cort': 'Un cortisol bas à 8 h impose l’hydrocortisone avant la lévothyroxine.',
 'tsh': 'La TSH seule est trompeuse dans l’atteinte hypophysaire : doser la T4 libre.',
 't4t3': 'Une T4 libre basse avec TSH normale signe une hypothyroïdie centrale.',
 'prl': 'Une prolactine modérément élevée évoque une atteinte de la tige.',
 'hcg': 'Une hCG élevée dans le sang ou le liquide céphalorachidien évoque un germinome.'}
if __name__ == '__main__':
    produire(M, PTS, SOURCES, CTX)
