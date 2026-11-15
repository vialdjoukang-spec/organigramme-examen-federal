"""Régénère PLAN_COMPLETUDE_EPIDEMIO.{html,md} depuis reseau.sqlite (table taches). Cases cochées en rouge, compteur t / n."""
import os, sys, json, html, collections
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from noyau import db, maintenant, SORTIE

SECT = {1: '1. Classe A (source suisse probable)', 2: '2. Classe B (chiffre surtout européen)', 3: '3. Classe C (rubriques, signes : valeur de contexte européenne)'}
REGLES = ['Chaque DX nommé : deux recherches lancées en même temps, EUROPE (général) et SUISSE (spécifique), en colonnes séparées.',
          '100 % = au moins une valeur européenne vérifiée par DX nommé ; la valeur suisse s’y ajoute dès qu’elle existe.',
          'Contexte complet bloquant pour chaque valeur : population, âge/sexe, définition, mesure et période, unité, année, territoire, type de source.',
          'Territoire toujours écrit (Suisse, pays européen, UE, Europe). Hors Europe : on s’arrête, la valeur ne compte pas.',
          'Sources : Suisse (OFS, OFSP-IDD, ONEC, Obsan/MonAM, cohortes CoLaus, SAPALDIA, SHCS) ; Europe (ECDC, Eurostat, Orphanet, EMA, OMS Europe, registres et études européens via Europe PMC/PubMed).',
          'Référentiel Gemini/MHT non fiable : contrôle seulement, jamais source.',
          '« Candidats à lire » = articles trouvés automatiquement : une valeur n’est « vérifiée » qu’après lecture de la source et remplissage des 8 colonnes.',
          'Aucune injection dans les cours sans PR conforme au prompt L1, avec seulement des valeurs vérifiées.',
          'Chaque IA écrit seulement dans son dossier NomIA__Completude_Epidemio.']

