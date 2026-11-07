# ROUTAGE DES MODÈLES — bascule économique (V0, 26.10.2026 ; rév. 30.10.2026)

Ordre de décision unique : **Qualité → Exhaustivité du fond → Économie → Esthétique.** L'économie est une sous-contrainte : on ne bascule vers un modèle moins cher que si le fond reste intact.

## Table de bascule

| Tâche | Qui | Modèle · effort | Pourquoi |
|---|---|---|---|
| Contrôles déterministes : tailles, 14 points, `FIN_FICHIER`, balises, `title=`, `popover`, liste DX A↔B, SHA-256, nommage 1 + 10 | **Script** `harnais/controle_lot.py` | aucun | Automatisme gratuit avant cognition payante. |
| Découpe d'un HTML multi-DD en 1 HTML par DD | **Script** `harnais/scinder_1_10.py` | aucun | Copie mot pour mot, aucune réécriture. |
| Rapport qualité (scores, corrections, avancement) | **Script** `harnais/rapport_qualite.py` | aucun | Agrégation déterministe des `.jsonl`. |
| Inventaires, tri, extraction de l'archive, manifestes, collage | Agent `mecanique` | **haiku · medium** | Tâche mécanique, risque nul. |
| Rédaction de la Phase A (elle fixe les 10 DD du LOT) | Agent `redacteur-phase-a` | **opus · xhigh** | Une liste DX fausse se propage aux 10 fichiers Phase B. |
| Rédaction d'un DD | Agent `redacteur` | **opus · xhigh** (remplace sonnet) | Chaque DD porte doses et conduites : le fond exige le meilleur modèle. |
| Audit médical avec correction en place : doses, seuils, AIPS, grossesse, conduite, ordre et gravité des DD | Agent `auditeur-medical` | **opus · xhigh** ; **max** si plus de 30 % à réécrire | Une erreur de dose est un risque vital ; l'auditeur corrige lui-même. |
| Audit linguistique et de conformité avec correction en place : langue, format, fenêtres, taille | Agent `auditeur-conformite` | **sonnet · high** | Tâche structurée, volumineuse ; le fond médical est déjà corrigé en amont. |
| Orchestration (session principale, « chef de production ») | Session principale | modèle de la session | Elle délègue, consigne, pousse ; elle n'écrit pas de contenu clinique. |

**Fable : non utilisé.** Aucun besoin démontré ; son surcoût n'est pas justifié ici.

## Aucun refus — celui qui trouve la faute la corrige (Prompt V0 §16.1)

1. **Ordre des audits pour un fichier** : `auditeur-medical` (fond, doses, conduite), puis `auditeur-conformite` (langue, format, fenêtres, taille).
2. **Correction en place.** Les deux auditeurs ont Edit et Write sur le fichier audité et sur `audits/`. Ils réécrivent, complètent ou sourcent eux-mêmes ; le rédacteur n'est jamais rappelé ; aucun fichier ne reste bloqué.
3. **Traçabilité.** Une ligne JSON par correction dans `LOT_Claude_Finaux/LOT_XXX/audits/corrections.jsonl` ; une ligne de scores (avant/après : médical, langue, prise en charge, examen) dans `audits/scores.jsonl`, avec taille et SHA-256 du fichier final.
4. **Au-delà de 30 % du fichier à réécrire** : l'`auditeur-medical` réécrit lui-même les points concernés en effort maximal. Il ne refuse jamais.

## Équipe par LOT

| LOT | Agents |
|---|---|
| **VIDE** (fabrication) | `redacteur-phase-a` ; puis `redacteur` (DX.1–5) et `redacteur` (DX.6–10) en parallèle après gel de la liste canonique ; chaque fichier passe par `auditeur-medical`, puis `auditeur-conformite` |
| **NON VIDE** (audit) | `auditeur-medical`, puis `auditeur-conformite`, chacun corrigeant en place |

## Règles qui tiennent la bascule

1. **Indépendance.** Un auditeur n'a jamais rédigé le texte qu'il audite : agent distinct, contexte vierge. Le fond médical est audité par un modèle de niveau supérieur ou égal à celui du rédacteur.
2. **Escalade sur échec constaté seulement** : plus de 30 % à réécrire, ou doute persistant sur une dose → effort maximal. Jamais « par précaution ».
3. **Désescalade systématique** : tout ce qu'un script ou Haiku sait faire ne monte jamais d'un cran.
4. **Journal de routage.** Chaque décision (agent, modèle, effort, raison) s'écrit en une ligne dans `journal/routage.jsonl`.
5. **Aucun tarif n'est écrit dans ce dépôt.** Prix et limites : docs.claude.com. Un chiffre non vérifié est interdit (Prompt V0 §4.2).

## Mise en œuvre dans Claude Code

- Les agents sont dans `.claude/agents/` : `mecanique`, `redacteur`, `redacteur-phase-a`, `auditeur-medical`, `auditeur-conformite`. Le frontmatter porte `model` (alias `haiku`, `sonnet`, `opus`) et `effort` (`medium`, `high`, `xhigh`, `max`).
- La session principale les invoque par leur nom et leur passe des **chemins**, jamais du contenu collé.
- Pour changer le modèle de la session principale : `/model`.

## Où va la plus grosse économie

Dans un LOT, la dépense dominante est la **lecture** : 11 fichiers de 80–150 Ko. Les leviers, par ordre d'efficacité :
1. `controle_lot.py` filtre tout ce qui est mécanique avant qu'un auditeur ne lise une ligne.
2. `controle_lot.py extraire --points …` : chaque auditeur lit d'abord ses points ([§16](../PROMPT_Casern/PROMPT_ULTIME_PRODUCTION_LOTS_V0.md)).
3. Extraits AIPS mis en cache par numéro Swissmedic (`.cache/aips/`), réutilisés par les 10 DD.
4. SHA-256 inchangé = scores inchangés : pas de relecture.
