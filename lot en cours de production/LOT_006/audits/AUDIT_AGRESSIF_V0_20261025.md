# Audit agressif V0 — LOT_006 — G6 Fièvre, frissons, hyperthermie

Date de lecture : 25 octobre 2026 (Europe/Zurich).
Référentiel : PROMPT ULTIME V0. Le score structurel « 98,8 % » du générateur V7 est rejeté comme score clinique.
Nature : rapport seul. Aucune monographie réécrite. Aucun dépôt dans Drive Finaux. Aucune fusion.

**Prêt-dépôt : NON.**

Question finale, pour le SSP et pour chacun des dix DX : **non**. Un candidat qui apprendrait ces fichiers ne peut pas viser 90 à 100 % des points de l’examen fédéral sur ce sujet, ni conduire chaque patient fébrile en sécurité à partir du seul texte.

## 1. Inventaire — ce qui existe vraiment

| Lieu | Constat lu cette session |
|---|---|
| Dossier Drive Finaux `1vg3IgMz_r-fvZWdMYP97oZs4XlWB6m8E` | Dossier présent, parent `LOTS_Finaux avec statut`, modifié le 2026-10-23 18:23 UTC. **Liste des enfants : vide.** |
| Archive Drive `1sl9nMTE0NyyS8Xmp87QkF9YSe0bds4X-` | Cinq Google Docs V5 « Ultra-Pédagogique », 8,9 à 11,6 Ko de métadonnée Drive, lus en texte. Conversion Docs : formules cassées, fenêtres devenues des ancres. |
| Git `origin/tunder/passation`, fichier `LOT_Tunder/LOT_006_AUDITE.zip` (313 724 octets) | **Seul corpus HTML complet.** Douze HTML + `PROGRESS.md`, horodatés 2026-10-24 18:26–18:41. C’est ce corpus qui est noté ci-dessous. |
| `LOT_Tunder/STATUT_LOTS_001_248.csv` | « AUDITÉ — sur Drive LOT_Tunder seulement », 5/5, même identifiant de dossier que le Finaux aujourd’hui vide. |
| `BASE_LOTS_CUMUL` `lots_cumul.csv` | LOT_006 : A 11/11, B 11/11, combiné 100 %, statut « audité », source « Drive ». Ce 100 % est un compteur de cases, pas la grille V0. |
| État des lieux flash (Drive, 2026-10-25) | « Statut Tunder : AUDITÉ — sur Drive LOT_Tunder seulement ». Aucune branche `audit/LOT_006` ni `flash/*` pour ce lot. Le 98,8 % cité dans le commit `audit/LOT_005` concerne le lot 005, pas le 006. |
| `main` et branches `beta/g6-lot*` | Cours G6 en 14 parties (`data/tip/G6.json`, 45 731 octets) et assets historiques. Ce n’est pas une monographie V0 à 150–200 Ko. |

`PROGRESS.md` du zip attribue **98,8 %** (`verif OK`) à l’Appel A et à chacun des dix DX. Ce chiffre est la sortie de `source/eval.sh` (vérificateur structurel V7). Il ne mesure ni la bande de poids par entité, ni la vérité des dénominateurs, ni la phrase coupée par une fenêtre.

Ko du tableau = octets / 1 000, comme le journal Tunder (« 92 Ko » pour 92 308 octets).

