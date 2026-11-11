# -*- coding: utf-8 -*-
"""DX.9 — Encéphalomyélite myalgique / syndrome de fatigue chronique et POTS. LOT 4, V5 → V7 AUDITÉ."""
from lot4_commun import *
POINT = mkPOINT('dx9')
M = META('dx9', 'DX.9', 'EM/SFC et POTS', 'Encéphalomyélite myalgique / syndrome de fatigue chronique (EM/SFC) et tachycardie orthostatique posturale',
         'LOT_004_DX9_EM_SFC_POTS_AUDITÉ.html',
         'Corrections majeures : le malaise post-effort est un critère cardinal, pas un signe pathognomonique ; prévalence 0,68 % (méta-analyse de Lim) au lieu de « 0,3–0,8 % selon l’OFSP » non sourcé ; mécanismes présentés comme hypothèses ; critères IOM 2015 et NICE 2021 distingués ; critère « FC debout ≥ 120 » retiré (HRS 2015) ; sel 10–12 g/j et eau 2–3 L/j selon HRS ; aucune recommandation suisse propre retrouvée.')
MPE = T('malaise post-effort', 'Le malaise post-effort est une aggravation de tous les symptômes, retardée de 12 à 48 h, après un effort même minime ; elle dure des jours ou des semaines.')
POTS = T('tachycardie orthostatique posturale (POTS)', 'Le POTS (postural orthostatic tachycardia syndrome) est une accélération excessive du cœur en position debout, sans chute de pression, avec des symptômes chroniques.')
PTS = []
def ADD(*a): PTS.append(POINT(*a))
ADD(1, 'Définition et sémantique',
 P('L’EM/SFC est une maladie chronique invalidante : une baisse importante des activités depuis plus de 6 mois, une fatigue non soulagée par le repos et un ' + MPE + '. '
   'Le malaise post-effort est le critère central ; il n’est pas pathognomonique, contrairement à l’original.', 34, 33) +
 F('Terminologie',
   TAB(['Terme', 'Définition exacte', 'À ne pas confondre avec'], [
    ['EM/SFC', 'Maladie définie par les critères IOM 2015 ou NICE 2021', 'Fatigue chronique banale'],
    ['Malaise post-effort', 'Aggravation retardée et prolongée après un effort', 'Courbatures normales'],
    ['POTS', 'Fréquence cardiaque + 30/min debout sans hypotension, symptômes chroniques', 'Hypotension orthostatique'],
    ['Pacing', 'Gestion de l’énergie sous le seuil de déclenchement', 'Exercice gradué'],
    ['Syndrome post-COVID', 'Symptômes > 3 mois après une COVID-19', 'EM/SFC (il peut en remplir les critères)'],
   ]) + P('L’OMS classe l’EM/SFC parmi les maladies du système nerveux (CIM-10 G93.3).', 34)))
ADD(2, 'Épidémiologie (Suisse, puis Europe)',
 P('En Suisse, aucune prévalence nationale publiée n’a été retrouvée ; le chiffre « 0,3–0,8 % selon l’OFSP » de l’original n’est pas sourcé. '
   'Une méta-analyse internationale estime la prévalence à 0,68 % (0,89 % avec les critères CDC 1994).', 35) +
 F('Chiffres, terrain et histoire naturelle',
   TAB(['Donnée', 'Valeur', 'Portée'], [
    ['Prévalence, méta-analyse', '0,68 %', 'Lim 2020'],
    ['Avec les critères CDC 1994', '0,89 %', 'Lim 2020'],
    ['SFC chez les patients fatigués en premier recours', '< 2 %', 'Revue de Stadje'],
    ['Sexe', 'Plus fréquent chez la femme', 'IOM 2015'],
    ['Âge', 'Adulte jeune et d’âge moyen', 'IOM 2015'],
   ]) + P('Le terrain associe souvent une infection déclenchante. '
          'Le pronostic est fluctuant ; la guérison complète est rare chez l’adulte, mais une amélioration fonctionnelle est fréquente.', 34, 2)))
