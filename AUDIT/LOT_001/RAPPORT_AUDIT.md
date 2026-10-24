# RAPPORT D’AUDIT · LOT_001 (24.10.2026)

Périmètre : 10 DX + Appel A (SSP G1 « Transpiration anormale » et liste du bloc 2). Grille V7 à 14 points ; le point 13.b est HUMAIN, d’où un plafond automatique de 98,8 %.

| Cours | Avant | Après | Fenêtres cliquables / à 2 onglets | Fichier(s) (octets) | Captures (captures/) |
|---|---|---|---|---|---|
| SSP | 87.5 % | 98,8 % | 71 / 71 | LOT_001_Appel_A_SSP_G1_Transpiration_anormale_AUDITÉ_a.html (110 898)<br>LOT_001_Appel_A_SSP_G1_Transpiration_anormale_AUDITÉ_b.html (148 145) | SSP_a_1..3, SSP_a_mobile_1..3, SSP_b_3, SSP_b_mobile_3 |
| DX.1 | 81.2 % | 98,8 % | 59 / 58 | LOT_001_DX1_Syndrome_coronarien_aigu_AUDITÉ.html (194 800) | DX1_1..3, DX1_mobile_1..3 |
| DX.2 | 80.0 % | 98,8 % | 36 / 36 | LOT_001_DX2_Hypoglycemie_AUDITÉ.html (140 644) | DX2_1..3, DX2_mobile_1..3 |
| DX.3 | 63.8 % | 98,8 % | 68 / 67 | LOT_001_DX3_Endocardite_infectieuse_AUDITÉ.html (190 371) | DX3_1..3, DX3_mobile_1..3 |
| DX.4 | 58.8 % | 98,8 % | 26 / 26 | LOT_001_DX4_Hyperhidrose_focale_primaire_AUDITÉ.html (109 362) | DX4_1..3, DX4_mobile_1..3 |
| DX.5 | 61.2 % | 98,8 % | 36 / 36 | LOT_001_DX5_Menopause_symptomes_vasomoteurs_AUDITÉ.html (123 558) | DX5_1..3, DX5_mobile_1..3 |
| DX.6 | 86.2 % | 98,8 % | 107 / 106 | LOT_001_DX6_Hyperthyroidie_AUDITÉ_a.html (157 359)<br>LOT_001_DX6_Hyperthyroidie_AUDITÉ_b.html (187 496) | DX6_1..3, DX6_mobile_1..3 |
| DX.7 | 70.0 % | 98,8 % | 37 / 37 | LOT_001_DX7_Tuberculose_AUDITÉ.html (125 550) | DX7_1..3, DX7_mobile_1..3 |
| DX.8 | 71.2 % | 98,8 % | 37 / 36 | LOT_001_DX8_VIH_AUDITÉ.html (119 673) | DX8_1..3, DX8_mobile_1..3 |
| DX.9 | 67.5 % | 98,8 % | 35 / 35 | LOT_001_DX9_Lymphome_de_Hodgkin_AUDITÉ.html (124 776) | DX9_1..3, DX9_mobile_1..3 |
| DX.10 | 78.8 % | 98,8 % | 33 / 32 | LOT_001_DX10_Pheochromocytome_AUDITÉ.html (107 129) | DX10_1..3, DX10_mobile_1..3 |
| **LOT** | **73,3 %** | **98,8 %** | | | |

verif_v7 : OK sur les 13 fichiers (pas de script, img, CSS externe ni `title=` ; FIN_FICHIER ; glossaire). Toutes les tailles sont entre 90 et 200 Ko ; DX6 et SSP sont découpés en _a/_b (> 198 Ko).

Les fenêtres avec un seul onglet (DX1, DX3, DX6, DX8 et DX10 : 1 chacune) viennent d’un examen de bibliothèque sans texte d’interprétation. L’écart est cosmétique et a été accepté.

Captures : 3 vues bureau + 3 vues mobile (390 px) par DX, dans corriges/LOT_001/captures/. Pour SSP_b, seule la vue 3 existe (en bureau et en mobile), car les ancres 1 et 2 sont dans _a. Des captures d’onglets supplémentaires existent pour DX1 et DX6.

