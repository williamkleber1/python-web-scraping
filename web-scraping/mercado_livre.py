"""
    consumindo busca do mercado livre
"""

import requests

from bs4 import BeautifulSoup
import pandas as pd

def get_preco(produto):
    valor = produto.find('span', 'price-tag-fraction').get_text(strip=True)
    try: 
        centavos= produto.find('span', 'price-tag-cents').get_text(strip=True)
        return f'{valor},{centavos}'
    except:
        return f'{valor},00'

def main():
  
    url_base = "https://lista.mercadolivre.com.br/"

    produto = "mi band 5"# input("qual o nome do produto?\n")

    response = requests.get(url_base + produto)

    site = BeautifulSoup(response.text, "html.parser")
    produtos = site.select('.ui-search-result')

    print(f"Foram encontrados {len(produtos)} produtos.")

    produtos_lista = []
    for produto in produtos:
        print(produto.find('h2', 'shops__item-title').get_text(strip=True))
        print(produto.find('a','ui-search-link' )['href'])
        print("preço ",get_preco(produto))

        produtos_lista.append([
            produto.find('h2', 'shops__item-title').get_text(strip=True),
            get_preco(produto),
            produto.find('a','ui-search-link' )['href']
            
        ])
        
    
    produtos_data = pd.DataFrame(produtos_lista, columns=["Produto", "preco", "link"])
    produtos_data.to_csv('results/produtos.csv', index=False, encoding = 'utf-8-sig', sep = ';')

# __name__
if __name__=="__main__":
	main()


