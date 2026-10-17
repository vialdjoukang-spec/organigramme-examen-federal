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
| [x] | NC-0 interaction : lieur gloLink, pile de fenêtres (5 niveaux, Retour, fil d’Ariane), couches et vues SVG, tour 8 vues · patch 0011, tests/test_ck_ui.py (47) | Hermès | 17.10.2026 |
| [ ] | Teintes des 7 jours et bandes de séance pâles à contraste AA (data-wd fourni par Hermès) | Apollon (PR #16) | 29.11.2026 |
| [ ] | Fusionner Atlas, puis Thémis, après CI verte | Athéna | 29.11.2026 |

## Phases suivantes

| Phase | Période | Agents | Porte |
|---|---|---|---|
| 2 · Interaction | 30.11.2026–10.01.2027 | Hermès, Mnémosyne | Les tests tactiles et clavier réussissent. |
| 3 · Confort et CS | 11.01–28.02.2027 | Atlas, Asclépios | Le premier affichage est deux fois plus rapide, et chaque image a sa licence vérifiée. |
| Continu | jusqu’au CS 2027 | Argos, Thémis, Janus, Athéna | Chaque ticket de veille est traité ou classé en moins de sept jours. |

## Chantier Nerfs crâniens · Dédale (plan du 17.10.2026)

| État | Tâche | Responsable | Échéance |
|---|---|---|---|
| [x] | Installer Blender 3.6.19 (sans écran), potrace 1.16 et svgo 4.0.0 sur le box ; Z-Anatomy hors dépôt (/workspace/ssp/nc_src/) | Dédale | 25.10.2026 |
| [x] | Écrire les automates tools/dedale/freestyle.py, trace.py, annoter.py, verifier.py avec leurs instructions | Dédale | 25.10.2026 |
| [x] | Produire le pilote VII : vues face, profil, trois quarts, plan (Gray788) et tour de 8 vues (feat/nc-schemas) | Dédale | 08.11.2026 |
| [ ] | Remplacer les annotations provisoires de nc/annot/nc07.yml par celles d’Ariane (foramens, sites lésionnels, branches) | Ariane, puis Dédale | 08.11.2026 |
| [ ] | Valider le pilote VII (valide_par_vial) | Vial | 08.11.2026 |
| [ ] | Produire les onze autres paires ; tours de 8 vues pour V et III-IV-VI seulement | Dédale | NC-2 |
