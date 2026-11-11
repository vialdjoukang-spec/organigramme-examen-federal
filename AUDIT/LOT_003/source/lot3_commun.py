# -*- coding: utf-8 -*-
"""Briques communes aux cours du LOT 3 (SSP G3 : soif excessive, polydipsie) : sources, différentiel commun, volet social suisse."""
import sys, os
sys.path.insert(0, '/workspace/audit_1_10/corriges/LOT_003/source/outils_local'); sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from gen_v7l import *
from src_lot3 import SOURCES
LOT_TITRE = 'LOT 3 · G3 · Soif excessive et polydipsie'
DOSSIER = 'corriges/LOT_003'
def META(pref, dx, court, long, fichier, statut_extra=''):
    return dict(pref=pref, dx=dx, court=court, long=long, dossier=DOSSIER, fichier=fichier, lot_titre=LOT_TITRE,
        sous_titre='PROFILES 2023 · SSP G3 · LOT 3 · Appel B · V7 · version AUDITÉE',
        statut=f'Cette version reprend la monographie {dx} du LOT 3 (export Google Docs V5, sans sources) et la convertit en structure V7 après audit médical et linguistique ; les sources ont été ajoutées par l’audit. {statut_extra}')

# Différentiel commun de la polyurie-polydipsie : une seule unité (prévalence pour 100 000 habitants) et une seule population (générale).
_DIFF = [
 ('dm', 'Diabète sucré (toutes formes)', ('≈ 6200 / 100 000', 2), 'Polyurie osmotique, glycosurie, amaigrissement', 'Glycémie, HbA1c'),
 ('mrc', 'Maladie rénale chronique (tous stades)', ('≈ 10 400 / 100 000', 45), 'Nycturie, urines peu concentrées (isosthénurie)', 'Créatinine et DFGe, albuminurie'),
 ('ic', 'Insuffisance cardiaque (soif non osmotique)', ('1000–2000 / 100 000', 40), 'Œdèmes, dyspnée, hyponatrémie de dilution', 'NT-proBNP, échocardiographie'),
 ('xero', 'Sécheresse buccale, toutes causes (soif sans polyurie)', ('≈ 22 000 / 100 000', 38), 'Diurèse normale, médicaments anticholinergiques', 'Débit salivaire, revue des médicaments'),
 ('hpt', 'Hyperparathyroïdie primaire (1re cause d’hypercalcémie)', ('85 (hommes) à 233 (femmes) / 100 000', 49), 'Lithiase, fatigue, constipation', 'Calcémie corrigée et PTH'),
 ('sjo', 'Syndrome de Sjögren primaire', ('≈ 61 / 100 000', 37), 'Yeux secs, parotides, femme de 40–60 ans', 'Anticorps anti-SSA, test de Schirmer'),
 ('avpd', 'Déficit en vasopressine (AVP-D, ancien diabète insipide central)', ('≈ 4 / 100 000', 26), 'Début brutal, nycturie, goût pour l’eau glacée', 'Copeptine stimulée'),
 ('avpr', 'Résistance à la vasopressine (AVP-R, néphrogénique)', ('non publiée en population générale', 51), 'Lithium au long cours, hypercalcémie, forme congénitale', 'Copeptine basale, lithémie'),
 ('pp', 'Polydipsie primaire', ('non publiée en population générale', 31), 'Trouble psychiatrique, conviction de « bien boire »', 'Natrémie basse-normale, copeptine stimulée'),
 ('iat', 'Diurèse iatrogène (diurétiques, gliflozines, perfusions)', ('non publiée en population générale', 54), 'Début après un nouveau médicament', 'Revue des médicaments, natriurèse'),
 ('hyperna', 'Déshydratation hypernatrémique (accès à l’eau limité)', ('non publiée en population générale', 32), 'Grand âge, démence, dépendance', 'Ionogramme, osmolalité'),
]
def DIFF(focus, titre=None):
    rows = []
    for k, nom, (val, s), ori, ex in _DIFF:
        n = f'<strong>{nom} (sujet traité ici)</strong>' if k in (focus if isinstance(focus, (list, tuple)) else [focus]) else nom
        rows.append([n + PR(val, s), ori, ex])
    return F(titre or 'Diagnostic différentiel (fréquences en exposant rouge, même unité : prévalence pour 100 000 habitants)',
      TAB(['Diagnostic et prévalence', 'Éléments d’orientation', 'Examen discriminant'], rows) +
      P('Ces chiffres sont des prévalences en population générale, adultes, Suisse quand une donnée suisse existe (diabète, maladie rénale), sinon Europe ou Amérique du Nord. '
        'Ils ne sont pas la probabilité d’un diagnostic chez un patient donné : chez un adulte qui boit trop, le diabète et les médicaments restent les premières hypothèses à vérifier.', 1, 3))

def SOCIAL(arret, conduite, lai='Une rente de l’assurance-invalidité (LAI) ne se discute qu’en cas d’incapacité de travail durable malgré le traitement.'):
    return H4('Volet social et assurantiel (Suisse)') + TAB(['Domaine', 'Ce qu’il faut savoir'], [
     ['Assurance obligatoire des soins (LAMal)', 'Elle prend en charge les examens et médicaments de la liste des spécialités, après franchise et quote-part ; la maladie relève de la LAMal, pas de l’assurance-accidents (LAA).'],
     ['Arrêt de travail', arret],
     ['Aptitude à conduire', conduite],
     ['Assurance-invalidité', lai],
    ]) + P('Les règles d’assurance et de conduite citées ici sont générales ; leur application dépend du dossier.', 56)

def FICHE(rows, *src):
    """Fiche médicament : classe, mécanisme (pharmacodynamie), pharmacocinétique, dose et durée, effets indésirables, contre-indications, interactions."""
    return F('Fiche médicament (classe, mécanisme, pharmacocinétique, dose AIPS, effets indésirables, contre-indications, interactions)',
      TAB(['Classe et molécule (®)', 'Mécanisme d’action', 'Pharmacocinétique', 'Dose et durée', 'Effets indésirables', 'Contre-indications', 'Interactions'], rows) +
      P('Les doses sont à vérifier dans l’information professionnelle suisse (AIPS, Swissmedic) avant toute prescription.', *(src + (55,))))
