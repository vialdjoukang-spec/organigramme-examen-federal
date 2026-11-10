# MISSION CORRECTION — après audit P3 (posture : IA de rédaction, prompt A-5, correction chirurgicale)

Lis `Claude/_outils/BRIEF_REDACTION.md` (environnement). Pour CHAQUE fichier qui t'est confié, depuis <WT> :
1. Lis `Claude/LOT_XXX/audits/<html>.audit.json` (corrections, help).
2. Si une correction exige une AIPS absente du paquet, ajoute-la :
   `python3 $L prep --lot XXX --cible <CIBLE> --entite "<entité>" --ajouter --dci <racine> --autorisation <n° Swissmedic>`
   puis vérifie dans l'extrait (`extraire --prefixe aips --motif ...`) la dose, la voie, la durée et le texte grossesse/allaitement,
   et ajuste `apres` pour qu'il recopie l'AIPS et cite l'ID exact de l'extrait (`aips-<n°>-<k>`). Une correction dont l'appui reste
   introuvable : supprime la phrase (`apres` vide) plutôt que d'écrire un chiffre non sourcé. Le texte AIPS ne s'adoucit jamais.
3. Écris tes corrections finales dans `_travail/<CIBLE>/corrections.json` ([{"avant","apres"}…], `avant` copié EXACTEMENT
   depuis les fragments `_travail/<CIBLE>/fragments/pNN.html`), puis applique :
   `python3 /home/user/organigramme-examen-federal/Claude/_outils/appliquer.py XXX <CIBLE> --json Claude/LOT_XXX/_travail/<CIBLE>/corrections.json`
   (une phrase « NON TROUVÉE » : corrige `avant` et relance sur un fichier ne contenant que celle-ci).
4. Corrige aussi les phrases de sa classe signalées en `help` (versions périmées → version récente lue ; phrases « de mémoire » →
   citées ou supprimées ; formules de lacune « faute d'extrait lisible » → supprimées, la lacune va dans HELP.md).
5. `finir` jusqu'à verdict non ROUGE, bande respectée ; aucune autre réécriture (règle du passage unique).
Réponds en ≤ 8 lignes par fichier : corrections appliquées / supprimées / non applicables (raison), verdict, octets.
Ne commite rien.
