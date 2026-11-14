# Audit médical agressif — Syndromes SY-28 à SY-54 (14.11.2026)

Objet : `syndromes/SY-28.json` à `SY-54.json`, lus en entier (≈ 190 Ko).

Méthode :
- **AIPS.** 33 AIPS ouvertes par URL refdata (`aips_fiche.py fiche`). Les citations des drapeaux rouges et du management ont été comparées au texte en cache, espaces et apostrophes normalisés : toutes sont retrouvées. Les 5 écarts du script tiennent à des espaces insérés par refdata (« 0 , 05 mg », « pend ant ») et ont été vérifiés à l'œil.
- **Corpus.** `trouve` a été lancé sur chaque molécule dite « absente » ou « non lue ».
- **Images.** 7 images lues (Read).
- **Source HUG.** Un contrôle ponctuel a porté sur la stratégie « Asthme » 2026, consultée par recherche web (PDF hug.ch). Il confirme salbutamol 2,5 mg toutes les 20 min, prednisone 50 mg × 5 j, SpO2 93–95 % et la coquille « 2 mg » de magnésium.
- **Renvois.** Tous les renvois S-xx et SY-xx existent.

## Verdict : **corrections requises**. 9 critiques, 3 graves. Question finale : **non**.

## Score (grille 2/1/0)

| Axe | Pts | Raison |
|---|---|---|
| Définition, symptômes, physiopathologie, étiologies, différentiels, phrases verbales | 2 × 6 | Justes et verbales ; VITE DIT CAFé bien tenu |
| Signes et valeurs | 2 | Peu de chiffres, tous sourcés (HUG, RMS) ou omis |
| Drapeaux rouges et urgences | 1 | Hyperkaliémie, seuil de K⁺ de l'acidocétose et cibles d'O2 non chiffrés (G1–G3) |
| Examens clés | 2 | Adaptés ; seuils de la PBS et de la protéinurie « À vérifier » |
| Management et doses AIPS | 0 | 9 critiques |
| Écarts AIPS/reco et hors AIPS signalés | 2 | Bien signalés (tamsulosine, MTX, IPP, terlipressine, Mg) |
| Synthèse orale CS | 2 | Claire et adaptée |
| Sources | 1 | HUG et RMS réellement lus ou résumés ; dates AIPS fausses (M1) |
| Images | 1 | Pertinentes ; visages partiellement identifiables (L2) |
| **Total** | **25/28 = 89,3 %** | Refusé (critiques présentes) |

## Critiques — PATCH exact

