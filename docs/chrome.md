# Chrome compartilhado (nav + footer + Recursos)

Padrão visual alinhado ao Canonical/Ubuntu (Vanilla): colunas **Produto · Recursos · Empresa**, não um dump de 15 links.

## Top nav (enxuto)

Produto · **Para parceiros** · **Para empresas** · **Recursos** · Empresa · CTA demo

- Home: `Recursos` → `#recursos`
- Subpáginas: `Recursos` → `../index.html#recursos` (marcado `is-selected` em guias/artigos)
- LPs de produto: `Para parceiros` / `Para empresas` marcados `is-selected` em `/para-parceiros/` e `/para-empresas/`

## Home como chooser

Após o hero, dois caminhos claros:

1. `/para-parceiros/` - API para parceiros (ICP, endpoints, preço por uso)
2. `/para-empresas/` - Dashboard para equipes (assinatura R$ 399/mês + R$ 5 por licitação monitorada/mês)

Home mantém value prop compartilhada + resumos finos de “para quem” e preço com link para as LPs. Detalhe profundo fica fora da home.

## Home `#recursos`

1. Cards de hubs: `/guias/`, `/comparativos/`, `/integracao-api-licitafit/`
2. 6 guias em destaque com blurb curto
3. CTA “Ver todos os guias”

## Footer (4 colunas + faixa legal)

| Coluna | Links |
|--------|-------|
| (marca) | Tagline CruzaEdital |
| **Produto** | Visão geral, API para parceiros, Dashboard para empresas, Demonstração |
| **Recursos** | Guias, Comparativos, FAQ, Integração API (**não** cada artigo) |
| **Empresa** | Launchbase, Privacidade e cookies, disclaimer, CNPJ |
| Faixa | © + atalhos Recursos/Guias/Comparativos/Privacidade |

## Artigos (guia/comparativo)

- Mesmo header/footer
- Breadcrumb: `Início / Recursos / Guias|Comparativos / Esta página`
- Bloco **Continue lendo** (3 links) antes do `</main>`

## LPs de produto

- Breadcrumb: `Início / Para parceiros (API)` ou `Início / Para empresas (Dashboard)`
- Canonical + JSON-LD com `SITE_ORIGIN`

## DRY

HTML estático com snippets sincronizados. Para reaplicar:

```bash
python3 scripts/sync-chrome.py
```

Edite metadados/`FEATURED`/`RELATED` em `scripts/sync-chrome.py` e rode de novo.


## Hub Guias (duas seções ICP)

1. `#parceiros` , Para parceiros de software (embutir matching, cobrança API, checklist ERP, feature UI, integração)
2. `#empresas` , Para equipes de licitação (usar Dashboard, upload/monitorar, go/no-go, checklist vertical, matching)
3. `#todos` , índice completo compartilhado


## Fontes / confiança (2026-09-25)

- Páginas: `/fontes-oficiais-pncp/`, `/como-funcionam-licitacoes-publicas/`, `/lei-14133-contexto-operadores/`, `/integracao-pncp-sistemas-licitacao/`, `/uso-responsavel-matching/`
- Hub Guias: seção `#confianca`
- LPs `/para-parceiros/` e `/para-empresas/`: faixa `#fontes-confianca` (links oficiais + fontes page)
- Ops interno: `docs/governo-solicitacoes.md` (espelho em workspace `/workspace/licitafit/docs/GOVERNO-SOLICITACOES.md`)


## Scripts compartilhados (head)

`scripts/sync-chrome.py` injeta:

1. `js/site-config.js` (analytics + formulário)
2. `js/site-origin.js` (SITE_ORIGIN)
3. `js/analytics.js` (no-op até configurar)
4. `js/demo-form.js` (só home + LPs com formulário)

Ver [analytics-e-formulario.md](analytics-e-formulario.md).

## Privacidade

- Página pública: `/privacidade/` (privacidade + cookies + direitos LGPD + formulário FormSubmit)
- Links no footer (coluna Empresa + faixa legal) via `scripts/sync-chrome.py`
- Formulários de demo linkam para Privacidade junto do hint de e-mail
