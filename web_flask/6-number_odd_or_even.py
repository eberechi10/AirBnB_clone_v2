#!/usr/bin/python3
"""script to start Flask web app"""

from flask import Flask, render_template
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """Return string Hello HNBN"""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Returns string HNBN"""
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def cT(text):
    """display C follow by value of text variable"""
    return "C {}".format(text.replace("_", " "))


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def pythonText(text="is cool"):
    """display Python follow by value of text variable"""
    return "Python {}".format(text.replace("_", " "))


@app.route('/number/<int:n>', strict_slashes=False)
def isNumber(n):
    """display “n is a number” when n is an integer"""
    if isinstance(n, int):
        return "{} is a number".format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n=None):
    """display a HTML page when n is an integer"""
    if isinstance(n, int):
        return render_template("5-number.html", n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def number_odd_or_even(n=None):
    """display a HTML page when n is an integer:
    H1 tag: “Number: n is even|odd” inside the tag BODY
    """
    if isinstance(n, int):
        if n % 2:

            eo = "odd"
        else:
            eo = "even"

        return render_template("6-number_odd_or_even.html", n=n, eo=eo)


if __name__ == "__main__":
    app.run(host="0.0.0.0")
