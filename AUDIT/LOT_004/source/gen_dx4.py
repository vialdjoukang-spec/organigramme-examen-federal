# -*- coding: utf-8 -*-
"""DX.4 — Hypothyroïdie primaire. LOT 4, V5 → V7 AUDITÉ."""
from lot4_commun import *
POINT = mkPOINT('dx4')
M = META('dx4', 'DX.4', 'Hypothyroïdie primaire', 'Hypothyroïdie primaire (thyroïdite de Hashimoto et causes iatrogènes)',
         'LOT_004_DX4_Hypothyroidie_primaire_AUDITÉ.html',
         'Corrections majeures : la carence en iode a été combattue par l’iodation du sel, pas par la « fluoration » ; Novothyral® associe lévothyroxine et liothyronine, il n’est pas « à libération prolongée » ; le génotypage DIO2 ne guide pas le traitement en 2026 ; prévalences non sourcées remplacées ; seuil d’âge de l’ETA (70 ans) rétabli.')
RETRO = T('rétrocontrôle négatif', 'Le rétrocontrôle négatif est le frein qu’exercent les hormones thyroïdiennes sur l’hypophyse : quand la T4 baisse, l’hypophyse sécrète plus de TSH.')
DESIO = T('désiodase', 'Les désiodases sont des enzymes qui retirent un atome d’iode à la T4 pour former la T3, la forme active, dans les tissus.')
PTS = []
def ADD(*a): PTS.append(POINT(*a))
ADD(1, 'Définition et sémantique',
 P('L’hypothyroïdie primaire est un manque d’hormones thyroïdiennes (thyroxine T4, triiodothyronine T3) dû à une maladie de la thyroïde elle-même. '
   'Le corps ralentit : fatigue, frilosité, prise de poids, constipation. La TSH monte, car l’hypophyse tente de stimuler une glande défaillante.', 21, 20) +
 F('Terminologie',
   TAB(['Terme', 'Définition exacte', 'À ne pas confondre avec'], [
    ['Hypothyroïdie avérée (franche)', 'TSH élevée et T4 libre basse', 'Hypothyroïdie infraclinique'],
    ['Hypothyroïdie infraclinique (fruste)', 'TSH élevée, T4 libre normale', 'Variation transitoire de la TSH (convalescence)'],
    ['Hypothyroïdie centrale', 'T4 libre basse avec TSH basse, normale ou peu élevée (hypophyse)', 'Hypothyroïdie primaire'],
    ['Thyroïdite de Hashimoto', 'Thyroïdite auto-immune chronique, anti-TPO positifs', 'Thyroïdite subaiguë de De Quervain (douloureuse)'],
    ['Myxœdème', 'Infiltration de la peau par des glycosaminoglycanes ; le godet ne prend pas', 'Œdème cardiaque ou rénal'],
   ]) + P('Le diagnostic repose sur la biologie, car les symptômes sont peu spécifiques.', 21)))
ADD(2, 'Épidémiologie (Suisse, puis Europe)',
 P('En Suisse, la carence en iode a disparu grâce à l’iodation du sel, introduite en 1922 ; la thyroïdite de Hashimoto est devenue la première cause. '
   'En Europe, une méta-analyse trouve 4,94 % d’hypothyroïdie non diagnostiquée, dont 0,62 % de forme avérée ; les femmes sont environ deux fois plus touchées (6,4 % contre 3,4 %).', 63, 18) +
 F('Chiffres, terrain et histoire naturelle',
   TAB(['Donnée', 'Valeur', 'Portée'], [
    ['Hypothyroïdie non diagnostiquée, Europe', '4,94 %', 'Méta-analyse de Garmendia Madariaga (2014)'],
    ['Dont hypothyroïdie avérée', '0,62 %', 'Même étude'],
    ['Femmes / hommes', '6,4 % / 3,4 %', 'Rapport ≈ 2 : 1 (l’original disait 8 : 1, sans source)'],
    ['Iode dans le sel suisse', '25 mg/kg depuis 2014', 'OSAV'],
    ['« 1–2 % avérée, 8–10 % infraclinique » (original)', 'Non sourcé en Suisse', 'Remplacé par les données européennes'],
   ]) + P('Le terrain à risque réunit le sexe féminin, l’âge, les autres maladies auto-immunes, le post-partum, l’amiodarone, le lithium et l’immunothérapie anticancéreuse. '
          'Le pronostic est excellent sous traitement ; le coma myxœdémateux, rare, a une mortalité élevée.', 18, 21)))
