#!/usr/bin/env python3
"""Patch 0099 · suspend les descriptions GES en conservant les identifiants et liens.

Rejouable depuis la base : APP_FILE=app_v2.html python3 tools/patches/0099-suspendre-gestes.py
Une deuxième exécution vérifie le résultat sans le modifier. Restauration : historique Git.
"""
import hashlib
import json
import os
from pathlib import Path
import sys

GES_OLD_SHA = 'de2f1eeb7bdee5a15f64130bf7f51a10aea842d610ec251b139af02429423474'
GES_NEW_SHA = '3a2c52ac1218ea1f706017fad97381f4a53351872750be70dcd9cded4a30e8c1'
ASSET_OLD_SHA = 'b7e10e34c5fbdc6a9debf2a4a6cec7c2522a1cdd3d897ddf2c80c650b505b971'
ASSET_NEW_SHA = '8401fd64eddb4808b7c16131cee9330ac47ce0767a7a8a11b9fec62f65ef0caa'
OLD_PANEL = '<p class="st">Région par région, dans l’ordre de l’examen : inspection, palpation, percussion, auscultation, mobilisation, tests spéciaux. Pour chaque signe recherché : le geste correct et son interprétation. Cochez un geste quand vous le maîtrisez : l’état est conservé.</p>'
NEW_PANEL = '<p class="st">Contenu en reconstruction. Les intitulés et liens des gestes restent consultables ; les descriptions de technique et d’interprétation sont temporairement retirées. Vos coches antérieures sont conservées, sans nouvelle évaluation pendant cette suspension.</p>'
OLD_SOURCE = 'const GES_SRC="Cadre : PROFILES 2023, EPA 2 « Évaluer l’état physique du patient » (SMIFK) ; format CS : OFSP, Exigences MED 2026, § 3.2 et § 5.1.4. Référence européenne de technique : Füeßl H. S., Middeke M., Anamnese und Klinische Untersuchung, Thieme (Duale Reihe). Catalogue compilé par Claude.";'
NEW_SOURCE = 'const GES_SRC="Contenu en reconstruction. Les descriptions et leurs références seront réexaminées avant republication.";'
FUNCTION_REVISIONS = (
    ('<input type="checkbox" data-g="${k}" ${GS[k]?\'checked\':\'\'}>', '<input type="checkbox" data-g="${k}" ${GS[k]?\'checked\':\'\'} ${!it.g&&!it.n?\'disabled aria-label="Progression enregistrée · contenu en reconstruction"\':\'\'}>'),
    ('<p>${esc(it.g)}</p><p class="i">${esc(it.n)}</p>', '${!it.g&&!it.n?\'<p class="st">Contenu en reconstruction · progression enregistrée conservée.</p>\':`<p>${esc(it.g)}</p><p class="i">${esc(it.n)}</p>`}'),
    ('gestes maîtrisés au total', 'coches historiques conservées'),
    (" if(ty==='g'){const r=GES.find(x=>x.id===a),it=r&&r.items[+b];if(!it)return null;return {hd:'Pour marquer le point · '+it.p,ti:it.s,h:'<b>Geste</b> : '+esc(it.g)+'<br><b>À énoncer</b> : '+esc(it.n)+'<br><b>Règle du temps « '+esc(it.p)+' »</b> : '+esc(PHT[it.p]||PHT['Tests spéciaux']),src:(it.src?it.src+' · ':'')+'OFSP, Exigences MED 2026, § 5.1.4 : seuls les gestes et mesures corrects rapportent des points, sans point négatif · PROFILES 2023, EPA 2'}}", " if(ty==='g'){const r=GES.find(x=>x.id===a),it=r&&r.items[+b];if(!it)return null;if(!it.g&&!it.n)return {hd:'Gestes · contenu en reconstruction',ti:it.s,h:'<p>Ce contenu est temporairement indisponible. L’intitulé et la progression enregistrée sont conservés.</p>',src:''};return {hd:'Pour marquer le point · '+it.p,ti:it.s,h:'<b>Geste</b> : '+esc(it.g)+'<br><b>À énoncer</b> : '+esc(it.n)+'<br><b>Règle du temps « '+esc(it.p)+' »</b> : '+esc(PHT[it.p]||PHT['Tests spéciaux']),src:(it.src?it.src+' · ':'')+'OFSP, Exigences MED 2026, § 5.1.4 : seuls les gestes et mesures corrects rapportent des points, sans point négatif · PROFILES 2023, EPA 2'}}"),
)


