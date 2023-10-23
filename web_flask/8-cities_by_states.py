#!/usr/bin/python3
# -*- coding: utf-8 -*-

""" script to start Flash Web App """
from models import storage

from models.state import State
from flask import Flask, render_template

app = Flask(__name__)


@app.teardown_appcontext
def appcontext_teardown(self):
    """storage to get data from storage """
    storage.close()


@app.route('/cities_by_states', strict_slashes=False)
def state_lists():
    """Display a HTML page containing states"""
    return render_template('8-cities_by_states.html',
                           states=storage.all(State))


if __name__ == '__main__':
    app.run(host="0.0.0.0")
