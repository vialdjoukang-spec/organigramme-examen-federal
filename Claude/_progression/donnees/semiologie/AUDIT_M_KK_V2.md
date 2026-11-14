# Audit V2 (tour de vérification) : M-01 à M-17 et K-01 à K-18

Version auditée : 35 JSON, 131 195 octets, SHA-256 de la concaténation `24d6707f…468b`. Date : 14.11.2026. J'ai lu `CORRECTIONS_M_KK.md` et relu chaque passage corrigé dans les fiches. Les fiches sont du JSON valide et aucun lien n'est mort (219 identifiants).

## Vérification des corrections

| # | Fiche | Statut | Contrôle fait ce jour |
|---|---|---|---|
| G1 | M-03 | **Corrigé** | J'ai vérifié chaque point dans SIRMED « Reanimation 2025 » (Wilmes, Regener ; SIRMED et SRC) : adrénaline « so früh wie möglich » en rythme non choquable, « ERC: nach dem 3. Schock » en rythme choquable, « i.v. VOR i.o. ». Les citations AIPS (n° 66396, n° 59528) restent exactes. |
| — | M-03, amiodarone | **Tranché** | Resuscitation Council UK, *Adult advanced life support Guidelines*, publiées le 27.10.2025, adaptation de l'ERC 2025 (Resuscitation 2025;215 Suppl 1:110769), texte lu : « Give amiodarone 300 mg IV … after a total of three shocks » ; « a further dose of amiodarone 150 mg IV … after a total of five shocks ». La fiche est juste ; l'étiquette « À vérifier » doit tomber (PATCH P1). |
| M1, M2 | M-14 | Corrigé | Le texte correspond à ASSM 2019, § 2.3 et § 2.4. |
| M3 | M-14, M-15, M-16, K-14 | Corrigé | Fedlex (version du 1.1.2026) : texte conforme aux art. 371 al. 1, 372, 378 al. 1, 379, 426, 429, 430 al. 2 et 5, 434 et 439 al. 2. |
| M4 | M-06 | Corrigé, **mais erreur nouvelle** | Le texte correspond à la stratégie HUG 2026 (bactériurie, p. 17 ; cystite). Erreur nouvelle : voir N1. |
| M5, M6 | M-07 | Corrigé | Le DOI et les paragraphes de la stratégie HUG Douleur aiguë 2024 sont exacts. |
| M7 | M-02 | Corrigé | Rossaint 2023, recommandations 1 à 3, lues dans Europe PMC : compression, garrot d'appoint, voies aériennes. Le rachis cervical reste honnêtement « À vérifier ». |
| M8 | K-15 | Corrigé | Conforme aux Informations MED 2026, § 5.5. |
| M9 | M-03, M-16 | Corrigé | La source est marquée « non lu, À vérifier ». La phrase « Im Zweifel reanimieren » figure bien dans SIRMED. |
| L1–L9 | — | Corrigés | La citation ASSM 2019, § 3.3 (« pas d'âge minimal légal ») est exacte. K-17 a un nouveau scénario, K-18 une demande en allemand standard, et K-01 à K-04 ont des phrases verbales. |

## Défauts restants et PATCH exacts

| # | Gravité | Emplacement | Extrait | PATCH | Source |
|---|---|---|---|---|---|
| N1 | **Moyen** (nouveau) | M-06, étape 4, `faire` 2 | « (ou d'emblée chez l'homme), nitrofurantoïne ou fosfomycine … posologie selon l'AIPS » | Ajouter : « Chez l'homme, la fosfomycine sort de l'indication AIPS (Monuril : « femmes et adolescentes >12 ans », « 3 g en dose unique ») ; le schéma HUG en deux doses est hors AIPS et doit être signalé comme tel. » | AIPS Monuril n° 49298 (nov. 2022), lue via `aips_fiche.py` ; HUG 2026 |
| P1 | Léger | M-03, étape 5, `faire` 4 et 6 ; dernière source | « (source européenne : RC UK ALS 2025, À vérifier) » ; « non relu par le rédacteur, À vérifier » | Écrire « (source européenne : Resuscitation Council UK, Adult ALS Guidelines 2025, adaptation ERC 2025 — lu le 14.11.2026) » ; pour l'auditeur : « amiodarone 300 mg après 3 chocs, 150 mg après 5 chocs ; électrodes antéro-postérieures après 3 chocs échoués ». | RC UK ALS 2025 |
| N2 | Léger | M-06, étape 4 | « triméthoprime-sulfaméthoxazole en alternative » | Écrire « … ou triméthoprime-sulfaméthoxazole en première ligne » et ajouter « chez la femme, décider avec la patiente : antibiotique de réserve ou réévaluation après 48 h d'AINS ». | HUG 2026, Traitement |
| N3 | Léger | M-06 | Durées absentes | Les durées diffèrent : la nitrofurantoïne dure 5 jours selon HUG et « 7–10 jours » selon l'AIPS Furadantine retard (n° 34921). Il faut signaler l'écart et ne pas citer de durée sans l'AIPS. | AIPS Furadantine retard ; HUG 2026 |
| N4 | Léger | M-02, étape A | « aucune source suisse ou européenne lue … À vérifier » | Conserver l'étiquette. Lire ensuite ERC 2025 *First Aid*, ou une source suisse de traumatologie, sur la restriction des mouvements du rachis. | — |

## Verdict

**Question finale : oui, sous réserve de N1.** G1 et les neuf défauts moyens sont corrigés sans erreur de fond, sauf N1, une erreur moyenne introduite par la correction M4 (fosfomycine chez l'homme hors AIPS). Après le PATCH de N1 (une phrase), le lot peut recevoir `audit-ok`. Aucun défaut critique. P1 et N2 à N4 sont légers et ne bloquent pas. Le moment de l'amiodarone est tranché : 300 mg après le 3e choc, 150 mg après le 5e (RC UK ALS 2025, adaptation ERC 2025, lu).