ADD(3, 'Physiopathologie',
 P('Dans la thyroïdite de Hashimoto, des lymphocytes et des anticorps anti-thyroperoxydase (anti-TPO) détruisent lentement la glande. '
   'La baisse de la T4 lève le ' + RETRO + ', et la TSH augmente. '
   'Dans les tissus, le manque de T3 ralentit la production de chaleur et d’énergie.', 21) +
 F('Chaîne logique : de l’anatomie au traitement',
   TAB(['Étape', 'Ce qu’il faut comprendre'], [
    ['Anatomie', 'La thyroïde, devant la trachée, fabrique la T4 et un peu de T3 à partir de l’iode.'],
    ['Physiologie', 'L’hypothalamus (TRH) et l’hypophyse (TSH) règlent la glande ; la ' + DESIO + ' active la T4 en T3 dans les tissus.'],
    ['Physiopathologie', 'La destruction de la glande fait baisser la T4 ; la TSH monte fortement, car la relation TSH–T4 est log-linéaire.'],
    ['Clinique', 'Le métabolisme ralentit : fatigue, frilosité, bradycardie, constipation, peau sèche.'],
    ['Examens', 'La TSH est le meilleur test de dépistage ; la T4 libre classe la forme.'],
    ['Traitement', 'La lévothyroxine remplace la T4 ; les tissus la transforment en T3.'],
   ]), 21) +
 F('Mécanisme, exploration et cible thérapeutique',
   TAB(['Mécanisme', 'Lésion ou cause', 'Exploration', 'Cible thérapeutique'], [
    ['Auto-immunité', 'Thyroïdite de Hashimoto', 'Anti-TPO, échographie', 'Lévothyroxine à vie'],
    ['Iatrogène', 'Thyroïdectomie, iode radioactif, radiothérapie du cou', 'Anamnèse', 'Lévothyroxine'],
    ['Médicaments', 'Amiodarone, lithium, inhibiteurs de points de contrôle immunitaire', 'TSH avant et pendant le traitement', 'Lévothyroxine, sans arrêter forcément le médicament'],
    ['Carence ou excès d’iode', 'Rare en Suisse', 'Iodurie', 'Corriger l’apport'],
   ]) + P('L’accumulation de glycosaminoglycanes dans la peau explique le myxœdème ; le ralentissement du muscle explique les crampes et le réflexe achilléen lent.', 21)) +
 F('Dose de lévothyroxine : calcul', P('Dose complète ≈ 1,6 µg × poids (kg) par jour chez l’adulte jeune sans maladie coronarienne.', 20) +
   P('Exemple : patiente de 62 kg, TSH 24 mUI/L, T4 libre 7 pmol/L : 1,6 × 62 = 99 µg, soit 100 µg par jour.', 20)))
ADD(4, 'Raisonnement clinique et diagnostic différentiel',
 P('Devant une fatigue, le médecin dose d’abord la TSH. '
   'Il reconnaît ensuite l’urgence vitale, rare : le coma myxœdémateux. '
   'Puis il cherche la cause : auto-immune, chirurgicale ou médicamenteuse, et il exclut une hypothyroïdie centrale si la TSH est inadaptée.', 20, 21) +
 DIFF('hypo') + DIFF_FAT() +
 F('Diagnostics voisins devant un bilan thyroïdien anormal',
   TAB(['Situation', 'TSH', 'T4 libre', 'Interprétation'], [
    ['Hypothyroïdie primaire avérée', 'Élevée', 'Basse', 'Traiter'],
    ['Hypothyroïdie infraclinique', 'Élevée', 'Normale', 'Contrôler, traiter selon ETA'],
    ['Hypothyroïdie centrale', 'Basse ou normale', 'Basse', 'Bilan hypophysaire, cortisol d’abord'],
    ['Phase de récupération d’une maladie aiguë', 'Transitoirement élevée', 'Normale ou basse', 'Recontrôler à distance'],
    ['Interférence de dosage (biotine)', 'Faussement abaissée ou élevée', 'Variable', 'Arrêter la biotine 2 jours avant'],
   ]) + P('Ces situations n’ont pas de fréquence commune publiée chez le patient fatigué.', 21)))
