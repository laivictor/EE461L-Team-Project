import json
import requests
import urllib.request
from bs4 import BeautifulSoup
from os import path

def scrape_photos():
    with open("venues.json") as f:
        data = json.load(f)

    for key in data:
        get_photo(key)

def get_response(url, filename):
    response = requests.get(url)
    with open(filename, 'wb') as f:
        f.write(response.content)


def get_photo(key):
    link = "https://en.wikipedia.org/wiki/"
    link = link + key[0:4] + "_" + key[4:] + "_" + "Olympics"

    file_name = "responses/wikipedia/" + key + ".html"

    if(not path.exists(file_name)):
        get_response(link, file_name)

    print(file_name)
    with open(file_name, 'rb') as f:
        soup = BeautifulSoup(f.read(), 'html.parser')
    infobox = soup.find('table', class_='infobox')
    image = infobox.find('img')
    print(image['src'])
    img_link = "https:" + image['src']
    img_data = requests.get(img_link).content
    with open("../static/host-cities/logos/" + key +'.png', 'wb') as handler:
        handler.write(img_data)

    

if __name__ == "__main__":
    scrape_photos()
    
    #https://en.wikipedia.org/wiki/2014_Winter_Olympics