| Entité | Fichier | Octets | Ko | SHA-256 | Bande 150–200 Ko |
|---|---|---:|---:|---|---|
| SSP G6, partie a (points 1–8) | `LOT_006_Appel_A_SSP_G6_Fievre_AUDITÉ_a.html` | 104 115 | 104,1 | `b78f27e1318b742be277c59e36cbdf8c376f9b577ad460504790bba1961e5b4d` | fragment |
| SSP G6, partie b (points 9–14) | `LOT_006_Appel_A_SSP_G6_Fievre_AUDITÉ_b.html` | 142 135 | 142,1 | `3c5910b2bf4d3f789bcb8a4be2baed2801d1152e89d4a4f8a409428ce9a0f85d` | fragment |
| **SSP G6 entier (a+b)** | les deux fichiers | **246 250** | **246,3** | — | **au-dessus de 200** |
| DX.1 Respiratoire | `…_DX1_Infections_respiratoires_AUDITÉ.html` | 153 009 | 153,0 | `fcd03ba267769ac3cc88dd0a65803b2b968552b73f3f13a96cc513ba7a65b0fd` | dans la bande |
| DX.2 Urinaire | `…_DX2_…` | 92 308 | 92,3 | `69621ca9f8d9b6555ee3f83e79b55a7e3b8cf9ae7d764ae45ce40981270df3e9` | en dessous |
| DX.3 Digestif | `…_DX3_…` | 118 028 | 118,0 | `50855ae95c95f547f26e0aaeae9444a1e96118521e6db41ce6f9c552a1b1ce35` | en dessous |
| DX.4 Peau | `…_DX4_…` | 90 070 | 90,1 | `d7f6daf2482f5f44402d14b5b583760427d6760fd20b00d7c263fbce878ff796` | en dessous |
| DX.5 Méningite | `…_DX5_…` | 132 856 | 132,9 | `19d206a8f5c4b4d6f7001fd5035a5515140a9b31bd081bb8e6de569e151eceb5` | en dessous |
| DX.6 Endocardite | `…_DX6_…` | 130 966 | 131,0 | `3a011060b2f5fa10ec6b514fe371f11ca618ae046bf9dcd59afc37c5cb8cf5c3` | en dessous |
| DX.7 Ostéo-articulaire | `…_DX7_…` | 123 146 | 123,1 | `3ab52fffe11a1b1d3b0771ea070defc4b27d31e605fee80af5fe5a564d13996e` | en dessous |
| DX.8 Systémique | `…_DX8_…` | 136 847 | 136,8 | `31685733156bfac7d38e3559931ce84f79d0b90ac9c9efd880637e8b8ad2a55c` | en dessous |
| DX.9 Cancer | `…_DX9_…` | 151 724 | 151,7 | `0c823239ae81231f89f9a11be54b0ebe559ab59481c0dcb8f0bd04491af3bbd8` | dans la bande |
| DX.10 Importation | `…_DX10_…` | 116 232 | 116,2 | `16000c582914a643ec755833bf1496a76404eb3374904edd1c3082d4f0da8253` | en dessous |

Huit DX sur dix sont sous 150 Ko. Le SSP dépasse 200 Ko une fois les deux parties réunies. Seuls DX.1 et DX.9 tombent dans la bande, et la question finale reste « non » pour eux. Chaque HTML a au moins une ligne de plus de 3 000 caractères (maximum observé : 13 707 dans la partie b).

Les cinq Google Docs d’archive ne sont pas notés comme livrable : ils ne sont pas du HTML, et le zip les présente comme l’original déjà corrigé. Ils restent une preuve d’écart. Exemple lu dans l’Appel A V5 : « Ceftriaxone 2 g IV/24h pour pyélonéphrite ou méningite ». Le HTML SSI ultérieur sépare pyélonéphrite instable 1 g/j et méningite 2 g toutes les 12 heures. La version Docs, si elle était encore servie, serait dangereuse.

## 2. Liste DX — Phase A et Phase B

Thèmes et ordre : les dix mêmes familles, DX.1 puis DX.10, dans l’Appel A (partie b) et dans les dix fichiers. Aucun badge 🚩. Aucun rang E1, E2, E3. Le mot « corrélation » et le numérotage « 7.1 » sont absents des douze HTML.

Les pourcentages ronds V5 (40 %, 18 %, 12 % …) ont été retirés. À leur place, des chiffres sourcés **qui ne partagent pas le même dénominateur** :

