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
    with open('countries.json') as json_file:
        countries = json.load(json_file)
    
    countries = sorted(countries, key = lambda i: i['country'])
    for c in countries:
        f = open('templates/countries/' + c['country'] + '.html', 'wb')
        wr = '<!DOCTYPE html><html><head><title>Countries</title><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/css/bootstrap.min.css"><script src="https://ajax.googleapis.com/ajax/libs/jquery/3.4.1/jquery.min.js"></script><script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/js/bootstrap.min.js"></script><title></title></head><li><a href="countries"> Countries </a></li><body><br><br>' + json2html.convert(json = c) + '<nav class="navbar navbar-inverse navbar-fixed-top navbar-expand-lg justify-content-between"><div class="container-fluid"><div class="navbar-header"><a class="navbar-brand" href="/countries"> Countries </a></div><ul class="nav navbar-nav"><li><a href="/countries"> Back </a></li></body><body></body></html>'
        f.write(wr.encode())
        f.close()
    names = [i['country'] for i in countries]
    return render_template(
            'countries.html', names = names)

@app.route('/countries/<string:page_name>/')
def open_country(page_name):
    return render_template('countries/%s.html' % page_name)

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
