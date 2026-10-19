# Contre-audit documentaire indépendant · G2 · 19.10.2026

Relecteur : agent `contre_audit_g2`, distinct de l'auteur. Périmètre : trois objets de `data/ck/mono/l.json`, `G2` de `data/ck/mono_ssp.json` et les 37 définitions ajoutées à `data/ck/glo.json`, diff clinique du lot seulement. Protocole six rubriques et chronologies du 18.10.2026 relus. Aucun contenu clinique modifié par le relecteur ; aucune validation médicale humaine revendiquée.

## Verdict final après corrections et nouvelle lecture

| Objet | Verdict | Empreinte SHA-256 de l'objet relu |
| --- | --- | --- |
| lymphome-hodgkinien | Accepté documentairement, réserves ci-dessous | `7c9343cd00dc4c44b7ff34c814a31e90168f9b64809e7282d91da789e64d3946` |
| lymphome-non-hodgkinien | Accepté documentairement, réserves ci-dessous | `3ab7c018cb018598829a2c4dec672f1a01f64788dc73529e0d32783f9887ee19` |
| leucemie-aigue | Accepté documentairement après corrections | `f39298d12d86b4cc8bfe6c9cb425d360bfe45711fc25ed0d0705b34bb821c467` |
| SSP G2 | Accepté documentairement après précision de l'origine de masse | `e56f169a97cc431e513a98e0fb261b71c5ecc2074b57df4794028405a7664728` |
| 37 nouvelles définitions, liste dans l'ordre du fichier | Acceptées documentairement après corrections sémantiques | `986d8aa50f803623d8f0dc0776dacc4504f327f1532db6c3939f1e8ad460c061` |

Empreintes calculées par `tools.coordination.calculer.empreinte`. Toute modification ultérieure impose une nouvelle comparaison. Les quatre objets suivent la structure à six rubriques et comportent les deux chronologies : référence avant bilan, premier texte identique à `exp_premier`, actions urgentes indépendantes de la confirmation, simultanéités explicites dans les situations pertinentes. Cette relecture documentaire ne vaut pas validation clinique humaine.

Empreinte du glossaire entier après ces ajouts : `8136647154f81b03a43b6830fee9ce32300f19a01e54ee20c66725f084cd3b8e`. Ce repère d'intégrité n'étend pas le périmètre de l'audit aux 646 définitions inchangées. Comparaison finale des cinq empreintes du tableau avec les fichiers actuels : concordante.

## Corrections demandées puis vérifiées dans les objets actuels

1. Leucémie aiguë : le bilan de lyse est désormais explicité par potassium, phosphate, calcium, urates, créatinine et LDH, avec résultats recherchés.
2. Leucémie aiguë : les soins urgents comprennent désormais antibiothérapie rapide en neutropénie fébrile, prélèvements microbiologiques sans retard des soins, hydratation adaptée et prévention/traitement de l'hyperuricémie selon le risque, surveillance rénale et électrolytique. Aucune dose de l'article n'est transposée. La cytoréduction urgente spécialisée en cas de leucostase est précisée.
3. G2 : exemples de masses non ganglionnaires, territoire drainé et échographie en cas de doute sont désormais présents avec source ORL dédiée, limitée au contexte cervical.
4. Glossaire : suppression des libellés nus « induction » et « consolidation » au profit de termes thérapeutiques spécifiques ; définition de lymphoblastique centrée sur les précurseurs des lymphocytes ; définition de maladie résiduelle centrée sur la persistance tumorale. L'identifiant `tretinoine` est normalisé et la phrase de cytoponction contient un verbe conjugué reconnu.

Fondement : Schiavini et coll., CHUV/USZ, 2025, tableau 1 p.589 et §2.2 p.590–591 pour le bilan et le support métabolique ; §2.4 p.593 pour l'urgence antibiotique. Le §2.3 p.591–593 soutient l'évaluation clinique de la leucostase sans seuil obligatoire de 100 G/L. Les critères intégrés restent fondés sur Onkopedia AML/LAL, plus précis que la phrase générique du même article.

## Appréciation par objet

### Lymphome hodgkinien

