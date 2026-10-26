#!/usr/bin/env python3
"""PROMPT DU PROJET — lecture seule (chmod 444, SHA-256 surveillé par harnais/dispositif/veille.py).
Usage : python3 harnais/prompt_projet.py   (affiche le prompt)   ·   --sha  (empreinte)
Toute modification exige l'ordre de Vial et la mise à jour de harnais/dispositif/prompt.sha256."""
import hashlib, sys
PROMPT = """PROJET — LOT_Claude_Finaux (Vial, 26.10.2026). Catalogue = 248 SSP (PROFILES 2023), jamais 256.
MISSION FILE G : LOT_001 → LOT_016, UN SEUL LOT ACTIF à la fois ; le LOT n+1 ne démarre que si le LOT n est ACHEVÉ (ACCEPTE déposé+mergé, ou REFUSE/BLOQUE consigné+mergé).
ENTRÉE : tableaux remplis par une autre IA (.cache/g_in/g_tables.json) : 10 DD + lignes vertes (jusqu'à 15 DD par LOT). La liste DX d'un LOT = lignes non vides du tableau, dans l'ordre du tableau (prévalence décroissante). Aucune modification de liste sans HELP.md motivé.
LIVRABLE PAR LOT : 1 Phase A (SSP + liste DX + tableau comparatif + algorithme) + N Phase B (un HTML par DD, N = 10 à 15). 100–200 Ko par fichier, bornes comprises ; > 200 Ko jamais. But : densité d'information, aucune notion omise.
ÉQUIPE PAR LOT : 2 rédacteurs (R1 : Phase A puis première moitié des DD ; R2 : seconde moitié) + 2 auditeurs indépendants (médical Opus : points 2,3,4,8,9,11,12 ; conformité/langue Sonnet : points 1,5,6,7,10,13,14). Le rédacteur n'est jamais l'auditeur. Phase B démarre en parallèle dès que la liste est connue.
SEUILS DE DÉPÔT : ≥ 90 %, zéro critique, question finale « oui », LOT complet, `python3 harnais/controle_lot.py verifier <dossier>` = CONFORME. Deux cycles d'audit au plus, puis REFUSE consigné, LOT suivant.
RÈGLES DE FOND : doses AIPS suisse seulement, texte lu via `python3 harnais/aips_texte.py <n°> --section <mot>` (jamais le Compendium) ; numéros Swissmedic lus, jamais déduits ; sources suisses/européennes lues et datées, sinon « À vérifier » ; PubMed via `python3 harnais/pubmed.py` ou MCP PubMed ; sources autorisées : harnais/SOURCES_AUTORISEES.md ; aucune dose, source, lien ou chiffre inventé ; aucune donnée personnelle ; ne jamais modifier /workspace/ssp/app.html.
RÉFÉRENCES : PROMPT_Casern/PROMPT_ULTIME_PRODUCTION_LOTS_V0.md (§9.1, §11–§16, §23) ; harnais/HARNAIS_OBLIGATOIRE.md ; harnais/ROUTAGE_MODELES.md.
DÉPÔT : LOT_Claude_Finaux/LOT_XXX/ (N HTML + MANIFESTE.json + audits/), branche prod/lot-XXX-final, PR, CI verte, fusion par commit de fusion. Aucun dépôt ailleurs.
ÉCHANGES AVEC VIAL : une ligne ; entre agents : concision maximale ; contenu des cours exclu de cette règle.
BLOCAGE SANS CONTOURNEMENT LÉGITIME : LOT_Claude_Finaux/ARRET.md, arrêt. Un LOT refusé n'est pas un blocage.
"""
if __name__ == "__main__":
    print(hashlib.sha256(PROMPT.encode()).hexdigest() if "--sha" in sys.argv else PROMPT)
