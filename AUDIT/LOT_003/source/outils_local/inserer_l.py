#!/usr/bin/env python3
"""inserer_fenetres.py — insertion déterministe des fenêtres d'examens (onglets Principe / Interprétation) dans un cours.
Usage : inserer_fenetres.py ENTREE.html SORTIE.html [--ctx ctx.json] [--portee point|cours] [--max-octets 200000]
Règles :
 - détection des examens par le lexique d'outils/examens.py (même moteur que l'audit) ;
 - 1re mention de chaque examen par point (section.point) — ou par cours avec --portee cours ;
 - jamais dans <summary>, <a>, <label>, titres, <th>, <title>, une fenêtre d'examen existante, ni dans les sources (#sources) ;
 - un <p> qui reçoit une fenêtre devient <div class="p"> (un <details> ne peut pas être enfant de <p>) ;
 - la CSS des fenêtres est ajoutée une seule fois dans le <style> existant ; le marqueur FIN_FICHIER est conservé ;
 - budget : si la taille dépasse --max-octets, seules les 1res mentions par cours sont encore enveloppées ;
 - ctx.json : {"_prefixe": "Dans l’hyperthyroïdie", "<clé>": "ligne propre au diagnostic"} → onglet Interprétation."""
import sys, os, re, json, argparse
from bs4 import BeautifulSoup, NavigableString, Comment
D = '/workspace/audit_1_10/bibliotheque_examens'
HERE = os.path.dirname(os.path.abspath(__file__))
X = os.path.join(HERE, '..', 'bib_extra')
sys.path.insert(0, HERE)
import examens_l as examens

SKIP = {'summary', 'a', 'label', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'th', 'title', 'style', 'script', 'head', 'nav', 'input'}
CSS_MARK = '/*FENETRES_EXAMENS*/'

def load_lib():
    idx = json.load(open(os.path.join(D, 'index.json')))
    lex2key = {v['lex']: k for k, v in idx.items()}
    frag = {k: open(os.path.join(D, v['fragment'])).read().strip() for k, v in idx.items()}
    if os.path.exists(os.path.join(X, 'index.json')):
        ix = json.load(open(os.path.join(X, 'index.json')))
        for k, v in ix.items():
            lex2key[v['lex']] = k; frag[k] = open(os.path.join(X, v['fragment'])).read().strip()
    return lex2key, frag

def skip(node):
    for p in node.parents:
        if p.name in SKIP: return True
        if p.name == 'details' and 'ex' in (p.get('class') or []): return True
        if p.get('id') == 'sources' or {'sources', 'sigles'} & set(p.get('class') or []): return True
    return False

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('entree'); ap.add_argument('sortie')
    ap.add_argument('--ctx'); ap.add_argument('--portee', default='point', choices=['point', 'cours'])
    ap.add_argument('--max-octets', type=int, default=200000)
    ap.add_argument('--prefixe-uid', default='x')
    a = ap.parse_args()
    lex2key, frag = load_lib()
    ctx = json.load(open(a.ctx)) if a.ctx else {}
    pref = ctx.get('_prefixe', 'Dans ce chapitre')
    src = open(a.entree, encoding='utf-8').read()
    soup = BeautifulSoup(src, 'html.parser')
    st = soup.find('style')
    if st is not None and CSS_MARK not in st.string:
        st.string = st.string + CSS_MARK + open(os.path.join(D, 'fenetres_examens.css')).read().replace('\n', '')
    size = len(str(soup).encode())
    seen_point, seen_course, uid, log = set(), set(), 0, []
    texts = [t for t in soup.find_all(string=True) if not isinstance(t, Comment) and t.strip() and not skip(t)]
    for t in texts:
        sec = t.find_parent('section', class_='point')
        scope = sec.get('id') if sec is not None else '_'
        s = str(t); hits = []
        for (b, e, name, cat, g) in examens.find(s):
            k = lex2key.get(name)
            if not k: continue
            m = re.match(r'\w*', s[e:]); e2 = e + (m.end() if m else 0)   # « thyroglobulin » → « thyroglobuline »
            if s[b:e2].count('(') > s[b:e2].count(')') and s[e2:e2 + 1] == ')': e2 += 1   # « … (TRAb) » : parenthèse fermée
            k = ctx.get('_alias', {}).get(k, k)   # ex. échographie générique → échographie thyroïdienne dans ce cours
            key_scope = (scope if a.portee == 'point' else '_', k)
            first_course = k not in seen_course
            if key_scope in seen_point: continue
            if not first_course and size > a.max_octets: continue
            seen_point.add(key_scope); seen_course.add(k)
            uid += 1
            c = ctx.get(k)
            cx = f"<div class='ctx'><strong>{pref} :</strong> {c}</div>" if c else ''
            w = frag[k].replace('{{UID}}', f'{a.prefixe_uid}{uid}').replace('{{LIBELLE}}', s[b:e2]).replace('{{CTX}}', cx)
            hits.append((b, e2, w)); size += len(w.encode()) - (e2 - b)
            log.append({'uid': uid, 'cle': k, 'point': scope, 'mot': s[b:e2]})
        if not hits: continue
        out, pos = [], 0
        for b, e, w in hits:
            out.append(s[pos:b]); out.append(w); pos = e
        out.append(s[pos:])
        new = BeautifulSoup(''.join(out), 'html.parser')
        for p in t.parents:
            if p.name == 'p':
                p.name = 'div'; p['class'] = (p.get('class') or []) + ['p']
        t.replace_with(new)
    html = str(soup)
    if 'FIN_FICHIER' not in html:
        html = html.replace('</body>', '<!-- FIN_FICHIER --></body>')
    open(a.sortie, 'w', encoding='utf-8').write(html)
    json.dump(log, open(a.sortie + '.fenetres.json', 'w'), ensure_ascii=False, indent=0)
    print(f"{uid} fenêtres insérées ; {len(seen_course)} examens distincts ; {len(html.encode())} octets → {a.sortie}")

if __name__ == '__main__':
    main()
