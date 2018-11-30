import socket


def test(a: str, b: int) -> int:
    print(a)
    print(b)
    return b


def main():
    # test("1", 2)
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    udp_socket.bind(("", 7890))
    # udp_socket.sendto(b"hahaha", ("localhost", 8080))
    while True:
        send_data = input("input send message")
        if send_data == "exit":
            udp_socket.close()
            return
        udp_socket.sendto(send_data.encode("utf-8"), ("localhost", 8080))


if __name__ == '__main__':
    main()
