# -*- coding: utf-8 -*-
"""DX.8 — Néoplasie occulte. LOT 4, V5 → V7 AUDITÉ."""
from lot4_commun import *
POINT = mkPOINT('dx8')
M = META('dx8', 'DX.8', 'Néoplasie occulte', 'Néoplasie occulte (fatigue révélatrice d’un cancer)',
         'LOT_004_DX8_Neoplasie_occulte_AUDITÉ.html',
         'Corrections majeures : incidence suisse ≈ 42 750 nouveaux cas par an (OFS) au lieu de 45 000 ; cancer chez 0,6 % des patients fatigués en premier recours (et non 1–3 %) ; « > 15 % » non sourcé retiré ; critères CRAB et SLiM séparés ; le ganglion de Troisier n’est pas pathognomonique ; dexaméthasone 4 mg 2×/j (essai) et méthylphénidate sans bénéfice démontré ; vaccins à ARN messager et anti-GDF-15 restent en recherche.')
CYTO = T('cytokines inflammatoires', 'Les cytokines (IL-6, IL-1, TNF) sont des messagers du système immunitaire ; produites en excès par une tumeur, elles coupent l’appétit, font fondre le muscle et bloquent le fer.')
PTS = []
def ADD(*a): PTS.append(POINT(*a))
ADD(1, 'Définition et sémantique',
 P('La fatigue d’une néoplasie occulte est un épuisement persistant, non soulagé par le repos, qui révèle un cancer encore non diagnostiqué. '
   'Les causes typiques sont le cancer du côlon droit, du rein, du poumon, du pancréas, les lymphomes et le myélome.', 30, 69) +
 F('Terminologie',
   TAB(['Terme', 'Définition exacte', 'À ne pas confondre avec'], [
    ['Fatigue liée au cancer', 'Épuisement persistant, disproportionné à l’effort, non soulagé par le repos', 'Fatigue ordinaire'],
    ['Cachexie', 'Perte de poids > 5 % en 6 mois avec fonte musculaire (consensus de Fearon)', 'Dénutrition simple'],
    ['Symptômes B', 'Fièvre > 38 °C, sueurs nocturnes, perte de poids > 10 % en 6 mois', 'Fièvre infectieuse'],
    ['Syndrome paranéoplasique', 'Manifestation à distance de la tumeur, par hormone ou anticorps', 'Métastase'],
    ['Altération de l’état général', 'Fatigue, perte d’appétit, perte de poids', 'Diagnostic final'],
   ]) + P('La fatigue liée au cancer est définie par l’ESMO.', 30)))
ADD(2, 'Épidémiologie (Suisse, puis Europe)',
 P('En Suisse, environ 42 750 nouveaux cancers sont diagnostiqués chaque année (OFS, période 2013–2017). '
   'Chez un patient fatigué en premier recours, un cancer n’est trouvé que dans 0,6 % des cas ; l’original indiquait 1–3 %. Les données internationales (études CAPER, Royaume-Uni) montrent que le risque monte nettement avec les signes d’alarme.', 29, 2, 69) +
 F('Chiffres, terrain et histoire naturelle',
   TAB(['Donnée', 'Valeur', 'Portée'], [
    ['Nouveaux cancers par an, Suisse', '≈ 42 750', 'OFS 2021'],
    ['Cancer chez les patients fatigués en premier recours', '0,6 %', 'Revue de Stadje'],
    ['Maladie somatique grave chez les patients fatigués', '4,3 %', 'Revue de Stadje'],
    ['Risque avec perte de poids ou anémie après 50–60 ans', 'Nettement plus élevé', 'Études CAPER (chiffre de l’original non sourcé)'],
   ]) + P('Le risque augmente avec l’âge, le tabac, l’alcool, l’obésité et les antécédents familiaux. '
          'Le pronostic dépend du type et du stade au diagnostic ; c’est pourquoi les signes d’alarme doivent mener vite aux examens.', 29, 69)))
