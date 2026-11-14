# Audit médical agressif : EXP_b.json (EXP-052 à EXP-102)

| Objet | Valeur |
|---|---|
| Fichier audité | `Claude/_progression/recensement/enrichi/EXP_b.json`, 171 698 octets, SHA-256 `3587c10a…a436`, commit 1f60c2f26 (14.11.2026) |
| Cadrage | `recensement.json > explorations` : 51 fiches (cardiologie fonctionnelle, pneumologie, digestif, rein, miction) |
| Méthode | 39 AIPS ouvertes dans le corpus refdata (`aips_fiche.py trouve` + texte HTML lu) ; plus de 30 calculs refaits en Python ; 12 recherches web (ESC, ERC, GINA, GOLD, EAU, Endocrine Society, FMH, SSH) |
| Verdict | **REFUSÉ** : 57 % (8/14) ; 16 défauts critiques ; question finale « **non** » |

## 1. Score (§ 12.2, adapté aux 7 axes de la commande, 2/1/0)

| Axe | Note | Raison |
|---|---|---|
| Examen de référence et première intention | 2 | L'examen de référence et la première intention sont justes et argumentés dans les 51 fiches |
| Lecture systématique | 2 | Les étapes sont ordonnées et techniques ; les formulations non verbales sont traitées à l'axe 7 |
| Valeurs normales et unités | 1 | PD20, FeNO, classes de FEVG périmées, DLCO incohérente, seuils pris à des sources américaines seules |
| Calculs | 1 | Les 30 calculs refaits sont exacts sauf CKD-EPI (69 et non 68) ; la formule MELD-Na annoncée manque |
| Syndrome et traitement | 1 | Les recommandations sont périmées : ERC 2021, ESC IC 2021, valvulopathies 2021, péricardite 2015, GINA 2024, GOLD 2025, EAU 2024–2025 |
| Doses AIPS | 0 | 16 molécules du corpus sont restées « non lues » ou « À vérifier » ; une contre-indication est omise ; 4 usages hors AIPS sont passés sous silence |
| Sources, traces et phrases | 1 | Une source est inventée (« ESE 2025 »), une source ATS est étiquetée ERS, l'adoption par la SSC est vérifiable mais reste « non lu » |

## 2. Critiques (bloquants)

