import os

from authlib.integrations.flask_client import OAuth
from flask import Flask, redirect, render_template, session, url_for

app = Flask(__name__)
app.secret_key = os.environ['SECRET_KEY']
app.config.update(
    {
        'ISIC_CLIENT_ID': os.environ['OAUTH_CLIENT_ID'],
        'ISIC_CLIENT_SECRET': os.environ['OAUTH_CLIENT_SECRET'],
        'ISIC_ACCESS_TOKEN_URL': f'{os.environ["OAUTH_BASE_URL"].rstrip("/")}/token/',
        'ISIC_AUTHORIZE_URL': f'{os.environ["OAUTH_BASE_URL"].rstrip("/")}/authorize',
        'ISIC_API_BASE_URL': os.environ['API_BASE_URL'].rstrip('/') + '/',
        'ISIC_CLIENT_KWARGS': {
            # Enable PKCE
            'code_challenge_method': 'S256',
        },
    }
)

oauth = OAuth(app)
oauth.register('isic')


@app.route('/login')
def login():
    redirect_uri = url_for('authorize', _external=True)
    return oauth.isic.authorize_redirect(redirect_uri)


@app.route('/authorize')
def authorize():
    oauth.isic.authorize_access_token()
    resp = oauth.isic.get('users/me')
    resp.raise_for_status()
    session['user'] = resp.json()
    return redirect('/')


@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect('/')


@app.route('/')
def index():
    ctx = {'logged_in': False}

    if 'user' in session:
        ctx['logged_in'] = True
        ctx['me'] = session['user']

    return render_template('index.html', **ctx)
