#!/usr/bin/env python3
import re,glob,html,sys
def tx(s): return re.sub(r'\s+',' ',html.unescape(re.sub(r'<[^>]+>',' ',s))).strip()
bad=0
for f in sorted(glob.glob('fragments/p*.html')):
    h=open(f,encoding='utf-8').read()
    for tag,b in re.findall(r'<(p|li|dd|div class="p")(?:\s[^>]*)?>(.*?)</(?:p|li|dd|div)>',h,re.S):
        for br in re.split(r'(?<=[.!?])\s+(?=[A-ZÀ-Ý«])',b):
            t=tx(re.sub(r'<sup class="r">.*?</sup>','',br,flags=re.S)); n=len(t.split())
            if n>28: print(f,n,t[:100]); bad+=1
print('trop longues:',bad)