ADD(5, 'Anamnèse ciblée et drapeaux rouges',
 P('L’anamnèse recherche la frilosité, la prise de poids, la constipation, les crampes, les règles abondantes et la lenteur. '
   'Elle note les antécédents de chirurgie ou d’iode radioactif, l’amiodarone, le lithium, l’immunothérapie et une grossesse.', 21) +
 U('Drapeaux rouges du coma myxœdémateux : hypothermie (< 35 °C), confusion, bradycardie, hypoventilation, hyponatrémie, souvent après une infection ou un sédatif chez une personne âgée. C’est une urgence : appeler le 144 et hospitaliser en soins intensifs.', 20) +
 F('Questions ciblées et leur raison',
   TAB(['Question', 'Pourquoi la poser'], [
    ['Avez-vous plus froid que votre entourage ?', 'La frilosité traduit le ralentissement de la thermogenèse.'],
    ['Avez-vous pris du poids sans manger plus ?', 'Rétention d’eau et métabolisme ralenti.'],
    ['Êtes-vous constipée depuis peu ?', 'Ralentissement du transit.'],
    ['Prenez-vous de l’amiodarone, du lithium, une immunothérapie ?', 'Causes iatrogènes fréquentes.'],
    ['Êtes-vous enceinte ou souhaitez-vous l’être ?', 'La cible de TSH et les doses changent.'],
    ['Prenez-vous de la biotine ?', 'Elle fausse certains dosages.'],
   ]), 21, 61))
ADD(6, 'Examen clinique',
 P('L’examen inspecte le visage, la peau et les sourcils, palpe la thyroïde et mesure le pouls. Il teste le réflexe achilléen.', 21) +
 P('Valeurs normales : thyroïde non palpable ou souple, pouls 60–100/min, réflexe achilléen à relaxation rapide. Les signes cliniques ont une sensibilité faible ; aucun ne suffit seul.', 21) +
 F('Signes, technique et valeur',
   TAB(['Signe', 'Technique', 'Ce qu’il signifie'], [
    ['Visage bouffi, paupières gonflées', 'Inspection', 'Myxœdème'],
    ['Peau sèche, froide, jaunâtre', 'Palpation du dos de la main', 'Ralentissement, carotène accumulé'],
    ['Goitre ferme et irrégulier', 'Palpation debout, derrière le patient, lors de la déglutition', 'Hashimoto'],
    ['Bradycardie', 'Pouls au repos', 'Moins de stimulation du cœur par la T3'],
    ['Relaxation lente du réflexe achilléen', 'Patient à genoux sur une chaise', 'Ralentissement musculaire'],
    ['Perte de la queue des sourcils', 'Inspection', 'Peu spécifique'],
   ]), 21))
ADD(7, 'Syndromes et signes cliniques',
 F('Signes fonctionnels (symptômes rapportés)', UL(['Fatigue, lenteur', 'Frilosité', 'Constipation', 'Crampes, raideur', 'Règles abondantes']), 21) +
 F('Signes physiques (constatés à l’examen)', UL(['Bradycardie', 'Peau sèche et froide', 'Visage bouffi', 'Voix rauque', 'Goitre ou thyroïde non palpable']), 21) +
 P('Le syndrome d’hypométabolisme réunit fatigue, frilosité, bradycardie, constipation et prise de poids : il traduit le manque de T3 dans les cellules. '
   'Le syndrome cutanéo-muqueux réunit myxœdème, grosse langue, voix rauque et canal carpien : il traduit l’infiltration des tissus.', 21) +
 F('Syndrome d’hypométabolisme', TAB(['Signe', 'Mécanisme', 'Valeur'], [
    ['Frilosité', 'Moins de production de chaleur', 'Évocateur'],
    ['Bradycardie', 'Moins de récepteurs β-adrénergiques sensibles', 'Peu sensible'],
    ['Prise de poids modérée', 'Rétention d’eau, métabolisme bas', 'Rarement > 5 kg'],
   ]), 21) +
 F('Syndrome cutanéo-muqueux', TAB(['Signe', 'Mécanisme', 'Valeur'], [
    ['Myxœdème', 'Glycosaminoglycanes dans le derme', 'Forme évoluée'],
    ['Voix rauque', 'Infiltration des cordes vocales', 'Tardif'],
    ['Syndrome du canal carpien', 'Compression du nerf médian', 'Peu spécifique'],
   ]), 21))
