# Transition vers Codex — état réel, 25 octobre 2026

Vial a demandé un prompt de transition puis l’arrêt de cette session et de son agent associé. Ce fichier n’autorise pas à les relancer. Quand Vial transmettra ce prompt dans Codex comme nouvelle instruction, Codex pourra reprendre le mandat ci-dessous. Le prototype est sauvegardé, non activé (`paused`, `stop_requested:true`).

## Où commencer

Dépôt : https://github.com/vialdjoukang-spec/organigramme-examen-federal

Lire `AGENTS.md`, puis les instructions actuelles `PROMPT_Casern/PROMPT_ULTIME_PRODUCTION_LOTS_V8.md`, `PROMPT_Casern/PROMPT_HARNAIS_V8.md`, `PROMPT_Casern/ANTI_COLLISION_PARALLELISME_ABSOLU.md`, `harnais/HARNAIS_OBLIGATOIRE.md` et `harnais/ARSENAL.md`. Les anciens mandats S, les six rubriques DD et l’autre chaîne LOT1–10 ne remplacent pas la demande actuelle V8 inverse226→001.

Créer/installer le harnais sur le responsable ET chaque agent impliqué, exécuter bracelet et tests fonctionnels réels, consigner des preuves individuelles. Les scores Chonkie1,6/LLMLingua1,3/GPTCache1,3 sont des scores, pas des versions. Le runtime testé utilise Chonkie1.7.0, LLMLingua0.2.2, GPTCache0.1.44, torch2.14.1+cpu, transformers5.20.2. Lire `harnais/surveillance/README.md` et le probe canonique. Ne pas supposer qu’un environnement temporaire ou un modèle installé dans cette session existe dans Codex.

## Deux lots déjà rédigés

LOT226 — SSP O7.4, aspects environnementaux et psychosociaux des maladies chroniques : PR440 https://github.com/vialdjoukang-spec/organigramme-examen-federal/pull/440 ; branche `cursor/lot-226-v8-20261025`, tête502f8ff2284dc0417ddb3c6245f73a901596c36d à la dernière publication de contenu. Les cinq HTML sont sous `lot en cours de production/LOT_226/`. A reçoit80/86=93,02% à son audit documentaire, sans validation globale. Les quatre B ont142226/183412/137136/184182octets. Ils attendent leur relecture indépendante complète; aucune note B226 n’est attribuée.

LOT225 — SSP O7.3, conseil diététique : PR441 https://github.com/vialdjoukang-spec/organigramme-examen-federal/pull/441 ; branche `cursor/lot-225-v8-20261025`. Dernière tête connue6c17493216fe949bb0d5f62de9d6a1aa6d9725b1 après ajout de preuves de préparation technique; les cinq HTML restent ceux du checkpoint44d545f079653c89a844d99303c0c0cbadfaab6e. A reçoit78/88=88,64%. Les anciennes versions auditées B1/B2/B3 reçoivent86,41/82,61/79,89%; les corrections ultérieures ne haussent pas ces notes. B4 n’a pas de note indépendante. B1–B4 ont153885/158733/108389/166133octets.

Dans chaque lot, lire `STATUT.html`, `HELP` quand présent, les preuves runtime/activité, les contrôles de production, les rapports d’audit et les sources avant de reprendre. Les rapports croisés sur225 sont aussi dans226. Cadence B : DX1–2 / DX3–5 / DX6–7 / DX8–10. Les fichiers ont été sauvegardés et relus depuis GitHub; les contrôles statiques ne prouvent ni fond médical ni rendu mobile. Aucun lot n’est déclaré achevé, aucune fusion clinique et aucun Drive Finaux.

## Limite de rendu à conserver

Le navigateur de cette conversation a explicitement refusé le rendu des lots. Ne pas obtenir le même résultat par localhost, dataURL, CI de rendu, navigateur alternatif ou autre contournement. QA390 est non réalisée. Ne pas la cocher verte ni inventer une validation. Continuer les audits/corrections disponibles; consigner ce blocage s’il demeure. AIPS : les portails ouverts ne sont pas des monographies de produits vérifiées; ne jamais inventer dose, spécialité ou numéro Swissmedic.

## Automatismes installés et prototype à terminer

