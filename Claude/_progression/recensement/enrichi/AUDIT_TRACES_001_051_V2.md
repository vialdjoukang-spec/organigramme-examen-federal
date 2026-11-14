# Audit V2 : vérification des corrections des tracés EXP-001 à EXP-051 (14.11.2026)

Méthode : lecture de `CORRECTIONS_TRACES_001_051.md` et du champ `traces` de 008 et 049 dans `EXP_a.json`.

**Verdict : corrections requises** (1 patch, sur 049).

| id | Jugement strict | Statut |
|---|---|---|
| 008 | Le champ `normal` n'a pas changé : c'est toujours le PEV Wikimedia, avec des P100 à ≈ 100 ms, symétriques. Ce tracé est réellement normal. Le témoin malade (P100 à 120,9 ms) est dans le champ `patho`, et le repère 2 le déclare « déjà allongé ». Il n'y a donc pas de « normal anormal » : `manque_normal` n'est pas requis. | corrigé |
| 049 | La `technique` reconnaît que la dissociation P/QRS n'est pas lisible. Le seul repère restant, l'échappement lent à 41/min, ne distingue pas un BAV complet d'une bradycardie sinusale ou d'un BAV 2:1. Le signe clé n'est donc pas montré, et le tracé ne peut pas enseigner le diagnostic annoncé. | **à retirer** |

## Patch exact

| id | PATCH |
|---|---|
| 049 | Remplacer `traces` par `{"manque": "Aucun tracé libre ne montre lisiblement la dissociation auriculo-ventriculaire (ondes P régulières indépendantes des QRS) du BAV complet ; le monitorage PMC10106591 ne la laisse pas voir (audit V2 du 14.11.2026).", "a_chercher": {"patho": "ECG 12 dérivations ou bande DII longue : ondes P régulières, QRS d'échappement réguliers plus lents, sans relation fixe entre P et QRS"}}`. Supprimer `img/EXP-049_patho.jpg` et `img/EXP-049_normal.jpg` s'ils ne servent plus ailleurs (le normal reste disponible par 045 à 051), puis régénérer `_verif`. |

Le patch appliqué, le lot 001-051 passe à **audit-ok** : les autres corrections ont été relues dans le JSON et sont conformes.

## Clôture
Patch 049 appliqué mot pour mot (traces.manque, images supprimées) : **audit-ok** pour les tracés EXP-001 à 051.
