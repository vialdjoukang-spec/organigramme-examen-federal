# RAPPORT D’AUDIT · LOT_005 (24.10.2026)

Périmètre : Appel A (SSP G5 « Sensation de maladie, malaise général » et liste des dix DX du bloc 2) et Appel B, parties 1–4 (DX.1 à DX.10). Grille V7 à 14 points ; le point 13.b est HUMAIN, d’où un plafond automatique de 98,8 % (100 % hors HUMAIN pour chaque fichier).

Originaux (non modifiés) : originaux/LOT_005. Corrigés : corriges/LOT_005. Générateurs reproductibles : source/gen_*.py (+ source/lot5_commun.py, source/outils_local/).

| Cours | Avant (score V7) | Après | Examens : avant (cliquables/mentions) → après (cliquables/à 2 onglets) | Phrases creuses | Phrases > 30 mots | Sigles non développés | Probabilités rouges (`sup.proba`) | Fichier(s) (octets) |
|---|---|---|---|---|---|---|---|---|
| SSP | 37,5 % | 98,8 % | 0/50 → 83/83 | 0 | 0 | 0 | 20 | LOT_005_Appel_A_SSP_G5_Sensation_de_maladie_AUDITÉ_a.html (122 999)<br>LOT_005_Appel_A_SSP_G5_Sensation_de_maladie_AUDITÉ_b.html (169 199) |
| DX.1 | 33,8 % | 98,8 % | 1/11 → 55/55 | 1 | 0 | 0 | 7 | LOT_005_DX1_Infections_virales_syndrome_grippal_AUDITÉ.html (156 941) |
| DX.2 | 35,0 % | 98,8 % | 0/23 → 25/25 | 0 | 0 | 0 | 4 | LOT_005_DX2_Malaise_iatrogene_medicamenteux_AUDITÉ.html (124 162) |
| DX.3 | 33,8 % | 98,8 % | 0/19 → 35/35 | 0 | 0 | 0 | 5 | LOT_005_DX3_Panique_et_trouble_somatique_AUDITÉ.html (125 400) |
| DX.4 | 30,0 % | 98,8 % | 1/76 → 37/37 | 0 | 0 | 0 | 3 | LOT_005_DX4_Troubles_metaboliques_electrolytiques_AUDITÉ.html (158 389) |
| DX.5 | 27,5 % | 98,8 % | 0/33 → 50/50 | 0 | 0 | 0 | 6 | LOT_005_DX5_Sepsis_occulte_AUDITÉ.html (141 852) |
| DX.6 | 41,2 % | 98,8 % | 0/75 → 43/43 | 0 | 0 | 0 | 5 | LOT_005_DX6_SCA_atypique_AUDITÉ.html (135 359) |
| DX.7 | non noté (DX.7 non découpé dans le diagnostic) | 98,8 % | — → 30/30 | 0 | 0 | 0 | 3 | LOT_005_DX7_PPR_Horton_lupus_AUDITÉ.html (106 322) |
| DX.8 | 27,5 % | 98,8 % | 0/13 → 33/33 | 0 | 0 | 0 | 4 | LOT_005_DX8_Delirium_et_glissement_AUDITÉ.html (112 187) |
| DX.9 | 31,2 % | 98,8 % | 0/53 → 40/40 | 0 | 0 | 0 | 4 | LOT_005_DX9_Endocardite_subaigue_AUDITÉ.html (120 652) |
| DX.10 | 26,2 % | 98,8 % | 0/19 → 33/33 | 0 | 0 | 0 | 4 | LOT_005_DX10_Intoxication_CO_gaz_AUDITÉ.html (136 320) |
| **LOT** | **32,4 %** | **98,8 %** | 0 fenêtre à 2 onglets avant | | | | | |

Avant : 0 fenêtre à 2 onglets dans tout le lot et aucune source citée dans l’original.

