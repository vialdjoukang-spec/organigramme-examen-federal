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
1. Tu choisis la source dans `nc/sources.yml` : modèle 3D Z-Anatomy (CC BY-SA 4.0, d’après BodyParts3D CC BY-SA 2.1 JP) pour les trois vues publiées, face, profil et trois quarts ; la planche de Gray (1918, domaine public) reste une donnée source, jamais une vue publiée ; licence vérifiée par l’API Commons ou le fichier License.txt, avec la date.
2. Tu produis le trait par automate seulement : `tools/dedale/crane.py` (crâne 3D au crayon, os seuls décimés, traits forts hiérarchisés), `tools/dedale/masques.py` (aplats) et les courbes du nerf ; jamais le modèle complet dans Blender (moins de 5 Go). Tu ne dessines rien à la main et tu ne génères aucune anatomie par IA.
3. Tu écris les annotations dans `nc/annot/ncXX.yml` (trajet, noyaux, foramens, territoires, sites lésionnels numérotés), chacune avec sa source, et les états dans `nc/presets/ncXX.yml` (8 repères au plus par état) ; `tools/dedale/annoter.py` compose le SVG à couches nommées : `trait`, `nerf`, `noyaux`, `foramens`, `territoires`, `lesions`, `legendes`, `legende`. Sur le dessin, aucun texte sauf le titre : chaque structure reçoit un petit numéro cerclé fléché, `<g class="nc-num" data-num data-nom data-glo>` cliquable ; les noms vont dans la légende numérotée en 2 colonnes sous le dessin ; même numéro pour la même structure dans les 3 vues.
4. Le nerf est en jaune intense `#FFC400`, cerné d’un trait sombre `#5a4500` d’environ 1 px, sur tout son trajet (noyau ou émergence jusqu’aux branches terminales), au-dessus de tout ; l’ancien vert `#156534` est refusé ; le crâne reste en traits gris et noirs, les aplats sont pâles ; le rouge est réservé au site lésionnel d’urgence vitale.
5. Tu passes `svgo`, puis `python3 tools/dedale/verifier.py ncXX` : couches présentes, aucun texte sur le dessin, repères disjoints et jamais sur le nerf, `data-nom` présent, lisibilité à 360 px, poids au plus 120 Ko par vue, crédit complet dans `assets/nc/credits.json`.
6. Le champ `valide_par_vial` reste faux tant que Vial n’a pas validé le schéma.
7. Exactement 3 vues publiées par paire : face, profil, trois quarts ; aucune rotation à 8 vues (décision du 17.10.2026, qui remplace la précédente).
8. Un schéma clé original peut s’ajouter quand la clinique l’exige (VII : `nc07-voie-motrice.svg`, tools/dedale/voie.py) : même style, même contrat de repères, références anatomiques lues et datées dans le crédit « Schéma original », points incertains marqués « À vérifier ».
# Interdits
Aucune image générée par IA, aucun calque d’une source sans licence compatible (Netter, Kenhub, Pinterest, manuels sous droits), aucune source marquée NoAI utilisée comme donnée d’entraînement.
# Règle universelle
Le projet cible doit avoir un résultat de HAUTE QUALITÉ. L’usage des jetons doit être raisonnable et optimisé, et tout gaspillage est formellement interdit. L’économie de jetons est autorisée si et seulement si elle ne dégrade pas la qualité du travail.
