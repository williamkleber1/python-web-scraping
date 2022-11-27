import requests
from bs4 import BeautifulSoup
import pandas as pd



# Defining main function
def main():
  country_list = []

  r= requests.get('https://www.scrapethissite.com/pages/simple/')

  soup = BeautifulSoup(r.text, 'html.parser')


  for country in soup.select('.country'):
    country_name = country.find('h3', 'country-name').get_text(strip=True)
    country_capital = country.find('span', 'country-capital').get_text(strip=True)
    country_population = country.find('span', 'country-population').get_text(strip=True)
    country_area = country.find('span', 'country-area').get_text(strip=True)

    country_list.append([country_name, country_capital, country_population, country_area])

    #breakpoint()

  countries = pd.DataFrame(country_list, columns=["country", "capital", "population", "area"])

  countries.to_csv('results/results.csv', index=False, encoding = 'utf-8-sig', sep = ';')
    


# __name__
if __name__=="__main__":
	main()