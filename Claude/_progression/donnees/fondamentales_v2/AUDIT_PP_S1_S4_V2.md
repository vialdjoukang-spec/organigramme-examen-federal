# Contre-audit — PP-S1 à PP-S4, version corrigée (commit 395a93b78, 185 affections)

Auditeur indépendant, 14.11.2026. Skills `medecin-expert` et `expert-web` appliqués.

**Méthode :**
- Lecture de `CORRECTIONS_PP_S1_S4.md`.
- Extraction, par comparaison avec `395a93b78^`, des 43 affections nouvelles ou renommées : 42 ajouts et le pneumothorax traumatique renommé.
- Relecture champ par champ de chaque défaut de l'audit V1.
- Résolution par script de tous les renvois (SY, S, EX, IMG, PP, LOT), avec vérification du `diagnostic` de chaque IMG et du `CATALOGUE_248.csv`.
- Recherche de doses.
- Recherche des molécules nouvelles dans le corpus AIPS local.
- Une recherche web : la référence Swiss Stroke Society 2021 existe, avec ce DOI et cette URL MDPI.

Par ordre du coordinateur, le schéma JSON ne compte plus comme défaut. Aucun fichier modifié hors ce rapport ; ni commit ni push.

## 1. Défauts bloquants de l'audit V1 : tous corrigés

| # | Vérifié dans | État |
|---|---|---|
| E1 | PP-S2-I `affections[3].mecanisme[2]` | Corrigé : le texte distingue le RAA (mimétisme moléculaire) de la GNA (complexes immuns) et précise que la pénicilline ne prévient pas la GNA. |
| E2 | PP-S1-A, myasthénie, `mecanisme[0]` | Corrigé : IgG1-3 activent le complément ; les anti-MuSK (IgG4) ne l'activent pas. |
| E3, E4 | PP-S3-V, TVP et EP | Corrigé : espace mort et effet shunt ; « probabilité non élevée » concorde désormais avec « faible ou intermédiaire ». |
| E5 | PP-S4-D et PP-S4-Tr | Corrigé : le pneumothorax spontané passe en D ; Tr garde les formes traumatique et compressive. |
| E6 à E11, renvois IMG et EX | Fiches concernées | Corrigés ; IMG-063, IMG-151 (Fallot), IMG-084 (SLA) et le panel d'expansions de la NF sont retirés. |
| M1 à M5 | S3-V, S3-D, S3-F, S3-C, S4-V, S4-F, S2-D, S2-V, S1-V | Présents : SCC, insuffisance mitrale, troubles de conduction, réentrées, TV et FV, Brugada, SDRA, épanchement pleural, décollement de rétine, rétinopathies diabétique et hypertensive, dissection cervicale. |
| S1, S2 | 36 fiches, `sources` | Corrigés : BTF et ATLS portent l'étiquette « source américaine, hors hiérarchie » ; les fiches internes portent la mention « lues par leurs rédacteurs, non relues ici » ; aucune source n'est marquée « lu ». |
| Doses | 36 fiches | Aucune dose ; les qualificatifs « forte dose » et « dose minimale » ont disparu. Restent « dose cumulée » (mécanisme toxique) et « TDM à faible dose » (technique), qui sont acceptables. |
| Renvois | 36 fiches | 100 % des renvois sont résolus. Les LOT cités existent dans le catalogue et sont pertinents, par exemple S1-V vers LOT_102 « Parésie » et S3-F vers LOT_148 « Syncope ». |

## 2. Audit des 42 affections ajoutées : 37 sont exactes, 5 sont à retoucher

Ces 37 affections sont exactes, et le contrôle porte sur des points précis : NMOSD et MOGAD (AQP4, complément, risque des traitements de la SEP) ; névrite optique (corticoïdes sans gain final) ; HINTS de profil périphérique ; Weber latéralisé du côté sain ; otospongiose (réflexe stapédien aboli) ; base contre acide dans la brûlure chimique ; Brugada (V1-V2 en dôme, fièvre) ; TGV (cœur en œuf, PGE1, Rashkind) ; WPW (on évite les freinateurs du nœud) ; digoxine (Na/K-ATPase, kaliémie, DigiFab présent dans le corpus) ; membranes hyalines ; Bochdalek (on évite le masque) ; pneumoconioses ; critères de Light ; pneumocystose ; corps étranger dans la bronche droite ; SDRA (PaO2/FiO2, décubitus ventral). Isuprel, Enspryng, Uplizna, Soliris et Bactrim figurent dans le corpus AIPS local.

