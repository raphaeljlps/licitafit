#!/usr/bin/env python3
"""Sync shared nav/footer/breadcrumbs/Continue-lendo across LicitaFit static HTML.

Idempotent: re-run after editing PAGES / FEATURED below.
See docs/chrome.md.
"""
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

PAGES = {
    "alerta-edital-vs-matching-catalogo": {
        "title": "Alerta de edital vs matching de catálogo",
        "short": "Alerta vs matching",
        "hub": "guias",
        "blurb": "Aviso por palavra-chave/CNAE/UF versus cruzamento com SKUs reais e status de requisitos.",
        "related": [
            ("needs-review-matched-conflito-unknown", "Status matched, conflito, unknown e needs_review — carga de revisão, não liberação jurídica."),
            ("matching-catalogo-edital", "Como o matching catálogo ↔ item evita falsa elegibilidade."),
            ("pncp-feed-vs-matching-catalogo", "Feed bruto do PNCP não é o mesmo que produto de matching."),
        ],
    },
    "needs-review-matched-conflito-unknown": {
        "title": "Matched, conflito, unknown e needs_review",
        "short": "Status e needs_review",
        "hub": "guias",
        "blurb": "Cada status descreve carga de revisão comercial — não parecer jurídico.",
        "related": [
            ("alerta-edital-vs-matching-catalogo", "Quando o alerta genérico não basta para priorizar."),
            ("limites-matching-licitafit", "O que o matching não afirma (habilitação e parecer)."),
            ("matching-catalogo-edital", "Matching catálogo ↔ item com requisitos a conferir."),
        ],
    },
    "checklist-oportunidades-governo-no-erp": {
        "title": "Checklist: oportunidades de governo no ERP",
        "short": "Checklist ERP",
        "hub": "guias",
        "blurb": "O que o product lead precisa no fluxo do ERP antes de prometer “licitações no software”.",
        "related": [
            ("feature-oportunidades-alinhadas-catalogo", "Feature UI: oportunidades alinhadas ao catálogo."),
            ("integracao-api-licitafit", "Visão de produto da integração API."),
            ("go-no-go-oportunidade-catalogo", "Go/no-go comercial com base no catálogo."),
        ],
    },
    "matching-catalogo-edital": {
        "title": "Matching catálogo ↔ item de edital",
        "short": "Matching catálogo ↔ item",
        "hub": "guias",
        "blurb": "Cruzar produtos do catálogo com itens do edital sem falsa elegibilidade.",
        "related": [
            ("alerta-edital-vs-matching-catalogo", "Alerta genérico vs matching de catálogo."),
            ("needs-review-matched-conflito-unknown", "Status e needs_review na prática."),
            ("limites-matching-licitafit", "Limites: não é habilitação jurídica."),
        ],
    },
    "limites-matching-licitafit": {
        "title": "Limites do matching LicitaFit",
        "short": "Limites do matching",
        "hub": "guias",
        "blurb": "Apoio à decisão comercial — não parecer jurídico nem garantia de habilitação.",
        "related": [
            ("matching-catalogo-edital", "Como o matching funciona no fluxo comercial."),
            ("needs-review-matched-conflito-unknown", "Status matched, conflito, unknown e needs_review."),
            ("retificacao-edital-impacto-matching", "Quando o edital muda, o matching precisa reavaliar."),
        ],
    },
    "retificacao-edital-impacto-matching": {
        "title": "Retificação de edital e impacto no matching",
        "short": "Retificação e matching",
        "hub": "guias",
        "blurb": "Mudança no edital ou no documento exige reavaliar matches e alertas.",
        "related": [
            ("limites-matching-licitafit", "Limites do matching e compliance."),
            ("matching-catalogo-edital", "Matching catálogo ↔ item de edital."),
            ("o-que-e-pncp", "O papel do PNCP na divulgação de compras públicas."),
        ],
    },
    "o-que-e-pncp": {
        "title": "O que é o PNCP",
        "short": "O que é o PNCP",
        "hub": "guias",
        "blurb": "Portal Nacional de Contratações Públicas: divulgação centralizada de compras.",
        "related": [
            ("pncp-feed-vs-matching-catalogo", "Feed PNCP vs matching de catálogo."),
            ("pncp-vs-portais-de-disputa", "PNCP vs portais onde a disputa ocorre."),
            ("alerta-edital-vs-matching-catalogo", "Alerta genérico vs matching."),
        ],
    },
    "go-no-go-oportunidade-catalogo": {
        "title": "Go/no-go de oportunidade com o catálogo",
        "short": "Go/no-go com catálogo",
        "hub": "guias",
        "blurb": "Decisão comercial de avançar ou não com base em SKUs e requisitos a conferir.",
        "related": [
            ("checklist-oportunidades-governo-no-erp", "Checklist para embutir oportunidades no ERP."),
            ("needs-review-matched-conflito-unknown", "Status que orientam revisão humana."),
            ("limites-matching-licitafit", "O que o matching não garante."),
        ],
    },
    "checklist-requisitos-notebooks-monitores": {
        "title": "Checklist de requisitos: notebooks e monitores",
        "short": "Checklist notebooks e monitores",
        "hub": "guias",
        "blurb": "Requisitos técnicos modeláveis nas categorias de foco atual.",
        "related": [
            ("matching-catalogo-edital", "Matching catálogo ↔ item."),
            ("needs-review-matched-conflito-unknown", "Status de requisitos e needs_review."),
            ("limites-matching-licitafit", "Limites do matching."),
        ],
    },
    "feature-oportunidades-alinhadas-catalogo": {
        "title": "Feature UI: oportunidades alinhadas ao catálogo",
        "short": "Feature UI no ERP",
        "hub": "guias",
        "blurb": "Como a feature aparece no software do parceiro — sem falsa elegibilidade.",
        "related": [
            ("checklist-oportunidades-governo-no-erp", "Checklist de product lead para o ERP."),
            ("integracao-api-licitafit", "Integração API — visão de produto."),
            ("go-no-go-oportunidade-catalogo", "Go/no-go com o catálogo."),
        ],
    },
    "pncp-feed-vs-matching-catalogo": {
        "title": "Feed PNCP vs matching de catálogo",
        "short": "Feed PNCP vs matching",
        "hub": "comparativos",
        "blurb": "Ingestão bruta do PNCP não substitui produto de matching com catálogo.",
        "related": [
            ("alerta-edital-vs-matching-catalogo", "Alerta genérico vs matching de catálogo."),
            ("o-que-e-pncp", "O que é o PNCP."),
            ("matching-catalogo-edital", "Matching catálogo ↔ item."),
        ],
    },
    "pncp-vs-portais-de-disputa": {
        "title": "PNCP vs portais de disputa",
        "short": "PNCP vs portais de disputa",
        "hub": "comparativos",
        "blurb": "Divulgação centralizada versus onde a disputa ocorre — contexto de mercado.",
        "related": [
            ("o-que-e-pncp", "O que é o PNCP."),
            ("pncp-feed-vs-matching-catalogo", "Feed PNCP vs matching."),
            ("alerta-edital-vs-matching-catalogo", "Alerta vs matching."),
        ],
    },
    "integracao-api-licitafit": {
        "title": "Integração API LicitaFit — visão de produto",
        "short": "Integração API",
        "hub": "recursos",
        "blurb": "Endpoints e eventos já publicados na landing — sem inventar campos.",
        "related": [
            ("checklist-oportunidades-governo-no-erp", "Checklist oportunidades no ERP."),
            ("feature-oportunidades-alinhadas-catalogo", "Feature UI no ERP."),
            ("limites-matching-licitafit", "Limites do matching."),
        ],
    },
}

