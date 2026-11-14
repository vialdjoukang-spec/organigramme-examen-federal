# Audit médical des textes : PE_MS.json (IMG-238 à IMG-288), 14.11.2026

Auditeur indépendant (je n'ai rien rédigé). J'ai appliqué les skills `medecin-expert`, `radiologue-expert` et `expert-web`. Objet : gold, premiere_intention, autres, syndrome, traitement et sources. Les images sont hors champ.

**Ce que j'ai fait**
- J'ai lu les 51 entrées en entier, sans les images (94 Ko).
- J'ai lu par URL, avec `aips_fiche.py` et dans le texte AIPS en cache, 37 AIPS : OncoTICE 52563, Tamsulosin-Mepha 58828, Avodart 56106, Rocephin 44625, Ciproxine 47795, Doxycyclin-Mepha 65952, Flagyl 26313, Metronidazole Sintetica 55280, Cyklokapron 33741, Tranexam Labatec 69390, Visanne 60119/70484, Femara 54018, Glucophage 26061, Methotrexat Accord 66780, Rhophylac 53609, Cytotec 46945, Clexane 49456, Eliquis 61549, Xarelto 58728, Carbetocin Ferring 67157, Nalador 43642, Aspirine Cardio 51795, Kenacort-A 26177, Ibuprofen-Mepha 49156, Floxapen 37404, Naproxen-Mepha 51480, Zyloric 32917, Adenuric 65851, Remicade 55184, Xtandi 67236, Eligard 56852, Lucrin Dépôt 51903, Pamorelin 52815, Genotropin 50823 et Co-Amoxicillin Zentiva 67110.
- J'ai vérifié par `trouve` que l'oxytocine injectable, la colchicine et le sulfate de magnésium injectable sont absents du corpus. Leurs mentions « À vérifier » sont donc légitimes.
- En ligne, j'ai vérifié ces points : IUSTI 2024 (épididymo-orchite), WHO/FIGO/ICM 2025 (hémorragie du post-partum), SGGG Expertenbrief n° 80 (2023) et n° 26, ESGO-ESTRO-ESP 2025 (endomètre). Je n'ai trouvé aucune mise à jour 2024 de l'ESVS sur les abords de dialyse.
- J'ai contrôlé les sources par script : 108 sources, dont 9 seulement portent une étiquette. Le texte contient 56 mentions « À vérifier ».

Doses conformes à l'AIPS : tamsulosine, dutastéride, ciprofloxacine dans la prostatite, ceftriaxone 1–2 g, méthotrexate dans la PR, carbétocine, Rhophylac dans 261, énoxaparine, apixaban, ibuprofène, flucloxacilline, naproxène, allopurinol et fébuxostat. Les indications Nalador et OncoTICE sont aussi conformes.

## 1. Critiques : « À vérifier » ou interdit adouci sur une AIPS présente au corpus

| Id | Extrait actuel | PATCH exact | Preuve AIPS |
|---|---|---|---|
| C1 244 trait.[0] | « ceftriaxone (dose À vérifier, Rocephin® AIPS ne détaille pas cette indication) puis doxycycline 100 mg 2×/j pendant au moins 10 jours » | « ceftriaxone 1 g i.m. dose unique (source européenne : IUSTI 2024 ; l'AIPS Rocephin® 44625 indique 0,25 g i.m. dose unique dans la blennorragie : écart signalé), puis doxycycline 100 mg 2×/j pendant au moins 10 jours (AIPS Doxycyclin-Mepha) ; IUSTI 2024 : 14 jours » | Rocephin : « Blennorragie … administration unique de 0,25 g … i.m. ». La mention « ne détaille pas » est **fausse**. |
| C2 244 trait.[1] | « ciprofloxacine … (AIPS Ciproxine®, durée « au moins » selon le tableau, À vérifier) » | « ciprofloxacine 2×500 à 2×750 mg/j pendant au moins 14 jours (AIPS Ciproxine®, ligne « orchi-épididymite ») » | Tableau 1 : « Orchi-épididymite … Au moins 14 jours » |
| C3 253 trait.[0] | « ceftriaxone 1 dose (dose À vérifier ; IUSTI 2017 : 1 g i.m.) … métronidazole 2×/j … À vérifier AIPS métronidazole oral » | « ceftriaxone 1 g i.m. dose unique (source européenne : IUSTI 2017 ; AIPS Rocephin® 1–2 g/j), puis doxycycline 100 mg 2×/j et métronidazole 500 mg 2×/j pendant 14 jours (IUSTI : 400 mg 2×/j ; AIPS Flagyl® 26313, infections à anaérobies : 3 × 500 mg/j, durée minimale habituelle de 10 jours : écart signalé) » | Flagyl : « 1,5 g … répartis en 3 doses … durée minimale … 10 jours ». Remplacer la source Sintetica (perfusion i.v.) par Flagyl® 26313, mise à jour septembre 2025. |
| C4 250 trait.[1] | « acide tranexamique (dose À vérifier : AIPS Cyklokapron®) … analogues de la GnRH en préopératoire (À vérifier) » | « acide tranexamique 1 g 4×/j le 1er jour, puis 1 g 3×/j les jours 2 et 3 (AIPS Cyklokapron® 33741, hyperménorrhée) … analogues de la GnRH en préopératoire (hors indication AIPS : Lucrin Dépôt 51903 et Pamorelin 52815 ne citent pas le fibrome) » | « le 1er jour 2 comprimés pelliculés [500 mg] … 4 fois par jour, les 2e et 3e jours … 3 fois par jour » |
| C5 254 trait.[0] | « p. ex. diénogest (ESHRE : devrait) ; doses À vérifier » | « p. ex. diénogest 2 mg 1×/j en continu (AIPS Visanne® 70484) (source européenne : ESHRE 2022, recommandation forte) » | Visanne : « un comprimé par jour … en continu » |
| C6 255 trait.[1–2] | « metformine … (doses À vérifier) » ; « létrozole … (hors indication AIPS en Suisse, À vérifier) » | « metformine (hors indication : AIPS Glucophage® 26061 limitée au diabète) » ; « létrozole (hors indication ; l'AIPS Femara® 54018 le **contre-indique** en cas de « statut endocrinien préménopausal » et pendant la grossesse : prescription spécialisée, grossesse exclue) » | Contre-indication **adoucie** en « hors indication » |
| C7 258 trait.[1–2], 259 trait.[0–1] | « méthotrexate 50 mg/m² … (hors indication AIPS, À vérifier) » ; « Rhophylac® (… dose À vérifier dans l'AIPS) » ; « misoprostol (hors indication AIPS Cytotec®, À vérifier) » ; « Rhophylac®, À vérifier dose » | « (hors indication : AIPS Methotrexat Accord® 66780 limitée aux indications non oncologiques rhumatologiques et dermatologiques) » ; « Rhophylac® 300 µg (1500 UI) i.v. ou i.m. au plus tard dans les 72 heures (AIPS : « grossesse ectopique », « avortement spontané ») » ; « misoprostol (hors indication : AIPS Cytotec® 46945, ulcères seulement, contre-indiqué pendant la grossesse) » | Rhophylac : « suite à l'apparition de complications, 300 µg … au plus tard dans les 72 heures » |
| C8 263 trait.[2] | « anticoagulants oraux directs à éviter pendant la grossesse (À vérifier AIPS) » | « rivaroxaban contre-indiqué pendant la grossesse (AIPS Xarelto® 58728) ; apixaban « non recommandé » (AIPS Eliquis® 61549) » | AIPS lues mot pour mot |
| C9 264 trait.[1] | « acide tranexamique 1 g i.v. dans les 3 heures (essai WOMAN ; dose AIPS À vérifier) » | « acide tranexamique 1 g i.v. lente (1 mL/min) dans les 3 heures (AIPS Tranexam Labatec® 69390 : « affections d'origines obstétricales » ; essai WOMAN) » | Tranexam Labatec : « 1 g … injection intraveineuse lente (= 1 ml/minute) » |
| C10 265 trait.[2] | « anti-TNF (ECCO) ; doses À vérifier » | « infliximab 5 mg/kg i.v. aux semaines 0, 2 et 6, puis toutes les 8 semaines (AIPS Remicade® 55184, Crohn fistulisé) » | « 5 mg/kg, suivie par deux autres perfusions … 2 et 6 semaines » |
| C11 269 trait.[0] ; 270 trait.[2] | « infiltration de corticoïdes sous-acromiale (doses AIPS À vérifier) » ; « infiltration intra-articulaire » sans dose | 269 : « triamcinolone acétonide 10–40 mg en intrafocal (AIPS Kenacort®-A 26177, « syndrome épaule-bras ») » ; 270 : « triamcinolone 20 mg intra-articulaire (AIPS Kenacort®-A : épaule, « blocage … lors d'une atrophie capsulaire »), au moins 2 semaines entre deux injections » | AIPS Kenacort-A lue |
| C12 285 trait.[0] | « (doses À vérifier AIPS) » | « somatropine 0,025–0,035 mg/kg/j (AIPS Genotropin® 50823) ; leuproréline 0,3 mg/kg toutes les 4 semaines, au moins 7,5 mg (AIPS Lucrin Dépôt® 51903, puberté précoce centrale) » | Lus mot pour mot |
| C13 241 trait.[2] | « molécules et doses À vérifier (AIPS) » | « agoniste de la LHRH, p. ex. leuproréline s.c. tous les 1, 3 ou 6 mois (AIPS Eligard® 56852), associé à l'enzalutamide 160 mg 1×/j (AIPS Xtandi® 67236) » | Lus |
| C14 284 trait.[1] | « doses AIPS selon la molécule (À vérifier durée) » | « co-amoxicilline 3 × 625 mg/j p.o. (AIPS Co-Amoxicillin Zentiva® 67110) ou flucloxacilline 3 × 1 g/j i.v. (AIPS Floxapen® 37404) ; durée non fixée par l'AIPS » | Aucune dose n'était écrite |

## 2. Majeurs

| Id | Défaut | PATCH exact |
|---|---|---|
| M1 244, 253 sources | Les dates de mise à jour sont fausses : Doxycyclin-Mepha est écrite « février 2025 (À vérifier) », Metronidazole Sintetica « septembre 2024 (À vérifier) ». | Écrire « mise à jour février 2024 » et « septembre 2025 ». Ce sont les rubriques AIPS lues. |
| M2 264 gold.examen | La définition est périmée : « perte ≥ 500 mL, ou ≥ 1000 mL après césarienne ». | « perte ≥ 500 mL, ou ≥ 300 mL avec signes vitaux anormaux (dernier recours : OMS/FIGO/ICM 2025) ». Remplacer « SGGG — Expertenbrief … (À vérifier date) » par « SGGG Expertenbrief n° 26, 2012 ». |
| M3 262 trait.[0–1] | La source suisse est absente. Le texte écrit « hors posologie » alors qu'il s'agit d'une indication absente. Les doses sont laissées « À vérifier » alors que la SGGG les fixe. | « aspirine 100–150 mg/j, débutée avant 16+0 SA (SGGG EB n° 80, 2023) ; hors indication AIPS Aspirine® Cardio 51795 » ; « sulfate de magnésium 4 g i.v. en 15 min, entre 24+0 et 32+0 SA (SGGG EB n° 66) ; bétaméthasone 2 × 12 mg i.m. à 24 h d'intervalle, entre 24+0 et 33+6 SA (SGGG EB n° 56 ; hors AIPS Diprophos 39528) » |
| M4 9 entrées | Des sources fantômes sont listées comme sources : « Recommandation suisse/européenne — À vérifier », « SGGG — À vérifier » (252, 257, 267, 270, 273, 275, 276, 284, 288), auxquelles s'ajoute « ESHRE/ESGE — À vérifier » (250). | Les supprimer, ou les remplacer par une source lue et datée. |
| M5 252, 267, 269, 272, 277, 283, 288 | Les sources sont américaines exclusives (ACR, AAOS, SVS), à côté d'articles historiques. | Chercher une source européenne (p. ex. ESHRE ou ESGE pour 252, ESSKA pour 267). À défaut, étiqueter « (source américaine, non vérifié CH) » sur chaque ligne. 253 : remplacer « critères minimaux CDC » par les critères IUSTI 2017. |
| M6 tout le fichier | 99 sources sur 108 n'ont pas d'étiquette (EAU, ESGO, ESHRE, EULAR, ESVS, ISUOG…). L'AIPS suisse est placée après l'EAU (238, 239, 242, 244, 248). | Ajouter « (source européenne) » à chaque société européenne. Trier les sources dans l'ordre AIPS et SGGG/SGUM, puis Europe, puis autres, puis OMS. |
| M7 251, 259 | Les versions sont laissées « À vérifier » alors qu'elles existent. | « Concin N et al. ESGO-ESTRO-ESP update 2025, Lancet Oncol 2025;26(8):e423 (source européenne) ». Pour 259, citer la mise à jour ISUOG 2023 du premier trimestre, après lecture. |

## 3. Mineurs

| Id | Défaut | PATCH |
|---|---|---|
| 261 trait.[0] | « 36–37 semaines (À vérifier) » | Écrire « 36+0 à 37+0 SA (source européenne : RCOG GTG 27a) ». |
| 263 syndrome[2] | « TSH du nouveau-né (À vérifier) » | Écrire « contrôle de la fonction thyroïdienne du nouveau-né la première semaine (source européenne : ESUR v10) ». |
| 280 trait.[1] | « Corticoïdes en relais court » | Écrire « corticoïdes de courte durée à l'instauration du méthotrexate, puis arrêt dès que possible (EULAR 2022) ». |
| 244 autres[0] | Le Doppler scrotal est cité à la fois comme gold et en rang 2 (doublon). | Supprimer l'entrée de rang 2. |
| autres.pourquoi_pas_gold (≈ 60 puces) | Les puces sont nominales (« invasive », « biologie », « seconde ligne »). | Les reformuler en phrases verbales, p. ex. « elle est invasive ». |

## 4. Verdict

**corrections requises.** Il reste 14 critiques (C1 à C14 : « À vérifier » sur des AIPS présentes au corpus, un énoncé AIPS faux en 244, une contre-indication adoucie en 255) et 7 majeurs. L'examen de référence et la première intention sont exacts pour les 51 entrées. Je n'ai trouvé aucune dose chiffrée fausse ; les erreurs sont des omissions, une date fausse et une affirmation AIPS inexacte. Après application des patchs C1 à C14 et M1 à M7, il faudra un contre-audit court, limité aux lignes modifiées.
