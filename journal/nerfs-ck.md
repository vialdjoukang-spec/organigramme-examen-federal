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
