---
name: AgentB__Harnais_LOT130
description: Harnais mécanique de l'agent AgentB__Harnais_LOT130 (LOT 130) — collecte, index BM25, recherche suisse, mémoire, CP, squelette V0, contrôles, rapport, captures, santé. À utiliser avant toute recherche de preuve ou tout contrôle de forme.
---
# AgentB__Harnais_LOT130 — mode d'emploi (court)
Environnement VM cloud : `H=$PWD/Leona__Harnais_Agents` (après `bash $H/coeur/installer.sh`) ; `export HARNAIS_INSTANCE=$H/instances/AgentB__Harnais_LOT130 ; alias harnais=$H/coeur/bin/harnais`

**Le harnais ne rédige ni ne juge.** Il fait le travail mécanique ; la rédaction, le choix clinique et l'audit restent à l'agent et à l'auditeur.

| Besoin | Commande |
|---|---|
| Collecter + indexer une source (cache, SHA-256, robots, 2 s/domaine) | `harnais collecter --url URL --dx DX2 --titre "…" --annee 2026` ou `--depuis sources_DX2.json [--dossier-local preuves/sources]` |
| Passages par rubrique, triés rang suisse puis BM25 | `harnais chercher "BPCO exacerbation" --rubrique p11 --dx DX2 [--suisse] [--max-age-ans 10] [--tri suisse|rang|pertinence|date] [--retenir]` |
| Prise en charge (Suisse obligatoire) | `harnais pec "BPCO exacerbation" --dx DX2` → code 3 = REFUS (aucune source suisse) ; exception non suisse → `<span class="exception-non-suisse">` + justification |
| Mémoire (état, décisions, preuves) | `harnais memoire ajouter --type decision --cle DX2-ordre --valeur "…"` ; `memoire lister --type preuve` ; `memoire exporter` |
| Point de contrôle | `harnais cp sauver --note "DX2 p1–p7 faits"` ; `harnais cp verifier` |
| Squelette V0 (îlots, justifié, fenêtres popover/details) | `harnais squelette --lot 130 --dx 2 --titre "…" --sortie f.html` |
| Contrôles + rapport coloré | `harnais controler f.html [--liens]` → `rapports/*.rapport.html` (code 2 = non conforme) |
| 4 captures × mobile/desktop | `harnais captures f.html` → `captures/` |
| Santé (auto toutes les 5 min) | `harnais sante` ; n'agir que si `sante/ALERTE.json` existe |

Surveillance : `nohup $H/surveillance/boucle_sante.sh $H/instances/AgentB__Harnais_LOT130 >/dev/null 2>&1 &` en début de session ; Actions `harnais-sante-*.yml` à chaque push. Registre des sources suisses : `$H/registre/SOURCES_SUISSES.csv` (rangs 1 AIPS → 7 international ; 8 = index NEO, orientation seulement, jamais preuve).
Interdits : jamais main, PR, `LOT_Claude_Finaux/`, `harnais/`, ni `psychotherapie-personnelle-de-Vial/` ; aucun chiffre sans passage source ; contenu « non validé cliniquement ».
