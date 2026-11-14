# Corrections de l'audit PHY-S5 à PHY-S8 (tour 1)

Auteur : Claude, posture médecin expert et expert-web, 14.11.2026. Objet : les 33 fiches `physiologie/PHY-S5-1` à `PHY-S8-10`, régénérées par le script de rédaction. Statut des fiches : « corrigé tour 1 (AUDIT_PHY_S5_S8), prêt pour contre-audit ».

## Grave

| N° | Fiche | Correction appliquée |
|---|---|---|
| 1 | S7-3 | La valeur devient « hausse ≥ 60 % en 48 h (doublement en moyenne) ». L'`usage` dit qu'une hausse < 60 % ou une baisse **fait suspecter**, sans la prouver, une grossesse non évolutive ou extra-utérine. Il ajoute que l'hCG ne localise pas la grossesse, qu'une grossesse intra-utérine viable peut monter moins vite et que la décision repose sur l'échographie et la clinique (HUG brochure GNE ; source européenne : NICE NG126, seuil de 63 %). L'`exemple` se termine par « on recontrôle l'hCG et l'on refait l'échographie avant tout méthotrexate ». La cible « méthotrexate » précise : « jamais sur la seule cinétique de l'hCG ». La source NICE est ajoutée : lue par l'auditeur, bloquée (403) lors de ma relecture. |

## Moyens

| N° | Fiche | Correction appliquée | Source |
|---|---|---|---|
| 2 | S8-3 | Le seuil de 550 nmol/L est daté et rattaché à un ancien dosage. Avec Elecsys Cortisol II (Roche cobas, dosage de l'Insel), les seuils sont de 426 nmol/L à 30 min et de 485 nmol/L à 60 min ; on demande le seuil propre au laboratoire. | Okutan S. et al., Endocrine 2024;85:321-30, PMC11246257 (source européenne, Danemark), texte intégral lu le 14.11.2026. Aucun seuil suisse publié pour ce dosage n'a été trouvé. |
| 3 | S8-4 | Le RAR ne s'interprète que si l'aldostérone dépasse 240 pmol/L et si la rénine est remontée au-dessus de son plancher. | SFE/SFHTA/AFCE 2016 (source européenne), via EX-1-S8-renine-aldosterone |
| 4 | S6-6 | La formule du trou corrigé pour l'albumine est ajoutée : trou + 0,25 × (40 − albumine en g/L) (non vérifié CH). La norme dépend de l'automate. | déduction |
| 5 | S5-5 | L'étape pancréatique est ajoutée : les protéases pancréatiques dégradent l'haptocorrine au duodénum, puis le facteur intrinsèque fixe la B12. Le dérèglement « insuffisance pancréatique exocrine (malabsorption de la B12) » est ajouté. | HUG, SMPR, « Déficit en vitamine B12 », 2013 (tableau 1), texte intégral lu |
| 6 | S7-4 | Le renvoi « thrombose → PP-S7-Ia » est remplacé par PP-S7-V. **Il manque une fiche PP « MTEV de la grossesse » : à créer.** | index PP |
| 7 | S7-4 | La ligne « seuils propres à la grossesse (anémie, créatinine, PA) : à vérifier, aucune source SSGO lue (non vérifié CH) » est ajoutée. | — |
| 8 | S5-4 | Pour l'agoniste du FXR : depuis le 20.08.2025, Swissmedic recommande de ne plus traiter de nouveaux patients par l'acide obéticholique (COBALT négatif) ; les agonistes PPAR forment l'alternative de deuxième ligne. | Swissmedic, HPC Ocaliva, 20.08.2025, lu |
| 9 | S8-9 | L'unité du lactate devient « mmol/L (HUG CHIMURG imprime µmol/L ; mmol/L par déduction) ». | EX-1-S6-equilibre-acide-base |
| 10 | toutes | Des sources lues sont ajoutées là où une porte s'est ouverte : HUG B12 2013 (S5-5), Swissmedic (S5-4), RMS 2005 « Le spot urinaire » (résumé ; S6-4, S6-5), Okutan 2024 (S8-3), NICE (S7-3, via l'auditeur). Le champ `honnetete` le dit ; les autres mécanismes gardent l'étiquette « déduction ». | Portes essayées sans succès : RMS 2016 (timeout), PDF RMS 8 557 (timeout), HUG stratégie B12 2022 (503), Springer (redirection). |

