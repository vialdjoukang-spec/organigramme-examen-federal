# Audit des tracés EXP-001 à EXP-051 (EXP_a.json), 14.11.2026

Méthode : les 41 copies `_verif` porteuses d'un tracé ont été regardées. Légendes et licences relues dans le XML Europe PMC ; aucune licence NC ni absente.
Sans tracé : 015, 016, 022, 031, 037, 038, 040, 041, 043 (`manque`) et 029 (vide).

**Verdict : corrections requises** (0 critique, 2 majeurs).

## 1. Majeurs

| id | Défaut constaté | PATCH exact |
|---|---|---|
| 008 PEV | Le repère 2 présente comme « P100 de référence » la courbe du **témoin malade** (myélite atopique). Sa P100 est à **120,9 ms**, au-delà de la norme (P100 ≈ 100 ms, limite supérieure ≈ 115 ms selon le laboratoire). Le tracé enseigne donc comme normale une latence allongée. | Repère 2 : `lesion` = « P100 d'un témoin malade à 120,9 ms (déjà allongée) » ; `semio` = « Ce témoin n'est pas normal : la comparaison se fait avec le tracé normal (P100 ≈ 100 ms). » Si une seule courbe pathologique est préférée, recadrer sur la courbe du bas. |
| 049 BAV | Le monitorage DII ne laisse pas voir d'onde P dissociée. Les marques « N » de l'appareil sont posées sur les QRS, et le sus-décalage ST domine le tracé. Le repère 1 « rythme d'échappement sans conduction AV » ne peut donc pas être vérifié à l'œil. De plus, le recadrage laisse visible une bande des panneaux B et C (photos de moniteur). | Option 1 (préférée) : chercher un ECG 12 dérivations de BAV complet avec ondes P dissociées visibles. Option 2 : recadrer sur le seul panneau A et écrire dans `technique` : « dissociation P/QRS non lisible sur ce monitorage ; diagnostic selon la légende des auteurs ». Repère 2 (échappement à 41/min) : garder. |

## 2. Points à juger en priorité (patho d'une autre cause que celle annoncée)

Aucun de ces cas n'enseigne d'erreur, car la cause réelle est chaque fois déclarée et la sémiologie du tracé est la même. Je les classe en mineurs, avec un ajout de texte.

| id | Jugement → PATCH |
|---|---|
| 004 HSV | Les décharges périodiques latéralisées viennent d'un état de mal aphasique non herpétique. La sémiologie est identique, et c'est déclaré → `semio` du repère 1 + « (les LPD ne sont pas spécifiques : elles orientent, la PCR HSV du LCR confirme) ». |
| 013 DMLA | NVC sur stries angioïdes : l'OCT montre bien du liquide sous-rétinien et un NVC → acceptable. |
| 014 OMD | Logettes cystoïdes sur NVC, pas sur diabète → `technique` + « l'OMD diabétique se reconnaît au contexte : exsudats, microanévrismes, pas de NVC ». |
| 025 vHIT | Le patient a un CANVAS, donc une atteinte **bilatérale**, alors que la névrite est unilatérale → `semio` + « dans la névrite, le vHIT est pathologique d'un seul côté ; un vHIT normal devant un vertige aigu fait craindre un AVC (HINTS) ». |
| 030 Récurrent | Le normal est une laryngoscopie « near-normal » après traitement d'une atteinte infectieuse. Le patho montre une paralysie **bilatérale**. Une image fixe ne montre pas l'immobilité → `technique` des deux clichés + « image fixe : l'immobilité se juge en phonation et en inspiration ». |
| 033 PNP axonale | Le syndrome de Miller Fisher n'est pas longueur-dépendant : le potentiel ulnaire est aboli aussi → `semio` + « dans la polyneuropathie axonale diabétique, l'atteinte est longueur-dépendante : sural aboli, membres supérieurs longtemps préservés ». |

## 3. Tracés imparfaits

| id | Jugement → PATCH |
|---|---|
| 003 | EEG d'un **enfant** (encéphalopathie au cours d'un Kawasaki), la même figure que EXP-153. Ralentissement diffus net, sans onde triphasique (déclaré) → ajouter « (même source que EXP-153) ». Mineur. |
| 006 | L'absence à 3 Hz est démonstrative. Le syndrome de West n'est pas illustré, et le normal est un adulte (déclaré) → `a_chercher` : hypsarythmie. Mineur. |
| 027 | Graphique de cohorte, déclaré. La chute sur les hautes fréquences (≥ 8 kHz) est lisible → acceptable. Ajouter dans `semio` du repère 1 : « l'ototoxicité touche d'abord les fréquences > 8 kHz, d'où l'audiométrie étendue ». Mineur. |

## 4. Autres mineurs

| id | Défaut constaté → PATCH |
|---|---|
| 042 | La pointe du repère 2 est dans le vide, au-dessus du tracé de FC → x = 55, y = 29, sur la courbe rouge. |
| 050 | La pointe du repère 2 est sur la ligne de base entre deux complexes de V6 → la placer sur le QRS de V6 (≈ x = 92, y = 66) puis contrôler. |
| 051 | La pause est un réflexe vagal peropératoire et non une maladie du sinus intrinsèque (déclaré) → `semio` + « la maladie du sinus se prouve par des pauses récidivantes hors cause réflexe ». |
| 045 à 051 (normal) | ECG PMC3038953 fig. 2 après réduction d'une FA par digoxine : acceptable (voir AUDIT_TRACES_052_153). Déclarer le contexte. |

## 5. Contrôles sans défaut

001, 002, 005, 007, 009, 010, 011, 012, 017, 018, 019, 020, 021, 023, 024, 026, 028, 032, 034, 035, 036, 039, 044, 045, 046, 047, 048.
Aucune identité visible (vignette vidéo masquée en 001 à 007).
