# -*- coding: utf-8 -*-
"""Table de traduction radiologique FR -> EN/DE pour la recherche d'images.

DIAG : une ligne par id : num | synonymes anglais (;) | terme allemand (Commons) | région EN | région DE
Le premier synonyme anglais est le plus fréquent dans les légendes de figures.
"""
import re

DIAG_TXT = r"""
042|pituitary macroadenoma;pituitary adenoma;pituitary microadenoma|Hypophysenadenom|pituitary|Hypophyse
043|craniopharyngioma|Kraniopharyngeom|sella|Sella
044|pituitary apoplexy|Hypophysenapoplexie|pituitary|Hypophyse
045|hypophysitis;pituitary stalk thickening|Hypophysitis|pituitary|Hypophyse
046|orbital cellulitis;preseptal cellulitis|Orbitaphlegmone|orbit|Orbita
047|orbital floor fracture;blowout fracture|Orbitabodenfraktur|orbit|Orbita
048|intraorbital foreign body;orbital foreign body|Fremdkörper Orbita|orbit|Orbita
049|thyroid eye disease;Graves ophthalmopathy;thyroid orbitopathy|endokrine Orbitopathie|orbit|Orbita
050|optic neuritis|Optikusneuritis|orbit|Orbita
051|retinoblastoma;choroidal melanoma;uveal melanoma|Aderhautmelanom|eye|Auge
052|retinal detachment|Netzhautablösung|eye|Auge
053|orbital abscess sinusitis;complicated sinusitis;subperiosteal abscess|Sinusitis|paranasal sinuses|Nasennebenhöhlen
054|chronic rhinosinusitis;nasal polyposis;fungal sinusitis;aspergilloma sinus|chronische Sinusitis|paranasal sinuses|Nasennebenhöhlen
055|mastoiditis|Mastoiditis|temporal bone|Felsenbein
056|cholesteatoma|Cholesteatom|temporal bone|Felsenbein
057|otosclerosis;otospongiosis|Otosklerose|temporal bone|Felsenbein
058|Le Fort fracture;zygomaticomaxillary complex fracture;zygomatic fracture|Mittelgesichtsfraktur|face|Gesichtsschädel
059|temporal bone fracture|Felsenbeinfraktur|temporal bone|Felsenbein
060|sinonasal carcinoma;sinonasal tumor;maxillary sinus carcinoma|Nasennebenhöhlenkarzinom|paranasal sinuses|Nasennebenhöhlen
061|osteonecrosis of the jaw;odontogenic cyst;radicular cyst;dentigerous cyst|Kieferzyste|mandible|Unterkiefer
062|head and neck squamous cell carcinoma;oropharyngeal carcinoma;laryngeal carcinoma|Larynxkarzinom|neck|Hals
063|retropharyngeal abscess;parapharyngeal abscess|Retropharyngealabszess|neck|Hals
064|epiglottitis;thumb sign|Epiglottitis|neck|Hals
065|Ludwig angina;Ludwig's angina|Mundbodenphlegmone|neck|Hals
066|esophageal foreign body;pharyngeal foreign body;fish bone|Fremdkörper Ösophagus|neck|Hals
067|thyroid nodule|Schilddrüsenknoten|thyroid|Schilddrüse
068|Graves disease;toxic nodule;thyroid scintigraphy hyperthyroidism|Morbus Basedow|thyroid|Schilddrüse
069|Hashimoto thyroiditis;subacute thyroiditis;de Quervain thyroiditis|Hashimoto-Thyreoiditis|thyroid|Schilddrüse
070|parathyroid adenoma|Nebenschilddrüsenadenom|neck|Hals
071|cervical lymphadenopathy;metastatic lymph node;cervical lymph node|Lymphknoten Hals|neck|Hals
072|pleomorphic adenoma;Warthin tumor;parotid tumor|Parotistumor|parotid|Parotis
073|sialolithiasis;submandibular stone;sialadenitis|Sialolithiasis|salivary gland|Speicheldrüse
074|thyroglossal duct cyst;branchial cleft cyst|Ductus-thyreoglossus-Zyste|neck|Hals
075|ectopic thyroid;lingual thyroid;thyroid agenesis|Zungengrundstruma|thyroid|Schilddrüse
076|carotid stenosis;internal carotid artery stenosis|Karotisstenose|carotid|Karotis
077|carotid dissection;vertebral artery dissection;cervical artery dissection|Karotisdissektion|carotid|Karotis
078|intracranial aneurysm;unruptured aneurysm;cerebral aneurysm|intrakranielles Aneurysma|brain|Gehirn
079|large vessel occlusion;middle cerebral artery occlusion;mechanical thrombectomy|Mediaverschluss|brain|Gehirn
080|giant cell arteritis;halo sign temporal artery|Riesenzellarteriitis|temporal artery|Arteria temporalis
081|subclavian steal|Subclavian-Steal|vertebral artery|Arteria vertebralis
082|lumbar disc herniation;disc herniation;herniated disc|Bandscheibenvorfall|lumbar spine|LWS
083|lumbar spinal stenosis;spinal canal stenosis|Spinalkanalstenose|lumbar spine|LWS
084|cervical spondylotic myelopathy;cervical myelopathy|zervikale Myelopathie|cervical spine|HWS
085|Modic changes;degenerative disc disease|Osteochondrose|lumbar spine|LWS
086|spondylolisthesis;spondylolysis;pars defect|Spondylolisthesis|lumbar spine|LWS
087|osteoporotic vertebral fracture;vertebral compression fracture|Wirbelkörperfraktur osteoporotisch|spine|Wirbelsäule
088|spinal metastasis;metastatic spinal cord compression;vertebral metastasis|Wirbelsäulenmetastase|spine|Wirbelsäule
089|multiple myeloma;myeloma lytic lesions|Multiples Myelom|spine|Wirbelsäule
090|spondylodiscitis;vertebral osteomyelitis|Spondylodiszitis|spine|Wirbelsäule
091|spinal epidural abscess;epidural abscess|epiduraler Abszess|spine|Wirbelsäule
092|sacroiliitis;axial spondyloarthritis|Sakroiliitis|sacroiliac joint|Iliosakralgelenk
093|cervical spine fracture;odontoid fracture;cervical spine injury|HWS-Fraktur|cervical spine|HWS
094|thoracolumbar fracture;burst fracture;Chance fracture|Berstungsfraktur|thoracolumbar spine|Wirbelsäule
095|scoliosis;adolescent idiopathic scoliosis|Skoliose|spine|Wirbelsäule
096|tethered cord;spinal dysraphism;myelomeningocele|Tethered cord|spine|Wirbelsäule
097|epidural fibrosis;recurrent disc herniation|Narbe Bandscheibe|lumbar spine|LWS
098|spinal cord infarction|Rückenmarksinfarkt|spinal cord|Rückenmark
099|spinal dural arteriovenous fistula|spinale durale AV-Fistel|spinal cord|Rückenmark
100|transverse myelitis;neuromyelitis optica;spinal cord multiple sclerosis|Myelitis|spinal cord|Rückenmark
101|subacute combined degeneration|funikuläre Myelose|spinal cord|Rückenmark
102|intramedullary tumor;spinal ependymoma;spinal meningioma;schwannoma spine|Ependymom spinal|spinal cord|Rückenmark
103|syringomyelia;syrinx|Syringomyelie|spinal cord|Rückenmark
104|cauda equina syndrome|Cauda-equina-Syndrom|lumbar spine|LWS
105|community-acquired pneumonia;lobar pneumonia;consolidation|Pneumonie|chest|Thorax
106|pulmonary tuberculosis;cavitary tuberculosis|Lungentuberkulose|chest|Thorax
107|Pneumocystis pneumonia;invasive aspergillosis;halo sign|Pneumocystis-Pneumonie|chest|Thorax
108|lung abscess|Lungenabszess|chest|Thorax
109|COVID-19 pneumonia;viral pneumonia;ground-glass opacities|COVID-19 Pneumonie|chest|Thorax
110|solitary pulmonary nodule;pulmonary nodule|Lungenrundherd|chest|Thorax
111|lung cancer;bronchogenic carcinoma;lung adenocarcinoma|Bronchialkarzinom|chest|Thorax
112|low-dose CT lung cancer screening;lung cancer screening|Lungenkrebs-Screening|chest|Thorax
113|lymphangitic carcinomatosis;pulmonary metastases|Lungenmetastasen|chest|Thorax
114|emphysema;COPD|Lungenemphysem|chest|Thorax
115|idiopathic pulmonary fibrosis;usual interstitial pneumonia;honeycombing|idiopathische Lungenfibrose|chest|Thorax
116|silicosis;asbestosis;pneumoconiosis|Silikose|chest|Thorax
117|bronchiectasis;cystic fibrosis|Bronchiektasen|chest|Thorax
118|sarcoidosis;hilar lymphadenopathy sarcoidosis|Sarkoidose|chest|Thorax
119|nonspecific interstitial pneumonia;NSIP|NSIP|chest|Thorax
120|hypersensitivity pneumonitis|exogen-allergische Alveolitis|chest|Thorax
121|granulomatosis with polyangiitis;Wegener granulomatosis|Granulomatose mit Polyangiitis|chest|Thorax
122|pulmonary edema;cardiogenic pulmonary edema;Kerley B lines|Lungenödem|chest|Thorax
123|acute respiratory distress syndrome;ARDS|ARDS|chest|Thorax
124|atelectasis;lobar collapse|Atelektase|chest|Thorax
125|pulmonary embolism|Lungenembolie|chest|Thorax
126|chronic thromboembolic pulmonary hypertension;CTEPH|CTEPH|chest|Thorax
127|drug-induced pneumonitis;radiation pneumonitis;radiation fibrosis|Strahlenpneumonitis|chest|Thorax
128|congenital pulmonary airway malformation;pulmonary sequestration;CPAM|Lungensequester|chest|Thorax
129|pulmonary contusion|Lungenkontusion|chest|Thorax
130|respiratory distress syndrome newborn;hyaline membrane disease;transient tachypnea of the newborn|Atemnotsyndrom Neugeborenes|chest|Thorax
131|bronchial foreign body;aspirated foreign body|Fremdkörperaspiration|chest|Thorax
132|pleural effusion|Pleuraerguss|chest|Thorax
133|empyema;pleural empyema;split pleura sign|Pleuraempyem|chest|Thorax
134|tension pneumothorax;pneumothorax|Pneumothorax|chest|Thorax
135|hemothorax|Hämatothorax|chest|Thorax
136|malignant pleural mesothelioma;mesothelioma;pleural metastases|Pleuramesotheliom|chest|Thorax
137|pleural plaques;calcified pleural plaques|Pleuraplaques|chest|Thorax
138|thymoma;anterior mediastinal mass;mediastinal teratoma;retrosternal goiter|Thymom|mediastinum|Mediastinum
139|mediastinitis|Mediastinitis|mediastinum|Mediastinum
140|Boerhaave syndrome;esophageal rupture;esophageal perforation|Boerhaave-Syndrom|mediastinum|Mediastinum
141|congenital diaphragmatic hernia|Zwerchfellhernie kongenital|chest|Thorax
142|coronary artery disease;coronary CT angiography stenosis;coronary stenosis|Koronarstenose|heart|Herz
143|myocardial infarction late gadolinium enhancement;myocardial infarction;myocardial viability|Myokardinfarkt|heart|Herz
144|coronary angiography;coronary angioplasty;percutaneous coronary intervention|Koronarangiographie|heart|Herz
145|infective endocarditis;valvular vegetation|Endokarditis|heart|Herz
146|pericardial effusion;cardiac tamponade;pericarditis|Perikarderguss|heart|Herz
147|myocarditis|Myokarditis|heart|Herz
148|aortic stenosis;mitral regurgitation|Aortenklappenstenose|heart|Herz
149|dilated cardiomyopathy;hypertrophic cardiomyopathy;heart failure cardiomegaly|dilatative Kardiomyopathie|heart|Herz
150|cardiac amyloidosis|kardiale Amyloidose|heart|Herz
151|atrial septal defect;ventricular septal defect;coarctation of the aorta|Vorhofseptumdefekt|heart|Herz
152|cardiac myxoma;left atrial myxoma;left ventricular thrombus|Vorhofmyxom|heart|Herz
153|central venous catheter malposition;nasogastric tube malposition;endotracheal tube position|Katheterfehllage|chest|Thorax
154|aortic dissection|Aortendissektion|aorta|Aorta
155|thoracic aortic aneurysm|thorakales Aortenaneurysma|aorta|Aorta
156|traumatic aortic injury;aortic transection|traumatische Aortenruptur|aorta|Aorta
157|intramural hematoma;penetrating atherosclerotic ulcer|intramurales Hämatom Aorta|aorta|Aorta
158|Takayasu arteritis;large vessel vasculitis;aortitis|Takayasu-Arteriitis|aorta|Aorta
159|superior vena cava syndrome;superior vena cava obstruction|Vena-cava-superior-Syndrom|mediastinum|Mediastinum
160|breast cancer;invasive ductal carcinoma;spiculated mass|Mammakarzinom|breast|Brust
161|screening mammography;mammography|Mammographie|breast|Brust
162|fibroadenoma;breast cyst|Fibroadenom|breast|Brust
163|breast abscess;mastitis|Mastitis|breast|Brust
164|rib fracture;flail chest|Rippenfraktur|chest|Thorax
165|breast implant rupture;intracapsular rupture;linguine sign|Implantatruptur|breast|Brust
166|hepatic hemangioma;focal nodular hyperplasia;hepatic adenoma|Leberhämangiom|liver|Leber
167|hepatocellular carcinoma|hepatozelluläres Karzinom|liver|Leber
168|liver metastases;hepatic metastases|Lebermetastasen|liver|Leber
169|liver abscess;hydatid cyst;echinococcosis liver|Leberabszess|liver|Leber
170|liver cirrhosis;cirrhosis portal hypertension|Leberzirrhose|liver|Leber
171|hepatic steatosis;fatty liver|Fettleber|liver|Leber
172|portal vein thrombosis;Budd-Chiari syndrome|Pfortaderthrombose|liver|Leber
173|liver laceration;hepatic injury|Leberruptur|liver|Leber
174|hepatic iron overload;hemochromatosis|Hämochromatose|liver|Leber
175|liver transplant hepatic artery thrombosis;TIPS stenosis;transjugular intrahepatic portosystemic shunt|TIPS|liver|Leber
176|acute cholecystitis|akute Cholezystitis|gallbladder|Gallenblase
177|cholelithiasis;gallstones|Cholezystolithiasis|gallbladder|Gallenblase
178|choledocholithiasis;common bile duct stone;cholangitis|Choledocholithiasis|bile duct|Gallengang
179|cholangiocarcinoma;Klatskin tumor;ampullary carcinoma|Klatskin-Tumor|bile duct|Gallengang
180|primary sclerosing cholangitis|primär sklerosierende Cholangitis|bile duct|Gallengang
181|gallbladder carcinoma;gallbladder polyp|Gallenblasenkarzinom|gallbladder|Gallenblase
182|choledochal cyst;biliary atresia|Choledochuszyste|bile duct|Gallengang
183|bile leak;biloma|Galleleck|liver|Leber
184|acute pancreatitis;necrotizing pancreatitis;walled-off necrosis;pancreatic pseudocyst|akute Pankreatitis|pancreas|Pankreas
185|chronic pancreatitis;pancreatic calcifications|chronische Pankreatitis|pancreas|Pankreas
186|pancreatic adenocarcinoma;pancreatic ductal adenocarcinoma;pancreatic cancer|Pankreaskarzinom|pancreas|Pankreas
187|intraductal papillary mucinous neoplasm;IPMN;pancreatic cystic neoplasm|IPMN|pancreas|Pankreas
188|pancreatic neuroendocrine tumor;neuroendocrine tumor;carcinoid|neuroendokriner Tumor|pancreas|Pankreas
189|autoimmune pancreatitis|Autoimmunpankreatitis|pancreas|Pankreas
190|splenic rupture;splenic laceration|Milzruptur|spleen|Milz
191|splenic infarction|Milzinfarkt|spleen|Milz
192|splenomegaly|Splenomegalie|spleen|Milz
193|acute mesenteric ischemia;superior mesenteric artery occlusion;pneumatosis intestinalis|Mesenterialischämie|abdomen|Abdomen
194|acute appendicitis;appendicitis|Appendizitis|appendix|Appendix
195|sigmoid diverticulitis;diverticulitis|Divertikulitis|colon|Kolon
196|pseudomembranous colitis;Clostridium difficile colitis;infectious colitis|pseudomembranöse Kolitis|colon|Kolon
197|colorectal cancer;rectal cancer;colon cancer|Kolonkarzinom|colon|Kolon
198|esophageal cancer;gastric cancer;gastric adenocarcinoma|Ösophaguskarzinom|stomach|Magen
199|gastrointestinal stromal tumor;GIST|GIST|stomach|Magen
200|small bowel obstruction;sigmoid volvulus;bowel obstruction|Dünndarmileus|abdomen|Abdomen
201|pneumoperitoneum;free air;perforated ulcer|Pneumoperitoneum|abdomen|Abdomen
202|Crohn disease;Crohn's disease|Morbus Crohn|small bowel|Dünndarm
203|toxic megacolon;ulcerative colitis|toxisches Megakolon|colon|Kolon
204|hypertrophic pyloric stenosis;pyloric stenosis|Pylorusstenose|pylorus|Pylorus
205|intussusception;ileocolic intussusception;target sign|Invagination|abdomen|Abdomen
206|midgut volvulus;intestinal malrotation;whirlpool sign|Volvulus Malrotation|abdomen|Abdomen
207|necrotizing enterocolitis;pneumatosis intestinalis|nekrotisierende Enterokolitis|abdomen|Abdomen
208|button battery ingestion;ingested foreign body;magnet ingestion|Knopfbatterie|abdomen|Abdomen
209|gastrointestinal bleeding;active extravasation;contrast extravasation|gastrointestinale Blutung|abdomen|Abdomen
210|hiatal hernia;achalasia;bird beak|Achalasie|esophagus|Ösophagus
211|ascites|Aszites|abdomen|Abdomen
212|peritoneal carcinomatosis;omental cake|Peritonealkarzinose|abdomen|Abdomen
213|incarcerated hernia;inguinal hernia;strangulated hernia|Leistenhernie|abdominal wall|Bauchwand
214|psoas hematoma;rectus sheath hematoma|Rektusscheidenhämatom|abdominal wall|Bauchwand
215|retroperitoneal fibrosis|retroperitoneale Fibrose|retroperitoneum|Retroperitoneum
216|postoperative abscess;intra-abdominal abscess|Abszess abdominal|abdomen|Abdomen
217|ureteral stone;urolithiasis;nephrolithiasis|Urolithiasis|kidney|Niere
218|acute pyelonephritis;renal abscess|akute Pyelonephritis|kidney|Niere
219|emphysematous pyelonephritis|emphysematöse Pyelonephritis|kidney|Niere
220|clear cell renal cell carcinoma;renal cell carcinoma|Nierenzellkarzinom|kidney|Niere
221|Bosniak cyst;complex renal cyst;renal cyst|Nierenzyste|kidney|Niere
222|angiomyolipoma;renal angiomyolipoma|Angiomyolipom|kidney|Niere
223|urothelial carcinoma upper tract;upper tract urothelial carcinoma;renal pelvis carcinoma|Urothelkarzinom Nierenbecken|kidney|Niere
224|adrenal adenoma;adrenal incidentaloma|Nebennierenadenom|adrenal|Nebenniere
225|pheochromocytoma|Phäochromozytom|adrenal|Nebenniere
226|renal artery stenosis;fibromuscular dysplasia|Nierenarterienstenose|kidney|Niere
227|renal infarction;renal vein thrombosis|Niereninfarkt|kidney|Niere
228|hydronephrosis;chronic kidney disease ultrasound|Hydronephrose|kidney|Niere
229|vesicoureteral reflux;voiding cystourethrogram;pelviureteric junction obstruction|vesikoureteraler Reflux|kidney|Niere
230|autosomal dominant polycystic kidney disease;polycystic kidney|Zystennieren|kidney|Niere
231|horseshoe kidney;ectopic kidney;pelvic kidney|Hufeisenniere|kidney|Niere
232|renal laceration;renal trauma|Nierenruptur|kidney|Niere
233|renal transplant;transplant renal artery stenosis;perinephric collection transplant|Nierentransplantat|kidney|Niere
234|Wilms tumor;nephroblastoma;neuroblastoma|Nephroblastom|kidney|Niere
235|abdominal aortic aneurysm;ruptured abdominal aortic aneurysm|Bauchaortenaneurysma|aorta|Aorta
236|endoleak;endovascular aneurysm repair|Endoleak|aorta|Aorta
237|chronic mesenteric ischemia;celiac artery stenosis;superior mesenteric artery stenosis|Truncus-coeliacus-Stenose|abdomen|Abdomen
238|bladder cancer;bladder tumor;urothelial carcinoma bladder|Harnblasenkarzinom|bladder|Harnblase
239|urinary retention;post-void residual;distended bladder|Harnverhalt|bladder|Harnblase
240|bladder rupture;urethral injury;retrograde urethrogram|Blasenruptur|bladder|Harnblase
241|prostate cancer;PI-RADS|Prostatakarzinom|prostate|Prostata
242|benign prostatic hyperplasia|benigne Prostatahyperplasie|prostate|Prostata
243|testicular torsion|Hodentorsion|testis|Hoden
244|epididymitis;orchitis;epididymo-orchitis|Epididymitis|testis|Hoden
245|testicular tumor;seminoma;testicular cancer|Seminom|testis|Hoden
246|varicocele|Varikozele|testis|Hoden
247|undescended testis;cryptorchidism|Maldescensus testis|inguinal|Leiste
248|prostatic abscess;prostatitis|Prostataabszess|prostate|Prostata
249|ovarian cyst;adnexal mass;dermoid cyst;ovarian tumor|Ovarialzyste|ovary|Ovar
250|uterine fibroid;leiomyoma uterus;uterine leiomyoma|Uterus myomatosus|uterus|Uterus
251|endometrial carcinoma;cervical cancer|Endometriumkarzinom|uterus|Uterus
252|ovarian torsion;adnexal torsion|Ovarialtorsion|ovary|Ovar
253|tubo-ovarian abscess;pyosalpinx;pelvic inflammatory disease|Tuboovarialabszess|ovary|Ovar
254|endometrioma;endometriosis;adenomyosis|Endometriose|uterus|Uterus
255|polycystic ovary;polycystic ovarian syndrome|polyzystisches Ovar|ovary|Ovar
256|bicornuate uterus;septate uterus;uterine anomaly|Uterus bicornis|uterus|Uterus
257|intrauterine device malposition;IUD|Intrauterinpessar|uterus|Uterus
258|ectopic pregnancy;tubal ectopic pregnancy|Extrauteringravidität|uterus|Uterus
259|early pregnancy ultrasound;gestational sac;yolk sac;crown-rump length|Fruchthöhle|uterus|Uterus
260|fetal anomaly;prenatal ultrasound;fetal malformation|Fehlbildung fetal Ultraschall|fetus|Fetus
261|placenta previa;placental abruption|Placenta praevia|placenta|Plazenta
262|fetal growth restriction;umbilical artery Doppler;intrauterine growth restriction|Wachstumsretardierung fetal|fetus|Fetus
263|appendicitis in pregnancy;MRI in pregnancy|Schwangerschaft MRT|pregnancy|Schwangerschaft
264|retained products of conception;postpartum hemorrhage|Plazentarest|uterus|Uterus
265|perianal fistula;anal fistula;perianal abscess|Analfistel|anal canal|Analkanal
266|pelvic organ prolapse;dynamic pelvic floor MRI;defecography|Beckenbodensenkung|pelvic floor|Beckenboden
267|anterior shoulder dislocation;Hill-Sachs lesion;Bankart lesion|Schulterluxation|shoulder|Schulter
268|clavicle fracture;proximal humerus fracture|Klavikulafraktur|shoulder|Schulter
269|rotator cuff tear;supraspinatus tear|Rotatorenmanschettenruptur|shoulder|Schulter
270|calcific tendinitis;adhesive capsulitis;calcific tendinopathy|Tendinosis calcarea|shoulder|Schulter
271|acromioclavicular joint dislocation;acromioclavicular separation|Schultereckgelenksprengung|shoulder|Schulter
272|supracondylar humerus fracture;supracondylar fracture;posterior fat pad sign|suprakondyläre Humerusfraktur|elbow|Ellenbogen
273|radial head fracture;fat pad sign|Radiusköpfchenfraktur|elbow|Ellenbogen
274|Monteggia fracture;Galeazzi fracture|Monteggia-Fraktur|forearm|Unterarm
275|lateral epicondylitis;common extensor tendinopathy|Epicondylitis humeri radialis|elbow|Ellenbogen
276|olecranon bursitis;septic bursitis|Bursitis olecrani|elbow|Ellenbogen
277|distal radius fracture;Colles fracture|distale Radiusfraktur|wrist|Handgelenk
278|scaphoid fracture|Skaphoidfraktur|wrist|Handgelenk
279|scapholunate dissociation;perilunate dislocation;lunate dislocation|skapholunäre Dissoziation|wrist|Handgelenk
280|rheumatoid arthritis;erosions rheumatoid hand|rheumatoide Arthritis|hand|Hand
281|hand osteoarthritis;erosive osteoarthritis;thumb base osteoarthritis|Rhizarthrose|hand|Hand
282|gout;chondrocalcinosis;double contour sign|Gicht|hand|Hand
283|carpal tunnel syndrome;median nerve|Karpaltunnelsyndrom|wrist|Handgelenk
284|flexor tenosynovitis;osteomyelitis finger|Beugesehnenscheidenphlegmone|hand|Hand
285|bone age;Greulich and Pyle|Knochenalter|hand|Hand
286|upper extremity deep vein thrombosis;subclavian vein thrombosis|Armvenenthrombose|arm|Arm
287|arteriovenous fistula stenosis;hemodialysis fistula;dialysis access|Dialyseshunt|arm|Arm
288|thoracic outlet syndrome;cervical rib|Halsrippe|shoulder|Schulter
289|femoral neck fracture;hip fracture|Schenkelhalsfraktur|hip|Hüfte
290|pelvic ring fracture;pelvic fracture;acetabular fracture|Beckenfraktur|pelvis|Becken
291|hip osteoarthritis|Coxarthrose|hip|Hüfte
292|avascular necrosis of the femoral head;osteonecrosis femoral head|Hüftkopfnekrose|hip|Hüfte
293|developmental dysplasia of the hip;hip dysplasia|Hüftdysplasie|hip|Hüfte
294|slipped capital femoral epiphysis|Epiphyseolysis capitis femoris|hip|Hüfte
295|Legg-Calve-Perthes disease;Perthes disease|Morbus Perthes|hip|Hüfte
296|septic arthritis hip;hip joint effusion;transient synovitis|Coxitis fugax|hip|Hüfte
297|femoroacetabular impingement;cam deformity|femoroazetabuläres Impingement|hip|Hüfte
298|anterior cruciate ligament tear;meniscal tear;bucket handle tear|vordere Kreuzbandruptur|knee|Knie
299|tibial plateau fracture|Tibiakopffraktur|knee|Knie
300|knee osteoarthritis|Gonarthrose|knee|Knie
301|ruptured Baker cyst;Baker cyst;popliteal cyst|Baker-Zyste|knee|Knie
302|osteochondritis dissecans|Osteochondrosis dissecans|knee|Knie
303|patellar dislocation;transient lateral patellar dislocation|Patellaluxation|knee|Knie
304|ankle fracture;bimalleolar fracture;Weber fracture|Sprunggelenksfraktur|ankle|Sprunggelenk
305|Achilles tendon rupture|Achillessehnenruptur|ankle|Sprunggelenk
306|stress fracture;metatarsal stress fracture|Ermüdungsfraktur|foot|Fuß
307|Charcot neuroarthropathy;diabetic foot osteomyelitis|Charcot-Fuß|foot|Fuß
308|gout foot;podagra;tophaceous gout|Gicht Fuß|foot|Fuß
309|clubfoot;congenital talipes equinovarus|Klumpfuß|foot|Fuß
310|deep vein thrombosis;femoral vein thrombosis|tiefe Venenthrombose|leg|Bein
311|peripheral arterial disease;acute limb ischemia;femoral artery occlusion|periphere arterielle Verschlusskrankheit|leg|Bein
312|great saphenous vein reflux;venous insufficiency;varicose veins|Varikose|leg|Bein
313|femoral pseudoaneurysm;pseudoaneurysm|Pseudoaneurysma femoral|groin|Leiste
314|popliteal artery aneurysm|Poplitealaneurysma|knee|Knie
315|acute osteomyelitis;pediatric osteomyelitis|akute Osteomyelitis|bone|Knochen
316|necrotizing fasciitis;cellulitis ultrasound|nekrotisierende Fasziitis|soft tissue|Weichteile
317|aggressive bone lesion;periosteal reaction;Codman triangle;moth-eaten|aggressive Knochenläsion|bone|Knochen
318|osteosarcoma;Ewing sarcoma|Osteosarkom|bone|Knochen
319|non-ossifying fibroma;enchondroma;bone island;fibrous dysplasia|nicht-ossifizierendes Fibrom|bone|Knochen
320|soft tissue sarcoma;liposarcoma;undifferentiated pleomorphic sarcoma|Weichteilsarkom|soft tissue|Weichteile
321|Salter-Harris fracture;physeal fracture|Salter-Harris-Fraktur|bone|Knochen
322|compartment syndrome;rhabdomyolysis;myonecrosis|Kompartmentsyndrom|muscle|Muskel
323|muscle strain;muscle tear;hamstring injury|Muskelfaserriss|muscle|Muskel
324|lymphoma PET/CT;Hodgkin lymphoma;Deauville|Hodgkin-Lymphom|whole body|Ganzkörper
325|FDG PET/CT staging;staging CT metastases|PET/CT Staging|whole body|Ganzkörper
326|RECIST;tumor response;target lesion|RECIST|whole body|Ganzkörper
327|bone metastases;bone scan metastases;skeletal metastases|Knochenmetastasen|whole body|Ganzkörper
328|immune checkpoint inhibitor pneumonitis;immune-related adverse event;hypophysitis ipilimumab|Immuntherapie Pneumonitis|whole body|Ganzkörper
329|metastatic spinal cord compression;spinal cord compression|Rückenmarkskompression|spine|Wirbelsäule
330|cancer of unknown primary;unknown primary PET/CT|CUP-Syndrom|whole body|Ganzkörper
331|dual-energy X-ray absorptiometry;DXA;osteoporosis|Osteoporose|spine|Wirbelsäule
332|Paget disease of bone;Paget's disease|Morbus Paget|bone|Knochen
333|rickets;osteomalacia;Looser zone|Rachitis|bone|Knochen
334|hyperparathyroidism subperiosteal resorption;brown tumor;salt and pepper skull|Hyperparathyreoidismus Knochen|hand|Hand
335|achondroplasia;osteogenesis imperfecta|Achondroplasie|bone|Knochen
336|diffuse idiopathic skeletal hyperostosis;ankylosing spondylitis;bamboo spine|Morbus Forestier|spine|Wirbelsäule
337|FAST ultrasound;Morison pouch free fluid;hemoperitoneum|Hämoperitoneum|abdomen|Abdomen
338|point-of-care ultrasound shock;inferior vena cava ultrasound;POCUS|IVC Sonographie|abdomen|Abdomen
339|pediatric head trauma;skull fracture child;epidural hematoma child|Schädelfraktur Kind|head|Schädel
340|child abuse;classic metaphyseal lesion;posterior rib fractures infant|Kindesmisshandlung|bone|Knochen
341|pediatric CT radiation dose;pediatric imaging|Kinderradiologie|whole body|Ganzkörper
342|fever of unknown origin PET/CT;FDG PET fever of unknown origin|FDG-PET Fieber|whole body|Ganzkörper
343|large vessel vasculitis PET;polymyalgia rheumatica PET;giant cell arteritis PET|Polymyalgia rheumatica|whole body|Ganzkörper
344|IgG4-related disease|IgG4-assoziierte Erkrankung|pancreas|Pankreas
"""


