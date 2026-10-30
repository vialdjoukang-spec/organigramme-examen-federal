# Brief commun — audits des fichiers Phase B de LOT_013 (G13 Décès non naturel)

Dépôt : /home/user/organigramme-examen-federal (branche production-v2 ; AUCUN commit ni push : la session principale s'en charge). D'autres agents travaillent en parallèle dans `lot en cours de production/LOT_013/` : tu ne modifies QUE le fichier audité, `HELP_DX<N>.md` et les deux journaux d'audit.

Pièces : `LISTE_DX_CANONIQUE.md` (GELÉE : le `<h2>` doit être mot pour mot `DX.<N> — <nom>`), `CORRECTIONS_AUDIT.md` (corrections de la Phase A à hériter), `evidence/` (+ `evidence/DX<N>_*`), `HELP_DX<N>.md`, `JOURNAL_DX<N>.md`, corpus AIPS `.cache/aips/AipsDownload_20261008.xml` (grep ciblé) et extraits `.cache/aips/<numéro>.txt`.
Règles : Prompt V0 §10–14, §16, §16.1 (aucun refus : tu corriges toi-même), harnais P2 (lecture ciblée par `python3 harnais/controle_lot.py extraire <fichier> --points …`).
Journaux (ajoute, n'efface rien) : `LOT_Claude_Finaux/LOT_013/audits/corrections.jsonl` (une ligne par correction ; lot "LOT_013", code_ssp "G13", lecon "DX.<N> — <nom>") et `LOT_Claude_Finaux/LOT_013/audits/scores.jsonl` (une ligne ; fichier "LOT_013_Phase_B_V0_DX.<N>.html", avant/après, octets, sha256).
Fin : `python3 harnais/controle_lot.py verifier "lot en cours de production/LOT_013" --sans-nom --json` (ne regarde que TON fichier ; les autres DX peuvent être en cours d'écriture) puis `python3 harnais/rapport_qualite.py`. Bande 80 000–150 000 octets ; FIN_FICHIER intact ; fenêtres popover ; aucun JavaScript. Réponse finale ≤ 15 lignes.