ADD(3, 'Physiopathologie',
 P('La tumeur et les cellules qui l’entourent libèrent des ' + CYTO + '. '
   'L’IL-6 fait produire au foie de l’hepcidine, qui bloque le fer : c’est l’anémie inflammatoire. '
   'Les cytokines dégradent aussi les protéines du muscle et agissent sur l’hypothalamus, qui coupe l’appétit.', 30) +
 F('Chaîne logique : de l’anatomie au traitement',
   TAB(['Étape', 'Ce qu’il faut comprendre'], [
    ['Anatomie', 'Une tumeur cachée (côlon droit, rein, moelle osseuse) grossit sans gêne locale.'],
    ['Physiologie', 'Le muscle, le foie et l’hypothalamus règlent l’énergie, le fer et l’appétit.'],
    ['Physiopathologie', 'Les cytokines dérèglent ces trois cibles ; le saignement occulte ajoute une carence en fer.'],
    ['Clinique', 'D’où la fatigue, la perte d’appétit, la perte de poids et la pâleur.'],
    ['Examens', 'Hémogramme, CRP, LDH, électrophorèse et imagerie orientent ; la biopsie confirme.'],
    ['Traitement', 'Traiter le cancer ; pour la fatigue, l’exercice physique est le premier moyen.'],
   ]), 30) +
 F('Mécanisme, exploration et cible thérapeutique',
   TAB(['Mécanisme', 'Lésion ou cause', 'Exploration', 'Cible thérapeutique'], [
    ['Anémie inflammatoire', 'Hepcidine élevée, fer bloqué', 'Ferritine normale ou haute, saturation basse', 'Traiter la tumeur'],
    ['Saignement occulte', 'Cancer colique droit', 'Ferritine basse, test FIT, coloscopie', 'Chirurgie, fer'],
    ['Fonte musculaire', 'Voie ubiquitine-protéasome', 'Poids, force', 'Exercice, nutrition'],
    ['Anorexie centrale', 'Cytokines, GDF-15 sur le tronc cérébral', 'Appétit', 'Nutrition ; anti-GDF-15 en recherche'],
    ['Hypercalcémie', 'Os ou PTHrP', 'Calcium', 'Hydratation, bisphosphonate'],
   ]) + P('Cette chaîne explique pourquoi la fatigue précède parfois toute plainte locale.', 30)) +
 F('Calcul de la perte de poids', P('Perte de poids (%) = (poids habituel − poids actuel) / poids habituel × 100.', 30) +
   P('Exemple : 80 kg puis 71 kg en 4 mois donnent 9 / 80 × 100 = 11,25 %, soit un symptôme B.', 30)))
ADD(4, 'Raisonnement clinique et diagnostic différentiel',
 P('Devant une fatigue inexpliquée après 50 ans, le médecin cherche d’abord les urgences oncologiques : hypercalcémie et compression de la moelle épinière. '
   'Puis il cherche des signes d’alarme ; sans eux, le rendement d’un bilan de cancer est faible.', 30, 2) +
 DIFF('cancer') + DIFF_FAT() +
 F('Cancers à évoquer selon les indices',
   TAB(['Indice', 'Cancer évoqué', 'Examen discriminant'], [
    ['Anémie ferriprive, homme ou femme ménopausée', 'Côlon droit, estomac', 'Coloscopie et gastroscopie'],
    ['Symptômes B, ganglions', 'Lymphome', 'Biopsie-exérèse d’un ganglion'],
    ['Douleurs osseuses, anémie, insuffisance rénale', 'Myélome', 'Électrophorèse, chaînes légères'],
    ['Hématurie sans douleur', 'Rein, vessie', 'Scanner, cystoscopie'],
    ['Fumeur, toux, hémoptysie', 'Poumon', 'Scanner thoracique'],
    ['Perte de poids, diabète récent, douleur dorsale', 'Pancréas', 'Scanner abdominal'],
   ]), 69, 31))
ADD(5, 'Anamnèse ciblée et drapeaux rouges',
 P('L’anamnèse cherche les cancers chez les parents du 1er degré, compte le tabac en paquets-années et vérifie les dépistages. '
   'Elle note la perte de poids, son délai et la présence d’un régime.', 30, 69) +
 U('Drapeaux rouges : symptômes B, douleurs osseuses nocturnes, déficit neurologique des jambes (compression de la moelle), confusion avec soif (hypercalcémie), hématurie, changement du transit, saignement. Une compression ou une hypercalcémie relève de l’urgence (hospitalisation immédiate) ; les autres imposent un bilan rapide.', 30) +
 F('Questions ciblées et leur raison',
   TAB(['Question', 'Pourquoi la poser'], [
    ['Avez-vous perdu du poids sans le vouloir ? Combien, en combien de temps ?', 'Symptôme B, cachexie.'],
    ['Avez-vous des sueurs la nuit ou de la fièvre ?', 'Lymphome.'],
    ['Avez-vous mal aux os la nuit ?', 'Métastases, myélome.'],
    ['Votre transit a-t-il changé ? Du sang dans les selles ?', 'Cancer colorectal.'],
    ['Avez-vous des démangeaisons sans éruption ?', 'Lymphome de Hodgkin.'],
    ['Quand avez-vous fait vos dépistages ?', 'Côlon, sein, col.'],
   ]), 30, 42))
