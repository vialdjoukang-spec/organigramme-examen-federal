# REPRISE — PONS-OBLONGATA (généré 2026-10-30T15:21:07+00:00, branche production-v2)

## Où on en est
- LOT_017 (EN_COURS) : 1 conformité faite ; 7 rédaction en cours ; 3 aucun fichier
- Déposés (dossier de travail conservé) : 011, 012, 013, 014, 015, 016

## Sûr (lu sur disque)
- 017 Phase_A : conformité faite, 136080 o, h3=14, FIN_FICHIER=oui, corr 51 (g 6, c 0)
- 017 DX.1 : rédaction en cours, 125722 o, h3=14, FIN_FICHIER=oui, corr 0 (g 0, c 0)
- 017 DX.2 : rédaction en cours, 123096 o, h3=14, FIN_FICHIER=oui, corr 0 (g 0, c 0)
- 017 DX.3 : rédaction en cours, 127544 o, h3=14, FIN_FICHIER=oui, corr 0 (g 0, c 0)
- 017 DX.4 : rédaction en cours, 117454 o, h3=14, FIN_FICHIER=NON, corr 0 (g 0, c 0)
- 017 DX.5 : rédaction en cours, 68916 o, h3=10, FIN_FICHIER=NON, corr 0 (g 0, c 0)
- LOT_017 : liste canonique gelée

## Incertain
- LOT_017 DX.1 : redacteur lancé 10-30T15:50 (opus/xhigh), aucun retour final sur disque (fichier modifié il y a 2 min) : probablement en cours ou interrompu
- LOT_017 DX.2 : redacteur lancé 10-30T15:50 (opus/xhigh), aucun retour final sur disque (fichier modifié il y a 1 min) : probablement en cours ou interrompu
- LOT_017 DX.3 : redacteur lancé 10-30T15:50 (opus/xhigh), aucun retour final sur disque (fichier modifié il y a 0 min) : probablement en cours ou interrompu
- LOT_017 DX.4 : redacteur lancé 10-30T15:50 (opus/xhigh), aucun retour final sur disque (fichier modifié il y a 0 min) : probablement en cours ou interrompu
- LOT_017 DX.5 : redacteur lancé 10-30T15:50 (opus/xhigh), aucun retour final sur disque (fichier modifié il y a 1 min) : probablement en cours ou interrompu
- LOT_017 DX.6 : redacteur lancé 10-30T16:20 (opus/xhigh), aucun retour final sur disque : probablement en cours ou interrompu
- LOT_017 DX.7 : redacteur lancé 10-30T16:21 (opus/xhigh), aucun retour final sur disque : probablement en cours ou interrompu
- LOT_017 items T non faits : T1 Verser dans `evidence/` les extraits des sources S44–S52  | T2 Phase A et tous les DX : vérifier tout chiffre repris d'A

## Prochaines actions (une ligne)
- 017 [Phase_A] : passe transversale T1–Tn (auditeur-medical opus xhigh), puis dépôt
- 017 [5 fichiers] : agent redacteur lancé 15:50 sans retour : vérifier d'abord le disque (état ci-dessus) ; ne relancer que s'il est mort
- 017 [DX.6] : agent redacteur lancé 16:20 sans retour : vérifier d'abord le disque (état ci-dessus) ; ne relancer que s'il est mort
- 017 [DX.7] : agent redacteur lancé 16:21 sans retour : vérifier d'abord le disque (état ci-dessus) ; ne relancer que s'il est mort
- 017 [DX.8] : lancer redacteur (opus, xhigh) DX.8 avec 'lot en cours de production/LOT_017/BRIEF_PHASE_B.md'
- 017 [DX.9] : lancer redacteur (opus, xhigh) DX.9 avec 'lot en cours de production/LOT_017/BRIEF_PHASE_B.md'
- 017 [DX.10] : lancer redacteur (opus, xhigh) DX.10 avec 'lot en cours de production/LOT_017/BRIEF_PHASE_B.md'

## Briefs types et commandes
- Rédacteur Phase B : `lot en cours de production/LOT_XXX/BRIEF_PHASE_B.md` ; audit médical : `harnais/briefs/AUDIT_MEDICAL.md` ; conformité : `harnais/briefs/CONFORMITE.md`.
- Prompt d'une ligne : « Lis <brief> ; fichier : <nom> ; LOT_XXX. » Au plus 5 agents opus en parallèle.
- `python3 harnais/pons_oblongata.py etat` ; `python3 harnais/controle_lot.py verifier "lot en cours de production/LOT_XXX"` ; `python3 harnais/audit_langue.py <fichier> --json`.
- Ne jamais reprendre un agent par SendMessage (recharge tout son historique) : relancer un agent neuf avec le brief et l'état disque. Détail : PROMPT_PRODUCTION_V2.md.
