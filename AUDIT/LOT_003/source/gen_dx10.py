# -*- coding: utf-8 -*-
"""DX.10 — Résistance à l'arginine-vasopressine (AVP-R, ancien diabète insipide néphrogénique), dont la forme induite par le lithium. LOT 3, V5 → V7 AUDITÉ."""
from lot3_commun import *
POINT = mkPOINT('dx10')
M = META('dx10', 'DX.10', 'Résistance à la vasopressine (AVP-R)', 'Résistance à l’arginine-vasopressine (AVP-R, ancien diabète insipide néphrogénique), forme du lithium et forme héréditaire',
         'LOT_003_DX10_Resistance_vasopressine_AVP_R_AUDITÉ.html',
         'Corrections : « cause n° 1 en Suisse » requalifiée (pas de donnée suisse) ; « AVP-R franc chez 15–20 % » remplacé par les chiffres publiés (défaut de concentration ≥ 54 %, polyurie franche 19 %) ; prévalence héréditaire « 1–9 / 1 000 000 » retirée (inconnue selon le consensus de 2024) ; '
         'perméabilité d’ENaC « 1,5–2 fois » et accumulation « 10–20 fois » retirées (non sourcées) ; « irréversible après 10–15 ans » corrigé (délai non établi) ; Moduretic® remplacé par Comilorid-Mepha® (Moduretic® absent du marché suisse) ; '
         'hausse de la lithiémie sous thiazidique sourcée (25–40 %) ; pistes de recherche corrigées : les essais de sildénafil et de metformine ont échoué.')
PTS = []
LI = T('lithium', 'Le lithium est un régulateur de l’humeur (thymorégulateur) du trouble bipolaire ; il réduit les rechutes et le risque suicidaire, mais sa marge thérapeutique est étroite.')
ENAC = T('ENaC', 'ENaC (epithelial sodium channel) est le canal sodique de la membrane apicale de la cellule principale du tube collecteur ; l’amiloride le bloque.')

p1 = (P('La résistance à l’arginine-vasopressine (AVP-R), ancien diabète insipide néphrogénique, est une incapacité du tube collecteur à répondre à la vasopressine. '
        'L’hormone est présente, souvent élevée, mais le rein ne retient pas l’eau ; l’urine reste diluée. '
        'Le nom a changé en 2022 pour éviter la confusion avec le diabète sucré.', 30, 51) +
      F('Terminologie',
        TAB(['Terme', 'Définition exacte', 'À ne pas confondre avec'], [
         ['AVP-R acquise', 'Résistance rénale due à un médicament (' + LI + ') ou à un trouble métabolique (hypercalcémie, hypokaliémie)', 'AVP-D : manque de sécrétion de l’hormone (DX.9)'],
         ['AVP-R congénitale', 'Mutation du récepteur V2 (gène AVPR2) ou de l’aquaporine 2 (gène AQP2)', 'Polyurie osmotique du diabète sucré'],
         ['Défaut de concentration', 'Urine moins concentrée qu’attendu, sans polyurie franche', 'AVP-R franche (> 3 L/24 h, urine < 300 mOsm/kg)'],
         ['Intoxication au lithium', 'Toxicité neurologique par lithiémie trop haute', 'Néphrotoxicité chronique du lithium'],
        ]), 30, 6, 97))
PTS.append(POINT(1, 'Définition et sémantique', p1))

