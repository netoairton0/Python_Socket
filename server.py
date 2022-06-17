import socket

IP_ADDRESS = '127.0.0.1'

PORT = 8000

MY_SERVER = (IP_ADDRESS, PORT)

tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

test = ''

tcp.bind(MY_SERVER)
tcp.listen(1)

connection, client = tcp.accept()

print(client , 'is connected!')

while True:
    message = connection.recv(2048)
    if test != message:
        print('<', message.decode("utf-8"), '>', 'Client:', client)
    
connection.close()
tcp.close()