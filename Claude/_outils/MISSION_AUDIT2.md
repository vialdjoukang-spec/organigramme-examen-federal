# MISSION AUDIT P3 — second passage (posture : IA d'audit médical indépendante)

Référence : PROMPT_LOTS_Lo_9.11.26 §Θ2–Θ3 (copie : /tmp/claude-0/-home-user/15c9849e-78d1-5a00-9dcf-bd21b180736d/scratchpad/ref/PROMPT_Casern/PROMPT_LOTS_Lo_9.11.26.claude.md).
Pour chaque fichier `<WT>/Claude/LOT_XXX/LOT_XXX_Phase_*.html` confié : lis son premier audit `audits/<html>.audit.json` et vérifie
dans le HTML actuel (points 4, 8, 9, 10, 11 extraits comme dans `Claude/_outils/MISSION_AUDIT_LOT.md`) que chaque correction Critique
et Grave est appliquée correctement ; lis le point 11 en entier ; confronte chaque dose, contre-indication et texte grossesse/allaitement
à l'extrait AIPS cité (`python3 /home/user/organigramme-examen-federal/Claude/_outils/lecon.py extraire --lot XXX --cible <CIBLE> --motif "ID|mot"` depuis WT) ;
signale toute erreur Critique nouvelle. Ne refais pas un audit complet ; ne modifie aucun HTML ; ne commite rien.
Écris `audits/<html>.audit2.json` : {"fichier","sha256","score_pct","finale":"oui|non","verdict":"ACCEPTE|CORRIGER","restants":[{"gravite","point","avant","apres","source"}]}
(`avant` copié exactement du HTML, une seule occurrence). ACCEPTE : score ≥ 90 %, zéro Critique, finale « oui ».
Réponds en ≤ 14 lignes : tableau fichier/score/finale/verdict et défauts Critiques ou Graves restants.
