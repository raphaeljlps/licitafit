# Dossiê de Mercado — LicitaFit

**Produto:** LicitaFit (Launchbase Tecnologia Ltda — CNPJ 35.078.004/0001-77)  
**Escopo:** Mercado B2B brasileiro — matching de catálogo de distribuidores de TI a licitações/PNCP, vendido como API embutível a vendors de ERP/software comercial.  
**Data de elaboração:** 25/09/2026 (America/Sao_Paulo)  
**Idioma:** Português brasileiro  
**Classificação:** Pesquisa estratégica — evidências e proxies; números inventados são proibidos.

---

## 1. Resumo executivo

O LicitaFit atua na interseção de três mercados: (i) **compras públicas** centralizadas no Portal Nacional de Contratações Públicas (PNCP) sob a Lei nº 14.133/2021; (ii) **distribuição de TIC** no Brasil, que movimentou **R$ 30,7 bilhões em 2025** (+7% a/a), com hardware respondendo por **44,5%** do faturamento dos associados Abradisti; e (iii) **software de gestão e força de vendas** usado por atacadistas/distribuidores (ERP, AFV, WMS comerciais).

A oportunidade específica **não** é ser mais um portal de alerta de editais (espaço já ocupado por ConLicitação, Licitei, Sollicita e similares), nem um chatbot genérico de “IA lê o edital”. É ser a **camada de decisão-suporte catalog-aware** — matching entre SKUs/especificações do catálogo do distribuidor e itens de contratações públicas — entregue via **API/webhooks embutíveis** no ERP ou software comercial do parceiro, com status explícito `needs_review` (não elegibilidade jurídica).

**Por que agora.** A Lei 14.133 tornou a divulgação no PNCP obrigatória e centralizada; APIs oficiais de **consulta pública** (sem autenticação para leitura) e manuais de integração (versão 2.6, atualizada em 31/08/2026) permitem ingestão estruturada de contratações, itens, documentos, atas e contratos. O governo segue como fatia relevante (~20% dos investimentos em TIC no país, segundo Abradisti/IT Data), ainda que tenha sido fraco em 2025 — o que aumenta a pressão dos canais por **qualificação melhor** das oportunidades, não por mais volume bruto de alertas.

**Preço público na landing (API parceiro):** R$ 50 por 1.000 requests, **mínimo R$ 490/mês**, e monitoramento a **R$ 1,90 por licitação monitorada / mês**. Cobrança alinhada a uso (sem métricas inventadas de volume). O **Dashboard B2B** usa assinatura de **R$ 399/mês** + **R$ 5 por licitação monitorada / mês**, sem cobrança por request; o monitoramento é superior aos R$ 1,90 da API. Validar contra: (a) valor percebido pelo vendor; (b) mix requests + monitoramento por partner; (c) preços opacos de plataformas de inteligência de licitação. Recomendação: manter o floor de R$ 490, observar overage de requests/monitoramento e **revenue share** opcional com early partners.

**Go-to-market prioritário:** vendas a **fundadores/PMs/parcerias** de ERPs e softwares comerciais para distribuição/atacado de TI (não Conta Azul / e-commerce genérico). ICP exemplificado neste dossiê inclui Onclick, Soften, Softcom, SIAC, ecossistema Winthor/TOTVS (Nextera, MáximaTech, PowerGO), Sankhya, CIGAM, ATS Resulth, Lexos, JD System, entre outros.

**Riscos-chave:** cobertura incompleta municipal/estadual apesar do PNCP; qualidade variável de descrições de itens; responsabilidade jurídica se o produto for interpretado como “aprovação legal”; LGPD sobre catálogos de parceiros; schema drift das APIs.

**Próximo passo de 30–60 dias:** 3–5 design partners com catálogo real (notebooks/monitores), pipeline PNCP→match→`needs_review`, e 10 conversas discovery com buyers do ICP.

---

## 2. Problema e oportunidade

### 2.1 Dor do distribuidor de TI (usuário econômico final)

Distribuidores e atacadistas de informática que vendem ao setor público enfrentam:

| Dor | Manifestação típica | Por que LicitaFit cabe |
| --- | --- | --- |
| Ruído de oportunidades | Alertas por palavra-chave (“notebook”, “monitor”) geram milhares de editais irrelevantes (serviços de TI, impressão, manutenção, itens fora do mix) | Matching contra **catálogo real** (SKU, marca, CPU, RAM, tela, garantia) |
| Retrabalho entre sistemas | Equipe gov em planilha; estoque/preço no ERP; AFV separado | API no fluxo do ERP/parceiro |
| Specs vs. edital | Edital pede “notebook Intel i5 16GB 512GB SSD 15,6” FHD”; cadastro tem 40 SKUs próximos | Score + `needs_review` + evidências |
| Tempo de resposta | Pregões eletrônicos com janelas curtas | Qualificação precoce (PCA + publicação) |
| Risco operacional | Apostar em item sem estoque/margem/substituição tributária | Integração futura com disponibilidade/preço do ERP (fora do MVP, mas narrativa) |

Fontes de contexto setorial: Abradisti (hardware como pilar; governo ~20% dos investimentos TIC, desempenho fraco em 2025); Onclick e SIAC documentam dores de serial/RMA/ST típicas do segmento — o mesmo perfil de empresa que precisa de ops rígidas **e** de oportunidade B2G.

### 2.2 Dor do ERP / software comercial (comprador primário)

Vendors que servem distribuidores:

- Diferenciação de produto: “módulo licitações” genérico (gestão de proposta/empenho) **sem** discovery inteligente de oportunidades alinhadas ao catálogo.
- Churn/expansão: clientes que vendem ao governo pedem integração com alertas externos (ConLicitação etc.) — o ERP perde a experiência e a dados.
- Roadmap: construir crawler multi-portal + matching NLP é caro e fora do core; **white-label/API** é caminho mais barato.

