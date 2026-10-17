# HANDOFF · passation entre sessions

Chaque agent ajoute sa section en tête, selon le modèle de l’annexe E2 du plan. Aucune donnée personnelle n’entre dans ce fichier public.

## Argos · veilles · 17.10.2026, Europe/Zurich
État       : Ve1 (OFSP, examen et inscription) et Ve2 (portail healthreg, Playwright) tournent par .github/workflows/veille-ve1.yml et veille-ve2.yml ; le premier rapport est enregistré.
Prochaine  : Argos teste la faisabilité de Ve3 (flux Swissmedic) et de Ve4 (XML Refdata) avant le 29.11.2026.
Sources    : robots.txt de bag.admin.ch et de healthreg-online.admin.ch lus le 17.10.2026 ; plan v2, section 11 et annexe D.
Pièges     : main est protégée ; veille/etat.json vit donc sur la branche veille-etat, que personne ne doit fusionner ni supprimer.
À vérifier : Janus contrôle vers le 17.11.2026 que la réactivation mensuelle (PUT …/enable) garde les veilles actives.

## Mnémosyne · mémorisation · 17.10.2026, Europe/Zurich
État       : data/MEM.json contient les douze méthodes et les références M1 à M24, reprises mot pour mot ; les 24 DOI se résolvent.
Prochaine  : En phase 2, après la fusion d’Hermès, Mnémosyne ajoute data-t="m|id" et les trois réglages, sur feat/memo-evidence.
Sources    : research_memorisation.md du 17.10.2026 ; doi.org, le 17.10.2026.
Pièges     : tools/build_mem.py régénère MEM.json ; on corrige la note source puis on relance le script, sans retoucher le JSON à la main.
À vérifier : Janus rejoue le contrôle des DOI sur la liste references de MEM.json.

## Athéna · coordination · 17.10.2026, Europe/Zurich
État       : La phase 0 est livrée : main est protégée, la CI (garde, html, liens, tests) réussit sur app_v2.html tel quel, et Pages publie l’application.
Prochaine  : Athéna ouvre les tickets de la phase 1 (brouillons dans journal/coordination.md), puis lance Atlas, Thémis et Argos dans cet ordre.
Sources    : J’ai lu le plan v2 (sections 1, 3, 4, 10, 12 et annexe E), le 17.10.2026.
Pièges     : Une ligne d’app_v2.html dépasse 4,8 millions de caractères ; les expressions régulières y expirent, et seul str.find fonctionne (tools/_app.py).
Pièges     : main exige une demande de fusion et les contrôles garde, html et tests, même pour l’administrateur ; aucun push direct n’aboutit.
Pièges     : GES est suivi de « ;const GES_SRC=… » sur la même ligne ; tools/_app.py délimite donc les constantes JSON par json.raw_decode.
À vérifier : Le jeton gh n’a pas le droit « project » ; le tableau Projects attend `gh auth refresh -s project` par le titulaire du compte.

## Prompt de continuité (annexe E3)
Tu es <Agent>, l’agent chargé de <spécialité> dans le projet « Organigramme Examen fédéral ».
Lis d’abord HANDOFF.md, ETAT.md et journal/<chantier>.md, puis ta fiche de mission (plan v2, section 4).
Ne lis jamais app_v2.html en entier : applique ssp-extrait-cible, ssp-patch et ssp-json-data.
Vérifie chaque modification avec ssp-tests, et contrôle chaque texte avec ssp-verite.
Ne modifie jamais app.html. N’utilise que des sources suisses et européennes, et des images réelles.
Respecte la règle universelle : le projet cible doit avoir un résultat de HAUTE QUALITÉ ; l’usage des jetons doit être raisonnable et optimisé, et tout gaspillage est formellement interdit ; l’économie de jetons est autorisée si et seulement si elle ne dégrade pas la qualité du travail.
Avant de t’arrêter, mets à jour HANDOFF.md, ETAT.md et ton journal.
