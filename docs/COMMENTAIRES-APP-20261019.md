# Commentaires techniques de l’application

Les commentaires suivants proviennent de app_v2.html. Ils sont déplacés ici pour respecter le budget de taille sans modifier les données médicales ni les jetons du code. Le patch rejouable0090 conserve chaque saut de ligne et refuse un ancrage manquant ou répété.

```text
/* Organigramme à mémoire permanente : un poste de travail en quatre vues (Calendrier, Vitrine, Calculs, Exigences), identité dorée de l'Examen fédéral · Version SSP. */
```

```text
/* Fond pâle par défaut */
```

```text
/* ---------- ATLAS : sauvegarde (export, import, erreurs de stockage) ---------- */
```

```text
/* Format v1 : {format:"organigramme-examen-federal",version:1,exporte:ISO,cles:{"orga-…":"<valeur brute>"}} ; orga-bak (date du dernier export) n’est pas exporté. */
```

```text
/* v1 : format initial ; une version future convertira ici les anciennes clés. */
```

```text
/* ---------- HERMÈS : sauvegarde automatique fiable (miroir IndexedDB, versions, persistance, fichier) ---------- */
```

```text
/* Chaque écriture réussie (lsSet) programme svFlush : copie « cur » dans IndexedDB avec somme FNV-1a, version horaire au plus, 30 versions gardées. */
```

```text
/* ---------- MNÉMOSYNE : persistance (base partagée, repli local) ---------- */
```

```text
/* ---------- Nomenclature et recherche ---------- */
```

```text
/* ---------- CHRONOS : grille au quart d'heure ---------- */
```

```text
/* ---------- HERMÈS : calendrier interactif (clic, plage, recherche floue, déplacement, durée, toucher, clavier) ---------- */
```

```text
/* Fenêtre de création rapide */
```

```text
/* Clic, plage, déplacement et durée */
```

```text
/* Clavier : flèches = déplacer de 15 min ou d’un jour ; Maj + flèches = durée ; Entrée = détails */
```

```text
/* ---------- ATLAS : agrégats ---------- */
```

```text
/* ---------- LOGOS : calculs ---------- */
```

```text
/* ---------- Exigences ---------- */
```

```text
/* ---------- Onglets et rendu ---------- */
```

```text
/* ---------- Affichage : intensité dorée, taille du texte ---------- */
```

```text
/* ---------- Mnémosyne : méthodes fondées sur les preuves (assets/memo/mem.js, chargé à la demande) ---------- */
```

```text
/* ---------- MNÉMÉ : mémorisation espacée ---------- */
```

```text
/* ---------- CS : plan en 6 phases ---------- */
```

```text
/* ---------- SCÈNE : générateur de scénarios IA ---------- */
```

```text
/* ---------- Journal des simulations CS ---------- */
```

```text
/* ---------- ATTENDUS : ce qui est noté, prérequis par épreuve ---------- */
```

```text
/* ---------- Notions CK : maîtrise notion par notion, objectif > 95 % ---------- */
```

```text
/* ---------- Chiron : stations CS (assets/st/, chargées à la demande) ---------- */
```

```text
/* ---------- Gestes d’examen physique ---------- */
```

```text
/* ---------- Import du résultat produit par l’IA ---------- */
```

```text
/* ---------- Infobulles : l’essentiel pour 100 % des points ---------- */
```

```text
/* Contrôles qui gardent leur propre action : un clic dessus n'épingle pas la fenêtre (le petit i et le mot souligné, eux, l'épinglent toujours). */
```

```text
/* ---------- HERMÈS · NC-0 : glossaire imbriqué (gloLink), pile de fenêtres, types CK (glo, syn, hyp, nc, loc), couches, vues et états des schémas ---------- */
```

```text
/* Données (Atlas, assets/ck/*.js, chargées par ckLoad et ckGlo du patch 0011) : CK_GLO_INDEX.e = [[id, type, libellé, formes, tranche], …] ;
   définitions par tranche (CK_GLO_A…) ; CK_SYN, CK_HYP, CK_NC, CK_LOC, CK_SRC, CK_DOSES_CH (objet par identifiant ou tableau).
   Schémas : CK_SVG[chemin du SVG] = texte SVG (assets/nc/ncXX.js, tools/nc_svg_js.py), états dans data-etats (Dédale). Aucune donnée ici. */
```

```text
/* Phrase : échappée, avec un point final seulement s’il manque (aucun « .. »). */
```

```text
/* Index du glossaire : formes pliées (sans accents ni casse) et sigles exacts (AVC) ; la plus longue forme l’emporte. */
```

```text
/* Chargement à la demande : la fenêtre s’affiche (« Chargement… »), puis se redessine sur place quand les fichiers sont là. */
```

```text
/* gloLink(racine, exclus, dansFenetre) : pose une clé de glossaire (type glo) sur la première occurrence de chaque terme par bloc ; ignore titres, liens, code,
   commandes, éléments déjà reliés et identifiants exclus (terme courant et ancêtres de la pile). Ne modifie aucune donnée (TIP, NOT, GES). */
```

```text
/* Pages : liaison à l’inactivité, par petits lots, sur les nœuds ajoutés au rendu ; jamais dans la fenêtre (liée à son ouverture). */
```

```text
/* Rendus des types CK. ckL : lien explicite vers une autre fenêtre (retiré s’il est déjà dans la pile ou au niveau 5). */
```

```text
/* Schémas : SVG en ligne depuis CK_SVG (assets/nc/ncXX.js), nettoyé ; états (data-etats) et couches réglables ; sinon image simple. */
```

```text
/* État X : [data-etat] visibles seulement pour X ; couches cochées d’après data-etats[X] (l’utilisateur peut ensuite les régler). */
```

```text
/* Couche c : tous ses groupes (#c ou [data-couche=c]) ; un groupe propre à un état (data-etat) ne s’affiche que dans cet état. */
```

```text
/* le SVG de Dédale porte déjà son crédit visible */
```

```text
/* Repères numérotés (Dédale : g.nc-num, data-num, data-nom, data-glo) : bulle « n · nom » après clic, toucher ou activation clavier ;
   clic, toucher ou Entrée ouvrent la fiche du glossaire au niveau suivant (même pile), sauf au niveau 5 ou si elle est déjà ouverte. */
```

```text
/* Pile de fenêtres : un terme ouvert depuis la fenêtre l’empile (5 niveaux au plus) ; « ← Retour » et le fil d’Ariane y reviennent. */
```