| N° | Intitulé Phase A (liste) | Chiffre cité comme rang | Intitulé du fichier Phase B |
|---|---|---|---|
| DX.1 | Infections respiratoires | 27,2 % des adultes fébriles aux urgences (Pays-Bas) | Infections des voies respiratoires hautes et basses (rhinopharyngite, angine, sinusite, bronchite, pneumonie) |
| DX.2 | Infections urinaires | près de la moitié des femmes au cours de la vie | Cystite, pyélonéphrite, prostatite et urosepsis |
| DX.3 | Gastro-entérites infectieuses | campylobactériose 92/100 000 par an (Suisse, 2024) | Virales, bactériennes, toxiniques et *Clostridioides difficile* |
| DX.4 | Peau et tissus mous | cellulite 199/100 000 personnes-années | Érysipèle, cellulite, abcès et fasciite nécrosante |
| DX.5 | Méningites et encéphalites | méningocoques 0,4/100 000 ; FSME 5,5/100 000 (Suisse) | Méningite bactérienne, encéphalite herpétique, encéphalite à tiques |
| DX.6 | Endocardite infectieuse | 13,8/100 000 par an (monde, 2019) | Fièvre, souffle, embolies, hémocultures et échocardiographie |
| DX.7 | Infections ostéo-articulaires | spondylodiscite 12,4/100 000 (Allemagne, 2019) | Arthrite septique, ostéomyélite, spondylodiscite, infection de prothèse |
| DX.8 | Maladies systémiques et connectivites | 22 % des fièvres d’origine inconnue | Lupus, artérite à cellules géantes, Still, polyarthrite rhumatoïde |
| DX.9 | Néoplasies et hémopathies | 7 % des fièvres d’origine inconnue | Fièvre néoplasique, lymphomes, leucémies et neutropénie fébrile |
| DX.10 | Fièvres d’importation | paludisme 21 % des voyageurs fébriles | Paludisme, dengue, fièvre entérique et rickettsioses |

Le critère V0 « mêmes noms, mot pour mot » n’est pas tenu : chaque titre B est une expansion. L’ordre n’est pas une prévalence suisse décroissante : une incidence mondiale d’endocardite (DX.6) est placée après une incidence suisse de méningocoque (DX.5), et une prévalence vie-entière de cystite (DX.2) est comparée à une part d’urgences néerlandaises (DX.1). La fasciite nécrosante et le paludisme grave n’ont ni badge ni rang d’exclusion en tête de liste. Un tableau comparatif existe dans la partie b ; ses cellules sont envahies par des fenêtres d’examen (radiographie, CRP, ponction lombaire, hémocultures) qui débordent le signe discriminant.

## 3. Grille 14 points — notes 2 / 1 / 0

Quarante-six questions, maximum 92. Note 2 = pleinement satisfaite, 1 = partielle, 0 = absente ou fausse. Le générateur est le même pour les onze monographies : la grille de base est commune. Deux monographies perdent des points supplémentaires, indiqués sous le tableau.

| Point | Questions | Notes de base | Obtenu / max |
|---|---|---|---|
| 1 Définition | 1.1 société datée ; 1.2 concision ; 1.3 notions voisines | 1, 2, 2 | 5 / 6 |
| 2 Épidémiologie | distribution, histoire naturelle, enjeux, chiffres sourcés | 1, 1, 1, 1 | 4 / 8 |
| 3 Physiopathologie | cascade, complications, lien au traitement, **tableau de corrélation**, concision | 2, 1, 1, **0**, 1 | 5 / 10 |
| 4 Démarche | graves d’abord ; signe qui tranche et piège | 1, 1 | 2 / 4 |
| 5 Anamnèse | raison physiopathologique ; drapeaux actionnables | 1, 1 | 2 / 4 |
| 6 Examen | normal avant pathologique ; technique et valeur | 1, 1 | 2 / 4 |
| 7 Syndromes | **7.1 numérotés**, fonctionnel / physique, définition, geste, mécanisme | **0**, 1, 1, 1, 1 | 4 / 10 |
| 8 Critères | société et année ; ce qui ne suffit pas | 1, 1 | 2 / 4 |
| 9 Examens | gold standard, intentions, prescription, interprétation, cas, alternatives | 1, 1, 1, 1, 1, 1 | 6 / 12 |
| 10 Arbre | embranchement signe → décision | 1 | 1 / 2 |
| 11 Prise en charge | but chiffré, ordre, urgences, formes simples, médicaments, non médicamenteux, social, situations spéciales, surveillance, sortie, pronostic | 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1 | 12 / 22 |
| 12 Prévention | trois niveaux avec substance suisse | 1 | 1 / 2 |
| 13 Points clés | 3 à 6 phrases intactes | 1 | 1 / 2 |
| 14 Pièges | piège et bonne réponse | 1 | 1 / 2 |
| **Total de base** | | | **48 / 92 = 52,2 %** |