## Contrôles
- verif_v7 : OK sur les 12 fichiers. Ils ne contiennent ni script, ni img, ni CSS externe, ni `title=`. Chaque fichier a son marqueur FIN_FICHIER, son glossaire des sigles et la mention « contenu produit par IA, non validé cliniquement ».
- Taille : toutes entre 90 et 200 Ko. Le SSP (≈ 292 Ko d’un bloc) est découpé en _a / _b.
- contraste.py : 0 élément sur les 12 fichiers, .proba comprise.
- Charte : règles du 24.10, 16:31–16:32. `.proba` est en `#C8102E`, gras, sans halo, sur fond bleu ciel pâle, via charte_v7plus.py relancé sur chaque fichier. La police est Atkinson Hyperlegible.
- Exigence V7 : 100 % des examens cliquables ouvrent une fenêtre à 2 onglets (Principe / Interprétation) sans JavaScript. Les captures de contrôle le confirment.
- Captures : `captures/<DX>_ctrl_principe.png` et `_ctrl_interpretation.png` pour DX1–DX10 et SSP_a, prises avec les nouvelles couleurs. Les anciennes captures DX*_1..3 datent d’avant le changement de couleur.
- MANIFEST.sha256 : sha256 des 12 fichiers AUDITÉ ; `sha256sum -c MANIFEST.sha256` OK.

## Corrections de fond apportées aux originaux (signalées dans le texte)
- **SSP :**
  - Les chiffres SSMIG non sourcés (8–15 %, > 20 %, > 30 %) sont remplacés par l’étude bâloise BANC : 13,5 % des patients non traumatiques ESI 2–3, âge médian 82 ans, affection grave à 30 jours chez 59 %, mortalité à 30 jours de 6 %.
  - La cinétique de la PCT non sourcée et l’affirmation « > 90 % » sur suPAR / MR-proADM sont supprimées.
  - Les pourcentages V5 des 10 DX sont remplacés par le chiffre publié de chaque DX. Le sous-tableau en « même unité » est exprimé pour 100 000 habitants et par an, avec une réserve explicite.
- **DX1 :** la dose rénale de Tamiflu® est corrigée (l’original indiquait 75 mg 1 fois par jour).
- **DX4 :** le glucose associé à l’insuline est corrigé. L’original indiquait 500 mL de glucose à 20 %, soit 100 g ; le corrigé indique 25 g, selon UK Kidney Association.
- **DX6 :** l’aspirine IV est corrigée à 75–250 mg (l’original indiquait 250–300 mg).
- **DX10 :**
  - SpCO : sensibilité 0,77 et spécificité 0,83 (Papin 2023). La CO-oxymétrie est l’examen de référence.
  - Il n’existe pas de score de société savante ; les critères retenus sont exposition + symptômes + HbCO.
  - OHB : délai « idéalement dans les 6 h » signalé comme repère d’expert, à vérifier.

## Chiffres et doses à faire vérifier par un médecin
### Doses (AIPS Swissmedic / recommandations citées ; à contrôler avant tout usage)
- **DX1 :**
  - oséltamivir 75 mg 2×/j pendant 5 j, et 30 mg 2×/j si DFGe réduit ;
  - baloxavir 40 mg (40–79 kg) ou 80 mg (≥ 80 kg) en dose unique ;
  - nirmatrelvir/ritonavir 300/100 mg 2×/j pendant 5 j, et 150/100 mg si DFGe 30–60 ;
  - paracétamol 500–1000 mg toutes les 6–8 h, maximum 4 g/j ;
  - ibuprofène 400 mg 3×/j pendant 3 j au maximum.
- **DX2 :**
  - lorazépam 1–2,5 mg per os ;
  - NaCl 3 % 150 mL en 20 min ;
  - cyproheptadine 12 mg puis 2 mg toutes les 2 h (hors AIPS, Boyer) ;
  - fluoxétine 10–20 mg/j en relais (hors AIPS) ;
  - magnésium 2 g IV pour une torsade de pointes (ERC 2021).
- **DX3 :**
  - escitalopram 5 mg puis 10 mg, maximum 20 mg (10 mg au maximum si ≥ 65 ans) ;
  - sertraline 25 mg puis 50 mg, maximum 200 mg ;
  - lorazépam 1 mg pour une crise invalidante.
- **DX4 :**
  - insuline rapide 10 U IV + 25 g de glucose ;
  - salbutamol 10–20 mg en nébulisation ;
  - gluconate de calcium 10 % 30 mL IV en 5–10 min ;
  - zolédronate 4 mg IV en ≥ 15 min ;
  - dénosumab 120 mg SC ;
  - calcitonine 4 UI/kg toutes les 12 h pendant 48 h au maximum ;
  - NaCl 3 % 150 mL (enfant : 2 mL/kg) ;
  - restriction hydrique < 800 mL/j.
