# -*- coding: utf-8 -*-
"""DX.2 — Épisode dépressif et burn-out (épuisement professionnel). LOT 4, V5 → V7 AUDITÉ."""
from lot4_commun import *
POINT = mkPOINT('dx2')
M = META('dx2', 'DX.2', 'Dépression et burn-out', 'Épisode dépressif et épuisement professionnel (burn-out)',
         'LOT_004_DX2_Depression_burn_out_AUDITÉ.html',
         'Corrections majeures : prévalence suisse remplacée par l’indicateur Obsan 2022 (9,8 %) ; « 25 % de burn-out » remplacé par les données MonAM et Job Stress Index ; le burn-out est un phénomène lié au travail dans la CIM-11, pas une maladie ; « antidépresseurs obligatoires » corrigé ; PLAFA développé.')
ANH = T('anhédonie', 'L’anhédonie est la perte du plaisir et de l’intérêt pour des activités autrefois agréables ; c’est l’un des deux symptômes centraux de la dépression.')
HHS = T('axe corticotrope', 'L’axe corticotrope relie l’hypothalamus (CRH), l’hypophyse (ACTH) et les surrénales (cortisol) ; il règle la réponse au stress.')
PTS = []
def ADD(*a): PTS.append(POINT(*a))
ADD(1, 'Définition et sémantique',
 P('L’épisode dépressif est un trouble de l’humeur : humeur triste ou ' + ANH + ' presque tous les jours pendant au moins 2 semaines, avec d’autres symptômes et une gêne dans la vie quotidienne. '
   'Le burn-out (épuisement professionnel) est un état d’épuisement lié à un stress chronique au travail mal géré.', 44, 45) +
 F('Terminologie',
   TAB(['Terme', 'Définition exacte', 'À ne pas confondre avec'], [
    ['Épisode dépressif (CIM-10 F32, CIM-11 6A70)', 'Humeur dépressive ou anhédonie ≥ 2 semaines avec symptômes associés', 'Tristesse réactionnelle, deuil'],
    ['Trouble dépressif récurrent', 'Au moins deux épisodes séparés par une rémission', 'Dysthymie (humeur basse chronique ≥ 2 ans)'],
    ['Burn-out (CIM-11 QD85)', 'Épuisement, distance mentale vis-à-vis du travail, efficacité réduite ; lié exclusivement au travail', 'Dépression : touche tous les domaines de la vie'],
    ['Épisode dépressif du trouble bipolaire', 'Dépression chez une personne qui a eu un épisode maniaque ou hypomaniaque', 'Dépression unipolaire'],
    ['Fatigue', 'Manque d’énergie physique ou mentale', 'Anhédonie : manque de plaisir'],
   ]) + P('Dans la CIM-11, le burn-out figure parmi les facteurs influençant l’état de santé : l’OMS le décrit comme un phénomène lié au travail, non comme une maladie.', 45)))
ADD(2, 'Épidémiologie (Suisse, puis Europe)',
 P('En Suisse, 9,8 % des personnes de 15 ans et plus avaient des symptômes dépressifs modérés à graves en 2022 (femmes 11,7 %, hommes 7,9 %). '
   'Chez les actifs occupés, 30,3 % présentent un épuisement émotionnel selon l’indicateur MonAM. '
   'Dans une revue internationale de premier recours, la dépression explique 18,5 % des consultations pour fatigue.', 6, 7, 2) +
 F('Chiffres, terrain et histoire naturelle',
   TAB(['Donnée', 'Valeur', 'Portée'], [
    ['Symptômes dépressifs modérés à graves (PHQ-9 ≥ 10), ≥ 15 ans', '9,8 % (2022)', 'Enquête suisse sur la santé, Obsan'],
    ['Femmes / hommes', '11,7 % / 7,9 %', 'Même enquête'],
    ['Épuisement émotionnel, actifs occupés 16–65 ans', '30,3 %', 'MonAM, Job Stress Index 2022'],
    ['Actifs en zone critique de stress', '28,2 %', 'Job Stress Index 2022 ; coût estimé ≈ CHF 6,5 milliards par an'],
    ['Dépression chez les patients qui consultent pour fatigue', '18,5 %', 'Revue de premier recours'],
    ['« 25 % de burn-out » (original)', 'Non sourcé', 'Remplacé par les deux indicateurs ci-dessus'],
   ]) + P('Le terrain à risque réunit le sexe féminin, les antécédents personnels ou familiaux, l’isolement, la maladie chronique et le stress au travail. '
          'Environ la moitié des personnes font une récidive après un premier épisode ; le risque de suicide est le pronostic vital à évaluer.', 6, 8, 2, 44)))
