# -*- coding: utf-8 -*-
"""
Amazon Web Scraping
Script para extrair informações de produtos da Amazon
"""

import requests as rq
from bs4 import BeautifulSoup as bs
import time
import sys
import csv
import os


# Configurações globais
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/144.0.0.0 Safari/537.36",
    "Accept-Language": "pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8",
    "Referer": "https://www.google.com/"
}

# Seletores CSS/ID para os elementos da página
SELECTORS = {
    'titulo': {'id': 'productTitle'},
    'preco_vista': {'class': 'a-offscreen'},
    'preco_parcelado': {'id': 'best-offer-string-cc'},
    'avaliacao': {'class': 'a-star-5'}
}


def buscar_produto(url):
    """
    Faz a requisição HTTP para a URL do produto
    
    Args:
        url (str): URL do produto na Amazon
        
    Returns:
        BeautifulSoup: Objeto soup com o HTML parseado ou None em caso de erro
    """
    try:
        print(f"[INFO] Buscando informacoes de: {url}")
        response = rq.get(url, headers=HEADERS, timeout=10)
        response.encoding = 'utf-8'
        
        # Verifica se a requisição foi bem sucedida
        if response.status_code == 200:
            print("[OK] Requisicao bem sucedida!")
            return bs(response.content, 'html.parser')
        else:
            print(f"[ERRO] Erro na requisicao. Status code: {response.status_code}")
            return None
            
    except rq.exceptions.RequestException as e:
        print(f"[ERRO] Erro ao fazer requisicao: {e}")
        return None


def extrair_texto_seguro(soup, selector_type, selector_value):
    """
    Extrai texto de um elemento HTML de forma segura
    
    Args:
        soup (BeautifulSoup): Objeto soup
        selector_type (str): Tipo do seletor ('id' ou 'class')
        selector_value (str): Valor do seletor
        
    Returns:
        str: Texto extraído ou mensagem de erro
    """
    try:
        if selector_type == 'id':
            elemento = soup.find(id=selector_value)
        elif selector_type == 'class':
            elemento = soup.find(class_=selector_value)
        else:
            return "Tipo de seletor invalido"
        
        if elemento:
            return elemento.get_text().strip()
        else:
            return "Nao encontrado"
            
    except AttributeError:
        return "Erro ao extrair"


def extrair_dados_produto(soup):
    """
    Extrai todas as informações do produto
    
    Args:
        soup (BeautifulSoup): Objeto soup com HTML do produto
        
    Returns:
        dict: Dicionário com os dados do produto
    """
    print("\n[INFO] Extraindo dados do produto...")
    
    dados = {}
    
    # Extrai título do produto
    dados['produto'] = extrair_texto_seguro(
        soup, 'id', SELECTORS['titulo']['id']
    )
    
    # Extrai preço à vista
    dados['preco_vista'] = extrair_texto_seguro(
        soup, 'class', SELECTORS['preco_vista']['class']
    )
    
    # Extrai preço parcelado
    dados['preco_parcelado'] = extrair_texto_seguro(
        soup, 'id', SELECTORS['preco_parcelado']['id']
    )
    
    # Extrai avaliação
    dados['avaliacao'] = extrair_texto_seguro(
        soup, 'class', SELECTORS['avaliacao']['class']
    )
    
    return dados


def exibir_dados(dados):
    """
    Exibe os dados do produto formatados
    
    Args:
        dados (dict): Dicionário com os dados do produto
    """
    print("\n" + "="*60)
    print("INFORMACOES DO PRODUTO")
    print("="*60)
    print(f"Produto: {dados.get('produto', 'N/A')}")
    print(f"Preco a vista: {dados.get('preco_vista', 'N/A')}")
    print(f"Preco parcelado: {dados.get('preco_parcelado', 'N/A')}")
    print(f"Avaliacao: {dados.get('avaliacao', 'N/A')}")
    print("="*60 + "\n")


def salvar_dados(dados, arquivo='produto_amazon.csv'):
    """
    Salva os dados em um arquivo CSV
    
    Args:
        dados (dict): Dicionário com os dados do produto
        arquivo (str): Nome do arquivo para salvar
    """
    try:
        # Se o arquivo já existe, apenas adiciona uma linha (append)
        # Se não existe, cria com cabeçalho
        mode = 'a' if os.path.exists(arquivo) else 'w'

        with open(arquivo, mode, newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=dados.keys())
            if mode == 'w':
                writer.writeheader()
            writer.writerow(dados)
        
        print(f"[OK] Dados salvos em: {arquivo}")
        
    except Exception as e:
        print(f"[ERRO] Erro ao salvar arquivo: {e}")


def main():
    """
    Função principal do programa
    """
    # URL do produto (pode ser modificada ou recebida como input)
    url_produto = "https://a.co/d/2upF4gx"
    
    # Opção para URL customizada
    if len(sys.argv) > 1:
        url_produto = sys.argv[1]
        print(f"[INFO] Usando URL personalizada: {url_produto}")
    
    # Busca o produto
    soup = buscar_produto(url_produto)
    
    if soup is None:
        print("[ERRO] Nao foi possivel obter os dados do produto.")
        return
    
    # Adiciona delay para ser "gentil" com o servidor
    time.sleep(1)
    
    # Extrai os dados
    dados = extrair_dados_produto(soup)
    
    # Exibe os dados
    exibir_dados(dados)
    
    # Pergunta se deseja salvar
    salvar = input("Deseja salvar os dados em um arquivo? (s/n): ").lower()
    if salvar == 's':
        nome_arquivo = input("Nome do arquivo (pressione Enter para usar 'produto_amazon.csv'): ").strip()
        if not nome_arquivo:
            nome_arquivo = 'produto_amazon.csv'
        salvar_dados(dados, nome_arquivo)
    
    print("\n[OK] Scraping concluido!")


if __name__ == "__main__":
    main()
