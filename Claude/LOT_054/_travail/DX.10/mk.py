import re,sys,glob,os
AL=dict(
E24a='w47f9f5-12',E24b='w47f9f5-13',E19a='w795426-5',E19b='w795426-6',IOTA='w0e3adc-6',
N1='w05e6f4-14',N2='w05e6f4-15',N3='w05e6f4-16',N4='w05e6f4-17',N5='w05e6f4-18',N6='w05e6f4-19',N7='w05e6f4-20',N8='w05e6f4-21',N9='w05e6f4-23',
LC='w51201b-27',LC1='w51201b-1',LC8='w51201b-8',LC10='w51201b-10',RS='wfa27c2-2',RS3='wfa27c2-3',RH='w6c8357-2',
U1='we7bdc5-6',U2='we7bdc5-7',U3='we7bdc5-8',U4='we7bdc5-9',U5='we7bdc5-10',UH='w7aeb3b-9',UH8='w7aeb3b-8',UH5='w7aeb3b-5',UP='wc98211-15',UP46='wc98211-46',
G6='w77ee86-6',G8='w77ee86-8',G9='w77ee86-9',G12='w77ee86-12',G13='w77ee86-13',G14='w77ee86-14',G17='w77ee86-17',G19='w77ee86-19',G20='w77ee86-20',G21='w77ee86-21',G22='w77ee86-22',G24='w77ee86-24',G25='w77ee86-25',G26='w77ee86-26',G31='w77ee86-31',G32='w77ee86-32',G33='w77ee86-33',G34='w77ee86-34',G35='w77ee86-35',G38='w77ee86-38',
SW2='w28c87a-2',SW3='w28c87a-3',SW5='w28c87a-5',SW6='w28c87a-6',SWg='wc3d5a3-5',
A7='w1f3d24-7',A9='w1f3d24-9',A10='w1f3d24-10',A11='w1f3d24-11',B3='w5e1529-3',B4='w5e1529-4',A35='w1ba703-35',A57='w1ba703-57',
S5='w465237-5',S6='w465237-6',S7='w465237-7',S8='w465237-8',P11='wf8ce0d-11',P12='wf8ce0d-12',P13='wf8ce0d-13',P14='wf8ce0d-14',P15='wf8ce0d-15',
D9='w09b633-9',D11='w09b633-11',D12='w09b633-12',D13='w09b633-13',LI8='we263c5-8',LI9='we263c5-9',LI11='we263c5-11',
R2='w3ebad4-2',R3='w3ebad4-3',R24='w3ebad4-24',R25='w3ebad4-25',R27='w3ebad4-27',
K11='w47ae9e-11',K12='w47ae9e-12',K13='w47ae9e-13',K14='w47ae9e-14',K15='w47ae9e-15',K16='w47ae9e-16',K17='w47ae9e-17',
L1='aips-66745-1',L2='aips-66745-2',L7='aips-66745-7',L10='aips-66745-10',L11='aips-66745-11',L12='aips-66745-12',L13='aips-66745-13',L16='aips-66745-16',L20='aips-66745-20',L24='aips-66745-24',L36='aips-66745-36',L42='aips-66745-42',L46='aips-66745-46',L47='aips-66745-47',L50='aips-66745-50',L54='aips-66745-54',L60='aips-66745-60',L18='aips-66745-18',L19='aips-66745-19',L15='aips-66745-15',L40='aips-66745-40',L44='aips-66745-44',L43='aips-66745-43',L3='aips-66745-3',L14='aips-66745-14',
Z2='aips-68652-2',Z4='aips-68652-4',Z5='aips-68652-5',Z6='aips-68652-6',Z7='aips-68652-7',Z20='aips-68652-20',Z21='aips-68652-21',Z24='aips-68652-24',Z25='aips-68652-25',Z27='aips-68652-27',Z40='aips-68652-40',Z17='aips-68652-17',
C1='aips-66717-1',C2='aips-66717-2',C3='aips-66717-3',C5='aips-66717-5',C7='aips-66717-7',C8='aips-66717-8',C11='aips-66717-11',C12='aips-66717-12',C14='aips-66717-14',C18='aips-66717-18',C21='aips-66717-21',C22='aips-66717-22',
T1='aips-56990-1',T4='aips-56990-4',T5='aips-56990-5',T9='aips-56990-9',T11='aips-56990-11',T14='aips-56990-14',T16='aips-56990-16',
V3='aips-67886-3',V9='aips-67886-9',V14='aips-67886-14',V16='aips-67886-16',V27='aips-67886-27',V28='aips-67886-28',V59='aips-67886-59',V89='aips-67886-89',V125='aips-67886-125',V127='aips-67886-127')
def R(m):
    ids=[x.strip() for x in m.group(1).split(',')]
    return ''.join(f'<sup class="r"><a href="#sb-{AL.get(i,i)}">{AL.get(i,i)}</a></sup>' for i in ids)
def conv(t): return re.sub(r'\[\[([^\]]+)\]\]',R,t)
def build(n):
    src=open(f'src/p{n:02d}.txt',encoding='utf8').read().split('\n')
    out=[];wins=[];k=0
    def flush():
        nonlocal wins
        for w in wins: out.append(w)
        wins=[]
    for line in src:
        if not line.strip(): continue
        if line.startswith('P: '):
            flush(); body=line[3:]
            def btn(m):
                nonlocal k
                k+=1; wid=f'dx10-p{n}-f{k}'
                wins.append(f'<div id="{wid}" popover class="fenetre"><div class="p">{conv(m.group(3))}</div></div>')
                return f'<button class="w" popovertarget="{wid}">{m.group(1)}</button>'
            body=re.sub(r'<<([^|>]+)\|([^|>]*)\|([^>]+)>>',btn,body)
            out.append(f'<div class="p">{conv(body)}</div>'); flush()
        elif line.startswith('H: '): flush(); out.append(f'<h4><em>{line[3:]}</em></h4>')
        elif line.startswith('UL: '):
            flush(); items=line[4:].split(' ## ')
            def btn2(m):
                nonlocal k
                k+=1; wid=f'dx10-p{n}-f{k}'
                wins.append(f'<div id="{wid}" popover class="fenetre"><div class="p">{conv(m.group(3))}</div></div>')
                return f'<button class="w" popovertarget="{wid}">{m.group(1)}</button>'
            out.append('<ul>'+''.join('<li>'+conv(re.sub(r'<<([^|>]+)\|([^|>]*)\|([^>]+)>>',btn2,i))+'</li>' for i in items)+'</ul>'); flush()
        elif line.startswith('T: '):
            rows=[r.split(' | ') for r in line[3:].split(' ;; ')]
            h='<div class="t"><table><thead><tr>'+''.join(f'<th>{conv(c)}</th>' for c in rows[0])+'</tr></thead><tbody>'
            for r in rows[1:]: h+='<tr>'+''.join(f'<td>{conv(c)}</td>' for c in r)+'</tr>'
            out.append(h+'</tbody></table></div>')
        else: raise SystemExit(f'ligne inconnue p{n}: {line[:60]}')
    open(f'fragments/p{n:02d}.html','w',encoding='utf8').write(''.join(out))
if __name__=='__main__':
    ns=[int(a) for a in sys.argv[1:]] or [int(re.search(r'p(\d+)',f).group(1)) for f in sorted(glob.glob('src/p*.txt'))]
    for n in ns: build(n)
