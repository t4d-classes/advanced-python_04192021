""" rate server module """
from typing import Optional
import multiprocessing as mp
import sys


def rate_server() -> None:
    """rate server"""
    while True:
        pass


class RateServerError(Exception):
    """ rate server error class """


def command_start_server(server_process: Optional[mp.Process]) -> None:
    """ command start server """

    if server_process and server_process.is_alive():
        print("server is already running")
    elif server_process:
        # step 3 - start the "server_process"
        print("server started")
    else:
        raise RateServerError("server process cannot be null")


def command_stop_server(server_process: Optional[mp.Process]) -> None:
    """ command stop server """

    if not server_process or not server_process.is_alive():
        print("server is not running")
    else:
        server_process.terminate()
        print("server stopped")


def main() -> None:
    """Main Function"""

    try:

        server_process: Optional[mp.Process] = None

        while True:

            command = input("> ")

            if command == "start":
                # step 1 - create a new process object and assign to
                # "server_process"
                command_start_server(server_process)
            elif command == "stop":
                command_stop_server(server_process)
                server_process = None
            # step 4 - add a command named "status" that outputs to the
            # console if the server is current running or not
            # hint: follow the command function pattern used by the other
            # commands
            elif command == "exit":
                # step 2 - terminate the "server_process" if the
                # "server_process" is an object and is alive
                break

    except KeyboardInterrupt:
        # step 5 - terminate the "server_process" if the
        # "server_process" is an object and is alive
        pass

    sys.exit(0)


if __name__ == '__main__':
    main()
