# ROUTAGE DES MODÈLES — bascule économique (V0, 26.10.2026)

Ordre de décision unique : **Qualité → Exhaustivité du fond → Économie → Esthétique.** L'économie est une sous-contrainte : on ne bascule vers un modèle moins cher que si le fond reste intact.

## Table de bascule

| Tâche | Qui | Pourquoi |
|---|---|---|
| Contrôles déterministes : tailles, 14 points, `FIN_FICHIER`, balises, `title=`, liste DX A↔B, SHA-256, nommage 1 + 10 | **Scripts** : `python3 harnais/controle_lot.py verifier …` | Automatisme gratuit avant cognition payante. Tout est déterministe. |
| Découpe d'un HTML multi-DD en 1 HTML par DD | **Script** : `python3 harnais/scinder_1_10.py …` | Copie mot pour mot, aucune réécriture. |
| Inventaires, tri, extraction de l'archive, manifestes, collage | Agent `mecanique` — **Haiku** | Tâche mécanique, risque nul. |
| Rédaction d'un DD ; audit linguistique et de conformité | Agents `redacteur`, `auditeur-conformite` — **Sonnet** | Bon rapport qualité/coût pour des tâches volumineuses et structurées. |
| Rédaction de la Phase A (elle fixe les 10 DD du LOT) | Agent `redacteur-phase-a` — **Opus** | Une liste DX fausse se propage aux 10 fichiers Phase B. |
| Audit médical : doses, seuils, AIPS, grossesse, ordre et gravité des DD | Agent `auditeur-medical` — **Opus** | Une erreur de dose est un risque vital ; l'économie ne passe pas avant ce critère. |
| Orchestration (agent principal, « chef de production ») | Session **Sonnet** | Elle délègue, consigne, pousse ; elle n'écrit pas de contenu clinique. |

## Équipe par LOT

| LOT | Agents |
|---|---|
| **VIDE** (fabrication) | 3 : `redacteur-phase-a` puis `redacteur` (DX.1–5) ; `redacteur` (DX.6–10) ; 1 auditeur médico-linguistique (`auditeur-medical` Opus, puis `auditeur-conformite` Sonnet) |
| **NON VIDE** (audit) | 2 : 1 auditeur médico-linguistique ; 1 `redacteur`, activé seulement si l'audit échoue |

## Règles qui tiennent la bascule

1. **Indépendance.** Le rédacteur d'un fichier n'est jamais son auditeur : agent distinct, contexte vierge. Le fond médical est audité par un modèle de niveau supérieur ou égal à celui du rédacteur.
2. **Escalade sur échec constaté seulement** : un critique médical trouvé, deux échecs sur le même fichier, ou un doute sur une dose. Jamais « par précaution ».
3. **Désescalade systématique** : tout ce qu'un script ou Haiku sait faire ne monte jamais d'un cran.
4. **Fable 5.1 : non utilisé** pour cette production. Aucun besoin démontré ; son surcoût n'est pas justifié ici.
5. **Aucun tarif n'est écrit dans ce dépôt.** Prix et limites : docs.claude.com. Un chiffre non vérifié est interdit (Prompt V0 §4.2).

## Mise en œuvre dans Claude Code

- Les agents sont dans `.claude/agents/` : `mecanique`, `redacteur`, `redacteur-phase-a`, `auditeur-medical`, `auditeur-conformite`. Le champ `model` utilise les alias `haiku`, `sonnet`, `opus` (suivent la version courante de chaque famille).
- L'agent principal les invoque par leur nom. Il passe des **chemins**, jamais du contenu collé.
- Pour changer le modèle de la session principale : `/model`.

## Où va la plus grosse économie

Dans un LOT, la dépense dominante est la **lecture** : 11 fichiers de 100–200 Ko. Les leviers, par ordre d'efficacité :
1. `controle_lot.py` filtre tout ce qui est mécanique avant qu'un auditeur ne lise une ligne.
2. `controle_lot.py extraire --points …` : chaque auditeur ne lit que ses points ([§16](../PROMPT_Casern/PROMPT_ULTIME_PRODUCTION_LOTS_V0.md)).
3. Extraits AIPS mis en cache par numéro Swissmedic (`.cache/aips/`), réutilisés par les 10 DD.
4. SHA-256 inchangé = verdict inchangé : pas de relecture.
