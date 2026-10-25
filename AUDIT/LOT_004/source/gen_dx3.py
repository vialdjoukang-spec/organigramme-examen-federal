# -*- coding: utf-8 -*-
"""DX.3 — Syndrome d'apnées obstructives du sommeil (SAOS). LOT 4, V5 → V7 AUDITÉ."""
from lot4_commun import *
POINT = mkPOINT('dx3')
M = META('dx3', 'DX.3', 'Apnées du sommeil', 'Syndrome d’apnées obstructives du sommeil (SAOS)',
         'LOT_004_DX3_SAOS_AUDITÉ.html',
         'Corrections majeures : le critère « ≥ 4 h sur 70 % des nuits » est une définition classique et une règle de l’assurance publique américaine, non retrouvée dans la LiMA ni les recommandations suisses 2020 ; unité de pression ajoutée (cmH₂O) ; la stimulation du nerf hypoglosse est autorisée depuis 2014 et n’est pas une « recherche 2026 » ; le sémaglutide n’a pas d’essai dédié au SAOS ; seuil d’Epworth « ≥ 16 » pour la conduite retiré (non sourcé).')
MEV = T('micro-éveil', 'Un micro-éveil est un éveil cortical de 3 à 15 secondes, visible à l’électroencéphalogramme, dont le patient ne se souvient pas ; répétés, ils fragmentent le sommeil.')
GEN = T('muscle génioglosse', 'Le génioglosse est le muscle qui tire la langue vers l’avant ; c’est le principal dilatateur du pharynx pendant l’inspiration.')
PTS = []
def ADD(*a): PTS.append(POINT(*a))
ADD(1, 'Définition et sémantique',
 P('Le syndrome d’apnées obstructives du sommeil (SAOS) est la répétition, pendant le sommeil, de fermetures complètes (apnées) ou partielles (hypopnées) du pharynx. '
   'Les efforts respiratoires persistent. Chaque événement provoque une baisse d’oxygène et un ' + MEV + ', ce qui rend le sommeil non réparateur.', 17, 14) +
 F('Terminologie',
   TAB(['Terme', 'Définition exacte (AASM 2012)', 'À ne pas confondre avec'], [
    ['Apnée obstructive', 'Baisse du débit ≥ 90 % pendant ≥ 10 s, avec efforts respiratoires', 'Apnée centrale : sans effort respiratoire'],
    ['Hypopnée', 'Baisse du débit ≥ 30 % pendant ≥ 10 s, avec désaturation ≥ 3 % ou micro-éveil', 'Ronflement simple'],
    ['Indice d’apnées-hypopnées (IAH)', 'Nombre d’apnées et d’hypopnées par heure de sommeil', 'Indice par heure d’enregistrement (polygraphie)'],
    ['Somnolence', 'Tendance à s’endormir en situation passive', 'Fatigue : manque d’énergie sans endormissement'],
    ['Syndrome obésité-hypoventilation', 'Obésité et PaCO₂ diurne > 45 mmHg', 'SAOS isolé'],
   ]) + P('La distinction entre fatigue et somnolence oriente tout le raisonnement : la somnolence fait penser d’abord au sommeil.', 15)))
