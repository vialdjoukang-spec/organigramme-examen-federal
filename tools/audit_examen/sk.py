import json,urllib.request,urllib.parse,sys
Q={'constantes':'Sphygmomanometer blood pressure measurement','peau':'Gray940 skin','tete-cou':'Gray1194 neck','thorax':'Gray967 lungs','coeur-vaisseaux':'Gray492 heart','seins':'Gray1172 mamma','abdomen':'abdominal quadrants regions diagram','tr-genital':'Gray1152 male pelvis','rachis':'Gray111 vertebral column','epaule':'Gray326 shoulder joint','coude-main':'Gray219 hand bones','hanche':'Gray342 hip joint','genou':'Gray349 knee','cheville-pied':'Gray290 foot bones','neuro-nc':'Brain human normal inferior view cranial nerves','neuro-moteur':'Grant 1962 dermatomes','meninge-gcs':'Gray769 meninges','pediatrie':'Gray197 fontanelles skull newborn','geriatrie':'Timed up and go test','psychiatrie':'Gray728 cerebrum lateral'}
H={'User-Agent':'oef-asclepios-audit/1.0 (vialdjoukang-spec)'}
def get(p):
  u='https://commons.wikimedia.org/w/api.php?'+urllib.parse.urlencode(p)
  return json.load(urllib.request.urlopen(urllib.request.Request(u,headers=H),timeout=30))
out={}
for k,q in Q.items():
  d=get(dict(action='query',format='json',generator='search',gsrsearch='File:'+q,gsrnamespace=6,gsrlimit=3,prop='imageinfo',iiprop='url|extmetadata|size'))
  L=[]
  for p in (d.get('query',{}).get('pages',{}) or {}).values():
    ii=p['imageinfo'][0];m=ii.get('extmetadata',{})
    f=lambda x:(m.get(x,{}).get('value','') or '')[:120]
    L.append(dict(t=p['title'],url=ii['descriptionurl'],lic=f('LicenseShortName'),licurl=f('LicenseUrl'),art=f('Artist'),w=ii.get('width'),h=ii.get('height')))
  out[k]=L;print(k,[(x['t'],x['lic']) for x in L],flush=True)
json.dump(out,open('sk.json','w'),ensure_ascii=False,indent=1)
