# CHANGELOG — PROMPT_Casern

## L1 — 10.11.2026 (ordre de Vial, bloquant)

- Nouveau nom de version : `PROMPT_LOTS_L1_10.11.26.{claude,codex,grok}.md` (remplace Lo_10.11.26).
- Cours entier de 80 à 150 Ko, fenêtres centrales occultantes (CSS `:target`) comprises ; seules les images sont hors limite (précision de Vial du 10.11.2026).
- Les examens complémentaires (biologie, imagerie interprétée et juxtaposée), l'anamnèse (symptômes caractérisés, typiques ou non) et l'examen physique ciblé (ordre topo-systémique : signe, technique, aspect ou son) se déploient en fenêtres.
- Le point 1 devient « Définition » seule. La sémantique et les notions voisines sont interdites, comme l'arbre CIM emboîté et le sommaire en boutons.
- Phrases verbales obligatoires ; toute persévération ou redondance est prohibée.
- Le front-end est uniforme du LOT 1 au LOT 248 (forme.css), avec une palette strictement différente d'un cours à l'autre, sans bleu. L'agent designer francophone est obligatoire.
- Porte bloquante `tools/garde/prompt_l1.py` dans le contrôle obligatoire `garde` : une PR de LOT porte la ligne « Prompt L1 lu et appliqué ».

## Lo 10.11.26 — 2026-11-10 (Claude, ordre de Vial)
- `PROMPT_LOTS_Lo_10.11.26.claude.md` remplace µ6 par **µ6 v2 : l'image, objet d'enseignement**. Elle est sourcée, interprétée (paire brut/annoté, lecture guidée, pièges, décision) et juxtaposée au point qu'elle sert. Une couverture minimale est fixée par point.
- Base : l'inventaire de 2 061 figures des LOTs 133–248 (`Claude/_outils/inventaire_images.py`). 86 % de ces figures sont des SVG ; 23 seulement ont une lecture guidée et 11 une licence citée. Modèles retenus : LOT_191 et LOT_133.
- Le reste du texte est identique à Lo 9.11.26.

## Navigation — 2026-11-08
- Le prompt de production le plus récent prouvé est le V0 révisé le 30 octobre 2026, commit `541c396da0b8358850fdc3fef4ff1194691936fd`. Ce texte n’est pas sur `main`.
- `00_LIRE_EN_PREMIER.md` pointe vers cette révision. Il ne prescrit plus V8.
- La copie `PROMPT_ULTIME_PRODUCTION_LOTS_V0.md` sur `main` reste celle du 26 octobre 2026.
- Les entrées V8, V7 et du 25 octobre 2026 ci-dessous sont inchangées. Aucun fichier n’a été supprimé.

## V8 — 2026-10-25 Europe/Zurich (Grok Bot)
- Remplace **PROMPT V7** (22.10.2026) comme prompt de production en vigueur.
- Demande obligatoire au démarrage : confirmer l’usage de PROMPT V8 (PROMPT_Casern).
- Noms de fichiers Appel A/B : motif `*_V8_*` (plus `*_V7_*`).
- Nouvelle section **HARNESS / BOUCLE DE VÉRITÉ** (expérience LOT_011 G11 + LOT_012 G12 / PR #436).
- Lieu de travail clarifié : GitHub `lot en cours de production/` d’abord ; Drive Finaux seulement si A+B validés ; pas de `lots-acheves` GitHub.
- Silence owner : blockers → Grok Bot uniquement.
- Vague inverse 248→001 documentée ; départ **LOT_226** O7.4 si assigné.
- Nouveau `PROMPT_HARNAIS_V8` (compréhension / mise en place / contrôle / vérif régulière) + PDF.
- `PLAN_HARNESS_ENGINEERING_V8` généralisé (plus limité à LOT_011), boucle de vérité, workflow 2026-10-25.
- Dossier agent-lisible `PROMPT_Casern/` publié GitHub + miroir Drive Finaux.

## V7 — 2026-10-22
- Prompt ultime production lots (14 pts, sources CH→EU, AIPS, HTML 90–200 Ko, audits, HELP).



## 2026-10-25 (màj) — Anti-collision & parallélisme absolu
- Ajout `ANTI_COLLISION_PARALLELISME_ABSOLU.md` (**outil d’onsession**)
- V8 §0 quater ; §5.3 corrigé
- Signé Grok Bot

---

*Signé : Grok Bot — 2026-10-25 Europe/Zurich — PROMPT_Casern / organigramme-examen-federal*
