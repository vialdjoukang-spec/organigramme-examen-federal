# Corrections du texte de TH.json (IMG-105 à IMG-165), 14.11.2026

Les patchs viennent de AUDIT_TEXTE_TH.md. Le champ `images` n'a pas été modifié. Le JSON est validé (json.load, 61 entrées).

## Critiques (14), tous appliqués
- 145 : flucloxacilline 12 g/j, 2 g au plus par perfusion ; l'AIPS Floxapen® 37404 la prévoit aussi : il n'y a donc pas d'écart avec l'ESC.
- 105 : amoxicilline 1 g 3×/j pendant 5 j (SSI 3007, validée le 15.05.2024 ; AIPS Amoxi-Mepha® 44911) ; co-amoxicilline 1 g 3×/j ; « À vérifier » supprimés ; source OrPha retirée.
- 109 : Tamiflu® 5 j ; dexaméthasone 6 mg/j, 10 j au plus (AIPS Dexamethason Zentiva® 41074).
- 117 : Trikafta® 67773 (remplace Kaftrio®).
- 121 : avacopan 30 mg 2×/j (AIPS Tavneos® 66772).
- 126 : riociguat titré jusqu'à 2,5 mg 3×/j au plus, si la pression systolique reste ≥ 95 mmHg.
- 130 : citrate de caféine 20 puis 5 mg/kg (AIPS Peyona® 65490).
- 125 : énoxaparine 1 mg/kg 2×/j pendant la grossesse (AIPS Clexane® 49456) ; flacon multidose de Fragmin® exclu.
- 144 : prasugrel 60 puis 10 mg (5 mg/j si < 60 kg ; déconseillé dès 75 ans) (AIPS Efient® 59136).
- 158 : tocilizumab 162 mg s.c. (AIPS Actemra® 58868) ; méthylprednisolone 250–1000 mg/j pendant 3 j.
- 136 : nivolumab 3 mg/kg toutes les 2 semaines + ipilimumab 1 mg/kg toutes les 6 semaines (AIPS Opdivo® 65660, Yervoy® 61798).
- 116 : indication de l'AIPS Ofev® (PID fibrosante progressive).
- 114 : Prolastin-C® 60 mg/kg/semaine (AIPS 69448).
- 135 : acide tranexamique 1 g + 1 g (guideline européenne 2023) ; l'AIPS 69880 ne cite pas le traumatisme.

## Majeurs (12), tous appliqués
- 149 : spironolactone hors indication de l'AIPS ; éplérénone (AIPS Inspra® 57147) ; ESC 2026.
- 122 et 149 : ESC 2026 pour l'insuffisance cardiaque ; furosémide 40 mg i.v. (AIPS Lasix®).
- 107 : 14 j selon l'AIPS, 21 j dans le VIH (EACS) ; schéma de prednisone ; doses TMP/SMX.
- 114 : GOLD 2026 ; AIPS Ultibro® 63132.
- 117 : ERS 2025 sur les bronchectasies.
- 148 : TAVI dès 70 ans (ESC/EACTS 2025, classe I).
- 163 : aucune flucloxacilline orale au corpus AIPS (reste À vérifier).
- 131 : séquence de l'ERC 2025 contre l'obstruction des voies aériennes.
- 158 : gold réécrit (échographie dans l'ACG ; angio-IRM dans Takayasu) ; la TEP passe en alternative.
- 119 : mycophénolate hors AIPS ; Endoxan® ; source ERS 2025.
- 146 : doses d'AAS et d'ibuprofène (hors indication de l'AIPS 49526).
- 127 : grades ESMO 2022.

## Mineurs
- 118 : AIPS Prednisone Streuli® 29349.
- 106 : Manuel de la tuberculose dans sa version du 18.01.2021.
- 145 : premiere_intention mise à null.
- 147 : premiere_intention = ECG, troponine et échocardiographie transthoracique.
- Toutes les sources sont étiquetées (européenne, non européenne, OMS) ; la source suisse est placée en tête.
- 108 : source BTS pleurale retirée.
- 162 : EUSOBI ajoutée.
- 120 : ERS ajoutée (À vérifier).
- Phrases verbales : 125, 144, 146.

## Restes « À vérifier »
- Doses ESC 2025 de la péricardite.
- Doses ESC 2026 de l'insuffisance cardiaque, à relire dans le texte.
- Texte final de l'ERC PLS.
- Antibiotique oral de la mastite.
- Référence exacte de l'ERS 2025 sur les PID des connectivites.
- EUSOBI et ERS pour la pneumopathie d'hypersensibilité.

## Tour 2 (AUDIT_TEXTE_TH_V2.md, 14.11.2026) : patchs appliqués mot pour mot
- Critique N1, 149 : bisoprolol de 1,25 à 10 mg/j par paliers (AIPS Bisoprolol Spirig HC® 70190) ; la source est ajoutée.
- Majeur N2, 146 : doses de la péricardite selon le tableau 13 de l'ESC 2025 (AAS et ibuprofène 3×/j avec décroissance, IPP, colchicine 0,5 mg 1 ou 2×/j pendant ≥ 3 mois) ; référence complète de Schulz-Menger 2025.
- Majeur N3, 147 et 146 : sport suspendu jusqu'à la rémission, au moins 1 mois (ESC 2025, classe I) ; la source de 147 est complétée.
- Majeur N4, 122 : furosémide ; « ESC 2026 » n'est plus présenté comme source d'un chiffre : il reste à relire dans la section 6.1.3.1.
- Mineurs :
  - 149 : spironolactone 12,5–25 mg/j, cible 50 mg/j (ESC 2026, tableau 11) ;
  - 118 : date de l'AIPS 29349 (juin 2026) ;
  - 108 : AIPS Co-Amoxi-Mepha® i.v. 56758 ;
  - 154 : AIPS Esmolol OrPha® 57413.
- Images non modifiées ; JSON validé (61 entrées).
