# -*- coding: utf-8 -*-
"""DX.5 — Asthénies infectieuses et post-virales (mononucléose à EBV, CMV, primo-infection VIH). LOT 4, V5 → V7 AUDITÉ."""
from lot4_commun import *
POINT = mkPOINT('dx5')
M = META('dx5', 'DX.5', 'Asthénies post-infectieuses', 'Asthénies infectieuses et post-virales (mononucléose infectieuse, cytomégalovirus, primo-infection par le virus de l’immunodéficience humaine)',
         'LOT_004_DX5_Asthenies_post_infectieuses_AUDITÉ.html',
         'Corrections majeures : l’éruption sous amoxicilline touche ≈ 30 % des enfants avec mononucléose (et non 90 %) ; les critères de Hoagland ne sont pas « de la Société suisse d’infectiologie » ; les vaccins contre le virus d’Epstein-Barr sont en phase précoce (et non III) ; la fatigue à 6 mois (12 %) vient de la cohorte de Dubbo, pas de l’OFSP.')
SB = T('comportement de maladie', 'Le comportement de maladie (sickness behaviour) est l’ensemble fatigue, somnolence, perte d’appétit et retrait social que provoquent les cytokines de l’inflammation en agissant sur le cerveau.')
LYA = T('lymphocytes atypiques', 'Les lymphocytes atypiques (hyperbasophiles) sont de grands lymphocytes T activés, au cytoplasme bleu foncé, qui réagissent contre les lymphocytes B infectés.')
PTS = []
def ADD(*a): PTS.append(POINT(*a))
ADD(1, 'Définition et sémantique',
 P('L’asthénie post-infectieuse est une fatigue physique et mentale qui dure des semaines à des mois pendant ou après une infection. '
   'Elle suit typiquement une mononucléose infectieuse à virus d’Epstein-Barr (EBV), une infection à cytomégalovirus (CMV) ou une primo-infection par le VIH. '
   'Au-delà de 6 mois avec malaise post-effort, il faut évoquer une EM/SFC.', 24, 22) +
 F('Terminologie',
   TAB(['Terme', 'Définition exacte', 'À ne pas confondre avec'], [
    ['Mononucléose infectieuse', 'Primo-infection symptomatique à EBV : fièvre, angine, adénopathies, lymphocytes atypiques', 'Angine à streptocoque'],
    ['Syndrome mononucléosique', 'Lymphocytose avec lymphocytes atypiques, quelle qu’en soit la cause (EBV, CMV, VIH, toxoplasme)', 'Mononucléose à EBV seule'],
    ['Fatigue post-infectieuse', 'Fatigue persistante après l’infection, sans autre cause', 'Infection encore active'],
    ['EM/SFC post-infectieuse', 'Fatigue ≥ 6 mois avec malaise post-effort (critères IOM 2015)', 'Convalescence normale'],
    ['Primo-infection VIH', 'Syndrome viral 2–6 semaines après la contamination', 'Mononucléose à EBV'],
   ]) + P('Le terme « asthénie post-virale » décrit un symptôme ; il ne dispense pas de chercher une infection en cours.', 22, 34)))
ADD(2, 'Épidémiologie (Suisse, puis Europe)',
 P('Plus de 90 % des adultes dans le monde sont porteurs de l’EBV. '
   'En Suisse, aucune donnée nationale publiée ne chiffre la fatigue post-infectieuse. '
   'Dans la cohorte internationale de Dubbo (253 patients), 12 % gardaient une fatigue invalidante à 6 mois après EBV, fièvre Q ou virus de Ross River.', 24, 22) +
 F('Chiffres, terrain et histoire naturelle',
   TAB(['Donnée', 'Valeur', 'Portée'], [
    ['Adultes séropositifs pour l’EBV', '> 90 %', 'Données internationales'],
    ['Fatigue invalidante à 6 mois après infection', '12 %', 'Cohorte de Dubbo (Australie)'],
    ['Syndrome de fatigue chronique à 6 mois', '11 %', 'Même cohorte'],
    ['Éruption sous amoxicilline, enfants avec mononucléose', '29,5 %', 'Chovel-Sella (2013) ; l’original disait 90 %'],
    ['Données suisses de fatigue post-infectieuse', 'Non publiées', 'Les chiffres « OFSP / RMS » de l’original n’ont pas été retrouvés'],
   ]) + P('Le terrain typique de la mononucléose est l’adolescent et l’adulte jeune de 15 à 25 ans. '
          'Le pronostic est bon : la plupart guérissent en 1 à 3 mois ; la gravité de l’infection initiale prédit la fatigue prolongée ; la mortalité est très faible.', 24, 22)))