ADD(6, 'Examen clinique',
 P('L’examen pèse le patient et palpe toutes les aires ganglionnaires, l’abdomen, les seins et la thyroïde. '
   'Il percute la colonne et fait un toucher rectal si les symptômes orientent.', 30) +
 P('Valeurs normales : ganglions < 1 cm, mous et mobiles. Un ganglion sus-claviculaire gauche (Troisier) évoque un cancer digestif ; il n’est pas pathognomonique, contrairement à l’original.', 30) +
 F('Signes, technique et valeur',
   TAB(['Signe', 'Technique', 'Ce qu’il signifie'], [
    ['Ganglion dur, fixé, > 1,5 cm', 'Palpation de toutes les aires', 'Suspect de cancer ou lymphome'],
    ['Ganglion de Troisier', 'Palpation sus-claviculaire gauche', 'Cancer abdominal ou pelvien probable'],
    ['Hépatomégalie nodulaire', 'Palpation, percussion', 'Métastases'],
    ['Splénomégalie', 'Palpation en décubitus latéral droit', 'Hémopathie'],
    ['Douleur à la percussion vertébrale', 'Percussion épineuse', 'Métastase osseuse'],
    ['Masse au toucher rectal', 'Toucher rectal', 'Cancer rectal ou prostatique'],
   ]), 30))
ADD(7, 'Syndromes et signes cliniques',
 F('Signes fonctionnels (symptômes rapportés)', UL(['Fatigue non soulagée par le repos', 'Perte d’appétit', 'Sueurs nocturnes', 'Douleurs osseuses', 'Démangeaisons']), 30) +
 F('Signes physiques (constatés à l’examen)', UL(['Perte de poids mesurée', 'Fonte des muscles des tempes et des cuisses', 'Ganglions', 'Pâleur', 'Masse abdominale']), 30) +
 P('L’altération de l’état général réunit fatigue, perte d’appétit et perte de poids : elle traduit l’action des cytokines. '
   'Le syndrome inflammatoire et anémique réunit pâleur, fièvre, anémie et plaquettes élevées : il traduit l’inflammation chronique.', 30) +
 F('Altération de l’état général et cachexie', TAB(['Signe', 'Mécanisme', 'Valeur'], [
    ['Perte de poids > 5 % en 6 mois', 'Fonte musculaire et graisseuse', 'Cachexie'],
    ['Fonte temporale', 'Perte musculaire', 'Gravité'],
    ['Perte d’appétit', 'Action hypothalamique', 'Fréquente'],
   ]), 30) +
 F('Syndrome inflammatoire et anémique', TAB(['Signe', 'Mécanisme', 'Valeur'], [
    ['Anémie, ferritine normale ou haute', 'Fer bloqué par l’hepcidine', 'Inflammation'],
    ['Saturation de la transferrine < 20 %', 'Fer peu disponible', 'Carence fonctionnelle'],
    ['Plaquettes élevées', 'IL-6', 'Peu spécifique'],
   ]), 30))
