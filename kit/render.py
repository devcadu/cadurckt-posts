"""Templates de carrossel do @cadurckt — renderiza slides 1080x1350 em PNG.

Uso: python3 render.py spec.json pasta_saida/
spec = {"tipo": "card"|"tweet"|"revista"|"foto", "nome": "...", "avatar": "...", "slides": [...]}
Destaque em vermelho: envolver o trecho com [[ ]]. Negrito: ** **.
"""
import json, re, sys, html, base64, pathlib
from playwright.sync_api import sync_playwright

ROOT = pathlib.Path(__file__).parent
W, H = 1080, 1350
RED = "#E5231B"
HANDLE = "@cadurckt"
NAME = "Carlos Eduardo"

def b64(path, mime):
    return f"data:{mime};base64," + base64.b64encode(pathlib.Path(path).read_bytes()).decode()

FONTS = {
    "Anton": ROOT / "fonts/Anton-Regular.ttf",
    "Montserrat": ROOT / "fonts/Montserrat[wght].ttf",
    "InterTight": ROOT / "fonts/InterTight[wght].ttf",
}
FONT_CSS = "".join(
    f"@font-face{{font-family:'{n}';src:url({b64(p,'font/ttf')}) format('truetype');font-weight:100 900}}"
    for n, p in FONTS.items())
NOISE = b64(ROOT / "noise.png", "image/png")

BASE_CSS = f"""{FONT_CSS}
*{{margin:0;padding:0;box-sizing:border-box}}
html,body{{width:{W}px;height:{H}px;overflow:hidden}}
body{{font-family:'InterTight',sans-serif;-webkit-font-smoothing:antialiased;position:relative}}
.red{{color:{RED}}}
.grain{{position:absolute;inset:0;background:url({NOISE});background-size:540px 675px;mix-blend-mode:overlay;pointer-events:none}}
"""

def hl(text, cls="red"):
    t = html.escape(text)
    t = re.sub(r"\[\[(.+?)\]\]", rf'<span class="{cls}">\1</span>', t)
    t = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", t)
    return t.replace("\n", "<br>")

def img_src(path):
    if not path: return None
    p = pathlib.Path(path)
    if not p.is_absolute(): p = ROOT / p
    return b64(p, "image/png" if p.suffix.lower() == ".png" else "image/jpeg")

def counter(i, n, color="#ffffff88"):
    return f'<div style="position:absolute;top:56px;right:64px;font-family:InterTight;font-weight:600;font-size:26px;letter-spacing:2px;color:{color}">{i:02d}/{n:02d}</div>'

# ---------- 1. CARD DE FRASE (padrão do perfil) ----------
def card(s, spec, i, n):
    return f"""<style>{BASE_CSS}
body{{background:#fff;display:flex;align-items:center;padding:0 100px}}
.q{{font-weight:750;font-size:{s.get('tamanho',76)}px;line-height:1.08;letter-spacing:-2.8px;color:#0b0b0b;max-width:880px}}
.h{{margin-top:38px;font-weight:500;font-size:30px;color:#8a8a8a;letter-spacing:-.2px}}
</style><div><div class="q">{hl(s['texto'])}</div><div class="h">{HANDLE}</div></div>"""

# ---------- 2. HISTORINHA ESTILO TWEET ----------
VERIF = '<svg width="34" height="34" viewBox="0 0 24 24" style="margin-left:8px"><path fill="#1D9BF0" d="M22.5 12.5c0-1.58-.875-2.95-2.148-3.6.154-.435.238-.905.238-1.4 0-2.21-1.71-3.998-3.818-3.998-.47 0-.92.084-1.336.25C14.818 2.415 13.51 1.5 12 1.5s-2.816.917-3.437 2.25c-.415-.165-.866-.25-1.336-.25-2.11 0-3.818 1.79-3.818 4 0 .494.083.964.237 1.4-1.272.65-2.147 2.018-2.147 3.6 0 1.495.782 2.798 1.942 3.486-.02.17-.032.34-.032.514 0 2.21 1.708 4 3.818 4 .47 0 .92-.086 1.335-.25.62 1.334 1.926 2.25 3.437 2.25 1.512 0 2.818-.916 3.437-2.25.415.163.865.248 1.336.248 2.11 0 3.818-1.79 3.818-4 0-.174-.012-.344-.033-.513 1.158-.687 1.943-1.99 1.943-3.484zm-6.616-3.334l-4.334 6.5c-.145.217-.382.334-.625.334-.143 0-.288-.04-.416-.126l-.115-.094-2.415-2.415c-.293-.293-.293-.768 0-1.06s.768-.294 1.06 0l1.77 1.767 3.825-5.74c.23-.345.696-.436 1.04-.207.346.23.44.696.21 1.04z"/></svg>'

