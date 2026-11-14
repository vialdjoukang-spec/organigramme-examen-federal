# Corrections des tracés EXP-001 à EXP-051 (suite à AUDIT_TRACES_001_051.md), 14.11.2026

Seul le champ `traces` de `EXP_a.json` a changé. J'ai régénéré les copies `_verif` et regardé celles de 008, 042, 049 et 050 ; `generer.py` est passé.

## Majeurs

| id | Correction appliquée |
|---|---|
| 008 | Repère 2 : `lesion` = « P100 d'un témoin malade à 120,9 ms (déjà allongée) » ; `semio` = « Ce témoin n'est pas normal : la comparaison se fait avec le tracé normal (P100 ≈ 100 ms). » Le normal reste le PEV Wikimedia (P100 ≈ 100 ms). |
| 049 | Option 2 : recadrage sur le seul panneau A (0–47 % de la largeur ; plus aucune bande des panneaux B et C). La `technique` porte « dissociation P/QRS non lisible sur ce monitorage ; diagnostic selon la légende des auteurs ». L'ancien repère 1, invérifiable, est supprimé ; le repère « échappement lent à 41/min » est gardé et renuméroté 1. Les candidats ne contiennent pas d'ECG 12 dérivations avec ondes P dissociées lisibles. |

## Cause déclarée (textes ajoutés)

| id | Ajout |
|---|---|
| 004 | `semio` du repère 1 : « (les LPD ne sont pas spécifiques : elles orientent, la PCR HSV du LCR confirme) » |
| 013 | Jugé acceptable par l'audit ; aucun changement de texte. Repères recentrés lors de la vérification initiale : liquide sous-rétinien sur l'étoile, NVC sur la flèche. |
| 014 | `technique` : « l'OMD diabétique se reconnaît au contexte : exsudats, microanévrismes, pas de NVC » |
| 025 | `semio` du repère 1 : « dans la névrite, le vHIT est pathologique d'un seul côté, et un vHIT normal devant un vertige aigu fait craindre un AVC (HINTS) » |
| 030 | `technique` des deux clichés : « image fixe : l'immobilité se juge en phonation et en inspiration » ; normal déclaré « un mois après traitement d'une atteinte infectieuse » |
| 033 | `semio` du repère 1 : « dans la polyneuropathie axonale diabétique, l'atteinte est longueur-dépendante : sural aboli, membres supérieurs longtemps préservés » |

## Mineurs

| id | Correction |
|---|---|
| 003 | `technique` + « (même source que EXP-153) » |
| 006 | `traces.a_chercher.patho` = hypsarythmie du syndrome de West, non illustrée |
| 027 | `semio` du repère 1 + « l'ototoxicité touche d'abord les fréquences > 8 kHz, d'où l'audiométrie étendue » |
| 042 | Repère 2 → (55 ; 29), sur la courbe rouge de FC (vérifié sur le rendu) |
| 050 | Repère 2 → (88 ; 64), sur le complexe de V6 (vérifié sur le rendu ; le point (92 ; 66) proposé tombait sur la ligne de base) |
| 051 | `semio` du repère 1 + « la maladie du sinus se prouve par des pauses récidivantes hors cause réflexe » |
| 045–051 | `technique` du normal : « rythme sinusal restauré par digoxine après réduction d'une fibrillation auriculaire » |
