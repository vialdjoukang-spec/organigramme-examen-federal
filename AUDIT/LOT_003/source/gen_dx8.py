# -*- coding: utf-8 -*-
"""DX.8 — Polyurie de la maladie rénale chronique, de la polykystose et du syndrome de levée d'obstacle. LOT 3, V5 → V7 AUDITÉ."""
from lot3_commun import *
POINT = mkPOINT('dx8')
M = META('dx8', 'DX.8', 'MRC, polykystose et levée d’obstacle', 'Polyurie rénale : maladie rénale chronique, polykystose et syndrome de levée d’obstacle',
         'LOT_003_DX8_MRC_polykystose_levee_obstacle_AUDITÉ.html',
         'Corrections : « 30–50 % des drainages » remplacé par la fourchette publiée (0,5–52 %) ; seuil « DFGe < 45 » retiré (non sourcé) ; compensation du syndrome de levée d’obstacle alignée sur la source (75 % de la diurèse de l’heure précédente, avis d’experts) ; ionogramme toutes les 12 h et non 4–6 h ; attribution SSED/SSMIG des règles des jours de maladie retirée (non vérifiée) ; « 4 piliers » limités à la MRC du diabète de type 2.')
ISO = T('isosthénurie', 'L’isosthénurie est une urine d’osmolalité fixe, proche de celle du plasma (≈ 300 mOsm/kg, densité ≈ 1,010) : le rein ne concentre ni ne dilue plus.')
SLO = T('SLO', 'Le syndrome de levée d’obstacle (SLO) est une polyurie après le drainage d’une obstruction urinaire basse ou bilatérale.')
PTS = []

p1 = (P('Deux causes rénales donnent une polyurie. La maladie rénale chronique (MRC) et la polykystose rénale autosomique dominante (PKAD) détruisent la médullaire ; l’urine devient isosthénurique. '
        'Le ' + SLO + ' survient après le drainage d’une obstruction urinaire basse, bilatérale ou sur rein unique.', 44, 46) +
      F('Terminologie',
        TAB(['Terme', 'Définition exacte', 'À ne pas confondre avec'], [
         ['MRC', 'DFGe < 60 mL/min/1,73 m² ou marqueur d’atteinte rénale pendant > 3 mois', 'Insuffisance rénale aiguë'],
         ['Isosthénurie', 'Osmolalité urinaire fixe ≈ 300 mOsm/kg', 'Urine diluée (< 100 mOsm/kg) de la polydipsie'],
         ['SLO physiologique', 'Élimination de l’excès d’eau et d’urée, ≈ 24 h', 'SLO pathologique (> 48 h, perte de sel)'],
         ['Nycturie', 'Lever nocturne pour uriner', 'Pollakiurie de l’obstacle prostatique'],
        ]), 44, 46))
PTS.append(POINT(1, 'Définition et sémantique', p1))

p2 = (P('En Suisse, l’étude de 2016 estime la prévalence de la MRC à 10,4 % des adultes. '
        'Dans une étude de séquençage nord-américaine, la PKAD touche ≈ 9,3 / 10 000 personnes ; les données européennes sont proches. '
        'Après drainage d’une obstruction, la fréquence publiée du SLO varie de 0,5 % à 52 %.', 45, 57, 46) +
      F('Chiffres, terrain et histoire naturelle',
        TAB(['Donnée', 'Valeur', 'Population'], [
         ['MRC (tous stades)', '10,4 %', 'Adultes en Suisse'],
         ['PKAD', '≈ 9,3 / 10 000', 'Population générale séquencée'],
         ['SLO après drainage', '0,5–52 %', 'Patients drainés pour obstruction'],
         ['Rétention aiguë au cours de la vie', '≈ 1 homme sur 10 de 70–79 ans', 'Hommes âgés'],
        ]) + P('Le terrain associe homme âgé avec hypertrophie prostatique, diabète ancien et MRC ; la mortalité du SLO pathologique non traité est réelle mais non chiffrée.', 46)))
PTS.append(POINT(2, 'Épidémiologie (Suisse, puis Europe)', p2))

