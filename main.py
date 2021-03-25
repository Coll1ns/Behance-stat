import requests
import json
from bs4 import BeautifulSoup
import re


html = requests.get('https://www.behance.net/tanya_durs').text
soup = BeautifulSoup(html, 'html.parser')
value = soup.find('div', class_='UserInfo-column-TMV').text
value = value.replace(",", "")
numbers = re.findall('\d+', value)

table = []
row = []
row.append('Project Views ' + numbers[0])
row.append('Appreciations ' + numbers[1])
row.append('Followers ' + numbers[2])
row.append('Following ' + numbers[3])
table.append(row)
print(row)

print(type(numbers))
