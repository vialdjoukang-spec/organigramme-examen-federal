# -*- coding: utf-8 -*-
"""DX.1 — Anémie ferriprive et carence en fer. LOT 4, V5 → V7 AUDITÉ."""
from lot4_commun import *
POINT = mkPOINT('dx1')
M = META('dx1', 'DX.1', 'Anémie ferriprive', 'Anémie ferriprive et carence en fer sans anémie',
         'LOT_004_DX1_Anemie_ferriprive_AUDITÉ.html',
         'Corrections majeures : Maltofer® est du fer ferrique (Fe³⁺, polymaltose), pas du sulfate ferreux ; l’hepcidine reste élevée environ 24 h (et non 48 h) ; le dépistage systématique pendant la grossesse sans anémie n’est plus recommandé ; chiffres suisses non sourcés remplacés.')
HEP = T('hepcidine', 'L’hepcidine est une hormone du foie qui bloque la ferroportine, la « porte de sortie » du fer de l’intestin et des macrophages ; elle monte après chaque prise de fer et lors d’une inflammation.')
FERR = T('ferritine', 'La ferritine est la protéine qui stocke le fer dans les cellules ; sa concentration sanguine reflète les réserves, mais elle augmente aussi en cas d’inflammation.')
ERY = T('érythropoïèse', 'L’érythropoïèse est la fabrication des globules rouges par la moelle osseuse ; elle consomme environ 20–25 mg de fer par jour, recyclé surtout à partir des globules rouges âgés.')
PTS = []
def ADD(*a): PTS.append(POINT(*a))
ADD(1, 'Définition et sémantique',
 P('La carence en fer est une baisse du fer total de l’organisme. On parle d’anémie ferriprive quand cette carence fait baisser l’hémoglobine sous la norme : < 120 g/L chez la femme, < 130 g/L chez l’homme (OMS). '
   'La fatigue vient du manque d’oxygène apporté aux muscles et du rôle du fer dans les enzymes de la respiration cellulaire.', 9) +
 F('Terminologie',
   TAB(['Terme', 'Définition exacte', 'À ne pas confondre avec'], [
    ['Carence en fer sans anémie (stade 1)', 'Ferritine basse, hémoglobine et volume globulaire normaux', 'Anémie ferriprive'],
    ['Érythropoïèse déficitaire en fer (stade 2)', 'Hémoglobine encore normale, mais moelle qui manque de fer (saturation de la transferrine basse)', 'Simple baisse des réserves'],
    ['Anémie ferriprive (stade 3)', 'Hémoglobine < 120 g/L (femme) ou < 130 g/L (homme), microcytaire et hypochrome', 'Anémie inflammatoire, thalassémie mineure'],
    ['Carence en fer fonctionnelle', 'Réserves présentes mais fer bloqué par l’' + HEP + ' (inflammation)', 'Carence absolue'],
    ['Sidéropénie', 'Synonyme ancien de carence en fer', 'Sidérose (surcharge)'],
   ]) + P('Il faut distinguer la carence en fer, qui est un symptôme, de sa cause, qui doit toujours être cherchée.', 9)))
ADD(2, 'Épidémiologie (Suisse, puis Europe)',
 P('En Suisse, une étude chez de jeunes Zurichoises trouve 22,7 % de carence en fer (ferritine < 15 µg/L) et 2,2 % d’anémie ferriprive. '
   'En Europe et aux États-Unis, 15–20 % des femmes réglées ont une carence sans anémie et ≈ 3 % une anémie ferriprive. '
   'Environ 80 % des anémies sont ferriprives.', 9) +
 F('Chiffres, terrain et histoire naturelle',
   TAB(['Donnée', 'Valeur', 'Portée'], [
    ['Carence en fer, jeunes femmes de Zurich', '22,7 % (ferritine < 15 µg/L)', 'Étude ancienne citée par mediX'],
    ['Anémie ferriprive, jeunes femmes de Zurich', '2,2 %', 'Même étude'],
    ['Anémie ferriprive, femmes réglées (Europe, États-Unis)', '≈ 3 %', 'Ordre de grandeur des enquêtes nationales'],
    ['Anémie chez les patients qui consultent pour fatigue', '2,8 %', 'Revue systématique de premier recours'],
    ['Part des anémies dues au fer', '≈ 80 %', 'Dont 80 % chez des femmes'],
    ['« 20 % des femmes, 5 % des hommes » (original)', 'Non sourcé', 'Retiré : aucune source OFS retrouvée'],
   ]) + P('Le terrain à risque réunit la femme réglée, la grossesse, le régime végétarien, le donneur de sang régulier, le sportif d’endurance et la personne âgée. '
          'Le pronostic dépend de la cause : il est excellent si la perte de sang est tarie, mauvais si un cancer digestif est découvert tard ; la mortalité propre de l’anémie n’est pas chiffrée dans les sources.', 9, 2)))