ADD(3, 'Physiopathologie',
 P('L’EBV infecte la gorge, puis les lymphocytes B. '
   'Des ' + LYA + ' se multiplient pour les détruire et libèrent des cytokines (interféron-γ, TNF-α, interleukines). '
   'Ces cytokines agissent sur le cerveau et provoquent le ' + SB + ', ce qui explique la fatigue.', 24, 22) +
 F('Chaîne logique : de l’anatomie au traitement',
   TAB(['Étape', 'Ce qu’il faut comprendre'], [
    ['Anatomie', 'L’anneau lymphatique de la gorge (amygdales), les ganglions, la rate et le foie hébergent les lymphocytes.'],
    ['Physiologie', 'Les lymphocytes T contrôlent les cellules infectées ; les cytokines coordonnent la réponse.'],
    ['Physiopathologie', 'L’EBV entre dans les lymphocytes B par le récepteur CD21 ; la réaction T massive fait gonfler les organes lymphoïdes.'],
    ['Clinique', 'D’où l’angine, les adénopathies, la grosse rate, l’hépatite et la fatigue.'],
    ['Examens', 'L’hémogramme montre les lymphocytes atypiques ; la sérologie date l’infection.'],
    ['Traitement', 'Symptomatique : le système immunitaire contrôle le virus, qui reste latent à vie.'],
   ]), 24) +
 F('Mécanisme, exploration et cible thérapeutique',
   TAB(['Mécanisme', 'Lésion', 'Exploration', 'Cible thérapeutique'], [
    ['Infiltration lymphoïde de la rate', 'Splénomégalie, risque de rupture', 'Palpation douce, échographie', 'Pas de sport de contact'],
    ['Hypertrophie des amygdales', 'Obstruction des voies aériennes', 'Examen ORL', 'Corticoïdes, hospitalisation'],
    ['Hépatite réactionnelle', 'Transaminases élevées', 'Bilan hépatique', 'Paracétamol à dose réduite'],
    ['Cytokines', 'Fatigue', 'Clinique', 'Reprise progressive des activités'],
   ]) + P('Le mécanisme de la fatigue prolongée n’est pas élucidé ; il ne s’explique pas par une infection persistante.', 22)) +
 F('Critères de Hoagland : calcul', P('Lymphocytes absolus (G/L) = leucocytes (G/L) × % de lymphocytes / 100. Critère : lymphocytes ≥ 50 % et lymphocytes atypiques ≥ 10 %.', 24) +
   P('Exemple : leucocytes 14,0 G/L, lymphocytes 60 % (8,4 G/L), atypiques 18 % : critère hématologique rempli.', 24)))
ADD(4, 'Raisonnement clinique et diagnostic différentiel',
 P('Devant une fatigue fébrile avec angine et adénopathies, le médecin cherche d’abord une urgence : obstruction des voies aériennes ou rupture de rate. '
   'Puis il distingue EBV, CMV, primo-infection VIH et toxoplasmose ; le VIH ne doit jamais être oublié. '
   'Si la fatigue persiste après guérison, il exclut une dépression ou une EM/SFC.', 24, 22) +
 DIFF('mni') + DIFF_FAT() +
 F('Syndromes mononucléosiques : diagnostic différentiel',
   TAB(['Cause', 'Élément distinctif', 'Examen discriminant'], [
    ['EBV', 'Angine marquée, adolescent, splénomégalie', 'Anticorps hétérophiles, VCA IgM'],
    ['CMV', 'Fièvre prolongée, angine modeste', 'IgM anti-CMV, avidité des IgG'],
    ['Primo-infection VIH', 'Éruption, ulcères buccaux, exposition à risque', 'Test combiné antigène p24 et anticorps, charge virale'],
    ['Toxoplasmose', 'Adénopathies, contact avec chat ou viande crue', 'Sérologie toxoplasmose'],
    ['Angine à streptocoque', 'Pas de lymphocytes atypiques', 'Test rapide streptocoque'],
    ['Hépatite virale aiguë', 'Ictère, transaminases > 10 fois la norme', 'Sérologies VHA, VHB, VHC'],
   ]) + P('Aucune fréquence commune n’est publiée chez le patient fatigué pour ces causes.', 24)))