p2 = (P('Aucune donnée suisse publiée n’a été trouvée. Chez l’adulte, le lithium est la cause acquise la plus citée. '
        'Dans une synthèse de 1987 portant sur ≈ 1100 patients sous lithium, ≥ 54 % ont un défaut de concentration et 19 % une polyurie franche.', 94, 97) +
      F('Chiffres, terrain et histoire naturelle',
        TAB(['Donnée', 'Valeur', 'Population'], [
         ['Défaut de concentration urinaire', '≥ 54 %', 'Patients sous lithium au long cours'],
         ['Polyurie franche', '19 %', 'Mêmes patients'],
         ['AVP-R franche après 15 ans de lithium', '≈ 12 %', 'Revue de 2018'],
         ['Fonction rénale altérée (DFGe bas)', '25,5 %', 'Méta-analyse de 2022, lithium au long cours'],
         ['AVP-R parmi les polyuries hypotoniques explorées', '2 % (3/144)', 'Étude européenne de 2018'],
         ['Formes congénitales liées à l’X (gène AVPR2)', '≈ 90 % des formes congénitales', 'Consensus de 2024 ; prévalence inconnue'],
        ]) + P('Le défaut de concentration peut apparaître 2–4 mois après le début du lithium. La forme congénitale se révèle vers l’âge moyen de ≈ 4 mois, par polyurie, retard de croissance et déshydratation.', 94, 97, 98, 27, 6) + P('Facteurs de risque et terrain : durée du lithium, âge avancé, sexe masculin pour la forme liée à l’X. '
        'Pronostic : la mortalité n’est pas chiffrée dans les sources ; des déshydratations sévères répétées du nourrisson peuvent laisser un retard de développement.', 97, 98, 6)))
PTS.append(POINT(2, 'Épidémiologie (Suisse, puis Europe)', p2))

p3 = (P('Normalement, la vasopressine se fixe au récepteur V2 de la cellule principale du tube collecteur. '
        'Le récepteur active l’AMP cyclique (AMPc) ; l’aquaporine 2 (AQP2) s’insère alors dans la membrane apicale et laisse passer l’eau. '
        'Dans l’AVP-R, une étape de cette chaîne est cassée.', 6, 51) +
      P('Le lithium filtré entre dans la cellule principale par le canal ' + ENAC + ', comme le sodium. '
        'Dans la cellule, il freine la production d’AMPc et la synthèse d’AQP2, en partie par l’inhibition de l’enzyme GSK3β (glycogène synthase kinase 3 bêta). '
        'D’où l’intérêt de l’amiloride : il ferme ENaC, donc la porte d’entrée du lithium.', 51, 94, 95) +
      F('Chaîne logique : de l’anatomie au traitement',
        TAB(['Étape', 'Ce qu’il faut comprendre'], [
         ['Anatomie', 'Cellule principale du tube collecteur : récepteur V2 sur la face sanguine, AQP2 et ENaC sur la face urinaire.'],
         ['Physiologie', 'La vasopressine fait entrer l’AQP2 dans la membrane : l’eau quitte l’urine vers la médullaire concentrée.'],
         ['Physiopathologie', 'Récepteur V2 muté, AQP2 absente ou lithium intracellulaire : la membrane reste imperméable à l’eau.'],
         ['Clinique', 'D’où une polyurie hypotonique qui ne répond pas à la desmopressine, et une soif intense.'],
         ['Examens', 'La copeptine basale est élevée (≥ 21,4 pmol/L) : l’hormone est là, le rein ne répond pas.'],
         ['Traitement', 'On réduit la charge osmotique, on ferme ENaC (amiloride) et on diminue le débit d’eau qui arrive au tube collecteur (thiazidique).'],
        ]), 6, 28, 51) +
      F('Formes congénitales (consensus de 2024)',
        TAB(['Forme', 'Gène et transmission', 'Mécanisme cellulaire'], [
         ['Liée à l’X (≈ 90 %)', 'AVPR2 (Xq28), récessive liée à l’X : surtout des garçons', 'Récepteur V2 mal replié, souvent retenu dans le réticulum endoplasmique'],
         ['Autosomique (< 10 %)', 'AQP2 (12q13), récessive ou dominante : filles et garçons', 'Canal AQP2 défectueux ; récepteur V2 et AMPc intacts'],
        ]) + P('Chez les femmes porteuses d’une mutation AVPR2, la sévérité varie selon l’inactivation du chromosome X.', 6)) +
      F('Pourquoi un diurétique réduit la diurèse (effet paradoxal)',
        TAB(['Mesure', 'Mécanisme', 'Gain'], [
         ['Régime pauvre en sel et en protéines', 'Le volume d’urine = charge osmotique / osmolalité urinaire ; l’osmolalité étant fixée bas, moins de solutés donne moins d’urine', 'Proportionnel à la baisse de la charge'],
         ['Thiazidique (hydrochlorothiazide)', 'Il bloque le cotransporteur NCC du tube distal ; la légère hypovolémie augmente la réabsorption proximale d’eau et de sel, qui ne dépend pas de la vasopressine', 'Jusqu’à 50 % de diurèse en moins à court terme, avec le régime pauvre en sel'],
         ['Amiloride', 'Il bloque ENaC : moins de lithium dans la cellule ; il compense aussi la perte de potassium du thiazidique', 'Effet additif au thiazidique'],
        ]), 6, 51, 95))
