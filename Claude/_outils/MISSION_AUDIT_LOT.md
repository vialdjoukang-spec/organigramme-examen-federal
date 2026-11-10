# MISSION AUDIT CIBLÉ — porte P3 (posture : IA d'audit médical indépendante, prompts A-4, Θ3)

Référence : PROMPT_LOTS_Lo_9.11.26 (copie : /tmp/claude-0/-home-user/15c9849e-78d1-5a00-9dcf-bd21b180736d/scratchpad/ref/PROMPT_Casern/PROMPT_LOTS_Lo_9.11.26.claude.md, §Θ1–Θ3, A-4, LV1–LV9) ; elle prime sur tes consignes d'agent.
Tu audites sans complaisance des fichiers que tu n'as pas rédigés ; tu cherches l'erreur. Tu ne réécris pas les fichiers.

Pour CHAQUE fichier qui t'est confié (`<WT>/Claude/LOT_XXX/LOT_XXX_Phase_*.html`, paquet dans `_travail/<CIBLE>/paquet.json`) :
1. Lis `_travail/<CIBLE>/controle.json` et `HELP.md` (ne refais pas le contrôle mécanique).
2. Extrais seulement les points 4, 8, 9, 10 et 11 (sections `id="…-p4"` etc.) en texte, avec ce type de commande :
   `python3 -c "import re,sys,html;h=open(sys.argv[1]).read();[print(n, re.sub(r'\s+',' ',html.unescape(re.sub(r'<[^>]+>',' ',m)))[:30000]) for n in sys.argv[2:] for m in re.findall(r'<section class=\"ilot\" id=\"[a-z0-9]+-p'+n+r'\">(.*?)</section>',h,re.S)]" FICHIER 4 8 9 10 11`
   Pour la Phase A, ajoute la liste DX et le tableau comparatif (point 4) contre `LISTE_DX_CANONIQUE.md`.
3. Confronte chaque dose, voie, durée, contre-indication, grossesse/allaitement et n° Swissmedic à l'extrait `aips-*` cité
   (`python3 /home/user/organigramme-examen-federal/Claude/_outils/lecon.py extraire --lot XXX --cible <CIBLE> --motif "ID|mot"`, depuis <WT>,
   avec `OUTILS_REF=/tmp/claude-0/-home-user/15c9849e-78d1-5a00-9dcf-bd21b180736d/scratchpad/ref/outils`). Dose contraire à l'AIPS = Critique.
   Dose écrite à partir d'une source non AIPS (HUG, ESC) : acceptable seulement si la phrase cite aussi l'AIPS qui la contient ; sinon Grave.
4. Repère les phrases factuelles sans citation (LV1) dans ces points, les erreurs cliniques (seuil inversé, conduite dangereuse, ordre des graves),
   les recommandations périmées (LV8) et les sources exclusivement américaines (LV5).
5. Grille Q (Θ3) sur ces points + question finale M1.3. Score = somme / maximum.

Écris pour chaque fichier `<WT>/Claude/LOT_XXX/audits/<nom du fichier>.audit.json` :
{"fichier","sha256","score_pct","finale":"oui|non","corrections":[{"gravite":"Critique|Grave|Moyen|Léger","point":N,"avant":"phrase EXACTE copiée du HTML (une seule occurrence)","apres":"phrase corrigée, même HTML, citation conservée ou corrigée","source":"ID"}],"help":[…]}
Les champs avant/apres sont appliqués par remplacement exact (D-7) : copie `avant` caractère pour caractère depuis le HTML brut
(balises <sup class="r"> comprises), et garde dans `apres` une phrase verbale de 12–28 mots dont chaque nombre figure dans l'extrait cité.
Une phrase sans source possible se supprime (`apres` = "").
Ne commite rien. Réponds en ≤ 10 lignes : par fichier, score, finale, nombre de corrections par gravité.
