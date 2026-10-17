# Rapport · feat/hermes-recherche-notions · Hermès · 17.10.2026

**Verdict :** prêt à fusionner si la CI (garde, html, liens, tests, visuel) réussit.

- Le diff touche app_v2.html par le seul patch 0009 (4 ancrages uniques, rejouable après 0004), ainsi que tests/, journal/, HANDOFF.md, ETAT.md et ce rapport ; orig/ reste intact.
- Suite locale 119/119 (dont 34 de tests/test_calendrier.py, avec recherche_notion sur ordinateur et mobile), gardes 5/5, empreinte de orig/app.html conforme, aucune erreur de console.
- Contrôle visuel : la liste des résultats reste lisible sur ordinateur (titre trouvé à droite, gris discret) et sur mobile (titre à la ligne) ; aucune couleur de fond codée en dur, seulement var(--mut).
- Le site public (PR #15) a été vérifié : même empreinte que main, 32/32 contrôles du Calendrier.
