# ETAT · pilotage Codex (lu par tools/porte.py)

Étape courante : voir `ETAT.json` (`python3 tools/porte.py etat`). Feuille de route : `CONTINUATION.md` (tableau en tête) et `tools/etapes.json`.
Légende : [x] fait · [ ] à faire. **Aucune étape de contenu (1 et suivantes) ne commence tant qu’une case ci-dessous reste vide** (`python3 tools/porte.py commencer 1` refuse).

## Porte de l’Étape 0 (installation, bloquante)

<!-- PORTE-ETAPE-0 -->
- [x] 0.1 J’ai lu AGENTS.md, puis CONTINUATION.md en entier (toutes les étapes, toutes les règles), puis HANDOFF.md (tête), ce fichier, PROCHAINE_ACTION.md
- [x] 0.2 J’ai lu docs/skills/README.md et les skills ssp-continuite, ssp-verite, ssp-posologie-suisse, ssp-audit-medical, ssp-fusion-patch, ssp-pilotage-codex
- [x] 0.3 Catalogue : `python3 tools/catalogue.py` lancé, sections « À COMPLÉTER PAR CODEX » remplies (MCP, skills de Codex), CATALOGUE.md présenté avant de commencer
- [x] 0.4 Proposition de skills : `python3 tools/propose_skills.py` lancé, docs/skills/PROPOSITIONS.md écrit et lu
- [x] 0.5 Veille de relance installée et testée (`bash tools/veille_relance.sh --une-fois --dry-run`), puis lancée (cron ou boucle) ; mode A ou B noté ci-dessous
- [x] 0.6 Droits de fusion vérifiés (`bash tools/file_fusion.sh --droits` : admin=true, merge_commit=true) ; file de fusion testée (`bash tools/file_fusion.sh --dry-run`)
- [x] 0.7 Modèle des tâches répétitives réglé : GPT 6 Luna (`gpt-6-luna`), ou modèle de secours noté ci-dessous
- [x] 0.8 Worktree de travail créé depuis origin/main (jamais de changement de branche dans /workspace/oef) ; tests de base OK (`python3 tests/run_tests.py` ou motif d’échec noté)
- [x] 0.9 Jauges lues (`python3 tools/jauge/binomes.py`) et valeur de départ notée ci-dessous
<!-- /PORTE-ETAPE-0 -->

## Réglages notés par Codex à l’Étape 0

- Mode de relance (A = `codex exec`, B = PROCHAINE_ACTION.md) : B (CLI présent mais authentification refusée ; aucun second agent CLI lancé)
- Lancement de la veille (commande exacte, cron ou boucle) : `nohup bash tools/veille_relance.sh --boucle 180 --sans-codex > .etat_local/veille_stdout.log 2>&1 < /dev/null &` ; PID dans `.etat_local/veille.pid` ; boucle locale seulement pendant la durée de vie de cet environnement
- Modèle des tâches répétitives : `gpt-6-luna` configuré pour la CLI, dont l’authentification échoue en HTTP 401. Aucun sous-agent lancé. Modèle courant pour les réparations/relectures ; scripts déterministes pour les inventaires. La rédaction de masse autonome reste indisponible, sans prétendre qu’un autre modèle CLI fonctionne.
- Jeton de fusion (gh de Codex, ou secret AUTO_FUSION_TOKEN) : gh de Codex, intégration GitHub (`admin=true`, `push=true`, `merge_commit=true`, `auto_merge=true`, `squash=false`), protection non lisible (403) (ne jamais écrire le jeton lui-même)
- Jauges au départ : Prévalences 0 % (0/2578) · Monographies 3 % (70/2280) le 18.10.2026 00:45 (Europe/Zurich)

## Journal des étapes (une ligne par fin d’étape ou de lot : date, étape, lot, PR, résultat)

- 18.10.2026 · Étape 0 préparée par Grok Bot (scripts, porte, veille, file de fusion) ; à exécuter par Codex.

- 18.10.2026 01:04 Europe/Zurich · Étape 0 en cours dans `/workspace/oef-codex`, branche `codex/etape-0` depuis origin/main 2228be7. Catalogue généré, complété, présenté et recopié dans PROCHAINE_ACTION.md. Propositions lues ; skill ssp-construction-ck créé. Veille testée en dry-run puis lancée en mode B. Droits de dépôt confirmés ; lecture de protection refusée 403, aucune modification de protection. Tests initiaux : Chromium manquant, installation effectuée puis suite relancée. Jauges : 0/2578 prévalences (0 %), 70/2280 monographies (3 %).

