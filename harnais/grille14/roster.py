#!/usr/bin/env python3
"""Équipe d'un LOT : autant d'agents que de diagnostics, 2 DD au plus par rédacteur, 4 DD au plus par auditeur.
  python3 harnais/grille14/roster.py <LOT> <N>   → écrit harnais/grille14/roster_<LOT>.json et l'affiche
Phase A : agent A (Sonnet 5.5 moyen). Phase B : R1..R8 (Sonnet 5.5 moyen, ≤ 2 DD). Audit : B1..B5 (Opus 5.5 moyen) ;
B1 audite d'abord la Phase A (liste des DD), puis 2 DD ; B2..B5 : 1 à 4 DD chacun."""
import json, sys
from pathlib import Path
D = Path(__file__).resolve().parent
COUL = {"A": "#f59e0b", "B1": "#fdba74", "B2": "#7dd3fc", "B3": "#86efac", "B4": "#c4b5fd", "B5": "#f9a8d4"}
def build(lot, n):
    wr = {f"R{k+1}": [i for i in (2*k+1, 2*k+2) if i <= n] for k in range((n + 1) // 2)}
    rem = n - 2; k = 4; base, extra = divmod(rem, k); aud = {"B1": [1, 2]}; cur = 3
    for j in range(2, 6):
        s = base + (1 if j - 2 < extra else 0); aud[f"B{j}"] = list(range(cur, cur + s)); cur += s
    f = lambda i: f"LOT_{lot}_Phase_B_V0_DX.{i}.html"; A = f"LOT_{lot}_Phase_A_V0.html"
    return dict(lot=lot, n=n, A=A, redacteurs={r: [f(i) for i in v] for r, v in wr.items()},
                auditeurs={b: ([A] if b == "B1" else []) + [f(i) for i in v] for b, v in aud.items()},
                dd_auditeur={f(i): b for b, v in aud.items() for i in v}, couleurs=COUL)
if __name__ == "__main__":
    lot, n = sys.argv[1], int(sys.argv[2]); r = build(lot, n)
    (D / f"roster_{lot}.json").write_text(json.dumps(r, ensure_ascii=False, indent=1)); print(json.dumps(r, ensure_ascii=False, indent=1))
