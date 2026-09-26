# LicitaFit

Landing page do LicitaFit (API da Launchbase Tecnologia Ltda que qualifica licitações públicas com o catálogo do distribuidor de TI).

## Conteúdo

- `index.html` , home chooser (dois caminhos + `#recursos`)
- `para-parceiros/` , LP API B2B2B (parceiros de software)
- `para-empresas/` , LP Dashboard B2B (equipes de licitação; R$ 399/mês + R$ 5 por licitação monitorada/mês)
- `guias/` , índice de guias AEO
- `comparativos/` , hub de comparativos (sem ranking)
- Artigos em pastas na raiz (`alerta-edital-vs-matching-catalogo/`, etc.)
- `js/site-origin.js` , **SITE_ORIGIN** (um lugar para trocar o host canônico)
- `js/site-config.js` , analytics + e-mail do formulário de demo
- `js/analytics.js` , carrega GA4/Plausible só se configurado
- `js/demo-form.js` , FormSubmit (destino `raphael@launchbase.dev`)
- `obrigado/` , página de sucesso do formulário
- `privacidade/` , privacidade e cookies (LGPD, formulário de direitos)
- `scripts/sync-chrome.py` , sincroniza nav/footer/breadcrumbs/Continue lendo
- `docs/chrome.md` , padrão de IA (nav/footer estilo Canonical)
- `sitemap.xml` / `robots.txt` , descoberta
- `css/vanilla.css` , estilos
- `images/` , imagens da landing

## SITE_ORIGIN (canonical)

| | URL |
|-|-----|
| **Intended canonical** | `https://www.licitafit.com.br` |
| **Visibilidade interim (GitHub Pages)** | `https://raphaeljlps.github.io/licitafit/` |
| **Legacy preview (STALE)** | `https://dapper-opera-mz8m.here.now` (não usar para demos) |

DNS/hosting do domínio canônico ainda **TBD**. Canonical tags, JSON-LD, `sitemap.xml` e `robots.txt` usam `https://www.licitafit.com.br` (**não** troque pelo URL do Pages).

Para ver a versão atual, use **GitHub Pages** (abaixo). O preview here.now **não** faz auto-deploy a partir de `main` e está desatualizado.

### Swap path (um lugar)

1. Edite a constante em [`js/site-origin.js`](js/site-origin.js) (`SITE_ORIGIN=...` no comentário e no código).
2. Busque/substitua a mesma string em: `sitemap.xml`, `robots.txt`, e em cada HTML (`<link rel="canonical">` + JSON-LD).

## Deploy / visibilidade

### GitHub Pages (recomendado enquanto DNS não está no ar)

> **Nota:** GitHub Pages em plano free exige repositório **público**. Se o repo voltar a privado, Pages deixa de servir; use Netlify (`netlify.toml`) ou Cloudflare Pages como alternativa. O canônico SEO continua `www.licitafit.com.br`.


Publicação estática a partir de `main` (root), com `.nojekyll`.

- Site: **https://raphaeljlps.github.io/licitafit/**
- Para parceiros: https://raphaeljlps.github.io/licitafit/para-parceiros/
- Para empresas: https://raphaeljlps.github.io/licitafit/para-empresas/
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

- Top nav: Produto · Para parceiros · Para empresas · Recursos · Empresa
- Home chooser com dois caminhos; `#recursos` com hubs + guias em destaque
- Footer Produto aponta para ambas as LPs (não lista todos os artigos)
- Artigos com breadcrumb e **Continue lendo**

## Formulário e analytics

- **Demo:** formulários na home e em `/para-parceiros/`, `/para-empresas/` enviam para **raphael@launchbase.dev** via FormSubmit (sem API key). Na primeira submissão ao site público, confirme o e-mail do FormSubmit. Ver também [`/privacidade/`](privacidade/).
- **Analytics:** desligado por padrão. Em `js/site-config.js`, defina `LF_ANALYTICS.provider` (`ga4` ou `plausible`) e `id`. Detalhes: [docs/analytics-e-formulario.md](docs/analytics-e-formulario.md).

## Documentação

- [Dossiê de mercado](docs/dossie-mercado-licitafit.md) (também em [HTML](docs/dossie-mercado-licitafit.html))
- [Chrome / IA](docs/chrome.md)
- [Analytics e formulário](docs/analytics-e-formulario.md)
- [Domínio e Search Console](docs/dominio-e-search-console.md)
- [Fluxo pós-demo (interno)](docs/fluxo-pos-demo.md)
- [Rascunho contato ATCG (não enviar)](docs/rascunho-contato-atcg.md)
