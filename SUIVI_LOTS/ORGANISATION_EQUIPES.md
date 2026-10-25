# Organisation des équipes de rédaction — LOT_227 à LOT_248 (v1.4)

Depuis la réorganisation du 2026-10-24, **quatre agents rédigent chaque LOT**, chacun un chapitre strict, en deux équipes. LOT_227, LOT_228 (Agent 1), LOT_238 et LOT_239 (Agent 2) sont rédigés en entier par un seul agent ; l'Agent 2 dépose LOT_239 complet (5 fichiers V7) et le signale à Tunder par « LOT_239 terminé : <lien> ».

## Équipe 1 — LOT_229 à LOT_237

| Agent | Chapitre | Fichier par LOT | Suivi |
|---|---|---|---|
| Agent 1 | Appel A + Partie 1 (DX.1–DX.2) | `LOT_X_Appel_A_V7_Plan_et_Liste.html`, `LOT_X_Appel_B_V7_Partie_1_DX.1_a_DX.2.html` | `SUIVI_AGENT_1_LOT_227-237.md` |
| Agent 3 | Partie 2 (DX.3–DX.5) | `LOT_X_Appel_B_V7_Partie_2_DX.3_a_DX.5.html` | `SUIVI_AGENT_3_EQUIPE_1.md` |
| Agent 5 | Partie 3 (DX.6–DX.7) | `LOT_X_Appel_B_V7_Partie_3_DX.6_a_DX.7.html` | `SUIVI_AGENT_5_EQUIPE_1.md` |
| Agent 7 | Partie 4 (DX.8–DX.10) | `LOT_X_Appel_B_V7_Partie_4_DX.8_a_DX.10.html` | `SUIVI_AGENT_7_EQUIPE_1.md` |

## Équipe 2 — LOT_240 à LOT_248

| Agent | Chapitre | Fichier par LOT | Suivi |
|---|---|---|---|
| Agent 2 | Appel A + Partie 1 (DX.1–DX.2) | `LOT_X_Appel_A_V7_Plan_et_Liste.html`, `LOT_X_Appel_B_V7_Partie_1_DX.1_a_DX.2.html` | `SUIVI_AGENT_2_LOT_238-248.md` |
| Agent 4 | Partie 2 (DX.3–DX.5) | `LOT_X_Appel_B_V7_Partie_2_DX.3_a_DX.5.html` | `SUIVI_AGENT_4_EQUIPE_2.md` |
| Agent 6 | Partie 3 (DX.6–DX.7) | `LOT_X_Appel_B_V7_Partie_3_DX.6_a_DX.7.html` | `SUIVI_AGENT_6_EQUIPE_2.md` |
| Agent 8 | Partie 4 (DX.8–DX.10) | `LOT_X_Appel_B_V7_Partie_4_DX.8_a_DX.10.html` | `SUIVI_AGENT_8_EQUIPE_2.md` |

## Loi fondamentale d'indépendance absolue, jusqu'au processus

- Chaque agent a ses propres scripts (`scripts_lots/agent_N/`), sa configuration, son état d'exécution (`~/.scripts_lots/agent_N/` : cache, retours, seaux de débit `etat/`, compteur), son dossier de travail `/workspace/agentN/` et ses seuls fichiers Drive. Aucun fichier, verrou ni budget n'est commun à deux agents.
- Aucun agent de rédaction n'écrit à un autre. Seul interlocuteur : Tunder.
- **Seule dépendance** : les agents des Parties 2 à 4 lisent, en lecture seule, l'Appel A V7 du LOT déposé sur Drive par l'agent Appel A de leur équipe, pour reproduire à l'identique la liste des 10 DX. Tant qu'il n'existe pas, ils ne font que réunir des sources.
- Les scripts `check` et `review` refusent (code 2) tout fichier hors du LOT, de la Partie ou du dossier de travail de l'agent.

## Flux

1. L'Agent 1 (ou 2) rédige l'Appel A du LOT_X, le dépose sur Drive dès qu'il passe `check`, puis rédige et dépose la Partie 1 ; il envoie à Tunder une ligne « LOT_X Appel A + Partie 1 déposés : <lien> » et passe au LOT_X+1 sans attendre.
2. Chaque agent des Parties 2 à 4 dépose son fichier, envoie à Tunder une ligne « LOT_X Partie N déposée : <lien> » et passe au LOT suivant.
3. Dépôt : Drive « LOTS_Finaux avec statut » (`1DaFAd0uamsJQY2NH0ocuy2bhpfcVk9Vu`), sous-dossier existant dont le nom commence par `LOT_X`, `text/html` sans conversion.
4. Tunder resynchronise le LOT sur GitHub (`lot/LOT_X`, `LOTS/LOT_X/`) quand les cinq fichiers V7 sont présents, coche toutes les lignes de suivi et ouvre les issues de fin de série `[FIN DE SÉRIE] Agent N — LOT_a–b · <chapitre>` (étiquette `fin-de-serie`, jamais `audit-ok`).

## Issues de fin de série attendues

| Agent | Titre |
|---|---|
| 1 | `[FIN DE SÉRIE] Agent 1 — LOT_227–237 · Appel A + Partie 1` (LOT_227–228 entiers ; LOT_229–237 Appel A + Partie 1) |
| 2 | `[FIN DE SÉRIE] Agent 2 — LOT_238–248 · Appel A + Partie 1` (LOT_238–239 entiers ; LOT_240–248 Appel A + Partie 1) |
| 3 | `[FIN DE SÉRIE] Agent 3 — LOT_229–237 · Partie 2` |
| 4 | `[FIN DE SÉRIE] Agent 4 — LOT_240–248 · Partie 2` |
| 5 | `[FIN DE SÉRIE] Agent 5 — LOT_229–237 · Partie 3` |
| 6 | `[FIN DE SÉRIE] Agent 6 — LOT_240–248 · Partie 3` |
| 7 | `[FIN DE SÉRIE] Agent 7 — LOT_229–237 · Partie 4` |
| 8 | `[FIN DE SÉRIE] Agent 8 — LOT_240–248 · Partie 4` |

Un LOT est complet quand ses cinq fichiers V7 sont cochés : Appel A + Partie 1 (suivi de l'Agent 1 ou 2) et Parties 2, 3, 4 (suivis des trois autres agents de l'équipe).

Nouvelle répartition du 24.10.2026 (11:00, Zurich) — remplace ORGANISATION_EQUIPES.md pour l'ordre de travail. LOT_219–248 hors plage.
