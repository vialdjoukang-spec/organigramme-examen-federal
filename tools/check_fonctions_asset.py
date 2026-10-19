#!/usr/bin/env python3
"""Vérifie l'extraction des fonctions et reconstruit le script principal."""
import importlib.util
from pathlib import Path
import subprocess
import sys
import tempfile

ROOT = Path(__file__).resolve().parents[1]
PATCH = ROOT / 'tools/patches/0098-externaliser-fonctions.py'
spec = importlib.util.spec_from_file_location('patch_0098', PATCH)
patch = importlib.util.module_from_spec(spec)
spec.loader.exec_module(patch)
REVISION = ROOT / 'tools/patches/0099-suspendre-gestes.py'
revision_spec = importlib.util.spec_from_file_location('patch_0099', REVISION)
revision = importlib.util.module_from_spec(revision_spec)
revision_spec.loader.exec_module(revision)


def check(app_path=ROOT / 'app_v2.html', asset_path=ROOT / patch.ASSET_REL):
    app = Path(app_path).read_text(encoding='utf-8')
    asset = Path(asset_path).read_text(encoding='utf-8')
    original_asset = revision.restore_asset(asset)
    if app.count(patch.SCRIPT_INSERT + patch.SCRIPT_ANCHOR) != 1:
        raise ValueError('Asset absent, asynchrone ou mal placé avant le script principal')
    if app.count(patch.SCRIPT_INSERT) != 1:
        raise ValueError('Chargement de l’asset répété')
    pos = 0
    restored = app.replace(patch.SCRIPT_INSERT, '', 1)
    for name in patch.SPACED_LINES:
        anchor = patch.marker(name) + '\n\n'
        if restored.count(anchor) != 1:
            raise ValueError(f'Ligne vide déplacée : {name}')
        restored = restored.replace(anchor, patch.marker(name) + '\n \n', 1)
    for name, width, expected in patch.MANIFEST:
        body = original_asset[pos:pos + width]
        if patch.sha(body) != expected or original_asset[pos + width:pos + width + 1] != '\n':
            raise ValueError(f'Corps de fonction altéré : {name}')
        pos += width + 1
        if restored.count(patch.marker(name)) != 1:
            raise ValueError(f'Marqueur absent ou répété : {name}')
        restored = restored.replace(patch.marker(name), body, 1)
    if pos != len(original_asset):
        raise ValueError('Contenu supplémentaire dans l’asset')
    if restored.count(patch.SCRIPT_ANCHOR) != 1:
        raise ValueError('Reconstruction du script principal incorrecte')
    if patch.sha(restored) == patch.APP_ORIGINAL_SHA256:
        print('Reconstruction octet pour octet du main d’origine confirmée.')
    else:
        print('Reconstruction complète ; le contenu du script principal a évolué depuis le patch.')
    start = app.index(patch.SCRIPT_ANCHOR) + len('<script>\n')
    end = app.index('</script>', start)
    with tempfile.TemporaryDirectory() as directory:
        files = [Path(directory) / 'fonctions.js', Path(directory) / 'main.js', Path(directory) / 'ensemble.js']
        files[0].write_text(asset, encoding='utf-8')
        files[1].write_text(app[start:end], encoding='utf-8')
        # Détecte aussi les collisions lexicales invisibles à deux parses isolés.
        files[2].write_text(asset + '\n' + app[start:end], encoding='utf-8')
        for path in files:
            subprocess.run(['node', '--check', str(path)], check=True, capture_output=True, text=True)
    return len(patch.MANIFEST), len(restored.encode('utf-8')) - len(app.encode('utf-8'))


if __name__ == '__main__':
    try:
        count, gain = check()
        print(f'{count} fonctions intactes ; gain dans app_v2.html : {gain} octets.')
    except (ValueError, subprocess.CalledProcessError) as error:
        sys.exit(f'ÉCHEC fonctions : {error}')
