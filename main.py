import json

from flask import Flask, render_template, request, Markup
import json
from json2html import *

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

@app.route('/sports')
def sports():
    return render_template(
            'sports.html')


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


@app.route('/sports/archery')
def archery():
  return render_template(
          'sports/archery.html')

@app.route('/sports/artistic-swimming')
def artistic_swimming():
  return render_template(
          'sports/artistic-swimming.html')

@app.route('/sports/athletics')
def athletics():
  return render_template(
          'sports/athletics.html')

@app.route('/sports/badminton')
def badminton():
  return render_template(
          'sports/badminton.html')

@app.route('/sports/baseball-softball')
def baseball_softball():
  return render_template(
          'sports/baseball-softball.html')

@app.route('/sports/basketball')
def basketball():
  return render_template(
          'sports/basketball.html')

@app.route('/sports/beach-volleyball')
def beach_volleyball():
  return render_template(
          'sports/beach-volleyball.html')

@app.route('/sports/boxing')
def boxing():
  return render_template(
          'sports/boxing.html')

@app.route('/sports/canoe-slalom')
def canoe_slalom():
  return render_template(
          'sports/canoe-slalom.html')

@app.route('/sports/canoe-sprint')
def canoe_sprint():
  return render_template(
          'sports/canoe-sprint.html')

@app.route('/sports/cycling-bmx')
def cycling_bmx():
  return render_template(
          'sports/cycling-bmx.html')

@app.route('/sports/cycling-mountain-bike')
def cycling_mountain_bike():
  return render_template(
          'sports/cycling-mountain-bike.html')

@app.route('/sports/cycling-road')
def cycling_road():
  return render_template(
          'sports/cycling-road.html')

@app.route('/sports/cycling-track')
def cycling_track():
  return render_template(
          'sports/cycling-track.html')

@app.route('/sports/diving')
def diving():
  return render_template(
          'sports/diving.html')

@app.route('/sports/equestrian-dressage')
def equestrian_dressage():
  return render_template(
          'sports/equestrian-dressage.html')

@app.route('/sports/equestrian-eventing')
def equestrian_eventing():
  return render_template(
          'sports/equestrian-eventing.html')

@app.route('/sports/equestrian-jumping')
def equestrian_jumping():
  return render_template(
          'sports/equestrian-jumping.html')

@app.route('/sports/fencing')
def fencing():
  return render_template(
          'sports/fencing.html')

@app.route('/sports/football')
def football():
  return render_template(
          'sports/football.html')

@app.route('/sports/golf')
def golf():
  return render_template(
          'sports/golf.html')

@app.route('/sports/gymnastics-artistic')
def gymnastics_artistic():
  return render_template(
          'sports/gymnastics-artistic.html')

@app.route('/sports/gymnastics-rhythmic')
def gymnastics_rhythmic():
  return render_template(
          'sports/gymnastics-rhythmic.html')

@app.route('/sports/handball')
def handball():
  return render_template(
          'sports/handball.html')

@app.route('/sports/hockey')
def hockey():
  return render_template(
          'sports/hockey.html')

@app.route('/sports/judo')
def judo():
  return render_template(
          'sports/judo.html')

@app.route('/sports/karate')
def karate():
  return render_template(
          'sports/karate.html')

@app.route('/sports/marathon-swimming')
def marathon_swimming():
  return render_template(
          'sports/marathon-swimming.html')

@app.route('/sports/modern-pentathlon')
def modern_pentathlon():
  return render_template(
          'sports/modern-pentathlon.html')

@app.route('/sports/rowing')
def rowing():
  return render_template(
          'sports/rowing.html')

@app.route('/sports/rugby')
def rugby():
  return render_template(
          'sports/rugby.html')

@app.route('/sports/sailing')
def sailing():
  return render_template(
          'sports/sailing.html')

@app.route('/sports/shooting')
def shooting():
  return render_template(
          'sports/shooting.html')

@app.route('/sports/skateboarding')
def skateboarding():
  return render_template(
          'sports/skateboarding.html')

@app.route('/sports/sport-climbing')
def sport_climbing():
  return render_template(
          'sports/sport-climbing.html')

@app.route('/sports/surfing')
def surfing():
  return render_template(
          'sports/surfing.html')

@app.route('/sports/swimming')
def swimming():
  return render_template(
          'sports/swimming.html')

@app.route('/sports/table-tennis')
def table_tennis():
  return render_template(
          'sports/table-tennis.html')

@app.route('/sports/taekwondo')
def taekwondo():
  return render_template(
          'sports/taekwondo.html')

@app.route('/sports/tennis')
def tennis():
  return render_template(
          'sports/tennis.html')

@app.route('/sports/trampoline')
def trampoline():
  return render_template(
          'sports/trampoline.html')

@app.route('/sports/triathlon')
def triathlon():
  return render_template(
          'sports/triathlon.html')

@app.route('/sports/volleyball')
def volleyball():
  return render_template(
          'sports/volleyball.html')

@app.route('/sports/water-polo')
def water_polo():
  return render_template(
          'sports/water-polo.html')

@app.route('/sports/weightlifting')
def weightlifting():
  return render_template(
          'sports/weightlifting.html')

@app.route('/sports/wrestling-freestyle')
def wrestling_freestyle():
  return render_template(
          'sports/wrestling-freestyle.html')

@app.route('/sports/wrestling-greco-roman')
def wrestling_greco_roman():
  return render_template(
          'sports/wrestling-greco-roman.html')

@app.route('/sports/alpine-skiing')
def alpine_skiing():
  return render_template(
          'sports/alpine-skiing.html')

@app.route('/sports/biathlon')
def biathlon():
  return render_template(
          'sports/biathlon.html')

@app.route('/sports/bobsleigh')
def bobsleigh():
  return render_template(
          'sports/bobsleigh.html')

@app.route('/sports/cross-country-skiing')
def cross_country_skiing():
  return render_template(
          'sports/cross-country-skiing.html')

@app.route('/sports/curling')
def curling():
  return render_template(
          'sports/curling.html')

@app.route('/sports/figure-skating')
def figure_skating():
  return render_template(
          'sports/figure-skating.html')

@app.route('/sports/freestyle-skiing')
def freestyle_skiing():
  return render_template(
          'sports/freestyle-skiing.html')

@app.route('/sports/ice-hockey')
def ice_hockey():
  return render_template(
          'sports/ice-hockey.html')

@app.route('/sports/luge')
def luge():
  return render_template(
          'sports/luge.html')

@app.route('/sports/nordic-combined')
def nordic_combined():
  return render_template(
          'sports/nordic-combined.html')

@app.route('/sports/short-track')
def short_track():
  return render_template(
          'sports/short-track.html')

@app.route('/sports/skeleton')
def skeleton():
  return render_template(
          'sports/skeleton.html')

@app.route('/sports/ski-jumping')
def ski_jumping():
  return render_template(
          'sports/ski-jumping.html')

@app.route('/sports/snowboard')
def snowboard():
  return render_template(
          'sports/snowboard.html')

@app.route('/sports/speed-skating')
def speed_skating():
  return render_template(
          'sports/speed-skating.html')

@app.route('/sports/basque-pelota')
def basque_pelota():
  return render_template(
          'sports/basque-pelota.html')


    
if __name__ == '__main__':
    # This is used when running locally only. When deploying to Google App
    # Engine, a webserver process such as Gunicorn will serve the app. This
    # can be configured by adding an `entrypoint` to app.yaml.
    app.run(host='127.0.0.1', port=8082, debug=True)
# [END gae_python37_app]
