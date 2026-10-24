# -*- coding: utf-8 -*-
"""gen_v7.py — briques communes des générateurs de cours V7 AUDITÉS (issues du pilote DX.6) + assemblage + découpage + pipeline.
Un générateur de monographie importe ces briques, remplit PTS (14 points) et appelle produire(META, PTS, SOURCES, ctx).
Pipeline déterministe par fichier : inserer_fenetres (fenêtres d'examens) → mobile (cartes ≤ 640 px, typographie) → sigles (glossaire).
Découpage : un seul fichier si le résultat final ≤ 198 000 octets ; sinon coupe aux frontières de points (jamais dans un point)."""
import os, re, sys, json, html as _h, subprocess, tempfile
ROOT = '/workspace/audit_1_10'
PY = os.path.join(ROOT, 'venv/bin/python')
CSS = open(os.path.join(ROOT, 'corriges/LOT_001/source/base.css')).read().strip()
MAXF = 198000
LOC = os.path.dirname(os.path.abspath(__file__))

def S(*n): return (' <span class="s">' + ' '.join(f'<a href="#source-S{i}">[S{i}]</a>' for i in n) + '</span>') if n else ''
def P(txt, *src): return f'<div class="p">{txt}{S(*src)}</div>\n'
def T(mot, definition): return f'<details class="terme"><summary>{mot}</summary><div class="exw">{definition}</div></details>'
def TAB(cols, rows, cap=None):
    h = ''.join(f'<th>{c}</th>' for c in cols)
    b = '\n'.join('<tr>' + ''.join(f'<td>{c}</td>' for c in r) + '</tr>' for r in rows)
    c = f'<caption>{cap}</caption>' if cap else ''
    return f"<div class=\"t\" style='overflow-x:auto;'><table>{c}<thead><tr>{h}</tr></thead><tbody>\n{b}\n</tbody></table></div>\n"
def F(summary, body, *rest):
    """Fenêtre de bloc ; les arguments entiers sont des numéros de sources ajoutés en fin de fenêtre, une chaîne fixe la classe."""
    cls = next((x for x in rest if isinstance(x, str)), 'fenetre'); src = [x for x in rest if isinstance(x, int)]
    if src: body += P('', *src)
    return f'<details class="{cls}"><summary>{summary}</summary>\n{body}</details>\n'
def PR(val, *src):
    """Probabilité ou prévalence d’un diagnostic en exposant rouge (règle 5), toujours sourcée."""
    assert src, 'PR sans source'
    return f'<sup class="proba">{val}</sup>' + S(*src)
def U(txt, *src): return f'<div class="urgence p">{txt}{S(*src)}</div>\n'
def UL(items): return '<ul>' + ''.join(f'<li>{x}</li>' for x in items) + '</ul>\n'
def OL(items): return '<ol>' + ''.join(f'<li>{x}</li>' for x in items) + '</ol>\n'
def H4(t): return f'<h4>{t}</h4>\n'
def mkPOINT(pref):
    def POINT(n, titre, body): return f'<section class="point" id="{pref}-p{n}"><h3><strong>{n}. {titre}</strong></h3>\n{body}</section>\n'
    return POINT

def build(M, pts, sources, suffixe='', titre_suite=''):
    nums = [int(re.search(r'id="%s-p(\d+)"' % M['pref'], x).group(1)) for x in pts]
    body = ''.join(pts)
    cites = {int(x) for x in re.findall(r'#source-S(\d+)', body)}
    src = '\n'.join(f'<li id="source-S{n}">[S{n}] {t}</li>' for n, t in sources if n in cites)
    manque = cites - {n for n, _ in sources}
    if manque: raise SystemExit(f'sources citées sans entrée : {sorted(manque)}')
    return ('<!DOCTYPE html>\n<html lang="fr"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">'
      f'<title>{M["lot_titre"]} · {M["dx"]} {M["court"]} · version AUDITÉE{suffixe}</title><style>{CSS}</style></head><body>\n'
      '<section class="limite" role="note" aria-label="Statut du fichier"><strong>Version AUDITÉE du 24 octobre 2026.</strong> '
      f'{M["statut"]} Elle n’est pas validée cliniquement par un médecin. '
      'Les posologies marquées « hors AIPS », c’est-à-dire absentes de l’information professionnelle suisse, proviennent de recommandations internationales et doivent être vérifiées avant toute prescription.</section>\n'
      f'<header><h2>{M["lot_titre"]} · {M["dx"]} {M["long"]}</h2><p>{M["sous_titre"]}</p></header><main>\n'
      '<nav aria-label="Navigation">' + ''.join(f'<a href="#{M["pref"]}-p{i}">{i}</a>' for i in nums) + '<a href="#sources">Sources</a></nav>\n'
      f'<details class="monographie" open><summary>{M["dx"]} · {M["long"]}{titre_suite}</summary>\n' + body + '</details>\n'
      '<section id="sources"><h2>Sources</h2><ol class="s">' + src + '</ol>'
      '<p class="s">Contenu produit par IA à partir des sources citées ; non validé cliniquement par un médecin.</p></section>\n'
      '</main>\n<!-- FIN_FICHIER -->\n</body></html>\n')

