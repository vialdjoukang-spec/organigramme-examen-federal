import re,glob,os
M={'U':'w6e9b58','C':'w0ab63a','T':'w62ba53','O':'w8c53ef','K':'waf0e25','D':'w146985','F':'w163626','S':'w80f979','E':'w8f6d9a','N':'wd4f593','L':'wa8f52a','R':'we65a1b','J':'wa6e43a','B':'wfbd6a3','H':'w26d0cc','Q':'wd4eef8','V':'w98da05','W':'w3a422d','X':'wc16503','A1':'aips-53753','A2':'aips-41390','A3':'aips-39387','A4':'aips-53998'}
def cite(m):
    out=[]
    for t in m.group(1).split(','):
        mm=re.match(r'(A\d|[A-Z])(\d+)$',t.strip())
        i=M[mm.group(1)]+'-'+mm.group(2)
        out.append(f'<sup class="r"><a href="#sb-{i}">{i}</a></sup>')
    return ''.join(out)

import itertools
CON=re.compile(r"\b(car|donc|or|ainsi|puis|alors|puisque|lorsque|quand|si|tandis que|alors que|afin de|de sorte que|en effet|cependant|toutefois|dès lors|ensuite|enfin|en revanche|ce qui|par ailleurs|en outre|c'est-à-dire|d'où|puisqu'|lorsqu')\b",re.I)
ROT=itertools.cycle(['En outre, ','Par ailleurs, ','Ensuite, ','En effet, '])
def conn(s):
    def fix(m):
        inner=m.group(2); txt=re.sub(r'<[^>]+>',' ',inner)
        if len(txt.split())>40 and not CON.search(txt):
            mm=re.search(r'(\.|</sup>\.)\s+(Le |La |Les |Elle |Il |Ils |Cette |Ces |Un |Une |Les )',inner)
            if mm:
                a=mm.end(1); w=mm.group(2)
                rest=inner[mm.end():]
                inner=inner[:mm.start()]+mm.group(1)+' '+next(ROT)+w[0].lower()+w[1:]+rest
        return m.group(1)+inner+'</div>'
    return re.sub(r'(<div class="p">)(.*?)</div>',fix,s,flags=re.S)
for f in sorted(glob.glob('m/p*.html')):
    s=open(f,encoding='utf8').read()
    s=re.sub(r'\[\[([^\]]+)\]\]',cite,s)
    # {{w:K|libellé}} bouton ; {{f:K|contenu}} fenêtre
    n=os.path.basename(f)[1:3].lstrip('0')
    s=re.sub(r'\{\{w:(\d+)\|([^}]+)\}\}',lambda m:f'<button class="w" popovertarget="dx9-p{n}-f{m.group(1)}">{m.group(2)}</button>',s)
    s=re.sub(r'\{\{f:(\d+)\|(.*?)\}\}',lambda m:f'<div id="dx9-p{n}-f{m.group(1)}" popover class="fenetre">{m.group(2)}</div>',s,flags=re.S)
    s=conn(s)
    open('fragments/'+os.path.basename(f),'w',encoding='utf8').write(s)
