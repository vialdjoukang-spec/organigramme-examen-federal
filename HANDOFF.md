# HANDOFF · passation entre sessions

Chaque agent ajoute sa section en tête, selon le modèle de l’annexe E2 du plan. Aucune donnée personnelle n’entre dans ce fichier public.

## Codex · relève du 18.10.2026 UTC
État       : porte 0 validée ; passages 0–17 consignés, projet NON clos. ETAT.json revient à 8, lot 2 ; en_attente conserve les étapes inachevées.
Prochaine  : lire docs/releves/RELEVE_CODEX_20261018.md ; reprendre G5 après #85, laisser la file poursuivre les chaînes et vérifier les prédécesseurs avant les labels.
Sources    : rapports AIPS sur #59/#61/#67/#70, audits et preuves ciblées sur les branches, sources brutes hors git.
Pièges     : CLI Luna en 401, veille mode B sans rédaction autonome ; incident #62 avant #60 consigné, verrou #82 ; ne pas transformer des brouillons en couverture achevée.
À vérifier : #64/#67/#70 attente-vial, croquis #80 et cinq stations non validés, audits et couverture restants. Ne pas arrêter la veille ni annoncer 100 %.

## Codex · Panacée Étape 5 · 18.10.2026 Europe/Zurich
État       : #60/#62 fusion de main, shards sans conflit réel signalé, toutes sections du rapport conservées, assets reconstruits ; suites 1.63 et pushes locaux sous flock, CI/fusions en attente.
Prochaine  : Étape 6, relire AIPS des quatre lots avant tout audit-ok ; ne pas se fier aux labels anciens de #59/#61.
Sources    : main et audits Érasistrate existants ; aucune nouvelle donnée clinique.
Pièges     : conserver les deux côtés des rapports ; appliquer 0026 aux versions anciennes avant génération des assets.
À vérifier : fin des suites locales/CI et fusion #60 puis #62 ; #64 reste attente-vial.

