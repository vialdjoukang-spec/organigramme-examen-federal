# Référence verte · phase 0 · Janus

**Date :** 17.10.2026 (Europe/Zurich) · **Fichier :** `app_v2.html` tel quel (SHA-256 `093b5c413d863f0d…`).

| Contrôle | Commande | Résultat de référence |
|---|---|---|
| Interaction, ordinateur (1366 × 860) | `tests/run_tests.py` → `test_tip.py` | 19/19 |
| Interaction, mobile (Pixel 7) | `tests/run_tests.py` → `test_tip.py` | 19/19 |
| Complémentaires (touche i, survol, défilement, appui long, toucher court) | `tests/run_tests.py` → `test_extra.py` | 5/5 |
| Erreurs de console | les deux scripts | 0 |
| Gardes (empreinte, budget, HTML) | `tests/test_gardes.py` | 5/5 |
| Empreinte de `orig/app.html` | `tools/check_hash.py` | `1e067c6ecb82190d…` |
| Budget | `tools/budget.py` | 5 682 786 octets sur 6 000 000 |
| Validateur Nu | `tools/html_check.py` | 207 erreurs connues, figées dans `qa/html-baseline.json` |

Les 207 erreurs HTML existaient déjà dans le fichier d’origine ; la plupart viennent de blocs `<style>` placés dans `<body>`. La CI refuse toute erreur nouvelle, et la référence ne peut que diminuer.

Les patchs `tools/patches/0001` et `0002`, appliqués à `orig/app.html`, reproduisent `app_v2.html` à l’octet près.
