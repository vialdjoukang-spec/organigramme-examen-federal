# Droits et pertinence — LOT 133 — 2 novembre 2026

Agent : `/root/droits_2044`. Périmètre : contrelecture des candidats radio/hemato et recherche distincte. Aucune modification HTML, globale ou Git.

## Contrelecture indépendante — hématologie

Rapport relu : `evidence/HEMATO_2044.json`. Aucun candidat prêt à intégrer. Chula-RBC : fichier LICENSE téléchargé indépendamment depuis API originale ; MIT Copyright 2021 Chula PIC Lab, formulation logiciel, et non CC0/BY/BY-SA/PD admis au mandat. Rejet confirmé sans prétendre que MIT interdirait juridiquement toute réutilisation. Preuve : `_travail/_cache/droits_2044/chula_LICENSE.txt`. Les autres rejets documentés dans HEMATO_2044 ne deviennent pas des licences vérifiées par cette contrelecture : aucun pixel disponible à auditer. Une licence de publication ou d’un dérivé ne remplace pas une autorisation originale des images.

## Acquisition distincte proposée — NON auto-auditée

Cliché thoracique authentique original, dépôt des auteurs Hannover Medical School :

- Dépôt : https://github.com/ml-workgroup/covid-19-image-repository
- Commit : `ad7ab099b425f16e06bba22322336b7d6a732965`
- Image : https://raw.githubusercontent.com/ml-workgroup/covid-19-image-repository/ad7ab099b425f16e06bba22322336b7d6a732965/png/00870a9c.png
- Licence : README « Master-, image- and laboratory-data of this repository are licensed under ... CC BY 3.0 ». LICENSE contient Attribution 3.0 Unported. Le README affirme que les images viennent de l’Institute for Diagnostic and Interventional Radiology, Hannover Medical School ; PNG réduits distribués par les auteurs eux-mêmes. Ce n’est pas un miroir d’un site refusé.
- Attribution requise par auteurs : auteurs du jeu COVID-19 Image Repository, institut précité, DOI https://doi.org/10.6084/m9.figshare.12275009 et licence https://creativecommons.org/licenses/by/3.0/. Les noms individuels restent à établir si souhaités ; ne pas les inventer.
- Copie : `_travail/_cache/droits_2044/png_00870a9c.png`, 640 × 524 ; SHA256 `62f73ee8798a45a6c4189c88c3b127c5b284a9c1e42fb26edf09eee38bb93ef0`.
- README, LICENSE, data.csv, arbre, commit et manifeste `candidate.json` conservés dans le même cache. Aucun filtre ni ajout aux pixels source.

Pertinence proposée DX3 : illustration d’opacités pulmonaires bilatérales. Métadonnées : CR/AP. Repère R original conservé. Ni pneumothorax, ni diagnostic de COVID-19 ou d’insuffisance respiratoire aiguë ne doivent être déduits des seuls pixels. FiO2 inconnue ; aucune gravité gazométrique imputée. Les dispositifs visibles ne sont pas des lésions.

Proposition d’annotation pour validation indépendante : pointe 1 vers (188,278), opacités basales droites ; pointe 2 vers (525,338), opacités basales gauches. Ne pas changer l’orientation. Mentionner « flèches et légende ajoutées » sur toute adaptation ; conserver source/attribution/licence.

L’agent `/root/radio_2044` a confirmé indépendamment les opacités bilatérales, la projection AP, le repère R et la clause CC BY3.0. Validation finale droits, cadrage pédagogique et annotations confiée à root : l’acquéreur n’émet pas son propre audit favorable.

## Recherche et réseau

Politique restricted/enforced vérifiée via outil environnement et fichier local. Recherche EuropePMC et recherche OUP refusées HTTP403 ; aucune relance par miroir ou modification proxy. Medical Journals Sweden recherche : HTTP503. NIHCC/ChestXray-NIHCC : dépôt inexistant ; autres résultats NIH tiers non retenus et aucun domaine public présumé. Le README de la collection Cohen a permis de découvrir la source originale Hannover ; aucune image récupérée dans cette collection tierce. Acquisition finale exclusivement depuis le dépôt original Hannover.
