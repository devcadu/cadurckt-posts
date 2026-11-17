#!/usr/bin/env python3
"""Baixa imagens exportadas do Canva usando o robô do GitHub (o sandbox não acessa o Canva direto).

Uso: python3 tools/baixar_imagens.py <lista.txt>
Cada linha da lista:  nome_local.jpg|URL_de_export_do_Canva|retrato   (ou paisagem)
- retrato  -> página 1080x1440 exportada inteira (use com background-size:cover)
- paisagem -> a imagem ocupa o topo 1080x810 da página; o script recorta esse pedaço
Resultado: arquivos em img/ (pasta do kit). Requer o repo clonado em /home/claude/cadurckt-posts.
"""
import sys, os, time, subprocess, shutil
from PIL import Image

REPO = "/home/claude/cadurckt-posts"
KIT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def git(*a):
    return subprocess.run(["git", "-C", REPO, *a], capture_output=True, text=True)

linhas = [l.strip() for l in open(sys.argv[1]) if l.strip()]
lote = time.strftime("%Y%m%d_%H%M%S")
git("pull", "-q")
os.makedirs(f"{REPO}/pedidos", exist_ok=True)
itens = []
with open(f"{REPO}/pedidos/{lote}.txt", "w") as f:
    for l in linhas:
        nome, url, tipo = l.split("|", 2)
        destino = f"banco/canva/{lote}/{nome}"
        f.write(f"{destino}|{url}\n")
        itens.append((nome, destino, tipo.strip()))
git("add", "pedidos"); git("commit", "-qm", f"pedido {lote}"); r = git("push", "-q")
if r.returncode: print(r.stderr); sys.exit(1)

for _ in range(40):  # até ~4 min
    time.sleep(6); git("pull", "-q")
    if all(os.path.exists(f"{REPO}/{d}") for _, d, _ in itens): break
falhas = []
for nome, d, tipo in itens:
    p = f"{REPO}/{d}"
    if not os.path.exists(p): falhas.append(nome); continue
    im = Image.open(p).convert("RGB")
    if tipo == "paisagem": im = im.crop((0, 0, 1080, 810))
    im.save(f"{KIT}/img/{nome}", quality=94)
    print("OK", f"img/{nome}", im.size)
if falhas: print("FALHOU:", falhas); sys.exit(1)
