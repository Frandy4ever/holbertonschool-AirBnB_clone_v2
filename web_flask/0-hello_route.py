#!/usr/bin/python3
"""
This script starts a simple Flask web application.

The web application listens on 0.0.0.0, port 5000, and has a single route:
- /: displays "Hello HBNB!"

Installation of Flask is required:
    pip install Flask
"""

from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """Route handler for the root path."""
    return 'Hello HBNB!'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
