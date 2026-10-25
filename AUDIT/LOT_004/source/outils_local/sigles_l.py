#!/usr/bin/env python3
"""sigles.py — ajoute (ou remplace) une fenêtre « Sigles et abréviations » au début de la monographie d'un fichier corrigé.
Usage : sigles.py FICHIER.html   (modifie le fichier en place ; travail local uniquement)
Seuls les sigles réellement présents dans le texte et connus du dictionnaire ci-dessous sont listés ;
les sigles inconnus sont affichés sur la sortie standard pour complément manuel (aucun développement inventé)."""
import sys, os, re
from bs4 import BeautifulSoup
sys.path.insert(0, '/workspace/audit_1_10/outils'); sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from style import SIGLE, UNITS, ROMAN

DEV = {
 'AWMF': 'Arbeitsgemeinschaft der Wissenschaftlichen Medizinischen Fachgesellschaften (registre allemand des lignes directrices)',
 'BOTOX': 'nom de marque de la toxine botulique A d’Allergan',
 'HDSS': 'Hyperhidrosis Disease Severity Scale (échelle de sévérité de l’hyperhidrose)',
 'QSART': 'Quantitative Sudomotor Axon Reflex Test (test quantitatif du réflexe axonal sudomoteur)',
 'USZ': 'Universitätsspital Zürich (Hôpital universitaire de Zurich)',
 'ADN': 'acide désoxyribonucléique',
 'ARN': 'acide ribonucléique',
 'AUC': 'aire sous la courbe des concentrations',
 'BAAR': 'bacilles acido-alcoolo-résistants',
 'ECBU': 'examen cytobactériologique des urines',
 'ENDO': 'EURO-ENDO, registre européen de l’endocardite',
 'EURO': 'EURO-ENDO, registre européen de l’endocardite',
 'HACEK': 'Haemophilus, Aggregatibacter, Cardiobacterium, Eikenella, Kingella',
 'IgG': 'immunoglobulines G',
 'IgM': 'immunoglobulines M',
 'POET': 'Partial Oral Endocarditis Treatment, essai danois',
 'TAVI': 'implantation transcathéter d’une valve aortique',
 'UFC': 'unités formant colonies',
 'ACTH': 'hormone corticotrope (adrénocorticotrophine)',
 'BPCO': 'bronchopneumopathie chronique obstructive',
 'ENETS': 'European Neuroendocrine Tumor Society',
 'FDG': 'fluorodésoxyglucose',
 'GLP': 'glucagon-like peptide (peptide apparenté au glucagon)',
 'IDF': 'International Diabetes Federation (Fédération internationale du diabète)',
 'IHSG': 'International Hypoglycaemia Study Group',
 'IM': 'intramusculaire',
 'JBDS': 'Joint British Diabetes Societies',
 'LADA': 'diabète auto-immun latent de l’adulte',
 'LiMA': 'liste des moyens et appareils (LAMal)',
 'MNT': 'maladies non transmissibles',
 'MR': 'libération modifiée (modified release)',
 'PEDLAUS': 'protocoles pédiatriques Lausanne (CHUV)',
 'SGLT2': 'cotransporteur sodium-glucose de type 2',
 'SSML': 'Société suisse de médecine légale',
 'AAS': 'acide acétylsalicylique',
 'ABCDE': 'séquence Airway, Breathing, Circulation, Disability, Exposure (voies aériennes, respiration, circulation, neurologie, exposition)',
 'ACS': 'acute coronary syndrome (syndrome coronarien aigu)',
 'AED': 'automated external defibrillator (défibrillateur automatisé externe)',
 'AIT': 'accident ischémique transitoire',
 'AVC': 'accident vasculaire cérébral',
 'BLS': 'basic life support (réanimation de base)',
 'COX': 'cyclo-oxygénase',
 'CYP2C19': 'cytochrome P450 2C19',
 'CYP3A4': 'cytochrome P450 3A4',
 'ClCr': 'clairance de la créatinine (Cockcroft-Gault, mL/min)',
 'CoA': 'coenzyme A',
 'DAPT': 'double antiagrégation plaquettaire',
 'EAS': 'European Atherosclerosis Society',
 'ESUR': 'European Society of Urogenital Radiology',
 'FC': 'fréquence cardiaque',
 'FFR': 'fractional flow reserve (réserve coronaire de débit)',
 'GRACE': 'Global Registry of Acute Coronary Events (score de risque)',
 'HDL': 'lipoprotéines de haute densité',
 'HMG': 'hydroxyméthylglutaryl',
 'IIa': 'facteur II activé (thrombine)',
 'LDL': 'lipoprotéines de basse densité',
 'MINOCA': 'myocardial infarction with non-obstructive coronary arteries (infarctus sans sténose coronaire significative)',
 'NSTE': 'sans sus-décalage persistant du segment ST',
 'NSTEMI': 'infarctus sans sus-décalage du segment ST',
 'OAC': 'ordonnance réglant l’admission à la circulation routière',
 'OFS': 'Office fédéral de la statistique',
 'P2Y12': 'récepteur plaquettaire de l’adénosine diphosphate',
 'PAS': 'pression artérielle systolique',
 'PCSK9': 'proprotéine convertase subtilisine/kexine de type 9',
 'SC': 'sous-cutané',
 'SCA': 'syndrome coronarien aigu',
 'SCORE2': 'Systematic Coronary Risk Evaluation 2 (risque cardiovasculaire à 10 ans)',
 'SRC': 'Swiss Resuscitation Council (conseil suisse de réanimation)',
 'STEMI': 'infarctus avec sus-décalage du segment ST',
 'V3R': 'dérivation précordiale droite en miroir de V3',
 'V4R': 'dérivation précordiale droite en miroir de V4 (infarctus du ventricule droit)',
 'AINS': 'anti-inflammatoire non stéroïdien', 'AIPS': 'information professionnelle suisse des médicaments (Swissmedic)',
 'ALAT': 'alanine aminotransférase', 'AMP': 'adénosine monophosphate', 'ANCA': 'anticorps anti-cytoplasme des polynucléaires neutrophiles',
 'ARA': 'antagoniste des récepteurs de l’angiotensine II', 'ASAT': 'aspartate aminotransférase', 'ATA': 'American Thyroid Association',
 'ATS': 'antithyroïdien de synthèse', 'AVK': 'antivitamine K', 'BWPS': 'score de Burch-Wartofsky', 'CAS': 'Clinical Activity Score',
 'CHA2DS2': 'score de risque embolique de la fibrillation atriale', 'VASc': 'second volet du score de risque embolique',
 'CIVD': 'coagulation intravasculaire disséminée', 'CK': 'créatine kinase', 'CKD': 'maladie rénale chronique (Chronic Kidney Disease)', 'CRP': 'protéine C réactive',
 'CT': 'tomodensitométrie', 'DFGe': 'débit de filtration glomérulaire estimé', 'DOTATATE': 'traceur analogue de la somatostatine',
 'DRESS': 'réaction médicamenteuse avec éosinophilie et symptômes systémiques', 'DXA': 'absorptiométrie biphotonique à rayons X',
 'ECG': 'électrocardiogramme', 'EDTA': 'acide éthylène-diamine-tétra-acétique (anticoagulant du tube)', 'EPI': 'équipement de protection individuelle',
 'EPO': 'érythropoïétine', 'ETA': 'European Thyroid Association', 'EU': 'européen', 'EUGOGO': 'European Group on Graves’ Orbitopathy',
 'FA': 'fibrillation atriale', 'FEVG': 'fraction d’éjection du ventricule gauche', 'FRAX': 'outil d’estimation du risque fracturaire à 10 ans',
 'FcRn': 'récepteur Fc néonatal', 'FSC': 'formule sanguine complète', 'GGT': 'gamma-glutamyl-transférase', 'GREAT': 'score prédictif de rechute du Basedow (Graves’ Recurrent Events After Therapy)',
 'HbA1c': 'hémoglobine glyquée', 'IEC': 'inhibiteur de l’enzyme de conversion', 'IGF': 'insulin-like growth factor', 'IMAO': 'inhibiteur de la monoamine oxydase',
 'INR': 'International Normalized Ratio', 'IRM': 'imagerie par résonance magnétique', 'IV': 'intraveineux', 'JTA': 'Japan Thyroid Association', 'KDIGO': 'Kidney Disease: Improving Global Outcomes',
 'LAA': 'loi fédérale sur l’assurance-accidents', 'LAI': 'loi fédérale sur l’assurance-invalidité', 'LAMal': 'loi fédérale sur l’assurance-maladie',
 'LLC': 'leucémie lymphoïde chronique', 'LSN': 'limite supérieure de la normale', 'LUKS': 'Luzerner Kantonsspital', 'MIBG': 'méta-iodobenzylguanidine',
 'NFS': 'numération formule sanguine', 'NT': 'N-terminal (NT-proBNP)', 'OH': 'hydroxy (25-OH-vitamine D)', 'OrPha': 'nom du titulaire (Esmolol OrPha®)',
 'OSAV': 'Office fédéral de la sécurité alimentaire et des affaires vétérinaires', 'OFSP': 'Office fédéral de la santé publique',
 'PAL': 'phosphatases alcalines', 'PAM': 'pression artérielle moyenne', 'PR': 'intervalle PR de l’ECG', 'PTH': 'parathormone', 'PTHrP': 'peptide apparenté à la parathormone',
 'PTI': 'purpura thrombopénique immunologique', 'PTU': 'propylthiouracile', 'QRS': 'complexe QRS de l’ECG', 'QT': 'intervalle QT de l’ECG', 'QTc': 'intervalle QT corrigé',
 'SHBG': 'protéine porteuse des hormones sexuelles', 'SIADH': 'sécrétion inappropriée d’hormone antidiurétique', 'SpO2': 'saturation pulsée en oxygène',
 'SSCC': 'Société suisse de chimie clinique', 'SSED': 'Société suisse d’endocrinologie et de diabétologie', 'ST': 'segment ST de l’ECG', 'STIR': 'séquence IRM de suppression de la graisse',
 'T3L': 'triiodothyronine libre', 'T4L': 'thyroxine libre', 'TCA': 'temps de céphaline activée', 'TEP': 'tomographie par émission de positons',
 'TIH': 'thrombopénie induite par l’héparine', 'TIRADS': 'système de classement échographique des nodules thyroïdiens', 'TP': 'taux de prothrombine',
 'TPO': 'thyroperoxydase', 'TRAb': 'anticorps anti-récepteur de la thyréostimuline', 'TSH': 'thyréostimuline', 'TSI': 'immunoglobulines stimulant la thyroïde',
 'VGM': 'volume globulaire moyen', 'VIH': 'virus de l’immunodéficience humaine', 'VS': 'vitesse de sédimentation', 'SpO': 'saturation pulsée en oxygène',
 'BNP': 'peptide natriurétique de type B', 'CHUV': 'Centre hospitalier universitaire vaudois', 'HUG': 'Hôpitaux universitaires de Genève', 'SFE': 'Société française d’endocrinologie',
 'NHS': 'National Health Service', 'FDA': 'Food and Drug Administration', 'BTA': 'British Thyroid Association', 'ALT': 'alanine aminotransférase', 'TS1': 'crise thyrotoxique certaine (JTA)', 'TS2': 'crise thyrotoxique probable (JTA)',
 'ICU': 'soins intensifs', 'IGRA': 'test de libération d’interféron gamma', 'PCR': 'amplification génique', 'IMC': 'indice de masse corporelle', 'SA': 'semaines d’aménorrhée',
 'TDM': 'tomodensitométrie', 'TBG': 'globuline liant la thyroxine', 'TRH': 'thyréolibérine', 'GO': 'orbitopathie de Basedow', 'RAI': 'iode radioactif',
 'ESC': 'European Society of Cardiology', 'ETO': 'échocardiographie transœsophagienne', 'ETT': 'échocardiographie transthoracique',
 'JAK2': 'Janus kinase 2', 'ADA': 'adénosine désaminase', 'CO': 'monoxyde de carbone', 'OMS': 'Organisation mondiale de la santé', 'VD': 'ventricule droit',
}
from sigles_extra import DEV_EXTRA
DEV.update(DEV_EXTRA)
MARK = 'sigles-auto'

