#!/usr/bin/env python3
"""Reconstruit les 14 fragments depuis l'ancien HTML : citation par phrase vérifiée contre le paquet."""
import re, json, html, sys, os
from bs4 import BeautifulSoup, NavigableString, Tag
sys.path.insert(0, '/home/user/organigramme-examen-federal/Claude/_outils')
import controle3 as C
D = 'Claude/LOT_001/_travail/PA/'
OLD = open('/tmp/claude-0/-home-user/15c9849e-78d1-5a00-9dcf-bd21b180736d/scratchpad/old.html').read()
PQ = json.load(open(D + 'paquet.json'))['passages']
PAS = {p['id']: p for p in PQ}
NUMS = {p['id']: C.nombres(p['texte']) for p in PQ}
BYURL = {}
for p in PQ: BYURL.setdefault(p['url'], []).append(p['id'])
# ancien S-id -> url
src = OLD[OLD.find('Sources</h2>'):]
SURL = {}
for m in re.finditer(r'<li id="S(\d+)">(.*?)</li>', src, re.S):
    u = re.search(r'href="(https?://[^"]+)"', m.group(2))
    if u: SURL['S' + m.group(1)] = html.unescape(u.group(1))
def mots(t):
    return {w[:6] for w in re.findall(r"[a-zà-ÿ]{5,}", t.lower())}
for p in PQ: p['_m'] = mots(p['texte'])
PROT = re.compile(r'\[(S\d+)\]')
NEEDED = set(json.load(open(D + 'needed.json'))) if os.path.exists(D + 'needed.json') else set()
USED = set(); perdus = []; stats = {'cite': 0, 'sans': 0, 'perdu': 0}
CONNECT_DEFAULT = 'Le lecteur ouvre les fenêtres de la rubrique « %s » : '

def choisir(ph, srcs, dose):
    t = C.texte(ph)
    nums = C.nombres(C.STRUCT.sub(' ', t))
    W = mots(t)
    cand = []
    for s in srcs:
        cand += BYURL.get(SURL.get(s, ''), [])
    cand = list(dict.fromkeys(cand))
    def score(i): return len(PAS[i]['_m'] & W) + (1.0 if i in USED else 0)
    def couvrir(pool, seuil):
        reste = set(nums); res = []
        pool = sorted(pool, key=lambda i: (-len(NUMS[i] & reste) if reste else 0, -score(i)))
        # greedy
        for _ in range(3):
            if not reste: break
            best = max(pool, key=lambda i: (len(NUMS[i] & reste), score(i)), default=None)
            if not best or not (NUMS[best] & reste): return None
            if score(best) < seuil and not res and False: return None
            res.append(best); reste -= NUMS[best]
        return res if not reste else None
    if dose:
        aips = [i for i in cand if i.startswith('aips')]
        # doses: tout l'AIPS, mais drogue reconnue par recouvrement
        if not aips: aips = [i for i in PAS if i.startswith('aips') and score(i) >= 4]
        if nums:
            res = couvrir(aips, 2)
            if res and any(score(i) >= 2 for i in res): return res
            aips = [i for i in PAS if i.startswith('aips') and score(i) >= 4]
            res = couvrir(aips, 4)
            return res
        b = max(aips, key=score, default=None)
        return [b] if b and score(b) >= 3 else None
    if nums:
        pools = [cand, [i for i in PAS if score(i) >= 4]]
        for k, pool in enumerate(pools):
            if not pool: continue
            if k == 0:
                # un seul extrait de la source citée qui couvre tout, avec recouvrement
                ok = [i for i in pool if nums <= NUMS[i]]
                if ok:
                    b = max(ok, key=score)
                    if score(b) >= 2: return [b]
                res = couvrir(pool, 0)
                if res and sum(score(i) for i in res) >= 3: return res
            else:
                ok = [i for i in pool if nums <= NUMS[i]]
                if ok:
                    b = max(ok, key=score)
                    if score(b) >= 5: return [b]
        return None
    # sans nombre : uniquement des extraits déjà cités par une phrase chiffrée (limite le poids des sources)
    cand = [i for i in cand if i in NEEDED] if NEEDED else cand
    if cand:
        b = max(cand, key=score)
        if score(b) >= 3: return [b]
    return 'AUCUNE'


