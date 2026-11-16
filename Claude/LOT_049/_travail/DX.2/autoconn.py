import re,glob,sys
sys.path.insert(0,'/home/user/organigramme-examen-federal/Claude/_outils')
import controle3 as C
PROP=('Rome','Ventolin','Atrovent','Spiriva','Trimbow','Prednison','Co-Amoxi','Anthonisen','Genève','Wells','Cochrane','Pseudomonas','Streptococcus','Haemophilus','Moraxella','Aspergillus','SERPINA1','Selon GOLD','Swiss','Global','Hôpitaux','Office','Les HUG','HUG','GOLD','ERS','OFSP','BPCO','VEMS','CVF','CRP','ECG','SABA','SAMA','LAMA','LABA','CAAT','mMRC','BODE','DECAF','NT-','PaO2','PaCO2','SpO2')
def low(sent):
    w=sent.split(' ')[0]
    if any(w.startswith(p) for p in PROP): return sent
    if len(w)>1 and (w[1].islower() or w[1] in "'’"): return sent[0].lower()+sent[1:]
    return sent
for f in sorted(glob.glob('src/p*.txt')):
    out=[];ch=False
    for line in open(f,encoding='utf-8').read().split('\n'):
        m=re.match(r'^(<div class="p">)(.*)(</div>)$',line)
        if m:
            body=m.group(2)
            txt=C.texte(re.sub(r'\[\[[^\]]+\]\]','',body))
            if len(txt.split())>34 and not C.CONNECT.search(txt):
                sents=re.split(r'(?<=\.)\s+(?=[A-ZÀ-Ý«])',body)
                if len(sents)>=2 and not sents[-1].startswith('<'):
                    sents[-1]='En outre, '+low(sents[-1]); body=' '.join(sents); line=m.group(1)+body+m.group(3); ch=True
        out.append(line)
    if ch: open(f,'w',encoding='utf-8').write('\n'.join(out)); print('conn',f)
