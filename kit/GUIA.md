# Guia de produção — Instagram Rocket+ (perfil da Rocket+, empresas de São Luís)

Este guia é a fonte da verdade para cada rodada agendada. Siga tudo à risca. Padrão visual aprovado pelo Carlos em 27/10/2026.

## 1. Público, tom e marca
- Público: donos de empresas de São Luís (todos os nichos) que faturam acima de R$ 50 mil/mês.
- Serviços da Rocket+: tráfego pago, produção de conteúdo, videomaker, IA no atendimento e treinamento comercial.
- Provas que PODEM ser usadas: +150 empresas de São Luís atendidas; mais de 6 anos de mercado; case Seven Supplements (Tadson, São Luís: de R$ 90 mil para mais de R$ 200 mil/mês); case Lavanderia 4 Estações (dobrou máquinas, +60% de faturamento). Nada além disso sem confirmação do Carlos.
- Tom: português do Brasil, direto, frases curtas, nada genérico. Sempre "você".
- Logo: `img/logo_wh.png` (fundos escuros/foto), `img/logo_bk.png` (fundos claros). Laranja da marca: #FD5202. Nome escrito: ROCKET+ (a logo mostra RCKT+).

## 2. Quadros e janelas do dia (1 carrossel por janela, 6 por dia: 7h, 11h, 14h, 16h, 18h, 19h30)
- **Janela 7h (topo):** primeiro pesquise notícias do dia/semana que afetem empresas (Meta, Instagram, WhatsApp, Google, economia, varejo, São Luís/Maranhão). Se houver notícia relevante e verificável → quadro **Rocket+ News**. Se não → **Caso de Marca** (história real de empresa nacional ou internacional com lição de marketing/gestão).
- **Janela 11h (educativo):** **Raio-X** — algo prático que a empresa aplica hoje (atendimento, WhatsApp, Google Perfil da Empresa, anúncios, conteúdo, comercial, pós-venda, recompra). Formato "N sinais / N erros / passo a passo", com checklist no penúltimo slide.
- **Janela 14h (autoridade):** alternar **Fala, Cadu** (opinião do Carlos na 1ª pessoa, com foto real dele), **Tese do Dono** (frase forte de gestão com personagem fictício gerado por IA) e **Bastidores/Resultados** (só com material real enviado pelo Carlos). Se a notícia do dia for forte, a janela 14h pode dar a visão do Carlos sobre ela.
- **Janela 16h (educativo 2):** **Raio-X** com foco em tráfego pago, Google e anúncios (palavra ADS de preferência), tema diferente do Raio-X das 11h.
- **Janela 18h (storytelling):** se a janela 7h foi Rocket+ News → **Caso de Marca**; se a 7h foi Caso de Marca → **Rocket+ News** (notícia da tarde) ou um segundo Caso de Marca de outro setor.
- **Janela 19h30 (fechamento do dia):** formato mais leve e de prova: **Tese do Dono**, **Mito x Verdade** do marketing, ou **Prova social** com os cases reais permitidos (Seven Supplements, Lavanderia 4 Estações). Não repetir o quadro usado às 14h.
- Antes de escolher o tema, leia `controle.md` e as linhas de HOJE: os 6 posts do dia precisam ter temas, quadros e imagens diferentes entre si: não repita tema, marca ou ângulo dos últimos 30 dias, e equilibre os quadros.

## 3. Regras de conteúdo (inegociáveis)
- Nunca inventar dados, números, depoimentos ou casos. Todo número vem de fonte pesquisada na hora (WebSearch/WebFetch) e entra no slide com linha "Fonte: <veículo>". Prefira fontes primárias e grandes veículos.
- Nunca usar foto, montagem ou imagem gerada com rosto de pessoa real/famosa. O famoso entra pelo NOME no título; a imagem é objeto-símbolo, cenário ou personagem fictício.
- Imagens geradas: sem logos, sem marcas, sem texto legível.
- Nunca prometer resultado garantido. Em resultados: "Resultados individuais".
- Texto sempre em HTML/CSS por cima da imagem, nunca gerado pela IA de imagem.

