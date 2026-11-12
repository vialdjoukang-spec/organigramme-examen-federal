# Audit médical A — LOT_024 Phase A (SSP S1.8, écoulement auriculaire)

| Élément | Valeur |
|---|---|
| Fichier | `LOT_024_Phase_A_V0.html`, 81 796 octets, SHA-256 `35f60693…72ea` |
| Date, auditeur | 12.11.2026, auditeur médical indépendant (Claude, sous-agent) ; cours non modifié |
| Lu | Rapport `controle_lot.py verifier` (NON CONFORME : ressource externe, Phase A < 100 Ko, titres Phase B DX.4–DX.10 décalés : contrôles non refaits) ; extraction des points 2, 3, 4, 8, 9, 11, 12 ; liste DX ; tableau ; arbre (point 10) |
| Sources confrontées | `dl24/` : HUG (S2, S4, S5, S6), SSI 2406 (S3), ENT UK (S8), Wiegand 2019 (S7), résumés PubMed (S9–S14, S16) ; S15 lu ce jour (PMID 9298613) ; `aips24/` : Panotile 31957, Ciproxin HC 54807, Ciloxan 51898 |
| Calcul refait | (1 405 − 123) / 123 = **+1 042 %** (× 11,4), outil Python |

## Score §12.2 (points audités)

| Point | Note | Raison |
|---|---|---|
| 2 Épidémiologie | 1 | Hausse de l'otite nécrosante fausse (n° 7) ; colonne « fréquence » sans chiffre pour DX.2, DX.3, DX.5 ; contradiction de sources non signalée |
| 3 Physiopathologie | 2 | Conforme à S7, S17, S3, S4 ; une seule déduction mineure (n° 20) |
| 4 Démarche | 1 | Pile bouton placée après le cholestéatome ; ligne « complication » extrapolée de la SSI |
| 8 Diagnostic positif | 1 | Cellules non soutenues (DX.7, DX.10) ; titres conformes à la liste |
| 9 Examens | 1 | Omet la biopsie systématique de l'otite nécrosante (S7) |
| 11 Prise en charge | 1 | Contenu riche, mais 11.A–D absents, aucune dose AIPS, CI AIPS incomplètes, critère « sans ototoxicité » faux, usages hors AIPS non signalés |
| 12 Prévention | 1 | Deux déductions attribuées à des sources qui ne les contiennent pas ; mesure « conduit sec » de S7 omise |
| **Total** | **8/14 = 57 %** | **Refusé** (< 90 %, défauts bloquants) |

## Corrections

