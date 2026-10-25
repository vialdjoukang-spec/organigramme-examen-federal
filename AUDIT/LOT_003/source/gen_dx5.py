# -*- coding: utf-8 -*-
"""DX.5 — Polyurie et polydipsie iatrogènes. LOT 3, V5 → V7 AUDITÉ."""
from lot3_commun import *
POINT = mkPOINT('dx5')
M = META('dx5', 'DX.5', 'Polyurie iatrogène', 'Polyurie et polydipsie iatrogènes (gliflozines, diurétiques, vaptans, osmoles)',
         'LOT_003_DX5_Polyurie_iatrogene_AUDITÉ.html',
         'Corrections majeures : « 3 % des consultations » et « l’hygiène divise par trois les mycoses » retirés faute de source ; fréquences des effets des gliflozines tirées de l’essai de 2015 ; seuil de fraction d’excrétion de l’urée sourcé (Carvounis 2002) ; arrêt préopératoire des gliflozines aligné sur l’ADA 2025.')
FEU = T('fraction d’excrétion de l’urée', 'La fraction d’excrétion de l’urée (FEUrée) est la part de l’urée filtrée qui passe dans l’urine ; contrairement au sodium, elle varie peu sous diurétique.')
AQ = T('aquarèse', 'L’aquarèse est une élimination d’eau libre sans sel, obtenue en bloquant le récepteur V2 de la vasopressine.')
PTS = []

p1 = (P('Une polyurie iatrogène est une diurèse > 3 L/24 h causée par un médicament. '
        'Le médicament fait perdre au rein du glucose (gliflozines), du sel (diurétiques), une osmole non réabsorbée (mannitol) ou de l’eau libre (vaptans). '
        'La soif suit la perte d’eau : elle compense, elle n’est pas la cause.', 78, 54) +
      F('Terminologie',
        TAB(['Terme', 'Définition exacte', 'À ne pas confondre avec'], [
         ['Diurèse osmotique', 'Eau entraînée par un soluté non réabsorbé (glucose, mannitol, urée)', 'Diurèse aqueuse (eau sans soluté)'],
         ['Natriurèse', 'Excrétion urinaire de sodium', 'Diurèse (volume d’urine)'],
         ['Aquarèse', 'Excrétion d’eau libre seule', 'Diurèse saline des diurétiques'],
         ['Gliflozine', 'Inhibiteur du cotransporteur sodium-glucose de type 2 (SGLT2)', 'Glinide (sécrétagogue de l’insuline)'],
         ['Acidocétose euglycémique', 'Acidocétose avec glycémie < 11,1 mmol/L', 'Cétose de jeûne simple'],
        ]), 7, 78))
PTS.append(POINT(1, 'Définition et sémantique', p1))

p2 = (P('Les gliflozines sont recommandées dans le diabète de type 2, l’insuffisance cardiaque et la maladie rénale chronique ; leur usage augmente donc en Suisse. '
        'Aucune fréquence suisse de polyurie iatrogène n’est publiée ; le « 3 % des consultations » de l’original a été retiré. '
        'Dans l’essai international de l’empagliflozine publié en 2015, l’empagliflozine provoque une infection génitale chez 6,4 % des patients, contre 1,8 % sous placebo.', 19, 79) +
      F('Chiffres, terrain et histoire naturelle',
        TAB(['Donnée', 'Valeur', 'Portée'], [
         ['Glycosurie sous gliflozine', '≈ 60–80 g de glucose par jour', 'Effet attendu'],
         ['Hausse de diurèse sous gliflozine', 'Quelques centaines de mL par jour, surtout les premiers jours', 'Souvent transitoire'],
         ['Infection génitale (essai de 2015)', '6,4 % contre 1,8 % (placebo)', 'Essai européen et mondial'],
         ['Déplétion volémique (essai de 2015)', '5,1 % contre 4,9 %', 'Plus fréquente chez l’âgé sous diurétique'],
         ['Acidocétose (essai de 2015)', '≈ 0,1 % des patients', 'Rare mais grave'],
         ['Terrain à risque', 'Âge > 75 ans, diurétique de l’anse associé, jeûne, chirurgie', 'Mortalité non chiffrée dans les sources'],
        ]) + P('Le pronostic est bon si les doses sont adaptées ; l’acidocétose euglycémique reste la complication qui menace la vie.', 7, 78), 79))
