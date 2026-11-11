# Audit agressif V0 — LOT_008 — G8 Hypothermie

| Élément | Valeur |
|---|---|
| Date | 2026-10-25, 20:43 CET (Europe/Zurich) |
| Rôle | Auditeur pair, rapport seulement. Aucun HTML de lot rédigé. |
| Brief | PROMPT ULTIME V0, plus le complément de densité et d'AIPS du 25.10.2026 |
| Objets | Branche `lot/LOT_008` (PR 407, cinq HTML) et dossier Drive `1QxQccTA70DBwo3bJ0rpjkz5yg_AcgO2j` |
| Décision | **Prêt-dépôt : NON.** Question finale : **NON** pour les 11 entités. Aucune fusion. |

Un score structurel « 14 titres présents » ne vaut pas un score V0. Le pourcentage ci-dessous est la grille des 46 questions (2 / 1 / 0). Il ne rachète ni une omission de densité, ni une critique, ni une question finale « non ».

## Verdict et trois critiques

**Prêt-dépôt : NON.**

1. **Omission de densité (critique, les 11 entités).** Un diagnostic sans information manquante vise 150–200 Ko de contenu propre. Tout matériau actuel sous 150 Ko est une **omission**, classée critique. Le SSP pèse 123 649 octets. Le plus lourd des DX (DX.1) pèse 76 289 octets. Le plus léger (DX.5) pèse 21 288 octets. Zéro entité n'entre dans la bande. Ce n'est pas un lot « un peu court mais acceptable ».
2. **Pharmacologie (critique).** DX.8 enseigne une charge intraveineuse de lévothyroxine de 200 à 400 µg selon l'ATA, puis 1,6 µg/kg/j à 75 % par voie intraveineuse, alors que le corpus AIPS Medina du 2026-10-08 ne contient aucune spécialité injectable de lévothyroxine (seulement Euthyrox®, autorisation 54949, et Eltroxin®-LF, autorisation 29812, comprimés). La même monographie fait débuter l'hypothyroïdie sévère à 0,025 mg/j par voie orale. La Partie 4 cite le Compendium (information abrégée), et la grossesse y est renvoyée à « l'IPr » au lieu du texte AIPS.
3. **Liste et preuve (critique).** Aucun badge 🚩 et aucun rang E1, E2, E3. L'ordre annoncé n'est pas une prévalence décroissante sur une seule population. En Partie 3, le PMID 37191873 est attribué à des auteurs et à un titre qui ne sont pas ceux de l'article.

## Complément — méthode de production (écart)

La méthode attendue, à consigner comme écart avec le V0 révisé, est la suivante.

1. Densifier de façon exhaustive, jusqu'à dépasser largement 200 Ko par entité.
2. Raboter et reformuler.
3. Vérifier chaque ligne contre le V0.
4. Arriver dans la bande finale de 150–200 Ko par entité (SSP, puis chaque DX).

Le lot livré n'a pas suivi ce cycle. Les cinq HTML sont des coques V7 (titres 1 à 14, fenêtres, tableaux) restées sous le plancher. Les nommer « Appel A / Appel B V7 » ne les place pas au format Phase A / Phase B V0. Il n'y a pas de HTML unique consolidé : cinq fichiers distincts, ce point d'interdit est respecté. Le regroupement de plusieurs DX dans un fichier reste permis seulement si **chaque** entité, isolée, pèse 150–200 Ko. Ici, aucune ne l'atteint.

## Inventaire et poids par entité

Mesure : octets du bloc `<details open>` de la monographie, hors glossaire commun et hors section Sources. Seuil lu comme 150 000–200 000 octets. En Kio (1024), le constat est le même.

