# Audit agressif — Physiologie v2, PHY-S1 à PHY-S4 (32 fiches)

Auditeur indépendant, 14.11.2026. Skills `medecin-expert` et `expert-web` appliqués. Aucun fichier modifié hors ce rapport ; ni commit ni push.

**Méthode :**
- Lecture champ par champ des 32 fiches (S1 : 9 ; S2 : 6 ; S3 : 10 ; S4 : 7).
- Recalcul par script de chaque exemple résolu.
- Confrontation de chaque valeur dite « suisse » à la fiche Examens citée : 17 valeurs vérifiées, toutes recopiées fidèlement.
- Résolution par script des passerelles et des renvois PP : aucun lien mort.
- Recherche de doses : aucune trouvée.
- Recherche web : ERS/ATS 2022, ESC 2024 HTA, ESC/EAS 2025, SpO2 cible. Aucune recommandation suisse trouvée pour l'HTA (SSH) ni pour la SpO2 cible.

## 1. Calculs refaits (outil : Python)

| Fiche | Calcul | Résultat refait | Verdict |
|---|---|---|---|
| S1-1 | Nernst K+ 4/140 puis 8/140 | −95,0 ; −76,5 mV | Juste |
| S1-6 | PAM 150/90 et 110/70 ; PPC (PIC 30) | 110 → 80 ; 83,3 → 53,3 | Juste |
| S1-8 | GCS 2+2+4 | 8 | Juste |
| S1-9 | Glucose LCR/sérum 1,5/7 | 0,21 (seuil 0,5 conforme à RMS 2016 via EX) | Juste |
| S2-1 | Accommodation 1/0,25 − 1 | 3 D | Juste |
| S2-2 | 80 − 60 dB | × 100 | Juste |
| S2-3 | Gain vHIT 120/200 | 0,6 | Juste |
| S2-4 | Goldmann 2,5/0,25 + 9 ; 2,5/0,1 + 9 | 19 ; 34 mmHg | Juste ; formule incomplète (M3) |
| S3-1 | FE (120 − 50)/120 | 58 % | Juste |
| S3-2 | 70 × 70 ; 40 × 120 | 4,9 ; 4,8 L/min | Juste |
| S3-3 | Laplace 150 ; 225 ; 112,5 | Exact | Conclusion fausse (L1) |
| S3-4 | PAM 120/80 ; 80/45 | 93,3 ; 56,7 | Juste |
| S3-5 | Bazett 400/√0,8 | 447 ms | Juste |
| S3-6 | PPC 80 − 10 ; 45 − 25 | 70 ; 20 mmHg | Juste |
| S3-7 | Starling ±10, puis 0 | Exact | Modèle obsolète (M5) |
| S3-8 | Guyton (7 − 2)/1 ; (7 − 7)/1 | 5 ; 0 | Juste |
| S3-9 | CaO2, DO2 | 18,7 → 935 ; 10,8 → 324 mL/min | Juste |
| S3-10 | Friedewald 6,0 − 1,2 − 1,0 | 3,8 mmol/L | Juste |
| S4-1 | r/2 → × 16 ; 500/2,5 ; 500/10 | 16 ; 200 ; 50 mL/cmH2O | Juste |
| S4-2 | 0,25/1,60 ; 1,85/3,10 | 15,6 % ; 0,60 | Juste ; critère obsolète (G1) |
| S4-3 | PAO2 0,21 × 95 − 5,25 ; gradient | 14,7 ; 7,7 kPa | Juste au niveau de la mer (M4) |
| S4-4 | CaO2 Hb 15 puis 7 | 19,8 ; 9,4 mL/dL | Juste |
| S4-5 | VA 172,6/40 ; PaCO2 172,6/2,15 | 4,3 L/min ; 80 mmHg | Juste |
| S4-6 | H-H 24/1,2 ; 30/(0,03 × 63,8) | 7,40 ; 7,295 | Juste ; interprétation cohérente |

## 2. Défauts (Critique 0 · Grave 3 · Moyen 7 · Léger 10)

