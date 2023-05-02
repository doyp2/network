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
        server.send('device2 quit'.encode())
        break
    else:
        heart = str(random.randrange(40,141))
        step = str(random.randrange(2000,6001))
        cal = str(random.randrange(1000,4001))
        msg = '/'.join([heart,step,cal])
        server.send(msg.encode())

server.close()