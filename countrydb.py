import pymongo
import json
from pymongo import MongoClient

#app.config['MONGO_DBNAME'] = 'restdb'
#app.config['MONGO_URI'] = 'mongodb+srv://chrisacosta:countrydb@countries-ob9ek.gcp.mongodb.net/test?retryWrites=true&w=majority'
#mongo = PyMongo(app)
#mongo2 = PyMongo(app, uri="mongodb://localhost:27017/databaseTwo")
#db = mongo.db
#col = db.collection

countryClient = MongoClient("mongodb+srv://chrisacosta:countrydb@countries-ob9ek.gcp.mongodb.net/test?retryWrites=true&w=majority")
countries_db = countryClient.countries_db
countries = countries_db.countries
init = False

# def create_db():
#     global init
#     if(init):
#         return

#     with open('countries.json') as json_file:
#         file_data = json.load(json_file)
#     countries.insert(file_data)
#     init = True
    
def get_all_countries():
    #create_db()
    return countries.find()