ADD(8, 'Critères diagnostiques',
 P('Le diagnostic est biologique. Un symptôme isolé ne suffit pas, pas plus que des anti-TPO positifs : il faut une TSH élevée, contrôlée, avec la T4 libre.', 19, 20) +
 F('Critères (ETA 2013, ATA 2014)',
   TAB(['Critère', 'Seuil'], [
    ['TSH normale (adulte)', '≈ 0,4–4,0 mUI/L selon le laboratoire'],
    ['Hypothyroïdie avérée', 'TSH > limite supérieure et T4 libre < limite inférieure (≈ 12 pmol/L)'],
    ['Infraclinique', 'TSH > limite supérieure, T4 libre normale, confirmée à 2–3 mois'],
    ['Infraclinique sévère', 'TSH ≥ 10 mUI/L'],
    ['Grossesse', 'Normes par trimestre ; à défaut, limite supérieure ≈ 4,0 mUI/L au 1er trimestre'],
   ]) + P('L’ETA recommande de répéter une TSH élevée isolée avant de traiter, car elle se normalise souvent.', 19, 61)))
ADD(9, 'Examens complémentaires',
 H4('9.a Examen de référence') +
 P('La référence est le couple TSH et T4 libre. '
   'La TSH a une sensibilité très élevée pour l’hypothyroïdie primaire ; sa spécificité baisse en convalescence, avec l’âge et en cas d’atteinte hypophysaire.', 20, 21) +
 H4('9.b Examens de première et de deuxième intention') +
 P('En première intention, on dose la TSH seule chez le patient fatigué. En deuxième intention, on ajoute la T4 libre si la TSH est anormale, puis les anti-TPO.', 20) +
 TAB(['Intention', 'Examen', 'Pourquoi'], [
  ['1re', 'TSH', 'Dépistage'],
  ['2e', 'T4 libre', 'Classer la forme'],
  ['2e', 'Anti-TPO', 'Cause auto-immune ; risque d’évolution'],
  ['2e', 'Échographie thyroïdienne', 'Nodule palpable, goitre asymétrique, compression'],
  ['2e', 'Cortisol du matin', 'Hypothyroïdie centrale : exclure une insuffisance corticotrope'],
  ['2e', 'Bilan lipidique, CK, sodium', 'Retentissement'],
 ]) +
 H4('9.c Prescription et formules') +
 P('Indication : fatigue, symptômes évocateurs, terrain à risque. Moment : le matin, à distance d’une maladie aiguë ; contrôle 6–8 semaines après tout changement de dose. '
   'Préparation : arrêt de la biotine 2 jours avant ; prise de lévothyroxine après la prise de sang le jour du contrôle.', 20) +
 TAB(['Grandeur', 'Formule', 'Repère'], [['Dose complète', '1,6 µg/kg/j', 'Adulte jeune'], ['Dose de départ', '12,5–25 µg/j', 'Âgé ou coronarien'], ['Paliers', '+12,5–25 µg toutes les 4–6 semaines', 'Selon la TSH']]) +
 H4('9.d Interprétation : positif, négatif, limite, discordant') +
 TAB(['Situation', 'Interprétation', 'Conduite'], [
  ['Positif : TSH > 10 mUI/L', 'Hypothyroïdie probable', 'T4 libre, traiter'],
  ['Négatif : TSH normale', 'Hypothyroïdie primaire exclue', 'Chercher une autre cause'],
  ['Limite : TSH 4–10 mUI/L', 'Infraclinique ou transitoire', 'Recontrôler à 2–3 mois avec anti-TPO'],
  ['Discordant : T4 libre basse, TSH normale', 'Hypothyroïdie centrale', 'Bilan hypophysaire, IRM'],
 ]) +
 H4('9.e Alternatives') +
 P('Grossesse : normes par trimestre, contrôle toutes les 4 semaines. Enfant : normes d’âge, dépistage néonatal. '
   'DFGe bas : TSH un peu plus haute sans hypothyroïdie. Produit iodé : il peut déclencher une hypothyroïdie ; l’IRM hypophysaire sert si la forme est centrale ; un pacemaker ne gêne pas l’échographie.', 61, 62))
