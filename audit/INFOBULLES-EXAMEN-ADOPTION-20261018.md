# Contrelecture technique · examen régional et adoption Iris

Verdict : favorable sur les corrections locales examinées, après correction du défaut de contrôle requis décrit ci-dessous. L’exécution de la CI sur la tête exacte et sa relecture restent requises avant fusion. Aucun fichier canonique modifié par la sentinelle ; aucune capture locale, lancement distant, adoption ou fusion exécuté.

## Examen régional dans la fiche SSP

Le patch0036 corrige une régression réelle : lorsque la monographie SSP complète interceptait le cours G1c5, les régions d’examen et renvois GES du cours étaient perdus. La branche c5 réutilise maintenant exFmt(T.c[5]), insère son résultat avant la rubrique5 (donc dans la rubrique4) et conserve les six rubriques.

L’examen est identifié par un sous-titre et sa provenance TIP.s est ajoutée distinctement de MO.s. Les balises b/strong de son corps sont retirées, tandis que sections régionales, phases, listes et boutons data-gx restent en place. Le gestionnaire data-gx existant précède le gestionnaire des infobulles et ouvre la bonne région GES en fermant la fiche : le patch ne remplace pas ce chemin.

Contrôle déterministe sur les données G1 réelles, par exécution isolée de exFmt : trois régions, quatre renvois et aucune balise b/strong résiduelle dans le corps ajouté. L’ancrage exact de rubrique5 existe dans la monographie SSP générée. Le nouveau test navigateur contrôle six rubriques, régions, liens et position avant la rubrique5 ; le test_examen existant conserve aussi la vérification de navigation effective. Leur exécution navigateur demeure à la CI exacte ; aucune réussite de navigateur local n’est revendiquée.

Limite explicite : l’ajout régional concerne l’ouverture du cours c5. Les autres entrées et la fiche SSP directe conservent leur monographie complète ; aucun audit clinique nouveau du texte de cours réutilisé n’est déduit de ce correctif de restitution.

## Adoption explicite par étiquette

Défaut initial signalé puis corrigé par l’intégrateur : le premier état du workflow ignorait le job requis visuel lorsqu’une étiquette iris: était posée. Un job ignoré peut satisfaire une exigence GitHub sans comparaison ; cette exclusion a été retirée. Dans l’état final relu, le déclenchement par étiquette exécute normalement visuel. L’adoption dépend de sa fin avec always(), sans remplacer son verdict. Une comparaison rouge ne devient pas verte par la seule étiquette ; après le commit de référence, les contrôles doivent être exécutés sur le nouveau SHA.

Contrôles finaux favorables :

- Numéro de PR numérique, base main, étiquette iris suivie de quarante caractères hexadécimaux et égalité exacte avec la tête actuelle. Les tests de SHA ont des sorties explicites sur échec.
- Vérification supplémentaire par le script habituel : visuel:nouvelle-reference obligatoire, branche locale et HEAD identiques à la PR.
- Sélection d’une exécution Visuel terminée sur cette branche et ce SHA, hors annulation ; téléchargement de son artefact visuel-reference-proposee. Un téléchargement ou un artefact absent fait échouer le script, sans adoption aveugle.
- Le script inchangé produit un commit explicite et le push reste sans force. Si la branche distante a avancé, le push normal refuse une divergence plutôt que de l’écraser.
- Aucun plafond ni calcul comparatif n’a été modifié dans ce lot. Le mécanisme d’adoption existant reste une décision explicite après examen ; il ne constitue ni accord médical ni autorisation de fusion pendant une CI rouge.

Le run d’adoption courant n’est pas encore terminé lorsque le script cherche un run achevé : une capture antérieure achevée sur le même SHA est donc nécessaire. Sans elle, le script refuse. La concurrency conserve la faculté d’annuler un ancien run lors d’un nouvel événement ; il faut attendre une véritable exécution de capture terminée avant de demander l’adoption.

## Aperçus de relecture

relecture.py ajoute les images d’écarts rouges existantes aux couples référence/actuel, sans modifier les captures, les mesures ou la référence. Les aperçus restent volontairement limités à cinq vues et à leur partie supérieure : ils ne prouvent pas à eux seuls une inspection intégrale de toutes les captures. Le rapport comparatif et les artefacts complets restent les éléments de contrôle pour les autres différences.

## Vérifications exécutées par la sentinelle

YAML analysé, JavaScript embarqué accepté par node --check, exFmt exécuté isolément sur G1, syntaxe de visuel_reference.sh vérifiée par bash -n, git diff --check réussi. Aucune protection de branche, étiquette distante, fichier app/workflow ou référence visuelle modifié par la sentinelle.
