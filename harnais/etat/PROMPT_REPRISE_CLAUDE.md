# PROMPT DE REPRISE — Claude (orchestrateur), à lire en premier à la reprise après la pause du 28.10.2026

**Mission.** Orchestrer la production des fiches Flash des 248 SSP (= 248 LOT, PROFILES 2023 ; liste : `harnais/etat/LOTS_248_DD.md`) pour Vial, médecin en spécialisation. Dépôt `vialdjoukang-spec/organigramme-examen-federal`, branche `claude/blissful-edison-1vq7na`. Réponses courtes, en français.

## Ordres de Vial en vigueur (non négociables)
- **Fiche Flash** : Pareto (20 % utile / 80 % résultat), phrases complètes, style universitaire, îlots à bordure et texte justifié (points 1-4 ensemble, 5-6 ensemble, reste replié), vraies fenêtres modales, mots interactifs partout, syndrome en tableau à 2 colonnes, algorithme en cases à traits orthogonaux. Référence : `harnais/etat/COURS_FLASH.md`, gabarit `harnais/brain/gabarit_flash.html`.
- **Volume** : 100–200 Ko, cible 150 ; jamais > 298 Ko (bloquant). Mesure : `python3 harnais/brain/mesure_ko.py`. Toujours s'assurer que le fond reste exact.
- **Vitesse** : production d'abord ; limite de 240 s par fragment pour le duo Sonnet (lanceur parallèle).
- **Opus / professeurs / auditeurs SUSPENDUS** jusqu'après le 248e LOT (fichier `.cache/brain/sans_professeur`). Les audits viennent à la fin. La mise en forme finale est faite à l'assemblage par un agent Sonnet 5.5 (`assembleur-mise-en-forme`).
- Refus notifié + correction, jamais d'arrêt sec ; un refus d'agent est détecté, consigné, relancé une fois avec le contexte légitime.
- Souplesse : un défaut sans conséquence pour l'apprentissage est un avertissement. Doses : AIPS suisse seulement ; jamais de chiffre ni de dose inventés.
- Ne jamais modifier `/workspace/ssp/app.html`. Aucune donnée personnelle dans ce dépôt public. Ne commiter dans `LOT_Claude_Finaux` que si la porte et le pré-commit passent, jamais en les contournant.
- Commits terminés par « Co-Authored-By: Claude Sonnet 5.5 <noreply@anthropic.com> » et « Claude-Session: https://claude.ai/code/session_01QZK4dvwhmDEnsTae9bMPTq ».

## État à la pause (28.10.2026, ~23:05 UTC)
- LOT_001 : 16/16 leçons rédigées (`essai_lot001/`) ; LOT_002 : 9/16 ; LOT_003 : 0/14 ; LOT_004 : 0/12. Rien promu dans `LOT_Claude_Finaux`.
- Porte médicale : le fichier AIPS doit être dans `.cache/aips/AipsDownload_20261008.xml` (le redemander à Vial si le conteneur est neuf). Fautes de langue restantes : consignées pour l'audit final.
- Le conteneur redémarre souvent : tout est enregistré leçon par leçon (`journal/*.fait.json`).

## Reprendre
1. `python3 harnais/brain/radar.py` (état).
2. `bash harnais/brain/relance_tout.sh` (idempotent ; capacité Sonnet : `.cache/brain/sonnet_max`, 48 ; surveiller la charge).
3. Veille de 15 min par `send_later` tant que des agents tournent ; republier l'état des lieux https://claude.ai/artifact/2xqRY3GJsgpLBFhXM2VR6S et le suivi par leçon https://claude.ai/artifact/KAujan5Hb5tTh7xPWLMbTk (`python3 harnais/brain/suivi_html.py`).
4. Livrer à Vial : 3 captures du LOT_001 (îlots, fenêtre ouverte, tableau syndrome, algorithme) et le tableau .md des fautes restantes ; puis PR (draft) et fusion par commit de fusion après CI verte.
5. Étendre au LOT 005 puis aux suivants ; hygiène : `macrophage.py`, `detective.py`.

## Questions ouvertes pour Vial
Volume exact voulu (100–150 ou 100–200 Ko) ; sens de « Les Lots avec… » (message coupé) ; coût (~5 $ par leçon mesuré, soit de l'ordre de 20 000 $ pour 248 LOT) et rythme acceptable.
