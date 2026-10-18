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
| 12 | audit galien-neuro glo-lot01a | automatiser par script ou skill ; modèle GPT 6 Luna (ordre de Vial) |
| 11 | audit galien-neuro glo-lot01b | automatiser par script ou skill ; modèle GPT 6 Luna (ordre de Vial) |
| 10 | visuel nouvelle référence | automatiser par script ou skill ; modèle GPT 6 Luna (ordre de Vial) |
| 7 | codex étape n | automatiser par script ou skill ; modèle GPT 6 Luna (ordre de Vial) |
| 4 | asclépios prévalence ssp | automatiser par script ou skill ; modèle GPT 6 Luna (ordre de Vial) |
| 4 | audit galien-têtecou glo-lot01a | automatiser par script ou skill ; modèle GPT 6 Luna (ordre de Vial) |
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

## Décisions Codex · 18.10.2026

- `tools/etapes.json` est un chemin, pas une commande : faux positif, couvert par ssp-pilotage-codex.
- Audits neuro, tête-cou, glossaire, Érasistrate et rapport : déjà couverts par ssp-audit-medical et les scripts régionaux ; ne pas automatiser le jugement clinique par simple remplacement.
- Monographies Panacée : ssp-construction-ck et mono_build.py ; prévalences : procédure P1–P7 et prev_build.py.
- Références visuelles : ssp-qualite-visuelle ; étapes Codex : ssp-pilotage-codex. Aucun nouveau doublon utile.
- Le lecteur AIPS réutilisable et ses trois tests sont décrits dans ssp-aips-verbatim.
