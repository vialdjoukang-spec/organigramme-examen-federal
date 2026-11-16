# Audit médical — LOT_044 DX.9 Pneumothorax spontané (porte P3)
Fichier : `LOT_044_Phase_B_V0_DX.9.html`, 154 221 octets, SHA-256 `106b248e…fc4911d`. Lecture : points 4, 8, 9, 10, 11 ; AIPS Dafalgan 47503, Morphini HCl Streuli 56554/56560, Xylocain 52094 lues ; liste Swissmedic du 30.09.2026.

| Point | Score | Raison |
|---|---|---|
| 4 | 2 | E1–E5 avant fréquents ; tableau tranche/piège complet |
| 8 | 2 | Critères datés, seuils BTS/ACCP, ce qui ne suffit pas |
| 9 | 2 | Gold standard, performances chiffrées vérifiées |
| 10 | 1 | « connue ou suspectée » = secondaire, contraire à ERS 2024 ; site de décompression sur source de 2012 |
| 11 | 1 | Paracétamol et morphine conformes ; lidocaïne sur AIPS d'un gel urétral (Critique) ; n° morphine injectable faux |
| **Total** | **8/10 = 80 %** | Finale : **non** |

| Gravité | Point | Extrait (avant) | Correction | Source |
|---|---|---|---|---|
| Critique | 11 | « L'information professionnelle de Xylocain® rappelle que la dose… » + cellule « Xylocain® 52094 » | Supprimer ; AIPS injectable Rapidocain 32381 ou Lidocain Streuli 30015 | aips-52094-1 (usage urologique) |
| Grave | 11 | HELP : lidocaïne d'infiltration « sans AIPS » | Monopréparations injectables existent | Liste Swissmedic |
| Grave | 11 | « Morphini HCl Streuli®, autorisation Swissmedic 56554 » (texte + tableau) | 56560 (solution injectable) | aips-56554-64 |
| Moyen | 10 | « Si une maladie pulmonaire est connue ou suspectée… secondaire » | « établie » | wa346e0-16 |
| Moyen | 10 | Décompression « par voie antérieure » (RMG 2012) | Source européenne récente ou « À vérifier » | LV8 |
| Léger | 8, 11 | Source « ACCP 2001 » en tableau ; lidocaïne sans citation ; paracétamol rénal omis | Voir JSON | wfad2fa-25, aips-47503-8 |

Vérifié conforme : Dafalgan 500–1000 mg, 4–8 h, 4 g, 2 g si hépatopathie ; morphine IV 2–10 mg à 10 mg/min, IM/SC 5–10 mg, max 30 mg/4–6 h ; allaitement contre-indiqué ; chiffres ERS 2024 (aide à la décision, PSP, RAMPP, ABP 1–2 mL/kg, OR 0,26, vol 7 jours).
Ce qui manque pour « oui » : AIPS de lidocaïne injectable, n° 56560, classification ERS. Détail applicable : `LOT_044_Phase_B_V0_DX.9.html.audit.json`.
