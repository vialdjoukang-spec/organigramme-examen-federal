# Audit radiologique des images IMG-042 à IMG-165 (14.11.2026)

Objet : champ `images` de `enrichi/TC_RA.json` et `enrichi/TH.json`. Audit indépendant, skill radiologue-expert.
Méthode : chaque copie `_verif/IMG-xxx.png` regardée ; image brute agrandie en cas de doute (064, 086, 098, 102, 140, 143) ; légende et licence de chaque article relues dans le texte intégral Europe PMC (XML) ; doublons cherchés par empreinte md5.
Hors champ, sans image (`manque`) : 062, 088, 097, 124, 142, 150, 161.

**Verdict : corrections requises** (4 critiques, 12 majeurs).

## 1. Critiques : l'image enseigne une erreur

| id | Défaut constaté | PATCH exact |
|---|---|---|
| 105 Pneumonie communautaire | PMC8683236 fig. 1 : la légende et le texte décrivent une opacité en coin (bosse de Hampton), soit un **infarctus pulmonaire septique** sur endocardite tricuspide, et non une pneumonie. | Retirer `patho` → `"manque": "cliché précédent = infarctus septique (PMC8683236), pas une pneumonie"`. Option de remplacement : PMC4735240 fig. 1 (condensation basale droite avec bronchogramme aérique, CC BY 4.0) ; il faut alors réécrire `technique` en « TDM thoracique ». |
| 119 PINS des connectivites | PMC4182847 : **pneumocystose** chez une patiente atteinte de PR et traitée par abatacept (la légende ajoute « aspect de PINS »). Coupe apicale, alors que la PINS prédomine aux bases avec épargne sous-pleurale. L'en-tête porte le nom de l'hôpital et la date. | Retirer `patho` → `"manque"`. Ne pas réutiliser cette image comme PINS. |
| 095 Scoliose idiopathique | PMC4929096 : la scoliose de 95° est **associée à une malformation de Chiari I et à une syringomyélie C6-T7**. Le texte « étiologie non précisée » est faux. | Option 1 : retrait → `manque`. Option 2 : `technique` = « … scoliose thoracique droite de 95° associée à une malformation de Chiari I et à une syringomyélie C6-T7 (donc non idiopathique) » ; `semio` + « ; une scoliose atypique impose une IRM à la recherche d'une syringomyélie ». |
| 149 Insuffisance cardiaque et CMH | PMC3039626 : il s'agit d'une **maladie de Fabry**, et non d'une CMH sarcomérique. | `technique` + « : maladie de Fabry » ; `lesion` = « rehaussement tardif de la paroi latérale (maladie de Fabry) » ; `semio` = « La paroi latérale d'un VG hypertrophique prend le gadolinium, ce qui, dans la maladie de Fabry, touche typiquement le segment basal inféro-latéral et distingue cette phénocopie d'une CMH sarcomérique. » |

## 2. Majeurs

