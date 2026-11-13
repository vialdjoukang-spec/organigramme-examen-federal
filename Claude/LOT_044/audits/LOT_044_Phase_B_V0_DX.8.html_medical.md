# Audit médical — LOT_044 DX.8 Péricardite aiguë (porte P3)
Fichier : `LOT_044_Phase_B_V0_DX.8.html`, 163 403 octets, SHA-256 `2f1766c7…7512e8`. Lecture : points 4, 8, 9, 10, 11 ; AIPS COLCTAB 67974 et Prednisone Stada 66994 lues dans le paquet ; liste élargie Swissmedic du 30.09.2026.

| Point | Score | Raison |
|---|---|---|
| 4 | 2 | Graves avant fréquents ; élément qui tranche et piège présents |
| 8 | 1 | Critères ESC 2025 faux : « défini » exige plus d'un critère additionnel (wd75364-20) |
| 9 | 2 | Gold standard, alternatives et interprétation présents |
| 10 | 1 | Nœud « défini » faux ; branche EP sans source |
| 11 | 0 | Grossesse adoucie contre l'AIPS (Critique) ; dose âgée hors AIPS ; AINS sans AIPS |
| **Total** | **6/10 = 60 %** | Finale : **non** |

| Gravité | Point | Extrait (avant) | Correction | Source |
|---|---|---|---|---|
| Critique | 11 | « En pratique suisse, le choix se fait donc en décision partagée avec l'obstétricien… » | AIPS prime : contre-indiquée en grossesse et allaitement ; contraception jusqu'à 3 mois après l'arrêt | aips-67974-7, -12 |
| Grave | 11 | « Chez la personne âgée, la dose de colchicine est réduite de moitié… » | Réduire ou espacer si fonction rénale baisse ; CI si polymorbidité | aips-67974-5, -7 |
| Grave | 8, 10 | « …et au moins un critère additionnel » (3 occurrences) | « plus d'un critère additionnel » | wd75364-20, w7d466b-23 |
| Grave | 8 | « Une douleur typique avec un frottement suffit… » ; « …avec un ECG évocateur suffit aussi. » | Douleur + 1 critère = possible | wd75364-20 |
| Grave | 11 | AINS/aspirine déclarés sans AIPS | Verser Brufen 45031 ou ASA-Tabs 49494 au paquet | Liste Swissmedic |
| Moyen | 11 | « Une protection gastrique par IPP est recommandée » | Exclure le lansoprazole (CI avec colchicine) | aips-67974-15 |
| Moyen | 11 | Atteinte hépatique ; CI omises (hommes 6 mois, anémie, IC sévère) | Ajouter | aips-67974-6, -7, -8, -12 |
| Moyen | 11 | « Ilaris est autorisé depuis août 2021 » | Ilaris 66191, autorisé depuis 2017 | Liste Swissmedic |
| Moyen | 11 | Critères de sortie sans citation | Sourcer | LV1 |
| Léger | 8, 9, 11 | 2 phrases LV1 ; NNT ICAP 4,8 calculé ; tableau « aiguë 4–6 sem » contre ESC 2025 | Voir JSON | — |

Ce qui manque pour « oui » : grossesse conforme à l'AIPS, critères 2025 corrigés, AIPS des AINS. Détail applicable : `LOT_044_Phase_B_V0_DX.8.html.audit.json`.