ADD(3, 'Physiopathologie',
 P('Le corps contient 3–4 g de fer, surtout dans l’hémoglobine. L’intestin n’en absorbe que 1–2 mg par jour, autant qu’il en perd. '
   'Toute perte de sang supplémentaire vide donc les réserves, parce que l’absorption ne peut pas suivre.', 9) +
 F('Chaîne logique : de l’anatomie au traitement',
   TAB(['Étape', 'Ce qu’il faut comprendre'], [
    ['Anatomie', 'Le duodénum absorbe le fer ; le foie, la rate et la moelle le stockent ; la moelle fabrique les globules rouges.'],
    ['Physiologie', 'L’' + ERY + ' recycle le fer des vieux globules. La ferritine stocke le fer ; l’hepcidine règle sa sortie.'],
    ['Physiopathologie', 'Sans fer, la moelle fabrique des globules petits (microcytose) et pâles (hypochromie). Le muscle manque d’oxygène et d’enzymes à fer, ce qui explique la fatigue.'],
    ['Clinique', 'D’où la pâleur, l’essoufflement à l’effort, les palpitations, puis les ongles cassants et la perte de cheveux.'],
    ['Examens', 'On mesure l’hémoglobine (anémie), la ferritine (réserves) et la CRP (inflammation qui fausse la ferritine).'],
    ['Traitement', 'On remplace le fer par la bouche ou par perfusion et, surtout, on traite la cause de la perte.'],
   ]), 9) +
 F('Mécanisme, exploration et cible thérapeutique',
   TAB(['Mécanisme', 'Lésion ou cause', 'Exploration', 'Cible thérapeutique'], [
    ['Perte de sang', 'Règles abondantes, ulcère, cancer colorectal, anti-inflammatoires', 'Anamnèse, endoscopies', 'Traiter la lésion, fer'],
    ['Besoin accru', 'Grossesse, croissance, sport d’endurance', 'Ferritine', 'Fer oral'],
    ['Absorption diminuée', 'Maladie cœliaque, gastrite atrophique, inhibiteurs de la pompe à protons, chirurgie bariatrique', 'IgA anti-transglutaminase, gastroscopie', 'Fer IV, régime sans gluten'],
    ['Blocage par l’hepcidine', 'Inflammation chronique, cancer, maladie rénale', 'CRP, saturation de la transferrine', 'Traiter l’inflammation, fer IV'],
   ]) + P('Le fer oral augmente l’hepcidine pendant environ 24 heures. C’est pourquoi une prise un jour sur deux est mieux absorbée qu’une prise quotidienne.', 11)))
ADD(4, 'Raisonnement clinique et diagnostic différentiel',
 P('Devant une fatigue, le médecin demande d’abord un hémogramme et une ferritine. '
   'Si la ferritine est basse, la carence est prouvée et il faut en trouver la cause. '
   'Chez l’homme et la femme ménopausée, la cause est digestive jusqu’à preuve du contraire ; chez la femme réglée, on évalue d’abord les règles.', 9) +
 DIFF('fer') + DIFF_FAT() +
 F('Diagnostic différentiel d’une anémie microcytaire',
   TAB(['Diagnostic', 'Ferritine', 'Autres éléments', 'Examen discriminant'], [
    ['Anémie ferriprive', 'Basse (< 30 µg/L)', 'Plaquettes souvent élevées', 'Ferritine, recherche de la perte'],
    ['Anémie inflammatoire', 'Normale ou haute', 'CRP élevée, saturation de la transferrine basse', 'Récepteur soluble de la transferrine'],
    ['Thalassémie mineure', 'Normale', 'Microcytose marquée avec hémoglobine peu basse, origine méditerranéenne ou asiatique', 'Électrophorèse de l’hémoglobine'],
    ['Anémie sidéroblastique', 'Normale ou haute', 'Alcool, médicaments, myélodysplasie', 'Myélogramme avec coloration de Perls'],
   ]) + P('Ces diagnostics n’ont pas de fréquence publiée sur une base commune chez le patient fatigué ; il ordonne la recherche selon la ferritine et la CRP.', 9)))
