import os, sys
# Patch 0020 · Asclépios · 17.10.2026 · fréquence (prévalence) de chaque diagnostic différentiel.
# PRV (JSON strict, écrit par tools/prev_build.py depuis data/ck/prev.json) : par SSP, la liste [index, %, opérateur]
# dans l'ordre d'affichage (chiffres sourcés en ordre décroissant, puis « % à vérifier » par probabilité clinique).
# L'index d'origine reste la clé ('d'+i) : la progression enregistrée de l'utilisateur ne bouge pas.
# Le pourcentage s'affiche en rouge (classe .pv) à côté du diagnostic, dans la liste et dans la fenêtre du diagnostic ;
# son survol ouvre pv|SSP|i : cadre, type de chiffre, source et date de lecture (assets/ck/prev.js, chargé à l'inactivité).
p = os.environ.get('APP_FILE') or sys.exit('Indiquez APP_FILE (copie de travail).')
assert not p.endswith('orig/app.html'), 'Interdit I1'
s = open(p, encoding='utf-8').read()

def rep(a, b):
    global s
    assert s.count(a) == 1, 'Ancrage absent ou répété : ' + a[:60]
    s = s.replace(a, b)

LEG = ('<p class="pvleg">Le pourcentage en rouge donne la fréquence du diagnostic chez les patients qui consultent pour cette plainte, '
       'dans le cadre indiqué (médecine de famille ou urgences, en Suisse ou en Europe). Une prévalence dans la population générale '
       'ne sert qu’à défaut, et elle porte alors la mention « population ». Ouvrez le diagnostic, puis survolez ou touchez son pourcentage pour lire '
       'le cadre, la source et sa date de lecture. Les diagnostics sont classés par fréquence décroissante ; « % à vérifier » signale qu’aucune '
       'source suisse ou européenne n’a encore été lue, et ces diagnostics suivent, dans l’ordre de leur probabilité clinique.</p>')

rep('</head>',
    '<style>.pv{color:var(--bad);font:700 .86rem var(--fb);margin-left:.4em;white-space:nowrap}.pv[data-t]{display:inline-block;min-width:24px;min-height:24px;line-height:24px;padding:0 3px;cursor:help;text-decoration:underline dotted;text-underline-offset:3px}'
    '.pv.av{font-weight:600;font-style:italic}.pv small{color:var(--mut);font-weight:500;font-style:normal}'
    '.pvleg{margin:4px 2px 8px;color:var(--ink);font-size:.76rem;line-height:1.4;text-align:justify}.pvl{margin:0 0 6px}</style></head>')

rep('const NLAB=[',
    'const PRV={};\n'
    "const PV_LEG='" + LEG.replace("'", "\\'") + "';\n"
    "function pvOf(c,i){const P=PRV[c];return P?P.find(x=>x[0]===i)||null:null}\n"
    "function pvFmt(x){if(!x||x[1]==null)return '% à vérifier';return (x[2]?x[2]+' ':'')+String(x[1]).replace('.',',')+' %'+(x[3]?' <small>population</small>':'')}\n"
    "function pvSpan(c,i,act){const x=pvOf(c,i);return `<span class=\"pv${x&&x[1]!=null?'':' av'}\"${act?` data-t=\"pv|${c}|${i}\" tabindex=\"0\" role=\"button\"`:''}>${pvFmt(x)}</span>`}\n"
    "function pvLine(c,i){const e=((ckW('PREV')||{})[c]||{})[i];return `<p class=\"pvl\"><b>Fréquence</b> : ${pvSpan(c,i,1)}${e&&e.cadre?' · '+esc(e.cadre)+'.':' · survolez ou touchez le pourcentage pour lire le cadre et la source.'}</p>`}\n"
    'const NLAB=[')

rep("N[0].forEach((t,i)=>o.push({k:'d'+i,s:'2 · Diagnostics différentiels',t}));",
    "(PRV[c]?PRV[c].map(x=>x[0]):N[0].map((t,i)=>i)).forEach(i=>o.push({k:'d'+i,s:'2 · Diagnostics différentiels',t:N[0][i],pv:pvSpan(c,i)}));")

rep('${n.sub?`<small>', "${n.pv||''}${n.sub?`<small>")

rep('<div class="nl">${R.map(n=>nRow(c,n))', '<div class="nl">${k[0]===\'2\'&&R.length?PV_LEG:\'\'}${R.map(n=>nRow(c,n))')

rep("h=T.d[i];src=T.s;if(MO)return {hd:'Monographie · '+a,ti:dn,h:MO.h,", "h=pvLine(a,i)+T.d[i];src=T.s;if(MO)return {hd:'Monographie · '+a,ti:dn,h:pvLine(a,i)+MO.h,")

rep('CK_DEP={glo:', "CK_DEP={pv:['prev','src'],glo:")

rep("if(!ckNeed(ty,a,key))return ckWait({syn:'Syndrome',hyp:'Exploration',loc:'Synthèse locale',nc:'Schéma'}[ty]);",
    "if(ty==='pv'){const nm=(NOT[a]||[[]])[0][+b]||'',H='Fréquence du diagnostic · '+a;if(!PRV[a])return {hd:H,ti:nm,h:'<p>Aucune fréquence n’est encore sourcée pour les diagnostics de ce SSP : chaque pourcentage reste <b>à vérifier</b>, et l’ordre suit encore la rédaction d’origine.</p>'};"
    "if(!ckNeed(ty,a,key))return ckWait(H,nm);const e=((ckData('PREV')||{})[a]||{})[b];if(!e)return null;const x=pvOf(a,+b),S=e.src?(ckData('SRC')||{})[e.src]:null;"
    "return {hd:H,ti:nm,h:(x&&x[1]!=null?`<p><span class=\"pv\">${pvFmt(x)}</span> ${e.type==='population'?'de la population générale : aucune donnée par motif de consultation n’a été trouvée.':'des patients qui consultent pour cette plainte.'}</p>`:'<p><span class=\"pv av\">% à vérifier</span> : aucune source suisse ou européenne n’a encore été lue pour ce chiffre ; le rang suit la probabilité clinique.</p>')"
    "+(e.cadre?`<p><b>Cadre</b> : ${esc(e.cadre)}.</p>`:'')+(S?`<p><b>Source</b> : ${S.url?`<a href=\"${esc(S.url)}\" target=\"_blank\" rel=\"noopener\">${esc(S.titre)}</a>`:esc(S.titre)} (${esc(S.org)})${e.loc?', '+esc(e.loc):''}, lue le ${ckDate(e.date_lu)}.</p>`:'')+(e.note?`<p>${esc(e.note)}</p>`:'')}}\n "
    "if(!ckNeed(ty,a,key))return ckWait({syn:'Syndrome',hyp:'Exploration',loc:'Synthèse locale',nc:'Schéma'}[ty]);")

# Chargement de prev.js et src.js à l'ouverture d'une fiche de Notions CK seulement (rien de plus au démarrage : CLS de l'accueil inchangé).
rep("function nBlock(c,compact){const s=BY[c];if(!s)return '';", "function nBlock(c,compact){const s=BY[c];if(!s)return '';if(PRV[c]&&typeof ckLoad==='function'){ckLoad('prev').catch(()=>{});ckLoad('src').catch(()=>{})}")

open(p, 'w', encoding='utf-8').write(s)
print('0020 appliqué')
