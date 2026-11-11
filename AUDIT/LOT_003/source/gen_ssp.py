# -*- coding: utf-8 -*-
"""Appel A du LOT 3 : SSP G3 « Soif excessive et polydipsie » (14 points) + bloc 2 (liste des dix diagnostics), version AUDITÉE.
Sources : S1–S14 = Appel A V7 r1 (numérotation conservée) ; S15+ = audit du 24.10.2026 (src_lot3.py)."""
from lot3_commun import *
import gen_v7l
POINT = mkPOINT('ssp')
M = dict(pref='ssp', dx='SSP G3', court='Soif excessive et polydipsie', long='Soif excessive et polydipsie (situation clinique de départ)', dossier=DOSSIER,
         fichier='LOT_003_Appel_A_SSP_G3_Soif_excessive_polydipsie_AUDITÉ.html', lot_titre=LOT_TITRE,
         sous_titre='PROFILES 2023 · SSP G3 · LOT 3 · Appel A · V7 · version AUDITÉE (14 points et liste des dix diagnostics)',
         statut='Cette version corrige l’Appel A du LOT 3 (plan V7 et liste, version de travail r1 du 23.10.2026) après audit médical et linguistique. '
                'Corrections : liste du bloc 2 alignée sur les dix monographies de l’Appel B (l’AVP-D gestationnelle passe dans les situations spéciales) ; '
                'répartition des polyuries hypotoniques ajoutée (étude de 2018 : polydipsie primaire 57 %, AVP-D 41 %, AVP-R 2 %) ; seuil de copeptine basale de l’AVP-R sourcé (2015) ; '
                'doses absentes de l’original complétées depuis les monographies du lot, marquées à vérifier dans l’AIPS.')
_build = gen_v7l.build
def _build_ssp(*a, **k):
    return _build(*a, **k).replace('<a href="#ssp-p15">15</a>', '<a href="#ssp-p15">Dix DX</a>')
gen_v7l.build = _build_ssp

AVP = T('vasopressine (AVP)', 'L’arginine-vasopressine, ou hormone antidiurétique, est fabriquée par l’hypothalamus et libérée par la post-hypophyse ; elle fait réabsorber l’eau par le rein.')
COP = T('copeptine', 'La copeptine est un fragment du précurseur de la vasopressine, libéré en quantité égale ; plus stable, elle se dose facilement à sa place.')
OSM = T('osmolalité', 'L’osmolalité est la concentration en particules d’un liquide (mOsm/kg) ; elle dit si l’eau manque (haute) ou est en excès (basse).')
AQP = T('aquaporine 2', 'L’aquaporine 2 est un canal à eau que la vasopressine insère dans la membrane du tube collecteur.')
DIUOSM = T('diurèse osmotique', 'La diurèse osmotique est une perte d’eau entraînée par une substance non réabsorbée dans l’urine, comme le glucose ou le mannitol.')
PTS = []

# ---------- 1
p1 = (P('La polydipsie est une prise de boissons excessive, objectivable ; la soif est la sensation qui pousse à boire. '
        'Le SSP G3 de PROFILES 2023 demande de distinguer trois mesures : la soif, le volume bu et le volume urinaire. '
        'Une soif sans polyurie oriente vers une bouche sèche, alors qu’une polyurie vraie oriente vers le rein ou la vasopressine.', 1, 3) +
  F('Terminologie : mot courant et terme exact',
    TAB(['Mot courant', 'Terme exact', 'Définition', 'À ne pas confondre avec'], [
     ['Avoir tout le temps soif', 'Soif excessive', 'Sensation de besoin de boire', 'Bouche sèche (xérostomie) sans manque d’eau'],
     ['Boire beaucoup', 'Polydipsie', 'Prise de boissons excessive, mesurable', 'Habitude de boire sans soif'],
     ['Uriner beaucoup', 'Polyurie', 'Diurèse ≥ 3 L/24 h ou > 40–50 mL/kg/24 h chez l’adulte' + S(3, 27), 'Pollakiurie : mictions fréquentes de petit volume'],
     ['Uriner la nuit', 'Nycturie', 'Réveil nocturne pour uriner', 'Preuve de polyurie : elle ne l’est pas'],
     ['Urine « claire »', 'Polyurie hypotonique', 'Osmolalité urinaire ≤ 300 mOsm/kg' + S(3), 'Diurèse osmotique (≥ 800 mOsm/kg)'],
     ['Diabète insipide', 'AVP-D (central) ou AVP-R (rénal)', 'Nouveaux noms depuis 2022' + S(30), 'Diabète sucré'],
     ['Potomanie', 'Polydipsie primaire', 'Apport d’eau excessif, vasopressine freinée' + S(31), 'Déficit en vasopressine partiel'],
    ])) +
  F('Pourquoi ces mots changent la décision',
    UL(['Une pollakiurie fait chercher une infection ou un trouble vésical, pas un test hormonal.',
        'Une polyurie hypotonique fait chercher l’AVP-D, l’AVP-R ou une polydipsie primaire.',
        'Une diurèse osmotique fait d’abord mesurer la glycémie.']), 3))
PTS.append(POINT(1, 'Définition et sémantique', p1))

