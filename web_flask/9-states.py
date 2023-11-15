#!/usr/bin/python3
"""
Script that starts a Flask web application
"""
from flask import Flask, render_template
from models import storage
from models.state import State
from models.city import City

app = Flask(__name__)


@app.route('/states', strict_slashes=False)
def states():
    """Display a HTML page with a list of all State objects"""
    states = storage.all(State).values()
    return render_template('9-states.html', state=states)


@app.route('/states/<id>', strict_slashes=False)
def state_cities(id):
    """Display a HTML page with cities of a specific State"""
    state = storage.get(State, id)
    if state:
        return render_template('state_cities.html', state=state)
    else:
        return render_template('not_found.html')


@app.teardown_appcontext
def close_session(exception):
    """After each request you must remove the current SQLAlchemy Session"""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
