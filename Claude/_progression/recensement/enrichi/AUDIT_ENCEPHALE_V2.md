# Audit médical V2 (contre-vérification) : encéphale IMG-001 à IMG-041

Auditeur indépendant, 14.11.2026. Je n'ai rien rédigé. J'ai appliqué les skills `medecin-expert` et `radiologue-expert`.

**Ce que j'ai fait**
- J'ai relu chaque champ visé par AUDIT_ENCEPHALE.md dans TC_encephale_a/b/c.json. Les trois JSON sont valides.
- J'ai relu dans le corpus refdata (cache local, texte AIPS) les AIPS suivantes : Rocephin 44625, Mephameson 31890, Fortecortin Inject 48669, Dexaméthasone Galepharm 66710, Metronidazol B. Braun 48018, Sulfate de Mg Bichsel 56394, Sabril 50043, Voranigo 69364, Ondexxya 67759, Pradaxa 61385, Amoxicillin OrPha 68815, Soliris 59282, Ultomiris 67278, Keppra 55297, Solu-Medrol 35112, Avastin 56922, Diprophos 39528, Plavix 70367, Aspirine Cardio 51795, Exelon 54275, Daraprim 20964 et Cyklokapron 33741.
- J'ai lu les sources en ligne : le résumé PubMed ESCMID 2024 (abcès), le résumé ESO-EANS 2025, le texte RCUK 2025 « Post-resuscitation care », qui reprend ERC-ESICM 2025, le résumé Saidha 2025 et le SGGG Expertenbrief n° 66.
- J'ai regardé les images 004, 006, 014, 015 et 028, ainsi que les surcharges `_verif` de 004, 006, 010, 013, 014, 015, 028 et 039.

## 1. Défauts du 1er audit : état

| Id | Défaut | État |
|---|---|---|
| 002, 004, 007, 009 ×2, 014, 018, 030, 040 (critiques) | Doses et indications | **Corrigés.** Le texte est conforme à l'AIPS lue : andexanet 400 mg + 4 mg/min ou 800 mg + 8 mg/min ; MgSO4 dans l'éclampsie, 4–6 g en 10 min puis 1 g/h ; dexaméthasone chez l'enfant, 0,15 mg/kg/6 h × 4 j ou 0,4 mg/kg/12 h × 2 j ; amoxicilline 2 g en 30 min, 3 à 6 ×/j ; vorasidénib 40 mg/j si ≥ 40 kg ; Fortecortin chez l'enfant, 0,5–1 mg/kg puis 0,25–0,5 mg/kg/j ; vigabatrine 50 mg/kg/j, « jusqu'à 150 mg/kg/j administrées » ; Galepharm dans les radiolésions, 8–12 mg puis 4 mg/6 h. |
| 031 (critique) | Bétaméthasone | **Non corrigé, et la correction contient une erreur** (voir C1). |
| 033 (critique) | Éculizumab et ravulizumab | Corrigé : l'indication NMOSD AQP4+ de l'adulte est lue dans les deux AIPS. |
| 002, 041, 003, 017, 032, 034 (majeurs) | Sources périmées | Corrigés. Les DOI et les années sont exacts. Le seuil OCT de 6 µm est conforme à Saidha 2025. |
| 004, 006, 014, 015, 028 (images) | Paires d'images | **Corrigées.** 004 : la coupe axial_23 passe par la citerne quadrigéminale, au même niveau que le cliché pathologique. 006 : la nouvelle paire FLAIR axiale est comparable. 014 : le vrai mismatch T2-FLAIR est visible, et les repères 1 (T2), 2 (centre FLAIR) et 3 (liseré) sont justes. 015 et 028 : le plan et la fenêtre sont désormais identiques ; les limites sont signalées. |
| 010, 013, 039 (repères) | Position des repères | **Corrigés.** 010 : le n° 1 tombe sur le temporal interne droit. 013 : le n° 3 tombe sur la corne frontale droite effacée. 039 : les repères 1 à 3 tombent sur l'hippocampe gauche. |
| 008 (abcès) | Durée de traitement | La durée de 6–8 semaines est **exacte** (ESCMID 2024 : conditionnelle, preuves faibles ; aucune recommandation sur le relais oral précoce). L'écart avec l'AIPS reste à signaler (voir M2). |
| 038 (post-arrêt cardiaque) | Température et PAM | Le seuil ≤ 37,5 °C et la PAM > 60–65 mmHg sont **exacts**. La durée « ≥ 72 h » est **fausse** (voir M1). |
| 024–027, 026, 005/007/014, 037, 021 | Autres majeurs et mineurs | Corrigés. |

## 2. Défauts restants ou introduits

