# -*- coding: utf-8 -*-
"""DX.3 — Xérostomie et syndrome de Sjögren. LOT 3, V5 → V7 AUDITÉ."""
from lot3_commun import *
POINT = mkPOINT('dx3')
M = META('dx3', 'DX.3', 'Xérostomie et Sjögren', 'Xérostomie (pseudo-polydipsie) et syndrome de Sjögren',
         'LOT_003_DX3_Xerostomie_Sjogren_AUDITÉ.html',
         'Corrections majeures : prévalences non sourcées remplacées (méta-analyses Agostini 2018 et Qin 2015) ; « 80 % de causes médicamenteuses » retiré faute de source ; focus score complété (« par 4 mm² ») ; rituximab signalé hors indication ; surveillance de grossesse anti-SSA alignée sur l’ACR 2020.')
AQP = T('aquaporine 5', 'L’aquaporine 5 est un canal à eau de la membrane apicale des cellules acineuses ; elle laisse passer l’eau vers la lumière de la glande.')
FS = T('focus score', 'Le focus score compte les foyers d’au moins 50 lymphocytes par 4 mm² de glande salivaire accessoire.')
PTS = []

p1 = (P('La xérostomie est la sensation de bouche sèche. L’hyposialie en est la mesure objective : débit salivaire non stimulé ≤ 0,1 mL/min. '
        'Le patient boit souvent de petites gorgées pour humidifier sa bouche (pseudo-polydipsie), sans polyurie vraie.', 35, 70) +
      F('Terminologie',
        TAB(['Terme', 'Définition exacte', 'À ne pas confondre avec'], [
         ['Xérostomie', 'Sensation subjective de sécheresse buccale', 'Hyposialie (mesurée)'],
         ['Hyposialie', 'Débit salivaire non stimulé ≤ 0,1 mL/min', 'Bouche sèche passagère (stress, respiration buccale)'],
         ['Pseudo-polydipsie', 'Boissons fréquentes en petites quantités, diurèse < 2,5 L/24 h', 'Polydipsie vraie avec polyurie'],
         ['Syndrome de Sjögren', 'Maladie auto-immune des glandes exocrines (salivaires, lacrymales)', 'Syndrome sec iatrogène ou lié à l’âge'],
         ['Xérophtalmie', 'Sécheresse oculaire (kératoconjonctivite sèche)', 'Conjonctivite allergique'],
        ]), 35))
PTS.append(POINT(1, 'Définition et sémantique', p1))

p2 = (P('Dans une méta-analyse internationale, la xérostomie touche ≈ 22 % de la population générale adulte. '
        'Le syndrome de Sjögren primaire est bien plus rare : ≈ 61 cas pour 100 000 habitants, avec ≈ 10 femmes pour 1 homme. '
        'Aucune donnée suisse publiée n’a été trouvée ; les chiffres « Suisse » de l’original ont été retirés.', 38, 37) +
      F('Chiffres, terrain et histoire naturelle',
        TAB(['Donnée', 'Valeur', 'Portée'], [
         ['Xérostomie, population générale (méta-analyse européenne et mondiale)', '≈ 22 %', 'Hausse avec l’âge et le nombre de médicaments'],
         ['Sjögren primaire, prévalence', '≈ 61 / 100 000 habitants', 'Méta-analyse de 2015'],
         ['Rapport femmes/hommes', '≈ 10/1', 'Pic entre 40 et 60 ans'],
         ['Anticorps anti-SSA chez le Sjögren primaire', '≈ 50–70 %', 'Varie selon les cohortes'],
         ['Risque de lymphome non hodgkinien (Sjögren)', '≈ 19 fois la population générale', 'Facteur pronostique majeur'],
        ]) + P('La mortalité du Sjögren dépend surtout du lymphome et des atteintes systémiques ; le terrain à risque est la femme d’âge moyen.', 69, 70), 37, 38))
