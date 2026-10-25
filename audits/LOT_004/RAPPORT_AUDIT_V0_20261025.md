# Audit agressif V0 — LOT_004 · G4 Fatigue, lassitude / fatigue, tiredness

| Champ | Valeur |
|---|---|
| Prompt | PROMPT ULTIME V0, lu en entier (upload du 25.10.2026) |
| Date | 25 octobre 2026, 20:25 Europe/Zurich |
| Rôle | Auditeur médical et de conformité. Non rédacteur de ce lot. Rapport seulement. |
| Matériau | Branche `origin/audit/LOT_004`, commit `cdb07f65` (« AUDIT LOT_004 — révision 1 »). Fichiers `AUDIT/LOT_004/LOT_004_*AUDITÉ*.html`. |
| Hors périmètre | Aucune fusion. Aucun message à l’owner. Aucun dépôt Drive. Aucune réécriture HTML (donc aucun auto-score d’une correction). |
| Score hérité | Le rapport du 24.10.2026 affiche **98,8 %** sur 12 fichiers. C’est un plafond automatique V7 (point 13.b « humain » laissé ouvert). **Ce chiffre n’est pas un score V0.** Il n’est pas repris. |

Grille : 46 questions d’obsession, notes 2 / 1 / 0, maximum 92, aucun « sans objet ». Seuil de validation ≥ 90 % et question finale « oui » et zéro critique. Cible 95–100 %.

Méthode réelle : texte principal des points 1, 2, 4, 8, 11, 13 et 14 de chaque entité (fenêtres d’examen retirées) ; lecture directe des points 1 à 5 et 9 du SSP, du bloc 2, du tableau comparatif, de l’algorithme et de la fiche médicament ; AIPS Ferinject® (authNr 57851) ouvert le 25.10.2026 ; recommandation Endocrine Society 2016 sur la crise, page publique ouverte le même jour. Les points 3, 6 et 7 des DX n’ont pas été relus fenêtre par fenêtre : ils sont notés 1 lorsque la rubrique existe, jamais 2 sur une fenêtre non lue. Un 2 n’est posé que sur un passage lu.

## 1. Inventaire et poids

Unité : **1 ko = 1 000 octets** (même convention que le rapport du 24.10.2026). Bande V0 : **150–200 ko par entité** (la monographie SSP, ou un DX), pas par fichier HTML. Le découpage `_a` / `_b` ne crée pas deux entités.

HTML « unique » SSP+10 DX : **absent**. Onze entités sont dans douze fichiers séparés. Conforme sur ce point. Les noms restent ceux de V7 (`Appel_A`, `AUDITÉ`), pas `LOT_004_Phase_A_V0_…`.

| Entité | Fichier(s) | Octets | ko | Bande brute 150–200 | HTML sans fenêtres `details.ex` | SHA-256 |
|---|---|---:|---:|---|---:|---|
| Phase A · SSP G4 | `…AUDITÉ_a.html` + `…_b.html` | 118 304 + 148 255 = **266 559** | **266,6** | **hors bande (trop lourd)** | 50 595 + 54 292 = **104 887** (sous 150) | `b0901bfa…f91050` · `63d88f53…c3fdf0` |
| DX.1 Anémie ferriprive | `…DX1_Anemie_ferriprive_AUDITÉ.html` | 180 551 | 180,6 | dans la bande | 63 623 | `8da628c2…2c67a4` |
| DX.2 Dépression, burn-out | `…DX2_Depression_burn_out_AUDITÉ.html` | 161 411 | 161,4 | dans la bande | 64 596 | `04b6be2c…15de96` |
| DX.3 SAOS | `…DX3_SAOS_AUDITÉ.html` | 133 458 | 133,5 | **sous 150** | 62 326 | `7ab37977…79bbf2` |
| DX.4 Hypothyroïdie primaire | `…DX4_Hypothyroidie_primaire_AUDITÉ.html` | 163 345 | 163,3 | dans la bande | 60 898 | `d9ce8558…72ce91` |
| DX.5 Asthénies post-infectieuses | `…DX5_Asthenies_post_infectieuses_AUDITÉ.html` | 164 400 | 164,4 | dans la bande | 58 316 | `3b5c840f…4a2c2c` |
| DX.6 Insuffisance cardiaque | `…DX6_Insuffisance_cardiaque_AUDITÉ.html` | 151 140 | 151,1 | dans la bande | 60 275 | `775212c4…29c9b26` |
| DX.7 Maladie rénale chronique | `…DX7_Maladie_renale_chronique_AUDITÉ.html` | 158 011 | 158,0 | dans la bande | 58 585 | `348a3efa…45cf76` |
| DX.8 Néoplasie occulte | `…DX8_Neoplasie_occulte_AUDITÉ.html` | 182 443 | 182,4 | dans la bande | 60 476 | `095c1bd9…a91513` |
| DX.9 EM/SFC, POTS | `…DX9_EM_SFC_POTS_AUDITÉ.html` | 127 863 | 127,9 | **sous 150** | 59 460 | `c0c45a12…fd9302` |
| DX.10 Addison | `…DX10_Maladie_d_Addison_AUDITÉ.html` | 154 935 | 154,9 | dans la bande | 58 488 | `98da8070…831dcd` |

