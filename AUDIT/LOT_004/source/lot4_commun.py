# -*- coding: utf-8 -*-
"""Briques communes aux cours du LOT 4 (SSP G4 : fatigue, épuisement) : sources, différentiels communs, volet social suisse, fiche médicament."""
import sys, os
sys.path.insert(0, '/workspace/audit_1_10/corriges/LOT_004/source/outils_local'); sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from gen_v7l import *
from src_lot4 import SOURCES
LOT_TITRE = 'LOT 4 · G4 · Fatigue, épuisement'
DOSSIER = 'corriges/LOT_004'
def META(pref, dx, court, long, fichier, statut_extra=''):
    return dict(pref=pref, dx=dx, court=court, long=long, dossier=DOSSIER, fichier=fichier, lot_titre=LOT_TITRE,
        sous_titre='PROFILES 2023 · SSP G4 · LOT 4 · Appel B · V7 · version AUDITÉE',
        statut=f'Cette version reprend la monographie {dx} du LOT 4 (export Google Docs V5, sans sources) et la convertit en structure V7 après audit médical et linguistique ; les sources ont été ajoutées par l’audit. {statut_extra}')

# Tableau 1 — même unité (prévalence pour 100 000) et même population de référence (population générale adulte ; sexe ou âge précisés quand la source l'impose).
_DIFF = [
 ('dep', 'Dépression (symptômes modérés à graves, PHQ-9 ≥ 10)', ('≈ 9800 / 100 000 (≥ 15 ans, Suisse 2022)', 6)),
 ('saos', 'Syndrome d’apnées obstructives du sommeil modéré à sévère (IAH ≥ 15/h)', ('23 400 (femmes) à 49 700 (hommes) / 100 000 (40–85 ans, Lausanne)', 14)),
 ('mrc', 'Maladie rénale chronique (tous stades)', ('≈ 10 400 / 100 000 (adultes, Suisse)', 28)),
 ('hypo', 'Hypothyroïdie non diagnostiquée (fruste et avérée)', ('≈ 4940 / 100 000, dont ≈ 620 avérée (Europe)', 18)),
 ('fer', 'Anémie ferriprive', ('≈ 3000 / 100 000 femmes en âge d’avoir des règles (Europe)', 9)),
 ('cancer', 'Cancer diagnostiqué dans les 10 dernières années', ('≈ 2600 / 100 000 (Suisse, à vérifier)', 29)),
 ('ic', 'Insuffisance cardiaque', ('1000–2000 / 100 000 adultes (Europe)', 25)),
 ('emsfc', 'Encéphalomyélite myalgique / syndrome de fatigue chronique (EM/SFC)', ('≈ 680 / 100 000 (méta-analyse mondiale)', 35)),
 ('addison', 'Insuffisance surrénale primaire (maladie d’Addison)', ('≈ 10–14 / 100 000 (Europe)', 38)),
 ('mni', 'Fatigue post-infectieuse (après mononucléose à EBV)', ('non publiée en population générale', 22)),
]
_ORI = {
 'dep': ('Anhédonie, humeur triste, réveil précoce, idées suicidaires', 'PHQ-9 puis entretien selon la CIM-11'),
 'saos': ('Ronflement, apnées vues par le conjoint, somnolence, obésité', 'Polygraphie ou polysomnographie'),
 'mrc': ('Hypertension, diabète, nycturie, anémie normocytaire', 'Créatinine et DFGe, albuminurie'),
 'hypo': ('Frilosité, prise de poids, constipation, peau sèche', 'TSH puis T4 libre'),
 'fer': ('Règles abondantes, pâleur, dyspnée d’effort, ongles cassants', 'Hémogramme et ferritine'),
 'cancer': ('Perte de poids, sueurs nocturnes, âge > 50 ans, saignement', 'Examen complet, dépistages, imagerie ciblée'),
 'ic': ('Dyspnée d’effort, œdèmes, orthopnée, cardiopathie connue', 'NT-proBNP puis échocardiographie'),
 'emsfc': ('Malaise post-effort, sommeil non réparateur, > 6 mois', 'Diagnostic clinique d’exclusion (IOM 2015)'),
 'addison': ('Mélanodermie, hypotension, envie de sel, hyponatrémie', 'Cortisol et ACTH du matin, test au Synacthène'),
 'mni': ('Angine, adénopathies, fièvre récente, adolescent', 'Anticorps hétérophiles, sérologie EBV'),
}
def DIFF(focus, titre=None):
    rows = []
    foc = focus if isinstance(focus, (list, tuple)) else [focus]
    for k, nom, (val, s) in _DIFF:
        n = f'<strong>{nom} (sujet traité ici)</strong>' if k in foc else nom
        rows.append([n + PR(val, s), _ORI[k][0], _ORI[k][1]])
    return F(titre or 'Diagnostic différentiel de la fatigue (prévalences en exposant rouge, même unité : pour 100 000 habitants)',
      TAB(['Diagnostic et prévalence', 'Éléments d’orientation', 'Examen discriminant'], rows) +
      P('Ces chiffres sont des prévalences en population générale, en Suisse quand une donnée suisse existe, sinon en Europe. '
        'Ils ne sont pas la probabilité d’un diagnostic chez un patient fatigué : le tableau suivant donne cette probabilité dans une autre population.', 2, 6, 14))

