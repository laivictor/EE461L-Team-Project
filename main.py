from flask import Flask, render_template, request, Markup
import json, operator
from json2html import *
import countrydb
import pandas as pd

app = Flask(__name__)
app.jinja_env.add_extension('jinja2.ext.loopcontrols')



#to add more pages create more of these functions with /custom-url
@app.route('/')
def home():

    with open('about.json', 'r') as about_file:
        stats_o = json.load(about_file)
        stats = json2html.convert(json = stats_o)
    return render_template(
            'home.html', stats = stats, obj = stats_o)

@app.route('/countries')
def countries():
    allcountries = countrydb.get_all_countries()
    allcountries = sorted(allcountries, key = lambda i: i['country'])
    return render_template(
            'countries.html', allcountries = allcountries)

@app.route('/countries/<string:page_name>/')
def open_country(page_name):
    countries = countrydb.get_all_countries()


    tb = [i for i in countries if i['country']==page_name][0]
    img = tb['img']
    tb = [{k: v for k, v in d.items() if k !='ranker'} for d in tb['data']]
    for i in tb:
        i.update({"games" : '<a href="/host-cities/select?game=' + i["games"].replace(' ', '') + '">' + i["games"] + '</a>'})    
    return render_template('countries_template.html', table = tb, country = page_name, img = img)
    
@app.route('/host-cities')
def venues():
    data = countrydb.get_all_host_cities()
    del data["_id"] #delete mongoid from this
    return render_template(
            'host-cities.html', obj=data)

@app.route('/host-cities/select')
def select():
    key= request.args.get('game')#yearseason
    data = countrydb.get_all_host_cities()
    del data["_id"] #delete mongoid from this
    obj = json.dumps(data[key],indent=4, sort_keys=True)
    obj = json.loads(obj)

    return render_template(
            'host-template.html', obj=obj, medals=Markup(obj["medal_table"]))


@app.route('/sports')
def sports():
    with open('templates/sports/sport.json') as sportfile:
        sport = json.load(sportfile)
    names = [i['name'] for i in sport]
    refs = [i['ref'] for i in sport]
    imgs = ['../static/' + i['img'] for i in sport]
    num = len(names)
    return render_template(
            'sports.html', names = names, refs = refs, imgs = imgs, num = num)

@app.route('/sports/<string:page_name>/')
def open_sport(page_name):
    with open('templates/sports/sport.json') as sportfile:
        sport = json.load(sportfile)
    tb = [i for i in sport if i['name']==page_name][0]
    name = tb['name']
    img = '../../static/' + tb['img']
    banner = '../../static/' + tb['banner']
    events = tb['events']
    return render_template(
            'sports/sports_template.html', name = name, img = img, banner = banner, events = events)


    
if __name__ == '__main__':
    # This is used when running locally only. When deploying to Google App
    # Engine, a webserver process such as Gunicorn will serve the app. This
    # can be configured by adding an `entrypoint` to app.yaml.
    app.run(host='127.0.0.1', port=8081, debug=True)
# [END gae_python37_app]