def charger_diag():
    table = {}
    for ligne in DIAG_TXT.strip().splitlines():
        num, en, de, reg, reg_de = [x.strip() for x in ligne.split("|")]
        table["IMG-" + num] = {
            "en": [t.strip() for t in en.split(";") if t.strip()],
            "de": de, "region": reg, "region_de": reg_de}
    return table


# Modalités : regex FR (dans la description a_chercher) -> clé
MODALITES_FR = [
    ("PET", r"\bTEP\b|PET|FDG|PSMA|DOTATATE|Ga-68|18F"),
    ("NM", r"scintigraph|SPECT|TEMP\b|médecine nucléaire|MIBG|sestamibi|technétium|99m"),
    ("MAMMO", r"mammograph|tomosynth"),
    ("ANGIO", r"angiograph|artériograph|coronarograph|phlébograph|DSA\b|soustraction"),
    ("MRI", r"\bIRM\b|IRM|imagerie par résonance|cholangio-IRM|entéro-IRM|arthro-IRM|\bT1\b|\bT2\b|FLAIR|diffusion"),
    ("CT", r"\bTDM\b|scanner|tomodensitom|angio-?TDM|uro-?TDM|cone beam|CBCT|coroscanner|coloscanner"),
    ("US", r"échograph|Doppler|écho\b|ETT\b|ETO\b|eFAST|FAST\b|POCUS|élastograph|échocardio"),
    ("FLUORO", r"transit|opacification|cystograph|urétrograph|hystérograph|TOGD|lavement|déféco|fluoro"),
    ("XR", r"radiograph|cliché|\bRX\b|radio\b|ASP\b|incidence|téléradio|EOS|densitom|DXA|ostéodensit"),
]

