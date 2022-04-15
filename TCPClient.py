import socket

IP = "127.0.0.1"
Port = 49668


TCPClient = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
TCPClient.connect((IP,Port))

message = input(">")
data = bytes(message, 'utf-8')

TCPClient.sendall(data)

serverdata = str(TCPClient.recv(1024))
print("From server: ", serverdata)
