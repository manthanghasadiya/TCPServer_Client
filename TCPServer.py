import socket

IP = "127.0.0.1"
Port = 49668

sendthis = "msg received"

TCPserver = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
TCPserver.bind((IP,Port))

print("Server is listening...")

TCPserver.listen()

connection, addr = TCPserver.accept()

while True:
    msg = connection.recv(1024)
    connection.sendall(msg)