## Règles du 24.10 (15:36) appliquées
- Ordre anatomie → physiologie → physiopathologie → clinique → examens → traitement, le pourquoi d’abord.
- Langage courant + terme exact (glossaire).
- Chiffres sourcés et prévalences comparables.
- Exposant rouge `sup.proba` sur chaque diagnostic, toujours sourcé, jamais inventé.
- Police Atkinson Hyperlegible.
- Captures.

## Modifications des outils partagés (additives, rétrocompatibles)
- outils/decoupe.py : un corrigé AUDITÉ dont le nom contient « appel_a » est découpé comme un Appel A.
- charte_v7plus.py, captures3.py, aide PR(), contrôles verif_v7, correction d’accolade dans mobile.py.
- Ajouts à sigles.py : CR, ESH, EXPeRT, PDE5, PPGL, ASSM, FMH, OFAS, plus la correction de LAGH.
- Nouvelles sources : src_P3b, src_P4a, src_P4b, src_A.

## Remarques
- LOT_1_Appel_A_Validation_et_Audit.html est un méta-document : il n’a pas été audité comme cours. Les fichiers INDEX_TRAVAIL de l’Appel B (1,2 Ko) sont de simples index.
- DX7, source S5 : texte en doublon (cosmétique).
- Les sigles ST et TB restent signalés dans le texte des fenêtres de bibliothèque (déjà le cas dans les DX précédents).

## Chiffres et doses à vérifier
Le détail par DX se trouve dans PROGRESS.md. Ci-dessous, les références ajoutées par l’audit, par fichier :

### LOT_001_Appel_A_SSP_G1_Transpiration_anormale_AUDITÉ_a.html
- [S106] Garmendia Madariaga A et al. The incidence and prevalence of thyroid dysfunction in Europe: a meta-analysis. J Clin Endocrinol Metab 2014;99:923–931.
- [S107] Office fédéral de la santé publique (OFSP). VIH, syphilis, gonorrhée et chlamydiose en Suisse : situation épidémiologique 2023. Bulletin OFSP.
- [S108] OFS et ONEC · Monitorage du cancer en Suisse, lymphome de Hodgkin C81. Moyennes annuelles 2018–2022.
- [S109] Lenders JWM et al. Pheochromocytoma and paraganglioma: an Endocrine Society clinical practice guideline. J Clin Endocrinol Metab 2014;99:1915–1942.
- [S110] Delgado V et al. 2023 ESC Guidelines for the management of endocarditis. Eur Heart J 2023;44:3948–4042.
- [S111] Collet JP et al. 2020 ESC Guidelines for the management of acute coronary syndromes in patients presenting without persistent ST-segment elevation. Eur Heart J 2021;42:1289–1367 (répartition des diagnostics finaux des douleurs thoraciques aiguës).
- [S112] The Menopause Society. The 2023 nonhormone therapy position statement. Menopause 2023;30:573–590.
- [S113] de Jonge P et al. Cross-national epidemiology of panic disorder and panic attacks in the World Mental Health Surveys. Depress Anxiety 2016;33:1155–1177.
- [S114] Marcy TR, Britton ML. Antidepressant-induced sweating. Ann Pharmacother 2005;39:748–752.
- [S115] OFS, NICER, Registre du cancer de l’enfant. Rapport suisse sur le cancer 2021 : lymphomes.

