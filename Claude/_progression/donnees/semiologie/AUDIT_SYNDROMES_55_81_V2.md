# Audit médical V2 (vérification des corrections) — SY-55 à SY-81 (14.11.2026)

J'ai lu `CORRECTIONS_SYNDROMES_55_81.md`, puis les champs corrigés des 27 JSON (tous chargés par `json.load`). J'ai relu par URL refdata, dans le cache `aips_fiche.py`, chaque dose ajoutée et les deux passages contestés.

## Verdict : **audit-ok**

Les 7 Critiques et les 9 Graves sont corrigés. Je ne trouve pas d'erreur nouvelle. Deux points de mon premier audit étaient faux : le correcteur a raison sur les deux (voir ci-dessous).

## Points contestés : décision

| Point | Texte de l'AIPS relu (Haldol® n° 26891 ; Solu-MEDROL® n° 35112) | Décision |
|---|---|---|
| C6, Haldol dans le délire | Injection, « Traitement aigu du délire […] • 1 à 10 mg par voie intramusculaire. • […] paliers toutes les 2 à 4 heures […] maximum de 10 mg/jour ». Le schéma « 2 à 5 mg i.m., renouvelable toutes les heures » suit la rubrique « maladie de Huntington ». | **Le correcteur a raison.** Mon patch C6 était faux : je l'avais tiré d'un extrait tronqué. Seule la règle de la personne âgée tenait. Elle est appliquée : 0,5 mg au début, 5 mg/jour au maximum. Cela découle de la règle « moitié de la plus faible dose adulte » et « moitié de la dose adulte ». |
| M4, Solu-Medrol | La phrase « La dose ne devrait pas être inférieure à 0.5 mg/kg de poids corporel par 24 heures » existe, mais seulement dans le paragraphe « Enfants et adolescents ». Aucune dose propre à l'AHAI de l'adulte. | **Le correcteur a raison sur le fond** : mon patch était faux pour l'adulte. Il écrit que la phrase « ne figure pas » dans l'AIPS. C'est inexact (elle concerne la pédiatrie), mais cela reste sans effet sur la fiche. « Dose À vérifier » est juste. |

## Vérification des corrections (AIPS relue)

| # | Fiche | Contrôle | Résultat |
|---|---|---|---|
| C1 | SY-56 | Miacalcic n° 38605 : 5 à 10 U.I./kg dans 500 ml, ≥ 6 h/jour ou 2 à 4 injections i.v. lentes, réhydratation | Conforme |
| C2 | SY-63, SY-67 | Acidum folicum Streuli n° 36752 : 5 mg/jour, ≤ 15 mg/jour ; contre-indication de l'acide folique seul dans l'anémie pernicieuse | Conforme |
| C3 | SY-63 | Ferinject n° 57851 : schéma simplifié, dose unique ≤ 20 mg/kg et ≤ 1000 mg, ≤ 1000 mg/semaine | Conforme |
| C4 | SY-69 | Quilonorm retard n° 35960 : 4 comprimés (1800 mg), lithiémie 0,8 à 1,2 mmol/l, ECG préalable | Conforme |
| C5 | SY-70 | 5 mg i.m., toutes les heures, 15 mg/jour suffisants le plus souvent, maximum 20 mg/jour ; moitié des doses après 65 ans | Conforme |
| C6 | SY-71 | 1 à 10 mg i.m., maximum 10 mg/jour ; 0,5 mg au début, 5 mg/jour au maximum chez la patiente de 84 ans | Conforme |
| C7 | SY-73, SY-74 | Valium n° 28840 : 0,1 à 0,2 mg/kg i.v., toutes les 8 h, « agitation motrice » | Conforme |
| G1 | SY-80 | Adrenalin Sintetica n° 56551 (novembre 2024) : 500 µg i.m., toutes les 5 min ; demi-dose sous tricyclique ou bêtabloquant ; synthèse orale à 0,5 mg | Conforme |
| G2 | SY-72 | Diazépam i.v. dans le délirium tremens (Valium) | Conforme |
| G3 | SY-55 | Mise en garde GlucaGen citée mot pour mot ; glucose i.v. chez l'alcoolique | Conforme |
| G4 | SY-63 | Vitarubine n° 21672 : 1000 µg/semaine, puis 1000 µg/mois ; tous les deux jours si atteinte neurologique | Conforme |
| G5 | SY-64 | Beriplex n° 00665 (octobre 2022) : 25, 35 ou 50 U.I./kg selon l'INR, ≤ 5000 U.I. ; Praxbind n° 65804 (mars 2021) : 5 g ; Ondexxya n° 67759 (avril 2025) : 400 mg puis 4 mg/min pendant 120 min, ou 800 mg puis 8 mg/min | Conforme |
| G6 | SY-78 | Pénicilline Grünenthal n° 56271 : 1 à 5 MUI/jour en 4 à 6 doses ; injection lente au-delà de 2 MUI | Conforme |
| G7 | SY-62 | Kenacort-A 10 en intrafocal, 10 à 40 mg, intervalle ≥ 2 semaines | Conforme |
| G8 | SY-73 | Critères de Hunter complets | Conforme (source à relire, signalé) |
| G9 | SY-57 | 150 ml de NaCl 3 % en 20 min, ≤ 2 répétitions, +5 mmol/l ; seuils 10 puis 8 mmol/l marqués « à relire » | Conforme |
| M2 | SY-80 | Ventolin n° 37397 (janvier 2026) : « bronchospasmes aigus : 1 - 2 inhalations » | Conforme |
| L1 | SY-56 | Zometa : « > 12.0 mg/dl [3.0 mmol/l] » dans les indications, « ≥3.0 mmol/l » dans la posologie ; la contradiction de l'AIPS est réelle | Conforme |
| L5 | SY-67 | Image relue : un seul œil, sclérotique jaune, ni nez ni visage ; domaine public, crédit « Auteur inconnu, recadré » | Conforme |

M1, M3, M5, M6, M7, L2, L3, L4 et L6 sont aussi relus et conformes.

## Restes non bloquants (Léger)

| Fiche, champ | Extrait | Patch |
|---|---|---|
| SY-80 management[1] | « 6-12 ans 0,3 mg, 6 mois-6 ans 0,15 mg » | Ajouter en tête : « plus de 12 ans 0,5 mg » (AIPS Adrenalin Sintetica). |
| SY-56 étiologies | « T (tumoral bénin) » pour l'adénome parathyroïdien | Acceptable ; ne rien changer. |

Les points restés « À vérifier » sont légitimes : NaCl 3 %, cyproheptadine et physostigmine sont absents du corpus, et aucune AIPS ne donne le bolus de glucose ni les volumes de cristalloïdes.
