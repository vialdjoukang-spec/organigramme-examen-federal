# Audit médical agressif des champs texte : AB.json (IMG-166 à IMG-237), 14.11.2026

**Version auditée** : `enrichi/AB.json`, 228 381 octets, SHA-256 `59ce228e26778b43…`, 72 entrées. **Champs** : gold, premiere_intention, autres, syndrome, traitement, sources. Les images sont hors champ, car elles sont déjà auditées.
**Méthode (ce que j'ai fait)** : j'ai relu les 72 traitements, les 72 listes de sources, les 72 « gold », les rangs et toutes les valeurs chiffrées. J'ai cherché 52 molécules dans le corpus (`aips_fiche.py trouve`). J'ai ouvert 44 AIPS (`fiche`) et cherché chaque dose citée dans le texte complet en cache. J'ai fait des recherches web ciblées sur EASL CHC 2025, BCLC 2025, ESVS 2025, IAP 2025, HerniaSurge 2023, ESGE 2021, Baveno VII, EAU 2026, EASL hémochromatose 2022, WSES rate 2017 et ESPR 2026.
**Ce qui est conforme** : les doses citées de Rocephin, Flagyl (amibiase 500 mg 3–4×/j, 7–10 j), Zentel (> 60 kg : 800 mg/j, 28 j), Glypressine, Aldactone (Na/K), Augmentin, Novalgin (5 g/j), Inflamac 50 (100–150 mg/j), Dificlir, Vancocin, Ciprofloxacine Zentiva et Propranolol Zentiva (phéochromocytome 60 mg/j, 3 j). Sont aussi justes : le miel ESPGHAN, l'albumine 8 g/l au-delà de 5 l, les seuils de Bosniak, de pylore, de GASA et d'ESVS 2024 (55/50 mm), ainsi que les « gold » de 70 entrées sur 72.
**Bilan** : 45 mentions « À vérifier » ; **aucun numéro Swissmedic** dans tout le fichier.

## 1. Défauts critiques : « À vérifier » alors que l'AIPS est au corpus et répond (17)

| # | Id · champ | Extrait fautif | PATCH exact (texte AIPS lu) |
|---|---|---|---|
| C1 | 167 · T2 | « doses AIPS CH À vérifier » | « atézolizumab 1200 mg i.v. puis bévacizumab 15 mg/kg toutes les 3 semaines (AIPS Tecentriq n° 66152, mars 2026 ; Avastin n° 56922, mai 2026) ; ou trémélimumab 300 mg en dose unique avec durvalumab 1500 mg à J1, puis durvalumab 1500 mg toutes les 4 semaines (AIPS Imjudo n° 68706, juin 2025 ; Imfinzi n° 66548, juin 2026) » |
| C2 | 170 · T1 | « dose 6,25 mg/j puis 12,5 mg/j hors indication AIPS CH — À vérifier » | « carvédilol : hors indication (AIPS Carvedilol Zentiva n° 57821, oct. 2023 : HTA, angor, insuffisance cardiaque) ; propranolol, seul BBNS avec cette indication : débuter à 20 mg 2×/j, puis titrer jusqu'à une baisse d'environ 25 % de la FC, au maximum 160 mg 2×/j, sauf cirrhose décompensée (AIPS Propranolol Zentiva n° 47025, janv. 2023) » |
| C3 | 172 · T0 ; 191 · T0 ; 227 · T0 | « dose AIPS CH selon spécialité À vérifier » | « énoxaparine 1 mg/kg s.c. toutes les 12 h, ou 1,5 mg/kg 1×/j sans complication (2×/j si cancer ou obésité), avec un relais par AVK (AIPS Clexane n° 49456, févr. 2026) » |
| C4 | 174 · T1 | « déférasirox (Exjade) ; dose AIPS CH À vérifier » | « 20 mg/kg 1×/j à jeun, 10 à 30 mg/kg/j selon les transfusions, au maximum 40 mg/kg/j ; contre-indiqué si ClCr < 60 ml/min (AIPS Exjade n° 57466, mars 2022) » |
| C5 | 175 · T2 | « lactulose, rifaximine … doses AIPS CH À vérifier » | « lactulose 30 à 50 ml 3×/j, avec 2 à 3 selles molles par jour pour objectif (AIPS Duphalac n° 32894, févr. 2023) ; rifaximine 550 mg 2×/j, pour prévenir la récidive (AIPS Xifaxan n° 63216, avr. 2023) » |
| C6 | 179 · T2 | « doses AIPS CH À vérifier » | « durvalumab 1500 mg + gemcitabine 1000 mg/m² + cisplatine 25 mg/m² toutes les 3 semaines (8 cycles au plus), puis durvalumab 1500 mg toutes les 4 semaines (AIPS Imfinzi n° 66548, juin 2026) » |
| C7 | 180 · T0 | « dose AIPS CH Ursofalk À vérifier » | « hors AMM : l'AIPS Ursofalk (n° 42782, mars 2025) couvre la CBP et non la CSP ; elle signale des effets indésirables sévères à 28–30 mg/kg/j dans la CSP » |
| C8 | 185 · T1 | « dose AIPS CH À vérifier » | « 25 000 à 80 000 U de lipase par repas principal, moitié pour une collation ; au maximum 10 000 U/kg/j (AIPS Creon n° 38219, janv. 2025) » |
| C9 | 188 · T1 | « doses AIPS CH À vérifier » | « lanréotide 120 mg tous les 28 jours pour une TNE-GEP G1–G2 (Ki-67 ≤ 10 %) de l'intestin moyen, du pancréas ou de siège inconnu (AIPS Somatuline n° 56148, avr. 2025) ; octréotide LAR 30 mg toutes les 4 semaines, **pour l'intestin moyen seulement** (AIPS Sandostatine LAR n° 53161, janv. 2021) » |
| C10 | 193 · T1 | « héparine non fractionnée ; dose AIPS CH À vérifier » | « bolus de 80 U.I./kg i.v., puis 18 U.I./kg/h, ajustés sur l'aPTT (AIPS Heparin-Na B. Braun n° 46613, juin 2026) » |
| C11 | 199 · T1 | « dose AIPS CH À vérifier » | « imatinib 400 mg/j, pendant au moins 36 mois (AIPS Glivec GIST n° 65814, juill. 2026) » |
| C12 | 202 · T0 | « dose AIPS CH Budenofalk À vérifier » | « budésonide 9 mg 1×/j le matin, pendant 8 semaines (AIPS Budenofalk Uno n° 61405, oct. 2022) » |
| C13 | 203 · T4 | « dose AIPS CH Pentasa/Salofalk À vérifier » | « mésalazine orale, au maximum 4 g/j en 2 à 4 prises, + 1 lavement de 1 g/j pendant 2 à 4 semaines (AIPS Pentasa n° 47502, févr. 2026) » |
| C14 | 209 · T1 | « IPP i.v. à forte dose … dose AIPS CH À vérifier » | « ésoméprazole 40 à 80 mg en 30 min, puis 8 mg/h pendant 72 h, puis 40 mg/j p.o. pendant 4 semaines ; l'indication AIPS est le traitement après endoscopie thérapeutique (AIPS Nexium i.v. n° 56730, juin 2026) » |
| C15 | 214 · T0 | « idarucizumab, andexanet ; doses AIPS CH À vérifier » | « AVK : vitamine K 10 mg i.v. + CCP selon l'INR : 25, 35 ou 50 U.I./kg, au maximum 5000 U.I. (AIPS Konakion MM n° 48112, janv. 2022 ; Beriplex n° 00665, oct. 2022) ; dabigatran : idarucizumab 5 g (AIPS Praxbind n° 65804, mars 2021) ; apixaban, rivaroxaban : andexanet selon le schéma de l'AIPS (Ondexxya n° 67759, avr. 2025) » |
| C16 | 220 · T2 ; 222 · T3 ; 230 · T1 | « doses AIPS CH À vérifier » | « pembrolizumab 200 mg toutes les 3 semaines ou 400 mg toutes les 6 semaines + axitinib 5 mg 2×/j (AIPS Keytruda n° 66231, oct. 2026 ; Inlyta n° 62281, sept. 2025) » ; « évérolimus 10 mg 1×/j (AIPS Votubia n° 62061, déc. 2022) » ; « tolvaptan 45 + 15 mg, puis 60 + 30 mg ou 90 + 30 mg par jour en 2 prises (AIPS Jinarc n° 65676, août 2025) » |
| C17 | 225 · T0 | « doxazosine ou phénoxybenzamine — dose AIPS CH À vérifier » | « doxazosine : hors indication (AIPS Cardura CR n° 54617, déc. 2020 : HTA seulement) ; phénoxybenzamine : absente du corpus, À vérifier (AIPS) » |

## 2. Défauts majeurs (13)

| # | Id · champ | Extrait fautif | PATCH exact | Source lue |
|---|---|---|---|---|
| M1 | toutes · sources | « Swissmedic, AIPS Zentel (2025)… », « (AIPS CH, 2026) » | Ajouter le n° et le mois de chaque AIPS : Rocephin n° 44625 (juin 2025), Flagyl n° 26313 (sept. 2025), Zentel (oct. 2025), Glypressine n° 44470 (mars 2024), Augmentin n° 45674 (sept. 2026), Stragen n° 58459 (avr. 2026), Inflamac 50 n° 55926 (avr. 2026), etc. | corpus refdata |
| M2 | 176, 178, 201, 216, 218, 219 · T | « habituellement 4,5 g toutes les 8 h (AIPS CH Stragen, 2026) » | « 2,25 à 4,5 g 3–4×/j ; habituellement 100 à 200 mg de pipéracilline/kg/j (AIPS Stragen n° 58459, avr. 2026) » ; le schéma de 4,5 g toutes les 8 h n'est pas dans l'AIPS | AIPS Stragen |
| M3 | 171 · T2 | « résmétirom peut être envisagé … statut CH À vérifier » | Ajouter : « sémaglutide, seul autorisé en Suisse pour la MASH non cirrhotique F2–F3 : 0,25 mg/semaine, puis paliers sur 16 semaines jusqu'à 2,4 mg/semaine (AIPS Wegovy n° 68798, août 2026) ; résmétirom absent du corpus » | AIPS Wegovy |
| M4 | 167 · sources | « EASL … 2018 (mise à jour 2025 À vérifier) » ; « BCLC 2022 » ; « ACR LI-RADS v2018 » | « EASL CPG on the management of HCC, J Hepatol 2025;82:315–374 » ; « BCLC 2025 update, J Hepatol 2025;83:1234–1248 » ; LI-RADS (source américaine) après EASL 2025 | PubMed 39690085 ; Clínic Barcelona |
| M5 | 170 · gold.pourquoi | « ≥ 15 kPa = hypertension portale … probable avec plaquettes » | « ≥ 25 kPa : HTPCS affirmée ; ≤ 15 kPa et plaquettes ≥ 150 G/l : HTPCS exclue ; 15–25 kPa : zone grise (Baveno VII) » | Baveno VII |
| M6 | 190 · T1 | « embolisation si … grade AAST ≥ III » | « … si blush, ou si lésion WSES III (AAST IV–V) même sans blush (WSES 2017, 1B) » | WSES 2017 |
| M7 | 209 · T0 | « Hb cible 70–80 g/l, 80–100 g/l si cardiopathie » | « transfuser si Hb ≤ 70 g/l, cible 70–90 g/l ; avec une maladie cardiovasculaire : si Hb ≤ 80 g/l, cible ≥ 100 g/l (ESGE 2021, forte) » | ESGE 2021 |
| M8 | 193 · S0 ; 237 · S0, T0 | « ESVS 2017 » | « ESVS 2025 CPG on mesenteric and renal arteries and veins, Eur J Vasc Endovasc Surg 2025;70:153–218 » ; revoir les forces | ESVS 2025 |
| M9 | 184 · S1 | « IAP/APA … Pancreatology 2013 » | « IAP Revised Guidelines on Acute Pancreatitis 2025, Pancreatology 2025;25:770–814 » ; revoir les forces | Pancreatology 2025 |
| M10 | 213 · S0, T0 | « HerniaSurge 2018 » | « HerniaSurge update, BJS Open 2023;7:zrad080 » (réparation laparo-endoscopique ou prépéritonéale préférée) | BJS Open 2023 |
| M11 | 205 · S0, T0 | « Ntoulia … ESPR 2016 (À vérifier) » ; « ESPR 2020 : doit » | « ESPR Abdominal Task Force, procedural recommendations for intussusception reduction, Pediatr Radiol 2026;56:260–268 » ; la force « 2020 : doit » est sans source | PubMed 41364218 |
| M12 | 217 · premiere_intention | « Échographie … chez la femme enceinte, l'enfant et le patient jeune » | « Échographie en première intention chez tous (EAU 2026 : « primary diagnostic imaging tool ») ; TDM sans injection à faible dose pour confirmer » | EAU Urolithiasis 2026 |
| M13 | 191, 192, 204, 206, 207, 214, 227 (+ 215, 225) · sources | « Am J Emerg Med 2009 (non suisse, À vérifier) », « N Engl J Med 2011 », « Endocrine Society 2014 » | Sources américaines exclusives : chercher et citer une source suisse ou européenne, ou l'étiqueter « source américaine seule ». La revue NEJM 2011 sur l'ECUN est périmée. | règle Suisse → Europe → OMS |

## 3. Défauts mineurs (8)

| # | Id · champ | Extrait → PATCH |
|---|---|---|
| m1 | 196 · S1 ; 195, 201 · T | Les dates AIPS sont fausses : Vancocin « mai 2026 » → **mars 2026** ; Dificlir « 2025 » → **déc. 2024** ; Aldactone (170, 211) « 2026 » → **août 2025** ; Novalgin (176, 184, 217) « 2026 » → **sept. 2025** ; Ciprofloxacine Zentiva (218) « 2026 » → **août 2025** ; Propranolol Zentiva (225) « 2026 » → **janv. 2023** |
| m2 | 170, 209 · T | Glypressine : ajouter « < 50 kg : 1 mg toutes les 4–6 h ; 12 mg/j pendant 36 h au plus, **puis 6 mg/j** » |
| m3 | 217 · T1 | « hors indication AIPS CH (À vérifier) » → « hors indication (AIPS Tamsulosin-Mepha n° 58828, déc. 2023 : HBP seulement) » |
| m4 | 189 · T0 ; 203 · T0 ; 215 · T0 ; 233 · T3 | « hors texte AIPS — À vérifier » → « indication AIPS sans dose propre (Prednisone Streuli n° 29349, juin 2026 ; Solu-Medrol n° 35112, août 2025 : MICI, rejet de greffe) » |
| m5 | 196 · syndrome | « créatinine > 133 µmol/l » → « créatinine > 50 % au-dessus de la valeur de base, ou T > 38,5 °C (ESCMID 2021) » |
| m6 | 194 · T1 | « récidive ≈ 30 % à 5 ans » → « ≈ 39 % à 5 ans (APPAC) » |
| m7 | 217–223, 229, 231–233 · sources | « EAU … 2025 » → « EAU 2026 » (version la plus récente) |
| m8 | 186, 197, 198 · T | « doses AIPS CH À vérifier » pour FOLFIRINOX, FOLFOX, CAPOX et FLOT : citer le protocole ESMO et l'AIPS de chaque composant. **Ces AIPS ne sont pas contrôlées dans cet audit.** |

## 4. Verdict

**Corrections requises.** Le fichier contient 17 défauts critiques (« À vérifier » ou absence de dose alors que l'AIPS répond), 13 défauts majeurs et 8 mineurs. Aucun numéro Swissmedic n'est cité. Une contre-audition est nécessaire après correction.
Limites : je n'ai pas lu les AIPS des composants de FOLFIRINOX, FOLFOX, CAPOX et FLOT, ni le texte complet d'ESVS 2025, d'IAP 2025 et d'ESPR 2026. Je n'ai pas vérifié les forces ESVS 2024 du dépistage ni celles de la réparation d'une rupture.
