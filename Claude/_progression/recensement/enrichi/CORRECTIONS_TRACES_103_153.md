# Corrections des tracés EXP-103 à EXP-153 (EXP_c.json), 14.11.2026

Réponse à `AUDIT_TRACES_052_153.md`. Seul le champ `traces` de `EXP_c.json` a changé. J'ai regardé chaque copie `_verif` concernée après correction.

| id | Défaut signalé | Correction |
|---|---|---|
| 103 (majeur) | Le repère 3 « fuite » pointait une courbe de débit plate. | J'ai supprimé le repère 3. La `semio` du repère 1 précise : « aucune fuite n'est enregistrée pendant cette onde ». |
| 152 | Le patho était le même tracé que EXP-052 (PMC10244670), et l'audit relevait un repère 3 et un normal à reprendre. | Le coordinateur garde ce tracé pour EXP-052. Aucun autre candidat ne montre un QTc > 500 ms avec onde T aplatie (478 ms, 492 ms en FA, hypothermie à ondes d'Osborn, FA à 463 ms). J'ai donc passé 152 en `traces.manque` et retiré ses images (`img/EXP-152_*`, `_verif/EXP-152.png`). |
| 105 | Le patho est un schéma, et non un tracé réel. | Je l'ai gardé, et ajouté `a_chercher.patho` : cystomanométrie réelle avec EMG sphinctérien en dyssynergie. |
| 106 | Les panneaux sains A sont à côté des panneaux B. | La `technique` précise : « panneaux A sains, B pathologiques ». |
| 127 | Les muscles de recueil diffèrent entre le normal et le patho. | La `technique` du patho le déclare : court extenseur des orteils, contre tibial antérieur pour le normal. |
| 129 | La pointe du repère 2 était sur un cycle. | Elle est déplacée dans l'intervalle apnéique entre deux cycles (23 ; 32), vérifiée en zoom. |
| 153 | Le patho vient d'un enfant. | La `technique` précise : « chez un enfant (encéphalopathie au cours d'une maladie de Kawasaki) ». |

Validation : le JSON est valide et `generer.py` passe.