ADD(3, 'Physiopathologie',
 P('La dépression naît d’une rencontre entre une vulnérabilité (gènes, histoire de vie) et des stress. '
   'Le stress prolongé active l’' + HHS + ' et dérègle les circuits de la récompense et des émotions. '
   'L’hypothèse des monoamines (sérotonine, noradrénaline, dopamine) explique l’action des antidépresseurs, mais pas toute la maladie.', 44) +
 F('Chaîne logique : de l’anatomie au traitement',
   TAB(['Étape', 'Ce qu’il faut comprendre'], [
    ['Anatomie', 'Cortex préfrontal, hippocampe, amygdale et noyau accumbens forment le réseau des émotions et de la récompense.'],
    ['Physiologie', 'Les monoamines modulent ce réseau ; le cortisol aide à faire face au stress à court terme.'],
    ['Physiopathologie', 'Un stress chronique maintient un cortisol élevé, diminue la plasticité de l’hippocampe et entretient une inflammation de bas grade.'],
    ['Clinique', 'D’où la tristesse, l’anhédonie, la fatigue, les troubles du sommeil et de la concentration.'],
    ['Examens', 'Le diagnostic est clinique ; la biologie sert à exclure une cause organique de fatigue.'],
    ['Traitement', 'La psychothérapie modifie les schémas de pensée ; les antidépresseurs agissent sur les monoamines et la plasticité.'],
   ]), 44) +
 F('Mécanisme, exploration et cible thérapeutique',
   TAB(['Mécanisme', 'Expression', 'Exploration', 'Cible'], [
    ['Déficit de la récompense', 'Anhédonie', 'Entretien, PHQ-9', 'Activation comportementale, antidépresseur'],
    ['Stress chronique', 'Épuisement, insomnie', 'Anamnèse professionnelle', 'Réduction des contraintes, arrêt de travail ciblé'],
    ['Distorsions cognitives', 'Culpabilité, pessimisme', 'Entretien', 'Thérapie cognitivo-comportementale (TCC)'],
    ['Cause organique', 'Fatigue, ralentissement', 'TSH, hémogramme, glycémie', 'Traiter la cause'],
   ]) + P('L’original parlait d’un « déficit structurel en sérotonine » : c’est une simplification, car le taux de sérotonine n’est pas mesurable chez le patient.', 44)) +
 F('Score PHQ-9 : calcul', P('Le PHQ-9 compte 9 items cotés de 0 (jamais) à 3 (presque tous les jours) sur les 2 dernières semaines ; le total va de 0 à 27.', 43) +
   TAB(['Score', 'Sévérité', 'Conduite'], [['0–4', 'Minime', 'Surveillance'], ['5–9', 'Légère', 'Soutien, réévaluation'], ['10–14', 'Modérée', 'Psychothérapie et/ou antidépresseur'], ['15–19', 'Modérément sévère', 'Antidépresseur et psychothérapie'], ['20–27', 'Sévère', 'Traitement combiné, avis psychiatrique']]) +
   P('Exemple : humeur 3 + anhédonie 3 + sommeil 2 + fatigue 3 + concentration 1 = 12, soit une dépression modérée. L’item 9 (idées de mort) doit toujours être lu à part.', 43)))
