#!/usr/bin/python3
# -*- coding: utf-8 -*-
""" script to start Flash Web Application """

from models import storage
from models.state import State

from flask import Flask, render_template
app = Flask(__name__)


@app.teardown_appcontext
def appcontext_teardown(self):
    """getting data on storage"""
    storage.close()


@app.route('/states_list', strict_slashes=False)
def state_lists():
    """Display a HTML page containing states"""
    return render_template('7-states_list.html',
                           states=storage.all(State))


if __name__ == '__main__':
    app.run(host="0.0.0.0")
