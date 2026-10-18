# Audit ciblé · ouverture par activation uniquement

Verdict : aucun chemin exécutable d’ouverture au simple survol détecté pour les fiches SSP, DD, termes .tw/glossaire ou repères NC. Deux points concrets restent signalés ci-dessous. Lecture seule des fichiers canoniques ; aucun lancement distant.

## Contrôles favorables

- Aucun gestionnaire mouseover, mouseenter, pointerover, pointerenter ou focusin restant dans app_v2.html.
- Aucun identifiant exécutable LP, lpT, lpFired, lpXY ou fine orphelin ; les occurrences homonymes dans les données médicales ne sont pas du code.
- Les chemins showTip/tipToggle restants viennent d’un clic, d’une activation clavier ou de la commande explicite « Ouvrir » de la recherche calendrier.
- Les retours asynchrones monoGet, sspMonoGet, memLoad et ckNeed vérifient que la fenêtre est déjà visible et sa clé inchangée. Une fermeture efface tipK : leur résolution ne réouvre pas une fiche fermée.
- La fermeture puis restitution du focus n’a plus de gestionnaire focusin ouvrant une autre fenêtre.
- Le timer calP.t conservé arme le déplacement tactile du calendrier ; il n’ouvre pas d’infobulle. Ses annulations pointerup/pointercancel et les gestes de redimensionnement subsistent. tipT reste déclaré null et annulable, sans temporisateur d’ouverture réarmé.
- Les .tw créés par gloLink et ckL ne portent plus de title ; les repères NC n’ont pas de title interne. La minibulle NC vient uniquement du clic ou de l’activation clavier.
- Vérification syntaxique du script embarqué extraite vers work/audit-clic-seul.js : node --check réussi. Pas de suite navigateur relancée par la sentinelle pendant les essais de l’intégrateur.

## Défaut clavier précis à vérifier/corriger

pvSpan(..., act=1) crée un span .pv avec data-t, tabindex=0 et role=button. Le gestionnaire global Entrée/Espace ne traite que .tw ; un span n’a pas de clic clavier natif. Le pourcentage focusable ne s’ouvre donc pas par Entrée/Espace, contrairement aux termes .tw et aux boutons natifs. Cette lacune paraît préexistante mais empêche d’affirmer que toutes les activations clavier sont couvertes.

Correction minimale suggérée : inclure les spans [data-t][role=button] pertinents dans l’activation clavier, sans doubler l’activation native des boutons/liens et sans interférer avec les commandes du calendrier.

## Réserve pour « aucun survol partout » au sens littéral

Six aides natives title subsistent hors des fiches cliniques : statut d’enregistrement (ligne397 au relevé), commande Placer (496), cases de temps travaillé (595), Retirer dans la sélection CS (688), jauge de notions (796), bouton de station CS (826). Les SVG NC possèdent aussi chacun un title racine, utilisé par aria-labelledby. Ces éléments peuvent afficher des bulles natives du navigateur ; aucun d’eux ne réouvre #tip. Les styles CSS :hover restants ne font que modifier couleur/contour/ombre.

Si l’interdiction couvre aussi ces aides natives, remplacer les title HTML par un libellé accessible approprié ; pour le SVG préserver son nom accessible avant d’enlever son title. Aucune suppression effectuée par la sentinelle.

Ce relevé porte sur l’état local examiné ; les modifications ultérieures de l’intégrateur demandent leurs propres contrôles.


Correction de l’intégrateur après ce relevé : les pourcentages .pv[data-t][role=button] répondent désormais à Entrée/Espace ; contrôle prévu dans test_infobulles_prototype_ui.py. Les aides natives des commandes générales et les titres accessibles SVG sont hors des fiches médicales ; les titres natifs des mots du glossaire et liens médicaux CK ont été retirés.
