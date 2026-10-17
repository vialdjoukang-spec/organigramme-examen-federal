---
name: ssp-json-data
description: >-
  Lis ce skill dès que tu modifies une constante de données de app_v2.html (TIP,
  NOT, GES, SSP, PHT, MEM, SESSION) : tu édites le JSON extrait, pas le fichier.
---
# But
Ce skill limite la lecture et le diff aux seules données modifiées.
# Déclencheur
Tu l’appliques avant toute modification d’une constante en JSON strict.
# Étapes
1. Tu lances `python3 tools/json_inject.py check <NOM>` ; un aller-retour « identique » garantit un diff propre.
2. Tu lances `python3 tools/json_inject.py extract <NOM>` ; la donnée s’écrit dans `data/<NOM>.json`.
3. Tu modifies seulement les entrées utiles de ce JSON, puis tu valides sa structure (mêmes clés, mêmes types).
4. Tu lances `python3 tools/json_inject.py inject <NOM>`, puis ssp-tests.
5. Une constante qui n’est pas du JSON strict (EXI, ATT, CLIN) se modifie par ssp-patch.
# Interdits
Tu ne lis jamais le reste du fichier pour modifier une donnée.
# Règle universelle
Le projet cible doit avoir un résultat de HAUTE QUALITÉ. L’usage des jetons doit être raisonnable et optimisé, et tout gaspillage est formellement interdit. L’économie de jetons est autorisée si et seulement si elle ne dégrade pas la qualité du travail.
