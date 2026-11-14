# Audit médical agressif — encéphale IMG-001 à IMG-041 (TC_encephale_a/b/c.json)

Auditeur indépendant, 14.11.2026. Skills `medecin-expert` et `radiologue-expert` appliqués.

**Méthode (ce qui a été fait réellement)**
- Lecture intégrale des 41 entrées.
- AIPS : 40 fiches lues dans le corpus refdata (`aips_fiche.py trouve/fiche`, cache local). Pour chacune, contrôle de la dose, de l'indication et de la date « Mise à jour ».
- Images : 35 paires examinées. J'ai produit ma propre surcharge des repères (pointe x,y ; départ fx,fy) depuis le JSON, avec un zoom sur IMG-013, IMG-016 et IMG-032. 6 entrées sont en `manque` (033, 034, 035, 038, 040, 041) : ce choix est accepté.
- Recommandations : la version la plus récente a été vérifiée en ligne (ESO SAH 2026, ESO-EANS ICH 2025, McDonald 2024, ERC-ESICM 2025, EHA-ESMO PCNSL 2024).

**Gravité**
- **Critique** : texte AIPS faux, ou « À vérifier » sur une molécule dont l'AIPS figure au corpus et répond à la question.
- **Majeur** : recommandation périmée, repère faux, paire non comparable, écart AIPS/recommandation non signalé, source américaine exclusive.
- **Mineur** : précision, forme, date.

---

## 1. Défauts critiques (10)

| Id | Champ | Ancien → nouveau (PATCH) | Preuve AIPS lue |
|---|---|---|---|
| 002 | traitement[5] | « anti-Xa : andexanet alfa ou concentré de complexe prothrombinique : À vérifier. » → « apixaban ou rivaroxaban : andexanet alfa (Ondexxya®) 400 mg en bolus puis 4 mg/min pendant 120 min (faible dose) ou 800 mg puis 8 mg/min pendant 120 min (dose élevée), selon la molécule, la dose et le délai depuis la prise (AIPS) ; sinon concentré de complexe prothrombinique. » + sources : « AIPS Ondexxya® (Swissmedic 67759), mise à jour avril 2025 » | Ondexxya 67759, tableau 1. La même entité est déjà correcte dans IMG-041. |
| 004 | traitement[2] | « dabigatran possible (RE-SPECT CVT 2019) : statut AIPS À vérifier » → « dabigatran : hors AIPS (Pradaxa® : fibrillation auriculaire non valvulaire, TVP/EP seulement) ; RE-SPECT CVT 2019 le montre aussi sûr que la warfarine, mais ESO 2017 ne recommande pas les AOD (faible) » | Pradaxa 61385, Indications, févr. 2024 |
| 007 | traitement[2] | « sulfate de magnésium … (dose AIPS : À vérifier) » → « éclampsie : sulfate de magnésium 4–6 g i.v. en 10 min, puis 1 g/h en perfusion continue (AIPS Sulfate de magnésium « Bichsel », Swissmedic 56394, oct. 2025) ; extraction fœtale » | Bichsel 56394, Posologie « En cas de crise d'éclampsie » |
| 009 | traitement[0] | « dose hors AIPS Mephameson®, qui ne précise pas cette indication » → « adulte : schéma ESCMID 10 mg toutes les 6 h pendant 4 j (hors schéma AIPS) ; l'AIPS Mephameson® cite la méningite (œdème cérébral) et donne chez l'enfant 0,15 mg/kg toutes les 6 h pendant 4 j, à débuter avant la première antibiothérapie » | Mephameson 31890 : Indications et Posologie pédiatrique. Le texte actuel est **faux**. |
| 009 | traitement[2] | « Ajouter l'amoxicilline … : dose AIPS À vérifier » → « Ajouter l'amoxicilline i.v. si risque de Listeria : infections sévères 2 g en perfusion de 30 min, 3 à 6 fois par jour (AIPS Amoxicillin OrPha, Swissmedic 68815, févr. 2026) ; ESCMID 2016 : 2 g toutes les 4 h » | Amoxicillin OrPha 68815 : la méningite figure dans les indications |
| 014 | traitement[2] | « vorasidénib (INDIGO 2023) : autorisation Swissmedic et dose AIPS À vérifier » → « vorasidénib (Voranigo®) 40 mg p.o. 1×/j si ≥ 40 kg, jusqu'à progression ; astrocytome ou oligodendrogliome de grade 2 IDH1/2 muté, opéré, sans radio- ni chimiothérapie immédiate (AIPS Voranigo®, Swissmedic 69364, mars 2026) » | Voranigo 69364 |
| 018 | traitement[3] | « dose pédiatrique selon le cas, À vérifier (AIPS Fortecortin® sans posologie pédiatrique fixe) » → « dexaméthasone i.v. chez l'enfant (tumeur cérébrale) : 0,5–1 mg/kg en dose initiale, puis 0,25–0,5 mg/kg/j en 4 prises (AIPS Fortecortin® Inject, Swissmedic 48669, juin 2022) » | Fortecortin 48669, Posologie enfants. Le texte actuel est **faux**. |
| 030 | traitement[0] | « (dose : À vérifier, AIPS Sabril) » → « vigabatrine en monothérapie des spasmes infantiles : 50 mg/kg/j, adaptable en une semaine, jusqu'à 150 mg/kg/j (AIPS Sabril®, Swissmedic 50043, avr. 2026) ; surveiller le champ visuel » | Sabril 50043 |
| 031 | traitement[0] | « (doses : À vérifier, AIPS non retrouvée) » → « sulfate de magnésium (neuroprotection fœtale avant 32 SA) : hors indication AIPS (AIPS Bichsel 56394 : tocolyse 4 g i.v. puis 1–2 g/h) ; bétaméthasone : AIPS absente du corpus, À vérifier (AIPS) » | Bichsel 56394. L'affirmation « AIPS non retrouvée » est fausse. |
| 033 | traitement[3] | « éculizumab, ravulizumab (À vérifier) » → « éculizumab (Soliris®, Swissmedic 59282) et ravulizumab (Ultomiris®, Swissmedic 67278) : autorisés dans la NMOSD AQP4+ de l'adulte (AIPS), posologie selon l'AIPS ; rituximab hors AIPS » | Soliris et Ultomiris : Indications NMOSD |
| 040 | traitement[1] | « dexaméthasone … (AIPS Dexaméthasone Galepharm, 2022 ; dose : À vérifier) » → « dexaméthasone 8–12 mg i.v. puis 4 mg i.v./i.m. toutes les 6 h, réduite par paliers à la plus faible dose efficace (AIPS Dexaméthasone Galepharm Amp, Swissmedic 66710, juin 2022 : œdème cérébral subaigu, radiolésions) » | Galepharm 66710 |

