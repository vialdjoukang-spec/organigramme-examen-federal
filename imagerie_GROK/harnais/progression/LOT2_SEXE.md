# Lot 2 — sexe explicite et silhouette

Branche `cursor/interface-didactique-ffbc`. 33 identifiants. `validate.py --only` : 33 partiels, 0 erreur, 0 complet.

Règle appliquée : le sexe n'est posé que si `caption_source` contient male, female, woman, women, girl, boy, homme, femme, garçon, ou « year-old man » / « years-old man ». « Man erkennt », « 40 F », Mann/Frau, et les codes de nom de fichier (66M, 88W, 82M, 75jm, 90W) ne comptent pas. Sinon sexe « À vérifier » et statut partiel. Un complet exigerait les deux sexes égaux (M ou F), un contour fermé d'au moins 8 sommets non rectangulaire relu sur l'overlay, et une `definition_source` autre que « À vérifier ».

## Complets

Aucun.

## Paires du même sexe, encore partielles

- IMG-134 : normale et pathologique M (homme de 30 ans, Commons CC0 ; pneumothorax d'un male de 23 ans, CC BY-SA). Contour du décollement pleural gauche de l'image (côté droit du patient). `definition_source` « À vérifier ». Le cliché ne montre pas le pneumothorax compressif.
- IMG-153 : les deux M (même thorax normal ; cathéter, male de 37 ans, domaine public). Bande le long du cathéter. `definition_source` « À vérifier ».

## Pathologique sexé, sans normale du même sexe et du même plan

- IMG-089 : pathologique M (« 57 year old man », myélome, foyer ostéocondensant). Pas de TDM corps entier basse dose masculine libre.
- IMG-091 : pathologique F (« 57-year-old woman », collection épidurale postérieure et bombement discal). La séquence du cliché est T2, pas une injection de gadolinium. Pas d'IRM lombaire féminine normale de même séquence.
- IMG-158 : normale M (« 15-year-old-boy », TEP-TDM). La légende Takayasu ne donne pas le sexe, et le plan n'est pas le même.

## Normales sexées réutilisées, pathologique sans mot de sexe

- IMG-132, IMG-164 : thorax PA, « 21 year old woman » (F). Épanchement et fractures de côtes : légendes sans sexe. IMG-132 : ménisque à droite de l'image, au-dessus de la bulle gastrique.
- IMG-133, IMG-136, IMG-138, IMG-154, IMG-155, IMG-157, IMG-159 : coupe TDM abdominale, « 21 year old male » (M). Écart de région ou de phase ; pathologiques « À vérifier ». IMG-136 : le manteau visible est à droite de l'image, sans repère R/L pour confirmer « rechts ».

## Les deux côtés « À vérifier »

IMG-160 (mama n'est pas femme), IMG-161 (« 40 F » n'est pas female/woman/femme ; pas de lésion décrite, donc pas de contour), IMG-166 (« Man erkennt » écarté), IMG-071 à IMG-076, IMG-078 à IMG-081, IMG-083 à IMG-085, IMG-087, IMG-088, IMG-090. Pour 071–091 aucune image normale de même modalité, même plan et même sexe explicite n'a été retenue sous licence CC0, domaine public, CC BY ou CC BY-SA. Les contours de lésion ont été redessinés (≥ 8 sommets) et relus sur `captures-interface/lot2/`. IMG-084 garde la source Zileli déjà présente ; elle ne suffit pas sans normale ni sexe.

## Bloquants

1. Légendes sans mot de sexe autorisé : impossible de poser M ou F.
2. IMG-134 et IMG-153 : sexes égaux, définition encore « À vérifier ».
3. IMG-089 et IMG-091 : un seul côté sexé, pas de normale appariée.
4. IMG-161 : aucun contour, aucune lésion décrite.
5. Écarts de plan ou de séquence signalés par validate (thorax PA vs face debout, TDM abdomen vs thorax, TEP multiplanaire vs coronal, CC vs oblique).
