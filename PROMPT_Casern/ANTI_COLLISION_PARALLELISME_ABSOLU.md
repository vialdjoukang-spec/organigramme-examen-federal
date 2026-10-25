# Anti-collision & parallélisme absolu — outil de session

**Règle bloquante — outil d’onsession.** À charger avec le harnais et le PROMPT V8 dès l’ouverture de session. Objectif : réduire à la nullité conflits Git, collisions de fichiers et double rédaction du même lot.

## 1. Parallélisme absolu d’action

Plusieurs agents / outils (Cursor, ChatGPT Sol Moyen, etc.) **peuvent et doivent** travailler **en même temps**, sans s’attendre.

Condition unique : **chemins et lots disjoints**.

- Un agent = **un seul LOT assigné** à la fois.
- Vague basse (ex. LOT_011 / LOT_012) et vague inverse (248→001, départ LOT_226) **coexistent** tant que les numéros de lot ne se croisent pas.
- Au croisement (même LOT réclamé deux fois) : **stop** ; Grok Bot arbitre ; jamais « je prends quand même ».

## 2. Isolation stricte (zéro collision)

| Zone | Règle |
|------|--------|
| Dossier lot | Tu n’écris **que** dans `lot en cours de production/LOT_XXX/` du LOT assigné. |
| Autre LOT_* | Tu ne modifies **jamais** un autre `LOT_*`. |
| Branche Git | Une branche **par lot** : `cursor/lot-XXX-…`. Jamais deux lots sur la même branche. |
| PR | Une PR = un lot (ou docs PROMPT_Casern seuls). |
| `harnais/` | Preuve sur ta branche de lot si besoin ; pas de force-push `main` ; ne « répare » pas le harnais d’autrui. |
| `PROMPT_Casern/` | **Lecture seule** pour les producteurs. Seul Grok Bot (ou GO owner) met à jour. |
| Drive Finaux | Jamais un lot incomplet. Jamais écraser le dossier d’un autre lot. |
| Fichiers globaux | Interdit `HANDOFF.md`, `ETAT.md`, inventaires, CI racine, sans mandat Grok Bot. |

## 3. Contrôles avant chaque écriture (outil de session)

1. Mon LOT assigné est-il encore le mien ?
2. Mon chemin cible est-il uniquement `…/LOT_XXX/` avec **mon** XXX ?
3. Ma branche porte-t-elle ce XXX seul ?
4. Personne d’autre n’écrit déjà ce LOT (PR / Drive) ?

Si doute → **stop** → Grok Bot.

## 4. OK vs interdit

**OK :** Appel B LOT_011 et LOT_012 en parallèle ; ChatGPT sur LOT_226 pendant Cursor sur 011/012 ; lectures concurrentes de PROMPT_Casern / harnais.

**Interdit :** deux agents sur le même LOT_XXX ; commit hors de son dossier ; merge qui écrase autrui ; lot incomplet dans Drive Finaux.


## 4 bis. Scripts régénératifs (exemple LOT_012 / PR #436)

Ne lance **pas** `tools/arsenal/pr.sh` (ni tout script qui régénère monographies / JSON cours) tant que le lot est en rédaction active (`tools/cours/lots/<SSP>.json` ou HTML Appel A/B en cours). C’est une **mesure anti-collision volontaire**, pas un oubli — à documenter dans la PR comme sur #436.

## 5. Phrase d’ancrage

« Je suis seul sur mon LOT ; les autres avancent en parallèle sur les leurs ; je ne croise jamais leurs chemins. »

---

*Signé : Grok Bot — 2026-10-25 Europe/Zurich — PROMPT_Casern / organigramme-examen-federal*
