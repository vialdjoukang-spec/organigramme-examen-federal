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
| 17 | audit galien-neuro nc07-chaine | automatiser par script ou skill ; modèle GPT 6 Luna (ordre de Vial) |
| 13 | visuel nouvelle référence | automatiser par script ou skill ; modèle GPT 6 Luna (ordre de Vial) |
| 12 | audit galien-neuro glo-lot01a | automatiser par script ou skill ; modèle GPT 6 Luna (ordre de Vial) |
| 11 | audit galien-neuro glo-lot01b | automatiser par script ou skill ; modèle GPT 6 Luna (ordre de Vial) |
| 7 | codex étape n | automatiser par script ou skill ; modèle GPT 6 Luna (ordre de Vial) |
| 4 | préciser le pays | automatiser par script ou skill ; modèle GPT 6 Luna (ordre de Vial) |
| 4 | préciser le compte | automatiser par script ou skill ; modèle GPT 6 Luna (ordre de Vial) |
| 4 | audit hérophile lot | automatiser par script ou skill ; modèle GPT 6 Luna (ordre de Vial) |
| 4 | hygie monographies lot | automatiser par script ou skill ; modèle GPT 6 Luna (ordre de Vial) |
| 4 | asclépios prévalence ssp | automatiser par script ou skill ; modèle GPT 6 Luna (ordre de Vial) |
| 4 | audit galien-têtecou glo-lot01a | automatiser par script ou skill ; modèle GPT 6 Luna (ordre de Vial) |
| 3 | pharmakon table suisse | automatiser par script ou skill ; modèle GPT 6 Luna (ordre de Vial) |
| 3 | audit érasistrate panacée | automatiser par script ou skill ; modèle GPT 6 Luna (ordre de Vial) |
| 3 | monographies panacée lot | automatiser par script ou skill ; modèle GPT 6 Luna (ordre de Vial) |
| 3 | audit galien rapport | automatiser par script ou skill ; modèle GPT 6 Luna (ordre de Vial) |

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

## Examen du lot 5 · 18.10.2026
`tools/etapes.json` est une configuration, pas une commande : candidat écarté. Rédaction/audit CK, posologie et continuité sont couverts par ssp-construction-ck, ssp-audit-medical, ssp-aips-verbatim et ssp-continuite ; aucun nouveau skill nécessaire.
