# Audit médical agressif : Management M-01 à M-17 et Communication K-01 à K-18

Version auditée : 35 fichiers JSON, 125 439 octets, SHA-256 de la concaténation `4706b7b7…9659` (commit 5c1f24343). Date : 14.11.2026. Auditeur indépendant (non rédacteur). Le score 14 points du §12.2 ne s'applique pas (fiches, pas monographies) ; chaque axe reçoit donc 2, 1 ou 0.

## Ce que j'ai réellement lu et vérifié

| Contrôle | Source ouverte ce jour | Résultat |
|---|---|---|
| Quatre dimensions KK | Exigences MED 2026 § 5.1.4 b (PDF OFSP) | Citation **exacte** dans K-01 à K-04 ; dimensions 1 et 4 non évaluées sans PS : exact |
| Ancres 1–5 | Directives MED 2026 § 4.3 h | Mention « construites, non officielles » présente dans K-01 à K-04 ; § 4.3 h exact |
| Format des stations | Informations MED 2026 § 5.1–5.6, note 1 ; Directives § 4.3 b, 5.2 e, 6.2 ; Richtlinien (de) § 5.2 e | Exact (4 + 9 min, 8 min, pas de résumé en CR, matériel, dialecte) |
| Adrénaline, amiodarone | AIPS refdata via `aips_fiche.py` : Adrenalin Aguettant 1 mg/mL n° 66396 (juin 2023) ; Amiodarone Labatec i.v. n° 59528 (mars 2025) | Citations **mot pour mot exactes**, numéros et dates exacts |
| ALS : moment des médicaments, accès | SIRMED (Suisse), « Reanimation 2025 », paraplegie.ch ; (source européenne : Resuscitation Council UK, algorithme ALS 2025) | Voir défaut G1 |
| Capacité de discernement | ASSM, directives « La capacité de discernement dans la pratique médicale » (2019, approuvées 29.11.2018), § 2.3, 2.4 | Voir M1, M2 |
| CC art. 16, 371, 378, 379, 429, 430, 434, 439 | fedlex, filestore, version du 1.1.2026 | Contenu des fiches exact ; « non relu » désormais levable |
| Guide ASSM 2022 | Zenodo 7148494, PDF lu | 10 citations « dire » vérifiées mot pour mot (vignette, thoracoscopie, OARS, DA, NURSE « pas déjà », 12 ans, 7 ans) |
| smarter medicine | SSMIG 2014 (5 points), SSMIG 2021_II point 1, SSI 2020 (5 points) | Exact ; bactériurie absente de la liste SSI (voir M4) |
| Calcul M-04 | Python : 0,2/0,8 = 0,25 ; × 10 = 2,5 ; 2,5/3,5 = 0,714 | Exact |
| Liens | 219 identifiants du corpus | Aucun lien mort |

## Défauts et PATCH exacts