- 18.10.2026 01:05 CEST · Étape 1 : PR ouvertes et checks de toutes les chaînes lus ; § C1 corrigé avec l'instantané réel. Pages = main (SHA-256 ci-dessus). Sauvegardes Grok absentes, branches distantes présentes ; aucun patch privé reconstitué. Jauges inchangées 0 %/3 %, contrôle jauge OK. PR Étape 0 : #71, auto-merge demandé, CI en cours.

- 18.10.2026 01:08 CEST · Étape 2 : corrections de la file/auto-fusion préparées et testées (5/5), workflow file-fusion déclenché ; deux sondes #71/#73 avec auto-merge MERGE actif. Résultat de bout en bout encore en attente des contrôles ; ne pas annoncer fusion/publication réussies. Poursuite Étape 3 selon R7 ; la file reprend les sondes.

- 18.10.2026 · Complément Étape 2 : #71 fusionnée automatiquement (843e2c3) après contrôles verts, Pages réussi sur le même SHA. Preuve de bout en bout obtenue ; #73 reste sonde supplémentaire. Le nohup initial a été terminé par l'environnement ; veille relancée au premier plan dans une session d'exécution persistante (`bash tools/veille_relance.sh --boucle 180 --sans-codex`, journal confirmé). Playwright local initial 1.62 différent de la CI : venv `/workspace/venv_ck` créé avec 1.63 et Chromium 1243.

- 18.10.2026 01:15 Europe/Zurich · Étape 3 traitée, fusions en attente : #43 fusionnée ; #44/#45 main intégré et correctifs Galien rejoués, suites locales lancées avant push ; #58 onze chiffres relus (Limper/BASEL IX), trois nouvelles fiches contre-lues avec ESGE/HAS/ESC, cadre et indications corrigés, audit écrit, contrôles de données verts, suite 1.63/push planifiés ; #47 fusion de main, toutes sections du rapport conservées, poussé et audit-ok. La file reprend les fusions. Étape 3 reste dans ETAT.json.en_attente tant que le critère n'est pas vert.

- 18.10.2026 · Étape 4 traitée, fusions/audit en attente : #50/#53/#54/#49 main intégré, shards résolus par le script sans conflit réel signalé, migration 0026 rejouée (elle était encore sur #50, contrairement à la relève), assets régénérés, suites 1.63 et pushes en file sous verrou. #64 : 25 fiches relues, sources hypothermie suisses relues ; doses non auditées et chiffres hors CH/UE remis À vérifier, cadre de cohorte corrigé ; signalement HOPE/décès potentiellement critique, label attente-vial et rapport rouge. Aucune fusion de #64 sans validation de Vial. Les labels #53/#54 attendent la fusion de la précédente.

- 18.10.2026 · Étape 5 traitée, fusions en attente : #60/#62 mises à jour avec main ; shards par merge_shards sans conflit réel signalé ; toutes sections d'audit conservées ; patch 0026 et assets reconstruits ; suites 1.63/pushes dans la file locale. Audits Érasistrate existants conservés, aucune nouvelle validation clinique.

