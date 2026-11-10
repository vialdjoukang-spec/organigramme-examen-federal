import subprocess,sys,json
d='/home/user/wt/lot-053/Claude/LOT_053/'
r=subprocess.run([sys.executable,'/home/user/organigramme-examen-federal/Claude/_outils/controle3.py',d+'LOT_053_Phase_B_V0_DX.5.html','--paquet',d+'_travail/DX.5/paquet.json','--ex','200'],capture_output=True,text=True)
R=json.loads(r.stdout)[0]
print(R['verdict'],R['octets'],R['connecteur%'],R['paragraphes_sans_connecteur'])
want=sys.argv[1:] or ['A_']
for k,v in R['defauts'].items():
    if any(k.startswith(w) for w in want):
        print(k,v['n'])
        for e in v['ex']: print('  ',e[:int(300)])