Le poids brut des DX « dans la bande » est en grande partie des fenêtres d’examens répétées (DX.1 : 67 fenêtres `ex`, 26 examens distincts). Le HTML privé de ces fenêtres pèse **58–65 ko** pour chaque DX et **105 ko** pour le SSP. Ce n’est pas 150–200 ko de contenu propre à l’entité.

Contrôles de forme communs aux 12 fichiers : `FIN_FICHIER` présent ; aucun attribut `title=` ; 10 à 20 lignes de plus de 3 000 caractères par fichier (interdit V0) ; 14 intitulés présents sur chaque DX ; le fichier `_a` s’arrête au point 8, le fichier `_b` porte les points 9–14 et le bloc 2.

Drive Finaux, dossier `1tiOFaNiG3v21V8kIyGO_w1xpGZ8j95yL` : liste demandée le 25.10.2026, **0 fichier retourné** (accès insuffisant ou dossier vide). Aucun dépôt n’est annoncé.

## 2. Liste DX — cohérence A ↔ B, gravité, ordre

Le bloc 2 (fichier `_b`) et les dix fichiers DX portent **les mêmes dix entités, dans le même ordre**. Ce n’est pas l’erreur du LOT_001 (un nom en A, un autre en B). Les libellés ne sont pas mot pour mot : « épuisement professionnel » (bloc 2) contre « burn-out » (fichier DX.2) ; « tachycardie orthostatique » contre « POTS ». **Grave**, pas une substitution de maladie.

Le bloc 2 annonce un ordre « du plus fréquent au plus rare chez le patient fatigué ». Les chiffres imprimés dans le même tableau contredisent cette phrase.

| Rang du fichier | Diagnostic | Chiffre imprimé dans le bloc 2 | Chez le patient fatigué (Stadje 2016, [S2], résumé) |
|---|---|---|---|
| DX.1 | Anémie ferriprive | ≈ 3 000 / 100 000 femmes réglées (Europe) | 2,8 % |
| DX.2 | Dépression | ≈ 9 800 / 100 000 ≥ 15 ans (Suisse 2022) | **18,5 %** |
| DX.3 | SAOS | 23 400–49 700 / 100 000 (40–85 ans, Lausanne) | non chiffré dans Stadje |
| DX.4 | Hypothyroïdie | ≈ 4 940 / 100 000 (Europe) | non isolé |
| DX.5 | Asthénies post-infectieuses | « non publiée en population générale » | — |
| DX.6 | Insuffisance cardiaque | 1 000–2 000 / 100 000 adultes (Europe) | dans les 4,3 % « somatiques graves » |
| DX.7 | Maladie rénale chronique | ≈ 10 400 / 100 000 adultes (Suisse) | non isolé |
| DX.8 | Néoplasie occulte | ≈ 2 600 / 100 000 « à vérifier » | 0,6 % |
| DX.9 | EM/SFC ± POTS | ≈ 680 / 100 000 (monde) | SFC < 2 % |
| DX.10 | Addison | ≈ 10–14 / 100 000 (Europe) | — |

