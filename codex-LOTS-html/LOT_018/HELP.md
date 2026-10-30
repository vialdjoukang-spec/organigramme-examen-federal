# Points ouverts — LOT_018

État au 30.10.2026 : première rédaction de la Phase A terminée ; LOT non clôturé.
Fichier : `LOT_018_Phase_A_V0.html`. Aucun score médical attribué.

## H1 — Classement des dix diagnostics

Les dix diagnostics et le tableau comparatif sont présents, mais leur ordre est provisoire. Les sources lues ne permettent pas de classer leur prévalence dans une population unique correspondant à ce symptôme composite. Les 6,2 % Obsan concernent une difficulté visuelle déclarée dans l’ESS 2012/2017, et non une distribution étiologique des consultations.

À résoudre pendant l’audit : préciser le contexte de classement, documenter les rangs par des données comparables et décider de la sélection. `LISTE_DX_CANONIQUE_PROVISOIRE.md` n’est pas une liste gelée. Aucun fichier de Phase B n’a été créé.

## H2 — Audit indépendant avant Phase B

`PROMPT_CODEX.md`, §6.3 : « Audit médical de la Phase A (poste auditeur, passe distincte — nouvelle tâche Codex ou nouvelle session, jamais dans la même passe que la rédaction) » ; cette passe gèle la liste.

§9.2 : « L’auditeur médical n’est pas le même modèle que le rédacteur » ; avec un seul modèle fort, le prompt prévoit `audit_croise_externe: true`.

Vial demande un travail seul. La production a donc été réalisée dans la session principale, avec GPT-6 Astra · ultra confirmé par Vial. L’audit externe est déclaré comme différé ; aucun auditeur n’a été contacté ni lancé pour cette production. Le script de routage refuse de consigner un poste différé. Les contrôles Python et la relecture du rédacteur ne satisfont pas l’exigence d’indépendance.

Prochaine étape : audit médical dans le cadre distinct exigé par le prompt, vérification des doses et sources, puis gel documenté de la liste. Les rôles différés ne doivent être activés qu’avec leur modèle réellement utilisé et leur passe effectivement réalisée.

## H3 — Contrôleurs historiques et norme V8

Les scripts officiels sont inchangés et leurs rapports bruts sont conservés :

- `audits/controle_officiel.json` : deux critiques (`title` et absence de références littérales `[S1]`).
- `audits/langue.json` : critique `title`, plus avertissements de langue et de typographie à examiner.
- `audits/controle_gabarit_officiel.json` : le contrôleur produit quatre critiques sur le modèle V8 officiel lui-même.

La section 12 de `PROMPT_PRODUCTION_V2.md` exige pourtant `<abbr title>` et des références en exposant, « jamais [S16] ». Les définitions d’abréviations sont conservées. La section Sources comporte huit entrées identifiées, reliées aux exposants. La critique des lignes trop longues a été corrigée dans le fichier produit ; les polices sont embarquées pour éviter une dépendance distante.

`audits/structure_v8.json` vérifie seulement les identifiants, liens, fenêtres, citations AIPS, polices et tailles. Son résultat positif ne remplace ni le contrôle officiel, qui reste négatif, ni un audit médical ou de conformité. Le fichier `MANIFESTE.json` est une empreinte du brouillon, pas une clôture de LOT. L’autorité qui maintient le harnais doit résoudre son désaccord avec la norme avant acceptation finale.

## H4 — Rendu visuel non vérifié

Le navigateur Playwright fourni n’était pas installé. Son téléchargement a reçu HTTP 403 (« Domain forbidden »). Chromium présent sur la machine a ensuite refusé l’ouverture locale avec `net::ERR_BLOCKED_BY_ADMINISTRATOR`. Ces restrictions n’ont pas été contournées.

Il reste à vérifier dans un environnement autorisé : lecture sur téléphone, contraste clair/sombre, clavier, défilement des tableaux, ouverture des sous-fenêtres et maintien de leur fenêtre parente après fermeture. Une règle locale limite le décalage horizontal des sous-fenêtres sur écran étroit ; son rendu n’a pas été mesuré. Aucune capture d’écran ni validation mobile n’est revendiquée.

## H5 — Glucocorticoïdes et statut d’emploi dans l’ACG

La stratégie d’urgence repose sur les recommandations EULAR lues. Les chiffres d’un protocole EULAR ne sont pas repris comme posologie AIPS. La fenêtre thérapeutique conserve les citations suisses relatives à la vitesse d’administration, aux contre-indications et à la grossesse, tout en signalant le protocole propre à l’ACG comme à vérifier.

Avant validation : déterminer la spécialité, la dose, la voie et le statut exact dans son information professionnelle ; expliciter tout usage hors information professionnelle. Ne pas interpréter les durées minimales d’injection citées comme un protocole complet d’ACG ou de névrite.
