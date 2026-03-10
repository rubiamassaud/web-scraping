# 🛒 Amazon Web Scraping

Script para extração automatizada de informações de produtos da Amazon, com suporte a exportação em CSV.

---

## 💡 Como funciona

1. Recebe a URL de um produto da Amazon
2. Faz a requisição HTTP simulando um navegador real (headers configurados)
3. Faz o parse do HTML com BeautifulSoup
4. Extrai título, preço à vista, preço parcelado e avaliação
5. Exibe os dados formatados e oferece a opção de salvar em CSV

---

## 🗂️ Estrutura do projeto

```
amazon-web-scraping/
│
├── amazon_scraping.py     # Script principal
├── produto_amazon.csv     # Arquivo de saída gerado após execução (opcional)
└── README.md
```

---

## ⚙️ Instalação

**1. Clone o repositório**
```bash
git clone https://github.com/rubiamassaud/web-scraping.git
cd web-scraping
```

**2. Crie e ative um ambiente virtual**
```bash
python -m venv venv
source venv/bin/activate      # Linux/macOS
venv\Scripts\activate         # Windows
```

**3. Instale as dependências**
```bash
pip install requests beautifulsoup4
```

---

## ▶️ Uso

**URL padrão (definida no script):**
```bash
python amazon_scraping.py
```

**URL personalizada via argumento:**
```bash
python amazon_scraping.py "https://www.amazon.com.br/dp/seu-produto"
```

**Saída esperada:**
```
[INFO] Buscando informacoes de: https://...
[OK] Requisicao bem sucedida!

[INFO] Extraindo dados do produto...

============================================================
INFORMACOES DO PRODUTO
============================================================
Produto: Nome do produto
Preco a vista: R$ 199,90
Preco parcelado: 10x R$ 19,99
Avaliacao: 4,5 de 5 estrelas
============================================================

Deseja salvar os dados em um arquivo? (s/n):
```

---

## 📦 Dados extraídos

| Campo | Descrição |
|---|---|
| `produto` | Título completo do produto |
| `preco_vista` | Preço à vista |
| `preco_parcelado` | Melhor oferta parcelada |
| `avaliacao` | Nota de avaliação dos compradores |

---

## 📋 Detalhes técnicos

- **Headers customizados** — User-Agent, Accept-Language e Referer configurados para simular um navegador real e reduzir bloqueios
- **Seletores centralizados** — todos os seletores CSS/ID ficam em um dicionário `SELECTORS`, facilitando manutenção quando a Amazon atualiza o layout
- **Extração segura** — função `extrair_texto_seguro` trata exceções elemento a elemento, evitando que a falha em um campo interrompa toda a coleta
- **CSV incremental** — ao salvar, o script detecta se o arquivo já existe e adiciona uma linha (`append`), preservando coletas anteriores

---

## ⚠️ Aviso

Este projeto foi desenvolvido para fins educacionais. Ao utilizar, respeite os [Termos de Uso da Amazon](https://www.amazon.com.br/gp/help/customer/display.html?nodeId=201909000) e evite requisições em volume ou frequência que possam sobrecarregar os servidores.

---

## 📦 Dependências

```
requests
beautifulsoup4
```

---

## 🤖 Tecnologias

- **Python 3.10+**
- **Requests** — requisições HTTP
- **BeautifulSoup4** — parse e extração de HTML
