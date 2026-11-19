"""Eurostat – EHIS vague 3 (hlth_ehis_cd1e, 2019) : prévalence déclarée des maladies chroniques, UE-27 (colonne Europe).
Appariement DX → maladie seulement quand elles correspondent. Idempotent, max. 3 valeurs par niveau."""
import os, sys, re, json, urllib.parse
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from noyau import db, fetch, maintenant, journal
from regles import norm
from recherche import conforme, initialiser
API = 'https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/hlth_ehis_cd1e'
CARTE = [
 (r'arthrose', 'ARTHRO', 'arthrose'),
 (r'^lombalgie|douleurs? dorsales?|^dorsalgie', 'LW_CHR_BACK', 'lombalgie ou autre affection chronique du dos'),
 (r'^cervicalgie', 'NECK', 'cervicalgie ou autre affection chronique du cou'),
 (r'^asthme', 'ASTHMA', 'asthme (y compris allergique)'),
 (r'\bbpco\b|bronchopneumopathie chronique obstructive|^bronchite chronique|emphyseme', 'CHR_LW_RES', 'bronchite chronique, BPCO ou emphysème'),
 (r'^infarctus (aigu )?du myocarde', 'HRT_CHR_ATK', 'infarctus du myocarde ou ses séquelles chroniques'),
 (r'^cardiopathie ischemique|^maladie coronarienne|^angor stable|^syndrome coronarien chronique', 'CHRT_ANGPEC', 'maladie coronarienne ou angine de poitrine'),
 (r'^hypertension arterielle(?! (pulmonaire|gravidique))|^hta\b|^hypertension (essentielle|primaire)', 'HBLPR', 'hypertension artérielle'),
 (r'dyslipidemie|hypercholesterolemie|hyperlipidemie', 'HBLLIP', 'taux élevé de lipides sanguins'),
 (r'^accident vasculaire cerebral|^avc\b', 'STRK_CHR', 'accident vasculaire cérébral ou ses séquelles chroniques'),
 (r'^cirrhose', 'CIRRHOSIS', 'cirrhose du foie'),
 (r'^incontinence urinaire', 'URIN', 'incontinence urinaire'),
 (r'^(maladie|insuffisance) renale chronique', 'KIDNEY', 'problèmes rénaux'),
 (r'^diabete(?! (insipide|gestationnel))|^diabete de type|^diabete sucre', 'DIAB', 'diabète'),
 (r'^rhinite allergique|^conjonctivite allergique|^allergie', 'ALLGY', 'allergie (rhinite, conjonctivite, dermatite, allergie alimentaire…, hors asthme allergique)'),
 (r'^depression(?! (de la commande|respiratoire))|^episode depressif|^trouble depressif', 'DPR_CHR', 'dépression chronique'),
]

def apparier(nom):
    n = norm(nom or '')
    for m, code, lib in CARTE:
        if re.search(m, n): return code, lib
    return None

def valeur(code):
    u = f'{API}?' + urllib.parse.urlencode([('geo', 'EU27_2020'), ('sex', 'T'), ('age', 'TOTAL'), ('isced11', 'TOTAL'), ('unit', 'PC'), ('hlth_pb', code), ('time', '2019'), ('lang', 'EN')])
    t, sha, *_ = fetch(u)
    if not t: return None
    v = json.loads(t).get('value', {}).get('0')
    return (v, u, sha) if v is not None else None

def executer():
    c = db(); initialiser(c); n = 0; cache = {}
    for lot, dx, dg, pe in c.execute('SELECT lot,dx,diagnostic,params_eu FROM taches').fetchall():
        a = apparier(dg)
        if not a: continue
        code, lib = a
        if code not in cache: cache[code] = valeur(code)
        if not cache[code]: continue
        v, u, sha = cache[code]; vt = f'{v}'.replace('.', ',')
        p = dict(cle=f'eurostat:hlth_ehis_cd1e:{code}:EU27_2020', source='Eurostat – EHIS vague 3 (hlth_ehis_cd1e)', valeur_txt=vt, unite='% des personnes de 15 ans et plus',
                 population='personnes de 15 ans et plus vivant en ménage privé, 27 États membres de l’UE', age_sexe='15 ans et plus ; deux sexes',
                 definition=f'maladie chronique déclarée au cours des 12 derniers mois : {lib}', mesure='prévalence déclarée sur 12 mois (enquête 2019)', annee='2019',
                 territoire='Union européenne (UE-27)', type_source='enquête européenne par interview sur la santé (EHIS), autodéclaration', url=u,
                 preuve=f'hlth_ehis_cd1e : hlth_pb={code}, geo=EU27_2020, sex=T, age=TOTAL, isced11=TOTAL, unit=PC, time=2019, value={v}', sha256=sha, hors_ch=1, statut='vérifié')
        p['phrase'] = f'En 2019, {vt} % des personnes de 15 ans et plus de l’UE-27 déclaraient : {lib} (enquête EHIS).'
        if conforme(p, 'eu'): continue
        P = [q for q in json.loads(pe) if q.get('statut') == 'vérifié' and q.get('cle') != p['cle']]
        if len(P) >= 3: continue
        c.execute("UPDATE taches SET statut_eu='vérifié', params_eu=?, date=?, agent=COALESCE(NULLIF(agent,''),'eurostat') WHERE lot=? AND dx=?",
                  (json.dumps(P + [p], ensure_ascii=False), maintenant(), lot, dx)); n += 1
        c.commit()
    journal(f'eurostat_ehis : {n} valeurs Europe'); print(n); return n

if __name__ == '__main__':
    executer()