| # | Gravité | Emplacement | Extrait (mot pour mot) | PATCH | Source |
|---|---|---|---|---|---|
| G1 | **Grave** | M-03, étape 5, `faire` 3 et 4 | « Administrer l'adrénaline selon l'AIPS : « Administration de 1 ml… » » | Insérer avant la citation : « Donner l'adrénaline dès que possible en asystolie ou en activité électrique sans pouls ; en rythme choquable, après le 3e choc, puis toutes les 3 à 5 minutes. » Insérer avant l'amiodarone : « Donner l'amiodarone après le 3e choc ; envisager 150 mg après le 5e choc. » Remplacer « Poser un accès veineux ou intraosseux » par « Poser d'abord un accès veineux, puis un accès intraosseux si la voie veineuse échoue ». | SIRMED, Reanimation 2025 (« i.v. VOR i.o. », « ERC: nach dem 3. Schock ») ; (source européenne : RC UK ALS 2025) |
| M1 | Moyen | M-14, étape 1, `faire` 1 | « la capacité se juge pour une décision donnée, à un moment donné (CC art. 16, cité par l'ASSM) » | Remplacer la parenthèse par « (ASSM, directives Capacité de discernement 2019, § 2.3 ; l'art. 16 CC ne le dit pas lui-même) ». | ASSM 2019 § 2.3 ; CC art. 16 |
| M2 | Moyen | M-14, étape 1, `faire` 2 ; grille 2 ; source 4 | « comprendre l'information, apprécier sa situation, raisonner sur les options, exprimer un choix stable (directives ASSM 2018, non lues, À vérifier) » | « Tester quatre capacités : compréhension, évaluation, formation de la volonté, concrétisation de la volonté (ASSM 2019, § 2.4, lu) ». Source 4 : « ASSM, … (2019) — lu le 14.11.2026, § 2.3–2.4 ». | ASSM 2019 § 2.4 |
| M3 | Moyen | M-14 étape 4 ; M-15 étape 3 ; M-16 étape 6 ; sources CC de M-14, M-15, M-16, K-14 | « selon l'ordre du CC (non relu, À vérifier) » ; « CC, non relu » | Écrire l'ordre de l'art. 378 al. 1 (personne désignée, curateur, conjoint, concubin, descendants, parents, frères et sœurs, chacun s'il assiste régulièrement) ; citer l'art. 379 ; art. 371 al. 1 « datées et signées » ; M-15 : ajouter « délai d'appel de dix jours (art. 439 al. 2) », « informer si possible un proche par écrit (art. 430 al. 5) » et les trois conditions du traitement sans consentement (art. 434). Remplacer « non relus » par « lus le 14.11.2026 (fedlex, version 1.1.2026) ». | CC art. 371, 378, 379, 430, 434, 439 |
| M4 | Moyen | M-06, `erreurs` 3 | « Traiter une bactériurie asymptomatique hors grossesse (déduction, À vérifier). » | « Traiter une bactériurie asymptomatique, sauf grossesse, greffe ou geste urologique invasif (cas par cas, avis infectiologique) (HUG 2026). » Ajouter un exemple de 1re ligne (cystite : nitrofurantoïne ou fosfomycine, HUG 2026), doses AIPS via `aips_fiche.py`. | HUG, Stratégie « Infections urinaires » 2026, p. 17 |
| M5 | Moyen | M-07, étape 4 et sources 5–6 | « (OMS, dernier recours, À vérifier) » ; « DN4 — non lu » | Citer la source suisse lue : « HUG, Stratégie Douleur aiguë 2024 (paliers OMS, DN4, laxatif systématique) ». Garder l'OMS en second. | HUG Douleur aiguë 2024, § 3–4.2 |
| M6 | Moyen | M-07, `exemple_station` | « explique la somnolence possible et la conduite interdite » | « … et l'interdiction de conduire tant qu'il se sent somnolent » (cohérent avec l'étape 5). | Cohérence interne |
| M7 | Moyen | M-02, étape A ; `exemple_station` | « Libérer les voies aériennes… » (cas d'un cycliste traumatisé) | Ajouter : « Chez le traumatisé, limiter les mouvements du rachis cervical pendant A. » Remplacer la source ATLS (américaine, non lue) par une source européenne : Rossaint et al., European guideline on management of major bleeding after trauma, 6e éd., Crit Care 2023 — à lire. | Règle « aucune source américaine exclusive » |
| M8 | Moyen | K-15, `exemple_station` | « L'examinateur note la communication avec l'infirmier et avec le médecin appelé. » | « L'examinateur note la communication avec le patient et avec l'infirmier (Informations MED 2026 § 5.5). » | Informations MED 2026 § 5.5 |
| M9 | Moyen | M-03 étape 6 ; M-16 étapes 4 et 6 | Aucune source suisse sur la décision de réanimation | Ajouter « ASSM, Directives Décisions de réanimation (éd. 2021) — non lu, À vérifier » et l'étape « Informer des chances réalistes de survie avant de demander le choix ». | ASSM (édition 2013 trouvée sur sams.ch ; 2021 non lue) |
| L1 | Léger | K-14, étape 4 | « l'ASSM écrit : « Dès douze ans, les adolescents sont capables de discernement » » | Citation exacte (vérifiée). Ajouter : « repères ASSM 2019 : 12 ans pour une intervention simple, 16 ans pour un traitement complexe ou long ». | ASSM 2019, p. 20 |
| L2 | Léger | M-14, M-15, M-16, K-14 sources | « art. 16 (cité mot pour mot par l'ASSM 2022) » | L'ASSM cite l'ancienne teneur (« à cause de ») ; écrire « teneur en vigueur : « en raison de son jeune âge… » ». | CC art. 16 |
| L3 | Léger | M-03, étape 5, `faire` 5 | « hypothermie » | « hypo- ou hyperthermie » ; ajouter « envisager la position antéro-postérieure des électrodes après 3 chocs ». | RC UK ALS 2025 |
| L4 | Léger | M-03, étape 3 | « chez l'enfant et le noyé, commencer par cinq insufflations puis 15:2 (enfant) » | « … puis 15:2 si formé à la réanimation pédiatrique, sinon 30:2 ». | SIRMED 2025 |
| L5 | Léger | M-10, ponction lombaire | « ou œdème papillaire (ESCMID…) » | ESCMID 2016 retient un GCS < 10, pas l'œdème papillaire ; corriger après lecture. | ESCMID 2016 (à lire) |
| L6 | Léger | M-01 et M-02, `exemple_station` | « Mme Meier, 45 ans… (exemple officiel) » ; « contrôle d'abord une hémorragie visible » | Séparer : « Exemple officiel : … » puis « Déroulé construit : … » ; l'âge et l'hémorragie ne figurent pas dans le texte officiel. | Informations MED 2026 § 5.1, 5.5 |
| L7 | Léger | K-18, étape 2 | « Dörf ich Hochdütsch rede ? … » | Un candidat qui comprend mal le dialecte demande en allemand standard : « Könnten wir bitte Hochdeutsch sprechen? Ich verstehe den Dialekt leider nicht so gut. » | Réalisme |
| L8 | Léger | K-01 à K-04, dernière ligne de grille | « Station sans PS : dimension non évaluée. » | Phrase verbale : « L'examinateur n'évalue pas cette dimension sans PS. » | Règle des phrases verbales |
| L9 | Léger | M-17 et K-17 | Même scénario (antihypertenseur du voisin) | Changer l'un des deux (ex. K-17 : surdosage d'insuline et hypoglycémie). | Redondance |

## Score par axe (2 / 1 / 0)

| Axe | Note | Raison |
|---|---|---|
| Doses AIPS | 2 | Deux citations exactes, numéros et dates justes ; aucune dose hors AIPS |
| ABCDE, BLS/ALS | 1 | BLS conforme ; ALS sans moment des médicaments ni priorité veineuse (G1, M7) |
| Antibiothérapie, antalgie | 1 | Principes justes ; sources suisses lisibles non utilisées (M4, M5) |
| Discernement, CC, directives anticipées | 1 | Contenu juste ; critères ASSM et articles CC « non lus » alors que lisibles (M1–M3) |
| Quatre dimensions KK, ancres | 2 | Citation exacte, mention « construites, non officielles » présente |
| Réalisme des formulations et stations | 1 | Bon dans l'ensemble ; M6, M8, L6, L7 |
| Étiquetage des sources, honnêteté lu/non lu | 1 | Honnête, mais ATLS américain seul (M7) et recherches incomplètes (ASSM 2019, CC) |
| Phrases verbales | 2 | Respectées, sauf L8 |

Total : 11 / 16 = 69 %. Aucun défaut critique.

## Verdict

**Question finale : non.** Le lot reste refusé tant que G1 et M1–M9 ne sont pas corrigés. Il manque : le moment de l'adrénaline et de l'amiodarone en ALS ; les critères ASSM 2019 et le texte du CC, désormais lisibles ; les sources suisses HUG pour l'antibiothérapie et l'antalgie ; une source européenne à la place de l'ATLS ; la lecture de l'ERC 2025 ALS et des directives ASSM Décisions de réanimation 2021. Après ces PATCH, le lot peut passer en `audit-ok`.
