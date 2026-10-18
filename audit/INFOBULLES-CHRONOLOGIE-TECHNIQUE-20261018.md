# Contre-audit technique indépendant · chronologies

Verdict : favorable sur la tête3613c38 après correction des défauts signalés ci-dessous. Aucun code canonique, app, garde/permanence ou workflow modifié par la sentinelle ; aucun navigateur local, lancement distant, adoption ou fusion.

## Rendu et compatibilité

Les fiches opt-in rendent six rubriques. La rubrique5 affiche exp_ref une fois, puis bilan_ordre numéroté (première étape identique à exp_premier), puis dia une fois. Le rendu chronologique n’ajoute plus les anciens exp_bio/exp_morph/exp_fonc/exp après cette séquence. La rubrique6 conserve A-But puis B-Moyens, phases numérotées et moyens mes/pha/aut dans la phase concernée. Les phases peuvent annoncer des actions parallèles ; leur ordre clinique reste à relire par un auditeur médical.

Les listes exigent1–6éléments, titres/textes non vides et clés admises ; les phases couvrent au moins mesures générales et pharmacologie, avec Autres facultatif selon pertinence. Un legacy sans drapeaux garde son rendu, sans être inventé comme chronologie relue. Les vieux champs sont conservés dans les données mais ne doivent pas servir de duplicata visuel. Leur information cliniquement utile doit être reprise dans les étapes par la rédaction : cette fidélité sémantique ne peut pas être prouvée par le schéma seul.

## Défauts trouvés et corrigés par le rédacteur

1. Le chemin binomes.py --check appelait chronology_review_ids avec trois arguments au lieu des cinq nécessaires : TypeError. Corrigé dans01a8e0a ; le chemin complet --check a été rejoué avec succès et possède un test dédié.
2. Les balises imbriquées STRONG/B majuscules échappaient au contrôle du gras, sensible à la casse. Corrigé dans3613c38 par re.I et test majuscule.
3. prototype_version=1.0 était accepté par prototype_ready mais rejeté par la jauge chronologique, rendant les compteurs incohérents. Contrat aligné dans3613c38 : entier1 strict, booléens et flottants rejetés.

## Gardes et attestations

Le contrôle de texte est récursif pour les structures imbriquées. La garde pharmacologique de mono_build contrôle les pha de chaque phase. Les doses déplacées dans mes/aut ne sont pas du ressort de cette garde ciblée, mais le checkpoint récursif les rejette également : cas mes, pha et aut effectivement essayés avec une table AIPS vide, tous bloqués. Pas de fuite globale de dose constatée par ce déplacement.

La nouvelle jauge documentaire ne compte pas une mention libre dans un rapport : elle exige une entrée du registre central de version entière1, chronologie_relue exactement true, validation_clinique exactement false, statut revue_documentaire, empreinte complète de la fiche actuelle, date valide non future, sources présentes au registre et rapport dont l’empreinte correspond. Le chemin du rapport ne peut pas être absolu ou remonter par ../. Une modification de la fiche ou du rapport révoque la reconnaissance. Les mesures structurelles et la relecture restent distinctes ; aucun accord clinique humain n’est inféré.

Le registre couplé de coordination exige lui aussi le drapeau chronologie_relue pour SSP et diagnostics. Les anciennes fiches et leurs anciens rapports ne sont pas rétrovalidés : le calcul réel HEAD conserve257monographies legacy mais zéro chronologie structurée et zéro nouvelle relecture chronologique reconnue, état attendu avant migration des données.

## Vérifications exécutées

- 14tests mono_prototype,6tests chronologie_jauges et8tests coordination_crise :28réussis.
- binomes.py --check --ref HEAD : réussi.
- Cas limites indépendants : dix versions invalides (booléens, flottants, chaînes, null), trois balisages gras majuscules/mixtes et cinq fausses attestations (1à la place de true,0à la place de false, statut booléen, date future, rapport remontant) rejetés.
- Checkpoint : doses nouvelles dans trois catégories de phase toutes refusées sans table AIPS correspondante.
- git diff --check : réussi.

Les validations G1–G8, la terminologie cliquable, l’ordre clinique réel du bilan/de la prise en charge et le rendu navigateur doivent être revérifiés sur les fiches effectivement intégrées. Aucun verdict technique ne valide leur contenu médical.
