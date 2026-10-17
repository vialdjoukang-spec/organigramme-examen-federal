# Rapport · feat/cs-stations · Chiron · 17.10.2026

**Verdict :** prêt à fusionner si la CI (garde avec cs_build --check et G1 à G8, html, liens, tests) réussit.

- app_v2.html change par le seul patch 0019 (trois ancrages uniques : </head>, renderNot, montage après nBlock) ; aucune donnée CS n’entre dans app_v2.html ; orig/ et app.html restent intacts.
- Données : data/cs/format.json, data/cs/stations.json (5 stations), data/cs/schema/ ; assets/st/ (6 fichiers, environ 65 Ko), chargés à la demande.
- Contrôles : tools/cs_build.py --check (schéma, SSP, clés GES, hyp, src existantes, lu_le, aucune dose chiffrée, verbe conjugué par phrase) ; Lyncée étendu à data/cs (0 terme nouveau non défini ; glossaire : signe-de-rovsing, ecos, dgn ; 3 exclusions motivées) ; G1 à G8 réussis ; tests/test_cs_stations.py 15/15 ; suite 241/241 ; gardes 5/5 ; test_ck 75/75.
- Fiche par défaut (G1) sans station : la référence visuelle ne change pas.
- Revue clinique : data/cs déclenche l’étiquette audit:galien ; valide_par_vial reste false sur les 5 stations.
