# Apollon · spécification de la présentation premium

Date : 17.10.2026 (Europe/Zurich). Portée : présentation seule. Le patch `tools/patches/0004-apollon-premium.py` ajoute `tools/patches/apollon.css` en fin du bloc de style principal. Il retire la feuille Google Fonts et ajoute `lang="fr"` sur `<html>`. Il ne change aucun texte, aucune donnée, aucun identifiant et aucun script.

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
| Contrôles d’interaction | 56/56 | 56/56 |

Restent hors périmètre (balisage, chantier d’Hermès) : `select-name` et `scrollable-region-focusable`, 4 nœuds chacun.
