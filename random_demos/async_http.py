from datetime import date, timedelta
from collections.abc import Generator
from typing import Any
import time
import json
import asyncio
import aiohttp
import holidays
import requests

rates: list[Any] = []

def business_days(start_date: date,
                  end_date: date) -> Generator[date, None, None]:
    us_holidays = holidays.UnitedStates()
    for n in range((end_date - start_date).days + 1):
        the_date = start_date + timedelta(n)
        if (the_date.weekday() < 5) and (the_date not in us_holidays):
            yield the_date

def main_sync() -> None:

    start_date = date(2019, 1, 1)
    end_date = date(2019, 2, 28)
    
    for single_date in business_days(start_date, end_date):
        single_date_str = single_date.strftime("%Y-%m-%d")
        url = f"https://api.ratesapi.io/api/{single_date_str}?base=USD&symbols=EUR,CAD"
        rates.append(json.loads(requests.request("GET", url).text))

async def main_async() -> None:

    start_date = date(2019, 1, 1)
    end_date = date(2019, 2, 28)

    async with aiohttp.ClientSession() as session:

        for single_date in business_days(start_date, end_date):
            single_date_str = single_date.strftime("%Y-%m-%d")        
            url = f'https://api.ratesapi.io/api/{single_date_str}?base=USD&symbols=EUR,CAD'
            async with session.get(url) as resp:
                rates.append(await resp.json())
                # print(rates)


start_time = time.time()
main_sync()
print(time.time() - start_time)
print(len(rates))

rates = []

start_time = time.time()
loop = asyncio.get_event_loop()
loop.run_until_complete(main_async())
print(time.time() - start_time)
print(len(rates))
