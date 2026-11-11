#!/usr/bin/env python3
"""decoupe.py — découpe déterministe des fichiers d'un LOT en monographies (SSP, DX.1–DX.10) et en 14 points V7 (§6).
Usage : decoupe.py LOT_001   →  work/LOT_001/decoupe.json
Règles :
 - fichiers de cours retenus : Appel A (Plan et Liste) et Appel B Parties (pièces a/b concaténées dans l'ordre) ;
   les fichiers INDEX / A_REDIGER / AUDIT / VALIDATION / MANIFEST sont classés « autre » ;
 - un titre de point = bloc court (≤ 160 car.) commençant par « N. » (1 ≤ N ≤ 14) hors fenêtre, ou titre gdoc ;
 - le point est attribué par le SENS du titre (lexique §6) ; si le numéro diffère, une anomalie est notée ;
 - changement de monographie : titre/summary commençant par « DX.n » ou « D3.n » (Appel B seulement)."""
import sys, os, re, json, glob
sys.path.insert(0, '/workspace/audit_1_10/outils')
from commun import linearize, lot_dir, work, norm

POINTS = {1: 'Définition et sémantique', 2: 'Épidémiologie (Suisse, puis Europe)', 3: 'Physiopathologie',
          4: 'Démarche diagnostique', 5: 'Anamnèse ciblée et drapeaux rouges', 6: 'Examen physique ciblé',
          7: 'Approche syndromique', 8: 'Diagnostic positif et critères', 9: 'Examens complémentaires',
          10: 'Arbre décisionnel', 11: 'Prise en charge (A-B-C-D)', 12: 'Prévention', 13: 'Points clés',
          14: 'Pièges et questions d’examen'}
KW = [  # ordre = priorité (testé sur les titres réels des LOTS 1–10)
    (13, r'points?\s+cl[ée]s|à retenir|messages?\s+cl'),
    (14, r'pi[èe]ges?'),
    (12, r'pr[ée]vention'),
    (10, r'arbre|algorithme|logigramme'),
    (3, r'physiopath'),
    (2, r'[ée]pid[ée]mio'),
    (6, r'examen (physique|clinique)'),
    (5, r'anamn[èe]se|drapeaux?'),
    (9, r'examens?\s+compl|explorations?|^examens?\b|imagerie|biologie'),
    (8, r'diagnostic positif|crit[èe]res'),
    (7, r'syndrom|signes|sympt[ôo]mes|s[ée]miolog'),
    (1, r'd[ée]finition|s[ée]mantique|terminologie'),
    (4, r'd[ée]marche|diagnostics? diff[ée]rentiel|hypoth[èe]ses'),
    (11, r'prise en charge|traitement|th[ée]rapeut|conduite à tenir'),
]
HEAD_RE = re.compile(r'^(?:point\s*)?(\d{1,2})(?:\s*[\.\)]|\s+[–—-])\s+(?!\d)(.{2,})$', re.I)
INLINE_HEAD = re.compile(r'^\s*(\d{1,2})\.\s+([^.]{3,110}?)\.\s+\S')
DX_RE = re.compile(r'^\s*(?:DX\s*\.?\s*(\d{1,2})|D\d{1,2}\.(\d{1,2}))(?!\d)\s*(?:[—–\-·:|]|\s)', re.I)
SRC_RE = re.compile(r'^(sources?|r[ée]f[ée]rences|bibliographie)\b', re.I)
BLOC2_RE = re.compile(r'\bbloc\s*2\b', re.I)

def classify(name):
    n = name.lower()
    if re.search(r'_audit[ée](?:_[a-z])?\.html$', n):
        return 'Corrigé AUDITÉ'
    if re.search(r'index|a_rediger|audit|validation|manifest|preaudit|help|registre|charte|mode_emploi|rapport|recherche', n) and not re.search(r'audit_corrige', n):
        return 'autre'
    if 'appel_a' in n and ('plan' in n or '14pts' in n):
        return 'Appel A'
    m = re.search(r'partie_(\d)', n)
    if 'appel_b' in n and m:
        return 'Partie ' + m.group(1)
    return 'autre'

