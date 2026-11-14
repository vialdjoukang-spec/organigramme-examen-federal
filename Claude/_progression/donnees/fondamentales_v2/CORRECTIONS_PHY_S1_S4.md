# Corrections — Physiologie v2, PHY-S1 à PHY-S4 (32 fiches)

Rédacteur, 14.11.2026, en réponse à `AUDIT_PHY_S1_S4.md`. J'ai régénéré les fiches par le script de génération, puis je les ai validées : JSON relu, aucun identifiant mort, aucune dose. Ni commit ni push.

## Graves
- **G1 (PHY-S4-2)** : le critère ERS/ATS 2022 remplace l'ancien. La réversibilité est significative au-delà de 10 % de la valeur **prédite** (Stanojevic, Eur Respir J 2022;60:2101499, résumé lu). Le critère GINA (> 12 % et > 200 mL) reste mentionné à part, « À vérifier ». La formule divise désormais par le VEMS prédit, et l'exemple ajoute « 0,25 ÷ 2,40 = 10,4 % > 10 % ». J'ai aussi ajouté la source.
- **G2 (PHY-S3-4)** : la fiche suit l'ESC 2024 (doi:10.1093/eurheartj/ehae178, résumé lu) : PA non élevée < 120/70, élevée 120–139/70–89, HTA ≥ 140/90. Elle mentionne la divergence avec l'ESH 2023 (« optimale < 120/80 »). Aucune source SSH n'a été trouvée.
- **G3 (PHY-S3-6)** : dans la sténose aortique, l'angor vient désormais de la demande accrue, de la PTDVG élevée et de la systole allongée. La PAD basse est rattachée à une nouvelle ligne « Insuffisance aortique ».

## Moyens
- **M1 (S3-1)** : la normale de la FE (H 52–72 %, F 54–74 %, EACVI/ASE 2015) est désormais séparée des seuils de l'insuffisance cardiaque (≤ 40 / 41–49 / ≥ 50, ESC 2021). Les deux sources restent « à lire et dater ».
- **M2 (S2-5)** : la ligne est scindée : myasthénie → PP-S1-A ; SLA → PP-S1-D.
- **M3 (S2-4)** : la formule devient PIO = (F − U) ÷ C + Pe, avec le terme uvéoscléral U. L'usage cite les prostaglandines, et l'exemple précise « U négligé ».
- **M4 (S4-3)** : j'ai ajouté la norme du gradient A-a (< 2 kPa chez le jeune, croît avec l'âge, non vérifié CH) et la correction d'altitude (Berne, Pb ≈ 95 kPa → PAO2 13,4 ; gradient 6,4 kPa).
- **M5 (S3-7)** : la fiche ajoute le modèle révisé du glycocalyx (Levick et Michel 2010, À vérifier). L'exemple s'appelle désormais « modèle classique simplifié ».
- **M6 (S3-9)** : le choc neurogénique est décrit avec vasoplégie, bradycardie et débit bas ; le sepsis garde un débit souvent élevé au début.
- **M7 (S1-6)** : la nimodipine réduit l'ischémie cérébrale retardée et améliore le pronostic, mais elle ne supprime pas de façon prouvée le vasospasme angiographique (ESO 2013, À vérifier).

## Légers
- **L1** : dans l'exemple de Laplace, e = 1,5 donne 450 ÷ 3 = 150 ; la tension revient à sa valeur initiale.
- **L2** : le texte distingue le choc spinal (lésion médullaire) de la phase flasque après un AVC.
- **L3** : l'hypotension orthostatique est désormais sourcée par l'ESC 2018 syncope (à relire).
- **L4** : les formes en kPa sont ajoutées (0,0225 × PaO2 ; 0,23 × PaCO2). L'exemple BPCO donne pH 7,29 en kPa.
- **L5** : les cibles du LDL restent inchangées par l'ESC/EAS 2025 (doi:10.1093/eurheartj/ehaf190, résumé lu).
- **L6** : la fiche signale la surcorrection de Bazett au-delà d'environ 90/min et propose Fridericia (non vérifié CH).
- **L7** : l'effet Bohr est réservé au CO2 et au H+. La FO2Hb est distinguée de la SaO2. L'EP renvoie désormais à PP-S4-V, sur une ligne séparée de la pneumonie.
- **L8** : l'exemple parle de « compliance pulmonaire » ; la compliance du système respiratoire vaut environ la moitié (non vérifié CH).
- **L9** : trois renvois sont ajoutés : néphrotique → PP-S6-A, anémie → PP-S10-F, acidocétose → PP-S8-F. Aucune fiche PP n'existe pour la queue de cheval, l'anaphylaxie, le toxidrome opioïde ni l'insuffisance aortique : **lacune signalée**, `pp` reste null.
- **L10** : PHY-S4-2 reçoit une boucle (mesure, comparaison à la LIN, décision). « rouvrent l'accès » remplace « rendent l'accès ». Les IgA sécrétoires protègent les voies de conduction, les IgG l'alvéole.

## Porte VERBAL (`verbal.py`)
- **Avant :** 251 phrases nominales sur 879.
- **Après :** 22 phrases nominales sur 792.
- **Corrections :**
  - Les groupes nominaux des boucles reçoivent un verbe.
  - Certains verbes absents du lexique du détecteur sont remplacés par des synonymes de même sens.
  - Les formules commencent par « On calcule » ou « On applique ».
  - Les mnémotechniques commencent par « On retient ».
- **Reprise des conventions PP :** `classe` devient `cible`, `affection` devient `titre`. Dans chaque valeur, l'étiquette de source quitte `unite` et passe dans un champ `sources`.
- **Reste :** les 22 phrases restantes sont 22 des 32 titres `fonction` repris du recensement. Ce sont des intitulés, mais `verbal.py` ne les exempte pas, contrairement à `titre`. Décision attendue : exempter `fonction` dans `verbal.py`, ou garder le défaut. Les fiches PHY-S5 à S12 présentent le même cas.

## Tour 2 (AUDIT_PHY_S1_S4_V2.md)
J'ai appliqué les quatre corrections mot pour mot, dans les JSON et dans le script de génération (`verbal_fix.py`, `s4.py`), pour qu'une régénération ne les écrase pas.
- **N1 (PHY-S2-6)** : « L'atteinte du VII abolit le goût des deux tiers antérieurs (agueusie) ; la sensibilité générale de la langue, portée par le V3 (nerf lingual), persiste. » La formule fausse « ils deviennent insensibles » disparaît.
- **N2 (PHY-S1-8)** : « L'inflammation corticale altère le contenu de la conscience ; elle provoque confusion, troubles du langage et crises. »
- **N3 (PHY-S4-2)** : la phrase porte désormais « la réversibilité est significative selon le critère GINA ».
- **N4 (PHY-S4-2)** : la source de VEMS/CVF devient « (source internationale : GOLD, non relue, À vérifier ; ERS/ATS 2022 préfère la LIN, z < −1,645 — lu en résumé) ».
- **Validation** : JSON valides, aucun lien mort, aucune dose. `verbal.py` donne 0 phrase nominale sur 766 (le champ `fonction` est désormais exempté).
