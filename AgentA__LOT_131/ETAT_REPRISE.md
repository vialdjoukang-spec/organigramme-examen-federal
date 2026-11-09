# État de reprise — LOT_131 (F1.2)

Pause du propriétaire, 9 novembre 2026, vers 16 h 23 (Europe/Zurich). Branche `agentA/lot-131`. Aucune pull request.

Le run GitHub Actions `42638280916` (workflow « Gemma LOT 131 ») était encore **en cours** au moment de cette pause. Il ne faut pas le relancer ni l'annuler : à la reprise, télécharger ses artefacts.

## Fait

- Liste DX gelée dans `LISTE_DX_CANONIQUE.md` (prévalence documentée, rangs E séparés).
- 47 extraits vérifiés comme sous-chaînes des sources lues le 9 novembre 2026 : `preuves/preuves.jsonl`, empreintes dans `preuves/SOURCES.json`. Les PDF complets ne sont pas versionnés.
- Prompt à passe unique : `PROMPT_RUBRIQUE_UNE_PASSE.md`. Gemma n'a pas reçu de seconde passe.
- Débit mesuré en local sur `gemma4:e4b-it-qat` : environ 12 tok/s, `think` vide. Essais archivés dans `Gemma__LOTS_Pilote/LOT_131/essai_prompt/`.
- Commit de départ du workflow : `6309ec6a`.
- Job Actions **DX.9 réussi**. Texte brut des 14 points : `Gemma__LOTS_Pilote/LOT_131/brut/DX.9/`.
- Outils d'audit (pas un second appel Gemma) : `outils/nombres.py`, `outils/corriger.py`, `outils/forme.py`, `outils/auditer.py`, `outils/metriques_francais.py`, `outils/assembler.py`.
- Brouillon d'assemblage **DX.9 seulement** : `LOT_131_Phase_B_V0_DX.9.html`, 82 151 octets. `controle_lot.py verifier --sans-nom` : 0 critique de forme, 14 points `dx9-p1`…`dx9-p14`, texte justifié, îlots, 6 fenêtres `<details>`, pas de fenêtre dans le point 13, fenêtre « Urgence — conduite chronologique » présente. Ce fichier n'est pas le lot final.

## Reste (ne pas commencer avant une reprise explicite)

- Attendre la fin du run `42638280916`, puis récupérer les artefacts des jobs encore ouverts au moment de la pause : Phase_A, DX.1, DX.2, DX.3, DX.4, DX.5, DX.6, DX.7, DX.8, DX.10. Si un job a échoué, le signaler et rédiger la partie manquante sans Gemma.
- Assembler les 11 HTML dans la bande 80 000–150 000 octets, avec les fenêtres V0 (une par notion technique, urgence chronologique, divergence le cas échéant), îlots, justification, ids intacts.
- Audit de l'auditeur : nombres hors extrait, sécurité, français, rapports colorés dans `audits/`, manifeste SHA-256.
- Le seuil pilote de répétition des 4-grammes (≤ 10 pour 1 000 mots) n'était pas atteint sur le brouillon DX.9 d'avant le complément d'extraits (54,4). Le détecteur de verbes signale à tort des phrases verbales. À recalculer sur les fichiers finaux, sans en faire un faux critique médical.
- Rapport final : tailles, SHA-256, fenêtres par fichier, part Gemma et part auditeur. Toujours sans pull request.
