
import requests
import urllib.request
import time
from bs4 import BeautifulSoup

import os.path
from os import path

def get_response(url, filename):
    #url = 'http://olympic.org/olympic-games'
    response = requests.get(url)
    # print(response.content)
    with open(filename, 'wb') as f:
        f.write(response.content)

filename = "response.html"
url = 'http://olympic.org/olympic-games'
if(not path.exists("response.html")):
    get_response(url, filename)

soup = 0

with open('response.html', 'rb') as f:
    soup = BeautifulSoup(f.read(), 'html.parser')

var1 = soup.findAll('li', class_='summergames')
result = []

for tag in var1:
    result.append(tag.find('a', href=True)['href'])

var2 = soup.findAll('li', class_='wintergames')
for tag in var2:
    result.append(tag.find('a', href=True)['href'])

#print(result)

url = "https://olympic.org" + result[6]
get_response(url, "athens.html")

with open('athens.html', 'rb') as f:
    soup = BeautifulSoup(f.read(), 'html.parser')
    
values = soup.findAll('div', class_='text-box')
apple = []
count = 0
athens_stats = []
for a in values:
    if count < 6:
        athens_stats.append(a.getText().split())
        count+=1
    else: 
        break
date = ""
fixed = []
fixed.append(athens_stats[1][0])
fixed.append("".join(athens_stats[1][1:6]))
athens_stats[1] = fixed
print(fixed)
print(athens_stats)
# for tag in values:
#     print(tag.find("strong"))
    #result.append(tag.find('a', href=True)['href'])

#print(values)


