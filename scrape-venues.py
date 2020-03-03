import json
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

def get_links():
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
        result.append(tag.find('a', href=True)['href'] + "+++Summer")

    var2 = soup.findAll('li', class_='wintergames')
    for tag in var2:
        result.append(tag.find('a', href=True)['href']+"+++Winter")

    return result

#print(result)

def scrape_hosts_info(link):
    """result is list of link to host"""
    link2 = link.split("+++")
    link = link2[0]
    season = link2[1]
    
    url = "https://olympic.org" + link
    file_name = "responses/" + link.strip("/") + ".html"

    if(not path.exists(file_name)):
        get_response(url, file_name)

    print(file_name)
    with open(file_name, 'rb') as f:
        soup = BeautifulSoup(f.read(), 'html.parser')
        
    values = soup.findAll('div', class_='text-box')
    
    count = 0
    athens_stats = []
    for a in values:
        if count < 6:
            athens_stats.append(a.getText().split())
            count+=1
        else: 
            
            break

    
    fixed = []
    fixed.append(athens_stats[1][0])
    fixed.append(" ".join(athens_stats[1][1:6]))
    athens_stats[1] = fixed
    fixed = []
    fixed.append(athens_stats[2][0])
    fixed.append(" ".join(athens_stats[2][1:len(athens_stats[2])]))
    athens_stats[2] = fixed
    athens_stats.append(season)
    return athens_stats



def make_dictionary(array_from_scrape):
    city =  " ".join(array_from_scrape[0][0:len(array_from_scrape[0])-1])
    year = array_from_scrape[0][-1]
    date = array_from_scrape[1][1]
    country = array_from_scrape[2][1]
    athletes = array_from_scrape[3][1]
    countries = array_from_scrape[4][1]
    events = array_from_scrape[5][1]
    season = array_from_scrape[6]






    obj = {"city":city, "year":year, "date":date, "season":season, "country":country, "athletes":athletes,
             "countries":countries, "events":events}
    return obj


if __name__ == "__main__":
    links = get_links()
    data = {}
    for link in links:
        dictionary = make_dictionary(scrape_hosts_info(link))
        if(int(dictionary['year']) < 2020):
            data[dictionary['year']+dictionary['season']] = dictionary

    with open('venues.json', 'w') as fp:
        json.dump(data, fp)
    













