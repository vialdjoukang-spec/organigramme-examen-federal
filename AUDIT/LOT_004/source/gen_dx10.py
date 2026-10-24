# -*- coding: utf-8 -*-
"""DX.10 — Maladie d’Addison. LOT 4, V5 → V7 AUDITÉ."""
from lot4_commun import *
POINT = mkPOINT('dx10')
M = META('dx10', 'DX.10', 'Maladie d’Addison', 'Maladie d’Addison (insuffisance surrénale primaire)',
         'LOT_004_DX10_Maladie_d_Addison_AUDITÉ.html',
         'Corrections majeures : seuil du pic de cortisol adapté aux dosages récents ≈ 390–415 nmol/L (et non 450) ; fludrocortisone de départ 50–100 µg ; crise : 100 mg d’hydrocortisone IV puis 200 mg/24 h ; Efmody® est autorisé dans l’hyperplasie congénitale, pas dans l’Addison ; « SSED » non sourcé retiré ; rapport Na/K non sourcé retiré ; thérapies cellulaires et rituximab présentés comme recherche.')
CORT = T('cortex surrénalien', 'Le cortex surrénalien est l’écorce des glandes posées sur les reins ; il fabrique le cortisol (hormone du stress et du sucre), l’aldostérone (hormone du sel) et des androgènes.')
PTS = []
def ADD(*a): PTS.append(POINT(*a))
ADD(1, 'Définition et sémantique',
 P('La maladie d’Addison est une insuffisance surrénale primaire : le ' + CORT + ' est détruit des deux côtés. '
   'Il manque alors le cortisol, l’aldostérone et les androgènes surrénaliens ; sans traitement, la maladie est mortelle.', 37, 57) +
 F('Terminologie',
   TAB(['Terme', 'Définition exacte', 'À ne pas confondre avec'], [
    ['Insuffisance surrénale primaire', 'Atteinte de la glande : cortisol et aldostérone bas, ACTH haute', 'Insuffisance corticotrope'],
    ['Insuffisance corticotrope (secondaire)', 'Manque d’ACTH : cortisol bas, aldostérone préservée', 'Addison'],
    ['Crise surrénalienne', 'Décompensation aiguë avec hypotension ; urgence vitale', 'Gastro-entérite simple'],
    ['Mélanodermie', 'Peau brune par excès de POMC et d’ACTH', 'Bronzage'],
    ['Polyendocrinopathie auto-immune', 'Association à d’autres maladies auto-immunes', 'Addison isolé'],
   ]) + P('Seule l’atteinte primaire donne une mélanodermie et une hyperkaliémie.', 37, 57)))
ADD(2, 'Épidémiologie (Suisse, puis Europe)',
 P('En Suisse, aucun registre national n’a été retrouvé. En Europe, la prévalence est d’environ 100–140 par million ; appliquée aux 8,9 millions d’habitants, elle donne environ 900–1250 patients (estimation).', 38) +
 F('Chiffres, terrain et histoire naturelle',
   TAB(['Donnée', 'Valeur', 'Portée'], [
    ['Prévalence', '≈ 100–140 / million', 'Europe, revues'],
    ['Cause auto-immune', '≈ 80–90 %', 'Pays industrialisés'],
    ['Crises surrénaliennes chez des patients éduqués', '8,3 pour 100 patients-années', 'Étude de Hahner 2015'],
    ['Insuffisance corticotrope après corticoïdes', 'Beaucoup plus fréquente que l’Addison', 'Endocrine Society'],
   ]) + P('Le terrain est celui des maladies auto-immunes (thyroïde, diabète de type 1, vitiligo). '
          'Le pronostic est bon sous traitement, mais les crises restent fréquentes et parfois mortelles.', 57, 39, 37)))