def scinder(t):
    res = []; d = 0; cur = ''
    i = 0
    while i < len(t):
        c = t[i]
        if c in '(«[': d += 1
        elif c in ')»]': d = max(0, d - 1)
        if c == ';' and d == 0 and i + 1 < len(t) and t[i + 1] == ' ':
            res.append(cur); cur = ''; i += 2; continue
        cur += c; i += 1
    res.append(cur)
    return res

NUMUSED = set()
def poser(ph0, r):
    end = ph0.rstrip()
    if r != 'AUCUNE' and (C.nombres(C.STRUCT.sub(' ', C.texte(ph0))) or C.DOSE.search(C.texte(ph0))): NUMUSED.update(r)
    if r == 'AUCUNE': return end
    m = re.search(r'([.!?]|[.!?]</\w+>)$', end)
    return (end[:m.start()] + cit(r) + end[m.start():]) if m else end + cit(r)

def clauses(ph0, use):
    """Phrase non vérifiable d'un bloc : cite chaque proposition, retire celles dont un nombre n'est pas lu."""
    core = ph0.strip().rstrip('.!?')
    for sep in ('; ', ', '):
        if sep not in core: continue
        parts = core.split(sep)
        if len(parts) < 2: continue
        res = []; ok = 0
        for part in parts:
            if not part.strip(): continue
            dose = bool(C.DOSE.search(C.texte(part)))
            r = choisir(part, use, dose)
            if r is None: continue
            res.append(part if r == 'AUCUNE' else part + cit(r)); ok += (r != 'AUCUNE')
        if ok and res:
            return sep.join(res) + '.'
    return None

def cit(ids):
    USED.update(ids)
    return ''.join(f'<sup class="r"><a href="#sb-{i}">{i}</a></sup>' for i in ids)

def traiter_texte(inner, bloc_srcs, td=False):
    """inner: html d'un bloc sans <details>. Retourne html de phrases citées."""
    inner = re.sub(r'<br\s*/?>', ' ', inner.replace('\n', ' '))
    finals = []
    srcs_bloc = list(dict.fromkeys(PROT.findall(inner[-160:])))  # marqueurs de fin
    # phrases
    parts = re.split(r'(?<=[.!?])\s+(?=[A-ZÀ-Ý«<])', inner.strip())
    out = []
    if not td:
        np_ = []
        for ph in parts:
            if len(C.texte(ph).split()) > 29 and '; ' in ph:
                ps = [x.strip() for x in scinder(ph.rstrip('.!? ')) if x.strip()]
                for i, x in enumerate(ps):
                    x = x[0].upper() + x[1:] if x else x
                    np_.append(x + '.')
            else: np_.append(ph)
        parts = np_
    for ph in parts:
        ss = list(dict.fromkeys(PROT.findall(ph)))
        ph0 = re.sub(r'\s*\[S\d+\]', '', ph).strip()
        ph0 = re.sub(r'^\s*(?:\[S\d+\]\s*)+', '', ph0)
        if len(C.texte(ph0).split()) < 2: 
            if ph0: out.append(ph0)
            continue
        use = ss + [s for s in bloc_srcs if s not in ss]
        dose = bool(C.DOSE.search(C.texte(ph0)))
        r = choisir(ph0, use, dose)
        if td and ph0.rstrip().endswith('?') and not C.DOSE.search(C.texte(ph0)): r = 'AUCUNE'
        if td and r not in (None,) and not C.nombres(C.STRUCT.sub(' ', C.texte(ph0))) and not dose: r = 'AUCUNE'
        if r is None and re.search(r'\b\d+,0\b', ph0):
            v = re.sub(r'\b(\d+),0\b(?![\d,])', r'\1', ph0)
            r2 = choisir(v, use, dose)
            if r2 not in (None, 'AUCUNE'): ph0, r = v, r2
        if r is None and td and len(C.texte(ph0).split()) <= 6 and not C.DOSE.search(C.texte(ph0)) and not re.search(r'\d{2,}', C.texte(ph0)):
            out.append(ph0); continue
        if r is None:
            rec = clauses(ph0, use)
            if rec:
                out.append(rec); stats['cite'] += 1; continue
            stats['perdu'] += 1
            perdus.append(C.texte(ph0)[:400])
            out.append(f'[[DROP{len(perdus)-1}]]')
            continue
        out.append(poser(ph0, r))
        stats['cite' if r != 'AUCUNE' else 'sans'] += 1
    return ' '.join(out)

