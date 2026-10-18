# Propositions de skills (générées par tools/propose_skills.py)

Relancer : `python3 tools/propose_skills.py`. Codex lit ce fichier à la fin de chaque étape : chaque candidat utile devient `docs/skills/<nom>/SKILL.md` (procédure courte, commandes exactes, pièges), les autres sont rayés avec leur motif.

Seuil : 3 occurrences. Corpus : journal/*.md, HANDOFF.md, CONTINUATION.md, .etat_local/*.log, git log.

## Commandes répétitives non couvertes par un skill

| Vu | Commande normalisée | Où | Skill proposé |
|---|---|---|---|
| 4 | `tools/etapes.json` | CONTINUATION.md | `ssp-etapes-json` |

## Tâches répétitives (sujets de commit)

| Vu | Début de sujet | Action |
|---|---|---|
| 12 | audit galien-neuro glo-lot01a | automatiser par script ou skill ; modèle GPT 6 Luna (ordre de Vial) |
| 11 | audit galien-neuro glo-lot01b | automatiser par script ou skill ; modèle GPT 6 Luna (ordre de Vial) |
| 10 | visuel nouvelle référence | automatiser par script ou skill ; modèle GPT 6 Luna (ordre de Vial) |
| 7 | codex étape n | automatiser par script ou skill ; modèle GPT 6 Luna (ordre de Vial) |
| 4 | audit galien-têtecou glo-lot01a | automatiser par script ou skill ; modèle GPT 6 Luna (ordre de Vial) |

## Squelette d'un skill

```markdown
---
name: ssp-<nom>
description: <quand l'utiliser, en une phrase>
---
# <Titre>
1. Préalable : <worktree, fichiers lus>
2. Commandes : <exactes, rejouables>
3. Contrôle : <tests, --check>
4. Pièges : <liste>
```

## Décisions de cette relève
- `tools/etapes.json` : fichier, faux positif ; pas de skill de commande.
- Audits, références visuelles et étapes : skills existants ; pas de doublon.
- Quatre lots AIPS : procédure récurrente concrète devenue `ssp-aips-verbatim`, comparateur testé et cache hors git.