# ---------- 2
p2 = (P('Aucune donnée suisse ne chiffre la polydipsie comme symptôme. '
        'En Suisse, l’Obsan rapporte un diabète déclaré chez 6,2 % des personnes de 15 ans et plus en 2022, et une étude nationale une maladie rénale chronique chez ≈ 10,4 % des adultes. '
        'Parmi les polyuries hypotoniques explorées en centre, la polydipsie primaire prédomine.', 2, 45, 27) +
  F('Chiffres comparables (même unité : prévalence pour 100 000 habitants)',
    TAB(['Entité', 'Prévalence', 'Population et portée'], [
     ['Diabète déclaré (Suisse, ESS 2022)', '≈ 6200 / 100 000' + S(2), '≥ 15 ans ; 4,8 % en 2017 ; femmes 5,6 %, hommes 6,9 %'],
     ['Maladie rénale chronique (Suisse)', '≈ 10 400 / 100 000' + S(45), 'Adultes, tous stades'],
     ['Sécheresse buccale (méta-analyse)', '≈ 22 000 / 100 000' + S(38), 'Adultes, international'],
     ['Insuffisance cardiaque (Europe)', '1000–2000 / 100 000' + S(40), 'Adultes'],
     ['Hyperparathyroïdie primaire', '85–233 / 100 000' + S(49), 'Hommes à femmes, Amérique du Nord'],
     ['Syndrome de Sjögren primaire', '≈ 61 / 100 000' + S(37), 'International'],
     ['Déficit en vasopressine (AVP-D)', '≈ 4 / 100 000' + S(26), 'International'],
     ['Polydipsie primaire, AVP-R, polyurie iatrogène', 'non publiée en population générale' + S(31, 51), '—'],
    ]) + P('Ces prévalences ne sont pas la probabilité d’un diagnostic devant un patient qui boit trop.', 2, 26)) +
  F('Répartition dans une population de patients polyuriques (autre dénominateur)',
    TAB(['Diagnostic final', 'Part des 144 polyuries hypotoniques explorées', 'Population'], [
     ['Polydipsie primaire', '57 % (82/144)' + S(27), '11 centres en Suisse, Allemagne et Brésil, 2013–2017'],
     ['Déficit en vasopressine (AVP-D)', '41 % (59/144)' + S(27), 'Même cohorte'],
     ['Résistance à la vasopressine (AVP-R)', '2 % (3/144)' + S(27), 'Même cohorte'],
    ])) +
  F('Terrain, facteurs de risque et pronostic',
    TAB(['Terrain ou facteur de risque', 'Ce qu’il expose', 'Pronostic chiffré'], [
     ['Grand âge, démence, dépendance', 'Hypernatrémie par accès à l’eau limité', 'Urgences de Berne : natrémie > 145 mmol/L chez 2 % des 43 911 patients ; 21 décès sur 74 hypernatrémies sévères (≈ 28 %)' + S(34)],
     ['Lithium au long cours', 'AVP-R acquise', 'Défaut de concentration ≥ 54 %, polyurie franche 19 %' + S(94)],
     ['Diabète, surtout de type 1 ou sous gliflozine', 'Acidocétose, état hyperosmolaire', 'Urgence vitale ; mortalité selon le terrain' + S(7)],
     ['Trouble psychiatrique, sexe et âge sans effet démontré', 'Polydipsie primaire, intoxication par l’eau', 'Hyponatrémie sévère possible' + S(31)],
     ['Chirurgie hypophysaire, traumatisme crânien', 'AVP-D', 'Mortalité liée aux dysnatrémies et au déficit corticotrope' + S(26)],
    ])))
PTS.append(POINT(2, 'Épidémiologie (Suisse, puis Europe)', p2))

# ---------- 3
p3 = (P(f'Quand l’{OSM} du plasma monte, l’hypothalamus déclenche la soif et libère la {AVP}. '
        f'Celle-ci se fixe au récepteur V2 du tube collecteur, qui insère l’{AQP} et réabsorbe l’eau. '
        'La polyurie vient d’un manque d’hormone (AVP-D), d’un rein sourd à l’hormone (AVP-R), d’un excès d’eau bue ou d’une substance qui entraîne l’eau.', 3, 26, 64) +
  F('Chaîne logique : de l’anatomie au traitement',
    TAB(['Étape', 'Ce qu’il faut comprendre'], [
     ['Anatomie', 'Osmorécepteurs et noyaux supra-optiques de l’hypothalamus, tige, post-hypophyse ; tube collecteur du rein.'],
     ['Physiologie', 'Pourquoi on a soif : la soif et la vasopressine corrigent ensemble une osmolalité trop haute ; une baisse de volume artériel stimule aussi la soif.'],
     ['Physiopathologie', 'Glucose urinaire (diurèse osmotique), hormone absente (AVP-D), récepteur inefficace (AVP-R : lithium, calcium haut, potassium bas), excès d’eau bue (polydipsie primaire), bouche sèche sans perte d’eau.'],
     ['Clinique', 'D’où une polyurie jour et nuit, une soif d’eau froide, ou une soif sans polyurie.'],
     ['Examens', 'Diurèse des 24 h, osmolalités, glycémie, natrémie, puis copeptine : chaque mesure teste un maillon de la chaîne.'],
     ['Traitement', 'Insuline et perfusion, desmopressine, amiloride, arrêt d’un médicament ou réduction des boissons : chacun corrige son maillon.'],
    ]), 3, 26, 64) +
  F('Mécanisme (lésion), exploration et cible thérapeutique',
    TAB(['Mécanisme', 'Exploration qui le montre', 'Cible thérapeutique'], [
     [f'Glycosurie : {DIUOSM}', 'Glycémie, cétonémie, osmolalité urinaire ≥ 800', 'Insuline, perfusion' + S(7)],
     ['Défaut de sécrétion de vasopressine (AVP-D)', 'Copeptine stimulée ≤ 4,9 pmol/L', 'Desmopressine (agoniste V2)' + S(27)],
     ['Résistance du récepteur V2 (AVP-R)', 'Copeptine basale ≥ 21,4 pmol/L', 'Cause (lithium, calcium) ; thiazidique, amiloride' + S(28, 6)],
     ['Excès d’eau bue (polydipsie primaire)', 'Copeptine stimulée > 4,9 pmol/L, natrémie basse-normale', 'Réduction progressive des boissons' + S(27, 31)],
     ['Hypercalcémie, hypokaliémie', 'Calcémie corrigée, kaliémie', 'Correction de l’ion et de sa cause' + S(48)],
     ['Bouche sèche sans perte d’eau', 'Diurèse normale, revue des médicaments', 'Arrêt de l’anticholinergique, salive artificielle' + S(39)],
    ]) + P('Le mécanisme explique pourquoi la desmopressine aide l’AVP-D mais est dangereuse dans la polydipsie primaire.', 3, 31)))
PTS.append(POINT(3, 'Physiopathologie', p3))

