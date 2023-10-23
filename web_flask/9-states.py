#!/usr/bin/python3
""" script for Flask running web app"""

from flask import Flask, render_template
from models import storage

from models.state import State


app = Flask(__name__)


@app.teardown_appcontext
def close(self):
    """ module for closing """
    storage.close()


@app.route('/states', strict_slashes=False)
def state():
    """Displays the lists of states"""
    states = storage.all(State)

    return render_template('9-states.html', states=states, mode='all')


@app.route('/states/<id>', strict_slashes=False)
def state_id(id):
    """Displays the lists of citys of that state"""
    for state in storage.all(State).values():
        if state.id == id:
            return render_template('9-states.html', states=state, mode='id')

    return render_template('9-states.html', states=state, mode='none')


if __name__ == '__main__':
    app.run(host="0.0.0.0")
