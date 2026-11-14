# Corrections après audit — Syndromes SY-55 à SY-81 (14.11.2026)

Réponse à `semiologie/AUDIT_SYNDROMES_55_81.md`. J'ai relu chaque dose ajoutée ou modifiée par URL refdata avec `Claude/_harnais/aips_fiche.py`, et je cite le texte de l'AIPS mot pour mot. Les 27 JSON se chargent avec `json.load`. Les renvois S-xx et les fichiers image existent. Je n'ai fait ni commit ni push.

## Critiques

| # | Fiche | Correction appliquée | AIPS relue |
|---|---|---|---|
| C1 | SY-56 | J'ajoute la calcitonine dans la crise hypercalcémique : 5 à 10 U.I./kg dans 500 ml en ≥ 6 h/jour, ou 2 à 4 injections i.v. lentes, avec réhydratation. | Miacalcic® Ampoules n° 38605, janvier 2022 |
| C2 | SY-63, SY-67 | Acide folique : 5 mg/jour jusqu'à normalisation, jusqu'à 15 mg/jour. Je ne le donne jamais seul dans l'anémie pernicieuse. | Acidum folicum Streuli® n° 36752, janvier 2023 |
| C3 | SY-63 | J'ajoute le schéma simplifié de Ferinject : Hb < 10 g/dl : 1500 ou 2000 mg ; 10 à < 14 g/dl : 1000 ou 1500 mg ; < 35 kg : 500 mg. Dose unique ≤ 20 mg/kg et ≤ 1000 mg, au plus 1000 mg par semaine. | Ferinject® n° 57851, juin 2025 |
| C4 | SY-69 | Lithium : 4 comprimés de Quilonorm retard (1800 mg) répartis dans la journée, lithiémie cible 0,8 à 1,2 mmol/l. | Quilonorm® retard n° 35960, mars 2025 |
| C5 | SY-70 | Halopéridol 5 mg i.m., renouvelable toutes les heures, 15 mg/jour suffisant le plus souvent, maximum 20 mg/jour ; moitié de ces doses après 65 ans. | Haldol® n° 26891, novembre 2024 |
| C6 | SY-71 | **Correction partielle, en désaccord avec l'audit.** Pour le délire, l'AIPS écrit « 1 à 10 mg par voie intramusculaire », paliers toutes les 2 à 4 h, maximum 10 mg/jour. Le schéma « 2 à 5 mg i.m. renouvelable toutes les heures » proposé par l'audit vaut pour la **maladie de Huntington**. J'ai vérifié le passage dans le HTML brut. Je garde 1 à 10 mg et j'ajoute la règle de la personne âgée : moitié de la plus faible dose adulte au début, moitié de la dose adulte au maximum. La synthèse orale de la patiente de 84 ans prévoit donc 0,5 mg. | Haldol® n° 26891 |
| C7 | SY-73, SY-74 | Diazépam i.v. lent, 0,1 à 0,2 mg/kg, répétable toutes les 8 h, matériel de réanimation prêt. L'AIPS cite les « épisodes d'agitation motrice » mais ne nomme pas les toxidromes. | Valium® n° 28840, juin 2023 |

## Graves

- **G1 (SY-80)** : avec l'ampoule, j'écris adrénaline 500 µg (0,5 ml à 1 mg/ml) i.m., répétable toutes les 5 min. Chez l'enfant : 0,3 mg de 6 à 12 ans, 0,15 mg de 6 mois à 6 ans. Demi-dose sous amitriptyline, imipramine ou bêtabloquant (Adrenalin Sintetica n° 56551). Les doses de Jext restent pour l'auto-injecteur. La synthèse orale passe à 0,5 mg.
- **G2 (SY-72)** : délirium tremens ou voie orale impossible → diazépam 0,1 à 0,2 mg/kg i.v., répété toutes les 8 h, puis relais oral (Valium® n° 28840). J'ai complété le drapeau rouge.
- **G3, M8 (SY-55)** : chez l'alcoolique, le dénutri ou le patient sous sulfonylurée, je préfère le glucose i.v. Je cite mot pour mot la phrase de l'AIPS : glucagon « peu ou pas d'effet ». L'indication se limite au diabétique traité à l'insuline (GlucaGen® n° 31489, URL refdata).
- **G4 (SY-63)** : vitamine B12 1000 µg i.m. par semaine, puis 1000 µg par mois à vie, et tous les deux jours au début s'il y a une atteinte neurologique (Vitarubine® n° 21672).
- **G5 (SY-64)** : j'ajoute les antidotes et le concentré de complexe prothrombinique (PPSB) :
  - Beriplex® n° 00665 : 25, 35 ou 50 U.I./kg selon l'INR, au plus 5000 U.I. ;
  - Praxbind® n° 65804 : 5 g ;
  - Ondexxya™ n° 67759 : 400 mg puis 4 mg/min, ou 800 mg puis 8 mg/min.
