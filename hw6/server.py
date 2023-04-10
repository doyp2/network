import socket
import time

BUFSIZE = 1024
port = 9000

s = socket.create_server(('', port), family=socket.AF_INET, backlog=1)
clinet1, addr1 = s.accept()
clinet2, addr2 = s.accept()

f = open('data.txt', 'w')
while True:
    msg = input("Input Message : ")
    if msg == 'quit':
        clinet1.send(msg.encode())
        clinet2.send(msg.encode())
        data1 = clinet1.recv(BUFSIZE)
        data2 = clinet2.recv(BUFSIZE)
        print(data1.decode())
        print(data2.decode())
        break
    if msg == '1':
        clinet1.send('Request'.encode())
        data = clinet1.recv(BUFSIZE)
        data = data.decode().split('/')
        # print(f'온도:{data[0]}, 습도:{data[1]}, 조도:{data[2]}')
        f.write(f'{time.asctime()}: Device1: Temp={data[0]}, Humid={data[1]}, lilum={data[2]}\n')
    elif msg == '2':
        clinet2.send('Request'.encode())
        data = clinet2.recv(BUFSIZE)
        data = data.decode().split('/')
        # print(f'심박수:{data[0]}, 걸음수:{data[1]}, 소모칼로리:{data[2]}')
        f.write(f'{time.asctime()}: Device2: Heartbeat={data[0]}, Steps={data[1]}, Cal={data[2]}\n')
    else:
        print('Input error')

s.close()
f.close()