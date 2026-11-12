# LOT_018 — corrections de l'audit 1 (A et B), 11.11.2026

Base : 4369ce2. Chaque défaut a été vérifié dans le fichier, puis dans la source réelle : AIPS refdata relues pour Actemra 58868, RINVOQ 67257, Prednisone Streuli 29349, Actilyse 48313, Metalyse 69958, Aspirine Cardio 51795, Eylea 62393, Alphagan 54605 et Diamox 21191, et PDF de Steffen & Tabibian (Rev Med Suisse 2015).

## audit1_A

| # | Fichier | Défaut | Décision | Motif |
|---|---|---|---|---|
| A0 | Phase A | Point 1 contenait le premier geste d'anamnèse | Appliqué | Le point 1 est la définition seule (L1-3). La phrase devient « Elle touche un œil ou les deux… ». |
| A1 | Phase A | La fenêtre f-a-semantique devenait orpheline | Appliqué | La fenêtre est rattachée au point 5 (« le médecin précise ce qu'il entend par perte de vision »). |
| A2 | Phase A | Formule de fabrication (« ne justifie pas d'en inventer un ») | Appliqué | La phrase est retirée. |
| A3 | Phase A | Formule de fabrication au point 12 | Appliqué | La phrase renvoie au point 12 de DX.4 (HUG : 3, 2 puis 1 an) et de DX.5, avec des liens vérifiés (#dx4-p12, #dx5-p12). |
| A4 | Phase A | Phrase sur la fabrication des questions du point 14 | Appliqué | La phrase est retirée. |
| A5 | Phase A | Fiche acétazolamide : « aucune dose pédiatrique n'est extrapolée » | Appliqué | Diamox 21191 indique « l'administration chez les enfants et les adolescents n'a pas été étudiée ». |
| A6 | DX.5 | Q14 Eylea : 8 semaines présenté comme un maximum définitif | Appliqué | Eylea 62393 (OMD) espace les injections à 8 semaines au maximum, puis demande de « vérifier au terme de la première année […] si les intervalles […] peuvent encore être espacés ». |
| A7 | DX.1 | Redite « amblyopie définitive après 6 ans » | Appliqué | La phrase est retirée. Le fait reste au point 3, dans la fenêtre amblyopie et au point 13. |
| A8 | DX.1 | Même redite en 11.D | Appliqué | La phrase renvoie maintenant au point 3. |
| A9 | DX.2 | Seuils d'acuité OAC en double avec DX.1 | Appliqué | La ligne renvoie à f-dx1-oac, qui porte les deux groupes et la vision monoculaire. DX.2 garde l'éblouissement, la perte récente d'un œil et la phrase sur les seuils du premier groupe propre au point 8. |
| A10 | DX.4 | Alphagan : allaitement présenté comme contre-indication | Appliqué | La rubrique Contre-indications d'Alphagan 54605 ne cite pas l'allaitement ; la rubrique Allaitement écrit « ne doit pas être utilisé pendant l'allaitement ». |
| A11 | Phase A, DX.1, DX.4, DX.5 | Tableaux qui défilent à 390 px | Non appliqué ici | Le réglage appartient à forme.css (agent designer) et non aux leçons. Il n'y a pas de débordement de page. |
| A12 | Phase A, DX.2, DX.4 | Schémas de prérequis manquants | Non appliqué | L'audit n'exige aucune correction avant le LOT_021. Ces schémas restent dans HELP.md. |

## audit1_B

| # | Fichier | Défaut | Décision | Motif |
|---|---|---|---|---|
| B0–B2 | DX.10 | #sb-s13 inexistant (inhibition de l'IL-6, CRP masquée, bilan avant tocilizumab) | Appliqué → #sb-aips-58868 [S15] | Actemra 58868 décrit les effets de l'inhibition de l'IL-6 sur la CRP. Elle ajoute « Actemra ne devrait pas être administré à des patients présentant une infection active ». |
| B3 | DX.10 | #sb-s14 inexistant (tuberculose active) | Appliqué → #sb-aips-67257 [S16] | La rubrique Contre-indications de RINVOQ 67257 mentionne les « patients atteints de tuberculose active ». |
| B4 | DX.10 | #sb-s12 inexistant (traitements à relever) | Appliqué | L'appel est retiré ; S1 suffit. |
| B5 | DX.10 | Ancre AIPS prednisone posée sur la cible EULAR 2018 | Appliqué | L'ancre est retirée et la phrase porte « hors AIPS ». L'AIPS 29349 ne contient aucune cible de décroissance pour l'ACG. |
| B6 | DX.9 | Ancre Actilyse posée sur THEIA | Appliqué | L'ancre est retirée et la phrase porte « hors AIPS ». Actilyse 48313 ne mentionne ni THEIA ni l'OACR. |
| B7 | DX.9 | Ancre Metalyse posée sur TenCRAOS | Appliqué | L'ancre est retirée et la phrase porte « hors AIPS ». Metalyse 69958 ne mentionne pas TenCRAOS. |
| B8 | DX.9 | Ancre Aspirine Cardio posée sur le bras témoin des essais | Appliqué | L'ancre est retirée et la phrase porte « hors AIPS ». |
| B9 | DX.9 | Même ancre au point 14 (dose de comparaison) | Appliqué | L'ancre est retirée. |
| B10 | DX.9 | Actilyse : contre-indication élargie à tout anticoagulant oral | Appliqué | Actilyse 48313 écrit « anticoagulants oraux (p.ex. sous antagonistes de la vitamine K avec un INR >1,3) ». |
| B11 | DX.8 | Incidence américaine présentée comme suisse | Appliqué | Le PDF de Steffen & Tabibian (RMS 2015) écrit « aux Etats-Unis […] Son incidence est estimée entre 1 et 5 / 100 000 personnes / an ». |
| B12 | DX.6 | Fiche acétazolamide en double avec la Phase A | Appliqué | Le lien renvoie à LOT_018_Phase_A_V0.html#f-a-m-acetazolamide. |
| B13 | DX.7 | Rang 🚩 E3 absent du titre | Appliqué | Le titre suit LISTE_DX_CANONIQUE.md. |
| B14 | DX.10 | Rang 🚩 E2 absent du titre | Appliqué | Le titre suit LISTE_DX_CANONIQUE.md. |
| B15 | DX.10 | Phrase de fabrication (lien vers l'urgence) | Appliqué | La phrase est réécrite selon la proposition de l'audit. |
| B16 | DX.6 | Phrase de fabrication (critères de sortie) | Appliqué | La phrase est réécrite selon la proposition de l'audit. |
| B17 | DX.8 | Phrase de fabrication (critères de sortie) | Appliqué | La phrase est réécrite selon la proposition de l'audit. |
| B18 | DX.9 | Phrase de fabrication (pronostic et sortie) | Appliqué | La phrase est réécrite selon la proposition de l'audit. |

Les doutes non bloquants de l'audit B ne sont pas traités ici : position avant chirurgie dans DX.7, fiches Solu-MEDROL répétées, EULAR 2025 lu en résumé, schémas des points 3. Ils restent ouverts dans HELP.md.

## Retraits (aucun fait unique perdu)
- **DX.6** : la fiche `.mb` f-dx6-m-acetazolamide (≈1,5 Ko) est retirée, avec l'entrée bibliographique S15 sb-aips-21191 qui n'est plus citée. Ce contenu reste en entier dans la fiche f-a-m-acetazolamide de la Phase A, plus complète. La phrase de la fiche retirée qui disait que l'acétazolamide ne remplace ni le laser ni l'avis urgent reste couverte par la note finale de la fiche de la Phase A.
- **DX.1** : une phrase sur l'amblyopie après 6 ans est retirée. Le fait reste au point 3, dans la fenêtre amblyopie et au point 13.
- **DX.2** : les valeurs d'acuité OAC sont retirées du tableau. Elles restent dans DX.1, dans f-dx1-oac.
- **Phase A** : deux phrases de fabrication sont retirées (fenêtre qui précède la fiche acétazolamide, et point 14).

## Contrôle final
- Les 11 fichiers passent `controle3 --script-ok` au VERT.
- `verif_aips` : OK partout, sans BLOQUANT. Il reste une alerte « dose_absente » dans DX.2 (AIPS 66151, 0,62 mg de phényléphrine) ; elle existait déjà et n'appartient pas à cet audit.
- Le script vérifie chaque `href="#…"` et chaque lien vers un autre fichier : 0 ancre absente (5 avant correction, toutes dans DX.10).
- Tailles en octets : Phase A 182 113 (118 Ko hors images), DX.1 91 054, DX.2 94 455, DX.3 99 479, DX.4 84 788, DX.5 108 271, DX.6 91 486, DX.7 86 611, DX.8 84 475, DX.9 95 594, DX.10 100 003. Tous les fichiers restent entre 80 et 150 Ko.
