#!/usr/bin/env python3
"""SUIVI — compteur gratuit (zéro modèle) de la consommation de chaque agent et de la boucle principale.

Lit les journaux locaux de Claude Code (~/.claude/projects/*/<session>.jsonl et subagents/agent-*.jsonl),
calcule pour chaque agent : tours, tokens (entrée, cache lu, cache écrit, sortie), coût équivalent, outils,
lectures de sources (WebFetch/curl), statut ; classe la tâche (rédaction 1 ou 2 DX, Phase A, audit, correction…).
Écrit Claude/_harnais/donnees/agents.jsonl (métriques seules, aucune donnée personnelle) et progression_agents.html.

Coût équivalent (unité = 1 token d'entrée non caché) : entrée ×1, cache écrit ×1,25, cache lu ×0,1, sortie ×5.
Usage : python3 Claude/_harnais/suivi.py [--projets ~/.claude/projects] [--html Claude/_harnais/progression_agents.html]
"""
import json, re, os, glob, argparse, collections, html, datetime

POIDS = dict(input_tokens=1, cache_creation_input_tokens=1.25, cache_read_input_tokens=0.1, output_tokens=5)
TYPES = [('redaction_2DX', r'agent \d DX\.\d+-\d+'), ('redaction_1DX', r'^LOT_0\d\d DX\.\d+$'),
         ('redaction_PhaseA', r'LOT_0\d\d Phase A$'), ('contre_audit', r'(?i)contre-audit'), ('audit', r'Audit|Porte'),
         ('correction', r'(?i)correction'), ('gel_P1', r'Gel P1'),
         ('recherche', r'(?i)source|chiffre|fréquence|extraire|faits|ESGE'), ('autre', r'.')]


def type_tache(d):
    for k, rx in TYPES:
        if re.search(rx, d or ''):
            return k
    return 'autre'


def lot_de(d):
    m = re.search(r'LOT_?0*(\d{1,3})', d or '')
    return int(m.group(1)) if m else None


def lire_agent(f):
    u = collections.Counter(); outils = collections.Counter(); n = 0; t0 = t1 = None; ctx_max = 0; dernier = ''
    for ligne in open(f, encoding='utf-8', errors='ignore'):
        try:
            d = json.loads(ligne)
        except Exception:
            continue
        ts = d.get('timestamp'); t0 = t0 or ts; t1 = ts or t1
        m = d.get('message') or {}
        if d.get('type') == 'assistant' and isinstance(m, dict):
            us = m.get('usage') or {}
            if us:
                n += 1
                for k in POIDS:
                    u[k] += us.get(k, 0) or 0
                ctx_max = max(ctx_max, (us.get('cache_read_input_tokens', 0) or 0) + (us.get('input_tokens', 0) or 0))
            for c in m.get('content') or []:
                if isinstance(c, dict) and c.get('type') == 'tool_use':
                    nom = c.get('name'); outils[nom] += 1
                    cmd = json.dumps(c.get('input', {}), ensure_ascii=False)
                    if nom == 'WebFetch' or re.search(r'\bcurl\b', cmd): outils['_web'] += 1
                    if re.search(r'refdata', cmd): outils['_aips'] += 1
                    if re.search(r'cliche\.py', cmd): outils['_images'] += 1
                    if nom == 'Read' or re.search(r'"command": "(cat|sed -n|head|tail) ', cmd): outils['_lectures'] += 1
                    if re.search(r'_harnais/(memoire|cache|resumeur|aips_fiche)', cmd): outils['_memoire'] += 1
                elif isinstance(c, dict) and c.get('type') == 'text' and c.get('text'):
                    dernier = c['text'][:160]
    return dict(tours=n, ctx_max=ctx_max, debut=t0, fin=t1, outils=dict(outils), dernier=dernier, **u)


