#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""build_ssp.py — Banque d'auteur (.py) → JSON (contrat) → HTML interactif « Réflexe SSP ».

Usage
  python3 build_ssp.py <dossier_SSP>            # lit _bank_GNN.py → écrit JSON + HTML
  python3 build_ssp.py <dossier_SSP> --json     # relit le JSON existant → réécrit le HTML seul
  python3 build_ssp.py <dossier_SSP> --print    # en plus : _print.html (questions puis corrigé en annexe)

Contrat (identique à build_g1_v2) : Type A 5 options, 1 seule clé, niveaux examen/approfondissement/specialiste,
blocs R/D/P, feedback 4 blocs (① pourquoi juste ② pourquoi pas les autres ③ perle ④ source) masqué tant que 💡 fermé,
mode révision avec confirmation, filtres EX/AP/SPE, score par niveau/bloc/spécialité, 🔥 sur SPE, localStorage par SSP.
"""
import json, random, html, collections, re, sys, os, glob, datetime

HERE = os.path.dirname(os.path.abspath(__file__))
TPL_DIR = os.path.join(HERE, '..', 'templates')
L = "ABCDE"
ORDER = {"R": 0, "D": 1, "P": 2}
TACHE = {"mechanisms": "Mécanismes", "assessment_diagnosis": "Évaluation / diagnostic", "management": "Prise en charge"}
BLOC = {"R": "Raisonner", "D": "Discriminer", "P": "Pièges & alarmes"}
BLOC_INV = {v: k for k, v in BLOC.items()}
NIV = {"examen": ("ex", "EX", "Examen"), "approfondissement": ("ap", "AP", "Approfondissement"), "specialiste": ("spe", "SPE", "Spécialiste")}
e = html.escape


def dx_cibles(dx):
    """'DX.4 vs DX.6' → ['DX.4','DX.6'] (le premier = DX cible, les suivants = discrimination croisée)."""
    out = []
    for m in re.findall(r'DX\.(\d+)', dx or ""):
        k = "DX." + m
        if k not in out: out.append(k)
    return out


def load_bank(d):
    banks = sorted(glob.glob(os.path.join(d, '_bank_G*.py')))
    if not banks: sys.exit(f"Aucun _bank_G*.py dans {d} (lancez init_ssp.py d'abord)")
    ns = {"__file__": banks[0]}
    Q = []
    def q(bloc, dx, tache, setting, stem, question, opts, why, pearl, src, pol="positive", niv="examen", spe=None, media=None, statut="revue_auto"):
        Q.append(dict(bloc=bloc, dx=dx, tache=tache, setting=setting, stem=stem, question=question, opts=opts, why=why,
                      pearl=pearl, src=src, polarite=pol, niveau=niv, specialite=spe, media=media, statut=statut))
    ns.update(q=q, Q=Q)
    exec(open(banks[0], encoding='utf-8').read(), ns)
    if 'META' not in ns: sys.exit("La banque doit définir META = {...}")
    return ns['META'], ns['Q'], os.path.basename(banks[0])


def check(Q):
    errs = []; warns = []
    for i, x in enumerate(Q, 1):
        if x['bloc'] not in ORDER: errs.append(f"Q{i}: bloc {x['bloc']}")
        if x['niveau'] not in NIV: errs.append(f"Q{i}: niveau {x['niveau']}")
        if x['niveau'] == 'specialiste' and not x['specialite']: errs.append(f"Q{i}: SPE sans spécialité")
        if len(x['opts']) != 5: errs.append(f"Q{i}: {len(x['opts'])} options (5 exigées)")
        if len({t for t, _ in x['opts']}) != 5: errs.append(f"Q{i}: options dupliquées")
        if any(not w for t, w in x['opts'][1:]): errs.append(f"Q{i}: distracteur sans « pourquoi pas »")
        if x['tache'] not in TACHE: errs.append(f"Q{i}: tache {x['tache']}")
        if not dx_cibles(x['dx']): warns.append(f"Q{i}: question transversale (aucun DX.n) : « {x['dx']} »")
    for w in warns: print("  ⚠", w)
    if errs: sys.exit("Banque invalide :\n  " + "\n  ".join(errs))


def keys_for(n, seed):
    keys = (list(L) * (n // 5 + 1))[:n]; random.Random(seed).shuffle(keys)
    for _ in range(50):
        ch = False
        for i in range(2, len(keys)):
            if keys[i] == keys[i-1] == keys[i-2]:
                j = next(k for k in range(len(keys)) if keys[k] != keys[i] and abs(k-i) > 2); keys[i], keys[j] = keys[j], keys[i]; ch = True
        if not ch: break
    return keys


def bank_to_json(meta, Q):
    check(Q)
    Q = sorted(Q, key=lambda x: ORDER[x['bloc']])
    keys = keys_for(len(Q), meta.get('seed', 2))
    lotn = meta['lot'].replace('_', ''); code = meta['code']; ver = meta.get('version', '2.0.0'); today = meta.get('date', datetime.date.today().isoformat())
    bank = []; cnt = collections.Counter()
    for i, x in enumerate(Q):
        cnt[x['bloc']] += 1
        k = L.index(keys[i]); opts = list(x['opts'][1:]); opts.insert(k, x['opts'][0])
        bank.append({"id": f"Q-{lotn}-{code}-{x['bloc']}-{cnt[x['bloc']]:02d}", "version": ver, "lot": meta['lot'], "ssp": code,
          "bloc": BLOC[x['bloc']], "dx": x['dx'], "dx_cibles": dx_cibles(x['dx']), "niveau": x['niveau'], "specialite": x['specialite'],
          "type": "A", "polarite": x['polarite'], "blueprint": {"tache": x['tache'], "setting": x['setting']},
          "stem": x['stem'], "question": x['question'], "options": [{"cle": L[j], "texte": t} for j, (t, _) in enumerate(opts)], "correct": [L[k]],
          "feedback": {"cle_libelle": opts[k][0], "pourquoi_vrai": x['why'], "pourquoi_faux_par_option": {L[j]: w for j, (t, w) in enumerate(opts) if j != k},
                       "perle_clinique": x['pearl'], "source_lecon": {"libelle": x['src'][1], "href": x['src'][0]}},
          "media": x['media'],
          "qualite": {"statut": x.get('statut', 'revue_auto'), "checklist_iml": {"couverture": True, "homogene": True, "sans_cue": True, "sans_trivia": True}, "relecteur": None},
          "historique": [{"version": ver, "date": today, "note": meta.get('note_version', 'build_ssp')}]})
    nmedia = sum(1 for b in bank if b['media'])
    stat = collections.Counter(b['qualite']['statut'] for b in bank)
    statut = 'valide' if stat and set(stat) == {'valide'} else ('brouillon' if stat.get('brouillon') else 'revue_auto')
    return {"lot": meta['lot'], "ssp": f"{code} — {meta['titre_court']}", "code": code, "titre": meta['titre'], "version": ver, "statut": statut,
      "format": "Type A, 5 options", "n": len(bank),
      "repartition_bloc": dict(collections.Counter(b['bloc'] for b in bank)),
      "repartition_niveau": dict(collections.Counter(b['niveau'] for b in bank)),
      "specialites_spe": dict(collections.Counter(b['specialite'] for b in bank if b['specialite'])),
      "cles": dict(sorted(collections.Counter(b['correct'][0] for b in bank).items())),
      "media": {"questions_avec_media": nmedia, "note": meta.get('note_media', '')},
      "rendu": {k: meta.get(k, '') for k in ('titre_court', 'n_dx', 'intro_R', 'intro_D', 'intro_P', 'carte_html', 'algo_html', 'footer', 'verdict_label')},
      "questions": bank}


def render(J, printmode=False):
    bank = J['questions']; R = J['rendu']; code = J['code']; lot = J['lot']
    def head(n, b):
        cls, c, lab = NIV[b['niveau']]
        badge = f'<span class="bd {cls}">{c}{" · " + e(b["specialite"]) if b["specialite"] else ""}</span>'
        neg = ' <span class="neg">question négative</span>' if b['polarite'] == "negative" else ""
        fire = '<button type="button" class="fire" aria-pressed="false" title="Cette question me passionne">🔥</button>' if b['niveau'] == "specialiste" else ""
        return f'<div class="qh"><span class="qn">Q{n}</span>{badge}<span class="tag">{e(b["dx"])}</span><span class="tag t2">{TACHE[b["blueprint"]["tache"]]} · {e(b["blueprint"]["setting"])}</span>{neg}{fire}</div>'
    def fbhtml(b):
        f = b['feedback']; c = b['correct'][0]
        others = "".join(f'<li><b>{k}</b> {e(v)}</li>' for k, v in f['pourquoi_faux_par_option'].items())
        med = ""
        if b['media']:
            m = b['media']; med = f'<details class="media"><summary>🖼 Voir le cliché</summary><figure><img src="{e(m["src"])}" alt="{e(m.get("alt",""))}" loading="lazy"><figcaption>{e(m.get("legende",""))}</figcaption></figure></details>'
        return f'''<div class="fb"><p class="ok">✅ <b>{c}</b> — {e(f["cle_libelle"])}</p>
<p><b>① Pourquoi c'est juste</b> {e(f["pourquoi_vrai"])}</p>
<details class="others"><summary><b>② Pourquoi pas les autres</b></summary><ul>{others}</ul></details>
<p><b>③ Perle</b> {e(f["perle_clinique"])}</p>{med}
<p class="src"><b>④ Source</b> <a href="{e(f["source_lecon"]["href"])}">{e(f["source_lecon"]["libelle"])}</a> · {lot} audité</p></div>'''
    def qhtml(n, b):
        cls = NIV[b['niveau']][0]
        if printmode:
            opts = "".join(f'<div class="opt"><span class="l">{o["cle"]}</span><span class="t">{e(o["texte"])}</span></div>' for o in b['options']); tail = ""
        else:
            opts = "".join(f'<label class="opt" data-k="{o["cle"]}"><input type="radio" name="{b["id"]}" value="{o["cle"]}"><span class="l">{o["cle"]}</span><span class="t">{e(o["texte"])}</span></label>' for o in b['options'])
            tail = f'<p class="res" aria-live="polite"></p><details class="reveal"><summary aria-label="Afficher le commentaire"><span class="bulb">💡</span><span class="rv">Commentaire</span></summary>{fbhtml(b)}</details>'
        return f'''<article class="qcm {cls}" id="{b["id"]}" data-c="{b["correct"][0]}" data-bloc="{b["bloc"]}" data-niv="{cls}" data-spe="{e(b["specialite"] or "")}">
{head(n,b)}<p class="stem">{e(b["stem"])}</p><p class="q">{e(b["question"])}</p><div class="opts">{opts}</div>{tail}</article>'''
    N = len(bank); nl = collections.Counter(b['niveau'] for b in bank)
    spes = sorted({b['specialite'] for b in bank if b['specialite']})
    secs = {"Raisonner": "", "Discriminer": "", "Pièges & alarmes": ""}
    for n, b in enumerate(bank, 1): secs[b['bloc']] += qhtml(n, b)
    nR, nD, nP = [sum(1 for b in bank if b['bloc'] == k) for k in secs]
    key = f"{lot.replace('_','')}_{code}_TypeA_v2"; vl = R.get('verdict_label') or f"Réflexe {code}"
    if printmode:
        cor = '<section id="corrige" style="break-before:page"><h2>✅ Corrigé commenté <small>· à consulter après avoir répondu</small></h2>'
        for n, b in enumerate(bank, 1):
            cls, c, lab = NIV[b['niveau']]
            fb = fbhtml(b).replace('<details class="others"><summary>', '<div class="others"><p>').replace('</summary><ul>', '</p><ul>').replace('</ul></details>', '</ul></div>')
            cor += f'<div class="card qcm {cls}" style="padding:10px"><div class="qh"><span class="qn">Q{n}</span><span class="bd {cls}">{c}{" · "+e(b["specialite"]) if b["specialite"] else ""}</span><span class="tag">{e(b["dx"])}</span></div>{fb}</div>'
        score, script = cor + '</section>', ""
    else:
        score = f'''<section id="score"><h2>★ Score <small>· par niveau et par spécialité</small></h2>
<div class="sc"><div>Total<b id="s-all">0/{N}</b></div><div class="s-ex"><span class="bd ex">EX</span> Examen<b id="s-ex">0/{nl["examen"]}</b></div><div class="s-ap"><span class="bd ap">AP</span> Approfondissement<b id="s-ap">0/{nl["approfondissement"]}</b></div><div class="s-spe"><span class="bd spe">SPE</span> Spécialiste<b id="s-spe">0/{nl["specialiste"]}</b></div></div>
<div class="sc" style="margin-top:10px"><div>① Raisonner<b id="s-R">0</b></div><div>② Discriminer<b id="s-D">0</b></div><div>🚩 Pièges<b id="s-P">0</b></div></div>
<table class="spe"><thead><tr><th>Spécialité (SPE)</th><th>Juste / posées</th><th>🔥</th></tr></thead><tbody>
{"".join(f'<tr data-spe="{e(s)}"><td>{e(s)}</td><td class="c">0/0</td><td class="f">0</td></tr>' for s in spes)}
</tbody></table>
<p class="exalt" id="exalt">Touchez 🔥 sur les questions SPE qui vous passionnent : la spécialité qui vous exalte apparaîtra ici.</p>
<p class="verdict" id="verdict"></p>
<button class="rev" id="revbtn" type="button">📖 Mode révision</button><button class="alt" type="button" id="resetbtn">↺ Recommencer</button>
</section>'''
        script = open(os.path.join(TPL_DIR, '_ssp_script.js'), encoding='utf-8').read().replace('%%KEY%%', key).replace('%%VERDICT%%', vl)
        script = '<script>\n' + script + '\n</script>'
    fonts = open(os.path.join(TPL_DIR, '_fonts.css'), encoding='utf-8').read()
    tpl = open(os.path.join(TPL_DIR, '_ssp_reflexe.html'), encoding='utf-8').read()
    rep = {'%%FONTS%%': fonts, '%%R%%': secs["Raisonner"], '%%D%%': secs["Discriminer"], '%%P%%': secs["Pièges & alarmes"],
           '%%SCORE%%': score, '%%SCRIPT%%': script, '%%CARTE%%': R['carte_html'], '%%ALGO%%': R['algo_html'], '%%FOOTER%%': R['footer'],
           '%%INTRO_R%%': R['intro_R'], '%%INTRO_D%%': R['intro_D'], '%%INTRO_P%%': R['intro_P'],
           '%%CODE%%': code, '%%TITRE_COURT%%': e(R['titre_court']), '%%LOT%%': lot, '%%NDX%%': str(R['n_dx']),
           '%%VMAJ%%': J['version'].split('.')[0],
           '%%NEX%%': str(nl["examen"]), '%%NAP%%': str(nl["approfondissement"]), '%%NSPE%%': str(nl["specialiste"]),
           '%%NR%%': str(nR), '%%ND%%': str(nD), '%%NP%%': str(nP), '%%N%%': str(N)}
    out = tpl
    for k in ['%%FONTS%%', '%%CARTE%%', '%%ALGO%%', '%%FOOTER%%', '%%INTRO_R%%', '%%INTRO_D%%', '%%INTRO_P%%', '%%R%%', '%%D%%', '%%P%%', '%%SCORE%%', '%%SCRIPT%%']:
        out = out.replace(k, rep.pop(k))
    for k, v in rep.items(): out = out.replace(k, v)
    if printmode:
        out = out.replace('<style>', '<style>\n.fb{display:block!important}.qcm .opt{cursor:default;padding:4px 8px;margin:3px 0}.qcm{padding:10px;margin:8px 0}\n', 1)
        out = out.replace("Mode d'emploi : choisissez une option", "Version papier : répondez d'abord ; le corrigé commenté est en annexe, après la dernière question. Version écran : choisissez une option")
    left = re.findall(r'%%[A-Z_]+%%', out)
    assert not left, left
    assert '<details open' not in out and 'details class="reveal" open' not in out, "réponse exposée"
    return out


def main():
    a = sys.argv[1:]
    if not a: sys.exit(__doc__)
    d = os.path.abspath(a[0]); only_json = '--json' in a; pr = '--print' in a
    jpath = glob.glob(os.path.join(d, 'LOT_*_TypeA_Reflexe.json'))
    if only_json:
        if not jpath: sys.exit("Pas de JSON à relire")
        J = json.load(open(jpath[0], encoding='utf-8')); base = jpath[0][:-5]
    else:
        meta, Q, bf = load_bank(d)
        J = bank_to_json(meta, Q)
        base = os.path.join(d, f"{meta['lot']}_{meta['code']}_TypeA_Reflexe")
        json.dump(J, open(base + '.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    open(base + '.html', 'w', encoding='utf-8').write(render(J))
    if pr: open(os.path.join(d, '_print.html'), 'w', encoding='utf-8').write(render(J, True))
    print(f"{J['code']}: {J['n']} Q · niveaux {J['repartition_niveau']} · blocs {J['repartition_bloc']} · clés {J['cles']} → {os.path.basename(base)}.html")


if __name__ == '__main__':
    main()
