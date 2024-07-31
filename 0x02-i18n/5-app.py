#!/usr/bin/env python3
""" task 5 """
from flask import Flask, render_template, request, g
from flask_babel import Babel
from typing import Dict, Union


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


class Config(object):
    """ base conf class """
    DEBUG = True
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app = Flask(__name__)
app.config.from_object(Config)
app.url_map.strict_slashes = False
babel = Babel(app)


@babel.localeselector
def get_locale() -> str:
    """ fn to determines the best match with our supported languages """
    locale = request.args.get('locale')
    if locale in app.config['LANGUAGES']:
        return locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])


def get_user(ID) -> Union[Dict, None]:
    """
    returns a user dictionary or None
    if the ID cannot be found or if login_as was not passed
    """
    if ID :
        return users.get(int(ID))
    return None


@app.before_request
def before_request() -> None:
    """
    use get_user to find a user if any,
    and set it as a global on flask.g.user
    """
    id = request.args.get('login_as')
    g.user = get_user(id)


@app.route("/")
def hello_world():
    """ define basic hello workd route"""
    return render_template('5-index.html')


if __name__ == '__main__':
    app.run()