| Entité | Fichier | Octets | Ko (÷1000) | Bande | Décision densité |
|---|---|---:|---:|---|---|
| SSP (Bloc 1) | Appel A | 123 649 | 123,6 | sous 150 | Omission critique |
| DX.1 Hypothermie accidentelle primaire | Partie 1 | 76 289 | 76,3 | sous 150 | Omission critique |
| DX.2 Infection et sepsis avec hypothermie | Partie 1 | 57 092 | 57,1 | sous 150 | Omission critique |
| DX.3 Traumatisé, submersion et périopératoire | Partie 2 | 31 605 | 31,6 | sous 150 | Omission critique |
| DX.4 Intoxications (alcool et médicaments) | Partie 2 | 29 372 | 29,4 | sous 150 | Omission critique |
| DX.5 Hypoglycémie | Partie 2 | 21 288 | 21,3 | sous 150 | Omission critique |
| DX.6 AVC et atteintes neurologiques | Partie 3 | 41 303 | 41,3 | sous 150 | Omission critique |
| DX.7 Dénutrition et anorexie mentale | Partie 3 | 42 023 | 42,0 | sous 150 | Omission critique |
| DX.8 Hypothyroïdie sévère et coma myxœdémateux | Partie 4 | 45 116 | 45,1 | sous 150 | Omission critique |
| DX.9 Insuffisance cardiaque et autres défaillances | Partie 4 | 39 476 | 39,5 | sous 150 | Omission critique |
| DX.10 Insuffisance surrénalienne et hypopituitarisme | Partie 4 | 40 717 | 40,7 | sous 150 | Omission critique |

Fichiers GitHub (`origin/lot/LOT_008`, dossier `LOTS/LOT_008/`) :

| Fichier | Octets | SHA-256 |
|---|---:|---|
| `LOT_008_Appel_A_V7_Plan_et_Liste.html` | 140 530 | `c3b6885c4e16add4b435f98b49aaae09d90ec2257bbb59d2705e840bd332e72a` |
| `LOT_008_Appel_B_V7_Partie_1_DX.1_a_DX.2.html` | 150 075 | `83701902d1bd97d8c7cf11d84191f517c401d4f2e783f5042f2884d90682c437` |
| `LOT_008_Appel_B_V7_Partie_2_DX.3_a_DX.5.html` | 98 379 | `95d9db7b1f041ba25fe0026b7a99dd0564e2dae396c1410d6a5fc299c0d20ecb` |
| `LOT_008_Appel_B_V7_Partie_3_DX.6_a_DX.7.html` | 95 314 | `63d2abcf2474fe0895ab815c4c560940c79ade96ba0800ff175459fb4767ff47` |
| `LOT_008_Appel_B_V7_Partie_4_DX.8_a_DX.10.html` | 139 648 | `cfa7866e2108a31489dda70521ecaed3526ea5a39d5b2df81e51f2209053ed38` |

Drive Finaux, dossier `1QxQccTA70DBwo3bJ0rpjkz5yg_AcgO2j` : cinq HTML, tailles identiques (140 530, 150 075, 98 379, 95 314, 139 648). L'Appel A Drive (id `15pyOljNJXJdQz_i1BzdkN0BOLvw0cUuY`) a le même SHA-256 que le fichier GitHub. Les quatre autres ont la même taille ; leur SHA Drive n'a pas été recalculé. Le dépôt Drive du 2026-10-24 précède cet audit. Il ne vaut pas validation V0.

Technique commune : HTML5, `FIN_FICHIER` présent, aucun `title=`, tableaux enveloppés, aucun script ni image. Fenêtres « pointeur » (« fenêtre complète … à sa première mention plus haut ») : 99 dans le SSP, 45 dans DX.1, 28 dans DX.2. Le mot « hypoglycémie » est coupé par une fenêtre (« Hypo » + fenêtre « glycémie ») dans l'Appel A, vers les lignes 119-120 et dans le titre de DX.5.

Absent du dossier de lot : `DECISION_SEANCE.md`, `evidence/`, `LISTE_DX_CANONIQUE.md`, `CORRECTIONS_AUDIT.md`, `HELP.md`, `audits/`. La PR 407 indique qu'aucune relecture clinique n'a été faite dans cette passe.

## Liste Phase A ↔ Phase B, gravité