La distinction entre forme classique et forme nodulaire est rétablie ; CD30/CD15 sont présentés comme typiques de la première. La biopsie tissulaire est correctement séparée de l'hémogramme et de la TEP-TDM de stadification. L'évaluation d'une compression respiratoire précède la confirmation. Préservation de fertilité et bilan d'organes sont placés avant les traitements concernés sans retarder l'urgence. Les protocoles ne sont pas généralisés au-delà de leur population.

### Lymphome non hodgkinien

L'hétérogénéité est explicite ; l'incidence, les scores, la TEP-TDM et le protocole d'un DLBCL ne sont plus appliqués à toute la catégorie. Le tissu permet la classification, les autres examens évaluent extension et retentissement. Une surveillance spécialisée concerne seulement certaines formes lentes sans indication immédiate ; une forme rapidement progressive ou compressive appelle une orientation accélérée. Remarque rédactionnelle mineure : la consigne « Ne pas étendre R-CHOP » peut être remplacée par une explication clinique de son indication restreinte.

### Leucémie aiguë

Le seuil AML est correctement limité à la lignée et assorti d'exceptions génétiques ; il n'est plus universel à la LAL. L'absence de blastes circulants n'exclut pas la maladie. L'hospitalisation, le traitement des urgences et l'ATRA dès suspicion de forme promyélocytaire ne dépendent pas de la confirmation médullaire ou génétique. La correction de la coagulation est parallèle. Les soins de support et le bilan de lyse demandés sont désormais explicites. Aucun seuil leucocytaire obligatoire ni leucaphérèse systématique n'est imposé.

### SSP G2

La plainte conserve les masses non ganglionnaires ; elle n'est pas réduite aux lymphomes. Le bilan est guidé par l'origine et le contexte, avec orientation urgente d'une leucémie possible et prélèvement adapté d'un lymphome possible. Une cause bénigne n'est pas déduite de la douleur seule ; un suivi est prévu. La source Planète Santé est un ancien outil de triage : elle soutient les alertes et la réévaluation, pas un algorithme spécialisé complet. Les exemples cervicaux et l'échographie sont désormais adossés au Collège ORL archivé ; aucun ancien bilan systématique n'est transposé à toute masse.

### Glossaire : sens et alias des 37 ajouts

Les définitions ont été lues une par une. Aucune définition directement circulaire n'est retenue. Les alias conservés sont des variantes de nombre ou un équivalent univoque dans le sens défini ; ATRA renvoie à la trétinoïne. Le risque concret d'« induction » était présent dans la porphyrie (`induction de l'ALA-synthase`) ; l'application contient aussi des sens anesthésiques et enzymatiques, ainsi que des sens mnésiques de « consolidation ». Les nouveaux libellés spécifiques, sans alias nu, corrigent ce détournement. L'emploi oncologique est annoncé dans les définitions concernées.

Liste vérifiée : `splenomegalie`, `lymphocyte`, `leucemie`, `hematologique`, `lymphoide`, `leucocytaire`, `lymphocytaire`, `sous-type`, `myeloide`, `leucostase`, `uricemie`, `anemique`, `lymphoblastique`, `hematologue`, `extraganglionnaire`, `hemato-oncologie`, `blaste`, `cytopenie`, `cytogenetique`, `immunohistochimie`, `histologie`, `cytoponction`, `cytoreduction`, `fibrinogene`, `syndrome-de-lyse-tumorale`, `pml`, `rara`, `consolidation-therapeutique`, `induction-therapeutique`, `remission`, `maladie-residuelle`, `gonadotoxique`, `preservation-de-la-fertilite`, `tep-tdm`, `cd30`, `cd15`, `tretinoine`.

## Sources ouvertes et relues indépendamment le 19.10.2026