ADD(10, 'Arbre décisionnel',
 P('Si la TSH est élevée, alors on dose la T4 libre. Si la T4 libre est basse, alors on traite ; si elle est normale, alors on recontrôle.', 19, 20) +
 F('Arbre décisionnel : fatigue et suspicion d’hypothyroïdie',
   OL(['TSH normale : hypothyroïdie primaire exclue.',
       'TSH élevée, T4 libre basse : hypothyroïdie avérée → lévothyroxine.',
       'TSH 4–10 mUI/L, T4 libre normale : recontrôle à 2–3 mois avec anti-TPO.',
       'TSH ≥ 10 mUI/L confirmée : traiter (ETA).',
       'TSH 4–10 mUI/L, patient < 70 ans symptomatique : essai de 3 mois de lévothyroxine, arrêt si pas d’effet.',
       'Grossesse ou désir de grossesse : traiter plus tôt, selon les normes du trimestre.',
       'T4 libre basse avec TSH inadaptée : cortisol et bilan hypophysaire avant la lévothyroxine.']), 19, 61))
ADD(11, 'Prise en charge',
 H4('11.A Buts : d’abord l’urgence (coma myxœdémateux), car la mortalité est élevée') +
 P('Le traitement rétablit l’euthyroïdie, normalise la TSH et supprime les symptômes, sans surdosage.', 20) +
 TAB(['But', 'Cible chiffrée'], [['TSH (adulte)', '≈ 0,4–4,0 mUI/L'], ['TSH (personne très âgée)', 'Cible plus haute tolérée, jusqu’à ≈ 6 mUI/L'], ['Grossesse', 'TSH < 2,5 mUI/L souvent visée']]) +
 H4('11.B Moyens et méthodes : forme compliquée en urgence, puis forme non compliquée en ambulatoire') +
 P('La forme compliquée (coma myxœdémateux) se traite en urgence aux soins intensifs : hydrocortisone d’abord, puis lévothyroxine IV, réchauffement et ventilation dans les premières heures. '
   'La forme non compliquée se traite en ambulatoire, avec des mesures générales et une éducation du patient sur la prise à jeun.', 20) +
 P('Moyens non médicamenteux : apport normal en iode (sel iodé), pas de supplément iodé à forte dose, pas d’algues en grande quantité.', 63) +
 FICHE([
  ['Hormone thyroïdienne : lévothyroxine (Euthyrox®, Eltroxin®, Tirosint®)', 'Remplace la T4, convertie en T3 par les désiodases', 'Demi-vie ≈ 7 jours ; équilibre en 6 semaines ; absorption ≈ 70 % à jeun', '1,6 µg/kg/j ; âgé ou coronarien : 12,5–25 µg/j puis paliers ; à vie si Hashimoto', 'Surdosage : palpitations, fibrillation atriale, ostéoporose', 'Insuffisance surrénale non traitée, infarctus récent', 'Fer, calcium, IPP, résines : espacer de 4 h ; augmente l’effet des anticoagulants'],
  ['Association lévothyroxine + liothyronine (Novothyral®)', 'Apporte T4 et T3', 'La T3 a une demi-vie courte (≈ 1 jour)', 'Pas de première intention', 'Pics de T3, palpitations', 'Maladie coronarienne, arythmie', 'Les mêmes'],
 ], 20, 21) +
 P('Correction : Novothyral® associe T4 et T3, sans libération prolongée. Le génotypage du gène DIO2, cité par l’original, ne guide pas le traitement en pratique.', 20, 21) +
 F('Situations particulières',
   TAB(['Situation', 'Particularité'], [
    ['Grossesse', 'Augmenter la dose d’environ 25–30 % dès le diagnostic de grossesse ; TSH toutes les 4 semaines'],
    ['Personne âgée', 'Commencer bas, augmenter lentement ; éviter le surdosage'],
    ['Enfant', 'Dose par kilo plus élevée ; dépistage néonatal en Suisse'],
    ['Insuffisance hépatique', 'Pas d’adaptation habituelle ; surveiller la TSH'],
    ['Insuffisance rénale (DFGe bas)', 'Pas d’adaptation de dose ; interpréter la TSH avec prudence'],
    ['Maladie coronarienne', 'Dose initiale 12,5–25 µg/j'],
   ]), 61, 20) +
 SOCIAL('Un arrêt de travail est rarement nécessaire ; la fatigue s’améliore en quelques semaines.',
        'L’hypothyroïdie traitée n’empêche pas la conduite ; un coma myxœdémateux ou une confusion l’interdisent jusqu’à guérison (LCR art. 31).') +
 H4('11.C Surveillance et critères de sortie') +
 TAB(['Quand', 'Quoi'], [
  ['6–8 semaines après tout changement', 'TSH (état d’équilibre)'],
  ['Puis tous les 6–12 mois', 'TSH une fois la dose stable'],
  ['Grossesse', 'TSH toutes les 4 semaines jusqu’à mi-grossesse'],
  ['Arrêt du traitement', 'Essai d’arrêt possible si infraclinique sans bénéfice après 3 mois'],
  ['Critères de sortie (coma myxœdémateux)', 'Conscience, température, ventilation et sodium normalisés'],
 ]) + P('Les anti-TPO ne se répètent pas au suivi, car leur titre ne change pas la dose.', 20) +
 H4('11.D Pronostic et recherche 2026') +
 P('Le pronostic est excellent sous traitement ; la thyroïdite de Hashimoto ne guérit pas.', 21) +
 P('L’intérêt de l’association T4 + T3 chez les patients restés fatigués avec une TSH normale reste à l’essai ; aucune recommandation ne la propose en routine en 2026.', 21))
