# Contre-audit V2 — PP-S5 à PP-S8 (36 fiches, 172 affections)

Auditeur indépendant, 14.11.2026. Ce contre-audit fait suite à `CORRECTIONS_PP_S5_S8.md`.
Méthode :
- relecture intégrale des 36 JSON régénérés ;
- comparaison avec la version V1 pour isoler les 30 affections ajoutées ou renommées ;
- contrôle des renvois IMG ajoutés dans `recensement.json` ;
- lecture des AIPS de 6 molécules dans files.refdata.ch, le 14.11.2026, aux URL de `aips_corpus_index.json`.

Aucun fichier modifié hors ce rapport ; ni commit ni push.

## 1. Graves et moyens de l'audit V1 : vérification

| Point V1 | État | Constat |
|---|---|---|
| E1 pylore | Corrigé | L'hypokaliémie est rénale et l'acidurie paradoxale est citée. |
| E2 à E7 | Corrigés | Kehr est latéralisé. Myélinolyse et œdème cérébral sont distingués. L'insuline résiduelle est en place. L'herpès est retiré des infections transplacentaires. L'acide folique est nuancé. SY-36 est retiré de l'ovaire. |
| M1 à M8 | Corrigés | Les 30 affections sont présentes. Leur contenu est audité au § 2. |
| S1 méthotrexate GEU | Corrigé | La source et la cible portent « hors indication autorisée ». |
| S2 fiches internes | Corrigé | Les fiches S-xx sont marquées « dépôt interne (non opposable) ». Chaque fiche S7 a au moins une source externe identifiée. |
| S3 à S6 | Corrigés | « lu par la fiche SY-xx, non relu ici » remplace le « lu » hérité. Les sources hors sujet sont retirées. L'origine « international… (dernier recours) » et le champ `recence` sont ajoutés. |
| R1, R2 | Corrigés | Les passerelles PHY sont propres à chaque lettre. Les doublons (colite post-antibiotique, urétrite, HCS de PP-S7-C) sont réduits à un renvoi PP. Toutes les images ajoutées existent et correspondent à leur affection. |
| Cascades, L4, L6 | Corrigés | Les 36 maillons « Normal » sont verbaux. Aucun qualificatif posologique ne reste. Les mnémotechniques sont en français. |

## 2. Affections ajoutées : audit

Les mécanismes, examens et cibles des affections ajoutées sont exacts :
- 21-hydroxylase ;
- 11β-HSD2 saturée dans le Cushing ;
- GNAS et pegvisomant ;
- hypophysite des anti-CTLA-4 et thyroïdite des anti-PD-1 ;
- thromboplastine et CIVD dans l'hématome rétroplacentaire ;
- toucher vaginal contre-indiqué dans le prævia ;
- VEGF dans l'hyperstimulation ovarienne ;
- androgénétique de la môle complète et hCG agissant sur le récepteur de la TSH ;
- NO et VIP dans l'achalasie ;
- opsonines de l'ascite et albumine contre le syndrome hépatorénal ;
- lithium par ENaC et amiloride ;
- macula densa et SGLT2 dans la néphropathie diabétique ;
- collagène α3(IV) dans la maladie anti-MBG ;
- INSL3 dans la descente testiculaire ;
- Listeria naturellement résistante aux céphalosporines ;
- thiamine avant le glucose dans la renutrition ;
- inflammasome NLRP3 et colchicine dans la goutte.

Aucune erreur médicale nouvelle n'a été trouvée. Les défauts restants concernent l'AIPS et les sources.

## 3. Nouveaux défauts et PATCH exacts