ADD(5, 'Anamnèse ciblée et drapeaux rouges',
 P('L’anamnèse cherche la perte : abondance et durée des règles, selles noires ou sang rouge, douleurs épigastriques, anti-inflammatoires, anticoagulants. '
   'Elle précise l’alimentation, les dons de sang et les symptômes digestifs d’une maladie cœliaque.', 9) +
 U('Drapeaux rouges : perte de poids inexpliquée, sang dans les selles, changement récent du transit, anémie nouvelle après 50 ans, dysphagie, méléna avec malaise. Ils imposent une endoscopie rapide ; un saignement actif avec hypotension impose l’hospitalisation immédiate (144).', 9) +
 F('Questions ciblées et leur raison',
   TAB(['Question', 'Pourquoi la poser'], [
    ['Vos règles durent-elles plus de 7 jours, avec des caillots ou des protections changées toutes les heures ?', 'Des règles abondantes sont la première cause chez la femme jeune.'],
    ['Avez-vous vu du sang ou des selles noires ?', 'Un saignement digestif impose une endoscopie.'],
    ['Prenez-vous de l’aspirine, des anti-inflammatoires ou un anticoagulant ?', 'Ils favorisent les saignements digestifs.'],
    ['Avez-vous des diarrhées, des ballonnements, une perte de poids ?', 'Ils évoquent une maladie cœliaque ou une maladie inflammatoire de l’intestin.'],
    ['Mangez-vous de la viande ? Donnez-vous votre sang ?', 'Un régime végétarien et les dons répétés augmentent le besoin.'],
    ['Avez-vous envie de glaçons ou de terre ?', 'Le pica est un signe évocateur de carence en fer.'],
   ]), 9))
ADD(6, 'Examen clinique',
 P('L’examen cherche une pâleur des conjonctives, plus fiable que celle de la peau, une tachycardie et un souffle systolique fonctionnel. '
   'Il inspecte les ongles, la langue et les commissures des lèvres, palpe l’abdomen et comporte un toucher rectal.', 9) +
 P('On note d’abord les valeurs normales de l’adulte : pouls 60–100/min au repos, conjonctives roses. '
   'La pâleur conjonctivale a une sensibilité faible : son absence n’exclut pas une anémie ; sa spécificité est meilleure, mais aucune valeur suisse n’est publiée.', 9) +
 F('Signes, technique et valeur',
   TAB(['Signe', 'Technique', 'Ce qu’il signifie'], [
    ['Pâleur conjonctivale', 'Abaisser la paupière inférieure à la lumière du jour', 'Anémie, souvent < 90–100 g/L'],
    ['Tachycardie, souffle systolique doux', 'Pouls au repos, auscultation du foyer pulmonaire', 'Compensation du débit cardiaque'],
    ['Koïlonychie (ongles en cuillère)', 'Regarder les ongles de profil', 'Carence ancienne'],
    ['Glossite, chéilite angulaire', 'Inspecter la langue et les coins de la bouche', 'Carence tissulaire en fer'],
    ['Masse abdominale, hépatomégalie', 'Palpation des quatre quadrants', 'Cancer digestif'],
    ['Sang au doigtier', 'Toucher rectal', 'Saignement bas ; un toucher normal n’exclut rien'],
   ]), 9))
ADD(7, 'Syndromes et signes cliniques',
 F('Signes fonctionnels (symptômes rapportés)', UL(['Fatigue, baisse de l’endurance', 'Essoufflement et palpitations à l’effort', 'Maux de tête, vertiges', 'Difficultés de concentration', 'Jambes sans repos, pica']), 9) +
 F('Signes physiques (constatés à l’examen)', UL(['Pâleur des conjonctives', 'Tachycardie, souffle systolique', 'Ongles cassants ou en cuillère', 'Chute de cheveux, peau sèche', 'Fissures aux coins de la bouche']), 9) +
 P('Le syndrome anémique réunit pâleur, essoufflement, palpitations et fatigue : il traduit le manque d’oxygène. '
   'Le syndrome de carence tissulaire réunit ongles, cheveux, langue et commissures : il traduit le rôle du fer dans les cellules qui se renouvellent vite.', 9) +
 F('Syndrome anémique', TAB(['Signe', 'Mécanisme', 'Valeur'], [
    ['Dyspnée d’effort', 'Moins d’oxygène transporté par litre de sang', 'Dépend de la vitesse d’installation'],
    ['Tachycardie', 'Le cœur augmente le débit pour compenser', 'Marquée si anémie rapide'],
    ['Fatigue', 'Hypoxie musculaire et enzymes à fer diminuées', 'Peu spécifique'],
   ]), 9) +
 F('Syndrome de carence tissulaire en fer', TAB(['Signe', 'Mécanisme', 'Valeur'], [
    ['Koïlonychie', 'Croissance anormale de l’ongle', 'Spécifique mais tardive'],
    ['Glossite atrophique', 'Atrophie des papilles', 'Aussi dans la carence en vitamine B12'],
    ['Pica', 'Mécanisme inconnu', 'Très évocateur ; disparaît vite sous fer'],
   ]), 9))