| # | Gravité | Emplacement | Extrait | PATCH exact |
|---|---|---|---|---|
| N1 | Moyen | PP-S1-Tr `affections[4].consequence_clinique` | « Un déficit des membres inférieurs s'associe à une anesthésie en selle, à une rétention urinaire et à une perte du tonus anal. » Ce texte ne décrit que la queue de cheval. | « La compression de la moelle donne un niveau sensitif, un syndrome pyramidal et des troubles sphinctériens ; la queue de cheval donne un déficit flasque des membres inférieurs, une anesthésie en selle, une rétention urinaire et une perte du tonus anal. » |
| N2 | Léger | PP-S1-Tr `affections[4]` (classement) | La fiche classe métastase et hernie discale en « Traumatique ». | Ajouter à `honnetete` : « Compression médullaire classée en Tr par regroupement ; ses causes sont aussi tumorales (PP-S9-T) et dégénératives (PP-S9-D). » |
| N3 | Léger | PP-S3-F `affections[5].cibles_therapeutiques[0].pourquoi` | « Elle resynchronise le myocarde. » | « Elle dépolarise en même temps tout le myocarde, ce qui laisse le nœud sinusal reprendre la commande ; une TV avec pouls relève d'une cardioversion synchronisée. » |
| N4 | Léger | PP-S1-T `affections[3].consequence_clinique` | « ou une uvéite » | « ou une uvéite postérieure (lymphome vitréo-rétinien associé) » |
| N5 | Léger | PP-S2-I `affections[8].examens` ; PP-S3-A `affections[3].examens` ; PP-S2-D `affections[5].examens` | Les listes sont vides alors que le texte nomme la TDM cervicale, l'angio-IRM ou le fond d'œil. | Ajouter `{"id":"EX-2-S2-echographie-irm-cervico-faciales"}` pour Ludwig ; ajouter l'EX d'angio-TDM ou d'angio-IRM aortique pour Takayasu ; ajouter un EX d'échographie oculaire, s'il existe, pour le décollement. |

## 3. Défaut nouveau introduit par la correction

| # | Gravité | Emplacement | Défaut | PATCH exact |
|---|---|---|---|---|
| S10 | Moyen | 27 fiches, `sources` | Le correcteur a recréé le défaut S4 de l'audit V1 (source copiée hors sujet). Michel P et al. (revascularisation de l'AVC ischémique) figure dans les 9 fiches PP-S1, y compris A, C, D, F, I, Ia, T et Tr. Les recommandations de la Swiss Society of Hypertension figurent dans les 9 fiches PP-S3, dont Tr, Ia et C. Barben et Rueegg (dépistage de la mucoviscidose) ainsi que SSP BPCO et asthme 2018 figurent dans les 9 fiches PP-S4, dont Tr, T, I et V. | Michel P : garder la source en PP-S1-V seulement. SSH : garder la source en PP-S3-F seulement (en S3-V si l'on veut). Barben et Rueegg : garder la source en PP-S4-C seulement. SSP BPCO et asthme : garder la source en PP-S4-A et PP-S4-D seulement. Supprimer ces chaînes partout ailleurs. Une copie en libre accès de Michel 2021 existe sur archive-ouverte.unige.ch (unige:152319) : la lire permettrait de passer le statut à « lu ». |

## 4. Réponse sur S5 : bloquant ou complément ?

**C'est un complément, pas un blocage.** Les fiches PP ne contiennent ni dose ni seuil décisionnel suisse ; leurs mécanismes relèvent de la physiopathologie classique. Chaque référence porte la mention « non lu » ou « À vérifier », et aucune ne prétend avoir été lue. Les affirmations qui dépendent de la Suisse portent toutes une réserve : plan de vaccination contre la FSME, dépistage de la mucoviscidose, SUVA, dépistage par TDM. Ces mentions honnêtes satisfont la règle « sinon À vérifier ».

Deux conditions s'appliquent : corriger S10, car une source hors sujet est une fausse caution même lorsqu'elle porte la mention « non lu » ; ne jamais passer une source à « lu » sans lecture datée.

À lister en compléments :
- Lire Michel 2021 sur UNIGE.
- Lire SSP BPCO et asthme 2018.
- Chercher les recommandations de la SOG/SSO et de la SSORL pour S2, car aucune source suisse n'y figure.
- Couvrir les sept IMG restants : 005, 007, 018, 098, 119, 128 et 139.

## 5. Verdict

| Critère | Note | Raison |
|---|---|---|
| Exactitude des chaînes | 2 | Les défauts E1 à E11 sont corrigés ; les ajouts sont justes, à part N1. |
| Exhaustivité | 2 | Les défauts M1 à M9 sont traités ; il reste sept IMG mineurs en complément. |
| Classement VITE DIT CAFé | 1 | La compression médullaire est classée en Tr (N2) ; la névrite vestibulaire est classée en F alors que son origine est probablement virale (acceptable). |
| Sources et honnêteté | 1 | Les étiquettes sont honnêtes, mais 27 fiches portent une source copiée hors sujet (S10) et aucune source n'a été lue. |
| Renvois et passerelles | 2 | 100 % des renvois sont résolus ; les LOT et les passerelles PP ↔ PP sont pertinents ; les doublons passent en forme courte. |
| Aucune dose, style | 2 | Aucune dose ; les phrases sont verbales. |

**Prêt pour `audit-ok` : oui, sous condition.** Les patchs S10 et N1 suffisent (opération de suppression et une phrase) ; N2 à N5 et les compléments de S5 peuvent suivre. Sans S10 et N1 : non.

Source web : [Michel P et al., Clin Transl Neurosci 2021 (MDPI)](https://www.mdpi.com/2514-183X/5/1/9) ; [copie UNIGE](https://archive-ouverte.unige.ch/unige:152319).

## Clôture
S10 et N1 appliqués mot pour mot (tour 2 du correcteur), N2–N4 faits ; N5 partiel (aucune fiche d'échographie oculaire dans le dépôt) listé en compléments, comme l'absence de recommandation suisse lue en entier : **audit-ok** pour PP-S1 à S4, conformément au verdict « oui si les deux patchs sont appliqués ». La Physiopathologie complète (108 fiches) est audit-ok.
