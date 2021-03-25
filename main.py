import requests
import json
from bs4 import BeautifulSoup
import re


html = requests.get('https://www.behance.net/tanya_durs').text
soup = BeautifulSoup(html, 'html.parser')
value = soup.find('div', class_='UserInfo-column-TMV').text
value = value.replace(",", "")
numbers = re.findall('\d+', value)


views = print('Project Views ' + numbers[0])
appreciations = print('Appreciations ' + numbers[1])
followers = print('Followers ' + numbers[2])
following = print('Following ' + numbers[3])