ADD(4, 'Raisonnement clinique et diagnostic différentiel',
 P('Devant une fatigue avec tristesse, le médecin évalue d’abord le risque suicidaire. '
   'Il cherche ensuite des antécédents d’épisode maniaque, car le traitement d’une dépression bipolaire est différent. '
   'Enfin, il exclut une cause organique : hypothyroïdie, anémie, apnées du sommeil, médicaments, alcool.', 44) +
 DIFF('dep') + DIFF_FAT() +
 F('Dépression, burn-out et diagnostics voisins',
   TAB(['Diagnostic', 'Élément distinctif', 'Examen discriminant'], [
    ['Épisode dépressif', 'Anhédonie dans tous les domaines de la vie', 'Entretien selon la CIM, PHQ-9'],
    ['Burn-out', 'Épuisement centré sur le travail ; plaisir conservé en vacances au début', 'Anamnèse professionnelle, inventaire de Maslach (MBI)'],
    ['Dépression bipolaire', 'Antécédent d’hypomanie, début précoce, antécédents familiaux', 'Entretien, questionnaire d’hypomanie'],
    ['Trouble anxieux', 'Inquiétude, tension, crises d’angoisse', 'HADS, entretien'],
    ['Hypothyroïdie', 'Frilosité, prise de poids, constipation', 'TSH'],
    ['Apnées du sommeil', 'Ronflement, somnolence diurne', 'Questionnaire Stop-Bang, polygraphie'],
   ]) + P('Le burn-out et la dépression se recouvrent souvent ; si les critères d’un épisode dépressif sont remplis, c’est ce diagnostic qui guide le traitement.', 44, 45)))
ADD(5, 'Anamnèse ciblée et drapeaux rouges',
 P('L’anamnèse explore l’humeur, le plaisir, le sommeil, l’appétit, l’énergie, la concentration et les idées de mort. '
   'Elle recherche les antécédents personnels et familiaux, les épisodes d’excitation, l’alcool, les drogues et les médicaments. '
   'Elle décrit le travail : charge, soutien, reconnaissance, conflits.', 44) +
 U('Drapeaux rouges : idées suicidaires avec plan ou moyens, absence de facteurs protecteurs, idées délirantes (ruine, culpabilité), refus de boire ou de manger, agitation grave. Ils imposent une évaluation psychiatrique en urgence (144 si danger immédiat) ; un placement à des fins d’assistance (PLAFA) est possible si le danger est grave et que la personne refuse les soins (CC art. 426).', 44, 71) +
 F('Questions ciblées et leur raison',
   TAB(['Question', 'Pourquoi la poser'], [
    ['Avez-vous perdu le plaisir pour ce que vous aimiez ?', 'Repère l’anhédonie, symptôme central.'],
    ['Avez-vous pensé que la vie ne valait pas la peine, ou à vous faire du mal ?', 'Évalue le risque suicidaire ; poser la question ne l’augmente pas.'],
    ['Avez-vous eu des périodes d’énergie excessive, avec peu de sommeil ?', 'Recherche une bipolarité.'],
    ['Combien d’alcool buvez-vous par semaine ?', 'L’alcool aggrave et imite la dépression.'],
    ['Votre fatigue disparaît-elle pendant les vacances ?', 'Oriente vers un burn-out plutôt qu’une dépression installée.'],
    ['Qui vous soutient ?', 'Les facteurs protecteurs comptent dans l’évaluation du risque.'],
   ]), 44))
ADD(6, 'Examen clinique',
 P('L’examen observe la présentation, le visage, le débit de parole et la rapidité des gestes. '
   'Il comprend un examen somatique complet, y compris thyroïde et neurologie, pour ne pas manquer une cause organique.', 44) +
 P('Valeurs normales : contact visuel, mimique mobile, parole fluide. Aucun signe d’examen n’a de sensibilité ni de spécificité suffisantes pour poser seul le diagnostic de dépression.', 44) +
 F('Signes, technique et valeur',
   TAB(['Signe', 'Technique', 'Ce qu’il signifie'], [
    ['Ralentissement psychomoteur', 'Observer la marche, les gestes, le temps de réponse', 'Dépression sévère, forme mélancolique'],
    ['Hypomimie, regard évité', 'Observer le visage pendant l’entretien', 'Tristesse, ralentissement'],
    ['Bradyphémie (parole lente)', 'Écouter le débit et les pauses', 'Ralentissement de la pensée'],
    ['Goitre, peau sèche, réflexes lents', 'Palpation du cou, réflexes achilléens', 'Hypothyroïdie'],
    ['Signe neurologique focal', 'Examen neurologique', 'Lésion cérébrale : imagerie'],
   ]), 44))
