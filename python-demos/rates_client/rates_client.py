""" rates client module """

from datetime import date
import requests
import time

from datetime_demos.business_days import business_days

def main() -> None:
    """ main """

    responses: list[str] = []

    for working_day in business_days(date(2019,1,1), date(2019,2,28)):
        working_day_str = working_day.strftime("%Y-%m-%d")
        url = "".join([
            #"https://api.ratesapi.io/api/",
            "http://localhost:5000/api/",
            working_day_str,
            "?base=USD&symbols=EUR,CAD"
        ])
        response = requests.request("GET", url)
        responses.append(response.text)

    print("\n".join(responses))


if __name__ == "__main__":

    start_time = time.time()

    main()

    print(time.time() - start_time)
