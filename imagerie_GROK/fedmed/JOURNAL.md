# Journal FedMed — fenêtres

Branche `leona/fedmed-fenetres`, créée depuis `origin/main` (`65244131a`). Écriture uniquement dans `imagerie_GROK/fedmed/`. Pas de PR, pas de fusion, pas d’issue.

## État

<!-- ETAT:DEBUT -->
- Découpage : 396 fenêtres, dont 132 sans normale au départ. Réinjection brute : octet identique au fichier Drive.
- Fenêtres fusionnées : 396 / 396. Sortie : `sortie/PROGRESSION__FedMed.html`.
- Normales ajoutées : 3 (IMG-157, IMG-159, IMG-257). Fenêtres encore sans normale : 129.
- Images retirées (licence hors liste blanche ou données patient) : 0.
- Signalements : 646, dont 628 « âge ou sexe absent » (cliché conservé), 15 normales locales non ajoutées, 3 normales ajoutées. Détail : `signaux/images_signalees.json`.
- Captures, console sans erreur : `captures/` (IMG-134, IMG-001, IMG-136, IMG-267, EXP-001, EXP-002, EXP-024, EXP-032, IMG-166, IMG-168, plus flèches et légende d'IMG-134).
- Segmentation : 396 fenêtres traitées par segment.py sur les clichés du fichier. Contours marqués approximatifs. 262 fenêtres ont au moins une structure, 306 un contour de lésion.
- Âge et sexe : attestés pour 143 clichés pathologiques (crédit, Europe PMC ou Commons). Sinon la ligne affiche « âge/sexe non documentés ».
- En-têtes de fenêtre et de cartes : fond #F3FAFD, bordure #87CEEB, police Atkinson Hyperlegible, y compris le titre.
- Captures poussées : IMG-134 (vue, flèches, survol, légende), IMG-136, EXP-001, IMG-157 (normale ajoutée), IMG-159, IMG-001, IMG-267, IMG-166, IMG-168, EXP-002, EXP-024, EXP-032.
- Normales ajoutées et gardées : IMG-157, IMG-159, IMG-209, IMG-216, IMG-219, IMG-257. Les candidats dont la légende n'attestait pas un cliché normal, ou dont l'incidence ou la modalité différait, ont été retirés.
- Fenêtres encore sans normale : 126. La recherche Commons et Europe PMC continue par lots. Le dossier leona/ n'est pas modifié.
<!-- ETAT:FIN -->

## Original

- Fichier : `original/PROGRESSION__FedMed.html`.
- sha256 : `92efecc27ab16238b7a123e8b178e687704abbc3464c36dc16e477fc6f6362fc` (identique au mandat).
- Taille sur disque : 40 406 154 octets. Longueur Unicode : 40 196 713 caractères. Le chiffre « 40 196 713 octets » du mandat correspond à cette longueur en caractères, pas à la taille UTF-8.
- Source : téléchargement en lecture seule. Le fichier Drive n’est pas modifié. Il reste le fichier final ; Leona le remplacera après accord de Vial.
- Le dépôt ne contient aucune donnée de `psychotherapie-personnelle-de-Vial/`.

## Décisions

- Une fenêtre est une entrée `enr` du recensement topo-systémique embarqué (`data-emb="rts"`) qui porte un cliché pathologique en data URI. Le décompte attendu est 396, dont 132 `manque_normal`. Les 101 autres entrées (sans cliché) restent dans le squelette.
- Le réencodage qui restitue l’octet d’origine : JSON interne compact `ensure_ascii=False` puis `</` → `<\/` ; HTML embarqué `ensure_ascii=False` puis `<` → `\u003c` ; le reste du fichier est recopié tel quel.
- Image du fichier Drive : retirée du rendu seulement si la licence est hors liste blanche ou si des données patient sont détectées (EXIF/XMP). L’absence d’âge ou de sexe est signalée sur la carte, sans retirer le cliché : ce n’est pas un champ du JSON source, et le retirer viderait la page. Une image locale n’est ajoutée que si la licence est sur la liste blanche, l’âge et le sexe sont présents, et aucune donnée patient n’est détectée.
- Les contours locaux ne sont dessinés que s’ils ont été tracés sur les mêmes octets que l’image affichée. Sinon ils servent au texte (aspect), pas au calque.
- Un aspect sans source lue est marqué « Interprétation de l'image (non sourcée) ».

## Reprise

Les 396 fenêtres sont fusionnées et la sortie est construite. Pour reprendre :

1. `python3 imagerie_GROK/fedmed/scripts/decouper.py` puis `scripts/test_roundtrip.py` si le squelette a changé.
2. `python3 imagerie_GROK/fedmed/scripts/fusionner.py --limite 30` (les identifiants déjà dans `fusion/etat.json` sont sautés).
3. `python3 imagerie_GROK/fedmed/scripts/reinjecter.py`
4. Captures : `scripts/capturer.mjs` avec Playwright et Chrome (`--no-sandbox`).

## Limites

- Une image du fichier Drive n'est retirée que si sa licence sort de la liste blanche ou si l'EXIF/XMP porte un marqueur patient. L'absence d'âge ou de sexe est signalée sur la carte ; le cliché reste, car ce n'est pas un champ du JSON source.
- Aucune inscription incrustée n'a été lue par OCR.
- Une normale locale n'est ajoutée que si la licence, l'âge, le sexe et l'auteur sont là, si le cliché est adulte, si la modalité est compatible et si l'écart d'âge connu ne dépasse pas 15 ans. IMG-158 a été refusée : 15 ans, `adulte` = non.
- Les contours locaux ne sont dessinés que sur les mêmes octets. IMG-159 et IMG-257 portent des couches sur la normale ajoutée. IMG-157 est ajoutée sans contour. Aucun contour de lésion du manifeste ne coïncidait avec le cliché du fichier : les repères du fichier sont conservés, et la bande est un cercle pointillé autour de la pointe quand il n'y a pas de polygone.
- Le texte des cartes condense les champs du fichier. Il n'ajoute pas de source nouvelle. Un aspect sans source lue porte « Interprétation de l'image (non sourcée) ».
