import requests
from bs4 import BeautifulSoup
import re
import pandas as pd
from datetime import date
data = {}


# function that is getting values from the behance site
def get_stat_today():
    html = requests.get('https://www.behance.net/tanya_durs').text
    soup = BeautifulSoup(html, 'html.parser')
    value = soup.find_all('tr', class_="UserInfo-statRow-Erw")
    key = 0

    for element in value:
        # key = element.find('td', class_='UserInfo-statColumn-1vg').text
        key_val = element.find(
            'td', class_='UserInfo-statColumn-1vg UserInfo-statValue-1_-').text
        key_val = key_val.replace(',', '')
        data[key] = int(key_val)
        key += 1


get_stat_today()

# df = pd.read_excel('Stats.xlsx')
# reading and flipping the table to extract previouse day data
df = pd.read_excel("test.xlsx")
df = df.T

# getting the last day data and making the diff arg that will be used to form the
# new row of data
last_day_stat = df.loc[df.index[-1], 0:3]
last_day_stat = pd.to_numeric(last_day_stat)
current_day_stat = pd.Series(data)
diff = current_day_stat - last_day_stat

# for # DEBUG:
# print(last_day_stat)
# print(current_day_stat)
# print(diff)


# here we are looking shape the series and make it ready to addotion
cur_date = date.today()
infront = pd.Series("-", index=[4])
current_day_stat = current_day_stat.append([infront, diff], ignore_index=True)
current_day_stat

current_day_stat.name = date.today()
df = df.append(current_day_stat)
df = df.T
df.to_excel('test.xlsx', index=False)