def tweet(s, spec, i, n):
    av = img_src(spec.get("avatar"))
    avatar = f'<div class="av" style="background-image:url({av})"></div>' if av else '<div class="av ph">CE</div>'
    img = img_src(s.get("imagem"))
    media = f'<div class="media" style="background-image:url({img});background-position:{s.get("foco","center")}"></div>' if img else ""
    size = s.get("tamanho") or (52 if media else 62)
    upper = "text-transform:uppercase;letter-spacing:-.5px;" if s.get("caixa_alta") else ""
    verif = VERIF if spec.get("verificado") else ""
    return f"""<style>{BASE_CSS}
body{{background:#fff;display:flex;flex-direction:column;justify-content:center;padding:0 92px}}
.top{{display:flex;align-items:center;gap:24px;margin-bottom:44px}}
.av{{width:120px;height:120px;border-radius:50%;background-size:cover;background-position:center;flex:none;box-shadow:0 0 0 1px #0001}}
.av.ph{{background:#111;color:#fff;font-weight:800;font-size:42px;display:flex;align-items:center;justify-content:center}}
.n{{font-weight:800;font-size:42px;color:#0f1419;letter-spacing:-.8px;display:flex;align-items:center}}
.u{{font-size:32px;color:#536471;margin-top:2px}}
.t{{font-weight:420;font-size:{size}px;line-height:1.24;color:#0f1419;letter-spacing:-1px;{upper}}}
.t b,.t .red{{font-weight:750}}
.media{{margin-top:46px;width:100%;height:540px;border-radius:30px;background-size:cover;box-shadow:0 24px 50px -20px #0005,0 0 0 1px #0001}}
</style>
<div class="top">{avatar}<div><div class="n">{NAME}{verif}</div><div class="u">{HANDLE}</div></div></div>
<div class="t">{hl(s['texto'])}</div>{media}"""

# ---------- 3. HISTORINHA ESTILO REVISTA ----------
def revista(s, spec, i, n):
    if s.get("layout") == "capa":
        img = img_src(s.get("imagem"))
        bg = f"url({img}) {s.get('foco','center')}/{s.get('zoom','cover')} no-repeat, #111" if img else "radial-gradient(circle at 50% 30%,#3a3a3a,#0b0b0b 70%)"
        sub = f'<div class="sub">{hl(s["subtitulo"])}</div>' if s.get("subtitulo") else ""
        return f"""<style>{BASE_CSS}
body{{background:{bg}}}
.shade{{position:absolute;inset:0;background:linear-gradient(180deg,rgba(0,0,0,.25) 0%,rgba(0,0,0,0) 30%,rgba(0,0,0,.15) 50%,rgba(0,0,0,.92) 88%)}}
.wrap{{position:absolute;left:0;right:0;bottom:78px;padding:0 60px;text-align:center}}
.kick{{display:inline-block;background:#fff;color:#0b0b0b;font-weight:700;font-size:38px;letter-spacing:-.6px;padding:10px 26px 12px;box-shadow:0 12px 30px -8px #000a;transform:rotate(-1.2deg)}}
.kick .red{{font-weight:850}}
.ttl{{font-family:'Anton';font-size:{s.get('tamanho',250)}px;line-height:.88;text-transform:uppercase;color:#fff;margin-top:18px;
      text-shadow:0 14px 40px rgba(0,0,0,.65)}}
.sub{{display:inline-block;margin-top:22px;background:{RED};color:#fff;font-weight:700;font-size:36px;padding:8px 22px 10px}}
</style><div class="shade"></div><div class="grain" style="opacity:.22"></div>
<div class="wrap"><div class="kick">{hl(s.get('chamada',''))}</div><div class="ttl">{hl(s['titulo'])}</div>{sub}</div>"""
    img = img_src(s.get("imagem"))
    photo = f'<div class="ph" style="background:url({img}) {s.get("foco","center")}/cover"></div>' if img else ""
    return f"""<style>{BASE_CSS}
body{{background:radial-gradient(120% 80% at 50% 40%,#1d1d1d 0%,#0a0a0a 70%);display:flex;flex-direction:column;justify-content:center;align-items:center;text-align:center;padding:0 76px}}
.ph{{position:absolute;inset:0;filter:grayscale(1) contrast(1.1) brightness(.35)}}
.bar{{width:90px;height:10px;background:{RED};margin-bottom:46px;position:relative}}
.ttl{{font-family:'Anton';font-size:{s.get('tamanho',138)}px;line-height:.98;text-transform:uppercase;color:#fff;position:relative;text-shadow:0 10px 30px #000}}
.sub{{margin-top:46px;font-weight:450;font-size:42px;line-height:1.3;color:#d6d6d6;max-width:880px;position:relative;letter-spacing:-.5px}}
.sub b,.sub .red{{font-weight:750}}
.foot{{position:absolute;bottom:58px;font-weight:600;font-size:26px;color:#ffffff66;letter-spacing:2px}}
</style>{photo}<div class="grain" style="opacity:.16"></div>{counter(i,n)}
<div class="bar"></div><div class="ttl">{hl(s['titulo'])}</div><div class="sub">{hl(s.get('texto',''))}</div><div class="foot">{HANDLE}</div>"""

