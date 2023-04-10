import socket
import random

BUFSIZE = 1024
port = 9000

server = socket.create_connection(('localhost',port))

while True:
    data = server.recv(BUFSIZE)
    if not data:
        break
    print(data.decode())
    if data.decode() == 'quit':
        server.send('device1 quit'.encode())
        break
    else:
        temp = str(random.randrange(0,41))
        hum = str(random.randrange(0,101))
        light = str(random.randrange(70,151))
        msg = '/'.join([temp,hum,light])
        server.send(msg.encode())

server.close()