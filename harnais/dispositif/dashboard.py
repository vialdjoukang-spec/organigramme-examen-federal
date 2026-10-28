#!/usr/bin/env python3
"""Tableau de bord en direct, branché sur le Harnais (veille + workflow + dossiers LOT).
  python3 harnais/dispositif/dashboard.py [port=8765]        serveur : http://localhost:PORT/  (/etat.json)
  python3 harnais/dispositif/dashboard.py --snapshot f.html  page statique avec l'état du moment"""
import glob, json, os, re, sys, time
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
R = Path(__file__).resolve().parents[2]
WF = Path.home() / ".claude/projects/-home-user-organigramme-examen-federal"
FONC = {"redacteur-phase-a": "Rédacteur Phase A", "redacteur": "Rédacteur DD", "auditeur-medical": "Auditeur médical", "auditeur-conformite": "Auditeur conformité", "mecanique": "Mécanique", "general-purpose": "Dépôt / PR"}
_pos = {}; _ev = []
SESS = WF / "939dd4bc-a7c0-53f6-b753-cf529d7def3a.jsonl"
def _ts(s):
    import calendar
    return calendar.timegm(time.strptime(s[:19], "%Y-%m-%dT%H:%M:%S")) + float("0" + s[19:23] if s[19:20] == "." else 0)
