from flask import Flask, render_template, request, Markup
import json
from json2html import *

app = Flask(__name__)

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
    with open('countries.json') as json_file:
        countries = json.load(json_file)
    countries = sorted(countries, key = lambda i: i['country'])
    names = [i['country'] for i in countries]
    imgs = [i['img'] for i in countries]
    num = len(names)
    return render_template(
            'countries.html', names = names, imgs = imgs, num = num)

@app.route('/countries/<string:page_name>/')
def open_country(page_name):
    with open('countries.json') as json_file:
        countries = json.load(json_file)
    tb = [i for i in countries if i['country']==page_name][0]
    del tb['img']
    table = json2html.convert(json = tb) #,table_attributes="class=\"datatable\""
    return render_template('countries_template.html', table = table)


@app.route('/host-cities')
def venues():

    data = None
    with open("host-cities/venues.json") as f:
        data = json.load(f)
    obj = json.dumps(data, indent=4, sort_keys=True)
    print(type(obj))
    return render_template(
            'host-cities.html', obj=data)

@app.route('/host-cities/select')
def select():
    key= request.args.get('game')#yearseason
    data = None
    with open("host-cities/venues.json") as f:
        data = json.load(f)
        
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
    banner = tb['banner']
    return render_template(
            'sports/sports_template.html', name = name, img = img, banner = banner)


    
if __name__ == '__main__':
    # This is used when running locally only. When deploying to Google App
    # Engine, a webserver process such as Gunicorn will serve the app. This
    # can be configured by adding an `entrypoint` to app.yaml.
    app.run(host='127.0.0.1', port=8081, debug=True)
# [END gae_python37_app]
