import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
addr = ('localhost', 9000)

sock.connect(addr)

msg = sock.recv(1024)
print(msg.decode())

sock.send(b'Doyeop Kim')# 이름 전송
num = sock.recv(1024)# 학번 출력
print(num.decode())

sock.close()