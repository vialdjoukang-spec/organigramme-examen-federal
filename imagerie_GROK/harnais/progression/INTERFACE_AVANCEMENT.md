# Interface didactique — avancement au 14.11.2026

## Faits

- Second audit de [l'auditeur](bc-143a29d4-f998-55ad-93ab-82f2cc05b769), vitrine IMG-134, branche `cursor/audit-prototypes-ffbc`. Couleurs, survol des poumons et du cœur, pointillé distinct et zoom lié acceptés. Reprises faites : la paroi ne teinte plus tout le cliché, le diaphragme s'épaissit au survol, la bulle de structure est au-dessus de chaque image (y compris mobile), l'indice 1 dit « Diagnostic : Pneumothorax », le zoom des boutons reste centré, et le pointillé suit la ligne pleurale au lieu de couvrir l'hémithorax. Captures 09, 10, 15, 17, 18, 20 et 22 refaites.
- Audit de [l'auditeur](bc-143a29d4-f998-55ad-93ab-82f2cc05b769) sur les six captures anciennes, branche `cursor/audit-prototypes-ffbc`. Rien n'est complet. IMG-001 : les ellipses ne suivent pas les globes, l'ethmoïde ni le parenchyme. IMG-134 de ces captures : zigzags, et le contour de lésion couvre l'hémithorax au lieu de la ligne pleurale. La vitrine ultérieure change les couleurs et le survol ; elle ne corrige pas ce contour de lésion. Textes entiers et anonymisation acceptés.
- [Lot 1](bc-9fc98fc7-7fb5-55ba-9689-fcbdbc42cf00) fusionné : IMG-023, 061, 064, 086, 105, 106, 108, 114, 118, 122, 123, 124, 125, 126, 129 restent partiels. Âges seulement quand la légende les donne. Anonymisation relue. Pas de complet.
- [Lot 1](bc-9fc98fc7-7fb5-55ba-9689-fcbdbc42cf00), recalage : mêmes identifiants des deux côtés pour IMG-023, 086, 105, 106, 108, 114, 118, 122, 123, 124, 125, 126 et 129. IMG-061 et IMG-064 sans couche, les masques ne suivaient ni l'os ni l'air. Âges conservés. Pas de complet.
- [Lot 2](bc-bcca8c7b-e85f-52c3-9498-16c5550d3fbb) fusionné : IMG-132, 133, 136, 138, 153, 154, 155, 157, 158, 159, 160, 161, 164, 166 restent partiels. IMG-134 non repris. Contours de lésion réécrits seulement pour IMG-132, 158 et 164. Pas de complet.
- [Lot 3](bc-73887395-333c-5a07-9683-0aa8520fe2d2) fusionné : IMG-167, 168, 169, 170, 171, 172, 176, 177, 228, 229, 230, 231, 235, 243, 244 restent partiels. Le contour d'IMG-243 est le même. Contours repris pour l'ascite d'IMG-170 et un kyste d'IMG-230. Les initiales de IMG-244 sont masquées. Pas de complet.
- [Lot 2](bc-bcca8c7b-e85f-52c3-9498-16c5550d3fbb), recalage : contours des deux côtés pour IMG-132, 133, 136, 138, 153, 154, 155, 159, 161, 164 et 166. IMG-157, 158 et 160 sans couche, les tracés traversaient le cadre. Âges et anonymisation conservés. IMG-134 inchangé. Pas de complet.
- [Lot 4](bc-5febe8e9-66eb-56a4-b6ab-b04b994684a1) fusionné : 25 paires d'IMG-245 à IMG-344 restent partielles. Dates, cabinet et marque masqués sur IMG-255, 273, 327 et 337. IMG-267 a 26 et 25 ans, mais le contour de la tête luxée dépasse encore la tête. Pas de complet.
- 14.11.2026 11:20, bouton « Rappel du code couleur structure – aspect ». La légende reprend exactement les couleurs des contours, structures en trait plein et lésions en pointillé, pour la technique affichée. Sans source lue, l'aspect est « À vérifier ». Capture `vitrine/25-legende-couleurs.png`.
- 14.11.2026 11:17, vitrine IMG-134. Anatomie segmentée par `segment.py` (scikit-image, SAM absent), recalée puis ressegmentée. Mêmes identifiants et mêmes couleurs des deux côtés. Survol lié. Lésion en pointillé rouge, distincte. Zoom lié. 24 captures relues dans `progression/captures-interface/vitrine/`, index joint. Le gril costal automatique était trop fragmenté : il n'est pas affiché. Le cœur suit le médiastin, un peu anguleux à la pointe. Une seule lésion visible.
- 14.11.2026 11:03, contraste. Le texte courant est blanc (#FFFFFF) ou #F2F4F7, les liens sont #A8DCFF, les bulles sont opaques. `scripts/contraste.py` refuse un texte sous 7:1 et un petit libellé sous 4,5:1. `build_app.py` ne génère plus la page si ce contrôle échoue. Captures relues : `captures-interface/IMG-001_desktop_anatomie.png`, `IMG-001_desktop_indice.png`, `IMG-001_desktop_source.png`, et les trois vues mobiles.
- 14.11.2026 11:01, prototypes IMG-001 et IMG-134. L'image normale est agrandie à l'affichage (échelle 1,12, sans déformation). Restent visibles l'âge, le sexe et « Source » (auteur, licence, URL et légende au survol). Le bouton Anatomie ajoute les couches de dehors en dedans ; le survol donne la description, source « À vérifier ». Le bouton Indice passe du diagnostic à la région, puis au signe, puis à la lésion. `validate.py` refuse un complet sans `anonymisation_verifiee` = oui des deux côtés, sans âges écartés d'au plus 15 ans, sans au moins trois couches, ou sans indices diagnostic / région / signe. Aucun des deux n'est complet : IMG-001 n'a pas l'âge pathologique ; IMG-134 n'illustre pas le pneumothorax compressif et sa définition reste « À vérifier ». Âges de IMG-134 : 30 ans et 23 ans. Anonymisation relue : pas de nom, de date ni d'établissement (marqueurs R, L et STAAND conservés). Captures : `captures-interface/IMG-001_desktop_anatomie.png`, `IMG-001_desktop_indice.png`, `IMG-134_desktop_indice.png`, et les mêmes en mobile.
- 14.11.2026, bulle IMG-001 : le texte n'est plus coupé. La définition est une fiche sous l'image, dans le panneau, relue en entier sur bureau (`progression/captures-interface/IMG-001_desktop_bulle.png`, jusqu'à « Confiance : haute ») et sur mobile (`IMG-001_mobile_bulle.png`). La bande reste sur le foyer.
- Règle de Vial du 14.11.2026 10:48, précisée : le même sexe seulement pour bassin, sein, organes génitaux. Ailleurs, adulte suffit. L'adulte vient de la légende ou d'un signe visible, noté dans `adulte_preuve`. Sans signe concluant : « À vérifier ». `validate.py` refuse un complet sans cette preuve.
- IMG-001 patho : adulte À vérifier (ethmoïde pneumatisé, pas de suture ni de physe sur la coupe). IMG-134 : oui des deux côtés (physes humérales soudées). IMG-136 : oui des deux côtés (squelette adulte). IMG-250 : oui des deux côtés (utérus adulte) mais sexe non écrit, donc pas complet. Aucun des quatre n'est complet (séquence ou sexe).
- `scripts/segment.py` segmente depuis la pointe (scikit-image : seuil, watershed, contour actif). SAM n'est pas installé : repli annoncé. `validate.py` rejette un polygone trop régulier et une lésion non ponctuelle de moins de 8 points.
- IMG-243 relu après segmentation : le contour suit le champ parenchymateux (bord du secteur et ligne cutanée), le point rouge est dedans, ce n'est plus un décagone. Capture `captures-interface/segment/IMG-243.png`. Reste partiel (sexe du testicule non écrit).
- Essais non retenus à l'œil : IMG-023 (tout le cerveau), IMG-061 (la moitié de la mandibule), IMG-064 (la flèche incrustée). Ils ne sont pas écrits dans les manifestes.
- Lots 1, 2 et 4 ont rendu (0, 0 et 2 complets annoncés). Le lot 3 a ensuite posé IMG-235 en complet. Relus : IMG-235, IMG-257 et IMG-267 sont des polygones réguliers, pas le bord de la lésion. Les trois sont repassés en partiel.
- Contrôle à l'œil des preuves d'adulte (`bc-4f77b9e3-02f6-5e6e-b53f-3ec179f6a4f1`) : les signes non conclusifs sont rejetés. IMG-136 patho et IMG-250 patho sont donc « À vérifier ». IMG-001 normal, IMG-134 et IMG-250 normal restent adultes par la légende (âge écrit).

## Faits (précédent)

- IMG-001, normale : `images/normal/IMG-001_normal.jpg`. TDM axiale sans injection, coupe 26, homme de 18 ans, CC0, Mikael Häggström, M.D. Source lue : https://commons.wikimedia.org/wiki/File:CT_of_a_normal_brain,_axial_26.png (légende du 16.03.2019). Scout sagittal retiré. Même étage que le pathologique (orbites, ethmoïde, lobes temporaux), relu à l'œil.
- IMG-001, pathologique : fichier Cerevisae déjà en place, CC BY-SA 4.0. Légende sans sexe et sans la mention « sans injection ». Bande de 16 points sur le foyer hyperdense au bout de la flèche blanche incrustée. Définition : Chieng et al., Singapore Med J 2020;61(5):230-237, lue le 14.11.2026. Statut : **partiel**.
- Interface : normale à gauche, pathologique à droite. Flèches cachées au départ, bouton « Révéler les flèches ». Clic sur le numéro : bande pointillée jaune (silhouette, élargie à l'écran pour rester lisible), nom, définition, source, preuve. « Mode défi » puis « Révéler et noter » : score. Sexe affiché dans les crédits.
- Captures relues à l'œil : `shots/interface_IMG-001.png` (flèches cachées), `shots/interface_IMG-001_bulles.png` (définition + bande), `shots/interface_IMG-001_defi.png` (Score 1/1, pastille dans la bande), `shots/interface_mobile_IMG-001.png`. Console Playwright : 0 erreur.
- `validate.py` refuse un complet sans normale, sans sexe établi et concordant (M/F), avec un contour rectangulaire ≤ 5 points, ou avec une définition « À vérifier ». 555 manifestes : 0 erreur, 0 complet valide, 350 partiels, 205 introuvables.
- Sexe posé depuis la légende (`caption_source`) seulement. Mots explicites : male/boy/homme/year-old man, female/woman/girl/femme. « man » seul ignoré (faux ami allemand « Man erkennt »). Les deux sexes dans la même légende → « À vérifier ».

## En cours

- Consignes du 14.11.2026 11 h 01 écrites dans `progression/CONSIGNES_14-11-1101.md` et transmises aux quatre lots et à l'auditeur. Prototypes IMG-001 et IMG-134 en place. Le redessin des contours reste scripté (`segment.py`).
- Lot 1 `bc-3c7f04cb-b49c-5f3b-9c92-3af7023e9930` : paires IMG-001 à IMG-129 (16), puis pathologiques IMG-002 à IMG-070.
- Lot 2 `bc-8f34385d-cb6c-53e4-ad71-fdd28d1deedb` : IMG-132 à IMG-166 (15), puis IMG-071 à IMG-141.
- Lot 3 `bc-4e45b5d2-c132-5c1d-bc8e-97181bfc32aa` : IMG-167 à IMG-244 (15), puis IMG-142 à IMG-260.
- Lot 4 `bc-2a7ab1bc-6808-5d9e-a189-7eca3f3eda49` : IMG-245 à IMG-344 (15), puis IMG-263 à IMG-338.
- Audit contours des 61 paires (`bc-4f77b9e3-02f6-5e6e-b53f-3ec179f6a4f1`), seconde lecture avec la règle adulte : IMG-001, IMG-134, IMG-136 et IMG-250 n'ont pas deux adultes établis par les légendes. IMG-250 exige en plus le sexe (utérus), non écrit. 56 contours restent grossiers. 0 complet.
- Le dépôt a 61 paires avec les deux fichiers, pas 112.

## Bloquants

- IMG-001 ne peut pas être complet : la légende pathologique n'établit pas un adulte. La séquence n'est pas écrite. La flèche source est incrustée.
- Relus à l'œil, encore grossiers : IMG-023 (deux pentagones sur les putamen), IMG-061 (hexagone autour de la lyse), IMG-105 (hexagone sur l'infiltrat). Un ovale régulier a été écarté : ce n'est pas le bord de la lésion. Captures : `progression/captures-interface/lot-silhouette/`.
- 56 contours des 61 paires sont grossiers (rectangle, hexagone ou trop peu de points). Seules silhouettes : IMG-001, IMG-134, IMG-136, IMG-250. Elles n'ont pas le même sexe des deux côtés.
- IMG-161 : les deux légendes disent « 40 F » (femme de 40 ans). Sexe posé à F des deux côtés. Reste partiel : deux incidences d'un dépistage sans lésion, aucun contour.
- Complets retirés pour légende muette sur le sexe : IMG-250, IMG-257, EXP-112.
- Sexe explicite d'un seul côté (l'autre absent ou À vérifier), non relus image par image : EXP-052 M, EXP-148 M, FTE-05 M, FTE-41 M, IMG-011 F, IMG-051 M, IMG-055 F, IMG-061 M, IMG-100 F, IMG-108 M, IMG-111 F, IMG-153 M, IMG-158 M, IMG-191 F, IMG-205 M, IMG-224 M, IMG-235 F, IMG-249 F, IMG-285 F, IMG-312 F, IMG-331 F, IMG-344 F.
- Tous les autres côtés : sexe À vérifier. Contours hors IMG-001 non relus à l'œil dans ce passage.

## Automates actifs

- GitHub Actions du dépôt, inchangé. Pas de veille locale.
