# Brief type — refonte d'une leçon déposée au format V8

Paramètres de l'appel : LOT, fichier (Phase A ou DX.N).
Source (ne pas modifier) : `LOT_Claude_Finaux/<LOT>/<fichier source>.html`. Sortie : `LOTS_V8/<LOT>/<même nom de fichier>.html`.
1. Lis la section 12 de `PROMPT_PRODUCTION_V2.md` et le modèle `harnais/modele_lecon/MODELE_DD_V8.html` ; reprends sa feuille de style `harnais/modele_lecon/style_lecon.css` telle quelle (îlots, bords vert/bleu ciel, Atkinson, exposants, abréviations au survol, fenêtres et sous-fenêtres).
2. Diagnostic différentiel : fiche x ≤ 9 Ko (14 parties, 2 à 4 phrases chacune, liées par des connecteurs) ; tout le reste en fenêtres et sous-fenêtres ; aucune redondance avec la Phase A du LOT (renvoi par une phrase). Phase A : texte de la fiche x ≤ 100 Ko (fenêtres et dépliants exclus, sans plafond) ; elle expose les 10 diagnostics différentiels.
3. On DÉPLACE, on ne compresse jamais : aucun fait, chiffre, dose, citation ou source ne disparaît (sauf ce qui est strictement redondant avec la Phase A pour un DD, remplacé par le renvoi) ; aucun fait nouveau. Les citations AIPS restent mot pour mot.
4. Sources en exposant `<sup class="s">16</sup>` ; liste des sources conservée (avec URL) dans un dépliant final ; chaque abréviation dans `<abbr title="…">` (définition tirée du texte source ; si absente, développement standard reconnu).
5. Figures et courbes en fenêtre ; ajoute une courbe seulement si les données de la source s'y prêtent.
6. Contrôles : `python3 harnais/verif_refonte.py <source> <sortie> --ref LOT_Claude_Finaux/<LOT>/<LOT>_Phase_A_V0.html` (sans --ref et avec --phase-a pour une Phase A) doit être VERT ; si des nombres manquent, réintègre-les en fenêtre (nombres conservés, taille, fenêtres, aucun script) ; `python3 harnais/taille_xy.py <sortie> --inscrire`.
7. Aucun commit ; téléchargements interdits (pas besoin de sources nouvelles). Réponse ≤ 4 lignes : T, fenêtres, verdict de verif_refonte.
8. Dernière ligne : `<!-- FIN_FICHIER <LOT>_<fichier>_V8 -->`.
- Les fenêtres doivent elles aussi être en phrases complètes et liées : ne pas déplacer tel quel l'ancien texte télégraphique dans une fenêtre « texte complet ».
- Le titre du diagnostic est un `<h1>` (nom exact de LISTE_DX_CANONIQUE.md), comme dans le modèle ; les parties sont en `<h2>`.
- Arbres décisionnels : en phrases liées (« Si …, alors … parce que … »), jamais en chaînes « → ».
- Tableaux d'origine : garder toutes les colonnes (dont « Conduite ») ; un piège sans sa conduite se lit comme une consigne.
- Le contrôle des nombres ne voit pas la perte de texte : comparer section par section avec la source avant de rendre.
- Retrait pour redondance : seulement si la Phase A V8 contient le passage mot pour mot (doses, citations AIPS, conduites comprises) ; sinon garder en fenêtre.
