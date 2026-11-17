Tu injectes dans le LOT_{N} des réponses DÉJÀ VÉRIFIÉES par un auditeur indépendant. Tu n'ajoutes RIEN qui ne figure pas dans le champ "a_injecter" des entrées vérifiées ; tu n'écris rien de mémoire.

Entrées :
- Entrées vérifiées pour ce lot : /tmp/claude-0/-home-user/71010596-18b4-52f5-b74d-84c8082950a7/scratchpad/rep/A_INJECTER_LOT_{N}.json (champs id, fichier_cible, emplacement, verdict, a_injecter, sources, affirmations).
- Questions d'origine (contexte exact de la lacune) : /tmp/claude-0/-home-user/71010596-18b4-52f5-b74d-84c8082950a7/scratchpad/rep/QUESTIONS_INDEX.json
- Fichiers du cours : /tmp/claude-0/-home-user/71010596-18b4-52f5-b74d-84c8082950a7/scratchpad/lot{N}/LOT_{N}_Appel_*.html (fichiers finaux, pas les *backup*/*pre*).
- Règles de style et gabarit : "/home/user/organigramme-examen-federal/claude/LOT Organigramme/PROMPT_ULTIME_PRODUCTION_LOTS_V7.md" (sections 7, 8, 10).

Méthode :
1. Avant toute modification, copie chaque fichier modifié en <nom>__preHELP.html dans le même dossier.
2. Pour chaque entrée : trouve l'emplacement (la mention « donnée non trouvée » correspondante ou le point concerné). Remplace la lacune par le contenu vérifié, réécrit en phrases courtes et verbales, au bon endroit du plan, en fenêtre <details> si c'est un détail, en tableau si c'est une liste de doses ou de seuils. Si le cours contenait une affirmation contraire à une valeur CORRIGÉE, corrige-la aussi.
3. Ajoute chaque source à la section Sources du fichier avec un numéro libre à partir de [S600], au format : [S6xx] Titre — Organisme — Année — URL — consulté le 23.10.2026. Cite ce numéro dans le texte injecté.
4. Contrôles avec python3 : balises équilibrées (html.parser, compte des <details>/<table>/<div> ouvrants et fermants), FIN_FICHIER présent en fin de fichier, aucun title=, aucune phrase sans verbe ajoutée. Note la taille ; si un fichier dépasse 200 000 octets, signale-le (ne coupe aucun contenu).
5. Écris /tmp/claude-0/-home-user/71010596-18b4-52f5-b74d-84c8082950a7/scratchpad/rep/INJECTION_LOT_{N}.json : [{"id":"","fichier":"","emplacement_reel":"","avant":"extrait court","apres":"extrait court","sources_ajoutees":["S600"]}] + {"fichiers_modifies":[{"nom":"","taille_avant":0,"taille_apres":0,"controles":"ok|…"}]}.
Réponds en 40 mots : entrées injectées, fichiers modifiés, tailles, anomalies.