- 18.10.2026 UTC · Étape 6 : 98 lignes/73 documents AIPS officiels relus, contrôles verbatim sans écart, quatre rapports poussés ; réserves KCl/aciclovir et attente-vial #67/#70 conservées.
- 18.10.2026 UTC · Étape 7 : #65/#68 reprises ; 166 définitions relues, sept corrections, baseline #68 à 3567 ; #65 resserrée à 3820, mais 92 candidats nouveaux restent à examiner.
- 18.10.2026 UTC · Étapes 8–11 INACHEVÉES : G5 #85 (44 DD sur quatre SSP, chiffres inconnus explicites) ; brouillons monographiques hors git ; inventaires de doses/glossaire. Aucun seuil de boucle ni couverture complète déclaré ; CLI de masse en 401. Passage R7 aux travaux suivants.
- 18.10.2026 UTC · Étape 12 : #83 restaure 72 titres critiques, captures ciblées relues, contraste clair 6,77:1 ; #84 corrige la réouverture après Fermer, reproduction 4/4 corrigée et suite 276/276. Audit transversal restant.
- 18.10.2026 UTC · Étapes 13–15 : #39/#41 reprises ; #80 prototype VII et #81 urgences lot 3 en brouillon, audits/validation Vial restants ; cinq stations pilotes restent valide_par_vial=false. Aucun accord inventé.
- 18.10.2026 UTC · Étape 16 : #32 reprise et captures de fond pâle relues (contraste secondaire/fond 8,55:1) ; #37 retrouvée sur origin, patch rejoué (60 DD S8), audit final restant. #16 fermée avec motif, branche conservée ; #56/#63 fermées comme remplacées.
- 18.10.2026 UTC · Incident : #62 fusionnée avant #60 le 17.10 à 23:55:43 UTC ; l’auto-fusion n’imposait pas les chaînes. #82 ajoute ce verrou, cinq tests dédiés et cinq tests de file réussis. Pas de réécriture de l’historique.
- 18.10.2026 UTC · Étape 17 contrôlée, NON VALIDÉE : jauges main 1 % et 4 %, Pages identique au SHA-256 de main 67ae383 à 00:00:20 UTC. Relève complète dans docs/releves/RELEVE_CODEX_20261018.md. Veille conservée ; reprise de la boucle 8, pas de fin du projet.

- 18.10.2026 00:52 UTC · Réconciliation des attentes : #45/#58/#60/#39/#84/#82 fusionnées. Étape 3 complète ; données des deux lots de l’étape 5 intégrées, incident #62 avant #60 conservé. Main : 38/2587 prévalences (1 %), 130/2287 monographies (6 %). Suite main 42a432d : 276/276. Pages = main 8dd0d0a (HTTP 200, SHA-256 9e4720c6ce86056e4648eaa8744fe183479d9ddbf6419f1bb13ad60d8a800969).
- 18.10.2026 UTC · Glossaire : #65 baseline 3735 après 139 entrées de main, neuf définitions et 45 définitions de compatibilité déjà relues dans #68. #68 : 527 entrées réunies, baseline 3571, neuf exclusions cliniques supprimées. G1/G2/G3/G6, Lyncée et quatre tests de migration passent. Aucun label #68 avant fusion #65. Les 38 candidats de migration hérités restent explicitement examinés dans le rapport.
- 18.10.2026 UTC · G5 #85 rejoué sur main après #58 ; union de prévalences et sources sans conflit réel, app repris de main et registres régénérés. Chiffres inconnus conservés. La chaîne historique prev reste #43→#44→#45→#58 ; chaîne séparée prev_g5 #58→#85 pour ne pas déplacer le critère de l’étape 3.

- 18.10.2026 01:15 UTC · #50, #53, #54 et #86 fusionnées ; main contient 207/2287 monographies (9 %), prévalences 38/2587 (1 %). Pages et quatre fichiers JS (mono-s, prev, glo-index, src) identiques à main 51cb2e5, HTTP 200. Les étapes 8–11 restent incomplètes.
- 18.10.2026 UTC · #65 : dix termes supplémentaires traités sans admission en référence, 406 entrées et baseline 3734 ; correctif 0030 des commandes calendrier, 74 contrôles CK UI et suite complète 276/276. #68 réuni : 535 entrées, baseline 3571 ; conflit hypertrophie résolu par source Larousse relue avec alias/flexions conservés. CI et fusion #65 avant #68 restent requises.
- 18.10.2026 UTC · #32 : adoption examinée de la référence CI (8c3e800) par script habituel sur runner, après refus local des artefacts en 403. Mesures 60 captures : zéro hausse axe grave/critique, débordement, clipping, police ou erreur JS ; CLS de référence 0,1347→0,0358, aucun seuil de configuration relevé. Contrôles après adoption relancés.
- 18.10.2026 UTC · DigiFab retrouvé dans le portail AIPS (Curatis, autorisation 59301), accès direct HTTP 200, révision 02/2026. Texte anglais à deux colonnes : extraction/audit de doses restant ; preuve audit/DIGIFAB-RECHERCHE-20261018.json. Aucune nouvelle dose publiée.

- 18.10.2026 01:16 UTC · #32 fusionnée (617878e), contrôles requis verts après adoption de la référence CI. Patch fond pâle, procédé runner et référence intégrés ; #37 reste en audit.

