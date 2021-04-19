""" app module """

from typing import Any
from flask import Flask

app = Flask(__name__)

@app.route("/")
def rates_by_date() -> Any:
    """ rates by date endpoint """
    return "Hello, World!"