Sur la population générale, le SAOS lausannois et la maladie rénale chronique dépassent l’anémie placée en DX.1. Chez le patient fatigué, la dépression (18,5 %) dépasse l’anémie (2,8 %). Les dénominateurs ne sont pas les mêmes (femmes réglées, 40–85 ans, ≥ 15 ans, Europe, monde) : le classement n’est pas une prévalence suisse décroissante.

Gravité : **aucun badge 🚩, aucun rang E1, E2, E3** dans les douze fichiers. L’Addison, décrite comme mortelle, reste DX.10. L’algorithme ne commence pas par une exclusion numérotée. Son premier embranchement mélange « instabilité ou idée suicidaire » avec DX.2, DX.10 ou une anémie sévère, puis enchaîne l’hémoglobine avant la TSH, la créatinine et le NT-proBNP. L’Addison ne réapparaît qu’au signe « hyponatrémie, hypotension ».

Le tableau comparatif existe (signe, examen, mécanisme, décision). Il n’a pas de colonne « rang d’exclusion ».

DX.2 regroupe dépression et burn-out (le texte dit correctement que QD85 n’est pas une maladie). DX.5 regroupe EBV, CMV et VIH. DX.9 regroupe EM/SFC et POTS. Ce sont des catégories fourre-tout, **graves** pour la discrimination.

## 3. Scores V0 — 2 / 1 / 0

Maximum par point : 6, 8, 10, 4, 4, 4, 10, 4, 12, 2, 22, 2, 2, 2. Total 92.

| Entité | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | Somme | % | Finale |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| **Phase A · SSP** | 5 | 4 | 6 | 2 | 2 | 2 | 5 | 3 | 9 | 1 | 13 | 1 | 2 | 1 | **56/92** | **60,9 %** | **NON** |
| DX.1 Anémie | 5 | 5 | 5 | 2 | 2 | 2 | 5 | 4 | 9 | 1 | 16 | 1 | 2 | 2 | **61/92** | **66,3 %** | **NON** |
| DX.2 Dépression | 4 | 6 | 5 | 2 | 3 | 2 | 5 | 3 | 8 | 1 | 14 | 1 | 2 | 2 | **58/92** | **63,0 %** | **NON** |
| DX.3 SAOS | 4 | 5 | 5 | 2 | 2 | 2 | 5 | 3 | 8 | 1 | 13 | 1 | 2 | 2 | **55/92** | **59,8 %** | **NON** |
| DX.4 Hypothyroïdie | 4 | 5 | 5 | 2 | 2 | 2 | 5 | 3 | 8 | 1 | 15 | 1 | 2 | 2 | **57/92** | **62,0 %** | **NON** |
| DX.5 Post-infectieux | 4 | 4 | 5 | 2 | 2 | 2 | 5 | 3 | 8 | 1 | 13 | 1 | 2 | 1 | **53/92** | **57,6 %** | **NON** |
| DX.6 Insuff. cardiaque | 5 | 4 | 5 | 2 | 2 | 2 | 5 | 4 | 9 | 1 | 15 | 1 | 2 | 2 | **59/92** | **64,1 %** | **NON** |
| DX.7 MRC | 4 | 5 | 5 | 2 | 2 | 2 | 5 | 3 | 8 | 1 | 14 | 1 | 2 | 2 | **56/92** | **60,9 %** | **NON** |
| DX.8 Néoplasie | 4 | 4 | 5 | 2 | 2 | 2 | 5 | 3 | 8 | 1 | 14 | 1 | 2 | 2 | **55/92** | **59,8 %** | **NON** |
| DX.9 EM/SFC, POTS | 4 | 3 | 5 | 2 | 2 | 2 | 4 | 3 | 7 | 1 | 12 | 1 | 2 | 2 | **50/92** | **54,3 %** | **NON** |
| DX.10 Addison | 4 | 4 | 5 | 3 | 3 | 2 | 5 | 4 | 9 | 1 | 16 | 1 | 2 | 2 | **61/92** | **66,3 %** | **NON** |

