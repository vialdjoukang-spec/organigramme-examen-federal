# Audit médical agressif : PHY-S5 à PHY-S8 (33 fiches)

Auditeur indépendant, 14.11.2026. Posture : skill `medecin-expert` (sources CH d'abord). Objet : `fondamentales_v2/physiologie/PHY-S5-1` à `PHY-S8-10`.

## 1. Contrôles réalisés

| Contrôle | Méthode | Résultat |
|---|---|---|
| Renvois PP, SY, S, EX, PH, SF | script sur les 33 fiches, puis confrontation aux index `semiologie/`, `physiopathologie/`, `examens/` | Tous les identifiants existent ; 2 renvois PP sont mal choisis (n° 6 et 15) |
| Valeurs normales | comparaison au champ `normal` des 25 fiches EX citées | Toutes les valeurs sont recopiées fidèlement ; la seule perte concerne l'étiquette « déduction » du lactate (n° 9) |
| 13 calculs | recalcul en Python : CST, SAAG, bilirubine libre, trou osmotique fécal, clairance, charge filtrée, osmolalité et trou osmolaire, FENa, trou anionique, ovulation, numération, hausse de l'hCG, terme, RAR, HbA1c, calcium corrigé, natrémie corrigée | **Tous sont justes** (exemples : FENa 0,143 % ; terme le 06.12.2026 ; HbA1c 7 % = 53,0 mmol/mol ; Na corrigée 142) |
| Doses | recherche des motifs mg, UI, g/j | Aucune dose n'apparaît : la règle est respectée |
| Sources | lecture des champs `sources` | Chaque fiche porte « Physiologie classique (déduction), aucune source lue » : l'étiquette est honnête, mais aucun mécanisme ne repose sur une source lue |

## 2. Défauts, gravité et PATCH exact

| N° | Fiche, champ | Extrait fautif | Gravité | PATCH exact | Source |
|---|---|---|---|---|---|
| 1 | S7-3 `formule.usage`, `exemple`, `valeurs_normales[0]` | « une hausse < 60 % en 48 h ou une baisse indique une grossesse non évolutive ou extra-utérine » | **Grave** | `usage` : « Devant un utérus vide, une hausse < 60 % en 48 h ou une baisse **fait suspecter** une grossesse non évolutive ou extra-utérine, sans la prouver : l'hCG ne localise pas la grossesse, une grossesse intra-utérine viable peut monter moins vite, et l'on décide sur l'échographie et la clinique (HUG brochure GNE ; source européenne : NICE NG126, seuil 63 %). » `exemple` : remplacer « la grossesse n'évolue pas normalement : on recherche une GEU » par « l'évolution est suspecte : on recontrôle l'hCG et l'on refait l'échographie avant tout méthotrexate ». `valeur` : « hausse ≥ 60 % en 48 h (doublement en moyenne) ». | NICE NG126 |
| 2 | S8-3 `valeurs_normales[1]` | « ≥ 550 : réponse normale (Zueger, SMW 2014…) » à côté d'une norme Insel cobas 2026 | Moyen | Ajouter : « seuil 2014 établi sur un ancien dosage ; les dosages monoclonaux récents (cobas) imposent un seuil plus bas : demander le seuil propre au laboratoire Insel (non vérifié CH) ». | EX-1-S8-cortisol-acth ; ESE/Endocrine Society 2024 (GIAI) |
| 3 | S8-4 `formule.usage` | « On dépiste l'hyperaldostéronisme primaire par le RAR… » | Moyen | Ajouter : « Le RAR n'est interprétable que si l'aldostérone dépasse 240 pmol/L et si la rénine est remontée à son plancher ; sinon il est faussement élevé. » Ces conditions figurent déjà dans la fiche EX. | EX-1-S8-renine-aldosterone (SFE/SFHTA/AFCE 2016, source européenne) |
| 4 | S6-6 `formule` | « trou anionique = Na − (Cl + HCO3-) » | Moyen | Ajouter à `usage` : « Corriger le trou pour l'albumine : trou corrigé = trou + 0,25 × (40 − albumine en g/L) (non vérifié CH) ; une hypoalbuminémie masque sinon une acidose à trou élevé. La norme dépend de l'automate. » | déduction ; à confirmer (RMS) |
| 5 | S5-5 `mecanisme[3]` | « l'haptocorrine la protège, puis le facteur intrinsèque gastrique la porte » | Moyen | « l'haptocorrine la protège dans l'estomac ; au duodénum, les protéases pancréatiques dégradent l'haptocorrine, et le facteur intrinsèque fixe alors la B12 et la porte jusqu'au récepteur de l'iléon terminal ». Ajouter le déréglement « insuffisance pancréatique exocrine (malabsorption de la B12) ». | déduction |
| 6 | S7-4 `dereglements[2]` | « thrombose (hypercoagulabilité) PP-S7-Ia » | Moyen | PP-S7-Ia ne traite que la thrombose sous contraception. Remplacer par `"pp": "PP-S7-V"`, ou bien signaler la fiche PP manquante « MTEV de la grossesse ». | index PP |
| 7 | S7-4 `valeurs_normales` | seules des valeurs « hors grossesse » sont données | Moyen | Ajouter les seuils gravidiques (anémie, créatinine) depuis une source CH (SSGO), sinon écrire « à vérifier (non vérifié CH) ». Le `lien_clinique` annonce des seuils différents sans en donner aucun. | — |
| 8 | S5-4 `cibles[2]` | « agoniste du FXR … (cholangite biliaire primitive) » | Moyen | Ajouter : « statut d'autorisation à vérifier (Swissmedic non lu ; l'autorisation conditionnelle de l'UE a été retirée en 2024 selon l'EMA, à confirmer) ; les agonistes PPAR forment l'alternative de deuxième ligne ». | à lire : Swissmedic, EMA |
| 9 | S8-9 `valeurs_normales[1]` | « lactate 0,4–1,9 mmol/L (HUG CHIMURG…) » | Moyen | Remplacer l'unité par « mmol/L (HUG CHIMURG imprime µmol/L ; mmol/L par déduction, via EX-1-S6-equilibre-acide-base) ». | EX fiche |
| 10 | Toutes, `sources` | « aucune source lue » pour chaque mécanisme | Moyen (global) | Lire un précis suisse ou européen par système (cours de physiologie UNIGE/UNIL, ou manuel européen daté) et le citer ; à défaut, garder l'étiquette. | — |
| 11 | S5-1 `definition` | « sécrète l'acide chlorhydrique par la pompe H+/K+-ATPase et le facteur intrinsèque » | Léger | « La cellule pariétale du fundus sécrète l'acide chlorhydrique grâce à la pompe H+/K+-ATPase ; elle sécrète aussi le facteur intrinsèque. » | — |
| 12 | S5-6 `mnemotechnique` | « 1972 à l'envers : 10-9-7-2 » | Léger | « Facteurs K : 10, 9, 7, 2 (« 1972 ») ; dans l'ordre croissant : 2, 7, 9, 10. » | calcul |
| 13 | S5-6 `valeurs_normales[2]` | « facteur V ≥ 70 après 3 mois » | Léger | « ≥ 70 % (dès l'âge de 3 mois) ». | EX-1-S5-tp-facteur-v |
| 14 | S5-8 `dereglements[1]` | C. difficile placé sous un mécanisme CFTR-AMPc | Léger | Préciser : « les toxines A et B lèsent l'épithélium (diarrhée inflammatoire) ; le choléra et les ETEC agissent, eux, par l'AMPc et le CFTR ». | déduction |
| 15 | S7-1 `dereglements[3]` | « léiomyomes, endométriose PP-S7-T » | Léger | Séparer : léiomyomes → PP-S7-T ; endométriose → PP-S7-F. | index PP |
| 16 | S7-1 `mecanisme[1]` | « l'œstradiol prolifère l'endomètre » | Léger | « l'œstradiol fait proliférer l'endomètre ». | — |
| 17 | S6-5 `cibles[3]` | « antagoniste de l'aldostérone … ils réduisent l'aldostérone » | Léger | « IEC et sartans réduisent l'aldostérone ; l'antagoniste en bloque le récepteur : tous élèvent la kaliémie ». | — |
| 18 | S6-1 `formule.usage` | clairance U × V ÷ P sans réserve | Léger | Ajouter : « la sécrétion tubulaire de créatinine fait surestimer le DFG, d'autant plus que le DFG baisse ». | déduction |
| 19 | S6-6 `mnemotechnique` | « MUDPILES (… Paraldéhyde …) » | Léger | Remplacer par « GOLDMARK (Glycols, Oxoproline, L-lactate, D-lactate, Méthanol, Aspirine, Rein, Kétones) », car le paraldéhyde n'est plus utilisé. | source européenne à lire |
| 20 | S6-3 `cibles[1]` | vaptan « fait perdre de l'eau libre (… polykystose) » | Léger | « dans la polykystose, il freine l'AMPc qui fait croître les kystes ». | — |
| 21 | S7-2 `lien_clinique` | « elle le rend azoospermique » | Léger | « elle peut le rendre oligo- ou azoospermique ». | — |
| 22 | S7-6 `lien_clinique` | « FSH haute avant 40 ans » | Léger | « aménorrhée ou oligoménorrhée depuis au moins 4 mois et FSH > 25 U/L avant 40 ans (source européenne : ESHRE 2024, à lire) ». | à lire |
| 23 | S7-7 | `valeurs_normales` est vide ; le lien dit « avant tout autre geste » | Léger | Ajouter les durées de travail (non vérifié CH) ; écrire : « on masse l'utérus et l'on donne un utérotonique **en même temps** que l'on appelle à l'aide et que l'on pose les voies ». | — |
| 24 | S8-4 `cibles[0]` | antagoniste MR « traite le Conn » | Léger | « il traite l'hyperaldostéronisme bilatéral ; l'adénome unilatéral relève de la surrénalectomie ». | — |
| 25 | S8-5 `chaine.capteur` | « glucose via GLUT2 » | Léger | « glucose (GLUT1 chez l'humain, GLUT2 chez le rongeur) et glucokinase ». | déduction |
| 26 | S8-5 `valeurs_normales[2]` | « 4,8–5,9 % ; 29–42 mmol/mol » | Léger | Le calcul montre que 5,9 % = 41 mmol/mol et que 42 mmol/mol = 6,0 %. Ajouter « (écart de conversion présent dans la source Insel) ». | calcul |
| 27 | S8-6 `lien_clinique` | PTH haute + hypercalcémie = hyperparathyroïdie primaire | Léger | Ajouter : « on exclut d'abord l'hypercalcémie hypocalciurique familiale (rapport des clairances Ca/créatinine < 0,01) ». | déduction |
| 28 | S8-8 `mecanisme[4]` ; `lien_clinique` ; `dereglements` | « la COMT et la MAO les dégradent en métanéphrines » | Léger | « la COMT les transforme en métanéphrines ; la MAO conduit à l'acide vanillylmandélique ». Ajouter : « la sudation (cholinergique) persiste sous bêtabloquant ». Ajouter le renvoi SY-80 (anaphylaxie). | — |
| 29 | S5-7 `chaine.capteur` | « macrophage splénique » présenté comme capteur | Léger | Cette chaîne est un flux métabolique, non une boucle régulée : la nommer « source → conjugaison → excrétion ». | — |
| 30 | S6-3, S8-1 | « diabète insipide » | Léger | Ajouter la nomenclature 2022 « déficit (ou résistance) en arginine-vasopressine ». | — |

## 3. Score et verdict

| Critère | Note (2/1/0) | Raison |
|---|---|---|
| Chaînes de régulation | 1 | Elles sont justes dans l'ensemble ; S5-5 (B12) est incomplète et S5-7 n'est pas une boucle |
| Valeurs et unités CH | 2 | Elles sont fidèles aux fiches EX ; les mentions « non vérifié CH » sont explicites |
| Formules et calculs | 1 | Les 13 calculs sont justes, mais l'interprétation hCG est abusive et la correction du trou anionique par l'albumine manque |
| Pont vers la pathologie | 1 | Tous les renvois existent ; 2 sont mal choisis |
| Pharmacologie (classe, pourquoi, aucune dose) | 2 | Aucune dose n'apparaît ; le statut d'autorisation du FXR reste à préciser |
| Sources | 1 | L'étiquetage est honnête, mais aucun mécanisme ne repose sur une source lue |

**Bilan : 0 Critique, 1 Grave, 9 Moyen, 20 Léger.** **Prêt pour `audit-ok` ? Non.** Il manque la correction du n° 1 (Grave) et des n° 2 à 9 (Moyen). Les corrections légères peuvent suivre dans le même passage.

Sources ouvertes par l'auditeur le 14.11.2026 : [NICE NG126](https://www.nice.org.uk/guidance/NG126/chapter/diagnosis-of-viable-intrauterine-pregnancy-and-of-tubal-ectopic-pregnancy) (source européenne) ; [ESE–Endocrine Society 2024, GIAI](https://ese-hormones.org/publications/directory/european-society-of-endocrinology-and-endocrine-society-joint-guideline-diagnosis-and-therapy-of-glucocorticoid-induced-adrenal-insufficiency) (résumé seulement). Les fiches EX citées ont été lues localement. Les mentions « à lire » ou « à confirmer » n'ont pas été vérifiées.
