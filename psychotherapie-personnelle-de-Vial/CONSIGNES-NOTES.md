# CONSIGNES DE PRISE DE NOTES — Lecture obligatoire avant toute séance

Ce fichier est la règle de fonctionnement du projet. Toute IA qui ouvre une séance doit le lire en premier, avant le README de phase ou le fichier de séance.

## Principe général

- Les notes sont prises **au fur et à mesure** de la séance, pas à la fin.
- Chaque affirmation de Vial est consignée telle quelle, entre guillemets si c'est une citation exacte, sinon reformulée fidèlement sans interprétation.
- L'IA note aussi ses propres interventions clés (questions posées, recadrages) pour que la séance soit rejouable.
- Rien n'est supprimé. Les corrections de Vial sont ajoutées comme entrées nouvelles datées, jamais en écrasant l'original.

## Structure d'une séance dans son fichier

Chaque fichier de séance (ex. 01.02-histoire-de-vie.md) contient :

1. **Le cadre** (objectifs, déroulement) — figé, ne pas modifier.
2. **Traces** — notes de séance, chronologiques, avec horodatage de bloc si possible.
3. **Le médecin parle** — tout commentaire clinique de Vial sur lui-même, isolé, non-dirigeant.
4. **Zones d'ombre** — cases vides repérées, jamais forcées.
5. **Prochaine étape** — une ligne : ce qui reste à faire dans cette séance ou la suivante.

## Règles de remplissage des Traces

- Format : `### [date] — [bloc]` suivi des notes en puces.
- Distinguer trois types de contenu : **dit par Vial**, **question de l'IA**, **observation de l'IA** (à marquer explicitement).
- Les nœuds (bascules) sont marqués `**NŒUD**` avec les trois questions réponses.
- Les zones d'ombre sont marquées `**ZONE D'OMBRE**` avec ce qui a été esquivé.
- Les récurrences émotionnelles sont marquées `**RÉCURRENCE**`.

## Après la séance

- Mettre à jour JOURNAL.md avec une entrée datée : ce qui a été fait, ce qui reste.
- Si une zone d'ombre a été ouverte, la mentionner dans le README de la phase concernée.
- Ne jamais modifier la phase 1 (fondations) hors ajouts de traces dans les fichiers de séance.

## Double position

Quand Vial parle en médecin de lui-même, la note va dans **Le médecin parle**, pas dans Traces. La règle du cadre 01.01 s'applique : le commentaire clinique est noté, il ne dirige pas.