PTS.append(POINT(3, 'Physiopathologie', p3))

p4 = (P('Le clinicien cherche d’abord l’urgence : intoxication au lithium et déshydratation hypernatrémique, qui s’aggravent l’une l’autre. '
        'Puis il élimine les causes métaboliques réversibles (hypercalcémie, hypokaliémie, voir DX.7). '
        'Enfin, il distingue l’AVP-R de l’AVP-D et de la polydipsie primaire par la copeptine.', 96, 3, 28) +
      DIFF('avpr') +
      F('Polyurie hypotonique explorée (même population : 144 patients de l’étude de 2018 ; probabilités en exposant rouge)',
        TAB(['Diagnostic', 'Copeptine', 'Indice décisif'], [
         ['AVP-D' + PR('41 %', 27), 'Stimulée ≤ 4,9 pmol/L', 'Début brutal, IRM hypothalamo-hypophysaire'],
         ['Polydipsie primaire' + PR('57 %', 27), 'Stimulée > 4,9 pmol/L', 'Trouble psychiatrique fréquent'],
         ['AVP-R' + PR('2 %', 27), 'Basale ≥ 21,4 pmol/L', 'Lithium, hypercalcémie, forme familiale'],
        ]) + P('Chez un patient sous lithium, la probabilité change : ≥ 54 % ont un défaut de concentration et 19 % une polyurie franche.', 94)))
PTS.append(POINT(4, 'Raisonnement clinique et diagnostic différentiel', p4))

p5 = (P('L’anamnèse précise la durée du lithium, la dose, les lithiémies récentes, la soif de jour et de nuit, et tout nouveau médicament.', 96, 97) +
      U('Drapeaux rouges de l’intoxication au lithium : tremblement grossier, troubles de l’élocution (dysarthrie), marche instable (ataxie), secousses musculaires (myoclonies), confusion, diarrhée ou vomissements. '
        'Ils imposent une lithiémie et un avis en urgence.', 96, 52) +
      F('Questions ciblées et leur raison',
        TAB(['Question', 'Pourquoi la poser'], [
         ['Depuis combien d’années prenez-vous du lithium ?', 'Le risque rénal augmente avec la durée.'],
         ['Avez-vous commencé un anti-inflammatoire, un antihypertenseur ou un diurétique ?', 'AINS, IEC, sartans et thiazidiques élèvent la lithiémie.'],
         ['Avez-vous eu de la diarrhée, des vomissements ou de la fièvre ?', 'La déshydratation fait monter la lithiémie.'],
         ['Combien de fois vous levez-vous la nuit pour uriner ?', 'La nycturie mesure la polyurie au quotidien.'],
         ['Un enfant de la famille a-t-il eu une polyurie dès la naissance ?', 'Forme liée à l’X chez un garçon.'],
         ['Avez-vous des calculs rénaux, une constipation, une faiblesse musculaire ?', 'Hypercalcémie ou hypokaliémie.'],
        ]), 96, 6))
