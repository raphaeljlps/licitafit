# Fluxo pós-demo (interno)

Runbook operacional depois que alguém envia o formulário de demonstração do CruzaEdital.
Não é conteúdo público da landing.

## Quem responde

| Papel | Responsável (hoje) | Canal |
|-------|--------------------|-------|
| Primeira resposta | Raphael (Launchbase) | Caixa **raphael@launchbase.dev** (FormSubmit) |
| Backup | (definir) | Mesmo e-mail / encaminhar |

Assunto típico do FormSubmit: `CruzaEdital: pedido de demonstracao...` (home, API ou Dashboard).

## SLA sugerido (meta interna)

| Etapa | Meta |
|-------|------|
| Confirmar recebimento / agendar | até **1 dia útil** |
| Call de demo (se houver fit) | até **5 dias úteis** após o aceite de horário |
| Follow-up se sem resposta do lead | **3 dias úteis** após o primeiro e-mail |

Se a caixa estiver cheia ou você estiver offline, anote no calendário e avise o backup. Não prometa SLA no site público sem alinhar capacidade.

## Antes da call (checklist rápido)

1. Ler o formulário: nome, empresa, interesse (API / Dashboard / ainda não sei), mensagem.
2. Abrir a LP certa: [`/para-parceiros/`](../para-parceiros/) ou [`/para-empresas/`](../para-empresas/).
3. Confirmar se FormSubmit já foi ativado neste domínio (ver [analytics-e-formulario.md](analytics-e-formulario.md)).
4. Não afirmar membership em associações (ATCG etc.) nem selos inventados.
5. Repetir o disclaimer: apoio à decisão comercial; não parecer jurídico; não garantia de habilitação.

## O que mostrar na call

### Se o interesse for **API** (parceiro de software / ERP / AFV)

- Página [`/para-parceiros/`](../para-parceiros/) e [`/integracao-api-licitafit/`](../integracao-api-licitafit/).
- Fluxo: catálogo do cliente do parceiro → matching com itens de edital (PNCP) → status (`matched`, `conflito`, `unknown`) + `needs_review`.
- Cobrança pública de referência: requests + monitoramento (valores na LP; confirmar se ainda vigentes).
- O que **não** mostrar como “pronto”: habilitação automática, parecer jurídico, UI com selo “habilitado”.
- Próximo passo típico: sandbox / escopo de integração / quem é o product lead técnico.

### Se o interesse for **Dashboard** (equipe de licitação / distribuidor)

- Página [`/para-empresas/`](../para-empresas/) e [`/como-usar-dashboard-matching-licitacoes/`](../como-usar-dashboard-matching-licitacoes/).
- Fluxo: upload/manutenção de catálogo → monitorar editais → fila de revisão com status.
- Cobrança pública de referência: assinatura + por licitação monitorada/mês (R$ 399/mês + R$ 5 por licitação monitorada / mês).
- O que **não** mostrar como “pronto”: garantia de ganhar pregão, cobertura 100% de todos os órgãos, parecer jurídico.
- Próximo passo típico: trial / amostra de catálogo / definição de volume de licitações monitoradas.

### Se o interesse for **ainda não sei**

- Começar pela home ([chooser](../index.html)): dois caminhos claros.
- Em 5 minutos: “você embute no software de terceiros (API) ou a equipe usa direto (Dashboard)?”.
- Seguir o roteiro API ou Dashboard conforme a resposta.

## Depois da call

- Registrar: fit (sim/não/talvez), próximo passo, data.
- Enviar e-mail curto com links das páginas vistas (Pages interim ou `www.licitafit.com.br` quando DNS estiver no ar).
- Se pedirem proposta: alinhar escopo antes de inventar preço fora da tabela pública.

## Ativação FormSubmit (se o lead disser que o form “não chegou”)

1. Verificar spam em `raphael@launchbase.dev`.
2. Se for a primeira vez no domínio público: abrir o e-mail **Activate Form** do FormSubmit.
3. Detalhes: [analytics-e-formulario.md](analytics-e-formulario.md).

## Espelho no workspace

Cópia de trabalho: `/workspace/licitafit/docs/fluxo-pos-demo.md` (manter alinhada a este arquivo no repo).