### LOT_001_Appel_A_SSP_G1_Transpiration_anormale_AUDITÉ_b.html
- [S106] Garmendia Madariaga A et al. The incidence and prevalence of thyroid dysfunction in Europe: a meta-analysis. J Clin Endocrinol Metab 2014;99:923–931.
- [S107] Office fédéral de la santé publique (OFSP). VIH, syphilis, gonorrhée et chlamydiose en Suisse : situation épidémiologique 2023. Bulletin OFSP.
- [S108] OFS et ONEC · Monitorage du cancer en Suisse, lymphome de Hodgkin C81. Moyennes annuelles 2018–2022.
- [S109] Lenders JWM et al. Pheochromocytoma and paraganglioma: an Endocrine Society clinical practice guideline. J Clin Endocrinol Metab 2014;99:1915–1942.
- [S110] Delgado V et al. 2023 ESC Guidelines for the management of endocarditis. Eur Heart J 2023;44:3948–4042.
- [S111] Collet JP et al. 2020 ESC Guidelines for the management of acute coronary syndromes in patients presenting without persistent ST-segment elevation. Eur Heart J 2021;42:1289–1367 (répartition des diagnostics finaux des douleurs thoraciques aiguës).
- [S112] The Menopause Society. The 2023 nonhormone therapy position statement. Menopause 2023;30:573–590.
- [S116] Zifodya JS et al. Xpert Ultra versus Xpert MTB/RIF for pulmonary tuberculosis and rifampicin resistance in adults with presumptive pulmonary tuberculosis. Cochrane Database Syst Rev 2021;2:CD009593.
- [S117] Branson BM et al. Laboratory testing for the diagnosis of HIV infection: updated recommendations. CDC et APHL ; 2014.

### LOT_001_DX10_Pheochromocytome_AUDITÉ.html
- [S25] de Jonge P et al. Cross-national epidemiology of panic disorder and panic attacks in the World Mental Health Surveys. Depress Anxiety 2016;33:1155–1177.
- [S26] Garmendia Madariaga A et al. The incidence and prevalence of thyroid dysfunction in Europe: a meta-analysis. J Clin Endocrinol Metab 2014;99:923–931.
- [S27] Office fédéral de la statistique (OFS). Enquête suisse sur la santé 2022 : diabète. Neuchâtel : OFS.
- [S28] The Menopause Society. The 2023 nonhormone therapy position statement. Menopause 2023;30:573–590.
- [S29] Mancia G et al. 2023 ESH Guidelines for the management of arterial hypertension. J Hypertens 2023;41:1874–2071.

### LOT_001_DX1_Syndrome_coronarien_aigu_AUDITÉ.html
- [S55] Visseren FLJ et al. 2021 ESC Guidelines on cardiovascular disease prevention in clinical practice. Eur Heart J. 2021;42:3227–3337. Référence ajoutée lors de l’audit.
- [S56] Office fédéral de la santé publique (OFSP). Plan de vaccination suisse 2026 : vaccination contre la grippe des personnes atteintes de maladies cardiovasculaires. Référence ajoutée lors de l’audit.
- [S57] Collet JP et al. 2020 ESC Guidelines for the management of acute coronary syndromes in patients presenting without persistent ST-segment elevation. Eur Heart J 2021;42:1289–1367 (répartition des diagnostics finaux des douleurs thoraciques aiguës).
- [S58] Erbel R et al. 2014 ESC Guidelines on the diagnosis and treatment of aortic diseases. Eur Heart J 2014;35:2873–2926.
- [S59] Konstantinides SV et al. 2019 ESC Guidelines for the diagnosis and management of acute pulmonary embolism. Eur Heart J 2020;41:543–603.
- [S60] Adler Y et al. 2015 ESC Guidelines for the diagnosis and management of pericardial diseases. Eur Heart J 2015;36:2921–2964.
- [S61] Ghadri JR et al. International Expert Consensus Document on Takotsubo Syndrome (Part I). Eur Heart J 2018;39:2032–2046.
- [S62] Garmendia Madariaga A et al. The incidence and prevalence of thyroid dysfunction in Europe: a meta-analysis. J Clin Endocrinol Metab 2014;99:923–931.
- [S64] Office fédéral de la statistique (OFS). Enquête suisse sur la santé 2022 : diabète déclaré.
- [S63] Lenders JWM et al. Pheochromocytoma and paraganglioma: an Endocrine Society clinical practice guideline. J Clin Endocrinol Metab 2014;99:1915–1942.

