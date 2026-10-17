"""Dédale-C · crâne 3D au crayon (traits pleins à graisse hiérarchisée) pour les 3 vues d'un nerf crânien.

INSTRUCTIONS (automate, zéro jeton) ------------------------------------------------
    blender -b --factory-startup -P tools/dedale/crane.py -- nc07 [--vues face,profil,34]
Mémoire : la scène part VIDE ; seuls les os du crâne, les noyaux du nerf et les régions
          du cadre (centre et échelle de la caméra) sont ajoutés depuis Z-Anatomy (bpy.data.libraries.load),
          puis les os sont DÉCIMÉS (modificateur Decimate) : jamais le modèle complet (11 Go). Pic mesuré : journal.
Entrées : tools/dedale/nerfs.json (« crane » : objets, graisses, décimation ; caméras de freestyle.py,
          contrôlées à 0,6 px près contre nc/trait/<nerf>-<vue>.json).
Sortie  : nc/trait/<nerf>-<vue>-crane.svg : groupes c-silhouette (trait épais), c-contours (moyen),
          c-details (léger), c-dents (léger), c-noyaux (noyaux pleins) ; tissus mous absents ; en coordonnées
          de base 800 px (les ancres de nc/trait/*.json s'y appliquent telles quelles) ;
          nc/trait/<nerf>-<vue>-crane.json : cadre (carré, coordonnées de base) et graisses.
Méthode : Freestyle (Cycles, surfaces en « holdout » : seules les lignes restent), une passe par graisse :
          silhouette extérieure ; silhouettes et bords ; arêtes vives (crease) ; épaisseur effilée aux deux
          bouts et légèrement modulée (bruit à graine fixe) pour l'allure crayon ; rendu agrandi puis vectorisé
          par potrace (formes pleines : l'épaisseur variable est conservée). Freestyle n'est pas rejouable à l'octet
          (écart mesuré : 94 px sur 21 500 px d'encre, invisible) ; le SVG publié l'est, depuis nc/trait versionné.
Interdits: aucun trait dessiné à la main ; aucun fichier du modèle copié dans le dépôt.
"""
import bpy, bmesh, json, math, os, re, subprocess, sys, tempfile
from mathutils import Vector
from bpy_extras.object_utils import world_to_camera_view

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
BLEND = os.environ.get('ZANATOMY', '/workspace/ssp/nc_src/Z-Anatomy/Startup.blend')
argv = sys.argv[sys.argv.index('--') + 1:] if '--' in sys.argv else []
NERF = argv[0] if argv else 'nc07'
VUES = argv[argv.index('--vues') + 1].split(',') if '--vues' in argv else None
CFG = json.load(open(os.path.join(HERE, 'nerfs.json'), encoding='utf-8'))
C, N = CFG['commun'], CFG['nerfs'][NERF]
K = C['crane']
W = C['resolution']
F = K['surechantillon']            # rendu F fois plus fin que la base 800 px
sc = bpy.context.scene
for o in list(bpy.data.objects):
    bpy.data.objects.remove(o)

NOYAUX = N.get('noyaux_objets', [])
CTRL = NOYAUX[0]
with bpy.data.libraries.load(BLEND, link=False) as (src, dst):
    dst.collections = [c for c in src.collections if c in set(C['cadre_collections']) | set(K['collections'])]
    dst.objects = sorted(set(K['objets']) | set(NOYAUX))
coll = {c.name: c for c in dst.collections if c}
for o in dst.objects:
    if o and o.name not in sc.collection.all_objects:
        sc.collection.objects.link(o)
for c in coll.values():
    sc.collection.children.link(c)
bpy.context.view_layer.update()


def mesh_de(cn):
    return sorted({o for o in coll[cn].all_objects if o.type == 'MESH' and not o.name.endswith('.j')
                   and not re.search(r'\.[a-z]$', o.name.replace('.r', '').replace('.l', ''))}, key=lambda o: o.name)


