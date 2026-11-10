import re,sys,glob
for f in glob.glob('/home/user/wt/lot-053/Claude/LOT_053/_travail/DX.1/fragments/p*.html'):
    s=open(f,encoding='utf8').read()
    s=re.sub(r'\.(<sup class="r">(?:<a [^>]*>[^<]*</a>)+</sup>)',r'\1.',s)
    open(f,'w',encoding='utf8').write(s)
