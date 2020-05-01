import pymongo
import json
from pymongo import MongoClient

client = MongoClient("mongodb+srv://chrisacosta:countrydb@countries-ob9ek.gcp.mongodb.net/test?retryWrites=true&w=majority")
db = client.countries_db

def getCountries():
    countries = db.countries
    return countries.find()

def getHostCities():
    cities = db.host_cities
    return cities.find_one()
    
'''

def create_sports_table():
    sports.drop()#clears table
    with open('templates/sports/sport.json') as sportfile:
        sport = json.load(sportfile)
    sportdict = {"sport":sport}
    sports.insert_one(sportdict)
    return


def get_sport():
    data = sports.find_one()
    return data["sport"]


def create_cities_table():
    cities.drop()#clears table
    with open("host-cities/venues.json") as json_f:
        data = json.load(json_f)
    cities.insert_one(data)
    return

'''