ADD(7, 'Syndromes et signes cliniques',
 F('Signes fonctionnels (symptômes rapportés)', UL(['Tristesse, perte de plaisir', 'Fatigue, manque d’énergie', 'Insomnie ou hypersomnie', 'Troubles de la concentration', 'Culpabilité, idées de mort']), 44) +
 F('Signes physiques (constatés à l’examen)', UL(['Ralentissement psychomoteur ou agitation', 'Hypomimie', 'Perte ou prise de poids', 'Parole lente', 'Négligence de soi']), 44) +
 P('Le syndrome dépressif réunit l’humeur triste, l’anhédonie et les signes somatiques ; il touche tous les domaines de la vie. '
   'Le syndrome d’épuisement professionnel réunit l’épuisement, la distance mentale vis-à-vis du travail et la baisse d’efficacité ; il reste lié au travail.', 44, 45) +
 F('Syndrome dépressif', TAB(['Signe', 'Mécanisme', 'Valeur'], [
    ['Anhédonie', 'Circuit de la récompense', 'Symptôme central'],
    ['Réveil précoce', 'Dérèglement du rythme circadien', 'Évoque la forme mélancolique'],
    ['Idées de culpabilité', 'Biais cognitifs négatifs', 'Sévérité ; délire si conviction'],
   ]), 44) +
 F('Syndrome d’épuisement professionnel', TAB(['Signe', 'Mécanisme', 'Valeur'], [
    ['Épuisement émotionnel', 'Ressources dépassées par les exigences', 'Mesuré par le MBI'],
    ['Cynisme, distance mentale', 'Protection contre la surcharge', 'Spécifique du burn-out'],
    ['Efficacité réduite', 'Perte de sens et de contrôle', 'Moins discriminant'],
   ]), 45))
ADD(8, 'Critères diagnostiques',
 P('Le diagnostic d’épisode dépressif repose sur l’entretien. Un score de questionnaire ne suffit pas : il dépiste et mesure la sévérité, mais ne remplace pas l’examen clinique.', 44, 43) +
 F('Critères CIM-10 de l’épisode dépressif (codage encore utilisé en Suisse)',
   TAB(['Élément', 'Exigence'], [
    ['Durée', 'Au moins 2 semaines'],
    ['Symptômes principaux', 'Humeur dépressive, perte d’intérêt ou de plaisir, baisse d’énergie'],
    ['Symptômes associés', 'Concentration, estime de soi, culpabilité, pessimisme, idées suicidaires, sommeil, appétit'],
    ['Léger', '2 principaux + 2 associés'],
    ['Moyen', '2 principaux + 3–4 associés'],
    ['Sévère', '3 principaux + ≥ 4 associés'],
   ]) + P('Critère de dépistage (recommandation SSAD 2016) : au seuil de 10, le PHQ-9 a une sensibilité et une spécificité de 88 %. '
   'L’original exigeait « au moins 2 symptômes cardinaux » sans préciser le nombre de symptômes associés : la sévérité dépend du total.', 44, 43)) +
 F('Critères CIM-11 du burn-out (QD85)', UL(['Sentiment d’épuisement ou de manque d’énergie', 'Distance mentale accrue, négativisme ou cynisme envers le travail', 'Efficacité professionnelle réduite', 'Uniquement dans le contexte du travail']), 45))
