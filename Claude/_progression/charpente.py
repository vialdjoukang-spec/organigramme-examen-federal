#!/usr/bin/env python3
"""CHARPENTE — génère tous les emplacements vides de la plateforme (CAHIER_ARCHITECTURE_v2, règle 0.1), zéro modèle.

Déterministe : les tables ci-dessous sont recopiées du cahier (parties 2, 3, 4, 5, 6, 7, 8) ; aucune donnée médicale.
Chaque fiche = un fichier JSON nommé par son identifiant ; chaque champ du gabarit présent avec « — ».
Les fiches déjà remplies sont préservées : seuls les champs encore « — » ou absents sont (ré)écrits (--force : tout réécrire).

Usage : python3 Claude/_progression/charpente.py [--force]
Sortie : Claude/_progression/donnees/{examens,pharmaco,psychiatrie,fondamentales}/<ID>.json + structure.json + gabarits.json
"""
import json, os, re, sys, unicodedata

ICI = os.path.dirname(os.path.abspath(__file__))
DON = os.path.join(ICI, 'donnees')
V = '—'

# ---------------------------------------------------------------- Partie 2 : référentiel des systèmes (figé)
SYSTEMES = [
    ('S1', 'Neurologie'), ('S2', 'Tête, cou, ORL, CMF et ophtalmologie'), ('S3', 'Cardiovasculaire'),
    ('S4', 'Respiratoire et thorax'), ('S5', 'Digestif et hépato-bilio-pancréatique'), ('S6', 'Néphro-urologique'),
    ('S7', 'Reproduction, gynéco-obstétrique et sénologie'), ('S8', 'Endocrino-métabolique et nutrition'),
    ('S9', 'Appareil locomoteur'), ('S10', 'Sang et immunité'), ('S11', 'Psychiatrie et sommeil'),
    ('S12', 'Peau et phanères'), ('T', 'Transversaux')]
NOM_SYS = dict(SYSTEMES)
COULEURS = {'normal': 'bleu', 'pathologie': 'rouge', 'traitement_systeme': 'vert', 'hors_systeme': 'violet',
            'non_medicamenteux': 'ocre', 'danger': 'orange'}

# ---------------------------------------------------------------- Partie 5 : neuf sous-onglets
SOUS_ONGLETS = [
    (1, 'Biologie médicale', 'Matrice', ['Sang et buvard', 'Moelle', 'Urines', 'LCR', 'Selles', 'Sérosités et synovial',
        'Respiratoire et ORL', 'Génital et fœto-maternel', 'Salive, sueur, calculs, peau'],
     'Discipline', ['Cytologie et hématologie', 'Hémostase', 'Biochimie', 'Immuno-hormonologie', 'Microbiologie', 'Pharmaco-toxicologie'],
     'un examen ou une lignée'),
    (2, 'Imagerie médicale', 'Système', None, 'Modalité', ['Radiographie', 'Échographie-Doppler', 'TDM', 'IRM', 'Médecine nucléaire',
        'Radiologie interventionnelle'], 'une modalité sur une région'),
    (3, 'Explorations fonctionnelles', 'Système', None, 'Condition', ['Repos', 'Effort', 'Provocation', 'Nycthémère-sommeil'], 'une exploration'),
    (4, 'Anatomie et cytologie pathologiques', 'Système', None, 'Prélèvement × technique', ['Biopsie', 'Pièce opératoire', 'Cytoponction', 'Cytologie'],
     'un prélèvement d\'un organe'),
    (5, 'Endoscopies diagnostiques', 'Système ou voie', None, 'Technique et prélèvements associés', ['Technique', 'Prélèvements associés'], 'une endoscopie'),
    (6, 'Allergologie clinique (in vivo)', 'Mécanisme', ['Immédiat IgE-médié', 'Retardé'], 'Allergène',
     ['Médicaments', 'Aliments', 'Venins', 'Produits de contraste', 'Pneumallergènes'], 'un type de test'),
    (7, 'Génétique médicale et génomique', 'Statut', ['Constitutionnel postnatal', 'Prénatal', 'Somatique tumoral'], 'Technique',
     ['Caryotype', 'FISH', 'ACPA', 'MLPA', 'NGS', 'PCR'], 'une indication génétique'),
    (8, 'Tests rapides au point de soin', 'Système', None, 'Technique', ['Immunochromatographie', 'Lecteur capillaire', 'Moléculaire rapide'],
     'un test et sa confirmation'),
    (9, 'Évaluations cognitives et psychométriques', 'Système', None, 'Mode', ['Hétéro-évaluation', 'Auto-évaluation'], 'un instrument ou une famille d\'échelles'),
]

# Partie 5.1 : adaptation du temps 2 (paramètre, normal, anomalie)
TEMPS2 = {1: ('Paramètre mesuré', 'Référence et unité', 'Écart et seuil'), 2: ('Structure examinée', 'Aspect normal', 'Signe élémentaire'),
          3: ('Mesure', 'Valeur normale (âge, sexe)', 'Profil anormal'),
          4: ('Examen : diagnostic ou indication ; anomalies recherchées', 'Architecture normale', 'Lésion élémentaire'),
          5: ('Segment', 'Muqueuse normale', 'Lésion, score'), 6: ('Test et allergène', 'Négatif valide', 'Seuil de positivité'),
          7: ('Gène ou région', 'Séquence de référence', 'Variant et sa classe'), 8: ('Cible', 'Négatif valide', 'Positif → confirmation obligatoire'),
          9: ('Score ou sous-score', 'Zone normale', 'Seuils de sévérité')}

# ---------------------------------------------------------------- Partie 7 : cartographie (recopiée ; [] = « — » affiché)
def L(s):
    return [x.strip() for x in s.split(' · ')] if s != V else []

