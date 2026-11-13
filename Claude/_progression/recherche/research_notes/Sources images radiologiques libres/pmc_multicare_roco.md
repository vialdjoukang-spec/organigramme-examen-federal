# PMC OA, Europe PMC, PubMed MCP, MultiCaRe, ROCOv2: free radiology figures from open-access literature

Research date: 13.11.2026. All endpoint tests were run with curl from this machine on that date, and the counts come from those runs. Tested scripts and downloads were kept in the session scratchpad and are not in the repository.

## 1. Concrete pipeline: query → CC BY figures with caption, image URL, licence and citation

### Takeaway
The best free pipeline uses the **Europe PMC REST search**, with the `FIG:` field to search figure captions plus the `OPEN_ACCESS:y`, `LICENSE:"cc by"` and `PUB_TYPE:"Case Reports"` filters. Each hit then goes through Europe PMC `fullTextXML`, which supplies the per-`<fig>` caption and the article `<license>`. The image comes from the **PMC Cloud Service on AWS** (`pmc-oa-opendata`), which needs no key; a per-article JSON gives `license_code`, the citation and `media_urls`. The old **PMC OA Web Service (oa.fcgi) is dead**: it was retired on 25.08.2026 and returns 404. The old `/pmc/articles/PMCxxx/bin/…` image URLs also return 404.

