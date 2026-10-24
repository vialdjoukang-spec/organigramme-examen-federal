# -*- coding: utf-8 -*-
"""Appel A du LOT 4 : SSP G4 « Fatigue, épuisement » (14 points) + bloc 2 (liste des dix diagnostics), version AUDITÉE.
L'original V5 n'avait aucune source : toutes les références viennent de src_lot4.py (audit du 24.10.2026)."""
from lot4_commun import *
import gen_v7l
POINT = mkPOINT('ssp')
M = dict(pref='ssp', dx='SSP G4', court='Fatigue, épuisement', long='Fatigue et épuisement (situation clinique de départ)', dossier=DOSSIER,
         fichier='LOT_004_Appel_A_SSP_G4_Fatigue_epuisement_AUDITÉ.html', lot_titre=LOT_TITRE,
         sous_titre='PROFILES 2023 · SSP G4 · LOT 4 · Appel A · V7 · version AUDITÉE (14 points et liste des dix diagnostics)',
         statut='Cette version corrige l’Appel A du LOT 4 (export Google Docs V5, sans sources) après audit médical et linguistique ; toutes les sources ont été ajoutées par l’audit. '
                'Corrections : la fatigue concerne 11–33 % des patients de premier recours, et une cause est trouvée chez 50–60 % d’entre eux (et non 30–40 %) ; '
                'il n’existe pas de « critères de l’Organisation mondiale de la santé » pour la fatigue chronique, ce sont ceux de l’Institute of Medicine (2015) et du NICE (2021) ; '
                'le pacing n’est pas une activité physique graduée, que le NICE déconseille ; les pourcentages non sourcés du bloc 2 sont remplacés par des prévalences sourcées de même unité.')
_build = gen_v7l.build
def _build_ssp(*a, **k):
    return _build(*a, **k).replace('<a href="#ssp-p15">15</a>', '<a href="#ssp-p15">Dix DX</a>')
gen_v7l.build = _build_ssp

FAT = T('asthénie', 'L’asthénie est le terme médical de la fatigue : une baisse de l’énergie physique ou mentale, disproportionnée à l’effort et non soulagée par le repos.')
MPE = T('malaise post-effort', 'Le malaise post-effort est une aggravation des symptômes 12–48 heures après un effort, même modeste, qui dure des jours ; il est le signe cardinal de l’encéphalomyélite myalgique.')
HEP = T('hepcidine', 'L’hepcidine est une hormone du foie qui bloque la sortie du fer de l’intestin ; elle augmente lors d’une inflammation.')
SOMN = T('somnolence', 'La somnolence est une envie de dormir pendant la journée ; elle se distingue de la fatigue, qui est un manque d’énergie sans endormissement.')
PTS = []
def ADD(*a): PTS.append(POINT(*a))

# ---------- 1
ADD(1, 'Définition et sémantique',
 P('La fatigue, ou ' + FAT + ', est un manque d’énergie physique ou mentale qui gêne la vie quotidienne. '
   'Elle se distingue de la fatigue physiologique, car elle est disproportionnée à l’effort et ne cède pas au repos. '
   'Le SSP G4 de PROFILES 2023 demande d’en trouver la cause, sans oublier une maladie grave.', 1, 3, 10) +
 F('Terminologie : mot courant et terme exact',
   TAB(['Mot courant', 'Terme exact', 'Définition', 'À ne pas confondre avec'], [
    ['Être fatigué', 'Asthénie', 'Manque d’énergie non soulagé par le repos', 'Fatigue normale après un effort'],
    ['S’endormir partout', 'Somnolence diurne', 'Envie de dormir le jour (échelle d’Epworth)', 'Fatigue sans endormissement'],
    ['Ne plus avoir de force', 'Faiblesse musculaire', 'Baisse de la force mesurable à l’examen', 'Asthénie, où la force est normale'],
    ['Être à bout au travail', 'Épuisement professionnel (burn-out)', 'Phénomène lié au travail, code QD85 de la CIM-11 (Classification internationale des maladies), non classé comme maladie', 'Dépression caractérisée'],
    ['Fatigue qui dure', 'Fatigue chronique', 'Fatigue de plus de 6 mois', 'Encéphalomyélite myalgique, qui exige d’autres critères'],
    ['« Crash » après un effort', 'Malaise post-effort', 'Aggravation retardée après un effort', 'Courbatures normales'],
   ]) + P('Il faut distinguer la fatigue de la somnolence et de la faiblesse, car chacune oriente vers d’autres causes.', 3, 45, 47)) +
 F('Durée de la plainte', TAB(['Durée', 'Terme'], [['≤ 1 mois', 'Fatigue aiguë'], ['1–6 mois', 'Fatigue subaiguë ou prolongée'], ['> 6 mois', 'Fatigue chronique']]) +
   P('Ces durées sont celles de la recommandation suisse mediX.', 10)))