CARTE = {
 1: {'S1': L("LCR : cytologie · LCR : protéines, albumine, glucose · LCR : lactates · LCR : PCR multiplex · LCR : auto-anticorps (NMDA, AQP4) · Vitamines B1 et B12 · Ammoniémie · Auto-anticorps onconeuronaux · Taux des antiépileptiques"),
     'S2': L("Prélèvement de gorge · Prélèvement oculaire · Prélèvements ORL : bactériologie et virologie · IgE spécifiques des pneumallergènes"),
     'S3': L("Troponines hypersensibles · BNP et NT-proBNP · Bilan lipidique · Hémocultures · ANCA · Digoxinémie et suivi des antiarythmiques"),
     'S4': L("Gaz du sang artériels · Alpha-1-antitrypsine · LBA et expectorations : cytologie · PCR Aspergillus · PCR respiratoires multiplex · Test de la sueur · Liquide pleural : critères de Light"),
     'S5': L("Bilan hépatique : ASAT, ALAT, PAL, GGT, bilirubine · TP et facteur V · Lipase · Albumine · Selles : parasitologie · Calprotectine fécale · Alpha-1-antitrypsine fécale · Sérologies des hépatites A à E · Sérologie cœliaque · Liquide d'ascite"),
     'S6': L("Créatinine, DFG, urée · Ionogramme : sodium et osmolalité · Ionogramme : potassium · Équilibre acide-base · ECBU · Protéinurie et albuminurie · Sédiment urinaire et cristallurie · Analyse des calculs · Complément · Anticorps anti-membrane basale glomérulaire"),
     'S7': L("hCG · FSH et LH · Œstradiol et progestérone · Testostérone · Spermogramme · Prélèvements vaginaux et lochies · Test de Kleihauer · Marqueurs sériques de la trisomie 21"),
     'S8': L("Glycémie et HbA1c · TSH, T4 libre, T3 libre · Cortisol et ACTH · Rénine et aldostérone · PTH · Vitamines D, B12, B9, B1 · Oligo-éléments · Acylcarnitines"),
     'S9': L("Calcium et phosphate · Phosphatases alcalines osseuses · CTX et PINP · Acide urique · CPK · Facteur rhumatoïde et anti-CCP · HLA-B27 · Liquide synovial : cytologie et cristaux"),
     'S10': L("Hémogramme : lignée rouge · Hémogramme : leucocytes et formule · Plaquettes · Frottis sanguin · Réticulocytes · Vitesse de sédimentation · TP, INR et TCA · Fibrinogène et D-dimères · Suivi biologique des anticoagulants · Ferritine et bilan martial · Hémolyse : haptoglobine, LDH, bilirubine · Myélogramme · Électrophorèse des protéines · Immunoglobulines G, A, M, E · Lymphocytes CD4 et CD8 · Sérologies VIH, VHB, VHC · Bilan prétransfusionnel"),
     'S11': L("Bilan initial du premier épisode psychiatrique · Bilan étiologique du delirium · Lithiémie et surveillance du lithium (TSH, calcium, créatinine) · Surveillance du valproate et de la carbamazépine · Surveillance de la clozapine (neutrophiles, troponine, CRP) · Bilan métabolique sous antipsychotique · Prolactine · Taux des antidépresseurs et antipsychotiques · Dépistage toxicologique urinaire et sanguin · Marqueurs de consommation d'alcool (CDT, PEth, GGT, VGM)"),
     'S12': L("Prélèvement mycologique · PCR herpès sur lésion"),
     'T': L("Marqueurs tumoraux · Toxicologie d'urgence")},
 2: {'S1': L("Radiographie et TDM du système nerveux central · IRM encéphalique et médullaire · Échographie transfontanellaire · Médecine nucléaire cérébrale · Neuroradiologie interventionnelle"),
     'S2': L("Radiographie et TDM des sinus, rochers et massif facial · Échographie et IRM cervico-faciales · Cytoponctions guidées"),
     'S3': L("Radiographie et TDM thorax-cœur · Coroscanner · Écho-Doppler des troncs supra-aortiques, des membres et des fistules · IRM cardiaque · Scintigraphie myocardique"),
     'S4': L("Radiographie du thorax · TDM thoracique haute résolution · Angio-TDM thoracique · Échographie pleurale · Scintigraphie de ventilation-perfusion · Ponction et biopsie guidées"),
     'S5': L("Échographie abdominale · Doppler porte · TDM abdomino-pelvienne · Bili-IRM · Biopsie guidée du foie et du pancréas"),
     'S6': L("Échographie rénale et vésicale · Uro-TDM · IRM rénale et prostatique · Scintigraphie rénale · Biopsie guidée du rein et de la prostate"),
     'S7': L("Échographie pelvienne et fœtale · Mammographie · IRM mammaire et pelvienne · Biopsie guidée du sein"),
     'S8': L("Échographie thyroïdienne · TDM des surrénales · IRM hypophysaire · Scintigraphies thyroïdienne, parathyroïdienne et MIBG · Ostéodensitométrie"),
     'S9': L("Radiographie standard et âge osseux · Échographie ostéo-articulaire · TDM ostéo-articulaire · IRM du rachis et des membres · Scintigraphie osseuse · Biopsie osseuse guidée"),
     'S10': L("Échographie ganglionnaire · TDM d'extension · TEP-TDM · IRM médullaire"),
     'S11': L("IRM cérébrale du premier épisode psychotique · Imagerie des troubles neurocognitifs (renvoi S1)"),
     'T': L("Imagerie pédiatrique · Imagerie oncologique · Imagerie des urgences : FAST, polytraumatisé")},
 3: {'S1': L("EEG de l'adulte, de l'enfant et du nouveau-né · Potentiels évoqués · Électroneuromyogramme"),
     'S2': L("Audiométrie · Vidéonystagmographie · Champ visuel automatisé · Pachymétrie cornéenne"),
     'S3': L("ECG · Holter ECG · Mesure ambulatoire de la pression artérielle · Épreuve d'effort · Échocardiographie transthoracique et transœsophagienne · Index de pression systolique et explorations vasculaires"),
     'S4': L("Spirométrie et test de réversibilité · Pléthysmographie · DLCO · Pressions respiratoires · Test de marche de 6 minutes · Oxymétrie nocturne · Test de provocation bronchique"),
     'S5': L("Manométrie œsophagienne et anorectale · pH-impédancemétrie · Temps de transit colique · Tests respiratoires (H. pylori, lactose)"),
     'S6': L("Débitmétrie · Cystomanométrie · Épreuves fonctionnelles rénales dynamiques"),
     'S7': L("Cardiotocographie · Explorations pelvi-périnéales"),
     'S8': L("Calorimétrie indirecte · Impédancemétrie · Épreuves dynamiques : Synacthène, HGPO, freinage"),
     'S9': L("Explorations motrices et posturales"),
     'S10': L("Capillaroscopie"),
     'S11': L("Polysomnographie [S1 S4] · Polygraphie ventilatoire nocturne [S1 S4] · Test itératif de latence d'endormissement · Test de maintien de l'éveil · Actimétrie · Agenda du sommeil · ECG sous psychotropes : QT · EEG en psychiatrie : delirium, catatonie, avant électroconvulsivothérapie"),
     'S12': L("Dermatoscopie")},
 4: {'S1': L("Biopsie de nerf, de muscle, de cerveau · Cytologie du LCR"),
     'S2': L("Cytoponction ganglionnaire et salivaire · Biopsie des glandes salivaires accessoires"),
     'S3': L("Biopsie myocardique · Biopsie d'artère temporale"),
     'S4': L("Cytologie du LBA et du liquide pleural · Biopsie de bronche, de poumon, de plèvre"),
     'S5': L("Biopsies digestives étagées · Pièces d'exérèse digestives · Cytoponction du pancréas"),
     'S6': L("Biopsie rénale : optique, immunofluorescence, électronique · Biopsie prostatique · Cytologie urinaire"),
     'S7': L("Biopsie du sein, de l'endomètre, du col · Frottis cervico-utérin"),
     'S8': L("Cytoponction thyroïdienne (Bethesda)"),
     'S9': L("Biopsie osseuse, synoviale, des tissus mous"),
     'S10': L("Biopsie ostéo-médullaire · Biopsie ganglionnaire"),
     'S12': L("Biopsie cutanée et immunofluorescence directe")},
 5: {'S1': [], 'S2': L("Endoscopie nasale et nasofibroscopie"), 'S3': [], 'S4': L("Bronchoscopie et brossage"),
     'S5': L("Œso-gastro-duodénoscopie · Coloscopie · Duodénoscopie et brossage biliaire · Écho-endoscopie"),
     'S6': L("Cystoscopie · Urétéroscopie"), 'S7': L("Hystéroscopie · Colposcopie"), 'S8': [],
     'S9': L("Arthroscopie diagnostique"), 'S10': []},
 6: {'S2': L("Prick-tests aux pneumallergènes"), 'S4': L("Tests cutanés aux allergènes respiratoires"),
     'S5': L("Tests cutanés et provocation orale alimentaires · Entérocolite induite par les protéines alimentaires"),
     'S10': L("Tests cutanés aux médicaments · Tests cutanés aux produits de contraste · Tests cutanés aux venins"),
     'S12': L("Tests épicutanés (patch-tests)")},
 7: {'S1': L("Panels de neurogénétique et expansions nucléotidiques"), 'S3': L("Panels des cardiomyopathies et des canalopathies"),
     'S5': L("Tests compagnons KRAS, NRAS, BRAF"), 'S6': L("Oncogénétique rénale et prostatique"),
     'S7': L("Dépistage prénatal non invasif · Caryotype fœtal et ACPA · MLPA du chromosome Y · BRCA1 et BRCA2"),
     'S8': L("Panels des maladies métaboliques"), 'S9': L("MLPA du gène SHOX et génétique osseuse"),
     'S10': L("Caryotype, FISH et NGS en onco-hématologie"),
     'S11': L("Pharmacogénétique des psychotropes (CYP2D6, CYP2C19) · Génétique du retard mental (X fragile, ACPA)")},
 8: {'S2': L("Test rapide du streptocoque A"), 'S4': L("Tests rapides grippe, SARS-CoV-2, VRS"), 'S6': L("Bandelette urinaire"),
     'S7': L("Test de grossesse urinaire"), 'S8': L("Glycémie capillaire"), 'S10': L("Tests rapides VIH, VHC, VHB"),
     'S11': L("Tests urinaires rapides des drogues · Éthylotest et alcoolémie"), 'T': L("CRP capillaire")},
 9: {'S1': L("Tests cognitifs de dépistage (MMSE, MoCA) · Bilan neuropsychologique · Épreuves exécutives (Go/No-Go)"),
     'S11': L("AMDP : examen psychopathologique standardisé · Dépression : dépistage et sévérité (PHQ-9, MADRS, HAM-D, GDS, EPDS) · Manie (YMRS) · Anxiété (GAD-7, HAM-A) · Trouble obsessionnel-compulsif (Y-BOCS) · Stress post-traumatique (PCL-5) · Troubles psychotiques (PANSS, BPRS) · Risque suicidaire · Addictions (AUDIT, Fagerström, CAGE) · TDAH (Conners enfant, ASRS adulte) · Troubles du spectre autistique (M-CHAT, ADOS) · Troubles des conduites alimentaires (SCOFF, EDE-Q) · Sommeil (Epworth, ISI, PSQI) · Delirium (CAM) · Personnalité · Capacité de discernement")},
}