ADD(3, 'Physiopathologie',
 P('Le plus souvent, des lymphocytes et des anticorps contre l’enzyme 21-hydroxylase détruisent les trois couches du cortex. '
   'Sans aldostérone, le rein perd le sel et retient le potassium. Sans cortisol, la glycémie baisse et les vaisseaux répondent moins à l’adrénaline.', 57) +
 F('Chaîne logique : de l’anatomie au traitement',
   TAB(['Étape', 'Ce qu’il faut comprendre'], [
    ['Anatomie', 'Trois couches : glomérulée (aldostérone), fasciculée (cortisol), réticulée (androgènes).'],
    ['Physiologie', 'L’hypophyse règle le cortisol par l’ACTH ; le rein règle l’aldostérone par la rénine.'],
    ['Physiopathologie', 'Le cortisol bas lève le frein sur l’hypophyse : la POMC monte et colore la peau.'],
    ['Clinique', 'D’où fatigue, perte de poids, hypotension, envie de sel et peau brune.'],
    ['Examens', 'Cortisol bas, ACTH haute, rénine haute ; test au Synacthène® pour confirmer.'],
    ['Traitement', 'Remplacer le cortisol (hydrocortisone) et l’aldostérone (fludrocortisone).'],
   ]), 57, 37) +
 F('Mécanisme, exploration et cible thérapeutique',
   TAB(['Mécanisme', 'Lésion ou cause', 'Exploration', 'Cible thérapeutique'], [
    ['Manque d’aldostérone', 'Couche glomérulée détruite', 'Na⁺ bas, K⁺ haut, rénine haute', 'Fludrocortisone'],
    ['Manque de cortisol', 'Couche fasciculée détruite', 'Cortisol bas, test au Synacthène®', 'Hydrocortisone'],
    ['Excès de POMC', 'Frein hypophysaire levé', 'ACTH haute', 'Hydrocortisone'],
    ['Manque d’androgènes', 'Couche réticulée détruite', 'DHEA-S bas', 'DHEA chez certaines femmes'],
   ]) + P('Cette chaîne explique pourquoi la dexaméthasone seule ne suffit pas : elle n’a aucun effet sur le sel.', 37)) +
 F('Trou anionique', P('Trou anionique = Na⁺ − (Cl⁻ + HCO₃⁻) ; normal 8–12 mmol/L.', 37) +
   P('Exemple : 128 − (100 + 18) = 10 mmol/L, soit une acidose à trou anionique normal par manque d’aldostérone.', 37)))
ADD(4, 'Raisonnement clinique et diagnostic différentiel',
 P('Devant une fatigue avec hypotension, le médecin cherche d’abord une crise surrénalienne : choc, vomissements, douleurs abdominales. '
   'Puis il distingue l’atteinte primaire de l’atteinte secondaire, beaucoup plus fréquente après l’arrêt brutal de corticoïdes pris plus de 3 semaines.', 37, 58) +
 DIFF('addison') + DIFF_FAT() +
 F('Causes et diagnostics voisins',
   TAB(['Cause ou diagnostic', 'Élément distinctif', 'Examen discriminant'], [
    ['Surrénalite auto-immune', 'Autres maladies auto-immunes', 'Anticorps anti-21-hydroxylase'],
    ['Tuberculose surrénalienne', 'Migration, antécédent de tuberculose', 'Scanner (calcifications), IGRA'],
    ['Métastases bilatérales', 'Cancer du poumon connu', 'Scanner'],
    ['Hémorragie bilatérale', 'Sepsis, anticoagulants', 'Scanner'],
    ['Adrénoleucodystrophie', 'Homme jeune, signes neurologiques', 'Acides gras à très longue chaîne'],
    ['Insuffisance corticotrope', 'Corticoïdes récents, pas de mélanodermie, K⁺ normal', 'ACTH basse'],
   ]), 37, 57))
