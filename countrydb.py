import pymongo
import json
from pymongo import MongoClient
import pycountry_convert as pc

#app.config['MONGO_DBNAME'] = 'restdb'
#app.config['MONGO_URI'] = 'mongodb+srv://chrisacosta:countrydb@countries-ob9ek.gcp.mongodb.net/test?retryWrites=true&w=majority'
#mongo = PyMongo(app)
#mongo2 = PyMongo(app, uri="mongodb://localhost:27017/databaseTwo")
#db = mongo.db
#col = db.collection

countryClient = MongoClient("mongodb+srv://chrisacosta:countrydb@countries-ob9ek.gcp.mongodb.net/test?retryWrites=true&w=majority")
countries_db = countryClient.countries_db
countries = countries_db.countries

'''
init = False
def create_db():
    global init
    if(init):
        return

    with open('countries.json') as json_file:
        file_data = json.load(json_file)
    foo = add_continents(file_data)
    countries.insert(foo)
    init = True
'''
def get_all_countries():
    #create_db()
    return countries.find()

'''
def add_continents(allcountries):
    countrieslist = [i['country'] for i in allcountries]
    continents = []
    for c in countrieslist:
        continent_name = 'failed'
        if c == 'Australasia':
            continent_name = 'OC'
        elif c == 'Bohemia' or c == 'Crete' or c == 'Czechoslovakia' or c == 'East Germany' or c == 'West Germany' or c == 'Kosovo' or c == 'Saar' or c == 'Serbia and Montenegro' or c == 'Yugoslavia':
            continent_name = 'EU'
        elif c == 'Chinese Taipei' or c == 'Malaya' or c == 'North Borneo' or c == 'North Yemen' or c == 'South Yemen' or c == 'Soviet Union' or c == 'South Vietnam' or c == 'Timor Leste' or c == 'United Arab Republic':
            continent_name = 'AS'
        elif c == 'Congo - Brazzaville' or c == 'Congo - Kinshasa' or c == 'Guinea Bissau' or c == 'Rhodesia':
            continent_name = 'AF'
        elif c == 'Individual Olympic Athletes' or c == 'Newfoundland' or c == 'Refugee Olympic Athletes' or c == 'Unified Team' or c == 'West Indies Federation':
            continent_name = 'NA'
        elif c == 'Netherlands Antilles':
            continent_name = 'SA'
        else:
            country_code = pc.country_name_to_country_alpha2(c, cn_name_format="default")
            continent_name = pc.country_alpha2_to_continent_code(country_code)
        continents.append(continent_name)
    for c, co in zip(allcountries, continents):
        c.update({"continent" : co})
    return allcountries
'''