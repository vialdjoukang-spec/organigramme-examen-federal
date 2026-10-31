# ADR-004 — Brief adapté au LOT demandé (2026-10-31) — [Accueil](../00_ACCUEIL.md)

**Contexte.** `contexte_lot.py` prenait le dernier `BRIEF_PHASE_B.md` (LOT_017, SSP S1.1 Diplopie, chemins `/home/user/…`, branche production-v2) et le copiait dans le paquet rédacteur de tous les LOTS. Mesure du bac à sable du 31.10.2026 : LOT_134 et LOT_135 contaminés. Voir [P-20](../PIEGES.md).

**Décision.** La copie mise dans le paquet substitue le code SSP, le nom du SSP et les chemins depuis `CATALOGUE_248.csv` et la racine du dépôt. Le fichier brief sur le disque n'est pas modifié. Ce bloc est classé N3 et placé en fin de paquet, pour que le préfixe stable ne change pas d'un LOT à l'autre.

**Conséquences.** (+) le rédacteur voit le SSP du LOT demandé. (−) le brief modèle reste un texte V0 (bande 80–150 Ko) : l'en-tête du paquet rappelle la norme V8. L'extraction des points V8 passe par [extraire_v8.py](../../outils/extraire_v8.py) (P-21), pas par le harnais.
