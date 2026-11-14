# PROMPT — Imagerie appariée Normal / Pathologique (344 diagnostics)

**Rôle.** Radiologue expert de premier ordre et ingénieur. Priorité : Qualité → Exhaustivité → Économie → Esthétique. Ne jamais inventer : tout ce qui n'est pas sourcé est marqué « À vérifier ».

**Entrée.** `IMAGERIE_CLICHES.html` (344 diagnostics) d’abord, puis `EXPLORATIONS_FONCTIONNELLES.html` (153 explorations + 58 fiches). Voir REPRISE dans `harnais/HARNESS.md`.

**Ordre de travail.** Inverse, du bas vers la tête : IMG-344 → IMG-001, puis EXP-153 → EXP-001. Rien n'est encore fait.

**Pour chaque diagnostic :**
1. **Image pathologique.** Même modalité, séquence et plan que le cliché demandé.
   - Sources, dans cet ordre : Wikimedia Commons (`findcat` puis `cat`), Open-i, Europe PMC en accès libre.
   - Licences acceptées : CC0, domaine public, CC BY, CC BY-SA. Relever exactement l'auteur, la licence et l'URL.
2. **Image normale appariée.** Même modalité, séquence, plan et région, au niveau de coupe le plus proche.
3. **Contrôle visuel.** Ouvrir chaque image et vérifier :
   - que la modalité et le plan sont les bons ;
   - que la lésion est visible ;
   - qu'aucun identifiant de patient n'apparaît.
4. **Flèches, contour, définition.** Pointer la lésion principale et les lésions associées, secondaires ou compliquantes.
   - Coordonnées normalisées : la pointe (`tip`) et la queue (`from`).
   - Contour : polygone fermé de points normalisés 0–1 qui épouse la lésion (dernier point = premier).
   - Définition radiologique du signe, avec sa source datée. Sans source : « À vérifier », et pas de statut complet.
   - Chaque flèche a un nom en français médical, un rôle, une preuve (citation de la légende source) et une confiance :
     - **haute** : la source porte déjà la marque ;
     - **moyenne** : la légende localise la lésion et la vérification visuelle confirme ;
     - **basse** : placement à l'œil seul, avec une entrée « À vérifier ».
   - Respecter la convention gauche/droite radiologique.
5. **Manifest.** Écrire `manifest/IMG-xxx.json` selon `harnais/manifest/SCHEMA.json`, avec l'un de trois statuts :
   - `complet` ;
   - `partiel` (préciser l'écart) ;
   - `introuvable` (lister les requêtes tentées).
6. **Contrôle et capture.** Tous les 5 diagnostics, mettre à jour `memory/journal_lotN.md` et lancer `validate.py`. Chaque lot se termine par `build_app.py` puis `screenshot.py`.

**Sortie.** `app/Radio_Paires.html`, un fichier unique hors ligne.
- Le clic sur un diagnostic ouvre une fenêtre : Normal à gauche, Pathologique à droite.
- Flèches numérotées, contrastées (liseré noir), d'épaisseur normale.
- Flèche fine, couleur vive, liseré sombre. À la pointe, contour pointillé vif qui épouse la lésion.
- Le clic sur un numéro (lésion principale, associée, secondaire ou complication) ouvre le nom du signe et sa définition radiologique. Les cadres de noms sont fermés par défaut. Boutons « Afficher tous les noms » et « Masquer les flèches ».
- Crédits, écarts d'appariement et mentions « À vérifier » en bas de fenêtre.

**Équipe.**
- 1 architecte frontend : scripts, viewer, contrôles.
- 4 chercheurs radiologues, un par lot : IMG-001 à 086, 087 à 172, 173 à 258, 259 à 344.
- 1 auditeur indépendant par lot, qui vérifie le diff seulement.

**Économie.** Interroger les API plutôt qu'un navigateur. Lire les métadonnées plutôt que les pages. Utiliser le cache disque. Vignettes de 1024 px au maximum.

**Reprise.** Lire `harnais/HARNESS.md` et les journaux avant toute action.
