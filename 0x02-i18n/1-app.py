#!/usr/bin/env python3
""" task 1 """
from flask import Flask, render_template
from flask_babel import Babel


app = Flask(__name__)


class Config(object):
    """ base conf class """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)
babel = Babel(app)


@app.route("/")
def hello_world():
    """ define basic hello workd route"""
    return render_template('0-index.html')


if __name__ == '__main__':
    app.run()
