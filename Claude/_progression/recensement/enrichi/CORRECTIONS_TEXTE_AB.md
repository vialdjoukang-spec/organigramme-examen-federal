# Corrections du texte de AB.json (IMG-166 à IMG-237) après AUDIT_TEXTE_AB.md, 14.11.2026

**Méthode** : j'ai relu chaque AIPS par son URL refdata (`aips_fiche.py trouve` puis `fiche`), puis j'ai cherché la dose dans le texte en cache. J'ai appliqué les modifications avec un script (`replace` avec assertion de présence) et vérifié que le champ `images` restait identique octet pour octet. Le JSON est valide et contient 72 entrées.

## Critiques (17/17)
C1–C17 sont appliqués avec la dose lue, le n° Swissmedic et le mois de mise à jour :
- 167 : Tecentriq 66152 (mars 2026), Avastin 56922, Imjudo 68706, Imfinzi 66548.
- 170 : carvédilol hors indication (57821) ; propranolol, avec l'indication HTP, à 20 mg 2×/j titré jusqu'à 160 mg 2×/j (47025).
- 172, 191, 227 : Clexane 49456.
- 174 : Exjade 57466, max. 40 mg/kg/j, CI si ClCr < 60.
- 175 : Duphalac 32894 et Xifaxan 63216.
- 179 : Imfinzi + gemcitabine-cisplatine.
- 180 : Ursofalk hors AMM dans la CSP (28–30 mg/kg/j).
- 185 : Creon 38219.
- 188 : Somatuline 56148 et Sandostatine LAR 53161 (intestin moyen).
- 193 : héparine 46613 (80 U.I./kg puis 18 U.I./kg/h).
- 199 : Glivec GIST 65814 (400 mg/j, ≥ 36 mois).
- 202 : Budenofalk Uno 61405.
- 203 : Pentasa 47502.
- 209 : Nexium i.v. 56730.
- 214 : Konakion MM 48112, à **10–20 mg** selon l'AIPS (et non 10 mg), Beriplex 00665, Praxbind 65804, Ondexxya 67759.
- 220 : Keytruda 66231 et Inlyta 62281.
- 222 : Votubia 62061.
- 230 : Jinarc 65676.
- 225 : Cardura CR 54617 (HTA seulement) ; phénoxybenzamine absente du corpus, donc « À vérifier ».

## Majeurs (13/13)
- **M1** : chaque citation AIPS porte désormais son n° et sa date. Les sources « Swissmedic, AIPS… » sans n° sont retirées. Chaque entrée a une ligne de source par AIPS citée.
- **M2** : Stragen est cité ainsi : « 2,25–4,5 g 3–4×/j, habituellement 100–200 mg/kg/j ». Le schéma « 4,5 g/8 h » est supprimé (176, 178, 201, 216, 218, 219).
- **M3** : Wegovy 68798 est ajouté pour la MASH F2–F3.
- **M4** : les sources sont mises à jour en EASL CHC 2025 et BCLC 2025. LI-RADS est étiqueté source américaine.
- **M5** : les seuils Baveno VII sont corrigés (25 / 15 kPa, zone grise).
- **M6** : WSES III (AAST IV–V) est embolisé même sans blush.
- **M7** : les seuils transfusionnels ESGE 2021 sont corrigés.
- **M8** : la source passe à ESVS 2025 (193, 237). Les forces restent « À vérifier » dans le texte intégral.
- **M9** : la source passe à IAP 2025 ; la force reste « À vérifier ».
- **M10** : la mise à jour HerniaSurge 2023 est ajoutée.
- **M11** : la source passe à ESPR 2026 ; la force « 2020 : doit » est supprimée.
- **M12** (217) : l'échographie est la première intention chez tous (EAU 2026).
- **M13** : les sources américaines sont étiquetées « source américaine seule » (191, 192, 204, 206, 214, 227). Pour 207, la source NEJM 2011 est marquée « à remplacer ». Pour 225, la position ESH 2020 est ajoutée. Pour 215, aucune recommandation européenne n'a été identifiée.

## Mineurs (8/8)
- **m1** : les dates AIPS sont corrigées : Vancocin mars 2026, Dificlir déc. 2024, Aldactone août 2025, Novalgin sept. 2025, Ciprofloxacine août 2025, Propranolol janv. 2023, Augmentin sept. 2026, Flagyl sept. 2025.
- **m2** : la Glypressine est indiquée < 50 kg, puis 6 mg/j.
- **m3** : Tamsulosin-Mepha 58828 (HBP seulement).
- **m4** : Prednisone Streuli 29349 et Solu-Medrol 35112 (indication sans dose propre).
- **m5** : critères de sévérité ESCMID.
- **m6** : APPAC 39 %.
- **m7** : EAU 2026.
- **m8** : FOLFIRINOX, FOLFOX, CAPOX et FLOT restent « À vérifier », car les AIPS de leurs composants n'ont pas été relues.

## Reste « À vérifier » (13 mentions)
- forces exactes d'ESVS 2025 et d'IAP 2025 ;
- phénoxybenzamine ;
- composants des chimiothérapies (186, 197, 198) ;
- antibiotiques néonataux (207) et source européenne de l'ECUN ;
- durée selon SSI (169) et date des recommandations SSI (218) ;
- PSOGI 2021 ;
- délai sportif après mononucléose (192).

Je n'ai pas vérifié moi-même les références de pages EASL 2025, BCLC 2025, ESVS 2025, IAP 2025 et ESPR 2026 : elles sont reprises de l'audit.
