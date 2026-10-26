# MESSAGE DE DÉMARRAGE — CLAUDE CODE — V0 (rév. 26.10.2026)

CLAUDE — lis dans cet ordre, puis exécute :

1. `PROMPT_Casern/MESSAGE_DEMARRAGE_CLAUDE_V0.md` (ce fichier) — brief : périmètre, file, équipes, règles, dépôt.
2. `PROMPT_Casern/PROMPT_ULTIME_PRODUCTION_LOTS_V0.md` — référence : 14 points, audit, Harness. Le `.md` fait foi.
3. `harnais/HARNAIS_OBLIGATOIRE.md`, puis `harnais/ROUTAGE_MODELES.md`.

**BLOQUANT avant tout :** Harness — Prompt V0 §5 / §5.1 (étape zéro : bracelet → ARSENAL → PREUVE_EMBOITEMENT). Sans Harness en place = pas de production.

**Catalogue = 248 SSP** (PROFILES 2023), **jamais 256**. `LOT_n` ↔ nom exact du SSP, dans `LOT_Claude_Finaux/CATALOGUE_248.csv`. **Pas d'attente de validation de Vial.** Droits : lecture et écriture sur le dépôt, pour cette mission.

## Priorité sur le `CLAUDE.md` racine

Le `CLAUDE.md` racine, `CONTINUATION.md` et `tools/porte.py` pilotent la feuille de route Codex. Pour cette mission, **ce brief prime** : pas de `tools/porte.py commencer`. `ETAT.md`, `HANDOFF.md`, `PROCHAINE_ACTION.md`, `PROMPT_Casern/` restent en **lecture seule** (Prompt §15). Règles de fond conservées : doses AIPS suisse uniquement, sources lues et datées sinon « À vérifier », aucune donnée personnelle, `/workspace/ssp/app.html` intouchable.

## Périmètre, sens, file active

