#!/usr/bin/env python3
"""BRACELET (V5, harnais Claude) — sélecteur : une tâche → 1 à 3 outils LOCAUX du harnais, jamais les 19.
Reprend le principe de bracelet_suggest.py (agentA/lot-109) ; les 19 bibliothèques externes sont remplacées par
leurs équivalents gratuits déjà installés (décision détaillée dans RAPPORT_HARNAIS.html, section Bracelet).
Usage : python3 Claude/_harnais/bracelet.py "<tâche>"
"""
import re, sys, unicodedata

CAT = [  # (catégorie du Bracelet, mots-clés, outils du harnais)
 ('Filtrage avant lecture', r'lire|relire|cours|html|point|fenetre|extrait|audit', ['extrait.py plan|point|cherche', 'resumeur.py <LOT>']),
 ('Filtrage avant lecture (web)', r'source|web|recommandation|ssi|ssgie|esc|guideline|pmc|citation|chiffre', ['sources_cache.py index|cherche', 'sources_cache.py disjoncteur']),
 ('AIPS', r'aips|dose|posologie|grossesse|allaitement|contre-indic|swissmedic|molecule|medicament', ['aips_fiche.py trouve <nom>', 'aips_fiche.py fiche <url SmPC>', 'aips_fiche.py verifier <html>']),
 ('Mémoire persistante', r'reprise|reprendre|memoire|carnet|deja|etat|ou en est|relais|remplace', ['memoire_agent.py lire|note', 'cerveau.py cherche "<question>"', 'resumeur.py --global']),
 ('Réutilisation et cache', r'image|figure|schema|illustration|couleur', ['images_lot.py <LOT>', 'cliche.py']),
 ('Protection et observation', r'cout|gaspill|token|consommation|progression|surveill|budget', ['gaspillon.py', 'suivi.py', 'modele.py']),
 ('Portes avant audit', r'controle|\bporte|\brendre|\bpr\b|abreviation|sigle|avant audit', ['controle3.py --script-ok', 'aips_fiche.py verifier', 'abreviations.py']),
]


def norm(t):
    t = unicodedata.normalize('NFKD', t.lower()); return ''.join(c for c in t if not unicodedata.combining(c))


if __name__ == '__main__':
    q = norm(' '.join(sys.argv[1:]))
    if not q: print(__doc__); sys.exit(0)
    sc = sorted(((-len(re.findall(rx, q)), i) for i, (c, rx, o) in enumerate(CAT)))
    choix = [CAT[i] for n, i in sc if n][:3] or [CAT[3]]
    outils = ([c[2][0] for c in choix] + [o for c in choix for o in c[2][1:]])[:3]  # 1 outil par catégorie d'abord
    print(' · '.join(c[0] for c in choix) + '\n' + '\n'.join('  ' + o for o in outils))
