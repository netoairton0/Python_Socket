import socket

IP_SERVER = '127.0.0.1'

SERVER_PORT = 8000

tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

DESTINY = (IP_SERVER, SERVER_PORT)

tcp.connect(DESTINY)

while True:
    message = input()
    tcp.send(bytes(message, "utf-8"))

tcp.close()