Mêmes dix intitulés, même ordre, mêmes numéros. Ce n'est pas l'inversion du type LOT_001 (un DX.1 remplacé par un autre diagnostic). L'écart de libellé DX.1 est réel : l'Appel A porte « (exposition au froid, immersion, avalanche) », le titre de la Partie 1 ne le reprend pas.

| N° | Appel A | Phase B | 🚩 | Rang E |
|---|---|---|---|---|
| DX.1 | Hypothermie accidentelle primaire (exposition au froid, immersion, avalanche) ≈ 44 % [S2] | Même nom, sans la parenthèse ; ≈ 44 % [S2] | aucun | aucun |
| DX.2 | Infection et sepsis avec hypothermie ≈ 10 à 32 % | Identique | aucun | aucun |
| DX.3 | Hypothermie du traumatisé, de la submersion et du périopératoire ≈ 14 % | Identique | aucun | aucun |
| DX.4 | Intoxications : alcool et médicaments (quétiapine, olanzapine, lithium, barbituriques…) ≈ 5 à 26 % | Identique | aucun | aucun |
| DX.5 | Hypoglycémie ≈ 5 à 11 % | Identique | aucun | aucun |
| DX.6 | AVC et atteintes neurologiques centrales ou médullaires ≈ 6 % | Identique | aucun | aucun |
| DX.7 | Dénutrition et anorexie mentale ≈ 4 % | Identique | aucun | aucun |
| DX.8 | Hypothyroïdie sévère et coma myxœdémateux ≈ 3 à 4 % | Identique ; la Partie 4 cite [S11], qui est bien Snijders dans ce fichier | aucun | aucun |
| DX.9 | Insuffisance cardiaque et autres défaillances d'organes ≈ 4 % | Identique, [S11] | aucun | aucun |
| DX.10 | Insuffisance surrénalienne et hypopituitarisme ≈ 1 % | Identique, [S11] | aucun | aucun |

L'algorithme de l'Appel A commence par l'arrêt circulatoire, puis la glycémie, puis le sepsis. Il ne nomme pas E1, E2, E3. Le sepsis, le coma myxœdémateux et l'insuffisance surrénalienne aiguë restent en fin de liste, sans badge.

### Pourquoi l'ordre n'est pas une prévalence décroissante

Source rouverte : Snijders, Roos, Keijsers, *Eur Geriatr Med* 2023;14:411-420, PMID 37191873, texte intégral PMC10261225, lu le 2026-10-25. Six cohortes, 2173 patients. Qualité jugée faible par les auteurs. Le critère d'inclusion de la revue est une température inférieure à 36,0 °C, alors que le lot définit l'hypothermie sous 35 °C.

Faits lus dans l'article, et usage qu'en fait le lot :

- Maladie aiguë : 49 à 51 % dans deux grandes cohortes. Le lot place pourtant en DX.1 l'hypothermie primaire à 44 %, chiffre d'**une seule** cohorte (Cassar, Malte, patients de plus de 16 ans hospitalisés). L'Appel B parle de « patients âgés » pour ces 44 % : la cohorte Cassar n'est pas restreinte aux 65 ans et plus.
- Takauji 2021, Japon, n = 1194, température ≤ 35 °C : traumatisme / submersion / détresse 164 (14 %), infection 116 (9,7 %), maladie cérébrovasculaire 72 (6,0 %), hypoglycémie 65 (5,4 %), dénutrition 52 (4,4 %), insuffisance cardiaque 45 (3,8 %), maladie endocrinienne 14 (1,2 %), alcool 57 (5 %), médicaments 25 (2 %).
- Le lot met l'infection (fourchette 10–32 %, le 32 % étant le sepsis de Cassar) **avant** le bloc traumatisme à 14 %. Sur la cohorte la plus grande, l'infection est à 9,7 %, donc **après** les 14 %. DX.9 imprime lui-même ce tableau japonais, qui contredit l'ordre canonique.
- DX.8 (3–4 %, Malte 3 % et États-Unis 4 % de 203) est classé avant DX.9 (45/1194 = 3,8 %). Les fourchettes se chevauchent ; l'ordre strict n'est pas tenu.
- DX.3, DX.4, DX.6, DX.9 et DX.10 collent des entités distinctes (traumatisme + submersion + périopératoire ; alcool + plusieurs médicaments ; AVC + moelle ; cœur + « autres défaillances » ; surrénale + hypophyse).

