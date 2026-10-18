---
name: ssp-qualite-visuelle
description: >-
  Lis ce skill avant de toucher à la présentation de app_v2.html (CSS, thèmes, typographie) et avant
  d’accepter un changement visuel : l’automate Iris juge chaque demande de fusion par captures et mesures.
---
# But
Ce skill fait juger le rendu par une machine, onglet par onglet, au lieu de le décrire ou de le relire.
# Déclencheur
Tu l’appliques à toute branche qui modifie l’apparence, et à chaque rapport « Iris · qualité visuelle ».
# Étapes
1. Tu lances en local `python3 tests/visuel/capture.py --sortie /tmp/iris`, puis `python3 tests/visuel/compare.py --sortie /tmp/iris` ; tu lis seulement le décompte et les lignes « ÉCHEC ».
2. Iris capture 9 onglets et la fenêtre épinglée, sur ordinateur (1440) et Pixel 7, en thème clair, « Fond doré » à 100 % et sombre, horloge figée au 16.11.2026.
3. Iris bloque : plus de 0,2 % de pixels changés, dimensions changées, nouveau problème axe-core grave ou critique (dont le contraste WCAG AA), débordement horizontal sur mobile, police en échec, CLS au-dessus du plafond, erreur JavaScript.
4. Un changement voulu s’accepte ainsi : tu poses l’étiquette `visuel:nouvelle-reference`, tu attends la fin de la tâche « visuel », tu lances `tools/visuel_reference.sh <PR>` sur la branche à jour, puis tu pousses ; la comparaison suivante doit être exacte.
5. Tu ouvres les images d’écart de l’artefact `visuel-rapport` (référence | actuel | écarts en rouge) avant d’adopter une référence, et tu justifies l’adoption dans la PR.
6. Une baisse des compteurs axe-core ou du CLS autorise à resserrer la référence par la même procédure ; une hausse exige une justification écrite.
# Interdits
Tu ne modifies jamais qa/visuel/reference* à la main, ni sans étiquette. Tu ne relèves aucun seuil de qa/visuel/config.json pour obtenir une CI verte. Tu n’ajoutes aucune ressource externe (CDN de polices ou de scripts) : la page doit s’afficher à l’identique en file:// sans réseau.
# Règle universelle
Le projet cible doit avoir un résultat de HAUTE QUALITÉ. L’usage des jetons doit être raisonnable et optimisé, et tout gaspillage est formellement interdit. L’économie de jetons est autorisée si et seulement si elle ne dégrade pas la qualité du travail.

## Artefacts inaccessibles depuis l’environnement local

Si le téléchargement des artefacts échoue mais que les écarts et mesures ont été examinés, la variante du workflow `Visuel` proposée par #32 propose `adopter_pr`. Attendre une exécution Visuel terminée sur le SHA exact de la PR puis lancer `gh workflow run visuel.yml --ref <branche> -f adopter_pr=<PR>`. Le job manuel vérifie numéro, branche, base main et SHA, puis exécute le même `tools/visuel_reference.sh` sur le runner. Il n’exécute aucune nouvelle capture et n’affaiblit aucun seuil. Si la tête a changé ou qu’aucune capture correspondante n’est terminée, il refuse. Après adoption, récupérer le commit, examiner la référence, puis pousser depuis le jeton habituel pour déclencher les contrôles requis (un push fait par GITHUB_TOKEN ne les déclenche pas toujours). Aucune fusion avant CI verte. Cette option reste une procédure d’adoption explicite après examen, jamais une acceptation automatique des régressions.

## Connecteur sans commande workflow_dispatch

Après examen des captures et des écarts sur le SHA exact, une étiquette explicite `iris:<SHA complet de 40 caractères>` sur la PR déclenche le même job d’adoption. Elle n’exprime aucun accord médical. Le runner refuse un SHA différent de la tête courante, une base autre que main, l’absence de `visuel:nouvelle-reference` ou l’absence de captures achevées correspondantes. Le script d’adoption et tous les seuils restent identiques. Supprimer cette étiquette après l’adoption ; relancer les contrôles sur le nouveau commit avant fusion. Ce mécanisme permet l’adoption examinée avec un connecteur GitHub dépourvu de commande de lancement manuel.
