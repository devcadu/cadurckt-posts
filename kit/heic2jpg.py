"""Decodifica HEIC do iPhone (grade de tiles HEVC) usando ffmpeg. Uso: heic2jpg.py in.heic out.jpg"""
import struct, sys, subprocess, tempfile, os
from PIL import Image
import io

def boxes(data, start, end):
    i = start
    while i < end:
        size, typ = struct.unpack(">I4s", data[i:i+8]); hdr = 8
        if size == 1: size = struct.unpack(">Q", data[i+8:i+16])[0]; hdr = 16
        if size == 0: size = end - i
        yield typ.decode("latin1"), i + hdr, i + size
        i += size

def full(data, s):  # version, flags, payload start
    return data[s], s + 4

def parse(path):
    d = open(path, "rb").read()
    meta = next((s, e) for t, s, e in boxes(d, 0, len(d)) if t == "meta")
    ms = meta[0] + 4
    sub = {t: (s, e) for t, s, e in boxes(d, ms, meta[1])}
    # pitm
    v, p = full(d, sub["pitm"][0]); primary = struct.unpack(">H" if v == 0 else ">I", d[p:p+(2 if v == 0 else 4)])[0]
    # iinf
    v, p = full(d, sub["iinf"][0]); n = struct.unpack(">H" if v == 0 else ">I", d[p:p+(2 if v == 0 else 4)])[0]; p += 2 if v == 0 else 4
    itypes = {}
    for t, s, e in boxes(d, p, sub["iinf"][1]):
        v2, q = full(d, s)
        if v2 >= 2:
            iid = struct.unpack(">H" if v2 == 2 else ">I", d[q:q+(2 if v2 == 2 else 4)])[0]; q += (2 if v2 == 2 else 4) + 2
            itypes[iid] = d[q:q+4].decode("latin1")
    idat0 = sub["idat"][0] if "idat" in sub else 0
    # iloc
    v, p = full(d, sub["iloc"][0])
    a = d[p]; b = d[p+1]; off_s, len_s, base_s = a >> 4, a & 15, b >> 4; idx_s = b & 15 if v in (1, 2) else 0; p += 2
    cnt = struct.unpack(">H" if v < 2 else ">I", d[p:p+(2 if v < 2 else 4)])[0]; p += 2 if v < 2 else 4
    rd = lambda n_: (int.from_bytes(d[p:p+n_], "big") if n_ else 0)
    loc = {}
    for _ in range(cnt):
        iid = int.from_bytes(d[p:p+(2 if v < 2 else 4)], "big"); p += 2 if v < 2 else 4
        cm = 0
        if v in (1, 2): cm = int.from_bytes(d[p:p+2], "big") & 15; p += 2
        p += 2  # data ref
        base = rd(base_s); p += base_s
        ec = struct.unpack(">H", d[p:p+2])[0]; p += 2
        ext = []
        for _ in range(ec):
            if idx_s: p += idx_s
            o = rd(off_s); p += off_s; l = rd(len_s); p += len_s
            ext.append((base + o + (idat0 if cm == 1 else 0), l))
        loc[iid] = ext
    # iref dimg
    refs = {}
    v, p = full(d, sub["iref"][0])
    w = 2 if v == 0 else 4
    for t, s, e in boxes(d, p, sub["iref"][1]):
        fid = int.from_bytes(d[s:s+w], "big"); c = struct.unpack(">H", d[s+w:s+w+2])[0]
        to = [int.from_bytes(d[s+w+2+k*w:s+w+2+(k+1)*w], "big") for k in range(c)]
        refs.setdefault(t, {})[fid] = to
    # iprp: ipco + ipma
    iprp = {t: (s, e) for t, s, e in boxes(d, sub["iprp"][0], sub["iprp"][1])}
    props = [(t, s, e) for t, s, e in boxes(d, iprp["ipco"][0], iprp["ipco"][1])]
    v, p = full(d, iprp["ipma"][0]); flags = int.from_bytes(d[iprp["ipma"][0]+1:iprp["ipma"][0]+4], "big")
    ec = struct.unpack(">I", d[p:p+4])[0]; p += 4
    assoc = {}
    for _ in range(ec):
        iid = int.from_bytes(d[p:p+(2 if v < 1 else 4)], "big"); p += 2 if v < 1 else 4
        k = d[p]; p += 1; lst = []
        for _ in range(k):
            if flags & 1: x = struct.unpack(">H", d[p:p+2])[0] & 0x7FFF; p += 2
            else: x = d[p] & 0x7F; p += 1
            lst.append(x)
        assoc[iid] = lst
    return d, primary, itypes, loc, refs, props, assoc

def hvcc_to_annexb(d, s, e):
    p = s + 22; n = d[p]; p += 1; out = b""
    for _ in range(n):
        p += 1; cnt = struct.unpack(">H", d[p:p+2])[0]; p += 2
        for _ in range(cnt):
            l = struct.unpack(">H", d[p:p+2])[0]; p += 2
            out += b"\x00\x00\x00\x01" + d[p:p+l]; p += l
    return out

def length_to_annexb(buf):
    out = b""; i = 0
    while i + 4 <= len(buf):
        l = struct.unpack(">I", buf[i:i+4])[0]; out += b"\x00\x00\x00\x01" + buf[i+4:i+4+l]; i += 4 + l
    return out

def item_data(d, loc, iid):
    return b"".join(d[o:o+l] for o, l in loc[iid])

def decode_hevc(d, loc, props, assoc, iid):
    hv = next(props[x-1] for x in assoc[iid] if props[x-1][0] == "hvcC")
    stream = hvcc_to_annexb(d, hv[1], hv[2]) + length_to_annexb(item_data(d, loc, iid))
    r = subprocess.run(["ffmpeg", "-loglevel", "error", "-f", "hevc", "-i", "pipe:0", "-frames:v", "1", "-f", "image2pipe", "-vcodec", "png", "pipe:1"], input=stream, capture_output=True)
    return Image.open(io.BytesIO(r.stdout)).convert("RGB")

def rotation(d, props, assoc, iid):
    for x in assoc.get(iid, []):
        t, s, e = props[x-1]
        if t == "irot": return (d[s] & 3) * 90
    return 0

def main(src, dst):
    d, prim, it, loc, refs, props, assoc = parse(src)
    if it[prim] == "grid":
        g = item_data(d, loc, prim); flags = g[1]; rows, cols = g[2] + 1, g[3] + 1
        fs = 4 if flags & 1 else 2
        W = int.from_bytes(g[4:4+fs], "big"); H = int.from_bytes(g[4+fs:4+2*fs], "big")
        tiles = refs["dimg"][prim]
        first = decode_hevc(d, loc, props, assoc, tiles[0]); tw, th = first.size
        canvas = Image.new("RGB", (cols * tw, rows * th))
        for k, tid in enumerate(tiles):
            im = first if k == 0 else decode_hevc(d, loc, props, assoc, tid)
            canvas.paste(im, ((k % cols) * tw, (k // cols) * th))
        img = canvas.crop((0, 0, W, H))
    else:
        img = decode_hevc(d, loc, props, assoc, prim)
    rot = rotation(d, props, assoc, prim)
    if rot: img = img.rotate(rot, expand=True)  # irot is counter-clockwise
    img.thumbnail((1800, 1800)); img.save(dst, quality=88)

if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
