# Rapport QA · feat/ck-interaction (NC-0, Hermès) · 17.10.2026, Europe/Zurich

| Contrôle | Résultat |
|---|---|
| tests/run_tests.py (dont les 43 de la phase 0 et test_calendrier 36) | 170/170 |
| tests/test_ck_ui.py (ordinateur 1366×900 et Pixel 7) | 49/49, aucune erreur de console |
| tests/test_gardes.py | 5/5 |
| tools/check_hash.py (orig/app.html) | conforme |
| tools/budget.py | 5 813 409 octets sur 6 000 000 |
| tools/nc_svg_js.py --check (données d’essai et assets/nc, nc07.js) | conforme |
| tools/dedale/verifier.py --tous, tests/test_dedale.py | 0 échec, 11/11 |
| Schéma réel nc07 (Dédale) dans la fenêtre | SVG intégré, 7 couches, 5 vues, crédit affiché, 0 texte coupé |
| Iris, texte coupé (CLIP_JS) | 0 élément coupé sur 72 vues |
| Iris, pixels | aucune différence avec main : les 9 écarts locaux « not » et « not-fenetre » sont identiques au pixel près sur le build de main (environnement local) |
| Performance du lieur | index de 3 200 termes construit en 8 ms ; aucune tâche longue ajoutée |

Les captures, prises avec les données d’essai (tests/fixtures/ck), ne sont pas versionnées : niveaux 1, 2 et 5, Retour, synthèse A/B, hypothèse et prise en charge, couches, vues, tour et repli <img>, sur ordinateur et mobile.

## Intégration sur main 4ff1cec (17.10.2026, Europe/Zurich)

| Contrôle | Résultat |
|---|---|
| tests/run_tests.py | 194/194 |
| tests/test_ck_ui.py | 61/61, dont 12 sur les données réelles, aucune erreur de console |
| tests/test_ck.py (Janus) | 61/61 |
| niveau1 G1 à G7, ck_build --check, nc_svg_check, nc_svg_js --check | réussis |
| tools/dedale/verifier.py, tests/test_dedale.py | 0 échec, 20/20 |
| Budget | app_v2.html 5 819 307 / 6 000 000 ; assets/nc 445 293 / 3 000 000 |
