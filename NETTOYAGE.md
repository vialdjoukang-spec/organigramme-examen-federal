# NETTOYAGE — supprimer l'indésirable, sans casser (V0, 26.10.2026)

**Quand :** après la première PR de dépôt fusionnée dans `LOT_Claude_Finaux/`. **Comment :** une PR séparée `nettoyage-v0`, un commit par catégorie. `git rm` est réversible par l'historique ; rien n'est détruit hors de git.

## Règle avant toute suppression

Pour chaque candidat : `grep -rIl "<nom du fichier>" --exclude-dir=.git .` (workflows, tests, outils, documents). **Référencé par un workflow, un test ou un outil → tu ne le supprimes pas** ; tu l'écris dans `LOT_Claude_Finaux/NETTOYAGE_RESULTAT.md` avec la référence trouvée.

## Candidats (observés dans le dépôt le 26.10.2026 ; à re-vérifier)

| Catégorie | Candidats | Condition |
|---|---|---|
| Prompts remplacés par V0 (le V0 déclare remplacer V8 et V7) | `PROMPT_Casern/PROMPT_ULTIME_PRODUCTION_LOTS_V8.md`, `.pdf` · `PROMPT_Casern/PROMPT_HARNAIS_V8.md`, `.pdf` · `PROMPT_Casern/PLAN_HARNESS_ENGINEERING_V8.html`, `.pdf` · `PROMPT_Casern/MESSAGE_DEMARRAGE_SENS_INVERSE.md` | non référencés |
| Doublons du harnais | `PROMPT_Casern/HARNAIS_OBLIGATOIRE.md`, `PROMPT_Casern/bracelet/` | `diff -r` avec `harnais/` : si identiques ou plus anciens, suppression ; si plus récents, tu fusionnes d'abord vers `harnais/` |
| Plan propre au LOT_011 | `harnais/plan_harness_engineering_lot11.html` | non référencé (l'ancien `HARNAIS_OBLIGATOIRE.md` le citait ; le nouveau non) |
| Brouillons multi-DD devenus redondants | Dans `lot en cours de production/LOT_XXX/` : fichiers `Appel_A_V7`, `Appel_B_V7_Partie_*` d'un LOT dont le verdict est `ACCEPTE` et dont les 11 HTML sont fusionnés | seulement après fusion de la PR de dépôt de ce LOT |
| Résidus de travail | `.cache/` (déjà ignoré), répertoires `__pycache__`, fichiers `*.pyc` éventuellement versionnés | `git ls-files` les montre |

## Jamais supprimés

`audit/`, `tests/`, `tools/`, `data/`, `assets/`, `orig/`, `journal/`, `app_v2.html`, `LOT_Claude_Finaux/`, l'archive `LOTS_Finaux avec statut-*.zip`, `ETAT.md`, `HANDOFF.md`, `PROCHAINE_ACTION.md`, `CLAUDE.md`, `AGENTS.md`, `CONTINUATION.md`. Dans le dossier d'un LOT refusé, les anciens fichiers restent : ils sont la seule copie.

## Ancien lieu de dépôt externe

Aucune action. Il n'est plus une cible ; tu n'y lis ni n'y écris rien pour ce nettoyage.

## Résultat

`LOT_Claude_Finaux/NETTOYAGE_RESULTAT.md` : liste des fichiers supprimés (avec la commande `grep` de contrôle), des fichiers conservés et pourquoi. La PR passe la CI avant fusion (`tools/arsenal/ci_attente.sh`).
