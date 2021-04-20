""" cpu bound single demo """

from collections.abc import Generator
import itertools
import time

def fibonacci() -> Generator[int, None, None]:
    """ generate an infinite fibonacci sequence """

    num_1 = 0
    num_2 = 1

    yield num_1
    yield num_2

    while True:

        next_num = num_1 + num_2
        yield next_num
        num_1 = num_2
        num_2 = next_num

def calc_fib_total(p_results: list[int]) -> None:
    """ calc fib total and add to list """

    total = 0
    for num in itertools.islice(fibonacci(), 0, 500000):
        total += num
    p_results.append(total)

if __name__ == "__main__":

    start_time = time.time()

    results: list[int] = []

    for _ in range(8):
        calc_fib_total(results)

    time_elapsed = time.time() - start_time
   
    print(len(results))
    print(time_elapsed)
