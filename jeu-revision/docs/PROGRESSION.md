# PROGRESSION GLOBALE · INTERNAT

## 1. Échelle de maîtrise (pour chaque pathologie)
Fais gravir 7 échelons à chaque pathologie, du fondamental à la prise en charge :
1. **Fondamental** : relie la structure et la fonction (anatomie, physiologie, biochimie).
2. **Mécanisme** : explique la physiopathologie qui produit les signes.
3. **Clinique** : fais reconnaître le signe clé et les drapeaux rouges.
4. **Démarche et différentiels** : fais classer les hypothèses, celles qui tuent d'abord, avec le signe qui les départage.
5. **Exploration** : fais choisir l'examen qui tranche et rejeter l'examen inutile.
6. **Diagnostic** : fais appliquer les critères suisses.
7. **Prise en charge** : fais aller des mesures générales aux spécifiques, puis au suivi, avec une prescription personnalisée et sans abus.
Ne déclare une pathologie **maîtrisée** qu'après les 7 échelons réussis avec la confiance « sûr », deux fois, à J+1 et à J+7, et rappelle-la à J+30.

## 2. Traqueur de progression (outil réel, écran « Tableau de bord »)
- Enregistre chaque coup : carte, échelon, réponse, confiance, temps de réponse, gravité de l'erreur.
- Affiche une carte de chaleur spécialité × échelon : on voit d'un coup d'œil, par exemple, qu'on rate l'exploration en néphrologie.
- Calcule la calibration : compare la confiance déclarée au taux de réussite ; signale l'excès de confiance.
- Liste les angles morts : erreurs commises avec « sûr », drapeaux rouges manqués, différentiels mortels oubliés.
- Mesure la vitesse : temps médian par échelon, objectif Urgence sous 20 s.
- Planifie la révision par répétition espacée (Leitner, 5 boîtes) et propose chaque jour une « Ronde » de 20 minutes bâtie sur les points les plus faibles.
- Estime une préparation à l'examen par domaine PROFILES, en ne comptant que les pathologies maîtrisées.
- Exporte et importe la progression en fichier JSON : le stockage du navigateur seul se perd si on vide le cache ou si on change d'appareil.

## 3. Grades
Fais monter le joueur d'Externe à Interne, puis Chef de clinique, puis Médecin cadre, selon la part de pathologies maîtrisées (25, 50, 75, 90 %).

## 4. Cycle de chaque spécialité
1. Fondamentaux : enchaîne des duels courts sur les échelons 1 et 2.
2. Consultation : déroule un cas par pathologie, sans chronomètre, en pénalisant l'excès d'examens.
3. Urgence : déroule les cas graves sous chronomètre.
4. Cas final : combine plusieurs pathologies et comorbidités, sous chronomètre, avec piège.
5. Planche : produis `planches/<specialite>.html` avec 4 captures (parcours, duel, fiche, tableau de bord) et la couverture (pathologies couvertes et manquantes, taux « À vérifier »).

## 5. Ordre global
Phase 0 (moteur et traqueur) → lots A à G des spécialités → paraclinique → disciplines transversales → sciences fondamentales transversales → **examen blanc PROFILES** (cas mêlés de toutes les spécialités, chronométrés, notés comme à l'examen).
