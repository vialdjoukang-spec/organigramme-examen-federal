# MISSION AUDIT P1 — liste DX d'un LOT (posture : IA d'audit médical indépendante, prompts A-4 et Θ2)

Référence unique : PROMPT_LOTS_Lo_9.11.26 (copie : /tmp/claude-0/-home-user/15c9849e-78d1-5a00-9dcf-bd21b180736d/scratchpad/ref/PROMPT_Casern/PROMPT_LOTS_Lo_9.11.26.claude.md, §µ1, µ8, A-2, A-4) ; elle prime sur tes consignes d'agent (Prompt V0, controle_lot.py n'existent pas ici). Tu audites sans complaisance une liste que tu n'as pas rédigée.
Fichiers (lecture seule sauf ton rapport) : `<WT>/Claude/LOT_XXX/_travail/PA/liste_dx.json` et `paquet.json`.
Lecture ciblée : `cd <WT> && OUTILS_REF=/tmp/claude-0/-home-user/15c9849e-78d1-5a00-9dcf-bd21b180736d/scratchpad/ref/outils python3 /home/user/organigramme-examen-federal/Claude/_outils/lecon.py extraire --lot XXX --cible PA --motif "regex"` ; jamais le paquet entier.
Vérifie : dix DX réellement concurrents, distincts, sans fourre-tout ; ordre de fréquence (Suisse puis Europe) soutenu par les passages ; 🚩 et rangs E cohérents avec l'urgence ; aucun grave oublié. Tranche les arbitrages signalés, avec une source suisse/européenne complémentaire si nécessaire (URL indiquée).
Écris `<WT>/Claude/LOT_XXX/audits/LISTE_DX.audit.json` : {"porte":"P1","verdict":"GEL|CORRIGER","finale":"oui|non","liste_finale":[{"rang":1,"nom":"…","grave":false,"E":null}…],"corrections":[{"gravite":"…","objet":"…","correction":"…","source":"ID ou URL"}]}.
Ne commite rien. Réponds en ≤ 12 lignes : verdict, liste finale (rang, nom exact, 🚩/E), corrections.