ADD(2, 'Épidémiologie (Suisse, puis Europe)',
 P('En Suisse, l’étude lausannoise HypnoLaus (2121 adultes de 40 à 85 ans) trouve un IAH ≥ 15/h chez 49,7 % des hommes et 23,4 % des femmes. '
   'Au niveau mondial, environ 425 millions d’adultes de 30 à 69 ans auraient un SAOS modéré à sévère.', 14, 50) +
 F('Chiffres, terrain et histoire naturelle',
   TAB(['Donnée', 'Valeur', 'Portée'], [
    ['IAH ≥ 15/h, hommes 40–85 ans (Lausanne)', '49,7 %', 'Mesure par polysomnographie, critères AASM 2012'],
    ['IAH ≥ 15/h, femmes 40–85 ans (Lausanne)', '23,4 %', 'Même étude'],
    ['SAOS modéré à sévère, monde, 30–69 ans', '≈ 425 millions', 'Estimation de Benjafield (2019), à vérifier'],
    ['Accidents de la route liés à la somnolence', '10–20 %', 'Recommandations suisses sur la conduite'],
    ['« 6–15 % des patients fatigués » (original)', 'Non sourcé', 'Retiré'],
   ]) + P('Le terrain à risque réunit le sexe masculin, l’âge, l’obésité, le tour de cou élevé, la rétrognathie et l’alcool. '
          'Le pronostic dépend de la somnolence (accidents) et du risque cardiovasculaire ; la mortalité propre n’est pas chiffrée dans les sources suisses relues.', 14, 15)))
ADD(3, 'Physiopathologie',
 P('Pendant le sommeil, le tonus du ' + GEN + ' baisse. '
   'Si le pharynx est étroit (graisse, grosses amygdales, mâchoire reculée), la pression négative de l’inspiration le ferme. '
   'Le manque d’oxygène déclenche une décharge du système nerveux sympathique et un micro-éveil qui rouvre le pharynx.', 17) +
 F('Chaîne logique : de l’anatomie au traitement',
   TAB(['Étape', 'Ce qu’il faut comprendre'], [
    ['Anatomie', 'Le pharynx est un tube souple sans squelette, maintenu ouvert par des muscles.'],
    ['Physiologie', 'Pendant le sommeil, le tonus de ces muscles diminue, surtout en sommeil paradoxal.'],
    ['Physiopathologie', 'Un pharynx étroit se ferme ; l’hypoxie et le micro-éveil répétés fragmentent le sommeil et élèvent la pression artérielle.'],
    ['Clinique', 'D’où le ronflement, les pauses vues par le conjoint, la somnolence, la nycturie et l’hypertension.'],
    ['Examens', 'La polygraphie ou la polysomnographie comptent les événements par heure.'],
    ['Traitement', 'La pression positive continue (PPC) agit comme une attelle d’air qui garde le pharynx ouvert.'],
   ]), 17) +
 F('Mécanisme, exploration et cible thérapeutique',
   TAB(['Mécanisme', 'Lésion ou cause', 'Exploration', 'Cible thérapeutique'], [
    ['Pharynx étroit', 'Obésité, amygdales, rétrognathie', 'Examen ORL, IMC, tour de cou', 'Perte de poids, orthèse, chirurgie'],
    ['Tonus musculaire bas', 'Alcool, benzodiazépines, sommeil paradoxal', 'Anamnèse', 'Arrêt des sédatifs'],
    ['Position dorsale', 'La langue recule', 'Polygraphie avec position', 'Thérapie positionnelle'],
    ['Collapsus récurrent', 'SAOS modéré à sévère', 'IAH', 'PPC'],
   ]) + P('Chaque micro-éveil augmente l’activité sympathique ; cela explique l’hypertension matinale et la nycturie, par libération du peptide natriurétique auriculaire.', 17)) +
 F('Calcul de l’IAH', P('IAH = (apnées + hypopnées) / temps total de sommeil (heures).', 17) +
   P('Exemple : 140 apnées et 70 hypopnées en 7 heures de sommeil donnent (140 + 70) / 7 = 30/h, soit un SAOS sévère.', 17)))
