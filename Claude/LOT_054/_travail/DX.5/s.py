import sys,json,urllib.request,urllib.parse,time
db=sys.argv[1]; q=sys.argv[2]
u="https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=%s&retmax=8&retmode=json&term=%s"%(db,urllib.parse.quote(q))
for i in range(3):
    try:
        ids=json.load(urllib.request.urlopen(u))['esearchresult']['idlist']; break
    except Exception as e: time.sleep(2); ids=[str(e)]
print(q,ids)
for i in ids:
    if not i.isdigit(): continue
    time.sleep(0.5)
    v="https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi?db=%s&retmode=json&id=%s"%(db,i)
    try:
        r=json.load(urllib.request.urlopen(v))['result'][i]; print(' ',i,r.get('pubdate',''),r.get('title','')[:110],'|',r.get('source',''))
    except Exception as e: print(' ',i,e)
