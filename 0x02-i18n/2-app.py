#!/usr/bin/env python3
""" task 2 """
from flask import Flask, render_template, request
from flask_babel import Babel


app = Flask(__name__)


class Config(object):
    """ base conf class """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)
babel = Babel(app)


@babel.localeselector
def get_locale():
    """ fn to determines the best match with our supported languages """
    return request.accept_languages.best_match[Config.LANGUAGES]


@app.route("/")
def hello_world():
    """ define basic hello workd route"""
    return render_template('0-index.html')


if __name__ == '__main__':
    app.run()