### LOT_001_DX2_Hypoglycemie_AUDITÉ.html
- [S55] International Diabetes Federation. IDF Diabetes Atlas, 10e édition, 2021 : région Europe. Référence ajoutée lors de l’audit.
- [S56] American Diabetes Association. Standards of Care in Diabetes 2026, section 6 (Glycemic goals and hypoglycemia) ; International Hypoglycaemia Study Group, Diabetes Care 2017;40:155–157. Référence ajoutée lors de l’audit.
- [S57] Cryer PE et al. Evaluation and management of adult hypoglycemic disorders: an Endocrine Society clinical practice guideline. J Clin Endocrinol Metab. 2009;94:709–728. Référence ajoutée lors de l’audit.
- [S58] Tox Info Suisse. Centre suisse d’information toxicologique, numéro d’urgence 145. Référence ajoutée lors de l’audit.
- [S59] Office fédéral de la santé publique (OFSP). Stratégie nationale Prévention des maladies non transmissibles (MNT) 2017–2028. Référence ajoutée lors de l’audit.
- [S60] Bornstein SR et al. Diagnosis and treatment of primary adrenal insufficiency: an Endocrine Society clinical practice guideline. J Clin Endocrinol Metab 2016;101:364–389.
- [S61] Service FJ et al. Functioning insulinoma: incidence, recurrence, and long-term survival of patients. Mayo Clin Proc 1991;66:711–719.
- [S62] Garmendia Madariaga A et al. The incidence and prevalence of thyroid dysfunction in Europe: a meta-analysis. J Clin Endocrinol Metab 2014;99:923–931.
- [S63] Lenders JWM et al. Pheochromocytoma and paraganglioma: an Endocrine Society clinical practice guideline. J Clin Endocrinol Metab 2014;99:1915–1942.
- [S64] Fiest KM et al. Prevalence and incidence of epilepsy: a systematic review and meta-analysis of international studies. Neurology 2017;88:296–303.

### LOT_001_DX3_Endocardite_infectieuse_AUDITÉ.html
- [S35] OFS, NICER, Registre du cancer de l’enfant. Rapport suisse sur le cancer 2021 : lymphomes.
- [S36] Gouliouris T, Aliyu SH, Brown NM. Spondylodiscitis: update on diagnosis and management. J Antimicrob Chemother 2010;65 Suppl 3:iii11–24.
- [S37] Blomström-Lundqvist C et al. European Heart Rhythm Association international consensus document on how to prevent, diagnose, and treat cardiac implantable electronic device infections. Europace 2020;22:515–549.
- [S38] Rees F, Doherty M, Grainge MJ, Lanyon P, Zhang W. The worldwide incidence and prevalence of systemic lupus erythematosus: a systematic review of epidemiological studies. Rheumatology 2017;56:1945–1961.
- [S39] Reynen K. Cardiac myxomas. N Engl J Med 1995;333:1610–1617.
- [S33] Fedlex. Ordonnance réglant l’admission des personnes et des véhicules à la circulation routière (OAC, RS 741.51), annexe 1 ; LAMal art. 31 (soins dentaires).

### LOT_001_DX4_Hyperhidrose_focale_primaire_AUDITÉ.html
- [S34] Office fédéral de la statistique (OFS). Enquête suisse sur la santé 2022 : diabète.
- [S35] Office fédéral de la santé publique (OFSP). La tuberculose en Suisse : situation épidémiologique (rapport annuel).
- [S36] OFS, NICER, Registre du cancer de l’enfant. Rapport suisse sur le cancer 2021 : lymphomes.
- [S37] Marcy TR, Britton ML. Antidepressant-induced sweating. Ann Pharmacother 2005;39:748–752.
- [S38] Lenders JWM et al. Pheochromocytoma and paraganglioma: an Endocrine Society clinical practice guideline. J Clin Endocrinol Metab 2014;99:1915–1942.

### LOT_001_DX5_Menopause_symptomes_vasomoteurs_AUDITÉ.html
- [S34] Office fédéral de la statistique (OFS). Enquête suisse sur la santé 2022 : diabète.
- [S35] Office fédéral de la santé publique (OFSP). La tuberculose en Suisse : situation épidémiologique (rapport annuel).
- [S36] OFS, NICER, Registre du cancer de l’enfant. Rapport suisse sur le cancer 2021 : lymphomes.
- [S37] Marcy TR, Britton ML. Antidepressant-induced sweating. Ann Pharmacother 2005;39:748–752.
- [S38] Lenders JWM et al. Pheochromocytoma and paraganglioma: an Endocrine Society clinical practice guideline. J Clin Endocrinol Metab 2014;99:1915–1942.
- [S39] The Menopause Society. The 2023 nonhormone therapy position statement. Menopause 2023;30:573–590.
- [S40] Avis NE et al. Duration of menopausal vasomotor symptoms over the menopause transition (SWAN). JAMA Intern Med 2015;175:531–539.
- [S41] de Jonge P et al. Cross-national epidemiology of panic disorder and panic attacks in the World Mental Health Surveys. Depress Anxiety 2016;33:1155–1177.
- [S42] Harlow SD et al. Executive summary of the Stages of Reproductive Aging Workshop + 10 (STRAW+10). Menopause 2012;19:387–395.