ADD(3, 'Physiopathologie',
 P('La cause reste inconnue. La maladie suit souvent une infection virale (virus d’Epstein-Barr, SARS-CoV-2). '
   'Des hypothèses impliquent un trouble de la régulation immunitaire, du système nerveux autonome et du métabolisme énergétique du muscle. Le dérèglement autonome provoque la tachycardie debout ; le défaut énergétique expliquerait le malaise post-effort.', 34) +
 F('Chaîne logique : de l’anatomie au traitement',
   TAB(['Étape', 'Ce qu’il faut comprendre'], [
    ['Anatomie', 'Le système nerveux autonome règle le pouls et le tonus des veines, ce qui explique son rôle debout.'],
    ['Physiologie', 'Debout, le sang descend dans les jambes, ce qui entraîne un resserrement des veines.'],
    ['Physiopathologie', 'Le dérèglement autonome, l’inflammation et l’énergie altérée provoqueraient les symptômes (hypothèses).'],
    ['Clinique', 'Cela explique le malaise post-effort, le brouillard mental et l’intolérance debout.'],
    ['Examens', 'Aucun biomarqueur ; le test d’orthostatisme objective le POTS, car la tachycardie augmente debout.'],
    ['Traitement', 'Le pacing diminue les rechutes ; l’eau et le sel augmentent le volume sanguin.'],
   ]), 34, 36) +
 F('Mécanisme, exploration et cible thérapeutique',
   TAB(['Mécanisme', 'Lésion ou cause', 'Exploration', 'Cible thérapeutique'], [
    ['Accumulation du sang dans les jambes', 'Tonus veineux insuffisant', 'Test d’orthostatisme', 'Eau, sel, bas de contention'],
    ['Tachycardie compensatrice', 'Hyperactivité sympathique', 'Test d’orthostatisme, Holter', 'Ivabradine, propranolol'],
    ['Énergie musculaire altérée (hypothèse)', 'Mitochondries, métabolisme', 'Test d’effort sur 2 jours (recherche)', 'Pacing'],
    ['Inflammation (hypothèse)', 'Après infection', 'Aucun test validé', 'Recherche'],
   ]) + P('Ces mécanismes restent des hypothèses ; l’original les présentait comme établis.', 34)) +
 F('Calcul du test d’orthostatisme', P('ΔFC = fréquence cardiaque maximale debout (1–10 min) − fréquence couchée.', 36) +
   P('Exemple : 68/min couchée et 112/min à 6 minutes debout, sans chute de pression, donnent + 44/min : critère de POTS rempli.', 36)))
ADD(4, 'Raisonnement clinique et diagnostic différentiel',
 P('Devant une fatigue invalidante depuis plus de 6 mois, le médecin cherche d’abord une urgence ou une maladie organique. '
   'Puis il cherche le malaise post-effort ; s’il manque, l’EM/SFC est improbable.', 33, 34) +
 DIFF('emsfc') + DIFF_FAT() +
 F('Diagnostics voisins',
   TAB(['Diagnostic', 'Élément distinctif', 'Examen discriminant'], [
    ['Dépression', 'Perte de plaisir et d’envie au premier plan', 'PHQ-9'],
    ['Hypothyroïdie', 'Froid, prise de poids', 'TSH'],
    ['Maladie cœliaque', 'Diarrhée, carence en fer', 'Anticorps anti-transglutaminase IgA'],
    ['Insuffisance surrénalienne', 'Hypotension, hyponatrémie', 'Cortisol matinal'],
    ['Apnées du sommeil', 'Ronflement, somnolence', 'Polygraphie'],
    ['Fibromyalgie', 'Douleur diffuse au premier plan', 'Clinique'],
    ['Sclérose en plaques, myasthénie', 'Signes neurologiques', 'IRM, anticorps'],
   ]), 33, 2))
ADD(5, 'Anamnèse ciblée et drapeaux rouges',
 P('L’anamnèse distingue l’EM/SFC de la dépression : le patient garde l’envie d’agir, mais son corps lâche 12 à 48 h après l’effort. '
   'Elle note le déclencheur, le sommeil, les troubles cognitifs et les symptômes debout.', 33, 34) +
 U('Drapeaux rouges qui remettent en cause le diagnostic : fièvre mesurée, perte de poids, déficit neurologique, CRP élevée, syncope d’effort. Une syncope d’effort ou un déficit aigu relève de l’urgence (144, hospitalisation immédiate).', 33) +
 F('Questions ciblées et leur raison',
   TAB(['Question', 'Pourquoi la poser'], [
    ['Que se passe-t-il le lendemain d’un effort ?', 'Malaise post-effort.'],
    ['Le sommeil vous repose-t-il ?', 'Sommeil non réparateur.'],
    ['Avez-vous du mal à vous concentrer ?', 'Troubles cognitifs.'],
    ['Avez-vous des palpitations ou des vertiges debout ?', 'Intolérance orthostatique, POTS.'],
    ['Avez-vous perdu le plaisir à faire les choses ?', 'Dépression.'],
    ['Tout a-t-il commencé après une infection ?', 'Déclencheur fréquent.'],
   ]), 33))