def pipeline(src_html, out, ctx_path, uid):
    r = subprocess.run([PY, f'{LOC}/inserer_l.py', src_html, out, '--ctx', ctx_path, '--portee', 'point',
                        '--max-octets', '100000000', '--prefixe-uid', uid], capture_output=True, text=True)
    if r.returncode: raise SystemExit(r.stderr)
    for tool in (f'{ROOT}/outils/mobile.py', f'{LOC}/sigles_l.py', f'{ROOT}/outils/charte_v7plus.py'):
        r2 = subprocess.run([PY, tool, out], capture_output=True, text=True)
        if r2.returncode: raise SystemExit(r2.stderr)
        if tool.endswith('sigles_l.py'): print('   ', r2.stdout.strip().split(':', 1)[-1][:160])
    return os.path.getsize(out)

def produire(M, PTS, SOURCES, ctx):
    """Écrit les sources intermédiaires dans corriges/LOT_X/source/ et les fichiers AUDITÉS finaux dans corriges/LOT_X/."""
    srcdir = os.path.join(ROOT, M['dossier'], 'source'); os.makedirs(srcdir, exist_ok=True)
    ctx_path = os.path.join(srcdir, f'ctx_{M["pref"]}.json'); json.dump(ctx, open(ctx_path, 'w'), ensure_ascii=False, indent=1)
    base = os.path.join(ROOT, M['dossier'], M['fichier'])          # …_AUDITÉ.html
    for old in [f for f in os.listdir(os.path.dirname(base)) if f.startswith(os.path.basename(base)[:-5])]:
        os.remove(os.path.join(os.path.dirname(base), old))
    def essai(groupes):
        res = []
        lettres = 'abcdef'
        for gi, g in enumerate(groupes):
            suf = '' if len(groupes) == 1 else '_' + lettres[gi]
            ts = '' if len(groupes) == 1 else f' (partie {lettres[gi]} : points {g[0]} à {g[-1]})'
            pts = [PTS[i - 1] for i in g]
            sp = os.path.join(srcdir, f'{M["pref"]}_source{suf}.html')
            open(sp, 'w', encoding='utf-8').write(build(M, pts, SOURCES, ' · ' + suf[1:] if suf else '', ts))
            out = base.replace('.html', suf + '.html') if suf else base
            n = pipeline(sp, out, ctx_path, (M['pref'] + (lettres[gi] if suf else '')).replace('-', ''))
            res.append((out, n))
        return res
    tailles = [len(p.encode()) for p in PTS]
    for k in (1, 2, 3, 4):
        # groupes contigus équilibrés en octets
        cible, groupes, cur, acc = sum(tailles) / k, [], [], 0
        for i, t in enumerate(tailles, 1):
            if cur and acc + t / 2 > cible * (len(groupes) + 1) and len(groupes) < k - 1:
                groupes.append(cur); cur = []
            cur.append(i); acc += t
        groupes.append(cur)
        res = essai(groupes)
        if all(n <= MAXF for _, n in res):
            for out, n in res: print(f'  → {os.path.relpath(out, ROOT)} : {n} octets')
            return res
        for out, _ in res: os.remove(out)
    raise SystemExit('découpage impossible sous 200 Ko')
