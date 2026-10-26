# MESSAGE DE DÉMARRAGE — CLAUDE CODE — V0 (rév. 26.10.2026)

CLAUDE — lis dans cet ordre, puis exécute :

1. `PROMPT_Casern/MESSAGE_DEMARRAGE_CLAUDE_V0.md` (ce fichier) — brief : périmètre, file, plages FAIT / NON FAIT, règles, dépôt.
2. `PROMPT_Casern/PROMPT_ULTIME_PRODUCTION_LOTS_V0.md` — référence : 14 points, audit, Harness. (Un PDF du même texte peut exister ; le `.md` fait foi.)
3. `harnais/HARNAIS_OBLIGATOIRE.md`, puis `harnais/ROUTAGE_MODELES.md`.

**BLOQUANT avant tout :** mettre en place le Harness — Prompt V0 §5 / §5.1 (étape zéro : bracelet → ARSENAL → PREUVE_EMBOITEMENT). Sans Harness en place = pas de production.

**Périmètre actuel :** uniquement les LOTS déjà FAIT (Phase A + Phase B), soit 75 LOTS. Enchaîne progressivement LOT par LOT : audit Harness + V0 → dépôt immédiat dans `LOT_Claude_Finaux/LOT_XXX/` (11 HTML séparés). Les LOTS NON FAIT ne sont pas concernés pour le moment.

**Catalogue = 248 SSP** (PROFILES 2023), **jamais 256** : même liste, forme éclatée localement. `LOT_n` ↔ nom exact du SSP, dans `LOT_Claude_Finaux/CATALOGUE_248.csv`.

**Pas d'attente de validation de Vial.** Droits : lecture et écriture sur le dépôt, pour cette mission.

## Priorité sur le `CLAUDE.md` racine

Le `CLAUDE.md` racine, `CONTINUATION.md` et `tools/porte.py` pilotent la feuille de route Codex (Étape 0 → 17). Pour cette mission, **ce brief a priorité** : tu ne lances pas `tools/porte.py commencer`, et `ETAT.md`, `HANDOFF.md`, `PROCHAINE_ACTION.md`, `PROMPT_Casern/` restent en **lecture seule** (Prompt V0 §15). Tu gardes les règles de fond du dépôt : doses AIPS suisse uniquement, sources lues et datées sinon « À vérifier », aucune donnée personnelle, `/workspace/ssp/app.html` intouchable.

## FAIT = Phase A + Phase B

- **Phase A** = monographie du SSP + liste des 10 DD (diagnostics différentiels) classés + tableau comparatif + algorithme.
- **Phase B** = 10 monographies DD.

Plages (cumul au 25.10.2026) :

- **FAIT (75) :** 001→012 · 041→042 · 073→078 · 104→113 · 137→148 · 181→183 · 208→218 · 227→231 · 233→244 · 246→247
- **NON FAIT (173) :** 013→040 · 043→072 · 079→103 · 114→136 · 149→180 · 184→207 · 219→226 · 232 · 245 · 248

## File d'attente — règles d'exécution

1. **Un seul LOT à la fois**, dans l'ordre croissant des LOTS FAIT. « Le précédent » = le LOT FAIT précédent dans cette liste (après 012 vient 041).
2. **Un LOT est terminé quand son verdict est consigné** dans `LOT_Claude_Finaux/ETAT_FILE.json` : `ACCEPTE` (déposé), `REFUSE`, `SOURCE_ABSENTE` ou `BLOQUE`. Un LOT refusé ou sans source ne bloque pas la file.
3. Audit **médico + linguistique** avec le Harness et le Prompt V0 : 14 points de monographie ; **150–200 Ko par entité** (SSP ou DD), un fichier = une entité ; AIPS selon Prompt V0 §23.
4. Phase A d'abord ; si elle est conforme, gel de `LISTE_DX_CANONIQUE.md`, puis les 10 fichiers Phase B (jusqu'à 5 en parallèle).
5. Seuils de dépôt : **≥ 90 %**, **zéro critique**, question finale **« oui »**, LOT COMPLET (Phase A + 10 DD), `controle_lot.py verifier` = **CONFORME**.
6. Sous seuil : retour au rédacteur (cycle +1), **deux cycles au plus** ; ensuite verdict `REFUSE`, LOT suivant. Aucun auto-audit, aucun score reporté d'une version à l'autre.

