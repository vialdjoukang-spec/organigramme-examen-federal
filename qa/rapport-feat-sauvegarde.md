# Rapport · feat/sauvegarde · Janus avec Atlas · 17.10.2026

**Verdict :** prêt à fusionner si la CI (garde, html, liens, tests) réussit.

- Le diff touche app_v2.html par le seul patch 0003 (11 ancrages uniques ; le style du bandeau va dans le `<style>` de `<head>`, car le validateur Nu refuse toute règle nouvelle dans celui de `<body>`), ainsi que tests/, journal/ et ce rapport ; orig/ reste intact.
- Les 43 contrôles de la phase 0 réussissent toujours, et les 13 contrôles nouveaux de tests/test_export.py réussissent (56/56, aucune erreur de console).
- Les quatre appels restants à `localStorage.setItem` sont `lsSet`, la sonde, l’import et sa restauration ; aucune écriture ne reste dans un bloc catch vide.
- Point à vérifier : le rappel d’export s’appuie sur l’horloge du navigateur ; un essai réel sur iOS Safari reste à faire par le titulaire.
