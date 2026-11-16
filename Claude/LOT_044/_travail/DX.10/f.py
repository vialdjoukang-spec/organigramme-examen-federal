import sys,json,re
sys.argv.pop(0)
exec(open('build_frag.py').read().split("def esc(s):")[0].replace('D = os.path.dirname(os.path.abspath(__file__))','D="."'))
a=sys.argv[0]; kw=norm(sys.argv[1]); w=int(sys.argv[2]) if len(sys.argv)>2 else 160
for i,t in NP:
    if i.startswith(ALIAS[a]+'-') and kw in t:
        k=t.index(kw); print(i,'…'+t[max(0,k-w//3):k+w]+'…\n')
