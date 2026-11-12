# Reprise — nouvelle session (environnement unique : organigramme-examen-federal)

**État : PAUSE.** Aucun agent ne tourne. Rien ne reprend sans le GO écrit de Vial.

## Étape 0 (machine vierge, une commande, ≈ 1 min)
`bash Claude/_harnais/installer.sh` — corpus AIPS hors ligne, verrous (lecture intégrale, MEDINA), contrôle de syntaxe.
Ne lis rien d'autre au démarrage : ni CONTINUATION.md, ni PROCHAINE_ACTION.md, ni `porte.py etat` (ancien chantier Codex).

## Ce qui est déjà fait (ne pas refaire)
- Harnais complet sur `main` : voir `Claude/_harnais/TABLEAU_DISPOSITIF.html` (entités, ce qu'elles empêchent, angles morts).
- Rapport chiffré : `Claude/_harnais/RAPPORT_HARNAIS.html`. Gaspillage : `Claude/_harnais/GASPILLON.html`.
- Premier message à Vial : une ligne « Harnais installé, pause maintenue, j'attends GO. » Rien de plus.

## Règles de l'orchestrateur (contre l'explosion du contexte)
1. **Session principale légère** : elle distribue, contrôle par scripts et fusionne. Elle ne rédige pas de cours, ne lit
   ni cours, ni AIPS, ni source en entier ; elle lit `Claude/LOT_0NN/MEMOIRE.md` et les sorties ≤ 15 lignes des agents.
2. **Sorties courtes** : toute commande passe par `| tail -20` ou `| head -40` ; jamais de JSON brut d'outil.
3. **Relais de session** : dès qu'un LOT est fusionné, ou après ≈ 150 échanges, mettre à jour ce fichier (section « Branches »)
   et `python3 Claude/_harnais/resumeur.py --global`, pousser, puis donner à Vial le prompt de démarrage pour une session neuve.
4. **Notifications GitHub** : une ligne de réponse au plus ; aucune relecture de PR entière.
5. **Agents** : description préfixée « [H] » ; brief = `Claude/_harnais/BRIEF_HARNAIS.md` ; ≤ 220 tours ; rapport ≤ 5 lignes.

## Au GO
1. Lancer la veille : `nohup bash Claude/_harnais/veille_harnais.sh 23 24 25 >/dev/null 2>&1 &`
2. Terminer les LOT dans l'ordre 023 → 024 → 025 selon le tableau ci-dessous, puis la file (Phase A par Claude, 5 agents × 2 DX).

## Branches (toutes poussées, propres)
| Chantier | Branche | Reste |
|---|---|---|
| LOT_023 | `claude/lot-023-renfort-l1` | contre-audit : 1 grave (n° Mestinon : 19943 comprimés, 19945 dragées, 56387 retard ; bibliographie), 2 moyens (allaitement Mestinon « ou cesser d'allaiter » ; DX.6 CROSS/FLOT), 7 légers ; puis PR |
| LOT_024 | `claude/lot-024-renfort-l1` | portes `aips_fiche.py verifier` + `abreviations.py` ; corrections audit1 A/B (critiques Co-Amoxi, Algifor ; graves dates AIPS DX.9/10, Rocephin allaitement) ; contre-audit ; PR |
| LOT_025 | `claude/lot-025-renfort-l1` + `claude/lot-025-agent-1..5` (WIP) | contre-audit Phase A ; reprise des 5 agents depuis leur WIP |