**Question finale, toutes les phases : NON.** Aucune monographie n’atteint 90 %. Le lot est refusé. Un fichier à 66 % ne se compense pas par un autre.

### Phase A — questions qui ne valent pas 2

- **Q1.1 = 1.** La définition est une phrase générale. PROFILES est nommé, mais [S1] est marqué « non relu ». mediX 09/2024 ([S10]) n’a été lu que pour les durées, et seulement en partie.
- **Q2.1 à Q2.4 = 1.** Les 11–33 % (RMS 2006) et les 50–60 % (RMS 2015) reposent sur des résumés. Le chiffre « cancer ≈ 2 600 / 100 000, à vérifier » reste dans le tableau. Mortalité propre « non chiffrée ».
- **Q3.1, Q3.2, Q3.3, Q3.5 = 1 ; Q3.4 = 2.** Le tableau lésion → exploration → cible existe. La cascade est une liste de causes, pas une chaîne de la fatigue. Les cibles (fer, lévothyroxine) n’ont pas leur mécanisme médicamenteux dans ce tableau.
- **Q4.1 et Q4.2 = 1.** Les urgences sont nommées avant le bilan, puis la liste figée contredit la prévalence et n’a pas de piège par DD grave.
- **Q5.1 et Q5.2 = 1.** Le « pourquoi » des questions est souvent une orientation, pas un mécanisme. Les drapeaux rouges omettent la douleur thoracique.
- **Q6.1 et Q6.2 = 1.** Le pouls 60–100/min est donné avant les signes. La tension n’a pas de chiffre. La technique de chaque signe n’a pas été auditée au-delà du titre de fenêtre.
- **Q7.1 à Q7.5 = 1.** Syndromes anémique, dépressif et d’apnées présents. Pas de numérotation 7.1, 7.2. Pas d’éclatement systématique signes fonctionnels / signes physiques pour chaque syndrome.
- **Q8.1 = 1 ; Q8.2 = 2.** Le point 8 du SSP enseigne les critères IOM 2015 de l’EM/SFC, qui sont ceux d’un DX, pas du symptôme. « Plus de 6 mois ne suffit pas » est juste.
- **Q9.1 = 2, Q9.2 = 2, Q9.5 = 2 ; Q9.3, Q9.4, Q9.6 = 1.** L’absence de gold standard de la fatigue est dite. Le tableau d’interprétation existe, avec une TSH « ≈ 0,4–4 mU/L » qui contredit le DX.4 (ETA : 0,4–2,5 avant 70 ans). Les lettres 9.c et 9.d ne sont pas celles de V0 (prescription et interprétation au lieu d’alternatives et de 2e intention) ; le contenu des alternatives est en 9.f.
- **Q10.1 = 1.** Des embranchements existent. Ils ne commencent pas par les rangs E.
- **Q11.2 = 2, Q11.6 = 2, Q11.7 = 2 ; Q11.5 = 0 ; les autres = 1.** But non chiffré pour le symptôme. Urgence résumée en une phrase (transfusion, hydrocortisone 100 mg IV), sans conduite minute par minute. La fiche médicament se termine par « Les doses sont à vérifier dans l’AIPS ». Sortie d’hospitalisation en une seule ligne groupée.
- **Q12.1 = 1.** Trois niveaux nommés, peu de substance suisse (sommeil, stress au travail, déconditionnement).
- **Q13.1 = 2.** Quatre à cinq phrases de points clés, les fenêtres portent le terme sans couper la syntaxe.
- **Q14.1 = 1.** Pièges utiles, et le texte dit qu’ils ne sont pas des questions officielles de l’examen fédéral.

### Phase B — écarts qui font varier le score

Le générateur recopie dans chaque DX le tableau de prévalence de la fatigue et le tableau Stadje. Le point 4 d’un DX n’est donc pas le différentiel de cette maladie. Tous les Q4 restent à 1, sauf l’Addison (3/4) : le texte lu distingue d’abord la crise, puis primaire et secondaire.

