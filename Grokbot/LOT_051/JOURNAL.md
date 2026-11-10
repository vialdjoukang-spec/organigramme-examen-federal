# LOT 051 — journal de la refonte

Date : 2026-11-10. Branche `grok/refonte-lot-051`. Pas de pull request, pas de fusion. Arrêt après DX.1 pour l’audit de Bitunder.

## E0 — collision

Lecture seule des branches `origin/claude/lot-051` et `origin/grok/lot-051-bande`. `outils/mere.py` n’a pas été exécuté : il écrit hors de `Grokbot/LOT_051/`. L’ancien HTML d’environ 11 Ko a été retiré du lot. Aucun fichier de `PROMPT_Casern/`, `outils/`, `.github/`, ni des autres dossiers d’IA n’a été modifié.

## E1 — liste gelée

`LISTE_DX_CANONIQUE.md`. Porte P1 dans `_travail/PA/gel_p1.json`. SHA-256 du texte hors ligne de signature : `08889f8f47fb9a91502a50aeef06723f6b69eb498065aac39f62469bace1e9c2`. Dix diagnostics, fréquence décroissante. La maladie coronarienne (12,5 %) garde le rang E1. L’embolie pulmonaire, sans pourcentage de premier recours dans les extraits, reçoit le rang E2.

## E2 — sources

Textes intégraux dans `_travail/evidence/` :

- Verdon 2007, BMC Family Practice 8:51, PMC2072948, https://europepmc.org/articles/PMC2072948
- Ronga 2012, BMC Family Practice 13:74, PMC3444903, https://europepmc.org/articles/PMC3444903
- Bösner 2013, BMC Family Practice 14:154, PMC3853238, https://europepmc.org/articles/PMC3853238
- Haasenritter 2015, Croatian Medical Journal 56(5):422-430, PMC4655927, https://europepmc.org/articles/PMC4655927
- Gencer 2010, BMC Medicine 8:9, PMC2832616, https://europepmc.org/articles/PMC2832616
- Irfen Dolo / Irfen Dolo forte, Mepha Pharma AG, Swissmedic 67372, mise à jour décembre 2024
- Dafalgan, UPSA Switzerland AG, Swissmedic 47503, 47505, 56318, mise à jour juillet 2026

Consultation : 2026-11-10. Paquets : `_travail/PA/paquet.json` et `_travail/DX.1/paquet.json`.

## E3 — contrats

`_travail/PA/contrat.json` (préfixe `pa`) et `_travail/DX.1/contrat.json` (préfixe `dx1`). Quatorze titres µ3. Sécurité : E1 coronarien, E2 embolique, palpation non spécifique, ibuprofène contre-indiqué au troisième trimestre et plafonné à 1200 mg par jour sans ordonnance.

## E4 à E7 — rédaction

Fragments `p01.html` à `p14.html`. Phase A : 15 fenêtres, accent brique `#6E2A22`, cliché ECG 12 dérivations en double vue (sus-décalage en V2, V3 et V4). DX.1 : 10 fenêtres, accent forêt `#0F4C2A`, planche de Gray au point 3 et radiographie thoracique de face au point 9. Bande latérale fixe, progression au défilement, section active, même gabarit, couleur d’accent différente. Fonds chauds, texte `#1a120c`. Aucune phrase « le médecin ».

## E8 — assemblage

`LOT_051_Phase_A_V0.html` : 112 531 octets. `LOT_051_Phase_B_V0_DX.1.html` : 107 862 octets. Sommes dans `MANIFESTE.json`. Le style d’assemblage à fond bleu-gris a été remplacé, dans les fichiers du lot seulement, par la palette chaude. `outils/assembler.py` n’a pas été modifié.

## E9 — controle3

`python3 outils/controle3.py` sur les deux HTML ensemble, `--min 100000 --max 150000 --points 14`, paquet DX.1. Verdict VERT pour les deux. Rapport : `_travail/controle.json`. Phase A : 286 phrases, connecteurs 52 %. DX.1 : 306 phrases, connecteurs 34 %. Aucun défaut rouge ni orange.

## E10 — audit médical indépendant

Un auditeur distinct a d’abord bloqué trois formulations. Elles ont été corrigées : le point douloureux et quatre caractères laissent le syndrome plausible (spécificité 0,54) sans le poser ; l’ibuprofène des deux premiers trimestres reste réservé à la nécessité absolue, à la dose la plus faible et à la durée la plus courte ; l’infection haute, l’œsophage, l’hypertension et la plèvre ne sont plus attribués au seul extrait suisse de 2007. Relecture du même auditeur : non bloquant. Il signale que l’association à un autre anti-inflammatoire « doit être évitée » dans l’information suisse : le DX.1 dit désormais « est donc à éviter ».

## Arrêt

DX.2 à DX.10 ne sont pas rédigés. Aucune pull request. Aucune fusion.

## fix051c — ré-audit (commit 38dbbe5e6)

Rangs E réordonnés (E1 pneumothorax sous tension, E2 maladie coronarienne, E3 dissection, E4 embolie) ; arbre ouvert sur une porte d’instabilité vitale ; angioscanner de dissection (Wikimedia Commons, CC BY-SA 3.0) au point 9 ; question finale ajoutée ; règle 6 de sélection dans la liste.

## fix051d — contre-vérification

Question finale : « oui » appuyé sur le tableau d’ouverture complété (signe, examen, conduite) ; la Phase B n’est plus qu’un approfondissement. Acide acétylsalicylique : indication et dose de l’AIPS Aspirine® Cardio (n° 51795, 200 à 300 mg) ; Aspégic® présenté hors AIPS, selon les HUG ; contre-indication aiguë limitée à l’allergie connue, diathèse hémorragique et hémorragie digestive selon l’AIPS ; phrase « dose selon le protocole SMUR » retirée. Contrôle de la dissection avant toute aspirine (point 4, fenêtre SCA, arbre, point 13) ; si suspicion, aucun antithrombotique et 144. Sortie de la porte d’instabilité : 144, oxygène, monitorage, voie veineuse, patchs, puis cause ciblée (pneumothorax sous tension, embolie massive, tamponnade, trouble du rythme). Carte ECG : coronaire droite, 7 % d’ondes Q nouvelles ou de sus-décalage ST. AIPS Aspégic® daté de décembre 2025. Doses de la péricardite : « protocole local », faute d’extrait ESC accessible. Tableau comparatif à 15 px calculés. Planche de Gray retirée de la Phase A pour la taille (fichier conservé pour DX.1 et DX.9). Liste : règle 6 reformulée, justification de E3 par les antithrombotiques ; ordre et titres inchangés ; SHA recalculé dans `gel_p1.json`. Phase A : 147 219 octets, controle3 VERT.
