#!/usr/bin/python3
"""
This script starts a Flask web application.

The web application listens on 0.0.0.0, port 5000, and has three routes:
- /: displays "Hello HBNB",
- /hbnb: displays 'HBNB',
- /c/<text>: displays 'C' followed by the content of the `text` var,
- /python/<text>: displays 'Python' followed by the content of the `text` var

Installation of Flask is required:
    pip install Flask
"""

from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hbnb():
    """Route handler for the root path."""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hello_hbnb():
    """Route handler for the /hbnb path."""
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c(text):
    """Route handler for the /c/<text> path."""
    text = text.replace("_", " ")
    return "C {}".format(text)


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python(text="is cool"):
    """Route handler for the /python/<text> path."""
    text = text.replace("_", " ")
    return "Python {}".format(text)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