PTS.append(POINT(2, 'Épidémiologie (Suisse, puis Europe)', p2))

p3 = (P('Chaque médicament bloque un transporteur précis du néphron. '
        'Ce qui reste dans le tubule retient l’eau par osmose ; l’urine augmente et la soif compense. '
        'Les vaptans, eux, bloquent le récepteur V2 de la vasopressine : c’est une ' + AQ + '.', 54, 78) +
      F('Chaîne logique : de l’anatomie au traitement',
        TAB(['Étape', 'Ce qu’il faut comprendre'], [
         ['Anatomie', 'Tube proximal (SGLT2), anse de Henle (cotransporteur Na-K-2Cl), tube distal (cotransporteur Na-Cl), tube collecteur (récepteur V2, aquaporine 2).'],
         ['Physiologie', 'Pourquoi l’urine reste petite : le rein réabsorbe ≈ 99 % du sodium et presque tout le glucose filtrés.'],
         ['Physiopathologie', 'Bloquer un transporteur laisse un soluté dans la lumière ; l’eau suit, d’où la polyurie.'],
         ['Clinique', 'Soif, polyurie, parfois hypotension orthostatique ou hypernatrémie si le patient ne boit pas.'],
         ['Examens', 'On cherche le soluté urinaire (glucose, sodium) et l’état du volume.'],
         ['Traitement', 'On adapte la dose et on garde, si possible, le médicament utile.'],
        ]), 54, 78) +
      F('Mécanisme, exploration et cible thérapeutique',
        TAB(['Médicament et site', 'Mécanisme et exploration', 'Cible thérapeutique et complications'], [
         ['Gliflozines : empagliflozine (Jardiance®), dapagliflozine (Forxiga®) ; tube proximal', 'Seuil rénal du glucose abaissé à ≈ 4–5 mmol/L ; glycosurie à la bandelette', 'Maintien du traitement ; mycoses génitales, acidocétose euglycémique'],
         ['Diurétiques de l’anse : furosémide (Lasix®), torasémide (Torem®)', 'Natriurèse jusqu’à ≈ 20–25 % du sodium filtré ; gradient médullaire aboli', 'Dose minimale efficace ; hypokaliémie, alcalose, hypovolémie'],
         ['Vaptan : tolvaptan (Jinarc®, Samsca®) ; tube collecteur', 'Aquarèse : urine très diluée, sodium urinaire bas', 'Boissons libres ; hypernatrémie, toxicité hépatique'],
         ['Mannitol IV, produit de contraste hyperosmolaire', 'Trou osmolaire plasmatique > 10 mOsm/kg', 'Surveillance de la natrémie et du volume'],
         ['Corticoïdes systémiques', 'Hyperglycémie, surtout l’après-midi après une prise matinale', 'Contrôle glycémique'],
        ]), 54, 58))
PTS.append(POINT(3, 'Physiopathologie', p3))

p4 = (P('Le médecin vérifie d’abord l’urgence : sous gliflozine, nausées ou dyspnée imposent une cétonémie même si la glycémie est normale. '
        'Puis il relie la polyurie à la chronologie des médicaments. '
        'Enfin, il écarte les autres causes de polyurie.', 7, 16) +
      DIFF('iat') +
      F('Diagnostic différentiel sous gliflozine (fréquences en exposant rouge, patients de l’essai de 2015 sous empagliflozine)',
        TAB(['Diagnostic', 'Éléments d’orientation', 'Examen discriminant'], [
         ['Infection génitale' + PR('6,4 %', 79), 'Prurit, brûlures, rougeur génitale', 'Examen local'],
         ['Déplétion volémique' + PR('5,1 %', 79), 'Vertiges debout, soif, diurétique associé', 'Pression orthostatique, créatinine'],
         ['Acidocétose euglycémique' + PR('≈ 0,1 %', 79), 'Nausées, vomissements, dyspnée de Kussmaul', 'Cétonémie, gaz du sang'],
         ['Glycosurie attendue sans complication', 'Bandelette 3+ ou 4+, glycémie normale', 'Aucun : effet du médicament (fréquence non chiffrée séparément)'],
        ]) + P('Ces fréquences viennent d’un même essai et d’une même population ; elles ne s’appliquent pas aux autres médicaments.', 79)))
