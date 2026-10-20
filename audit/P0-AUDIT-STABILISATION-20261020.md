# P0 · stabilisation et assainissement · 20.10.2026

**Statut : en cours ; CI finale, fusion et publication des correctifs encore requises.** Aucune modification de contenu clinique ni de présentation. Le mandat courant est `docs/MANDAT-REMASTERING-P0-P4.md`.

## État vérifié et périmètre

Main initial : `3e940e2a151aa4583d0fccae8f466ae9a681268b`. CI `39396371174`, Pages `39396431006` réussis. Contrôle visuel final de PR159 : `39395506228`, tête `1bd1c71d5c3fa2963a78cb1f338b1e1843ecbf3b`, réussi. La protection GitHub est illisible par cette intégration (HTTP403), sans modification des règles ; les contrôles minimaux sont imposés indépendamment.

Catalogue réel : G16/S113/F44/O75 =248SSP,3472parties. `controler.py` reconnaît54cours/756parties contre-audités documentaires (G16,S38), sans validation médicale humaine. S3.4/S3.5 ont été intégrés par `9f733ac` sans contre-audit enregistré ; leur achèvement n’est pas acquis. La preuve réseau `P0-PUBLICATION-BASELINE-20261020.json` compare114fichiers (application, progression et tous les assets) : HTTP200 et SHA-256 identiques au main initial. Elle permet d’enregistrer les publications manquantes S3.2/S3.3 ; le planificateur reconnaît désormais38/113S. Premier travail P1 après clôture P0 : contre-audit S3.4/S3.5 existants, avant #161.

106PR ouvertes inventoriées :1techniqueP0,25ALPHA et1supportdocumentaire/P1,74BETTA/P3,1GAMMA/P4,4historiques/pilote. Le rapport `P0-FILE-PR-20261020.json` conserve numéro, branche, SHA, ordre et dépendances ; aucune PR clinique ni branche supprimée. Aucun auto-merge actif observé. Les titres ne certifient pas le périmètre réel, qui sera vérifié à chaque lot. Aucun ancien registre ni fermeture de PR ne vaut publication.

## Anomalies et corrections techniques

1. Anciennes chaînes autorisant les PR inconnues et les anciennes phases : barrière commune depuis la configuration canonique de main ; liste technique explicite numéro/SHA/priorité ; clinique centralisée manuellement. Liste initialement vide ; pas d’autorisation implicite.
2. Deux voies de fusion indépendantes : auto-fusion et file utilisent maintenant le même garde, qui refuse toute lecture invalide ou périmètre clinique. Le worker n’utilise plus les anciennes chaînes comme autorisation.
3. Workflow modifiable depuis une PR : `pull_request_target` et checkout main exclusivement ; aucun code de PR exécuté par ce workflow privilégié. Pas d’auto-merge différé : fusion immédiate sur SHA exact seulement.
4. CI incomplète ou ambiguë : garde/html/tests/visuel/checkpoint/schemas exigés SUCCESS, autres contrôles bloquants s’ils échouent ou attendent. Une observation GitHub associe la tête aux contrôles ; SHA différent ou contrôle requis ignoré refuse le vert. La configuration et l’état complet sont relus avant fusion ; la fenêtre API résiduelle est documentée, sans prétendre à une transaction.
5. Arsenal réécrivant l’historique : merge normal de main et push normal ; tests avec vrai dépôt distant prouvent conservation des commits et refus d’écraser un travail concurrent connu.
6. Faux positif concentration dans l’arsenal et défaut de PR202 : concentration µg/L exclue, doses/24h et doses/kg avec espaces toujours détectées. Le garde AIPS principal reste intact. PR202 reste conservée tant que la correction n’est pas intégrée et auditée.
7. G3 autorisant des voisins par simple préfixe : chemin exact par défaut, sous-arbre seulement avec slash terminal explicite ; cinq anciennes règles réduites aux chemins exacts déjà utilisés, aucun pays ni hôte ajouté. Tests de collision de DOI, domaine ressemblant et traversée de chemin. Les deux ajouts proposés dans PR229 restent à documenter pour les lots concernés ; pas d’autorisation large accordée.
8. Catalogues SRC hérités hors lot : audit des74BETTA,17blobs SRC et477blobs canoniques distincts.22candidats de retrait de131occurrences orphelines, avec archives intégrales et asset SRC produit par le compilateur officiel. Les22commits conservant les131références en archives sont appliqués, avec contrôle des3seuls chemins modifiés : `P0-NETTOYAGE-APPLIQUE-20261020.json`. Le contre-audit couvre aussi1611fichiers actifs supplémentaires sur les22arbres ; aucune référence supprimée n’y est utilisée. Les22refus G3 restants sont conservés (projection contre le code et la politique P0) ; cela ne vaut pas CI verte des PR futures.
9. Suivi contradictoire : mandat P0–P4 et checkpoints en tête des documents ; catalogue d’outils complété, porte0 complète ; planificateur explicitement P0/stabilisation, sans attribution ni reprise clinique ; publications S3.2/S3.3 enregistrées avec preuve réseau réelle. Les instructions historiques restent disponibles.

## Audits, contrôles et limites

Les deux agents de diagnostic sont devenus auteurs de leurs propositions ; leurs propres rapports ne valent pas contre-audit de ces modifications. Le contre-audit final indépendant est réalisé par `/root/p0_contre_audit`, modèle `gpt-6-astra` réellement demandé, avec empreintes des fichiers dans `P0-CONTRE-AUDIT-TECHNIQUE-20261020.json`. L’analyse de sources et le nettoyage ont leur rapport indépendant distinct. Aucun médecin n’a validé ce correctif technique.

Tests ciblés : garde/file de fusion, observation CI, historique Git, arsenal, périmètres G3, socle CK82contrôles, cours18tests et contrat de mandat. La CI GitHub sur la tête finale demeure l’autorité pour les parcours navigateur, le visuel et les autres gardes. Aucun seuil, budget, source, référence visuelle ni contrôle n’est assoupli.

Les refus G3 restant sur des sources réellement utilisées relèvent de leurs lots cliniques P3 : pays ISO invalide, document hors liste ou éditeur non vérifié. Ils restent refusés ; aucune lecture réseau refusée n’est déclarée accomplie. Ils ne sont pas des défaillances du garde. Les PR futures restent suspendues pendant P0 ; aucune rédaction P1–P4 engagée.

## Reprise exacte

Exécuter les tests ciblés, relire le contre-audit, ouvrir la PR technique avec « Automates actifs », attendre tous les contrôles sur son SHA exact, fusionner sans `--admin` ni force-push, observer le run Pages du commit intégré puis comparer les octets publics. Consigner ensuite le bilan et fermer P0 seulement si les critères sont tous prouvés. Un watcher ou un commentaire ne prouve pas une IA autonome ; aucun dispositif permanent de production n’est revendiqué.
