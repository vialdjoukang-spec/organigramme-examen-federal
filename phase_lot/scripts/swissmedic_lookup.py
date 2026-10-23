#!/usr/bin/env python3
"""Résout les numéros depuis un CSV officiel, jamais depuis une URL ou une dose."""
import argparse,csv,json,unicodedata
from pathlib import Path
from urllib.parse import urlencode

def norm(value):
    return ''.join(c for c in unicodedata.normalize('NFKD',value.casefold()) if not unicodedata.combining(c)).replace('-','').replace(' ','')

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('csv',type=Path);p.add_argument('query');p.add_argument('--limit',type=int,default=15);a=p.parse_args()
    with a.csv.open(encoding='utf-8-sig',newline='') as f:
        reader=csv.DictReader(f);fields=reader.fieldnames
        number=next(k for k in fields if "N° d'autorisation" in k)
        name=next(k for k in fields if 'Dénomination du médicament' in k)
        result=[]
        for row in reader:
            if norm(a.query) not in norm(row[name]): continue
            auth=row[number]
            result.append({'name':row[name],'authorization_read_in_csv':auth,'source_csv':str(a.csv),
                'professional_information_url_hint':'https://www.swissmedicinfo-pro.ch/showText.aspx?'+urlencode({'authNr':auth,'lang':'FR','supportMultipleResults':1,'textType':'FI'}),
                'dose_verified':False,'export_only_status':'Vérifier la liste étendue et la notice actuelle'})
            if len(result)>=a.limit:break
    print(json.dumps(result,ensure_ascii=False,indent=2))
