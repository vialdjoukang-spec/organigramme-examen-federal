# HELP_DX3 — LOT_016, Phase B, DX.3 Anorexie du vieillissement (30.10.2026)

Format Prompt V0 §18. Chaque question demande : recommandation suisse en vigueur (organisme, titre, année, URL), version la plus récente, doses AIPS avec numéro Swissmedic si un médicament est concerné, à défaut source européenne récente, extrait mot pour mot daté.

## H16-DX3-01 — Fréquence suisse de l'anorexie du vieillissement comme cause de PPI
- Identifiant : LOT_016, Phase B, DX.3, point 2.
- Contexte : le HTML écrit « La fréquence suisse de l'anorexie du vieillissement comme cause de PPI est une donnée non trouvée dans les sources consultées » ; la fréquence vient de la cohorte de Barcelone (5,3 %, calcul dérivé).
- Question : quelle étude suisse (Obsan, OFS, HUG, CHUV, Unisanté, Berne) chiffre les causes bucco-dentaires, de déglutition et sociales d'une PPI après 65 ans ?
- Déjà cherché : COFA 2018, RMS 2020 (HUG), Imoberdorf 2010, études bernoises 2024–2025 (Europe PMC), 30.10.2026.
- Emplacement : point 2, paragraphe principal.

## H16-DX3-02 — Recommandation suisse propre à l'anorexie du vieillissement ou à la santé bucco-dentaire du sujet âgé
- Identifiant : DX.3, points 1, 11, 12.
- Contexte : le HTML écrit « Aucune recommandation suisse propre à l'anorexie du vieillissement n'a été trouvée » ; il s'appuie sur la COFA 2018, la RMS 2020 et l'ESPEN 2022.
- Question : la Société professionnelle suisse de gériatrie (SPSG/SFGG), la SSO ou la SSNC publient-elles une recommandation sur l'anorexie du vieillissement, la dysphagie ou les soins bucco-dentaires des personnes âgées ?
- Déjà cherché : recherche web du 30.10.2026 (revmed.ch, edi.admin.ch) ; page UNIGE de F. Müller bloquée par un système de sécurité (non contourné).
- Emplacement : point 11, paragraphe d'introduction.

## H16-DX3-03 — Valeur diagnostique des signes buccaux, du Mini-Cog, de la GDS, de la VFS et de la FEES
- Identifiant : DX.3, points 6, 8, 9.a.
- Contexte : le HTML écrit que la sensibilité et la spécificité des signes buccaux et sociaux, de la VFS et de la FEES sont une donnée non trouvée ; les seuils du Mini-Cog et de la GDS en forme courte ne sont pas donnés.
- Question : quelle source suisse ou européenne chiffre ces valeurs et fixe les seuils du Mini-Cog et de la GDS-15 ?
- Déjà cherché : Bosch 2017, ESSD-EUGMS 2016, EWGSOP2 2019, 30.10.2026.
- Emplacement : point 6 (paragraphe principal), point 8 (fenêtre `dx3-p8-scores`), point 9.a (fenêtre `dx3-p9-gold`).

## H16-DX3-04 — Prévalence suisse de l'édentement, du port de prothèse et de la solitude après 65 ans
- Identifiant : DX.3, point 2, fenêtre `dx3-p2-suisse`.
- Contexte : seules deux petites études bernoises (2024, 2025) ont été lues ; aucune valeur OFS (ESS 2022) sur l'édentement, les prothèses ou le sentiment de solitude des 65 ans ou plus.
- Question : quelles valeurs l'ESS 2022 (OFS) ou l'Obsan donnent-elles pour ces trois indicateurs, par âge ?
- Déjà cherché : Obsan (indicateur des besoins dentaires non satisfaits : HTTP 404 en français), OFS, 30.10.2026.
- Emplacement : point 2, fenêtre `dx3-p2-suisse`.

## H16-DX3-05 — Critères suisses de sortie et traitement de la pneumonie d'aspiration
- Identifiant : DX.3, point 11.B (fenêtre `dx3-p11-urg`) et 11.D (fenêtre `dx3-p11-sortie`).
- Contexte : aucune liste officielle de critères de sortie n'a été trouvée ; l'antibiothérapie de la pneumonie d'aspiration est renvoyée à sa prise en charge propre, sans source lue.
- Question : quelle recommandation suisse (Société suisse d'infectiologie, SSNC, hôpitaux universitaires) fixe l'antibiothérapie de la pneumonie d'aspiration du sujet âgé et des critères de sortie après dénutrition ?
- Déjà cherché : ESSD-EUGMS 2016, ESPEN 2022, Reber 2019, 30.10.2026.
- Emplacement : fenêtres `dx3-p11-urg` et `dx3-p11-sortie`.

## H16-DX3-06 — Doses AIPS de la vitamine D et de la vitamine B12 chez le sujet âgé
- Identifiant : DX.3, points 9.b et 12 (fenêtres `dx3-p9-interp`, `dx3-p12-prim`).
- Contexte : la COFA recommande une supplémentation en vitamine D toute l'année et cite un traitement de la carence en B12 ; le HTML ne donne aucune dose faute d'AIPS lue.
- Question : quelles spécialités suisses (numéro Swissmedic) et quelles posologies AIPS s'appliquent à la prévention de la carence en vitamine D et au traitement de la carence en B12 chez le sujet âgé ?
- Déjà cherché : COFA 2018 ; corpus AIPS non interrogé pour ces molécules (hors du cœur de DX.3), 30.10.2026.
- Emplacement : fenêtres `dx3-p9-interp` et `dx3-p12-prim`.

## État après l'audit médical (30.10.2026, auditeur-medical, opus, xhigh)

- H16-DX3-05 : comblée en partie. Antibiothérapie de la pneumonie d'aspiration écrite d'après la SPILF 2025 (Infect Dis Now 2025;55:105081, points forts lus sur em-consulte ; texte intégral non accessible) et l'AIPS d'Augmentin comprimés filmés (45674, 53692, septembre 2026). Reste ouvert : recommandation suisse (Société suisse d'infectiologie : site ssi.guidelines.ch non lisible sans JavaScript) et critères suisses de sortie.
- H16-DX3-06 : comblée en partie. Dose recommandée de vitamine D écrite d'après la COFA 2018 (« une supplémentation de 800 UI/ jour est recommandée ») ; spécialité suisse et posologie AIPS toujours non lues (aucune monopréparation de cholécalciférol trouvée par nom dans le corpus le 30.10.2026).
- Nouvelles sources lues par l'audit (copies dans le scratchpad de l'auditeur, non versées dans `evidence/`, hors périmètre d'écriture) : fiche ESPEN GLIM 2024 (critère inflammation) ; OPAS art. 7, 8, 8a (Fedlex, état le 1.8.2026) ; CC art. 453 (Fedlex, état le 1.7.2026) ; AIPS Marcoumar® 19395 et Augmentin 45674/53692. À verser dans `evidence/DX3_*` par la session principale.