- **DX.1 (66,3 %).** Définition OMS chiffrée. mediX 2025 cité pour la ferritine. Pièges concrets (Maltofer® = fer ferrique, endoscopie chez l’homme). La fiche Ferinject® est en grande partie concordante avec l’AIPS lue ce jour (voir §4) mais classe l’infection aiguë en contre-indication. Q11.5 = 1, pas 2.
- **DX.2 (63,0 %).** Obsan 9,8 % et MonAM 30,3 % sont datés dans les sources (indicateurs consultés, pas recontrôlés ici). Critères CIM-10 pour un codage suisse qui bascule vers la CIM-11 : le burn-out est en CIM-11, l’épisode dépressif reste enseigné en CIM-10. Le texte le dit. Doses d’ISRS : le rapport d’auteurs du 24.10.2026 écrit qu’elles viennent de l’utilisateur et n’ont pas été revérifiées dans chaque information professionnelle.
- **DX.3 (59,8 %).** HypnoLaus (49,7 % / 23,4 %) est la bonne étude lausannoise, citée sur résumé. Critères AASM 2014 (source américaine) comme référence du diagnostic. Observance « ≥ 4 h / 70 % » : le propre texte dit que ce seuil est américain et absent de la LiMA. AD109 / FDA cité comme non autorisé en Suisse : le statut est honnête, la source de décision reste américaine. Fichier sous 150 ko.
- **DX.4 (62,0 %).** Cibles ETA 2013 lues dans le squelette (0,4–2,5 et 1–5). L’ATA 2014 (américaine) est co-référence des critères et des pièges. Conflit de seuil avec la Phase A.
- **DX.5 (57,6 %).** Fourre-tout EBV, CMV, VIH. Cohorte de Dubbo australienne, pas suisse. Le piège d’examen est maigre (point 14 à 1).
- **DX.6 (64,1 %).** Définition et critères ESC 2021 présents. Le rapport d’auteurs dit que les seuils de NT-proBNP selon l’âge (450 / 900 / 1 800) n’ont pas été relus dans le texte ESC. La fenêtre d’examen du SSP ne montre que le seuil aigu < 300 ng/L ; les points clés du DX disent < 125 ng/L en ambulatoire. Les deux seuils existent dans la littérature, mais ils ne sont pas tenus ensemble dans une même phrase d’interprétation.
- **DX.7 (60,9 %).** SKIPOGH 10,4 % annoncé dans le bloc 2. KDIGO comme référence internationale. Le squelette du point 11 n’a pas été assez lu pour un 2 en pharmacologie (finérénone, iSGLT2).
- **DX.8 (59,8 %).** Le rang repose sur « ≈ 2 600 / 100 000, à vérifier ». Stadje 0,6 % est le seul chiffre de probabilité chez le fatigué. Le rapport d’auteurs dit que la durée de perfusion du pembrolizumab n’a pas été relue dans l’information professionnelle de Keytruda®.
- **DX.9 (54,3 %).** Aucune prévalence suisse retrouvée par les auteurs (l’« OFSP 0,3–0,8 % » de l’original est retiré). Critères IOM 2015 et NICE 2021, pas une société suisse. POTS collé à l’EM/SFC. Naltrexone à faible dose hors indication, avec la réserve Younger 2014 (douleur chronique, pas EM/SFC) — cette réserve est honnête. Sel 10–12 g/j : non revu sur une source suisse dans cet audit. Fichier sous 150 ko. Q11 le plus bas (12/22).
- **DX.10 (66,3 %).** Crise : hydrocortisone 100 mg IV ou IM puis 200 mg/24 h et 1 L de NaCl 0,9 % la première heure. Concordant avec le texte Endocrine Society 2016 ouvert ce jour (100 mg puis 200 mg/24 h). La spécialité suisse (Solu-Cortef®, enregistrement ODDB 23533 vu en fiche publique) n’est pas nommée dans la phrase de crise. L’AIPS Solu-Cortef n’a pas été ouvert en entier ici : la dose de crise n’est donc pas déclarée « vérifiée AIPS ». La fenêtre Synacthène enseigne encore un pic < 500 nmol/L comme confirmation, alors que le point 14 dit de ne pas appliquer 500 à toutes les trousses. Un lecteur de la fenêtre apprend le mauvais seuil. Plenadren® : limitation SL décrite ; les auteurs écrivent que la posologie en maladie intercurrente reste à relire dans l’information professionnelle complète.