# Pour chaque modalité : requête Europe PMC (FIG:...), regex légende EN, mots Commons EN/DE
MODALITE_INFO = {
    "CT":    {"epmc": '(FIG:CT OR FIG:"computed tomography")', "rx": r"\bCT\b|computed tomograph|\bCTA\b|\bMDCT\b|\bHRCT\b|\bCECT\b|\bNCCT\b|tomodensit",
              "en": "CT", "de": "CT", "nom": "TDM"},
    "MRI":   {"epmc": '(FIG:MRI OR FIG:"magnetic resonance")', "rx": r"\bMRI?\b|magnetic resonance|\bMRCP\b|\bMRA\b|T1-?weighted|T2-?weighted|\bT1WI\b|\bT2WI\b|\bFLAIR\b|\bDWI\b|\bSTIR\b",
              "en": "MRI", "de": "MRT", "nom": "IRM"},
    "US":    {"epmc": '(FIG:ultrasound OR FIG:ultrasonography OR FIG:sonography OR FIG:Doppler OR FIG:echocardiography)', "rx": r"ultraso|sonograph|\bUS\b|Doppler|echocardiogra|\bTTE\b|\bTEE\b|\bPOCUS\b|\bFAST\b",
              "en": "ultrasound", "de": "Sonographie", "nom": "Échographie"},
    "XR":    {"epmc": '(FIG:radiograph OR FIG:"x-ray" OR FIG:radiography)', "rx": r"radiograph|x-?ray|\bfilm\b|plain film|\bCXR\b|DXA|DEXA|densitometr",
              "en": "X-ray", "de": "Röntgen", "nom": "Radiographie"},
    "MAMMO": {"epmc": '(FIG:mammogram OR FIG:mammography OR FIG:tomosynthesis)', "rx": r"mammogra|tomosynthes",
              "en": "mammography", "de": "Mammographie", "nom": "Mammographie"},
    "NM":    {"epmc": '(FIG:scintigraphy OR FIG:SPECT OR FIG:"bone scan" OR FIG:scan)', "rx": r"scintigra|\bSPECT\b|bone scan|\bscan\b.*(99m|Tc)|99m|Tc-|sestamibi|MIBG|nuclear",
              "en": "scintigraphy", "de": "Szintigraphie", "nom": "Scintigraphie"},
    "PET":   {"epmc": '(FIG:PET OR FIG:"positron emission")', "rx": r"\bPET\b|positron|FDG|PSMA|DOTATATE",
              "en": "PET", "de": "PET", "nom": "TEP"},
    "ANGIO": {"epmc": '(FIG:angiography OR FIG:angiogram OR FIG:arteriogram OR FIG:DSA)', "rx": r"angiogra|arteriogra|venogra|\bDSA\b|digital subtraction",
              "en": "angiography", "de": "Angiographie", "nom": "Angiographie"},
    "FLUORO": {"epmc": '(FIG:fluoroscopy OR FIG:swallow OR FIG:cystogram OR FIG:urethrogram OR FIG:enema OR FIG:"contrast study")', "rx": r"fluorosc|swallow|esophagogra|cystogra|cystourethrogra|urethrogra|enema|contrast study|defecogra|hysterosalpingogra|upper GI",
              "en": "fluoroscopy", "de": "Röntgen Kontrastmittel", "nom": "Opacification"},
}

