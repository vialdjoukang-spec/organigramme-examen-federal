# Contre-audit des textes : PE_MS.json (IMG-238 à IMG-288), V2, 14.11.2026

Auditeur indépendant. J'ai appliqué les skills `medecin-expert` et `expert-web`.

**Ce que j'ai fait**
- J'ai lu CORRECTIONS_TEXTE_PE_MS.md.
- J'ai relu dans PE_MS.json le traitement, les sources et le gold des 21 entrées modifiées. Le JSON est valide.
- J'ai comparé chaque dose aux extraits AIPS lus par URL au tour 1 (cache `aips_fiche.py`) : Rocephin, Ciproxine, Doxycyclin-Mepha, Flagyl, Cyklokapron, Tranexam Labatec, Visanne, Femara, Glucophage, Rhophylac, Cytotec, Methotrexat Accord, Xarelto, Eliquis, Remicade, Kenacort-A, Genotropin, Lucrin Dépôt, Eligard, Xtandi, Co-Amoxicillin Zentiva et Floxapen.
- J'ai contrôlé par script les 51 entrées : étiquettes, ordre des sources, sources fantômes, sources américaines, mentions « À vérifier ».

## 1. État des défauts V1

| Id | État |
|---|---|
| C2–C14 | **Corrigés.** Les doses, voies, rythmes et contre-indications sont conformes aux AIPS. L'interdiction Femara n'est plus adoucie : « CONTRE-INDIQUE … préménopausal et pendant la grossesse ». Rhophylac cite « grossesse ectopique » et « avortement spontané », 300 µg en 72 h. Xarelto est contre-indiqué, Eliquis « non recommandé ». Remicade : 5 mg/kg aux semaines 0, 2 et 6, puis toutes les 8 semaines. Kenacort-A : 10–40 mg en intrafocal, 20 mg en intra-articulaire pour l'épaule. Lucrin : 0,3 mg/kg, au moins 7,5 mg. |
| C1 (244) | La dose AIPS de 0,25 g est exacte, mais le choix crée une erreur nouvelle (R1 ci-dessous). |
| M1 | **Corrigé.** Doxycyclin-Mepha est datée de février 2024. Flagyl, de septembre 2025, remplace Metronidazole Sintetica (perfusion i.v.). |
| M2 | **Corrigé.** La définition OMS/FIGO/ICM 2025 est appliquée et la source OMS est placée en dernier. SGGG EB 26 (2012) est citée. |
| M3 | **Corrigé.** SGGG EB 80 (100–150 mg, avant 16+0 SA), EB 56 et EB 66 sont citées. « Hors indication » remplace « hors posologie ». |
| M4 | **Corrigé.** Aucune source fantôme ne reste (vérifié par script). |
| M5 | **Corrigé selon l'alternative prévue.** Les sources sont étiquetées « (source américaine, non vérifié CH) ». En 252, 267 et 288, la seule source reste américaine : je classe ce point en mineur résiduel (R5). |
| M6 | **Corrigé.** Le script ne trouve plus aucune source non étiquetée. Deux erreurs d'ordre restent (R4). |
| M7 | **Corrigé.** ESGO-ESTRO-ESP 2025 (Lancet Oncol 2025;26(8):e423) et ISUOG 2023 (Bilardo) sont citées. |
| Mineurs V1 | **Corrigés** : 261, 263, 280 et les puces `pourquoi_pas_gold`, désormais verbales. |

**Les 15 « À vérifier » restants sont honnêtes.** Ils portent sur l'oxytocine injectable et la colchicine (absentes du corpus), sur les chimiothérapies (238, 245, 251), sur les biothérapies de la PR (280), sur des seuils ou durées sans source lue (248, 249, 253, 258, 276), sur la date SGUM (260) et sur trois versions de sources (263, 265).

## 2. Défauts restants

| Gravité | Id · champ | Extrait actuel | PATCH exact | Preuve |
|---|---|---|---|---|
| **Majeur** R1 (nouveau) | 244 traitement[0] | « ceftriaxone 0,25 g i.m. dose unique (AIPS Rocephin®, « blennorragie » ; IUSTI 2024 : 1 g i.m., écart signalé) » | « ceftriaxone 1 g i.m. dose unique (source européenne : IUSTI 2024 ; dans la posologie générale de l'AIPS Rocephin®, 1–2 g/j ; la ligne « blennorragie » de l'AIPS indique 0,25 g, dose dépassée par la résistance du gonocoque : écart signalé) » | L'AIPS lue indique « En général, 1 - 2 g … une fois par jour » et « Blennorragie … 0,25 g ». Une dose de 0,25 g expose à l'échec thérapeutique. Elle contredit aussi 253, qui donne 1 g pour la même cible. |
| Mineur R2 | 238 autres[1].pourquoi_pas_gold | « (non standard en Suisse) » | Remplacer par « elle ne remplace pas encore la résection de stadification (EAU 2025) ». | La mention « À vérifier » a été retirée sans source : l'affirmation n'est plus étayée. |
| Mineur R3 | Sources 250, 263, 264, 269, 270, 285 | « (Swissmedic n° …, lue par l'audit) » | Donner les dates AIPS lues : Lucrin Dépôt « mai 2025 », Xarelto « mai 2025 », Tranexam Labatec « juillet 2026 », Kenacort-A « décembre 2021 ». | Rubrique « Mise à jour » des AIPS |
| Mineur R4 | Ordre des sources 255 et 265 | 255 : Teede (internationale) avant Rotterdam (européenne). 265 : Parks (article) avant ECCO et ESGAR. | 255 : placer Rotterdam avant Teede. 265 : placer Parks en dernier. | Règle Suisse → Europe → autres |
| Mineur R5 | 252, 267, 288 sources | Une seule source, américaine | Ajouter une source européenne lue quand elle est trouvée. Sinon, le champ peut rester tel quel. | Étiquette déjà présente |
| Mineur R6 | 264 traitement[1] | « affections d'origine obstétricale » | Citer mot pour mot : « affections d'origines obstétricales ». | AIPS Tranexam Labatec 69390 |
| Mineur R7 | 244 autres | Le tableau `autres` est vide depuis le retrait du doublon. | Rien à faire si le gabarit accepte un tableau vide. Sinon, ajouter « IRM scrotale, rang 2 : abcès ou masse équivoque ». | Schéma |

## 3. Verdict

**corrections requises.** Il reste 1 majeur (R1, une ligne) et 6 mineurs. Aucune critique ne reste. Hors R1, aucune dose, contre-indication ou date fausse n'a été introduite. Après application de R1 mot pour mot, PE_MS (texte) peut recevoir « audit-ok » sans nouveau tour. Les mineurs R2 à R7 peuvent être appliqués dans le même commit.