ADD(5, 'Anamnèse ciblée et drapeaux rouges',
 P('L’anamnèse précise le début, la fièvre, la douleur à la déglutition, les contacts, les rapports sexuels non protégés des 6 dernières semaines et les médicaments. '
   'Elle mesure le retentissement : école, travail, sport.', 24) +
 U('Drapeaux rouges : douleur brutale de l’hypochondre gauche irradiant à l’épaule (rupture de rate), stridor ou impossibilité d’avaler la salive (obstruction), ictère, saignements, troubles neurologiques. Ils imposent une hospitalisation urgente ; appeler le 144 si choc ou détresse respiratoire.', 24) +
 F('Questions ciblées et leur raison',
   TAB(['Question', 'Pourquoi la poser'], [
    ['Avez-vous mal en avalant ? Arrivez-vous à boire ?', 'Évalue l’obstruction et la déshydratation.'],
    ['Avez-vous eu des rapports non protégés récemment ?', 'Une primo-infection VIH doit être cherchée.'],
    ['Avez-vous pris un antibiotique ? Une éruption est-elle apparue ?', 'L’amoxicilline donne souvent une éruption dans la mononucléose.'],
    ['Faites-vous un sport de contact ?', 'Risque de rupture de rate.'],
    ['Avez-vous un chat ? Mangez-vous de la viande peu cuite ?', 'Toxoplasmose.'],
    ['Votre fatigue s’aggrave-t-elle après un effort, le lendemain ?', 'Un malaise post-effort évoque une EM/SFC débutante.'],
   ]), 24, 23, 34))
ADD(6, 'Examen clinique',
 P('L’examen inspecte la gorge et les paupières, palpe les ganglions et, très doucement, la rate et le foie. Il cherche une éruption et un ictère.', 24) +
 P('Valeurs normales : ganglions < 1 cm, rate non palpable. La splénomégalie est palpable chez environ la moitié des patients ; la palpation a une sensibilité modeste, d’où l’échographie si un sport est prévu.', 24) +
 F('Signes, technique et valeur',
   TAB(['Signe', 'Technique', 'Ce qu’il signifie'], [
    ['Angine érythémato-pultacée ou à fausses membranes', 'Inspection avec abaisse-langue', 'EBV probable chez le jeune'],
    ['Pétéchies du voile du palais', 'Inspection', 'Évocateur, non spécifique'],
    ['Œdème des paupières supérieures (signe de Hoagland)', 'Inspection', 'Évocateur d’EBV'],
    ['Adénopathies cervicales postérieures', 'Palpation bilatérale', 'Plus évocatrices d’EBV que les antérieures'],
    ['Splénomégalie', 'Palpation douce, patient en décubitus latéral droit', 'Risque de rupture'],
    ['Éruption maculo-papuleuse', 'Inspection de la peau', 'Souvent après amoxicilline'],
   ]), 24, 23))
ADD(7, 'Syndromes et signes cliniques',
 F('Signes fonctionnels (symptômes rapportés)', UL(['Fatigue intense', 'Mal de gorge', 'Fièvre', 'Douleurs musculaires', 'Perte d’appétit']), 24) +
 F('Signes physiques (constatés à l’examen)', UL(['Angine', 'Adénopathies cervicales', 'Splénomégalie', 'Hépatomégalie, ictère', 'Œdème palpébral']), 24) +
 P('Le syndrome mononucléosique clinique réunit fièvre, angine, adénopathies et fatigue : il traduit la réaction lymphocytaire. '
   'Le syndrome d’hépatite réactionnelle réunit nausées, gêne de l’hypochondre droit et transaminases élevées : il traduit l’infiltration du foie.', 24) +
 F('Syndrome mononucléosique', TAB(['Signe', 'Mécanisme', 'Valeur'], [
    ['Angine', 'Infection de l’épithélium et des amygdales', 'Très fréquente chez l’adolescent'],
    ['Adénopathies', 'Prolifération lymphocytaire', 'Postérieures, symétriques'],
    ['Splénomégalie', 'Infiltration de la rate', 'Risque de rupture les 3–4 premières semaines'],
   ]), 24) +
 F('Syndrome d’hépatite réactionnelle', TAB(['Signe', 'Mécanisme', 'Valeur'], [
    ['Transaminases 2–5 fois la norme', 'Infiltration lymphocytaire du foie', 'Fréquente'],
    ['Ictère', 'Cholestase ou hémolyse', 'Rare'],
    ['Nausées', 'Hépatite', 'Peu spécifique'],
   ]), 24))
