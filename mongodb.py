import pymongo
import json
from pymongo import MongoClient

class Database:

    instance = None
    client = None
    db = None

    def __init__(self):
        Database.instance = self
        Database.client = MongoClient("mongodb+srv://chrisacosta:countrydb@countries-ob9ek.gcp.mongodb.net/test?retryWrites=true&w=majority")
        Database.db = Database.client.countries_db

    @staticmethod
    def getInstance():
        if Database.instance == None:
            Database()
        return Database.instance

    def getCountries(self):
        countries = self.db.countries
        return countries.find()

    def getHostCities(self):
        cities = self.db.host_cities
        return cities.find_one()
    
    def getSports(self):
        sports = self.db.sports
        data = sports.find_one()
        return data["sport"]
    