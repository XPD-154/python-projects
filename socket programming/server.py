import socket

server = socket.socket()
print('Socket Created')

server.bind(('localhost', 9999))

server.listen(3)
print('waiting for connections')

while True:
    client, addr = server.accept()

    name = client.recv(1024).decode()

    print("Connected with", addr, name)

    client.send(bytes('welcome','utf-8'))

    client.close()
