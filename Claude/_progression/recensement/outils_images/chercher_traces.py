#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Recherche de tracés libres pour les explorations fonctionnelles EXP-001 à EXP-153.

Réutilise chercher.py (cache HTTP disque, Europe PMC, dépôt AWS de PMC, Commons, téléchargement ≤ 900 px).
Description voulue : enrichi/EXP_*.json > traces.a_chercher {normal, patho} ; technologie : recensement.json.
Technologies VENT et DYN exclues (schémas dessinés à part ; ce script n'en dessine aucun).
Sorties : candidats/EXP-xxx/{candidats.json, normal_n.jpg, patho_n.jpg}, planche_traces.html, journal_traces.log.
Le choix final de l'image revient à l'humain.
Usage : python3 chercher_traces.py [--sans-commons] [--complement] [--ids EXP-045 ...] [--force] [--stats] [--planche]
"""
import argparse, csv, glob, json, os, re, sys
from datetime import datetime

ICI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, ICI)
import chercher as C  # noqa: E402

C.JOURNAL = os.path.join(ICI, "journal_traces.log")
log = C.log
EXCLUS = {"VENT", "DYN"}

# ---------------------------------------------------------------- familles de tracés
# rx : la légende doit la contenir ; fig : clause Europe PMC ; com : mot Commons ; mc : sous-types MultiCaRe (bonus)
# nrm : indices supplémentaires de normalité propres au tracé
K = {
    "ECG": dict(rx=r"\bECGs?\b|\bEKGs?\b|electrocardiogra|12-lead|Holter|rhythm strip|telemetry|loop recorder",
                fig='(FIG:ECG OR FIG:electrocardiogram OR FIG:EKG)', com="ECG", mc={"ekg"},
                nrm=r"normal sinus rhythm|normal (12-lead )?(ECG|EKG|electrocardiogra)|sinus rhythm"),
    "HOLTER": dict(rx=r"Holter|loop recorder|\bILR\b|ambulatory (ECG|electrocardiogra)|telemetry|rhythm strip|\bECG\b|\bEKG\b|electrocardiogra",
                   fig='(FIG:Holter OR FIG:"loop recorder" OR FIG:ECG OR FIG:electrocardiogram)', com="ECG", mc={"ekg"},
                   nrm=r"sinus rhythm"),
    "EXER": dict(rx=r"exercise (stress )?(test|ECG|electrocardiogra)|treadmill|stress (ECG|test)|ergometr|Bruce protocol",
                 fig='(FIG:"exercise test" OR FIG:"exercise ECG" OR FIG:treadmill OR FIG:"stress test")', com="exercise ECG", mc={"ekg"},
                 nrm=r"negative (exercise|stress)"),
    "EEG": dict(rx=r"\bEEGs?\b|electroencephalogra", fig='(FIG:EEG OR FIG:electroencephalogram OR FIG:electroencephalography)',
                com="EEG", mc={"eeg"}, nrm=r"posterior dominant rhythm|alpha rhythm|normal background|well-organized background"),
    "TCD": dict(rx=r"transcranial Doppler|\bTCD\b|transcranial color|middle cerebral artery Doppler",
                fig='(FIG:"transcranial Doppler")', com="transcranial Doppler", mc=set(), nrm=r"normal flow"),
    "EP": dict(rx=r"evoked potential|\bVEPs?\b|\bSSEPs?\b|\bSEPs?\b|\bMEPs?\b|\bP100\b|\bN20\b|\bABR\b|\bBAEP|brainstem auditory|auditory brainstem",
               fig='(FIG:"evoked potential" OR FIG:"evoked potentials" OR FIG:VEP OR FIG:SSEP OR FIG:MEP OR FIG:ABR)', com="evoked potential",
               mc={"eeg", "emg"}, nrm=r"normal (latenc|amplitude|P100|N20|wave)"),
    "ERG": dict(rx=r"electroretinogra|\bERGs?\b|ISCEV", fig='(FIG:electroretinogram OR FIG:electroretinography OR FIG:ERG)',
                com="electroretinogram", mc=set(), nrm=r"normal (ERG|response|amplitude)"),
    "NCS": dict(rx=r"nerve conduction|conduction stud|\bNCS\b|\bCMAPs?\b|\bSNAPs?\b|compound (muscle|motor) action|sensory nerve action|"
                   r"repetitive (nerve )?stimulation|\bRNS\b|F[- ]waves?|electroneuro|\bENMG\b|\bEMG\b|electromyogra|distal (motor )?latency",
                fig='(FIG:"nerve conduction" OR FIG:"compound muscle action potential" OR FIG:"repetitive nerve stimulation" OR FIG:electromyography OR FIG:EMG)',
                com="nerve conduction", mc={"emg"}, nrm=r"normal (conduction|CMAP|SNAP|amplitude|latenc)"),
    "EMG": dict(rx=r"\bEMG\b|electromyogra|needle (EMG|electrode|examination)|motor unit|fibrillation potential|positive sharp wave|fasciculation potential",
                fig='(FIG:EMG OR FIG:electromyography OR FIG:electromyogram OR FIG:"motor unit")', com="electromyography", mc={"emg"},
                nrm=r"normal motor unit|electrical silence|full (interference|recruitment)"),
    "VF": dict(rx=r"visual field|perimetr|Humphrey|Goldmann|\b(24|30|10)-2\b|\bSITA\b", fig='(FIG:"visual field" OR FIG:perimetry OR FIG:Humphrey)',
               com="visual field", mc=set(), nrm=r"full (visual )?field|normal (visual )?field"),
    "OCT": dict(rx=r"\bOCT\b|optical coherence tomogra", fig='(FIG:OCT OR FIG:"optical coherence tomography")', com="optical coherence tomography",
                mc={"oct"}, nrm=r"normal (fovea|foveal|macula|retina)|foveal (depression|contour|pit)|healthy (eye|retina)"),
    "ACUITE": dict(rx=r"visual acuity|optotype|Snellen|LEA (symbols|chart)|eye chart|logMAR", fig='(FIG:"visual acuity" OR FIG:optotype OR FIG:Snellen)',
                   com="visual acuity chart", mc=set(), nrm=r"normal (visual )?acuity"),
    "AUDIO": dict(rx=r"audiogra|pure[- ]tone|audiometr|hearing threshold|air[- ]bone gap|air conduction|bone conduction",
                  fig='(FIG:audiogram OR FIG:audiometry OR FIG:"pure-tone" OR FIG:"pure tone")', com="audiogram", mc={"chart"},
                  nrm=r"normal hearing|within normal limits"),
    "TYMPANO": dict(rx=r"tympanogra|tympanometr|acoustic reflex|stapedial reflex", fig='(FIG:tympanogram OR FIG:tympanometry)', com="tympanogram",
                    mc={"chart"}, nrm=r"type A\b"),
    "OEA": dict(rx=r"otoacoustic|\bOAEs?\b|DPOAE|TEOAE|\bABR\b|auditory brainstem|newborn hearing screening",
                fig='(FIG:"otoacoustic emissions" OR FIG:DPOAE OR FIG:TEOAE OR FIG:"auditory brainstem response")', com="otoacoustic emissions",
                mc=set(), nrm=r"\bpass\b|present (emissions|response)"),
    "VNG": dict(rx=r"nystagm|videonystagmo|\bVNG\b|video-?oculogra|Dix-?Hallpike|eye movement record",
                fig='(FIG:nystagmus OR FIG:videonystagmography OR FIG:videooculography)', com="nystagmus", mc=set(), nrm=r"no nystagmus"),
    "VHIT": dict(rx=r"head impulse|\bv?HIT\b|vestibulo-?ocular reflex gain|VOR gain", fig='(FIG:"head impulse" OR FIG:vHIT)', com="video head impulse test",
                 mc=set(), nrm=r"normal (VOR )?gain|gain of 1"),
    "VFSS": dict(rx=r"videofluoroscop|swallow(ing)? study|barium swallow|modified barium|\bVFSS\b|\bVFSE\b|\bFEES\b|fiberoptic endoscopic evaluation of swallowing",
                 fig='(FIG:videofluoroscopy OR FIG:videofluoroscopic OR FIG:"swallow study")', com="videofluoroscopy swallow", mc={"x_ray", "fluoroscopy"},
                 nrm=r"normal swallow|no (penetration|aspiration)|safe swallow"),
    "LARYNGO": dict(rx=r"laryngoscop|vocal (fold|cord)s?|stroboscop|glottis|glottic", fig='(FIG:laryngoscopy OR FIG:"vocal fold" OR FIG:"vocal cord")',
                    com="laryngoscopy vocal folds", mc={"airway_endoscopy"}, nrm=r"normal (vocal|larynx|glottis|laryngeal)"),
    "OLFACT": dict(rx=r"Sniffin|olfactory (test|function)|smell (test|identification)|UPSIT|olfactometr|\bTDI\b",
                   fig='(FIG:"Sniffin" OR FIG:"olfactory test" OR FIG:"olfactory function")', com="Sniffin Sticks", mc=set(), nrm=r"normosmi"),
    "TILT": dict(rx=r"tilt[- ]table|head-?up tilt|tilt test|orthostatic (test|challenge)", fig='(FIG:"tilt table" OR FIG:"tilt test" OR FIG:"head-up tilt")',
                 com="tilt table test", mc={"chart"}, nrm=r"normal (response|tilt)"),
    "ECHO": dict(rx=r"echocardiogra|apical (four|4)|four-chamber|4-chamber|parasternal|\bTTE\b|\bTEE\b|transthoracic|transesophageal|Doppler",
                 fig='(FIG:echocardiography OR FIG:echocardiogram OR FIG:"transthoracic")', com="echocardiography", mc={"ultrasound"},
                 nrm=r"normal (LV|left ventric|systolic|valve|echocardiogra)|preserved ejection fraction"),
    "RHC": dict(rx=r"right heart catheteri|pressure (tracing|waveform|curve)|pulmonary artery pressure|wedge pressure|\bPAWP\b|\bPCWP\b|\bmPAP\b",
                fig='(FIG:"right heart catheterization" OR FIG:"pressure tracing" OR FIG:"pressure waveform")', com="right heart catheterization pressure",
                mc={"chart"}, nrm=r"normal (pressure|pulmonary)"),
    "CPET": dict(rx=r"cardiopulmonary exercise|\bCPET\b|\bCPX\b|\bVO2\b|VE/VCO2|ergospirom|Wasserman|oxygen uptake",
                 fig='(FIG:"cardiopulmonary exercise" OR FIG:CPET OR FIG:"VO2")', com="cardiopulmonary exercise test", mc={"chart"},
                 nrm=r"healthy (subject|control|volunteer)"),
    "MAPA": dict(rx=r"ambulatory blood pressure|\bABPM\b|24[- ]?h(our)? blood pressure|blood pressure profile|dipp",
                 fig='(FIG:"ambulatory blood pressure" OR FIG:ABPM)', com="ambulatory blood pressure monitoring", mc={"chart"}, nrm=r"\bdipper|normal dipping"),
    "MARCHE6": dict(rx=r"six-?minute walk|6-?min(ute)? walk|\b6MWT\b|walk test", fig='(FIG:"six-minute walk" OR FIG:"6-minute walk" OR FIG:6MWT)',
                    com="six minute walk test oximetry", mc={"chart"}, nrm=r"healthy|normal (saturation|SpO2)"),
    "HRM": dict(rx=r"high[- ]resolution (esophageal |oesophageal )?manometr|\bHRM\b|pressure topograph|Clouse|esophageal manometr|oesophageal manometr|\bIRP\b|\bDCI\b",
                fig='(FIG:"high-resolution manometry" OR FIG:"high resolution manometry" OR FIG:"esophageal manometry")', com="high resolution manometry",
                mc={"chart"}, nrm=r"normal (peristalsis|swallow|motility|esophageal)|intact peristalsis"),
    "PH": dict(rx=r"pH[- ]impedance|impedance[- ]pH|pH[- ]?metry|pH monitoring|pH recording|pH tracing|\bMII-pH\b|acid exposure|Bravo",
               fig='(FIG:"pH-impedance" OR FIG:"pH monitoring" OR FIG:"impedance-pH" OR FIG:"pH-metry")', com="esophageal pH monitoring", mc={"chart"},
               nrm=r"normal (acid exposure|pH)"),
    "VIDANGE": dict(rx=r"gastric emptying", fig='(FIG:"gastric emptying")', com="gastric emptying scintigraphy", mc={"scintigraphy", "spect", "chart"},
                    nrm=r"normal (gastric )?emptying"),
    "TRANSIT": dict(rx=r"colonic transit|radio-?opaque markers?|Sitzmarks?|transit (study|time)", fig='(FIG:"colonic transit" OR FIG:"radiopaque markers")',
                    com="colonic transit markers", mc={"x_ray"}, nrm=r"normal (colonic )?transit"),
    "ELASTO": dict(rx=r"transient elastograph|FibroScan|liver stiffness|vibration-controlled", fig='(FIG:"transient elastography" OR FIG:FibroScan OR FIG:"liver stiffness")',
                   com="FibroScan transient elastography", mc={"ultrasound"}, nrm=r"normal (liver )?stiffness"),
    "DEBIT": dict(rx=r"uroflow|urinary flow|flow rate|\bQmax\b|flowmetr", fig='(FIG:uroflowmetry OR FIG:uroflow OR FIG:"urinary flow")', com="uroflowmetry",
                  mc={"chart"}, nrm=r"normal (flow|uroflow)|bell-shaped"),
    "UDS": dict(rx=r"urodynami|cystometr|detrusor pressure|\bPdet\b|pressure[- ]flow|\bPves\b|\bPabd\b|filling phase|voiding phase",
                fig='(FIG:urodynamic OR FIG:urodynamics OR FIG:cystometry OR FIG:cystometrogram)', com="urodynamics", mc={"chart"},
                nrm=r"stable (detrusor|bladder)|normal (cystometr|urodynami|detrusor|bladder)"),
    "ARM": dict(rx=r"anorectal manometr|ano-?rectal manometr|recto-?anal inhibitory|\bRAIR\b|anal (sphincter )?pressure|balloon expulsion|high[- ]resolution anorectal",
                fig='(FIG:"anorectal manometry" OR FIG:"rectoanal inhibitory reflex" OR FIG:"anal manometry")', com="anorectal manometry", mc={"chart"},
                nrm=r"(RAIR|inhibitory reflex) (was )?present|presence of (the )?(RAIR|rectoanal)|normal (anorectal|anal|RAIR)"),
    "CTG": dict(rx=r"cardiotocogra|\bCTG\b|fetal heart rate (tracing|pattern|monitoring)|electronic fetal monitoring|\bFHR\b",
                fig='(FIG:cardiotocography OR FIG:cardiotocogram OR FIG:CTG OR FIG:"fetal heart rate tracing")', com="cardiotocography", mc={"chart"},
                nrm=r"normal (CTG|cardiotocogra|FHR|fetal heart)|reassuring|category I\b"),
    "DOPPLER_OMB": dict(rx=r"umbilical arter|umbilical Doppler|end-diastolic (flow|velocit)|\bUmA\b", fig='(FIG:"umbilical artery Doppler" OR FIG:"umbilical artery")',
                        com="umbilical artery Doppler", mc={"ultrasound"}, nrm=r"positive end-diastolic|forward (diastolic )?flow|normal (umbilical|Doppler|PI)"),
    "COL": dict(rx=r"cervical length|transvaginal (ultraso|sonogra|scan)|cervix|funnel", fig='(FIG:"cervical length" OR FIG:"transvaginal ultrasound")',
                com="cervical length ultrasound", mc={"ultrasound"}, nrm=r"normal (cervical length|cervix)|closed cervix"),
    "DOPPLER_PEN": dict(rx=r"penile (Doppler|duplex|ultraso)|cavernosal arter|cavernous arter|peak systolic velocit",
                        fig='(FIG:"penile Doppler" OR FIG:"penile duplex" OR FIG:"cavernosal artery")', com="penile Doppler", mc={"ultrasound"},
                        nrm=r"normal (arterial|penile|cavernosal|Doppler)"),
    "HYCOSY": dict(rx=r"HyCoSy|HyFoSy|hysterosalpingo-?(contrast-?|foam-?)?sonograph|tubal patency|contrast sonograph",
                   fig='(FIG:HyCoSy OR FIG:HyFoSy OR FIG:hysterosalpingo-contrast OR FIG:hysterosalpingo-foam)', com="hysterosalpingo contrast sonography",
                   mc={"ultrasound"}, nrm=r"patent (tube|fallopian)|bilateral (tubal )?patency|free spill"),
    "CAPILLARO": dict(rx=r"capillaroscop|nailfold", fig='(FIG:capillaroscopy OR FIG:nailfold)', com="nailfold capillaroscopy", mc={"other_medical_photograph"},
                      nrm=r"hairpin|normal (capillaroscop|pattern|capillar)"),
    "ALLEN": dict(rx=r"Allen('s)? test|plethysmogra|palmar arch|pulse oximetr", fig='(FIG:"Allen test" OR FIG:plethysmography OR FIG:"palmar arch")',
                  com="Allen test", mc=set(), nrm=r"normal (Allen|plethysmogra|waveform)|negative Allen"),
    "DYNAMO": dict(rx=r"dynamomet|grip strength|handgrip|hand grip|Jamar", fig='(FIG:dynamometer OR FIG:"grip strength" OR FIG:handgrip)',
                   com="hand dynamometer", mc=set(), nrm=r"normal grip"),
    "IPS": dict(rx=r"ankle[- ]brachial|\bABI\b|Doppler waveform|triphasic|monophasic|biphasic|continuous[- ]wave Doppler|pulse volume record",
                fig='(FIG:"ankle-brachial index" OR FIG:"Doppler waveform" OR FIG:"triphasic")', com="Doppler waveform ankle", mc={"ultrasound", "chart"},
                nrm=r"triphasic|normal (ABI|ankle|waveform)"),
    "TCPO2": dict(rx=r"\bTcPO2\b|\bTcpO2\b|transcutaneous oxygen|toe pressure|toe-brachial", fig='(FIG:TcPO2 OR FIG:"transcutaneous oxygen" OR FIG:"toe pressure")',
                  com="transcutaneous oxygen pressure", mc=set(), nrm=r"normal (TcPO2|toe pressure)"),
    "DOPPLER_VEIN": dict(rx=r"venous reflux|saphen|venous (duplex|Doppler)|duplex (ultraso|scan)|reflux time", fig='(FIG:"venous reflux" OR FIG:"saphenous vein" OR FIG:"venous duplex")',
                         com="venous reflux Doppler saphenous", mc={"ultrasound"}, nrm=r"no reflux|competent|normal (venous|valve)"),
    "MARCHE": dict(rx=r"gait speed|walking speed|Timed Up and Go|\bTUG\b|gait analysis|Tinetti|chair stand", fig='(FIG:"gait speed" OR FIG:"Timed Up and Go" OR FIG:"gait analysis")',
                   com="gait analysis", mc={"chart"}, nrm=r"healthy|normal gait"),
    "DXA": dict(rx=r"\bDXA\b|\bDEXA\b|dual-energy X-ray|body composition|lean (mass|tissue)", fig='(FIG:DXA OR FIG:DEXA OR FIG:"body composition")',
                com="DXA body composition", mc={"x_ray"}, nrm=r"normal (body|lean|muscle)"),
    "POSTURO": dict(rx=r"posturograph|stabilogra|stabilometr|cent(er|re) of pressure|force (platform|plate)|postural sway|statokinesigram",
                    fig='(FIG:posturography OR FIG:stabilogram OR FIG:"center of pressure" OR FIG:stabilometry)', com="stabilogram", mc={"chart"},
                    nrm=r"healthy|normal (sway|balance|posturo)"),
    "PSG": dict(rx=r"polysomnogra|\bPSG\b|hypnogra|polygraph|sleep (study|recording)|respiratory polygraphy|epoch",
                fig='(FIG:polysomnography OR FIG:polysomnogram OR FIG:hypnogram OR FIG:"sleep study")', com="polysomnography", mc={"eeg", "chart"},
                nrm=r"normal (sleep|breathing|polysomnogra|hypnogra)|healthy (sleeper|subject|control)"),
    "MSLT": dict(rx=r"\bMSLT\b|multiple sleep latency|maintenance of wakefulness|\bMWT\b|hypnogra|sleep latency|SOREMP",
                 fig='(FIG:"multiple sleep latency" OR FIG:MSLT OR FIG:hypnogram OR FIG:"maintenance of wakefulness")', com="hypnogram", mc={"eeg", "chart"},
                 nrm=r"normal (sleep|MSLT|latency|hypnogra)|healthy"),
    "ACTI": dict(rx=r"actigra|actogra|actimetr|rest-activity", fig='(FIG:actigraphy OR FIG:actogram OR FIG:"rest-activity")', com="actigraphy",
                 mc={"chart"}, nrm=r"healthy|normal (rest|sleep|actigra|circadian)"),
    "OXY": dict(rx=r"oximetr|\bSpO2\b|oxygen saturation", fig='(FIG:"nocturnal oximetry" OR FIG:"overnight oximetry" OR FIG:"oxygen saturation")',
                com="overnight oximetry", mc={"chart"}, nrm=r"normal (oximetr|saturation|SpO2)"),
    "DERMO": dict(rx=r"dermoscop|dermatoscop|epiluminescen", fig='(FIG:dermoscopy OR FIG:dermatoscopy OR FIG:dermoscopic)', com="dermoscopy",
                  mc={"skin_photograph"}, nrm=r"benign (nevus|naevus)|common (nevus|naevus)|regular (pigment )?network|reticular pattern"),
}
for _k, _v in K.items():
    _v["crx"] = re.compile(_v["rx"], re.I)
    _v["cnrm"] = re.compile(_v["nrm"], re.I)

# ---------------------------------------------------------------- table : familles (normal, patho) + termes anglais du pathologique
T = {
    "EXP-001": ("EEG", "EEG", ["spike-and-wave", "spike and wave", "generalized spike", "epileptiform discharges", "interictal spikes", "sharp waves"]),
    "EXP-002": ("EEG", "EEG", ["nonconvulsive status epilepticus", "non-convulsive status", "NCSE", "status epilepticus", "rhythmic discharges"]),
    "EXP-003": ("EEG", "EEG", ["triphasic waves", "hepatic encephalopathy", "diffuse slowing", "metabolic encephalopathy"]),
    "EXP-004": ("EEG", "EEG", ["periodic lateralized", "lateralized periodic discharges", "PLEDs", "LPDs", "herpes simplex encephalitis"]),
    "EXP-005": ("EEG", "EEG", ["periodic sharp wave complexes", "Creutzfeldt-Jakob", "periodic sharp wave", "PSWC"]),
    "EXP-006": ("EEG", "EEG", ["3 Hz spike", "absence seizure", "childhood absence", "hypsarrhythmia", "infantile spasms", "West syndrome"]),
    "EXP-007": ("EEG", "EEG|TCD", ["electrocerebral silence", "electrocerebral inactivity", "brain death", "reverberating flow", "oscillating flow", "systolic spikes"]),
    "EXP-008": ("EP", "EP", ["delayed P100", "prolonged P100", "P100 latency", "multiple sclerosis", "optic neuritis"]),
    "EXP-009": ("EP", "EP", ["absent N20", "bilateral absence of N20", "N20 absent", "cardiac arrest", "hypoxic-ischemic", "anoxic"]),
    "EXP-010": ("VF", "VF", ["arcuate scotoma", "nasal step", "glaucoma", "glaucomatous"]),
    "EXP-011": ("VF", "VF", ["bitemporal hemianopia", "bitemporal hemianopsia", "bitemporal", "chiasm"]),
    "EXP-012": ("VF", "VF", ["homonymous hemianopia", "homonymous hemianopsia", "homonymous", "macular sparing"]),
    "EXP-013": ("OCT", "OCT", ["subretinal fluid", "pigment epithelial detachment", "neovascular age-related macular degeneration",
                               "choroidal neovascularization", "neovascular AMD", "wet AMD"]),
    "EXP-014": ("OCT", "OCT", ["diabetic macular edema", "diabetic macular oedema", "cystoid macular edema", "intraretinal fluid", "intraretinal cysts"]),
    "EXP-015": ("EP", "EP", ["optic neuritis", "delayed P100", "prolonged P100"]),
    "EXP-016": ("ACUITE", "ACUITE", ["amblyopia", "amblyopic"]),
    "EXP-017": ("ERG", "ERG", ["retinitis pigmentosa", "rod-cone dystrophy", "extinguished", "cone-rod dystrophy", "reduced amplitude"]),
    "EXP-018": ("AUDIO", "AUDIO", ["presbycusis", "age-related hearing loss", "high-frequency sensorineural", "sloping sensorineural"]),
    "EXP-019": ("TYMPANO|AUDIO", "AUDIO|TYMPANO", ["conductive hearing loss", "air-bone gap", "otitis media with effusion", "type B tympanogram",
                                                  "flat tympanogram", "otosclerosis", "Carhart notch"]),
    "EXP-020": ("AUDIO", "AUDIO", ["sudden sensorineural hearing loss", "sudden hearing loss", "SSNHL", "unilateral sensorineural"]),
    "EXP-021": ("AUDIO", "AUDIO", ["noise-induced hearing loss", "4 kHz notch", "4-kHz notch", "noise notch", "acoustic trauma"]),
    "EXP-022": ("EP", "EP|AUDIO", ["vestibular schwannoma", "acoustic neuroma", "prolonged I-V", "wave V latency", "retrocochlear"]),
    "EXP-023": ("OEA", "OEA", ["refer", "absent otoacoustic", "absent OAE", "congenital hearing loss", "auditory neuropathy", "absent wave V"]),
    "EXP-024": ("VNG", "VNG", ["benign paroxysmal positional vertigo", "BPPV", "torsional nystagmus", "geotropic", "Dix-Hallpike"]),
    "EXP-025": ("VHIT", "VHIT", ["vestibular neuritis", "catch-up saccades", "covert saccades", "overt saccades", "reduced gain", "vestibular neuronitis"]),
    "EXP-026": ("AUDIO", "AUDIO", ["Meniere", "Ménière", "low-frequency sensorineural", "low-frequency hearing loss", "endolymphatic hydrops"]),
    "EXP-027": ("AUDIO", "AUDIO", ["ototoxicity", "cisplatin", "aminoglycoside", "ototoxic", "extended high-frequency"]),
    "EXP-028": ("VFSS", "VFSS", ["silent aspiration", "aspiration", "laryngeal penetration", "penetration-aspiration"]),
    "EXP-030": ("LARYNGO", "LARYNGO", ["vocal fold paralysis", "vocal cord paralysis", "vocal fold immobility", "recurrent laryngeal nerve palsy", "vocal cord palsy"]),
    "EXP-031": ("OLFACT", "OLFACT", ["anosmia", "hyposmia", "olfactory dysfunction", "smell loss"]),
    "EXP-032": ("NCS", "NCS", ["carpal tunnel syndrome", "median neuropathy", "prolonged distal latency"]),
    "EXP-033": ("NCS", "NCS", ["axonal polyneuropathy", "axonal neuropathy", "diabetic neuropathy", "absent sural", "reduced SNAP"]),
    "EXP-034": ("NCS", "NCS", ["Guillain-Barré", "Guillain-Barre", "conduction block", "temporal dispersion", "demyelinating", "CIDP", "AIDP", "sural sparing"]),
    "EXP-035": ("NCS", "NCS", ["decremental response", "decrement", "myasthenia gravis"]),
    "EXP-036": ("NCS", "NCS", ["Lambert-Eaton", "incremental response", "increment", "post-exercise facilitation"]),
    "EXP-037": ("EMG", "EMG", ["amyotrophic lateral sclerosis", "fasciculation", "fibrillation potentials", "positive sharp waves", "motor neuron disease", "ALS"]),
    "EXP-038": ("EMG", "EMG", ["myositis", "myopathic", "polyphasic", "early recruitment", "inflammatory myopathy", "dermatomyositis"]),
    "EXP-039": ("EMG", "EMG", ["radiculopathy", "denervation", "fibrillation potentials", "positive sharp waves"]),
    "EXP-040": ("EMG", "EMG", ["muscular dystrophy", "Duchenne", "myopathic", "polyphasic", "early recruitment"]),
    "EXP-041": ("NCS", "NCS|EMG", ["nerve injury", "axonotmesis", "neurotmesis", "denervation", "absent CMAP", "Wallerian", "fibrillation potentials"]),
    "EXP-042": ("TILT", "TILT", ["orthostatic hypotension", "neurogenic orthostatic", "autonomic failure", "blood pressure drop", "autonomic neuropathy"]),
    "EXP-043": ("EP", "EP", ["cervical myelopathy", "central motor conduction time", "prolonged CMCT", "prolonged central conduction"]),
    "EXP-044": ("EP", "EP", ["loss of motor evoked potentials", "MEP loss", "signal loss", "amplitude reduction", "significant decrease", "intraoperative neuromonitoring"]),
    "EXP-045": ("ECG", "ECG", ["atrial fibrillation"]),
    "EXP-046": ("ECG", "ECG", ["atrial flutter", "flutter waves", "sawtooth"]),
    "EXP-047": ("ECG", "ECG", ["Wolff-Parkinson-White", "WPW", "delta wave", "pre-excitation", "preexcitation", "supraventricular tachycardia", "AVNRT"]),
    "EXP-048": ("ECG", "ECG", ["ventricular tachycardia", "ventricular fibrillation", "wide complex tachycardia", "capture beat", "fusion beat", "AV dissociation"]),
    "EXP-049": ("ECG", "ECG", ["Mobitz", "atrioventricular block", "AV block", "complete heart block", "third-degree", "second-degree"]),
    "EXP-050": ("ECG", "ECG", ["left bundle branch block", "LBBB", "right bundle branch block", "RBBB", "bundle branch block", "hemiblock", "fascicular block"]),
    "EXP-051": ("HOLTER", "HOLTER", ["sinus pause", "sinus arrest", "sick sinus", "sinus node dysfunction", "tachy-brady", "junctional escape"]),
    "EXP-052": ("ECG", "ECG", ["QT prolongation", "prolonged QT", "long QT", "torsade de pointes", "torsades de pointes", "QTc"]),
    "EXP-053": ("ECG", "ECG", ["Brugada", "coved", "long QT syndrome", "congenital long QT", "LQTS"]),
    "EXP-054": ("ECG", "ECG", ["hyperkalemia", "hyperkalaemia", "peaked T", "hypokalemia", "hypokalaemia", "U wave", "hypocalcemia", "hypercalcemia"]),
    "EXP-055": ("HOLTER", "HOLTER", ["asystole", "loop recorder", "syncope", "paroxysmal AV block", "high-grade AV block", "pause"]),
    "EXP-056": ("ECG", "ECG", ["pacemaker malfunction", "failure to capture", "loss of capture", "undersensing", "oversensing", "failure to sense", "pacing spike"]),
    "EXP-057": ("ECG", "ECG", ["Osborn wave", "J wave", "hypothermia", "tricyclic", "amitriptyline", "sodium channel blocker"]),
    "EXP-058": ("ECG", "ECG", ["inferior STEMI", "ST-segment elevation", "ST elevation", "STEMI", "inferior myocardial infarction"]),
    "EXP-059": ("ECG", "ECG", ["ST depression", "ST-segment depression", "Wellens", "NSTEMI", "T-wave inversion"]),
    "EXP-060": ("EXER", "EXER", ["ST depression", "ST-segment depression", "ischemia", "ischaemia", "positive exercise"]),
    "EXP-061": ("ECHO", "ECHO", ["reduced ejection fraction", "dilated cardiomyopathy", "left ventricular dysfunction", "heart failure", "LVEF"]),
    "EXP-062": ("ECHO", "ECHO", ["aortic stenosis", "peak velocity", "mean gradient", "aortic valve stenosis"]),
    "EXP-063": ("ECHO", "ECHO", ["mitral regurgitation", "PISA", "regurgitant jet", "aortic regurgitation"]),
    "EXP-064": ("RHC", "RHC", ["pulmonary arterial hypertension", "pulmonary hypertension", "precapillary"]),
    "EXP-065": ("ECG", "ECG", ["pericarditis", "PR depression", "diffuse ST elevation", "electrical alternans", "tamponade", "low voltage"]),
    "EXP-066": ("CPET", "CPET", ["heart failure", "VE/VCO2 slope", "peak VO2", "reduced peak"]),
    "EXP-067": ("MAPA", "MAPA", ["non-dipper", "non-dipping", "nondipping", "nocturnal hypertension", "masked hypertension", "white coat"]),
    "EXP-068": ("ECG", "ECG", ["left ventricular hypertrophy", "LVH", "Sokolow", "strain pattern"]),
    "EXP-069": ("ECG", "ECG", ["hypertrophic cardiomyopathy", "HCM", "apical hypertrophic", "giant negative T", "deep T-wave inversion"]),
    "EXP-082": ("MARCHE6|OXY", "MARCHE6|OXY", ["exertional desaturation", "desaturation", "interstitial lung disease", "pulmonary fibrosis"]),
    "EXP-087": ("HRM", "HRM", ["achalasia"]),
    "EXP-088": ("PH", "PH", ["gastroesophageal reflux", "acid exposure", "reflux episodes", "GERD", "acid reflux"]),
    "EXP-089": ("HRM", "HRM", ["jackhammer", "hypercontractile", "distal esophageal spasm", "diffuse esophageal spasm"]),
    "EXP-090": ("VIDANGE", "VIDANGE", ["gastroparesis", "delayed gastric emptying"]),
    "EXP-094": ("TRANSIT", "TRANSIT", ["slow transit constipation", "colonic inertia", "slow-transit", "delayed colonic transit"]),
    "EXP-095": ("ELASTO", "ELASTO", ["cirrhosis", "advanced fibrosis", "liver stiffness", "kPa"]),
    "EXP-102": ("DEBIT", "DEBIT", ["bladder outlet obstruction", "benign prostatic", "urethral stricture", "plateau", "obstructive", "reduced Qmax"]),
    "EXP-103": ("UDS", "UDS", ["detrusor overactivity", "involuntary detrusor contraction", "overactive bladder", "phasic detrusor"]),
    "EXP-104": ("UDS", "UDS", ["stress urinary incontinence", "stress incontinence", "cough leak", "leak point pressure"]),
    "EXP-105": ("UDS", "UDS", ["detrusor-sphincter dyssynergia", "detrusor sphincter dyssynergia", "DSD", "neurogenic bladder", "neurogenic detrusor"]),
    "EXP-106": ("ARM", "ARM", ["fecal incontinence", "faecal incontinence", "sphincter defect", "low resting pressure"]),
    "EXP-107": ("ARM", "ARM", ["dyssynergic defecation", "dyssynergia", "paradoxical contraction", "balloon expulsion", "outlet obstruction"]),
    "EXP-108": ("ARM", "ARM", ["Hirschsprung", "absent rectoanal inhibitory", "absence of RAIR", "absent RAIR"]),
    "EXP-109": ("CTG", "CTG", ["late deceleration", "reduced variability", "pathological CTG", "fetal distress", "sinusoidal", "prolonged deceleration"]),
    "EXP-111": ("DOPPLER_OMB", "DOPPLER_OMB", ["absent end-diastolic", "reversed end-diastolic", "AEDF", "REDF", "fetal growth restriction"]),
    "EXP-112": ("COL", "COL", ["short cervix", "funneling", "funnelling", "cervical shortening"]),
    "EXP-114": ("DOPPLER_PEN", "DOPPLER_PEN", ["arteriogenic", "arterial insufficiency", "vasculogenic erectile dysfunction", "erectile dysfunction"]),
    "EXP-115": ("HYCOSY", "HYCOSY", ["tubal occlusion", "tubal blockage", "hydrosalpinx", "tubal obstruction"]),
    "EXP-116": ("CAPILLARO", "CAPILLARO", ["scleroderma pattern", "systemic sclerosis", "giant capillaries", "megacapillaries", "microhemorrhages", "avascular"]),
    "EXP-117": ("ALLEN", "ALLEN", ["abnormal Allen", "incomplete palmar arch", "ulnar artery occlusion", "positive Allen"]),
    "EXP-118": ("NCS", "NCS", ["ulnar neuropathy", "cubital tunnel", "ulnar nerve entrapment", "slowing across the elbow"]),
    "EXP-119": ("NCS|EMG", "NCS|EMG", ["brachial plexus", "root avulsion", "preganglionic", "plexopathy"]),
    "EXP-120": ("DYNAMO", "DYNAMO", ["sarcopenia", "low grip strength", "weak grip", "reduced grip strength", "frailty"]),
    "EXP-121": ("IPS", "IPS", ["peripheral artery disease", "peripheral arterial disease", "monophasic", "dampened", "ankle-brachial index"]),
    "EXP-122": ("TCPO2", "TCPO2", ["critical limb ischemia", "chronic limb-threatening", "CLTI", "toe pressure", "TcPO2"]),
    "EXP-123": ("DOPPLER_VEIN", "DOPPLER_VEIN", ["venous reflux", "saphenous reflux", "venous insufficiency", "great saphenous vein reflux", "varicose"]),
    "EXP-124": ("MARCHE", "MARCHE", ["slow gait", "gait speed", "Timed Up and Go", "falls", "frailty"]),
    "EXP-125": ("DXA", "DXA", ["sarcopenia", "appendicular lean", "low muscle mass", "appendicular skeletal muscle"]),
    "EXP-126": ("POSTURO", "POSTURO", ["Romberg", "postural instability", "increased sway", "balance impairment", "vestibular"]),
    "EXP-127": ("NCS", "NCS", ["peroneal neuropathy", "fibular neuropathy", "fibular head", "conduction block", "peroneal nerve palsy", "foot drop"]),
    "EXP-128": ("PSG", "PSG", ["obstructive sleep apnea", "obstructive sleep apnoea", "obstructive apnea", "OSA", "hypopnea", "desaturation"]),
    "EXP-129": ("PSG", "PSG", ["Cheyne-Stokes", "central sleep apnea", "central sleep apnoea", "central apnea", "periodic breathing"]),
    "EXP-130": ("MSLT", "MSLT|PSG", ["narcolepsy", "SOREMP", "sleep-onset REM", "cataplexy"]),
    "EXP-131": ("PSG", "PSG", ["periodic limb movements", "PLMS", "restless legs", "periodic leg movements"]),
    "EXP-132": ("PSG", "PSG", ["REM sleep behavior disorder", "REM sleep behaviour disorder", "REM sleep without atonia", "RSWA", "RBD"]),
    "EXP-133": ("ACTI", "ACTI", ["delayed sleep phase", "delayed sleep-wake phase", "circadian rhythm disorder", "insomnia", "irregular sleep"]),
    "EXP-134": ("MSLT", "MSLT", ["sleepiness", "short sleep latency", "maintenance of wakefulness", "excessive daytime sleepiness"]),
    "EXP-135": ("OXY", "OXY", ["nocturnal desaturation", "nocturnal hypoxemia", "sleep-related hypoxemia", "hypoventilation", "COPD"]),
    "EXP-151": ("DERMO", "DERMO", ["melanoma", "blue-white veil", "atypical network", "atypical pigment network"]),
    "EXP-152": ("ECG", "ECG", ["QT prolongation", "prolonged QT", "long QT", "antipsychotic", "torsade", "QTc"]),
    "EXP-153": ("EEG", "EEG", ["diffuse slowing", "delirium", "triphasic waves", "encephalopathy", "theta", "delta"]),
}

EXCLU_RX = re.compile(r"H&E|hematoxylin|haematoxylin|eosin|micrograph|immunohisto|histolog|histopath|flow ?chart|PRISMA|forest plot|Kaplan|"
                      r"schematic|diagram|illustration|cartoon|drawing", re.I)
RADIO_RX = re.compile(r"\bCT\b|computed tomogra|\bMRI\b|magnetic resonance|radiograph|\bPET\b", re.I)
NEG_RX = re.compile(r"no (evidence|sign|signs) of|without (evidence|signs?) of|ruled out|was excluded|resolution of|resolved|"
                    r"normali[sz]ed|after (treatment|therapy|ablation|cardioversion|correction)|post-?treatment|remission", re.I)
NORMAL_FAUX_RX = re.compile(r"(absence|loss|lack|disappearance) of (the )?normal|compared (with|to) (the )?normal|instead of|rather than|than normal|"
                            r"returned to normal|return to normal|\bno normal|without normal|normal(ly)? (limits )?.{0,15}(except|but)|upper limit of normal|lower limit of normal", re.I)
STAT_RX = re.compile(r"correlat|association|\baverage|\bmean (value|threshold|curve|data)|as a function of|\bgroups?\b|box ?plot|scatter|"
                     r"\bROC\b|regression|prevalence|participants|cohort|classification scheme|criteria|meta-analys|odds ratio|"
                     r"sensitivity and specificity|bar (graph|chart)|histogram|study design|enrol|questionnaire", re.I)
NORMAL_NEG_RX = re.compile(r"abnormal|patholog|lesion|block\b|fibrillation|tachycardia|elevation|depression|delay|prolong|loss|absent|"
                           r"reduced|decreased|impair", re.I)


def familles(spec):
    return [K[f] for f in spec.split("|")]


def score_trace(texte, ctx, role, mc_sub=None, exige_famille=True):
    """Score d'une légende de tracé ; None = rejet. Renvoie (score, motifs, panneau)."""
    if not texte or EXCLU_RX.search(texte):
        return None
    fams = ctx["fam"][role]
    pre, segs = C.panneaux(texte)
    cibles = [(None, texte)] if not segs else [(l, pre + " " + s) for l, s in segs]
    meilleur = None
    for lettre, t in cibles:
        seg = t[len(pre):] if lettre else t
        sc, motifs = 0.0, []
        if any(f["crx"].search(t) for f in fams):
            sc += 2; motifs.append("tracé")
        elif mc_sub and any(mc_sub in f["mc"] for f in fams):
            sc += 1; motifs.append("type d'index")
        elif exige_famille:
            continue
        else:
            sc -= 1
        if mc_sub and any(mc_sub in f["mc"] for f in fams):
            sc += 1; motifs.append(f"index {mc_sub}")
        if role == "patho":
            best = 0
            for i, terme in enumerate(ctx["termes_en"]):
                m = C.match_terme(terme, seg)
                if not m and lettre:
                    m = C.match_terme(terme, pre) * 0.75
                if m:
                    best = max(best, (2.5 if m >= 2 else 1.5) + (1 if i == 0 else 0) + m)
            if not best:
                continue
            sc += best; motifs.append("diagnostic")
            if NEG_RX.search(seg):
                continue
            if re.search(r"\bnormal\b", seg, re.I):
                sc -= 1; motifs.append("contient «normal»")
        else:
            normal = C.NORMAL_RX.search(seg) and not NORMAL_FAUX_RX.search(seg)
            extra = any(f["cnrm"].search(seg) for f in fams)
            if not (normal or extra):
                continue
            sc += 2.5 if normal else 2; motifs.append("normal")
            if extra and normal:
                sc += 1; motifs.append("indice propre")
            if NORMAL_NEG_RX.search(seg):
                sc -= 1.5; motifs.append("mot pathologique")
            if any(C.match_terme(tm, seg) for tm in ctx["termes_en"][:3]):
                sc -= 1; motifs.append("terme du diagnostic")
        if RADIO_RX.search(seg) and not any(f["crx"].search(seg) for f in fams):
            sc -= 1.5; motifs.append("autre modalité")
        if STAT_RX.search(t):
            sc -= 2; motifs.append("graphique de groupe")
        if lettre:
            sc -= 0.5; motifs.append(f"panneau {lettre}")
        if len(t) > 700:
            sc -= 0.5
        if meilleur is None or sc > meilleur[0]:
            meilleur = (round(sc, 2), motifs, lettre)
    return meilleur


# ---------------------------------------------------------------- index locaux (tous types sauf anatomopathologie)
def charger_index_traces():
    f_cache = os.path.join(C.CACHE, "index_traces.json")
    if os.path.exists(f_cache):
        recs = json.load(open(f_cache, encoding="utf-8"))
        log(f"Index tracés (cache) : {len(recs)} légendes candidates")
        return recs
    union = re.compile("|".join(f"(?:{v['rx']})" for v in K.values()), re.I)
    recs = []
    f = os.path.join(C.INDEX, "mc_captions_and_labels.csv")
    if os.path.exists(f):
        csv.field_size_limit(10 ** 8)
        with open(f, encoding="utf-8") as fh:
            for row in csv.DictReader(fh):
                if row["image_type"] == "pathology" or not C.lic_libre(row["license"]) or not union.search(row["caption"]):
                    continue
                m = re.match(r"(PMC\d+)_\d+_(.+)$", row["main_image"])
                if m:
                    recs.append({"src": "MultiCaRe", "pmcid": m.group(1), "fichier": m.group(2), "legende": row["caption"],
                                 "sub": row["image_subtype"], "licence": row["license"]})
    lic = {}
    f = os.path.join(C.INDEX, "roco_license_information.csv")
    if os.path.exists(f):
        with open(f, encoding="utf-8") as fh:
            for row in csv.DictReader(fh):
                lic[row["ID"]] = (row["PMCID"], row["Attribution"])
    for f in glob.glob(os.path.join(C.INDEX, "roco_*_captions.csv")):
        with open(f, encoding="utf-8") as fh:
            for row in csv.DictReader(fh):
                pm, att = lic.get(row["ID"], (None, ""))
                if pm and C.lic_libre(att) and union.search(row["Caption"]):
                    recs.append({"src": "ROCOv2", "pmcid": pm, "fichier": None, "legende": row["Caption"], "sub": None, "licence": att[:12]})
    json.dump(recs, open(f_cache, "w", encoding="utf-8"), ensure_ascii=False)
    log(f"Index tracés : {len(recs)} légendes candidates (MultiCaRe hors anatomopathologie + ROCOv2)")
    return recs


def chercher_index_traces(recs, ctx, role, limite=40):
    res = []
    rxs = [f["crx"] for f in ctx["fam"][role]]
    for r in recs:
        leg = r["legende"]
        if not any(x.search(leg) for x in rxs):
            continue
        s = score_trace(leg, ctx, role, mc_sub=r["sub"])
        if s:
            res.append({"source": r["src"], "pmcid": r["pmcid"], "fichier": r["fichier"], "legende": leg, "score": s[0],
                        "motifs": s[1], "panneau": s[2], "licence_index": r["licence"], "sub": r["sub"]})
    res.sort(key=lambda x: -x["score"])
    return res[:limite]


def chercher_epmc_traces(ctx, role, max_articles=12):
    figs_q = " OR ".join(f["fig"] for f in ctx["fam"][role])
    if role == "patho":
        reqs = [f'FIG:"{t}" AND ({figs_q}) AND OPEN_ACCESS:y AND {C.LIC_Q} AND IN_EPMC:y' for t in ctx["termes_en"][:3]]
    else:
        reqs = [f'(FIG:normal OR FIG:healthy) AND ({figs_q}) AND OPEN_ACCESS:y AND {C.LIC_Q} AND IN_EPMC:y']
    pmcids = []
    for q in reqs:
        j = C.http_json("https://www.ebi.ac.uk/europepmc/webservices/rest/search",
                        {"query": q, "format": "json", "resultType": "lite", "pageSize": 15}, source="epmc")
        for res in ((j or {}).get("resultList") or {}).get("result", []):
            if res.get("pmcid") and res["pmcid"] not in pmcids:
                pmcids.append(res["pmcid"])
    out = []
    for pm in pmcids[:max_articles]:
        figs, _ = C.figures_pmc(pm)
        for f in figs:
            s = score_trace(f["legende"], ctx, role)
            if s:
                out.append({"source": "EuropePMC", "pmcid": pm, "fichier": f["href"], "legende": f"{f['label']} {f['legende']}".strip(),
                            "score": s[0], "motifs": s[1], "panneau": s[2]})
    return out


def candidats_commons_traces(ctx):
    titres = {"patho": [], "normal": []}
    fp, fn = ctx["fam"]["patho"][0], ctx["fam"]["normal"][0]
    for t in ctx["termes_en"][:2]:
        titres["patho"] += C.commons_search(f'{fp["com"]} {t}', 15)
    titres["normal"] += C.commons_search(f'normal {fn["com"]}', 15)
    tous = list(dict.fromkeys(titres["patho"] + titres["normal"]))
    infos = C.commons_info(tous) if tous else {}
    out = {"patho": [], "normal": []}
    for role in ("patho", "normal"):
        for t in dict.fromkeys(titres[role]):
            ii = infos.get(t)
            if not ii or ii.get("mime") not in ("image/jpeg", "image/png", "image/gif", "image/tiff", "image/webp"):
                continue
            em = ii.get("extmetadata", {})
            lic = C.sans_html((em.get("LicenseShortName") or {}).get("value", ""))
            if not C.lic_libre(lic) and not re.search(r"public domain|^PD", lic, re.I):
                continue
            desc = C.sans_html((em.get("ImageDescription") or {}).get("value", ""))
            texte = t[5:].rsplit(".", 1)[0].replace("_", " ") + ". " + desc
            s = score_trace(texte, ctx, role)
            if not s:
                continue
            sc, motifs, pan = s
            if min(ii.get("width", 0), 10000) < 400:
                sc -= 1; motifs = motifs + ["petite image"]
            out[role].append({"source": "Commons", "titre": t, "legende": texte[:900], "score": round(sc, 2), "motifs": motifs,
                              "panneau": pan, "licence": lic, "url_image": C.miniature_standard(ii),
                              "url_source": ii.get("descriptionurl"), "auteur": C.sans_html((em.get("Artist") or {}).get("value", ""))[:300],
                              "credit": C.sans_html((em.get("Credit") or {}).get("value", ""))[:300],
                              "taille": f'{ii.get("width")}x{ii.get("height")}'})
    return out


# ---------------------------------------------------------------- traitement
def charger_cibles():
    rec = json.load(open(os.path.join(C.RECENS, "recensement.json"), encoding="utf-8"))
    enr = {}
    for f in sorted(glob.glob(os.path.join(C.RECENS, "enrichi", "EXP_*.json"))):
        try:
            enr.update(json.load(open(f, encoding="utf-8")))
        except ValueError:
            log(f"  ! {f} illisible")
    cibles = []
    for e in rec["explorations"]:
        tech = e["explorations"][0]["tech"]
        if tech in EXCLUS:
            continue
        cibles.append((e, tech, enr.get(e["id"], {})))
    return cibles


def contexte_trace(e, tech, enr):
    fn, fp, termes = T[e["id"]]
    ac = (enr.get("traces") or {}).get("a_chercher") or {}
    return {"id": e["id"], "diagnostic": e["diagnostic"], "tech": tech, "gold": (enr.get("gold") or {}).get("examen", ""),
            "termes_en": termes, "spec": {"normal": fn, "patho": fp},
            "fam": {"normal": familles(fn), "patho": familles(fp)}, "desc": {"normal": ac.get("normal", ""), "patho": ac.get("patho", "")}}


def traiter(e, tech, enr, recs, force=False, complement=False, sans_commons=False):
    iid = e["id"]
    dossier = os.path.join(C.CANDIDATS, iid)
    sortie = os.path.join(dossier, "candidats.json")
    if os.path.exists(sortie) and not force:
        anc = json.load(open(sortie, encoding="utf-8"))
        if not (complement and anc.get("commons_a_completer")):
            return anc
    os.makedirs(dossier, exist_ok=True)
    ctx = contexte_trace(e, tech, enr)
    fpool = os.path.join(dossier, "pool_pmc.json")
    if os.path.exists(fpool):
        pool = json.load(open(fpool, encoding="utf-8"))
    else:
        pool = {"patho": [], "normal": []}
        for role in ("patho", "normal"):
            pool[role] += chercher_index_traces(recs, ctx, role)
            pool[role] += chercher_epmc_traces(ctx, role)
        json.dump(pool, open(fpool, "w", encoding="utf-8"), ensure_ascii=False)
    pool2 = {}
    for role, liste in pool.items():  # re-score à chaque passe
        pool2[role] = []
        for c in liste:
            s = score_trace(c["legende"], ctx, role, mc_sub=c.get("sub"))
            if s:
                pool2[role].append(dict(c, score=s[0], motifs=s[1], panneau=s[2]))
    pool = pool2
    if sans_commons:
        incomplet = True
    else:
        e0 = C.ETAT_COMMONS["echecs"]
        com = candidats_commons_traces(ctx)
        incomplet = C.ETAT_COMMONS["echecs"] > e0
        for role in ("patho", "normal"):
            pool[role] += com[role]
    for vieux in glob.glob(os.path.join(dossier, "*.jpg")):
        os.remove(vieux)
    res = {"id": iid, "diagnostic": e["diagnostic"], "tech": tech, "gold": ctx["gold"], "date": f"{datetime.now():%Y-%m-%d %H:%M}",
           "commons_a_completer": incomplet, "requete": {"termes_en": ctx["termes_en"], "familles": ctx["spec"]}}
    for role in ("normal", "patho"):
        res[role] = {"a_chercher": ctx["desc"][role], "modalite": ctx["spec"][role].replace("|", " / "), "details": [],
                     "nb_bruts": len(pool[role]), "candidats": C.selectionner(pool[role], dossier, role)}
    tmp = sortie + ".tmp"
    json.dump(res, open(tmp, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    os.replace(tmp, sortie)
    log(f"{iid} {e['diagnostic'][:45]} : normal {len(res['normal']['candidats'])}/{res['normal']['nb_bruts']}, "
        f"patho {len(res['patho']['candidats'])}/{res['patho']['nb_bruts']}")
    return res


def resultats():
    out = []
    for e, tech, _ in charger_cibles():
        p = os.path.join(C.CANDIDATS, e["id"], "candidats.json")
        out.append((e, json.load(open(p, encoding="utf-8")) if os.path.exists(p) else None))
    return out


def stats():
    rs = resultats()
    n = len(rs)
    faits = [r for _, r in rs if r]
    p1 = sum(1 for r in faits if r["patho"]["candidats"]); n1 = sum(1 for r in faits if r["normal"]["candidats"])
    deux = sum(1 for r in faits if r["patho"]["candidats"] and r["normal"]["candidats"])
    src = {}
    for r in faits:
        for role in ("normal", "patho"):
            for c in r[role]["candidats"]:
                src[c["source"]] = src.get(c["source"], 0) + 1
    print(f"Cibles (hors VENT/DYN) : {n} ; traitées : {len(faits)}")
    print(f"≥1 patho : {p1}/{n} ({100*p1/n:.0f} %) ; ≥1 normal : {n1}/{n} ({100*n1/n:.0f} %) ; les deux : {deux}/{n} ({100*deux/n:.0f} %)")
    print(f"Par source : {src} ; Commons à compléter : {sum(1 for r in faits if r.get('commons_a_completer'))}")
    print("Sans patho : " + ", ".join(r["id"] for r in faits if not r["patho"]["candidats"]))
    print("Sans normal : " + ", ".join(r["id"] for r in faits if not r["normal"]["candidats"]))


def planche(sortie=os.path.join(ICI, "planche_traces.html")):
    import planche as P
    rs = [r for _, r in resultats() if r]
    n = len(rs) or 1
    p1 = sum(1 for r in rs if r["patho"]["candidats"]); n1 = sum(1 for r in rs if r["normal"]["candidats"])
    E = P.E
    blocs = []
    for r in rs:
        roles = []
        for role, nom in (("normal", "Normal"), ("patho", "Pathologique")):
            d = r[role]
            cartes = "".join(P.carte(c, i + 1) for i, c in enumerate(d["candidats"])) or '<p class="vide">Aucun candidat libre fiable.</p>'
            roles.append(f'<div class="role {role}"><h3>{nom} · {E(d["modalite"])}</h3>'
                         f'<p class="voulu">Voulu : {E(d["a_chercher"])}</p><div class="grille">{cartes}</div></div>')
        rep = " · Commons à compléter" if r.get("commons_a_completer") else ""
        blocs.append(f'<section class="dx" id="{E(r["id"])}"><h2>{E(r["id"])} — {E(r["diagnostic"])} <small>{E(r["tech"])}{rep}</small></h2>'
                     f'<p class="gold">Examen de référence : {E(r.get("gold", ""))}</p>{"".join(roles)}</section>')
    page = (f'<!doctype html><html lang="fr"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">'
            f'<title>Planche des tracés</title><style>{P.CSS}</style></head><body>'
            f'<h1>Planche de contrôle des tracés candidats (explorations fonctionnelles)</h1>'
            f'<p class="resume">{len(rs)} explorations (VENT et DYN exclues) · ≥1 normal : {n1} ({100*n1//n} %) · ≥1 pathologique : {p1} ({100*p1//n} %). '
            f'Licences libres seulement (CC0, domaine public, CC BY, CC BY-SA ; NC/ND et articles rétractés rejetés). '
            f'Choix final après vérification visuelle.</p>'
            f'<nav><input id="q" placeholder="Filtrer (id, diagnostic, mot de légende)"></nav>'
            f'{"".join(blocs)}<script>{P.JS}</script></body></html>')
    open(sortie, "w", encoding="utf-8").write(page)
    print(f"Planche : {sortie} ({len(rs)} explorations)")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--ids", nargs="*")
    ap.add_argument("--force", action="store_true")
    ap.add_argument("--complement", action="store_true")
    ap.add_argument("--sans-commons", action="store_true")
    ap.add_argument("--stats", action="store_true")
    ap.add_argument("--planche", action="store_true")
    ap.add_argument("--fils", type=int, default=4, help="parallélisme de la passe 1 (sans Commons)")
    a = ap.parse_args()
    if a.stats:
        return stats()
    if a.planche:
        return planche()
    os.makedirs(C.CANDIDATS, exist_ok=True)
    cibles = [c for c in charger_cibles() if not a.ids or c[0]["id"] in a.ids]
    manq = [c[0]["id"] for c in cibles if c[0]["id"] not in T]
    if manq:
        log(f"  ! sans table de traduction : {', '.join(manq)}")
    recs = charger_index_traces()
    log(f"Début tracés : {len(cibles)} explorations ({a.fils} fils)")

    def un(c):
        e, tech, enr = c
        if e["id"] not in T:
            return
        try:
            traiter(e, tech, enr, recs, a.force, a.complement, a.sans_commons)
        except Exception as ex:
            log(f"  ! {e['id']} échec {ex.__class__.__name__}: {ex}")
    if a.fils > 1 and a.sans_commons:  # Commons reste séquentiel (429)
        from concurrent.futures import ThreadPoolExecutor
        with ThreadPoolExecutor(a.fils) as ex:
            list(ex.map(un, cibles))
    else:
        for c in cibles:
            un(c)
    log("Fin.")


if __name__ == "__main__":
    main()