p3 = (P('Le rein sain concentre l’urine jusqu’à ≈ 1200 mOsm/kg grâce au gradient de la médullaire. '
        'Dans la MRC et la PKAD, la fibrose ou les kystes détruisent ce gradient ; l’urine reste à ≈ 300 mOsm/kg. '
        'Comme la charge de solutés à éliminer ne change pas, le volume d’urine augmente.', 32, 44) +
      P('Dans le SLO, la pression dans les tubules baisse le gradient et les transporteurs de sel ; le tube collecteur répond moins à la vasopressine. '
        'L’urée et le sel accumulés pendant l’obstruction sont ensuite filtrés en masse.', 46) +
      F('Chaîne logique : de l’anatomie au traitement',
        TAB(['Étape', 'Ce qu’il faut comprendre'], [
         ['Anatomie', 'Médullaire rénale avec anses de Henlé et vasa recta ; prostate autour de l’urètre.'],
         ['Physiologie', 'Pourquoi le rein sain urine peu la nuit : il concentre l’urine jusqu’à ≈ 1200 mOsm/kg.'],
         ['Physiopathologie', 'Médullaire détruite (MRC, PKAD) ou lésée par la pression (SLO) : urine non concentrée.'],
         ['Clinique', 'D’où la nycturie, la soif et, après drainage, la polyurie massive.'],
         ['Examens', 'On mesure le DFGe, l’albuminurie, l’osmolalité urinaire et on fait une échographie rénale.'],
         ['Traitement', 'On protège le rein (MRC), on compense une partie des pertes (SLO).'],
        ]), 32, 46) +
      F('Volume urinaire minimal obligatoire',
        TAB(['Situation', 'Charge de solutés', 'Osmolalité urinaire maximale', 'Volume minimal'], [
         ['Rein sain', '750 mOsm/j', '1200 mOsm/kg', '750 / 1200 ≈ 0,6 L/j'],
         ['Isosthénurie (MRC, PKAD)', '750 mOsm/j', '300 mOsm/kg', '750 / 300 = 2,5 L/j'],
        ]) + P('Le calcul suit la formule volume = charge de solutés / osmolalité urinaire maximale.', 32)) +
      F('Mécanisme, exploration et cible thérapeutique',
        TAB(['Mécanisme', 'Exploration', 'Cible thérapeutique'], [
         ['Gradient médullaire détruit', 'Osmolalité urinaire', 'Accès libre à l’eau'],
         ['Perte de néphrons', 'DFGe, albuminurie', 'Bloqueur du système rénine-angiotensine, gliflozine'],
         ['Kystes qui grossissent (PKAD)', 'Échographie, volume rénal', 'Tolvaptan si progression rapide'],
         ['Perte de sel après drainage', 'Natriurèse, ionogramme', 'Compensation partielle par NaCl 0,45 %'],
        ]), 44, 58, 46))
PTS.append(POINT(3, 'Physiopathologie', p3))

p4 = (P('Après un drainage, le clinicien cherche d’abord l’urgence : hypotension, tachycardie, dysnatrémie, hypokaliémie. '
        'Puis il sépare le SLO physiologique, qui s’arrête en ≈ 24 h, du SLO pathologique, qui dure > 48 h. '
        'Devant une nycturie chronique, il distingue l’isosthénurie du diabète et de l’obstacle prostatique.', 46) +
      DIFF('mrc') +
      F('Après drainage d’une obstruction (même population : patients drainés ; probabilités en exposant rouge)',
        TAB(['Situation', 'Argument', 'Conduite'], [
         ['SLO (toutes formes)' + PR('0,5–52 %', 46), 'Diurèse > 200 mL/h pendant 2 h ou > 3 L/24 h', 'Surveillance rapprochée'],
         ['SLO pathologique' + PR('non chiffrée', 46), 'Polyurie > 48 h, hypotension, natriurèse > 40 mmol/L', 'Perfusion, avis néphrologique'],
         ['Pas de SLO' + PR('complément, non chiffré', 46), 'Diurèse < 200 mL/h', 'Sortie après 24 h'],
        ])))
PTS.append(POINT(4, 'Raisonnement clinique et diagnostic différentiel', p4))