Citation fausse, Partie 3, source [S2], ligne 279 du HTML : « Snijders BMG, Roeleveld HG, Raijmann RCMA et al. Accidental hypothermia in older adults… PMID 37191873 ». Les auteurs réels sont Birgitta M. G. Snijders, Marvin J. Roos et Carolina J. P. W. Keijsers, et le titre réel est *Incidences of underlying causes of hypothermia in older patients in the emergency department*. Les effectifs 72/1194 et 52/1194 figurent bien dans l'article ; la référence bibliographique, elle, est fabriquée. Les pourcentages de DX.6 et DX.7 s'appuient sur cette ligne.

Darocha, Pasquier et al., *Nat Rev Dis Primers* 2026;12:43, PMID 42393082, DOI 10.1038/s41572-026-00717-7 : la notice existe (publiée le 2 juillet 2026). Elle a été ouverte. Elle ne répare pas l'ordre des DX.

## Scores — grille 14 points

Quarante-six questions, maximum 92. Barème : **2** exigence tenue dans le point ; **1** élément présent, incomplet, mal affecté, ou sourcé hors AIPS / hors population suisse ; **0** absent, faux ou dangereux. Le rédacteur du lot n'est pas le notateur. Aucun score d'une jauge V7 n'est repris : aucun pourcentage structurel n'était écrit dans les HTML.

Seuil de validation : ≥ 90 % (soit au moins 83/92), zéro critique, question finale « oui ». Le plus haut score ici est 63,0 %. Toutes les questions finales sont « non » : un candidat ne peut pas couvrir l'examen fédéral sur ces monographies ni prendre en charge le coma myxœdémateux ou la crise surrénalienne avec le seul texte livré, au calibre actuel et avec la charge intraveineuse américaine.

| Entité | Points | % | Zéros | Question finale | Décision |
|---|---:|---:|---:|---|---|
| SSP | 53/92 | 57,6 | 3 | non | Refusé |
| DX.1 | 58/92 | 63,0 | 1 | non | Refusé |
| DX.2 | 49/92 | 53,3 | 1 | non | Refusé |
| DX.3 | 41/92 | 44,6 | 5 | non | Refusé |
| DX.4 | 39/92 | 42,4 | 7 | non | Refusé |
| DX.5 | 41/92 | 44,6 | 8 | non | Refusé |
| DX.6 | 44/92 | 47,8 | 2 | non | Refusé |
| DX.7 | 47/92 | 51,1 | 0 | non | Refusé |
| DX.8 | 56/92 | 60,9 | 4 | non | Refusé |
| DX.9 | 46/92 | 50,0 | 4 | non | Refusé |
| DX.10 | 48/92 | 52,2 | 4 | non | Refusé |

DX.7 n'a aucun zéro sur les 46 questions : presque tout y est partiel (quarante-cinq « 1 »). Le refus vient du seuil, de la question finale, et de l'omission de densité (42 023 octets).

Zéros qui portent le refus clinique, au-delà du calibre :

