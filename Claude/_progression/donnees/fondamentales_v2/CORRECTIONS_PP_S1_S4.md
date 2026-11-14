# Corrections — PP-S1 à PP-S4 (suite de AUDIT_PP_S1_S4.md)

Rédacteur, 14.11.2026. Les 36 fiches ont été régénérées et comptent désormais 185 affections (143 avant correction). `verbal.py` ne trouve aucune phrase nominale sur 1 426 phrases ; `controle.py` est VERT ; tous les renvois SY, S, EX, IMG, PH, PP et LOT ont été vérifiés par script. Le schéma JSON de S1 à S4 reste inchangé, sur décision du coordinateur. Rien n'a été commité ni poussé.

## Exactitude

| # | Statut | Correction |
|---|---|---|
| E1 | Fait | PP-S2-I : le RAA naît du mimétisme moléculaire ; la GNA post-streptococcique naît du dépôt de complexes immuns, et la pénicilline ne la prévient pas. |
| E2 | Fait | PP-S1-A : les anticorps anti-RACh (IgG1-3) détruisent les récepteurs par le complément ; les anti-MuSK (IgG4) empêchent leur regroupement sans activer le complément. |
| E3, E4 | Fait | PP-S3-V : la fiche explique l'espace mort et l'effet shunt, renvoie à PP-S4-V et précise que la probabilité de Wells « n'est pas élevée ». |
| E5 | Fait | Le pneumothorax spontané passe dans PP-S4-D ; PP-S4-Tr garde les formes traumatique et compressive. |
| E6 à E10 | Fait | Syndrome malin : réflexes normaux ou diminués. GAFA : semi-mydriase. Parkinson : voies directe (D1) et indirecte (D2). Bezold-Jarisch : hypothèse discutée. Gépants : la fiche précise leur rôle dans la crise. |
| E11 | Fait | Le bilan du thymome renvoie à `EX-2-S3-radiographie-tdm-thorax-coeur` et non plus à l'angio-TDM. |
| IMG et EX | Fait | La fiche retire IMG-063 de l'abcès péri-amygdalien, IMG-151 de Fallot, IMG-084 de la SLA et le panel d'expansions de la NF. |

## Affections ajoutées (M1 à M9)

- **S1** : dissection carotidienne ou vertébrale (V) ; FSME (I) ; lymphome cérébral primitif (T) ; compression médullaire et queue de cheval, commotion cérébrale (Tr) ; NMOSD et MOGAD, névrite optique (A) ; trouble neurologique fonctionnel, polyneuropathie diabétique, sclérose combinée par carence en B12 (F).
- **S2** : rétinopathies diabétique et hypertensive (V) ; décollement de rétine, cholestéatome, otospongiose (D) ; angine de Ludwig, sialolithiase (I) ; névrite vestibulaire avec HINTS, surdité brusque (F) ; brûlure chimique avec « Rinçage immédiat et prolongé avant tout examen », fracture du rocher (Tr) ; ostéonécrose des mâchoires et angio-œdème des IEC, avec renvoi à PP-S9-Ia et PP-S12-Ia (Ia).
- **S3** : syndrome coronarien chronique (V) ; insuffisance mitrale, troubles de conduction (D) ; tachycardies par réentrée et WPW, TV et FV, Raynaud (F) ; Brugada, transposition des gros vaisseaux (C) ; Takayasu (A) ; intoxication digitalique (Ia).
- **S4** : SDRA (V) ; épanchement pleural avec critères de Light (F) ; maladie des membranes hyalines, hernie diaphragmatique (C) ; abcès pulmonaire, pneumocystose (I) ; corps étranger bronchique de l'enfant (Tr) ; pneumothorax spontané, pneumoconioses (D).

Sept IMG non demandés par l'audit restent sans affection : 005, 007, 018, 098, 119, 128 et 139. Il faudra les traiter dans une passe ultérieure.

## Sources et honnêteté