# ---------- 4. FOTO REAL + FRASE ----------
CAP = """font-family:'Montserrat';font-weight:800;color:#fff;text-align:center;letter-spacing:-1.2px;line-height:1.14;
-webkit-text-stroke:9px #000;paint-order:stroke fill;text-shadow:0 8px 24px rgba(0,0,0,.55);position:absolute;left:50px;right:50px"""
CAP_RED = f".c .red{{color:#fff;background:{RED};-webkit-text-stroke:0;text-shadow:none;padding:0 16px 4px;-webkit-box-decoration-break:clone;box-shadow:0 10px 26px -6px #000a}}"

def foto(s, spec, i, n):
    src = img_src(s["imagem"]); pos = s.get("foco", "center")
    if s.get("dividido"):
        src2 = img_src(s.get("imagem2") or s["imagem"]); pos2 = s.get("foco2", pos)
        return f"""<style>{BASE_CSS}
.h{{position:absolute;left:0;width:{W}px;height:{H//2}px;overflow:hidden}}
.a{{top:0;background:url({src}) {pos}/cover;filter:grayscale(1) contrast(1.12) brightness(.95)}}
.b{{top:{H//2}px;background:url({src2}) {pos2}/cover;filter:saturate(1.25) contrast(1.08) brightness(1.08)}}
.b::after{{content:'';position:absolute;inset:0;background:linear-gradient(180deg,#ffb238,#ff7a1a);mix-blend-mode:color;opacity:.38}}
.h::before{{content:'';position:absolute;inset:0;background:radial-gradient(120% 90% at 50% 40%,transparent 55%,rgba(0,0,0,.45));z-index:1}}
.line{{position:absolute;top:{H//2-3}px;left:0;right:0;height:6px;background:#000}}
.c{{{CAP};font-size:{s.get('tamanho',70)}px;z-index:3}} {CAP_RED}
</style><div class="h a"></div><div class="h b"></div><div class="line"></div><div class="grain" style="opacity:.14;z-index:2"></div>
<div class="c" style="bottom:{H//2+44}px">{hl(s['texto'])}</div>
<div class="c" style="bottom:52px">{hl(s['texto2'])}</div>"""
    where = s.get("posicao", "baixo")
    y = {"baixo": "bottom:110px", "cima": "top:110px", "meio": "top:50%;transform:translateY(-50%)"}[where]
    bw = "filter:grayscale(1) contrast(1.1);" if s.get("pb") else "filter:contrast(1.04) saturate(1.05);"
    return f"""<style>{BASE_CSS}
.bg{{position:absolute;inset:0;background:url({src}) {pos}/{s.get('zoom','cover')} no-repeat;{bw}}}
.v{{position:absolute;inset:0;background:radial-gradient(120% 85% at 50% 38%,transparent 50%,rgba(0,0,0,.5)),linear-gradient(180deg,transparent 58%,rgba(0,0,0,.55))}}
.c{{{CAP};{y};font-size:{s.get('tamanho',68)}px}} {CAP_RED}
</style><div class="bg"></div><div class="v"></div><div class="grain" style="opacity:.14"></div><div class="c">{hl(s['texto'])}</div>"""

FIT_JS = """() => {
  const sel = ['.q','.t','.ttl','.sub','.c','.kick'];
  const els = sel.flatMap(s => [...document.querySelectorAll(s)]);
  const out = () => els.some(e => { const r = e.getBoundingClientRect(); return r.top < 30 || r.bottom > 1320 || r.left < 20 || r.right > 1060; })
                    || document.body.scrollHeight > 1350;
  let k = 0;
  while (out() && k < 25) { els.forEach(e => { const fs = parseFloat(getComputedStyle(e).fontSize); e.style.fontSize = (fs * 0.95) + 'px'; }); k++; }
  return k;
}"""

RENDER = {"card": card, "tweet": tweet, "revista": revista, "foto": foto}

def main(spec_path, out_dir):
    spec = json.loads(pathlib.Path(spec_path).read_text())
    out = pathlib.Path(out_dir); out.mkdir(parents=True, exist_ok=True)
    fn = RENDER[spec["tipo"]]; n = len(spec["slides"]); files = []
    with sync_playwright() as p:
        b = p.chromium.launch(); pg = b.new_page(viewport={"width": W, "height": H})
        for i, s in enumerate(spec["slides"], 1):
            pg.set_content(f"<!doctype html><meta charset=utf-8><body>{fn(s, spec, i, n)}</body>")
            pg.evaluate("document.fonts.ready"); pg.wait_for_timeout(200)
            # auto-ajuste: diminui a letra se algum texto passar da arte
            pg.evaluate(FIT_JS)
            f = out / f"{spec.get('nome', spec['tipo'])}_{i:02d}.png"
            pg.screenshot(path=str(f), clip={"x": 0, "y": 0, "width": W, "height": H}); files.append(str(f))
        b.close()
    print("\n".join(files))

if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