ADD(8, 'Critères diagnostiques',
 P('Le diagnostic de cancer exige une preuve histologique sur biopsie. Une imagerie suspecte ne suffit pas.', 30, 31) +
 F('Critères du myélome (International Myeloma Working Group, consensus 2014)',
   TAB(['Critère', 'Seuil'], [
    ['Plasmocytes clonaux médullaires', '≥ 10 % (ou plasmocytome prouvé), plus ≥ 1 événement ci-dessous'],
    ['C : calcium', '> 2,75 mmol/L ou > 0,25 mmol/L au-dessus de la normale'],
    ['R : rein', 'Créatinine > 177 µmol/L ou clairance < 40 mL/min'],
    ['A : anémie', 'Hb < 100 g/L ou > 20 g/L sous la normale'],
    ['B : os', '≥ 1 lésion lytique au scanner ou à la TEP-scanner'],
    ['SLiM (marqueurs sans symptôme)', 'Plasmocytes ≥ 60 % ; rapport des chaînes légères ≥ 100 ; > 1 lésion focale à l’IRM'],
   ]) + P('L’original mélangeait les critères CRAB et SLiM ; ils sont séparés ici.', 31)) +
 F('Score de performance ECOG', TAB(['Grade', 'Description'], [['0', 'Activité normale'], ['1', 'Gêne aux efforts soutenus, travail léger possible'], ['2', 'Autonome, debout > 50 % de la journée, pas de travail'], ['3', 'Au lit ou au fauteuil > 50 % de la journée'], ['4', 'Alité en permanence, dépendant'], ['5', 'Décès']]), 32))
ADD(9, 'Examens complémentaires',
 H4('9.a Examen de référence') +
 P('L’examen de référence est l’analyse histologique d’une biopsie. Pour un lymphome, on préfère la biopsie-exérèse d’un ganglion entier ; la cytoponction seule ne suffit pas. La biopsie a une sensibilité et une spécificité élevées ; la cytoponction a une sensibilité insuffisante pour classer un lymphome.', 30) +
 H4('9.b Examens de première et de deuxième intention') +
 P('En première intention, on fait une biologie large et une imagerie simple. En deuxième intention, on fait l’endoscopie ou le scanner selon les indices.', 30, 69) +
 TAB(['Intention', 'Examen', 'Pourquoi'], [
  ['1re', 'Hémogramme, frottis', 'Anémie, cytopénie, cellules anormales'],
  ['1re', 'CRP, vitesse de sédimentation', 'Inflammation'],
  ['1re', 'LDH', 'Renouvellement cellulaire (lymphome)'],
  ['1re', 'Calcium, créatinine, tests hépatiques', 'Hypercalcémie, rein, foie'],
  ['1re', 'Électrophorèse des protéines, chaînes légères libres', 'Myélome'],
  ['1re', 'Radiographie thoracique, échographie abdominale', 'Masse, ganglions profonds'],
  ['2e', 'Coloscopie et gastroscopie', 'Anémie ferriprive'],
  ['2e', 'Scanner thoraco-abdomino-pelvien', 'Recherche sans signe focal'],
  ['2e', 'TEP-scanner au FDG', 'Bilan d’extension, lymphome'],
 ]) +
 H4('9.c Prescription et formules') +
 P('Indication : fatigue avec signe d’alarme ou anomalie biologique. Moment : sans délai si un drapeau rouge est présent. '
   'Préparation : préparation colique pour la coloscopie ; à jeun et glycémie contrôlée pour la TEP-scanner.', 30) +
 TAB(['Grandeur', 'Formule', 'Repère'], [['Perte de poids', '(habituel − actuel) / habituel × 100', '> 10 % en 6 mois : symptôme B'], ['Rapport des chaînes légères', 'Kappa / lambda', '0,26–1,65 normal']]) +
 H4('9.d Interprétation : positif, négatif, limite, discordant') +
 TAB(['Situation', 'Interprétation', 'Conduite'], [
  ['Positif : masse à l’imagerie', 'Cancer probable', 'Biopsie'],
  ['Négatif : biologie et examen normaux, pas d’alarme', 'Cancer très improbable', 'Surveillance, autre cause'],
  ['Limite : pic monoclonal < 30 g/L sans atteinte', 'Gammapathie de signification indéterminée possible', 'Avis hématologique, suivi'],
  ['Discordant : marqueur tumoral élevé, imagerie normale', 'Faux positif fréquent', 'Ne pas multiplier les examens'],
 ]) +
 H4('9.e Alternatives') +
 P('Grossesse : échographie et IRM sans gadolinium plutôt que scanner. Enfant : avis oncopédiatrique. '
   'DFGe < 30 : scanner sans iode ou IRM ; la TEP-scanner reste possible.', 30))
