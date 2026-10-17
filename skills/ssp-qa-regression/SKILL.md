---
name: ssp-qa-regression
description: >-
  Lis ce skill pour contrôler une branche avant fusion : il fixe la référence
  verte et refuse toute régression.
---
# But
Ce skill fait apparaître une régression dans la CI avant toute fusion.
# Déclencheur
Janus l’applique à chaque branche et à chaque demande de fusion.
# Étapes
1. La référence verte compte 19 + 19 + 5 contrôles réussis et zéro erreur de console (`tests/run_tests.py`).
2. Les gardes doivent réussir : empreinte de orig/app.html, budget (app_v2.html ≤ 6 Mo, image ≤ 200 Ko), aucune erreur HTML nouvelle par rapport à `qa/html-baseline.json`.
3. Chaque critère d’acceptation du chantier reçoit un test ou un contrôle nommé.
4. Une baisse du nombre d’erreurs HTML autorise à resserrer la référence (`tools/html_check.py <json> --update`), jamais à l’élargir.
5. Tu consignes le verdict dans `qa/rapport-<branche>.md`, avec le lien vers la CI.
# Interdits
Tu ne corriges pas le code d’un autre agent : tu ouvres un ticket et tu renvoies la branche.
# Règle universelle
Le projet cible doit avoir un résultat de HAUTE QUALITÉ. L’usage des jetons doit être raisonnable et optimisé, et tout gaspillage est formellement interdit. L’économie de jetons est autorisée si et seulement si elle ne dégrade pas la qualité du travail.
