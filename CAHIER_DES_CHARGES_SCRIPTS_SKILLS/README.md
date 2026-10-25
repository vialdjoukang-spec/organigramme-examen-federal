# Cahier des charges — scripts déterministes des agents de rédaction (version 1.3)

Ce dossier documente les scripts **livrés** dans `scripts_lots/` pour les agents de rédaction (Agent 1 : LOT_227–237 ; Agent 2 : LOT_238–248). Les scripts sont du code déterministe, sans aucune IA.

| Fichier | Contenu |
|---|---|
| `CAHIER_DES_CHARGES_SCRIPTS_SKILLS_GROK.md` | Règle n° 1 (silence des agents), architecture, script source, liste blanche validée, script synchrone en lecture seule, LanguageTool, compteur de jetons, plans de secours, tests et banc d'essai, décisions, modifications du V7-Tunder, limites |
| `RECHERCHE_OUTILS.md` | Relevé du 24.10.2026 des compétences et serveurs MCP |
| `controle_v7.py` | Copie de référence du script d'origine ; la version intégrée est `scripts_lots/common/controle_v7.py` |

Points essentiels :
- **Règle n° 1 :** les agents n'écrivent jamais à l'utilisateur, sauf LOT terminé, série terminée ou urgence, en une ligne de 15 mots au plus.
- Chaque agent utilise ses deux scripts : `scripts_lots/agent_N/script_source.py` et `script_synchrone.py`.
- `script_source.py check` bloque le dépôt d'un fichier contenant une affirmation non sourcée.
- Le script synchrone est strictement en lecture seule sur les LOT ; cinq tests et une analyse statique le prouvent.
- Dépôt : `lot/LOT_X`, dossier `LOTS/LOT_X/` ; plan B Drive « LOTS_Finaux avec statut ».
