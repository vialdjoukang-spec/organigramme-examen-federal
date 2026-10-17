# HANDOFF Hérophile (auditeur suiveur monographies CK)
Début : 2026-10-17 22:15 (Zurich). Worktree /workspace/oef-herophile (branche audit/herophile).
Lots audités : (aucun)
- Lot 1 (G1, 14 DD, Hygie, PR #46 fusionnée avant audit) : audité depuis main → PR #49 (50 corrections : 8 médicales, 24 sourcing, 18 linguistiques ; 0 critique). Script : hippo_work/fix_lot1.py ; journal lot1_log.json.
- audit/RAPPORT_AUDIT_MEDICAL.md : créé dans PR #49 ; Galien a le même fichier sur audit/galien-prev → conflit add/add au second merge : garder les deux sections.
- Règle linguistique retenue : def/phy/dia/epi en phrases verbales ; cli/exp listes admises ; but/mes/pha à l'infinitif admis.
- Méthode suivante : poll_main.sh (fusions main touchant data/ck/mono, Hygie de G2 en avant, Panacée du dernier groupe en arrière) ; sources vérifiées = `mono_build.py --draft <SSP>` (lignes « src »).
- 22:36 nouveau flux (Vial) : PR des rédacteurs ouvertes SANS fusion ; j'audite, je pousse sur leur branche, puis `gh pr edit N --add-label audit-ok` (fusion auto + Pages). Ne pas fusionner à la main.
- Lot 2 Hygie (G2, 21 DD, PR #50) : 45 corrections poussées sur feat/mono-g2 (worktree /workspace/oef-herophile-h), label audit-ok posé.
- Panacée lot 1 (O7.26–O7.24, 27 DD, PR #51 fusionnée avant audit) : 100 corrections ajoutées à PR #49 (fedlex : CC, LAGH, LPMA, Cst. ; liste suisse des antidotes 2026/2027). Script fix_pan1.py.
- Outils : newmono.py base head (monographies changées), autosrc.py (sources vérifiées TIP.v par DD), rapport_section.py (section du rapport), poll_pr.sh (PR sans audit-ok). pr_seen.txt = PR/sha déjà audités.
- Sources locales : hippo_work/src (cc_1.html, lagh.html, lpma.html, cst.html, antid.txt, tb.txt, …).
- 22:45 répartition : Hérophile = chaîne Hygie seulement ; Érasistrate = Panacée (#51 déjà audité dans #49, noté au rapport).
- Lot 3 (#53, G3+G4, 24 DD) : 47 corrections poussées (worktree oef-herophile-h3). Lot 4 (#54, G5+G6, 32 DD) : 51 corrections poussées (worktree oef-herophile-h4, branche locale herophile-g5 → push HEAD:feat/mono-g5 car Hygie occupe feat/mono-g5 dans /workspace/wt_hygie).
- #50 : main fusionnée (shards fusionnés clé par clé par merge_shards.py, assets/mono régénérés, assets/ck/mono-* retirés), label audit-ok.
- Labels audit-ok NON posés sur #53 et #54 : ordre imposé #50 → #53 → #54 ; à poser dès que #50 (puis #53) est fusionnée, après fusion de main et mono_build.
- BLOQUANTS : (1) auto-fusion.yml échoue : `gh pr merge --auto` sans checkout ni GH_REPO (« not a git repository ») ; (2) les commits de fusion du bot déclenchent des CI « action_required » (contourné sur #49 par un commit vide) ; (3) visuel en échec sur #53.
- Session 2 (23:01) : poll_h2.sh (Hygie seul + fusions #49/#50/#53/#54 ; seen_hygie.txt, merged_seen.txt).
- Lot 5 (#64, G7+G8, 25 DD) : 22 corrections poussées sur feat/mono-g7 (worktree oef-herophile-h5, branche locale herophile-g7) ; rapport dans #49. Doses citées conformes à doses_ch (#59/#61). Label NON posé : ordre #50 → #53 → #54 → #64.
- 23:05 état : auto-fusion cassée (#63 en cours), visuel rouge sur #50/#53/#54 (Iris) ; toutes BEHIND main.
