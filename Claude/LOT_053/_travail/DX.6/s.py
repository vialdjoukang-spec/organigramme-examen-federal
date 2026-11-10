import sys,urllib.request,urllib.parse,re,json
def get(u):
    return urllib.request.urlopen(u,timeout=40).read().decode()
for q in sys.argv[1:]:
    u="https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=pmc&retmax=8&term="+urllib.parse.quote(q)
    ids=re.findall(r"<Id>(\d+)</Id>",get(u))
    print("==",q)
    if not ids: continue
    s=json.loads(get("https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi?db=pmc&retmode=json&id="+",".join(ids)))
    for i in ids:
        d=s['result'][i]; print(i,d.get('pubdate','')[:4],d.get('fulljournalname','')[:30],'|',d['title'][:110])
