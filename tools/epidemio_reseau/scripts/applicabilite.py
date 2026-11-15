"""Applicabilité d'un paramètre biostatistique par DX (A/B/C/N), règles déterministes + score de confiance.
A : applicable, source suisse probable ; B : applicable, seulement hors Suisse ; C : peu ou pas applicable ; N : sans nom (Phase A).
Recherche seule : aucune injection, aucun push."""
import json, os, re, sys, sqlite3, collections
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from regles import norm, apparier
RAC = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# --- N : nom absent ou invalide (fragment d'extraction) ---
NOM_INVALIDE = re.compile(r'^\(.*\)$|^\W*$|^(et|a|à|de|ou)\s+dx\b|^\d+$|^[\W\d]{0,3}$|donnee non trouvee')

# --- C : rubriques, gestes, décisions, notions transversales, symptômes isolés ---
C_RUBRIQUE = re.compile(
 r'^(bilan|demarche|examens?\b|imagerie|irm\b|scanner|dosage|perfusion|prophylaxie|antibiotique sur|neuroleptique poursuivi|oxygene pour|check-?up|'
 r'mammographie|antigene prostatique|decision partagee|depistage|calendrier|rattrapage|vaccinations?\b|readaptation|neuromodulation|prise en charge|'
 r'suivi\b|orientation|consultation|certificat|representant|mineur capable|personne incapable|refus d|surconsommation|antagonisme|diagnostic organique|'
 r'risque absolu|pression arterielle$|resultat biologique|reaction au produit|patient (stable|instable)|situation\b|personnel de sante|grossesse et protection|'
 r'plaie et effet|demande|organisation|choix|strategie|indication|contre-indication|annonce|information|consentement|ordonnance|prescription|'
 r'transmission|coordination|communication|evaluation|triage|tri\b|surveillance|education|conseil|entretien|traitement|therapie|medicaments?$|'
 r'signe d.alarme|logopedie|recuperation$|necrose$|oubli$|contention|forme persistante|contexte de|sterilet|pertes physiologiques|virage|'
 r'crise d.un|fugue|peur (focale|apres)|dysbiose$|(homme|femme) jeune|(pustule|papule|plaque prurigineuse|macule)$|lesion veineuse associee|conduite a tenir|'
 r'intervention|geste|technique|procedure|protocole|equipe|reseau|filiere|parcours|role|place de|ivresse ou etat|trouble psychique$|'
 r'causes? (endocriniennes|organiques|psychiques)$|forme fonctionnelle$|menace cardiovasculaire$|fuite de gaz$|perte de selles$|sphincter interne faible$|'
 r'situation refractaire|examens sans benefice|imagerie et radioprotection|nodule pulmonaire decouvert|risque cardiovasculaire, lipides)')
C_TRANSVERSAL = re.compile(r'categorie diagnostique|toutes causes|catégorie cim|categorie cim|\(comorbidite\)|composante psychique|pathologie somatique claire|'
                           r'problemes? (musculo|lies aux medicaments)|maladie somatique grave|cause de (fuo|douleur)|plusieurs causes|origine mixte|'
                           r'antecedent de|chez l.asymptomatique|a bas risque$|^\w+ (stable|instable)$')
SYMPTOME = re.compile(r'^(douleur|prurit|fievre|toux|dyspnee|crampes?|agitation|presyncope|tremblement|fatigue|nausees?|vomissements?|vertiges?|'
                      r'cephalees?|rectorragie|melena|hematemese|saignement|oedeme|prise de poids|perte de poids|anorexie|xerostomie|flush|polydipsie|'
                      r'somnolence|ronflement|dysphonie|diarrhee|constipation|transit|protrusion|ecoulement|epistaxis|hemoptysie|palpitations?|'
                      r'malaise|syncope|chute|confusion|insomnie|hoquet|ballonnement|eructation|halitose|acouphenes?|hyperhidrose secondaire|'
                      r'sueurs?|bouffees|frissons|asthenie|amaigrissement|dysurie|pollakiurie|hematurie|proteinurie|globe vesical|myokymie)')