# Classement lexical strict : un mot du titre nomme explicitement l'entrée ou l'axe ; sinon « — » (à attribuer par le rédacteur).
MOTS_PRIMAIRE = {
 1: [(r'\bLCR\b', 'LCR'), (r'Selles|fécale', 'Selles'), (r'urinaire|ECBU|Protéinurie|cristallurie', 'Urines'), (r'Myélogramme', 'Moelle'),
     (r'LBA|expectorations|respiratoires|gorge|\bORL\b', 'Respiratoire et ORL'), (r'pleural|ascite|synovial', 'Sérosités et synovial'),
     (r'vaginaux|lochies|Spermogramme', 'Génital et fœto-maternel'), (r'sueur|calculs|mycologique|sur lésion', 'Salive, sueur, calculs, peau'),
     (r'Hémo|sanguin|Gaz du sang', 'Sang et buvard')],
 7: [(r'prénatal|fœtal', 'Prénatal'), (r'compagnons|onco-hématologie', 'Somatique tumoral')],
}
MOTS_AXE = {
 1: [(r'PCR|Hémocultures|ECBU|Sérologie|bactériologie|parasitologie|mycologique|Prélèvement', 'Microbiologie'),
     (r'Hémogramme|Plaquettes|Frottis sanguin|Réticulocytes|Myélogramme|sédimentation', 'Cytologie et hématologie'),
     (r'\bTP\b|INR|TCA|Fibrinogène|D-dimères|anticoagulants', 'Hémostase'),
     (r'Taux des|Digoxinémie|toxicologique|Toxicologie|Lithiémie', 'Pharmaco-toxicologie')],
 2: [(r'Radiographie', 'Radiographie'), (r'Échographie|Écho-Doppler|Doppler|FAST', 'Échographie-Doppler'), (r'TDM|Coroscanner', 'TDM'),
     (r'IRM', 'IRM'), (r'Scintigraph|TEP|nucléaire', 'Médecine nucléaire'), (r'Biopsie|Ponction|Cytoponction|interventionnelle', 'Radiologie interventionnelle')],
 3: [(r'effort|marche', 'Effort'), (r'provocation|Synacthène|HGPO|freinage', 'Provocation'),
     (r'nocturne|Holter|ambulatoire|sommeil|Polysomnographie|latence|éveil|Actimétrie', 'Nycthémère-sommeil')],
 4: [(r'Biopsie', 'Biopsie'), (r'exérèse', 'Pièce opératoire'), (r'Cytoponction', 'Cytoponction'), (r'Cytologie|Frottis', 'Cytologie')],
 5: [(r'brossage', 'Prélèvements associés')],
 6: [(r'médicaments', 'Médicaments'), (r'alimentaires', 'Aliments'), (r'venins', 'Venins'), (r'contraste', 'Produits de contraste'),
     (r'pneumallergènes|allergènes respiratoires', 'Pneumallergènes')],
 7: [(r'Caryotype', 'Caryotype'), (r'FISH', 'FISH'), (r'ACPA', 'ACPA'), (r'MLPA', 'MLPA'), (r'NGS', 'NGS')],
 8: [(r'capillaire', 'Lecteur capillaire')],
}

ID_CAHIER = {'Lithiémie et surveillance du lithium (TSH, calcium, créatinine)': 'lithiemie'}  # exemple de la partie 8
STOP = {'de', 'du', 'des', 'et', 'la', 'le', 'les', 'l', 'd', 'a', 'au', 'aux', 'en', 'sous', 'par', 'sur', 'un', 'une', 'avant', 'chez', 'son'}


