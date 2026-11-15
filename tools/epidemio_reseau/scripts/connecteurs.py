"""Connecteurs aux sources ouvertes suisses (données structurées d'abord). Chaque indicateur porte son contexte complet."""
import re, io, csv, html, json
from concurrent.futures import ThreadPoolExecutor
import openpyxl
from noyau import fetch, db, journal
from normaliseur import parse, _num

def fmt(x, dec=0):
    s = f'{x:,.{dec}f}'.replace(',', '\u202f').replace('.', ',')
    return s

def put(c, d):
    cols = ['cle','source','libelle','valeur','valeur_txt','unite','population','age_sexe','definition','mesure','annee',
            'territoire','type_source','url','preuve','sha256','phrase','hors_ch']
    d.setdefault('hors_ch', 0)
    c.execute(f'INSERT OR REPLACE INTO indicateurs({",".join(cols)}) VALUES({",".join("?"*len(cols))})', [d.get(k) for k in cols])

def texte(h):
    t = re.sub(r'<(script|style|svg)[^>]*>.*?</\1>', ' ', h, flags=re.S)
    return re.sub(r'\s+', ' ', html.unescape(re.sub(r'<[^>]+>', ' ', t))).strip()

# ---------- OFS – Statistique médicale des hôpitaux 2022 (XLSX, cellule) ----------
MS_PAGE = 'https://www.bfs.admin.ch/asset/fr/28625235'
MS_XLSX = 'https://dam-api.bfs.admin.ch/hub/api/dam/assets/28625235/master'
def ofs_ms(c):
    data, sha, d, f = fetch(MS_XLSX, binaire=True)
    wb = openpyxl.load_workbook(io.BytesIO(data), read_only=True)
    feuilles = {}
    for sh in ['Total', 'Femmes', 'Hommes']:
        for r in wb[sh].iter_rows(min_row=15, max_row=400, values_only=True):
            if r[0] and re.fullmatch(r'\d{3}', str(r[0]).strip()):
                tot = r[22] if len(r) > 22 else None
                feuilles.setdefault(str(r[0]).strip(), {'label': r[1]})[sh] = tot
    n = 0
    for code, v in feuilles.items():
        def num(x): return x if isinstance(x, (int, float)) else (0 if x in ('.', None) else None)
        t, fe, ho = num(v.get('Total')), num(v.get('Femmes')), num(v.get('Hommes'))
        sheet = 'Total'
        if t is None or t == 0:
            if fe and not ho: t, sheet = fe, 'Femmes'
            elif ho and not fe: t, sheet = ho, 'Hommes'
        if not t: continue
        lab = v['label'].strip()
        sexe = {'Total': f'tous âges ; deux sexes (femmes {fmt(fe or 0)}, hommes {fmt(ho or 0)})',
                'Femmes': 'tous âges ; femmes', 'Hommes': 'tous âges ; hommes'}[sheet]
        put(c, dict(cle=f'ms:{code}', source='OFS – Statistique médicale des hôpitaux (MS)', libelle=lab, valeur=t,
            valeur_txt=fmt(t), unite='cas hospitaliers/an',
            population='Cas d’hospitalisation (sorties) en hôpitaux suisses, soins aigus, réadaptation et psychiatrie',
            age_sexe=sexe,
            definition=f'Diagnostic principal codé CIM-10-GM appartenant au groupe {code} « {lab} » (liste OMS de mise en tableaux de la morbidité)',
            mesure='Nombre annuel de cas hospitaliers (séjours, pas personnes distinctes)', annee='2022',
            territoire='Suisse ; contexte hospitalier stationnaire', type_source='Relevé administratif exhaustif (OFS, MS)',
            url=MS_PAGE, preuve=f'XLSX je-f-14.04.01.02.01 2022, feuille {sheet}, ligne {code} « {lab} », colonne Total = {t}', sha256=sha,
            phrase=f'En 2022, les hôpitaux suisses ont enregistré {fmt(t)} cas d’hospitalisation dont le diagnostic principal relevait du groupe « {lab} » (CIM-10-GM), tous âges confondus ({sexe.split(" ; ")[1]}) ; il s’agit de séjours, non de patients distincts (OFS, Statistique médicale des hôpitaux).'))
        n += 1
    journal(f'OFS-MS 2022 : {n} groupes CIM-10 chargés (SHA {sha[:12]})'); return n

