import requests
from bs4 import BeautifulSoup
import re
import pandas as pd
from datetime import date

#getting the valuse on the row variable from the behance site
html = requests.get('https://www.behance.net/tanya_durs').text
soup = BeautifulSoup(html, 'html.parser')
data = {}
value = soup.find_all('tr', class_="UserInfo-statRow-Erw")
key = 0

for element in value:
	key_val = element.find('td', class_='UserInfo-statColumn-1vg UserInfo-statValue-1_-').text
	key_val = key_val.replace(',', '')
	data[key] = key_val
	key +=1
	

print(data)