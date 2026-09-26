# Notas de pesquisa , CruzaEdital (2026-09-25)

## Mercado
- Abradisti Estudo Setorial 2026 (IT Data): distribuição TIC R$ 30,7 bi em 2025 (+7%); hardware 44,5%; 51 associados = 87% do setor; governo ~20% investimentos TIC (fraco em 2025).
  URL: https://abradisti.org.br/noticias/setor-de-distribuicao-de-tic-movimenta-r-307-bilhoes-e-cresce-7-em-2025-aponta-abradisti/
- ATA360 (claim secundário citando PNCP/MGI): >R$ 1 tri compras públicas 2025; >1 mi processos. Tratar como claim de vendor, não IBGE.
- ABINEE: eletroeletrônico R$ 270,8 bi 2025; Informática R$ 47,753 bi.

## PNCP
- Manual Integração v2.6 (31/08/2026): https://pncp.gov.br/manual/pt-br/latest/
- Produção API: https://pncp.gov.br/api/pncp , manutenção exige JWT
- Consulta pública: https://pncp.gov.br/api/consulta , /v1/contratacoes/publicacao etc.
- Swagger consulta: https://pncp.gov.br/api/consulta/swagger-ui/index.html
- Itens: GET /v1/orgaos/{cnpj}/compras/{ano}/{sequencial}/itens , campos descricao, catalogoCodigoItem, ncmNbsCodigo, quantidade, valorUnitarioEstimado
- Dados abertos: https://www.gov.br/pncp/pt-br/acesso-a-informacao/dados-abertos
- CSV repositório: https://repositorio.dados.gov.br/seges/comprasgov/anual/
- Compras.gov dados abertos: https://www.gov.br/compras/pt-br/cidadao/portal-de-dados-abertos
- Swagger compras: https://dadosabertos.compras.gov.br/swagger-ui/index.html

## Nota técnica
- Curl TLS ao pncp.gov.br falhou do box (EOF SSL) em 2026-09-25; documentação e gist manuais usáveis; revalidar conectividade operacional.

## Concorrentes verificados
- ConLicitação, Licitei, Licitar Digital, Sollicita (Negócios Públicos), Nextera Licitações (Winthor), JD System WSGE Licitações, LicitaCloud, ATA360
- "Bidu" como produto de alertas: NÃO verificado em pesquisa 2026-09-25

## ICP software
- Onclick, Soften, Softcom Tecnologia, SIAC, ATS Resulth, Sankhya, CIGAM, TOTVS Winthor + partners (Nextera, MáximaTech, PowerGO), Lexos, JD System, Adiasoft, Target Sistemas