def nettoie_spans(soup):
    for sp in soup.find_all('span'):
        if sp.get('class') and 'g' in sp.get('class'): continue
        txt = sp.get_text()
        sp.replace_with(NavigableString(txt))

def inner(tag):
    return ''.join(str(c) for c in tag.contents)


def corps_fenetre(w):
    srcs_all = list(dict.fromkeys(PROT.findall(w.get_text())))
    out = []; buf = ''
    def flush():
        nonlocal buf
        if buf.strip():
            h = traiter_texte(buf, srcs_all)
            if h.strip(): out.append(f'<div class="p">{h}</div>')
        buf = ''
    for c in w.contents:
        if isinstance(c, Tag) and c.name == 'div' and 'tw' in (c.get('class') or []):
            flush(); out.append(convert_block(c, 0, [], 'pa'))
        elif isinstance(c, Tag) and c.name in ('ul', 'ol'):
            flush(); out.append(convert_block(c, 0, [], 'pa'))
        elif isinstance(c, Tag) and c.name == 'br': buf += ' '
        elif isinstance(c, Tag) and c.name == 'strong' and not buf.strip() and not out and c.get_text().rstrip().endswith(('.', ':')) and len(c.get_text().split()) < 14:
            out.append(f'<h4><em>{html.escape(c.get_text(" ", strip=True).rstrip(".:"))}</em></h4>')
        else: buf += str(c)
    flush()
    return ''.join(out)


def blocs(el, pn, fen, pre):
    out = []; buf = ''; pend = []; rub = [None]
    def lead_pend():
        if not pend: return
        sents = []
        for g in range(0, len(pend), 3):
            grp = pend[g:g + 3]
            lst = grp[0] if len(grp) == 1 else ', '.join(grp[:-1]) + ' et ' + grp[-1]
            sub = f'une notion de la rubrique « {rub[0]} »' if (g == 0 and rub[0]) else ('une notion' if g == 0 else 'une autre notion')
            sents.append(f'Si {sub} reste floue, ' + (f'la fenêtre {lst} la précise.' if len(grp) == 1 else f'les fenêtres {lst} la précisent.'))
        out.append('<div class="p">' + ' '.join(sents) + '</div>')
        pend.clear(); rub[0] = None
        out.extend(fen); fen.clear()
    def flush():
        nonlocal buf
        if buf.strip():
            h = traiter_texte(buf, list(dict.fromkeys(PROT.findall(el.get_text()))))
            if h.strip(): out.append(f'<div class="p">{h}</div>')
        buf = ''
    for c in el.contents:
        if isinstance(c, Tag) and c.name == 'details':
            if buf.strip():
                lead = re.sub(r'\s*\[S\d+\]', '', buf).strip().rstrip(':').strip()
                if C.est_verbale(lead) and len(lead.split()) > 6 and not pend: flush()
                else:
                    rub[0] = re.sub(r'^(?:Fenêtres?)\s+(?:de |du |des |d\')?', '', lead, flags=re.I).strip() or None
                    buf = ''
            Cpt.n += 1
            fid = f'{pre}-p{pn}-f{Cpt.n}'
            lib = c.find('summary').get_text(' ', strip=True)
            w = c.find('div', class_='w')
            nettoie_spans(w)
            pend.append(f'<button class="w" popovertarget="{fid}">{html.escape(lib)}</button>')
            fen.append(f'<div id="{fid}" popover class="fenetre">{corps_fenetre(w)}</div>')
        elif isinstance(c, Tag) and c.name == 'div' and 'tw' in (c.get('class') or []):
            flush(); lead_pend(); out.append(convert_block(c, pn, fen, pre))
        elif isinstance(c, Tag) and c.name in ('ul', 'ol'):
            flush(); lead_pend(); out.append(convert_block(c, pn, fen, pre))
        elif isinstance(c, Tag) and c.name == 'strong' and not buf.strip() and not out and not pend and c.get_text().rstrip().endswith(('.', ':')) and len(c.get_text().split()) < 14:
            out.append(f'<h4><em>{html.escape(c.get_text(" ", strip=True).rstrip(".:"))}</em></h4>')
        elif isinstance(c, Tag) and c.name == 'br': buf += ' '
        else:
            if pend: lead_pend()
            buf += str(c)
    flush(); lead_pend()
    return '\n'.join(out)