| # | Grav. | Emplacement | Extrait | PATCH exact | Source |
|---|---|---|---|---|---|
| G1 | **Grave** | PHY-S4-2 `valeurs_normales[1]`, `formule.exemple`, `sources[1]` | « hausse du VEMS ≥ 12 % et ≥ 200 mL … ERS/ATS » | `valeur` : « hausse du VEMS ou de la CVF > 10 % de la valeur **prédite** (ERS/ATS 2022) ; 12 % et 200 mL par rapport à la valeur initiale reste le critère GINA de l'asthme ». Ajouter à `exemple` : « VEMS prédit 2,40 L : 0,25 ÷ 2,40 = 10,4 % > 10 % : la réponse est significative selon ERS/ATS 2022. » Mettre la source à jour. | Source européenne : Stanojevic et coll., ERS/ATS technical standard, Eur Respir J 2022;60:2101499 (lu en résumé, non relu en entier) |
| G2 | **Grave** | PHY-S3-4 `valeurs_normales[0]` | « PA optimale au cabinet < 120/80 … ESH/ESC » | `parametre` : « PA de cabinet » ; `valeur` : « non élevée < 120/70 ; élevée 120–139/70–89 ; HTA ≥ 140/90 » ; `unite` : « mmHg (source européenne : ESC 2024, Eur Heart J 2024, doi:10.1093/eurheartj/ehae178 ; l'ESH 2023 garde “optimale < 120/80”) ». | Lu en résumé. Aucune position de la SSH trouvée. |
| G3 | **Grave** | PHY-S3-6 `dereglements[1].mecanisme` | « L'hypertrophie augmente la demande et la PAD peut baisser » | « L'hypertrophie augmente la demande ; la pression télédiastolique élevée et la systole allongée réduisent la perfusion sous-endocardique ; un angor apparaît sans sténose coronaire. » La PAD basse caractérise l'**insuffisance** aortique. | Déduction de la formule de la fiche (PPC = PAD − PTDVG) |
| M1 | Moyen | PHY-S3-1 `valeurs_normales[2]` | « FE du VG ≥ 50 % (ESC — non relues) » | Distinguer deux notions. Valeur normale : « 52–72 % (H) ; 54–74 % (F) » (source européenne : EACVI/ASE, Lang 2015). Seuils de l'insuffisance cardiaque : « ≤ 40 réduite ; 41–49 modérément réduite ; ≥ 50 préservée » (source européenne : ESC 2021 IC). | À lire puis à dater |
| M2 | Moyen | PHY-S2-5 `dereglements[2].pp` | « Myasthénie, SLA » → `PP-S1-A` | Scinder la ligne. Myasthénie → `PP-S1-A`. SLA → `PP-S1-D`, où elle figure ; PHY-S1-3 l'y range déjà. | `PP-S1-D.json` lu |
| M3 | Moyen | PHY-S2-4 `formule.expression` | « PIO = F ÷ C + Pe » | « PIO = (F − U) ÷ C + Pe (U = écoulement uvéoscléral) ». Sans U, l'effet des prostaglandines cité dans `cibles[1]` reste inexplicable. L'exemple reste valable avec U = 0 : ajouter « (U négligé) ». | Physiologie classique (non vérifié CH) |
| M4 | Moyen | PHY-S4-3 `formule`, `valeurs_normales` | « Pb ≈ 101,3 kPa » ; aucune norme du gradient | Ajouter « en altitude, Pb baisse : Berne (540 m) ≈ 95 kPa → PAO2 13,4 ; gradient 6,4 kPa ». Ajouter une valeur : « gradient A-a normal < 2 kPa chez le jeune ; il croît avec l'âge (non vérifié CH) ». Sans cette norme, « gradient élevé » n'a pas de référence. | Calcul refait par formule barométrique |
| M5 | Moyen | PHY-S3-7 `mecanisme[1]` | « Au pôle veineux … une partie du liquide est réabsorbée » | Ajouter : « Le modèle révisé (glycocalyx) montre qu'à l'état stable la réabsorption veineuse reste faible ; la lymphe ramène l'essentiel du filtrat. » Nommer l'exemple « modèle classique simplifié ». | Source européenne : Levick et Michel, Cardiovasc Res 2010 (non relu ce jour, À vérifier) |
| M6 | Moyen | PHY-S3-9 `mecanisme[2]` | « Le choc distributif (… atteinte médullaire) … débit reste souvent élevé » | « … le sepsis garde souvent un débit élevé au début ; le choc neurogénique associe vasoplégie et **bradycardie**, avec un débit bas. » | Physiologie : perte du tonus sympathique cardiaque (déduction) |
| M7 | Moyen | PHY-S1-6 `cibles[2]` | « nimodipine : Il prévient le vasospasme ischémique » | « Elle réduit l'ischémie cérébrale retardée et améliore le pronostic après HSA, sans supprimer de façon prouvée le vasospasme angiographique. » | Source européenne : ESO 2013 (Steiner, Cerebrovasc Dis) — À vérifier |
| L1 | Léger | PHY-S3-3 `formule.exemple` | « e = 2 : 112,5 ; donc l'hypertrophie normalise » | Remplacer « e = 2 : 450 ÷ 4 = 112,5 » par « e = 1,5 : 450 ÷ 3 = 150 ; la tension revient à sa valeur initiale ». | Calcul refait |
| L2 | Léger | PHY-S1-3 `mecanisme[4]` | « (AVC, traumatisme médullaire) … (choc spinal) » | « … d'abord une paralysie flasque (choc spinal si la lésion est médullaire, phase flasque après un AVC) … » | Terminologie |
| L3 | Léger | PHY-S3-4 `valeurs_normales[1]` | « hypotension orthostatique … (non vérifié CH) » | `unite` : « mmHg (source européenne : ESC 2018 syncope, Brignole, Eur Heart J 2018 — à relire) ». | Libellé |
| L4 | Léger | PHY-S3-9 et S4-4 `formule` ; PHY-S4-6 `formule` | « 0,003 × PaO2 (mmHg) » ; « 0,03 × PaCO2 en mmHg » | Ajouter les formes en kPa, l'unité des laboratoires suisses : « 0,0225 × PaO2 (kPa) » et « 0,23 × PaCO2 (kPa) ». Avec 0,23, l'exemple BPCO donne pH 7,29. | Calcul refait |
| L5 | Léger | PHY-S3-10 `valeurs_normales`, `sources` | « ESC/EAS 2019 » | Ajouter « cibles inchangées par la mise à jour ESC/EAS 2025 (Mach, Eur Heart J 2025, doi:10.1093/eurheartj/ehaf190) ». Relire la fiche Examens. | Lu en résumé |
| L6 | Léger | PHY-S3-5 `formule.usage` | Bazett seul | Ajouter : « Bazett surcorrige au-dessus d'environ 90/min ; on préfère alors Fridericia (QT ÷ ∛RR) » (non vérifié CH). | Physiologie classique |
| L7 | Léger | PHY-S4-4 `mecanisme[3]`, `valeurs[1]`, `dereglements[1].pp` | « … 2,3-DPG … (effet Bohr) » ; « oxyhémoglobine 90–95 % » ; « EP » → `PP-S4-I` | Réserver « effet Bohr » au CO2 et au H+. Préciser « FO2Hb (fraction), distincte de la SaO2 ». Envoyer l'EP vers `PP-S4-V`. | Terminologie |
| L8 | Léger | PHY-S4-1 `formule.exemple` | « 500 ÷ 2,5 = 200 mL/cmH2O » | Écrire « compliance **pulmonaire** ». Celle du système respiratoire vaut environ la moitié (non vérifié CH). | Physiologie classique |
| L9 | Léger | `pp: null`, 6 lignes | Queue de cheval (S1-5), néphrotique (S3-7), anaphylaxie (S3-7), anémie (S4-4), acidocétose (S4-6), toxidrome opioïde (S1-8, S4-5) | Néphrotique → `PP-S6-A` ; anémie → `PP-S10-Tr` ou `PP-S10-F` ; acidocétose → `PP-S8-F`. Aucune fiche PP n'existe pour les autres : signaler la lacune. | Script de résolution |
| L10 | Léger | PHY-S4-2 `boucle` (null) ; PHY-S2-6 `cibles[0]` ; PHY-S4-7 `mecanisme[3]` | Boucle absente ; « rendent l'accès » ; « IgA … dans les alvéoles » | Ajouter une boucle : capteur « aucun (examen) », intégrateur « comparaison à la LIN », effecteur « décision ». Corriger en « rouvrent l'accès ». Écrire « IgA sécrétoires dans les voies de conduction, IgG dans l'alvéole ». | Cohérence |

## 3. Vérifié conforme
- **Boucles :** baroréflexe (IX/X, NTS, SRAA, macula densa, β1-rénine) ; chémorécepteurs (H+ central, PaO2 périphérique vers 8 kPa, hyperoxie de l'hypercapnique expliquée par la VHP et l'effet Haldane) ; cycle cardiaque et B1/B2 ; Frank-Starling ; V/Q, shunt et espace mort ; courbe de l'HbO2 et CO ; potentiel d'action et Nernst ; Rinne/Weber ; HINTS ; DPAR ; Brown-Séquard.
- **Valeurs « suisses » (17) :** toutes identiques aux fiches Examens citées (HUG, USB, Insel).
- **Pharmacologie :** les cibles restent des classes sans dose ; aucune dose ni voie trouvée.
- **Honnêteté :** les étiquettes « (non vérifié CH) », « non lu » et « (déduction) » sont présentes et honnêtes. Les phrases sont verbales.
- **Lacunes de source :** aucune source suisse trouvée pour l'HTA (SSH), la SpO2 cible 88–92 % (BTS, à relire) ni les normes de physiologie classique ; ces valeurs gardent leur étiquette.

## 4. Verdict
**Non** pour `audit-ok` en l'état. Il faut corriger G1, G2 et G3, ainsi que M1 à M7. Les légers peuvent suivre dans le même lot. Après ces patchs, aucun défaut bloquant ne reste : les calculs sont justes et aucune dose n'apparaît.