| # | Emplacement | Extrait | PATCH exact (source lue) |
|---|---|---|---|
| C1 | EXP-095 traitement[1] | « AIPS Dilatrend n° 53162 : rubrique posologie non extraite par l'outil (À vérifier, AIPS) » | « carvédilol (Baveno VII) ; **hors indication AIPS** (HTA, angor, IC) ; AIPS Dilatrend n° 53162 (oct. 2023) : **contre-indiqué en cas d'insuffisance hépatique cliniquement manifeste**, de BPCO ou d'asthme ; posologie HTA 12,5 mg/j pendant 2 j puis 25 mg/j (max. 50 mg/j) ; la dose Baveno (6,25 puis 12,5 mg/j) relève de la recommandation européenne » |
| C2 | EXP-055 traitement[4] | « midodrine (AIPS Gutron n° 44977 : rubrique posologie non extraite, À vérifier) » | « midodrine : AIPS Gutron n° 44976/44977 (mars 2021) : formes sévères 3 × 2,5 mg/j, jusqu'à 15 mg/j, dernière prise ≥ 4 h avant le coucher ; contre-indiquée en cas de cardiopathie organique sévère, d'HTA, de rétention urinaire, de grossesse et d'allaitement » |
| C3 | EXP-065 traitement[0] | « ibuprofène : AIPS Brufen n° 45031 sans posologie extraite (À vérifier) » | « ibuprofène : **hors indication AIPS** (péricardite absente) ; AIPS Brufen n° 45031 (déc. 2024) : dose journalière maximale 2400 mg ; contre-indiqué si IC NYHA III–IV, si clairance < 30 ml/min, en cas d'ulcère ou de saignement digestif ; la dose ESC de 600 mg toutes les 8 h reste sous ce maximum » |
| C4 | EXP-058 traitement[1] ; EXP-059[0] ; EXP-060[0] | « libellé SCA absent de l'AIPS Aspégic lue → À vérifier » ; « AIPS de l'aspirine cardio non trouvée dans le corpus » | « AIPS Aspirine Cardio n° 51795 (mars 2026) : infarctus aigu 200–300 mg i.v. ou p.o. (forme non gastrorésistante, croquée), puis 100 mg/j dès J2 ; l'angor instable est indiqué ; indications cardiovasculaires 100 mg/j » |
| C5 | EXP-058 traitement[3] | « posologie : AIPS Heparin-Na B. Braun n° 46613, non lue ici » | « AIPS n° 46613 (juin 2026) : NSTEMI bolus 60–70 UI/kg i.v. (max. 5000 UI) puis 12–15 UI/kg/h (max. 1000 UI/h), adaptés à l'aPTT ; STEMI sous fibrinolyse : bolus 60 UI/kg » |
| C6 | EXP-052 traitement[3] | « isoprénaline, À vérifier : disponibilité CH » | « isoprénaline : Isuprel n° 56457 (nov. 2020), **hors indication AIPS** pour les torsades (indications : bradycardie avant pacemaker, Stokes-Adams) ; 0,2–10 mg/24 h en perfusion ; arrêt si FC ≥ 130/min » |
| C7 | EXP-054 traitement[4] | « KCl 7,45 % Sintetica n° 56521, non lue ici » | « AIPS n° 56521 (févr. 2024) : toujours diluer ; si K > 2,5 mmol/l : 10 mmol/h au maximum, 40 mmol/l au maximum et 200 mmol/j au maximum » |
| C8 | EXP-061 traitement[0–1] | « Entresto n° 65673, Forxiga n° 65176 : non lues ici » ; « doses plus faibles en HFrEF … → À vérifier » | « Entresto (sept. 2025) : 2 × 100 mg/j (2 × 50 mg sans IEC ni ARA préalable), doublé toutes les 2–4 sem. jusqu'à 2 × 200 mg ; Forxiga (août 2026) : 10 mg 1×/j ; Aldactone n° 27257 : entretien **25–100 mg/j** dans l'AIPS, ce qui couvre la dose ESC » |
| C9 | EXP-069[0], 070[0], 072[1], 078[0] | « AIPS Camzyos / Symbicort / Ofev / Esbriet / Adempas … non lue ici » | Remplacer chaque mention par la posologie mot pour mot de l'AIPS (toutes présentes : n° 68477, 55568, 65330, 66422, 62903) ; pour Symbicort (juin 2023), voir G6 |
| C10 | EXP-088[0] ; EXP-094[0] | « dose : voir l'AIPS du produit (non consultée ici) » | IPP : choisir et citer Pantozol ou Nexium (présents) ; macrogol : « Transipeg n° 53282 (juil. 2021) : 1–4 sachets/j, moyenne 2 sachets/j » ; prucalopride : AIPS Resolor n° 59304 (mars 2022), indication « constipation chronique idiopathique de l'adulte après échec des laxatifs » |

## 3. Graves