FEATURED = [
    "alerta-edital-vs-matching-catalogo",
    "needs-review-matched-conflito-unknown",
    "checklist-oportunidades-governo-no-erp",
    "matching-catalogo-edital",
    "limites-matching-licitafit",
    "o-que-e-pncp",
]

HEADER_RE = re.compile(r"  <header id=\"navigation\"[\s\S]*?</header>", re.M)
FOOTER_RE = re.compile(
    r"  <footer class=\"p-strip(?: is-shallow)?\"[^>]*id=\"rodape\"[\s\S]*?</footer>",
    re.M,
)
BREADCRUMB_RE = re.compile(r"          <p class=\"lf-breadcrumb\">[\s\S]*?</p>", re.M)
RELATED_RE = re.compile(
    r"    <section class=\"p-strip[^\"]*\"[^>]*id=\"(?:continue-lendo|relacionados)\"[\s\S]*?</section>\s*",
    re.M,
)
RELATED_H2_RE = re.compile(
    r"    <section class=\"p-strip[^\"]*\"[^>]*>\s*<div class=\"row\">\s*<div class=\"col-\d+\">\s*<h2>Relacionados</h2>[\s\S]*?</section>\s*",
    re.M,
)
RECURSOS_RE = re.compile(
    r"    <section class=\"p-strip\"[^>]*id=\"recursos\"[\s\S]*?</section>\s*",
    re.M,
)


