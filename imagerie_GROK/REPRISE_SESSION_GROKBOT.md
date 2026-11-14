# Reprise de session — imagerie_GROK

**Dernière mise à jour :** samedi 14 novembre 2026, 12:33 (Europe/Zurich). Utilisation de la session précédente : 72,6 %. Ce fichier est sur `main`, dans le dossier de travail `imagerie_GROK/`. Il sert à relancer une nouvelle session Grok Bot si la précédente s’arrête sans prévenir.

---

## Prompt de continuation (à coller dans une nouvelle session Grok Bot)

```
Tu es Grok Bot. Reprends le mandat imagerie_GROK de Vial (vialdjoukang-spec), dépôt https://github.com/vialdjoukang-spec/organigramme-examen-federal, dossier imagerie_GROK/ uniquement, branche main. Lis d’abord ce fichier : imagerie_GROK/REPRISE_SESSION_GROKBOT.md (le présent prompt en est le résumé). Réponses courtes à Vial.

Objectif. Harnais et paires normale (GAUCHE) / pathologique (DROITE) pour IMAGERIE_CLICHES.html (IMG-344 → IMG-001), puis EXPLORATIONS_FONCTIONNELLES.html (EXP-153 → EXP-001), puis les fiches FTE. Qualité > exhaustivité. Tu n’inventes rien : « À vérifier » si ce n’est pas sourcé. Aucun « complet » de complaisance : c’est validate.py qui décide, après relecture à l’œil des captures.

Interface déjà exigée, à terminer et à montrer :
- contraste fort : traits et courbes 2–3 px avec halo sombre 1–2 px ; texte blanc sur fond sombre opaque, facilement lisible ;
- survol lié des structures des DEUX côtés : la structure homologue s’allume en face, même code couleur à gauche et à droite ; la bulle donne le nom et la description radiologique normale ;
- lésions : une couleur pointillée distincte par lésion, différente des couleurs d’anatomie ; flèches numérotées cachées par un bouton ; le clic ouvre une bande annotée qui suit la silhouette ;
- zoom +, zoom − et réinitialisation sur chaque côté, plus un zoom lié ;
- bouton « Anatomie » : contours de l’externe vers l’interne ;
- bouton « Rappel du code couleur structure – aspect » : pour chaque structure, sa couleur et son aspect selon la technique affichée (radio, scanner, IRM, échographie), sourcé ou « à vérifier » ;
- côté pathologique : diagnostic cherché, puis indices guidés, puis révélation, puis les autres lésions ;
- texte minimal visible : âge, sexe, et « Source » soulignée (détail au survol) ; la normale est légèrement agrandie pour paraître de même taille.

Contraintes dures, sans exception :
- n’écrire que dans imagerie_GROK/ sur main ;
- intégration par PR, checks verts, merge normal ; pas de force push, pas de bypass admin ;
- pas de labels audit-ok, attente-vial ou infra ; pas d’issue, pas de commentaire ;
- ne jamais lire psychotherapie-personnelle-de-Vial/ ;
- licences libres seulement (CC0, domaine public, CC BY, CC BY-SA), avec auteur et URL ;
- données patient détruites sauf âge et sexe (anonymisation vérifiée) ;
- le même sexe n’est exigé que si le sexe change l’anatomie (bassin, sein, organes génitaux) ; ailleurs, « adulte » suffit, avec preuve de maturité dans adulte_preuve si besoin ; tranche d’âge comparable ;
- chaque corps de PR doit contenir une section « ## Automates actifs » dont les puces ne listent que `tools/garde/checkpoint.py` et les workflows `checkpoint.yml`, `ci.yml` et `visuel.yml` (sinon le checkpoint R15 échoue).

État au 14 novembre 2026, 12:30 (Europe/Zurich) :
- main : 0 complet, environ 350 partiels, 205 introuvables (liste : à récupérer /workspace/bilan_imagerie/INTROUVABLES_imagerie_GROK.md, déjà remise à Vial) ;
- PR #726 (branche cursor/interface-didactique-ffbc) NON fusionnée dans main : lots d’appariement et contours homologues commencés, aucun élément complet ;
- scripts du harnais : imagerie_GROK/harnais/scripts/ (validate.py, build_app.py, screenshot.py, segment.py, fetch_commons.py, fetch_openi.py, normalize.py). Sur la box, screenshot.py se lance avec Chrome : executable_path="/usr/bin/google-chrome", args=["--no-sandbox"].

Agents en cours au 12:30 (Europe/Zurich) — ne pas les laisser seuls, relancer ou récupérer leur travail :
- agent d’interface principal (vitrine IMG-134 + lots) : https://cursor.com/agents/bc-54c6c840-a735-550f-950b-d0d43f25ffbc — branche PR cursor/interface-didactique-ffbc, vitrine attendue aussi sur cursor/vitrine-IMG-134 ;
- IMG-136 : https://cursor.com/agents/bc-babf0942-ba0c-5336-a623-2840ac04ed6d ;
- IMG-250 : https://cursor.com/agents/bc-2a60c85b-90cb-5379-b24a-d1c18ab1c597 ;
- IMG-267 : https://cursor.com/agents/bc-4206405b-ad12-5a66-afd3-12b3d4f0994b ;
- IMG-132 : https://cursor.com/agents/bc-862c5fa9-f349-5048-b9ca-eac5c44fee4d ;
- IMG-158 : https://cursor.com/agents/bc-563d0fae-85c6-50a7-bda2-3f376c933485 ;
- IMG-164 : https://cursor.com/agents/bc-20b32c0f-b311-5dba-b805-5449cce38c0c ;
- IMG-161 : https://cursor.com/agents/bc-2d77c58a-c894-5e11-8866-34554d74d02b ;
- IMG-243 : https://cursor.com/agents/bc-c67b4218-588c-5d0f-bddf-fd4283e8d8a6 ;
- IMG-001 : chantier local sur la box Leona ; copier le résultat dans le dépôt (ne pas le laisser seulement sur la machine).
Chaque agent vitrine travaille sur cursor/vitrine-IMG-XXX et dépose au moins 20 captures relues à l’œil dans imagerie_GROK/harnais/progression/captures-interface/vitrine/IMG-XXX/ (plus index.md). Ne modifier que le manifeste, les contours et les captures de SA paire. Les changements de code génériques vont dans imagerie_GROK/harnais/progression/vitrine/IMG-XXX_PATCH_NOTES.md, sans toucher le cœur sans nécessité, et sans PR/merge/issue/commentaire de la part de ces agents vitrine.

Prochaines étapes, dans cet ordre :
1) Collecter les 20 captures (ou plus) de chaque paire vitrine et les envoyer à Vial.
2) Intégrer les branches cursor/vitrine-IMG-XXX dans la PR #726.
3) Faire fusionner la PR #726 dès que les checks sont verts (merge normal, pas de bypass).
4) Refaire les contours par segmentation pour le reste des paires.
5) Traiter les FTE, puis les EXP.
6) Intégrer les images que Vial trouvera pour les « introuvables ».

Tiens ce fichier imagerie_GROK/REPRISE_SESSION_GROKBOT.md à jour sur main (PR + merge normal) à chaque avancée notable, et dès que l’utilisation de la session approche 90 %, pour qu’il reste disponible même si tout s’arrête. Mets à jour la ligne « Dernière mise à jour » (heure Europe/Zurich + pourcentage d’utilisation).
```