### Cited Findings
- **The PMC OA Web Service is retired.** The page now reads: "OA Web Service API August 25, 2026 As part of the PMC Article Dataset Changes announced on February 12, 2026, the PMC OA Web Service is no longer available." — [PMC OA service page](https://pmc.ncbi.nlm.nih.gov/tools/oa-service/). Test: `curl "https://www.ncbi.nlm.nih.gov/pmc/utils/oa/oa.fcgi?id=PMC13476372"` → HTTP 404.
- **NLM moved retrieval to the cloud.** NLM's Jan–Feb 2026 bulletin says the PMC Cloud Service on AWS became the primary retrieval source in August 2026, that the OA Web Service is withdrawn, and that individual FTP article packages are discontinued. The old `oa_comm`/`oa_noncomm` prefixes stayed available only until August 2026 — [NLM Technical Bulletin jf26](https://www.nlm.nih.gov/pubs/techbull/jf26/jf26_Changes_to_PMC_ArtDsDistribServs_2026.html); [PMC FTP page](https://pmc.ncbi.nlm.nih.gov/tools/ftp); [PMC AWS page](https://pmc.ncbi.nlm.nih.gov/tools/pmcaws/).
- **The AWS datasets are free.** They are "freely accessible on AWS, without charge, through either an HTTPS or S3 URL, and without any log-in" — [PMC AWS page](https://pmc.ncbi.nlm.nih.gov/tools/pmcaws/) (search-snippet summary).
- **The AWS bucket was tested and works.** `curl "https://pmc-oa-opendata.s3.amazonaws.com/?list-type=2&prefix=PMC13476372"` lists `PMC13476372.1/` with `.json` (957 B), `.xml` (43 KB), `.txt`, `.pdf` (1.3 MB) and two figure JPGs (74 KB and 61 KB). The JSON at `https://pmc-oa-opendata.s3.amazonaws.com/PMC13476372.1/PMC13476372.1.json` holds `"license_code": "CC BY"`, `"citation": "Cureus. 2026 Jul 15;18(7):e112750. doi: 10.7759/cureus.112750"`, the title, the PMID, `is_retracted`, and `media_urls` (s3:// paths to each image). The HTTPS image `https://pmc-oa-opendata.s3.amazonaws.com/PMC13476372.1/cureus-0018-00000112750-i01.jpg` → 200, 74,293 bytes — [AWS bucket, tested](https://pmc-oa-opendata.s3.amazonaws.com/PMC13476372.1/PMC13476372.1.json).
- **Europe PMC fullTextXML gives captions and licence.** `curl "https://www.ebi.ac.uk/europepmc/webservices/rest/PMC13476372/fullTextXML"` → 200, JATS XML. The `<permissions><license>` element reads "Creative Commons Attribution License CC-BY 4.0". Each `<fig id="FIG1">` contains `<label>`, `<caption><title>…</title><p>…</p></caption>` and `<alternatives><graphic xlink:href="cureus-0018-00000112750-i01.jpg">` with processing instructions `<?cloudpmc-path blobs/7c29/13476372/87b017f9c4c0/cureus-…-i01.jpg?>`, original width and height (3000×1568), and scaled size. The FIG1 caption reads "Non-contrast head CT scan showing hyper-densities along basal cisterns with a perimesencephalic hemorrhage pattern (white arrows)" — [Europe PMC fullTextXML, tested](https://www.ebi.ac.uk/europepmc/webservices/rest/PMC13476372/fullTextXML).
- **Three image URL patterns were tested:**
  - `https://cdn.ncbi.nlm.nih.gov/pmc/blobs/7c29/13476372/87b017f9c4c0/cureus-0018-00000112750-i01.jpg` → 200 image/jpeg. This URL is built from the `cloudpmc-path` processing instruction.
  - `https://europepmc.org/articles/PMC13476372/bin/…jpg` → 403.
  - `https://www.ncbi.nlm.nih.gov/pmc/articles/PMC13476372/bin/…jpg` → 404.
  - Source: tests on this machine; see [Europe PMC REST](https://europepmc.org/RestfulWebService).
- **The Europe PMC search and its filters were tested.** Endpoint: `https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=…&format=json&resultType=core&pageSize=…`. In `resultType=core` each record has a `license` field. The values seen were `cc by`, `cc by-nc`, `cc by-nc-nd` and `cc by-nc-sa`. For appendicitis OA case reports the distribution was 140 / 21 / 36 / 3. `LICENSE:"cc by"` matches **only** pure CC BY: the counts are lower than all-OA, so it does not also return BY-NC — [Europe PMC REST](https://europepmc.org/RestfulWebService) (tested).
- **The `FIG:` field searches figure captions.** It returns hit counts for example queries such as `FIG:"subarachnoid hemorrhage" AND FIG:CT AND OPEN_ACCESS:y AND LICENSE:"cc by" AND PUB_TYPE:"Case Reports"` → 361 articles (tested). Caveat: `FIG:` terms can match **different** figures of the same article, so the modality and diagnosis must be re-checked per `<fig>` after download.
- **Five consecutive search calls were all served.** They returned 200 in about 2.9 s in total, with no throttling observed — test on this machine.
- **The PubMed MCP tool was tested.** `mcp__PubMed__get_full_text_article(["PMC13476372"])` returns the identifiers (PMCID, PMID, DOI), title, abstract and plain full text with figure captions as text ("Figure 1 Non-contrast head CT scan showing …"). It returns **no image URLs, no licence and no figure IDs**, and it requires PubMed attribution plus DOI links — [PubMed via MCP; DOI of the test article](https://doi.org/10.7759/cureus.112750).
- **BioC is unusable for very recent PMCIDs.** `https://www.ncbi.nlm.nih.gov/research/bionlp/RESTful/pmcoa.cgi/BioC_json/PMC13476372/unicode` → "No result can be found", and the same happened for PMC7000000. BioC is not usable for this pipeline as tested; it is text-only in any case — test on this machine.
- **Europe PMC also has a supplementary-files endpoint.** `…/rest/PMC13476372/supplementaryFiles` → 200 (a zip of 142 KB) — tested.

### Recommended pipeline (tested pieces)

```
1. SEARCH (Europe PMC):
   GET https://www.ebi.ac.uk/europepmc/webservices/rest/search
       ?query=FIG:"pneumothorax" AND (FIG:radiograph OR FIG:"x-ray") AND OPEN_ACCESS:y
              AND (LICENSE:"cc by" OR LICENSE:"cc0") AND PUB_TYPE:"Case Reports" AND IN_EPMC:y
       &resultType=core&format=json&pageSize=100&cursorMark=*
   → pmcid, doi, title, authorString, journal, pubYear, license
2. FIGURES: GET .../rest/{PMCID}/fullTextXML → for each <fig>: label, caption text, graphic href,
   <?cloudpmc-path ...?>, original-width/height; re-read <permissions><license>
3. IMAGE: https://pmc-oa-opendata.s3.amazonaws.com/{PMCID}.{ver}/{href}
   (find {ver} via ?list-type=2&prefix={PMCID}), or https://cdn.ncbi.nlm.nih.gov/pmc/{cloudpmc-path}
4. LICENCE/CITATION CROSS-CHECK: {PMCID}.{ver}.json → license_code, citation, is_retracted
5. LOCAL FILTER: regex on caption (dx + modality + sequence/view), reject if license_code ∉ {CC BY, CC0, CC BY-SA}
6. OUTPUT ROW: caption | image URL | licence | "Authors, Title, Journal Year; DOI; CC BY 4.0; modified (cropped/annotated)"
```

### Inferences
- Cureus (CC BY) dominates the recent hits. Its figures often have clear single-modality captions such as "Non-contrast head CT … (white arrows)", which makes Cureus a prime supplier.
- `FIG:` + `LICENSE:"cc by"` + `PUB_TYPE:"Case Reports"` is the most precise server-side filter available without downloading a corpus.
- The `{ver}` suffix (`.1`) in the S3 path must be discovered by listing or from the JSON. Later article versions get `.2` and so on.

### Gaps
- No official Europe PMC rate-limit figure was retrieved: the Europe PMC REST documentation page returned 403 to WebFetch. Throttle politely, for example to ≤5 req/s. **To verify.**
- Whether `cdn.ncbi.nlm.nih.gov/pmc/blobs/…` URLs are stable enough for hotlinking is not documented. Download and self-host the images instead; attribution permits this under CC BY.

## 2. Licences per item (CC BY vs NC/ND) and the Swiss public-website constraint

### Takeaway
Licence is **per article**, and every figure inherits it. Only **CC BY, CC BY-SA and CC0** suit a public Swiss teaching site that adds numbered markers, which counts as an adaptation. **CC BY-NC** is risky, and **CC BY-ND / CC BY-NC-ND forbid modified images, so they are unusable with our markers.** Roughly half of OA radiology case-report figures are pure CC BY.

### Cited Findings
- **Europe PMC licence split for appendicitis OA case reports (n=200 sample):** CC BY 140, CC BY-NC-ND 36, CC BY-NC 21, CC BY-NC-SA 3 — [Europe PMC search, tested](https://www.ebi.ac.uk/europepmc/webservices/rest/search).
- **MultiCaRe as a whole is CC BY-NC-SA**, but individual items carry their article's licence. Image counts in v3.0.1: CC BY 72,664; CC BY-NC 33,680; CC BY-NC-SA 32,890; CC0 20. These were counted locally from `captions_and_labels.csv` and match the record's "72K CC BY, 33K CC BY-NC, 32K CC BY-NC-SA, 20 CC0" — [Zenodo MultiCaRe v3.0.1, 10.5281/zenodo.20416562](https://zenodo.org/records/20416562).
- **The MultiCaRe data dictionary lists the licence values:** "CC BY, CC BY-NC-ND, CC BY-NC-SA, CC BY-NC, NO-CC CODE, CC BY-ND and CC BY-SA"; "NO-CC CODE means … the actual license cannot be retrieved through the API". Note: the image file itself contains only CC BY / BY-NC / BY-NC-SA / CC0 — [MultiCaRe data_dictionary.csv](https://zenodo.org/records/20416562).
- **ROCOv2 has a dataset-level Zenodo licence of `cc-by-nc-4.0`** — [Zenodo ROCOv2 10.5281/zenodo.10821435](https://zenodo.org/records/10821435) (API tested).
- **ROCOv2 per-image licences come from `license_information.csv`** (columns ID, PMCID, Attribution, Link). Counted locally: CC BY 60,980; CC BY-NC 18,793; "PUBLIC" 14; "CC" 2 — [Zenodo ROCOv2](https://zenodo.org/records/10821435).
- **ROCOv2 licence rule, quoted from the paper:** "only images from CC BY licensed articles (including CC BY-NC, but excluding CC BY-ND and CC BY-SA) are included" — [ROCOv2 paper, Sci Data 2024, PMC11208523](https://europepmc.org/article/PMC/PMC11208523).
- **The Hugging Face MultiCaRe mirror (OpenMed) declares `cc-by-4.0` in its metadata, while its README says the licence is per article.** Do not trust the mirror header — [HF OpenMed/multicare-images](https://huggingface.co/datasets/OpenMed/multicare-images/blob/main/README.md) (search-snippet).

### Inferences
- **Hard filter: keep `license ∈ {CC BY, CC BY-SA, CC0}`.**
  - Flag CC BY-NC as "NC: avoid". A free educational site is arguably non-commercial, but ambiguity remains, especially if the site ever carries ads or is linked to paid courses.
  - **Exclude any ND licence**, because our numbered markers are a modification.
- **The dataset-level NC licences (MultiCaRe BY-NC-SA, ROCOv2 BY-NC) cover the compilation.** Images taken individually from CC BY articles keep CC BY, but citation must point to the **original article**, not only to the dataset. *Legal interpretation: to verify.*
- **Attribution must name the modification**, for example: "Figure 1 from Author et al., Cureus 2026, doi:…, CC BY 4.0; cropped, original arrows retained, numbered markers added."

### Gaps
- No Swiss-specific legal opinion on CC BY-NC for a free public teaching site was sought; that is out of scope.

## 3. MultiCaRe and ROCOv2: size, format, taxonomy, local filtering

### Takeaway
**Both datasets can be filtered locally by modality and licence** using small CSV/parquet files of about 10–55 MB, without downloading the images. Diagnosis filtering must still rely on caption regex (MultiCaRe) or UMLS CUIs (ROCOv2).
- **MultiCaRe** has better modality, region and view labels, but its images are small: median 14 KB, in webp format, and pre-split from compound figures.
- **ROCOv2** keeps original PMC JPEGs, at better resolution, and contains only non-compound radiology images, but its diagnosis CUIs are automatic.

### Cited Findings
- **MultiCaRe v3.0.1 at a glance:**
  - Published 27.05.2026, DOI 10.5281/zenodo.20416562. Over 76,000 case reports and over 139,000 images.
  - Files: 9 image zips (PMC1–PMC9.zip, 56–918 MB each, ≈2.6 GB of images in total), `captions_and_labels.csv` 53.6 MB, `metadata.parquet` 20.4 MB, `cases.parquet` 168 MB, `case_images.parquet` 55 MB, `abstracts.parquet` 48 MB, `data_dictionary.csv`.
  - Source: [Zenodo API, tested](https://zenodo.org/api/records/20416562).
  - The previous version, v2.1 (zenodo 14994046, 08.03.2025), is 2.87 GB — [Zenodo](https://zenodo.org/records/14994046).
- **MultiCaRe label taxonomy (from `data_dictionary.csv`):**
  - `image_type`: 7 classes (radiology, pathology, chart, endoscopy, medical_photograph, ophthalmic_imaging, electrography).
  - `image_subtype`: 40 classes (x_ray, ct, mri, ultrasound, ekg, …).
  - `radiology_region`: 9 classes; `radiology_region_granular`: 19 classes.
  - `radiology_view`: 12 classes (axial, frontal, transabdominal…).
  - A supervised multilabel column with 89 classes, and a semi-supervised one with 56 more (anteroposterior, lung_window, venogram…).
  - **There is no diagnosis label.** Each row has the caption, licence, patient_id and `case_substring`; `metadata.parquet` carries title, authors, journal, year, DOI, PMID, MeSH and licence, enough for full citation.
  - Source: [Zenodo MultiCaRe](https://zenodo.org/records/20416562).
- **Counts in MultiCaRe v3.0.1, computed locally:**
  - Radiology images: 70,003, of which CC BY: 35,240.
  - By subtype: ct 27,539; mri 20,364; x_ray 13,335; ultrasound 6,085; pet 2,015.
  - Image files are `.webp`; median file_size is 14,206 bytes.
  - Source: local analysis of [captions_and_labels.csv](https://zenodo.org/records/20416562).
- **How the MultiCaRe labels and images were produced:**
  - "Image labels were created based on the contents of their corresponding captions, by using Spark NLP for Healthcare and manual annotations."
  - "Images were preprocessed with OpenCV in order to remove borders and split figures containing multiple images."
  - Images from case reports "may contain burned drawings (such as arrows, circles or asterisks)".
  - Source: [MultiCaRe Data in Brief paper, PMC10792687](https://pmc.ncbi.nlm.nih.gov/articles/PMC10792687).
- **The MultiCaRe `main_image_link` column is filled for only 8,463 / 139,254 rows**, and uses the old `/pmc/articles/…/bin/` pattern, which returned 404 when tested. Rebuild the URLs via the AWS bucket instead — local analysis plus test.
- **ROCOv2 at a glance:**
  - Zenodo v2.0.1 (DOI 10.5281/zenodo.10821435), with 79,789 images and seven modalities.
  - Files: train_images.zip 4.6 GB, valid 0.86 GB, test 0.86 GB (total ≈6.36 GB); captions CSV (train 10 MB); `*_concepts.csv` (automatic UMLS CUIs); `*_concepts_manual.csv` (manual modality, body region and directionality for X-ray); `cui_mapping.csv`; `license_information.csv` 9.4 MB.
  - Source: [Zenodo API, tested](https://zenodo.org/api/records/10821435).
- **How ROCOv2 was built (from the paper):**
  - Concepts were extracted with MedCAT on UMLS.
  - "Concepts for clinical modality, anatomy (X-ray), and directionality (X-ray) were manually curated and additionally evaluated by a radiologist."
  - Images are "JPEG images of various sizes taken directly from PMC … provided exactly as they appear in the PMC Open Access Subset".
  - Compound-figure and radiology classifiers filter to "non-compound radiological images".
  - Source: [ROCOv2 paper PMC11208523](https://europepmc.org/article/PMC/PMC11208523); [Zenodo description](https://zenodo.org/records/10821435).
- **Most frequent manual concepts in ROCOv2 train (local count):** C0040405 20,459; C1306645 "Plain x-ray" 16,441; C0024485 9,790; C0041618 8,305; C0817096 "Chest" 5,260; C0002978 3,958. Several CUIs have no name in `cui_mapping.csv`. In UMLS, C0040405 = X-ray CT, C0024485 = MRI, C0041618 = ultrasonography and C0002978 = angiogram; these names come from general UMLS knowledge and were **not re-verified** here. Local analysis of the [Zenodo ROCOv2](https://zenodo.org/records/10821435) files.
- **The ImageCLEF 2023 versions required a signed user agreement; the public Zenodo release does not** — [Zenodo ROCOv2](https://zenodo.org/records/10821435).

### Inferences
- **Recommended local workflow:**
  1. Download only the metadata: MultiCaRe `captions_and_labels.csv` + `metadata.parquet` (≈75 MB), and ROCOv2 `*_captions.csv` + `*_concepts_manual.csv` + `license_information.csv` (≈25 MB).
  2. Filter on licence, modality and caption regex.
  3. Fetch the selected originals at full resolution from the PMC AWS bucket using the PMCID, rather than downloading the dataset zips.
- **Do not use MultiCaRe image files for display.** At a 14 KB median, webp, re-cropped, they are too small for teaching. Use MultiCaRe as an **index** and take the original from PMC.

### Gaps
- The ROCOv2 per-modality totals across all splits were not recomputed; only the train manual concepts were counted.
- `pyarrow` is not installed, so the `metadata.parquet` columns (MeSH) were not explored. MeSH could improve diagnosis matching.

## 4. Coverage test for typical exam diagnoses

### Takeaway
**There are enough CC BY hits for every test diagnosis except DVT Doppler**, which is weak in the curated datasets but adequate in Europe PMC through `FIG:`. Raw counts overestimate usable images by about 2–5×, because of compound figures, wrong-figure matches and poor quality. Manual radiologist review remains mandatory.

### Cited Findings

**A. Europe PMC article counts, OA + CC BY + Case Reports (tested 13.11.2026)**

Two query styles were compared:
- **TITLE_ABS:** diagnosis and modality terms in the title or abstract.
- **FIG:** terms in the figure captions.

| Diagnosis + modality | TITLE_ABS, OA case reports (all licences) | TITLE_ABS, CC BY | FIG, CC BY case reports | FIG, CC BY all article types |
|---|---|---|---|---|
| SAH + CT | 641 | 260 | 361 | 750 |
| Ischaemic stroke + DWI | 109 | 64 | 306 ("diffusion-weighted" + infarct) | 656 |
| Brain abscess + MRI | 176 | 90 | 87 ("brain abscess", any modality) | 206 |
| Pneumothorax + CXR | 281 | 150 | 1,224 (pneumothorax, any modality) | 2,527 |
| Appendicitis + CT | 764 | 431 | 149 | 307 |
| DVT + Doppler/US | 424 | 245 | 86 | 167 |
| Aortic dissection + CT/angio | 500 | 294 | n/t | n/t |
| PE + CTPA | 68 | 43 | n/t | n/t |

Source: [Europe PMC REST search](https://www.ebi.ac.uk/europepmc/webservices/rest/search) (tested; counts are articles, not figures).

**B. Image-level counts in the curated datasets (caption regex, computed locally)**

- **MultiCaRe** columns:
  - *Raw:* all licences.
  - *CC BY/SA/0:* CC BY, CC BY-SA or CC0 only.
  - *+ subtype label:* also matches the `image_subtype` label (ct / mri / x_ray / ultrasound).
- **ROCOv2:** train split only, about 60k of 80k images.

| Diagnosis + modality | MultiCaRe raw | MultiCaRe CC BY/SA/0 | + subtype label | ROCOv2 train raw | ROCOv2 train CC BY |
|---|---|---|---|---|---|
| SAH + CT | 183 | 51 | 48 | 55 | 35 |
| Stroke/infarct + DWI | 251 | 96 | 92 | 47 | 37 |
| Abscess + MRI (broad regex) | 209 | 67 | 60 | 158 | 112 |
| Pneumothorax + radiograph | 98 | 61 | 60 | 265 | 211 |
| Appendicitis/appendix + CT | 60 | 38 | 38 | 109 | 80 |
| DVT + US/Doppler | 7 | 4 | 4 | 7 | 5 |
| Aortic dissection + CT/angio | 35 | 23 | 19 | 36 | 30 |
| "Normal/unremarkable" captions | 257 | 148 | n/a | 155 | 124 |

Source: local analysis of [MultiCaRe v3.0.1](https://zenodo.org/records/20416562) and [ROCOv2](https://zenodo.org/records/10821435) captions.

- **Arrow mentions are frequent.** Among the MultiCaRe CC BY matches, the captions explicitly mention arrows, arrowheads or asterisks in 14/51 (SAH), 36/96 (stroke), 27/67 (abscess), 20/61 (pneumothorax), 21/38 (appendicitis) and 13/23 (dissection). Example: "Brain computed tomography revealed subarachnoid hemorrhage (the red arrow) and irregular hypointensity shadows… (the white arr…)" — local analysis of [MultiCaRe](https://zenodo.org/records/20416562); the paper confirms burned-in "arrows, circles or asterisks" ([PMC10792687](https://pmc.ncbi.nlm.nih.gov/articles/PMC10792687)).
- **Captions are informative enough for automatic matching.** Example: "Non-contrast head CT scan showing hyper-densities along basal cisterns with a perimesencephalic hemorrhage pattern (white arrows)" names the modality, contrast, finding and marker. ROCOv2 captions are terse but explicit, for example "Head CT demonstrating left parotiditis." — [Europe PMC fullTextXML PMC13476372](https://www.ebi.ac.uk/europepmc/webservices/rest/PMC13476372/fullTextXML); [ROCOv2 train_captions.csv](https://zenodo.org/records/10821435).

### Inferences
- **Caption matching quality:**
  - Case-report captions usually name the modality, and often the sequence (DWI, T1 post-gadolinium) and the plane. Regex on dx + modality gives good recall.
  - Precision suffers from three things: differential or excluded findings ("no evidence of SAH"), multi-panel captions, and follow-up or post-treatment images. Add negation filtering ("no", "without", "resolved") and prefer figure 1 or the "on admission" figures.
- **Teaching suitability:**
  - Case reports often show **one dominant lesion**, which is good, but frequently a **rare or atypical** presentation, which is bad for exam basics. Prefer captions with classic wording.
  - **Pre-existing arrows conflict with our numbered markers.** Options:
    - (a) Keep the image and number the author's arrows in our legend.
    - (b) Choose arrow-free images: about 60–75% of matches by the caption-mention count. Captions do not always mention the arrows, so check visually.
    - (c) Avoid digital removal of arrows: it is an adaptation allowed under CC BY when declared, but it is medically risky and conflicts with the source.
- **Normal comparison images are scarce and biased:**
  - Literature captions rarely show normals. When they do, the normal is usually a follow-up ("unremarkable after treatment") or a contralateral side.
  - About 120–150 CC BY "normal/unremarkable" captions exist in each dataset, but many are partial statements.
  - Better strategy: use Europe PMC `FIG:"normal chest radiograph"` (43 CC BY articles, 26 case reports), resolved follow-up images, and anatomy or normal-variant papers, or complement with other sources (Wikimedia Commons, Radiopaedia-free sets, open datasets). Those are covered by other researchers.
- **DVT Doppler is the weakest category in the curated sets** (4–5 CC BY images). Use Europe PMC `FIG:` (86 CC BY case reports) and manual selection.

### Gaps
- The figure-level usable rate was **not measured** by visual review. Spot-check about 20 per diagnosis before relying on the counts.
- The ROCOv2 valid and test splits were not counted; they would add about 25%.
- The ischaemic-stroke regex in MultiCaRe and ROCOv2 also catches non-stroke infarcts (for example, myocardial infarction on DWI is unlikely, but "infarct" in other organs is possible). These counts are upper bounds.
