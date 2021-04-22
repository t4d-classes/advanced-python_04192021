""" rate server module """
from typing import Optional, Any
from multiprocessing.sharedctypes import Synchronized  # type: ignore
from datetime import datetime, date
from decimal import Decimal
import multiprocessing as mp
import socket
import threading
import sys
import re
import json
import requests
import pyodbc

RATESAPP_CONN_OPTIONS = [
    "DRIVER={ODBC Driver 17 for SQL Server}",
    "SERVER=localhost\\SQLExpress",
    "DATABASE=ratesapp",
    "UID=sa",
    "PWD=sqldbpass",
]

RATESAPP_CONN_STRING = ";".join(RATESAPP_CONN_OPTIONS)

CLIENT_COMMAND_PARTS = [
    r"^(?P<name>[A-Z]*) ",
    r"(?P<date>[0-9]{4}-[0-9]{2}-[0-9]{2}) ",
    r"(?P<symbols>[A-Z,:;|]*)$",
]

CLIENT_COMMAND_REGEX = re.compile("".join(CLIENT_COMMAND_PARTS))


def get_rate_from_api(closing_date: date, currency_symbol: str,
                      currency_rates: list[tuple[date, str, Decimal]]) -> None:
    """ get rate from api """

    url = "".join([
        "https://api.ratesapi.io/api/",
        closing_date.strftime("%Y-%m-%d"),
        "?base=USD&symbols=",
        currency_symbol,
    ])

    response = requests.request("GET", url)

    rate_data = json.loads(response.text)

    currency_rates.append(
        (closing_date,
         currency_symbol,
         Decimal(str(rate_data["rates"][currency_symbol]))))


class ClientConnectionThread(threading.Thread):
    """ client connection thread """

    def __init__(self,
                 conn: socket.socket,
                 client_count: Synchronized,
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

                client_command_str: str = data.decode('UTF-8')

                client_command_match = CLIENT_COMMAND_REGEX.match(
                    client_command_str)

                if not client_command_match:
                    self.conn.sendall(b"Invalid Command Format")
                else:
                    self.process_client_command(
                        client_command_match.groupdict())

        except OSError:
            pass

        with self.client_count.get_lock():
            self.client_count.value -= 1

    def process_client_command(self, client_command: dict[str, Any]) -> None:
        """ process client command """

        if client_command["name"] == "GET":

            with pyodbc.connect(RATESAPP_CONN_STRING) as con:

                closing_date = datetime.strptime(
                    client_command["date"], "%Y-%m-%d")

                currency_symbols_re = re.compile(r"[,:;|]")

                currency_symbols = currency_symbols_re.split(
                    client_command["symbols"])

                sql_params: list[Any] = [closing_date]
                sql_params.extend(currency_symbols)

                placeholders = ",".join("?" * len(currency_symbols))

                sql = " ".join([
                    "select closingdate, currencysymbol, exchangerate",
                    "from rates",
                    "where closingdate = ? ",
                    f"and currencysymbol in ({placeholders})"])

                cached_currency_symbols: set[str] = set()

                rate_responses = []

                with con.cursor() as cur:

                    for rate in cur.execute(sql, sql_params):
                        cached_currency_symbols.add(rate.currencysymbol)
                        exchange_rate = str(rate.exchangerate)
                        rate_responses.append(
                            f"{rate.currencysymbol}: {exchange_rate}")

                currency_rate_threads: list[threading.Thread] = []
                currency_rates: list[tuple[date, str, Decimal]] = []

                for currency_symbol in currency_symbols:
                    if currency_symbol not in cached_currency_symbols:

                        currency_rate_thread = threading.Thread(
                            target=get_rate_from_api,
                            args=(closing_date,
                                  currency_symbol, currency_rates))

                        currency_rate_thread.start()
                        currency_rate_threads.append(currency_rate_thread)

                for currency_rate_thread in currency_rate_threads:
                    currency_rate_thread.join()

                if len(currency_rates) > 0:

                    with con.cursor() as cur:

                        sql = " ".join([
                            "insert into rates",
                            "(closingdate, currencysymbol, exchangerate)",
                            "values",
                            "(?, ?, ?)",
                        ])

                        cur.executemany(sql, currency_rates)

                    for currency in currency_rates:
                        rate_responses.append(
                            f"{currency[1]}: {currency[2]}")

                self.conn.sendall(
                    "\n".join(rate_responses).encode("UTF-8"))
        else:
            self.conn.sendall(b"Invalid Command Name")


def rate_server(host: str, port: int, client_count: Synchronized) -> None:
    """rate server"""

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as socket_server:

        socket_server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        socket_server.bind((host, port))
        socket_server.listen(100)

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


def command_client_count(client_count: int) -> None:
    """ command client count """

    print(f"client count: {client_count}")


def command_clear_cache() -> None:
    """ command clear cache """

    with pyodbc.connect(RATESAPP_CONN_STRING) as con:
        con.execute("delete from rates")

    print("cache cleared")


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
            elif command == "count":
                command_client_count(client_count.value)
            elif command == "clear":
                command_clear_cache()
            elif command == "exit":
                if server_process and server_process.is_alive():
                    server_process.terminate()
                break

    except KeyboardInterrupt:
        if server_process and server_process.is_alive():
            server_process.terminate()

    sys.exit(0)


if __name__ == '__main__':
    main()
