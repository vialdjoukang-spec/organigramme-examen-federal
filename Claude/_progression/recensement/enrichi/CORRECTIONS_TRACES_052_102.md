# Corrections des tracés EXP-052 à EXP-102 (EXP_b.json), 14.11.2026

Corrections faites d'après `AUDIT_TRACES_052_153.md`. Seul le champ `traces` a changé. Le JSON est valide et `generer.py` est relancé.

| id | Correction |
|---|---|
| 052, 053, 055, 057, 058, 065, 068, 069 | La `technique` du tracé normal commun (PMC3038953, fig. 2) déclare désormais son contexte : « enregistré après réduction d'une FA par digoxine chez un adolescent sain (fig. 2) ». J'ai supprimé le doublon « d'adolescent en bonne santé ». |
| 052 / 152 | Je garde le tracé patho PMC10244670 (fig. 2A) pour **052 seulement** : un QT long acquis bradycardie-dépendant à 543 ms y prépare des torsades, ce qui colle à l'entité. La `technique` de 052 dit « tracé réservé à EXP-052 (ne pas le réutiliser pour EXP-152) ». **EXP-152 (EXP_c.json) doit recevoir un autre tracé.** Les autres candidats de 052 ne conviennent pas : PMC10076737 a un QTc de 478 ms en tachycardie, et PMC7847214 mêle bloc sino-auriculaire et ondes d'Osborn. |
| 102 | Le repère 1 dit maintenant « Qmax abaissé à 7 ml/s », valeur de la légende. Sa `semio` est ajustée. |
| 061 normal | La `technique` précise désormais le panneau A, cas 4 : un apparenté asymptomatique d'une famille SCN5A, dont la légende des auteurs donne le VG comme normal (« Case 4 and Case 5 presented a normal left ventricle »). Le panneau dilaté (50 mm) n'est pas repris. |
| 066 | Je n'ai rien changé : l'audit juge acceptable le format différent entre le normal et le patho, déjà déclaré. |
