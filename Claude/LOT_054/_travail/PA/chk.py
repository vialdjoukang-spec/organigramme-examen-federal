import subprocess,json,sys
r=subprocess.run(['python3','/home/user/organigramme-examen-federal/Claude/_outils/controle3.py','Claude/LOT_054/LOT_054_Phase_A_V0.html','--paquet','Claude/LOT_054/_travail/PA/paquet.json','--ex','400'],capture_output=True,text=True)
j=json.loads(r.stdout)[0]
print(j['verdict'],j['octets'],'conn',j['connecteur%'],'sansconn',j['paragraphes_sans_connecteur'],'phrases',j['phrases'])
want=sys.argv[1:] 
for k,v in j['defauts'].items():
    print('##',k,v['n'])
    if not want or k in want:
        for e in v['ex']: print('  -',e)
