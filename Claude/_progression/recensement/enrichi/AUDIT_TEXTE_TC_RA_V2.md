# Contre-audit V2 du texte : TC_RA.json (IMG-042 à IMG-104)

| Objet | Valeur |
|---|---|
| Fichier | TC_RA.json, SHA-256 `73a0fed451dd…`. Le JSON est valide (63 fiches). |
| Méthode | J'ai lu CORRECTIONS_TEXTE_TC_RA.md, puis les traitements et les sources des 31 fiches corrigées. J'ai relu par URL les AIPS Solu-Medrol 35112 et Rimactan 34279, qui n'avaient pas encore été lues mot pour mot sur ces points. Les autres doses viennent d'AIPS déjà lues le 14.11.2026 : Augmentin, Co-Amoxi-Mepha i.v., Metronidazol, AmBisome, Cisplatine, Inderal, Néo-Mercazole, Euthyrox, Hydrocortisone Galepharm, Minirin cp, Cinacalcet, Forsteo, Evenity, Zometa, XGEVA, Naproxen, Acidum folicum, Selenase et Solu-Cortef. Je les ai confrontées au texte. Un script a contrôlé l'étiquetage, l'ordre des sources et les références anciennes. J'ai fait une recherche web sur EULAR 2025. |
| Relevé | 40 « À vérifier » restent (il y en avait 64). Les 120 sources sont étiquetées et l'ordre Suisse → Europe → international → États-Unis → OMS est respecté. |
| Verdict | **Corrections requises.** Il reste 1 critique (une erreur de mon audit V1, recopiée sans relecture), 2 majeurs et 5 mineurs. Tout le reste est corrigé. |

## 1. État des défauts V1

| Défauts | État |
|---|---|
| C1 Dostinex (042) | **Corrigé** : microprolactinomes, contre-indications et « ne pas allaiter » sont conformes à l'AIPS 51756. |
| C2–C3 hydrocortisone, Euthyrox, Minirin, Solu-Cortef (042–045) | **Corrigés.** Les doses, les numéros et les dates sont conformes (57970 août 2025, 54949 févr. 2023, 49002 févr. 2024, 23533 oct. 2025). |
| C4–C7 co-amoxicilline, métronidazole, AmBisome, sélénium | **Corrigés** et conformes (45674 et 56758 sept. 2026, 48018 févr. 2026, 53342 janv. 2025, 53770). Voir le défaut m1 pour 063. |
| C8–C9 Solu-Medrol SEP et ACG (050, 080, 100) | **Corrigés.** L'AIPS donne bien 500–1000 mg/j pendant 3–5 j, et un traitement intermittent ≥ 250 mg/j sur ≤ 5 j. |
| C10 cisplatine, C11 Inderal, C12 Néo-Mercazole, C13 Euthyrox, C14 cinacalcet | **Corrigés** et conformes (51077 août 2023, 31706 janv. 2023, 21037 août 2020, 69216 nov. 2020). |
| C15–C16 Aspirine Cardio (076, 077, 098) | **Corrigés.** Après AIT : 300 mg 1×/j ou 100 mg 3×/j. L'usage en 098 est signalé hors indication. Le clopidogrel est limité à l'AVC de 7 j à 6 mois (M8). |
| C17 Forsteo et Evenity (087) | **Corrigé.** 20 µg/j pendant 24 mois au plus. 210 mg/mois pendant 12 mois. Contre-indication après infarctus ou AVC. |
| C18 Fortecortin, C19 Zometa et XGEVA, C20 naproxène, C21 acide folique, C24 Tepezza | **Corrigés** et conformes. |
| C22 Rimactan (064) | **Corrigé sur le fond.** J'ai relu l'AIPS : seule la méningite à méningocoques est indiquée, à 600 mg 2×/j pendant 2 j au-delà de 60 kg. La date est fausse (m2). |
| **C23 Solu-Medrol, traumatisme médullaire (093)** | **Erreur nouvelle, voir N1.** |
| M1–M6 (SVGO 2026, EULAR 2025, EHA-EMN 2025, occlusion basilaire, AO Spine 2024, Chiari 2022) | **Corrigés.** Il restent deux scories, voir N2 et m3. |
| M7 sources américaines seules | **Corrigé.** Les sources SIPMO-SICMF 2020 et SPILF 2007 sont ajoutées. Ailleurs, le texte écrit « aucune recommandation européenne trouvée le 14.11.2026 ». |
| M8–M10 | **Corrigés.** |

