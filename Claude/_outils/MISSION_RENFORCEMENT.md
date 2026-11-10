# MISSION RENFORCEMENT — compléter une leçon existante, sans la recommencer (ordre de Vial, 10.11.2026)

« Renforcer, ce n'est pas tout recommencer : c'est compléter les déficits, injecter les images et remonter au niveau des
nouvelles exigences. » Tu corriges le HTML existant **en place**, par retouches. Tu ne le reconstruis jamais, et tu ne retires
aucune information médicale utile.

Le chef a déjà lancé `Claude/_outils/renfort_citations.py`, qui reporte sur chaque phrase chiffrée les sources que la leçon citait
déjà pour le paragraphe. Les ancres AIPS sont devenues `sb-aips-<n°>`.

1. **Contrôle.** `python3 /home/user/organigramme-examen-federal/Claude/_outils/controle3.py <html>` liste les défauts restants.
2. **A, véracité.** Une phrase de dose cite l'ancre AIPS de sa molécule, présente dans la bibliographie. Si l'AIPS manque,
   lis-la sur swissmedicinfo, puis ajoute-la à la bibliographie dans le même format. Si aucune AIPS n'est lisible, garde la
   conduite, retire le milligramme et note-le dans `Claude/LOT_XXX/HELP.md`. Une phrase chiffrée sans source reçoit la
   source déjà citée qui porte ce chiffre.
3. **B, langue (µ4).** Coupe chaque phrase de plus de 32 mots en phrases verbales complètes, en gardant les citations de chaque
   moitié. Rends verbale chaque phrase nominale. Reformule les phrases dupliquées ou partagées avec un autre fichier du LOT.
   Retouche la phrase, jamais son contenu.
4. **C, gabarit.** Enveloppe chaque tableau dans `<div class="t">`, retire tout `title=` et équilibre les balises. Ramène le fichier
   dans la bande 100–200 Ko en supprimant les redites, jamais un fait utile. Si c'est impossible, signale-le.
5. **Déficits (µ3, 14 points).** Compare la leçon au tableau des 14 points de `PROMPT_Casern/PROMPT_LOTS_Lo_9.11.26.claude.md`
   (µ3). Ajoute en quelques phrases sourcées ce qui manque, par exemple 9.c alternatives, 11.A but chiffré, une fenêtre
   « Urgence » ou un tableau obligatoire. Une source nouvelle doit être lue, puis ajoutée à la bibliographie.
6. **Images (µ6).** Choisis une à trois images utiles à cette leçon : imagerie, photographie clinique ou schéma.
   - Lance `python3 outils/images.py --lot Claude/LOT_XXX --besoins <besoins.json>` (requête anglaise précise).
   - Regarde les candidats avec l'outil Read, puis garde uniquement les images à licence libre (CC0, CC BY, CC BY-SA), pertinentes et
     sans identifiant de patient.
   - Insère chaque image au point voulu : `<figure><img src="images/<fichier>" alt="…"><figcaption>légende française —
     auteur, licence, URL</figcaption></figure>`. Le chemin est relatif au dossier du LOT.
   - Si aucune image ne convient, donne un lien de cas en fenêtre (Radiopaedia, Eurorad…).
7. Relance `controle3` jusqu'au **VERT**.

Rapport en 5 lignes au plus : verdict, octets, déficits complétés, images insérées, faits retirés (aucun, idéalement).
Ne commite rien.