| Gravité | Id · champ | Extrait actuel | Patch exact | Preuve |
|---|---|---|---|---|
| **Critique** C1 | 031 traitement[0] | « bétaméthasone : AIPS absente du corpus, À vérifier » | « bétaméthasone : hors AIPS (Diprophos®, Swissmedic 39528, mars 2026 : aucune indication de maturation pulmonaire ; l'AIPS signale un risque d'hypoglycémie néonatale après 33 SA) ; schéma selon SGGG (Expertenbrief n° 56) » | Diprophos 39528 lue |
| **Critique** C2 | 006 traitement[1] | « antiagrégant après un AVC lacunaire symptomatique (molécule et dose : À vérifier) » | « clopidogrel (Plavix®) 75 mg 1×/j après un AVC récent (7 j à 6 mois) (AIPS Swissmedic 70367, sept. 2022), ou aspirine (AIPS Aspirine Cardio®, Swissmedic 51795, mars 2026 : 300 mg/j après AIT ; les 100 mg/j usuels en Europe sont hors schéma AIPS) » | Plavix, Aspirine Cardio |
| **Critique** C3 | 033 traitement[0] | « indication NMO hors libellé SEP, À vérifier » | « hors AIPS (Solu-Medrol®, Swissmedic 35112, août 2025 : poussées aiguës de SEP seulement) » | Solu-Medrol |
| **Critique** C4 | 040 traitement[2] | « bévacizumab (hors indication de l'AIPS, À vérifier) » | « bévacizumab : hors AIPS (Avastin®, Swissmedic 56922, mai 2026 : glioblastome récidivant seulement) » | Avastin |
| **Critique** C5 | 021 traitement[0] | « démence à corps de Lewy hors AIPS, À vérifier » | Supprimer « À vérifier ». L'AIPS Exelon (janvier 2024) indique la démence d'Alzheimer et la démence parkinsonienne seulement. | Exelon 54275 |
| **Critique** C6 | 001[5], 012[1], 021[1–2], 030[3], 034[1], 035[0–1], 037[1] | « doses À vérifier », « (À vérifier) » | Lire l'AIPS de chaque molécule (Aspirine Cardio, Plavix, Solu-Medrol, Seroquel 54182, Leponex 37491, Trittico 46559, MabThera 54378, Endoxan 25441, Minirin 43585). Écrire ensuite la dose AIPS, ou « hors AIPS (n°, indication) ». | Molécules présentes au corpus. Le 1er audit ne les avait pas relevées. |
| **Majeur** M1 | 038 traitement[0] | « (cible ≤ 37,5 °C) pendant au moins 72 h » | « pendant 36 à 72 h » | ERC-ESICM 2025, repris par RCUK 2025 : « Prevent active fever for 36 to 72 h » |
| **Majeur** M2 | 008 traitement[1–2] | « Durée totale de 6 à 8 semaines » ; « Flagyl® comprimés pour un relais oral » | Ajouter : « écart : l'AIPS Metronidazol B. Braun (48018, févr. 2026) prévoit 5–7 j, 10 j au plus en règle générale, et contre-indique le 1er trimestre de grossesse ». Remplacer « Flagyl… relais oral » par « relais oral non recommandé faute de données (ESCMID 2024) ». | AIPS 48018 ; résumé ESCMID |
| **Majeur** M3 (source suisse) | 031 traitement[0], sources | Aucune source suisse ; MgSO4 sans schéma | « MgSO4 entre 24+0 et 32+0 SA : bolus unique de 4 g en 15 min ; 1 g/h facultatif, 24 h au plus (SGGG Expertenbrief n° 66, 16.12.2019) » ; ajouter la source | Texte SGGG lu |
| **Majeur** M4 | 002[0] et 041[4] | La cible de « 140 mmHg » n'a pas été relue dans le texte 2025. 041 l'attribue à ESO-EANS 2025 sans réserve. | Lire le texte intégral (PMC12098356), sinon écrire dans 041 la même réserve que dans 002. | Résumé : « acute blood pressure lowering » = faible, sans chiffre |
| Mineur | 024–027 | « AIPS (Mephameson®, …) … (40–100 mg i.v.) » | « 40–100 mg (Galepharm, Fortecortin) ; 50–100 mg (Mephameson) » | Mephameson 31890 |
| Mineur | 038[2] | « au moins 72 h après normothermie » | « ≥ 72 h après la RACS, facteurs confondants (sédation) exclus » | RCUK/ERC 2025 |
| Mineur | 015 normal.technique | « injection non précisée » | « aspect injecté probable (sinus caverneux et veines corticales rehaussés) » | Image regardée |
| Mineur | 002/041 ; 033 | Débit du bolus d'andexanet absent ; vaccination antiméningococcique absente | « bolus à 30 mg/min » ; « vaccination antiméningococcique obligatoire avant éculizumab ou ravulizumab (AIPS) » | Ondexxya ; Soliris/Ultomiris |
| Mineur | 004, 006 | Images de 252 px et 250 px de large | Remplacer si une version plus large existe. | — |

**Critère de Vial « Suisse d'abord »** : je n'ai confirmé de source suisse que pour 031 (SGGG, voir M3). Les sources suisses déjà citées (OFSP 028, Swiss Memory Clinics 021) sont conformes. Pour l'ESCMID (008, 009 : SSI), l'ESO (002–006, 041 : Société suisse de neurologie / Swiss Stroke Society) et l'ERC (038 : Swiss Resuscitation Council), je n'ai trouvé aucun document suisse lisible : le site ssi.guidelines.ch est vide sans JavaScript. Ces cas restent « non vérifié CH », ce qui n'est pas un défaut prouvé. Les sources non suisses figurent bien entre parenthèses.

## 3. Verdict

**corrections requises** : il reste 6 lignes critiques (C1 à C6, des « À vérifier » sur des molécules présentes au corpus) et 4 majeures (M1 à M4). Les défauts d'images et de repères sont tous corrigés.
