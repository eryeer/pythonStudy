from socket import *

tcp_socket = socket(AF_INET, SOCK_STREAM)
ip = "127.0.0.1"
port = 7878
tcp_socket.connect((ip, port))
data = input("pls input data")
tcp_socket.send(data.encode("utf-8"))
recv_data = tcp_socket.recv(1024)
print(recv_data.decode('utf-8'))
tcp_socket.close()
