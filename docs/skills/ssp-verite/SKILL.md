---
name: ssp-verite
description: >-
  Lis ce skill avant de livrer tout texte visible et avant chaque fusion :
  chaque affirmation cite une source lue et datée, sinon elle devient « À
  vérifier ».
---
# But
Ce skill empêche tout fait inventé d’entrer dans l’application.
# Déclencheur
Tu l’appliques avant de livrer un texte visible ; Janus l’applique avant chaque fusion.
# Étapes
1. Chaque phrase factuelle cite une source lue, avec son URL, son paragraphe et sa date de lecture.
2. La source primaire applicable la plus récente l’emporte ; une source suisse précède une source européenne ; aucune autre source clinique n’est admise.
3. Un fait sans source lue devient « À vérifier », avec un ticket « Point à vérifier ».
4. Chaque phrase contient un verbe conjugué ; tu réécris toute phrase nominale.
5. Une URL ou un DOI ajouté doit répondre sans erreur (contrôle lychee de la CI).
# Interdits
Tu ne résumes, ne raccourcis ni ne reformules un texte clinique pour économiser des jetons. Un test automatique ne remplace pas la validation par un médecin.
# Règle universelle
Le projet cible doit avoir un résultat de HAUTE QUALITÉ. L’usage des jetons doit être raisonnable et optimisé, et tout gaspillage est formellement interdit. L’économie de jetons est autorisée si et seulement si elle ne dégrade pas la qualité du travail.

## Inventaire des marques restantes

`python3 tools/inventaire_a_verifier.py --ref origin/main --sortie audit/RESTE_A_VERIFIER_20261018.json` lit seulement l’instantané Git demandé. Le rapport conserve le SHA, les nombres de champs et d’occurrences, les fichiers et les pointeurs JSON. Le balisage HTML et les entités sont lus comme du texte. Il n’évalue aucune affirmation et n’inclut pas les branches non fusionnées : ne jamais transformer ce recensement en certificat médical ou en preuve de clôture. Les attentes R13 et les validations de Vial restent dans ETAT.json.
