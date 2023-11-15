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

from flask import Flask, render_template

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


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """Route handler for the /number/<n> path."""
    return "{} is a number".format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """Check if n is an integer and render HTML template """
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def number_odd_or_even(n):
    """
    Check if n is an integer and render HTML template with
    even/odd information
    """
    return render_template('6-number_odd_or_even.html', n=n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
