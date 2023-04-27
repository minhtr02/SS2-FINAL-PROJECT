from flask import Flask, render_template
from flask_dance.contrib.google import make_google_blueprint, google
from flask_session import Session

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecretkey'
app.config['SESSION_TYPE'] = 'filesystem'
Session(app)

blueprint = make_google_blueprint(client_id='YOUR_CLIENT_ID',
                                  client_secret='YOUR_CLIENT_SECRET',
                                  scope=['profile', 'email'])

app.register_blueprint(blueprint, url_prefix='/login')

@app.route('/')
def index():
    if not google.authorized:
        return render_template('login.html')
    resp = google.get('/oauth2/v1/userinfo')
    assert resp.ok, resp.text
    return f'You are {resp.json()["email"]}'