ADD(4, 'Raisonnement clinique et diagnostic différentiel',
 P('Le médecin distingue d’abord la somnolence de la fatigue. '
   'Il cherche ensuite une urgence de sécurité : endormissement au volant ou métier à risque. '
   'Puis il évalue la probabilité de SAOS par un questionnaire et choisit l’examen du sommeil.', 15) +
 DIFF('saos') + DIFF_FAT() +
 F('Diagnostics voisins de la somnolence',
   TAB(['Diagnostic', 'Élément distinctif', 'Examen discriminant'], [
    ['SAOS', 'Ronflement, apnées vues, obésité', 'Polygraphie ou polysomnographie'],
    ['Syndrome obésité-hypoventilation', 'IMC ≥ 30 kg/m², hypercapnie diurne', 'Gaz du sang, bicarbonates'],
    ['Apnées centrales', 'Insuffisance cardiaque, opiacés, respiration de Cheyne-Stokes', 'Polysomnographie'],
    ['Narcolepsie', 'Cataplexie, endormissements irrésistibles, sujet jeune', 'Polysomnographie et test itératif de latence d’endormissement'],
    ['Manque de sommeil', 'Moins de 6 h par nuit, rattrapage le week-end', 'Agenda du sommeil'],
    ['Dépression', 'Anhédonie, sommeil non réparateur sans ronflement', 'PHQ-9'],
   ]) + P('Ces diagnostics n’ont pas de fréquence commune publiée chez le patient fatigué.', 15)))
ADD(5, 'Anamnèse ciblée et drapeaux rouges',
 P('L’anamnèse, idéalement avec le conjoint, recherche le ronflement, les pauses respiratoires, les réveils en étouffement, la nycturie et les maux de tête du matin. '
   'Elle précise la somnolence au volant, l’alcool, les sédatifs et le métier.', 15) +
 U('Drapeaux rouges : endormissement ou quasi-accident au volant, chauffeur professionnel ou métier de sécurité, hypercapnie connue, insuffisance cardiaque. Le patient somnolent ne doit plus conduire jusqu’au traitement efficace ; le médecin l’informe par écrit et peut signaler le cas à l’autorité (LCR art. 15d) ; en cas de détresse respiratoire, appeler le 144.', 15, 41) +
 F('Questions ciblées et leur raison',
   TAB(['Question', 'Pourquoi la poser'], [
    ['Ronflez-vous fort ? Votre conjoint a-t-il vu des pauses ?', 'Ce sont les signes les plus évocateurs.'],
    ['Vous endormez-vous en lisant, devant la télévision, au volant ?', 'Mesure la somnolence (échelle d’Epworth).'],
    ['Vous réveillez-vous en étouffant, la bouche sèche ?', 'Réveils liés aux apnées.'],
    ['Combien de fois urinez-vous la nuit ?', 'La nycturie est fréquente dans le SAOS.'],
    ['Buvez-vous de l’alcool le soir ? Prenez-vous des somnifères ?', 'Ils relâchent le pharynx et aggravent les apnées.'],
    ['Quel est votre métier ? Conduisez-vous un camion ou un car ?', 'Le groupe 2 de permis a des exigences plus strictes.'],
   ]), 15, 48))
ADD(6, 'Examen clinique',
 P('L’examen mesure l’IMC, le tour de cou et la pression artérielle. Il inspecte la gorge (amygdales, luette, langue) et la mâchoire.', 48) +
 P('Valeurs normales : IMC 18,5–24,9 kg/m², tour de cou < 40 cm. Le tour de cou > 40 cm fait partie du questionnaire Stop-Bang ; un Stop-Bang ≥ 3 a une sensibilité élevée mais une spécificité faible.', 48) +
 F('Signes, technique et valeur',
   TAB(['Signe', 'Technique', 'Ce qu’il signifie'], [
    ['Tour de cou > 40 cm', 'Mètre ruban sous la pomme d’Adam, debout', 'Risque accru de SAOS'],
    ['IMC ≥ 30 kg/m²', 'Poids / taille²', 'Facteur de risque principal'],
    ['Score de Mallampati III–IV', 'Bouche ouverte, langue tirée, sans phonation', 'Oropharynx encombré'],
    ['Grosses amygdales', 'Inspection avec abaisse-langue', 'Cause fréquente chez l’enfant'],
    ['Rétrognathie', 'Profil du visage', 'Pharynx étroit'],
    ['Hypertension', 'Mesure aux deux bras, au repos', 'Conséquence du SAOS'],
   ]), 48))
