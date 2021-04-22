""" rate server module """
from typing import Optional
from multiprocessing.sharedctypes import Synchronized # type: ignore
import multiprocessing as mp
import sys
import socket
import threading

class ClientConnectionThread(threading.Thread):
    """ client connection thread """

    def __init__(self,
                 conn: socket.socket,
                 client_count: Synchronized
                 ) -> None:
        threading.Thread.__init__(self)
        self.conn = conn
        self.client_count = client_count

    def run(self) -> None:

        self.conn.sendall(b"Connected to the Rate Server")

        try:
            while True:
                data = self.conn.recv(2048)
                if not data:
                    break
                self.conn.sendall(data)
        except OSError:
            pass

        with self.client_count.get_lock():
            self.client_count.value -= 1

def rate_server(host: str, port: int, client_count: Synchronized) -> None:
    """rate server"""

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as socket_server:

        socket_server.bind((host, port))
        socket_server.listen()

        while True:

            conn, _ = socket_server.accept()

            client_con_thread = ClientConnectionThread(conn, client_count)
            client_con_thread.start()

            with client_count.get_lock():
                client_count.value += 1

class RateServerError(Exception):
    """ rate server error class """


def command_start_server(
    server_process: Optional[mp.Process],
    client_count: Synchronized) -> Optional[mp.Process]:
    """ command start server """

    if server_process and server_process.is_alive():
        print("server is already running")
    else:
        server_process = mp.Process(
            target=rate_server, args=("127.0.0.1", 5000, client_count))
        server_process.start()
        print("server started")

    return server_process


def command_stop_server(
    server_process: Optional[mp.Process]) -> Optional[mp.Process]:
    """ command stop server """

    if not server_process or not server_process.is_alive():
        print("server is not running")
    else:
        server_process.terminate()
        server_process = None
        print("server stopped")

    return server_process

def command_server_status(server_process: Optional[mp.Process]) -> None:
    """ command server status """

    if server_process and server_process.is_alive():
        print("server is running")
    else:
        print("server is stopped")

def command_exit(server_process: Optional[mp.Process]) -> None:
    """ command exit """

    if server_process and server_process.is_alive():
        server_process.terminate()

def command_client_count(client_count: int) -> None:
    """ command client count """
    print(f"client count: {client_count}")


def main() -> None:
    """Main Function"""

    try:

        client_count: Synchronized = mp.Value('i', 0)
        server_process: Optional[mp.Process] = None

        while True:

            command = input("> ")

            if command == "start":
                server_process = command_start_server(
                    server_process, client_count)
            elif command == "stop":
                server_process = command_stop_server(server_process)
            elif command == "status":
                command_server_status(server_process)
            elif command =="count":
                command_client_count(client_count.value)
            elif command == "exit":
                command_exit(server_process)
                break # exits the while loop

    except KeyboardInterrupt:
        command_exit(server_process)

    sys.exit(0)


if __name__ == '__main__':
    main()
