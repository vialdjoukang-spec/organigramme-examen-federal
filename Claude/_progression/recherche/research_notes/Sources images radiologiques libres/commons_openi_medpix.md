# Wikimedia Commons, NIH Open-i et MedPix : accès programmatique gratuit à des images radiologiques

Tests en direct menés le 13.11.2026 avec curl depuis le conteneur cloud (sortie par un proxy HTTPS partagé). Les sorties brutes sont dans le scratchpad de la session ; ce qui en compte est recopié ci-dessous.

## 1. Quels points d'accès répondent aujourd'hui à un script, avec quels paramètres, et quels champs JSON portent l'URL, la légende, la licence et l'auteur ?

### Takeaway
Ce 13.11.2026, seul Wikimedia Commons répond à un script : l'API MediaWiki `https://commons.wikimedia.org/w/api.php` fonctionne (search + imageinfo/extmetadata), mais le proxy partagé reçoit beaucoup de HTTP 429. Le site d'Open-i, y compris `/api/search`, renvoie une page HTML « The web site is currently under maintenance » et aucun JSON. MedPix redirige vers une page LHNCBC qui annonce une indisponibilité.

### Cited Findings
**Wikimedia Commons (testé, fonctionne)**
- Recherche plein texte limitée aux fichiers (`srnamespace=6`) : `curl -A "ProgressionEdu/1.0 (educational)" "https://commons.wikimedia.org/w/api.php?action=query&list=search&srsearch=pneumothorax%20x-ray&srnamespace=6&srlimit=3&srinfo=totalhits&format=json&formatversion=2"`. Réponse : `query.searchinfo.totalhits` = 556 ; `query.search[].title` = « File:X-ray of pneumothorax signs.jpg », etc. — test en direct, [API Commons](https://commons.wikimedia.org/w/api.php)
- Métadonnées par image, avec jusqu'à 50 titres séparés par `|` dans une seule requête : `action=query&prop=imageinfo&titles=File:Subarachnoid hemorrhage CT.jpg|File:X-ray of pneumothorax signs.jpg&iiprop=url|extmetadata|size|mime&iiurlwidth=800&iiextmetadatafilter=LicenseShortName|LicenseUrl|Artist|Credit|ImageDescription|AttributionRequired|UsageTerms|Copyrighted&iiextmetadatalanguage=en&format=json&formatversion=2`. Champs utiles : `query.pages[].imageinfo[0].url` (original), `.thumburl` (vignette à la largeur demandée), `.width` et `.height`, `.extmetadata.LicenseShortName.value`, `.LicenseUrl.value`, `.Artist.value` (HTML), `.Credit.value`, `.ImageDescription.value` (légende en HTML), `.AttributionRequired.value` — test en direct, [API Commons](https://commons.wikimedia.org/w/api.php)
- Résultats réels de ce test :
  - « Subarachnoid hemorrhage CT.jpg » : 476×596, CC BY-SA 3.0, Artist « Dr. George Jallo, pediatric neurosurgeon at Johns Hopkins ».
  - « X-ray of pneumothorax signs.jpg » : 1980×1684, CC BY-SA 3.0, auteur Karthik Easvur, own work.
  - « Ultrasonography of deep vein thrombosis of the femoral vein.jpg » : 695×456, CC0, Mikael Häggström.
  - « CT of a normal brain, coronal 53.png » : 640×426, CC0, Mikael Häggström.
  - « Subhepatische Appendicitis 45M - CT coronar - 001.jpg » : 1595×545, CC BY-SA 4.0, Hellerhoff, légende détaillée en allemand.

  Source : test en direct, [API Commons](https://commons.wikimedia.org/w/api.php)
- Définition des champs extmetadata : `ImageDescription` = description ; `Artist` = auteur, qui « might contain complex HTML, multiple authors » ; `Credit` = source ; `LicenseShortName` = « short human-readable license name » ; `Copyrighted` = « True or False (for public domain images) » ; `Restrictions` = « trademarks or personality rights » ; `AttributionRequired` = obligation légale d'attribuer ; `Attribution` = attribution personnalisée qui remplace Artist et Credit. Avertissement de la page : « For multi-licensed images, these values are currently unreliable » — [Extension:CommonsMetadata](https://www.mediawiki.org/wiki/Extension:CommonsMetadata)
- Limites de débit :
  - Il n'existe pas de plafond chiffré en lecture : « There is no hard speed limit on read requests ». La page recommande des requêtes en série et non en parallèle, des titres groupés par `|` et le paramètre `maxlag` pour les tâches non interactives.
  - En cas d'erreur `ratelimited`, il faut réessayer avec un backoff exponentiel.

  Source : [API:Etiquette](https://www.mediawiki.org/wiki/API:Etiquette)
- User-Agent : le format attendu est `<client>/<version> (<contact>) <lib>/<version>`. Un User-Agent absent ou générique « fail with an HTTP 403 », et un script sans contact « may be blocked without notice » — [WMF User-Agent Policy](https://foundation.wikimedia.org/wiki/Policy:Wikimedia_Foundation_User-Agent_Policy)
- Observation de test : même avec le User-Agent « ProgressionEdu/1.0 (educational) » et des pauses de 1,5 à 8 s, environ une requête sur deux a reçu HTTP 429 (« You are making too many requests to the API ») ; il a fallu des reprises espacées de 10 à 60 s. À l'inverse, une requête sans User-Agent personnalisé est passée une fois (HTTP 200). Le 429 semble donc lié à l'IP du proxy partagé plutôt qu'au seul User-Agent — test en direct.

**NIH Open-i (testé, hors service)**
- `https://openi.nlm.nih.gov/`, `/services`, `/api/search?query=pneumothorax&m=1&n=2`, `/api/search?query=stroke&it=m&m=1&n=5` et `/gridquery?q=…` renvoient tous HTTP 200 en `text/html` (13 854 octets) avec le texte « There seems to be an error … The web site is currently under maintenance. we are sorry for the inconvenience ». Aucun JSON n'est renvoyé. Test en direct deux fois le 13.11.2026 — [Open-i](https://openi.nlm.nih.gov/)
- Le catalogue fédéral, modifié le 18.06.2025, documente encore l'API à `https://openi.nlm.nih.gov/services#searchAPIUsingGET` et indique « MedPix can be accessed programmatically via the Open-i API » — [data.gov MedPix](https://catalog.data.gov/dataset/medpix)
- Filtres connus par l'interface :
  - Image Type, dont « CT Scan », « Graphics » et « MRI ». L'URL `gridquery?it=c` filtre les scanners.
  - License Type : Attribution, Attribution noncommercial, Attribution noncommercial no derivatives, etc.
  - Collections : PubMed Central, Indiana U. Chest X-rays, USC Orthopedic Surgical Anatomy, etc.
  - « Reuse … is determined by the license type of the image ».

  Sources : [Open-i FAQ](https://openi.nlm.nih.gov/faq), [gridquery it=c](https://openi.nlm.nih.gov/gridquery?it=c), [HSLS Update](https://info.hsls.pitt.edu/updatereport/2019/july-2019/open-i%C2%AE-a-unique-image-search-engine/)

### Inferences
- Open-i, connaissances antérieures à vérifier : la documentation `/services` est hors ligne et l'archive Wayback est bloquée par le proxy. Syntaxe connue avant la panne :
  - requête : `GET https://openi.nlm.nih.gov/api/search?query=<termes>&m=<début, base 1>&n=<fin>`, avec environ 30 résultats au plus par appel ;
  - `it` (type d'image) : `x` radiographie, `c` CT, `m` IRM, `u` échographie, `p` photo, `g` graphique, `mc` microscopie, `xg` exclut les graphiques, `xm` exclut les figures multipanneaux ;
  - `coll` (collection) : `pmc`, `cxr` (Indiana), `mpx` (MedPix), `usc`, `hmd` ;
  - `lic` (licence) : `by`, `bync`, `byncnd`, `byncsa`, etc. ;
  - autres filtres : `sp` (spécialité), `at` (type d'article), `fields` ;
  - champs JSON : `total` et `list[]`, dont `imgLarge`, `imgThumb` (chemins relatifs à préfixer par `https://openi.nlm.nih.gov`), `image.caption`, `image.mention`, `uid`, `pmcid`, `journal_title`, `authors` et `license`.

  À revalider dès le retour du service.
- Pour un pipeline fiable aujourd'hui, Commons est la seule source automatisable. Il faut prévoir un backoff, du cache et des lots de 50 titres.

### Gaps
- Je n'ai pas pu lire la documentation officielle d'Open-i (`/services` en maintenance, web.archive.org bloqué par le proxy). Les codes exacts de `it`, `coll` et `lic` restent « À vérifier ».
- Je n'ai trouvé aucune date annoncée de retour d'Open-i.

## 2. MedPix est-il encore en ligne ou accessible par API, et sous quelle licence ?

### Takeaway
MedPix n'est plus servi par la NLM : `medpix.nlm.nih.gov` redirige (HTTP 302) vers `lhncbc.nlm.nih.gov/medpix.html`, qui annonce une indisponibilité. Selon une notice NLM relayée par la recherche web, les fonctions MedPix ne sont plus disponibles à la NLM et les cas sont renvoyés vers l'ASNR (Case of the Week, AJNR). L'accès par Open-i `coll=mpx` est lui-même hors service. À exclure du pipeline actuel.

### Cited Findings
- `https://medpix.nlm.nih.gov/home` et `/advancedsearch` renvoient HTTP 302 vers `https://lhncbc.nlm.nih.gov:443/medpix.html` — test en direct, [MedPix](https://medpix.nlm.nih.gov/home)
- La page LHNCBC indique que les fonctions sont « temporarily unavailable due to technical issues » et renvoie au NLM Support Center ; elle ne mentionne aucune API ni aucune licence d'image — [LHNCBC MedPix](https://lhncbc.nlm.nih.gov/medpix.html)
- Une notice NLM, citée par la recherche web, précise que « MedPix® Medical Image Database, Teaching File, CME, and CUP functions are no longer available at NLM » et dirige vers l'ASNR Case of the Week — [medpix.nlm.nih.gov/advancedsearch](https://medpix.nlm.nih.gov/advancedsearch) (texte de la notice relayé par le moteur de recherche ; le curl direct ne montre plus que la redirection) ; [AJNR case archive](https://www.ajnr.org/case-archive)
- Notice data.gov : licence de la fiche « odc-odbl », accès « public », modifiée le 18.06.2025. Il s'agit de la licence de la fiche catalogue et non, de façon démontrée, de celle de chaque image — [data.gov MedPix](https://catalog.data.gov/dataset/medpix)

### Inferences
- Même quand MedPix était en ligne, les images étaient majoritairement des contributions sous droits d'auteur des contributeurs, pour un usage éducatif (souvenir non vérifié aujourd'hui). Pour un site public suisse, il ne faut pas l'utiliser sans licence explicite par image.
- Les cas ASNR/AJNR relèvent du droit d'auteur de l'éditeur et ne sont pas sous licence libre : je les exclus.

### Gaps
- Je n'ai trouvé ni date exacte de fermeture ni texte de licence MedPix accessible aujourd'hui.

## 3. Quelle couverture pour les diagnostics typiques d'examen ?

### Takeaway
Sur Commons, la couverture est bonne pour la radiographie et le scanner (pneumothorax, appendicite CT, embolie pulmonaire, cerveau normal), mais faible en recherche anglaise libre pour l'IRM de diffusion de l'AVC et l'échographie. Il faut alors chercher dans les catégories ou en allemand (fonds Hellerhoff). Open-i et MedPix n'ont pas pu être comptés (hors service).

### Cited Findings
Comptes `srinfo=totalhits` sur Commons, espace File (6), le 13.11.2026. Le compte inclut des PDF et du bruit. Source : test en direct, [API Commons](https://commons.wikimedia.org/w/api.php).

| Requête | Hits | 1er résultat pertinent |
|---|---|---|
| subarachnoid hemorrhage CT | 48 | Subarachnoid hemorrhage CT.jpg (CC BY-SA 3.0) |
| ischemic stroke diffusion MRI | 9 | aucun pertinent (PDF d'articles) |
| stroke diffusion-weighted MRI | 9 | aucun pertinent |
| pneumothorax x-ray | 556 | X-ray of pneumothorax signs.jpg (CC BY-SA 3.0) |
| appendicitis CT | 860 | Subhepatische Appendicitis … CT coronar (Hellerhoff, CC BY-SA 4.0) |
| appendicitis ultrasound | 44 | Appendicitis ultrasound.png |
| deep vein thrombosis ultrasound | 35 | Doppler … axillary and subclavian vein thrombosis – annotated ; Ultrasonography of DVT of the femoral vein (CC0) |
| aortic dissection CT | 96 | Descending (Type B Stanford) Aortic Dissection.PNG |
| pulmonary embolism CT | 239 | Pulmonary embolism CTPA.JPEG |
| normal CT brain | 3344 | CT of a normal brain, coronal 53.png (CC0) |
| normal chest X-ray PA | 1304 | Normal posteroanterior (PA) chest radiograph (X-ray).jpg |
| Radiopaedia stroke diffusion | 0 | — |

- Tailles des catégories (`prop=categoryinfo`) — test en direct, [API Commons](https://commons.wikimedia.org/w/api.php) :
  - Category:Radiology : 298 fichiers, 45 sous-catégories.
  - Category:Medical imaging : 464 fichiers, 43 sous-catégories.
  - Category:Radiopaedia : 40 fichiers, 1 sous-catégorie.
  - Category:Case Western Reserve University : 44 fichiers, 17 sous-catégories.
  - Category:Projectional radiography : 10 fichiers.
  - Absentes : « Category:Hellerhoff », « Images by Hellerhoff », « Normal chest radiographs », « CT of normal brain ».

### Inferences
- La qualité pédagogique est inégale :
  - Les images de Hellerhoff (radiologue allemand, CC BY-SA, légendes cliniques détaillées en allemand, versions « Annotation ») et de Mikael Häggström (CC0, séries annotées et normales) sont les plus utiles.
  - Les titres « Ultrasound Scan ND … » sont des scans sans légende, à écarter.
- Les Hellerhoff se trouvent par l'utilisateur et non par une catégorie, par exemple avec `list=allimages&aiuser=Hellerhoff&aisort=timestamp`. Les termes allemands donnent de meilleurs résultats (« Appendicitis », « Pneumothorax », « Subarachnoidalblutung », « Hirninfarkt DWI »). Ce sont des inférences, non testées faute de quota.
- Pour l'IRM de diffusion de l'AVC, mieux vaut des termes plus courts (« DWI infarct », « MRI stroke ») et les catégories de type « MRI of stroke » plutôt que la recherche anglaise longue. Non testé (429).
- La « Category:Radiopaedia » ne contient que 40 fichiers : ce n'est pas un gisement Radiopaedia significatif. Radiopaedia elle-même est sous CC BY-NC-SA, hors périmètre de cette note.

### Gaps
- Je n'ai obtenu aucun compte Open-i ni MedPix (services indisponibles).
- Je n'ai pas pu tester les variantes allemandes ni la recherche `deepcat:`, à cause des 429 répétés.

## 4. Meilleure stratégie pour les images normales de référence

### Takeaway
Les images normales se trouvent sur Commons, par une recherche « normal » combinée à la modalité et au plan. Exemples : « CT of a normal brain, coronal NN » (série CC0 de Häggström, 640×426) et « Normal posteroanterior (PA) chest radiograph (X-ray).jpg ». On vérifie ensuite par imageinfo la licence et la largeur avant de les apparier au cliché pathologique de même modalité et de même plan.

### Cited Findings
- « normal CT brain » donne 3344 hits ; les premiers sont « CT of a normal brain, coronal 53/22.png » (CC0, Mikael Häggström) — test en direct, [API Commons](https://commons.wikimedia.org/w/api.php)
- « normal chest X-ray PA » donne 1304 hits ; le premier est « Normal posteroanterior (PA) chest radiograph (X-ray).jpg » — test en direct, [API Commons](https://commons.wikimedia.org/w/api.php)
- Commons fournit `width` et `height` ainsi qu'une vignette à la largeur demandée (`iiurlwidth=800` donne `thumburl`), ce qui permet de rejeter les images trop petites (< 600 px) — test en direct

### Inferences
Stratégie proposée :
1. Rechercher `normal <modalité> <région> <plan>` (anglais, puis allemand « Normalbefund »).
2. Filtrer `AttributionRequired`, `LicenseShortName` ∈ {CC0, PD, CC BY, CC BY-SA} et une largeur ≥ 600 px.
3. Préférer les séries d'un même auteur (Häggström, Hellerhoff) pour garder une fenêtre et un plan homogènes.
4. Stocker en local l'URL du fichier, l'auteur nettoyé du HTML et la licence, pour l'attribution.

Pour l'usage en Suisse : CC0 et PD sont libres ; CC BY et CC BY-SA imposent l'attribution, avec un partage à l'identique pour BY-SA si l'image est modifiée (annotations) ; NC et ND sont à exclure pour un site public, ou à signaler.

### Gaps
- Je n'ai pas d'inventaire systématique des normaux par région (abdomen CT, échographie normale de l'appendice, Doppler veineux normal), faute de quota de requêtes.
