#!/usr/bin/env python3
"""examens.py — détection déterministe des examens complémentaires (lexique français) et contrôle de la
nouvelle exigence : chaque examen cliquable (fenêtre) avec 2 onglets « Principe » et « Interprétation ».
Usage : examens.py LOT_001   (lit work/LOT_001/decoupe.json, écrit work/LOT_001/examens.json)
Cliquable = l'occurrence est dans le <summary> d'une fenêtre <details>, ou dans <a href>/<button>/[onclick]/[role=tab]/popover.
2 onglets = la fenêtre ouverte contient deux libellés courts « Principe » et « Interprétation »."""
import sys, os, re, json
sys.path.insert(0, '/workspace/audit_1_10/outils'); sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from commun import work

# (nom canonique, catégorie, regex)  — catégories : BIO, FONC, IMG, AUTRE (anapath, endoscopie, tests)
LEX = [
 ('NFS / hémogramme', 'BIO', r"\bNFS\b|h[ée]mogramme|formule sanguine|num[ée]ration[- ]formule"),
 ('CRP', 'BIO', r"\bCRP\b|prot[ée]ine C[- ]r[ée]active"),
 ('Procalcitonine (PCT)', 'BIO', r"\bPCT\b|procalcitonine"),
 ('Vitesse de sédimentation (VS)', 'BIO', r"vitesse de s[ée]dimentation|\bVS\b(?= |,|\))"),
 ('Ionogramme / électrolytes', 'BIO', r"ionogramme|[ée]lectrolytes|natr[ée]mie|kali[ée]mie|calc[ée]mie"),
 ('Créatinine / DFGe', 'BIO', r"cr[ée]atinin|\bDFGe?\b|cl(?:ai)?rance de la cr"),
 ('Urée', 'BIO', r"\bur[ée]e\b"),
 ('Bilan hépatique', 'BIO', r"bilan h[ée]patique|transaminases|\bALAT\b|\bASAT\b|\bGGT\b|gamma-?GT|bilirubin|phosphatases? alcalines?"),
 ('Glycémie', 'BIO', r"glyc[ée]mie|glucose plasmatique|glucom[èe]tre"),
 ('HbA1c', 'BIO', r"HbA1c|h[ée]moglobine glyqu[ée]e"),
 ('TSH', 'BIO', r"\bTSH\b|thyr[ée]ostimuline"),
 ('T4 / T3 libres', 'BIO', r"\b[fF]?T4L?\b|\bT4 libre|\bT3L?\b|\bT3 libre|thyroxine libre"),
 ('Anticorps anti-récepteur TSH (TRAb)', 'BIO', r"TRAb|(?:anticorps )?anti-?r[ée]cepteurs? de la TSH|anticorps (?:dirig[ée]s contre le |du )r[ée]cepteur de la TSH|\bTSI\b"),
 ('Thyroglobuline', 'BIO', r'(?<!anti-)thyroglobulin'),
    ('Anti-TPO', 'BIO', r"anti-?TPO|anti-?thyroperoxydase"),
 ('Troponine', 'BIO', r"troponine|\bhs-?cTn|\bcTn[IT]?\b"),
 ('BNP / NT-proBNP', 'BIO', r"NT-?pro-?BNP|\bBNP\b"),
 ('D-dimères', 'BIO', r"D-?dim[èe]res"),
 ('Gaz du sang', 'BIO', r"gaz du sang|gazom[ée]trie|\bGDS\b"),
 ('Lactate', 'BIO', r"lactat[ée]mie|\blactates?\b"),
 ('Hémocultures', 'BIO', r"h[ée]mocultures?"),
 ('ECBU / analyse d’urine', 'BIO', r"\bECBU\b|examen cytobact[ée]riologique des urines|bandelette urinaire|s[ée]diment urinaire|uroculture"),
 ('Ponction lombaire / LCR', 'BIO', r"ponction lombaire|\bLCR\b|liquide c[ée]phalo-?rachidien"),
 ('Sérologies', 'BIO', r"s[ée]rologies?"),
 ('Test VIH (Ag/Ac 4e génération)', 'BIO', r"test (?:de d[ée]pistage )?(?:du )?VIH|\bAg/Ac\b|4e g[ée]n[ée]ration|test combin[ée]"),
 ('Charge virale', 'BIO', r"charge virale|ARN VIH|ARN viral"),
 ('Lymphocytes CD4', 'BIO', r"\bCD4\b"),
 ('IGRA / test tuberculinique', 'BIO', r"\bIGRA\b|QuantiFERON|T-?SPOT|test tuberculinique|intradermor[ée]action|\bIDR\b|Mantoux"),
 ('Examen microbiologique des expectorations (BAAR, culture, PCR mycobactéries)', 'BIO', r"\bBAAR\b|Ziehl|expectorations?|crachats|tubage gastrique|Xpert|GeneXpert"),
 ('PCR (amplification génique)', 'BIO', r"\bPCR\b|amplification (?:g[ée]nique|des acides nucl)"),
 ('Bilan lipidique', 'BIO', r"bilan lipidique|\bLDL\b|cholest[ée]rol|triglyc[ée]rides"),
 ('Coagulation (TP/INR/TCA/fibrinogène)', 'BIO', r"\bINR\b|\bTP\b|\bTCA\b|\baPTT\b|\bTTPa\b|fibrinog[èe]ne|taux de prothrombine|crase"),
 ('Ferritine / bilan martial', 'BIO', r"ferritin|bilan martial|fer s[ée]rique|transferrine"),
 ('LDH', 'BIO', r"\bLDH\b|lactate d[ée]shydrog[ée]nase"),
 ('Électrophorèse des protéines', 'BIO', r"[ée]lectrophor[èe]se"),
 ('Métanéphrines', 'BIO', r"m[ée]tan[ée]phrines?|normétanéphrine|catécholamines? (?:plasmatiques|urinaires)"),
 ('Chromogranine A', 'BIO', r"chromogranine"),
 ('5-HIAA', 'BIO', r"5-?HIAA|acide 5-hydroxy"),
 ('Tryptase', 'BIO', r"tryptase"),
 ('Cortisol / test de freinage', 'BIO', r"cortisol|test de freinage|freinage (?:minute|faible|fort)"),
 ('FSH / LH / œstradiol', 'BIO', r"\bFSH\b|\bLH\b|[œoe]stradiol"),
 ('hCG (test de grossesse)', 'BIO', r"\bhCG\b|β-?hCG|test de grossesse"),
 ('Prolactine', 'BIO', r"prolactin"),
 ('Vitamine B12 / folates', 'BIO', r"vitamine B12|cobalamine|folates?"),
 ('CK', 'BIO', r"\bCK\b|cr[ée]atine kinase|\bCPK\b"),
 ('Toxicologie / dosage médicamenteux', 'BIO', r"toxicolog|dosage (?:plasmatique|m[ée]dicamenteux)|alcool[ée]mie|[ée]thanol[ée]mie"),
 ('Frottis sanguin', 'BIO', r"frottis sanguin|goutte [ée]paisse|frottis-goutte"),
 ('Cytométrie en flux', 'BIO', r"cytom[ée]trie"),
 ('Peptide C / insuline', 'BIO', r"peptide C|insulin[ée]mie|pro-?insuline"),
 ('Bilan phosphocalcique / PTH', 'BIO', r"\bPTH\b|parathormone|phosphat[ée]mie"),
 # fonctionnels
 ('ECG', 'FONC', r"\bECG\b|[ée]lectrocardiogramme"),
 ('Holter (ECG / tensionnel)', 'FONC', r"\bHolter\b"),
 ('MAPA / mesure ambulatoire PA', 'FONC', r"\bMAPA\b|mesure ambulatoire de la pression"),
 ('Épreuve d’effort', 'FONC', r"[ée]preuve d['’]effort|ergom[ée]trie|test d['’]effort"),
 ('Spirométrie', 'FONC', r"spirom[ée]trie|\bVEMS\b"),
 ('Pléthysmographie', 'FONC', r"pl[ée]thysmographie"),
 ('DLCO', 'FONC', r"\bDLCO\b|capacit[ée] de diffusion"),
 ('Oxymétrie / saturation', 'FONC', r"oxym[ée]trie|\bSpO[2₂]"),
 ('EEG', 'FONC', r"\bEEG\b|[ée]lectroenc[ée]phalogra"),
 ('EMG / ENMG', 'FONC', r"\bE?N?MG\b|[ée]lectromyogra|[ée]lectroneuromyogra"),
 ('Polysomnographie / polygraphie', 'FONC', r"polysomnograph|polygraphie (?:ventilatoire|respiratoire)"),
 ('Test de Minor (iode-amidon)', 'FONC', r"\bMinor\b|iode[- ]amidon|amidon iod[ée]"),
 ('Gravimétrie sudorale', 'FONC', r"gravim[ée]tri"),
 ('Test sudoral thermorégulateur / QSART', 'FONC', r"\bQSART\b|test (?:de )?sudo|thermor[ée]gulat\w* sudoral|sudoscan"),
 ('Tests autonomiques (tilt-test, Ewing)', 'FONC', r"tilt-?test|table bascul|tests? (?:du syst[èe]me )?autonom"),
 # imagerie
 ('Radiographie', 'IMG', r"radiograph|\bRx\b|clich[ée]s? (?:du )?thora|radiologie"),
 ('Échographie (générique)', 'IMG', r"[ée]chograph(?!ie (?:cardiaque|thyro|abdom|cervic|ganglion|transthor|trans-?thor|transœso|pelv|endo))|ultrason"),
 ('Échographie cervicale / thyroïdienne', 'IMG', r"[ée]chographie (?:cervicale|thyro|du cou|de la thyro)"),
 ('Échographie ganglionnaire', 'IMG', r"[ée]chographie ganglion"),
 ('Échocardiographie (ETT/ETO)', 'IMG', r"[ée]chocardiograph|\bETT\b|\bETO\b|[ée]chographie (?:cardiaque|transthor|trans-?thor|transœso)"),
 ('Échographie abdominale / pelvienne', 'IMG', r"[ée]chographie (?:abdom|pelv|endo)"),
 ('Scanner / TDM', 'IMG', r"scanner|\bTDM\b|tomodensitom|\bCT\b(?!-)|angio-?CT|coroscanner"),
 ('IRM', 'IMG', r"\bIRM\b|r[ée]sonance magn[ée]tique"),
 ('TEP / PET-scan', 'IMG', r"\bTEP\b|\bPET\b|PET-?(?:CT|scan)|TEP-?(?:TDM|scan)|tomographie par [ée]mission"),
 ('Scintigraphie (thyroïde, MIBG, DOTATATE…)', 'IMG', r"scintigraph|\bMIBG\b|DOTATATE|\bSPECT\b|octréoscan"),
 ('Coronarographie / angiographie', 'IMG', r"coronarograph|angiograph|art[ée]riograph|phl[ée]bograph"),
 ('Doppler', 'IMG', r"doppler|[ée]cho-?doppler"),
 ('Mammographie', 'IMG', r"mammograph"),
 ('Ostéodensitométrie', 'IMG', r"ost[ée]odensitom|\bDXA\b|absorptiom"),
 # autres
 ('Biopsie / histologie', 'AUTRE', r"biops|histolog|anatomopatholog|cytoponction|ponction[- ]biopsie|exérèse ganglionnaire"),
 ('Endoscopie (FOGD, coloscopie, bronchoscopie)', 'AUTRE', r"endoscop|fibroscop|gastroscop|coloscop|bronchoscop|\bLBA\b|lavage broncho"),
 ('Myélogramme / biopsie ostéomédullaire', 'AUTRE', r"my[ée]logramme|biopsie ost[ée]o-?m[ée]dullaire|moelle osseuse"),
 ('Tests génétiques', 'AUTRE', r"test g[ée]n[ée]tique|analyse g[ée]n[ée]tique|g[ée]notypage|s[ée]quen[cç]age"),
]
from lex_extra import LEX_EXTRA
LEX = LEX_EXTRA + LEX
# compilation insensible à la casse ; un sigle court (≤ 6 car.) trouvé en minuscules est rejeté (ex. « tp », « vs »).
COMP = [(n, c, re.compile(r, re.I)) for n, c, r in LEX]