# ---------- 4
p4 = (P('Le médecin cherche d’abord une urgence : acidocétose, état hyperosmolaire, hypernatrémie ou hyponatrémie symptomatique. '
        'Ensuite, il confirme la polyurie par la diurèse des 24 heures, puis mesure l’osmolalité urinaire. '
        'Enfin, il sépare diurèse osmotique, polyurie hypotonique et soif sans polyurie.', 3, 7) +
  DIFF([], 'Diagnostic différentiel (fréquences en exposant rouge, même unité : prévalence pour 100 000 habitants)') +
  F('Polyurie hypotonique explorée (même population : 144 patients de l’étude de 2018)',
    TAB(['Diagnostic', 'Copeptine', 'Indice décisif'], [
     ['Polydipsie primaire' + PR('57 %', 27), 'Stimulée > 4,9 pmol/L', 'Natrémie basse-normale, trouble psychiatrique fréquent'],
     ['AVP-D' + PR('41 %', 27), 'Stimulée ≤ 4,9 pmol/L', 'Début brutal, chirurgie ou lésion hypophysaire'],
     ['AVP-R' + PR('2 %', 27), 'Basale ≥ 21,4 pmol/L', 'Lithium, hypercalcémie, forme familiale'],
    ])) +
  F('Hiérarchie des urgences : danger, discriminant, action',
    TAB(['Danger', 'Discriminant', 'Action immédiate'], [
     ['Acidocétose diabétique', 'Cétonémie ≥ 3,0 mmol/L, pH < 7,3 ou bicarbonates < 18 mmol/L', 'Hôpital, perfusion, puis insuline' + S(7)],
     ['État hyperosmolaire', 'Osmolalité efficace > 300 mOsm/kg, sans acidose', 'Hôpital, perfusion' + S(7)],
     ['Hypernatrémie', 'Natrémie > 145 mmol/L, confusion', 'Eau libre, correction ≤ 10 mmol/L par 24 h si chronique' + S(32)],
     ['Hyponatrémie sévère symptomatique', 'Natrémie basse, convulsions, coma', 'NaCl 3 % 150 mL en 20 minutes' + S(62)],
    ])) +
  F('Ce qui mime une polyurie',
    P('Une infection urinaire, une hypertrophie prostatique ou une vessie hyperactive donnent des mictions fréquentes de petit volume. '
      'Le calendrier mictionnel et la diurèse des 24 heures évitent cette confusion.', 3)))
PTS.append(POINT(4, 'Raisonnement clinique et diagnostic différentiel', p4))

# ---------- 5
p5 = (P('L’entretien quantifie les boissons et les urines sur 24 heures, puis précise le début, la nycturie, le poids, les médicaments et les antécédents hypophysaires.', 3, 5, 7) +
  F('Questions et ce que la réponse change',
    TAB(['Question', 'Raison', 'Ce que la réponse change'], [
     ['Combien de litres buvez-vous et urinez-vous par jour ?', 'La sensation ne mesure pas le volume.', 'Une diurèse normale oriente vers une bouche sèche.'],
     ['Vous levez-vous la nuit pour uriner ou boire ?', 'Une polyurie hypotonique persiste la nuit.', 'Des mictions nocturnes de petit volume orientent vers la vessie.'],
     ['Le début a-t-il été brutal ?', 'Un début du jour au lendemain évoque l’AVP-D.', 'IRM hypophysaire si l’AVP-D se confirme.'],
     ['Avez-vous maigri, vomi ou respirez-vous vite ?', 'La carence en insuline produit des cétones.', 'Cétonémie et gaz du sang immédiats.'],
     ['Prenez-vous du lithium, un diurétique ou une gliflozine ?', 'Ces médicaments modifient la concentration ou font uriner.', 'Revue du traitement avec le prescripteur.'],
     ['Opération ou traumatisme de la tête, grossesse en cours ?', 'L’hypophyse ou le placenta modifient la vasopressine.', 'Avis endocrinien ou obstétrical.'],
     ['Avez-vous la bouche ou les yeux secs ?', 'Une xérostomie donne soif sans polyurie.', 'Revue des anticholinergiques, recherche d’un Sjögren.'],
     ['Préférez-vous l’eau glacée, même la nuit ?', 'Ce goût accompagne souvent l’AVP-D.', 'Indice, pas une preuve.'],
     ['Trouble psychiatrique ou conviction de « bien boire » ?', 'La polydipsie primaire en dépend souvent.', 'Recherche d’une hyponatrémie.'],
    ]), 3, 26, 31, 39) +
  U('<b>Drapeaux rouges et urgence (hospitalisation immédiate, 144 si coma)</b> : confusion, convulsions, coma, hypotension, vomissements avec respiration rapide, incapacité de boire. '
    'Ils imposent une natrémie et une glycémie immédiates ; aucune restriction hydrique ni desmopressine empirique à domicile.', 5, 7, 62))
PTS.append(POINT(5, 'Anamnèse ciblée et drapeaux rouges', p5))

# ---------- 6
p6 = (P('Le médecin mesure la conscience, la pression, le pouls, la température et le poids, puis cherche les signes de déshydratation et la cause. '
        'Il décrit le normal avant l’anomalie et confronte chaque signe à la biologie. '
        'Aucun signe isolé n’a de sensibilité ni de spécificité suffisantes pour mesurer le manque d’eau.', 5, 7, 32) +
  F('Technique, normal, anomalie et valeur',
    TAB(['Geste (technique)', 'Normal attendu', 'Anomalie et signification'], [
     ['Conscience : orientation, attention', 'Patient orienté', 'Confusion : dysnatrémie ou hyperosmolarité' + S(32, 62)],
     ['Pression et pouls couché puis debout', 'Stables', 'Hypotension, tachycardie : hypovolémie' + S(7)],
     ['Poids comparé au poids antérieur', 'Stable', 'Perte rapide avec polyurie : manque d’eau' + S(3)],
     ['Muqueuse buccale', 'Humide', 'Sèche : sensibilité et spécificité faibles chez la personne âgée' + S(32)],
     ['Respiration', 'Calme', 'Ample et rapide (Kussmaul) : acidocétose' + S(7)],
     ['Champ visuel au doigt', 'Complet', 'Hémianopsie bitemporale : lésion hypophysaire' + S(26)],
     ['Œdèmes, ascite, turgescence jugulaire', 'Absents', 'Soif non osmotique de l’insuffisance cardiaque ou de la cirrhose' + S(40, 41)],
     ['Glandes salivaires, yeux', 'Parotides souples, larmes', 'Parotides gonflées, yeux secs : Sjögren' + S(35)],
     ['Globe vésical', 'Absent', 'Rétention : risque de polyurie de levée d’obstacle' + S(46)],
    ])))
