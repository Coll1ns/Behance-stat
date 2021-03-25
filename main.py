import requests
from bs4 import BeautifulSoup
import re

username = input('Enter user name: ').lower()
url = 'https://www.behance.net/' + username
html = requests.get(url).text

soup = BeautifulSoup(html, 'html.parser')

table = []

value = soup.find_all('tr', class_="UserInfo-statRow-Erw")

for element in value:
    row = []
    row.append(element.find('td', class_='UserInfo-statColumn-1vg').text)
    row.append(element.find('td', class_='UserInfo-statColumn-1vg UserInfo-statValue-1_-').text)
    table.append(row)
print(table)


# value = soup.find('div', class_='UserInfo-column-TMV')
# test_val = soup.find_all('tr', class_="UserInfo-statRow-Erw")
# value = value.replace(",", "")
# numbers = re.findall('\d+', value)


# print(test_val)
# views = print('Project Views ' + numbers[0])
# appreciations = print('Appreciations ' + numbers[1])
# followers = print('Followers ' + numbers[2])
# following = print('Following ' + numbers[3])
#
