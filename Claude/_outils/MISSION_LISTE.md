# MISSION LISTE — étapes E2–E3 d'un LOT (posture : IA de haut niveau de raisonnement, prompt A-2)

Lis d'abord `Claude/_outils/BRIEF_REDACTION.md` (environnement, sources, outil lecon.py). CIBLE = PA.
1. Constitue les sources de la Phase A (étape 1 du brief, 10–15 URL, Suisse puis Europe ; résumés PubMed via
   `https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&id=<PMID>&rettype=abstract&retmode=text`),
   puis `prep --cible PA` (sans --dci).
2. Établis, à partir des seuls passages lus, les dix diagnostics différentiels qui concurrencent réellement la SSP :
   fréquence décroissante en Suisse (Europe à défaut), chaque rang justifié par un ID de passage ; DX graves 🚩 avec rang
   d'exclusion E1, E2… (un grave rare garde son rang de fréquence) ; ni doublon déguisé, ni fourre-tout, ni hors-sujet.
   Pour une SSP transversale (éthique, droit, communication, prévention, contraception, conception) : dix scénarios gradués (µ8).
3. Écris dans le worktree :
   - `Claude/LOT_XXX/_travail/PA/liste_dx.json` : {"critere_ordre":"…","dx":[{"rang":1,"nom":"…","grave":false,"E":null,"justification":"phrase verbale","citations":["ID"]}…]}
   - `Claude/LOT_XXX/LISTE_DX_BROUILLON.md` : une ligne `DX.<i> — <nom exact>` (+ ` 🚩 E<n>`) par DX.
   - `Claude/LOT_XXX/_travail/PA/dci.txt` : `PA: racines…` puis `DX.i: racines…` (DCI probables de la prise en charge).
4. Ne rédige pas la monographie. Ne commite rien. Réponds en ≤ 15 lignes : liste (rang, nom, 🚩/E), critère d'ordre,
   arbitrages à trancher par l'audit P1, sources principales.
