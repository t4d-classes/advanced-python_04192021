""" rate client module """
import socket
import sys

from rates_shared.utils import read_config


def main() -> None:
    """Main Function"""

    try:
        config = read_config()
        host = config["server"]["host"]
        port = int(config["server"]["port"])

        with socket.socket(
                socket.AF_INET, socket.SOCK_STREAM) as client_socket:
            client_socket.connect((host, port))

            print(client_socket.recv(2048).decode("UTF-8"))

            while True:

                command = input("> ")

                if command == "exit":
                    break
                else:
                    client_socket.sendall(command.encode("UTF-8"))
                    print(client_socket.recv(2048).decode("UTF-8"))

            client_socket.close()
    except ConnectionResetError:
        print("Server connection was closed.")
    except ConnectionRefusedError:
        print("Server is not running.")
    except KeyboardInterrupt:
        pass

    sys.exit(0)


if __name__ == '__main__':
    main()
