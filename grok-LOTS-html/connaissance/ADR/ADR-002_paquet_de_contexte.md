# ADR-002 — Paquet de contexte par LOT et par poste (2026-10-31) — [Accueil](../00_ACCUEIL.md)

**Contexte.** Chaque run relit PROMPT_PRODUCTION_V2, PROMPT_GROK, rôle, brief, leçons, et (rédacteur) `MODELE_DD_V8.html` de 254 Ko.
**Décision.** `outils/contexte_lot.py construire LOT_XXX` écrit un fichier par poste, ordonné stable → volatil ; le modèle est remplacé par un squelette (≈ 21 Ko, résumé, l'original reste la référence). Premier message de run constant (PROMPTS_QUI_MARCHENT).
**Conséquences.** (+) lecture réduite, préfixe stable. (−) l'économie de cache dépend du fournisseur ; le squelette peut faire perdre un détail de gabarit : le rédacteur lit l'original en cas de doute et la porte contrôle la structure.
