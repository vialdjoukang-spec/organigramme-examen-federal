# Rapport QA · feat/ck-interaction (NC-0, Hermès) · 17.10.2026, Europe/Zurich

| Contrôle | Résultat |
|---|---|
| tests/run_tests.py (dont les 43 de la phase 0 et test_calendrier 36) | 168/168 |
| tests/test_ck_ui.py (ordinateur 1366×900 et Pixel 7) | 47/47, aucune erreur de console |
| tests/test_gardes.py | 5/5 |
| tools/check_hash.py (orig/app.html) | conforme |
| tools/budget.py | 5 813 294 octets sur 6 000 000 |
| tools/nc_svg_js.py --check (données d’essai) | conforme |
| Iris, texte coupé (CLIP_JS) | 0 élément coupé sur 72 vues |
| Iris, pixels | aucune différence avec main : les 9 écarts locaux « not » et « not-fenetre » sont identiques au pixel près sur le build de main (environnement local) |
| Performance du lieur | index de 3 200 termes construit en 8 ms ; aucune tâche longue ajoutée |

Les captures, prises avec les données d’essai (tests/fixtures/ck), ne sont pas versionnées : niveaux 1, 2 et 5, Retour, synthèse A/B, hypothèse et prise en charge, couches, vues, tour et repli <img>, sur ordinateur et mobile.