ADD(9, 'Examens complémentaires',
 H4('9.a Examen de référence') +
 P('La référence est l’entretien clinique structuré (par exemple le MINI). '
   'Le PHQ-9 a une sensibilité et une spécificité d’environ 88 % au seuil de 10 dans l’étude de validation ; ce sont des valeurs de dépistage, pas de diagnostic.', 43, 44) +
 H4('9.b Examens de première et de deuxième intention') +
 P('En première intention, on fait un bilan simple pour exclure une cause somatique. En deuxième intention, l’imagerie cérébrale n’est utile que si la présentation est atypique.', 44) +
 TAB(['Intention', 'Examen', 'Pourquoi'], [
  ['1re', 'Questionnaires PHQ-9 ou HADS', 'Mesurer la sévérité et suivre l’évolution'],
  ['1re', 'TSH', 'Hypothyroïdie'],
  ['1re', 'Hémogramme, ferritine', 'Anémie, carence en fer'],
  ['1re', 'Glycémie, créatinine, électrolytes, calcium', 'Causes métaboliques, bilan avant traitement'],
  ['2e', 'Vitamine B12', 'Carence chez le sujet âgé ou végétarien'],
  ['2e', 'IRM cérébrale', 'Début après 50–60 ans, signe neurologique, déclin cognitif'],
  ['2e', 'ECG', 'Avant un antidépresseur qui allonge le QT (citalopram, escitalopram)'],
 ]) +
 H4('9.c Prescription et formules') +
 P('Indication : fatigue avec tristesse ou perte de plaisir, au premier recours. Moment : au diagnostic, puis toutes les 2–4 semaines pour suivre l’effet. '
   'Préparation : aucune ; le questionnaire se remplit seul, en 5 minutes.', 43) +
 TAB(['Grandeur', 'Formule', 'Repère'], [['PHQ-9', 'Somme des 9 items (0–3)', '0–27 ; réponse si baisse ≥ 50 %'], ['Rémission', 'PHQ-9 < 5', 'Objectif du traitement']]) +
 H4('9.d Interprétation : positif, négatif, limite, discordant') +
 TAB(['Situation', 'Interprétation', 'Conduite'], [
  ['Positif : PHQ-9 ≥ 10', 'Dépression probable', 'Entretien diagnostique'],
  ['Négatif : PHQ-9 < 5', 'Dépression peu probable', 'Chercher une autre cause de fatigue'],
  ['Limite : PHQ-9 5–9', 'Symptômes légers', 'Réévaluer en 2–4 semaines'],
  ['Discordant : score bas mais item 9 positif', 'Risque suicidaire', 'Évaluation immédiate du risque'],
 ]) +
 H4('9.e Alternatives') +
 P('Grossesse et post-partum : échelle d’Édimbourg. Enfant et adolescent : versions adaptées et avis pédopsychiatrique. '
   'Personne âgée : échelle de dépression gériatrique. Le DFGe guide le choix et la dose de certains antidépresseurs ; aucun examen avec iode ni IRM n’est nécessaire en routine.', 44))
ADD(10, 'Arbre décisionnel',
 P('Si les idées suicidaires sont graves, alors l’évaluation psychiatrique est urgente. Si le risque est faible, le traitement dépend de la sévérité.', 44, 46) +
 F('Arbre décisionnel : fatigue avec humeur triste',
   OL(['Dépister : PHQ-2 puis PHQ-9 si positif.',
       'Évaluer le risque suicidaire : plan, moyens, facteurs protecteurs.',
       'Risque élevé : urgence psychiatrique, hospitalisation, PLAFA si refus et danger grave.',
       'Chercher une bipolarité : si présente, pas d’antidépresseur seul, avis psychiatrique.',
       'Exclure une cause organique : TSH, hémogramme, ferritine, glycémie.',
       'Forme légère : soutien, activation, psychothérapie ; réévaluer en 2–4 semaines.',
       'Forme modérée à sévère : psychothérapie et antidépresseur ; réévaluer à 2–4 semaines puis à 6–8 semaines.']), 44, 46))
