""" server module """

import socket

with socket.socket(
    socket.AF_INET,
    socket.SOCK_STREAM) as socket_server:

    socket_server.bind(('127.0.0.1', 5000))
    socket_server.listen()

    conn, addr = socket_server.accept()

    data_str = "Connected to the server."
    data_bytes: bytes = data_str.encode("UTF-8")
    data_str_len: int = len(data_str)
    data_bytes_len: int = len(data_bytes)
    data_bytes_sent: int = 0

    header = f"Content-Length: {data_str_len};"

    conn.send(header.encode('UTF-8'))

    # sendall does this code below
    while data_bytes_sent < data_bytes_len:
        data_bytes_sent = data_bytes_sent + conn.send(
            data_bytes[data_bytes_sent:])
    
    

    # data_len: int = len(data) - 1
    # data_sent: int = 0

    # print(data_len)
    # conn.send(data_len.to_bytes(8, 'big'))
    # conn.sendall(data_len.to_bytes(8, 'big'))

    # conn.sendall(data) # - does what the following two lines of code do
    # while data_sent < data_len:
        # data_sent = data_sent + conn.send(data[data_sent:])

    # client_msg = conn.recv(1024)

    # print(client_msg.decode("UTF-8"))
    # print(client_msg)

    # conn.sendall(client_msg)
