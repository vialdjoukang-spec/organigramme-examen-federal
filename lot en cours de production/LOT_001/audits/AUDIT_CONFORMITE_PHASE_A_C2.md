# Audit de conformité et de langue — LOT_001 Phase A (cycle C2)

Fichier : LOT_001_Phase_A_V0.html — 186 209 octets (bande 100–200 Ko respectée) — SHA-256 3180b291f2a40efdcc7867771e96275c9c18a8863c89ab20dfbd0b2274c5c054
Outils : `controle_lot.py verifier` et `extraire --points 1,5,6,7,10,13,14` ; `aips_texte.py` (52433, 55057, 31489, 69243, 70200, 32920) ; rendu Chromium 390 px ; contrôles par script (balises, abréviations, répétitions). Rapports C1 lus seulement pour vérifier les corrections ; note refaite à neuf, aucun score reporté.

## 1. Contrôles de structure et de technique

| Contrôle | Résultat |
|---|---|
| 14 points présents, titres et ordre conformes à §11 | Oui |
| Taille 100–200 Ko (§14) | Oui (186 209 o) |
| `verifier` sur le fichier Phase A | 0 critique, 0 avertissement. La seule critique du lot (« DX présents [1,2,3,4,5,7,8] ; attendus 1 à 10 ») concerne l'avancement de la Phase B, pas la Phase A. |
| Balises équilibrées, FIN_FICHIER, aucun `title=`, aucun script/image/lien externe, ligne max 1 708 car., 27 tableaux sur 27 enveloppés (`.tw`) | Oui |
| 390 px sans défilement horizontal (Chromium : scrollWidth 390 = clientWidth 390) | Oui (vérifié par exécution, contrairement à la mention de la section Sources, devenue inexacte et à retirer) |
| Liste DX.1–DX.10 du fichier = `LISTE_DX_CANONIQUE.md` (noms, ordre, numéros) | Oui, 10/10 ; titres Phase B existants (DX.1, 2, 3, 4, 5, 7, 8) identiques aux noms canoniques |
| Phrase coupée par une fenêtre dans les points 1, 5, 6, 7, 13 | Aucune constatée |
| Doses AIPS citées dans les points 13–14 (BOTOX 50 U/aisselle, 16 sem., CI infection du site ; Dysport 100 U, 12 sem. ; GlucaGen 0,5 mg < 25 kg, CI phéochromocytome ; Axhidrox grossesse et adulte ; glucose 20 % 40 mL = 8 g) | Conformes au texte AIPS relu le 26.10.2026 |

## 2. Corrections C1 : vérification

| Correction C1 | État C2 |
|---|---|
| P6 tableau (Peau, Pouls, Ganglions) : phrases verbales | Faite |
| P10 : nœuds 0–11 finissant par un verbe | Faite |
| P7 : colonne Mécanisme verbale ; gestes pour Fatigue, Baisse d'appétit, Thermophobie | Faite |
| P1 : « Terme à éviter » en phrases verbales | Faite pour cette colonne ; les colonnes 2 et 3 restent nominales (voir 4) |
| Abréviations SSED, SSML, IP, CEP développées | Faite (CG055 reste un code de formulaire, non développé) |
| « Piège : … » remplacé par « Le piège consiste à… » | Faite, mais la formule se répète 13 fois dans le fichier (voir 4) |
| « n'exclut pas » (≥ 10 occurrences) | Réduite à 8 variantes ; acceptable |

## 3. Score §12.2 (points 1, 5, 6, 7, 10, 13, 14 ; 2 critères par point, maximum 28)

| Point | Contenu au bon point | Forme (verbes, fenêtres, abréviations) | Score |
|---|---|---|---|
| 1 | 2 | 1 | 3/4 |
| 5 | 1 | 2 | 3/4 |
| 6 | 1 | 2 | 3/4 |
| 7 | 1 | 2 | 3/4 |
| 10 | 2 | 2 | 4/4 |
| 13 | 2 | 2 | 4/4 |
| 14 | 1 | 2 | 3/4 |
| **Total** | | | **23/28 = 82,1 %** |

