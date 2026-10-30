# Leçons de LOT_016 (à appliquer dès la Phase A de LOT_017)

1. **Potassium i.v.** : toujours écrire « contrôler la diurèse avant tout potassium » (AIPS KCl 29552 : « Contrôler la diurèse avant la perfusion. ») et citer ses contre-indications (acidose, déshydratation sévère) quand une conduite en donne. Critique de LOT_016.
2. **Kaliémie < 3,5 mmol/L** : potassium d'abord, insuline différée.
3. **Crise surrénalienne** : prélever cortisol et ACTH juste avant l'hydrocortisone si cela ne retarde rien ; adulte ESE/ES 2024 ; enfant BSPED 2023 (NICE NG243 y renvoie avant 16 ans).
4. **Artérite à cellules géantes** : « plus de 50 ans », avis spécialisé dans les 24 heures, jamais « sujet âgé » ni « plus de 65 ans ».
5. **Test VIH** : directive OFSP PICT 2015 (OPAS art. 12d), pas NICE QS157.
6. **Usage hors information professionnelle** : à écrire en clair chaque fois que la dose ou l'indication dépasse l'AIPS (doses de consensus, voies, âge), sans omettre la contre-indication AIPS correspondante.
7. **Contre-indications AIPS complètes** : chaque médicament conseillé dans une conduite d'urgence doit avoir sa contre-indication pertinente citée (esmolol et propranolol en insuffisance cardiaque, Néo-Mercazole et hyperthyroïdie à l'iode).
8. **Numéro Swissmedic par forme galénique** ; vérifier par script dans le XML.
9. **Diagnostics différentiels graves à ne pas omettre** au point 4 et dans l'arbre (PPR/ACG manquait dans DX.6).
10. **Taille** : viser 110–125 Ko au premier jet ; chaque audit ajoute 4 à 7 Ko ; plafond pratique 140 000 octets.
11. **Scratchpad** : un sous-dossier propre par agent (`<LOT>_<fichier>_<rôle>/`), jamais la racine partagée ni le dépôt.
12. **Extraits evidence** : toute nouvelle source citée a son extrait daté dans `evidence/` (le rédacteur ou la passe transversale l'écrit).
13. **Ne pas inventer un raisonnement comme recommandation** : un choix de traitement déduit des AIPS est écrit comme tel.
14. **Rappels de sciences fondamentales (ordre de Vial du 30.10.2026).** Pour les SSP dont le raisonnement repose sur l'anatomie et la physiologie (neuro-ophtalmologie et neurologie, endocrinologie et métabolisme, néphrologie, cardiologie, hématologie, etc.), le point 3 (physiopathologie) contient systématiquement les rappels de base indispensables à la compréhension (anatomie, physiologie, biochimie) : soit une explicitation brève entre parenthèses, soit un terme cliquable ouvrant une fenêtre `popover` qui l'explique (anatomie des voies, boucles de régulation, mécanismes). Rappels sourcés (manuel ou revue), courts, au service du raisonnement clinique ; l'auditeur médical vérifie leur exactitude, l'auditeur de conformité leur présence.
