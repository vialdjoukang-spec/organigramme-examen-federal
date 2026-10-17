# HANDOFF · passation entre sessions

Chaque agent ajoute sa section en tête, selon le modèle de l’annexe E2 du plan. Aucune donnée personnelle n’entre dans ce fichier public.

## Hermès · nerfs crâniens et CK, NC-0 interaction · 17.10.2026, Europe/Zurich
État       : Patch 0012 (feat/ck-interaction, PR #24), rejoué après le 0011 d’Atlas. Il apporte : le lieur gloLink, branché sur CK_GLO_INDEX.e = [id, type, libellé, formes, tranche] (index chargé à l’inactivité) ; la pile de fenêtres imbriquées (5 niveaux, « ← Retour », fil d’Ariane, aucun lien vers un terme déjà ouvert ; survol, clic, clavier, toucher, panneau bas sur mobile) ; les types tipFor glo|id, syn|id, hyp|id[|pec], loc|module|A|B et nc|id|vue. Les données se chargent à la demande par ckLoad/ckGlo : la fenêtre affiche « Chargement… », puis se redessine sur place. Le réglage « Fond doré » a quitté l’en-tête (champ caché conservé). tests/test_ck_ui.py : 66/66 (données d’essai et données réelles de main) ; suite 199/199 ; test_ck 61/61 ; G1 à G7 réussis.
Partage    : Janus est propriétaire de tests/test_ck.py (données, schémas, gardes). Hermès est propriétaire de tests/test_ck_ui.py (interaction, pile de fenêtres, gloLink, couches SVG, ordinateur et mobile). Personne ne modifie le fichier de l’autre sans le prévenir.
Contrat    : Pour les schémas, l’ordre est CK_NC[id].vues (face, profil, trois_quarts ; la clé « 34 » est acceptée comme alias), puis CK_SVG[chemin], fourni par assets/nc/<id>.js et compilé par tools/nc_svg_js.py (la CI schemas fait --check : après toute retouche d’un SVG, relancer l’outil). Les états viennent de data-etats de Dédale : les boutons Trajet, Branches, Fonctions et Lésions affichent [data-etat=X] par l’attribut display et cochent les couches de data-etats[X] ; l’utilisateur règle ensuite chaque couche. Le crédit est celui que le SVG affiche. Repères numérotés (contrat Dédale, avant fusion de sa PR) : g.nc-num avec data-num, data-nom et data-glo facultatif. Le survol (ordinateur), le focus et le toucher affichent une bulle « n · nom » (avec la définition courte si elle est chargée) ; le clic, le toucher ou Entrée ouvrent glo|<data-glo> au niveau suivant de la pile (pas au niveau 5, ni si la fiche est déjà ouverte). La case « Légende numérotée » règle la couche legende (id ou data-couche) ; une couche absente du SVG n’a pas de case. Vues affichées : Face, Profil, Trois quarts. Sans JS, le schéma retombe sur <img> et les couches sont désactivées. Sous le schéma s’affichent les sites lésionnels (liens vers syn et hyp) et l’anatomie repliée.
Prochaine  : Apollon : dans le patch 0005, renommer « Par défaut (réglage « Fond doré ») », puisque le réglage n’est plus visible ; styliser les .ck-* (variables CSS seulement). Dédale : certaines étiquettes de la vue de face se touchent (captures ordinateur et mobile, n° 34 et 35). Atlas : loc.js est vide, donc la synthèse locale n’est testée que sur les données d’essai.
Pièges     : Le lieur ignore titres, boutons, champs, .tw, #grid et .blk, mais il lie le texte des gestes cochables (label[data-t]) : le clic ouvre alors le terme sans cocher la case. Un sigle (2 à 6 majuscules) se compare avec la casse. Aucun « window.CK_ » ni « glo|<id> » littéral dans app_v2.html (test_ck_socle et Lyncée). Le rouge passe seulement par .urg ou [data-bloquant] (G7). Phrase : ckP() n’ajoute un point que s’il manque.
À vérifier : Les mots d’interface « Foramens » et « Sites lésionnels » doivent recevoir une entrée de glossaire (Hippocrate).

## Podalire · chaîne clinique du VII (NC-1) · 17.10.2026, Europe/Zurich
État       : feat/nc07-chaine : data/ck/syn.json (5 syndromes vii-site1 à vii-site5, module neuro-nc), hyp.json (12 hypothèses : avc-ischemique et avc-hemorragique bloquantes, tumeur-cerebrale, bell, zona-oticus, schwannome-vestibulaire, fracture-rocher, otite-moyenne-compliquee, cholesteatome, neuroborreliose, tumeur-parotide, traumatisme-facial), nc.json (nc07 : noyaux, trajet, foramens, territoires, 5 lésions, vues), 10 sources ajoutées à src.json ; G1 à G7 conformes, Lyncée 0 terme nouveau. La branche contient la PR #22 (glossaire lot 01), dont les identifiants glo sont cités.
Prochaine  : Galien relit le diff (audit:galien), définit les termes listés dans journal/nerfs-ck.md et lit les posologies « À vérifier » ; Podalire source les points « À vérifier » ; Hermès affiche hyp, syn et nc dans tipFor.
Sources    : HUG, Protocole PFP v1.2 du 04.04.2023 ; DGN/SNG S2k 030-013 (2022) ; DGN S3 030-071 Neuroborreliose (2024) ; ESO IVT (2021) ; ESO-ESMINT thrombectomie (2019) ; ESO-EANS hémorragie intracérébrale (2025) ; EANO schwannome vestibulaire (2020) ; EANO gliomes (2021) ; ESMO-EURACAN glandes salivaires (2022) ; lus le 17.10.2026.
Pièges     : G1 lit « 30 mL » comme une dose : un volume d’hématome s’écrit « 30 millilitres ». Podalire n’écrit aucune posologie : une dose passe par dose_ref vers doses_ch.json, sinon la phrase « La posologie … reste À vérifier ». Les identifiants syn et hyp sont cités par nc/annot/nc07.yml : ne pas les renommer. Les sigles d’éditeurs des titres de sources sont exclus de Lyncée avec motif (qa/termes_exclus.txt).
À vérifier : imagerie et chirurgie de la fracture du rocher, de l’otite compliquée, du cholestéatome et des plaies des rameaux ; précautions des produits de contraste ; « atteinte d’un seul rameau évoque une tumeur » (L5) ; posologies de la corticothérapie, de la thrombolyse et des antibiotiques.

## Hippocrate et Galien · NC-0 glossaire CK et audit médical · 17.10.2026, Europe/Zurich
État       : feat/ck-glossaire-lot01 (sur feat/ck-socle) : glo.json 100 entrées (70 signes, 25 syndromes, 3 examens, 2 termes ; 6 « À vérifier »), src.json 19 sources, doses_ch.json 3 lignes AIPS ; 29 fautes corrigées par les automates régionaux (0 critique, 3 majeures, 26 mineures), qa/audit/RAPPORT_FAUTES.md ; G1 à G7 et Lyncée réussissent.
Prochaine  : Asclépios contre-lit doses_ch.json et qa/posologies.md ; Vial coche qa/validation-vial-glo-lot01.md ; Hippocrate écrit le lot 02 (hyposmie, quadranopsie, cécité, hémiparésie, hypotonie, méningite…).
Sources    : CEN (chapitre 9, sémiologie analytique et topographique), HUG protocole PFP v1.2 du 04.04.2023, SFE item 244, HAS PNDS Cushing 2022, AIPS Valtrex® (12.2025) et Prednisone Streuli® (06.2026), lus le 17.10.2026.
Pièges     : Une correction d'audit passe par galien_region.py corriger --plan <fichier.yml> (le texte « avant » figure une seule fois) ; puis galien_region.py registre écrit fautes.jsonl avec le hachage réel et ne réécrit jamais une ligne existante. Une définition du glossaire ne doit contenir ni son libellé ni ses alias (Lyncée).
Pièges     : Les doses ne se lisent qu'à la main, une page AIPS par produit ; aucune extraction du Compendium ni de Swissmedic. Une dose hors AIPS n'entre pas dans doses_ch.json.
À vérifier : Rebaser sur main après la fusion de la PR #20. Les ajouts swissmedicinfo-pro.ch, cen-neurologie.fr et sfendocrino.org attendent l'accord de Vial et d'Argos.

## Atlas et Janus · NC-0 socle CK et audit de niveau 1 · 17.10.2026, Europe/Zurich
État       : feat/ck-socle : schémas data/ck/schema (src, glo, sig, syn, hyp, nc, loc, doses_ch), données vides et conformes, tools/ck_build.py → assets/ck/*.js (742 octets), patch 0011 (ckLoad, ckGlo, index à l’inactivité ; +659 octets dans app_v2.html), budgets étendus, Lyncée et sa référence (3 849 termes), G1 à G7 (tools/audit/niveau1.py, artefact audit-flags), Alétheia, rapport_fautes.py, nc_svg_check.py ; tests : test_ck.py 61/61, test_ck_socle.py 12/12, suite 133/133, gardes 5/5.
Prochaine  : Hermès branche tipFor et gloLink sur ckLoad/ckGlo/CK_GLO_INDEX ; Hippocrate remplit glo.json par lots et resserre la référence (--update) ; Galien remplit doses_ch.json et fautes.jsonl ; Dédale dépose assets/nc/*.svg et credits.json (couches trait, nerf, legendes ; licence_derivee CC BY-SA).
Sources    : Plan Nerfs crâniens et CK, sections 3, 4, 8 et 9 ; propositions/audit-medical.yml et domaines.yml (17.10.2026).
Pièges     : Après toute modification de data/ck, lancez python3 tools/ck_build.py : la CI échoue si assets/ck n’est pas à jour. Le nom de variable suit le fichier : glo-index.js → window.CK_GLO_INDEX, glo-a.js → window.CK_GLO_A.
Pièges     : Toute demande de fusion qui ajoute un terme médical dans TIP, NOT, GES, le HTML statique ou data/ck échoue à G4 tant qu’il n’est pas défini dans glo.json ou exclu avec motif ; une dose ajoutée dans TIP/NOT/GES échoue à G1 sans « À vérifier » dans le même texte.
Pièges     : G6 lit tools/audit/verbes_conjugues.txt.gz ; on le régénère par tools/audit/verbes_gen.py, jamais à la main.
À vérifier : Liste G6 à régénérer depuis Lexique 3.83 (site indisponible le 17.10.2026) ; filtre MeSH pour le tri ; domaines escardio.org, has-sante.fr, escmid.org (Argos).

## Dédale · schémas des nerfs crâniens (NC-0, pilote VII) · 17.10.2026, Europe/Zurich
État       : feat/nc-numeros : retour de l’utilisateur « trop saturé d’annotation ; numéro fléché et cliquable avec le nom de la structure, pour aérer au maximum ». Les 3 vues assets/nc/nc07-{face,profil,34}.svg (crâne au crayon, nerf jaune #FFC400 cerné de #5a4500, 8,5 px hors tout sur 800 px) n’ont plus aucun texte sur le dessin, sauf le titre : chaque structure porte un petit numéro cerclé fléché, aéré, jamais sur le nerf ; les noms sont dans une légende numérotée en 2 colonnes, en petits caractères, sous le dessin (couche « legende »). États trajet (8 repères), branches (6), fonctions (5), lésions (5, site 1 en rouge). verifier.py V9, V11, V13 à V15 ; tests/test_dedale.py 30/30.
Contrat    : chaque repère est <g class="nc-num" data-num="n" data-nom="nom de la structure" data-glo="identifiant glo.json, s’il existe" data-ref="id nc/annot" tabindex="0" role="button" aria-label="n · nom">, avec trait de rappel path.ld, pointe path.ah, cercle circle.cr (r = 14, trait 2,2 px, fond blanc), numéro text.nm (gras, 18 px sur 800 px). Classe « u » en plus (cr, nm, ld, ah) = site d’urgence, rouge. Les repères d’un état sont dans g.numeros[data-etat][data-couche] ; numéro = rang dans nc/presets/<nerf>.yml, identique dans les 3 vues (le même numéro désigne la même structure ; un repère absent d’une vue garde son numéro).
Contrat    : la légende est g#legende[data-couche="legende"], une g.legende[data-etat] par état (text.lg, numéro dans tspan.n) ; la couche « legende » figure dans data-etats de chaque état, l’application peut la masquer et afficher le nom au toucher ou au clic d’un .nc-num (data-nom, infobulle de glossaire si data-glo). Le crédit court (g#credit) reste toujours visible. Le manifeste assets/nc/nc07-presets.json liste par vue et par état : num, ref, nom, glo.
Prochaine  : Athéna transmet le contrat à Hermès (clic ou toucher → nom, infobulle de glossaire) ; Vial valide les 3 vues ; même chaîne pour les autres paires après portage de freestyle.py en mode ajout seul.
Sources    : Z-Anatomy License.txt (CC BY-SA 4.0) ; nc/annot/nc07.yml (Ariane) ; data/ck/glo.json (Hippocrate) ; lus le 17.10.2026.
Pièges     : Ne jamais ouvrir le modèle complet (11 Go) : freestyle.py le fait, il est gelé ; crane.py et masques.py ajoutent seulement les objets utiles. Freestyle n’est pas rejouable à l’octet : la CI rejoue annoter.py depuis nc/trait versionné, pas Blender. svgo applique les transformations aux chemins du nerf et des noyaux : leurs épaisseurs s’écrivent en px de l’image dans la feuille de style (annoter.py échoue sinon). svgo trie les attributs : un test ne cherche jamais un ordre d’attributs.
À vérifier : F2 (fond du méat) et repères a_verifier d’Ariane ; le repère 1 des lésions (cortex moteur) pointe dans la voûte vide (cerveau non dessiné) ; data-glo n’existe que pour les sites lésionnels (paralysie faciale centrale ou périphérique, hyperacousie) : le glossaire n’a pas encore les structures anatomiques ; numéros de 18 px (8,1 px à 360 px) et légende de 22 px (9,9 px à 360 px) sous le minimum de 13 px de l’ancienne règle, par choix (cercle de 13,5 px à 360 px).

## Hermès · calendrier et sauvegarde automatique · 17.10.2026, Europe/Zurich
État       : PR #15 fusionnée dans main le 17.10.2026 à 13:26 (commit de fusion 3c9b878, sans écrasement) ; Pages publie la même empreinte que main ; tests/test_calendrier.py rejoué contre le site public : 32/32, aucune erreur de console. Patch 0009 (PR #18, fusionnée le 17.10.2026 à 13:55) : la recherche trouve aussi un SSP par ses diagnostics différentiels et ses notions (NOT), avec le titre trouvé sous le nom ; suite 119/119, gardes 5/5.
Prochaine  : Apollon (PR #16) pose les teintes de jour et les bandes de séance pâles : data-wd (1 = lundi … 7 = dimanche) existe désormais sur .hd et .col, y compris en vue « Jour » ; il remplace donc nth-child par [data-wd] et peut teinter la colonne du jour. Mnémosyne réutilise showTip/tipToggle inchangés.
Sources    : MDN StorageManager.persist(), IndexedDB, File System Access API ; WebKit « Full Third-Party Cookie Blocking and More » (plafond de 7 jours), lus le 17.10.2026.
Pièges     : Tout appel à lsSet déclenche svTouch ; le miroir ne démarre qu’après le contrôle de démarrage (svReady), pour ne jamais écraser la copie de secours par un état vide. test_export simule l’effacement Safari en supprimant aussi IndexedDB.
Pièges     : Dans les tests mobiles, la barre d’onglets collante (≈ 200 px sur 412 px de large) masque le haut de l’écran ; faites défiler avec behavior:'instant' et un décalage.
Pièges     : Patch 0010 : blkFit() mesure chaque bande après renderGrid (et au redimensionnement, aux polices chargées) ; il pose --cl (lignes qui tiennent), .mini (moins d’une ligne : une seule ligne compacte) ou .nodu (durée masquée si elle cache l’horaire). Une règle CSS nouvelle sur .blk ne doit pas fixer -webkit-line-clamp en dur. Iris échoue sur tout texte coupé sans ellipse ni texte complet (CLIP_JS, état cal-bandes-semaine et cal-bandes-jour).
Pièges     : fz() renvoie un tableau portant R.why (code → titre trouvé dans NOT) ; le second niveau n’est consulté que si le nom et le code ne donnent rien pour ce SSP.
Pièges     : Un conflit dans app_v2.html ne se résout jamais à la main : reprenez la version de main, puis rejouez votre patch (skill ssp-fusion-patch).
À vérifier : Le fichier automatique n’existe que sur Chromium de bureau ; ailleurs le bouton reste caché. Essai réel sur iOS Safari (persistance refusée, versions) par le titulaire.

## Asclépios · examen physique · 17.10.2026, Europe/Zurich
État       : feat/asclepios-examen : GES en 3 axes (13 régions, 6 systèmes, 3 populations ; 22 entrées, 315 gestes), sous-régions, ordre strict, 7 gestes nouveaux sourcés, 12 doublons en renvois bidirectionnels, 19 croquis (assets/cs, credits.json) ; TIP champ 5 structuré pour 198 SSP, 15 marqués « À compléter », 35 laissés tels quels (contenu non clinique d’examen). Patch 0008, tests/test_examen.py (16 contrôles), Pages publie assets/.
Prochaine  : Vial valide les croquis (valide_par_vial) ; Asclépios relit les 113 blocs « Autres éléments ciblés » et rédige les 15 champs vides avec sources.
Sources    : StatPearls/NCBI (NBK271, NBK551612, NBK549844, NBK538499, NBK558918, NBK256, NBK513250, NBK557639, NBK557862, NBK459125, NBK470595, NBK549859, NBK544226), PMC3993046, PMC5890131 ; Füeßl/Middeke (pages à vérifier) ; Wikimedia Commons et Open-i lus le 17.10.2026.
Pièges     : La progression des gestes est indexée par it.k (clé historique « région_index ») : ne jamais renuméroter k. Les scripts tools/asclepios/*.py refusent de tourner deux fois (garde d’idempotence). Le champ 5 est un format compact (§ région, ¶ phase, • élément, @ puces) rendu par exFmt().
À vérifier : Pages Füeßl/Middeke des 7 gestes nouveaux ; classement automatique des éléments du champ 5 (relecture humaine par échantillon).
Classes    : .ex-axe/.ex-axe__h (rail des régions), .ex-region/.ex-region__h, .ex-phase[data-ordre=1…6|M|N], .ex-items, .ex-fig/.ex-fig__cap/.ex-fig__credit, .ex-xref/.ex-chip[data-gx], .ex-av, .ex-flash — conformes à qa/apollon/spec.md § 7 ; data-ordre « M » (Mesures) et « N » (Neurologique) s’ajoutent aux valeurs 1 à 6.
## Thémis · Exigences 2027 · 17.10.2026, Europe/Zurich
État       : L’onglet « Exigences » compte 46 cases stables (data/EXI.json), un bandeau 2027 et des badges « À vérifier auprès de la MEBEKO » ; SESSION centralise les dates ; patch 0004 ; tests/test_exigences.py (13 contrôles) ; suite 69/69, gardes 5/5.
Prochaine  : Thémis met data/SESSION.json à jour (tools/build_exi.py, puis json_inject.py inject SESSION) dès que l’OFSP publie les dates 2027.
Sources    : research_exigences.md (S1 à S12, N1), lues le 17.10.2026.
Pièges     : Les coches vivent sous « x:<id> » dans S.exi, à côté des clés a… (Attendus) et cp… (CS) ; on ne renumérote jamais un identifiant.
À vérifier : A3, A4, C4, C6, C7, C8, C10, D2, D5, E2 et E3 attendent une réponse de la MEBEKO ou une publication de l’OFSP.

## Atlas · sauvegarde · 17.10.2026, Europe/Zurich
État       : Le chantier export/import est sur feat/sauvegarde (PR #11) : patch 0003, CSS du bandeau dans le style de head, tests/test_export.py (13 contrôles) ; suite locale 56/56 et gardes 5/5.
Prochaine  : Athéna fusionne PR #11 dès que la CI (garde, html, tests) est verte.
Sources    : Ticket #5 ; plan v2 fiche Atlas ; MDN Storage quotas ; WebKit 7-Day Cap (lus le 17.10.2026).
Pièges     : Toute règle CSS nouvelle dans le style de body crée des erreurs Nu ; le bandeau #bak doit rester dans le style de head.
À vérifier : Le rappel d’export à sept jours et le message de stockage plein sont couverts par tests/test_export.py.

## Argos · veilles · 17.10.2026, Europe/Zurich
État       : Ve1 (OFSP) et Ve2 (healthreg) sont dans main (PR #4 fusionnée) ; workflows veille-ve1.yml et veille-ve2.yml actifs.
Prochaine  : Argos teste la faisabilité de Ve3 (flux Swissmedic) et de Ve4 (XML Refdata) avant le 29.11.2026.
Sources    : robots.txt de bag.admin.ch et de healthreg-online.admin.ch lus le 17.10.2026 ; plan v2, section 11 et annexe D.
Pièges     : main est protégée ; veille/etat.json vit donc sur la branche veille-etat, que personne ne doit fusionner ni supprimer.
À vérifier : Janus contrôle vers le 17.11.2026 que la réactivation mensuelle (PUT …/enable) garde les veilles actives.

## Mnémosyne · mémorisation · 17.10.2026, Europe/Zurich
État       : data/MEM.json contient les douze méthodes et les références M1 à M24, reprises mot pour mot ; les 24 DOI se résolvent (PR #3).
Prochaine  : En phase 2, après la fusion d’Hermès, Mnémosyne ajoute data-t="m|id" et les trois réglages, sur feat/memo-evidence.
Sources    : research_memorisation.md du 17.10.2026 ; doi.org, le 17.10.2026.
Pièges     : tools/build_mem.py régénère MEM.json ; on corrige la note source puis on relance le script, sans retoucher le JSON à la main.
À vérifier : Janus rejoue le contrôle des DOI sur la liste references de MEM.json.

## Athéna · coordination · 17.10.2026, Europe/Zurich
État       : La phase 0 est livrée ; les tickets de phase 1 (#5 à #10) sont ouverts ; MEM.json et les veilles Ve1/Ve2 sont dans main ; les dix skills sont dans la bibliothèque partagée.
Prochaine  : Fusionner PR #11 (Atlas) quand la CI est verte ; la version datée de phase 0 attend encore l’accord du titulaire (I6).
Sources    : J’ai lu le plan v2 (sections 1, 3, 4, 10, 12 et annexe E), le 17.10.2026.
Pièges     : Une ligne d’app_v2.html dépasse 4,8 millions de caractères ; les expressions régulières y expirent, et seul str.find fonctionne (tools/_app.py).
Pièges     : main exige une demande de fusion et les contrôles garde, html et tests, même pour l’administrateur ; aucun push direct n’aboutit.
Pièges     : GES est suivi de « ;const GES_SRC=… » sur la même ligne ; tools/_app.py délimite donc les constantes JSON par json.raw_decode.
À vérifier : Le jeton gh n’a pas le droit « project » ; le tableau Projects attend `gh auth refresh -s project` par le titulaire du compte.

## Prompt de continuité (annexe E3)
Tu es <Agent>, l’agent chargé de <spécialité> dans le projet « Organigramme Examen fédéral ».
Lis d’abord HANDOFF.md, ETAT.md et journal/<chantier>.md, puis ta fiche de mission (plan v2, section 4).
Ne lis jamais app_v2.html en entier : applique ssp-extrait-cible, ssp-patch et ssp-json-data.
Vérifie chaque modification avec ssp-tests, et contrôle chaque texte avec ssp-verite.
Ne modifie jamais app.html. N’utilise que des sources suisses et européennes, et des images réelles.
Respecte la règle universelle : le projet cible doit avoir un résultat de HAUTE QUALITÉ ; l’usage des jetons doit être raisonnable et optimisé, et tout gaspillage est formellement interdit ; l’économie de jetons est autorisée si et seulement si elle ne dégrade pas la qualité du travail.
Avant de t’arrêter, mets à jour HANDOFF.md, ETAT.md et ton journal.
