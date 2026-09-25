# LicitaFit

Landing page do LicitaFit — API da Launchbase Tecnologia Ltda que qualifica licitações públicas com o catálogo do distribuidor de TI.

## Conteúdo

- `index.html` — página principal
- `guias/` — índice de guias AEO
- `alerta-edital-vs-matching-catalogo/` — guia #1: alerta genérico vs matching de catálogo
- `needs-review-matched-conflito-unknown/` — guia #2: matched, conflito, unknown e `needs_review`
- `js/site-origin.js` — **SITE_ORIGIN** (um lugar para trocar o host canônico)
- `sitemap.xml` / `robots.txt` — descoberta
- `css/vanilla.css` — estilos
- `images/` — imagens da landing

## SITE_ORIGIN (canonical)

| | URL |
|-|-----|
| **Intended canonical** | `https://www.licitafit.com.br` |
| **Preview (verificação até DNS)** | `https://dapper-opera-mz8m.here.now` |

DNS/hosting do domínio canônico ainda **TBD**. Canonical tags, JSON-LD, `sitemap.xml` e `robots.txt` já usam `https://www.licitafit.com.br`.

### Swap path (um lugar)

1. Edite a constante em [`js/site-origin.js`](js/site-origin.js) (`SITE_ORIGIN=...` no comentário e no código).
2. Busque/substitua a mesma string em: `sitemap.xml`, `robots.txt`, e em cada HTML (`<link rel="canonical">` + JSON-LD).

## Preview local

Abra `index.html` no navegador ou sirva a pasta com qualquer servidor estático.

## Site publicado (preview)

https://dapper-opera-mz8m.here.now/

- Guias: https://dapper-opera-mz8m.here.now/guias/
- Guia #1: https://dapper-opera-mz8m.here.now/alerta-edital-vs-matching-catalogo/
- Guia #2: https://dapper-opera-mz8m.here.now/needs-review-matched-conflito-unknown/

## Documentação

- [Dossiê de mercado](docs/dossie-mercado-licitafit.md) (também em [HTML](docs/dossie-mercado-licitafit.html))
