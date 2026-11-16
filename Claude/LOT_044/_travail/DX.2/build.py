#!/usr/bin/env python3
# expansion des citations abrégées {e86,t9,a60140-5} -> <sup class="r">…
import re,os,glob
PRE={'e':'esc24-','t':'w75f58a-','r':'we00180-','n':'w93658b-','h':'wfba9d7-','c':'w302bd2-','a':'aips-'}
def sup(m):
    out=''
    for k in m.group(1).split(','):
        k=k.strip(); i=PRE[k[0]]+k[1:]
        out+=f'<sup class="r"><a href="#sb-{i}">{i}</a></sup>'
    return out
for f in sorted(glob.glob('src/p*.html')):
    s=open(f,encoding='utf-8').read()
    s=re.sub(r'([.!?])\s*(\{[eatrnhc][\w\-,\s]*\})',lambda m:m.group(2)+m.group(1),s)
    s=re.sub(r'\{([eatrnhc][\w\-]*(?:,\s*[eatrnhc][\w\-]*)*)\}',sup,s)
    open('fragments/'+os.path.basename(f),'w',encoding='utf-8').write(s)