ADD(8, 'Critères diagnostiques',
 P('Le diagnostic combine clinique, hémogramme et sérologie. L’hémogramme seul ne suffit pas : CMV, VIH et toxoplasmose donnent le même tableau.', 24) +
 F('Critères de Hoagland (1975) et confirmation biologique',
   TAB(['Critère', 'Seuil'], [
    ['Clinique', 'Fièvre, angine, adénopathies'],
    ['Lymphocytes', '≥ 50 % des leucocytes'],
    ['Lymphocytes atypiques', '≥ 10 % des leucocytes'],
    ['Sérologie', 'Anticorps hétérophiles positifs ou VCA IgM positifs avec EBNA négatifs'],
   ]) + P('Ces critères sont décrits par Hoagland ; l’original les attribuait à tort à une société suisse. Aucune recommandation nationale suisse n’a été retrouvée.', 24)))
ADD(9, 'Examens complémentaires',
 H4('9.a Examen de référence') +
 P('La référence est la sérologie spécifique de l’EBV (VCA IgM, VCA IgG, EBNA). '
   'Le test des anticorps hétérophiles a une spécificité élevée, mais une sensibilité plus faible la première semaine et chez l’enfant de moins de 4 ans ; environ 25 % de faux négatifs au début.', 24) +
 H4('9.b Examens de première et de deuxième intention') +
 P('En première intention, on fait hémogramme avec frottis, transaminases, test rapide et test VIH. En deuxième intention, on fait la sérologie spécifique de l’EBV, du CMV et de la toxoplasmose si le test rapide est négatif.', 24) +
 TAB(['Intention', 'Examen', 'Pourquoi'], [
  ['1re', 'Hémogramme et frottis sanguin', 'Lymphocytes atypiques, plaquettes'],
  ['1re', 'Bilan hépatique', 'Hépatite réactionnelle'],
  ['1re', 'Test des anticorps hétérophiles', 'Diagnostic rapide'],
  ['1re', 'Test VIH de 4e génération', 'Ne jamais manquer une primo-infection'],
  ['2e', 'Sérologies EBV, CMV, toxoplasmose', 'Test rapide négatif ou grossesse'],
  ['2e', 'Échographie abdominale', 'Taille de la rate avant reprise du sport'],
  ['2e', 'PCR EBV ou CMV', 'Patient immunodéprimé'],
 ]) +
 H4('9.c Prescription et formules') +
 P('Indication : fièvre, angine, adénopathies et fatigue chez un jeune, ou fatigue fébrile inexpliquée. Moment : dès les symptômes ; répéter le test rapide après 1 semaine s’il est négatif. '
   'Préparation : aucune ; informer le patient du test VIH.', 24) +
 TAB(['Grandeur', 'Formule', 'Repère'], [['Lymphocytes absolus', 'Leucocytes × % lymphocytes / 100', '> 4 G/L évocateur'], ['Lymphocytes atypiques', '% du total', '≥ 10 %']]) +
 H4('9.d Interprétation : positif, négatif, limite, discordant') +
 TAB(['Situation', 'Interprétation', 'Conduite'], [
  ['Positif : VCA IgM +, EBNA −', 'Primo-infection EBV', 'Traitement symptomatique, pas de sport de contact'],
  ['Négatif : VCA et EBNA négatifs', 'Pas d’EBV', 'CMV, VIH, toxoplasmose'],
  ['Limite : VCA IgM faiblement +', 'Réaction croisée possible', 'Contrôle à 2 semaines'],
  ['Discordant : EBNA + dès le 1er prélèvement', 'Infection ancienne', 'Chercher une autre cause, notamment le VIH'],
 ]) +
 H4('9.e Alternatives') +
 P('Grossesse : sérologies CMV et toxoplasmose avec avidité des IgG, car le risque fœtal change la conduite. Enfant < 4 ans : sérologie spécifique plutôt que test rapide. '
   'DFGe bas : aucun contraste n’est nécessaire. Ni iode ni IRM ne sont utiles ; l’échographie reste possible avec un pacemaker.', 24))