ADD(7, 'Syndromes et signes cliniques',
 F('Signes fonctionnels (symptômes rapportés)', UL(['Somnolence diurne', 'Sommeil non réparateur, fatigue au réveil', 'Ronflement, pauses respiratoires', 'Maux de tête du matin', 'Nycturie, troubles de la concentration']), 15) +
 F('Signes physiques (constatés à l’examen)', UL(['Obésité, tour de cou élevé', 'Oropharynx encombré', 'Rétrognathie', 'Hypertension', 'Œdèmes si hypoventilation associée']), 48) +
 P('Le syndrome de fragmentation du sommeil réunit somnolence, fatigue et troubles de l’attention : il vient des micro-éveils. '
   'Le syndrome d’hyperactivité sympathique nocturne réunit hypertension, nycturie et sueurs : il vient des décharges adrénergiques.', 17) +
 F('Syndrome de fragmentation du sommeil', TAB(['Signe', 'Mécanisme', 'Valeur'], [
    ['Somnolence', 'Sommeil morcelé par les micro-éveils', 'Mesurée par l’Epworth'],
    ['Troubles de l’attention', 'Privation de sommeil profond', 'Risque d’accident'],
    ['Irritabilité', 'Privation de sommeil', 'Peu spécifique'],
   ]), 17) +
 F('Syndrome d’hyperactivité sympathique nocturne', TAB(['Signe', 'Mécanisme', 'Valeur'], [
    ['Hypertension résistante', 'Décharges sympathiques répétées', 'Chercher un SAOS'],
    ['Nycturie', 'Peptide natriurétique libéré par la distension des oreillettes', 'Fréquente'],
    ['Fibrillation atriale', 'Hypoxie et variations de pression thoracique', 'Association connue'],
   ]), 17))
ADD(8, 'Critères diagnostiques',
 P('Le diagnostic repose sur un enregistrement du sommeil. Un ronflement ou un questionnaire positif ne suffit pas à poser le diagnostic.', 17, 48) +
 F('Critères (AASM, classification internationale des troubles du sommeil, 3e édition, 2014)',
   TAB(['Critère', 'Seuil'], [
    ['IAH ≥ 15/h', 'Suffit, même sans symptômes'],
    ['IAH 5–14/h', 'Avec somnolence, insomnie, sommeil non réparateur, hypertension, maladie coronarienne, fibrillation atriale ou trouble de l’humeur'],
    ['Sévérité', 'Léger 5–14/h ; modéré 15–29/h ; sévère ≥ 30/h'],
    ['Désaturation d’une hypopnée', '≥ 3 % de SpO₂ (règle recommandée)'],
   ]) + P('Ces critères sont ceux de l’AASM ; les sociétés suisses de pneumologie et de médecine du sommeil les utilisent.', 17, 16)))