# ---------- OFS – Causes de décès 2024 (XLSX, cellules) ----------
COD_PAGE = 'https://www.bfs.admin.ch/asset/fr/36262352'
COD_XLSX = 'https://dam-api.bfs.admin.ch/hub/api/dam/assets/36262352/master'
def ofs_cod(c):
    data, sha, d, f = fetch(COD_XLSX, binaire=True)
    wb = openpyxl.load_workbook(io.BytesIO(data), read_only=True)
    rows = list(wb['2024'].iter_rows(values_only=True)); n = 0
    def iv(x): return int(str(x).replace("'", '').replace('-', '0') or 0)
    for i, r in enumerate(rows[5:37], start=6):
        lab = (r[1] if r[1] and r[0] in (None, 'dont:') else r[0]) or ''
        lab = str(lab).strip()
        if not lab or lab == 'Total': continue
        try: hs, he, fs, fe = map(iv, r[2:6])
        except Exception: continue
        tot = hs + he + fs + fe
        cle = 'cod:' + re.sub(r'[^a-z0-9]+', '_', __import__('regles').norm(lab)).strip('_')
        put(c, dict(cle=cle, source='OFS – Statistique des causes de décès (CoD)', libelle=lab, valeur=tot, valeur_txt=fmt(tot),
            unite='décès/an', population='Population résidante permanente de Suisse décédée en 2024',
            age_sexe=f'tous âges ; hommes {fmt(hs+he)}, femmes {fmt(fs+fe)}',
            definition=f'Cause initiale de décès « {lab} » (CIM-10, certificat médical de décès)',
            mesure='Nombre annuel de décès (somme hommes/femmes, Suisses et étrangers)', annee='2024', territoire='Suisse ; population résidante',
            type_source='Relevé exhaustif obligatoire (OFS, CoD)', url=COD_PAGE,
            preuve=f'XLSX su-f-14.03.04.01.08, feuille 2024, ligne {i} « {lab} » : H-Suisse {hs} + H-Étranger {he} + F-Suisse {fs} + F-Étranger {fe} = {tot}', sha256=sha,
            phrase=f'En 2024, {fmt(tot)} décès en Suisse ont eu pour cause initiale « {lab} » (hommes {fmt(hs+he)}, femmes {fmt(fs+fe)}), selon la statistique exhaustive des causes de décès de l’OFS.'))
        n += 1
    journal(f'OFS-CoD 2024 : {n} causes chargées (SHA {sha[:12]})'); return n

# ---------- OFS/ONEC – Monitorage du cancer 2018–2022 (page officielle, chiffres clés) ----------
CANCERS = ['C00-14','C15','C16','C18-20','C22','C23-24','C25','C32','C33-34','C38-4-C45-0','C43','C50','C53','C54-55','C56',
           'C61','C62','C64','C67','C70-72','C73','C81','C82-86-C96','C90','C91','C92-94']
def _cancer(slug):
    url = f'https://cancer-monitorage.bfs.admin.ch/fr/detail/{slug}/'
    h, sha, d, f = fetch(url); return slug, url, h, sha
