""" rates client module """

from datetime import date
import requests
import time
import threading

from datetime_demos.business_days import business_days

def get_rates(working_day: date, responses: list[str]) -> None:

    working_day_str = working_day.strftime("%Y-%m-%d")
    url = "".join([
        "https://api.ratesapi.io/api/",
        # "http://localhost:5000/api/",
        working_day_str,
        "?base=USD&symbols=EUR"
    ])
    response = requests.request("GET", url)
    responses.append(response.text)

def main() -> None:
    """ main """

    responses: list[str] = []
    threads: list[threading.Thread] = []

    for working_day in business_days(date(2019,1,1), date(2019,2,28)):
        a_thread = threading.Thread(
            target=get_rates, args=(working_day, responses))
        a_thread.start()
        threads.append(a_thread)

    for a_thread in threads:
        a_thread.join()

    print("\n".join(responses))


if __name__ == "__main__":

    start_time = time.time()

    main()

    print(time.time() - start_time)
