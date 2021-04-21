""" do it thread module """

import threading

# from thread_demos.my_thread_events import all_done

class DoItThread(threading.Thread):
    """ do it thread """

    def __init__(self, host: str, port: int, all_done: threading.Event) -> None:
        threading.Thread.__init__(self)
        self.host = host
        self.port = port
        self.all_done = all_done

    def run(self) -> None:

        print(f"Starting Thread Id: {self.ident}")
        print(f"Host: {self.host}")
        print(f"Port: {self.port}")

        while not self.all_done.is_set():
            pass

        print(f"Exiting Thread Id: {self.ident}")

