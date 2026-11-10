import json,sys
R=json.load(open('/home/user/wt/lot-054/Claude/LOT_054/_travail/DX.2/controle.json'))[0]
print(R['verdict'],R['octets'],R['connecteur%'],R['paragraphes_sans_connecteur'])
for k,v in R['defauts'].items():
    print('##',k,v['n'])
    if len(sys.argv)<2 or k in sys.argv[1:]:
        for e in v['ex']: print('  -',e)