PTS.append(POINT(4, 'Raisonnement clinique et diagnostic différentiel', p4))

p5 = (P('L’anamnèse date chaque début ou hausse de dose. '
        'Elle cherche une gliflozine, un diurétique, un vaptan, un corticoïde ou une perfusion de mannitol. '
        'Elle demande aussi si le patient boit selon sa soif.', 54, 78) +
      U('Drapeaux rouges : malaise ou syncope en position debout, nausées et vomissements sous gliflozine, diurèse qui s’effondre, confusion sous vaptan. Ils imposent une évaluation en urgence et souvent une hospitalisation immédiate.', 7, 58) +
      F('Questions ciblées et leur raison',
        TAB(['Question', 'Pourquoi la poser'], [
         ['Quel médicament a été commencé ou augmenté récemment ?', 'La chronologie est le principal argument.'],
         ['Prenez-vous une gliflozine (Jardiance®, Forxiga®) ?', 'Sous gliflozine, une nausée peut cacher une acidocétose euglycémique.'],
         ['Avez-vous moins mangé, vomi ou été opéré ?', 'Le jeûne et la chirurgie déclenchent l’acidocétose.'],
         ['Avez-vous des vertiges en vous levant ?', 'Ils signent une hypovolémie.'],
         ['Prenez-vous de la cortisone le matin ?', 'Les corticoïdes élèvent la glycémie de l’après-midi.'],
         ['Avez-vous des démangeaisons génitales ?', 'Mycose favorisée par la glycosurie.'],
        ]), 79, 19))
PTS.append(POINT(5, 'Anamnèse ciblée et drapeaux rouges', p5))

p6 = (P('L’examen évalue le volume extracellulaire. À l’état normal, la pression systolique baisse de moins de 20 mmHg debout et le poids est stable. '
        'Les signes d’hypovolémie ont une sensibilité modeste ; la créatinine et la pression debout les complètent.', 54) +
      F('Signes, technique et valeur',
        TAB(['Signe', 'Technique', 'Ce qu’il signifie'], [
         ['Pression couché puis debout', 'Après 5 minutes couché, puis à 1 et 3 minutes debout', 'Baisse ≥ 20/10 mmHg : hypotension orthostatique'],
         ['Poids', 'Comparer au poids sec habituel', 'Perte rapide : déplétion volémique'],
         ['Organes génitaux', 'Inspection si prurit', 'Balanite ou vulvo-vaginite à Candida'],
         ['Respiration ample et rapide', 'Fréquence respiratoire', 'Respiration de Kussmaul (acidose)'],
         ['Œdèmes', 'Pression sur le tibia', 'Indication persistante du diurétique'],
        ]), 54, 79))
PTS.append(POINT(6, 'Examen clinique', p6))