Motifs des « 1 » : P1 forme (cellules nominales) ; P5 contenu (questions clés absentes) ; P6 contenu (pression artérielle sans valeur normale ni seuil) ; P7 contenu (gestes absents pour plusieurs signes) ; P14 contenu (réponse contradictoire et affirmation non sourcée). Les points 2, 3, 4, 8, 9, 11, 12 ne sont pas notés ici.

## 4. Corrections

| Classe | Emplacement | Extrait | Correction | Source |
|---|---|---|---|---|
| Moyen | P6, tableau, ligne Pression artérielle | Normal attendu : « Le médecin standardise la mesure selon la Société suisse d'hypertension. » ; pathologique : « Une pression normale entre les accès laisse ouverte l'hypothèse d'un PPGL. » | La colonne « Normal attendu » ne donne aucune valeur et la colonne pathologique aucun seuil (Q6.1, Q6.2). Écrire la valeur normale et le seuil d'hypertension de S79, puis déplacer la phrase sur l'organisation de la mesure en colonne « Geste ». | S79 (Société suisse d'hypertension) |
| Moyen | P14, question « Un début après 25 ans exclut-il une forme primaire ? » | « Non, il la rend seulement moins probable. » contre P8 : « un début après 25 ans rendent une forme secondaire probable » | Les deux points se contredisent. Aligner P14 sur S114 (critère « début avant 25 ans » parmi 7, 4 requis) et corriger la faute d'accord de P8 (« rend »). | S114 |
| Moyen | P14, question sur les expectorations | « Le guide a remplacé l'ancienne règle des trois expectorations. » | Aucun point 1–13 ni l'INDEX (S18 : « 2 expectorations à 1 h d'intervalle ») ne mentionne une règle antérieure. Retirer la phrase ou la sourcer par un extrait daté. | S18 |
| Moyen | P5, tableau des questions | Intro : « le début, l'étendue, la symétrie, les déclencheurs, le sommeil, le retentissement » | Aucune ligne pour les déclencheurs (chaleur, émotion, repas), l'anamnèse familiale (critère suisse de S114), les comorbidités (diabète, thyroïde) ni l'alcool et la caféine. Ajouter ces questions avec raison et conséquence. | S114, S3 |
| Moyen | P7, fenêtres « Faim, nausée, trouble visuel, céphalée » et « Dyspnée » ; tableau 7.2 | « sa chaîne causale propre reste non documentée » ; « Les gestes de recherche figurent au point 6. » ; « mesure la pression aux deux bras » | §11 exige un geste de recherche et un mécanisme pour chaque signe. Ajouter la question ou la manœuvre (échelle de la faim, questionnaire visuel, dyspnée à l'effort) ; décrire le geste de « pression aux deux bras », « peau chaude et moite » et « tachycardie de repos » au lieu de renvoyer au point 6. | S59, S73–S75 |
| Moyen | P1, tableau, colonnes 2 et 3 | « Une sudation focale, bilatérale, idiopathique et gênante (DDG 2023). » ; « Un accès de chaleur avec rougeur et sueur lié à la transition ménopausique. » ; « Une élévation régulée de la consigne thermique. » | Phrases nominales (§14.4-1, tableaux inclus). Écrire « L'hyperhidrose focale primaire désigne une sudation… ». | S3 |
| Moyen | Sources hors liste de Vial dans les points relus | S59 (uhmeded.uhcw.nhs.uk), S60 (nhs.uk), S28 (covwarkformulary.nhs.uk), S75 (uclh.nhs.uk), S91 (bloodcancer.org.uk), S36/S46/S62/S80/S90/S92 (archives.uness.fr), S96/S63 (cep.splf.fr), S49/S104 (urofrance.org), S66 (firendo.fr), S68 (lymphome.ch), S55 (chuv.ch), S78 (erasme.be) | Les gestes du point 6 reposent surtout sur des supports britanniques et français ; la hiérarchie Suisse → Europe → international (§13.1) n'est pas respectée et ces domaines ne figurent pas dans `SOURCES_AUTORISEES.md`. Chercher un support suisse (HUG, RMS, Unisanté) ou déclarer le recours comme choix de repli ; remplacer S91 (association de patients) par une source médicale pour la définition de la fatigue (§14.4-7). | SOURCES_AUTORISEES.md §1–10 |
| Moyen | P10, nœud 3 | « (cadre HUG ou ESC nommé) » | Méta-commentaire sans contenu. Nommer le document (HUG_000001139 ; ESC 2023). | S89, S93 |
| Léger | P1, P7 | « Le piège consiste à… » (3 occurrences dans chacun ; 13 dans le fichier) ; P14 : « Non, elle ne l'exclut pas. » répété | Zéro répétition : varier les formulations. | |
| Léger | P1, P6, P7, P10, P14 | Légendes : « Normal attendu, geste et signe pathologique, région par région » ; « Huit syndromes éclatés en signes fonctionnels… » ; « Si X → Y : branches ordonnées… » ; « Question d'examen → bonne réponse → raison » ; « Fenêtres de technique et de valeur : » | Légendes nominales : leur donner un verbe conjugué. | |
| Léger | P5, colonne 3 | « Il fait rechercher immédiatement une cause cardiaque. » ; « Il propose un test adapté… » | Le pronom « Il » ouvre la cellule sans antécédent ; écrire « Le médecin ». | |
| Léger | P6, tableau Thorax | « B1 et B2 s'entendent » | B1 et B2 (bruits du cœur) ne sont développés que dans la fenêtre suivante ; « DX » n'est jamais développé (diagnostic différentiel numéroté). | |
| Léger | P6, fenêtres Pâleur et Tirage | « La pâleur à deux sites motive l'hémogramme sans compter deux preuves. » ; « Trente mouvements par minute avec tirage font deux constatations, sans nommer la cause. » | Phrases obscures : réécrire la décision clinique voulue. | |
| Léger | HELP | « donnée non trouvée » (P1 chromhidrose, P5 âge de début, P7 nausée et appétit) | §13.3-6 exige une question HELP pour chaque donnée introuvable ; HELP.md ne contient que Q4–Q6. | |
| Léger | Section Sources | « L'affichage à 390 px n'a pas été vérifié par exécution » | Mention devenue fausse (rendu 390 px sans débordement constaté). | |

Aucune correction Critique dans les points relus. Aucune erreur de dose AIPS constatée dans les points 13–14.

## 5. Liste DX

| Contrôle | Résultat |
|---|---|
| Noms, numéros, ordre = liste canonique | Oui (10/10) |
| Rang E, 🚩 et fréquence de chaque DD | Conformes à la liste canonique |
| Légende du tableau | Léger : « Liste DX.4 → DX.10 (noms exacts de la liste canonique) » alors que le tableau contient DX.1 à DX.10 ; écrire « DX.1 → DX.10 ». |
| Critère d'ordre (§9.1-1 : classement par fréquence décroissante) | Grave, en attente de décision : DX.1–DX.3 passent avant DX.4 (2–4 %, fréquence supérieure). Le critère est écrit en tête du Bloc 2 et les graves restent visibles, mais l'écart avec §9.1 n'est pas tranché (HELP Q6). La liste ne doit pas être gelée avant la décision de Vial. |
| Cohérence A↔B | Titres de 7 fichiers Phase B identiques ; DX.6, DX.9 et DX.10 absents (travail en cours, pas un écart). |

## 6. Décision

Score 82,1 % < 90 %. Critique : 0. Refus selon §12.2 : retour au rédacteur avec les lignes à 1 du tableau 3 et les corrections Moyen du tableau 4.

**Question finale (« Vial peut-il gagner 90–100 % des points et traiter ce patient en sécurité ? ») : NON** pour l'instant : les points 5, 6, 7 et 14 laissent des questions clés, des valeurs normales et des gestes manquants, et le point 14 contient une contradiction avec le point 8.
