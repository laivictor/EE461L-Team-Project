import json
from flask import Flask, render_template
from json2html import *

app = Flask(__name__)

#to add more pages create more of these functions with /custom-url
@app.route('/')
def home():
    return render_template(
            'home.html')

@app.route('/countries')
def countries():
   # linksFile = open('countries.json', 'r')
   # country = json.load(linksFile)   
    with open('countries.json') as json_file:
        country = json.load(json_file)
    afg = json2html.convert(json = country[0])
    return render_template(
            'countries.html', country = afg)

@app.route('/sports')
def sports():
    return render_template(
            'sports.html')

@app.route('/venues')
def venues():
    return render_template(
            'venues.html')
            
    # return render_template(
    #         'home.html', other_param1='hello', other_param2='hey')

if __name__ == '__main__':
    # This is used when running locally only. When deploying to Google App
    # Engine, a webserver process such as Gunicorn will serve the app. This
    # can be configured by adding an `entrypoint` to app.yaml.
    app.run(host='127.0.0.1', port=8080, debug=True)
# [END gae_python37_app]
