# Audit indépendant de l’orchestration Modification_1_CK / Modification_2_CS

Relecteur : `/root/audit_orchestration`, modèle `gpt-6-astra`, distinct des auteurs initiaux du coordinateur et de l’extraction. Verdict : **favorable documentaire technique après corrections**, avec limites ci-dessous. Aucune validation médicale humaine ou publication n’est attestée.

## Périmètre et exclusions

Contrat, planificateur, relais, raccordement CI, tests et extraction des fonctions. Aucun contenu clinique, registre d’audits de cours, seuil, protection de fusion ou publication modifié. Le registre de réservations a été lu et laissé à son responsable. `app_v2.html` évolue pendant l’intégration clinique : aucune empreinte globale de ce fichier n’est gelée ici. Le gel technique couvre l’asset de fonctions et son manifeste ; toute modification de Gestes/CS ultérieure est hors de ce verdict.

## Défauts corrigés

| Gravité | Constat initial | Correction |
|---|---|---|
| Majeure | Publication acceptée avec commit inexistant et deux SHA inventés mais égaux ; le test initial acceptait ce faux positif. | Commit réel ancêtre de `origin/main`, SHA-256 des octets Git, chemins et URL Pages exacts, horodatage non futur, URL du run. ALPHA : cours extrait du TIP du commit. BETTA : source monographique unique et tranche publiée avec payload identique. |
| Majeure | ALPHA n’imposait pas Astra au rapport courant ; BETTA pouvait conserver un audit historique générique. | Attestation Astra et hashes actuels de cours ; registre `audits_dd` Astra lié à chaque monographie. |
| Majeure | Monographie partagée : périmètres de deux SSP pouvaient être égaux sans preuve d’adéquation au contexte. | Audit de phase BETTA lié aussi à `CONTEXTE:<SSP>` : code, titre, liste NOT. Inventaire coordination comparé au NOT actuel. |
| Majeure | GAMMA pouvait réduire son périmètre à un fichier arbitraire. | Périmètre calculé : app, CSS, JS config/stations, JSON CS. Les fichiers choisis par le registre ne réduisent plus sa couverture. |
| Majeure | `plan_adapte` pouvait clôturer une absence de DD sans livraison de l’adaptation. | Seule une décision Astra motivée `sans_differentiel_applicable` clôt une absence ; un plan adapté reste du travail. |
| Majeure | Statut inconnu ignoré, auteur répété et unités répétées contournables ; propositions encore présentes malgré anomalies. | Statuts fermés ; agents et branches uniques parmi les travaux effectivement occupés, unités uniques ; modèle/raisonnement contrôlés ; aucune proposition en cas d’anomalie. |
| Majeure | Le chemin TERMINE précédait le contrôle des réservations. | Contrôle des réservations avant clôture ; résumé seul insuffisant dans `complete()`, toutes phases favorables exigées. |
| Majeure | Monographies dupliquées écrasées silencieusement. | Détection et blocage. |
| Modérée | Code autorisant 120 s entre demandes contre 1 800 s annoncées. | Minimum de 1 800 s ; contrôle de progression toujours à 120 s. |
| Modérée | Checkout shallow susceptible de manquer les anciens commits publiés. | Récupération de l’historique avant snapshot. Test réel clone profondeur 1, ancien commit retrouvé, `origin/main` conservant le vrai sommet distant. |
| Modérée | Deux parses JS isolés ne détectaient pas une collision lexicale entre scripts. | Parse combiné supplémentaire ; test négatif `const monday` dans le principal. |
| Modérée | Lots terminés en attente de publication comptés comme agents occupés, pouvant bloquer les nouvelles réservations. | Seuls `en_redaction` et `en_audit` occupent une place ; statut et action précise présents dans la reprise. Quatre réservations dont deux `a_publier` sur la même branche d’intégration sont acceptées. |
| Modérée | Date locale Zurich rejetée à tort avant minuit UTC. | Instant `audit_utc` non futur, fuseau IANA et concordance exacte de `lu_le`. S1.3/S1.4 acceptés sans réécrire leurs rapports. |

## Ordre et reprises

ALPHA : S → F → O, deux SSP au plus par réservation. BETTA : G → S → F → O, un SSP courant, trois DD au plus par réservation. GAMMA : organisation → couleurs → fond/forme après BETTA. Les audits de phase conditionnent le passage suivant. Les métadonnées de modèle et l’indépendance annoncée font partie du contrat.

Le raccord `porte.ordre()` donne priorité au mandat courant avant les anciens critères ; un test vérifie cette priorité. Les réservations actives sont reprises avant attribution. Elles ne constituent ni activité réelle ni progrès publié. Le planificateur est un lecteur : le responsable demeure l’unique écrivain du registre avec les protections Git. Il ne garantit pas seul l’ordre des fusions entre branches parallèles, qui reste à assurer par le coordinateur. Les baux worker, agent et demande du relais restent distincts ; verrou local et CAS GitHub existants conservés. Aucun watcher ne renouvelle un bail d’agent. Une notification conserve `execution_ia_prouvee:false`.

Les audits de GAMMA portent sur le périmètre actuel complet : une modification ultérieure de couleurs ou de contenu périme aussi un audit antérieur d’organisation. Il faut reconfirmer les jalons affectés sur le nouvel état ; ils ne constituent pas une clôture irrévocable.

La fenêtre de 20 minutes, contrôlée nominalement toutes les 120 s et amorcée par cron de cinq minutes, ne garantit pas du temps réel. L’environnement Codex cloud manquant n’a pas été configuré par cet audit.

