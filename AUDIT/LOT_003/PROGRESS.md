# LOT_003 — progression (audit du 24.10.2026)
Méthode : source/gen_dxN.py importe source/lot3_commun.py (→ outils_local/gen_v7l.py, sources src_lot3.py, DIFF commun, SOCIAL, FICHE).
Évaluation : source/eval.sh (decoupe_l → examens → style → score → verif_v7). Fragments supplémentaires : source/bib_extra (build_extra.py).
Gabarit de complétude (proxys score.py) : P6 « normal » + sensibilité/spécificité ; P7 fenêtres « Signes fonctionnels » / « Signes physiques » (≥ 5 fenêtres) ;
P8 « ne suffit pas » ; P9 texte « première intention / deuxième intention », indication / moment / préparation, alternatives grossesse/enfant/DFGe/iode/IRM ;
P11 titres 11.A (urgence… car) / 11.B / 11.C / 11.D, « forme compliquée », FICHE médicament ; P12 primaire/secondaire/tertiaire + mention suisse.
## État
- [x] DX.1 Diabète décompensé — 98,8 % ; fichiers _a/_b
- [x] DX.2 … DX.10, SSP + bloc 2 ; captures ; RAPPORT_AUDIT.md ; MANIFEST.sha256 (voir fin de fichier)
## Chiffres à vérifier
### DX.1
- Consensus 2024 : ACD glycémie ≥ 11,1 ou diabète connu, β-OHB ≥ 3,0, pH < 7,30 ou HCO₃ < 18 ; EHH ≥ 33,3, osmolalité efficace > 300 (totale > 320), HCO₃ ≥ 15 ; résolution β-OHB < 0,6 + pH ≥ 7,30 ou HCO₃ ≥ 18 ; EHH résolu < 300 mOsm/kg, glycémie < 13,9.
- Liquides 1–1,5 L la 1re h (15–20 mL/kg), puis 250–500 mL/h ; glucose dès < 13,9 ; insuline 0,1 U/kg/h (bolus 0,1 facultatif), 0,05 dès < 13,9 ; K⁺ < 3,5 : 10–20 mmol/h ; 3,5–5 : 20–30 mmol/L ; bicarbonate si pH < 7,0 ; phosphate < 0,32 mmol/L.
- EHH (JBDS 2023) : osmolalité −3 à −8 mOsm/kg/h, glycémie ≤ 5 mmol/L/h, insuline 0,05 U/kg/h si glycémie ne baisse plus ou β-OHB > 1,0.
- ACD au diagnostic du type 1 enfant 20–45 % (Cherubini 2020) ; mortalité ACD < 1 % ; EHH ≈ 5–20 % ; œdème cérébral 0,5–0,9 % (ISPAD 2022) ; déficit hydrique 100 mL/kg (ACD), 100–220 mL/kg (EHH).
- Katz 0,3 × (glycémie − 5,5) ; Hillier 0,4 ; Winter 1,5 × HCO₃ + 8 ± 2.
- Peptide C < 200 pmol/L / > 600 pmol/L (ADA/EASD 2021) ; téplizumab ≈ 2 ans de délai (Herold 2019) ; rémission type 2 HbA1c < 6,5 % ≥ 3 mois.
- Traitement de fond : insuline 0,4–0,5 U/kg/j ; metformine 500 mg 1–2×/j, CI DFGe < 30 ; gliflozines 10 mg ; sémaglutide 0,25→1 mg ; tirzépatide 2,5→15 mg ; demi-vie empagliflozine ≈ 12 h ; suspension gliflozine 3 jours avant chirurgie.
- Remboursement LAMal de l’éducation thérapeutique (conseil en diabétologie) sur prescription ; statut suisse du zimislécel et de l’icodec.

## DX.2 FAIT (98.8 %, 0/0/0) — chiffres à vérifier
- Berne urgences (Arampatzis 2012, S34) : 2 % Na > 145 ; 74 hypernatrémies sévères > 149 sur 43 911 ; 38 % symptômes neuro ; 21 décès / 74 (≈ 28 %, calculé à partir du résumé).
- Lindner 2007 (S66) : 9 % (2 % admission, 7 % acquise) ; mortalité 39–43 % vs 24 % ; RR 2,1.
- Lindner 2009 (S67) : fièvre 45 %, polyurie 38 %, IRA 35 %, hypertoniques 27 %, diarrhée 18 % (n = 45).
- Chauhan 2019 (S65) : correction rapide non associée à surmortalité (rétrospectif).
- Bornes 146–150/151–160/> 160 = repères d’enseignement non consensuels (signalé).
- Exemple calcul : 35 L, Na 160 → déficit ≈ 5 L ; ΔNa/L : G5 −4,4 ; NaCl 0,45 −2,3 ; 0,9 −0,2.
- Furosémide 20–40 mg IV ; demi-vie 1–2 h (AIPS à revérifier).