## 4. Faits critiques ouverts pendant cet audit

### Ferinject® — AIPS lue

Source ouverte le 25.10.2026 : information professionnelle allemande, `swissmedicinfo.ch`, `authNr=57851`. Le numéro est dans l’URL du cours ([S75]) ; il n’est pas répété comme numéro d’autorisation dans la phrase de dose.

Concordant avec la fiche du SSP : perfusion ≤ 20 mg/kg et ≤ 1 000 mg, maximum 1 000 mg par semaine, surveillance 30 minutes, contre-indication au 1er trimestre.

**Discordant — critique de contre-indication.** La colonne « Contre-indications » de la fiche dit « Infection aiguë, 1er trimestre de grossesse ». L’AIPS place l’infection ailleurs : « Bei akuten oder chronischen Infektionen, Asthma, Ekzemen oder atopischen Allergien sollte parenterales Eisen mit Vorsicht verabreicht werden » (mises en garde). Les contre-indications lues sont l’hypersensibilité, l’anémie non ferriprive, la surcharge en fer et le premier trimestre. Classer l’infection aiguë comme contre-indication est une erreur de catégorie AIPS.

L’AIPS distingue aussi l’injection (≤ 15 mg/kg) et la perfusion (≤ 20 mg/kg). La fiche ne dit que la perfusion. Omission, pas une dose fausse.

### Hydrocortisone de crise

Page Endocrine Society, guideline d’insuffisance surrénale primaire, ouverte le 25.10.2026 : 100 mg parentéral immédiat, puis 200 mg/24 h. Le cours DX.10 dit la même chose, plus 1 L de NaCl 0,9 % la première heure (non revu sur l’AIPS suisse dans cette session). Pas de spécialité ® ni de numéro Swissmedic dans la phrase.

### Ce qui n’a pas été rouvert

Obsan 9,8 %, HypnoLaus, Garmendia, Stadje, mediX intégral, Keytruda®, Zoloft®, Euthyrox®, Gutron®, Procoralan®, Kerendia®, Plenadren® en texte intégral. Le rapport d’auteurs du 24.10.2026 déclare lui-même plusieurs de ces doses « non revérifiées ». Cet audit ne les convertit pas en doses confirmées. [S1] PROFILES reste « non relu » dans le fichier.

### Fenêtres hors sujet

Bibliothèque d’examens collée dans chaque monographie. Occurrences dans le texte visible (exemples) :

| Terme hors du sujet de la fatigue | SSP `_a` | DX.2 | DX.6 | DX.10 |
|---|---:|---:|---:|---:|
| Freinage (dexaméthasone, Cushing) | 12 | 12 | 6 | 54 |
| Cushing | 5 | 7 | 2 | 20 |
| Critères de Duke (endocardite) | 1 | 1 | 7 | 1 |
| Triade de Whipple | 1 | 3 | 0 | 2 |
| JAK2 / Vaquez | 3 / 2 | 6 / 5 | 3 / 2 | 2 / 1 |

La fenêtre « cortisol » du SSP enseigne le freinage pour hypercortisolisme au milieu d’un cours sur la fatigue et l’Addison. Aucune image : l’interdit « pas d’image » est respecté. Le hors-sujet est textuel.

### Contradiction interne de seuil

Phase A, point 9.d : TSH « ≈ 0,4–4 mU/L ». DX.4, point 11 : « ≈ 0,4–2,5 mUI/L » avant 70 ans (ETA 2013). Les deux ne peuvent pas être la cible enseignée en même temps.

## 5. Corrections classées (extrait)

### Critique

