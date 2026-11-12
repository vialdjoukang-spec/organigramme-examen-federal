# Audit médical A — LOT_025 Phase A V0 (SSP S1.9)

| Élément | Valeur |
|---|---|
| Fichier | `LOT_025_Phase_A_V0.html` · 81 427 octets · SHA-256 `d7a8b0b6ff0232fac82d05e119755bbc217a56b39e65aa9c27c1266f426b4d78` |
| Date | 12.11.2026 · auditeur médical A (points 2, 3, 4, 8, 9, 11, 12) |
| Rapport mécanique | `controle_lot.py verifier` : 1 critique (script, image ou feuille de style externe), 1 avertissement (mention « non validé cliniquement » absente). Non refait. |
| Sources relues | dl25b/ (SSI 2408 v24612, Paediatrica 2023, HUG ORL 2019, HUG aphtes 2011, HUG affections buccales 2025, HUG soins de bouche 2024, Ligue Sjögren, SSORL, CHUV ×2, Miranda-Rius, Sørensen, Kontogiannopoulos, Scully résumé) ; dl25/ (extraits fréquences, OFS 2021) |
| AIPS | Corpus `AipsDownload_20261008.xml` indexé (10 177 entrées fr) ; monographies HTML lues : Salagen 55901, Daktarin Gel oral 43494, Kenacort-A Orabase 35039, Dermovate 39905, Betnesol 30120, Plaquenil 53831, MabThera 54378, Benlysta 61532, Mycostatine 33043, Bucco Tantum 39997, Augmentin 45674, Dalacin C 35438 |
| Calculs refaits (Python) | DX.9 : (791 + 372) / 8,33 M ≈ 14,0 / 100 000 / an (calcul dérivé, population approximative) ; Sjögren 3,8/10 000 ≈ 1/2 632 ; gingivostomatite 1/303 = 0,33 % des passages, 372/702 = 53,0 % herpétiques. Chiffres du cours exacts. |

## Score §12.2 (points audités)

| Point | Notes (Q) | Score | Raison principale |
|---|---|---|---|
| 2 | Q2.1 1 · Q2.2 1 · Q2.3 1 · Q2.4 1 | 4/8 | Données suisses limitées au cancer ; coût absent ; un chiffre mal attribué (n° 8) |
| 3 | Q3.1 1 · Q3.2 1 · Q3.3 1 · Q3.4 1 · Q3.5 2 | 6/10 | Tableau « Siège / Mécanisme / DX » sans colonnes Exploration ni Thérapeutique |
| 4 | Q4.1 2 · Q4.2 1 | 3/4 | E1 a son piège ; E2 sans piège explicite |
| 8 | Q8.1 1 · Q8.2 1 | 2/4 | Centor SSI 2024 présent ; aucun critère ACR/EULAR (Sjögren) ; « ce qui ne suffit pas » faible |
| 9 | Q9.1 0 · Q9.2 1 · Q9.3 1 · Q9.4 1 · Q9.5 1 · Q9.6 0 | 4/12 | Pas de gold standard ni 9.a–d ; aucune alternative (grossesse, enfant) |
| 11 | Q11.1 0 · .2 1 · .3 1 · .4 1 · .5 0 · .6 1 · .7 0 · .8 0 · .9 1 · .10 0 · .11 1 | 6/22 | Aucune spécialité, dose, numéro Swissmedic, CI ni interaction ; ni grossesse ni insuffisances ; ni but ni sortie |
| 12 | Q12.1 1 | 1/2 | Trois niveaux présents ; aucune recommandation suisse datée ; vaccination HPV absente |
| **Total** | | **26/62 = 41,9 %** | **Refusé (< 90 %, critiques présentes)** |

## Corrections

