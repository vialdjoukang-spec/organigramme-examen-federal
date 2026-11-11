# CONSTRUCTION DU PROJET — outils, scripts, compétences (état au 24.10.2026, 22 h, heure de Zurich)

L'archive **CONSTRUCTION_PROJET_outils_scripts.zip** (dans ce dossier) contient toute la construction du projet. Une fois décompressée, elle reproduit l'arborescence `/workspace/` de la machine de Tunder.

## 1. Chaîne d'audit V7 (Tunder) : `audit_1_10/`
- `outils/` contient la chaîne complète : `gen_v7.py` (génère le HTML V7) → `examens.py` / insertion des fenêtres d'examens cliquables (onglets Principe / Interprétation) → `mobile.py` → `sigles.py` (+ `sigles_add.py`) → `charte_v7plus.py` (couleurs : #C8102E sans halo, fond bleu ciel pâle) → `verif_v7.py` (les 14 points V7) → `score.py` (98,8 % au maximum ; le critère 13.b reste humain) → `contraste.py` (WCAG ≥ 4,5) → `style.py` (phrases de plus de 30 mots, points trop longs, sigles).
- Les autres fichiers de `outils/` (`decoupe.py`, `rapport.py`, `commun.py`, `run_lot.sh`) servent d'outils annexes.
- `bibliotheque_examens/` contient les fiches réutilisables des examens. Le fragment VIH contient une phrase incomplète à corriger.
- `corriges/LOT_00X/` contient les fichiers AUDITÉ, et `source/` contient les générateurs `gen_dxN.py`, `gen_ssp.py`, `eval.sh` et les registres de sources. On y trouve aussi `RAPPORT_AUDIT.md`, `MANIFEST.sha256` et `PROGRESS.md`, qui sert de journal de reprise.
- `verif_utilisateur/` contient la vérification de LOT_004 faite par Vial.
- `BRIEF_AUDIT_PARALLELE.md` est le brief d'audit. La compétence correspondante s'appelle « audit-lot-v7 ».
- Relancer un DX : `cd corriges/LOT_00X/source && bash eval.sh`.

## 2. Scripts des rédacteurs : `scripts_lots/`
- `equipes/` contient S1A.py, S1B.py, S2A.py et S2B.py, plus un README. Tous sont en lecture seule et n'émettent que des alertes.
  - S1A et S1B contrôlent les sources (sites accrédités, fiabilité).
  - S2A et S2B contrôlent les 14 points V7.
  - Un code de sortie 0 est la condition pour déposer.
- `agent_N/` contient la configuration de chaque agent. On y trouve aussi `common/`, `banc/` (le banc de tests) et `lancer_tests.sh` (57 tests, tous passent), ainsi que `generer_configs.py`.

## 3. Organisation des équipes : `equipes/`, `instructions_agents/`
- `EQUIPES_V1.6.md` et `DISPOSITIF_EQUIPES_V1.6.pdf` décrivent l'organisation : 6 équipes de 3 agents.
- `equipes/agent_N/` contient pour chaque agent `DEMARRER.md`, `ETAT.md` et `config.json`.
- `instructions_agents/instructions_agent_N.md` contient les instructions v1.6 de chaque agent.

## 4. Compétences gratuites et messages : `reorg/`
- `reorg/skills/` contient 4 compétences : performance-redaction-lot, concentration-fil-redaction, anti-gaspillage-redaction et harness-redacteur-v7. Elles sont prêtes mais **pas encore enregistrées** comme compétences.
- `reorg/messages_v1.6/` contient les messages de lancement envoyés aux 18 agents.

## 5. Référentiels
- `v7.md` et `v7_drive.md` : le prompt et la charte V7.
- `consigne_1535.txt` : les règles de cours de Vial du 24.10 à 15 h 35.
- `inventaire/` : l'inventaire Drive de LOT_001 à LOT_248, fait le 24.10 à 10 h 56.

## 6. Statut des LOTs
Voir **STATUT_LOTS_001_248** (Google Sheet, dans ce dossier). Il donne pour chaque LOT l'équipe, les responsables, les fichiers présents, le statut, la branche GitHub, la prochaine action et l'id du dossier Drive. Les dépôts y sont relevés sur Drive le 24.10 à 22 h 10.

**Règle anti-doublon** : avant de rédiger, relister le dossier Drive du LOT et sauter tout fichier déjà présent. Un LOT « ACHEVÉ V7 5/5 » ne se rédige plus : il passe à l'audit.
