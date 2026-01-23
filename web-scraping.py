# Importando Bibliotecas
import requests as rq
from bs4 import BeautifulSoup as bs

# Pegando HTML do Site
html_completo = rq.get("http://webscraping.andreregino.com.br")
html_formatado = bs(html_completo.content, 'html.parser')

print(html_formatado.prettify())

todas_ocorrencias_h2 = html_formatado.find_all(["h2", "h1"])
for ocorrencia_h2 in todas_ocorrencias_h2:
    print(ocorrencia_h2.text)

# Pegando conteúdo usando Classes e IDs
preco = html_formatado.find_all(class_="card-title pricing-card-title")
print(preco)
pre_requisito = html_formatado.find(id="pre-requisite-section")
print(pre_requisito)

# Pegando conteúdo usando filtro de texto
todas_ocorrencias_h2 = html_formatado.find_all(["h2", "h1"], text="Reviews")
for ocorrencia_h2 in todas_ocorrencias_h2:
    print(ocorrencia_h2.text)

    import re

    todas_ocorrencias_h2 = html_formatado.find_all(
        ["h2", "h1"], text=re.compile("Para que aprender"))
for ocorrencia_h2 in todas_ocorrencias_h2:
    print(ocorrencia_h2.text)

    botao = html_formatado.find(class_="price").a
    print(botao['href'])

    imagem = html_formatado.find("img")
    print(imagem['src'])

    elemento_da_lista = html_formatado.find(
        "section", class_="content-section").ul.li
    print(elemento_da_lista)

    quarto_elemento_lista = html_formatado.select(
        ".content-section ul li:nth-of-type(4)")
    print(quarto_elemento_lista)