PTS.append(POINT(6, 'Examen clinique', p6))

# ---------- 7
p7 = (P('Les signes fonctionnels sont rapportés : soif, mictions abondantes, nycturie, fatigue. '
        'Les signes physiques sont constatés : hypotension, perte de poids, confusion, muqueuses sèches. '
        'Ils se groupent en quatre syndromes, chacun avec son mécanisme et son examen.', 3, 7) +
  F('Signes fonctionnels (rapportés par le patient)',
    UL(['Soif intense, parfois d’eau glacée', 'Mictions abondantes jour et nuit', 'Nycturie', 'Fatigue, crampes', 'Céphalées, nausées (hyponatrémie)']), 3, 62) +
  F('Signes physiques (constatés par le médecin)',
    UL(['Hypotension, tachycardie', 'Perte de poids rapide', 'Confusion, convulsions', 'Respiration de Kussmaul', 'Muqueuses sèches']), 7, 32) +
  F('Syndromes, signes et discriminant',
    TAB(['Syndrome', 'Signes', 'Mécanisme', 'Discriminant'], [
     ['Syndrome de diurèse osmotique', 'Soif, polyurie, amaigrissement', 'Le glucose urinaire entraîne l’eau', 'Glycémie, osmolalité urinaire ≥ 800' + S(7, 3)],
     ['Syndrome polyuro-polydipsique hypotonique', 'Polyurie jour et nuit, urine claire', 'Défaut d’action de la vasopressine ou excès d’eau', 'Osmolalité urinaire ≤ 300, copeptine' + S(3, 27)],
     ['Syndrome hyperosmolaire (hypernatrémie)', 'Somnolence, confusion, peu de soif chez l’âgé', 'Manque d’eau libre', 'Natrémie > 145 mmol/L' + S(32, 34)],
     ['Syndrome d’intoxication par l’eau', 'Céphalées, nausées, convulsions', 'Excès d’eau libre, œdème cérébral', 'Natrémie basse' + S(62, 31)],
    ])) +
  F('Comment rechercher les signes',
    P('La nycturie se documente par un calendrier mictionnel avec volumes ; une seule fréquence ne suffit pas. '
      'La tachycardie se mesure après repos, et les osmolalités se dosent au laboratoire.', 3)) +
  F('Termes', P('Termes : ' + T('nycturie', 'La nycturie est le fait de se lever la nuit pour uriner ; elle ne prouve pas une polyurie.') + ', '
               + T('respiration de Kussmaul', 'La respiration de Kussmaul est ample et rapide ; elle élimine du CO₂ pour compenser une acidose.') + '.', 3, 7)))
PTS.append(POINT(7, 'Syndromes et signes cliniques', p7))

# ---------- 8
p8 = (P('La SSP G3 n’a pas de critère unique : on prouve d’abord la polyurie, puis on identifie son mécanisme. '
        'Les critères de polyurie de la revue de 2025 et de l’étude de 2018 sont une diurèse ≥ 3 L/24 h ou > 50 mL/kg/24 h. '
        'Chaque cause garde ses critères : consensus de 2024 pour les crises du diabète, copeptine pour la vasopressine.', 3, 27, 7) +
  F('Critères et seuils par étape',
    TAB(['Étape', 'Critère et seuil', 'Ce qu’il ne démontre pas'], [
     ['Polyurie (adulte)', '≥ 3 L/24 h ou > 40–50 mL/kg/24 h' + S(3, 27), 'Ni un AVP-D, ni un diabète sucré'],
     ['Polyurie hypotonique', 'Osmolalité urinaire ≤ 300 mOsm/kg' + S(3), 'Ne sépare pas l’AVP-D de la polydipsie primaire'],
     ['Diurèse osmotique', 'Osmolalité urinaire ≥ 800 mOsm/kg' + S(3), 'Ne prouve pas que le glucose en est la cause'],
     ['Acidocétose (consensus 2024)', 'Glycémie ≥ 11,1 mmol/L ou diabète connu, β-hydroxybutyrate ≥ 3,0 mmol/L, pH < 7,3 ou bicarbonates < 18 mmol/L' + S(7), 'Une glycémie modérée ne l’exclut pas'],
     ['AVP-D (étude 2018)', 'Copeptine ≤ 4,9 pmol/L après NaCl 3 % (natrémie ≥ 150 mmol/L)' + S(27), 'Hors protocole, le seuil ne vaut pas'],
     ['AVP-R (étude 2015)', 'Copeptine basale ≥ 21,4 pmol/L sans privation d’eau' + S(28), 'Ne dispense pas de chercher lithium ou calcium'],
    ]) + P('Une soif, une nycturie ou une natrémie normale ne suffit pas à poser un diagnostic.', 3)))
PTS.append(POINT(8, 'Critères diagnostiques', p8))

