# Audit de conformité L1 — LOT_023 Phase A (audit B)

Fichier : LOT_023_Phase_A_V0.html (81 992 o, bande 80–150 Ko respectée). Modèle : LOT_022. Le cours n'a pas été modifié.
Outil : `controle_lot.py verifier` → critiques : 3 lignes > 3 000 caractères (l.73, 114, 151) ; ressources externes forme.css/forme.js (identiques à LOT_022, donc conformes au front-end uniforme) ; avertissement « non validé cliniquement » absent (identique à LOT_022).

Constats positifs : 14 points présents et bien affectés ; point 1 = définition seule ; point 6 = 7 fenêtres, une par région ; point 14 = 8 questions avec renvoi ; 32 fenêtres, aucune imbriquée, tous les liens ouvrent une fenêtre existante ; base anatomo-fonctionnelle avec image réelle (Gray 994) et 6 repères ; ordre DX.1→DX.10 et 🚩 E1–E3 conformes à LISTE_DX_CANONIQUE.md ; aucun attribut title.

1. [majeure] Lignes > 3 000 caractères (l.73, 114, 151) → couper ces trois lignes par des retours à la ligne entre blocs (critique du harnais, absente de LOT_022).
2. [majeure] Abréviations jamais développées dans le texte : « L’UEG et l’ESNM définissent… », « l’ESGE », « l’ESO et l’ESSD », « FEES », « NIHSS », « ORL », « bpa », « AVC » (chapeau) → développer à la première occurrence (United European Gastroenterology, European Society for Neurogastroenterology and Motility, etc. ; « accident vasculaire cérébral (AVC) »).
3. [majeure] Point 2 : « Ces deux chiffres placent la dysphagie après AVC en tête… devant la maladie de Parkinson (plus de 15 000 personnes) » → compare un nombre de cas à des fréquences hétérogènes, ce que la fenêtre « Limites » interdit ; reformuler d’après les pourcentages de dysphagie par terrain.
4. [majeure] Point 4 : « les cinq urgences, de E1 à E5 » et fenêtre E1–E5 → la liste canonique ne fixe que 🚩 E1–E3 ; E4 et E5 sont absents des points 2, 8, 10, 13. Ramener à E1–E3 ou justifier E4/E5 sans rang.
5. [mineure] Point 3, fenêtre « Trois niveaux, trois mécanismes » → le tableau compte quatre lignes ; titrer « Quatre niveaux, quatre mécanismes ».
6. [mineure] Redites chiffrées : 35 %/82 % de Parkinson (point 2 tableau, « Limites », point 13) ; récidive de 21 % (points 4, 11 tableau, 11 urgence) ; antibiotique préventif (point 11 ×1, point 12 ×2) ; délai de 6 h répété 7 fois → garder une seule occurrence par chiffre et renvoyer au point.
7. [mineure] Phrases > 28 mots : « Elles définissent la dysphagie œsophagienne comme une difficulté d’avaler ressentie derrière le sternum, due à une anomalie… » (point 1) ; « La dysphagie touche 10 à 20 % … et la dysphagie oropharyngée atteint 48,1 %… » (point 2) ; « L’examen suit l’ordre du danger : … » (point 6) ; « La prévention secondaire dépiste… » (point 12) → scinder en deux phrases de 12 à 28 mots.
8. [mineure] Phrases non verbales : « Situation : », « Erreur du débutant : », « Minute 0 : », « Image : Henry Vandyke Carter… », cellules « Bilan spécialisé de la jonction pharyngo-œsophagienne » (DX.8) et « Bilan neurologique spécialisé » (DX.9) → réécrire en phrases verbales ; préciser les examens (vidéofluoroscopie, œsogastroduodénoscopie, anticorps anti-récepteur de l’acétylcholine) si une source les cite.
9. [mineure] Repère 6 de l’image placé près de la trachée (étiquette « Trachea ») alors que le texte désigne l’œsophage → recaler le cercle sur l’œsophage postérieur (x ≈ 120–150) ou vérifier visuellement.
10. [mineure] Point 5, tableau : « Pourquoi » en phrases nominales courtes et « Un reflux connu ne rend pas l’obstacle bénin » → harmoniser en phrases verbales complètes.

Verdict : cohérence A↔B non contrôlée ici (hors périmètre de cet audit). Dépôt possible après les corrections 1 à 4.
