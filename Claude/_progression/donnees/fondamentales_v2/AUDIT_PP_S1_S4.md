# Audit médical agressif — PP-S1 à PP-S4 (36 fiches, 143 affections)

Auditeur indépendant (non rédacteur), 14.11.2026. Posture : skills `medecin-expert` et `expert-web`.
Méthode : lecture intégrale des 36 JSON par script (S1 : 37 affections, S2 : 40, S3 : 34, S4 : 32) ; résolution des 253 renvois SY, S, EX, IMG, PH, SF contre `donnees/` et `recensement/` (fiches PP exclues) ; confrontation de chaque IMG à son `diagnostic` dans `recensement/recensement.json` ; recherche des IMG des régions TC, TH et RA qu'aucune fiche PP ne cite ; recherche de doses ; présence des molécules citées dans `Claude/_harnais/donnees/aips_corpus_index.json`. Une recherche web (dépistage néonatal CF). Aucun fichier modifié hors ce rapport ; ni commit ni push.

## 1. Contrôles mécaniques

| Contrôle | Résultat |
|---|---|
| Renvois | 252/253 résolus. Le seul échec est le texte provisoire `"LOT correspondant (à résoudre par le titre du cours)"`, présent dans les 36 fiches. |
| Pertinence IMG | Quatre écarts : IMG-063 (abcès rétro- et parapharyngé) pour l'abcès péri-amygdalien (PP-S2-I) ; IMG-151 (CIA, CIV, coarctation) pour Fallot (PP-S3-C) ; IMG-084 (myélopathie cervicarthrosique) pour la SLA (PP-S1-D) ; EX `panels-neurogenetique-expansions-nucleotidiques` pour la NF1 (PP-S1-C), qui n'est pas une maladie à expansion. |
| Schéma | Les fiches S1 à S4 utilisent `titre`, `cibles_therapeutiques`, `examens`, des `sources` en chaînes et un `examen_cle` objet. Les fiches S5 à S12 utilisent `nom`, `cible_therapeutique`, `renvois_examen`, des `sources` en objets {ref, origine, statut}, plus `doses` et `cadrage_recensement`. Le module contient donc deux schémas. |
| Doses chiffrées | Aucune. Restent les qualificatifs « forte dose » (S1-A, S2-V), « dose minimale efficace » (S2-Ia) et « faible dose » (S4-T). |
| Molécules absentes du corpus AIPS local | La cyproheptadine (S1-Ia) et le dexrazoxane (S3-Ia) n'y figurent pas. Les autres molécules y figurent : Ondexxya, Praxbind, Tepezza, Camzyos, Koselugo, Beyfortus, Xenazine, Nimotop, Parlodel, Dantamacrin, Xifaxan, Rilutek, Ofev, Esbriet, Betaserc, Diamox, Mestinon. |

## 2. Exactitude physiopathologique

| # | Gravité | Emplacement | Extrait fautif | PATCH exact |
|---|---|---|---|---|
| E1 | Grave | PP-S2-I, `affections[3].mecanisme[2]` | « Par mimétisme moléculaire, le streptocoque peut ensuite provoquer un rhumatisme articulaire aigu ou une glomérulonéphrite. » | « Par mimétisme moléculaire, le streptocoque peut provoquer un rhumatisme articulaire aigu ; par dépôt de complexes immuns, il peut provoquer une glomérulonéphrite post-streptococcique, que la pénicilline ne prévient pas. » |
| E2 | Moyen | PP-S1-A, `affections[2].mecanisme[0]` | « anti-récepteur de l'acétylcholine (ou anti-MuSK) bloquent et détruisent les récepteurs […] par le complément » | « Les anticorps anti-récepteur de l'acétylcholine (IgG1-3) bloquent les récepteurs et les détruisent par le complément ; les anti-MuSK (IgG4) empêchent leur regroupement sans activer le complément. » |
| E3 | Moyen | PP-S3-V, `affections[4].mecanisme[1]` | « des zones ventilées ne sont plus perfusées, et l'hypoxémie s'installe » | « des zones ventilées ne sont plus perfusées (espace mort) ; le débit dévié surperfuse les zones restantes, ce qui crée l'hypoxémie (effet shunt). » Cette formulation reprend celle, juste, de PP-S4-V `affections[0].mecanisme[1]`. |
| E4 | Moyen | PP-S3-V, `affections[4].examen_revelateur` contre `mnemotechnique` | « Si la probabilité clinique reste faible » contre « faible ou intermédiaire » | Remplacer dans `examen_revelateur` : « Si la probabilité clinique n'est pas élevée (Wells), des D-dimères normaux excluent la maladie ». |
| E5 | Moyen | PP-S4-Tr, `affections[0]` | Le pneumothorax spontané primaire est classé « Traumatique ». | Scinder l'affection : « pneumothorax spontané (rupture de bulles) » va dans PP-S4-D ou PP-S4-F ; PP-S4-Tr garde le pneumothorax traumatique et le pneumothorax compressif. |
| E6 | Léger | PP-S1-Ia, `affections[1].mnemotechnique` | « Le syndrome malin est lent, rigide et aréflexique » | « Le syndrome malin est lent, rigide, avec des réflexes normaux ou diminués ; le sérotoninergique est rapide, clonique et hyperréflexique. » |
| E7 | Léger | PP-S2-F, `affections[0].consequence_clinique` | « la pupille reste en mydriase aréactive » | « la pupille reste en semi-mydriase aréactive » |
| E8 | Léger | PP-S1-D, `affections[1].mecanisme[1]` | « la voie indirecte s'emballe et freine le mouvement » | « la voie directe (D1) faiblit et la voie indirecte (D2) se désinhibe ; le pallidum interne freine alors davantage le thalamus moteur. » |
| E9 | Léger | PP-S3-F, `affections[2].mecanisme[0]` | « le ventricule peu rempli se contracte fort et stimule des afférences vagales » | Ajouter : « (réflexe de Bezold-Jarisch, hypothèse discutée) ». |
| E10 | Léger | PP-S1-F, `affections[0].cibles_therapeutiques[1]` | « anticorps anti-CGRP et gépants […] préviennent les crises » | « Ils bloquent le CGRP ou son récepteur ; les anticorps préviennent les crises, et certains gépants traitent aussi la crise (statut AIPS à vérifier). » |
| E11 | Léger | PP-S1-A, `affections[2].examens` | `EX-2-S4-angio-tdm-thoracique` pour chercher un thymome | Remplacer par l'EX de TDM thoracique injectée (non angiographique), ou ajouter une note. |

