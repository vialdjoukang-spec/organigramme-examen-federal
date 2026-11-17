"""Contrôle de reprise textuelle : cherche les suites de N mots communes entre le texte du jeu
et les textes sources téléchargés (HTML/TXT). Usage :
  node tests/dump_text.js > /tmp/jeu.txt && python3 tests/check_overlap.py /tmp/jeu.txt 6 source1.txt source2.html ..."""
import re, sys, html
def norm(t): return re.findall(r"[a-zà-ÿœ0-9]+", html.unescape(re.sub("<[^>]+>", " ", t)).lower().replace("’", "'"))
jeu, n, srcs = sys.argv[1], int(sys.argv[2]), sys.argv[3:]
J = norm(open(jeu, encoding="utf8").read()); jg = {tuple(J[i:i+n]) for i in range(len(J)-n+1)}
total = 0
for f in srcs:
    S = norm(open(f, encoding="utf8", errors="ignore").read())
    common = sorted(" ".join(x) for x in jg & {tuple(S[i:i+n]) for i in range(len(S)-n+1)})
    total += len(common); print(f"{f}: {len(common)} suite(s) de {n} mots", common[:20])
sys.exit(0)
