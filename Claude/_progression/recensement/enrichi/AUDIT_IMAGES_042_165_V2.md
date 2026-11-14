# Audit radiologique V2 : vérification des corrections IMG-042 à IMG-165 (14.11.2026)

Méthode : lecture de `CORRECTIONS_IMAGES_042_104.md` et `CORRECTIONS_IMAGES_105_165.md`, des champs `images` du JSON et des copies `_verif` régénérées. Les rendus de 064 et 135 ont été agrandis. Les légendes de 064 (PMC12906715) et de 086 (PMC4985337) ont été relues dans le XML Europe PMC. Une empreinte md5 a été calculée pour 153.

**Verdict : corrections requises.** Il reste deux patchs de texte mineurs (§ 3). Tous les critiques et majeurs de V1 sont corrigés.

## 1. Critiques de V1

| id | Contrôle | Statut |
|---|---|---|
| 105 | `images.manque` motivé ; plus d'image ni de `_verif` | corrigé |
| 119 | `images.manque` motivé ; plus d'image ni de `_verif` | corrigé |
| 095 | La `technique` précise désormais « Chiari I + syringomyélie C6-T7, donc non idiopathique ». La `semio` renvoie à l'IRM. | corrigé (ponctuation : § 3) |
| 149 | La maladie de Fabry est nommée dans `technique`, `lesion` et `semio`. Le texte parle de phénocopie et non plus de CMH. | corrigé |

## 2. Majeurs de V1

| id | Contrôle sur le rendu | Statut |
|---|---|---|
| 050 | Le normal est le T1 coronal injecté (panneau B, même article) : nerfs non rehaussés. La différence de plan est déclarée. | corrigé |
| 064 | Le patho est remplacé par PMC12906715 fig. 1 (« thumbprint sign », CC BY 4.0). Sur l'agrandissement, le repère 1 (59 ; 54) tombe sur l'opacité arrondie de l'épiglotte, juste à gauche de la flèche des auteurs. | corrigé |
| 086 | J'ai relu la légende : l'image est la **fig. 7 (le père)**, et non la fig. 6. La légende nomme un « grade 2 spondylolisthesis… congenital abnormality of the facets and the pars ». Le grade est donc sourcé, et aucune lyse n'est désignée sur ce cliché. **Mon patch V1 était erroné ; le correcteur a raison** de garder le grade et de refuser le repère « lyse ». La `semio` renvoie aux obliques et à la TDM. | accepté |
| 102 | Le repère 1 (43,5 ; 47,5) touche un nodule rehaussé de la moelle cervicale. | corrigé |
| 112 | « (même cas que IMG-110) » est ajouté. NELSON et EUPS 2017 sont cités à côté de Lung-RADS. | corrigé |
| 116 | Le repère 2 est renommé « plaque pleurale calcifiée ». | corrigé |
| 122 | Le repère 2 (70 ; 74) se trouve dans la silhouette cardiaque élargie et non plus sur l'électrode. | corrigé |
| 135 | Sur l'agrandissement, le repère (27 ; 74) se trouve sur l'interface oblique entre les deux couches de l'épanchement déclive. | corrigé |
| 140 | Le repère 1 (55 ; 50) touche la fuite de contraste désignée par la flèche noire. Le repère 2 se trouve dans l'air péri-œsophagien. | corrigé |
| 153 | Le normal est identique, au md5 près, à `IMG-123_normal.jpg` (PMC2700481 fig. 1, adulte de soins intensifs). Le nourrisson est retiré. | corrigé |
| 154 | `lesion` = « dilatation de l'aorte ascendante disséquée ». Le texte ne prétend plus montrer le voile. | corrigé |
| 158 | Le repère 1 (48 ; 31) se trouve à la pointe de la flèche noire, sur la crosse fixante. | corrigé |
| 164 | `images.manque` ; plus d'image ni de `_verif`. | corrigé (texte : § 3) |

Les mineurs de V1 relus dans le JSON sont appliqués : 085 (CC BY 4.0), 091, 078, 070, 067, 049, 073, 106, 108, 136, 130, 133, 155, 156, 163, et la mention du niveau de coupe dans la série TH.

## 3. Patchs restants (mineurs)

| id | Défaut | PATCH exact |
|---|---|---|
| 164 `images.manque` | La définition est ambiguë : « ≥ 2 fractures sur ≥ 3 côtes contiguës » peut se lire comme 2 fractures au total. Par ailleurs, « aucune image libre » est faux : PMC4175749 fig. 13a (TDM coronale en fenêtre osseuse, volet de 4 fractures sur 3 arcs consécutifs) est sous CC BY 3.0. Elle n'est simplement pas dans les candidats. | `manque` = « Aucune image retenue ne montre un volet costal (≥ 3 côtes contiguës fracturées chacune en ≥ 2 points) ; candidate libre à intégrer : PMC4175749 fig. 13a (CC BY 3.0). La candidate précédente montrait une fracture isolée (audit images 14.11.2026). » |
| 095 `semio` | La ponctuation est doublée : « … plus inclinées. ; une scoliose… ». | Remplacer « inclinées. ; une scoliose » par « inclinées ; une scoliose ». |

Une fois ces deux remplacements appliqués, le verdict passe à **audit-ok** sans nouvelle relecture d'image.

## Clôture
Les 2 patchs restants (164 manque réécrit, 095 ponctuation) ont été appliqués mot pour mot : **audit-ok** pour les images IMG-042 à 165.