# ---------- 2
ADD(2, 'Épidémiologie (Suisse, puis Europe)',
 P('En Suisse, 11–33 % des patients de premier recours se plaignent de fatigue. '
   'Dans la cohorte lausannoise (CoLaus), 21,9 % des personnes de 45–86 ans se disent fatiguées. '
   'Une cause est trouvée chez 50–60 % des patients ; l’original annonçait à tort 30–40 %.', 3, 5, 4) +
 F('Chiffres, terrain et pronostic',
   TAB(['Donnée', 'Valeur', 'Population et portée'], [
    ['Patients de premier recours qui se plaignent de fatigue', '11–33 %' + S(3), 'Suisse, Revue Médicale Suisse 2006'],
    ['Fatigue en population générale', '21,9 %' + S(5), 'Lausanne, 45–86 ans (CoLaus)'],
    ['Vitalité et énergie fortes', 'Hommes 50,5 %, femmes 40,1 %' + S(51), 'Suisse, Enquête suisse sur la santé 2022'],
    ['Épuisement émotionnel au travail', '30,3 %' + S(7), 'Actifs occupés de 16–65 ans, Suisse 2022'],
    ['Cause retrouvée chez le patient fatigué', '50–60 %' + S(4), 'Suisse, premier recours'],
    ['« 10–20 % des consultations » (original)', 'Non retrouvé', 'Remplacé par la donnée sourcée ci-dessus'],
   ]) + P('Les données internationales vont dans le même sens : la revue de Stadje (2016) trouve une dépression chez 18,5 % et un cancer chez 0,6 % des patients fatigués.', 2) +
   P('Le terrain compte : la fatigue est plus fréquente chez la femme, en cas de dépression, d’anémie ou d’obésité, mais elle n’est pas liée à la thyréostimuline (TSH) dans CoLaus. '
     'Le pronostic dépend de la cause ; la mortalité propre de la fatigue n’est pas chiffrée dans les sources.', 5)) +
 DIFF([]))

# ---------- 3
ADD(3, 'Physiopathologie',
 P('La fatigue n’a pas un mécanisme unique. Elle provient d’un manque d’oxygène ou d’énergie pour les cellules, d’une inflammation, d’un trouble hormonal, d’un mauvais sommeil ou d’une maladie de l’humeur. '
   'Comprendre le mécanisme explique le signe et dit quel examen demander.', 2, 3) +
 F('Chaîne logique : de l’anatomie au traitement',
   TAB(['Étape', 'Ce qu’il faut comprendre'], [
    ['Anatomie', 'Le muscle, le cœur, le rein, la thyroïde, les surrénales et le cerveau participent tous à l’énergie disponible.'],
    ['Physiologie', 'L’hémoglobine transporte l’oxygène ; les hormones thyroïdiennes règlent la vitesse du métabolisme ; le cortisol maintient la tension et la glycémie ; le sommeil restaure le cerveau.'],
    ['Physiopathologie', 'Une anémie diminue l’oxygène livré au muscle. Une hypothyroïdie ralentit le métabolisme. Les cytokines de l’inflammation (interleukines 1 et 6, facteur de nécrose tumorale) agissent sur le cerveau et provoquent la fatigue.'],
    ['Clinique', 'D’où l’essoufflement de l’anémie, la frilosité de l’hypothyroïdie, l’hypotension de l’Addison, la somnolence des apnées.'],
    ['Examens', 'On mesure ce qui manque : hémoglobine, ferritine, TSH, glycémie, créatinine, protéine C réactive (CRP).'],
    ['Traitement', 'On corrige la cause ; il n’existe pas de traitement général de la fatigue.'],
   ]), 2, 3) +
 F('Mécanisme, lésion, exploration et cible thérapeutique',
   TAB(['Mécanisme', 'Lésion ou cause', 'Exploration', 'Cible thérapeutique'], [
    ['Moins d’oxygène livré', 'Anémie, insuffisance cardiaque', 'Hémogramme, NT-proBNP', 'Fer, traitement cardiaque'],
    ['Métabolisme ralenti', 'Hypothyroïdie', 'TSH, T4 libre', 'Lévothyroxine'],
    ['Inflammation, cytokines', 'Infection, cancer, maladie inflammatoire', 'CRP, examen complet', 'Traiter la maladie'],
    ['Manque de cortisol', 'Maladie d’Addison', 'Cortisol et hormone corticotrope (ACTH) du matin', 'Hydrocortisone'],
    ['Toxines urémiques, anémie rénale', 'Maladie rénale chronique', 'Créatinine, débit de filtration glomérulaire estimé (DFGe)', 'Néphroprotection'],
    ['Sommeil fragmenté', 'Apnées du sommeil', 'Questionnaires, polygraphie', 'Pression positive continue'],
    ['Humeur et motivation diminuées', 'Dépression, épuisement', 'Questionnaire PHQ-9 (Patient Health Questionnaire)', 'Psychothérapie, antidépresseur'],
   ]) + P('L’original parlait d’une « carence en adénosine triphosphate (ATP) par hypothyroïdie » et d’un « hypercortisolisme de stress » : ce sont des simplifications ; le lien entre stress et cortisol reste une hypothèse.', 3, 21)) +
 F('Fenêtre de calcul : constantes érythrocytaires et fer',
   TAB(['Grandeur', 'Formule', 'Valeur normale et seuil'], [
    ['Volume globulaire moyen (VGM)', 'Hématocrite (%) × 10 / érythrocytes (T/L)', '80–100 fL ; < 80 : microcytose (fer, thalassémie) ; > 100 : macrocytose (B12, folates, alcool, hypothyroïdie)'],
    ['Saturation de la transferrine', 'Fer sérique / capacité totale de fixation × 100', '20–45 % ; ≤ 20 % : carence si inflammation'],
    ['Hémoglobine', 'Mesurée', 'Anémie si < 120 g/L (femme) ou < 130 g/L (homme), selon l’OMS (Organisation mondiale de la santé)'],
    ['Ferritine', 'Mesurée', '< 15 µg/L : réserves épuisées ; 15–30 µg/L : réserves réduites'],
   ]) + P('Ces seuils sont ceux de mediX 2025 ; l’original donnait des normes « 140–180 g/L » sans source, retirées.', 9)))