# ---------- 9
P9 = (F('9.a Examens de référence (gold standard)',
   TAB(['Question', 'Examen de référence', 'Performance (sensibilité, spécificité, précision)', 'Limite'], [
    ['Y a-t-il une polyurie ?', 'Diurèse des 24 h avec volume', 'Mesure directe' + S(3), 'Recueil incomplet fréquent'],
    ['AVP-D ou polydipsie primaire ?', 'Copeptine après NaCl 3 %', 'Précision 96,5 %, contre 76,6 % pour la privation d’eau' + S(27), 'Centre expert, natrémie toutes les 30 min'],
    ['Alternative', 'Copeptine après arginine (60 min)', 'Seuil 3,8 pmol/L : précision 93 % en 2019 ; 74,4 % contre 95,6 % pour le NaCl 3 % en 2023' + S(29, 4), 'Moins précise'],
    ['AVP-R ?', 'Copeptine basale', '≥ 21,4 pmol/L : sensibilité et spécificité 100 % (petite série)' + S(28), 'Peu de patients étudiés'],
    ['Acidocétose ?', 'β-hydroxybutyrate sanguin et gaz du sang', 'Seuils du consensus 2024' + S(7), 'La cétonurie est moins spécifique'],
   ])) +
  F('9.b Première intention, deuxième intention',
   TAB(['Intention', 'Examen', 'Critère de passage'], [
    ['Première intention', 'Diurèse des 24 h, osmolalités plasmatique et urinaire, glycémie, natrémie, kaliémie, calcémie, créatinine', 'Toute soif avec polyurie probable' + S(3)],
    ['En urgence', 'Cétonémie, gaz du sang veineux', 'Vomissements, respiration rapide, glycémie élevée' + S(7)],
    ['Deuxième intention', 'Copeptine basale puis stimulée', 'Polyurie hypotonique confirmée' + S(27, 28)],
    ['Troisième intention', 'IRM hypothalamo-hypophysaire ; test génétique', 'AVP-D confirmé ; AVP-R de l’enfant' + S(26, 6)],
   ])) +
  F('9.c Prescription : indication, moment, préparation',
   UL(['Indication : la copeptine stimulée n’est demandée qu’après preuve d’une polyurie hypotonique.',
       'Moment : la copeptine basale se prélève sans restriction d’eau préalable.',
       'Préparation : arrêt de la desmopressine 24 h avant le test ; pas de NaCl 3 % si épilepsie ou insuffisance cardiaque.',
       'La diurèse des 24 h commence après une miction jetée et se termine par la première urine du lendemain.']), 27, 28, 3) +
  F('9.d Interprétation (valeurs SI)',
   TAB(['Mesure', 'Normal', 'Seuil', 'Signification et conduite'], [
    ['Natrémie', '135–145 mmol/L', '> 145 ; < 135', 'Manque d’eau ; excès d’eau : décision selon les symptômes' + S(32, 62)],
    ['Osmolalité urinaire', 'Variable selon les boissons', '≤ 300 ; ≥ 800 mOsm/kg', 'Hypotonique ; osmotique' + S(3)],
    ['Osmolalité efficace', '2 × Na + glucose', '> 300 mOsm/kg', 'État hyperosmolaire si glycémie très élevée' + S(7)],
    ['Copeptine stimulée', '—', '≤ 4,9 ; > 4,9 pmol/L', 'AVP-D ; polydipsie primaire' + S(27)],
   ])) +
  F('9.e Cas de figure',
   TAB(['Résultat', 'Signification', 'Conduite'], [
    ['Positif (copeptine stimulée ≤ 4,9)', 'AVP-D', 'IRM, bilan hypophysaire'],
    ['Négatif (diurèse < 3 L/24 h)', 'Pas de polyurie', 'Chercher une pollakiurie ou une bouche sèche'],
    ['Limite (osmolalité urinaire 300–800)', 'Zone grise', 'Avis endocrinien, test spécialisé'],
    ['Discordant (polyurie et natrémie normale)', 'Soif conservée qui compense', 'Ne pas exclure un AVP-D'],
   ]) + P('Exemple : Na 145 mmol/L et glycémie 20 mmol/L donnent 2 × 145 + 20 = 310 mOsm/kg.', 3, 7)) +
  F('9.f Alternatives et terrains particuliers',
   TAB(['Situation', 'Adaptation'], [
    ['Grossesse', 'Pas de NaCl 3 % sans équipe obstétrico-endocrinienne ; IRM sans gadolinium'],
    ['Enfant', 'Test génétique si AVP-R congénitale ; références adaptées à l’âge' + S(6)],
    ['DFGe < 30 mL/min/1,73 m² (insuffisance rénale)', 'Osmolalité urinaire basse attendue ; avis néphrologique' + S(44)],
    ['Produit de contraste iodé', 'Inutile au bilan ; l’IRM hypophysaire n’en utilise pas'],
    ['Stimulateur cardiaque', 'Compatibilité vérifiée avant IRM'],
   ]) + P('Ces adaptations demandent un protocole local écrit.', 3)))
p9 = (P('Le bilan de première intention se fait en même temps : diurèse des 24 h, osmolalités, glycémie, natrémie, kaliémie, calcémie et créatinine. '
        'La copeptine ne vient qu’ensuite, en centre expert. '
        'La référence est la copeptine après NaCl 3 %, plus précise que la privation d’eau.', 3, 27) + P9)
PTS.append(POINT(9, 'Examens complémentaires', p9))

# ---------- 10
p10 = (P('Si le patient est confus, hypotendu ou acidosique, alors il est hospitalisé avant tout test. '
         'Si la diurèse est normale, alors la soif vient de la bouche ou de la vessie. '
         'Si la polyurie est hypotonique, alors la copeptine sépare les trois causes.', 3, 7) +
  F('Embranchements et décisions',
    TAB(['Si…', 'Alors…', 'Contrôle suivant'], [
     ['Confusion, hypotension, cétones et acidose', 'Hôpital, perfusion, examens en parallèle', 'Natrémie, glycémie, pH répétés'],
     ['Diurèse < 3 L/24 h', 'Pollakiurie, infection, bouche sèche', 'Calendrier mictionnel'],
     ['Osmolalité urinaire ≥ 800 mOsm/kg', 'Diurèse osmotique : glycémie, médicaments', 'Glycosurie, cétonémie'],
     ['Osmolalité urinaire ≤ 300 mOsm/kg', 'Polyurie hypotonique', 'Copeptine basale'],
     ['Copeptine basale ≥ 21,4 pmol/L', 'AVP-R', 'Lithium, calcium, potassium'],
     ['Copeptine stimulée ≤ 4,9 pmol/L', 'AVP-D', 'IRM, bilan hypophysaire'],
     ['Copeptine stimulée > 4,9 pmol/L', 'Polydipsie primaire', 'Natrémie, prise en charge du comportement'],
     ['Osmolalité 300–800 ou résultats discordants', 'Ne pas conclure', 'Avis endocrinien'],
    ]) + P('Une seule valeur de laboratoire ne dicte jamais toute la prise en charge.', 3, 27, 28)))
PTS.append(POINT(10, 'Arbre décisionnel', p10))

