# Chrome compartilhado (nav + footer + Recursos)

Padrão visual alinhado ao Canonical/Ubuntu (Vanilla): colunas **Produto · Recursos · Empresa**, não um dump de 15 links.

## Top nav (enxuto)

Produto · **Para parceiros** · **Para empresas** · **Recursos** · Empresa · CTA demo

- Home: `Recursos` → `#recursos`
- Subpáginas: `Recursos` → `../index.html#recursos` (marcado `is-selected` em guias/artigos)
- LPs de produto: `Para parceiros` / `Para empresas` marcados `is-selected` em `/para-parceiros/` e `/para-empresas/`

## Home como chooser

Após o hero, dois caminhos claros:

1. `/para-parceiros/` — API B2B2B (ICP, endpoints, preço por uso)
2. `/para-empresas/` — Dashboard B2B (em preparação; preço sob consulta)

Home mantém value prop compartilhada + resumos finos de “para quem” e preço com link para as LPs. Detalhe profundo fica fora da home.

## Home `#recursos`

1. Cards de hubs: `/guias/`, `/comparativos/`, `/integracao-api-licitafit/`
2. 6 guias em destaque com blurb curto
3. CTA “Ver todos os guias”

## Footer (4 colunas + faixa legal)

| Coluna | Links |
|--------|-------|
| (marca) | Tagline LicitaFit |
| **Produto** | Visão geral, API para parceiros, Dashboard para empresas, Demonstração |
| **Recursos** | Guias, Comparativos, FAQ, Integração API — **não** cada artigo |
| **Empresa** | Launchbase, disclaimer, CNPJ |
| Faixa | © + atalhos Recursos/Guias/Comparativos |

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
