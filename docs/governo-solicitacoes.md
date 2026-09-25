# Solicitações e confirmações junto ao governo / PNCP

**Uso:** documentação interna de operações (Launchbase / LicitaFit).  
**Não é** material de marketing nem parecer jurídico.  
**Atualizado:** 2026-09-25 (America/Sao_Paulo).

Objetivo: checklist do que confirmar ou solicitar aos canais oficiais antes e durante o uso em produção de **dados públicos** do PNCP / dados abertos, e o que **não** misturar com o produto comercial de matching.

---

## 1. Papéis distintos (não misturar)

| Papel | Quem | O que fazer |
|-------|------|-------------|
| Órgão / plataforma que **alimenta** o PNCP | Entes e portais credenciados | Credenciamento MGI, APIs de manutenção, JWT, treina → produção |
| Consumidor de **consulta / dados abertos** | Qualquer interessado (inclui produtos comerciais) | Usar endpoints/docs públicos; respeitar termos e limites |
| Produto **LicitaFit** | Launchbase | Matching catálogo ↔ itens publicados; API/Dashboard comerciais |

LicitaFit **não** publica atos no PNCP e **não** substitui o Manual oficial de integração destinado a quem alimenta o portal.

---

## 2. Fontes oficiais (verificar sempre no hub)

| Recurso | URL | Notas |
|---------|-----|-------|
| Hub PNCP (gov.br) | https://www.gov.br/pncp/pt-br | Ponto de partida institucional |
| Portal PNCP | https://pncp.gov.br/ | Consulta / divulgação |
| Editais | https://pncp.gov.br/app/editais | UI pública |
| Lei 14.133/2021 | https://www.planalto.gov.br/ccivil_03/_ato2019-2022/2021/lei/l14133.htm | Texto Planalto |
| Manual de Integração | https://pncp.gov.br/manual/pt-br/latest/ | v2.6 citada em 2026; revalidar versão |
| Dados abertos (página) | https://www.gov.br/pncp/pt-br/acesso-a-informacao/dados-abertos | Consultas sem login (conforme a página) |
| FAQ PNCP | https://www.gov.br/pncp/pt-br/pncp/perguntas-e-respostas | Inclui credenciais produção |
| Portal de Serviços MGI | https://portaldeservicos.gestao.gov.br | Chamados / suporte citados pelo Manual |
| Telefone Central | 0800 978 9001 | Citado no Manual/FAQ; pode haver indisponibilidade (comunicados 2026) |
| Nova Lei (Compras) | https://www.gov.br/compras/pt-br/nllc | Material institucional complementar |

**Desconhecido / a revalidar operacionalmente**

- Conectividade TLS do ambiente de produção Launchbase → `pncp.gov.br` (já houve EOF SSL em testes de box em 2026-09-25; ver `docs/research-notes/fontes-chave.md` no repo).
- Rate limits numéricos vigentes da API de **consulta** (não inventar; extrair do Manual/Swagger vigentes).
- Termos de atribuição / licença de uso comercial de dumps CSV em repositórios de dados abertos (URLs de repositório podem mudar).
- Se existir canal de e-mail dedicado além do Portal de Serviços: **não confirmado** nesta data; usar Portal + 0800 conforme FAQ.

Swagger / bases citados em notas internas (revalidar):

- Produção API PNCP: `https://pncp.gov.br/api/pncp`
- Consulta: `https://pncp.gov.br/api/consulta` (Swagger UI referido em notas: `.../api/consulta/swagger-ui/index.html`)
- Treinamento: `https://treina.pncp.gov.br` (+ swagger correspondente no Manual)

---

## 3. O que pedir / confirmar (checklist)

### 3.1 Uso de dados públicos em produto comercial