# ---------- 4
ADD(4, 'Raisonnement clinique et diagnostic différentiel',
 P('Le médecin écarte d’abord une urgence : anémie sévère, saignement, hyperkaliémie, insuffisance surrénale aiguë, idées suicidaires. '
   'Ensuite, il sépare la fatigue isolée de la fatigue accompagnée de fièvre, de perte de poids ou de douleurs. '
   'Puis il cherche une cause somatique et psychique en même temps.', 2, 3, 58) +
 U('Correction : l’original classait la néoplasie occulte et l’insuffisance cardiaque terminale parmi les urgences ; ce sont des diagnostics à ne pas manquer, pas des urgences immédiates.', 2) +
 DIFF_FAT() +
 F('Étapes ordonnées du raisonnement',
   OL(['Urgence vitale ? Pouls, tension, conscience, idées suicidaires : si oui, hospitaliser ou appeler le 144.',
       'Drapeaux rouges ? Perte de poids, sueurs, fièvre, ganglions, saignement : bilan rapide.',
       'Somnolence plutôt que fatigue ? Échelle d’Epworth, apnées.',
       'Humeur triste, anhédonie ? PHQ-9.',
       'Bilan sanguin de base, puis examens orientés.',
       'Fatigue sans cause après 6 mois : critères d’encéphalomyélite myalgique.']), 2, 3, 10))

# ---------- 5
ADD(5, 'Anamnèse ciblée et drapeaux rouges',
 P('L’anamnèse précise la durée, l’effet du repos et le retentissement sur le travail. '
   'Elle demande la qualité du sommeil, l’humeur, les médicaments, l’alcool et les règles. '
   'Elle recherche les symptômes qui orientent vers un organe.', 3, 10) +
 U('Drapeaux rouges : perte de poids inexpliquée, sueurs nocturnes, fièvre prolongée, ganglions, saignement, dyspnée de repos, idées suicidaires. Ils imposent un bilan rapide ; une idée suicidaire avec plan ou une instabilité impose une prise en charge immédiate (144).', 2, 44) +
 F('Questions ciblées et leur raison',
   TAB(['Question', 'Pourquoi la poser'], [
    ['Depuis quand êtes-vous fatigué, et le repos vous aide-t-il ?', 'Durée et caractère pathologique'],
    ['Vous endormez-vous en lisant ou en conduisant ?', 'Somnolence : apnées du sommeil'],
    ['Avez-vous perdu l’envie et le plaisir ? Pensez-vous à mourir ?', 'Dépression et risque suicidaire'],
    ['Avez-vous perdu du poids, transpiré la nuit, eu de la fièvre ?', 'Cancer, infection'],
    ['Vos règles sont-elles abondantes ? Avez-vous vu du sang dans les selles ?', 'Carence en fer'],
    ['Votre fatigue s’aggrave-t-elle un ou deux jours après un effort ?', 'Malaise post-effort'],
    ['Quels médicaments, quel alcool, quelles drogues prenez-vous ?', 'Cause médicamenteuse ou toxique'],
   ]) + P('Le PHQ-9 quantifie l’humeur ; un score ≥ 10 signale des symptômes modérés.', 43)))

# ---------- 6
ADD(6, 'Examen clinique',
 P('L’examen est complet, car la fatigue peut venir de tous les organes. '
   'Il note d’abord les valeurs normales : pouls 60–100/min, tension, poids et indice de masse corporelle. '
   'Il inspecte la peau, palpe la thyroïde, les ganglions et l’abdomen, ausculte le cœur et les poumons.', 3) +
 F('Signes, technique et valeur',
   TAB(['Signe', 'Technique', 'Ce qu’il signifie'], [
    ['Pâleur conjonctivale', 'Abaisser la paupière à la lumière du jour', 'Anémie ; sensibilité faible, spécificité meilleure'],
    ['Goitre', 'Palper la thyroïde pendant la déglutition', 'Maladie thyroïdienne'],
    ['Ganglions > 1 cm, durs', 'Palper les aires cervicales, axillaires, inguinales', 'Lymphome, infection'],
    ['Hépatosplénomégalie', 'Palpation et percussion de l’abdomen', 'Mononucléose, hémopathie'],
    ['Mélanodermie, hypotension orthostatique', 'Inspecter les plis et les gencives ; tension couchée puis debout', 'Maladie d’Addison'],
    ['Œdèmes, crépitants', 'Godet, auscultation des bases', 'Insuffisance cardiaque'],
    ['Faiblesse objective', 'Testing musculaire', 'Maladie neuromusculaire, pas une asthénie'],
   ]) + P('Aucun signe isolé n’a une valeur suffisante ; l’examen oriente les examens complémentaires.', 2, 3)))

