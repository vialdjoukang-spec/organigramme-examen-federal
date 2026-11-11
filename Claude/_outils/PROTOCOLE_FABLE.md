# PROTOCOLE FABLE — renfort et audit L1 d'un LOT, en parallèle (ordre de Vial du 11.11.2026)

But : chaque LOT (Phase A + DX.1–DX.10) renforcé L1, audité deux fois (médical + design), fusionné dans main, sans aucun
relâchement de qualité. Plusieurs LOTs avancent de front, un chef de LOT par LOT. Le bloc L1 de
`PROMPT_Casern/PROMPT_LOTS_L1_10.11.26.claude.md` prime ; ce protocole dit seulement qui fait quoi, et dans quel ordre.

## Rôles
- **Chef de LOT** (une session ou un agent par LOT) : branche `claude/lot-NNN-renfort-l1`, worktree propre. Il ne rédige pas
  les DX : il prépare, répartit, tranche, corrige les restes d'audit, ouvre la PR.
- **Rédacteur** : UN fichier par agent (un fichier lourd épuise un contexte). Onze rédacteurs peuvent tourner ensemble.
- **Designer** (agent `designer`) : la forme des 11 cours, par les outils ; jamais le contenu médical.
- **Auditeur** (agent `auditeur-medical`) : toujours neuf. Il n'audite jamais un texte qu'il a rédigé, et le contre-auditeur
  n'est jamais le premier auditeur. Deux auditeurs par passe : Phase A + DX.1–5, puis DX.6–10.

## Étapes et portes (une porte fermée arrête le LOT ; rien ne se contourne)
0. **Départ.** `git fetch origin main` ; brancher depuis `origin/main` (ou fusionner main dans la branche existante) ;
   `python3 Claude/_outils/forme.py Claude/LOT_NNN/*.html` ; `python3 Claude/_outils/controle3.py --script-ok Claude/LOT_NNN/*.html`.
   Si le LOT est attribué à une autre IA dans `ATTRIBUTIONS.json`, le réattribuer à « Claude » dans la PR du LOT, sans
   écraser sa branche ni son travail en cours.
1. **P1 — liste DX gelée.** `Claude/LOT_NNN/audits/LISTE_DX.audit.json` (dix diagnostics distincts, ordre de fréquence
   sourcé, drapeaux et rangs E), puis `python3 Claude/_outils/geler.py NNN`.
2. **Renfort.** Phase A par le chef de LOT ou un rédacteur ; un rédacteur par DX, tous ensemble
   (`Claude/_outils/MISSION_RENFORCEMENT.md`). Chaque rédacteur valide son seul fichier par chemin
   (`git commit -- <fichier>`), jamais `git add -A`, jamais de checkout/reset/stash dans le worktree partagé.
   Sortie exigée par fichier : `controle3 --script-ok` VERT ; 80 000–150 000 octets ; point 1 = définition seule ; fenêtres
   `:target` ; examen physique en une fenêtre par région ; une fiche `.mb` par molécule ; point 14 ≥ 6 questions ;
   phrases verbales de 12 à 28 mots ; aucune formule de lacune.
3. **P2 — AIPS mécanique.** `python3 Claude/_outils/verif_aips.py Claude/LOT_NNN/*.html` : zéro défaut bloquant (ancre sans
   bibliographie, bibliographie sans URL refdata, citation absente de l'AIPS citée). Chaque alerte « dose absente de
   l'AIPS citée » est relue : mauvaise AIPS collée → corriger ; dose de recommandation → la phrase le dit (« hors AIPS »,
   divergence écrite) et la conduite suit l'AIPS.
4. **P3 — aucun fait perdu.** Tout retrait fait pour la taille est une redite, consignée dans `HELP.md` avec l'endroit où
   l'information reste. Un rédacteur qui ne tient pas 150 Ko sans couper un fait s'arrête et le signale ; le chef de LOT
   déplace le fait vers la Phase A ou un autre DX, ou trouve la redite.
5. **Designer.** Agent `designer` sur les 11 fichiers : contrôle à 1280 et 390 px, corrections de forme, planche de
   5 captures par cours (`python3 Claude/_outils/planche5.py Claude/LOT_NNN --sortie …`), envoyée à Vial.
6. **P4 — audit 1 (médical + design).** Deux auditeurs neufs. Rapports `audits/LOT_NNN_A_DX1-5.audit.json` et
   `audits/LOT_NNN_DX6-10.audit.json` : verdict, défauts classés (Critique, Grave, Moyen, Léger), `avant` exact,
   `correction` prête à coller, source. Ils relisent à la main au moins 40 renvois AIPS par moitié, et la liste des retraits.
7. **Corrections.** Un correcteur par fichier touché, ou le chef de LOT si les corrections sont courtes. Puis `forme.py`,
   `controle3`, `verif_aips`.
8. **P5 — contre-audit.** Deux auditeurs neufs : `audits/LOT_NNN_audit2_*.audit.json`. Fusion possible si zéro Critique,
   zéro Grave, et chaque Moyen corrigé ou justifié dans `HELP.md`.
9. **PR vers main.** Corps : la ligne « Prompt L1 lu et appliqué. », le résumé des audits, la section « ## Automates
   actifs » (ci.yml, checkpoint.yml, auto-fusion.yml, file-fusion.yml, garde-progres.yml). Étiquette `audit-ok`, fusion
   automatique par commit de fusion, abonnement à la PR ; les remarques de Codex sont vérifiées, et corrigées si elles
   sont vraies.

## Règles constantes
- Sources suisses puis européennes, lues et datées ; aucune source seulement américaine en appui d'une décision ; rien d'inventé.
- Chaque dose renvoie à l'AIPS de sa molécule (jamais le Compendium) ; texte AIPS lu sur refdata
  (index : `AipsDownload_*.zip`, ou `Claude/_outils/lecon.py prep`).
- Commits terminés par « Prompt L1 lu et appliqué. », Co-Authored-By et Claude-Session. Jamais de `--force`, jamais de
  suppression de branche.
- Un doute médical que les sources ne tranchent pas va dans `HELP.md` et dans le rapport au chef d'orchestre ; il ne se
  règle jamais par une phrase vague dans le cours.

## Cadence
- Le chef d'orchestre lance les LOTs en ordre croissant, par vagues (4 LOTs de front au départ ; davantage si une vague
  sort sans Critique à l'audit 1). Les PR sont indépendantes ; elles fusionnent dans l'ordre où elles sont prêtes.
- Chaque matin à 8h00 (Europe/Zurich) : HTML de progression de tous les LOTs (`outils/progression.py` sur main à jour).
