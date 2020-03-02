from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hello():
    """Return a friendly HTTP greeting."""
    return 'Hello World!'

#to add more pages create more of these functions with /custom-url
@app.route('/home')
def home():
    return render_template(
            'home.html')
            
    # return render_template(
    #         'home.html', other_param1='hello', other_param2='hey')

if __name__ == '__main__':
    # This is used when running locally only. When deploying to Google App
    # Engine, a webserver process such as Gunicorn will serve the app. This
    # can be configured by adding an `entrypoint` to app.yaml.
    app.run(host='127.0.0.1', port=8080, debug=True)
# [END gae_python37_app]