ADD(12, 'Prévention',
 P('La prévention repose sur un apport suffisant en iode, la surveillance de la TSH sous amiodarone, lithium ou immunothérapie, et le dépistage chez la femme enceinte à risque.', 63, 60, 61) +
 F('Prévention primaire, secondaire et tertiaire',
   TAB(['Niveau', 'Mesure'], [
    ['Primaire', 'Sel iodé (programme suisse depuis 1922)'],
    ['Secondaire', 'TSH sous amiodarone, lithium, immunothérapie ; femmes enceintes à risque'],
    ['Tertiaire', 'Dose adaptée, éviter surdosage et coma myxœdémateux'],
   ]) + P('En Suisse, l’OSAV fixe la teneur en iode du sel ; l’original confondait iodation et fluoration.', 63)))
ADD(13, 'Points clés',
 P('La TSH est le test de dépistage ; la T4 libre classe la forme. '
   'Une TSH élevée isolée se recontrôle avant de traiter. '
   'Chez le sujet âgé ou coronarien, la lévothyroxine commence à faible dose. '
   'Dans une hypothyroïdie centrale, le cortisol se corrige avant la lévothyroxine.', 19, 20))
ADD(14, 'Pièges d’examen',
 TAB(['Piège', 'Ce qu’il faut répondre'], [
  ['Pleine dose chez un coronarien âgé', 'Non : 12,5–25 µg/j, risque d’angine de poitrine'],
  ['Lévothyroxine avant hydrocortisone dans une atteinte hypophysaire', 'Non : risque de crise surrénalienne'],
  ['Contrôler la TSH 2 semaines après un changement', 'Non : attendre 6–8 semaines'],
  ['Prendre la lévothyroxine avec le fer ou le calcium', 'Il faut espacer de 4 h'],
  ['Croire que la fluoration du sel corrige la carence en iode', 'Non : c’est l’iodation'],
  ['Traiter une TSH à 6 mUI/L mesurée une seule fois', 'Il faut la recontrôler à 2–3 mois'],
 ]) + P('Ces pièges reprennent les recommandations de l’ETA et de l’ATA.', 19, 20))
CTX = {'_prefixe': 'Dans l’hypothyroïdie primaire',
 'tsh': 'Une TSH élevée est le premier signe ; > 10 mUI/L confirmée impose le traitement.',
 't4t3': 'Une T4 libre basse avec TSH élevée définit la forme avérée ; la T3 n’est pas utile.',
 'tpo': 'Des anti-TPO positifs signent une thyroïdite de Hashimoto et prédisent l’évolution.',
 'echothy': 'Elle ne sert que si un nodule ou un goitre asymétrique est palpé.',
 'cort': 'Un cortisol bas impose l’hydrocortisone avant la lévothyroxine.',
 'lip': 'Un LDL élevé peut baisser sous traitement.',
 'ck': 'Des CK élevées traduisent une myopathie hypothyroïdienne.',
 'iono': 'Une hyponatrémie évoque une forme sévère.',
 'irm': 'Une IRM hypophysaire sert si l’hypothyroïdie est centrale.',
 'nfs': 'Une anémie peut accompagner l’hypothyroïdie.'}
if __name__ == '__main__':
    produire(M, PTS, SOURCES, CTX)
