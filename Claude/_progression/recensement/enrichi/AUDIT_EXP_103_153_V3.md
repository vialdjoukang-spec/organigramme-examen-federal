# Contre-audit V3 : EXP_c.json (EXP-103 à EXP-153), 14.11.2026

**Version auditée** : EXP_c.json, 125 654 octets, SHA-256 `65710f32…3b00c45c`.

**Méthode** : j'ai comparé ce fichier par programme à la version V2 (commit 0b1145ad7). Dix champs ont changé, tous dans le périmètre de P1 à P9 : 113 sources ; 114 traces et traitement ; 122 traces et valeurs_normales ; 135 sources ; 136 traces et valeurs_normales ; 137 autres ; 141 traces. Aucun autre champ n'a été touché.

| Patch | id · champ | Texte relu | Statut |
|---|---|---|---|
| P1 | 137 · autres[2].pourquoi_pas_gold | « il exige un cathétérisme veineux fémoral bilatéral jusqu'aux sinus pétreux » | corrigé. La seule « ponction lombaire » restante est en EXP-130 (hypocrétine du LCR), où elle est exacte. |
| P2 | 113 · sources | « AIPS Gonal-f PEN n° 56689, août 2026, refdata (lu) » | corrigé |
| P3 | 136 · valeur, traces | « hausse ≥ 200 (70 µg/l), c.-à-d. > 500 (180 µg/l) à 30 min » ; patho « ≤ 500 nmol/l » | corrigé et conforme à l'AIPS Synacthen n° 31723 |
| P4 | 122 · traces.normal | « TcPO2 ≥ 60 mmHg au dos du pied (pas d'ischémie) » | corrigé et cohérent avec les valeurs |
| P5 | 114 · traces.normal | « pic systolique > 30 cm/s, télédiastolique ≤ 5 cm/s » | corrigé et cohérent avec les valeurs |
| P6 | 141 · traces.normal | « au-dessus du seuil du laboratoire (≈ 7 µg/l …) » | corrigé ; la zone grise a disparu |
| P7 | 114 · traitement[1] | « … ou un stimulateur de la guanylate cyclase (riociguat) » | corrigé et conforme aux contre-indications de l'AIPS Viagra |
| P8 | 135 · sources | « Essai INOX, Lacasse Y et al., N Engl J Med 2020;383:1129-38 (protocole lu ; article non lu) » | corrigé |
| P9 | 122 · valeurs_normales[0].source | « ≥ 25 : IWGDF/ESVS/SVS 2023 ; ≥ 60 et < 30 : revue secondaire (non lus) » | corrigé |

**Verdict : audit-ok.** Les 9 points sont appliqués sans erreur nouvelle. Les compléments déjà marqués honnêtement « À vérifier » restent ouverts. Ils ne bloquent pas la publication : molécules absentes du corpus, schémas obstétricaux en attente d'un avis SGGG, OAC à lire sur fedlex, seuils EULAR et EAU cités par une source secondaire. Je n'ai rien modifié d'autre ; ni commit ni push.