def DIFF_FAT():
    """Tableau 2 — autre population (patients de premier recours consultant pour fatigue), autre unité (% de ces patients) : séparé et nommé."""
    rows = [
     ['Dépression' + PR('18,5 % (IC 95 % 16,2–21,0)', 2), 'Première cause identifiée'],
     ['Maladie somatique grave, toutes causes' + PR('4,3 % (IC 95 % 2,7–6,7)', 2), 'Insuffisance cardiaque, rénale, endocrinienne, infection'],
     ['Anémie' + PR('2,8 % (IC 95 % 1,6–4,8)', 2), 'Surtout chez la femme jeune'],
     ['Syndrome de fatigue chronique' + PR('< 2 %', 2), 'Diagnostic d’exclusion'],
     ['Cancer' + PR('0,6 % (IC 95 % 0,3–1,3)', 2), 'Rare, mais plus fréquent après 50 ans'],
     ['Aucune cause précise retrouvée' + PR('≈ 40–50 %', 4), 'Fatigue « idiopathique », suivie dans le temps'],
    ]
    return F('Probabilité d’une cause chez l’adulte qui consulte pour fatigue en premier recours (autre population, autre unité : % de ces patients)',
      TAB(['Cause et fréquence chez le patient fatigué', 'Commentaire'], rows) +
      P('La revue systématique de Stadje (2016) regroupe des études de médecine de famille. '
        'En Suisse, la Revue Médicale Suisse rapporte une étiologie identifiée chez 50–60 % des patients ; le reste est une fatigue sans cause retrouvée.', 2, 4))

def SOCIAL(arret, conduite, lai='Une rente de l’assurance-invalidité (LAI) ne se discute qu’en cas d’incapacité de travail durable malgré le traitement ; une détection précoce auprès de l’office AI est possible dès 30 jours d’incapacité.'):
    return H4('Volet social et assurantiel (Suisse)') + TAB(['Domaine', 'Ce qu’il faut savoir'], [
     ['Assurance obligatoire des soins (LAMal)', 'Elle prend en charge les examens et médicaments de la liste des spécialités, après franchise et quote-part ; la maladie relève de la LAMal, pas de l’assurance-accidents (LAA).'],
     ['Arrêt de travail', arret],
     ['Aptitude à conduire', conduite],
     ['Assurance-invalidité', lai],
    ]) + P('Les règles d’assurance et de conduite citées ici sont générales ; leur application dépend du dossier.', 41)

def FICHE(rows, *src):
    """Fiche médicament : classe, mécanisme (pharmacodynamie), pharmacocinétique, dose et durée, effets indésirables, contre-indications, interactions."""
    return F('Fiche médicament (classe, mécanisme, pharmacocinétique, dose AIPS, effets indésirables, contre-indications, interactions)',
      TAB(['Classe et molécule (®)', 'Mécanisme d’action', 'Pharmacocinétique', 'Dose et durée', 'Effets indésirables', 'Contre-indications', 'Interactions'], rows) +
      P('Les doses sont à vérifier dans l’information professionnelle suisse (AIPS, Swissmedic) avant toute prescription.', *(src + (40,))))
