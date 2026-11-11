Nouvelle répartition du 24.10.2026 (11:00, Zurich) — remplace ORGANISATION_EQUIPES.md pour l'ordre de travail. LOT_219–248 hors plage.

# Répartition LOT_218 → LOT_1 (décision de l'utilisateur du 2026-10-24)

Travail **descendant**, sans chevauchement. LOT_219–248 : hors périmètre (déjà produits). Source : `scripts_lots/generer_configs.py` (configurations) et `instructions_agents/generer_instructions.py` (instructions).

| Agent | Équipe | Chapitre | Plage (ordre de traitement) | Nb LOT | Fichiers Appel A / Appel B (local V7) | Nom de dépôt Drive | Historique / exception |
|---|---|---|---|---|---|---|---|
| 1 | 1 | L'Appel A (plan et liste des 10 DX) et l'Appel B Partie 1 (DX.1 à DX.2) | LOT_218 → LOT_110 (218, 217, …, 110) | 109 | `LOT_X_Appel_A_V7_Plan_et_Liste.html` + `LOT_X_Appel_B_V7_Partie_1_DX.1_a_DX.2.html` | « Agent_1 \| LOT_X Appel A — Plan et liste des différentiels.html » + « Agent_1 \| LOT_X Partie 1 — <noms des différentiels>.html » | LOT_227, LOT_228 (entiers), LOT_229 (A + P1) : contrôle/relecture de l'existant, aucun nouveau travail |
| 3 | 1 | L'Appel B Partie 2 (DX.3 à DX.5) | LOT_218 → LOT_110 (218, 217, …, 110) | 109 | `LOT_X_Appel_B_V7_Partie_2_DX.3_a_DX.5.html` | « Agent_3 \| LOT_X Partie 2 — <noms des différentiels>.html » | — |
| 5 | 1 | L'Appel B Partie 3 (DX.6 à DX.7) | LOT_218 → LOT_110 (218, 217, …, 110) | 109 | `LOT_X_Appel_B_V7_Partie_3_DX.6_a_DX.7.html` | « Agent_5 \| LOT_X Partie 3 — <noms des différentiels>.html » | — |
| 7 | 1 | L'Appel B Partie 4 (DX.8 à DX.10) | LOT_218 → LOT_110 (218, 217, …, 110) | 109 | `LOT_X_Appel_B_V7_Partie_4_DX.8_a_DX.10.html` | « Agent_7 \| LOT_X Partie 4 — <noms des différentiels>.html » | — |
| 2 | 2 | L'Appel A (plan et liste des 10 DX) et l'Appel B Partie 1 (DX.1 à DX.2) | LOT_109 → LOT_1 (109, 108, …, 1) | 109 | `LOT_X_Appel_A_V7_Plan_et_Liste.html` + `LOT_X_Appel_B_V7_Partie_1_DX.1_a_DX.2.html` | « Agent_2 \| LOT_X Appel A — Plan et liste des différentiels.html » + « Agent_2 \| LOT_X Partie 1 — <noms des différentiels>.html » | LOT_238 (entier, historique) ; **LOT_239 : dépôt des Parties 3 et 4 déjà rédigées** ; LOT_1 : réutiliser l'Appel A V7 existant sur Drive après vérification |
| 4 | 2 | L'Appel B Partie 2 (DX.3 à DX.5) | LOT_109 → LOT_1 (109, 108, …, 1) | 109 | `LOT_X_Appel_B_V7_Partie_2_DX.3_a_DX.5.html` | « Agent_4 \| LOT_X Partie 2 — <noms des différentiels>.html » | — |
| 6 | 2 | L'Appel B Partie 3 (DX.6 à DX.7) | LOT_109 → LOT_1 (109, 108, …, 1) | 109 | `LOT_X_Appel_B_V7_Partie_3_DX.6_a_DX.7.html` | « Agent_6 \| LOT_X Partie 3 — <noms des différentiels>.html » | — |
| 8 | 2 | L'Appel B Partie 4 (DX.8 à DX.10) | LOT_109 → LOT_1 (109, 108, …, 1) | 109 | `LOT_X_Appel_B_V7_Partie_4_DX.8_a_DX.10.html` | « Agent_8 \| LOT_X Partie 4 — <noms des différentiels>.html » | — |

## Règles communes

- Numéros : `LOT_1` ≡ `LOT_01` ≡ `LOT_001` pour les scripts (1–99 acceptés avec ou sans zéros) ; sous-dossiers Drive « LOT_NNN — … » sur 3 chiffres, sous « LOTS_Finaux avec statut » (`1DaFAd0uamsJQY2NH0ocuy2bhpfcVk9Vu`).
- Fichiers locaux : noms V7 (exigés par `check`/`review`/`watch`) ; dépôt Drive : « Agent_N | LOT_X Appel A — Plan et liste des différentiels.html » / « Agent_N | LOT_X Partie K — <noms des différentiels>.html ».
- `LOT_N_SPEC.md` : lecture seule s'il existe ; fichiers `_A_REDIGER` (~1 Ko, LOT_217–226 notamment) : intacts.
- Dossier Drive `1sY8ed56jWj1su0imvX-dk6mVb_sGTFoB` : jamais ouvert.
- Crédo : « Être concis et faire preuve d'une précision fine avec élégance dans la formulation — être EXHAUSTIF dans le fond : les notions dans une formulation verbale claire, usage de fenêtres / mots cliquables interactifs pour les précisions complémentaires » ; obsession de la grille de validation en 14 parties (V7-Tunder §6/§6.1).

## Couverture

- Équipe 1 : LOT_218–110 = 109 LOT × 5 fichiers (Agent 1 : A + P1 ; Agent 3 : P2 ; Agent 5 : P3 ; Agent 7 : P4).
- Équipe 2 : LOT_109–1 = 109 LOT × 5 fichiers (Agent 2 : A + P1 ; Agent 4 : P2 ; Agent 6 : P3 ; Agent 8 : P4).
- Vérifié par `test_chaque_fichier_v7_a_exactement_un_proprietaire` (LOT_1–218, formes `LOT_n` et `LOT_00n`) et `test_lot_219_a_248_hors_perimetre_sauf_historique`.