## DX.3 FAIT (98.8 %, 0/0/0) — chiffres à vérifier
- Agostini 2018 (S38) xérostomie ≈ 22 % ; Qin 2015 (S37) ≈ 61/100 000, F/H ≈ 10/1 (10,72 de mémoire) ; anti-SSA 50–70 % (S70).
- Zintzaras 2005 (S69) : lymphome RR ≈ 19 (SIR 18,8 de mémoire) — à vérifier.
- ACR/EULAR 2016 Se 96 %, Sp 95 %. Salive repos 0,3–0,4 mL/min (S70, à vérifier).
- QUANTEC < 25 Gy (S73) ; PARSPORT 74 % → 38 % (S74). PATCH : 18 % → 7,4 % (S72). ACR 2020 échos 16–18 → 26 SA (S71).
- Pilocarpine Salagen® 5 mg ×3–4, max 30 mg/j ; HCQ ≤ 5 mg/kg (AIPS à vérifier). OPAS art. 18 (S76) à vérifier lettre exacte.
- NEPTUNUS ianalumab (S75) : sources de presse/congrès 2026.

## DX.4 FAIT (98.8 %, 0/0/0) — chiffres à vérifier
- Fenske 2018 (S27) : 82/144 PP (57 %), 59 DI central (41 %), 3 néphrogènes (2 %) ; précision 96,5 % vs 76,6 % ; PP vs DI partiel 95,2 % vs 73,3 %.
- Sailer 2017 (S31) : 11–20 % schizophrénie. Winzeler 2021 (S77) : −490 mL/8 h (−17 %).
- Protocole NaCl 3 % : 250 mL / 15 min puis 0,15 mL/kg/min, Na q30 min, cible ≥ 150 ; fin 30 mL/kg eau (protocole Fenske, à revérifier).
- ESE 2014 (S62) : 150 mL NaCl 3 % / 20 min ×2–3, +5 mmol/L, ≤ 10/24 h.
- Seuil poids +2–3 kg : empirique (signalé). Clozapine 200–450 mg/j, NFS hebdo 18 semaines (AIPS à vérifier).
- Natrémie de grossesse −4–5 mmol/L (repère physiologique, source S62 non vérifiée).

## DX.5 FAIT (98.8 %, 0/0/0) — chiffres à vérifier
- EMPA-REG (S79) : infection génitale 6,4 % vs 1,8 % ; déplétion volémique 5,1 % vs 4,9 % ; acidocétose ≈ 0,1 % (de mémoire, à vérifier dans l’article).
- Heerspink 2016 (S78) : glycosurie 60–80 g/j ; seuil rénal 4–5 mmol/L.
- Carvounis 2002 (S80) : FEUrée < 35 % Se 90 %, Sp 96 % (à vérifier).
- ADA 2025 (S19) : arrêt gliflozine 3 j (ertugliflozine 4 j) avant chirurgie.
- Anse : 20–25 % du sodium filtré (S54). Torasémide t½ 3–4 h ; tolvaptan t½ 3–12 h ; transaminases mensuelles 18 mois puis /3 mois (AIPS Jinarc).

## DX.6 — chiffres à vérifier
- OPTIMIZE-HF (S81) : 19,7 % de natrémie < 135 sur 47 647 patients (vérifié résumé PubMed).
- Angeli 2006 (S42) : 49,4 % / 21,6 % / 5,7 % (n = 997, natrémie disponible chez 983 ; vérifié résumé).
- Vaduganathan 2020 (S82) : HR 0,38 critère combiné (≈ 62 %) — estimation inter-essais.
- ESC : prévalence IC 1–2 % ; seuils NT-proBNP 125/300/450/900/1800.
- SAAG précision ≈ 97 % ; ascite > 1,5 L pour la matité ; polynucléaires ≥ 250/mm³ ; albumine 8 g/L retiré > 5 L ; albumine 1 g/kg (EASL 2018).
- Demi-vies sacubitril ≈ 1,4 h, valsartan ≈ 10 h, bisoprolol 10–12 h (Swissmedicinfo à contrôler).
- Réadaptation cardiaque ambulatoire : remboursement par OPAS (art. 25) — S56 cite la LAMal, préciser l'article.
- FINEARTS-HF / SUMMIT : autorisation suisse dans l'IC à FEVG préservée non vérifiée.

