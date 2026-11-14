# Corrections — PHY-S9 à PHY-S12 (suite de AUDIT_PHY_S9_S12.md)

Corrections appliquées le 14.11.2026 aux 23 fiches de `physiologie/`. Ni commit ni push.

| # | Fiche | Correction appliquée |
|---|---|---|
| M1 | S9-4 | Le retard de consolidation dépend du site (variable) et la pseudarthrose survient à ≥ 6 mois (HAS, résumé ; FDA : 9 mois). Ces deux valeurs sont marquées « non vérifié CH ». Le chiffre « > 3 mois », qui n'avait aucune source, a été supprimé. |
| M2 | S11-6 | La marche autonome survient vers 12 mois (8,5–20). Au-delà de 20 mois, on investigue (Jenni et Rousson, Zurich, FNS 2013). |
| M3 | S12-3 | On calcule l'IPS avec la plus haute des deux pressions humérales. Un IPS ≤ 0,90 signe une artériopathie (ESC 2024). Sous 0,5, la compression est contre-indiquée ; entre 0,5 et 0,8, on demande un avis spécialisé (CHUV, procédure 16, 2019). Le nouvel exemple donne 0,43. |
| M4 | S12-4 | On recherche HLA-B*15:02 chez les patients d'origine chinoise Han ou thaïe, car l'allèle prédit le SJS et la NET. Un test négatif réduit le risque sans l'annuler. Source : Fachinfo Tegretal (DE) ; l'AIPS reste À vérifier. |
| M5 | S11-3 | Le cortisol freine l'hypothalamus et l'hypophyse. Il agit aussi sur l'hippocampe, qui freine à son tour le noyau paraventriculaire. |
| M6 | S9-1 | L'ATP détache la myosine de l'actine. Sans ATP, les ponts restent accrochés, d'où la rigidité cadavérique. |
| M7 | S10-3 | L'acide folinique contourne le blocage de la DHFR (sauvetage après méthotrexate). L'acide folique réduit seulement la toxicité du méthotrexate à faible dose. |
| M8 | S12-5 | Selon HUG 2011 : la chute quotidienne atteint 30–80 cheveux/j ; le télogène concerne 10–15 % des cheveux (test de traction : 5–7 sur 50). L'anagène dure environ 3 ans chez l'homme et 6 ans chez la femme, le catagène 2 à 3 semaines. L'effluvium survient 2 à 3 mois après l'événement. |
| M9 | passerelles | On a ajouté PP-S4-T (S9-2), PP-S10-T (S10-1), PP-S9-F (S10-2), PP-S1-F et PP-S10-A (S10-3), PP-S10-I (S10-5), PP-S7-A (S10-6) et PP-S1-D (S11-4). On a retiré PP-S9-A de S9-2. |
| M10 | sources | La mention Guyton/Boron a disparu ; chaque fiche indique désormais « (déduction), aucune source lue » pour les mécanismes. Les sources lues par l'audit ont été ajoutées (HUG 2026 sommeil, HUG 2011 cheveux, CHUV 2016 hypothermie, CHUV 2019 IPS, FNS 2013). |
| L1 | S11-4 | Un cycle dure 90–110 min et une nuit en compte 4 à 6 (HUG, 12.02.2026). Le pourcentage de REM reste « non vérifié CH ». |
| L2 | S12-2 | L'hypothermie commence sous 35 °C (CHUV, SJTREM 2016). Le coup de chaleur dépasse 40 °C (RMS 2012, résumé). |
| L3 | S11-3 | Les données sont surtout animales ; chez l'humain, on ne dispose que de données d'observation. |
| L4 | S10-5 | La mnémotechnique cite les AVK (phenprocoumone, acénocoumarol) au lieu de la warfarine. |
| L5 | S10-5 | Les D-dimères s'expriment en µg/L FEU. La fiche EX n'a pas été modifiée, faute de mandat. |
| L6 | S10-1, S10-7 | Les valeurs d'hémoglobine portent la mention « > 12 ans ». |
| L7 | S10-7 | La ferrochélatase agit de retour dans la mitochondrie. |
| L8 | S10-6 | Un anticorps irrégulier (anti-Kidd, anti-Kell, anti-D) provoque une hémolyse aiguë ou retardée. |
| L9 | S11-1 | La plupart des antipsychotiques bloquent D2 ; l'aripiprazole élève peu la prolactine. |

**Validation.** Les 23 JSON sont valides et toutes les passerelles existent. `verbal.py` signale 10 phrases sur 373, toutes dans le champ `fonction` : ces titres viennent du recensement et restent inchangés.

**Restes.** Les lacunes côté PP du § 4 de l'audit ne sont pas traitées (hors périmètre PHY). Le sourire-réponse, l'angoisse de l'étranger, la proportion de REM et le cycle anagène gardent « non vérifié CH ».
