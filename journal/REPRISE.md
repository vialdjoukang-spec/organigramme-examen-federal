# REPRISE — PONS-OBLONGATA (généré 2026-10-30T14:23:46+00:00, branche production-v2)

## Où on en est
- LOT_017 (EN_COURS) : 1 rédaction en cours ; 10 aucun fichier
- Déposés (dossier de travail conservé) : 011, 012, 013, 014, 015, 016

## Sûr (lu sur disque)
- 017 Phase_A : rédaction en cours, 118483 o, h3=14, FIN_FICHIER=oui, corr 0 (g 0, c 0)

## Incertain
- LOT_017 Phase_A : redacteur-phase-a lancé 10-30T14:44 (opus/xhigh), aucun retour final sur disque (fichier modifié il y a 1 min) : probablement en cours ou interrompu

## Prochaines actions (une ligne)
- 017 [Phase_A] : agent redacteur-phase-a lancé 14:44 sans retour : vérifier d'abord le disque (état ci-dessus) ; ne relancer que s'il est mort
- 017 [10 fichiers] : attendre le gel de LISTE_DX_CANONIQUE.md (audit médical de la Phase A)

## Briefs types et commandes
- Rédacteur Phase B : `lot en cours de production/LOT_XXX/BRIEF_PHASE_B.md` ; audit médical : `harnais/briefs/AUDIT_MEDICAL.md` ; conformité : `harnais/briefs/CONFORMITE.md`.
- Prompt d'une ligne : « Lis <brief> ; fichier : <nom> ; LOT_XXX. » Au plus 5 agents opus en parallèle.
- `python3 harnais/pons_oblongata.py etat` ; `python3 harnais/controle_lot.py verifier "lot en cours de production/LOT_XXX"` ; `python3 harnais/audit_langue.py <fichier> --json`.
- Ne jamais reprendre un agent par SendMessage (recharge tout son historique) : relancer un agent neuf avec le brief et l'état disque. Détail : PROMPT_PRODUCTION_V2.md.
