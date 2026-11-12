# Reprise — nouvelle session (environnement unique : organigramme-examen-federal), 12.11.2026

**État : PAUSE.** Aucun agent ne tourne. Rien ne reprend sans le GO de Vial.

## Étape 0 (machine vierge, 2 commandes)
1. `git fetch origin claude/harnais && git worktree add /home/user/wt/harnais claude/harnais`
2. `cd /home/user/wt/harnais && bash Claude/_harnais/installer.sh` (corpus AIPS hors ligne, verrou, contrôle de syntaxe)

## Première production demandée par Vial (sans attendre qu'il le redise)
Un **tableau théorique du dispositif** : chaque entité fonctionnelle (script, mémoire, porte, veille, verrou, agent, PR, CI),
son rôle, son déclencheur, ce qu'elle **empêche réellement** (preuve mesurée ou testée), et sa limite. Distinguer ce qui est
prouvé (mesure Gaspillon, test du verrou, audit reproduit) de ce qui est seulement attendu. Source : `RAPPORT_HARNAIS.html`,
`GASPILLON.html`, les docstrings de `Claude/_harnais/*.py`. Livrer en HTML, puis attendre le GO.

## Branches (toutes poussées, propres)
| Chantier | Branche | Reste |
|---|---|---|
| Harnais | `claude/harnais` (PR #652, brouillon, CI verte) | fusion au GO |
| LOT_023 | `claude/lot-023-renfort-l1` | contre-audit : 1 grave (n° Mestinon : 19943 comprimés, 19945 dragées, 56387 retard), 2 moyens (allaitement Mestinon « ou cesser d'allaiter », DX.6 CROSS/FLOT), 7 légers ; puis PR |
| LOT_024 | `claude/lot-024-renfort-l1` | portes `aips_fiche.py verifier` + `abreviations.py`, corrections audit1 A/B (critiques Co-Amoxi, Algifor), contre-audit, PR |
| LOT_025 | `claude/lot-025-renfort-l1` + `claude/lot-025-agent-1..5` (WIP) | contre-audit Phase A ; reprise des 5 agents depuis leur WIP |

## Règles du harnais (résumé)
Brief agents : `Claude/_harnais/BRIEF_HARNAIS.md`. Jamais de lecture intégrale d'un cours (`extrait.py`) ; mémoire avant relecture
(`resumeur.py`, `memoire_agent.py`, `cerveau.py`) ; AIPS par `aips_fiche.py trouve|fiche|verifier` ; sources par `sources_cache.py` ;
agents décrits « [H] … » pour la mesure ; veille `veille_harnais.sh 23 24 25` au GO. Le dépôt MEDINA est fermé.
