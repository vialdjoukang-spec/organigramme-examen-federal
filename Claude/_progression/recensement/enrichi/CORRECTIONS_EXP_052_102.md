# Corrections : EXP_b.json (EXP-052 à EXP-102) après AUDIT_EXP_052_102.md

Date : 14.11.2026. Le JSON reste valide (json.load : 51 entrées). AIPS lues par URL refdata avec `aips_fiche.py` (texte HTML en cache) ; deux recherches web (ESC 2026 IC, ERC 2025).

## Critiques
| # | Fiche | Correction appliquée (source lue) |
|---|---|---|
| C1 | 095 | Carvédilol : hors indication AIPS ; contre-indiqué en cas d'« insuffisance hépatique cliniquement manifeste » ; posologie HTA 12,5 mg/j pendant 2 j puis 25 mg/j (Dilatrend n° 53162, oct. 2023) ; dose Baveno étiquetée européenne |
| C2 | 055 | Midodrine : 3 × 2,5 mg/j, jusqu'à 15 mg/j, contre-indications (Gutron n° 44976/44977, mars 2021) |
| C3 | 065 | Ibuprofène hors indication ; dose journalière maximale 2400 mg ; contre-indications NYHA III–IV et clairance < 30 ml/min (Brufen n° 45031, déc. 2024) |
| C4 | 058, 059, 060 | Aspirine Cardio n° 51795 (mars 2026) : infarctus 200–300 mg puis 100 mg/j ; 100 mg/j dans les indications cardiovasculaires |
| C5 | 058, 059 | Héparine B. Braun n° 46613 (juin 2026) : NSTEMI 60–70 U.I./kg puis 12–15 U.I./kg/h ; STEMI avec fibrinolyse 60 U.I./kg (max. 4000) puis 12 U.I./kg/h |
| C6 | 052 | Isoprénaline hors indication AIPS pour les torsades ; 0,2–10 mg/24 h ; arrêt si FC ≥ 130/min (Isuprel n° 56457, nov. 2020) |
| C7 | 054 | KCl 7,45 % Sintetica n° 56521 (févr. 2024) : 10 mmol/h, 40 mmol/l et 200 mmol/j au maximum si K > 2,5 mmol/l |
| C8 | 061 | Entresto (sept. 2025), Forxiga (août 2026), Aldactone (entretien 25–100 mg/j) cités mot pour mot |
| C9 | 069, 070, 072, 078 | Camzyos, Symbicort, Ofev, Esbriet, Adempas : posologies AIPS citées |
| C10 | 088, 094 | Nexium MUPS n° 55609 (20 mg 1×/j) ; Transipeg n° 53282 ; Resolor n° 59304 |

## Graves
- G1 : ERC 2021 → ERC 2025 (052, 054, 057) ; hypothermie : transfert vers un centre d'ECMO veino-artérielle.
- G2 : ESC 2026 IC (ehag100) : HFrEF < 50 %, HFpEF ≥ 50 %, HFmrEF supprimée, ARM classe I ; vérifié par recherche web (sources secondaires).
- G3 : ESC/EACTS 2025 (ehaf194) : TAVI dès 70 ans ; intervention précoce IIa (062, 063).
- G4 : ESC 2025 myo-péricardite (ehaf192) : colchicine 3–6 mois, corticoïdes en 2e ligne, anti-IL-1 en 3e ligne.
- G5 : GINA 2026 et GOLD 2026 (070, 071, 073, 075) ; nouveau seuil du groupe E non relu (À vérifier).
- G6 : Symbicort à la demande seul (paliers 1–2) signalé hors AIPS.
- G7 : « ESE 2025 » supprimé → Endocrine Society 2025, étiquetée USA (dernier recours) ; ESC 2024 HTA ajoutée.
- G8 : spironolactone dans l'hyperaldostéronisme : texte AIPS exact (100–400 mg/j avant l'opération ; dose efficace la plus faible chez l'inopérable).
- G9 : ATS 2020 (Jacobs) étiquetée USA ; équivalent ERS non trouvé.
- G10, G11 : bicarbonate (intoxication tricyclique) et Paspertin (gastroparésie) signalés hors indication AIPS, avec extraits.
- G12 : 090 → UEG/ESNM 2021 ; 076 → ERS 2022 (≥ 50 ppb) ; 086 → ERS 2017 (Randerath) ajoutée, non lue.

## Moyens et légers
- M1 : la mention « SSC … non lu » est remplacée dans toutes les fiches par la plateforme FMH « Guides de pratique Suisse ».
- M2 : seuils QTc étiquetés AHA/ACCF/HRS 2009 (non vérifié CH) ; cible kaliémique non chiffrée.
- M3 : posologie Lokelma complétée. M4 : PD20 corrigée (normale > 400 µg ; À vérifier sur le texte intégral). M5 : FeNO ≥ 50 ppb (ERS 2022).
- M6 : VO2 < 10 = haut risque, sans contre-indication absolue. M7 : DLCO < 60 %. M8 : formule MELD-Na ajoutée ; règle Swisstransplant À vérifier.
- M9 : 5e définition universelle 2026 signalée (seuils À vérifier). M10 : EAU 2026 ; Proscar n° 51774 et Avodart n° 56106 cités.
- L1 : CKD-EPI ≈ 69 ml/min/1,73 m². L2 : unité du KCO. L3 : « (mesure du JT) ». L4 : items rendus verbaux (071, 073, 080, 082, 093). L5 : protocole Metcalf clarifié. L6 : citrate de potassium absent du corpus. L7 : nomenclature AVP-D / AVP-R.

## Restes « À vérifier »
Colchicine, gluconate ou chlorure de calcium i.v. et citrate de potassium sont absents du corpus refdata. Les textes intégraux suivants n'ont pas été lus : ESC/EACTS 2025, ESC 2025 péricardite, GINA 2026, GOLD 2026, EAU 2026, Endocrine Society 2025, ERS 2017 sur la PD20 et Randerath, ainsi que la règle Swisstransplant.
