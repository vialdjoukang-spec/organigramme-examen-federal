# Apollon · spécification de la présentation premium

Date : 17.10.2026 (Europe/Zurich). Portée : présentation seule. Le patch `tools/patches/0005-apollon-premium.py` ajoute `tools/patches/apollon.css` en fin du bloc de style principal. Il retire la feuille Google Fonts et ajoute `lang="fr"` sur `<html>`. Il ne change aucun texte, aucune donnée, aucun identifiant et aucun script.

> **Règle universelle.** Le projet cible doit avoir un résultat de HAUTE QUALITÉ. L’usage des jetons doit être raisonnable et optimisé, et tout gaspillage est formellement interdit. L’économie de jetons est autorisée si et seulement si elle ne dégrade pas la qualité du travail.

## 0. Directives du titulaire (17.10.2026, obligatoires)
1. **Texte justifié.** Les paragraphes, les descriptions et le corps de la fenêtre sont en `text-align: justify`, avec `hyphens: auto` et `lang="fr"` pour éviter les lézardes. Le texte reste aligné à gauche pour les libellés courts, les boutons, les onglets, les cellules de tableau, les listes et la colonne latérale étroite, ainsi que sous 360 px de largeur.
2. **Couleur parcimonieuse.** Le rouge est réservé à l’information capitale : erreur de stockage, retard d’échéance, action destructrice. Les titres (h1 à h3, titre de la fenêtre) sont en gras et noirs, ou dans l’encre la plus foncée en thème doré. La palette des familles est désaturée et sans rouge, la ligne « maintenant » du calendrier passe à l’encre, et le surtitre passe au gris.
3. **Bandeau d’en-tête.** Dans la fenêtre d’information, la partie (surtitre) et le titre sont au-dessus du contenu, sur une bande vert pâle (`--band`) séparée du texte par un filet. Le texte suit, complet avant d’être court. Le même motif s’applique aux bandeaux : la sauvegarde aujourd’hui, et le bandeau 2027 de Thémis dès sa fusion.

## 1. Principes
1. **Sobriété.** L’or sert d’accent rare (liens, bouton principal, repères), jamais de décor ni de titre. Le texte doré est foncé (bronze) en thème clair et clair en thème sombre, pour respecter le contraste AA.
2. **Hiérarchie par la typographie.** Les titres utilisent un serif humaniste, et le corps un sans-serif du système. Les chiffres sont en mono tabulaire.
3. **Surfaces calmes.** Les surfaces ont des bordures fines et des ombres douces à trois niveaux, et aucune couleur saturée hors des états.
4. **Zéro dépendance.** Les polices viennent du système. L’application s’affiche donc à l’identique en `file://` sans réseau et sur Pages, et le fichier ne prend aucun octet de police.
5. **Accessibilité d’abord.** Le contraste respecte AA, les cibles mesurent au moins 24 px (WCAG 2.2), l’anneau de focus est visible partout, et le mouvement réduit est respecté.

## 2. Jetons
| Jeton | Clair | Sombre | Usage |
|---|---|---|---|
| `--bg` | `#f5efe1` ↔ `#ffffff`, selon « Fond doré » | `#1a1812` ↔ `#0f0f0e` | fond de page |
| `--paper` | `#fffefb` | `#1a1813` | cartes, fenêtre |
| `--ink` | `#17150f` | `#f4eedf` | texte |
| `--mut` | `#575141` | `#cbc2ac` | texte secondaire (AA) |
| `--line` | `#e4dcc8` | `#38332a` | bordures |
| `--soft` | `#f3eddf` | `#24211a` | indicateurs, en-têtes de section |
| `--gold` | `#7a5b12` | `#e3c374` | accent texte, liens, bouton principal |
| `--gold2` | `#d9b65e` | `#c9a54f` | remplissages décoratifs |
| `--on-gold` | `#ffffff` | `#17140c` | texte sur `--gold` |
| `--band` · `--band-line` · `--band-lab` | `#eaf4ed` · `#cbe2d3` · `#245536` | `#1c2a21` · `#2d4535` · `#a3d6b5` | bandeau d’en-tête (fenêtre, bandeaux) |
| `--ok` · `--warn` · `--bad` | `#1d6a3a` · `#8a5207` · `#a12a24` | `#74d39b` · `#f2bb63` · `#f39087` | états |

