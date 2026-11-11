# MISSION — banque QCM et questions type examen (un groupe PROFILES)

Le réceptacle (`outils/receptacle.py`) lit `Claude/_reference/qcm/<GROUPE>.json` (G, S1…S9, F1, F2, O1…O7) et l'affiche
sous le bouton « Banque QCM et questions type examen » du groupe. Sans fichier : espace vide, prêt à recevoir.

## Règles
- Format de l'examen fédéral suisse : **type A** (une seule meilleure réponse sur 5) et **Kprim** (4 affirmations vraies ou fausses).
- Chaque question part d'un SSP du groupe et d'un diagnostic de sa liste gelée ; la réponse se justifie par le cours audité
  (Phase A ou B) ou par une source suisse lue, citée dans `sources`. Rien de mémoire ; doses : AIPS suisse.
- Vignette clinique courte, chiffrée, phrases verbales ; distracteurs plausibles ; explication de 1 à 3 phrases.

## Format
```json
{
  "groupe": "G",
  "version": 1,
  "questions": [
    {
      "id": "G1-001",
      "ssp": "G1",
      "dx": 2,
      "type": "A",
      "enonce": "Vignette clinique, puis question.",
      "choix": ["…", "…", "…", "…", "…"],
      "reponse": 1,
      "explication": "Pourquoi B, pourquoi pas les autres.",
      "sources": ["LOT_001 Phase B DX.2, point 8", "[1] Source suisse lue, date"]
    },
    {
      "id": "G1-002", "ssp": "G1", "dx": 4, "type": "Kprim",
      "enonce": "Affirmations sur …",
      "choix": ["Affirmation 1", "Affirmation 2", "Affirmation 3", "Affirmation 4"],
      "reponse": [true, false, true, false],
      "explication": "…", "sources": ["…"]
    }
  ]
}
```
`reponse` : index (0 = A) pour le type A ; quatre booléens dans l'ordre des affirmations pour Kprim. `id` = code du SSP
puis numéro sur trois chiffres, unique. Valider : `python3 -m json.tool` puis régénérer le réceptacle.