class Cpt: n = 0
def convert_block(el, pn, fen, pre):
    """Retourne html du bloc converti (str), fen: liste de popovers à placer après."""
    if isinstance(el, NavigableString): return ''
    nm = el.name
    cls = el.get('class') or []
    if nm in ('h3', 'h4'):
        t = el.get_text(' ', strip=True)
        return f'<h4><em>{html.escape(t)}</em></h4>'
    if nm == 'div' and ('p' in cls or 'k' in cls or 'u' in cls):
        nettoie_spans(el)
        return blocs(el, pn, fen, pre)
    if nm == 'div' and 'tw' in cls:
        tb = el.find('table')
        nettoie_spans(tb)
        for sp in list(tb.find_all('span')): pass
        cap = tb.find('caption')
        o = ['<div class="t" style="overflow-x:auto"><table>']
        if cap: o.append(f'<caption>{html.escape(cap.get_text(" ", strip=True))}</caption>')
        for tr in tb.find_all('tr'):
            cells = []
            for c in tr.find_all(['th', 'td']):
                if c.name == 'th':
                    cells.append(f'<th>{c.decode_contents()}</th>'); continue
                srcs = list(dict.fromkeys(PROT.findall(c.get_text()) + PROT.findall(tr.get_text())))
                h = traiter_texte(inner(c), srcs, td=True)
                if not h.strip(): h = '—'
                k = f' class="{" ".join(c["class"])}"' if c.get('class') else ''
                cells.append(f'<td{k}>{h}</td>')
            o.append('<tr>' + ''.join(cells) + '</tr>')
        o.append('</table></div>')
        return '\n'.join(o)
    if nm in ('ul', 'ol'):
        lis = []
        for li in el.find_all('li', recursive=False):
            lis.append('<li>' + traiter_texte(inner(li), list(dict.fromkeys(PROT.findall(li.get_text())))) + '</li>')
        return f'<ul>{"".join(lis)}</ul>'
    return f'<!--NONGERE {nm}-->'

def section(htmlsec, pn, pre='pa'):
    Cpt.n = 0
    soup = BeautifulSoup(htmlsec, 'lxml')
    body = soup.body
    out = []; fen = []
    for el in body.children:
        if isinstance(el, NavigableString): continue
        b = convert_block(el, pn, fen, pre)
        if b: out.append(b)
        # popovers après le bloc
        if fen:
            out.extend(fen); fen.clear()
    return '\n'.join(out)

if __name__ == '__main__':
    m = OLD[OLD.find('<main'):OLD.find('Sources</h2>')]
    pts = {}
    pos = [(int(x.group(1)), x.start(), x.end()) for x in re.finditer(r'<h3 id="ssp-p(\d+)">.*?</h3>', m)]
    iend = m.find('</section>', pos[-1][2])
    for k, (n, s, e) in enumerate(pos):
        fin = pos[k + 1][1] if k + 1 < len(pos) else iend
        pts[n] = m[e:fin]
    b2 = m[m.find('id="bloc2"'):]
    b2 = b2[b2.find('</h2>') + 5:]
    ia = b2.find('<h3 id="algorithme"')
    dxpart, algo = b2[:ia], b2[ia:]
    algo = algo[:algo.rfind('</section>')] if '</section>' in algo else algo
    dxpart = re.sub(r'<h3 id="dx(\d+)">(.*?)</h3>', lambda x: f'<h3>{x.group(2)}</h3>', dxpart)
    dxpart = dxpart.replace('<h3 id="comparatif">', '<h3>')
    pts[4] += '\n<h3>4.b Les dix diagnostics différentiels du LOT_001</h3>\n' + dxpart
    pts[10] += '\n' + algo
    for n in range(1, 15):
        txt = section(pts[n], n)
        open(D + f'fragments/p{n:02d}.html', 'w').write(txt + '\n')
    open(D + 'HELP_perdus.txt', 'w').write('\n'.join(perdus))
    if '--needed' in sys.argv: json.dump(sorted(NUMUSED), open(D + 'needed.json', 'w'))
    print(stats)
