# JOURNAL — LOT_016 — DX.9 Anorexie mentale

- 2026-10-30 — Rédaction de `LOT_016_Phase_B_V0_DX.9.html` (rédacteur Phase B). Titre `<h2>` repris mot pour mot de `LISTE_DX_CANONIQUE.md` : « DX.9 — Anorexie mentale ». Corrections d'audit héritées : 2 (cortisol et ACTH avant l'hydrocortisone, renvoi DX.10), 5 et 6 (thiamine hors information professionnelle, numéros par forme), 8 (LS Benerva), 9 (OPAS jusqu'au 31.12.2026, LiMA dès le 1.1.2027), 10 (GLIM 2024 : inflammation non remplie sans biologie), 12 (hyponatrémie, TSH), 17 (aucun méta-terme).
- Hypothèse (rangs E) : la monographie garde les rangs de la Phase A ; DX.9 est E3. Le point 4 place E1 (Addison) et E2 (diabète) avant l'instabilité propre de l'anorexie mentale, car ces deux urgences la miment.
- Hypothèse (renutrition) : le consensus suisse Friedli 2018 (Reber 2019) exclut les troubles alimentaires ; la grille MEED est spécifique. Le fichier présente les deux schémas et écrit la divergence sans trancher (HELP H16-DX9-03).
- Hypothèse (sources) : aucune recommandation suisse propre à l'anorexie mentale n'a été trouvée ; ordre retenu : OFSP, Revue Médicale Suisse (CHUV), Université de Fribourg, Fedlex, ASSM, AIPS, puis MEED (Royaume-Uni), NICE NG69, HAS 2010 (page HAS : validée le 1.6.2010, aucune version plus récente visible le 30.10.2026), WFSBP 2023. Méta-analyse américaine Kutz 2020 citée seulement en complément de Botella 2013 (Espagne).
- Doses : AIPS lues dans les documents liés au XML local et mises en cache : 63180, 52780 (lu, non cité), 36360, 45726, 53929, 09395, 29550, 41181 ; 53709, 45880 et 10989 déjà en cache. Magnesiocard® 2,5 comprimés = 45730 (LS : AMM 45730077). Zyprexa® comprimés filmés = 53709, Velotab = 55311. Aucune dose d'olanzapine pour l'anorexie mentale (hors information professionnelle, HELP H16-DX9-06).
- Remboursement : API publique LS lue le 30.10.2026 (Phoscap 1.11.2015 ; KCl Retard 15.3.1972 ; Magnesiocard 2,5 1.2.2023 ; Calcimagon-D3 et Vi-De 3 avec limitation ; Zyprexa sans limitation ; Kaliumphosphat : 0 résultat).
- Droit : Code civil, état 1.7.2026 ; art. 16, 19c, 377–380, 426–429, 433–435, 439 comparés automatiquement à la version du 1.1.2027 : identiques.
- Taille : 131 041 octets à la remise (SHA-256 6f02ed5fd03f66cdef0bc80d100162c9277a70f0d36cb6ff5f3f5b303e242988) (au-dessus de la cible 110–125 Ko, sous le seuil de compression de 135 Ko) ; densité due aux citations AIPS complètes (contre-indications, grossesse, allaitement) de onze spécialités. Contrôle `controle_lot.py verifier --sans-nom` : 0 critique, 0 avertissement. Contrôle des 128 citations « … » par script contre `evidence/` et `.cache/aips/` : 126 retrouvées ; 2 écarts de mise en page (exposant « 3e » de l'AIPS Zyprexa ; tableau à colonnes de l'annexe 1 OPAS, phrase confirmée par la correction d'audit 9).

## Extraits ajoutés dans `evidence/` (correspondance avec les [Sn] du fichier DX.9)

| [Sn] DX.9 | Fichier `evidence/` |
|---|---|
| S1 | S01 (Phase A) |
| S2 | S13 (Phase A) + DX9_S2_OMS_CDDR2024_6B80_complet.txt |
| S3 | S14 (Phase A) |
| S4 | DX9_S4_OFSP_troubles_alimentaires_prevalence_2012.txt |
| S5 | DX9_S5_OFSP_SSPH2022_COVID_TCA.txt |
| S6 | DX9_S6_RMS2016_Helfer_CHUV_anorexie_somatique.txt |
| S7 | DX9_S7_Wyssen2019_SZPN_S3_Essstoerungen_CH.txt |
| S8, S9, S10, S16 | DX9_S8_S9_S10_S16_resumes_EuropePMC.txt |
| S11 | S15 (Phase A) + DX9_S11_MEED2022-2025_tableaux_renutrition.txt |
| S12 | DX9_S12_NICE_NG69_anorexie_mentale.txt |
| S13 | DX9_S13_HAS2010_anorexie_mentale_fiches_1-3.txt |
| S14 | S16 (Phase A) + DX9_S14_Reber2019_perimetre_Friedli2018.txt |
| S15 | DX9_S15_WFSBP2023_olanzapine_resume.txt |
| S17, S19–S22 | DX9_AIPS_Zyprexa_Phoscap_K_Mg_Ca-D_glucose_NaCl.txt (+ `.cache/aips/<numéro>.txt`) |
| S18 | S27 (Phase A) |
| S23 | DX9_LS_OFSP_liste_specialites.txt |
| S24 | DX9_Fedlex_CC_16_19c_377-380_426-439.txt |
| S25 | DX9_ASSM_PHC2018_mesures_de_contrainte.txt |
| S26 | DX9_Fedlex_OPAS_9b_11b_OAMal_71a_71d.txt (+ S28 Phase A) |
| S27 | S28 (Phase A) + DX9_LiMA2027_chap36_GESKES2026_anorexie.txt |
| S28, S29, S30 | S17, S18, S19 (Phase A) |
| S31 | S25 (Phase A) + DX9_S31_Oksnes2024_hyponatremie_cas1.txt |
| S32 | S03 (Phase A) + DX9_GLIM2024_ESPEN_fiche_inflammation.txt |
