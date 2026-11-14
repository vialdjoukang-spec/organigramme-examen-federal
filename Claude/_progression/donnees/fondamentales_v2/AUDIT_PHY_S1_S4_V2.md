# Contre-audit — PHY-S1 à PHY-S4, version corrigée (commit 65875a14a)

Auditeur indépendant, 14.11.2026. Skills `medecin-expert` et `expert-web` appliqués. Aucun fichier modifié hors ce rapport ; ni commit ni push.

**Méthode :**
- Lecture de `CORRECTIONS_PHY_S1_S4.md`.
- Diff mot à mot `fef44af50 → HEAD` des 32 fiches, y compris chaque verbe remplacé et chaque champ renommé.
- Recalcul des exemples nouveaux.
- Résolution par script des renvois PP, SY, S, EX et PH.
- Recherche de doses.
- Contrôle du schéma : `titre`, `cible`, `sources` présents partout.

Par ordre du coordinateur, je n'ai pas évalué les titres `fonction`. Les cinq `pp` null restants sont des compléments à venir : queue de cheval, deux toxidromes opioïdes, insuffisance aortique et anaphylaxie.

## 1. Défauts du premier audit

| # | Vérifié dans | État |
|---|---|---|
| G1 | PHY-S4-2 `valeurs_normales[1–2]`, `formule`, `sources` | **Corrigé.** ERS/ATS 2022 retient > 10 % de la valeur prédite ; GINA (> 12 % et > 200 mL) figure à part. L'exemple 0,25 ÷ 2,40 = 10,4 % est juste. |
| G2 | PHY-S3-4 `valeurs_normales[0–1]` | **Corrigé.** ESC 2024 donne : non élevée < 120/70, élevée 120–139/70–89, HTA ≥ 140/90. La divergence avec l'ESH 2023 est signalée. |
| G3 | PHY-S3-6 `dereglements[1]` et nouvelle ligne IA | **Corrigé.** La sténose aortique passe par la PTDVG et la systole allongée ; la PAD basse va à l'insuffisance aortique. |
| M1 | PHY-S3-1 | **Corrigé.** La normale EACVI/ASE est séparée des seuils de l'ESC 2021. |
| M2 | PHY-S2-5 | **Corrigé.** Myasthénie → PP-S1-A ; SLA → PP-S1-D, avec SY-1 (syndrome pyramidal) et S-26 (motricité), qui sont pertinents. |
| M3 | PHY-S2-4 | **Corrigé.** La fiche écrit (F − U) ÷ C + Pe ; l'usage cite les prostaglandines ; l'exemple précise « U négligé ». |
| M4 | PHY-S4-3 | **Corrigé.** La norme du gradient (< 2 kPa) est ajoutée ; le calcul pour Berne, refait, donne 18,6 → 13,4 → 6,4 kPa. |
| M5 | PHY-S3-7 | **Corrigé.** Le modèle révisé est ajouté avec l'étiquette « À vérifier » ; l'exemple porte le nom « modèle classique simplifié ». |
| M6 | PHY-S3-9 | **Corrigé.** La fiche distingue le sepsis (débit élevé) du choc neurogénique (bradycardie, débit bas). |
| M7 | PHY-S1-6 | **Corrigé.** La fiche dit : ischémie retardée réduite, vasospasme non supprimé de façon prouvée. |
| L1–L10 | 14 fiches | **Corrigés.** Laplace e = 1,5 → 150 (juste). Formes en kPa : pH 7,29 refait juste. Renvois PP-S6-A, PP-S10-F (carences : bonne cible), PP-S8-F et PP-S4-V. Boucle de S4-2 ajoutée. IgA et IgG, effet Bohr et FO2Hb corrigés. |

**Contrôles :** aucun renvoi mort, aucune dose, schéma homogène. Les champs renommés (`affection` → `titre`, `classe` → `cible`, étiquette → `sources`) gardent leur contenu à l'identique.

## 2. Défauts nouveaux ou résiduels

| # | Grav. | Emplacement | Extrait | PATCH exact |
|---|---|---|---|---|
| N1 | **Moyen** (erreur introduite) | PHY-S2-6 `dereglements` « Paralysie faciale idiopathique », `mecanisme` | « abolit le goût des deux tiers antérieurs ; ils deviennent insensibles » | « L'atteinte du VII abolit le goût des deux tiers antérieurs (agueusie) ; la sensibilité générale de la langue, portée par le V3 (nerf lingual), persiste. » |
| N2 | Léger (sens restreint) | PHY-S1-8 `dereglements` « Encéphalite herpétique », `mecanisme` | « L'inflammation corticale réduit le contenu de la conscience » | « L'inflammation corticale altère le contenu de la conscience ; elle provoque confusion, troubles du langage et crises. » |
| N3 | Léger | PHY-S4-2 `formule.exemple` | « 0,25 ÷ 1,60 = 15,6 % (≥ 12 %) : la réversibilité est significative » | Insérer « selon le critère GINA » après « significative ». Sinon, la phrase contredit la formule ERS/ATS 2022, qui divise par le prédit. |
| N4 | Léger | PHY-S4-2 `valeurs_normales[0].sources` | « GOLD et ERS/ATS — non relues pour cette fiche » | « (source internationale : GOLD, non relue, À vérifier ; ERS/ATS 2022 préfère la LIN, z < −1,645 — lu en résumé) ». |

Les autres verbes remplacés gardent leur sens. Exemples : « touche », « oriente vers », « réduit brutalement », « comprime les veines et réduit », « favorise », « corrige en minutes une partie de ».

## 3. Verdict
**Oui** pour `audit-ok`, à une condition : appliquer N1, seule erreur introduite par la correction, en un remplacement d'une phrase. N2 à N4 sont légers et ne bloquent pas. Aucun défaut grave ne reste.

## Clôture
N1 à N4 appliqués mot pour mot (tour 2) : **audit-ok** pour PHY-S1 à S4. La Physiologie complète (88 fiches) est audit-ok.
