import os, sys, json
# Patch 0004 · Thémis · 17.10.2026 · onglet « Exigences » 2027 : constantes SESSION et EXI (JSON strict, data/*.json),
# 46 cases à identifiant stable, migration des clés e0…e15, bandeau 2027 et badges « À vérifier auprès de la MEBEKO ».
# Se rejoue après 0001 à 0003 sur une copie (APP_FILE). Chaque ancrage doit apparaître une seule fois.
p = os.environ.get('APP_FILE') or sys.exit('Indiquez APP_FILE (copie de travail).')
assert not p.endswith('orig/app.html'), 'Interdit I1'
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
s = open(p, encoding='utf-8').read()
J = lambda n: json.dumps(json.load(open(os.path.join(ROOT, 'data', n + '.json'), encoding='utf-8')), ensure_ascii=False, separators=(',', ':'))

def rep(a, b):
    global s
    assert s.count(a) == 1, ('ancrage', a[:60], s.count(a))
    s = s.replace(a, b)

# 1. Données : l’ancien tableau EXI (16 points indexés) devient SESSION + EXI en JSON strict.
i = s.find('const EXI=[\n'); j = s.find('\n];\nconst $=s=>', i)
assert i > 0 and j > i and s.count('const EXI=[\n') == 1
s = s[:i] + 'const SESSION=' + J('SESSION') + ';\nconst EXI=' + J('EXI') + ';' + s[j + 3:]

# 2. Style (dans le style de head, comme #bak).
rep('.bak{display:flex', (
 '.exi-bn{padding:12px 14px;border:1px solid var(--line);border-left:4px solid var(--gold);border-radius:10px;background:var(--paper);margin:0 0 14px}'
 '.exi-bn p{margin:4px 0}.exi-bn .cd{font-weight:700}#exi fieldset{border:1px solid var(--line);border-radius:10px;margin:0 0 14px;padding:4px 14px 8px}'
 '#exi legend{font-weight:700;padding:0 6px}#exi legend small{font-weight:400;color:var(--mut)}'
 '.vb{display:inline-block;margin-left:6px;padding:1px 8px;border-radius:999px;background:#fde8c8;color:#6b3a00;border:1px solid #c77700;font-size:.78rem;font-weight:600;white-space:nowrap}'
 '.exi-n{display:block;color:var(--mut);font-style:italic}\n.bak{display:flex'))

# 3. Bandeau et conteneur.
rep('<div class="card"><h2>Ce qu’il faut réunir et savoir</h2><p class="st">Chaque point cite sa source officielle. Cochez au fur et à mesure : l’état est conservé.</p><div id="exi"></div></div>',
    '<div class="card"><h2>Inscription à l’examen fédéral 2027 · diplôme hors UE/AELE</h2><div class="exi-bn" id="exi-bn" role="region" aria-label="Session 2027"></div>'
    '<p class="st">Ce parcours vise le titulaire d’un diplôme hors UE/AELE dont la décision MEBEKO ouvre l’accès à l’examen fédéral. Chaque point cite sa source officielle, et chaque point non confirmé porte le badge « À vérifier auprès de la MEBEKO ». Vos coches restent dans ce navigateur. Le format de l’examen figure dans l’onglet « Attendus ».</p>'
    '<p class="st" id="exi-c" role="status"></p><div id="exi"></div></div>')