p7 = (P('Deux syndromes dominent. Le syndrome de glycosurie normoglycémique est attendu sous gliflozine. '
        'Le syndrome d’hypovolémie avec hypokaliémie signe un excès de diurétique.', 78, 54) +
      F('Signes fonctionnels (symptômes rapportés)', UL(['Soif, mictions fréquentes', 'Vertiges debout', 'Crampes, faiblesse (hypokaliémie)', 'Prurit génital', 'Nausées, douleurs abdominales (acidocétose)']), 78) +
      F('Signes physiques (constatés à l’examen)', UL(['Hypotension orthostatique', 'Perte de poids', 'Balanite, vulvo-vaginite', 'Respiration de Kussmaul']), 54) +
      F('Syndrome de glycosurie normoglycémique (gliflozine)',
        TAB(['Signe', 'Mécanisme', 'Valeur'], [
         ['Glycosurie 3+ ou 4+', 'Blocage du SGLT2', 'Preuve que le médicament agit'],
         ['Glycémie normale ou peu élevée', 'Glucose éliminé par le rein', 'Ne pas conclure à un diabète déséquilibré'],
         ['Polyurie modérée', 'Diurèse osmotique', 'Souvent transitoire'],
        ]), 78) +
      F('Syndrome d’hypovolémie avec hypokaliémie (diurétiques)',
        TAB(['Signe', 'Mécanisme', 'Valeur'], [
         ['Hypotension orthostatique', 'Perte de sel et d’eau', 'Réduire la dose'],
         ['Hypokaliémie, alcalose', 'Perte de potassium et d’ions H⁺ au tube distal', 'Risque d’arythmie'],
         ['Créatinine en hausse', 'Insuffisance rénale fonctionnelle', 'FEUrée < 35 %'],
        ]), 54, 80))
PTS.append(POINT(7, 'Syndromes et signes cliniques', p7))

p8 = (P('Aucune société savante ne publie de critère propre à la polyurie iatrogène. Le diagnostic repose sur la chronologie, le soluté urinaire attendu et l’amélioration à l’adaptation de la dose. '
        'Pour l’acidocétose euglycémique, le critère du consensus de 2024 s’applique : pH < 7,30 ou bicarbonate < 18 mmol/L, cétonémie ≥ 3,0 mmol/L. '
        'Une glycémie normale ne suffit pas à l’écarter.', 7, 54) +
      F('Signature urinaire selon le médicament',
        TAB(['Médicament', 'Soluté urinaire', 'Osmolalité urinaire'], [
         ['Gliflozine', 'Glucose ++++', 'Iso-osmotique ou plus'],
         ['Diurétique de l’anse ou thiazide', 'Sodium et chlore élevés', '≈ 300 mOsm/kg'],
         ['Tolvaptan', 'Sodium bas, eau libre', '< 100–200 mOsm/kg'],
         ['Mannitol', 'Mannitol (trou osmolaire)', 'Élevée'],
        ]), 54, 58))
PTS.append(POINT(8, 'Critères diagnostiques', p8))

