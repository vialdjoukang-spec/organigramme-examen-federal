---
name: ssp-synthese-locale
description: >-
  Lis ce skill avant de construire la « Synthèse locale » d’un module d’examen :
  icône verte, deux sous-onglets (A. Syndromes ; B. Diagnostics · Exploration ·
  Prise en charge), infobulles au survol et au clic.
---
# But
Ce skill donne à chaque zone explorée une synthèse locale complète et sans redondance.
# Déclencheur
Tu l’appliques à toute entrée de `data/ck/loc.json` et au rendu `loc|<module>|A` ou `loc|<module>|B`.
# Étapes
1. Tu listes les syndromes LOCAUX aux organes de la zone du module (exemple : neuro-nc → syndromes des nerfs crâniens, du tronc cérébral, du sinus caverneux, de l’apex orbitaire, de l’angle ponto-cérébelleux).
2. Sous-onglet A : chaque syndrome ouvre une infobulle avec les symptômes complémentaires à demander et l’orientation diagnostique.
3. Sous-onglet B : chaque diagnostic ouvre une infobulle avec le syndrome, l’examen de référence ou de 1re intention (et l’alternative), la 2e et la 3e intention, ce que chacun recherche, puis la prise en charge en étapes.
4. Tu réutilises par identifiant les entrées de syn.json et hyp.json ; tu ne recopies aucun texte.
5. Tu vérifies au clavier, à la souris et au toucher que chaque infobulle s’ouvre, s’épingle et se ferme (tests/test_ck.py).
# Interdits
Tu ne crées pas de syndrome hors de la zone ; tu renvoies vers le module concerné par un lien `x`.
# Règle universelle
Le projet cible doit avoir un résultat de HAUTE QUALITÉ. L’usage des jetons doit être raisonnable et optimisé, et tout gaspillage est formellement interdit. L’économie de jetons est autorisée si et seulement si elle ne dégrade pas la qualité du travail.