PTS.append(POINT(5, 'Anamnèse ciblée et drapeaux rouges', p5))

p6 = (P('L’examen évalue l’hydratation (pression artérielle couchée et debout, muqueuses, poids), la neurologie et la thyroïde. '
        'À l’état normal, le patient n’a ni tremblement d’action grossier, ni ataxie, ni nystagmus. '
        'Aucun signe d’examen n’a une sensibilité ni une spécificité suffisantes pour poser l’AVP-R : la diurèse et la copeptine le font.', 96, 28) +
      F('Signes, technique et valeur',
        TAB(['Signe', 'Technique', 'Ce qu’il signifie'], [
         ['Tremblement grossier, myoclonies', 'Bras tendus, épreuve doigt-nez', 'Intoxication au lithium (le tremblement fin est fréquent à dose normale)'],
         ['Ataxie, nystagmus', 'Marche, poursuite oculaire', 'Atteinte cérébelleuse du lithium'],
         ['Réflexes vifs', 'Marteau réflexe', 'Neurotoxicité'],
         ['Hypotension orthostatique, muqueuses sèches', 'Pression couchée puis debout', 'Déshydratation'],
         ['Goitre', 'Palpation du cou', 'Goitre ou hypothyroïdie induits par le lithium'],
        ]), 96, 97))
PTS.append(POINT(6, 'Examen clinique', p6))

p7 = (P('Deux syndromes se combinent. Le premier est la polyurie qui résiste à la vasopressine. '
        'Le second est la neurotoxicité du lithium, déclenchée par la déshydratation que cette polyurie provoque : c’est un cercle vicieux.', 51, 96) +
      F('Signes fonctionnels (symptômes rapportés)', UL(['Polyurie, nycturie', 'Soif intense', 'Tremblement, troubles de la marche', 'Diarrhée, nausées']), 97) +
      F('Signes physiques (constatés à l’examen)', UL(['Signes de déshydratation', 'Tremblement grossier, ataxie', 'Confusion', 'Goitre']), 96) +
      F('Syndrome polyuro-polydipsique hypotonique résistant à la vasopressine',
        TAB(['Signe', 'Mécanisme', 'Valeur'], [
         ['Diurèse > 50 mL/kg/24 h ou > 3 L/24 h', 'Le tube collecteur ne retient pas l’eau', 'Définit la polyurie'],
         ['Osmolalité urinaire < 300 mOsm/kg', 'Urine non concentrée', 'Hypotonique'],
         ['Pas de concentration sous desmopressine', 'Le récepteur ou le canal ne répond pas', 'Distingue l’AVP-R de l’AVP-D'],
        ]), 3, 6, 97) +
      F('Syndrome de neurotoxicité aiguë du lithium',
        TAB(['Signe', 'Mécanisme', 'Valeur'], [
         ['Tremblement grossier, ataxie, dysarthrie', 'Accumulation cérébrale du lithium', 'Urgence'],
         ['Confusion, myoclonies', 'Encéphalopathie', 'Gravité'],
         ['Lithiémie au-delà de 1,0–1,2 mmol/L', 'Rein déshydraté : plus de lithium réabsorbé', 'Limites hautes les plus citées, sans seuil consensuel'],
        ]), 52, 96))
PTS.append(POINT(7, 'Syndromes et signes cliniques', p7))

p8 = (P('Selon la revue de 2025, le consensus de 2024 et l’étude de 2015, les critères de l’AVP-R sont deux : une polyurie hypotonique (> 50 mL/kg/24 h, urine < 300 mOsm/kg) et une copeptine basale ≥ 21,4 pmol/L. '
        'Une polyurie sous lithium ne suffit pas : il faut exclure le diabète sucré et l’hypercalcémie.', 3, 28) +
      F('Critères et performance',
        TAB(['Élément', 'Seuil', 'Valeur diagnostique'], [
         ['Polyurie', '> 50 mL/kg/24 h', 'Condition préalable'],
         ['Osmolalité urinaire', '< 300 mOsm/kg', 'Polyurie hypotonique (souvent < 200 dans la forme congénitale)'],
         ['Copeptine basale, sans restriction hydrique', '≥ 21,4 pmol/L', 'AVP-R ; sensibilité et spécificité 100 % dans l’étude de 2015 (petit effectif)'],
         ['Forme congénitale', 'Variant pathogène AVPR2 ou AQP2', 'Diagnostic définitif ; génétique d’emblée chez l’enfant'],
        ]), 3, 6, 28))
