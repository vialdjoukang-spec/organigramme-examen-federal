---
name: ssp-pilotage-codex
description: Lis ce skill au début de chaque session Codex : porte des étapes, veille de relance, file de fusion, modèle des tâches répétitives.
---
# Pilotage par étapes (Codex)

1. **Début de session** : `python tools/garde/checkpoint.py --inventaire` (automates actifs, R15) ; `cat PROCHAINE_ACTION.md` ; `python3 tools/porte.py etat` ; lire la section « Étape N » de CONTINUATION.md.
2. **Porte** : `python3 tools/porte.py commencer N` (code 2 = Étape 0 incomplète : ne faire que l'Étape 0).
3. **Travail** : petits lots, une PR par lot, audit agressif aussitôt, label `audit-ok`. Tâche répétitive → modèle `gpt-6-luna` (ordre de Vial), sinon le moins cher, noté dans ETAT.md.
4. **Fin d'étape ou de lot** : tests, push, HANDOFF.md, ligne du journal des étapes d'ETAT.md, `python3 tools/propose_skills.py`, puis `python3 tools/porte.py terminer`. Boucle sans critère finie : `"fin_boucle": N` dans ETAT.json avant `terminer`.
5. **Veille (R15)** : GitHub Actions, aucun PC : `garde-progres.yml` (10 min) → STALL après 30 min sans contenu → `@codex` sur la PR « Pilote Codex » ; 60 min → courriel à Vial ; PR sans commit 60 min → recyclage. `checkpoint.yml` exige « Automates actifs » dans chaque PR, refuse une fausse fin d'étape en boucle et toute dose sans ligne AIPS. Seuils : `tools/garde/config.json`. `tools/veille_relance.sh` : facultatif. « Codex doit être libre, indépendant de tout PC ».
6. **Fusion** : `bash tools/file_fusion.sh` (`--dry-run`, `--chaine NOM`, `--droits`). Échecs → `journal/echecs_fusion.md`. Jamais `--admin`, squash ni force-push.
7. **Obstacle** : consigner, passer au lot ou à l'étape suivante. S'arrêter est interdit. Décision de Vial → étiquette `attente-vial` (courriel via `appel-vial.yml`) et continuer ailleurs. Un relevé seul ne termine jamais une boucle.

Pièges : ETAT.json et PROCHAINE_ACTION.md sont réécrits par la veille, commite-les avec ton lot ; `.etat_local/` n'est jamais versionné ; un label `attente-vial` (faute critique) suspend la chaîne.
