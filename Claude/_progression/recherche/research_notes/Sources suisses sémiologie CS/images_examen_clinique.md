# Images et vidéos réelles sous licence libre pour l'examen clinique (surtout neurologique)

Relevé du 14.11.2026. Les comptes Commons ont été obtenus par l'API (`prop=categoryinfo`, `list=search`, `prop=imageinfo&iiprop=extmetadata`) et les licences ont été lues dans les métadonnées de chaque fichier (champ `LicenseShortName`). Les pages NOVEL, Utah NeuroLogic Exam, Stanford, MediaWiki et WMF ont été lues dans leur texte intégral. La recherche suisse s'est limitée à des résumés de moteur. Aucune image générée par IA n'a été retenue.

## 1. Wikimedia Commons : catégories, comptes, licences, accès API

### Takeaway
Commons couvre bien les signes généraux (hippocratisme, ictère, œdème, xanthélasma, anisocorie, paralysie faciale, papillœdème, Kayser-Fleischer) avec des photos réelles sous CC BY, CC BY-SA ou dans le domaine public. Pour les manœuvres neurologiques, la couverture est mince : quelques fichiers seulement pour le Babinski, le réflexe rotulien, le Romberg, le Kernig et le Brudzinski, souvent des gravures anciennes (Gowers 1886-1907, Medical diagnosis 1922). L'accès par API demande un User-Agent descriptif et des largeurs de miniature standard.