| id | Défaut constaté | PATCH exact |
|---|---|---|
| 050 (paire signalée) | Le normal est en T2 (fig. 4A de PMC10225563), alors que le panneau **4B du même article montre un T1 avec injection normal**. | `normal.technique` = « IRM orbitaire, T1 axial après gadolinium (panneau B) : nerfs optiques sans rehaussement » ; recadrer le panneau B. |
| 064 (paire signalée) | Repère 1 (45 ; 51) posé dans la **colonne d'air oropharyngée**. La flèche des auteurs vise (≈ 48 ; 57). Le cliché est très sombre. Le normal est une photo d'écran où la mandibule se superpose (rachis de SPA). | Repère 1 : x = 48, y = 57. Ajouter dans `technique` : « signe du pouce peu contrasté ». Remplacer le normal dès qu'un profil cervical libre plus net est trouvé. |
| 086 Spondylolyse | La seule tête de flèche visible désigne la **lyse isthmique** selon la légende (fig. 6). La mention « la supérieure… hors sujet » est fausse sur le recadrage. Le « grade 2 de Meyerding » n'est pas sourcé. La lyse n'a aucun repère. | `technique` = « … tête de flèche noire des auteurs : lyse isthmique bilatérale (mère hétérozygote MPS) » ; `semio` : remplacer « de grade 2… (25 à 50 %) » par « (grade non précisé par les auteurs) » ; ajouter un repère 2 « lyse isthmique » à (70 ; 66), à contrôler sur le rendu. |
| 102 Tumeurs intramédullaires | Repère 1 (45,5 ; 30) posé sur la jonction bulbo-médullaire, **sans nodule rehaussé**. Les nodules intramédullaires siègent plus bas. | Repère 1 : x = 43,5, y = 47,5 (fx 12, fy 40). |
| 112 Dépistage TDM faible dose | **Image et coordonnées identiques à 110** (même md5). Lung-RADS est une source américaine seule. | Option 1 : remplacer par un autre cas de dépistage. Option 2 : `technique` + « (même cas que IMG-110) » ; `semio` + référence européenne (position EUPS 2017, volumétrie NELSON) à côté de Lung-RADS. |
| 122 OAP cardiogénique | Repère 2 « cardiomégalie » posé (74 ; 62) sur une **électrode ECG**. | Repère 2 sur le bord gauche de la silhouette cardiaque, ≈ (84 ; 74), à contrôler sur `_verif`. |
| 140 Boerhaave | Repère 1 (51 ; 47) dans la **bulle d'air** du pneumomédiastin, et non sur la fuite de contraste. | Repère 1 : x = 55, y = 50. |
| 153 (exemple signalé) | Le normal est un **nourrisson de 13 mois** porteur d'une sténose trachéale congénitale (PMC9978948). Il n'est pas comparable au patho adulte. | Normal = `img/IMG-123_normal.jpg` (PMC2700481 fig. 1 : RX AP normale d'un adulte de soins intensifs, CC BY), avec la `technique` qui l'accompagne. |
| 158 Aortite FDG | Repère 1 (36 ; 30) posé sur la **queue** de la flèche noire. La crosse fixante est à sa pointe. | Repère 1 : x = 48, y = 31. |
| 164 (exemple signalé) | La coupe montre **une seule fracture costale** et un hémopneumothorax. Elle ne montre pas de volet. L'examen est sans injection, alors que le gold indique « avec injection ». | Patho = PMC4175749 fig. 13a (TDM coronale en fenêtre osseuse, volet de 4 fractures sur 3 arcs consécutifs, CC BY 3.0). À défaut : `semio` + « fracture isolée sur cette coupe ; le volet exige ≥ 3 côtes consécutives fracturées en 2 points ». |
| 154 Dissection | Le voile n'est pas lisible au point visé. La flèche des auteurs désigne la **dilatation anévrismale**. | Option 1 : patho = PMC6100680 fig. 1 (type A, voile net, CC BY 4.0). Option 2 : `lesion` = « dilatation de l'aorte ascendante disséquée ». |
| 116 Pneumoconioses | Repère 2 « fibrose sous-pleurale » posé sur une **plaque calcifiée** gauche. | `lesion` = « plaque pleurale calcifiée » ; `semio` = « Une plaque pariétale calcifiée borde aussi la plèvre gauche, ce qui confirme l'atteinte bilatérale. » |

## 3. Mineurs

| id | Défaut constaté → PATCH |
|---|---|
| 085 | Licence notée « CC BY-SA 4.0 », alors que la source (PMC12554187) est en **CC BY 4.0** → `licence` = « CC BY 4.0 ». |
| 106 | Repère 1 posé dans la condensation ; la tête de flèche des auteurs (arbre en bourgeons) vise ≈ (25 ; 55) → repère 1 : x = 25, y = 55. |
| 135 | La pointe du repère touche l'interface poumon-épanchement, et non le niveau liquide-liquide → abaisser à ≈ (30 ; 82), à contrôler. |
| 091 | La pointe touche le bord médullaire → la décaler de 3 % vers l'arrière, dans la collection. |
| 078 (paire signalée) | « sacculaire » n'est pas sourcé : la fig. 3 dit seulement « giant aneurysm » → `semio` : retirer « sacculaire ». La différence de technique entre TOF et ASN est déclarée. |
| 072, 081, 085, 096, 098, 100, 103 (paires signalées) | Repères corrects, vérifiés (098 et 096 agrandis). Les différences de séquence ou de segment sont déclarées. Aucun patch. |
| 070 | Patient atteint de NEM 1 (souvent une hyperplasie multiglandulaire) ; cliché planaire unique → `semio` : remplacer « persistante » par « focale » et ajouter « (contexte de NEM 1) ». |
| 073 | Aucun calcul n'est montré pour « sialolithiase » → garder, mais chercher une image de lithiase. |
| 067 | Nodule de 4,8 mm selon la légende → `semio` + « < 10 mm : pas de cytoponction en EU-TIRADS 5 ». |
| 049 | « comprime l'apex » n'est pas visible sur cette coupe mi-orbitaire → « peut comprimer le nerf optique à l'apex ». |
| 136 | La fig. 2 montre l'épaississement **résiduel après traitement** → le préciser dans `technique`. |
| 163, 155, 156, 133, 130 | Préciser le contexte : abcès sur mastite granulomateuse ; anévrisme de Takayasu ; enfant de 9 ans ; enfant ; nouveau-né infecté par la COVID. |
| 108 | Le niveau hydro-aérique n'est pas visible : la légende dit seulement « abscess » → `lesion` = « cavité à paroi épaisse ». |
| Série TH | Un normal TDM « crosse aortique » sert 19 fois, même pour des pathos basaux (107, 109, 115, 117, 120, 128, 129, 164) : le niveau de coupe n'est pas comparable. |

## 4. Contrôles sans défaut

042-048, 051-061, 063, 065, 066, 068, 069, 071, 074-077, 079, 080, 082-084, 087, 089, 090, 092-094, 099, 101, 104, 107, 109-111, 113, 114, 117, 118, 120, 121, 123, 125-129, 131, 132, 134, 137-139, 141, 143-148, 151, 152, 157, 159, 160, 162, 165.

Licences : toutes les sources sont en CC BY 2.0, 3.0 ou 4.0, vérifiées dans le XML Europe PMC. Le crédit est présent partout. Seule erreur d'étiquette : 085.
