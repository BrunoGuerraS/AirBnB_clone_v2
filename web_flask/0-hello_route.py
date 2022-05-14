#!/usr/bin/python3
"""
we start work with flask
"""
from flask import Flask

app = Flask(__name__)

@app.route('/', strict_slashes=False)
def initFlask():
    ''' print message '''
    return “Hello HBNB!”


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