def course_files(lot):
    d = lot_dir(lot)
    files = sorted(glob.glob(os.path.join(d, '**', '*.html'), recursive=True))
    out = []
    for f in files:
        t = classify(os.path.basename(f))
        if t == 'autre' or os.path.getsize(f) < 2000:
            continue
        out.append((t, f))
    order = {'Appel A': 0, 'Partie 1': 1, 'Partie 2': 2, 'Partie 3': 3, 'Partie 4': 4, 'Corrigé AUDITÉ': 5}
    out.sort(key=lambda x: (order[x[0]], os.path.basename(x[1])))
    return out

def map_point(title):
    t = title.lower()
    for p, rx in KW:
        if re.search(rx, t):
            return p
    return None

def decoupe(lot):
    courses, order = {}, []
    windows_all = {}
    files = course_files(lot)
    for typ, f in files:
        blocks, windows = linearize(f)
        windows_all.update(windows)
        cur = 'SSP' if typ == 'Appel A' else None
        point = None
        for b in blocks:
            t = b['text']
            is_head = b['tag'] in ('h1','h2','h3','h4','h5','h6','summary') or (len(t) <= 160 and b['tag'] in ('p','div','text'))
            if b['depth'] == 0 and is_head and len(t) <= 200:
                if typ != 'Appel A':
                    if typ == 'Corrigé AUDITÉ' and b['tag'] == 'summary' and re.match(r'^SSP(\s+G\d+)?\s*·', t):
                        cur = 'SSP'; point = None
                        if cur not in courses:
                            courses[cur] = {'id': cur, 'title': t, 'type': typ, 'files': [], 'blocks': [], 'heads': []}; order.append(cur)
                        if os.path.basename(f) not in courses[cur]['files']: courses[cur]['files'].append(os.path.basename(f))
                        continue
                    if typ == 'Corrigé AUDITÉ' and b['tag'] == 'summary' and BLOC2_RE.search(t):
                        cur = 'APPEL_A_BLOC2'; point = None
                        courses.setdefault(cur, {'id': cur, 'title': t, 'type': typ, 'files': [], 'blocks': [], 'heads': []})
                        if cur not in order: order.append(cur)
                        continue
                    m = DX_RE.match(t)
                    if m and (b['tag'] in ('h1','h2','h3','h4','summary') or (b['tag'] in ('p','div','text') and len(t) <= 160)) and not HEAD_RE.match(t):
                        cur = 'DX.%d' % int(m.group(1) or m.group(2)); point = None
                        if cur not in courses:
                            courses[cur] = {'id': cur, 'title': t, 'type': typ, 'files': [], 'blocks': [], 'heads': []}
                            order.append(cur)
                        if os.path.basename(f) not in courses[cur]['files']:
                            courses[cur]['files'].append(os.path.basename(f))
                        continue
                elif BLOC2_RE.search(t) and b['tag'] in ('h1','h2','h3','h4','summary'):
                    cur = 'APPEL_A_BLOC2'; point = None
                    courses.setdefault(cur, {'id': cur, 'title': t, 'type': typ, 'files': [], 'blocks': [], 'heads': []})
                    if cur not in order: order.append(cur)
                    continue
                if SRC_RE.match(t) and b['tag'] in ('h1','h2','h3','h4','summary'):
                    point = 'sources'; continue
                m = HEAD_RE.match(t)
                if m and cur and cur != 'APPEL_A_BLOC2':
                    num = int(m.group(1)); sem = map_point(m.group(2))
                    strong_like = b['tag'] in ('h1','h2','h3','h4','h5','h6','summary') or len(t) <= 120
                    if 1 <= num <= 14 and strong_like and (sem is not None or b['tag'].startswith('h')):
                        p = sem or num
                        c = courses[cur]
                        c['heads'].append({'num': num, 'sem': sem, 'assigned': p, 'title': t, 'file': b['file']})
                        point = p
                        continue
            # format V5/V6 : « 9. Examens complémentaires : … . Texte du point » dans un même paragraphe (souvent dans un <details>)
            if cur and cur != 'APPEL_A_BLOC2' and b['depth'] <= 1 and b['tag'] in ('p', 'div', 'text', 'li'):
                mi = INLINE_HEAD.match(t)
                if mi and 1 <= int(mi.group(1)) <= 14:
                    sem = map_point(mi.group(2))
                    if sem is not None:
                        c0 = courses.setdefault(cur, {'id': cur, 'title': 'SSP — ' + os.path.basename(f), 'type': typ, 'files': [], 'blocks': [], 'heads': []})
                        if cur not in order: order.append(cur)
                        c0['heads'].append({'num': int(mi.group(1)), 'sem': sem, 'assigned': sem, 'title': mi.group(0)[:90], 'file': b['file'], 'inline': True})
                        point = sem
                        b = dict(b, ctx='main' if b['ctx'] == 'fenetre' and b['depth'] == 1 else b['ctx'])
            if cur is None:
                continue
            if cur not in courses:
                courses[cur] = {'id': cur, 'title': 'SSP — ' + os.path.basename(f), 'type': typ, 'files': [], 'blocks': [], 'heads': []}
                order.append(cur)
            if os.path.basename(f) not in courses[cur]['files']:
                courses[cur]['files'].append(os.path.basename(f))
            b['point'] = point
            courses[cur]['blocks'].append(b)
    # synthèse par point
    res = []
    for cid in order:
        c = courses[cid]
        if cid == 'APPEL_A_BLOC2':
            res.append({'id': cid, 'title': c['title'], 'type': c['type'], 'files': c['files'], 'bloc2_words': sum(len(b['text'].split()) for b in c['blocks']),
                        'bloc2_tables': None, 'points': {}, 'anomalies': [], 'blocks': c['blocks']})
            continue
        pts = {}
        anomalies = []
        for p in range(1, 15):
            bl = [b for b in c['blocks'] if b.get('point') == p]
            main = [b for b in bl if b['ctx'] == 'main' and not b['cell']]
            pts[p] = {'present': any(h['assigned'] == p for h in c['heads']), 'words_total': sum(len(b['text'].split()) for b in bl),
                      'words_main': sum(len(b['text'].split()) for b in main),
                      'n_fenetres': len({s[2] for b in bl for s in b['spans'] if s[2]}),
                      'n_cells': sum(1 for b in bl if b['cell']),
                      'titles': [h['title'] for h in c['heads'] if h['assigned'] == p]}
            if not pts[p]['present']:
                anomalies.append(f'point {p} ({POINTS[p]}) ABSENT')
            elif pts[p]['words_total'] < 25:
                anomalies.append(f'point {p} ({POINTS[p]}) quasi vide ({pts[p]["words_total"]} mots)')
            if len(pts[p]['titles']) > 1:
                anomalies.append(f'point {p} : {len(pts[p]["titles"])} titres concurrents → ' + ' | '.join(pts[p]['titles']))
        for h in c['heads']:
            if h['sem'] and h['sem'] != h['num']:
                anomalies.append(f'titre « {h["title"][:80]} » numéroté {h["num"]} mais correspond au point {h["sem"]} (§6)')
            if not h['sem']:
                anomalies.append(f'titre « {h["title"][:80]} » non reconnu par le lexique §6 (attribué au n° {h["num"]})')
        res.append({'id': cid, 'title': c['title'], 'type': c['type'], 'files': c['files'], 'points': pts,
                    'coverage': sum(1 for p in pts.values() if p['present'] and p['words_total'] >= 25),
                    'anomalies': anomalies, 'blocks': c['blocks']})
    return {'lot': lot, 'files': [(t, os.path.basename(f), os.path.getsize(f)) for t, f in files], 'courses': res, 'windows': windows_all}

if __name__ == '__main__':
    lot = sys.argv[1]
    d = decoupe(lot)
    json.dump(d, open(work(lot, 'decoupe.json'), 'w'), ensure_ascii=False)
    for c in d['courses']:
        if c['id'] == 'APPEL_A_BLOC2':
            print(f"{c['id']:<14} Bloc 2 : {c['bloc2_words']} mots"); continue
        miss = [p for p in range(1, 15) if not c['points'][p]['present']]
        print(f"{c['id']:<14} {c['coverage']:>2}/14  manquants={miss}  mots={sum(p['words_total'] for p in c['points'].values())}  fichiers={len(c['files'])}")
