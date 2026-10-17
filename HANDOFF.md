# HANDOFF · passation entre sessions

Chaque agent ajoute sa section en tête, selon le modèle de l’annexe E2 du plan. Aucune donnée personnelle n’entre dans ce fichier public.

## Thémis · Exigences 2027 · 17.10.2026, Europe/Zurich
État       : L’onglet « Exigences » compte 46 cases stables (data/EXI.json), un bandeau 2027 et des badges « À vérifier auprès de la MEBEKO » ; SESSION centralise les dates ; patch 0004 ; tests/test_exigences.py (13 contrôles) ; suite 69/69, gardes 5/5.
Prochaine  : Thémis met data/SESSION.json à jour (tools/build_exi.py, puis json_inject.py inject SESSION) dès que l’OFSP publie les dates 2027.
Sources    : research_exigences.md (S1 à S12, N1), lues le 17.10.2026.
Pièges     : Les coches vivent sous « x:<id> » dans S.exi, à côté des clés a… (Attendus) et cp… (CS) ; on ne renumérote jamais un identifiant.
À vérifier : A3, A4, C4, C6, C7, C8, C10, D2, D5, E2 et E3 attendent une réponse de la MEBEKO ou une publication de l’OFSP.

## Atlas · sauvegarde · 17.10.2026, Europe/Zurich
État       : Le chantier export/import est sur feat/sauvegarde (PR #11) : patch 0003, CSS du bandeau dans le style de head, tests/test_export.py (13 contrôles) ; suite locale 56/56 et gardes 5/5.
Prochaine  : Athéna fusionne PR #11 dès que la CI (garde, html, tests) est verte.
Sources    : Ticket #5 ; plan v2 fiche Atlas ; MDN Storage quotas ; WebKit 7-Day Cap (lus le 17.10.2026).
Pièges     : Toute règle CSS nouvelle dans le style de body crée des erreurs Nu ; le bandeau #bak doit rester dans le style de head.
À vérifier : Le rappel d’export à sept jours et le message de stockage plein sont couverts par tests/test_export.py.

## Argos · veilles · 17.10.2026, Europe/Zurich
État       : Ve1 (OFSP) et Ve2 (healthreg) sont dans main (PR #4 fusionnée) ; workflows veille-ve1.yml et veille-ve2.yml actifs.
Prochaine  : Argos teste la faisabilité de Ve3 (flux Swissmedic) et de Ve4 (XML Refdata) avant le 29.11.2026.
Sources    : robots.txt de bag.admin.ch et de healthreg-online.admin.ch lus le 17.10.2026 ; plan v2, section 11 et annexe D.
Pièges     : main est protégée ; veille/etat.json vit donc sur la branche veille-etat, que personne ne doit fusionner ni supprimer.
À vérifier : Janus contrôle vers le 17.11.2026 que la réactivation mensuelle (PUT …/enable) garde les veilles actives.

## Mnémosyne · mémorisation · 17.10.2026, Europe/Zurich
État       : data/MEM.json contient les douze méthodes et les références M1 à M24, reprises mot pour mot ; les 24 DOI se résolvent (PR #3).
Prochaine  : En phase 2, après la fusion d’Hermès, Mnémosyne ajoute data-t="m|id" et les trois réglages, sur feat/memo-evidence.
Sources    : research_memorisation.md du 17.10.2026 ; doi.org, le 17.10.2026.
Pièges     : tools/build_mem.py régénère MEM.json ; on corrige la note source puis on relance le script, sans retoucher le JSON à la main.
À vérifier : Janus rejoue le contrôle des DOI sur la liste references de MEM.json.

## Athéna · coordination · 17.10.2026, Europe/Zurich
État       : La phase 0 est livrée ; les tickets de phase 1 (#5 à #10) sont ouverts ; MEM.json et les veilles Ve1/Ve2 sont dans main ; les dix skills sont dans la bibliothèque partagée.
Prochaine  : Fusionner PR #11 (Atlas) quand la CI est verte ; la version datée de phase 0 attend encore l’accord du titulaire (I6).
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
