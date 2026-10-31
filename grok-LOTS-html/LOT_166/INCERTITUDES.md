# Incertitudes — LOT_166

Faits retirés du cours ou non chiffrés, parce que la source ouverte ne les portait pas. Aucun n'est un critère central.

1. Prévalence suisse des dix causes : aucune série lue. Pas de pourcentage suisse dans le cours. Le 80 % de cirrhose parmi les ascites est le chiffre occidental de l'EASL 2018.
2. Texte intégral de l'ATLS, 10e édition : livre non ouvert. Les quatre fenêtres du FAST et l'ajout pleural de l'eFAST sont enseignés comme l'examen nommé dans le travail de 2021 sur le signe de la colonne, sans numéro de page ATLS.
3. Liste intégrale des 73 énoncés WINFOCUS 2012 : seul le résumé a été lu (65 recommandations fortes). Le cours ne fabrique pas la liste.
4. Seuil protéique qui sépare l'ascite cardiaque de l'ascite cirrhotique : pas dans l'extrait EASL ouvert. Le gradient haut des deux est enseigné, pas un chiffre de protéine inventé.
5. Signe du plancton : le titre de 2018 est cité, le résumé consulté ne donne pas de sensibilité. Le signe est dans le cours, sans pourcentage.
6. Dose d'aspirine anti-inflammatoire de la péricardite : l'information professionnelle ouverte (Aspirine Cardio) n'est pas ce schéma. Aucun gramme d'aspirine n'est affirmé. L'ibuprofène est dosé depuis le n° 48164, avec sa contre-indication en cas de cirrhose ou d'ascite.
7. Indication « péritonite bactérienne spontanée » : absente de l'extrait Ceftriaxon Labatec n° 59876. La fourchette 1 à 2 g, jusqu'à 4 g, est citée comme infections sévères, et le décalage est écrit dans le cours.
8. Schéma d'albumine 1,5 gramme par kilogramme puis 1 gramme par kilogramme, et 8 g/l d'ascite retirée : EASL 2018. Albunorm n° 62660 ne fixe pas ces chiffres. Le cours le dit.
9. Image pleurale Wikimedia : l'en-tête du fichier d'origine portait un nom. Il a été recadré avant dépôt. Ce n'est pas un retrait médical.

Bug noté, fichier non modifié : `grok-LOTS-html/outils/dessinateur/dessinateur.py`, fonction `verifier`. Elle exige dans la question les mots « faux chenal », « 2014 », « 2020 », « 2022 » et « Radiopaedia », contrôle écrit pour l'exemple de dissection aortique de LOT_150 et appliqué à toute commande `rendre`, qui quitte alors en échec. Les figures de LOT_166 sont produites par l'appel de `rendre()` puis `page()`, sans ce contrôle. Le fragment contient un script. La porte des leçons interdit `<script>`. La fenêtre de la leçon reçoit donc le fragment sans script (boutons radio, titre au survol, légende numérotée). La page `.htm` voisine garde le script.
