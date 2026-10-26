# HARNAIS OBLIGATOIRE — V0 renforcé (26.10.2026)

**BLOQUANT : sans exécuter ce harnais, tu ne produis pas.** Ce fichier remplace la version du 25.10.2026. Il ne contient plus aucune règle de dépôt externe : le dépôt final est `LOT_Claude_Finaux/`.

## Contenu embotté

- `harnais/ARSENAL.md` · `harnais/bracelet/` (`bracelet_suggest.py`, `BRACELET_OPTIMISATION.md`, `catalog.json`)
- `harnais/controle_lot.py` — contrôles mécaniques d'un LOT, extraction de points, manifeste
- `harnais/scinder_1_10.py` — découpe d'un HTML multi-DD en 1 HTML par DD
- `harnais/ROUTAGE_MODELES.md` · `.claude/agents/` — bascule des modèles
- `harnais/PREUVE_EMBOITEMENT.txt` — preuve datée, jamais inventée

## 1. Protocole (étape zéro)

1. Lire `harnais/ARSENAL.md`, puis ce fichier, puis `harnais/ROUTAGE_MODELES.md`.
2. `python3 harnais/bracelet/bracelet_suggest.py "<tâche>"`. Le script suggère 1 à 3 outils **pour cette tâche** ; le top-3 change avec le texte. Tu en appliques 1 à 3, jamais les 19.
3. Écrire `harnais/PREUVE_EMBOITEMENT.txt` en **ajoutant** un bloc (date Europe/Zurich, tâche, sortie réelle collée sans retouche, code de sortie, `ARSENAL_lu`, `HARNAIS_lu`, producteur). Une PREUVE inventée invalide la session.
4. `python3 -m py_compile harnais/controle_lot.py harnais/scinder_1_10.py` : doit réussir.
5. **PREUVE verte → GO.** Sinon : `ARRET.md`, stop.

Relancer le bracelet : au démarrage, au début de chaque LOT, avant chaque PR, après tout incident.

## 2. Boucle de vérité (avant chaque pas non trivial)

(1) Le harnais est-il en place ? (2) Le respecté-je maintenant ? Réponse « non » → corriger avant d'agir. Pas non trivial = collecte de sources, rédaction, audit, PR, dépôt.

## 3. Paramètres d'économie (par défaut ; qualité d'abord)

| # | Paramètre | Valeur |
|---|---|---|
| P1 | Contrôle mécanique avant tout appel modèle | `controle_lot.py verifier` à chaque fichier ; une non-conformité mécanique renvoie au rédacteur **sans** audit modèle |
| P2 | Lecture d'un HTML | jamais en entier au-delà de 50 Ko : `controle_lot.py extraire <fichier> --points N,N` |
| P3 | Partage de la lecture | auditeur médical : points 2, 3, 4, 8, 9, 11, 12 (+ liste, tableau, algorithme de la Phase A) ; auditeur linguistique : points 1, 5, 6, 7, 10, 13, 14 |
| P4 | Cycles rédaction → audit | 2 au plus par fichier ; 3ᵉ échec → verdict `REFUSE` consigné, LOT suivant |
| P5 | Cache | résultats mécaniques par SHA-256 dans `.cache/harnais/` ; extraits AIPS par n° Swissmedic dans `.cache/aips/` ; sources dans `evidence/` indexées par `evidence/INDEX.md` |
| P6 | Pas de relecture | SHA-256 identique au dernier verdict → verdict réutilisé |
| P7 | Entrées des agents | chemins et numéros de points, jamais du contenu collé |
| P8 | Sorties des agents | 15 lignes au plus + chemin du rapport ; rapports d'audit en tableaux, extraits ≤ 200 caractères |
| P9 | Parallélisme | LOT vide : 2 rédacteurs en parallèle (DX.1–5 et DX.6–10) **après** gel de la liste canonique ; 1 auditeur ; un seul LOT à la fois |
| P10 | AIPS | XML jamais ouvert en entier ; extraction ciblée par numéro ou DCI, puis cache |
| P11 | Escalade de modèle | sur échec constaté uniquement ([ROUTAGE_MODELES.md](ROUTAGE_MODELES.md)) |
| P12 | Sauvegarde du travail | commit + push après chaque fichier validé ; une session arrêtée sans push a produit zéro |
| P13 | Mémoire de file | `LOT_Claude_Finaux/ETAT_FILE.json` : file, cycles, scores, verdicts. On le lit, on ne relit pas l'historique |
| P14 | Jamais | lire `app_v2.html` en entier ; relire une PR entière ; suivre la CI à la main (`tools/arsenal/ci_attente.sh`) |
| P15 | Taille | bande **100–200 Ko** par fichier ; **bornes comprises**, jamais au-dessus de 200 Ko ; but = densité d'information, pas longueur |

## 4. Décider sans hésiter

| Situation | Décision |
|---|---|
| Le prompt, le brief ou ce harnais tranche | Tu appliques, sans question. |
| Plusieurs lectures possibles et aucune règle | Tu prends la plus prudente pour le patient, tu notes une ligne dans `JOURNAL.md`, tu avances. |
| Score < 90 %, un critique, ou question finale « non » | Retour au rédacteur (cycle +1). Aucun dépôt. |
| Molécule présente dans le corpus AIPS, dose non relue | Tu la lis dans le corpus. « À vérifier (AIPS) » est interdit. |
| Molécule absente du corpus et de swissmedicinfo.ch | « À vérifier (AIPS) » + question dans `HELP.md` ; le LOT reste déposable seulement si aucune dose n'est affirmée. |
| Aucune pièce source pour un LOT (dépôt, archive zip, Drive en lecture seule) | LOT **VIDE** : fabrication complète (3 agents). |
| Pièces présentes | LOT **NON VIDE** : audit médico-linguistique seul (2 agents) ; réécriture seulement si l'audit échoue. |
| Fichier > 200 Ko | Non conforme : tu comprimes la forme, jamais le fond. Fichier < 100 Ko : omission présumée, tu densifies. |
| CI rouge pour une raison propre au nouveau dossier | Tu corriges ta PR ; si la cause est la CI elle-même, tu l'écris dans `journal/echecs_fusion.md` et tu ne la modifies pas. |

## 5. STOP — et seulement dans ces cas

Corpus AIPS local absent ; droit d'écriture refusé ; filtre de sécurité ; harnais absent ; PREUVE impossible. Tu écris `LOT_Claude_Finaux/ARRET.md` (cause exacte, dernier état, prochaine action) et tu t'arrêtes. **Tu ne contournes pas.** Un lot refusé ou sans source n'est **pas** un blocage.

## 6. Interdits

Produire sans harnais · allumer tout le bracelet · économiser en amputant le fond · diluer pour paraître exhaustif · contourner un outil ou un filtre sans le dire · s'auto-auditer · toucher `PROMPT_Casern/`, `HANDOFF.md`, `ETAT.md`, `PROCHAINE_ACTION.md` sans mandat · déposer hors `LOT_Claude_Finaux/` · inventer une dose, un numéro Swissmedic, une URL, une PREUVE.
