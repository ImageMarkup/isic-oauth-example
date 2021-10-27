import os

from flask import Flask, render_template
from flask_dance.consumer import OAuth2ConsumerBlueprint

app = Flask(__name__)
app.secret_key = os.environ['SECRET_KEY']

isic_oauth = OAuth2ConsumerBlueprint(
    'isic-oauth',
    __name__,
    client_id=os.environ['OAUTH_CLIENT_ID'],
    client_secret=os.environ['OAUTH_CLIENT_SECRET'],
    base_url=os.environ['OAUTH_BASE_URL'],
    token_url=f'{os.environ["OAUTH_BASE_URL"]}/oauth/token/',
    authorization_url=f'{os.environ["OAUTH_BASE_URL"]}/oauth/authorize',
    redirect_url=os.environ['OAUTH_REDIRECT_URL'],
)
app.register_blueprint(isic_oauth, url_prefix='/login')


@app.route('/')
def index():
    ctx = {'logged_in': False}

    if isic_oauth.session.authorized:
        resp = isic_oauth.session.get('/api/v2/users/me')
        ctx['logged_in'] = True
        ctx['me'] = resp.json()

    return render_template('index.html', **ctx)
