import socket


def main():
    # create socket
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)


    # bind local info, you have to bind your local computer ip
    local_addr = ("", 8080)
    udp_socket.bind(local_addr)
    while True:
        # receive data
        data = udp_socket.recvfrom(1024)
        recv_msg = data[0]
        send_addr = data[1]
        # print data
        print("%s:%s" % (str(send_addr), recv_msg.decode("utf-8")))
    # close socket
    udp_socket.close()


if __name__ == '__main__':
    main()
