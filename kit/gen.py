L='<img src="img/logo_wh.png" style="height:38px;display:block">'
LB='<img src="img/logo_bk.png" style="height:38px;display:block">'
def dots(n): return '<div class="dots">'+''.join('<i class="on"></i>' if i==n else '<i></i>' for i in range(5))+'</div>'
def top(n): return f'<div class="top"><div class="logo">{L}</div>{dots(n)}</div>'
def photo(img,pos="50% 20%",h=380,extra=""):
    return f'<div class="frame" style="height:{h}px;position:relative;{extra}"><div style="position:absolute;inset:0;background:url(img/{img}) {pos}/cover;filter:grayscale(1) brightness(.8) contrast(1.05)"></div></div>'
s=[]
s.append(f'''<section class="v2">
<div class="fill" style="background-image:url(img/2810-19_capa.jpg);background-position:50% 30%"></div><div class="shade" style="background:linear-gradient(180deg,rgba(7,7,7,.1) 0%,rgba(7,7,7,.2) 40%,rgba(7,7,7,.88) 66%,#070707 84%)"></div>
<div class="top"><div class="logo">{L}</div><div class="tag or">Prova social</div></div>
<div class="body" style="bottom:170px;text-align:center">
<div class="sub m" style="font-size:40px;letter-spacing:.06em">2 empresas de São Luís. Números reais.</div>
<div class="t1" style="font-size:230px;margin:10px 0 6px;white-space:nowrap;text-shadow:0 10px 40px rgba(0,0,0,.6)">Prova</div>
<div class="t1" style="font-size:90px">Não é promessa.<br><span class="acc">É resultado.</span></div>
<div style="display:flex;justify-content:center;margin-top:44px"><div class="swipe">arraste para o lado <b></b></div></div></div></section>''')
s.append(f'''<section class="v2"><div class="lines"></div><div class="vig"></div>{top(0)}
<div class="body" style="top:200px">
<div class="sub acc" style="font-size:42px;letter-spacing:.08em">Seven Supplements · São Luís</div>
<div class="t1" style="font-size:96px;margin-top:14px">Estava travado.<br><span class="acc">Depois dobrou.</span></div>
<div style="margin-top:70px;display:grid;gap:22px">
<div class="box"><div class="k">Antes</div><div class="t1" style="font-size:150px;line-height:1.05;white-space:nowrap">R$ 90 mil</div><div class="sub m" style="font-size:40px">por mês</div></div>
<div class="box" style="border-color:var(--or);background:linear-gradient(135deg,rgba(253,82,2,.25),rgba(253,82,2,.05))"><div class="k">Depois</div><div class="t1 acc" style="font-size:150px;line-height:1.05;white-space:nowrap">R$ 200 mil+</div><div class="sub m" style="font-size:40px">por mês</div></div></div></div>
<div class="src" style="bottom:52px">Case Seven Supplements (Tadson). Resultados individuais.</div></section>''')
s.append(f'''<section class="light"><div class="grid"></div>
<div class="top"><div class="logo dk">{LB}</div><div class="tag dk">3 / 7</div></div>
<div class="body" style="top:230px">
<div class="sub" style="color:var(--or);font-size:42px;letter-spacing:.08em">Lavanderia 4 Estações</div>
<div class="t1" style="font-size:104px;color:#0a0a0a;margin-top:14px">Mais máquinas.<br><span class="hl">Mais caixa.</span></div>
<div style="margin-top:56px;display:grid;grid-template-columns:1fr 1fr;gap:22px">
<div style="background:#fff;border-radius:26px;padding:44px 36px;box-shadow:0 10px 30px rgba(0,0,0,.06)"><div class="t1" style="font-size:200px;color:var(--or);line-height:1">2x</div><div class="sub" style="color:#0a0a0a;font-size:44px">máquinas na operação</div></div>
<div style="background:#0a0a0a;border-radius:26px;padding:44px 36px"><div class="t1" style="font-size:200px;color:var(--or);line-height:1">+60%</div><div class="sub" style="font-size:44px">de faturamento</div></div></div>
</div>
<div style="position:absolute;left:80px;right:80px;bottom:150px;border:2px solid rgba(253,82,2,.6);border-radius:24px;padding:30px 36px;background:#fff"><div class="sub" style="color:var(--or);font-size:40px">A lição</div><div class="sub" style="color:#0a0a0a;font-size:42px;text-transform:none;font-weight:500;line-height:1.2">Máquina nova só paga quando a fila enche.</div></div>
<div class="src" style="bottom:52px">Case Lavanderia 4 Estações. Resultados individuais.</div></section>''')
s.append(f'''<section class="v2"><div class="lines"></div><div class="vig"></div>{top(2)}
<div class="body" style="top:180px">
<div class="t1" style="font-size:92px">+150 empresas.<br><span class="acc">6 anos de mercado.</span></div>
<div style="margin-top:36px">{photo("carlos_escritorio.jpg","50% 25%",640)}</div>
<div class="box" style="margin-top:34px"><div class="k">O que isso quer dizer</div><div class="v">Não é sorte de uma campanha. É método aplicado em empresa de São Luís, todo dia.</div></div></div></section>''')
s.append(f'''<section class="v2"><div class="lines"></div><div class="vig"></div>{top(3)}
<div class="body" style="top:200px">
<div class="t1" style="font-size:100px">Resultado vem de<br><span class="acc">3 coisas juntas</span></div>
<div style="margin-top:50px;display:grid;gap:24px">
<div class="box" style="display:flex;gap:30px;align-items:center"><span class="t1" style="font-size:96px;color:var(--or)">1</span><span class="sub" style="font-size:46px"><span class="acc">Atrair</span> cliente certo com tráfego pago</span></div>
<div class="box" style="display:flex;gap:30px;align-items:center"><span class="t1" style="font-size:96px;color:var(--or)">2</span><span class="sub" style="font-size:46px"><span class="acc">Atender</span> rápido, sem deixar lead esfriar</span></div>
<div class="box" style="display:flex;gap:30px;align-items:center"><span class="t1" style="font-size:96px;color:var(--or)">3</span><span class="sub" style="font-size:46px"><span class="acc">Vender</span> com time comercial treinado</span></div></div></div>
<div class="btn" style="bottom:90px"><span>Faltou uma, o dinheiro vaza</span><span>→</span></div></section>''')
s.append(f'''<section class="v2"><div class="fill" style="background-image:url(img/carlos_estudio2.jpg);background-position:50% 15%;filter:grayscale(1) brightness(.5)"></div><div class="shade" style="background:linear-gradient(180deg,rgba(7,7,7,.8) 0%,rgba(7,7,7,.85) 40%,#070707 85%)"></div>
<div class="top"><div class="logo">{L}</div>{dots(4)}</div>
<div class="body" style="top:260px">
<div class="sub acc" style="font-size:42px;letter-spacing:.08em">Pergunta pro dono</div>
<div class="t1" style="font-size:118px;margin-top:14px">E o seu número<br>de hoje,<br><span class="acc">é o que você queria?</span></div>
<div class="box" style="margin-top:56px;background:rgba(7,7,7,.8)"><div class="k">Se não é</div><div class="v">O problema quase nunca é o produto. É o caminho entre o anúncio e a venda.</div></div></div>
<div class="src" style="bottom:52px">Resultados individuais. Nenhum resultado é garantido.</div></section>''')
s.append(f'''<section class="v2"><div class="ctaph" style="background-image:url(img/carlos_palco.jpg)"></div><div class="vig"></div><div class="glow" style="opacity:.9;bottom:-300px"></div>
<div class="top"><div class="logo">{L}</div><div class="tag">7 / 7</div></div>
<div class="body" style="top:300px;z-index:3">
<div class="t1" style="font-size:104px">Quer ser o<br>próximo <span class="acc">caso real?</span></div>
<div class="sub m" style="margin-top:56px;font-size:44px">Comenta a palavra</div>
<div class="kw" style="margin-top:16px">ROCKET</div>
<div class="sub m" style="margin-top:36px;font-size:36px">e eu te chamo no direct. Ou clique em <span style="color:#fff">Enviar mensagem.</span></div></div>
<div class="bot"><span class="m">Rocket+ · São Luís</span><span class="m">+150 empresas atendidas</span></div></section>''')
open('2810-19.html','w').write('<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"><link rel="stylesheet" href="style.css"></head><body>\n'+'\n'.join(s)+'\n</body></html>')
