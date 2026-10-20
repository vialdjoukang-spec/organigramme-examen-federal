# P0 · stabilisation et assainissement · 20.10.2026

**Correctifs P0 audités, fusionnés et publiés ; clôture documentaire à fusionner et publier avant démarrage P1.** Aucune modification de contenu clinique ni de présentation. Le mandat courant est `docs/MANDAT-REMASTERING-P0-P4.md`.

## État vérifié et périmètre

Main initial : `3e940e2a151aa4583d0fccae8f466ae9a681268b`. CI `39396371174`, Pages `39396431006` réussis. Contrôle visuel final de PR159 : `39395506228`, tête `1bd1c71d5c3fa2963a78cb1f338b1e1843ecbf3b`, réussi. La branche est protégée et expose garde/html/tests/visuel obligatoires ; le détail intégral de protection reste illisible (HTTP403). Aucune règle n’a été modifiée ; les six contrôles de la barrière P0 ont été vérifiés.

Catalogue réel : G16/S113/F44/O75 =248SSP,3472parties. `controler.py` reconnaît54cours/756parties contre-audités documentaires (G16,S38), sans validation médicale humaine. S3.4/S3.5 ont été intégrés par `9f733ac` sans contre-audit enregistré ; leur achèvement n’est pas acquis. La preuve réseau `P0-PUBLICATION-BASELINE-20261020.json` compare114fichiers (application, progression et tous les assets) : HTTP200 et SHA-256 identiques au main initial. Elle permet d’enregistrer les publications manquantes S3.2/S3.3 ; le planificateur reconnaît désormais38/113S. Premier travail P1 après clôture P0 : contre-audit S3.4/S3.5 existants, avant #161.

106PR ouvertes inventoriées :1techniqueP0,25ALPHA et1supportdocumentaire/P1,74BETTA/P3,1GAMMA/P4,4historiques/pilote. Le rapport `P0-FILE-PR-20261020.json` conserve numéro, branche, SHA, ordre et dépendances ; aucune PR clinique ni branche supprimée. Aucun auto-merge actif observé. Les titres ne certifient pas le périmètre réel, qui sera vérifié à chaque lot. Aucun ancien registre ni fermeture de PR ne vaut publication.

## Anomalies et corrections techniques

1. Anciennes chaînes autorisant les PR inconnues et les anciennes phases : barrière commune depuis la configuration canonique de main ; liste technique explicite numéro/SHA/priorité ; clinique centralisée manuellement. Liste initialement vide ; pas d’autorisation implicite.
2. Deux voies de fusion indépendantes : auto-fusion et file utilisent maintenant le même garde, qui refuse toute lecture invalide ou périmètre clinique. Le worker n’utilise plus les anciennes chaînes comme autorisation.
3. Workflow modifiable depuis une PR : `pull_request_target` et checkout main exclusivement ; aucun code de PR exécuté par ce workflow privilégié. Pas d’auto-merge différé : fusion immédiate sur SHA exact seulement.
4. CI incomplète ou ambiguë : garde/html/tests/visuel/checkpoint/schemas exigés SUCCESS, autres contrôles bloquants s’ils échouent ou attendent. Une observation GitHub associe la tête aux contrôles ; SHA différent ou contrôle requis ignoré refuse le vert. La configuration et l’état complet sont relus avant fusion ; la fenêtre API résiduelle est documentée, sans prétendre à une transaction.
5. Arsenal réécrivant l’historique : merge normal de main et push normal ; tests avec vrai dépôt distant prouvent conservation des commits et refus d’écraser un travail concurrent connu.
6. Faux positif concentration dans l’arsenal et défaut de PR202 : concentration µg/L exclue, doses/24h et doses/kg avec espaces toujours détectées. Le garde AIPS principal reste intact. PR202 fermée après intégration et audit du correctif ; sa branche reste conservée.
7. G3 autorisant des voisins par simple préfixe : chemin exact par défaut, sous-arbre seulement avec slash terminal explicite ; cinq anciennes règles réduites aux chemins exacts déjà utilisés, aucun pays ni hôte ajouté. Tests de collision de DOI, domaine ressemblant et traversée de chemin. Les deux ajouts proposés dans PR229 restent à documenter pour les lots concernés ; pas d’autorisation large accordée.
8. Catalogues SRC hérités hors lot : audit des74BETTA,17blobs SRC et477blobs canoniques distincts.22candidats de retrait de131occurrences orphelines, avec archives intégrales et asset SRC produit par le compilateur officiel. Les22commits conservant les131références en archives sont appliqués, avec contrôle des3seuls chemins modifiés : `P0-NETTOYAGE-APPLIQUE-20261020.json`. Le contre-audit couvre aussi1611fichiers actifs supplémentaires sur les22arbres ; aucune référence supprimée n’y est utilisée. Les22refus G3 restants sont conservés (projection contre le code et la politique P0) ; cela ne vaut pas CI verte des PR futures.
9. Suivi contradictoire : mandat P0–P4 et checkpoints en tête des documents ; catalogue d’outils complété, porte0 complète ; planificateur explicitement P0/stabilisation pendant la stabilisation, sans attribution ni reprise clinique ; P0 conservé dans cette clôture et activation P1 seulement après preuve de publication ; publications S3.2/S3.3 enregistrées avec preuve réseau réelle. Les instructions historiques restent disponibles.