ADD(5, 'Anamnèse ciblée et drapeaux rouges',
 P('L’anamnèse cherche une fatigue croissante dans la journée, une perte d’appétit et de poids, une envie de sel et des malaises debout. '
   'Elle note les corticoïdes pris, même en inhalation ou en infiltration.', 37) +
 U('Drapeaux rouges de crise surrénalienne : douleurs abdominales, vomissements, fièvre, confusion, hypotension. Ils imposent l’appel au 144 et une hydrocortisone IV immédiate, sans attendre les résultats.', 58, 37) +
 F('Questions ciblées et leur raison',
   TAB(['Question', 'Pourquoi la poser'], [
    ['Êtes-vous plus fatigué le soir ?', 'Fatigue croissante typique.'],
    ['Avez-vous envie de manger très salé ?', 'Manque d’aldostérone.'],
    ['Avez-vous des vertiges en vous levant ?', 'Hypotension orthostatique.'],
    ['Avez-vous pris des corticoïdes ces derniers mois ?', 'Insuffisance corticotrope.'],
    ['Avez-vous une maladie de la thyroïde ou un diabète de type 1 ?', 'Auto-immunité associée.'],
    ['Votre peau a-t-elle foncé ?', 'Mélanodermie.'],
   ]), 37, 57))
ADD(6, 'Examen clinique',
 P('L’examen cherche une peau brune sur les plis, les cicatrices et les gencives, et mesure la pression couché puis debout.', 37) +
 P('Valeurs normales : pas de chute de pression > 20 mmHg debout. Il note aussi un vitiligo et, chez la femme, une perte des poils axillaires et pubiens.', 57) +
 F('Signes, technique et valeur',
   TAB(['Signe', 'Technique', 'Ce qu’il signifie'], [
    ['Mélanodermie des plis et des cicatrices', 'Inspection en lumière du jour', 'Atteinte primaire'],
    ['Taches brunes des gencives', 'Inspection de la bouche', 'Atteinte primaire'],
    ['Hypotension orthostatique', 'Pression couché puis debout', 'Manque de sel'],
    ['Vitiligo', 'Inspection', 'Auto-immunité'],
    ['Perte de poils axillaires et pubiens (femme)', 'Inspection', 'Manque d’androgènes'],
   ]), 37, 57))
ADD(7, 'Syndromes et signes cliniques',
 F('Signes fonctionnels (symptômes rapportés)', UL(['Fatigue croissante dans la journée', 'Perte d’appétit, nausées', 'Envie de sel', 'Vertiges debout', 'Douleurs abdominales']), 37) +
 F('Signes physiques (constatés à l’examen)', UL(['Mélanodermie', 'Hypotension', 'Perte de poids', 'Vitiligo']), 37) +
 P('Le syndrome de manque de sel réunit hypotension, envie de sel, sodium bas et potassium haut : il traduit le manque d’aldostérone. '
   'Le syndrome de manque de cortisol réunit fatigue, perte de poids, hypoglycémie et peau brune : il traduit le manque de cortisol et l’excès de POMC.', 37, 57) +
 F('Manque d’aldostérone', TAB(['Signe', 'Mécanisme', 'Valeur'], [
    ['Hyponatrémie', 'Fuite de sel', 'Fréquente'],
    ['Hyperkaliémie', 'Potassium retenu', 'Atteinte primaire'],
    ['Rénine élevée', 'Volume bas', 'Atteinte primaire'],
   ]), 37) +
 F('Déficit en glucocorticoïdes', TAB(['Signe', 'Mécanisme', 'Valeur'], [
    ['Hypoglycémie', 'Moins de néoglucogenèse', 'Surtout chez l’enfant'],
    ['Mélanodermie', 'Excès de POMC', 'Atteinte primaire'],
    ['Fatigue', 'Manque de cortisol', 'Constante'],
   ]), 37))
ADD(8, 'Critères diagnostiques',
 P('Le diagnostic exige un cortisol insuffisant au test de stimulation et une ACTH élevée. Un cortisol bas isolé ne suffit pas.', 37) +
 F('Critères (Endocrine Society 2016, seuils mis à jour 2021)',
   TAB(['Critère', 'Seuil'], [
    ['Pic de cortisol après 250 µg de Synacthène® (30 ou 60 min)', '< 500 nmol/L (anciens dosages)'],
    ['Avec les dosages récents (Roche Gen II, spectrométrie de masse)', '≈ 390–415 nmol/L (14–15 µg/dL)'],
    ['ACTH du matin', '> 2 fois la limite supérieure : atteinte primaire'],
    ['Cortisol du matin', '< 140 nmol/L avec ACTH haute : très évocateur'],
    ['Rénine', 'Élevée, aldostérone basse'],
   ]) + P('Selon cette recommandation, l’original indiquait à tort 450 nmol/L ; les seuils dépendent du dosage du laboratoire.', 37, 59)))
