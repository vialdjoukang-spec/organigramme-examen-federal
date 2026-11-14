# Audit radiologique des images IMG-166 à IMG-218 (AB.json), 14.11.2026

Méthode :
- chaque copie `_verif/IMG-xxx.png` a été regardée ; les images brutes de 167 et 169 ont été agrandies sur une grille de coordonnées ;
- la légende et la licence de chaque article ont été relues dans le XML Europe PMC (licence de 183 et 176 contrôlée par l'API Europe PMC, légende de 183 relue dans BioC) ;
- les candidats de remplacement ont été vérifiés dans `outils_images/candidats/`.

Sans image (`manque`) : 174, 198, 206.

**Verdict : corrections requises** (3 critiques, 9 majeurs).

## 1. Critiques

| id | Défaut constaté | PATCH exact |
|---|---|---|
| 167 CHC | Agrandi : le repère 2 « thrombus de la VCI » (56 ; 50) tombe sur l'**aorte**, ronde et opacifiée, à gauche du rachis. La longue flèche jaune des auteurs vise la VCI hypodense (fig. 9 de PMC3748773 : « central filling defect in the IVC »). | Repère 2 : x = 47, y = 47 (fx 72, fy 18). |
| 199 GIST | Le JSON indique une licence « CC BY », mais le XML de PMC3629169 (Oncol Lett, Spandidos) porte **CC BY-NC 3.0**, licence non libre au sens du schéma. | Remplacer le patho par PMC13387274 fig. 1 (TDM coronale d'une GIST gastrique, CC BY) ou PMC8341026 fig. 1 (masse gastrique exophytique, CC BY), tous deux dans les candidats. À défaut : `images.manque`. |
| 201 Pneumopéritoine | L'image est la **fig. 3** de PMC5325505 (`g003` des candidats). Sa légende la décrit comme la radiographie de J1 après la chirurgie, avec une « significant regression of pneumoperitoneum ». Elle est donc présentée à tort comme un pneumopéritoine typique, et le « debout » n'est pas sourcé (patient de réanimation). | Remplacer le patho par PMC8216704 fig. 1 (« extensive pneumoperitoneum, bilateral free intraperitoneal air », CC BY, `candidats/IMG-201/patho_6.jpg`), avec des repères à poser sur les deux croissants sous-diaphragmatiques, aux pointes des flèches bleues, puis à contrôler sur `_verif`. À défaut : `technique` = « Radiographie thoracique de face au lit à J1 postopératoire : pneumopéritoine bilatéral en régression ». |

## 2. Majeurs

| id | Défaut constaté | PATCH exact |
|---|---|---|
| 167, 169, 172 (normaux) | Le normal (PMC9001859 fig. 4) n'est pas normal : patient **porteur d'une anastomose splénorénale**, rate absente, branche porte gauche élargie (les têtes de flèche des auteurs la désignent). Ce cas d'hypertension portale sert de normal à une thrombose porte (172) et à un CHC (167). | 167 et 172 : normal = PMC9006245 fig. 2 (TDM axiale injectée au temps portal, pancréas normal, foie et rate normaux, CC BY 4.0, `candidats/IMG-184/normal_2.jpg`), à recadrer pour retirer les flèches. 169 : normal = `img/IMG-173_normal.jpg` (PMC9434024, foie et rate normaux). |
| 184, 185, 186, 189, 212, 215, 218 (normaux) | Le normal (PMC3529420) montre un **foie stéatosique**, hypodense par rapport à la rate. La légende dit « fatty liver ». Le même cliché sert de normal à 7 pathologies. | Normal = PMC9006245 fig. 2 (voir ci-dessus) pour 184, 185, 186, 189 et 215. Pour 212 et 218 (coupes rénales et péritonéales basses) : même image, avec dans `technique` « niveau de coupe différent ». |
| 169 Abcès | Agrandi : le repère 1 (22 ; 52) tombe à côté d'un vaisseau. La flèche noire des auteurs vise le plus gros abcès, centré vers (15 ; 54). | Repère 1 : x = 15, y = 54 (fx 6, fy 82). |
| 212 Carcinose | Le repère 1 (55 ; 25) touche la paroi aérique du côlon transverse. Le gâteau épiploïque est la bande tissulaire antérieure désignée par la flèche blanche. | Repère 1 : x = 55, y = 16. |
| 217 Lithiase | Le repère 1 « calcul » (35 ; 82) vise la jonction pyélo-urétérale. Le calcul hyperdense (8,7 mm selon la légende) se trouve sous la flèche noire inférieure. L'examen est **injecté**, alors que le gold est une TDM sans injection. | Repère 1 : x = 37, y = 92. `technique` + « (avec injection ; le diagnostic de référence se fait sans injection) ». |
| 218 PNA | Les deux repères (22 ; 55) et (80 ; 55) tombent dans la **graisse périrénale**, et non sur le néphrogramme strié. | Repère 1 : x = 24, y = 67 ; repère 2 : x = 75, y = 67 (à contrôler sur `_verif`). |
| 178 Lithiase de la VBP | PMC13473696 est un cas de **situs inversus** (foie à gauche sur l'image), ce qui n'est pas déclaré. | Remplacer le patho par PMC8958046 fig. 4 (calcul du bas cholédoque, MIP, CC BY, déjà utilisé en 177). À défaut : `technique` + « situs inversus : foie à droite de l'image ». |

## 3. Mineurs

| id | Défaut constaté → PATCH |
|---|---|
| 196 | Le normal porte le texte incrusté des auteurs « Normal small and large bowel on initial CT » → le recadrer pour retirer la bande supérieure. |
| 203 | La colectasie est induite par la clozapine et ne vient pas d'une RCH. C'est déclaré dans `technique` → ajouter dans `semio` « (cause médicamenteuse ; aspect identique à la colectasie de la RCH) ». |
| 215 | La FRP est révélatrice d'un **lymphome** (titre de l'article) → `technique` + « FRP associée à un lymphome ». |
| 170 | L'ascite vient d'une hépatopathie de Fontan, et non d'une cirrhose commune → le préciser dans `technique`. |
| 213 | La hernie d'Amyand n'est pas étranglée → `semio` + « non étranglée sur ce cliché ». |
| 195 | Le normal est une coupe pelvienne basse (vessie), le patho une coupe iliaque → ajouter « niveau de coupe différent ». |
| 182 | Seul le kyste du cholédoque associé à une atrésie duodénale est montré ; l'atrésie biliaire reste à illustrer. |
| 205, 214 | Préciser le contexte : invagination sur lymphome chez l'enfant ; hématome iatrogène après arthrodèse lombaire. |
| 201 (normal) | La RX normale est reprise d'IMG-105 (patient du bilan préopératoire, PMC3996492 fig. 3). La légende confirme « normal » et IMG-105 est désormais en `manque` : la réutilisation est acceptable. |

## 4. Contrôles sans défaut

166, 168, 171, 173, 175, 176, 177, 179, 180, 181, 183, 187, 188, 190 (repère corrigé, juste), 191, 192 (repère corrigé, juste), 193, 194, 197, 200, 202, 204 (4 mm et 26 mm vérifiés dans la légende), 207, 208, 209, 210, 211, 216.
Le repère de 170 (ascite entre le foie et la paroi) est juste.

Licences : CC BY 2.0, 3.0 ou 4.0 vérifiées dans le XML, sauf **199 (CC BY-NC 3.0)**. Le crédit est présent partout.