p5 = (P('L’anamnèse cherche une nycturie ancienne, des antécédents familiaux de kystes rénaux ou d’anévrisme cérébral, un jet faible et une sonde récente.', 46, 88) +
      U('Drapeaux rouges après drainage : diurèse > 200 mL/h pendant 2 h, hypotension, confusion, kaliémie < 3 mmol/L. Ils imposent une hospitalisation immédiate et une surveillance horaire.', 46) +
      F('Questions ciblées et leur raison',
        TAB(['Question', 'Pourquoi la poser'], [
         ['Combien de fois vous levez-vous la nuit pour uriner ?', 'La nycturie précoce évoque l’isosthénurie.'],
         ['Un parent a-t-il des kystes rénaux ou un anévrisme cérébral ?', 'Évoque une PKAD.'],
         ['Votre jet est-il faible, avez-vous du mal à vider la vessie ?', 'Obstacle prostatique.'],
         ['Prenez-vous un anticholinergique ?', 'Il favorise la rétention.'],
         ['Avez-vous soif, des vertiges en vous levant ?', 'Déshydratation.'],
        ]), 46))
PTS.append(POINT(5, 'Anamnèse ciblée et drapeaux rouges', p5))

p6 = (P('Avant le drainage, l’examen palpe et percute le globe vésical, mat et tendu ; à l’état normal, la vessie vide n’est pas palpable. '
        'Le toucher rectal apprécie la prostate ; la palpation lombaire cherche de gros reins bosselés. '
        'Le globe clinique a une sensibilité imparfaite ; l’échographie vésicale mesure le volume retenu.', 46) +
      F('Signes, technique et valeur',
        TAB(['Signe', 'Technique', 'Ce qu’il signifie'], [
         ['Globe vésical', 'Palpation, percussion sus-pubienne', 'Rétention urinaire'],
         ['Prostate grosse et ferme', 'Toucher rectal', 'Hypertrophie bénigne'],
         ['Gros reins bosselés', 'Palpation bimanuelle', 'PKAD'],
         ['Hypotension orthostatique', 'Pression couchée puis debout', 'SLO déplétif'],
         ['Poids', 'Pesée quotidienne', 'Bilan de liquide'],
        ]), 46))
PTS.append(POINT(6, 'Examen clinique', p6))

p7 = (P('Deux syndromes s’opposent par leur rythme. Le syndrome d’isosthénurie est chronique et nocturne. '
        'Le syndrome de levée d’obstacle est aigu et suit le drainage.', 46, 44) +
      F('Signes fonctionnels (symptômes rapportés)', UL(['Nycturie', 'Soif', 'Jet faible', 'Vertiges après le drainage']), 46) +
      F('Signes physiques (constatés à l’examen)', UL(['Globe vésical', 'Gros reins', 'Hypotension orthostatique', 'Perte de poids rapide']), 46) +
      F('Syndrome d’isosthénurie',
        TAB(['Signe', 'Mécanisme', 'Valeur'], [
         ['Nycturie, urines pâles', 'Urine fixe ≈ 300 mOsm/kg', 'MRC ou PKAD'],
         ['Polydipsie modérée', 'Volume obligatoire augmenté', 'Compensation'],
         ['Créatinine élevée', 'Perte de néphrons', 'Stade de MRC'],
        ]), 44) +
      F('Syndrome de levée d’obstacle',
        TAB(['Signe', 'Mécanisme', 'Valeur'], [
         ['Diurèse > 200 mL/h', 'Urée et sel accumulés', 'Critère diagnostique'],
         ['Hypotension, tachycardie', 'Perte de volume', 'Forme pathologique'],
         ['Hypokaliémie, dysnatrémie, hypomagnésémie', 'Pertes urinaires', 'Complications'],
        ]), 46))
PTS.append(POINT(7, 'Syndromes et signes cliniques', p7))

p8 = (P('Le critère KDIGO 2024 de la MRC est un DFGe < 60 mL/min/1,73 m² ou une albuminurie ≥ 3 mg/mmol pendant > 3 mois. '
        'Le SLO se définit par une diurèse > 200 mL/h pendant 2 h ou > 3 L/24 h après drainage, selon un consensus d’experts. '
        'Une polyurie isolée ne suffit pas sans la notion de drainage.', 44, 46) +
      F('Classification KDIGO 2024',
        TAB(['Catégorie', 'Seuil', 'Remarque'], [
         ['G3a / G3b', 'DFGe 45–59 / 30–44', 'Risque modéré à élevé'],
         ['G4 / G5', 'DFGe 15–29 / < 15', 'Préparer la suppléance'],
         ['A1 / A2 / A3', 'Albuminurie < 3 / 3–30 / > 30 mg/mmol', 'Le risque croît avec l’albuminurie'],
         ['PKAD (critères de Pei, 15–39 ans)', '≥ 3 kystes au total', '40–59 ans : ≥ 2 par rein ; ≥ 60 ans : ≥ 4 par rein'],
        ]) + P('Les critères de Pei s’appliquent quand un parent est atteint et que le gène n’est pas connu.', 88)))
