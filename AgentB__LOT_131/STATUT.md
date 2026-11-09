# STATUT · LOT_131 · agent B · 9 novembre 2026

Branche : `agentB/lot-131-p2`. Travail interrompu sur consigne de Vial, même incomplet. Rien n’a été supprimé.

## DX pairs

| DX | Nom | HTML | État |
| --- | --- | --- | --- |
| DX.2 | Varicocèle | 101109 octets, déjà poussé | Monographie écrite. Aucun médicament nommé : pas de posologie AIPS à insérer. |
| DX.4 | Hypospadias | posologies recopiées au point 11 | Testogel 56779, Nebido 56813, Spirig HC 68976 et Mepha 68989 sont recopiés mot pour mot, avec l’indication d’hypogonadisme de l’homme adulte, pas l’hypospadias. Testogel n’est pas autorisé chez l’enfant. |
| DX.6 | Torsion du testicule | 100699 octets, déjà poussé | Monographie écrite. Aucun médicament nommé : pas de posologie AIPS à insérer. |
| DX.8 | Carcinome épidermoïde du pénis | notices recopiées | Efudix 36464, Aldara 55070, Gardasil 9 65387 en phrases séparées, et Cisplatine Sandoz 51077. Le pénis n’est pas l’indication du cisplatine ni des crèmes. |
| DX.10 | Gangrène de Fournier | au-dessus de 100000 octets | Bloc AIPS conservé. Les phrases qui niaient le corpus ont été retirées. Le céfotaxime reste absent du corpus. |

Les DX impairs et la Phase A ne sont pas le travail de cette branche.

## Règle doses du 9 novembre 2026

- Passe AIPS commencée, non close. Aucun décompte final de doses auditées mot pour mot.
- Céfotaxime : absent du corpus AIPS local du 8.10.2026. Aucune dose.
- Fosfomycine intraveineuse : aucune spécialité intraveineuse trouvée. Le sachet oral 66690 n’est pas une dose de Fournier.
- Gutron (midodrine) : aucun DX pair ne le cite. Le n° 44976 n’existe pas. La notice est Gutron 44977 ; MIDODRIN SUBSTIPHARM est le 69384. Aucune mention « absent » et aucune dose n’ont été écrites.
- « À vérifier » n’a pas été utilisé.

## Reprise

1. Recoller chaque citation entre guillemets à la notice, y compris tableaux rénaux.
2. Retirer les phrases qui disent encore qu’une notice n’a pas été lue.
3. Recopier, sans les appliquer à la mauvaise indication, les posologies de la testostérone (DX.4) et du cisplatine 51077 (DX.8).
4. Remonter DX.10 dans la bande 100000–150000 octets, puis relancer `harnais/controle_lot.py`.
