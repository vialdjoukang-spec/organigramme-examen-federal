# Audit radiologique des images IMG-219 à IMG-237 (AB.json), 14.11.2026

Méthode : chaque copie `_verif/IMG-xxx.png` a été regardée ; l'image brute de 225 a été agrandie sur une grille de coordonnées. Légende et licence de chaque article relues dans le XML Europe PMC.
Sans image (`manque`) : 229, 236.

**Verdict : corrections requises** (0 critique, 3 majeurs).

## 1. Points à juger en priorité

| id | Jugement | Gravité | PATCH exact |
|---|---|---|---|
| 221 Kystes rénaux (Bosniak 2019) | L'image n'enseigne pas d'erreur. Le texte décrit honnêtement un « kyste d'aspect simple », et la légende de PMC5450333 fig. 5 dit seulement « renal cyst ». Elle n'illustre pourtant pas ce que l'entité doit apprendre : il n'y a ni cloison, ni paroi épaisse, ni nodule rehaussé. Le classement Bosniak I est en outre invérifiable sur une seule phase injectée (« +C »), sans densité mesurée. | majeur | `lesion` = « kyste d'aspect simple (Bosniak I présumé) » ; `semio` = « Une formation ronde, homogène, de densité liquidienne et à paroi fine siège dans le rein droit ; le classement Bosniak I exige une densité de −9 à 20 UH sans injection et l'absence de rehaussement, invérifiables sur cette seule phase injectée. » Ajouter au champ `images` : `"a_chercher": "kyste complexe Bosniak IIF à IV en TDM multiphasique (cloisons épaisses, nodule rehaussé)"`. |
| 237 Ischémie mésentérique chronique | Le diagnostic illustré est juste : un syndrome du ligament arqué médian (« celiac artery stenosis due to overlying median arcuate ligament with post-stenotic dilation »), le repère étant posé sur l'ostium cœliaque. Le texte le déclare comme cause rare, distincte de l'athérome. En revanche, la forme typique (sténoses athéromateuses calcifiées d'au moins 2 troncs, tronc cœliaque et AMS) n'est jamais montrée. Le seul cliché enseigne ainsi l'exception à la place de la règle. | majeur | Garder l'image, avec `technique` + « forme non athéromateuse ; l'ischémie mésentérique chronique typique associe des sténoses athéromateuses ostiales d'au moins 2 troncs digestifs ». Ajouter au champ `images` : `"a_chercher": "angio-TDM sagittale : sténoses athéromateuses calcifiées ostiales du tronc cœliaque et de l'AMS"`. |
| 225 Phéochromocytome | Le normal sans injection face au patho injecté est déclaré. La comparaison porte sur la taille et la forme de la surrénale, ce qui reste valable. Le défaut n'est donc pas bloquant. En agrandissant l'image, on voit que la pointe du repère (30 ; 57) touche le bord latéral de la masse. Le cliché, teinté de cyan, est peu contrasté. | mineur | Repère 1 : x = 33, y = 54. Ajouter dans `technique` : « photographie d'écran teintée ». Remplacer le normal par une TDM injectée normale des surrénales dès qu'une source libre se présente. |
| 233 Greffon rénal | Le normal est un rein natif adulte (PMC4808817 fig. 4 : pics systoliques aigus, IR 0,60), ce qui est déclaré. Le patho est un greffon en FID (PMC12602614 fig. 2 : « tardus parvus… decreased resistive index (0.58) ») et le repère est posé sur le pic arrondi. Le seul écart est la nature du rein (natif contre greffon), qui ne change pas la sémiologie de l'onde. | mineur | `semio` + « (la légende retient un IR abaissé à 0,58 et une onde tardus-parvus dans les artères segmentaires du pôle supérieur) ». |

## 2. Autre majeur

| id | Défaut constaté | PATCH exact |
|---|---|---|
| 235 AAA | L'article décrit une **rupture constituée** (« AAA rupture », anémie aiguë). La large plage tissulaire qui entoure l'aorte est un hématome rétropéritonéal, alors que la `semio` du repère 2 dit « rupture imminente ». La mesure de 51,5 mm porte sur la **lumière opacifiée**, alors que le diamètre d'un AAA se mesure paroi externe à paroi externe. | Repère 2 : `semio` = « Un croissant de haute densité dans la paroi signe la fissuration de l'anévrisme. » Ajouter un repère 3 « hématome rétropéritonéal » en (65 ; 45), à contrôler sur `_verif`, avec `semio` = « Une infiltration hématique entoure l'aorte et efface la graisse, ce qui signe la rupture. » Repère 1 : `semio` = « La lumière opacifiée mesure 51 mm ; le diamètre de l'anévrisme se mesure paroi externe à paroi externe, ici plus grand. » |

## 3. Mineurs

| id | Défaut constaté → PATCH |
|---|---|
| 224 | La patiente a un **syndrome de Cushing** : c'est un adénome sécrétant, pas un incidentalome fortuit. La densité n'est pas donnée par les auteurs → `technique` + « adénome cortisolique (contexte de Cushing) ; densité non précisée ; l'incidentalome bénin se définit par une densité ≤ 10 UH sans injection ». |
| 226 | Les sténoses rénales viennent d'une artérite de **Takayasu**, et non de l'athérome. C'est déclaré dans `technique` → `semio` + « (cause inflammatoire ; la sténose athéromateuse, plus fréquente, est ostiale chez le sujet âgé) ». |
| 228 | Le patho vient d'un **enfant** dont l'hydronéphrose accompagne un abcès rétropéritonéal (PMC8260211), alors que le normal est un rein adulte → déclarer l'âge et le contexte dans `technique`. |
| 220 | Une seule phase injectée est montrée, alors que la référence est multiphasique → `technique` + « phase unique ; le rehaussement > 20 UH se démontre en comparant avec la phase sans injection ». |
| 237 normal | Le normal vient d'un patient revu après la décompression d'un pneumopéritoine compressif. C'est déclaré et la légende dit « return to normal opacification » : acceptable. |

## 4. Contrôles sans défaut

219, 222 (TDM sans injection et lésions graisseuses bilatérales vérifiées dans la légende), 223, 227, 230, 231, 232 (grade IV AAST chez un enfant de 9 ans, vérifié), 234.

Licences : CC BY 2.0, 3.0 ou 4.0 dans le XML de chaque source. Le crédit est présent partout.