| N° | Classe | Emplacement · extrait exact (≤ 200 car.) | Correction · source |
|---|---|---|---|
| 1 | bloquante (Critique) | 11, fenêtre Aphtes · « le clobétasol et la bétaméthasone en bain de bouche, dont la dose se lit dans l'AIPS de chaque produit » | Faux : Dermovate® (39905) vise les dermatoses cutanées ; Betnesol® (30120) n'a aucune indication buccale. Écrire « usage hors AIPS (off-label), sans dose AIPS ». Source : AIPS 39905, 30120 ; HUG aphtes 2011 (Dermovate® crème). |
| 2 | bloquante (Critique) | 11, fenêtre Aphtes · « Les HUG citent la triamcinolone en pâte adhésive » | Ajouter : Kenacort®-A Orabase (35039), ½ cm 2–3×/j ; **contre-indiqué** en cas d'infection mycosique ou bactérienne buccale et de gingivite herpétique primaire. Ces cas recouvrent DX.3 et DX.6. Source : AIPS 35039. |
| 3 | bloquante (Critique) | 11, fenêtre Candidose · « par nystatine ou miconazole en gel oral » | Ajouter les CI de Daktarin® Gel oral (43494) : nourrisson < 4 mois, insuffisance hépatique, simvastatine, atorvastatine, lovastatine, midazolam oral, triazolam, allongeurs du QT, ergotamine. Ajouter aussi : grossesse seulement en cas de nécessité absolue. Source : AIPS 43494. |
| 4 | majeure (Grave) | 11, Urgence APA · « par amoxicilline-acide clavulanique ou clindamycine » | Molécules sans renvoi AIPS. Ajouter spécialité, numéro (ex. Augmentin 45674 ; Dalacin® C 35438), dose et voie IV lues dans l'AIPS. Le même défaut touche pénicilline V, amoxicilline, céfuroxime, clarithromycine, nystatine, fluconazole, lidocaïne et benzydamine (Q11.5). |
| 5 | majeure (Grave) | 11, Bouche sèche · « La pilocarpine stimule les récepteurs M3 ; sa prescription suit son AIPS » | Salagen® (55901) est indiqué seulement pour la xérostomie grave post-radiothérapie ORL et la xérostomie du Sjögren : il est hors AIPS dans la xérostomie médicamenteuse. Citer aussi 5 mg 4×/j, l'arrêt sans effet à 2–3 mois, l'asthme non maîtrisé et une ClCr < 10 mL/min (CI), ainsi que le texte grossesse et allaitement. |
| 6 | majeure (Grave) | 11, Sjögren · « l'hydroxychloroquine, du méthotrexate, de la cortisone, du mycophénolate mofétil, du rituximab ou du bélimumab » | Signaler « hors AIPS en Suisse pour la maladie de Sjögren ». Plaquenil® 53831 couvre PR, lupus, photodermatoses et paludisme ; MabThera® 54378 n'a aucune indication Sjögren ; Benlysta® 61532 couvre seulement le LED et la néphrite lupique. |
| 7 | majeure (Grave) | 9 TDR et 11 Situations spéciales · « antécédent de rhumatisme articulaire aigu ou migration récente justifient un test systématique dès un score de 3 » | Paediatrica : « Des antécédents de RAA justifient un Strepto-test **quel que soit le score de Centor** ». La migration doit venir « d'un pays en développement ». Source : S3. |
| 8 | majeure (Grave) | 2, Limites · « Chez les hommes de 71 à 92 ans au Royaume-Uni, 31 % … 20 % … S26 » | Chiffre mal attribué : il vient de Ramsay SE et al., BMJ Open 2015;5:e009476 (doi:10.1136/bmjopen-2015-009476). Sørensen 2018 étudie des hommes danois. Ajouter la référence ou supprimer la phrase. |
| 9 | majeure (Grave) | 11, Carcinome · « Les récidives dépassent 75 % des cas durant les deux premières années » | Contresens. Écrire « Plus de 75 % des récidives surviennent durant les deux premières années ». Source : HUG ORL 2019 (« Récidives : > 75 % les deux premières années »). |
| 10 | majeure (Grave) | 9 Sjögren et 8 tableau · « la biopsie des glandes salivaires de la lèvre confirme l'atteinte glandulaire » ; « Schirmer » dans « Ce qui confirme » | La Ligue précise que le Schirmer « ne suffit pas » et que l'inflammation labiale existe sans auto-immunité « jusqu'à 10 % des cas ». Remplacer « confirme » par « soutient » et ajouter les critères ACR/EULAR datés, après lecture de leur source. |
| 11 | majeure (Grave) | 12 et 14 · « une tuméfaction glandulaire nouvelle peut révéler un lymphome S8 » ; « parotide qui gonfle … Un lymphome » | Phrase non soutenue par S8. La Ligue cite des ganglions gonflés récents, des sueurs nocturnes, une perte de poids et une fatigue inhabituelle. Il faut citer ces signes ou une source qui lit la parotide. |
| 12 | majeure (Grave) | 3, 8, 10, 13 · « un obstacle canalaire fait gonfler la glande au moment des repas S6 S9 » ; « Si une glande gonfle au repas » | Ni S6, ni S9, ni S12 ne mentionnent le rythme prandial, signe clé de DX.10. Ajouter une source lue. « Imagerie » (DX.10, S9) n'est pas non plus dans S9. |
| 13 | majeure (Grave) | 11.A–11.D · « 11.A — Urgences » … « 11.D — Situations spéciales » | La structure V0 attend A But, B Moyens (urgences, AIPS, situations spéciales), C Surveillance et D Pronostic/guérison. Réaffecter les blocs et ajouter le but et le pronostic. |
| 14 | majeure (Grave) | 11, Situations spéciales (4 items) | Ajouter grossesse et allaitement (texte AIPS Daktarin et Salagen non adouci), sujet âgé polymédiqué, insuffisance hépatique (CI Daktarin) et insuffisance rénale (CI Salagen ClCr < 10). |
| 15 | majeure (Grave) | 8, « Les dix diagnostics retenus » (colonnes Orientation / Ce qui confirme / Vigilance) | Le Bloc 2 V0 exige les colonnes signe clé, examen qui tranche, **mécanisme**, **conduite immédiate** et **rang E**, plus une justification de chaque DX (entrée et rang). Les compléter. |
| 16 | majeure (Grave) | 10, Arbre décisionnel | Aucune branche pour DX.5 (ulcère au contact d'un agent blessant → correction puis contrôle à 3 semaines) ni pour DX.6 (petit enfant fébrile, gencives). Les ajouter. |
| 17 | mineure | 8, Hors liste · « Le lichen plan buccal et la leucoplasie … S14 » | Mauvaise source : Scully (résumé lu) ne les cite pas. Citer S5 (lichen plan) et S4 (leucoplasie, états précancéreux). |
| 18 | mineure | 8 tableau DX.5 · « Guérison après correction S14 » | Non présent dans S14. Citer une source lue ou retirer. |
| 19 | mineure | 9 TDR · « Indication : un score de Centor de 3 à 4, chez l'enfant de plus de 3 ans » | La SSI pose l'indication antibiotique « adultes et enfants » avec un TDR positif. Préciser que le TDR concerne aussi l'adulte. Source : S2. |
| 20 | mineure | 4 · « car un antibiotique seul ne vide pas l'abcès S4 » ; « Erreur du débutant : appliquer le score de Centor… S2 S4 » ; « Avis ORL urgent » | Déductions présentées comme sourcées (S4 ne les dit pas). Les marquer comme raisonnement. |
| 21 | mineure | 11, Pharyngite · « Le pédiatre prévoit donc un contrôle à 72 heures » | Il s'agit de la vignette clinique de S3. La règle générale est une réévaluation à 48–72 h sans critère d'inquiétude. |
| 22 | mineure | 3 · « la xérostomie peut toucher 70 % des adultes qui prennent un traitement S12 » | Chiffre de seconde main (réf. 24 de S12), discordant avec S15 (32,1 %). Commenter l'écart. |
| 23 | mineure | 2 · « les rangs 2 à 7 indicatifs » | DX.7 (prévalence) et DX.8–10 (incidences) ne sont pas comparables non plus. Étendre la réserve. DX.9 ≈ 14,0/100 000 (calcul dérivé) contre DX.10 7,27–14,10 : écart faible. |
| 24 | mineure | 2 · « Les aphtes touchent 10 à 20 % de la population » | S5 écrit « Incidence 10–20 % » et « Prévalence 1 % ». Garder le terme et la prévalence. |
| 25 | mineure | 8 · « La forme herpétiforme … petits ulcères de 2 à 8 mm » | La mise en page de la diapositive S5 est ambiguë. Vérifier ce chiffre ou le retirer. |
| 26 | mineure | 12, prévention primaire | Ajouter la vaccination HPV (OFSP, plan de vaccination de l'année en cours, à lire) et une recommandation suisse datée pour chaque niveau. |
| 27 | mineure | 8 tableau DX.2 · « Lien chronologique et revue des traitements S6 » | S6 ne parle pas de lien chronologique. Reformuler ou sourcer. |
| 28 | mineure | Sources S4 (2019), S5 (2011) | Supports d'enseignement anciens. Signaler leur date dans le texte quand ils fondent une conduite (APA, aphtes). Taux suisse de consultation pour pharyngite : rester « À vérifier ». |

Hors périmètre, observé : les titres internes de Phase B divergent de la liste gelée (`DX.10.html` → « DX.8 — Sialolithiase… », `DX.2.html` → « DX.6 — … »). C'est une erreur critique de lot (§16).

## Question finale

**Non.** Vial ne peut pas traiter ce patient en sécurité avec ce texte. Les contre-indications AIPS manquent (Orabase sur herpès ou mycose, interactions de Daktarin). Deux usages hors AIPS sont présentés comme documentés dans l'AIPS. Le seuil de test chez l'enfant aux antécédents de RAA est faux. Le cours n'a ni spécialité, ni dose, ni numéro Swissmedic, ni texte grossesse/allaitement. Il manque aussi 11.A–D conforme, le tableau comparatif complet et les branches DX.5/DX.6.
