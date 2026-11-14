# Jetons — nuit du 14.11.2026 (Europe/Zurich)

Les durées et les appels évités sont des estimations, marquées comme telles. Seuls les éléments réellement passés par un manifeste comptent comme traités.

## Harnais (coordinateur)

- Éléments traités : 0 diagnostic publié. Un essai de rendu sur une vraie paire Commons (pneumothorax gauche, domaine public, et thorax normal CC0) est archivé dans progression/essai-reel/. Statut de cet essai : partiel, écart expiration contre inspiration, sujets différents. Ce n'est pas le manifeste de IMG-134.
- Appels de modèle : le placement du contour et la lecture des deux clichés sont le jugement radiologique. Le téléchargement, la validation, le rendu et la capture sont des scripts.
- Appels de modèle : 1 session coordinateur pour le jugement du rendu (flèche, contour, définition au clic). Le téléchargement, la validation, le rendu et les captures de l'essai sont des scripts.
- Durée : le contrôle négatif de `validate.py` et l'essai visuel tiennent en une commande `essai_harnais.py` (estimation : quelques minutes, pas une mesure d'horloge de jeton).
- Épargné par les scripts (estimation) : un essai du viewer relancé à la main, case par case, aurait relu le gabarit entier à chaque correction. Ici `validate.py` refuse seul un point hors image, un polygone ouvert, une définition vide et une définition non sourcée sur un statut complet.

## Lots IMG (agentA/imagerie-lot1 à lot4)

- Lot 1, IMG-344 → IMG-259 : non commencé. Éléments traités 0. Appels 0.
- Lot 2, IMG-258 → IMG-173 : non commencé. Éléments traités 0. Appels 0.
- Lot 3, IMG-172 → IMG-087 : non commencé. Éléments traités 0. Appels 0.
- Lot 4, IMG-086 → IMG-001 : non commencé. Éléments traités 0. Appels 0.
- Épargné par les scripts (estimation) : recherche Commons/Open-i, cache disque, normalisation JPEG et `validate.py` évitent de réécrire ces étapes dans le contexte du modèle. Le gain chiffré n'est pas mesuré.

## Audits (agentB/imagerie-audit1 à audit4)

- Non commencés : un audit ne démarre qu'une fois des manifestes écrits, et ne corrige que ce qu'il a revu.

## Explorations EXP-153 → EXP-001, puis FTE

- Non commencées. Elles attendent la fin de l'imagerie.

## Point à 02:58 Europe/Zurich (estimation d'horloge, pas une mesure de jetons)

- Demandes de fusion fusionnées par commit de fusion, CI verte : #678 (harnais), #679 (IMG-086–082), #680 (IMG-258–254), #681 (IMG-172–168).
- Les chercheurs continuent. Le bilan HTML est recalculé depuis les manifestes des worktrees.
- Épargné par les scripts (estimation) : validate.py a refusé les manifests incomplets avant les audits ; les téléchargements passent par le cache commun.

## Point à 03:55 Europe/Zurich

- Lot 1 (IMG-344→259) : 86/86 manifestes, validate.py sans erreur (57 partiels, 29 introuvables, 0 complet). Audit indépendant fusionné pour IMG-344→315. IMG-314→259 pas encore tous audités.
- Lots 2, 3 et 4 encore en recherche. Explorations et FTE pas commencées : l'imagerie n'est pas close.
- Fusions de la nuit : #678 #679 #680 #681 #682 #683 #684 #685 #686 #687.

## Point à 04:50 Europe/Zurich

- IMG : lots 1, 2 et 4 ont 86/86 manifestes, validate.py sans erreur. Lot 3 : environ 61/86, reprise en cours vers IMG-111.
- Audits fusionnés par commit de fusion après CI verte : #679 #680 #681 #683 #684 #685 #686 #687 #688 #689 #690 #691.
- Explorations EXP et fiches FTE : pas commencées, l'imagerie du lot 3 n'est pas close.
- Archive horaire toujours lancée (tmux imagerie-heure).

## Point à 05:30 Europe/Zurich

- Imagerie : 344/344 manifestes, validate.py sans erreur sur chaque lot. Audits fusionnés par vagues (dernier #692). Il reste des paquets non audités (IMG-269→259, IMG-208→173, IMG-137→087, IMG-036→001, et d'autres déjà en cours d'audit).
- Explorations : quatre chercheurs lancés. EXP-3 a déjà poussé des introuvables et des paires. Le catalogue EXP/FTE est sur main (#696).
- FTE : pas commencées.
- Bilan HTML recalculé sur le disque : voir BILAN_NUIT_20261114.html. Archive horaire active.

## Point à 06:07 Europe/Zurich

- 555/555 éléments ont un manifeste. validate.py : zéro erreur sur les quatre lots d'imagerie, sur EXP-038→001, et sur FTE-30 à FTE-33.
- Décompte du bilan : voir BILAN_NUIT_20261114.html régénéré à cette heure (plus aucun « en recherche »).
- Les explorations et les fiches ne sont pas encore auditées ni fusionnées. Une partie de l'imagerie l'est (fusions #679 à #695).
- Estimation : les scripts ont fait le téléchargement, la validation et le décompte. Le jugement (lire l'image, poser le contour, choisir complet/partiel/introuvable) est resté aux modèles.


## Décompte après audit · 14.11.2026

Les 555 manifestes audités sont sur main : 3 complets, 347 partiels, 205 introuvables, 0 en recherche. Le bilan HTML reprend ces statuts, élément par élément.
