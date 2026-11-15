"""Eurostat – causes de décès (hlth_cd_asdr2) : taux de mortalité standardisé, UE-27 (colonne Europe) et Suisse (colonne Suisse),
même définition CIM-10 des deux côtés. Appariement DX → cause seulement quand la cause correspond à la maladie nommée.
Idempotent : ajoute la valeur aux tâches (max. 3 valeurs par niveau), ne remplace jamais une valeur déjà vérifiée par une autre source."""
import os, sys, re, json, urllib.parse
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from noyau import db, fetch, maintenant, journal
from regles import norm
from recherche import conforme, initialiser

API = 'https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/hlth_cd_asdr2'
K = r'(cancer|carcinome|adenocarcinome|tumeur maligne|neoplasie maligne|neoplasme malin)'
# (motif sur le nom normalisé, code Eurostat, libellé FR de la définition, sexe)
CARTE = [
 (r'tuberculose', 'A15-A19_B90', 'tuberculose (A15–A19, B90)', 'T'),
 (r'hepatite (b|c)\b.*chronique|hepatite chronique (b|c)\b', 'B180-B182', 'hépatite virale chronique B ou C (B18.0–B18.2)', 'T'),
 (r'^hepatites? virale', 'B15-B19_B942', 'hépatites virales et séquelles (B15–B19, B94.2)', 'T'),
 (r'\bvih\b|\bsida\b', 'B20-B24', 'maladie due au VIH (B20–B24)', 'T'),
 (K + r'.*\bsein\b|\bsein\b.*' + K, 'C50', 'tumeur maligne du sein (C50)', 'F'),
 (K + r'.*(poumon|bronch|pulmonaire)', 'C33_C34', 'tumeur maligne de la trachée, des bronches et du poumon (C33–C34)', 'T'),
 (K + r'.*(colorectal|colon|rectum|rectal|anus|anal)', 'C18-C21', 'tumeur maligne du côlon, du rectum et de l’anus (C18–C21)', 'T'),
 (K + r'.*(estomac|gastrique)', 'C16', 'tumeur maligne de l’estomac (C16)', 'T'),
 (K + r'.*oesophag', 'C15', 'tumeur maligne de l’œsophage (C15)', 'T'),
 (r'hepatocarcinome|carcinome hepatocellulaire|' + K + r'.*(du foie|hepatique)', 'C22', 'tumeur maligne du foie et des voies biliaires intrahépatiques (C22)', 'T'),
 (K + r'.*pancrea', 'C25', 'tumeur maligne du pancréas (C25)', 'T'),
 (K + r'.*larynx', 'C32', 'tumeur maligne du larynx (C32)', 'T'),
 (r'melanome', 'C43', 'mélanome malin de la peau (C43)', 'T'),
 (K + r'.*col (de l.)?uter', 'C53', 'tumeur maligne du col de l’utérus (C53)', 'F'),
 (K + r'.*endometre', 'C54_C55', 'tumeur maligne du corps de l’utérus (C54–C55)', 'F'),
 (K + r'.*ovaire', 'C56', 'tumeur maligne de l’ovaire (C56)', 'F'),
 (K + r'.*prostat', 'C61', 'tumeur maligne de la prostate (C61)', 'M'),
 (K + r'.*\brein\b|carcinome renal', 'C64', 'tumeur maligne du rein (C64)', 'T'),
 (K + r'.*vessie', 'C67', 'tumeur maligne de la vessie (C67)', 'T'),
 (r'glioblastome|\bgliome|' + K + r'.*(cerveau|cerebral)', 'C70-C72', 'tumeur maligne du cerveau et du système nerveux central (C70–C72)', 'T'),
 (K + r'.*thyro', 'C73', 'tumeur maligne de la thyroïde (C73)', 'T'),
 (r'lymphome|hodgkin', 'C81-C86', 'maladie de Hodgkin et lymphomes (C81–C86)', 'T'),
 (r'leucemie', 'C91-C95', 'leucémies (C91–C95)', 'T'),
 (r'myelome', 'C88_C90_C96', 'myélome et autres tumeurs lymphoïdes (C88, C90, C96)', 'T'),
 (r'^diabete(?! (insipide|gestationnel))|diabete de type (1|2)|diabete sucre', 'E10-E14', 'diabète sucré (E10–E14)', 'T'),
 (r'alzheimer', 'G30', 'maladie d’Alzheimer (G30)', 'T'),
 (r'^demence|^trouble neurocognitif majeur', 'F01_F03', 'démences (F01, F03)', 'T'),
 (r'^maladie de parkinson|^parkinson\b', 'G20', 'maladie de Parkinson (G20)', 'T'),
 (r'alcoolisme|dependance (a l.)?alcool|trouble (lie a|de l.usage de) l.alcool|sevrage alcoolique', 'F10', 'troubles mentaux et du comportement liés à l’alcool (F10)', 'T'),
 (r'cardiopathie ischemique|maladie coronarienne|coronaropathie|angor stable', 'I20-I25', 'cardiopathies ischémiques (I20–I25)', 'T'),
 (r'infarctus (aigu )?du myocarde|syndrome coronarien aigu', 'I21_I22', 'infarctus aigu du myocarde, y compris récidive (I21–I22)', 'T'),
 (r'accident vasculaire cerebral|^avc\b|maladie cerebrovasculaire|infarctus cerebral|hemorragie (intracerebrale|intracranienne spontanee)', 'I60-I69', 'maladies cérébrovasculaires (I60–I69)', 'T'),
 (r'^grippe', 'J09-J11', 'grippe (J09–J11)', 'T'),
 (r'^pneumonie|^pneumopathie (communautaire|aigue|infectieuse)', 'J12-J18', 'pneumonie (J12–J18)', 'T'),
 (r'^asthme', 'J45_J46', 'asthme et état de mal asthmatique (J45–J46)', 'T'),
 (r'\bbpco\b|bronchopneumopathie chronique obstructive', 'J40-J44_J47', 'bronchite chronique, emphysème, BPCO et bronchectasies (J40–J44, J47)', 'T'),
 (r'ulcere (gastrique|duodenal|peptique|gastro-duodenal)', 'K25-K28', 'ulcère de l’estomac, du duodénum et du jéjunum (K25–K28)', 'T'),
 (r'^cirrhose|hepatopathie chronique|maladie chronique du foie', 'K70_K73_K74', 'maladie chronique du foie (K70, K73, K74)', 'T'),
 (r'mort subite du nourrisson', 'R95', 'syndrome de mort subite du nourrisson (R95)', 'T'),
 (r'^noyade|quasi-noyade', 'W65-W74', 'noyade et submersion accidentelles (W65–W74)', 'T'),
 (r'^suicide(?! assiste)|tentative de suicide|risque suicidaire|crise suicidaire|automutilation', 'X60-X84_Y870', 'lésions auto-infligées (suicide) (X60–X84, Y87.0)', 'T'),
 (r'^homicide', 'X85-Y09_Y871', 'agressions (homicide) (X85–Y09, Y87.1)', 'T'),
 (r'accident de la (route|circulation)', 'V_Y85', 'accidents de transport (V01–V99, Y85)', 'T'),
 (r'^covid', 'U071', 'COVID-19, virus identifié (U07.1)', 'T'),
]
SEXE = {'T': 'deux sexes', 'F': 'femmes', 'M': 'hommes'}

