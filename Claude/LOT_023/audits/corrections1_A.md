# Corrections audit 1 (A) — LOT_023, DX.1 à DX.5

| N° | Fichier | Gravité | Résultat |
|---|---|---|---|
| 1 | DX.1 | Grave, métoclopramide ESO 2021 vs ESO 2026 | fait : divergence écrite (S3), métoclopramide non retenu en prévention |
| 2 | DX.3 | Grave, contre-indications Buscopan | fait : recopiées de l'AIPS 17352 (adénome prostatique, sténoses mécaniques ajoutés) |
| 3 | DX.1 | Grave, repère 3 épiglotte | fait : cercle déplacé à (445, 145), régénéré par cliche.py figure, superposition PIL vérifiée visuellement |
| 4 | DX.3 | Moyen, délai « quatre heures » | fait : remplacé par le délai ESGE 2016 rec. 7 (de préférence 2 h, au plus tard 6 h), vérifié dans le texte ESGE |
| 5 | DX.4 | Moyen, fenêtre « Bouche » | fait : geste et interprétation ajoutés sans appel de source (S1 HUG dyspepsie ne couvre pas l'examen buccal) |
| 6 | DX.4 | Moyen, repère 3 | fait : cercle à (505, 445), régénéré par cliche.py figure, superposition vérifiée visuellement |
| 7 | DX.2 | Moyen, contre-indications Madopar | fait : recopiées de l'AIPS 38096 |
| 8 | DX.2 | Moyen, voies de remplacement sans AIPS | fait : formulation de la correction appliquée |
| 9 | DX.1 | Léger, contre-indications Paspertin | fait : ajouts d'après l'AIPS 32733 |
| 10 | DX.1 | Léger, retournement | fait : « comité d'experts … conseille » |
| 11 | DX.2 | Léger, légende image | fait : attribution française ; S11–S14 renumérotés S10–S13 |
| 12 | DX.3 | Léger, Cochrane | fait : « n'a démontré d'effet supérieur au placebo » |
| 13 | DX.4 | Léger, appels « aips-54380 » | fait : 4 appels affichent S8 ; S8–S10 renumérotés S7–S9 (plus de trou) |
| 14 | DX.5 | Léger, Jorveza | fait : formulation vérifiée dans l'AIPS 66999 |
| 15 | DX.5 | Léger, attribution BSG | fait : BSG [S6] ; AIPS suisse [S15] |

Contrôles : controle3 --script-ok VERT sur les 11 fichiers (80–150 Ko) ; verif_aips OK.
Réserve : le n° 13 de la correction proposait « S9 » ; la renumérotation sans trou donne S8 pour l'AIPS 54380.
