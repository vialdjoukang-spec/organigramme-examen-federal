#!/usr/bin/env python3
"""Sonde GitHub sans commentaire, écriture clinique, appel IA ou secret requis."""
import datetime, json, urllib.request

URL='https://api.github.com/repos/vialdjoukang-spec/organigramme-examen-federal/contents/phase_lot/config/file.json?ref=Organigramme'

if __name__=='__main__':
    req=urllib.request.Request(URL,headers={'Accept':'application/vnd.github.raw+json','User-Agent':'PhaseLOT-Heartbeat'})
    with urllib.request.urlopen(req,timeout=20) as r: queue=json.load(r)
    print(json.dumps({'observed_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),
                      'active':[x['lot'] for x in queue['lots'] if x['production_status']=='ACTIF'],
                      'ai_started':False,'notice':'Une sonde ne réveille pas le chat et ne renouvelle aucun bail.'},ensure_ascii=False))