def tokens():
    fs = [(SESS, "principal")]
    for jf in glob.glob(str(WF / "*/subagents/workflows/wf_*/agent-*.jsonl")) + glob.glob(str(WF / "*/subagents/agent-*.jsonl")):
        m = jf[:-6] + ".meta.json"
        try: r = json.load(open(m)).get("agentType", "agent")
        except Exception: r = "agent"
        fs.append((Path(jf), r))
    for f, role in fs:
        if not f.exists(): continue
        p0 = _pos.get(str(f), 0); sz = f.stat().st_size
        if sz <= p0: continue
        with open(f, "rb") as h:
            h.seek(p0); data = h.read()
        nl = data.rfind(b"\n")
        if nl < 0: continue
        _pos[str(f)] = p0 + nl + 1
        for l in data[:nl].splitlines():
            try:
                e = json.loads(l); u = e["message"]["usage"]; _ev.append((_ts(e["timestamp"]), role, u.get("output_tokens", 0), u.get("input_tokens", 0) + u.get("cache_creation_input_tokens", 0), u.get("cache_read_input_tokens", 0)))
            except Exception: pass
    ev = sorted(_ev); now = time.time(); tot = {}; ser = []; co = ci = cr = 0
    for t, role, o, i, c in ev:
        co += o; ci += i; cr += c; x = tot.setdefault(role, [0, 0, 0]); x[0] += o; x[1] += i; x[2] += c
        if not ser or t - ser[-1][0] >= 20: ser.append([int(t), co, ci, cr])
        else: ser[-1] = [int(t), co, ci, cr]
    if ev and (not ser or ser[-1][1] != co): ser.append([int(ev[-1][0]), co, ci, cr])
    if len(ser) > 240: ser = ser[:: len(ser) // 240 + 1] + [ser[-1]]
    r5 = [e for e in ev if e[0] > now - 300]
    return dict(serie=ser, total=dict(sortie=co, entree=ci, cache=cr), par_role=tot, debit_min=round(sum(e[2] + e[3] for e in r5) / 5), debit_sortie_min=round(sum(e[2] for e in r5) / 5))
def divers(ag, lot):
    import shutil, subprocess
    out = {}
    try: out["verrous"] = [json.load(open(p)) for p in glob.glob(str(R / ".cache/verrous/*.lock"))]
    except Exception: out["verrous"] = []
    out["lecons"] = {}
    for p in glob.glob(str(R / "harnais/LECONS/*.md")):
        out["lecons"][Path(p).stem] = len(re.findall(r"^\s*\d+\.\s+\*\*", open(p, encoding="utf-8").read(), re.M))
    try:
        L = json.load(open(R / "LOT_Claude_Finaux/ETAT_FILE.json"))["lots"][:16]
        out["file_g"] = [dict(lot=l["lot"], code=l["code"], verdict=l.get("verdict"), merge=l.get("merge")) for l in L]
    except Exception: out["file_g"] = []
    try:
        g = lambda *a: subprocess.run(["git", *a], cwd=R, capture_output=True, text=True).stdout.strip()
        out["git"] = dict(branche=g("rev-parse", "--abbrev-ref", "HEAD"), dernier=g("log", "-1", "--format=%h %s")[:70], modifies=len(g("status", "--short").splitlines()))
    except Exception: out["git"] = None
    try: out["sentinelle"] = json.load(open(R / ".cache/harnais/sentinelle.json"))
    except Exception: out["sentinelle"] = None
    out["disque_libre_go"] = round(shutil.disk_usage(R).free / 1e9, 1)
    act = [a for a in ag if a["actif"]]
    red = sum(a["type"] in ("redacteur", "redacteur-phase-a") for a in act); au = sum(a["type"] in ("auditeur-medical", "auditeur-conformite") for a in act)
    out["equipe"] = dict(redacteurs=red, auditeurs=au, ok_redacteurs=1 <= red <= 8, ok_auditeurs=1 <= au <= 2)
    labs = [a["label"] for a in act]; out["collision"] = len(labs) != len(set(labs)) or len({v["fichier"] for v in out["verrous"]}) != len(out["verrous"])
    if lot:
        ecr = [f for f in lot["fichiers"] if f["ecrit"]]; out["ko_ecrits"] = sum(f["ko"] for f in ecr)
    return out
def etat():
    now = time.time(); ag = []
    for jf in glob.glob(str(WF / "*/subagents/workflows/wf_*/journal.jsonl")):
        if now - os.path.getmtime(jf) > 3 * 3600: continue
        d = Path(jf).parent; st = {}
        for l in open(jf):
            try: e = json.loads(l)
            except Exception: continue
            if e.get("type") == "started": st[e["agentId"]] = dict(id=e["agentId"], label=e["label"], phase=e["phase"], actif=True, wf=d.name)
            elif e.get("type") == "result" and e["agentId"] in st: st[e["agentId"]]["actif"] = False
        for i, a in st.items():
            m = d / f"agent-{i}.meta.json"; j = d / f"agent-{i}.jsonl"
            try: tp = json.loads(m.read_text()).get("agentType", "")
            except Exception: tp = ""
            a["fonction"] = FONC.get(tp, tp); a["type"] = tp
            a["depuis_s"] = int(now - m.stat().st_mtime) if m.exists() else 0
            a["derniere_activite_s"] = int(now - j.stat().st_mtime) if j.exists() else None
            if a["actif"] and (a["derniere_activite_s"] is None or a["derniere_activite_s"] > 180): a["actif"] = False; a["orphelin"] = True
            ag.append(a)
    plans = sorted(glob.glob(str(R / ".cache/travail/LOT_*/PLAN.json")), key=os.path.getmtime)
    lot = None
    if plans:
        P = json.load(open(plans[-1])); D = Path(plans[-1]).parent; N = P["N"]; fich = []
        for i in ["A"] + list(range(1, N + 1)):
            n = f"LOT_{P['lot']}_Phase_A_V0.html" if i == "A" else f"LOT_{P['lot']}_Phase_B_V0_DX.{i}.html"
            f = D / n; ecr = f.exists(); ko = f.stat().st_size // 1000 if ecr else 0
            med = list((D / "audits").glob(f"MED_{n}_C*.md")); conf = list((D / "audits").glob(f"CONF_{n}_C*.md"))
            fich.append(dict(i=str(i), ecrit=ecr, ko=ko, med=len(med), conf=len(conf), audite=bool(med and conf)))
        pts = sum(x["ecrit"] + x["audite"] for x in fich); tot = 2 * (N + 1) + 1
        try: ev = next(l for l in json.load(open(R / "LOT_Claude_Finaux/ETAT_FILE.json"))["lots"] if l["lot"] == P["lot"]); dep = bool(ev.get("merge"))
        except Exception: dep = False
        lot = dict(lot=P["lot"], code=P["code"], nom=P["nom"], N=N, fichiers=fich, ecrits=sum(x["ecrit"] for x in fich), audites=sum(x["audite"] for x in fich), depose=dep, pct=round(100 * (pts + dep) / tot))
    try: h = json.load(open(R / ".cache/harnais/etat.json"))
    except Exception: h = None
    return dict(t=time.strftime("%H:%M:%S"), agents=ag, actifs=sum(a["actif"] for a in ag), termines=sum(not a["actif"] for a in ag), lot=lot, harnais=h, tokens=tokens(), divers=divers(ag, lot))
PAGE = r'''<!DOCTYPE html><html lang="fr"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>HARNAIS · DIRECT</title><style>
:root{--bg:#0b1020;--card:#141b34;--ln:#26305a;--fg:#e8ecff;--mut:#8b96c9;--g:#22d38a;--r:#ff5d73;--o:#ffa94d;--b:#5aa9ff;--v:#b388ff;--y:#ffd43b}
*{box-sizing:border-box}body{margin:0;background:radial-gradient(1200px 600px at 10% -10%,#1b2557,transparent),var(--bg);color:var(--fg);font:14px/1.45 system-ui,sans-serif;padding:20px clamp(12px,3vw,40px) 50px}
h1{margin:0;font-size:1.2rem;letter-spacing:.08em}.sub{color:var(--mut);font-size:12px;margin:2px 0 18px}.live{display:inline-block;width:9px;height:9px;border-radius:50%;background:var(--g);box-shadow:0 0 10px var(--g);margin-right:8px;animation:p 1.2s infinite}@keyframes p{50%{opacity:.25}}
.k{display:grid;grid-template-columns:repeat(auto-fit,minmax(150px,1fr));gap:12px;margin-bottom:16px}.c{background:var(--card);border:1px solid var(--ln);border-radius:14px;padding:14px 16px}.c b{display:block;font-size:2rem;line-height:1.1}.c span{color:var(--mut);font-size:12px}
.big{padding:18px}.bar{height:26px;border-radius:13px;background:#0a0f23;border:1px solid var(--ln);overflow:hidden;margin:10px 0}.fill{height:100%;background:linear-gradient(90deg,var(--b),var(--g));transition:width .6s;display:flex;align-items:center;justify-content:flex-end;padding-right:10px;font-weight:700;color:#04122a}
.grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(88px,1fr));gap:8px;margin-top:10px}.f{border-radius:10px;padding:6px 8px;border:1px solid var(--ln);font-size:11px;background:#0e1430}.f b{display:block;font-size:12px}.f.e{border-color:var(--b);background:#12244a}.f.a{border-color:var(--g);background:#0f3a2c}.f.w{opacity:.55}
table{width:100%;border-collapse:collapse}th,td{padding:8px 10px;border-bottom:1px solid var(--ln);text-align:left;font-size:13px}th{color:var(--mut);font-weight:600;font-size:11px;text-transform:uppercase;letter-spacing:.06em}
.t{display:inline-block;padding:2px 10px;border-radius:999px;font-weight:700;font-size:12px;color:#06101f!important}.t-redacteur-phase-a{background:var(--v)}.t-redacteur{background:var(--b)}.t-auditeur-medical{background:var(--r)}.t-auditeur-conformite{background:var(--o)}.t-mecanique{background:#9aa4d6}.t-general-purpose{background:var(--g)}
.st{font-weight:700}.on{color:var(--g)}.off{color:var(--mut)}h2{font-size:12px;color:var(--mut);letter-spacing:.1em;text-transform:uppercase;margin:22px 0 8px}.hv{display:flex;gap:8px;flex-wrap:wrap}.hv span{padding:3px 10px;border-radius:999px;font-size:12px;border:1px solid var(--ln)}.ok{color:var(--g);border-color:var(--g)!important}.ko{color:var(--r);border-color:var(--r)!important}</style></head><body>
<h1><span class="live" id="lv"></span>HARNAIS · FILE G · EN DIRECT</h1><div class="sub" id="sub">connexion…</div>
<div class="k"><div class="c"><b id="ka" style="color:var(--g)">–</b><span>agents actifs</span></div><div class="c"><b id="kt">–</b><span>agents terminés (ce LOT)</span></div><div class="c"><b id="kl" style="color:var(--y)">–</b><span>LOT actif</span></div><div class="c"><b id="kp" style="color:var(--b)">–</b><span>progression du LOT</span></div></div>
<div class="c big"><div id="lt"></div><div class="bar"><div class="fill" id="fl" style="width:0">0 %</div></div><div id="lm" class="sub"></div><div class="grid" id="gr"></div></div>
<h2>Consommation de tokens (calculée depuis les journaux, en direct)</h2><div class="c"><div id="tk" class="hv" style="margin-bottom:8px"></div><svg id="ch" viewBox="0 0 1000 230" width="100%"></svg><svg id="ch2" viewBox="0 0 1000 90" width="100%"></svg><div id="tr" class="sub"></div></div>
<h2>Équipe et règles</h2><div class="c"><div class="hv" id="eq"></div><div class="hv" id="vr" style="margin-top:8px"></div></div>
<h2>File G · 16 LOTS</h2><div class="c"><div class="grid" id="fg"></div></div>
<h2>Travail en cours</h2><div class="c"><div class="hv" id="dv"></div></div>
<h2>Agents</h2><div class="c"><table><thead><tr><th>Fonction</th><th>Tâche</th><th>LOT</th><th>Phase</th><th>État</th><th>Durée</th><th>Dernière activité</th></tr></thead><tbody id="tb"></tbody></table></div>
<h2>Harnais (veille 1 s)</h2><div class="hv" id="hv"></div>
<script>
const $=i=>document.getElementById(i),mm=s=>s==null?'–':s<60?s+' s':Math.floor(s/60)+' min '+s%60+' s';
function draw(d){const L=d.lot;$('ka').textContent=d.actifs;$('kt').textContent=d.termines;$('kl').textContent=L?'LOT_'+L.lot:'–';$('kp').textContent=L?L.pct+' %':'–';$('sub').textContent='mis à jour '+d.t+(window.SNAP?' · instantané (non live)':'');
if(L){$('lt').innerHTML='<b>LOT_'+L.lot+' · '+L.code+'</b> — '+L.nom;$('fl').style.width=Math.max(L.pct,4)+'%';$('fl').textContent=L.pct+' %';$('lm').textContent=L.ecrits+'/'+(L.N+1)+' fichiers écrits · '+L.audites+'/'+(L.N+1)+' audités (médical + conformité) · dépôt '+(L.depose?'fait':'à faire');
$('gr').innerHTML=L.fichiers.map(f=>'<div class="f '+(f.audite?'a':f.ecrit?'e':'w')+'"><b>'+(f.i=='A'?'Phase A':'DX.'+f.i)+'</b>'+(f.ecrit?f.ko+' Ko':'—')+(f.audite?' · ✔ audité':f.ecrit?' · écrit':'')+'</div>').join('')}
const T=d.tokens,DV=d.divers,k=n=>n>=1e6?(n/1e6).toFixed(2)+' M':n>=1e3?Math.round(n/1e3)+' k':n;
$('tk').innerHTML=['<span class="ok">sortie '+k(T.total.sortie)+'</span>','<span style="color:var(--b);border-color:var(--b)">entrée+écriture cache '+k(T.total.entree)+'</span>','<span>lecture cache '+k(T.total.cache)+'</span>','<span style="color:var(--o);border-color:var(--o)">débit '+k(T.debit_min)+'/min (sortie '+k(T.debit_sortie_min)+'/min)</span>'].join('');
(function(){const s=T.serie;if(s.length<2){$('ch').innerHTML='';return}const W=1000,H=230,m={l:54,r:12,t:12,b:22},t0=s[0][0],t1=s[s.length-1][0],mx=Math.max(...s.map(p=>Math.max(p[1],p[2])))*1.08||1,X=t=>m.l+(W-m.l-m.r)*(t-t0)/Math.max(1,t1-t0),Y=v=>m.t+(H-m.t-m.b)*(1-v/mx);
let g='';for(let i=0;i<=4;i++){const y=m.t+(H-m.t-m.b)*i/4;g+='<line x1="'+m.l+'" x2="'+(W-m.r)+'" y1="'+y+'" y2="'+y+'" stroke="#26305a"/><text x="'+(m.l-6)+'" y="'+(y+4)+'" text-anchor="end" fill="#8b96c9" font-size="10">'+k(mx*(1-i/4))+'</text>'}
const P=c=>s.map((p,i)=>(i?'L':'M')+X(p[0])+' '+Y(p[c])).join('');g+='<path d="'+P(2)+'" stroke="#5aa9ff" stroke-width="2.5" fill="none"/><path d="'+P(1)+'" stroke="#22d38a" stroke-width="2.5" fill="none"/><text x="'+(m.l+6)+'" y="'+(m.t+12)+'" fill="#22d38a" font-size="11">● sortie cumulée</text><text x="'+(m.l+120)+'" y="'+(m.t+12)+'" fill="#5aa9ff" font-size="11">● entrée cumulée</text><text x="'+(W-m.r)+'" y="'+(H-6)+'" text-anchor="end" fill="#8b96c9" font-size="10">'+new Date(t1*1000).toLocaleTimeString()+'</text><text x="'+m.l+'" y="'+(H-6)+'" fill="#8b96c9" font-size="10">'+new Date(t0*1000).toLocaleTimeString()+'</text>';$('ch').innerHTML=g;
const r=s.slice(1).map((p,i)=>[p[0],(p[1]-s[i][1])/Math.max(1,p[0]-s[i][0])*60]),rm=Math.max(...r.map(x=>x[1]),1);$('ch2').innerHTML='<text x="4" y="12" fill="#ffa94d" font-size="11">● débit de sortie (tokens/min)</text>'+r.map(x=>'<rect x="'+X(x[0])+'" y="'+(86-70*x[1]/rm)+'" width="3" height="'+(70*x[1]/rm)+'" fill="#ffa94d" opacity=".8"/>').join('')})();
$('tr').textContent='Par rôle (sortie / entrée) : '+Object.entries(T.par_role).map(([r,v])=>r+' '+k(v[0])+' / '+k(v[1])).join(' · ');
const E=DV.equipe;$('eq').innerHTML=(DV.sentinelle?'<span class="'+(DV.sentinelle.alertes.length?'ko':'ok')+'">sentinelle : '+(DV.sentinelle.alertes.length?DV.sentinelle.alertes.join(' | '):'effectifs conformes')+'</span>':'')+['<span class="'+(E.ok_redacteurs?'ok':'ko')+'">rédacteurs actifs '+E.redacteurs+' (cible jusqu'à 8)</span>','<span class="'+(E.ok_auditeurs?'ok':'ko')+'">auditeurs actifs '+E.auditeurs+' (cible 1–2)</span>','<span class="'+(DV.collision?'ko':'ok')+'">'+(DV.collision?'✘ COLLISION détectée':'✔ non-collision')+'</span>'].join('');
$('vr').innerHTML=(DV.verrous.length?DV.verrous.map(v=>'<span>🔒 '+v.agent+' · '+v.fichier.split('/').pop()+'</span>').join(''):'<span>aucun verrou actif</span>')+Object.entries(DV.lecons).map(([r,n])=>'<span class="'+(n<=5?'ok':'ko')+'">leçons '+r+' '+n+'/5</span>').join('');
$('fg').innerHTML=DV.file_g.map(l=>'<div class="f '+(l.verdict=='ACCEPTE'?'a':l.verdict?'ko':(d.lot&&l.lot==d.lot.lot)?'e':'w')+'"><b>LOT_'+l.lot+' · '+l.code+'</b>'+(l.verdict||((d.lot&&l.lot==d.lot.lot)?'ACTIF':'en attente'))+'</div>').join('');
$('dv').innerHTML=['<span>branche '+(DV.git?DV.git.branche:'–')+'</span>','<span>dernier commit '+(DV.git?DV.git.dernier:'–')+'</span>','<span>fichiers modifiés (non commités) '+(DV.git?DV.git.modifies:'–')+'</span>','<span>disque libre '+DV.disque_libre_go+' Go</span>','<span>volume écrit LOT '+(DV.ko_ecrits||0)+' Ko</span>','<span>veille tick '+(d.harnais?d.harnais.tick:'–')+'</span>'].join('');
const lot=L?'LOT_'+L.lot:'–';$('tb').innerHTML=d.agents.slice().sort((a,b)=>b.actif-a.actif).map(a=>'<tr><td><span class="t t-'+a.type+'">'+a.fonction+'</span></td><td>'+a.label+'</td><td>'+lot+'</td><td>'+a.phase+'</td><td class="st '+(a.actif?'on':'off')+'">'+(a.actif?'● actif':'terminé')+'</td><td>'+mm(a.depuis_s)+'</td><td>'+(a.actif?mm(a.derniere_activite_s):'')+'</td></tr>').join('');
$('hv').innerHTML=d.harnais?Object.entries(d.harnais.controles).map(([k,v])=>'<span class="'+(v?'ok':'ko')+'">'+(v?'✔ ':'✘ ')+k+'</span>').join(''):'<span class="ko">veille absente</span>'}
async function tick(){try{draw(await (await fetch('etat.json',{cache:'no-store'})).json())}catch(e){if(window.SNAP)draw(window.SNAP);else $('sub').textContent='serveur injoignable'}}
if(window.SNAP)draw(window.SNAP);else{tick();setInterval(tick,2000)}
</script></body></html>'''
class H(BaseHTTPRequestHandler):
    def do_GET(s):
        if s.path.startswith("/etat.json"): b = json.dumps(etat(), ensure_ascii=False).encode(); ct = "application/json"
        else: b = PAGE.encode(); ct = "text/html; charset=utf-8"
        s.send_response(200); s.send_header("Content-Type", ct); s.send_header("Cache-Control", "no-store"); s.end_headers(); s.wfile.write(b)
    def log_message(s, *a): pass
if __name__ == "__main__":
    if "--snapshot" in sys.argv:
        out = sys.argv[sys.argv.index("--snapshot") + 1]; Path(out).write_text(PAGE.replace("<script>", "<script>window.SNAP=" + json.dumps(etat(), ensure_ascii=False) + ";", 1), encoding="utf-8"); print(out)
    else: ThreadingHTTPServer(("0.0.0.0", int(sys.argv[1]) if len(sys.argv) > 1 else 8765), H).serve_forever()
