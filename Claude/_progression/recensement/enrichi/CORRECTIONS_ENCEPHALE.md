# Corrections — encéphale IMG-001 à IMG-041 (réponse à AUDIT_ENCEPHALE.md)

Correcteur, 14.11.2026. Skills `medecin-expert` et `radiologue-expert` appliqués. Fichiers modifiés : `TC_encephale_a/b/c.json`, `img/IMG-004_normal`, `IMG-006_normal/patho`, `IMG-014_normal/patho`, `IMG-015_normal`, `IMG-028_normal`, `_verif/IMG-004, 006, 010, 013, 014, 015, 028, 032, 039.png`.
Doses : chaque dose a été relue dans l'AIPS avec `aips_fiche.py` (corpus refdata AipsDownload_20261008, rubrique Posologie, n° et « Mise à jour » cités). JSON valide ; `generer.py` sans erreur.

## 1. Critiques (10/10 appliqués)

| Id | Décision | Vérification |
|---|---|---|
| 002 | Appliqué : andexanet alfa 400 mg + 4 mg/min 120 min ou 800 mg + 8 mg/min 120 min, selon molécule, dose et délai ; ajout : excès d'événements thromboemboliques (ESO-EANS 2025) | Ondexxya 67759, avril 2025, tableau 1 |
| 004 | Appliqué : dabigatran hors AIPS | Pradaxa 61385, février 2024 : FA non valvulaire, TVP/EP |
| 007 | Appliqué : 4–6 g i.v. en 10 min puis 1 g/h | Bichsel 56394, octobre 2025, « En cas de crise d'éclampsie » |
| 009 [0] | Appliqué : ESCMID adulte 10 mg/6 h × 4 j hors schéma AIPS ; AIPS enfant 0,15 mg/kg/6 h × 4 j (ou 0,4 mg/kg/12 h × 2 j), avant la 1re antibiothérapie | Mephameson 31890, juin 2022 (méningite dans les indications) |
| 009 [2] | Appliqué : amoxicilline 2 g en 30 min, 3 à 6 ×/j | Amoxicillin OrPha 68815, février 2026 (méningite indiquée) |
| 014 | Appliqué : vorasidénib 40 mg 1×/j si ≥ 40 kg, jusqu'à progression ou intolérance | Voranigo 69364, mars 2026 |
| 018 | Appliqué : 0,5–1 mg/kg puis 0,25–0,5 mg/kg/j en 4 prises | Fortecortin Inject 48669, juin 2022 |
| 030 | Appliqué, formulation corrigée : 50 mg/kg/j, ajustable en une semaine ; jusqu'à 150 mg/kg/j « ont été administrées » avec bonne tolérance (l'AIPS ne fixe pas 150 mg/kg/j comme cible) | Sabril 50043, avril 2026 |
| 031 | Appliqué : MgSO4 neuroprotection hors AIPS (AIPS : tocolyse 4 g puis 1–2 g/h) ; bétaméthasone : `trouve Celestone` → absente du corpus, « À vérifier » maintenu | Bichsel 56394 |
| 033 | Appliqué : éculizumab (NMOSD AQP4+ adulte, forme récurrente) et ravulizumab (NMOSD AQP4+ adulte) | Soliris 59282, avril 2026 ; Ultomiris 67278, février 2026 |
| 040 | Appliqué : 8–12 mg i.v. puis 4 mg i.v./i.m. toutes les 6 h (radiolésions) | Dexaméthasone Galepharm 66710, juin 2022 |

## 2. Majeurs

