#!/usr/bin/env python3
"""segment.py — contourne une lésion à partir d'un point, sur CPU.

  python3 scripts/segment.py manifest/IMG-243.json [--arrow 0] [--seed 0.52,0.48]
      [--out progression/captures-interface/segment/IMG-243.png] [--write]

Le point graine est la pointe de la flèche, ou --seed x,y (coordonnées 0–1).
Sans --write, le manifeste n'est pas modifié : seule la superposition est écrite.

Méthode : scikit-image. Les traits fins (cadre Doppler, flèche incrustée) sont
effacés par un médian, puis trois essais (seuil local, watershed, contour actif)
gardent le masque qui contient le point, ni trop petit ni collé au cadre.
Le contour est rééchantillonné en 12 à 60 points, normalisés, fermé.

SAM / MedSAM : utilisés seulement si un module CPU est déjà importable
(`segment_anything` ou `transformers` avec un poids local). Sinon repli
scikit-image, annoncé sur la sortie.
"""
import json, os, sys
import numpy as np
from PIL import Image, ImageDraw

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def _sam_mask(im, sx, sy):
    """Masque SAM si un poids CPU est déjà là. None sinon."""
    try:
        import torch
        from segment_anything import sam_model_registry, SamPredictor
    except Exception:
        return None
    ckpt = os.environ.get("SAM_CHECKPOINT", "")
    if not ckpt or not os.path.isfile(ckpt):
        return None
    kind = os.environ.get("SAM_TYPE", "vit_b")
    sam = sam_model_registry[kind](checkpoint=ckpt)
    sam.to("cpu")
    pred = SamPredictor(sam)
    rgb = np.stack([im, im, im], axis=-1)
    pred.set_image(rgb)
    masks, scores, _ = pred.predict(point_coords=np.array([[sx, sy]]), point_labels=np.array([1]), multimask_output=True)
    return masks[int(np.argmax(scores))]

def _suppress_lines(im):
    from skimage import filters, morphology
    local = filters.median(im, morphology.disk(5))
    lines = im.astype(np.int16) > local.astype(np.int16) + 16
    clean = im.copy()
    clean[lines] = local[lines]
    return clean

def _component(mask, sy, sx):
    from skimage import measure, morphology
    if not mask[sy, sx]:
        return None
    lab = measure.label(mask)
    mask = lab == lab[sy, sx]
    mask = morphology.remove_small_holes(mask, max_size=1500)
    return mask

def _mask_threshold(sm, sy, sx):
    """Seuil plus bas sous la graine : le champ proche de l'échographie est plus sombre."""
    sv = float(sm[sy, sx])
    above = max(8.0, sv * 0.50)
    below = max(6.0, sv * 0.28)
    mask = np.zeros(sm.shape, dtype=bool)
    mask[:sy] = sm[:sy] >= above
    mask[sy:] = sm[sy:] >= below
    return _component(mask, sy, sx)

def _mask_watershed(sm, sy, sx):
    from skimage import filters, segmentation, morphology
    grad = filters.sobel(sm)
    markers = np.zeros(sm.shape, dtype=np.int32)
    markers[sy, sx] = 1
    # fond : bords sombres
    dark = sm < max(6.0, float(np.percentile(sm, 8)))
    markers[dark] = 2
    if markers.max() < 2:
        return None
    labels = segmentation.watershed(grad, markers)
    mask = labels == 1
    mask = morphology.opening(mask, morphology.disk(1))
    return _component(mask, sy, sx)

def _mask_active(clean, sy, sx):
    from skimage.segmentation import inverse_gaussian_gradient, morphological_geodesic_active_contour
    g = inverse_gaussian_gradient(clean.astype(np.float32), alpha=80, sigma=1.6)
    h, w = clean.shape
    rad = max(12, int(0.06 * min(h, w)))
    yy, xx = np.ogrid[:h, :w]
    init = (yy - sy) ** 2 + (xx - sx) ** 2 <= rad * rad
    evo = morphological_geodesic_active_contour(g, 90, init, smoothing=2, balloon=1)
    return _component(evo, sy, sx)

