#!/usr/bin/env python3
"""ASSEMBLER — fragments de points → HTML final autonome (charte Vial), Sources limitées aux extraits cités,
FIN_FICHIER, puis MANIFESTE (octets + SHA-256). Zéro modèle.

Usage :
  python3 assembler.py --fragments DX.1/fragments --paquet DX.1/paquet.json --contrat contrat.json \
     --titre "DX.1 — Ascite de l'hypertension portale" --sortie LOT_166_Phase_B_V0_DX.1.html [--figures DX.1/figures.json]
figures.json : [{"point":9,"fichier":"images/ab12.jpg","legende":"…","attribution":"Auteur, CC BY-SA 4.0, URL"}]
(les figures ne sont insérées qu'après inspection visuelle validée : clé "inspectee": true)
"""
import os, re, json, html, hashlib, argparse, base64

CSS = """:root{--fond:#eef1f3;--ilot:#fff;--encre:#16202a;--accent:#0b5c7a;--bord:#c9d2d9;--alerte:#9b1c1c}
*{box-sizing:border-box}body{margin:0;background:var(--fond);color:var(--encre);font:16px/1.55 "Atkinson Hyperlegible",Verdana,sans-serif}
main{max-width:980px;margin:0 auto;padding:12px}h2{font-size:1.35rem;margin:.4rem 0 1rem}
section.ilot{background:var(--ilot);border:1px solid var(--bord);border-radius:10px;padding:14px 16px;margin:0 0 14px;
box-shadow:0 1px 0 #fff inset,3px 4px 0 #cfd8de,6px 8px 14px rgba(20,40,60,.12)}
h3{font-size:1.08rem;margin:0 0 .5rem;color:var(--accent)}.p{margin:0 0 .7rem}
.t{overflow-x:auto}table{border-collapse:collapse;width:100%;font-size:.93rem}td,th{border:1px solid var(--bord);padding:5px 7px;vertical-align:top}
.fenetre{max-width:min(860px,94vw);max-height:86vh;overflow:auto;border:2px solid var(--accent);border-radius:12px;padding:16px 18px;
box-shadow:0 18px 50px rgba(0,0,0,.35)}.fenetre::backdrop{background:rgba(10,20,30,.45)}
button.w{all:unset;color:var(--accent);border-bottom:1px dotted var(--accent);cursor:pointer}
sup.r a{font-size:.72em;color:#557;text-decoration:none}.alerte{border-left:5px solid var(--alerte);padding-left:10px}
figure{margin:.6rem 0}figure img{max-width:100%;height:auto;border-radius:6px}figcaption{font-size:.86rem;color:#445}
@media(max-width:420px){body{font-size:15px}section.ilot{padding:10px}}"""


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--fragments', required=True)
    ap.add_argument('--paquet', required=True)
    ap.add_argument('--contrat', required=True)
    ap.add_argument('--titre', required=True)
    ap.add_argument('--sortie', required=True)
    ap.add_argument('--figures')
    ap.add_argument('--integrer-images', action='store_true', help='images en data: URI (fichier autonome)')
    a = ap.parse_args()
    C, PQ = json.load(open(a.contrat)), json.load(open(a.paquet))
    P = {p['id']: p for p in PQ['passages']}
    figs = [f for f in (json.load(open(a.figures)) if a.figures else []) if f.get('inspectee')]
    pre = C.get('PREFIX', 'dx')
    corps, cites = [], []
    for n in range(1, 15):
        f = os.path.join(a.fragments, f'p{n:02d}.html')
        frag = open(f).read() if os.path.exists(f) else '<div class="p">POINT MANQUANT</div>'
        cites += re.findall(r'href="#sb-([\w.\-:]+)"', frag)
        fig = ''
        for g in (x for x in figs if x['point'] == n):
            src = g['fichier']
            if a.integrer_images:
                ext = src.rsplit('.', 1)[-1].replace('jpg', 'jpeg')
                src = f"data:image/{ext};base64," + base64.b64encode(open(src, 'rb').read()).decode()
            fig += (f'<figure><img src="{src}" alt="{html.escape(g["legende"])}"><figcaption>{html.escape(g["legende"])} '
                    f'— {html.escape(g["attribution"])}</figcaption></figure>')
        corps.append(f'<section class="ilot" id="{pre}-p{n}"><h3 id="{pre}-h{n}"><strong>{n}. '
                     f'{html.escape(C["points"][str(n)]["titre"])}</strong></h3>{frag}{fig}</section>')
    vus = list(dict.fromkeys(cites))
    src = ''.join(f'<li id="sb-{i}">[{i}] {html.escape(P[i]["source"])}{" — " + html.escape(P[i]["url"]) if P[i].get("url") else ""}'
                  f'{" (consulté le " + P[i]["date"] + ")" if P[i].get("date") else ""}</li>' for i in vus if i in P)
    nom = os.path.splitext(os.path.basename(a.sortie))[0]
    doc = (f'<!DOCTYPE html>\n<html lang="fr"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">'
           f'<title>{html.escape(a.titre)}</title><style>{CSS}</style></head><body><main><h2>{html.escape(a.titre)}</h2>'
           + '\n'.join(corps) +
           f'<section class="ilot" id="{pre}-sources"><h3>Sources</h3><ol>{src}</ol><p class="p">Le contenu reprend les sources citées ; '
           f'il n’a pas été validé cliniquement par un médecin.</p></section></main></body></html>\n<!-- FIN_FICHIER {nom} -->\n')
    open(a.sortie, 'w').write(doc)
    b = doc.encode()
    man = os.path.join(os.path.dirname(a.sortie) or '.', 'MANIFESTE.json')
    m = json.load(open(man)) if os.path.exists(man) else {}
    m[os.path.basename(a.sortie)] = {'octets': len(b), 'sha256': hashlib.sha256(b).hexdigest()}
    json.dump(m, open(man, 'w'), ensure_ascii=False, indent=1)
    absents = [i for i in vus if i not in P]
    print(f'{a.sortie}: {len(b)} o, {len(vus)} sources citées' + (f', CITATIONS INCONNUES {absents}' if absents else ''))


if __name__ == '__main__':
    main()