p9 = (H4('9.a Examen de référence') +
      P('Il n’existe pas d’examen de référence unique : on associe la revue des médicaments, la bandelette urinaire et l’ionogramme. '
        'En cas d’insuffisance rénale sous diurétique, une ' + FEU + ' < 35 % a une sensibilité de 90 % et une spécificité de 96 % pour l’origine fonctionnelle.', 80) +
      H4('9.b Examens de première et de deuxième intention') +
      P('En première intention : bandelette urinaire, ionogramme avec kaliémie, créatinine et DFGe, glycémie, cétonémie si gliflozine. '
        'En deuxième intention : gaz du sang si cétonémie ≥ 1,5 mmol/L, natriurèse et FEUrée, osmolalité plasmatique si mannitol.', 7, 80) +
      TAB(['Intention', 'Examen', 'Pourquoi'], [
       ['1re', 'Bandelette urinaire', 'Glycosurie attendue sous gliflozine'],
       ['1re', 'Ionogramme, kaliémie, créatinine', 'Hypovolémie, hypokaliémie, hyper- ou hyponatrémie'],
       ['1re', 'Cétonémie capillaire (β-hydroxybutyrate)', 'Acidocétose euglycémique sous gliflozine'],
       ['2e', 'Gaz du sang veineux', 'pH, bicarbonate, trou anionique'],
       ['2e', 'Natriurèse, FEUrée', 'Origine fonctionnelle d’une insuffisance rénale'],
       ['2e', 'Transaminases', 'Toxicité hépatique du tolvaptan'],
      ]) +
      H4('9.c Prescription et calculs') +
      P('Indication : toute polyurie apparue après un changement de traitement. Moment : 2–4 semaines après le début d’un diurétique ou d’une gliflozine ; immédiatement si symptômes. '
        'Préparation : échantillon d’urine avant toute nouvelle dose de diurétique.', 54, 44) +
      TAB(['Calcul', 'Formule', 'Seuil'], [
       ['Fraction d’excrétion du sodium (FENa)', '(Na urinaire × créatinine plasmatique) / (Na plasmatique × créatinine urinaire) × 100', '< 1 % : origine fonctionnelle (sans diurétique)'],
       ['Fraction d’excrétion de l’urée', '(urée urinaire × créatinine plasmatique) / (urée plasmatique × créatinine urinaire) × 100', '< 35 % : origine fonctionnelle (même sous diurétique)'],
      ]) +
      H4('9.d Interprétation : positif, négatif, limite, discordant') +
      TAB(['Résultat', 'Signification', 'Conduite'], [
       ['Positif : glycosurie avec glycémie normale sous gliflozine', 'Effet attendu', 'Rassurer, poursuivre'],
       ['Négatif : pas de glycosurie sous gliflozine', 'Mauvaise observance ou DFGe très bas', 'Vérifier la prise et la fonction rénale'],
       ['Limite : cétonémie 0,6–1,5 mmol/L', 'Cétose débutante', 'Arrêter la gliflozine, manger, recontrôler'],
       ['Discordant : glycémie normale et pH < 7,30', 'Acidocétose euglycémique', 'Urgence : insuline IV et glucose'],
      ]) +
      H4('9.e Alternatives') +
      P('Grossesse : gliflozines et vaptans sont à éviter. Enfant : indications rares, avis spécialisé. '
        'DFGe : la baisse initiale de ≈ 10–25 % après une gliflozine est attendue ; une baisse > 30 % impose de réévaluer le volume. Le produit de contraste iodé hyperosmolaire peut lui-même provoquer une diurèse osmotique ; l’IRM n’a pas de rôle ici.', 44, 78))
PTS.append(POINT(9, 'Examens complémentaires', p9))

p10 = (P('Si la polyurie sous gliflozine est bien tolérée, sans hypovolémie ni cétose, le médecin rassure et garde le traitement, car il protège le cœur et le rein. '
         'S’il existe une hypotension orthostatique sous gliflozine et diurétique de l’anse, il réduit d’abord le diurétique.', 40, 44) +
       F('Arbre décisionnel : polyurie sous traitement',
         OL(['Nausées, vomissements ou dyspnée sous gliflozine : cétonémie et gaz du sang immédiatement.',
             'Hypotension orthostatique : réduire le diurétique de l’anse (par exemple de moitié), garder la gliflozine.',
             'Hypernatrémie sous tolvaptan : boissons libres, contrôle de la natrémie, réduire ou arrêter.',
             'Hypokaliémie sous diurétique : supplément de potassium ou diurétique épargneur.',
             'Polyurie persistante après adaptation : chercher une autre cause (DX.1, DX.9, DX.10).']), 7, 54))
PTS.append(POINT(10, 'Arbre décisionnel', p10))

fiche = FICHE([
  ['Gliflozine : empagliflozine (Jardiance®)', 'Inhibe le SGLT2 du tube proximal', 'Demi-vie ≈ 12 h', '10 mg 1 fois/j, au long cours', 'Mycose génitale, hypovolémie, acidocétose euglycémique', 'Diabète de type 1 (hors indication), acidocétose', 'Diurétiques (hypovolémie), insuline (hypoglycémie)'],
  ['Diurétique de l’anse : torasémide (Torem®)', 'Inhibe le cotransporteur Na-K-2Cl', 'Demi-vie ≈ 3–4 h ; métabolisme hépatique', '5–20 mg/j ; réduire si hypotension', 'Hypokaliémie, hypovolémie, hyperuricémie', 'Anurie, hypovolémie', 'Lithium (lithémie accrue), anti-inflammatoires (effet réduit)'],
  ['Vaptan : tolvaptan (Jinarc®)', 'Antagoniste du récepteur V2', 'Demi-vie ≈ 3–12 h ; CYP3A4', 'Selon l’indication (polykystose), titration', 'Soif, polyurie, toxicité hépatique', 'Hypovolémie, incapacité à boire', 'Inhibiteurs du CYP3A4 (kétoconazole, jus de pamplemousse)'],
 ], 58, 79)