- [ ] Confirmar na página de Dados Abertos / Manual quais operações são **públicas sem cadastro**.
- [ ] Registrar a data e a URL da política/termos consultados (print ou PDF arquivado).
- [ ] Confirmar se há exigência de **atribuição** ao citar dados do PNCP em UI ou docs.
- [ ] Confirmar se há restrições a redistribuição, cache prolongado ou uso comercial além da consulta.
- [ ] **Desconhecido até confirmar:** SLA de disponibilidade da API de consulta; políticas de bloqueio por IP.

### 3.2 Rate limits e boa cidadania

- [ ] Extrair do Manual/Swagger limites de taxa, paginação e campos de atualização (`/atualizacao` etc., se aplicável à consulta usada).
- [ ] Definir backoff, cache e monitoramento internos compatíveis (sem assumir números inventados).
- [ ] Abrir chamado no Portal de Serviços **somente** se o Manual indicar esse canal para consumidores (hoje o Manual enfatiza suporte a **integração de sistemas** que publicam; para consulta pública, o escopo do suporte pode ser limitado; **marcar como incerto**).

### 3.3 Credenciais (só se o caso de uso exigir)

Aplica-se se Launchbase/LicitaFit um dia precisar de API de **manutenção** ou de ambiente autenticado. **Hoje o matching comercial tipicamente não precisa publicar no PNCP.**

- [ ] Cadastro no Portal de Serviços MGI.
- [ ] Credenciamento no ambiente de **treinamento** (treina.pncp.gov.br), conforme FAQ/Manual.
- [ ] Testes documentados (links de evidência).
- [ ] Solicitação de produção com: razão social, CNPJ, ID do sistema no treina (conforme FAQ “credenciais de produção”).
- [ ] Guarda segura de login/senha/JWT; rotação; sem commit em repo.

### 3.4 Contatos oficiais (públicos)

| Canal | Uso |
|-------|-----|
| https://portaldeservicos.gestao.gov.br | Chamados / cadastro (citado Manual § Suporte e FAQ) |
| 0800 978 9001 | Telefone Central MGI (verificar comunicados de indisponibilidade) |
| https://www.gov.br/pncp/pt-br | Informações institucionais / comunicados |

**Não inventar** e-mails ou WhatsApps “oficiais” sem página gov.br.

### 3.5 Compliance de produto (interno, não pedido ao governo)

- [ ] Copy e UI: matching ≠ habilitação ≠ julgamento.
- [ ] Landing aponta fontes oficiais (`/fontes-oficiais-pncp/`, `/uso-responsavel-matching/`).
- [ ] Isolamento de catálogo entre clientes/parceiros.
- [ ] Log de origem do dado (identificador PNCP / versão) para auditoria comercial.

---

## 4. O que **não** solicitar ao governo (evitar confusão)

- Homologação ou “selo LicitaFit aprovado pelo PNCP” (não existe esse framing).
- Que o PNCP “integre” matching de catálogo privado como feature oficial.
- Interpretação jurídica vinculante via Central de Atendimento (canal técnico/operacional).

---

## 5. Produção: checklist mínimo Launchbase

1. Revalidar URLs e versão do Manual na semana do go-live.
2. Smoke test consulta pública (editais/itens) a partir da rede de produção.
3. Documentar rate limit observado + política de retry.
4. Arquivar termos/dados abertos consultados (data + URL).
5. Runbook: PNCP fora do ar → mensagem ao cliente sem overclaim; fila de retry.
6. Revisão jurídica externa **se** o contrato com cliente exigir (fora do escopo deste README).

---

## 6. Histórico de dúvidas em aberto

| Item | Status |
|------|--------|
| Rate limit oficial numérico da API consulta | Desconhecido (ler Manual/Swagger vigente) |
| Licença explícita de redistribuição comercial de dumps | Desconhecido |
| E-mail dedicado além do Portal | Não encontrado em fontes públicas usadas em 2026-09-25 |
| Necessidade futura de credencial de manutenção | Não aplicável ao matching atual; reavaliar se o produto mudar |

