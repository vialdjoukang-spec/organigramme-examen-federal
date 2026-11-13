# CAHIER D'ARCHITECTURE · Plateforme de révision clinique suisse

> Version 2 · 13.11.2026 · décisions de la partie 12 validées.
> Document de travail pour Claude Code : construire d'abord **toute la charpente** (emplacements vides), ensuite seulement le contenu.

---

## 0. Règles non négociables

1. **Charpente avant contenu.** Chaque emplacement existe, vide (« — »), avant toute rédaction.
2. **Un seul gabarit par type de fiche**, identique partout.
3. **Neurologie et psychiatrie sont deux systèmes séparés** (S1 et S11) : stations, classes, fiches, examens distincts. Une molécule commune (ex. valproate) a une fiche dans chacun, avec son « pourquoi elle » propre.
4. **Psychiatrie : CIM-10 exclusivement**, chapitre V (F00–F99).
5. **Sources suisses** : information professionnelle Swissmedic (corpus AIPS du harnais) d'abord, puis sociétés et hôpitaux universitaires suisses, puis européennes en le signalant. « Selon X » seulement si la page de X a été lue ; sinon « (non vérifié CH) ».
6. **Forme** : texte en **Atkinson Hyperlegible** uniquement (titres libres), ≈ 15 px ; colonne de lecture ≤ 760 px ; rail vertical + sommaire latéral numéroté ; une seule fenêtre ouverte ; contraste ≥ 7:1 ; couleur à sens fixe (bleu normal, rouge pathologie, vert traitement du système, violet hors système, ocre non médicamenteux, orange danger).

---

## 1. Huit niveaux, de la coque vers le centre

| Niveau | Contenu |
|---|---|
| 1 Plateforme | Révision clinique suisse |
| 2 Module | Pharmacologie · Examens paracliniques · Sciences fondamentales |
| 3 Système | S1–S12 + Transversaux, communs aux trois modules |
| 4 Sous-onglet / chapitre | Examens : 9 sous-onglets. Pharmacologie : chapitres. |
| 5 Fiche | un examen, une lignée, une pathologie ou une molécule |
| 6 Temps | blocs fixes du gabarit |
| 7 Ligne | une indication, une norme, un tableau clinique |
| 8 Champ | la plus petite case à remplir |

---

## 2. Référentiel des systèmes (figé)

| Code | Système | Contenu |
|---|---|---|
| S1 | **Neurologie** | SNC, nerfs, muscles, épilepsie, mouvements anormaux, démences (versant neurologique : G30–G31), SEP, AVC, céphalées |
| S2 | Tête, cou, ORL, CMF et ophtalmologie | oreille, nez, gorge, sinus, face, glandes salivaires, œil |
| S3 | Cardiovasculaire | cœur, vaisseaux, circulation pulmonaire, lipides |
| S4 | Respiratoire et thorax | voies aériennes, poumon, plèvre, médiastin |
| S5 | Digestif et hépato-bilio-pancréatique | tube digestif, foie, voies biliaires, pancréas |
| S6 | Néphro-urologique | rein, eau et électrolytes, voies urinaires, prostate |
| S7 | Reproduction, gynéco-obstétrique et sénologie | fertilité, grossesse, utérus, ovaires, sein |
| S8 | Endocrino-métabolique et nutrition | axes hormonaux, diabète, os minéral, vitamines |
| S9 | Appareil locomoteur | os, articulations, muscles, rachis |
| S10 | Sang et immunité | lignées, hémostase, immunité, lymphomes |
| S11 | **Psychiatrie et sommeil** | CIM-10 F00–F99, sommeil (F51 et G47), addictions, cadre légal suisse |
| S12 | Peau et phanères | dermatologie, ongles, cheveux |
| T | Transversaux | pédiatrie, sujet âgé, oncologie, urgences et toxicologie, infectiologie (pharmacologie) |