ADD(9, 'Examens complémentaires',
 H4('9.a Examen de référence') +
 P('L’examen de référence est la polysomnographie en laboratoire, qui mesure aussi le sommeil. '
   'La polygraphie à domicile a, chez le patient à forte probabilité, une sensibilité et une spécificité suffisantes ; elle sous-estime l’IAH, car elle divise par le temps d’enregistrement.', 17, 16) +
 H4('9.b Examens de première et de deuxième intention') +
 P('En première intention, on fait une polygraphie si la probabilité est élevée et sans comorbidité lourde. En deuxième intention, on fait une polysomnographie si la polygraphie est négative ou si une autre maladie du sommeil est suspectée.', 16) +
 TAB(['Intention', 'Examen', 'Pourquoi'], [
  ['1re', 'Échelle d’Epworth, Stop-Bang', 'Mesurer la somnolence et la probabilité'],
  ['1re', 'Polygraphie respiratoire', 'Compter les événements à domicile'],
  ['2e', 'Polysomnographie', 'Polygraphie négative, comorbidité, autre trouble du sommeil'],
  ['2e', 'Gaz du sang artériels', 'Obésité marquée : chercher une hypoventilation'],
  ['2e', 'Test de maintien de l’éveil', 'Prouver l’aptitude à conduire du groupe 2 sous traitement'],
  ['2e', 'HbA1c, lipides', 'Risque cardiométabolique associé'],
 ]) +
 H4('9.c Prescription et formules') +
 P('Indication : forte suspicion clinique de SAOS. Moment : nuit habituelle, sans changement de traitement. '
   'Préparation : éviter l’alcool et les sédatifs inhabituels ; l’OPAS rembourse l’examen dans les centres reconnus par la SSSSC.', 16) +
 TAB(['Grandeur', 'Formule', 'Repère'], [['IAH', '(apnées + hypopnées) / heures de sommeil', '< 5/h normal'], ['Indice d’événements respiratoires (polygraphie)', '(apnées + hypopnées) / heures d’enregistrement', 'Sous-estime l’IAH']]) +
 H4('9.d Interprétation : positif, négatif, limite, discordant') +
 TAB(['Situation', 'Interprétation', 'Conduite'], [
  ['Positif : IAH ≥ 15/h', 'SAOS modéré à sévère', 'PPC'],
  ['Négatif : IAH < 5/h, faible suspicion', 'SAOS exclu', 'Chercher une autre cause'],
  ['Limite : IAH 5–14/h', 'SAOS léger', 'Traiter si symptômes ou comorbidité'],
  ['Discordant : polygraphie normale, forte suspicion', 'Faux négatif possible', 'Polysomnographie'],
 ]) +
 H4('9.e Alternatives') +
 P('Grossesse : polygraphie possible, PPC sans risque. Enfant : polysomnographie et avis ORL, car les seuils diffèrent (IAH > 1/h). '
   'DFGe bas : aucun produit de contraste n’est utilisé. Iode et IRM ne sont pas nécessaires ; un pacemaker n’empêche pas l’enregistrement.', 17))
ADD(10, 'Arbre décisionnel',
 P('Si le patient est somnolent et ronfle, alors on fait un examen du sommeil. Si l’IAH est ≥ 15/h, alors la PPC est proposée.', 17, 16) +
 F('Arbre décisionnel : fatigue, ronflement, somnolence',
   OL(['Somnolence au volant : arrêt de la conduite, examen rapide.',
       'Epworth > 10 ou Stop-Bang ≥ 3 : polygraphie.',
       'Polygraphie IAH ≥ 15/h : PPC ; 5–14/h avec symptômes : PPC ou orthèse d’avancée mandibulaire.',
       'Polygraphie normale avec forte suspicion : polysomnographie.',
       'Hypercapnie : chercher un syndrome obésité-hypoventilation, ventilation non invasive.',
       'Somnolence persistante sous PPC efficace : chercher une autre cause (narcolepsie, manque de sommeil, dépression).']), 15, 16))
