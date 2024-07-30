#!/usr/bin/env python3
""" task 2 """
from flask import Flask, render_template, request
from flask_babel import Babel


app = Flask(__name__)


class Config(object):
    """ base conf class """
    DEBUG = True
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)
app.url_map.strict_slashes = False
babel = Babel(app)


@babel.localeselector
def get_locale() -> str:
    """ fn to determines the best match with our supported languages """
    return request.accept_languages.best_match[app.config.LANGUAGES]


@app.route("/")
def hello_world():
    """ define basic hello workd route"""
    return render_template('2-index.html')


if __name__ == '__main__':
    app.run()