def _ok(g):
    if len(g) > 6: return True
    up = sum(ch.isupper() for ch in g); lo = sum(ch.islower() for ch in g)
    return up >= lo

def find(text):
    out = []
    for n, c, rx in COMP:
        for m in rx.finditer(text):
            if m.start() > 0 and text[m.start() - 1].isalpha():
                continue   # milieu de mot (« hypoglycémie » ne contient pas l’examen « glycémie »)
            if _ok(m.group(0)):
                out.append((m.start(), m.end(), n, c, m.group(0)))
    out.sort()
    # supprime les chevauchements (le plus long l'emporte)
    res, last = [], -1
    for o in sorted(out, key=lambda x: (x[0], -(x[1] - x[0]))):
        if o[0] >= last:
            # « thyréostimuline (TSH) » : même examen à ≤ 3 caractères → une seule mention
            if res and res[-1][2] == o[2] and o[0] - res[-1][1] <= 3:
                res[-1] = (res[-1][0], o[1], o[2], o[3], res[-1][4]); last = o[1]; continue
            res.append(o); last = o[1]
    return res

def analyse(lot):
    d = json.load(open(work(lot, 'decoupe.json')))
    W = d['windows']
    per_course, distinct = {}, {}
    for c in d['courses']:
        st = {'occ': 0, 'clickable': 0, 'two_tabs': 0, 'by_cat': {}, 'by_point': {}, 'examples_non_click': []}
        for b in c['blocks']:
            if b.get('point') == 'sources':
                continue
            for (a, e, n, cat, g) in find(b['text']):
                st['occ'] += 1
                st['by_cat'][cat] = st['by_cat'].get(cat, 0) + 1
                pt = str(b.get('point'))
                st['by_point'][pt] = st['by_point'].get(pt, 0) + 1
                win = None; click = False
                for (sa, se, wid, kind) in b['spans']:
                    if sa <= a and e <= se:
                        click = True; win = wid; break
                tabs = bool(win and W.get(win, {}).get('tab_principe') and W[win].get('tab_interpretation'))
                st['clickable'] += click; st['two_tabs'] += tabs
                x = distinct.setdefault(n, {'cat': cat, 'occ': 0, 'clickable': 0, 'two_tabs': 0, 'courses': set(), 'forms': set()})
                x['occ'] += 1; x['clickable'] += click; x['two_tabs'] += tabs; x['courses'].add(c['id']); x['forms'].add(g)
                if not click and len(st['examples_non_click']) < 5:
                    st['examples_non_click'].append(f"[{c['id']} pt {pt}] …{b['text'][max(0,a-50):e+40]}…")
        per_course[c['id']] = st
    for x in distinct.values():
        x['courses'] = sorted(x['courses']); x['forms'] = sorted(x['forms'])[:6]
        x['besoin_fenetre'] = x['two_tabs'] < x['occ']
    return {'lot': lot, 'per_course': per_course, 'distinct': distinct,
            'n_windows_with_2_tabs': sum(1 for w in W.values() if w['tab_principe'] and w['tab_interpretation'])}

if __name__ == '__main__':
    lot = sys.argv[1]
    r = analyse(lot)
    json.dump(r, open(work(lot, 'examens.json'), 'w'), ensure_ascii=False, indent=1)
    T = [0, 0, 0]
    for cid, s in r['per_course'].items():
        T[0] += s['occ']; T[1] += s['clickable']; T[2] += s['two_tabs']
        print(f"{cid:<14} occ={s['occ']:>4} cliquables={s['clickable']:>4} 2onglets={s['two_tabs']:>3}  {s['by_cat']}")
    print('TOTAL', T, 'examens distincts:', len(r['distinct']), 'fenêtres à 2 onglets:', r['n_windows_with_2_tabs'])