def sha(text):
    return hashlib.sha256(text.encode('utf-8')).hexdigest()


def ges_span(app):
    marker = '\nconst GES='
    if app.count(marker) != 1:
        raise ValueError('Ancrage GES absent ou répété')
    start = app.index(marker) + len(marker)
    value, offset = json.JSONDecoder().raw_decode(app, start)
    return start, offset, value


def pause(value):
    if len(value) != 22 or sum(len(r['items']) for r in value) != 315:
        raise ValueError('Catalogue GES inattendu')
    original = json.loads(json.dumps(value, ensure_ascii=False))
    for region in value:
        for item in region['items']:
            if not isinstance(item.get('g'), str) or not isinstance(item.get('n'), str):
                raise ValueError('Champs GES g/n absents ou mal typés')
            item['g'] = item['n'] = ''
    for before, after in zip(original, value):
        b = [{k: v for k, v in item.items() if k not in ('g', 'n')} for item in before['items']]
        a = [{k: v for k, v in item.items() if k not in ('g', 'n')} for item in after['items']]
        if before['id'] != after['id'] or b != a or {k:v for k,v in before.items() if k != 'items'} != {k:v for k,v in after.items() if k != 'items'}:
            raise ValueError('Identifiants, ordre, liens ou métadonnées modifiés')
    return json.dumps(value, ensure_ascii=False, separators=(',', ':'))


def revise_asset(asset):
    if sha(asset) != ASSET_OLD_SHA:
        raise ValueError('Asset de fonctions différent de la base attestée')
    for old, new in FUNCTION_REVISIONS:
        if asset.count(old) != 1:
            raise ValueError('Ancrage fonctionnel absent ou répété')
        asset = asset.replace(old, new, 1)
    if sha(asset) != ASSET_NEW_SHA:
        raise ValueError('Asset révisé différent de la version attendue')
    return asset


def restore_asset(asset):
    """Ramène uniquement les révisions attestées au corps original du patch 0098."""
    for old, new in reversed(FUNCTION_REVISIONS):
        if asset.count(new) != 1:
            raise ValueError('Révision fonctionnelle absente ou répétée')
        asset = asset.replace(new, old, 1)
    return asset


def transform(app, asset):
    start, end, value = ges_span(app)
    current = app[start:end]
    if sha(current) == GES_NEW_SHA and sha(asset) == ASSET_NEW_SHA and NEW_PANEL in app and NEW_SOURCE in app:
        return app, asset
    if sha(current) != GES_OLD_SHA:
        raise ValueError('GES ne correspond ni à la base ni à la suspension')
    updated = pause(value)
    if sha(updated) != GES_NEW_SHA:
        raise ValueError('GES suspendu différent de la version attendue')
    if app.count(OLD_PANEL) != 1 or app.count(OLD_SOURCE) != 1:
        raise ValueError('Ancrages d’interface absents ou répétés')
    result = app[:start] + updated + app[end:]
    result = result.replace(OLD_PANEL, NEW_PANEL, 1).replace(OLD_SOURCE, NEW_SOURCE, 1)
    return result, revise_asset(asset)


def main():
    path = os.environ.get('APP_FILE') or sys.exit('Indiquez APP_FILE.')
    if path.endswith('orig/app.html'):
        sys.exit('Interdit : orig/app.html')
    app_path = Path(path)
    asset_path = Path(os.environ.get('ASSET_FILE', app_path.parent / 'assets/config/fonctions.js'))
    old_app = app_path.read_text(encoding='utf-8')
    old_asset = asset_path.read_text(encoding='utf-8')
    new_app, new_asset = transform(old_app, old_asset)
    if new_app == old_app and new_asset == old_asset:
        print('0099 déjà appliqué ; empreintes vérifiées.')
        return
    asset_path.write_text(new_asset, encoding='utf-8')
    app_path.write_text(new_app, encoding='utf-8')
    print(f'GES suspendu : 22 régions, 315 clés préservées ; {len(old_app.encode())-len(new_app.encode())} octets économisés dans app_v2.html.')


if __name__ == '__main__':
    main()