ADD(9, 'Examens complémentaires',
 H4('9.a Examen de référence') +
 P('L’examen de référence est le test au Synacthène® : 250 µg IV ou IM, cortisol à 0, 30 et 60 min. '
   'Il est précédé du cortisol et de l’ACTH à 8 h ; il ne doit jamais retarder le traitement d’une crise. Sa sensibilité est élevée pour l’atteinte primaire, plus faible pour une atteinte corticotrope récente ; sa spécificité est élevée.', 37) +
 H4('9.b Examens de première et de deuxième intention') +
 P('En première intention, on dose ionogramme, cortisol, ACTH et rénine. En deuxième intention, on cherche la cause.', 37) +
 TAB(['Intention', 'Examen', 'Pourquoi'], [
  ['1re', 'Ionogramme, urée, créatinine, glycémie, calcium', 'Na⁺ bas, K⁺ haut, hypoglycémie'],
  ['1re', 'Cortisol et ACTH à 8 h', 'Orientation primaire ou secondaire'],
  ['1re', 'Rénine et aldostérone', 'Manque d’aldostérone'],
  ['1re', 'Test au Synacthène®', 'Confirmation'],
  ['2e', 'Anticorps anti-21-hydroxylase', 'Cause auto-immune (positifs dans la majorité des cas)'],
  ['2e', 'TSH, anticorps anti-TPO, HbA1c, vitamine B12', 'Maladies auto-immunes associées'],
  ['2e', 'Scanner des surrénales', 'Anticorps négatifs : tuberculose, métastases, hémorragie'],
  ['2e', 'Acides gras à très longue chaîne', 'Homme jeune : adrénoleucodystrophie'],
 ]) +
 H4('9.c Prescription et formules') +
 P('Indication : fatigue avec hypotension, hyponatrémie, hyperkaliémie ou mélanodermie. Moment : cortisol et ACTH à 8 h ; test au Synacthène® à tout moment. '
   'Préparation : arrêter les œstrogènes oraux 6 semaines avant si possible, car ils augmentent la protéine porteuse du cortisol.', 37) +
 TAB(['Grandeur', 'Formule', 'Repère'], [['Trou anionique', 'Na⁺ − (Cl⁻ + HCO₃⁻)', '8–12 mmol/L'], ['Conversion du cortisol', 'µg/dL × 27,6 = nmol/L', '18 µg/dL ≈ 500 nmol/L']]) +
 H4('9.d Interprétation : positif, négatif, limite, discordant') +
 TAB(['Situation', 'Interprétation', 'Conduite'], [
  ['Positif : pic sous le seuil, ACTH haute', 'Addison', 'Traitement à vie'],
  ['Négatif : pic au-dessus du seuil', 'Insuffisance surrénale exclue', 'Autre cause'],
  ['Limite : pic juste sous le seuil', 'Selon le dosage', 'Vérifier le seuil du laboratoire'],
  ['Discordant : pic normal mais corticoïdes arrêtés récemment', 'Insuffisance corticotrope récente possible', 'Retester plus tard'],
 ]) +
 H4('9.e Alternatives') +
 P('Grossesse : le cortisol total monte ; seuils propres et avis spécialisé. Enfant : test au Synacthène® avec dose adaptée. '
   'DFGe < 30 : les seuils restent valables ; hyperkaliémie à interpréter avec la fonction rénale.', 37))
ADD(10, 'Arbre décisionnel',
 P('Si une crise est suspectée, alors on traite avant de tester. Sinon, on dose le cortisol du matin puis on confirme.', 37, 58) +
 F('Arbre décisionnel : fatigue avec suspicion d’insuffisance surrénale',
   OL(['Choc, vomissements : prélever cortisol et ACTH, puis hydrocortisone 100 mg IV et NaCl 0,9 % sans attendre.',
       'Patient stable : cortisol et ACTH à 8 h.',
       'Cortisol < 140 nmol/L et ACTH haute : Addison très probable.',
       'Cortisol 140–500 nmol/L : test au Synacthène®.',
       'Pic insuffisant et ACTH haute : atteinte primaire ; rénine.',
       'Anticorps anti-21-hydroxylase ; si négatifs, scanner.']), 37))
