"""Dédale-M · silhouettes pleines des territoires (masques) à partir du modèle Z-Anatomy, en mémoire réduite.

INSTRUCTIONS (automate, zéro jeton) ------------------------------------------------
    blender -b --factory-startup -P tools/dedale/masques.py -- nc07
Le script part d'une scène VIDE et n'ajoute (bpy.data.libraries.load) que les objets utiles de
/workspace/ssp/nc_src/Z-Anatomy/Startup.blend : jamais le modèle entier (qui occupe plus de 11 Go une fois
évalué). Mémoire mesurée : voir le journal (sous 5 Go exigés).
Entrées : tools/dedale/nerfs.json (« masques » : groupes d'objets par fonction ; caméras identiques à
          freestyle.py : même centre, même échelle, mêmes angles) ; nc/trait/<nerf>-<vue>.json (contrôle).
Sortie  : nc/trait/<nerf>-<vue>-masques.svg : un <g id="m-<groupe>"> par groupe, silhouette pleine vectorisée ;
          nc/trait/<nerf>-<vue>-masques.json : centre projeté de chaque objet des groupes (ancres supplémentaires).
Méthode : chaque groupe est rendu seul par Cycles (fond transparent, 16 échantillons, graine fixe) ;
          le canal alpha seuillé à 0,5 est vectorisé par potrace (-t 4 -a 1 -O 0.4) ; contrôle : le centre
          projeté de chaque ancre commune doit coïncider à 0,5 px près avec nc/trait/<nerf>-<vue>.json.
"""
import bpy, json, math, os, re, subprocess, sys, tempfile
from mathutils import Vector
from bpy_extras.object_utils import world_to_camera_view

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
BLEND = os.environ.get('ZANATOMY', '/workspace/ssp/nc_src/Z-Anatomy/Startup.blend')
argv = sys.argv[sys.argv.index('--') + 1:] if '--' in sys.argv else []
NERF = argv[0] if argv else 'nc07'
CFG = json.load(open(os.path.join(HERE, 'nerfs.json'), encoding='utf-8'))
C, N = CFG['commun'], CFG['nerfs'][NERF]
W = C['resolution']
M = N['masques']
sc = bpy.context.scene
for o in list(bpy.data.objects):
    bpy.data.objects.remove(o)

# 1. Noms à ajouter : régions du cadre (centre et échelle de la caméra) et objets des masques.
with bpy.data.libraries.load(BLEND, link=False) as (src, dst):
    colls = set(C['cadre_collections']) | {g['collection'] for g in M.values() if 'collection' in g}
    dst.collections = [c for c in src.collections if c in colls]
    dst.objects = sorted({n for g in M.values() for n in g.get('objets', [])} | {'Tongue', 'Lacrimal gland.r'})
coll = {c.name: c for c in dst.collections if c}
for o in dst.objects:
    if o and o.name not in sc.collection.all_objects:
        sc.collection.objects.link(o)
for c in coll.values():
    if c.name not in [x.name for x in sc.collection.children]:
        sc.collection.children.link(c)
bpy.context.view_layer.update()


def mesh_de(cn, side=None, excl=()):
    return sorted({o for o in coll[cn].all_objects if o.type == 'MESH' and not o.name.endswith('.j')
                   and not re.search(r'\.[a-z]$', o.name.replace('.r', '').replace('.l', ''))
                   and (side is None or o.name.endswith('.' + side)) and not any(x in o.name for x in excl)},
                  key=lambda o: o.name)


cad = [o for cn in C['cadre_collections'] for o in mesh_de(cn)]
bb = [o.matrix_world @ Vector(c) for o in cad for c in o.bound_box]
mn = Vector((min(p.x for p in bb), min(p.y for p in bb), min(p.z for p in bb)))
mx = Vector((max(p.x for p in bb), max(p.y for p in bb), max(p.z for p in bb)))
CEN = (mn + mx) / 2
ext = mx - mn
SCALE = C['marge'] * max(ext.z, math.hypot(ext.x, ext.y))
GROUPES = {}
for g, d in M.items():
    objs = [bpy.data.objects[n] for n in d.get('objets', [])]
    if 'collection' in d:
        objs += mesh_de(d['collection'], N['cote'], d.get('exclure', ()))
    GROUPES[g] = objs

