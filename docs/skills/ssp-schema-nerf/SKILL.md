---
name: ssp-schema-nerf
description: >-
  Lis ce skill avant de produire ou de modifier un schéma de nerf crânien : le
  trait dérive d’une source anatomique sous licence, par automate, puis reçoit
  des couches d’annotation sourcées.
---
# But
Ce skill garantit des schémas simples au crayon, anatomiquement exacts et traçables jusqu’à leur source.
# Déclencheur
Tu l’appliques à toute création ou modification dans `assets/nc/`.
# Étapes
1. Tu choisis la source dans `nc/sources.yml` : modèle 3D Z-Anatomy (CC BY-SA 4.0, d’après BodyParts3D CC BY-SA 2.1 JP) pour les vues face, profil et trois quarts ; planche de Gray (1918, domaine public) pour le plan du nerf ; licence vérifiée par l’API Commons ou le fichier License.txt, avec la date.
2. Tu produis le trait par automate seulement : `tools/dedale/freestyle.py` (Blender sans écran, rendu de contours Freestyle en SVG) ou `tools/dedale/trace.py` (crayon par densité, masque de couleur du nerf, vectorisation potrace). Tu ne dessines rien à la main et tu ne génères aucune anatomie par IA.
3. Tu écris les annotations dans `nc/annot/ncXX.yml` (trajet, noyaux, foramens, territoires, sites lésionnels numérotés), chacune avec sa source ; `tools/dedale/annoter.py` compose le SVG à couches nommées : `trait`, `nerf`, `noyaux`, `foramens`, `territoires`, `lesions`, `legendes`.
4. Le nerf est le seul élément en couleur (vert foncé `#156534`) ; le trait de fond reste gris crayon ; le rouge est réservé au site lésionnel d’urgence vitale.
5. Tu passes `svgo`, puis `python3 tools/dedale/verifier.py ncXX` : couches présentes, texte lisible à 360 px, poids au plus 120 Ko par vue, crédit complet dans `assets/nc/credits.json`.
6. Le champ `valide_par_vial` reste faux tant que Vial n’a pas validé le schéma.
7. Rotation à 8 vues seulement pour V, VII et III-IV-VI (décision du 17.10.2026).
# Interdits
Aucune image générée par IA, aucun calque d’une source sans licence compatible (Netter, Kenhub, Pinterest, manuels sous droits), aucune source marquée NoAI utilisée comme donnée d’entraînement.
# Règle universelle
Le projet cible doit avoir un résultat de HAUTE QUALITÉ. L’usage des jetons doit être raisonnable et optimisé, et tout gaspillage est formellement interdit. L’économie de jetons est autorisée si et seulement si elle ne dégrade pas la qualité du travail.
