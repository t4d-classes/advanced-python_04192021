""" app module """

from typing import Any
import csv
import pathlib
import math

from flask import Flask, jsonify, abort, request

rates: list[dict[str,Any]] = []

data_file_path = pathlib.Path("rates_api", "data", "eurofxref-hist.csv")

with open(data_file_path, "r") as data_file:
    data_file_csv = csv.DictReader(data_file)

    for rate_row in data_file_csv:

        rate_entry = { "Date": rate_row["Date"], "EUR": 1.0 }

        for rate_col in rate_row:
            if rate_col != "Date" and len(rate_col) > 0:
                if rate_row[rate_col] == "N/A":
                    rate_entry[rate_col] = math.nan
                else:
                    rate_entry[rate_col] = float(rate_row[rate_col])

        rates.append(rate_entry)

app = Flask(__name__)

@app.route("/api/<rate_date>")
def rates_by_date(rate_date: str) -> Any:
    """ rates by date endpoint """

    for rate in rates:

        if rate["Date"] == rate_date:

            base_country = request.args.get("base", "EUR")

            if "symbols" in request.args:
                country_symbols = request.args["symbols"].split(",")
            else:
                country_symbols = [ col for col in rate if col != "Date" ]

            country_rates = {
                country_code : country_rate / rate[base_country]
                for (country_code, country_rate) in rate.items()
                if country_code != "Date" and country_code in country_symbols
            }

            return jsonify({
                "date": rate["Date"],
                "base": base_country,
                "rates": country_rates,
            })

    abort(404)
