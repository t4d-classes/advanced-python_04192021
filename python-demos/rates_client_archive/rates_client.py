""" rates client module """

from datetime import date, datetime
from typing import TypedDict
import time
import threading
import queue
import json
import pathlib
import csv

import requests
from datetime_demos.business_days import business_days

responses_done = threading.Event()
processed_responses_done = threading.Event()

class Rate(TypedDict):
    """ rate typed dictionary """
    closing_date: date
    eur: float

def get_rates(working_day: date, responses: queue.Queue[str]) -> None:
    """ get rates """

    working_day_str = working_day.strftime("%Y-%m-%d")
    url = "".join([
        "https://api.ratesapi.io/api/",
        # "http://localhost:5000/api/",
        working_day_str,
        "?base=USD&symbols=EUR"
    ])
    response = requests.request("GET", url)
    print(f"getting rate for {working_day}")
    responses.put(response.text)

def process_rate(
    responses: queue.Queue[str],
    processed_responses: queue.Queue[Rate]) -> None:
    """ process rates into a typed dictionary """

    while True:
        try:
            rate_data = responses.get(timeout=0.1)
            rate = json.loads(rate_data)
            print(f"processing rate for {rate['date']}")
            processed_responses.put({
                "closing_date": datetime.strptime(rate["date"], "%Y-%m-%d"),
                "eur": rate["rates"]["EUR"]
            })
            responses.task_done()
        except queue.Empty:
            if responses_done.is_set():
                break
            else:
                continue

def save_rates(processed_responses: queue.Queue[Rate]) -> None:
    """ saves rates to a csv file """

    with open(pathlib.Path("output", "euro-rates.csv"),
            "w", newline="\n") as rates_file:

        rates_csv = csv.writer(rates_file)
        while True:
            try:
                rate = processed_responses.get(timeout=0.1)
                rates_csv.writerow(rate.values())
                processed_responses.task_done()
            except queue.Empty:
                if processed_responses_done.is_set():
                    break
                else:
                    continue

def main() -> None:
    """ main """

    responses: queue.Queue[str] = queue.Queue()
    processed_responses: queue.Queue[Rate] = queue.Queue()
    threads: list[threading.Thread] = []

    process_rate_thread = threading.Thread(
        target=process_rate, args=(responses, processed_responses))
    process_rate_thread.start()

    save_rates_thread = threading.Thread(
        target=save_rates, args=(processed_responses,))
    save_rates_thread.start()

    for working_day in business_days(date(2019,1,1), date(2019,1,15)):
        a_thread = threading.Thread(
            target=get_rates, args=(working_day, responses))
        a_thread.start()
        threads.append(a_thread)

    for a_thread in threads:
        a_thread.join()

    responses_done.set()

    process_rate_thread.join()

    processed_responses_done.set()

    save_rates_thread.join()

if __name__ == "__main__":

    start_time = time.time()

    main()

    print(time.time() - start_time)