PTS.append(POINT(8, 'Critères diagnostiques', p8))

p9 = (H4('9.a Examen de référence') +
      P('Chez l’adulte, la référence biologique est la copeptine basale associée à l’osmolalité urinaire. '
        'Au seuil de 21,4 pmol/L, la sensibilité et la spécificité étaient de 100 % dans l’étude de 2015. '
        'Chez l’enfant, la référence est le test génétique (AVPR2, AQP2), qui évite le test de restriction hydrique, dangereux chez le nourrisson.', 28, 6) +
      H4('9.b Examens de première et de deuxième intention') +
      P('En première intention : lithiémie, natrémie, kaliémie, calcium, glycémie, créatinine et DFGe, TSH. '
        'En deuxième intention : copeptine basale, séquençage génétique chez l’enfant, échographie rénale et vésicale.', 3, 6, 99) +
      TAB(['Intention', 'Examen', 'Pourquoi'], [
       ['1re', 'Lithiémie 12 h après la dernière prise', 'Toxicité ou sous-dosage'],
       ['1re', 'Natrémie, osmolalités plasmatique et urinaire', 'Polyurie hypotonique, hypernatrémie'],
       ['1re', 'Calcium, potassium, glycémie', 'Causes métaboliques et diurèse osmotique'],
       ['1re', 'Créatinine et DFGe, TSH', 'Néphropathie et hypothyroïdie du lithium'],
       ['2e', 'Copeptine basale', 'Confirme l’AVP-R'],
       ['2e', 'Séquençage génétique (AVPR2, AQP2)', 'Forme congénitale'],
       ['2e', 'Échographie rénale et vésicale, avant et après miction', 'Dilatation due au débit urinaire (hydronéphrose chez 34 % des patients congénitaux)'],
      ]) +
      H4('9.c Prescription et calculs') +
      P('Indication : polyurie hypotonique, surtout sous lithium. Moment : lithiémie le matin, 12 h après la prise du soir, à l’équilibre. '
        'Préparation : aucune restriction hydrique avant la copeptine basale ; noter l’heure de la dernière prise.', 28, 52) +
      TAB(['Calcul', 'Formule', 'Exemple'], [
       ['Volume d’urine', 'Charge osmotique (mOsm/j) / osmolalité urinaire (mOsm/kg)', '900 / 100 = 9 L ; 600 / 100 = 6 L'],
       ['Charge osmotique rénale (nourrisson)', 'Protéines (g) × 4 + 2 × (Na + K en mmol)', 'Cible ≈ 15 mOsm/kg/j chez le nourrisson'],
       ['Polyurie', 'Diurèse / poids', '> 50 mL/kg/24 h'],
      ]) + P('La formule du volume illustre le principe ; les exemples chiffrés sont pédagogiques.', 6) +
      H4('9.d Interprétation : positif, négatif, limite, discordant') +
      TAB(['Résultat', 'Signification', 'Conduite'], [
       ['Positif : copeptine basale ≥ 21,4 pmol/L', 'AVP-R', 'Cause : lithium, calcium, potassium, génétique'],
       ['Négatif : < 21,4 pmol/L', 'AVP-D ou polydipsie primaire', 'Copeptine stimulée (DX.9, DX.4)'],
       ['Limite : AVP-R partielle', 'Réponse partielle à la desmopressine', 'Génétique, avis spécialisé'],
       ['Discordant : polyurie, lithiémie normale', 'L’AVP-R ne dépend pas du taux du jour', 'Ne pas augmenter la dose ; discuter amiloride'],
      ]) +
      H4('9.e Alternatives') +
      P('Grossesse : lithium et diurétiques sous avis spécialisé ; échographie sans irradiation ; les inhibiteurs des prostaglandines sont contre-indiqués. '
        'Enfant : génétique d’emblée. DFGe bas : la copeptine s’accumule, interpréter avec prudence. Aucun produit iodé n’est nécessaire ; l’IRM ne sert que si un AVP-D reste possible.', 6))
