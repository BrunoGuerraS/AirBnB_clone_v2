#!/usr/bin/python3
"""
handler diferents routes
"""
from email.policy import strict
from flask import Flask

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
def replaceText(text):
    ''' replace text from search bar'''
    return "C {}".format(text.replace('_', ' '))


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