**Interfaces S1 ↔ S11 (passerelles, jamais fusion)** :
- Démences : pathologie et pharmacologie spécifique (inhibiteurs de l'acétylcholinestérase, mémantine) en **S1** ; troubles psychiques et comportementaux de la démence et delirium (F05) en **S11**.
- Sommeil organique (G47 : apnées, narcolepsie, syndrome des jambes sans repos) rangé en **S11** par décision, code G conservé, étiquette S1 / S4.
- Antiépileptiques thymorégulateurs : une fiche S1 (épilepsie), une fiche S11 (trouble bipolaire).

---

## 3. Module Pharmacologie : gabarit général

Chaîne obligatoire : **Normal → Altération (VITDITCAF) → Pathologie → Traitement complet → Classe → Molécule.**

- **Normal** : le trajet de ce qui circule dans le système ; chaque structure traversée = une station numérotée (structure-fonction locale + « si elle se dérègle »).
- **Altérations** : grille **« VITE DIT : CAFé »** (V Vasculaire · I Infectieux · T Tumoral · D Dégénératif · I Iatrogène · T Traumatique · C Congénital · A Auto-immun · F Fonctionnel), 9 lignes par station, « — » si vide, jamais forcée.
- **Traitement** : flèche de la pathologie vers une barre verticale de bandes : médicament du système = *classe biochimique (classe fonctionnelle) : DCI (marque®)* cliquable ; hors système = survol avec posologie complète ; non médicamenteux = survol avec procédure, indications, contre-indications.
- **Fenêtre de classe** : classification fonctionnelle, mnémotechnique, une bande par sous-classe avec **« Quand la choisir »**, chefs de file suisses cliquables.
- **Fiche molécule** : pourquoi elle · indications · (spectre) · PK A-D-M-E + courbe commentée | PD · posologie (adulte, âgé, enfant, sexe, IR par DFG, IH par Child-Pugh, grossesse, allaitement) · pièges « si → alors » · source.

Systèmes atypiques : adapter la coque, garder la chaîne, justifier en une ligne (infectiologie : germe × site × terrain ; endocrinologie : axes ; sang : lignées et cascade). **La psychiatrie a son gabarit propre (partie 4).**

---

## 4. Psychiatrie et sommeil (S11) : gabarit propre

### 4.1 Coque : la CIM-10, chapitre V

La coque n'est pas un trajet de substance : c'est la **classification CIM-10**, de F0 à F9 (**dix blocs**, et non F1–F9 : le bloc F0 existe).

| Bloc | Intitulé CIM-10 |
|---|---|
| F00–F09 | Troubles mentaux organiques, y compris symptomatiques |
| F10–F19 | Troubles mentaux et du comportement liés à l'utilisation de substances psychoactives |
| F20–F29 | Schizophrénie, trouble schizotypique et troubles délirants |
| F30–F39 | Troubles de l'humeur (affectifs) |
| F40–F48 | Troubles névrotiques, troubles liés à des facteurs de stress et troubles somatoformes |
| F50–F59 | Syndromes comportementaux associés à des perturbations physiologiques et à des facteurs physiques (dont F51 sommeil non organique) |
| F60–F69 | Troubles de la personnalité et du comportement chez l'adulte |
| F70–F79 | Retard mental |
| F80–F89 | Troubles du développement psychologique |
| F90–F98 | Troubles du comportement et troubles émotionnels apparaissant habituellement durant l'enfance et l'adolescence |
| F99 | Trouble mental, sans précision |
| + Sommeil | F51 (non organique) et G47 (organique) réunis dans un chapitre « Sommeil » |
| + Cadre suisse | Capacité de discernement, placement à des fins d'assistance, traitement sans consentement, directives anticipées |

Source des critères : **CIM-10, chapitre V, descriptions cliniques et directives pour le diagnostic (OMS)**. Si un chiffre (durée, nombre de symptômes) n'y figure pas, compléter par les **critères diagnostiques pour la recherche de la CIM-10**, en le signalant. Jamais une autre classification.

### 4.2 Deux vues sur les mêmes pathologies

- **Vue CIM-10** : F0 → F9, une bande par bloc, pathologies dans l'ordre des codes.
- **Vue par âge** : 4 onglets **Enfant · Adolescent · Adulte · Sujet âgé**. Une pathologie figure sous chaque âge où elle se présente, avec une ligne sur ce que l'âge change (présentation, diagnostic différentiel, traitement).

Une pathologie = un identifiant unique ; les deux vues pointent sur la même fiche.

### 4.3 Ligne de pathologie

```
[F32.2 Épisode dépressif sévère sans symptômes psychotiques]  ➜  | Psychothérapie (survol)        |
   survol : critères CIM-10 condensés                            | Antidépresseurs (ISRS) : …     |  ← clic
                                                                 | Mesures (survol)               |
```

**Survol « critères CIM-10 »** :
- **tous** les critères présents, aucun omis ;
- **jamais mot pour mot** : une phrase très courte par critère ;
- **termes discriminants en gras** (ceux qui séparent du diagnostic voisin) ;
- structure fixe : critères principaux · critères associés · nombre requis · durée · spécifications (sévérité, syndrome somatique, symptômes psychotiques) · exclusions ;
- code CIM-10 en tête.

**Barre de traitement**, à droite de la pathologie :
- psychothérapies et mesures (survol : type, indication, durée) ;
- pharmacologie psychiatrique (clic → fenêtre de classe) ;
- hors psychiatrie (survol : posologie complète) ;
- mesures légales ou sociales si pertinentes (survol).

### 4.4 Classes psychiatriques

| Classe fonctionnelle | Sous-classes à prévoir |
|---|---|
| Antidépresseurs | ISRS · IRSNa · tricycliques · IMAO · antagonistes α2 (mirtazapine) · bupropion · agomélatine · trazodone · vortioxétine · eskétamine |
| Antipsychotiques | 1re génération · 2e génération · formes retard injectables · clozapine (classe à part : résistance) |
| Thymorégulateurs | lithium · valproate · lamotrigine · carbamazépine · antipsychotiques à action thymique |
| Anxiolytiques | benzodiazépines · prégabaline · hydroxyzine · ISRS en fond |
| Hypnotiques et chronobiotiques | apparentés aux benzodiazépines (« Z ») · mélatonine · antagonistes de l'orexine · antidépresseurs sédatifs |
| Psychostimulants et TDAH | méthylphénidate · amphétamines · atomoxétine · guanfacine |
| Addictions | agonistes opioïdes (méthadone, buprénorphine) · naltrexone · acamprosate · disulfirame · nalméfène · varénicline · substituts nicotiniques |
| Troubles du sommeil organiques | traitements de l'apnée (renvoi S4), de la narcolepsie, du syndrome des jambes sans repos |

**Particularité psychiatrique obligatoire : la matrice « profil clinique → chef de file »** dans chaque fenêtre de classe. Plusieurs chefs de file coexistent ; chacun est meilleur pour un profil donné.

| Profil clinique dominant | Chef de file préféré | Pourquoi (mécanisme, effet recherché) | À éviter et pourquoi |
|---|---|---|---|

Profils à prévoir au minimum :
- **Dépression** : avec syndrome somatique (mélancolique) · anxieuse · avec insomnie · avec ralentissement ou hypersomnie · avec douleurs · avec symptômes psychotiques · du sujet âgé · de la grossesse et du post-partum · avec comorbidité cardiaque · résistante.
- **Psychose** : premier épisode · symptômes négatifs prédominants · agitation aiguë · résistance · risque métabolique · QT long · hyperprolactinémie · sujet âgé et démence · Parkinson · mauvaise observance.
- **Trouble bipolaire** : manie aiguë · dépression bipolaire · prévention · cycles rapides · grossesse · insuffisance rénale.
- **Anxiété et sommeil** : aigu vs chronique · sujet âgé · antécédent d'addiction.
- **Addictions** : par substance, sevrage vs maintien.

### 4.5 Fiche molécule psychiatrique (gabarit général + 6 ajouts)

1. **Profil réceptoriel** (dans la PD) : affinités 5-HT, NA, DA, H1, muscariniques, α1 ; chaque effet indésirable relié à son récepteur.
2. **Délai d'action et titration.**
3. **Performance par profil clinique** (renvoi à la matrice 4.4).
4. **Arrêt, sevrage et changement** (« switch ») : schéma et syndrome d'arrêt.
5. **Surveillance** : biologie, ECG (QT), poids et métabolique, taux plasmatique ; renvois vers les fiches d'examens S11.
6. **Posologie par âge** : enfant · adolescent · adulte · sujet âgé (autorisation suisse par âge précisée), en plus de IR, IH, grossesse, allaitement.

### 4.6 Explorations psychiatriques (module Examens, S11)

Minutieuses, toujours reliées à une décision : bilan initial du premier épisode, bilan du delirium, surveillance de chaque psychotrope, imagerie quand elle change la conduite, exploration du sommeil, psychométrie par trouble, pharmacogénétique, capacité de discernement. Liste complète en partie 7.

---

## 5. Module Examens paracliniques : 9 sous-onglets

| N° | Sous-onglet | Entrée primaire | Axe secondaire | Unité de fiche |
|---|---|---|---|---|
| 1 | Biologie médicale | Matrice (sang et buvard, moelle, urines, LCR, selles, sérosités et synovial, respiratoire et ORL, génital et fœto-maternel, salive-sueur-calculs-peau) ; bascule « par système » | Discipline : cytologie et hématologie, hémostase, biochimie, immuno-hormonologie, microbiologie, pharmaco-toxicologie | un examen ou une lignée |
| 2 | Imagerie médicale | Système | Radiographie, échographie-Doppler, TDM, IRM, médecine nucléaire, radiologie interventionnelle | une modalité sur une région |
| 3 | Explorations fonctionnelles | Système | Repos, effort, provocation, nycthémère-sommeil | une exploration |
| 4 | Anatomie et cytologie pathologiques | Système | Biopsie, pièce opératoire, cytoponction, cytologie × technique | un prélèvement d'un organe |
| 5 | Endoscopies diagnostiques | Système ou voie | Technique, prélèvements associés | une endoscopie |
| 6 | Allergologie clinique (in vivo) | Mécanisme : immédiat IgE-médié, retardé | Médicaments, aliments, venins, produits de contraste, pneumallergènes | un type de test |
| 7 | Génétique médicale et génomique | Statut : constitutionnel postnatal, prénatal, somatique tumoral | Caryotype, FISH, ACPA, MLPA, NGS, PCR | une indication génétique |
| 8 | Tests rapides au point de soin | Système | Immunochromatographie, lecteur capillaire, moléculaire rapide | un test et sa confirmation |
| 9 | Évaluations cognitives et psychométriques | Système (S1 cognitif, S11 psychiatrique) | Hétéro- ou auto-évaluation | un instrument ou une famille d'échelles |

### 5.1 Gabarit de fiche d'examen

| Bloc | Colonnes |
|---|---|
| En-tête | nom exact et synonymes · systèmes (principal + étiquettes) · prélèvement ou conditions · bon usage suisse (Liste des analyses, Smarter Medicine, dose d'irradiation OFSP) |
| Temps 1 · Indications | urgence-aigu · diagnostic-étiologie · dépistage-pré-thérapeutique · suivi-surveillance · **ne pas demander** |
| Temps 2 · L'examen | paramètre · normal (unité, laboratoire suisse) · anomalie élémentaire (sens, seuil) · seuil d'alerte — **un paramètre lu seul** |
| Temps 3 · Interprétation | 1 entité anormale chiffrée · 2 anomalies associées (présentes · à rechercher) · 3 syndrome clinique (anamnèse · status) · 4 conclusion (confirmation · diagnostic · conduite) — **plusieurs anomalies associées** |
| Annexe A · Pièges | si… → conséquence pour le patient ; mnémotechnique dès 3 entités |
| Annexe B · Passerelles | type · fiche cible · pourquoi |

Adaptation du temps 2 :

| Sous-onglet | « Paramètre » | « Normal » | « Anomalie » |
|---|---|---|---|
| 1 Biologie | paramètre mesuré | référence et unité | écart et seuil |
| 2 Imagerie | structure examinée | aspect normal | signe élémentaire |
| 3 Explorations | mesure | valeur normale (âge, sexe) | profil anormal |
| 4 Anapath | **« Examen : diagnostic ou indication ; anomalies recherchées »** (règle absolue) | architecture normale | lésion élémentaire |
| 5 Endoscopie | segment | muqueuse normale | lésion, score |
| 6 Allergologie | test et allergène | négatif valide | seuil de positivité |
| 7 Génétique | gène ou région | séquence de référence | variant et sa classe |
| 8 Tests rapides | cible | négatif valide | positif → confirmation obligatoire |
| 9 Psychométrie | score ou sous-score | zone normale | seuils de sévérité |

### 5.2 Passerelles obligatoires

| Type | De → Vers |
|---|---|
| Prélèvement | 2 Imagerie (geste guidé), 5 Endoscopie → 1 Biologie, 4 Anapath |
| Test compagnon | 4 Anapath tumorale → 7 Génétique somatique |
| Confirmation | 8 Test rapide positif → 1 Biologie |
| In vivo ↔ in vitro | 6 Allergologie ↔ 1 IgE spécifiques |
| Sommeil | 3 Explorations S11 ↔ S1, S4 |
| Suivi thérapeutique | 1 Biologie, 3 ECG → fiche molécule (pharmacologie) |
| Diagnostic psychiatrique | 9 Psychométrie → pathologie CIM-10 (S11) |
| Fondement | toute fiche → Sciences fondamentales |

---

## 6. Module Sciences fondamentales

Par système : Anatomie · Embryologie et histologie · Physiologie · Biochimie et biologie moléculaire · Physiopathologie générale. Transversaux : Génétique · Immunologie · Microbiologie · Biostatistique et épidémiologie. Gabarit : cadre d'ensemble → entités → liens logiques → ponts cliniques.
Pour S11 : neurobiologie des circuits et des neurotransmetteurs, chronobiologie et physiologie du sommeil, psychologie du développement.

---

## 7. Cartographie des emplacements d'examens

Système principal en premier ; étiquettes secondaires entre crochets. « — » = aucun examen, case affichée.

### Sous-onglet 1 · Biologie médicale

| Système | Emplacements |
|---|---|
| S1 Neurologie | LCR : cytologie · LCR : protéines, albumine, glucose · LCR : lactates · LCR : PCR multiplex · LCR : auto-anticorps (NMDA, AQP4) · Vitamines B1 et B12 · Ammoniémie · Auto-anticorps onconeuronaux · Taux des antiépileptiques |
| S2 Tête, cou, ORL, CMF et ophtalmologie | Prélèvement de gorge · Prélèvement oculaire · Prélèvements ORL : bactériologie et virologie · IgE spécifiques des pneumallergènes |
| S3 Cardiovasculaire | Troponines hypersensibles · BNP et NT-proBNP · Bilan lipidique · Hémocultures · ANCA · Digoxinémie et suivi des antiarythmiques |
| S4 Respiratoire et thorax | Gaz du sang artériels · Alpha-1-antitrypsine · LBA et expectorations : cytologie · PCR Aspergillus · PCR respiratoires multiplex · Test de la sueur · Liquide pleural : critères de Light |
| S5 Digestif et hépato-bilio-pancréatique | Bilan hépatique : ASAT, ALAT, PAL, GGT, bilirubine · TP et facteur V · Lipase · Albumine · Selles : parasitologie · Calprotectine fécale · Alpha-1-antitrypsine fécale · Sérologies des hépatites A à E · Sérologie cœliaque · Liquide d'ascite |
| S6 Néphro-urologique | Créatinine, DFG, urée · Ionogramme : sodium et osmolalité · Ionogramme : potassium · Équilibre acide-base · ECBU · Protéinurie et albuminurie · Sédiment urinaire et cristallurie · Analyse des calculs · Complément · Anticorps anti-membrane basale glomérulaire |
| S7 Reproduction, gynéco-obstétrique et sénologie | hCG · FSH et LH · Œstradiol et progestérone · Testostérone · Spermogramme · Prélèvements vaginaux et lochies · Test de Kleihauer · Marqueurs sériques de la trisomie 21 |
| S8 Endocrino-métabolique et nutrition | Glycémie et HbA1c · TSH, T4 libre, T3 libre · Cortisol et ACTH · Rénine et aldostérone · PTH · Vitamines D, B12, B9, B1 · Oligo-éléments · Acylcarnitines |
| S9 Appareil locomoteur | Calcium et phosphate · Phosphatases alcalines osseuses · CTX et PINP · Acide urique · CPK · Facteur rhumatoïde et anti-CCP · HLA-B27 · Liquide synovial : cytologie et cristaux |
| S10 Sang et immunité | Hémogramme : lignée rouge · Hémogramme : leucocytes et formule · Plaquettes · Frottis sanguin · Réticulocytes · Vitesse de sédimentation · TP, INR et TCA · Fibrinogène et D-dimères · Suivi biologique des anticoagulants · Ferritine et bilan martial · Hémolyse : haptoglobine, LDH, bilirubine · Myélogramme · Électrophorèse des protéines · Immunoglobulines G, A, M, E · Lymphocytes CD4 et CD8 · Sérologies VIH, VHB, VHC · Bilan prétransfusionnel |
| S11 Psychiatrie et sommeil | Bilan initial du premier épisode psychiatrique · Bilan étiologique du delirium · Lithiémie et surveillance du lithium (TSH, calcium, créatinine) · Surveillance du valproate et de la carbamazépine · Surveillance de la clozapine (neutrophiles, troponine, CRP) · Bilan métabolique sous antipsychotique · Prolactine · Taux des antidépresseurs et antipsychotiques · Dépistage toxicologique urinaire et sanguin · Marqueurs de consommation d'alcool (CDT, PEth, GGT, VGM) |
| S12 Peau et phanères | Prélèvement mycologique · PCR herpès sur lésion |
| T Transversaux | Marqueurs tumoraux · Toxicologie d'urgence |

### Sous-onglet 2 · Imagerie médicale

| Système | Emplacements |
|---|---|
| S1 Neurologie | Radiographie et TDM du système nerveux central · IRM encéphalique et médullaire · Échographie transfontanellaire · Médecine nucléaire cérébrale · Neuroradiologie interventionnelle |
| S2 Tête, cou, ORL, CMF et ophtalmologie | Radiographie et TDM des sinus, rochers et massif facial · Échographie et IRM cervico-faciales · Cytoponctions guidées |
| S3 Cardiovasculaire | Radiographie et TDM thorax-cœur · Coroscanner · Écho-Doppler des troncs supra-aortiques, des membres et des fistules · IRM cardiaque · Scintigraphie myocardique |
| S4 Respiratoire et thorax | Radiographie du thorax · TDM thoracique haute résolution · Angio-TDM thoracique · Échographie pleurale · Scintigraphie de ventilation-perfusion · Ponction et biopsie guidées |
| S5 Digestif et hépato-bilio-pancréatique | Échographie abdominale · Doppler porte · TDM abdomino-pelvienne · Bili-IRM · Biopsie guidée du foie et du pancréas |
| S6 Néphro-urologique | Échographie rénale et vésicale · Uro-TDM · IRM rénale et prostatique · Scintigraphie rénale · Biopsie guidée du rein et de la prostate |
| S7 Reproduction, gynéco-obstétrique et sénologie | Échographie pelvienne et fœtale · Mammographie · IRM mammaire et pelvienne · Biopsie guidée du sein |
| S8 Endocrino-métabolique et nutrition | Échographie thyroïdienne · TDM des surrénales · IRM hypophysaire · Scintigraphies thyroïdienne, parathyroïdienne et MIBG · Ostéodensitométrie |
| S9 Appareil locomoteur | Radiographie standard et âge osseux · Échographie ostéo-articulaire · TDM ostéo-articulaire · IRM du rachis et des membres · Scintigraphie osseuse · Biopsie osseuse guidée |
| S10 Sang et immunité | Échographie ganglionnaire · TDM d'extension · TEP-TDM · IRM médullaire |
| S11 Psychiatrie et sommeil | IRM cérébrale du premier épisode psychotique · Imagerie des troubles neurocognitifs (renvoi S1) |
| T Transversaux | Imagerie pédiatrique · Imagerie oncologique · Imagerie des urgences : FAST, polytraumatisé |

### Sous-onglet 3 · Explorations fonctionnelles

| Système | Emplacements |
|---|---|
| S1 Neurologie | EEG de l'adulte, de l'enfant et du nouveau-né · Potentiels évoqués · Électroneuromyogramme |
| S2 Tête, cou, ORL, CMF et ophtalmologie | Audiométrie · Vidéonystagmographie · Champ visuel automatisé · Pachymétrie cornéenne |
| S3 Cardiovasculaire | ECG · Holter ECG · Mesure ambulatoire de la pression artérielle · Épreuve d'effort · Échocardiographie transthoracique et transœsophagienne · Index de pression systolique et explorations vasculaires |
| S4 Respiratoire et thorax | Spirométrie et test de réversibilité · Pléthysmographie · DLCO · Pressions respiratoires · Test de marche de 6 minutes · Oxymétrie nocturne · Test de provocation bronchique |
| S5 Digestif et hépato-bilio-pancréatique | Manométrie œsophagienne et anorectale · pH-impédancemétrie · Temps de transit colique · Tests respiratoires (H. pylori, lactose) |
| S6 Néphro-urologique | Débitmétrie · Cystomanométrie · Épreuves fonctionnelles rénales dynamiques |
| S7 Reproduction, gynéco-obstétrique et sénologie | Cardiotocographie · Explorations pelvi-périnéales |
| S8 Endocrino-métabolique et nutrition | Calorimétrie indirecte · Impédancemétrie · Épreuves dynamiques : Synacthène, HGPO, freinage |
| S9 Appareil locomoteur | Explorations motrices et posturales |
| S10 Sang et immunité | Capillaroscopie |
| S11 Psychiatrie et sommeil | Polysomnographie [S1 S4] · Polygraphie ventilatoire nocturne [S1 S4] · Test itératif de latence d'endormissement · Test de maintien de l'éveil · Actimétrie · Agenda du sommeil · ECG sous psychotropes : QT · EEG en psychiatrie : delirium, catatonie, avant électroconvulsivothérapie |
| S12 Peau et phanères | Dermatoscopie |

### Sous-onglet 4 · Anatomie et cytologie pathologiques

| Système | Emplacements |
|---|---|
| S1 Neurologie | Biopsie de nerf, de muscle, de cerveau · Cytologie du LCR |
| S2 Tête, cou, ORL, CMF et ophtalmologie | Cytoponction ganglionnaire et salivaire · Biopsie des glandes salivaires accessoires |
| S3 Cardiovasculaire | Biopsie myocardique · Biopsie d'artère temporale |
| S4 Respiratoire et thorax | Cytologie du LBA et du liquide pleural · Biopsie de bronche, de poumon, de plèvre |
| S5 Digestif et hépato-bilio-pancréatique | Biopsies digestives étagées · Pièces d'exérèse digestives · Cytoponction du pancréas |
| S6 Néphro-urologique | Biopsie rénale : optique, immunofluorescence, électronique · Biopsie prostatique · Cytologie urinaire |
| S7 Reproduction, gynéco-obstétrique et sénologie | Biopsie du sein, de l'endomètre, du col · Frottis cervico-utérin |
| S8 Endocrino-métabolique et nutrition | Cytoponction thyroïdienne (Bethesda) |
| S9 Appareil locomoteur | Biopsie osseuse, synoviale, des tissus mous |
| S10 Sang et immunité | Biopsie ostéo-médullaire · Biopsie ganglionnaire |
| S12 Peau et phanères | Biopsie cutanée et immunofluorescence directe |

### Sous-onglet 5 · Endoscopies diagnostiques

| Système | Emplacements |
|---|---|
| S1 Neurologie | — |
| S2 Tête, cou, ORL, CMF et ophtalmologie | Endoscopie nasale et nasofibroscopie |
| S3 Cardiovasculaire | — |
| S4 Respiratoire et thorax | Bronchoscopie et brossage |
| S5 Digestif et hépato-bilio-pancréatique | Œso-gastro-duodénoscopie · Coloscopie · Duodénoscopie et brossage biliaire · Écho-endoscopie |
| S6 Néphro-urologique | Cystoscopie · Urétéroscopie |
| S7 Reproduction, gynéco-obstétrique et sénologie | Hystéroscopie · Colposcopie |
| S8 Endocrino-métabolique et nutrition | — |
| S9 Appareil locomoteur | Arthroscopie diagnostique |
| S10 Sang et immunité | — |

### Sous-onglet 6 · Allergologie clinique (in vivo)

| Système | Emplacements |
|---|---|
| S2 Tête, cou, ORL, CMF et ophtalmologie | Prick-tests aux pneumallergènes |
| S4 Respiratoire et thorax | Tests cutanés aux allergènes respiratoires |
| S5 Digestif et hépato-bilio-pancréatique | Tests cutanés et provocation orale alimentaires · Entérocolite induite par les protéines alimentaires |
| S10 Sang et immunité | Tests cutanés aux médicaments · Tests cutanés aux produits de contraste · Tests cutanés aux venins |
| S12 Peau et phanères | Tests épicutanés (patch-tests) |

### Sous-onglet 7 · Génétique médicale et génomique

| Système | Emplacements |
|---|---|
| S1 Neurologie | Panels de neurogénétique et expansions nucléotidiques |
| S3 Cardiovasculaire | Panels des cardiomyopathies et des canalopathies |
| S5 Digestif et hépato-bilio-pancréatique | Tests compagnons KRAS, NRAS, BRAF |
| S6 Néphro-urologique | Oncogénétique rénale et prostatique |
| S7 Reproduction, gynéco-obstétrique et sénologie | Dépistage prénatal non invasif · Caryotype fœtal et ACPA · MLPA du chromosome Y · BRCA1 et BRCA2 |
| S8 Endocrino-métabolique et nutrition | Panels des maladies métaboliques |
| S9 Appareil locomoteur | MLPA du gène SHOX et génétique osseuse |
| S10 Sang et immunité | Caryotype, FISH et NGS en onco-hématologie |
| S11 Psychiatrie et sommeil | Pharmacogénétique des psychotropes (CYP2D6, CYP2C19) · Génétique du retard mental (X fragile, ACPA) |

### Sous-onglet 8 · Tests rapides au point de soin

| Système | Emplacements |
|---|---|
| S2 Tête, cou, ORL, CMF et ophtalmologie | Test rapide du streptocoque A |
| S4 Respiratoire et thorax | Tests rapides grippe, SARS-CoV-2, VRS |
| S6 Néphro-urologique | Bandelette urinaire |
| S7 Reproduction, gynéco-obstétrique et sénologie | Test de grossesse urinaire |
| S8 Endocrino-métabolique et nutrition | Glycémie capillaire |
| S10 Sang et immunité | Tests rapides VIH, VHC, VHB |
| S11 Psychiatrie et sommeil | Tests urinaires rapides des drogues · Éthylotest et alcoolémie |
| T Transversaux | CRP capillaire |

### Sous-onglet 9 · Évaluations cognitives et psychométriques

| Système | Emplacements |
|---|---|
| S1 Neurologie | Tests cognitifs de dépistage (MMSE, MoCA) · Bilan neuropsychologique · Épreuves exécutives (Go/No-Go) |
| S11 Psychiatrie et sommeil | AMDP : examen psychopathologique standardisé · Dépression : dépistage et sévérité (PHQ-9, MADRS, HAM-D, GDS, EPDS) · Manie (YMRS) · Anxiété (GAD-7, HAM-A) · Trouble obsessionnel-compulsif (Y-BOCS) · Stress post-traumatique (PCL-5) · Troubles psychotiques (PANSS, BPRS) · Risque suicidaire · Addictions (AUDIT, Fagerström, CAGE) · TDAH (Conners enfant, ASRS adulte) · Troubles du spectre autistique (M-CHAT, ADOS) · Troubles des conduites alimentaires (SCOFF, EDE-Q) · Sommeil (Epworth, ISI, PSQI) · Delirium (CAM) · Personnalité · Capacité de discernement |

---

## 8. Nomenclature et granularité

| Module | Identifiant | Exemple |
|---|---|---|
| Examens | EX-[sous-onglet]-[système]-[nom] | EX-1-S11-lithiemie |
| Pharmacologie | PH-[système]-[chapitre]-[molécule] | PH-S11-antidepresseurs-sertraline |
| Pathologie psychiatrique | PS-[code CIM-10] | PS-F32.2 |
| Sciences fondamentales | SF-[système]-[discipline]-[notion] | SF-S11-physiologie-sommeil |

- L'identifiant ne change jamais ; titres modifiables.
- **Créer** une fiche : indications et lecture propres. **Fusionner** : toujours interprétés ensemble. **Scinder** : temps 3 > 12 lignes.
- Données en fichiers séparés de la page ; un script assemble et contrôle (identifiants uniques, passerelles valides, aucune case vide sans « — », aucun terme vague sans chiffre dans une posologie).

---

## 9. Ordre de construction

1. Figer le référentiel des systèmes (partie 2). **Fait.**
2. Figer sous-onglets, entrées, axes (partie 5). **Fait.**
3. Arrêter la liste des emplacements et leurs identifiants (parties 4, 7, 8).
4. Générer toutes les fiches vides.
5. Tracer les passerelles entre fiches vides.
6. Contrôle automatique.
7. Afficher et relire la charpente publiée.
8. Remplir par système, par ordre d'importance pour l'examen, avec sources suisses ; réinjecter le contenu archivé (cardiovasculaire, infectiologie, 10 fiches de biologie, 1 d'imagerie) dans les nouveaux emplacements.

---

## 10. Corrections apportées à la demande

| Demande | Correction |
|---|---|
| « CIM-10 de F1 à F9 » | **F0 à F9** : dix blocs, F00–F09 (troubles organiques, dont démences et delirium) inclus ; plus F99. |
| Sommeil en psychiatrie | Retenu. Mais dans la CIM-10, les troubles organiques du sommeil (apnées, narcolepsie, jambes sans repos) sont codés **G47**, chapitre neurologique. Ils sont rangés en S11 avec leur code G, étiquetés S1 et S4. |
| Critères « exactement comme la CIM-10 » | La CIM-10 a deux textes : **descriptions cliniques** (base retenue) et **critères pour la recherche** (seulement pour un chiffre manquant, signalé). |
| Démences | À cheval : maladie et anti-démentiels en S1 ; symptômes psychiques et comportementaux, delirium en S11. |
| Groupes d'âge | Vue par âge ajoutée **à côté** de la vue CIM-10, pas à la place : la CIM-10 reste la coque, l'âge est un filtre. |
