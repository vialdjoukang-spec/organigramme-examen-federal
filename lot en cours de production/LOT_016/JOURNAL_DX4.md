# JOURNAL_DX4 — LOT_016 — DX.4 Hyperthyroïdie (thyrotoxicose)

Rédacteur Phase B DX.4, 30.10.2026 (Europe/Zurich). Fichier : `LOT_016_Phase_B_V0_DX.4.html`.

## Hypothèses et décisions
- Aucune recommandation suisse de traitement de l'hyperthyroïdie trouvée (SSED : seulement la stratégie de dosage SSCC/SSED d'octobre 2025, [S5]). Le traitement suit l'ETA 2018 [S2], la HAS 2022 [S4] (texte francophone européen, adultes de moins de 65 ans) et le consensus ETA/BTA/SfE 2026 [S3] ; chaque dose non AIPS est attribuée à sa source et marquée « hors information professionnelle ».
- Doses de crise du consensus 2026 supérieures aux AIPS (propranolol 60–80 mg/4 h vs Inderal® 10–40 mg 3–4×/j ; carbimazole 80–100 mg/j vs Néo-Mercazole® 20–60 mg/j ; propylthiouracile 500–1000 mg puis 250 mg/4 h vs Propycil® 300–600 mg/j) : écrites comme divergence, sans trancher.
- Iodure dans la crise : seule spécialité suisse = Iodure de potassium 65 SERB (accident nucléaire), qui contre-indique l'hyperthyroïdie ; Lugol, perchlorate et thiamazole : 0 occurrence dans la liste Swissmedic au 30.09.2026 → écrits « non autorisé en Suisse » / absent, sans dose AIPS.
- Enfant : divergence AIPS Néo-Mercazole® (0,7–0,8 mg/kg/j, 30 mg/j au plus avant 12 ans) ↔ ETA 2022 (0,25–0,75 mg/kg/j en une prise) écrite ; la décision est laissée au pédiatre endocrinologue.
- Fréquence dans la PPI : 75/2677 = 2,8 % (64 thyrotoxicoses + 11 thyroïdites subaiguës, Bosch 2017, calcul dérivé recalculé).
- Correction d'audit 12 (piège TSH élevée / insuffisance surrénalienne) intégrée aux points 4 (E5), 5, 9.b, 10, 13 et 14 ; correction 15 (thyrotoxicose + défaillance d'organe = crise → soins intensifs) intégrée aux points 4, 10, 11 et 13.
- Pas d'espace insécable (leçon 11 de LOT_015), bien que §14.4 du Prompt les mentionne : la leçon, plus récente, prime.
- Beloc ZOK® (métoprolol) et la chlorpromazine du consensus ne sont pas utilisés (AIPS non relue en entier ou dose non vérifiée) : aucune dose écrite.
- ETA 2018 Basedow, ETA 2015 et ETA 2018 amiodarone : texte intégral inaccessible (Europe PMC HTTP 500 ; PMC : vérification anti-robot ; éditeur HTTP 403 ; aucun contournement). Résumés Europe PMC + extraits de `evidence/S17` utilisés.
- Le dossier temporaire de session est partagé entre rédacteurs : travail placé dans un sous-dossier propre `LOT_016_DX4/`.

## Contrôles faits
- `python3 harnais/controle_lot.py verifier "lot en cours de production/LOT_016" --sans-nom --json` : DX.4, 0 critique, 0 avertissement, 29 fenêtres popover, 14 points, titre conforme ; 118 789 octets, SHA-256 43ec00e130f609b3b817c7d652936d56c02f3c360ab21db08eafaad0c92d15e8.
- 69 citations entre guillemets vérifiées par script contre les textes AIPS, HAS, SSCC, OSAV et la LS : 69 retrouvées. Source [S34] NICE NG12 (1.13.2, avril 2026) lue dans evidence/S10.
- AIPS mises en cache : 21037, 56300, 52728, 49358, 57068, 50711, 53770 ; relues en cache : 31706, 49576, 23533, 29349, 33393, 46269.