cam_d = bpy.data.cameras.new('DD_cam'); cam_d.type = 'ORTHO'; cam_d.ortho_scale = SCALE
cam = bpy.data.objects.new('DD_cam', cam_d); sc.collection.objects.link(cam); sc.camera = cam
r = sc.render
r.engine = 'CYCLES'; sc.cycles.samples = 16; sc.cycles.seed = 0; sc.cycles.use_denoising = False
r.film_transparent = True; r.resolution_x = r.resolution_y = W; r.resolution_percentage = 100
r.image_settings.file_format = 'PNG'; r.image_settings.color_mode = 'RGBA'
TMP = tempfile.mkdtemp(prefix='dedale_m_')


def placer(az, pl):
    a, e = math.radians(az), math.radians(pl)
    direc = Vector((-math.sin(a) * math.cos(e), -math.cos(a) * math.cos(e), math.sin(e)))
    cam.location = CEN + direc * 2.0
    cam.rotation_euler = (-direc).to_track_quat('-Z', 'Y').to_euler()
    bpy.context.view_layer.update()


def centre(o):
    me = o.evaluated_get(bpy.context.evaluated_depsgraph_get()).to_mesh()
    v = sum((o.matrix_world @ p.co for p in me.vertices), Vector()) / max(1, len(me.vertices))
    o.evaluated_get(bpy.context.evaluated_depsgraph_get()).to_mesh_clear(); return v


def potrace_alpha(png):
    import numpy as np  # numpy est livré avec Blender
    img = bpy.data.images.load(png)
    a = np.array(img.pixels[:], dtype=np.float32).reshape(W, W, 4)[::-1, :, 3]
    bpy.data.images.remove(img)
    pbm = os.path.join(TMP, 'm.pbm'); svg = os.path.join(TMP, 'm.svg')
    with open(pbm, 'wb') as f:
        f.write(b'P1\n%d %d\n' % (W, W))
        for row in (a > 0.5):
            f.write((''.join('1' if v else '0' for v in row) + '\n').encode())
    subprocess.run(['potrace', pbm, '-s', '--flat', '-t', '4', '-a', '1', '-O', '0.4', '-u', '10', '-o', svg], check=True)
    s = open(svg).read()
    tr = re.search(r'transform="([^"]+)"', s).group(1)
    return tr, ' '.join(d.replace('\n', ' ') for d in re.findall(r' d="([^"]+)"', s))


for nom, v in CFG['vues'].items():
    placer(v['azimut'], v['plongee'])
    ref = json.load(open(os.path.join(ROOT, 'nc', 'trait', '%s-%s.json' % (NERF, nom)), encoding='utf-8'))['ancres']
    for n in ('Tongue', 'Lacrimal gland.r'):
        p = world_to_camera_view(sc, cam, centre(bpy.data.objects[n]))
        x, y = p.x * W, (1 - p.y) * W
        assert abs(x - ref[n][0]) < 0.6 and abs(y - ref[n][1]) < 0.6, ('caméra différente de freestyle.py', nom, n, x, y, ref[n])
    out, anc = [], {}
    for g, objs in GROUPES.items():
        for o in objs:
            p = world_to_camera_view(sc, cam, centre(o))
            anc[o.name] = [round(p.x * W, 1), round((1 - p.y) * W, 1)]
        keep = {o.name for o in objs}
        for o in sc.objects:
            o.hide_render = o.type != 'CAMERA' and o.name not in keep
        r.filepath = os.path.join(TMP, 'r.png')
        bpy.ops.render.render(write_still=True)
        tr, d = potrace_alpha(r.filepath)
        out.append('<g id="m-%s"><path transform="%s" d="%s"/></g>' % (g, tr, d))
    f = os.path.join(ROOT, 'nc', 'trait', '%s-%s-masques.svg' % (NERF, nom))
    open(f, 'w', encoding='utf-8', newline='\n').write(
        '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 %d %d" data-nerf="%s" data-vue="%s">%s</svg>\n' % (W, W, NERF, nom, ''.join(out)))
    json.dump({'nerf': NERF, 'vue': nom, 'ancres': anc}, open(f[:-4] + '.json', 'w', encoding='utf-8', newline='\n'),
              ensure_ascii=False, indent=1, sort_keys=True)
    print('DEDALE masques', nom, os.path.getsize(f), 'octets')
print('DEDALE fin masques')
