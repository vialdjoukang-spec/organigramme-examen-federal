# Audit médical agressif — PHY-S9 à PHY-S12 (23 fiches)

Auditeur indépendant, 14.11.2026. J'ai lu les 23 JSON en entier. J'ai confronté chaque valeur normale à la fiche EX citée (`donnees/examens/*.json`), j'ai refait les 9 calculs par script et j'ai testé l'existence des 160 passerelles. Je n'ai lu aucune AIPS : le cache `.cache/aips/` n'existe pas. Aucune dose ne figure dans les fiches (recherche par expression régulière). Je n'ai rien modifié d'autre que ce fichier ; ni commit ni push.

## 1. Contrôles globaux

| Contrôle | Résultat |
|---|---|
| Valeurs normales avec étiquette de laboratoire (Viollier, HUG, Insel, CHUV, SVTM) | **Conformes** aux fiches EX sources, chiffre pour chiffre (CK, myoglobine, Ca, PTH, 25-OH-D, CTX, PINP, Hb, VGM, TCMH, réticulocytes, ferritine, transferrine, CST, B12, holoTC, folates, plaquettes, VPM, Quick, TCA, fibrinogène, D-dimères, prolactine, cortisol, ACTH). |
| Calculs refaits (Python) | **Tous justes** : Ca corrigé 2,40 ; RétA 80 G/L ; CST 13,3 % ; INR 2,0 ; CaO2 19,998 ≈ 20 ; efficacité 75 % ; âge corrigé 4,16 mois ; Wallace 27 % (total 100 %) ; IPS 0,50. |
| Passerelles | **160/160 existent**. En revanche, plusieurs renvoient vers une fiche PP qui ne traite pas l'entité citée (voir M9). |
| Doses | Aucune. |
| Sources | Honnêtes dans leur libellé (« repris de la fiche EX… », « non lu »). Défaut systémique : tous les **mécanismes** reposent sur Guyton et Boron, manuels américains « non lus » (voir M10). |

## 2. Défauts, gravité et PATCH exact

Aucun défaut Critique ni Grave. Il y a 10 défauts Moyens et 9 Légers.

