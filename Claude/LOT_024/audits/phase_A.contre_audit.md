# Contre-audit — LOT_024 Phase A (S1.8, écoulement auriculaire), après corrections

| Élément | Valeur |
|---|---|
| Fichier | `LOT_024_Phase_A_V0.html`, 88 783 octets, SHA-256 `86ada1fc0fdf9fd0…` ; cours non modifié |
| Date | 12.11.2026, contre-auditeur Claude (sous-agent) |
| Harnais | `verifier` : NON CONFORME (critique : image `images/…webp` et script `../_polices/forme.js` externes ; avertissement : mention « non validé cliniquement » absente). Contrôles non refaits |
| Lu | Points 2, 3, 4, 8–12 (extraction) ; `dl24/` : SSI 2406, HUG ×4, ENT UK, Wiegand 2019, résumés PubMed ; `aips24/` : Panotile 31957 (mars 2021), Ciproxin HC 54807 (mars 2024), Amoxi-Mepha 44911/49929 (sept. 2026) |
| Calculs (Python) | 1 405/123 = × 11,4 (+1 042 %) ; SSI enfant 25 mg/kg/12 h = 50 mg/kg/j ; SSI adulte 1 g/8 h = 3 000 mg/j |

## Suivi des 23 corrections de l'audit A

| N° | Statut | Constat dans le fichier actuel |
|---|---|---|
| 1 | partielle | 11.A–D créés ; doses et grossesse/allaitement ajoutées. 11.C ne donne aucun critère de sortie explicite ; erreurs nouvelles C1, G1, G2 |
| 2, 3, 4 | corrigées | Critère AIPS de perforation ; CI Panotile complète ; CI Ciproxin HC (fongique, otite moyenne) |
| 5 | corrigée | Chirurgie limitée à la série hongroise S14 ; E1 sans « chirurgie » |
| 6 | équivalente | Affirmation sur l'ofloxacine retirée |
| 7 | corrigée | « multipliée par 11 » |
| 8 | partielle | Antifongiques locaux dits « hors AIPS » ; fluconazole et itraconazole sans AIPS ni « À vérifier (AIPS) » |
| 9, 12, 13, 15–20, 22 | corrigées | Conformes aux sources |
| 10 | corrigée | Biopsie ajoutée ; « toujours » de S7 omis (L1) |
| 11 | corrigée | Pile bouton « Avant tout » dans l'arbre ; P4 la classe hors rang (équivalent) |
| 14 | corrigée | OMA « rare chez l'adulte » (S3) ; S15 toujours absent du corpus local |
| 21 | partielle | « Par déduction » et Panotile/néomycine ajoutés ; « conduit gardé sec, séché au sèche-cheveux » (S7) absent |
| 23 | partielle | « admissions chirurgicales » corrigé ; S15 non déposé dans `dl24/` |

## Suivi de l'audit B

| N° | Statut | Constat |
|---|---|---|
| 1, 2 | non corrigées | Harnais toujours NON CONFORME (ressources externes, mention absente) |
| 3 | non corrigée | P14 : insecte vivant renvoie encore au « (point 6) » |
| 4 | partielle | SSI et TEP développés ; « AIPS » paraît au sommaire avant son développement (point 6) |
| 5 | corrigée | Phrase du P4 scindée |
| 6 | partielle | P9 « L'imagerie, complétée… » : 33 mots |
| 7, 8, 9 | non corrigées | 1 seul « Interprétation » sur 7 tableaux ; repère 2 encore à (423,319) ; « 48 à 72 » 7 fois |

## Erreurs restantes ou créées par les corrections

| N° | Classe | Emplacement, extrait | Correction | Source |
|---|---|---|---|---|
| C1 | Critique | P11 fenêtre « Situations spéciales » : « l'AIPS d'Amoxi-Mepha… déconseille l'allaitement » | Texte adouci. Écrire : « ne doit pas être administrée pendant l'allaitement ; sinon, sevrer l'enfant ». | AIPS 44911 |
| G1 | Grave | P11 « OMA perforée » : « la SSI propose 25 mg/kg toutes les 12 heures » (sans durée) | Ajouter la durée SSI de l'OMA perforée de l'enfant : 10 jours. | SSI 2406 |
| G2 | Grave | P11 : amoxicilline prescrite sans contre-indication ni alternative | Ajouter les CI AIPS : hypersensibilité aux pénicillines ou céphalosporines ; prudence en cas de mononucléose ou leucémie lymphoïde. Ajouter les alternatives SSI : céfuroxime 15 mg/kg/12 h (adulte 500 mg/12 h) ; clarithromycine 7,5 mg/kg/12 h (adulte cotrimoxazole 160/800 mg/12 h). Marquer « À vérifier (AIPS) » leurs doses hors corpus. | AIPS 44911 ; SSI 2406 |
| M1 | Moyen | « Chez l'enfant… sans dépasser 10 jours de traitement » | La limite de 10 jours vaut pour tous les âges. La déplacer après les doses adulte et enfant. | AIPS 31957 |
| M2 | Moyen | « fluconazole ou l'itraconazole » | Marquer « À vérifier (AIPS) » ; aucune AIPS lue. | Prompt V0 §13 |
| M3 | Moyen | 11.C « Surveillance et critères de sortie » | Énoncer un critère de sortie (ex. : avis ORL obtenu, douleur contrôlée, plan de contrôle à 48–72 h) tiré d'une source lue. | Prompt V0 §9 |
| M4 | Moyen | P12 : mesure de S7 absente | Ajouter : « garder le conduit sec, le sécher au sèche-cheveux après l'eau ». | S7 |
| M5 | Moyen | P2 « presque inexistante dans une série finlandaise S15 » | Déposer S15 dans `dl24/`, sinon retirer. | S15 |
| L1 | Léger | P9 : « Une biopsie s'impose pour exclure… » | Écrire « s'impose toujours ». | S7 |
| L2 | Léger | 11.A « forme nécrosante en heures » ; fenêtre « Heures à jours » | Aligner sur « heures à jours ». | S7, S12 |
| L3 | Léger | CI Ciproxin HC : « infection fongique du conduit » ; hypersensibilité omise (Ciproxin HC, Panotile) | Écrire « infections fongiques » ; ajouter l'hypersensibilité aux quinolones ou aux composants. | AIPS 54807, 31957 |

Contrôles conformes : doses Ciproxin HC (3 gouttes 2×/j, 7 j, dès 2 ans, test de sensibilité préalable) et Panotile (adulte 4–5 gouttes 2–4×/j ; enfant 2–3 gouttes 3–4×/j) ; grossesse et allaitement Ciproxin HC et Panotile ; dose adulte SSI (3 000 mg/j) dans la fourchette AIPS 1 500–3 000 mg/j ; divergence de rythme pédiatrique signalée ; numéros et dates Swissmedic conformes. Aucune source américaine exclusive ; S16 est australienne, signalée comme telle. SSI 2406 valable jusqu'au 15.12.2026 : relire après cette date.

## Score §12.2 (points audités)

| Point | Note | Raison |
|---|---|---|
| 2 | 2 | Chiffres conformes ; S15 à déposer (M5) |
| 3, 4, 8, 9, 10 | 2 chacun | Conformes aux sources lues |
| 11 | 1 | C1, G1, G2, M1–M3 |
| 12 | 1 | Mesure S7 omise (M4) |
| **Total** | **14/16 = 87,5 %** | < 90 %, un Critique ouvert |

**Verdict : CORRECTIONS.** **Question finale : non.** Il manque C1, G1, G2, M1–M5 et les points B 1, 2, 3, 7, 8, 9.
