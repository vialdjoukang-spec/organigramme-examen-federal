# MISSION RÉDACTION — une leçon (posture : IA de rédaction, prompt A-1 ; chaîne M5 E2, E5, E6, E8)

Lis d'abord `Claude/_outils/BRIEF_REDACTION.md` et applique-le à la lettre ; puis lis `Claude/LOT_XXX/LISTE_DX_CANONIQUE.md` (liste gelée).
Tu rédiges UNE leçon : la Phase A (CIBLE = PA) ou un DX (CIBLE = DX.i). Tu n'écris que dans `Claude/LOT_XXX/_travail/<CIBLE>/`
et dans ton HTML final. Les autres rédacteurs du LOT travaillent en parallèle sur les autres cibles : ne touche pas à leurs dossiers.

## Sources
- Réutilise d'abord les URL pertinentes de `Claude/LOT_XXX/_travail/PA/urls.txt` (déjà en cache), puis ajoute des sources
  propres à ta cible (recommandation suisse ou européenne de l'entité, la plus récente ; épidémiologie ; physiopathologie ;
  examens ; traitement). DX : 8 à 15 URL propres à l'entité.
- `--dci` : racines de ta ligne dans `Claude/LOT_XXX/_travail/PA/dci.txt` (complète si la prise en charge l'exige).
  Une molécule sans AIPS lisible : classe et conduite sans milligramme, et entrée dans `_travail/<CIBLE>/HELP.md`.

## Contenu propre à la cible
- **DX.i** : monographie de l'entité en 14 points (µ3), centrée sur sa présentation dans la SSP du LOT ; `<h2>` = titre
  `DX.i — <nom exact de la liste gelée>`. Aucun renvoi « voir Phase A », aucun point omis. Point 4 : ses propres
  différentiels discriminants (les graves d'abord). Ne recopie aucune phrase d'un autre fichier du LOT.
- **PA** : monographie de la SSP en 14 points, avec en plus :
  - point 4 : la liste DX.1–DX.10 (noms EXACTS de la liste gelée, badge 🚩 et rang E, `<span class="freq">XX %</span>`
    seulement si sourcé, sinon « Ne rang » avec l'argument sourcé) puis le **tableau comparatif** dix lignes × cinq colonnes
    (signe clé, examen qui tranche, mécanisme, conduite immédiate, rang E) ;
  - point 10 : l'**algorithme**, qui commence par l'exclusion de E1, E2… puis discrimine les DX fréquents.
- SSP transversale (µ8) : points sans objet déclarés tels par une phrase verbale qui en donne la raison.

## Fin
Assemble et contrôle (`finir`), corrige jusqu'au verdict non ROUGE dans la bande 100–200 Ko, vise VERT.
Réponds en ≤ 12 lignes (verdict, octets, connecteur%, défauts restants, HELP, sources principales). Ne commite rien.
