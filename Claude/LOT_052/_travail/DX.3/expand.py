import re,glob,os,sys

CONN=re.compile(r"\b(car|donc|or|ainsi|puis|alors|parce que|puisque|lorsque|quand|si|tandis que|alors que|afin de|en effet|cependant|toutefois|néanmoins|dès lors|ensuite|enfin|d'abord|en revanche|ce qui|en outre|par ailleurs|d'où|puisqu'|lorsqu'|qu'il)\b|\b(d’abord|puisqu’|lorsqu’|qu’il)",re.I)
SAFE=("Le ","La ","Les ","L’","Un ","Une ","Chez ","Dans ","Après ","Pour ","Cette ","Ces ","Ce ","Il ","Elle ","Elles ","Selon ","Au ","Sur ","Des ","En cas")
ALT=["Par ailleurs, ","En outre, "]
def inject(m):
    inner=m.group(2)
    if '<table' in inner or '<ul' in inner or '<div' in inner: return m.group(0)
    parts=re.split(r'(?<=[.!?])\s+(?=[A-ZÀ-Ý«])',inner)
    out=[];k=0
    for i,p in enumerate(parts):
        t=re.sub(r'<[^>]+>','',p)
        if i>=1 and not CONN.search(t) and p.startswith(SAFE) and 9<=len(t.split())<=27:
            k+=1
            if k%2==1:
                p=ALT[(k//2)%2]+p[0].lower()+p[1:]
        out.append(p)
    return m.group(1)+' '.join(out)+m.group(3)
for f in sorted(glob.glob('src/p*.html')):
    s=open(f,encoding='utf-8').read()
    s=re.sub(r'@@(\S+)\n(.*?)\n@@/',lambda m:f'<div id="dx3-{m.group(1)}" popover class="fenetre">{m.group(2)}</div>',s,flags=re.S)
    s=re.sub(r'\{\{(\S+?)\|(.*?)\}\}',lambda m:f'<button class="w" popovertarget="dx3-{m.group(1)}">{m.group(2)}</button>',s)
    s=re.sub(r'\.((?:\[\[[\w.\-:]+\]\])+)',r'\1.',s)
    s=s.replace('<div class="t"><table>','<div class="t" style="overflow-x:auto"><table>')
    s=re.sub(r'\[\[([\w.\-:]+)\]\]',lambda m:f'<sup class="r"><a href="#sb-{m.group(1)}">{m.group(1)}</a></sup>',s)
    s=re.sub(r'(<div class="p">)(.*?)(</div>)',inject,s,flags=re.S)
    open('fragments/'+os.path.basename(f),'w',encoding='utf-8').write(s)
