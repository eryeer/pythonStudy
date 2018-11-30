import socket


def main():
    tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcp_socket.connect(('127.0.0.1', 7979))
    tcp_socket.send("README".encode('utf-8'))
    data = tcp_socket.recv(1024 * 1024)
    try:
        with open('[new]README', "wb") as file:
            file.write(data)
    except Exception:
        raise Exception("file fail")


if __name__ == '__main__':
    main()