PTS.append(POINT(2, 'Épidémiologie (Suisse, puis Europe)', p2))

p3 = (P('La salive aqueuse provient surtout des parotides et des glandes sous-mandibulaires. Le parasympathique la commande : l’acétylcholine se fixe sur les récepteurs muscariniques M3. '
        'Le calcium intracellulaire ouvre des canaux à chlore ; l’eau suit par l’' + AQP + '. '
        'Tout ce qui bloque ce récepteur ou détruit les acini assèche la bouche.', 70) +
      F('Chaîne logique : de l’anatomie au traitement',
        TAB(['Étape', 'Ce qu’il faut comprendre'], [
         ['Anatomie', 'Trois paires de glandes majeures (parotides, sous-mandibulaires, sublinguales) et des centaines de glandes accessoires dans la lèvre.'],
         ['Physiologie', 'Pourquoi la salive compte : elle humidifie, tamponne l’acidité et protège l’émail ; on en produit ≈ 0,3–0,4 mL/min au repos.'],
         ['Physiopathologie', 'Dans le Sjögren, des lymphocytes infiltrent et détruisent les acini ; les anticholinergiques bloquent le récepteur M3 ; la radiothérapie détruit les acini.'],
         ['Clinique', 'D’où la bouche sèche, la dysphagie des aliments secs, les caries du collet et la sécheresse oculaire.'],
         ['Examens', 'On mesure la salive et les larmes, puis on cherche l’auto-immunité (anti-SSA, biopsie des glandes salivaires).'],
         ['Traitement', 'On retire la cause, on stimule la salive restante (pilocarpine) et on protège les dents.'],
        ]), 70) +
      F('Mécanisme, exploration et cible thérapeutique',
        TAB(['Mécanisme', 'Exploration', 'Cible thérapeutique'], [
         ['Blocage muscarinique (antidépresseurs, neuroleptiques, antimuscariniques vésicaux)', 'Revue des médicaments', 'Déprescription'],
         ['Infiltration lymphocytaire auto-immune (Sjögren)', 'Anti-SSA, biopsie des glandes salivaires accessoires', 'Stimulation salivaire, immunomodulation si atteinte systémique'],
         ['Atrophie post-radique', 'Anamnèse de radiothérapie cervicale', 'Prévention par radiothérapie épargnant les parotides'],
         ['Infiltration granulomateuse ou IgG4', 'Biopsie, IgG4 sériques, imagerie thoracique', 'Corticothérapie selon la cause'],
         ['Déshydratation vraie', 'Natrémie, osmolalité', 'Réhydratation'],
        ]), 70))
PTS.append(POINT(3, 'Physiopathologie', p3))

p4 = (P('Le médecin vérifie d’abord qu’il ne s’agit pas d’une vraie polyurie (diabète, hypercalcémie, défaut de vasopressine). '
        'Puis il cherche une cause médicamenteuse, la plus fréquente en pratique. '
        'Enfin, il distingue le Sjögren des autres infiltrations des glandes salivaires.', 35, 70) +
      DIFF('xero') +
      F('Diagnostic différentiel de la sécheresse buccale (probabilités en exposant rouge)',
        TAB(['Diagnostic', 'Éléments d’orientation', 'Examen discriminant'], [
         ['Xérostomie, toutes causes' + PR('≈ 22 % des adultes', 38), 'Plainte de bouche sèche', 'Débit salivaire non stimulé'],
         ['Syndrome de Sjögren primaire' + PR('≈ 0,06 % des habitants', 37), 'Femme, yeux secs, parotides', 'Anti-SSA, biopsie'],
         ['Cause médicamenteuse', 'Anticholinergiques, diurétiques, opioïdes', 'Amélioration à l’arrêt (fréquence chiffrée non publiée)'],
         ['Sarcoïdose (syndrome de Heerfordt)', 'Parotidite, uvéite, paralysie faciale', 'Radiographie du thorax, biopsie'],
         ['Hépatite C, VIH', 'Facteurs de risque', 'Recherche d’anticorps et de virus'],
         ['Maladie associée aux IgG4', 'Glandes sous-mandibulaires dures', 'IgG4 sériques, biopsie'],
        ]) + P('Seules les deux premières lignes disposent d’une prévalence publiée ; les autres causes n’ont pas de fréquence comparable.', 37, 38), 70))