- [Onkopedia Hodgkin, décembre 2023](https://www.onkopedia.com/de/onkopedia/guidelines/hodgkin-lymphom/@@guideline/html/index.html), §2.1, 4, 5.2, 5.3, 6.1 : variantes, tissu, stadification et traitement adapté.
- [Onkopedia DLBCL, décembre 2025](https://www.onkopedia.com/de/onkopedia/guidelines/diffuses-grosszelliges-b-zell-lymphom/@@guideline/html/index.html), §3 et §4.1–4.3 : prélèvement suffisant, typage, extension et préparation ; conclusions limitées à ce sous-type.
- [Onkopedia AML, septembre 2025](https://www.onkopedia.com/de/onkopedia/guidelines/akute-myeloische-leukaemie-aml/@@guideline/html/index.html), §4 et §5.2.1 : présentation et critères selon classification.
- [Onkopedia LAL, mars 2026](https://www.onkopedia.com/de/onkopedia/guidelines/akute-lymphatische-leukaemie-all/@@guideline/html/index.html), §4, §5.2–5.3 : sang éventuellement sans blastes, prélèvement médullaire et distinction LAL/LBL.
- [Onkopedia APL, janvier 2026](https://www.onkopedia.com/de/onkopedia/guidelines/akute-promyelozyten-leukaemie-apl/@@guideline/html/index.html), §1 et §6.1 : ATRA dès suspicion, correction hémostatique parallèle.
- [Ligue suisse, lymphomes hodgkiniens](https://www.liguecancer.ch/a-propos-du-cancer/les-differents-types-de-cancer/les-lymphomes-hodgkiniens), symptômes, examens et facteurs de choix thérapeutique ; pas de période des estimations annuelles fournie.
- [Ligue suisse, diagnostic lymphomes B/T, octobre 2025](https://www.liguecancer.ch/a-propos-du-cancer/les-differents-types-de-cancer/les-lymphomes-non-hodgkiniens/comment-le-diagnostic-de-lymphome-a-cellules-b-ou-a-cellules-t-est-il-etabli/), premiers examens, tissu et choix d'extension adapté.
- [Ligue suisse, traitement lymphomes B/T](https://www.liguecancer.ch/a-propos-du-cancer/les-differents-types-de-cancer/les-lymphomes-non-hodgkiniens/comment-traite-t-on-un-lymphome/), attente surveillée de certaines formes et familles de traitements.
- [CHUV, leucémie aiguë, page 2019](https://www.chuv.ch/fr/hematologie/hem-home/personnel-de-la-sante/maladies-et-traitements/leucemies-aigues-et-chroniques/leucemie-aigue), description et diagnostic ; ne suffit pas pour un protocole actuel universel.
- [Planète Santé, grosseur/ganglion, 20.09.2011](https://www.planetesante.ch/Symptomes/J-ai-une-grosseur-un-ganglion-qui-m-inquiete), questions de triage, évolution et consultation.
- [HUG, lymphome de Hodgkin](https://www.hug.ch/atlas-sante/pathologie/lymphome-de-hodgkin) et [lymphome non hodgkinien](https://www.hug.ch/atlas-sante/pathologie/lymphome-non-hodgkinien), textes pédagogiques ; vidéos non auditées, aucun protocole tiré d'elles.
- [Schiavini et coll., CHUV/USZ, 2025](https://api.unil.ch/iris/server/api/core/bitstreams/32ec80c8-9f43-4c79-b739-a7fb9d65a77e/content), Revue de médecine interne 46:588–593, DOI `10.1016/j.revmed.2025.04.025` ; tableau 1 et §2.2–2.4.
- [Collège français d'ORL, campus archivé, 21.07.2014](https://archives.uness.fr/sites/campus-unf3s-2014/orl/enseignement/adenopathie/site/html/1.html), §1.1–1.5 : interrogatoire, examen, origine de masse et échographie cervicale. Source ancienne limitée à cette orientation ; ses stratégies de bilan systématique ne sont pas adoptées.

## Limites maintenues

Fréquences comparables dans G2 et sex-ratios chiffrés restent À vérifier ; aucun ordre de fréquence n'est certifié. Posologies non révisées via AIPS et non publiées. L'audit clinique documentaire ne remplace ni les contrôles déterministes du responsable, ni la vérification du glossaire et du rendu, ni la CI, ni la validation médicale humaine. Aucune nouvelle faute critique identifiée dans les objets rédigés. Le PDF HUG `260410_lymphomemsd.pdf` est daté avril 2010 ; il n'a pas servi à valider les traitements actuels.
