import re,glob
for f in glob.glob('/home/user/wt/lot-053/Claude/LOT_053/_travail/DX.1/fragments/p*.html'):
    s=open(f,encoding='utf8').read()
    # split multi-anchor sups
    def split(m):
        anchors=re.findall(r'<a [^>]*>[^<]*</a>',m.group(0))
        return ''.join('<sup class="r">'+a+'</sup>' for a in anchors)
    s=re.sub(r'<sup class="r">(?:<a [^>]*>[^<]*</a>){2,}</sup>',split,s)
    s=re.sub(r'\.((?:<sup class="r"><a [^>]*>[^<]*</a></sup>)+)',r'\1.',s)
    s=s.replace('<div class="t"><table>','<div class="t" style="overflow-x:auto;"><table>')
    open(f,'w',encoding='utf8').write(s)