ADD(10, 'Arbre décisionnel',
 P('Si le test rapide est positif chez un adolescent typique, alors le diagnostic est posé. S’il est négatif, alors on demande la sérologie et le test VIH.', 24) +
 F('Arbre décisionnel : fatigue fébrile avec angine et adénopathies',
   OL(['Stridor, salive non avalée, douleur splénique : urgence.',
       'Hémogramme, frottis, transaminases, test rapide, test VIH.',
       'Test rapide positif : mononucléose à EBV.',
       'Test rapide négatif : VCA IgM, EBNA, IgM anti-CMV, toxoplasmose.',
       'EBNA positif d’emblée : infection ancienne → CMV, VIH (charge virale si suspicion), toxoplasmose.',
       'Fatigue > 6 mois avec malaise post-effort : évaluer une EM/SFC.']), 24, 34))
ADD(11, 'Prise en charge',
 H4('11.A Buts : d’abord l’urgence (obstruction, rupture de rate), car elles peuvent tuer en quelques heures') +
 P('Le traitement soulage, prévient la rupture de rate et accompagne une reprise progressive sans déconditionnement.', 24) +
 TAB(['But', 'Cible chiffrée'], [['Fièvre', 'Disparition en 10–14 jours en général'], ['Sport de contact', 'Arrêt ≥ 3–4 semaines'], ['Reprise', 'Activités normales en 1–3 mois']]) +
 H4('11.B Moyens et méthodes : forme compliquée en urgence, puis forme non compliquée en ambulatoire') +
 P('La forme compliquée (obstruction des voies aériennes, rupture de rate, anémie hémolytique ou thrombopénie sévère) se traite en urgence à l’hôpital, dans les premières heures. '
   'La forme non compliquée se traite en ambulatoire : mesures générales (boire, repos selon la fatigue) et éducation du patient sur le sport et la contagion.', 24) +
 P('Moyens non médicamenteux : repos adapté, reprise progressive selon la tolérance, pas de port de charges lourdes ni de sport de contact pendant au moins 3–4 semaines.', 24) +
 FICHE([
  ['Antalgique-antipyrétique : paracétamol (Dafalgan®)', 'Inhibe la synthèse centrale des prostaglandines', 'Demi-vie ≈ 2 h ; métabolisme hépatique', '500–1000 mg toutes les 6 h ; dose réduite (≈ 2 g/j) si hépatite', 'Toxicité hépatique en surdosage', 'Insuffisance hépatique sévère', 'Alcool'],
  ['AINS : ibuprofène (Irfen®)', 'Inhibe les cyclo-oxygénases', 'Demi-vie ≈ 2 h', '400 mg 3 fois par jour, quelques jours', 'Brûlures d’estomac, atteinte rénale', 'Ulcère, insuffisance rénale, grossesse au 3e trimestre', 'Anticoagulants'],
  ['Corticoïde : prednisone (Prednisone Streuli®)', 'Anti-inflammatoire puissant', 'Demi-vie ≈ 3 h', 'Cure courte réservée aux complications, dose selon le spécialiste', 'Hyperglycémie, insomnie', 'Forme non compliquée', 'AINS (ulcère)'],
 ], 24) +
 P('Aucun antiviral (aciclovir) n’est recommandé dans la forme non compliquée. L’amoxicilline n’est pas indiquée ; elle provoque une éruption chez environ 30 % des enfants atteints.', 24, 23) +
 F('Situations particulières',
   TAB(['Situation', 'Particularité'], [
    ['Grossesse', 'Une primo-infection CMV ou toxoplasmose exige un suivi spécialisé ; pas d’AINS au 3e trimestre'],
    ['Personne âgée', 'Tableau atypique, hépatite plus marquée'],
    ['Enfant', 'Formes souvent pauvres ; test rapide moins sensible avant 4 ans'],
    ['Insuffisance hépatique', 'Paracétamol à dose réduite'],
    ['Insuffisance rénale (DFGe bas)', 'Éviter les AINS'],
    ['Immunodépression', 'PCR, risque de lymphoprolifération'],
   ]), 24) +
 SOCIAL('Un arrêt de travail ou d’école de quelques semaines est souvent nécessaire ; la reprise peut être progressive.',
        'La fatigue intense peut réduire l’aptitude à conduire ; le patient doit s’abstenir s’il se sent somnolent (LCR art. 31).') +
 H4('11.C Surveillance et critères de sortie') +
 TAB(['Quand', 'Quoi'], [
  ['Après 1–2 semaines', 'Fièvre, déglutition, douleur abdominale'],
  ['Après 4–6 semaines', 'Hémogramme et transaminases si anomalies marquées'],
  ['Après 3–4 semaines', 'Rate : reprise du sport si non palpable, échographie chez l’athlète'],
  ['Après 6 mois', 'Fatigue persistante : bilan d’EM/SFC'],
  ['Critères de sortie (hospitalisation)', 'Déglutition possible, voies aériennes libres, hémoglobine stable'],
 ]) + P('L’arrêt du sport de contact se lève quand la rate n’est plus palpable et au moins 3–4 semaines après le début.', 24) +
 H4('11.D Pronostic et recherche 2026') +
 P('La guérison clinique survient chez la plupart en 1–3 mois ; le virus reste latent à vie dans les lymphocytes B. Environ 12 % gardent une fatigue invalidante à 6 mois.', 24, 22) +
 P('Des vaccins contre l’EBV (dont un vaccin à ARN messager) sont en essais de phase 1–2 ; l’original parlait de phase III, ce qui est inexact.', 24))
