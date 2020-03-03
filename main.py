from flask import Flask, render_template
import json
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

    data = None
    with open("venues.json") as f:
        data = json.load(f)
    obj = json.dumps(data, indent=4, sort_keys=True)

    return render_template(
            'venues.html', obj=data)

@app.route('/venues/select')
def select():
    key= request.args.get('game')#yearseason
    data = None
    with open("venues.json") as f:
        data = json.load(f)
        
    obj = json.dumps(data[key], indent=4, sort_keys=True)

    return render_template(
            'venues.html', obj=data)


if __name__ == '__main__':
    # This is used when running locally only. When deploying to Google App
    # Engine, a webserver process such as Gunicorn will serve the app. This
    # can be configured by adding an `entrypoint` to app.yaml.
    app.run(host='127.0.0.1', port=8080, debug=True)
# [END gae_python37_app]
