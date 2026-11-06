# Rapport — chantiers 2 à 6 du 6 novembre 2026

## Fait

- **2 — Existant documenté.** `RECAP_TECHNOS_EXISTANTES.md` distingue prompteur, rédacteurs A/B pairs-impairs, mode Harnais seul sans Routage, V7/V8, Medina CHAPTER_SPEC, garde, veille, certitude, pre-commit, audits, Bracelet, Skills et dessinateur. Les éléments non retrouvés sont explicitement signalés.
- **3 — Obsidian et quantification.** Les 22 diagrammes Atelier ont des cartes-notes rectangulaires, courbes avec flèches, vignettes Graph (cercles + traits) au bon endroit et une légende : coût évité estimé, coût API des scripts, performance/5, qualité/5, complexité/5 et justification. Aucun chiffre n’est présenté comme mesuré.
- **4 — Harnais enrichi en architecture.** `HARNAIS_BRACELET_V4.md` décrit le circuit Bracelet 1–3 outils, caches, scripts, modèles locaux, escalade contrôlée et preuves. Onze fiches « chef-d’œuvre » ont leur SVG associé. Outils repérés : Ollama, llama.cpp, OpenCode, Promptfoo ; sources GitHub et pistes X déclarées comme telles.
- **5 — Cerveau secondaire + quasi-zéro coût.** Le circuit global affiche lecture d’index, Bracelet, tests/caches zéro token, essai local, escalade et audit intégré. La cible de 99 % concerne les appels payants évités sur des flux adaptés, jamais une promesse de coût total ou de qualité.
- **6 — Bac à sable.** Onglet 🧪 avec six options, coût, limites et qualité attendue. Mini-vault réel : six notes Markdown liées et `Circuit_Zero_Cout.canvas` (six cartes-fichiers, six flèches, JSON Canvas 1.0).
- **Livraisons.** HTML régénéré, captures vérifiées, audit étendu, deux ZIP et dossier pour nouvelle PR préparés. Aucun push, aucune PR, aucun merge.

## Vérifications

`AUDIT_V3.md` : **58 contrôles OK / 0 KO**, dont fonctionnement mobile, absence de débordement et erreurs JavaScript, 22 légendes, 12 schémas d’architecture, vault et documents. Les images clés ont été ouvertes : Obsidian Desktop/Mobile, bac à sable Desktop/Mobile, harnais et réseau interactif. Une anomalie CSS masquant la légende a été détectée et corrigée avant livraison.

Captures principales :
- `captures/10_Obsidian_SVG_Desktop.png`
- `captures/11_Obsidian_SVG_Mobile.png`
- `captures/13_Bac_a_sable_Desktop.png`
- `captures/15_Harnais_Desktop.png`
- `captures/16_Bac_a_sable_Mobile.png`
- `captures/03_Reseaux_Interactifs.png`

## Reste / limites

- Les architectures nouvelles ne modifient pas le harnais de production existant ; elles doivent être évaluées sur dix tâches réelles avant adoption.
- Aucun benchmark réel n’établit 99–100 % d’économie totale : il faut mesurer appels, coût complet, temps et qualité avant/après.
- Les nouveaux outils locaux ne sont pas installés ni validés dans les productions ; la revue humaine du contenu sensible reste nécessaire.
- Le dossier `Outils et techno d'optimisation/` est prêt pour une **nouvelle PR**, mais aucune PR n’a été créée. La PR #508 n’a pas été touchée.
- `audit-lot-v7` n’a pas été retrouvé comme fichier dans les sources consultées ; les fichiers V7 existent. Cela est noté dans le récapitulatif.

## Références

`REFERENCES_OBSIDIAN.md` contient les liens Obsidian Canvas/Graph, JSON Canvas, GitHub et X consultés, ainsi que la méthode des estimations.
