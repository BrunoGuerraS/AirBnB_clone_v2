#!/usr/bin/python3
"""
handler diferents routes
"""
from email.policy import strict
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def initFlask():
    ''' home rout '''
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def gohbnb():
    ''' go to hbnb route '''
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def cisfun(text):
    ''' replace text from search bar'''
    return "C {}".format(text.replace('_', ' '))


@app.route('/python/', strict_slashes=False, defaults={'text': "is cool"})
@app.route('/python/<text>', strict_slashes=False)
def pycool(text):
    ''' show python is cool'''
    return "Python {}".format(text.replace('_', ' '))


@app.route('/number/<int:n>', strict_slashes=False)
def onlynum(n: int):
    ''' show only number'''
    return "{} is a number".format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def showTempla(n):
    ''' render our templates '''
    return render_template('5-number.html', num=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def oddoreven(n):
    ''' show depending if it's odd or even '''
    return render_template('6-number_odd_or_even.html', num=n)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
