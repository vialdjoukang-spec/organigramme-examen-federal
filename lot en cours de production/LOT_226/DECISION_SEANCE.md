# DECISION_SEANCE — LOT_226 — 25 octobre 2026, Europe/Zurich

## Mandat et décision

Vial a confié le pilotage à Codex dans cette conversation : « Prends le contrôle et pilote ton projet ».
Codex consigne les choix opérationnels ci-dessous au titre de cette délégation. Cette citation ne signifie pas que Vial a répondu individuellement aux sept questions du §7 ; les choix de découpage et de répartition sont ceux du chef de production sous ce mandat.

Le référentiel est le second PDF PROMPT ULTIME V0 remis par Vial, de 31 pages, SHA-256 `75cc2d8052e7e967c3a10f3397d1b7cc31de6356ccf892881aa64c73d64c2967`. Il s'applique immédiatement, sans attente de confirmation externe. La PR447 prépare sa publication ; elle est suivie sans dupliquer ni modifier ce chantier.

## Périmètre décidé

- Le chef réattribue à la présente séance la préparation et la remise en conformité du seul LOT_226, SSP O7.4.
- La progression est ciblée sur ce lot entamé. Aucune vague descendante et aucun LOT_225, LOT_224 ou autre numéro ne sont attribués automatiquement.
- Les branches historiques et la PR440 restent intactes. Leurs auteurs, réserves et scores V8 ne deviennent pas des validations V0.
- La branche de préparation `infra/pilotage-v0-lot-226-20261025` part de `main`, commit `d63373a58f16cc854f82971d833539a6e49808a5`.
- Le chantier technique porte sur `harnais/pilotage_lots/`, ses tests et la preuve individuelle du responsable. Aucun automate existant n'est activé, modifié ou remplacé par cette séance sans revue indépendante.
- Les fichiers globaux d'application, les autres lots, les autres vagues et les tâches préexistantes sont préservés. `tools/arsenal/pr.sh` n'est pas exécuté.

## Ressources et limites réellement constatées

Un seul exécutant Codex est actif. Aucun sous-agent n'est lancé et aucun auditeur indépendant n'est réputé disponible. GitHub est accessible en lecture ; la capacité d'écriture sera vérifiée par la publication de la branche de préparation. Le solde du forfait est inaccessible. Le runtime Python local ne contenait initialement aucune des trois bibliothèques ; son installation et son test réel sont des prérequis, pas une preuve déjà acquise.

Le refus historique QA390 reste bloquant pour la validation. Aucun contournement par navigateur alternatif, localhost, dataURL ou CI de rendu n'est autorisé. Aucun dépôt Drive Finaux n'est prévu avant validation complète et vérification des octets.

## Répartition et découpage

| Intervenant | Rôle | Fichiers et actions attribués | État |
| --- | --- | --- | --- |
| Codex | Chef de production, préparation technique, futur rédacteur LOT_226 | Cette décision ; preuves individuelles ; inventaire V0 ; HELP ; moteur de contrôle technique non déployé ; Phase A après harnais vert | Actif |
| Auditeur indépendant | Audit médical puis audit linguistique/conformité, avec deux grilles séparées | Versions figées de Phase A et de chaque fichier Phase B ; identité distincte du rédacteur | Non affecté ; aucune validation possible en son absence |

La Phase B est découpée pour cette séance en dix fichiers d'une monographie : cela permet de mesurer et de réauditer chaque entité de 150–200 Ko sans imposer la cadence V8. Ce choix est propre à la séance.

- Phase A : `LOT_226_Phase_A_V0_SSP_et_10DD.html`.
- Phase B : pour chaque k de 1 à 10, `LOT_226_Phase_B_V0_Partie_<k>_DX.<k>_a_DX.<k>.html`.
- Les dix fichiers B restent fermés à la rédaction jusqu'à validation de A, gel de `LISTE_DX_CANONIQUE.md` et consignation de `CORRECTIONS_AUDIT.md`.
- Les noms exacts des dix scénarios restent à établir sur sources et à valider ; aucun gel n'est inventé à partir de la liste historique.

## Ordre de travail et portes

1. Installer et tester réellement le harnais du responsable ; dater la preuve et distinguer sélecteur, versions et résultats fonctionnels.
2. Publier cette décision et un checkpoint technique vérifiable, sans activer le prototype V8.
3. Adapter les contrôles à V0 : décision explicite, découpage variable, poids par monographie, Phase A avant B, liste canonique, deux audits indépendants et question finale « oui » obligatoire.
4. Reprendre les preuves et lacunes de Phase A du LOT_226 ; ne pas reporter son ancien score.
5. Obtenir les audits indépendants sur la version figée, puis seulement ouvrir B.
6. Ne passer à aucun autre lot sans une nouvelle attribution consignée. Un automate ne choisit jamais lui-même un numéro libre.

La préparation technique peut progresser pendant qu'un prérequis clinique manque. Elle ne vaut ni GO clinique, ni audit indépendant, ni validation du lot, ni déploiement du pilotage.

## Précision de Vial pendant la séance — densité et corpus AIPS

Vial demande un premier dossier exhaustif, sans plafond intermédiaire, pouvant dépasser largement 200 Ko. La reformulation vient ensuite : elle retire le redondant et le hors-sujet, jamais un critère, une dose ou adaptation AIPS, une alerte, un rang E, un seuil ou un examen discriminant. Le fichier final est contrôlé ligne par ligne contre V0 et chaque monographie doit atteindre 150–200 Ko de contenu propre. Le contrôle de taille final ne doit donc pas interrompre la rédaction du dossier exhaustif.

Vial signale le corpus AIPS dans `vialdjoukang-spec/Medina` et une copie annoncée dans le Drive `PROMPT_Casern`. Le chef vérifie sa structure, sa provenance, sa date et sa couverture avant d'utiliser des données médicamenteuses. La disponibilité d'un fichier ne prouve pas que chaque information professionnelle a été lue ou qu'une dose a été vérifiée.

La préférence de cadence GitHub 5 min / GPT 1 h est retenue pour étude d'intégration. Le workflow existant reste inchangé ; aucune tâche horaire n'est activée dans cette séance de préparation.

## Reprise autorisée — 25 octobre 2026

Instruction actuelle de Vial : « continue le Travail de Codex sur Organigramme ». La présente reprise conserve LOT_226, sa branche, son chef de production, son découpage et les exclusions déjà décidées. Elle reprend la PR453 ; elle n’attribue aucun autre lot et ne crée aucun rôle d’audit indépendant.

Le test canonique individuel a réussi dans le nouvel environnement avec les versions du watcher existant. La collecte de sources et la rédaction manuelle de Phase A peuvent donc reprendre. Le moteur reste arrêté jusqu’au contre-audit indépendant et aux autres portes documentées. Les corrections techniques de cette reprise n’activent aucun workflow.
