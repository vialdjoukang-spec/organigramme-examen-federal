# Prompt de reprise — 14.11.2026 (pour la prochaine IA)

Tu reprends le projet de Vial (dépôt `vialdjoukang-spec/organigramme-examen-federal`). Lis d'abord `.claude/skills/medecin-expert/SKILL.md`, `.claude/skills/expert-web/SKILL.md` et `Claude/CONSIGNES_VIAL.md`. Travaille par scripts gratuits d'abord, agents ensuite ; réponses courtes à Vial ; aucune phrase nominale ; fond de page blanc ; aucune image générée par IA.

**Fichier de référence (front-end) :** `Claude/PROGRESSION__FedMed_Claude_14.11.2026.html` sur `main` (85 Mo). C'est le fichier de Grok (imagerie et explorations superbement annotées : ne touche ni à leur contenu ni à leur design) avec les 352 cours intégrés. Il se régénère ainsi :
```
git show origin/leona/fedmed-fenetres:imagerie_GROK/fedmed/sortie/PROGRESSION__FedMed.html > base.html
python3 outils/corriger_fedmed.py base.html corrige.html
python3 outils/injecter_cours_fedmed.py corrige.html Claude/PROGRESSION__FedMed_Claude_14.11.2026.html
```
Ne jamais écrire dans `imagerie_GROK/`. Fusion par PR, CI verte, commit de fusion, section « ## Automates actifs » (checkpoint.py, checkpoint.yml, ci.yml, visuel.yml), ligne « Prompt L1 lu et appliqué ».

---

## Priorité 1 — Plateforme aux couleurs de luxe (front-end seulement)

Périmètre : la page d'affichage (front-end) de tous les fichiers HTML de progression ; **aucun cours n'est concerné** (le contenu des cours, `Claude/LOT_*/…`, reste intact) ; les fenêtres d'imagerie de Grok gardent leurs couleurs.

1. **Remplacer totalement les 20 thèmes** par des palettes de luxe (ex. noir onyx, or champagne, bordeaux, vert émeraude, bleu nuit, ivoire, bronze, platine, rose poudré, ardoise…), en gardant : même nombre de thèmes (20), même principe (au plus 3 couleurs par thème, la dernière réservée à la bande EYE SPOT des titres), **atténuation de 50 %** vers le blanc, fond de page blanc, texte #111/#000, **contraste ≥ 7:1 vérifié par script** (les assertions de `outils/receptacle.py` doivent rester vraies).
   - Sources du code : `Claude/_progression/themes.json` (palettes), `outils/receptacle.py` (fonctions `attenue`, `eye*`, CSS des zones), et le CSS équivalent présent dans le fichier FedMed (grep `--eye`, `data-theme`).
2. **Bouton Thème utilisable partout** (onglets Cours, Examens, Pharmacologie, Sciences fondamentales, pages embarquées Sémiologie / Physiologie / Physiopathologie / Recensement) **sauf dans les fenêtres d'imagerie** ; le thème choisi se propage aux iframes embarquées (postMessage ou variables CSS), jamais au contenu des cours.
3. **Rails d'icônes moins lourds** : réduire la taille des titres associés aux icônes (≈ −20 %) et la taille des icônes (≈ −25 %), resserrer les plages (marges) ; vérifier qu'aucun texte ne devient illisible (taille minimale 13 px, contraste ≥ 7:1).
4. **Police Atkinson Hyperlegible réellement intégrée** : aujourd'hui, les cours injectés chargent la police par Google Fonts (dépendance Internet). Corriger dans `outils/injecter_cours_fedmed.py` : intégrer une seule fois les 4 fichiers `Claude/_polices/atkinson-hyperlegible-latin-*.woff2` en base64 dans le fichier, puis les injecter dans chaque cours au moment de l'ouverture (même mécanisme que les images `@@IMG:…@@`). Vérifier par Playwright que `document.fonts.check('16px "Atkinson Hyperlegible"')` est vrai **hors ligne**, dans la page et dans un cours.
5. Preuve : captures avant/après de 3 thèmes, bureau 1400 px et téléphone 390 px, zéro erreur console, puis PR.

## Priorité 2 — Contenu encore incomplet

1. **Anatomie** (Sciences fondamentales, sous-onglet 1) : 71 fiches minimum / 117 cible (`Claude/_progression/recensement_sf/recensement_sf.json > anatomie`, schéma dans `schemas`). Images réelles seulement (Commons, Gray's Anatomy domaine public). Rédaction → audit indépendant → corrections → audit-ok.
2. **Images manquantes** : 30 diagnostics d'imagerie sans cliché, 150 sans normal, 71 explorations sans tracé (`Claude/_progression/recensement/BESOINS_IMAGES.html`) ; gestes de Status à photographier (liste dans chaque fiche `donnees/semiologie/status/S-xx.json`, champ `a_fournir`). Vial fournit une partie ; le script `outils_images/chercher.py` complète.
3. **Schémas à dessiner** (seule exception autorisée aux images réelles : courbes théoriques) : spirométrie, boucles débit-volume, cinétiques des tests dynamiques (explorations VENT et DYN).
4. **Compléments listés dans les audits** (« compléments à venir ») : recommandations suisses à lire en texte intégral (SSI, Swiss Stroke Society, SRC…), molécules absentes du corpus AIPS (colchicine, oxytocine injectable, éthosuximide…), fiches PP « pancréatite chronique » et « MTEV de la grossesse ».

## Priorité 3 — Exercices et épreuves (squelette d'abord)

1. Bande « QCMs : A, K′ _ Menu long » sous chaque zone exerçable ; bouton Réponse → argumentation, « pourquoi pas X », liens vers les cours.
2. Épreuves blanches de 120 questions chronométrées, proportions de l'examen fédéral (format officiel 2026 : `Claude/_progression/recherche/reports/Sources suisses sémiologie CS.md`).

## Priorité 4 — Décisions de Vial en attente

- Purge de l'historique git pour IMG-242 (nom de patient d'un article CC BY, déjà masqué dans le fichier actuel).
- Images intimes masquées (S-11, S-14, S-16, lividités) : garder ou remplacer.
- Reprise des LOT_033–034 (en pause, Phase A audit-ok).

## Repères

- Bilan de nuit : `Claude/_progression/bilans/BILAN_NUIT_14_11.html`. Tous les contenus listés y sont audit-ok (imagerie 344, explorations 153, Sémiologie 219, Physiologie 88, Physiopathologie 108).
- Pages sources : `Claude/_progression/recensement/generer.py`, `donnees/semiologie/generer_status.py`, `donnees/fondamentales_v2/generer_sf.py` ; assemblage du `progression.html` interne : `outils/assembler_progression.py`.
- Compteur gratuit de tokens : `Claude/_harnais/suivi.py`.