# ---------- 7
ADD(7, 'Syndromes et signes cliniques',
 F('Signes fonctionnels (symptômes rapportés)', UL(['Fatigue, endurance diminuée', 'Sommeil non réparateur ou somnolence', 'Essoufflement, palpitations', 'Troubles de la concentration', 'Tristesse, perte d’envie']), 3) +
 F('Signes physiques (constatés à l’examen)', UL(['Pâleur', 'Goitre, peau sèche', 'Ganglions, hépatosplénomégalie', 'Œdèmes', 'Mélanodermie, hypotension']), 3) +
 P('Le syndrome anémique réunit fatigue, pâleur, essoufflement d’effort, palpitations et céphalées. '
   'Le syndrome dépressif réunit humeur triste, anhédonie, fatigue souvent matinale et troubles du sommeil.', 9, 44) +
 F('Syndrome anémique', TAB(['Signe', 'Mécanisme', 'Valeur'], [
    ['Dyspnée d’effort', 'Moins d’oxygène par litre de sang', 'Dépend de la vitesse d’installation'],
    ['Tachycardie', 'Le cœur augmente son débit', 'Marquée si anémie rapide'],
    ['Pâleur', 'Moins d’hémoglobine dans la peau', 'Spécifique, peu sensible'],
   ]), 9) +
 F('Syndrome dépressif', TAB(['Signe', 'Mécanisme', 'Valeur'], [
    ['Anhédonie', 'Circuit de la récompense moins actif', 'Signe central'],
    ['Fatigue matinale', 'Rythme veille-sommeil perturbé', 'Évocatrice'],
    ['Idées de mort', 'Désespoir', 'Toujours les chercher'],
   ]), 44) +
 F('Syndrome d’apnées du sommeil', TAB(['Signe', 'Mécanisme', 'Valeur'], [
    ['Somnolence', 'Micro-éveils répétés qui fragmentent le sommeil', 'Échelle d’Epworth > 10'],
    ['Ronflement, apnées vues', 'Fermeture du pharynx pendant le sommeil', 'Questionnaire Stop-Bang'],
   ]), 47, 48))

# ---------- 8
ADD(8, 'Critères diagnostiques',
 P('La fatigue est un symptôme et n’a pas de critère propre. '
   'Selon la recommandation de l’Institute of Medicine (IOM, 2015), l’encéphalomyélite myalgique exige 6 mois de fatigue, un malaise post-effort et un sommeil non réparateur. '
   'Une fatigue de plus de 6 mois ne suffit pas à poser ce diagnostic.', 34, 33) +
 F('Critères de l’encéphalomyélite myalgique (IOM 2015 et NICE 2021)',
   TAB(['Critère', 'IOM 2015', 'NICE 2021 (National Institute for Health and Care Excellence)'], [
    ['Durée', '≥ 6 mois', '≥ 3 mois'],
    ['Fatigue avec baisse nette des activités', 'Obligatoire', 'Obligatoire'],
    ['Malaise post-effort', 'Obligatoire', 'Obligatoire'],
    ['Sommeil non réparateur', 'Obligatoire', 'Obligatoire'],
    ['Troubles cognitifs ou intolérance orthostatique', 'L’un des deux', 'Troubles cognitifs obligatoires'],
   ]) + P('Correction : l’original attribuait ces critères à l’OMS ; l’OMS ne publie pas de critères de fatigue chronique.', 34, 33)) +
 F('Critères qui définissent les causes fréquentes',
   TAB(['Cause', 'Critère et seuil', 'Source'], [
    ['Anémie', 'Hémoglobine < 120 g/L (femme), < 130 g/L (homme)', 'OMS, mediX 2025' + S(9)],
    ['Carence en fer', 'Ferritine < 15 µg/L (épuisée) ou 15–30 µg/L (réduite)', 'mediX 2025' + S(9)],
    ['Dépression', 'PHQ-9 ≥ 10 : symptômes modérés ; diagnostic par entretien', 'Kroenke 2001' + S(43)],
    ['Apnées du sommeil modérées', 'Index d’apnées-hypopnées ≥ 15/h', 'AASM 2012 (American Academy of Sleep Medicine)' + S(17)],
   ])))

