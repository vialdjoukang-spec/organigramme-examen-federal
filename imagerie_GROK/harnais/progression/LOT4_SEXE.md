# Lot 4 — sexe explicite et contour en silhouette

Branche `cursor/interface-didactique-ffbc`. 14.11.2026.
Trente id. Sexe lu seulement dans `caption_source` : male, female, woman, women, girl, boy, homme, femme, garçon, « year-old man », « yo man ». « Man erkennt » et « Säugling », « child », « Prostatakrebs » ne comptent pas. Sinon sexe « À vérifier » et statut partiel.
Un complet exige les deux sexes égaux, un contour d’au moins 8 sommets non rectangulaire relu sur l’overlay, et une `definition_source` qui n’est pas « À vérifier ». Même modalité, même plan, même séquence. Licences CC0, domaine public, CC BY, CC BY-SA.

Contrôle : `python3 scripts/validate.py --only` sur ces trente id, 0 erreur. Complets validés : 2. Partiels : 28.

## Complets

| id | sexe | paire |
| --- | --- | --- |
| IMG-257 | F / F | DIU en place (female, 25 ans) et DIU perforé (woman, 67 ans), US sagittale mode B. |
| IMG-267 | M / M | Face d’épaule en place (male, 26 ans, vide articulaire) et luxation avant réduction (male, 25 ans). Hill-Sachs et Bankart absents de cette incidence. |

## Bloquants (partiels)

| id | sexe N / P | pourquoi ce n’est pas complet |
| --- | --- | --- |
| IMG-245 | À vérifier / À vérifier | légendes sans male ; axial contre longitudinal |
| IMG-246 | À vérifier / À vérifier | légendes sans male ; plans différents |
| IMG-247 | À vérifier / À vérifier | légendes sans boy/male ; pas une sonde inguinale nommée |
| IMG-249 | F / F | woman des deux côtés, même endovaginale oblique ; la normale est un corps jaune gravide |
| IMG-250 | F / À vérifier | fibrome sans woman/female |
| IMG-254 | F / À vérifier | adénomyose sans woman/female |
| IMG-255 | F / À vérifier | SOPK sans woman ; plan oblique contre rendu 3D |
| IMG-258 | F / F | sagittal contre oblique |
| IMG-327 | À vérifier / À vérifier | « Prostatakrebs » n’est pas male |
| IMG-337 | À vérifier / À vérifier | loge de Morison sans sexe |
| IMG-339 | M / À vérifier | nourrisson, « Säugling » n’est pas boy/girl ; plans différents |
| IMG-342 | À vérifier / À vérifier | TEP sans sexe ; le second volet est un contrôle traité |
| IMG-343 | À vérifier / À vérifier | TEP sans sexe ; plans différents |
| IMG-344 | F / F | femme des deux côtés ; TDM médiane de grossesse contre phase pancréatique axiale et coronale. Le cliché masculin de 21 ans a été retiré (sexe discordant). |
| IMG-263 | — / À vérifier | « Fötus » n’est pas woman ; pas de normale |
| IMG-265 | — / À vérifier | fistule T2 sans sexe ; pas de pelvis normal |
| IMG-266 | — / À vérifier | rectocèle sans woman ; pas de plancher normal |
| IMG-268 | M / À vérifier | fracture de clavicule sans sexe |
| IMG-269 | — / À vérifier | coiffe sans sexe ; pas d’échographie normale |
| IMG-270 | M / À vérifier | dépôt calcique sans sexe. Le cliché fléché d’une femme de 33 ans n’a pas de face normale de femme. |
| IMG-271 | M / À vérifier | disjonction sans sexe ; la normale n’est pas comparative |
| IMG-272 | À vérifier / À vérifier | « child » n’est pas boy/girl ; profil seul |
| IMG-273 | M / À vérifier | tête radiale sans sexe |
| IMG-274 | — / À vérifier | avant-bras sans sexe. La face « female 63 years » ne montre que le coude : non retenue. |
| IMG-277 | M / À vérifier | « Man erkennt » et « 12-jährigen » ne sont pas un sexe ; face seule contre face et profil |
| IMG-278 | M / À vérifier | scaphoïde sans sexe |
| IMG-280 | M / À vérifier | érosions sans sexe ; pas de pieds |
| IMG-281 | M / À vérifier | rhizarthrose sans woman. Une main de femme de 71 ans existe, sans main normale de femme : non appariée à l’homme de 31 ans. |

Overlays relus : `progression/captures-interface/lot4/IMG-*.png`.