ADD(8, 'Critères diagnostiques',
 P('L’anémie se définit par l’hémoglobine seule (critère OMS). Sa cause ferriprive se prouve par une ferritine basse. '
   'Une microcytose ne suffit pas : elle manque au début et existe aussi dans la thalassémie. '
   'Une ferritine normale ne suffit pas à exclure la carence si la CRP est élevée.', 9) +
 F('Critères (OMS pour l’anémie ; mediX 2025 pour les réserves en fer)',
   TAB(['Critère', 'Seuil'], [
    ['Anémie, femme non enceinte', 'Hémoglobine < 120 g/L'],
    ['Anémie, homme', 'Hémoglobine < 130 g/L'],
    ['Anémie, grossesse', '< 110 g/L (< 105 g/L au 2e trimestre)'],
    ['Réserves épuisées', 'Ferritine < 15 µg/L'],
    ['Réserves réduites', 'Ferritine 15–30 µg/L'],
    ['Carence si inflammation ou maladie chronique', 'Saturation de la transferrine ≤ 20 %'],
   ]) + P('L’original affirmait que les critères OMS associent « inévitablement » une ferritine < 30 µg/L : c’est faux, l’OMS définit l’anémie par l’hémoglobine seule.', 9)) +
 F('Gravité de l’anémie', TAB(['Grade', 'Hémoglobine'], [['Légère', '90–120 g/L (femme)'], ['Modérée à sévère', '< 90 g/L'], ['Sévère', '< 60–70 g/L']]) +
   P('La tolérance compte plus que le chiffre : une angine de poitrine ou une syncope imposent une prise en charge urgente.', 9)))
