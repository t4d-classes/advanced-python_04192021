""" thread class """

import time

from thread_demos.my_thread_events import all_done
from thread_demos.do_it_thread import DoItThread


thread_1 = DoItThread('host', 9999, all_done)
thread_1.start()

thread_2 = DoItThread('host', 8888, all_done)
thread_2.start()

time.sleep(2)

all_done.set()
