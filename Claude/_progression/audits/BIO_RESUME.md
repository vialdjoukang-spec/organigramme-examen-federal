# Biologie (EX-1) : résumé des verdicts, 13.11.2026

Source : `Claude/_progression/audits/bio_*.audit.json`, dernière vérification indépendante de chaque groupe.
Les 12 groupes portent audit-ok. Les 11 corrections mineures sont levées le 13.11.2026 (0 restant).

| Groupe | Fiches | Restants de l'audit | Verdict (vérification) | Restants mineurs |
|---|---|---|---|---|
| S1 | 9 | 16 | audit-ok (v2) | 0 (AIPS Benerva 10989 cité) |
| S2/S12/T | 8 | 8 | audit-ok (v1) | 0 |
| S3 | 6 | 5 | audit-ok (v1) | 0 |
| S4 | 7 | 8 | audit-ok (v1) | 0 (mnémotechnique « 0,5 – 0,6 – 2/3 ») |
| S5 | 10 | 16 | audit-ok (v1) | 0 (phrase d'audit retirée ; tableau 5 cité) |
| S6 | 10 | 15 | audit-ok (v1) | 0 |
| S7 | 8 | 14 | audit-ok (v1) | 0 (doublon supprimé ; outil corrigé) |
| S8 | 8 | 12 | audit-ok (v1) | 0 (C5DC « non vérifié CH » ; ICP-MS : zinc sang total, Cu/Se sérum, Medics 09.2022) |
| S9 | 8 | 12 | audit-ok (v1) | 0 |
| S10 a | 9 | 8 | audit-ok (v1) | 0 |
| S10 b | 8 | 10 | audit-ok (v1) | 0 (HNF 2712 en déduction ; AIPS Pradaxa 61385 mot pour mot) |
| S11 | 10 | 13 | audit-ok (v1) | 0 (« prescrite seule » présent, HUG RPA 3803 ; passerelles « — » supprimées par l'outil) |

Assemblage du 13.11.2026 : controle.py VERT (409 fiches). La page `receptacle.py --audites 1-32` s'ouvre sur la fiche
EX-1-S1-lcr-cytologie avec 0 erreur console et sans défilement horizontal à 1280 et 390 px.
Capture : `Claude/_progression/captures/bio_fiche_1280.png`.

Outil : `charpente.py` fusionne désormais les passerelles par (type, cible), sans recréer de doublon ni réinjecter de « — » dans une fiche remplie (`fusion_passerelles`) ; relance : 0 fiche écrite, `git diff --stat donnees` vide.