# ---------- 9
ADD(9, 'Examens complémentaires',
 H4('9.a Examen de référence') +
 P('Il n’existe pas d’examen de référence de la fatigue : le diagnostic est un processus d’exclusion. '
   'Chaque examen n’a de sensibilité et de spécificité que pour une cause ; par exemple, une ferritine < 15 µg/L a une spécificité proche de 100 % pour la carence en fer.', 2, 9) +
 H4('9.b Examens de première et de deuxième intention') +
 P('En première intention, devant une fatigue de plus d’un mois, on demande un bilan sanguin court. '
   'En deuxième intention, on choisit les examens selon les signes trouvés, parce qu’un bilan large produit surtout des faux positifs.', 3, 10) +
 TAB(['Intention', 'Examen', 'Pourquoi'], [
  ['1re', 'Hémogramme (formule sanguine complète)', 'Anémie, signes d’hémopathie'],
  ['1re', 'Ferritine', 'Carence en fer'],
  ['1re', 'TSH', 'Hypothyroïdie'],
  ['1re', 'CRP', 'Inflammation, qui fausse la ferritine'],
  ['1re', 'Glycémie', 'Diabète'],
  ['1re', 'Créatinine et DFGe, ionogramme', 'Maladie rénale, hyponatrémie'],
  ['2e', 'Bilan hépatique', 'Hépatite, alcool'],
  ['2e', 'Vitamine B12', 'Macrocytose, régime végétalien'],
  ['2e', 'Sérologie du virus d’Epstein-Barr (EBV), test VIH (virus de l’immunodéficience humaine)', 'Fatigue post-infectieuse, primo-infection'],
  ['2e', 'Polygraphie ventilatoire', 'Apnées du sommeil'],
  ['2e', 'Cortisol du matin', 'Maladie d’Addison'],
  ['2e', 'NT-proBNP', 'Insuffisance cardiaque'],
 ]) + P('L’original citait l’hépatite C sans critère : la sérologie se demande en cas de facteur de risque ou de transaminases élevées.', 3) +
 H4('9.c Prescription') +
 P('Indication : fatigue de plus d’un mois, ou drapeau rouge quelle que soit la durée. Moment : le matin, à distance d’une infection aiguë ; le cortisol se dose vers 8 h. '
   'Préparation : aucun jeûne pour le bilan de base ; arrêt du fer oral 1 semaine avant un contrôle de ferritine.', 9, 10, 37) +
 H4('9.d Interprétation : normal, seuil, signification, conduite') +
 TAB(['Examen', 'Normal (SI)', 'Seuil', 'Signification', 'Conduite'], [
  ['Hémoglobine', '120–160 g/L (femme)', '< 120 g/L', 'Anémie', 'VGM, ferritine'],
  ['Ferritine', '30–300 µg/L', '< 30 µg/L', 'Carence en fer', 'Chercher la cause'],
  ['TSH', '≈ 0,4–4 mU/L', '> 4 mU/L', 'Hypothyroïdie possible', 'T4 libre'],
  ['CRP', '< 5 mg/L', '> 10 mg/L', 'Inflammation', 'Chercher une infection ou une tumeur'],
  ['DFGe', '> 90 mL/min/1,73 m²', '< 60', 'Maladie rénale si > 3 mois', 'Albuminurie'],
 ]) + P('Les normes dépendent du laboratoire ; celles-ci sont des repères.', 9, 27) +
 H4('9.e Cas de figure') +
 TAB(['Situation', 'Interprétation', 'Conduite'], [
  ['Positif : un examen anormal explique la fatigue', 'Cause probable', 'Traiter et réévaluer la fatigue'],
  ['Négatif : bilan normal', 'Cause somatique fréquente peu probable', 'Sommeil, humeur, suivi dans le temps'],
  ['Limite : TSH à 5 mU/L', 'Anomalie fruste', 'Contrôler à 6–12 semaines'],
  ['Discordant : ferritine 80 µg/L et CRP haute', 'Carence masquée par l’inflammation', 'Saturation de la transferrine'],
 ]) +
 H4('9.f Alternatives') +
 P('Grossesse : normes propres de l’hémoglobine et de la TSH. Enfant : normes d’âge. DFGe bas : la saturation de la transferrine complète la ferritine. '
   'Un produit iodé ou une IRM (imagerie par résonance magnétique) ne servent qu’à chercher une cause ciblée ; un pacemaker n’empêche pas la polygraphie.', 9, 61))

# ---------- 10
ADD(10, 'Arbre décisionnel',
 P('Si une urgence est présente, alors le patient est adressé à l’hôpital. Sinon, le médecin fait le bilan de base. '
   'Si le bilan est normal, il évalue le sommeil et l’humeur ; si la fatigue dure plus de 6 mois, il vérifie les critères d’encéphalomyélite myalgique.', 3, 10, 34) +
 F('Arbre décisionnel : adulte fatigué',
   OL(['Instabilité, idée suicidaire, saignement : 144 ou hôpital.',
       'Drapeau rouge : bilan rapide orienté → imagerie, avis spécialisé.',
       'Bilan de base anormal → traiter la cause (fer, lévothyroxine, diabète, rein).',
       'Somnolence, Epworth > 10 → polygraphie.',
       'PHQ-9 ≥ 10 → entretien et traitement de la dépression.',
       'Tout normal → suivi à 4–6 semaines, conseils de sommeil et d’activité adaptée.',
       'Plus de 6 mois, malaise post-effort → critères IOM 2015, pacing.']), 2, 3, 10, 34))