Exemplos de módulos nativos ou adjacentes (gestão pós-oportunidade, não matching catalog-first): Nextera Licitações (Winthor), JD System WSGE Licitações, Licitações by Portal de Compras Públicas (lado órgão/TOTVS Protheus).

### 2.3 Dor das equipes de vendas / gov sales

Força de vendas e times de licitação gastam tempo em triagem manual. Ferramentas de mercado resolvem **descoberta ampla** e, cada vez mais, “pergunte ao edital” (IA sobre PDF). Continuam fracas em: *“dado o meu catálogo desta semana, quais itens deste aviso eu realmente posso ofertar?”* — exatamente o gap do LicitaFit.

### 2.4 Framing da oportunidade

LicitaFit é **decision-support**:

- **Não** substitui análise jurídica do edital.
- **Não** declara elegibilidade ou compliance.
- **Sim** ranqueia/filtra oportunidades e itens com evidência de match e força humano a revisar (`needs_review`).

Isso reduz risco de produto e diferencia de chatbots “AI for editais”.

---

## 3. Mercado-alvo

### 3.1 Compras públicas no Brasil

**Marco legal.** A Lei nº 14.133, de 1º de abril de 2021, estabelece normas gerais de licitação e contratação para a administração pública. O **PNCP** é o sítio oficial de divulgação centralizada e obrigatória dos atos exigidos pela lei ([gov.br/compras — NLLC](https://www.gov.br/compras/pt-br/nllc); [gov.br — PNCP](https://www.gov.br/rededeparcerias/pt-br/servicos/portal-nacional-de-contratacoes-publicas-pncp)).

**Papel do PNCP.** Centraliza PCA (Planos de Contratações Anuais), editais/avisos, atas de registro de preços, contratos e dados estatísticos; disponibiliza APIs e dados abertos para integração.

**Volume.** Não há, neste dossiê, um número oficial IBGE/MGI auditado pelo autor para “total de compras públicas 2025” obtido diretamente de painel governamental no momento da pesquisa. Claims de mercado (ex.: ATA360 citando PNCP/MGI: **mais de R$ 1 trilhão** e **mais de 1 milhão de processos** em 2025, ~12–16% do PIB) devem ser tratados como **estimativas de terceiros** até cruzamento com painéis oficiais do PNCP/MGI. **Proxy qualitativo:** o mercado é estruturalmente grande, multi-esfera (União, estados, 5.570 municípios) e digitalmente mais centralizado pós-14.133.

**Tendências relevantes ao LicitaFit:**

1. Obrigação de publicação no PNCP → **fonte canônica preferencial** para ingestão.
2. Persistência de portais de disputa (Compras.gov.br, Licitar Digital, BLL, BNC, etc.) → PNCP não elimina a necessidade de link ao sistema de origem (`linkSistemaOrigem`).
3. Categoria de processo **Informática (TIC)** e itens de PCA “Soluções de TIC” existem nas tabelas de domínio oficiais — úteis para filtragem.
4. Margens de preferência e conteúdo nacional aparecem em campos de item (API de itens) — relevantes para notebooks/hardware com incentivo.

### 3.2 Distribuição de hardware de TI / canal B2G

| Indicador | Valor | Fonte | Acesso |
| --- | --- | --- | --- |
| Faturamento distribuição TIC Brasil 2025 | R$ 30,7 bilhões | Abradisti / IT Data — Estudo Setorial 2026 | 25/09/2026 |
| Crescimento 2025 | +7% a/a | Idem | Idem |
| Representatividade Abradisti | 51 distribuidores = 87% do setor | Idem | Idem |
| Share hardware no faturamento associados | 44,5% | Idem | Idem |
| Governo nos investimentos TIC (contexto) | ~20%; desempenho fraco em 2025 | Idem | Idem |
| Projeção crescimento distribuição 2026 (média) | ~6% | Idem | Idem |
| Censo revendas 2025 | +9,4% (1.176 respostas) | Abradisti 15º Censo | Idem |

**Implicação:** mesmo com governo fraco em 2025, o canal continua estruturado (distribuidores + milhares de revendas). Hardware permanece o maior bloco — alinhado ao start do LicitaFit (notebooks/monitores).

**Proxy ABINEE (indústria, não distribuição):** setor eletroeletrônico R$ 270,8 bi em 2025; área de Informática R$ 47,753 bi (+12% nominal / +9% real) — [ABINEE](https://www.abinee.org.br/faturamento-do-setor-em-2025/). Útil como contexto de oferta, não como TAM do LicitaFit.

### 3.3 Vendors de software (ERP / força de vendas / comercial)

Segmentos de software relevantes (não exaustivo):

1. **ERP para distribuição/atacado** com clientes de informática (Onclick, Soften, Softcom, SIAC, ATS Resulth, Lexos, Target, CIGAM, Sankhya, TOTVS Winthor/Protheus).
2. **Força de vendas (AFV)** integrada a esses ERPs (MáximaTech, PowerGO e similares).
3. **Módulos de licitação já existentes** (Nextera, JD System) — potenciais **parceiros de complementaridade** ou concorrentes parciais (pós-match / gestão de contrato, não discovery catalog-aware).

**Fora do ICP (exemplos):** Conta Azul (MEI/PME serviços genéricos); Bling (e-commerce); ERPs só varejo puro sem atacado B2B.

### 3.4 TAM / SAM / SOM (com premissas transparentes)

> **Aviso:** abaixo é **framing estimativo**. Onde não há dado público, a célula é marcada como *estimativa/proxy*. Não usar como forecast financeiro auditado.

| Camada | Definição operacional | Ordem de grandeza | Premissas / status do dado |
| --- | --- | --- | --- |
| **TAM (mercado amplo)** | Valor econômico de software/serviços de inteligência e gestão de vendas ao governo no Brasil + spend em ferramentas de alerta/licitação por empresas fornecedoras | **Não quantificado com rigor neste dossiê** | Sem estatística oficial consolidada de “gasto das empresas com software de licitação”. Proxy: compras públicas totais (claims ~R$ 1 tri) são **GSV público**, não receita de software. |
| **SAM (mercado servível)** | Vendors de ERP/AFV/comercial que atendem **distribuidores/atacadistas de TIC** no Brasil + seus clientes finais com operação B2G de hardware | **Estimativa qualitativa: dezenas de vendors relevantes; milhares de distribuidores/revendas no ecossistema Abradisti** | 51 distribuidores grandes + 1.176+ revendas no censo; número de ERPs especializados = lista ICP (§8), não censo completo. |
| **SOM (mercado obtível 3 anos)** | Receita LicitaFit de **software partners** (floor R$ 490/mês + usage de requests e monitoramento) × N partners ativos | **Exemplo ilustrativo (não forecast):** 20 partners no floor = R$ 9,8 mil MRR base; usage e monitoramento empurram ARPU acima do mínimo | Depende de win rate, mix de requests/monitoramento e se há fee por tenant/distribuidor. |

**Proxy útil para pricing do partner:** se um ERP embute LicitaFit e cobra do distribuidor um add-on de R$ 200–500/mês (estimativa a validar), o partner ainda tem margem com o floor LicitaFit de R$ 490/mês a partir de ~1–3 clientes ativos (usage adicional de requests/monitoramento escala com o uso) — tese de partner-led growth.

**Volume de matching (produto):** indisponível neste dossiê o volume oficial filtrado “apenas notebooks/monitores no PNCP 2025”. Deve ser medido no experimento de 30 dias via API de consulta + filtro de itens (§12).

---

## 4. Fontes de dados públicos — ONDE obter

### 4.1 PNCP — Portal Nacional de Contratações Públicas

| Recurso | URL | Uso para LicitaFit | Auth |
| --- | --- | --- | --- |
| Portal | https://pncp.gov.br | UI, validação manual | Público |
| Manual de Integração v2.6 | https://pncp.gov.br/manual/pt-br/latest/ | Schema de escrita/consulta detalhada; histórico 31/08/2026 | Público |
| API manutenção (órgãos/plataformas) | `https://pncp.gov.br/api/pncp` | Não é o caminho principal do LicitaFit (envio de compras) | JWT (login + Bearer; token ~1h) |
| Swagger manutenção | https://pncp.gov.br/api/pncp/swagger-ui/index.html | Exploração | — |
| Homologação | https://treina.pncp.gov.br / `.../api/pncp` | Testes | Credenciais de treino |
| **API de Consultas (leitura)** | `https://pncp.gov.br/api/consulta` | **Ingestão principal** | Consulta pública (sem login para leitura) |
| Swagger consultas | https://pncp.gov.br/api/consulta/swagger-ui/index.html | Contratos OpenAPI | — |
| Dados abertos (página) | https://www.gov.br/pncp/pt-br/acesso-a-informacao/dados-abertos | Catálogo de downloads/APIs | Público |
| CSV anuais (repositório) | https://repositorio.dados.gov.br/seges/comprasgov/anual/ | Backfill / analytics | Público |

**Endpoints de consulta (Manual API Consultas v1.0 — documentação pública espelhada / oficial):**

| Endpoint | Função |
| --- | --- |
| `GET /v1/contratacoes/publicacao` | Contratações por data de publicação (`dataInicial`, `dataFinal` AAAAMMDD, `codigoModalidadeContratacao` obrigatório, paginação) |
| `GET /v1/contratacoes/proposta` | Contratações com recebimento de propostas em aberto |
| `GET /v1/atas` | Atas de RP por vigência |
| `GET /v1/contratos` | Contratos/empenhos por publicação |
| `GET /v1/pca/` e `/v1/pca/usuario` | Itens de PCA (planejamento — sinal precoce) |

**Detalhe de contratação/itens/documentos** (Manual Integração — base `api/pncp`, GETs tipicamente públicos):

| Endpoint | Função |
| --- | --- |
| `GET /v1/orgaos/{cnpj}/compras/{ano}/{sequencial}` | Cabeçalho da contratação |
| `GET /v1/orgaos/{cnpj}/compras/{ano}/{sequencial}/itens` | **Lista de itens** (core do matching) |
| `GET .../itens/{numeroItem}` | Item unitário |
| Documentos da contratação | Consulta de anexos (edital, TR, etc. — ver manual seções de documentos) |

**Campos de item relevantes ao matching (amostra oficial):** `numeroItem`, `descricao` (até 2048), `quantidade`, `unidadeMedida`, `valorUnitarioEstimado`, `valorTotal`, `materialOuServico`, `catalogoCodigoItem`, `catalogo` (objeto), `ncmNbsCodigo`, `ncmNbsDescricao`, `informacaoComplementar`, benefícios ME/EPP, margens de preferência, `orcamentoSigiloso`, situação do item.

**Campos de contratação úteis:** `objetoCompra`, `modalidadeNome`, `dataAberturaProposta` / `dataEncerramentoProposta`, `orgaoEntidade`, `unidadeOrgao` (UF/município), `linkSistemaOrigem`, `srp`, `valorTotalEstimado`, `numeroControlePNCP`.

**Rate limits:** o manual enfatiza paginação (`tamanhoPagina` até 500 em vários serviços; default menor em publicacao). **Limite explícito de RPS não foi encontrado** na documentação pública revisada em 25/09/2026 — tratar como risco operacional (backoff, cache, respeito a 429/5xx).

**Cobertura vs. gaps:** PNCP é obrigatório na 14.133, mas a qualidade/completude depende do sistema de origem e do órgão. Gaps típicos: atraso de publicação; itens pobres (“aquisição de equipamentos de informática”); anexos essenciais só em PDF; municípios pequenos com adesão irregular histórica (tendência de melhora, não garantia de 100%).

### 4.2 Compras.gov.br / ComprasNet (federal)

| Recurso | URL |
| --- | --- |
| Portal de Dados Abertos Compras | https://www.gov.br/compras/pt-br/cidadao/portal-de-dados-abertos |
| API dados abertos (Swagger) | https://dadosabertos.compras.gov.br/swagger-ui/index.html |
| Catálogo de materiais | https://catalogo.compras.gov.br/ |
| Nova Lei / PNCP (contexto) | https://www.gov.br/compras/pt-br/nllc |

Uso: complementar federal (SIASG/Compras.gov), CATMAT/códigos de catálogo, preços de referência — **não substitui** PNCP multi-esfera.

### 4.3 Outras fontes

| Fonte | URL / nota | Uso |
| --- | --- | --- |
| dados.gov.br / repositório SEGES | https://repositorio.dados.gov.br/seges/comprasgov/anual/ | Bulk CSV |
| TCU / Painéis | Portais de transparência e fiscalização | Contexto, sanções (não core MVP) |
| Diários Oficiais | Ainda usados por agregadores legados | Preferir PNCP; DO como fallback histórico |
| Portais de disputa | ComprasNet, Licitar Digital, BLL, BNC, Licitações-e, etc. | `linkSistemaOrigem`; não scrapear ToS à toa |

### 4.4 Anexos (editais PDF/DOC)

- Contratações no PNCP exigem documento anexo na publicação (manual de inserção).
- APIs de consulta de documentos retornam URIs/metadados; download do arquivo segue links oficiais.
- Extensões aceitas estão em tabelas de domínio do manual.
- **Para matching MVP:** priorizar **itens estruturados** (`descricao`, NCM, código catálogo). PDF/TR como enriquecimento assíncrono (OCR/NLP) com custo e risco maiores — nunca como única fonte de “elegibilidade”.

### 4.5 Dados de catálogo do parceiro (entrada LicitaFit)

Formatos esperados (sugestão de contrato de API; a validar com design partners):

| Campo | Obrigatório | Exemplos |
| --- | --- | --- |
| `sku` / código interno | Sim | `NB-DELL-5490-16-512` |
| `titulo` / descrição curta | Sim | Notebook Dell Latitude 5490 |
| `marca`, `modelo` | Fortemente recomendado | Dell / Latitude 5490 |
| Specs tipadas | Recomendado (MVP notebooks/monitores) | cpu, ram_gb, storage_gb, screen_inch, resolution, os, warranty_months |
| `ncm` | Recomendado | 8471.30.xx |
| `ean` / part number fabricante | Opcional | |
| `preco_ref`, `estoque` | Opcional (fase 2) | |
| `ativo` | Sim | boolean |

Envio: JSON bulk via API, CSV SFTP, ou webhook de sincronização periódica. Volume típico de distribuidor de TI: milhares a dezenas de milhares de SKUs — desenhar upsert incremental.

---

## 5. Meios de obtenção — COMO obter/processar

### 5.1 Preferência legal e técnica

| Método | Recomendação | Comentário |
| --- | --- | --- |
| API oficial PNCP consulta | **Preferencial** | Sem credencial para leitura; estável o suficiente para produto |
| CSV dados abertos | Backfill / reconciliação | Latência diária/anual conforme publicação |
| API Compras.gov dados abertos | Complemento federal | |
| Scraping de portais | **Evitar** como default | ToS, instabilidade, risco jurídico; só se API oficial inexistente e com parecer jurídico |
| Compra de feed de agregador | Opcional | Custo; dependência; pode conflitar com posicionamento |

### 5.2 Padrões de ingestão

1. **Polling** de `contratacoes/publicacao` por janelas curtas (ex.: D-1 → D0) para cada `codigoModalidadeContratacao` relevante (ao menos pregão eletrônico=6, concorrência, dispensa).
2. **Polling** de `contratacoes/proposta` para janela de disputa aberta.
3. **PCA** periódico (semanal) para sinal precoce de demanda de TIC.
4. Para cada `numeroControlePNCP` / (cnpj, ano, sequencial): fetch de **itens** + metadados de **documentos**.
5. **Change detection:** armazenar hash de cabeçalho/itens/`dataAtualizacao`; reprocessar só deltas.
6. **Webhooks LicitaFit → partner:** emitir eventos `opportunity.matched`, `opportunity.updated`, `opportunity.closed` (PNCP não oferece webhook público documentado na pesquisa — o push é responsabilidade do LicitaFit).

### 5.3 Parsing e matching (alto nível)

```
Ingestão PNCP → Normalização (texto, NCM, catálogo)
     → Indexação (BM25 / embeddings + filtros estruturados)
     → Match com catálogo do tenant
     → Score + razões (evidências)
     → Status needs_review | low_confidence | no_match
     → API / Webhooks / UI embutida
```

Heurísticas iniciais (MVP notebooks/monitores):

- Filtro léxico + NCM + palavras de família de produto.
- Extração de atributos (regex/NER leve): polegadas, RAM, SSD, resolução, processador.
- Score composto; **nunca** auto-aprovar participação.
- Humanos no partner/distribuidor fecham a decisão.

### 5.4 Riscos operacionais

| Risco | Mitigação |
| --- | --- |
| Dados incompletos / descrição genérica | Flag `low_confidence`; incentivar revisão de TR/PDF |
| Schema drift (manual 2.x frequente) | Contract tests contra OpenAPI; alertas de campo novo/removido |
| Fragmentação multi-portal | PNCP como verdade de aviso; link origem para disputa |
| Lag de publicação | SLA transparente; complementar com PCA |
| Rate limit / indisponibilidade | Fila, retry, cache, multi-região; CSVs como fallback |
| TLS/rede | Monitorar; no ambiente de pesquisa (25/09/2026) curl TLS ao host falhou pontualmente — validar em infra de produção |

### 5.5 Arquitetura sugerida (LicitaFit)

| Camada | Componentes |
| --- | --- |
| Ingestion | Workers PNCP consulta + CSV reconciler + document fetcher |
| Normalize | Canonical Opportunity / LineItem / Document |
| Catalog | Tenant catalog store (versionado) |
| Match | Feature extraction + scorer + explanation builder |
| Serve | REST API, webhooks assinados, embed SDK, admin |
| Ops | Observabilidade, DLQ, replay, data quality dashboards |
| Compliance | Logs de decisão, disclaimer `needs_review`, retenção LGPD |

---

## 6. Concorrência e adjacentes

### 6.1 Ferramentas brasileiras de alerta / inteligência de licitação

| Empresa / produto | Site | Posicionamento observado | Relação com LicitaFit |
| --- | --- | --- | --- |
| **ConLicitação** | https://conlicitacao.com.br/ | Monitoramento amplo (afirma 6.000+ fontes), boletins, gestão, chat, IA (“Pergunte ao Edital”), robô de lances; planos Super/Premium/Advanced/Black (preços não públicos na página; assinatura 6/12/24 meses, só PJ) | Concorrente de **atenção do usuário final**; não é embed catalog-aware para ERP |
| **Licitei** | https://www.licitei.com.br/ | PNCP + portais, “Pergunte ao Edital”, robô de lances, gestão docs | Idem |
| **Licitar Digital** | https://licitar.digital/ | Plataforma de pregão (órgãos ↔ fornecedores), forte MG/AMM | Infra de disputa; não matching de catálogo de distribuidor |
| **Sollicita (Grupo Negócios Públicos)** | https://sollicita.com.br/ | Conteúdo, banco de editais, planos Pro | Conteúdo + busca; não API embed para ERP de TI |
| **Nextera Licitações** | https://nextera.com.br/solucoes/nextera-licitacoes-winthor/ | Gestão de licitações **integrada ao Winthor** (importar editais, cotações, atas, empenhos) | **Adjacente/complementar** no ERP; foco gestão, não discovery catalog-first |
| **JD System — WSGE Licitações** | https://jdsystem.com.br/modulo-licitacoes/ | Proposta→contrato→empenho→pedido no ERP | Gestão pós-oportunidade |
| **LicitaCloud** | https://licitacloud.com.br/ | Gestão de licitações SaaS | Verificar profundidade de matching em discovery |
| **ATA360** | https://ata360.com.br/ | IA/dados para **entes públicos** (fundamentação) | Outro lado do mercado (governo), não ERP de distribuidor |
| **Licitações by Portal de Compras Públicas (TOTVS)** | https://produtos.totvs.com/... | Sistema para **órgãos** (white-label), integração Protheus | Lado comprador público |

**Nota sobre “Bidu”:** na pesquisa de 25/09/2026 **não foi confirmado** um produto comercial de alertas de licitação amplamente conhecido sob o nome “Bidu”. Tratar menções históricas como não verificadas.

### 6.2 Startups “IA para editais”

Tendência: Q&A sobre PDF, resumo de exigências, geração de declarações. Úteis, mas:

- Otimizam leitura do documento, não **estoque/catálogo do vendedor**.
- Aumentam risco se sugerirem “você está apto” sem disclaimer.

LicitaFit deve **evitar** essa narrativa e, se usar LLM, limitar a extração de atributos / explicação de score.

### 6.3 O que ERPs já oferecem nativamente

- Cadastro de proposta, contrato, empenho, pedido (Nextera, JD System, módulos Winthor).
- Raramente: motor de matching contínuo PNCP × catálogo serializado de TI.
- Integrações pontuais com portais de disputa.

### 6.4 Matriz de diferenciação

| Dimensão | Portais de alerta | IA-edital | Módulo ERP gestão | **LicitaFit** |
| --- | --- | --- | --- | --- |
| Canal de venda | Direct ao fornecedor | Direct | Via ERP | **Via software partner (embed)** |
| Input principal | Keywords / CNAE | PDF edital | Edital já escolhido | **Catálogo do distribuidor** |
| Output | Lista de editais | Resumo/Q&A | Workflow interno | **Itens ranqueados + needs_review** |
| Decisão legal | Às vezes ambígua | Risco alto | N/A | **Explicitamente não legal** |
| Dados | Multi-fonte / scrapers | Docs | Manual/import | **PNCP-first oficial** |

---

## 7. ICP e personas

### 7.1 Comprador primário (economic buyer no go-to-market)

| Atributo | Detalhe |
| --- | --- |
| Cargo | Founder, Head de Produto, Parcerias, CTO de ERP/AFV/software comercial |
| Empresa | Serve **distribuidores/atacadistas** (idealmente TI/eletrônicos) no Brasil |
| Motivação | Diferenciação de roadmap, retenção de clientes B2G, receita de add-on |
| Budget | SaaS B2B R$ 1–5k/mês plausível por módulo parceiro (a validar) |
| Sucesso | Time-to-embed < 30–60 dias; demos com catálogo real; casos de uso notebooks/monitores |

### 7.2 Usuário final (dentro do cliente do partner)

- Coordenador de licitações / vendas governo do distribuidor.
- Analista comercial que monta proposta.
- (Secundário) vendedor AFV que só precisa de “oportunidades quentes”.

### 7.3 Critérios de qualificação (partner)

- Tem base de clientes em distribuição/atacado **com catálogo de produtos**.
- Pelo menos um segmento de TI/eletrônicos **ou** roadmap claro para isso.
- API/extensibilidade (webhooks, app store, ou equipe capaz de integrar).
- Clientes que já participam ou desejam participar de licitações.
- Não exige que LicitaFit emita parecer jurídico.

### 7.4 Desqualificadores

- ERP só serviços/financeiro sem catálogo de SKUs (ex.: Conta Azul clássico).
- Pure marketplace/e-commerce sem operação B2B de distribuição.
- Pedido de “garantir habilitação / ganhar pregão automaticamente”.
- Necessidade exclusiva de robô de lances (outro produto).
- Jurisdição fora do Brasil sem PNCP.

---

## 8. Potenciais clientes (targets nomeados)

> Lista verificável por site público em 25/09/2026. **Não é endosso** nem confirmação de interesse. Prioridade = fit percebido com distribuição TI + capacidade de embed. Onde o fit TI é parcial, prioridade cai.

| # | Empresa | Site | Por que fit | Ângulo de entrada | Prioridade |
| --- | --- | --- | --- | --- | --- |
| 1 | **Onclick** | https://onclick.com.br/ | ERP explícito para **distribuidora de informática/eletrônicos** (série, IMEI, RMA, ST) | “Add-on B2G catalog-match no mesmo stack que já domina serial/ST” | **Alta** |
| 2 | **Soften Sistemas** | https://www.softensistemas.com.br/ | ERP com vertical distribuidora (afirma 1.800+ distribuidoras) | Parceria de módulo / API para clientes com vendas governo | **Alta** |
| 3 | **Softcom Tecnologia** | https://softcomtecnologia.com.br/ | Softcom Atacado; rede de parceiros PME | Embed via canal de parceiros Softcom | **Alta** |
| 4 | **SIAC Sistemas** | https://www.siacsistemas.com.br/informatica | Vertical **Informática** (serial, RMA, garantia) | Pilot com clientes loja/distribuição de informática | **Alta** |
| 5 | **Nextera** | https://nextera.com.br/ | Já vende **Licitações + Winthor** — gap de discovery catalog-aware | Complementar (não substituir) motor de match PNCP | **Alta** |
| 6 | **MáximaTech** | https://maximatech.com.br/ | AFV/logística no atacado; integração Winthor | Oportunidades quentes no maxPedido / stack Winthor | **Alta** |
| 7 | **PowerGO** | https://powergo.com.br/ | AFV offline; integra TOTVS, Sankhya, etc. | Feature “oportunidades governo” no app de pedido | **Alta** |
| 8 | **JD System (WSGE)** | https://jdsystem.com.br/ | Módulo Licitações nativo (proposta→empenho) | Pré-qualificar itens antes da proposta | **Alta** |
| 9 | **TOTVS Winthor (ecossistema)** | https://www.totvs.com/ (linha Winthor) | ERP dominante em atacado/distribuição | Via ISVs (Nextera/Máxima) antes de GTM direto TOTVS | **Alta** |
| 10 | **Sankhya** | https://www.sankhya.com.br/ | ERP forte em atacado | App/integração no marketplace Sankhya | **Média** |
| 11 | **CIGAM** | https://www.cigam.com.br/distribuicao | ERP médio/grande para distribuição | Parceria módulo vertical TI | **Média** |
| 12 | **ATS Informática (Resulth)** | https://www.atsinformatica.com.br/ | ERP atacadista/distribuidor | Verticalizar para clientes de informática | **Média** |
| 13 | **Lexos** | https://www.lexos.com.br/ | Sistema para distribuidora; integrações Winthor no ecossistema | API de oportunidades no ERP Lexos | **Média** |
| 14 | **Target Sistemas** | (buscar target sistemas distribuição) | Foco histórico em distribuição médio/grande | Validar vertical TI antes de outreach | **Média** |
| 15 | **Adiasoft** | https://www.adiasoft.com/br/ | ERP multi-país; base BR | Só se houver clientes BR de TI | **Baixa** |
| 16 | **Softcom Informática (SAS ERP)** | http://softcominformatica.com.br/ | ERP atacado/varejo (entidade distinta da Softcom Tecnologia — validar) | Clarificar empresa e carteira TI | **Média** |
| 17 | **TS Sistemas (SOFTCOM ERP)** | https://tssistemas.com/ | ERP distribuidora com menção a **Licitações** + AFV | Ângulo: alimentar módulo licitações com match | **Alta** |
| 18 | **Micro ERP** | https://microerp.software/ | ERP com página de revenda | Filtrar se há atacado TI | **Baixa** |
| 19 | **Senior Sistemas** | https://www.senior.com.br/ | ERP enterprise | Ciclo longo; só com sponsor | **Baixa** |
| 20 | **Linx** | https://www.linx.com.br/ | Mais varejo | Fraco para atacado TI | **Baixa** |
| 21 | **Omie** | https://www.omie.com.br/ | Cloud PME genérico | Poucos distribuidores TI típicos | **Baixa** |
| 22 | **Portal de Compras Públicas / ISVs TOTVS** | via ficha TOTVS | Integrações lado público | Parceria indireta de dados/fluxo fornecedor | **Média** |
| 23 | **LicitaCloud** | https://licitacloud.com.br/ | SaaS gestão licitações | White-label match engine | **Média** |
| 24 | **Elmar / E-Licitação** | https://elmartecnologia.com.br/ | Software de licitação | Avaliar se atendem fornecedores TI | **Baixa** |
| 25 | **Distribuidores âncora (design partners de catálogo)** | Ingram Micro BR, TD SYNNEX BR, locais Abradisti (ex. Agis citada em notícia Abradisti) | Catálogo real para calibração de match — **não** são buyers do SaaS partner, mas essenciais no piloto | NDA + sync de catálogo notebooks/monitores | **Alta** (piloto dados) |

**Métodos para expandir a lista (se <30 verificáveis de ERP puro):**

1. Buscas: `"ERP" "distribuidora de informática"`, `"módulo licitações" Winthor`, `"força de vendas" atacado`.
2. Membros e expositores Abradisti / Futurecom / feiras de canal.
3. Marketplaces de apps TOTVS, Sankhya, Senior.
4. LinkedIn Sales Nav: título “Parcerias” + keywords ERP distribuição.
5. Perguntar a 5 distribuidores: “qual ERP/AFV vocês usam?” (pesquisa primária — §12).

---

## 9. Canais go-to-market

| Canal | Ação | Prioridade |
| --- | --- | --- |
| **Partner sales outbound** | Lista §8; sequência LinkedIn + e-mail founder/PM | Alta |
| **ISVs do ecossistema Winthor/TOTVS** | Co-selling com quem já tem módulo licitações | Alta |
| **Abradisti** | Associação real e ativa ([abradisti.org.br](https://abradisti.org.br/)); Encontro Anual; estudos setoriais; networking com distribuidores (para design partners de catálogo) e vendors | Alta |
| **Futurecom** | Abradisti renovou apoio institucional Futurecom 2026 (outubro, SP) — canal de presença | Média-Alta |
| **Conteúdo técnico** | “Como matchear catálogo com itens PNCP” (sem scrapers) — SEO para PMs de ERP | Média |
| **Comunidades de canal** | Inforchannel, PartnerSales, TI Inside (mídia que repercute Abradisti) | Média |
| **Marketplace de apps** | Após 2–3 cases | Média |
| **Direct ao distribuidor** | Só se partner-led travar; cuidado para não competir com buyers | Baixa no início |

---

## 10. Riscos regulatórios e de produto

| Risco | Detalhe | Mitigação |
| --- | --- | --- |
| Interpretação como aconselhamento jurídico | Usuário pode achar que “match = pode habilitar” | Disclaimer fixo; status `needs_review`; ToS; UI sem linguagem de elegibilidade |
| Lei 14.133 / responsabilidade em certame | Erro de triagem não deve ser atribuído ao LicitaFit como garantia | Contrato B2B com limitação de responsabilidade; logs |
| **LGPD** | Catálogo pode conter dados comerciais sensíveis; usuários pessoas físicas em contas | Base legal contratual; DPA com partners; minimização; retenção; criptografia; subprocessadores documentados |
| Propriedade do catálogo | Partner/distribuidor dono dos dados | Sem treinar modelos públicos sem opt-in; isolamento multi-tenant |
| Uso de dados públicos PNCP | Dados oficiais reutilizáveis, mas atribuição e atualização importam | Citar PNCP; não republicar como “fonte oficial única” enganosa |
| Preferências / conteúdo nacional | Campos existem; interpretação errada gera risco comercial | Expor campos brutos; não “decidir” margem de preferência |
| Robôs de lance / automação de disputa | Fora do escopo; risco regulatório alto | Explicitamente fora do produto |
| Scraping indevido | Violação de ToS / CFA | Política: só APIs/dados abertos oficiais |

---

## 11. Implicações para produto e preço

### 11.1 Preço público API: usage + floor + monitoramento

| Argumento a favor | Argumento contrário / nuance |
| --- | --- |
| Floor R$ 490/mês acessível para SaaS B2B de módulo | ConLicitação etc. cobram do **fornecedor final** valores provavelmente maiores (opacos; ciclos 6–24 meses) — referência diferente |
| Facilita land em ERP early-stage | Partners com muitos tenants podem gerar overage alto de requests/monitoramento |
| Alinhado a uso real (requests + licitações monitoradas) | Precisa de metering claro e previsibilidade de fatura para o buyer |

**Packaging publicado na landing (API parceiro):**

1. **Requests** — R$ 50 por 1.000 requests.
2. **Floor** — mínimo R$ 490/mês.
3. **Monitoramento** — R$ 1,90 por licitação monitorada / mês.
4. **Dashboard B2B** — assinatura de R$ 399/mês + R$ 5 por licitação monitorada / mês, sem cobrança por request (oferta distinta da API).
5. **Revenue share opcional** — % sobre add-on cobrado do distribuidor (alinha incentivos).
6. **Pilot 60 dias** — fee reduzido ou gratuito contra case study + dados de catálogo.

**Não incluir no preço MVP:** robô de lances, parecer jurídico, monitoramento de chat de pregão.

### 11.2 Implicações de roadmap

1. PNCP items-first matching + API.
2. Embed UI mínima (lista + evidências + needs_review).
3. PCA early signals.
4. Enriquecimento TR/PDF opcional.
5. Famílias de produto além de notebooks/monitores.
6. Disponibilidade/preço do ERP (fase 2).

---

## 12. Plano de próximas pesquisas / experimentos (30–60 dias)

| Semana | Experimento | Sucesso |
| --- | --- | --- |
| 1 | Pipeline: `contratacoes/publicacao` → itens → store; medir volume diário e % itens com descrição útil / NCM / catálogo | Dashboard interno com cobertura |
| 1–2 | Amostrar 200 itens “informática”; rótulo manual match vs. catálogo piloto (1 distribuidor ou catálogo público fabricante) | Precision@K baseline |
| 2–3 | 10 calls discovery (PMs ERP §8 Alta) — script: dor B2G, módulo atual, willingness to pay, requisitos API | ≥3 interessados em pilot |
| 3–4 | Design partner tech: sync catálogo notebooks/monitores; embed em staging | Primeiro `needs_review` real no workflow do partner |
| 4–6 | Pricing test: floor R$490 + usage (requests/monitoramento) vs. flat legado | Sinal qualitativo + 1 LOI/pilot pago |
| Contínuo | Monitorar OpenAPI PNCP / manual 2.x; medir falhas TLS/5xx | SLOs definidos |
| Contínuo | Mapear 10 distribuidores Abradisti e ERPs que usam (pesquisa primária) | Expandir §8 com dados reais |

**Não fazer nestes 60 dias:** scraping agressivo; claims de elegibilidade; GTM massivo a distribuidores contornando partners.

---

## 13. Fontes e bibliografia

Acesso de todas as URLs: **25/09/2026**, salvo indicação.

### Legislação e governo

1. Lei nº 14.133/2021 — https://www.planalto.gov.br/ccivil_03/_ato2019-2022/2021/lei/l14133.htm  
2. Portal de Compras — Nova Lei de Licitações — https://www.gov.br/compras/pt-br/nllc  
3. PNCP (Rede de Parcerias) — https://www.gov.br/rededeparcerias/pt-br/servicos/portal-nacional-de-contratacoes-publicas-pncp  
4. Manual de Integração PNCP v2.6 — https://pncp.gov.br/manual/pt-br/latest/  
5. Acesso ao PNCP (auth, URLs) — https://pncp.gov.br/manual/pt-br/latest/acesso_ao_pncp/index.html  
6. Consultar itens de contratação — https://pncp.gov.br/manual/pt-br/latest/contratacao/consultar_itens_de_uma_contratacao.html  
7. Swagger API PNCP — https://pncp.gov.br/api/pncp/swagger-ui/index.html  
8. Swagger API Consultas — https://pncp.gov.br/api/consulta/swagger-ui/index.html  
9. Dados abertos PNCP — https://www.gov.br/pncp/pt-br/acesso-a-informacao/dados-abertos  
10. Repositório CSV compras/PNCP — https://repositorio.dados.gov.br/seges/comprasgov/anual/  
11. Portal Dados Abertos Compras.gov.br — https://www.gov.br/compras/pt-br/cidadao/portal-de-dados-abertos  
12. Swagger dados abertos compras — https://dadosabertos.compras.gov.br/swagger-ui/index.html  
13. Catálogo Compras.gov.br — https://catalogo.compras.gov.br/  

### Mercado TIC / distribuição

14. Abradisti — Setor movimenta R$ 30,7 bi em 2025 — https://abradisti.org.br/noticias/setor-de-distribuicao-de-tic-movimenta-r-307-bilhoes-e-cresce-7-em-2025-aponta-abradisti/  
15. Inforchannel (eco Abradisti) — https://inforchannel.com.br/2026/05/22/setor-de-distribuicao-de-tic-cresceu-7-em-2025-aponta-estudo-da-abradisti/  
16. Abradisti home — https://abradisti.org.br/  
17. ABINEE — Faturamento 2025 — https://www.abinee.org.br/faturamento-do-setor-em-2025/  

### Concorrentes e adjacentes

18. ConLicitação — https://conlicitacao.com.br/ | Planos — https://conlicitacao.com.br/planos/  
19. Licitei — https://www.licitei.com.br/ | Portais — https://www.licitei.com.br/portais  
20. Licitar Digital — https://licitar.digital/  
21. Sollicita — https://sollicita.com.br/  
22. Negócios Públicos — https://www.negociospublicos.com.br/  
23. Nextera Licitações — https://nextera.com.br/solucoes/nextera-licitacoes-winthor/  
24. JD System Licitações — https://jdsystem.com.br/modulo-licitacoes/  
25. LicitaCloud — https://licitacloud.com.br/  
26. ATA360 (claims de mercado) — https://ata360.com.br/investidores | https://ata360.com.br/imprensa  
27. TOTVS — Licitações by Portal de Compras Públicas — https://produtos.totvs.com/ficha-tecnica/licitacoes-by-portal-de-compras-publicas/  

### ICP / software

28. Onclick — https://onclick.com.br/erp-distribuidora-informatica-eletronicos/  
29. Soften — https://www.softensistemas.com.br/segmentos/distribuidora  
30. Softcom Tecnologia — https://softcomtecnologia.com.br/  
31. SIAC Informática — https://www.siacsistemas.com.br/informatica  
32. MáximaTech — https://maximatech.com.br/  
33. PowerGO — https://powergo.com.br/  
34. Sankhya Atacado — https://www.sankhya.com.br/segmentos-de-atuacao/erp-para-empresas-de-atacado/  
35. CIGAM Distribuição — https://www.cigam.com.br/distribuicao  
36. ATS Informática — https://www.atsinformatica.com.br/  
37. Lexos — https://www.lexos.com.br/  
38. TS Sistemas — https://tssistemas.com/  

### Documentação auxiliar de API (espelho comunitário do manual de consultas)

39. Gist Manual API Consultas PNCP (conteúdo alinhado ao manual oficial de consultas) — https://gist.github.com/Micael106/04a3e5515057ab11ea8797603682f0bd  

### Lacunas explícitas registradas na pesquisa

- Preços públicos de ConLicitação/Licitei/Sollicita: **não divulgados** nas páginas visitadas.  
- Volume oficial PNCP filtrado só para notebooks/monitores 2025: **não extraído** (API TLS instável no ambiente de coleta; pendente medição §12).  
- Produto “Bidu” de alertas: **não verificado**.  
- Total consolidado oficial “R$ X bi em compras públicas 2025” direto de painel MGI: **não baixado** neste ciclo; claims de terceiros sinalizados.

---

*Documento elaborado para uso interno de estratégia LicitaFit / Launchbase Tecnologia Ltda. Não constitui aconselhamento jurídico.*
