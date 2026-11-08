
> Copie du **25 octobre 2026** dans `PROMPT_Casern/`. Elle est antérieure à `harnais/HARNAIS_OBLIGATOIRE.md` du 26 octobre 2026 sur `main`, lui-même antérieur à la révision du 30 octobre 2026 : [HARNAIS OBLIGATOIRE, rév. 30.10.2026](https://github.com/vialdjoukang-spec/organigramme-examen-federal/blob/6b6bee7b4c4aa99e4f261c2a5cc635744c0cec16/harnais/HARNAIS_OBLIGATOIRE.md). Le texte ci-dessous est conservé.

## Étape zéro (BLOQUANT) — avant toute activité

1. **Création / installation** du harnais sur l’agent (`harnais/` + bracelet)
2. **Test** : `python3 harnais/bracelet/bracelet_suggest.py "…"`
3. **Confirmation de fonctionnement** : PREUVE_EMBOITEMENT verte (Chonkie 1.6 · LLMLingua 1.3 · GPTCache 1.3)
4. **GO** (owner ou Grok Bot) — seulement ensuite : production

Sans étape zéro complète → stop.

# HARNAIS OBLIGATOIRE — embotté (Vial, 2026-10-25 Europe/Zurich)

BLOQUANT : confirmation obligatoire que le harnais **fonctionne** (PREUVE verte) **avant toute activité** ; sans cela, tu ne produis pas.

## Contenu embotté
- `harnais/ARSENAL.md`
- `harnais/bracelet/` (`bracelet_suggest.py`, `BRACELET_OPTIMISATION.md`, `catalog.json`)
- `harnais/plan_harness_engineering_lot11.html`

## Protocole
1. Lire `harnais/ARSENAL.md`.
2. `python3 harnais/bracelet/bracelet_suggest.py "<tâche>"`.
3. `tools/arsenal/extrait.py` / `lot.py` / `pr.sh` / `ci_attente.sh`.
4. Monographie V8 14 pts SSP + DD ; silence owner ; pas Drive Finaux avant validation.
5. Écrire `harnais/PREUVE_EMBOITEMENT.txt` (date + sortie bracelet + ARSENAL lu).

---

*Signé : Grok Bot — 2026-10-25 Europe/Zurich — PROMPT_Casern / organigramme-examen-federal*
