# Audit de conformité et de langue — LOT_001 Phase A (cycle C1)

Fichier : LOT_001_Phase_A_V0.html — 171 635 octets (bande 100–200 Ko respectée) — SHA-256 b3ec1b93e4aa00b45b274e62a44f98c4c5c13507a745f19a5c77295857f597a2
Outils : `controle_lot.py verifier` (critiques du fichier : aucune) ; `extraire --points 1,5,6,7,10,13,14`. Point 14 lu jusqu'à la liste DX ; les 10 noms DX comparés par script à LISTE_DX_CANONIQUE.md.

## 1. Contrôles de structure

| Contrôle | Résultat |
|---|---|
| 14 points présents, titres et ordre conformes à §11 (1 à 14) | Oui |
| Taille 100–200 Ko | Oui (171 635 o) |
| Liste DX.1–DX.10 du fichier = liste canonique, mots et ordre | Oui (10/10, vérifié par script) |
| 11.A à 11.D présents | Oui (une occurrence chacun) |
| Cohérence A↔B | Non vérifiable : aucun fichier Phase B. Le script signale « DX Phase B [] » et « LISTE_DX absente ou illisible » ; le fichier existe, c'est le script qui ne le lit pas. Aucun écart prouvé. |
| Sections partagées ou renvoi à un autre fichier | Aucun constaté dans les points lus |

## 2. Score §12.2 (points 1, 5, 6, 7, 10, 13, 14 ; 2 questions par point, maximum 28)

| Point | Contenu au bon point | Forme (verbes, fenêtres, abréviations) | Score |
|---|---|---|---|
| 1 | 2 | 1 | 3/4 |
| 5 | 2 | 2 | 4/4 |
| 6 | 2 | 1 | 3/4 |
| 7 | 1 | 2 | 3/4 |
| 10 | 2 | 1 | 3/4 |
| 13 | 2 | 2 | 4/4 |
| 14 | 2 | 1 | 3/4 |
| **Total** | | | **23/28 = 82,1 %** |

Les points 2, 3, 4, 8, 9, 11, 12 ne sont pas notés ici (autres auditeurs).

## 3. Corrections

| Classe | Emplacement | Extrait | Correction |
|---|---|---|---|
| Moyen | Point 6, tableau, ligne Peau | « Sueur focale bilatérale : profil primaire ; sécheresse étendue à la chaleur : perte de refroidissement. » | Écrire des phrases verbales (« Une sueur focale bilatérale indique le profil primaire. »). |
| Moyen | Point 6, ligne Pouls ; ligne Ganglions | « Tachycardie > 100/min, pouls irrégulier ou tremblement fin nouveau : glycémie, ECG ou bilan… » ; « Tuméfaction acquise > 1 cm : élément du diagnostic clinique… » | Même correction : sujet, verbe, complément. |
| Moyen | Point 10, colonnes 2 et 3 | « 0. Confusion, malaise, dyspnée ou instabilité → fonctions vitales, glycémie, filière urgente adaptée. » | Garder « si X → Y » mais finir par un verbe (« … → le médecin mesure les fonctions vitales et la glycémie »). Vaut pour les nœuds 0 à 11. |
| Moyen | Point 7, tableau, colonne Mécanisme | « La contre-régulation autonome puis la neuroglycopénie ; la glycémie tranche… » | Phrases verbales dans les 8 lignes. |
| Moyen | Point 7, définitions Fatigue, Baisse d'appétit, Thermophobie | « La fatigue (asthénie) est un ressenti d'incapacité… » | §11 exige un geste de recherche concret pour chaque signe : ajouter la question ou le geste (échelle, pesée, entretien). |
| Moyen | Point 1, tableau, colonnes « Terme à éviter » | « « Transpiration nerveuse » sans évaluation. » ; « « Sueurs banales ». » | Phrase verbale (« Le médecin évite l'expression … »). |
| Léger | Point 14, réponse CHUV/ESE | « Après 45 ans, le tableau typique suffit (ESE 2025). » ; « SSED/SSML 2025 » ; « CG055 » ; « IP suisse lue » | Développer SSED/SSML, CG055 et IP (information professionnelle) au point d'emploi dans ces points ; ESE est développé plus haut. |
| Léger | Point 6, fenêtre Auscultation | « (CEP 2009) » | Développer CEP. |
| Léger | Point 5, 6 et 14, tournures « Piège : traiter le signe sans mesurer la glycémie. » | Phrases infinitives | Verbe conjugué (« Le piège consiste à traiter… »). |
| Léger | Points 5, 6, 7 | « n'exclut pas / n'exclut ni » (≥ 10 occurrences) | Varier ou supprimer les redites (zéro répétition). |

Aucune correction Critique ni Grave. Aucune phrase coupée par une fenêtre constatée dans les points 1, 5, 6, 7, 13. Sources : aucune vérification médicale faite ici (hors périmètre).

## 4. Décision

Score 82,1 % < 90 %. Critique : 0. Refus selon §12.2 : retour au rédacteur avec les lignes à 1 ci-dessus.

**Question finale (« Vial peut-il gagner 90–100 % des points et traiter ce patient en sécurité ? ») : NON** pour la forme, tant que les phrases non verbales et les abréviations ne sont pas corrigées.