def slug(t, mots=5):
    t = re.sub(r'\[[^\]]*\]', '', t)
    t = re.sub(r'\s\(.*', '', t)
    t = unicodedata.normalize('NFKD', t.replace('œ', 'oe').replace('Œ', 'oe')).encode('ascii', 'ignore').decode().lower()
    w = [x for x in re.split(r'[^a-z0-9]+', t) if x and x not in STOP]
    return '-'.join(w[:mots])


def etiquettes(t):
    m = re.search(r'\[([^\]]+)\]', t)
    return m.group(1).split() if m else []


def classer(table, t):
    out = []
    for motif, val in table:
        if re.search(motif, t) and val not in out:
            out.append(val)
    return out or [V]

# ---------------------------------------------------------------- Gabarits
G_EXAMEN = {
 'entete': {'nom_exact': V, 'synonymes': V, 'prelevement_conditions': V, 'bon_usage_suisse': V},
 'temps1_indications': {'urgence_aigu': V, 'diagnostic_etiologie': V, 'depistage_pretherapeutique': V, 'suivi_surveillance': V, 'ne_pas_demander': V},
 'temps2_examen': [{'parametre': V, 'normal': V, 'anomalie': V, 'seuil_alerte': V}],
 # Bloc optionnel (Vial, 13.11.2026) : un paramètre calculé = formule, usage pratique, exemple résolu, source.
 'calculs': [{'nom': V, 'formule': V, 'a_quoi_ca_sert': V, 'exemple': V, 'source': V}],
 'temps3_interpretation': [{'entite_anormale_chiffree': V, 'associees_presentes': V, 'associees_a_rechercher': V, 'syndrome_anamnese': V,
                            'syndrome_status': V, 'confirmation': V, 'diagnostic': V, 'conduite': V}],
 'annexeA_pieges': {'lignes': [{'si': V, 'consequence': V}], 'mnemotechnique': V},
 'sources': [V],
}
STATION = {'n': 1, 'structure': V, 'structure_fonction': V, 'si_dereglement': V,
           'vite_dit_cafe': {k: V for k in ['V Vasculaire', 'I Infectieux', 'T Tumoral', 'D Dégénératif', 'I Iatrogène', 'T Traumatique',
                                             'C Congénital', 'A Auto-immun', 'F Fonctionnel']}}
TRAITEMENT = {'systeme': [{'classe_biochimique': V, 'classe_fonctionnelle': V, 'dci': V, 'marque': V, 'cible': V}],
              'hors_systeme': [{'dci': V, 'posologie_complete': V}],
              'non_medicamenteux': [{'procedure': V, 'indications': V, 'contre_indications': V}]}
G_CHAINE = {'normal': {'trajet': V, 'stations': [STATION]}, 'pathologies': [{'nom': V, 'station': V, 'traitement': TRAITEMENT}],
            'classes': [{'nom': V, 'cible': V}], 'sources': [V]}
G_CLASSE = {'classification_fonctionnelle': V, 'mnemotechnique': V,
            'bandes': [{'sous_classe': V, 'quand_la_choisir': V, 'chefs_de_file': [V]}], 'sources': [V]}
POSO = {'adulte': V, 'sujet_age': V, 'enfant': V, 'sexe': V, 'ir_dfg': V, 'ih_child_pugh': V, 'grossesse': V, 'allaitement': V}
G_MOLECULE = {'pourquoi_elle': V, 'indications': V, 'spectre': V,
              'pk': {'absorption': V, 'distribution': V, 'metabolisme': V, 'elimination': V, 'courbe_commentee': V},
              'pd': {'mecanisme': V}, 'posologie': POSO, 'pieges': [{'si': V, 'alors': V}], 'source': V}
G_MOLECULE_PSY = {**G_MOLECULE,
                  'pd': {'mecanisme': V, 'profil_receptoriel': {k: V for k in ['5-HT', 'NA', 'DA', 'H1', 'muscariniques', 'alpha1']},
                         'effets_indesirables_par_recepteur': [{'recepteur': V, 'effet': V}]},
                  'delai_titration': {'delai_action': V, 'titration': V},
                  'performance_par_profil': V,
                  'arret_sevrage_switch': {'schema_arret': V, 'syndrome_arret': V, 'switch': V},
                  'surveillance': {'biologie': V, 'ecg_qt': V, 'poids_metabolique': V, 'taux_plasmatique': V},
                  'posologie_par_age': {'enfant': V, 'adolescent': V, 'adulte': V, 'sujet_age': V, 'autorisation_suisse_par_age': V}}
AGES = ['Enfant', 'Adolescent', 'Adulte', 'Sujet âgé']
G_PATHO = {'criteres_cim10': {'criteres_principaux': [V], 'criteres_associes': [V], 'nombre_requis': V, 'duree': V,
                              'specifications': {'severite': V, 'syndrome_somatique': V, 'symptomes_psychotiques': V},
                              'exclusions': [V], 'termes_discriminants': [V], 'texte_source': 'descriptions cliniques', 'complement_recherche': V},
           'barre_traitement': {'psychotherapies_mesures': [{'type': V, 'indication': V, 'duree': V}], 'pharmacologie_psychiatrique': [V],
                                'hors_psychiatrie': [{'dci': V, 'posologie_complete': V}], 'mesures_legales_sociales': [V]},
           'ages': {a: {'presente': V, 'ce_que_lage_change': V} for a in AGES}, 'sources': [V]}
G_BLOC = {'pathologies': [V], 'sources': [V]}
G_SF = {'cadre_ensemble': V, 'entites': [V], 'liens_logiques': [V], 'ponts_cliniques': [V], 'sources': [V]}
G_CLASSE_PSY = {**G_CLASSE, 'matrice_profil_chef_de_file': [{'profil': V, 'chef_de_file': V, 'pourquoi': V, 'a_eviter_pourquoi': V}]}
G_CHAPITRE = {'rubriques': {}, 'sources': [V]}
GABARITS = {'examen': G_EXAMEN, 'chaine': G_CHAINE, 'classe': G_CLASSE, 'classe_psy': G_CLASSE_PSY, 'chapitre_psy': G_CHAPITRE, 'molecule': G_MOLECULE,
            'molecule_psy': G_MOLECULE_PSY, 'pathologie_psy': G_PATHO, 'bloc_psy': G_BLOC, 'fondamentale': G_SF}

# ---------------------------------------------------------------- Parties 3 et 4 : pharmacologie
COQUE = {'T-infectiologie': 'germe × site × terrain', 'S8': 'axes hormonaux', 'S10': 'lignées et cascade'}
DOMAINES_T = ['pediatrie', 'sujet-age', 'oncologie', 'urgences-toxicologie', 'infectiologie']
NOMS_T = {'pediatrie': 'Pédiatrie', 'sujet-age': 'Sujet âgé', 'oncologie': 'Oncologie', 'urgences-toxicologie': 'Urgences et toxicologie',
          'infectiologie': 'Infectiologie'}