## 4. Padrão visual (copie dos modelos em `modelos/`)
Modelos aprovados: `modelos/modelo_caso_de_marca.html` (referência principal do padrão v2), `modelos/modelo_raiox.html`, `modelos/modelo_fala_cadu.html`. Use `style.css` (classes `.v2`, `.t1`, `.acc`, `.sub`, `.frame`, `.box`, `.lines`, `.vig`, `.fill`, `.shade`, `.tl`, `.ctaph`, `.kw`, `.light`, `.hl`, `.dots`, `.tag`).
- Formato 1080x1350, 6 a 7 slides.
- **Imagem em quase todo slide**: capa com foto/imagem full-bleed escurecida (`.fill` + `.shade`); internos com imagem em moldura arredondada (`.frame`) ou de fundo com degradê. No máximo 1–2 slides só tipográficos por carrossel.
- Tipografia: títulos em Anton caixa alta branca com a virada em laranja (`.acc`); evitar caixa laranja em tudo (caixa `.hl` só em fundo claro ou 1x por carrossel). Apoio em Barlow Condensed (`.sub`). Corpo em Inter só quando precisar.
- Alternar fundos: escuro `.v2` (com `.lines` e `.vig`), claro `.light` (papel com grade) e foto. Números grandes em Anton.
- Componentes: selos de dado sobre a foto, caixa "O problema"/"A lição" com borda laranja (`.box`), linha do tempo (`.tl`), indicador `.dots` no topo, botão laranja no rodapé puxando o próximo slide (`.btn`).
- Capa: título centralizado ou na base, máx. 3 níveis (linha pequena `.sub` + palavra gigante + frase), e pílula "arraste para o lado".
- **Último card (CTA) SEMPRE** com foto do Carlos em baixa opacidade (`.ctaph`, opacity .22, P&B) + "Comenta a palavra" + palavra do ManyChat em `.kw` + "e eu te chamo no direct. Ou clique em Enviar mensagem." + rodapé "Rocket+ · São Luís / +150 empresas atendidas". Isso vale para todos os formatos.

## 5. Palavras do ManyChat (só estas 4, sempre)
- **CRESCER** — gestão, crescimento, processos, casos de marca
- **VENDER** — atendimento, WhatsApp, comercial, vendas
- **ADS** — tráfego pago, anúncios, Meta/Google
- **ROCKET** — falar com o time / contratar
Escolha a que combina com o tema. Não invente outras.

## 6. Fotos reais (rodízio para não ficar repetitivo)
Fotos em `img/`: carlos_palco, carlos_estudio1, carlos_estudio2, carlos_escritorio (Carlos); time_dupla (Carlos + colega; recortar só o Carlos), time_mulher1 (colega do time — nome/cargo ainda não informados; NÃO usar até o Carlos confirmar).
- Consulte `controle.md`: a mesma foto não aparece em dias seguidos nem 2x no mesmo dia; varie recorte e tratamento (P&B, crop de rosto, corpo).
- Fotos sempre em P&B ou dessaturadas e escurecidas.

## 7. Geração de imagens (Canva + ElevenLabs econômico, com cota)
Decisão do Carlos (27/10/2026): mesclar Canva e ElevenLabs, gastando pouco saldo. Cotas rígidas:

| Janela | Fonte | Máx. por rodada |
|---|---|---|
| 07h | Canva | 1 imagem (capa) |
| 18h | ElevenLabs (modo econômico) | 1 imagem (capa) |
| 19h30 | ElevenLabs (modo econômico) | 1 imagem (capa) |
| 11h, 14h, 16h | nenhuma IA | 0 |
| refação | só se o Carlos pedir para trocar a imagem | 1, na mesma fonte da janela original |

- **Teto mensal:** Canva 35 imagens/mês; ElevenLabs 60 imagens/mês. Antes de gerar, some no `controle.md` (coluna "IA usada") quantas já saíram no mês corrente. Se bater o teto, não gere: use foto real.
- Demais slides e janelas: fotos reais do Carlos/time (seção 6), slides tipográficos e componentes gráficos do `style.css` (números grandes, telas de WhatsApp/painel feitas em HTML, linha do tempo, checklist, caixas). Se existir `banco/` com fotos no kit, use com rodízio.
- Nunca gerar de novo só para "tentar de novo": se a imagem ficar ruim, use foto real.
- Registre no `controle.md`, na coluna "IA usada", a fonte e quantidade (ex.: `canva 1`, `eleven 1`, `nenhuma`).

### 7A. ElevenLabs (modo econômico: 18h e 19h30)
`creative_create_flow` → `creative_add_flow_node` (node_type `image-generation`, model `gpt-image-2.5-sunburst`, model_parameters `{"aspect_ratio":"4:5","resolution":"1K","quality":"medium"}`) com o prompt → `creative_run_flow_nodes` com **generations_count 1** → consulte `creative_get_flow_run_status` (esperando o poll_after_seconds) até concluir → baixe o `content_url` com curl para `img/<post_id>_capa.png` (esse domínio o sandbox acessa) → redimensione para 1080 de largura. NUNCA use 2K/4K, quality high/max, nem mais de 1 geração. Nunca repita a chamada.

