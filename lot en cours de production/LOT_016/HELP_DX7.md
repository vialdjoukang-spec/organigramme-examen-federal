# HELP_DX7 — LOT_016 — DX.7 Diabète sucré déséquilibré ou inaugural

## H16-16 — Seuils diagnostiques suisses du diabète et critères du syndrome hyperosmolaire — proposée close
- Seuils SSED trouvés : Obsan Bericht 10/2020, tableau T 5.1 (valeurs SGED/SSED) : glycémie à jeun ≥ 7,0 mmol/L ; HGPO 2 h ≥ 11,1 mmol/L ; HbA1c ≥ 6,5 % ; glycémie aléatoire ≥ 11,1 mmol/L avec symptômes ; prédiabète 5,6–6,9 mmol/L et HbA1c 5,7–6,4 % (https://www.obsan.admin.ch/sites/default/files/2021-09/obsan_10_2020_bericht.pdf, lu le 30.10.2026 ; `evidence/DX7_S02_…`).
- Figure 2b du consensus 2024 lue en image (https://pmc.ncbi.nlm.nih.gov/articles/instance/11343900/bin/125_2024_6183_Fig2_HTML.jpg, 30.10.2026) : glucose ≥ 33,3 mmol/L ; osmolalité efficace > 300 mOsm/kg [2 × Na + glucose] ou totale > 320 mOsm/kg ; β-OHB < 3,0 mmol/L ou bandelette < 2+ ; pH ≥ 7,3 et bicarbonate ≥ 15 mmol/L (`evidence/DX7_S05_…`).
- Reste ouvert : le document SSED d'origine (recommandation diagnostique) n'a pas été lu directement.

## H16-DX7-01 — Protocole suisse d'acidocétose de l'enfant
- Contexte : le fichier suit l'ISPAD 2022 (traduction française) ; aucun protocole de la Société suisse de pédiatrie ou d'un hôpital pédiatrique suisse n'a été trouvé.
- Question : quel protocole suisse (SSP/SGP, SGPED, HUG, CHUV, Kinderspital) fixe le remplissage, l'insuline et le potassium de l'ACD pédiatrique ?
- Déjà cherché : recherche web du 30.10.2026 (« acidocétose diabétique enfant recommandations suisses ») ; Wiley pedi.13406 : HTTP 403.
- Emplacement : DX.7, point 11.B, fenêtre `dx7-p11-enf`.

## H16-DX7-02 — Potassium intraveineux dans l'acidocétose et AIPS suisses
- Contexte : les AIPS de KCl 29552, 56521 et 56471 contre-indiquent l'acidose et la déshydratation sévère ; 29552 renvoie au « lactate de potassium », introuvable dans le XML AIPS du 8.10.2026 (recherche « lactate de potassium », « Kaliumlactat », « acétate de potassium »).
- Question : quelle spécialité potassique suisse autorisée les hôpitaux suisses emploient-ils dans l'ACD, et sous quelle justification ?
- Emplacement : DX.7, point 11.B, fenêtre `dx7-p11-conflits`.

## H16-DX7-03 — Données non trouvées
- Sensibilité et spécificité des signes physiques de déshydratation dans la crise hyperglycémique (point 6).
- Alternative d'imagerie du pancréas si DFGe < 30 mL/min/1,73 m², allergie iodée ou IRM impossible (point 9.c ; NG12 ne cite que TDM puis échographie).
- Coût national du diabète en Suisse (point 2).
- Règles d'arrêt de travail, d'assurance invalidité et d'assurance accidents propres au diabète (point 11.B).
- Directives SSED 2017 sur l'aptitude à conduire : tableau non lisible (image) dans la stratégie HUG 2022 ; texte SSED non lu.

## Audit médical DX.7 (auditeur-medical, opus, xhigh) — 30.10.2026
- H16-DX7-02 — réponse partielle : le corpus AIPS du 8.10.2026 ne contient aucune spécialité de « lactate de potassium » (recherche dans les descriptions du XML : « lactat », « Kalium », « potass », « KCl »). Kaliumphosphat 1 Molar B. Braun (45880) contre-indique « Hyperphosphatémie, hyperkaliémie, hypocalcémie, insuffisance rénale. », sans contre-indiquer l'acidose ; l'ISPAD 2022 associe KCl et phosphate de potassium (20 + 20 mmol/L). Le choix hospitalier suisse reste à confirmer par un protocole suisse (question ouverte).
- H16-DX7-04 — dose de glucose intraveineux dans l'hypoglycémie sévère : aucune AIPS lue ne la fixe. Glucose 20 % et 40 % B. Braun (29550, févr. 2025 ; https://files.refdata.ch/simis-public-prod/MedicinalDocuments/d0758e59ddb240c1a1101f0a4c837783-fr.html et …/2acbcc46a2914016a8c1a3aecf8b58bc-fr.html) : « Traitement de l’hypoglycémie » ; « Perfusion veineuse centrale uniquement. » ; « L’utilisation d’une solution de glucose à 10 % est recommandée pour le traitement de l’hypoglycémie chez les enfants. » Glucosum « Bichsel » (32920, mai 2020 ; …/0fbf8a305fc34409879ae7f7241f48ef-fr.html) : « Les solutions de perfusion glucosées de 20 % à 50 % peuvent être administrées en présence d'états hypoglycémi ques » ; « devraient cependant être perfusées par un cathéter veineux central ». Question : quelle source suisse (SSED, Tox Info Suisse, protocole hospitalier) fixe le bolus de glucose intraveineux de l'adulte et de l'enfant ? Emplacement : DX.7, fenêtre `dx7-p11-hypo`. Extraits non copiés dans `.cache/aips/` (écriture hors mandat de l'audit) : 29550 et 32920 à mettre en cache par la session principale.
- H16-DX7-03 (imagerie du pancréas si DFGe < 30 mL/min/1,73 m²) : ESMO 2023 (Ann Oncol 2023, PMID 37678671) non lisible (HTTP 403 le 30.10.2026) ; donnée toujours non trouvée.
