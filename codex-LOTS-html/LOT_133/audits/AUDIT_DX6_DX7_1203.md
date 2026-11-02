# Contre-audit ciblé DX6 / DX7 · 02.11.2026

Auditeur distinct : audit_1203. Révision des trois corrections P11 DX6 et des appuis documentaires DX7 ; aucun audit clinique exhaustif, aucun score, aucune validation médicale humaine. Réserves1103 héritées sans réouverture des points résolus. Les protocoles spécialisés complets restent une extension facultative du cours adulte.

## Markdown contrôlé

- DX6 : SHA256 `7af8753ee05b8f5b5a1eebf469389f25a0838059f6d577b1c84a77cbc437dd50`.
- DX7 : SHA256 `fa6ea80ec6a97acbe318b596e3e378e20607d465295d1435c1c465fbfe932305`.
- `controler_brouillons.py` exécuté indépendamment : chacun 14 parties et14 questions, code0. Premier DX6 refusé pour titres `## **N.` ; auteur a restauré `## N.` sans modifier contrôleur. Ce contrôle est structurel seulement.

## DX6 : sources et concordance

Relecture le02.11.2026 des fichiers `dx6_0330/*_live.txt` et des extraits `pharma6_1203`, acquisition héritée02.11.2026 ; aucune nouvelle requête réseau par cet auditeur, aucune dernière version réglementaire revendiquée. Neuf SHA source/response/extrait de `evidence/PHARMA_DX6_1203.json` recalculés et concordants.

| Notice / URL documentaire | Mise à jour indiquée | SHA256 texte source | Passage relu |
|---|---|---|---|
| [Duphalac32894](https://files.refdata.ch/simis-public-prod/MedicinalDocuments/5dc918d4c0ea4013ad4633b4d6ffbf93-fr.html) | février2023 | `5f42ebdf3b6bfbb133ae35cf918e42f5da3422736388e7d48a21a9c098e3d222` | L50–68 : CI lactose puis prudence, contradiction réelle |
| [Xifaxan63216](https://files.refdata.ch/simis-public-prod/MedicinalDocuments/aa77f4ff3bb64f6e94ca973ed8d8f11f-fr.html) | avril2023 | `2b931b38fd0bbb4ef299e3d260ea0205bf2310cb2da25f448e3098d828f34ce5` | L115–126 : SJS/NET et arrêt immédiat/évaluation |
| [Rocephin44625](https://files.refdata.ch/simis-public-prod/MedicinalDocuments/8d9346c377864ce8a9b0034d146e9b2f-fr.html) | juin2025 | `48fc09cd7ee17d4ef42b9718b544b47a33f04fe30012f2e9a90cb0126b734190` | L116–119,171–174,202–207,784–785 : calcium IV, mélange/simultanéité, succession et rinçage |

Les trois corrections sont recevables. Duphalac : la seconde phrase ne lève pas la CI ; clarification préalable sans autorisation déduite. La contradiction documentaire reste ouverte. Rifaximine : SJS/NET cirrhotiques, arrêt au premier signe et évaluation concordants. Ceftriaxone : absence de mélange/dilution calcique et de simultanéité, même tubulures distinctes ; succession adulte avec rinçage ;48h réservé au nouveau-né, aucune transposition adulte. Calcium oral et voie IM distingués. C. difficile présent dans source mais hors ajout ciblé : aucune prétention de sécurité exhaustive et aucune nouvelle condition de clôture imposée.

HTML DX6 SHA256 `199b127024a1f20b5ed0d18510488143aa02cf16bf2ebac72bca5d75846907dc` : les trois passages rendus contre-lus, attribution A1/A2/A6 conservée ; concordance recevable.

## DX7 : portée réellement vérifiée

`evidence/ACTUALITE_DX7_1203.json` : dix empreintes du cache `actualite7_1203` recalculées, toutes concordantes. Les68 lignes de `S6_passages_relus.txt` correspondent exactement aux réponses sources historiques. SHA extraits `c56d1793a55ea9720699c8c0ddf3082fe19653b09e65aa4b974bd9098ad8dc83`.

Source [ACVC/ESC statement2022](https://pmc.ncbi.nlm.nih.gov/articles/PMC9020374/) datée18.01.2022, consultation/cache02.11.2026 : `escopen.json` SHA `7c131d6c0af32c65c7afa2b307c3ef020dbbfe58ed9f4c9f2d2f403acc15998d`, `escupdate_read.json` SHA `50841eb6dd13ed5986316a7529b23ad09b54b68835841086c36e19a10d91dc5b`. Relecture ciblée L277–284,293–305,412–415,437–438 : biomarqueurs selon contexte, monitorage, congestion/hypoperfusion, soutien respiratoire et vasodilatateurs. Ces passages soutiennent les reformulations P4/P6/P8/P11. Origine européenne et hébergement américain distincts ; texte intégral non revendiqué.

[HUG2022](https://www.hug.ch/sites/interhug/files/2022-12/strategies_insuffisance_cardiaque.pdf) : acquisition auteur02.11.2026 12:05UTC HTTP200, SHA PDF `945a28a1ad469ad289d79dcdfbe660cefaef16f2dd66ec0fa463fb1a6b3fc5bf`, texte `b0abaeda505fa919a0e39abc66b49f962ab2b0bf60ecbac017ce8b391572cd08`, identiques aux preuves antérieures. Portée chronique uniquement, pas actualité2026 déduite.

[S5 ESC2021](https://academic.oup.com/eurheartj/article/42/36/3599/6358045) reste403. Retrait des appuis cliniques S5 recevable ; limite d’accès demeure. [DOI signalement2026](https://doi.org/10.1093/eurheartj/ehag100) redirigé selon acquisition auteur vers page OUP403 : ce routage n’authentifie ni titre complet ni recommandations. Identité/portée non démontrées explicitement ; aucune nouvelle recommandation et aucune inexistence déduites. Réserve d’actualité maintenue. Forxiga conserve le verdict pharma1020, aucune dose réauditée ou ajoutée ici.

HTML DX7 SHA256 `82ba9c00584211bc6dfa4da60bc4f11d08578e5d71087478795e4246e1242160` : P11 aigu, réserve2026 et bibliographie S6/S7 contre-lus, S5 non cité. Chapeau générique préparatoire seulement (chapeau MD complet non reproduit), mais réserve d’identité/portée2026 bien présente P11/bibliographie. Concordance ciblée recevable. Microcorrection finale MD : préfixes L des lignes remplacés par « lignes », mêmes numéros et fond ; contrôle officiel 14/14 repassé au SHA final. L’ancien SHA des contrôles linguistiques ne constitue pas, à lui seul, une invalidation du fond.

## Réserves réelles

Aucune image clinique intégrée dans les dix HTML au contrôle mécanique présent : zéro balise img. Cette absence demeure un vrai blocage de complétude iconographique ; les captures navigateur ne le lèvent pas. Limites de fraîcheur et contradiction Duphalac maintenues. Réception des corrections préparatoires ciblées possible ; aucune clôture clinique globale du lot revendiquée.
