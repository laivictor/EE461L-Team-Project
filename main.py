from flask import Flask, render_template, request, Markup
import json, operator
from json2html import *
import countrydb, TemplateMethods

app = Flask(__name__)
app.jinja_env.add_extension('jinja2.ext.loopcontrols')

#to add more pages create more of these functions with /custom-url
@app.route('/')
def home():
    home_template = TemplateMethods.HomeTemplate()
    return home_template.getPage()

@app.route('/countries')
def countries():
    country_template = TemplateMethods.CountryTemplate()
    return country_template.getPage()

@app.route('/countries/<string:page_name>/')
def open_country(page_name):
    open_country_template = TemplateMethods.OpenCountryTemplate({"page_name":page_name})
    return open_country_template.getPage()
    
@app.route('/host-cities')
def venues():
    host_template = TemplateMethods.HostCityTemplate()
    return host_template.getPage()

@app.route('/host-cities/select')
def select():
    city_template = TemplateMethods.HostCitySelectTemplate({"game": request.args.get("game")})
    return city_template.getPage()

@app.route('/sports')
def sports():
    sport_template = TemplateMethods.SportsTemplate()
    return sport_template.getPage()

@app.route('/sports/<string:page_name>/')
def open_sport(page_name):
    open_template = TemplateMethods.OpenSportTemplate({"page_name":page_name})
    return open_template.getPage()


    
if __name__ == '__main__':
    # This is used when running locally only. When deploying to Google App
    # Engine, a webserver process such as Gunicorn will serve the app. This
    # can be configured by adding an `entrypoint` to app.yaml.
    app.run(host='127.0.0.1', port=8081, debug=True)
# [END gae_python37_app]
