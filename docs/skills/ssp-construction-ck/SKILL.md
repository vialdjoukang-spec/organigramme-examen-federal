---
name: ssp-construction-ck
description: Reconstruire les monographies, prévalences et doses après un lot ou une fusion, sans modifier les fichiers générés à la main.
---
# Construction des lots CK

1. Lire CONTINUATION.md et commencer l'étape courante avec `python3 tools/porte.py commencer N`. Réserver le lot dans une branche et sa PR.
2. Monographies : écrire seulement `data/ck/mono/*.json`, puis `python3 tools/mono_build.py` et `python3 tools/mono_build.py --check`. En conflit, `python3 tools/merge_shards.py <shards>` ; relire chaque clé signalée « CONFLIT RÉEL ».
3. Prévalences : écrire seulement `data/ck/prev.json`, puis `python3 tools/prev_build.py` et `python3 tools/prev_build.py --check`. Conserver exactement les libellés DD ; chiffre sans source lue, cadre, emplacement et date : « À vérifier ».
4. Doses : relire chaque ligne contre l'AIPS officielle, notamment µ/mg et les en-têtes ; `python3 tools/doses_check.py` si le script est présent sur la branche. Son absence ne vaut jamais validation. Le Compendium est exclu par CONTINUATION.md.
5. Après modification CK : `python3 tools/ck_build.py`, `python3 tools/ck_build.py --check`, `python3 tools/lyncee.py`, puis `python3 tests/run_tests.py`. Auditer médicalement le diff et consigner le verdict avant `audit-ok`.
6. Aucun générateur ni test ne remplace la lecture clinique. Ne pas augmenter une baseline ou enlever un contrôle pour faire passer le lot. Ne jamais modifier app.html.