ADD(10, 'Arbre décisionnel',
 P('Si un signe d’alarme est présent, alors le bilan se fait sans délai. Sinon, une biologie de base suffit d’abord.', 30, 2) +
 F('Arbre décisionnel : fatigue avec suspicion de cancer',
   OL(['Compression de la moelle, hypercalcémie : urgence.',
       'Signes d’alarme ? Bilan rapide.',
       'Biologie : hémogramme, CRP, LDH, calcium, créatinine, électrophorèse.',
       'Anémie ferriprive : coloscopie et gastroscopie.',
       'Signe focal : imagerie ciblée.',
       'Pas de signe focal mais biologie anormale : scanner thoraco-abdomino-pelvien.',
       'Lésion : biopsie, puis colloque multidisciplinaire.']), 30, 69))
ADD(11, 'Prise en charge',
 H4('11.A Buts : d’abord l’urgence (compression médullaire, hypercalcémie), car elle peut laisser des séquelles en quelques heures') +
 P('Le traitement vise la guérison ou le contrôle du cancer, la correction des troubles métaboliques et le soulagement de la fatigue.', 30) +
 TAB(['But', 'Cible chiffrée'], [['Fatigue', 'Baisse sur l’échelle 0–10'], ['Poids', 'Stabilisation'], ['Calcium', '2,15–2,55 mmol/L']]) +
 H4('11.B Moyens et méthodes : forme compliquée en urgence, puis forme non compliquée en ambulatoire') +
 P('La forme compliquée se traite en urgence : dexaméthasone et IRM dans les heures qui suivent pour une compression ; hydratation et bisphosphonate pour une hypercalcémie. '
   'La forme non compliquée se traite en ambulatoire, avec des mesures générales : colloque multidisciplinaire, chirurgie, radiothérapie ou traitement médical.', 30) +
 P('Pour la fatigue liée au cancer, l’ESMO recommande d’abord l’exercice physique aérobie et de renforcement, avec un soutien nutritionnel et psychologique.', 30) +
 FICHE([
  ['Anti-PD-1 : pembrolizumab (Keytruda®)', 'Lève le frein des lymphocytes T contre la tumeur', 'Intraveineux, demi-vie ≈ 26 j', '200 mg toutes les 3 semaines ou 400 mg toutes les 6 semaines, en perfusion de 30 min', 'Thyroïdite, colite, hépatite, hypophysite', 'Selon l’indication', 'Corticoïdes au long cours'],
  ['Anti-CD20 : rituximab (MabThera®)', 'Détruit les lymphocytes B', 'Intraveineux', 'Selon le protocole du lymphome', 'Réaction à la perfusion, réactivation de l’hépatite B', 'Infection active grave', 'Vaccins vivants'],
  ['Corticoïde : dexaméthasone (Fortecortin®)', 'Anti-inflammatoire', 'Demi-vie biologique 36–54 h', '4 mg 2×/j pendant 14 jours (essai, cancer avancé)', 'Hyperglycémie, myopathie, insomnie', 'Infection non contrôlée', 'Antidiabétiques, AINS'],
  ['Psychostimulant : méthylphénidate (Ritaline®)', 'Augmente la dopamine', 'Demi-vie ≈ 2–3 h', '5–10 mg le matin et à midi (hors indication)', 'Insomnie, tachycardie', 'Arythmie, hypertension non contrôlée', 'IMAO'],
 ], 30, 68) +
 P('Le méthylphénidate n’a pas fait mieux que le placebo dans l’essai de Bruera (2013) ; son usage reste un essai individuel.', 68) +
 F('Situations particulières',
   TAB(['Situation', 'Particularité'], [
    ['Grossesse', 'Cancer du sein ou lymphome possibles ; imagerie sans irradiation ; avis multidisciplinaire'],
    ['Personne âgée', 'Évaluation gériatrique avant le traitement'],
    ['Enfant', 'Leucémies, tumeurs cérébrales ; centre d’oncopédiatrie'],
    ['Insuffisance hépatique', 'Adapter les chimiothérapies'],
    ['Insuffisance rénale (DFGe bas)', 'Penser au myélome ; adapter les doses'],
   ]), 30) +
 SOCIAL('L’arrêt de travail est fréquent pendant le traitement ; la reprise progressive est encouragée.',
        'La conduite dépend des symptômes et des traitements : métastases cérébrales, opioïdes forts ou fatigue sévère l’interdisent.') +
 H4('11.C Surveillance et critères de sortie') +
 TAB(['Quand', 'Quoi'], [
  ['À chaque consultation', 'Fatigue sur l’échelle 0–10, poids, score ECOG'],
  ['Avant chaque cycle', 'Hémogramme (neutropénie)'],
  ['Sous immunothérapie', 'TSH, cortisol, tests hépatiques'],
  ['Selon le protocole', 'Scanner selon les critères RECIST 1.1'],
  ['Critères de sortie d’hospitalisation', 'Calcium normalisé, douleur contrôlée, plan oncologique établi'],
 ]) + P('Toute fièvre sous chimiothérapie impose un hémogramme le jour même.', 30) +
 H4('11.D Pronostic et recherche 2026') +
 P('Le pronostic dépend du type, du stade et de l’état général. Une rémission complète prolongée sur 5 ans équivaut souvent à une guérison.', 30) +
 P('Les vaccins personnalisés à ARN messager et les anticorps anti-GDF-15 contre la cachexie sont en recherche ; ils ne sont pas utilisés en routine, contrairement à l’original.', 30))
