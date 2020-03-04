from flask import Flask, render_template
import os

app = Flask(__name__)

#to add more pages create more of these functions with /custom-url
@app.route('/')
def home():
    return render_template(
            'home.html')

@app.route('/countries')
def countries():
    return render_template(
            'countries.html')

@app.route('/sports')
def sports():
    return render_template(
            'sports.html')

@app.route('/venues')
def venues():
    return render_template(
            'venues.html')


@app.route('/sports/archery')
def archery():
  return render_template(
          'sports/archery.html')

@app.route('/sports/artistic_swimming')
def artistic_swimming():
  return render_template(
          'sports/artistic_swimming.html')

@app.route('/sports/athletics')
def athletics():
  return render_template(
          'sports/athletics.html')

@app.route('/sports/badminton')
def badminton():
  return render_template(
          'sports/badminton.html')

@app.route('/sports/baseball_softball')
def baseball_softball():
  return render_template(
          'sports/baseball_softball.html')

@app.route('/sports/basketball')
def basketball():
  return render_template(
          'sports/basketball.html')

@app.route('/sports/beach_volleyball')
def beach_volleyball():
  return render_template(
          'sports/beach_volleyball.html')

@app.route('/sports/boxing')
def boxing():
  return render_template(
          'sports/boxing.html')

@app.route('/sports/canoe_slalom')
def canoe_slalom():
  return render_template(
          'sports/canoe_slalom.html')

@app.route('/sports/canoe_sprint')
def canoe_sprint():
  return render_template(
          'sports/canoe_sprint.html')

@app.route('/sports/cycling_bmx')
def cycling_bmx():
  return render_template(
          'sports/cycling_bmx.html')

@app.route('/sports/cycling_mountain_bike')
def cycling_mountain_bike():
  return render_template(
          'sports/cycling_mountain_bike.html')

@app.route('/sports/cycling_road')
def cycling_road():
  return render_template(
          'sports/cycling_road.html')

@app.route('/sports/cycling_track')
def cycling_track():
  return render_template(
          'sports/cycling_track.html')

@app.route('/sports/diving')
def diving():
  return render_template(
          'sports/diving.html')

@app.route('/sports/equestrian_dressage')
def equestrian_dressage():
  return render_template(
          'sports/equestrian_dressage.html')

@app.route('/sports/equestrian_eventing')
def equestrian_eventing():
  return render_template(
          'sports/equestrian_eventing.html')

@app.route('/sports/equestrian_jumping')
def equestrian_jumping():
  return render_template(
          'sports/equestrian_jumping.html')

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

@app.route('/sports/gymnastics_artistic')
def gymnastics_artistic():
  return render_template(
          'sports/gymnastics_artistic.html')

@app.route('/sports/gymnastics_rhythmic')
def gymnastics_rhythmic():
  return render_template(
          'sports/gymnastics_rhythmic.html')

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

@app.route('/sports/marathon_swimming')
def marathon_swimming():
  return render_template(
          'sports/marathon_swimming.html')

@app.route('/sports/modern_pentathlon')
def modern_pentathlon():
  return render_template(
          'sports/modern_pentathlon.html')

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

@app.route('/sports/sport_climbing')
def sport_climbing():
  return render_template(
          'sports/sport_climbing.html')

@app.route('/sports/surfing')
def surfing():
  return render_template(
          'sports/surfing.html')

@app.route('/sports/swimming')
def swimming():
  return render_template(
          'sports/swimming.html')

@app.route('/sports/table_tennis')
def table_tennis():
  return render_template(
          'sports/table_tennis.html')

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

@app.route('/sports/water_polo')
def water_polo():
  return render_template(
          'sports/water_polo.html')

@app.route('/sports/weightlifting')
def weightlifting():
  return render_template(
          'sports/weightlifting.html')

@app.route('/sports/wrestling_freestyle')
def wrestling_freestyle():
  return render_template(
          'sports/wrestling_freestyle.html')

@app.route('/sports/wrestling_greco_roman')
def wrestling_greco_roman():
  return render_template(
          'sports/wrestling_greco_roman.html')

@app.route('/sports/alpine_skiing')
def alpine_skiing():
  return render_template(
          'sports/alpine_skiing.html')

@app.route('/sports/biathlon')
def biathlon():
  return render_template(
          'sports/biathlon.html')

@app.route('/sports/bobsleigh')
def bobsleigh():
  return render_template(
          'sports/bobsleigh.html')

@app.route('/sports/cross_country_skiing')
def cross_country_skiing():
  return render_template(
          'sports/cross_country_skiing.html')

@app.route('/sports/curling')
def curling():
  return render_template(
          'sports/curling.html')

@app.route('/sports/figure_skating')
def figure_skating():
  return render_template(
          'sports/figure_skating.html')

@app.route('/sports/freestyle_skiing')
def freestyle_skiing():
  return render_template(
          'sports/freestyle_skiing.html')

@app.route('/sports/ice_hockey')
def ice_hockey():
  return render_template(
          'sports/ice_hockey.html')

@app.route('/sports/luge')
def luge():
  return render_template(
          'sports/luge.html')

@app.route('/sports/nordic_combined')
def nordic_combined():
  return render_template(
          'sports/nordic_combined.html')

@app.route('/sports/short_track')
def short_track():
  return render_template(
          'sports/short_track.html')

@app.route('/sports/skeleton')
def skeleton():
  return render_template(
          'sports/skeleton.html')

@app.route('/sports/ski_jumping')
def ski_jumping():
  return render_template(
          'sports/ski_jumping.html')

@app.route('/sports/snowboard')
def snowboard():
  return render_template(
          'sports/snowboard.html')

@app.route('/sports/speed_skating')
def speed_skating():
  return render_template(
          'sports/speed_skating.html')

@app.route('/sports/basque_pelota')
def basque_pelota():
  return render_template(
          'sports/basque_pelota.html')




os.system('python sports/sports.py')
            
    # return render_template(
    #         'home.html', other_param1='hello', other_param2='hey')

#if __name__ == '__main__':
    # This is used when running locally only. When deploying to Google App
    # Engine, a webserver process such as Gunicorn will serve the app. This
    # can be configured by adding an `entrypoint` to app.yaml.
#    app.run(host='127.0.0.1', port=8080, debug=True)
# [END gae_python37_app]