## 3. Affections importantes manquantes

Preuve objective : le recensement du dépôt contient des IMG qu'aucune fiche PP ne cite (IMG-005, 007, 017, 018, 033, 050, 052, 056, 057, 059, 065, 077, 098, 104, 107, 108, 116, 119, 123, 124, 128, 130, 131, 132, 133, 139, 141, 142, 150, 155, 159).

| # | Gravité | Fiche | Manque | PATCH |
|---|---|---|---|---|
| M1 | Grave | PP-S3-V, PP-S3-D | Le syndrome coronarien chronique (angor stable, IMG-142) manque ; l'insuffisance mitrale manque aussi (IMG-148 la cite). | Ajouter « syndrome coronarien chronique » : sténose fixe, la demande dépasse l'apport à l'effort ; ECG d'effort, scanner coronaire, imagerie de stress ; cibles : bêtabloquants, nitrés, antiagrégants, statines. Ajouter « insuffisance mitrale » (prolapsus, dilatation annulaire, surcharge de volume). |
| M2 | Grave | PP-S3-F, PP-S3-D | Les troubles de conduction et les autres arythmies manquent : BAV, dysfonction sinusale, tachycardie par réentrée nodale, WPW, TV et FV, Brugada. | Ajouter « troubles de conduction » (fibrose de Lenègre, BAV ; cible : stimulateur) et « tachycardies par réentrée » (circuit nodal ou voie accessoire ; cible : adénosine, ablation). Ajouter Brugada (SCN5A) dans PP-S3-C. |
| M3 | Grave | PP-S4-F ou PP-S4-V | Le SDRA (IMG-123) et l'épanchement pleural (IMG-132, critères de Light) manquent alors que l'empyème (IMG-133) existe. | Ajouter « SDRA » : lésion de la membrane alvéolo-capillaire, œdème lésionnel, shunt ; cible : ventilation protectrice, décubitus ventral. Ajouter « épanchement pleural » : transsudat (Starling) ou exsudat (perméabilité) ; ponction et critères de Light. |
| M4 | Grave | PP-S2-D, PP-S2-V | Le décollement de rétine (IMG-052), la rétinopathie diabétique et la rétinopathie hypertensive manquent, alors qu'elles sont fréquentes à l'examen. | Ajouter « décollement de rétine rhegmatogène » : déchirure, passage du vitré, myodésopsies, éclairs, voile ; urgence chirurgicale. Ajouter « rétinopathie diabétique » : microangiopathie, ischémie, VEGF ; cible : anti-VEGF, laser. |
| M5 | Grave | PP-S1-V | La dissection des artères cervicales (IMG-077) manque, alors qu'elle est la première cause d'AVC du sujet jeune et provoque un syndrome de Horner (SY-11). | Ajouter « dissection carotidienne ou vertébrale » : hématome de paroi, sténose ou embolie ; cervicalgie, Horner, AVC ; angio-IRM avec T1 fat-sat. |
| M6 | Moyen | PP-S1-A, -I, -T, -Tr, -F | NMOSD et MOGAD (IMG-033), névrite optique (IMG-050), méningo-encéphalite à tiques (FSME, endémique en Suisse), lymphome cérébral primitif (IMG-017), compression médullaire et queue de cheval (IMG-104), commotion cérébrale ; dans PP-S1-F : trouble neurologique fonctionnel, polyneuropathie diabétique, sclérose combinée de la moelle par carence en B12. | Ajouter une affection par manque, au format existant. Pour la FSME, renvoyer au plan de vaccination de l'OFSP. |
| M7 | Moyen | PP-S2-F, -I, -D, -Tr, -Ia | Névrite vestibulaire (diagnostic différentiel de l'AVC, test HINTS), surdité brusque, cholestéatome (IMG-056), otospongiose (IMG-057), angine de Ludwig (IMG-065), sialolithiase (IMG-073), brûlure chimique de l'œil, fracture du rocher (IMG-059), ostéonécrose des mâchoires (IMG-061, citée en S9-Ia : renvoi), angio-œdème des IEC (S12-Ia : renvoi). | Idem. Pour la brûlure chimique : « Rinçage immédiat et prolongé avant tout examen. » |
| M8 | Moyen | PP-S3-C, -A, -F, -Ia | Transposition des gros vaisseaux (cyanose néonatale, PGE1) ; Takayasu (IMG-158 le cite) ; Raynaud ; intoxication digitalique. | Idem. |
| M9 | Moyen | PP-S4-C, -I, -Tr, -D | Détresse respiratoire du prématuré par déficit en surfactant (IMG-130) ; hernie diaphragmatique (IMG-141) ; abcès pulmonaire (IMG-108) ; pneumocystose (IMG-107) ; corps étranger bronchique de l'enfant (IMG-131) ; pneumoconioses (IMG-116, SUVA). | Idem. |

## 4. Sources et honnêteté

| # | Gravité | Emplacement | Défaut | PATCH exact |
|---|---|---|---|---|
| S1 | Grave | PP-S1-Tr, `sources[3]` | La Brain Trauma Foundation est américaine, mais la fiche l'étiquette « source européenne ». | `"(source américaine, hors hiérarchie : Brain Trauma Foundation, 4e éd., 2016 — non lue)"` ; ajouter `"(source européenne : recommandations de l'EAN ou de l'ESICM sur le TCC — non lues, À vérifier)"`. |
| S2 | Grave | 9 fiches PP-S1, `sources[0]` | « Fiches Sémiologie SY-1 à SY-31 et Status S-25 à S-30, audit-ok (lu le 14.11.2026) » : une fiche interne y sert de source, la lecture est héritée, et la plage est fausse, car les fiches renvoient aussi à SY-37 à SY-80 et à S-01 à S-33. | `"Fiches internes SY et S citées en renvoi (dépôt, non opposables ; lues par leurs rédacteurs, non relues ici)"`. |
| S3 | Moyen | PP-S3-Tr, PP-S4-Tr | ATLS (American College of Surgeons) est étiqueté « source internationale ». | `"(source américaine, hors hiérarchie : ATLS, 10e éd., 2018 — non lu)"`. |
| S4 | Moyen | 9 fiches PP-S2, `sources[1]` | Les recommandations EGS sur le glaucome sont copiées sur les 9 fiches, y compris sur les tumeurs, les traumatismes et la thyroïde. | Ne garder la source qu'en S2-D et S2-F. Ailleurs, citer une source pertinente « non lue », par exemple l'European Thyroid Association pour la thyroïde (déjà présente en S2-T) ou l'EULAR pour l'ACG. |
| S5 | Moyen | 36 fiches | La fiche ne lit aucune source et ne donne aucun lien ; les 36 fiches citent les sociétés suisses de façon générique (« recommandations non lues »). | Pour chaque système, lire et dater au moins une source suisse avec son URL : Swiss Stroke Society, SSC et ESC, SGP et SSP, SSI. Passer le statut à « lu le JJ.MM.AAAA » seulement après lecture. |
| S6 | Léger | PP-S4-C, `affections[0].examen_revelateur` | « Le dépistage néonatal oriente (À vérifier en Suisse) » | « Le dépistage néonatal suisse (IRT puis ADN sur carte de Guthrie, depuis janvier 2011) oriente ». Source : Rueegg et al., Paediatrica 2013 (boris.unibe.ch/40843). |
| S7 | Léger | PP-S4-A (GINA), PP-S4-D (GOLD), PP-S1-F (ICHD-3) | L'étiquette « internationale » sort de la hiérarchie Suisse → Europe → OMS. | `"(international, non européen : … — non lu)"` ; chercher d'abord la SSP ou l'ERS. |
| S8 | Léger | PP-S1-Ia (cyproheptadine), PP-S3-Ia (dexrazoxane) | Ces molécules sont absentes du corpus AIPS local. | Ajouter « (enregistrement suisse non trouvé dans le corpus AIPS local, À vérifier) ». |
| S9 | Léger | PP-S4-T, `affections[0].examen_revelateur` | « la TDM à faible dose sert au dépistage » | « la TDM à faible dose permet le dépistage (programme suisse et remboursement à vérifier) ». |

## 5. Renvois, redondance, style

| # | Gravité | Emplacement | Défaut | PATCH |
|---|---|---|---|---|
| R1 | Moyen | Module | Deux schémas coexistent (voir § 1). | Aligner S1 à S4 sur le schéma de S5 à S12 (`nom`, `cible_therapeutique`, `renvois_examen`, sources en objets, `doses`), ou l'inverse, avant toute intégration au front-end. |
| R2 | Moyen | Doublons | Hémorragie sous anticoagulant (S1-Ia, S3-Ia, S10-Ia) ; ACG (S2-V, S3-A) ; EP (S3-V, S4-V), avec un mécanisme contradictoire (E3) ; Hashimoto (S2-A, S8-A) ; cancer thyroïdien (S2-T, S8-T) ; anti-NMDA, syndrome malin et syndrome sérotoninergique (S1, S11) ; zona (S1-I, S12-I) ; NF (S1-C, S12-C). | Garder la forme complète une seule fois : S10-Ia, S3-A, S4-V, S8-A, S8-T, S1. Ailleurs, garder une phrase et ajouter `{"vers":"Physiopathologie","id":"PP-…"}`. |
| R3 | Moyen | 36 fiches, `passerelles` | Les passerelles PHY ne sont pas spécifiques ; le cours n'est pas résolu. | Résoudre l'id du LOT ; ajouter les passerelles croisées PP ↔ PP. |
| R4 | Léger | S1-A, S2-V, S2-Ia | « forte dose », « dose minimale efficace » | Écrire « corticoïdes (bolus, selon AIPS) » ; « la plus courte exposition possible ». |
| R5 | Léger | Cascades S1 à S4 | Les maillons commencent par « Normal : », « Altération : » ; la plupart restent verbaux. Le style est conforme. | Aucun. |

## 6. Points vérifiés exacts (échantillon)

Les points suivants sont exacts : pénombre et œdème cytotoxique ; PPC = PAM − PIC ; hématome extradural (biconvexe, limité par les sutures) ; voie indirecte dans Huntington ; thiamine avant le glucose ; ammoniac et glutamine astrocytaire ; LQT1, LQT2, LQT3 et leurs déclencheurs ; Fallot et accroupissement ; CMH et Valsalva ; CHA2DS2-VA (ESC 2024) ; loi de Laplace et AAA ; isthme aortique et ligament artériel ; OACR et tache rouge cerise ; plancher orbitaire et réflexe oculo-cardiaque ; HPV, E6/E7, p53 et Rb ; RB1 et l'éviction de la TDM ; AAT aux bases ; FPI et la nocivité des corticoïdes ; espace mort et shunt (S4-V) ; oxygène et azote dans le pneumothorax.

## 7. Verdict

| Critère | Note (2/1/0) | Raison |
|---|---|---|
| Exactitude des chaînes | 1 | Une erreur de mécanisme classique (E1, GNPS) ; quatre imprécisions (E2 à E5). |
| Exhaustivité des affections | 0 | Angor stable, troubles de conduction, SDRA, épanchement pleural, décollement de rétine, rétinopathie diabétique et dissection cervicale manquent ; 31 IMG du recensement restent sans affection. |
| Classement VITE DIT CAFé | 1 | Le pneumothorax spontané est classé « Traumatique » ; l'insuffisance cardiaque est classée « Dégénératif » sans réserve. |
| Sources et honnêteté | 0 | La fiche ne lit aucune source et ne donne aucun lien ; une source américaine porte l'étiquette « européenne » ; la lecture des fiches internes est héritée. |
| Renvois et passerelles | 1 | 252/253 renvois sont résolus, mais 4 IMG ou EX ne correspondent pas, des doublons subsistent et deux schémas coexistent. |
| Aucune dose, style | 2 | Aucune dose chiffrée ; les phrases sont verbales ; il reste quelques qualificatifs posologiques. |

**Prêt pour `audit-ok` : non.** Il manque les corrections E1 à E5, M1 à M5, S1, S2 et R1. Les défauts Moyen restants (M6 à M9, S3 à S5, R2 et R3) peuvent suivre dans une seconde passe ; les défauts Léger peuvent suivre en dernier.

Source web consultée : [Rueegg et al., Paediatrica 2013](https://boris.unibe.ch/40843/1/Rueegg%20Paediatrica%202013_fre.pdf) ; [Barben et al., SwissMedForum 2023](https://boris.unibe.ch/178617/2/Barben_SwissMedForum_2023_fr.pdf).