cad = [o for cn in C['cadre_collections'] for o in mesh_de(cn)]
bb = [o.matrix_world @ Vector(c) for o in cad for c in o.bound_box]
mn = Vector((min(p.x for p in bb), min(p.y for p in bb), min(p.z for p in bb)))
mx = Vector((max(p.x for p in bb), max(p.y for p in bb), max(p.z for p in bb)))
CEN = (mn + mx) / 2
ext = mx - mn
SCALE = C['marge'] * max(ext.z, math.hypot(ext.x, ext.y))
OS = sorted({bpy.data.objects[n] for n in K['objets']} | {o for cn in K['collections'] for o in mesh_de(cn)}, key=lambda o: o.name)
DCOL = bpy.data.collections.new('DD_dents')
DENTS = [o for o in OS if any(o in mesh_de(cn) for cn in K['legers'])]     # dents : trait léger, jamais la silhouette
OSP = [o for o in OS if o not in DENTS]
for o in DENTS:
    DCOL.objects.link(o)


def fuse(objs, name, dist):
    bm = bmesh.new(); dg = bpy.context.evaluated_depsgraph_get()
    for o in objs:
        me = o.evaluated_get(dg).to_mesh()
        tmp = bmesh.new(); tmp.from_mesh(me); tmp.transform(o.matrix_world)
        m2 = bpy.data.meshes.new('t'); tmp.to_mesh(m2); tmp.free(); bm.from_mesh(m2); bpy.data.meshes.remove(m2)
        o.evaluated_get(dg).to_mesh_clear()
    bmesh.ops.remove_doubles(bm, verts=bm.verts, dist=dist); bmesh.ops.recalc_face_normals(bm, faces=bm.faces)
    me = bpy.data.meshes.new(name); bm.to_mesh(me); bm.free()
    ob = bpy.data.objects.new(name, me); sc.collection.objects.link(ob)
    return ob


TR = []   # tronc cérébral : non dessiné (tissu mou absent) ; les noyaux pleins marquent l'origine
NO = [bpy.data.objects[n] for n in NOYAUX]
faces0 = sum(len(o.data.polygons) for o in OS)
for o in OS:
    m = o.modifiers.new('DD_dec', 'DECIMATE'); m.ratio = K['decimation']; m.use_collapse_triangulate = False
bpy.context.view_layer.update()
dg = bpy.context.evaluated_depsgraph_get()
faces1 = sum(len(o.evaluated_get(dg).data.polygons) for o in OS)
print('DEDALE os', len(OS), 'faces', faces0, '->', faces1)

hold = bpy.data.materials.new('DD_holdout'); hold.use_nodes = True
nt = hold.node_tree; nt.nodes.clear()
h = nt.nodes.new('ShaderNodeHoldout'); out = nt.nodes.new('ShaderNodeOutputMaterial')
nt.links.new(h.outputs[0], out.inputs['Surface'])
for o in OS + TR + NO:
    o.data.materials.clear(); o.data.materials.append(hold)

cam_d = bpy.data.cameras.new('DD_cam'); cam_d.type = 'ORTHO'; cam_d.ortho_scale = SCALE
cam = bpy.data.objects.new('DD_cam', cam_d); sc.collection.objects.link(cam); sc.camera = cam
r = sc.render
r.engine = 'CYCLES'; sc.cycles.samples = 4; sc.cycles.seed = 0; sc.cycles.use_denoising = False
sc.cycles.pixel_filter_width = 1.0
r.threads_mode = 'FIXED'; r.threads = 4
sc.cycles.use_auto_tile = False
r.film_transparent = True; r.resolution_x = r.resolution_y = W * F; r.resolution_percentage = 100
r.image_settings.file_format = 'PNG'; r.image_settings.color_mode = 'RGBA'
r.use_freestyle = True; r.line_thickness_mode = 'ABSOLUTE'
vl = sc.view_layers[0]; vl.use_freestyle = True
fs = vl.freestyle_settings; fs.crease_angle = math.radians(K['angle_arete']); fs.use_smoothness = True
fs.use_suggestive_contours = True; fs.kr_derivative_epsilon = K.get('suggestif', 0.0)
for ls in list(fs.linesets):
    fs.linesets.remove(ls)
