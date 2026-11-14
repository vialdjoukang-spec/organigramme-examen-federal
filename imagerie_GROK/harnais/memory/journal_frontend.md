# Journal frontend/outils (ingénieur architecte) — 14.11.2026
- Livré : scripts/_common.py (cache HTTP cache/), fetch_commons.py (search/findcat/cat/info/get), fetch_openi.py (search/get, 512 px max),
  normalize.py, validate.py, build_app.py + app_template.html, screenshot.py. Usage : HARNESS.md § Outils.
- Statut affiché dans l'app = statut validé (validate.check) ; manifest en erreur → « Non validé » + liste des erreurs dans la fenêtre.
- Manifests TEST-* créés puis supprimés (images/test supprimé). Captures de test conservées : shots/harnais_test_*.png.
- Rebuild : python3 scripts/build_app.py && python3 scripts/screenshot.py --tag <lot> (vérifie console, débordement mobile, bulle au clic, Entrée clavier).
- Placement des bulles : algorithme à 8 positions (évite pointe de flèche, autres bulles/badges, débordement du cadre).