MARQUEUR_MALADIE = re.compile(r'(ite\b|ites\b|ose\b|oses\b|syndrome|maladie|cancer|carcinome|tumeur|infection|insuffisance|fracture|luxation|ulcere|'
                              r'lesion|hernie|kyste|polype|stenose|paralysie|thrombose|embolie|dissection|anevrisme|deficit|carence|intoxication|'
                              r'allergi|anemie|leucemie|lymphome|myelome|diabete|hypertension|epilepsie|migraine|demence|depress|anxi|psychose|'
                              r'addiction|dependance|trouble|dystrophie|dysplasie|malformation|atresie|agenesie|fistule|hemorragie|hematome|'
                              r'infarctus|ischemie|hypo|hyper|apnee|reflux|incontinence|prolapsus|endometri|grossesse|accouchement)')
SYMPT_QUALIF = re.compile(r'(medicamenteu|fonctionnel|psychogene|d.origine|lie[e]? a|essentiel|chronique|aigu|iatrogene|post-|primaire|nocturne)')

# --- A : source suisse probable (au-delà des règles de regles.py) ---
A_MOTIFS = [
 (r'suicid|autodommag|automutilation|autoagressi', 'OFS causes de décès (suicide, suicide assisté) ; Obsan'),
 (r'homicide|violence (domestique|dans le couple)|maltraitance|abus sexuels|harcelement|cyberharcelement|crimes? de haine|discrimination',
  'OFS statistique policière de la criminalité ; enquêtes suisses (Obsan, HBSC, Optimus)'),
 (r'deces (inattendu|de nature indeterminee|en lien)|mort subite du nourrisson|mortalite infantile|deces non naturel', 'OFS causes de décès'),
 (r'interruption (volontaire )?de grossesse|\bivg\b|avortement', 'OFS statistique des interruptions de grossesse'),
 (r'premature|prematurite|cesarienne|grossesse extra|fausse couche|\bnaissances?\b|accouchement|diabete gestationnel|pre-?eclampsie|mortinaissance',
  'OFS statistique des naissances et des hôpitaux'),
 (r'chute|fracture du col du femur|fracture (de la hanche|du poignet|vertebrale)|osteoporo', 'Obsan/ESS (chutes, ostéoporose) ; OFS hôpitaux ; BPA'),
 (r'infarctus|syndrome coronarien|avc|accident vasculaire|insuffisance cardiaque|fibrillation auriculaire|cardiopathie|arret cardiaque',
  'OFS causes de décès et hôpitaux ; registres AMIS Plus, Swiss Stroke Registry'),
 (r'accident(?! vasculaire| ischemique)|traumatism|noyade|brulure|engelure|gelure|morsure|piqure|intoxication|empoisonnement', 'BPA, statistique LAA, Tox Info Suisse, OFS'),
 (r'abus d|mesusage|alcool|tabag|tabac|nicotin|cannabis|opioide|cocaine|stupefiant|substance|addiction|jeux? (d.argent|pathologique)|dependance',
  'MonAM / Addiction Suisse / ESS'),
 (r'(?<!immuno)depress|anxi|trouble bipolaire|schizophren|psychose|burn-?out|epuisement|trouble (du comportement alimentaire|de stress)|anorexie mentale|boulimie|'
  r'tdah|deficit de l.attention|autis|demence|alzheimer|detresse psychique|insomnie|troubles? du sommeil|douleur chronique$|douleurs? chroniques?\b', 'Obsan (santé psychique), ESS, statistique psychiatrique'),
 (r'obesit|surpoids|diabete(?! insipide)|prediabete|hypertension arterielle|hypercholesterol|dyslipidemi|cholesterol', 'MonAM / ESS'),
 (r'asthme|bpco|bronchopneumopathie chronique|allergi|rhinite allergique|eczema atopique|dermatite atopique|urticaire', 'MonAM / ESS / SAPALDIA'),
 (r'arthrose|lombalgie|dorsalgie|mal de dos|polyarthrite rhumatoide|rhumatism', 'ESS (maladies chroniques, douleurs) ; Obsan'),
 (r'insuffisance renale|maladie renale chronique|dialyse|greffe|transplant', 'Registres suisses (SRRQAP, Swisstransplant, STCS)'),
 (r'escarre|lesion de pression|lesions? des tissus profonds|dermite associee a l.incontinence', 'ANQ – mesure nationale de prévalence (escarres)'),
 (r'infection (nosocomiale|du site operatoire|associee aux soins)|resistan', 'Swissnoso, anresis'),
 (r'vaccin|couverture vaccinale|statut (vaccinal|inconnu)', 'OFSP – couverture vaccinale'),
 (r'cancer|carcinome|tumeur maligne|lymphome|leucemie|myelome|sarcome|melanome|retinoblastome|neuroblastome|nephroblastome|glioblastome|gliome',
  'Registres des tumeurs (ONEC, RCdE), OFS'),
 (r'surdite|presbyacousie|deficience visuelle|cecite|cataracte|glaucome|degenerescence maculaire', 'ESS (limitations), OFS'),
 (r'incontinence urinaire|incontinence fecale', 'ESS (incontinence) ; études suisses'),
 (r'pneumonie|bronchiolite|infection (respiratoire|des voies respiratoires)|grippe|covid|gastro-?enterite', 'OFSP Sentinella, IDD, OFS hôpitaux'),
 (r'sclerose en plaques|parkinson|epilepsie|migraine', 'Registres et cohortes suisses (Swiss MS Registry), ESS'),
 (r'handicap|invalidite|limitations? fonctionnelles|readaptation', 'OFS (handicap), AI'),
]
A_COMP = [(re.compile(m), s) for m, s in A_MOTIFS]
RARE = re.compile(r'(syndrome de [a-z]|maladie de [a-z]|congenital|genetique|familial|hereditaire|monogenique|syndromique|dystrophie|atresie|'
                  r'agenesie|microcephalie|craniostenose|lie a [a-z0-9]{2,6}\b|deficit en|mucopolysacchar|lysosomal|mitochondri|rare|'
                  r'juvenile|du nourrisson|neonatal|idiopathique|amylose|vascularite|porphyrie|histiocyt|mastocyt)')
