# Jeux de données radiologiques ouverts et Radiopaedia : sources d'images NORMALES et PATHOLOGIQUES

Recherche du 13.11.2026. Usage visé : site éducatif public, gratuit, non commercial, en Suisse.
Légende des restrictions : **NC** = non commercial ; **ND** = pas d'œuvre dérivée ; **SA** = partage à l'identique ; **DUA** = accord d'utilisation signé ; **CRED** = accès accrédité (formation, compte vérifié).
Avertissement méthode : radiopaedia.org (licence, conditions d'utilisation) répondait HTTP 402 à WebFetch ; ses conditions ne sont connues que par extraits de recherche. Les pages de CheXpert, MURA, NIH (Box) et des PDF RSNA n'ont pas pu être lues. Toute ligne marquée « À vérifier » doit être relue sur la page source avant publication.

## Quels jeux donnent des images normales légalement réutilisables, prêtes à voir, par région et modalité ?

### Takeaway
Seuls quelques jeux autorisent clairement la republication d'images sur un site public : TCIA (la plupart des collections en CC BY 3.0/4.0, dont LIDC-IDRI), IXI (IRM cérébrale normale, CC BY-SA 3.0), MedMNIST (CC BY 4.0, sauf DermaMNIST NC) et NIH ChestX-ray14 (« aucune restriction », attribution demandée). MIMIC-CXR, VinDr-CXR (PhysioNet, CRED + DUA « ne pas partager les données »), OASIS (candidature, recherche académique) et CheXpert/MURA (accord de recherche Stanford, NC) **ne conviennent pas** à la republication d'images ; Radiopaedia et CQ500 sont NC-SA, donc utilisables pour un site non commercial à condition d'attribuer et de garder la même licence.

### Cited Findings

**TCIA (The Cancer Imaging Archive)**
- La plupart des données sont sous CC BY 3.0 ou CC BY 4.0 : « Most data are freely available to browse, download, and use for commercial, scientific and educational purposes. » — [TCIA Data Usage Policies](https://www.cancerimagingarchive.net/data-usage-policies-and-restrictions/)
- Un petit nombre de collections portent une licence CC avec restriction commerciale (NC) ; cette option n'est plus offerte aux nouveaux dépôts ; la licence de chaque collection figure dans son tableau « Data Access » — [TCIA Data Usage Policies](https://www.cancerimagingarchive.net/data-usage-policies-and-restrictions/)
- Les collections soumises à DUA sont désormais hébergées par le NCI Cancer Research Data Commons, avec demande via dbGaP (politique NIH d'avril 2025) — [TCIA Data Usage Policies](https://www.cancerimagingarchive.net/data-usage-policies-and-restrictions/)
- Tout utilisateur s'engage à ne pas tenter d'identifier ni de contacter les participants ; les redistributeurs doivent attribuer chaque jeu et exiger la même attribution en aval — [TCIA Data Usage Policies](https://www.cancerimagingarchive.net/data-usage-policies-and-restrictions/)
- API REST publique (NBIA Search) : base `https://services.cancerimagingarchive.net/nbia-api/services/v1`, points `getSeries`, `getImage` (ZIP de la série, fichier de licence inclus) ; plus de clé API requise pour les collections publiques ; les collections restreintes passent par l'API authentifiée — [TCIA REST API Guide](https://wiki.cancerimagingarchive.net/display/Public/TCIA+REST+API+Guide)
- Couverture : oncologique (patients porteurs de cancer) ; format DICOM natif.

**LIDC-IDRI (sur TCIA)**
- Licence CC BY 3.0 pour images, annotations XML et métadonnées ; citation avec DOI obligatoire — [TCIA LIDC-IDRI](https://www.cancerimagingarchive.net/collection/lidc-idri/)
- 1 010 sujets, 1 308 études, 244 527 images DICOM (CT, DX, CR) ; ≈ 133 Go ; la description dit 1 018 cas (incohérence interne) — [TCIA LIDC-IDRI](https://www.cancerimagingarchive.net/collection/lidc-idri/)
- Téléchargement des images par TCIA Data Retriever (manifeste) ; annotations en téléchargement direct (8,6 Mo) — [TCIA LIDC-IDRI](https://www.cancerimagingarchive.net/collection/lidc-idri/)

**NIH ChestX-ray14**
- Carte de jeu Hugging Face reprenant les conditions NIH : « no restrictions on the use of the NIH chest x-ray images », avec attribution demandée (lien vers le site NIH, citation de l'article CVPR 2017, mention du NIH Clinical Center) ; le champ licence y vaut « unknown » — [Hugging Face, alkzar90/NIH-Chest-X-ray-dataset](https://huggingface.co/datasets/alkzar90/NIH-Chest-X-ray-dataset/blob/main/README.md)
- Format PNG ; classe « No Finding » présente (À vérifier : effectif exact, ≈ 60 000 selon la littérature, non relu ici).

**RSNA Pneumonia Detection Challenge (2018)**
- Sous-ensemble de 30 000 radiographies issues de NIH CXR14, dont 15 000 positives ; boîtes tracées par six radiologues certifiés — [arXiv 1811.08939 / revue arXiv 2408.13315](https://arxiv.org/pdf/2408.13315) ; [RSNA, page du défi](https://www.rsna.org/rsnai/ai-image-challenge/rsna-pneumonia-detection-challenge-2018)
- Licence : régie par les règles de la compétition Kaggle ; non confirmée ici — [RSNA](https://www.rsna.org/rsnai/ai-image-challenge/rsna-pneumonia-detection-challenge-2018)

**RSNA Intracranial Hemorrhage (2019)**
- > 25 000 scanners crâniens annotés (présence, localisation, type d'hémorragie) ; conditions dans un PDF « Terms of Use and Attribution » non lu — [RSNA ICH 2019](https://www.rsna.org/rsnai/ai-image-challenge/rsna-intracranial-hemorrhage-detection-challenge-2019)
- Publié « under a non-commercial license » selon RSNA — [RSNA News, avril 2020](https://www.rsna.org/news/2020/april/ai-challenge-dataset)

**RSNA Cervical Spine Fracture (2022)** : aucune condition de licence trouvée ; seule la page de liste RSNA mentionne le défi — [RSNA](https://www.rsna.org/rsnai/ai-image-challenge/rsna-intracranial-hemorrhage-detection-challenge-2019). À vérifier sur Kaggle.

**MIMIC-CXR-JPG (PhysioNet)**
- PhysioNet Credentialed Health Data License 1.5.0 + DUA ; accès réservé aux utilisateurs accrédités ayant suivi la formation CITI ; la DUA impose « the user will not share the data » — [PhysioNet MIMIC-CXR-JPG 2.1.0](https://physionet.org/content/mimic-cxr-jpg/2.1.0/)
- 377 110 JPG (qualité 95, convertis du DICOM), 14 étiquettes CheXpert/NegBio dont « No Finding » ; pas de boîtes — [PhysioNet MIMIC-CXR-JPG](https://physionet.org/content/mimic-cxr-jpg/2.1.0/)

**VinDr-CXR (PhysioNet)**
- Même licence accréditée + DUA ; formation CITI requise — [PhysioNet VinDr-CXR 1.0.0](https://physionet.org/content/vindr-cxr/1.0.0/)
- 18 000 radiographies DICOM ; entraînement : 10 606 normales / 4 394 anormales ; test : 2 052 normales / 948 anormales ; 22 anomalies locales localisées par **boîtes englobantes** — [PhysioNet VinDr-CXR](https://physionet.org/content/vindr-cxr/1.0.0/)

**CheXpert, MURA (Stanford AIMI)**
- Jeux disponibles « without charge for non-commercial research purposes » ; CheXpert exige l'acceptation d'un Research Use Agreement — [Stanford AIMI](https://aimi.stanford.edu/shared-datasets) ; [TensorFlow Datasets, CheXpert](https://www.tensorflow.org/datasets/catalog/chexpert?hl=cs)
- MURA « freely available » selon l'article ; aucun texte de licence trouvé — [arXiv 1712.06957](https://arxiv.org/pdf/1712.06957.pdf)

**MedMNIST**
- CC BY 4.0 pour tous les jeux sauf DermaMNIST (CC BY-NC 4.0) ; code Apache-2.0 ; résolutions 28, 64, 128, 224 px (2D) et 28³/64³ (3D) ; modalités radiographie, OCT, échographie, CT, microscopie électronique — [medmnist.com](https://medmnist.com/)

**IXI (IRM cérébrale normale)**
- CC BY-SA 3.0 ; près de 600 sujets « normal, healthy » ; T1, T2, PD, MRA, DTI (15 directions) ; NIfTI ; archives .tar en téléchargement direct — [IXI Dataset](https://brain-development.org/ixi-dataset/)

**OASIS**
- « non-commercial, academic research purposes only » ; accès sur candidature, hébergement NITRC-IR ; interdiction de reconstruire un visage ; stockage sécurisé, destruction à la fin du projet — [OASIS Brains](https://sites.wustl.edu/oasisbrains/)
- OASIS-3 : 755 adultes cognitivement normaux ; T1w, T2w, FLAIR, ASL, SWI, TOF, BOLD, DTI ; TEP — [OASIS Brains](https://sites.wustl.edu/oasisbrains/)

**BraTS / UPenn-GBM**
- BraTS 2021 Segmentation Training et Classifier Training listés CC BY 4.0 sur TCIA ; un jeu de validation marqué « TCIA Restricted » ; jeu test séquestré sur Synapse (syn25829067) ; UPENN-GBM en CC BY 4.0 — [TCIA wiki BraTS 2021](https://wiki.cancerimagingarchive.net/x/GgdgCQ) ; [TCIA wiki](https://wiki.cancerimagingarchive.net/x/ewJdC)
- Les NIfTI d'entraînement sont « brain-extracted » (crâne retiré) — [TCIA wiki](https://wiki.cancerimagingarchive.net/x/gwCFD)

**CQ500 (scanner crânien, Qure.ai)**
- Licence CC BY-NC-SA ; 491 scanners crâniens, 205 positifs pour hémorragie ; vérité terrain = consensus de trois radiologues ; fractures de la voûte, déviation de la ligne médiane, effet de masse — [Qure.ai blog](https://qure.ai/blog/challenges-of-development-validation-of-deep-learning-for-radiology) ; [PhysioNet BHX](https://physionet.org/content/bhx-brain-bounding-box/)

**Échographie / Doppler**
- BUSI : licence « Not stated » (article source en CC BY 4.0) ; CAMUS (échocardiographie) : CC BY-NC-SA 4.0 — [arXiv 2609.19230, audit de licences](https://arxiv.org/pdf/2609.19230)
- BUS-BRA (Zenodo, « Open ») : licence non confirmée — [Zenodo 7730709](https://zenodo.org/records/7730709)

**Radiopaedia**
- Images sous licence CC BY-NC-SA 3.0 Unported **modifiée** ; attribution : nom du contributeur + Radiopaedia.org, avec liens vers le cas, la page d'accueil et la page de licence ; pas de filigrane ; tout usage hors de cette licence exige l'accord écrit du contributeur (ou de Radiopaedia s'il a délégué ce droit) ; le **texte** des articles devient propriété de Radiopaedia — [Radiopaedia, Licence](https://images.radiopaedia.org/licence) ; [Radiopaedia, Terms](https://radiopaedia.org/terms?lang=us) (extraits de recherche, pages non lisibles : HTTP 402)
- La licence NC-SA par défaut rend ces images inéligibles à Wikimedia Commons/Wikipédia — [Radiopaedia, article « images »](https://radiopaedia.org/articles/images?lang=us)
- Radlines, alternative sans but lucratif, utilise CC BY 4.0 par défaut et dépose la plupart de ses images sur Wikimedia Commons — [Radlines](https://radlines.org/Radiopaedia)

### Inferences
- **Radiographie thoracique normale** : NIH ChestX-ray14 (PNG, « No Finding ») est la source la plus simple à republier, attribution comprise. VinDr-CXR et MIMIC sont exclus (DUA « ne pas partager »).
- **IRM cérébrale normale par séquence** : IXI (T1, T2, PD, MRA, DTI) en CC BY-SA 3.0 ; obligation de publier les dérivés (coupes PNG) sous CC BY-SA. Pas de FLAIR ni de SWI dans IXI ; OASIS-3 les a, mais ses conditions interdisent la republication.
- **Scanner cérébral normal** : aucune source CC BY claire trouvée. CQ500 (NC-SA, 491 scanners dont ≈ 286 sans hémorragie) est la meilleure option pour un site non commercial, sous réserve de relire la licence exacte.
- **Scanner abdominal « normal »** : TCIA ne contient que des patients oncologiques ; des coupes de régions non atteintes peuvent servir d'anatomie normale (CC BY), à étiqueter « coupe sans lésion visible » et non « sujet sain ».
- **Échographie** : aucune source CC BY confirmée ; CAMUS est NC-SA. Wikimedia Commons reste la voie la plus sûre, au cas par cas.
- **Radiopaedia** : un site éducatif suisse non commercial peut réutiliser ses images sous CC BY-NC-SA 3.0 avec attribution complète et licence identique pour les dérivés (flèches numérotées = dérivé → NC-SA). Le **scraping massif** reste juridiquement incertain (conditions non lues) ; récupération manuelle et cas par cas, ou demande écrite à Radiopaedia.
- **Images « Radiopaedia » sur Wikimedia Commons** : suspectes par défaut, car NC-SA est incompatible avec Commons ; ne réutiliser que si la page Commons montre une licence libre accordée par l'auteur lui-même.
- **Licence la plus contraignante du lot = celle du site** : mélanger CC BY-SA (IXI) et CC BY-NC-SA (Radiopaedia, CQ500) sur une même image composite crée une incompatibilité SA ; garder chaque image sous sa propre licence, légendée individuellement.

### Gaps
- Texte exact des conditions Radiopaedia sur scraping, API et intégration (HTTP 402) ; l'existence d'une API publique Radiopaedia n'a pas été vérifiée.
- Licences exactes des jeux RSNA (ICH, pneumonie, rachis cervical) : PDF et règles Kaggle non lus.
- Texte des accords CheXpert et MURA (clause de redistribution).
- Licence officielle NIH ChestX-ray14 (page Box illisible) ; effectif exact « No Finding ».
- Effectifs « normaux » de CQ500 et termes exacts sur headctstudy.qure.ai.
- Licences d'autres jeux échographiques/Doppler (POCUS, thyroïde, rein, carotide) non recherchées faute de temps.

## Quels jeux fournissent des annotations de lésions (boîtes, masques) pour placer les flèches automatiquement ?

### Takeaway
Boîtes englobantes : VinDr-CXR (22 anomalies, mais DUA), RSNA Pneumonia (boîtes sur images NIH), NIH ChestX-ray14 (≈ 984 boîtes, 8 pathologies), BHX sur CQ500 (hémorragies). Contours/masques : LIDC-IDRI (nodules, XML, CC BY 3.0), BraTS 2021 (masques tumoraux, CC BY 4.0 pour l'entraînement), Seg-CQ500 (51 scanners), BUSI/CAMUS en échographie. Pour un site public, les combinaisons les plus sûres sont LIDC-IDRI + BraTS (CC BY) et NIH/RSNA (sous réserve des règles Kaggle).

### Cited Findings
- VinDr-CXR : boîtes englobantes pour 22 anomalies locales, entraînement et test — [PhysioNet VinDr-CXR](https://physionet.org/content/vindr-cxr/1.0.0/)
- NIH ChestX-ray14 : ≈ 984 boîtes tracées par un radiologue certifié pour 8 pathologies ; le nombre d'images varie selon les sources (880, 980 ou 983) — [Hugging Face, NIH CXR](https://huggingface.co/datasets/alkzar90/NIH-Chest-X-ray-dataset/blob/main/README.md) ; [Emergent Mind](https://api.emergentmind.com/topics/nih-chestx-ray14-dataset)
- RSNA Pneumonia : boîtes sur toutes les images positives (six radiologues), test validé par trois radiologues — [revue arXiv 2408.13315](https://arxiv.org/pdf/2408.13315)
- LIDC-IDRI : lecture en deux phases par quatre radiologues thoraciques ; nodules ≥ 3 mm contourés, < 3 mm et non-nodules ≥ 3 mm marqués ; outil conseillé `pylidc` — [TCIA LIDC-IDRI](https://www.cancerimagingarchive.net/collection/lidc-idri/)
- BHX : boîtes d'hémorragie aiguë par type, sur CQ500, en accès ouvert PhysioNet ; Seg-CQ500 : masques pour 51 scanners — [PhysioNet BHX](https://physionet.org/content/bhx-brain-bounding-box/) ; [Zenodo 8063221](https://zenodo.org/records/8063221)
- MIMIC-CXR : étiquettes au niveau de l'image seulement, pas de boîtes — [PhysioNet MIMIC-CXR-JPG](https://physionet.org/content/mimic-cxr-jpg/2.1.0/)
- RSNA ICH : localisation et type d'hémorragie évalués ; format des étiquettes (par coupe ou par boîte) non précisé sur la page — [RSNA ICH 2019](https://www.rsna.org/rsnai/ai-image-challenge/rsna-intracranial-hemorrhage-detection-challenge-2019)

### Inferences
- Placement automatique d'une flèche : centre de la boîte (x + w/2, y + h/2) ou centroïde du masque (`scipy.ndimage.center_of_mass`), puis flèche tirée depuis l'extérieur de la lésion vers ce point ; pour un masque 3D, choisir la coupe de surface lésionnelle maximale.
- MedMNIST n'a pas d'annotations de localisation (classification seule) et sa résolution (≤ 224 px) est trop faible pour un cours.

### Gaps
- Licence de BHX et de Seg-CQ500 non relue.
- Présence de boîtes ou masques dans RSNA ICH et RSNA rachis cervical non confirmée.

## Quelle chaîne logicielle libre minimale transforme une coupe DICOM en JPEG pédagogique avec fenêtre adaptée ?

### Takeaway
Python + pydicom (lecture DICOM, LUT de modalité) + numpy (fenêtrage) + Pillow (écriture JPEG/PNG) suffit pour le scanner et la radiographie ; SimpleITK ou nibabel lit les volumes NIfTI (IXI, BraTS) ; `pylidc` lit les annotations LIDC. Le fenêtrage est une opération linéaire : clip des UH dans [L − W/2, L + W/2] puis mise à l'échelle 0–255.

### Cited Findings
- L'API TCIA renvoie des séries DICOM en ZIP, sans clé pour les collections publiques — [TCIA REST API Guide](https://wiki.cancerimagingarchive.net/display/Public/TCIA+REST+API+Guide)
- IXI est livré en NIfTI ; MIMIC-CXR-JPG en JPG ; VinDr-CXR et LIDC en DICOM — [IXI](https://brain-development.org/ixi-dataset/) ; [PhysioNet MIMIC-CXR-JPG](https://physionet.org/content/mimic-cxr-jpg/2.1.0/) ; [PhysioNet VinDr-CXR](https://physionet.org/content/vindr-cxr/1.0.0/) ; [TCIA LIDC-IDRI](https://www.cancerimagingarchive.net/collection/lidc-idri/)
- `pylidc` est l'outil recommandé par TCIA pour les annotations LIDC — [TCIA LIDC-IDRI](https://www.cancerimagingarchive.net/collection/lidc-idri/)

### Inferences
Chaîne proposée (connaissances techniques usuelles, pages de documentation non relues dans cette session) :

```python
import numpy as np, pydicom
from pydicom.pixel_data_handlers.util import apply_modality_lut
from PIL import Image, ImageDraw

FENETRES = {            # (largeur W, niveau L) en UH — valeurs usuelles, À vérifier
    "cerveau":   (80, 40),
    "sous_dural":(200, 75),
    "os":        (2000, 500),
    "poumon":    (1500, -600),
    "mediastin": (350, 50),
    "abdomen":   (400, 40),
    "foie":      (150, 30),
}

def dicom_vers_jpeg(chemin, fenetre, sortie, fleches=()):
    ds = pydicom.dcmread(chemin)
    hu = apply_modality_lut(ds.pixel_array, ds)       # RescaleSlope/Intercept -> UH
    W, L = FENETRES[fenetre]
    img = np.clip((hu - (L - W / 2)) / W, 0, 1) * 255
    if getattr(ds, "PhotometricInterpretation", "") == "MONOCHROME1":
        img = 255 - img                               # radiographies inversées
    im = Image.fromarray(img.astype(np.uint8)).convert("RGB")
    d = ImageDraw.Draw(im)
    for n, (x, y) in enumerate(fleches, 1):           # centre de boîte ou centroïde de masque
        d.line([(x + 40, y - 40), (x + 6, y - 6)], fill=(255, 220, 0), width=3)
        d.text((x + 44, y - 56), str(n), fill=(255, 220, 0))
    im.save(sortie, quality=90)
```

- Radiographies (CR/DX) : utiliser `pydicom.pixel_data_handlers.util.apply_voi_lut(arr, ds)` (fenêtre stockée dans le DICOM) plutôt qu'une fenêtre en UH, puis gérer MONOCHROME1.
- NIfTI (IXI, BraTS) : `SimpleITK.ReadImage` → `GetArrayFromImage` → choisir la coupe axiale ; normaliser l'IRM par percentiles (1–99 %), puisque l'IRM n'a pas d'unités absolues.
- Supprimer les métadonnées : écrire un JPEG neuf depuis le tableau de pixels (aucune balise DICOM transmise) ; vérifier l'absence de texte incrusté (nom, date) dans les pixels des radiographies.
- Dépendances toutes libres : `pip install pydicom numpy pillow SimpleITK pylidc` (+ `pylibjpeg`/`gdcm` pour les DICOM compressés JPEG 2000).

### Gaps
- Valeurs de fenêtre non vérifiées sur une source primaire (page Radiopaedia « windowing » illisible, HTTP 402) : à confirmer avant publication.
- Signature exacte des fonctions pydicom (déplacées vers `pydicom.pixels` dans les versions 3.x) non vérifiée.