ADD(12, 'Prévention',
 P('La prévention repose sur l’hygiène (pas de partage de verres en phase aiguë), le préservatif et le dépistage du VIH après exposition à risque.', 24) +
 F('Prévention primaire, secondaire et tertiaire',
   TAB(['Niveau', 'Mesure'], [
    ['Primaire', 'Hygiène, préservatif ; pas de vaccin disponible contre l’EBV ou le CMV'],
    ['Secondaire', 'Test VIH devant tout syndrome mononucléosique'],
    ['Tertiaire', 'Reprise progressive, prévention du déconditionnement, repérage d’une EM/SFC'],
   ]) + P('En Suisse, aucune recommandation nationale propre à la mononucléose n’a été retrouvée ; le test VIH suit la règle internationale.', 24)))
ADD(13, 'Points clés',
 P('Un syndrome mononucléosique impose un test VIH. '
   'Des EBNA positifs dès le premier prélèvement excluent une primo-infection récente à EBV. '
   'Pas de sport de contact pendant au moins 3–4 semaines. '
   'L’amoxicilline n’est pas indiquée et provoque souvent une éruption.', 24, 23))
ADD(14, 'Pièges d’examen',
 TAB(['Piège', 'Ce qu’il faut répondre'], [
  ['Amoxicilline pour une angine qui est une mononucléose', 'Non : éruption chez ≈ 30 % des enfants'],
  ['Oublier le VIH devant un syndrome mononucléosique', 'Il faut un test de 4e génération'],
  ['Conclure à une mononucléose avec EBNA positifs', 'Non : infection ancienne, chercher une autre cause'],
  ['Autoriser le football à 1 semaine', 'Non : attendre au moins 3–4 semaines'],
  ['Exclure l’EBV sur un test rapide négatif à J3', 'Non : le répéter ou faire la sérologie'],
  ['Donner de l’aciclovir dans la forme simple', 'Non : aucun bénéfice démontré'],
 ]) + P('Ces pièges reprennent les erreurs de l’original et la revue de Dunmire.', 24, 23))
CTX = {'_prefixe': 'Dans l’asthénie post-infectieuse',
 'ebv': 'VCA IgM positifs et EBNA négatifs confirment une mononucléose à EBV.',
 'sero': 'Elles distinguent EBV, CMV et toxoplasmose ; l’avidité des IgG date l’infection.',
 'nfs': 'Des lymphocytes ≥ 50 % dont ≥ 10 % atypiques orientent vers un syndrome mononucléosique.',
 'frottis': 'Il montre les lymphocytes atypiques hyperbasophiles.',
 'hep': 'Des transaminases 2–5 fois la norme signalent l’hépatite réactionnelle.',
 'vih': 'Un test de 4e génération positif impose la charge virale et l’avis spécialisé.',
 'echoabdo': 'Elle mesure la rate avant la reprise d’un sport de contact.',
 'pcr': 'Elle sert chez l’immunodéprimé, où la sérologie est peu fiable.',
 'cv': 'Une charge virale élevée confirme une primo-infection VIH avant la séroconversion.',
 'crp': 'Une CRP très élevée oriente plutôt vers une infection bactérienne.'}
if __name__ == '__main__':
    produire(M, PTS, SOURCES, CTX)