## Audits, contrôles et limites

Les deux agents de diagnostic sont devenus auteurs de leurs propositions ; leurs propres rapports ne valent pas contre-audit de ces modifications. Le contre-audit final indépendant est réalisé par `/root/p0_contre_audit`, modèle `gpt-6-astra` réellement demandé, avec empreintes des fichiers dans `P0-CONTRE-AUDIT-TECHNIQUE-20261020.json`. L’analyse de sources et le nettoyage ont leur rapport indépendant distinct. Aucun médecin n’a validé ce correctif technique.

Tests ciblés : garde/file de fusion, observation CI, historique Git, arsenal, périmètres G3, socle CK82contrôles, cours18tests et contrat de mandat. La CI GitHub sur la tête finale demeure l’autorité pour les parcours navigateur, le visuel et les autres gardes. Aucun seuil, budget, source, référence visuelle ni contrôle n’est assoupli.

Les refus G3 restant sur des sources réellement utilisées relèvent de leurs lots cliniques P3 : pays ISO invalide, document hors liste ou éditeur non vérifié. Ils restent refusés ; aucune lecture réseau refusée n’est déclarée accomplie. Ils ne sont pas des défaillances du garde. Les PR futures restent suspendues pendant P0 ; aucune rédaction P1–P4 engagée.

## Preuves de livraison et bilan

PR [268](https://github.com/vialdjoukang-spec/organigramme-examen-federal/pull/268), tête finale `a60232967dab20a4b5e924a90768a249da4bd4c6` ; CI39410475983, Visuel39410476041 et Checkpoint39410475984 réussis sur cette tête. Les six contrôles requis sont verts (`P0-CI-TETE-20261020.json`). Fusion normale, sans contournement : `b22c1b41f88bc132b94e021bb9eb6f459e8dfa13`, arbre identique à la tête auditée. CI main39411571707 réussie. Pages39411579782 réussi sur ce même commit ;114 réponses HTTP200 avec SHA-256 identiques (`P0-PUBLICATION-CORRECTIFS-20261020.json`). Le test visuel final constate60comparaisons sans différence, aucune nouvelle violation axe sérieuse/critique ni débordement mobile ; il ne certifie pas la future charte P4 sur l’interface historique.

Six rapports d’un même contre-auditeur indépendant Astra couvrent le code technique, les sources, la documentation, le planificateur, les clones Git et les permissions. `P0-AUDIT-MANIFESTE-20261020.json` lie les20fichiers de code à leur dernière empreinte auditée. Le contre-audit documentaire de clôture est ajouté séparément ; aucune attestation humaine médicale.

| Indicateur | Résultat |
|---|---|
| Priorité | P0 |
| Tâches prévues / achevées | 9 groupes techniques / 9 correctifs livrés ; clôture documentaire dans cette proposition |
| Anomalies / corrections | 9 groupes / 9 ;22branches,131occurrences inutilisées archivées |
| Audits indépendants | 1contre-auditeur Astra,6rapports techniques/documentaires ; clôture relue séparément |
| Tests / CI | Six contrôles de tête verts ; CI main réussie ; tests ciblés, navigateur et visuel réussis |
| PR fusionnées | #268 ; #202 close comme remplacée, branche conservée |
| Commit des correctifs | `b22c1b41f88bc132b94e021bb9eb6f459e8dfa13` |
| Publication | Pages39411579782 réussi,114fichiers200identiques |
| Reliquat P0 | Fusion/CI/publication de cette clôture documentaire ; aucun correctif de code bloquant restant identifié |
| Priorité suivante | P1 : audit S3.4/S3.5, puis reprise des PR ALPHA dans l’ordre du catalogue |

## Limites et reprise exacte

L’inventaire actualisé compte105PR historiques ouvertes après fermeture202 ;150est en brouillon, pour P4. Les états de conflit post-fusion étaient inconnus lors du dernier relevé et ne sont pas assimilés à une absence de conflits. Les71DIRTY/35BEHIND historiques ne sont pas des valeurs actuelles. Chaque lot futur exige réconciliation, audit et CI sur sa tête finale. Aucun doublon clinique n’a été supprimé, aucune branche effacée. Les22refus G3 projetés sur des sources utilisées restent bloquants pour les futurs lots concernés ; ce n’est pas un dysfonctionnement technique.

Attendre le contre-audit et la CI de la clôture documentaire sur sa tête exacte, fusionner et vérifier sa publication, puis confirmer P0 et exécuter P1. La configuration reste à P0 pour empêcher matériellement toute attribution anticipée ; activer P1 dans une transition distincte après ces preuves. Un watcher ou un commentaire ne prouve pas une IA autonome ; aucun dispositif permanent de production n’est revendiqué.