PTS.append(POINT(8, 'Critères diagnostiques', p8))

p9 = (H4('9.a Examen de référence') +
      P('Pour la MRC, la référence est le DFGe par l’équation CKD-EPI, avec la cystatine C si besoin, et l’albuminurie. '
        'Pour la PKAD, l’échographie selon Pei a une sensibilité et une spécificité élevées ; l’IRM aide chez le sujet jeune. '
        'Pour le SLO, la mesure horaire de la diurèse suffit.', 44, 88, 46) +
      H4('9.b Examens de première et de deuxième intention') +
      P('En première intention : créatinine et DFGe, urée, ionogramme, bicarbonate, albuminurie et échographie rénale et vésicale. '
        'En deuxième intention : calcium, phosphate, PTH et hémoglobine dans la MRC ; natriurèse, kaliurèse et osmolalité urinaire dans le SLO.', 44, 46) +
      TAB(['Intention', 'Examen', 'Pourquoi'], [
       ['1re', 'Créatinine, DFGe', 'Stade de MRC'],
       ['1re', 'Albuminurie', 'Risque et néphroprotection'],
       ['1re', 'Échographie rénale et vésicale', 'Taille des reins, kystes, dilatation, résidu'],
       ['2e, SLO', 'Natriurèse, osmolalité urinaire', 'Diurèse d’urée (brève) ou de sel (à risque)'],
       ['2e, MRC', 'PTH, phosphate, hémoglobine', 'Complications'],
      ]) +
      H4('9.c Prescription et calculs') +
      P('Indication : tout drainage d’une rétention chronique ou d’une obstruction bilatérale. Moment : diurèse notée toutes les 2 h, électrolytes toutes les 12–24 h. '
        'Préparation : aucune.', 46) +
      TAB(['Calcul', 'Formule', 'Seuil'], [
       ['Fraction d’excrétion du sodium', '(Na urinaire × créatinine plasmatique) / (Na plasmatique × créatinine urinaire) × 100, mêmes unités', '> 2 % : atteinte tubulaire'],
       ['Natriurèse ponctuelle', 'Dosage direct', '> 40 mmol/L : lésion tubulaire, risque de SLO pathologique'],
       ['Densité urinaire', 'Bandelette ou réfractomètre', '1,010 : iso-osmotique ; 1,000 : perte de sel et d’eau'],
      ]) +
      H4('9.d Interprétation : positif, négatif, limite, discordant') +
      TAB(['Résultat', 'Signification', 'Conduite'], [
       ['Positif : diurèse > 200 mL/h pendant 2 h', 'SLO', 'Surveillance, compensation partielle'],
       ['Négatif : diurèse < 200 mL/h à 24 h', 'Pas de SLO', 'Sortie possible'],
       ['Limite : 3 L/24 h sans débit horaire élevé', 'SLO probable', 'Poursuivre la surveillance'],
       ['Discordant : polyurie > 48 h malgré un poids normal', 'SLO pathologique', 'Avis néphrologique'],
      ]) +
      H4('9.e Alternatives') +
      P('Grossesse : échographie seule. Enfant : valves de l’urètre postérieur. '
        'DFGe < 30 : pas de produit iodé si possible ; l’IRM sans gadolinium mesure le volume des reins polykystiques.', 44))
PTS.append(POINT(9, 'Examens complémentaires', p9))