| N° | Classe | Emplacement, extrait exact | Correction | Source |
|---|---|---|---|---|
| 1 | bloquante | P11 : aucun sous-titre 11.A, 11.B, 11.C ni 11.D ; amoxicilline sans spécialité, dose ni n° Swissmedic | Créer 11.A–D. Ajouter les situations spéciales, les seuils de surveillance et les critères de sortie. Donner la dose SSI de l'amoxicilline avec son AIPS lue. Citer la grossesse et l'allaitement de Ciproxin HC (« ne doit pas être utilisé… sauf absolue nécessité ») et de Panotile (« prudence »). | Prompt V0 §9 l. 373, §17 ; SSI 2406 ; AIPS 54807, 31957 |
| 2 | bloquante | P11 : « Un tympan non visualisé impose donc de choisir une préparation sans ototoxicité, avec l'ORL » | Critère faux : l'AIPS de Ciproxin HC ne décrit aucune ototoxicité chez le cobaye, mais contre-indique une perforation « connue ou supposée ». Écrire : « Un tympan non visualisé exclut toute préparation dont l'AIPS contre-indique la perforation connue ou supposée (Ciproxin HC, Panotile) ; l'ORL choisit d'après l'AIPS. » | AIPS 54807 |
| 3 | bloquante | P11 : « L'AIPS de Panotile interdit son emploi en cas de perforation du tympan » | Contre-indication adoucie. L'AIPS ajoute « après interventions chirurgicales et lors d'une lésion préexistante du conduit auditif ». | AIPS 31957 |
| 4 | majeure | P11, fenêtre « Gouttes et tympan » : CI Ciproxin HC réduite à la perforation | Ajouter « Infections fongiques » (lien avec DX.4) et « n'est pas indiqué pour le traitement d'une otite moyenne » (lien avec DX.2). | AIPS 54807 |
| 5 | majeure | P11 : « Chirurgie : une fuite otologique de liquide cérébrospinal se traite chirurgicalement » ; P4 E1 « … et chirurgie » | Généralisation abusive. Les HUG proposent parfois une surveillance sans intervention selon la fracture. Réserver la chirurgie certaine à la fuite otogène de la série S14. | S5, S14 |
| 6 | majeure | P11 : « Des collyres antibiotiques, surtout l'ofloxacine, servent parfois hors indication… sort de leur information professionnelle S7 » | Une revue allemande ne prouve pas l'AIPS suisse. Citer l'AIPS de Ciloxan 51898 (indication oculaire seule). Pour l'ofloxacine, lire son AIPS ou retirer l'affirmation. | AIPS 51898 |
| 7 | majeure | P2 : « L'otite externe nécrosante a augmenté de 1 142 % en Angleterre entre 2002 et 2017 » | 123 → 1 405 cas = × 11,4, soit +1 042 %. Le résumé de S10 indique 1 142 %, ce qui est une erreur de calcul de la source. Écrire « multipliée par 11 ». | S10, calcul refait |
| 8 | majeure | P11 : « Mèches… ciclopirox, nystatine, clotrimazole ou miconazole » ; « fluconazole ou itraconazole » | Signaler l'usage auriculaire hors information professionnelle suisse. Marquer ces molécules « À vérifier (AIPS) », car elles sont absentes du corpus. | S7 ; Prompt V0 §13 |
| 9 | majeure | P4 étape 5 et P11 : « L'antibiothérapie intraveineuse dure plusieurs semaines » | S7 donne « au moins 4–6 semaines », par voie parentérale ou orale selon l'antibiogramme. Le choix intraveineux vient de la série S12. | S7, S12 |
| 10 | majeure | P9 : biopsie absente pour l'otite nécrosante | Ajouter : « Une biopsie s'impose toujours pour exclure un carcinome ou un cholestéatome du conduit. » | S7 |
| 11 | majeure | P4 et P10 : pile bouton après « E3 — Cholestéatome » | Incohérent avec la ligne « Minutes » du P11. Placer la pile bouton en tête de l'arbre, ou préciser que l'ordre E ne règle pas le délai. | S8 |
| 12 | majeure | P10 : « tente un seul retrait adapté, puis adresse à l'ORL en cas d'échec » | Contredit le P11 (« plusieurs tentatives ») et ENT UK (« multiple failed attempts »). Écrire : « La première tentative est décisive ; l'échec répété fait adresser. » | S8 |
| 13 | mineure | P2 DX.10 : « La plus rare ; elle suit surtout une fracture de la base du crâne. S5 S14 » | Aucune source citée ne compare les fréquences ni ne désigne une cause dominante. S13 dit seulement « rare phenomenon ». | S13 |
| 14 | mineure | P2 : « L'otite moyenne aiguë perforée vient ensuite, car l'otorrhée signe la perforation » ; cellules DX.2, DX.3, DX.5 | Le motif n'est pas une fréquence. Ajouter que l'OMA est « rare chez les adultes » (S3) et que l'otite moyenne chronique suppurée est devenue « presque inexistante » en Finlande (S15). | S3, S15 |
| 15 | mineure | P2 : « Sa fréquence baisse toutefois après 60 ans S2 » | Signaler la divergence avec Neher : chez l'homme, le pic se situe vers 70 ans. | S2, S9 |
| 16 | mineure | P2 : « …treize patients…, ce qui confirme sa rareté hors d'un registre national » | Retirer : une série monocentrique ne mesure pas une incidence. | S12 |
| 17 | mineure | P4 : « Fièvre élevée… Rechercher une infection systémique et une mastoïdite S3 » | La SSI vise seulement l'altération de l'état général du jeune enfant. « Fièvre élevée » et « mastoïdite » ne figurent pas dans la recommandation. | S3 |
| 18 | mineure | P8 DX.7 : « Traumatisme, douleur, saignement. Otoscopie S6 » | S6 dit : douleur soudaine, baisse auditive, acouphènes, parfois vertiges. | S6 |
| 19 | mineure | P11 : « Un antibiotique oral se justifie seulement en cas d'extension, de diabète mal équilibré ou d'immunodépression » | Ajouter « ou si le traitement local est impossible ». | S7 |
| 20 | mineure | P11 : « Les anesthésiques locaux sont contre-indiqués si le tympan est perforé » ; P3 : « innervation sensitive multiple, ce qui explique l'intensité » | Ajouter « ou porteur d'un drain transtympanique ». Rattacher l'intensité de la douleur au périoste, non à l'innervation. | S7 |
| 21 | mineure | P12 : « range les piles bouton hors de portée des enfants » ; « ne reçoit plus de préparation qui en contient » | Présenter ces mesures comme des déductions. Préciser que Panotile contient de la néomycine. Ajouter « conduit gardé sec, séché au sèche-cheveux ». | S8, S7, AIPS 31957 |
| 22 | mineure | P11, tableau « À prévoir » : « DX.3 Otite moyenne chronique », « DX.7 Perforation traumatique », « DX.10 Fuite de liquide cérébrospinal » ; DX.4–DX.6 absents | Reprendre les titres exacts de la liste gelée et compléter les trois lignes manquantes. | LISTE_DX_CANONIQUE |
| 23 | mineure | P2 : « 8,6 chirurgies pour 100 000 » | La source parle d'« admissions chirurgicales ». S15 manque au corpus local : l'ajouter à `dl24/`. | S16, S15 |

Aucune source exclusivement américaine ne sert d'appui. Numéros Swissmedic 31957 et 54807, ainsi que leurs dates (mars 2021, mars 2024), sont conformes aux AIPS lues.

**Question finale : non.** Il manque 11.A–D (situations spéciales, surveillance, critères de sortie), les doses AIPS, les contre-indications AIPS complètes et la correction des défauts n° 2 à 12.
