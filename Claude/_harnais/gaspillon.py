#!/usr/bin/env python3
"""LE_GASPILLON — détecteur gratuit de gaspillage (zéro modèle), sur les journaux locaux de chaque agent.

Règles (une alerte = règle, agent, preuve courte, coût évité estimé en équivalent-tokens) :
  G1 REFETCH    même URL rapatriée deux fois, ou URL déjà dans sources_index → sources_cache.py cherche
  G2 DOMAINE    domaine en échec (403/404/429/court) relancé ≥ 2 fois → disjoncteur de sources_cache
  G3 INTEGRAL   Read sans limite ou cat d'un fichier > 50 Ko → resumeur / grep / sed -n
  G4 RELECTURE  même fichier lu ≥ 3 fois → MEMOIRE.md, carnet memoire_agent.py
  G5 SORTIE     résultat d'outil > 20 000 car. (principe RTK) : il pèse à chaque tour suivant
  G6 CONTEXTE   contexte > 250 k tokens → relais : MEMOIRE + nouvel agent
  G7 TOURS      tours > budget du type de tâche
  G8 ECHEC      même commande en échec ≥ 2 fois → corriger avant de relancer
  G9 MEDINA     tout accès à /home/user/Medina (projet fermé, ordre de Vial du 12.11.2026 ; corpus AIPS
                désormais dans ~/.cache/medina_aips → aips_fiche.py trouve)
Coût d'un résultat d'outil : car./3,5 × (1,25 + 0,1 × min(150, tours restants)), puisque le contexte est relu à chaque tour.
Usage : python3 Claude/_harnais/gaspillon.py [--depuis AAAA-MM-JJ] [--actifs]  → donnees/gaspillon.json + GASPILLON.html
"""
import json, re, os, glob, sys, html, collections, urllib.parse

PROJ = os.path.expanduser('~/.claude/projects')
D = os.path.dirname(os.path.abspath(__file__))
BUDGET = dict(redaction_2DX=220, redaction_1DX=130, redaction_PhaseA=260, audit=90, contre_audit=90, correction=80,
              gel_P1=60, recherche=60, autre=150)
sys.path.insert(0, D)
from suivi import type_tache, lot_de  # noqa: E402

ERR = re.compile(r'(?i)\b(403|404|429|forbidden|not found|too many requests|timed? ?out|ECONNRESET|could not resolve)\b')


def urls(inp):
    s = json.dumps(inp, ensure_ascii=False)
    return re.findall(r'https?://[^\s"\'\\)>]+', s)


def deja_index():
    f = os.path.join(D, 'donnees', 'sources_index.jsonl')
    return {json.loads(l)['url'] for l in open(f, encoding='utf-8')} if os.path.exists(f) else set()


def analyse(f, idx, desc=''):
    lignes = []
    for l in open(f, encoding='utf-8', errors='ignore'):
        try: lignes.append(json.loads(l))
        except Exception: pass
    tours = sum(1 for d in lignes if d.get('type') == 'assistant' and (d.get('message') or {}).get('usage'))
    usages, k, al = {}, 0, []
    vus_url, lus, echecs, dom_ko, ctx = collections.Counter(), collections.Counter(), collections.Counter(), collections.Counter(), 0
    for d in lignes:
        m = d.get('message') or {}
        if not isinstance(m, dict): continue
        if d.get('type') == 'assistant' and m.get('usage'):
            k += 1; us = m['usage']
            ctx = max(ctx, (us.get('cache_read_input_tokens') or 0) + (us.get('input_tokens') or 0) + (us.get('cache_creation_input_tokens') or 0))
        for c in m.get('content') or []:
            if not isinstance(c, dict): continue
            if c.get('type') == 'tool_use':
                inp = c.get('input') or {}; usages[c.get('id')] = (c.get('name'), inp, k)
                s = json.dumps(inp, ensure_ascii=False)
                if '/home/user/Medina' in s or '/Medina/' in s:
                    if not any(a[0] == 'G9' for a in al): al.append(('G9', 'accès au projet fermé MEDINA : ' + s[:90], 0))
                for u in urls(inp) if (c.get('name') == 'WebFetch' or re.search(r'\bcurl\b', s)) else []:
                    vus_url[u] += 1
                    if vus_url[u] == 2: al.append(('G1', u[:110], 0))
                    elif vus_url[u] == 1 and u in idx: al.append(('G1', 'déjà en cache : ' + u[:100], 0))
                p = inp.get('file_path') if c.get('name') == 'Read' else None
                mc = re.match(r'\s*(?:cat)\s+(\S+\.html?)\b', inp.get('command', '') or '')
                p = p or (mc.group(1) if mc else None)
                if p:
                    lus[p] += 1
                    if lus[p] == 3: al.append(('G4', os.path.basename(p), 0))
                    try:
                        if os.path.getsize(p) > 50000 and not inp.get('limit'):
                            al.append(('G3', f'{os.path.basename(p)} ({os.path.getsize(p)//1000} Ko)', 0))  # coût compté en G5
                    except OSError: pass
            elif c.get('type') == 'tool_result':
                nom, inp, kk = usages.get(c.get('tool_use_id'), (None, {}, k))
                cont = c.get('content'); txt = cont if isinstance(cont, str) else json.dumps(cont, ensure_ascii=False)
                if len(txt) > 20000:
                    al.append(('G5', f'{nom} {len(txt)//1000} k car.', int(len(txt) / 3.5 * (1.25 + 0.1 * min(150, tours - kk)))))
                if c.get('is_error') or (nom in ('WebFetch', 'Bash') and ERR.search(txt[:600] or '')):
                    for u in urls(inp):
                        h = re.sub(r"^https?://([^/:?#]+).*", r"\1", u); dom_ko[h] += 1
                        if dom_ko[h] == 2: al.append(('G2', h, 0))
                    if nom == 'Bash' and c.get('is_error'):
                        cmd = (inp.get('command') or '')[:80]; echecs[cmd] += 1
                        if echecs[cmd] == 2: al.append(('G8', cmd, 0))
    if ctx > 250000: al.append(('G6', f'{ctx//1000} k tokens', 0))
    t = type_tache(desc); b = BUDGET.get(t, 150)
    if tours > b: al.append(('G7', f'{tours} tours > {b} ({t})', 0))
    return dict(tours=tours, ctx=ctx, type=t, lot=lot_de(desc), alertes=al)


