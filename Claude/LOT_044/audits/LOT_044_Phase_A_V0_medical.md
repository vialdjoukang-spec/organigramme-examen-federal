# Audit médical ciblé — LOT_044_Phase_A_V0.html

Version : 167566 octets, SHA-256 `c9141ba0897f0ed6601ebc72ad1866db3f89149b9791d67720e2c06c9a5f6a3e`. Points lus : 2, 3, 4, 8, 9, 10 (PA), 11, 12 ; AIPS confrontées aux extraits du paquet et au corpus AipsDownload_20261008.

| Point | Note et raison |
|---|---|
| P2 | 2 — TOPIC suisse daté, contexte cabinet/urgence/ambulance, histoire naturelle. |
| P3 | 2 — chaîne mécanisme→examen→traitement et tableau de corrélation présents. |
| P4 | 2 — liste et rangs E conformes à LISTE_DX_CANONIQUE ; Boerhaave hors liste ; discriminants avec piège. |
| P8 | 1 — critères STEMI/UDMI/PERC/YEARS corrects ; probabilité HUG (table 2006) et ergométrie « test de base » périmées (LV8). |
| P9 | 1 — gold standards déclarés ; seuil âge sans « > 75 ans » ; seuil O2 94 % contredit le point 10 (90 %). |
| P10 | 1 — chaque nœud décide ; nœud E1 « traiter comme coronarien » placé avant l’exclusion de la dissection (E2). |
| P11 | 1 — structure A–D complète ; 4 Critiques AIPS (voie Aspirine Cardio, CI nitroglycérine, CI aspirine, < 18 ans). |
| P12 | 1 — trois niveaux ; aucune recommandation suisse de prévention (AGLA/SSC). |

**Score : 11/16 = 68.8 %. Question finale : non.** Manque : 4 Critiques AIPS ; probabilité prétest et place de l’ergométrie périmées ; fentanyl i.v. sans AIPS alors que 3 monographies existent ; incohérence du seuil d’oxygène.

| Gravité | Point | Extrait (≤ 200 car.) | Correction | Source |
|---|---|---|---|---|
| Critique | 11 | Intraveineuse ou orale, comprimé croqué | Intraveineuse ou orale ; la charge de 200 à 300 mg exige une forme non gastro-résistante, car Aspirine® Cardio ne se croque pas aips-51795-4 aips-51795-3 | aips-51795-3 ; aips-51795-4 |
| Critique | 11 | Les contre-indications sont le choc, l’infarctus aigu avec pressions de remplissage basses, l’hypotension prononcée avec une pression systolique inférieure ou égale à 90 mmHg, l’hypovolémie sévère et  | Les contre-indications comprennent le choc, l’infarctus du myocarde aigu, l’hypotension avec une systolique inférieure ou égale à 90 mmHg, l’hypovolémie et l’anémie sévères, et le riociguat aips-36830 | aips-36830-3 |
| Critique | 11 | Les contre-indications sont l’hypersensibilité aux salicylates, le bronchospasme après un anti-inflammatoire, la diathèse hémorragique, l’ulcère gastroduodénal actif, la cirrhose avec ascite et l’insu | Les contre-indications comprennent l’hypersensibilité aux salicylates, la diathèse hémorragique, l’ulcère actif, l’insuffisance cardiaque sévère NYHA III-IV, une clairance inférieure à 30 ml/min et le | aips-51795-5 |
| Critique | 11 | Chez l’enfant, les données d’efficacité et de sécurité sont absentes pour Aspirine® Cardio avant 18 ans aips-51795-4 . | Chez l’enfant et l’adolescent de moins de 18 ans, Aspirine® Cardio ne doit pas être utilisé, faute de données d’efficacité et de sécurité aips-51795-4 . | aips-51795-4 |
| Grave | 8 | Un homme de 55 ans avec un angor atypique a une probabilité clinique de coronaropathie de 65 % wfba9d7-7 . | Le support des HUG reprend une table de 2006 qui attribue 65 % à un homme de 55 ans avec un angor atypique, valeur à remplacer par le modèle ESC actuel wfba9d7-7 . | wfba9d7-7 ; ESC 2024 CCS, Essential Messages (modèle RF-CL, Classe I) |
| Grave | 8 | L’ergométrie devient le test de base pour une probabilité intermédiaire, entre 15 et 85 % wfba9d7-13 . | Le support des HUG faisait de l’ergométrie le test de base entre 15 et 85 %, alors que l’ESC actuelle y privilégie l’imagerie fonctionnelle de stress wfba9d7-13 . | wfba9d7-13 ; ESC 2024 CCS, Essential Messages (imagerie de stress si > 15–85 %) |
| Moyen | 9 | Ce seuil porte la proportion de patients dont l’embolie peut être exclue de 6,4 à 30 %, sans faux négatif supplémentaire w613fa4-83 . | Chez les patients de plus de 75 ans, ce seuil porte de 6,4 à 30 % la proportion d’embolies exclues, sans faux négatif supplémentaire w613fa4-83 . | w613fa4-83 |
| Moyen | 9 | Saturation en oxygène inférieure à 94 % Hypoxémie Oxygène pour viser 94 à 98 % | Saturation en oxygène inférieure à 90 % Hypoxémie Oxygène lors du transfert d’un infarctus aigu, comme au point 10 wcdaf96-19 | wcdaf96-19 ; ESC 2023 SCA (pas d’O2 systématique si SaO2 ≥ 90 %) |
| Moyen | 10 | Si le doute persiste sans diagnostic alternatif, alors on traite comme une origine coronarienne avérée w8db60a-5 . | Si le doute persiste sans diagnostic alternatif, et après recherche des signes de dissection du nœud E2, alors on traite comme une origine coronarienne avérée w8db60a-5 . | w8db60a-5 |
| Léger | 8 | Dans les autres dérivations, le seuil est d’au moins 1 mm, car il faut exclure l’effet de la masse myocardique : en l’absence d’hypertrophie ventriculaire gauche ou de bloc de branche gauche w8db60a-4 | Dans les autres dérivations, le seuil est d’au moins 1 mm, en l’absence d’hypertrophie ventriculaire gauche ou de bloc de branche gauche w8db60a-4 . | w8db60a-4 |
| Léger | 11 | Une capsule suffit en règle générale, car la limite est de 5 capsules par jour aips-36830-2 . | Une capsule suffit en règle générale, deux exceptionnellement, et la dose quotidienne ne dépasse pas 5 capsules aips-36830-2 . | aips-36830-2 |
| Léger | 9 | Chez la femme, la sensibilité est donc de 61 % et la spécificité de 70 % wfba9d7-11 . | Chez la femme, la sensibilité est de 61 % et la spécificité de 70 % wfba9d7-11 . | wfba9d7-11 |
| Grave | HELP | Fentanyl i.v. déclaré sans AIPS (HELP 1) | Lire et citer l’AIPS de Fentanyl-Mepha i.v./i.m. (53484), Fentanyl Sintetica (53987) ou Fentanyl-Piramal (31110), présents dans AipsDownload_20261008. | erweiterte_ham_ind.xlsx (30.09.2026) ; idx SmPC |
| Moyen | HELP | Nitrés dans le STEMI (protocole HUG) face à l’AIPS Streuli qui contre-indique l’infarctus aigu | Nommer la forme i.v. (Nitroglycerin Sintetica 55459, CI : infarctus avec basses pressions de remplissage) pour l’usage hospitalier. | aips-36830-3 ; aips-55459-6 |
| Moyen | HELP | Prévention : aucune recommandation suisse | Ajouter AGLA/SSC datées. | HELP 4–5 |
