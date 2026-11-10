import json,sys
R=json.load(open('/home/user/wt/lot-053/Claude/LOT_053/_travail/DX.9/controle.json'))[0]
k=sys.argv[1]
for e in R['defauts'].get(k,{'ex':[]})['ex']: print(e)
