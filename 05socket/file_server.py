import socket


def read_file(file_name):
    data = None
    try:
        file = open(file_name, 'rb')
        data = file.read()
        file.close()
    except Exception as ret:
        print("open failed %s" % ret)
    return data


def main():
    tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcp_socket.bind(('', 7979))
    tcp_socket.listen(128)
    new_socket, addr = tcp_socket.accept()
    recv = new_socket.recv(1024)
    print("receive %s" % recv.decode('utf-8'))
    data_bytes = read_file(recv.decode('utf-8'))
    if data_bytes:
        new_socket.send(data_bytes)

    new_socket.close()
    tcp_socket.close()


if __name__ == '__main__':
    main()
