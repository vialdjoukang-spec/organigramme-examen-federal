# LOT_226 — Modification obligatoire du périmètre du harnais

Date : 25 octobre 2026 · Europe/Zurich.
Source : instruction explicite de Vial dans la session LOT_226.

## Différence vue et enregistrée

Ancienne portée : « Création / installation du harnais sur toi ».
Nouvelle portée : « Création / installation du harnais sur TOI ET TOUT AGENT IMPLIQUÉ DANS LE PROJET ».

## Application obligatoire

- Le responsable et chaque agent qu’il implique doivent lire HARNAIS_OBLIGATOIRE et PROMPT_HARNAIS_V8 de PROMPT_Casern et utiliser harnais/ du dépôt.
- Chacun doit exécuter bracelet_suggest dans son propre environnement et produire sa propre preuve datée, fondée sur une sortie réelle ; la preuve du responsable ne vaut pas preuve pour un autre agent.
- Le contrôle attendu du sélecteur est Chonkie 1.6, LLMLingua 1.3, GPTCache 1.3. Il s’agit de scores de suggestion, pas de versions ni d’une validation des bibliothèques.
- Aucun agent ne produit avant la validation de sa propre étape zéro et le GO explicite applicable au mandat.
- Avant chaque pas non trivial : harnais en place ? Est-il respecté ?
- La consigne doit être transmise à tout nouvel agent impliqué. Aucune installation sur un agent externe non accessible n’est présumée.

## État au moment de la sauvegarde

Le responsable a installé localement le harnais issu de main, commit ef32263eb53e8667d1becadfff2e1cb1a9eb30d8 (fusion PR #436), lu les consignes et exécuté le sélecteur avec succès. Aucun autre agent n’a été lancé ou impliqué dans cette session ; les autres sessions du projet ne sont pas déclarées contrôlées.

Commande de contrôle réellement exécutée :

```bash
python3 harnais/bracelet/bracelet_suggest.py 'LOT_226 O7.4 evidence web html document long cache'
```

Sortie, code de retour 0 :

```text
1. [filtrage_nettoyage] Chonkie (feynic/chonkie) — découper longs documents  score=1.6
2. [filtrage_nettoyage] LLMLingua (microsoft/LLMLingua) — compresser entrées longues  score=1.3
3. [reutilisation_cache] GPTCache (zilliztech/GPTCache) — cache réponses similaires  score=1.3
```

LOT_226 / SSP O7.4 demeure en attente du GO explicite, puis du oui à la question « Est-ce bien PROMPT V8 (PROMPT_Casern) que je dois utiliser ? ». Aucune rédaction des Appels A ou B n’est commencée. Aucun autre lot ni fichier partagé n’est modifié. tools/arsenal/pr.sh n’est pas exécuté. Aucun dépôt dans Drive Finaux.
