---
name: ssp-images-licence
description: >-
  Lis ce skill avant d’ajouter une image clinique : seules des images réelles, sous licence vérifiée
  et légères, entrent dans le dépôt.
---
# But
Ce skill empêche toute image sans licence, générée ou trop lourde.
# Déclencheur
Tu l’appliques avant d’ajouter une image dans assets/.
# Étapes
1. L’image provient d’une source retenue par le plan (section 9), par exemple Wikimedia Commons, Open-i ou Europe PMC.
2. Sa licence figure parmi les licences acceptées par le plan ; tu notes l’attribution complète (titre, auteur, source, licence).
3. Tu remplis `assets/cs/credits.json` : fichier, titre, auteur, URL source, licence, URL de licence, date de lecture, validé.
4. Tu convertis l’image en WebP de 200 Ko au plus, sans recadrage ni retouche qui modifie le signe clinique.
5. Le champ « validé » reste faux tant qu’un humain n’a pas confirmé le signe.
# Interdits
Aucune image générée, dessinée par IA ou en SVG ne remplace une image clinique réelle.
# Règle universelle
Le projet cible doit avoir un résultat de HAUTE QUALITÉ. L’usage des jetons doit être raisonnable et optimisé, et tout gaspillage est formellement interdit. L’économie de jetons est autorisée si et seulement si elle ne dégrade pas la qualité du travail.
