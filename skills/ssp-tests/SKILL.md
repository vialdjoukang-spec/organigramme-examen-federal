---
name: ssp-tests
description: >-
  Lis ce skill après chaque patch ou chaque injection de données : tu vérifies par l’exécution des 43
  contrôles au lieu de relire le code.
---
# But
Ce skill remplace la relecture par une ligne de résultat, sans réduire les contrôles.
# Déclencheur
Tu l’appliques après chaque modification de app_v2.html, avant tout commit.
# Étapes
1. Tu lances `python3 tests/run_tests.py` ; il exécute 19 contrôles sur ordinateur, 19 sur mobile et 5 complémentaires.
2. Tu lances `python3 tests/test_gardes.py` et `python3 tools/check_hash.py`.
3. Tu lis seulement le décompte et les lignes « ÉCHEC ».
4. Un échec se corrige dans ton patch ; tu relances ensuite les tests.
5. Tu ajoutes un test pour chaque critère d’acceptation nouveau de ton chantier, avec Janus.
# Interdits
Tu ne supprimes, n’assouplis ni ne raccourcis aucun contrôle pour obtenir une CI verte.
# Règle universelle
Le projet cible doit avoir un résultat de HAUTE QUALITÉ. L’usage des jetons doit être raisonnable et optimisé, et tout gaspillage est formellement interdit. L’économie de jetons est autorisée si et seulement si elle ne dégrade pas la qualité du travail.
