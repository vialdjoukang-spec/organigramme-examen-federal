# Corrections appliquées après l'audit des images IMG-289 à IMG-344 (MI_TR.json), 14.11.2026

Source : `AUDIT_IMAGES_289_344.md`. J'ai regardé chaque `_verif` après correction. Le JSON est valide et `generer.py` a été relancé.

## Majeurs
| id | Correction |
|---|---|
| 340 | Repère 3 déplacé en (82 ; 34) : métaphyse tibiale proximale, sur le cliché des membres inférieurs, à la pointe de la flèche des auteurs. |
| 326 | Le champ `normal` est supprimé (`img/IMG-326_normal.jpg` effacé). Comme le générateur n'a pas de champ « référence », la figure entière est reprise en patho : A est déclaré « référence avant traitement (0 mois) » dans `technique`, B est le contrôle à 6 mois. Le repère est posé sur le panneau B en (63 ; 81). J'ai ajouté un `manque_normal`. |

## Mineurs
| id | Correction |
|---|---|
| 304 | Repère 1 placé sur le trait de fibula en (30 ; 47). |
| 337 | Ajout dans `technique` : lacération hépatique iatrogène par massage cardiaque ; même lecture chez le polytraumatisé. |
| 325 | Bande de titre recadrée (12 % supérieurs) ; y recalculés selon y' = (y − 12)/0,88. |
| 323 | Ajout dans `technique` : le normal (gastrocnémien) et le patho (poplité) sont deux muscles différents. |
| 329 | Âges déclarés : le normal est un enfant, le patho un adulte. |
| 338 | Repère placé dans l'épanchement latéral au ventricule gauche, en (69 ; 55). Le patch proposait (66 ; 50), mais ce point tombait sur la paroi : il a été ajusté après contrôle. |
| 341 | Justification de radioprotection ajoutée dans `technique`. |
| 327 | Traceur « nommé selon le texte de l'article ». |

Sans changement, comme le jugeait l'audit : 299, 321, 292.