Les rayons valent 8, 12 et 18 px, plus une pastille. Les ombres ont trois niveaux : `--sh-1` pour le repos, `--sh-2` pour l’élévation et `--sh-3` pour la fenêtre. Le mouvement dure 160 ms avec `cubic-bezier(.2,.7,.2,1)`. L’anneau de focus a 2 px.

## 3. Échelle typographique (rapport 1,2)
| Niveau | Police | Taille / interligne | Graisse |
|---|---|---|---|
| Titre principal | serif (`Iowan Old Style`, `Palatino`, `P052`, `Georgia`), encre | `clamp(1.85rem, 4.2vw, 2.75rem)` / 1.08 | 700 |
| h2 | serif, encre | 1.32rem / 1.25 | 700 |
| h3 | sans, encre | 1rem / 1.35 | 700 |
| Corps | sans (`system-ui`, `Segoe UI`, `Roboto`, `Noto Sans`) | 15px / 1.55 | 400 |
| Surtitre | sans, capitales, interlettrage .2em | .7rem | 650 |
| Chiffres | mono (`ui-monospace`, `SF Mono`, `Cascadia Mono`, `Consolas`) | 1.4rem (1.2rem sur mobile) | 600 |

## 4. Composants
- **En-tête.** Il porte un halo doré proportionnel à « Fond doré » (réglé par vous) et l’ombre `--sh-2`. La place des indicateurs est réservée, ce qui ramène le CLS au chargement de 0,156 à 0,042 sur ordinateur.
- **Barre d’onglets.** C’est un rail segmenté, collant et légèrement translucide. L’onglet actif est encré. Sur mobile, elle tient sur une seule ligne défilante (de 182 px à 52 px de haut).
- **Cartes et indicateurs.** Rayon de 18 px, bordure fine, ombre `--sh-1`. Les indicateurs sont sur fond `--soft` avec chiffres tabulaires.
- **Boutons et champs.** Les boutons mesurent au moins 36 px de haut. Le bouton principal est bronze avec un texte `--on-gold` (AA dans les deux thèmes). Le survol rehausse la bordure, et l’appui enfonce le bouton d’un pixel.
- **Puces et icône i.** Elles mesurent au moins 24 à 28 px (cible WCAG 2.2).
- **Listes de SSP et calendrier.** Les états de survol et de sélection sont doux. L’en-tête du jour est en pastille bronze.
- **Jauges.** Le rail est en creux et le remplissage en dégradé. La largeur s’anime en 0,4 s, sauf en mouvement réduit.
- **Fenêtre d’information.** Elle s’ouvre sur un bandeau vert pâle qui porte la partie et le titre (serif gras, encre). Viennent ensuite le texte justifié et les sources, avec l’ombre `--sh-3`.
- **Bandeau 2027 (`.exi-bn`, Thémis).** La première phrase (« La session 2026 est terminée ») est sur la bande vert pâle, et les autres phrases sont dessous, alignées à gauche, car les dates y sont insécables. Le compte à rebours `.cd` est en rouge gras, parce que c’est une échéance capitale. Les liens sont en bronze.
- **Badge « À vérifier » (`.exi-vb`).** C’est une pastille ivoire ambrée avec un liseré gauche ambre et une encre noire (AA dans les deux thèmes). Le rouge n’est pas utilisé : il s’agit d’un point à vérifier, pas d’une alerte.
- **Barre collante.** `html{scroll-padding-top: safe-area + var(--nav-h)}`, avec `--nav-h` à 64 px sur ordinateur et 62 px sur mobile. Une ancre, un `scrollIntoView` ou un focus s’arrête donc sous la barre d’onglets. Iris contrôle chaque panneau (état `masquage`) : avant, 18 vues sur 18 étaient masquées en thème clair, et après, il n’y en a plus aucune. Le cas d’un changement d’onglet alors que la page est défilée loin relève du script, puisqu’il faudrait remonter au haut du panneau ; il est confié à Hermès.
- **Bandeau de sauvegarde.** Le message est en gras sur la bande, et les actions sont dessous. L’état d’alerte se signale par un liseré ambre, et l’erreur de stockage par le rouge. Elle reste un panneau bas sur mobile, et son comportement est inchangé.