- SSP : Q3.4 (pas de tableau lésion → exploration → thérapeutique au point 3), Q4.1 (les graves ne précèdent pas les fréquents), Q7.1 (pas de 7.1).
- DX.1 et DX.2 : Q7.1 absent.
- DX.5 : Q3.4 (tableau « mécanisme / conséquence / clinique », pas le tableau exigé), Q6.1 (pas de normal avant le pathologique), Q7.2 et Q7.4 (syndromes en une ligne), Q9.5, Q9.6, Q11.8.
- DX.6 : Q2.4 (chiffres accrochés à la citation fabriquée), Q11.5 (altéplase 0,9 mg/kg sans fiche AIPS dans le fichier).
- DX.8 : Q6.1, Q11.5 (charge ATA et contradiction avec 0,025 mg/j), Q11.8 (grossesse adoucie ; allaitement déclaré absent alors que l'AIPS en parle), Q11.10 (critères de sortie écrits « dérivés, à confirmer »).
- DX.9 : Q6.1, Q11.5 (furosémide via le Compendium), Q9.6, Q11.10.
- DX.10 : Q2.2, Q11.5, Q11.8, Q11.10.
- DX.3 et DX.4 : plusieurs zéros de forme (syndromes non éclatés, cas de figure, sortie, enjeux).

### Grille question par question

| Q | SSP | DX.1 | DX.2 | DX.3 | DX.4 | DX.5 | DX.6 | DX.7 | DX.8 | DX.9 | DX.10 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 1.1 | 2 | 2 | 2 | 1 | 1 | 2 | 1 | 1 | 1 | 1 | 1 |
| 1.2 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 2 | 1 | 1 |
| 1.3 | 2 | 2 | 1 | 1 | 1 | 2 | 1 | 1 | 2 | 1 | 1 |
| 2.1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| 2.2 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 0 |
| 2.3 | 1 | 1 | 1 | 0 | 0 | 0 | 1 | 1 | 1 | 1 | 1 |
| 2.4 | 1 | 1 | 1 | 1 | 1 | 1 | 0 | 1 | 1 | 1 | 1 |
| 3.1 | 2 | 2 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| 3.2 | 2 | 2 | 2 | 1 | 1 | 1 | 1 | 1 | 2 | 2 | 2 |
| 3.3 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 2 | 1 | 1 |
| 3.4 | 0 | 1 | 1 | 1 | 1 | 0 | 1 | 1 | 2 | 2 | 2 |
| 3.5 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 2 | 1 | 1 |
| 4.1 | 0 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 2 | 2 | 2 |
| 4.2 | 1 | 2 | 1 | 1 | 1 | 1 | 1 | 1 | 2 | 1 | 2 |
| 5.1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 2 | 1 | 1 |
| 5.2 | 2 | 2 | 2 | 1 | 1 | 1 | 1 | 2 | 1 | 1 | 2 |
| 6.1 | 2 | 2 | 1 | 1 | 0 | 0 | 1 | 1 | 0 | 0 | 1 |
| 6.2 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| 7.1 | 0 | 0 | 0 | 1 | 1 | 1 | 1 | 1 | 2 | 2 | 1 |
| 7.2 | 1 | 1 | 1 | 1 | 0 | 0 | 1 | 1 | 1 | 1 | 1 |
| 7.3 | 1 | 1 | 1 | 0 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| 7.4 | 1 | 1 | 1 | 0 | 0 | 0 | 1 | 1 | 1 | 1 | 1 |
| 7.5 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 2 | 1 | 1 |
| 8.1 | 2 | 2 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| 8.2 | 2 | 2 | 1 | 1 | 1 | 1 | 1 | 1 | 2 | 1 | 1 |
| 9.1 | 2 | 2 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| 9.2 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| 9.3 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| 9.4 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 2 | 1 | 1 |
| 9.5 | 1 | 1 | 1 | 1 | 0 | 0 | 1 | 1 | 1 | 1 | 1 |
| 9.6 | 1 | 1 | 1 | 0 | 1 | 0 | 1 | 1 | 1 | 0 | 1 |
| 10.1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| 11.1 | 2 | 2 | 2 | 1 | 1 | 2 | 1 | 1 | 1 | 1 | 1 |
| 11.2 | 1 | 2 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| 11.3 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| 11.4 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| 11.5 | 1 | 1 | 1 | 1 | 1 | 1 | 0 | 1 | 0 | 0 | 0 |
| 11.6 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| 11.7 | 1 | 1 | 1 | 1 | 0 | 1 | 1 | 1 | 1 | 1 | 1 |
| 11.8 | 1 | 1 | 1 | 1 | 1 | 0 | 1 | 1 | 0 | 1 | 0 |
| 11.9 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| 11.10 | 1 | 1 | 1 | 0 | 0 | 1 | 1 | 1 | 0 | 0 | 0 |
| 11.11 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| 12.1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| 13.1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| 14.1 | 1 | 2 | 1 | 1 | 1 | 1 | 1 | 1 | 2 | 1 | 2 |

## AIPS — corpus Medina lu

Accès : oui. Dépôt public `vialdjoukang-spec/Medina`, fichier `AipsDownload_20261008.zip` (1 437 690 octets, SHA-256 `9fd0c713e28cd0a9ff402d2f621b032e9086f2df150c63291ab721e6a06aaced`). Contenu : `AipsDownload_20261008.xml`, attribut `generatedOn="2026-10-08T00:30:27Z"`, 10 221 faisceaux, 5 389 SmPC. C'est un index (numéro d'autorisation, titulaire, URL HTML et PDF), pas le texte intégral collé dans le XML. Les SmPC français ont été ouverts sur `files.refdata.ch` à partir de cet index, le 2026-10-25.