PTS.append(POINT(4, 'Raisonnement clinique et diagnostic différentiel', p4))

p5 = (P('L’anamnèse confirme d’abord l’absence de polyurie. Elle liste ensuite tous les médicaments, car leur effet anticholinergique s’additionne. '
        'Elle recherche enfin les signes d’une maladie générale.', 70) +
      U('Drapeaux rouges : tuméfaction parotidienne dure et persistante, adénopathies, purpura, cryoglobulinémie ou complément bas chez un patient Sjögren. Ils font craindre un lymphome et imposent un avis spécialisé sans délai ; une hospitalisation immédiate n’est nécessaire qu’en cas d’urgence systémique.', 69, 70) +
      F('Questions ciblées et leur raison',
        TAB(['Question', 'Pourquoi la poser'], [
         ['Urinez-vous plus de 2,5 L par jour, la nuit aussi ?', 'Une polyurie oriente vers une vraie polydipsie.'],
         ['Pouvez-vous avaler un biscuit sec sans boire ?', 'Le « signe du biscuit » objective l’hyposialie.'],
         ['Avez-vous du sable dans les yeux ?', 'La xérophtalmie oriente vers un Sjögren.'],
         ['Quels médicaments prenez-vous ?', 'Antidépresseurs tricycliques, neuroleptiques et antimuscariniques vésicaux bloquent la salive.'],
         ['Avez-vous reçu une radiothérapie du cou ?', 'C’est un critère d’exclusion du Sjögren.'],
         ['Avez-vous des douleurs articulaires, un purpura, des glandes gonflées ?', 'Ce sont des atteintes systémiques ou des signes de lymphome.'],
        ]), 35, 70))
PTS.append(POINT(5, 'Anamnèse ciblée et drapeaux rouges', p5))

p6 = (P('L’examen inspecte la bouche à la lampe. À l’état normal, un lac de salive se trouve sous la langue et la muqueuse brille. '
        'Les signes ont une sensibilité et une spécificité modestes ; la mesure du débit salivaire les complète.', 70) +
      F('Signes, technique et valeur',
        TAB(['Signe', 'Technique', 'Ce qu’il signifie'], [
         ['Absence de lac salivaire', 'Inspecter le plancher buccal langue relevée', 'Hyposialie'],
         ['Langue dépapillée, fissurée', 'Inspection', 'Sécheresse chronique'],
         ['Caries du collet', 'Inspection des dents', 'Perte de la protection salivaire'],
         ['Perlèche, muguet', 'Inspection des commissures', 'Candidose favorisée par la sécheresse'],
         ['Parotides augmentées de volume', 'Palpation bimanuelle', 'Sjögren ; dure et asymétrique : lymphome'],
         ['Abaisse-langue qui colle à la muqueuse', 'Appliquer puis retirer', 'Sécheresse marquée'],
        ]), 70))
PTS.append(POINT(6, 'Examen clinique', p6))