## 5. Mesures (automate Iris, poste local, 60 captures)
| Mesure | Avant | Après |
|---|---|---|
| axe-core, contraste en thème clair et doré (nœuds) | 289 | 0 |
| axe-core, contraste en thème sombre (nœuds) | 34 | 0 |
| axe-core, taille de cible | 21 | 0 |
| axe-core, `html-has-lang` | 18 | 0 |
| Requêtes réseau de polices | 5 | 0 |
| CLS au chargement, ordinateur | 0,156 | 0,042 |
| Débordement horizontal sur mobile | 0 | 0 |
| Contraste minimal des bandes de séance | 3,44:1 | 6,03:1 |
| Haut de panneau masqué par la barre d’onglets (thème clair) | 18 vues | 0 |
| Contrôles d’interaction | 69/69 | 69/69 |

Restent hors périmètre (balisage, chantier d’Hermès) : `select-name` et `scrollable-region-focusable`, 4 nœuds chacun.

## 6. Calendrier : teintes de jour et bandes de séance (directive du 17.10.2026)
- Chaque jour de la semaine a sa teinte très pâle : `--day1` lundi (bleu), `--day2` mardi (vert), `--day3` mercredi (ivoire), `--day4` jeudi (lavande), `--day5` vendredi (eau), `--day6` samedi (rose) et `--day7` dimanche (pierre). Le thème sombre a des teintes très sombres et équivalentes. La teinte couvre la colonne et son en-tête de jour.
- Chaque séance `.blk` mêle 14 % de sa couleur de famille (`--bc`) à du blanc (24 % sur fond sombre). Elle a un filet de 1 px, un liseré gauche de 4 px et une encre `--blk-ink` pour tous ses textes. Le contraste mesuré par Iris est d’au moins 6,0:1 en clair et en doré, et de 6,8:1 en sombre, pour 42 textes sur les 7 jours. Le minimum exigé est de 4,5:1, et un échec bloque la fusion.
- **Sélecteurs stables pour Hermès.** Ces sélecteurs sont `.grid > .col[data-wd="N"]` et `.grid > .hd[data-wd="N"]`, où N vaut 1 pour lundi et 7 pour dimanche. L’attribut `data-wd` est posé par Hermès (patch 0004) ; il est stable et ne dépend pas de l’ordre des enfants.
- Iris ajoute l’état `cal-seances`. Il sème deux séances par jour dans le stockage local du test, mesure le contraste de chaque texte de séance contre le fond réellement peint (couleurs résolues par canevas) et lance axe-core sur le calendrier rempli.

## 7. Composants réservés à l’examen physique (Asclépios)
Ces classes sont déjà stylées dans `apollon.css`, sans balisage pour l’instant. Elles sont stables et sémantiques :
| Classe | Élément conseillé | Rôle |
|---|---|---|
| `.ex-region` | `<section>` | Section d’une région anatomique : carte et bandeau d’en-tête |
| `.ex-region__h` | `<h3>` (premier enfant) | Titre de région sur la bande vert pâle, en gras noir |
| `.ex-phase` + `data-ordre="1"…"6"` | `<h4>` | Sous-titre de phase dans l’ordre strict : Inspection, Palpation, Percussion, Auscultation, Mobilisation, Tests spéciaux |
| `.ex-fig` | `<figure>` | Croquis anatomique centré, de 520 px au plus, avec un fond blanc |
| `.ex-fig figcaption` / `.ex-fig__cap` | `<figcaption>` | Légende complète |
| `.ex-fig__credit` | `<small>` dans la légende | Crédit TASL (titre, auteur, source, licence), en gris |
| `.ex-xref` / `.ex-chip` | `<nav>` de liens ou de boutons | Puces de renvoi (région × système, SSP liés), avec une cible de 28 px |

## 8. Organisation du CSS
`apollon.css` suit l’ordre **jetons → base → mise en page → composants → utilitaires**. Le bloc 1 contient les jetons et les thèmes, le bloc 2 la typographie et la justification, le bloc 3 les surfaces, et les blocs 4 à 7 les onglets, contrôles, listes, calendrier, jauges, fenêtre, bandeaux et composants de l’examen. Le bloc 8 réunit la stabilité (CLS) et le mouvement réduit. Il vient après les deux blocs historiques, pour que ses règles l’emportent à spécificité égale, sans `!important` sauf pour le mouvement réduit.
- **Polices.** Une pile système remplace Google Fonts : aucun octet ajouté, et un rendu hors ligne identique. L’auto-hébergement aurait coûté environ 250 Ko en base64, sur les 295 Ko de marge du budget de 6 Mo.
- **Styles en ligne.** Environ 45 attributs `style` restent en place. Environ la moitié portent des valeurs calculées par le script (positions et hauteurs des séances, largeurs des jauges, couleurs de famille `--gc`, `--pc`, `--bc`) et doivent rester en ligne. L’autre moitié est statique (`width:80px`, `margin-left:auto`, `grid-column:1/-1`) et se trouve dans le balisage d’Hermès et d’Atlas. Apollon ne le déplace pas, pour ne changer aucun balisage ; ces styles sont listés pour Hermès, qui pourra les convertir en classes utilitaires lors de sa refonte.

