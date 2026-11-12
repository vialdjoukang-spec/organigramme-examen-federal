# DX.9 — Myasthénie auto-immune : audits A/B et contre-audit (12.11.2026)

Réserve : aucun outil de sous-agent n'était disponible dans cette session ; les audits A et B ont été conduits par le rédacteur, phrase par phrase contre les sources lues (texte intégral ou résumé, AIPS refdata).

## Audit A (médical) — constats et corrections
- Contre-indications de la prednisone non lues → remplacées par celles de l'AIPS 29349 (hypersensibilité ; traitement prolongé : ulcère, ostéoporose sévère, diabète de type 2…).
- Azathioprine et allaitement : l'AIPS 31887 interdit l'allaitement, le consensus nordique (S2) l'autorise → conduite AIPS enseignée, divergence écrite.
- Prednisone : « risque de crise au début du traitement » surinterprétait l'AIPS → « risque accru si anticholinestérasiques associés ».
- Deux renvois S1 portaient sur le passage des syndromes congénitaux (muscle lisse et cardiaque) → phrases réécrites sur S2.
- Trois attributions trop larges corrigées (dysphagie du sujet âgé attribuée à S3, « salves rapides » attribuées à S4, ptosis « oriente fortement »).
- Divergence AIPS ↔ recommandation écrite pour la prednisone (arrêt des anticholinestérasiques 24 h avant selon l'AIPS).
- Doses hors AIPS signalées : prednisone, IgIV (pas d'indication myasthénie dans l'AIPS Privigen), azathioprine (schéma myasthénique), pyridostigmine pédiatrique et 720 mg, édrophonium.

## Audit B (conformité) — constats
- 14 points présents ; point 1 = définition seule (consensus nordique 2024) ; ancienne architecture (sommaire, popover) supprimée.
- 36 fenêtres `:target`, 6 fiches `.mb` (pyridostigmine, prednisone, azathioprine, IgIV, efgartigimod, éculizumab), fenêtre « Urgence — conduite chronologique », 8 questions au point 14.
- Images réelles, couleur quand disponible (OpenStax CC BY 4.0) ; photo clinique (CC BY 2.0) ; TDM (CC BY-SA 3.0) ; noms préfixés dx9_.
- controle3 --script-ok VERT ; 90 513 o (87 311 o hors images) ; verif_aips OK (6 AIPS).

## Contre-audit
Toutes les corrections A et B sont appliquées et vérifiées par controle3 et verif_aips. Reste ouvert : aucune recommandation suisse de société savante lue sur la myasthénie (HELP.md) ; figure de décrément (M-dekr.png) non prise (429).