PTS.append(POINT(9, 'Examens complémentaires', p9))

p10 = (P('Si l’AVP-R est due au lithium, alors le médecin décide avec le psychiatre : réduire, garder ou remplacer le lithium. '
         'Si le lithium reste indispensable, il ajoute l’amiloride et contrôle la lithiémie.', 95, 97) +
       F('Arbre décisionnel de l’AVP-R',
         OL(['Signes neurologiques, lithiémie haute, hypernatrémie : urgence, hospitalisation.',
             'Polyurie hypotonique confirmée : calcium, potassium, glycémie ; corriger une cause métabolique.',
             'Copeptine basale ≥ 21,4 pmol/L : AVP-R ; chez l’enfant, génétique.',
             'Sous lithium : dose minimale efficace, avis psychiatrique ; si le lithium reste nécessaire, amiloride.',
             'Forme congénitale : régime pauvre en sel et en protéines, thiazidique ± amiloride ; inhibiteur des prostaglandines chez l’enfant.']), 6, 95, 97))
PTS.append(POINT(10, 'Arbre décisionnel', p10))

fiche = FICHE([
  ['Diurétique épargneur de potassium : amiloride (Comilorid-Mepha® avec hydrochlorothiazide ; amiloride seul non commercialisé en Suisse)', 'Bloque ENaC : moins de lithium dans la cellule, moins de perte de potassium', 'Non métabolisé, éliminé par le rein ; demi-vie ≈ 6–9 h (à vérifier, AIPS)', 'Essai de 1985 : diurèse 4,7 → 3,1 L/24 h ; dose de l’original 5–10 mg 1–2 fois/j (hors AIPS, à vérifier)', 'Hyperkaliémie, nausées', 'Hyperkaliémie, DFGe très bas', 'IEC, sartans, potassium (hyperkaliémie)'],
  ['Thiazidique : hydrochlorothiazide (Esidrex®, Comilorid-Mepha® 5/50 ou mite 2,5/25 mg)', 'Bloque NCC ; l’hypovolémie légère augmente la réabsorption proximale', 'Demi-vie ≈ 6–15 h (à vérifier, AIPS)', '25 mg 1–2 fois/j chez l’adulte (consensus de 2024, hors indication AIPS)', 'Hypokaliémie, hyponatrémie, hyperuricémie', 'Hyponatrémie, goutte', 'Lithium : lithiémie + 25–40 %'],
  ['Inhibiteur des prostaglandines : indométacine (enfant)', 'Moins de prostaglandines : meilleure réabsorption d’eau', 'Demi-vie courte', 'Dose de l’original 1,5–2 mg/kg/j (hors AIPS, à vérifier) ; arrêt à l’âge adulte', 'Ulcère, toxicité rénale', 'Lithium, grossesse', 'Lithium (intoxication)'],
 ], 6, 95, 96, 100)