Numéros cités par le lot et présents dans l'index : 23533 Solu-Cortef®, 56472 Adrénaline « Bichsel », 41060 Cordarone® solution injectable, 42423 Glucose 5 % et 10 % Fresenius, 10989 Benerva®, 60142 Piperacillin-Tazobactam Labatec®, 35960 Quilonorm® retard, 32920 Glucosum « Bichsel ». Leur présence dans l'index ne valide pas chaque dose écrite : seules les quatre fiches ci-dessous ont été lues en entier dans cet audit.

Constat sur les fiches lues :

- **Lévothyroxine.** Aucune spécialité injectable dans l'index (recherche thyrox / liothyronine). Eltroxin®-LF, SmPC français, autorisation 29812 : comprimés sécables à 0,05 mg et 0,1 mg. Pour les patients de plus de 50 ans, une cardiopathie ou une insuffisance thyroïdienne sévère, « la dose initiale ne sera que de 0,025 mg par jour ». Cette phrase orale du lot est conforme. La charge de 200 à 400 µg intraveineux n'est pas une dose AIPS. Grossesse, texte lu : « Le traitement par Eltroxine-LF ne doit pas être interrompu en cours de grossesse. » Allaitement, texte lu : la lévothyroxine ne se retrouve qu'en très faibles concentrations dans le lait, et il est peu probable que des doses physiologiques aient des effets néfastes sur le nourrisson. Le lot écrit que l'extrait AIPS « ne mentionne pas l'allaitement ». Cette phrase est fausse au regard de la fiche ouverte.
- **Solu-Cortef®, autorisation 23533.** Le SmPC dit que des doses initiales allant jusqu'à 100 mg s'administrent par voie intraveineuse en 30 secondes au minimum, puis à des intervalles de 2, 4 ou 6 heures, et que la posologie élevée ne dépasse en général pas 48 à 72 heures. Le lot en est proche, avec un flou (« toutes les 2 à 6 heures » au lieu de « 2, 4 ou 6 heures »). Grossesse, texte lu : Solu-Cortef ne doit pas être administré pendant la grossesse, en particulier les trois premiers mois, sauf nécessité absolue. Le lot renvoie à « selon l'IPr ». C'est un adoucissement.
- **Adrénaline « Bichsel », autorisation 56472.** Réanimation cardiopulmonaire, adultes : initialement 1 mg i.v. (10 ml de la solution à 0,1 mg/ml), à répéter toutes les 3 à 5 minutes. Enfants : 0,01 mg/kg i.v. Cette dose du lot, lorsqu'elle vise la réanimation, correspond au SmPC lu. Elle ne couvre pas l'interdiction CHUV des médicaments sous 30 °C, qui est un protocole local et non une phrase AIPS.