## 9. Défaut trouvé pendant les mesures (hors périmètre, pour Hermès)
Au rechargement, l’application rouvre le dernier onglet mémorisé (`orga-tab`). Si c’est « Notions CK » ou « Gestes d’examen », le script lève `Cannot access 'NSEL' before initialization` ou `Cannot access 'GS' before initialization`. Le défaut existe déjà dans `orig/app.html`. Iris l’évite dans son état semé en fixant `orga-tab` à « cal », et il faudra le corriger dans le script.

## 10. Thèmes de fond d’écran et sélecteur (demande du titulaire, 17.10.2026)
- **Dix thèmes** (`tools/patches/fonds.json`) remplacent la surface des textes : fond de page, cartes, panneaux, indicateurs et en-têtes de section. Aucun n’a de dominante dorée ou jaune, et le halo doré est neutralisé (`--gilt:0`). Ce sont blanc neutre adouci, gris perle, sauge pâle, gris-bleu pâle, bleu brume, lavande grise, menthe très pâle, rose grisé, ardoise sombre et graphite sombre. Le contraste du texte principal va de 13,0:1 à 18,4:1 et celui du texte secondaire de 7,3:1 à 9,7:1 : tous les thèmes sont AAA. Le test `tests/test_fond.py` vérifie ce minimum de 7:1 pour les dix.
- **Bouton « Thème de fond d’écran ».** Il est fixe en bas à droite sur tous les onglets, avec une cible de 44 à 48 px. Sur mobile, il se réduit à une icône, avec un libellé conservé pour les lecteurs d’écran. Il ouvre un panneau à boutons radio, avec le bandeau d’en-tête vert pâle. Le panneau se ferme par Échap, par « Fermer » ou par un clic à l’extérieur, et le focus revient au bouton. Le choix est enregistré dans `localStorage` sous `orga-fond` et appliqué dans `<head>` avant le premier affichage. Chaque thème fixe aussi `data-theme` (clair ou sombre), pour que les accents restent cohérents. « Par défaut » rend la main au réglage « Fond doré ».
- **Classes stables.** Elles sont `.fond-btn`, `.fond-pan`, `.fond-h` et `.sw`, plus l’attribut `:root[data-fond="<id>"]`.

## 11. Contraintes du validateur (pour tout agent qui ajoute du CSS)
- Une règle dont le sélecteur dépend d’un attribut de `<html>` (`data-theme`, `data-fond`) va dans le style de `<head>`, car dans `@scope` (racine `<body>`) elle ne s’applique pas.
- Les jetons vont dans le style de `<head>` (`tools/patches/apollon-jetons.css`, sélecteurs `:root:root…`). Les composants vont dans le style de `<body>`, à l’intérieur de `@scope { … }`, où le validateur Nu admet les règles.
- Ces formes font échouer le validateur, il faut les éviter : `nth-child(N of S)` (plantage), et un pourcentage `calc(var(--x)*N%)` ou `var(--x)` dans `color-mix()`.

## 12. Fond par défaut quasi neutre (priorité du titulaire, 17.10.2026 : « Le fond est toujours aussi jaune »)
- **Surfaces.** La page est en `#fbfbf8`, les cartes et panneaux en `#ffffff`, les surfaces douces en `#f3f3f1` et les filets en `#dededb`. Le halo doré de l’en-tête est retiré, et les teintes de jour sableuses sont remplacées par un gris neutre et un gris sauge.
- **Encre.** Le texte principal est en `#1a1a1a` (17,4:1 sur carte) et le texte secondaire en `#4a4a4a` (8,6:1 sur la page) : les deux sont AAA. En sombre, le texte `#ececec` repose sur `#1c1d1f` et la page sur `#141516`.
- **Curseur « Fond doré ».** Il ne teinte plus les surfaces de texte, car le fond est fixé par jeton. C’est le seul effet visible de ce changement sur un réglage existant ; le relibellé ou le retrait du curseur est à décider par Hermès.