p11 = (H4('11.A Buts : d’abord l’urgence (intoxication au lithium, hypernatrémie), car elles menacent le cerveau') +
       P('Le traitement réduit la diurèse, prévient la déshydratation et évite l’intoxication au lithium.', 6, 96) +
       TAB(['But', 'Cible chiffrée'], [
        ['Diurèse', 'Baisse durable ; la cible « < 3 L/24 h » de l’original n’est pas sourcée'],
        ['Natrémie', '135–145 mmol/L'],
        ['Lithiémie d’entretien', '0,6–0,8 mmol/L (adulte de 18–65 ans)'],
       ]) + P('La cible de lithiémie suit la recommandation internationale de 2019.', 52) +
       H4('11.B Moyens et méthodes : forme compliquée en urgence, forme non compliquée en ambulatoire') +
       P('La forme compliquée relève de l’urgence. Réhydrater avec du glucose 5 %, pas avec du NaCl 0,9 % : 1 L de NaCl 0,9 % exige ≈ 3 L d’urine pour être éliminé. '
         'La natrémie ne doit pas baisser de plus de 8 mmol/L par jour.', 6) +
       P('En ambulatoire : accès libre à l’eau, sel ≤ 6 g/j et protéines < 1 g/kg/j avec une diététicienne, boissons sans sucre. '
         'Le thiazidique se poursuit selon la préférence du patient.', 6) +
       F('Traitements selon la situation',
         TAB(['Situation', 'Traitement', 'Pourquoi'], [
          ['AVP-R du lithium, lithium indispensable', 'Amiloride', 'Ferme l’entrée du lithium dans la cellule'],
          ['AVP-R du lithium, alternative possible', 'Changer de thymorégulateur (décision psychiatrique)', 'L’AVP-R peut régresser à l’arrêt'],
          ['Ajout d’un thiazidique sous lithium', 'Baisse empirique de la dose de lithium, lithiémie à J5–J7', 'La lithiémie monte de 25–40 %'],
          ['Hypercalcémie, hypokaliémie', 'Corriger la cause (DX.7)', 'Résistance réversible'],
          ['Forme congénitale de l’enfant', 'Thiazidique + inhibiteur des prostaglandines ± amiloride', 'Consensus de 2024'],
         ]), 6, 95, 96) +
       fiche +
       F('Situations particulières',
         TAB(['Situation', 'Particularité'], [
          ['Grossesse', 'Inhibiteurs des prostaglandines contre-indiqués ; lithium sous avis spécialisé'],
          ['Personne âgée', 'Diurèse spontanément plus basse : réviser régime et médicaments'],
          ['Enfant', 'Propreté souvent acquise seulement dans la 2e décennie'],
          ['Insuffisance rénale (DFGe bas)', 'Amiloride : risque d’hyperkaliémie ; lithium à rediscuter'],
          ['Insuffisance hépatique sévère', 'Thiazidique prudent : l’hypokaliémie favorise l’encéphalopathie (AIPS à vérifier)'],
          ['Chirurgie, jeûne > 4 h', 'Glucose 5 % IV au débit d’entretien'],
         ]), 6, 55) +
       SOCIAL('Un arrêt de travail court suffit lors d’une intoxication ou d’un ajustement (durée non chiffrée dans les sources).',
              'La conduite est possible si le trouble bipolaire est stable et sans signe de toxicité (OAC, annexe 1).') +
       H4('11.C Surveillance et critères de sortie') +
       TAB(['Quand', 'Quoi'], [
        ['J5–J7 après tout changement (diurétique, AINS, dose)', 'Lithiémie, natrémie, kaliémie, créatinine'],
        ['Tous les 3–6 mois sous lithium', 'Lithiémie ; DFGe, TSH, calcium au moins 2 fois par an'],
        ['Au moins tous les 2 ans (forme congénitale)', 'Échographie rénale et vésicale'],
        ['Critères de sortie', 'Lithiémie dans la cible, natrémie stable, plan d’urgence remis, éducation faite'],
       ]) + P('Le rythme de surveillance du lithium suit NICE et doit être vérifié dans la version en vigueur.', 99, 6) +
       H4('11.D Pronostic et recherche 2026') +
       P('L’AVP-R du lithium régresse souvent à l’arrêt, mais devient en partie irréversible avec la durée ; le délai exact n’est pas établi. '
         'Dans la forme congénitale, ≈ 50 % des adultes ont une MRC de stade ≥ 2 et l’obésité est plus fréquente (41 % contre 16 %).', 94, 97, 6) +
       P('Recherche : les essais de sildénafil, de riociguat et de metformine ont échoué ; un essai d’antagoniste V1a a été arrêté. '
         'Les agonistes des récepteurs EP2 et EP4 et les chaperons pharmacologiques restent au stade animal ou cellulaire en 2026.', 6))
