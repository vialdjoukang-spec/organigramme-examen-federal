---
name: ssp-patch
description: >-
  Lis ce skill avant toute modification du code de app_v2.html : chaque
  changement s’écrit comme un patch à ancrage unique et rejouable.
---
# But
Ce skill fait écrire seulement le changement, de façon vérifiable et rejouable.
# Déclencheur
Tu l’appliques pour tout changement de code, de style ou de constante non JSON (EXI, ATT, CLIN).
# Étapes
1. Tu repères une chaîne d’ancrage dans la vue de ssp-extrait-cible, puis tu vérifies par `str.find` qu’elle apparaît une seule fois dans app_v2.html.
2. Tu écris `tools/patches/NNNN-<objet>.py` sur le modèle de 0001 : lecture de `APP_FILE`, `assert s.count(A) == 1`, remplacement, écriture.
3. Le patch échoue si l’ancrage manque ou se répète ; tu choisis alors un ancrage plus long, sans jamais remplacer « toutes les occurrences ».
4. Tu l’appliques avec `APP_FILE=app_v2.html`, puis tu lances ssp-tests.
5. Tu relis seulement `git diff --stat` et le diff autour de l’ancrage.
# Interdits
Tu ne réécris jamais le fichier entier à la main, et tu n’appliques jamais un patch à orig/app.html.
# Règle universelle
Le projet cible doit avoir un résultat de HAUTE QUALITÉ. L’usage des jetons doit être raisonnable et optimisé, et tout gaspillage est formellement interdit. L’économie de jetons est autorisée si et seulement si elle ne dégrade pas la qualité du travail.