def nav_html(prefix: str, selected: str | None = None) -> str:
    def href(path: str) -> str:
        if path.startswith("#"):
            return f"{prefix}index.html{path}" if prefix else path
        return f"{prefix}{path}"

    items = [
        ("produto", "Produto", href("#produto")),
        ("como", "Como funciona", href("#como-funciona")),
        ("quem", "Para quem", href("#para-quem")),
        (
            "recursos",
            "Recursos",
            href("#recursos") if not prefix else f"{prefix}index.html#recursos",
        ),
        ("preco", "Preço", href("#preco")),
        ("empresa", "Empresa", href("#empresa")),
    ]
    lis = []
    for key, label, url in items:
        sel = " is-selected" if selected == key else ""
        lis.append(
            f'          <li class="p-navigation__item{sel}">'
            f'<a class="p-navigation__link" href="{url}">{label}</a></li>'
        )
    logo = "#topo" if not prefix else f"{prefix}index.html"
    cta = "#demonstracao" if not prefix else f"{prefix}index.html#demonstracao"
    return f"""  <header id="navigation" class="p-navigation is-dark">
    <div class="p-navigation__row--25-75">
      <div class="p-navigation__banner">
        <div class="p-navigation__tagged-logo">
          <a class="p-navigation__link" href="{logo}">
            <div class="p-navigation__logo-title lf-logo">LicitaFit</div>
          </a>
        </div>
        <a href="#navigation" class="p-navigation__toggle--open" title="Menu">Menu</a>
        <a href="#topo" class="p-navigation__toggle--close" title="Fechar menu">Fechar menu</a>
      </div>
      <nav class="p-navigation__nav" aria-label="Principal">
        <ul class="p-navigation__items">
{chr(10).join(lis)}
        </ul>
        <ul class="p-navigation__items">
          <li class="p-navigation__item">
            <a class="p-navigation__link" href="{cta}">Falar com vendas</a>
          </li>
        </ul>
      </nav>
    </div>
  </header>"""


def footer_html(prefix: str) -> str:
    def h(path: str) -> str:
        if path.startswith("#"):
            return f"{prefix}index.html{path}" if prefix else path
        return f"{prefix}{path}"

    return f"""  <footer class="p-strip is-shallow" id="rodape">
    <div class="row">
      <div class="col-3">
        <p>
          <strong>LicitaFit</strong><br />
          Qualificação de licitações consciente de catálogo, para software de distribuidores de TI.
        </p>
      </div>
      <div class="col-3">
        <p class="p-muted-heading">Produto</p>
        <ul class="p-list">
          <li class="p-list__item"><a href="{h('#produto')}">Produto</a></li>
          <li class="p-list__item"><a href="{h('#como-funciona')}">Como funciona</a></li>
          <li class="p-list__item"><a href="{h('#preco')}">Preço</a></li>
          <li class="p-list__item"><a href="{h('#demonstracao')}">Demonstração</a></li>
        </ul>
      </div>
      <div class="col-3">
        <p class="p-muted-heading">Recursos</p>
        <ul class="p-list">
          <li class="p-list__item"><a href="{h('guias/')}">Guias</a></li>
          <li class="p-list__item"><a href="{h('comparativos/')}">Comparativos</a></li>
          <li class="p-list__item"><a href="{h('#faq')}">FAQ</a></li>
          <li class="p-list__item"><a href="{h('integracao-api-licitafit/')}">Integração API</a></li>
        </ul>
      </div>
      <div class="col-3">
        <p class="p-muted-heading">Empresa</p>
        <ul class="p-list">
          <li class="p-list__item"><a href="{h('#empresa')}">Launchbase Tecnologia</a></li>
        </ul>
        <p class="lf-legal">
          Apoio à decisão comercial — não é parecer jurídico nem garantia de habilitação.
        </p>
        <p class="lf-legal">Launchbase Tecnologia Ltda · CNPJ 35.078.004/0001-77</p>
      </div>
    </div>
    <div class="row" style="margin-top:1.5rem;border-top:1px solid #d9d9d9;padding-top:1rem">
      <div class="col-12">
        <p class="lf-legal u-no-margin--bottom">
          © Launchbase Tecnologia Ltda ·
          <a href="{h('#recursos')}">Recursos</a> ·
          <a href="{h('guias/')}">Guias</a> ·
          <a href="{h('comparativos/')}">Comparativos</a>
        </p>
      </div>
    </div>
  </footer>"""