def ofs_cancer(c):
    n = 0
    with ThreadPoolExecutor(4) as ex: res = list(ex.map(_cancer, CANCERS))
    for slug, url, h, sha in res:
        if not h: journal(f'cancer {slug} : page indisponible'); continue
        t = texte(re.sub(r'</p>', ' ¦ ', h))
        nom = t.split(' | ')[0].strip()
        per = re.search(r'Chiffres clés de la période (\d{4})[–-](\d{4})', t)
        m = re.search(r'Nombre Nouveaux cas (.*?) Décès (.*?) Taux Nouveaux cas pour 100 000 (.*?) Décès pour 100 000 (.*?) Age médian', t)
        if not (m and per): journal(f'cancer {slug} : chiffres clés non lus'); continue
        def deux(s):
            cel = [x.strip() for x in s.split('¦') if x.strip()]
            if len(cel) != 2: return None
            out = []
            for x in cel:
                if x in ('–', '-', '—'): out.append(0.0); continue
                p = parse(x)
                if p is None: return None
                out.append(p.bas)
            return out
        nc, dc, tn, td = (deux(m.group(k)) for k in range(1, 5))
        periode = f'{per.group(1)}–{per.group(2)}'
        if not (nc and tn): journal(f'cancer {slug} : format inattendu « {m.group(0)[:120]} »'); continue
        for i, sexe in ((0, 'hommes'), (1, 'femmes')):
            if not nc[i] or nc[i] < 20: continue   # sexe non concerné ou effectif marginal
            put(c, dict(cle=f'can:{slug}:inc_{sexe[0]}', source='OFS / ONEC – Monitorage du cancer', libelle=f'{nom} – incidence ({sexe})',
                valeur=tn[i], valeur_txt=fmt(tn[i], 1), unite='nouveaux cas pour 100 000 personnes/an',
                population=f'Population résidante de Suisse, {sexe}', age_sexe=f'tous âges ; {sexe}',
                definition=f'Nouveau cas de tumeur maligne {slug} (CIM-10), enregistré par les registres cantonaux des tumeurs ; estimation nationale ONEC',
                mesure=f'Incidence annuelle (taux pour 100 000 tel que publié, moyenne annuelle {periode})', annee=periode, territoire='Suisse ; population générale',
                type_source='Registres des tumeurs (ONEC) et statistique des causes de décès (OFS) – monitorage officiel', url=url,
                preuve=f'Chiffres clés {periode} : nouveaux cas/an H {fmt(nc[0])}, F {fmt(nc[1])} ; taux pour 100 000 H {tn[0]}, F {tn[1]}', sha256=sha,
                phrase=f'En Suisse, sur {periode}, on a compté en moyenne {fmt(nc[i])} nouveaux cas par an de {nom.lower()} chez les {sexe}, soit {fmt(tn[i],1)} nouveaux cas pour 100 000 {sexe} par an (ONEC/OFS, monitorage du cancer).'))
            n += 1
        if dc:
            tot = dc[0] + dc[1]
            put(c, dict(cle=f'can:{slug}:deces', source='OFS / ONEC – Monitorage du cancer', libelle=f'{nom} – décès',
                valeur=tot, valeur_txt=fmt(tot), unite='décès/an', population='Population résidante de Suisse',
                age_sexe=f'tous âges ; hommes {fmt(dc[0])}, femmes {fmt(dc[1])}',
                definition=f'Décès avec cause initiale tumeur maligne {slug} (CIM-10)', mesure=f'Nombre annuel moyen de décès ({periode})',
                annee=periode, territoire='Suisse ; population générale', type_source='Statistique des causes de décès (OFS) – monitorage officiel',
                url=url, preuve=f'Chiffres clés {periode} : décès/an H {fmt(dc[0])}, F {fmt(dc[1])}', sha256=sha,
                phrase=f'Sur {periode}, le {nom.lower()} a causé en moyenne {fmt(tot)} décès par an en Suisse (hommes {fmt(dc[0])}, femmes {fmt(dc[1])}).'))
            n += 1
    journal(f'Monitorage cancer : {n} indicateurs'); return n