- **DX5 et SSP :**
  - ceftriaxone 2 g IV/j (méningite : 2 g toutes les 12 h) ;
  - co-amoxicilline 2,2 g IV toutes les 8 h ;
  - pipéracilline-tazobactam 4,5 g IV toutes les 6–8 h ;
  - cristalloïdes 30 mL/kg en 3 h ;
  - hydrocortisone 200 mg/j ;
  - seuils de noradrénaline (0,1 et 0,25 µg/kg/min).
- **DX6 :**
  - aspirine : charge de 150–300 mg per os ou 75–250 mg IV, puis 75–100 mg/j ;
  - ticagrélor 180 mg puis 90 mg 2×/j ;
  - prasugrel 60 mg puis 10 mg/j (5 mg si ≥ 75 ans ou < 60 kg) ;
  - HNF 70–100 UI/kg ;
  - atorvastatine 40–80 mg.
- **DX7 :**
  - prednisone : 40–60 mg/j dans l’ACG, puis 15–20 mg/j à 2–3 mois et ≤ 5 mg/j à 1 an ; 12,5–25 mg/j dans la PPR ;
  - méthylprednisolone 250–1000 mg/j IV pendant 3 j en cas de menace visuelle ;
  - tocilizumab 162 mg SC par semaine ;
  - hydroxychloroquine ≤ 5 mg/kg/j.
- **DX8 :** halopéridol 0,5 mg ; quétiapine 12,5–25 mg (hors AIPS).
- **DX9 :**
  - flucloxacilline 12 g/j IV pendant 4–6 semaines ;
  - ceftriaxone 2 g/j ;
  - gentamicine 3 mg/kg/j ;
  - rifampicine 900 mg/j en 3 doses (prothèse) ;
  - amoxicilline 2 g per os en prophylaxie dentaire ;
  - 3 paires d’hémocultures.
- **DX10 :**
  - O2 normobare 12–15 L/min pendant environ 12 h ;
  - OHB « idéalement dans les 6 h » (repère d’expert, non trouvé dans ECHM 2016) ;
  - hydroxocobalamine (Cyanokit®) 5 g IV en 15 min, plus 5 g selon la gravité ;
  - interactions avec l’OHB (bléomycine, doxorubicine, cisplatine) non vérifiées dans les sources citées.