def main():
    depuis = sys.argv[sys.argv.index('--depuis') + 1] if '--depuis' in sys.argv else '2026-11-11'
    idx = deja_index(); res = []
    for f in glob.glob(f'{PROJ}/*/*/subagents/agent-*.jsonl') + glob.glob(f'{PROJ}/*/*.jsonl'):
        if '/subagents/' not in f and os.path.getsize(f) < 1000: continue
        meta = f.replace('.jsonl', '.meta.json'); desc = ''
        if os.path.exists(meta):
            try: desc = json.load(open(meta)).get('description', '')
            except Exception: pass
        if '/subagents/' not in f: desc = 'boucle principale'
        import datetime
        if datetime.datetime.fromtimestamp(os.path.getmtime(f)).date().isoformat() < depuis: continue
        r = analyse(f, idx, desc); r.update(agent=os.path.basename(f)[:-6], desc=desc[:70])
        if r['alertes']: res.append(r)
    par = collections.Counter(); cout = collections.Counter()
    for r in res:
        for g, _, c in r['alertes']: par[g] += 1; cout[g] += c
    os.makedirs(os.path.join(D, 'donnees'), exist_ok=True)
    json.dump(dict(par_regle=par, cout_estime=cout, agents=res), open(os.path.join(D, 'donnees', 'gaspillon.json'), 'w'), ensure_ascii=False, indent=0)
    lig = ''.join(f'<tr><td>{g}</td><td>{par[g]}</td><td>{cout[g]/1e6:.1f} M</td></tr>' for g in sorted(par))
    det = ''.join(f'<tr><td>{html.escape(r["desc"])}</td><td>{r["tours"]}</td><td>{r["ctx"]//1000} k</td><td>'
                  + '<br>'.join(html.escape(f'{g} {p}') for g, p, _ in r['alertes'][:6]) + '</td></tr>'
                  for r in sorted(res, key=lambda r: -sum(c for *_, c in r['alertes']))[:60])
    open(os.path.join(D, 'GASPILLON.html'), 'w').write(
        '<!doctype html><meta charset=utf-8><title>Le Gaspillon</title><style>body{font:15px system-ui;margin:16px;max-width:1000px}'
        'table{border-collapse:collapse;width:100%}td,th{border:1px solid #ccc;padding:4px;vertical-align:top}</style>'
        f'<h1>Le Gaspillon</h1><p>{len(res)} agents en alerte depuis {depuis}.</p><table><tr><th>Règle</th><th>Alertes</th><th>Coût évitable estimé</th></tr>{lig}</table>'
        f'<h2>Agents</h2><table><tr><th>Agent</th><th>Tours</th><th>Contexte</th><th>Alertes</th></tr>{det}</table>')
    print(' '.join(f'{g}:{par[g]}({cout[g]/1e6:.1f}M)' for g in sorted(par)), f'| {len(res)} agents')


if __name__ == '__main__':
    main()