## DX.7 — chiffres à vérifier
- Yeh 2013 (S49) : 233/100 000 femmes, 85/100 000 hommes (2010).
- Walker & Shane 2022 (S48) : ≈ 90 % HPT primaire + cancer (vérifié résumé) ; adénome ≈ 85 %.
- Endocrine Society 2023 (S85) : dénosumab suggéré avant bisphosphonate ; calcitonine arrêtée après 48–72 h (vérifié résumé). NaCl 200–300 mL/h, diurèse 100–150 mL/h : à contrôler dans le texte intégral.
- Zometa® 4 mg ≥ 15 min ; Xgeva® 120 mg ; Miacalcic® injectable : disponibilité suisse à vérifier (Swissmedicinfo).
- Critères chirurgicaux 2022 (S47) : âge < 50, +0,25 mmol/L, DFGe < 60, calciurie > 10 mmol/24 h, T-score ≤ −2,5.
- Os affamé : seuil < 2,1 mmol/L (Witteveen 2013, S86 ; définitions variables).
- Christensen : < 0,01 / > 0,02.

## DX.8 — chiffres à vérifier
- Forni Ogna 2016 (S45) : MRC 10,4 % en Suisse.
- Lanktree 2018 (S57) : PKAD ≈ 9,3 / 10 000.
- Halbgewachs & Domes 2015 (S46, vérifié texte intégral) : SLO 0,5–52 % ; > 200 mL/h × 2 h ou > 3 L/24 h ; physiologique ≈ 24 h, pathologique > 48 h ; compensation 75 % de la diurèse de l'heure précédente (niveau III) ; NaCl 0,45 % si troubles cognitifs ; Na urinaire > 40 ; diurèse /2 h, constantes /6–8 h, électrolytes /12–24 h ; rétention aiguë 1/10 hommes 70–79 ans.
- Nyman 1997 (S90) : vidange rapide sans surcroît de complications.
- Critères de Pei 2009 (S88) ; KDIGO 2024 : PAS systolique < 120, gliflozine si DFGe ≥ 20, baisse albuminurie ≥ 30 %.
- Jinarc® 45/15 → 90/30 mg ; Pradif® T 0,4 mg ; demi-vies (Swissmedicinfo).
- « SSED recommande l'albuminurie annuelle chez le diabétique » : formulation à confirmer (recommandation SSED).

## DX.9 — chiffres à vérifier
- Prévalence AVP-D ≈ 1/25 000 (S26) ; ≈ 80 % de neurones détruits (S26).
- Fenske 2018 (S27) : 57 % / 41 % / 2 % ; précision 96,5 % ; Se/Sp > 90 % au seuil 4,9 (Se ≈ 93 %, Sp ≈ 100 % de mémoire — à vérifier).
- Timper 2015 (S28) : basale ≥ 21,4 pmol/L Se/Sp 100 %. Winzeler 2019 (S29) : arginine ≤ 3,8 à 60 min, 93 %. Christ-Crain 2023 (S4) : 74 % vs 96 %.
- Behan 2015 (S91) : 27 % Na 131–134, 14,6 % ≤ 130 (vérifié résumé). Atila 2022 (S92) : 22 % hyponatrémie signalée.
- Atila 2023 (S93) : déficit en ocytocine (test MDMA) ; essais d'ocytocine 2026 non vérifiés.
- Contre-indications du NaCl 3 % (épilepsie, IC), arrêt desmopressine 24 h avant, réduction de dose si DFGe < 50 (AIPS Minirin®) ; demi-vie desmopressine 2–3 h ; hydrocortisone 15–25 mg/j.
- Natrémie toutes les 4–6 h à l'hôpital (S5, Society for Endocrinology).