ADD(11, 'Prise en charge',
 H4('11.A Buts : d’abord l’urgence (crise surrénalienne), car elle peut tuer en quelques heures') +
 P('Le traitement remplace les hormones manquantes, restaure le poids et la pression, et prévient les crises.', 37) +
 TAB(['But', 'Cible chiffrée'], [['Hydrocortisone', '15–25 mg/j en 2–3 prises'], ['Rénine sous fludrocortisone', 'Moitié supérieure de la normale'], ['Pression debout', 'Sans hypotension orthostatique']]) +
 H4('11.B Moyens et méthodes : forme compliquée en urgence, puis forme non compliquée en ambulatoire') +
 P('La forme compliquée (crise surrénalienne) se traite en urgence : hydrocortisone 100 mg IV ou IM, puis 200 mg/24 h, et 1 L de NaCl 0,9 % dans la première heure. '
   'La forme non compliquée se traite en ambulatoire, avec des mesures générales : sel libre, carte d’urgence, kit d’injection et règles de stress.', 37, 58) +
 P('Règles de stress : doubler la dose orale si fièvre > 38 °C, la tripler si > 39 °C, jusqu’à la guérison ; passer à l’injection en cas de vomissements.', 37) +
 FICHE([
  ['Glucocorticoïde : hydrocortisone (Hydrocortison Galepharm® ; Alkindi® chez l’enfant)', 'Remplace le cortisol', 'Demi-vie ≈ 1,5 h', '15–25 mg/j en 2–3 prises (ex. 10–5–5 mg à 7 h, 12 h, 16 h), à vie', 'Surdosage : prise de poids, hypertension, ostéoporose', 'Aucune en substitution', 'Inducteurs du CYP3A4 (rifampicine) : augmenter'],
  ['Hydrocortisone à libération modifiée (Plenadren®)', 'Profil plus proche du rythme naturel', '1 prise le matin', '20 mg le matin', 'Comme ci-dessus', 'Aucune en substitution', 'Inducteurs du CYP3A4'],
  ['Minéralocorticoïde : fludrocortisone (Florinef®)', 'Remplace l’aldostérone', 'Demi-vie ≈ 3,5 h', '50–100 µg le matin ; jusqu’à 200 µg si besoin', 'Œdèmes, hypertension, hypokaliémie', 'Aucune en substitution', 'Diurétiques'],
 ], 37, 40) +
 P('Au-delà de 50 mg/j d’hydrocortisone, la fludrocortisone est inutile, car l’hydrocortisone active alors le récepteur du sel.', 37) +
 F('Situations particulières',
   TAB(['Situation', 'Particularité'], [
    ['Grossesse', 'Hydrocortisone + 20–40 % au 3e trimestre ; 100 mg à l’accouchement'],
    ['Personne âgée', 'Dose la plus basse efficace ; surveiller l’os et la pression'],
    ['Enfant', 'Hydrocortisone en granulés selon la surface corporelle'],
    ['Insuffisance hépatique', 'Hydrocortisone sans adaptation majeure'],
    ['Insuffisance rénale (DFGe bas)', 'Fludrocortisone réduite si hypertension ou œdèmes'],
    ['Chirurgie', '100 mg IV à l’induction, puis 200 mg/24 h'],
   ]), 37) +
 SOCIAL('Un arrêt de travail est fréquent au diagnostic ; la reprise est habituelle sous traitement.',
        'L’Addison traité n’interdit pas la conduite ; une crise ou une hypoglycémie l’interdit temporairement.') +
 H4('11.C Surveillance et critères de sortie') +
 TAB(['Quand', 'Quoi'], [
  ['Chaque consultation', 'Fatigue, poids, pression couché et debout'],
  ['Une à deux fois par an', 'Na⁺, K⁺, rénine'],
  ['Chaque année', 'TSH, HbA1c, vitamine B12'],
  ['À ne pas faire', 'Doser l’ACTH ou le cortisol pour régler l’hydrocortisone'],
  ['Critères de sortie d’hospitalisation', 'Pression stable, alimentation possible, dose orale doublée, éducation faite'],
 ]) + P('L’hydrocortisone se règle sur la clinique.', 37) +
 H4('11.D Pronostic et recherche 2026') +
 P('Sous traitement, la vie est presque normale ; les crises restent la principale cause de décès évitable.', 57, 39) +
 P('Les pompes sous-cutanées d’hydrocortisone sont en évaluation. Efmody® est autorisé dans l’Union européenne pour l’hyperplasie congénitale, pas pour l’Addison ; les thérapies cellulaires restent de la recherche.', 57))
