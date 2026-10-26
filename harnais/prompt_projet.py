#!/usr/bin/env python3
"""PROMPT DU PROJET — lecture seule (chmod 444, SHA-256 surveillé par harnais/dispositif/veille.py).
Usage : python3 harnais/prompt_projet.py   (affiche le prompt)   ·   --sha  (empreinte)
Toute modification exige l'ordre de Vial et la mise à jour de harnais/dispositif/prompt.sha256."""
import hashlib, sys
PROMPT = """PROJET — LOT_Claude_Finaux (Vial, 26.10.2026). Catalogue = 248 SSP (PROFILES 2023), jamais 256.
MISSION FILE G : LOT_001 → LOT_016, UN SEUL LOT ACTIF à la fois ; le LOT n+1 ne démarre que si le LOT n est ACHEVÉ (ACCEPTE déposé+mergé, ou REFUSE/BLOQUE consigné+mergé).
ENTRÉE : tableaux remplis par une autre IA (.cache/g_in/g_tables.json) : 10 DD + lignes vertes (jusqu'à 15 DD par LOT). La liste DX d'un LOT = lignes non vides du tableau, dans l'ordre du tableau (prévalence décroissante). Aucune modification de liste sans HELP.md motivé.
LIVRABLE PAR LOT : 1 Phase A (SSP + liste DX + tableau comparatif + algorithme) + N Phase B (un HTML par DD, N = 10 à 15). 100–200 Ko par fichier, bornes comprises ; > 200 Ko jamais. But : densité d'information, aucune notion omise.
ÉQUIPE PAR LOT : TOUJOURS 2 à 3 rédacteurs actifs (pool de 3 : Phase A en premier, puis les DD). AUCUN auditeur-modèle (zéro token d'audit) : le contrôle est fait par SCRIPTS du Harnais — `python3 harnais/audit_lot.py <LOT>` (contrôle médical d'ancrage : doses vs texte AIPS, PMID, structure §11 ; contrôle de langue LanguageTool + règles) puis AUDIT AVANT SORTIE `python3 harnais/audit_sortie.py <LOT>` (Harnais sain + forme + médical + langue), imposé par le hook git pre-commit. Les rapports MED_/CONF_ servent de CORRECTIONS aux rédacteurs.
SEUILS DE DÉPÔT : ≥ 90 %, zéro critique, question finale « oui », LOT complet, `python3 harnais/controle_lot.py verifier <dossier>` = CONFORME. Deux cycles d'audit au plus, puis REFUSE consigné, LOT suivant.
LOI DE NON-COLLISION ET D'INDÉPENDANCE TOTALE (PROMPT_Casern/ANTI_COLLISION_PARALLELISME_ABSOLU.md, adaptée) : un agent = un fichier assigné ; avant d'écrire : `python3 harnais/verrou.py claim <fichier> <ton_label>` (code 3 = STOP, ne pas écrire), après : `release` ; tu n'écris QUE ton fichier (rédacteur) ou ton rapport (auditeur) dans .cache/travail/LOT_XXX/ du LOT actif ; jamais un autre LOT, jamais PROMPT_Casern/, ETAT.md, HANDOFF.md, harnais/ (hors LECONS de ton rôle à la demande) ; notes partagées interdites (HELP.md → HELP_<ton_label>.md). Indépendance : un rédacteur ne contrôle jamais son propre fichier (contrôle = scripts) ; contexte vierge à chaque agent ; aucun score reporté d'un cycle à l'autre.
LEÇONS : au départ, lis harnais/LECONS/<ton rôle>.md (5 leçons au plus, issues des LOTS précédents) et applique-les.
CREDO (Vial) : EXHAUSTIVITÉ DANS UNE GRANDE DENSITÉ + CONCISION IMPORTANTE, SANS PERTE D'INFORMATION. Richesse sans superficialité ; discours droit au but quand c'est indiqué ; on comprime la FORME (phrases courtes, tableaux, termes interactifs, fenêtres <details> pour le détail), jamais le FOND.
RÈGLES DE FOND : doses AIPS suisse seulement, texte lu via `python3 harnais/aips_texte.py <n°> --section <mot>` (jamais le Compendium) ; numéros Swissmedic lus, jamais déduits ; sources suisses/européennes lues et datées, sinon « À vérifier » ; PubMed via `python3 harnais/pubmed.py` ou MCP PubMed ; sources autorisées : harnais/SOURCES_AUTORISEES.md ; aucune dose, source, lien ou chiffre inventé ; aucune donnée personnelle ; ne jamais modifier /workspace/ssp/app.html.
RÉFÉRENCES : PROMPT_Casern/PROMPT_ULTIME_PRODUCTION_LOTS_V0.md (§9.1, §11–§16, §23) ; harnais/HARNAIS_OBLIGATOIRE.md ; harnais/ROUTAGE_MODELES.md.
DÉPÔT : LOT_Claude_Finaux/LOT_XXX/ (N HTML + MANIFESTE.json + audits/), branche prod/lot-XXX-final, PR, CI verte, fusion par commit de fusion. Aucun dépôt ailleurs.
ÉCHANGES AVEC VIAL : une ligne ; entre agents : concision maximale ; contenu des cours exclu de cette règle.
BLOCAGE SANS CONTOURNEMENT LÉGITIME : LOT_Claude_Finaux/ARRET.md, arrêt. Un LOT refusé n'est pas un blocage.
"""
if __name__ == "__main__":
    print(hashlib.sha256(PROMPT.encode()).hexdigest() if "--sha" in sys.argv else PROMPT)
