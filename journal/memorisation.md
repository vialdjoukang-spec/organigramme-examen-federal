# Journal · Mémorisation · Mnémosyne

Chaque entrée porte une date (Europe/Zurich), une décision et les sources lues. Aucune donnée personnelle n’entre dans ce journal public.

- Le chantier démarre à sa phase (plan v2, section 3) ; aucune entrée pour l’instant.

## 17.10.2026 · Phase 1 · data/MEM.json (Mnémosyne, données seules)
- J’ai construit data/MEM.json par tools/build_mem.py, qui reprend mot pour mot research_memorisation.md : douze méthodes, avec pour chacune le texte de la fenêtre, les preuves générales, les preuves en médecine (statut et texte), les références et la ligne du tableau de synthèse.
- Le script vérifie qu’il y a douze méthodes et 24 références (M1 à M24), et que chaque DOI cité a sa référence complète ; chaque texte repris figure tel quel dans la note source.
- Les 24 DOI se résolvent auprès de doi.org (API des handles, code 1) le 17.10.2026 ; Janus peut rejouer ce contrôle sur la liste `references`.
- La méthode 12 (techniques à faible utilité) n’a pas de bloc « Preuves en médecine » dans la note ; le champ vaut donc null, et la méthode 5 n’a pas de bloc « Preuves générales ». Je n’ai rien ajouté.
- L’intégration dans app_v2.html (type m|id de tipFor) attend la phase 2, après la fusion d’Hermès.

## 17.10.2026 · Phase 2 · intégration dans app_v2.html (Mnémosyne)
- J’ai corrigé tools/build_mem.py : la ligne de séparation du tableau de synthèse était lue comme la méthode 1, donc chaque « synthese » portait la ligne de la méthode précédente.
- J’ai écrit data/MEM_app.json : pour chaque méthode, une ligne « Pour l’examen fédéral » qui ne cite que des fonctions réelles (calendrier, « Lu · séance accomplie », « QCM réussis % », note de séance, fiche éclair, liste « À réviser », recherche par diagnostic différentiel, notions CK, Synthèse locale, onglet CS), et la liste des phrases du « Texte à coller » qui décrivaient des fonctions absentes (invite « Pourquoi ? », minuteur, masquage du contenu).
- Patch 0015 : carte de 12 méthodes, type m|id, deux options nouvelles, consigne de séance ; les clés de réglage existantes restent intactes (contrôle reglages_anciens_intacts).
- Recoupement lu le 17.10.2026 : PubMed 19930508 confirme 39 % contre 26 % et d = 0,91 (Larsen 2009) ; ERIC EJ1310148 confirme g = 0,74 (Latimier 2021).