def collecter(projets):
    lignes = []
    for sess in glob.glob(os.path.join(projets, '*', '*.jsonl')):
        sid = os.path.basename(sess)[:-6]
        principal = lire_agent(sess)
        principal.update(id='principal-' + sid[:8], desc='boucle principale', type='principal', lot=None)
        lignes.append(principal)
        for f in glob.glob(os.path.join(projets, '*', sid, 'subagents', 'agent-*.jsonl')):
            aid = os.path.basename(f)[6:-6]
            meta = {}
            try:
                meta = json.load(open(f[:-6] + '.meta.json'))
            except Exception:
                pass
            r = lire_agent(f)
            desc = meta.get('description', '')
            r.update(id=aid, desc=desc, type=type_tache(desc), lot=lot_de(desc), fini=meta.get('finished'),
                     modele_agent=meta.get('agentType'))
            lignes.append(r)
    for r in lignes:
        r['cout'] = round(sum(r.get(k, 0) * w for k, w in POIDS.items()))
    return lignes


def page(lignes, sortie):
    maintenant = datetime.datetime.utcnow().isoformat(timespec='minutes')
    actifs = [r for r in lignes if r['type'] != 'principal' and not r.get('fini')]
    tot = sum(r['cout'] for r in lignes)
    rows = ''.join(
        '<tr class="%s"><td>%s</td><td>%s</td><td>%s</td><td>%d</td><td>%.0f k</td><td>%.0f k</td><td>%.2f M</td><td>%d</td><td>%d</td><td>%s</td></tr>' % (
            'actif' if not r.get('fini') and r['type'] != 'principal' else '', html.escape(r['desc'][:60]), r['type'],
            r.get('lot') or '', r['tours'], r['ctx_max'] / 1e3, r['output_tokens'] / 1e3, r['cout'] / 1e6,
            r['outils'].get('_web', 0), r['outils'].get('_memoire', 0), html.escape((r.get('fin') or '')[:16]))
        for r in sorted(lignes, key=lambda r: r.get('fin') or '', reverse=True))
    open(sortie, 'w', encoding='utf-8').write(f'''<!doctype html><html lang="fr"><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1"><title>Progression des agents</title>
<style>body{{font:14px system-ui;margin:16px;background:#f6fbff;color:#123}}table{{border-collapse:collapse;width:100%}}
td,th{{border-bottom:1px solid #d8e6f0;padding:4px 6px;text-align:left}}tr.actif{{background:#e9f9ee;font-weight:600}}
.k{{display:inline-block;background:#fff;border:1px solid #cfe3ef;border-radius:8px;padding:8px 12px;margin:4px}}</style>
<h1>Progression des agents</h1><p>Relevé du {maintenant} UTC (script gratuit, aucun modèle).</p>
<div class="k">Agents : {len(lignes) - 1}</div><div class="k">Actifs : {len(actifs)}</div>
<div class="k">Coût équivalent total : {tot / 1e6:.0f} M</div>
<div style="overflow-x:auto"><table><tr><th>Agent</th><th>Type</th><th>LOT</th><th>Tours</th><th>Contexte max</th>
<th>Sortie</th><th>Coût éq.</th><th>Web</th><th>Mémoire</th><th>Dernière activité</th></tr>{rows}</table></div></html>''')


if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    ap.add_argument('--projets', default=os.path.expanduser('~/.claude/projects'))
    ap.add_argument('--donnees', default='Claude/_harnais/donnees/agents.jsonl')
    ap.add_argument('--html', default='Claude/_harnais/progression_agents.html')
    a = ap.parse_args()
    L = collecter(a.projets)
    os.makedirs(os.path.dirname(a.donnees), exist_ok=True)
    with open(a.donnees, 'w', encoding='utf-8') as f:
        for r in L:
            r = dict(r); r.pop('dernier', None)
            f.write(json.dumps(r, ensure_ascii=False) + '\n')
    page(L, a.html)
    print(f'{len(L)} entrées ; coût total {sum(r["cout"] for r in L) / 1e6:.0f} M éq. ; {a.html}')
