import sys,json,urllib.request,urllib.parse
db=sys.argv[1]; t=sys.argv[2]
u="https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?"+urllib.parse.urlencode({'db':db,'retmax':12,'retmode':'json','term':t,'sort':'relevance'})
ids=json.load(urllib.request.urlopen(u))['esearchresult']['idlist']
u2="https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi?"+urllib.parse.urlencode({'db':db,'id':','.join(ids),'retmode':'json'})
r=json.load(urllib.request.urlopen(u2))['result']
for i in ids: print(i,r[i].get('pubdate','')[:4],r[i].get('title','')[:110],'|',r[i].get('source',''))
