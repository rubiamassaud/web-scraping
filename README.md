🛒 Amazon Web Scraping
Script Python para extrair informações de produtos da Amazon de forma automatizada.

📋 Descrição
Este projeto realiza web scraping na Amazon para coletar informações de produtos, incluindo:

Nome do produto
Preço à vista
Preço parcelado
Avaliação dos clientes

🚀 Tecnologias Utilizadas
Python 3.x
requests - Para fazer requisições HTTP
BeautifulSoup4 - Para parsing de HTML
time - Para adicionar delays entre requisições

📦 Instalação
1. Clone o repositório
bashgit clone https://github.com/rubiamassaud/web-scraping.git
cd web-scraping
2. Instale as dependências
bashpip install -r requirements.txt

💻 Como Usar
Uso Básico
bashpython amazon-web-scraping-melhorado.py
Uso com URL Personalizada
bashpython amazon-web-scraping-melhorado.py "https://a.co/d/sua-url-aqui"

📊 Exemplo de Saída
🔍 Buscando informações de: https://a.co/d/2upF4gx
✅ Requisição bem sucedida!

📦 Extraindo dados do produto...

============================================================
📊 INFORMAÇÕES DO PRODUTO
============================================================
🏷️  Produto: Echo Dot (5ª Geração) | O Echo Dot com o melhor som...
💰 Preço à vista: R$ 399,00
💳 Preço parcelado: 10x de R$ 39,90
⭐ Avaliação: 4,5 de 5 estrelas
============================================================

💾 Deseja salvar os dados em um arquivo? (s/n):

🔧 Funcionalidades
✅ Tratamento de erros robusto
✅ Encoding UTF-8 para caracteres especiais
✅ Headers customizados para evitar bloqueios
✅ Funções organizadas e reutilizáveis
✅ Opção de salvar dados em arquivo
✅ Timeout em requisições
✅ Delays para não sobrecarregar o servidor
✅ Mensagens informativas com emojis

📁 Estrutura do Projeto
web-scraping/
│
├── amazon-web-scraping.py    # Versão original
├── requirements.txt                     # Dependências do projeto
└── README.md                           # Documentação

⚠️ Aviso Legal
Este projeto é apenas para fins educacionais. Ao fazer web scraping:
Respeite o robots.txt do site
Não sobrecarregue os servidores com muitas requisições
Verifique os Termos de Serviço da Amazon
Use delays entre requisições
Considere usar APIs oficiais quando disponíveis

🔮 Melhorias Futuras
 Suporte para múltiplos produtos
 Exportação para CSV/JSON
 Monitoramento de preços ao longo do tempo
 Notificações quando o preço cair
 Interface gráfica (GUI)
 Suporte para outras lojas online

🤝 Contribuindo
Contribuições são bem-vindas! Sinta-se à vontade para:

📝 Licença
Este projeto está sob a licença MIT. Veja o arquivo LICENSE para mais detalhes.

👩‍💻 Autora
Rubia Massaud

GitHub: @rubiamassaud

📞 Contato
Se você tiver dúvidas ou sugestões, sinta-se à vontade para abrir uma issue no GitHub!

⭐ Se este projeto foi útil para você, considere dar uma estrela!
