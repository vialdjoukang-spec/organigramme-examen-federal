# Audit radiologique des images IMG-269 à IMG-288 (PE_MS.json), 14.11.2026

Méthode :
- chaque copie `_verif/IMG-xxx.png` a été regardée ;
- l'image brute de 273 a été agrandie ;
- la légende et la licence de chaque article ont été relues dans le XML Europe PMC ; pour les figures Wikimedia (CC0), j'ai relu la mention reportée dans le JSON.

Sans image (`manque`) : 284.

**Verdict : corrections requises** (0 critique, 1 majeur).

## 1. Majeur

| id | Défaut constaté | PATCH exact |
|---|---|---|
| 282 Goutte | La `technique` affirme « pas de signe du double contour sur ce cliché ». La légende de PMC13730182 fig. 9A dit au contraire : « Note the hyperechoic double contour lines at the proximal and distal dorsal interphalangeal joint cartilage (curved arrows) ». Les deux flèches courbes sont visibles sur `_verif`. Le texte nie donc le signe le plus spécifique de la goutte, alors que l'image le montre. | `technique` = « Échographie longitudinale du 5e doigt, homme de 55 ans goutteux : tophus sous-cutanés (têtes de flèche) et signe du double contour (flèches courbes des auteurs) ». Ajouter le repère 2 en (78 ; 55), à contrôler sur `_verif` : `lesion` = « signe du double contour » ; `semio` = « Une ligne hyperéchogène irrégulière double la surface du cartilage articulaire : c'est le dépôt d'urate, très spécifique de la goutte. » |

## 2. Écarts signalés, jugés un à un

| id | Jugement |
|---|---|
| 271 | Le normal est la même épaule de face (PMC8175186). L'absence d'incidence de Zanca et de cliché comparatif est déclarée. La ligne inférieure de la clavicule est comparable : acceptable. |
| 272 | Il n'y a pas de normal, et le profil manque alors que la classification de Gartland se lit sur le profil (déclaré). Mineur → `semio` + « le type de Gartland se confirme sur le profil strict ». |
| 273 | Le normal est un coude gauche de face, le patho un coude droit de face. Agrandi, le repère touche bien le fragment marginal déplacé de la tête radiale. L'image est petite → mineur : agrandir le recadrage (×2) autour du coude. |
| 275 | Le côté sain du même patient (fig. 1, « unaffected / affected side ») est un bon couple comparatif. Le repère est sur le tendon, sous la flèche des auteurs : conforme. |
| 276 | Il n'y a pas de normal ; la nature septique non précisée est déclarée. Le repère 1 est dans la collection anéchogène, le repère 2 sur la synoviale hyperhémique : conforme à la légende de la fig. 2. |
| 288 | Il n'y a pas de normal ; la manœuvre n'est pas précisée (déclaré). Le repère est posé entre les flèches, sur le segment non opacifié : conforme à la légende de la fig. 3C. |

## 3. Mineurs

| id | Défaut constaté → PATCH |
|---|---|
| 269 | Normal en T1/DP sur épaule droite, patho en T2 avec suppression de graisse sur épaule gauche. C'est déclaré → ajouter « côté opposé » dans `technique`. |
| 270 | L'entité couvre aussi la capsulite rétractile, qui n'est pas illustrée. La fig. 8 montre en outre une migration intra-osseuse → `technique` + « migration intra-osseuse de la calcification (IRM du même cas) ». |
| 278 | Normal : enfant de 10 ans, poignet entier. Patho : adulte de 33 ans, coupe centrée sur le scaphoïde. Âges déclarés ; plan identique : acceptable. |
| 281 | La pointe du repère 2 (62 ; 67) tombe sur la base du 1er métacarpien, au-dessus de l'interligne trapézo-métacarpien → x = 61, y = 71. |
| 285 | Le normal vient d'un patient atteint d'un syndrome de Dubowitz, dont l'âge osseux concorde avec l'âge civil (déclaré) : acceptable. |

## 4. Contrôles sans défaut

274 (Bado III, flèches épaisse et fine vérifiées), 277, 279, 280, 283 (21 mm² = 0,208 cm², conforme à l'écran), 286, 287 (409 cm/s, IR 0,33 et suspicion de sténose de la veine de drainage, vérifiés dans la légende).

Licences : CC BY 2.0 à 4.0 dans le XML, et CC0 Wikimedia pour les normaux du coude, du poignet et de la main. Le crédit est présent partout.

## Clôture
282 (technique + repère 2 en 78 ; 55, contrôlé sur _verif) appliqué : **audit-ok** pour IMG-269 à 288.
