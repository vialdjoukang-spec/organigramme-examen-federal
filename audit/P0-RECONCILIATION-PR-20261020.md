# P0 — File des PR et réconciliation future

Observation GitHub MCP du 20 octobre 2026. Aucun appel GitHub CLI, aucune mutation, aucun changement du code de PR268 par cet agent.

- Main observé séparément : `b22c1b41f88bc132b94e021bb9eb6f459e8dfa13`.
- Le relevé initial contient106 PR historiques, hors correctif 268 :71 DIRTY et35 BEHIND, aucune valeur nulle. Les106 têtes concordent avec `audit/P0-FILE-PR-20261020.json`.
- Après la fusion 268, un unique rafraîchissement des106 PR retourne `mergeable:null`, `mergeable_state:unknown` pour toutes : GitHub n'a pas fourni de classification recalculée. Ces valeurs ne sont pas interprétées comme une absence de conflits. Aucun nouveau tour complet n'a été lancé.
- La fermeture de 202 est vérifiée à 10:59:07 UTC, tête `badd4402994892b95a7ab842baf9135af4b4ca5e`. Il reste donc105 PR historiques ouvertes dans ce périmètre. Le précédent comptage déterminé, après retrait de 202, serait70 DIRTY/35 BEHIND ; il reste historique.
- PR 150 est bien repassée en brouillon ; sa tête est conservée. Toutes les106 têtes historiques ont encore une branche dans le relevé des 125 branches. Aucun SHA de branche identique à celui d'une autre branche n'est observé. Aucun doublon technique de branche n'est donc démontré par égalité de tête.
- 19 branches n'avaient pas de PR ouverte dans la collection initiale. Elles comprennent main, automates/prevalences, garde/etat, veille-etat, des archives de préparation et des expériences. Une absence de PR ou un âge ne prouve pas leur inutilité. Aucune suppression proposée sans comparaison d'ascendance et vérification de sauvegarde.

## Superpositions vérifiées, sans interprétation médicale

| PR | Périmètre commun constaté | Conséquence pratique |
|---|---|---|
|161 / 164|`data/ck/src.json`, `assets/ck/src.js`, `assets/config/tip.js` ; leurs cours canoniques S3.6–S3.7 et S3.8–S3.9 sont disjoints|Reprendre les JSON du lot depuis main, préserver les sources par identifiant, puis régénérer les assets. Ne jamais remplacer un asset partagé par une ancienne copie.|
|187 / 252|`data/ck/mono/a.json`, `data/ck/mono/i.json` et leurs deux assets ; tous les SHA de blobs partagés diffèrent|Superposition certaine, équivalence non démontrée. Aucun contenu clinique supprimé ou clos. Réconciliation par clé et comparaison trois voies seulement au chantier BETTA.|
|202 / 268|202 touche uniquement `tools/arsenal/_c.py` et son test|Le coordinateur a repris et amélioré ce correctif dans 268, puis fermé 202. La branche est conservée.|
|229|`qa/domaines.yml` seulement|Comparer les deux adresses proposées au correctif G3 intégré et aux lots destinataires ; aucun visa médical ni fusion automatique n'en découle.|

Ces six PR sont un contrôle ciblé de superpositions, pas un inventaire exhaustif des fichiers des105 PR.

## Dépendances de reprise

1. La clôture P0 exige les preuves du correctif 268 et sa publication. Les conflits sur les lots de priorités futures restent conservés dans une file exploitable ; leur constat seul ne justifie aucune intégration clinique pendant P0.
2. Au début de P1, examiner d'abord les preuves des cours déjà présents dans main, notamment S3.4–S3.5, avant de reprendre 161. Présence du contenu et validité des preuves de relecture/publication sont distinctes.
3. Avant chaque lot : relever main et la tête de PR, contrôler à nouveau l'état de fusion, comparer les données canoniques avec la base commune, récupérer seulement les unités du lot et conserver tous les autres contenus.
4. Pour ALPHA : `data/tip/<SSP>.json` reste canonique ; utiliser `tools/cours/appliquer.py` pour le lot, puis reconstruire les assets par les outils existants. Chaque correction substantielle appelle une nouvelle contrelecture indépendante sur les nouvelles empreintes ; vérifier CI et publication avant le lot suivant.
5. Pour BETTA, à P3 seulement : traiter les shards partagés avec la fusion trois voies par clé prévue dans `tools/merge_shards.py`, puis compiler. Les désaccords cliniques exigent le contre-audit ; ils ne sont pas résolus en choisissant un fichier entier.
6. Les35 anciens BEHIND ne sont pas présumés prêts à fusionner : mise à jour éventuelle, audit et CI modifient la preuve du SHA. Les71 anciens DIRTY ne sont pas qualifiés de conflits cliniques sans comparaison trois voies.

Preuves structurées : `audit/P0-CONFLITS-AVANT-FUSION-20261020.json` (historique déterminé) et `audit/P0-CONFLITS-PR-20261020.json` (dernière observation, fermeture 202, six relevés de fichiers et 125 branches). Aucun audit médical n'est attesté par ce rapport technique.
