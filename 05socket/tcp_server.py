import socket


def main():
    tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    addr = ('', 7878)
    tcp_socket.bind(addr)
    tcp_socket.listen(128)
    while True:
        print("等待新的客户端")
        client_socket, client_addr = tcp_socket.accept()
        print(client_addr)
        recv_data = client_socket.recv(1024)
        print(recv_data)
        client_socket.send("ja".encode('utf-8'))
        client_socket.close()
    tcp_socket.close()


if __name__ == '__main__':
    main()