LS = fs.linesets.new('DD'); LS.select_by_visibility = True; LS.visibility = 'VISIBLE'; LS.select_by_edge_types = True
st = LS.linestyle; st.color = (0, 0, 0); st.caps = 'ROUND'
st.use_length_min = True
tap = st.thickness_modifiers.new('effile', 'ALONG_STROKE'); tap.mapping = 'CURVE'; tap.blend = 'MULTIPLY'
cv = tap.curve.curves[0]
for x, y in ((0.0, 0.25), (0.15, 1.0), (0.85, 1.0), (1.0, 0.25)):
    cv.points.new(x, y)
for p in list(cv.points)[:2]:
    pass
tap.curve.update()
bruit = st.thickness_modifiers.new('crayon', 'NOISE'); bruit.blend = 'ADD'; bruit.period = 40.0; bruit.seed = 7
TYPES = ('select_silhouette', 'select_border', 'select_crease', 'select_contour', 'select_external_contour',
         'select_suggestive_contour', 'select_ridge_valley', 'select_material_boundary', 'select_edge_mark')
TMP = tempfile.mkdtemp(prefix='dedale_c_')


def placer(az, pl):
    a, e = math.radians(az), math.radians(pl)
    direc = Vector((-math.sin(a) * math.cos(e), -math.cos(a) * math.cos(e), math.sin(e)))
    cam.location = CEN + direc * 2.0
    cam.rotation_euler = (-direc).to_track_quat('-Z', 'Y').to_euler()
    bpy.context.view_layer.update()


def proj(v):
    p = world_to_camera_view(sc, cam, v)
    return p.x * W, (1 - p.y) * W


def centre(o):
    me = o.evaluated_get(bpy.context.evaluated_depsgraph_get()).to_mesh()
    v = sum((o.matrix_world @ p.co for p in me.vertices), Vector()) / max(1, len(me.vertices))
    o.evaluated_get(bpy.context.evaluated_depsgraph_get()).to_mesh_clear(); return v


def rendre(objs, types, epais, lmin=3, freestyle=True, garder=None):
    keep = {o.name for o in objs}
    for o in sc.objects:
        o.hide_render = o.type != 'CAMERA' and o.name not in keep
    for t in TYPES:
        setattr(LS, t, t in types)
    st.thickness = epais; bruit.amplitude = epais * K['bruit']; st.length_min = lmin * F
    LS.select_by_collection = False
    LS.select_by_face_marks = False
    if garder is not None:      # seules les lignes de ces objets (les autres objets cachent sans dessiner)
        LS.select_by_collection = True; LS.collection = DCOL; LS.collection_negation = 'INCLUSIVE'
    else:
        LS.select_by_collection = False
    r.use_freestyle = freestyle
    if not freestyle:   # silhouette pleine (noyaux) : surface opaque blanche
        for o in objs:
            o.data.materials.clear(); o.data.materials.append(plein)
    r.filepath = os.path.join(TMP, 'r.png')
    bpy.ops.render.render(write_still=True)
    if not freestyle:
        for o in objs:
            o.data.materials.clear(); o.data.materials.append(hold)
    return r.filepath


plein = bpy.data.materials.new('DD_plein')


def potrace(png, cadre_px):
    import numpy as np
    img = bpy.data.images.load(png)
    w, h = img.size
    a = np.array(img.pixels[:], dtype=np.float32).reshape(h, w, 4)[::-1, :, 3]
    bpy.data.images.remove(img)
    pbm = os.path.join(TMP, 'm.pbm'); svg = os.path.join(TMP, 'm.svg')
    with open(pbm, 'wb') as f:
        f.write(b'P1\n%d %d\n' % (w, h))
        for row in (a > 0.5):
            f.write((''.join('1' if v else '0' for v in row) + '\n').encode())
    subprocess.run(['potrace', pbm, '-s', '--flat', '-t', str(K['potrace_t']), '-a', '1', '-O', str(K['potrace_O']),
                    '-u', '10', '-o', svg], check=True)
    s = open(svg).read()
    tr = re.search(r'transform="translate\(([-\d.]+),([-\d.]+)\) scale\(([-\d.]+),([-\d.]+)\)"', s)
    ty, sx, sy = float(tr.group(2)), float(tr.group(3)), float(tr.group(4))
    # pixels du rendu recadré -> coordonnées de base : x0 + px / F
    x0, y0 = cadre_px[0] / F, cadre_px[1] / F
    t = 'matrix(%.5f 0 0 %.5f %.3f %.3f)' % (sx / F, sy / F, x0, y0 + ty / F)
    return t, ' '.join(d.replace('\n', ' ') for d in re.findall(r' d="([^"]+)"', s))