ENTITE_Q = re.compile(r'(essentiel\b|de tension|positionnel|paroxysti|vasovagal|reflexe|de holmes|cerebelleux|chronique fonctionnel|primaire|'
                      r'diverticulaire|\bfuo\b|sans cause retrouvee|menopause|rythmique|convulsivante)')
NETTOYAGE = re.compile(r'\s*(donnee|donnée) non trouvee? dans les sources consultees?.*$|\s*\[S\d+\]', re.I)
CLES_CH = ('can:', 'idd:', 'cod:', 'obs:')

def classer(nom, statut_dx='', verifie_ch=False):
    """Retourne (classe, motif, confiance)."""
    nom = re.sub(r'\s*donnée non trouvée dans les sources consultées.*$|\s*\[S\d+\]', '', nom or '')
    n = norm(nom).strip()
    if not n or NOM_INVALIDE.search(n) or len(re.sub(r'[^a-z]', '', n)) < 4:
        return 'N', 'DX sans nom exploitable : en attente de la Phase A', 1.0
    if verifie_ch:
        return 'A', 'paramètre suisse déjà vérifié dans le réseau', 1.0
    m = apparier(nom)
    ex_ch = [k for k, t in m if t == 'exact' and k.startswith(CLES_CH)]
    if ex_ch:
        return 'A', f'indicateur suisse exact connu ({", ".join(ex_ch[:2])})', 0.95
    if C_RUBRIQUE.search(n):
        return 'C', 'rubrique, geste, décision ou organisation des soins (pas une entité morbide)', 0.85
    if C_TRANSVERSAL.search(n):
        return 'C', 'notion transversale ou catégorie hétérogène (dénominateur non définissable)', 0.8
    for rx, src in A_COMP:
        if rx.search(n):
            return 'A', f'thème couvert par une source suisse : {src}', 0.75
    ex_ms = [k for k, t in m if t == 'exact']
    if ex_ms:
        return 'A', f'groupe exact de la statistique médicale des hôpitaux OFS ({ex_ms[0]})', 0.7
    if SYMPTOME.search(n) and ENTITE_Q.search(n):
        return 'B', 'symptôme érigé en entité nosologique précise : études hors Suisse', 0.6
    if SYMPTOME.search(n) and not MARQUEUR_MALADIE.search(re.sub(r'^\S+\s?', '', n) if SYMPTOME.match(n) else n):
        return 'C', 'symptôme ou signe isolé (fréquence dépendante du contexte de consultation)', 0.7
    if any(k.startswith(CLES_CH) for k, t in m):
        return 'A', f'indicateur suisse de groupe ({[k for k, t in m if k.startswith(CLES_CH)][0]}) : valeur spécifique à rechercher', 0.6
    if RARE.search(n):
        return 'B', 'entité rare ou syndromique : pistes Orphanet, ECDC, GBD, études', 0.7
    if m:
        return 'B', f'seul un groupe hospitalier OFS large existe ({m[0][0]}) : valeur spécifique hors Suisse (études, GBD)', 0.55
    return 'B', 'entité clinique précise sans indicateur suisse connu : études ou GBD hors Suisse', 0.5