EXCLU = re.compile(r'^(dysphagie|camptocormie|polyneuropathie|ascite|aphasie|tachycardie|neuropathie|neoplasie \(|pheochromocytome)')
def apparier(nom):
    n = norm(nom or '')
    if EXCLU.search(n): return None          # complication ou entité différente : la mortalité de la maladie mère ne décrit pas ce DX
    for m, code, lib, sx in CARTE:
        if re.search(m, n):
            if code == 'C50' and re.search(r"chez l.homme", n): sx = 'M'
            return code, lib, sx
    return None

def valeurs(code, sx):
    u = f'{API}?' + urllib.parse.urlencode([('geo', 'EU27_2020'), ('geo', 'CH'), ('sex', sx), ('age', 'TOTAL'), ('unit', 'RT'), ('icd10', code), ('lang', 'EN')])
    t, sha, date, _ = fetch(u)
    if not t: return {}
    d = json.loads(t); dim = d['dimension']; gi = dim['geo']['category']['index']; ti = dim['time']['category']['index']
    nt = len(ti); out = {}
    for g, gidx in gi.items():
        ans = sorted(((y, d['value'].get(str(gidx * nt + i))) for y, i in ti.items()), reverse=True)
        y, v = next(((y, v) for y, v in ans if v is not None), (None, None))
        if v is not None: out[g] = (y, v, u, sha)
    return out

def param(code, lib, sx, g, y, v, u, sha):
    eu = g == 'EU27_2020'
    terr = 'Union européenne (UE-27)' if eu else 'Suisse'
    vt = f'{v:.2f}'.rstrip('0').rstrip('.').replace('.', ',')
    p = dict(cle=f'eurostat:hlth_cd_asdr2:{code}:{g}:{sx}', source='Eurostat – causes de décès (hlth_cd_asdr2)', valeur_txt=vt, unite='décès pour 100 000 habitants',
             population=f"population résidente {'des 27 États membres de l’UE' if eu else 'de Suisse'}", age_sexe=f'tous âges, standardisé sur la population type européenne 2013 ; {SEXE[sx]}',
             definition=f'décès dont la cause initiale est : {lib}', mesure=f'taux de mortalité standardisé selon l’âge, annuel ({y})', annee=y, territoire=terr,
             type_source='statistique officielle des causes de décès (certificats de décès), transmise à Eurostat', url=u,
             preuve=f'hlth_cd_asdr2 : icd10={code}, geo={g}, sex={sx}, age=TOTAL, unit=RT, time={y}, value={v}', sha256=sha, hors_ch=int(eu), statut='vérifié')
    p['phrase'] = f"En {y}, le taux de mortalité standardisé ({lib.split(' (')[0]}, {SEXE[sx]}) était de {vt} décès pour 100 000 habitants ({terr})."
    return p

def executer():
    c = db(); initialiser(c); n = {'eu': 0, 'ch': 0}; cache = {}
    for lot, dx, dg, pe, pc in c.execute('SELECT lot,dx,diagnostic,params_eu,params_ch FROM taches').fetchall():
        a = apparier(dg)
        if not a: continue
        code, lib, sx = a
        if (code, sx) not in cache: cache[(code, sx)] = valeurs(code, sx)
        V = cache[(code, sx)]
        for niv, g, old in (('eu', 'EU27_2020', pe), ('ch', 'CH', pc)):
            if g not in V: continue
            p = param(code, lib, sx, g, *V[g])
            if conforme(p, niv): continue
            P = [q for q in json.loads(old) if q.get('statut') == 'vérifié' and q.get('cle') != p['cle']]
            if len(P) >= 3: continue
            c.execute(f"UPDATE taches SET statut_{niv}='vérifié', params_{niv}=?, date=?, agent=COALESCE(NULLIF(agent,''),'eurostat') WHERE lot=? AND dx=?",
                      (json.dumps(P + [p], ensure_ascii=False), maintenant(), lot, dx)); n[niv] += 1
        c.commit()
    journal(f"eurostat_cod : {n['eu']} valeurs Europe, {n['ch']} valeurs Suisse"); print(n); return n

if __name__ == '__main__':
    executer()