- 18.10.2026 UTC · #49/#59/#61/#65 fusionnées. #65 intègre 414 entrées, référence 3730 et correctifs de sélection/disposition : suite 278/278, référence visuelle conservée. #68 (543 entrées, référence 3567) corrige des cibles trop petites dans Notions ; captures et référence en cours de vérification.
- 18.10.2026 UTC · Nouvelle revue en contexte : cardioverter était défini comme un appareil ; correction terminologique avec CHUV § Traitements effectivement relu, journal des fautes mis à jour. La conduite périopératoire présente une ambiguïté potentiellement critique : proposition #88 attente-vial, sources ESC 2022 §6.4 et HUG 2024 §2, aucune dose nouvelle et aucune fusion sans accord.
- 18.10.2026 UTC · Inventaire par SHA et pointeur : 577 champs, 605 occurrences sur main 33bb1d0 ; recensement des marques explicites, pas un audit ni une validation des branches non fusionnées. Scripts et procédure ajoutés au catalogue et au skill vérité.

## Notes modèle (écrites par la veille si GPT 6 Luna est refusé)

18.10.2026 : Luna indisponible par la CLI (401). Modèle de secours : modèle courant de cette session, seul modèle callable sans lancer un autre agent ; utilisé pour les rédactions/relectures, les inventaires étant exécutés par scripts. Le 401 bloque la relance CLI autonome, pas le travail interactif. Les contenus encore à rédiger et à auditer restent dus ; aucune indisponibilité médicale générale n’est déduite de cette erreur.

---

# Historique : phases du plan initial (avant Codex)


Athéna tient ce fichier à jour à chaque porte d’étape. Chaque tâche a un responsable et une échéance (Europe/Zurich).
Légende : [x] fait · [ ] à faire · [~] en cours.

## Phase 0 · Socle (19–25.10.2026) · porte : la CI réussit sur app_v2.html tel quel, et l’empreinte de app.html est contrôlée

