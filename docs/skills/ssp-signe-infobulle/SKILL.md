---
name: ssp-signe-infobulle
description: >-
  Lis ce skill dès qu’un texte de l’application emploie un signe, un syndrome ou
  un terme médical spécialisé : chaque terme s’ouvre, au survol, au clic et au
  toucher, sur sa définition tirée du glossaire imbriqué, y compris les termes
  employés dans une définition.
---
# But
Ce skill garantit qu’aucun signe, syndrome ni terme médical spécialisé ne reste sans définition, à aucun niveau d’imbrication.
# Déclencheur
Tu l’appliques avant de livrer tout texte visible (TIP, NOT, GES, données CK, glossaire lui-même, HTML statique) et à chaque rapport de l’automate Lyncée.
# Ce qui est automatique (tu ne le fais pas à la main)
- Détection : `python3 tools/lyncee.py` repère les termes candidats dans tout le texte, définitions comprises (glossaire, MeSH français, morphologie médicale, éponymes, abréviations, moins le lexique courant et `qa/termes_exclus.txt`).
- Liaison : `gloLink()` pose `data-t="glo|id"` à l’affichage, dans les pages ET dans le corps de chaque infobulle ; aucune balise n’est écrite dans TIP, NOT ou GES (budget de 6 Mo protégé).
- Garde : la CI échoue sur tout terme nouveau non défini ; `qa/termes-baseline.json` ne peut que baisser.
# Ce qui demande ta rédaction et ta relecture
1. Tu cherches le terme dans `data/ck/glo.json` (identifiant, libellé, flexion, synonyme). S’il existe, tu n’écris rien.
2. Sinon, tu crées l’entrée selon `data/ck/schema/glo.schema.json` : `type` (signe, syndrome, terme, examen, abréviation, éponyme) ; `def` en une à trois phrases dans les termes propres au terme (pour un signe : ce que l’on voit, palpe, entend ou mesure, et comment on le recherche) ; `composantes` pour un signe composite (exemple : faciès cushingoïde = faciès lunaire, pléthore faciale, comblement sus-claviculaire, bosse de bison, hirsutisme, acné, vergetures pourpres larges) ; `orientation` en une phrase si utile ; `src` (URL, paragraphe ou page) et `lu_le`.
3. Chaque terme spécialisé employé DANS ta définition doit exister dans le glossaire (exemple : « pléthore » dans la définition du faciès cushingoïde) ; Lyncée te liste ceux qui manquent, et tu les crées.
4. Pas de cycle direct : une définition ne s’emploie pas elle-même et n’est pas circulaire ; Lyncée signale ces cas. L’affichage limite la pile à 5 niveaux et ne relie pas un terme déjà ouvert.
5. Sans source suisse ou européenne lue, l’entrée porte `statut: "À vérifier"` et ouvre un ticket « Point à vérifier ».
6. Un terme courant (non spécialisé) va dans `qa/termes_exclus.txt` avec un motif écrit d’une ligne.
7. Validation : tous les signes et syndromes sont relus, plus un échantillon de 10 % des autres termes (décision du 17.10.2026) ; Asclépios recoupe les entrées écrites par Galien ou Hippocrate.
# Interdits
Pas de définition vague, circulaire ou nominale ; chaque phrase contient un verbe conjugué. Pas de composante inventée. Pas d’exclusion sans motif pour faire passer la CI.
# Règle universelle
Le projet cible doit avoir un résultat de HAUTE QUALITÉ. L’usage des jetons doit être raisonnable et optimisé, et tout gaspillage est formellement interdit. L’économie de jetons est autorisée si et seulement si elle ne dégrade pas la qualité du travail.