# ---------- 11
ADD(11, 'Prise en charge',
 H4('11.A Buts : d’abord l’urgence (anémie mal tolérée, insuffisance surrénale aiguë, risque suicidaire), car elle peut tuer en quelques heures') +
 P('Le but est de traiter la cause, de restaurer l’autonomie et d’éviter le déconditionnement. '
   'La cible dépend de la cause : par exemple, une ferritine de 50–100 µg/L après une carence en fer.', 9) +
 H4('11.B Moyens : forme compliquée en urgence, puis forme non compliquée en ambulatoire') +
 P('La forme compliquée relève de l’hôpital dans l’heure : transfusion d’une anémie mal tolérée, hydrocortisone 100 mg IV d’une crise surrénalienne. '
   'La forme non compliquée se traite en ambulatoire, avec des mesures générales et l’éducation du patient.', 9, 58) +
 P('Moyens non médicamenteux : hygiène du sommeil, activité physique adaptée, psychothérapie (thérapie cognitivo-comportementale) si dépression ou insomnie. '
   'Dans l’encéphalomyélite myalgique, le pacing reste sous le seuil qui déclenche le malaise post-effort ; l’activité physique graduée est déconseillée par le NICE.', 33, 44) +
 FICHE([
  ['Fer IV : carboxymaltose ferrique (Ferinject®)', 'Livre le fer aux macrophages', 'Fer libéré en quelques jours', 'Besoin total 500–2000 mg selon hémoglobine et poids ; par perfusion ≤ 20 mg/kg et ≤ 1000 mg, max 1000 mg par semaine ; surveillance 30 min', 'Hypophosphatémie, réaction de perfusion', 'Infection aiguë, 1er trimestre de grossesse', 'Aucune alimentaire'],
  ['Fer oral : sulfate ferreux (Tardyferon®)', 'Fer absorbé par le duodénum', 'Absorption 10–20 %, freinée par l’hepcidine ≈ 24 h', '60–100 mg de fer élément un jour sur deux (ou 80–100 mg par jour)', 'Nausées, constipation', 'Hémochromatose', 'Calcium, inhibiteurs de la pompe à protons, lévothyroxine : espacer'],
  ['Hormone thyroïdienne : lévothyroxine (Euthyrox®)', 'Remplace la thyroxine (T4)', 'Demi-vie ≈ 7 jours', '1,6 µg/kg/j à jeun, poids idéal si obésité ; âgé ou coronarien : 12,5–25 µg/j, paliers toutes les 4–6 semaines', 'Palpitations, fibrillation atriale si surdosage', 'Insuffisance surrénale non traitée', 'Fer, calcium : espacer de 4 h'],
  ['Antidépresseur de classe ISRS (inhibiteur sélectif de la recapture de la sérotonine) : sertraline (Zoloft®)', 'Bloque la recapture de la sérotonine', 'Demi-vie ≈ 1 jour', '50 mg/j ; paliers de 50 mg espacés d’au moins 1 semaine ; max 200 mg/j', 'Nausées, hyponatrémie', 'Inhibiteurs de la monoamine oxydase', 'Anticoagulants, tramadol'],
 ], 9, 75, 11, 20, 44) +
 P('Aucun stimulant n’est validé contre la fatigue sans cause ; le méthylphénidate n’a pas fait mieux qu’un placebo dans la fatigue du cancer.', 68) +
 F('Situations particulières',
   TAB(['Situation', 'Particularité'], [
    ['Grossesse et allaitement', 'Normes propres ; fer IV seulement dès le 2e trimestre'],
    ['Personne âgée', 'Plus de causes somatiques et médicamenteuses ; lévothyroxine à faible dose'],
    ['Enfant et adolescent', 'Mononucléose, dépression, harcèlement'],
    ['Insuffisance hépatique', 'Prudence avec les sédatifs et les antidépresseurs'],
    ['Insuffisance rénale (DFGe bas)', 'Anémie rénale, doses adaptées'],
   ]), 9, 44) +
 SOCIAL('Un arrêt de travail se discute selon la cause et la durée ; dans l’épuisement, il est limité et associé à un plan de reprise.',
        'La somnolence diurne interdit la conduite jusqu’au traitement (LCR art. 31, recommandation suisse).') +
 H4('11.C Surveillance et critères de sortie') +
 TAB(['Quand', 'Quoi'], [
  ['Après 4–6 semaines', 'Réévaluer la fatigue et le résultat du traitement'],
  ['Après 4 semaines de fer', 'Hémoglobine : hausse d’environ 20 g/L attendue'],
  ['6–8 semaines après un changement de lévothyroxine', 'TSH'],
  ['Arrêt du traitement', 'Fer arrêté quand la ferritine atteint 50–100 µg/L'],
  ['Critères de sortie (après hospitalisation)', 'Hémodynamique stable, cause identifiée, suivi fixé'],
 ]) + P('L’original proposait des réticulocytes à J7 : leur hausse vers 7–10 jours est un repère, à vérifier.', 9) +
 H4('11.D Pronostic, guérison et recherche 2026') +
 P('Le pronostic est excellent quand la cause est simple, comme une carence ou une hypothyroïdie. '
   'Dans l’encéphalomyélite myalgique, la guérison est rare chez l’adulte. '
   'La recherche de 2026 étudie l’inflammation du cerveau et le métabolisme mitochondrial, sans traitement prouvé.', 9, 33, 34))

# ---------- 12
ADD(12, 'Prévention',
 P('La prévention primaire passe par le sommeil, l’activité physique et la prévention du stress au travail. '
   'La prévention secondaire repère tôt une dépression ou un épuisement professionnel. '
   'La prévention tertiaire évite le déconditionnement et la perte d’emploi.', 7, 8, 44) +
 F('Prévention primaire, secondaire et tertiaire',
   TAB(['Niveau', 'Mesure', 'Source'], [
    ['Primaire', 'Hygiène du sommeil, activité physique, gestion de la santé en entreprise (Promotion Santé Suisse)', 'Job Stress Index' + S(8)],
    ['Secondaire', 'PHQ-9 en cas de fatigue ; dépistage du cancer du côlon de 50 à 69 ans (OFSP)', 'Kroenke, OPAS' + S(43, 42)],
    ['Tertiaire', 'Détection précoce par l’assurance-invalidité, reprise progressive', 'LAI' + S(41)],
   ])))