1. **Ordre et gravité du bloc 2.** Emplacement : fichier `_b`, section « Bloc 2 ». Extrait : « Les dix diagnostics gardent l’ordre de l’original, du plus fréquent au plus rare chez le patient fatigué. » Le même tableau place l’anémie (2,8 % des fatigués ; 3 000/100 000 femmes réglées) avant la dépression (18,5 % ; 9 800/100 000). Aucun 🚩, aucun E. Addison en DX.10. Correction exigée : un seul dénominateur suisse ou, à défaut, le rang chez le patient fatigué (Stadje) avec les graves marqués E et placés en tête d’algorithme, sans changer leur rang de fréquence. Puis regeler la liste et réaligner les dix fichiers.
2. **Bande 150–200 ko de contenu utile, par entité.** Le SSP pèse 266,6 ko bruts et 105 ko sans fenêtres d’examen. DX.3 = 133,5 ko, DX.9 = 127,9 ko. Le poids « conforme » des autres DX est de la copie de fenêtres. Correction : rédiger le contenu propre jusqu’à la bande, retirer les fenêtres qui ne servent pas l’entité. Ne pas fusionner les DX pour faire du poids.
3. **Contre-indication Ferinject®.** Fiche médicament, colonne contre-indications : « Infection aiguë ». AIPS 57851 lue le 25.10.2026 : précaution, pas contre-indication. Correction : recopier la liste des contre-indications de l’AIPS, et la mise en garde infections à part, sans l’adoucir ni la durcir.

### Grave

- Fenêtre Synacthène : pic < 500 nmol/L présenté comme confirmation, contredit par le point 14 du DX.10 et par la révision du 24.10 (seuils de trousses récentes).
- TSH 0,4–4 (Phase A) contre 0,4–2,5 (DX.4).
- Libellés A/B non identiques (burn-out / épuisement ; POTS / tachycardie orthostatique).
- DX.5 et DX.9 fourre-tout.
- Sources « résumé consulté » ou « non relu » sous des chiffres de conduite (S1, S10, seuils NT-proBNP, doses d’ISRS, perfusion de pembrolizumab, Plenadren intercurrent).
- Références américaines comme critère (ATA 2014, AASM 2014, IOM 2015) là où une source suisse ou européenne existe ou doit être déclarée absente.
- Lignes > 3 000 caractères ; noms de fichiers V7.

### Moyen

- Point 8 du SSP occupé par les critères de l’EM/SFC.
- Lettres 9.a–d décalées par rapport à V0.
- Pas de `LISTE_DX_CANONIQUE.md`.
- Mention finale « doses à vérifier dans l’AIPS » : honnête, et elle interdit de traiter le fichier comme prescriptible.

## 6. Harnais

`python3 harnais/bracelet/bracelet_suggest.py` a été exécuté. Sortie réelle collée dans `harnais/PREUVE_EMBOITEMENT.txt` : Graphiti 1.3, Mem0 1.3, Chonkie 0.2. Le top-3 doctrinal (Chonkie 1.6, LLMLingua 1.3, GPTCache 1.3) **n’est pas sorti**. Preuve non verte. Écart : documents découpés en squelettes (usage réel de Chonkie) ; pas de réemploi du score 98,8 % ; `app_v2.html` non lu ; `pr.sh` non lancé. L’audit a continué parce que l’ordre de cette session est un rapport, pas une rédaction.

## 7. Conclusion

**Prêt-dépôt Drive Finaux : NON.**

Trois critiques, pas une de plus :

1. L’ordre DX.1–DX.10 n’est pas la prévalence décroissante annoncée, et aucun grave n’a de badge ni de rang E.
2. Aucune entité ne pèse 150–200 ko de contenu propre ; DX.3 et DX.9 sont sous 150 ko même en fichier brut ; le SSP dépasse 200 ko par empilement.
3. La fiche Ferinject® transforme une précaution AIPS (infection) en contre-indication, et le fichier dit encore de vérifier les doses avant de prescrire. La question finale est « non » sur la Phase A et sur chacun des dix DX.

Le 98,8 % V7 ne qualifie pas ce lot sous V0. Tous les scores de cette grille sont entre **54,3 %** et **66,3 %**.