Ajustements :

- Phase A (SSP) : Q2.4 = 0 et Q4.1 = 0, parce que l’ordre est présenté comme une prévalence alors que les dénominateurs sont incompatibles et que les urgences vitales n’ouvrent pas la liste. **46 / 92 = 50,0 %.**
- DX.5 : Q11.1 = 0. La phrase d’ouverture dit que l’étude néerlandaise a fait passer la mortalité de 30 % à 20 %. Le tableau plus bas donne la dexaméthasone à 10 mg toutes les 6 heures pendant 4 jours, ce qui rejoint l’ESCMID 2016 ouverte pendant cet audit. Les deux énoncés coexistent ; le chiffre 30 → 20 reste faux dans le texte principal. **47 / 92 = 51,1 %.**

Les quatorze titres sont présents. Les sous-titres 9.a–9.e et 11.A–11.D sont présents. Le 9.b regroupe première et seconde intention ; le 9.c est la prescription ; le 9.d est l’interprétation ; le 9.e porte les alternatives. Le plan V0 place les alternatives en 9.c et la seconde intention en 9.d : le contenu est décalé. Le point 3 a une « chaîne logique » anatomie → clinique, sans le tableau « lésion → exploration → thérapeutique ». Le point 7 a un tableau de syndromes, sans 7.1 / 7.2.

### Tableau des scores

| Entité | Score V0 | Seuil ≥ 90 % | Question finale | Décision |
|---|---:|---|---|---|
| Phase A — SSP G6 | **50,0 %** (46/92) | non | **non** | refusé |
| DX.1 Respiratoire | **52,2 %** (48/92) | non | **non** | refusé |
| DX.2 Urinaire | **52,2 %** (48/92) | non | **non** | refusé |
| DX.3 Digestif | **52,2 %** (48/92) | non | **non** | refusé |
| DX.4 Peau / fasciite | **52,2 %** (48/92) | non | **non** | refusé |
| DX.5 Méningite / encéphalite | **51,1 %** (47/92) | non | **non** | refusé |
| DX.6 Endocardite | **52,2 %** (48/92) | non | **non** | refusé |
| DX.7 Ostéo-articulaire | **52,2 %** (48/92) | non | **non** | refusé |
| DX.8 Connectivites | **52,2 %** (48/92) | non | **non** | refusé |
| DX.9 Cancer / neutropénie | **52,2 %** (48/92) | non | **non** | refusé |
| DX.10 Fièvres d’importation | **52,2 %** (48/92) | non | **non** | refusé |

Le lot est refusé dès le premier fichier. Aucune moyenne ne compense.

## 4. Trois critiques qui bloquent le dépôt

### Critique 1 — Poids et score structurel

La bande V0 est 150–200 Ko **par SSP et par DX**. Huit DX sont en dessous (90,1 à 136,8 Ko). Le SSP réuni pèse 246,3 Ko. Le journal célèbre pourtant 98,8 % et note « 92 Ko » ou « 90 Ko » comme un achèvement. Ce 98,8 % compte des titres, des fenêtres et un script `eval.sh`. Il ne voit pas l’omission de volume, ni le dépassement du SSP, ni les lignes de plus de 3 000 caractères. Le registre cumulé qui affiche 11/11 et 100 % est le même genre de compteur. Il ne vaut pas une validation V0.

### Critique 2 — Liste, gravité, fenêtres

L’ordre DX.1–DX.10 aligne des parts d’urgences, des prévalences vie-entière, des incidences et des parts de fièvre inexpliquée. Les titres B ne recopient pas les titres A. Méningite, fasciite et paludisme grave ne portent ni 🚩 ni rang E. Les fenêtres d’examen sont un bloc répété (hémocultures, scanner, IRM) qui importe goitre, embolie pulmonaire, adénome hypophysaire et orbitopathie dans la méningite et dans la pneumonie. La phrase de définition est coupée au milieu d’un mot :

