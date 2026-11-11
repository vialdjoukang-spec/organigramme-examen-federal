"""Équilibre les parenthèses finales de chaque bloc ADD(...) d'un générateur (aide d'écriture locale)."""
import sys, io, tokenize, re
f = sys.argv[1]; lines = open(f).read().split('\n')
starts = [i for i, l in enumerate(lines) if re.match(r'^(ADD\(|CTX = |if __name__)', l)]
for a, b in zip(starts, starts[1:]):
    if not lines[a].startswith('ADD('): continue
    blk = '\n'.join(lines[a:b]).rstrip()
    depth = 0
    for t in tokenize.generate_tokens(io.StringIO(blk + '\n').readline):
        if t.type == tokenize.OP:
            if t.string in '([{': depth += 1
            elif t.string in ')]}': depth -= 1
    if depth:
        last = max(i for i in range(a, b) if lines[i].strip())
        if depth > 0: lines[last] += ')' * depth
        else: lines[last] = lines[last][:depth] if lines[last].endswith(')' * -depth) else lines[last]
        print('bloc', lines[a][:12], 'corrigé de', -depth)
open(f, 'w').write('\n'.join(lines))