| # | Gravité | Emplacement | Extrait | PATCH exact |
|---|---|---|---|---|
| C1 | **Critique** (règle « À vérifier » pour une molécule présente dans le corpus) | PP-S7-T, môle, `cible_therapeutique[1].pourquoi` | « qui répond au méthotrexate (statut AIPS à vérifier) » | « qui répond au méthotrexate (indication AIPS : « choriocarcinome et autres tumeurs trophoblastiques », Methotrexat-Teva onco n° 47999, février 2025) » |
| C2 | **Critique** | PP-S7-Ia, tératogènes, `cible_therapeutique[2].pourquoi` | « (déduction ; à vérifier dans l'AIPS du valproate) » | « … il n'annule pas le risque propre au valproate : « les données disponibles ne mettent pas en évidence d'action préventive de l'acide folique sur les malformations liées au valproate » (AIPS Depakine n° 34734, septembre 2025) ». Ajouter la source `{"ref":"AIPS Depakine n° 34734, septembre 2025, rubrique Grossesse","origine":"Suisse (AIPS)","statut":"lu"}`, puis retirer « Swissmedic… référence précise à identifier ». |
| C3 | **Critique** | PP-S5-Ia, ulcère aux AINS, `cible_therapeutique[1].classe` | « (misoprostol ; statut AIPS en Suisse à vérifier) » | « (misoprostol ; indication AIPS Cytotec n° 46945, février 2026 : prévention des ulcères gastroduodénaux sous AINS au long cours, chez l'arthrosique ou le polyarthritique sévère) » |
| C4 | **Critique** | PP-S6-F, lithiase, `cible_therapeutique[1].classe` | « (tamsulosine ; usage hors indication AIPS, statut à vérifier) » | « (tamsulosine ; hors indication AIPS : « Traitement des symptômes fonctionnels de l'hyperplasie bénigne de la prostate », Tamsulosin-Mepha retard n° 58828, décembre 2023) » |
| C5 | **Critique** | PP-S7-F, SOPK, `cible_therapeutique[2].classe` | « (létrozole ; hors indication AIPS, statut à vérifier) » | « (létrozole ; hors indication AIPS : cancer du sein de la femme ménopausée seulement, Letrozol Accord n° 68655, août 2021) » |
| C6 | **Critique** | PP-S8-T, Cushing, `cible_therapeutique[1].classe` | « (métyrapone, osilodrostat ; statut AIPS à vérifier) » | « (osilodrostat, indication AIPS : « traitement du syndrome de Cushing et d'autres causes d'hypercorticisme endogène », Isturisa n° 67262, janvier 2026 ; métyrapone absente du corpus AIPS suisse) » |
| M1 | Moyen | PP-S5-Tr, `sources` | « American College of Surgeons, ATLS » : source américaine exclusive. | Remplacer par `{"ref":"(source européenne : S3-Leitlinie Polytrauma/Schwerverletzten-Behandlung, DGU, édition à vérifier)","origine":"Europe","statut":"non lu"}`. |
| M2 | Moyen | PP-S6-D et PP-S6-V, `sources` | Le guide KDIGO « Glomerular Diseases » ne soutient ni l'HBP, ni la MRC, ni la néphropathie diabétique, ni les fiches vasculaires. | Dans PP-S6-D : `{"ref":"(source internationale : KDIGO 2024 Clinical Practice Guideline for the Evaluation and Management of CKD)","origine":"international, non européen (dernier recours)","statut":"non lu"}`. Dans PP-S6-V : retirer KDIGO Glomerular. |
| L1 | Léger | PP-S8-Tr, `sources` | Christ-Crain 2019 porte l'origine « Suisse (auteurs) » : une revue internationale n'est pas une source suisse. | `"origine":"revue internationale (auteure bâloise)"` |
| L2 | Léger | PP-S7-V, prævia, `cible_therapeutique[0]` | La césarienne programmée est présentée comme systématique. | « césarienne programmée si le placenta recouvre l'orifice ou en est très proche » |
| L3 | Léger | PP-S7-C, HCS, `cible_therapeutique[0].pourquoi` | « voir PP-S8-C » ne dit pas pourquoi la cible agit. | « elles remplacent cortisol et aldostérone et freinent l'ACTH (détail dans PP-S8-C) » |

## 4. Points restants : bloquants ou non

| Point restant | Bloque ? | Raison |
|---|---|---|
| Sources ajoutées au statut « non lu » | Non | La règle exige une source lue et datée, **sinon** la mention « À vérifier ». L'étiquetage est honnête. À lister comme complément à venir : lecture et datation. |
| « SGGG… référence précise à identifier » (PP-S7-C, -D, -T) | Non | Chaque fiche porte déjà une source externe identifiée : Gravholt 2017, EMAS, ESMO/ESGO. Ces lignes servent de rappel, pas de caution. Elles doivent passer dans un champ `complements_a_venir`, hors de `sources`. |
| « Swissmedic… référence précise à identifier » (PP-S7-Ia) | Non, si C2 est appliqué | L'AIPS Depakine lue la remplace. |
| Passerelle `cours` « LOT correspondant » | Non | Le schéma lui-même utilise ce libellé dans son exemple. Complément à venir : résoudre l'identifiant par le titre du cours. |
| Mécanismes rédigés en déduction d'expert | Non | La mention `honnetete` le déclare. Aucun chiffre n'est avancé. |

## 5. Verdict

| Critère | Note V2 | Raison |
|---|---|---|
| Exactitude physiopathologique | 2 | Les erreurs V1 sont corrigées ; aucune erreur nouvelle dans les 30 ajouts. |
| Exhaustivité | 2 | Les archétypes manquants sont ajoutés. |
| Cibles et « pourquoi » | 1 | Six mentions « à vérifier » subsistent sur des AIPS présentes dans le corpus (C1 à C6). |
| Sources et honnêteté | 1 | Une source américaine exclusive (M1) et une source hors sujet (M2) subsistent. |
| Renvois et passerelles | 2 | Les renvois sont résolus, les passerelles propres à chaque lettre, les doublons réduits. |
| Doses et style | 2 | Aucune dose ; les phrases sont verbales. |

**`audit-ok` : non en l'état. Oui dès l'application des patchs C1 à C6, qui sont des remplacements de chaînes.** M1 et M2 sont à appliquer dans la même passe. Les points Léger et ceux du § 4 vont dans une liste « compléments à venir » et ne bloquent pas.

## Clôture
C1 à C6 et les 2 moyens appliqués mot pour mot après relecture des AIPS (tour 2 du correcteur) : **audit-ok** pour PP-S5 à S8, conformément au verdict « oui après les 6 patchs ». Compléments à venir : sources « non lu », références SGGG/Swissmedic, passerelle LOT, statut de l'amiloride.
