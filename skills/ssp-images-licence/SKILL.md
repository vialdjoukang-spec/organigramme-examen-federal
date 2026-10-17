---
name: ssp-images-licence
description: >-
  Lis ce skill avant d’ajouter une image : les images cliniques sont réelles,
  les schémas anatomiques dérivent par automate d’une source sous licence ; tout
  est crédité et léger.
---
# But
Ce skill empêche toute image sans licence, générée ou trop lourde.
# Déclencheur
Tu l’appliques avant d’ajouter une image dans assets/.
# Étapes
1. L’image provient d’une source retenue par le plan, par exemple Wikimedia Commons, Open-i, Europe PMC ou Z-Anatomy.
2. Sa licence figure parmi les licences acceptées (domaine public, CC0, CC BY, CC BY-SA) ; tu notes l’attribution complète (titre, auteur, source, licence).
3. Tu remplis `assets/cs/credits.json` ou `assets/nc/credits.json` : fichier, titre, auteur, URL source, licence, URL de licence, modifications, date de lecture, validé.
4. Une photo clinique devient un WebP de 200 Ko au plus, sans retouche qui modifie le signe. Un schéma anatomique dérivé devient un SVG de 120 Ko au plus par vue.
5. Le champ « validé » reste faux tant qu’un humain n’a pas confirmé le contenu.
6. Pas de photo de personne identifiable sans mention de consentement.
# Exception encadrée (approuvée le 17.10.2026)
Un schéma anatomique en SVG est admis seulement s’il dérive par automate (ssp-schema-nerf) d’une source sous licence compatible, avec la mention « œuvre dérivée » et la même licence si elle est à partage identique (CC BY-SA).
# Interdits
Aucune image générée ou dessinée par IA ; aucun SVG ne remplace une photo clinique réelle d’un signe.
# Règle universelle
Le projet cible doit avoir un résultat de HAUTE QUALITÉ. L’usage des jetons doit être raisonnable et optimisé, et tout gaspillage est formellement interdit. L’économie de jetons est autorisée si et seulement si elle ne dégrade pas la qualité du travail.
