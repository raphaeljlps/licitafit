# Chrome compartilhado (nav + footer + Recursos)

Padrão visual alinhado ao Canonical/Ubuntu (Vanilla): colunas **Produto · Recursos · Empresa**, não um dump de 15 links.

## Top nav (enxuto)

Produto · Como funciona · Para quem · **Recursos** · Preço · Empresa · CTA demo

- Home: `Recursos` → `#recursos`
- Subpáginas: `Recursos` → `../index.html#recursos` (marcado `is-selected` em guias/artigos)

## Home `#recursos`

1. Cards de hubs: `/guias/`, `/comparativos/`, `/integracao-api-licitafit/`
2. 6 guias em destaque com blurb curto
3. CTA “Ver todos os guias”

## Footer (4 colunas + faixa legal)

| Coluna | Links |
|--------|-------|
| (marca) | Tagline LicitaFit |
| **Produto** | #produto, #como-funciona, #preco, #demonstracao |
| **Recursos** | Guias, Comparativos, FAQ, Integração API — **não** cada artigo |
| **Empresa** | Launchbase, disclaimer, CNPJ |
| Faixa | © + atalhos Recursos/Guias/Comparativos |

## Artigos (guia/comparativo)

- Mesmo header/footer
- Breadcrumb: `Início / Recursos / Guias|Comparativos / Esta página`
- Bloco **Continue lendo** (3 links) antes do `</main>`

## DRY

HTML estático com snippets sincronizados. Para reaplicar:

```bash
python3 scripts/sync-chrome.py
```

Edite metadados/`FEATURED`/`RELATED` em `scripts/sync-chrome.py` e rode de novo.
