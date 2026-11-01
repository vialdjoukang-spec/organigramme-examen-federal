# Niveaux de question — EX · AP · SPE

| Code | Champ `niveau` | Couleur | Pour qui / quoi | Part visée |
|---|---|---|---|---|
| **EX** | `examen` | noir `#1a1a1a` | Le réflexe attendu de **tout** candidat à l'examen fédéral CK : reconnaître le DD, l'examen qui tranche, l'alarme, la 1re ligne. | 55–65 % |
| **AP** | `approfondissement` | bleu `#0B5A8C` (texte bleu) | Le **pourquoi** : mécanisme, chaîne anatomie → physiologie → physiopathologie → clinique → traitement. Rend l'EX inoubliable. | ≈ 20–25 % |
| **SPE** | `specialiste` + `specialite` obligatoire | violet `#6B2D8B`, badge `SPE · <spécialité>`, bouton 🔥 | Décision de 2e ligne pour **sentir la spécialité** (orientation de carrière). Le tableau 🔥 agrège juste/posées par spécialité. | ≈ 15–20 % |

Règles
- Couverture DD : **≥ 2 EX cibles par DX** ; AP et SPE enrichissent (signalés par `couverture_dd.py` quand un DX n'en a aucun).
- Une SPE sans `specialite` bloque le build.
- Les filtres Tous / EX / AP / SPE du HTML et les scores par niveau reposent sur ce champ.
- La médecine d'abord : l'examen n'est qu'une partie du but ; AP et SPE ne sont pas « hors programme », ils ancrent l'EX.