# ---------- 11
FICHE_SSP = FICHE([
  ['Analogue V2 : desmopressine (Minirin®, Minirin® Melt)', 'Agoniste du récepteur V2 : insère l’aquaporine 2', 'Demi-vie ≈ 2–3 h ; action 6–12 h', 'AVP-D : Melt 60–120 µg au coucher puis 2–3 prises/j ; comprimés 0,1–0,2 mg 2–3 fois/j (à vérifier, AIPS)', 'Hyponatrémie, céphalées', 'Polydipsie primaire, hyponatrémie', 'AINS, carbamazépine, ISRS (hyponatrémie)'],
  ['Soluté hypertonique : NaCl 3 %', 'Élève la natrémie et retire l’eau du cerveau', 'Effet immédiat', 'Hyponatrémie sévère symptomatique : 150 mL IV en 20 min, jusqu’à 2 fois ; pas plus de 10 mmol/L le premier jour', 'Surcorrection, myélinolyse', 'Hyponatrémie asymptomatique chronique', 'Desmopressine, diurétiques'],
  ['Insuline rapide IV : insuline humaine (Actrapid®)', 'Freine la lipolyse et la cétogenèse', 'Demi-vie IV de quelques minutes', 'Acidocétose : 0,1 U/kg/h à débit fixe, après la kaliémie (protocole JBDS)', 'Hypoglycémie, hypokaliémie', 'Kaliémie < 3,5 mmol/L non corrigée', 'Aucune majeure'],
  ['Diurétique épargneur de potassium : amiloride (Comilorid-Mepha®, associé à l’hydrochlorothiazide)', 'Bloque le canal ENaC, porte d’entrée du lithium', 'Demi-vie ≈ 6–9 h (à vérifier)', 'AVP-R du lithium : 5–10 mg 1–2 fois/j (hors AIPS, à vérifier)', 'Hyperkaliémie', 'DFGe bas, hyperkaliémie', 'IEC, sartans : hyperkaliémie'],
 ], 14, 62, 16, 95, 100)
p11 = (P('La prise en charge traite d’abord l’urgence, car une dysnatrémie ou une acidocétose tue plus vite que la cause. '
         'Ensuite, elle corrige le mécanisme : insuline, desmopressine, arrêt d’un médicament ou réduction des boissons. '
         'Elle ne donne jamais de desmopressine ni de restriction d’eau à l’aveugle.', 5, 7, 31) +
  F('11.A Buts : formes compliquées (urgence) et non compliquées',
    P('Forme compliquée (acidocétose, hypernatrémie, hyponatrémie symptomatique) : c’est une urgence hospitalière, car le cerveau souffre des variations d’osmolalité.', 7, 62) +
    P('Objectifs chiffrés : natrémie chronique corrigée de ≤ 10 mmol/L par 24 h ; cétonémie < 0,6 mmol/L et pH > 7,3 pour lever l’acidocétose.', 32, 7) +
    P('Dans la forme non compliquée, le but est une diurèse et une soif compatibles avec une vie normale, sans hyponatrémie.', 3)) +
  F('11.B Moyens',
    F('Formes compliquées : chronologie aux urgences',
      OL(['Minute 0 : voies aériennes, conscience, pression, glycémie et natrémie au lit du patient.',
          'Première heure : si choc, NaCl 0,9 % avant toute eau libre ; kaliémie avant l’insuline.',
          'Heures suivantes : natrémie toutes les 4 heures pendant la réanimation, puis au moins toutes les 12 heures.',
          'Desmopressine seulement si l’AVP-D est prouvé, en surveillant la surcorrection.']), 5, 7, 16) +
    F('Formes non compliquées : mesures générales puis ordre',
      OL(['Éducation : calendrier des boissons et des urines, signes d’alerte.', 'Traitement de la cause : diabète, médicament, calcium, potassium.',
          'AVP-D : desmopressine avec échappement hebdomadaire.', 'Polydipsie primaire : réduction progressive des boissons, psychothérapie si besoin.',
          'AVP-R : régime pauvre en sel et en protéines, thiazidique ou amiloride selon la cause.']), 3, 6, 31, 91) +
    FICHE_SSP +
    SOCIAL('Un arrêt de travail est justifié pendant une décompensation ; la polyurie chronique demande des pauses et un accès libre aux toilettes et à l’eau.',
           'La conduite est suspendue après confusion, convulsion ou hypoglycémie sévère, selon les recommandations de la SSED pour le diabète.') + P('', 13) +
    F('Situations spéciales',
      TAB(['Situation', 'Adaptation'], [
       ['Grossesse et allaitement', 'AVP-D gestationnelle (vasopressinase placentaire) : la desmopressine reste active ; avis obstétrico-endocrinien' + S(26)],
       ['Personne âgée', 'Soif émoussée : risque d’hypernatrémie ; accès à l’eau organisé' + S(32)],
       ['Enfant', 'AVP-R congénitale : équipe pédiatrique et néphrologique' + S(6)],
       ['Insuffisance rénale (DFGe bas)', 'Amiloride évité ; doses adaptées selon l’AIPS' + S(55)],
       ['Insuffisance hépatique', 'Hyponatrémie de dilution fréquente : pas de NaCl 0,9 % pour la corriger' + S(41)],
      ]))) +
  F('11.C Surveillance et critères de sortie',
    TAB(['Quoi', 'Quand', 'Seuil d’action'], [
     ['Natrémie', 'Toutes les 4 h en réanimation, puis ≥ toutes les 12 h' + S(5), 'Variation > 10 mmol/L par 24 h : arrêt de la correction'],
     ['Natrémie sous desmopressine', 'J3, J7, 1 mois, puis régulièrement', 'Natrémie basse : arrêt temporaire de la dose' + S(91)],
     ['Bilan entrées-sorties', 'Chaque jour à l’hôpital', 'Polyurie persistante : réévaluation'],
     ['Lithémie, créatinine, calcémie', 'Selon le traitement', 'Hausse : avis spécialisé' + S(52)],
    ]) + H4('Critères de sortie, un par un') +
    OL(['La conscience et l’hémodynamique sont stables.', 'La natrémie évolue sans correction trop rapide.', 'Le patient peut boire et accéder à l’eau.',
        'Le traitement est concilié et compris.', 'Un suivi endocrinien ou néphrologique est fixé.']), 5, 10) +
  F('11.D Pronostic, guérison et recherche 2026',
    P('Le pronostic suit la cause : la polyurie du diabète guérit avec l’équilibre glycémique, l’AVP-D permanent se contrôle sans guérir. '
      'La recherche de 2025 propose un score clinique qui évite certains tests ; il doit encore être validé ailleurs.', 3, 11) +
    P('Dans la polydipsie primaire, le dulaglutide a réduit les boissons de 490 mL sur 8 heures dans un essai de 2021 ; il reste expérimental.', 77)))
