# Instructions des agents de rédaction (V7-Tunder) — version 1.4 (8 agents, 2 équipes)

| Fichier | Agent | Équipe | Chapitre | Série | Scripts | Dossier de travail |
|---|---|---|---|---|---|---|
| `instructions_agent_1.md` | Agent 1 | 1 | Appel A + Partie 1 (LOT_227–228 rédigés entiers) | LOT_227–237 | `scripts_lots/agent_1/` | `/workspace/agent1/` |
| `instructions_agent_3.md` | Agent 3 | 1 | Partie 2 (DX.3–DX.5) | LOT_229–237 | `scripts_lots/agent_3/` | `/workspace/agent3/` |
| `instructions_agent_5.md` | Agent 5 | 1 | Partie 3 (DX.6–DX.7) | LOT_229–237 | `scripts_lots/agent_5/` | `/workspace/agent5/` |
| `instructions_agent_7.md` | Agent 7 | 1 | Partie 4 (DX.8–DX.10) | LOT_229–237 | `scripts_lots/agent_7/` | `/workspace/agent7/` |
| `instructions_agent_2.md` | Agent 2 | 2 | Appel A + Partie 1 (LOT_238 et LOT_239 rédigés entiers ; LOT_239 déposé complet par l'Agent 2) | LOT_238–248 | `scripts_lots/agent_2/` | `/workspace/agent2/` (+ `/workspace/lots/` pour LOT_239) |
| `instructions_agent_4.md` | Agent 4 | 2 | Partie 2 (DX.3–DX.5) | LOT_240–248 | `scripts_lots/agent_4/` | `/workspace/agent4/` |
| `instructions_agent_6.md` | Agent 6 | 2 | Partie 3 (DX.6–DX.7) | LOT_240–248 | `scripts_lots/agent_6/` | `/workspace/agent6/` |
| `instructions_agent_8.md` | Agent 8 | 2 | Partie 4 (DX.8–DX.10) | LOT_240–248 | `scripts_lots/agent_8/` | `/workspace/agent8/` |

**Règle n° 1, en tête de chaque fichier : silence total envers l'utilisateur.** Trois cas seulement (fichier du LOT déposé, série terminée, urgence), chacun en une seule ligne de 15 mots au plus ; toute autre sollicitation reçoit « Bien reçu ; je passe par Tunder. ». Tout est centralisé vers Tunder.

**Loi fondamentale d'indépendance absolue, jusqu'au processus.** Chaque agent a ses scripts, sa configuration, son état (`~/.scripts_lots/agent_N/` : cache, retours, `etat/` des seaux de débit, compteur), son dossier de travail `/workspace/agentN/`, ses seuls fichiers Drive. Aucun message entre agents de rédaction ; aucune lecture des fichiers d'un autre agent, sauf l'Appel A V7 déposé sur Drive par l'agent Appel A de l'équipe, téléchargé et lu en lecture seule. `check` et `review` refusent (code 2) tout fichier hors du LOT, de la Partie ou du dossier de l'agent.

Flux :
1. Agent 1/2 : Appel A (déposé sur Drive dès qu'il passe `check`), puis Partie 1 ; un message à Tunder « LOT_X Appel A + Partie 1 déposés : <lien> » ; LOT suivant sans attendre.
2. Agents 3–8 : sources tant que l'Appel A du LOT n'est pas sur Drive ; puis leur Partie, avec la liste des DX reproduite à l'identique ; un message « LOT_X Partie N déposée : <lien> » ; LOT suivant.
3. Dépôt : dossier Drive « LOTS_Finaux avec statut » (`1DaFAd0uamsJQY2NH0ocuy2bhpfcVk9Vu`), sous-dossier existant dont le nom commence par `LOT_X` (créé seulement s'il n'existe pas), `text/html` sans conversion.
4. Tunder (agent `db322130-de1f-49d9-a669-bd9b54729c37`) resynchronise un LOT sur GitHub (`lot/LOT_X`, `LOTS/LOT_X/`) quand ses cinq fichiers V7 sont présents, coche tous les fichiers de suivi et ouvre les issues `[FIN DE SÉRIE] Agent N — LOT_a–b · <chapitre>` (étiquette `fin-de-serie`, jamais `audit-ok`).

Règles communes conservées (V7-Tunder §5) : aucun audit par les agents de rédaction (audit différé à Tunder, seuil de 90 %) ; rien sans source, sources suisses d'abord ; uniquement les deux scripts déterministes de l'agent, sans IA ; chaque message autorisé journalisé par `scripts_lots/common/compteur_tokens.py`.

`generer_instructions.py` régénère les huit fichiers à partir d'un modèle unique (`python3 generer_instructions.py`), pour qu'ils restent identiques hors numéro d'agent, équipe, chapitre et série.
