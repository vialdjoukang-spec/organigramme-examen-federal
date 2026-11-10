import re,json,glob,os,sys
D=os.path.dirname(os.path.abspath(__file__))
A={'H':'w87388a','R':'wfcbcb1','G':'wd01433','P':'w7aeb74','A':'wb601d8','A2':'wc16be7','M':'w3dcc88','B':'w1730ea','F':'aips-57851','N':'aips-67001','V':'aips-15398','T':'aips-37448','C':'aips-21672','CO':'aips-68216','FO':'aips-36752'}
ids={p['id'] for p in json.load(open(D+'/paquet.json'))['passages']}
def rep(m):
    out=''
    for tok in m.group(1).split(','):
        al,n=tok.strip().split(':'); i=A[al]+'-'+n
        if i not in ids: print('ID INCONNU',i); sys.exit(1)
        out+=f'<sup class="r"><a href="#sb-{i}">{i}</a></sup>'
    return out
for f in sorted(glob.glob(D+'/src/p*.html')):
    t=open(f).read()
    t=re.sub(r'\{([A-Z0-9]+:\d+(?:,\s*[A-Z0-9]+:\d+)*)\}',rep,t)
    open(D+'/fragments/'+os.path.basename(f),'w').write(t)
print('ok')