ADD(11, 'Prise en charge',
 H4('11.A Buts : d’abord l’urgence (risque suicidaire), car il peut tuer en quelques heures') +
 P('Les buts sont la sécurité, puis la rémission, puis la prévention des rechutes et le retour au travail.', 44) +
 TAB(['But', 'Cible chiffrée'], [['Réponse', 'Baisse du PHQ-9 d’au moins 50 %'], ['Rémission', 'PHQ-9 < 5'], ['Maintien', 'Traitement poursuivi au moins 6 mois après la rémission']]) +
 H4('11.B Moyens et méthodes : forme compliquée en urgence, puis forme non compliquée en ambulatoire') +
 P('La forme compliquée (risque suicidaire élevé, délire, refus de s’alimenter) relève de l’hôpital psychiatrique. '
   'La forme non compliquée se traite en ambulatoire, avec des mesures générales : sommeil régulier, activité physique, réduction de l’alcool, et une éducation du patient sur le délai d’action.', 44, 46) +
 P('La psychothérapie (TCC, thérapie interpersonnelle) est efficace dans les formes légères à modérées. Pour le burn-out, on adapte la charge de travail et on prépare un retour progressif.', 44, 46) +
 FICHE([
  ['ISRS : sertraline (Zoloft®), escitalopram (Cipralex®)', 'Bloque la recapture de la sérotonine', 'Demi-vie ≈ 1 jour ; état d’équilibre en 1 semaine', 'Sertraline 50 mg/j (max 200) ; escitalopram 10 mg/j (max 20)', 'Nausées, troubles sexuels, hyponatrémie, saignements', 'IMAO, allongement du QT (escitalopram)', 'Anticoagulants, AINS, tramadol, triptans (syndrome sérotoninergique)'],
  ['IRSN : venlafaxine (Efexor®), duloxétine (Cymbalta®)', 'Bloque la recapture de la sérotonine et de la noradrénaline', 'Métabolisme hépatique', 'Venlafaxine 75 mg/j ; duloxétine 60 mg/j', 'Hausse de la pression, sueurs, syndrome d’arrêt', 'Hypertension non contrôlée, insuffisance hépatique (duloxétine)', 'IMAO, autres sérotoninergiques'],
  ['Antidépresseur noradrénergique et sérotoninergique : mirtazapine (Remeron®)', 'Bloque les récepteurs α2 et H1', 'Sédatif à faible dose', '15–45 mg le soir', 'Somnolence, prise de poids', 'Prudence si conduite', 'Alcool, sédatifs'],
 ], 44) +
 P('Le choix tient compte des effets indésirables, des comorbidités et des préférences ; l’original déclarait les antidépresseurs « obligatoires » dans la forme sévère, alors qu’ils y sont recommandés.', 44, 46) +
 F('Situations particulières',
   TAB(['Situation', 'Particularité'], [
    ['Grossesse et allaitement', 'Sertraline souvent préférée ; décision partagée avec gynécologue et psychiatre'],
    ['Personne âgée', 'Doses réduites, hyponatrémie et chutes à surveiller ; éviter les tricycliques'],
    ['Enfant et adolescent', 'Psychothérapie d’abord ; fluoxétine si antidépresseur ; risque suicidaire accru au début'],
    ['Insuffisance hépatique', 'Doses réduites ; éviter la duloxétine'],
    ['Insuffisance rénale (DFGe bas)', 'Adapter la venlafaxine ; sertraline peu modifiée'],
    ['Trouble bipolaire', 'Pas d’antidépresseur seul : thymorégulateur, avis psychiatrique'],
   ]), 44, 40) +
 SOCIAL('Un arrêt de travail partiel ou complet, limité et réévalué toutes les 2–4 semaines, aide en cas d’épuisement ; un arrêt long sans plan de reprise augmente le risque de désinsertion.',
        'Les antidépresseurs sédatifs et l’insomnie peuvent réduire l’aptitude à conduire (LCR art. 31) ; le patient doit s’abstenir s’il se sent somnolent.') +
 H4('11.C Surveillance et critères de sortie') +
 TAB(['Quand', 'Quoi'], [
  ['Après 1–2 semaines', 'Tolérance, risque suicidaire (levée d’inhibition possible au début)'],
  ['Après 2–4 semaines', 'Premier effet attendu ; sinon vérifier dose et observance'],
  ['Après 6–8 semaines', 'Effet complet : changer de stratégie si réponse insuffisante'],
  ['Chaque mois', 'PHQ-9 et capacité de travail'],
  ['Arrêt du traitement', 'Au moins 6 mois après la rémission, diminution progressive sur plusieurs semaines'],
  ['Critères de sortie d’hospitalisation', 'Risque suicidaire réduit, plan de suivi, entourage informé'],
 ]) + P('Chez la personne âgée, la natrémie se contrôle après le début d’un ISRS, car l’hyponatrémie par sécrétion inappropriée d’hormone antidiurétique est plus fréquente.', 44, 40) +
 H4('11.D Pronostic et recherche 2026') +
 P('Environ la moitié des patients rechutent après un premier épisode ; le risque augmente avec le nombre d’épisodes. Le burn-out a un pronostic favorable si la situation de travail change.', 44) +
 P('L’eskétamine intranasale (Spravato®) est autorisée par Swissmedic pour la dépression résistante, sous surveillance. La psilocybine à forte dose reste en recherche ; le micro-dosage, cité par l’original, n’a pas montré d’efficacité.', 72, 44))