def _contour_of(mask):
    from skimage import measure
    # Un bord d'image ne doit pas devenir une corde à travers la lésion.
    padded = np.pad(mask.astype(float), 1, constant_values=0)
    cs = measure.find_contours(padded, 0.5)
    if not cs:
        return None
    cs.sort(key=len, reverse=True)
    c = cs[0] - 1
    return c

def _resample(c, n, w, h):
    if len(c) < n:
        n = max(12, len(c) // 2)
    d = np.diff(c, axis=0)
    step = np.sqrt((d ** 2).sum(1))
    s = np.concatenate([[0], np.cumsum(step)])
    if s[-1] < 1:
        return None
    target = np.linspace(0, s[-1], n, endpoint=False)
    pts = np.vstack([np.interp(target, s, c[:, i]) for i in (0, 1)]).T
    def clip(v):
        return round(min(1.0, max(0.0, float(v))), 4)
    norm = [[clip(p[1] / w), clip(p[0] / h)] for p in pts]
    norm.append(norm[0])
    return norm

def _inside(poly, x, y):
    c = False
    for i in range(len(poly)):
        x1, y1 = poly[i]
        x2, y2 = poly[(i + 1) % len(poly)]
        if ((y1 > y) != (y2 > y)) and (x < (x2 - x1) * (y - y1) / ((y2 - y1) or 1e-9) + x1):
            c = not c
    return c

def _score(mask, sm):
    frac = float(mask.mean())
    if frac < 0.01 or frac > 0.62:
        return -1
    # bord qui suit un vrai gradient, pas le cadre noir
    return frac * (1.2 - abs(frac - 0.25))

def segment_image(im, sx, sy):
    from skimage import filters
    sam = _sam_mask(im, sx, sy)
    clean = _suppress_lines(im)
    sm = filters.gaussian(clean.astype(np.float32), sigma=1.6, preserve_range=True)
    cands = []
    if sam is not None:
        cands.append(("sam", sam))
    for name, fn in (
        ("seuil", lambda: _mask_threshold(sm, sy, sx)),
        ("watershed", lambda: _mask_watershed(sm, sy, sx)),
        ("actif", lambda: _mask_active(clean, sy, sx)),
    ):
        try:
            mask = fn()
        except Exception:
            mask = None
        if mask is not None:
            cands.append((name, mask))
    best, best_s, best_name = None, -1, ""
    for name, mask in cands:
        if not mask[sy, sx]:
            continue
        s = _score(mask, sm)
        if s > best_s:
            best, best_s, best_name = mask, s, name
    return best, best_name, sm

def polygon(im, sx, sy, n=32):
    h, w = im.shape
    mask, name, _ = segment_image(im, sx, sy)
    if mask is None:
        return None, "échec"
    from skimage import morphology
    mask = morphology.closing(mask, morphology.disk(6))
    mask = morphology.opening(mask, morphology.disk(3))
    if not mask[sy, sx]:
        return None, name + " (lissage hors graine)"
    c = _contour_of(mask)
    if c is None:
        return None, name
    # viser 12–60 points ; 32 par défaut, moins si le contour est court
    count = int(np.clip(len(c) / 8, 12, 60))
    if n:
        count = int(np.clip(n, 12, 60))
    norm = _resample(c, count, w, h)
    if not norm or not _inside(norm[:-1], sx / w, sy / h):
        return None, name + " (graine hors contour)"
    return norm, name

def _nearest(mask, sy, sx):
    if mask[sy, sx]:
        return sy, sx
    ys, xs = np.where(mask)
    if len(ys) == 0:
        return None
    i = np.argmin((ys - sy) ** 2 + (xs - sx) ** 2)
    return int(ys[i]), int(xs[i])


def segment_like(im, sx, sy, mode):
    """Région de même nature que la graine : air, os, eau ou enveloppe."""
    from skimage import filters, morphology, measure
    sm = filters.gaussian(im.astype(np.float32), sigma=1.1, preserve_range=True)
    h, w = sm.shape
    if mode == "air":
        mask = sm <= np.percentile(sm, 42)
        mask[: int(h * 0.15), :] = False
        mask[int(h * 0.76) :, :] = False
        if sx < w / 2:
            mask[:, int(w * 0.50) :] = False
        else:
            mask[:, : int(w * 0.50)] = False
        mask = morphology.closing(mask, morphology.disk(14))
    elif mode == "os":
        mask = sm >= np.percentile(sm, 72)
        mask[: int(h * 0.08), :] = False
        mask[int(h * 0.78) :, :] = False
        mask = morphology.closing(mask, morphology.disk(12))
        from scipy import ndimage
        mask = ndimage.binary_fill_holes(mask)
        return mask
    elif mode == "enveloppe":
        mask = sm >= 26
        mask = morphology.closing(mask, morphology.disk(3))
        mask = morphology.remove_small_holes(mask, max_size=8000)
    else:
        mask = (sm >= 100) & (sm <= 185)
        mask[:, : int(w * 0.32)] = False
        mask[:, int(w * 0.72) :] = False
        mask[: int(h * 0.22), :] = False
        mask[int(h * 0.70) :, :] = False
        mask = morphology.closing(mask, morphology.disk(7))
    hit = _nearest(mask, sy, sx)
    if hit is None:
        return None
    sy, sx = hit
    lab = measure.label(mask)
    comp = lab == lab[sy, sx]
    if mode == "os":
        comp = morphology.remove_small_objects(comp, max_size=400)
        if not comp.any():
            return None
        # Le gril est l'ensemble des corticales, pas une seule côte.
        comp = morphology.closing(lab > 0, morphology.disk(9))
    return comp


def contour_from_seed(im, x, y, mode, n=28):
    """Contour normalisé depuis un point. SAM si un poids est là, sinon scikit-image."""
    h, w = im.shape
    sx = min(max(int(round(x * (w - 1))), 1), w - 2)
    sy = min(max(int(round(y * (h - 1))), 1), h - 2)
    sam = _sam_mask(im, sx, sy)
    mask = sam if sam is not None else None
    how = "sam" if mask is not None else ""
    if mask is None or not mask[sy, sx]:
        mask = segment_like(im, sx, sy, mode)
        how = "scikit-image " + mode
    if mask is None:
        return None, how or "échec", (sx, sy)
    c = _contour_of(mask)
    if c is None:
        return None, how, (sx, sy)
    count = int(np.clip(n, 12, 60))
    norm = _resample(c, count, w, h)
    return norm, how, (sx, sy)


def _canvas(im, shape):
    from skimage.transform import resize
    x = resize(im.astype(np.float32), shape, anti_aliasing=True, preserve_range=True)
    lo, hi = np.percentile(x, (2, 98))
    if hi <= lo:
        hi = lo + 1
    return np.clip((x - lo) / (hi - lo), 0, 1)


def _fit(moved, shape):
    """Ramène une image rééchantillonnée à la taille cible, centrée."""
    out = np.zeros(shape, dtype=np.float32)
    h, w = moved.shape
    H, W = shape
    y0 = max(0, (H - h) // 2)
    x0 = max(0, (W - w) // 2)
    ys = max(0, (h - H) // 2)
    xs = max(0, (w - W) // 2)
    hh = min(h, H)
    ww = min(w, W)
    out[y0:y0 + hh, x0:x0 + ww] = moved[ys:ys + hh, xs:xs + ww]
    return out, x0 - xs, y0 - ys


def preparer_recalage(src, dst):
    """Affine (échelle + translation) puis flux élastique, une fois pour le couple.

    SAM absent : scikit-image (corrélation de phase, flux TV-L1).
    """
    from skimage.registration import phase_cross_correlation, optical_flow_tvl1
    from skimage.transform import rescale
    shape = (384, 288)
    from skimage.exposure import match_histograms
    A = _canvas(src, shape)
    B = _canvas(dst, shape)
    A = match_histograms(A, B)
    best = None
    for scale in (0.98, 1.0, 1.02):
        moved = rescale(A, scale, anti_aliasing=True, preserve_range=True)
        canvas, ox, oy = _fit(moved, shape)
        shift, error, _ = phase_cross_correlation(B, canvas, upsample_factor=4)
        # Un thorax de face est déjà cadré : un grand décalage est un faux appariement.
        if abs(shift[0]) > shape[0] * 0.08 or abs(shift[1]) > shape[1] * 0.08:
            error = error + 1.0
        if best is None or error < best[0]:
            best = (error, scale, shift, canvas, ox, oy)
    _, scale, shift, canvas, ox, oy = best
    shift = (float(np.clip(shift[0], -shape[0] * 0.08, shape[0] * 0.08)),
             float(np.clip(shift[1], -shape[1] * 0.08, shape[1] * 0.08)))
    try:
        flow_r, flow_c = optical_flow_tvl1(B, canvas, num_iter=8, num_warp=2, attachment=8)
        how = "affine+élastique scikit-image"
    except Exception:
        flow_r = np.zeros(shape, np.float32)
        flow_c = np.zeros(shape, np.float32)
        how = "affine scikit-image"
    return {"shape": shape, "scale": scale, "shift": shift, "ox": ox, "oy": oy,
            "flow_r": flow_r, "flow_c": flow_c, "how": how}


def appliquer_recalage(reg, x, y):
    shape = reg["shape"]
    py = y * (shape[0] - 1) * reg["scale"] + reg["oy"] - reg["shift"][0]
    px = x * (shape[1] - 1) * reg["scale"] + reg["ox"] - reg["shift"][1]
    iy = int(np.clip(round(py), 0, shape[0] - 1))
    ix = int(np.clip(round(px), 0, shape[1] - 1))
    py = float(np.clip(py + reg["flow_r"][iy, ix], 0, shape[0] - 1))
    px = float(np.clip(px + reg["flow_c"][iy, ix], 0, shape[1] - 1))
    return px / (shape[1] - 1), py / (shape[0] - 1)


def draw(path, norm, sx, sy, dest):
    im = Image.open(path).convert("RGB")
    w, h = im.size
    d = ImageDraw.Draw(im)
    d.line([(p[0] * w, p[1] * h) for p in norm], fill=(255, 214, 0), width=2)
    d.ellipse((sx - 3, sy - 3, sx + 3, sy + 3), fill=(255, 40, 40))
    os.makedirs(os.path.dirname(dest), exist_ok=True)
    im.save(dest)
    return dest

def main():
    a = sys.argv[1:]
    if not a or a[0].startswith("-"):
        print(__doc__)
        return 2
    man_path = a[0]
    if not os.path.isabs(man_path):
        man_path = os.path.join(ROOT, man_path)
    opt = lambda k, d=None: a[a.index(k) + 1] if k in a else d
    arrow = int(opt("--arrow", "0"))
    seed = opt("--seed")
    write = "--write" in a
    npts = int(opt("--points", "32"))
    m = json.load(open(man_path, encoding="utf-8"))
    p = m.get("patho") or {}
    arrows = p.get("arrows") or []
    if arrow >= len(arrows):
        print("flèche absente")
        return 1
    rel = p.get("file")
    img_path = rel if os.path.isabs(rel) else os.path.join(ROOT, rel)
    im = np.array(Image.open(img_path).convert("L"))
    h, w = im.shape
    if seed:
        x, y = (float(t) for t in seed.split(","))
    else:
        x, y = arrows[arrow]["tip"]
    sx, sy = int(round(x * (w - 1))), int(round(y * (h - 1)))
    sx, sy = min(max(sx, 1), w - 2), min(max(sy, 1), h - 2)
    norm, how = polygon(im, sx, sy, npts)
    sam = _sam_mask(im, sx, sy)
    print("méthode:", how if norm else how, "| SAM:", "masque" if sam is not None else "absent, repli scikit-image")
    if not norm:
        print("segmentation impossible")
        return 1
    out = opt("--out")
    if not out:
        out = os.path.join(ROOT, "progression", "captures-interface", "segment", f"{m.get('id','img')}.png")
    if not os.path.isabs(out):
        out = os.path.join(ROOT, out)
    draw(img_path, norm, sx, sy, out)
    print("points", len(norm) - 1)
    print("overlay", out)
    if write:
        arrows[arrow]["contour"] = norm
        json.dump(m, open(man_path, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
        open(man_path, "a", encoding="utf-8").write("\n")
        print("manifeste mis à jour")
    else:
        print(json.dumps(norm))
    return 0

def ecrire_anatomie(man_path, structures):
    """Segmente la normale depuis chaque graine, recale le point, segmente la pathologique.

    structures : liste de dicts id, ordre, nom, x, y, mode, description, source.
    """
    m = json.load(open(man_path, encoding="utf-8"))
    npath = os.path.join(ROOT, m["normal"]["file"])
    ppath = os.path.join(ROOT, m["patho"]["file"])
    nim = np.array(Image.open(npath).convert("L"))
    pim = np.array(Image.open(ppath).convert("L"))
    sam = _sam_mask(nim, 10, 10)
    print("SAM:", "présent" if sam is not None else "absent, repli scikit-image")
    reg = preparer_recalage(nim, pim)
    print("recalage:", reg["how"], "échelle", round(reg["scale"], 3))
    normal, patho = [], []
    for st in structures:
        if st["mode"] == "base":
            continue
        norm, how, _ = contour_from_seed(nim, st["x"], st["y"], st["mode"])
        mx, my = appliquer_recalage(reg, st["x"], st["y"])
        pnorm, phow, _ = contour_from_seed(pim, mx, my, st["mode"])
        print(f"{st['id']}: normale {how} {0 if not norm else len(norm)-1} pts | "
              f"-> ({mx:.2f},{my:.2f}) | patho {phow} {0 if not pnorm else len(pnorm)-1} pts")
        base = {"id": st["id"], "ordre": st["ordre"], "nom": st["nom"],
                "description": st["description"], "source": st["source"], "graine": [round(st["x"], 4), round(st["y"], 4)]}
        if norm:
            normal.append({**base, "contour": norm})
        if pnorm:
            patho.append({**base, "graine": [round(mx, 4), round(my, 4)], "contour": pnorm})
    for st in structures:
        if st["mode"] != "base":
            continue
        def bas(layers):
            pts = []
            for layer in layers:
                if not str(layer["id"]).startswith("poumon"):
                    continue
                ys = [p[1] for p in layer["contour"]]
                cut = max(ys) - 0.10
                low = [p for p in layer["contour"] if p[1] >= cut]
                pts.extend(low)
            pts.sort(key=lambda p: p[0])
            return pts
        nb, pb = bas(normal), bas(patho)
        print(f"{st['id']}: bases normale {len(nb)} patho {len(pb)}")
        meta = {"id": st["id"], "ordre": st["ordre"], "nom": st["nom"],
                "description": st["description"], "source": st["source"]}
        if len(nb) >= 8:
            normal.append({**meta, "graine": [st["x"], st["y"]], "contour": nb})
        if len(pb) >= 8:
            patho.append({**meta, "graine": [st["x"], st["y"]], "contour": pb})
    normal.sort(key=lambda s: (s["ordre"], s["id"]))
    patho.sort(key=lambda s: (s["ordre"], s["id"]))
    return normal, patho


if __name__ == "__main__":
    sys.exit(main() or 0)