# (chapitre, titre, sous-classes, molécules nommées par le cahier {sous-classe: [(slug, DCI)]})
CLASSES_PSY = [
 ('antidepresseurs', 'Antidépresseurs', ['ISRS', 'IRSNa', 'Tricycliques', 'IMAO', 'Antagonistes α2 (mirtazapine)', 'Bupropion', 'Agomélatine',
   'Trazodone', 'Vortioxétine', 'Eskétamine'],
  {'ISRS': [('sertraline', 'Sertraline')], 'Antagonistes α2 (mirtazapine)': [('mirtazapine', 'Mirtazapine')], 'Bupropion': [('bupropion', 'Bupropion')],
   'Agomélatine': [('agomelatine', 'Agomélatine')], 'Trazodone': [('trazodone', 'Trazodone')], 'Vortioxétine': [('vortioxetine', 'Vortioxétine')],
   'Eskétamine': [('esketamine', 'Eskétamine')]}),
 ('antipsychotiques', 'Antipsychotiques', ['1re génération', '2e génération', 'Formes retard injectables', 'Clozapine (classe à part : résistance)'],
  {'Clozapine (classe à part : résistance)': [('clozapine', 'Clozapine')]}),
 ('thymoregulateurs', 'Thymorégulateurs', ['Lithium', 'Valproate', 'Lamotrigine', 'Carbamazépine', 'Antipsychotiques à action thymique'],
  {'Lithium': [('lithium', 'Lithium')], 'Valproate': [('valproate', 'Valproate')], 'Lamotrigine': [('lamotrigine', 'Lamotrigine')],
   'Carbamazépine': [('carbamazepine', 'Carbamazépine')]}),
 ('anxiolytiques', 'Anxiolytiques', ['Benzodiazépines', 'Prégabaline', 'Hydroxyzine', 'ISRS en fond'],
  {'Prégabaline': [('pregabaline', 'Prégabaline')], 'Hydroxyzine': [('hydroxyzine', 'Hydroxyzine')]}),
 ('hypnotiques', 'Hypnotiques et chronobiotiques', ['Apparentés aux benzodiazépines (« Z »)', 'Mélatonine', 'Antagonistes de l\'orexine',
   'Antidépresseurs sédatifs'], {'Mélatonine': [('melatonine', 'Mélatonine')]}),
 ('psychostimulants', 'Psychostimulants et TDAH', ['Méthylphénidate', 'Amphétamines', 'Atomoxétine', 'Guanfacine'],
  {'Méthylphénidate': [('methylphenidate', 'Méthylphénidate')], 'Atomoxétine': [('atomoxetine', 'Atomoxétine')], 'Guanfacine': [('guanfacine', 'Guanfacine')]}),
 ('addictions', 'Addictions', ['Agonistes opioïdes (méthadone, buprénorphine)', 'Naltrexone', 'Acamprosate', 'Disulfirame', 'Nalméfène', 'Varénicline',
   'Substituts nicotiniques'],
  {'Agonistes opioïdes (méthadone, buprénorphine)': [('methadone', 'Méthadone'), ('buprenorphine', 'Buprénorphine')], 'Naltrexone': [('naltrexone', 'Naltrexone')],
   'Acamprosate': [('acamprosate', 'Acamprosate')], 'Disulfirame': [('disulfirame', 'Disulfirame')], 'Nalméfène': [('nalmefene', 'Nalméfène')],
   'Varénicline': [('varenicline', 'Varénicline')]}),
 ('sommeil-organique', 'Troubles du sommeil organiques', ['Traitements de l\'apnée (renvoi S4)', 'Traitements de la narcolepsie',
   'Traitements du syndrome des jambes sans repos'], {}),
]
PROFILS = {
 'antidepresseurs': ['Dépression avec syndrome somatique (mélancolique)', 'Dépression anxieuse', 'Dépression avec insomnie',
   'Dépression avec ralentissement ou hypersomnie', 'Dépression avec douleurs', 'Dépression avec symptômes psychotiques', 'Dépression du sujet âgé',
   'Dépression de la grossesse et du post-partum', 'Dépression avec comorbidité cardiaque', 'Dépression résistante'],
 'antipsychotiques': ['Psychose : premier épisode', 'Psychose : symptômes négatifs prédominants', 'Psychose : agitation aiguë', 'Psychose : résistance',
   'Psychose : risque métabolique', 'Psychose : QT long', 'Psychose : hyperprolactinémie', 'Psychose : sujet âgé et démence', 'Psychose : Parkinson',
   'Psychose : mauvaise observance'],
 'thymoregulateurs': ['Bipolaire : manie aiguë', 'Bipolaire : dépression bipolaire', 'Bipolaire : prévention', 'Bipolaire : cycles rapides',
   'Bipolaire : grossesse', 'Bipolaire : insuffisance rénale'],
 'anxiolytiques': ['Anxiété : aigu', 'Anxiété : chronique', 'Anxiété : sujet âgé', 'Anxiété : antécédent d\'addiction'],
 'hypnotiques': ['Sommeil : aigu', 'Sommeil : chronique', 'Sommeil : sujet âgé', 'Sommeil : antécédent d\'addiction'],
 'addictions': ['Addiction (substance : —) : sevrage', 'Addiction (substance : —) : maintien'],
}
CLASSES_S1 = [('antidementiels', 'Anti-démentiels', ['Inhibiteurs de l\'acétylcholinestérase', 'Mémantine'], {'Mémantine': [('memantine', 'Mémantine')]}),
              ('antiepileptiques', 'Antiépileptiques', ['Antiépileptiques thymorégulateurs'],
               {'Antiépileptiques thymorégulateurs': [('valproate', 'Valproate'), ('lamotrigine', 'Lamotrigine'), ('carbamazepine', 'Carbamazépine')]})]

# ---------------------------------------------------------------- Partie 4.1 : coque CIM-10
BLOCS = [('F00-F09', 'Troubles mentaux organiques, y compris symptomatiques'),
         ('F10-F19', 'Troubles mentaux et du comportement liés à l\'utilisation de substances psychoactives'),
         ('F20-F29', 'Schizophrénie, trouble schizotypique et troubles délirants'), ('F30-F39', 'Troubles de l\'humeur (affectifs)'),
         ('F40-F48', 'Troubles névrotiques, troubles liés à des facteurs de stress et troubles somatoformes'),
         ('F50-F59', 'Syndromes comportementaux associés à des perturbations physiologiques et à des facteurs physiques (dont F51 sommeil non organique)'),
         ('F60-F69', 'Troubles de la personnalité et du comportement chez l\'adulte'), ('F70-F79', 'Retard mental'),
         ('F80-F89', 'Troubles du développement psychologique'),
         ('F90-F98', 'Troubles du comportement et troubles émotionnels apparaissant habituellement durant l\'enfance et l\'adolescence'),
         ('F99', 'Trouble mental, sans précision')]
