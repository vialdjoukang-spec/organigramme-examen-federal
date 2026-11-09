# STATUT · LOT_131 · agent B · 9 novembre 2026

Branche : `agentB/lot-131-p2`. Travail interrompu sur consigne de Vial, même incomplet. Rien n’a été supprimé.

## DX pairs

| DX | Nom | HTML | État |
| --- | --- | --- | --- |
| DX.2 | Varicocèle | 101109 octets, déjà poussé | Monographie écrite. Aucun médicament nommé : pas de posologie AIPS à insérer. |
| DX.4 | Hypospadias | 100141 octets, HTML régénéré, non repoussé avant ce commit | Monographie écrite. Mentions de testostérone (Testogel 56779, Nebido 56813, Testostérone Spirig HC 68976, Testosteron-Mepha 68989) : l’hypospadias n’est pas leur indication. La posologie mot pour mot de ces notices n’est pas encore recopiée dans le point 11. |
| DX.6 | Torsion du testicule | 100699 octets, déjà poussé | Monographie écrite. Aucun médicament nommé : pas de posologie AIPS à insérer. |
| DX.8 | Carcinome épidermoïde du pénis | 102301 octets, HTML régénéré, non repoussé avant ce commit | Monographie écrite. Bloc AIPS inséré (Efudix 36464, Aldara 55070, Gardasil 9 65387). L’audit mot pour mot n’est pas terminé : plusieurs citations Gardasil ne sont pas encore des sous-chaînes exactes de la notice. Le cisplatine est nommé sans notice recopiée (Cisplatine Sandoz 51077 existe ; le pénis n’y figure pas). |
| DX.10 | Gangrène de Fournier | 96094 octets, jamais commité avant ce commit | Monographie rédigée, hors bande du harnais (sous 100000 octets). Bloc AIPS présent (58151, 59766, 53105, 59764, 70800, 48018, 58919, 68511, 59876, 55902, 66690, 57469). L’audit mot pour mot n’est pas fini : espaces, tableaux rénaux et quelques phrases jointes ne collent pas encore à la notice. Des phrases anciennes disent encore que le corpus ou un numéro Swissmedic n’a pas été lu. |

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