ADD(9, 'Examens complémentaires',
 H4('9.a Examen de référence') +
 P('L’examen de référence historique est la coloration de Perls du myélogramme, qui montre l’absence de fer médullaire. '
   'En pratique, la ferritine le remplace : une ferritine < 15 µg/L a une spécificité proche de 100 % pour une carence ; sa sensibilité est moindre, car l’inflammation l’augmente.', 9) +
 H4('9.b Examens de première et de deuxième intention') +
 P('En première intention, on demande hémogramme, ferritine et CRP. En deuxième intention, on cherche la cause et on précise la carence si l’inflammation gêne la lecture.', 9) +
 TAB(['Intention', 'Examen', 'Pourquoi'], [
  ['1re', 'Hémogramme avec volume globulaire et réticulocytes', 'Confirme l’anémie et son caractère peu régénératif'],
  ['1re', 'Ferritine', 'Mesure les réserves'],
  ['1re', 'CRP', 'Signale l’inflammation qui élève la ferritine'],
  ['2e', 'Saturation de la transferrine', 'Prouve la carence quand la ferritine est faussée'],
  ['2e', 'IgA anti-transglutaminase et IgA totales', 'Maladie cœliaque'],
  ['2e', 'Gastroscopie et coloscopie', 'Cause digestive'],
  ['2e', 'Électrophorèse de l’hémoglobine', 'Thalassémie si ferritine normale'],
 ]) +
 H4('9.c Prescription et formules') +
 P('Indication : fatigue, anémie microcytaire, terrain à risque ou contrôle d’un traitement. Moment : le matin, à distance d’une infection aiguë. '
   'Préparation : aucun jeûne nécessaire ; arrêt du fer oral 1 semaine avant un contrôle de ferritine, sinon le résultat est surestimé.', 9) +
 TAB(['Grandeur', 'Formule', 'Repère'], [
  ['Déficit en fer (Ganzoni)', 'Poids (kg) × (Hb cible 15 − Hb actuelle) (g/dL) × 2,4 + 500 mg de réserves', 'Réserves de 500 mg si poids > 35 kg ; poids idéal (indice de masse corporelle de 25) si obésité'],
  ['Schéma simplifié (Swissmedic)', 'Hb < 10 g/dL : 1500 mg (35–70 kg) ou 2000 mg (≥ 70 kg) ; Hb 10–14 : 1000 ou 1500 mg ; Hb ≥ 14 : 500 mg', 'Information professionnelle de Ferinject®'],
  ['Règle simple (mediX)', 'Ferritine < 10 µg/L : 1000 mg ; 10–15 µg/L : 500 mg', 'Dose cumulée sans anémie marquée'],
  ['Saturation de la transferrine', 'Fer sérique / capacité totale de fixation × 100', 'Normale 20–45 %'],
 ]) + P('Exemple : femme de 60 kg, Hb 9 g/dL, cible 15 g/dL : 60 × 6 × 2,4 + 500 = 1364 mg, arrondi à 1300 mg selon l’information professionnelle, en 2 perfusions espacées d’au moins 7 jours.', 13, 75, 9) +
 H4('9.d Interprétation : positif, négatif, limite, discordant') +
 TAB(['Situation', 'Interprétation', 'Conduite'], [
  ['Positif : ferritine < 15 µg/L', 'Carence certaine', 'Traiter et chercher la cause'],
  ['Négatif : ferritine > 100 µg/L sans inflammation', 'Carence improbable', 'Chercher une autre cause de fatigue'],
  ['Limite : ferritine 15–30 µg/L', 'Réserves réduites', 'Selon symptômes et terrain'],
  ['Discordant : ferritine 50–100 µg/L, CRP haute, TSAT < 20 %', 'Carence masquée par l’inflammation', 'Récepteur soluble de la transferrine ou essai de fer IV'],
 ]) +
 H4('9.e Alternatives') +
 P('Grossesse : hémogramme et ferritine si anémie ou facteur de risque ; le fer IV n’est donné qu’à partir du 2e trimestre. Enfant : mêmes examens avec des normes d’âge. '
   'DFGe bas : la saturation de la transferrine complète la ferritine. Le scanner avec iode et l’IRM ne servent qu’à chercher une cause ; un pacemaker n’empêche pas les endoscopies.', 9))
ADD(10, 'Arbre décisionnel',
 P('Si l’hémogramme montre une anémie microcytaire, alors on dose la ferritine. Si la ferritine est basse, la carence est prouvée et l’on cherche la cause selon l’âge et le sexe.', 9) +
 F('Arbre décisionnel : fatigue et suspicion de carence en fer',
   OL(['Hémogramme, ferritine, CRP chez tout patient fatigué à risque.',
       'Ferritine < 30 µg/L : carence → traiter et chercher la cause.',
       'Femme réglée sans signe digestif : évaluer les règles, IgA anti-transglutaminase ; endoscopie si échec du traitement.',
       'Homme ou femme ménopausée : endoscopies ; après 50 ans, la coloscopie d’abord, avant 50 ans la gastroscopie avec biopsies d’abord.',
       'Ferritine normale et CRP élevée : saturation de la transferrine → carence fonctionnelle → oriente vers une maladie inflammatoire.',
       'Ferritine normale et CRP normale : électrophorèse de l’hémoglobine → thalassémie, ou autre cause de fatigue.']), 9))
