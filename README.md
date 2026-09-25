# LicitaFit

Landing page do LicitaFit — API da Launchbase Tecnologia Ltda que qualifica licitações públicas com o catálogo do distribuidor de TI.

## Conteúdo

- `index.html` — página principal (inclui seção mid-page `#recursos`)
- `guias/` — índice de guias AEO
- `comparativos/` — hub de comparativos (sem ranking)
- Artigos em pastas na raiz (`alerta-edital-vs-matching-catalogo/`, etc.)
- `js/site-origin.js` — **SITE_ORIGIN** (um lugar para trocar o host canônico)
- `scripts/sync-chrome.py` — sincroniza nav/footer/breadcrumbs/Continue lendo
- `docs/chrome.md` — padrão de IA (nav/footer estilo Canonical)
- `sitemap.xml` / `robots.txt` — descoberta
- `css/vanilla.css` — estilos
- `images/` — imagens da landing

## SITE_ORIGIN (canonical)

| | URL |
|-|-----|
| **Intended canonical** | `https://www.licitafit.com.br` |
| **Visibilidade interim (GitHub Pages)** | `https://raphaeljlps.github.io/licitafit/` |
| **Preview antigo (STALE — não redeploya)** | `https://dapper-opera-mz8m.here.now` |

DNS/hosting do domínio canônico ainda **TBD**. Canonical tags, JSON-LD, `sitemap.xml` e `robots.txt` usam `https://www.licitafit.com.br` — **não** troque pelo URL do Pages.

### Importante: here.now está desatualizado

O preview `https://dapper-opera-mz8m.here.now/` **não faz auto-deploy** a partir de `main`. Ele ainda mostra a landing antiga (sem Guias/FAQ/footer de recursos). Use **GitHub Pages** (abaixo) para ver a versão atual.

### Swap path (um lugar)

1. Edite a constante em [`js/site-origin.js`](js/site-origin.js) (`SITE_ORIGIN=...` no comentário e no código).
2. Busque/substitua a mesma string em: `sitemap.xml`, `robots.txt`, e em cada HTML (`<link rel="canonical">` + JSON-LD).

## Deploy / visibilidade

### GitHub Pages (recomendado enquanto DNS não está no ar)

> **Nota:** GitHub Pages em plano free exige repositório **público**. Se o repo voltar a privado, Pages deixa de servir; use Netlify (`netlify.toml`) ou Cloudflare Pages como alternativa. O canônico SEO continua `www.licitafit.com.br`.


Publicação estática a partir de `main` (root), com `.nojekyll`.

- Site: **https://raphaeljlps.github.io/licitafit/**
- Guias: https://raphaeljlps.github.io/licitafit/guias/
- Comparativos: https://raphaeljlps.github.io/licitafit/comparativos/

Reativar/ajustar (admin do repo):

```bash
gh api --method POST /repos/raphaeljlps/licitafit/pages \
  -f build_type=legacy \
  -f source[branch]=main \
  -f source[path]=/
```

Homepage do repositório aponta para o URL do Pages (interim). O canônico de SEO continua `www.licitafit.com.br`.

### Preview local

```bash
python3 -m http.server 8080
# abra http://127.0.0.1:8080/
```

## Informação (IA)

Ver [docs/chrome.md](docs/chrome.md). Resumo:

- Top nav enxuto com entrada única **Recursos**
- Home `#recursos` com hubs + guias em destaque
- Footer em colunas Produto / Recursos / Empresa (não lista todos os artigos)
- Artigos com breadcrumb e **Continue lendo**

## Documentação

- [Dossiê de mercado](docs/dossie-mercado-licitafit.md) (também em [HTML](docs/dossie-mercado-licitafit.html))
- [Chrome / IA](docs/chrome.md)