PTS.append(POINT(11, 'Prise en charge', p11))

p12 = (P('Sous lithium, la surveillance régulière de la lithiémie, du DFGe, du calcium et de la TSH dépiste la néphropathie avant qu’elle ne soit irréversible.', 99, 97) +
       F('Prévention primaire, secondaire et tertiaire',
         TAB(['Niveau', 'Mesure'], [
          ['Primaire', 'Lithiémie la plus basse efficace ; éviter AINS et thiazidiques sans contrôle ; boire pendant une gastro-entérite'],
          ['Secondaire', 'Diurèse et DFGe surveillés ; génétique néonatale chez le garçon d’une mère porteuse'],
          ['Tertiaire', 'Amiloride, régime, plan d’urgence et carte, échographie régulière'],
         ]) + P('En Suisse, aucun programme national dédié n’existe ; Comilorid-Mepha® figure dans la liste des spécialités (LS) de l’Office fédéral de la santé publique (OFSP).', 100, 6)))
PTS.append(POINT(12, 'Prévention', p12))

PTS.append(POINT(13, 'Points clés',
 P('L’AVP-R est l’ancien diabète insipide néphrogénique : l’hormone est là, le rein ne répond pas. '
   'Une copeptine basale ≥ 21,4 pmol/L la confirme. '
   'L’amiloride ferme l’entrée du lithium. '
   'Un thiazidique élève la lithiémie de 25–40 %.', 30, 28, 95, 96)))

PTS.append(POINT(14, 'Pièges d’examen',
 TAB(['Piège', 'Ce qu’il faut répondre'], [
  ['Ajouter un thiazidique ou un AINS sous lithium sans contrôle', 'Faute : baisser la dose, lithiémie à J5–J7'],
  ['Réhydrater au NaCl 0,9 %', 'Glucose 5 % : le sel aggrave l’hypernatrémie'],
  ['Traiter l’AVP-R par desmopressine', 'Elle est inefficace ; c’est un test, pas un traitement'],
  ['Augmenter le lithium parce que la lithiémie est basse avec polyurie', 'La polyurie ne reflète pas le taux du jour'],
 ]) + P('Ces réponses suivent le consensus de 2024 et la revue des interactions de 1995.', 6, 96)))

CTX = {'_prefixe': 'Devant une polyurie sous lithium',
 'lithemie': 'Une lithiémie au-delà de 1,0–1,2 mmol/L avec signes neurologiques impose l’hospitalisation.',
 'copeptine': 'Une copeptine basale ≥ 21,4 pmol/L confirme l’AVP-R sans test de restriction.',
 'osmo': 'Une osmolalité urinaire < 300 mOsm/kg confirme la polyurie hypotonique.',
 'iono': 'Une hypercalcémie ou une hypokaliémie est une cause réversible d’AVP-R.',
 'creat': 'Un DFGe en baisse sous lithium impose de rediscuter le traitement.',
 'tsh': 'Une TSH élevée signe une hypothyroïdie induite par le lithium.',
 'gen': 'Un variant AVPR2 chez un garçon confirme la forme liée à l’X.',
 'echorein': 'Une dilatation des voies urinaires traduit le débit urinaire chronique.',
 'gly': 'Une glycémie élevée oriente vers une diurèse osmotique et non vers l’AVP-R.',
 'pth': 'Une PTH élevée sous lithium évoque une hyperparathyroïdie induite.'}
if __name__ == '__main__':
    produire(M, PTS, SOURCES, CTX)
