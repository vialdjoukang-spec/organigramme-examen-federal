# Reprise — nouvelle session (environnement unique : organigramme-examen-federal)

**État (13.11.2026) : LOT_023 à 032 fusionnés ; LOT_033–034 EN PAUSE. Priorité de Vial : chantier PROGRESSION (`Claude/_progression/`, cahier d'architecture v2) — charpente puis contenu.** Aucun agent ne tourne. Prochaine étape : la file (LOT suivants), 2 LOT en parallèle (10 agents) — objectif de Vial, coût estimé ≈ 96 % d'un ancien LOT (r = 0,48).

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

4. **Leçons du 12.11** : `Claude/_outils/verif_aips.py` lit désormais les mots refdata découpés en `<span>` (fusionner `main` dans toute branche LOT avant ses portes) ; donner aux agents les chemins ABSOLUS des outils (`/home/user/organigramme-examen-federal/Claude/_harnais/`), sinon ils ne les trouvent pas depuis leur worktree ; chaque LOT : rédaction → designer → audits médical + conformité → corrections → vérification finale → contrôle ultime ciblé (jusqu'à audit-ok) → planche → PR → fusion après CI verte.

5. **Disque** : le quota de session s'est rempli le 13.11 (conteneur redémarré). Supprimer chaque worktree d'agent après push (`git worktree remove`), purger le scratchpad des LOT fusionnés. Coût mesuré (suivi.py compte désormais les agents Workflow) : LOT_026 = 50 M éq., LOT_027 = 57 M, contre ≈ 67 M pour un LOT d'avant le harnais (16, 19–22) : −21 % par LOT, 2 LOT ≈ 159 % d'un ancien LOT (modèle prévu : 96 %).

## Branches (toutes poussées, propres)
| Chantier | Branche | Reste |
|---|---|---|
| LOT_023 | fusionné (PR #655, 12.11.2026, contrôle ultime audit-ok) | planche `Claude/LOT_023/PLANCHE_LOT_023.html` (PR #656) |
| LOT_024 | fusionné (PR #657, 12.11.2026, contrôle ultime levé, planche `Claude/LOT_024/PLANCHE_LOT_024.html`) | rien |
| LOT_025 | fusionné (PR #658, 12.11.2026, contrôle ultime audit-ok, planche) | 2 légers non bloquants : crédit photo DX.5 mot pour mot (affiliation NJDS) ; précision Schirmer répétée DX.7 |
| LOT_026 | fusionné (PR #662, 13.11.2026, audit-ok, planche) | rien |
| LOT_027 | fusionné (PR #663, 13.11.2026, audit-ok, planche) | rien |
| LOT_028 à 032 | fusionnés (PR #664, #666, #667, #668, #669 ; 13.11.2026 ; audit-ok, fond blanc, planches) | rien |
| LOT_033 | `claude/lot-033-renfort-l1` (Phase A audit-ok, liste gelée) + `claude/lot-033-agent-1..5` (WIP 1 et 3 poussés) | EN PAUSE (Vial, 13.11) : reprendre au step rédaction DX (workflow `lot033-complet`, resume) |
| LOT_034 | `claude/lot-034-renfort-l1` (Phase A audit-ok, liste gelée) + agents 1–2 commencés | EN PAUSE (Vial, 13.11) : reprendre au step rédaction DX (workflow `lot034-complet`) |