ADD(6, 'Examen clinique',
 P('L’examen au repos est souvent normal. Il cherche une synovite, un déficit neurologique ou un gros organe, qui orienteraient ailleurs.', 33) +
 P('Valeurs normales : hausse du pouls < 30/min debout, chute de la pression systolique < 20 mmHg. Le test d’orthostatisme objective souvent un POTS.', 36) +
 F('Signes, technique et valeur',
   TAB(['Signe', 'Technique', 'Ce qu’il signifie'], [
    ['Tachycardie debout ≥ 30/min', '10 min couché puis 10 min debout, mesures toutes les 2 min', 'POTS'],
    ['Chute de pression ≥ 20/10 mmHg dans les 3 min', 'Même test', 'Hypotension orthostatique (autre diagnostic)'],
    ['Jambes violacées debout', 'Inspection', 'Sang accumulé dans les jambes'],
    ['Synovite', 'Palpation des articulations', 'Maladie inflammatoire'],
    ['Déficit focal', 'Examen neurologique', 'Autre diagnostic'],
   ]), 36, 33))
ADD(7, 'Syndromes et signes cliniques',
 F('Signes fonctionnels (symptômes rapportés)', UL(['Fatigue profonde', 'Malaise post-effort', 'Sommeil non réparateur', 'Brouillard mental', 'Palpitations debout']), 34) +
 F('Signes physiques (constatés à l’examen)', UL(['Tachycardie orthostatique', 'Acrocyanose des jambes debout', 'Examen neurologique normal']), 36) +
 P('Le syndrome d’intolérance à l’effort réunit malaise post-effort, sommeil non réparateur et épuisement : il traduit une capacité énergétique réduite. '
   'Le syndrome cognitif et autonome réunit brouillard mental, sensibilité au bruit et intolérance debout : il traduit le dérèglement du système nerveux autonome.', 34, 36) +
 F('Intolérance à l’effort', TAB(['Signe', 'Mécanisme', 'Valeur'], [
    ['Malaise post-effort', 'Inconnu', 'Critère central'],
    ['Sommeil non réparateur', 'Inconnu', 'Critère obligatoire'],
    ['Baisse des activités', 'Fatigue', 'Critère obligatoire'],
   ]), 34) +
 F('Syndrome cognitif et autonome', TAB(['Signe', 'Mécanisme', 'Valeur'], [
    ['Brouillard mental', 'Hypothèse inflammatoire', 'Critère (1 sur 2)'],
    ['Intolérance orthostatique', 'Dysautonomie', 'Critère (1 sur 2)'],
    ['Hypersensibilité sensorielle', 'Inconnu', 'Fréquente'],
   ]), 34))
ADD(8, 'Critères diagnostiques',
 P('Le diagnostic est clinique, après un bilan d’exclusion. Une fatigue chronique seule ne suffit pas.', 34, 33) +
 F('Critères IOM 2015 et NICE 2021',
   TAB(['Critère', 'IOM 2015', 'NICE 2021'], [
    ['Durée', '≥ 6 mois', 'Suspicion dès 6 semaines ; diagnostic après 3 mois'],
    ['Baisse des activités avec fatigue', 'Obligatoire', 'Obligatoire'],
    ['Malaise post-effort', 'Obligatoire', 'Obligatoire'],
    ['Sommeil non réparateur', 'Obligatoire', 'Obligatoire'],
    ['Troubles cognitifs', '1 sur 2 avec l’intolérance orthostatique', 'Obligatoire'],
    ['Intensité', 'Modérée à sévère ≥ 50 % du temps', '—'],
   ]) + P('Aucune recommandation suisse propre n’a été retrouvée ; l’original affirmait que ces critères étaient « adoptés en Suisse ». Les critères de consensus international de 2011 sont plus stricts.', 34, 33, 56)) +
 F('Critères du POTS (HRS 2015)', TAB(['Critère', 'Seuil'], [['Hausse de fréquence cardiaque debout', '≥ 30/min (≥ 40/min de 12 à 19 ans) dans les 10 min'], ['Pression', 'Pas d’hypotension orthostatique'], ['Symptômes', 'Chroniques (≥ 6 mois)']]), 36))
