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

3. **Planche de captures obligatoire par LOT** (ordre de Vial, 12.11.2026) : `python3 Claude/_outils/planche5.py Claude/LOT_0NN --sortie Claude/LOT_0NN/PLANCHE_LOT_0NN.html` (gratuit, Playwright), commitée avec le LOT et envoyée à Vial avant la PR.

## Branches (toutes poussées, propres)
| Chantier | Branche | Reste |
|---|---|---|
| LOT_023 | fusionné (PR #655, 12.11.2026, contrôle ultime audit-ok) | planche `Claude/LOT_023/PLANCHE_LOT_023.html` (PR #656) |
| LOT_024 | fusionné (PR #657, 12.11.2026, contrôle ultime levé, planche `Claude/LOT_024/PLANCHE_LOT_024.html`) | rien |
| LOT_025 | `claude/lot-025-renfort-l1` (Phase A) + `claude/lot-025-agent-1..5` (DX.1+8, 2+7, 3+6, 4+5, 9+10) | Phase A : contre-audit CORRECTIONS (4 graves Salagen/Kenacort/renvois, 8 moyens), rédacteur lancé 12.11 ; 5 rédacteurs DX lancés 12.11 (workflow lot025-redaction) ; puis fusion des branches agents dans renfort-l1, designer, audits, planche, PR |
