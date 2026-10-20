# ARSENAL · économie de jetons, précision dans la concision (Vial, 20.10.2026)

Obligatoire pour tout agent. Outils gratuits, locaux, dans `tools/arsenal/`. Sorties compactes : une ligne ou du JSON.

## Interdits communs
- Lire `app_v2.html` en entier (≈ 440 Ko) : `extrait.py` ou `tools/slim.py`. Doute : `python3 tools/budget.py --lignes 300 <fichier>`.
- Relire une PR entière, `git diff` complet ou des journaux de CI : `audit_diff.py`, `ci_attente.sh`.
- Régénérer les assets à la main ou suivre la CI à la main : `pr.sh`, `ci_attente.sh`.
- Générer une image : jamais. Inventer une dose : jamais (AIPS suisse ou « À vérifier (AIPS) »).

## Alpha · cours SSP en 14 parties
1. `tools/arsenal/extrait.py ssp <SSP> [--partie N]`
2. rédiger `tools/cours/lots/<SSP>.json` (14 parties, références, `lu_le`)
3. `tools/arsenal/lot.py cours <SSP> …`
4. `tools/arsenal/pr.sh "Alpha <SSP>" <SSP> …`
5. `tools/arsenal/ci_attente.sh`
Interdit : toucher aux DD, aux monographies, à `data/TIP.json` publié.

## Beta · monographies DD en 6 rubriques
1. `tools/arsenal/extrait.py mono <clé> [--champ pha]`
2. `python3 tools/mono_build.py --draft <SSP>` (aide, existant seulement)
3. `tools/arsenal/lot.py mono <clé> …`
4. `tools/arsenal/pr.sh "Beta <groupe-lot>"`
5. `tools/arsenal/ci_attente.sh`
Interdit : appliquer les 6 rubriques aux cours SSP ; dose sans extrait AIPS.

## Gamma · régions CS
1. `tools/arsenal/extrait.py liste region` puis `extrait.py region <id>`
2. `python3 tools/cs_build.py --check`
3. `python3 -m unittest discover -s tests`  (uniquement les tests touchés : `-p 'test_<x>*.py'`)
4. `tools/arsenal/pr.sh "Gamma <phase>"`
5. `tools/arsenal/ci_attente.sh`
Interdit : réécrire les textes des gestes (secteur Delta).

## Delta · gestes et pages région CS
1. `tools/arsenal/extrait.py region <id> --k <geste>`
2. images : sourcées et licenciées (skill `docs/skills/ssp-images-licence`), jamais générées
3. `tools/arsenal/lot.py auto`
4. `tools/arsenal/pr.sh "Delta <région>"`
5. `tools/arsenal/ci_attente.sh`
Interdit : modifier la présentation des régions (secteur Gamma) ; signe sans source propre.

## Auditeur · audit grok-bot
1. `gh pr checkout <n>`
2. `tools/arsenal/audit_diff.py [--max 400]` (valeurs modifiées + sources seulement)
3. `tools/arsenal/lot.py auto -v`
4. `tools/arsenal/ci_attente.sh`
5. `gh pr merge <n> --merge` après CI verte et audit signé
Interdit : auditer un texte qu'on a rédigé ; fusionner une CI non verte.

CI : `test_arsenal.py` et `lot.py auto` (résumé d'une ligne) tournent sur chaque PR.