La Partie 4 reste en critique : ses sources [S1] à [S5] pointent vers `compendium.ch` (« information professionnelle abrégée »), pour Solu-Cortef, Florinef, Synacthène, Eltroxin et Lasix. Le corpus Medina était disponible et contient les SmPC. Les doses de Cordarone, glucose, thiamine, naloxone, pipéracilline-tazobactam et lithium n'ont pas été relues mot à mot dans cet audit ; leurs numéros d'autorisation, eux, sont dans l'index.

## Autres écarts (graves ou moyens)

- Deux dates du protocole CHUV : V2.0 dans l'Appel A, « 2020 » en Partie 3 [S3]. La version en vigueur n'est pas tranchée ici.
- DX.5 donne une conduite HUG utile (15 g de glucides, glucose 40 % si trouble de conscience) mais la monographie fait 21 Ko : l'omission reste critique.
- L'Appel A place « au plus 1,5 à 6,0 g de glucose par kilo et par jour » comme dose AIPS du glucose 10 %. C'est un plafond de perfusion, pas le bolus de l'hypoglycémie. La fiche 42423 n'a pas été relue ici ; le risque de confusion est signalé, pas confirmé comme contresens d'extrait.
- HAS 2010 pour l'anorexie en Partie 3 : source européenne ancienne, à confronter à la version la plus récente et au protocole HUG déjà cité.
- Fenêtres qui coupent la phrase porteuse, en particulier autour de la lévothyroxine et de l'hydrocortisone en DX.8.

## HELP (lacunes, sans invention)

1. LOT_008, DX.8, point 11. Quelle spécialité suisse de lévothyroxine, si elle existe hors du corpus du 2026-10-08, autorise une voie injectable, avec dose AIPS et numéro d'autorisation lu sur la fiche, pas sur une URL ? Déjà cherché : index Medina `AipsDownload_20261008.xml`, 2026-10-25. Cible : remplacer la charge ATA.
2. LOT_008, Bloc 2. Quelle série suisse (OFS, registre, centre) donne la part de chaque cause parmi les hypothermies définies par une température centrale inférieure à 35 °C ? Déjà cherché : Snijders 2023, qui mélange un seuil à 36 °C et des cohortes étrangères. Cible : réordonner DX.1 à DX.10.
3. LOT_008, DX.8 et DX.10, point 11.8. Coller le paragraphe grossesse et allaitement du SmPC Solu-Cortef (23533) et d'Eltroxin-LF (29812), sans formule « selon l'IPr ».

## Ce qui a été fait, et ce qui ne l'a pas été

Fait : lecture du brief V0 ; bracelet exécuté (sortie réelle dans `PREUVE_EMBOITEMENT.txt`) ; cinq HTML extraits de `origin/lot/LOT_008` ; tailles et SHA-256 ; découpage par monographie ; Appel A Drive retéléchargé et comparé (SHA identique) ; Snijders 2023 et Darocha 2026 ouverts ; zip Medina lu ; quatre SmPC français ouverts.

Non fait : relecture de chaque SmPC cité ; rehash des quatre HTML Drive autres que l'Appel A ; dépôt ou déplacement Drive ; fusion ; contact de l'owner. Les pages AIPS n'ont pas été ouvertes sur swissmedicinfo.ch : elles l'ont été via les URL du corpus refdata du zip Medina.

Contenu établi à partir des fichiers du lot et des sources ouvertes pendant cet audit. Non validé cliniquement par un médecin.

## Automates actifs

Ce rapport ne modifie aucun workflow. Automates présents sur `main` au moment de l'audit : `appel-vial.yml`, `auto-fusion.yml`, `checkpoint.yml`, `ci.yml`, `codex-cloud-120.yml`, `file-fusion.yml`, `garde-progres.yml`, `harnais-5min.yml`, `liens-hebdo.yml`, `pages-apres-fusion.yml`, `pages.yml`, `prevalences-recherche.yml`, `veille-ve1.yml`, `veille-ve2.yml`, `visuel.yml`.
