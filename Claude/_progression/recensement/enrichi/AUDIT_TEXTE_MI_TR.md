# Audit médical agressif — champs texte de MI_TR.json (IMG-289 à IMG-344)

Auditeur indépendant, 14.11.2026. J'ai appliqué les skills `medecin-expert`, `radiologue-expert` et `expert-web`. Les images sont hors champ.

**Méthode (ce que j'ai fait)**
- J'ai lu les champs gold, premiere_intention, autres, syndrome, traitement et sources des 56 entrées.
- J'ai cherché chaque molécule avec `aips_fiche.py trouve` (corpus refdata du 08.10.2026). J'ai lu la fiche, puis le HTML brut quand la rubrique Posologie était tronquée : 27 AIPS au total.
- J'ai vérifié en ligne quatre points : UICC TNM 9e éd., ATLS 11e éd., classe de la recommandation ESC 2024 sur le rivaroxaban et existence d'une recommandation ESVS 2024 sur les anévrismes poplités.
- Barème : **Critique** = « À vérifier » sur une AIPS présente au corpus qui répond, ou texte AIPS faux. **Majeur** = recommandation périmée, force fausse, examen de référence faux, source américaine seule, écart AIPS non signalé. **Mineur** = date, précision, forme.

## 1. Défauts critiques (11)

| Id | Champ | Extrait fautif → PATCH | Preuve AIPS lue |
|---|---|---|---|
| 290 | traitement[1] | « acide tranexamique (dose : À vérifier, AIPS) » → « acide tranexamique 1 g i.v. en 10 min puis 1 g en 8 h, dans les 3 h suivant le traumatisme (source européenne : Rossaint et al., guideline européenne sur le saignement traumatique, 6e éd., 2023) ; hors schéma AIPS : l'AIPS donne 1 g i.v. lent toutes les 6–8 h dans la fibrinolyse générale (Acide tranexamique Stragen®, n° 65978, févr. 2024) » | Stragen 65978 et Nardia 70581 : posologie i.v. ; aucune ne cite le traumatisme |
| 291 | traitement[1] | « AINS … à dose minimale : À vérifier (AIPS) » → « AINS oral à dose minimale et pour une durée courte : ibuprofène 1200–1800 mg/j en plusieurs prises, puis 600–1200 mg/j en entretien (AIPS Ibuprofen-Mepha Teva, n° 49156, déc. 2024 ; indication « coxarthroses ») ; AINS topique d'abord si possible » | 49156 : Indications et Posologie |
| 308 | traitement[0] | « colchicine absente du corpus AIPS » est faux → « colchicine 1 mg puis 0,5 mg 2 h après, au maximum 2 mg/24 h le 1er jour, puis 0,5 mg 2–3×/j ; arrêt en cas de diarrhée ; au maximum 6 mg par crise (AIPS COLCTAB®, n° 67974) » | COLCTAB 67974, rubrique « Crise aiguë d'arthrite goutteuse » |
| 316 | traitement[1] | « clindamycine (doses : À vérifier, AIPS) » → « clindamycine i.v. 2400–2700 mg/j en 2–4 doses (infection très sévère), enfant 25–40 mg/kg/j (AIPS Clindamycin [Phosphat]-Mepha, n° 62980, août 2025), associée à une bêta-lactamine à large spectre » | 62980, tableau Posologie parentérale |
| 324 | traitement[0] | « doses : À vérifier (AIPS) » → « rituximab 375 mg/m² i.v. au J1 de chaque cycle CHOP (AIPS MabThera®, n° 54378, déc. 2025) ; autres cytostatiques selon le protocole du centre » | MabThera 54378 : Indications (LDGCB) et Posologie |
| 327 | traitement[0] | « intervalle de 3–4 semaines : À vérifier » → « toutes les 3 à 4 semaines, avec 500 mg de calcium et 400 UI de vitamine D par jour (AIPS) » | Onco Sandoz 62625 : texte lu mot pour mot |
| 327 | traitement[1] | « dénosumab 120 mg … (AIPS forme onco : À vérifier) » → « dénosumab 120 mg s.c. toutes les 4 semaines, avec au moins 500 mg de calcium et 400 UI de vitamine D par jour (AIPS XGEVA®, n° 61865, sept. 2026) » | XGEVA 61865 : Posologie usuelle |
| 332 | traitement[0] | « dose unique : À vérifier mot pour mot » → « dose unique de 5 mg i.v. ; une nouvelle perfusion en cas de rechute, au plus tôt 1 an après (AIPS Aclasta®, n° 57363, mars 2026) » | Aclasta 57363 : « Pour le traitement de la maladie de Paget… dose unique de 5 mg » |
| 333 | traitement[0] | « cholécalciférol absent du corpus AIPS » est faux → « traitement du rachitisme par vitamine D3 : nourrisson 500–1000 UI/j ; 1–18 ans 1000–5000 UI/j pendant 6 semaines, puis 500–1000 UI/j, sous contrôle de la calcémie (AIPS Vitamine D3 Spirig HC®, n° 69997, oct. 2025) » | 69997 : « Traitement du rachitisme » |
| 333 | traitement[1] | « burosumab (AIPS Crysvita : À vérifier) » → « burosumab s.c. : enfant dès 1 an 0,4 mg/kg toutes les 2 semaines, jusqu'à 2 mg/kg (90 mg au maximum) ; adulte 1 mg/kg toutes les 4 semaines (90 mg au maximum) ; arrêter phosphate oral et calcitriol 1 semaine avant (AIPS CRYSVITA, n° 66801, déc. 2025) » | 66801 : Posologie |
| 335 | traitement[1] | « vosoritide (AIPS : À vérifier) » → « vosoritide s.c. 1×/j, environ 15–30 µg/kg selon le poids (tableau AIPS), dès 4 mois tant que les cartilages de croissance sont ouverts, après confirmation génétique (AIPS Voxzogo®, n° 69569, oct. 2024) » | 69569 : Indications et Posologie |

## 2. Défauts majeurs (17)

| Id | Défaut | PATCH |
|---|---|---|
| 290, 337 | ATLS 10e éd. (2018) périmé ; l'ACS a lancé la 11e éd. en 2025 (xABCDE). La source européenne manque | « ATLS, 11e édition, 2025 (source américaine) » + « Rossaint R et al., European guideline on management of major bleeding and coagulopathy following trauma, 6e éd., Crit Care 2023 » |
| 291, 300 | EULAR 2018 ne traite que de la prise en charge non médicamenteuse : il ne fonde pas les lignes AINS ni paracétamol. Le paracétamol en 1re ligne est périmé | Remplacer « paracétamol puis AINS » par « AINS topique (genou) puis AINS oral à dose minimale » ; ajouter « ESCEO, algorithme arthrose, 2019 (source européenne) » |
| 296, 315 | La flucloxacilline seule couvre mal *Kingella kingae* (< 4 ans), que le texte cite lui-même | « < 4 ans : amoxicilline-acide clavulanique ou céfuroxime (source suisse : Paediatrica 34(4), 2023, à lire et à dater) ; flucloxacilline si *S. aureus* » |
| 296 | « SSI … : À vérifier » : source suisse non cherchée | Lire les recommandations PIGS et Paediatrica 2023, puis les citer datées |
| 304, 305 | « thromboprophylaxie : À vérifier » alors que l'AIPS Clexane® est au corpus | « énoxaparine 40 mg s.c. 1×/j si haut risque (AIPS Clexane®, n° 49456, févr. 2026) ; immobilisation plâtrée sans chirurgie : décision individuelle, hors indication explicite de l'AIPS » |
| 305 | AAOS 2010 : source américaine seule et ancienne | Chercher une source suisse ou européenne (ESSKA) ; sinon garder AAOS avec l'étiquette « source américaine » |
| 294, 295 | Sources américaines seules (AAFP 2017, StatPearls 2023) | Chercher une source suisse (pédiatrie) ou européenne (EPOS) ; sinon l'étiqueter « source américaine » |
| 309 | Gold faux : le pied bot est un diagnostic clinique, une radiographie « en charge » est impossible chez le nouveau-né et la méthode Ponseti n'utilise pas les angles radiographiques | gold « Examen clinique (score de Pirani) » ; radiographie réservée aux formes atypiques ou résistantes |
| 311 | Force fausse : ESC 2024 classe le rivaroxaban 2,5 mg 2×/j + AAS après revascularisation en IIa (« devrait »), pas « peut » | « … : devrait (ESC 2024, IIa) » ; préciser « ne pas débuter avant l'hémostase (AIPS) » |
| 313 | Source américaine seule (Webber, Circulation 2007) | Chercher une source européenne ; sinon l'étiqueter « source américaine » |
| 314 | « ESVS, Peripheral arterial aneurysms, 2024 » est introuvable. Le seuil de 20 mm vient de la SVS 2021 (américaine), qui le classe en recommandation forte | « SVS, Popliteal artery aneurysms, J Vasc Surg 2021 (source américaine) : réparer si ≥ 20 mm (forte) » ; supprimer la source ESVS |
| 316 | IDSA 2014 : source américaine seule | Ajouter « WSES/SIS-E, Skin and soft tissue infections, 2022 (source européenne) » |
| 325 | TNM 8e éd. périmée : l'UICC a publié la 9e éd. en juillet 2025, en vigueur depuis le 01.01.2026 | « UICC, TNM 9e édition, 2025 » |
| 329 | « dexaméthasone (dose : À vérifier, AIPS) » : Fortecortin® Inject (n° 48669) ne cite pas la compression médullaire | « dexaméthasone 16 mg/j (NICE NG234, 2023, non vérifié CH) ; hors indication AIPS (Fortecortin® : œdème cérébral seulement) » |
| 328 | La dose de corticoïde du grade 2 manque | « prednisone 0,5–1 mg/kg/j (ESMO 2022) » ; pas de corticoïde pour une thyroïdite isolée |
| 343 | Doses absentes. Actemra® n'est pas donné à une seule dose | « ACG débutante : 162 mg s.c. toutes les 2 semaines (1×/semaine possible) ; ACG récidivante : 1×/semaine ; prednisone < 60 mg/j à l'instauration (AIPS Actemra®, n° 58868, sept. 2026) » ; prednisone PPR 12,5–25 mg/j (EULAR/ACR 2015) |
| 344 | « rituximab (doses : À vérifier) » : la maladie à IgG4 ne figure pas dans l'AIPS MabThera® | « rituximab : hors AIPS (MabThera® n° 54378 n'a pas cette indication) » ; corticoïde initial 0,6 mg/kg/j (consensus international 2015, à lire) |

