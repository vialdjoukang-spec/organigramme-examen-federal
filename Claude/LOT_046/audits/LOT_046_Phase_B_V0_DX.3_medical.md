# Audit médical — LOT_046_Phase_B_V0_DX.3.html
Version : 165437 octets, SHA-256 `17570713e2ad6673`. Audit ciblé Θ3, points 4, 8, 9, 10, 11 ; extraits AIPS du paquet et liste HAM 30.09.2026 lus.

| Point | Note | Raison |
|---|---|---|
| 4 | 1/2 | Graves avant fréquents ; exclusion de l'IC par seuils non aigus |
| 8 | 2/2 | Rome 2021 datée, seuils exacts, ce qui ne suffit pas |
| 9 | 1/2 | NT-proBNP > 125 en aigu ; éosinophiles < 0,1 G/L « contre-indiqué » excessif |
| 10 | 1/2 | VNI sur « ou » ; oxygène contrôlé placé après l'antibiotique |
| 11 | 0/2 | Salbutamol, prednisone, co-amoxicilline, doxycycline déclarés sans AIPS alors que présents dans le corpus ; formules de lacune |

**Score : 50.0 %. Question finale : non.** Des corrections Critique restent ouvertes ; le fichier ne passe pas la porte.

| Gravité | Pt | Extrait (≤ 200 car.) | Source |
|---|---|---|---|
| Critique | 11 | Le salbutamol par inhalation n'a pas d'information professionnelle lisible dans la base utilisée, donc seule la classe est décrite ici. | aips-37397-3, aips-37397-43 (présents dans le corpus du LOT, paquet PA ; formule de lacune LV7) |
| Critique | 11 | Salbutamol inhalé (spécialité sans AIPS lue) | aips-37397-43 |
| Grave | 11 | L'information professionnelle ne contient pas de posologie propre à l'exacerbation de BPCO, donc la stratégie HUG et GOLD retiennent une durée de 5 jours w18c561-68 gold2026-565 . | w18c561-68, aips-69640-7 (dose déjà écrite dans la PA) |
| Grave | 11 | Corticoïde oral pendant 5 jours ; dose standard de la stratégie HUG non reproduite ici faute d'AIPS lu (voir HELP) | w18c561-68, aips-69640-7 |
| Critique | 11 | Le document lu concerne les suspensions pédiatriques, donc la dose adulte n'est pas reproduite ici, et la stratégie HUG retient l'amoxicilline-clavulanate par voie orale pendant 5 jours en ambulatoire | aips-45674-4 (paquet DX.1 du même LOT) ; formule de lacune LV7 |
| Critique | 11 | Alternative empirique selon GOLD, dose non lue dans l'AIPS | aips-44000-8 (dose présente dans le paquet DX.3 lui-même) |
| Grave | 4 | Une valeur de BNP inférieure à 35 ng/l ou de NT-proBNP inférieure à 125 ng/l permet d'écarter l'insuffisance cardiaque w149687-30 . | w149687-30 (seuils non aigus appliqués à une dyspnée aiguë) |
| Moyen | 10 | Si la gazométrie montre un pH inférieur à 7,35 ou une pression partielle de gaz carbonique supérieure à 6,0 kPa, alors on instaure la ventilation non invasive en l'absence de contre-indication w18c561 | w18c561-73, gold2026-527 (acidose = pH ET PaCO2 ; une hypercapnie compensée n'impose pas la VNI) |

Corrections exactes (avant/après) : `LOT_046_Phase_B_V0_DX.3.html.audit.json`.

**Ce qui manque :**
- Salbutamol inhalé : Ventolin nébuliseur-doseur 54320 et Diskus 53898 (aips-37397) ; Salbu Orion Easyhaler 53190 ; Ventolin Dosier-Aerosol présent dans la liste HAM.
- Céfuroxime et lévofloxacine orales : monopréparations HAM (Tavanic 54365, Levofloxacin Sandoz 59085) à rapatrier.
