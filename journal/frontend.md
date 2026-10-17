# Journal · Frontend Premium · Iris (automate) et Apollon

Chaque entrée porte une date (Europe/Zurich), une décision et les sources lues. Aucune donnée personnelle n’entre dans ce journal public.

## Fiche de mission · Iris · automate de qualité visuelle
Couleur : arc-en-ciel (gris neutre dans les rapports)

> **Règle universelle.** Le projet cible doit avoir un résultat de HAUTE QUALITÉ. L’usage des jetons doit être raisonnable et optimisé, et tout gaspillage est formellement interdit. L’économie de jetons est autorisée si et seulement si elle ne dégrade pas la qualité du travail.

| Champ | Contenu |
|---|---|
| Mission | Iris refuse toute régression du rendu avant fusion : captures, accessibilité, débordement, polices et stabilité de mise en page. |
| Fichiers | `.github/workflows/visuel.yml`, `tests/visuel/capture.py`, `tests/visuel/compare.py`, `qa/visuel/config.json`, `qa/visuel/reference/` et `reference.json` (référence engagée), `tools/visuel_reference.sh`. |
| Entrées | `app_v2.html` de la demande de fusion ; Playwright 1.63.0 et axe-core 4.14.0, figés par version et empreinte SHA-256. |
| Déclenchement | Chaque demande de fusion vers main, chaque lundi à 04:41 UTC (06:41 Europe/Zurich), et à la demande. Coût : 0 CHF (dépôt public). |
| Étapes | 1. Captures de 10 vues × 2 profils (1440 × 900, Pixel 7) × 3 thèmes (clair, Fond doré 100 %, sombre), horloge figée. 2. Écart de pixels (tolérance 32 par canal, seuil 0,2 %). 3. axe-core WCAG 2.2 AA, cliquet par vue et par règle sur les impacts graves et critiques ; contraste rapporté à part. 4. Débordement horizontal (bloquant sur mobile). 5. Polices : échecs de chargement, requêtes réseau, rendu hors ligne. 6. CLS au chargement (plafond 0,1, ou référence + 0,02). 7. Rapport en artefact, dans le résumé et en commentaire de PR. |
| Interdits | Aucune modification de la référence sans l’étiquette `visuel:nouvelle-reference` ; aucun seuil relevé pour verdir ; aucune écriture dans `app_v2.html` ni dans `orig/`. |
| Acceptation | Deux exécutions successives sur le même fichier donnent 0 capture changée. Une PR qui modifie `qa/visuel/reference*` sans étiquette échoue. Une PR qui ajoute un problème grave d’accessibilité échoue. |
| Livrable | La tâche « visuel », requise sur main après la fusion de sa propre PR. |
| Passation | Janus trie les rapports hebdomadaires ; Apollon adopte la référence de la refonte par la procédure du skill `ssp-qualite-visuelle`. |

## Fiche de mission · Apollon · frontend premium
Couleur : or soleil

> **Règle universelle.** (identique à celle d’Iris, ci-dessus.)

| Champ | Contenu |
|---|---|
| Mission | Apollon donne à `app_v2.html` une présentation haut de gamme, sobre et cohérente, sans changer ni contenu, ni données, ni identifiants, ni comportement. |
| Fichiers | Un seul patch de style, `tools/patches/NNNN-apollon-*.py` (skill ssp-patch) ; la spécification `qa/apollon/spec.md`. |
| Étapes | 1. Spécification (jetons, échelle typographique, composants) et maquettes avant/après de 2 à 3 onglets. 2. Patch CSS sur branche. 3. Attente de la fusion de Thémis, rebase, rejeu du patch. 4. Tests 43/43, gardes, Iris ; nouvelle référence adoptée explicitement. |
| Interdits | I1 à I8 ; aucune police externe ; aucun changement de JS, de texte, de données ou d’ID ; budget de 6 Mo. |
| Acceptation | 43/43 contrôles, gardes vertes, aucun nouveau problème axe-core grave, moins de nœuds en échec de contraste qu’avant, aucun débordement mobile, rendu identique hors ligne. |

## Entrées
- 17.10.2026 · Iris est écrit et rejoué deux fois sur le poste : 60 captures, 0 changée d’une exécution à l’autre. État de départ mesuré : 271 nœuds en échec de contraste en thème clair (16 en sombre), CLS 0,15 sur ordinateur, polices Google chargées par le réseau (rendu hors ligne différent de 1,08 %). Ces écarts sont tolérés par la référence de départ et désignés à Apollon.
- 17.10.2026 · Les références sont produites par la CI elle-même (rendu Ubuntu), jamais sur le poste, et stockées en WebP sans perte, à 1800 px de haut au plus, pour limiter le poids du dépôt (≈ 8 Mo par référence).
- 17.10.2026 · Iris est fusionné (PR #13), avec une référence de 60 captures adoptée par la procédure de l’étiquette. Thémis l’a déjà suivie pour la PR #14.
- 17.10.2026 · Apollon applique les directives du titulaire : texte justifié avec césure, titres noirs en gras, rouge réservé à l’information capitale, bandeaux d’en-tête vert pâle (fenêtre, sauvegarde, bandeau 2027, badge « À vérifier »), teintes de jour du calendrier et bandes de séance AA.
- 17.10.2026 · Iris gagne deux contrôles : l’état « cal-seances », qui mesure le contraste de 42 textes de séance (minimum 6,03:1 après refonte, contre 3,44:1 avant), et le « masquage » du haut de panneau sous la barre collante (18 vues masquées sur 18 avant, 0 après).
- 17.10.2026 · Défaut signalé à Hermès : l’onglet mémorisé « Notions CK » ou « Gestes » lève une erreur au rechargement. Le défaut existe déjà dans orig/app.html.
