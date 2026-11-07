# Ressources communes des IA (lecture seule)

Tout ce qu'il faut pour produire hors ligne, relevé le 30.10.2026. Aucune IA ne modifie ce dossier ; pour l'enrichir, copie dans ton propre dossier `<ia>-LOTS-html/_cache/`.

| Ressource | Chemin | Contenu | Mise à jour |
|---|---|---|---|
| Index AIPS | `aips/AipsDownload_20261008.xml` | toutes les informations professionnelles et notices suisses (numéro Swissmedic, titulaire, URL des documents officiels), édition du 08.10.2026 | téléchargement AIPS de Swissmedic/refdata |
| Informations professionnelles (FR) | `aips/fi_fr/<numéro>.txt.gz` | texte intégral français de chaque information professionnelle humaine (4 646), tiré des documents officiels `files.refdata.ch` | `python3 ressources_ia/outils/aips.py telecharger-tout` |
| Extraits déjà lus | `aips/extraits/<numéro>.txt` | 331 extraits ciblés écrits pendant LOT_013–017 | — |
| Outil AIPS | `outils/aips.py` | `chercher <nom ou numéro>` ; `lire <numéro> [motif]` (ex. `lire 29552 grossesse`) | — |
| Conditionnements autorisés | `swissmedic/swissmedic_conditionnements_autorises_2026-09-30.xlsx` | liste Swissmedic « Zugelassene Packungen » (numéro par forme galénique, statut) | https://www.swissmedic.ch/dam/swissmedic/de/dokumente/internetlisten/zugelassene_packungen_human.xlsx.download.xlsx/zugelassene_packungen_ham.xlsx |
| Médicaments humains autorisés | `swissmedic/swissmedic_medicaments_humains.xlsx` | liste Swissmedic des médicaments à usage humain | https://www.swissmedic.ch/dam/swissmedic/de/dokumente/internetlisten/zugelassene_arzneimittel_ham_ind.xlsx.download.xlsx/Zugelassene_Arzneimittel_HAM.xlsx |
| Liste des spécialités (OFSP) | `liste_specialites/liste_specialites_ofsp.json.gz` | 3 383 spécialités remboursées : formes, prix, limitations, dates d'admission | API https://epl.bag.admin.ch/api/sl/public/medicinal-products?page=1&size=100&search= |
| Preuves déjà lues | `../lot en cours de production/LOT_0*/evidence/` | extraits datés de toutes les sources des LOTS 013–017 (avec `INDEX.md`) | — |

Règles : les doses viennent de ces informations professionnelles suisses seulement, jamais du Compendium ; citer mot pour mot la dose, les contre-indications, la grossesse, l'allaitement et l'enfant ; donner le numéro Swissmedic de la forme galénique (vérifié dans la liste des conditionnements) ; tout usage hors information professionnelle est écrit en clair.
