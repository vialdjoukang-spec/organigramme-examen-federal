from pathlib import Path
import subprocess,json,hashlib
root=Path('ChatGPT_Codex/LOT_083');base=root/'_travail/reprise'
items=[('redaction_PA','LOT_083_Phase_A_V0.html','e234189e86ed81663be699e7718cc0a96671800ad163c8f084637381f6b54e8d',39),('redaction_DX1_2/DX.1','LOT_083_Phase_B_V0_DX.1.html','314abf2e172af11029d843cd4d973148f43ef0d15c17ac93bca00bb10d1cf1b8',40),('redaction_DX1_2/DX.2','LOT_083_Phase_B_V0_DX.2.html','073d48ae1667a6e54ebaa13ef188c27b15c8665c98315a453f484c7361cf68ad',41),('redaction_DX6_7/DX.6','LOT_083_Phase_B_V0_DX.6.html','628a734dfd9d820b335a3f269f43a6456cbd9c1956ea8b66bc28134b47dff780',42),('redaction_DX6_7/DX.7','LOT_083_Phase_B_V0_DX.7.html','7683254f2aed09caff24b610847044da246a70dc280f66759d3a83999c241b68',43),('redaction_DX5_8/DX.8','LOT_083_Phase_B_V0_DX.8.html','5e395347106eef4c085cb47fe70fea57ea51fe37e2a280db2443b0308dd5efc4',44),('redaction_DX5_8/DX.5','LOT_083_Phase_B_V0_DX.5.html','46a5ed25759cabc6e0212a8c21381fa3927df886b12105a4f642cc6e4243de36',44)]
for folder,name,sha,total in items:
 source=base/folder/name
 assert hashlib.sha256(source.read_bytes()).hexdigest()==sha
 subprocess.run(['python3',str(base/'publier_copie.py'),str(source),sha,str(total),f'LOT083 : intégration de {name}, preuves et version stable poussées ; P3 selon rapport indépendant.'],check=True)
 subprocess.run(['git','add',str(root/name),str(root/'MANIFESTE.json'),str(root/'ETAT_FILE.json'),'ChatGPT_Codex/JOURNAL_NUIT.md',str(base/folder)],check=True)
 subprocess.run(['git','commit','-m',f'LOT083: intégrer {name} et ses preuves'],check=True)
 subprocess.run(['git','push','origin','codex/lot-083'],check=True)
 print('POUSSE',name,total,flush=True)