- **Les 248 LOTS**, dans le sens **LOT_001 → LOT_002 → … → LOT_248**.
- **File active de 10 LOTS par exécution** (ex. 001→010) ; à la fin, arrêt propre et mise à jour de `LOT_Claude_Finaux/PROGRESSION.html`.
- **Un seul LOT à la fois.** Le LOT n+1 ne démarre (ni transformation ni fabrication) que si le LOT n est **ACHEVÉ** :
  - `ACCEPTE` : 11 HTML audités déposés dans `LOT_Claude_Finaux/LOT_XXX/`, poussés et **mergés** ;
  - ou `REFUSE` (deux cycles d'audit non conformes) / `BLOQUE` : verdict consigné dans `LOT_Claude_Finaux/ETAT_FILE.json` et **mergé**.

## Deux cas par LOT (déterminés par les pièces sources, pas par le catalogue)

| État | Travail | Agents |
|---|---|---|
| **VIDE** (aucune pièce) | **Fabrication** : Harness, bracelet, P1–P15 appliqués fermement | **3** : rédacteur 1 (Phase A, puis DX.1–5), rédacteur 2 (DX.6–10 après gel de `LISTE_DX_CANONIQUE.md`), 1 auditeur médico-linguistique |
| **NON VIDE** (pièces présentes) | **Audit médico-linguistique uniquement** ; pas de réécriture si l'audit passe | **2** : 1 auditeur ; 1 rédacteur activé **seulement** si l'audit échoue |

L'**auditeur est unique, indépendant, costaud** : deux grilles séparées (médicale Opus : points 2, 3, 4, 8, 9, 11, 12 ; conformité/langue Sonnet : points 1, 5, 6, 7, 10, 13, 14), qui s'en tient au Prompt V0 (§11, §12, §16, §19). Jamais le rédacteur.

## Livrable : 11 HTML par LOT (1 + 10)

- **Phase A : 1 HTML** — SSP + liste des 10 DD classés + tableau comparatif + algorithme : `LOT_XXX_Phase_A_V0.html`.
- **Phase B : 10 HTML**, un par DD : `LOT_XXX_Phase_B_V0_DX.<i>.html`, `<i>` de 1 à 10. Titre = `DX.<i> — <nom exact de la liste canonique>`.
- **Taille : 100–200 Ko par fichier, bornes comprises (aucune non-conformité dans cet intervalle) ; au-dessus de 200 Ko : jamais.** Le but est la **densité d'information**, pas la longueur : l'intervalle est large pour qu'aucune notion ne soit omise. Hors intervalle, moins de 100 Ko = omission présumée ; plus de 200 Ko = non conforme (tu comprimes la forme, jamais le fond).
- Aucun HTML consolidé, aucun regroupement de DD. Les brouillons multi-DD se découpent avec `python3 harnais/scinder_1_10.py` (copie mot pour mot).
- **Seuils de dépôt :** ≥ 90 %, zéro critique, question finale « oui », LOT COMPLET, `controle_lot.py verifier` = CONFORME.

## Sources d'entrée (lecture seule)

1. `lot en cours de production/LOT_XXX/`.
2. L'archive `LOTS_Finaux avec statut-*.zip` à la racine du dépôt (jamais modifiée) ; un LOT à la fois dans `.cache/sources/LOT_XXX/`.
3. Drive de Vial, **lecture seule** : https://drive.google.com/drive/folders/1DaFAd0uamsJQY2NH0ocuy2bhpfcVk9Vu — sous-dossier « ARCHIVES — Contenu des LOTS 001 à 020 — avant reprise du LOT 011 » (pièces des LOTS 002 à 006 ; les dossiers `LOT_002`…`LOT_006` de niveau supérieur sont vides). Drive inaccessible : verdict `BLOQUE` (`ARCHIVES_INACCESSIBLE`), pas de fabrication par-dessus.
4. Aucune pièce nulle part = LOT VIDE = fabrication.

## Dépôt — sans validation de Vial

Après audit conforme : **déposer immédiatement** les 11 HTML, `MANIFESTE.json` et `audits/` dans `LOT_Claude_Finaux/LOT_XXX/`.

1. Branche `prod/lot-XXX-final` basée sur `main` ; un seul LOT par branche.
2. `python3 harnais/controle_lot.py manifeste LOT_Claude_Finaux/LOT_XXX` après le gel.
3. Commit, push, PR ; `tools/arsenal/ci_attente.sh` ; fusion par commit de fusion après CI verte (`gh pr merge --merge`).
4. Mise à jour de `ETAT_FILE.json` (dans une PR mergée).

**Interdit** d'attendre un OK de Vial : l'audit (Harness + Prompt V0) **est** la porte. **Aucun dépôt** hors de `LOT_Claude_Finaux/` — pas de dépôt sur le Drive. Pas de dépôt si l'audit n'est pas conforme, si le score est sous seuil ou si le LOT est incomplet.

## Modèles

Agent principal : Sonnet. Délégation aux agents de `.claude/agents/` : voir `harnais/ROUTAGE_MODELES.md`. Le rédacteur n'est jamais l'auditeur.

## Arrêt

Blocage sans contournement légitime (corpus AIPS local absent, écriture refusée, filtre de sécurité, harnais absent) : écris `LOT_Claude_Finaux/ARRET.md`, **arrête-toi**, ne contourne pas. Vial reprend le matin.

## Nettoyage

Exécute `NETTOYAGE.md` **après** la première PR de dépôt fusionnée, dans une PR séparée `nettoyage-v0`.

## Première étape courte

Après l'étape zéro, crée `LOT_Claude_Finaux/PROGRESSION.html` : en-tête « Catalogue = 248 SSP (PROFILES 2023) » ; une ligne par LOT de la file active = n° + nom du SSP + état (VIDE / NON VIDE) + score % Phase A + % Phase B + verdict ; scores inconnus = « — ». **Pas de « 256 SSP » nulle part.**