### 7B. Canva (janela 7h)
1. Gerar: `generate-image` (Canva) com `aspectRatio` `PORTRAIT_4_5` (capa/fundo full-bleed) ou `LANDSCAPE_4_3` (imagem em `.frame`). Prompt em inglês: "Cinematic photorealistic photo of …, dark moody, warm orange light, film grain, empty space for text. No text, no logos, no brand names, no readable signs, no recognizable faces." Depois `get-generate-image-job` até SUCCESS (espere ~20 s entre consultas com uma espera em loop, não com sleeps encadeados). Anote o media id (MA…). Olhe a prévia; se ficar ruim, gere UMA nova com outro prompt (máx. 1 refação por imagem). Nunca rosto de pessoa real/famosa.
2. Alta resolução (a prévia do Canva é minúscula): `copy-design` da moldura **DAHZLHQqHQk** com `page_numbers [1]` → novo design. `read-design` dele com `open_transaction: true` e `fields ["design_content"]`. Na página 1: `delete_element` do elemento existente e `insert_fill` da 1ª imagem. Para cada imagem extra: `add_page` (1080x1440), leia de novo os IDs das páginas (`read-design` com o transaction_id e `page_indices`) e faça `insert_fill` nela. Posição: retrato → top 0, left -41, width 1162, height 1440; paisagem → top 0, left 0, width 1080, height 810. Depois `edit-design` com `finalize: "commit"`.
3. Exportar: `export-design` do design copiado, `{"type":"jpg","quality":95,"width":1080}` → lista de URLs (uma por página, em ordem).
4. Baixar: o sandbox não acessa o Canva; quem baixa é o robô do GitHub (Action `baixar-imagens` no repo devcadu/cadurckt-posts). Garanta o repo clonado (seção 10, passo 2), escreva `lista.txt` com uma linha por imagem `nome.jpg|URL|retrato` (ou `paisagem`) e rode `python3 tools/baixar_imagens.py lista.txt` na pasta do kit. As imagens chegam em `img/` (retrato 1080x1440, paisagem 1080x810). Nomeie `<post_id>_capa.jpg`, `<post_id>_2.jpg`…
5. Olhe cada imagem baixada (Read) antes de usar. Se o Canva disser que o limite de IA acabou, avise o Carlos no app (SendUserMessage) e faça o carrossel só com fotos reais e componentes gráficos.

## 8. Montagem e checagem
1. `cd` na pasta do kit, `npm i @fontsource/anton @fontsource/inter @fontsource/barlow-condensed` (as fontes ficam em `node_modules`).
2. Escreva o carrossel em `<slug>.html` na raiz do kit (mesmo padrão dos modelos, caminhos `style.css` e `img/...`).
3. `python3 render.py <slug>` → PNGs em `out/<slug>/` e folha em `out/<slug>_folha.png`.
4. Leia a folha e cada slide suspeito: nada cortado ou vazando, sem palavra órfã no título, texto longe do rodapé, contraste ok, logo presente, CTA com foto e palavra. Corrija e renderize de novo até ficar limpo.
5. Zip numerado na ordem de postar.

## 9. Legenda
Gancho (situação/pergunta + emoji) → explicação curta → lista com emojis numerados → virada para a Rocket+ em 1 frase → CTAs: "📌 Salva…" e "💬 Comenta PALAVRA que eu te chamo no direct, ou clique no botão Enviar mensagem." → exatamente 5 hashtags em minúsculas (sempre incluir #saoluis e #rocketmais).
Se houver números, citar a fonte no fim da legenda.

## 10. Entrega (WhatsApp + app)
1. Converta os slides para JPG (qualidade 92, 1080x1350) com nomes 01.jpg, 02.jpg…
2. Hospedagem pública: chame `add_repo` (owner devcadu, repo cadurckt-posts, access push), clone raso em `/home/claude/cadurckt-posts`, copie os JPGs para `rocketmais/<AAAA-MM-DD>_<janela>/` (ex.: `rocketmais/2026-10-28_07h/`), faça commit e push na main. URLs públicas: `https://raw.githubusercontent.com/devcadu/cadurckt-posts/main/rocketmais/<pasta>/01.jpg` (confira com curl que voltam 200).
3. Código do post (`post_id`): `DDMM-HH` da janela (ex.: 2810-07, 2810-11, 2810-14, 2810-16, 2810-18, 2810-19). Em refação, mantenha o mesmo código.
4. Envie para aprovação pelo Make: `scenarios_run` no cenário **8200349** ("Rocket+ — 1. Enviar post para aprovação") com `responsive: true` e `data`: post_id, janela, quadro, tema, legenda (pronta para publicar), imagens (array de URLs na ordem) e telefone `5598981620090`. Se falhar, confira a execução (`executions_get-detail`) e tente de novo uma única vez.
5. Também mande no app: SendUserFile (status proactive) com a folha de contato, e SendUserMessage curto com quadro, tema, código e fontes.
6. A publicação acontece só quando o Carlos responde APROVADO no WhatsApp (cenário 8200365 publica no @agenciarocketmais). NUNCA publique por conta própria.
7. Atualize `controle.md` (data, janela, código, quadro, tema, palavra, fotos usadas, status: aguardando aprovação) e republique só esse arquivo no artifact do kit.

## 11. Refação (rodada de hora em hora)
- Leia no Make o data store **234471** ("Posts Rocket+") os registros com `status = refazer`. Para cada um: leia `feedback`, refaça o carrossel seguindo o pedido (mesmo quadro e tema, salvo se o pedido mudar), suba em `rocketmais/<pasta-original>_v2/` (v3, v4…), e reenvie pelo cenário 8200349 com o MESMO post_id (isso volta o status para pendente). Registre no `controle.md`.
