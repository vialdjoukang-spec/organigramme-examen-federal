import sys
def patch(fn, pairs):
    s = open(fn, encoding='utf-8').read()
    for a, b in pairs:
        if a not in s: print('ABSENT:', a[:70]); continue
        s = s.replace(a, b, 1)
    open(fn, 'w', encoding='utf-8').write(s)
