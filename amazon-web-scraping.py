# Importando Bibliotecas
import requests as rq
from bs4 import BeautifulSoup as bs
import re

# Coletando dados da Amazon
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/144.0.0.0 Safari/537.36",
    "Accept-Language": "pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8",
    "Referer": "https://www.google.com/"
}
projeto_amazon = rq.get("https://a.co/d/2upF4gx", headers=HEADERS)
amazon = bs(projeto_amazon.content, 'html.parser')
print(amazon.prettify())

produto = amazon.find(id="productTitle").getText().strip()
preco_a_vista = amazon.find("span", class_="a-offscreen").getText()
preco_parcelado = amazon.find("span", id="best-offer-string-cc").getText()
avaliacao = amazon.find("i", class_="a-star-5").getText().strip()

print("Nome do produto:", produto)
print("Valor à vista", preco_a_vista)
print("Valor parcelado", preco_parcelado)
print("Avaliação", avaliacao)