# Plan / séquence / incidence : regex FR -> (étiquette EN pour Commons, regex légende EN)
DETAILS_FR = [
    (r"axial", "axial", r"\baxial\b|transverse|transaxial"),
    (r"coronal|frontal", "coronal", r"coronal"),
    (r"sagittal", "sagittal", r"sagittal"),
    (r"\bT1\b", "T1", r"\bT1"),
    (r"\bT2\b", "T2", r"\bT2"),
    (r"FLAIR", "FLAIR", r"FLAIR"),
    (r"diffusion", "diffusion", r"diffusion|\bDWI\b|\bADC\b"),
    (r"gadolinium|après injection|rehauss|contraste|portal|artériel|injecté", "contrast", r"contrast|enhanc|gadolinium|post-?gad|portal venous|arterial phase|\bCECT\b"),
    (r"sans injection|non injecté|spontané", "non-contrast", r"non-?contrast|unenhanced|without contrast|plain CT|\bNCCT\b"),
    (r"STIR|saturation de graisse|suppression de graisse|fat", "fat-saturated", r"\bSTIR\b|fat[- ]?sat|fat[- ]?suppress"),
    (r"face|PA\b|postéro-antérieur|de face", "frontal", r"\bPA\b|posteroanterior|postero-anterior|frontal|\bAP\b|anteroposterior"),
    (r"profil", "lateral", r"lateral"),
    (r"Doppler", "Doppler", r"Doppler"),
    (r"fenêtre osseuse|os\b|osseu", "bone window", r"bone window|bone algorithm"),
    (r"fenêtre pulmonaire|parenchym", "lung window", r"lung window|parenchymal"),
    (r"angio", "angiography", r"angiogra|\bCTA\b|\bMRA\b"),
]


def detecter_modalite(desc):
    tete = desc.split(":")[0]
    for txt in (tete, desc):
        trouves = [(m.start(), k) for k, rx in MODALITES_FR for m in [re.search(rx, txt, re.I)] if m]
        if trouves:
            return sorted(trouves)[0][1]
    return None


def detecter_details(desc):
    tete = desc.split(":")[0]
    res = []
    for rx_fr, etiq, rx_en in DETAILS_FR:
        if re.search(rx_fr, tete, re.I):
            res.append((etiq, rx_en))
    return res
