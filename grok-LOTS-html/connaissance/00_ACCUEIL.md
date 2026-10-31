# 00 Accueil — base de connaissance de la production Grok (LOTS 134–248)

Nœud central. Chaque note de ce dossier renvoie ici et à au moins une autre note : aucune note orpheline (`python3 grok-LOTS-html/outils/vault_lint.py`).

| Note | Rôle | Qui l'écrit | Quand on la lit |
|---|---|---|---|
| [PIEGES.md](PIEGES.md) | mémoire persistante des pièges et leçons (ID `P-xx`, symptôme, cause, parade) | Tunder, à chaque défaut répété ou nouveau | début de chaque passe (déjà dans le paquet de contexte) |
| [PROMPTS_QUI_MARCHENT.md](PROMPTS_QUI_MARCHENT.md) | messages de lancement constants par poste | Tunder | au lancement d'un run |
| [COUTS.jsonl](COUTS.jsonl) | une ligne par passe : coût relatif mesuré (`outils/couts.py noter`) | script | fin de passe ; bilan par LOT |
| [CONSO.jsonl](CONSO.jsonl) | durée, octets, jetons estimés, fenêtres, VM (`outils/compteur_conso.py`) | script | `debut` / `fin` de chaque fichier |
| [PREVISION_SIMULATION.json](PREVISION_SIMULATION.json) | coûts prévus par la simulation (HYPOTHÈSES), à comparer au réel dans `couts.py bilan` | Tunder | après 3 à 5 LOTS réels |
| [TARIFS_RELATIFS.json](TARIFS_RELATIFS.json) | barème relatif des modèles (HYPOTHÈSES à remplacer par les valeurs réelles de l'abonnement) | Vial / Tunder | quand le tarif réel change |
| [HOOKS.md](HOOKS.md) | garde pre-commit : ce qu'elle contrôle, comment l'ajouter au crochet existant | Tunder | installation, dépannage |
| [certitude_redaction.py](../outils/certitude_redaction.py) | script de certitude du rédacteur (31.10.2026) : 14 points, doses AIPS mot pour mot, chiffres datés, tailles V8, leçons des audits 134/135 ; VERT / ORANGE / ROUGE, zéro jeton | rédacteur | avant chaque commit de leçon |
| [ADR/](ADR/) | décisions d'architecture datées (une par fichier) | Tunder | avant de changer le circuit |
| [JOURNAL_CONNAISSANCE.md](JOURNAL_CONNAISSANCE.md) | journal quotidien, une ligne par fait notable, renvoie vers PIEGES / ADR | Tunder | fin de journée |

## Règles de la base (tirées du graphe Obsidian étudié)
1. Un hub, des rayons : toute note est atteignable en un clic depuis cet accueil.
2. Un incident = une entrée de `PIEGES.md` + une ligne de journal qui la cite ; jamais l'un sans l'autre.
3. Une décision = un ADR numéroté (contexte, décision, conséquences, date) ; on ne réécrit pas un ADR, on le remplace par un nouveau.
4. Les coûts se notent à chaque passe, pas à la fin : sans mesure, aucune optimisation n'est prouvée.
5. Le paquet de contexte inclut `PIEGES.md` et `PROMPTS_QUI_MARCHENT.md` : la mémoire sert avant l'erreur, pas après.
6. Budget : `PIEGES.md` ≤ 8 Ko dans le paquet ; au-delà, archiver les pièges résolus dans `ADR/`.

Liens : [Journal](JOURNAL_CONNAISSANCE.md) · [Décisions](ADR/ADR-001_porte_zero_jeton.md)