ADD(11, 'Prise en charge',
 H4('11.A Buts : d’abord l’urgence (saignement actif, anémie mal tolérée), car elle peut tuer en quelques heures') +
 P('Le traitement normalise l’hémoglobine, remplit les réserves et supprime la cause de la perte. La cible est une ferritine de 50–100 µg/L après une anémie.', 9) +
 TAB(['But', 'Cible chiffrée'], [
  ['Hémoglobine', 'Hausse d’environ 20 g/L en 4 semaines'],
  ['Réserves', 'Ferritine 50–100 µg/L'],
  ['Cause', 'Saignement tari ou cause traitée'],
 ]) +
 H4('11.B Moyens et méthodes : forme compliquée en urgence, puis forme non compliquée en ambulatoire') +
 P('La forme compliquée (saignement actif, angine de poitrine, syncope) relève de l’urgence : transfusion de concentrés érythrocytaires et endoscopie. '
   'La forme non compliquée se traite en ambulatoire par le fer oral, avec des mesures générales d’alimentation et l’éducation du patient.', 9) +
 P('Moyens non médicamenteux : alimentation riche en fer héminique (viande rouge), légumineuses, thé et café à distance des repas. La vitamine C n’a pas d’effet notable démontré sur l’absorption.', 9) +
 FICHE([
  ['Fer ferreux oral (Fe²⁺) : sulfate ferreux (Tardyferon®), Ferrum Hausmann®', 'Apporte du fer absorbé par le duodénum', 'Absorption 10–20 %, freinée par l’hepcidine pendant ≈ 24 h', '60–100 mg de fer élément un jour sur deux (ou 80–100 mg par jour), 30 min avant le repas ; 3 mois après normalisation de l’Hb', 'Nausées, constipation, selles noires', 'Hémochromatose, anémie sans carence', 'Antiacides, IPP, calcium, lévothyroxine, quinolones, tétracyclines (espacer de 2 h)'],
  ['Fer ferrique oral (Fe³⁺) : polymaltose (Maltofer®)', 'Complexe ferrique absorbé plus lentement', 'Absorption un peu plus faible que le Fe²⁺', 'Même logique de dose', 'Un peu mieux toléré', 'Idem', 'Moins d’interactions alimentaires'],
  ['Fer IV : carboxymaltose ferrique (Ferinject®), dérisomaltose (Monofer®)', 'Livre le fer directement aux macrophages', 'Le fer est libéré en quelques jours ; la ferritine monte vite', 'Ferinject® ≤ 20 mg/kg et ≤ 1000 mg par perfusion, max 1000 mg par semaine (Swissmedic) ; 1re perfusion ≤ 500 mg selon mediX, surtout sans anémie ou si petit poids', 'Hypophosphatémie liée au facteur de croissance des fibroblastes 23 (FGF-23) (plus fréquente sous Ferinject®), réactions de perfusion, anaphylaxie très rare', 'Infection aiguë, 1er trimestre de grossesse, surcharge en fer', 'Aucune interaction alimentaire'],
 ], 9, 75, 11, 74, 73) +
 P('Correction de l’original : Maltofer® est du fer ferrique (polymaltose), pas du sulfate ferreux. La dose de 80 mg par jour de l’essai de Vaucher est une alternative.', 9, 12) +
 F('Situations particulières',
   TAB(['Situation', 'Particularité'], [
    ['Grossesse', 'Traiter dès ferritine < 15 µg/L, même sans anémie ; fer IV seulement à partir du 2e trimestre'],
    ['Personne âgée (≥ 80 ans)', '15 mg par jour peut suffire et est mieux toléré'],
    ['Enfant', 'Doses par kilo et formes liquides ; chercher une carence alimentaire'],
    ['Insuffisance rénale (DFGe bas)', 'Fer IV fréquent ; éviter de nouvelles perfusions si TSAT > 30 % ou ferritine > 500 µg/L'],
    ['Insuffisance hépatique', 'Prudence avec le fer IV ; chercher une hypertension portale qui saigne'],
    ['Carence sans anémie et fatigue', 'Bénéfice prouvé surtout si ferritine < 15 µg/L ; essai à discuter au cas par cas'],
   ]), 9, 12) +
 SOCIAL('Un arrêt de travail est rarement nécessaire ; il se discute pour une anémie sévère mal tolérée, le temps de la correction.',
        'L’anémie n’interdit pas la conduite, sauf vertiges ou syncope ; dans ce cas, s’abstenir jusqu’à correction (LCR art. 31).') +
 H4('11.C Surveillance et critères de sortie') +
 TAB(['Quand', 'Quoi'], [
  ['Après 4 semaines', 'Hémoglobine : elle doit avoir monté d’environ 20 g/L ; sinon vérifier l’observance, la perte, l’absorption'],
  ['Toutes les 4 semaines', 'Hémoglobine jusqu’à normalisation'],
  ['6–8 semaines après la dernière prise orale', 'Ferritine pour juger les réserves ; 12 semaines après un fer IV'],
  ['Arrêt du traitement', 'Quand la ferritine atteint 50–100 µg/L'],
  ['Critères de sortie (après transfusion)', 'Hémodynamique stable, saignement contrôlé, cause identifiée ou bilan programmé'],
 ]) + P('Ce rythme de suivi provient de la recommandation mediX ; aucune durée consensuelle n’existe pour la carence sans anémie.', 9) +
 H4('11.D Pronostic et recherche 2026') +
 P('Le pronostic est excellent si la cause est traitée ; il dépend sinon de la lésion causale. Les récidives sont fréquentes si les règles abondantes persistent.', 9) +
 P('Des molécules qui bloquent l’hepcidine sont en recherche, sans autorisation en Suisse en 2026. L’original les présentait comme un traitement prêt : c’est une surinterprétation.', 9))
