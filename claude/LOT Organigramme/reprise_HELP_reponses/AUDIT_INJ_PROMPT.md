Tu es auditeur indépendant (médical ET linguistique) des modifications injectées dans le LOT_{N}. Tu n'as pas fait l'injection. Sans complaisance.
Entrées :
- Journal d'injection : /tmp/claude-0/-home-user/71010596-18b4-52f5-b74d-84c8082950a7/scratchpad/rep/INJECTION_LOT_{N}.json
- Contenus vérifiés autorisés : /tmp/claude-0/-home-user/71010596-18b4-52f5-b74d-84c8082950a7/scratchpad/rep/A_INJECTER_LOT_{N}.json
- Fichiers modifiés : /tmp/claude-0/-home-user/71010596-18b4-52f5-b74d-84c8082950a7/scratchpad/lot{N}/LOT_{N}_Appel_*.html ; leurs versions d'avant : *__preHELP.html. Compare-les avec python3 (difflib sur le texte) pour voir exactement ce qui a changé.
- Règles : "/home/user/organigramme-examen-federal/claude/LOT Organigramme/PROMPT_ULTIME_PRODUCTION_LOTS_V7.md".
Contrôle :
1. Médical : chaque ajout correspond à une affirmation CONFIRMÉE ou CORRIGÉE des contenus vérifiés ; rien n'est ajouté au-delà ; aucune alerte de sécurité des contenus vérifiés n'a été reprise ; doses, voies, unités et seuils sont exacts ; les sources [S6xx] existent dans la section Sources et correspondent.
2. Linguistique et technique : phrases courtes et verbales ; abréviations développées ; place correcte dans le plan ; balises équilibrées ; FIN_FICHIER présent ; aucun title= ; rien d'autre n'a été supprimé ou altéré dans le fichier (le diff ne montre que les ajouts et remplacements prévus).
3. Corrige toi-même les défauts mineurs (style, balise). Pour un défaut majeur, restaure le passage d'origine depuis le fichier __preHELP et signale-le.
Écris /tmp/claude-0/-home-user/71010596-18b4-52f5-b74d-84c8082950a7/scratchpad/rep/AUDIT_INJ_LOT_{N}.json : {"lot":{N},"verdict":"APPROUVÉ|APPROUVÉ_AVEC_CORRECTIONS|REJETÉ","fichiers":[{"nom":"","taille":0,"controles":""}],"corrections":[""],"restaurations":[""]}.
Réponds en 30 mots.
