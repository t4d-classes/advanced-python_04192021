""" business days module """

from datetime import timedelta, date
from collections.abc import Generator
import holidays

def business_days_list(start_date: date, end_date: date) -> list[date]:
    """ business days func """

    working_days = []

    us_holidays = holidays.UnitedStates()

    for num in range((end_date - start_date).days + 1):
        the_date = start_date + timedelta(days=num)
        if (the_date.weekday() < 5) and (the_date not in us_holidays):
            working_days.append(the_date)

    return working_days

def business_days(start_date: date, end_date: date) -> Generator[
    date, None, None]:
    """ business days func """

    us_holidays = holidays.UnitedStates()

    for num in range((end_date - start_date).days + 1):
        the_date = start_date + timedelta(days=num)
        if (the_date.weekday() < 5) and (the_date not in us_holidays):
            print("in the generator")
            yield the_date


def main() -> None:
    """ main """

    start_date = date(2021, 7, 1)
    end_date = date(2021, 7, 7)

    for working_day in business_days(start_date, end_date):
        print("in the loop")
        print(working_day.strftime("%Y-%m-%d"))

    print("\n".join([ working_day.strftime("%Y-%m-%d")
        for working_day in business_days(start_date, end_date)]))

if __name__ == "__main__":
    main()