def main(f):
    html = open(f, encoding='utf-8').read()
    soup = BeautifulSoup(html, 'html.parser')
    old = soup.find(id=MARK)
    if old: old.decompose()
    body = soup.find('details', class_='monographie') or soup.body
    txt = ' '.join(t for t in body.find_all(string=True))
    found, unknown = [], set()
    for m in SIGLE.finditer(txt):
        sg = m.group(1)
        if sg in UNITS or ROMAN.match(sg) or re.fullmatch(r'[A-Z]\d+|\d+[A-Z]|S\d+', sg) or len(sg) > 12: continue
        if sg in DEV:
            if sg not in found: found.append(sg)
        else: unknown.add(sg)
    found.sort(key=str.lower)
    items = ''.join(f'<li><strong>{s}</strong> ({DEV[s]})</li>' for s in found)
    frag = BeautifulSoup(f'<details class="fenetre sigles" id="{MARK}"><summary>Sigles et abréviations de ce fichier</summary><ul class="s">{items}</ul></details>', 'html.parser')
    summ = body.find('summary') if body.name == 'details' else None
    (summ.insert_after if summ else body.insert)(*( [frag] if summ else [0, frag]))
    open(f, 'w', encoding='utf-8').write(str(soup))
    print(f'{os.path.basename(f)} : {len(found)} sigles listés ; inconnus (à compléter) : {sorted(unknown)}')

if __name__ == '__main__':
    for f in sys.argv[1:]: main(f)
