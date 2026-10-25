
## Étape zéro (BLOQUANT) — avant toute activité

1. **Création / installation** du harnais sur l’agent (`harnais/` + bracelet)
2. **Test** : `python3 harnais/bracelet/bracelet_suggest.py "…"`
3. **Confirmation de fonctionnement** : PREUVE_EMBOITEMENT verte (Chonkie 1.6 · LLMLingua 1.3 · GPTCache 1.3)
4. **GO** (owner ou Grok Bot) — seulement ensuite : production

Sans étape zéro complète → stop.

# PROMPT HARNAIS V8 — compréhension, mise en place, contrôle, vérification

**Public :** tout agent (Cursor Cloud, ChatGPT Sol Moyen, auditeur) qui produit un lot PROFILES.
**Date :** 2026-10-25 Europe/Zurich · remplace les consignes harnais ad hoc des LOT_011 / LOT_012.

---


## 0. Confirmation obligatoire avant toute activité

**BLOQUANT (owner 2026-10-25).** Avant **toute** activité d’agent : exécuter `python3 harnais/bracelet/bracelet_suggest.py "…"`, écrire/rafraîchir `harnais/PREUVE_EMBOITEMENT.txt`, vérifier top-3 Chonkie 1.6 · LLMLingua 1.3 · GPTCache 1.3. **Sans preuve verte → zéro production.**

## 1. Compréhension — qu’est-ce que le harnais ?

Le **harnais** (harness) est l’ensemble des outils **autour** de l’agent, pas l’agent lui-même. Il force la précision, coupe le gaspillage de jetons et empêche la production sans preuve.

Sur `main` (PR **#436**, SHA de référence post-LOT_012) :

| Pièce | Rôle |
|---|---|
| `harnais/bracelet/bracelet_suggest.py` | Suggère le top d’outils pour la tâche (Chonkie **1.6**, LLMLingua **1.3**, GPTCache **1.3**, etc.) |
| `harnais/bracelet/catalog.json` | Catalogue d’outils du bracelet |
| `harnais/bracelet/BRACELET_OPTIMISATION.md` | Doctrine bracelet |
| `harnais/ARSENAL.md` | Économie de jetons : `extrait.py`, `lot.py`, `pr.sh`, `ci_attente.sh` |
| `harnais/HARNAIS_OBLIGATOIRE.md` | Protocole bloquant |
| `harnais/PREUVE_EMBOITEMENT.txt` | Preuve datée que le harnais a été exécuté |

Sans harnais, l’agent relit trop, invente, oublie les sources CH, et s’épuise.

---

## 2. Mise en place — checklist d’embarquement

1. Confirmer que tu es sur une branche basée sur `main` **après** PR #436 (dossier `harnais/` présent à la racine du dépôt).
2. Lire entièrement `harnais/HARNAIS_OBLIGATOIRE.md` puis `harnais/ARSENAL.md`.
3. Vérifier l’exécutable : `python3 harnais/bracelet/bracelet_suggest.py --help` ou une tâche sèche.
4. Si le dossier manque : **stop** ; signaler à Grok Bot ; ne pas inventer un bracelet parallèle.
5. Copie locale de travail autorisée sous `/cursor/stores/.../harnais/` pour tests, mais la **source de vérité** reste `harnais/` sur `main`.

---

## 3. Contrôle — boucle de vérité (permanente)

Avant **chaque** pas non trivial (crawl, rédaction d’une monographie, audit, ouverture PR, dépôt) :

1. **Harnais en place ?** — fichiers présents, lecture ARSENAL faite dans cette session.
2. **Je le respecte ?** — j’ai appelé `bracelet_suggest` pour cette tâche ; je suis le top-3 ; je n’ai pas lu `app_v2.html` entier ; je n’écris pas dans Drive Finaux trop tôt.

Cette boucle n’est **pas** une question unique au démarrage : c’est un réflexe récurrent (« boucle de vérité »).

---

## 4. Vérification fonctionnelle régulière

### 4.1 Exécuter le bracelet
```bash
python3 harnais/bracelet/bracelet_suggest.py "<description courte de la tâche>"
```
Exemple : `python3 harnais/bracelet/bracelet_suggest.py "evidence SSP O7.4 sources CH OFSP Obsan"`

### 4.2 Lire le top-3
La sortie liste des outils ordonnés. **Top-3** = les trois premiers pertinents pour la tâche. Tu les utilises (ou tu justifies par écrit pourquoi tu en choisis un autre). Ignorer systématiquement le bracelet = non-respect du harnais.

### 4.3 Écrire la PREUVE
Fichier `harnais/PREUVE_EMBOITEMENT.txt` (ou `PREUVE_EMBOITEMENT_HOST.txt` en local de test) :
```
date: 2026-10-25T.. Europe/Zurich
tâche: ...
bracelet_sortie: <coller la sortie réelle>
ARSENAL_lu: oui
agent: <nom>
```
**Crédibilité :** la sortie doit matcher un run local réel du script. Une PREUVE inventée est une violation de la section « Honnêteté sur tes actes » du PROMPT V8.

### 4.4 Rythme
- Au **démarrage** de session / Appel A / Appel B
- Avant chaque **gros fetch** ou guideline longue
- Avant **ouverture de PR**
- Après tout **suspect** (erreur MCP, lecture trop large, oubli AIPS)

### 4.5 R15 Automates
Ne **jamais** mettre `harnais/*` dans les puces « Automates actifs » du corps de PR. Uniquement workflows CI / outils réellement touchés.

---

## 5. Interdits liés au harnais

- Produire sans PREUVE à jour
- Contourner `extrait.py` / lire `app_v2.html` entier
- Inventer une dose faute d’AIPS (écrire « À vérifier (AIPS) »)
- Annoncer Drive Finaux avant A+B validés
- Chatter l’owner (blockers → Grok Bot)

---

## 6. Lien avec PROMPT V8

Le fichier `PROMPT_ULTIME_PRODUCTION_LOTS_V8.md` intègre la section **0 bis HARNESS / BOUCLE DE VÉRITÉ**. Ce présent document est le **prompt interne de compréhension** du harnais : à lire au démarrage avec le V8, puis à reconsulter dès que la boucle de vérité répond « non ».


---

*Signé : Grok Bot — 2026-10-25 Europe/Zurich — PROMPT_Casern / organigramme-examen-federal*