ADD(9, 'Examens complémentaires',
 H4('9.a Examen de référence') +
 P('Il n’existe aucun biomarqueur validé. La référence est l’application des critères cliniques après exclusion des autres diagnostics. Sans examen de référence, la sensibilité et la spécificité des critères ne peuvent pas être mesurées ; le test d’orthostatisme a une spécificité limitée.', 34, 33) +
 H4('9.b Examens de première et de deuxième intention') +
 P('En première intention, on fait un bilan d’exclusion simple et un test d’orthostatisme. En deuxième intention, on adresse en centre spécialisé.', 33) +
 TAB(['Intention', 'Examen', 'Pourquoi'], [
  ['1re', 'Hémogramme, CRP, vitesse de sédimentation', 'Anémie, inflammation'],
  ['1re', 'Ferritine, vitamine B12', 'Carences'],
  ['1re', 'TSH', 'Hypothyroïdie'],
  ['1re', 'Glycémie, HbA1c', 'Diabète'],
  ['1re', 'Créatinine, ionogramme, calcium, tests hépatiques', 'Rein, foie, calcium'],
  ['1re', 'Créatine kinase', 'Myopathie'],
  ['1re', 'Anticorps anti-transglutaminase IgA', 'Maladie cœliaque'],
  ['1re', 'Cortisol matinal', 'Insuffisance surrénalienne'],
  ['1re', 'Test d’orthostatisme de 10 min', 'POTS'],
  ['2e', 'Test d’inclinaison (tilt-test)', 'Dysautonomie'],
  ['2e', 'Test d’effort cardiopulmonaire sur 2 jours', 'Recherche ; risque de malaise post-effort'],
 ]) +
 H4('9.c Prescription et formules') +
 P('Indication : fatigue > 6 mois avec malaise post-effort, ou symptômes debout. Moment : test d’orthostatisme le matin. '
   'Préparation : éviter café, nicotine et repas lourd avant le test ; noter les médicaments qui accélèrent le cœur.', 36) +
 TAB(['Grandeur', 'Formule', 'Repère'], [['ΔFC', 'FC debout max − FC couchée', '≥ 30/min : POTS'], ['Chute de pression', 'PAS couchée − PAS debout', '≥ 20 mmHg : hypotension orthostatique']]) +
 H4('9.d Interprétation : positif, négatif, limite, discordant') +
 TAB(['Situation', 'Interprétation', 'Conduite'], [
  ['Positif : ΔFC ≥ 30/min sans chute de pression', 'POTS', 'Eau, sel, contention'],
  ['Négatif : ΔFC < 20/min', 'Pas de POTS', 'EM/SFC possible quand même'],
  ['Limite : ΔFC 25–29/min', 'Non concluant', 'Répéter, tilt-test'],
  ['Discordant : POTS mais bilan inflammatoire anormal', 'Autre cause', 'Reprendre le bilan'],
 ]) +
 H4('9.e Alternatives') +
 P('Grossesse : le POTS peut varier ; avis spécialisé avant tout médicament. Enfant et adolescent : seuil de 40/min. '
   'DFGe < 30 : chercher une cause rénale de fatigue avant de retenir l’EM/SFC.', 36, 33))
ADD(10, 'Arbre décisionnel',
 P('Si le malaise post-effort manque, alors on cherche un autre diagnostic. S’il est présent avec les critères, alors on pose l’EM/SFC.', 33, 34) +
 F('Arbre décisionnel : fatigue invalidante depuis plus de 6 mois',
   OL(['Drapeau rouge : urgence ou bilan ciblé.',
       'Bilan d’exclusion de première intention.',
       'Bilan anormal : traiter la cause.',
       'Bilan normal : chercher le malaise post-effort.',
       'Absent : dépression, burn-out, déconditionnement ; activité progressive.',
       'Présent avec critères : EM/SFC ; pacing.',
       'Symptômes debout : test d’orthostatisme ; traiter le POTS.']), 33))