## Extraction JavaScript

Analyse indépendante du script antérieur de HEAD et de l’asset avec Acorn embarqué dans Node, utilisé seulement comme instrument d’audit : 165 nœuds extraits, tous `FunctionDeclaration`, correspondant à 165 déclarations directement globales parmi les 183 initiales. Aucun corps imbriqué, fonction asynchrone ou génératrice déplacé ; aucun `use strict` perdu. Toutes les déclarations complètes correspondent exactement à l’original.

Le script classique est chargé une seule fois, synchronement, immédiatement avant le principal. Déclarer ces fonctions ne lance aucun de leurs corps. Le garde vérifie leurs hashes/longueurs, marqueurs, absence de code ajouté et syntaxe isolée/combinée. Les six espaces historiques sont explicitement reconstructibles. Gain dans l’app : **90 444 octets**. Le SHA global historique reste informatif quand le principal évolue cliniquement ; il n’est pas présenté comme preuve d’identité de l’app actuelle entière.

## Tests exécutés

- `test_mandat.py` : 21 réussis, comprenant faux commits/hashes/URL/unités/dates, indépendance, ordre, doublons, périmètre tronqué, fin, capacité réelle, compilation monographique périmée, priorité du mandat et reprise shallow.
- `test_garde_permanence.py` : 14 réussis.
- `test_codex_cloud_120.py` : 13 réussis.
- `test_fonctions_asset.py` : 4 réussis, incluant corruption, chargement différé, code ajouté et collision entre scripts.
- `check_fonctions_asset.py` : 165 corps intacts, gain 90 444 octets.
- Planificateur sur arbre intégré : ALPHA/S, incomplet, zéro anomalie au moment du contrôle ; 248 SSP, 2 587 occurrences, 2 287 diagnostics uniques.
- `git diff --check` : réussi.

## Limites d’attestation

1. La publication est vérifiée hors ligne en cohérence avec une observation HTTP enregistrée. Le planificateur ne télécharge pas Pages ni les résultats GitHub à chaque passage. Le responsable doit réellement vérifier le run, son SHA, sa réussite et les octets publics avant de signer le rapport. Une URL syntaxiquement valide ne prouve pas seule un déploiement ; une personne pouvant modifier les preuves et le code peut fabriquer une attestation. Revue et protections Git restent nécessaires.
2. Le modèle et le relecteur sont des métadonnées, sans signature du fournisseur ; ils doivent correspondre aux agents réellement lancés. Aucune disponibilité future n’est déduite d’un fichier JSON.
3. Chromium est absent et le téléchargement Playwright a échoué. Aucun parcours UI, capture visuelle, test tactile/clavier ou mesure responsive n’est déclaré réussi ici. Les tests navigateur restent requis sur un exécuteur fonctionnel.
4. La CI du SHA final, les fusions protégées et Pages restent à réaliser. Aucun push, fusion, publication ou message externe envoyé par cet auditeur.
5. Le schéma exact des preuves et la portée des dates/contextes sont décrits dans `docs/MODIFICATIONS-1-CK-2-CS.md`.

## Gel des fichiers techniques relus

`app_v2.html` et `tools/mandat/registre.json` exclus car évolutifs pendant l’intégration. Toute modification d’un fichier gelé appelle un contrôle ciblé et un renouvellement de son empreinte.

| Fichier | SHA-256 des octets |
|---|---|
| `tools/porte.py` | `ddb539fff13763b998984409c83d08e99f77fe7dad03a0777839dbcf2ea91fd0` |
| `tools/mandat/contrat.json` | `7bc496755adc36b31f68c70398da4db8174c35625c9e50b51703cd4fe248966f` |
| `tools/mandat/planifier.py` | `0245b3b195db51c770fb6bbdbe499f6d6ab5cff4f475e4a2a1d025d3b6d21cb3` |
| `tests/test_mandat.py` | `e41c4f301cfb0c70dbb206e7f92fd3f3da1a3381be7bc9fbc2153674b74a91fd` |
| `tools/garde/permanence.py` | `9689e97e502a12aaf24e35c130d53a86d60401a32ed4bf15ecfcfc13635e706e` |
| `tools/garde/codex_cloud_120.py` | `8181ac75cb73108a32d7e93c77aef7b5a9a017c01a9f9fbb739219bf15dd6771` |
| `.github/workflows/ci.yml` | `0d2f905ecb66afac7025d80c20054dcd55518e2dbca5841d3bfbd04c01983f9c` |
| `.github/workflows/codex-cloud-120.yml` | `aebba67809458ae24d6dc327445d3e4c167b6ed9066f8f6d82ec61fa6748ad51` |
| `docs/MODIFICATIONS-1-CK-2-CS.md` | `c6b6ba22dd7e7b0b757c90d3ce3b74ee107abcb305227d1d52253930dbf75a52` |
| `tools/patches/0098-externaliser-fonctions.py` | `6830ac810e7a1d30b65d026ff6c5d4ef6482da511e7acc6cd854c4967a826ca2` |
| `tools/check_fonctions_asset.py` | `16147f18cbbf83de5904d8a7ae5e1349b2cb2e6b8fe953fe11cb8cf404844cfa` |
| `tests/test_fonctions_asset.py` | `060200437d6560087283f3241c97713f98b31c72aa13d8f9d15e315d82e62cfb` |
| `assets/config/fonctions.js` | `b7e10e34c5fbdc6a9debf2a4a6cec7c2522a1cdd3d897ddf2c80c650b505b971` |

Instant UTC du gel : 2026-10-19T22:38:12.412838+00:00.
