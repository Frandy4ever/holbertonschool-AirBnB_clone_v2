#!/usr/bin/python3
"""
This script starts a Flask web application.

The web application listens on 0.0.0.0, port 5000, and has a two routes:
- /: displays "Hello HBNB",
- /hbnb: displays 'HBNB'

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


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