ADD(12, 'Prévention',
 P('La prévention des crises repose sur l’éducation du patient et de ses proches à adapter les doses.', 39, 37) +
 F('Prévention primaire, secondaire et tertiaire',
   TAB(['Niveau', 'Mesure'], [
    ['Primaire', 'Réduire progressivement une corticothérapie prolongée au lieu de l’arrêter'],
    ['Secondaire', 'Chercher l’Addison devant une hyponatrémie inexpliquée ou un vitiligo avec fatigue'],
    ['Tertiaire', 'Carte d’urgence, kit d’hydrocortisone 100 mg, règles de stress'],
   ]) + P('En Suisse, le kit d’urgence est remboursé par l’assurance de base sur prescription ; ce point de l’original est à vérifier.', 16)))
ADD(13, 'Points clés',
 P('La mélanodermie et l’hyperkaliémie signent l’atteinte primaire. '
   'Le test au Synacthène® confirme le diagnostic. '
   'Une crise se traite avant tout test, par hydrocortisone 100 mg IV. '
   'Au-delà de 50 mg/j d’hydrocortisone, la fludrocortisone est inutile.', 37, 58))
ADD(14, 'Pièges d’examen',
 TAB(['Piège', 'Ce qu’il faut répondre'], [
  ['Donner de la dexaméthasone seule', 'Non : elle n’a pas d’effet sur le sel'],
  ['Régler l’hydrocortisone sur l’ACTH', 'Non : surdosage et syndrome de Cushing'],
  ['Attendre le test au Synacthène® en pleine crise', 'Non : traiter d’abord'],
  ['Arrêter brutalement une corticothérapie prolongée', 'Non : risque d’insuffisance corticotrope'],
  ['Appliquer le seuil de 500 nmol/L à tous les dosages', 'Non : vérifier le seuil du laboratoire'],
 ]) + P('Ces pièges reprennent l’Endocrine Society.', 37, 59))
CTX = {'_prefixe': 'Dans la maladie d’Addison',
 'synacthene': 'Un pic sous le seuil du laboratoire confirme l’insuffisance surrénale.',
 'cort': 'Un cortisol du matin < 140 nmol/L avec ACTH haute est très évocateur.',
 'acth': 'Une ACTH > 2 fois la normale signe l’atteinte primaire.',
 'renine': 'Une rénine élevée signe le manque d’aldostérone.',
 'anti21': 'Des anticorps positifs signent la cause auto-immune.',
 'iono': 'Na⁺ bas et K⁺ haut orientent vers le manque d’aldostérone.',
 'gly': 'Une hypoglycémie traduit le manque de cortisol.',
 'tdm': 'Il cherche tuberculose, métastases ou hémorragie si les anticorps sont négatifs.',
 'tsh': 'Une hypothyroïdie associée est fréquente.',
 'tpo': 'Des anticorps positifs évoquent une polyendocrinopathie auto-immune.',
 'igra': 'Il oriente vers une tuberculose surrénalienne.',
 'dxa': 'Elle surveille l’os en cas de surdosage prolongé.'}
if __name__ == '__main__':
    produire(M, PTS, SOURCES, CTX)