def generer(dest=None):
    from recherche import COLS, exporter_jsonl
    dest = dest or os.environ.get('EPI_PLAN') or SORTIE
    c = db()
    T = [dict(zip(COLS, r)) for r in c.execute('SELECT * FROM taches ORDER BY priorite, entite, lot, dx')]
    nN = c.execute("SELECT COUNT(*) FROM applicabilite WHERE classe='N'").fetchone()[0]
    ck = c.execute("SELECT fait, date FROM checkpoint WHERE etape='recherche'").fetchone()
    n = len(T); t = sum(x['statut_eu'] == 'vérifié' for x in T); tc = sum(x['statut_ch'] == 'vérifié' for x in T)
    deux = sum(x['statut_eu'] == 'vérifié' or x['statut_ch'] == 'vérifié' for x in T)
    seu = collections.Counter(x['statut_eu'] for x in T); sch = collections.Counter(x['statut_ch'] for x in T)
    pc = lambda a: (f"{100 * a / n:.1f}" if n else '0').replace('.', ',')
    now = maintenant()[:16].replace('T', ' ')
    def val(x, niv):
        v = [q for q in json.loads(x[f'params_{niv}']) if q.get('statut') == 'vérifié']
        if v: return ' ; '.join(f"{q['valeur_txt']} {q['unite']} ({q['territoire']}, {q['annee']})" for q in v[:3])
        st = x[f'statut_{niv}']
        return f"{len(json.loads(x[f'candidats_{niv}']))} candidat(s) à lire" if st == 'candidats à lire' else st
    G = collections.OrderedDict()
    for x in T: G.setdefault(x['priorite'], collections.OrderedDict()).setdefault(x['entite'], []).append(x)
    H = ['<!doctype html><html lang="fr"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">',
         '<title>Plan de complétude épidémiologique</title><style>',
         'body{font:15px/1.45 system-ui,sans-serif;margin:0 auto;max-width:860px;padding:12px;color:#222}h1{font-size:1.3em}h2{font-size:1.1em;margin-top:1.4em}',
         '.cpt{font-size:1.6em;font-weight:700;color:#c00;margin:.3em 0}.barre{height:12px;background:#eee;border-radius:6px;overflow:hidden;margin-bottom:6px}.barre i{display:block;height:100%;background:#c00}',
         'ul{list-style:none;padding-left:0}li{padding:4px 0;border-bottom:1px solid #f0f0f0}.dx{font-weight:600}.niv{display:block;padding-left:4px;font-size:.93em}',
         'input[type=checkbox]{accent-color:#d00;width:17px;height:17px;vertical-align:middle;margin-right:5px}.ok{color:#b00}',
         'details{margin:4px 0}summary{cursor:pointer;font-weight:600}.n{color:#c00;font-weight:600}table{border-collapse:collapse}td,th{border:1px solid #ddd;padding:3px 6px}</style></head><body>',
         '<h1>Plan de complétude épidémiologique – Europe + Suisse</h1>',
         f'<p class="cpt">Europe : {t} / {n} tâches ({pc(t)} %)</p><div class="barre"><i style="width:{pc(t).replace(",", ".")}%"></i></div>',
         f'<p class="cpt" style="font-size:1.2em">Suisse : {tc} / {n} ({pc(tc)} %) · au moins une valeur : {deux} / {n}</p>',
         f'<p>Mis à jour le {now} (Europe/Zurich). Dernier lot : {html.escape(ck[0]) if ck else "—"}. Une tâche = un DX nommé ; '
         'case rouge cochée = valeur vérifiée, contexte complet.</p>',
         '<table><tr><th>Statut</th><th>Europe</th><th>Suisse</th></tr>' + ''.join(f'<tr><td>{html.escape(k)}</td><td>{seu.get(k, 0)}</td><td>{sch.get(k, 0)}</td></tr>' for k in sorted(set(seu) | set(sch))) + '</table>',
         f'<p>Hors compteur : {nN} DX sans nom (N), à reclasser après la Phase A (section 4).</p>',
         '<h2>Règles</h2><ul>' + ''.join(f'<li>• {html.escape(r)}</li>' for r in REGLES) + '</ul>']
    M = ['# Plan de complétude épidémiologique – Europe + Suisse', '', f'**Europe : {t} / {n} tâches ({pc(t)} %)** · Suisse : {tc} / {n} ({pc(tc)} %) · au moins une valeur : {deux} / {n}',
         f'Mis à jour le {now} (Europe/Zurich). Une tâche = un DX nommé. Version à cases rouges : `PLAN_COMPLETUDE_EPIDEMIO.html`.', '',
         '| Statut | Europe | Suisse |', '|---|---|---|'] + [f'| {k} | {seu.get(k, 0)} | {sch.get(k, 0)} |' for k in sorted(set(seu) | set(sch))] + ['', f'Hors compteur : N {nN} (section 4).', '', '## Règles'] + [f'- {r}' for r in REGLES]
    for p, E in G.items():
        tt = [x for e in E.values() for x in e]; ft = sum(x['statut_eu'] == 'vérifié' for x in tt); fc = sum(x['statut_ch'] == 'vérifié' for x in tt)
        H.append(f'<h2>{SECT.get(p, p)} <span class="n">EU {ft} / {len(tt)} · CH {fc}</span></h2>'); M += ['', f'## {SECT.get(p, p)} — Europe {ft} / {len(tt)} · Suisse {fc}']
        for e, L in E.items():
            fe = sum(x['statut_eu'] == 'vérifié' for x in L)
            H.append(f'<details{" open" if p == 1 and fe < len(L) and len(H) < 400 else ""}><summary>{html.escape(L[0]["diagnostic"])} <span class="n">{fe} / {len(L)}</span></summary><ul>')
            M.append(f"- **{L[0]['diagnostic']}** ({fe} / {len(L)})")
            for x in L:
                oe, oc = x['statut_eu'] == 'vérifié', x['statut_ch'] == 'vérifié'
                H.append(f'<li><span class="dx">LOT_{x["lot"]:03d} DX{x["dx"]}</span>'
                         f'<label class="niv{" ok" if oe else ""}"><input type="checkbox" disabled{" checked" if oe else ""}>Europe : {html.escape(val(x, "eu"))}</label>'
                         f'<label class="niv{" ok" if oc else ""}"><input type="checkbox" disabled{" checked" if oc else ""}>Suisse : {html.escape(val(x, "ch"))}</label></li>')
                M.append(f"  - [{'x' if oe else ' '}] LOT_{x['lot']:03d} DX{x['dx']} Europe : {val(x, 'eu')}")
                M.append(f"  - [{'x' if oc else ' '}] LOT_{x['lot']:03d} DX{x['dx']} Suisse : {val(x, 'ch')}")
            H.append('</ul></details>')
    H += ['<h2>4. Reclassement après la Phase A</h2>', f'<ul><li><label><input type="checkbox" disabled>{nN} DX sans nom : relancer <code>applicabilite.py</code> puis <code>recherche.py</code> quand les noms existent.</label></li></ul></body></html>']
    M += ['', '## 4. Reclassement après la Phase A', f'- [ ] {nN} DX sans nom : relancer `applicabilite.py` puis `recherche.py` quand les noms existent.']
    os.makedirs(dest, exist_ok=True)
    for ext, body in (('html', '\n'.join(H)), ('md', '\n'.join(M) + '\n')):
        f = os.path.join(dest, f'PLAN_COMPLETUDE_EPIDEMIO.{ext}')
        open(f + '.tmp', 'w', encoding='utf-8').write(body); os.replace(f + '.tmp', f)
    exporter_jsonl(c, os.path.join(dest, 'taches.jsonl'))
    return t, tc, n

if __name__ == '__main__':
    print(generer())