ADD(11, 'Prise en charge',
 H4('11.A Buts : d’abord l’urgence (syncope, déshydratation), car elle peut blesser dans les minutes qui suivent une chute') +
 P('Le traitement stabilise l’énergie, évite les rechutes, contrôle l’intolérance debout et protège la qualité de vie et les droits sociaux.', 33) +
 TAB(['But', 'Cible chiffrée'], [['Malaise post-effort', 'Moins d’épisodes'], ['Eau (POTS)', '2–3 L/j'], ['Sel (POTS)', '10–12 g/j sans hypertension']]) +
 H4('11.B Moyens et méthodes : forme compliquée en urgence, puis forme non compliquée en ambulatoire') +
 P('La forme compliquée (syncope avec blessure, déshydratation sévère) se traite en urgence : perfusion de solution saline dans les heures qui suivent. '
   'La forme non compliquée se traite en ambulatoire, avec des mesures générales : pacing, journal d’activité et aménagement du travail.', 33, 36) +
 P('Le pacing consiste à fractionner les activités physiques et mentales pour rester sous son seuil. Le cardiofréquencemètre peut aider ; le seuil de « 60 % de la fréquence maximale » de l’original n’est pas sourcé.', 33) +
 P('POTS : eau 2–3 L/j, sel 10–12 g/j et bas de contention jusqu’à la taille.', 36) +
 FICHE([
  ['Inhibiteur du courant If : ivabradine (Procoralan®)', 'Ralentit le nœud sinusal sans baisser la pression', 'Demi-vie ≈ 2 h ; CYP3A4', '2,5 mg 2×/j, puis 5 mg 2×/j selon le pouls (hors indication) ; l’information suisse ne prévoit pas le POTS ; max 7,5 mg 2×/j', 'Phosphènes, bradycardie', 'Grossesse, bradycardie', 'Inhibiteurs du CYP3A4'],
  ['Bêtabloquant : propranolol (Inderal®)', 'Bloque les récepteurs β', 'Demi-vie ≈ 3–6 h', '10–20 mg jusqu’à 4×/j (hors indication)', 'Fatigue, hypotension', 'Asthme', 'Vérapamil'],
  ['Agoniste α1 : midodrine (Gutron®)', 'Resserre les vaisseaux', 'Demi-vie du métabolite ≈ 3 h', 'Départ 2,5 mg 2–3×/j ; entretien 5–10 mg 3×/j ; max 30 mg/j ; dernière prise ≥ 4 h avant le coucher', 'Hypertension couchée, chair de poule', 'Hypertension sévère', 'Autres vasoconstricteurs'],
  ['Naltrexone à faible dose (préparation magistrale)', 'Hypothèse : modulation de la microglie via le récepteur de type Toll 4 (TLR4), rebond des endorphines', 'Demi-vie courte', '0,5–1,5 mg le soir, titration lente jusqu’à 3–4,5 mg/j (hors indication)', 'Rêves vifs, céphalées', 'Opioïdes', 'Opioïdes'],
 ], 36, 33, 81, 82, 83) +
 P('Aucun médicament n’est autorisé pour l’EM/SFC. La naltrexone à faible dose n’a pas de preuve solide ; elle n’impose pas de surveillance hépatique à ces doses. '
   'La revue de Younger (2014) porte sur la douleur chronique, pas sur l’EM/SFC : elle documente le mécanisme et les doses usuelles, pas l’efficacité.', 33, 40, 83) +
 F('Situations particulières',
   TAB(['Situation', 'Particularité'], [
    ['Grossesse', 'Éviter ivabradine ; eau, sel et contention'],
    ['Personne âgée', 'Penser d’abord aux causes organiques'],
    ['Enfant', 'Scolarité adaptée ; seuil POTS de 40/min'],
    ['Insuffisance hépatique', 'Prudence avec la naltrexone'],
    ['Insuffisance rénale (DFGe bas)', 'Midodrine à réduire'],
    ['Forme sévère alitée', 'Soins à domicile, réduction des stimulations'],
   ]), 33) +
 SOCIAL('L’arrêt de travail est souvent prolongé ; un temps partiel adapté est préférable à une reprise brutale.',
        'L’EM/SFC n’interdit pas la conduite ; une somnolence ou des syncopes l’interdisent temporairement.') +
 H4('11.C Surveillance et critères de sortie') +
 TAB(['Quand', 'Quoi'], [
  ['À chaque consultation', 'Journal d’activité, fréquence des malaises post-effort'],
  ['Sous ivabradine ou propranolol', 'Pouls, pression'],
  ['Sous midodrine', 'Pression couchée'],
  ['Si nouveau symptôme', 'Reprendre le bilan'],
  ['Critères de sortie d’hospitalisation', 'Pas de syncope, hydratation correcte, plan de pacing'],
 ]) + P('Une aggravation brutale impose de chercher une autre maladie.', 33) +
 H4('11.D Pronostic et recherche 2026') +
 P('L’EM/SFC est chronique et fluctuante ; la rémission complète est rare chez l’adulte et plus fréquente chez l’enfant.', 34, 33) +
 P('L’immunoadsorption et des modulateurs du métabolisme sont en recherche ; aucun traitement n’est validé.', 33))