ADD(12, 'Prévention',
 P('La prévention repose sur l’arrêt du tabac, la limitation de l’alcool, l’activité physique et les dépistages organisés.', 42) +
 F('Prévention primaire, secondaire et tertiaire',
   TAB(['Niveau', 'Mesure'], [
    ['Primaire', 'Tabac, alcool, poids, vaccination contre le papillomavirus et l’hépatite B'],
    ['Secondaire', 'Côlon de 50 à 69 ans : test FIT tous les 2 ans ou coloscopie tous les 10 ans ; mammographie selon les programmes cantonaux'],
    ['Tertiaire', 'Réadaptation oncologique, suivi des séquelles'],
   ]) + P('En Suisse, l’OPAS rembourse le dépistage du cancer du côlon de 50 à 69 ans.', 42)))
ADD(13, 'Points clés',
 P('Un cancer est rare chez un patient fatigué sans signe d’alarme. '
   'Les signes d’alarme imposent un bilan rapide. '
   'Seule la biopsie confirme le cancer. '
   'Les marqueurs tumoraux ne servent pas au dépistage d’une fatigue, car ils sont peu sensibles et peu spécifiques.', 2, 30))
ADD(14, 'Pièges d’examen',
 TAB(['Piège', 'Ce qu’il faut répondre'], [
  ['Donner des corticoïdes avant la biopsie d’un ganglion suspect', 'Non : ils masquent un lymphome'],
  ['Se contenter d’une cytoponction pour un lymphome', 'Non : biopsie-exérèse'],
  ['Doser CEA, CA 19-9 et CA 125 devant une fatigue', 'Non : faux positifs et faux négatifs'],
  ['Attribuer une anémie ferriprive de l’homme à l’alimentation', 'Non : endoscopies'],
  ['Dire que le ganglion de Troisier est pathognomonique', 'Non : il est évocateur'],
 ]) + P('Ces pièges reprennent l’ESMO et les études CAPER.', 30, 69))
CTX = {'_prefixe': 'Devant une suspicion de cancer occulte',
 'nfs': 'Une anémie, une cytopénie ou des cellules anormales orientent le bilan.',
 'frottis': 'Des blastes ou des rouleaux de globules rouges orientent vers une hémopathie.',
 'crp': 'Une CRP élevée sans infection doit faire chercher une tumeur ou une inflammation.',
 'vs': 'Une vitesse très élevée évoque un myélome ou une inflammation.',
 'ldh': 'Une LDH élevée évoque un renouvellement cellulaire rapide (lymphome).',
 'epp': 'Un pic monoclonal évoque un myélome ou une gammapathie.',
 'flc': 'Un rapport ≥ 100 est un critère SLiM du myélome.',
 'marq': 'Ils servent au suivi d’un cancer connu, pas au dépistage.',
 'fit': 'Un test positif impose une coloscopie.',
 'endo': 'Elle cherche un cancer digestif devant une anémie ferriprive.',
 'tdm': 'Il cherche une tumeur sans signe focal.',
 'tep': 'Elle sert au bilan d’extension et aux lymphomes.',
 'biopsie': 'Elle seule confirme le cancer.',
 'radio': 'Une masse ou des ganglions médiastinaux orientent le bilan.',
 'echoabdo': 'Elle cherche une masse, des ganglions profonds ou des métastases.',
 'iono': 'Une hypercalcémie est une urgence.'}
if __name__ == '__main__':
    produire(M, PTS, SOURCES, CTX)