| Id | Décision |
|---|---|
| 002, 041 | Appliqué. ESO-EANS 2025 (Eur Stroke J 2025;10(4):1007-86) vérifiée sur PubMed : baisse tensionnelle aiguë et évacuation du cérébelleux > 15 ml = recommandations faibles. La cible de 140 mmHg n'a pas pu être relue dans le texte intégral (page PMC trop longue, XML non fourni) : je l'ai gardée et signalée « reprise d'ESO 2014, non relue ». |
| 003 | Appliqué. ESO/EANS/ESMINT 2026 (doi 10.1093/esj/aakag043), résumé relu : nimodipine orale et coils plutôt que clip (preuves élevées) ; exclusion dans les 24 h (consensus d'experts). Nimodipine orale placée en premier, voie i.v. de l'AIPS gardée en alternative. |
| 004 | Appliqué, avec une autre coupe que celle de l'audit : axial_20 passe par les atriums, plus haut que le cliché pathologique. J'ai choisi axial_23 (CC0, mésencéphale, citerne quadrigéminale), qui correspond au cliché pathologique. Le champ technique « fosse postérieure » est corrigé. |
| 005, 007, 014 | Appliqué : lévétiracétam 500 mg 2×/j dès le 1er jour, jusqu'à 1500 mg 2×/j (Keppra 55297 ; la date de l'AIPS est bien avril 2023). |
| 006 | Appliqué autrement. La série `Brain_MRI_FLAIR_Cor` ne compte qu'une seule image sur Commons, et aucun FLAIR coronal normal libre n'existe au niveau des cornes frontales. J'ai donc remplacé la **paire entière** par une paire axiale FLAIR comparable : normal `Mri_Brain_Flair_Axial_(12)` (511KeV, CC BY-SA 4.0) et pathologique `Leukoaraiosis.jpg` (Dudall, CC BY-SA 3.0). J'ai posé 2 repères nouveaux et contrôlé `_verif/IMG-006.png`. Les mineurs de 006 (Fazekas, dilatation) visaient l'ancienne image : la sémiologie est réécrite selon la nouvelle (« Fazekas profond 2 »). |
| 008 | Appliqué avec correction. Ceftriaxone 4 g/j, dose maximale de l'AIPS, mais l'AIPS la donne **en une prise** : le fractionnement 2 × 2 g est signalé « hors schéma AIPS ». Le résumé ESCMID 2024 a été relu : la durée est de **6–8 semaines** (conditionnelle, preuves faibles), et ESCMID ne fait **aucune recommandation** sur le relais oral précoce. L'ancien texte « relais oral après ≈ 2 semaines » était donc faux : il est retiré. Le métronidazole i.v. est cité selon l'AIPS Metronidazol i.v. B. Braun 48018 (février 2026, abcès cérébral dans les indications) : 15 mg/kg, puis 7,5 mg/kg toutes les 6 h pendant 3 j, puis toutes les 12 h. Flagyl est présenté comme relais oral. |
| 010 | Appliqué (33, 63) ; vérifié sur `_verif` : la pointe est sur le temporal interne. |
| 013 | Appliqué (43,5 ; 36,5) ; vérifié : la pointe est sur la corne frontale droite rétrécie. |
| 014 | Appliqué en remplaçant l'image fautive. Le nouveau cliché pathologique est `Astrocytoma,_grade_2,_T2-FLAIR-Mismatch.jpg` (Corell et al., BMC Cancer 2020, CC BY 4.0). C'est un vrai mismatch : T2 et FLAIR côte à côte, sur un astrocytome de grade 2 (statut IDH non analysé, ce que dit le champ technique). Le normal est un montage T2 + FLAIR au même niveau (511KeV, CC BY-SA 4.0). Il porte 3 repères (hypersignal T2, centre supprimé en FLAIR, liseré), contrôlés sur `_verif`. PCV/témozolomide : hors AIPS (Temodal 54577, décembre 2021 : glioblastome, gliome malin récidivant). |
| 015 | Appliqué en partie. Il n'existe pas de série `MRI_Brain_T1_Cor` sur Commons. J'ai pris un T1 coronal libre (`Cavum_septi_pellucidi_MRT_cor_T1.jpg`, Hellerhoff, CC BY-SA 3.0) : il est dans le même plan, mais la coupe est plus antérieure et l'injection n'est pas précisée. Les deux limites sont écrites dans le champ technique. |
| 017 | Appliqué : EHA-ESMO 2024 (Ann Oncol 2024;35:491-507, doi vérifié sur PubMed). Le texte intégral n'a pas été lu, ce qui est signalé. Le traitement (MATRix, consolidation) était déjà conforme. |
| 024, 025 | Appliqué : NICE NG232 (2023) et Undén 2013 ajoutés ; BTF/Bullock marqués « (non vérifié CH/UE) ». |
| 024–027 | Appliqué : l'écart avec l'AIPS est signalé (Galepharm 66710 : œdème post-traumatique 40–100 mg i.v., texte lu), avec CRASH 2004 et « ne doit pas être prescrite ». |
| 026 | Appliqué : CRASH-3 1 g en 10 min puis 1 g en 8 h ; hors AIPS (Cyklokapron 33741, juin 2026 : indications relues, sans le traumatisme crânien). |
| 028 | Appliqué : normal en fenêtre osseuse `CT-Felsenbein-10.jpg` (Hellerhoff, CC BY 3.0, série anatomique). Il est un peu plus bas que le cliché pathologique, ce qui est signalé. |
| 032 | Appliqué : McDonald 2024 (Lancet Neurol 2025;24:850-65, résumé relu) avec 5 topographies, veine centrale et anneau paramagnétique, chaînes légères κ, PEV et OCT (Saidha 2025). |
| 034 | Appliqué : Solu-Medrol (35112, août 2025 ; « selon les données publiées », SEP 500–1000 mg/j pendant 3–5 j). Ig i.v. : Privigen nommé, hors AIPS. |
| 038 | Appliqué. ERC-ESICM 2025 (Intensive Care Med 2025;51:2213-88, doi vérifié) : prévention de la fièvre **≤ 37,5 °C** pendant ≥ 72 h et PAM > 60–65 mmHg. Ces valeurs viennent de résumés secondaires concordants, faute d'accès au texte intégral, ce que signale la source. Le seuil 37,7 °C de 2021 est retiré. |