# ---------- OFSP – IDD, déclaration obligatoire et Sentinella (CSV API) ----------
IDD = {'TUBERCULOSIS_oblig': 'tuberculose', 'HIV_oblig': 'infection à VIH (nouveaux diagnostics)', 'AIDS_oblig': 'sida',
       'SYPHILIS_oblig': 'syphilis', 'GONORRHEA_oblig': 'gonorrhée', 'CHLAMYDIOSIS_oblig': 'chlamydiose',
       'HEPATITIS_A_oblig': 'hépatite A', 'HEPATITIS_B_oblig': 'hépatite B', 'HEPATITIS_C_oblig': 'hépatite C', 'HEPATITIS_E_oblig': 'hépatite E',
       'CAMPYLOBACTERIOSIS_oblig': 'campylobactériose', 'SALMONELLOSIS_oblig': 'salmonellose', 'SHIGELLOSIS_oblig': 'shigellose',
       'EHEC_oblig': 'infection à EHEC', 'LISTERIOSIS_oblig': 'listériose', 'LEGIONELLOSIS_oblig': 'légionellose',
       'MENINGO_oblig': 'méningococcie invasive', 'IPD_oblig': 'pneumococcie invasive', 'HAEMOPHILUSINFLUENZAE_oblig': 'infection invasive à Haemophilus influenzae',
       'MALARIA_oblig': 'paludisme', 'DENGUEFEVER_oblig': 'dengue', 'MEASLES_oblig': 'rougeole', 'RUBELLA_oblig': 'rubéole',
       'TBE_oblig': 'méningo-encéphalite à tiques (FSME)', 'TULAREMIA_oblig': 'tularémie', 'QFEVER_oblig': 'fièvre Q',
       'TYPHOIDPARATYPHOIDFEVER_oblig': 'fièvre typhoïde/paratyphoïde', 'CJD_oblig': 'maladie de Creutzfeldt-Jakob',
       'TETANUS_oblig': 'tétanos', 'DIPHTHERIA_oblig': 'diphtérie', 'BOTULISM_oblig': 'botulisme', 'BRUCELLOSIS_oblig': 'brucellose',
       'INFLUENZA_oblig': 'grippe (confirmée en laboratoire)', 'MONKEYPOX_oblig': 'mpox', 'CHIKUNGUNYA_oblig': 'chikungunya',
       'HANTA_oblig': 'hantavirose', 'TRICHINELLOSIS_oblig': 'trichinellose', 'ZIKA_oblig': 'zika', 'WESTNILEFEVER_oblig': 'fièvre du Nil occidental',
       'LYME_sentinella': 'borréliose de Lyme (consultations)', 'HERPESZOSTER_sentinella': 'zona (consultations)',
       'POSTZOSTERNEURALGIA_sentinella': 'névralgie post-zostérienne (consultations)', 'PERTUSSIS_sentinella': 'coqueluche (consultations)'}
ANNEE_IDD = '2025'
def _idd(f):
    url = f'https://api.idd.bag.admin.ch/api/v1/export/latest/{f}/csv'
    t, sha, d, p = fetch(url); return f, url, t, sha
