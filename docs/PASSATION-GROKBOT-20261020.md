# Passation à Grokbot · 20 octobre 2026

## Décision de Vial et responsabilité

Le 20.10.2026 à 07:51 Europe/Zurich, Vial a donné l’ordre : « Grokbot reprends la suite. Repose toi. Transfert lui tes droits ».

**Grokbot reprend la responsabilité opérationnelle. ChatGPT arrête sa production et ses agents.** Les autorisations déjà données par Vial couvrent la lecture, la rédaction, les corrections, les branches, les audits, les PR, les fusions protégées et la publication dans ce dépôt, sans nouvelle demande entre les lots. Les décisions courantes lui reviennent dans ce périmètre. Tous les livrables restent dans `vialdjoukang-spec/organigramme-examen-federal`.

Cette passation transmet le mandat et les autorisations de travail. Elle ne modifie pas les permissions techniques de GitHub : aucun compte GitHub « Grokbot » n’a pu être identifié dans les PR/commentaires examinés, et le connecteur disponible ne permet pas d’ajouter un collaborateur ou de modifier son rôle. Grokbot utilisera les accès de sa propre connexion ; aucun identifiant ou secret n’est transmis. Sa réception et son démarrage ne sont pas présumés.

## État publié réellement vérifié

Base de reprise : `main`, commit **`83ab692a171000775e45dfa43a4a72d289eeeb3f`**, fusion de la [PR151](https://github.com/vialdjoukang-spec/organigramme-examen-federal/pull/151) le 20.10 à 01:49:18 UTC.

- **52/248 cours, 728/3472 parties** : G1–G16, S1.1–S1.23, S2.1–S2.12 et S3.1.
- Dans la catégorie S : **36/113 cours** publiés ; prochain cours **S3.2**. Il reste 77 S, puis 44 F et 75 O pour ALPHA.
- CI main `39355542367` : garde, HTML, schémas et tests réussis. Visuel PR `39354809465` réussi. Pages `39355549019` et `39355542445` réussis.
- Contrôle HTTP effectué pendant la passation : **15 adresses HTTP 200 et octets identiques au commit publié**, dont `index.html`, `app_v2.html` et `assets/config/tip.js`. Preuve : `audit/PUBLICATION-ALPHA-S1.11-S3.1-20261020.json`.
- Le contrôle des liens de PR151 conserve trois erreurs réseau sur 200 URL : deux délais dépassés sur `revmed.ch` et une connexion refusée sur `worldgastroenterology.org`. La CI globale de PR n’est donc pas présentée comme entièrement verte. Les contrôles requis documentés `garde`, `html`, `tests`, `visuel` ont réussi ; aucun assouplissement TLS.

## Travaux ultérieurs non récupérables : ne pas les compter

Les anciennes notes annoncent des lots S3.2–S4.7 préparés ou audités localement. Ils n’avaient pas été poussés. Après le nettoyage automatique de l’espace temporaire, les worktrees ne sont plus présents ; les 22 branches distantes et les références exactes du registre ont été contrôlées. Les sept commits de lots S3.2–S4.5 renvoient « No commit found » (HTTP 422). Aucun livrable de S4.6–S4.7 n’est récupéré.

Ces réservations sont clôturées avec le statut `annule`, motif de passation et références historiques conservées. **Aucun de ces lots ne vaut relecture ou publication acquise.** Reprendre S3.2 depuis `main`, sauf récupération ultérieure des objets réels, suivie d’une nouvelle vérification des empreintes et de l’audit. Les 52 cours fusionnés sont intacts.

## Ordre de travail à conserver

1. **ALPHA** : finir S, puis F, puis O ; deux cours au plus par lot/agent, chacun avec ses 14 parties spécifiques. La demande initiale utilise GPT-6 élevé et des contre-audits indépendants Astra : médecine, fond, forme, concision, précision. La PR153 propose l’autorisation explicite de `grok-bot` comme contre-auditeur, avec indépendance et dates conservées ; Grokbot reprend cette modification. Noter les modèles réellement exécutés, sans fabriquer de signature Astra. Audit de catégorie et publication vérifiée avant la suivante.
2. **BETTA** : après ALPHA, G → S → F → O, un SSP à la fois ; trois différentiels au plus par lot de rédaction et par audit indépendant. Plan monographique de six rubriques, avec adaptation justifiée lorsque nécessaire. Ne jamais appliquer ce plan aux 14 parties du cours SSP.
3. **GAMMA** : après BETTA, régions cliquables sur une ligne symétrique, hauteur uniforme, couleurs distinctes ; temps de l’examen à gauche et image pertinente à droite. La [PR150](https://github.com/vialdjoukang-spec/organigramme-examen-federal/pull/150) est un brouillon à conserver pour cette étape, pas un travail terminé. Les descriptions des 315 Gestes sont temporairement suspendues avec l’accord de Vial ; clés, liens et progression sont conservés.

## Travaux Grokbot déjà ouverts

Au moment de la passation, deux propositions nouvelles sont visibles sous le compte propriétaire : [PR152](https://github.com/vialdjoukang-spec/organigramme-examen-federal/pull/152), BETTA G2 avec trois différentiels, et [PR153](https://github.com/vialdjoukang-spec/organigramme-examen-federal/pull/153), acceptation documentaire du contre-auditeur `grok-bot` citant un ordre de Vial à 07:40. Elles ne sont ni modifiées ni fusionnées par ChatGPT. Grokbot reprend leur validation et vérifie leur ordre d’intégration avec les dernières instructions de Vial ; la présente passation ne prétend pas que toute la phase ALPHA est terminée.

## Supports et contrôles

Lire `AGENTS.md`, `docs/MODIFICATIONS-1-CK-2-CS.md`, `docs/PROMPT-DIRECTEUR-ACADEMIQUE.md`, puis lancer `python3 tools/mandat/planifier.py`. Les cours canoniques sont `data/tip/<SSP>.json` ; `tools/cours/appliquer.py <SSP>` applique un lot relu et régénère `assets/config/tip.js`. Le HTML mesure 440 518 octets ; les 248 cours restent complets dans les fichiers du dépôt. Ne pas remplacer l’application entière par celle d’une ancienne branche.

Conserver DD, fondamentaux, sources, visas hérités et marqueurs d’examen `§`, `¶`, `@`, chacun sur sa ligne. Sources primaires CH/Europe lues et datées ; exception internationale limitée à la définition `c[0]`. Doses AIPS suisse seulement, sinon réserve précise. Audits liés aux 14 empreintes réelles, aucune validation humaine inventée. Gardes, Lyncée, compilateurs, tests navigateur et comparaison visuelle avant fusion normale par commit de fusion ; contrôle des octets publics après Pages.

## Arrêt et relais

Le bail de ChatGPT est libéré et aucun agent de rédaction ou d’audit de cette session ne poursuit. La configuration du relais **Codex** est mise à `enabled:false` dans cette passation pour éviter une reprise concurrente ; ce réglage devient effectif après fusion. Il ne constitue pas un relais Grokbot. Le connecteur Codex signalait un quota épuisé et aucune exécution distante n’était prouvée. Grokbot pourra mettre en place son propre mécanisme de reprise dans le dépôt en indiquant ses capacités réelles.