## 2. Défauts majeurs

| Id | Champ | Défaut → PATCH |
|---|---|---|
| 002 | traitement[0], [6], sources[0] | La source ESO 2014 est périmée. **Patch** : « ESO-EANS guideline on stroke due to spontaneous intracerebral haemorrhage, Eur Stroke J 2025;10(4):1007-86 (doi 10.1177/23969873251340815) ». Baisse tensionnelle aiguë : recommandation faible. Hématome cérébelleux : « > 3 cm » → « > 15 ml (ESO-EANS 2025, faible) ». Cible chiffrée : à relire dans le texte 2025. |
| 041 | traitement[3], sources[2] | « (ESO, À vérifier pour la version 2025) » et « 2025 : À vérifier » → même référence ESO-EANS 2025. Supprimer « À vérifier ». |
| 003 | traitement[0], [1], sources[0] | La source ESO 2013 est remplacée par **ESO/EANS/ESMINT 2026** (Vergouwen M et al., Eur Stroke J 2026;11(5), doi 10.1093/esj/aakag043). **Patch** : « Exclure l'anévrisme dans les 24 h si une équipe dédiée est disponible (consensus) ; embolisation plutôt que clip si les deux sont également possibles (recommandation fondée sur les preuves) ». Nimodipine : placer en premier la « voie orale 60 mg toutes les 4 h (6 × 60 mg/j) : recommandée par ESO 2026 (preuves élevées) ». La voie i.v. AIPS reste l'alternative (patient qui ne peut avaler). |
| 004 | images.normal | La coupe normale (fosse postérieure, axial_30) ne correspond pas au cliché pathologique, qui passe par le 3e ventricule et les noyaux gris. Le champ `patho.technique` « (fosse postérieure) » est faux. **Patch** : normal → `CT_of_a_normal_brain,_axial_20.png` ; technique patho → « TDM sans injection, coupe axiale (3e ventricule) ; flèche rouge d'origine ». |
| 005, 007, 014 | traitement (« antiépileptique : molécule et dose À vérifier ») | Ce texte contredit IMG-015 et IMG-016. **Patch** : « après une crise : p. ex. lévétiracétam 500 mg 2×/j, jusqu'à 1500 mg 2×/j (AIPS Keppra®, Swissmedic 55297, avr. 2023) ; pas de prophylaxie ». |
| 006 | images.normal | La coupe coronale normale passe par les orbites ; la coupe pathologique passe par les cornes frontales. **Patch** : choisir une coupe coronale FLAIR normale au niveau des cornes frontales ou des 3e et 4e ventricules (Commons, même série `Brain_MRI_FLAIR_Cor`). |
| 008 | traitement[1], [2] | « schéma 2 g toutes les 12 h : À vérifier » → « 4 g/j, dose maximale AIPS, en 2 × 2 g (ESCMID 2024) ». « (ESCMID 2024 : À vérifier) » : lire la recommandation et dater, ou retirer la durée. Flagyl 26313 est une AIPS orale : préciser « relais oral » ou citer une AIPS de métronidazole i.v. |
| 010 | reperes[0] | La pointe (20,55) tombe sur le néocortex temporal latéral, alors que la sémiologie décrit l'hippocampe. **Patch** : x 33, y 63, fx 4, fy 90. |
| 013 | reperes[2] | La pointe (50,40) tombe sur le septum et la corne frontale **gauche**, bien visible. La corne droite est la corne comprimée. **Patch** : x 43, y 36, fx 92, fy 8. |
| 014 | reperes[1].semio, gold.pourquoi[1] | Le cliché est un **oligodendrogliome**. Or le signe du mismatch T2-FLAIR caractérise l'astrocytome IDH muté **non codélété** : l'invoquer ici enseigne une erreur. **Patch semio** : « Une bordure hyperintense cerne une masse kystique à centre supprimé en FLAIR ; ce n'est pas un signe du mismatch, qui exige un astrocytome IDH muté non codélété et une comparaison avec le T2. » Repère 1 : « sans rehaussement attendu dans le bas grade » → « le rehaussement n'exclut pas un oligodendrogliome de grade 2 ». PCV/témozolomide « doses À vérifier » → « hors AIPS (Temodal® : glioblastome et gliome malin récidivant) ; doses selon protocole ». |
| 015 | images.normal | La paire n'est pas comparable : T1 axial sans injection contre T1 coronal injecté. **Patch** : coupe coronale T1 normale (série `MRI_Brain_T1_Cor` de Commons), sinon signaler explicitement « plan différent ». |
| 017 | sources[1] | « ESMO-EANO … 2023 (À vérifier : référence exacte) » → « Ferreri AJM et al. Primary CNS lymphomas: EHA–ESMO Clinical Practice Guideline. Ann Oncol 2024;35:491-507 ». Mettre à jour le traitement en conséquence (MATRix, consolidation). |
| 024, 025 | sources | Les sources sont exclusivement américaines (Brain Trauma Foundation, Bullock 2006). **Patch** : ajouter « NICE NG232 Head injury, 2023 » et « Undén J et al., Scandinavian guidelines, BMC Med 2013 » pour les indications d'imagerie. Garder BTF pour les seuils chirurgicaux en le signalant « (non vérifié CH/UE) ». |
| 024–027 | traitement (« pas de corticoïdes ») | L'écart avec l'AIPS n'est pas signalé : Mephameson®, Fortecortin® et Dexaméthasone Galepharm citent l'« œdème cérébral … traumatisme cranio-cérébral » (40–100 mg i.v.). **Patch** : ajouter « écart : l'AIPS indique la dexaméthasone dans l'œdème post-traumatique, mais CRASH 2004 montre une surmortalité ; ne doit pas être prescrite ». |
| 026 | traitement[3] | « hors AIPS, À vérifier » → « hors AIPS (Cyklokapron®, Swissmedic 33741 : pas d'indication en traumatisme crânien) ; schéma CRASH-3 : 1 g i.v. en 10 min puis 1 g en 8 h, dans les 3 h ». |
| 028 | images.normal | La fenêtre cérébrale ne se compare pas à la fenêtre osseuse du cliché pathologique. **Patch** : normal en fenêtre osseuse au niveau de la base (série `CT_of_a_normal_brain` en fenêtre os, ou autre image libre). |
| 032 | gold, autres R2/R3/R4, sources[0] | Les critères de McDonald 2017 sont périmés. **Patch** : « critères de McDonald 2024 (Montalban X et al., Lancet Neurol 2025;24:850-65) ». Gold : DIS ≥ 2 des **5** topographies (nerf optique ajouté), signe de la veine centrale et lésions à anneau paramagnétique comme marqueurs d'appui. R2 « ne démontre pas la dissémination » → « le nerf optique compte comme 5e topographie ». R3 : « bandes oligoclonales ou chaînes légères libres κ ». R4 « n'entrent pas dans les critères » → « PEV et OCT peuvent démontrer l'atteinte optique (McDonald 2024) ». |
| 034 | traitement[0], [1] | « (dose hors libellé spécifique, À vérifier) » → « hors AIPS (Solu-Medrol® : poussée de SEP 500–1000 mg/j pendant 3–5 j) ; schéma de consensus 1 g/j pendant 5 j ». Pour les Ig i.v., nommer le produit et préciser « hors AIPS ». |
| 038 | traitement, sources | ERC 2021 est périmé. **Patch** : « Nolan JP et al. ERC-ESICM guidelines 2025: post-resuscitation care (Resuscitation / Intensive Care Med 2025) ». Seuil de prévention de la fièvre (> 37,7 °C dans la version 2022) et PAM > 60–65 mmHg : à relire dans le texte 2025 avant publication. |

## 3. Défauts mineurs (patch court)

| Id | Défaut → PATCH |
|---|---|
| 001 | Endartériectomie « ≥ 70 % » → « 70–99 % (recommandée), à considérer 50–69 % (ESVS 2023) ». |
| 001 | Image : la sémiologie et les repères sont justes. |
| 002 | Ajouter un repère sur l'inondation ventriculaire seulement si elle est démontrée ; sinon rien. |
| 003 | Images et repères justes. |
| 005 | Le cliché montre seulement le cavernome. Ajouter « (la MAV n'est pas illustrée) » dans `technique`. |
| 006 | `reperes[0]` : « Fazekas élevé » → « Fazekas périventriculaire 2 (halo lisse) ». |
| 006 | `reperes[1]` : la dilatation est discrète. Atténuer en « ventricules à la limite supérieure ». |
| 007 | Normal (noyaux gris) et pathologique (mésencéphale) sont à des niveaux différents. |
| 007 | `reperes[1].semio` → « …oriente vers un œdème vasogénique (PRES) ; la diffusion normale l'oppose à un infarctus bilatéral de l'ACP ». |
| 008, 009, 013, 016, 017 | Le normal est en T1 **sans** injection face à un T1 injecté. C'est signalé : garder, mais écrire « contraste différent » dans le champ technique du normal. |
| 009 | La prise de contraste leptoméningée est subtile et se confond avec les veines corticales. Préférer un FLAIR injecté si une image libre existe. |
| 009 | Ajouter une source suisse (ssi.guidelines.ch, méningite). |
| 011 | Seule la toxoplasmose est illustrée, et en FLAIR, alors que le gold est un T1 injecté : le signaler. |
| 011 | Remplacer EANO 2015 par EHA-ESMO 2024. Vérifier la version EACS en vigueur (12.0 de 2023 ; version ultérieure non vérifiée). |
| 012 | Niveaux de coupe différents (noyaux gris contre centre ovale). |
| 016 | L'image fait 330 px. Les deux repères sont exacts (vérifié au zoom). |
| 018, 019 | Le normal passe par le mésencéphale et les orbites (adulte) ; le pathologique passe par le bulbe ou le méat acoustique. Choisir une coupe normale au niveau du 4e ventricule ou du méat. |
| 018 | Remplacer « Thomas A, Noël G 2019 (À vérifier) » par une recommandation SIOP-E ou EANO datée. |
| 020 | « p-tau181 » → « p-tau217 de préférence (Jack 2024) ». |
| 020 | Repères 1 et 2 redondants : #1 → « élargissement de la fissure choroïdienne et de la corne temporale ». |
| 021 | Date de l'AIPS Exelon® : « avril 2025 » → « janvier 2024 ». |
| 021 | Seule la démence à corps de Lewy est illustrée ; la DFT ne l'est pas. |
| 022, 035 | Aucune source européenne. Le signaler « (non vérifié CH/UE) ». |
| 023 | Paire, repères et dose de Madopar® conformes à l'AIPS (38096). |
| 025 | Le cliché est une photo d'écran, avec le curseur visible. Le remplacer si une TDM libre de meilleure qualité existe. |
| 026 | « frontal basal » → « frontal antérieur ». |
| 026 | Repère 2 : « autre zone d'impact » → « second foyer de contrecoup ». |
| 026 | Les lésions axonales diffuses ne sont pas illustrées : le signaler. |
| 027 | NaCl hypertonique : citer une AIPS de NaCl 10 % ou écrire « hors AIPS ». |
| 028 | Vaccination antipneumococcique : remplacer « À vérifier » par la recommandation OFSP/CFV (fistule de LCR = groupe à risque). La source reste à lire et à dater. |
| 029, 030 | Séquence (T1/T2) ou âge (adulte/nourrisson) différents entre normal et pathologique. Mention à ajouter. |
| 032 | Repère 2 : la lésion est en substance blanche profonde → « hypersignal T2 de la substance blanche frontale gauche ». |
| 032 | Repères 1 et 3 exacts (vérifié au zoom). |
| 036, 037, 039 | Paires et repères exacts. |
| 037 | Date de l'AIPS Minirin® injectable : « avril 2026 » → « février 2024 ». |
| 037 | Spasovski 2014 : force « devrait » → « doit (1D) ». |
| 039 | Ajouter un repère « hypersignal T2 hippocampique gauche ». |

## 4. Points vérifiés conformes

- **AIPS** : posologies conformes, mot pour mot pour l'essentiel :
  - Actilyse, Metalyse (dose, CI, 24 h sans héparine ni AAS, thrombectomie) ;
  - Nimotop i.v. et comprimés, Fragmin, Beriplex, Konakion (10–20 mg), Praxbind, Ondexxya (041) ;
  - Zovirax i.v. (10 mg/kg/8 h, 10 j), Daraprim, Temodal ;
  - Mephameson et Fortecortin chez l'adulte (8–12 mg puis 4 mg/6 h) ;
  - Keppra, Kisunla (350/700/1050 puis 1400 mg ; ApoE ε4 non homozygote), Donepezil-Mepha, Rivastigmin-Mepha, Memantin-Mepha, Madopar, Mannitol (1–2 g/kg en 30–60 min) ;
  - Votubia (4,5 mg/m², taux résiduel 3–15 ng/ml), Koselugo, Solu-Medrol, Uplizna, Enspryng ;
  - Benerva : l'écart avec EFNS est correctement signalé.
- **Dates « Mise à jour »** : exactes sauf Exelon et Minirin.
- **Gold et première intention** : le piège urgence est bien distingué. Formulations exactes pour 001, 003, 004, 008, 017, 026, 031, 035 et 036.
- **Ordre des autres examens** : cohérent sur les 41 entrées.

## 5. Verdict

**corrections requises** : il reste 11 défauts critiques (10 entités) et 19 lignes de défauts majeurs.

Sources consultées :
- [ESO/EANS/ESMINT aSAH 2026](https://www.medthority.com/guidelines/acute-cerebrovascular-disease/esoeansesmint-guideline-on-aneurysmal-subarachnoid-haemorrhage/)
- [ESO-EANS ICH 2025](https://www.medthority.com/guidelines/acute-cerebrovascular-disease/eso-and-eans-guideline-on-stroke-due-to-spontaneous-intracerebral-haemorrhage/)
- [McDonald 2024 (ECTRIMS)](https://ectrims.eu/press/revisions-to-mcdonald-diagnostic-criteria-for-multiple-sclerosis-published/)
- [ERC-ESICM 2025](https://pubmed.ncbi.nlm.nih.gov/41123621/)
- [EHA-ESMO PCNSL 2024](https://esmo.org/guidelines/guidelines-by-topic/esmo-clinical-practice-guidelines-haematological-malignancies/primary-central-nervous-system-lymphomas)
- Corpus AIPS refdata (AipsDownload_20261008), fiches lues le 14.11.2026.
