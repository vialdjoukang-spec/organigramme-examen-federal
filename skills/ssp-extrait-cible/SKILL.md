---
name: ssp-extrait-cible
description: >-
  Lis ce skill avant toute lecture du fichier de travail app_v2.html : il remplace la lecture du
  fichier entier par une vue de code sans données.
---
# But
Ce skill fait lire environ 2 % du fichier au lieu de 5,4 Mo, sans rien perdre du code.
# Déclencheur
Tu l’appliques avant d’ouvrir app_v2.html, quelle que soit la raison.
# Étapes
1. Tu lances `python3 tools/slim.py` ; la vue s’écrit dans `.cache/app_v2.slim.html`.
2. Tu lis la vue avec des extraits ciblés (offset et limit), jamais en entier si un repère suffit.
3. Pour trouver un ancrage dans le vrai fichier, tu utilises Python et `str.find`, car les expressions régulières expirent sur des lignes de plusieurs millions de caractères.
4. Pour lire une donnée (TIP, NOT, GES, SSP, PHT), tu l’extrais avec ssp-json-data au lieu d’ouvrir le fichier.
# Interdits
Tu n’édites jamais la vue : elle sert à lire. Tu ne modifies jamais orig/app.html.
# Règle universelle
Le projet cible doit avoir un résultat de HAUTE QUALITÉ. L’usage des jetons doit être raisonnable et optimisé, et tout gaspillage est formellement interdit. L’économie de jetons est autorisée si et seulement si elle ne dégrade pas la qualité du travail.