ADD(11, 'Prise en charge',
 H4('11.A Buts : d’abord l’urgence (sécurité routière, hypercapnie), car la somnolence peut tuer au volant') +
 P('Le traitement garde le pharynx ouvert, supprime la somnolence et réduit le risque cardiovasculaire.', 15) +
 TAB(['But', 'Cible chiffrée'], [['IAH résiduel', '< 5–10/h sous traitement'], ['Somnolence', 'Epworth ≤ 10'], ['Observance', '≥ 4 h par nuit sur ≥ 70 % des nuits (définition classique), lue sur l’appareil']]) +
 H4('11.B Moyens et méthodes : forme compliquée en urgence, puis forme non compliquée en ambulatoire') +
 P('La forme compliquée (hypercapnie, insuffisance respiratoire, somnolence grave chez un chauffeur) relève de l’urgence : gaz du sang et ventilation non invasive dans les heures qui suivent, à l’hôpital. '
   'La forme non compliquée se traite en ambulatoire, avec des mesures générales : perte de poids, pas d’alcool le soir, éviter le dos, et une éducation du patient à la PPC.', 15, 16) +
 P('Moyens non médicamenteux : PPC autopilotée (pression habituellement 4–20 cmH₂O), orthèse d’avancée mandibulaire si SAOS léger à modéré ou refus, chirurgie ORL ou maxillo-faciale chez des patients choisis.', 17) +
 FICHE([
  ['Agoniste double GIP/GLP-1 : tirzépatide (Mounjaro®)', 'Agoniste des récepteurs GIP et GLP-1 : satiété, perte de poids', 'Demi-vie ≈ 5 jours ; injection hebdomadaire', '2,5 mg/semaine pendant 4 semaines, puis 5 mg ; paliers de 2,5 mg espacés d’au moins 4 semaines ; max 15 mg', 'Nausées, diarrhée, pancréatite rare', 'Antécédent de cancer médullaire de la thyroïde, grossesse', 'Retarde la vidange gastrique (contraceptifs oraux)'],
 ], 49, 78) +
 P('Dans l’essai SURMOUNT-OSA, le tirzépatide a réduit l’IAH d’environ 50–60 % chez des patients obèses ; le sémaglutide n’a pas d’essai dédié au SAOS. '
   'En Suisse, Mounjaro® est autorisé pour le contrôle du poids si IMC ≥ 30, ou ≥ 27 avec une comorbidité ; le SAOS figure parmi ces comorbidités. '
   'Il n’a pas d’indication pour le SAOS sans surpoids ; le remboursement n’a pas été revérifié.', 49, 78) +
 F('Situations particulières',
   TAB(['Situation', 'Particularité'], [
    ['Grossesse', 'Le SAOS s’aggrave ; PPC sans danger ; pas de tirzépatide'],
    ['Personne âgée', 'Somnolence moins marquée ; chercher troubles cognitifs et chutes'],
    ['Enfant', 'Amygdales et végétations : ablation chirurgicale d’abord'],
    ['Insuffisance hépatique', 'Éviter les sédatifs qui aggravent les apnées'],
    ['Insuffisance rénale (DFGe bas)', 'SAOS fréquent ; prudence avec les sédatifs'],
    ['Insuffisance cardiaque', 'Chercher des apnées centrales avant la ventilation'],
   ]), 17, 25) +
 SOCIAL('Un arrêt de travail se discute pour les métiers de sécurité jusqu’au traitement efficace.',
        'L’OAC exige l’absence de maladie entraînant une somnolence diurne accrue ; une PPC efficace et suivie rétablit l’aptitude. Pour le groupe 2 (camion, car, taxi), un test de maintien de l’éveil est recommandé.') +
 P('La location de la PPC est remboursée par l’assurance de base (liste des moyens et appareils) ; en Suisse romande, la Ligue pulmonaire fournit souvent l’appareil et le suivi. L’original citait « 4 h sur 70 % des nuits » comme règle LAMal. La LiMA (position 14.11) renvoie aux recommandations suisses de 2020 : contrôle à 3 mois puis annuel, sans seuil chiffré retrouvé.', 16, 15, 85) +
 H4('11.C Surveillance et critères de sortie') +
 TAB(['Quand', 'Quoi'], [
  ['Après 1 mois', 'Observance, fuites, IAH résiduel lus sur l’appareil'],
  ['Après 3 mois', 'Epworth, pression artérielle, aptitude à conduire'],
  ['Chaque année', 'Contrôle par le centre ou la Ligue pulmonaire'],
  ['Arrêt de la PPC', 'Possible seulement après perte de poids majeure et nouvel enregistrement normal'],
  ['Critères de sortie (hospitalisation pour hypercapnie)', 'PaCO₂ stabilisée, ventilation réglée, suivi programmé'],
 ]) + P('Le rythme de suivi suit les pratiques des centres suisses ; il n’est pas fixé par la loi.', 15) +
 H4('11.D Pronostic et recherche 2026') +
 P('Le SAOS est une maladie chronique, contrôlée par la PPC tant qu’elle est utilisée ; une rémission est possible après chirurgie bariatrique ou maxillo-faciale.', 17) +
 P('La stimulation du nerf hypoglosse est autorisée depuis 2014 pour les patients choisis qui ne tolèrent pas la PPC. L’association aroxybutynine-atomoxétine (AD109) a terminé sa phase III ; l’agence américaine du médicament (FDA) a accepté la demande d’autorisation en juillet 2026. '
   'La décision américaine est attendue le 28.02.2027 ; le produit n’est autorisé ni en Suisse ni dans l’Union européenne.', 17, 77))