p11 = (H4('11.A Buts : d’abord l’urgence (acidocétose euglycémique, hypovolémie sévère), car elles menacent la vie') +
       P('Le traitement garde les médicaments protecteurs, prévient l’hypovolémie et l’acidocétose, et corrige les électrolytes.', 19, 40) +
       TAB(['But', 'Cible chiffrée'], [
        ['Pression debout', 'Baisse < 20/10 mmHg'],
        ['Kaliémie', '3,5–5,0 mmol/L'],
        ['Cétonémie sous gliflozine', '< 0,6 mmol/L'],
       ]) +
       H4('11.B Moyens et méthodes : forme compliquée en urgence, forme non compliquée en ambulatoire') +
       P('L’acidocétose euglycémique compliquée relève de l’urgence : insuline IV à débit fixe et glucose 10 % dès la première heure, car la glycémie est basse. '
         'En ambulatoire, l’éducation passe par les règles des jours de maladie : arrêt temporaire de la gliflozine, du diurétique et des inhibiteurs du système rénine-angiotensine pendant une gastro-entérite ou une fièvre.', 16, 19) +
       P('Avant une chirurgie programmée, la gliflozine s’arrête 3 jours avant (4 jours pour l’ertugliflozine).', 19) +
       F('Traitements selon la situation',
         TAB(['Situation', 'Traitement', 'Pourquoi'], [
          ['Hypotension orthostatique sous gliflozine et diurétique', 'Réduire le diurétique (par exemple torasémide 20 → 10 mg/j)', 'La gliflozine est plus protectrice'],
          ['Mycose génitale sous gliflozine', 'Clotrimazole (Gyno-Canesten®) local ou fluconazole (Diflucan®) 150 mg en dose unique', 'Traitement sans arrêter la gliflozine'],
          ['Acidocétose euglycémique', 'Arrêt de la gliflozine, insuline IV, glucose 10 %', 'Bloquer la cétogenèse'],
          ['Hypernatrémie sous tolvaptan', 'Boire selon la soif, réduire la dose', 'Compenser l’aquarèse'],
         ]), 16, 55) +
       fiche +
       F('Situations particulières',
         TAB(['Situation', 'Particularité'], [
          ['Grossesse', 'Gliflozines, vaptans contre-indiqués ; diurétiques seulement si indispensable'],
          ['Personne âgée', 'Risque d’hypovolémie : doses minimales, pesée'],
          ['Enfant', 'Indications pédiatriques limitées ; avis spécialisé'],
          ['Insuffisance rénale (DFGe < 20–25)', 'Effet glycosurique faible ; maintien possible selon KDIGO 2024'],
          ['Insuffisance hépatique', 'Tolvaptan contre-indiqué si atteinte hépatique'],
         ]), 44, 55) +
       SOCIAL('Un arrêt de travail est rarement nécessaire ; il l’est après une acidocétose ou une hypovolémie hospitalisée (quelques jours, durée non chiffrée).',
              'La conduite est déconseillée en cas de malaises orthostatiques ou d’hypoglycémies, jusqu’à leur correction (OAC, annexe 1).',
              'Les médicaments cités sont remboursés par la LAMal dans leurs indications de la liste des spécialités.') +
       H4('11.C Surveillance et critères de sortie') +
       TAB(['Quand', 'Quoi'], [
        ['À 2–4 semaines', 'Créatinine, kaliémie, pression debout, poids'],
        ['Chaque mois pendant 18 mois, puis tous les 3 mois', 'Transaminases et bilirubine sous tolvaptan (Jinarc®) ; arrêt si hausse marquée'],
        ['Lors de toute maladie aiguë', 'Cétonémie sous gliflozine'],
        ['Critères de sortie (après acidocétose)', 'pH > 7,30, cétonémie < 0,6 mmol/L, alimentation reprise, éducation faite'],
       ]) +
       H4('11.D Pronostic et recherche 2026') +
       P('Le pronostic est bon quand les doses sont adaptées et les règles des jours de maladie connues. '
         'La recherche porte sur les combinaisons de gliflozines et de diurétiques dans l’insuffisance cardiaque, qui augmentent l’effet diurétique.', 40, 78))