PATHOS = [('F32.2', 'Épisode dépressif sévère sans symptômes psychotiques', 'F30-F39')]  # seule ligne d'exemple du cahier (4.3)

# ---------------------------------------------------------------- Partie 6 : sciences fondamentales
DISC = [('anatomie', 'Anatomie'), ('embryologie-histologie', 'Embryologie et histologie'), ('physiologie', 'Physiologie'),
        ('biochimie-biologie-moleculaire', 'Biochimie et biologie moléculaire'), ('physiopathologie-generale', 'Physiopathologie générale')]
SF_T = [('genetique', 'Génétique'), ('immunologie', 'Immunologie'), ('microbiologie', 'Microbiologie'),
        ('biostatistique-epidemiologie', 'Biostatistique et épidémiologie')]
SF_S11 = [('neurobiologie', 'circuits-neurotransmetteurs', 'Neurobiologie des circuits et des neurotransmetteurs'),
          ('physiologie', 'sommeil', 'Chronobiologie et physiologie du sommeil'),
          ('psychologie', 'developpement', 'Psychologie du développement')]


# ================================================================ Génération
FICHES = {}


def P(type_, cible, pourquoi=V):
    return {'type': type_, 'cible': cible, 'pourquoi': pourquoi}


def ajoute(f):
    assert f['id'] not in FICHES, f['id']
    FICHES[f['id']] = f
    return f


def gen_examens():
    carte = []
    for n, nom, prim, prim_vals, axe, axe_vals, unite in SOUS_ONGLETS:
        bloc = {'n': n, 'titre': nom, 'entree_primaire': prim, 'valeurs_primaires': prim_vals or [c for c, _ in SYSTEMES],
                'axe_secondaire': axe, 'valeurs_axe': axe_vals, 'unite': unite, 'temps2': TEMPS2[n], 'systemes': []}
        for sysc, titres in CARTE[n].items():
            ids = []
            for t in titres:
                titre = re.sub(r'\s*\[[^\]]+\]', '', t)
                fid = f'EX-{n}-{sysc}-{ID_CAHIER.get(titre, slug(t))}'
                g = json.loads(json.dumps(G_EXAMEN))
                f = {'id': fid, 'module': 'examens', 'type': 'examen', 'titre': titre, 'sous_onglet': n, 'systeme': sysc,
                     'etiquettes': etiquettes(t), 'entree_primaire': classer(MOTS_PRIMAIRE[n], t) if n in MOTS_PRIMAIRE else [sysc],
                     'axe_secondaire': classer(MOTS_AXE.get(n, []), t), **g, 'passerelles': []}
                ajoute(f); ids.append(fid)
            bloc['systemes'].append({'code': sysc, 'nom': NOM_SYS[sysc], 'fiches': ids})
        carte.append(bloc)
    return carte


def molecule(sysc, chap, slug_m, dci, sous_classe, psy):
    g = json.loads(json.dumps(G_MOLECULE_PSY if psy else G_MOLECULE))
    return ajoute({'id': f'PH-{sysc}-{chap}-{slug_m}', 'module': 'pharmaco', 'type': 'molecule_psy' if psy else 'molecule', 'titre': dci,
                   'systeme': sysc, 'classe': f'PH-{sysc}-{chap}', 'sous_classe': sous_classe, **g, 'passerelles': []})


def classe(sysc, chap, titre, sous, mols, psy):
    g = json.loads(json.dumps(G_CLASSE))
    bandes = []
    for sc in sous:
        ids = [molecule(sysc, chap, s, d, sc, psy)['id'] for s, d in mols.get(sc, [])]
        bandes.append({'sous_classe': sc, 'quand_la_choisir': V, 'chefs_de_file': ids or [V]})
    g['bandes'] = bandes
    f = {'id': f'PH-{sysc}-{chap}', 'module': 'pharmaco', 'type': 'classe_psy' if psy else 'classe', 'titre': titre, 'systeme': sysc, **g, 'passerelles': []}
    if psy:
        f['matrice_profil_chef_de_file'] = [{'profil': p, 'chef_de_file': V, 'pourquoi': V, 'a_eviter_pourquoi': V} for p in PROFILS.get(chap, [V])]
    return ajoute(f)


def gen_pharmaco():
    arbre = []
    for sysc, nom in SYSTEMES:
        if sysc == 'S11':
            ids = [classe('S11', c, t, s, m, True)['id'] for c, t, s, m in CLASSES_PSY]
            arbre.append({'code': 'S11', 'nom': nom, 'coque': 'CIM-10, chapitre V (gabarit propre, partie 4)', 'chaines': [], 'classes': ids})
            continue
        domaines = [(f'PH-T-chaine-{d}', f'Transversaux · {NOMS_T[d]}', f'T-{d}') for d in DOMAINES_T] if sysc == 'T' else [(f'PH-{sysc}-chaine', nom, sysc)]
        chaines = []
        for fid, titre, cle in domaines:
            g = json.loads(json.dumps(G_CHAINE))
            ajoute({'id': fid, 'module': 'pharmaco', 'type': 'chaine', 'titre': titre, 'systeme': sysc,
                    'coque': COQUE.get(cle, 'trajet de ce qui circule dans le système'),
                    'justification_coque': V if cle not in COQUE else 'Système atypique : coque adaptée, chaîne gardée (partie 3).',
                    'nombre_stations': V, **g, 'passerelles': []})
            chaines.append(fid)
        ids = [classe(sysc, c, t, s, m, False)['id'] for c, t, s, m in CLASSES_S1] if sysc == 'S1' else []
        arbre.append({'code': sysc, 'nom': nom, 'coque': COQUE.get(sysc, 'trajet de ce qui circule dans le système'), 'chaines': chaines, 'classes': ids})
    return arbre


def gen_psy():
    blocs = []
    for code, titre in BLOCS:
        g = json.loads(json.dumps(G_BLOC))
        f = ajoute({'id': f'PS-{code}', 'module': 'psychiatrie', 'type': 'bloc_psy', 'titre': f'{code} · {titre}', 'systeme': 'S11',
                    'code_cim10': code, **g, 'passerelles': []})
        blocs.append({'id': f['id'], 'code': code, 'titre': titre, 'pathologies': []})
    for code, titre, bloc in PATHOS:
        g = json.loads(json.dumps(G_PATHO))
        ajoute({'id': f'PS-{code}', 'module': 'psychiatrie', 'type': 'pathologie_psy', 'titre': f'{code} {titre}', 'systeme': 'S11',
                'code_cim10': code, 'bloc': f'PS-{bloc}', **g, 'passerelles': []})
        next(b for b in blocs if b['code'] == bloc)['pathologies'].append(f'PS-{code}')
        FICHES[f'PS-{bloc}']['pathologies'] = [f'PS-{code}']
    ajoute({'id': 'PS-F51-G47', 'module': 'psychiatrie', 'type': 'chapitre_psy', 'titre': 'Sommeil · F51 (non organique) et G47 (organique)',
            'systeme': 'S11', 'etiquettes': ['S1', 'S4'], 'code_cim10': 'F51 · G47',
            'rubriques': {'F51 Troubles du sommeil non organiques': [V], 'G47 Troubles du sommeil organiques (étiquettes S1, S4)': [V]},
            'sources': [V], 'passerelles': []})
    ajoute({'id': 'PS-CADRE-CH', 'module': 'psychiatrie', 'type': 'chapitre_psy', 'titre': 'Cadre suisse', 'systeme': 'S11', 'code_cim10': V,
            'rubriques': {r: [V] for r in ['Capacité de discernement', 'Placement à des fins d\'assistance', 'Traitement sans consentement',
                                            'Directives anticipées']}, 'sources': [V], 'passerelles': []})
    blocs += [{'id': 'PS-F51-G47', 'code': 'F51 · G47', 'titre': 'Sommeil', 'pathologies': []},
              {'id': 'PS-CADRE-CH', 'code': 'CH', 'titre': 'Cadre suisse', 'pathologies': []}]
    ages = {a: [p for p in FICHES if FICHES[p]['type'] == 'pathologie_psy'] for a in AGES}
    return {'blocs': blocs, 'ages': ages}


