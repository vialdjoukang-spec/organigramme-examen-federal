# REPRISE — PONS-OBLONGATA (généré 2026-10-30T14:50:07+00:00, branche production-v2)

## Où on en est
- LOT_017 (EN_COURS) : 1 audit médical fait ; 5 rédaction en cours ; 5 aucun fichier
- Déposés (dossier de travail conservé) : 011, 012, 013, 014, 015, 016

## Sûr (lu sur disque)
- 017 Phase_A : audit médical fait, 135753 o, h3=14, FIN_FICHIER=oui, corr 46 (g 6, c 0)
- LOT_017 : liste canonique gelée

## Incertain
- LOT_017 Phase_A : redacteur-phase-a lancé 10-30T14:44 (opus/xhigh), aucun retour final sur disque (fichier modifié il y a 3 min) : probablement en cours ou interrompu
- LOT_017 Phase_A : auditeur-conformite lancé 10-30T15:50 (sonnet/high), aucun retour final sur disque : probablement en cours ou interrompu
- LOT_017 DX.1 : redacteur lancé 10-30T15:50 (opus/xhigh), aucun retour final sur disque : probablement en cours ou interrompu
- LOT_017 DX.2 : redacteur lancé 10-30T15:50 (opus/xhigh), aucun retour final sur disque : probablement en cours ou interrompu
- LOT_017 DX.3 : redacteur lancé 10-30T15:50 (opus/xhigh), aucun retour final sur disque : probablement en cours ou interrompu
- LOT_017 DX.4 : redacteur lancé 10-30T15:50 (opus/xhigh), aucun retour final sur disque : probablement en cours ou interrompu
- LOT_017 DX.5 : redacteur lancé 10-30T15:50 (opus/xhigh), aucun retour final sur disque : probablement en cours ou interrompu
- LOT_017 items T non faits : T1 Verser dans `evidence/` les extraits des sources S44–S52 

## Prochaines actions (une ligne)
- 017 [Phase_A] : agent redacteur-phase-a lancé 14:44 sans retour : vérifier d'abord le disque (état ci-dessus) ; ne relancer que s'il est mort
- 017 [5 fichiers] : agent redacteur lancé 15:50 sans retour : vérifier d'abord le disque (état ci-dessus) ; ne relancer que s'il est mort
- 017 [DX.6] : lancer redacteur (opus, xhigh) DX.6 avec 'lot en cours de production/LOT_017/BRIEF_PHASE_B.md'
- 017 [DX.7] : lancer redacteur (opus, xhigh) DX.7 avec 'lot en cours de production/LOT_017/BRIEF_PHASE_B.md'
- 017 [DX.8] : lancer redacteur (opus, xhigh) DX.8 avec 'lot en cours de production/LOT_017/BRIEF_PHASE_B.md'
- 017 [DX.9] : lancer redacteur (opus, xhigh) DX.9 avec 'lot en cours de production/LOT_017/BRIEF_PHASE_B.md'
- 017 [DX.10] : lancer redacteur (opus, xhigh) DX.10 avec 'lot en cours de production/LOT_017/BRIEF_PHASE_B.md'

## Briefs types et commandes
- Rédacteur Phase B : `lot en cours de production/LOT_XXX/BRIEF_PHASE_B.md` ; audit médical : `harnais/briefs/AUDIT_MEDICAL.md` ; conformité : `harnais/briefs/CONFORMITE.md`.
- Prompt d'une ligne : « Lis <brief> ; fichier : <nom> ; LOT_XXX. » Au plus 5 agents opus en parallèle.
- `python3 harnais/pons_oblongata.py etat` ; `python3 harnais/controle_lot.py verifier "lot en cours de production/LOT_XXX"` ; `python3 harnais/audit_langue.py <fichier> --json`.
- Ne jamais reprendre un agent par SendMessage (recharge tout son historique) : relancer un agent neuf avec le brief et l'état disque. Détail : PROMPT_PRODUCTION_V2.md.