- **G6 (SY-78)** : forme sévère → benzylpénicilline 1 à 5 millions d'U.I. par jour en 4 à 6 doses (Pénicilline « Grünenthal » n° 56271, qui nomme l'érysipèle).
- **G7 (SY-62)** : injection intrafocale de Kenacort-A 10 seulement, 10 à 40 mg selon la taille de la région, à au moins 2 semaines d'intervalle.
- **G8 (SY-73)** : je donne les critères de Hunter en entier ; le dernier critère devient « hypertonie, température > 38 °C et clonus oculaire ou inductible ». La source reste à relire.
- **G9 (SY-57)** : NaCl 3 % 150 ml en 20 min, répété au plus 2 fois jusqu'à +5 mmol/l, puis ≤ 10 mmol/l le premier jour et ≤ 8 mmol/l ensuite. Source européenne lue via un résumé secondaire, à relire. Le NaCl 3 % est absent du corpus AIPS.

## Moyens

- **M1 (SY-74)** : le bicarbonate est hors AIPS dans cette indication. L'AIPS Bichsel n° 36797 autorise les acidoses et les intoxications aux barbituriques.
- **M2 (SY-80)** : j'ajoute le salbutamol, 1 à 2 inhalations dans le bronchospasme aigu (Ventolin n° 37397). L'anaphylaxie n'y est pas nommée.
- **M3 (SY-79)** : on suspecte le sepsis devant toute infection avec dysfonction d'organe. Le qSOFA sert au pronostic, pas seul au dépistage (SSC 2021).
- **M4 (SY-67)** : je remplace l'extrait Solu-Medrol par l'indication « Anémie hémolytique auto-immune acquise ». La dose « ≥ 0,5 mg/kg/24 h » citée par l'audit **ne figure pas** dans le texte refdata lu ; je laisse donc la dose « À vérifier ».
- **M5 (SY-77)** : je précise que l'adrénaline, les antihistaminiques et les corticoïdes sont peu ou pas efficaces dans l'angio-œdème bradykinique.
- **M6 (SY-68)** : je source PROFILES 2 (EPA 2d, examen dès 2028), lu en résumé via le rapport du 14.11.2026.
- **M7 (SY-68)** : escitalopram après 65 ans, 5 mg puis au maximum 10 mg (Escitalopram-Mepha n° 62787).

## Légers

- **L1 (SY-56)** : l'AIPS Zometa® (refdata n° 56257, mars 2026) se contredit. Les indications écrivent « > 12.0 mg/dl [3.0 mmol/l] », la posologie « ≥ 3.0 mmol/l ». Je cite les deux formules et j'ajoute la contre-indication pendant la grossesse et l'allaitement.
- **L2** : je corrige les lettres VITE DIT CAFé.
  - Métabolique et endocrinien passent en « F (fonctionnel) : … » : SY-58, 60, 62, 68, 69, 70, 71 et 81.
  - SY-56 : l'adénome parathyroïdien passe en « T (tumoral bénin) ».
  - SY-60 : la grossesse passe en F.
- **L3 (SY-77)** : j'écris EAACI 2022 dans les examens comme dans les sources.
- **L4 (SY-75)** : je cite l'AIPS Naloxon OrPha (URL refdata, n° 56952) pour le risque de sevrage aigu, au lieu de « (déduction) ».
- **L5 (SY-67)** : je recadre l'image sur un seul œil, sans nez ni visage, à partir de la miniature de 960 px. L'original est dans le domaine public, ce qui permet le recadrage. J'ai regardé le résultat. Le crédit devient « Auteur inconnu, recadré ».
- **L6** : j'ajoute la clé `image.legende` à `semiologie/SCHEMA_SYNDROME.md`, sur ordre de correction.

## Reste « À vérifier »

- Volume du bolus de glucose : l'AIPS ne donne pas de bolus.
- Absents du corpus AIPS : NaCl 3 %, cyproheptadine, physostigmine.
- Dose du corticoïde dans l'anaphylaxie et dans l'hémolyse auto-immune.
- Volumes de cristalloïdes : aucune AIPS ne les fixe.
- Guides européens non lus : EAACI, ESE, BOAST, SCORTEN, Hunter.
- Chapitres de ssi.guidelines.ch.
