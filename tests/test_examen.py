# Asclépios · contrôles de l'examen physique (structure GES, ordre des phases, renvois, croquis, champ 5 de TIP).
# Sortie : JSON de contrôles booléens + 'errors'. Variables : APP_FILE, CHROME_PATH.
import asyncio, json, os, sys
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
APP=os.path.abspath(os.environ.get('APP_FILE',os.path.join(ROOT,'app_v2.html')))
CHROME=os.environ.get('CHROME_PATH') or None
from playwright.async_api import async_playwright
CRED=json.load(open(os.path.join(ROOT,'assets/cs/credits.json')))
STATIC=r"""(()=>{const R={},O={'Inspection':1,'Palpation':2,'Percussion':3,'Auscultation':4};
R.axes_trois=GES.every(r=>['reg','sys','pop'].includes(r.ax))&&['reg','sys','pop'].every(a=>GES.some(r=>r.ax===a));
const K=GES.flatMap(r=>r.items.map(i=>i.k));R.cles_uniques=K.length===new Set(K).size&&K.every(Boolean);
R.cles_historiques=Array.from({length:0}).length===0&&['constantes','peau','tete-cou','thorax','coeur-vaisseaux','seins','abdomen','tr-genital','rachis','epaule','coude-main','hanche','genou','cheville-pied','neuro-nc','neuro-moteur','meninge-gcs','pediatrie','geriatrie','psychiatrie'].every(id=>K.some(k=>k===id+'_0'));
let bad=[];GES.filter(r=>r.ax!=='pop').forEach(r=>{const g={};r.items.forEach(it=>{(g[it.sr||'']=g[it.sr||'']||[]).push(it)});Object.values(g).forEach(L=>{let mx=0,seenIP=false;const ab=r.id==='abdomen'?{'Inspection':1,'Auscultation':2,'Percussion':3,'Palpation':4}:O;L.forEach(it=>{const v=ab[it.p];if(v){if(v<mx)bad.push(r.id+':'+it.s);mx=Math.max(mx,v)}if(it.p==='Mobilisation'&&mx<2&&L.some(x=>x.p==='Palpation'))bad.push(r.id+':'+it.s)})})});R.ordre_phases=bad.length===0;if(bad.length)R._bad=bad;
R.renvois_resolus=GES.every(r=>r.items.every(it=>!it.x||it.x.every(([rid,s])=>{const g=GES.find(x=>x.id===rid);return g&&g.items.some(i=>i.s===s)})));
R.renvois_bidirectionnels=GES.every(r=>r.items.every(it=>!it.x||it.x.every(([rid,s])=>GES.find(x=>x.id===rid).items.find(i=>i.s===s).x.some(([a,b])=>a===r.id&&b===it.s))));
R.nouveaux_sources=GES.every(r=>r.items.every(it=>!/_n\d+$/.test(it.k)||(it.src&&it.av)));
const T=Object.values(TIP).filter(t=>t.c.length>5);let tb=0,tc=0;const SEQ='0M123456N',SA='0M14325 6N'.replace(' ','');
T.forEach(t=>{const s=t.c[5];if(s[0]!=='§')return;let reg='',last=-1;s.split('\n').forEach(l=>{if(l[0]==='§'){reg=l.slice(1);last=-1}else if(l[0]==='¶'){const q=(reg==='abdomen'?'0M1432 56N'.replace(' ',''):SEQ).indexOf(l[1]);if(q<=last)tb++;last=q}else if(l[0]==='@'){l.slice(1).split(' ').filter(Boolean).forEach(x=>{if(x.startsWith('r:')?!GES.some(g=>g.id===x.slice(2)):!K.includes(x))tc++})}})});
R.tip_ordre_phases=tb===0;R.tip_puces_resolues=tc===0;
R.tip_vides_marques=T.filter(t=>!t.c[5].replace(/<[^>]+>/g,'').trim()).length===0;R.s8_differentiels=[1,2,3,4,5,6,7,8,9,10,11,12].every(n=>{const k='S8.'+n;return NOT[k][0].length>=5&&TIP[k].d.length===NOT[k][0].length&&TIP[k].d.every(x=>x.replace(/<[^>]+>/g,'').length>=150)&&!/• &lt;<br>• p<br>/.test(TIP[k].c[12]+TIP[k].c[13])});R.tip_sans_a_completer=T.every(t=>!t.c[5].startsWith('À compléter'));R.tip_autres_rediges=T.every(t=>{const s=t.c[5],i=s.indexOf('§autres');if(i<0)return true;const j=s.indexOf('\n§',i+1);return s.slice(i,j<0?undefined:j).split('\n').filter(l=>l.startsWith('• ')).every(l=>/^• <b>[^<]+<\/b> : .{12,}[.!?]$/.test(l))});
return R})()"""
async def main():
  out={};errs=[]
  async with async_playwright() as p:
    b=await p.chromium.launch(args=['--no-sandbox'],**({'executable_path':CHROME} if CHROME else {}))
    pg=await (await b.new_context(viewport={'width':1280,'height':900})).new_page()
    pg.on('pageerror',lambda e:errs.append(str(e)))
    await pg.goto('file://'+APP);await pg.wait_for_timeout(1500)
    st=await pg.evaluate(STATIC);bad=st.pop('_bad',None)
    if bad: errs.append('ordre : '+', '.join(bad[:6]))
    out.update(st)
    figs={r for r in await pg.evaluate("GES.filter(r=>r.fig).map(r=>r.fig.f)")}
    names={c['fichier'] for c in CRED['images']}
    out['croquis_credites']=figs<=names and all(os.path.getsize(os.path.join(ROOT,f))<=200*1024 for f in figs)
    await pg.click('.tab[data-v=ges]');await pg.wait_for_timeout(300)
    await pg.click('#g-reg [data-r=abdomen]');await pg.wait_for_timeout(300)
    out['gestes_sections_phases']=await pg.evaluate("document.querySelectorAll('#g-list .ex-region .ex-phase').length>=4&&!!document.querySelector('#g-list .ex-fig img[loading=lazy]')")
    out['croquis_charge']=await pg.evaluate("new Promise(r=>{const i=document.querySelector('#g-list .ex-fig img');i.loading='eager';if(i.complete&&i.naturalWidth)return r(true);i.onload=()=>r(i.naturalWidth>0);i.onerror=()=>r(false);setTimeout(()=>r(false),4000)})")
    await pg.click('#g-list .ex-chip[data-gx^="vasc|"]');await pg.wait_for_timeout(400)
    out['renvoi_navigue']=await pg.evaluate("GREG==='vasc'&&!!document.querySelector('#g-list .ex-flash')")
    await pg.mouse.move(1,1)
    await pg.evaluate("(()=>{const e=document.createElement('span');e.dataset.t='n|G1|c5';document.body.appendChild(e);showTip(e,true);e.style.display='none'})()")
    await pg.wait_for_timeout(200)
    out['tip_regions_rendues']=await pg.evaluate("document.querySelectorAll('#tip .ex-region .ex-region__h').length>=2&&document.querySelectorAll('#tip .ex-chip').length>=1")
    await pg.evaluate("document.querySelector('#tip .ex-chip').click()");await pg.wait_for_timeout(400)
    out['tip_puce_navigue']=await pg.evaluate("document.querySelector('.tab[data-v=ges]').getAttribute('aria-selected')==='true'&&document.getElementById('tip').hidden&&GREG==='constantes'")
    await b.close()
  out['errors']=errs
  print(json.dumps(out,ensure_ascii=False))
asyncio.run(main())