### LOT_001_DX6_Hyperthyroidie_AUDITÉ_a.html
- [S23] Biondi B et al. 2015 European Thyroid Association Guidelines on Diagnosis and Treatment of Endogenous Subclinical Hyperthyroidism. Eur Thyroid J. 2015;4:149–163. Référence ajoutée lors de l’audit.
- [S24] Bartalena L et al. 2018 European Thyroid Association Guidelines for the Management of Amiodarone-Associated Thyroid Dysfunction. Eur Thyroid J. 2018;7:55–66. Référence ajoutée lors de l’audit.
- [S25] Bartalena L et al. The 2021 European Group on Graves’ Orbitopathy (EUGOGO) Clinical Practice Guidelines for the Medical Management of Graves’ Orbitopathy. Eur J Endocrinol. 2021;185:G43–G67. Référence ajoutée lors de l’audit.
- [S27] Akamizu T et al. Diagnostic criteria, clinical features, and incidence of thyroid storm based on nationwide surveys. Thyroid. 2012;22:661–679. Référence ajoutée lors de l’audit.
- [S28] Burch HB, Wartofsky L. Life-threatening thyrotoxicosis: thyroid storm. Endocrinol Metab Clin North Am. 1993;22:263–277. Référence ajoutée lors de l’audit.
- [S31] Taylor PN et al. Global epidemiology of hyperthyroidism and hypothyroidism. Nat Rev Endocrinol. 2018;14:301–316. Référence ajoutée lors de l’audit.
- [S32] Mourits MP et al. Clinical activity score as a guide in the management of patients with Graves’ ophthalmopathy. Clin Endocrinol. 1997;47:9–14. Référence ajoutée lors de l’audit.
- [S33] U.S. Food and Drug Administration. Safety communication: biotin (vitamin B7) can interfere with laboratory tests, 2017, mise à jour 2019. Référence ajoutée lors de l’audit.
- [S34] Rudd KE et al. Global, regional, and national sepsis incidence and mortality, 1990–2017. Lancet 2020;395:200–211.
- [S35] Lenders JWM et al. Pheochromocytoma and paraganglioma: an Endocrine Society clinical practice guideline. J Clin Endocrinol Metab 2014;99:1915–1942.
- [S36] de Jonge P et al. Cross-national epidemiology of panic disorder and panic attacks in the World Mental Health Surveys. Depress Anxiety 2016;33:1155–1177.
- [S37] The Menopause Society. The 2023 nonhormone therapy position statement. Menopause 2023;30:573–590.

### LOT_001_DX6_Hyperthyroidie_AUDITÉ_b.html
- [S24] Bartalena L et al. 2018 European Thyroid Association Guidelines for the Management of Amiodarone-Associated Thyroid Dysfunction. Eur Thyroid J. 2018;7:55–66. Référence ajoutée lors de l’audit.
- [S25] Bartalena L et al. The 2021 European Group on Graves’ Orbitopathy (EUGOGO) Clinical Practice Guidelines for the Medical Management of Graves’ Orbitopathy. Eur J Endocrinol. 2021;185:G43–G67. Référence ajoutée lors de l’audit.
- [S26] Alexander EK et al. 2017 Guidelines of the American Thyroid Association for the Diagnosis and Management of Thyroid Disease During Pregnancy and the Postpartum. Thyroid. 2017;27:315–389. Référence ajoutée lors de l’audit.
- [S29] Russ G et al. European Thyroid Association Guidelines for Ultrasound Malignancy Risk Stratification of Thyroid Nodules in Adults: the EU-TIRADS. Eur Thyroid J. 2017;6:225–237. Référence ajoutée lors de l’audit.
- [S30] Marcocci C et al. Selenium and the course of mild Graves’ orbitopathy. N Engl J Med. 2011;364:1920–1931. Référence ajoutée lors de l’audit.
- [S32] Mourits MP et al. Clinical activity score as a guide in the management of patients with Graves’ ophthalmopathy. Clin Endocrinol. 1997;47:9–14. Référence ajoutée lors de l’audit.
- [S33] U.S. Food and Drug Administration. Safety communication: biotin (vitamin B7) can interfere with laboratory tests, 2017, mise à jour 2019. Référence ajoutée lors de l’audit.