def gen_sf():
    arbre = []
    for sysc, nom in SYSTEMES:
        if sysc == 'T':
            items = [(f'SF-T-{d}', t) for d, t in SF_T]
        elif sysc == 'S11':
            items = [(f'SF-S11-{d}-{n}', t) for d, n, t in SF_S11]
        else:
            items = [(f'SF-{sysc}-{d}', t) for d, t in DISC]
        for fid, t in items:
            g = json.loads(json.dumps(G_SF))
            ajoute({'id': fid, 'module': 'fondamentales', 'type': 'fondamentale', 'titre': t, 'systeme': sysc, **g, 'passerelles': []})
        arbre.append({'code': sysc, 'nom': nom, 'fiches': [i for i, _ in items]})
    return arbre


def lien(src, typ, cible, pourquoi=V, retour=False):
    if src not in FICHES or cible not in FICHES:
        raise SystemExit(f'passerelle impossible : {src} → {cible}')
    p = P(typ, cible, pourquoi)
    if p not in FICHES[src]['passerelles']:
        FICHES[src]['passerelles'].append(p)
    if retour:
        lien(cible, typ, src, pourquoi)


def ex(n, sysc, debut):
    m = [i for i, f in FICHES.items() if f['type'] == 'examen' and f['sous_onglet'] == n and f['systeme'] == sysc and f['titre'].startswith(debut)]
    if len(m) != 1:
        raise SystemExit(f'examen introuvable ou ambigu : {n} {sysc} {debut} → {m}')
    return m[0]


def passerelles():
    exs = [f for f in FICHES.values() if f['type'] == 'examen']
    # Prélèvement : 2 Imagerie (geste guidé) et 5 Endoscopie → 4 Anapath du même système
    for f in exs:
        geste = (f['sous_onglet'] == 2 and 'Radiologie interventionnelle' in f['axe_secondaire']) or f['sous_onglet'] == 5
        if geste:
            for g in exs:
                if g['sous_onglet'] == 4 and g['systeme'] == f['systeme']:
                    lien(f['id'], 'Prélèvement', g['id'], 'prélèvement obtenu par ce geste')
    # Test compagnon : 4 Anapath → 7 Génétique somatique tumorale du même système
    for g in exs:
        if g['sous_onglet'] == 7 and 'Somatique tumoral' in g['entree_primaire']:
            for f in exs:
                if f['sous_onglet'] == 4 and f['systeme'] == g['systeme']:
                    lien(f['id'], 'Test compagnon', g['id'], 'si lésion tumorale')
    # Confirmation : 8 Test rapide positif → 1 Biologie (paires nommées par les deux titres)
    for (s, a), (s2, b) in [(('S2', 'Test rapide du streptocoque'), ('S2', 'Prélèvement de gorge')), (('S4', 'Tests rapides grippe'), ('S4', 'PCR respiratoires')),
                            (('S6', 'Bandelette urinaire'), ('S6', 'ECBU')), (('S6', 'Bandelette urinaire'), ('S6', 'Sédiment urinaire')),
                            (('S7', 'Test de grossesse'), ('S7', 'hCG')), (('S8', 'Glycémie capillaire'), ('S8', 'Glycémie et HbA1c')),
                            (('S10', 'Tests rapides VIH'), ('S10', 'Sérologies VIH')), (('S11', 'Tests urinaires rapides'), ('S11', 'Dépistage toxicologique')),
                            (('S11', 'Éthylotest'), ('S11', 'Dépistage toxicologique'))]:
        lien(ex(8, s, a), 'Confirmation', ex(1, s2, b), 'test rapide positif : confirmation obligatoire')
    # In vivo ↔ in vitro : 6 Allergologie (pneumallergènes) ↔ 1 IgE spécifiques des pneumallergènes
    ige = ex(1, 'S2', 'IgE spécifiques')
    for f in exs:
        if f['sous_onglet'] == 6 and 'Pneumallergènes' in f['axe_secondaire']:
            lien(f['id'], 'In vivo ↔ in vitro', ige, retour=True)
    # Sommeil : 3 Explorations S11 ↔ S1, S4
    for t in ['Polysomnographie', 'Polygraphie ventilatoire']:
        lien(ex(3, 'S11', t), 'Sommeil', ex(3, 'S4', 'Oxymétrie nocturne'), retour=True)
    for t in ['Polysomnographie', 'EEG en psychiatrie']:
        lien(ex(3, 'S11', t), 'Sommeil' if t == 'Polysomnographie' else 'Fondement', ex(3, 'S1', 'EEG'), retour=True)
    # Suivi thérapeutique : 1 Biologie, 3 ECG → fiche molécule ou classe
    for (s, t), cibles in [(('S11', 'Lithiémie'), ['PH-S11-thymoregulateurs-lithium']),
                           (('S11', 'Surveillance du valproate'), ['PH-S11-thymoregulateurs-valproate', 'PH-S11-thymoregulateurs-carbamazepine']),
                           (('S11', 'Surveillance de la clozapine'), ['PH-S11-antipsychotiques-clozapine']),
                           (('S11', 'Bilan métabolique'), ['PH-S11-antipsychotiques']), (('S11', 'Prolactine'), ['PH-S11-antipsychotiques']),
                           (('S11', 'Taux des antidépresseurs'), ['PH-S11-antidepresseurs', 'PH-S11-antipsychotiques']),
                           (('S1', 'Taux des antiépileptiques'), ['PH-S1-antiepileptiques-valproate', 'PH-S1-antiepileptiques-lamotrigine',
                                                                   'PH-S1-antiepileptiques-carbamazepine'])]:
        for c in cibles:
            lien(ex(1, s, t), 'Suivi thérapeutique', c, retour=True)
    for c in ['PH-S11-antipsychotiques', 'PH-S11-antidepresseurs']:
        lien(ex(3, 'S11', 'ECG sous psychotropes'), 'Suivi thérapeutique', c, retour=True)
    # Diagnostic psychiatrique : 9 Psychométrie S11 → bloc CIM-10 (intitulés de la partie 4.1)
    for t, cibles in [('Dépression', ['PS-F30-F39', 'PS-F32.2']), ('Manie', ['PS-F30-F39']), ('Anxiété', ['PS-F40-F48']),
                      ('Trouble obsessionnel', ['PS-F40-F48']), ('Stress post', ['PS-F40-F48']), ('Troubles psychotiques', ['PS-F20-F29']),
                      ('Addictions', ['PS-F10-F19']), ('TDAH', ['PS-F90-F98']), ('Troubles du spectre', ['PS-F80-F89']),
                      ('Troubles des conduites alimentaires', ['PS-F50-F59']), ('Sommeil', ['PS-F51-G47']), ('Delirium', ['PS-F00-F09']),
                      ('Personnalité', ['PS-F60-F69']), ('Capacité de discernement', ['PS-CADRE-CH'])]:
        for c in cibles:
            lien(ex(9, 'S11', t), 'Diagnostic psychiatrique', c)
    lien(ex(7, 'S11', 'Génétique du retard mental'), 'Diagnostic psychiatrique', 'PS-F70-F79')
    # Interfaces S1 ↔ S11 (partie 2) : passerelles, jamais fusion
    for m in ['valproate', 'lamotrigine', 'carbamazepine']:
        lien(f'PH-S1-antiepileptiques-{m}', 'Interface S1 ↔ S11', f'PH-S11-thymoregulateurs-{m}', 'même molécule, « pourquoi elle » propre', retour=True)
    lien('PS-F00-F09', 'Interface S1 ↔ S11', 'PH-S1-antidementiels', 'démence : pharmacologie spécifique en S1', retour=True)
    lien('PS-F51-G47', 'Interface S1 ↔ S11', 'PH-S11-sommeil-organique', retour=True)
    # Ligne de pathologie (4.3) : F32.2 → antidépresseurs (clic) ; bloc parent
    lien('PS-F32.2', 'Traitement', 'PH-S11-antidepresseurs', 'barre de traitement : pharmacologie psychiatrique')
    FICHES['PS-F32.2']['barre_traitement']['pharmacologie_psychiatrique'] = ['PH-S11-antidepresseurs']
    # Fondement : toute fiche → Sciences fondamentales du système
    for f in list(FICHES.values()):
        if f['module'] == 'fondamentales':
            continue
        s = f['systeme']
        cible = {'S11': 'SF-S11-physiologie-sommeil' if 'sommeil' in f['titre'].lower() or f['id'] == 'PS-F51-G47' else 'SF-S11-neurobiologie-circuits-neurotransmetteurs',
                 'T': 'SF-T-microbiologie' if f['id'] == 'PH-T-chaine-infectiologie' else ('SF-T-genetique' if f.get('sous_onglet') == 7 else 'SF-T-biostatistique-epidemiologie')}.get(s, f'SF-{s}-physiologie')
        lien(f['id'], 'Fondement', cible)
        if f.get('sous_onglet') == 7 and s != 'T':
            lien(f['id'], 'Fondement', 'SF-T-genetique')
        if f.get('sous_onglet') == 6:
            lien(f['id'], 'Fondement', 'SF-T-immunologie')


