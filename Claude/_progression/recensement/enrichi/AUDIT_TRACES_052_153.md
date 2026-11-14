# Audit des tracés EXP-052 à EXP-153 (EXP_b.json, EXP_c.json), 14.11.2026

Méthode : les 43 copies `_verif` porteuses d'un tracé ont été regardées par planches de 2 ou 3. Légendes et licences relues dans le XML Europe PMC ; pour 087 et 089, le fichier Wikimedia est en CC BY-SA 3.0. Les autres identifiants sont soit en `manque`, soit sans tracé (champ `traces` vide).

**Verdict : corrections requises** (0 critique, 1 majeur).

## 1. Majeur

| id | Défaut constaté | PATCH exact |
|---|---|---|
| 103 Hyperactivité détrusorienne | Le repère 3 « débit de fuite pendant l'onde » (35 ; 10) pointe la courbe de débit Q, qui reste **plate** à cet endroit. Le débit n'apparaît qu'en fin de tracé, à la miction. Le repère montre donc une fuite qui n'existe pas. | Supprimer le repère 3. Si une fuite doit être montrée, chercher un autre tracé. Dans la `semio` du repère 1, ajouter « (aucune fuite n'est enregistrée pendant cette onde) ». |

## 2. Question posée : l'ECG normal commun (PMC3038953, fig. 2)

**Acceptable.** La légende dit « normal sinus rhythm restored to 65 bpm after a dose of digoxin ; PR 129 ms, QRS 100 ms, QTc 398 ms ». Sur le rendu, le rythme est sinusal, les intervalles sont normaux, et je ne vois ni cupule digitalique du ST, ni onde f résiduelle. Aucune identité n'apparaît (le cartouche est vierge). Seul défaut, mineur : ce contexte n'est pas déclaré. Pour 052, 053, 055, 057, 058, 065, 068 et 069, ajouter dans `technique` : « après réduction d'une FA par digoxine chez un adolescent sain (fig. 2) ».

## 3. Mineurs

| id | Défaut constaté → PATCH |
|---|---|
| 052 / 152 | Le **même** tracé patho (PMC10244670, fig. 2A) sert aux deux entités → ajouter « (même tracé que EXP-152) » dans la `technique` de 052, et l'inverse pour 152. Le repère 3 de 152 (« bradycardie ») pointe une ligne isoélectrique → le placer sur l'espace RR de D2, x = 30, y = 40. |
| 152 normal | Le cliché garde les panneaux B et C (échocardiographie : septum discrètement épaissi, FEVG légèrement abaissée) → recadrer sur le panneau A (ECG). |
| 102 | La légende donne un Qmax de **7 ml/s** → `lesion` = « Qmax abaissé à 7 ml/s ». |
| 061 normal | « LVDd 43 mm » vient de PMC9120596, où la fig. 2B montre un VG **dilaté** (cas 1) ; ce panneau est probablement la fig. 4B, après transplantation. Préciser le panneau et le contexte dans `technique`, sinon remplacer le normal. |
| 105 | Le patho est un **schéma** et non un tracé réel (déclaré) → garder, mais ajouter dans `a_chercher` une cystomanométrie avec EMG réelle. |
| 106 | Le patho reprend les panneaux sains A à côté des panneaux B → acceptable. Préciser dans `technique` : « panneaux A sains, B pathologiques ». |
| 127 | Normal recueilli sur le tibial antérieur, patho sur le court extenseur des orteils : muscles différents → le déclarer. |
| 129 | La pointe du repère 2 « apnée centrale » est sur le pic d'un cycle et non dans l'intervalle → x = 24, y = 26. |
| 153 | Le patho vient d'un **enfant** (encéphalopathie au cours d'un Kawasaki), et non d'un delirium de l'adulte → déclarer l'âge et le contexte dans `technique`. |
| 066 | Le normal est un panneau de Wasserman en 9 graphiques, le patho une courbe temporelle : formats non comparables (déclaré) → acceptable. |
| 116 normal | Quelques anses sont tortueuses ou croisées (aspect normal variant, 8/mm selon la légende) → acceptable. |

## 4. Identité, licences, contrôles sans défaut

- Identité : aucune n'est visible. Le cartouche de 068 est masqué par les auteurs ; 123 ne montre que la date de l'appareil.
- Licences : toutes CC BY (2.0 à 4.0) dans le XML, aucune NC ; 087 et 089 sont en CC BY-SA 3.0 (Wikimedia).
- Tracés conformes à l'anomalie annoncée, repères justes : 053, 054, 055, 056, 057, 058, 060, 062, 063, 065, 067, 068, 069, 087, 088, 089, 090, 107, 108, 109, 111, 112, 115, 118, 123, 128, 130, 131, 132, 133, 151.

## Clôture
Majeur 103 (repère « fuite » retiré) et mineurs appliqués par les deux correcteurs (CORRECTIONS_TRACES_052_102.md, _103_153.md) ; 152 passé en manque : **audit-ok** pour les tracés EXP-052 à 153.
