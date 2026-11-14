# Harnais RADIO-PAIRES — mémoire persistante (lire en premier, mettre à jour à chaque lot)
Objectif : 344 diagnostics (diagnostics.json) × 2 images : NORMAL (toujours à gauche) + PATHOLOGIQUE annotée,
même modalité / même séquence / même plan / même région que le cliché demandé (champ `cliche`).
Ordre de priorité : Qualité → Exhaustivité → Économie → Esthétique. Jamais inventer. Doute ⇒ « À vérifier ».

## Sources autorisées (ordre de préférence, API d'abord, zéro navigateur)
1. Wikimedia Commons API (licence libre lisible dans imageinfo extmetadata : LicenseShortName, Artist, ImageDescription).
   `https://commons.wikimedia.org/w/api.php?action=query&generator=search&gsrnamespace=6&gsrsearch=...&prop=imageinfo&iiprop=url|extmetadata|size&iiurlwidth=1024&format=json` (User-Agent obligatoire).
2. Open-i NIH `https://openi.nlm.nih.gov/api/search?query=...&m=1&n=20` (figures PMC : licence de l'article à vérifier ; ne garder que CC BY / CC BY-SA / CC0 / PD).
3. Europe PMC / PMC OA (figures d'articles CC BY) avec légende de figure.
Interdit : images sans licence identifiée, Radiopaedia/sites commerciaux sauf licence explicite compatible et crédit, captures d'atlas protégés.
Une NORMALE peut être de n'importe quelle source libre mais DOIT être appariée (modalité+séquence+plan+région ; fenêtre identique pour TDM).

## Annotations (manifest/IMG-xxx.json, voir SCHEMA)
- Chaque flèche : tip [x,y] normalisés 0–1 sur l'image patho, `from` [x,y] (queue), `label` (nom de la lésion), `role` ∈ principale|associee|secondaire|complication,
  `evidence` = citation exacte de la légende/description source qui localise la lésion, ou "visuel" ; `confidence` ∈ haute|moyenne|basse.
- Localisation : (a) si l'image source porte déjà des flèches/marques → pointer exactement là (haute) ; (b) si la légende localise (côté, lobe, segment) → vérifier visuellement en ouvrant l'image (Read) et placer (moyenne) ; (c) purement visuel → basse + "À vérifier". Gauche/droite radiologique : le côté gauche de l'image = droite du patient (TDM/IRM axiale, RX face).
- Ouvrir CHAQUE image retenue avec Read (vision) avant de la valider : vérifier modalité, plan, qualité, absence d'identifiants patients, pathologie visible.

## Fichiers
- images/normal/IMG-xxx_normal.jpg, images/patho/IMG-xxx_patho.jpg (JPEG, côté long ≤ 1024 px, qualité 85).
- manifest/IMG-xxx.json (un par diagnostic). Statut : complet | partiel (paire non parfaite, préciser) | introuvable (avec requêtes tentées).
- memory/journal_lotN.md : avancement, requêtes efficaces, pièges (reprise sans perte si contexte perdu).
- scripts/ : outils partagés (fetch_commons.py, fetch_openi.py, normalize.py, validate.py). Réutiliser, ne pas réécrire.
- Cache HTTP : cache/ (ne jamais retélécharger une même URL).

## Économie
Requêtes API en anglais (terminologie radiologique), limitées ; légende lue en métadonnées plutôt que page HTML ; pas de navigateur.

## Outils (scripts/, Python 3 stdlib + Pillow ; cache HTTP disque cache/ partagé : une URL n'est jamais retéléchargée)
- `python3 scripts/fetch_commons.py findcat "pneumothorax"` → noms de catégories Commons (plus précis que le plein texte).
- `python3 scripts/fetch_commons.py cat "X-rays of pneumothorax" [-n 50]` → fichiers d'une catégorie.
- `python3 scripts/fetch_commons.py search "query filetype:bitmap" [-n 15] [--json]` → `titre | licence | LxH | description | url`.
  Préfixe `!` = licence hors liste blanche (rejeter), `~` = pas une image (PDF/vidéo).
- `python3 scripts/fetch_commons.py info "File:X.jpg"` → métadonnées complètes (licence, auteur, description, catégories).
- `python3 scripts/fetch_commons.py get "File:X.jpg" images/patho/IMG-xxx_patho.jpg` → vignette 1024 px normalisée + `…jpg.meta.json`
  (title, source_url, license, license_url, author, credit, description) : recopier ces champs dans le manifest.
- `python3 scripts/fetch_openi.py search "query" [--it x|c|m|u] [--lic by] [-n 15]` → `clé | licence | revue année | modalité | légende`.
  `!` = licence absente ou NC/ND (rejeter). `get <clé> dest.jpg [--q "query"]` (clé de la dernière recherche par défaut) ;
  Open-i sert au plus 512 px ; meta.json contient citation + légende (= caption_source).
- `python3 scripts/normalize.py src dest.jpg` ou `--inplace f.jpg…` → JPEG ≤ 1024 px, q85, sans EXIF.
- `python3 scripts/validate.py [--only IMG-001,IMG-002] [--quiet]` → tableau + `validate_report.json` ; code 1 si erreur.
  Contrôles : fichiers JPEG ≤ 1024, licence liste blanche (CC0 / PD / CC BY x.y / CC BY-SA x.y), auteur + source_url,
  modalité/plan/séquence identiques normal = patho et conformes au cliché (pour « complet »), ≥ 1 flèche `principale`,
  tip/from dans [0,1], label/role/evidence/confidence présents, confiance `basse` ⇒ label cité dans `a_verifier`.
  Lancer après CHAQUE manifest ; un manifest en erreur s'affiche « erreur » dans l'app (jamais « complet »).
- `python3 scripts/build_app.py [--external] [--include-test]` → `app/Radio_Paires.html` (hors-ligne, images en data URI ; `--external` = liens vers images/).
- `python3 scripts/screenshot.py` → captures `shots/*.png` + contrôle console sans erreur.
- Manifests de test : `manifest/TEST-*.json` (ignorés par défaut, `--include-test` pour les voir) — à supprimer après essai.

## Consigne Vial 2026-11-14 01:02 : ordre INVERSE (fin → début) dans chaque lot ; cadres de noms fermés par défaut, ouverts au clic sur le numéro.

## REPRISE — ordre impératif (MAJ 2026-11-14 01:25)
Source unique : `imagerie_GROK/BESOINS_IMAGES.html` (remplace l'ancien « Clichés à réunir »). Extraire ses tableaux avant tout.
1. **A. Imagerie (IMG-001…344)** d'abord, ordre inverse 344 → 001 ; reprendre les manifests existants.
2. **C. Explorations fonctionnelles (EXP-001…153)** une fois A achevé : paire tracé normal + pathologique, mêmes règles (licence, appariement, flèches, manifest). Courbes ventilatoires et tests dynamiques/métaboliques : schémas dessinés par script, sources de valeurs citées.