p10 = (P('Si la diurèse dépasse 200 mL/h pendant 2 h après drainage, alors le médecin mesure les électrolytes sanguins et urinaires. '
         'Il ne remplace pas 100 % des pertes, car la perfusion entretient la polyurie ; la natriurèse oriente le soluté.', 46) +
       F('Arbre décisionnel après drainage d’une obstruction',
         OL(['Drainer librement et complètement ; le clampage n’apporte rien.',
             'Diurèse toutes les 2 h, constantes toutes les 6–8 h, électrolytes toutes les 12–24 h.',
             'Diurèse > 200 mL/h pendant 2 h : SLO → électrolytes toutes les 12 h, pesée.',
             'Patient lucide : boissons libres ; sinon NaCl 0,45 % à 75 % de la diurèse de l’heure précédente.',
             'Polyurie > 48 h ou hypotension : SLO pathologique → avis néphrologique.']), 46, 90))
PTS.append(POINT(10, 'Arbre décisionnel', p10))

fiche = FICHE([
  ['Gliflozine : dapagliflozine (Forxiga®)', 'Bloque le cotransporteur sodium-glucose SGLT2 ; baisse la pression intraglomérulaire', 'Demi-vie ≈ 13 h', '10 mg/j ; au long cours si DFGe ≥ 20', 'Infection génitale, déshydratation', 'Dialyse, diabète de type 1', 'Diurétiques'],
  ['Alphabloquant : tamsulosine (Pradif® T)', 'Bloque les récepteurs α1A de la prostate', 'Demi-vie ≈ 10–15 h', '0,4 mg/j', 'Hypotension orthostatique, éjaculation rétrograde', 'Hypotension orthostatique', 'Inhibiteurs du CYP3A4'],
  ['Antagoniste V2 : tolvaptan (Jinarc®)', 'Bloque le récepteur V2 ; freine la croissance des kystes', 'Métabolisme hépatique', '45/15 mg à 90/30 mg/j en 2 prises', 'Polyurie, soif, atteinte hépatique', 'Hépatopathie, hypovolémie', 'Inhibiteurs du CYP3A4'],
 ], 44, 58, 55)
p11 = (H4('11.A Buts : d’abord l’urgence (choc après drainage), car il menace la vie en quelques heures') +
       P('Dans le SLO, le but est d’éviter le choc et les dysnatrémies sans entretenir la polyurie. Dans la MRC, le but est de ralentir la perte de DFGe.', 46, 44) +
       TAB(['But', 'Cible chiffrée'], [
        ['Diurèse après drainage', '< 3 L/24 h à la guérison'],
        ['Compensation IV', '≈ 75 % de la diurèse de l’heure précédente (avis d’experts)'],
        ['Pression artérielle (MRC)', 'Systolique < 120 mmHg si tolérée (KDIGO)'],
        ['Albuminurie (MRC)', 'Réduction ≥ 30 %'],
       ]) +
       H4('11.B Moyens et méthodes : forme compliquée en urgence, forme non compliquée en ambulatoire') +
       P('Le SLO compliqué se traite en urgence : perfusion adaptée aux électrolytes urinaires, surveillance horaire. '
         'Une revue de 1997 montre que la vidange rapide et complète ne cause pas plus d’hématurie ni d’hypotension.', 46, 90) +
       P('En ambulatoire, l’éducation de la MRC porte sur l’accès libre à l’eau, la chaleur et les jeûnes prolongés.', 44) +
       F('Traitements selon la situation',
         TAB(['Situation', 'Traitement', 'Pourquoi'], [
          ['MRC avec albuminurie', 'IEC ou sartan à dose maximale tolérée', 'Baisse la pression glomérulaire'],
          ['MRC, DFGe ≥ 20', 'Gliflozine', 'Ralentit la perte de DFGe'],
          ['MRC du diabète de type 2 avec albuminurie', 'Finérénone (Kerendia®) ; sémaglutide (essai de 2024)', 'Moins d’événements rénaux'],
          ['PKAD à progression rapide', 'Tolvaptan', 'Freine la croissance des kystes'],
          ['Hypertrophie prostatique', 'Tamsulosine, puis chirurgie si rétention', 'Lève l’obstacle'],
         ]), 44, 89, 87, 58) +
       fiche +
       F('Situations particulières',
         TAB(['Situation', 'Particularité'], [
          ['Grossesse', 'IEC, sartans, gliflozines et tolvaptan contre-indiqués'],
          ['Personne âgée', 'Risque de déshydratation ; surveillance de la natrémie'],
          ['Enfant', 'Valves de l’urètre postérieur, uropathies'],
          ['Insuffisance rénale (DFGe < 30)', 'Doses à adapter ; pas d’AINS'],
          ['Insuffisance hépatique', 'Tolvaptan contre-indiqué ; bilan hépatique mensuel pendant 18 mois'],
         ]), 44, 55, 58) +
       SOCIAL('Un arrêt de travail est souvent nécessaire pendant l’hospitalisation pour SLO (durée non chiffrée dans les sources).',
              'La conduite n’est pas limitée par la MRC stable ; elle l’est en dialyse mal tolérée (OAC, annexe 1).') +
       H4('11.C Surveillance et critères de sortie') +
       TAB(['Quand', 'Quoi'], [
        ['Toutes les 2 h après drainage', 'Diurèse'],
        ['Toutes les 12 h si SLO', 'Électrolytes, magnésium, phosphate, urée, créatinine ; poids quotidien'],
        ['Selon le stade (MRC)', 'DFGe et albuminurie 1 à 4 fois par an'],
        ['Critères de sortie', 'Pas de SLO à 24 h, ou diurèse < 3 L/24 h, électrolytes stables'],
       ]) +
       H4('11.D Pronostic et recherche 2026') +
       P('Le SLO physiologique guérit en ≈ 24 h ; la forme pathologique dure > 48 h. '
         'En 2026, la recherche porte sur l’association de plusieurs néphroprotecteurs dans la MRC du diabète de type 2.', 46, 87, 89))