## Sources d'entrée des LOTS FAIT

1. `lot en cours de production/LOT_XXX/` (LOT_011 et LOT_012 y sont).
2. L'archive d'export `LOTS_Finaux avec statut-*.zip`, que Vial dépose **à la racine du dépôt** (toutes ses parties). Elle n'est jamais modifiée ; tu en extrais **un LOT à la fois** dans `.cache/sources/LOT_XXX/` (dossier non versionné). Nom du dossier attendu : colonne `nom_dossier_attendu_dans_archive` du catalogue.
3. Aucune pièce → `SOURCE_ABSENTE`.

Si l'archive n'est pas encore à la racine, tu travailles d'abord sur les LOTS dont les pièces sont dans le dépôt, puis tu notes l'absence de l'archive dans `ETAT_FILE.json`. Tu ne cherches pas les pièces ailleurs.

## Livrable : 11 HTML par LOT (1 + 10)

- **Phase A : 1 HTML** — le SSP avec sa liste de DD classés, le tableau comparatif, l'algorithme, etc., comme le demande le Prompt V0 : `LOT_XXX_Phase_A_V0.html`.
- **Phase B : 10 HTML**, un par DD : `LOT_XXX_Phase_B_V0_DX.<i>.html`, `<i>` de 1 à 10. Titre = `DX.<i> — <nom exact de la liste canonique>`.
- **1 + 10 = 11 HTML pour 1 LOT.** Aucun HTML consolidé, aucun regroupement de DD.
- Les brouillons multi-DD existants se découpent avec `python3 harnais/scinder_1_10.py` (copie mot pour mot) ; le rédacteur redistribue les sections partagées.
- Le dépôt ne modifie en rien le contenu audité.

## Dépôt — sans validation de Vial

Après audit conforme : **déposer immédiatement** les 11 HTML, `MANIFESTE.json` et `audits/` dans `LOT_Claude_Finaux/LOT_XXX/`.

1. Branche `prod/lot-XXX-final` basée sur `main` ; un seul LOT par branche.
2. `python3 harnais/controle_lot.py manifeste LOT_Claude_Finaux/LOT_XXX` après le gel.
3. Commit, push, PR ; `tools/arsenal/ci_attente.sh` ; fusion par commit de fusion après CI verte (`gh pr merge --merge`).
4. Mise à jour de `ETAT_FILE.json`.

**Interdit** d'attendre un OK, un feu vert ou une validation de Vial : l'audit (Harness + Prompt V0) **est** la porte. **Aucun dépôt** hors de `LOT_Claude_Finaux/` — ni Google Drive, ni autre dossier. Pas de dépôt si l'audit n'est pas conforme, si le score est sous seuil ou si le LOT est incomplet.

## Modèles

Agent principal : Sonnet. Délégation aux agents de `.claude/agents/` (Haiku, Sonnet, Opus selon la tâche) : voir `harnais/ROUTAGE_MODELES.md`. Le rédacteur n'est jamais l'auditeur.

## Arrêt

Blocage sans contournement légitime (corpus AIPS local absent, écriture refusée, filtre de sécurité, harnais absent) : écris `LOT_Claude_Finaux/ARRET.md`, **arrête-toi**, ne contourne pas. Vial reprend le matin.

## Nettoyage

Exécute `NETTOYAGE.md` (racine de ce kit) **après** la première PR de dépôt fusionnée, dans une PR séparée `nettoyage-v0`.

## Première étape courte

Après l'étape zéro, crée `LOT_Claude_Finaux/PROGRESSION.html` : en-tête « Catalogue = 248 SSP (PROFILES 2023) », légende « FAIT = Phase A + Phase B » ; une ligne par LOT = n° + **nom du SSP PROFILES 2023** + score % Phase A + % Phase B + statut ; scores inconnus = « — ». Puis enchaîne les LOTS selon la file. **Pas de « 256 SSP » nulle part.**
