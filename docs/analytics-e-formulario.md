# Analytics e formulário de demonstração

Configuração em um lugar: [`js/site-config.js`](../js/site-config.js).

## Formulário (FormSubmit → e-mail)

Pedidos de demonstração nas páginas **home**, **para-parceiros** e **para-empresas** enviam para:

**raphael@launchbase.dev**

via [FormSubmit](https://formsubmit.co/) (`action="https://formsubmit.co/raphael@launchbase.dev"`).

Não precisa de API key nem backend. Campos ocultos: `_subject`, `_next` (página [`/obrigado/`](../obrigado/)), honeypot `_honey`, `origem_pagina`.

### Ativação (obrigatório na primeira vez)

1. Publique o site (GitHub Pages a partir de `main`).
2. Envie **um** pedido de teste pelo formulário na URL pública (não use só `localhost`; o FormSubmit associa o domínio).
3. Abra a caixa de **raphael@launchbase.dev** e clique no link **Activate Form** / confirmar do FormSubmit.
4. A partir daí, novos envios chegam como e-mail normal (assunto `LicitaFit: pedido de demonstracao...`).

Se o envio falhar, o formulário mostra o fallback `mailto:raphael@launchbase.dev`.

### Trocar o e-mail de destino

Edite `LF_FORM.email` e `LF_FORM.endpoint` em `js/site-config.js`, e o `action=` padrão nos três formulários HTML (ou deixe o `js/demo-form.js` sobrescrever o `action` em runtime).

### Alias FormSubmit (opcional)

Depois de ativar, o FormSubmit pode fornecer um hash aleatório no lugar do e-mail na URL (`https://formsubmit.co/xxxxx`). Isso evita expor o endereço no HTML. Se usar o hash, atualize `LF_FORM.endpoint` e os `action=` dos forms.

## Analytics (desligado por padrão)

Arquivos:

- `js/site-config.js` → `window.LF_ANALYTICS = { provider, id }`
- `js/analytics.js` → carrega o script **somente** se `provider` não for `none` e `id` estiver preenchido
- Inclusão em todas as páginas via `scripts/sync-chrome.py` (junto com `site-origin.js`)

### Ativar Google Analytics 4

1. Crie uma propriedade GA4 e copie o Measurement ID (`G-XXXXXXXX`).
2. Em `js/site-config.js`:

```js
global.LF_ANALYTICS = {
  provider: 'ga4',
  id: 'G-XXXXXXXX'  // cole o ID real
};
```

3. Commit e push para `main` (Pages atualiza em alguns minutos).

### Ativar Plausible

1. Crie o site em [plausible.io](https://plausible.io) (ou instância self-hosted) com o domínio canônico, ex.: `licitafit.com.br` (e/ou o host do Pages se for a URL pública atual).
2. Em `js/site-config.js`:

```js
global.LF_ANALYTICS = {
  provider: 'plausible',
  id: 'licitafit.com.br'  // data-domain
};
```

Para Plausible self-hosted, edite a URL do script em `js/analytics.js`.

### Deixar desligado

Mantenha `provider: 'none'` e `id: ''`. Nenhum beacon é enviado.

## Sync chrome

```bash
python3 scripts/sync-chrome.py
```

Reaplica nav/footer e garante os scripts `site-config` + `site-origin` + `analytics` (+ `demo-form` na home e nas LPs).
