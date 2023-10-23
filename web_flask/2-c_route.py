#!/usr/bin/python3
""" script to start Flask web app, listening on 0.0.0.0, port 5000
"""

from flask import Flask

app = Flask("__name__")


@app.route('/', strict_slashes=False)
def hello():
    """Return a Hello HNBN"""
    return ("Hello HBNB!")


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """Return a string HNBN"""

    return ("HBNB")


@app.route("/c/<text>", strict_slashes=False)
def cT(text):
    """it displays C followed by value text variable"""

    return "C {}".format(text.replace("_", " "))


if __name__ == "__main__":
    app.run(host="0.0.0.0")
