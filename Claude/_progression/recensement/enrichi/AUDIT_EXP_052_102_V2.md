# Contre-audit V2 : EXP_b.json (EXP-052 à EXP-102)

| Objet | Valeur |
|---|---|
| Version auditée | `EXP_b.json`, 181 901 octets, SHA-256 `0503257c…ed7af9` ; le JSON est valide (51 entrées) |
| Référence | `AUDIT_EXP_052_102.md` (V1 : 57 %, 16 critiques) et `CORRECTIONS_EXP_052_102.md` |
| Méthode | 24 AIPS relues dans le texte HTML refdata par URL (numéro, date, extrait) ; calculs refaits en Python ; 2 recherches web (ESC 2026 IC, ERC 2025) ; recherche des formulations résiduelles dans le JSON |
| Verdict | **VALIDÉ** : 14/14 (100 %), zéro critique, zéro grave ; il reste 1 défaut léger à corriger (patch ci-dessous) |

## 1. Critiques V1 : vérification une par une

| # | Fiche | Contrôle dans le texte AIPS | Résultat |
|---|---|---|---|
| C1 | 095 | Dilatrend n° 53162 (oct. 2023) : la fiche signale le hors-indication et cite mot pour mot la contre-indication « insuffisance hépatique cliniquement manifeste » ; posologie HTA 12,5 puis 25 mg/j ; la dose Baveno est étiquetée européenne | Corrigé |
| C2 | 055 | Gutron n° 44976/44977 (mars 2021) : 3 × 2,5 mg/j, « jusqu'à 15 mg/jour », contre-indications | Corrigé |
| C3 | 065 | Brufen n° 45031 (déc. 2024) : hors indication, maximum 2400 mg/j, contre-indications NYHA III–IV et clairance < 30 ml/min | Corrigé |
| C4 | 058, 059, 060 | Aspirine Cardio n° 51795 (mars 2026) : 200–300 mg puis 100 mg/j ; 100 mg/j dans les indications cardiovasculaires | Corrigé |
| C5 | 058, 059 | Héparine n° 46613 (juin 2026) : STEMI sous fibrinolyse 60 U.I./kg (max. 4000) puis 12 U.I./kg/h (max. 1000) ; NSTEMI 60–70 U.I./kg (max. 5000) puis 12–15 U.I./kg/h | Corrigé, chiffres exacts |
| C6 | 052 | Isuprel n° 56457 (nov. 2020) : hors indication pour les torsades, 0,2–10 mg/24 h, arrêt si FC ≥ 130/min | Corrigé |
| C7 | 054 | KCl 7,45 % Sintetica n° 56521 (févr. 2024) : 10 mmol/h, 40 mmol/l et 200 mmol/j | Corrigé |
| C8 | 061 | Entresto (sept. 2025), Forxiga 10 mg (août 2026), Aldactone en entretien 25–100 mg/j | Corrigé |
| C9 | 069, 070, 072, 078 | Camzyos (janv. 2026 : 5 mg/j, max. 15 mg/j, FEVG < 55 % et < 50 %) ; Symbicort (juin 2023) ; Ofev 150 mg 2×/j (mars 2025) ; Esbriet 801 mg 3×/j (août 2022) ; Adempas 0,5–2,5 mg 3×/j, PAS ≥ 95 mmHg (juil. 2025) | Corrigé |
| C10 | 088, 094 | Nexium MUPS 20 mg 1×/j (citation exacte) ; Transipeg 1–4 sachets/j ; Resolor 1 mg porté à 2 mg, arrêt après 4 semaines | Corrigé ; date Nexium fausse (voir L1) |
| Ajout | 102 | Proscar 5 mg/j (nov. 2025) ; Avodart (oct. 2025) | Conforme |

## 2. Graves V1

