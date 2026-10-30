# Cahier des charges — prototypes de format (ordre de Vial du 30.10.2026)

Chapitre retenu : LOT_016 DX.10 « Insuffisance surrénalienne primaire (maladie d'Addison) », diagnostic différentiel du SSP G16 « Perte de poids, perte d'appétit ».
Source unique du fond : `LOT_Claude_Finaux/LOT_016/LOT_016_Phase_B_V0_DX.10.html` (138 Ko, audité deux fois, sources et AIPS vérifiées). Cours du SSP : `LOT_Claude_Finaux/LOT_016/LOT_016_Phase_A_V0.html`.

## Interdits
- Aucun fait, chiffre, dose, seuil ou source qui ne figure pas déjà dans le fichier source (on retire, on reformule, on regroupe ; on n'ajoute rien de non sourcé). Les citations AIPS restent mot pour mot entre guillemets.
- Aucune phrase nominale ni fragment télégraphique : des phrases complètes, grammaticalement correctes, courtes mais liées par des connecteurs logiques (car, donc, puis, ensuite, cependant, en revanche, ainsi, c'est pourquoi, lorsque, si…alors). Un texte normal, agréable à lire.
- Aucune redondance avec le cours du SSP (Phase A) : tout ce qui vaut pour toute perte de poids (épidémiologie générale de la perte de poids, GLIM, bilan de base commun, démarche générale, dénutrition, renutrition générale) est supprimé et remplacé, si utile, par une phrase de renvoi : « voir le cours Perte de poids, perte d'appétit ». Ne reste que ce qui est SPÉCIFIQUE à la maladie d'Addison comme cause de perte de poids.
- Aucun JavaScript, aucun `title=`, aucune espace insécable.

## Les 14 parties, en plan d'ouvrage sérieux
Ordre : titre ; encadré « L'essentiel » (4 à 6 phrases) ; sommaire en flux normal (liste numérotée cliquable, JAMAIS collée en haut de l'écran, ni fixe, ni « au plafond ») ; puis 1 Définition, 2 Épidémiologie, 3 Physiopathologie (avec les rappels d'anatomie et de physiologie de l'axe corticotrope et de la glande surrénale), 4 Démarche diagnostique, 5 Anamnèse et drapeaux rouges, 6 Examen physique, 7 Approche syndromique, 8 Diagnostic positif, 9 Examens complémentaires, 10 Arbre décisionnel, 11 Prise en charge en Suisse (urgence, traitement de fond, suivi, éducation), 12 Prévention, 13 Points clés, 14 Pièges d'examen ; sources numérotées ; mention « Contenu établi à partir des sources citées ; non validé cliniquement par un médecin. ».
Titres de parties `<h2>` numérotés, sous-titres `<h3>`. Mise en page de livre : colonne de lecture d'environ 70 caractères, interlignage confortable, marges, typographie soignée, thème clair et sombre, lisible à 390 px.

## Vraies fenêtres (problème 1 et 3)
« Fenêtre » = une vraie fenêtre comme celle d'un logiciel : un cadre flottant centré au-dessus de la page, fond de page assombri, barre de titre (titre de la fenêtre + bouton de fermeture ✕ à droite), corps défilant, ombre portée, coins arrondis. Implémentation sans JavaScript : API HTML `popover`.
- Déclencheur : un mot ou groupe de mots DANS la phrase, `<button type="button" class="terme" popovertarget="w-…">mot</button>`, stylé comme un lien de lecture (soulignement pointillé, petite icône ⧉), jamais un bouton gris.
- Fenêtre : `<div id="w-…" popover class="fenetre"><div class="barre"><span>Titre</span><button type="button" popovertarget="w-…" popovertargetaction="hide" aria-label="Fermer">✕</button></div><div class="corps">…</div></div>` placé après le `</p>` ; CSS : `position:fixed; inset:0; margin:auto; width:min(92vw,44rem); max-height:80vh; overflow:auto` ; `::backdrop` assombri.
- Mots dépliables : pour une précision d'une ou deux phrases, `<details class="deplier"><summary>terme</summary>…</details>` en ligne.
- Densité : au moins une fenêtre ou un dépliable par partie où un détail utile (dose complète, critère, tableau, rappel anatomique, citation AIPS longue) alourdirait la phrase principale. Le texte principal se lit d'un trait sans ouvrir de fenêtre ; les fenêtres approfondissent.

## Trois versions demandées
- V1 « sans redondance » : tout le spécifique de la source, débarrassé du commun avec la Phase A, réécrit en prose correcte avec fenêtres ; moins de 100 000 octets.
- V2 « cours court + notions courtes » : texte principal le plus bref possible (viser 25–45 Ko au total), chaque notion en une à trois phrases, l'approfondissement en fenêtres ; le seuil est la taille minimale pour un score d'au moins 90/100 à l'examen et 90/100 en prise en charge quotidienne.
- V3 « choix de l'expert » : la version que l'auteur juge la meilleure pour l'étudiant (examen fédéral et pratique quotidienne), en respectant toutes les règles ci-dessus ; taille libre sous 100 000 octets, justifiée.