## 3. Défauts mineurs (10)

| Id | Défaut | PATCH |
|---|---|---|
| 311 | Date AIPS fausse : « 2026 » | « mai 2025 » |
| 331 | Alendronate Sandoz® 70 : « 2024 » est faux | « juillet 2023 » |
| 331 | Denosumab-Mepha osteo : « décembre 2025 » est faux | « septembre 2026 » |
| 289 | « ostéosynthèse (Garden I–II, sujet jeune) » mélange deux critères | « ostéosynthèse si Garden I–II, ou chez le sujet jeune quel que soit le stade ; arthroplastie si Garden III–IV chez le sujet âgé » |
| 299 | « seuil : À vérifier » | « marche articulaire > 2 mm (AO Surgery Reference, à lire) » |
| 334 | Le critère calcémie manque | ajouter « calcémie > 0,25 mmol/l au-dessus de la norme ; DFG < 60 ml/min ou lithiase » |
| 335 | « bisphosphonates (doses : À vérifier) » | « hors AIPS : aucune AIPS suisse ne cite l'ostéogenèse imparfaite » |
| 293, 340, 341 | Sources suisses marquées « À vérifier » (SGUM, Protection de l'enfant, niveaux de référence de l'OFSP) | Lire chaque source, la dater ou la retirer |
| 311 | « 6 P » écrit en anglais ; « ischémie permanente critique » | traduire les 6 P ; « ischémie chronique menaçant le membre (CLTI) » |
| 327 | EAU 2024 : l'association EAU met sa recommandation à jour chaque année | citer l'édition la plus récente |

## 4. Points confirmés conformes à l'AIPS lue

Clexane® 40 mg/j en prophylaxie, puis 1 mg/kg 2×/j ou 1,5 mg/kg 1×/j (49456, févr. 2026). Aclasta® après fracture du col (57363). Flucloxacilline 2–8 g/j ; enfant jusqu'à 100–150 mg/kg/j, au plus 33 mg/kg par dose (60092, janv. 2025). Allopurinol 100 mg/j au départ (70148, janv. 2025). Apixaban 10 mg 2×/j pendant 7 j, puis 5 mg 2×/j (70399, févr. 2024). Alendronate 70 mg par semaine, au moins ½ h avant le repas. Aclasta® 5 mg/an. Critères RECIST 1.1, Kocher, Lugano/Deauville et T-score OMS : exacts.

## Verdict

**Corrections requises.** Il faut appliquer les 11 défauts critiques et les 17 défauts majeurs avant `audit-ok`. Les défauts critiques tiennent tous à un « À vérifier » ou à une fausse mention « absent du corpus » sur une AIPS que j'ai trouvée et lue.