p7 = (P('Deux syndromes dominent. Le syndrome sec associe bouche et yeux secs ; il évoque un Sjögren. '
        'Le syndrome anticholinergique associe bouche sèche, mydriase, tachycardie, constipation et rétention d’urine ; il évoque un médicament.', 70) +
      F('Signes fonctionnels (symptômes rapportés)', UL(['Bouche sèche, soif sans polyurie', 'Gêne à avaler les aliments secs', 'Brûlures buccales, goût altéré', 'Yeux qui piquent, sensation de sable', 'Fatigue, douleurs articulaires (Sjögren)']), 70) +
      F('Signes physiques (constatés à l’examen)', UL(['Absence de lac salivaire', 'Caries du collet', 'Parotides augmentées de volume', 'Purpura des jambes (vascularite)', 'Mydriase et tachycardie (anticholinergiques)']), 70) +
      F('Syndrome sec (Sjögren)',
        TAB(['Signe', 'Mécanisme', 'Valeur'], [
         ['Xérostomie', 'Destruction des acini salivaires', 'Constante'],
         ['Xérophtalmie', 'Atteinte des glandes lacrymales', 'Test de Schirmer'],
         ['Arthralgies, fatigue', 'Activation immunitaire', 'Fréquentes'],
        ]), 70) +
      F('Syndrome anticholinergique',
        TAB(['Signe', 'Mécanisme', 'Valeur'], [
         ['Bouche sèche', 'Blocage M3 salivaire', 'Réversible à l’arrêt'],
         ['Mydriase, vision floue', 'Blocage M3 de l’iris et du muscle ciliaire', 'Risque de glaucome par fermeture de l’angle'],
         ['Rétention d’urine, constipation', 'Blocage de la vessie et de l’intestin', 'Surtout chez l’homme âgé'],
        ]), 70))
PTS.append(POINT(7, 'Syndromes et signes cliniques', p7))

p8 = (P('Le critère de classification ACR/EULAR 2016 du Sjögren primaire s’applique à un patient qui a une sécheresse oculaire ou buccale. '
        'Il additionne cinq éléments ; un total ≥ 4 points classe le patient, avec une sensibilité de 96 % et une spécificité de 95 %. '
        'La sécheresse seule ne suffit pas.', 35) +
      F('Critères de classification ACR/EULAR 2016',
        TAB(['Élément', 'Seuil', 'Points'], [
         ['Biopsie des glandes salivaires accessoires', FS + ' ≥ 1 foyer / 4 mm²', '3'],
         ['Anticorps anti-SSA (Ro)', 'Positifs', '3'],
         ['Score de coloration oculaire', '≥ 5 (ou van Bijsterveld ≥ 4) dans au moins un œil', '1'],
         ['Test de Schirmer', '≤ 5 mm en 5 minutes dans au moins un œil', '1'],
         ['Débit salivaire non stimulé', '≤ 0,1 mL/min (≤ 1,5 mL en 15 minutes)', '1'],
        ]) + P('Exclusions : radiothérapie cervicale, hépatite C active, sida, sarcoïdose, amylose, réaction du greffon contre l’hôte, maladie à IgG4.', 35)))
PTS.append(POINT(8, 'Critères diagnostiques', p8))

