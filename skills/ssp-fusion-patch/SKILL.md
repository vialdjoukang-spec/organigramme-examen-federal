---
name: ssp-fusion-patch
description: >-
  Lis ce skill quand main a avancé pendant ton chantier : il intègre main dans ta branche sans jamais
  résoudre à la main un conflit dans app_v2.html ni dans la référence visuelle.
---
# But
Ce skill garde app_v2.html reproductible lors d’une fusion : la version de main plus ton patch rejoué.
# Étapes
1. Tu lances `git fetch && git merge --no-commit origin/main`.
2. Pour app_v2.html, tu prends `git checkout origin/main -- app_v2.html`, puis tu rejoues ton patch avec `APP_FILE=app_v2.html`. Si un ancrage manque, tu l’allonges ou tu le déplaces dans le patch.
3. Pour qa/visuel, tu prends la version de main ; la référence se régénère ensuite par l’étiquette et tools/visuel_reference.sh.
4. Pour les listes (SUITES, ETAT.md, HANDOFF.md), tu gardes les deux côtés.
5. Avant le commit, `git grep -n '^<<<<<<<\|^>>>>>>>'` ne doit rien trouver, et `<!doctype` ne doit apparaître qu’une fois dans app_v2.html.
6. Tu lances ssp-tests, puis tu poses le commit de fusion.
# Interdits
Tu n’utilises jamais `git add -A` tant qu’un conflit reste ouvert, et tu ne forces jamais un push sur main.
# Règle universelle
Le projet cible doit avoir un résultat de HAUTE QUALITÉ. L’usage des jetons doit être raisonnable et optimisé, et tout gaspillage est formellement interdit. L’économie de jetons est autorisée si et seulement si elle ne dégrade pas la qualité du travail.
