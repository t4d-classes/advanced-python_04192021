from concurrent.futures import ThreadPoolExecutor, wait, FIRST_COMPLETED
from random import randint
import time
import threading


def task() -> str:
    """ task """
    my_thread = threading.current_thread()
    print(f"starting task {my_thread.ident}")
    time.sleep(randint(1,5))
    print(f"stopping task {my_thread.ident}")
    return f"thread {my_thread.ident} wins!"


with ThreadPoolExecutor(max_workers=3) as executor:

    for future in wait(
        [executor.submit(task) for _ in range(3)],
        return_when=FIRST_COMPLETED).done:
        
        print(future.result())