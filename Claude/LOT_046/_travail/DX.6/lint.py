import re,glob,html
for f in sorted(glob.glob('fragments/p*.html')):
    h=open(f).read()
    h=re.sub(r'<sup class="r">.*?</sup>','',h)
    for b in re.findall(r'<(?:p|li|td|dd|div class="p")(?:\s[^>]*)?>(.*?)</(?:p|li|td|dd|div)>',h,re.S):
        t=re.sub(r'\s+',' ',html.unescape(re.sub(r'<[^>]+>',' ',b))).strip()
        for s in re.split(r'(?<=[.!?])\s+(?=[A-ZÀ-Ý«])',t):
            n=len(s.split())
            if n>28: print(f,n,s[:110])
import sys
if len(sys.argv)>1:
    CON=re.compile(r"\b(car|donc|or|ainsi|puis|alors|parce que|puisque|lorsque|quand|si|tandis que|alors que|afin de|afin que|pour que|de sorte que|c'est pourquoi|en effet|cependant|toutefois|néanmoins|par conséquent|dès lors|ensuite|enfin|d'abord|en revanche|ce qui|grâce à|à cause de|en raison de|si bien que|de ce fait|par ailleurs|en outre|autrement dit|c'est-à-dire|d'où|puisqu'|lorsqu'|qu'il)\b",re.I)
    for f in sorted(glob.glob('fragments/p*.html')):
        if sys.argv[1] not in f: continue
        h=open(f).read(); h=re.sub(r'<sup class="r">.*?</sup>','',h)
        tot=0;ok=0
        for b in re.findall(r'<(?:p|li|dd|div class="p")(?:\s[^>]*)?>(.*?)</(?:p|li|dd|div)>',h,re.S):
            t=re.sub(r'\s+',' ',html.unescape(re.sub(r'<[^>]+>',' ',b))).strip()
            for s in re.split(r'(?<=[.!?])\s+(?=[A-ZÀ-Ý«])',t):
                if len(s.split())<4: continue
                tot+=1
                if CON.search(s): ok+=1
                elif len(sys.argv)>2: print('  -',s[:100])
        print(f,ok,tot,round(100*ok/max(tot,1)))
