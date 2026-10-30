# REPRISE — PONS-OBLONGATA (généré 2026-10-30T20:27:39+00:00, branche production-v2)

**PAUSE ACTIVE** — 2026-10-30T16:50:29+00:00 ; motif : STOP d'urgence demandé par Vial
Règle : pendant la pause, aucun agent n'est lancé ; les agents en cours finissent leur fichier (pause douce, aucun jeton perdu) ; arrêt dur seulement sur ordre explicite de Vial. Sortie : `python3 harnais/pons_oblongata.py reprise`.

## Où on en est
- LOT_017 (EN_COURS) : 1 conformité faite ; 6 rédigé ; 4 rédaction en cours
- Déposés (dossier de travail conservé) : 011, 012, 013, 014, 015, 016

## Sûr (lu sur disque)
- 017 Phase_A : conformité faite, 136080 o, h3=14, FIN_FICHIER=oui, corr 51 (g 6, c 0)
- 017 DX.1 : rédigé, 125722 o, h3=14, FIN_FICHIER=oui, corr 0 (g 0, c 0)
- 017 DX.2 : rédigé, 123096 o, h3=14, FIN_FICHIER=oui, corr 0 (g 0, c 0)
- 017 DX.3 : rédigé, 130454 o, h3=14, FIN_FICHIER=oui, corr 0 (g 0, c 0)
- 017 DX.4 : rédigé, 133289 o, h3=14, FIN_FICHIER=oui, corr 0 (g 0, c 0)
- 017 DX.5 : rédigé, 133605 o, h3=14, FIN_FICHIER=oui, corr 0 (g 0, c 0)
- 017 DX.6 : rédaction en cours, 63432 o, h3=10, FIN_FICHIER=NON, corr 0 (g 0, c 0)
- 017 DX.7 : rédigé, 114648 o, h3=14, FIN_FICHIER=oui, corr 0 (g 0, c 0)
- 017 DX.9 : rédaction en cours, 42077 o, h3=6, FIN_FICHIER=NON, corr 0 (g 0, c 0)
- 017 DX.10 : rédaction en cours, 38824 o, h3=6, FIN_FICHIER=NON, corr 0 (g 0, c 0)
- LOT_017 : liste canonique gelée

## Incertain
- LOT_017 DX.6 : redacteur lancé 10-30T16:20 (opus/xhigh), aucun retour final sur disque (fichier modifié il y a 279 min) : probablement en cours ou interrompu
- LOT_017 DX.8 : redacteur lancé 10-30T16:26 (opus/xhigh), aucun retour final sur disque : probablement en cours ou interrompu
- LOT_017 DX.9 : redacteur lancé 10-30T16:29 (opus/xhigh), aucun retour final sur disque (fichier modifié il y a 279 min) : probablement en cours ou interrompu
- LOT_017 DX.10 : redacteur lancé 10-30T16:30 (opus/xhigh), aucun retour final sur disque (fichier modifié il y a 278 min) : probablement en cours ou interrompu
- LOT_017 items T non faits : T1 Verser dans `evidence/` les extraits des sources S44–S52  | T2 Phase A et tous les DX : vérifier tout chiffre repris d'A

## Prochaines actions (une ligne)
- 017 [Phase_A] : passe transversale T1–Tn (auditeur-medical opus xhigh), puis dépôt
- 017 [DX.1] : lancer auditeur-medical (opus, xhigh) avec harnais/briefs/AUDIT_MEDICAL.md sur LOT_017_Phase_B_V0_DX.1.html
- 017 [DX.2] : lancer auditeur-medical (opus, xhigh) avec harnais/briefs/AUDIT_MEDICAL.md sur LOT_017_Phase_B_V0_DX.2.html
- 017 [DX.3] : lancer auditeur-medical (opus, xhigh) avec harnais/briefs/AUDIT_MEDICAL.md sur LOT_017_Phase_B_V0_DX.3.html
- 017 [DX.4] : lancer auditeur-medical (opus, xhigh) avec harnais/briefs/AUDIT_MEDICAL.md sur LOT_017_Phase_B_V0_DX.4.html
- 017 [DX.5] : lancer auditeur-medical (opus, xhigh) avec harnais/briefs/AUDIT_MEDICAL.md sur LOT_017_Phase_B_V0_DX.5.html
- 017 [DX.6] : agent redacteur lancé 16:20 sans retour : vérifier d'abord le disque (état ci-dessus) ; ne relancer que s'il est mort
- 017 [DX.7] : lancer auditeur-medical (opus, xhigh) avec harnais/briefs/AUDIT_MEDICAL.md sur LOT_017_Phase_B_V0_DX.7.html
- 017 [DX.8] : agent redacteur lancé 16:26 sans retour : vérifier d'abord le disque (état ci-dessus) ; ne relancer que s'il est mort
- 017 [DX.9] : agent redacteur lancé 16:29 sans retour : vérifier d'abord le disque (état ci-dessus) ; ne relancer que s'il est mort
- 017 [DX.10] : agent redacteur lancé 16:30 sans retour : vérifier d'abord le disque (état ci-dessus) ; ne relancer que s'il est mort

## Briefs types et commandes
- Rédacteur Phase B : `lot en cours de production/LOT_XXX/BRIEF_PHASE_B.md` ; audit médical : `harnais/briefs/AUDIT_MEDICAL.md` ; conformité : `harnais/briefs/CONFORMITE.md`.
- Prompt d'une ligne : « Lis <brief> ; fichier : <nom> ; LOT_XXX. » Au plus 5 agents opus en parallèle.
- `python3 harnais/pons_oblongata.py etat` ; `python3 harnais/controle_lot.py verifier "lot en cours de production/LOT_XXX"` ; `python3 harnais/audit_langue.py <fichier> --json`.
- Ne jamais reprendre un agent par SendMessage (recharge tout son historique) : relancer un agent neuf avec le brief et l'état disque. Détail : PROMPT_PRODUCTION_V2.md.