### Chiffres et références signalés dans le texte
- Papin M et al., Eur J Emerg Med 2023 (méta-analyse SpCO) : liste complète des auteurs et pagination à vérifier.
- Seuils de procalcitonine (algorithmes de Schuetz) et rythme de contrôle « tous les 2–3 jours sous antibiotique » (pratique courante, non chiffré explicitement dans S117).
- Sources ajoutées par l’audit mais non rouvertes (mention « à vérifier » dans chaque fichier) :
  - [S1] Swissmedic. Information professionnelle des médicaments autorisés en Suisse (AIPS), swissmedicinfo.ch : Dafalgan®, Irfen®, Tamiflu®, Xofluza®, Paxlovid®, Rocephin®, Co-Amoxi-Mepha®, Tazobac®, Temesta®, Cipralex®, Zoloft®, Zometa®, Brilique®, Efient®, Aspirin Cardio®, Clexane®, Seroquel®, Haldol®, Spiricort®, RoActemra®, Plaquenil®, Calcium Sandoz®, Actrapid®, Resonium®.
  - [S3] Office fédéral de la santé publique (OFSP), Commission fédérale pour les vaccinations (CFV). Plan de vaccination suisse 2025.
  - [S4] Singer M, Deutschman CS, Seymour CW et al. The Third International Consensus Definitions for Sepsis and Septic Shock (Sepsis-3). JAMA 2016;315:801–810.
  - [S5] Evans L, Rhodes A, Alhazzani W et al. Surviving Sepsis Campaign: international guidelines for management of sepsis and septic shock 2021. Intensive Care Med 2021;47:1181–1247.
  - [S6] Royal College of Physicians. National Early Warning Score (NEWS) 2. Londres, 2017.
  - [S7] Lim WS, van der Eerden MM, Laing R et al. Defining community acquired pneumonia severity on presentation to hospital (CURB-65). Thorax 2003;58:377–382.
  - [S8] Organisation mondiale de la santé (OMS). Influenza (seasonal) : aide-mémoire, 2023.
  - [S9] Byrne RA, Rossello X, Coughlan JJ et al. 2023 ESC Guidelines for the management of acute coronary syndromes. Eur Heart J 2023;44:3720–3826.
  - [S10] Thygesen K, Alpert JS, Jaffe AS et al. Fourth Universal Definition of Myocardial Infarction (2018). Eur Heart J 2019;40:237–269.
  - [S12] Spasovski G, Vanholder R, Allolio B et al. Clinical practice guideline on diagnosis and treatment of hyponatraemia (ESE, ESICM, ERA-EDTA). Eur J Endocrinol 2014;170:G1–G47.
  - [S13] Lott C, Truhlář A, Alfonzo A et al. European Resuscitation Council Guidelines 2021: cardiac arrest in special circumstances (hyperkaliémie, hypothermie, intoxications). Resuscitation 2021;161:152–219.
  - [S14] Weaver LK. Carbon monoxide poisoning. N Engl J Med 2009;360:1217–1225.
  - [S15] Tox Info Suisse. Rapport annuel (cas d’intoxication annoncés en Suisse) ; numéro d’urgence 145. toxinfo.ch.
  - [S16] Inouye SK, Westendorp RG, Saczynski JS. Delirium in elderly people. Lancet 2014;383:911–922.
  - [S18] American Psychiatric Association. Diagnostic and Statistical Manual of Mental Disorders, 5e édition, texte révisé (DSM-5-TR). 2022.
  - [S19] Spitzer RL, Kroenke K, Williams JB, Löwe B. A brief measure for assessing generalized anxiety disorder: the GAD-7. Arch Intern Med 2006;166:1092–1097.
  - [S20] Keck ME, Ropohl A, Bondolfi G et al. Die Behandlung der Angsterkrankungen (recommandations de la Société suisse des troubles anxieux et de la dépression, SSAD). Swiss Med Forum 2011;11:558–566 et 586–591.
  - [S21] Dunkley EJC, Isbister GK, Sibbritt D et al. The Hunter Serotonin Toxicity Criteria. QJM 2003;96:635–642.
  - [S22] Naranjo CA, Busto U, Sellers EM et al. A method for estimating the probability of adverse drug reactions. Clin Pharmacol Ther 1981;30:239–245.
  - [S23] O’Mahony D, Cherubini A, Guiteras AR et al. STOPP/START criteria for potentially inappropriate prescribing in older people: version 3. Eur Geriatr Med 2023;14:625–632.
  - [S24] Loi fédérale sur les médicaments et les dispositifs médicaux (LPTh, RS 812.21), art. 59 (obligation d’annoncer les effets indésirables) ; Swissmedic, portail d’annonce ElViS. fedlex.admin.ch.
  - [S25] Horowitz MA, Taylor D. Tapering of SSRI treatment to mitigate withdrawal symptoms. Lancet Psychiatry 2019;6:538–546.
  - [S27] Hellmich B, Agueda A, Monti S et al. 2018 Update of the EULAR recommendations for the management of large vessel vasculitis. Ann Rheum Dis 2020;79:19–30.
  - [S28] Dejaco C, Singh YP, Perel P et al. 2015 Recommendations for the management of polymyalgia rheumatica: a EULAR/ACR collaborative initiative. Ann Rheum Dis 2015;74:1799–1807.
  - [S29] Dasgupta B, Cimmino MA, Maradit-Kremers H et al. 2012 provisional classification criteria for polymyalgia rheumatica: a EULAR/ACR collaborative initiative. Ann Rheum Dis 2012;71:484–492.
  - [S30] Aringer M, Costenbader K, Daikh D et al. 2019 EULAR/ACR classification criteria for systemic lupus erythematosus. Ann Rheum Dis 2019;78:1151–1159.
  - [S31] Fanouriakis A, Kostopoulou M, Andersen J et al. EULAR recommendations for the management of systemic lupus erythematosus: 2023 update. Ann Rheum Dis 2024;83:15–29.
  - [S32] Dejaco C, Ramiro S, Bond M et al. EULAR recommendations for the use of imaging in large vessel vasculitis in clinical practice: 2023 update. Ann Rheum Dis 2024;83:741–751.
  - [S34] Rudd KE, Johnson SC, Agesa KM et al. Global, regional, and national sepsis incidence and mortality, 1990–2017. Lancet 2020;395:200–211.
  - [S35] Société suisse d’infectiologie (SSI). Recommandations : infections urinaires, pneumonie communautaire, sepsis (ssi.guidelines.ch).
  - [S38] Inouye SK, van Dyck CH, Alessi CA et al. Clarifying confusion: the Confusion Assessment Method. Ann Intern Med 1990;113:941–948.
  - [S40] Rockwood K, Song X, MacKnight C et al. A global clinical measure of fitness and frailty in elderly people (Clinical Frailty Scale). CMAJ 2005;173:489–495.
  - [S41] smarter medicine – Choosing Wisely Switzerland. Listes « Top 5 » de la Société suisse de médecine interne générale (SSMIG), ambulatoire et hospitalière. smartermedicine.ch.
  - [S42] Pirmohamed M, James S, Meakin S et al. Adverse drug reactions as cause of admission to hospital: prospective analysis of 18 820 patients. BMJ 2004;329:15–19.
  - [S43] Boyer EW, Shannon M. The serotonin syndrome. N Engl J Med 2005;352:1112–1120.
  - [S44] Upadhyay A, Jaber BL, Madias NE. Incidence and prevalence of hyponatremia. Am J Med 2006;119(7 Suppl 1):S30–S35.
  - [S45] El-Hajj Fuleihan G, Clines GA, Hu MI et al. Treatment of hypercalcemia of malignancy in adults: an Endocrine Society clinical practice guideline. J Clin Endocrinol Metab 2023;108:507–528.
  - [S47] Kessler RC, Chiu WT, Jin R et al. The epidemiology of panic attacks, panic disorder, and agoraphobia in the National Comorbidity Survey Replication. Arch Gen Psychiatry 2006;63:415–424.
  - [S48] Schuler D, Tuch A, Peter C. La santé psychique en Suisse. Monitoring 2020 (rapport Obsan 15/2020). Neuchâtel : Observatoire suisse de la santé.
  - [S49] Hampson NB, Piantadosi CA, Thom SR, Weaver LK. Practice recommendations in the diagnosis, management, and prevention of carbon monoxide poisoning. Am J Respir Crit Care Med 2012;186:1095–1101.
  - [S50] Weaver LK, Hopkins RO, Chan KJ et al. Hyperbaric oxygen for acute carbon monoxide poisoning. N Engl J Med 2002;347:1057–1067.
  - [S53] Six AJ, Backus BE, Kelder JC. Chest pain in the emergency room: value of the HEART score. Neth Heart J 2008;16:191–196.
  - [S54] Kroenke K, Spitzer RL, Williams JB. The PHQ-15: validity of a new measure for evaluating the severity of somatic symptoms. Psychosom Med 2002;64:258–266.
  - [S55] Comité d’experts en médecine des voyages (CEMV) et OFSP. Prévention et prise en charge du paludisme chez les voyageurs (healthytravel.ch).
  - [S56] Office fédéral de la statistique (OFS). Causes de décès en Suisse, statistique annuelle. bfs.admin.ch.
  - [S57] Kellum JA, Lameire N et al. KDIGO Clinical Practice Guideline for Acute Kidney Injury. Kidney Int Suppl 2012;2:1–138.
  - [S58] Hoorn EJ, Zietse R. Diagnosis and treatment of hyponatremia: compilation of the guidelines. J Am Soc Nephrol 2017;28:1340–1349.
  - [S59] Fédération des médecins suisses (FMH) / Ordonnance réglant l’admission à la circulation routière (OAC, RS 741.51), annexe 1 : exigences médicales minimales pour la conduite. fedlex.admin.ch.
  - [S60] Loi fédérale sur l’assurance-maladie (LAMal, RS 832.10), art. 25 ; Loi fédérale sur l’assurance-accidents (LAA, RS 832.20) ; Loi fédérale sur l’assurance-invalidité (LAI, RS 831.20). fedlex.admin.ch.
  - [S61] Code des obligations (CO, RS 220), art. 324a (salaire en cas d’empêchement de travailler) ; certificat d’incapacité de travail selon la FMH.
  - [S62] Wilson JMG, Jungner G (OMS) et Swiss Medical Board : principes du dépistage ; OFSP, stratégie nationale de prévention des maladies non transmissibles (MNT) 2017–2028.
  - [S64] Allgöwer M, Burri C. « Schockindex ». Dtsch Med Wochenschr 1967;92:1947–1950 (indice de choc = fréquence cardiaque / pression systolique).
  - [S65] Chartrand C, Leeflang MM, Minion J et al. Accuracy of rapid influenza diagnostic tests: a meta-analysis. Ann Intern Med 2012;156:500–511.
  - [S66] Merckx J, Wali R, Schiller I et al. Diagnostic accuracy of novel and traditional rapid tests for influenza infection compared with RT-PCR: a systematic review and meta-analysis. Ann Intern Med 2017;167:394–409.
  - [S67] Torres A, Peetermans WE, Viegi G, Blasi F. Risk factors for community-acquired pneumonia in adults in Europe: a literature review. Thorax 2013;68:1057–1065.
  - [S72] Henssler J, Schmidt Y, Schmidt U et al. Incidence of antidepressant discontinuation symptoms: a systematic review and meta-analysis. Lancet Psychiatry 2024;11:526–535.
  - [S73] Jacob S, Spinler SA. Hyponatremia associated with selective serotonin-reuptake inhibitors in older adults. Ann Pharmacother 2006;40:1618–1622.
  - [S74] Zeppenfeld K, Tfelt-Hansen J, de Riva M et al. 2022 ESC Guidelines for the management of patients with ventricular arrhythmias and the prevention of sudden cardiac death. Eur Heart J 2022;43:3997–4126.
  - [S75] Boustani M, Campbell N, Munger S et al. Impact of anticholinergics on the aging brain: a review and practical application (échelle ACB). Aging Health 2008;4:311–320.
  - [S76] Nolen WA, Licht RW, Young AH et al. What is the optimal serum level for lithium in the maintenance treatment of bipolar disorder? A systematic review and recommendations from the ISBD/IGSLI Task Force. Bipolar Disord 2019;21:394–409.
  - [S77] McDonagh TA, Metra M, Adamo M et al. 2021 ESC Guidelines for the diagnosis and treatment of acute and chronic heart failure. Eur Heart J 2021;42:3599–3726.
  - [S78] pharmaSuisse. Polymedikations-Check : contrôle de la polymédication en pharmacie pour les patients prenant au moins 4 médicaments pendant au moins 3 mois (convention tarifaire LOA).
  - [S79] Lenders JWM, Duh QY, Eisenhofer G et al. Pheochromocytoma and paraganglioma: an Endocrine Society clinical practice guideline. J Clin Endocrinol Metab 2014;99:1915–1942.
  - [S80] Garmendia Madariaga A, Santos Palacios S, Guillén-Grima F, Galofré JC. The incidence and prevalence of thyroid dysfunction in Europe: a meta-analysis. J Clin Endocrinol Metab 2014;99:923–931.
  - [S81] Lenders JWM, Eisenhofer G, Mannelli M, Pacak K. Phaeochromocytoma. Lancet 2005;366:665–675.
  - [S82] Organisation mondiale de la santé. Classification internationale des maladies, 11e révision (CIM-11), en vigueur depuis le 1er janvier 2022 ; 6B01 trouble panique, 6C20 trouble de détresse corporelle.
  - [S83] National Institute for Health and Care Excellence. Generalised anxiety disorder and panic disorder in adults: management (CG113). 2011, mise à jour 2020.
  - [S84] Kroenke K, Spitzer RL, Williams JB, Monahan PO, Löwe B. Anxiety disorders in primary care: prevalence, impairment, comorbidity, and detection. Ann Intern Med 2007;146:317–325.
  - [S85] Alfonzo A, Harrison A, Baines R et al. Clinical practice guidelines: treatment of acute hyperkalaemia in adults. UK Kidney Association (Renal Association), 2020.
  - [S86] Katz MA. Hyperglycemia-induced hyponatremia: calculation of expected serum sodium depression. N Engl J Med 1973;289:843–844.
  - [S87] Hillier TA, Abbott RD, Barrett EJ. Hyponatremia: evaluating the correction factor for hyperglycemia. Am J Med 1999;106:399–403.
  - [S88] Gennari FJ. Hypokalemia. N Engl J Med 1998;339:451–458.
  - [S89] Umpierrez GE, Davis GM, ElSayed NA et al. Hyperglycemic crises in adults with diabetes: a consensus report. Diabetes Care 2024;47:1257–1275.
  - [S90] Stewart AF. Hypercalcemia associated with cancer. N Engl J Med 2005;352:373–379.
  - [S91] Verbalis JG, Goldsmith SR, Greenberg A et al. Diagnosis, evaluation, and treatment of hyponatremia: expert panel recommendations. Am J Med 2013;126:S1–S42.
  - [S93] Goto M, Al-Hasan MN. Overall burden of bloodstream infection and nosocomial bloodstream infection in North America and Europe. Clin Microbiol Infect 2013;19:501–509.
  - [S94] Schlapbach LJ, Zimmermann EA, Meylan S et al. Swiss Sepsis National Action Plan. Front Med (Lausanne) 2023;10:1114546.
  - [S95] Vincent JL, Moreno R, Takala J et al. The SOFA (Sepsis-related Organ Failure Assessment) score to describe organ dysfunction/failure. Intensive Care Med 1996;22:707–710.
  - [S97] Mach F, Baigent C, Catapano AL et al. 2019 ESC/EAS Guidelines for the management of dyslipidaemias. Eur Heart J 2020;41:111–188.
  - [S98] Collet JP, Thiele H, Barbato E et al. 2020 ESC Guidelines for the management of acute coronary syndromes in patients presenting without persistent ST-segment elevation. Eur Heart J 2021;42:1289–1367.
  - [S101] Miller A, Green M, Robinson D. Simple rule for calculating normal erythrocyte sedimentation rate. Br Med J 1983;286:266 (homme : âge/2 ; femme : (âge + 10)/2).
  - [S103] National Institute for Health and Care Excellence (NICE). Delirium: prevention, diagnosis and management in hospital and long-term care (CG103), mise à jour 2023.
  - [S104] MacLullich AMJ et al. Le 4AT, outil de dépistage du delirium (www.the4at.com) : vigilance 0 ou 4, AMT4 0–2, mois à l’envers 0–2, changement aigu ou fluctuant 0 ou 4 ; score ≥ 4 : delirium possible.
  - [S112] Satran D, Henry CR, Adkinson C et al. Cardiovascular manifestations of moderate to severe carbon monoxide poisoning. J Am Coll Cardiol 2005;45:1513–1516 (atteinte myocardique, troponine ou CK-MB élevée, chez environ 37 % des 230 patients).
  - [S113] Swissmedic. Information professionnelle Cyanokit® (hydroxocobalamine) : 5 g IV en 15 minutes chez l’adulte, deuxième dose de 5 g possible selon la gravité ; coloration rouge de la peau et des urines, interférence avec des dosages colorimétriques. swissmedicinfo.ch.
  - [S118] Dantzer R, O’Connor JC, Freund GG, Johnson RW, Kelley KW. From inflammation to sickness and depression: when the immune system subjugates the brain. Nat Rev Neurosci 2008;9:46–56 (cytokines IL-1β, IL-6, TNF-α ; voies humorale et vagale ; comportement de maladie).
  - [S119] Pepys MB, Hirschfield GM. C-reactive protein: a critical update. J Clin Invest 2003;111:1805–1812 (synthèse hépatique sous IL-6 ; demi-vie plasmatique ≈ 19 heures, constante quelle que soit la maladie).

## Remarques
- Le point 13.b (contenu « ne jamais oublier ») relève de la relecture HUMAINE ; il est rédigé mais non noté automatiquement.
- Le style compte des « symboles » (→, =, >) : ils viennent surtout des formules des fenêtres de la bibliothèque d’examens partagée (lecture seule) et sont inévitables.
- Les dossiers partagés outils/ et bibliotheque_examens/ n’ont pas été modifiés. Les copies locales sont dans source/outils_local/ et les ajouts de sigles dans source/outils_local/sigles_extra.py.
- LOT_006 : non commencé.