def ofsp_idd(c):
    n = 0
    with ThreadPoolExecutor(3) as ex: res = list(ex.map(_idd, IDD))
    for f, url, t, sha in res:
        if not t: journal(f'IDD {f} : indisponible'); continue
        rows = list(csv.DictReader(io.StringIO(t)))
        grp = [k for k in ('agegroup', 'sex', 'type') if k in rows[0]]
        def tout(r): return all(r.get(g) in ('all', 'NA', '', None) for g in grp)
        cand = [r for r in rows if r['temporal_type'] == 'year' and r['temporal'] == ANNEE_IDD and r['georegion'] in ('CHFL', 'CH') and tout(r)
                and r['valueCategory'] in ('cases', 'consultations')]
        if not cand: journal(f'IDD {f} : pas de ligne annuelle {ANNEE_IDD} agrégée'); continue
        cand.sort(key=lambda r: (r['georegion'] != 'CHFL', r['valueCategory'] != 'cases'))
        r = cand[0]; mal = IDD[f]; sent = f.endswith('sentinella'); terr = 'Suisse et Liechtenstein' if r['georegion'] == 'CHFL' else 'Suisse'
        sysm = 'système Sentinella (consultations de médecine de premier recours, extrapolées)' if sent else 'système de déclaration obligatoire (critères de déclaration OFSP, cas confirmés)'
        v = float(r['value']); inc = r.get('incValue')
        unite = 'consultations/an' if sent else 'cas déclarés/an'
        put(c, dict(cle=f'idd:{f}:n', source='OFSP – IDD (déclaration obligatoire/Sentinella)', libelle=f'{mal} – cas annuels', valeur=v, valeur_txt=fmt(v, 0 if v == int(v) else 1),
            unite=unite, population=f'Population résidante de {terr}', age_sexe='tous âges ; deux sexes',
            definition=f'Cas de {mal} selon le {sysm}', mesure=f'Nombre annuel ({ANNEE_IDD})', annee=ANNEE_IDD, territoire=f'{terr} ; population générale',
            type_source='Surveillance épidémiologique nationale OFSP (Loi sur les épidémies)', url=url,
            preuve=f'{f}.csv : valueCategory={r["valueCategory"]}, temporal={r["temporal"]}, georegion={r["georegion"]}, value={r["value"]}, incValue={inc}', sha256=sha,
            phrase=f'En {ANNEE_IDD}, l’OFSP a recensé {fmt(v, 0 if v == int(v) else 1)} {"consultations" if sent else "cas déclarés"} de {mal} en {terr} ({sysm}).'))
        n += 1
        if inc not in (None, '', 'NA'):
            iv = float(inc)
            put(c, dict(cle=f'idd:{f}:inc', source='OFSP – IDD (déclaration obligatoire/Sentinella)', libelle=f'{mal} – incidence', valeur=iv, valeur_txt=fmt(iv, 2 if iv < 1 else 1),
                unite=('consultations' if sent else 'cas déclarés') + ' pour 100 000 habitants/an', population=f'Population résidante de {terr} (n = {r["pop"]})',
                age_sexe='tous âges ; deux sexes', definition=f'Cas de {mal} selon le {sysm}', mesure=f'Incidence annuelle déclarée ({ANNEE_IDD})',
                annee=ANNEE_IDD, territoire=f'{terr} ; population générale', type_source='Surveillance épidémiologique nationale OFSP', url=url,
                preuve=f'{f}.csv : temporal={r["temporal"]}, georegion={r["georegion"]}, incValue={inc}, pop={r["pop"]}', sha256=sha,
                phrase=f'En {ANNEE_IDD}, l’incidence déclarée de {mal} était de {fmt(iv, 2 if iv < 1 else 1)} {"consultations" if sent else "cas"} pour 100 000 habitants par an en {terr} ({sysm}).'))
            n += 1
    journal(f'OFSP-IDD : {n} indicateurs ({ANNEE_IDD})'); return n

# ---------- Obsan / MonAM – indicateurs (page officielle, phrase de tête + définition) ----------
OBSAN = ['monam/diabete-age-15','monam/hypertension-arterielle-age-15','monam/taux-de-cholesterol-eleve-age-15','monam/surpoids-et-obesite-age-15',
 'monam/maladies-des-voies-respiratoires-age-15','monam/maladies-cardiovasculaires-prevalence-age-15','monam/arthrose-arthrite-et-osteoporose-age-15',
 'obsan/symptomes-de-depression','obsan/bronchite-chroniqueemphyseme','obsan/osteoporose','obsan/troubles-du-sommeil','obsan/maux-de-dos-ou-de-tete',
 'obsan/infarctus-du-myocarde','obsan/attaques-cerebrales','obsan/taux-d-hospitalisation-pour-fracture-de-la-hanche','obsan/suicide-et-suicide-assiste',
 'monam/asthme-age-14-15','monam/consommation-d-alcool-chronique-a-risque-age-15','monam/consommation-de-tabac-age-15','obsan/chutes',
 'monam/diabete-age-14-15','monam/surpoids-et-obesite-age-6-12','monam/deces-dus-a-la-drogue','monam/pratique-de-jeu-a-risque-ou-problematique-age-15',
 'monam/consommation-de-cannabis-age-15-64','monam/traitements-par-agonistes-opiodes','obsan/maladies-psychiques-les-plus-frequentes-en-traitement-stationnaire',
 'monam/mortalite-due-a-lalcool-age-15-74','monam/mortalite-due-au-tabac','monam/cancer-prevalence','monam/utilisation-problematique-dinternet-age-15',
 'monam/consommation-de-somniferes-ou-tranquillisants-age-15','obsan/accidents']
