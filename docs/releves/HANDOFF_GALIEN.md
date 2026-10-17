# Relève Galien · 17.10.2026 ~22:00 (Europe/Zurich)
## Fait
- PR #39 (feat/galien-nc07-revue) : main fusionnée (71a1d2d ; glo.json par union d'identifiants, aucun doublon ; assets/ck régénérés ; baseline Lyncée resserrée à 3753). Tous les jobs verts SAUF « visuel » : CLS bureau 0,13 à 0,17 (plafond 0,144 / 0,100 lent). Source du décalage (artefact visuel-rapport) : SECTION#v-cal.panel h103>376 à t≈670 ms, donc le calendrier rendu après la première peinture ; le glo-index plus lourd (31 ko contre 17 ko) retarde le rendu. Ce n'est pas un problème médical : il faut un correctif CLS d'Iris (réserver la hauteur de #v-cal ou rendre le calendrier avant de charger glo-index). feat/trauma-ddx échoue aussi au visuel. Depuis, main a avancé (#40), donc #39 demande une nouvelle fusion de main.
- PR #41 (fix/galien-tip-revue, 633aeea) : 16 fautes dans TIP champ 5 (#33) corrigées par tools/galien/tip_corr01.py (rejouable) ; glossaire S100B, source R-SNC-TCC ; 2 fautes CS (G6, S2.5) par tools/galien/cs_corr01.py ; rapport qa/audit-galien-tip-urgences.md ; registre fautes.jsonl (18 lignes nouvelles). Fusion (merge commit) dès que la CI est verte.
- Urgences lots 1 et 2 (#35, #38) : niveau 2 accepté, sans faute trouvée. 27 entrées du glossaire restent « À vérifier » (liste dans le rapport).
- audits_faits.txt : d253d06, 49aef17, c08236e, 3a1c4e3.
## Reste
1. Fusionner #39 après le correctif CLS (fusionner main, rejouer, vérifier le hash, puis `gh pr merge 39 --merge --match-head-commit <sha>`).
2. Les 27 signes « À vérifier » : les sourcer dans les lignes directrices déjà citées (SSC, EAACI, ESC IC, CEN).
3. Les ~85 termes de journal/nerfs-ck.md (l. 132 et 180).
4. Doses : 0 lue. compendium.ch et swissmedicinfo sont des applications JS illisibles par WebFetch ; il faut les lire à la main dans le navigateur, produit par produit.
5. Les grilles KK et les rôles des patients standardisés des stations CS, relus mot à mot.

# Relève Galien · audit prévalence des différentiels · 17.10.2026 (Europe/Zurich)
- Outils : /workspace/hippo_work/galien_prev/{poll2.sh,wait.sh,vue.py,RAPPORT.md,seen_prev} ; sources en src/ (verdon2008, eurodem).
- Rapport : PR #47 (audit/galien-prev, worktree /workspace/oef-galien-prev) ; seul fichier audit/RAPPORT_AUDIT_MEDICAL.md, copie de travail RAPPORT.md.
- G1 (#43) : 11 chiffres exacts ; ajout angor stable 11,2 % (S2.4, S2.5) ; note pariétale ; cadre S2.4. Commit 14f601a (+2d78eca).
- G2 (#44) : 4 chiffres exacts ; ajout SCA équivalent angineux (S2.7). Commit 7309a34.
- G3 (#45) : 7 chiffres exacts ; ajout diverticulite, DANS, urgences gynéco ; OPTIMA exclu de Lyncée. Commit fddaa42.
- À faire en fin : 72 textes de DD commencent par « À ne pas manquer.</b> » sans balise ouvrante (mention rouge perdue) → script rejouable après les groupes d'Asclépios.