resultats = {}
for nom, v in CFG['vues'].items():
    if VUES and nom not in VUES:
        continue
    placer(v['azimut'], v['plongee'])
    ref = json.load(open(os.path.join(ROOT, 'nc', 'trait', '%s-%s.json' % (NERF, nom)), encoding='utf-8'))['ancres']
    x, y = proj(centre(bpy.data.objects[CTRL]))
    assert abs(x - ref[CTRL][0]) < 0.6 and abs(y - ref[CTRL][1]) < 0.6, ('caméra différente de freestyle.py', nom, x, y, ref[CTRL])
    # cadre carré : boîte projetée des os (coins des boîtes englobantes), marge
    pts = []
    for o in OS:   # boîte projetée des sommets réels (les boîtes englobantes débordent en vue oblique)
        me = o.evaluated_get(bpy.context.evaluated_depsgraph_get()).to_mesh()
        pts += [proj(o.matrix_world @ me.vertices[i].co) for i in range(0, len(me.vertices), 7)]
        o.evaluated_get(bpy.context.evaluated_depsgraph_get()).to_mesh_clear()
    bx0, bx1 = min(p[0] for p in pts), max(p[0] for p in pts)
    by0, by1 = min(p[1] for p in pts), max(p[1] for p in pts)
    S = max(bx1 - bx0, by1 - by0) * (1 + 2 * K['marge_cadre'])
    cx, cy = (bx0 + bx1) / 2, (by0 + by1) / 2
    cadre = [round(cx - S / 2, 1), round(cy - S / 2, 1), round(S, 1), round(S, 1)]
    k = W / S                          # agrandissement final (base -> image publiée)
    px = [round(cadre[0] * F), round(cadre[1] * F), round(S * F), round(S * F)]
    R = W * F
    r.use_border = True; r.use_crop_to_border = True
    r.border_min_x, r.border_max_x = px[0] / R, (px[0] + px[2]) / R
    r.border_max_y, r.border_min_y = 1 - px[1] / R, 1 - (px[1] + px[3]) / R
    groupes = []
    G = K['graisses']
    for gid, objs, types, larg, lmin in (
            ('c-details', OS, ('select_crease', 'select_suggestive_contour'), G['details'], K['longueur_min_details']),
            ('c-dents', OS, ('select_silhouette', 'select_border'), G['dents'], K['longueur_min']),
            ('c-contours', OSP, ('select_silhouette', 'select_border'), G['contours'], K['longueur_min']),
            ('c-silhouette', OSP, ('select_external_contour',), G['silhouette'], K['longueur_min'])):
        if gid == 'c-dents':        # lignes des dents seules, mais cachées par les os qui les couvrent
            for o in OSP:
                o.hide_render = False
        png = rendre(objs if gid != 'c-dents' else OS, types, larg / k * F, lmin, garder=DENTS if gid == 'c-dents' else None)
        t, d = potrace(png, px)
        groupes.append('<g id="%s"><path transform="%s" d="%s"/></g>' % (gid, t, d))
    png = rendre(NO, (), 1, freestyle=False)
    t, d = potrace(png, px)
    groupes.append('<g id="c-noyaux"><path transform="%s" d="%s"/></g>' % (t, d))
    f = os.path.join(ROOT, 'nc', 'trait', '%s-%s-crane.svg' % (NERF, nom))
    open(f, 'w', encoding='utf-8', newline='\n').write(
        '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 %d %d" data-nerf="%s" data-vue="%s">%s</svg>\n'
        % (W, W, NERF, nom, ''.join(groupes)))
    json.dump({'nerf': NERF, 'vue': nom, 'cadre': cadre, 'graisses_px': K['graisses'], 'decimation': K['decimation'],
               'faces_os': [faces0, faces1]},
              open(f[:-4] + '.json', 'w', encoding='utf-8', newline='\n'), ensure_ascii=False, indent=1, sort_keys=True)
    print('DEDALE crane', nom, os.path.getsize(f), 'octets', cadre)
print('DEDALE fin crane')