---

## 1. Objectif et règles de Vial

Dépôt : [vialdjoukang-spec/organigramme-examen-federal](https://github.com/vialdjoukang-spec/organigramme-examen-federal). Dossier de travail : `imagerie_GROK/`. Qualité > exhaustivité > économie. Concision, phrases verbales. Ne rien inventer.

À lire dans l’ordre, dans `imagerie_GROK/` : `PROMPT_IMAGERIE.md`, `STRATEGIE.md`, `harnais/HARNESS.md` (section REPRISE), `harnais/memory/BRIEF_CHERCHEUR.md`, `harnais/manifest/SCHEMA.json`. Traiter `IMAGERIE_CLICHES.html` (344 DX, ordre IMG-344 → IMG-001), puis `EXPLORATIONS_FONCTIONNELLES.html` (153 explorations, EXP-153 → EXP-001), puis les 58 fiches FTE. Considérer que rien n’est « complet » tant que `validate.py` ne l’a pas accepté et qu’une capture n’a pas été relue à l’œil.

### Harnais

Pour chaque lésion : contour (liste de points normalisés 0–1, polygone fermé, ≥ 3 points, silhouette réelle, jamais un rectangle ni un hexagone grossier) + définition radiologique du signe, sourcée. `build_app.py` : flèche fine d’épaisseur normale, couleur vive sur liseré sombre ; à la pointe, contour pointillé vif épousant la lésion. Clic sur le numéro d’une lésion (principale, associée, secondaire, complication locale) → nom du signe + définition. `validate.py` contrôle contours, définition, preuve, confiance, et bloque les faux « complet ». Tester avec `screenshot.py` et relire les captures avant d’enchaîner.

Pour chaque élément : 1 image normale + 1 pathologique, même modalité / séquence / plan. Licences CC0, domaine public, CC BY ou CC BY-SA seulement ; auteur + URL notés. Ouvrir chaque image, vérifier à l’œil, signaler tout écart d’appariement.

### Interface (10:08, addendum 11:01, consignes 11:17 et 11:20)

- Normale à GAUCHE, pathologique à DROITE. Agrandir légèrement la normale à l’affichage pour qu’elle paraisse de même taille (sans déformer le rapport hauteur/largeur).
- Tranche d’âge comparable. Le même sexe n’est exigé que lorsque le sexe change l’anatomie (bassin, sein, organes génitaux) ; ailleurs, « adulte » suffit, établi par un signe de maturité visible consigné dans `adulte_preuve`. Origine de l’image indifférente (licence libre obligatoire), à condition que toute donnée privée soit détruite : masquer nom, identifiant, date, établissement incrustés ; ne garder que l’âge et le sexe. `validate.py` contrôle le champ d’anonymisation vérifiée.
- Contraste des lignes, courbes et textes : trait 2–3 px avec halo sombre de 1–2 px ; étiquettes en blanc sur fond sombre opaque ; facilement visibles.
- Survol des structures des DEUX côtés, en survol lié : la structure homologue s’allume en face. Même code couleur pour la même structure à gauche et à droite. La bulle donne le nom et la description radiologique normale (aspect / densité / signal / échogénicité selon la technique).
- Lésions : palette distincte de l’anatomie ; chaque lésion a une couleur pointillée différente des autres. Flèches numérotées cachées par un bouton ; le clic ouvre une bande annotée qui suit la silhouette, avec le nom du signe, la définition sourcée et la preuve.
- Zoom +, zoom − et réinitialisation sur chaque côté, plus un zoom lié.
- Bouton « Anatomie » (côté normal) : tracé progressif des structures, des plus externes vers les plus internes.
- Bouton « Rappel du code couleur structure – aspect » : pour chaque structure, sa couleur et son aspect dans la technique affichée (opaque ou clair en radio, densité au scanner, signal T1/T2 en IRM, échogénicité en échographie), sourcé ou « à vérifier ». Les lésions y figurent aussi. Valable quelle que soit la technique en cours d’affichage.
- Côté pathologique : d’abord le diagnostic cherché, puis des indices guidés (région, signe, révélation), puis les autres lésions / diagnostics présents sur l’image, sourcés par la légende ou « À vérifier ». Mode défi ludique (score / retour).
- Texte minimal visible : âge, sexe, et le mot « Source » souligné (auteur, licence, URL, légende au survol). Tout le reste passe en survol ou en panneau repliable.

Un « complet » exige notamment : paire acceptable au regard des règles de sexe et d’âge, anonymisation vérifiée, anatomie par couches fonctionnelle et relue à l’œil, bande annotée et accompagnement des lésions (principale + autres) fonctionnels, définition sourcée. `validate.py` refuse un complet s’il manque la normale, si le sexe n’est pas établi là où il le faut, si le contour est un rectangle de 5 points ou moins, si la définition reste « À vérifier », ou s’il manque `adulte_preuve` / l’anonymisation.

Les mandats sources (box Leona, si elle est encore là) : `/workspace/outils-puissants/Leona__Imagerie_Nuit_20261114/MANDAT.md`, `MANDAT_INTERFACE.md`, `MANDAT_INTERFACE_ADDENDUM_1101.md`, `MANDAT_VITRINE_PARALLELE.md`.

---

## 2. Contraintes dures

- N’écrire que dans `imagerie_GROK/` sur `main`. Ne pas écrire dans `LOT_Claude_Finaux/` ni dans `harnais/` à la racine du dépôt.
- Intégration par PR, checks verts, merge normal. Pas de force push, pas de bypass admin.
- Pas de labels `audit-ok`, `attente-vial` ou `infra`. Pas d’issue, pas de commentaire.
- Ne jamais lire `psychotherapie-personnelle-de-Vial/`.
- Licences libres seulement (CC0, domaine public, CC BY, CC BY-SA), avec auteur et URL. Images non libres interdites. Pas d’achat.
- Données patient détruites sauf âge et sexe.
- Aucun « complet » de complaisance : `validate.py` décide, après relecture à l’œil.
- Réponses courtes à Vial.
- Corps de chaque PR : section `## Automates actifs` dont les puces listent uniquement `tools/garde/checkpoint.py` et les workflows `checkpoint.yml`, `ci.yml` et `visuel.yml` (le checkpoint R15 échoue sinon). Format qui passe :

```
## Automates actifs
- `tools/garde/checkpoint.py`
- `.github/workflows/checkpoint.yml`
- `.github/workflows/ci.yml`
- `.github/workflows/visuel.yml`
```

---

## 3. État actuel (14 novembre 2026, 12:30, Europe/Zurich)

- **main :** 0 élément complet, environ 350 partiels, 205 introuvables. Liste des introuvables déjà remise à Vial : `/workspace/bilan_imagerie/INTROUVABLES_imagerie_GROK.md` (sur la box). Vial cherche lui-même ces clichés ; les intégrer quand il les apportera.
- **PR [#726](https://github.com/vialdjoukang-spec/organigramme-examen-federal/pull/726)** (branche `cursor/interface-didactique-ffbc`) : ouverte, **non fusionnée**. Travaux déjà dans cette branche, tous encore partiels :
  - lots d’appariement : IMG-001 à IMG-129, IMG-132 à IMG-166, IMG-245 à IMG-344 ;
  - contours anatomiques homologues gauche/droite sur 13 paires du lot 1 ; IMG-061 et IMG-064 sans contours d’anatomie (le tracé ne suivait ni l’os ni l’air) ;
  - données privées masquées sur IMG-255, IMG-273, IMG-327 et IMG-337 ;
  - IMG-267 : âges 26 et 25 ans notés ; le contour de la tête luxée déborde encore ;
  - lésions redessinées seulement pour IMG-132, IMG-158 et IMG-164 ;
  - la vitrine (contraste, survol lié, couleurs, zoom, bouton du code couleur) et les 20 captures d’une même paire n’étaient pas encore livrées à Vial au moment de cette reprise ; les agents vitrine tournent pour ça.
- **Scripts du harnais :** `imagerie_GROK/harnais/scripts/` — `validate.py`, `build_app.py`, `screenshot.py`, `segment.py`, `fetch_commons.py`, `fetch_openi.py`, `normalize.py`. Application générée : `app/Radio_Paires.html`. Sur la box, lancer `screenshot.py` avec `executable_path="/usr/bin/google-chrome"` et `args=["--no-sandbox"]`. Les fetches passent par les API (pas de navigateur) et le cache. Les contours de silhouette se font avec `segment.py` ou scikit-image à partir d’un point par structure (MedSAM ou SAM si possible sur CPU), avec recalage de la normale vers la pathologique ; chaque contour est relu à l’œil.

---

## 4. Agents en cours au 14 novembre 2026, 12:30 (Europe/Zurich)

| Paire / rôle | Agent | Branche prévue | Captures |
|---|---|---|---|
| Interface principale : vitrine IMG-134 + lots | [bc-54c6c840-a735-550f-950b-d0d43f25ffbc](https://cursor.com/agents/bc-54c6c840-a735-550f-950b-d0d43f25ffbc) | `cursor/interface-didactique-ffbc` (PR #726) et `cursor/vitrine-IMG-134` | `imagerie_GROK/harnais/progression/captures-interface/vitrine/IMG-134/` |
| IMG-136 | [bc-babf0942-ba0c-5336-a623-2840ac04ed6d](https://cursor.com/agents/bc-babf0942-ba0c-5336-a623-2840ac04ed6d) | `cursor/vitrine-IMG-136` | `…/vitrine/IMG-136/` |
| IMG-250 | [bc-2a60c85b-90cb-5379-b24a-d1c18ab1c597](https://cursor.com/agents/bc-2a60c85b-90cb-5379-b24a-d1c18ab1c597) | `cursor/vitrine-IMG-250` | `…/vitrine/IMG-250/` |
| IMG-267 | [bc-4206405b-ad12-5a66-afd3-12b3d4f0994b](https://cursor.com/agents/bc-4206405b-ad12-5a66-afd3-12b3d4f0994b) | `cursor/vitrine-IMG-267` | `…/vitrine/IMG-267/` |
| IMG-132 | [bc-862c5fa9-f349-5048-b9ca-eac5c44fee4d](https://cursor.com/agents/bc-862c5fa9-f349-5048-b9ca-eac5c44fee4d) | `cursor/vitrine-IMG-132` | `…/vitrine/IMG-132/` |
| IMG-158 | [bc-563d0fae-85c6-50a7-bda2-3f376c933485](https://cursor.com/agents/bc-563d0fae-85c6-50a7-bda2-3f376c933485) | `cursor/vitrine-IMG-158` | `…/vitrine/IMG-158/` |
| IMG-164 | [bc-20b32c0f-b311-5dba-b805-5449cce38c0c](https://cursor.com/agents/bc-20b32c0f-b311-5dba-b805-5449cce38c0c) | `cursor/vitrine-IMG-164` | `…/vitrine/IMG-164/` |
| IMG-161 | [bc-2d77c58a-c894-5e11-8866-34554d74d02b](https://cursor.com/agents/bc-2d77c58a-c894-5e11-8866-34554d74d02b) | `cursor/vitrine-IMG-161` | `…/vitrine/IMG-161/` |
| IMG-243 | [bc-c67b4218-588c-5d0f-bddf-fd4283e8d8a6](https://cursor.com/agents/bc-c67b4218-588c-5d0f-bddf-fd4283e8d8a6) | `cursor/vitrine-IMG-243` | `…/vitrine/IMG-243/` |
| IMG-001 | chantier **local** sur la box Leona (pas un agent cursor.com) | à copier ensuite vers `cursor/vitrine-IMG-001` | `…/vitrine/IMG-001/` |

Captures attendues par paire vitrine : au moins 20 captures réelles relues à l’œil (bureau 1440×900, plus 2 en mobile), avec `index.md`. Elles doivent montrer : vue initiale, étapes d’anatomie, survol lié gauche→droite puis droite→gauche, légende du code couleur, défi et indices, révélation, bande, autres lésions, zoom, zoom lié, survol de la Source, mobile.

Les agents vitrine ne font pas de PR, ni merge, ni issue, ni commentaire. L’agent de reprise ou l’agent d’interface principal intègre leur travail dans la PR #726.

---

## 5. Prochaines étapes (dans l’ordre)

1. Collecter les 20 captures (ou plus) de chaque paire vitrine et les envoyer à Vial.
2. Intégrer les branches `cursor/vitrine-IMG-XXX` dans la PR #726.
3. Faire fusionner la PR #726 dès que les checks sont verts (merge normal, pas de bypass). Si un check échoue : lire la raison, corriger, recommencer.
4. Refaire les contours par segmentation pour le reste des paires.
5. Traiter les FTE, puis les EXP.
6. Intégrer les images que Vial trouvera pour les « introuvables ».

Tenir ce fichier à jour sur `main` à chaque avancée notable, et automatiquement quand l’utilisation de la session approche 90 %.

**Dernière mise à jour :** samedi 14 novembre 2026, 12:33 (Europe/Zurich). Utilisation de la session précédente : 72,6 %.