# ---------- 13
ADD(13, 'Points clés',
 P('La fatigue est un symptôme : on cherche toujours une cause, somatique et psychique en même temps. '
   'Une urgence et un drapeau rouge passent avant tout bilan. '
   'Un bilan de base court suffit en première intention : hémogramme, ferritine, TSH, CRP, glycémie, créatinine. '
   'Une ferritine normale n’exclut pas une carence si la CRP est élevée. '
   'Après 6 mois, le malaise post-effort fait évoquer une encéphalomyélite myalgique.', 2, 9, 34))

# ---------- 14
ADD(14, 'Pièges d’examen',
 TAB(['Piège', 'Bonne réponse'], [
  ['Confondre fatigue et somnolence', 'Non : la somnolence oriente vers les apnées ; il faut l’échelle d’Epworth.'],
  ['Donner un somnifère ou une benzodiazépine sans chercher des apnées', 'Erreur : ces médicaments peuvent aggraver les apnées ; il faut d’abord évaluer le sommeil.'],
  ['Exclure une carence en fer parce que la ferritine est à 80 µg/L avec une CRP élevée', 'Non : il faut la saturation de la transferrine.'],
  ['Prescrire une activité physique graduée dans l’encéphalomyélite myalgique', 'Non : le NICE la déconseille ; la réponse est le pacing.'],
  ['Demander un bilan très large d’emblée', 'Non : il produit des faux positifs ; il faut un bilan court puis orienté.'],
  ['Oublier les idées suicidaires', 'Erreur : il faut toujours les demander.'],
 ]) + P('Correction : l’original parlait d’« arrêts respiratoires fatals » sous benzodiazépines ; le risque réel est une aggravation des apnées, surtout avec l’alcool ou les opioïdes. Ces pièges ne sont pas des questions officielles.', 3, 33))

# ---------- Bloc 2 : dix diagnostics
L = lambda f, t: f'<a href="{f}">{t}</a>'
DXL = [
 ('DX.1', 'Anémie ferriprive et carence en fer', 'LOT_004_DX1_Anemie_ferriprive_AUDITÉ.html', PR('≈ 3000 / 100 000 femmes réglées (Europe)', 9), 'Première cause organique chez la femme jeune ; anémie chez 2,8 % des patients fatigués.', (9, 2)),
 ('DX.2', 'Dépression et épuisement professionnel', 'LOT_004_DX2_Depression_burn_out_AUDITÉ.html', PR('≈ 9800 / 100 000 (≥ 15 ans, Suisse 2022)', 6), 'Première cause trouvée : 18,5 % des patients fatigués.', (6, 2)),
 ('DX.3', 'Syndrome d’apnées obstructives du sommeil (SAOS)', 'LOT_004_DX3_SAOS_AUDITÉ.html', PR('23 400 (femmes) à 49 700 (hommes) / 100 000 (40–85 ans, Lausanne)', 14), 'Sommeil non réparateur et somnolence ; risque routier.', (14, 15)),
 ('DX.4', 'Hypothyroïdie primaire', 'LOT_004_DX4_Hypothyroidie_primaire_AUDITÉ.html', PR('≈ 4940 / 100 000, dont ≈ 620 avérée (Europe)', 18), 'Ralentissement, frilosité ; une TSH suffit au dépistage.', (18, 20)),
 ('DX.5', 'Asthénies post-infectieuses (virus d’Epstein-Barr, cytomégalovirus, VIH)', 'LOT_004_DX5_Asthenies_post_infectieuses_AUDITÉ.html', PR('non publiée en population générale', 22), 'Fatigue qui suit une infection ; 12 % à 6 mois dans la cohorte de Dubbo.', (22, 24)),
 ('DX.6', 'Insuffisance cardiaque', 'LOT_004_DX6_Insuffisance_cardiaque_AUDITÉ.html', PR('1000–2000 / 100 000 adultes (Europe)', 25), 'Fatigue d’effort par bas débit ; plus de 10 % après 70 ans.', (25, 26)),
 ('DX.7', 'Maladie rénale chronique', 'LOT_004_DX7_Maladie_renale_chronique_AUDITÉ.html', PR('≈ 10 400 / 100 000 (adultes, Suisse)', 28), 'Anémie rénale et toxines urémiques ; souvent silencieuse.', (28, 27)),
 ('DX.8', 'Néoplasie occulte', 'LOT_004_DX8_Neoplasie_occulte_AUDITÉ.html', PR('≈ 2600 / 100 000 (cancer dans les 10 ans, Suisse, à vérifier)', 29), 'Rare chez le patient fatigué (0,6 %), à chercher devant un drapeau rouge.', (29, 2)),
 ('DX.9', 'Encéphalomyélite myalgique / syndrome de fatigue chronique (EM/SFC), tachycardie orthostatique', 'LOT_004_DX9_EM_SFC_POTS_AUDITÉ.html', PR('≈ 680 / 100 000 (méta-analyse mondiale)', 35), 'Diagnostic positif sur des critères, après 6 mois ; malaise post-effort.', (34, 35)),
 ('DX.10', 'Maladie d’Addison (insuffisance surrénale primaire)', 'LOT_004_DX10_Maladie_d_Addison_AUDITÉ.html', PR('≈ 10–14 / 100 000 (Europe)', 38), 'Rare mais mortelle : mélanodermie, hypotension, hyponatrémie.', (37, 38)),
]
b15 = (P('Les dix diagnostics gardent l’ordre de l’original, du plus fréquent au plus rare chez le patient fatigué. '
         'Les pourcentages de l’original (25 %, 20 %, 15 % …) n’avaient pas de source et sont remplacés par des prévalences de même unité.', 2, 3) +
  TAB(['Rang', 'Diagnostic et prévalence (pour 100 000 habitants)', 'Pourquoi il figure dans la liste'],
      [[d, L(f, n) + pr, j + S(*s)] for d, n, f, pr, j, s in DXL]) +
  P('L’original citait la Société suisse de psychiatrie, la Société suisse d’endocrinologie et de diabétologie (SSED) et le Groupe suisse de recherche clinique sur le cancer (SAKK). '
    'Il citait aussi la Société suisse de médecine interne générale (SSMIG). Ces sources n’ont pas été retrouvées pour ces chiffres ; elles sont retirées.', 2) +
  F('Tableau comparatif : signe, examen, mécanisme, décision',
    TAB(['Diagnostic', 'Signe clé', 'Examen clé', 'Mécanisme', 'Décision immédiate'], [
     ['Anémie ferriprive', 'Pâleur, règles abondantes', 'Hémogramme, ferritine', 'Moins d’oxygène livré', 'Fer, chercher la perte'],
     ['Dépression', 'Anhédonie, idées de mort', 'PHQ-9', 'Humeur et motivation', 'Évaluer le risque suicidaire'],
     ['Apnées du sommeil', 'Ronflement, somnolence', 'Polygraphie', 'Sommeil fragmenté', 'Pas de conduite si somnolent'],
     ['Hypothyroïdie', 'Frilosité, constipation', 'TSH', 'Métabolisme ralenti', 'Lévothyroxine'],
     ['Post-infectieuse', 'Angine, ganglions récents', 'Sérologie EBV, VIH', 'Inflammation persistante', 'Repos relatif, pas de sport de contact'],
     ['Insuffisance cardiaque', 'Dyspnée, œdèmes', 'NT-proBNP', 'Bas débit', 'Échocardiographie'],
     ['Maladie rénale', 'Nycturie, hypertension', 'Créatinine, albuminurie', 'Toxines, anémie', 'Néphroprotection'],
     ['Néoplasie', 'Perte de poids, sueurs', 'Examen ciblé, imagerie', 'Cytokines', 'Bilan rapide'],
     ['EM/SFC', 'Malaise post-effort', 'Aucun : critères cliniques', 'Hypothèses', 'Pacing'],
     ['Addison', 'Mélanodermie, hypotension', 'Cortisol, ACTH', 'Manque de cortisol', 'Hydrocortisone si crise'],
    ]), 2, 3) +
  F('Algorithme discriminant',
    OL(['Instabilité ou idée suicidaire ? DX.2, DX.10 ou anémie sévère : urgence.',
        'Hémoglobine basse, ferritine basse ? DX.1.',
        'TSH élevée ? DX.4. Créatinine élevée ? DX.7. NT-proBNP élevé ? DX.6.',
        'Somnolence et ronflement ? DX.3.',
        'Infection récente ? DX.5.',
        'Drapeau rouge ? DX.8.',
        'Hyponatrémie, hypotension ? DX.10.',
        'Bilan normal, plus de 6 mois, malaise post-effort ? DX.9.']) +
    P('Plusieurs causes peuvent coexister ; une cause trouvée n’exclut pas une dépression associée.', 2)))