PTS.append(POINT(11, 'Prise en charge', p11))

p12 = (P('La prévention passe par l’éducation à l’introduction : boire selon la soif, suspendre la gliflozine les jours de maladie, connaître les signes de mycose. '
         'L’hygiène génitale est conseillée, mais son effet préventif n’est pas chiffré dans les sources ; le « divise par trois » de l’original a été retiré.', 19, 79) +
       F('Prévention primaire, secondaire et tertiaire',
         TAB(['Niveau', 'Mesure'], [
          ['Primaire', 'Règles des jours de maladie remises par écrit dès l’introduction'],
          ['Secondaire', 'Créatinine et kaliémie à 2–4 semaines ; cétonémie au moindre symptôme'],
          ['Tertiaire', 'Revoir les associations après une hypovolémie ou une acidocétose'],
         ]) + P('En Suisse, les recommandations de la SSED reprennent les règles des jours de maladie des sociétés internationales.', 19)))
PTS.append(POINT(12, 'Prévention', p12))

PTS.append(POINT(13, 'Points clés',
 P('Sous gliflozine, une glycosurie 4+ prouve que le médicament agit. '
   'Une nausée sous gliflozine impose une cétonémie, même avec une glycémie normale. '
   'En cas d’hypotension, on réduit d’abord le diurétique de l’anse. '
   'Sous diurétique, une FEUrée < 35 % signe une insuffisance rénale fonctionnelle.', 7, 80)))

PTS.append(POINT(14, 'Pièges d’examen',
 TAB(['Piège', 'Ce qu’il faut répondre'], [
  ['Glycémie à 8,5 mmol/L sous gliflozine, vomissements, pH 7,12', 'Acidocétose euglycémique : cétonémie, insuline IV et glucose 10 %'],
  ['Arrêter la gliflozine pour une baisse de DFGe de 15 %', 'Non : baisse attendue ; réévaluer seulement si > 30 %'],
  ['Utiliser la FENa sous diurétique', 'Elle est faussement élevée ; utiliser la FEUrée'],
  ['Conclure à un diabète déséquilibré devant une glycosurie 4+', 'Effet normal de la gliflozine'],
 ]) + P('Ces pièges suivent les recommandations sur les crises hyperglycémiques et la maladie rénale chronique.', 7, 44)))

CTX = {'_prefixe': 'Sous traitement polyurique',
 'cetone': 'Sous gliflozine, une cétonémie ≥ 3,0 mmol/L avec acidose signe l’acidocétose, même avec une glycémie normale.',
 'iono': 'La kaliémie et la natrémie dépistent l’hypokaliémie des diurétiques et l’hypernatrémie des vaptans.',
 'natriurese': 'Sous diurétique, la natriurèse est élevée ; préférer la FEUrée pour juger le volume.',
 'gly': 'Sous gliflozine, la glycémie peut être normale malgré une acidocétose.',
 'creat': 'Une baisse du DFGe de 10–25 % après une gliflozine est attendue ; au-delà de 30 %, réévaluer le volume.',
 'gds': 'Le gaz du sang mesure le pH et le bicarbonate quand la cétonémie dépasse 1,5 mmol/L.',
 'osmo': 'Un trou osmolaire > 10 mOsm/kg fait évoquer le mannitol.',
 'hep': 'Sous tolvaptan, les transaminases se contrôlent chaque mois pendant 18 mois.'}
if __name__ == '__main__':
    produire(M, PTS, SOURCES, CTX)
