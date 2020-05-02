from mongodb import Database
from flask import Flask, render_template, request, Markup
import json, urllib
from urllib import *
from json2html import *
from abc import ABC, abstractmethod

class PageTemplate(ABC):

    def __init__(self, template_name, args):
        """this can be overrided by sublclasses to avoid passing in template_name parameter every time"""
        self.template_name = template_name
        self.args = args

    @abstractmethod
    def formatData(self):
        """this is abstract, it should be defined by each subclass, gets data from database and formats it to be passed as obj"""
        #manipulate data and return, data will be the parameters passed into the template
        data = None
        return data


    def getPage(self):
        """this is the same for every subclass"""
        
        nav = """<nav class='navbar navbar-inverse navbar-fixed-top navbar-expand-lg justify-content-between'>
                <div class='container-fluid'>
                <div class='navbar-header'>
                    <a class='navbar-brand' href='/'> The Olympics </a>
                </div>
                <ul class='nav navbar-nav'>
                    <li><a href='/countries'> Countries </a></li>
                <li><a href='/host-cities'> Host Cities </a></li>
                <li><a href='/sports'> Sports </a></li>
                </ul>
                </div>
            </nav>"""


        return render_template(self.template_name, obj=self.formatData(), nav=nav)
        

class HostCityTemplate(PageTemplate):
    def __init__(self):
        self.template_name= "host-cities.html"

    def formatData(self):
        data = Database.getInstance().getHostCities()
        del data["_id"] #delete mongoid from this
        for key in data.keys():#normalize some countries with different names than link
            country = data[key]["country"]
            if "China" in country:
                country = "China"
            elif "Russia" in country:
                country = "Russia"
            elif "United States" in country:
                country = "United States"
            elif "Republic of Korea" in country:
                country="South Korea"
            elif "Great Britain" in country:
                country = "United Kingdom"
            elif "Australia, Sweden" in country:
                data[key]["country"] = "<a class='btn-link' href='/countries/Australia'>Australia</a>, <a class='btn-link' href='/countries/Sweden'>Sweden</a>"
                continue

            countrylink = "<a class='btn-link' href='/countries/"+ country.replace(" ", "%20")+"'>" + data[key]["country"] +"</a>"
            data[key]["country"] = countrylink
        return data
    
class HostCitySelectTemplate(PageTemplate):
    def __init__(self, args):
        self.template_name = "host-template.html"
        self.args = args

    def formatData(self):
        key= self.args['game']#yearseason
        data = Database.getInstance().getHostCities()
        del data["_id"] #delete mongoid from this
        obj = json.dumps(data[key],indent=4, sort_keys=True)
        obj = json.loads(obj)
        return obj

class HomeTemplate(PageTemplate):
    def __init__(self):
        self.template_name = "home.html"
    
    def formatData(self):
        with open('about.json', 'r') as about_file:
            stats_o = json.load(about_file)
            stats = json2html.convert(json = stats_o)
        obj = stats_o
        obj["stats"] = stats
        return obj

class SportsTemplate(PageTemplate):
    def __init__(self):
        self.template_name = "sports.html"

    def formatData(self):
        sport = Database.getInstance().getSports()
        names = [i['name'] for i in sport]
        refs = [i['ref'] for i in sport]
        imgs = ['../static/' + i['img'] for i in sport]
        num = len(names)
        obj = {"names": names, "refs":refs, "imgs": imgs, "num":num}
        return obj
    
class OpenSportTemplate(PageTemplate):
    def __init__(self, args):
        self.template_name = "sports/sports_template.html"
        self.args = args
    
    def formatData(self):
        with open('templates/sports/sport.json') as sportfile:
            sport = json.load(sportfile)
        tb = [i for i in sport if i['name']==self.args['page_name']][0]
        name = tb['name']
        img = '../../static/' + tb['img']
        banner = '../../static/' + tb['banner']
        events = tb['events']
        obj = {"name":name, "img": img, "banner":banner, "events": events}
        return obj

class CountryTemplate(PageTemplate):
    def __init__(self):
        self.template_name = "countries.html"
    
    def formatData(self):
        allcountries = Database.getInstance().getCountries()
        allcountries = sorted(allcountries, key = lambda i: i['country'])
        return {"allcountries":allcountries}

class OpenCountryTemplate(PageTemplate):
    def __init__(self, args):
        self.template_name = "countries_template.html"
        self.args = args

    def formatData(self):
        countries = Database.getInstance().getCountries()
        tb = [i for i in countries if i['country']==self.args['page_name']][0]
        img = tb['img']
        tb = [{k: v for k, v in d.items() if k !='ranker'} for d in tb['data']]
        years = [i['games'] for i in tb]
        for i in tb:
            i.update({"games" : '<a href="/host-cities/select?game=' + i["games"].replace(' ', '') + '">' + i["games"] + '</a>'})

        return {"table":tb, "country":self.args['page_name'],"img":img, "years":years}    