| # | Emplacement | Défaut | PATCH (source) |
|---|---|---|---|
| G1 | EXP-052, 054, 057 sources | ERC 2021 est remplacé | « ERC Guidelines 2025, Special circumstances (Resuscitation 2025;215 suppl. 1), source européenne » ; relire hyperK et hypothermie |
| G2 | EXP-061 valeurs et sources | L'ESC IC 2021 est remplacée par l'ESC IC 2026 (ehag100) : HFrEF < 50 %, HFpEF ≥ 50 %, HFmrEF supprimée, ARM classe I quelle que soit la FEVG | Réécrire les trois seuils de FEVG et la ligne HFpEF ; « (source européenne : ESC 2026, résumé) » |
| G3 | EXP-062, 063 | L'ESC/EACTS 2025 est sortie : TAVI dès ≥ 70 ans (I-A) ; intervention précoce IIa dans la SA serrée asymptomatique à bas risque | Supprimer « ≥ 75 ans … À vérifier » ; citer ESC/EACTS 2025 (ehaf194) |
| G4 | EXP-065 | ESC 2015 ; l'ESC 2025 myocardite-péricardite existe et la SSC l'a adoptée (guidelines.fmh.ch) | Citer ESC 2025 (ehaf192) : AINS ou aspirine + colchicine 3–6 mois, corticoïdes en 2e ligne, anti-IL-1 en 3e ligne |
| G5 | EXP-070, 075, 071, 073 | GINA 2024 et GOLD 2025 sont périmés : GINA 2026 (5.5.2026) et GOLD 2026 (10.11.2025, seuil du groupe E abaissé) | Mettre à jour les deux références et revérifier les groupes B/E |
| G6 | EXP-070 traitement[0] | Le traitement à la demande seul (paliers 1–2) est **hors AIPS** : Symbicort est indiqué « si les glucocorticoïdes inhalés, utilisés seuls, ne suffisent pas » | Ajouter : « paliers 1–2 : hors indication AIPS Symbicort n° 55568 » |
| G7 | EXP-101 sources | « ESE 2025 » n'existe pas : c'est l'**Endocrine Society 2025** (Adler, JCEM 2025;110:2453-95), source américaine | « USA (dernier recours) : Endocrine Society 2025 » ; ajouter l'ESC 2024 HTA (dépistage) comme source européenne |
| G8 | EXP-101 traitement[1] | La dose « 100 mg puis 200 mg » vient de la rubrique HTA | AIPS Aldactone : « 100–400 mg/j en préparation à l'opération ; inopérable : dose efficace la plus faible possible » |
| G9 | EXP-082 sources | « ERS 2020 … (Am J Respir Crit Care Med 2020;202:e121) » est la recommandation **ATS** 2020 (Jacobs), américaine | Corriger l'étiquette en « USA (dernier recours) : ATS 2020 » et chercher l'équivalent ERS |
| G10 | EXP-057 traitement[0] | Le bicarbonate n'est pas indiqué dans l'intoxication tricyclique (AIPS : acidoses, barbituriques) ; 1 mmol/kg est la dose de « tamponnement à l'aveugle en réanimation » | Ajouter « hors indication AIPS n° 36797 » et citer l'extrait exact |
| G11 | EXP-090 traitement[2] | Paspertin n'est pas indiqué dans la gastroparésie (indications : nausées et vomissements ; 5 j au maximum) | Ajouter « hors indication AIPS ; 5 jours au maximum (dyskinésies tardives) » |
| G12 | EXP-086 valeurs ; EXP-090 valeurs ; EXP-076 | Les seuils viennent d'une source américaine seule (ATS 2019, SNMMI/ANMS 2008, ATS 2011) | EXP-090 : citer UEG/ESNM 2021 ; EXP-076 : citer ERS 2022 ; EXP-086 : chercher ERS (Randerath) ou SSP |

## 4. Moyens et légers