## 3. Mineurs

Appliqués :
- 001 ESVS 2023 (70–99 % / 50–69 %) ;
- 005 « MAV non illustrée » ;
- 007 semio PRES et niveaux différents ;
- 008, 009, 013, 016, 017 « contraste différent » ;
- 009 contraste leptoméningé subtil ;
- 011 EHA-ESMO 2024 et EACS 13.0 (chapitre non relu, « À vérifier ») ;
- 012, 018, 019, 029, 030 mentions de niveau, séquence ou âge ;
- 020 p-tau217 et repère 1 renommé ;
- 021 Exelon janvier 2024 (vérifié) et DFT non illustrée ;
- 022, 035 « (non vérifié CH/UE) » ;
- 025 photo d'écran signalée ;
- 026 « frontal antérieur », « second foyer de contrecoup » et LAD non illustrées ;
- 027 NaCl 10 % hors AIPS (Sintetica 56539 : hyponatrémie…) ;
- 028 vaccination : Plan de vaccination suisse 2026 (OFSP/CFV, février 2026, PDF lu : fracture de la base / fistule de LCR = groupe à risque, PCV) ;
- 032 repère 2 (substance blanche profonde, vérifié sur la grille) ;
- 037 Minirin février 2024 (vérifié) et Spasovski « doit (1D) » ;
- 039 repère 3 ajouté et repères 1 et 3 écartés pour ne pas se superposer, puis vérifiés au zoom.

Non appliqués :
- 002 : repère d'inondation ventriculaire non ajouté, faute d'inondation démontrée sur le cliché, comme le prévoit l'audit.
- 009 : source ssi.guidelines.ch non ajoutée (non lue).
- 018 : la référence SIOP-E/EANO datée n'a pas été retrouvée ; « À vérifier » est maintenu, pour ne rien inventer.
- 038 : l'hypothermie néonatale reste sourcée ERC 2021 ; la version 2025 n'a pas été relue (signalé).

