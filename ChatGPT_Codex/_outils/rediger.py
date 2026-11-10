#!/usr/bin/env python3
"""REDIGER — instancie le prompt de point (P-POINT) avec le paquet, appelle UN modèle en UNE passe, archive.

Moteurs (gratuits d'abord) :
  --moteur local      : modèle installé sur la machine (serveur local, http://127.0.0.1:11434/api/generate)
  --moteur compatible : tout point /v1/chat/completions (passerelle LiteLLM, LM Studio, vLLM, Portkey…) via --url/--cle
  --moteur sec        : n'appelle rien ; écrit les prompts instanciés (copier-coller manuel dans l'IA de rédaction choisie)
Le nom du modèle se passe par --modele ou par la variable d'environnement MODELE_LOCAL.
Règles : une sortie reçue n'est JAMAIS renvoyée au modèle (pas d'aller-retour) ; la correction est chirurgicale
(auditeur) ; une réponse vide/coupée réseau peut être relancée UNE fois.

Usage :
  python3 rediger.py --gabarit P-POINT.txt --paquet DX.1/paquet.json --contrat contrat.json \
     --points 1-14 --sortie DX.1/fragments --moteur local --modele "$MODELE_LOCAL"
contrat.json : {"LOT":"166","CODE_SSP":"F2.18","ENTITE":"…","PREFIX":"dx1","SECURITE":"…",
                "points":{"1":{"titre":"Définition et sémantique","exige":"…","octets":6000,"squelette":"…"}, …}}
"""
import os, re, json, time, argparse, hashlib, urllib.request


def passages(paquet, ids, plafond):
    P = {p['id']: p for p in paquet['passages']}
    out, n = [], 0
    for i in ids:
        p = P.get(i)
        if not p:
            continue
        bloc = f"[{i}] ({p['source']}, {p.get('date') or 's.d.'}) {p['texte']}"
        if n + len(bloc) > plafond:
            break
        out.append(bloc)
        n += len(bloc)
    return '\n'.join(out) or '(aucun extrait : n’écris que des phrases sans chiffre, ou laisse le point court)'


def appeler(moteur, modele, prompt, octets, url, cle):
    num = int(1.3 * octets / 3.3)
    if moteur == 'local':
        corps = {'model': modele, 'prompt': prompt, 'stream': False, 'think': False,
                 'options': {'temperature': 0.2, 'repeat_penalty': 1.1, 'num_ctx': 8192, 'num_predict': num}}
        req = urllib.request.Request(url or 'http://127.0.0.1:11434/api/generate', json.dumps(corps).encode(),
                                     {'Content-Type': 'application/json'})
        return json.loads(urllib.request.urlopen(req, timeout=900).read())['response']
    corps = {'model': modele, 'temperature': 0.2, 'max_tokens': num, 'messages': [{'role': 'user', 'content': prompt}]}
    req = urllib.request.Request(url, json.dumps(corps).encode(),
                                 {'Content-Type': 'application/json', 'Authorization': f'Bearer {cle or ""}'})
    return json.loads(urllib.request.urlopen(req, timeout=900).read())['choices'][0]['message']['content']


def plage(s):
    a, _, b = s.partition('-')
    return list(range(int(a), int(b or a) + 1))


if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    ap.add_argument('--gabarit', required=True)
    ap.add_argument('--paquet', required=True)
    ap.add_argument('--contrat', required=True)
    ap.add_argument('--points', default='1-14')
    ap.add_argument('--sortie', required=True)
    ap.add_argument('--moteur', default='sec', choices=['local', 'compatible', 'sec'])
    ap.add_argument('--modele', default=os.environ.get('MODELE_LOCAL', ''))
    ap.add_argument('--url')
    ap.add_argument('--cle', default=os.environ.get('CLE_API'))
    ap.add_argument('--plafond', type=int, default=9000, help='caractères d’extraits par point')
    a = ap.parse_args()
    G, PQ, C = open(a.gabarit).read(), json.load(open(a.paquet)), json.load(open(a.contrat))
    os.makedirs(a.sortie, exist_ok=True)
    for n in plage(a.points):
        dest = os.path.join(a.sortie, f'p{n:02d}.html')
        if os.path.exists(dest):
            continue  # déjà reçu : jamais régénéré (anti-aller-retour)
        pt = C['points'][str(n)]
        val = dict(C, N=n, TITRE_POINT=pt['titre'], CONTENU_EXIGE=pt['exige'], OCTETS_CIBLE=pt['octets'],
                   SQUELETTE=pt.get('squelette', ''), PASSAGES=passages(PQ, PQ['points'].get(str(n), []), a.plafond))
        prompt = re.sub(r'\{(\w+)\}', lambda m: str(val.get(m.group(1), m.group(0))), G)
        open(os.path.join(a.sortie, f'p{n:02d}.prompt.txt'), 'w').write(prompt)
        if a.moteur == 'sec':
            continue
        for essai in (1, 2):
            try:
                t0 = time.time()
                rep = appeler(a.moteur, a.modele, prompt, pt['octets'], a.url, a.cle)
                break
            except Exception as e:
                rep = None
                if essai == 2:
                    print(f'p{n}: échec réseau {e}')
        if rep:
            rep = re.sub(r'^```(?:html)?\s*|\s*```$', '', rep.strip())
            open(dest, 'w').write(rep)
            json.dump({'modele': a.modele, 'secondes': round(time.time() - t0), 'octets': len(rep.encode()),
                       'sha256_prompt': hashlib.sha256(prompt.encode()).hexdigest()},
                      open(dest + '.meta.json', 'w'))
            print(f'p{n}: {len(rep.encode())} o')
