# Journal · Nerfs crâniens et partie CK (plan du 17.10.2026)

Chaque agent ajoute ses entrées datées (Europe/Zurich) : ce qui est fait, sources lues, « À vérifier », prochaine action.

## Atlas et Janus · NC-0 socle et contrôles · 17.10.2026, Europe/Zurich

### Décisions
- 14:00 · Atlas et Janus livrent ensemble sur une seule branche, feat/ck-socle (au lieu de feat/ck-socle + qa/ck-controles), pour que les contrôles et le socle qu’ils vérifient entrent dans main en même temps.
- 14:05 · Lyncée reste déterministe en CI : aucune liste externe n’est téléchargée. Le MeSH bilingue (CC BY-NC) et Lexique 3.83 (CC BY-SA) deviennent des aides au tri local. Motif : lexique.org a renvoyé HTTP 200 sans corps, puis 503, depuis le box le 17.10.2026 ; un gate dépendant d’un site lent rendrait la CI instable.
- 14:09 · La liste des formes conjuguées de G6 (tools/audit/verbes_conjugues.txt.gz, 83 502 formes) vient d’un conjugueur interne appliqué à 1 681 lemmes VERB/AUX relevés par spaCy fr_core_news_sm dans TIP, NOT et GES, plus une table d’irréguliers. tools/audit/verbes_gen.py bascule sur Lexique 3.83 dès que .cache/lexique/Lexique383.tsv existe.
- 14:10 · Dans syn.json, les hypothèses d’orientation s’appellent `hyp` (identifiants de hyp.json) au lieu de `orientation`, pour ne pas mélanger un champ de texte (glo.orientation) et une liste d’identifiants. Le schéma sig = entrée de glo de type « signe » avec `recherche` obligatoire.
- 14:11 · Les définitions du glossaire se publient par tranches (glo-<première lettre>.js) ; l’index glo-index.js porte [id, type, libellé, formes, tranche] pour le lieur d’Hermès.
- 14:13 · Référence de Lyncée créée : 3 868 candidats, 19 exclusions motivées (mots de la langue générale), 3 849 termes non définis. Elle ne peut que baisser (contrôle --diff contre la branche de base).
- 14:13 · Référence des doses héritées (TIP, NOT, GES) : 297 clés, 473 mentions ; une dose nouvelle dans ce contenu exige une source suisse ou la mention « À vérifier » dans le même texte.
- 14:15 · G7 porte sur les données CK et sur les règles CSS `.ck-…` seulement, pour ne pas bloquer la refonte d’Apollon sur le reste de l’application.
- 14:16 · Décision de Vial du 17.10.2026 appliquée mécaniquement : une faute critique de qa/audit/fautes.jsonl sans `accord_vial` daté fait échouer la CI (rapport_fautes.py --check).
- 14:17 · Décision de Vial du 17.10.2026 appliquée : une vue dérivée de assets/nc exige `licence_derivee` CC BY-SA dans credits.json (nc_svg_check.py).

