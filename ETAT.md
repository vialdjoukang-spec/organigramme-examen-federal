# ETAT · Organigramme Examen fédéral

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
| [x] | Calendrier interactif (clic, plage, recherche floue, déplacement, durée, toucher, clavier) et sauvegarde automatique fiable (IndexedDB, versions, persistance, fichier) · patch 0004, PR #15 fusionnée | Hermès | 17.10.2026 |
| [x] | Recherche par diagnostic différentiel et notion · patch 0009, PR #18 fusionnée | Hermès | 17.10.2026 |
| [x] | Bandes de séance sans texte coupé (ordinateur) et contrôle Iris du texte coupé · patch 0010, tests/test_calendrier.py (36) | Hermès | 17.10.2026 |
| [x] | NC-0 interaction : lieur gloLink sur CK_GLO_INDEX, pile de fenêtres (5 niveaux, Retour, fil d’Ariane), types glo, syn, hyp, loc et nc chargés à la demande, vues, couches et états des schémas · patch 0012, tests/test_ck_ui.py (66) | Hermès | 17.10.2026 |
| [ ] | Teintes des 7 jours et bandes de séance pâles à contraste AA (data-wd fourni par Hermès) | Apollon (PR #16) | 29.11.2026 |
| [ ] | Fusionner Atlas, puis Thémis, après CI verte | Athéna | 29.11.2026 |

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
| [ ] | Schéma clé nc07-voie-motrice (1er et 2e motoneurones, innervation bilatérale ou controlatérale, états central et peripherique), en tête de nc07.vues : fait et vérifié sur la branche feat/nc07-voie-motrice, EN PAUSE avant PR et fusion (reprise : HANDOFF.md, section Dédale) | Dédale | après la pause |
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