## Légers (11 à 30)

Toutes les corrections légères sont appliquées selon le patch de l'audit :

- définition de S5-1 ;
- mnémotechnique « 1972 » ;
- facteur V « dès 3 mois » ;
- C. difficile (toxines A et B) opposé au choléra et aux ETEC (AMPc, CFTR) ;
- endométriose renvoyée vers PP-S7-F et léiomyomes vers PP-S7-T ;
- « fait proliférer » ;
- action de l'antagoniste de l'aldostérone sur la kaliémie ;
- surestimation du DFG par la clairance de la créatinine ;
- GOLDMARK à la place de MUDPILES ;
- effet du vaptan dans la polykystose ;
- « oligo- ou azoospermique » ;
- critère ESHRE 2024 de l'insuffisance ovarienne prématurée (≥ 4 mois, FSH > 25 U/L, via EX-1-S7-fsh-lh) ;
- S7-7 : utérotonique donné « en même temps » que l'appel à l'aide, et ligne « durées du travail : non vérifié CH » ;
- traitement du Conn selon que l'atteinte est bilatérale ou unilatérale ;
- GLUT1 chez l'humain ;
- écart de conversion de l'HbA1c dans la source Insel ;
- exclusion de l'hypercalcémie hypocalciurique familiale ;
- COMT et métanéphrines opposées à MAO et acide vanillylmandélique ;
- sudation persistante sous bêtabloquant ;
- SY-80 (anaphylaxie) placé en passerelle sémiologique, car aucune fiche PP ne le couvre ;
- S5-7 : la chaîne devient « source → conjugaison → excrétion » ;
- nomenclature 2022 « déficit ou résistance en arginine-vasopressine » (S6-3, S8-1).

## Validation

- Script de validation : 33 fiches, 0 erreur (schéma, renvois PP, EX, PH et « via » existants, aucune dose).
- `verbal.py` signale encore 324 phrases sur 876. Les fiches PP déjà auditées en comptent autant. Ces signalements portent sur des étiquettes (unités, classes, noms d'affection, chaînes, formules, mnémotechniques), puis sur 36 phrases rédigées qui contiennent un verbe conjugué absent du lexique du détecteur (« sécrète », « réabsorbe », « freine »…). Je n'ai trouvé aucune phrase nominale réelle. J'ai reformulé la phrase de réserve sur les doses pour qu'elle passe.

## Tour 2 (AUDIT_PHY_S5_S8_V2)

| Réf. | Fiche | Correction appliquée mot pour mot |
|---|---|---|
| A | S5-5 | Le dérèglement devient « cancer pancréatique (insuffisance pancréatique exocrine, malabsorption de la B12) », avec PP-S5-T et SY-39. **Complément PP à venir : « pancréatite chronique ».** |
| B | S7-4 | `dereglements[2]` devient « maladie thromboembolique veineuse de la grossesse (hypercoagulabilité ; fiche PP dédiée à venir) », avec PP-S7-V et SY-23. La formulation fausse « hémorragie du post-partum, pré-éclampsie : terrain hypercoagulable » est supprimée. **Complément PP à venir : « MTEV de la grossesse ».** |
| C | S7-3 | Statut de la source NICE : « seuil de 63 % vu par l'auditeur dans un résumé de recherche de la page NG126 (14.11.2026) ; page non lue en entier ». |
| D | S8-3 | L'unité du seuil Synacthen précise maintenant l'origine des seuils : 100 volontaires sains danois, 250 µg IV, femmes sous œstrogènes oraux exclues. Ils ne s'appliquent que si l'Insel dose par Elecsys Cortisol II (cobas), ce qui reste à confirmer. Les œstrogènes oraux élèvent faussement le cortisol total. |
| E | toutes | Chaque champ `honnetete` est désormais construit à partir des sources de sa propre fiche marquées « lu » :<br>• S5-4 : HPC Swissmedic ;<br>• S5-5 : HUG B12 2013 ;<br>• S6-4 et S6-5 : RMS 2005, résumé ;<br>• S8-3 : Okutan 2024.<br>Les autres fiches indiquent qu'aucune source n'a été relue. |

Validation : le script de validation passe sur les 33 fiches sans erreur. `verbal.py` signale 324 phrases sur 909. Ce sont des étiquettes et des verbes absents du lexique ; l'auditeur les a jugés non bloquants au paragraphe 4.