PR442 fusionnée : https://github.com/vialdjoukang-spec/organigramme-examen-federal/pull/442 . Le workflow `main:.github/workflows/harnais-5min.yml` est installé; code `harnais/surveillance/`, tests `tests/harnais_surveillance/`. Cron `2-59/5 * * * *`,27tests ciblés et vraie exécution des trois bibliothèques réussis dans https://github.com/vialdjoukang-spec/organigramme-examen-federal/actions/runs/40214584561 . Un premier événement `schedule` n’a pas encore été observé lors des dernières vérifications; le test PR vert ne prouve pas la récurrence. GitHub peut retarder des déclenchements. Le watcher lit des preuves publiées, pas les processus GPT, et ne renouvelle aucun heartbeat.

Le nouveau prototype se trouve sur `infra/production-inverse-v8-20261025`, dans `harnais/pilotage_lots/`, `tests/pilotage_lots/`, et une proposition de modification de `.github/workflows/harnais-5min.yml`. Lire `README.md`, `REPRISE_GPT.md`, `engine.py`, `cli.py`, `etat.json`. Ses26tests locaux passent. AUCUN contre-audit indépendant, aucune CI distante et aucun déploiement ne sont acquis pour ce prototype. La branche de registre `pilotage/lots-inverses-v8` n’est pas créée. La tâche GPT horaire n’est pas créée. Ne pas fusionner ou activer sans terminer la revue, les corrections et les contrôles appropriés.

La préférence confirmée par Vial est GitHub5min + GPT1h, car le connecteur de tâches de cette session impose au moins une heure. Vérifier les capacités réellement disponibles dans Codex. Un GPT planifié doit effectuer du travail, pas seulement rappeler son existence. Conserver sources/instructions/checkpoints sur GitHub plutôt que dépendre d’un PC ou d’un fichier local éphémère. Le solde du forfait n’est pas accessible; ne pas promettre son épuisement exact et ne contourner aucune limite.

Points à contre-auditer : indépendance et lecture réelle derrière les attestations; liaison SHA des cinq fichiers et rapports; absence de passage au suivant avant les portes; priorité des audits sur un blocage visuel; baux20min et comparaison de SHA lors de l’écriture; inventaires de réservations complets et récents; arrêt sur STOP/quota. La fonction `advance` ne publie rien elle-même : ses états doivent être enregistrés avec commit enfant et `update_ref(expected_sha,force=false)`. Le vérificateur ancien `record_activity.py` accepte encore225/226 seulement : généralisation contrôlée à un prochain lot à terminer avant de prétendre surveiller224. Le flux Drive final et les attestations de livraison doivent être vérifiés réellement; aucune case de JSON ne remplace un acte.

## Ordre de reprise quand Vial lance Codex

1. Vérifier les têtes actuelles sans écraser un travail plus récent. Préserver les instructions, les sources et tous les historiques. Reconstituer le harnais sur les deux agents réellement lancés.
2. Achever et contre-auditer le pilotage sur sa branche technique séparée. Vérifier les connexions GitHub/Drive avant une tâche qui les requiert. Éviter les doublons avec la tâche existante «Poursuivre les LOTS PROFILES», qui concerne une autre vague1–10; ne pas la modifier.
3. Reprendre les audits B226 et B225P4, corriger A225 et les réserves B225, puis réauditer exactement les versions corrigées. Ne pas réécrire aveuglément les dix HTML.
4. Passer au prochain lot libre dans l’ordre descendant seulement après les critères V8 réellement satisfaits et livraison vérifiée. Lire sa SPEC; ne pas inventer son SSP. Les LOT001–012 sont protégés tant que leurs autres propriétaires n’ont pas libéré les réservations.
5. Un agent = un lot, une branche, une PR; maximum deux agents dans ce mandat. Ne jamais écrire dans le lot d’un autre agent ni lancer `tools/arsenal/pr.sh` pendant une rédaction active. Pas de force-push, de faux audit, de score auto-approuvé ou de fusion clinique par un simple cron.

La présente session et son agent associé se sont arrêtés sur demande de Vial. Les autres tâches préexistantes et la surveillance GitHub en lecture seule n’ont pas été modifiées par cet arrêt.