ADD(12, 'Prévention',
 P('Aucune mesure n’a prouvé qu’elle prévient l’EM/SFC. Une reprise progressive après une infection est raisonnable, mais non démontrée.', 33) +
 F('Prévention primaire, secondaire et tertiaire',
   TAB(['Niveau', 'Mesure'], [
    ['Primaire', 'Vaccination contre la COVID-19 et la grippe selon le plan suisse'],
    ['Secondaire', 'Reconnaître tôt le malaise post-effort et adapter l’activité'],
    ['Tertiaire', 'Pacing, aménagement du travail, soutien social'],
   ]) + P('En Suisse, le plan de vaccination de l’OFSP s’applique ; aucune mesure propre à l’EM/SFC n’existe.', 33, 41)))
ADD(13, 'Points clés',
 P('Le malaise post-effort est le critère central. '
   'Aucun biomarqueur ne confirme l’EM/SFC : le diagnostic reste clinique, après un bilan d’exclusion simple. '
   'Le pacing est le traitement de base ; le POTS associé se traite par l’eau, le sel et la contention. '
   'Le NICE 2021 déconseille l’exercice gradué à paliers fixes, car il ignore le malaise post-effort.', 33, 70))
ADD(14, 'Pièges d’examen',
 TAB(['Piège', 'Ce qu’il faut répondre'], [
  ['Prescrire un exercice gradué intensif', 'Non : risque de rechute prolongée'],
  ['Conclure à une dépression sans chercher le malaise post-effort', 'Non : interroger sur le lendemain de l’effort'],
  ['Retenir un POTS malgré une chute de pression', 'Non : c’est une hypotension orthostatique'],
  ['Citer l’essai PACE comme preuve de l’exercice gradué', 'Non : ses résultats sont contestés'],
  ['Dire que le malaise post-effort est pathognomonique', 'Non : il est cardinal'],
 ]) + P('Ces pièges reprennent le NICE et l’IOM.', 33, 34, 70))
CTX = {'_prefixe': 'Dans l’EM/SFC',
 'ortho': 'Une hausse ≥ 30/min sans chute de pression signe un POTS.',
 'cpet': 'Sur 2 jours, une baisse au 2e jour est décrite en recherche ; le test peut déclencher un malaise post-effort.',
 'nfs': 'Un hémogramme anormal oriente vers une autre cause.',
 'crp': 'Une CRP élevée remet en cause le diagnostic.',
 'vs': 'Une vitesse élevée remet en cause le diagnostic.',
 'tsh': 'Une TSH anormale oriente vers la thyroïde.',
 'ttg': 'Des anticorps positifs orientent vers une maladie cœliaque.',
 'cort': 'Un cortisol matinal bas impose un test au Synacthène®.',
 'ck': 'Une CK élevée oriente vers une myopathie.',
 'ferritine': 'Une ferritine basse oriente vers une carence en fer.',
 'b12': 'Une B12 basse peut expliquer fatigue et troubles cognitifs.',
 'holter': 'Il documente la tachycardie dans la vie courante.'}
if __name__ == '__main__':
    produire(M, PTS, SOURCES, CTX)