## Codex · reprise Étapes 3–4 · 18.10.2026 Europe/Zurich
État       : #43 et #71 fusionnées ; Pages #71 prouvé. #44/#45 reprises et testées, pushes en cours ; #58 audit final écrit et suite 1.63 ; #47 rapport réuni/poussé. #50/#53/#54/#49 reconstruites, suites/pushes locaux en file. #64 poussée avec attente-vial et audit partiel.
Prochaine  : Étape 5 (#60 → #62) ; maintenir les reprises des Étapes 3/4 dans ETAT.json.en_attente. Après fusion de #50, poser audit-ok sur #53 ; après #53 sur #54, conformément à l'audit Hérophile existant.
Sources    : Limper/BASEL IX/ESGE/HAS/ESC pour #58 ; Europe PMC XML publics PMC8744717, PMC10448201, PMC9518193 pour hypothermie #64, lus le 17.10 UTC / 18.10 Zurich.
Pièges     : patch 0026 encore non intégré au départ, nouvelle construction dans assets/mono ; modèles cliniques AIPS lue ne prouvent pas une ligne de doses validée ; dates ISO UTC pour les gardes.
À vérifier : signalement potentiellement critique HOPE/décès de #64 (R13), audit primaire endocrinien restant, doses AIPS Étape 6, CI et publications. Aucun succès ou accord médical inventé.

## Codex · reprise technique #62 · 2026-10-17T23:49:59+00:00
État       : fusion de main et reconstruction des assets ; suite locale 1.63 code 1, aucune assertion abaissée.
Prochaine  : vérifier CI et fusion par la file dans l'ordre ; label d'audit selon la relève clinique et la PR précédente.
Sources    : origin/main, patch 0026 et audit Hérophile existant ; aucun nouveau texte clinique rédigé.
Pièges     : les monographies quittent assets/ck pour assets/mono ; ne pas résoudre leurs assets à la main.
À vérifier : CI et publication ; un échec local ne constitue pas une validation.
## Codex · fusion-publication Étape 2 · 18.10.2026 01:08 CEST
État       : correctifs file_fusion (repli 403 et réessai Pages sans nouvelle fusion), suspension attente-vial dans auto-fusion et 5 tests d'intégration, tous verts ; deux sondes #71/#73 avec auto-merge MERGE actif, contrôles en cours. PR Étape 1 : #72.
Prochaine  : Étape 3, chaîne prévalences #43 → #44 → #45 → #58 puis #47 ; ne pas confondre CI en cours et succès de publication. Intégrer les PR Codex dans l'ordre après #71.
Sources    : sorties gh locales et GitHub Actions, tests/test_file_fusion.py ; aucune source clinique ni app_v2 modifiée.
Pièges     : erreur HTTP 403 de protection renvoyée sur stdout par gh ; ne jamais la traiter comme des noms de contrôles. Une publication échouée doit être réessayée sans exiger une nouvelle fusion.
À vérifier : fin des deux sondes, visuel et suite complète en cours ; secret non lisible (403), protection inchangée.

## Codex · état réel Étape 1 · 18.10.2026 01:05 CEST
État       : branche codex/etape-1, PR Étape 0 #71 en CI ; état complet des PR et checks enregistré dans CONTINUATION C1 ; Pages = origin/main, empreinte vérifiée.
Prochaine  : Étape 2, corriger le parseur de protection 403 dans file_fusion et prouver fusion/Pages sur une sonde.
Sources    : gh pr list et statusCheckRollup, origin/main 2228be7, Pages HTTP 200 lus maintenant ; bundle absent des chemins documentés.
Pièges     : UNKNOWN n'est pas CLEAN ; gh pr edit échoue sur projectCards déprécié, utiliser l'API labels. Le CLI Codex ne se connecte pas, veille mode B.
À vérifier : audits finaux #58/#64/#68 et relecture intégrale AIPS #59/#61/#67/#70 ; aucune validation clinique ajoutée par l'installation.

## Codex · installation Étape 0 · 18.10.2026, Europe/Zurich
État       : branche codex/etape-0, worktree /workspace/oef-codex depuis 2228be7 ; neuf actions de porte exécutées ; catalogue complété et présenté, skill ssp-construction-ck, veille B testée puis lancée ; validation porte et PR en cours.
Prochaine  : verifier0, terminer, commiter/pousser la PR Étape 0, puis étape 1 dans l'ordre. La fusion reste soumise à la CI verte.
Sources    : AGENTS.md, CONTINUATION.md entier, PROCHAINE_ACTION, ETAT et journaux lus ; six skills de porte et ssp-tests lus ; sorties CLI/gh du 18.10.2026.
Pièges     : CLI installé sans authentification utilisable ; mode B ne lance pas de session distante. HTTP 403 pour lire la protection malgré droits admin du dépôt. Le serveur codex exec-server ne doit pas être pris pour codex exec.
À vérifier : CI distante et publication ; Chromium installé après échec initial des tests, suite relancée ; sauvegardes Grok hors de cet environnement à inspecter à l'étape 1.

## Asclépios · fréquence (prévalence) des diagnostics différentiels · 17.10.2026, Europe/Zurich
État       : feat/ddx-prevalence : data/ck/prev.json (source unique) ; tools/audit/prevalence.py (règles P1 à P7 : chaque DD une fois avec son nom exact, chiffre dans ]0 ; 100], chiffre ⇒ src de src.json + loc + date_lu, sans chiffre ⇒ « À vérifier », ordre décroissant calculé puis rang clinique, somme ≤ 100 %) ; tools/prev_build.py (--check en CI) écrit PRV dans app_v2.html ([index, %, op, population] dans l'ordre d'affichage) et assets/ck/prev.js (cadre, source, emplacement, date) ; ck_build inclut prev.js. Patch 0020 : % rouge (.pv) à côté de chaque DD, fenêtre pv|SSP|i (cadre, source, date), ligne « Fréquence » en tête de la fenêtre du DD, légende du chiffre, tri par PRV ; la clé de progression reste 'd'+index d'origine. tests/test_prevalence.py 35/35 ; prev.js et src.js se chargent à l’ouverture d’une fiche Notions (rien de plus au démarrage). Le % de la liste est un texte (aucune cible tactile de plus) ; le % de la fenêtre du diagnostic ouvre la source (pv|SSP|i).
Décision   : le chiffre est la fréquence du diagnostic parmi les patients consultant pour la plainte du SSP, dans un cadre nommé (médecine de famille ou urgences, CH ou UE) ; une prévalence de population ne sert qu'à défaut (type « population », affichée). Le texte des 226 SSP rédigés ne change pas : seuls les champs de prev.json et l'ordre s'ajoutent.
Prochaine  : groupes de contenu, un commit poussé par groupe (Galien audite derrière) : 1 douleur thoracique (S2.5), 2 dyspnée, 3 douleur abdominale, 4 céphalée, 5 fièvre, 6 syncope ; puis les 12 SSP S8 (PR #37) quand elle est fusionnée.
Pièges     : ne jamais éditer PRV à la main (prev_build --check échoue) ; aucun « window.CK_ » littéral dans app_v2.html (ckW('PREV')) ; un chiffre exige l'emplacement exact (tableau, page).
Groupes poussés : G1 thorax (S2.5, S2.4 ; Verdon 2008, Swiss Med Wkly, tableau 1 ; 11 chiffres, 9 « à vérifier » : dissection, pneumothorax, tamponnade, péricardite, Boerhaave, aucun cas parmi 672) · branche feat/ddx-prev-g1-thorax (PR #43). G2 dyspnée (S2.7 ; EURODEM, Eur J Emerg Med 2019, tableau 1, 2525 patients de 66 urgences européennes ; 4 chiffres, 6 « à vérifier ») · branche feat/ddx-prev-g2-dyspnee. S2.12 (douleur pariétale) attend une source propre à la douleur pariétale. Prochain : G3 douleur abdominale (S3.1), puis S7.6, G6, F1.19.

Groupes poussés : G1 thorax (S2.5, S2.4 ; Verdon 2008, Swiss Med Wkly, tableau 1 ; 11 chiffres, 9 « à vérifier » : dissection, pneumothorax, tamponnade, péricardite, Boerhaave, aucun cas parmi 672) · branche feat/ddx-prev-g1-thorax. S2.12 (douleur pariétale) attend une source propre à la douleur pariétale. Prochain : G2 dyspnée (S2.7), puis S3.1, S7.6, G6, F1.19.
Groupes poussés : (aucun pour l'instant)
## Flux de fusion · auto-fusion après audit · 17.10.2026, Europe/Zurich

Les rédacteurs ouvrent leur demande de fusion **sans** la fusionner. L'auditeur (médical et linguistique) audite, pousse ses corrections sur la branche de la PR, puis ajoute le label `audit-ok`. Le reste est automatique :

1. Le workflow `.github/workflows/auto-fusion.yml` se déclenche sur `labeled` (et sur `synchronize` / `reopened` si le label est déjà présent).
2. Il met la branche à jour avec `main` via l'API `update-branch` (jamais de force-push).
3. Il active l'auto-merge en **commit de fusion** (`gh pr merge --auto --merge`).
4. GitHub fusionne dès que les contrôles requis (`garde`, `html`, `tests`, `visuel`) sont verts et que la branche est à jour (`strict`). Aucune protection de branche n'est affaiblie.
5. La publication Pages : `.github/workflows/pages-apres-fusion.yml` écoute `pull_request` fermée et fusionnée, puis relance `pages.yml` via `workflow_dispatch` sur `main` (exception documentée pour `GITHUB_TOKEN` ; l'environnement `github-pages` refuse un déploiement lancé depuis un événement `pull_request`).

Réglages dépôt : `allow_auto_merge=true`, `allow_merge_commit=true`, label `audit-ok`.

## Auto-fusion · mise en place · 17.10.2026, Europe/Zurich
État       : Workflow `auto-fusion.yml`, Pages déclenché aussi sur PR fusionnée, label `audit-ok`, auto-merge du dépôt activé. Test de bout en bout prévu juste après la fusion de cette PR (commentaire dans HANDOFF, label `audit-ok`).
Partage    : Les rédacteurs n'appellent plus `gh pr merge`. Seul l'auditeur pose `audit-ok` après audit.
Prochaine  : Vérifier sur une PR triviale que la fusion et Pages suivent le label.
Pièges     : Ne pas retirer un contrôle requis ni baisser `required_approving_review_count`. Ne jamais force-push la branche d'une PR labellisée.

## Chiron · stations CS, pilote · 17.10.2026, Europe/Zurich
État       : feat/cs-stations : format data/cs/format.json (10 règles officielles, 6 formats, ASM 75 % et KK 25 %, chacun sourcé) et data/cs/stations.json (5 stations), schémas data/cs/schema/, compilateur tools/cs_build.py (--check en CI) → assets/st/index.js (window.CS_ST_INDEX) et assets/st/<id>.js, chargés à la demande par stLoad. Patch 0019 : bouton « Station CS » sur la fiche SSP (Notions CK), panneau à sections (consigne, rôle du PS avec « seulement si demandé », résultats, grille ASM avec gestes g|… et chaînes hyp|…, KK, pièges, À vérifier, sources). Lyncée lit data/cs. tests/test_cs_stations.py 15/15 ; suite 241/241 ; G1 à G8 réussis.
Prochaine  : Vial relit les 5 stations (valide_par_vial reste false) ; Galien audite data/cs (étiquette audit:galien) ; stations suivantes par SSP à haut rendement, une par compétence manquante (dossier, modèle).
Sources    : Exigences MED 2026 et Infotext MED 2026 (OFSP/MEBEKO), ASSM/FMH 3.2 et 3.3, DGN 030-141 (2026), EAES 2015, EHF/ESC 2017, pädiatrie schweiz 2019, Kinderspital Zürich (fièvre sans foyer), Rev Med Suisse 2016 (examen de l’abdomen) ; toutes lues le 17.10.2026.
Pièges     : Après toute retouche de data/cs, relancez python3 tools/cs_build.py ; une source citée doit exister dans data/ck/src.json (puis ck_build). cs_build refuse toute dose chiffrée (mg, µg, UI) : écrire « À vérifier ». Les clés GES sont les clés k (comme ckGes), pas des index. Le panneau se place après le premier p.st de nBlock : renderNotSoft lit ce p.st.
À vérifier : voir le champ a_verifier de chaque station et la note de session 2027 de format.json.
## Podalire · urgences CK, lot 2 · 17.10.2026, Europe/Zurich
État       : feat/ck-urgences-lot2 (sur main 49aef17) : 10 hypothèses bloquantes (hemorragie-digestive-haute, asthme-aigu-grave, exacerbation-bpco, insuffisance-cardiaque-aigue, choc-cardiogenique, hypoglycemie-severe, hyponatremie, insuffisance-renale-aigue, corps-etranger-inhale, polytraumatisme), 8 syndromes urg-* avec gestes GES (dont urg-deficit-neuro-brutal, qui renvoie aux hypothèses AVC du VII sans les dupliquer), 55 entrées de glossaire, 11 sources, loc.json étendu à abdomen, thorax, neuro-nc, tete-cou et neuro-moteur. G1 à G8 réussis ; suite 209/209 ; test_ck 75/75.
Prochaine  : Galien contre-lit le lot 2 après la fusion (audit:galien) et lit dans l’AIPS les posologies « À vérifier » ; Vial et Argos confirment les domaines liguepulmonaire.ch et abcd.care ; lot 3 possible : hémorragie variqueuse (Baveno VII, non lu), épiglottite, sources suisses de l’asthme (SGP-SSP).
Sources    : ESGE 2021 hémorragie non variqueuse ; NVL Asthma 5.0 (2024) ; ERS/ATS 2017 exacerbations de BPCO ; Ligue pulmonaire suisse, Guide de poche BPCO (2023) ; ESC 2021 insuffisance cardiaque ; JBDS 01 hypoglycémie (2023) ; guideline européenne hyponatrémie 2014 (version abrégée BANTAO) ; ERBP 2012 sur KDIGO ; ERC 2021 BLS ; S3 AWMF 187-023 polytraumatisme (2022) ; guideline européenne du saignement traumatique (2023) ; lus le 17.10.2026 (PDF gardés hors dépôt). GINA et GOLD ne servent pas de source principale.
Pièges     : G6 ne connaît pas « rétrécissent ». Lyncée découpe « Glasgow-Blatchford » au trait d’union : écrire « score de Blatchford ». « IIa » et « IIb » sont lus comme des termes : écrire le niveau de la recommandation en mots. Les titres anglais des sources demandent une exclusion motivée.
À vérifier : toutes les posologies et tous les volumes (inhibiteur de la pompe à protons, bêta-2 mimétiques, ipratropium, corticoïdes de l’asthme et de la BPCO, sulfate de magnésium, diurétiques, vasodilatateurs, inotropes, noradrénaline, glucose et glucagon, soluté salé hypertonique, urée, cristalloïdes, acide tranexamique) ; hémorragie variqueuse (Baveno VII non lu) ; chapitre BPCO de la NVL non obtenu ; mise à jour ciblée ESC 2023 non lue ; partie 2 de l’ERBP (épuration extrarénale) non lue ; endoscopie après un corps étranger ; choix de l’antibiotique de la BPCO selon les résistances suisses ; signes cliniques de l’insuffisance cardiaque (Table 6 de l’ESC non relue).

## Mnémosyne · onglet « Mémorisation », phase 2 · 17.10.2026, Europe/Zurich
État       : feat/memo-evidence : patch 0018 (carte « Méthodes fondées sur les preuves », 12 méthodes ; type tipFor m|id : survol, clic épinglé, toucher, clavier ; bouton « i » sur chaque stratégie et sur « Méthode d’espacement » ; options « Rétroaction obligatoire » et « Réapprentissage successif », actives par défaut ; consigne de séance #m-cons tirée des options). Données : data/MEM.json → assets/memo/mem.js (window.MEM_DATA, 37 Ko, chargé par memLoad au clic sur l’onglet ou à l’inactivité ; +7 Ko dans app_v2.html). tests/test_memo.py 17/17.
Prochaine  : Janus contrôle les 24 DOI de data/MEM.json (liste « references ») ; Iris adopte la nouvelle référence visuelle de l’onglet memo.
Sources    : research_memorisation.md (17.10.2026), M1 à M24 ; recoupements lus le 17.10.2026 : PubMed 19930508 (Larsen 2009 : 39 % contre 26 %, d = 0,91) et ERIC EJ1310148 (Latimier 2021 : g = 0,74).
Pièges     : Après toute retouche de data/MEM.json ou data/MEM_app.json, relancez python3 tools/build_mem.py <note> (ou --js sans la note) ; test_memo échoue si assets/memo/mem.js n’est pas à jour. « principe » = « Texte à coller » moins les phrases listées dans MEM_app.json « retire », qui décrivaient des fonctions absentes ; la ligne « examen » les remplace et ne cite que des fonctions réelles. Le tableau de synthèse était décalé d’une ligne en phase 1 (ligne d’en-tête lue comme méthode 1) : corrigé.
À vérifier : aucune valeur ; la méthode 12 n’a pas de bloc « Preuves en médecine » dans la note (affiché tel quel).
## Podalire · urgences CK, lot 1 · 17.10.2026, Europe/Zurich
État       : feat/ck-urgences-lot1 (construite sur feat/nc07-justification, PR #29) : 10 hypothèses bloquantes (sca, embolie-pulmonaire, dissection-aortique, pneumothorax-sous-tension, sepsis, anaphylaxie, meningite-bacterienne, etat-de-mal-epileptique, acidocetose-diabetique, hyperkaliemie), 7 syndromes urg-*, 25 signes et 19 termes au glossaire, 9 sources, loc.json rempli pour coeur-vaisseaux, constantes, meninge-gcs et peau. Champ nouveau syn.gestes (clés k de GES, contrôlées par ck_build) ; patch 0017 : « Gestes à faire » dans la fenêtre Syndrome et lien « Syndromes d’urgence de la région → » dans l’onglet Gestes. G1 à G8 réussis ; suite 199/199 ; test_ck 75/75.
Prochaine  : Galien contre-lit le lot (audit:galien) ; Galien lit à la main dans l’AIPS chaque posologie « À vérifier » et l’ajoute à doses_ch.json, puis Podalire remplace la phrase par dose_ref ; Iris établit la nouvelle référence visuelle de l’onglet Gestes (lien ajouté sous le titre) ; lot 2 : asthme aigu et BPCO (source européenne à trouver), hémorragie digestive (ESGE), AVC déjà couvert par le VII.
Sources    : ESC 2023 SCA ; ESC 2019 EP ; ESC 2024 artères périphériques et aorte ; SSC 2021 (ESICM) ; EAACI 2021 anaphylaxie ; JBDS 2023 acidocétose ; DGN S2k état de mal (2020) ; ESCMID 2016 méningite ; ERC 2021 circonstances particulières ; lus le 17.10.2026 (PDF gardés hors dépôt).
Pièges     : G1 lit un seuil de laboratoire suivi de « mmol » ou « µg » comme une dose : écrire « millimoles par litre ». G6 ne connaît pas « entre » ni « resserre » : écrire « pénètre », « contracte ». Une définition ne cite ni son alias ni un terme qui la cite en retour (Lyncée, paires circulaires). Une clé de syn.gestes absente de GES fait échouer ck_build.
À vérifier : toutes les posologies et tous les volumes (aucune dose écrite) ; contre-indications de la fibrinolyse et de la thrombolyse ; traitement de la dissection quand les bêtabloquants sont contre-indiqués ; complications du TEVAR ; ligne POCUS du pneumothorax ; délai du contrôle de la source ; résistance du pneumocoque en Suisse ; statut suisse du lévétiracétam et du valproate ; DOI du JBDS (version 2022, texte lu 2023) ; validité AWMF du DGN expirée en 2025.

## Hermès · nerfs crâniens et CK, NC-0 interaction · 17.10.2026, Europe/Zurich
État       : Patch 0012 (feat/ck-interaction, PR #24), rejoué après le 0011 d’Atlas. Il apporte : le lieur gloLink, branché sur CK_GLO_INDEX.e = [id, type, libellé, formes, tranche] (index chargé à l’inactivité) ; la pile de fenêtres imbriquées (5 niveaux, « ← Retour », fil d’Ariane, aucun lien vers un terme déjà ouvert ; survol, clic, clavier, toucher, panneau bas sur mobile) ; les types tipFor glo|id, syn|id, hyp|id[|pec], loc|module|A|B et nc|id|vue. Les données se chargent à la demande par ckLoad/ckGlo : la fenêtre affiche « Chargement… », puis se redessine sur place. Le réglage « Fond doré » a quitté l’en-tête (champ caché conservé). tests/test_ck_ui.py : 74/74 (données d’essai, plus 22 contrôles sur les données réelles de main : 14 à la fusion de #24, et 8 avec le patch 0013 : repères de Dédale et couches à plusieurs groupes) ; suite 207/207 ; test_ck 61/61 ; G1 à G7 réussis.
Partage    : Janus est propriétaire de tests/test_ck.py (données, schémas, gardes). Hermès est propriétaire de tests/test_ck_ui.py (interaction, pile de fenêtres, gloLink, couches SVG, ordinateur et mobile). Personne ne modifie le fichier de l’autre sans le prévenir.
Contrat    : Pour les schémas, l’ordre est CK_NC[id].vues (face, profil, trois_quarts ; la clé « 34 » est acceptée comme alias), puis CK_SVG[chemin], fourni par assets/nc/<id>.js et compilé par tools/nc_svg_js.py (la CI schemas fait --check : après toute retouche d’un SVG, relancer l’outil). Les états viennent de data-etats de Dédale : les boutons Trajet, Branches, Fonctions et Lésions affichent [data-etat=X] par l’attribut display et cochent les couches de data-etats[X] ; l’utilisateur règle ensuite chaque couche. Le crédit est celui que le SVG affiche. Repères numérotés (contrat Dédale, PR #28) : g.nc-num avec data-num, data-nom et data-glo facultatif. Le survol (ordinateur), le focus et le toucher affichent une bulle « n · nom » (avec la définition courte si elle est chargée) ; le clic, le toucher ou Entrée ouvrent glo|<data-glo> au niveau suivant de la pile (pas au niveau 5, ni si la fiche est déjà ouverte). La case « Légende numérotée » règle la couche legende (id ou data-couche) ; une couche absente du SVG n’a pas de case. Vues affichées : Face, Profil, Trois quarts. Sans JS, le schéma retombe sur <img> et les couches sont désactivées. Sous le schéma s’affichent les sites lésionnels (liens vers syn et hyp) et l’anatomie repliée.
Prochaine  : Apollon : dans le patch 0005, renommer « Par défaut (réglage « Fond doré ») », puisque le réglage n’est plus visible ; styliser les .ck-* (variables CSS seulement). Dédale : certaines étiquettes de la vue de face se touchent (captures ordinateur et mobile, n° 34 et 35). Atlas : loc.js est vide, donc la synthèse locale n’est testée que sur les données d’essai.
Pièges     : Patch 0013 : une couche peut compter plusieurs groupes (#c et g.numeros[data-couche=c][data-etat]) ; ckApply les règle tous, et un groupe propre à un état ne s’affiche que dans cet état. Un test doit viser le cercle du repère (circle.cr), car le centre du groupe tombe sur le trait de rappel.
Pièges     : Le lieur ignore titres, boutons, champs, .tw, #grid et .blk, mais il lie le texte des gestes cochables (label[data-t]) : le clic ouvre alors le terme sans cocher la case. Un sigle (2 à 6 majuscules) se compare avec la casse. Aucun « window.CK_ » ni « glo|<id> » littéral dans app_v2.html (test_ck_socle et Lyncée). Le rouge passe seulement par .urg ou [data-bloquant] (G7). Phrase : ckP() n’ajoute un point que s’il manque.
À vérifier : Les mots d’interface « Foramens » et « Sites lésionnels » doivent recevoir une entrée de glossaire (Hippocrate).

## Podalire · chaîne justifiée du VII (G8) · 17.10.2026, Europe/Zurich
État       : feat/nc07-justification : chaque examen et chaque moyen des 12 hypothèses du VII porte mecanisme, principe, pourquoi_ce_choix (et limites pour un moyen) ; G8 dans niveau1.py, étape CI, 12 tests dans test_ck.py ; syn.vues renvoie à nc|nc07|voie_motrice ; patch 0014 affiche ces champs ; skills ssp-chaine-clinique et ssp-audit-medical à jour.
Prochaine  : Dédale livre assets/nc/nc07-voie-motrice.svg et l’ajoute à nc07.vues.voie_motrice (l’avertissement de ck_build disparaît) ; Galien relit la justification (audit:galien).
Pièges     : une justification recopiée d’un autre champ ou de moins de 20 caractères fait échouer G8 ; l’ancien champ pourquoi est refusé. Les verbes « enlever », « convenir » et « coaguler » manquent au lexique de G6 : écrire « retirer », « être contre-indiqué ».

## Podalire · chaîne clinique du VII (NC-1) · 17.10.2026, Europe/Zurich
État       : feat/nc07-chaine : data/ck/syn.json (5 syndromes vii-site1 à vii-site5, module neuro-nc), hyp.json (12 hypothèses : avc-ischemique et avc-hemorragique bloquantes, tumeur-cerebrale, bell, zona-oticus, schwannome-vestibulaire, fracture-rocher, otite-moyenne-compliquee, cholesteatome, neuroborreliose, tumeur-parotide, traumatisme-facial), nc.json (nc07 : noyaux, trajet, foramens, territoires, 5 lésions, vues), 10 sources ajoutées à src.json ; G1 à G7 conformes, Lyncée 0 terme nouveau. La branche contient la PR #22 (glossaire lot 01), dont les identifiants glo sont cités.
Prochaine  : Galien relit le diff (audit:galien), définit les termes listés dans journal/nerfs-ck.md et lit les posologies « À vérifier » ; Podalire source les points « À vérifier » ; Hermès affiche hyp, syn et nc dans tipFor.
Sources    : HUG, Protocole PFP v1.2 du 04.04.2023 ; DGN/SNG S2k 030-013 (2022) ; DGN S3 030-071 Neuroborreliose (2024) ; ESO IVT (2021) ; ESO-ESMINT thrombectomie (2019) ; ESO-EANS hémorragie intracérébrale (2025) ; EANO schwannome vestibulaire (2020) ; EANO gliomes (2021) ; ESMO-EURACAN glandes salivaires (2022) ; lus le 17.10.2026.
Pièges     : G1 lit « 30 mL » comme une dose : un volume d’hématome s’écrit « 30 millilitres ». Podalire n’écrit aucune posologie : une dose passe par dose_ref vers doses_ch.json, sinon la phrase « La posologie … reste À vérifier ». Les identifiants syn et hyp sont cités par nc/annot/nc07.yml : ne pas les renommer. Les sigles d’éditeurs des titres de sources sont exclus de Lyncée avec motif (qa/termes_exclus.txt).
À vérifier : imagerie et chirurgie de la fracture du rocher, de l’otite compliquée, du cholestéatome et des plaies des rameaux ; précautions des produits de contraste ; « atteinte d’un seul rameau évoque une tumeur » (L5) ; posologies de la corticothérapie, de la thrombolyse et des antibiotiques.

## Hippocrate et Galien · NC-0 glossaire CK et audit médical · 17.10.2026, Europe/Zurich
État       : feat/ck-glossaire-lot01 (sur feat/ck-socle) : glo.json 100 entrées (70 signes, 25 syndromes, 3 examens, 2 termes ; 6 « À vérifier »), src.json 19 sources, doses_ch.json 3 lignes AIPS ; 29 fautes corrigées par les automates régionaux (0 critique, 3 majeures, 26 mineures), qa/audit/RAPPORT_FAUTES.md ; G1 à G7 et Lyncée réussissent.
Prochaine  : Asclépios contre-lit doses_ch.json et qa/posologies.md ; Vial coche qa/validation-vial-glo-lot01.md ; Hippocrate écrit le lot 02 (hyposmie, quadranopsie, cécité, hémiparésie, hypotonie, méningite…).
Sources    : CEN (chapitre 9, sémiologie analytique et topographique), HUG protocole PFP v1.2 du 04.04.2023, SFE item 244, HAS PNDS Cushing 2022, AIPS Valtrex® (12.2025) et Prednisone Streuli® (06.2026), lus le 17.10.2026.
Pièges     : Une correction d'audit passe par galien_region.py corriger --plan <fichier.yml> (le texte « avant » figure une seule fois) ; puis galien_region.py registre écrit fautes.jsonl avec le hachage réel et ne réécrit jamais une ligne existante. Une définition du glossaire ne doit contenir ni son libellé ni ses alias (Lyncée).
Pièges     : Les doses ne se lisent qu'à la main, une page AIPS par produit ; aucune extraction du Compendium ni de Swissmedic. Une dose hors AIPS n'entre pas dans doses_ch.json.
À vérifier : Rebaser sur main après la fusion de la PR #20. Les ajouts swissmedicinfo-pro.ch, cen-neurologie.fr et sfendocrino.org attendent l'accord de Vial et d'Argos.

## Atlas et Janus · NC-0 socle CK et audit de niveau 1 · 17.10.2026, Europe/Zurich
État       : feat/ck-socle : schémas data/ck/schema (src, glo, sig, syn, hyp, nc, loc, doses_ch), données vides et conformes, tools/ck_build.py → assets/ck/*.js (742 octets), patch 0011 (ckLoad, ckGlo, index à l’inactivité ; +659 octets dans app_v2.html), budgets étendus, Lyncée et sa référence (3 849 termes), G1 à G7 (tools/audit/niveau1.py, artefact audit-flags), Alétheia, rapport_fautes.py, nc_svg_check.py ; tests : test_ck.py 61/61, test_ck_socle.py 12/12, suite 133/133, gardes 5/5.
Prochaine  : Hermès branche tipFor et gloLink sur ckLoad/ckGlo/CK_GLO_INDEX ; Hippocrate remplit glo.json par lots et resserre la référence (--update) ; Galien remplit doses_ch.json et fautes.jsonl ; Dédale dépose assets/nc/*.svg et credits.json (couches trait, nerf, legendes ; licence_derivee CC BY-SA).
Sources    : Plan Nerfs crâniens et CK, sections 3, 4, 8 et 9 ; propositions/audit-medical.yml et domaines.yml (17.10.2026).
Pièges     : Après toute modification de data/ck, lancez python3 tools/ck_build.py : la CI échoue si assets/ck n’est pas à jour. Le nom de variable suit le fichier : glo-index.js → window.CK_GLO_INDEX, glo-a.js → window.CK_GLO_A.
Pièges     : Toute demande de fusion qui ajoute un terme médical dans TIP, NOT, GES, le HTML statique ou data/ck échoue à G4 tant qu’il n’est pas défini dans glo.json ou exclu avec motif ; une dose ajoutée dans TIP/NOT/GES échoue à G1 sans « À vérifier » dans le même texte.
Pièges     : G6 lit tools/audit/verbes_conjugues.txt.gz ; on le régénère par tools/audit/verbes_gen.py, jamais à la main.
À vérifier : Liste G6 à régénérer depuis Lexique 3.83 (site indisponible le 17.10.2026) ; filtre MeSH pour le tri ; domaines escardio.org, has-sante.fr, escmid.org (Argos).

## Dédale · schémas des nerfs crâniens (NC-0, pilote VII) · 17.10.2026, Europe/Zurich
État       : feat/nc-numeros : retour de l’utilisateur « trop saturé d’annotation ; numéro fléché et cliquable avec le nom de la structure, pour aérer au maximum ». Les 3 vues assets/nc/nc07-{face,profil,34}.svg (crâne au crayon, nerf jaune #FFC400 cerné de #5a4500, 8,5 px hors tout sur 800 px) n’ont plus aucun texte sur le dessin, sauf le titre : chaque structure porte un petit numéro cerclé fléché, aéré, jamais sur le nerf ; les noms sont dans une légende numérotée en 2 colonnes, en petits caractères, sous le dessin (couche « legende »). États trajet (8 repères), branches (6), fonctions (5), lésions (5, site 1 en rouge). verifier.py V9, V11, V13 à V15 ; tests/test_dedale.py 30/30.
Contrat    : chaque repère est <g class="nc-num" data-num="n" data-nom="nom de la structure" data-glo="identifiant glo.json, s’il existe" data-ref="id nc/annot" tabindex="0" role="button" aria-label="n · nom">, avec trait de rappel path.ld, pointe path.ah, cercle circle.cr (r = 14, trait 2,2 px, fond blanc), numéro text.nm (gras, 18 px sur 800 px). Classe « u » en plus (cr, nm, ld, ah) = site d’urgence, rouge. Les repères d’un état sont dans g.numeros[data-etat][data-couche] ; numéro = rang dans nc/presets/<nerf>.yml, identique dans les 3 vues (le même numéro désigne la même structure ; un repère absent d’une vue garde son numéro).
Contrat    : la légende est g#legende[data-couche="legende"], une g.legende[data-etat] par état (text.lg, numéro dans tspan.n) ; la couche « legende » figure dans data-etats de chaque état, l’application peut la masquer et afficher le nom au toucher ou au clic d’un .nc-num (data-nom, infobulle de glossaire si data-glo). Le crédit court (g#credit) reste toujours visible. Le manifeste assets/nc/nc07-presets.json liste par vue et par état : num, ref, nom, glo.
Prochaine  : Athéna transmet le contrat à Hermès (clic ou toucher → nom, infobulle de glossaire) ; Vial valide les 3 vues ; même chaîne pour les autres paires après portage de freestyle.py en mode ajout seul.
Sources    : Z-Anatomy License.txt (CC BY-SA 4.0) ; nc/annot/nc07.yml (Ariane) ; data/ck/glo.json (Hippocrate) ; lus le 17.10.2026.
Pièges     : Ne jamais ouvrir le modèle complet (11 Go) : freestyle.py le fait, il est gelé ; crane.py et masques.py ajoutent seulement les objets utiles. Freestyle n’est pas rejouable à l’octet : la CI rejoue annoter.py depuis nc/trait versionné, pas Blender. svgo applique les transformations aux chemins du nerf et des noyaux : leurs épaisseurs s’écrivent en px de l’image dans la feuille de style (annoter.py échoue sinon). svgo trie les attributs : un test ne cherche jamais un ordre d’attributs.
À vérifier : F2 (fond du méat) et repères a_verifier d’Ariane ; le repère 1 des lésions (cortex moteur) pointe dans la voûte vide (cerveau non dessiné) ; data-glo n’existe que pour les sites lésionnels (paralysie faciale centrale ou périphérique, hyperacousie) : le glossaire n’a pas encore les structures anatomiques ; numéros de 18 px (8,1 px à 360 px) et légende de 22 px (9,9 px à 360 px) sous le minimum de 13 px de l’ancienne règle, par choix (cercle de 13,5 px à 360 px).

## Hermès · calendrier et sauvegarde automatique · 17.10.2026, Europe/Zurich
État       : PR #15 fusionnée dans main le 17.10.2026 à 13:26 (commit de fusion 3c9b878, sans écrasement) ; Pages publie la même empreinte que main ; tests/test_calendrier.py rejoué contre le site public : 32/32, aucune erreur de console. Patch 0009 (PR #18, fusionnée le 17.10.2026 à 13:55) : la recherche trouve aussi un SSP par ses diagnostics différentiels et ses notions (NOT), avec le titre trouvé sous le nom ; suite 119/119, gardes 5/5.
Prochaine  : Apollon (PR #16) pose les teintes de jour et les bandes de séance pâles : data-wd (1 = lundi … 7 = dimanche) existe désormais sur .hd et .col, y compris en vue « Jour » ; il remplace donc nth-child par [data-wd] et peut teinter la colonne du jour. Mnémosyne réutilise showTip/tipToggle inchangés.
Sources    : MDN StorageManager.persist(), IndexedDB, File System Access API ; WebKit « Full Third-Party Cookie Blocking and More » (plafond de 7 jours), lus le 17.10.2026.
Pièges     : Tout appel à lsSet déclenche svTouch ; le miroir ne démarre qu’après le contrôle de démarrage (svReady), pour ne jamais écraser la copie de secours par un état vide. test_export simule l’effacement Safari en supprimant aussi IndexedDB.
Pièges     : Dans les tests mobiles, la barre d’onglets collante (≈ 200 px sur 412 px de large) masque le haut de l’écran ; faites défiler avec behavior:'instant' et un décalage.
Pièges     : Patch 0010 : blkFit() mesure chaque bande après renderGrid (et au redimensionnement, aux polices chargées) ; il pose --cl (lignes qui tiennent), .mini (moins d’une ligne : une seule ligne compacte) ou .nodu (durée masquée si elle cache l’horaire). Une règle CSS nouvelle sur .blk ne doit pas fixer -webkit-line-clamp en dur. Iris échoue sur tout texte coupé sans ellipse ni texte complet (CLIP_JS, état cal-bandes-semaine et cal-bandes-jour).
Pièges     : fz() renvoie un tableau portant R.why (code → titre trouvé dans NOT) ; le second niveau n’est consulté que si le nom et le code ne donnent rien pour ce SSP.
Pièges     : Un conflit dans app_v2.html ne se résout jamais à la main : reprenez la version de main, puis rejouez votre patch (skill ssp-fusion-patch).
À vérifier : Le fichier automatique n’existe que sur Chromium de bureau ; ailleurs le bouton reste caché. Essai réel sur iOS Safari (persistance refusée, versions) par le titulaire.

## Asclépios · examen physique · 17.10.2026, Europe/Zurich
État       : feat/asclepios-examen : GES en 3 axes (13 régions, 6 systèmes, 3 populations ; 22 entrées, 315 gestes), sous-régions, ordre strict, 7 gestes nouveaux sourcés, 12 doublons en renvois bidirectionnels, 19 croquis (assets/cs, credits.json) ; TIP champ 5 structuré pour 198 SSP, 15 marqués « À compléter », 35 laissés tels quels (contenu non clinique d’examen). Patch 0008, tests/test_examen.py (16 contrôles), Pages publie assets/.
Prochaine  : Vial valide les croquis (valide_par_vial) ; Asclépios relit les 113 blocs « Autres éléments ciblés » et rédige les 15 champs vides avec sources.
Sources    : StatPearls/NCBI (NBK271, NBK551612, NBK549844, NBK538499, NBK558918, NBK256, NBK513250, NBK557639, NBK557862, NBK459125, NBK470595, NBK549859, NBK544226), PMC3993046, PMC5890131 ; Füeßl/Middeke (pages à vérifier) ; Wikimedia Commons et Open-i lus le 17.10.2026.
Pièges     : La progression des gestes est indexée par it.k (clé historique « région_index ») : ne jamais renuméroter k. Les scripts tools/asclepios/*.py refusent de tourner deux fois (garde d’idempotence). Le champ 5 est un format compact (§ région, ¶ phase, • élément, @ puces) rendu par exFmt().
À vérifier : Pages Füeßl/Middeke des 7 gestes nouveaux ; classement automatique des éléments du champ 5 (relecture humaine par échantillon).
Classes    : .ex-axe/.ex-axe__h (rail des régions), .ex-region/.ex-region__h, .ex-phase[data-ordre=1…6|M|N], .ex-items, .ex-fig/.ex-fig__cap/.ex-fig__credit, .ex-xref/.ex-chip[data-gx], .ex-av, .ex-flash — conformes à qa/apollon/spec.md § 7 ; data-ordre « M » (Mesures) et « N » (Neurologique) s’ajoutent aux valeurs 1 à 6.
## Thémis · Exigences 2027 · 17.10.2026, Europe/Zurich
État       : L’onglet « Exigences » compte 46 cases stables (data/EXI.json), un bandeau 2027 et des badges « À vérifier auprès de la MEBEKO » ; SESSION centralise les dates ; patch 0004 ; tests/test_exigences.py (13 contrôles) ; suite 69/69, gardes 5/5.
Prochaine  : Thémis met data/SESSION.json à jour (tools/build_exi.py, puis json_inject.py inject SESSION) dès que l’OFSP publie les dates 2027.
Sources    : research_exigences.md (S1 à S12, N1), lues le 17.10.2026.
Pièges     : Les coches vivent sous « x:<id> » dans S.exi, à côté des clés a… (Attendus) et cp… (CS) ; on ne renumérote jamais un identifiant.
À vérifier : A3, A4, C4, C6, C7, C8, C10, D2, D5, E2 et E3 attendent une réponse de la MEBEKO ou une publication de l’OFSP.

## Asclépios · examen physique (TIP champ 5) · 17.10.2026, Europe/Zurich
État       : 15 champs « À compléter » écrits et sourcés (v.c[5] « complété ») ; 113 blocs « Autres éléments ciblés » revus (355 éléments → 290 phrases complètes) ; scripts rejouables dans tools/asclepios/tip_*.py.
Prochaine  : Galien relit le diff de TIP (niveau 2) ; puis diagnostics différentiels du bloc trauma S8.1–S8.12 et sections de cours de moins de 200 caractères.
Sources    : voir journal/asclepios.md, étape 3 (toutes lues le 17.10.2026).
Pièges     : Lyncée regroupe les variantes d’un terme ; retirer une variante peut faire apparaître une autre comme « nouvelle » (extra-digestif) ; les titres anglais et les initiales d’auteurs dans v.S sont scannés.
À vérifier : ESC 2022 (G14), nerf axillaire (S8.4), signes de fracture de la base (S8.7), signes œsophagiens (S8.6), SOSORT, Epworth, ROR, délai des vaccins vivants reconstitués, échelle d’agitation de S9.8.

## Atlas · sauvegarde · 17.10.2026, Europe/Zurich
État       : Le chantier export/import est sur feat/sauvegarde (PR #11) : patch 0003, CSS du bandeau dans le style de head, tests/test_export.py (13 contrôles) ; suite locale 56/56 et gardes 5/5.
Prochaine  : Athéna fusionne PR #11 dès que la CI (garde, html, tests) est verte.
Sources    : Ticket #5 ; plan v2 fiche Atlas ; MDN Storage quotas ; WebKit 7-Day Cap (lus le 17.10.2026).
Pièges     : Toute règle CSS nouvelle dans le style de body crée des erreurs Nu ; le bandeau #bak doit rester dans le style de head.
À vérifier : Le rappel d’export à sept jours et le message de stockage plein sont couverts par tests/test_export.py.

## Argos · veilles · 17.10.2026, Europe/Zurich
État       : Ve1 (OFSP) et Ve2 (healthreg) sont dans main (PR #4 fusionnée) ; workflows veille-ve1.yml et veille-ve2.yml actifs.
Prochaine  : Argos teste la faisabilité de Ve3 (flux Swissmedic) et de Ve4 (XML Refdata) avant le 29.11.2026.
Sources    : robots.txt de bag.admin.ch et de healthreg-online.admin.ch lus le 17.10.2026 ; plan v2, section 11 et annexe D.
Pièges     : main est protégée ; veille/etat.json vit donc sur la branche veille-etat, que personne ne doit fusionner ni supprimer.
À vérifier : Janus contrôle vers le 17.11.2026 que la réactivation mensuelle (PUT …/enable) garde les veilles actives.

## Mnémosyne · mémorisation · 17.10.2026, Europe/Zurich
État       : data/MEM.json contient les douze méthodes et les références M1 à M24, reprises mot pour mot ; les 24 DOI se résolvent (PR #3).
Prochaine  : En phase 2, après la fusion d’Hermès, Mnémosyne ajoute data-t="m|id" et les trois réglages, sur feat/memo-evidence.
Sources    : research_memorisation.md du 17.10.2026 ; doi.org, le 17.10.2026.
Pièges     : tools/build_mem.py régénère MEM.json ; on corrige la note source puis on relance le script, sans retoucher le JSON à la main.
À vérifier : Janus rejoue le contrôle des DOI sur la liste references de MEM.json.

## Athéna · coordination · 17.10.2026, Europe/Zurich
État       : La phase 0 est livrée ; les tickets de phase 1 (#5 à #10) sont ouverts ; MEM.json et les veilles Ve1/Ve2 sont dans main ; les dix skills sont dans la bibliothèque partagée.
Prochaine  : Fusionner PR #11 (Atlas) quand la CI est verte ; la version datée de phase 0 attend encore l’accord du titulaire (I6).
Sources    : J’ai lu le plan v2 (sections 1, 3, 4, 10, 12 et annexe E), le 17.10.2026.
Pièges     : Une ligne d’app_v2.html dépasse 4,8 millions de caractères ; les expressions régulières y expirent, et seul str.find fonctionne (tools/_app.py).
Pièges     : main exige une demande de fusion et les contrôles garde, html et tests, même pour l’administrateur ; aucun push direct n’aboutit.
Pièges     : GES est suivi de « ;const GES_SRC=… » sur la même ligne ; tools/_app.py délimite donc les constantes JSON par json.raw_decode.
À vérifier : Le jeton gh n’a pas le droit « project » ; le tableau Projects attend `gh auth refresh -s project` par le titulaire du compte.

## Prompt de continuité (annexe E3)
Tu es <Agent>, l’agent chargé de <spécialité> dans le projet « Organigramme Examen fédéral ».
Lis d’abord HANDOFF.md, ETAT.md et journal/<chantier>.md, puis ta fiche de mission (plan v2, section 4).
Ne lis jamais app_v2.html en entier : applique ssp-extrait-cible, ssp-patch et ssp-json-data.
Vérifie chaque modification avec ssp-tests, et contrôle chaque texte avec ssp-verite.
Ne modifie jamais app.html. N’utilise que des sources suisses et européennes, et des images réelles.
Respecte la règle universelle : le projet cible doit avoir un résultat de HAUTE QUALITÉ ; l’usage des jetons doit être raisonnable et optimisé, et tout gaspillage est formellement interdit ; l’économie de jetons est autorisée si et seulement si elle ne dégrade pas la qualité du travail.
Avant de t’arrêter, mets à jour HANDOFF.md, ETAT.md et ton journal.

## Hygie · monographies des différentiels · 17.10.2026, Europe/Zurich
État       : Lot 1 poussé (G1, 14 diagnostics) : hyperhidrose-primaire-focale, hyperhidrose-medicamenteuse-et-toxique, thyrotoxicose, pheochromocytome-et-paragangliome, hypoglycemie, lymphome-hodgkinien-ou-non-hodgkinien, tuberculose, endocardite-infectieuse, infection-a-vih, sevrage-alcoolique-complique, syndrome-serotoninergique, menopause-et-syndrome-climaterique, trouble-anxieux-et-attaque-de-panique, syndrome-d-apnees-obstructives-du-sommeil.
Prochaine  : Lot 2 = G2 (`python3 tools/mono_build.py --draft G2` imprime l'existant TIP.d à reprendre ; clés déjà faites marquées « (fait) »).
Méthode    : data/ck/mono/<lettre>.json (clé = libellé normalisé, partagée entre SSP) → `python3 tools/mono_build.py` → assets/ck/mono-<lettre>.js ; patch 0025 (survol/clic du DD, repli sur TIP.d). CI : `mono_build.py --check`.
Pièges     : Doses : jamais de chiffre dans « pha » sans AIPS lue (« dose : à vérifier (AIPS) ») ; gras réservé aux titres (contrôlé) ; rouge = <span class="mono-r">. Budget assets/ck 2,5 Mo : ~2 280 monographies × ~2 Ko le dépasseront, prévoir un budget mono séparé (décision de Vial).
À vérifier : Hérophile : épidémiologie et sex-ratio marqués « à vérifier » à sourcer (CH/UE), toutes les doses (AIPS).

## Panacée · monographies des différentiels, depuis la fin · 17.10.2026, Europe/Zurich
Lot 1 (O7.26, O7.25, O7.24 ; 27 diagnostics) : intoxication-au-paracetamol … paternalisme-excessif. Doses : aucune entrée doses_ch pertinente, toutes « à vérifier (AIPS) » ; épidémiologie chiffrée « à vérifier (source CH/UE) ».
Lot 2 (O7.23, O7.22, O7.21 ; 29 diagnostics, PR feat/mono-panacee-2, en attente d'audit Hérophile) : decompensation-metabolique-aigue … complements-a-haute-dose.
Sources lues le 17.10.2026 : OFSP/Concept national maladies rares (7,2 %, estimation 2012) ; Elder 2013 PMID 23114748 (porphyrie) ; Br J Dermatol 2024 PMID 38848542 (nécrolyse) ; EAS 2015 PMID 25694464 (statines) ; EAACI 2021 PMID 34343358 (anaphylaxie) ; OFS ESS 2022 su-f-14.02-ESS-COMPLEM_CH (médecine complémentaire) ; CC art. 307, 314c, 443 (fedlex, état 01.07.2026).
Doses : doses_ch.json (3 entrées : valaciclovir ×2, prednisone) sans correspondance → toutes « à vérifier (AIPS) ».
Astuce : fedlex se lit par curl sur filestore (…/eli/cc/24/233_245_233/20260701/fr/html/fedlex-data-admin-ch-eli-cc-24-233_245_233-20260701-fr-html.html), puis extraction par id="art_N" ; Orphanet bloque les robots.
Prochain : Lot 3 = O7.20, O7.19, O7.18 et en dessous (Hygie monte depuis G2).