# ---------------------------------------------------------------- exécution réseau
AJOUTS = {  # valeurs vérifiées hors pipeline, injectées sur main (source primaire, contexte complet)
 (4, 1): ('PR #743', 'CH'), (4, 8): ('PR #743', 'hors CH (UE + CH)'), (218, 2): ('PR #743', 'CH'),
 (1, 8): ('PR #742', 'CH'), (6, 7): ('PR #742', 'CH'), (30, 7): ('PR #742', 'hors CH'), (32, 1): ('PR #742', 'hors CH'), (32, 8): ('PR #742', 'hors CH'),
}

NOMS_CONNUS = {(218, 2): 'Infection VIH chez les hommes ayant des rapports sexuels avec des hommes (HSH)'}  # nom repris de la box PR #743

def executer():
    import csv
    from noyau import db, SORTIE
    c = db()
    R = sorted((json.loads(r[0]) for r in c.execute('SELECT json FROM resultats')), key=lambda x: (x['lot'], x['dx']))
    c.execute('CREATE TABLE IF NOT EXISTS applicabilite(lot INT, dx INT, diagnostic TEXT, classe TEXT, motif TEXT, confiance REAL, verifie INT, source_verif TEXT, PRIMARY KEY(lot,dx))')
    out = []
    for r in R:
        v_pipe = any(p['statut'] == 'vérifié' for p in r['params'])
        aj = AJOUTS.get((r['lot'], r['dx']))
        r['diagnostic'] = r['diagnostic'] or NOMS_CONNUS.get((r['lot'], r['dx']), '')
        k, mo, conf = classer(r['diagnostic'], r['statut_dx'], v_pipe or (aj and aj[1] == 'CH'))
        ver = bool(v_pipe or aj)
        src = 'réseau (pipeline)' if v_pipe else (f'{aj[0]} ({aj[1]})' if aj else '')
        partiel = any(p['statut'].startswith('partiel') for p in r['params'])
        out.append(dict(lot=r['lot'], dx=r['dx'], diagnostic=r['diagnostic'] or '', classe=k, motif=mo, confiance=conf, verifie=ver, source_verif=src, partiel=partiel))
        c.execute('INSERT OR REPLACE INTO applicabilite VALUES(?,?,?,?,?,?,?,?)', (r['lot'], r['dx'], r['diagnostic'], k, mo, conf, int(ver), src))
    c.execute("INSERT OR REPLACE INTO checkpoint VALUES('applicabilite','fait',datetime('now','localtime'))"); c.commit()
    json.dump(out, open(f'{SORTIE}/out/APPLICABILITE.json', 'w'), ensure_ascii=False, indent=0)
    with open(f'{SORTIE}/out/APPLICABILITE.csv', 'w', newline='', encoding='utf-8-sig') as f:
        w = csv.DictWriter(f, fieldnames=list(out[0]), delimiter=';'); w.writeheader(); w.writerows(out)
    return out

if __name__ == '__main__':
    o = executer(); print(collections.Counter(x['classe'] for x in o), sum(x['verifie'] for x in o))
