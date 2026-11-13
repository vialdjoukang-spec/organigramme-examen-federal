# Biologie (EX-1) : résumé des verdicts, 13.11.2026

Source : `Claude/_progression/audits/bio_*.audit.json`, dernière vérification indépendante de chaque groupe.
Les 12 groupes portent audit-ok. Il reste 11 corrections mineures, aucune critique, grave ni moyenne.

| Groupe | Fiches | Restants de l'audit | Verdict (vérification) | Restants mineurs |
|---|---|---|---|---|
| S1 | 9 | 16 | audit-ok (v2) | 1 : vitamines-b1-b12, « PO 100 mg/j » attribué au HUG SMPR seul alors que l'AIPS Benerva 10989 le donne |
| S2/S12/T | 8 | 8 | audit-ok (v1) | 0 |
| S3 | 6 | 5 | audit-ok (v1) | 0 |
| S4 | 7 | 8 | audit-ok (v1) | 1 : liquide-pleural-criteres-light, mnémotechnique à aligner sur « 0,5 – 0,6 – 2/3 » |
| S5 | 10 | 16 | audit-ok (v1) | 1 : bilan-hepatique-asat-alat-pal, phrase d'audit recopiée dans temps2_examen[0].anomalie |
| S6 | 10 | 15 | audit-ok (v1) | 0 |
| S7 | 8 | 14 | audit-ok (v1) | 1 : passerelle en double « Fondement → SF-S7-physiologie » sans pourquoi ; charpente.py (l. 520) la recrée |
| S8 | 8 | 12 | audit-ok (v1) | 2 : acylcarnitines (C5DC attribué à neoscreening.ch) ; oligo-elements (ICP-MS sérique) |
| S9 | 8 | 12 | audit-ok (v1) | 0 |
| S10 a | 9 | 8 | audit-ok (v1) | 0 |
| S10 b | 8 | 10 | audit-ok (v1) | 2 : suivi-biologique-anticoagulants (piège HNF hors HUG 2712) ; tp-inr-tca (citation AIPS Pradaxa) |
| S11 | 10 | 13 | audit-ok (v1) | 2 : 18 passerelles « — » recréées par charpente.py ; « prescrite seule » à rétablir (HUG RPA 3803) |

Assemblage du 13.11.2026 : controle.py VERT (409 fiches). La page `receptacle.py --audites 1-32` s'ouvre sur la fiche
EX-1-S1-lcr-cytologie avec 0 erreur console et sans défilement horizontal à 1280 et 390 px.
Capture : `Claude/_progression/captures/bio_fiche_1280.png`.