PTS.append(POINT(11, 'Prise en charge', p11))

# ---------- 12
p12 = (P('La prévention primaire réduit le risque de diabète de type 2 selon les recommandations suisses de la SSED et protège les personnes âgées de la chaleur. '
         'La prévention secondaire mesure tôt glycémie et électrolytes devant une vraie polyurie. '
         'La prévention tertiaire évite l’hyponatrémie sous desmopressine et la déshydratation des patients dépendants.', 8, 68, 3, 91) +
  F('Niveaux de prévention',
    TAB(['Niveau', 'Mesure', 'Source'], [
     ['Primaire', 'Activité physique et poids ; plan canicule de l’OFSP pour les personnes âgées', 'SSED, OFSP' + S(8, 68)],
     ['Secondaire', 'Glycémie, natrémie et osmolalités dès qu’une polyurie est confirmée ; lithémie et créatinine sous lithium', 'Revue 2025, ISBD' + S(3, 52)],
     ['Tertiaire', 'Échappement hebdomadaire sous desmopressine, carte d’urgence, accès à l’eau', 'Society for Endocrinology' + S(5, 91)],
    ])))
PTS.append(POINT(12, 'Prévention', p12))

# ---------- 13
PTS.append(POINT(13, 'Points clés',
 P('Une soif ne prouve pas une polyurie : on mesure la diurèse des 24 heures. '
   'Une acidocétose ou une dysnatrémie passe avant tout test. '
   'Une urine hypotonique fait doser la copeptine en centre expert. '
   'La polydipsie primaire est la cause la plus fréquente des polyuries hypotoniques explorées. '
   'La desmopressine n’est jamais donnée à l’aveugle.', 3, 7, 27)))

# ---------- 14
PTS.append(POINT(14, 'Pièges d’examen',
 TAB(['Piège', 'Bonne réponse'], [
  ['Dix mictions de 50 mL par jour : polyurie ?', 'Non : c’est une pollakiurie ; mesurer la diurèse des 24 h.'],
  ['Natrémie normale chez un patient qui boit 6 L : AVP-D exclu ?', 'Non : une soif conservée compense les pertes.'],
  ['Desmopressine pour une polydipsie primaire ?', 'Non : le patient continue à boire et fait une hyponatrémie.'],
  ['Restriction d’eau empirique à domicile ?', 'Non : elle peut provoquer une hypernatrémie en cas d’AVP-D ou d’AVP-R.'],
  ['Glycémie à 12 mmol/L sous gliflozine : acidocétose exclue ?', 'Non : doser la cétonémie, l’acidocétose peut être euglycémique.'],
  ['Appliquer le seuil de l’arginine au test au NaCl 3 % ?', 'Non : chaque test a son propre seuil.'],
  ['IRM hypophysaire en premier ?', 'Non : diurèse, osmolalités et glycémie d’abord.'],
 ]) + P('Ces pièges entraînent le raisonnement et ne sont pas des questions officielles de l’examen fédéral.', 3, 7, 27)))