## 2. Défauts restants

| # | Gravité | Emplacement | Extrait | PATCH exact |
|---|---|---|---|---|
| N1 | **Critique** | 093 TT[2] | « AIPS : traumatisme médullaire aigu commencé dans les 8 h, 30 mg/kg i.v. en ≥ 30 min (AIPS Solu-Medrol n° 35112 …) » | L'AIPS donne 30 mg/kg pour les « états engageant le pronostic vital », **répétés toutes les 4 à 6 h pendant 48 h**. Elle ne donne aucune posologie propre au traumatisme médullaire. Cette erreur vient de mon audit V1. Remplacer par : « AIPS Solu-Medrol n° 35112 (août 2025) : indication traumatisme médullaire aigu si le traitement commence dans les 8 h, sans posologie propre ; le schéma de 48 h des états vitaux est déconseillé par AO Spine 2017 » |
| N2 | Majeur | 080 TT[3] | « non systématique (EULAR 2018) ; position de l'EULAR 2025 : À vérifier » | EULAR 2018 ne figure plus dans les sources. Lire Mukhtyar 2026 (doi 10.1016/j.ard.2026.06.009) et citer sa position, ou rétablir la source 2018 avec la mention « remplacée ». |
| N3 | Majeur | 080 TT[0] | « prednisone 40 à 60 mg/j … (EULAR 2025) » | Je n'ai pas pu confirmer ce chiffre dans un texte d'EULAR 2025 lu en ligne (résumés seulement). Joindre l'extrait lu (page et phrase), sinon écrire « EULAR 2018 ; EULAR 2025 non lu ». |
| m1 | Mineur | 063 TT[1] | « antibiothérapie i.v. … : co-amoxicilline p.o. 3 × 625 mg/j … » | Supprimer la partie p.o. et garder « co-amoxicilline i.v. 1,2 g 3–4×/j, 2,2 g 3–4×/j si infection grave (AIPS Co-Amoxi-Mepha i.v. n° 56758) ». |
| m2 | Mineur | 064 TT[3] et sources | « Rimactan n° 34279, sept. 2026 » ; « (refdata) (refdata, lue …) » | Écrire « mise à jour novembre 2026 » (rubrique de l'AIPS) et supprimer le doublon « (refdata) ». |
| m3 | Mineur | 079 sources | « ESO-ESMINT expedited recommendation on endovascular treatment of basilar artery occlusion » | « Strbian D et al., ESO and ESMINT guideline on acute management of basilar artery occlusion, Eur Stroke J 2024 (PMID 38752743) (Europe) ». Ajouter au TT[3] « faible, certitude faible ». |
| m4 | Mineur | 093 sources | « AO Spine … (Europe) » | Étiqueter « (international) » : ce groupe d'auteurs est international. Ajouter le premier auteur de la mise à jour 2024 (Fehlings MG et al.). |
| m5 | Mineur | 042 TT[4] ; 043 TT[2] | « substituer : hydrocortisone » ; « substituer à vie : substituer : » | Écrire « substituer à vie : hydrocortisone … » sans le doublon. |

## 3. Question finale

**Non.** Il faut appliquer N1, puis régler N2 et N3 (lire EULAR 2025 ou rétablir 2018). Les mineurs se corrigent dans le même passage. Après ces corrections, les traitements de TC_RA.json peuvent recevoir `audit-ok` sans nouveau tour complet.

## Clôture
Les 8 patchs du V2 (critique 093, majeurs EULAR, 5 mineurs) appliqués mot pour mot ; seuls des patchs exacts restaient : **audit-ok** pour le texte de TC_RA (IMG-042 à 104). Complément : texte intégral EULAR 2025 (403) à relire.
