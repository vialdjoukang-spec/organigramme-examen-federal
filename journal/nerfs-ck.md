# Journal · Nerfs crâniens et partie CK (plan du 17.10.2026)

Chaque agent ajoute ses entrées datées (Europe/Zurich) : ce qui est fait, sources lues, « À vérifier », prochaine action.

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

## Hermès · NC-0 interaction · 17.10.2026, Europe/Zurich

Fait : patch 0011, avec le lieur gloLink, la pile de fenêtres imbriquées (5 niveaux, Retour, fil d’Ariane, sans cycle), les types glo, syn, hyp (exploration puis prise en charge), loc (synthèse locale, onglets A et B) et nc (vues, couches, tour 8 vues, repli <img>). Ajouts : tools/nc_svg_js.py, données d’essai tests/fixtures/ck, tests/test_ck_ui.py (49 contrôles, ordinateur et Pixel 7, texte coupé compris). Suite complète 170/170, gardes 5/5.
Sources : aucune source clinique utilisée ; aucune donnée clinique n’est introduite.
À vérifier : les entrées de glossaire pour les mots d’interface « Foramens » et « Sites lésionnels » ; le rendu final des .ck-* dans les 10 thèmes d’Apollon ; les doses (AIPS/Swissmedic) relèvent d’Hippocrate et de Janus.
Prochaine action : après les fusions d’Atlas, d’Hippocrate et de Dédale, rebaser (ssp-fusion-patch), puis rejouer test_ck_ui et les captures sur les vraies données.
