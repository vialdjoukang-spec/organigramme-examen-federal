import re,os,sys
AL=dict(SSC='w452516',AW='w603765',BU='w18dc8f',EQ='w649d13',KI='w045799',MO='w5e4677',ML='w6bfde2',S3='wf90eee',CO='w7d81c2',FU='w85d626',AN='wd994d6',WR='w81ae4d',HE='w2a7740',MS='w1e3e2a',MT='wf96001',PC='wac52bd',PL='w60d94c',WA='w8e2f69',DU='w81e9aa',DG='wdeace1',LP='w039ff8',ES='wff317b',PG='w78489d',SW='w0eb353',CE='w683a5c',DH='wdd3059',TH='w6fa1eb',VE='w0af5a7',TE='w4b0c96',IM='w741c90')
def idof(k):
    a,n=k.split(':')
    return f'aips-{n}' if a=='A' else f'{AL[a]}-{n}'
def rep(m):
    return ''.join(f'<sup class="r"><a href="#sb-{idof(k)}">{idof(k)}</a></sup>' for k in m.group(1).split(','))
here=os.path.dirname(os.path.abspath(__file__))
os.makedirs(here+'/fragments',exist_ok=True)
for n in range(1,15):
    f=f'{here}/s/p{n:02d}.html'
    if os.path.exists(f):
        t=open(f,encoding='utf-8').read()
        t=re.sub(r'\{([A-Z0-9]+:[0-9\-]+(?:,[A-Z0-9]+:[0-9\-]+)*)\}',rep,t)
        t=t.replace('<div class="t">','<div class="t" style="overflow-x:auto">')
        open(f'{here}/fragments/p{n:02d}.html','w',encoding='utf-8').write(t)
