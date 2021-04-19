""" rates client module """

import json
import requests


def main() -> None:
    """ main """
    
    url = "http://localhost:5000/api/2021-04-01?base=USD&symbols=EUR,CAD"

    response = requests.request("GET", url)

    rates = json.loads(response.text)

    print(rates)


if __name__ == "__main__":
    main()
