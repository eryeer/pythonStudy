import socket
import re
import threading


def service_client(new_socket):
    request = new_socket.recv(1024)
    request_lines = request.decode('utf-8').splitlines()
    print(request_lines)
    file_name = re.match(r"[^/]+(/[^ ]*)", request_lines[0]).group(1)

    if file_name == "/":
        file_name = "./html" + "/index.html"
    else:
        file_name = "./html" + file_name

    try:
        file = open(file_name, "rb")
    except Exception as ret:
        response = "HTTP/1.1 404 NOT FOUND\r\n"
        response += "\r\n"
        response += "can not find the page"
        new_socket.send(response.encode('utf-8'))
    else:
        response = "HTTP/1.1 200 OK\r\n"
        response += "\r\n"
        new_socket.send(response.encode('utf-8'))
        new_socket.send(file.read())
    finally:
        new_socket.close()


def main():
    """用来完成整体的控制"""
    tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 设置当服务器先close 即服务器端4次挥手之后资源能够立即释放，这样就保证了，下次运行程序时 可以立即绑定7788端口
    tcp_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    tcp_socket.bind(("", 7890))
    tcp_socket.listen(128)
    while True:
        new_socket, client_addr = tcp_socket.accept()
        process = threading.Thread(target=service_client, args=(new_socket,))
        process.start()
    tcp_socket.close()


if __name__ == '__main__':
    main()
 