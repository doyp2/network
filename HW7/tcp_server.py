import socket
import time
import threading

def handler(cs,ca):
    while True:
        data = cs.recv(1024)
        if 'quit' in data.decode():
            if [cs,ca] in clients:
                print(ca,'exited')
                clients.remove([cs,ca])
                continue
        if [cs,ca] not in clients:
            print('new client', ca)
            clients.append([cs,ca])
        print(time.asctime()+str(ca)+':'+data.decode())
        for client in clients:
            if client[1] != ca:
                client[0].send(data)

clients = []
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('',2500))
s.listen(10)

print('Server Started')

while True:
    cs, ca = s.accept()
    th = threading.Thread(target=handler, args=(cs,ca))
    th.start()