# ---------- Bloc 2 : dix diagnostics
L = lambda f, t: f'<a href="{f}">{t}</a>'
DXL = [
 ('DX.1', 'Diabète sucré décompensé (acidocétose, état hyperosmolaire)', 'LOT_003_DX1_Diabete_decompense_AUDITÉ_a.html', PR('≈ 6200 / 100 000 (diabète)', 2), 'Urgence la plus fréquente : la glycémie et la cétonémie tranchent en minutes.', (7, 2)),
 ('DX.2', 'Déshydratation hypernatrémique', 'LOT_003_DX2_Deshydratation_hypernatremique_AUDITÉ.html', PR('non publiée en population générale', 32), 'Danger vital chez la personne âgée qui ne peut pas boire.', (32, 34)),
 ('DX.3', 'Xérostomie et syndrome de Sjögren', 'LOT_003_DX3_Xerostomie_Sjogren_AUDITÉ.html', PR('≈ 22 000 / 100 000 (bouche sèche) ; Sjögren ≈ 61 / 100 000', 38, 37), 'Soif sans polyurie : le piège le plus fréquent.', (38, 35)),
 ('DX.4', 'Polydipsie primaire', 'LOT_003_DX4_Polydipsie_primaire_AUDITÉ.html', PR('non publiée en population générale', 31), '57 % des polyuries hypotoniques explorées en centre ; la desmopressine y est dangereuse.', (27, 31)),
 ('DX.5', 'Polyurie iatrogène', 'LOT_003_DX5_Polyurie_iatrogene_AUDITÉ.html', PR('non publiée en population générale', 54), 'Gliflozines, diurétiques, perfusions : la chronologie oriente.', (54, 78)),
 ('DX.6', 'Insuffisance cardiaque et cirrhose (soif non osmotique)', 'LOT_003_DX6_Insuffisance_cardiaque_cirrhose_AUDITÉ.html', PR('1000–2000 / 100 000 (insuffisance cardiaque)', 40), 'Soif avec œdèmes et hyponatrémie de dilution.', (40, 41)),
 ('DX.7', 'Hypercalcémie et hypokaliémie', 'LOT_003_DX7_Hypercalcemie_hypokaliemie_AUDITÉ.html', PR('85–233 / 100 000 (hyperparathyroïdie primaire)', 49), 'AVP-R acquise réversible quand l’ion se corrige.', (48, 47)),
 ('DX.8', 'Maladie rénale chronique, polykystose, levée d’obstacle', 'LOT_003_DX8_MRC_polykystose_levee_obstacle_AUDITÉ.html', PR('≈ 10 400 / 100 000 (maladie rénale chronique)', 45), 'Le rein malade ne concentre plus : nycturie.', (44, 46)),
 ('DX.9', 'Déficit en vasopressine (AVP-D)', 'LOT_003_DX9_Deficit_vasopressine_AVP_D_AUDITÉ.html', PR('≈ 4 / 100 000', 26), 'Début brutal ; 41 % des polyuries hypotoniques explorées ; copeptine stimulée.', (26, 27)),
 ('DX.10', 'Résistance à la vasopressine (AVP-R)', 'LOT_003_DX10_Resistance_vasopressine_AVP_R_AUDITÉ.html', PR('non publiée en population générale', 51), 'Lithium au long cours ; copeptine basale ≥ 21,4 pmol/L.', (28, 94)),
]
b15 = (P('Les dix diagnostics suivent un ordre de sécurité : urgences métaboliques d’abord, puis soif sans polyurie, polyuries hypotoniques et causes rénales. '
         'Le rang est pédagogique, car aucune donnée suisse ne chiffre la part de chaque cause.', 3, 1) +
  TAB(['Rang', 'Diagnostic et prévalence (pour 100 000 habitants)', 'Pourquoi il figure dans la liste'],
      [[d, L(f, n) + pr, j + S(*s)] for d, n, f, pr, j, s in DXL]) +
  F('Tableau comparatif : signe, examen, mécanisme, décision',
    TAB(['Diagnostic', 'Signe clé', 'Examen clé', 'Mécanisme', 'Décision immédiate'], [
     ['Diabète décompensé', 'Polyurie, amaigrissement, vomissements', 'Glycémie, cétonémie, pH', 'Diurèse osmotique', 'Hôpital si acidose'],
     ['Déshydratation hypernatrémique', 'Confusion, peu de soif', 'Natrémie > 145 mmol/L', 'Manque d’eau libre', 'Eau libre lente'],
     ['Xérostomie, Sjögren', 'Bouche sèche, diurèse normale', 'Revue des médicaments, anti-SSA', 'Salive diminuée', 'Arrêt de l’anticholinergique'],
     ['Polydipsie primaire', 'Boissons fluctuantes', 'Copeptine stimulée > 4,9', 'Excès d’eau bue', 'Pas de desmopressine'],
     ['Polyurie iatrogène', 'Début après un médicament', 'Chronologie, glycosurie', 'Glucose ou sel urinaire', 'Revue du traitement'],
     ['Insuffisance cardiaque, cirrhose', 'Œdèmes, ascite', 'NT-proBNP, natrémie', 'Volume artériel bas', 'Pas de NaCl 0,9 %'],
     ['Hypercalcémie, hypokaliémie', 'Constipation, faiblesse', 'Calcémie, PTH, kaliémie', 'Récepteur V2 inhibé', 'Corriger l’ion'],
     ['MRC, levée d’obstacle', 'Nycturie, globe vésical', 'Créatinine, échographie', 'Rein qui ne concentre plus', 'Compenser une partie des pertes'],
     ['AVP-D', 'Début brutal, eau glacée', 'Copeptine stimulée ≤ 4,9', 'Hormone absente', 'Desmopressine'],
     ['AVP-R', 'Lithium', 'Copeptine basale ≥ 21,4', 'Rein sourd à l’hormone', 'Amiloride, thiazidique'],
    ]), 3, 7, 27, 28) +
  F('Algorithme discriminant',
    OL(['Confusion, vomissements, respiration rapide ? Glycémie, cétonémie, natrémie : DX.1 ou DX.2.',
        'Diurèse des 24 h normale ? Bouche sèche : DX.3.',
        'Œdèmes ou ascite ? DX.6.',
        'Osmolalité urinaire ≥ 800 ? Glucose ou médicament : DX.1 ou DX.5.',
        'Calcium haut, potassium bas, créatinine élevée ? DX.7 ou DX.8.',
        'Polyurie hypotonique ? Copeptine : DX.4, DX.9 ou DX.10.']) +
    P('Plusieurs causes peuvent coexister ; une grossesse fait aussi évoquer une AVP-D gestationnelle.', 3, 26)))
PTS.append(f'<section class="point" id="ssp-p15"><h3><strong>Bloc 2 · Liste des dix diagnostics du LOT 3</strong></h3>\n{b15}</section>\n')

CTX = {'_prefixe': 'Devant une soif excessive',
 'osmo': 'L’osmolalité urinaire ≤ 300 mOsm/kg signe une polyurie hypotonique ; ≥ 800 une diurèse osmotique.',
 'iono': 'La natrémie dit si l’eau manque (> 145 mmol/L) ou est en excès (< 135 mmol/L).',
 'gly': 'Une glycémie élevée oriente vers une diurèse osmotique ; ≥ 11,1 mmol/L avec cétones fait chercher une acidocétose.',
 'cetone': 'Un β-hydroxybutyrate ≥ 3,0 mmol/L avec acidose définit l’acidocétose.',
 'gds': 'Le gaz du sang veineux donne le pH et les bicarbonates de l’acidocétose.',
 'creat': 'La créatinine et le DFGe cherchent une maladie rénale qui empêche de concentrer.',
 'copeptine': 'La copeptine basale ≥ 21,4 pmol/L signe l’AVP-R ; stimulée ≤ 4,9 pmol/L l’AVP-D.',
 'lithemie': 'La lithémie se contrôle chez tout patient sous lithium qui urine beaucoup.',
 'pth': 'La PTH précise la cause d’une hypercalcémie.',
 'hba1c': 'L’HbA1c dit si le diabète est ancien ou récent.',
 'irm': 'L’IRM hypophysaire cherche la cause d’un AVP-D confirmé.',
 'restriction': 'La privation d’eau est moins précise que la copeptine (76,6 % contre 96,5 %).',
 'ecbu': 'L’ECBU cherche une infection devant des mictions fréquentes de petit volume.',
 'schirmer': 'Le test de Schirmer mesure les larmes devant une bouche et des yeux secs.',
 'bnp': 'Le NT-proBNP oriente vers une insuffisance cardiaque devant une soif avec œdèmes.',
 'echorein': 'L’échographie rénale cherche une polykystose ou un obstacle.',
 'hcg': 'Le test de grossesse précède l’imagerie et oriente vers une AVP-D gestationnelle.',
}
if __name__ == '__main__':
    produire(M, PTS, SOURCES, CTX)