### Cited Findings
**Comptes par catégorie** (fichiers directs / sous-catégories, API du 14.11.2026). Source : API Commons, par exemple [Category:Physical examinations](https://commons.wikimedia.org/wiki/Category:Physical_examinations).
- Catégorie mère : `Physical examinations` 204/38. Elle contient notamment Abdominal examination, Auscultation, Palpation, Percussion (medicine), Romberg's test, Monofilament testing, Tongue examination, Nail examinations, Musculoskeletal examination et Vital signs.
- Les noms anglais intuitifs « Physical examination » et « Neurological examination » n'existent pas sur Commons. Les noms réels sont `Physical examinations` et `Neurological tests` (3/7, avec Reflexes, HINTS-test, Equilibrioception tests, EMG et EEG).
- Réflexes :
  - `Reflexes` 26/18 (sous-catégories : Plantar reflex, Stretch reflexes, Triceps reflex, Corneal reflex, Chaddock reflex, Pupillary light reflex, Primitive reflexes, Videos of reflexes, Reflex hammers) ;
  - `Patellar reflex` 8/1 ;
  - `Plantar reflex` 0/2, qui mène à `Babinski's sign` 4/1 ;
  - `Triceps reflex` 1 ; `Corneal reflex` 1 ; `Chaddock reflex` 1 ; `Pupillary light reflex` 10 (surtout des schémas) ; `Reflex hammers` 32 ;
  - aucune catégorie « Achilles reflex » ni « Ankle jerk ».
- Méningés et coordination : `Romberg's test` 2 ; `Brudziński's sign` 2 (fichiers non listés, API muette au second appel) ; aucune catégorie Kernig, mais un fichier `Kernig's sign cerebrospinal meningitis.jpg` dans le domaine public ; aucune catégorie finger-nose, heel-shin ou pronator drift.
- Yeux :
  - `Anisocoria` 7/1 ; `Miosis` 8 ; `Mydriasis` 6 ; `Horner's syndrome` 6 (surtout des schémas et des animaux) ; `Ptosis (eyelid)` 22/7 ; `Nystagmus` 17/2 (GIF et .ogv) ; `Strabismus` 29/13 ;
  - `Ocular fundus` 61/5, dont `Fundus of papilledema` 2 ; `Ophthalmoscopy` 18 ; `Visual field test` 8/2 ; `Hemianopsia` 2/3.
- Neuromusculaire et neurologie :
  - `Fasciculation` 9 (liste non obtenue, à vérifier) ; `Muscle atrophy` 17/2 ; `Tremor` 24/1 (surtout des vidéos .ogv d'articles PLOS/BMC) ; `Ataxia` 16/2 ; `Cerebellar ataxia` 5/2 ;
  - `Bell's palsy` 29/2, dont une série allemande de photos d'un même patient de J1 à J19 avec le signe de Charles Bell (`Fazialislähmung Tag 05 Bell-Phänomen`) ; `Facial nerve paralysis` 16/4 ;
  - `Foot drop` 10 ; `Gowers' sign` 3 ; `Myasthenia gravis` 10 ; `Monofilament testing` 3 ; `Rinne test` 2 ; `Weber test` 2 ; `Tuning forks` 104 ; `Snellen charts` 39 ;
  - aucune catégorie Asterixis, Spasticity, Clonus, Hoffmann's sign ni Gait disorders.
- Signes généraux :
  - `Nail clubbing` 16 ; `Jaundice` 36/2 ; `Edema` 63/20 ; `Xanthelasma` 14 ; `Spider angioma` 8 ; `Palmar erythema` 1 ; `Caput medusae` 2 ; `Gynecomastia` 45 ; `Cyanosis` 24 ; `Ascites` 25 ; `Jugular venous pressure` 4 ;
  - `Petechiae` 14 ; `Splinter hemorrhage` 2 ; `Osler's node` 2 ; `Arcus senilis` 7 ; `Goiters` 89 ; `Exophthalmos` 26 ; `Acromegaly` 62 ; `Cushing's syndrome` 18 ; `Acanthosis nigricans` 20 ;
  - `Tophus` 34 ; `Dupuytren's contracture` 39 ; `Erythema nodosum` 13 ; `Pectus excavatum` 15 ; `Lymphadenopathy` 4/17 ; `Medical signs` 12/3.
- Planches d'anatomie : `Gray's Anatomy plates` compte 528 fichiers et 19 sous-catégories.

**Fichiers candidats et licences lues** (API `extmetadata`). Source : [Commons](https://commons.wikimedia.org/wiki/Main_Page), page de chaque fichier.

| Fichier | Licence | Contenu |
|---|---|---|
| `'Knee Jerk' from W R Gowers' Manual of Diseases of the Nervous System 1886.jpg` | domaine public | gravure de Gowers montrant le réflexe rotulien |
| `Knee-jerk. Wellcome L0014111.jpg`, `The knee jerk Wellcome L0022447.jpg` | CC BY 4.0 | Wellcome Collection |
| `Patelar.JPG` | domaine public | réflexe rotulien |
| `BabinskiSign.jpg` | domaine public | photo réelle, pied droit |
| `Babinski-newborn.jpg` | CC BY-SA 3.0 | nourrisson |
| `Babinski's sign (de).png` | CC BY-SA 3.0 | dessin légendé en allemand |
| `Kernig's sign cerebrospinal meningitis.jpg` | domaine public | photo historique, Harlem Hospital, planche 12 |
| `Romberg.jpg` | CC BY-SA 3.0 | « Signe de Romberg » |
| `CCG Romberg-Test.png` | CC BY-SA 4.0 | image extraite d'une vidéo, Maluck et Langenberg |
| `Clubbed fingers.JPG` | CC BY-SA 4.0 | hippocratisme digital |
| `Clubbing of fingers.jpg` | CC BY-SA 3.0 | hippocratisme digital |
| `Schamroths.jpg` | CC BY 3.0 | signe de Schamroth négatif |
| `Jaundice eye.jpg` | domaine public | ictère scléral, CDC |
| `Scleral Icterus.jpg` | CC BY 4.0 | ictère scléral |
| `Combinpedal.jpg` | CC BY-SA 3.0 | œdème prenant le godet, J. Heilman |
| `Papilledema.jpg` | CC BY 3.0 | J. Trobe, Kellogg Eye Center |
| `Fundal photograph showing severe papilloedema in the right eye.jpg` | CC BY 2.0 | papillœdème sévère |
| `Kayser-Fleischer ring.jpg` | CC BY 3.0 | anneau de Kayser-Fleischer |
| `Anisocoria.jpg` | CC BY 3.0 | anisocorie |
| `Miosis.jpg` | CC BY 2.5 | myosis |
| `Xanthelasma.jpg` | CC BY 3.0 de | xanthélasma |
| `Eyelid Xanthelasma.jpg` | CC BY-SA 3.0 | xanthélasma palpébral |
| `Arm and hand of a patient with xanthelasma … Wellcome L0061148.jpg` | CC BY 4.0 | aquarelle, Wellcome |
| `Parkinsonian gait indoor 01.jpg` | CC BY 4.0 | marche parkinsonienne |
| `Trendelenburg gait.jpg` | CC BY 4.0 | marche de Trendelenburg |

**Manuels anciens dans le domaine public.** Source : recherche de fichiers sur Commons.
- Les scans de Gowers, *A manual of diseases of the nervous system* (1886, 1888, 1892, 1907), existent sous deux formes : des PDF complets issus d'Internet Archive et des figures isolées issues de « Internet Archive Book Images ».
- Ces figures portent la mention de licence « No restrictions ». Exemple : `A manual of diseases of the nervous system (1892) (14781216544).jpg`, une amyotrophie faciale (fig. 158).
- Autres sources du même type : *Medical diagnosis for the student and practitioner* (1922, « No restrictions »), *Diseases of the nervous system* (1915) et les dessins parkinsoniens de Gowers (`Drawings of a Parkinson patient by William Gowers.jpg`).

**Vidéos sur Commons.**
- Commons héberge des vidéos `.ogv` importées des suppléments d'articles en libre accès (PLOS, BMC), par exemple un tremblement psychogène (4 fichiers, J Med Case Rep, 2011), le syndrome parkinsonien après H1N1 et des nystagmus. Leur licence d'origine est CC BY. Source : [Category:Tremor](https://commons.wikimedia.org/wiki/Category:Tremor), [Category:Nystagmus](https://commons.wikimedia.org/wiki/Category:Nystagmus).
- Une recherche `filemime:video/webm` n'a trouvé aucune vidéo d'examen neurologique, de fasciculation ou de Babinski. Source : recherche API Commons, 14.11.2026.

**Accès par API.**
- Le User-Agent est obligatoire, au format `<client>/<version> (<contact>) <lib>/<version>`. Les valeurs génériques (« curl », « Python-urllib ») sont à proscrire, et une requête sans en-tête descriptif peut recevoir une erreur 403. Source : [Politique User-Agent WMF](https://foundation.wikimedia.org/wiki/Policy:Wikimedia_Foundation_User-Agent_Policy).
- Les largeurs de miniature standard sont 20, 40, 60, 120, 250, 330, 500, 960, 1280, 1920 et 3840 px.
  - Une URL directe dont la largeur n'est pas standard est rejetée et peut recevoir une erreur 429.
  - Une largeur demandée par `imageinfo&iiurlwidth=` est arrondie à la valeur standard supérieure.
  - Source : [Common thumbnail sizes](https://www.mediawiki.org/wiki/Common_thumbnail_sizes), page modifiée le 20.10.2026.

### Inferences
- Le script devrait procéder ainsi :
  1. viser les catégories exactes listées ci-dessus, puis compléter par `list=search&srnamespace=6` ;
  2. lire `LicenseShortName`, `Artist` et `AttributionRequired` dans `extmetadata` ;
  3. garder seulement les licences PD, CC0, CC BY et CC BY-SA, et rejeter tout fichier marqué NC ou ND ;
  4. demander `iiurlwidth=330` ou `500` ;
  5. faire une pause d'environ 1 s entre deux lots de 25 titres.
- Les fichiers CC BY-SA obligent à publier sous la même licence l'image modifiée (recadrage légendé). Mieux vaut l'intégrer sans la modifier, avec l'attribution et le lien vers la licence.
- La recherche plein texte est bruitée : « finger nose » renvoie des avions immatriculés VH-FNT, « Hoffmann » des noms propres. Un contrôle humain ou un filtrage par catégorie reste nécessaire.

### Gaps
- Les fichiers des catégories `Fasciculation` (9) et `Brudziński's sign` (2) n'ont pas été listés : l'API a renvoyé une réponse vide au second appel. Leur nature et leur licence sont à vérifier.
- Le caractère réel (photo de patient ou schéma) des fichiers de `Ptosis (eyelid)`, `Gowers' sign`, `Foot drop` et `Fasciculation` n'a pas été contrôlé un par un.

## 2. Figures en libre accès, NIH/NLM, NOVEL, Stanford Medicine 25, facultés suisses

### Takeaway
Les figures en libre accès de Europe PMC sous CC BY sont la meilleure réserve de photos réelles de signes rares (papillœdème, hippocratisme, Kayser-Fleischer, paralysie faciale, Horner). La licence doit cependant être revérifiée article par article. Les ressources suivantes ne conviennent pas pour une reprise directe :
- NOVEL est sous CC BY-NC-ND, donc un drapeau NC et ND ;
- l'examen neurologique de l'Université d'Utah est sous CC BY-NC-SA, donc un drapeau NC ;
- Stanford Medicine 25 n'a pas de licence ouverte (tous droits réservés) ;
- aucune vidéo sous licence libre n'a été trouvée à l'UNIGE, à l'UNIL ni au CHUV.

### Cited Findings
**Europe PMC.** Requêtes REST `FIG:"…" AND LICENSE:"cc by"` envoyées le 14.11.2026 à [l'API Europe PMC](https://www.ebi.ac.uk/europepmc/webservices/rest/search). Nombre d'articles :

| Requête FIG | Articles | Exemple ou remarque |
|---|---|---|
| Babinski | 39 | PMC12704114, « other Babinski sign » dans le spasme hémifacial |
| Kernig | 1 | hors sujet |
| Brudzinski | 1 | PMC5827054, étude de précision diagnostique (tableau probable) |
| fasciculations | 56 | |
| Romberg | 140 | bruité |
| asterixis | 143 | très bruité : les premiers résultats sont hors sujet |
| papilledema | 279 | |
| clubbing | 217 | PMC13091931, hippocratisme acquis |
| xanthelasma | 35 | |
| Horner syndrome | 36 | |
| ptosis + oculomotor | 43 | |
| Kayser-Fleischer | 52 | |
| Hoffmann sign | 2 | |
| pronator drift | 3 | figures de capteurs, pas de photos |
| winged scapula | 19 | |
| Gowers sign | 2 | PMC7752564, myopathie de Duchenne |
| facial palsy | 222 | |
| Lasegue | 4 | |
| Babinski + `cc by-nc` | 8 | à exclure |

**NOVEL (Université d'Utah).** « All materials within … NOVEL are licensed by a Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International License ». Le droit d'auteur reste aux auteurs. Source : [NOVEL Copyright](https://novel.utah.edu/copyright/).
- La collection NOTE (99 vidéos d'examen neuro-ophtalmologique) exige une licence payante TDS. Source : [NOVEL About](https://novel.utah.edu/about/).
- Une page liée à la NANOS exige en plus de demander la permission. Cette contradiction n'est pas résolue. Source : [résultat de recherche NOVEL](https://novel.utah.edu/about/copyright/).

**NeuroLogic Examination (Larsen et Stensaas, Utah et Nebraska).** Plus de 250 vidéos de patients réels, couvrant l'état mental, les nerfs crâniens, la coordination, la sensibilité, la motricité et la marche.
- Licence : « Creative Commons Attribution-NonCommerical-ShareAlike ». Le lien pointe vers la version 4.0, mais les liens « Deed » et « Legal Code » pointent vers la 2.5 : la page est incohérente.
- Les vidéos se téléchargent en ZIP protégés par un mot de passe que le site fournit.
- Source : [Copyright NeuroLogic Exam](https://neurologicexam.med.utah.edu/adult/html/copyright.html).

**Stanford Medicine 25.**
- Le pied de page n'indique que « ©2026 Stanford University » et renvoie aux conditions générales de Stanford. Source : [Stanford Medicine 25](https://stanfordmedicine25.stanford.edu/).
- Ces conditions limitent le téléchargement à l'usage personnel non commercial (« only for User's own personal, non-commercial use ») et interdisent de « copy, reproduce, retransmit, distribute, publish ». Elles ne mentionnent aucune licence Creative Commons. Source : [Stanford Terms of Use](https://www.stanford.edu/site/terms/).

**Université du Cap.** Vidéo d'examen neurologique de R. Eastman sous CC BY-NC-ND 3.0, signalée par un résumé de recherche (non lu sur la page source). Source : [OER Africa](https://www.oerafrica.org/resource/examination-nervous-system-video-tutorial.md).

**Suisse.**
- Aucune vidéo d'examen neurologique sous licence Creative Commons n'a été trouvée à l'UNIGE, à l'UNIL ni au CHUV. Sources : recherches web du 14.11.2026 ; [document UNIGE AMC2](https://www.unige.ch/medecine/download_file/view/7287/1971).
- Une revue médicale suisse de 2019 décrit la plateforme « virtual skills » de l'UNIL : des vidéos d'examen clinique réservées aux étudiants. Source : [Serval UNIL](https://serval.unil.ch/resource/serval:BIB_3CF763C8A52A.P001/REF), lu dans un résumé.
- Cette plateforme est issue du Swiss Virtual Campus (2004), validé par cinq facultés suisses, sous l'adresse virtualskillslab.net. Source : [présentation Bonvin 2004](https://library.med.utah.edu/publishing/slice/2004/friday_auditorium/04_07_02_AM_rbonvin.pdf). Son accès actuel et sa licence ne sont pas vérifiés.

### Inferences
- `LICENSE:"cc by"` semble aussi correspondre à des variantes comme cc by-nc (une requête séparée cc by-nc renvoie 8 résultats pour Babinski). Le script devrait donc lire le champ `license` de chaque article (`resultType=core`, ou le XML JATS `<license>`) et ne garder que `cc by`, `cc by-sa` et `cc0`.
- Le terme `FIG:` ramène des articles où le mot apparaît ailleurs que dans une légende pertinente, comme le montrent les résultats « asterixis ». Le tri humain des légendes est indispensable.
- NOVEL (NC-ND), l'examen neurologique d'Utah (NC-SA) et l'Université du Cap (NC-ND) sont à signaler comme NC. Un site éducatif public sans but commercial pourrait se discuter, mais la règle « libre seulement » les exclut. Ils peuvent au mieux servir de liens externes, sans intégration.
- Pour une source suisse réelle, il faudrait écrire aux facultés (UNIL « virtual skills », UNIGE, HUG) pour obtenir une autorisation : c'est une décision de Vial.
- Les images des NIH et du CDC (par exemple `Jaundice eye.jpg`, PHIL) sont dans le domaine public américain. Leur statut en Suisse est généralement accepté sur Commons.

### Gaps
- Open-i (NLM) n'a pas été interrogé : la licence suit celle de l'article PMC source.
- Le site de la Wellcome Collection n'a pas été interrogé directement : ses fichiers vus sur Commons sont sous CC BY 4.0.
- Les conditions de réutilisation des serveurs vidéo UNIGE (mediaserver) et UNIL n'ont pas été trouvées. Elles sont « À vérifier » par un contact direct.
- La licence des vidéos neuroexam.com (OUP) n'a pas été trouvée.

## 3. Manœuvres et signes sans image libre trouvée (à fournir par un humain)

### Takeaway
Aucune image réelle et libre n'a été trouvée sur Commons pour la plupart des manœuvres dynamiques de l'examen neurologique. Il faudra filmer ou photographier sur place, avec le consentement du patient ou d'un figurant, ou bien chercher article par article dans Europe PMC.

### Cited Findings
Absences sur Commons (14.11.2026) : aucune catégorie et aucun fichier pertinent dans les 10 premiers résultats de recherche. Source : API Commons.
- **Doigt-nez et talon-genou :** la recherche ne renvoie que du bruit (avions VH-FNT, livres de recettes).
- **Pronator drift (épreuve des bras tendus) :** 4 résultats, tous hors sujet.
- **Signe de Hoffmann :** seulement des noms propres.
- **Astérixis :** 5 résultats, dont aucune image (un fichier audio de prononciation, des PDF).
- **Lasègue :** plaques de rue et PDF anciens.
- **Réflexe achilléen et clonus :** aucune catégorie.
- **Spasticité, rigidité, dysdiadococinésie, réflexe nauséeux, déviation de la langue, champ visuel par confrontation :** aucune catégorie. Il existe seulement `Tongue examination` dans `Physical examinations`, à examiner.
- **Fasciculations :** une catégorie de 9 fichiers existe, mais aucune vidéo `.webm`. Une photo statique est de toute façon peu utile pour ce signe.
- **Démarche hémiplégique (en fauchage) :** aucun résultat.
- **Réflexes bicipital et stylo-radial :** seule la catégorie `Triceps reflex` (1 fichier) existe.

Couvertes seulement par des gravures anciennes ou une ou deux photos (source : tableau de la section 1) :
- **Kernig :** une photo historique dans le domaine public.
- **Brudzinski :** 2 fichiers, non vérifiés.
- **Romberg :** 2 images sous CC BY-SA.
- **Réflexe rotulien :** gravures de Gowers et de la Wellcome Collection, plus une photo dans le domaine public.

### Inferences
- Liste à confier à un humain, par ordre de priorité :
  1. doigt-nez ;
  2. talon-genou ;
  3. épreuve des bras tendus (Barré, Mingazzini) ;
  4. Hoffmann ;
  5. réflexe achilléen ;
  6. réflexes bicipital et stylo-radial ;
  7. clonus ;
  8. astérixis (vidéo) ;
  9. fasciculations (vidéo) ;
  10. Lasègue ;
  11. Brudzinski (si les 2 fichiers ne conviennent pas) ;
  12. examen des nerfs crâniens (champ visuel par confrontation, oculomotricité, langue, voile du palais) ;
  13. démarches pathologiques autres que parkinsonienne et Trendelenburg.
- Une photo prise par un enseignant suisse avec un figurant consentant, publiée sous CC BY 4.0, réglerait à la fois la licence et la protection des données personnelles (pas de visage identifiable).

### Gaps
- Europe PMC n'a pas été inspectée figure par figure pour ces manœuvres. Seuls les nombres d'articles sont connus (par exemple Hoffmann 2, pronator drift 3, Lasègue 4). Certaines y ont peut-être une photo CC BY utilisable.
