---
name: ssp-revue-diff
description: >-
  Lis ce skill pour relire une demande de fusion ou ton propre travail : la revue porte sur ce qui
  change, pas sur le fichier entier.
---
# But
Ce skill fait porter la revue sur quelques centaines de lignes au lieu de millions de caractères.
# Déclencheur
Janus et Athéna l’appliquent à chaque demande de fusion ; tout agent l’applique avant de livrer.
# Étapes
1. Tu lis `git diff --stat origin/main...HEAD`.
2. Tu lis le diff mot à mot des vues extraites (`git diff --word-diff`) ou des fichiers data/.
3. Tu vérifies le rapport de CI (garde, html, tests, liens) au lieu de rejouer chaque test.
4. Tu rouvres app_v2.html seulement autour d’un ancrage précis, par `str.find`.
5. Tu écris un rapport bref dans `qa/rapport-<branche>.md` : verdict, échecs, points à vérifier.
# Interdits
Tu ne fusionnes jamais une branche dont la CI échoue.
# Règle universelle
Le projet cible doit avoir un résultat de HAUTE QUALITÉ. L’usage des jetons doit être raisonnable et optimisé, et tout gaspillage est formellement interdit. L’économie de jetons est autorisée si et seulement si elle ne dégrade pas la qualité du travail.
