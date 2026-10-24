# Suivi des LOT 227 à 248

**Tunder lit ces fichiers en premier.** Ils indiquent, LOT par LOT, ce qui est fait et où chercher.

| Fichier | Agent | LOT |
|---|---|---|
| [SUIVI_AGENT_1_LOT_227-237.md](SUIVI_AGENT_1_LOT_227-237.md) | Agent 1 | LOT_227 à LOT_237 |
| [SUIVI_AGENT_2_LOT_238-248.md](SUIVI_AGENT_2_LOT_238-248.md) | Agent 2 | LOT_238 à LOT_248 |

## Principes

- Un fichier par agent : les deux agents n'écrivent jamais dans le même fichier, ce qui évite tout conflit de fusion.
- Chaque agent coche ☑ chaque LOT réellement terminé selon le V7, avec la date et l'heure de Zurich, une note brève (par exemple « LOT_230 fait ») et l'endroit où chercher.
- Le signal officiel de fin de série est une issue GitHub intitulée `[FIN DE SÉRIE] Agent N — LOT_x–y`, avec l'étiquette `fin-de-serie`. L'étiquette `audit-ok` est interdite.
- Le chat sert uniquement aux urgences.

## Lecture rapide

1. Ouvrez le fichier de l'agent concerné.
2. Comptez les ☑ : ils donnent les LOT terminés sur 11.
3. Suivez le lien de la colonne « Où chercher ».
4. L'issue `[FIN DE SÉRIE]` confirme la clôture d'une série.
