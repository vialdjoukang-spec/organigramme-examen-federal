# Contre-audit des champs texte : AB.json après CORRECTIONS_TEXTE_AB.md, 14.11.2026

**Version auditée** : `enrichi/AB.json`, SHA-256 `5d72e16e91712def…`, 72 entrées ; champs texte seulement.
**Méthode (ce que j'ai fait)** :
- J'ai relu les traitements, les sources, le gold et la première intention des 29 entrées corrigées, puis les traitements de 17 autres entrées.
- J'ai extrait par script les 49 couples « AIPS n° / mise à jour ». Chacun concorde avec le corpus refdata.
- J'ai relu dans le texte AIPS en cache, par URL, chaque dose ajoutée par le correcteur :
  - Budenofalk Uno, dégression un jour sur deux ;
  - Glivec GIST, 600 à 800 mg ;
  - Imfinzi CVB, gemcitabine et cisplatine à J1 et J8 ;
  - Jinarc, paliers d'au moins une semaine ;
  - Konakion MM ;
  - Wegovy MASH ;
  - Stragen ;
  - Prednisone Streuli, indication Crohn et RCH.
- J'ai vérifié par PubMed (efetch) les volumes et pages de HerniaSurge 2023 et d'ESPR 2026.
- J'ai lu le texte intégral de l'ESVS 2025 (PDF du dépôt de Turku, 154 p.) pour les forces de recommandation.

## 1. Corrections validées

| Bloc | Résultat |
|---|---|
| C1–C17 | Les 17 sont corrigés, avec dose, n° et date exacts. La phénoxybenzamine reste « À vérifier » à bon droit, car elle est absente du corpus. |
| **Konakion (214)** | **J'accepte « 10–20 mg i.v. »**. C'est le seul chiffre de l'AIPS lié aux anticoagulants oraux : « Intoxication aiguë par des anticoagulants oraux 10-20 mg de vitamine K1 … par jour par voie i.v. ». Mon « 10 mg » de V1 venait du schéma d'intervention en urgence (phenprocoumone + CCP 60 U.I./kg), qui est moins adapté à un hématome. Seule une précision reste à ajouter (n4). |
| Stragen (M2) | Conforme : « 2.25 à 4.5 g … 3-4 fois/jour », « habituellement entre 100 et 200 mg de pipéracilline par kilogramme ». |
| Wegovy (M3) | Conforme : indication « MASH non cirrhotique … F2 à F3 », palier de 0,25 mg sur 16 semaines jusqu'à 2,4 mg/semaine. |
| M1, M4–M7, M9, M11–M13 | Conformes. Les pages EASL 2025 (82:315–374), BCLC 2025, IAP 2025 (25:770–814), ESPR 2026 (56:260–268) et BJS Open 2023 (7:zrad080) sont exactes. |
| m1–m8 | Conformes, sauf m7, appliqué partiellement (voir n3). |
| Les 13 « À vérifier » restants | Ce sont des compléments honnêtes. La force IAP 2025 reste à vérifier, car le texte intégral est payant et n'a pas été lu. |

## 2. Défauts restants ou nouveaux

| # | Grav. | Id · champ | Extrait fautif | PATCH exact | Source lue |
|---|---|---|---|---|---|
| N1 | **Majeur** (erreur nouvelle, issue de ma V1 qui s'appuyait sur une source secondaire) | 213 · T0 | « avec prothèse, de préférence laparo-endoscopique ou prépéritonéale (HerniaSurge 2018, mise à jour 2023) » | « cure chirurgicale avec prothèse (HerniaSurge 2018 : doit) ; la technique prépéritonéale ouverte est une alternative acceptable au Lichtenstein ; aucune voie prépéritonéale n'est préférée à l'autre (mise à jour HerniaSurge 2023 : faible) » | BJS Open 2023, texte intégral PMC10588975 : « preperitoneal flat mesh technique seems to be an acceptable alternative » (Weak) ; « No recommendation to advocate laparo-endoscopic … over open preperitoneal repairs » |
| N2 | **Majeur** | 193 · T0 | « (ESVS 2025 ; force à relire dans le texte intégral — À vérifier) » | « revascularisation endovasculaire en première intention si occlusion thrombotique ou embolique de l'AMS (ESVS 2025, rec. 37 : IIa B, devrait) ; revascularisation avant résection (rec. 35 : IIa C, devrait) ; résection sans rétablissement et laparotomie de second regard (rec. 40 : IIa C, devrait) » | ESVS 2025, recommandations 35, 37 et 40 (lues) |
| N3 | **Majeur** | 237 · T0 et T2 | « (ESVS 2025 ; force … — À vérifier) » ; « nutrition » | T0 : « … endovasculaire en première intention si l'anatomie s'y prête (ESVS 2025, rec. 14 : I B, doit) » ; T2 : « ne pas retarder la revascularisation pour renutrir en cas d'ischémie chronique sévère (rec. 13 : III C, ne doit pas) » | ESVS 2025, recommandations 13 et 14 (lues) |
| n1 | Mineur | 179, 199, 202, 230 · sources | « AIPS AIPS Imfinzi … » (lignes en double) | Supprimer les 4 lignes « AIPS AIPS … » | script |
| n2 | Mineur | 189 · T0 | « prednisolone … (AIPS Prednisone Streuli n° 29349, juin 2026) » | « … (AIPS Prednisolone Streuli n° 29348, juin 2026) » | corpus refdata |
| n3 | Mineur | 229 · T0, S0 | « EAU/ESPU 2025 » | « EAU/ESPU 2026 » (m7 incomplet) | — |
| n4 | Mineur | 214 · T0 | « vitamine K 10–20 mg i.v. » | « vitamine K 10–20 mg/j i.v. (« intoxication aiguë par des anticoagulants oraux ») » | AIPS Konakion MM n° 48112 |
| n5 | Mineur | 180 · sources | La source de l'AIPS Ursofalk manque. | Ajouter « AIPS Ursofalk n° 42782 (mise à jour mars 2025), refdata.ch, lue le 14.11.2026 » | corpus |

## 3. Verdict

**Corrections requises (mineures en volume)**. Il reste 3 majeurs : 1 erreur nouvelle (N1) et 2 forces ESVS désormais connues (N2, N3), ainsi que 5 mineurs. Une fois ces 8 patchs appliqués tels quels, le fichier peut passer en **audit-ok** sans troisième lecture complète. Une vérification par script des 8 chaînes suffit.

## Clôture
Les 8 patchs du V2 appliqués mot pour mot (tour 2) : **audit-ok** pour le texte de AB (IMG-166 à 237). Tous les textes de l'imagerie (IMG-001 à 344) sont audit-ok.
