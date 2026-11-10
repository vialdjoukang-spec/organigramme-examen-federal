# MISSION RENFORCEMENT — compléter une leçon existante, sans la recommencer (ordre de Vial, 10.11.2026)

« Renforcer, ce n'est pas tout recommencer : c'est compléter les déficits, injecter les images et remonter au niveau des
nouvelles exigences. » Tu corriges le HTML existant **en place**, par retouches. Tu ne le reconstruis jamais, et tu ne retires
aucune information médicale utile.

Le chef a déjà lancé `Claude/_outils/renfort_citations.py`, qui reporte sur chaque phrase chiffrée les sources que la leçon citait
déjà pour le paragraphe. Les ancres AIPS sont devenues `sb-aips-<n°>`.

0. **Interdit dans le cours** : toute formule de lacune (« À vérifier », « non lu », « aucune donnée suisse »). Une lacune va dans `Claude/LOT_XXX/HELP.md`.
1. **Contrôle.** `python3 /home/user/organigramme-examen-federal/Claude/_outils/controle3.py <html>` liste les défauts restants.
2. **A, véracité.** Une phrase de dose cite l'ancre AIPS de sa molécule, présente dans la bibliographie. Si l'AIPS manque,
   lis-la dans le corpus local (swissmedicinfo est illisible depuis ici) :
   `python3 Claude/_outils/lecon.py prep --lot XXX --cible <CIBLE> --ajouter --dci <racine> --aips-max 4` (ou `--autorisation <n°>`),
   puis `lecon.py extraire --lot XXX --cible <CIBLE> --prefixe aips --motif "<regex>"`, puis ajoute-la à la bibliographie dans le même format. Si aucune AIPS n'est lisible, garde la
   conduite, retire le milligramme et note-le dans `Claude/LOT_XXX/HELP.md`. Une phrase chiffrée sans source reçoit la
   source déjà citée qui porte ce chiffre.
3. **B, langue (µ4).** Coupe chaque phrase de plus de 32 mots en phrases verbales complètes, en gardant les citations de chaque
   moitié. Rends verbale chaque phrase nominale. Reformule les phrases dupliquées ou partagées avec un autre fichier du LOT.
   Retouche la phrase, jamais son contenu.
4. **C, gabarit.** Retire d'abord les polices intégrées (`@font-face` en data:) : le gabarit µ7 n'en prévoit pas. Enveloppe chaque tableau dans `<div class="t">`, retire tout `title=` et équilibre les balises. Ramène le fichier
   dans la bande 100–200 Ko en supprimant les redites, jamais un fait utile. Si c'est impossible, signale-le.
5. **Déficits (µ3, 14 points).** Compare la leçon au tableau des 14 points de `PROMPT_Casern/PROMPT_LOTS_Lo_9.11.26.claude.md`
   (µ3). Ajoute en quelques phrases sourcées ce qui manque, par exemple 9.c alternatives, 11.A but chiffré, une fenêtre
   « Urgence » ou un tableau obligatoire. Une source nouvelle doit être lue, puis ajoutée à la bibliographie.
6. **Images (µ6 v2, `PROMPT_Casern/PROMPT_LOTS_Lo_10.11.26.claude.md` sur la branche claude/prompt-lo-images, PR #601).**
   Une image est un objet d'enseignement, jamais une décoration. Couverture : au point 9, le cliché de la modalité décisive ;
   au point 6, le signe visible quand il existe.
   - Cherche : `python3 /home/user/organigramme-examen-federal/Claude/_outils/cliche.py chercher "<requête anglaise>"`.
   - Prends : `... cliche.py prendre "File:…" --lot Claude/LOT_XXX` (licence vérifiée, WebP, reprise sur 429). Sur un 429
     persistant, ne réessaie pas : ajoute la ligne `<chemin absolu du dossier LOT>|File:…` à `/home/user/wt/images_attente.txt`
     (une file unique télécharge en série), note l'insertion à faire dans HELP.md et continue.
   - Regarde l'image avec Read. Vérifie la modalité et la présence réelle du signe, puis place 1 à 4 repères en % (x, y).
   - Compose : `... cliche.py figure --meta Claude/LOT_XXX/images/<nom>.json --titre … --cliche "<modalité, incidence…>"
     --reperes '[[x,y,"lecture du repère"],…]' --pieges '["…"]' --decision "<conduite>"`, puis colle le bloc dans le point.
   - Remplace toute figure déjà présente sans lecture guidée par ce format.
7. Relance `controle3` jusqu'au **VERT**.

Rapport en 5 lignes au plus : verdict, octets, déficits complétés, images insérées, faits retirés (aucun, idéalement).
Travaille dans un dossier temporaire privé (`mktemp -d`), jamais dans un scratchpad partagé. Ne commite rien.
