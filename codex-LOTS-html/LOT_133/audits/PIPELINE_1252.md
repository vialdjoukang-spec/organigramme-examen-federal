# Pipeline iconographique — audit technique 1252

Date : 02.11.2026. Périmètre : pipeline, tests et documentation ; aucun HTML clinique modifié.

## Écart confirmé

`integrer()` accédait directement à `sources['images_et_schemas']`. Le fichier réel `LOT_133/SOURCES.json` possède `lectures`, `images` et des compléments, mais aucune collection `images_et_schemas`. Même avec pixels licites et revues disponibles, l'intégration aurait levé `KeyError` avant la sauvegarde. Le défaut est donc indépendant du blocage actuel d'acquisition.

## Correction

Initialiser uniquement la collection manquante avec `setdefault`, conserver toutes les autres rubriques et refuser une collection malformée avant écriture. L'outil de rendu existant fournit déjà les deux vues du même cliché, contours rouges pointillés, numéros et légendes ; il n'a pas été réécrit. Aucun changement du commun ou du formateur de sources.

## Vérifications exécutées

Commande depuis la racine : `python3 -B -m unittest discover -s codex-LOTS-html/outils/illustration -p 'test_*.py'`.
Résultat : **42 tests réussis**. Trois régressions ajoutées : intégration sur la structure documentaire sans collection d'illustrations et préservation des crédits ; collection malformée refusée sans modification ; clic depuis une fenêtre liée à deux niveaux, références conservées et chaque cible de bouton résolue exactement une fois. La comparaison, les pointillés et la légende sont vérifiés structurellement ; crédits et URL source/licence du rendu concordent avec le registre.

## Application au LOT_133

Les commandes `preparer` puis `integrer` avec `codex-LOTS-html/LOT_133/illustrations/pipeline/PLAN.json` sont détaillées dans `../../outils/illustration/PIPELINE.md`. Ce plan reste à constituer après acquisition des pixels ; aucune spécification clinique ni coordonnée d'annotation n'a été inventée. La revue réelle de l'original puis du rendu et ses captures restent obligatoires avant intégration.

Les attestations des tests sont simulées et explicitement marquées comme telles. Aucun test n'est une inspection visuelle. Aucun nouveau cliché acquis, généré ou intégré ; aucune licence propre à une nouvelle figure ni validation médicale revendiquée. Les tests ont utilisé leurs fichiers temporaires puis les ont supprimés ; seuls les quatre fichiers autorisés sont livrés.