PTS.append(f'<section class="point" id="ssp-p15"><h3><strong>Bloc 2 · Liste des dix diagnostics du LOT 4</strong></h3>\n{b15}</section>\n')

CTX = {'_prefixe': 'Devant une fatigue',
 'nfs': 'L’hémoglobine dit s’il y a une anémie ; le VGM oriente vers le fer (< 80 fL) ou la B12 (> 100 fL).',
 'ferritine': 'Une ferritine < 15 µg/L prouve la carence en fer ; 15–30 µg/L signale des réserves réduites.',
 'tsat': 'Une saturation ≤ 20 % confirme la carence quand la CRP fausse la ferritine.',
 'tsh': 'Une TSH élevée fait doser la T4 libre ; une TSH normale exclut une hypothyroïdie primaire.',
 'crp': 'Une CRP élevée oriente vers une inflammation et rend la ferritine faussement normale.',
 'gly': 'Une glycémie élevée fait chercher un diabète, cause de fatigue.',
 'creat': 'La créatinine et le DFGe cherchent une maladie rénale chronique.',
 'iono': 'Une hyponatrémie fait évoquer une maladie d’Addison, une hypothyroïdie ou un médicament.',
 'hep': 'Des transaminases élevées font chercher une hépatite ou une consommation d’alcool.',
 'b12': 'Une B12 basse explique une macrocytose et des troubles neurologiques.',
 'ebv': 'Des anticorps hétérophiles positifs confirment une mononucléose récente.',
 'vih': 'Un test VIH se propose devant un syndrome viral ou une fatigue avec facteur de risque.',
 'psg': 'La polygraphie confirme les apnées si l’index est ≥ 15/h.',
 'quest': 'Une échelle d’Epworth > 10 signale une somnolence diurne excessive.',
 'cort': 'Un cortisol du matin bas fait faire un test au Synacthène.',
 'bnp': 'Un NT-proBNP normal rend l’insuffisance cardiaque peu probable.',
}
if __name__ == '__main__':
    produire(M, PTS, SOURCES, CTX)