## 4. Sigle
« PIC » (pression intracrânienne) → « pression intracrânienne » en toutes lettres (1 occurrence, IMG-026). Aucune autre occurrence dans les trois fichiers.

---

# Tour 2 (réponse à AUDIT_ENCEPHALE_V2.md, 14.11.2026)

Skills `medecin-expert`, `radiologue-expert` et `expert-web` appliqués. `aips_fiche.py` a été appelé avec l'URL refdata, jamais avec un simple numéro ; le texte a été relu dans la rubrique Posologie ou Indications, puis daté. JSON valide ; `generer.py` sans erreur.

## Critiques
| Id | Décision | Preuve lue |
|---|---|---|
| C1 031 | Appliqué. Bétaméthasone 2 × 12 mg i.m. à 24 h d'intervalle entre 24+0 et 33+6 SA (SGGG, Expertenbrief n° 56, 03.05.2019). Hors AIPS : Diprophos n'a aucune indication de maturation pulmonaire et signale l'hypoglycémie néonatale après 33 SA. | Diprophos 39528 (mars 2026) : indications et rubrique Grossesse ; EB 56 lu en ligne (rosenfluh) |
| C2 006 | Appliqué : clopidogrel 75 mg 1×/j (AVC récent, 7 j à environ 6 mois) ; Aspirine Cardio après AIT 300 mg 1×/j **ou 100 mg 3×/j** (l'AIPS dit les deux) ; 100 mg/j hors schéma AIPS. | Plavix 70367 (sept. 2022) ; Aspirine Cardio 51795 (mars 2026) |
| C3 033 | Appliqué : méthylprednisolone hors AIPS dans la NMO (Solu-Medrol : poussées de SEP seulement, parmi les indications neurologiques). | Solu-Medrol 35112 (août 2025) |
| C4 040 | Appliqué : bévacizumab hors AIPS (au niveau cérébral, Avastin n'indique que le glioblastome récidivant après témozolomide). | Avastin 56922 (mai 2026) |
| C5 021[0] | Appliqué : « À vérifier » supprimé ; Exelon n'indique que la démence d'Alzheimer et la démence parkinsonienne. | Exelon 54275 (janvier 2024) |
| C6 | Appliqué pour chaque ligne : 001[5] Plavix/Aspirine ; 012[1] Solu-Medrol hors AIPS (syndrome de reconstitution immunitaire absent des indications), 012[2] reformulé sans « À vérifier » ; 021[1] quétiapine hors AIPS (Seroquel « non homologué » chez le dément âgé) et clozapine hors AIPS (Leponex : psychose parkinsonienne seulement) ; 021[2] trazodone hors AIPS (Trittico : troubles dépressifs) ; 030[3] Aspirine Cardio hors AIPS ; 034[1] et 035[0] rituximab hors AIPS (MabThera : vascularites à ANCA, pas l'encéphalite ni la vascularite primitive du SNC) et cyclophosphamide (Endoxan : « maladies auto-immunes d'évolution menaçante », liste d'exemples ; posologie générale 10–15 mg/kg tous les 2–5 j) ; 035[1] Imurek, CellCept et Methotrexat Accord hors AIPS ; 037[1] Minirin hors AIPS (diabète insipide central, test). Ajouté de moi-même : 022 acétazolamide hors AIPS (Diamox 21191, juillet 2026). | Seroquel 54182, Leponex 37491, Trittico 46559, MabThera 54378, Endoxan 25441, Imurek 31887, CellCept 53337, Methotrexat Accord 66780, Minirin 43585, Diamox 21191 |

## Majeurs
| Id | Décision |
|---|---|
| M1 038 | Appliqué : prévention de la fièvre pendant 36 à 72 h. Mineur 038[2] : pronostic évalué 72 h ou plus après le retour à une circulation spontanée, sédatifs, opioïdes et curares exclus. Texte RCUK 2025 (reprise d'ERC-ESICM 2025) lu le 14.11.2026. |
| M2 008 | Appliqué : écart signalé avec l'AIPS 48018 (5–7 j, en règle 10 j au plus, 1er trimestre contre-indiqué) ; Flagyl en relais oral retiré ; « relais oral précoce non recommandé faute de données (ESCMID 2024) ». |
| M3 031 | Appliqué : SGGG, Expertenbrief n° 66 du 16.12.2019, lu en texte intégral (PDF Gynäkologie 2020/03) : bolus unique de 4 g en perfusion courte de 15 min, entretien facultatif de 1 g/h, 24 h au plus, entre 24+0 et 32+0 SA. |
| M4 002/041 | Appliqué. Le tableau 2 de l'ESO-EANS 2025 a été lu sur PMC12098356 (le lecteur web en a donné un extrait cité ; le XML intégral n'est pas fourni par l'éditeur). Sa formulation : pression systolique < 140 mmHg dans les 6 h si l'hématome est mineur ou modéré (< 30 ml) ; pas de baisse > 70 mmHg ni de baisse active sous 110 mmHg ; maintien < 140 mmHg jusqu'à 7 j ; suggestion, recommandation faible. La même phrase figure dans 002 et 041. |

## Mineurs
Appliqués :
- 024–027 : la dose initiale post-traumatique est donnée AIPS par AIPS (40–100 mg pour Fortecortin et Galepharm, **50–100 mg** pour Mephameson, texte lu).
- 015 : la mention « aspect injecté probable » est ajoutée.
- 002 et 041 : le bolus d'andexanet est passé « à 30 mg/min » (Ondexxya).
- 033 : la vaccination antiméningococcique est notée obligatoire avant éculizumab ou ravulizumab (Soliris et Ultomiris, texte lu).

Non appliqué :
- 004 et 006 : les images restent étroites (252 et 250 px), car Commons ne fournit pas de version plus large de ces fichiers.

## Règle de Vial « Suisse d'abord »
- **Traitements** : chaque mention d'une société non suisse entre parenthèses est désormais préfixée « source européenne : » (ESO, ESCMID, EANO, EHA-ESMO, EACS, ERC-ESICM, ESVS, EAN/MDS-ES, Spasovski 2014). La même règle vaut pour « source américaine : » (Brain Trauma Foundation, Angioma Alliance) et « source britannique : » (ABN/BIA).
- **Sources** : elles sont triées Suisse (AIPS, OFSP, SGGG, Swiss Memory Clinics) → Europe → autres → OMS en dernier. Toute source non suisse porte son étiquette : « (source européenne) », « (source britannique) », « (source américaine) », « (source internationale) », « (étude, source non suisse) » ou « (dernier recours : OMS) ».
- **Versions suisses cherchées sans succès** (portes essayées) :
  - Hémorragie cérébrale (Swiss Stroke Society) : recherche web FR/DE « Empfehlungen Hirnblutung », sans résultat. Seul le registre suisse (Bettschen 2024, BORIS) est sorti, et ce n'est pas une recommandation.
  - Réanimation (Swiss Resuscitation Council) : seule une présentation « Reanimation 2025 » de SIRMED/SRC est sortie, sans texte d'adoption lisible.
  - Méningite et abcès (SSI) : ssi.guidelines.ch reste vide sans JavaScript (constat de l'auditeur V2 confirmé).
  
  Ces cas restent cités en source européenne.
- **Seule source suisse ajoutée** : SGGG EB 66 et EB 56 pour IMG-031.

## « À vérifier » restants (hors périmètre du V2, aucun ne cache une AIPS du corpus qui répondrait)
- 007 : cible tensionnelle du PRES.
- 009 : vancomycine selon la résistance suisse.
- 010 : prolongation de l'aciclovir.
- 011 : schéma EACS 13.0.
- 023 : EAN/MDS-ES.
- 027 : dose de NaCl hypertonique.
- 032 : traitements de fond de la SEP.
- 039 : antiépileptiques.
- IMG-018 : SIOP-E.
- IMG-038 : nouveau-né ERC 2025.
- IMG-031 : imagerie, Société suisse de néonatologie.