> « sous l’effet de pyrogène » + fenêtre + « s. Elle se distingue de l’hyperthermie »

Le « s » du pluriel est resté hors de la fenêtre. Le même mécanisme coupe la SpO₂ dans le but chiffré du DX.1.

### Critique 3 — Chiffres de conduite

1. DX.5, point 11, phrase porteuse : « dans l’étude néerlandaise, la dexaméthasone a réduit la mortalité de 30 % à 20 % ». Plus bas, le tableau dit 10 mg toutes les 6 heures pendant 4 jours, et une ligne Cochrane parle de risque relatif 0,84 pour la mortalité à pneumocoque. L’ESCMID 2016, ouverte le 25 octobre 2026 (`Clinical Microbiology and Infection`, van de Beek et al.), énonce 10 mg toutes les 6 heures pendant 4 jours chez l’adulte, et 0,15 mg/kg toutes les 6 heures chez l’enfant. Le rythme adulte du tableau est donc aligné sur cette source. Le 30 % → 20 % de la phrase d’ouverture ne l’est pas. Le même fichier restreint la dexaméthasone de l’enfant aux moins de 5 ans non vaccinés contre *Haemophilus* : l’ESCMID 2016 ne pose pas cette restriction.
2. DX.10 met côte à côte Riamet® « AIPS : 24 comprimés sur 3 jours » et « Swiss TPH 2025 : 4 comprimés 2 fois par jour pendant 5 jours (40 comprimés) », sans dire laquelle appliquer demain. Les numéros Swissmedic cités (Rocephin® 44625, dexaméthasone 57974, etc.) viennent, selon les fichiers, du miroir ch.oddb.org le 24 octobre 2026. Cette session n’a pas rouvert swissmedicinfo.ch : ces numéros ne sont ni confirmés ni déclarés inventés.
3. La source [S73] de l’Appel A est le guide IDSA 2014 des infections de peau, et [S139] du DX.9 est le guide ASCO/IDSA 2018 de la neutropénie fébrile. V0 n’admet pas une recommandation exclusivement américaine comme référence de conduite.

## 5. Ce qui a été ouvert, et ce qui ne l’a pas été

Ouvert et lu : les douze HTML et `PROGRESS.md` du zip ; les cinq Google Docs d’archive ; les métadonnées et listes Drive ; `lots_cumul.csv` ; l’état des lieux flash (extrait LOT_006) ; l’ESCMID méningite 2016 (page éditeur) ; le critère OMS d’hyperparasitémie n’a pas été isolé comme un seuil unique de 2 % dans l’extrait des lignes directrices OMS du 30 novembre 2024 consulté ici. Le fichier DX.10 attribue « parasitémie > 2 % chez le non-immun » à l’OMS dans la couche Docs V5 ; le HTML renvoie les critères au Swiss TPH 2025. Cette attribution OMS de la couche V5 reste non confirmée.

Non ouvert pendant cette session : swissmedicinfo.ch, la page SSI `ssi.guidelines.ch/guideline/2315/fr`, le PDF de Gans 2002, le texte intégral Swiss TPH 2025. Les doses du HTML qui s’appuient seulement sur ces adresses restent « à revérifier sur la source primaire ».

## 6. Technique HTML (conformité)

Présents : `<!DOCTYPE html>`, `FIN_FICHIER`, `<details>`, tableaux souvent enveloppés de `overflow-x:auto`, section Sources, mention de non-validation clinique. Absents : attribut `title=` utilisé comme infobulle, scripts, images.

En défaut : lignes > 3 000 caractères dans chaque fichier ; en-tête de la partie b « points 9 à 15 » alors que le plan s’arrête au point 14 ; fenêtres qui coupent mots et phrases ; poids hors bande.

## 7. Décision

**Prêt-dépôt : NON.**

Le lot retourne au rédacteur. Le gel d’une liste canonique n’a pas lieu. Drive Finaux ne reçoit rien. Les trois critiques ci-dessus sont bloquantes, avec le score sous 90 % et la question finale « non ».

Contenu de ce rapport établi à partir des fichiers et des pages cités ; non validé cliniquement par un médecin.
