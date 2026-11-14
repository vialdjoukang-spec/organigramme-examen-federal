# Journal FedMed — fenêtres

Branche `leona/fedmed-fenetres`, créée depuis `origin/main` (`65244131a`). Écriture uniquement dans `imagerie_GROK/fedmed/`. Pas de PR, pas de fusion, pas d’issue.

## État

<!-- ETAT:DEBUT -->
- Découpage fait : 396 fenêtres, dont 132 sans normale. Réinjection brute : octet identique.
- Échantillon capturé : IMG-134, IMG-001, IMG-136, IMG-267, EXP-001, EXP-002, EXP-024, EXP-032, IMG-166, IMG-168.
- Fenêtres fusionnées : 344 / 396.
- Normales ajoutées : 1.
- Signalements : 555. Détail : signaux/images_signalees.json.
- Reprise : python3 imagerie_GROK/fedmed/scripts/fusionner.py --limite 30
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

1. `python3 imagerie_GROK/fedmed/scripts/decouper.py`
2. `python3 imagerie_GROK/fedmed/scripts/test_roundtrip.py`
3. `python3 imagerie_GROK/fedmed/scripts/fusionner.py --limite 10`
4. `python3 imagerie_GROK/fedmed/scripts/reinjecter.py`
5. `python3 imagerie_GROK/fedmed/scripts/capturer.py`

Les scripts sont idempotents. `fusion/etat.json` liste les identifiants déjà écrits. Relancer `fusionner.py` reprend les manquants.