def _obs(s):
    url = f'https://ind.obsan.admin.ch/fr/indicator/{s}'
    h, sha, d, f = fetch(url); return s, url, h, sha
def obsan(c):
    n = 0
    with ThreadPoolExecutor(3) as ex: res = list(ex.map(_obs, OBSAN))
    for s, url, h, sha in res:
        if not h: journal(f'Obsan {s} : indisponible'); continue
        t = texte(h)
        mt = re.match(r'(.*?) \| (MonAM|Obsan)', t); titre = mt.group(1) if mt else s
        lead = re.search(r'(?:Indicateurs Obsan DE FR IT EN|DE FR IT EN) ' + re.escape(titre) + r' (.*?)(?= Cet indicateur| Thèmes liés|$)', t)
        lead = lead.group(1) if lead else ''
        phrase1 = re.split(r'(?<=[.])\s+(?=[A-ZÀ-Ý])', lead)[0] if lead else ''
        defi = re.search(r'Définition (.*?)(?= Méthode| Source| Remarque| Interprétation| Bibliographie|$)', t)
        defi = defi.group(1)[:600] if defi else ''
        an = re.search(r'\b(20\d\d)\b', phrase1)
        v = re.search(r'(\d+(?:[.,]\d+)?)\s?(%|‰| pour 100[\s\u202f\u00a0\']?000)', phrase1)
        pop = re.search(r'(?:proportion|part|nombre|taux)[^.]{0,40}?\b(de (?:la )?(?:personnes|population|jeunes|enfants|adultes|femmes|hommes)[^.;]{0,140})', defi)
        val = _num(v.group(1))[0] if v else None
        if not pop:
            pp = re.search(r'(de la population(?: suisse| en Suisse)?(?: âgée de [^,.;]*)?|des jeunes âgés de [^,.;]*|des enfants et adolescents âgés de [^,.;]*)', phrase1)
            pop = type('M', (), {'group': lambda self, i, v=pp.group(1) if pp else '': v})() if pp else None
        put(c, dict(cle=f'obs:{s}', source='Obsan / OFSP-MonAM – indicateur', libelle=titre, valeur=val, valeur_txt=v.group(1) if v else '',
            unite=('%' if v and '%' in v.group(2) else (v.group(2).strip() if v else '')),
            population=(pop.group(1).strip() if pop else ''), age_sexe=(re.search(r'\(âge: ?([^)]*)\)', titre).group(1) + ' ans' if re.search(r'\(âge: ?([^)]*)\)', titre) else ''),
            definition=defi[:300], mesure=('Prévalence déclarée (enquête)' if 'Enquête' in defi or 'ESS' in defi or 'HBSC' in defi else 'Indicateur Obsan'),
            annee=an.group(1) if an else '', territoire='Suisse', type_source=('Enquête suisse sur la santé (ESS), OFS' if 'ESS' in defi else 'Indicateur officiel Obsan/OFSP'),
            url=url, preuve=phrase1[:400], sha256=sha, phrase=phrase1[:400]))
        n += 1
    journal(f'Obsan/MonAM : {n} indicateurs'); return n



