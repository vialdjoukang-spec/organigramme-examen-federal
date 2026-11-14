# Audit radiologique V2 : vérification des corrections IMG-166 à IMG-218 (14.11.2026)

Méthode :
- lecture de `CORRECTIONS_IMAGES_166_218.md` et des champs `images` de `AB.json` ;
- examen des copies `_verif` régénérées (167, 169, 178, 199, 201, 212, 217, 218) ;
- md5 des normaux, pour contrôler les remplacements ;
- relecture dans le XML Europe PMC de la légende et de la licence des deux nouvelles sources.

**Verdict : corrections requises.** Il reste deux patchs mineurs (§ 3). Les 3 critiques et les 9 majeurs de V1 sont corrigés.

## 1. Critiques de V1

| id | Contrôle | Statut |
|---|---|---|
| 167 | Le repère 2 (47 ; 47) touche la VCI hypodense, à la pointe de la longue flèche jaune des auteurs, et non plus l'aorte. | corrigé |
| 199 | PMC13387274 fig. 1 : la légende dit « large GIST arising from the stomach (white arrow) » et la licence est **CC BY 4.0** (vérifiée dans le XML). L'image CC BY-NC est retirée. | corrigé (pointe du repère : § 3) |
| 201 | PMC8216704 fig. 1 : la légende dit « Extensive pneumoperitoneum, bilateral free intraperitoneal air (blue arrows) » et la licence est **CC BY** (vérifiée dans le XML). Les repères 1 (17 ; 18) et 2 (84 ; 13) sont aux pointes des flèches bleues, sur les coupoles décollées. « debout » est retiré. | corrigé |

## 2. Majeurs de V1

| id | Contrôle | Statut |
|---|---|---|
| Normaux 167, 172, 184-186, 189, 212, 215, 218 | Le md5 est identique pour les 9 fichiers. PMC9006245 fig. 2 montre un pancréas, un foie et une rate normaux ; les flèches rouges des auteurs sont déclarées. Le niveau de coupe différent est déclaré pour 212 et 218. | corrigé |
| Normal 169 | Le md5 est identique à `IMG-173_normal.jpg` (PMC9434024 : foie et rate normaux). | corrigé (texte : § 3) |
| 169 | Le repère 1 (15 ; 54) est au centre de l'abcès, sous la flèche noire. | corrigé |
| 212 | Le repère 1 (55 ; 16) est dans le gâteau épiploïque, sous la flèche blanche. | corrigé |
| 217 | Le repère 1 (37 ; 92) touche le calcul hyperdense, à la pointe de la flèche noire inférieure. L'injection est déclarée. | corrigé |
| 218 | Les repères (24 ; 67) et (75 ; 67) tombent dans le parenchyme rénal et non plus dans la graisse. | corrigé |
| 178 | `technique` déclare le situs inversus totalis et le foie à droite de l'image. | corrigé |

J'ai relu dans le JSON les mineurs de V1 : 196, 203, 215, 170, 213, 195, 182, 205 et 214 sont appliqués.

## 3. Patchs restants (mineurs)

| id | Défaut | PATCH exact |
|---|---|---|
| 169 `normal.technique` | Le texte a été copié depuis PMC9006245 et décrit une autre image : « temps portal… pancréas… flèches rouges des auteurs sur le pancréas normal ». L'image réelle (PMC9434024) est une coupe haute du dôme hépatique, sans flèches et avec des artefacts de bras. | `technique` = « TDM abdominale injectée, coupe axiale haute : foie et rate normaux, sans lésion focale (artefacts de bras) ». |
| 199 repère 1 | La pointe (50 ; 60) touche le bord médial de la masse, au contact du mésentère. | Repère 1 : x = 61, y = 60 (centre de la masse, à gauche de la flèche blanche des auteurs). |

Une fois ces deux remplacements appliqués, le verdict passe à **audit-ok** sans nouvelle relecture d'image.

## Clôture
Les 2 patchs mineurs (169 technique, 199 repère 61 ; 60) ont été appliqués mot pour mot : **audit-ok** pour IMG-166 à 218.