PTS.append(POINT(11, 'Prise en charge', p11))

p12 = (P('En cas de diarrhée, fièvre ou vomissements, le patient suspend temporairement les IEC, sartans, diurétiques, metformine, gliflozines et AINS, car la déshydratation aggrave l’atteinte rénale. '
         'Cette règle repose sur un avis de pratique, sans essai contrôlé.', 44) +
       F('Prévention primaire, secondaire et tertiaire',
         TAB(['Niveau', 'Mesure'], [
          ['Primaire', 'Contrôle de la pression et du diabète'],
          ['Secondaire', 'Créatinine et albuminurie chez l’hypertendu et le diabétique'],
          ['Tertiaire', 'Néphroprotection, éviction des AINS, règles des jours de maladie'],
         ]) + P('En Suisse, l’OFSP inclut la MRC dans la stratégie nationale des maladies non transmissibles ; la SSED recommande l’albuminurie annuelle chez le diabétique.', 45)))
PTS.append(POINT(12, 'Prévention', p12))

PTS.append(POINT(13, 'Points clés',
 P('Le rein malade urine plus parce qu’il ne concentre plus. '
   'Après drainage, une diurèse > 200 mL/h pendant 2 h définit le SLO. '
   'On compense une partie des pertes, jamais la totalité. '
   'La vidange rapide de la vessie est sûre.', 46, 90)))

PTS.append(POINT(14, 'Pièges d’examen',
 TAB(['Piège', 'Ce qu’il faut répondre'], [
  ['Clamper la sonde tous les 500 mL', 'Inutile : la vidange rapide n’augmente pas les complications'],
  ['Remplacer 100 % de la diurèse', 'Entretient la polyurie ; viser ≈ 75 %'],
  ['Croire qu’une MRC rend oligurique', 'Aux stades 3–4, l’isosthénurie rend souvent polyurique'],
  ['Oublier la polyurie du tolvaptan', 'Effet attendu ; accès libre à l’eau'],
 ]) + P('Ces réponses suivent la revue de 1997 et la synthèse de 2015.', 90, 46)))

CTX = {'_prefixe': 'Devant une polyurie rénale',
 'creat': 'Le DFGe < 60 pendant > 3 mois définit la MRC (KDIGO 2024).',
 'albu': 'Une albuminurie ≥ 3 mg/mmol classe A2 et justifie la néphroprotection.',
 'iono': 'Après drainage, les électrolytes se contrôlent toutes les 12–24 h.',
 'natriurese': 'Une natriurèse > 40 mmol/L signale une lésion tubulaire et un risque de SLO pathologique.',
 'osmo': 'Une osmolalité urinaire fixe ≈ 300 mOsm/kg signe l’isosthénurie.',
 'echorein': 'L’échographie compte les kystes (critères de Pei) et cherche une dilatation.',
 'pth': 'La PTH suit le retentissement osseux de la MRC.'}
if __name__ == '__main__':
    produire(M, PTS, SOURCES, CTX)