| # | Emplacement | Défaut → PATCH |
|---|---|---|
| M1 | 12 fiches cardiologiques | « SSC applique les recommandations ESC (adoption formelle À vérifier) — non lu » → la plateforme FMH « Guides de pratique Suisse » recense les ESC adoptées (SCA 2023, AV 2022, CCS 2024, cardiomyopathies 2023, myopéricardite 2025, HTA 2024) ; citer l'entrée FMH |
| M2 | EXP-052 valeurs | Le QTc < 450/460 ms n'est pas un seuil ESC 2022 (critère classique AHA/HRS 2009) → « (non vérifié CH) » ; la cible K 4,5–5,0 n'est pas attribuée de façon vérifiée |
| M3 | EXP-054 traitement[2] | Lokelma est incomplet → « 10 g 3×/j 24–48 h (+24 h au maximum), puis 5 g/j (jusqu'à 10 g/j) ; ne pas l'utiliser en urgence vitale (AIPS janv. 2026) » |
| M4 | EXP-075 valeurs et traces | « PD20 positive < 200 µg » semble faux : la classification ERS 2017 lue de mémoire place la normale > 400 µg, la limite à 100–400 µg et l'HRB légère à 25–100 µg ; à confirmer sur le texte intégral (403 en ligne) |
| M5 | EXP-070 valeurs | « ≥ 40 (ERS 2022) » est inexact : l'ERS retient 50 ppb pour appuyer le diagnostic (vote 10 contre 5) ; 40 ppb n'est qu'un compromis |
| M6 | EXP-066 traitement[1] | « contre-indique une pneumonectomie si VO2 < 10 » → « signale un haut risque ; oriente vers une résection limitée ou un traitement non chirurgical (ERS/ESTS 2009) » |
| M7 | EXP-078 | La trace demande « DLCO < 50 % » alors que la valeur indique DETECT < 60 % → harmoniser à 60 % |
| M8 | EXP-096 | Le MELD-Na est annoncé dans l'examen de référence, mais sa formule manque ; la règle Swisstransplant n'est pas lue → ajouter la formule et la marquer « À vérifier » |
| M9 | EXP-058 | La 5e définition universelle de l'infarctus (ESC 2026) est parue → revérifier les seuils de sus-décalage du ST |
| M10 | EXP-100, 102 | EAU/ESPU 2024 et EAU 2025 sont remplacées par EAU 2026 (mars 2026) ; l'inhibiteur de la 5α-réductase doit citer l'AIPS Proscar (n° 51774) ou Avodart (n° 56106) |
| L1 | EXP-097 calculs[0] | « ≈ 68 » → « ≈ 69 ml/min/1,73 m² » (valeur recalculée : 69,2) |
| L2 | EXP-077 | « KCO … → 1,0 » → « 1,0 mmol/min/kPa/l » |
| L3 | EXP-052 lecture[4] | « (QT JT) » est tronqué → « (mesure du JT) » |
| L4 | EXP-071 T0, 073 T1, 082 T1, 093 T1, 080 lecture | Les items nominaux deviennent verbaux (« arrête le tabac », « prescrit une réadaptation », « lit le pH ») |
| L5 | EXP-094 calculs | « prise unique de 24 marqueurs/j pendant 3 j » se contredit → « 24 marqueurs par jour pendant 3 j » |
| L6 | EXP-099 T0 | « AIPS non consultée » → « citrate de potassium absent du corpus refdata (À vérifier, AIPS) » |
| L7 | EXP-098 | Ajouter la nomenclature 2022 : « déficit / résistance en AVP » |

## 5. Contrôles conformes
- Les calculs refaits sont justes : Bazett 447, Fridericia 474/516, PISA 0,50 cm², continuité 0,70, Bernoulli 81, RVP 7,5, Devereux 234, MELD 21,0, FIB-4 2,0, Cockcroft 57, trou anionique 30/15, Winter 23, BOOI 64, BCI 120, PD20 153, Enright 574/520, PAO2 à Davos 72, Duke −5.
- Les AIPS citées concordent mot pour mot (numéro et date) : Mg Bichsel, Inderal, Lokelma, bicarbonate, Florinef, Brilique (« au moins 12 mois »), Arixtra, Aldactone, Paspertin, Pylera, Creon, Minirin injectable, Tamsulosin Zentiva, Aspégic.

**Question finale : non.** Il manque les 16 posologies AIPS du corpus, la contre-indication hépatique du carvédilol, les mentions hors AIPS (Symbicort, bicarbonate, Paspertin, Brufen, isoprénaline, carvédilol) et la mise à jour vers ERC 2025, ESC 2025–2026, GINA 2026, GOLD 2026 et EAU 2026.
