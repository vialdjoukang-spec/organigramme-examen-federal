# Interface didactique — avancement au 14.11.2026

## Faits

- 14.11.2026, bulle IMG-001 : le texte n'est plus coupé. La définition est une fiche sous l'image, dans le panneau, relue en entier sur bureau (`progression/captures-interface/IMG-001_desktop_bulle.png`, jusqu'à « Confiance : haute ») et sur mobile (`IMG-001_mobile_bulle.png`). La bande reste sur le foyer.
- Sexe IMG-001 : la légende Cerevisae ne le donne pas. Commons n'a pas d'autre fichier. Les articles CC BY-NC-ND sont écartés. PMC4489032 (CC BY 4.0) est une cohorte : le mot male y est un pourcentage, pas le sexe du cliché. Pas de remplacement.

## Faits (précédent)

- IMG-001, normale : `images/normal/IMG-001_normal.jpg`. TDM axiale sans injection, coupe 26, homme de 18 ans, CC0, Mikael Häggström, M.D. Source lue : https://commons.wikimedia.org/wiki/File:CT_of_a_normal_brain,_axial_26.png (légende du 16.03.2019). Scout sagittal retiré. Même étage que le pathologique (orbites, ethmoïde, lobes temporaux), relu à l'œil.
- IMG-001, pathologique : fichier Cerevisae déjà en place, CC BY-SA 4.0. Légende sans sexe et sans la mention « sans injection ». Bande de 16 points sur le foyer hyperdense au bout de la flèche blanche incrustée. Définition : Chieng et al., Singapore Med J 2020;61(5):230-237, lue le 14.11.2026. Statut : **partiel**.
- Interface : normale à gauche, pathologique à droite. Flèches cachées au départ, bouton « Révéler les flèches ». Clic sur le numéro : bande pointillée jaune (silhouette, élargie à l'écran pour rester lisible), nom, définition, source, preuve. « Mode défi » puis « Révéler et noter » : score. Sexe affiché dans les crédits.
- Captures relues à l'œil : `shots/interface_IMG-001.png` (flèches cachées), `shots/interface_IMG-001_bulles.png` (définition + bande), `shots/interface_IMG-001_defi.png` (Score 1/1, pastille dans la bande), `shots/interface_mobile_IMG-001.png`. Console Playwright : 0 erreur.
- `validate.py` refuse un complet sans normale, sans sexe établi et concordant (M/F), avec un contour rectangulaire ≤ 5 points, ou avec une définition « À vérifier ». 555 manifestes : 0 erreur, 0 complet valide, 350 partiels, 205 introuvables.
- Sexe posé depuis la légende (`caption_source`) seulement. Mots explicites : male/boy/homme/year-old man, female/woman/girl/femme. « man » seul ignoré (faux ami allemand « Man erkennt »). Les deux sexes dans la même légende → « À vérifier ».

## En cours

- Quatre lots disjoints sur les 61 paires qui ont déjà les deux images (le dépôt n'en a pas 112), puis les partiels qui n'ont que la pathologique. Chaque lot remplace la normale pour le même sexe explicite et redessine les contours grossiers. L'auditeur distinct relit ensuite contours et captures.

## Bloquants

- IMG-001 ne peut pas être complet : sexe pathologique À vérifier, séquence non écrite, flèche et cartouche déjà incrustés (le défi est éventé par cette flèche).
- Aucune paire n'a le même sexe explicite des deux côtés. Complets retirés pour légende muette sur le sexe : IMG-250, IMG-257, EXP-112.
- Sexe explicite d'un seul côté (l'autre absent ou À vérifier), non relus image par image : EXP-052 M, EXP-148 M, FTE-05 M, FTE-41 M, IMG-011 F, IMG-051 M, IMG-055 F, IMG-061 M, IMG-100 F, IMG-108 M, IMG-111 F, IMG-153 M, IMG-158 M, IMG-191 F, IMG-205 M, IMG-224 M, IMG-235 F, IMG-249 F, IMG-285 F, IMG-312 F, IMG-331 F, IMG-344 F.
- Tous les autres côtés : sexe À vérifier. Contours hors IMG-001 non relus à l'œil dans ce passage.

## Automates actifs

- GitHub Actions du dépôt, inchangé. Pas de veille locale.