| # | Gr. | Fiche, champ | Extrait fautif | PATCH exact | Source |
|---|---|---|---|---|---|
| M1 | Moyen | PHY-S9-4 `valeurs_normales` | « retard de consolidation… > 3 mois » ; « pseudarthrose… > 6 mois » | `{"parametre":"retard de consolidation","valeur":"délai habituel du site dépassé (variable : semaines au radius distal, mois au tibia)","unite":"(déduction)"}` ; `{"parametre":"pseudarthrose : absence de consolidation sans progression","valeur":"≥ 6","unite":"mois (source européenne : HAS, lu dans un résumé ; FDA : 9 mois)"}` | Aucune source suisse trouvée (Revue médicale suisse, AO) : « > 3 mois » n'a aucune source. |
| M2 | Moyen | PHY-S11-6 `valeurs_normales` | « marche autonome… ≈ 12 (9–18) mois » | `{"parametre":"marche autonome","valeur":"≈ 12 (8,5–20)","unite":"mois ; au-delà de 20 mois, investiguer (Jenni et Rousson, Études longitudinales de Zurich, Kinderspital Zürich, FNS 2013)"}` | Communiqué FNS du 28.03.2013, lu. |
| M3 | Moyen | PHY-S12-3 `formule` | « une valeur < 0,9 signe une artériopathie » ; « 70 ÷ 140 = 0,5, donc l'artériopathie est sévère » | `usage` : « On divise la pression systolique de la cheville par **la plus haute des deux pressions humérales**. Un IPS ≤ 0,90 signe une artériopathie (source européenne : ESC 2024). Un IPS < 0,5 contre-indique la compression ; entre 0,5 et 0,8, on prend un avis spécialisé (CHUV, procédure de soin 16, 22.01.2019). » `exemple` : « La cheville est à 60 mmHg et le bras à 140 mmHg : 60 ÷ 140 ≈ 0,43, donc l'IPS est < 0,5 et la compression est contre-indiquée. » | CHUV `care_process_16`, PDF lu ; ESC 2024 lu dans des résumés seulement. 0,50 se trouve exactement à la frontière : l'exemple actuel est ambigu. |
| M4 | Moyen | PHY-S12-4 `cible_pharmacologique` | « HLA-B*15:02 avant la carbamazépine, chez les patients d'origine asiatique, prévient le SJS et la NET » | « Avant la carbamazépine, on recherche HLA-B*15:02 chez les patients d'origine chinoise Han ou thaïe, car cet allèle prédit fortement le SJS et la NET ; un test négatif réduit le risque sans l'annuler (source européenne : Fachinformation Tegretal, Allemagne ; AIPS suisse Tegretol non lue, À vérifier). » | Fachinfo DE lue dans un résumé. « Asiatique » est trop large (Japon et Corée : HLA-A*31:01). « Prévient » surestime l'effet. |
| M5 | Moyen | PHY-S11-3 `mecanisme[4]` | « le cortisol freine enfin l'hypothalamus, l'hypophyse et l'hippocampe » | « le cortisol freine enfin l'hypothalamus et l'hypophyse ; il agit aussi sur l'hippocampe, qui freine à son tour le noyau paraventriculaire (rétrocontrôle négatif) » | L'hippocampe est un relais inhibiteur, pas une cible freinée. Erreur de chaîne. |
| M6 | Moyen | PHY-S9-1 `mecanisme[4]` | « le relâchement consomme donc aussi de l'ATP, ce qu'illustre la rigidité cadavérique » | « la pompe SERCA recapte ensuite le calcium, et une nouvelle molécule d'ATP détache la myosine de l'actine : le relâchement consomme donc de l'ATP. Sans ATP, les ponts restent accrochés, ce qui produit la rigidité cadavérique. » | La rigidité illustre le détachement, non la SERCA. |
| M7 | Moyen | PHY-S10-3 `cible_pharmacologique` | « inhibent la dihydrofolate réductase, ce que l'acide folique ou folinique compense » | « …inhibent la dihydrofolate réductase. L'acide folinique contourne ce blocage (sauvetage après méthotrexate à forte dose) ; l'acide folique, qui a besoin de l'enzyme, réduit seulement la toxicité du méthotrexate à faible dose. » | L'acide folique ne contourne pas la DHFR. |
| M8 | Moyen | PHY-S12-5 `valeurs_normales` et `mecanisme[0]` | « chute quotidienne ≈ 50–100 » ; « plusieurs années » | `{"parametre":"chute quotidienne","valeur":"30–80","unite":"cheveux/j (HUG)"}` ; `{"parametre":"cheveux en télogène (test de traction : 5–7 sur 50)","valeur":"10–15","unite":"% (HUG)"}` ; anagène : « environ 3 ans chez l'homme et 6 ans chez la femme (HUG) » ; catagène « 2 à 3 semaines (HUG) » ; effluvium « 2–3 mois après l'événement (HUG) ». Source à ajouter : « HUG, UpDates MSD “Chute de cheveux”, Laffitte et Gaspoz, 19.09.2011 (PDF lu le 14.11.2026) ». | PDF HUG lu. |
| M9 | Moyen | Passerelles (plusieurs fiches) | Renvois manquants ou vides | Ajouter : S9-2 → `PP-S4-T` (Lambert-Eaton) ; S10-1 → `PP-S10-T` (Vaquez, JAK2) ; S10-2 → `PP-S9-F` (hémochromatose) ; S10-3 → `PP-S1-F`, `PP-S10-A` (sclérose combinée, Biermer) ; S10-5 → `PP-S10-I` (CIVD) ; S10-6 → `PP-S7-A` (allo-immunisation anti-D) ; S11-4 → `PP-S1-D` (trouble du comportement en sommeil paradoxal). Retirer `PP-S9-A` de S9-2 : cette fiche ne traite pas la myasthénie. | Vérifié par `grep` dans `physiopathologie/`. |
| M10 | Moyen | Toutes, `sources` | « Physiologie de référence (Guyton et Hall, Boron)… (non lu) » | Remplacer, là où un chiffre ou une chaîne est cité, par les sources lues ci-dessous (§ 3). Ailleurs, écrire : « Mécanisme : (déduction), aucune source lue ». | Source américaine non lue = aucune source. |

