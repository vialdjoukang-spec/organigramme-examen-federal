# Rapport · fix/bandes-calendrier · Hermès · 17.10.2026

**Verdict :** prêt à fusionner si la CI (garde, html, liens, tests, visuel) réussit.

- Le diff touche app_v2.html par le seul patch 0010 (5 ancrages uniques, rejouable après 0004 ; règles CSS dans le style de head, préfixées par #grid), tests/visuel/capture.py et compare.py (contrôle du texte coupé), tests/test_calendrier.py (bandes_sans_coupure), HANDOFF.md, ETAT.md, le journal et ce rapport ; orig/ reste intact.
- Suite locale 121/121, gardes 5/5, empreinte de orig/app.html conforme, aucune erreur de console.
- Iris en local : 0 texte coupé sur 72 vues (3 thèmes × 2 profils × 10 onglets et états, plus vues Semaine et Jour avec séances de 15 à 120 min) ; sur main, le même contrôle relève 30 éléments coupés.
- Aucune couleur codée en dur ; la hauteur des bandes reste proportionnelle à la durée.