| # | Résultat |
|---|---|
| G1 | ERC 2025 Special Circumstances (Resuscitation 2025;215 suppl. 1:110753) : la référence est vérifiée ; aucune mention « ERC 2021 » ne subsiste |
| G2 | ESC 2026 IC (ehag100, présidents Køber et Adamo) : référence vérifiée ; HFrEF < 50 %, HFpEF ≥ 50 % ; NT-proBNP marqué « à revérifier » |
| G3, G4 | ESC/EACTS 2025 (TAVI dès 70 ans, IIa précoce) et ESC 2025 myo-péricardite : appliqués et marqués « texte intégral non lu » |
| G5 | GINA 2026 et GOLD 2026 : appliqués ; le seuil du groupe E est marqué À vérifier |
| G6, G10, G11 | Hors AIPS signalés avec extrait : Symbicort à la demande seul (070, 075), bicarbonate dans l'intoxication tricyclique, Paspertin dans la gastroparésie |
| G7, G8 | « ESE 2025 » est supprimé ; l'Endocrine Society 2025 est étiquetée USA (dernier recours) ; l'extrait Aldactone (100–400 mg/j, dose minimale chez l'inopérable) est exact |
| G9, G12 | ATS 2020 et ATS 2019/2011 sont étiquetées USA ; les sources européennes sont ajoutées (UEG/ESNM 2021, ERS 2022 ; ERS 2017 marquée non lue) |

## 3. Moyens et légers V1
Tous sont corrigés. Contrôles chiffrés :
- CKD-EPI 2021 ≈ 69 (valeur recalculée : 69,2).
- MELD-Na = MELD + 1,32 × (137 − Na) − 0,033 × MELD × (137 − Na), avec Na borné entre 125 et 137 ; l'exemple donne 25,4, soit « ≈ 25 », exact.
- La DLCO est harmonisée à 60 % (valeur et trace).
- La PD20 est corrigée (normale > 400 µg) et honnêtement marquée « lu de mémoire, À vérifier ».
- Le seuil de FeNO est fixé à ≥ 50 ppb.
- L'unité du KCO est ajoutée.
- « (mesure du JT) » remplace le texte tronqué.
- Les items sont rendus verbaux.

La recherche ne trouve plus aucune occurrence de « non lue ici », « non consultée », « non extraite », « ESE 2025 », « ERS 2020 », « ERC 2021 », « GINA 2024 » ni « GOLD 2025 ».

## 4. Nouveau défaut (non bloquant)

| # | Gravité | Emplacement | Extrait | PATCH exact |
|---|---|---|---|---|
| L1 | Léger | EXP-088, traitement[0] et sources[2] | « (AIPS Nexium MUPS n° 55609, juillet 2026) » ; « mise à jour juillet 2026) — lu » | Remplacer « juillet 2026 » par « juin 2026 » aux deux endroits. Le texte AIPS porte « Mise à jour de l'information Juin 2026 » ; juillet 2026 n'est que la date de dépôt refdata |

## 5. Compléments à venir (hors verdict, honnêtement marqués)
- Molécules absentes du corpus : colchicine, gluconate ou chlorure de calcium i.v., nadolol, citrate de potassium.
- Textes intégraux non lus : ESC/EACTS 2025, ESC 2025 et 2026, GINA et GOLD 2026, EAU 2026, Endocrine Society 2025, ERS 2017, Randerath, Swisstransplant, sociétés suisses (SSP, SGG, SSN, SSH, SGED).

## 6. Score (7 axes, 2/1/0)
Examen de référence 2 · lecture 2 · valeurs et unités 2 · calculs 2 · syndrome et traitement 2 · doses AIPS 2 (L1 n'est qu'une date) · sources et phrases 2. **Total : 14/14.**

**Question finale : oui.** Toutes les doses du corpus sont citées par URL, avec leur numéro et leur date. Les usages hors AIPS et les contre-indications sont signalés. Les sources sont étiquetées selon l'ordre Suisse → Europe → USA. Seul le patch L1 reste à appliquer.

## Clôture
Patch léger EXP-088 (Nexium MUPS juin 2026) appliqué : **audit-ok** pour EXP-052 à 102. Les 153 explorations fonctionnelles sont audit-ok (texte ; tracés à chercher).
