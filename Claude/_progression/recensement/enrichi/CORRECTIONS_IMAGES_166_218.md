# Corrections des images IMG-166 à IMG-218 après l'audit du 14.11.2026

Toutes les corrections ont été appliquées. Chaque copie `_verif` a été régénérée par le script, puis regardée.

## Critiques
- **167** : le repère 2 (thrombus de la VCI) passe en (47 ; 47) et vise la VCI, plus l'aorte.
- **199** : l'image PMC3629169, sous licence CC BY-NC, est retirée. Elle est remplacée par PMC13387274 fig. 1 (TDM coronale d'une GIST gastrique, CC BY), avec un repère sur la masse. Le repère des métastases hépatiques est supprimé.
- **201** : la figure postopératoire est retirée. Elle est remplacée par PMC8216704 fig. 1 (pneumopéritoine bilatéral étendu, CC BY), avec deux repères aux pointes des flèches bleues. Le mot « debout » est retiré de `technique`.

## Majeurs
- **Normaux 167, 172, 184, 185, 186, 189, 212, 215 et 218** : le normal est désormais PMC9006245 fig. 2 (TDM portale ; foie, rate et pancréas normaux). Les flèches rouges des auteurs restent sur le pancréas normal, car elles le recouvrent et un recadrage l'aurait amputé ; elles sont déclarées dans `technique`. Pour 212 et 218, `technique` précise « niveau de coupe différent ».
- **Normal 169** : le normal est celui d'IMG-173 (PMC9434024 ; foie et rate normaux).
- **Repères** :
  - 169 : repère 1 en (15 ; 54) ;
  - 212 : repère 1 en (55 ; 16) ;
  - 217 : repère 1 en (37 ; 92), et `technique` signale que l'examen est injecté alors que la référence se fait sans injection ;
  - 218 : repères en (24 ; 67) et (75 ; 67), sur le néphrogramme strié.
- **178** : le situs inversus totalis est déclaré dans `technique`. Aucun remplaçant libre et lisible n'était disponible, car la fig. 4 de PMC8958046 ne figure pas parmi les candidats.

## Mineurs
- **196** : le normal est recadré pour retirer la bande de texte des auteurs.
- **203** : `semio` précise « cause médicamenteuse ; aspect identique à la colectasie de la RCH ».
- **215** : `technique` mentionne la FRP associée à un lymphome.
- **170** : `technique` précise qu'il s'agit d'une hépatopathie de Fontan.
- **213** : `semio` précise « non étranglée sur ce cliché ».
- **195** : `technique` du normal précise « niveau de coupe différent ».
- **182** : `technique` précise que l'atrésie des voies biliaires reste à illustrer.
- **205** et **214** : le contexte est ajouté à `technique` (invagination sur lymphome ; hématome après arthrodèse lombaire).

## Contrôle final
- `enrichi/AB.json` est un JSON valide et `python3 generer.py` passe.
- Toutes les licences retenues sont des CC BY.
- 201 normal : le fichier img/IMG-105_normal.jpg a disparu du dépôt, mais la copie déjà faite dans img/IMG-201_normal.jpg est conservée avec son crédit.