p9 = (H4('9.a Examen de référence') +
      P('Il n’existe pas d’examen de référence unique : la classification combine anti-SSA et biopsie des glandes salivaires accessoires. '
        'Ensemble, les critères ACR/EULAR atteignent une sensibilité de 96 % et une spécificité de 95 %.', 35) +
      H4('9.b Examens de première et de deuxième intention') +
      P('En première intention : débit salivaire, test de Schirmer, anticorps antinucléaires, anti-SSA et anti-SSB, électrophorèse des protéines, glycémie. '
        'En deuxième intention : biopsie des glandes salivaires accessoires si les anticorps sont négatifs, échographie des glandes salivaires, complément et cryoglobulines.', 35, 70) +
      TAB(['Intention', 'Examen', 'Pourquoi'], [
       ['1re', 'Débit salivaire non stimulé et test de Schirmer', 'Objectivent la sécheresse'],
       ['1re', 'Anti-SSA et anti-SSB', 'Marqueurs du Sjögren (3 points si anti-SSA positifs)'],
       ['1re', 'Électrophorèse des protéines sériques', 'Hypergammaglobulinémie, pic monoclonal'],
       ['1re', 'Glycémie et natrémie', 'Exclure diabète et déshydratation vraie'],
       ['2e', 'Biopsie des glandes salivaires accessoires', 'Focus score si anticorps négatifs'],
       ['2e', 'Complément (C4) et cryoglobulines', 'Risque de lymphome'],
      ]) +
      H4('9.c Prescription') +
      P('Indication : sécheresse persistante > 3 mois sans cause médicamenteuse. Moment : à distance d’un épisode infectieux. '
        'Préparation : débit salivaire à jeun, sans parler ni fumer 1 heure avant ; arrêter les anticholinergiques si possible.', 35, 70) +
      H4('9.d Interprétation : normal, seuil, signification, conduite') +
      TAB(['Résultat', 'Signification', 'Conduite'], [
       ['Positif : anti-SSA présents et sécheresse objective', '≥ 4 points : Sjögren classé', 'Avis rhumatologique, bilan systémique'],
       ['Négatif : débit salivaire normal', 'Pas d’hyposialie objective', 'Revoir la respiration buccale et les médicaments'],
       ['Limite : anti-SSA isolés, sécheresse modérée', '3 points : non classé', 'Biopsie des glandes salivaires'],
       ['Discordant : anti-SSA négatifs, forte sécheresse', 'Sjögren séronégatif possible', 'Biopsie ; chercher IgG4, sarcoïdose, hépatite C'],
      ]) +
      H4('9.e Alternatives') +
      P('Grossesse : anti-SSA à doser, car ils menacent le cœur fœtal. Enfant : rare, avis pédiatrique. '
        'DFGe < 30 : pas de contre-indication aux examens. L’échographie des glandes salivaires évite l’iode ; l’IRM sert si une masse parotidienne est palpée.', 71, 70))
PTS.append(POINT(9, 'Examens complémentaires', p9))

p10 = (P('Si la diurèse est normale et la glycémie normale, la soif vient de la bouche, pas du sang. '
         'Le médecin révise alors l’ordonnance ; si la sécheresse persiste ou si les yeux sont secs, il oriente vers le bilan de Sjögren.', 70) +
       F('Arbre décisionnel : bouche sèche',
         OL(['Diurèse > 2,5 L/24 h ou glycémie élevée : vraie polydipsie, voir DX.1 et DX.9.',
             'Médicament anticholinergique : déprescrire et réévaluer en 4–6 semaines.',
             'Radiothérapie cervicale : xérostomie post-radique, soins dentaires et pilocarpine.',
             'Sécheresse persistante : débit salivaire, Schirmer, anti-SSA.',
             'Score ACR/EULAR ≥ 4 : Sjögren ; < 4 avec forte suspicion : biopsie.',
             'Parotide dure, purpura, complément bas : avis spécialisé rapide (lymphome).']), 35, 70))
PTS.append(POINT(10, 'Arbre décisionnel', p10))

fiche = FICHE([
  ['Parasympathomimétique : pilocarpine (Salagen®)', 'Agoniste des récepteurs muscariniques M3', 'Demi-vie ≈ 1 h', '5 mg 3–4 fois/j aux repas, maximum 30 mg/j ; évaluer après 3 mois', 'Sueurs (très fréquentes), nausées, mictions fréquentes', 'Asthme non contrôlé, iritis aiguë, glaucome par fermeture de l’angle', 'Bêtabloquants (troubles de conduction), anticholinergiques (effet opposé)'],
  ['Antipaludéen : hydroxychloroquine (Plaquenil®)', 'Inhibe la signalisation des récepteurs Toll endosomaux', 'Demi-vie de plusieurs semaines', '200–400 mg/j, ≤ 5 mg/kg de poids réel par jour ; durée prolongée', 'Rétinopathie (contrôle annuel après 5 ans), allongement du QT', 'Maculopathie connue', 'Médicaments allongeant le QT, digoxine'],
 ], 36)
