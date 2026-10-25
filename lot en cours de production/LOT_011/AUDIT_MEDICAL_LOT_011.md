# Audit médical — LOT_011 — G11 Troubles du sommeil

Auditeur médical, rôle distinct du rédacteur d’origine et distinct de l’auditeur linguistique.
Date : 2026-10-25, 18:15 Europe/Zurich.
Prompt : V8, `PROMPT_Casern/PROMPT_ULTIME_PRODUCTION_LOTS_V8.md`, §5.2–5.3, §6.3, §12.
Périmètre : HTML du dossier `lot en cours de production/LOT_011/` après reprise des parties B depuis le Drive (tailles d’origine identiques). `app_v2.html` non lu.

## Sources réellement ouvertes pendant cet audit

- [S6] Riemann D et coll. European Insomnia Guideline 2023. Journal of Sleep Research. DOI 10.1111/jsr.14035. Page Wiley lue le 25.10.2026 (résumé et tableau 16).
- [S1 relu] Bassetti CLA et coll. Epidemiology and Economic Burden of Sleep Disorders in Europe. European Journal of Neurology. 2026. DOI 10.1111/ene.70463. Version PMC lue le 25.10.2026.
- [S3 relu] Kim HK, Shin HR. Sleep Medicine Research. 2024. DOI 10.17241/smr.2024.02258. Page lue le 25.10.2026. Le « 8 % » et l’enquête de 2 019 adultes sont confirmés. Aucune correction de ce chiffre.
- [S7] Information professionnelle Quviviq®, daridorexant, état juillet 2024, numéro d’autorisation 68481 lu à la rubrique Zulassungsnummer. Page allemande swissmedicinfo lue le 25.10.2026.
- Calcul dérivé, fait avec l’interpréteur : 45 × 0,133322 = 6,0 kPa ; 50 × 0,133322 = 6,67 kPa, arrondi à 6,7 kPa.

Non ouverts : volume ICSD-3 et ICSD-3-TR, autres AIPS, texte suisse de conduite, recommandations 2024 des jambes sans repos, consensus 2025 du trouble en sommeil paradoxal, HypnoLaus. Ces manques restent dans `HELP_LOT_011.md`. Aucune dose n’a été comblée de mémoire.

## Score §6.3

Cinquante questions (section 6.1), 2 points si la question est satisfaite, 1 si elle l’est en partie, 0 si elle est absente ou fausse, sans objet seulement avec motif. Maximum 100. Le score du fichier est la moyenne de ses monographies.

| Fichier | Score | Critique restante |
|---|---|---|
| Appel A | 90 % | 0 |
| Partie 1 | 93 % | 0 |
| Partie 2 | 89 % | 0 |
| Partie 3 | 90 % | 0 |
| Partie 4 | 89 % | 0 |

Détail des pertes (points retirés sur 100) après correction :

| Monographie | Pertes retenues | Score |
|---|---|---|
| SSP G11 | grossesse 2, foie 2, rein 2, enfant 1, autres doses 1, épidémiologie suisse 1, sensibilité 1, sortie 1 | 89 |
| DX.1 apnées | grossesse 2, enfant 1, foie 1, rein 1, sensibilité 1, bandes diagnostiques 1, indication suisse de pression positive 1 | 92 |
| DX.2 insomnie | épidémiologie suisse 1, sensibilité 1, autres molécules 1, assurances 1, sortie 1, modèles fins d’hyperéveil 1 | 94 |
| DX.3 bruxisme | grossesse 2, foie 2, rein 2, enfant 1, dose 1, sensibilité 1, épidémiologie suisse 1 | 89 |
| DX.4 jambes sans repos | grossesse 2, foie 2, rein 2, enfant 1, ferritine 1, dose 1, écart 3 % / 5–7 % assumé 1 | 89 |
| DX.5 circadien | grossesse 2, foie 2, rein 2, enfant 1, lux et mélatonine 1, sensibilité 1, épidémiologie suisse 1 | 89 |
| DX.6 mouvements périodiques | grossesse 2, foie 2, rein 2, enfant 1, dose 1, manuel de cotation non ouvert 1, épidémiologie 1 | 89 |
| DX.7 somnambulisme | grossesse 1, enfant 1, autres hypnotiques 1, sensibilité 1, épidémiologie 1, sortie 1, foie 1, rein 1 | 91 |
| DX.8 trouble paradoxal | grossesse 2, foie 2, rein 2, dose 1, seuil d’atonie 1, séries non rouvertes 1 | 90 |
| DX.9 narcolepsie | grossesse 2, enfant 2, foie 2, rein 2, éveillants 1, texte de conduite 1 | 89 |
| DX.10 hypersomnie | grossesse 2, foie 2, rein 2, enfant 1, éveillant 1, prévalence 1, sensibilité 1 | 89 |