def recursos_section() -> str:
    hubs = """    <section class="p-strip" id="recursos">
      <div class="row">
        <div class="col-8">
          <h2>Recursos</h2>
          <p class="p-heading--4">Aprenda e compare — sem rankings inventados</p>
          <p>
            Guias e comparativos para product leads de ERP e equipes comerciais de distribuidores de TI.
            Conteúdo educacional; o LicitaFit permanece apoio à decisão comercial.
          </p>
        </div>
      </div>
      <div class="row u-equal-height" style="margin-top:1rem">
        <div class="col-4">
          <div class="p-card">
            <p class="p-muted-heading">Hub</p>
            <h3 class="p-card__title"><a href="guias/">Guias</a></h3>
            <p class="p-card__content">
              Matching, status de requisitos, checklist de ERP, PNCP e limites do produto.
            </p>
            <p class="p-card__content"><a href="guias/">Ver guias →</a></p>
          </div>
        </div>
        <div class="col-4">
          <div class="p-card">
            <p class="p-muted-heading">Hub</p>
            <h3 class="p-card__title"><a href="comparativos/">Comparativos</a></h3>
            <p class="p-card__content">
              Contrastes honestos: alerta vs matching, feed PNCP vs produto, PNCP vs portais de disputa.
            </p>
            <p class="p-card__content"><a href="comparativos/">Ver comparativos →</a></p>
          </div>
        </div>
        <div class="col-4">
          <div class="p-card">
            <p class="p-muted-heading">Parceiro</p>
            <h3 class="p-card__title"><a href="integracao-api-licitafit/">Integração API</a></h3>
            <p class="p-card__content">
              Visão de produto dos endpoints e eventos já descritos na landing — sem inventar campos.
            </p>
            <p class="p-card__content"><a href="integracao-api-licitafit/">Ver integração →</a></p>
          </div>
        </div>
      </div>
      <div class="row" style="margin-top:2rem">
        <div class="col-12">
          <h3>Guias em destaque</h3>
        </div>
      </div>
      <div class="row u-equal-height">
"""
    cards = []
    for i, slug in enumerate(FEATURED):
        meta = PAGES[slug]
        cards.append(
            f"""        <div class="col-4">
          <div class="p-card">
            <h4 class="p-heading--5"><a href="{slug}/">{meta['title']}</a></h4>
            <p class="p-card__content">{meta['blurb']}</p>
          </div>
        </div>"""
        )
        if (i + 1) % 3 == 0 and i + 1 < len(FEATURED):
            cards.append(
                '      </div>\n      <div class="row u-equal-height" style="margin-top:1rem">'
            )
    tail = """      </div>
      <div class="row" style="margin-top:1.5rem">
        <div class="col-12">
          <p>
            <a class="p-button" href="guias/">Ver todos os guias</a>
            <a href="comparativos/">Comparativos</a>
            ·
            <a href="#faq">FAQ</a>
          </p>
        </div>
      </div>
    </section>
"""
    return hubs + "\n".join(cards) + "\n" + tail