# ---------- Obsan/MonAM : extraction CURÉE (valeur lue sur la page par motif ; contexte tiré de la définition officielle) ----------
ESS = 'Enquête transversale par interview – Enquête suisse sur la santé (ESS) 2022, OFS (n ≈ 22 000) ; indicateur MonAM/OFSP'
POP15 = 'Population de 15 ans et plus vivant en ménage privé en Suisse'
OBS_SPEC = [  # (clé, page, motif de la valeur, population, âge/sexe, définition du cas, mesure, unité, année, type)
 ('diabete', 'monam/diabete-age-15', r'En 2022, (\d+,\d)% de la population en Suisse déclarait avoir reçu un diagnostic de diabète', POP15, '15 ans et plus ; deux sexes',
  'Diabète déclaré (diagnostic médical reçu) et/ou prise d’un médicament antidiabétique', 'Prévalence déclarée au moment de l’enquête', '%', '2022', ESS),
 ('hta', 'monam/hypertension-arterielle-age-15', r'En Suisse, (\d+,\d)% de la population souffraient d’hypertension en 2022', POP15, '15 ans et plus ; deux sexes',
  'Hypertension artérielle déclarée et/ou prise de médicaments antihypertenseurs', 'Prévalence déclarée au moment de l’enquête', '%', '2022', ESS),
 ('cholesterol', 'monam/taux-de-cholesterol-eleve-age-15', r'En 2022, (\d+,\d)% de la population en Suisse déclarait avoir une cholestérolémie élevée', POP15, '15 ans et plus ; deux sexes',
  'Cholestérolémie élevée déclarée et/ou prise d’un hypolipémiant', 'Prévalence déclarée au moment de l’enquête', '%', '2022', ESS),
 ('obesite', 'monam/surpoids-et-obesite-age-15', r'ou obèse \((\d+,\d) %\)', POP15, '15 ans et plus ; deux sexes',
  'Obésité : IMC ≥ 30 kg/m² calculé sur poids et taille autodéclarés', 'Prévalence au moment de l’enquête', '%', '2022', ESS),
 ('surpoids_obesite', 'monam/surpoids-et-obesite-age-15', r'En 2022, (\d+,\d) % de la population suisse était en surpoids', POP15, '15 ans et plus ; deux sexes',
  'Surpoids ou obésité : IMC ≥ 25 kg/m² (autodéclaré)', 'Prévalence au moment de l’enquête', '%', '2022', ESS),
 ('asthme', 'monam/maladies-des-voies-respiratoires-age-15', r'(\d+,\d)% de la population a reçu un diagnostic médical pour de l’asthme', POP15, '15 ans et plus ; deux sexes',
  'Asthme diagnostiqué par un médecin, présent au cours des 12 derniers mois (autodéclaré)', 'Prévalence sur 12 mois', '%', '2022', ESS),
 ('bpco', 'monam/maladies-des-voies-respiratoires-age-15', r'et (\d+,\d)% pour une bronchite chronique, une BPCO symptomatique ou un emphysème', POP15, '15 ans et plus ; deux sexes',
  'Bronchite chronique, BPCO symptomatique ou emphysème diagnostiqué par un médecin, 12 derniers mois (autodéclaré)', 'Prévalence sur 12 mois', '%', '2022', ESS),
 ('arthrose', 'monam/arthrose-arthrite-et-osteoporose-age-15', r'En 2022, (\d+,\d)% de la population suisse souffrait d’arthrose ou d’arthrite', POP15, '15 ans et plus ; deux sexes',
  'Arthrose ou arthrite (autodéclarée) au cours des 12 derniers mois', 'Prévalence sur 12 mois', '%', '2022', ESS),
 ('osteoporose', 'monam/arthrose-arthrite-et-osteoporose-age-15', r'd’arthrose ou d’arthrite et (\d+,\d)% d’ostéoporose', POP15, '15 ans et plus ; deux sexes',
  'Ostéoporose (autodéclarée) au cours des 12 derniers mois', 'Prévalence sur 12 mois', '%', '2022', ESS),
 ('asthme_14_15', 'monam/asthme-age-14-15', r'En 2022, (\d+,\d)% des jeunes âgés de 14 et 15 ans en Suisse disent souffrir d’asthme', 'Élèves de 14 et 15 ans scolarisés en Suisse', '14–15 ans ; deux sexes',
  'Asthme diagnostiqué par un médecin (déclaré par l’élève)', 'Prévalence déclarée au moment de l’enquête', '%', '2022', 'Enquête scolaire HBSC 2022 ; indicateur MonAM/OFSP'),
 ('diabete_14_15', 'monam/diabete-age-14-15', r'(\d+,\d)% des jeunes âgés de 14 et 15 ans ont dit souffrir de diabète', 'Élèves de 14 et 15 ans scolarisés en Suisse', '14–15 ans ; deux sexes',
  'Diabète de type 1 ou 2 diagnostiqué par un médecin (déclaré par l’élève)', 'Prévalence déclarée au moment de l’enquête', '%', '2022', 'Enquête scolaire HBSC 2022 ; indicateur MonAM/OFSP'),
 ('alcool_chronique', 'monam/consommation-d-alcool-chronique-a-risque-age-15', r'En 2022, (\d+,\d)% de la population suisse consomme régulièrement de l\'alcool', POP15, '15 ans et plus ; deux sexes',
  'Consommation quotidienne moyenne d’alcool pur (autodéclarée) à risque moyen à élevé pour la santé (seuils OFSP)', 'Prévalence au moment de l’enquête', '%', '2022', ESS),
 ('tabac', 'monam/consommation-de-tabac-age-15', r'En 2022, (\d+,\d)% de la population suisse fumait', POP15, '15 ans et plus ; deux sexes',
  'Fumeur quotidien ou occasionnel (y compris tabac chauffé, hors cigarette électronique)', 'Prévalence au moment de l’enquête', '%', '2022', ESS),
 ('jeu', 'monam/pratique-de-jeu-a-risque-ou-problematique-age-15', r'En 2022, (\d+,\d)% de la population suisse a connu au cours de la vie un comportement à risque', POP15, '15 ans et plus ; deux sexes',
  'Pratique de jeux d’argent à risque ou problématique (questionnaire de dépistage, 4 questions)', 'Prévalence sur la vie entière', '%', '2022', ESS),
 ('cancer_prev5', 'monam/cancer-prevalence', r'passant de 1520 à (\d+) cas pour 100 000 habitants', 'Population résidante de Suisse', 'tous âges ; deux sexes',
  'Personne vivante ayant reçu un diagnostic de cancer (tous sièges) au cours des 5 années précédentes', 'Prévalence partielle à 5 ans (fin 2022)', 'cas pour 100 000 habitants', '2022',
  'Registres des tumeurs – ONEC/NICER ; indicateur MonAM/OFSP'),
]
def obsan_cure(c):
    n = 0
    for cle, page, motif, pop, age, defi, mes, unite, an, typ in OBS_SPEC:
        url = f'https://ind.obsan.admin.ch/fr/indicator/{page}'
        h, sha, d, f = fetch(url)
        if not h: continue
        t = texte(h); m = re.search(motif, t)
        if not m: journal(f'Obsan {cle} : motif non trouvé sur la page → non injecté'); continue
        val = _num(m.group(1))[0]; s0 = max(0, t.rfind('.', 0, m.start()) + 1); s1 = t.find('.', m.end()); phrase_src = t[s0:s1 + 1].strip()
        put(c, dict(cle=f'obs:{cle}', source='Obsan / OFSP-MonAM – indicateur', libelle=page.split('/')[-1], valeur=val, valeur_txt=m.group(1), unite=unite,
            population=pop, age_sexe=age, definition=defi, mesure=mes, annee=an, territoire='Suisse ; population vivant à domicile (communauté)', type_source=typ,
            url=url, preuve=phrase_src[:400], sha256=sha,
            phrase=f'En {an}, en Suisse, {m.group(1)} {unite} – {mes.lower()} – parmi : {pop.lower()} ({age}) ; définition du cas : {defi.lower()} ({typ.split(" ;")[0]}).'))
        n += 1
    journal(f'Obsan curé : {n}/{len(OBS_SPEC)} indicateurs lus sur page'); return n

def tout():
    c = db()
    for fn in (ofs_ms, ofs_cod, ofs_cancer, ofsp_idd, obsan_cure):
        etape = fn.__name__
        if c.execute('SELECT 1 FROM checkpoint WHERE etape=?', (etape,)).fetchone(): continue
        k = fn(c); c.execute('INSERT OR REPLACE INTO checkpoint VALUES(?,?,datetime("now"))', (etape, str(k))); c.commit()
        print(etape, k, flush=True)
    c.close()
if __name__ == '__main__': tout()
