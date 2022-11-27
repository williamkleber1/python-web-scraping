
from bs4 import BeautifulSoup
import requests, csv

response = requests.get('https://www.scrapethissite.com/pages/simple/')
soup_obj = BeautifulSoup(response.text, 'html.parser')

with open('results/results.csv', 'w', newline='', encoding='utf-8-sig') as file_result:
	writer = csv.writer(file_result, delimiter=';', quoting=csv.QUOTE_ALL)
	writer.writerow(["country", "capital", "population"])

	for country in soup_obj.select('.country'):
		country_name = country.find('h3', 'country-name').get_text(strip=True)
		country_capital = country.find('span', 'country-capital').get_text(strip=True)
		country_population = country.find('span', 'country-population').get_text(strip=True)
		writer.writerow([country_name, country_capital, country_population])
	file_result.close()