def related_block(slug: str, prefix: str = "../") -> str:
    meta = PAGES[slug]
    items = []
    for rel_slug, note in meta["related"][:3]:
        rel = PAGES[rel_slug]
        items.append(
            f"""            <li class="p-list__item">
              <a href="{prefix}{rel_slug}/">{rel['title']}</a>
              — {note}
            </li>"""
        )
    if meta["hub"] == "guias":
        hub_link, hub_label = f"{prefix}guias/", "Ver todos os guias"
    elif meta["hub"] == "comparativos":
        hub_link, hub_label = f"{prefix}comparativos/", "Ver comparativos"
    else:
        hub_link, hub_label = f"{prefix}index.html#recursos", "Ver recursos"
    return f"""    <section class="p-strip--light" id="continue-lendo">
      <div class="row">
        <div class="col-8">
          <h2>Continue lendo</h2>
          <ul class="p-list">
{chr(10).join(items)}
          </ul>
          <p><a href="{hub_link}">{hub_label} →</a></p>
        </div>
      </div>
    </section>
"""


def breadcrumb_html(
    slug: str | None = None, hub_page: str | None = None, prefix: str = "../"
) -> str:
    parts = [
        f'<a href="{prefix}index.html">Início</a>',
        '<span class="lf-muted"> / </span>',
        f'<a href="{prefix}index.html#recursos">Recursos</a>',
    ]
    if hub_page == "guias":
        parts += ['<span class="lf-muted"> / </span>', "<span>Guias</span>"]
    elif hub_page == "comparativos":
        parts += ['<span class="lf-muted"> / </span>', "<span>Comparativos</span>"]
    elif slug:
        meta = PAGES[slug]
        if meta["hub"] == "guias":
            parts += [
                '<span class="lf-muted"> / </span>',
                f'<a href="{prefix}guias/">Guias</a>',
                '<span class="lf-muted"> / </span>',
                f'<span>{meta["short"]}</span>',
            ]
        elif meta["hub"] == "comparativos":
            parts += [
                '<span class="lf-muted"> / </span>',
                f'<a href="{prefix}comparativos/">Comparativos</a>',
                '<span class="lf-muted"> / </span>',
                f'<span>{meta["short"]}</span>',
            ]
        else:
            parts += [
                '<span class="lf-muted"> / </span>',
                f'<span>{meta["short"]}</span>',
            ]
    return (
        "          <p class=\"lf-breadcrumb\">\n            "
        + "\n            ".join(parts)
        + "\n          </p>"
    )


def main() -> None:
    index_path = ROOT / "index.html"
    index = index_path.read_text()
    index = HEADER_RE.sub(nav_html(""), index)
    index = FOOTER_RE.sub(footer_html(""), index)
    if RECURSOS_RE.search(index):
        index = RECURSOS_RE.sub(recursos_section() + "\n", index, count=1)
    else:
        index = index.replace(
            '    <section class="p-strip" id="preco">',
            recursos_section() + '\n    <section class="p-strip" id="preco">',
        )
    index_path.write_text(index)
    print("Updated index.html")

    for hub in ("guias", "comparativos"):
        path = ROOT / hub / "index.html"
        html = path.read_text()
        html = HEADER_RE.sub(nav_html("../", selected="recursos"), html)
        html = FOOTER_RE.sub(footer_html("../"), html)
        html = BREADCRUMB_RE.sub(breadcrumb_html(hub_page=hub), html, count=1)
        path.write_text(html)
        print(f"Updated {hub}/index.html")

    for slug in PAGES:
        path = ROOT / slug / "index.html"
        if not path.exists():
            print(f"MISSING {slug}")
            continue
        html = path.read_text()
        html = HEADER_RE.sub(nav_html("../", selected="recursos"), html)
        html = FOOTER_RE.sub(footer_html("../"), html)
        html = BREADCRUMB_RE.sub(breadcrumb_html(slug=slug), html, count=1)
        html = RELATED_RE.sub("", html)
        html = RELATED_H2_RE.sub("", html)
        block = related_block(slug)
        # RELATED_RE trailing \s* may eat spaces before </main>; insert flexibly
        html = re.sub(r"[ \t]*</main>", block + "  </main>", html, count=1)
        path.write_text(html)
        print(f"Updated {slug}/index.html")

    print("DONE")


if __name__ == "__main__":
    main()