# 4. Rendu, migration et enregistrement.
i = s.find('function renderExi(){'); j = s.find('\n', i)
s = s[:i] + r"""const fdt=d=>d.split('-').reverse().join('.');
function exiMig(){const x=S.exi||(S.exi={});if(x._m27)return false;let any=false;EXI.items.forEach(it=>(it.m||[]).forEach(k=>{if(k in x){any=true;if(x[k]&&!('x:'+it.id in x))x['x:'+it.id]=true}}));if(any)x._m27=1;return any}
function exiBanner(){const I=SESSION.inscription,P=SESSION.precedente,d0=new Date(I.debut+'T00:00:00'),d1=new Date(I.fin+'T23:59:59'),now=new Date(),j=t=>Math.ceil((t-now)/864e5);
 const cd=now<d0?'L’inscription ouvre dans '+j(d0)+' jours, le '+fdt(I.debut)+'.':now<=d1?'L’inscription se ferme dans '+j(d1)+' jours, le '+fdt(I.fin)+'.':'La période d’inscription 2027 est close depuis le '+fdt(I.fin)+'.';
 return '<p><b>La session '+P.annee+' est terminée</b> : le CK a eu lieu les '+fdt(P.ck[0])+' et '+fdt(P.ck[1])+', et le CS du '+fdt(P.cs[0])+' au '+fdt(P.cs[1])+' (<a href="'+P.url+'" target="_blank" rel="noopener">'+esc(P.ref)+'</a>).</p>'
 +'<p>L’inscription à l’examen '+SESSION.annee+' est ouverte du <b>'+fdt(I.debut)+'</b> au <b>'+fdt(I.fin)+'</b> (<a href="'+I.url+'" target="_blank" rel="noopener">'+esc(I.source)+'</a>). <span class="cd" id="exi-cd">'+cd+'</span></p>'
 +'<p>Le CK aurait lieu les '+fdt(SESSION.ck.dates[0])+' et '+fdt(SESSION.ck.dates[1])+', et le CS entre le '+fdt(SESSION.cs.debut)+' et le '+fdt(SESSION.cs.fin)+' ; ces dates sont <b>à confirmer</b>, car seule une <a href="'+SESSION.dates_source.url+'" target="_blank" rel="noopener">source facultaire</a> les annonce et l’OFSP ne les a pas publiées. <span class="vb">À vérifier auprès de la MEBEKO</span></p>'}
function renderExi(){if(exiMig())put('reglages','exigences',S.exi);const x=S.exi;$('#exi-bn').innerHTML=exiBanner();
 $('#exi').innerHTML=Object.entries(EXI.groupes).map(([g,lab])=>{const L=EXI.items.filter(it=>it.g===g);return '<fieldset><legend>'+esc(lab)+' <small>('+L.filter(it=>x['x:'+it.id]).length+'/'+L.length+')</small></legend>'+L.map(it=>`<label class="chk" data-s="${it.s}"><input type="checkbox" id="exi-${it.id}" data-x="${it.id}" ${x['x:'+it.id]?'checked':''}><span><b>${it.id}</b> · ${esc(it.t)}${it.s==='a_verifier'?'<span class="vb">À vérifier auprès de la MEBEKO</span>':''}${it.n?'<span class="exi-n">'+esc(it.n)+'</span>':''}</span><small>Source officielle : <a href="${it.u}" target="_blank" rel="noopener">${esc(it.r)}</a>${it.e?' · Échéance : '+fdt(it.e):''}</small></label>`).join('')+'</fieldset>'}).join('');
 const n=EXI.items.filter(it=>x['x:'+it.id]).length,v=EXI.items.filter(it=>it.s==='a_verifier').length;$('#exi-c').textContent=n+' points sur '+EXI.items.length+' sont cochés ; '+v+' points restent à vérifier auprès de la MEBEKO (sources lues le '+fdt(EXI.lu)+').'}""" + s[j:]
rep("$('#exi').addEventListener('change',e=>{const i=e.target.dataset.i;if(i==null)return;S.exi['e'+i]=e.target.checked;put('reglages','exigences',S.exi)});",
    "$('#exi').addEventListener('change',e=>{const k=e.target.dataset.x;if(!k)return;S.exi._m27=1;S.exi['x:'+k]=e.target.checked;put('reglages','exigences',S.exi);renderExi();const f=document.getElementById('exi-'+k);if(f)f.focus()});")

# 5. Dates : l’onglet Calculs ne présente plus 2026 comme à venir ; la date CK par défaut suit SESSION.
i = s.find('<p class="st">Dates 2026 de référence'); j = s.find('</p>', i) + 4
s = s[:i] + '<p class="st">La session 2026 est terminée. Pour 2027, la faculté de Genève annonce sous réserve le CK les 10 et 12 août et le CS entre le 6 et le 10 septembre ; ces dates restent à confirmer par l’OFSP (voir l’onglet « Exigences »).</p>' + s[j:]
rep('exam:"2027-08-03"', 'exam:"2027-08-10"')
open(p, 'w', encoding='utf-8').write(s)
print('0004 appliqué.')
