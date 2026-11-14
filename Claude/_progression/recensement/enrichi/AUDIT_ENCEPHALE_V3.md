# Audit médical V3 (dernier tour) : encéphale IMG-001 à IMG-041

Auditeur indépendant, 14.11.2026. J'ai appliqué les skills `medecin-expert` et `radiologue-expert`.

**Ce que j'ai fait**
- J'ai lu la section « Tour 2 » de CORRECTIONS_ENCEPHALE.md, puis chaque champ visé dans TC_encephale_a/b/c.json. Les trois JSON sont valides.
- J'ai relu dans le corpus refdata, par URL, les AIPS suivantes : Metronidazol B. Braun 48018, MabThera 54378, Endoxan 25441, Imurek 31887, CellCept 53337, Methotrexat Accord 66780, Leponex 37491, Seroquel 54182, Diamox 21191, Plavix 70367, Aspirine Cardio 51795, Solu-Medrol 35112, Avastin 56922, Diprophos 39528 et Exelon 54275.
- J'ai lu en ligne :
  - le texte du webinaire officiel ESO « ICH guideline » du 21.01.2026, qui reproduit la PICO 2 d'ESO-EANS 2025 ;
  - le résumé PubMed 42095756 (mise à jour 2025 de la recommandation ESO sur la pression artérielle, Eur Stroke J 2026) ;
  - le texte RCUK 2025, qui reprend ERC-ESICM 2025 ;
  - les SGGG Expertenbriefe n° 66 (texte intégral) et n° 56 (résumé).
- J'ai contrôlé par script que toutes les sources sont triées Suisse → Europe → autres → OMS et que chaque source non suisse porte son étiquette.

## 1. Défauts V2 : état

| Id | Défaut V2 | État |
|---|---|---|
| C1 031 | Bétaméthasone | **Corrigé.** Le texte dit « hors AIPS (Diprophos 39528) ». Le schéma de 2 × 12 mg i.m. à 24 h d'intervalle, entre 24+0 et 33+6 SA, correspond à SGGG EB 56. |
| C2 006 (et 001) | Antiagrégant | **Corrigé.** Clopidogrel 75 mg/j, AVC de 7 j à 6 mois. Aspirine Cardio 300 mg/j ou 100 mg 3×/j après AIT : conforme à l'AIPS. |
| C3 033, C4 040, C5 021 | « À vérifier » | **Corrigés.** Les mentions « hors AIPS » sont exactes. |
| C6 012, 021, 022, 030, 034, 035, 037 | « À vérifier » | **Corrigés.** Les indications et les dates sont conformes aux AIPS lues : MabThera déc. 2025, Endoxan févr. 2021, Imurek avr. 2026, Leponex juin 2026, Seroquel et Diamox juil. 2026. |
| M1 038 | Durée de prévention de la fièvre | **Corrigé.** Le texte dit « 36 à 72 h » et place le pronostic à ≥ 72 h après le retour à une circulation spontanée, facteurs confondants exclus (RCUK/ERC-ESICM 2025). |
| M2 008 | Métronidazole | **Corrigé.** L'écart avec l'AIPS 48018 est signalé mot pour mot (5–7 j, 10 j au plus, « cas isolés justifiés », 1er trimestre contre-indiqué). Le relais par Flagyl est retiré. |
| M3 031 | Source suisse | **Corrigé.** SGGG EB 66 : bolus de 4 g en 15 min, entretien facultatif de 1 g/h, 24 h au plus, entre 24+0 et 32+0 SA. Le texte est conforme. |
| M4 002/041 | Cible tensionnelle | Les **chiffres sont exacts** : < 140 mmHg dans les 6 h si l'hématome fait moins de 30 ml, pas de baisse de plus de 70 mmHg, pas de baisse active sous 110 mmHg, maintien < 140 mmHg jusqu'à 7 j. En revanche, la **force est fausse** (voir R1). |
| Mineurs V2 | Mephameson 50–100 mg, 015 « aspect injecté », bolus d'andexanet à 30 mg/min, vaccination antiméningococcique | Corrigés. |

## 2. Défauts restants

| Gravité | Id · champ | Extrait actuel | Patch exact | Preuve |
|---|---|---|---|---|
| **Majeur** R1 | 002 traitement[0] et 041 traitement[4] | « (source européenne : ESO-EANS 2025, suggestion, recommandation faible) » | « (source européenne : ESO-EANS 2025 et mise à jour ESO 2025 sur la pression artérielle : **consensus d'experts**, vote 15/15 ; la recommandation fondée sur les preuves juge le bénéfice net incertain, qualité faible) ». Ajouter aux sources de 002 et de 041 : « Sandset EC et al. 2025 update to ESO guideline on blood pressure management in acute ischaemic stroke and intracerebral haemorrhage. Eur Stroke J 2026;11(5):aakag004 (doi 10.1093/esj/aakag004) (source européenne) » | PICO 2 : « Expert consensus statements … Vote: 15/15 » ; recommandation fondée sur les preuves : « balance … uncertain … recruitment to ongoing RCTs », qualité faible. PubMed 42095756 : « expert consensus supports early systolic BP reduction to < 140 mmHg » |
| Mineur | 018 sources | L'OMS est citée en 2e position. « Thomas A, Noël G 2019 (À vérifier) » et « SIOP-Europe … » n'ont pas d'étiquette. | Ajouter « (source non suisse) » et « (source européenne) ». Placer l'OMS en dernier. | Règle de Vial |
| Mineur | 009 gold.premiere_intention, 019 gold.pourquoi[2], 038 gold.pourquoi[1] | « (ESCMID 2016) », « (EANO 2020) », « (ERC-ESICM) » | Écrire « (source européenne : ESCMID 2016) », et de même pour les deux autres. | Règle de Vial (étiquette entre parenthèses) |
| Mineur | 035 traitement[0] | Endoxan : « liste d'exemples sans cette maladie » | Ajouter : « la liste cite les vascularites systémiques, mais pas la vascularite primitive du SNC » | AIPS Endoxan 25441 |

**Règle « Suisse d'abord »** : les sources sont triées et étiquetées ; le seul écart est 018 (mineur). La seule source suisse trouvée est la SGGG (031), et elle est citée. Pour la SSI, la Swiss Stroke Society et le Swiss Resuscitation Council, je n'ai trouvé aucun document lisible ; ce n'est pas un défaut prouvé.

**Erreur nouvelle** : aucune dose ni aucune indication fausse n'a été introduite au tour 2. La seule nouvelle erreur est la force de la recommandation dans R1.

## 3. Verdict

**corrections requises** : il reste 1 majeur (R1, à corriger en 2 lignes et 2 sources) et aucun critique. Après application du patch R1, l'encéphale peut recevoir « audit-ok » sans nouveau tour.

## 4. Clôture (14.11.2026)
Patch R1 appliqué mot pour mot (002 traitement[0], 041 traitement[4], source Sandset 2026 ajoutée) ainsi que les quatre mineurs (018 ordre et étiquettes, 009/019/038 étiquettes, 035 nuance Endoxan). Conformément au verdict de l'auditeur (« après application du patch R1, l'encéphale peut recevoir audit-ok sans nouveau tour ») : **audit-ok**.
