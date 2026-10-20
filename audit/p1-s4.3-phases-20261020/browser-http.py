"""Transport HTTP seul : les assertions des deux fichiers de tests sont inchangées."""
import asyncio, functools, http.server, importlib.util, os, pathlib, runpy, threading
from playwright.async_api import Page
ROOT = pathlib.Path(os.environ['PHASES_PROJECTION'])
class Quiet(http.server.SimpleHTTPRequestHandler):
    def log_message(self, *args): pass
server=http.server.ThreadingHTTPServer(('127.0.0.1',0),functools.partial(Quiet,directory=str(ROOT)))
threading.Thread(target=server.serve_forever,daemon=True).start()
original_goto=Page.goto
async def goto(self,url,*args,**kwargs):
    prefix=ROOT.as_uri()+'/'
    if str(url).startswith(prefix):url='http://127.0.0.1:'+str(server.server_port)+'/'+str(url)[len(prefix):]
    return await original_goto(self,url,*args,**kwargs)
Page.goto=goto
os.environ['COURS_UI_SSP']='S4.2 S4.3'
os.environ['CHROME_PATH']='/usr/bin/chromium'
os.environ.pop('GITHUB_ACTIONS',None)
spec=importlib.util.spec_from_file_location('existing_ui',ROOT/'tests/test_infobulles_prototype_ui.py')
module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module)
print('Début main EXISTANT test_infobulles_prototype_ui.py : G1–G16 + S4.2/S4.3, bureau/mobile, toutes assertions conservées',flush=True)
asyncio.run(module.main())
print('Début main EXISTANT test_examen.py : toutes assertions/observations conservées',flush=True)
runpy.run_path(str(ROOT/'tests/test_examen.py'),run_name='__main__')
server.shutdown()
