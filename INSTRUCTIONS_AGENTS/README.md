# Instructions des agents de rédaction (V7-Tunder) — version 1.3

| Fichier | Agent | Série | Scripts |
|---|---|---|---|
| `instructions_agent_1.md` | Agent 1 — Grok 4.7 haute vitesse | LOT_227 à LOT_237 | `scripts_lots/agent_1/` |
| `instructions_agent_2.md` | Agent 2 — Grok 4.7 haute vitesse | LOT_238 à LOT_248 | `scripts_lots/agent_2/` |

**Règle n° 1, en tête de chaque fichier : silence total envers l'utilisateur.** Seuls trois cas autorisent un message (LOT terminé, série terminée, urgence), chacun en une seule ligne de 15 mots au plus. Toute autre sollicitation reçoit la réponse unique « Bien reçu ; je passe par Tunder. ». Tout est centralisé vers Tunder.

Règles communes (V7-Tunder §5) :
- Un seul agent par LOT. Chaque agent rédige seul l'Appel A, puis l'Appel B Parties 1 à 4 (cadence 2-3-2-3), cours par cours.
- Aucun audit par les agents de rédaction : l'audit est différé à la phase Tunder (seuil de 90 % avant le dépôt final dans `LOT_Finaux_Audités`).
- Dépôt des brouillons sur `lot/LOT_X`, dossier `LOTS/LOT_X/` ; plan B Drive « LOTS_Finaux avec statut ».
- Chaque agent n'utilise que ses deux scripts (`script_source.py`, `script_synchrone.py`), du code déterministe sans aucune IA.
- Chaque message autorisé est journalisé par `scripts_lots/common/compteur_tokens.py`.
- Après chaque LOT, l'agent coche son fichier de suivi ; en fin de série, il ouvre l'issue `[FIN DE SÉRIE] Agent N — LOT_x–y` avec l'étiquette `fin-de-serie`, jamais `audit-ok`.

`generer_instructions.py` régénère les deux fichiers à partir d'un modèle unique, pour qu'ils restent identiques hors numéro d'agent et série.
