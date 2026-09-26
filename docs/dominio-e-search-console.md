# Domínio e Google Search Console (quando o DNS estiver pronto)

Notas de preparação. **Não afirma** que `www.licitafit.com.br` já resolve ou que o Search Console já está verificado.

Canonical SEO do site: `https://www.licitafit.com.br` (ver `js/site-origin.js`).
Visibilidade interim enquanto DNS não aponta: `https://raphaeljlps.github.io/licitafit/` (GitHub Pages a partir de `main`).

## Ordem sugerida

1. **DNS** do domínio (e `www`) apontando para o host escolhido (GitHub Pages custom domain, Netlify, Cloudflare Pages, etc.).
2. Confirmar HTTPS e que a home carrega no canônico.
3. Manter `SITE_ORIGIN`, `sitemap.xml`, `robots.txt` e tags `canonical` / JSON-LD alinhados a `https://www.licitafit.com.br` (já é o valor atual; só mude se o canônico mudar de verdade).
4. **Google Search Console (GSC):** criar propriedade no domínio ou no prefixo URL.
5. **Verificar** propriedade (DNS TXT, arquivo HTML, ou meta tag; escolha um método e documente aqui depois).
6. **Enviar sitemap:** `https://www.licitafit.com.br/sitemap.xml` (já referenciado em `robots.txt`).
7. Pedir indexação da home e das LPs principais (`/para-parceiros/`, `/para-empresas/`, `/guias/`, `/privacidade/`) se quiser acelerar (opcional).

## GitHub Pages + domínio customizado (resumo)

Se continuar no Pages:

1. Em Settings → Pages, adicionar custom domain `www.licitafit.com.br` (e apex se desejar).
2. Criar os registros DNS que o GitHub indicar (em geral CNAME para `www` → `raphaeljlps.github.io`, e registros A/AAAA ou ALIAS no apex conforme a doc vigente do GitHub).
3. Esperar propagação; habilitar “Enforce HTTPS” quando disponível.
4. Só então verificar no GSC o **canônico**, não só o `github.io`.

Consulte a documentação oficial do GitHub Pages (custom domain) no dia da configuração; os IPs/registros podem mudar.

## Sitemap e robots (já no repo)

- `sitemap.xml`: lista de URLs sob `https://www.licitafit.com.br/...`
- `robots.txt`: `Sitemap: https://www.licitafit.com.br/sitemap.xml`

Enquanto o DNS não resolver, o Google pode não conseguir buscar essas URLs pelo host canônico. O Pages interim continua útil para demos humanas; SEO canônico espera o DNS.

## Checklist (Raphael)

- [ ] DNS apex + www apontando e HTTPS ok
- [ ] Propriedade criada no Search Console
- [ ] Verificação concluída
- [ ] Sitemap enviado e sem erro bloqueante
- [ ] (Opcional) Analytics ligado em `js/site-config.js` e privacidade revisada

## Relacionado

- [analytics-e-formulario.md](analytics-e-formulario.md) (FormSubmit + analytics opcional)
- [README](../README.md) (SITE_ORIGIN e deploy)