| # | Statut | Correction |
|---|---|---|
| S1, S3 | Fait | La Brain Trauma Foundation et l'ATLS portent l'étiquette « source américaine, hors hiérarchie » ; la fiche ajoute une source européenne (EAN, ESICM) avec la mention « non lue ». |
| S2 | Fait | Les fiches internes portent la mention « lues par leurs rédacteurs, non relues ici » ; aucune n'est marquée « lu ». |
| S4 | Fait | La source EGS ne reste qu'en S2-D et S2-F ; S2-V ajoute l'EULAR (vascularites), avec la mention « non lue ». |
| S5 | Partiel | La fiche ajoute une référence suisse avec URL par système (Swiss Stroke Society 2021 ; SSH 2018 ; dépistage CF par Barben 2023 et Rueegg 2013 ; SSP BPCO et asthme 2018). Aucun texte intégral n'a pu être lu (403, 503, PDF illisible) : toutes ces références restent marquées « non lu ». Pour S2, aucune source suisse n'a été trouvée. |
| S6 à S9 | Fait | Dépistage néonatal suisse (IRT puis ADN, depuis 2011) ; GINA, GOLD et ICHD-3 étiquetées « international, non européen » ; cyproheptadine et dexrazoxane marqués « absents du corpus AIPS local, À vérifier » ; dépistage par TDM marqué « programme suisse à vérifier ». |

## Renvois et style

- **R1, schéma** : la fiche ne change rien, sur ordre du coordinateur ; la page normalisera les variantes de champs.
- **R2, doublons** : cinq affections passent en forme courte avec `renvoi_physiopathologie` : hémorragie sous anticoagulant (S1-Ia et S3-Ia vers PP-S10-Ia), ACG (S2-V vers PP-S3-A), Hashimoto (S2-A vers PP-S8-A) et cancer thyroïdien (S2-T vers PP-S8-T). L'EP reste complète en S4-V, et S3-V garde la TVP. Les fiches S11 et S12 restent responsables de leurs propres doublons (S1 garde la forme complète).
- **R3, passerelles** : le texte provisoire « LOT correspondant » est supprimé. Chaque fiche renvoie à 1 à 3 LOT SSP du `CATALOGUE_248.csv` (numéro et code vérifiés par script) et à des passerelles croisées PP ↔ PP.
- **R4, style** : la fiche écrit « corticoïdes en bolus (selon AIPS) » et « exposition la plus courte possible ».

## Tour 2 (suite de AUDIT_PP_S1_S4_V2.md)

| # | Statut | Correction |
|---|---|---|
| S10 | Fait, mot pour mot | Chaque source suisse ne reste que dans la fiche qu'elle concerne : Michel 2021 en PP-S1-V ; SSH 2018 en PP-S3-F ; Barben 2023 et Rueegg 2013 en PP-S4-C ; SSP asthme 2018 en PP-S4-A ; SSP BPCO 2018 en PP-S4-D. Les 27 autres copies sont supprimées. |
| N1 | Fait, mot pour mot | PP-S1-Tr distingue la compression médullaire (niveau sensitif, syndrome pyramidal, troubles sphinctériens) du syndrome de la queue de cheval (déficit flasque, anesthésie en selle, rétention, perte du tonus anal). |
| N2 | Fait | La phrase de réserve sur le classement en Tr (causes tumorales PP-S9-T et dégénératives PP-S9-D) est ajoutée au champ `honnetete` de PP-S1-Tr. |
| N3 | Fait | TV et FV : la défibrillation dépolarise tout le myocarde ; une TV avec pouls relève d'une cardioversion synchronisée. |
| N4 | Fait | Lymphome cérébral primitif : la fiche précise « uvéite postérieure (lymphome vitréo-rétinien associé) ». |
| N5 | Partiel | Ludwig renvoie à `EX-2-S2-echographie-irm-cervico-faciales`, et Takayasu à `EX-2-S4-angio-tdm-thoracique`. Le dépôt ne contient aucun EX d'échographie oculaire : la liste du décollement de rétine reste vide. |

Validation : `verbal.py` ne trouve aucune phrase nominale sur 1 427 ; `controle.py` est VERT. Restent à faire, en compléments S5 : lire Michel 2021 (UNIGE, unige:152319) et les recommandations SSP 2018 ; chercher des sources SOG/SSO et SSORL pour S2 ; couvrir les IMG 005, 007, 018, 098, 119, 128 et 139.