OPTIONNELS = ('calculs',)  # blocs de gabarit facultatifs : présents dans les fiches neuves, ajoutés à la main ailleurs


def fusion(ancien, neuf):
    """Garde ce qui est rempli dans l'ancien fichier ; complète les champs manquants par « — »."""
    if isinstance(neuf, dict) and isinstance(ancien, dict):
        return {k: fusion(ancien[k], v) if k in ancien else v for k, v in neuf.items()} | {k: v for k, v in ancien.items() if k not in neuf}
    return neuf if ancien == V or ancien in ('', None, [], {}) else ancien


def fusion_passerelles(ancien, neuf):
    """Fusion non destructive, dédoublonnée par (type, cible). Une fiche remplie (au moins un « pourquoi » rédigé)
    ne reçoit jamais de passerelle « — » de la charpente ; une entrée « — » cède devant la même (type, cible) rédigée."""
    def rempli(p):
        return p.get('pourquoi') not in (V, '', None)
    remplie = any(rempli(p) for p in ancien)
    sortie, index = [], {}
    for p in list(ancien) + [x for x in neuf if not remplie or rempli(x)]:
        k = (p.get('type'), p.get('cible'))
        if k not in index:
            index[k] = len(sortie); sortie.append(p)
        elif rempli(p) and not rempli(sortie[index[k]]):
            sortie[index[k]] = p
    return sortie


def ecrire():
    force = '--force' in sys.argv
    n = 0
    for fid, f in FICHES.items():
        d = os.path.join(DON, f['module'])
        os.makedirs(d, exist_ok=True)
        p = os.path.join(d, fid + '.json')
        if os.path.exists(p) and not force:
            f = fusion(json.load(open(p, encoding='utf-8')), f)
            ancien = json.load(open(p, encoding='utf-8'))
            for k in OPTIONNELS:  # un bloc optionnel n'est jamais injecté dans une fiche existante : elle reste intacte
                if k not in ancien:
                    f.pop(k, None)
            f['passerelles'] = fusion_passerelles(json.load(open(p, encoding='utf-8')).get('passerelles', []), FICHES[fid]['passerelles'])
        if os.path.exists(p):
            brut = open(p, encoding='utf-8').read()
            if json.loads(brut) == f:
                continue
            fin = '\n' if brut.endswith('\n') else ''
        else:
            fin = '\n'
        open(p, 'w', encoding='utf-8').write(json.dumps(f, ensure_ascii=False, indent=1) + fin); n += 1
    return n


if __name__ == '__main__':
    structure = {'version': 'cahier v2 · 13.11.2026', 'systemes': [{'code': c, 'nom': n} for c, n in SYSTEMES], 'couleurs': COULEURS,
                 'examens': gen_examens(), 'pharmaco': gen_pharmaco(), 'psychiatrie': gen_psy(), 'fondamentales': gen_sf(), 'ages': AGES}
    passerelles()
    gab = {k: v for k, v in GABARITS.items() if v is not None}
    os.makedirs(DON, exist_ok=True)
    for nom, obj in [('structure.json', structure), ('gabarits.json', gab)]:
        open(os.path.join(DON, nom), 'w', encoding='utf-8').write(json.dumps(obj, ensure_ascii=False, indent=1) + '\n')
    cpt = {}
    for f in FICHES.values():
        cle = f['module'] + (f' {f["sous_onglet"]}' if f['module'] == 'examens' else '')
        cpt[cle] = cpt.get(cle, 0) + 1
    print(f'{len(FICHES)} fiches ({ecrire()} écrites) · ' + ' · '.join(f'{k}: {v}' for k, v in sorted(cpt.items())))