| # | Emplacement | Extrait | PATCH | Source lue |
|---|---|---|---|---|
| C1 | SY-54 management[2] | « hors AIPS pour l'insuline humaine Actrapid HM … décrit seulement la voie sous-cutanée … absente du corpus refdata » | Deux affirmations fausses : l'AIPS figure au corpus (n° 44610) et autorise la voie IV. Écrire : « Actrapid HM : « son administration se fait par voie sous-cutanée ou intraveineuse » ; « Seul Actrapid HM (solution d'insuline) peut être administré par voie intraveineuse » ; perfusion stable « entre 0,05 UI/ml à 1,0 UI/ml » dans NaCl 0,9 % (AIPS Insulines Humaines HM Novo Nordisk n° 44610, avril 2026) ; débit selon le protocole hospitalier. » | AIPS lue |
| C2 | SY-47 management[4] | « l'AIPS d'Aspirin Cardio est absente du corpus refdata consulté : dose À vérifier » | « Aspirine en prévention de la pré-éclampsie : hors AIPS (indications cardiovasculaires seulement ; AIPS Aspirine® Cardio n° 51795, mars 2026) ; dose selon le SGGG Expertenbrief n° 80 (à lire) ». | AIPS lue |
| C3 | SY-47 management[1] | « dose maximale de ce schéma À vérifier » | « … on peut ensuite doubler cette dose toutes les 30 minutes jusqu'à l'obtention d'une baisse tensionnelle suffisante ou jusqu'à une dose de 160 mg/h » (AIPS Trandate® n° 41529, mars 2026). Ajouter la contre-indication : « Antécédents d'asthme bronchique ou de bronchopneumopathie obstructive ». | AIPS lue |
| C4 | SY-45 management[0] | « TMP/SMX 160/800 mg 2×/j 7 jours (AIPS de TMP/SMX non lue, À vérifier) » | « co-trimoxazole (indication « pyélonéphrite ») : « Posologie habituelle » 1 comprimé de Bactrim forte matin et soir, « à intervalles de 12 heures » (AIPS Bactrim forte n° 48306, mars 2023) ». | AIPS lue |
| C5 | SY-53 management[2] | « la dose d'hydrocortisone orale est absente du corpus (Hydrocortone, À vérifier ; RMS 2017 cite 15–25 mg/j) » | « hydrocortisone orale : « Insuffisance surrénale chronique : 10 à 20 mg par jour, parfois davantage, avec 4 à 6 g de chlorure de sodium ou un minéralocorticoïde » (AIPS Hydrocortisone Galepharm n° 57970, août 2025) ; la RMS 2017 cite 15–25 mg/j ». | AIPS lue |
| C6 | SY-32 management[2] | « forme orale, la forme IV n'a pas été lue : À vérifier » | « métronidazole IV : « Dose initiale de 15 mg … par kg de poids corporel », puis « 7,5 mg … par kg de poids corporel toutes les 6 heures pendant 3 jours, puis toutes les 12 heures » ; indication : péritonite (AIPS Metronidazol i.v. B. Braun n° 48018, février 2026) ». | AIPS lue |
| C7 | SY-36 management[0] | « dose orale non lue, À vérifier » | « Lasix comprimés (40 mg) : « En général, le traitement débute chez les adultes par ½ à 1 à 2 comprimés/jour ; dose d'entretien : ½ à 1 comprimé/jour » (AIPS Lasix® comprimés n° 30629, mai 2025) ». | AIPS lue |
| C8 | SY-29 management[4] et SY-47 management[2] | « Sulfate de magnésium Bichsel n° 56394, absente du corpus refdata » | Affirmation fausse : l'AIPS figure au corpus (refdata 31.07.2026, mise à jour octobre 2025). Le texte cité est exact. Corriger la mention et la date. | `trouve` |
| C9 | SY-28 management[4], SY-48 management[0] | « antalgie (molécule et dose À vérifier : AIPS non lue) » | Nommer une molécule et citer sa dose AIPS (par exemple, morphine IV : « injecter lentement 2 – 10 mg », AIPS Morphini HCl Streuli n° 56554), ou écrire « antalgie IV selon le protocole » sans « AIPS non lue ». | Règle §23 |

## Graves (urgences)

| # | Emplacement | Défaut | PATCH |
|---|---|---|---|
| G1 | SY-42 management[0] | L'hyperkaliémie menaçante est renvoyée au « protocole de l'établissement ; AIPS non lues ». C'est une urgence CS. | Nommer le gluconate de calcium IV, l'insuline rapide avec glucose et le salbutamol nébulisé, chacun avec sa dose AIPS (Actrapid HM n° 44610 et Ventolin n° 37397 déjà lues), et préciser le seuil d'ECG. |
| G2 | SY-54 drapeaux[1], management[1] | Le seuil de potassium sous lequel l'insuline est différée et le volume de NaCl 0,9 % restent « À vérifier ». | Lire RMS 2019 (déjà citée) et écrire le seuil de K⁺ et le débit initial de NaCl ; nommer le KCl (AIPS Kaliumchlorid B. Braun n° 29552). |
| G3 | SY-29, SY-30, SY-31 management[0] | La cible de SpO2 du BPCO hypercapnique reste « À vérifier » dans 3 fiches, alors que la stratégie HUG BPCO 2026 est déclarée « lue ». | Reprendre la cible de la stratégie HUG BPCO, ou écrire « non trouvée dans HUG BPCO 2026 ». |

## Moyens

| # | Emplacement | PATCH |
|---|---|---|
| M1 | Toutes les fiches (sources) | Les dates citées sont celles de la publication refdata, pas celles de la « Mise à jour de l'information ». Corriger : Ventolin janvier 2026 ; Inderal janvier 2023 ; Glypressine mars 2024 ; Sandostatine mars 2023 ; Néo-Mercazole août 2020 ; Eltroxine juin 2023 ; Solu-Cortef octobre 2025 ; Ciproxine août 2025 ; Trandate mars 2026 ; Voltarène avril 2026 ; Prednisone juin 2026 ; Rocephin juin 2025. |
| M2 | SY-50 management[0] | Propranolol sans contre-indication : ajouter celle de l'AIPS Inderal (asthme, BPCO). |
| M3 | SY-28 management[1] | Site d'exsufflation : citer une source (ERC/SRC) au lieu de « À vérifier ». |
| M4 | SY-32, SY-36 | Seuil de PNN de la péritonite bactérienne spontanée et compensation d'albumine : source européenne (EASL 2018) à lire et citer. |
| M5 | SY-48 physiopathologie[1] | Délai de viabilité testiculaire non chiffré : le lire dans RMS 2017 (citée). |
| M6 | SY-39, SY-40, SY-41, SY-52 | Molécules « À vérifier » non nommées : nommer et doser selon l'AIPS, ou supprimer la mention. |

## Légers

L1 : le crédit de SY-35 (« Dr Thomas F. Sellers ») diffère de Commons, qui indique un auteur inconnu (CDC PHIL, domaine public) ; aligner le crédit sur Commons.
L2 : visages partiellement identifiables en SY-35 (yeux, nez), SY-50 (visage entier) et SY-51 (bandeau seul) ; ce sont des photos publiées, mais le consentement n'est pas documenté. Préférer un recadrage sur les yeux.
L3 : licences de SY-36, 37, 41, 50, 51 et 52 non revérifiées (limite de l'API Commons) ; SY-35 est confirmée en domaine public.
L4 : SY-31, la naloxone cite le schéma postopératoire de l'AIPS ; préciser le schéma du surdosage si l'AIPS le donne.
L5 : SY-38, ajouter l'érythromycine avant l'endoscopie (source ESGE à lire).
