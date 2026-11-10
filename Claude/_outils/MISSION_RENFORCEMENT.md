# MISSION RENFORCEMENT — une leçon existante (LOTs G, 001–016) portée au verdict VERT

Ordre de Vial (10.11.2026) : les LOTs G doivent être lisibles à 100 %. La leçon existe sur `main`, mais elle cite par paragraphe
(`[S1]`) et `controle3` la classe ROUGE ou ORANGE (chiffres non sourcés phrase par phrase, doses sans extrait AIPS, phrases longues
ou nominales). Tu la reconstruis dans la chaîne M5 en gardant son fond, sans en perdre l'essentiel.

1. Applique `Claude/_outils/MISSION_REDACTION.md` et `BRIEF_REDACTION.md`, avec ces différences.
2. **Base** : le HTML existant `Claude/LOT_XXX/<fichier>` est ton plan et ta matière (structure des 14 points, fenêtres, tableaux,
   algorithme). Son titre `<h2>` reste identique. Sa bibliographie fournit tes premières URL (`urls.txt`) ; ajoute les recommandations
   suisses ou européennes plus récentes si nécessaire. `--dci` : les molécules que la leçon traite.
3. **Règle** : chaque phrase chiffrée cite l'ID d'un extrait lu qui contient ce chiffre ; chaque dose cite l'extrait AIPS
   (`aips-<n°>-<k>`) et le recopie. Une affirmation sans extrait lu est supprimée et notée dans `_travail/<CIBLE>/HELP.md` ;
   aucune formule de lacune dans le cours. **Avant toute suppression d'un élément essentiel** (critères diagnostiques, schémas
   thérapeutiques, durées, indications chirurgicales, algorithme) dont la source est illisible (403, PDF binaire), cherche une
   source lisible équivalente : texte intégral PMC ou Europe PMC, pocket guideline, synthèse suisse ou européenne qui la reprend.
   Le renforcement ne doit jamais appauvrir la leçon. Un nombre que la source écrit en toutes lettres s'écrit en toutes lettres
   comme elle, cité ; jamais remplacé par une formule vague.
4. `finir --lot XXX --cible <CIBLE> --titre "<titre exact>"` jusqu'au **VERT**, dans la bande 100–200 Ko. Le HTML final remplace
   l'ancien au même chemin.
Rapport ≤ 6 lignes : verdict, octets, éléments supprimés faute de source, HELP. Ne commite rien.
