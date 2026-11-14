# Audit radiologique V2 : vérification des corrections IMG-238 à IMG-268 (14.11.2026)

Méthode :
- lecture de `CORRECTIONS_IMAGES_238_268.md` et des champs `images` de `PE_MS.json` ;
- examen des copies `_verif` régénérées de 240, 242, 248, 252, 255 et 262 ;
- recherche dans `git log` des commits qui contiennent `img/IMG-242_patho.jpg`.

**Verdict : corrections requises.** Il reste un point bloquant hors de mes droits (242, historique git) et un repère mineur (255).

## 1. Critiques et majeurs de V1

| id | Contrôle sur le rendu | Statut |
|---|---|---|
| 262 | Je juge l'option retenue (garder l'image et la réécrire) juste. Agrandi, le spectre passe sous la ligne de base en fin de diastole, au point « ED » ; le bandeau indique « 3 Trim ». `technique`, `lesion` et `semio` décrivent désormais une diastole inversée (REDV) au 3e trimestre, et la `technique` signale l'interversion de légende de l'article. Le normal (même article, 3e trimestre, diastole positive) est comparable. | corrigé |
| 240 | Avec le nouveau fenêtrage, la vessie opacifiée et le liquide intrapéritonéal dense autour des anses sont visibles. Le repère 1 touche le défect du dôme, sous la flèche des auteurs. Le repère 2 (36 ; 47) est dans le liquide dense. Le fenêtrage ajusté est déclaré. | corrigé |
| 252 | Le repère 3 « ovaire sans flux interne » est conforme à la légende (« absent ovarian vascularity »). Le message sur le flux conservé est dans `syndrome`. La différence de technique du normal est déclarée. | corrigé |
| 248 | Les repères (36 ; 33) et (64 ; 37) sont dans les plages « AB » des auteurs. | corrigé |
| 242 | Le fichier image actuel masque le nom sous une bande noire (rendu `_verif` contrôlé). En revanche, le fichier non masqué figure dans le commit `70201f7f0`, antérieur au masquage `f94387961`. **Le nom du patient reste lisible dans l'historique d'un dépôt public.** | **non corrigé** |

## 2. Mineurs de V1

| id | Contrôle | Statut |
|---|---|---|
| 247 | La licence est passée en « CC BY ». La mention non sourcée est retirée. | corrigé |
| 255 | Le contexte (stimulation ovarienne, hyperstimulation) est ajouté. En revanche, la pointe du repère 2 (82 ; 45) tombe sur la capsule supérieure de l'ovaire droit et non dans la couronne folliculaire. | à reprendre |
| 239, 265 | « même patient » est corrigé ; la séquence différente est déclarée. | corrigé |

## 3. Patchs restants

| id | Gravité | PATCH exact |
|---|---|---|
| 242 | majeur (donnée personnelle) | Purger le blob de l'historique (`git filter-repo --path Claude/_progression/recensement/img/IMG-242_patho.jpg --invert-paths`, puis réajouter le fichier masqué) et pousser en force. Cette décision revient à Vial : poser l'étiquette `attente-vial`. À défaut de purge, retirer l'image (`images.manque`) n'efface pas l'historique. |
| 255 repère 2 | mineur | x = 69, y = 48 (follicules périphériques de l'ovaire droit), puis contrôle sur `_verif`. |

## Clôture
255 repère 2 replacé en (69 ; 48). Le fichier IMG-242 actuel est masqué ; reste la question de la purge de l'historique git (image d'origine dans le commit 70201f7f0, issue d'un article CC BY déjà public) : **attente-vial**. Contenu : audit-ok.
