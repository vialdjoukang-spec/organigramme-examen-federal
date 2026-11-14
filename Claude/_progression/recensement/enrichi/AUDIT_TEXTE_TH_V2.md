# Contre-audit médical V2 : texte de TH.json (IMG-105 à IMG-165)

Auditeur indépendant, 14.11.2026. J'ai lu CORRECTIONS_TEXTE_TH.md, puis le texte (gold, premiere_intention, traitement, sources) des 26 entrées visées. J'ai aussi relevé par script tous les « À vérifier » restants des 61 entrées.

**Sources relues moi-même**
- **ESC 2025, myocardite et péricardite** : PDF intégral (Schulz-Menger J et al., Eur Heart J 2025;46(40):3952–4041, doi 10.1093/eurheartj/ehaf192). J'ai lu le tableau 13 et le tableau de recommandations 26.
- **ESC 2026, insuffisance cardiaque** : texte OUP (Køber L et al., Eur Heart J 2026;47(38):5346–5457, doi 10.1093/eurheartj/ehag100, PMID 42661420). J'ai lu le tableau 11 et les recommandations sur les ARM. Le texte HTML ne donne ni la dose i.v. de diurétique de l'anse ni le seuil des dérivés nitrés.
- **AIPS** : les AIPS lues au tour 1 restent valables. J'ai relu l'AIPS Bisoprolol Spirig HC 70190 (titration dans l'insuffisance cardiaque).

## 1. Défauts du tour 1 : état

| Défaut | État |
|---|---|
| 14 critiques : 145 Floxapen, 105, 109, 117, 121, 126, 130, 125, 144, 158, 136, 116, 114, 135 | **Corrigés.** Les doses, numéros et dates sont conformes aux AIPS lues (Floxapen 12 g/j, 2 g au plus par perfusion ; Tamiflu 5 j ; Dexamethason 6 mg ≤ 10 j ; Trikafta ; Tavneos 30 mg 2×/j ; Adempas 2,5 mg 3×/j ; Peyona 20 puis 5 mg/kg ; Clexane 1 mg/kg 2×/j ; Efient 60/10/5 mg ; Actemra 162 mg toutes les 2 semaines ou 1×/semaine ; Solu-Medrol ; Opdivo 3 mg/kg + Yervoy 1 mg/kg, restriction PD-L1 ; Ofev ; Prolastin-C 60 mg/kg ; tranexamique). |
| Majeurs : Aldactone/Inspra (149), Bactrim/EACS (107), GOLD 2026 (114), ERS 2025 (117), ESC/EACTS 2025 (148), 131, 158 gold, 119, 127, 163 | **Corrigés.** 107 est conforme à l'AIPS 48306 et à EACS. 148 donne la classe I à ≥ 70 ans avec valve tricuspide. 163 est maintenant un « À vérifier » honnête. |
| 146 doses de péricardite | **Incomplet** (voir N2). |
| 122/149 doses ESC 2026 | **Partiellement exact** (voir N3 et N4). |

## 2. Défauts restants ou nouveaux

| Gravité | Id · champ | Extrait actuel | Patch exact | Preuve lue |
|---|---|---|---|---|
| **Critique** N1 | 149 traitement[2] | « bêtabloquant (bisoprolol, titration AIPS À vérifier) » | « bêtabloquant : bisoprolol 1,25 mg/j, augmenté par paliers (2,5 ; 3,75 ; 5 ; 7,5 mg) jusqu'à 10 mg/j dès la 12e semaine, chez le patient stable (AIPS Bisoprolol Spirig HC® 70190, déc. 2020 ; ESC 2026 : 1,25 → 10 mg/j) ». Ajouter la source « AIPS Bisoprolol Spirig HC® (n° 70190, mise à jour décembre 2020) ». | AIPS 70190 : « 1re semaine: 1.25 mg … Dès la 12e semaine: 10 mg ». Tableau 11 de l'ESC 2026. Je n'avais pas relevé ce défaut au tour 1 : l'erreur est la mienne. |
| **Majeur** N2 | 146 traitement[0] et sources | « AAS 750–1000 mg ou ibuprofène 600 mg toutes les 8 h (ESC, doses à relire dans ESC 2025 …) + colchicine 3 mois » | « péricardite : AAS 750–1000 mg 3×/j ou ibuprofène 600–800 mg 3×/j pendant 1–2 semaines, puis décroissance (AAS : −250 mg ; ibuprofène : −200 mg toutes les 1–2 semaines), avec un IPP ; colchicine 0,5 mg 1×/j si < 70 kg ou insuffisance rénale sévère, sinon 0,5 mg 2×/j, pendant ≥ 3 mois (ESC 2025, classe I) ; AAS et ibuprofène hors indication de l'AIPS Aspirine® 49526 ; aucune AIPS suisse de colchicine au corpus du 08.10.2026 ». Source : « Schulz-Menger J et al., 2025 ESC Guidelines for the management of myocarditis and pericarditis, Eur Heart J 2025;46:3952–4041 (source européenne) ». | Tableau 13 de l'ESC 2025 |
| **Majeur** N3 | 147 traitement[1] ; 146 traitement[1] | « contre-indique le sport de compétition 3–6 mois (ESC 2025) » | « suspend l'activité physique jusqu'à la rémission, pendant au moins 1 mois, selon une approche individualisée (ESC 2025, classe I) ». En 146 : « suspend le sport jusqu'à la rémission, au moins 1 mois (ESC 2025) ». Dans les sources de 147, remplacer « (À vérifier) » par la référence complète de N2. | Tableau 26 de l'ESC 2025 : « Restriction of physical exercise until remission, for at least 1 month … I C ». La durée de 3–6 mois n'est pas celle de l'ESC 2025. |
| **Majeur** N4 | 122 traitement[1] | « dose ≥ dose orale habituelle chez le patient déjà traité (ESC 2026) » | Supprimer « (ESC 2026) ». Écrire : « 40 mg i.v., répétable à 20 min, ≤ 4 mg/min (AIPS Lasix® 30630) ; chez le patient déjà traité, dose i.v. d'au moins la dose orale habituelle (à relire dans la section 6.1.3.1 de l'ESC 2026) ». | Le texte lu de l'ESC 2026 ne donne pas de dose i.v. Attribuer ce chiffre à l'ESC 2026 serait inventer. |
| Mineur | 149 traitement[3] | « spironolactone 25–50 mg/j (ESC) » | « spironolactone 12,5–25 mg/j, cible 50 mg/j (ESC 2026, tableau 11 ; ARM classe I, A) » | ESC 2026 |
| Mineur | 118 sources | « (n° 29349, mise à jour 2026) » | « (n° 29349, mise à jour juin 2026) » | AIPS 29349 |
| Mineur | 108 traitement[0] ; 154 traitement[2] | « co-amoxicilline i.v. puis p.o. … (AIPS) » cite l'AIPS orale ; « esmolol (AIPS) » sans numéro | Citer l'AIPS i.v. « Co-Amoxi-Mepha® i.v. (n° 56758) » ; « esmolol (AIPS Esmolol OrPha® 57413) » | Corpus refdata |

**« À vérifier » restants acceptés comme compléments** (aucune AIPS en cause, ou AIPS absente du corpus) : 163 antibiotique oral de la mastite ; références ERS (108, 120, 131), EUSOBI (162), ERC PLS final (131) ; 111, 113, 120 (corticoïdes ou molécules non nommés) ; 128, 132, 133, 135, 150, 155, 156, 164 (seuils de recommandations, pas de doses AIPS).

**Erreur nouvelle introduite par le correcteur** : N3 (attribution erronée à l'ESC 2025) et N4 (chiffre attribué à l'ESC 2026 sans lecture). Aucune dose AIPS fausse n'a été introduite.

## 3. Verdict

**corrections requises** : 1 critique (N1) et 3 majeurs (N2–N4), tous corrigeables mot pour mot par les patchs ci-dessus. Une fois ces quatre patchs et les trois mineurs appliqués, TH peut recevoir « audit-ok » sans nouveau tour.
