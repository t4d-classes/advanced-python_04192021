""" rate client module """
import sys
import socket

def client(host: str, port: int) -> None:
    """ client """

    try:
        with socket.socket(
            socket.AF_INET, socket.SOCK_STREAM) as socket_client:

            socket_client.connect((host, port))

            print(socket_client.recv(2048).decode("UTF-8"))

            while True:

                command = input("> ")

                if command == "exit":
                    break
                else:
                    if not command:
                        continue
                    socket_client.sendall(command.encode("UTF-8"))
                    print(socket_client.recv(2048).decode("UTF-8"))

    except ConnectionResetError:
        print("Server connection is closed.")

    except KeyboardInterrupt:
        pass

client("127.0.0.1", 5000)

sys.exit(0)