## 16:33 — règle couleur 16:31 appliquée
- .proba → `color:#C8102E;font-weight:700;` (sans halo) dans DX1a/b–DX9 ; contraste.py : 0 élément sur tous. eval.sh : 98,8 % partout, verif_v7 OK.
- Reste : DX.10, SSP/Appel A, captures (1 par DX), RAPPORT, MANIFEST.
- 16:35 charte_v7plus relancé sur DX1–DX9 (fond bleu ciel, #C8102E) ; contraste 0 partout.

## DX.10 — Résistance à la vasopressine (AVP-R) — FAIT (24.10, ~16:50)
- Fichier : LOT_003_DX10_Resistance_vasopressine_AVP_R_AUDITÉ.html (147 259 o), score 98.8 % (hors HUMAIN 100 %), verif_v7 OK, contraste 0.
- Sigles ajoutés à outils_local/sigles_extra.py : AMPc, EP2, EP4, LS, NCC, NICE, V1a.
- Chiffres/doses à vérifier : amiloride 5–10 mg 1–2×/j, indométacine 1,5–2 mg/kg/j, HCTZ 25 mg 1–2×/j (hors AIPS) ; demi-vies amiloride 6–9 h, HCTZ 6–15 h ; rythme NICE CG185 ; réduction de dose lithium (empirique) ; seuil copeptine 21,4 pmol/L (Se/Spé 100 %, étude 2015) ; lithiémie +25–40 % sous thiazide ; thiazide + insuffisance hépatique (AIPS).
- Reste : SSP/Appel A, captures, RAPPORT_AUDIT.md, MANIFEST.sha256.

## Correction transversale Fenske 2018 (S27, vérifié PubMed 30067922) — 24.10 ~17:05
- 144 patients, 11 centres (Suisse, Allemagne, Brésil) : polydipsie primaire 82 (57 %), AVP-D 59 (41 %), AVP-R 3 (2 %).
- DX9 et DX10 inversaient AVP-D et PP (« AVP-D 57 % ») : corrigé et régénéré. DX4 omettait le Brésil : corrigé (« cohorte internationale de 2018 »).
- DX4 : 2.b de nouveau à 2 après correction ; DX10 : OFSP développé à la 1re occurrence (glossaire LS reformulé sans « OFSP »).

## Appel A SSP G3 + bloc 2 — FAIT (24.10, ~17:15), 98,8 % (hors HUMAIN 100 %)
- Fichiers : LOT_003_Appel_A_SSP_G3_Soif_excessive_polydipsie_AUDITÉ_a.html (128 455 o) et _b.html (144 564 o) ; verif_v7 OK ; contraste 0 ; 43 examens cliquables, 43 fenêtres à 2 onglets.
- outils_local/decoupe_l.py : le résumé « SSP G3 · … » est reconnu comme SSP (regex ^SSP(\s+G\d+)?\s*·).
- Bloc 2 aligné sur les 10 monographies de l’Appel B ; AVP-D gestationnelle déplacée en situation particulière ; prévalences en rouge en /100 000 (même unité), répartition Fenske dans un tableau séparé (autre dénominateur).
- À vérifier : Minirin® Melt 60–120 µg au coucher puis 2–3 prises/j, comprimés 0,1–0,2 mg 2–3×/j (AIPS) ; amiloride 5–10 mg 1–2×/j (hors AIPS) ; demi-vie amiloride 6–9 h ; NaCl 3 % 150 mL/20 min (ESE 2014, S62) ; Actrapid® 0,1 U/kg/h (JBDS, S16) ; prévalences : diabète ≈ 6200, MRC ≈ 10 400, IC 1000–2000, bouche sèche ≈ 22 000, Sjögren ≈ 61, HPT primaire 85–233, AVP-D ≈ 4 / 100 000 ; copeptine basale ≥ 21,4 pmol/L (2015), stimulée 4,9 pmol/L (2018).

## Clôture LOT_003 (24.10, ~17:25)
- eval.sh : 11 cours à 98,8 % (hors HUMAIN 100 %), LOT 98,8 % ; verif_v7 OK sur 13 fichiers ; contraste 0 sur 13 fichiers.
- Captures : captures/ (3 vues par fichier via outils/captures3.py ; vues 1–2 absentes pour DX1_b et SSP_b, ancres dans _a).
- Fichiers .fenetres.json orphelins supprimés (DX1 non découpé, SSP non découpé).
- RAPPORT_AUDIT.md et MANIFEST.sha256 écrits. LOT_004 : non commencé.