ADD(12, 'Prévention',
 P('La prévention vise les terrains à risque. Elle passe par une alimentation riche en fer, le traitement des règles abondantes et une ferritine avant les dons de sang répétés.', 9) +
 F('Prévention primaire, secondaire et tertiaire',
   TAB(['Niveau', 'Mesure'], [
    ['Primaire', 'Alimentation riche en fer ; traitement des règles abondantes (stérilet au lévonorgestrel, par exemple)'],
    ['Secondaire', 'Hémogramme et ferritine si symptômes ou terrain à risque ; pas de dépistage généralisé sans symptômes'],
    ['Tertiaire', 'Traiter la cause, contrôler la ferritine, prévenir la récidive'],
   ]) + P('En Suisse, mediX ne recommande plus de dépistage systématique pendant la grossesse sans anémie ni facteur de risque ; l’original disait le contraire. Le dépistage du cancer du côlon de 50 à 69 ans est remboursé par l’assurance de base (OFSP).', 9, 42)))
ADD(13, 'Points clés',
 P('La ferritine basse prouve la carence en fer ; l’hémoglobine définit l’anémie. '
   'Une carence en fer est un symptôme : sa cause doit toujours être cherchée. '
   'Après 50 ans, une anémie ferriprive impose une coloscopie. '
   'Le fer oral se donne un jour sur deux, car l’hepcidine bloque l’absorption pendant environ 24 heures.', 9, 11))
ADD(14, 'Pièges d’examen',
 TAB(['Piège', 'Ce qu’il faut répondre'], [
  ['Donner du fer à un homme de 60 ans sans endoscopie', 'Non : il faut une coloscopie et une gastroscopie'],
  ['Croire que Maltofer® est du sulfate ferreux', 'Non : c’est du fer ferrique (polymaltose)'],
  ['Exclure une carence parce que la ferritine est à 80 µg/L avec une CRP élevée', 'Non : il faut la saturation de la transferrine'],
  ['Doser la ferritine pendant le traitement oral', 'Il faut attendre 6–8 semaines après la dernière prise'],
  ['Traiter toute fatigue avec ferritine à 40 µg/L', 'Non : le bénéfice est prouvé surtout sous 15 µg/L'],
  ['Prescrire du fer sans chercher une maladie cœliaque', 'Il faut les IgA anti-transglutaminase si la cause n’est pas évidente'],
 ]) + P('Ces pièges reprennent les erreurs les plus fréquentes signalées par la recommandation mediX.', 9))
CTX = {'_prefixe': 'Dans l’anémie ferriprive',
 'nfs': 'L’hémoglobine définit l’anémie ; un volume globulaire < 80 fL et des plaquettes hautes orientent vers le fer.',
 'ferritine': 'Une ferritine < 15 µg/L prouve la carence ; 15–30 µg/L signale des réserves réduites.',
 'crp': 'Une CRP élevée rend la ferritine faussement normale : on ajoute la saturation de la transferrine.',
 'tsat': 'Une TSAT ≤ 20 % confirme la carence quand la ferritine est faussée par l’inflammation.',
 'stfr': 'Le sTfR élevé distingue la carence en fer de l’anémie inflammatoire pure.',
 'ttg': 'Les IgA anti-transglutaminase positives expliquent une carence par malabsorption.',
 'endo': 'Après 50 ans, la coloscopie vient d’abord ; avant 50 ans, la gastroscopie avec biopsies.',
 'fit': 'Un FIT négatif ne dispense pas de coloscopie devant une anémie ferriprive.',
 'bom': 'La coloration de Perls montre l’absence de fer médullaire ; elle n’est plus nécessaire en pratique.',
 'b12': 'Une carence associée en B12 peut rendre l’anémie normocytaire.'}
if __name__ == '__main__':
    produire(M, PTS, SOURCES, CTX)
