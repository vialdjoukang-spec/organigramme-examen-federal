Rédige UN fichier Phase B de LOT_014 — SSP PROFILES G14 « Décès inattendu ou mort subite | unexpected or sudden death » (chaque DX est une cause de mort subite ou inattendue, monographie clinique 14 points, Prompt V0 §11). LOT VIDE : fabrication.

Dépôt : /home/user/organigramme-examen-federal (branche production-v2 ; AUCUN commit ni push, la session principale s'en charge). Dix rédacteurs travaillent en parallèle dans le même dossier `lot en cours de production/LOT_014/` : tu n'écris QUE les fichiers nommés ci-dessous.

Lis d'abord : `LECONS_LOT_013.md` (leçons du lot précédent, obligatoires), `LISTE_DX_CANONIQUE.md` (GELÉE), `CORRECTIONS_AUDIT.md` (corrections d'audit à hériter sans exception), `evidence/INDEX.md` (26+ sources déjà lues, réutilise-les), `HELP.md` ; puis Prompt V0 §10–14 et §9.3 (`PROMPT_Casern/PROMPT_ULTIME_PRODUCTION_LOTS_V0.md`). Pour la cohérence avec la Phase A, extrais seulement ce qui concerne ton scénario : `python3 harnais/controle_lot.py extraire "lot en cours de production/LOT_014/LOT_014_Phase_A_V0.html" --points 1,2,3` et cherche ton DX dans le tableau comparatif (`grep -n`).

Livrable : `lot en cours de production/LOT_014/LOT_014_Phase_B_V0_DX.<N>.html`
- HTML5 autonome, 80 000–150 000 octets (bornes comprises ; vise ≈ 100–120 Ko, densité sans remplissage).
- `<h2>DX.<N> — <nom exact de la liste canonique></h2>` mot pour mot ; une seule monographie `<section class="monograph" id="dx<N>">` avec 14 titres `<h3 id="dx<N>-p1">`…`dx<N>-p14` (plan §11 transposé §9.3).
- Grandes fenêtres = API `popover` (§14.2) : bouton `popovertarget` dans la phrase, `<div id="dx<N>-…" popover class="fenetre">` APRÈS le `</p>`, bouton Fermer ; ids préfixés `dx<N>-` et uniques ; aucun JavaScript, aucun `title=`, tableaux enveloppés `overflow-x:auto`, lisible à 390 px.
- Phrases verbales courtes ; abréviations développées ; sources [S1]…[Sn] propres au fichier (titre, organisme, année, URL, date de consultation) ; mention « Contenu établi à partir des sources citées ; non validé cliniquement par un médecin. » ; dernière ligne `<!-- FIN_FICHIER LOT_014_Phase_B_DX.<N> -->`.
- Sources suisses d'abord (Fedlex avec date d'état, cantons, OFS, OFSP, BPA, SGRM/SSML, IRM, CURML, ASSM, Tox Info Suisse), puis Europe ; jamais une source américaine exclusive ; aucune donnée de mémoire. Donnée introuvable = « donnée non trouvée dans les sources consultées ».
- Doses : uniquement d'après le corpus AIPS local `.cache/aips/AipsDownload_20261008.xml` (grep ciblé, jamais ouvert en entier ; numéro Swissmedic lu ; extrait en cache `.cache/aips/<numéro>.txt`). Molécule absente du corpus et de swissmedicinfo.ch = « À vérifier (AIPS) » sans dose.

Fichiers annexes autorisés (pour éviter les collisions) : nouvelles sources dans `evidence/DX<N>_*.txt` ; hypothèses dans `JOURNAL_DX<N>.md` ; lacunes dans `HELP_DX<N>.md`. Ne modifie PAS `evidence/INDEX.md`, `HELP.md`, `JOURNAL.md`, ni aucun autre fichier.

Après écriture : `python3 harnais/controle_lot.py verifier "lot en cours de production/LOT_014" --sans-nom --json` et corrige toute critique portant sur TON fichier ; `wc -c` pour la taille. Rédige par blocs (anti-troncature §14.5). N'attribue aucun score. Réponse finale ≤ 15 lignes.
