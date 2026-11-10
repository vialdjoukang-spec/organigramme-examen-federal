> **BLOQUANT — PROMPT L1 (ordre de Vial du 10.11.2026).** Avant toute action sur un LOT, lis le bloc L1 en tête de ton prompt (`PROMPT_Casern/PROMPT_LOTS_L1_10.11.26.claude.md`, `.codex.md` ou `.grok.md`) et applique-le : cours entier de 80 à 150 Ko fenêtres comprises (seules les images sont hors limite), fenêtres centrales occultantes, point 1 = Définition seule, aucune ancienne architecture, phrases verbales sans redondance, front-end uniforme (forme.css) avec palette différente par cours, agent designer francophone. Toute PR de LOT porte la ligne « Prompt L1 lu et appliqué », sinon `garde` la refuse.

# 00 — LIRE EN PREMIER (PROMPT_Casern)

Tu ouvres ce dossier **avant** toute production de lot.

Correction de navigation du 8 novembre 2026. Le prompt de production courant est le **V0 révisé le 30 octobre 2026**. Cette révision n’est pas dans `main`. Les fichiers V8 du 25 octobre 2026 et la copie V0 du 26 octobre 2026 restent dans l’arbre : ils sont historiques.

## Étape zéro (BLOQUANT) — avant toute activité

1. **Création / installation** du harnais sur l’agent (`harnais/` + bracelet). Le texte qui fait foi est la révision du 30 octobre 2026 : [HARNAIS OBLIGATOIRE, rév. 30.10.2026](https://github.com/vialdjoukang-spec/organigramme-examen-federal/blob/6b6bee7b4c4aa99e4f261c2a5cc635744c0cec16/harnais/HARNAIS_OBLIGATOIRE.md). `harnais/HARNAIS_OBLIGATOIRE.md` sur `main` est la copie du 26 octobre 2026.
2. **Test** : `python3 harnais/bracelet/bracelet_suggest.py "…"`
3. **Confirmation de fonctionnement** : PREUVE_EMBOITEMENT verte (Chonkie 1.6 · LLMLingua 1.3 · GPTCache 1.3)
4. **GO** (owner ou Grok Bot) — seulement ensuite : production

Sans étape zéro complète → stop.

## Projet
Encyclopédie interactive PROFILES 2023 (248 SSP) pour l’examen fédéral suisse de médecine humaine — dépôt `vialdjoukang-spec/organigramme-examen-federal`.

## Ordre de lecture obligatoire
1. Ce fichier (`00_LIRE_EN_PREMIER.md`)
2. `LIEU_DE_TRAVAIL.md` — la section « Cumul » y est l’état daté du 25 octobre 2026
2bis. `ANTI_COLLISION_PARALLELISME_ABSOLU.md` — **outil d’onsession** : parallélisme absolu + zéro collision
3. **PROMPT ULTIME V0, révision du 30 octobre 2026**, à lire en entier. Commit `541c396da0b8358850fdc3fef4ff1194691936fd`, blob `18f7bf366074` : [PROMPT ULTIME V0, rév. 30.10.2026](https://github.com/vialdjoukang-spec/organigramme-examen-federal/blob/541c396da0b8358850fdc3fef4ff1194691936fd/PROMPT_Casern/PROMPT_ULTIME_PRODUCTION_LOTS_V0.md)
4. `MESSAGE_DEMARRAGE_CLAUDE_V0.md` — brief du 26 octobre 2026, seule version de ce fichier. Il indique le sens LOT_001 → LOT_248. Il ne remplace pas la révision du 30 octobre du prompt.
5. Routage des modèles, révision du 30 octobre 2026 : [ROUTAGE DES MODÈLES, rév. 30.10.2026](https://github.com/vialdjoukang-spec/organigramme-examen-federal/blob/565fb1a007adb945bd0ba41f3af03a89c5b9c64b/harnais/ROUTAGE_MODELES.md). `harnais/ROUTAGE_MODELES.md` sur `main` est la copie du 26 octobre 2026.

La révision du 30 octobre 2026 se lit sans demander une confirmation du numéro de prompt.

## En vigueur
- Prompt de production : **V0, révision du 30 octobre 2026** (lien du point 3). Son en-tête déclare qu’elle remplace V8 et V7. Date interne et dernier commit du fichier concordent.
- Copie sur `main` de `PROMPT_ULTIME_PRODUCTION_LOTS_V0.md` : révision du **26 octobre 2026**, conservée, elle ne fait plus foi.
- Harnais et routage qui font foi : révisions du **30 octobre 2026** (liens des points 1 et 5).
- Sens de la file : `MESSAGE_DEMARRAGE_CLAUDE_V0.md` du **26 octobre 2026** (LOT_001 → LOT_248), plus récent que le départ en sens inverse du 25 octobre 2026.

## Historique conservé
Ces fichiers restent dans le dépôt. Ils ne sont pas le prompt courant :

- `PROMPT_ULTIME_PRODUCTION_LOTS_V8.md` et son PDF
- `PROMPT_HARNAIS_V8.md` et son PDF
- `PLAN_HARNESS_ENGINEERING_V8.html` et son PDF
- `MESSAGE_DEMARRAGE_SENS_INVERSE.md` (départ LOT_226, procédure du 25 octobre 2026)
- `HARNAIS_OBLIGATOIRE.md` de ce dossier (copie du 25 octobre 2026, antérieure à `harnais/HARNAIS_OBLIGATOIRE.md`)

## Signature
Les fichiers de ce dossier sont signés **Grok Bot** et datés pour tracer l’évolution.

---

*Signé : Grok Bot — 2026-10-25 Europe/Zurich — PROMPT_Casern / organigramme-examen-federal*

*Pointeurs corrigés le 2026-11-08. Textes du 25 et du 26 octobre conservés. Aucun fichier supprimé.*
