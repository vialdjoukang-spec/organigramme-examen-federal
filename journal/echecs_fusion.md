# Échecs de fusion-publication (tools/file_fusion.sh)

Une ligne par échec nouveau. Le travail continue toujours ; Codex traite ces lignes à l’étape 2 ou dans l’étape de la chaîne.

- 2026-10-17 23:04 UTC · #49 · conflit avec main : git merge origin/main + merge_shards.py + mono_build.py/prev_build.py (jamais à la main)
- 2026-10-17 23:04 UTC · #50 · conflit avec main : git merge origin/main + merge_shards.py + mono_build.py/prev_build.py (jamais à la main)
- 2026-10-17 23:04 UTC · #60 · conflit avec main : git merge origin/main + merge_shards.py + mono_build.py/prev_build.py (jamais à la main)
- 2026-10-17 23:04 UTC · #59 · conflit avec main : git merge origin/main + merge_shards.py + mono_build.py/prev_build.py (jamais à la main)
- 2026-10-17 23:04 UTC · #65 · conflit avec main : git merge origin/main + merge_shards.py + mono_build.py/prev_build.py (jamais à la main)

- 18.10.2026 · Étape 0 · Lecture de protection main via l'intégration refusée (HTTP 403). Droits de dépôt admin/push/merge_commit/auto_merge confirmés. Protection conservée ; ne pas considérer le JSON d'erreur comme une liste de checks.
- 18.10.2026 · Étape 0 · Codex CLI installé mais test gpt-6-luna refusé pour authentification. Mode B retenu ; aucun renouvellement de connexion interactif demandé.

- 18.10.2026 01:07 CEST · Étape 2 · Lecture des secrets Actions refusée (403) ; gh opérationnel, auto-fusion #71 a réussi à activer MERGE. Aucune intervention interactive ni nouveau secret. Réparation du repli 403 et du réessai Pages livrée séparément.
- 2026-10-17 23:11 UTC · #44 · conflit avec main : git merge origin/main + merge_shards.py + mono_build.py/prev_build.py (jamais à la main)
- 2026-10-17 23:12 UTC · #60 · contrôle requis garde en échec
- 2026-10-17 23:15 UTC · #44 · contrôle requis visuel en échec

- 18.10.2026 · Étape 3 · #44/#45/#58 : conflits dans app_v2 et prev.js ; app repris de main, correctifs audités rejoués, assets régénérés. Les fusions restent en attente des suites et de la CI, sans forçage. Poursuite Étape 4 selon R7, reprise par la file.
- 18.10.2026 · Tests locaux initiaux : Playwright 1.62 différent du 1.63 figé dans la CI ; échecs d'interaction de fermeture/panneau calendrier constatés. Venv 1.63 et Chromium 1243 installés, aucune assertion abaissée.

- 18.10.2026 · Étape 4 · Reprises des cinq PR effectuées ; fusions en attente de CI et d'ordre des labels. #64 suspendue par attente-vial (HOPE et constat de décès), pas d'audit-ok ; la file poursuit les autres chaînes.
- 2026-10-17 23:50 UTC · #75 · gh pr merge refusé (protection, tête changée ou droits)
- 2026-10-18 00:06 UTC · #45 · conflit avec main : git merge origin/main + merge_shards.py + mono_build.py/prev_build.py (jamais à la main)
- 2026-10-18 00:07 UTC · #41 · conflit avec main : git merge origin/main + merge_shards.py + mono_build.py/prev_build.py (jamais à la main)

- 18.10.2026 UTC · Incident #62 : fusion automatique à 23:55:43 UTC avant #60, causée par le workflow qui ignorait les prédécesseurs. Audit-ok de #61 retiré temporairement ; #82 ajoute le verrou de chaîne. #60 doit encore réunir ses données avec main ; aucune fusion annulée ni protection contournée.
- 2026-10-18 00:29 UTC · #32 · contrôle requis visuel en échec
- 2026-10-18 00:47 UTC · #83 · conflit avec main : git merge origin/main + merge_shards.py + mono_build.py/prev_build.py (jamais à la main)
- 2026-10-18 00:57 UTC · #65 · contrôle requis tests en échec

- 18.10.2026 UTC · #83 : push non-fast-forward refusé car le bot avait avancé la branche ; fetch, réunion des commits distants, diff --check et push sans force réussis (0b86173).
- 18.10.2026 UTC · #32 : téléchargement local des deux artefacts refusé 403. Repli exécuté par le même script sur runner, SHA/branche/base vérifiés ; adoption et relance des contrôles sans contournement de protection.
- 2026-10-18 01:16 UTC · #32 · gh pr merge refusé (protection, tête changée ou droits)
- 2026-10-18 01:23 UTC · #65 · contrôle requis visuel en échec
- 2026-10-18 01:27 UTC · #61 · conflit avec main : git merge origin/main + merge_shards.py + mono_build.py/prev_build.py (jamais à la main)
- 2026-10-18 01:27 UTC · #85 · conflit avec main : git merge origin/main + merge_shards.py + mono_build.py/prev_build.py (jamais à la main)
- 2026-10-18 01:45 UTC · #68 · contrôle requis visuel en échec
- 2026-10-18 01:56 UTC · #68 · contrôle requis html en échec

- 18.10.2026 UTC · #68 : garde, tests 278 et visuel verts après adoption, contrôle HTML rouge pour deux règles nouvelles dans un style hérité du corps. Patch corrigé en portant les mêmes dimensions sur les éléments créés ; référence HTML inchangée, nouvelle CI demandée.

- 18.10.2026 02:19 UTC · #83 : liens en échec par quatre délais revmed.ch, sans erreur HTTP invalide. Reprise de main après #85, contrôle relancé vert ; aucune exclusion ni règle affaiblie.