Appel A = moyenne des onze lignes = 990/11 = **90 %**.
Partie 1 = (92+94)/2 = **93 %**. Partie 2 = 89 %. Partie 3 = (89+91)/2 = **90 %**. Partie 4 = (90+89+89)/3 = **89 %**.

Les zéros restants portent sur des situations spéciales dont la source n’a pas été ouverte. Ils ne sont pas des doses fausses. Ils empêchent les parties 2 et 4 d’atteindre 90 %.

## Corrections

### Critique

Aucune erreur critique trouvée, et aucune laissée. Le lot d’origine ne chiffrait aucune dose. L’audit n’a pas inventé de dose hors de l’AIPS lue.

### Grave

1. Fichier : parties B, surtout la partie 3. Emplacement : blocs « Mémo » en fin de fichier. Extrait : « Sur la copie, cette décision se rédige en phrase verbale. On nomme la source lue le 25.10.2026 lorsqu’elle existe, [S1] à [S5] selon le cas ». Correction : 68 paragraphes identiques retirés (11, 4, 41 et 12). Ce n’était pas une donnée clinique. Source : V8 §7 (pas de remplissage). Le détail de forme est dans l’audit linguistique. L’effet médical est d’avoir gonflé les fichiers sans ajouter de fait.
2. Fichier : Appel A, point 11 ; partie 1, DX.2. Extrait : « Le guide de 2023 n’ayant pas été rouvert, la phrase « la thérapie cognitivo-comportementale est le premier choix » reste À vérifier ». Correction : le guide a été ouvert. La thérapie cognitivo-comportementale de l’insomnie est le premier choix, grade A, chez l’adulte de tout âge, avec ou sans comorbidité. L’hygiène seule n’est pas ce traitement. Un médicament vient si elle ne suffit pas. Source : Riemann 2023, tableau 16, page lue le 25.10.2026.
3. Fichier : partie 4, DX.9, point 11 ; Appel A, tableau du point 3. Extrait : « Les médicaments éveillants et les traitements de la cataplexie restent À vérifier (AIPS). Aucun nom de spécialité et aucune dose. » Correction : Quviviq® (daridorexant, autorisation 68481) est contre-indiqué dans la narcolepsie. La dose d’insomnie, 50 mg ou 25 mg, ne se prescrit pas ici. Source : information professionnelle, rubrique Contre-indications, juillet 2024.
4. Fichier : partie 3, DX.7, point 11. Extrait : « La branche médicament reste fermée tant que l’AIPS n’est pas lue. » Correction : si un comportement complexe apparaît sous Quviviq® (somnambulisme, conduite endormie), on arrête le produit immédiatement. Cette dose ne traite pas la déambulation. Source : même information professionnelle, rubrique des comportements complexes du sommeil.

### Moyen

1. Fichier : Appel A et partie 1, épidémiologie des apnées. Extrait : « 18 % pour un indice d’au moins 15, surtout à partir de 30 ans ». Correction : le 18 % de l’article vise les personnes de 30 ans ou plus, parce que les données dès 20 ans étaient insuffisantes, pour un indice ≥ 15. Source : Bassetti 2026, tableau 1 et note, PMC lu le 25.10.2026. Les chiffres 0,009 % / 0,0087 %, 10 %, 3 %, 0,03 %, la fourchette de narcolepsie 1,05 à 79,40 pour 100 000, et 1 855 euros par habitant en Suisse sont conformes à la même page. Ils n’ont pas été modifiés.
2. Fichier : Appel A et partie 1, hypoventilation. Extrait : « supérieure à 45 mm Hg » et « supérieure à 50 mm Hg ». Correction : ajout de 6,0 kPa et 6,7 kPa, marqués calcul dérivé. Les seuils en mm Hg du chapitre n’ont pas été changés.
3. Fichier : Appel A, point 8, et partie 1, question d’examen. Extrait : « Les bandes léger, modéré et sévère ne figurent pas dans le tableau lu : elles restent À vérifier. » Correction : les coupures 5–15, 15–30 et ≥ 30 restent À vérifier comme classification diagnostique. L’AIPS de Quviviq® décrit des études à 5–< 30 et ≥ 30 événements par heure, patients sous pression positive exclus, sans hausse de l’indice ni baisse de saturation, et sans donnée dans la bronchopneumopathie chronique obstructive sévère. Ce n’est pas le traitement de l’apnée. Source : information professionnelle, juillet 2024.

### Léger

Aucune correction médicale légère isolée. Les « À vérifier (AIPS) » conservés sont des absences de source, comptées dans le score, pas des phrases fausses à réécrire.

## Sécurité patient

La conduite dangereuse reste suspendue dès la somnolence incoercible. Le lit se sécurise dès le récit d’un rêve violent ou d’une déambulation. Quviviq® ne se commence pas le jour même si une apnée est plausible et non traitée. La narcolepsie contre-indique ce produit. Un comportement complexe impose son arrêt.

Contenu d’audit produit par IA ; non validé cliniquement par un médecin.