ADD(12, 'Prévention',
 P('La prévention combine la réduction du stress au travail, le repérage précoce et l’éducation du patient et de ses proches aux signes de rechute.', 8, 44) +
 F('Prévention primaire, secondaire et tertiaire',
   TAB(['Niveau', 'Mesure'], [
    ['Primaire', 'Gestion de la santé en entreprise, soutien social, activité physique'],
    ['Secondaire', 'Repérage par PHQ-2 chez le patient fatigué ou à risque'],
    ['Tertiaire', 'Traitement de maintien, retour au travail progressif, prévention du suicide'],
   ]) + P('En Suisse, Promotion Santé Suisse soutient la gestion de la santé en entreprise ; la ligne 143 (La Main Tendue) offre une écoute en cas de crise.', 8)))
ADD(13, 'Points clés',
 P('Le risque suicidaire s’évalue d’abord, à chaque consultation. '
   'Une bipolarité doit être cherchée avant tout antidépresseur. '
   'Le burn-out est un phénomène lié au travail ; si les critères de dépression sont remplis, la dépression guide le traitement. '
   'Un antidépresseur agit en 2–4 semaines et se poursuit au moins 6 mois après la rémission.', 44, 45))
ADD(14, 'Pièges d’examen',
 TAB(['Piège', 'Ce qu’il faut répondre'], [
  ['Donner un antidépresseur seul à un patient bipolaire', 'Non : risque de virage maniaque ; thymorégulateur et avis psychiatrique'],
  ['Ne pas demander les idées suicidaires de peur de les susciter', 'Il faut les demander : la question ne les augmente pas'],
  ['Coder le burn-out comme une maladie de la CIM-11', 'Non : c’est un phénomène lié au travail (QD85)'],
  ['Arrêter l’antidépresseur dès l’amélioration', 'Non : au moins 6 mois après la rémission'],
  ['Conclure à une dépression sans TSH ni hémogramme', 'Il faut exclure une cause organique de fatigue'],
  ['Juger l’inefficacité après 1 semaine', 'Il faut attendre 2–4 semaines pour un premier effet'],
 ]) + P('Ces pièges reprennent les recommandations suisses de la SSAD.', 44))
CTX = {'_prefixe': 'Dans la dépression et le burn-out',
 'quest': 'Un PHQ-9 ≥ 10 rend une dépression probable ; l’item 9 se lit toujours à part.',
 'tsh': 'Une TSH élevée oriente vers une hypothyroïdie qui imite la dépression.',
 'nfs': 'Une anémie peut expliquer la fatigue sans dépression.',
 'ferritine': 'Une ferritine < 15 µg/L explique une fatigue à traiter en parallèle.',
 'b12': 'Une carence en B12 peut donner humeur basse et troubles cognitifs.',
 'iono': 'Une hyponatrémie apparaît parfois sous ISRS chez la personne âgée.',
 'irm': 'L’IRM cérébrale ne sert que si la présentation est atypique ou neurologique.',
 'ecg': 'Un QT long contre-indique le citalopram et l’escitalopram à forte dose.',
 'gly': 'Une hyperglycémie peut aggraver la fatigue et l’humeur.',
 'creat': 'Le DFGe guide la dose de certains antidépresseurs.'}
if __name__ == '__main__':
    produire(M, PTS, SOURCES, CTX)