| État | Tâche | Responsable | Échéance |
|---|---|---|---|
| [x] | Créer le dépôt public, protéger main (demande de fusion et CI verte exigées) | Héphaïstos | 25.10.2026 |
| [x] | Écrire la CI : garde (empreinte, budget), html (Nu), liens (lychee), tests (Playwright) | Héphaïstos | 25.10.2026 |
| [x] | Activer Pages, les modèles de tickets, les étiquettes et Dependabot | Héphaïstos | 25.10.2026 |
| [ ] | Créer le tableau Projects à quatre colonnes (droit « project » du jeton gh requis) | Héphaïstos | 25.10.2026 |
| [x] | Brancher les tests existants et enregistrer la référence verte (43/43, gardes 5/5) | Janus | 25.10.2026 |
| [x] | Rédiger les dix skills de la section 10 et en garder la copie versionnée dans skills/ | Athéna | 25.10.2026 |
| [x] | Installer les dix skills dans la bibliothèque partagée de l’assistant | Athéna | 25.10.2026 |
| [x] | Créer ETAT.md, HANDOFF.md et un journal par chantier | Athéna | 25.10.2026 |
| [x] | Ouvrir un ticket « Tâche d’agent » par tâche de la phase 1 (issues #5 à #10) | Athéna | 25.10.2026 |
| [ ] | Publier la version datée de la phase 0 (accord requis, interdit I6) | Athéna | 25.10.2026 |

## Phase 1 · Échéance (26.10–29.11.2026) · porte : Athéna fusionne Atlas puis Thémis avant le 30.11.2026, et la veille officielle produit son premier rapport

| État | Tâche | Responsable | Échéance |
|---|---|---|---|
| [x] | Livrer l’export et l’import de la progression, et les erreurs de stockage visibles | Atlas | 15.11.2026 |
| [x] | Écrire tests/test_export.py | Janus, avec Atlas | 15.11.2026 |
| [x] | Refondre l’onglet « Exigences » pour la session 2027 (data/EXI.json, cases à statut ; PR feat/exigences-2027) | Thémis | 29.11.2026 |
| [x] | Activer les veilles officielles Ve1 et Ve2 à partir de tools/templates/veille-squelette.yml (PR #4 fusionnée) | Argos | 15.11.2026 |
| [ ] | Tester la faisabilité de Ve3 (flux Swissmedic) et de Ve4 (XML Refdata) | Argos | 29.11.2026 |
| [x] | Préparer data/MEM.json sans toucher au code (PR #3 fusionnée) | Mnémosyne | 29.11.2026 |
| [x] | Intégrer les 12 méthodes dans l’onglet « Mémorisation » (m|id, options rétroaction et réapprentissage, patch 0018, tests/test_memo.py 17/17) | Mnémosyne | 29.11.2026 |
| [x] | Calendrier interactif (clic, plage, recherche floue, déplacement, durée, toucher, clavier) et sauvegarde automatique fiable (IndexedDB, versions, persistance, fichier) · patch 0004, PR #15 fusionnée | Hermès | 17.10.2026 |
| [x] | Recherche par diagnostic différentiel et notion · patch 0009, PR #18 fusionnée | Hermès | 17.10.2026 |
| [x] | Bandes de séance sans texte coupé (ordinateur) et contrôle Iris du texte coupé · patch 0010, tests/test_calendrier.py (36) | Hermès | 17.10.2026 |
| [x] | NC-0 interaction : lieur gloLink sur CK_GLO_INDEX, pile de fenêtres (5 niveaux, Retour, fil d’Ariane), types glo, syn, hyp, loc et nc chargés à la demande, vues, couches et états des schémas · patch 0012, patch 0013 (repères réels), tests/test_ck_ui.py (74) | Hermès | 17.10.2026 |
| [ ] | Teintes des 7 jours et bandes de séance pâles à contraste AA (data-wd fourni par Hermès) | Apollon (PR #16) | 29.11.2026 |
| [ ] | Fusionner Atlas, puis Thémis, après CI verte | Athéna | 29.11.2026 |
| [x] | Stations CS, pilote : format officiel sourcé (data/cs/format.json), 5 stations (S2.5, S7.6, S3.1, O7.10, G6), tools/cs_build.py, patch 0019 « Station CS », tests/test_cs_stations.py (15) | Chiron | 17.10.2026 |
| [ ] | Relire les 5 stations pilotes (valide_par_vial) | Vial | 29.11.2026 |

## Phases suivantes

| Phase | Période | Agents | Porte |
|---|---|---|---|
| 2 · Interaction | 30.11.2026–10.01.2027 | Hermès, Mnémosyne | Les tests tactiles et clavier réussissent. |
| 3 · Confort et CS | 11.01–28.02.2027 | Atlas, Asclépios | Le premier affichage est deux fois plus rapide, et chaque image a sa licence vérifiée. |
| Continu | jusqu’au CS 2027 | Argos, Thémis, Janus, Athéna | Chaque ticket de veille est traité ou classé en moins de sept jours. |

## Chantier Nerfs crâniens et CK · NC-0 Socle (17–25.10.2026) · porte : socle, lieur et audit de niveau 1 sur main ; un terme non défini fait échouer la CI

| État | Tâche | Responsable | Échéance |
|---|---|---|---|
| [x] | Schémas JSON data/ck/schema (src, glo, sig, syn, hyp, nc, loc, doses_ch) | Atlas | 25.10.2026 |
| [x] | Compilateur tools/ck_build.py → assets/ck/*.js, contrôle --check en CI (G5) | Atlas | 25.10.2026 |
| [x] | Chargement différé : ckLoad, ckGlo, index du glossaire après load, à l’inactivité (patch 0011) | Atlas | 25.10.2026 |
| [x] | Budgets : assets/ck ≤ 2,5 Mo, SVG ≤ 120 Ko, assets/nc ≤ 3 Mo | Atlas | 25.10.2026 |
| [x] | Lyncée et qa/termes-baseline.json (3 849 termes, ne peut que baisser) | Janus | 25.10.2026 |
| [x] | Audit de niveau 1 G1 à G7, Alétheia, artefact audit-flags, étiquette audit:galien | Janus, avec Galien | 25.10.2026 |
| [x] | tools/audit/rapport_fautes.py et blocage d’une faute critique sans accord de Vial | Janus, avec Galien | 25.10.2026 |
| [x] | tests/test_ck.py (61, données, schémas et contrôles) et tests/test_ck_socle.py (12) | Janus | 25.10.2026 |
| [ ] | Types tipFor (glo, syn, hyp, nc, loc), gloLink(), pile de 5 fenêtres | Hermès | 25.10.2026 |
| [x] | Premier lot de 100 signes et syndromes dans data/ck/glo.json (feat/ck-glossaire-lot01) | Hippocrate | 25.10.2026 |
| [x] | Table suisse des doses data/ck/doses_ch.json (lecture à la main ; 3 lignes, 2 doses « À vérifier ») | Galien | 25.10.2026 |
| [x] | Six automates d’audit régional et premier rapport des fautes corrigées (29) | Galien | 25.10.2026 |
| [ ] | Contre-lecture des doses | Asclépios | 25.10.2026 |
| [ ] | Validation des signes et syndromes du lot 01 et des doses « À vérifier » | Vial | à fixer |
| [ ] | Régénérer la liste G6 depuis Lexique 3.83 ; filtre MeSH pour le tri | Janus | 25.10.2026 |

## Chantier Nerfs crâniens · Dédale (plan du 17.10.2026)

| État | Tâche | Responsable | Échéance |
|---|---|---|---|
| [x] | Installer Blender 3.6.19 (sans écran), potrace 1.16 et svgo 4.0.0 sur le box ; Z-Anatomy hors dépôt (/workspace/ssp/nc_src/) | Dédale | 25.10.2026 |
| [x] | Écrire les automates tools/dedale/freestyle.py, trace.py, annoter.py, verifier.py avec leurs instructions | Dédale | 25.10.2026 |
| [x] | Produire le pilote VII : vues face, profil, trois quarts, plan (Gray788) et tour de 8 vues (feat/nc-schemas) | Dédale | 08.11.2026 |
| [x] | Remplacer les annotations provisoires de nc/annot/nc07.yml par celles d’Ariane (foramens, sites lésionnels, branches) | Ariane, puis Dédale | 08.11.2026 |
| [x] | Une image = une idée : préréglages trajet, branches, fonctions, lésions, plan (8 étiquettes au plus, contrôlés par verifier.py) | Dédale | 08.11.2026 |
| [x] | Trois vues seulement (face, profil, 34) : crâne au crayon, nerf jaune, états trajet/branches/fonctions/lésions dans chaque SVG ; tour et plan retirés | Dédale | 08.11.2026 |
| [x] | Repères numérotés fléchés et cliquables (g.nc-num, data-num, data-nom, data-glo), aucun texte sur le dessin, légende en 2 colonnes (feat/nc-numeros) | Dédale | 08.11.2026 |
| [ ] | Valider le pilote VII (valide_par_vial) | Vial | 08.11.2026 |
| [ ] | Produire les onze autres paires (3 vues chacune, sans tour) ; porter freestyle.py en mode ajout seul d’abord | Dédale | NC-2 |

## Chantier Nerfs crâniens · Podalire (chaîne clinique, plan du 17.10.2026)

| État | Tâche | Responsable | Échéance |
|---|---|---|---|
| [x] | Chaîne clinique des 5 sites du VII dans data/ck (syn, hyp, nc, src) : 5 syndromes, 12 hypothèses, nc07 (feat/nc07-chaine) | Podalire | 08.11.2026 |
| [ ] | Revue clinique de niveau 2 de la chaîne du VII (audit:galien) | Galien | 08.11.2026 |
| [ ] | Définir les termes de la liste « Termes pour Galien » (journal/nerfs-ck.md) | Galien | 08.11.2026 |
| [ ] | Lire à la main dans l’AIPS les posologies marquées « À vérifier » (corticothérapie, thrombolyse, antibiotiques de la neuroborréliose) | Galien | 08.11.2026 |
| [ ] | Sourcer les points « À vérifier » (fracture du rocher, otite compliquée, cholestéatome, plaie des rameaux, produits de contraste) | Podalire | NC-1b |
| [x] | Mettre à jour nc07.vues quand Dédale livre les 3 vues « crâne, nerf jaune » | Podalire, avec Dédale | NC-1b |
| [x] | Justifier chaque examen et chaque moyen du VII (mécanisme, principe, pourquoi ce choix, limites) et ajouter le contrôle G8 (feat/nc07-justification) | Podalire | 17.10.2026 |
| [x] | Urgences CK, lot 1 : 10 hypothèses bloquantes, 7 syndromes avec gestes GES reliés, 44 entrées de glossaire, 9 sources ; patch 0017 (feat/ck-urgences-lot1) | Podalire | 17.10.2026 |
| [ ] | Contre-lire le lot 1 des urgences (audit:galien) et lire dans l’AIPS les posologies « À vérifier » | Galien | NC-1b |
| [x] | Urgences CK, lot 2 : 10 hypothèses bloquantes (hémorragie digestive haute, asthme aigu grave, exacerbation de BPCO, insuffisance cardiaque aiguë, choc cardiogénique, hypoglycémie sévère, hyponatrémie, insuffisance rénale aiguë, corps étranger inhalé, polytraumatisme), 8 syndromes, 55 entrées de glossaire, 11 sources (feat/ck-urgences-lot2) | Podalire | 17.10.2026 |
| [ ] | Contre-lire le lot 2 des urgences (audit:galien) et lire dans l’AIPS les posologies « À vérifier » | Galien | NC-1b |
| [ ] | Livrer la vue nc07 « voie_motrice » (cortex, faisceau, noyau double, nerf) citée par les 5 syndromes du VII | Dédale | NC-1b |


### Actualisation après les fusions #68 et #85 · 18.10.2026 UTC

Étape 7 : critère vérifié, #65 puis #68 fusionnées, 543 entrées et référence 3567. #85 fusionnée, fréquences inconnues préservées ; couverture toujours 1 %/9 %. Inventaire de main 27c9658 : 751 champs explicitement À vérifier, 779 occurrences. Contrôle de publication 02:23 UTC : application et quatre JS identiques à cet instantané. ETAT.json conserve la reprise à 8 et refuse la clôture.

Actualisation 2026-10-18T02:30:26.096088+00:00 : #41 fusionnée (5de965f) après #83, contrôles requis verts et 278 tests. #81 reste en audit. Les corrections cliniques R13 #64/#67/#70/#88 restent en attente de Vial. La clôture reste refusée ; reprise à l’étape 8, lot 3.

### Lot 3 des prévalences · 18.10.2026
#90 : une fréquence retenue (SCA, Zurich, 1/53), dix-neuf inconnues conservées. CI 7abe19c : 278/278 ; passage local 276/278, puis calendrier 36/36 après deux échecs tactiles intermittents. Aucune assertion changée. #91 réservé derrière #64 dans la chaîne Hygie. Projet non clos.

### Reprise après le lot 3 · 18.10.2026 UTC

#90 est fusionnée (6bbbde7). Main : 39/2587 fréquences, jauge arrondie 2 % ; 207/2287 monographies, 9 %. Une seule fréquence a été retenue après relecture (SCA, Zurich, 1/53) ; les dix-neuf autres du lot restent inconnues. Source de Berne non retenue sous la règle d’éditeur, miroir suisse inaccessible ; incohérences de l’autre tableau européen consignées. Aucun pays, chiffre ou critère inventé.

#91 contient six propositions G9 (xérose, prurits rénal, ferriprive, médicamenteux, neuropathiques, psychogène), EDF 2025 et HUG relus. Elles ne comptent pas dans main. Le verrou #64→#91 est dans main ; predecesseurs_fusion.py 91 constate #64 OPEN et ready=false. Ne pas activer directement l’auto-merge de #91.

Pages vérifié à 02:54:35 UTC : accueil, app et quatre JS HTTP 200, identiques à main 6bbbde7. Inventaire actualisé : 788 champs, 817 marques, 24 fichiers. La clôture reste refusée ; reprise étape 8 lot 4, G1–G4, S8 après #37. Les instantanés antérieurs restent historiques.

Complément 02:58 UTC : #91 passe la suite locale 278/278 sur 7af1a77, après les contrôles G1/G2/G3/G6 et Lyncée sans terme nouveau. PR prête et audit-ok ; aucun auto-merge directement activé. La preuve de chaîne constate #64 OPEN et ready=false. Les CI exactes restent requises ; six monographies hors main, pas de gain de couverture publié annoncé.

### Reprise cloud · 18.10.2026, Europe/Zurich

Accords Vial lus sur #88/#64/#67/#70. Corrections poussées sur les cinq PR ; G1–G8 locaux verts. Fusion #88 observée dans main aacfff7 (tête d4fa7f7). #64/#91/#67/#70 restent ouvertes à la dernière observation publique ; relecture primaire et CI exactes requises. API GitHub, HUG, DOI et Refdata sont refusés par la politique réseau active ; domaines ajoutés au brouillon, non appliqués au runtime observé. Aucun nouveau lot 8/9, gain de couverture ou fin de boucle revendiqué.

### Notes modèle · reprise du 18.10.2026
Lot G1–G4 : traitement mécanique par script déterministe ; jugement et audit séquentiel par le modèle courant de secours, Luna CLI indisponible dans la relève. Aucun nouveau service de rédaction autonome déclaré.

### Reprise du 18.10.2026 Europe/Zurich
Chaîne #64→#91→#67→#70 fusionnée ; audits et contrôles requis verts. #97 G1–G4 : 60 fréquences explicitement inconnues, aucun chiffre nouveau ; #98 deux propositions G9. Sources officielles et limites réseau consignées, médecin non revendiqué. Garde-progres et file-fusion actives, cadence réelle espacée observée. Étape 8 lot 5 en cours, clôture refusée.

- Fin du lot de reprise : #97 fusionnée, lot 5 en cours. #98 ajoute deux propositions G9 avec réserves, pour 240/2287 sur sa branche. Prévalences 39/2587 ; aucune clôture, aucune nouvelle validation Vial ou de médecin inventée. Relève détaillée mise à jour.

### 18.10.2026 Europe/Zurich · lot 5 et gales
#99 fusionnée : six fréquences relues à Brest, cadre et biais explicites, 45/2587 sur main. #100 réunit deux gales, cinq épidémiologies précisées et six définitions ; sept autres G9 restent dus, aucun squelette Vaquez. Action limitée sur les œufs attribuée à l’ivermectine seulement ; posologies suisses À vérifier. Modèle courant de secours pour la rédaction/relecture, CLI Luna en 401 dans la relève ; mécanique par scripts déterministes. Boucle 8 lot 6, G11–G14 ; clôture refusée, veille maintenue.

- 18.10.2026 · Étape 8 lot 6 : G11–G14, 56 DD conservés, inconnues explicites ; 45/2587 inchangé. Audit et G1–G8 réussis. Pages toujours refusé dans cette session ; GitHub, EDF et HUG accessibles. CI exacte requise avant fusion.

- 18.10.2026 Europe/Zurich · Étape 9, complément G9 : psoriasis et urticaire chronique rédigés et audités, six définitions ; branche 244/2287 et 569 termes, référence 3563. #101 fusionnée, 45/2587 fréquences inchangé, lot 7 G15, G16, S1.1 et S1.2. CI et fusion du complément requises.

## Étape 8 lot 7 · G15–S1.2 · 18.10.2026 Europe/Zurich
54 DD conservés exactement, inconnues explicites, zéro chiffre ajouté ; prévalences 45/2587, monographies 244/2287 inchangées. Contre-lecture séquentielle, G1–G8, builders, Lyncée et gardes réussis. Suite navigateur locale arrêtée avant tout test : exécutable Chromium Playwright absent ; CI complète requise avant fusion. Pages HTTP 200, app identique à main bfa43f2 avant le lot. Prochaine : cinq G9, puis G10 ; prévalences S1.3–S1.6. Boucles ouvertes.
Modèle : mécanique par script déterministe ; jugement et contre-lecture par le modèle courant de secours, Luna CLI signalée indisponible en 401 dans la relève, aucun sous-agent lancé.

## 18.10.2026 Europe/Zurich · dispositif de recherche catégorielle demandé par Vial
STOP temporaire des lots8/9 : automates G/S/F/O, requêtes CH puis Europe, consultation/population, Europe PMC/Crossref/HUG, calculateur et page publique par4 catégories et19 secteurs. État sur branche séparée automates/prevalences ; candidats jamais comptés comme données cliniques. Agent auditeur statistique distinct demandé et lancé : revue indépendante, corrections de conservation des preuves/sigles courts/diversité des résultats et de bruit lexical. Contrôle mécanique continu + file de relance Codex, sans prétendre que commenter prouve l’exécution. Premiers lancements locaux4/4 :20 extraits HUG à vérifier, aucun nouveau chiffre publié. APIs EBI/Crossref refusées dans le runtime ; état partiel explicite, test Actions requis. Suite de tests ciblés et G1–G8 verts, CI entière requise. Reprise après activation : cinq G9, puis G10 ; prévalences S1.3–S1.6. Les boucles restent ouvertes.