p11 = (H4('11.A Buts : d’abord l’urgence (lymphome, vascularite grave), car elle seule menace la vie') +
       P('Le traitement soulage la sécheresse, protège les dents et les yeux, et dépiste tôt le lymphome.', 36) +
       TAB(['But', 'Cible chiffrée'], [
        ['Charge anticholinergique', 'Réduire le nombre de médicaments anticholinergiques à 0 si possible'],
        ['Soins dentaires', 'Contrôle dentaire tous les 6 mois, fluor topique'],
        ['Dépistage du lymphome', 'Examen et biologie tous les 6–12 mois'],
       ]) +
       H4('11.B Moyens et méthodes : forme compliquée en urgence, forme non compliquée en ambulatoire') +
       P('Les mesures non médicamenteuses passent en premier, car elles suffisent souvent : déprescription, gommes sans sucre, substituts salivaires, larmes artificielles sans conservateur. '
         'L’éducation porte sur l’hygiène dentaire et l’eau à petites gorgées. '
         'Une forme compliquée (vascularite grave, suspicion de lymphome) relève de l’urgence : avis spécialisé dans les 24 heures.', 36, 70) +
       F('Traitements selon la situation',
         TAB(['Situation', 'Traitement', 'Pourquoi'], [
          ['Sécheresse légère', 'Gommes sans sucre, substituts salivaires', 'Stimulation mécanique'],
          ['Sécheresse modérée à sévère avec glandes résiduelles', 'Pilocarpine', 'Stimule les acini restants'],
          ['Arthralgies, fatigue (Sjögren)', 'Hydroxychloroquine selon EULAR 2020', 'Effet modeste sur les douleurs articulaires'],
          ['Atteinte systémique grave (vascularite, neuropathie, pneumopathie)', 'Glucocorticoïdes, puis immunosuppresseur ou rituximab hors indication Swissmedic', 'Contrôle de l’inflammation'],
         ]), 36) +
       fiche +
       F('Situations particulières',
         TAB(['Situation', 'Particularité'], [
          ['Grossesse avec anti-SSA', 'Hydroxychloroquine recommandée ; échocardiographie fœtale répétée de 16–18 à 26 semaines (bloc auriculo-ventriculaire congénital)'],
          ['Personne âgée', 'Polymédication : revue systématique des anticholinergiques'],
          ['Enfant', 'Sjögren rare ; parotidites récidivantes'],
          ['Insuffisance rénale (DFGe < 30)', 'Hydroxychloroquine à dose réduite'],
          ['Insuffisance hépatique', 'Pilocarpine à dose réduite'],
         ]), 71, 55) +
       SOCIAL('Un arrêt de travail n’est en général pas nécessaire ; il peut l’être lors des poussées systémiques (durée non chiffrée dans les sources).',
              'La conduite est possible ; la pilocarpine peut gêner la vision de nuit (myosis).',
              'Les soins dentaires peuvent être pris en charge par l’assurance de base (OPAS art. 18, maladies des glandes salivaires), sur garantie préalable.') +
       P('Cette prise en charge dentaire suppose que les lésions soient inévitables malgré une hygiène correcte.', 76) +
       H4('11.C Surveillance et critères de sortie') +
       TAB(['Quand', 'Quoi'], [
        ['À 3 mois', 'Efficacité et tolérance de la pilocarpine ; arrêt si inefficace'],
        ['Tous les 6 mois', 'Contrôle dentaire, palpation des parotides et des ganglions'],
        ['Tous les 6–12 mois', 'Électrophorèse des protéines, complément, cryoglobulines'],
        ['Chaque année après 5 ans d’hydroxychloroquine', 'Examen ophtalmologique'],
        ['Critères de sortie du suivi rapproché', 'Sécheresse contrôlée, absence d’atteinte systémique ; le suivi reste annuel à vie'],
       ]) +
       H4('11.D Pronostic et recherche 2026') +
       P('La xérostomie médicamenteuse régresse le plus souvent à l’arrêt du médicament. Le Sjögren reste chronique ; son pronostic dépend du lymphome. '
         'En 2026, les essais de phase III de l’ianalumab (anti-récepteur BAFF) ont réduit l’activité de la maladie ; aucune autorisation Swissmedic n’est connue à la date du cours.', 69, 75))