### Sources lues
- Plan Nerfs crâniens et CK, sections 3, 4, 8 et 9, et propositions/audit-medical.yml, propositions/domaines.yml (local, 17.10.2026).
- MDN, requestIdleCallback et HTMLScriptElement (comportement de <script src> en file://), connus et vérifiés par test Playwright le 17.10.2026.

### À vérifier
- Lexique 3.83 : régénérer la liste G6 à partir de Lexique dès que lexique.org livre le fichier (Janus).
- MeSH bilingue de l’Inserm : brancher le filtre de tri en cache local (Janus, avec Hippocrate).
- Domaines escardio.org, has-sante.fr et escmid.org : confirmation manuelle (Argos).

- 14:45 · Fusion de main (PR #18 et #19) : Hermès a pris le numéro 0010 (bandes du calendrier) ; le patch d’Atlas devient 0011, rejoué sur l’app_v2.html de main (ssp-fusion-patch). tests/test_audit.py devient tests/test_ck.py (Janus : données, schémas, contrôles) ; Hermès garde tests/test_ck_ui.py.
- 14:46 · Les cinq skills du chantier et ssp-images-licence amendé sont copiés dans skills/.

- 15:40 · Iris signalait en CI un CLS de 0,43 sur ordinateur pour les seules branches qui contiennent le socle (local : 0,1832, identique à main). Par prudence, l’index du glossaire se charge désormais après l’événement load, puis à l’inactivité (+41 octets).

### Prochaine action
- Hippocrate : premier lot de 50 entrées dans data/ck/glo.json ; `python3 tools/lyncee.py --json .cache/lyncee.json` donne les candidats par fréquence ; `--update` resserre la référence.
- Hermès : brancher tipFor (glo|id, syn|id, hyp|id, nc|id|vue, loc|module|A ou B) sur ckLoad() et ckGlo(), et gloLink() sur window.CK_GLO_INDEX.
- Galien : remplir data/ck/doses_ch.json et qa/audit/fautes.jsonl ; la revue de niveau 2 part de l’artefact audit-flags et de l’étiquette audit:galien.

## 17.10.2026 — Phase NC-0, glossaire et audit médical (Hippocrate et Galien)
- Branche feat/ck-glossaire-lot01, reconstruite sur feat/ck-socle (PR #20, Atlas) pour en suivre les schémas ; à rebaser sur main après la fusion de #20 (ssp-fusion-patch). app_v2.html, app.html et orig/ ne sont pas touchés.
- Hippocrate : data/ck/glo.json, 100 entrées (70 signes, 25 syndromes, 3 examens, 2 termes ; 94 « sourcé », 6 « À vérifier ») en deux unités de 50 ; data/ck/src.json, 19 sources. Les définitions n’emploient plus leur propre libellé (règle de Lyncée) ; région et motif « À vérifier » vivent dans qa/audit/glo-meta.json, car le schéma glo n’a pas ces champs.
- Galien : tools/audit/galien_region.py (travail, corriger, registre) et regions.yml ; 29 fautes corrigées (0 critique, 3 majeures, 26 mineures), un commit chacune ; qa/audit/RAPPORT_FAUTES.md.
- Galien : data/ck/doses_ch.json, 3 lignes lues à la main dans l’AIPS ; 2 doses hors étiquette « À vérifier » dans qa/posologies.md.
- Écarts au socle, motivés : swissmedicinfo-pro.ch (hôte réel de l’AIPS) admis par le schéma doses_ch et G1 ; cen-neurologie.fr et sfendocrino.org ajoutés à qa/domaines.yml ; sept lemmes ajoutés à la liste G6 ; quatre exclusions Lyncée ; référence Lyncée resserrée de 3 849 à 3 826 termes.
- En attente : la contre-lecture des doses par Asclépios, la validation de Vial (qa/validation-vial-glo-lot01.md, qa/posologies.md) et l’accord de Vial et d’Argos sur les trois domaines.

## Dédale · NC-0 automates et NC-1 pilote VII · 17.10.2026, Europe/Zurich

### Décisions
- 14:00 · Blender 3.6.19 LTS (et non 4.x) : le module « Freestyle SVG Exporter » y est livré, et Startup.blend de Z-Anatomy date de mai 2023.
- 14:03 · Z-Anatomy téléchargé depuis le dépôt GitHub officiel (Z-Anatomy.zip, 86 734 957 octets, sha256 e0296885…) dans /workspace/ssp/nc_src/, hors dépôt. L’archive Zenodo (CC BY 4.0, 2021) n’est pas utilisée : on suit la licence CC BY-SA 4.0 du dépôt actuel.
- 14:10 · La peau est faite des régions de la tête, de la face et du cou fusionnées (sommets confondus à 2 mm, normales recalculées) : à 1 mm, les coutures entre régions réapparaissent comme des traits parasites.
- 14:12 · Chaque groupe (territoires, crâne, tronc, peau) est rendu seul : c’est ce qui donne le crâne « en transparence » sans qu’un groupe en masque un autre. Le nerf est projeté depuis ses courbes de Bézier (un tube de 0,5 mm rendu par Freestyle donnerait un double trait).
- 14:19 · Territoires : un passage par muscle, contour extérieur seul. Les muscles minces (frontal, temporo-pariétal, aponévrose épicrânienne) donnaient des hachures ; l’aponévrose épicrânienne est exclue (ce n’est pas un muscle).
- 14:21 · Le modèle évalué dépasse 11 Go : freestyle.py supprime d’abord les objets inutiles (en conservant leur position dans le monde), ce qui ramène une vue à quelques secondes ; une seule instance de Blender à la fois.
- 14:22 · Rejouabilité vérifiée : deux exécutions de freestyle.py donnent nc/trait/* identiques à l’octet ; trace.py aussi ; annoter.py --verifier recompose les 4 vues à l’octet (svgo 4.0.0 figé).
- 14:30 · Format de assets/nc/credits.json aligné sur tools/nc_svg_check.py de Janus (branche feat/ck-socle) : liste d’entrées, « fichier » = nom simple, champs url, derive, licence_derivee = CC BY-SA 4.0.
- 14:32 · Les données d’Ariane n’existent pas encore : nc/annot/nc07.yml est PROVISOIRE. Seuls des objets nommés du modèle reçoivent une position (noyau moteur du VII, noyau salivaire supérieur, glande parotide) ; foramens, sites lésionnels et noms des branches restent « À vérifier », sans position inventée.
- 14:35 · Gray788 est en noir et blanc : pas de masque de couleur pour le plan du VII ; trace.py retire 801 composantes de texte (légendes anglaises). Une règle plus large effaçait aussi le ganglion otique : refusée. Quelques fragments restent (« Small », « Petro », « heno », « max »).

### Sources lues
- Z-Anatomy, License.txt (CC BY-SA 4.0 ; attributions BodyParts3D CC BY-SA 2.1 JP, Cranial Nerves and Foramina, University of Dundee CAHID, CC BY 4.0), https://raw.githubusercontent.com/Z-Anatomy/Models-of-human-anatomy/master/License.txt, lu le 17.10.2026.
- Wikimedia Commons, API imageinfo de File:Gray788.png (LicenseShortName : Public domain ; H. V. Carter, Gray 1918), lu le 17.10.2026.
- Plan Nerfs crâniens et CK, sections 4, 5, 8 et 13 ; prompts 00 et 03 ; skills ssp-schema-nerf, ssp-images-licence (amendée), ssp-continuite, ssp-patch, ssp-tests (local, 17.10.2026).

### À vérifier
- Toutes les annotations de nc/annot/nc07.yml (Ariane) ; les positions des noyaux viennent du modèle, pas d’un atlas relu.
- Liste des muscles rattachés au VII dans le modèle (collection « Facial nerve (VII) » de Z-Anatomy) : Ariane la confirme.
- Validation visuelle du pilote par Vial (valide_par_vial reste faux).

### Prochaine action
- Ariane livre nc/annot/nc07.yml (foramens, ≥ 3 sites lésionnels sourcés, branches, ancres du plan) ; Dédale relance `python3 tools/dedale/annoter.py nc07`, puis verifier.py.
- Après validation de Vial : onze autres paires (nerfs.json : objets et ancres par nerf), tours pour V et III-IV-VI.

## Ariane · neuro-anatomie du VII (NC-1, pilote) · 17.10.2026, Europe/Zurich
### Fait
- nc/annot/nc07.yml réécrit : trajet en 8 segments, 3 noyaux, 3 foramens, 4 territoires (moteur, gustatif, parasympathique, sensitif), 5 sites lésionnels numérotés (plan, figure 3) avec niveau, déficit, signes, examen orientant et hypothèses, 20 légendes (segments, branches, glandes), 65 termes pour le glossaire.
- Ancres dérivées dans freestyle.py (debut, entree, sortie, genou, avant, milieu, branche_vers, branche_depuis) : foramens, genoux, segments et origines de branches calculés sur la géométrie du modèle. Contrôle : segment mastoïdien 11,3 mm (littérature 12,8 à 13 mm), tympanique 13,3 mm (9,3 mm), corde du tympan 4,0 mm au-dessus du foramen (Gray : environ 6 mm).
- annoter.py : badges contenus dans la hauteur du dessin ; mention « À vérifier » adaptée.
- Blender : le modèle complet (environ 11,5 Go) déclenche l'OOM du box ; tout nouveau rendu exige un .blend réduit sous 5 Go (consigne d'Athéna, 17.10.2026 14:52).
### Sources lues (17.10.2026)
- Gray 1918, § 5g The Facial Nerve, fig. 788 à 790, https://www.bartleby.com/107/202.html.
- Gupta et al. 2013, Radiol Res Pract, PMC3676972, section Anatomy.
- PMC6171777, section Results.
- DGN/SNG S2k 030-013 (2022), doi:10.1007/s42451-022-00489-w : Einführung, Klinische Untersuchung, Elektrophysiologische Diagnostik, Bildgebung, Laboruntersuchungen, Prognose.
### À vérifier
- F2 (fond du méat) : position approchée. Repères de la vue plan (Gray 788) non posés.
- L1 : conduite en urgence à sourcer (Swiss Stroke Society ou ESO) ; repère au centre du gyrus précentral. L5 : critère tumoral à sourcer.
- Identifiants hyp à créer dans hyp.json ; data/ck/nc.json attend la fusion de PR #20.
### Prochaine action
- Hippocrate et Galien : 65 termes ; Podalire : chaîne clinique des 5 sites ; puis validation de Vial.

## 17.10.2026 · Dédale · préréglages (une image = une idée)
- L’image unique de 30 repères est remplacée par 5 préréglages : trajet (rocher agrandi, encart), branches (profil), fonctions (trois quarts, aplats pâles), lésions 1 à 5 (1 en rouge, dans l’encart), plan.
- Branches en profil plutôt que de face : rendu de face essayé : les 5 branches se tassent sur une bande verticale de la joue et les repères marginal et cervical se confondent ; en profil, elles s’ouvrent en éventail (T-Z-B-M-C de haut en bas).
- Trajet : l’étiquette « segment labyrinthique » est fondue dans « ganglion géniculé » (repères distants de 12 px même agrandis).

## Podalire · chaîne clinique du VII (NC-1) · 17.10.2026, Europe/Zurich

### Décisions
- 16:45 · Branche feat/nc07-chaine créée depuis origin/main (dbf010c, PR #20), puis fusion de feat/ck-glossaire-lot01 (PR #22, verte, non encore fusionnée) : les syndromes citent ses identifiants glo (paralysie-faciale-peripherique, -centrale, signe-de-charles-bell, hyperacousie, syndrome-de-ramsay-hunt…), que G5 exige. La PR #22 doit donc entrer dans main avant ou avec celle-ci.
- 16:50 · Un syndrome par site (vii-site1-central, vii-site2-genicule, vii-site3-tympanique, vii-site4-mastoidien, vii-site5-extracranien), module neuro-nc ; les 12 identifiants d’hypothèses reprennent ceux de nc/annot/nc07.yml (Ariane), sans renommage.
- 16:55 · « Examen de référence » seulement quand la source le dit : IRM T1 avec gadolinium pour le schwannome vestibulaire (EANO 2020, « gold standard ») et IRM sans et avec gadolinium pour la tumeur cérébrale (EANO 2021, « diagnostic gold standard »). Toutes les autres hypothèses sont en 1re, 2e et 3e intention. L’artériographie numérisée est nommée « examen de référence » des malformations dans l’alternative de l’hémorragie (ESO-EANS 2025, « reference standard of IADSA »).
- 17:00 · Rouge (bloquant: true) pour les deux seules urgences vitales : AVC ischémique et hémorragie intracérébrale.
- 17:05 · Aucune posologie écrite. Le zona otique renvoie par dose_ref aux deux lignes suisses du valaciclovir lues par Galien (valaciclovir-po-adulte-zona, -ir). La corticothérapie (HUG : schéma par kg ; DGN : deux schémas en mg) ne correspond à aucune ligne de doses_ch.json : elle reste « À vérifier ».
- 17:10 · Divergence signalée, non tranchée : la ponction lombaire est recommandée chez l’adulte par la DGN, mais réservée aux formes atypiques par les HUG ; l’antiviral dans la paralysie de Bell vise les grades V-VI (DGN) ou IV-VI (HUG). Les deux positions sont écrites, avec leur source.
- 17:15 · Quatorze termes que Lyncée signalait ont été reformulés sans perte de sens (« moitié de la langue » pour « hémilangue », « malformation caverneuse », « ENMG », « fosse postérieure »…). Huit sigles ou mots anglais présents seulement dans les titres de sources sont exclus avec motif, selon le précédent CEEDMM/PNDS.
- 17:20 · nc07.vues pointe vers les préréglages fusionnés (branches = profil, lésions = trois quarts, plan) ; à remplacer quand Dédale livre les 3 vues « crâne, nerf jaune ».

### Sources lues (17.10.2026)
- HUG, Service des urgences, « Paralysie faciale périphérique », protocole v1.2 du 04.04.2023, § 1 à 6, https://www.hug.ch/sites/interhug/files/2023-04/paralysie_faciale_peripherique_avril_2023_1.pdf.
- DGN/SNG, S2k 030-013 « Therapie der idiopathischen Fazialisparese » (28.02.2022) : Was gibt es Neues, Die wichtigsten Empfehlungen, § 2.1 (Tabelle 1), 2.2, 2.3, 2.4, 2.5, 2.6, 3.1 (zona otique), 3.2 et Tabelle 4, https://register.awmf.org/assets/guidelines/030-013l_S2k_Therapie-Idiopathische-Fazialisparese-Bell%E2%80%99s-Palsy_2022-05.pdf.
- DGN, S3 030-071 « Neuroborreliose » (30.04.2024) : § 3.10 (critères possible, probable, certaine), recommandations sur l’antibiothérapie et sa durée, § 5.2.4 et recommandation 15, https://register.awmf.org/assets/guidelines/030-071l_S3_Neuroborreliose_2024-05.pdf.
- ESO, thrombolyse intraveineuse (2021), recommandations et déclarations de consensus (version MAGICapp), doi:10.1177/2396987321989865.
- ESO-ESMINT, thrombectomie mécanique (2019), questions 1, 2, 8.4 et 8.5 (version MAGICapp), doi:10.1177/2396987319832140.
- ESO-EANS, hémorragie intracérébrale (2025), PICO 1.1, 1.2.1, 1.2.2, 2, 4.1, 5.2 (PMC12098356 et présentation officielle sur eso-stroke.org), doi:10.1177/23969873251340815.
- EANO, schwannome vestibulaire (2020), Abstract, Diagnostic Procedures (Imaging), Therapeutic Strategies, Follow-up (PMC6954440), doi:10.1093/neuonc/noz153.
- EANO, gliomes diffus de l’adulte (2021), Preoperative diagnostics, Tissue acquisition (PMC7904519), doi:10.1038/s41571-020-00447-z.
- ESMO-EURACAN, cancers des glandes salivaires (2022), Diagnostic work-up, Recommendations, Surgical management (PMC9808465), doi:10.1016/j.esmoop.2022.100602.

### À vérifier
- Fracture du rocher : choix de l’imagerie (scanner haute résolution) et critères chirurgicaux ; une recommandation ENT UK existe (entuk.org, hors liste blanche G3) : Argos et Janus jugent s’il faut l’admettre.
- Otite moyenne compliquée et cholestéatome : choix scanner ou IRM, antibiothérapie, paracentèse, chirurgie.
- Plaie des rameaux : conduite, suture ou greffe et délai.
- Précautions des produits de contraste iodé et du gadolinium (insuffisance rénale, grossesse).
- L5 (Ariane) : « l’atteinte d’un seul rameau évoque une tumeur » reste à sourcer ; « évolution chronique atypique, cause tumorale » est désormais sourcée (HUG § 2).
- Posologies : corticothérapie de la paralysie de Bell et du zona otique, altéplase et ténectéplase, antihypertenseurs de l’hémorragie, antidotes des anticoagulants, antibiotiques de la neuroborréliose.

### Termes pour Galien
Déjà dans la liste d’Ariane (nc07.yml) : méat acoustique interne, angle ponto-cérébelleux, canal facial, nerf grand pétreux, corde du tympan, nerf du muscle stapédien, réflexe stapédien, lagophtalmie, otoscopie, conque, cholestéatome, neuroborréliose, zona otique, schwannome vestibulaire.
Nouveaux (chaîne clinique) : thrombolyse intraveineuse ; thrombectomie mécanique ; altéplase ; ténectéplase ; imagerie de perfusion ; décalage diffusion-FLAIR ; angioscanner ; angio-IRM ; IRM de diffusion ; séquence FLAIR ; gadolinium ; INR ; antivitamine K ; anticoagulant oral direct ; numération plaquettaire ; circulation antérieure ; centre de l’AVC (unité neurovasculaire) ; signes précoces d’ischémie ; hémorragie intracérébrale ; hématome ; cause macrovasculaire ; malformation artérioveineuse ; anévrisme intracrânien ; fistule durale ; malformation caverneuse ; thrombose veineuse cérébrale ; artériographie numérisée ; concentré de complexe prothrombinique ; antidote spécifique ; fosse postérieure ; trouble de la déglutition ; diagnostic tissulaire ; échelle de House-Brackmann ; syncinésie ; électroneuromyographie (ENMG) ; perte axonale ; amplitude motrice ; charge palpébrale ; réanimation microchirurgicale ; greffe transfaciale ; anastomose hypoglosso-faciale ; transfert musculaire ; conduit auditif externe ; vésicules ; zona sans éruption ; virus varicelle-zona ; ponction lombaire ; méningite lymphocytaire ; barrière hémato-encéphalique ; synthèse intrathécale d’anticorps ; index d’anticorps spécifiques ; immunoblot ; test immuno-enzymatique ; érythème migrant ; radiochirurgie ; audiométrie ; monitorage du nerf facial ; réunion de concertation pluridisciplinaire ; mastoïde ; mastoïdite ; otite moyenne ; paracentèse ; cytoponction à l’aiguille fine ; système de Milan ; biopsie au trocart ; parotidectomie totale ; adénopathie ; diagnostic d’exclusion ; tumeur de la parotide ; fracture du rocher ; otalgie ; dysgueusie.
Lyncée ne détecte pas ces termes (règles d’affixes) : G4 passe, mais la règle du glossaire imbriqué exige leur définition.

### Prochaine action
- Galien : revue de niveau 2 du diff data/ck (audit:galien), définitions ci-dessus, posologies AIPS.
- Podalire : sourcer les points « À vérifier » (NC-1b), puis chaîne des paires suivantes après validation du pilote par Vial.
## 17.10.2026 · Dédale · trois vues, crâne au crayon, nerf jaune
- Direction de l'utilisateur : moins d'images, croquis forts. Publié : nc07-face, nc07-profil, nc07-34 seulement ; tour de 8 vues, préréglages séparés et plan Gray retirés (le plan reste donnée source dans nc/trait).
- Crâne : tools/dedale/crane.py, os seuls (48 objets, 151 227 faces décimées à 118 512), scène vide, pic mémoire 0,94 à 1,06 Go ; tissus mous absents.
- Nerf : jaune #FFC400 (6,5 px) cerné de #5a4500 (1 px), dessiné au-dessus de tout ; noyaux pleins en jaune.
- Fonctions : l'aplat « moteur » est retiré (il couvrait la voûte) ; la motricité est portée par le nerf lui-même.

## Hermès · NC-0 interaction · 17.10.2026, Europe/Zurich

Fait : patch 0012, avec le lieur gloLink, la pile de fenêtres imbriquées (5 niveaux, Retour, fil d’Ariane, sans cycle), les types glo, syn, hyp (exploration puis prise en charge), loc (synthèse locale, onglets A et B) et nc (vues, couches, tour 8 vues, repli <img>). Ajouts : tools/nc_svg_js.py, données d’essai tests/fixtures/ck, tests/test_ck_ui.py (49 contrôles, ordinateur et Pixel 7, texte coupé compris). Suite complète 170/170, gardes 5/5.
Sources : aucune source clinique utilisée ; aucune donnée clinique n’est introduite.
À vérifier : les entrées de glossaire pour les mots d’interface « Foramens » et « Sites lésionnels » ; le rendu final des .ck-* dans les 10 thèmes d’Apollon ; les doses (AIPS/Swissmedic) relèvent d’Hippocrate et de Janus.
Prochaine action : après les fusions d’Atlas, d’Hippocrate et de Dédale, rebaser (ssp-fusion-patch), puis rejouer test_ck_ui et les captures sur les vraies données.

### Hermès · intégration sur main (9ae4ed1 puis 4ff1cec) · 17.10.2026, Europe/Zurich
Fait : le patch est renuméroté 0012, après le 0011 d’Atlas. Le lieur lit CK_GLO_INDEX.e et charge la tranche de définitions à l’ouverture ; syn, hyp, loc, nc, src et doses_ch se chargent à la demande, avec redessin sur place. Plus aucun « .. » (ckP). Les états de Dédale (data-etats) sont branchés. Les vues sont lues dans nc.json (3 vues). nc07.js est régénéré. Sur mobile, le schéma tient en largeur. Le réglage « Fond doré » est retiré de l’en-tête. G7 : l’urgence passe par .urg[data-bloquant]. test_ck_ui compte 61 contrôles, dont 12 sur les données réelles.
Sources : aucune source clinique ajoutée.
À vérifier : chevauchement d’étiquettes de la vue de face (Dédale) ; libellé « Par défaut » du sélecteur de fond (Apollon, patch 0005).
Prochaine action : quand loc.json aura des entrées, ajouter une vérification de la synthèse locale sur les données réelles.
Ajout (17:45) : repères numérotés g.nc-num, avec bulle « n · nom » et ouverture de la fiche du glossaire dans la pile ; case « Légende numérotée » (couche legende), construite sur le contrat de Dédale avant la fusion de sa PR (données d’essai). test_ck_ui compte 66 contrôles.

## 17.10.2026 · Dédale · repères numérotés, dessin aéré
- Retour de l’utilisateur : « Trop saturé d'annotation. Numéro fléché et cliquable avec le nom de la structure anatomique pour aérer au maxi. »
- Règle pour toutes les paires : aucun texte sur le dessin sauf le titre ; un numéro cerclé (fond blanc, trait sombre, chiffre gras ; 30 px hors tout sur 800 px, 13,5 px à 360 px) et une flèche fine par structure ; repères aérés, jamais l’un sur l’autre ni sur le nerf jaune ; légende numérotée en 2 colonnes, petits caractères, sous le dessin (couche « legende », masquable) ; même numéro, même structure dans les 3 vues.
- Placement : candidats autour de l’ancre (40 à 200 px), interdits sur le nerf et les noyaux (8,5 px d’épaisseur + 3 px de jeu), conflits (cercles à moins de 2 rayons + 14 px, flèches croisées, flèche sous un cercle) résolus par recherche locale à graine fixe, puis aération par répulsion (200 départs).
- Correction au passage : les épaisseurs du nerf (8,5 px, dont 6,5 px de jaune) et du cerne des noyaux (1 px) sont enfin celles de l’image : svgo applique les transformations aux chemins, la feuille de style les réduisait d’un facteur 1,3.
- Contrat des repères pour Hermès : HANDOFF.md, section Dédale.


## Podalire · chaîne justifiée du VII (G8) · 17.10.2026, Europe/Zurich
Retour de Vial : « Tu parles de thrombolyse comme si tu avais introduit le principe… Pourquoi pas autre chose ? ».
### Décisions
- Chaque examen porte `mecanisme`, `principe`, `recherche`, `pourquoi_ce_choix` ; chaque moyen spécifique porte `mecanisme`, `principe`, `texte` (le moyen nommé), `pourquoi_ce_choix`, `limites`. L’ancien champ `pourquoi` disparaît du schéma.
- G8 (tools/audit/niveau1.py, étape CI dédiée) refuse un champ absent, vide, de moins de 20 caractères ou 3 mots, ou recopié d’un autre champ ; une phrase « … À vérifier » reste admise faute de source lue. Les quatre champs entrent dans CHAMPS_PROSE (G6).
- Central ou périphérique : syn.json (5 syndromes) et nc07 site 1 disent que la partie haute du noyau reçoit des fibres des deux hémisphères et la partie basse d’un seul ; la lésion au-dessus du noyau épargne donc le front, la lésion du nerf ne l’épargne pas. Chaque syndrome renvoie à `nc|nc07|voie_motrice` (champ syn.vues) ; ck_build avertit tant que Dédale n’a pas livré la vue, et la fenêtre retombe sur la première vue du nerf.
- Patch 0013 : la fenêtre affiche ces champs, une ligne par partie, et le lien « Sur le schéma ».
### Sources lues (17.10.2026)
- CEN, Sémiologie neurologique, chapitre 9, nerf facial : noyau double, partie supérieure à afférences pyramidales bilatérales, partie inférieure à afférences unilatérales.
- ESO-EANS 2025 (PMC12098356) : la pression élevée s’associe à l’expansion de l’hématome ; baisser la pression vise à la prévenir ; produits de dégradation et lésion secondaire ; antidotes (PCC et vitamine K, idarucizumab, andexanet alfa) à faible niveau de preuve.
- DGN 030-013 : causes discutées (inflammation auto-immune, réactivation HSV-1, facteurs ischémiques) ; bénéfice des corticoïdes (NNT 10) ; troubles du sommeil rapportés ; antiviral seulement en plus, formes sévères.
- DGN 030-071 : doxycycline aussi efficace que les bêtalactamines, même tolérance ; limite d’âge de 8 ans levée ; choix selon allergies, grossesse, mode d’administration.
### À vérifier (en plus de la liste NC-1)
- Mode d’action des thrombolytiques et des corticoïdes au-delà de ce que disent les lignes directrices lues ; complications propres de la thrombectomie ; « l’hémisphère opposé » pour la partie basse du noyau (le CEN écrit « unilatérales ») ; choix scanner ou IRM pour l’os du rocher.
### Termes pour Galien (nouveaux)
zone récupérable (pénombre) ; expansion de l’hématome ; lésion secondaire ; stent retriever ; aspiration au contact ; reperfusion ; fibrine ; inhibiteur du facteur Xa ; idarucizumab ; andexanet alfa ; dabigatran ; bêtalactamine ; afférences pyramidales ; voie motrice ; clairance de la créatinine.
