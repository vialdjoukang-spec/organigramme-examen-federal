import re,glob,os
AL={'sfe':'w716338','hp':'w04c5a2','hg':'wc26608','jb':'w5d6de5','ih':'w17a045','ob':'wa3c27f','ft':'wa5f3f2','g4':'w27ceb5','sg':'wcc4907','hv':'w6a0434','in':'w318537','en':'w33eada',
'gg':'aips-31489','bq':'aips-67465','gc':'aips-65441','nr':'aips-55045','hm':'aips-44610','hb':'aips-51750','gl':'aips-57611','g2':'aips-65967','sh':'w15c467','g40':'aips-29550719','g10':'aips-29550190','g20':'aips-29550212'}
def cid(x):
    x=x.strip(); a,n=x.rsplit('-',1)
    return AL[a]+'-'+n
def rep(m):
    return ''.join(f'<sup class="r"><a href="#sb-{cid(i)}">{cid(i)}</a></sup>' for i in m.group(1).split(','))
for f in sorted(glob.glob('src/p*.html')):
    t=open(f,encoding='utf-8').read()
    t=re.sub(r'\.\[\[([^\]]+)\]\]',lambda m: rep(m)+'.',t)
    t=re.sub(r'\[\[([^\]]+)\]\]',rep,t)
    open('fragments/'+os.path.basename(f),'w',encoding='utf-8').write(t)