ADD(12, 'Prévention',
 P('La prévention repose sur la lutte contre l’obésité, l’éviction des sédatifs et de l’alcool le soir, et le repérage du SAOS chez les conducteurs somnolents.', 14, 15) +
 F('Prévention primaire, secondaire et tertiaire',
   TAB(['Niveau', 'Mesure'], [
    ['Primaire', 'Poids sain, activité physique, pas d’alcool le soir'],
    ['Secondaire', 'Questionnaire chez le patient fatigué qui ronfle, l’hypertendu résistant, le chauffeur'],
    ['Tertiaire', 'PPC suivie, aptitude à la conduite réévaluée, risque cardiovasculaire traité'],
   ]) + P('En Suisse, les recommandations de la SSSSC sur la conduite et l’OPAS encadrent ce repérage.', 15, 16)))
ADD(13, 'Points clés',
 P('La somnolence n’est pas la fatigue : elle oriente vers un trouble du sommeil. '
   'Un IAH ≥ 15/h définit un SAOS modéré à sévère. '
   'Une polygraphie normale n’exclut pas un SAOS si la suspicion est forte. '
   'Le patient somnolent ne doit pas conduire jusqu’au traitement efficace.', 17, 15))
ADD(14, 'Pièges d’examen',
 TAB(['Piège', 'Ce qu’il faut répondre'], [
  ['Prescrire une benzodiazépine pour des réveils nocturnes', 'Non : elle relâche le pharynx et allonge les apnées'],
  ['Exclure un SAOS sur une polygraphie normale', 'Non : faire une polysomnographie si la suspicion reste forte'],
  ['Croire que la LAMal exige 4 h sur 70 % des nuits', 'Seuil classique et américain ; non retrouvé dans la LiMA ni les recommandations suisses 2020 (à vérifier)'],
  ['Oublier la conduite', 'Il faut informer le patient et documenter l’information'],
  ['Mettre une PPC à un patient insuffisant cardiaque avec apnées centrales', 'Il faut d’abord caractériser les apnées par polysomnographie'],
  ['Oublier l’unité de la pression', 'La PPC se règle en cmH₂O'],
 ]) + P('Ces pièges reprennent les erreurs de l’original et les recommandations suisses.', 15, 16))
CTX = {'_prefixe': 'Dans le SAOS',
 'psg': 'Un IAH ≥ 15/h confirme un SAOS modéré à sévère et justifie la PPC.',
 'quest': 'Un Epworth > 10 ou un Stop-Bang ≥ 3 justifie un enregistrement du sommeil.',
 'gds': 'Une PaCO₂ > 45 mmHg de jour évoque un syndrome obésité-hypoventilation.',
 'hba1c': 'Une HbA1c élevée signale un diabète, fréquent avec le SAOS.',
 'ecg': 'Une fibrillation atriale est plus fréquente en cas de SAOS sévère.',
 'echocoeur': 'Elle cherche une insuffisance cardiaque devant des apnées centrales.',
 'tsh': 'Une hypothyroïdie peut aggraver les apnées et la fatigue.',
 'nfs': 'Une polyglobulie peut traduire une hypoxie chronique.'}
if __name__ == '__main__':
    produire(M, PTS, SOURCES, CTX)