| # | Gr. | Fiche, champ | PATCH exact |
|---|---|---|---|
| L1 | Léger | PHY-S11-4 `valeurs_normales[0]` | `{"parametre":"durée d'un cycle (4 à 6 cycles par nuit)","valeur":"90–110","unite":"min (HUG, mise à jour 12.02.2026)"}` ; `definition` : « …par cycles de 90 à 110 minutes ». REM « ≈ 20–25 % » : garder « (non vérifié CH) » ; Revue médicale suisse 2007 (narcolepsie) donne 25 %, résumé seulement. |
| L2 | Léger | PHY-S12-2 `valeurs_normales` | `{"parametre":"hypothermie (stade 1 suisse : 35–32 °C)","valeur":"< 35","unite":"°C (Deslarzes, Pasquier et al., CHUV, SJTREM 2016;24:16, lu)"}` ; `{"parametre":"coup de chaleur, avec trouble neurologique","valeur":"> 40","unite":"°C (Revue médicale suisse 2012, coup de chaleur d'effort, lu dans un résumé)"}` |
| L3 | Léger | PHY-S11-3 `regulation` | « (données surtout expérimentales chez l'humain) » → « (données surtout animales ; chez l'humain, données d'observation) ». |
| L4 | Léger | PHY-S10-5 `mnemotechnique` | « la warfarine » → « les AVK (phenprocoumone, acénocoumarol en Suisse) ». La warfarine n'est pas l'AVK de référence en Suisse (statut Swissmedic non vérifié). |
| L5 | Léger | PHY-S10-5 `valeurs_normales[3]` | `"unite": "µg/L FEU (Insel)"` ; préciser l'unité FEU dans la fiche EX aussi. |
| L6 | Léger | PHY-S10-1 et S10-7, Hb | `"parametre": "hémoglobine, homme > 12 ans"` (et femme), comme la fiche EX. |
| L7 | Léger | PHY-S10-7 `mecanisme[2]` | « la ferrochélatase, **de retour dans la mitochondrie**, insère enfin le fer… » |
| L8 | Léger | PHY-S10-6 `lien_clinique` | « Un anticorps irrégulier (anti-Kidd, anti-Kell, anti-D) provoque soit une hémolyse aiguë, soit une hémolyse retardée par réponse anamnestique. » |
| L9 | Léger | PHY-S11-1 `cible_pharmacologique` | « La plupart des antipsychotiques bloquent D2… (l'aripiprazole, agoniste partiel, élève peu la prolactine) ». |

## 3. Valeurs « non vérifié CH » : bilan de la recherche

| Valeur | Source trouvée (statut) | Décision |
|---|---|---|
| Cycle du sommeil | HUG, laboratoire du sommeil, 12.02.2026 (lu) | Patch L1 |
| Cycle du poil, chute quotidienne | HUG UpDates MSD 2011 (PDF lu) | Patch M8 |
| Développement (marche) | Jenni, Zurich, FNS 2013 (lu) ; sourire et angoisse de l'étranger : rien de suisse trouvé (checklists de pédiatrie suisse non extraites) | Patch M2 ; le reste garde « non vérifié CH » |
| Thermorégulation | CHUV et Lausanne 2016 (lu) ; Revue médicale suisse 2012 (résumé) | Patch L2 |
| Consolidation osseuse | Aucune source suisse trouvée (portes : Revue médicale suisse, AO, Wikipédia, revues) ; HAS (résumé) | Patch M1 |

## 4. Pont vers la pathologie : lacunes côté PP (signal, sans patch PHY)

Aucune fiche PP ne traite l'hyperthermie maligne (S9-1), la pseudarthrose (S9-4), le scorbut ni l'Ehlers-Danlos (S9-5, alors que le renvoi pointe vers `PP-S12-D`), la porphyrie (S10-7), la narcolepsie (S11-4), le coup de chaleur (S12-2), ni l'effluvium, la pelade ou l'alopécie androgénétique (S12-5, dont les trois renvois PP sont vides sur ce sujet).

## 5. Score et verdict

| Critère | Note | Raison |
|---|---|---|
| Chaînes et régulations | 1 | Exactes sauf M5, M6, M7 |
| Valeurs et unités | 1 | Les valeurs suisses sont exactes ; M1, M2, M8, L5 et L6 restent à corriger |
| Formules et calculs | 1 | Les 9 calculs sont justes ; l'interprétation de l'IPS est fautive (M3) |
| Pont vers la pathologie | 1 | M9 et les lacunes PP du § 4 |
| Pharmacologie sans dose | 1 | Aucune dose, mais M4 et M7 |
| Sources honnêtes | 1 | Les libellés sont honnêtes, mais les mécanismes ne reposent sur aucune source lue (M10) |
| Phrases verbales | 2 | Le style est conforme ; je n'ai relevé aucune phrase nominale fautive |

**Publiable en l'état : non.** Il faut appliquer M1 à M9, puis remplacer la mention Guyton/Boron dans les fiches patchées (M10). Ensuite, le lot peut passer ; les Légers ne bloquent pas.