PTS.append(POINT(11, 'Prise en charge', p11))

p12 = (P('La prévention vise surtout la xérostomie évitable : moins de médicaments anticholinergiques et radiothérapie qui épargne les parotides. '
         'La radiothérapie par modulation d’intensité garde une dose moyenne < 25 Gy sur au moins une parotide. '
         'Elle réduit la xérostomie de grade ≥ 2 à 12 mois de 74 % à 38 %.', 73, 74) +
       F('Prévention primaire, secondaire et tertiaire',
         TAB(['Niveau', 'Mesure'], [
          ['Primaire', 'Prescription prudente des anticholinergiques chez la personne âgée ; épargne parotidienne en radiothérapie'],
          ['Secondaire', 'Débit salivaire et anti-SSA devant une sécheresse persistante'],
          ['Tertiaire', 'Fluor, contrôles dentaires, dépistage du lymphome'],
         ]) + P('En Suisse, les soins dentaires liés au Sjögren peuvent relever de l’OPAS ; la garantie de l’assureur doit précéder les soins.', 76)))
PTS.append(POINT(12, 'Prévention', p12))

PTS.append(POINT(13, 'Points clés',
 P('Une soif sans polyurie vient souvent d’une bouche sèche. '
   'La première cause à chercher est un médicament anticholinergique. '
   'Le Sjögren se classe avec le score ACR/EULAR 2016 (≥ 4 points). '
   'Une parotide dure et persistante fait craindre un lymphome.', 35, 69)))

PTS.append(POINT(14, 'Pièges d’examen',
 TAB(['Piège', 'Ce qu’il faut répondre'], [
  ['Prendre une xérostomie pour une polydipsie', 'Mesurer la diurèse : < 2,5 L/24 h écarte une polyurie'],
  ['Oublier la grossesse chez une femme anti-SSA positive', 'Risque de bloc auriculo-ventriculaire congénital ; hydroxychloroquine et échocardiographie fœtale'],
  ['Classer un Sjögren après radiothérapie cervicale', 'C’est un critère d’exclusion'],
  ['Prescrire la pilocarpine à un asthmatique non contrôlé', 'Contre-indication'],
  ['Négliger une parotide dure', 'Avis rapide : lymphome possible'],
 ]) + P('Sous hydroxychloroquine, la récidive du bloc congénital passe de ≈ 18 % (données historiques) à 7,4 % chez les mères ayant déjà eu un enfant atteint.', 72)))

CTX = {'_prefixe': 'Devant une bouche sèche',
 'ssa': 'Des anti-SSA positifs apportent 3 points du score ACR/EULAR 2016 ; en grossesse, ils imposent une surveillance cardiaque fœtale.',
 'schirmer': 'Un débit salivaire ≤ 0,1 mL/min et un Schirmer ≤ 5 mm en 5 minutes valent chacun 1 point.',
 'bgsa': 'Un focus score ≥ 1 foyer/4 mm² apporte 3 points ; la biopsie se fait surtout si les anticorps sont négatifs.',
 'epp': 'Une hypergammaglobulinémie est fréquente ; un pic monoclonal fait chercher un lymphome.',
 'gly': 'Une glycémie normale écarte la soif du diabète.',
 'iono': 'Une natrémie normale écarte une déshydratation vraie.',
 'irm': 'L’IRM caractérise une masse parotidienne.'}
if __name__ == '__main__':
    produire(M, PTS, SOURCES, CTX)