### LOT_001_DX7_Tuberculose_AUDITÉ.html
- [S29] OFS, NICER, Registre du cancer de l’enfant. Rapport suisse sur le cancer 2021.
- [S30] Office fédéral de la santé publique (OFSP). VIH, syphilis, gonorrhée et chlamydiose en Suisse : situation épidémiologique 2023. Bulletin OFSP.
- [S31] Delgado V et al. 2023 ESC Guidelines for the management of endocarditis. Eur Heart J 2023;44:3948–4042.
- [S32] Grunewald J et al. Sarcoidosis. Nat Rev Dis Primers 2019;5:45.
- [S33] Garmendia Madariaga A et al. The incidence and prevalence of thyroid dysfunction in Europe: a meta-analysis. J Clin Endocrinol Metab 2014;99:923–931.
- [S34] Zifodya JS et al. Xpert Ultra versus Xpert MTB/RIF for pulmonary tuberculosis and rifampicin resistance in adults with presumptive pulmonary tuberculosis. Cochrane Database Syst Rev 2021;2:CD009593.
- [S35] Steingart KR et al. Sputum processing methods to improve the sensitivity of smear microscopy for tuberculosis: a systematic review. Lancet Infect Dis 2006;6:664–674.

### LOT_001_DX8_VIH_AUDITÉ.html
- [S22] European Centre for Disease Prevention and Control (ECDC), OMS Europe. HIV/AIDS surveillance in Europe 2024 – 2023 data. Stockholm : ECDC ; 2024.
- [S23] Garmendia Madariaga A et al. The incidence and prevalence of thyroid dysfunction in Europe: a meta-analysis. J Clin Endocrinol Metab 2014;99:923–931.
- [S24] OFS, NICER, Registre du cancer de l’enfant. Rapport suisse sur le cancer 2021.
- [S25] Delgado V et al. 2023 ESC Guidelines for the management of endocarditis. Eur Heart J 2023;44:3948–4042.
- [S26] OFSP · Tuberculose en Suisse et au Liechtenstein en 2025. Bulletin du 21 septembre 2026. Référence ajoutée lors de l’audit du 24 octobre 2026 (source du cours DX.7).
- [S27] Branson BM et al. Laboratory testing for the diagnosis of HIV infection: updated recommendations. CDC and APHL ; 2014.

### LOT_001_DX9_Lymphome_de_Hodgkin_AUDITÉ.html
- [S14] OFSP · Tuberculose en Suisse et au Liechtenstein en 2025. Bulletin du 21 septembre 2026. Référence ajoutée lors de l’audit du 24 octobre 2026 (source du cours DX.7).
- [S15] Office fédéral de la santé publique (OFSP). VIH, syphilis, gonorrhée et chlamydiose en Suisse : situation épidémiologique 2023. Bulletin OFSP.
- [S16] Garmendia Madariaga A et al. The incidence and prevalence of thyroid dysfunction in Europe: a meta-analysis. J Clin Endocrinol Metab 2014;99:923–931.
- [S17] Grunewald J et al. Sarcoidosis. Nat Rev Dis Primers 2019;5:45.


## Sécurité
- Aucune écriture sur Drive, aucun push GitHub : tout le travail est local, sous /workspace/audit_1_10.
- Le dossier Drive privé 1sY8ed56jWj1su0imvX-dk6mVb_sGTFoB n’a jamais été ouvert, listé ni lu.
- **Contenu non validé cliniquement** : une relecture médicale humaine est requise (point 13.b et chiffres ci-dessus).
